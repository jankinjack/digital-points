/**
 * \file    micro_dp_0x01.c
 * \brief   Variable sampling function (0x01) — on-demand memory read and immediate transmission.
 *
 * The 0x01 function allows the host to request real-time values of specific variables.
 * The host sends a payload containing memory addresses and data types; the node validates
 * the alignment, safely reads the current values (via interrupt locking or double-read patterns),
 * and immediately responds with the sampled data and a system clock timestamp.
 */

#include "micro_dp.h"
#include "micro_dp_crc16.h"

static Exception_DP build_0x01_frame(void);

/**
 * \brief   Process an incoming 0x01 frame from the host.
 *
 * \param   frame: Pointer to the received frame buffer.
 * 
 * \retval  DP_OK: Frame processed successfully; response will be built.
 * \retval  DP_ERROR: Invalid variable count, CRC mismatch, or invalid memory alignment.
 */
EXPORT Exception_DP process_0x01_frame(const uint_least8_t * const frame)
{
    // Extract the requested variable count.
    const uint_fast8_t var_count = (uint_fast8_t)frame[2];

    // Validate the variable count and ensure the node is idle and ready.
    if ((var_count == 0u) || (var_count > MICRO_DP.info.max_var_count)
        || (SIGNALS_DP.build_function != NULL) || (MICRO_DP.mode != DP_MODE_IDLE))
    {
        return DP_ERROR;
    }

    // Calculate frame size and validate CRC-16.
    const size_t   size = 3 + (5 * (size_t)var_count);
    const uint16_t crc  = crc16(frame, size);

    if (BYTES_TO_UINT16(frame[size], frame[size + 1u]) != crc)
    {
        return DP_ERROR;
    }

    // Point to the frame payload.
    const uint_least8_t * const payload = &frame[3];

    // Parse and validate each variable configuration.
    for (ptrdiff_t i = 0; i < (ptrdiff_t)var_count; i++)
    {
        const ptrdiff_t j = 5 * i;

        // Extract the variable type and memory address.
        const Types_DP var_type = (Types_DP)payload[j];
        const uintptr_t address = BYTES_TO_UINT32(payload[j + 1], payload[j + 2], payload[j + 3], payload[j + 4]);

        const int_fast8_t address_alignment = are_type_and_address_valid(address, var_type);

        // Validate the variable type and memory alignment.
        // 64-bit variables currently lack proper alignment support.
        if ((address_alignment == -1) ||
            ((address_alignment != 0) && ((var_type == DP_TYPE_INT64) || (var_type == DP_TYPE_UINT64) ||
                (var_type == DP_TYPE_FLOAT64))))
        {
            return DP_ERROR;
        }

#if DP_BYTE_SIZE == 16
        address_alignment = address_alignment >> 1;
#endif

        // Store the validated configuration into the global state.
        MICRO_DP.vars[i].address_alignment = address_alignment;
        MICRO_DP.vars[i].type = var_type;
        MICRO_DP.vars[i].ptr = (Value_DP_Union *)(void *)(address - (uintptr_t)address_alignment);
    }

    // Update the global variable count only after successful validation.
    MICRO_DP.var_count = var_count;

    // Function 0x01 requires an immediate response containing the sampled data.
    return build_0x01_frame();  // REGISTER_BUILD_FUNCTION(build_0x01_frame);
}

/**
 * \brief   Build a 0x01 response frame to send to the host.
 *
 * Offset   | Size | Description
 * ---------|------|-------------
 * 0        | 1    | Node Address
 * 1        | 1    | Frame Mode
 * 2        | 1    | Variable Count
 * 3..M     | Var. | Variables Payload (repeated "Variable Count" times)
 * M+1..M+2 | 2    | CRC-16 over header and payload (16-bit Big-Endian)
 * M+3..M+7 | 5    | Magic Key Terminator (DP_KEY)

 *
 * \retval  DP_OK: Frame built and transmitted successfully.
 * \retval  DP_ERROR: Transmission failed.
 */
