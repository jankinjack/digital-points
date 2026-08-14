import time
from typing import Iterator, TYPE_CHECKING

import numpy as np

from model.interface.build_frame import build_0x04_frame, MAX_SIGNAL_CHUNK_SIZE
from model.interface.process_frame import process_0x04_ack_frame
from model.interface.function_0x02 import function_0x02

from model.fra.fra import FRA
import model.fra.excitation as excitation

from model.trigger import Trigger

if TYPE_CHECKING:
    import threading

    from model.interface.serial_interface import SerialInterface
    from model.interface.can_interface import CAN_Interface
    from model.interface.jtag_interface import JTAG_Interface
    from model.interface.stub_interface import StubInterface


def _upload_signal_chunks(
        interface: 'SerialInterface | CAN_Interface | JTAG_Interface | StubInterface',
        node_address: int,
        signal: np.ndarray,
        num_periods: int,
        ) -> bool:
    """
    Upload the excitation signal to the MCU in chunks.
    Returns True if all chunks were successfully acknowledged, False otherwise.
    """

    start_index = 0
    num_chunks = max(1, int(np.ceil(len(signal) / MAX_SIGNAL_CHUNK_SIZE)))

    for chunk in np.array_split(signal, num_chunks):
        if len(chunk) == 0:
            continue

        frame_write = build_0x04_frame(
            node_address, start_index, num_periods, chunk
            )

        # Retry up to 3 times per chunk.
        interface.timeout = 0.5

        for _ in range(3):
            interface.write_frame(frame_write)
            frame_read = interface.read_frame(lambda len_: len_ == 4)

            if frame_read and process_0x04_ack_frame(tuple(frame_read)):
                break
        else:
            return False

        start_index += len(chunk)

    return True


def function_0x04(
        interface: 'SerialInterface | CAN_Interface | JTAG_Interface | StubInterface',
        event: 'threading.Event',
        node_address: int,
        types: list[int] | tuple[int, ...],
        addresses: list[int] | tuple[int, ...],
        global_trigger: 'Trigger',
        lines_number: int,
        signal: np.ndarray = np.array([0]),
        ) -> Iterator[tuple[bool, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
    """
    Generator for Frequency Response Analysis (function 0x04).
    Generates excitation signals, uploads them to the MCU,
    captures the response via triggered reads (0x02),
    and computes the frequency response (FRA).

    Yields:
        A tuple: (is_finished, x_data, y_data,
        frequencies, magnitudes, phases).
    """

    # Create a local FRA trigger based on global settings.
    trigger = Trigger(enable_save_config=False)
    trigger.address = 0
    trigger.type_ = 'fra_t'
    trigger.edge = 'Leading Edge'
    trigger.count = 1
    trigger.sample_count = 1
    trigger.pre_trigger = 0
    trigger.level = 0
    trigger.max_number_samples = global_trigger.max_number_samples
    trigger.settling_time = global_trigger.settling_time
    trigger.one_shot_mode = True
    trigger.tx_number_samples = global_trigger.tx_number_samples
    trigger.sampling_frequency = global_trigger.sampling_frequency

    # Extract FRA configuration.
    n_list = global_trigger.fra_n_list
    dividers = global_trigger.fra_dividers
    frequencies = global_trigger.fra_frequencies
    amplitudes = global_trigger.fra_amplitudes
    repeat = global_trigger.fra_repeat
    average_type = global_trigger.fra_average_type
    excitation_type = global_trigger.fra_excitation_type
    harmonics = global_trigger.fra_harmonics

    if (len(n_list) == 0
            or len(dividers) == 0
            or len(frequencies) == 0
            or len(amplitudes) == 0
            or repeat == 0
            or not average_type
            or not excitation_type
            or len(harmonics) == 0):
        return

    sampling_frequency = float(trigger.sampling_frequency or 1)
    num_freqs = len(frequencies)

    if num_freqs == 0:
        return

    magnitudes = np.zeros(num_freqs, dtype=np.float64)
    phases = np.zeros(num_freqs, dtype=np.float64)

    trigger.fra_progress = (0, 0, '')

    if excitation_type == 'Single-Sine Excitation':
        f_prev = frequencies[0]

        for i, (n, d, a, f, h) in enumerate(zip(
                n_list, dividers, amplitudes, frequencies, harmonics
                )):

            # Check the connection.
            if not event.is_set() or not interface.is_connected():
                break

            if n * d <= 2:
                break

            # Generate the single-sine excitation signal.
            signal, _ = excitation.single_sine_signal(
                amplitude=a,
                num_points=n,
                harmonic=h,
                divisor=d
                )

            fra = FRA(sampling_frequency, (h,), average_type, repeat)

            interface.timeout = 0.5

            # Repeat measurement for averaging.
            for r in range(repeat):
                fra_progress = (
                    f,
                    int(100 * (i + 1) / len(n_list)),
                    f'Repeat {r}/{repeat}'
                    )
                global_trigger.fra_progress = fra_progress

                if not _upload_signal_chunks(
                        interface, node_address, signal, n
                        ):
                    break

                # Wait for signal settling (empirical formula
                # based on previous frequency).
                time.sleep(1.2 / f_prev)
                f_prev = f

                trigger.sample_count = int(d)
                trigger.post_trigger = int(n)

                if not trigger.is_ready():
                    break

                # Get a generator for 0x02.
                gen_0x02 = function_0x02(
                    interface,
                    event,
                    node_address,
                    types, addresses, trigger,
                    )

                try:
                    x_data, y_data = next(gen_0x02)
                except StopIteration:
                    break

                if x_data.size == 0 or y_data.size == 0:
                    raise ValueError

                yield (
                    False,
                    x_data, y_data,
                    frequencies[:i], magnitudes[:i], phases[:i]
                    )

                # Split response into input (y_a) and output (y_b).
                y_a = y_data[:lines_number]
                y_b = y_data[lines_number:]

                fra.add_data(y_a, y_b)
            else:
                # Executed only if the inner 'repeat' loop finished
                # without 'break'.
                magnitudes[i] = fra.response_magnitude[0]
                phases[i] = fra.response_phase[0]
                continue

            break
    else:
        n = int(n_list[0])
        d = int(dividers[0])
        fra = FRA(sampling_frequency / d, harmonics, average_type, 1)

        # Repeat measurement for averaging.
        for r in range(repeat):
            fra_progress = (
                0,
                int(100),
                f'Repeat {r}/{repeat}'
                )
            global_trigger.fra_progress = fra_progress

            if not _upload_signal_chunks(interface, node_address, signal, n):
                break

            trigger.post_trigger = n
            trigger.sample_count = d

            if not trigger.is_ready():
                return

            gen_0x02 = function_0x02(
                interface,
                event,
                node_address,
                types, addresses, trigger,
                )

            try:
                x_data, y_data = next(gen_0x02)
            except StopIteration:
                break

            if x_data.size == 0 or y_data.size == 0:
                raise ValueError

            # Get dp-lines to process the response.
            y_a = y_data[:lines_number]
            y_b = y_data[lines_number:]

            # Add data to FRA.
            fra.add_data(y_a, y_b)

            # Get the response's magnitude and phase.
            magnitudes = fra.response_magnitude
            phases = fra.response_phase

            yield False, x_data, y_data, frequencies, magnitudes, phases

    # Final yield.
    yield True, np.array([]), np.array([]), frequencies, magnitudes, phases
