
import os
import platform
import threading
from typing import Optional, Callable, Self
from contextlib import suppress
import time

import can
from can.interfaces import gs_usb, robotell, canalystii

if platform.system() == 'Linux':
    from can.interfaces import socketcan

import usb

from controller.common import chunks
from model.interface.build_frame import DP_KEY


class CAN_Interface():

    __slots__ = (
        '_bus_type',
        '_bitrate',
        '_baudrate',
        '_id',
        '_extended_id',
        '_port',
        '_timeout',
        '_write_lock',
        '_bus',
        '_abm',
        '_auto_retransmit',
        )
    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self) -> None:

        self._bus_type = None
        self._bitrate = None
        self._baudrate = None
        self._id = None
        self._extended_id = None
        self._port = None
        self._timeout = None

        self._write_lock = threading.Lock()

        self._bus = None

        self._abm = None
        self._auto_retransmit = None

    @property
    def port(self) -> Optional[str]:
        return self._port

    @port.setter
    def port(self, new_port: str) -> None:

        if new_port != self._port:
            self.disconnect_from_port()
            self._port = new_port if new_port != '' else None

    @property
    def baudrate(self) -> Optional[int]:
        return self._baudrate

    @baudrate.setter
    def baudrate(self, new_baudrate: int) -> None:
        self._baudrate = new_baudrate

    @property
    def bus_type(self) -> Optional[str]:
        return self._bus_type

    @bus_type.setter
    def bus_type(self, new_bus_type: str) -> None:
        self._bus_type = new_bus_type

    @property
    def bitrate(self) -> Optional[int]:
        return self._bitrate

    @bitrate.setter
    def bitrate(self, new_bitrate: int) -> None:
        self._bitrate = new_bitrate

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        self._id = new_id

    @property
    def extended_id(self) -> Optional[bool]:
        return self._extended_id

    @extended_id.setter
    def extended_id(self, new_extended_id: bool) -> None:
        self._extended_id = new_extended_id

    @property
    def abm(self) -> Optional[bool]:
        return self._abm

    @abm.setter
    def abm(self, new_abm: bool) -> None:
        self._abm = new_abm

    @property
    def auto_retransmit(self) -> Optional[bool]:
        return self._auto_retransmit

    @auto_retransmit.setter
    def auto_retransmit(self, new_auto_retransmit: bool) -> None:
        self._auto_retransmit = new_auto_retransmit

    @property
    def timeout(self) -> float | int | None:
        return self._timeout

    @timeout.setter
    def timeout(self, new_timeout: Optional[float | int]) -> None:
        self._timeout = new_timeout

    def connect_to_port(self) -> bool:
        """ Connect to current CAN port. """

        if self._bus_type != 'robotell' or self.port:
            self.disconnect_from_port()

        # Connect to the port.
        with suppress(Exception):
            if self._bus_type == 'socketcan' and platform.system() == 'Linux':
                os.system(
                    'sudo ip link set can0 up type can bitrate ' + str(self._bitrate)
                    )
                self._bus = socketcan.SocketcanBus(channel='can0')
            elif self._bus_type == 'robotell':
                if not self._port:
                    return False

                self._bus = robotell.robotellBus(
                    channel=self._port,
                    ttyBaudrate=int(self._baudrate or 115200),
                    bitrate=self._bitrate,
                    )
            elif self._bus_type == 'gs_usb':
                dev = usb.core.find(idVendor=0x1D50, idProduct=0x606F)
                if dev:
                    self._bus = gs_usb.GsUsbBus(
                        channel=dev.product,
                        bus=dev.bus,
                        address=dev.address,
                        bitrate=self._bitrate,
                        )
            elif self._bus_type == 'canalyst_ii':
                self._bus = canalystii.CANalystIIBus(
                    channel=0,
                    device=0,
                    bitrate=self._bitrate,
                    )
            else:
                self._bus = None

        return self.is_connected()

    def disconnect_from_port(self) -> bool:
        """ Disconnect from current COM port. """

        with suppress(Exception):
            if self._bus:
                # Repeat shutting down just in case.
                for _ in range(5):
                    with suppress(Exception):
                        usb.util.dispose_resources(self._bus.gs_usb.gs_usb)

                    self._bus.shutdown()
                    time.sleep(0.1)
                
                self._bus = None

            if self._bus_type == 'socketcan' and platform.system() == 'Linux':
                os.system(
                    'sudo ip link set can0 down type can'
                    )

        return not self.is_connected()

    def is_connected(self) -> bool:

        if self._bus_type == 'robotell':
            is_connected = (self._bus is not None
                and self._bus.serialPortOrig.isOpen())
        else:
            is_connected = (self._bus is not None
                and self._bus.state == can.bus.BusState.ACTIVE)

        return is_connected

    def _atomic_write(self, data: bytearray) -> int:
        """ Atomic write with locking. """

        with suppress(Exception), self._write_lock:
            self._bus.send(
                can.Message(
                    is_extended_id=self._extended_id,
                    arbitration_id=self._id,
                    data=data,
                    is_rx=False,
                    )
                )

        return len(data)

    def write_frame(self, frame_write: list[int] | tuple[int, ...]) -> bool:
        """ Write (send) a frame. """

        for chunk in chunks(frame_write, 8):
            self._atomic_write(bytearray(chunk))

        return True

    def read_frame(
            self,
            check_func: Callable,
            blocked_thread_exit: Callable = lambda: False,
            ) -> list[int]:
        """ Read (receive) a frame. """

        frame_read = []
        check_seq = DP_KEY

        real_timeout = self._timeout

        if self._timeout is None:
            self._timeout = 0.1

        with suppress(Exception):
            while True:
                message_read = self._bus.recv(timeout=self._timeout)

                if message_read:
                    if not message_read.is_error_frame and message_read.is_rx:
                        frame_read += list(message_read.data)

                        seq = [i+len(check_seq) for i in range(len(frame_read))
                            if frame_read[i:i+len(check_seq)] == check_seq]

                        # Finding the DP_KEY-sequence.
                        if seq:
                            frame_read = frame_read[:seq[-1]]
                            break
                elif real_timeout is not None:
                    return []

                # Conditional exit inside blocking thread.
                if blocked_thread_exit():
                    return []

        # Check if the frame is read.
        if (len(frame_read) < 9 or not check_func(len(frame_read))):
            return []

        return frame_read[0:-5]

    def flush_tx_buffer(self) -> None:
        """ Flush TX buffer. """

        with suppress(Exception):
            self._bus.flush_tx_buffer()
