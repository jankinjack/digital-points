import subprocess
from typing import Callable

GDB_PATH = 'gdb'
GDB_DUMP_SCRIPT = 'client/model/elf_parser/dump_globals.py'

ARCH_BYTESIZE_DICT = {
    'EM_TI_C2000': 16,
    }

ARCH_BYTESIZE = 8
ARCH_ADDR_ALIGNMENT = 1

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


class ELF_Parser:

    def __init__(self) -> None:
        super().__init__()

    def get_variables_from_elf(
        self,
        file_name: str,
        progress_callback: Callable[[float], None],
        exclude_patterns: tuple[str, ...],
    ) -> list[dict]:
        """Get list of variables from an ELF file using GDB.

        Args:
            file_name: Path to the ELF file.
            progress_callback: Callback function receiving progress percentage.
            exclude_patterns: Patterns to filter out variable names.

        Returns:
            List of variable dicts with keys: name, address, type, bytesize.
        """

        command = (
            f'{GDB_PATH} -nx -batch '
            f'-iex "set auto-load no" '
            f'-x {GDB_DUMP_SCRIPT} "{file_name}"'
            )

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                )
        except Exception:
            return []

        lines = result.stdout.split('\n')
        total_lines = len(lines)
        variables: list[dict] = []

        progress_callback(0)

        for i, line in enumerate(lines):
            parts = line.split('|')

            if len(parts) != 4:
                continue

            name, var_type, address_str, bytesize_str = parts

            try:
                address = int(address_str)
                bytesize = int(bytesize_str)
            except ValueError:
                continue

            variables.append({
                'name': name,
                'address': address,
                'type': var_type,
                'bytesize': bytesize,
                })

            progress_callback(
                100 * i / total_lines if total_lines > 0 else 100
                )

        def is_valid_variable(variable: dict) -> bool:
            """ Check if a variable passes all validation filters. """

            return (
                variable['type'] is not None
                and variable['type'] != '(unsupported)'
                and variable['name']
                and not any(s in variable['name'] for s in exclude_patterns)
                and isinstance(variable['address'], int)
                and variable['address'] >= 0
                and isinstance(variable['bytesize'], int)
                and variable['bytesize'] > 0
                )

        # Filter, deduplicate, and sort variables.
        filtered_variables = filter(is_valid_variable, variables)
        sorted_variables = sorted(
            {x['name']: x for x in filtered_variables}.values(),
            key=lambda item: item['name'].lower(),
        )

        progress_callback(100)

        return sorted_variables
