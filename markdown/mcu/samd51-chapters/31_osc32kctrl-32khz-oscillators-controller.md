# 29. OSC32KCTRL – 32KHz Oscillators Controller

*Source: `Atmel-SAMD51.pdf`, pages 811-830 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                        OSC32KCTRL – 32KHz Oscillators Controller


29.    OSC32KCTRL – 32KHz Oscillators Controller

29.1   Overview
       The 32KHz Oscillators Controller (OSC32KCTRL) provides a user interface to the 32.768kHz oscillators:
       XOSC32K and OSCULP32K.
       The OSC32KCTRL sub-peripherals can be enabled, disabled, calibrated, and monitored through
       interface registers.
       All sub-peripheral statuses are collected in the Status register (STATUS). They can additionally trigger
       interrupts upon status changes through the INTENSET, INTENCLR, and INTFLAG registers.



29.2   Features
         • 32.768kHz Crystal Oscillator (XOSC32K)
             – Programmable start-up time
             – Crystal or external input clock on XIN32 I/O
             – Clock failure detection with safe clock switch
             – Clock failure event output
         • 32.768kHz Ultra Low-Power Internal Oscillator (OSCULP32K)
             – Ultra low-power, always-on oscillator
             – Frequency fine tuning
         • Calibration value loaded from Flash factory calibration at Reset
         • 1.024 kHz clock outputs available




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 811
                                                            SAM D5x/E5x Family Data Sheet
                                                            OSC32KCTRL – 32KHz Oscillators Controller


29.3     Block Diagram
             XOUT32        XIN32
                                            OSC32KCTRL

                                                     32K OSCILLATORS
                                                         CONTROL
                                                                                                CFD Event
                                                        CFD
                                                        CFD
                                                                                                CLK_XOSC32K
                 XOSC32K

                                                                                                CLK_RTC




                                                                          RTCCTRL

                                                                                                CLK_OSCULP32K
               OSCULP32K



                                                      STATUS


                                                   INTERRUPTS                                   Interrupts




29.4     Signal Description
          Signal                   Description       Type
          XIN32                    Analog Input      32.768 kHz Crystal Oscillator or external clock input
          XOUT32                   Analog Output     32.768 kHz Crystal Oscillator output

         The I/O lines are automatically selected when XOSC32K is enabled.
         Note: The signal of the external crystal oscillator may affect the jitter of neighboring pads.



29.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

29.5.1   I/O Lines
         I/O lines are configured by OSC32KCTRL when XOSC32K is enabled, and need no user configuration.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 812
                                                            SAM D5x/E5x Family Data Sheet
                                                           OSC32KCTRL – 32KHz Oscillators Controller

29.5.2   Power Management
         The OSC32KCTRL will continue to operate in any sleep mode where a 32KHz oscillator is running as
         source clock. The OSC32KCTRL interrupts can be used to wake up the device from sleep modes.
         Related Links
         18. PM – Power Manager

29.5.3   Clocks
         The OSC32KCTRL gathers controls for all 32KHz oscillators and provides clock sources to the Generic
         Clock Controller (GCLK), Real-Time Counter (RTC), and Watchdog Timer (WDT).
         The available clock sources are: XOSC32K and OSCULP32K.
         The OSC32KCTRL bus clock (CLK_OSC32KCTRL_APB) can be enabled and disabled in the Main Clock
         module (MCLK).

29.5.4   Interrupts
         The interrupt request lines are connected to the interrupt controller. Using the OSC32KCTRL interrupts
         requires the interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

29.5.5   Events
         The events of this peripheral are connected to the Event System.
         Related Links
         31. EVSYS – Event System

29.5.6   Debug Operation
         When the CPU is halted in debug mode, OSC32KCTRL will continue normal operation. If OSC32KCTRL
         is configured in a way that requires it to be periodically serviced by the CPU through interrupts or similar,
         improper operation or data loss may result during debugging.

29.5.7   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Flag Status and Clear (INTFLAG) register
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller

29.5.8   Analog Connections
         The external 32.768kHz crystal must be connected between the XIN32 and XOUT32 pins, along with any
         required load capacitors. For details on recommended oscillator characteristics and capacitor load, refer
         to the related links.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 813
                                                               SAM D5x/E5x Family Data Sheet
                                                              OSC32KCTRL – 32KHz Oscillators Controller


29.6     Functional Description

