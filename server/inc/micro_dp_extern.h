#ifndef MICRO_DP_EXTERN_H
#define MICRO_DP_EXTERN_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

typedef enum
{
    DP_OK = 0,
    DP_ERROR,

    DP_EXCEPTION_END,

} Exception_DP;

typedef struct
{
    // Function to get system clock counter.
    size_t (*get_sys_clk_counter)(void);

    // System clock frequency.
    uint32_t sys_clk_freq;

    // Sampling frequency (frequency of 'micro_dp_context()' call).
    uint32_t sampling_freq;

    // Function to transmit a frame.
    Exception_DP (*func_transmit)(const uint_least8_t * const, const size_t);

    // [optional] Functions to disable/enable interrupts
    // or warranty of non-interruptions.
    bool uninterrupted;
    void (*disable_interrupts)(void);
    void (*enable_interrupts)(void);

    // Limitation of allocated memory, [bytes].
    size_t memory_limit;

    // [optional] Range of valid addresses in memory to read variables.
    uintptr_t valid_min_addr;  // Default value = 0.
    uintptr_t valid_max_addr;  // Default value = UINTPTR_MAX.

    // [optional] Max number of variables to read.
    uint_fast32_t max_var_count;  // Default value: 4.

    // [optional] Pointer to a user-defined static buffer for memory allocation.
    void *static_buffer;  // Default value: NULL (HEAP is used).

    // [optional] The node's address.
    uint_least8_t node_addr;  // Default value: 0.

} Info_DP_Struct;

Exception_DP micro_dp_init(Info_DP_Struct *);
float micro_dp_context(void);
Exception_DP micro_dp_background(void);
void micro_dp_handle_rx_chunk(const uint_least8_t * const, const size_t);

#endif  // MICRO_DP_EXTERN_H
