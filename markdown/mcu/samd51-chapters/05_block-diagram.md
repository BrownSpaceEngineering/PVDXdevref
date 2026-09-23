# 3. Block Diagram

*Source: `Atmel-SAMD51.pdf`, pages 20-21 — SAMD51 family datasheet*

                                                                                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                                                                                                                                                                       Block Diagram


3.    Block Diagram
      The actual configuration may vary with device memory and number of pins. Refer to the Configuration
      Summary for details.


3.1   SAM D5x/E5x Block Diagram
                                                      SWO
                                                                                                        24bit SysTick




                                                                                          TPIU
                                                    TRACECLK
                                                  TRACEDATA[3:0]
                                                                                                          Counter                                1024/512/256KB                                               256/192/128KB




                                                                                                                                 CORESIGHT ETB
                                                                                                   CORTEX-M4                                          NVM                                                         SRAM
                                                                                                  PROCESSOR




                                                                                                                                     ETM
                                                                                                                                                    NVM                                                          SRAM
                                                                       BACKUP                     Fmax 120MHz                                                               DMA
                                                                                                                                                 CONTROLLER                                                   CONTROLLER
                                                                        SRAM                                                                                             CONTROLLER
                                                                                                  MPU                 FPU                           Cache                                                   RAMECC


                                                                                                                  I         D
                                                                                                                Cortex M
                                                                                                             Cache Controller
                      SWCLK
                                               SERIAL
                      SWDIO
                                                WIRE
                                                                   M     S                        S                     M                               M                          M                    S                                  DMA                 CD
                                                                                                                                                                                                                                             2x SDHC          CMD
                                               DEVICE                                                                                                                                                   S                                                      WP
                                                                                                                                                                                                                                           Host Controller     CK
                                               SERVICE                                                                          HIGH SPEED                                                                                                                   DAT[3:0]
                                                 UNIT                                                                           BUS MATRIX                                                                                           DMA
                                                                                                                                                                                                                                                                DP
                                                                                                                                                                                                                                        USB FS/LS               DM
                                                                   S            S                                                                                   M     S         S         S                                        HOST/DEVICE           SOF-1KHz

                                                                                                                                                                                                                               DMA
                                                                                                                                                                                                                                                             GTXEN
                                                                                                                                                                                                                                                             GTXCK
                                                                                                                                                                                                                                                             GTX[3:0]
                                                                                                                                                                                                                                                             GTXER
                                                                                                                                                                                             AHB-APB                                                         GRXER
                                                            AHB-APB          AHB-APB                                                                                                                                                                         GRXCK
                                                                                                                        EVENT SYSTEM                                             AHB-APB     BRIDGE B                                ETHERNET                GRX[3:0]
                                                            BRIDGE A         BRIDGE D
                                                                                                                                                                                 BRIDGE C                                              MAC                   GRXDV
                                                                                                                                                                                                                                                              GCOL
                                                                                                                                                                                                                                                              GCRS
                                                                                                                                                                                                                                                             GMDIO
                                                                                    DMA                                              PAD0                      CS         XIP                     DMA                                                         GMDC
                                                                                                                                                                        MEMORY
                                     PERIPHERAL                                                                                      PAD1                     SCK
                                                                                                 4x SERCOM                                                  DATA[3:0]
                                                                                                                                                                                  QUAD-SPI
                                  ACCESS CONTROLLER                                                                                  PAD2
                                                                                                                                     PAD3                                                                                DMA




                                                                                                                                                                                                                                                                         PORT
                                                                                                                                                                                                                                                                TX
                                               POWER                                                                                                                                              DMA                                2x CAN
                                                                                    DMA                                                                                                                                                                         RX
                                              MANAGER                                     TIMER / COUNTER                            WO0                                               AES
                                                                                            8 x Timer Counter                        WO1
                                         MAIN CLOCKS                                        FOR  CONTROL                                                                                                                 DMA
                                                                                                                                                                                                                                                              WO0
                                         CONTROLLER                                                                                                                                               DMA
                                                                                                                                                                                                                          2x TIMER / COUNTER                  WO1
                                                                                    DMA                                                                                    INTEGRITY CHECK                                    8 x Timer Counter
                                                                                                                                     WO0                                       MONITOR                                       FOR   CONTROL                    WO2
                                           RESET                                        2x TIMER / COUNTER                           WO1
                                                                                            8 x Timer Counter
        PORT




                                         CONTROLLER                                                                                                                                                                      DMA

                                                                                                                                                                           TRUE RANDOM                                                                        WO0
                                                                                                                                   AIN[15:0]                                                                              2x TIMER / COUNTER
                         OSCILLATORS CONTROLLER                                     DMA
                                                                                                                                                                         NUMBER GENERATOR                                     8 x Timer Counter               WO1
                                                                                           2x 16-CHANNEL                            VREFA
                XIN                     CFD
                                                                                            8 x Timer
                                                                                          12-bit      Counter
                                                                                                 ADC 1MSPS                          VREFB
               XOUT                             DFLL48M
                                                                                                                                                     PORT




                            XOSC48M                                                                                                 VREFC                                                                                DMA                                   QDI0
                                                                                                                                                                                PUBLIC KEY
                                                                                                                                                                                                                                                               QDI1
                                                                                                                                                                              CRYPTOGRAPHY                                POSITION DECODER
                XIN
                                               FDPLL200M                                                                                                                       CONTROLLER                                                                      QDI2
                                        CFD                                             PERIPHERAL TOUCH                             X/Y[31:0]
               XOUT
                            XOSC48M                                                       8CONTROLLER
                                                                                            x Timer Counter
                                               FDPLL200M                                                                                                     PAD0                                 DMA

                                                                                                                                                             PAD1                                                                                              OUT
                                                                                                                                                                                 2x SERCOM                                           4x CCL                   IN[2:0]
                                                                                    DMA
                                                                                                                                   VOUT[1:0]                 PAD2
                            OSC32K CONTROLLER                                              DUAL-CHANNEL                                                      PAD3
                XIN32                                                                                                               VREFA
                                        CFD                                                8 x Timer
                                                                                          12-bit DAC Counter
                                                                                                     1MSPS
               XOUT32                                                                                                                                         WO0                                 DMA
                            XOSC32K             OSCULP32K                                                                       MCKn, n={0,1}                                                                                      2 ANALOG                   AIN[3:0]
                                                                                    DMA
                                                                                                                                                              WO1
                                                                                                                                                                    .
                                                                                                                                                                         2x TIMER / COUNTER
                                                                                                                                SCKn, n={0,1}                                                                                    COMPARATORS
                                                                                                                                                                    .        8 x Timer
                                                                                                                                                                            FOR        Counter
                                                                                                                                                                                  CONTROL
                                                                                                  Inter-IC                       FSn, n={0,1}                 WO7 .
                            SUPPLY CONTROLLER                                                8 x Timer Counter                      SDO
                                                                                             Sound Controller
                                                                                                                                     SDI                                                          DMA
                                                  VREF                                                                                                        WO0
                                BOD33                                               DMA
                                                                                                                                    CLK
                                                                                                                                                              WO1
                                                                                                                                                                         2x TIMER / COUNTER
                                                                                                                                   DEN1                                      8 x Timer Counter
                                                  VREG                                       Parallel Capture
                                                                                                                                   DEN2
                                                                                             8 x Controller
                                                                                                 Timer Counter                   DATA[13:0]
                GCLK_IO[7..0]       GENERIC CLOCK
                                     CONTROLLER

                                         WATCHDOG
                                           TIMER
                                                          DMA
                TAMPER[4:0]               REAL-TIME
                                          COUNTER
                EXTINT[15..0]
                                 EXTERNAL INTERRUPT
                    NMI
                                    CONTROLLER

                                         FREQUENCY
                                           METER
                  PAD0                                    DMA

                  PAD1
                                          2x SERCOM
                  PAD2
                  PAD3

                                                          DMA

                   WO0
                                  2x TIMER / COUNTER
                   WO1                8 x Timer Counter




      Note:
       1. Some products have different number of SERCOM instances, Timer/Counter instances, PTC
            signals and ADC signals.
       2. The block diagram is representing SAM E54P. Refer to the Configuration Summary for the
            configuration of a given device.




      © 2019 Microchip Technology Inc.                                                                                                                Datasheet                                                                                      DS60001507E-page 20
                                   SAM D5x/E5x Family Data Sheet
                                                      Block Diagram

Related Links
1. Configuration Summary




© 2019 Microchip Technology Inc.   Datasheet          DS60001507E-page 21
