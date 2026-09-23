# 10. Processor and Architecture

*Source: `Atmel-SAMD51.pdf`, pages 61-80 — SAMD51 family datasheet*

                                                            SAM D5x/E5x Family Data Sheet
                                                                                  Processor and Architecture


10.      Processor and Architecture

10.1     Cortex M4 Processor
                              ™
         The ARM®Cortex -M4 processor is a high performance 32-bit processor designed for the microcontroller
         market. It offers the following significant benefits to developers:
           • Outstanding processing performance combined with fast interrupt handling
           •   Enhanced system debug with extensive breakpoint and trace capabilities
           •   Efficient processor core, system and memories
           •   Ultra low-power consumption with integrated sleep modes
           •   Platform security robustness, with integrated memory protection unit (MPU).
         The implemented ARM Cortex-M4 is revision r0p1
         For additional information, refer to http://www.arm.com
         The Cortex-M4 processor is built on a high-performance processor core with a 3-stage pipeline Harvard
         architecture, making it ideal for demanding embedded applications. The processor delivers exceptional
         power efficiency through an efficient instruction set and extensively optimized design, providing high-end
         processing hardware including IEEE 754-compliant single-precision floating-point computation, a range of
         single-cycle and SIMD multiplication and multiply-with-accumulate capabilities, saturating arithmetic and
         dedicated hardware division.
         To facilitate the design of cost-sensitive devices, the Cortex-M4 processor implements tightly-coupled
         system components that reduce processor area while significantly improving interrupt handling and
         system debug capabilities. The Cortex-M4 processor implements a version of the Thumb instruction set
         based on Thumb®-2 technology, ensuring high code density and reduced program memory requirements.
         The Cortex-M4 instruction set provides the exceptional performance expected of a modern 32-bit
         architecture, with the high code density of 8-bit and 16-bit microcontrollers.
         The Cortex-M4 processor closely integrates a configurable NVIC, to deliver industry-leading interrupt
         performance. The NVIC includes a Non-Maskable interrupt (NMI), and provides up to 8 interrupt priority
         levels. The tight integration of the processor core and NVIC provides fast execution of Interrupt Service
         Routines (ISRs), dramatically reducing the interrupt latency. This is achieved through the hardware
         stacking of registers, and the ability to suspend load-multiple and store-multiple operations. Interrupt
         handlers do not require wrapping in assembler code, removing any code overhead from the ISRs. A tail-
         chain optimization also significantly reduces the overhead when switching from one ISR to another.
         To optimize low-power designs, the NVIC integrates with the sleep modes, that include a deep sleep
         function that enables the entire device to be rapidly powered down while still retaining program state.

10.1.1   System Level Interface
         The Cortex-M4 processor provides multiple interfaces using AMBA technology to provide high-speed,
         low-latency memory accesses. It supports unaligned data accesses and implements atomic bit
         manipulation that enables faster peripheral controls, system spinlocks and thread-safe Boolean data
         handling.
         The Cortex-M4 processor has a memory protection unit (MPU) that provides fine grain memory control,
         enabling applications to utilize multiple privilege levels, separating and protecting code, data and stack on
         a task-by-task basis. Such requirements are becoming critical in many embedded applications such as
         automotive.




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 61
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                Processor and Architecture

