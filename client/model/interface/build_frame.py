from itertools import chain
import struct
from typing import Optional

import numpy as np

import info

from model.trigger import Trigger
from model.interface.crc16 import crc16

# Mapping of struct format characters to their byte sizes.
# Note: Indices 10 and 11 duplicate 'f' (4 bytes)
# likely for specific MCU type aliases.
PACK_SIZE = (
    ('b', 1),
    ('B', 1),
    ('h', 2),
    ('H', 2),
    ('i', 4),
    ('I', 4),
    ('q', 8),
    ('Q', 8),
    ('f', 4),
    ('d', 8),
    ('f', 4),
    ('f', 4),
    )

FUNCTION_ID = {
    '0x00':  100,
    '0x01':  101,
    '0x02':  102,
    '0x02_ack': 103,
    '0x03':  104,
    '0x04':  105,
    }

# Proprietary key appended to all frames for basic validation.
DP_KEY_STR = b'vicet'
DP_KEY = tuple(DP_KEY_STR)

# Maximum allowed length for a single FRA signal chunk in one frame
MAX_SIGNAL_CHUNK_SIZE = 20


def _finalize_frame(frame: tuple[int, ...]) -> tuple[int, ...]:
    """
    Append CRC-16 checksum and the proprietary DP_KEY to the packed frame.
    Centralizes the finalization logic for all protocol frames.
    """

    return frame + crc16(frame) + DP_KEY


def build_0x00_frame(slave_address: int) -> tuple[int, ...]:
    """ Build a frame for function 0x00 (device info and heartbeat). """

    from model.elf_file_parser import ARCH_ADDR_ALIGNMENT

    packed_data = struct.pack(
        '<BBBHHH',
        slave_address,
        FUNCTION_ID['0x00'],
        ARCH_ADDR_ALIGNMENT,
        *map(int, info.__version__.split('.'))
        )

    return _finalize_frame(tuple(packed_data))


def build_0x01_frame(
        slave_address: int,
        types: list[int] | tuple[int, ...],
        addresses: list[int] | tuple[int, ...],
        ) -> tuple[int, ...]:
    """ Build a frame for function 0x01 (read variables). """

    num_vars = len(addresses)

    # Interleave types and addresses: [type1, addr1, type2, addr2, ...].
    type_address = chain.from_iterable(zip(types, addresses))

    packed_data = struct.pack(
        f'<BBB{num_vars*"BI"}',
        slave_address,
        FUNCTION_ID['0x01'],
        num_vars,
        *type_address
        )

    return _finalize_frame(tuple(packed_data))


def build_0x02_frame(
        slave_address: int,
        trigger: Trigger,
        types: list[int] | tuple[int, ...],
        addresses: list[int] | tuple[int, ...],
        ) -> tuple[int, ...]:
    """ Build a frame for the function 0x02 (trigger read). """

    trigger_type_fmt = PACK_SIZE[trigger.type_][0]
    num_vars = len(addresses)

    # Interleave types and addresses: [type1, addr1, type2, addr2, ...].
    type_address = chain.from_iterable(zip(types, addresses))

    packed_data = struct.pack(
        f'<BBBI{trigger_type_fmt}BHHBIBB{num_vars*"BI"}',
        slave_address,
        FUNCTION_ID['0x02'],
        trigger.type_,
        trigger.address,
        trigger.level,
        trigger.count,
        trigger.pre_trigger,
        trigger.post_trigger,
        trigger.edge,
        trigger.settling_samples,
        trigger.sample_count,
        num_vars,
        *type_address,
    )

    return _finalize_frame(tuple(packed_data))


def build_0x02_ack_frame(
        slave_address: int,
        repeat: Optional[str],
        ) -> tuple[int, ...]:
    """
    Build a acknowledgement frame for the function 0x02
    (trigger acknowledgement).
    """

    repeat_code = {None: 0, 'one': 1, 'all': 2, 'start': 3}.get(repeat, 0)
    packed_data = struct.pack(
        '<BBB',
        slave_address,
        FUNCTION_ID['0x02_ack'],
        repeat_code
        )

    return _finalize_frame(tuple(packed_data))


def build_0x03_frame(
        slave_address: int,
        type_: int,
        address: int,
        value: float | int,
        ) -> tuple[int, ...]:
    """ Build a frame for the function 0x03 (write variable). """

    fmt_char = PACK_SIZE[type_][0]
    is_float_type = fmt_char in ('f', 'd')

    # Validate value type against the expected struct format.
    if is_float_type != isinstance(value, (float, np.floating)):
        return tuple()

    packed_data = struct.pack(
        f'<BBBI{fmt_char}',
        slave_address,
        FUNCTION_ID['0x03'],
        type_,
        address,
        value,
    )

    return _finalize_frame(tuple(packed_data))


def build_0x04_frame(
        slave_address: int,
        start_index: int,
        num_periods: int,
        signal: np.ndarray,
        ) -> tuple[int, ...]:
    """ Build a frame for the function 0x04 (FRA excitation signal upload). """

    length = len(signal)

    if length > MAX_SIGNAL_CHUNK_SIZE:
        return tuple()

    packed_data = struct.pack(
        f'<BBIIB{length}f',
        slave_address,
        FUNCTION_ID['0x04'],
        start_index,
        num_periods,
        length,
        *signal,
    )

    return _finalize_frame(tuple(packed_data))
