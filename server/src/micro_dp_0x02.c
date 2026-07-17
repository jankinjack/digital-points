/**
 * \file    micro_dp_0x02.c
 * \brief   Triggered acquisition function (0x02) — circular buffering and edge-triggered data capture.
 *
 * The 0x02 function implements a continuous data acquisition system with a circular buffer.
 * It supports pre-trigger and post-trigger sample collection, configurable decimation,
 * and various edge-triggered conditions. Upon a trigger event, the captured data is
 * transmitted to the host in chunked frames with an acknowledgement mechanism.
 */

#include <string.h>

#include "micro_dp.h"
#include "micro_dp_crc16.h"

static inline bool_t is_trigger_occurred(void);
static inline void common_collect(void);

static Exception_DP build_0x02_ack_frame(void);
static Exception_DP build_0x02_frame(void);

/**
 * \brief   State machine for collecting 0x02 triggered samples.
 *
 * \return  Current excitation value to be applied to the system.
 */
EXPORT float32_t collect_0x02_vars(void)
{
    switch (MICRO_DP.stage_0x02)
    {
        case DP_0x02_STAGE_PRE_PROCESS:
        {
            // Wait for the settling time to expire.
            if (MICRO_DP.trigger.settling_time_count < MICRO_DP.trigger.settling_time)
            {
                micro_dp_excitation();
                MICRO_DP.trigger.settling_time_count++;
            }
            else if (MICRO_DP.trigger.pre_trigger > 0u)
            {
                // Apply decimation (sample rate division).
                if (++MICRO_DP.sample_count_count >= MICRO_DP.sample_count)
                {
                    MICRO_DP.sample_count_count = 0u;

                    common_collect();

                    // Wait for the circular buffer to be fully populated for the first time.
                    if (MICRO_DP.trigger.current_pointer >= MICRO_DP.trigger.fill_pointer)
                    {
                        MICRO_DP.stage_0x02 = DP_0x02_STAGE_PRE_COLLECT;
                    }
                }
            }
            else
            {
                MICRO_DP.stage_0x02 = DP_0x02_STAGE_PRE_COLLECT;
            }
        } break;

        case DP_0x02_STAGE_PRE_COLLECT:
        {
            // Apply decimation (sample rate division).
            if (++MICRO_DP.sample_count_count >= MICRO_DP.sample_count)
            {
                MICRO_DP.sample_count_count = 0u;

                // Prevent buffer overwriting when excitation is enabled.
                if (!MICRO_DP.excitation.enable)
                {
                    common_collect();
                }
                else
                {
                    micro_dp_excitation();
                }

                // Check if a trigger event has occurred.
                if (is_trigger_occurred())
                {
                    // Transition to post-trigger collection stage.
                    MICRO_DP.stage_0x02 = DP_0x02_STAGE_POST_COLLECT;

                    // Record the buffer position at the moment of the trigger event.
                    MICRO_DP.trigger.fill_pointer = MICRO_DP.trigger.current_pointer;
                }
            }
        } break;

        case DP_0x02_STAGE_POST_COLLECT:
        {
            // Apply decimation (sample rate division).
            if (++MICRO_DP.sample_count_count >= MICRO_DP.sample_count)
            {
                MICRO_DP.sample_count_count = 0u;

                micro_dp_excitation();
                common_collect();

                // Check if all post-trigger samples have been collected.
                if (++MICRO_DP.trigger.post_trigger_count >= MICRO_DP.trigger.post_trigger)
                {
                    // Disable excitation.
                    MICRO_DP.excitation.enable = false;
                    MICRO_DP.excitation.value  = 0.f;

                    // Transition to transmission stage.
                    MICRO_DP.stage_0x02 = DP_0x02_STAGE_TX;
                    REGISTER_BUILD_FUNCTION(build_0x02_frame);
                }
            }
        } break;

        case DP_0x02_STAGE_IDLE:
        case DP_0x02_STAGE_TX:
        case DP_0x02_STAGE_ACK:
        case DP_0x02_STAGE_WAIT_ACK:
        default:
        {
            // No action.
        } break;
    }

    return MICRO_DP.excitation.value;
}

/**
 * \brief   Acquire samples for all configured variables into the circular buffer.
 */
