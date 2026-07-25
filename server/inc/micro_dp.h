/**
 * \file    micro_dp.h
 * \brief   Core data structures, enumerations, and macro definitions for the MicroDP.
 *
 * This header defines state machine structures and utility macros used across
 * all MicroDP protocol modules. It serves as the central configuration hub
 * for the library.
 */

#ifndef MICRO_DP_H
#define MICRO_DP_H

#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#include "micro_dp_extern.h"

#define DP_VERSION_MAJOR ((uint16_t)0)
#define DP_VERSION_MINOR ((uint16_t)1)
#define DP_VERSION_PATCH ((uint16_t)3)

// Export defines for DLLs.
#ifdef MICRO_DP_EXPORTS
    #ifdef _WIN32
    #define EXPORT __declspec(dllexport)
    #else
    #define EXPORT __attribute__((visibility("default")))
    #endif
#else
    #define EXPORT
#endif

// Magic key for frame termination.
#define DP_KEY "vicet"

// Architecture bit width detection.
#if UINT_FAST8_MAX == UINTMAX_C(0xFF)
    #define DP_ARCH_BIT_WIDTH (8)
#elif UINT_FAST8_MAX == UINTMAX_C(0xFFFF)
    #define DP_ARCH_BIT_WIDTH (16)
#elif UINT_FAST8_MAX == UINTMAX_C(0xFFFFFFFF)
    #define DP_ARCH_BIT_WIDTH (32)
#elif UINT_FAST8_MAX == UINTMAX_C(0xFFFFFFFFFFFFFFFF)
    #define DP_ARCH_BIT_WIDTH (64)
#endif

// Byte size detection.
#define DP_BYTE_SIZE CHAR_BIT

// Byte serialization macros (Little-Endian).
#define BYTES_TO_UINT64(b1, b2, b3, b4, b5, b6, b7, b8)                                                                                          \
    (uint64_t)((uint64_t)((uint64_t)(b1) & (uint64_t)0x000000FFu) | (uint64_t)((uint64_t)((uint64_t)(b2) << 8u) & (uint64_t)0x000000000000FF00u) \
               | (uint64_t)((uint64_t)((uint64_t)(b3) << 16u) & (uint64_t)0x0000000000FF0000u)                                                   \
               | (uint64_t)((uint64_t)((uint64_t)(b4) << 24u) & (uint64_t)0x00000000FF000000u)                                                   \
               | (uint64_t)((uint64_t)((uint64_t)(b5) << 32u) & (uint64_t)0x000000FF00000000u)                                                   \
               | (uint64_t)((uint64_t)((uint64_t)(b6) << 40u) & (uint64_t)0x0000FF0000000000u)                                                   \
               | (uint64_t)((uint64_t)((uint64_t)(b7) << 48u) & (uint64_t)0x00FF000000000000u)                                                   \
               | (uint64_t)((uint64_t)((uint64_t)(b8) << 56u) & (uint64_t)0xFF00000000000000u))

#define BYTES_TO_UINT32(b1, b2, b3, b4)                                                                                                  \
    (uint32_t)((uint32_t)((uint32_t)(b1) & (uint32_t)0x000000FFu) | (uint32_t)((uint32_t)((uint32_t)(b2) << 8u) & (uint32_t)0x0000FF00u) \
               | (uint32_t)((uint32_t)((uint32_t)(b3) << 16u) & (uint32_t)0x00FF0000u)                                                   \
               | (uint32_t)((uint32_t)((uint32_t)(b4) << 24u) & (uint32_t)0xFF000000u))

#define BYTES_TO_UINT16(b1, b2)                                                                                                  \
    (uint16_t)((uint16_t)((uint16_t)(b1) & (uint16_t)0x00FFu) | (uint16_t)((uint16_t)((uint16_t)(b2) << 8) & (uint16_t)0xFF00u))

#define READ_BYTE(v, index)                                                                                                      \
    (uint_least8_t)((uint_fast32_t)((uint_fast32_t)(v) >> (uint_fast32_t)((uint_fast32_t)(index) << 3u)) & (uint_fast32_t)0xFFu)

// Inter-module signal routing macros.
#define REGISTER_BUILD_FUNCTION(func)           \
    do                                          \
    {                                           \
        if (SIGNALS_DP.build_function == NULL)  \
        {                                       \
            SIGNALS_DP.build_function = (func); \
        }                                       \
    } while (0)

