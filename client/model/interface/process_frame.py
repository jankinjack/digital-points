
import struct

import numpy as np

from model.interface.crc16 import crc16
from model.interface.build_frame import FUNCTION_ID, PACK_SIZE


class ProcessingError(Exception):
    """Custom exception for frame processing errors."""
    pass


def _verify_crc16(frame: list[int] | tuple[int, ...]) -> bool:
    """
    Verify the CRC-16 checksum of the frame.
    Assumes the last 2 bytes of the frame are the CRC (Big-Endian).
    """

    if len(frame) < 3:
        return False

    payload = frame[:-2]
    crc_bytes = crc16(payload)

    calculated_crc = (crc_bytes[1] << 8) | crc_bytes[0]
    received_crc = (frame[-2] << 8) | frame[-1]

    return calculated_crc == received_crc


def process_0x00_frame(frame: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    """ Process a frame for function 0x00 (device info and heartbeat). """

    if not frame or frame[1] != FUNCTION_ID['0x00'] or len(frame) != 15:
        raise ProcessingError("Invalid 0x00 frame structure or Function ID.")

    if not _verify_crc16(frame):
        raise ProcessingError('CRC-16 verification failed for 0x00 frame.')

    # Get data.
    (_, _, sampling_frequency, max_number_samples, tx_number_samples, vars_number) = \
        struct.unpack_from('<BBIIHB', bytes(frame), 0)

    return (
        sampling_frequency,
        max_number_samples,
        tx_number_samples,
        vars_number
        )


def process_0x01_frame(
        frame: list[int] | tuple[int, ...]
        ) -> np.ndarray:
    """ Process a frame for function 0x01 (read variables). """

    if not frame or frame[1] != FUNCTION_ID['0x01'] or len(frame) < 3:
        raise ProcessingError('Invalid 0x01 frame structure or Function ID.')

    if not _verify_crc16(frame):
        raise ProcessingError('CRC-16 verification failed for 0x01 frame.')

    # Get service data.
    _, _, var_number = struct.unpack_from('<BBB', bytes(frame), 0)

    variables = np.zeros((var_number, 1), dtype=np.float64)
    offset = 3

    for j in range(var_number):
        if offset >= len(frame) - 2:
            raise ProcessingError('Unexpected end of 0x01 frame payload.')

        var_type = frame[offset]
        if var_type >= len(PACK_SIZE):
            raise ProcessingError(f'Unknown variable type index: {var_type}')

        fmt_char, type_size = PACK_SIZE[var_type]
        variables[j, 0] = struct.unpack_from(
            f'<{fmt_char}',
            bytes(frame),
            offset + 1
            )[0]
        offset += 1 + type_size

    return variables


def process_0x02_ack_frame(frame: list[int] | tuple[int, ...]) -> bool:
    """
    Process an acknowledgement frame for function 0x02
    (trigger acknowledgement).
    """

    if not frame or frame[1] != FUNCTION_ID['0x02'] or len(frame) != 4:
        return False

    return _verify_crc16(frame)


def process_0x02_frame(
        frame: list[int] | tuple[int, ...]
        ) -> tuple[np.ndarray, int, int]:
    """ Process a frame for function 0x02. """

    if not frame or frame[1] != FUNCTION_ID['0x02'] or len(frame) < 16:
        raise ProcessingError('Invalid 0x02 frame structure or Function ID.')

    if not _verify_crc16(frame):
        raise ProcessingError('CRC-16 verification failed for 0x02 frame.')

    _, _, end_frame, trig_sample, samples_count, vars_count = \
        struct.unpack_from(
            '<BBBHHB',
            bytes(frame),
            0
            )

    variables = np.zeros((vars_count, samples_count), dtype=np.float64)

    # Each variable chunk has 2 bytes header
    #   + (samples_count * 8) bytes of data.
    # The MCU sends 8 bytes per sample regardless of the actual type size.
    chunk_size = 2 + samples_count * 8
    offset = 8

    for j in range(vars_count):
        if offset + chunk_size > len(frame) - 2:
            raise ProcessingError('Unexpected end of 0x02 frame payload.')

        var_type = frame[offset + 1]

        if var_type >= len(PACK_SIZE):
            raise ProcessingError(f'Unknown variable type index: {var_type}')

        fmt_char = PACK_SIZE[var_type][0]

        val_offset = offset + 2
        for i in range(samples_count):
            variables[j, i] = struct.unpack_from(
                f'<{fmt_char}',
                bytes(frame),
                val_offset
                )[0]
            val_offset += 8  # Skip the rest of the 8-byte buffer.

        offset += chunk_size

    return variables, end_frame, trig_sample


def process_0x03_ack_frame(frame: list[int] | tuple[int, ...]) -> bool:
    """
    Process a confirm frame for function 0x03
    (write variable acknowledgement).
    """

    if not frame or frame[1] != FUNCTION_ID['0x03'] or len(frame) < 4:
        return False

    return _verify_crc16(frame)


def process_0x04_ack_frame(frame: list[int] | tuple[int, ...]) -> bool:
    """
    Process a confirm frame for function 0x04
    (FRA excitation acknowledgment).
    """

    if not frame or frame[1] != FUNCTION_ID['0x04'] or len(frame) < 4:
        return False

    return _verify_crc16(frame)
