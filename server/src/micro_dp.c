/**
 * \file    micro_dp.c
 * \brief   Core initialization, memory management, and execution context for the MicroDP protocol.
 *
 * This module implements the main state machine, dynamic memory allocation within a static buffer,
 * and the RX/TX frame processing pipeline. It serves as the central hub for all MicroDP functions.
 */

#include <stdalign.h>
#include <string.h>

#include "micro_dp.h"
#include "micro_dp_crc16.h"

static inline void *micro_dp_calloc(const void * const, const size_t, const size_t, const size_t);
static inline void micro_dp_free(void);

const size_t TYPE_BYTESIZE[DP_TYPE_END] = {
#if DP_BYTE_SIZE == 8
    [DP_TYPE_INT8] = 1,  [DP_TYPE_UINT8] = 1,  [DP_TYPE_INT16] = 2,   [DP_TYPE_UINT16] = 2,  [DP_TYPE_INT32] = 4, [DP_TYPE_UINT32] = 4,
    [DP_TYPE_INT64] = 8, [DP_TYPE_UINT64] = 8, [DP_TYPE_FLOAT32] = 4, [DP_TYPE_FLOAT64] = 8, [DP_TYPE_FRA] = 4,   [DP_TYPE_IMMEDIATE] = 4,
#elif DP_BYTE_SIZE == 16
    [DP_TYPE_INT16] = 1,  [DP_TYPE_UINT16] = 1,  [DP_TYPE_INT32] = 2,   [DP_TYPE_UINT32] = 2, [DP_TYPE_INT64] = 4,
    [DP_TYPE_UINT64] = 4, [DP_TYPE_FLOAT32] = 2, [DP_TYPE_FLOAT64] = 4, [DP_TYPE_FRA] = 2,    [DP_TYPE_IMMEDIATE] = 2,
#endif
};

static const size_t TYPE_ALIGNMENT[DP_TYPE_END] = {
#if DP_BYTE_SIZE == 8
    [DP_TYPE_INT8]      = alignof(int8_t),      [DP_TYPE_UINT8]     = alignof(uint8_t),
#endif
    [DP_TYPE_INT16]     = alignof(int16_t),     [DP_TYPE_UINT16]    = alignof(uint16_t),
    [DP_TYPE_INT32]     = alignof(int32_t),     [DP_TYPE_UINT32]    = alignof(uint32_t),
    [DP_TYPE_INT64]     = alignof(int64_t),     [DP_TYPE_UINT64]    = alignof(uint64_t),
    [DP_TYPE_FLOAT32]   = alignof(float32_t),   [DP_TYPE_FLOAT64]   = alignof(float64_t),
    [DP_TYPE_FRA]       = alignof(float32_t),   [DP_TYPE_IMMEDIATE] = alignof(Value_DP_Union),
};

// The main structure.
Micro_DP_Struct MICRO_DP      = { 0 };

// Reset state snapshot used to restore the initial configuration.
Micro_DP_Struct NULL_MICRO_DP = { 0 };

// Inter-module signal routing structure.
Signals_DP_Struct SIGNALS_DP = { 0 };

static Exception_DP (* const PROCESS_FUNCTION[DP_MODE_END])(const uint_least8_t * const) = {
    [DP_MODE_0x00] = process_0x00_frame,           [DP_MODE_0x01] = process_0x01_frame, [DP_MODE_0x02] = process_0x02_frame,
    [DP_MODE_0x03] = process_0x03_frame,           [DP_MODE_0x04] = process_0x04_frame,

    [DP_MODE_0x02_ACK] = process_0x02_ack_frame,
};

/**
 * \brief   Initialize the MicroDP protocol engine and allocate required memory.
 *
 * \param   info: Pointer to a structure with user-defined hardware parameters.
 *
 * \retval  DP_OK: Initialization successful.
 * \retval  DP_ERROR: Invalid configuration or memory allocation failed.
 */
