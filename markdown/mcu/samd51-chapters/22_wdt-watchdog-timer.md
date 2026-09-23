# 20. WDT – Watchdog Timer

*Source: `Atmel-SAMD51.pdf`, pages 265-282 — SAMD51 family datasheet*

                                                        SAM D5x/E5x Family Data Sheet
                                                                                   WDT – Watchdog Timer


20.    WDT – Watchdog Timer

20.1   Overview
       The Watchdog Timer (WDT) is a system function for monitoring correct program operation. It makes it
       possible to recover from error situations such as runaway or deadlocked code. The WDT is configured to
       a predefined time-out period, and is constantly running when enabled. If the WDT is not cleared within the
       time-out period, it will issue a system reset. An early-warning interrupt is available to indicate an
       upcoming watchdog time-out condition.
       The window mode makes it possible to define a time slot (or window) inside the total time-out period
       during which the WDT must be cleared. If the WDT is cleared outside this window, either too early or too
       late, a system reset will be issued. Compared to the normal mode, this can also catch situations where a
       code error causes the WDT to be cleared frequently.
       When enabled, the WDT will run in active mode and any sleep modes, except Hibernate, Backup and
       OFF sleep mode. It is asynchronous and runs from a CPU-independent clock source. The WDT will
       continue operation and issue a system reset or interrupt even if the main clocks fail.



20.2   Features
         • Issues a system reset if the Watchdog Timer is not cleared before its time-out period
         • Early Warning interrupt generation
         • Asynchronous operation from dedicated oscillator
         • Two types of operation
             – Normal
             – Window mode
         • Selectable time-out periods
             – From 8 cycles to 16,384 cycles in Normal mode
             – From 16 cycles to 32,768 cycles in Window mode
         • Always-On capability




       © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 265
                                                           SAM D5x/E5x Family Data Sheet
                                                                                        WDT – Watchdog Timer


20.3     Block Diagram
         Figure 20-1. WDT Block Diagram
                                                0xA5



                                                                     0
                                               CLEAR



                                            CLK_WDT_OSC
                         OSC32KCTRL                              COUNT




                        PER/WINDOWS/EWOFFSET

                                                                                Early Warning Interrupt
                                                                                Reset



20.4     Signal Description
         Not applicable.



20.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

20.5.1   I/O Lines
         Not applicable.

20.5.2   Power Management
         The WDT can continue to operate in any sleep modes where the selected source clock is running. The
         WDT interrupts can be used to wake up the device from sleep modes. The events can trigger other
         operations in the system without exiting sleep modes.
         Related Links
         18. PM – Power Manager

20.5.3   Clocks
         The WDT bus clock (CLK_WDT_APB) can be enabled and disabled (masked) in the Main Clock module
         (MCLK).
         A 1.024 kHz oscillator clock (CLK_WDT_OSC) is required to clock the WDT internal counter.
         The CLK_WDT_OSC CLOCK is sourced from the clock of the internal Ultra Low-Power Oscillator
         (OSCULP32K). Due to ultra low-power design, the oscillator is not accurate, hence the exact time-out
         period may vary from device-to-device. This variation must be considered when designing software that
         uses the WDT to ensure that the time-out periods used are valid for all devices.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 266
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       WDT – Watchdog Timer

         The counter clock CLK_WDT_OSC is asynchronous to the bus clock (CLK_WDT_APB). Due to this
         asynchronicity, writing to certain registers will require synchronization between the clock domains. Refer
         to 20.6.7 Synchronization for further details.
         Related Links
         15.6.2.6 Peripheral Clock Masking
         29. OSC32KCTRL – 32KHz Oscillators Controller

20.5.4   DMA
         Not applicable.

20.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the WDT interrupt(s) requires the
         interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

20.5.6   Events
         Not applicable.

20.5.7   Debug Operation
         When the CPU is halted in debug mode the WDT will halt normal operation.

20.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Flag Status and Clear (INTFLAG) register
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.

20.5.9   Analog Connections
         Not applicable.



20.6     Functional Description

