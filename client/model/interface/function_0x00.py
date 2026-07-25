
from typing import TYPE_CHECKING

from model.interface.build_frame import build_0x00_frame
from model.interface.process_frame import ProcessingError, process_0x00_frame

if TYPE_CHECKING:
    from model.interface.serial_interface import SerialInterface
    from model.interface.can_interface import CAN_Interface
    from model.interface.stub_interface import StubInterface


def function_0x00(
        interface: 'SerialInterface | CAN_Interface | StubInterface',
        node_address: int,
        ) -> tuple[int, int, int, int, int]:
    """
    Execute function 0x00: Request device information and handshake parameters.

    Args:
        interface: The active communication interface.
        node_address: The target slave/node address.

    Returns:
        A tuple containing: 
        (sys_clock_freq, sampling_freq, max_samples, tx_samples, vars_count).

    Raises:
        RuntimeError: If the frame fails to send, the response is empty/invalid, 
        or the CRC check fails.
    """

    frame_write = build_0x00_frame(node_address)

    if not interface.write_frame(frame_write):
        raise RuntimeError("Failed to write 0x00 frame to the interface.")

    # Temporarily set a short timeout for the heartbeat response.
    original_timeout = interface.timeout
    interface.timeout = 0.5

    try:
        # Read the response frame (expected length is 24 bytes including DP_KEY).
        frame_read = interface.read_frame(lambda len_: len_ == 24)

        if not frame_read:
            raise RuntimeError("Empty or timeout response received for 0x00 frame.")

        return process_0x00_frame(tuple(frame_read))

    except ProcessingError as e:
        raise RuntimeError(f"Failed to process 0x00 frame payload: {e}") from e
    finally:
        # Restore the original timeout to prevent side-effects 
        # on subsequent interface operations.
        pass # interface.timeout = original_timeout
