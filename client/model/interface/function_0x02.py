
import threading
from typing import Iterator, Optional, Callable, TYPE_CHECKING

import numpy as np

from model.interface.build_frame import (
    build_0x02_frame,
    build_0x02_ack_frame,
    )
from model.interface.process_frame import (
    ProcessingError,
    process_0x02_frame,
    process_0x02_ack_frame,
    )

from info import STUB_MICRO_DP

if STUB_MICRO_DP:
    from model.interface.stub_interface import lib

if TYPE_CHECKING:
    from model.interface.serial_interface import SerialInterface
    from model.interface.can_interface import CAN_Interface
    from model.interface.stub_interface import StubInterface
    from model.trigger import Trigger


def function_0x02(
        interface: 'SerialInterface | CAN_Interface | StubInterface',
        event: threading.Event,
        node_address: int,
        types: list[int] | tuple[int, ...],
        addresses: list[int] | tuple[int, ...],
        trigger: 'Trigger',
        set_long_read: Callable = lambda _: None,
        ) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """
    Generator for Triggered Mode (function 0x02).
    Sends trigger configuration to the MCU, waits for the hardware trigger event,
    reads the buffered data chunks, and yields the aligned time-series arrays.
    """

    def _ack_0x02(repeat: Optional[str] = None) -> bool:
        # Build a acknowledgement frame to write.
        frame_write = build_0x02_ack_frame(
            node_address,
            repeat=repeat,
            )

        return interface.write_frame(frame_write)

    trigger.stage = 'Started'

    pre_trigger = trigger.pre_trigger
    post_trigger = trigger.post_trigger

    # Save original timeout to restore it later.
    original_timeout = interface.timeout

    err_count_out = 0

    try:
        while event.is_set() and interface.is_connected() and err_count_out < 5:

            # Initial data.
            y_data_chunks = []

            # Assemble a frame to write.
            frame_write = build_0x02_frame(
                node_address,
                trigger,
                types, addresses,
                )

            interface.timeout = 0.5

            if not interface.write_frame(frame_write):
                err_count_out += 1
                continue

            frame_read = interface.read_frame(lambda len_: len_ == 9)

            if not frame_read or not process_0x02_ack_frame(tuple(frame_read)):
                err_count_out += 1
                continue

            err_count_out = 0
            err_count_in = 0

            if not _ack_0x02(repeat='start'):
                continue

            # Switch to infinite timeout while waiting for the hardware trigger.
            interface.timeout = None
            trigger.stage = 'Waiting for the trigger'
            end = False

            # Check if the serial interface is open.
            while (event.is_set()
                    and not end
                    and interface.is_connected()
                    and err_count_in < 5):

                # Read the responses.
                if not STUB_MICRO_DP:
                    set_long_read(interface.timeout is None)
                    frame_read = interface.read_frame(
                        check_func=lambda len_: len_ >= 25,
                        blocked_thread_exit=lambda: not event.is_set(),
                        )
                    set_long_read(False)
                else:
                    frame_read = None

                    while (event.is_set()
                            and interface.is_connected()
                            and not frame_read):
                        frame_read = interface.read_frame(
                            check_func=lambda len_: len_ >= 25,
                            blocked_thread_exit=lambda: not event.is_set(),
                            )

                        lib.micro_dp_context()

                if not frame_read:
                    if not _ack_0x02(repeat='one'):
                        break

                    err_count_in += 1
                    continue

                trigger.stage = 'Reading the buffer'
                interface.timeout = 0.5

                # Get data from the frame.
                try:
                    result = process_0x02_frame(frame_read)
                    (variables, end_frame, trig_sample) = result
                except ProcessingError:
                    if not _ack_0x02(repeat='one'):
                        break

                    err_count_in += 1
                    continue

                # Accumulate data.
                y_data_chunks.append(variables)

                if end_frame == 1:
                    try:
                        # Concatenate all chunks into a single array.
                        y_data = np.hstack(y_data_chunks)

                        # Generate time axis relative to the trigger point.
                        x_data = np.linspace(
                            -pre_trigger, post_trigger - 1, pre_trigger + post_trigger
                            ) * trigger.sample_count / trigger.sampling_frequency

                        # Align the data so the trigger point is correctly positioned.
                        shift = -(trig_sample + post_trigger)
                        y_data = np.roll(y_data, shift=shift, axis=1)

                        end = True
                    except (IndexError, ValueError):
                        # Handle desync or malformed sample indices from the MCU.
                        _ack_0x02(repeat='all')

                        err_count_in += 1
                        y_data_chunks.clear()

                        continue

                if not _ack_0x02():
                    err_count_in += 1
                else:
                    err_count_in = 0

                if end:
                    yield x_data, y_data
                    break

    finally:
        # Restore the original timeout to prevent
        # breaking subsequent operations in other modes.
        pass # interface.timeout = original_timeout