20.6.1   Principle of Operation
         The Watchdog Timer (WDT) is a system for monitoring correct program operation, making it possible to
         recover from error situations such as runaway code, by issuing a Reset. When enabled, the WDT is a
         constantly running timer that is configured to a predefined time-out period. Before the end of the time-out
         period, the WDT should be set back, or else, a system Reset is issued.
         The WDT has two modes of operation, Normal mode and Window mode. Both modes offer the option of
         Early Warning interrupt generation. The description for each of the basic modes is given below. The
         settings in the Control A register (CTRLA) and the Interrupt Enable register (handled by INTENCLR/
         INTENSET) determine the mode of operation:




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 267
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       WDT – Watchdog Timer

          Table 20-1. WDT Operating Modes

          CTRLA.ENABLE            CTRLA.WEN      Interrupt Enable    Mode
          0                       x              x                   Stopped
          1                       0              0                   Normal mode
          1                       0              1                   Normal mode with Early Warning interrupt
          1                       1              0                   Window mode
          1                       1              1                   Window mode with Early Warning interrupt

20.6.2    Basic Operation

20.6.2.1 Initialization
          The following bits are enable-protected, meaning that they can only be written when the WDT is disabled
          (CTRLA.ENABLE=0):
           • Control A register (CTRLA), except the Enable bit (CTRLA.ENABLE)
           • Configuration register (CONFIG)
           • Early Warning Interrupt Control register (EWCTRL)
          Enable-protected bits in the CTRLA register can be written at the same time as CTRLA.ENABLE is
          written to '1', but not at the same time as CTRLA.ENABLE is written to '0'.
          The WDT can be configured only while the WDT is disabled. The WDT is configured by defining the
          required Time-Out Period bits in the Configuration register (CONFIG.PER). If Window mode operation is
          desired, the Window Enable bit in the Control A register must be set (CTRLA.WEN=1) and the Window
          Period bits in the Configuration register (CONFIG.WINDOW) must be defined.
          Enable-protection is denoted by the "Enable-Protected" property in the register description.
20.6.2.2 Configurable Reset Values
          After a Power-on Reset, some registers will be loaded with initial values from the NVM User Row.
          This includes the following bits and bit groups:
           • Enable bit in the Control A register, CTRLA.ENABLE
           • Always-On bit in the Control A register, CTRLA.ALWAYSON
           • Watchdog Timer Windows Mode Enable bit in the Control A register, CTRLA.WEN
           • Watchdog Timer Windows Mode Time-Out Period bits in the Configuration register,
             CONFIG.WINDOW
           • Time-Out Period bits in the Configuration register, CONFIG.PER
           • Early Warning Interrupt Time Offset bits in the Early Warning Interrupt Control register,
             EWCTRL.EWOFFSET
20.6.2.3 Enabling, Disabling, and Resetting
          The WDT is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The
          WDT is disabled by writing a '0' to CTRLA.ENABLE.
          The WDT can be disabled only if the Always-On bit in the Control A register (CTRLA.ALWAYSON) is '0'.
20.6.2.4 Normal Mode
          In Normal mode operation, the length of a time-out period is configured in CONFIG.PER. The WDT is
          enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). Once enabled, the




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 268
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                               WDT – Watchdog Timer

        WDT will issue a system reset if a time-out occurs. This can be prevented by clearing the WDT at any
        time during the time-out period.
        The WDT is cleared and a new WDT time-out period is started by writing 0xA5 to the Clear register
        (CLEAR). Writing any other value than 0xA5 to CLEAR will issue an immediate system reset.
        There are 12 possible WDT time-out (TOWDT) periods, selectable from 8ms to 16s.
       By default, the early warning interrupt is disabled. If it is desired, the Early Warning Interrupt Enable bit in
       the Interrupt Enable register (INTENSET.EW) must be written to '1'. The Early Warning Interrupt is
       disabled again by writing a '1' to the Early Warning Interrupt bit in the Interrupt Enable Clear register
       (INTENCLR.EW).
       If the Early Warning Interrupt is enabled, an interrupt is generated prior to a WDT time-out condition. In
       Normal mode, the Early Warning Offset bits in the Early Warning Interrupt Control register,
       EWCTRL.EWOFFSET, define the time when the early warning interrupt occurs. The Normal mode
       operation is illustrated in the figure Normal-Mode Operation.
        Figure 20-2. Normal-Mode Operation
                                                 WDT Count

                                                                                                   Timely WDT Clear
                                          PER[3:0] = 1
                                                                                                   WDT Timeout

                                                                                                   System Reset
                                  EWOFFSET[3:0] = 0
                                                                                                   Early Warning Interrupt


                                                                                                     t[ms]
                                                             5   10   15    20   25      30   35

                                                                                 TOWDT



