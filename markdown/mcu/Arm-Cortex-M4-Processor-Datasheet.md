# Arm-Cortex-M4-Processor-Datasheet

*Source: `original/mcu/Arm-Cortex-M4-Processor-Datasheet.pdf` (10 pages)*

<!-- page 1 -->

# **Arm Cortex-M4 Datasheet** 



<!-- Start of picture text -->
Datasheet<br><!-- End of picture text -->



Figure 1: Block diagram of the Cortex-M4 processor 

## Overview 

The Cortex-M4 processor is developed to address digital signal control markets that demand an efficient, easy-to-use blend of control and signal processing capabilities. The combination of high-efficiency signal processing functionality with the low-power, low-cost and ease-ofuse benefits of the Cortex-M family of processors satisfies many markets. These industries include motor control, automotive, power management, embedded audio and industrial automation markets. 

## Features 

|**Feature**|**Description**|
|---|---|
|Architecture|Armv7E-M|
|Bus Interface|3x AMBA AHB-Lite interface (Harvard bus architecture)<br>AMBA ATB interface for CoreSight debug components|
|ISA Support|Thumb/Thumb-2|
|Pipeline|3-stage + branch speculation|
|DSP Extension|Single-cycle 16/32-bit MAC<br>Single-cycle dual 16-bit MAC<br>8/16-bit SIMD arithmetic<br>Hardware Divide (2-12 cycles)|
|Floating-Point Unit|Optional single precision floating point unit (FPU)<br>IEEE 754 compliant|
|Memory Protection|Optional 8-region MPU with sub regions<br>and background region|
|Bit Manipulation|Integrated Bit Field Processing Instructions<br>& Bus Level Bit Banding|
|Interrupts|Non-maskable interrupt (NMI) + 1 to 240 physical interrupts|
|Interrupt Priority Levels|8 to 256 priority levels|
|Wake-up Interrupt<br>Controller|Optional|
|Sleep Modes|Integrated WFI and WFE Instructions and Sleep On Exit capability<br>Sleep & Deep Sleep Signals<br>Optional Retention Mode with Arm Power Management Kit|
|Debug|Optional JTAG andSerial Wire Debug ports<br>Up to 8 Breakpoints and 4 Watchpoints|
|Trace|Optional Instruction Trace (ETM), Data Trace (DWT),<br>and Instrumentation Trace (ITM)|



1 



<!-- page 2 -->

## About the Processor 

The Cortex-M4 processor is a low-power processor that features low gate count, low interrupt latency, and low-cost debug. The Cortex-M4 with FPU is a processor with the same capability as the Cortex-M4 processor and includes floating-point arithmetic functionality. Both processors are intended for deeply embedded applications that require fast interrupt response features. 

The Cortex-M4 processor includes: 

- A processor core 

- A Nested Vectored Interrupt Controller (NVIC) closely integrated with the processor 

- core to achieve low latency interrupt processing 

Multiple high-performance bus interfaces 

A low-cost debug solution with the optional ability to: 

- Implement breakpoints and code patches 

- Implement watchpoints, tracing, and system profiling 

- Support printf style debugging 

- Bridge to a Trace Port Analyzer (TPA) 

An optional Memory Protection Unit (MPU) 

- A Floating Point Unit (FPU) in the Cortex-M4 with FPU processor 

## Block Diagram 



Figure 2: Cortex-M4 processor components 

2 



<!-- page 3 -->

## Cortex-M4 Components 

### **Processor** 

The Cortex-M4 processor features a low gate count processor core, with low latency interrupt processing that has: 

- A subset of the Thumb instruction set, defined in the Armv7-M architecture 

- Banked Stack Pointer (SP) 

- Hardware divide instructions, SDIV and UDIV 

- Handler and Thread modes 

- Thumb and Debug states 

- Support for interruptible-continued instructions LDM, STM, PUSH, and POP for low interrupt latency 

- Automatic processor state saving and restoration for low latency Interrupt Service Routine (ISR) entry and exit 

- Support for Armv6 big-endian byte-invariant or little-endian accesses 

- Support for Armv6 unaligned accesses 

**Floating Point Unit (FPU) in the Cortex-M4 with FPU processor providing:** 

- 32-bit instructions for single-precision (C float) data-processing operations 

- Combined Multiply and Accumulate instructions for increased precision (Fused MAC) 

- Hardware support for conversion, addition, subtraction, multiplication with optional accumulate, division, and square root 

- Hardware support for denormals and all IEEE rounding modes 

- 32 dedicated 32-bit single precision registers, also addressable as 16 

- double-word registers 

- Decoupled three-stage pipeline 

### **Nested Vectored Interrupt Controller** 

Nested Vectored Interrupt Controller (NVIC) closely integrated with the processor core to achieve low latency interrupt processing. Features include: 

- External interrupts, configurable from 1 to 240 

- Bits of priority, configurable from 3 to 8 

- Dynamic reprioritization of interrupts 