static Exception_DP build_0x01_frame(void)
{
    // Use a local pointer to avoid repetitive dereferencing of the global structure.
    uint_least8_t * const tx_buf = MICRO_DP.mem.tx_buf;

    tx_buf[0] = MICRO_DP.info.node_addr;
    tx_buf[1] = (uint_least8_t)DP_MODE_0x01;
    tx_buf[2] = (uint_least8_t)MICRO_DP.var_count;

    ptrdiff_t i = 3;
    
    Value_DP_Union sample[20];
    
    // Read variables.
    read_variable(sample, MICRO_DP.var_count);

    for (ptrdiff_t j = 0; j < (ptrdiff_t)MICRO_DP.var_count; j++)
    {
        // Append the variable type.
        tx_buf[i] = (uint_least8_t)MICRO_DP.vars[j].type;
        i++;

        // Serialize the variable bytes based on the architecture byte size.
        const size_t type_bytesize = TYPE_BYTESIZE[MICRO_DP.vars[j].type];
        const ptrdiff_t address_alignment = (ptrdiff_t)MICRO_DP.vars[j].address_alignment;

#if DP_BYTE_SIZE == 8
        memcpy(&tx_buf[i], &sample[j].uint8_array[address_alignment], type_bytesize);
        i += type_bytesize;
#elif DP_BYTE_SIZE == 16
        memcpy(&tx_buf[i], &sample[j].uint16_array[address_alignment], type_bytesize);
        i += type_bytesize;
#endif
    }

    // CRC-16 over the header and payload (16-bit BE).
    const uint16_t crc = crc16(tx_buf, (size_t)i);

    tx_buf[i] = READ_BYTE(crc, 1);
    i++;
    tx_buf[i] = READ_BYTE(crc, 0);
    i++;

    // Magic Key Terminator.
    memcpy(&tx_buf[i], DP_KEY, 5);
    i += 5;

    // Transmit the fully built frame via the hardware callback.
    return MICRO_DP.info.func_transmit(tx_buf, (size_t)i);
}

/**
 * \brief   Calculate the tx buffer size required by build_0x01_frame().
 *
 * Uses a stub transmit function to capture the byte count without actually
 * sending data over the physical interface. This is typically called during
 * system initialization to pre-allocate the exact amount of memory needed
 * for the tx buffer.
 *
 * \return  Byte count needed for the 0x01 response frame.
 */
EXPORT size_t get_0x01_frame_size(void)
{
    static const float64_t stub_var = 0.;

    // Backup the real transmit callback.
    Exception_DP (* const original_func_transmit)(const uint_least8_t * const, const size_t) = MICRO_DP.info.func_transmit;

    // Backup the current global state.
    const uint_fast8_t original_var_count = MICRO_DP.var_count;

    // Setup the worst-case scenario (maximum variables of the largest type).
    MICRO_DP.var_count = MICRO_DP.info.max_var_count;

    for (ptrdiff_t i = 0; i < (ptrdiff_t)MICRO_DP.var_count; i++)
    {
        MICRO_DP.vars[i].type = DP_TYPE_FLOAT64;
        MICRO_DP.vars[i].address_alignment = 7;
        MICRO_DP.vars[i].ptr = (Value_DP_Union *)&stub_var;
    }

    // Replace it with a stub function.
    // The stub intercepts the transmission request and records the requested
    // frame size into MICRO_DP.mem.stub_size instead of sending it.
    MICRO_DP.info.func_transmit = micro_dp_func_transmit_stub;

    // Execute the builder to trigger the stub and capture the size.
    build_0x01_frame();

    // Restore the original transmit callback.
    MICRO_DP.info.func_transmit = original_func_transmit;

    // Restore the original global state.
    MICRO_DP.var_count = original_var_count;

    for (ptrdiff_t i = 0; i < (ptrdiff_t)MICRO_DP.var_count; i++)
    {
        MICRO_DP.vars[i].type = DP_TYPE_INT8;
        MICRO_DP.vars[i].address_alignment = 0;
        MICRO_DP.vars[i].ptr = NULL;
    }

    return MICRO_DP.mem.stub_size;
}