29.6.1   Principle of Operation
         XOSC32K and OSCULP32K are configured via OSC32KCTRL control registers. Through this interface,
         the sub-peripherals are enabled, disabled, or have their calibration values updated.
         The STATUS register gathers different status signals coming from the sub-peripherals of OSC32KCTRL.
         The status signals can be used to generate system interrupts, and in some cases wake up the system
         from standby mode, provided the corresponding interrupt is enabled.

29.6.2   32 kHz External Crystal Oscillator (XOSC32K) Operation
         The XOSC32K can operate in two different modes:
           • External clock, with an external clock signal connected to XIN32
           • Crystal oscillator, with an external 32.768 kHz crystal connected between XIN32 and XOUT32
         At reset, the XOSC32K is disabled, and the XIN32/XOUT32 pins can either be used as General Purpose
         I/O (GPIO) pins or by other peripherals in the system.
         When XOSC32K is enabled, the operating mode determines the GPIO usage. When in crystal oscillator
         mode, the XIN32 and XOUT32 pins are controlled by the OSC32KCTRL, and GPIO functions are
         overridden on both pins. When in external clock mode, only the XIN32 pin will be overridden and
         controlled by the OSC32KCTRL, while the XOUT32 pin can still be used as a GPIO pin.

          Enabling,              The XOSC32K is enabled by writing a '1' to the Enable bit in the 32 kHz External
          Disabling              Crystal Oscillator Control register (XOSC32K.ENABLE = 1).
                                 The XOSC32K is disabled by writing a '0' to the Enable bit in the 32 kHz External
                                 Crystal Oscillator Control register (XOSC32K.ENABLE = 0).
          Mode Selection         To enable the XOSC32K in Crystal Oscillator mode, the XTALEN bit in the 32 kHz
                                 External Crystal Oscillator Control register must be written (XOSC32K.XTALEN = 1).
                                 If XOSC32K.XTALEN is '0', the External Clock Input mode will be enabled.
          Gain Selection         When a crystal oscillator is selected, a controllable gain is provided. Writing to the
                                 Control Gain Mode bit field (XOSC32K.CGM) will select a gain setting appropriate
                                 for the desired trade-off between low power and high speed.
          32KHz and 1KHz The XOSC32K 32.768 kHz output is enabled by setting the 32 kHz Output Enable
          Output         bit in the 32 kHz External Crystal Oscillator Control register (XOSC32K.EN32K=1).
                         The XOSC32K also has a 1.024 kHz clock output. This is enabled by setting the 1
                         kHz Output Enable bit in the 32 kHz External Crystal Oscillator Control register
                         (XOSC32K.EN1K = 1).
          Configuration          It is also possible to lock the XOSC32K configuration by setting the Write Lock bit in
          Lock                   the 32 kHz External Crystal Oscillator Control register (XOSC32K.WRTLOCK=1). If
                                 set, the XOSC32K configuration is locked until a Power-On Reset (POR) is
                                 detected.

         The XOSC32K will behave differently in different sleep modes based on the settings of
         XOSC32K.RUNSTDBY, XOSC32K.ONDEMAND, and XOSC32K.ENABLE. If XOSC32KCTRL.ENABLE =
         0, the XOSC32K will be always stopped. For XOS32KCTRL.ENABLE = 1, this table is valid:




         © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 814
                                                            SAM D5x/E5x Family Data Sheet
                                                           OSC32KCTRL – 32KHz Oscillators Controller

         Table 29-1. XOSC32K Sleep Behavior

          CPU Mode                      XOSC32K.          XOSC32K.          Sleep Behavior of XOSC32K and CFD
                                       RUNSTDBY          ONDEMAND
          Active or Idle                    -                  0            Always run
          Active or Idle                    -                  1            Run if requested by peripheral
          Standby                           1                  0            Always run
          Standby                           1                  1            Run if requested by peripheral
          Standby                           0                   -           Run if requested by peripheral

         As a crystal oscillator usually requires a very long start-up time, the 32KHz External Crystal Oscillator will
         keep running across resets when XOSC32K.ONDEMAND=0, except for power-on reset (POR). After a
         reset or when waking up from a sleep mode where the XOSC32K was disabled, the XOSC32K will need
         a certain amount of time to stabilize on the correct frequency. This start-up time can be configured by
         changing the Oscillator Start-Up Time bit group (XOSC32K.STARTUP) in the 32 kHz External Crystal
         Oscillator Control register. During the start-up time, the oscillator output is masked to ensure that no
         unstable clock propagates to the digital logic.
         Once the external clock or crystal oscillator is stable and ready to be used as a clock source, the
         XOSC32K Ready bit in the Status register is set (STATUS.XOSC32KRDY=1). The transition of
         STATUS.XOSC32KRDY from '0' to '1' generates an interrupt if the XOSC32K Ready bit in the Interrupt
         Enable Set register is set (INTENSET.XOSC32KRDY=1).
         The XOSC32K can be used as a source for Generic Clock Generators (GCLK) or for the Real-Time
         Counter (RTC). Before enabling the GCLK or the RTC module, the corresponding oscillator output must
         be enabled (XOSC32K.EN32K or XOSC32K.EN1K) in order to ensure proper operation. In the same way,
         the GCLK or RTC modules must be disabled before the clock selection is changed. For details on RTC
         clock configuration, refer also to 29.6.6 Real-Time Counter Clock Selection.
         Related Links
         14. GCLK - Generic Clock Controller
         21. RTC – Real-Time Counter