#define REGISTER_PROCESS_FUNCTION(func)           \
    do                                            \
    {                                             \
        if (SIGNALS_DP.process_function == NULL)  \
        {                                         \
            SIGNALS_DP.process_function = (func); \
        }                                         \
    } while (0)

#define UNREGISTER_BUILD_FUNCTION()    do { SIGNALS_DP.build_function = NULL; } while (0)
#define UNREGISTER_PROCESS_FUNCTION()  do { SIGNALS_DP.process_function = NULL; } while (0)

// Utility macros.
#define DP_MAX(a, b) (((a) > (b)) ? (a) : (b))
#define DP_MIN(a, b) (((a) < (b)) ? (a) : (b))
#define DP_CLAMP(x, min, max) (((x) < (min)) ? (min) : (((x) > (max)) ? (max) : (x)))

#define SAFE_CALL(func, ...)       \
        do                         \
        {                          \
            if (func)              \
            {                      \
                func(__VA_ARGS__); \
            }                      \
        } while (0)

// Custom typedefs.
typedef _Bool  bool_t;
typedef float  float32_t;
typedef double float64_t;

typedef enum
{
    DP_MODE_IDLE     = 0,
    DP_MODE_0x00     = 100,
    DP_MODE_0x01     = 101, // Real-Time Mode
    DP_MODE_0x02     = 102, // Triggered Mode.
    DP_MODE_0x02_ACK = 103, // Triggered Mode (acknowledgement).
    DP_MODE_0x03     = 104, // Writing value to the variable.
    DP_MODE_0x04     = 105, // Start FRA excitation.

    DP_MODE_END = 107,

} Modes_DP;

typedef enum
{
    DP_TYPE_INT8 = 0,
    DP_TYPE_UINT8,
    DP_TYPE_INT16,
    DP_TYPE_UINT16,
    DP_TYPE_INT32,
    DP_TYPE_UINT32,
    DP_TYPE_INT64,
    DP_TYPE_UINT64,
    DP_TYPE_FLOAT32,
    DP_TYPE_FLOAT64,

    // Special types for triggering.
    DP_TYPE_FRA,
    DP_TYPE_IMMEDIATE,

    DP_TYPE_END,

} Types_DP;

typedef enum
{
    DP_EDGE_LEADING = 0,
    DP_EDGE_TRAILING,
    DP_EDGE_ALTER,

    DP_EDGE_END

} Edge_DP;

typedef enum
{
    DP_TRIGGER_NONE = 0,
    DP_TRIGGER_MORE,
    DP_TRIGGER_LESS

} TriggerState_DP;

typedef enum
{
    DP_0x02_STAGE_IDLE = 0,
    DP_0x02_STAGE_ACK,
    DP_0x02_STAGE_PRE_PROCESS,
    DP_0x02_STAGE_PRE_COLLECT,
    DP_0x02_STAGE_POST_COLLECT,
    DP_0x02_STAGE_TX,
    DP_0x02_STAGE_WAIT_ACK

} Stage_0x02_DP;

typedef enum
{
    DP_0x02_TX_CMD_CONTINUE = 1,
    DP_0x02_TX_CMD_RESTART,
    DP_0x02_TX_CMD_START,

} Transmit_0x02_CMD_DP;

typedef enum
{
    DP_0x02_TX_CHUNK_INTERMEDIATE = 0,
    DP_0x02_TX_CHUNK_FINAL

} Transmit_0x02_Chunk_DP;

typedef union
{
#if DP_BYTE_SIZE == 8
    int8_t  int8;
    uint8_t uint8;
#endif
    int16_t   int16;
    uint16_t  uint16;
    int32_t   int32;
    uint32_t  uint32;
    int64_t   int64;
    uint64_t  uint64;
    float32_t float32;
    float64_t float64;

#if DP_BYTE_SIZE == 8
    uint8_t uint8_array[8];
#endif
    uint16_t uint16_array[4];
    uint32_t uint32_array[2];

} Value_DP_Union;

typedef struct
{
    // Auxiliary value (e.g. trigger threshold).
    Value_DP_Union aux_value;

    // Pointer to the variable.
    Value_DP_Union * ptr;

    // Variable data type.
    Types_DP type;

    // Alignment remainder for non-aligned addresses.
    int_fast8_t address_alignment;

} Var_DP_Struct;