EXPORT Exception_DP micro_dp_init(Info_DP_Struct * const info)
{
    MICRO_DP = NULL_MICRO_DP;

    // Store the hardware configuration.
    MICRO_DP.info = *info;

    // Limit the maximum number of variables to safe bounds.
    MICRO_DP.info.max_var_count = DP_CLAMP(MICRO_DP.info.max_var_count, 4u, 20u);

    // Validate required hardware callbacks.
    if ((MICRO_DP.info.func_transmit == NULL)
        || (MICRO_DP.info.static_buffer == NULL))
    {
        return DP_ERROR;
    }

    // Prevent re-initialization.
    if (MICRO_DP.mem.initialized)
    {
        return DP_ERROR;
    }

    // Expand valid RAM memory range to maximum if boundaries are not defined or invalid.
    if (MICRO_DP.info.valid_min_addr >= MICRO_DP.info.valid_max_addr)
    {
        MICRO_DP.info.valid_min_addr = 0u;
        MICRO_DP.info.valid_max_addr = UINTPTR_MAX;
    }

    // Set default address alignment.
    MICRO_DP.mem.address_alignment = 1u;

    // Allocate memory for variable configurations.
    MICRO_DP.vars = (Var_DP_Struct *)micro_dp_calloc(
        MICRO_DP.info.static_buffer,
        MICRO_DP.info.max_var_count,
        sizeof(Var_DP_Struct),
        MICRO_DP.info.memory_limit
    );

    if (MICRO_DP.vars == NULL)
    {
        goto FREE_MEMORY;
    }

    // Compute the initial buffer size for tx/rx buffers (placeholder allocation).
    const size_t buf_size = MICRO_DP.info.memory_limit / 2 - (MICRO_DP.info.max_var_count + 1) * sizeof(Var_DP_Struct) / 2;

    MICRO_DP.mem.tx_buf = (uint_least8_t *)micro_dp_calloc(
        MICRO_DP.info.static_buffer,
        buf_size,
        sizeof(uint_least8_t),
        MICRO_DP.info.memory_limit
    );

    if (MICRO_DP.mem.tx_buf == NULL)
    {
        goto FREE_MEMORY;
    }

    MICRO_DP.mem.rx_buf = (uint_least8_t *)micro_dp_calloc(
        MICRO_DP.info.static_buffer,
        buf_size,
        sizeof(uint_least8_t),
        MICRO_DP.info.memory_limit
    );

    if (MICRO_DP.mem.rx_buf == NULL)
    {
        goto FREE_MEMORY;
    }

    MICRO_DP.mem.var_samples = (Value_DP_Union *)micro_dp_calloc(
        MICRO_DP.info.static_buffer,
        1,
        sizeof(Value_DP_Union),
        MICRO_DP.info.memory_limit
    );

    if (MICRO_DP.mem.var_samples == NULL)
    {
        goto FREE_MEMORY;
    }

    // Calculate the maximum required transmit buffer size across all functions.
    MICRO_DP.mem.max_size_tx = DP_MAX(get_0x00_frame_size(), get_0x01_frame_size());
    MICRO_DP.mem.max_size_tx = DP_MAX(MICRO_DP.mem.max_size_tx, get_size_build_0x02_ack_frame());
    MICRO_DP.mem.max_size_tx = DP_MAX(MICRO_DP.mem.max_size_tx, get_0x02_frame_size());
    MICRO_DP.mem.max_size_tx = DP_MAX(MICRO_DP.mem.max_size_tx, get_size_build_0x03_ack_frame());
    MICRO_DP.mem.max_size_tx = DP_MAX(MICRO_DP.mem.max_size_tx, get_size_build_0x04_ack_frame());

    micro_dp_free();

    // Allocate memory for variable configurations
    // again after free.
    MICRO_DP.vars = (Var_DP_Struct *)micro_dp_calloc(
        MICRO_DP.info.static_buffer,
        MICRO_DP.info.max_var_count,
        sizeof(Var_DP_Struct),
        MICRO_DP.info.memory_limit
    );

    if (MICRO_DP.vars == NULL)
    {
        goto FREE_MEMORY;
    }

    // Calculate the optimal number of samples per transmission chunk for function 0x02.
    // 10u = Header (7) + CRC (2) + Overhead (1)
    MICRO_DP.mem.samples_count_tx_0x02 =
        (uint_fast16_t)(((uint_fast32_t)MICRO_DP.mem.max_size_tx - 10u - (2u * MICRO_DP.info.max_var_count)) / (8u * MICRO_DP.info.max_var_count));

    // Recompute the exact tx buffer size based on the calculated chunk size.
    MICRO_DP.mem.max_size_tx = 10u + (MICRO_DP.mem.samples_count_tx_0x02 * (8u * MICRO_DP.info.max_var_count)) + (2u * MICRO_DP.info.max_var_count);

    // Calculate the maximum required receive buffer size across all functions.
    const size_t rx_max_size_0x00 = 9u + 4u;
    const size_t rx_max_size_0x01 = 3u + (5u * MICRO_DP.info.max_var_count) + 4u;
    const size_t rx_max_size_0x02 = 19u + 8u + (5u * MICRO_DP.info.max_var_count) + 4u;
    const size_t rx_max_size_0x03 = 7u + 8u + 4u;
    const size_t rx_max_size_0x04 = 11u + (4u * 20u) + 4u;

    MICRO_DP.mem.rx_buf_size = DP_MAX(rx_max_size_0x00, rx_max_size_0x01);
    MICRO_DP.mem.rx_buf_size = DP_MAX(MICRO_DP.mem.rx_buf_size, rx_max_size_0x02);
    MICRO_DP.mem.rx_buf_size = DP_MAX(MICRO_DP.mem.rx_buf_size, rx_max_size_0x03);
    MICRO_DP.mem.rx_buf_size = DP_MAX(MICRO_DP.mem.rx_buf_size, rx_max_size_0x04);

    // Allocate memory for the receive buffer.
    MICRO_DP.mem.rx_buf =
        (uint_least8_t *)micro_dp_calloc(MICRO_DP.info.static_buffer, MICRO_DP.mem.rx_buf_size, sizeof(uint_least8_t), MICRO_DP.info.memory_limit);

    if (MICRO_DP.mem.rx_buf == NULL)
    {
        goto FREE_MEMORY;
    }

    // Allocate memory for the transmit buffer.
    MICRO_DP.mem.tx_buf =
        (uint_least8_t *)micro_dp_calloc(MICRO_DP.info.static_buffer, MICRO_DP.mem.max_size_tx, sizeof(uint_least8_t), MICRO_DP.info.memory_limit);

    // Check if the memory hasn't been allocated.
    if (MICRO_DP.mem.tx_buf == NULL)
    {
        goto FREE_MEMORY;
    }

    // Compute the maximum possible number of samples according to the memory limitation.
    MICRO_DP.trigger.samples_count = MICRO_DP.info.memory_limit / sizeof(Value_DP_Union);

    // Iteratively attempt to allocate the circular sample buffer, reducing the size if necessary.
    do
    {
        MICRO_DP.mem.var_samples =
            (Value_DP_Union *)micro_dp_calloc(MICRO_DP.info.static_buffer, MICRO_DP.trigger.samples_count, sizeof(Value_DP_Union), MICRO_DP.info.memory_limit);
        MICRO_DP.trigger.samples_count--;

    } while ((MICRO_DP.mem.var_samples == NULL) && (MICRO_DP.trigger.samples_count != 0u));

    if (MICRO_DP.mem.var_samples == NULL)
    {
        goto FREE_MEMORY;
    }

    MICRO_DP.mem.initialized = true;

    // Save the successfully allocated state as the reset snapshot.
    NULL_MICRO_DP.info                  = MICRO_DP.info;
    NULL_MICRO_DP.mem                   = MICRO_DP.mem;
    NULL_MICRO_DP.vars                  = MICRO_DP.vars;
    NULL_MICRO_DP.tx_samples_count      = MICRO_DP.tx_samples_count;
    NULL_MICRO_DP.trigger.samples_count = MICRO_DP.trigger.samples_count;

#ifdef MICRO_DP_EXPORTS
    srand(1000u);
#endif

    return DP_OK;

FREE_MEMORY:
    micro_dp_free();

    return DP_ERROR;
}

