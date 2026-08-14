/**
 * \file    micro_dp_0x04.c
 * \brief   Excitation signal generation function (0x04) — chunked waveform download and playback.
 *
 * The 0x04 function allows the host to upload a custom excitation waveform (e.g., sinusoidal)
 * in chunks. Once the full waveform period is loaded into the memory buffer, the node enables
 * the continuous playback of the signal via the micro_dp_excitation() routine.
 */

#include "micro_dp.h"
#include "micro_dp_crc16.h"

static Exception_DP build_0x04_ack_frame(void);

/**
 * \brief   Process an incoming 0x04 frame from the host.
 *
 * \param   frame: Pointer to the received frame buffer.
 * 
 * \retval  DP_OK: Frame processed successfully; acknowledgement will be built.
 * \retval  DP_ERROR: Signal chunk exceeds the allocated buffer capacity.
 */
EXPORT Exception_DP process_0x04_frame(const uint_least8_t * const frame)
{
    // Disable excitation while the signal buffer is being updated.
    MICRO_DP.excitation.enable = false;

    // Extract signal configuration from the frame.
    ptrdiff_t start_index        = 2 * (ptrdiff_t)BYTES_TO_UINT32(frame[2], frame[3], frame[4], frame[5]);
    const uint32_t signal_period = BYTES_TO_UINT32(frame[6], frame[7], frame[8], frame[9]);
    const size_t signal_length   = (size_t)frame[10];

    // Check number of samples for generating excitation signal.
    if (start_index + (2 * signal_length) > (ptrdiff_t)MICRO_DP.trigger.samples_count)
    {
        return DP_ERROR;
    }


    // Deserialize the signal chunk into the sample buffer.
    const uint_least8_t * payload = &frame[11];

    for (ptrdiff_t i = 0; i < (ptrdiff_t)signal_length; i++)
    {
#if DP_BYTE_SIZE == 8
        MICRO_DP.mem.var_samples[start_index].uint8_array[0] = payload[(4 * i) + 0];
        MICRO_DP.mem.var_samples[start_index].uint8_array[1] = payload[(4 * i) + 1];
        MICRO_DP.mem.var_samples[start_index].uint8_array[2] = payload[(4 * i) + 2];
        MICRO_DP.mem.var_samples[start_index].uint8_array[3] = payload[(4 * i) + 3];
#elif DP_BYTE_SIZE == 16
        MICRO_DP.mem.var_samples[start_index].uint16_array[0] = BYTES_TO_UINT16(payload[(4 * i) + 0], payload[(4 * i) + 1]);
        MICRO_DP.mem.var_samples[start_index].uint16_array[1] = BYTES_TO_UINT16(payload[(4 * i) + 2], payload[(4 * i) + 3]);
#endif

        start_index += 2;
    }

    // Commit the updated signal period to the global state.
    MICRO_DP.excitation.n_period = signal_period;

    if (start_index >= (2 * (ptrdiff_t)MICRO_DP.excitation.n_period))
    {
        MICRO_DP.excitation.n      = 0u;
        MICRO_DP.excitation.enable = true;
    }

    // Synchronize the backup state.
    NULL_MICRO_DP.excitation = MICRO_DP.excitation;

    REGISTER_BUILD_FUNCTION(build_0x04_ack_frame);

    return DP_OK;
}

/**
 * \brief   Build a 0x04 acknowledgement frame to send to the host.
 * 
 * Offset | Size | Description
 * -------|------|-------------
 * 0      | 1    | Node Address
 * 1      | 1    | Frame Mode
 * 2..3   | 2    | CRC-16 over header only (Big-Endian: MSB first, LSB second)
 *
 * \retval  DP_OK: Frame built and transmitted successfully.
 * \retval  DP_ERROR: Transmission failed.
 */
static Exception_DP build_0x04_ack_frame(void)
{
    // Use a local pointer to avoid repetitive dereferencing of the global structure.
    uint_least8_t * const tx_buf = &MICRO_DP.mem.tx_buf[1];

    tx_buf[0] = MICRO_DP.info.node_addr;
    tx_buf[1] = (uint_least8_t)DP_MODE_0x04;

    // CRC-16 over the header (16-bit BE).
    const uint16_t crc = crc16(tx_buf, 2);

    tx_buf[2] = READ_BYTE(crc, 1);
    tx_buf[3] = READ_BYTE(crc, 0);

    cobs_encode(MICRO_DP.mem.tx_buf, 5);

    // Transmit the fully built frame via the hardware callback.
    return MICRO_DP.info.func_transmit(MICRO_DP.mem.tx_buf, 6);
}

/**
 * \brief   Apply the configured excitation signal to the system output.
 *
 * This function is called periodically by the acquisition state machine.
 * It reads the next sample from the loaded waveform buffer and updates the excitation value.
 */
EXPORT void micro_dp_excitation(void)
{
    if (MICRO_DP.excitation.enable)
    {
        // Read the current sample from the waveform buffer.
        MICRO_DP.excitation.value = MICRO_DP.mem.var_samples[2 * (ptrdiff_t)MICRO_DP.excitation.n].float32;

        MICRO_DP.excitation.n++;

        // Wrap the sample index if it reaches the end.
        if (MICRO_DP.excitation.n >= MICRO_DP.excitation.n_period)
        {
            MICRO_DP.excitation.n = 0u;
        }
    }
    else
    {
        MICRO_DP.excitation.value = 0.f;
    }
}

/**
 * \brief   Calculate the tx buffer size required by build_0x04_ack_frame().
 *
 * Uses a stub transmit function to capture the byte count without actually
 * sending data over the physical interface. This is typically called during
 * system initialization to pre-allocate the exact amount of memory needed
 * for the tx buffer.
 *
 * \return  Byte count needed for the 0x04 acknowledgement frame.
 */
EXPORT size_t get_size_build_0x04_ack_frame(void)
{
    // Backup the real transmit callback.
    Exception_DP (* const func_transmit)(const uint_least8_t * const, const size_t) = MICRO_DP.info.func_transmit;

    // Replace it with a stub function.
    // The stub intercepts the transmission request and records the requested
    // frame size into MICRO_DP.mem.stub_size instead of sending it.
    MICRO_DP.info.func_transmit = micro_dp_func_transmit_stub;

    // Execute the builder to trigger the stub and capture the size.
    build_0x04_ack_frame();

    // Restore the original transmit callback.
    MICRO_DP.info.func_transmit = func_transmit;

    return MICRO_DP.mem.stub_size;
}
