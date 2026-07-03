<h1 align="center"><img src="misc/logo_small_circle.svg" alt="Digital Points"><br>Digital Points</h1>

<h3 align="center">[<a
href="#about">About</a>] [<a
href="#features">Features</a>] [<a
href="#quickstart">Quickstart</a>] [<a
href="#build-from-source">Build from source</a>]</h3>

![Digital Points main window](misc/main.png)

## About

Digital Points is an open-source real-time debugging tool for embedded systems. It functions as a software oscilloscope and enables developers to read and visualize microcontroller variables via standard communication interfaces (serial, CAN), perform FFT/DSP operations, measure frequency responses (Bode plots), and design digital PID controllers.

Supported MCU architectures:
- ARM Cortex-M4/M7 (gcc, clang)
- TI C2000 (cl2000)
- RISC-V RV32I (gcc)

### Features

- **Real-Time Mode**: Reads the selected variables at the maximum available rate.

![Real-Time Mode demo](misc/rtm_demo.gif)

- **Triggered Mode**: Captures variables within a time window at a specified sampling frequency.

![Triggered Mode demo](misc/tm_demo.gif)

- **Frequency Response Analysis (FRA) Mode**: Measures frequency responses of a real-time control system using single-tone excitation with stepped frequency sweep or multi-tone excitation.

![FRA Mode demo](misc/fra_demo.gif)

- **Digital PID Controller Design**: Calculates digital PID controller coefficients based on frequency responses.

![PID controller design demo](misc/pid_demo.gif)

## Quickstart

1. Install `Digital Points`.

2. Add the `microdp` library to your embedded project:

    2.1 Add `libmicrodp` folder to *include paths* of the project.

    2.2 Add the appropriate static library from the folder to the project's build.

3. Implement a transmit function for your communication interface using the following prototype. It must return `DP_OK` on success:

```C
Exception_DP func_transmit(const uint_least8_t * const frame, const size_t byte_size);
```

4. Initialize the library anywhere in your code:

```C
#include "micro_dp_extern.h"

// Declare a static buffer to limit memory consumption.
static uint_least8_t DP_HEAP[10000];

// Implement a function to get the system core clock counter.
static size_t get_sys_clk_counter(void)
{
    // This is an example for ARM Cortex-M.
    return (size_t)DWT->CYCCNT;
}

// Declare the config structure.
static const Info_DP_Struct INFO =
{
    .sys_clk_freq    = 200000000,               // System core clock frequency, [Hz].
    .sampling_freq   = 100000,                  // Sampling frequency, [Hz].
    .func_transmit   = func_transmit,           // Function pointer to transmit frames.
    .static_buffer   = DP_HEAP,                 // Pointer to the buffer for memory allocation.
    .memory_limit    = sizeof(DP_HEAP),         // Available memory size, [byte].
    .get_sys_clk_counter = get_sys_clk_counter  // Function pointer to get the current system core clock counter.
};

...

int main(void)
{
    // Initialize the 'micro_dp' library.
    micro_dp_init(&INFO);
    ...
}
```

5. Call background and context functions:

```C
int main(void)
{
    while (1)
    {
        // Call this function within your main loop
        // or any non-time-critical task.
        micro_dp_background();
    }
}

void timer_irq_handler(void)
{
    // Call this function periodically at the sampling frequency.
    micro_dp_context();
}
```

6. Call the receive function to pass a chunk of data (or all the data) to the library:

```C
void interface_irq_handler(void)
{
    // Example 1: Byte-by-byte reception
    uint_least8_t data = get_interface_data();

    // Pass a single byte to the library.
    micro_dp_handle_rx_chunk(&data, 1);

    /*
    // Example 2: Buffer reception.
    uint_least8_t data[10];
    
    for (size_t i = 0; i < sizeof(data); i++)
    {
        data[i] = get_interface_data();
    }

    // Pass the entire buffer (or a part of it) to the library.
    micro_dp_handle_rx_chunk(data, sizeof(data));
    */
}
```

7. Build the project, flash the MCU, and launch the Digital Points application.

8. Load an ELF file (*.axf, *.elf, *.out, *.prx, *.puff, *.so) with DWARF debug information from your project into `Digital Points` and configure the communication interface on the `Settings` page.

> **Note**: Enable maximum DWARF debug information in your compiler (e.g. `-g3` for GCC/clang).

9. Check the connection status `Linked/Unlinked` in the bottom-left corner of the window.

## Build from source

Clone the repository:

```bash
git clone https://github.com/jankinjack/digital_points.git
cd digital-points
```

### Build Client

1. Install Python 3.11 or later.

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

1. Install [MSVC](https://visualstudio.microsoft.com/ru/vs/features/cplusplus/).

2. Run the build script:

```bash
python build_client.py
```

### Build Server

1. Install compilers and add them to PATH:

    - [GCC](https://gcc.gnu.org/) / [MSYS2 GCC](https://packages.msys2.org/packages/gcc)
    - [Clang](https://clang.llvm.org/) / [MSYS2 LLVM](https://packages.msys2.org/packages/llvm)
    - [C2000-CGT](https://www.ti.com/tool/C2000-CGT)

2. Install [Meson Build](https://mesonbuild.com/) and add it to PATH.

3. Run the build script:

```bash
python build_server.py
```