/**
 * \brief   Execute the fast loop (high-priority periodic tasks).
 *
 * \return  Current excitation value to be applied to the system.
 */
EXPORT float micro_dp_context(void)
{
    // Collect variables.
    if (MICRO_DP.mode == DP_MODE_0x02)
    {
        return collect_0x02_vars();
    }

    return 0.f;
}

/**
 * \brief   Execute the background loop (low-priority frame processing and transmission).
 *
 * \retval  DP_OK: All pending tasks processed successfully.
 * \retval  DP_ERROR: An error occurred during frame processing or transmission.
 */
EXPORT Exception_DP micro_dp_background(void)
{
    Exception_DP exception = DP_OK;

    Exception_DP (* const store_process_function)(const uint_least8_t *) = SIGNALS_DP.process_function;

    // Process incoming frames.
    if (store_process_function != NULL)
    {
        UNREGISTER_PROCESS_FUNCTION();
        exception = store_process_function(&MICRO_DP.mem.rx_buf[1]);
    }

    if (!MICRO_DP.mem.initialized)
    {
        return DP_OK;
    }

    // Build and transmit response frames.
    Exception_DP (* const store_build_function)(void) = SIGNALS_DP.build_function;

    if (store_build_function != NULL)
    {
        UNREGISTER_BUILD_FUNCTION();
        exception = store_build_function();
    }

    return exception;
}