static inline void common_collect(void)
{
    read_variable(MICRO_DP.trigger.current_pointer, MICRO_DP.var_count);

    MICRO_DP.trigger.current_pointer += MICRO_DP.var_count;

    // Wrap the circular buffer pointer if it reaches the end.
    if (MICRO_DP.trigger.current_pointer >= MICRO_DP.trigger.end_pointer)
    {
        MICRO_DP.trigger.current_pointer = MICRO_DP.mem.var_samples;
    }
}

/**
 * \brief   Process an incoming 0x02 frame from the host.
 *
 * \param   frame: Pointer to the received frame buffer.
 * 
 * \retval  DP_OK: Frame processed successfully; acknowledgement will be built.
 * \retval  DP_ERROR: Invalid configuration, CRC mismatch, or invalid memory alignment.
 */
EXPORT Exception_DP process_0x02_frame(const uint_least8_t * const frame)
{
    micro_dp_reset();

    // Extract trigger configuration.
    Types_DP trigger_type = (Types_DP)frame[2];
    uintptr_t trigger_address;

    // Handle special trigger types.
    if (trigger_type == DP_TYPE_FRA)
    {
        trigger_type = DP_TYPE_UINT32;
        trigger_address = (uintptr_t)&MICRO_DP.excitation.n;
    }
    else if (trigger_type == DP_TYPE_IMMEDIATE)
    {
        // This address will not be used in fact.
        trigger_address = (uintptr_t)&MICRO_DP.trigger.var.aux_value;
    }
    else
    {
        trigger_address = BYTES_TO_UINT32(frame[3], frame[4], frame[5], frame[6]);
    }

    // Validate trigger type and address.
    if ((are_type_and_address_valid(trigger_address, trigger_type) != 0) || (SIGNALS_DP.build_function != NULL)
        || (MICRO_DP.mode != DP_MODE_IDLE))
    {
        goto FREE_0x02;
    }

    // Parse trigger threshold value.
    Value_DP_Union trigger_aux_value;

#if DP_BYTE_SIZE == 8

    (void)memcpy((void *)&trigger_aux_value, (const void *)&frame[7], TYPE_BYTESIZE[(ptrdiff_t)trigger_type]);

    const uint_least8_t * const frame_offset = &frame[7u + TYPE_BYTESIZE[trigger_type]];

#elif DP_BYTE_SIZE == 16

    const uint64_t integer_form = BYTES_TO_UINT64(frame[7], frame[8], frame[9], frame[10], frame[11], frame[12], frame[13], frame[14]);

    (void)memcpy((void *)&trigger_aux_value, (const void *)&integer_form, TYPE_BYTESIZE[(ptrdiff_t)trigger_type]);

    const uint_least8_t * const frame_offset = &frame[7u + 2u * TYPE_BYTESIZE[trigger_type]];

#endif

    // Extract trigger count (minimum 1).
    const uint_fast8_t trigger_count = (frame_offset[0] >= (uint_least8_t)1u) ? ((uint_fast8_t)frame_offset[0]) : (1u);

    // Extract and validate trigger edge.
    const Edge_DP trigger_edge = (Edge_DP)frame_offset[5];

    if (trigger_edge >= DP_EDGE_END)
    {
        goto FREE_0x02;
    }

    // Extract timing parameters.
    const uint_fast32_t settling_time = BYTES_TO_UINT32(frame_offset[6], frame_offset[7], frame_offset[8], frame_offset[9]);
    const uint_fast8_t decimation_factor = (uint_fast8_t)frame_offset[10];

    // Extract and validate variable count.
    const uint_fast8_t var_count = (uint_fast8_t)frame_offset[11];

    if ((var_count == 0u) || (var_count > MICRO_DP.info.max_var_count))
    {
        goto FREE_0x02;
    }

    // Extract pre-trigger and post-trigger sample counts.
    const uint_fast16_t pre_trigger = BYTES_TO_UINT16(frame_offset[1], frame_offset[2]);
    const uint_fast16_t post_trigger = BYTES_TO_UINT16(frame_offset[3], frame_offset[4]);
    const uint_fast32_t samples_per_var = pre_trigger + post_trigger;

    // Validate total sample count against buffer capacity.
    const uint_fast32_t total_samples = samples_per_var * var_count;

    if (total_samples > MICRO_DP.trigger.samples_count)
    {
        goto FREE_0x02;
    }

    // Validate payload CRC-16.
#if DP_BYTE_SIZE == 8
    const size_t size = 19 + TYPE_BYTESIZE[trigger_type] + (5 * (size_t)var_count);
#elif DP_BYTE_SIZE == 16
    const size_t size = 19 + (2 * TYPE_BYTESIZE[trigger_type]) + (5 * (size_t)var_count);
#endif
    const uint16_t crc = crc16(frame, size);

    if (BYTES_TO_UINT16(frame[size], frame[size + 1u]) != crc)
    {
        goto FREE_0x02;
    }

    // Parse and validate variable configurations.
    const uint_least8_t *ptr = &frame_offset[12];

    for (ptrdiff_t i = 0; i < (ptrdiff_t)var_count; i++)
    {
        // Get a type and an address of a variable.
        const Types_DP var_type = (Types_DP)ptr[0];
        const uintptr_t var_address = BYTES_TO_UINT32(ptr[1], ptr[2], ptr[3], ptr[4]);
        int_fast8_t alignment = are_type_and_address_valid(var_address, var_type);

        // Check if the variable's type and address are valid.
        // 64-bit variables are unsupported now with alignment checking...
        if ((alignment == -1) || ((alignment != 0)
                && ((var_type == DP_TYPE_INT64) || (var_type == DP_TYPE_UINT64)
                    || (var_type == DP_TYPE_FLOAT64))))
        {
            goto FREE_0x02;
        }

#if DP_BYTE_SIZE == 16
        alignment = alignment >> 1;
#endif

        MICRO_DP.vars[i].type = var_type;
        MICRO_DP.vars[i].address_alignment = alignment;
        MICRO_DP.vars[i].ptr = (Value_DP_Union *)(void *)(var_address - (uintptr_t)alignment);

        ptr += 5;
    }

    // All validations passed. Commit the parsed configuration to the global state.
    MICRO_DP.trigger.var.type = trigger_type;
    MICRO_DP.trigger.var.ptr = (Value_DP_Union *)(void *)trigger_address;
    MICRO_DP.trigger.var.aux_value = trigger_aux_value;
    MICRO_DP.trigger.count = trigger_count;
    MICRO_DP.trigger.edge = trigger_edge;
    MICRO_DP.trigger.settling_time = settling_time;
    
    MICRO_DP.sample_count = decimation_factor;
    MICRO_DP.var_count = var_count;
    MICRO_DP.trigger.pre_trigger = pre_trigger;
    MICRO_DP.trigger.post_trigger = post_trigger;
    MICRO_DP.trigger.samples_count_per_var = samples_per_var;

    // Initialize circular buffer pointers.
    MICRO_DP.trigger.current_pointer = MICRO_DP.mem.var_samples;
    MICRO_DP.trigger.end_pointer     = MICRO_DP.mem.var_samples + (ptrdiff_t)total_samples;
    MICRO_DP.trigger.fill_pointer    = MICRO_DP.mem.var_samples + (ptrdiff_t)((size_t)pre_trigger * (size_t)var_count);

    // Transition to acknowledgement stage.
    MICRO_DP.mode       = DP_MODE_0x02;
    MICRO_DP.stage_0x02 = DP_0x02_STAGE_ACK;

    REGISTER_BUILD_FUNCTION(build_0x02_ack_frame);

    return DP_OK;

FREE_0x02:
    micro_dp_reset();
    return DP_ERROR;
}