- Priority grouping 

   - This enables selection of preempting interrupt levels and non preempting interrupt levels. 

Support for tail-chaining and late arrival of interrupts 

- This enables back-to-back interrupt processing without the overhead of state saving and restoration between interrupts. 

3 



<!-- page 4 -->

- Processor state automatically saved on interrupt entry, and restored on interrupt exit, with no instruction overhead 

- Optional Wake-up Interrupt Controller (WIC), providing ultra-low power sleep mode support 

## **Memory Protection Unit (MPU)** 

An optional MPU for memory protection, including: 

- Eight memory regions 

- Sub Region Disable (SRD), enabling efficient use of memory regions 

- The ability to enable a background region that implements the default memory map attributes 

## **Cross Trigger Interface Unit** 

The optional CTI enables the debug logic and the Embedded Trace Macrocell (ETM) to interact with each other and with other CoreSight components. 

## **Debug and Trace** 

Low-cost debug solution that features: 

- Debug access to all memory and registers in the system, including access to memory mapped devices, access to internal core registers when the core is halted, and access to debug control registers even while SYSRESETn is asserted 

- Serial Wire Debug Port (SW-DP) or Serial Wire JTAG Debug Port (SWJ-DP) debug access, or both 

- Optional Flash Patch and Breakpoint (FPB) unit for implementing breakpoints and code patches 

- Optional Data Watchpoint and Trace (DWT) unit for implementing watchpoints, data tracing, and system profiling 

- Optional Instrumentation Trace Macrocell (ITM) for support of printf style debugging 

- Optional Trace Port Interface Unit (TPIU) for bridging to a Trace Port Analyzer (TPA), including Single Wire Output (SWO) mode 

- Optional ETM for instruction trace 

## **ETM interface** 

The ETM interface enables simple connection of an ETM to the processor. It provides a channel for instruction trace to the ETM. 

## **AHB Trace Macrocell interface** 

The AHB Trace Macrocell (HTM) interface enables a simple connection of the AHB trace macrocell to the processor. It provides a channel for the data trace to the HTM. 

Your implementation must include this interface to use the HTM interface. You must set TRCENA to 1 in the Debug Exception and Monitor Control Register (DEMCR) before you enable the HTM to enable the HTM port to supply trace data. 

4 



<!-- page 5 -->

## **Bus interfaces** 

Three Advanced High-performance Bus-Lite (AHB-Lite) interfaces: ICode, DCode, 

- and System bus interfaces 

Private Peripheral Bus (PPB) based on Advanced Peripheral Bus (APB) interface 

Bit-band support that includes atomic bit-band write and read operations 

- Memory access alignment 

- Write buffer for buffering of write data 

Exclusive access transfers for multiprocessor systems 

## **Debug port AHB-AP interface** 

The processor contains an Advanced High-performance Bus Access Port (AHB-AP) interface for debug accesses. An external Debug Port (DP) component accesses this interface. The Cortex-M4 system supports three possible DP implementations: 

Serial Wire JTAG Debug Port (SWJ-DP) 

   - The SWJ-DP is a standard CoreSight debug port that combines JTAG-DP and Serial Wire Debug Port (SW-DP). 

- SW-DP 

   - This provides a two-pin interface to the AHB-AP port. 

- No DP present 

   - If no debug functionality is present within the processor, a DP is not required. 

The two DP implementations provide different mechanisms for debug access to the processor. Your implementation must contain only one of these components. 

# Cortex-M4 Pipeline 

Figure 3: Cortex-M4 processor pipeline 



5 



<!-- page 6 -->

# Processor Configuration Options 

The Cortex-M4 processor has configurable options that you can set during the implementation and integration stages to match your functional requirements. 

|**Feature**|**Options**|
|---|---|
|Number of interrupts|Specifies number of interrupts (1-240 interrupts)|
|Levels of interrupt priority|Between 3 and 8 bits of interrupt priority, between 8 and 256 levels<br>of priority|
||No MPU|
|MPU present|MPU present|
|FPU t|No FPU|
|presen|FPU present|
|Bit Banding|Specifies whether bit-banding is present|
|AHB Control|Specifies whether AB-Lite buses maintain control information during<br>wait stated transfers|
|Debug Level|Specifies the level of debug support (0 to 3)|
|Trace Level|Specifies the level of trace support (0 to 3)|
|Reset all registers|Specifies whether all synchronous state or only architecturally<br>required state is reset|
|JTAG present|Enables or disables the JTAG portion of the debug port|
|Clock Gate Present|Specifies whether architectural clock gates are included|
|Observation|Enables observation of internal state of the processor|
|WIC present|Specifies whether a WIC is present|
|WIC Lines|Number of WIC lines (minimum 2)|



6 



<!-- page 7 -->

# Instruction Set 



<!-- Start of picture text -->
Armv7-M<br>Armv6-M<br><!-- End of picture text -->





<!-- Start of picture text -->
Cortex-M0/M0+<br>Cortex-M3<br>Cortex-M4<br>Cortex-M7<br><!-- End of picture text -->