/**
 * \brief   Process an incoming data chunk from the physical interface.
 *
 * \param   chunk: Pointer to the received data chunk.
 * \param   size: Number of bytes in the chunk.
 */
EXPORT void micro_dp_handle_rx_chunk(const uint_least8_t * const chunk, const size_t size)
{
    if (!MICRO_DP.mem.initialized || (chunk == NULL))
    {
        return;
    }

    // Disable interrupts to protect shared state.
    SAFE_CALL(MICRO_DP.info.disable_interrupts);

    for (ptrdiff_t i = 0; i < size; i++)
    {
        const uint_least8_t byte = chunk[i];

        // Store the byte in the circular receive buffer.
        MICRO_DP.mem.rx_buf[MICRO_DP.mem.rx_buf_ptr] = byte;
        MICRO_DP.mem.rx_buf_ptr++;

        if (MICRO_DP.mem.rx_buf_ptr >= MICRO_DP.mem.rx_buf_size)
        {
            MICRO_DP.mem.rx_buf_ptr = 0;
        }

        // Find the delimiter byte to detect the end of a frame.
        if (byte == 0x00)
        {
            cobs_decode(MICRO_DP.mem.rx_buf, MICRO_DP.mem.rx_buf_ptr - 1);

            const uint_least8_t * const frame = &MICRO_DP.mem.rx_buf[1];
            const uint_least8_t node_addr = frame[0];
            const Modes_DP mode = (Modes_DP)frame[1];

            // Validate that the frame is addressed to this node,
            // the function is supported, and the CRC is valid.
            if ((node_addr == MICRO_DP.info.node_addr) && (mode < DP_MODE_END))
            {
                const size_t frame_data_size = MICRO_DP.mem.rx_buf_ptr - 4;
                const uint16_t crc = crc16(frame, frame_data_size);

                if (BYTES_TO_UINT16(frame[frame_data_size], frame[frame_data_size + 1]) == crc)
                {
                    // Process the frame.
                    REGISTER_PROCESS_FUNCTION(PROCESS_FUNCTION[(ptrdiff_t)mode]);
                }
            }

            MICRO_DP.mem.rx_buf_ptr = 0;
        }
    }

    SAFE_CALL(MICRO_DP.info.enable_interrupts);
}

/**
 * \brief   Reset the MicroDP state machine to its initial configuration.
 */
EXPORT void micro_dp_reset(void)
{
    // Disable interrupts to protect shared state.
    SAFE_CALL(MICRO_DP.info.disable_interrupts);
    MICRO_DP = NULL_MICRO_DP;
    if (MICRO_DP.vars != NULL)
    {
        memset((void *)MICRO_DP.vars, 0, MICRO_DP.info.max_var_count * sizeof(Var_DP_Struct));
    }
    SAFE_CALL(MICRO_DP.info.enable_interrupts);
}