20.6.2.5 Window Mode
       In Window mode operation, the WDT uses two different time specifications: the WDT can only be cleared
       by writing 0xA5 to the CLEAR register after the closed window time-out period (TOWDTW), during the
       subsequent Normal time-out period (TOWDT). If the WDT is cleared before the time window opens (before
       TOWDTW is over), the WDT will issue a system reset.
        Both parameters TOWDTW and TOWDT are periods in a range from 8ms to 16s, so the total duration of the
        WDT time-out period is the sum of the two parameters.
        The closed window period is defined by the Window Period bits in the Configuration register
        (CONFIG.WINDOW), and the open window period is defined by the Period bits in the Configuration
        register (CONFIG.PER).
        By default, the Early Warning interrupt is disabled. If it is desired, the Early Warning Interrupt Enable bit in
        the Interrupt Enable register (INTENSET.EW) must be written to '1'. The Early Warning Interrupt is
        disabled again by writing a '1' to the Early Warning Interrupt bit in the Interrupt Enable Clear
        (INTENCLR.EW) register.
        If the Early Warning interrupt is enabled in Window mode, the interrupt is generated at the start of the
        open window period, i.e. after TOWDTW. The Window mode operation is illustrated in figure Window-Mode
        Operation.




       © 2019 Microchip Technology Inc.                                    Datasheet                                         DS60001507E-page 269
                                                                          SAM D5x/E5x Family Data Sheet
                                                                                                                  WDT – Watchdog Timer

         Figure 20-3. Window-Mode Operation
                                                  WDT Count

                                                                                                      Timely WDT Clear
                                        PER[3:0] = 0
                                                                                                      WDT Timeout




                                                       Open
                                                                                                      Early WDT Clear
                                    WINDOW[3:0] = 0
                                                                                                      Early Warning Interrupt




                                                       Closed
                                                                                                      System Reset
                                                                                                        t[ms]
                                                                5   10   15    20    25     30   35

                                                                         TOWDTW     TOWDT




20.6.3   DMA Operation
         Not applicable.

20.6.4   Interrupts
         The WDT has the following interrupt source:
           • Early Warning (EW): Indicates that the counter is approaching the time-out condition.
              – This interrupt is an asynchronous wake-up source.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs.
         Each interrupt can be individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Set (INTENSET) register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Clear (INTENCLR) register.
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or the
         WDT is reset. See the 20.8.6 INTFLAG register description for details on how to clear interrupt flags. All
         interrupt requests from the peripheral are ORed together on system level to generate one combined
         interrupt request to the NVIC. The user must read the INTFLAG register to determine which interrupt
         condition is present.
         Note: Interrupts must be globally enabled for interrupt requests to be generated.
         Related Links
         10.2 Nested Vector Interrupt Controller
         18. PM – Power Manager

20.6.5   Events
         Not applicable.

20.6.6   Sleep Mode Operation
         The WDT will continue to operate in any sleep mode where the source clock is active except backup
         mode. The WDT interrupts can be used to wake up the device from a sleep mode. An interrupt request
         will be generated after the wake-up if the Interrupt Controller is configured accordingly. Otherwise the
         CPU will wake up directly, without triggering an interrupt. In this case, the CPU will continue executing
         from the instruction following the entry into sleep.
         Related Links
         20.8.1 CTRLA




         © 2019 Microchip Technology Inc.                                     Datasheet                                         DS60001507E-page 270
                                                           SAM D5x/E5x Family Data Sheet
                                                                                     WDT – Watchdog Timer

20.6.7   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following registers are synchronized when written:
           •   Enable bit in Control A register (CTRLA.ENABLE)
           •   Window Enable bit in Control A register (CTRLA.WEN)
           •   Always-On bit in control Control A (CTRLA.ALWAYSON)
           •   Watchdog Clear register (CLEAR)
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.
         Required read synchronization is denoted by the "Read-Synchronized" property in the register
         description.

20.6.8   Additional Features