/**
 * \brief   Process an incoming 0x02 acknowledgement frame from the host.
 *
 * \param   frame: Pointer to the received frame buffer.
 * 
 * \retval  DP_OK: Frame processed successfully.
 * \retval  DP_ERROR: Invalid CRC.
 */
EXPORT Exception_DP process_0x02_ack_frame(const uint_least8_t * const frame)
{
    if (MICRO_DP.stage_0x02 != DP_0x02_STAGE_WAIT_ACK)
    {
        return DP_OK;
    }

    const uint16_t crc = crc16(frame, 3);

    if (BYTES_TO_UINT16(frame[3], frame[4]) != crc)
    {
        return DP_ERROR;
    }

    const Transmit_0x02_CMD_DP command = (Transmit_0x02_CMD_DP)frame[2];

    if (command == DP_0x02_TX_CMD_CONTINUE)
    {
        if (MICRO_DP.tx_samples_count >= MICRO_DP.mem.samples_count_tx_0x02)
        {
            MICRO_DP.tx_samples_count -= DP_MIN(MICRO_DP.mem.samples_count_tx_0x02, MICRO_DP.tx_samples_count);
        }

        MICRO_DP.trigger.end = false;
    }
    else if (command == DP_0x02_TX_CMD_RESTART)
    {
        MICRO_DP.tx_samples_count = 0u;

        MICRO_DP.trigger.end = false;
    }
    else if (command == DP_0x02_TX_CMD_START)
    {
        MICRO_DP.stage_0x02 = DP_0x02_STAGE_PRE_PROCESS;
        return DP_OK;
    }
    else
    {
        // No action.
    }

    if (!MICRO_DP.trigger.end)
    {
        MICRO_DP.stage_0x02 = DP_0x02_STAGE_TX;
        REGISTER_BUILD_FUNCTION(build_0x02_frame);
    }
    else
    {
        micro_dp_reset();
    }

    return DP_OK;
}