/**
 * \brief   Validate a variable's type and memory address, returning the alignment remainder.
 *
 * \param   address: The memory address to validate.
 * \param   type: The data type expected at the address.
 *
 * \return  The alignment remainder (>= 0) if valid, or -1 if invalid.
 */
EXPORT int_fast8_t are_type_and_address_valid(const uintptr_t address, const Types_DP type)
{
    const bool_t is_type_valid = (type >= DP_TYPE_INT8) && (type < DP_TYPE_END);
    const bool_t is_addr_in_range = (address >= MICRO_DP.info.valid_min_addr) &&
                                    ((address + (uintptr_t)TYPE_BYTESIZE[type] - 1u) <= MICRO_DP.info.valid_max_addr);
    const bool_t is_naturally_aligned = (address % TYPE_ALIGNMENT[type]) == 0u;

    if (is_type_valid && is_addr_in_range && is_naturally_aligned)
    {
        return (int_fast8_t)(address % MICRO_DP.mem.address_alignment);
    }

    return -1;
}

/**
 * \brief   Allocate and zero-initialize memory from a static buffer.
 *
 * \param   buf: Pointer to the static memory buffer.
 * \param   count: Number of elements to allocate.
 * \param   size: Size of each element in bytes.
 * \param   memory_limit: Maximum allowed allocation size within the static buffer.
 *
 * \return  Pointer to the allocated and zeroed memory, or NULL if out of memory.
 */
static inline void *micro_dp_calloc(const void * const buf, const size_t count, const size_t size, const size_t memory_limit)
{
    if ((buf != NULL) && (memory_limit > 0u))
    {
        const size_t alloc_size = size * count;
        static const size_t alignment = alignof(int);

        // Calculate the offset aligned to the system's integer boundary.
        const size_t offset = ((MICRO_DP.mem.alloc_end + alignment - 1u) / alignment) * alignment;

        if ((offset + alloc_size) <= memory_limit)
        {
            void * const alloc_start = (void *)((ptrdiff_t)buf + (ptrdiff_t)offset);

            MICRO_DP.mem.alloc_end = offset + alloc_size;

            return memset(alloc_start, 0, alloc_size);
        }
    }

    return NULL;
}

/**
 * \brief   Release all memory allocated from the static buffer.
 */
static inline void micro_dp_free(void)
{
    MICRO_DP.mem.alloc_end = 0;
}

/**
 * \brief   Read variable values.
 *
 * \param   dest: pointer to a destination.
 * \param   var_count: amount of variable to read.
 *
 */
void read_variable(Value_DP_Union * const dest, const size_t var_count)
{
    if (dest == NULL)
    {
        return;
    }
    
    // Fastest path: sampling without interrupt management.
    if (MICRO_DP.info.uninterrupted)
    {
        for (ptrdiff_t i = 0; i < var_count; i++)
        {
#ifndef MICRO_DP_EXPORTS
            (void)memcpy((void *)&dest[i], (const void *)MICRO_DP.vars[i].ptr, sizeof(Value_DP_Union));
#else
            dest[i].float32 = (float)rand() / (float)RAND_MAX;
#endif
        }
    }
    // Medium path: sampling with interrupt locking.
    else if (MICRO_DP.info.disable_interrupts != NULL)
    {
        MICRO_DP.info.disable_interrupts();

        for (ptrdiff_t i = 0; i < var_count; i++)
        {
#ifndef MICRO_DP_EXPORTS
            (void)memcpy(&dest[i], MICRO_DP.vars[i].ptr, sizeof(Value_DP_Union));
#else
            dest[i].float32 = (float)rand() / (float)RAND_MAX;
#endif
        }

        MICRO_DP.info.enable_interrupts();
    }
    // Slowest path: sampling with double-read pattern for concurrent access safety.
    else
    {
        for (ptrdiff_t i = 0; i < var_count; i++)
        {
            const volatile Value_DP_Union * const src = MICRO_DP.vars[i].ptr;
            volatile Value_DP_Union sample;
            volatile Value_DP_Union sample_check;

            // Safely read the variable value using a double-read pattern.
            // If the reads mismatch, the value was updated concurrently and must be re-read.
            do
            {
#ifndef MICRO_DP_EXPORTS
                (void)memcpy((void *)&sample, (const void *)src, sizeof(Value_DP_Union));
                (void)memcpy((void *)&sample_check, (const void *)src, sizeof(Value_DP_Union));
#else
                sample.float32 = (float)rand() / (float)RAND_MAX;
                sample_check.float32 = sample.float32;
#endif

            } while (memcmp((void *)&sample, (void *)&sample_check, sizeof(Value_DP_Union)) != 0);

            dest[i] = sample;
        }
    }
}

