import os
import ctypes
import time

# Define the relative path to the compiled C library.
LIB_FILENAME = "server/builds/dll/libmicrodp_gcc_dll_fast.dll"
lib_path = os.path.abspath(LIB_FILENAME)

if not os.path.exists(lib_path):
    raise FileNotFoundError(f"Stub library not found at: {lib_path}")

lib = ctypes.CDLL(lib_path)

# Define custom ctypes function prototypes.
ExceptionDP = ctypes.c_int
GET_SYS_CLK_COUNTER = ctypes.CFUNCTYPE(ctypes.c_size_t)
FUNC_TRANSMIT = ctypes.CFUNCTYPE(ExceptionDP, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t)
VOID_FUNC = ctypes.CFUNCTYPE(None)


class InfoDPStruct(ctypes.Structure):
    """ Structure representing the configuration passed to the Micro DP C library. """

    _fields_ = [
        ("sampling_freq", ctypes.c_uint32),
        ("func_transmit", FUNC_TRANSMIT),
        ("uninterrupted", ctypes.c_bool),
        ("disable_interrupts", VOID_FUNC),
        ("enable_interrupts", VOID_FUNC),
        ("memory_limit", ctypes.c_size_t),
        ("valid_min_addr", ctypes.c_void_p),
        ("valid_max_addr", ctypes.c_void_p),
        ("max_var_count", ctypes.c_uint32),
        ("static_buffer", ctypes.c_void_p),
        ("node_addr", ctypes.c_uint8),
        ]


# Set argument and return types for C functions.
lib.micro_dp_init.argtypes = [ctypes.POINTER(InfoDPStruct)]
lib.micro_dp_init.restype = ExceptionDP

lib.micro_dp_background.argtypes = []
lib.micro_dp_background.restype = ExceptionDP

lib.micro_dp_handle_rx_chunk.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t]
lib.micro_dp_handle_rx_chunk.restype = None

# Global state to store the latest received frame and system clock counter.
RX_FRAME: list[int] = []


@FUNC_TRANSMIT
def py_func_transmit(frame_ptr: ctypes.POINTER(ctypes.c_uint8), size: int) -> int:
    """ Callback invoked by the C library when a frame is transmitted. """

    global RX_FRAME
    
    # Read the byte array from the C pointer.
    response_bytes = ctypes.string_at(frame_ptr, size)
    
    # Store the response as a list of integers for Python-side processing.
    RX_FRAME = list(response_bytes)
    return 0  # DP_OK


@VOID_FUNC
def py_disable_interrupts() -> None:
    """ Stub callback for disabling interrupts (no-op in Python environment). """

    pass


@VOID_FUNC
def py_enable_interrupts() -> None:
    """ Stub callback for enabling interrupts (no-op in Python environment). """

    pass


def get_stub_rx_frame() -> list[int]:
    """ Retrieve the latest frame received by the stub. """

    global RX_FRAME
    frame = RX_FRAME
    RX_FRAME = []

    return frame


# Allocate a 1 MB static buffer for the C library to use.
# IMPORTANT: This must remain in the global scope so the Python garbage collector 
# doesn't free the memory while the C library is still using it.
BUFFER_SIZE: int = 1 * 1024 * 1024
my_static_pool = (ctypes.c_uint8 * BUFFER_SIZE)()


def _initialize_stub() -> None:
    """ Initialize the Micro DP C library with mock callbacks and memory buffers. """

    info = InfoDPStruct()

    info.sampling_freq = 100_000
    info.func_transmit = py_func_transmit
    info.uninterrupted = True
    info.disable_interrupts = py_disable_interrupts
    info.enable_interrupts = py_enable_interrupts

    # Pass the pointer to the static buffer.
    info.static_buffer = ctypes.cast(my_static_pool, ctypes.c_void_p)
    info.memory_limit = BUFFER_SIZE

    info.valid_min_addr = 0
    info.valid_max_addr = 0xFFFFFFFFFFFFFFFF
    info.max_var_count = 20
    info.node_addr = 0

    res = lib.micro_dp_init(ctypes.byref(info))
    if res != 0:
        RuntimeError(f"micro_dp_init returned: {res} (Expected 0 for DP_OK)")


# Auto-initialize when the module is imported.
_initialize_stub()