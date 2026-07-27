
import re
from pathlib import Path
from typing import Optional, Callable
from contextlib import suppress
from typing import TYPE_CHECKING

from elftools.elf.elffile import ELFFile
from elftools.dwarf.enums import DW_FORM_raw2name
from elftools.dwarf.dwarf_expr import DWARFExprParser

if TYPE_CHECKING:
    import elftools

DEFAULT_TYPE_TO_ABSTRACT = {
    'char': 'signed int',
    'signed char': 'signed int',
    'unsigned char': 'unsigned int',
    'short': 'signed int',
    'signed short': 'signed int',
    'short unsigned int': 'unsigned int',
    'short signed int': 'signed int',
    'short int': 'signed int',
    'unsigned short': 'unsigned int',
    'int': 'signed int',
    'signed int': 'signed int',
    'unsigned int': 'unsigned int',
    'long int': 'signed int',
    'long signed int': 'signed int',
    'long unsigned int': 'signed int',
    'long': 'signed int',
    'unsigned long': 'unsigned int',
    'long long int': 'signed int',
    'long long signed int': 'signed int',
    'long long unsigned int': 'unsigned int',
    'float': 'float',
    'double': 'float',
    '_Bool': 'unsigned int',
    'union': '(unsupported)',
    'pointer': '(unsupported)',
    'none': '(unsupported)',
    }

ABSTRACT_TYPE_TO_STDINT = {
    8: {
        'signed int': {
            0: '(unsupported)',
            1: 'int8_t',
            2: 'int16_t',
            4: 'int32_t',
            8: 'int64_t',
            },
        'unsigned int': {
            0: '(unsupported)',
            1: 'uint8_t',
            2: 'uint16_t',
            4: 'uint32_t',
            8: 'uint64_t',
            },
        'float': {
            0: '(unsupported)',
            4: 'float32_t',
            8: 'float64_t',
            },
        '(unsupported)': {
            0: '(unsupported)',
            1: '(unsupported)',
            2: '(unsupported)',
            4: '(unsupported)',
            8: '(unsupported)',
            }
        },
    16: {
        'signed int': {
            0: '(unsupported)',
            1: 'int16_t',
            2: 'int32_t',
            4: 'int64_t',
            },
        'unsigned int': {
            0: '(unsupported)',
            1: 'uint16_t',
            2: 'uint32_t',
            4: 'uint64_t',
            },
        'float': {
            0: '(unsupported)',
            2: 'float32_t',
            4: 'float64_t',
            },
        '(unsupported)': {
            0: '(unsupported)',
            1: '(unsupported)',
            2: '(unsupported)',
            4: '(unsupported)',
            8: '(unsupported)',
            }
        }
}

DEF_TYPES = {
    'char': 'int8_t',
    'unsigned char': 'uint8_t',
    'short': 'int16_t',
    'short unsigned int': 'uint16_t',
    'short signed int': 'int16_t',
    'short int': 'int16_t',
    'unsigned short': 'uint16_t',
    'int': 'int32_t',
    'unsigned int': 'uint32_t',
    'long int': 'int32_t',
    'long unsigned int': 'uint32_t',
    'long': 'int32_t',
    'unsigned long': 'uint32_t',
    'long long int': 'int64_t',
    'long long unsigned int': 'uint64_t',
    'float': 'float32_t',
    'double': 'float64_t',
    '_Bool': 'bool8_t',
    'union': '(unsupported)',
    'pointer': '(unsupported)',
    'none': '(unsupported)',
    }

VAR_TYPE_BITS = {
    'int8_t': 8,
    'uint8_t': 8,
    'int16_t': 16,
    'uint16_t': 16,
    'int32_t': 32,
    'uint32_t': 32,
    'int64_t': 64,
    'uint64_t': 64,
    'float32_t': 32,
    'float64_t': 64,

    'fra_t': 32,
    'immediate_t': 32,

    'none': 0,
    }

ARCH_BYTESIZE_DICT = {
    'EM_TI_C2000': 16,
    }

ARCH_BYTESIZE = 8
ARCH_ADDR_ALIGNMENT = 1


