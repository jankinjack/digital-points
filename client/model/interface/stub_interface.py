import threading
import ctypes
from contextlib import suppress
from typing import Optional, Callable, Self

from model.interface.stub_server import lib, get_stub_rx_frame


class StubInterface:
    """
    Singleton wrapper around a serial interface stub.
    Provides thread-safe writing and custom frame reading logic
    based on the COBS algorithm.
    """

    __slots__ = (
        '_write_lock',
        '_is_initialized',
        'connected',
        '_write_buf',
        '_read_buf',
        '_port',
        '_baudrate',
        '_parity',
        '_stopbits',
        '_bytesize',
        '_timeout',
    )

    __instance = None

    def __new__(cls) -> Self:
        """ Ensure only one instance of the stub interface exists. """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        """ Initialize the Singleton instance, preventing re-initialization. """

        # Prevent re-initialization of the Singleton instance.
        if getattr(self, '_is_initialized', False):
            return

        # Note: args and kwargs are accepted for API compatibility but ignored,
        # as StubInterface implicitly inherits from object, which takes no arguments.
        super().__init__()

        self._write_lock = threading.Lock()
        self._is_initialized = True

        self.connected = False
        self._write_buf: list[int] = []
        self._read_buf: list[int] = []

        # Serial port configuration parameters
        self._port: Optional[str] = None
        self._baudrate: Optional[int] = None
        self._parity: Optional[str] = None
        self._stopbits: Optional[float] = None
        self._bytesize: Optional[int] = None
        self._timeout: Optional[float] = None

    @property
    def port(self) -> Optional[str]:
        """ Get the serial port name. """

        return self._port

    @port.setter
    def port(self, new_port: Optional[str]) -> None:
        """ Set the serial port name. """

        self._port = new_port

    @property
    def baudrate(self) -> Optional[int]:
        """ Get the serial baud rate. """

        return self._baudrate

    @baudrate.setter
    def baudrate(self, new_baudrate: Optional[int]) -> None:
        """ Set the serial baud rate. """

        self._baudrate = new_baudrate

    @property
    def parity(self) -> Optional[str]:
        """ Get the serial parity setting. """

        return self._parity

    @parity.setter
    def parity(self, new_parity: Optional[str]) -> None:
        """ Set the serial parity setting. """

        self._parity = new_parity

    @property
    def stopbits(self) -> Optional[float]:
        """ Get the serial stop bits. """

        return self._stopbits

    @stopbits.setter
    def stopbits(self, new_stopbits: Optional[float]) -> None:
        """ Set the serial stop bits. """

        self._stopbits = new_stopbits

    @property
    def bytesize(self) -> Optional[int]:
        """ Get the serial byte size. """

        return self._bytesize

    @bytesize.setter
    def bytesize(self, new_bytesize: Optional[int]) -> None:
        """ Set the serial byte size. """

        self._bytesize = new_bytesize

    @property
    def timeout(self) -> Optional[float]:
        """ Get the serial read/write timeout. """

        return self._timeout

    @timeout.setter
    def timeout(self, new_timeout: Optional[float]) -> None:
        """ Set the serial read/write timeout. """

        self._timeout = new_timeout

    # --- Connection Methods ---

    def connect_to_port(self) -> bool:
        """ Simulate connecting to the serial port. """

        self.connected = True

        return self.is_connected()

    def disconnect_from_port(self) -> bool:
        """ Simulate disconnecting from the serial port. """

        self.connected = False
        return not self.is_connected()

    def is_connected(self) -> bool:
        """Check if the stub interface is currently connected."""

        return self.connected

    def _atomic_write(self, data: bytearray) -> int:
        """
        Thread-safe write operation that passes data to the C library stub
        and updates the receive buffer.
        """

        with suppress(Exception), self._write_lock:
            self._write_buf = list(data)

            ChunkArray = ctypes.c_uint8 * len(self._write_buf)
            c_chunk = ChunkArray.from_buffer_copy(data)

            lib.micro_dp_handle_rx_chunk(c_chunk, len(c_chunk))

            return len(self._write_buf)

        return 0

    def write_frame(self, frame_write: list[int] | tuple[int, ...]) -> bool:
        """ Send a complete frame and verify that all bytes were written. """

        with suppress(Exception):
            len_written = self._atomic_write(bytearray(frame_write))
            return len_written == len(frame_write)

        return False

    def read_frame(
        self,
        check_func: Callable[[int], bool],
        blocked_thread_exit: Callable[[], bool] = lambda: False,
    ) -> list[int]:
        """
        Read a frame from the stub receive buffer.

        Args:
            check_func: A callback to validate the frame length.
            blocked_thread_exit: A callback to check if a blocked thread should exit
                                (kept for API compatibility).

        Returns:
            The processed frame as a list of integers, or an empty list if invalid.
        """

        frame_read = []

        while True:
            lib.micro_dp_background()
            self._read_buf = get_stub_rx_frame()

            if self._read_buf:
                frame_read += self._read_buf
            else:
                break

        # A valid frame must be at least 9 bytes long and pass the custom check.
        if len(frame_read) < 9 or not check_func(len(frame_read)):
            return []

        # Strip the last 5 bytes (likely CRC or termination sequence).
        return list(frame_read[:-5])

    def flush_tx_buffer(self) -> None:
        """ Clear the transmit buffer (stub implementation does nothing). """

        pass