/**
 * \brief   Build a 0x02 acknowledgement frame to send to the host.
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
static Exception_DP build_0x02_ack_frame(void)
{
    uint_least8_t * const tx_buf = MICRO_DP.mem.tx_buf;

    tx_buf[0] = MICRO_DP.info.node_addr;
    tx_buf[1] = (uint_least8_t)DP_MODE_0x02;

    // CRC-16 over the header (16-bit BE).
    const uint16_t crc = crc16(tx_buf, 2);

    tx_buf[2] = READ_BYTE(crc, 1);
    tx_buf[3] = READ_BYTE(crc, 0);

    // Magic Key Terminator.
    memcpy(&tx_buf[4], DP_KEY, 5);

    MICRO_DP.stage_0x02 = DP_0x02_STAGE_WAIT_ACK;

    // Transmit the fully built frame via the hardware callback.
    return MICRO_DP.info.func_transmit(tx_buf, 9u);
}

/**
 * \brief   Build a 0x02 data frame to send to the host.
 * 
 * Offset   | Size | Description
 * ---------|------|-------------
 * 0        | 1    | Node Address
 * 1        | 1    | Frame Mode
 * 2        | 1    | Last Chunk Flag (0 = intermediate chunk, 1 = final chunk)
 * 3..4     | 2    | Trigger Sample Index (16-bit Little-Endian)
 * 5..6     | 2    | Chunk Size: Samples count per variable in this chunk (16-bit Little-Endian)
 * 7        | 1    | Variable Count (Number of variables in this frame)
 * 8..M     | Var. | Variables Payload (Repeated "Variable Count" times)
 * M+1..M+2 | 2    | CRC-16 over header and payload (Big-Endian: MSB first, LSB second)
 * M+3..M+7 | 5    | Magic Key Terminator (DP_KEY)
 *
 * \retval  DP_OK: Frame built and transmitted successfully.
 * \retval  DP_ERROR: Transmission failed.
 */