20.6.8.1 Always-On Mode
         The Always-On mode is enabled by setting the Always-On bit in the Control A register
         (CTRLA.ALWAYSON=1). When the Always-On mode is enabled, the WDT runs continuously, regardless
         of the state of CTRLA.ENABLE. Once written, the Always-On bit can only be cleared by a power-on
         reset. The Configuration (CONFIG) and Early Warning Control (EWCTRL) registers are read-only
         registers while the CTRLA.ALWAYSON bit is set. Thus, the time period configuration bits (CONFIG.PER,
         CONFIG.WINDOW, EWCTRL.EWOFFSET) of the WDT cannot be changed.
         Enabling or disabling Window mode operation by writing the Window Enable bit (CTRLA.WEN) is allowed
         while in Always-On mode, but note that CONFIG.PER cannot be changed.
         The Interrupt Clear and Interrupt Set registers are accessible in the Always-On mode. The Early Warning
         interrupt can still be enabled or disabled while in the Always-On mode, but note that
         EWCTRL.EWOFFSET cannot be changed.
         Table WDT Operating Modes With Always-On shows the operation of the WDT for
         CTRLA.ALWAYSON=1.
         Table 20-2. WDT Operating Modes With Always-On

          WEN       Interrupt Enable        Mode
          0         0                       Always-on and normal mode
          0         1                       Always-on and normal mode with Early Warning interrupt
          1         0                       Always-on and window mode
          1         1                       Always-on and window mode with Early Warning interrupt

20.6.8.2 Early Warning
         The Early Warning interrupt notifies that the WDT is approaching its time-out condition. The Early
         Warning interrupt behaves differently in Normal mode and in Window mode.
         In Normal mode, the Early Warning interrupt generation is defined by the Early Warning Offset in the
         Early Warning Control register (EWCTRL.EWOFFSET). The Early Warning Offset bits define the number
         of CLK_WDT_OSC clocks before the interrupt is generated, relative to the start of the watchdog time-out
         period.




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 271
                                                 SAM D5x/E5x Family Data Sheet
                                                                            WDT – Watchdog Timer

The user must take caution when programming the Early Warning Offset bits. If these bits define an Early
Warning interrupt generation time greater than the watchdog time-out period, the watchdog time-out
system reset is generated prior to the Early Warning interrupt. Consequently, the Early Warning interrupt
will never be generated.
In window mode, the Early Warning interrupt is generated at the start of the open window period. In a
typical application where the system is in sleep mode, the Early Warning interrupt can be used to wake
up and clear the Watchdog Timer, after which the system can perform other tasks or return to sleep
mode.

          If the WDT is operating in Normal mode with CONFIG.PER = 0x2 and
          EWCTRL.EWOFFSET = 0x1, the Early Warning interrupt is generated 16
          CLK_WDT_OSC clock cycles after the start of the time-out period. The time-out system
          reset is generated 32 CLK_WDT_OSC clock cycles after the start of the watchdog time-
          out period.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 272
                                                               SAM D5x/E5x Family Data Sheet
                                                                                        WDT – Watchdog Timer


20.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0     ALWAYSON                                           WEN         ENABLE
 0x01         CONFIG          7:0                WINDOW[3:0]                                   PER[3:0]
 0x02        EWCTRL           7:0                                                          EWOFFSET[3:0]
 0x03        Reserved
 0x04        INTENCLR         7:0                                                                                EW
 0x05        INTENSET         7:0                                                                                EW
 0x06        INTFLAG          7:0                                                                                EW
 0x07        Reserved
                              7:0                                  CLEAR     ALWAYSON    WEN         ENABLE
                             15:8
 0x08       SYNCBUSY
                             23:16
                             31:24
 0x0C         CLEAR           7:0                                      CLEAR[7:0]




20.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 20.5.8 Register Access Protection.
          Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
          Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
          refer to 20.6.7 Synchronization.
          Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
          Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




          © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 273
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                              WDT – Watchdog Timer