29.6.3   Clock Failure Detection Operation
         The Clock Failure Detector (CFD) allows the user to monitor the external clock or crystal oscillator signal
         provided by the external oscillator (XOSC32K). The CFD detects failing operation of the XOSC32K clock
         with reduced latency, and allows to switch to a safe clock source in case of clock failure. The user can
         also switch from the safe clock back to XOSC32K in case of recovery. The safe clock is derived from the
         OSCULP32K oscillator with a configurable prescaler. This allows to configure the safe clock in order to
         fulfill the operative conditions of the microcontroller.
         In sleep modes, CFD operation is automatically disabled when the external oscillator is not requested to
         run by a peripheral. See the Sleep Behavior table above when this is the case.
         The user interface registers allow to enable, disable, and configure the CFD. The Status register provides
         status flags on failure and clock switch conditions. The CFD can optionally trigger an interrupt or an event
         when a failure is detected.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 815
                                                  SAM D5x/E5x Family Data Sheet
                                                  OSC32KCTRL – 32KHz Oscillators Controller

Clock Failure Detection
The CFD is reset only at power-on (POR). The CFD does not monitor the XOSC32K clock when the
oscillator is disabled (XOSC32K.ENABLE=0).
Before starting CFD operation, the user must start and enable the safe clock source (OSCULP32K
oscillator).
CFD operation is started by writing a '1' to the CFD Enable bit in the External Oscillator Control register
(CFDCTRL.CFDEN). After starting or restarting the XOSC32K, the CFD does not detect failure until the
start-up time has elapsed. The start-up time is configured by the Oscillator Start-Up Time in the External
Multipurpose Crystal Oscillator Control register (XOSC32K.STARTUP). Once the XOSC32K Start-Up
Time is elapsed, the XOSC32K clock is constantly monitored.
During a period of 4 safe clocks (monitor period), the CFD watches for a clock activity from the
XOSC32K. There must be at least one rising and one falling XOSC32K clock edge during 4 safe clock
periods to meet non-failure conditions. If no or insufficient activity is detected, the failure status is
asserted: The Clock Failure Detector status bit in the Status register (STATUS.XOSC32KFAIL) and the
Clock Failure Detector interrupt flag bit in the Interrupt Flag register (INTFLAG.XOSC32KFAIL) are set. If
the XOSC32KFAIL bit in the Interrupt Enable Set register (INTENSET.XOSC32KFAIL) is set, an interrupt
is generated as well. If the Event Output enable bit in the Event Control register (EVCTRL.CFDEO) is set,
an output event is generated, too.
After a clock failure was issued the monitoring of the XOSC32K clock is continued, and the Clock Failure
Detector status bit in the Status register (STATUS.XOSC32KFAIL) reflects the current XOSC32K activity.

Clock Switch
When a clock failure is detected, the XOSC32K clock is replaced by the safe clock in order to maintain an
active clock during the XOSC32K clock failure. The safe clock source is the OSCULP32K oscillator clock.
Both 32KHz and 1KHz outputs of the XOSC32K are replaced by the respective OSCULP32K 32KHz and
1KHz outputs. The safe clock source can be scaled down by a configurable prescaler to ensure that the
safe clock frequency does not exceed the operating conditions selected by the application. When the
XOSC32K clock is switched to the safe clock, the Clock Switch bit in the Status register
(STATUS.XOSC32KSW) is set.
When the CFD has switched to the safe clock, the XOSC32K is not disabled. If desired, the application
must take the necessary actions to disable the oscillator. The application must also take the necessary
actions to configure the system clocks to continue normal operations. In the case the application can
recover the XOSC32K, the application can switch back to the XOSC32K clock by writing a '1' to Switch
Back Enable bit in the Clock Failure Control register (CFDCTRL.SWBACK). Once the XOSC32K clock is
switched back, the Switch Back bit (CFDCTRL.SWBACK) is cleared by hardware.

