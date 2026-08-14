
import threading
import serial
from typing import Optional, Callable, Self
from contextlib import suppress

from cobs import cobs


class SerialInterface(serial.Serial):
    """
    Singleton wrapper around pyserial's Serial class.
    Provides thread-safe writing and custom frame reading logic
    based on the COBS algorithm via serial port.
    """

    __slots__ = (
        '_write_lock',
        '_is_initialized',
        )
    __instance = None

    def __new__(cls) -> Self:
        """ Ensure only one instance of the serial interface exists. """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        # Prevent re-initialization of the Singleton instance
        if getattr(self, '_is_initialized', False):
            return

        super().__init__(*args, **kwargs)

        self._write_lock = threading.Lock()
        self._is_initialized = True

    @serial.Serial.port.setter
    def port(self, new_port: Optional[str]) -> None:
        """
        Override port setter to safely disconnect
        before changing the port.
        """

        if serial.Serial.parity.fset is None:
            return

        if new_port != self.port:
            self.disconnect_from_port()

            # Set to None if empty string is provided.
            serial.Serial.port.fset(
                self,
                new_port if new_port != '' else None,
                )

    @serial.Serial.baudrate.setter
    def baudrate(self, new_baudrate: int) -> None:
        serial.Serial.baudrate.fset(self, new_baudrate)

    @serial.Serial.parity.setter
    def parity(self, new_parity: str) -> None:
        """
        Map human-readable parity names
        to pyserial's internal constants.
        """

        if serial.Serial.parity.fset is None:
            return

        for key, name in serial.PARITY_NAMES.items():
            if name == new_parity:
                serial.Serial.parity.fset(self, key)
                return

    @serial.Serial.stopbits.setter
    def stopbits(self, new_stopbits: int | float) -> None:
        serial.Serial.stopbits.fset(self, float(new_stopbits))

    @serial.Serial.bytesize.setter
    def bytesize(self, new_bytesize: int) -> None:
        serial.Serial.bytesize.fset(self, new_bytesize)

    @serial.Serial.timeout.setter
    def timeout(self, new_timeout: Optional[float | int]) -> None:
        """ Safely set the read timeout, ignoring invalid values. """

        with suppress(Exception):
            serial.Serial.timeout.fset(self, new_timeout)

    def connect_to_port(self) -> bool:
        """ Open the serial port and flush buffers. """

        self.disconnect_from_port()

        if not self.port:
            return False

        with suppress(Exception):
            # Connect to the serial port.
            if not self.is_connected():
                self.open()
                self.reset_input_buffer()
                self.reset_output_buffer()

        return self.is_connected()

    def disconnect_from_port(self) -> bool:
        """ Close the serial port if it is currently open. """

        with suppress(Exception):
            if self.is_connected():
                self.close()

        return not self.is_connected()

    def is_connected(self) -> bool:
        """ Check if the serial port is currently open. """

        return self.isOpen()

    def _atomic_write(self, data: bytearray | bytes) -> int:
        """ Thread-safe write operation. """

        with suppress(Exception), self._write_lock:
            return self.write(data) or 0

        return 0

    def write_frame(self, frame_write: list[int] | tuple[int, ...]) -> bool:
        """ Send a complete frame and verify that all bytes were written. """

        with suppress(Exception):
            len_written = self._atomic_write(bytearray(frame_write))

            self.flush()

            # Check if the entire frame is written.
            return len_written == len(frame_write)

        return False

    def read_frame(
            self,
            check_func: Callable,
            blocked_thread_exit: Callable = lambda: False,
            ) -> list[int]:
        """
        Read a frame terminated by the delimeter byte.

        Args:
            check_func: A callback to validate the length of the received frame.
            blocked_thread_exit: A callback to gracefully abort reading if the
                                calling thread is requested to stop.

        Returns:
            A list of integers representing the frame bytes (excluding the delimiter byte),
            or an empty list if the read fails or is aborted.
        """

        real_timeout = self.timeout

        if self.timeout is None:
            self.timeout = 0.1

        try:
            while True:
                frame_read = self.read_until(expected=b'\x00')

                if frame_read:
                    break

                # If the original timeout was not None,
                # it means we just hit the timeout
                # and shouldn't loop indefinitely.
                if real_timeout is not None:
                    self.timeout = real_timeout
                    return []

                # Check if the background thread has been signaled to stop.
                if blocked_thread_exit():
                    self.timeout = real_timeout
                    return []
        except Exception:
            return []
        finally:
            # Always restore the original timeout to prevent
            # side-effects on subsequent read operations.
            pass # self.timeout = real_timeout

        frame_read = cobs.decode(frame_read[:-1])

        # Validate frame length and custom check function.
        # Minimum frame size is 4 bytes.
        if len(frame_read) < 4 or not check_func(len(frame_read)):
            return []

        return list(frame_read)

    def flush_tx_buffer(self) -> None:
        """ Discard all data in the transmit buffer. """

        with suppress(Exception):
            self.reset_output_buffer()
