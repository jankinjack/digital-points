import os
import time
import threading
from typing import Optional, TYPE_CHECKING
import shutil
from inspect import currentframe, getframeinfo

import serial.tools.list_ports

import numpy as np

from PySide6.QtCore import Signal, QObject

import __main__

from model.trigger import Trigger

from model.interface.build_frame import build_0x03_frame
from model.interface.process_frame import process_0x03_ack_frame
from model.interface.function_0x00 import function_0x00
from model.interface.function_0x01 import function_0x01
from model.interface.function_0x02 import function_0x02
from model.interface.function_0x04 import function_0x04

from info import STUB_MICRO_DP

from model.interface.serial_interface import SerialInterface
from model.interface.can_interface import CAN_Interface
from model.interface.jtag_interface import JTAG_Interface

if STUB_MICRO_DP:
    from model.interface.stub_interface import StubInterface

if TYPE_CHECKING:
    from digital_points import DigitalPoints

# Valid operational modes.
SCOPE_MODES = {
    'Real-Time Mode',
    'Trigger Mode',
    'FRA Mode',
    }

# Struct format characters and their sizes in bytes.
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
    )


class InterfaceThread(threading.Thread):
    """Custom thread class for handling interface operations."""

    __slots__ = ('_change_ui',)

    def __init__(self, change_ui: bool = True, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._change_ui = change_ui

    @property
    def change_ui(self) -> bool:
        return self._change_ui


class InterfaceBase(QObject):
    """
    Base class for hardware interface management.
    Handles background polling, data acquisition, and command execution.
    """

    __slots__ = (
        '_dp',
        '_mode',
        '_vars_number',
        '_node_address',
        '_trigger',
        '_command_event',
        '_share_objects',
        '_ext_handler',
        '_thread',
        '_long_read',
        '_delayed_func',
        '_instances',
        '_interface',
        '_store_com_ports',
        '_dump_size_mb',
        )

    # Qt Signals.
    update_scope_data = Signal(tuple, np.ndarray, tuple, bool, int)
    update_fra_data = Signal(tuple, np.ndarray, tuple, bool, int)
    fra_finished = Signal()
    set_config_parameter = Signal(
        (tuple, str),
        (tuple, int),
        (tuple, float),
        (tuple, bool),
        )
    set_sys_clock_freq = Signal(str)
    node_status_changed = Signal(bool)
    frame_rate_changed = Signal(float)
    ext_handler_0x01 = Signal(int, tuple)
    list_of_com_ports_changed = Signal(tuple, tuple)
    log_info = Signal(str)
    log_warning = Signal(str)
    log_error = Signal(str)

    def __init__(self, dp: 'DigitalPoints') -> None:
        super().__init__()

        self._dp = dp

        self._mode = None
        self._vars_number = 4
        self._node_address = None

        self._dump_size_mb = 0

        self._trigger = Trigger()

        self._command_event = threading.Event()
        self._share_objects = None
        self._ext_handler = False

        self._thread = InterfaceThread(
            target=self._common_thread,
            args=(self._command_event,),
            daemon=True,
            )

        self._long_read = False
        self._delayed_func = []

        self._instances = {
            'serial': SerialInterface() if not STUB_MICRO_DP else StubInterface(),
            'can': CAN_Interface(),
            'jtag': JTAG_Interface(),
            }
        self._interface = self._instances['serial']
        self._store_com_ports = None

    @property
    def thread_(self) -> InterfaceThread:
        return self._thread

    @property
    def instances(self) -> dict:
        return self._instances

    @property
    def dump_size_mb(self) -> int:
        return self._dump_size_mb

    @dump_size_mb.setter
    def dump_size_mb(self, new_dump_size_mb: int) -> None:
        self._dump_size_mb = new_dump_size_mb

        # Save in config file.
        self.set_config_parameter[tuple, int].emit(
            ('rtm', 'dump_size_mb'), new_dump_size_mb
            )

    @property
    def interface(self) -> 'SerialInterface | CAN_Interface | JTAG_Interface | StubInterface':
        return self._interface

    @interface.setter
    def interface(
            self,
            new_interface: 'SerialInterface | CAN_Interface | JTAG_Interface | StubInterface'
            ) -> None:
        self._interface = new_interface

    @property
    def trigger(self) -> Trigger:
        return self._trigger

    @property
    def mode(self) -> Optional[str]:
        return self._mode

    @mode.setter
    def mode(self, new_mode: Optional[str]) -> None:
        if self._mode != new_mode:
            self._mode = new_mode

            # Save in config file.
            self.set_config_parameter[tuple, str].emit(('mode',), new_mode)

    @property
    def vars_number(self) -> int:
        return self._vars_number

    @vars_number.setter
    def vars_number(self, new_vars_number: int) -> None:
        self._vars_number = new_vars_number

    @property
    def node_address(self) -> Optional[int]:
        return self._node_address

    @node_address.setter
    def node_address(self, new_node_address: int) -> None:
        if self._node_address != new_node_address:
            self._node_address = new_node_address

            # Save in config file.
            self.set_config_parameter[tuple, int].emit(
                ('node address',), new_node_address
                )

    def connect_to_node(
            self,
            share_objects: Optional[list[tuple[int, int]]] = None,
            ) -> None:
        """ Start the data acquisition thread. """

        self._share_objects = share_objects
        self._command_event.set()

    def disconnect_from_node(self) -> None:
        """ Stop the data acquisition thread. """

        self._share_objects = None
        self._command_event.clear()

    def is_started(self) -> bool:
        """ Check if the acquisition thread is currently running. """
        return self._command_event.is_set()

    def _common_thread(self, event: threading.Event) -> None:
        """
        Main background thread loop for device polling
        and data acquisition.
        """

        node_status = False

        while True:
            try:

                # Poll available COM ports.
                com_ports_objects = serial.tools.list_ports.comports()
                com_ports = tuple(sorted([
                    com_port.device for com_port in com_ports_objects
                    ]))

                # Check of the list of COM ports has been changed.
                if (self._store_com_ports is None
                        or set(com_ports) != set(self._store_com_ports)):

                    if self._store_com_ports is None:
                        self._store_com_ports = ()

                    self.list_of_com_ports_changed.emit(
                        com_ports, self._store_com_ports,
                        )
                    self._store_com_ports = com_ports

                # Device polling logic when event is NOT set (idle state).
                if not event.wait(timeout=0.5):
                    # Get information about MicroDP.
                    try:
                        result = function_0x00(
                            self._interface, int(self._node_address or 0),
                            )

                        (sample_freq, n_max, tx_max, n_vars) = result

                    except Exception:
                        if node_status:
                            node_status = False
                            self.node_status_changed.emit(False)

                        """
                        frame_info = getframeinfo(currentframe())

                        self.log_error.emit(
                            f'{type(e).__name__}: {str(e)}'
                            f' : {os.path.basename(frame_info.filename)}, {frame_info.lineno}'
                            )
                        """
                        continue

                    params_valid_and_changed = (
                        sample_freq is not None
                        and n_max is not None
                        and tx_max is not None
                        and n_vars is not None
                        and (
                            self.trigger.sampling_frequency != sample_freq
                            or self.trigger.max_number_samples != n_max
                            or self.trigger.tx_number_samples != tx_max
                            or self.vars_number != n_vars
                            )
                        )

                    if params_valid_and_changed:
                        self.trigger.sampling_frequency = sample_freq
                        self.trigger.max_number_samples = n_max
                        self.trigger.tx_number_samples = tx_max
                        self.vars_number = n_vars

                        self.node_status_changed.emit(True)

                    if not node_status:
                        self.node_status_changed.emit(True)
                        node_status = True
                    continue

                # If event is set but no objects, skip.
                if self._share_objects is None:
                    continue

                # Extract types and addresses for acquisition.
                types = [object_[0] for object_ in self._share_objects]
                addresses = [object_[1] for object_ in self._share_objects]
                n_vars = len(self._share_objects)

                match self.mode:
                    case 'Real-Time Mode':

                        # Remove previous dumps.
                        dump_dir = __main__.FULL_PATH / 'dumps'
                        shutil.rmtree(dump_dir, ignore_errors=True)

                        # Get a generator for 0x01.
                        gen_0x01 = function_0x01(
                            self._interface,
                            event,
                            int(self._node_address or 0),
                            types, addresses,
                            dump_size=int(
                                self._dump_size_mb * 1024 * 1024 / 4
                                ),
                            )

                        while event.is_set():
                            # Call the delayed function.
                            temp = self._delayed_func
                            self._delayed_func = []

                            for d_func in temp:
                                if (d_func[0] is not None
                                        and d_func[1] is not None):
                                    d_func[0](**d_func[1])

                            try:
                                # Get data from the generator.
                                delta, x_data, y_data, dump = next(gen_0x01)
                            except StopIteration:
                                break
                            except Exception as e:
                                frame_info = getframeinfo(currentframe())

                                self.log_error.emit(
                                    f'{type(e).__name__}: {str(e)}'
                                    f' : {os.path.basename(frame_info.filename)}, {frame_info.lineno}'
                                    )
                                break

                            # Process the data.
                            if not self._ext_handler:
                                self.update_scope_data.emit(
                                    range(n_vars),
                                    x_data, y_data,
                                    True,   # Enable math.
                                    dump,
                                    )
                            else:
                                for i, y in enumerate(y_data):
                                    self.ext_handler_0x01.emit(i, (x_data, y))

                            # Update frame rate.
                            self.frame_rate_changed.emit(1/delta if delta > 0 else 0)

                    case 'Trigger Mode':
                        # Check the trigger.
                        if not self.trigger.is_ready():
                            self.log_warning.emit(
                                'the trigger configuration is not valid.'
                                )
                            continue

                        def __set_long_read(long_read: bool) -> None:
                            self._long_read = long_read

                        # Get a generator for 0x02.
                        gen_0x02 = function_0x02(
                            self._interface,
                            event,
                            int(self._node_address or 0),
                            types, addresses, self.trigger,
                            __set_long_read,
                            )

                        while event.is_set():
                            # Call the delayed function.
                            temp = self._delayed_func
                            self._delayed_func = []

                            for d_func in temp:
                                if (d_func[0] is not None
                                        and d_func[1] is not None):
                                    d_func[0](**d_func[1])

                            try:
                                # Get data from the generator.
                                x_data, y_data = next(gen_0x02)
                            except StopIteration:
                                break

                            self.update_scope_data.emit(
                                range(len(y_data)),
                                x_data, y_data,
                                True,   # Enable math.
                                -1,     # Disable dumps.
                                )

                            if self._trigger.one_shot_mode:
                                break

                        self.trigger.stage = '-'

                    case 'FRA Mode':
                        # Use only two variables to measure
                        # frequency responses.
                        if len(addresses) == 2:
                            # Get a generator for 0x04.
                            gen_0x04 = function_0x04(
                                self._interface,
                                event,
                                int(self._node_address or 0),
                                types, addresses, self.trigger,
                                len(self._dp.main.graph_scope.axes[0].lines),
                                self._dp.fra_settings.graph_fra_excitation.lines[0].y_data,
                                )

                            while event.is_set():
                                try:
                                    # Get data from the generator.
                                    result = next(gen_0x04)

                                    (finish, x_data, y_data, frequencies, magnitudes, phases) = result

                                    if x_data is not None and y_data is not None:
                                        self.update_scope_data.emit(
                                            range(len(y_data)),
                                            x_data, y_data,
                                            True,   # Enable math.
                                            -1,     # Disable dumps.
                                            )

                                    if frequencies.size == magnitudes.size == phases.size > 0:
                                        # Plot the frequency responses.
                                        self.update_fra_data.emit(
                                            (0, 1),
                                            frequencies,
                                            (magnitudes, phases),
                                            False,      # Disable math.
                                            -1,         # Disable dumps.
                                            )

                                    if finish:
                                        self.fra_finished.emit()
                                        break
                                except Exception:
                                    break
                        else:
                            self.log_info.emit(
                                'Select two variables for FRA.'
                                )

                    case _:
                        pass

                self.disconnect_from_node()
            except Exception as e:
                frame_info = getframeinfo(currentframe())

                self.log_error.emit(
                    f'{type(e).__name__}: {str(e)}'
                    f' : {os.path.basename(frame_info.filename)}, {frame_info.lineno}'
                    )

                # Prevent 100% CPU usage
                # in case of an unexpected rapid error loop.
                time.sleep(0.5)

    def _process_delayed_functions(self) -> None:
        """ Execute queued delayed functions safely. """

        temp = self._delayed_func
        self._delayed_func = []

        for func, kwargs in temp:
            if func is not None and kwargs is not None:
                func(**kwargs)

    def write_value_0x03(
            self,
            type_: int,
            address: int,
            write_value: float | int,
            delayed: bool = False,
            ) -> None:
        """ Write a value to a specific variable on the MCU. """

        # Queue the write operation if the interface is currently busy.
        if self.is_started() and not delayed and not self._long_read:
            args = {
                'type_': type_,
                'address': address,
                'write_value': write_value,
                'delayed': True,
                }
            self._delayed_func.append((self.write_value_0x03, args))
            return

        if not self._interface.is_connected():
            return

        self._interface.timeout = 0.2

        # Build a frame to write.
        frame_write = build_0x03_frame(
            int(self._node_address or 0), type_, address, write_value
            )

        # Attempt to write and verify up to 3 times.
        for _ in range(3):
            self._interface.write_frame(frame_write)
            frame_read = self._interface.read_frame(lambda len_: len_ == 9)

            if frame_read and process_0x03_ack_frame(tuple(frame_read)):
                return  # Success

    def read_values_0x01(
            self,
            types: list[int] | tuple[int, ...],
            addresses: list[int] | tuple[int, ...],
            delayed: bool = False,
            ) -> None:
        """ Read values of specified variables from the MCU. """

        if self._long_read:
            self.ext_handler_0x01.emit(0, (None, None))
            return

        # Queue the read operation if the interface is currently busy.
        if self.is_started() and not delayed:
            args = {
                'types': types,
                'addresses': addresses,
                'delayed': True,
                }
            self._delayed_func.append((self.read_values_0x01, args))
            return

        gen_0x01 = function_0x01(
            self._interface,
            self._command_event,
            int(self._node_address or 0),
            types, addresses,
            non_thread=True,
            )

        try:
            _, x_data, y_data, _ = next(gen_0x01)

            for i, y in enumerate(y_data):
                self.ext_handler_0x01.emit(i, (x_data, y))

        except StopIteration:
            return
        except Exception as e:
            frame_info = getframeinfo(currentframe())

            self.log_error.emit(
                f'{type(e).__name__}: {str(e)}'
                f' : {os.path.basename(frame_info.filename)}, {frame_info.lineno}'
                )