Prescaler
The CFD has an internal configurable prescaler to generate the safe clock from the OSCULP32K
oscillator. The prescaler size allows to scale down the OSCULP32K oscillator so the safe clock frequency
is not higher than the XOSC32K clock frequency monitored by the CFD. The maximum division factor is
2.
The prescaler is applied on both outputs (32KHz and 1KHz) of the safe clock.

          Example 29-1. Example
          For an external crystal oscillator at 32KHz and the OSCULP32K frequency is 32KHz, the
          XOSC32K.CFDPRESC should be set to 0 for a safe clock of equal frequency.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 816
                                                          SAM D5x/E5x Family Data Sheet
                                                         OSC32KCTRL – 32KHz Oscillators Controller

         Event
         If the Event Output Enable bit in the Event Control register (EVCTRL.CFDEO) is set, the CFD clock
         failure will be output on the Event Output. When the CFD is switched to the safe clock, the CFD clock
         failure will not be output on the Event Output.

         Sleep Mode
         The CFD is halted depending on configuration of the XOSC32K and the peripheral clock request. For
         further details, refer to the Sleep Behavior table above. The CFD interrupt can be used to wake up the
         device from sleep modes.

29.6.4   32 kHz Ultra Low-Power Internal Oscillator (OSCULP32K) Operation
         The OSCULP32K provides a tunable, low-speed, and ultra low-power clock source. The OSCULP32K is
         factory-calibrated under typical voltage and temperature conditions.
         The OSCULP32K is enabled by default after a Power-on Reset (POR), and will always run except during
         POR. The frequency of the OSCULP32K Oscillator is controlled by the value in the Calibration bits in the
         32 kHz Ultra Low-Power Internal Oscillator Control register (OSCULP32K.CALIB). This data is used to
         compensate for process variations.
         OSCULP32K.CALIB is automatically loaded from Flash Factory Calibration during start-up. The
         calibration value can be overridden by the user by writing to OSCULP32K.CALIB.
         Users can lock the OSCULP32K configuration by setting the Write Lock bit in the 32 kHz Ultra Low-Power
         Internal Oscillator Control register (OSCULP32K.WRTLOCK = 1). If set, the OSCULP32K configuration is
         locked until POR is detected.
         The OSCULP32K can be used as a source for Generic Clock Generators (GCLK) or for the Real-Time
         Counter (RTC). To ensure proper operation, the GCLK or RTC modules must be disabled before the
         clock selection is changed.
         Related Links
         21. RTC – Real-Time Counter
         29.6.6 Real-Time Counter Clock Selection
         14. GCLK - Generic Clock Controller

29.6.5   Watchdog Timer Clock Selection
         The Watchdog Timer (WDT) uses the internal 1.024kHz OSCULP32K output clock. This clock is running
         all the time and internally enabled when requested by the WDT module.
         Related Links
         20. WDT – Watchdog Timer

29.6.6   Real-Time Counter Clock Selection
         Before enabling the RTC module, the RTC clock must be selected first. All oscillator outputs are valid as
         RTC clock. The selection is done in the RTC Control register (RTCCTRL). To ensure a proper operation,
         it is highly recommended to disable the RTC module first, before the RTC clock source selection is
         changed.
         Related Links
         21. RTC – Real-Time Counter