10.1.2   Integrated Configurable Debug
         The Cortex-M4 processor implements a complete hardware debug solution. This provides high system
         visibility of the processor and memory through a 2-pin Serial Wire Debug (SWD) port that is ideal for
         microcontrollers and other small package devices.
         For system trace the processor integrates an Instrumentation Trace Macrocell (ITM) alongside data
         watchpoints and a profiling unit. The Embedded Trace Macrocell (ETM) delivers unrivaled instruction
         trace capture in an area far smaller than traditional trace units, enabling many low cost MCUs to
         implement full instruction trace for the first time.
         To enable simple and cost-effective profiling of the system events these generate, a stream of software-
         generated messages, data trace, and profiling information is exported over three different ways:
           • Output off chip using the TPIU, through a single pin, called Serial Wire Viewer (SWV). Limited to ITM
             system trace
           • Output off chip using the TPIU, through a 4-bit pin interface. Bandwidth is limited
           • Internally stored in RAM, using the CoreSight ETB. Bandwidth is then optimal but capacity is limited
         The Flash Patch and Breakpoint Unit (FPB) provides up to 8 hardware breakpoint comparators that
         debuggers can use. The comparators in the FPB also provide remap functions of up to 8 words in the
         program code in the CODE memory region. This enables applications stored on a non-erasable, ROM-
         based microcontroller to be patched if a small programmable memory, for example flash, is available in
         the device. During initialization, the application in ROM detects, from the programmable memory, whether
         a patch is required. If a patch is required, the application programs the FPB to remap a number of
         addresses. When those addresses are accessed, the accesses are redirected to a remap table specified
         in the FPB configuration, which means the program in the non-modifiable ROM can be patched.

10.1.3   Cortex-M4 Processor Features and Configuration
           •   Thumb® instruction set combines high code density with 32-bit performance
           •   IEEE 754-compliant single-precision Floating Point Unit (FPU)
           •   Integrated sleep modes for low power consumption
           •   Fast code execution permits slower processor clock or increases Sleep mode time
           •   Hardware division and fast digital-signal-processing orientated multiply accumulate
           •   Saturating arithmetic for signal processing
           •   Deterministic, high-performance interrupt handling for time-critical applications
           •   Memory Protection Unit (MPU) for safety-critical applications
           •   Extensive debug and trace capabilities: Serial Wire Debug and Serial Wire Trace reduce the number
               of pins required for debugging, tracing, and code profiling.

          Features                  Cortex-M4 Options                             SAM D5x/E5x Configuration
          Interrupts                1 to 240                                      138
          Number of priority        3 to 8                                        3 = eight levels of priority
          bits
          Data endianness           Little-endian or big-endian                   Little-endian
          SysTick Timer                                                           0x80000000
          calibration value
          MPU                       Present or Not present                        Present




         © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 62
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    Processor and Architecture

         ...........continued
          Features                  Cortex-M4 Options                                  SAM D5x/E5x Configuration
          Debug support level 0 = No debug. No DAP, breakpoints,                       3 = Full debug plus DWT data
                              watchpoints, Flash patch, or halting debug.              matching.
                                    1 = Minimum debug. Two breakpoints, one
                                    watchpoint, no Flash patch.
                                    2 = Full debug minus DWT data matching.
                                    3 = Full debug plus DWT data matching.

          Trace support level       0 = No trace. No ETM, ITM or DWT triggers and      2 = Full trace. ITM, TPIU, ETM,
                                    counters.                                          and DWT triggers and
                                                                                       counters are present. HTM
                                    1 = Standard trace. ITM and DWT triggers and
                                                                                       port is not present
                                    counters, but no ETM.
                                    2 = Full trace. Standard trace plus ETM.
                                    3 = Full trace plus HTM port.

          JTAG                      Present or Not present                             Not present
          Bit Banding               Present or Not present                             Not present
          FPU                       Present or Not present                             Present