20.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       x initially determined from NVM User Row after reset
               Property:    PAC Write-Protection, Write-Synchronized


         Bit         7            6             5             4            3             2             1            0
                ALWAYSON                                                               WEN          ENABLE
   Access           R/W                                                                 R/W          R/W
    Reset            x                                                                   x             x


               Bit 7 – ALWAYSON Always-On
               This bit allows the WDT to run continuously. After being set, this bit cannot be written to '0', and the WDT
               will remain enabled until a power-on Reset is received. When this bit is '1', the Control A register
               (CTRLA), the Configuration register (CONFIG) and the Early Warning Control register (EWCTRL) will be
               read-only, and any writes to these registers are not allowed.
               Writing a '0' to this bit has no effect.
               This bit is not Enable-Protected.
               This bit is loaded from NVM User Row at start-up.
                Value        Description
                0            The WDT is enabled and disabled through the ENABLE bit.
                1            The WDT is enabled and can only be disabled by a power-on reset (POR).

               Bit 2 – WEN Watchdog Timer Window Mode Enable
               This bit enables Window mode. It can only be written if the peripheral is disabled unless
               CTRLA.ALWAYSON=1. The initial value of this bit is loaded from Flash Calibration.
               This bit is loaded from NVM User Row at startup.
                Value        Description
                0            Window mode is disabled (normal operation).
                1            Window mode is enabled.

               Bit 1 – ENABLE Enable
               This bit enables or disables the WDT. It can only be written if CTRLA.ALWAYSON=0.
               Due to synchronization, there is delay between writing CTRLA.ENABLE until the peripheral is enabled/
               disabled. The value written to CTRLA.ENABLE will read back immediately, and the Enable bit in the
               Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be cleared
               when the operation is complete.
               This bit is not Enable-Protected.
               This bit is loaded from NVM User Row at startup.
                Value        Description
                0            The WDT is disabled.
                1            The WDT is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 274
                                                                SAM D5x/E5x Family Data Sheet
                                                                                        WDT – Watchdog Timer

20.8.2         Configuration

               Name:       CONFIG
               Offset:     0x01
               Reset:      x initially determined from NVM User Row after reset
               Property:   PAC Write-Protection


         Bit        7             6                 5      4            3          2                1           0
                                      WINDOW[3:0]                                       PER[3:0]
   Access          R/W          R/W             R/W       R/W          R/W        R/W              R/W         R/W
    Reset           x             x                 x      x            x          x                x           x


               Bits 7:4 – WINDOW[3:0] Window Mode Time-Out Period
               In Window mode, these bits determine the watchdog closed window period as a number of cycles of the
               1.024kHz CLK_WDT_OSC clock.
               These bits are loaded from NVM User Row at start-up.
                Value      Name                             Description
                0x0        CYC8                             8 clock cycles
                0x1        CYC16                            16 clock cycles
                0x2        CYC32                            32 clock cycles
                0x3        CYC64                            64 clock cycles
                0x4        CYC128                           128 clock cycles
                0x5        CYC256                           256 clock cycles
                0x6        CYC512                           512 clock cycles
                0x7        CYC1024                          1024 clock cycles
                0x8        CYC2048                          2048 clock cycles
                0x9        CYC4096                          4096 clock cycles
                0xA        CYC8192                          8192 clock cycles
                0xB        CYC16384                         16384 clock cycles
                0xC-0xF Reserved                            Reserved

               Bits 3:0 – PER[3:0] Time-Out Period
               These bits determine the watchdog time-out period as a number of 1.024kHz CLK_WDTOSC clock
               cycles. In Window mode operation, these bits define the open window period.
               These bits are loaded from NVM User Row at startup.
                Value      Name                              Description
                0x0        CYC8                               8 clock cycles
                0x1        CYC16                              16 clock cycles
                0x2        CYC32                              32 clock cycles
                0x3        CYC64                              64 clock cycles
                0x4        CYC128                             128 clock cycles
                0x5        CYC256                             256 clock cycles
                0x6        CYC512                             512 clock cycles
                0x7        CYC1024                            1024 clock cycles
                0x8        CYC2048                            2048 clock cycles
                0x9        CYC4096                            4096 clock cycles
                0xA        CYC8192                            8192 clock cycles
                0xB        CYC16384                           16384 clock cycles




           © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 275
                                    SAM D5x/E5x Family Data Sheet
                                                 WDT – Watchdog Timer

 Value        Name                 Description
 0xC -        -                    Reserved
 0xF




© 2019 Microchip Technology Inc.     Datasheet         DS60001507E-page 276
                                                               SAM D5x/E5x Family Data Sheet
                                                                                        WDT – Watchdog Timer

20.8.3         Early Warning Control

               Name:       EWCTRL
               Offset:     0x02
               Reset:      x initially determined from NVM User Row after reset
               Property:   PAC Write-Protection


         Bit        7             6           5            4            3          2            1           0
                                                                                    EWOFFSET[3:0]
   Access                                                              R/W        R/W          R/W         R/W
    Reset                                                               x          x            x           x


               Bits 3:0 – EWOFFSET[3:0] Early Warning Interrupt Time Offset
               These bits determine the number of GCLK_WDT clock cycles between the start of the watchdog time-out
               period and the generation of the Early Warning interrupt. These bits are loaded from NVM User Row at
               start-up.
                Value      Name                              Description
                0x0        CYC8                              8 clock cycles
                0x1        CYC16                             16 clock cycles
                0x2        CYC32                             32 clock cycles
                0x3        CYC64                             64 clock cycles
                0x4        CYC128                            128 clock cycles
                0x5        CYC256                            256 clock cycles
                0x6        CYC512                            512 clock cycles
                0x7        CYC1024                           1024 clock cycles
                0x8        CYC2048                           2048 clock cycles
                0x9        CYC4096                           4096 clock cycles
                0xA        CYC8192                           8192 clock cycles
                0xB -      Reserved                          Reserved
                0xF




           © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 277
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                              WDT – Watchdog Timer