/**
 * \brief   COBS encode: insert length bytes to eliminate interior zero bytes.
 *
 * The caller must have prepended a 0x00 byte before the data block. This
 * sentinel guarantees the backward search always terminates without
 * out-of-bounds access. The function modifies the buffer in-place and
 * appends a trailing 0x00 terminator.
 *
 * \param   buffer: Pointer to the data buffer (must have 1 extra byte at end).
 * \param   size: Number of data bytes (excluding the prepended and appended 0x00).
 */
void cobs_encode(uint_least8_t * const buffer, const size_t size)
{
    // Sentinel at buffer[-1] is guaranteed by caller; start at last data byte.
    const uint_least8_t * end_of_block = &buffer[size - 1];

    // Prepend a 0x00 terminator (COBS overhead byte).
    // Also serves as a sentinel so the backward search never underflows.
    buffer[0] = 0x00;

    uint_least8_t * cursor;

    do
    {
        // Search backward for the next 0x00 byte.
        // The prepended 0x00 at buffer[0] guarantees termination.
        for (cursor = (uint_least8_t *)end_of_block; *cursor != 0x00u; cursor--)
        {
        }

        // Replace the 0x00 with the distance to the previous 0x00 (1-indexed).
        *cursor = (uint_least8_t)(end_of_block - cursor + 1);

        // Move to the preceding block.
        end_of_block = cursor - 1;

    } while (cursor > buffer);

    // If the original data started with 0x00, the loop wrote 0x00 at buffer[0].
    // COBS spec: a block-length of 0 is invalid, so use 0x01 (block of length 1
    // containing just the implicit zero).
    if (buffer[0] == 0x00u)
    {
        buffer[0] = 0x01u;
    }

    // Append the trailing 0x00 frame terminator.
    buffer[size] = 0x00u;
}

/**
 * \brief   COBS decode: remove length bytes and restore zero bytes.
 *
 * The function modifies the buffer in-place, shrinking the data. It returns
 * early when it encounters a block-length of 0 (end of valid encoded data),
 * leaving any trailing bytes untouched.
 *
 * \param   buffer: Pointer to the COBS-encoded buffer (modified in-place).
 * \param   size: Total number of bytes in the buffer.
 */
void cobs_decode(uint_least8_t * buffer, const size_t size)
{
    const uint_least8_t * const end_of_buffer = buffer + size - 1;

    do
    {
        const uint_least8_t tmp = *buffer;

        // Block-length of 0 signals end of valid encoded data.
        // Return early, leaving any trailing bytes unmodified.
        if (tmp == 0)
        {
            return;
        }

        // Zero out the block-length byte and advance by that many positions.
        *buffer = 0x00u;
        buffer += tmp;

    } while (buffer < end_of_buffer);
}

/**
 * \brief   Stub transmit function used to calculate frame sizes without actual transmission.
 *
 * \param   frame: Pointer to the frame buffer (ignored).
 * \param   size: Number of bytes in the frame.
 *
 * \retval  DP_OK: Always succeeds.
 */
EXPORT Exception_DP micro_dp_func_transmit_stub(const uint_least8_t * const frame, const size_t size)
{
    MICRO_DP.mem.stub_size = size;
    return DP_OK;
}
