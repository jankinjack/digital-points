/**
 * \file    micro_dp_0x03.c
 * \brief   Variable write function (0x03) — direct memory write with write-verify pattern.
 *
 * The 0x03 function allows the host to write a value to a specific memory address.
 * The host sends the variable type, memory address, and value; the node validates
 * the alignment and safely writes the value using a write-verify pattern to ensure
 * data integrity, then responds with a acknowledgement frame.
 */

#include <string.h>

#include "micro_dp.h"
#include "micro_dp_crc16.h"

static Exception_DP build_0x03_ack_frame(void);

/**
 * \brief   Process an incoming 0x03 frame from the host.
 *
 * \param   frame: Pointer to the received frame buffer.
 * 
 * \retval  DP_OK: Frame processed successfully; acknowledgement will be built.
 * \retval  DP_ERROR: Invalid variable type, address, or CRC mismatch.
 */
EXPORT Exception_DP process_0x03_frame(const uint_least8_t * const frame)
{
    // Extract the variable type and memory address.
    const Types_DP type = (Types_DP)frame[2];
    const uintptr_t address = BYTES_TO_UINT32(frame[3], frame[4], frame[5], frame[6]);

    // Validate the variable type and memory alignment.
    if (are_type_and_address_valid(address, type) == -1)
    {
        return DP_ERROR;
    }

    // Calculate frame size and validate CRC-16.
#if DP_BYTE_SIZE == 8
    const size_t size = 7u + TYPE_BYTESIZE[type];
#elif DP_BYTE_SIZE == 16
    const size_t size = 7u + (2u * TYPE_BYTESIZE[type]);
#endif
    const uint16_t crc = crc16(frame, size);

    if (BYTES_TO_UINT16(frame[size], frame[(ptrdiff_t)(size + 1u)]) != crc)
    {
        return DP_ERROR;
    }

#if 0
    // Check if float numbers are inf or NaN.
    if (((type == DP_TYPE_FLOAT32) && !isfinite(*(const float *)(const void *)&frame[7]))
        || ((type == DP_TYPE_FLOAT64) && !isfinite(*(const double *)(const void *)&frame[7])))
    {
        return DP_ERROR;
    }
#endif

    // Safely write the variable value using a write-verify pattern.
    // If the written value doesn't match, retry the write operation.
    uint64_t sample;

    do
    {
        sample = BYTES_TO_UINT64(frame[7], frame[8], frame[9], frame[10], frame[11], frame[12], frame[13], frame[14]);

        (void)memcpy((void *)address, (const void *)&sample, TYPE_BYTESIZE[(ptrdiff_t)type]);

    } while (memcmp((const void *)address, (const void *)&sample, TYPE_BYTESIZE[(ptrdiff_t)type]) != 0);

        // Register the 0x03 acknowledgement response builder.
    REGISTER_BUILD_FUNCTION(build_0x03_ack_frame);

    return DP_OK;
}

/**
 * \brief   Build a 0x03 acknowledgement frame to send to the host.
 * 
 * Offset | Size | Description
 * -------|------|-------------
 * 0      | 1    | Node Address
 * 1      | 1    | Frame Mode
 * 2..3   | 2    | CRC-16 over header only (Big-Endian: MSB fist, LSB second)
 * 4..8   | 5    | Magic Key Terminator (DP_KEY)
 *
 * \retval  DP_OK: Frame built and transmitted successfully.
 * \retval  DP_ERROR: Transmission failed.
 */
static Exception_DP build_0x03_ack_frame(void)
{
    // Use a local pointer to avoid repetitive dereferencing of the global structure.
    uint_least8_t * const tx_buf = MICRO_DP.mem.tx_buf;

    tx_buf[0] = MICRO_DP.info.node_addr;
    tx_buf[1] = (uint_least8_t)DP_MODE_0x03;

    // CRC-16 over the header and payload (16-bit BE).
    const uint16_t crc = crc16(tx_buf, 2);

    tx_buf[2] = READ_BYTE(crc, 1);
    tx_buf[3] = READ_BYTE(crc, 0);

    // Magic Key Terminator.
    memcpy(&tx_buf[4], DP_KEY, 5);

    // Transmit the fully built frame via the hardware callback.
    return MICRO_DP.info.func_transmit(tx_buf, 9u);
}

/**
 * \brief   Calculate the tx buffer size required by build_0x03_ack_frame().
 *
 * Uses a stub transmit function to capture the byte count without actually
 * sending data over the physical interface. This is typically called during
 * system initialization to pre-allocate the exact amount of memory needed
 * for the tx buffer.
 *
 * \return  Bytes count needed for the 0x03 acknowledgement frame.
 */
EXPORT size_t get_size_build_0x03_ack_frame(void)
{
    // Backup the real transmit callback.
    Exception_DP (* const original_func_transmit)(const uint_least8_t * const, const size_t) = MICRO_DP.info.func_transmit;

    // Replace it with a stub function.
    // The stub intercepts the transmission request and records the requested
    // frame size into MICRO_DP.mem.stub_size instead of sending it.
    MICRO_DP.info.func_transmit = micro_dp_func_transmit_stub;

    // Execute the builder to trigger the stub and capture the size.
    build_0x03_ack_frame();

    // Restore the original transmit callback.
    MICRO_DP.info.func_transmit = original_func_transmit;

    return MICRO_DP.mem.stub_size;
}