29.6.7   Interrupts
         The OSC32KCTRL has the following interrupt sources:




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 817
                                                            SAM D5x/E5x Family Data Sheet
                                                           OSC32KCTRL – 32KHz Oscillators Controller

           • XOSC32KRDY - 32KHz Crystal Oscillator Ready: A 0-to-1 transition on the STATUS.XOSC32KRDY
             bit is detected
           • XOSC32KFAIL - Clock Failure Detector: A 0-to-1 transition on the STATUS.XOSC32KFAIL bit is
             detected
         All these interrupts are synchronous wake-up source.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear register (INTFLAG) is set when the interrupt condition occurs. Each interrupt can be enabled
         individually by setting the corresponding bit in the Interrupt Enable Set register (INTENSET), and disabled
         by setting the corresponding bit in the Interrupt Enable Clear register (INTENCLR). An interrupt request is
         generated when the interrupt flag is set and the corresponding interrupt is enabled. The interrupt request
         remains active until the interrupt flag is cleared, the interrupt is disabled or the OSC32KCTRL is reset.
         See the INTFLAG register for details on how to clear interrupt flags.
         The OSC32KCTRL has one common interrupt request line for all the interrupt sources. The user must
         read the INTFLAG register to determine which interrupt condition is present. Refer to the INTFLAG
         register for details.
         Note: Interrupts must be globally enabled for interrupt requests to be generated.
         Related Links
         18. PM – Power Manager
         10.2 Nested Vector Interrupt Controller

29.6.8   Events
         The CFD can generate the following output event:
          • Clock Failure Detector (XOSC32KFAIL): Generated when the Clock Failure Detector status bit is set
             in the Status register (STATUS.XOSC32KFAIL). The CFD event is not generated when the Clock
             Switch bit (STATUS.SWBACK) in the Status register is set.
         Writing a '1' to an Event Output bit in the Event Control register (EVCTRL.CFDEO) enables the CFD
         output event. Writing a '0' to this bit disables the CFD output event. Refer to the Event System chapter for
         details on configuring the event system.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 818
                                                               SAM D5x/E5x Family Data Sheet
                                                               OSC32KCTRL – 32KHz Oscillators Controller


29.7      Register Summary

 Offset        Name        Bit Pos.

                                                                                         XOSC32KFAI                  XOSC32KRD
                              7:0
                                                                                                L                        Y
 0x00        INTENCLR        15:8
                             23:16
                             31:24
                                                                                         XOSC32KFAI                  XOSC32KRD
                              7:0
                                                                                                L                        Y
 0x04        INTENSET        15:8
                             23:16
                             31:24
                                                                                         XOSC32KFAI                  XOSC32KRD
                              7:0
                                                                                                L                        Y
 0x08        INTFLAG         15:8
                             23:16
                             31:24
                                                                                         XOSC32KFAI                  XOSC32KRD
                              7:0                                            XOSC32KSW
                                                                                                L                        Y
 0x0C         STATUS         15:8
                             23:16
                             31:24
 0x10        RTCCTRL          7:0                                                                     RTCSEL[2:0]
 0x11
   ...       Reserved
 0x13
                              7:0     ONDEMAND RUNSTDBY             EN1K       EN32K      XTALEN        ENABLE
 0x14        XOSC32K
                             15:8                   CGM[1:0]       WRTLOCK                            STARTUP[2:0]
 0x16        CFDCTRL          7:0                                                        CFDPRESC       SWBACK        CFDEN
 0x17         EVCTRL          7:0                                                                                     CFDEO
 0x18
   ...       Reserved
 0x1B
                              7:0                                                           EN1K         EN32K
                             15:8     WRTLOCK                                      CALIB[5:0]
 0x1C       OSCULP32K
                             23:16
                             31:24




29.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
          the 8-bit quarters and 16-bit halves of a 32-bit register and the 8-bit halves of a 16-bit register can be
          accessed directly.
          All registers with write-access can be write-protected optionally by the peripheral access controller (PAC).
          Optional Write-Protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write-




          © 2019 Microchip Technology Inc.                      Datasheet                              DS60001507E-page 819
                                                  SAM D5x/E5x Family Data Sheet
                                                 OSC32KCTRL – 32KHz Oscillators Controller

Protection" property in the register description. Write-protection does not apply to accesses through an
external debugger.
Related Links
27. PAC - Peripheral Access Controller




© 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 820
                                                                  SAM D5x/E5x Family Data Sheet
                                                                  OSC32KCTRL – 32KHz Oscillators Controller