Figure 5: Instruction set 

7 



<!-- page 8 -->

# Power, Performance and Area 

|DMIPS|CoreMark/MHz|
|---|---|
|1.25|3.42|



|Configuration|90LP<br>(7-track, R<br>1.2V, 25°C|Vt, typical<br>)|65LP<br>(8 Track , R<br>1.2V, 25°C|Vt, typical<br>)|40LP<br>(9 Track, RVt,<br>1.1v, 25°C)|typical|28HPM<br>(9-track,<br>0.9v, 85°|HVt, typical<br>C)|
|---|---|---|---|---|---|---|---|---|
||Area<br>mm<sup>2</sup>|Power<br>µW/MHz|Area<br>mm<sup>2</sup>|Power<br>µW/MHz|Area<br>mm<sup>2</sup>|Power<br>µW/MHz|Area<br>mm<sup>2</sup>|Power<br>µW/MHz|
|Minimum<br>Configuration*|0.119|32.82|0.076|26.40|0.028|12.26|0.020|8.47|
|Feature Rich**|0.304|41.47|0.201|35.54|0.082|15.48|0.053|11.20|



|Max Freq|40LP|28HPM|
|---|---|---|
||(9-track RVt, typical 1.1v, 25C)|(12track , LVt, typical 0.9v, 85°C)|
|Feature Rich Configuration**|223MHz|822MHz|



* MPU_PRESENT 0; NUM_IRQ 1; LVL_WIDTH 3; TRACE_LVL 0; DEBUG_LVL 0; JTAG_ PRESENT 0; CLKGATE_PRESENT 1; RESET_ALL_REGS 0; WIC_PRESENT 0; WIC_LINES 3; BB_PRESENT 0; CONST_AHB_CTRL 0; FPU_PRESENT 0; 

** MPU_PRESENT 1; NUM_IRQ 64; LVL_WIDTH 3; TRACE_LVL 2; DEBUG_LVL 3; JTAG_ PRESENT 0; CLKGATE_PRESENT 1; RESET_ALL_REGS 0; WIC_PRESENT 1; WIC_LINES 67; BB_PRESENT 0; CONST_AHB_CTRL 0; FPU_PRESENT 1; 

8 



<!-- page 9 -->

# Additional Technical documents 

**1.** Cortex-M4 Technical Reference Manual  - TRM 

**2.** Cortex-M4 Integration and Implementation Manual – available as part of the Bill of Materials 

**3.** Armv7-M Architecture Reference Manual  - ARM 

**4.** CoreSight ETM-M4 Technical Reference Manual - ETM 

# Glossary of Terms 

|AHB|Advanced High-performance Bus|
|---|---|
|ATB|Advanced Trace Bus|
|C-AHB|Code AHB|
|CTI|Cross Trigger Interface|
|D-AHB|Debug AHB|
|DSP|Digital Signal Processing|
|DWT|Data Watchpoint and Trace|
|ETM|Embedded Trace Macrocell|
|FPU|Floating Point Unit|
|IEEE|Institute of Electrical and Electronics Engineers|
|ISR|Interrupt Service Routine|
|ITM|Instrumentation Trace Macrocell|
|JTAG|Joint Test Action Group|
|MAC|Multiply and Accumulate|
|MPU|Memory Protection Unit|
|NMI|Non-maskable Interrupt|
|NVIC|Nested Vectored Interrupt Controller|
|PPB|Private Peripheral Bus|
|S-AHB|System AHB|
|SIMD|Single Instruction, Multiple Data|
|SWO|Serial Wire Output|
|TPA|Trace Port Analyzer|
|TPIU|Trace Port Interface Unit|
|WFE|Wait for event|
|WFI|Wait for interrupt|
|WIC|Wake-up Interrupt Controller|



9 



<!-- page 10 -->

# Contact details 

**UK Europe Japan** Salesinfo-eu@Arm.com Salesinfo-eu@Arm.com Salesinfo-eu@Arm.com 

**USA Asia Pacific Korea** Salesinfo-us@Arm.com Salesinfo-us@Arm.com Salesinfo-us@Arm.com 

**China** Salesinfo-eu@Arm.com 

**Taiwan** 

Salesinfo-eu@Arm.com 

**Israel India** Salesinfo-us@Arm.com Salesinfo-us@Arm.com 

All brand names or product names are the property of their respective holders. Neither the whole nor any part of the information contained in, or the product described in, this document may be adapted or reproduced in any material form except with the prior written permission of the copyright holder. The product described in this document is subject to continuous developments and improvements. All particulars of the product and its use contained in this document are given in good faith. All warranties implied or expressed, including but not limited to implied warranties of satisfactory quality or fitness for purpose are excluded. This document is intended only to provide information to the reader about the product. To the extent permitted by local laws Arm shall not be liable for any loss or damage arising from the use of any information in this document or any error or omission in such information. 

© Arm Ltd. 2020 

10 