20.8.4         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x04
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

         Bit         7             6            5             4             3             2             1            0
                                                                                                                    EW
   Access                                                                                                           R/W
    Reset                                                                                                            0


               Bit 0 – EW Early Warning Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Early Warning Interrupt Enable bit, which disables the Early Warning
               interrupt.
                Value        Description
                0            The Early Warning interrupt is disabled.
                1            The Early Warning interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 278
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                             WDT – Watchdog Timer

20.8.5         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x05
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         7             6            5             4             3            2             1                0
                                                                                                                    EW
   Access                                                                                                          R/W
    Reset                                                                                                               0


               Bit 0 – EW Early Warning Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit sets the Early Warning Interrupt Enable bit, which enables the Early Warning
               interrupt.
                Value        Description
                0            The Early Warning interrupt is disabled.
                1            The Early Warning interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 279
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         WDT – Watchdog Timer

20.8.6         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x06
               Reset:      0x00
               Property:   N/A


         Bit        7             6           5            4            3            2            1               0
                                                                                                              EW
   Access                                                                                                     R/W
    Reset                                                                                                         0


               Bit 0 – EW Early Warning
               This flag is cleared by writing a '1' to it.
               This flag is set when an Early Warning interrupt occurs, as defined by the EWOFFSET bit group in
               EWCTRL.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Early Warning interrupt flag.




           © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 280
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                           WDT – Watchdog Timer

20.8.7         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x08
               Reset:      0x00000000
               Property:   -


         Bit        31           30           29          28           27            26          25          24


   Access
    Reset


         Bit        23           22           21          20           19            18          17          16


   Access
    Reset


         Bit        15           14           13          12           11            10          9           8


   Access
    Reset


         Bit        7             6           5            4            3             2          1           0
                                                         CLEAR     ALWAYSON          WEN       ENABLE
   Access                                                  R            R             R          R
    Reset                                                  0            0             0          0


               Bit 4 – CLEAR Clear Synchronization Busy
               Value      Description
               0          Write synchronization of the CLEAR register is complete.
               1          Write synchronization of the CLEAR register is ongoing.

               Bit 3 – ALWAYSON Always-On Synchronization Busy
               Value      Description
               0          Write synchronization of the CTRLA.ALWAYSON bit is complete.
               1          Write synchronization of the CTRLA.ALWAYSON bit is ongoing.

               Bit 2 – WEN Window Enable Synchronization Busy
               Value      Description
               0          Write synchronization of the CTRLA.WEN bit is complete.
               1          Write synchronization of the CTRLA.WEN bit is ongoing.

               Bit 1 – ENABLE Enable Synchronization Busy
               Value      Description
               0          Write synchronization of the CTRLA.ENABLE bit is complete.
               1          Write synchronization of the CTRLA.ENABLE bit is ongoing.




           © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 281
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                           WDT – Watchdog Timer

20.8.8         Clear

               Name:       CLEAR
               Offset:     0x0C
               Reset:      0x00
               Property:   Write-Synchronized


         Bit           7          6             5           4                3         2            1            0
                                                                CLEAR[7:0]
   Access              W         W             W            W                W        W             W            W
    Reset              0          0             0           0                0         0            0            0


               Bits 7:0 – CLEAR[7:0] Watchdog Clear
               In Normal mode, writing 0xA5 to this register during the watchdog time-out period will clear the Watchdog
               Timer and the watchdog time-out period is restarted.
               In Window mode, any writing attempt to this register before the time-out period started (i.e., during
               TOWDTW) will issue an immediate system Reset. Writing 0xA5 during the time-out period TOWDT will clear
               the Watchdog Timer and the complete time-out sequence (first TOWDTW then TOWDT) is restarted.
               In both modes, writing any other value than 0xA5 will issue an immediate system Reset.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 282