29.8.1         Interrupt Enable Clear

               Name:       INTENCLR
               Offset:     0x00
               Reset:      0x00000000
               Property:   PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit        31            30           29            28           27            26           25            24


   Access
    Reset


         Bit        23            22           21            20           19            18           17            16


   Access
    Reset


         Bit        15            14           13            12           11            10            9            8


   Access
    Reset


         Bit         7            6             5            4             3            2             1            0
                                                                                   XOSC32KFAIL                XOSC32KRDY
   Access                                                                              R/W                        R/W
    Reset                                                                               0                          0


               Bit 2 – XOSC32KFAIL XOSC32K Clock Failure Detector Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the XOSC32K Clock Failure Interrupt Enable bit, which disables the
               XOSC32K Clock Failure interrupt.
               Value         Description
               0             The XOSC32K Clock Failure Detection is disabled.
               1             The XOSC32K Clock Failure Detection is enabled. An interrupt request will be generated
                             when the XOSC32K Clock Failure Detection interrupt flag is set.

               Bit 0 – XOSC32KRDY XOSC32K Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the XOSC32K Ready Interrupt Enable bit, which disables the XOSC32K
               Ready interrupt.
               Value         Description
               0             The XOSC32K Ready interrupt is disabled.
               1             The XOSC32K Ready interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 821
                                                                 SAM D5x/E5x Family Data Sheet
                                                                 OSC32KCTRL – 32KHz Oscillators Controller

29.8.2         Interrupt Enable Set

               Name:       INTENSET
               Offset:     0x04
               Reset:      0x00000000
               Property:   PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

         Bit        31            30           29           28            27           26           25            24


   Access
    Reset


         Bit        23            22           21           20            19           18           17            16


   Access
    Reset


         Bit        15            14           13           12            11           10            9            8


   Access
    Reset


         Bit         7            6            5             4            3            2             1            0
                                                                                  XOSC32KFAIL                XOSC32KRDY
   Access                                                                             R/W                        R/W
    Reset                                                                              0                          0


               Bit 2 – XOSC32KFAIL XOSC32K Clock Failure Detector Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the XOSC32K Clock Failure Interrupt Enable bit, which enables the
               XOSC32K Clock Failure interrupt.
               Value         Description
               0             The XOSC32K Clock Failure Detection is disabled.
               1             The XOSC32K Clock Failure Detection is enabled. An interrupt request will be generated
                             when the XOSC32K Clock Failure Detection interrupt flag is set.

               Bit 0 – XOSC32KRDY XOSC32K Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the XOSC32K Ready Interrupt Enable bit, which enables the XOSC32K
               Ready interrupt.
               Value         Description
               0             The XOSC32K Ready interrupt is disabled.
               1             The XOSC32K Ready interrupt is enabled.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 822
                                                                SAM D5x/E5x Family Data Sheet
                                                                OSC32KCTRL – 32KHz Oscillators Controller

29.8.3         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x08
               Reset:      0x00000000
               Property:   –


         Bit        31           30           29           28           27           26           25           24


   Access
    Reset


         Bit        23           22           21           20           19           18           17           16


   Access
    Reset


         Bit        15           14           13           12           11           10           9            8


   Access
    Reset


         Bit        7             6           5            4            3            2            1            0
                                                                                XOSC32KFAIL               XOSC32KRDY
   Access                                                                           R/W                       R/W
    Reset                                                                            0                         0


               Bit 2 – XOSC32KFAIL XOSC32K Clock Failure Detector
               This flag is cleared by writing a '1' to it.
               This flag is set on a zero-to-one transition of the XOSC32K Clock Failure Detection bit in the Status
               register (STATUS.XOSC32KFAIL) and will generate an interrupt request if INTENSET.XOSC32KFAIL is
               '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the XOSC32K Clock Failure Detection flag.

               Bit 0 – XOSC32KRDY XOSC32K Ready
               This flag is cleared by writing a '1' to it.
               This flag is set by a zero-to-one transition of the XOSC32K Ready bit in the Status register
               (STATUS.XOSC32KRDY), and will generate an interrupt request if INTENSET.XOSC32KRDY=1.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the XOSC32K Ready interrupt flag.




           © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 823
                                                                SAM D5x/E5x Family Data Sheet
                                                                OSC32KCTRL – 32KHz Oscillators Controller

