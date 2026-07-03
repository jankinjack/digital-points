
import threading
from typing import Iterator, TYPE_CHECKING
from pathlib import Path

import numpy as np

import __main__

from model.interface.build_frame import build_0x01_frame
from model.interface.process_frame import ProcessingError, process_0x01_frame

if TYPE_CHECKING:
    from model.interface.serial_interface import SerialInterface
    from model.interface.can_interface import CAN_Interface
    from model.interface.stub_interface import StubInterface


def _save_dump_worker(dump_path: Path, dump_array: np.ndarray, header: str) -> None:
    """ Worker function for the background dump-saving thread. """

    np.savetxt(
        dump_path,
        dump_array,
        delimiter=', ',
        header=header,
        comments='',
    )


def function_0x01(
        interface: 'SerialInterface | CAN_Interface | StubInterface',
        event: threading.Event,
        node_address: int,
        types: list[int] | tuple[int, ...],
        addresses: list[int] | tuple[int, ...],
        sys_freq: float | int,
        non_thread: bool = False,
        dump_size: int = 0
        ) -> Iterator[tuple[float, int, np.ndarray, np.ndarray]]:
    """
    Generator that continuously polls the MCU (function 0x01),
    accumulates time-series data, and optionally dumps it to CSV files.
    
    Yields:
        A tuple containing: (delta_time, x_data_array, y_data_array, dump_state_flag).
    """

    x_list = []
    y_list = []
    
    tic = 0
    n_dump = 0
    err_count = 0
    
    is_first_packet = True
    is_first_yield = True
    
    # Pre-build CSV header for dumps
    csv_header = 'time, ' + ', '.join(
        f'{hex(addr)}/{type_}' for type_, addr in zip(types, addresses)
    )
    
    dump_dir = __main__.FULL_PATH / 'dumps'
    if dump_size > 0:
        dump_dir.mkdir(exist_ok=True)

    while (non_thread or event.is_set()) and interface.is_connected() and err_count < 5:
        frame_write = build_0x01_frame(node_address, types, addresses)

        if not interface.write_frame(frame_write):
            err_count += 1
            continue

        frame_read = interface.read_frame(lambda len_: len_ >= 16)
        
        if not frame_read:
            err_count += 1
            continue

        try:
            # process_0x01_frame returns variables with shape (N, 1)
            variables, sys_clock = process_0x01_frame(frame_read)
            err_count = 0  # Reset error count on successful read.
        except ProcessingError:
            err_count += 1
            continue

        # Handle 32-bit unsigned integer timer overflow elegantly using bitmask.
        delta_ticks = (sys_clock - tic) & 0xFFFFFFFF
        tic = sys_clock
        
        # Skip delta calculation for the very first packet.
        if is_first_packet:
            is_first_packet = False
            delta_sec = 0.0
            x_list.append(0.0)
        else:
            delta_sec = delta_ticks / sys_freq
            x_list.append(x_list[-1] + delta_sec)

        # Accumulate data.
        y_list.append(variables[:, 0]) 

        # Check if dump threshold is reached.
        # Size is measured in array elements (equivalent to original y_data.size + x_data.size).
        current_size = (len(addresses) + 1) * len(x_list)
        
        if dump_size > 0 and current_size >= dump_size:
            # Keep the last point to ensure visual continuity on the graph.
            num_points_to_dump = len(x_list) - 1
            
            dump_x = x_list[:num_points_to_dump]
            dump_y = y_list[:num_points_to_dump]
            
            # Stack time and variables into a single 2D array for CSV.
            dump_array = np.column_stack([dump_x] + dump_y)
            dump_path = dump_dir / f'dump_{n_dump}.csv'
            
            # Start background thread to save data without blocking the acquisition loop.
            threading.Thread(
                target=_save_dump_worker,
                args=(dump_path, dump_array, csv_header),
                daemon=True,
            ).start()
            
            # Reset buffers, keeping ONLY the last point for continuity.
            x_list = [x_list[-1]]
            y_list = [y_list[-1]]
            
            # Convert remaining buffer to numpy arrays for the yield.
            x_data = np.array(x_list)
            y_data = np.column_stack(y_list)
            
            yield delta_sec, x_data, y_data, n_dump
            n_dump += 1
            continue

        # Convert lists to numpy arrays for yielding to the GUI.
        x_data = np.array(x_list)
        y_data = np.column_stack(y_list) if y_list else np.empty((len(addresses), 0))

        # Replicate original state flags (-1 for first packet, -2 for continuous streaming).
        dump_state = -1 if is_first_yield else -2

        if is_first_yield:
            is_first_yield = False

        yield delta_sec, x_data, y_data, dump_state