10.1.4   Cortex-M4 Core Peripherals

          Nested                The Nested Vector Interrupt Controller (NVIC) is an embedded interrupt controller
          Vectored              that supports low latency interrupt processing.
          Interrupt
          Controller
          System Control The System Control Block (SCB) is the programmers model interface to the
          Block          processor. It provides system implementation information and system control,
                         including configuration, control, and reporting of system exceptions. Refer to the
                         Cortex-M4 Technical Reference Manual for details (http://www.arm.com).
          System Timer          The system timer, SysTick, is a 24-bit count-down timer. Use this as a Real-Time
                                Operating System (RTOS) tick timer or as a simple counter. The SysTick timer runs
                                on the processor clock and it does not decrement when the processor is halted for
                                debugging. Refer to the Cortex-M4 Technical Reference Manual for details (http://
                                www.arm.com).
          Memory                The Memory Protection Unit (MPU) improves system reliability by defining the
          Protection Unit       memory attributes for different memory regions. It provides up to eight different
                                regions, and an optional predefined background region. Refer to the Cortex-M4
                                Technical Reference Manual for details (http://www.arm.com).
          Floating-Point        The Floating Point Unit (FPU) provides IEEE 754-compliant operations on single-
          Unit                  precision, 32-bit, floating-point values. Refer to the Cortex-M4 Technical Reference
                                Manual for details (http://www.arm.com).

10.1.5   Cortex-M4 Address Map




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 63
                                                            SAM D5x/E5x Family Data Sheet
                                                                                   Processor and Architecture

          Address                                        Core Peripheral
          0xE000E008-0xE000E00F                          System control block
          0xE000E010-0xE000E01F                          System timer
          0xE000E100-0xE000E4EF                          Nested Vectored Interrupt Controller
          0xE000ED00-0xE000ED3F                          System control block
          0xE000ED90-0xE000ED93                          MPU Type Register
          0xE000ED90-0xE000EDB8                          Memory Protection Unit
          0xE000EF00-0xE000EF03                          Nested Vectored Interrupt Controller
          0xE000EF30-0xE000EF44                          Floating Point Unit

         Related Links
         8. Product Memory Mapping Overview



10.2     Nested Vector Interrupt Controller

10.2.1   Overview
         The Nested Vectored Interrupt Controller (NVIC) in the SAM D5x/E5x family devices supports 138
         interrupts with eight different priority levels. For more details, refer to the Cortex-M4 Technical Reference
         Manual (http://www.arm.com).

10.2.2   Interrupt Line Mapping
         Each of the interrupt lines is connected to one peripheral instance, as shown in the table below. Each
         peripheral can have many interrupt flags, located in the peripheral’s Interrupt Flag Status and Clear
         (INTFLAG) register.
         An interrupt flag is set when the interrupt condition occurs. Each interrupt in the peripheral can be
         individually enabled by writing a '1' to the corresponding bit in the peripheral’s Interrupt Enable Set
         (INTENSET) register, and disabled by writing '1' to the corresponding bit in the peripheral’s Interrupt
         Enable Clear (INTENCLR) register.
         An interrupt request is generated from the peripheral when the interrupt flag is set and the corresponding
         interrupt is enabled.
         Depending on their criticality, the interrupt requests for one peripheral are either ORed together on
         system level, generating one interrupt or directly connected to an NVIC interrupt lines. This is described
         in the table below.
         An interrupt request will set the corresponding interrupt pending bit in the NVIC interrupt pending
         registers (SETPEND/CLRPEND bits in ISPR/ICPR).
         For the NVIC to activate the interrupt, it must be enabled in the NVIC interrupt enable register (SETENA/
         CLRENA bits in ISER/ICER). The NVIC interrupt priority registers IPR0-IPR7 provide a priority field for
         each interrupt.

          Module                                                                    Source                     Line
          EIC NMI - External Interrupt Control                                      NMI                        NMI




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 64
                                           SAM D5x/E5x Family Data Sheet
                                                       Processor and Architecture

...........continued
 Module                                                 Source                 Line
 PM - Power Manager                                     SLEEPRDY               0
 MCLK - Main Clock                                      CKRDY                  1
 OSCCTRL - Oscillators Control                          XOSCFAIL 0             2
                                                        XOSCRDY 0
                                                        XOSCFAIL 1             3
                                                        XOSCRDY 1
                                                        DFLLLOCKC              4
                                                        DFLLLOCKF
                                                        DFLLOOB
                                                        DFLLRCS
                                                        DFLLRDY
                                                        DPLLLCKF 0             5
                                                        DPLLLCKR 0
                                                        DPLLLDRTO 0
                                                        DPLLLTO 0
                                                        DPLLLCKF 1             6
                                                        DPLLLCKR 1
                                                        DPLLLDRTO 1
                                                        DPLLLTO 1
 OSC32KCTRL - 32 kHz Oscillators Control                XOSC32KFAIL            7
                                                        XOSC32KRDY
 SUPC - Supply Controller                               BOD33RDY               8
                                                        B33SRDY
                                                        VCORERDY
                                                        VREGRDY
                                                        BOD33DET               9
 WDT - Watchdog Timer                                   EW                     10




© 2019 Microchip Technology Inc.           Datasheet                 DS60001507E-page 65
                                       SAM D5x/E5x Family Data Sheet
                                                   Processor and Architecture

...........continued
 Module                                             Source                Line
 RTC - Real-Time Counter                            CMP A 0               11
                                                    CMP A 1
                                                    CMP A 2
                                                    CMP A 3
                                                    OVF A
                                                    PER A 0
                                                    PER A 1
                                                    PER A 2
                                                    PER A 3
                                                    PER A 4
                                                    PER A 5
                                                    PER A 6
                                                    PER A 7
                                                    TAMPER A
 EIC - External Interrupt Controller                EXTINT 0              12
                                                    EXTINT 1              13
                                                    EXTINT 2              14
                                                    EXTINT 3              15
                                                    EXTINT 4              16
                                                    EXTINT 5              17
                                                    EXTINT 6              18
                                                    EXTINT 7              19
                                                    EXTINT 8              20
                                                    EXTINT 9              21
                                                    EXTINT 10             22
                                                    EXTINT 11             23
                                                    EXTINT 12             24
                                                    EXTINT 13             25
                                                    EXTINT 14             26
                                                    EXTINT 15             27
 FREQM - Frequency Meter                            DONE                  28




© 2019 Microchip Technology Inc.       Datasheet                DS60001507E-page 66
                                               SAM D5x/E5x Family Data Sheet
                                                           Processor and Architecture

...........continued
 Module                                                     Source                  Line
 NVMCTRL - Non-Volatile Memory Controller(1)                0                       29
                                                            1
                                                            2
                                                            3
                                                            4
                                                            5
                                                            6
                                                            7
                                                            8                       30
                                                            9
                                                            10
 DMAC - Direct Memory Access Controller                     SUSP 0                  31
                                                            TCMPL 0
                                                            TERR 0
                                                            SUSP 1                  32
                                                            TCMPL 1
                                                            TERR 1
                                                            SUSP 2                  33
                                                            TCMPL 2
                                                            TERR 2
                                                            SUSP 3                  34
                                                            TCMPL 3
                                                            TERR 3
                                                            SUSP 4..31              35
                                                            TCMPL 4..31
                                                            TERR 4..31




© 2019 Microchip Technology Inc.               Datasheet                  DS60001507E-page 67
                                             SAM D5x/E5x Family Data Sheet
                                                             Processor and Architecture

...........continued
 Module                                                       Source                Line
 EVSYS - Event System Interface                               EVD 0                 36
                                                              OVR 0
                                                              EVD 1                 37
                                                              OVR 1
                                                              EVD 2                 38
                                                              OVR 2
                                                              EVD 3                 39
                                                              OVR 3
                                                              EVD 4..11             40
                                                              OVR 4..11
 PAC - Peripheral Access Controller                           ERR                   41
 RAM ECC                                                      0                     45
                                                              1
 SERCOM0 - Serial Communication Interface 0(1)                0                     46
                                                              1                     47
                                                              2                     48
                                                              3                     49
                                                              4
                                                              5
                                                              7
 SERCOM1 - Serial Communication Interface 1(1)                0                     50
                                                              1                     51
                                                              2                     52
                                                              3                     53
                                                              4
                                                              5
                                                              7




© 2019 Microchip Technology Inc.                 Datasheet                DS60001507E-page 68
                                             SAM D5x/E5x Family Data Sheet
                                                             Processor and Architecture

...........continued
 Module                                                       Source              Line
 SERCOM2 - Serial Communication Interface 2(1)                0                   54
                                                              1                   55
                                                              2                   56
                                                              3                   57
                                                              4
                                                              5
                                                              7
 SERCOM3 - Serial Communication Interface 3(1)                0                   58
                                                              1                   59
                                                              2                   60
                                                              3                   61
                                                              4
                                                              5
                                                              7
 SERCOM4 - Serial Communication Interface 4(1)                0                   62
                                                              1                   63
                                                              2                   64
                                                              3                   65
                                                              4
                                                              5
                                                              7
 SERCOM5 - Serial Communication Interface 5(1)                0                   66
                                                              1                   67
                                                              2                   68
                                                              3                   69
                                                              4
                                                              5
                                                              7




© 2019 Microchip Technology Inc.                 Datasheet              DS60001507E-page 69
                                             SAM D5x/E5x Family Data Sheet
                                                             Processor and Architecture

...........continued
 Module                                                       Source              Line
 SERCOM6 - Serial Communication Interface 6(1)                0                   70
                                                              1                   71
                                                              2                   72
                                                              3                   73
                                                              4
                                                              5
                                                              7
 SERCOM7 - Serial Communication Interface 7(1)                0                   74
                                                              1                   75
                                                              2                   76
                                                              3                   77
                                                              4
                                                              5
                                                              7
 CAN0 - Control Area Network 0                                LINE 0              78
                                                              LINE 1
 CAN1 - Control Area Network 1                                LINE 0              79
                                                              LINE 1




© 2019 Microchip Technology Inc.                 Datasheet              DS60001507E-page 70
                                   SAM D5x/E5x Family Data Sheet
                                               Processor and Architecture

...........continued
 Module                                         Source                  Line
 USB - Universal Serial Bus                     EORSM DNRSM             80
                                                EORST RST
                                                LPM DCONN
                                                LPMSUSP DDISC
                                                MSOF
                                                RAMACER
                                                RXSTP TXSTP 0..7
                                                STALL0 STALL 0..7
                                                STALL1 0..7
                                                SUSPEND
                                                TRFAIL0 TRFAIL 0..7
                                                TRFAIL1 PERR 0..7
                                                UPRSM
                                                WAKEUP
                                                SOF HSOF                81
                                                TRCPT0 0..7             82
                                                TRCPT1 0..7             83
 GMAC - Ethernet MAC                            GMAC                    84
                                                WOL




© 2019 Microchip Technology Inc.   Datasheet                  DS60001507E-page 71
                                   SAM D5x/E5x Family Data Sheet
                                               Processor and Architecture

...........continued
 Module                                         Source               Line
 TCC0 - Timer Counter Control 0                 CNT A                85
                                                DFS A
                                                ERR A
                                                FAULTA A
                                                FAULTB A
                                                FAULT0 A
                                                FAULT1 A
                                                OVF
                                                TRG
                                                UFS A
                                                MC 0                 86
                                                MC 1                 87
                                                MC 2                 88
                                                MC 3                 89
                                                MC 4                 90
                                                MC 5                 91
 TCC1 - Timer Counter Control 1                 CNT A                92
                                                DFS A
                                                ERR A
                                                FAULTA A
                                                FAULTB A
                                                FAULT0 A
                                                FAULT1 A
                                                OVF
                                                TRG
                                                UFS A
                                                MC 0                 93
                                                MC 1                 94
                                                MC 2                 95
                                                MC 3                 96




© 2019 Microchip Technology Inc.   Datasheet               DS60001507E-page 72
                                   SAM D5x/E5x Family Data Sheet
                                               Processor and Architecture

...........continued
 Module                                         Source               Line
 TCC2 - Timer Counter Control 2                 CNT A                97
                                                DFS A
                                                ERR A
                                                FAULTA A
                                                FAULTB A
                                                FAULT0 A
                                                FAULT1 A
                                                OVF
                                                TRG
                                                UFS A
                                                MC 0                 98
                                                MC 1                 99
                                                MC 2                 100
 TCC3 - Timer Counter Control 3                 CNT A                101
                                                DFS A
                                                ERR A
                                                FAULTA A
                                                FAULTB A
                                                FAULT0 A
                                                FAULT1 A
                                                OVF
                                                TRG
                                                UFS A
                                                MC 0                 102
                                                MC 1                 103




© 2019 Microchip Technology Inc.   Datasheet               DS60001507E-page 73
                                   SAM D5x/E5x Family Data Sheet
                                               Processor and Architecture

...........continued
 Module                                         Source               Line
 TCC4 - Timer Counter Control 4                 CNT A                104
                                                DFS A
                                                ERR A
                                                FAULTA A
                                                FAULTB A
                                                FAULT0 A
                                                FAULT1 A
                                                OVF
                                                TRG
                                                UFS A
                                                MC 0                 105
                                                MC 1                 106
 TC0 - Basic Timer Counter 0                    ERR A                107
                                                MC 0
                                                MC 1
                                                OVF
 TC1 - Basic Timer Counter 1                    ERR A                108
                                                MC 0
                                                MC 1
                                                OVF
 TC2 - Basic Timer Counter 2                    ERR A                109
                                                MC 0
                                                MC 1
                                                OVF
 TC3 - Basic Timer Counter 3                    ERR A                110
                                                MC 0
                                                MC 1
                                                OVF




© 2019 Microchip Technology Inc.   Datasheet               DS60001507E-page 74
                                     SAM D5x/E5x Family Data Sheet
                                                 Processor and Architecture

...........continued
 Module                                           Source              Line
 TC4 - Basic Timer Counter 4                      ERR A               111
                                                  MC 0
                                                  MC 1
                                                  OVF
 TC5 - Basic Timer Counter 5                      ERR A               112
                                                  MC 0
                                                  MC 1
                                                  OVF
 TC6 - Basic Timer Counter 6                      ERR A               113
                                                  MC 0
                                                  MC 1
                                                  OVF
 TC7 - Basic Timer Counter 7                      ERR A               114
                                                  MC 0
                                                  MC 1
                                                  OVF
 PDEC - Position Decoder                          DIR A               115
                                                  ERR A
                                                  OVF
                                                  VLC A
                                                  MC 0                116
                                                  MC 1                117
 ADC0 - Analog Digital Converter 0                OVERRUN             118
                                                  WINMON
                                                  RESRDY              119
 ADC1 - Analog Digital Converter 1                OVERRUN             120
                                                  WINMON
                                                  RESRDY              121
 AC - Analog Comparators                          COMP 0              122
                                                  COMP 1
                                                  WIN 0




© 2019 Microchip Technology Inc.     Datasheet              DS60001507E-page 75
                                                SAM D5x/E5x Family Data Sheet
                                                                     Processor and Architecture

...........continued
 Module                                                                Source                  Line
 DAC - Digital-to-Analog Converter                                     OVERRUN A 0             123
                                                                       OVERRUN A 1
                                                                       UNDERRUN A 0
                                                                       UNDERRUN A 1
                                                                       EMPTY 0                 124
                                                                       EMPTY 1                 125
                                                                       RESRDY 0                126
                                                                       RESRDY 1                127
 I2S - Inter-IC Sound Interface                                        RXOR 0                  128
                                                                       RXOR 1
                                                                       RXRDY 0
                                                                       RXRDY 1
                                                                       TXRDY 0
                                                                       TXRDY 1
                                                                       TXUR 0
                                                                       TXUR 1
 PCC - Parallel Capture Controller                                     PCC                     129
 AES - Advanced Encryption Standard                                    ENCCMP                  130
                                                                       GFMCMP
 TRNG - True Random Generator                                          IS0                     131
 ICM - Integrity Check Monitor                                         ICM                     132
 PUKCC - Public-Key Cryptography Controller                            PUKCC                   133
 QSPI - Quad SPI interface                                             QSPI                    134
 SDHC0 - SD/MMC Host Controller 0                                      SDHC0                   135
                                                                       TIMER
 SDHC1 - SD/MMC Host Controller 1                                      SDHC1                   136
                                                                       TIMER

Note:
 1. The integer number specified in the source refers to the respective bit position in the INTFLAG
      register of respective peripheral.
Note: Lines not listed here are reserved.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 76
                                                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                                                                                                    Processor and Architecture


10.3     High-Speed Bus System

10.3.1   Features
         High-Speed Bus Matrix has the following features:
            •              Symmetric crossbar bus switch implementation
            •              Allows concurrent accesses from different masters to different slaves
            •              32-bit data bus
            •              Operation at a one-to-one clock frequency with the bus masters
         FlexRAM Memory has the following features:
            • Unified System Memory area
            • Allows concurrent accesses from different masters
            • Offers privileged accesses from specific masters

10.3.2   Configuration
         Figure 10-1. Master-Slave Relations High-Speed Bus Matrix
                                                                                                    High-Speed Bus SLAVES




                                                                                                                                                    HSB-PB Bridge C


                                                                                                                                                                      HSB-PB Bridge D
                                                                                                                HSB-PB Bridge A


                                                                                                                                  HSB-PB Bridge B




                                                                                                                                                                                                                        BACKUPRAM
                                            NVMCTRL0


                                                       NVMCTRL1


                                                                  SEEPROM




                                                                                                                                                                                        PUKCC
                                                                            SRAM0


                                                                                    SRAM1


                                                                                            SRAM2


                                                                                                    SRAM3




                                                                                                                                                                                                SDHC0


                                                                                                                                                                                                        SDHC1


                                                                                                                                                                                                                 QSPI
                                             0          1          2        3       4       5       6             7                 8                 9                 10              11      12      13        14     15



                            CM4S        0


                            CMCC        1
          High-Speed Bus
             MASTERS




                            DMAC DTWR 4


                            DMAC DTRD   5


                            ICM         6


                            DSU         7




         Table 10-1. High Speed Bus Matrix Masters

          High-Speed Bus Matrix Masters                                                                     Master ID
          CM4S - Cortex M4 Processor                                                                        0
          CMCC - Cortex-M Cache Controller                                                                  1
          DMAC - Direct Memory Access Controller / Data                                                     4
          Write Access
          DMAC - Direct Memory Access Controller / Data                                                     5
          Read Access




         © 2019 Microchip Technology Inc.                                                              Datasheet                                                                                                DS60001507E-page 77
                                                          SAM D5x/E5x Family Data Sheet
                                                                                Processor and Architecture

         ...........continued
          High-Speed Bus Matrix Masters                       Master ID
          ICM - Integrity Check Monitor                       6
          DSU - Device Service Unit                           7

         Table 10-2. High-Speed Bus Matrix Slaves

          High-Speed Bus Matrix Slaves                        Slave ID
          Internal Flash Memory                               0, 1
          Smart EEPROM                                        2
          SRAM Port 0 - CM4 Access                            3
          SRAM Port 1 - DSU Access                            4
          SRAM Port 2 - DMAC Data-Write Access                5
          SRAM Port 3 - DMAC Data-Read and ICM Access         6
          AHB-APB Bridge A                                    7
          AHB-APB Bridge B                                    8
          AHB-APB Bridge C                                    9
          AHB-APB Bridge D                                    10
          PUKCC                                               11
          SDHC0                                               12
          SDHC1                                               13
          QSPI                                                14
          BACKUP RAM Memory                                   15

10.3.3   SRAM Quality of Service
         To ensure that masters with latency requirements get sufficient priority when accessing RAM, priority
         levels can be assigned to the masters for different types of access.
         The Quality of Service (QoS) level is independently selected for each master accessing the RAM. For any
         access to the RAM, the RAM also receives the QoS level. The QoS levels and their corresponding bit
         values for the QoS level configuration is shown in the table below.
         Table 10-3. Quality of Service

          Value                              Name                               Description
          0x0                                DISABLE                            Background (no sensitive
                                                                                operation)
          0x1                                LOW                                Sensitive Bandwidth
          0x2                                MEDIUM                             Sensitive Latency
          0x3                                HIGH                               Critical Latency




         © 2019 Microchip Technology Inc.                   Datasheet                              DS60001507E-page 78
                                                      SAM D5x/E5x Family Data Sheet
                                                                          Processor and Architecture

If a master is configured with QoS level DISABLE (0x0) or LOW (0x1) there will be a minimum latency of
one cycle for the RAM access.
The priority order for concurrent accesses are decided by two factors. First, the QoS level for the master
and second, a static priority given by the port ID. The lowest port ID has the highest static priority. See the
tables below for details.
The CPU QoS level can be written/read, using 32-bit access only, at address 0x4100C11C, bits [1:0]. Its
reset value is 0x3.
The ICM QoS level can be written/read, using 32-bit access only, at address 0x4100C128, bits [1:0]. Its
reset value is 0x1.
Refer to different master QOS control registers for configuring QoS for the other masters (DSU, DMAC,
CAN, USB).
Table 10-4. SRAM Port Connections QoS

 SRAM Port                Port ID            Connection Type       QoS                   default QoS
 Connection
 CM4 - Cortex M4          0                  Bus Matrix            0x4100C11C,           0x3
 Processor                                                         bits[1:0](1)
 DSU - Device             1                  Bus Matrix            IP-CFG.LQOS           0x2
 Service Unit
 DMAC - Direct            2 (WR), 3 (RD)     Bus Matrix            IP-                   0x2
 Memory Access                                                     PRICTRL0.QOSn
 Controller - Data
 Access
 ICM - Integrity          3                  Bus Matrix            0x4100C128,           0x1
 Check Monitor                                                     bits[1:0](1)
 DMAC - Direct            4, 5               Direct                IP-                   0x2
 Memory Access                                                     PRICTRL0.QOSn
 Controller - Fetch
 Access
 DMAC - Direct            6, 7               Direct                IP-                   0x2
 Memory Access                                                     PRICTRL0.QOSn
 Controller - Write-
 Back Access
 SDHC0 - SD/MMC           8                  Direct                STATIC-1              0x1
 Host Controller
 SDHC1 - SD/MMC           9                  Direct                STATIC-1              0x1
 Host Controller
 CAN0 - Control           10                 Direct                IP-MRCFG.QOS          0x1
 Area Network
 CAN1 - Control           11                 Direct                IP-MRCFG.QOS          0x1
 Area Network




© 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 79
                                              SAM D5x/E5x Family Data Sheet
                                                                Processor and Architecture

...........continued
 SRAM Port                Port ID    Connection Type      QoS             default QoS
 Connection
 GMAC - Ethernet          12         Direct               STATIC-2        0x2
 MAC
 USB - Universal          13         Direct               IP-             0x3
 Serial Bus -                                             QOSCTRL.CQOS
 Configuration
 Access
 USB - Universal          13         Direct               IP-             0x3
 Serial Bus - Data                                        QOSCTRL.DQOS
 Access

Note: 1. Using 32-bit access only.




© 2019 Microchip Technology Inc.              Datasheet                    DS60001507E-page 80