static Exception_DP build_0x02_frame(void)
{
    // Use a local pointer to avoid repetitive dereferencing of the global structure.
    uint_least8_t * const tx_buf = MICRO_DP.mem.tx_buf;

    tx_buf[0] = MICRO_DP.info.node_addr;
    tx_buf[1] = (uint_least8_t)DP_MODE_0x02;

    // Calculate the trigger sample index.
    const uint16_t trigger_sample_index = (uint16_t)((ptrdiff_t)(MICRO_DP.trigger.fill_pointer - MICRO_DP.mem.var_samples) / (ptrdiff_t)MICRO_DP.var_count);

    tx_buf[3] = READ_BYTE(trigger_sample_index, 0);
    tx_buf[4] = READ_BYTE(trigger_sample_index, 1);

    // Calculate the number of samples to transmit in this chunk.
    const uint_fast16_t chunk_size = DP_MIN(MICRO_DP.trigger.samples_count_per_var - MICRO_DP.tx_samples_count, MICRO_DP.mem.samples_count_tx_0x02);
    const size_t tx_end = MICRO_DP.tx_samples_count + chunk_size;

    // Number of samples to transmit.
    tx_buf[5] = READ_BYTE(chunk_size, 0);
    tx_buf[6] = READ_BYTE(chunk_size, 1);
    tx_buf[7] = (uint_least8_t)MICRO_DP.var_count;

    ptrdiff_t i = 8u;

    for (ptrdiff_t k = 0; k < (ptrdiff_t)MICRO_DP.var_count; k++)
    {
        tx_buf[i] = (uint_least8_t)k;
        i++;
        tx_buf[i] = (uint_least8_t)MICRO_DP.vars[k].type;
        i++;

        const uintptr_t address_alignment = MICRO_DP.vars[k].address_alignment;
        const size_t valid_bytes = TYPE_BYTESIZE[MICRO_DP.vars[k].type];
        const size_t type_bytesize = valid_bytes + address_alignment;

#if DP_BYTE_SIZE == 8
        const size_t padding = 8u - valid_bytes;
#elif DP_BYTE_SIZE == 16
        const size_t padding = 4u - valid_bytes;
#endif
        
        Value_DP_Union * ptr = &MICRO_DP.mem.var_samples[(MICRO_DP.tx_samples_count * MICRO_DP.var_count) + k];

        for (ptrdiff_t j = 0; j < chunk_size; j++)
        {
            memcpy(&tx_buf[i], &ptr->uint8_array[address_alignment], valid_bytes);
            i += valid_bytes;
            
            memset(&tx_buf[i], 0, padding);
            i += padding;

            ptr += MICRO_DP.var_count;
        }
    }

    MICRO_DP.tx_samples_count += chunk_size;

    // Check if this is the last chunk.
    if (MICRO_DP.tx_samples_count >= MICRO_DP.trigger.samples_count_per_var)
    {
        tx_buf[2] = (uint_least8_t)DP_0x02_TX_CHUNK_FINAL;
        MICRO_DP.trigger.end = true;
    }
    else
    {
        tx_buf[2] = (uint_least8_t)DP_0x02_TX_CHUNK_INTERMEDIATE;
    }

    // CRC-16 over the header and payload (16-bit BE).
    const uint16_t crc = crc16(tx_buf, i);

    tx_buf[i] = READ_BYTE(crc, 1);
    i++;
    tx_buf[i] = READ_BYTE(crc, 0);
    i++;

    // Magic Key Terminator.
    memcpy(&tx_buf[i], DP_KEY, 5);
    i += 5;

    MICRO_DP.stage_0x02 = DP_0x02_STAGE_WAIT_ACK;

    // Transmit the fully built frame via the hardware callback.
    return MICRO_DP.info.func_transmit(tx_buf, i);
}

/**
 * \brief   Evaluate the trigger condition based on the current variable value and edge type.
 *
 * \return  true if the trigger event has occurred, false otherwise.
 */