29.8.4         Status

               Name:       STATUS
               Offset:     0x0C
               Reset:      0x00000000
               Property:   –


         Bit        31           30           29           28           27           26    25          24


   Access
    Reset


         Bit        23           22           21           20           19           18    17          16


   Access
    Reset


         Bit        15           14           13           12           11           10    9           8


   Access
    Reset


         Bit        7             6           5            4            3             2    1           0
                                                                   XOSC32KSW XOSC32KFAIL          XOSC32KRDY
   Access                                                               R             R                R
    Reset                                                               0             0                0


               Bit 3 – XOSC32KSW XOSC32K Clock Switch
               Value      Description
               0          XOSC32K is not switched and provided the crystal oscillator.
               1          XOSC32K is switched to be provided by the safe clock.

               Bit 2 – XOSC32KFAIL XOSC32K Clock Failure Detector
               Value      Description
               0          XOSC32K is passing failure detection.
               1          XOSC32K is not passing failure detection.

               Bit 0 – XOSC32KRDY XOSC32K Ready
               Value      Description
               0          XOSC32K is not ready.
               1          XOSC32K is stable and ready to be used as a clock source.




           © 2019 Microchip Technology Inc.                      Datasheet                 DS60001507E-page 824
                                                                SAM D5x/E5x Family Data Sheet
                                                                OSC32KCTRL – 32KHz Oscillators Controller

29.8.5         RTC Clock Selection Control

               Name:       RTCCTRL
               Offset:     0x10
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6            5            4             3            2             1            0
                                                                                                 RTCSEL[2:0]
   Access                                                                             R/W           R/W          R/W
    Reset                                                                              0             0            0


               Bits 2:0 – RTCSEL[2:0] RTC Clock Selection
               These bits select the source for the RTC.
                Value      Name               Description
                0x0        ULP1K              1.024kHz from 32KHz internal ULP oscillator
                0x1        ULP32K             32.768kHz from 32KHz internal ULP oscillator
                0x2,       Reserved           -
                0x3
                0x4        XOSC1K             1.024kHz from 32KHz external oscillator
                0x5        XOSC32K            32.768kHz from 32KHz external crystal oscillator
                0x6        Reserved
                0x7        Reserved




           © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 825
                                                                        SAM D5x/E5x Family Data Sheet
                                                                    OSC32KCTRL – 32KHz Oscillators Controller

29.8.6         32KHz External Crystal Oscillator (XOSC32K) Control

               Name:        XOSC32K
               Offset:      0x14
               Reset:       0x2080
               Property:    PAC Write-Protection


         Bit         15              14              13        12             11        10              9           8
                                          CGM[1:0]         WRTLOCK                               STARTUP[2:0]
   Access                         R/W                R/W      R/W                       R/W            R/W         R/W
    Reset                            0                1         0                        0              0           0


         Bit          7              6                5         4                3       2              1           0
                ONDEMAND      RUNSTDBY                        EN1K          EN32K    XTALEN        ENABLE
   Access            R/W          R/W                         R/W            R/W        R/W            R/W
    Reset             1              0                          0                0       0              0


               Bits 14:13 – CGM[1:0] Control Gain Mode
               These bits control the gain of the external crystal oscillator.
                Value      Name                        Description
                0x1        XT                          Standard mode
                0x2        HS                          High Speed mode

               Bit 12 – WRTLOCK Write Lock
               This bit locks the XOSC32K register for future writes, effectively freezing the XOSC32K configuration.
                Value       Description
                0           The XOSC32K configuration is not locked.
                1           The XOSC32K configuration is locked.

               Bits 10:8 – STARTUP[2:0] Oscillator Start-Up Time
               These bits select the start-up time for the oscillator.
               The OSCULP32K oscillator is used to clock the start-up counter.
               Table 29-2. Start-Up Time for 32KHz External Crystal Oscillator

               STARTUP[2:0] Number of OSCULP32K                     Number of XOSC32K         Approximate Equivalent
                            Clock Cycles                            Clock Cycles              Time
                                                                                              [ms]
               0x0               2048                               3                         62.592
               0x1               4096                               3                         125.092
               0x2               16384                              3                         500.092
               0x3               32768                              3                         1000.0092
               0x4               65536                              3                         2000.0092
               0x5               131072                             3                         4000.0092
               0x6               262144                             3                         8000.0092
               0x7               -                                  -                         Reserved




           © 2019 Microchip Technology Inc.                             Datasheet                       DS60001507E-page 826
                                                  SAM D5x/E5x Family Data Sheet
                                                  OSC32KCTRL – 32KHz Oscillators Controller

Note:
 1. Actual Start-Up time is 1 OSCULP32K cycle + 3 XOSC32K cycles.
 2. The given time assumes an XTAL frequency of 32.768kHz.

Bit 7 – ONDEMAND On Demand Control
This bit controls how the XOSC32K behaves when a peripheral clock request is detected. For details,
refer to Table 29-1.