typedef struct
{
    // Trigger variable configuration.
    Var_DP_Struct var;

    // Pointer to the current sample in the circular buffer.
    Value_DP_Union * current_pointer;

    // Pointer to the trigger event sample.
    Value_DP_Union * fill_pointer;

    // Pointer to the end of the circular buffer.
    Value_DP_Union * end_pointer;

    // Trigger event count.
    uint_fast8_t count;

    // Pre-trigger sample count.
    uint_fast16_t pre_trigger;

    // Post-trigger sample count.
    uint_fast16_t post_trigger;

    // Current post-trigger sample counter.
    uint_fast16_t post_trigger_count;

    // Settling time before acquisition.
    uint_fast32_t settling_time;

    // Current settling time counter.
    uint_fast32_t settling_time_count;

    // Trigger edge type.
    Edge_DP edge;

    // Previous trigger state for edge detection.
    TriggerState_DP prev_state;

    // Total samples per variable for Triggered Mode.
    size_t samples_count_per_var;

    // Flag indicating the end of the TX stage.
    bool_t end;

    // Total capacity of the sample buffer.
    uint32_t samples_count;

} Trigger_DP_Struct;

typedef struct
{
    bool_t    enable;
    uint32_t  n;
    uint32_t  n_period;
    float32_t value;

} Excitation_DP_Struct;

typedef struct
{
    // User-defined hardware configuration.
    Info_DP_Struct info;

    // Current node operating mode.
    Modes_DP mode;

    /// Current stage of the 0x02 state machine.
    Stage_0x02_DP stage_0x02;

    struct
    {
        // Samples per transmission chunk in Triggered Mode.
        uint_fast16_t samples_count_tx_0x02;

        // Circular buffer for acquired samples.
        Value_DP_Union * var_samples;

        // Transmit buffer.
        uint_least8_t * tx_buf;

        // Receive buffer.
        uint_least8_t * rx_buf;

        // Size of the receive buffer.
        size_t          rx_buf_size;

        // Current write index in the receive buffer.
        size_t          rx_buf_ptr;

        // DP_KEY parsing sequence index
        ptrdiff_t       sequence;

        // Memory initialization flag.
        bool_t initialized;

        // End offset of the custom memory allocator.
        size_t alloc_end;

        // Maximum transmit buffer size.
        size_t max_size_tx;

        // Required address alignment in bytes.
        uintptr_t address_alignment;

        // Frame size captured by the transmit stub.
        size_t stub_size;

    } mem;

    // Array of configured variables.
    Var_DP_Struct * vars;

    // Number of samples transmitted so far.
    size_t tx_samples_count;

    // Trigger configuration and state.
    Trigger_DP_Struct trigger;

    // Excitation signal state.
    Excitation_DP_Struct excitation;

    // Number of configured variables.
    uint_fast8_t var_count;

    // Decimation factor (sample rate division).
    uint_fast8_t sample_count;

    // Current decimation counter.
    uint_fast8_t sample_count_count;

} Micro_DP_Struct;

typedef struct
{
    // Function for building and transmitting frames.
    Exception_DP (*build_function)(void);

    // Function for processing frames.
    Exception_DP (*process_function)(const uint_least8_t * const);

} Signals_DP_Struct;

// External global variables and functions.
extern const size_t TYPE_BYTESIZE[DP_TYPE_END];

extern Micro_DP_Struct   MICRO_DP;
extern Micro_DP_Struct   NULL_MICRO_DP;
extern Signals_DP_Struct SIGNALS_DP;

Exception_DP process_0x00_frame(const uint_least8_t * const);
Exception_DP process_0x01_frame(const uint_least8_t * const);
Exception_DP process_0x02_frame(const uint_least8_t * const);
Exception_DP process_0x03_frame(const uint_least8_t * const);
Exception_DP process_0x04_frame(const uint_least8_t * const);

size_t get_0x00_frame_size(void);
size_t get_0x01_frame_size(void);
size_t get_size_build_0x02_ack_frame(void);
size_t get_0x02_frame_size(void);
size_t get_size_build_0x03_ack_frame(void);
size_t get_size_build_0x04_ack_frame(void);

Exception_DP process_0x02_ack_frame(const uint_least8_t * const);

float32_t collect_0x02_vars(void);

void micro_dp_reset(void);
void micro_dp_excitation(void);

int_fast8_t are_type_and_address_valid(const uintptr_t, const Types_DP);

void read_variable(Value_DP_Union * const, const size_t);

Exception_DP micro_dp_func_transmit_stub(const uint_least8_t * const, const size_t);

#endif  // MICRO_DP_H