static inline bool_t is_trigger_occurred(void)
{
    TriggerState_DP state;

#ifndef MICRO_DP_EXPORTS
    const Value_DP_Union trigger_value = *MICRO_DP.trigger.var.ptr;
#else
    const Value_DP_Union trigger_value = { .float32 = (float)rand() / (float)RAND_MAX };
#endif

    switch (MICRO_DP.trigger.var.type)
    {
#if DP_BYTE_SIZE == 8
        case DP_TYPE_INT8:
        {
            state = (trigger_value.int8 > MICRO_DP.trigger.var.aux_value.int8) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_UINT8:
        {
            state = (trigger_value.uint8 > MICRO_DP.trigger.var.aux_value.uint8) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;
#endif

        case DP_TYPE_INT16:
        {
            state = (trigger_value.int16 > MICRO_DP.trigger.var.aux_value.int16) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_UINT16:
        {
            state = (trigger_value.uint16 > MICRO_DP.trigger.var.aux_value.uint16) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_INT32:
        {
            state = (trigger_value.int32 > MICRO_DP.trigger.var.aux_value.int32) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_FRA:
        case DP_TYPE_UINT32:
        {
            state = (trigger_value.uint32 > MICRO_DP.trigger.var.aux_value.uint32) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_INT64:
        {
            state = (trigger_value.int64 > MICRO_DP.trigger.var.aux_value.int64) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_UINT64:
        {
            state = (trigger_value.uint64 > MICRO_DP.trigger.var.aux_value.uint64) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_FLOAT32:
        {
            state = (trigger_value.float32 > MICRO_DP.trigger.var.aux_value.float32) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_FLOAT64:
        {
            state = (trigger_value.float64 > MICRO_DP.trigger.var.aux_value.float64) ? (DP_TRIGGER_MORE) : (DP_TRIGGER_LESS);
        } break;

        case DP_TYPE_IMMEDIATE:
        {
            return true;
        }

        case DP_TYPE_END:
        default:
        {
            return false;
        }
    }

    // Evaluate the trigger edge condition.
    switch (MICRO_DP.trigger.edge)
    {
        case DP_EDGE_LEADING:
        {
            if ((state == DP_TRIGGER_MORE) && (MICRO_DP.trigger.prev_state == DP_TRIGGER_LESS))
            {
                MICRO_DP.trigger.count--;
            }
        } break;

        case DP_EDGE_TRAILING:
        {
            if ((state == DP_TRIGGER_LESS) && (MICRO_DP.trigger.prev_state == DP_TRIGGER_MORE))
            {
                MICRO_DP.trigger.count--;
            }
        } break;

        case DP_EDGE_ALTER:
        {
            if (state != MICRO_DP.trigger.prev_state)
            {
                MICRO_DP.trigger.count--;
            }
        } break;

        case DP_EDGE_END:
        default:
        {
            return false;
        }
    }

    // Store the current state for the next cycle.
    MICRO_DP.trigger.prev_state = state;

    return (MICRO_DP.trigger.count == 0u);
}

/**
 * \brief   Calculate the tx buffer size required by build_0x02_ack_frame().
 *
 * Uses a stub transmit function to capture the byte count without actually
 * sending data over the physical interface. This is typically called during
 * system initialization to pre-allocate the exact amount of memory needed
 * for the tx buffer.
 *
 * \return  Byte count needed for the 0x02 acknowledgement frame.
 */
EXPORT size_t get_size_build_0x02_ack_frame(void)
{
    // Backup the real transmit callback.
    Exception_DP (* const original_func_transmit)(const uint_least8_t * const, const size_t) = MICRO_DP.info.func_transmit;

    // Replace it with a stub function.
    // The stub intercepts the transmission request and records the requested
    // frame size into MICRO_DP.mem.stub_size instead of sending it.
    MICRO_DP.info.func_transmit = micro_dp_func_transmit_stub;

    // Execute the builder to trigger the stub and capture the size.
    build_0x02_ack_frame();

    // Restore the original transmit callback.
    MICRO_DP.info.func_transmit = original_func_transmit;

    return MICRO_DP.mem.stub_size;
}

/**
 * \brief   Calculate the tx buffer size required by build_0x02_frame().
 *
 * Uses a stub transmit function to capture the byte count without actually
 * sending data over the physical interface. This is typically called during
 * system initialization to pre-allocate the exact amount of memory needed
 * for the tx buffer.
 *
 * \return  Byte count needed for the 0x02 data frame.
 */
EXPORT size_t get_0x02_frame_size(void)
{
    // Backup the real transmit callback.
    Exception_DP (* const original_func_transmit)(const uint_least8_t * const, const size_t) = MICRO_DP.info.func_transmit;

    // Backup the current global state.
    const uint_fast8_t original_var_count = MICRO_DP.var_count;
    const uint_fast16_t original_tx_samples = MICRO_DP.mem.samples_count_tx_0x02;
    const uint32_t original_samples_per_var = MICRO_DP.trigger.samples_count_per_var;
    const uint_fast8_t original_tx_count = MICRO_DP.tx_samples_count;

    for (uint_fast16_t n = 1; MICRO_DP.mem.stub_size < 450; n++)
    {
        // Setup the worst-case scenario.
        MICRO_DP.var_count = MICRO_DP.info.max_var_count;
        MICRO_DP.trigger.samples_count_per_var = 1000;
        MICRO_DP.mem.samples_count_tx_0x02 = n;
        MICRO_DP.tx_samples_count = 0u;

        for (ptrdiff_t i = 0; i < (ptrdiff_t)MICRO_DP.var_count; i++)
        {
            MICRO_DP.vars[i].type = DP_TYPE_FLOAT64;
            MICRO_DP.vars[i].address_alignment = 7;
        }

        // Replace it with a stub function.
        // The stub intercepts the transmission request and records the requested
        // frame size into MICRO_DP.mem.stub_size instead of sending it.
        MICRO_DP.info.func_transmit = micro_dp_func_transmit_stub;

        // Execute the builder to trigger the stub and capture the size.
        build_0x02_frame();

        // Restore the original transmit callback.
        MICRO_DP.info.func_transmit = original_func_transmit;

        // Restore the original global state.
        MICRO_DP.var_count = original_var_count;
        MICRO_DP.mem.samples_count_tx_0x02 = original_tx_samples;
        MICRO_DP.trigger.samples_count_per_var = original_samples_per_var;
        MICRO_DP.tx_samples_count = original_tx_count;

        for (ptrdiff_t i = 0; i < (ptrdiff_t)MICRO_DP.var_count; i++)
        {
            MICRO_DP.vars[i].type = DP_TYPE_INT8;
            MICRO_DP.vars[i].address_alignment = 0;
        }
    }

    return MICRO_DP.mem.stub_size;
}