Bit 6 – RUNSTDBY Run in Standby
This bit controls how the XOSC32K behaves during standby sleep mode. For details, refer to Table 29-1.

Bit 4 – EN1K 1KHz Output Enable
Value      Description
0          The 1KHz output is disabled.
1          The 1KHz output is enabled.

Bit 3 – EN32K 32KHz Output Enable
Value      Description
0          The 32KHz output is disabled.
1          The 32KHz output is enabled.

Bit 2 – XTALEN Crystal Oscillator Enable
This bit controls the connections between the I/O pads and the external clock or crystal oscillator.
 Value       Description
 0           External clock connected on XIN32. XOUT32 can be used as general-purpose I/O.
 1           Crystal connected to XIN32/XOUT32.

Bit 1 – ENABLE Oscillator Enable
Value      Description
0          The oscillator is disabled.
1          The oscillator is enabled.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 827
                                                                    SAM D5x/E5x Family Data Sheet
                                                                    OSC32KCTRL – 32KHz Oscillators Controller

29.8.7         Clock Failure Detector Control

               Name:        CFDCTRL
               Offset:      0x16
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7             6            5             4             3            2             1             0
                                                                                     CFDPRESC      SWBACK         CFDEN
   Access                                                                               R/W           R/W          R/W
    Reset                                                                                0             0             0


               Bit 2 – CFDPRESC Clock Failure Detector Prescaler
               This bit selects the prescaler for the Clock Failure Detector.
                Value       Description
                0           The CFD safe clock frequency is the OSCULP32K frequency
                1           The CFD safe clock frequency is the OSCULP32K frequency divided by 2

               Bit 1 – SWBACK Clock Switch Back
               This bit clontrols the XOSC32K output switch back to the external clock or crystal scillator in case of clock
               recovery.
                Value       Description
                0           The clock switch is disabled.
                1           The clock switch is enabled. This bit is reset when the XOSC32K output is switched back to
                            the external clock or crystal oscillator.

               Bit 0 – CFDEN Clock Failure Detector Enable
               This bit selects the Clock Failure Detector state.
                Value       Description
                0           The CFD is disabled.
                1           The CFD is enabled.




           © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 828
                                                                 SAM D5x/E5x Family Data Sheet
                                                                 OSC32KCTRL – 32KHz Oscillators Controller

29.8.8         Event Control

               Name:       EVCTRL
               Offset:     0x17
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6            5             4            3            2             1               0
                                                                                                                   CFDEO
   Access                                                                                                           R/W
    Reset                                                                                                            0


               Bit 0 – CFDEO Clock Failure Detector Event Out Enable
               This bit controls whether the Clock Failure Detector event output is enabled and an event will be
               generated when the CFD detects a clock failure.
                Value       Description
                0           Clock Failure Detector Event output is disabled, no event will be generated.
                1           Clock Failure Detector Event output is enabled, an event will be generated.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 829
                                                                  SAM D5x/E5x Family Data Sheet
                                                                  OSC32KCTRL – 32KHz Oscillators Controller

29.8.9         32KHz Ultra Low Power Internal Oscillator (OSCULP32K) Control

               Name:       OSCULP32K
               Offset:     0x1C
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31            30           29           28            27                 26     25           24


   Access
    Reset


         Bit        23            22           21           20            19                 18     17           16


   Access
    Reset


         Bit        15            14           13           12            11                 10      9           8
                 WRTLOCK                                                        CALIB[5:0]
   Access          R/W                        R/W           R/W           R/W                R/W   R/W          R/W
    Reset            0                          0            0             0                  0      0           x


         Bit         7            6             5            4             3                  2      1           0
                                                                                         EN1K      EN32K
   Access                                                                                    R/W   R/W
    Reset                                                                                     1      1


               Bit 15 – WRTLOCK Write Lock
               This bit locks the OSCULP32K register for future writes to fix the OSCULP32K configuration.
                Value       Description
                0           The OSCULP32K configuration is not locked.
                1           The OSCULP32K configuration is locked.

               Bits 13:8 – CALIB[5:0] Oscillator Calibration
               These bits control the oscillator calibration.
               These bits are loaded from Flash Calibration at startup.

               Bit 2 – EN1K 1kHz Output Enable
               Value      Description
               0          The 1kHz output is disabled
               1          The 1kHz output is enabled.

               Bit 1 – EN32K
               Value      Description
               0          The 32kHz output is disabled.
               1          The 32kHz output is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 830