class ELF_Parser():

    def __init__(self) -> None:
        super().__init__()

    def get_variables_from_elf(
            self,
            file_name: str,
            progress_callback: Callable,
            exclude_patterns: tuple,
            ) -> list:
        """ Get list of variables. """

        with Path(file_name).open('rb') as read_file, suppress(Exception):
            elf_file = ELFFile(read_file)
            dwarf_info = elf_file.get_dwarf_info()

            unique_global_variables = {}
            for symbol in elf_file.get_section_by_name('.symtab').iter_symbols():
                entry = symbol.entry

                # Is it variable?
                if (entry.st_info.type == 'STT_OBJECT'
                        and symbol.name[0].isalpha()
                        and re.match(r'^[A-Za-z0-9_]+$', symbol.name)):
                    unique_global_variables[symbol.name] = {
                        'address': entry.st_value
                        }

            # Get variables from the file.
            variables = []
            cu_number = sum(1 for _ in dwarf_info.iter_CUs())
            for i, cu in enumerate(dwarf_info.iter_CUs()):
                variables += self.die_info_rec(
                    cu.get_top_DIE(),
                    unique_global_variables,
                    )

                progress_callback(100 * i / cu_number)

            global ARCH_BYTESIZE
            global ARCH_ADDR_ALIGNMENT

            ARCH_BYTESIZE = ARCH_BYTESIZE_DICT.get(
                elf_file.header.e_machine, 8
                )
            ARCH_ADDR_ALIGNMENT = elf_file.elfclass // ARCH_BYTESIZE

            # Assemble structs into separate variables.
            assembled_variables = []
            for variable in variables:
                assembled_variables += self.assemble_struct(
                    variable,
                    ARCH_BYTESIZE,
                    )

            # Filter variables.
            filtered_variables = filter(
                lambda x: (
                    x['type'] is not None
                    and x['type'] != '(unsupported)'
                    and x['name']
                    and not any(s in x['name'] for s in exclude_patterns)
                    and x['type'] in DEF_TYPES.values()
                    and isinstance(x['address'], (int, type(None)))
                    and x['address'] >= 0
                    and isinstance(x['bytesize'], (int, type(None)))
                    and x['bytesize'] > 0
                    ),
                assembled_variables,
                )

            # Sort and thin variables.
            sorted_variables = sorted(
                {x['name']: x for x in filtered_variables}.values(),
                key=lambda item: item['name'].lower(),
                )

            progress_callback(100)

            # Remove sensitive symbols.
            return sorted_variables

        return []

    def die_info_rec(
            self,
            die: 'elftools.DIE',
            unique_global_variables: dict,
            indent_level: int = 0,
            ) -> list:
        """ Process the DIE. """

        variables = []

        # If it is a global variable with name.
        if (indent_level == 1
                and die.tag == 'DW_TAG_variable'
                and 'DW_AT_name' in die.attributes):
            name = die.attributes['DW_AT_name'].value.decode()

            # Condition to process the variables only once.
            if name in unique_global_variables:
                info = self.type_die_rec(
                    die,
                    unique_global_variables[name]['address']
                    )

                if info is not None:
                    variables.append(info)

        child_indent = indent_level + 1
        for child in die.iter_children():
            variables += self.die_info_rec(
                child,
                unique_global_variables,
                child_indent
                )

        return variables

    def clear_typedef(
            self,
            type_die: 'elftools.DIE',
            array: bool = False,
            ) -> Optional['elftools.DIE']:
        """ Convert 'decorated' types into base types. """

        if type_die is None:
            return None

        while type_die.tag in (
                'DW_TAG_typedef',
                'DW_TAG_volatile_type',
                'DW_TAG_enumeration_type',
                'DW_TAG_const_type',
                'DW_TAG_lo_user',
                'DW_TAG_array_type' if array else None,
                ):
            type_die = self.get_die_type_attribute(type_die)

            if type_die is None:
                return None

        return type_die

    def calc_attribute_value(
            self,
            die: 'elftools.DIE',
            attribute: str
            ) -> Optional[int]:
        """ Calculate value for specific attribute. """

        if attribute not in die.attributes:
            return None

        attr = die.attributes[attribute]
        form = attr.form
        raw_value = attr.raw_value
        value = attr.value

        if form == 'DW_FORM_indirect':
            form = DW_FORM_raw2name[attr.raw_value]
            raw_value = value

        if form in {
                'DW_FORM_ref1',
                'DW_FORM_ref2',
                'DW_FORM_ref4',
                'DW_FORM_ref8',
                'DW_FORM_ref',
                'DW_FORM_ref_udata',
                }:
            return raw_value + die.cu.cu_offset
        elif form in {
                'DW_FORM_ref_addr',
                'DW_FORM_implicit_const',
                }:
            return raw_value
        elif form in {
                'DW_FORM_data1',
                'DW_FORM_data2',
                'DW_FORM_data4',
                'DW_FORM_data8',
                }:
            return value
        elif form in {
                'DW_FORM_ref_sup4',
                'DW_FORM_ref_sup8',
                'DW_FORM_GNU_ref_alt',
                }:
            if die.dwarfinfo.supplementary_dwarfinfo:
                return die.dwarfinfo.supplementary_dwarfinfo.get_DIE_from_refaddr(
                    raw_value
                    )
        elif form in {
                'DW_FORM_block',
                'DW_FORM_block1',
                'DW_FORM_block2',
                'DW_FORM_block4',
                }:
            dwarf_expr_parser = DWARFExprParser(die.cu.structs)
            parsed = dwarf_expr_parser.parse_expr(value)
            return parsed[0].args[0]

        return None

    def get_die_type_attribute(self, die: 'elftools.DIE') -> Optional['elftools.DIE']:
        try:
            return die.get_DIE_from_attribute('DW_AT_type')
        except (TypeError, NotImplementedError, KeyError):
            refaddr = self.calc_attribute_value(die, 'DW_AT_type')
            if refaddr is not None:
                return die.dwarfinfo.get_DIE_from_refaddr(refaddr)

            return None

    def type_die_rec(self, die: 'elftools.DIE', parent_address: int) -> dict:
        """ Process the type of DIE. """

        # Get the variable's name.
        # Substructures or unions inside structures may not have
        # name, so check it and replace the name by 'empty symbol'.
        if 'DW_AT_name' in die.attributes:
            name = die.attributes['DW_AT_name'].value.decode()
        else:
            name = None

        # Get the variable's type-DIE.
        type_die = self.get_die_type_attribute(die)
        type_die = self.clear_typedef(type_die)

        if type_die is None:
            return {
                'name': name,
                'type': 'none',
                'address': parent_address,
                'bytesize': 0,
            }

        elif type_die.tag == 'DW_TAG_structure_type':
            members = [
                self.type_die_rec(
                    child,
                    parent_address + self.calc_attribute_value(
                        child,
                        'DW_AT_data_member_location',
                        )
                    )
                for child in type_die.iter_children() if child.tag == 'DW_TAG_member'
                ]

            return {
                'name': name,
                'type': 'struct',
                'address': parent_address,
                'bytesize': 0,
                'members': members,
                }

        elif type_die.tag == 'DW_TAG_base_type' or type_die.tag == 'DW_TAG_lo_user':
            return {
                'name': name,
                'type': type_die.attributes['DW_AT_name'].value.decode(),
                'address': parent_address,
                'bytesize': type_die.attributes['DW_AT_byte_size'].value,
                }

        elif type_die.tag == 'DW_TAG_union_type':
            members = [
                self.type_die_rec(
                    child,
                    parent_address,
                    )
                for child in type_die.iter_children() if child.tag == 'DW_TAG_member'
                ]

            return {
                'name': name,
                'type': 'union',
                'address': parent_address,
                'bytesize': 0,
                'members': members,
                }

        elif type_die.tag == 'DW_TAG_pointer_type':
            return {
                'name': name,
                'type': 'pointer',
                'address': parent_address,
                # Get the size of pointer from info about the architecture.
                'bytesize': type_die.dwarfinfo.config.default_address_size,
                }

        elif type_die.tag == 'DW_TAG_array_type':
            item_type = self.get_die_type_attribute(type_die)

            item_type = self.clear_typedef(item_type, array=True)

            if item_type is not None:
                # Get the size of pointer from info about the architecture.
                if item_type.tag != 'DW_TAG_pointer_type':
                    item_size = item_type.attributes['DW_AT_byte_size'].value
                else:
                    item_size = item_type.dwarfinfo.config.default_address_size

                subranges = type_die.iter_children()

                array_size = []

                for subrange in subranges:
                    if 'DW_AT_upper_bound' in subrange.attributes:
                        array_size.append(
                            subrange.attributes['DW_AT_upper_bound'].value + 1
                            )
                    elif 'DW_AT_count' in subrange.attributes:
                        array_size.append(
                            subrange.attributes['DW_AT_count'].value
                            )
                    else:
                        return {
                            'name': name,
                            'type': 'none',
                            'address': parent_address,
                            'bytesize': 0,
                            }

                # Support arrays only of base types.
                if item_type.tag == 'DW_TAG_base_type':
                    return {
                        'name': ('{}' + '[{}]'*len(array_size)).format(
                            name, *array_size
                            ),
                        'type': item_type.attributes['DW_AT_name'].value.decode(),
                        'address': parent_address,
                        'bytesize': item_size,
                        }

        return {
            'name': name,
            'type': 'none',
            'address': parent_address,
            'bytesize': 0,
        }

    def assemble_struct(
            self,
            variable: dict,
            byte_size: int,
            parent_name: Optional[str] = None
            ) -> list:
        """ Assemble a structure into a separate variable. """

        if variable['type'] == 'struct' or variable['type'] == 'union':

            assembled_members = []

            for member in variable['members']:
                tmp = self.assemble_struct(member, byte_size, variable['name'])
                for member in tmp:
                    if parent_name is not None:
                        member['name'] = f"{parent_name}.{member['name']}"
                    assembled_members.append(member)

            return assembled_members

        if parent_name is not None:
            variable['name'] = f"{parent_name}.{variable['name']}"

        if variable['type'] in DEFAULT_TYPE_TO_ABSTRACT:
            abstract_type = DEFAULT_TYPE_TO_ABSTRACT[variable['type']]

            if abstract_type != '(unsupported)':
                variable['type'] = ABSTRACT_TYPE_TO_STDINT[byte_size][abstract_type][variable['bytesize']]
            else:
                variable['type'] = None

        return [variable]
