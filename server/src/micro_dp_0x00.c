/**
 * \file    micro_dp_0x00.c
 * \brief   Heartbeat function (0x00) - node identification and capability exchange.
 *
 * The 0x00 function initiates the communication between the host and the node.
 * The host sends a heartbeat request; the node validates the protocol version
 * and responds with its system parameters (clock frequency, buffer sizes, etc.).
 */

#include "micro_dp.h"
#include "micro_dp_crc16.h"

static Exception_DP build_0x00_frame(void);

/**
 * \brief   Process an incoming 0x00 (heartbeat) frame from the host.
 *
 * The function checks that the DP version matches the node's firmware.
 * On success, stores the host's address alignment hint,
 * registers the response builder, and resets the node to an idle state (no active measurement).
 *
 * \param   frame: Pointer to the received frame buffer.
 * 
 * \retval  DP_OK: Frame processed successfully; response will be built.
 * \retval  DP_ERROR: Invalid CRC or version mismatch.
 */
EXPORT Exception_DP process_0x00_frame(const uint_least8_t * const frame)
{
    // Validate CRC.
    const uint16_t crc = crc16(frame, 9);
    const bool_t is_crc_valid = (BYTES_TO_UINT16(frame[9], frame[10]) == crc);

    // Validate DP version against the micro_dp's definitions.
    const bool_t is_version_valid = (BYTES_TO_UINT16(frame[3], frame[4]) == DP_VERSION_MAJOR)
        && (BYTES_TO_UINT16(frame[5], frame[6]) == DP_VERSION_MINOR)
        && (BYTES_TO_UINT16(frame[7], frame[8]) == DP_VERSION_PATCH);

    if (is_crc_valid && is_version_valid)
    {
        // Store the address alignment hint to subsequently validate variable addresses.
        MICRO_DP.mem.address_alignment = frame[2];

        // Register the 0x00 response builder.
        // This function will be called by the background to build the reply.
        REGISTER_BUILD_FUNCTION(build_0x00_frame);

        // Function 0x00 acts as an "idle" signal - no measurement is in progress.
        // Reset all internal measurement states and disable any active excitation.
        micro_dp_reset();
        MICRO_DP.excitation.enable = false;

        return DP_OK;
    }

    // Reject the frame if CRC or version validation fails.
    return DP_ERROR;
}

/**
 * \brief   Build a 0x00 (heartbeat response) frame to send to the host.
 *
 * The response carries the node's identity and capabilities:
 * system clock frequency, sampling frequency, trigger buffer size,
 * tx chunk size, and variable count.
 * 
 * Offset | Size | Description
 * -------|------|-------------
 * 0      | 1    | Node Address
 * 1      | 1    | Frame Mode
 * 2..5   | 4    | System Clock Frequency [Hz] (32-bit Little-Endian)
 * 6..9   | 4    | Sampling Frequency [Hz] (32-bit Little-Endian)
 * 10..13 | 4    | Trigger Sample Count (32-bit Little-Endian)
 * 14..15 | 2    | Samples count per frame to transmit in Triggered Mode (16-bit Little-Endian)
 * 16     | 1    | Maximum variable count
 * 17..18 | 2    | CRC-16 over header and payload (16-bit Big-Endian: MSB first, LSB second)
 * 19..23 | 5    | Magic Key Terminator (DP_KEY)
 *
 * \retval  DP_OK: Frame built and transmitted successfully.
 * \retval  DP_ERROR: Transmission failed.
 */
static Exception_DP build_0x00_frame(void)
{
    // Use a local pointer to avoid repetitive dereferencing of the global structure.
    uint_least8_t * const tx_buf = MICRO_DP.mem.tx_buf;

    tx_buf[0] = MICRO_DP.info.node_addr;
    tx_buf[1] = (uint_least8_t)DP_MODE_0x00;

    // System Clock Frequency (32-bit LE), [Hz].
    tx_buf[2]  = READ_BYTE(MICRO_DP.info.sys_clk_freq, 0);
    tx_buf[3]  = READ_BYTE(MICRO_DP.info.sys_clk_freq, 1);
    tx_buf[4]  = READ_BYTE(MICRO_DP.info.sys_clk_freq, 2);
    tx_buf[5]  = READ_BYTE(MICRO_DP.info.sys_clk_freq, 3);

    // Sampling Frequency (32-bit LE), [Hz].
    tx_buf[6]  = READ_BYTE(MICRO_DP.info.sampling_freq, 0);
    tx_buf[7]  = READ_BYTE(MICRO_DP.info.sampling_freq, 1);
    tx_buf[8]  = READ_BYTE(MICRO_DP.info.sampling_freq, 2);
    tx_buf[9]  = READ_BYTE(MICRO_DP.info.sampling_freq, 3);

    // Trigger Sample Count (32-bit LE).
    tx_buf[10] = READ_BYTE(MICRO_DP.trigger.samples_count, 0);
    tx_buf[11] = READ_BYTE(MICRO_DP.trigger.samples_count, 1);
    tx_buf[12] = READ_BYTE(MICRO_DP.trigger.samples_count, 2);
    tx_buf[13] = READ_BYTE(MICRO_DP.trigger.samples_count, 3);

    // Samples count per frame to transmit in Triggered Mode (16-bit LE).
    tx_buf[14] = READ_BYTE(MICRO_DP.mem.samples_count_tx_0x02, 0);
    tx_buf[15] = READ_BYTE(MICRO_DP.mem.samples_count_tx_0x02, 1);

    // Maximum variable count.
    tx_buf[16] = READ_BYTE(MICRO_DP.info.max_var_count, 0);

    // CRC-16 over the header and payload (16-bit BE).
    const uint16_t crc = crc16(tx_buf, 17);
    tx_buf[17] = READ_BYTE(crc, 1);
    tx_buf[18] = READ_BYTE(crc, 0);

    // Magic Key Terminator.
    memcpy(&tx_buf[19], DP_KEY, 5);

    // Transmit the fully built frame via the hardware callback.
    return MICRO_DP.info.func_transmit(tx_buf, 24u);
}

/**
 * \brief   Calculate the tx buffer size required by build_0x00_frame().
 *
 * Uses a stub transmit function to capture the byte count without actually
 * sending data over the physical interface. This is typically called during
 * system initialization to pre-allocate the exact amount of memory needed
 * for the tx buffer.
 *
 * \return  Byte count needed for the 0x00 response frame.
 */
EXPORT size_t get_0x00_frame_size(void)
{
    // Backup the real transmit callback.
    Exception_DP (* const original_func_transmit)(const uint_least8_t * const, const size_t) = MICRO_DP.info.func_transmit;

    // Replace it with a stub function.
    // The stub intercepts the transmission request and records the requested
    // frame size into MICRO_DP.mem.stub_size instead of sending it.
    MICRO_DP.info.func_transmit = micro_dp_func_transmit_stub;

    // Execute the builder to trigger the stub and capture the size.
    build_0x00_frame();

    // Restore the original transmit callback.
    MICRO_DP.info.func_transmit = original_func_transmit;

    return MICRO_DP.mem.stub_size;
}
