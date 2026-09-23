# 28. OSCCTRL – Oscillators Controller

*Source: `Atmel-SAMD51.pdf`, pages 763-810 — SAMD51 family datasheet*

                                                           SAM D5x/E5x Family Data Sheet
                                                                         OSCCTRL – Oscillators Controller


28.    OSCCTRL – Oscillators Controller

28.1   Overview
       The Oscillators Controller (OSCCTRL) provides a user interface to the XOSCn, DFLL48M, and two
       FDPLL200M.
       Through the interface registers, it is possible to enable, disable, calibrate, and monitor the oscillators.
       The status of all oscillators are collected in the Status register (STATUS). They can additionally trigger
       interrupts upon status changes via the INTENSET, INTENCLR, and INTFLAG registers.



28.2   Features
         • Digital Frequency-Locked Loop (DFLL48M)
            – Internal oscillator with no external components
            – 48 MHz output frequency
            – Operates stand-alone as a high-frequency programmable oscillator in Open Loop mode
            – Operates as an accurate frequency multiplier against a known frequency in Closed Loop mode
         • Two 8-48 MHz Crystal Oscillators (XOSCn)
            – Tunable gain control
            – Programmable start-up time
            – Crystal or external input clock on XIN I/O
            – Clock failure detection with safe clock switch
            – Clock failure event output
         • Two Digital Phase-Locked Loop (DPLLn)
            – 96 MHz to 200 MHz output frequency from a 32 kHz to 3.2 MHz reference clock
            – Two DPLLs, each with four selectable reference clocks
            – Adjustable digital filter for jitter optimization
            – Adjustable DCO filter for a 4-stages differential ring oscillator
            – Fractional part used to achieve 1/32th of reference clock step
            – Embedded test mode controller




       © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 763
                                                                SAM D5x/E5x Family Data Sheet
                                                                                  OSCCTRL – Oscillators Controller


28.3     Block Diagram
         Figure 28-1. OSCCTRL Block Diagram
                                                                        XOUT[1:0] XIN[1:0]


                                                  OSCCTRL                     2        2


                                                                                             CFD Event0
                                      CLK_XOSC0                              XOSC     CFD


                                                                                             CFD Event1
                                      CLK_XOSC1                              XOSC     CFD

                                                      OSCILLATORS
                                                       CONTROL
                                    CLK_DFLL48M                             DFLL48M


                                      CLK_DPLL0                           FDPLL200M


                                      CLK_DPLL1                           FDPLL200M




                                                                            STATUS


                                                                          INTERRUPTS           Interrupts
                                                                          GENERATOR




28.4     Signal Description
          Signal          Description                                                                         Type
          XIN[1:0]        Multipurpose Crystal Oscillator or external clock generator input                   Analog input
          XOUT[1:0]       Multipurpose Crystal Oscillator output                                              Analog output

         The I/O lines are automatically selected when XOSCn is enabled.


28.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

28.5.1   I/O Lines
         I/O lines are configured by OSCCTRL when XOSCn is enabled, and need no user configuration.

28.5.2   Power Management
         The OSCCTRL can continue to operate in any sleep mode where the selected source clock is running.
         The OSCCTRL interrupts can be used to wake up the device from sleep modes. The events can trigger
         other operations in the system without exiting sleep modes.
         Related Links
         18. PM – Power Manager

28.5.3   Clocks
         The OSCCTRL gathers controls for all device oscillators and provides clock sources to the Generic Clock
         Controller (GCLK). The available clock sources are: XOSCn, DFLL48M, and FDPLL200Mn.




         © 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 764
                                                           SAM D5x/E5x Family Data Sheet
                                                                         OSCCTRL – Oscillators Controller

         The DFLL48M requires a reference clock (GCLK_DFLL48M_REF) from the GCLK. The control logic uses
         the oscillator output, which is also asynchronous to the user interface clock (CLK_OSCCTRL_APB). Due
         to this asynchronicity, writes to certain registers will require synchronization between the clock domains.
         Refer to Synchronization for further details.
         The FDPLL200Mn require a reference clock (GCLK_DPLL) for the FDPLL output. When the optional lock
         timer timeout function is used, a 32KHz reference clock (GCLK_DPLL_32K) is also required. Both
         reference clocks can either stem from the GCLK and/or from external oscillators.

28.5.4   DMA
         Not applicable.

28.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. Using the OSCCTRL interrupts requires
         the interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

28.5.6   Events
         The events of this peripheral are connected to the Event System.
         Related Links
         31. EVSYS – Event System

28.5.7   Debug Operation
         When the CPU is halted in debug mode the OSCCTRL continues normal operation. If the OSCCTRL is
         configured in a way that requires it to be periodically serviced by the CPU through interrupts or similar,
         improper operation or data loss may result during debugging.

28.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Flag Status and Clear register (INTFLAG)
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

28.5.9   Analog Connections
         The 8-48 MHz crystal must be connected between the XIN and XOUT pins, along with any required load
         capacitors.
         Note: Refer to the Electrical Characteristics for more information about load capacitors.



28.6     Functional Description

28.6.1   Principle of Operation
         XOSC, DFLL48M, and DPLL200M are configured via OSCCTRL control registers. Through this interface,
         the oscillators are enabled, disabled, or have their calibration values updated.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 765
                                                             SAM D5x/E5x Family Data Sheet
                                                                         OSCCTRL – Oscillators Controller

         The Status register gathers different status signals coming from the oscillators controlled by the
         OSCCTRL. The status signals can be used to generate system interrupts, and in some cases wake up
         the system from Sleep mode, provided the corresponding interrupt is enabled.

28.6.2   External Multipurpose Crystal Oscillator (XOSCn) Operation
         The XOSCn can operate in two different modes:
           • External clock, with an external clock signal connected to the XIN pin
           • Crystal oscillator, with an external 8-48 MHz crystal
         The XOSCn can be used as a clock source for generic clock generators. This is configured by the
         Generic Clock Controller.
         At reset, the XOSCn is disabled, and the XINn/XOUTn pins can be used as General Purpose I/O (GPIO)
         pins or by other peripherals in the system. When XOSCn is enabled, the operating mode determines the
         GPIO usage. When in crystal oscillator mode, the XINn and XOUTn pins are controlled by the OSCCTRL,
         and GPIO functions are overridden on both pins. When in external clock mode, only the XINn pins will be
         overridden and controlled by the OSCCTRL, while the XOUTn pins can still be used as GPIO pins.
         The XOSCn is enabled by writing a '1' to the Enable bit in the External Multipurpose Crystal Oscillator
         Control register (XOSCCTRLn.ENABLE). To enable XOSCn as an external crystal oscillator, the XTAL
         Enable bit (XOSCCTRLn.XTALEN) must written to '1'. If XOSCCTRLn.XTALEN is zero, the external clock
         input on XIN will be enabled.
         When in crystal oscillator mode (XOSCCTRLn.XTALEN=1), the External Multipurpose Crystal Oscillator
         Current Control (XOSCCTRLn.IPTAT, XOSCCTRLn.IMULT) must be set to match the external crystal
         oscillator frequency. If the External Multipurpose Crystal Oscillator Enable Amplitude Loop Control
         (XOSCCTRLn.ENALC) is '1', the oscillator amplitude will be automatically adjusted, and in most cases
         result in lower power consumption.
         The bias current of the Crystal Oscillator can be adjusted to the desired value for a proper oscillation by
         setting the bit fields XOSCCTRLn.IPTAT and XOSCCTRLn.IMULT. See the recommended setting in table
         Table 28-7.
         The low buffer gain is used to adjust the oscillator's amplitude in automatic loop control
         (XOSCCTRLn.ENALC=1). The default value of LOWBUFGAIN=0 should be used to allow operating with
         a low amplitude oscillator. The setting LOWBUFGAIN=1 can be used to to solve stability issues. If set, the
         oscillator's amplitude is increased by a factor of approximately 2.
         The XOSCn will behave differently in different sleep modes, based on the settings of
         XOSCCTRLn.RUNSTDBY, XOSCCTRLn.ONDEMAND, and XOSCCTRLn.ENABLE
         Table 28-1. XOSC Sleep Behavior

           XOSCCTRLn.RUNS             XOSCCTRLn.ONDE XOSCTRLn.ENABL              Sleep Behavior
                TDBY                      MAND       E
                       -                    -            0                       Disabled
                      0                     0            1                       Always run in Idle Sleep modes.
                                                                                 Run in Standby Sleep mode if
                                                                                 requested by a peripheral.
                      0                     1            1                       Only run in Idle or Standby Sleep
                                                                                 modes if requested by a
                                                                                 peripheral.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 766
                                                               SAM D5x/E5x Family Data Sheet
                                                                           OSCCTRL – Oscillators Controller

         ...........continued
           XOSCCTRLn.RUNS             XOSCCTRLn.ONDE XOSCTRLn.ENABL                  Sleep Behavior
                TDBY                      MAND       E
                      1                      0             1                         Always run in Idle and Standby
                                                                                     Sleep modes.
                      1                      1             1                         Only run in Idle or Standby Sleep
                                                                                     modes if requested by a
                                                                                     peripheral.

         After a hard reset, or when waking up from a sleep mode where the XOSCn was disabled, the XOSCn
         will need a certain amount of time to stabilize on the correct frequency. This start-up time can be
         configured by changing the Oscillator Start-Up Time bit group (XOSCCTRLn.STARTUP) in the External
         Multipurpose Crystal Oscillator Control register. During the start-up time, the oscillator output is masked to
         ensure that no unstable clock propagates to the digital logic. The External Multipurpose Crystal Oscillator
         Ready bit in the Status register (STATUS.XOSCRDYn) is set when the external clock or crystal oscillator
         is stable and ready to be used as a clock source. An interrupt is generated on a zero-to-one transition on
         STATUS.XOSCRDYn if the External Multipurpose Crystal Oscillator Ready bit in the Interrupt Enable Set
         register (INTENSET.XOSCRDYn) is set.
         Related Links
         14. GCLK - Generic Clock Controller

28.6.3   Clock Failure Detection Operation
         The Clock Failure Detector (CFD) allows the user to monitor the external clock or crystal oscillator clock
         signal provided by the External Multipurpose Crystal Oscillator (XOSCn). It detects failing operation of the
         XOSCn clock, and allows to switch to a safe clock in case of clock failure. The user can also switch from
         the safe clock to the XOSCn clock in case of clock recovery. The safe clock is derived from the DFLL48M
         with a configurable prescaler. This allows to configure the safe clock in order to fulfill the operative
         conditions of the microcontroller. The CFD operation is automatically suspended when the XOSCn clock
         is not requested in ONDEMAND mode or halted in STANDBY.
         The user interface registers allow to enable, disable and configure the CFD. The Status register gives
         status on failure and clock switch conditions. The Clock Failure Detector can optionally trigger an interrupt
         or an event when a failure is detected.

         Clock Failure Detection
         At reset, the CFD is disabled. The CFD does not monitor the XOSCn clock when the oscillator is disabled
         (XOSCCTRLn.ENABLE = 0).
         Before starting the CFD operation, the user must start and enable the safe clock source (DFLL48M). To
         start the CFD operation, the user must write a one to the CFD Enable bit in the External Oscillator Control
         register (XOSCCTRLn.CFDEN). After the start or restart of the XOSCn, the CFD does not detect failure
         until the start-up time, as configured by the Oscillator Start-Up Time (XOSCCTRLn.STARTUP) in the
         External Multipurpose Crystal Oscillator Control register, is elapsed. Once the XOSCn Start-Up Time is
         elapsed, the XOSCn clock is constantly monitored.
         During a period of 4 safe clocks , the CFD watches for a clock activity from the XOSCn. There must be
         one rising and one falling XOSCn clock edges during a 4 safe clock periods to meet a non failure status.
         If no activity is detected, the failure status is asserted. The Clock Failure status bit in the Status register
         (STATUS.CLKFAILn) is set. The Clock Failure interrupt flag bit in the Interrupt Flag register




         © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 767
                                                          SAM D5x/E5x Family Data Sheet
                                                                        OSCCTRL – Oscillators Controller

         (INTFLAG.CLKFAILn) is set. If the CLKFAILn bit in the Interrupt Enable Set register
         (INTENSET.CLKFAILn) is set, an interrupt is generated . An output event is generated as well, if the
         Event Output enable bit in the Event Control register (EVCTRL.CFDEOn) is set.
         The XOSCn clock continues to be monitored after a clock failure. The Clock Failure status bit in the
         Status register (STATUS.CLKFAILn) reflects the current XOSCn clock activity.

         Clock Switch
         When a clock failure is detected, the XOSCn clock is replaced by the safe clock in order to maintain an
         active clock during the XOSCn clock failure. The safe clock source is the DFLL48M oscillator clock. The
         safe clock source can be downscaled with a configurable prescaler to ensure that the safe clock
         frequency does not exceed the operating conditions selected by the application. When the XOSCn clock
         is switched to the safe clock, the Clock Switch bit (STATUS.CLKSWn) in the Status register is set.
         When the CFD has switched to the safe clock, the XOSCn is not disabled. The application must take the
         necessary actions to disable the oscillator N. The application must also take the necessary actions to
         configure the system clocks to continue normal operations.
         In the case the application can recover the XOSCn , it can switch back to the XOSCn clock by writing a
         one to Switch Back bit (XOSCCTRLn.SWBCK) in the External Oscillator Control register. Once the
         XOSCn clock is switched back, the Switch Back bit (XOSCCTRLn.SWBCK) is cleared by the hardware.

         Prescaler
         The CFD has an internal configurable prescaler (XOSCCTRLn.CFDPRESC) to generate the safe clock
         from the DFLL48M clock. The prescaler size allows to scale down the DFLL48M clock such that the safe
         clock is not higher than the XOSCn clock frequency monitored by the CFD. The frequency divider is
         2^CFDPRESC where CFDPRESC range from 0 to 15.
         Example: for an external crystal oscillator at 8 mHz and the DFLL48M internal oscillator configured to
         generate a 48 mHz clock, the prescaler should select a downscale value above 6 (48/8), eg. 8, thus
         CFDPRESC=3.

         Event
         If the Event Output enable bit in the Event Control register (EVCTRL.CFDEOn) is set, the CFD clock
         failure will be output on the Event Output. When the CFD is switched to the safe clock, the CFD clock
         failure will not be output on the Event Output.

         Sleep Mode
         The CFD is halted depending on configuration of the XOSCn and the peripheral clock request. For further
         details, refer to the Sleep Behavior table above. The CFD interrupt can be used to wake up the device
         from sleep modes.

28.6.4   Digital Frequency Locked Loop (DFLL48M) Operation
         The DFLL48M can operate in both open-loop mode and closed-loop mode. In closed-loop mode, a low-
         frequency clock with high accuracy should be used as the reference clock to get high accuracy on the
         output clock (CLK_DFLL48M).
         The DFLL48M can be used as a source for the generic clock generators.
         Related Links
         14. GCLK - Generic Clock Controller




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 768
                                                          SAM D5x/E5x Family Data Sheet
                                                                        OSCCTRL – Oscillators Controller

28.6.4.1 Basic Operation

        Operating modes
        The DFLL48M will behave differently in different sleep modes based on the settings of
        DFLLCTRLA.RUNSTDBY, DFLLCTRLA.ONDEMAND and DFLLCTRLA.ENABLE, as shown in the
        following table.
        Table 28-2. DFLL48M Sleep Behavior

         DFLLCTRLA.RUNSTD                  DFLLCTRLA.ONDEMA    DFLLCTRLA.ENABLE           Sleep Behavior
         BY                                ND
         -                                 -                   0                          Disabled
         0                                 0                   1                          Always run in Idle Sleep
                                                                                          modes. Run in Standby
                                                                                          Sleep mode if requested
                                                                                          by a peripheral.
         0                                 1                   1                          Only run in Idle or
                                                                                          Standby Sleep modes if
                                                                                          requested by a
                                                                                          peripheral.
         1                                 0                   1                          Always run in Idle and
                                                                                          Standby Sleep modes.
         1                                 1                   1                          Only run in Idle or
                                                                                          Standby Sleep modes if
                                                                                          requested by a
                                                                                          peripheral.

        The DFLL48M is used as a clock source for the generic clock generators, as described in the GCLK
        chapter.
        The DFLL48M is factory-calibrated for 48MHz. Registers DFLLVAL.COARSE and DFLLVAL.FINE store
        frequency calibration after reset.

        Open-Loop Operation
        After any reset, the open-loop mode is selected. When operating in open-loop mode, the output
        frequency of the DFLL48M will be determined by the values written to the DFLL Coarse Value bit group
        and the DFLL Fine Value bit group (DFLLVAL.COARSE and DFLLVAL.FINE) in the DFLL Value register.
        It is possible to change the values of DFLLVAL.COARSE and DFLLVAL.FINE and thereby the output
        frequency of the DFLL48M output clock, CLK_DFLL48M, while the DFLL48M is enabled and in use.
        CLK_DFLL48M is ready to be used when STATUS.DFLLRDY is set after enabling the DFLL48M.

        Closed-Loop Operation
        In closed-loop operation, the output frequency is continuously regulated against a reference clock. Once
        the multiplication factor is set, the oscillator fine tuning is automatically adjusted. The DFLL48M must be
        correctly configured before closed-loop operation can be enabled. After enabling the DFLL48M, it must
        be configured in the following way:




        © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 769
                                                  SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

  1.   Enable and select a reference clock (CLK_DFLL48M_REF). CLK_DFLL48M_REF is Generic Clock
       Channel 0 (DFLL48M_Reference). Refer to GCLK for details.
  2.   Select the maximum step size allowed in finding the Coarse and Fine values by writing the
       appropriate values to the DFLL Coarse Maximum Step and DFLL Fine Maximum Step bit groups
       (DFLLMUL.CSTEP and DFLLMUL. FSTEP) in the DFLL Multiplier register. A small step size will
       ensure low overshoot on the output frequency, but will typically result in longer lock times. A high
       value might give a large overshoot, but will typically provide faster locking. DFLLMUL.CSTEP and
       DFLLMUL.FSTEP should not be higher than 50% of the maximum value of DFLLVAL.COARSE and
       DFLLVAL.FINE, respectively.
  3.   Select the multiplication factor in the DFLL Multiply Factor bit group (DFLLMUL.MUL) in the DFLL
       Multiplier register. Care must be taken when choosing DFLLMUL.MUL so that the output frequency
       does not exceed the maximum frequency of the device. If the target frequency is below the
       minimum frequency of the DFLL48M, the output frequency will be equal to the DFLL minimum
       frequency.
  4.   Start the closed loop mode by writing a one to the DFLL Mode Selection bit (DFLLCTRLA.MODE)
       in the DFLL Control register.
The frequency of CLK_DFLL48M (Fclkdfll48m) is given by:
�clkdfll48m = DFLLMUL.MUL × �clkdfll48mref

where Fclkdfll48mref is the frequency of the reference clock (CLK_DFLL48M_REF). DFLLVAL.COARSE
and DFLLVAL.FINE are read-only in closed-loop mode, and are controlled by the frequency tuner to meet
user specified frequency. In closed-loop mode, the value in DFLLVAL.COARSE is used by the frequency
tuner as a starting point for Coarse. Writing DFLLVAL.COARSE to a value close to the final value before
entering closed-loop mode will reduce the time needed to get a lock on Coarse.

Frequency Locking
The locking of the frequency in closed-loop mode is divided into two stages. In the first, coarse stage, the
control logic quickly finds the correct value for DFLLVAL.COARSE and sets the output frequency to a
value close to the correct frequency. On coarse lock, the DFLL Locked on Coarse Value bit
(STATUS.DFLLLOCKC) in the Status register will be set.
In the second, fine stage, the control logic tunes the value in DFLLVAL.FINE so that the output frequency
is very close to the desired frequency. On fine lock, the DFLL Locked on Fine Value bit
(STATUS.DFLLLOCKF) in the Status register will be set.
If the the ByPass Lock bit (DFLLCTRLB.BPLCKC) in the DFLL Control register is set, the coarse stage is
by-passed, the DFLLVAL.COARSE keeps it’s value and the DFLL Coarse Value bit
(STATUS.DFLLLOCKC) is immediately set.
Interrupts are generated by both STATUS.DFLLLOCKC and STATUS.DFLLLOCKF if
INTENSET.DFLLOCKC or INTENSET.DFLLOCKF are written to '1'.
CLK_DFLL48M is ready to be used when the DFLL Ready bit (STATUS.DFLLRDY) in the Status register
is set, but the accuracy of the output frequency depends on which locks are set. For lock times, refer to
the Electrical Characteristics.

Frequency Error Measurement
The ratio between CLK_DFLL48M_REF and CLK48M_DFLL is measured automatically when the
DFLL48M is in closed loop mode. The difference between this ratio and the value in DFLLMUL.MUL is




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 770
                                                           SAM D5x/E5x Family Data Sheet
                                                                         OSCCTRL – Oscillators Controller

         stored in the DFLL Multiplication Ratio Difference bit group (DFLLVAL.DIFF) in the DFLL Value register.
         The relative error on CLK_DFLL48M compared to the target frequency is calculated as follows:
                    DIFF
         ERROR =
                    MUL

         Drift Compensation
         If the Stable DFLL Frequency bit (DFLLCTRLB.STABLE) in the DFLL Control register is zero, the
         frequency tuner will automatically compensate for drift in the CLK_DFLL48M without losing either of the
         locks. This means that DFLLVAL.FINE can change after every measurement of CLK_DFLL48M. If the
         DFLLVAL.FINE value overflows or underflows due to large drift in temperature and/or voltage, the DFLL
         Out Of Bounds bit (STATUS.DFLLOOB) in the Status register will be set. After an Out of Bounds error
         condition, the user must rewrite DFLLMUL.MUL to ensure correct CLK_DFLL48M frequency. An interrupt
         is generated on a zero-to-one transition on STATUS.DFLLOOB if the DFLL Out Of Bounds bit
         (INTENSET.DFLLOOB) in the Interrupt Enable Set register is set. This interrupt will also be set if the tuner
         is not able to lock on the correct Coarse value. If the Stable DFLL Frequency bit (DFLLCTRLB.STABLE)
         in the DFLL Control register is one, the DFLLVAL.COARSE and DFLLVAL.FINE values will stay constant
         after the lock. The user can check for a possible drift by reading the frequency error in the DFLL
         Multiplication Ratio Difference bit group (DFLLVAL.DIFF).

         Reference Clock Stop Detection
         If CLK_DFLL48M_REF stops or is running at a very low frequency (slower than CLK_DFLL48M/(2 *
         MULMAX)), the DFLL Reference Clock Stopped bit (STATUS.DFLLRCS) in the Status register will be set.
         Detecting a stopped reference clock can take a long time, on the order of 217 CLK_DFLL48M cycles.
         When the reference clock is stopped, the DFLL48M will operate as if in open-loop mode. Closed-loop
         mode operation will automatically resume if the CLK_DFLL48M_REF is restarted. An interrupt is
         generated on a zero-to-one transition on STATUS.DFLLRCS if the DFLL Reference Clock Stopped bit
         (INTENSET.DFLLRCS) in the Interrupt Enable Set register is set.
         Related Links
         9.4 NVM User Page Mapping
         14. GCLK - Generic Clock Controller

28.6.4.2 Additional Features

         Dealing with Delay in the DFLL in Closed-Loop Mode
         The time from selecting a new CLK_DFLL48M frequency until this frequency is output by the DFLL48M
         can be up to several microseconds. If the value in DFLLMUL.MUL is small, this can lead to instability in
         the DFLL48M locking mechanism, which can prevent the DFLL48M from achieving locks. To avoid this, a
         chill cycle, during which the CLK_DFLL48M frequency is not measured, can be enabled. The chill cycle is
         enabled by default, but can be disabled by writing a one to the DFLL Chill Cycle Disable bit
         (DFLLCTRLB.CCDIS) in the DFLL Control register. Enabling chill cycles might double the lock time.
         Another solution to this problem consists of using less strict lock requirements. This is called Quick Lock
         (QL), which is also enabled by default, but it can be disabled by writing a one to the Quick Lock Disable
         bit (DFLLCTRLB.QLDIS) in the DFLL Control register. The Quick Lock might lead to a larger spread in the
         output frequency than chill cycles, but the average output frequency is the same.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 771
                                                            SAM D5x/E5x Family Data Sheet
                                                                          OSCCTRL – Oscillators Controller

         USB Clock Recovery Mode
         USB Clock Recovery mode can be used to create the 48MHz USB clock from the USB Start Of Frame
         (SOF). This mode is enabled by writing a '1' to both the USB Clock Recovery Mode bit and the Mode bit
         in DFLL Control register (DFLLCTRLB.USBCRM and DFLLCTRLB.MODE).
         In USB Clock Recovery mode, the status bits of the DFLL in OSCCTRL.STATUS are determined by the
         USB bus activity, and have no valid meaning. The SOF signal from USB device will be used as reference
         clock (CLK_DFLL_REF), ignoring the selected generic clock reference. When the USB device is
         connected, a SOF will be sent every 1ms, thus DFLLVAL.MUX bits should be written to 0xBB80 to obtain
         a 48MHz clock. In USB clock recovery mode, the DFLLCTRLB.BPLCKC bit state is ignored, and the
         value stored in the DFLLVAL.COARSE will be used as final Coarse value.
         The COARSE value for a calibrated 48 MHz frequency is loaded from NVM after any system reset and
         may vary in operating modes different of the USB Clock Recovery Mode. The initial COARSE value can
         be saved and restored by the software if necessary.
         The locking procedure will also go instantaneously to the fine lock search.
         The DFLLCTRLB.QLDIS bit must be cleared and DFLLCTRLB.CCDIS should be set to speed up the lock
         phase. The DFLLCTRLB.STABLE bit state is ignored, an auto jitter reduction mechanism is used instead.

         Wake from Sleep Modes
         DFLL48M can optionally reset its lock bits when it is disabled. This is configured by the Lose Lock After
         Wake bit (DFLLCTRLB.LLAW) in the DFLL Control register. If DFLLCTRLB.LLAW is zero, the DFLL48M
         will be re-enabled and start running with the same configuration as before being disabled, even if the
         reference clock is not available. The locks will not be lost. Thus it is important that the user checks that
         the DFLL48M has reached the COARSE and FINE lock stage before entering a sleep mode. When the
         reference clock has restarted, the Fine tracking will quickly compensate for any frequency drift during
         sleep if DFLLCTRLB.STABLE is zero. If DFLLCTRLB.LLAW is one when disabling the DFLL48M, the
         DFLL48M will lose all its locks, and needs to regain these through the full lock sequence.

         Wait for Lock
         DFLL48M can optionally control the issued clock. This is configured by the Wait For Lock bit
         (DFLLCTRLB.WAITLOCK) in the DFLL Control register. If DFLLCTRLB.WAITLOCK is zero, the
         DFLL48M will issue a clock immediately after the ready bit (STATUS.DFLLRDY) has risen. If
         DFLLCTRLB.WAITLOCK is one, the DFLL48M will issue a clock immediately after the fine lock bit
         (STATUS.DFLLCKF) has risen. Using the wait for lock feature allows a better accuracy of the issued
         DFLL48M clock, conversely it increases the startup time of the DFLL48M clock.

         Accuracy
         There are two main factors that determine the accuracy of Fclkdfll48m. These can be tuned to obtain
         maximum accuracy when fine lock is achieved.
           • Fine resolution: The frequency step between two Fine values.
           • The accuracy of the reference clock.

28.6.5   Digital Phase Locked Loop (DPLL) Operation
         The task of the DPLL is to maintain coherence between the input (reference) signal and the respective
         output frequency CLK_DPLL through phase comparison. The DPLL controller supports four independent
         sources of reference clocks:
           • XOSC32K: This clock is provided by the 32K External Crystal Oscillator (XOSC32K).




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 772
                                                                          SAM D5x/E5x Family Data Sheet
                                                                                         OSCCTRL – Oscillators Controller

          • XOSC0 and XOSC1: These clocks are provided by the External Multipurpose Crystal Oscillator
            (XOSC).
          • GCLK: This clock is provided by the Generic Clock Controller.
        When the controller is enabled, the relationship between the reference clock frequency and the output
        clock frequency is as shown below:
                                                 LDRFRAC
        �CLK_DPLLn = �CKR × LDR + 1 +
                                                    32
        Where:
        fCLK_DPLLn is the frequency of the DPLL output clock, LDR is the loop divider ratio integer part and
        LDRFRAC is the loop divider ratio fractional part, fCKR is the frequency of the selected reference clock.
        Figure 28-2. DPLL Block Diagram
            XIN32
                          XOSC32K
          XOUT32
                                                                            DPLLCTRLB.FILTER
                                     DPLLCTRLB.DIV
              XIN                                         CKR
                           XOSCn           DIVIDER                  TDC      DIGITAL FILTER    DCO        CG   CLK_DPLL
            XOUT



                                                                                                     CK
                         GCLK_DPLL                                               RATIO


                                                 DPLLCTRLB.REFCLK              DPLLRATIO


        When the controller is disabled, the output clock is low. If the Loop Divider Ratio Fractional part bit field in
        the DPLL Ratio register (DPLLRATIO.LDRFRAC) is zero, the DPLL works in Integer mode. Otherwise,
        the fractional mode is activated. The fractional part has a negative impact on the jitter of the DPLL.

                    For example (Integer mode only): Assuming fCKR = 32 kHz and fCLK_DPLLn = 112 MHz, the
                    multiplication ratio is 3500. It means that LDR must be set to 3499.


                    For example (Fractional mode): Assuming fCKR = 32 kHz and fCLK_DPPLn = 112.003000
                    MHz, the multiplication ratio is 3500.9375 (3500 + 3/32). Thus LDR is set to 3499 and
                    LDRFRAC to 3.

        Related Links
        14. GCLK - Generic Clock Controller
        29. OSC32KCTRL – 32KHz Oscillators Controller

28.6.5.1 Basic Operation

        Initialization, Enabling, Disabling, and Resetting
        The DPLLCn is enabled by writing a ‘1’ to the Enable bit in the Control register (DPLLnCTRLA.ENABLE).
        The DPLLCn is disabled by writing a ‘0’ to DPLLnCTRLA.ENABLE. The DPLLnSYNCBUSY.ENABLE is
        set when the DPLLnCTRLA.ENABLE bit is modified. It is cleared when the DPLLCn output clock
        CLK_DPLLn has sampled the bit at the high level, or cleared when the output clock is no longer running
        (for disable operation).




        © 2019 Microchip Technology Inc.                                  Datasheet                       DS60001507E-page 773
                                                            SAM D5x/E5x Family Data Sheet
                                                                             OSCCTRL – Oscillators Controller

Figure 28-3. Enable synchronization busy operation
              CLK_APB_OSCCTRL

                              ENABLE

                                   CK


                  SYNCBUSY.ENABLE

The frequency of the DPLLCn output clock CLK_DPLLn is stable when the module is enabled and when
the LOCK bit is set. When DPLLnCTRLB.LTIME is different from 0, a user defined lock time is used to
validate the lock operation. In that case the lock time is constant. If DPLLnCTRLB.LTIME is zero, the lock
signal is linked with the status bit of the DPLLCn (DPLLnSTATUS.LOCK), the lock time vary depending
on the filter selection and final target frequency. When DPLLnCTRLB.WUF is set the wake up fast mode
is activated. In that mode the clock gating cell is enabled at the end of the startup time. At that time the
final frequency is not stable as it is still the acquisition period, but it allows to save hundreds of
microseconds. After the first acquisition, DPLLnCTRLB.LBYPASS indicates if the Lock signal is discarded
from the control of the clock gater (CG) generating the output clock CLK_DPLLn.
Table 28-3. CLK_DPLLn behavior from startup to first edge detection.

 WUF                                    LTIME                                         CLK_DPLLn Behavior
 0                                      0                                             Normal Mode: First Edge when
                                                                                      lock is asserted
 0                                      Not Equal To Zero                             Lock Timer Timeout mode: First
                                                                                      Edge when the timer down-
                                                                                      counts to 0.
 1                                      X                                             Wake Up Fast Mode: First Edge
                                                                                      when CK is active (startup time)

Table 28-4. CLK_DPLLn behavior after First Edge detection.

 LBYPASS                                                           CLK_DPLLn Behavior
 0                                                                 Normal Mode: the CLK_DPLLn is turned off when
                                                                   lock signal is low.
 1                                                                 Lock Bypass Mode: the CLK_DPLLn is always
                                                                   running, lock is irrelevant.

Figure 28-4. CK and CLK_DPLL output from DPLL off mode to running mode

                     CKR


                 ENABLE


                      CK

               CLK_DPLL


                   LOCK


                                                t startup_time          t lock_time          CK STABLE




© 2019 Microchip Technology Inc.                                 Datasheet                          DS60001507E-page 774
                                                         SAM D5x/E5x Family Data Sheet
                                                                          OSCCTRL – Oscillators Controller

Figure 28-5. CK and CLK_DPLL output from DPLL off mode to running mode when wake up fast
is activated

                     CKR


                 ENABLE


                      CK

               CLK_DPLL


                   LOCK


                                             t startup_time         t lock_time      CK STABLE
Figure 28-6. CK and CLK_DPLL output from running mode to DPLLC off mode.

                     CKR

                 ENABLE


                      CK


               CLK_DPLL


                   LOCK



Operating modes
The DPLLn will behave differently in different sleep modes based on the settings of
DPLLnCTRLA.RUNSTDBY, DPLLnCTRLA.ONDEMAND and DPLLnCTRLA.ENABLE.
Table 28-5. DPLL Sleep Behavior

 DPLLCTRLA.RUNSTD                  DPLLCTRLA.ONDEMA DPLLCTRLA.ENABLE                  Sleep Behavior
 BY                                ND
 -                                 -                            0                     Disabled
 0                                 0                            1                     Always run in Idle Sleep
                                                                                      modes. Run in Standby
                                                                                      Sleep mode if requested
                                                                                      by a peripheral.
 0                                 1                            1                     Only run in Idle or
                                                                                      Standby Sleep modes if
                                                                                      requested by a
                                                                                      peripheral.
 1                                 0                            1                     Always run in Idle and
                                                                                      Standby Sleep modes.
 1                                 1                            1                     Only run in Idle or
                                                                                      Standby Sleep modes if
                                                                                      requested by a
                                                                                      peripheral.




© 2019 Microchip Technology Inc.                              Datasheet                    DS60001507E-page 775
                                                 SAM D5x/E5x Family Data Sheet
                                                              OSCCTRL – Oscillators Controller

Reference Clock Switching
When a software operation requires reference clock switching, the normal operation is to disable the
DPLLn, modify the DPLLnCTRLB.REFCLK to select the desired reference source and activate the
DPLLn again. The CLK_DPLLn output clock is ready when DPLLnSTATUS.CLKRDY bit is set.

XOSC Reference Clock Divider
DPLLnCTRLB.DIV[10:0] bits are used to set the XOSC clock division factor and can be calculated with
following formula:
          �XOSC
�DIV =
      2 × DIV + 1
For more information, refer to DPLLnCTRLB.

Loop Divider Ratio Updates
The DPLLn Controller supports on-the-fly update of the DPLLnRATIO register, so it is allowed to modify
the loop divider ratio and the loop divider ratio fractional part when the DPLLn is enabled. Ensure the
following conditions, or else the on-the-fly updating of the divider ratio will fail:
  • DPLLnCTRLB.LBYPASS must be '0' (normal mode).
  • DPLLnCTRLB.LTIME must not be 0x0, which is the default value.
  • A DPLLn 32KHz clock (GCLK_DPLLn_32K) is configured in the GCLK peripheral as the internal lock
    timer.
Write DPLLnRATIO.LDR[12:0] bits to set the integer part of the frequency multiplier, and write
DPLLnRATIO.LDRFRAC[4:0] bits to set the fractional part of the frequency multiplier. Due to
synchronization there is a delay between writing to DPLLnRATIO.LDRFRAC[4:0] or
DPLLnRATIO.LDR[12:0] and the effect on the DPLLn output clock. The value written
DPLLnRATIO.LDRFAC[4:0] or DPLLnRATIO.LDR[12:0] will be read back immediately, and the
DPLLRATIO bit in the synchronization busy register DPLLnSYNCBUSY.DPLLRATIO, will be set.
DPLLnSYNCBUSY.DPLLRATIO will be cleared when the operation is completed.STATUS.DPLLnLDRTO
is set when the DPLLnRATIO register has been modified and the DPLLn analog cell has successfully
sampled the updated value. At that time the DPLLnSTATUS.LOCK bit is cleared and set again by
hardware when the output frequency reached a stable state. Note that if only the fractional part of loop
divider ratio (DPLLnRATIO.LDRFRAC) is updated, the lock status (DPLLnSTATUS.LOCK) will not be
cleared.
Figure 28-7. RATIOCTRL register update operation

                     CKR

                LDR
                              mult0      mult1
                LDRFRAC


                      CK


               CLK_DPLL


                    LOCK


                   LOCKL




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 776
                                                             SAM D5x/E5x Family Data Sheet
                                                                           OSCCTRL – Oscillators Controller

         Digital Filter Selection
         The digital filter selection can be changed from the filter selection register DPLLnCTRLB.FILTER. The
         DPLL digital filter coefficients are automatically adjusted in order to provide a good compromise between
         stability and jitter. For more information, refer to DPLLnCTRLB.

         Sigma-Delta DCO Filter Selection
         The sigma-delta DAC low pass filter can be controlled and adjusted from the DCO filter selection register
         DPLLnCTRLB.DCOFILTER[2:0]. For more information, refer to DPLLnCTRLB.
         Related Links
         14. GCLK - Generic Clock Controller

28.6.6   DMA Operation
         Not applicable.

28.6.7   Interrupts
         The OSCCTRL has the following interrupt sources:
           • XOSCRDY - Multipurpose Crystal Oscillator Ready: A 0-to-1” transition on the STATUS.XOSCRDY
             bit is detected
           • CLKFAIL - Clock Failure . A “0-to-1” transition on the STATUS.CLKFAIL bit is detected.
           • DFLLRDY - DFLL48m Ready: A “0-to-1” transition on the STATUS.DFLLRDY bit is detected
           • DPLLnLOCKR - DPLLn Lock Rise: A “0-to-1” transition on the STATUS.DPLLnLOCKR bit is detected
           • DPLLnLOCKF - DPLLn Lock Fall: A “0-to-1” transition on the STATUS.DPLLnLOCKF bit is detected
           • DPLLnLTTO - DPLLn Lock Timer Time-out: A “0-to-1” transition on the STATUS.DPLLnLTTO bit is
             detected
           • DPLLnLDRTO - DPLLn Loop Divider Ratio Update Complete. A “0-to-1” transition on the
             STATUS.DPLLnLDRTO bit is detected
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear register (INTFLAG) is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a one to the corresponding bit in the Interrupt Enable Set register
         (INTENSET), and disabled by writing a one to the corresponding bit in the Interrupt Enable Clear register
         (INTENCLR). An interrupt request is generated when the interrupt flag is set and the corresponding
         interrupt is enabled. The interrupt request remains active until the interrupt flag is cleared, the interrupt is
         disabled or the OSCCTRL is reset. INTFLAG register for details on how to clear interrupt flags.
         The OSCCTRL has one common interrupt request line for all the interrupt sources. The user must read
         the INTFLAG register to determine which interrupt condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated.

28.6.8   Events
         The CFD can generate the following output event:
          • Clock Failure (CLKFAIL): Generated when the Clock Failure status bit is set in the Status register
             (STATUS.CLKFAIL). The CFD event is not generated when the Clock Switch bit (STATUS.CLKSW)
             in the Status register is set.
         Writing a '1' to an Event Output bit in the Event Control register (EVCTRL.CFDEO) enables the CFD
         output event. Writing a '0' to this bit disables the CFD output event. Refer to the Event System chapter for
         details on configuring the event system.




         © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 777
                                                          SAM D5x/E5x Family Data Sheet
                                                                        OSCCTRL – Oscillators Controller

28.6.9   Synchronization
         Due to the multiple clock domains, some registers in the DFLL48M must be synchronized when
         accessed. A register can require:
           • Synchronization when written
           • Synchronization when read
           • No synchronization
         When executing an operation that requires synchronization, the relevant synchronization bit in the
         Synchronization Busy register (DFLLSYNC) will be set immediately, and cleared when synchronization is
         complete.
         The following registers need synchronization:
           •   ENABLE bit in DFLLCTRLA register - write-synchronized
           •   DFLLCTRLB register - read-synchronized
           •   DFLLVAL register - read- and write-synchronized
           •   DFLLMUL register - write-synchronized
         Due to the multiple clock domains (XOSC32K, XOSC, GCLK and CK), some registers in the DPLL must
         be synchronized when accessed. A register can require:
           • Synchronization when written
           • No synchronization
         When executing an operation that requires synchronization, the relevant synchronization bit in the
         Synchronization Busy register (DPLLnSYNCBUSY) will be set immediately, and cleared when
         synchronization is complete.
         The following bits need synchronization when written:
           • Enable bit in control register A (DPLLnCTRLA.ENABLE)
           • DPLLn Ratio register (DPLLnRATIO)




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 778
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                     OSCCTRL – Oscillators Controller


28.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         EVCTRL          7:0                                                                               CFDEO1     CFDEO0
 0x01
   ...       Reserved
 0x03
                              7:0                                                      XOSCFAIL1   XOSCFAIL0   XOSCRDY1   XOSCRDY0
                             15:8                                          DFLLRCS     DFLLLCKC    DFLLLCKF     DFLLOOB    DFLLRDY
 0x04        INTENCLR
                             23:16                                                    DPLL0LDRTO DPLL0LTO      DPLL0LCKF DPLL0LCKR
                             31:24                                                    DPLL1LDRTO DPLL1LTO      DPLL1LCKF DPLL1LCKR
                              7:0                                                      XOSCFAIL1   XOSCFAIL0   XOSCRDY1   XOSCRDY0
                             15:8                                          DFLLRCS     DFLLLCKC    DFLLLCKF     DFLLOOB    DFLLRDY
 0x08        INTENSET
                             23:16                                                    DPLL0LDRTO DPLL0LTO      DPLL0LCKF DPLL0LCKR
                             31:24                                                    DPLL1LDRTO DPLL1LTO      DPLL1LCKF DPLL1LCKR
                              7:0                                                                  XOSCFAIL    XOSCRDY1   XOSCRDY0
                             15:8                                          DFLLRCS     DFLLLCKC    DFLLLCKF     DFLLOOB    DFLLRDY
 0x0C        INTFLAG
                             23:16                                                    DPLL0LDRTO DPLL0LTO      DPLL0LCKF DPLL0LCKR
                             31:24                                                    DPLL1LDRTO DPLL1LTO      DPLL1LCKF DPLL1LCKR
                              7:0                         XOSCCKSW1 XOSCCKSW0 XOSCFAIL1            XOSCFAIL0   XOSCRDY1   XOSCRDY0
                             15:8                                          DFLLRCS     DFLLLCKC    DFLLLCKF     DFLLOOB    DFLLRDY
 0x10         STATUS
                             23:16                                                    DPLL0LDRTO   DPLL0TO     DPLL0LCKF DPLL0LCKR
                             31:24                                                    DPLL1LDRTO   DPLL1TO     DPLL1LCKF DPLL1LCKR
                              7:0     ONDEMAND RUNSTDBY                                             XTALEN      ENABLE
                                                                                                                          LOWBUFGAI
                             15:8      ENALC                        IMULT[3:0]                           IPTAT[1:0]
 0x14       XOSCCTRL0                                                                                                        N
                             23:16                  STARTUP[3:0]                                                 SWBEN     CFDEN
                             31:24                                                                    CFDPRESC[3:0]
                              7:0     ONDEMAND RUNSTDBY                                             XTALEN      ENABLE
                                                                                                                          LOWBUFGAI
                             15:8      ENALC                        IMULT[3:0]                           IPTAT[1:0]
 0x18       XOSCCTRL1                                                                                                        N
                             23:16                  STARTUP[3:0]                                                 SWBEN     CFDEN
                             31:24                                                                    CFDPRESC[3:0]
 0x1C       DFLLCTRLA         7:0     ONDEMAND RUNSTDBY                                                         ENABLE
 0x1D
   ...       Reserved
 0x1F
 0x20       DFLLCTRLB         7:0     WAITLOCK   BPLCKC      QLDIS          CCDIS       USBCRM       LLAW        STABLE     MODE
 0x21
   ...       Reserved
 0x23
                              7:0                                                FINE[7:0]
                             15:8                                  COARSE[5:0]
 0x24         DFLLVAL
                             23:16                                               DIFF[7:0]
                             31:24                                               DIFF[15:8]




          © 2019 Microchip Technology Inc.                            Datasheet                                DS60001507E-page 779
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                         OSCCTRL – Oscillators Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                                 MUL[7:0]
                                 15:8                                               MUL[15:8]
   0x28            DFLLMUL
                                 23:16                                             FSTEP[7:0]
                                 31:24                                CSTEP[5:0]
   0x2C           DFLLSYNC        7:0                                          DFLLMUL      DFLLVAL   DFLLCTRLB       ENABLE
   0x2D
     ...           Reserved
   0x2F
   0x30          DPLL0CTRLA       7:0     ONDEMAND RUNSTDBY                                                           ENABLE
   0x31
     ...           Reserved
   0x33
                                  7:0                                                 LDR[7:0]
                                 15:8                                                                  LDR[12:8]
   0x34          DPLL0RATIO
                                 23:16                                                                LDRFRAC[4:0]
                                 31:24
                                  7:0              REFCLK[2:0]                  WUF                          FILTER[3:0]
                                 15:8      DCOEN              DCOFILTER[2:0]                LBYPASS                  LTIME[2:0]
   0x38          DPLL0CTRLB
                                 23:16                                                DIV[7:0]
                                 31:24                                                                               DIV[10:8]
                                  7:0                                                                  DPLLRATIO      ENABLE
                                 15:8
   0x3C       DPLL0SYNCBUSY
                                 23:16
                                 31:24
                                  7:0                                                                                CLKRDY       LOCK
                                 15:8
   0x40         DPLL0STATUS
                                 23:16
                                 31:24
   0x44          DPLL1CTRLA       7:0     ONDEMAND RUNSTDBY                                                           ENABLE
   0x45
     ...           Reserved
   0x47
                                  7:0                                                 LDR[7:0]
                                 15:8                                                                  LDR[12:8]
   0x48          DPLL1RATIO
                                 23:16                                                                LDRFRAC[4:0]
                                 31:24
                                  7:0              REFCLK[2:0]                  WUF                          FILTER[3:0]
                                 15:8      DCOEN              DCOFILTER[2:0]                LBYPASS                  LTIME[2:0]
   0x4C          DPLL1CTRLB
                                 23:16                                                DIV[7:0]
                                 31:24                                                                               DIV[10:8]
                                  7:0                                                                  DPLLRATIO      ENABLE
                                 15:8
   0x50       DPLL1SYNCBUSY
                                 23:16
                                 31:24




              © 2019 Microchip Technology Inc.                          Datasheet                                    DS60001507E-page 780
                                                                  SAM D5x/E5x Family Data Sheet
                                                                               OSCCTRL – Oscillators Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                                                    CLKRDY      LOCK
                                 15:8
   0x54         DPLL1STATUS
                                 23:16
                                 31:24




28.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Write-protection
               is denoted by the "PAC Write-Protection" property in each individual register description. Refer to the
               28.5.8 Register Access Protection section and the PAC - Peripheral Access Controller chapter for details.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" or "Write-Synchronized" property in each individual register description. Refer to
               the section on Synchronization for details.
               Related Links
               28.6.9 Synchronization




              © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 781
                                                                SAM D5x/E5x Family Data Sheet
                                                                             OSCCTRL – Oscillators Controller

28.8.1         Event Control

               Name:       EVCTRL
               Offset:     0x00
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6            5            4            3            2            1            0
                                                                                                CFDEO1       CFDEO0
   Access           R             R            R            R            R            R           R/W          R/W
    Reset            0            0            0            0            0            0            0            0


               Bits 0, 1 – CFDEO Clock n Failure Detector Event Output Enable [n=0,1]
               This bit indicates whether the XOSC Clock Failure detector event output is enabled or not and an output
               event will be generated when the XOSC Clock Failure detector detects a clock failure.
               0: Clock Failure detector event output is disabled and an event will not be generated.
               1: Clock Failure detector event output is enabled and an event will be generated.
               To prevent false event generation, the bit CFDEOn must be set or cleared only when the XOSCn is
               disabled (XOSCCTRLn.ENABLE=0).




           © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 782
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                OSCCTRL – Oscillators Controller

28.8.2         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x04
               Reset:       0x00000000
               Property:    PAC Write-Protection
               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).


         Bit        31            30           29            28            27           26            25           24
                                                                      DPLL1LDRTO     DPLL1LTO     DPLL1LCKF    DPLL1LCKR
   Access                                                                 R/W          R/W           R/W           R/W
    Reset                                                                  0             0            0             0


         Bit        23            22           21            20            19           18            17           16
                                                                      DPLL0LDRTO     DPLL0LTO     DPLL0LCKF    DPLL0LCKR
   Access                                                                 R/W          R/W           R/W           R/W
    Reset                                                                  0             0            0             0


         Bit        15            14           13            12            11           10            9             8
                                                          DFLLRCS      DFLLLCKC      DFLLLCKF      DFLLOOB      DFLLRDY
   Access                                                   R/W           R/W          R/W           R/W           R/W
    Reset                                                     0            0             0            0             0


         Bit         7            6             5             4            3             2            1             0
                                                                       XOSCFAIL1    XOSCFAIL0     XOSCRDY1     XOSCRDY0
   Access                                                                 R/W          R/W           R/W           R/W
    Reset                                                                  0             0            0             0


               Bit 27 – DPLL1LDRTO DPLL1 Loop Divider Ratio Update Complete Interrupt Enable
               0: The DPLL1 Loop Divider Ratio Update Complete interrupt is disabled.
               1: The DPLL1 Loop Divider Ratio Update Complete interrupt is enabled, and an interrupt request will be
               generated when the DPLL1 Loop Divider Ratio Update Complete Interrupt flag is set.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit will clear the DPLL1 Loop Divider Ratio Update Complete Interrupt Enable bit,
               which disables the DPLL1 Loop Divider Ratio Update Complete interrupt.

               Bit 26 – DPLL1LTO DPLL1 Lock Timeout Interrupt Enable
               0: The DPLL1 Lock Timeout interrupt is disabled.
               1: The DPLL1 Lock Timeout interrupt is enabled, and an interrupt request will be generated when the
               DPLL1 Lock Timeout Interrupt flag is set.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit will clear the DPLL1 Lock Timeout Interrupt Enable bit, which disables the DPLL1
               Lock Timeout interrupt.

               Bit 25 – DPLL1LCKF DPLL1 Lock Fall Interrupt Enable
               0: The DPLL1 Lock Fall interrupt is disabled.
               1: The DPLL1 Lock Fall interrupt is enabled, and an interrupt request will be generated when the DPLL1
               Lock Fall Interrupt flag is set.




           © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 783
                                                   SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DPLL1 Lock Fall Interrupt Enable bit, which disables the DPLL1 Lock
Fall interrupt.

Bit 24 – DPLL1LCKR DPLL1 Lock Rise Interrupt Enable
0: The DPLL1 Lock Rise interrupt is disabled.
1: The DPLL1 Lock Rise interrupt is enabled, and an interrupt request will be generated when the DPLL1
Lock Rise Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DPLL1 Lock Rise Interrupt Enable bit, which disables the DPLL1 Lock
Rise interrupt.

Bit 19 – DPLL0LDRTO DPLL0 Loop Divider Ratio Update Complete Interrupt Enable
0: The DPLL0 Loop Divider Ratio Update Complete interrupt is disabled.
1: The DPLL0 Loop Divider Ratio Update Complete interrupt is enabled, and an interrupt request will be
generated when the DPLL0 Loop Divider Ratio Update Complete Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DPLL0 Loop Divider Ratio Update Complete Interrupt Enable bit,
which disables the DPLL0 Loop Divider Ratio Update Complete interrupt.

Bit 18 – DPLL0LTO DPLL0 Lock Timeout Interrupt Enable
0: The DPLL0 Lock Timeout interrupt is disabled.
1: The DPLL0 Lock Timeout interrupt is enabled, and an interrupt request will be generated when the
DPLL0 Lock Timeout Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DPLL0 Lock Timeout Interrupt Enable bit, which disables the DPLL0
Lock Timeout interrupt.

Bit 17 – DPLL0LCKF DPLL0 Lock Fall Interrupt Enable
0: The DPLL0 Lock Fall interrupt is disabled.
1: The DPLL0 Lock Fall interrupt is enabled, and an interrupt request will be generated when the DPLL0
Lock Fall Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DPLL0 Lock Fall Interrupt Enable bit, which disables the DPLL0 Lock
Fall interrupt.

Bit 16 – DPLL0LCKR DPLL0 Lock Rise Interrupt Enable
0: The DPLL0 Lock Rise interrupt is disabled.
1: The DPLL0 Lock Rise interrupt is enabled, and an interrupt request will be generated when the DPLL0
Lock Rise Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DPLL0 Lock Rise Interrupt Enable bit, which disables the DPLL0 Lock
Rise interrupt.

Bit 12 – DFLLRCS DFLL Reference Clock Stopped Interrupt Enable
0: The DFLL Reference Clock Stopped interrupt is disabled.
1: The DFLL Reference Clock Stopped interrupt is enabled, and an interrupt request will be generated
when the DFLL Reference Clock Stopped Interrupt flag is set.
Writing a zero to this bit has no effect.




© 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 784
                                                   SAM D5x/E5x Family Data Sheet
                                                                 OSCCTRL – Oscillators Controller

Writing a '1' to this bit will clear the DFLL Reference Clock Stopped Interrupt Enable bit, which disables
the DFLL Reference Clock Stopped interrupt.

Bit 11 – DFLLLCKC DFLL Lock Coarse Interrupt Enable
0: The DFLL Lock Coarse interrupt is disabled.
1: The DFLL Lock Coarse interrupt is enabled, and an interrupt request will be generated when the DFLL
Lock Coarse Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DFLL Lock Coarse Interrupt Enable bit, which disables the DFLL Lock
Coarse interrupt.

Bit 10 – DFLLLCKF DFLL Lock Fine Interrupt Enable
0: The DFLL Lock Fine interrupt is disabled.
1: The DFLL Lock Fine interrupt is enabled, and an interrupt request will be generated when the DFLL
Lock Fine Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DFLL Lock Fine Interrupt Enable bit, which disables the DFLL Lock
Fine interrupt.

Bit 9 – DFLLOOB DFLL Out Of Bounds Interrupt Enable
0: The DFLL Out Of Bounds interrupt is disabled.
1: The DFLL Out Of Bounds interrupt is enabled, and an interrupt request will be generated when the
DFLL Out Of Bounds Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DFLL Out Of Bounds Interrupt Enable bit, which disables the DFLL
Out Of Bounds interrupt.

Bit 8 – DFLLRDY DFLL Ready Interrupt Enable
0: The DFLL Ready interrupt is disabled.
1: The DFLL Ready interrupt is enabled, and an interrupt request will be generated when the DFLL
Ready Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the DFLL Ready Interrupt Enable bit, which disables the DFLL Ready
interrupt.

Bits 2, 3 – XOSCFAIL XOSC n Clock Failure Interrupt Enable
0: The XOSC n Clock Failure interrupt is disabled.
1: The XOSC0 Clock Failure interrupt is enabled, and an interrupt request will be generated when the
XOSC0 Clock Failure Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the XOSC n Clock Failure Interrupt Enable bit, which disables the XOSC n
Clock Failure interrupt.

Bits 0, 1 – XOSCRDY XOSC n Ready Interrupt Enable
0: The XOSC n Ready interrupt is disabled.
1: The XOSC0 Ready interrupt is enabled, and an interrupt request will be generated when the XOSC n
Ready Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will clear the XOSC n Ready Interrupt Enable bit, which disables the XOSC n
Ready interrupt.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 785
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                OSCCTRL – Oscillators Controller

28.8.3         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x08
               Reset:       0x00000000
               Property:    PAC Write-Protection
               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).


         Bit        31            30           29            28           27            26            25           24
                                                                      DPLL1LDRTO     DPLL1LTO    DPLL1LCKF     DPLL1LCKR
   Access                                                                 R/W          R/W           R/W          R/W
    Reset                                                                  0             0            0             0


         Bit        23            22           21            20           19            18            17           16
                                                                      DPLL0LDRTO     DPLL0LTO    DPLL0LCKF     DPLL0LCKR
   Access                                                                 R/W          R/W           R/W          R/W
    Reset                                                                  0             0            0             0


         Bit        15            14           13            12            11           10            9             8
                                                          DFLLRCS      DFLLLCKC     DFLLLCKF      DFLLOOB       DFLLRDY
   Access                                                   R/W           R/W          R/W           R/W          R/W
    Reset                                                    0             0             0            0             0


         Bit         7            6             5            4             3             2            1             0
                                                                      XOSCFAIL1     XOSCFAIL0     XOSCRDY1     XOSCRDY0
   Access                                                                 R/W          R/W           R/W          R/W
    Reset                                                                  0             0            0             0


               Bit 27 – DPLL1LDRTO DPLL1 Loop Divider Ratio Update Complete Interrupt Enable
               0: The DPLL1 Loop Divider Ratio Update Complete interrupt is disabled.
               1: The DPLL1 Loop Divider Ratio Update Complete interrupt is enabled, and an interrupt request will be
               generated when the DPLL1 Loop Divider Ratio Update Complete Interrupt flag is set.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit will set the DPLL1 Loop Divider Ratio Update Complete Interrupt Enable bit, which
               enables the DPLL1 Loop Divider Ratio Update Complete interrupt.

               Bit 26 – DPLL1LTO DPLL1 Lock Timeout Interrupt Enable
               0: The DPLL1 Lock Timeout interrupt is disabled.
               1: The DPLL1 Lock Timeout interrupt is enabled, and an interrupt request will be generated when the
               DPLL1 Lock Timeout Interrupt flag is set.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit will set the DPLL1 Lock Timeout Interrupt Enable bit, which enables the DPLL1
               Lock Timeout interrupt.

               Bit 25 – DPLL1LCKF DPLL1 Lock Fall Interrupt Enable
               0: The DPLL1 Lock Fall interrupt is disabled.
               1: The DPLL1 Lock Fall interrupt is enabled, and an interrupt request will be generated when the DPLL1
               Lock Fall Interrupt flag is set.




           © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 786
                                                  SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DPLL1 Lock Fall Interrupt Enable bit, which enables the DPLL1 Lock
Fall interrupt.

Bit 24 – DPLL1LCKR DPLL1 Lock Rise Interrupt Enable
0: The DPLL1 Lock Rise interrupt is disabled.
1: The DPLL1 Lock Rise interrupt is enabled, and an interrupt request will be generated when the DPLL1
Lock Rise Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DPLL1 Lock Rise Interrupt Enable bit, which enables the DPLL1 Lock
Rise interrupt.

Bit 19 – DPLL0LDRTO DPLL0 Loop Divider Ratio Update Complete Interrupt Enable
0: The DPLL0 Loop Divider Ratio Update Complete interrupt is disabled.
1: The DPLL0 Loop Divider Ratio Update Complete interrupt is enabled, and an interrupt request will be
generated when the DPLL0 Loop Divider Ratio Update Complete Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DPLL0 Loop Divider Ratio Update Complete Interrupt Enable bit, which
enables the DPLL0 Loop Divider Ratio Update Complete interrupt.

Bit 18 – DPLL0LTO DPLL0 Lock Timeout Interrupt Enable
0: The DPLL0 Lock Timeout interrupt is disabled.
1: The DPLL0 Lock Timeout interrupt is enabled, and an interrupt request will be generated when the
DPLL0 Lock Timeout Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DPLL0 Lock Timeout Interrupt Enable bit, which enables the DPLL0
Lock Timeout interrupt.

Bit 17 – DPLL0LCKF DPLL0 Lock Fall Interrupt Enable
0: The DPLL0 Lock Fall interrupt is disabled.
1: The DPLL0 Lock Fall interrupt is enabled, and an interrupt request will be generated when the DPLL0
Lock Fall Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DPLL0 Lock Fall Interrupt Enable bit, which enables the DPLL0 Lock
Fall interrupt.

Bit 16 – DPLL0LCKR DPLL0 Lock Rise Interrupt Enable
0: The DPLL0 Lock Rise interrupt is disabled.
1: The DPLL0 Lock Rise interrupt is enabled, and an interrupt request will be generated when the DPLL0
Lock Rise Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DPLL0 Lock Rise Interrupt Enable bit, which enables the DPLL0 Lock
Rise interrupt.

Bit 12 – DFLLRCS DFLL Reference Clock Stopped Interrupt Enable
0: The DFLL Reference Clock Stopped interrupt is disabled.
1: The DFLL Reference Clock Stopped interrupt is enabled, and an interrupt request will be generated
when the DFLL Reference Clock Stopped Interrupt flag is set.
Writing a zero to this bit has no effect.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 787
                                                  SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

Writing a '1' to this bit will set the DFLL Reference Clock Stopped Interrupt Enable bit, which enables the
DFLL Reference Clock Stopped interrupt.

Bit 11 – DFLLLCKC DFLL Lock Coarse Interrupt Enable
0: The DFLL Lock Coarse interrupt is disabled.
1: The DFLL Lock Coarse interrupt is enabled, and an interrupt request will be generated when the DFLL
Lock Coarse Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DFLL Lock Coarse Interrupt Enable bit, which enables the DFLL Lock
Coarse interrupt.

Bit 10 – DFLLLCKF DFLL Lock Fine Interrupt Enable
0: The DFLL Lock Fine interrupt is disabled.
1: The DFLL Lock Fine interrupt is enabled, and an interrupt request will be generated when the DFLL
Lock Fine Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DFLL Lock Fine Interrupt Disable/Enable bit, disable the DFLL Lock
Fine interrupt and set the corresponding interrupt request.

Bit 9 – DFLLOOB DFLL Out Of Bounds Interrupt Enable
0: The DFLL Out Of Bounds interrupt is disabled.
1: The DFLL Out Of Bounds interrupt is enabled, and an interrupt request will be generated when the
DFLL Out Of Bounds Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DFLL Out Of Bounds Interrupt Enable bit, which enables the DFLL Out
Of Bounds interrupt.

Bit 8 – DFLLRDY DFLL Ready Interrupt Enable
0: The DFLL Ready interrupt is disabled.
1: The DFLL Ready interrupt is enabled, and an interrupt request will be generated when the DFLL
Ready Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the DFLL Ready Interrupt Enable bit, which enables the DFLL Ready
interrupt.

Bits 2, 3 – XOSCFAIL XOSCn Clock Failure Interrupt Enable
0: The XOSCn Clock Failure interrupt is disabled.
1: The XOSCn Clock Failure interrupt is enabled, and an interrupt request will be generated when the
XOSCn Clock Failure Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the XOSCn Clock Failure Interrupt Enable bit, which enables the XOSCn
Clock Failure interrupt.

Bits 0, 1 – XOSCRDY XOSCn Ready Interrupt Enable
0: The XOSCn Ready interrupt is disabled.
1: The XOSCn Ready interrupt is enabled, and an interrupt request will be generated when the XOSC0
Ready Interrupt flag is set.
Writing a zero to this bit has no effect.
Writing a '1' to this bit will set the XOSCn Ready Interrupt Enable bit, which enables the XOSCn Ready
interrupt.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 788
                                                                  SAM D5x/E5x Family Data Sheet
                                                                               OSCCTRL – Oscillators Controller

28.8.4         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x0C
               Reset:      0x00000000


         Bit        31            30           29           28            27           26            25            24
                                                                     DPLL1LDRTO     DPLL1LTO     DPLL1LCKF      DPLL1LCKR
   Access                                                                R/W          R/W           R/W           R/W
    Reset                                                                 0             0            0              0


         Bit        23            22           21           20            19           18            17            16
                                                                     DPLL0LDRTO     DPLL0LTO     DPLL0LCKF      DPLL0LCKR
   Access                                                                R/W          R/W           R/W           R/W
    Reset                                                                 0             0            0              0


         Bit        15            14           13           12            11           10            9              8
                                                         DFLLRCS      DFLLLCKC      DFLLLCKF     DFLLOOB        DFLLRDY
   Access                                                   R/W          R/W          R/W           R/W           R/W
    Reset                                                    0            0             0            0              0


         Bit         7            6             5            4            3             2            1              0
                                                                                    XOSCFAIL     XOSCRDY1       XOSCRDY0
   Access                                                                             R/W           R/W           R/W
    Reset                                                                               0            0              0


               Bit 27 – DPLL1LDRTO DPLL1 Loop Divider Ratio Update Complete
               This flag is cleared by writing a '1' to it.
               This flag is set on a zero-to-one transition of the DPLL1 Loop Divider Ratio Update Complete bit in the
               Status register (STATUS.DPLL1LDRTO) and will generate an interrupt request if
               INTENSET.DPLL1LDRTO is '1'.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the DPLL1 Loop Divider Ratio Update Complete interrupt flag.

               Bit 26 – DPLL1LTO DPLL1 Lock Timeout
               This flag is cleared by writing a '1' to it.
               This flag is set on a zero-to-one transition of the DPLL1 Lock Timeout bit in the Status register (STATUS.
               DPLL1LTO) and will generate an interrupt request if INTENSET.DPLL1LTO is '1'.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the DPLL1 Lock Timeout interrupt flag.

               Bit 25 – DPLL1LCKF DPLL1 Lock Fall
               This flag is cleared by writing a '1' to it.
               This flag is set on a zero-to-one transition of the DPLL1 Lock Fall bit in the Status register
               (STATUS.DPLL1LCKF) and will generate an interrupt request if INTENSET.DPLL1LCKF is '1'.
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the DPLL1 Lock Fall interrupt flag.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 789
                                                   SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

Bit 24 – DPLL1LCKR DPLL1 Lock Rise
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DPLL1 Lock Rise bit in the Status register (STATUS.
DPLL1LCKR) and will generate an interrupt request if INTENSET.DPLL1LCKR is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DPLL1 Lock Rise interrupt flag.

Bit 19 – DPLL0LDRTO DPLL0 Loop Divider Ratio Update Complete
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DPLL0 Loop Divider Ratio Update Complete bit in the
Status register (STATUS.DPLL0LDRTO) and will generate an interrupt request if
INTENSET.DPLL0LDRTO is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DPLL0 Loop Divider Ratio Update Complete interrupt flag.

Bit 18 – DPLL0LTO DPLL0 Lock Timeout
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DPLL0 Lock Timeout bit in the Status register (STATUS.
DPLL0LTO) and will generate an interrupt request if INTENSET.DPLL0LTO is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DPLL0 Lock Timeout interrupt flag.

Bit 17 – DPLL0LCKF DPLL0 Lock Fall
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DPLL0 Lock Fall bit in the Status register
(STATUS.DPLL0LCKF) and will generate an interrupt request if INTENSET.DPLL0LCKF is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DPLL0 Lock Fall interrupt flag.

Bit 16 – DPLL0LCKR DPLL0 Lock Rise
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DPLL0 Lock Rise bit in the Status register (STATUS.
DPLL0LCKR) and will generate an interrupt request if INTENSET.DPLL0LCKR is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DPLL0 Lock Rise interrupt flag.

Bit 12 – DFLLRCS DFLL Reference Clock Stopped
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DFLL Reference Clock Stopped bit in the Status register
(STATUS. DFLLRCS) and will generate an interrupt request if INTENSET.DFLLRCS is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DFLL Reference Clock Stopped interrupt flag.

Bit 11 – DFLLLCKC DFLL Lock Coarse
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DFLL Lock Coarse bit in the Status register
(STATUS.DFLLLCKC) and will generate an interrupt request if INTENSET.DFLLLCKC is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DFLL Lock Coarse interrupt flag.




© 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 790
                                                   SAM D5x/E5x Family Data Sheet
                                                                 OSCCTRL – Oscillators Controller

Bit 10 – DFLLLCKF DFLL Lock Fine
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DFLL Lock Fine bit in the Status register
(STATUS.DFLLLCKF) and will generate an interrupt request if INTENSET.DFLLLCKF is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DFLL Lock Fine interrupt flag.

Bit 9 – DFLLOOB DFLL Out Of Bounds
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DFLL Out Of Bounds bit in the Status register
(STATUS.DFLLOOB) and will generate an interrupt request if INTENSET.DFLLOOB is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DFLL Out Of Bounds interrupt flag.

Bit 8 – DFLLRDY DFLL Ready
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the DFLL Ready bit in the Status register
(STATUS.DFLLRDY) and will generate an interrupt request if INTENSET.DFLLRDY is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DFLL Ready interrupt flag.

Bit 2 – XOSCFAIL XOSCn Clock Failure
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the XOSCn Clock Failure bit in the Status register
(STATUS.XOSCFAILn) and will generate an interrupt request if INTENSET.XOSCFAILn is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the XOSCn Clock Failure interrupt flag.

Bits 0, 1 – XOSCRDY XOSCn Ready
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the XOSC0 Ready bit in the Status register
(STATUS.XOSCRDYn) and will generate an interrupt request if INTENSET.XOSCRDYn is '1'.
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the XOSCn Ready interrupt flag.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 791
                                                                SAM D5x/E5x Family Data Sheet
                                                                               OSCCTRL – Oscillators Controller

28.8.5         Status

               Name:      STATUS
               Offset:    0x10
               Reset:     0x00000000


         Bit        31           30              29        28            27           26         25           24
                                                                     DPLL1LDRTO    DPLL1TO    DPLL1LCKF   DPLL1LCKR
   Access                                                                R            R          R            R
    Reset                                                                0            0           0           0


         Bit        23           22              21        20            19           18         17           16
                                                                     DPLL0LDRTO    DPLL0TO    DPLL0LCKF   DPLL0LCKR
   Access                                                                R            R          R            R
    Reset                                                                0            0           0           0


         Bit        15           14              13        12            11           10          9           8
                                                         DFLLRCS      DFLLLCKC     DFLLLCKF   DFLLOOB      DFLLRDY
   Access                                                   R            R            R          R            R
    Reset                                                   0            0            0           0           0


         Bit        7             6               5         4            3            2           1           0
                                              XOSCCKSW1 XOSCCKSW0    XOSCFAIL1    XOSCFAIL0   XOSCRDY1    XOSCRDY0
   Access                                        R          R            R            R          R           R/W
    Reset                                         0         0            0            0           0           0


               Bit 27 – DPLL1LDRTO DPLL1 Loop Divider Ratio Update Complete
               0: DPLL1 Loop Divider Ratio Update Complete not detected.
               1: DPLL1 Loop Divider Ratio Update Complete detected.

               Bit 26 – DPLL1TO DPLL1 Lock Timeout
               0: DPLL1 Lock time-out not detected.
               1: DPLL1 Lock time-out detected.

               Bit 25 – DPLL1LCKF DPLL1 Lock Fall
               0: DPLL1 Lock fall edge not detected.
               1: DPLL1 Lock fall edge detected.

               Bit 24 – DPLL1LCKR DPLL1 Lock Rise
               0: DPLL1 Lock rise edge not detected.
               1: DPLL1 Lock rise edge detected.

               Bit 19 – DPLL0LDRTO DPLL0 Loop Divider Ratio Update Complete
               0: DPLL0 Loop Divider Ratio Update Complete not detected.
               1: DPLL0 Loop Divider Ratio Update Complete detected.

               Bit 18 – DPLL0TO DPLL0 Lock Timeout
               0: DPLL0 Lock time-out not detected.
               1: DPLL0 Lock time-out detected.




           © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 792
                                                  SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

Bit 17 – DPLL0LCKF DPLL0 Lock Fall
0: DPLL0 Lock fall edge not detected.
1: DPLL0 Lock fall edge detected.

Bit 16 – DPLL0LCKR DPLL0 Lock Rise
0: DPLL0 Lock rise edge not detected.
1: DPLL0 Lock rise edge detected.

Bit 12 – DFLLRCS DFLL Reference Clock Stopped
0: DFLL reference clock is running.
1: DFLL reference clock has stopped.

Bit 11 – DFLLLCKC DFLL Lock Coarse
0: No DFLL coarse lock detected.
1: DFLL coarse lock detected.

Bit 10 – DFLLLCKF DFLL Lock Fine
0: No DFLL fine lock detected.
1: DFLL fine lock detected.

Bit 9 – DFLLOOB DFLL Out Of Bounds
0: No DFLL Out Of Bounds detected.
1: DFLL Out Of Bounds detected.

Bit 8 – DFLLRDY DFLL Ready
0: DFLL is not ready.
1: DFLL is stable and ready to be used as a clock source.

Bit 5 – XOSCCKSW1 XOSC1 Clock Switch
0: XOSC1 is not switched and provides the external clock or crystal oscillator clock.
1: XOSC is switched and provides the safe clock.

Bit 4 – XOSCCKSW0 XOSC0 Clock Switch
0: XOSC0 is not switched and provides the external clock or crystal oscillator clock.
1: XOSC0 is switched and provides the safe clock.

Bit 3 – XOSCFAIL1 XOSC1 Clock Failure
0: XOSC1 failure not detected.
1: XOSC1 failure detected.

Bit 2 – XOSCFAIL0 XOSC0 Clock Failure
0: XOSC0 failure not detected.
1: XOSC0 failure detected.

Bit 1 – XOSCRDY1 XOSC1 Ready
0: XOSC1 is not ready.
1: XOSC1 is stable and ready to be used as a clock source.

Bit 0 – XOSCRDY0 XOSC0 Ready
0: XOSC0 is not ready.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 793
                                               SAM D5x/E5x Family Data Sheet
                                                             OSCCTRL – Oscillators Controller

1: XOSC0 is stable and ready to be used as a clock source.




© 2019 Microchip Technology Inc.                 Datasheet                    DS60001507E-page 794
                                                                            SAM D5x/E5x Family Data Sheet
                                                                                        OSCCTRL – Oscillators Controller

28.8.6         External Multipurpose Crystal Oscillator Control

               Name:       XOSCCTRL
               Offset:     0x14 + n*0x04 [n=0..1]
               Reset:      0x00000080
               Property:   PAC Write-Protection


         Bit         31           30               29                 28          27          26                 25           24
                                                                                               CFDPRESC[3:0]
   Access                                                                         R/W         R/W                R/W         R/W
    Reset                                                                          0           0                  0           0


         Bit         23           22               21                 20          19          18                 17           16
                                      STARTUP[3:0]                                                          SWBEN           CFDEN
   Access            R/W         R/W               R/W                R/W                                        R/W         R/W
    Reset             0           0                  0                 0                                          0           0


         Bit         15           14               13                 12          11          10                  9           8
                  ENALC                                  IMULT[3:0]                                 IPTAT[1:0]           LOWBUFGAIN
   Access            R/W         R/W               R/W                R/W         R/W         R/W                R/W         R/W
    Reset             0           0                  0                 0           0           0                  0           0


         Bit          7           6                  5                 4           3           2                  1           0
                ONDEMAND      RUNSTDBY                                                      XTALEN          ENABLE
   Access            R/W         R/W                                                          R/W                R/W
    Reset             1           0                                                            0                  0


               Bits 27:24 – CFDPRESC[3:0] Clock Failure Detector Prescaler
               These bits select the prescaler for the clock failure detector.
               The DFLL48 oscillator is used to clock the CFD prescaler.
               The CFD safe clock frequency is the DFLL48 frequency divided by 2^CFDPRESC.

               Bits 23:20 – STARTUP[3:0] Start-Up Time
               These bits select start-up time for the oscillator XOSCn according to the table below.
               The OSCULP32K oscillator is used to clock the start-up counter.
               Table 28-6. Start-UpTime for External Multipurpose Crystal Oscillator

               STARTUP[3:0]                   Number of                       Number of XOSC             Approximate
                                              OSCULP32K Clock                 Clock Cycles               Equivalent Time(
                                              Cycles
               0x0                            1                               3                          31µs
               0x1                            2                               3                          61μs
               0x2                            4                               3                          122μs
               0x3                            8                               3                          244μs
               0x4                            16                              3                          488μs
               0x5                            32                              3                          977μs




           © 2019 Microchip Technology Inc.                                 Datasheet                             DS60001507E-page 795
                                                     SAM D5x/E5x Family Data Sheet
                                                                   OSCCTRL – Oscillators Controller

...........continued
 STARTUP[3:0]                      Number of             Number of XOSC           Approximate
                                   OSCULP32K Clock       Clock Cycles             Equivalent Time(
                                   Cycles
 0x6                               64                    3                        1953μs
 0x7                               128                   3                        3906μs
 0x8                               256                   3                        7813μs
 0x9                               512                   3                        15625μs
 0xA                               1024                  3                        31250μs
 0xB                               2048                  3                        62500μs
 0xC                               4096                  3                        125000μs
 0xD                               8192                  3                        250000μs
 0xE                               16384                 3                        500000μs
 0xF                               32768                 3                        1000000μs

Bit 17 – SWBEN Xosc Clock Switch Enable
This bit controls the XOSCn output clock switch back to the external clock or crystal oscillator in case of
clock recovery :
0: The clock switch back is disabled.
1: The clock switch back is enabled. This bit is reset once the XOSCn output clock is switched back to the
external clock or crystal oscillator.

Bit 16 – CFDEN Clock Failure Detector Enable
This bit controls the XOSCn clock failure detector :
0: the Clock Failure Detector is disabled.
1: the Clock Failure Detector is enabled.

Bit 15 – ENALC Automatic Loop Control Enable
This bit controls the XOSCn automatic loop control :
0: the automatic loop control is disabled.
1: the automatic loop control is enabled. Oscillator's amplitude will be automatically adjusted during
Crystal Oscillator operation.

Bits 14:11 – IMULT[3:0] Oscillator Current Multiplier
These bits select the current multiplier for the oscillator XOSCn, given in table External Multipurpose
Crystal Oscillator Current Settings.

Bits 10:9 – IPTAT[1:0] Oscillator Current Reference
These bits select the current reference for the oscillator XOSCn, given in table below.




© 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 796
                                                 SAM D5x/E5x Family Data Sheet
                                                               OSCCTRL – Oscillators Controller

Table 28-7. External Multipurpose Crystal Oscillator Current Settings

                                                               Current Setting
          Frequency Range                      IMULT[3:0]                          IPTAT[1:0]
 24MHz to 48MHz                                     6                                   3
 16MHz to 24MHz                                     5                                   3
 8MHz to 16MHz                                      4                                   3
 8MHz                                               3                                   2

For relatively small CLOAD in a frequency range, the setting for the lower frequency range can be used
to preserve current consumption.

Bit 8 – LOWBUFGAIN Low Buffer Gain Enable
0: The low buffer gain of oscillator XOSCn is disabled.
1: The low buffer gain of oscillator XOSCn is enabled.
When XOSCCTRLn.ENALC=0 this bit has no effect.
When XOSCCTRLn.ENALC=1, this bit is used to adjust the oscillator's amplitude in automatic loop
control.
The default value of LOWBUFGAIN=0 should be used to allow operating with a low amplitude oscillator.
Use this setting except to solve stability issues.
Setting LOWBUFGAIN=1 will increase the oscillator's amplitude by a factor of approximately 2. Use this
setting to solve stability issues.

Bit 7 – ONDEMAND On Demand Control
The On Demand operation mode allows the oscillator XOSCn to be enabled or disabled, depending on
peripheral clock requests.
If On Demand is set, the oscillator will be running only when requested by a peripheral and enabled
(XOSCCTRLn. ENABLE=1). If there is no peripheral requesting the oscillator’s clock source, the oscillator
will be in a disabled state.
If On Demand is cleared, the oscillator will always be running when enabled (XOSCCTRLn.ENABLE=1).
In standby sleep mode, the On Demand operation is still active.
0: The oscillator is always on.
1: The oscillator is running when a peripheral is requesting the oscillator to be used as a clock source.
The oscillator is not running if no peripheral is requesting the clock source.

Bit 6 – RUNSTDBY Run in Standby
This bit controls how the XOSCn behaves during standby sleep mode:
0: The XOSCn is not running in standby sleep mode if no peripheral requests the clock.
1: The XOSCn is running in standby sleep mode. If ONDEMAND is one, the XOSCn will be running when
a peripheral is requesting the clock. If ONDEMAND is zero, the clock source will always be running in
standby sleep mode.

Bit 2 – XTALEN Crystal Oscillator Enable
This bit controls the connections between the I/O pads and the external clock or crystal oscillator XOSCn:
0: External clock connected on XIN. XOUT can be used as general-purpose I/O.
1: Crystal connected to XIN/XOUT.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 797
                                       SAM D5x/E5x Family Data Sheet
                                                   OSCCTRL – Oscillators Controller

Bit 1 – ENABLE Oscillator Enable
0: The oscillator XOSCn is disabled.
1: The oscillator XOSCn is enabled.




© 2019 Microchip Technology Inc.       Datasheet                    DS60001507E-page 798
                                                                 SAM D5x/E5x Family Data Sheet
                                                                              OSCCTRL – Oscillators Controller

28.8.7         DFLL48M Control A

               Name:       DFLLCTRLA
               Offset:     0x1C
               Reset:      0x82
               Property:   PAC Write-Protection


         Bit         7            6            5             4            3            2             1            0
                ONDEMAND      RUNSTDBY                                                            ENABLE
   Access          R/W           R/W                                                                R/W
    Reset            1            0                                                                  1


               Bit 7 – ONDEMAND On Demand Control
               The On Demand operation mode allows the DFLL to be enabled or disabled depending on peripheral
               clock requests.
               If On Demand is set, the DFLL will only be running when requested by a peripheral and enabled
               (DFLLTRLA. ENABLE=1). If there is no peripheral requesting the DFLL’s clock source, the DFLL will be in
               a disabled state.
               If On Demand is disabled the DFLL will always be running when enabled (DFLLTRLA.ENABLE=1). In
               standby sleep mode, the On Demand operation is still active.
               0: The DFLL is always on.
               1: The DFLL is running when a peripheral is requesting the DFLL to be used as a clock source. The DFLL
               is not running if no peripheral is requesting the clock source.

               Bit 6 – RUNSTDBY Run in Standby
               This bit controls how the DFLL behaves during standby sleep mode:
               0: The DFLL is not running in standby sleep mode if no peripheral requests the clock.
               1: The DFLL is running in standby sleep mode. If ONDEMAND is one, the DFLL will be running when a
               peripheral is requesting the clock. If ONDEMAND is zero, the clock source will always be running in
               standby sleep mode.

               Bit 1 – ENABLE DFLL Enable
               0: The DFLL oscillator is disabled.
               1: The DFLL oscillator is enabled.
               Note: This bit is write-synchronized: Due to synchronization, there is delay from updating the register
               until the peripheral is enabled/disabled. The value written to DFLLCTRLA.ENABLE will read back
               immediately after written.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 799
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                     OSCCTRL – Oscillators Controller

28.8.8         DFLL48M Control B

               Name:        DFLLCTRLB
               Offset:      0x20
               Reset:       0x00
               Property:    Read-Synchronized


         Bit         7             6              5             4              3            2        1            0
                 WAITLOCK       BPLCKC         QLDIS          CCDIS        USBCRM         LLAW     STABLE       MODE
   Access           R/W           R/W           R/W            R/W           R/W           R/W      R/W          R/W
    Reset            0             0              0             0              0            0        0            0


               Bit 7 – WAITLOCK Wait Lock
               This bit controls the DFLL output clock, depending on lock status:
               0: Output clock before the DFLL is locked.
               1: Output clock when DFLL is locked (Fine lock).

               Bit 6 – BPLCKC Bypass Coarse Lock
               This bit controls the coarse lock procedure:
               0: Bypass coarse lock is disabled.
               1: Bypass coarse lock is enabled.

               Bit 5 – QLDIS Quick Lock Disable
               0: Quick Lock is enabled.
               1: Quick Lock is disabled.

               Bit 4 – CCDIS Chill Cycle Disable
               0: Chill Cycle is enabled.
               1: Chill Cycle is disabled.

               Bit 3 – USBCRM USB Clock Recovery Mode
               0: USB Clock Recovery Mode is disabled.
               1: USB Clock Recovery Mode is enabled.

               Bit 2 – LLAW Lose Lock After Wake
               0: Locks will not be lost after waking up from sleep modes if the DFLL clock has been stopped.
               1: Locks will be lost after waking up from sleep modes if the DFLL clock has been stopped.

               Bit 1 – STABLE Stable DFLL Frequency
               0: FINE calibration tracks changes in output frequency.
               1: FINE calibration register value will be fixed after a fine lock.

               Bit 0 – MODE Operating Mode Selection
               0: The DFLL operates in open-loop operation.
               1: The DFLL operates in closed-loop operation.




           © 2019 Microchip Technology Inc.                           Datasheet                       DS60001507E-page 800
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                         OSCCTRL – Oscillators Controller

28.8.9         DFLL48M Value

               Name:       DFLLVAL
               Offset:     0x24
               Reset:      0x0000XXXX
               Property:   PAC Write-Protection, Read-Synchronized, Write-Synchronized


         Bit        31           30           29                 28                27          26        25           24
                                                                      DIFF[15:8]
   Access           R             R           R                  R                 R           R         R            R
    Reset           0             0            0                 0                  0           0        0            0


         Bit        23           22           21                 20                19          18        17           16
                                                                      DIFF[7:0]
   Access           R             R           R                  R                 R           R         R            R
    Reset           0             0            0                 0                  0           0        0            x


         Bit        15           14           13                 12                11          10        9            8
                                                   COARSE[5:0]
   Access          R/W          R/W           R/W            R/W                   R/W         R/W
    Reset           0             0            0                 0                  0           x


         Bit        7             6            5                 4                  3           2        1            0
                                                                      FINE[7:0]
   Access          R/W          R/W           R/W            R/W                   R/W         R/W      R/W          R/W
    Reset           0             0            0                 0                  0           0        0            x


               Bits 31:16 – DIFF[15:0] Multiplication Ratio Difference
               In closed-loop mode (DFLLCTRLB.MODE is written to one), this bit group indicates the difference
               between the ideal number of DFLL cycles and the counted number of cycles. This value is not updated in
               open-loop mode, and should be considered invalid in that case.

               Bits 15:10 – COARSE[5:0] Coarse Value
               Set the value of the Coarse Calibration register. In closed-loop mode, this field is read-only.
               The DFLL48M is factory-calibrated for 48MHz. Register DFLLVAL.COARSE stores the coarse frequency
               calibration after reset.

               Bits 7:0 – FINE[7:0] Fine Value
               Set the value of the Fine Calibration register. In closed-loop mode, this field is read-only.
               The DFLL48M is factory-calibrated for 48MHz. Register DFLLVAL.FINE stores the coarse frequency
               calibration after reset.




           © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 801
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                       OSCCTRL – Oscillators Controller

28.8.10 DFLL48M Multiplier

           Name:        DFLLMUL
           Offset:      0x28
           Reset:       0x00000000
           Property:    PAC Write-Protection, Write-Synchronized


     Bit        31            30            29                28                 27          26        25           24
                                                 CSTEP[5:0]
  Access        R/W          R/W           R/W                R/W                R/W         R/W
   Reset         0             0             0                 0                  0           0


     Bit        23            22            21                20                 19          18        17           16
                                                                    FSTEP[7:0]
  Access        R/W          R/W           R/W                R/W                R/W         R/W      R/W          R/W
   Reset         0             0             0                 0                  0           0        0            0


     Bit        15            14            13                12                 11          10        9            8
                                                                    MUL[15:8]
  Access        R/W          R/W           R/W                R/W                R/W         R/W      R/W          R/W
   Reset         0             0             0                 0                  0           0        0            0


     Bit         7             6             5                 4                  3           2        1            0
                                                                     MUL[7:0]
  Access        R/W          R/W           R/W                R/W                R/W         R/W      R/W          R/W
   Reset         0             0             0                 0                  0           0        0            0


           Bits 31:26 – CSTEP[5:0] Coarse Maximum Step
           This bit group indicates the maximum step size allowed during coarse adjustment in closed-loop mode.
           When adjusting to a new frequency, the expected output frequency overshoot depends on this step size.

           Bits 23:16 – FSTEP[7:0] Fine Maximum Step
           This bit group indicates the maximum step size allowed during fine adjustment in closed-loop mode.
           When adjusting to a new frequency, the expected output frequency overshoot depends on this step size.

           Bits 15:0 – MUL[15:0] DFLL Multiply Factor
           This field determines the ratio of the CLK_DFLL output frequency to the CLK_DFLL_REF input frequency.
           Writing to the MUL bits will cause locks to be lost and the fine calibration value to be reset to its midpoint.




       © 2019 Microchip Technology Inc.                                Datasheet                        DS60001507E-page 802
                                                            SAM D5x/E5x Family Data Sheet
                                                                           OSCCTRL – Oscillators Controller

28.8.11 DFLL48M Synchronization

           Name:       DFLLSYNC
           Offset:     0x2C
           Reset:      0x00


     Bit         7            6            5            4            3             2            1              0
                                                     DFLLMUL      DFLLVAL     DFLLCTRLB      ENABLE
  Access                                                R            R            R             R
   Reset                                                0            0             0            0


           Bit 4 – DFLLMUL DFLLMUL Synchronization Busy
           This bit is cleared when the synchronization of DFLLMUL register between the clock domains is
           complete.
           This bit is set when the synchronization of DFLLMUL register between clock domains is started.
           The DFLLMUL synchronization only applies for write operations.

           Bit 3 – DFLLVAL DFLLVAL Synchronization Busy
           This bit is cleared when the synchronization of DFLLVAL register between the clock domains is complete.
           This bit is set when the synchronization of DFLLVAL register between clock domains is started.
           The DFLLVAL synchronization applies for read and write operations.

           Bit 2 – DFLLCTRLB DFLLCTRLB Synchronization Busy
           This bit is cleared when the synchronization of DFLLCTRLB register between the clock domains is
           complete.
           This bit is set when the synchronization of DFLLCTRLB register between clock domains is started.
           The DFLLCTRLB synchronization only applies for write operations.

           Bit 1 – ENABLE ENABLE Synchronization Busy
           This bit is cleared when the synchronization of ENABLE register bit between the clock domains is
           complete.
           This bit is set when the synchronization of ENABLE register bit between clock domains is started.




       © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 803
                                                          SAM D5x/E5x Family Data Sheet
                                                                        OSCCTRL – Oscillators Controller

28.8.12 DPLL Control A

           Name:       DPLLCTRLA
           Offset:     0x30 + n*0x14 [n=0..1]
           Reset:      0x80
           Property:   PAC Write-Protection, Write-Synchronized(ENABLE), Enable-Protected (ONDEMAND,
                       RUNSTDBY)


     Bit        7             6           5           4            3            2            1           0
            ONDEMAND     RUNSTDBY                                                         ENABLE
  Access       R/W          R/W                                                            R/W
   Reset        1             0                                                              0


           Bit 7 – ONDEMAND On Demand Control
           The On Demand operation mode allows the DPLLn to be enabled or disabled, depending on peripheral
           clock requests.
           If On Demand is set, the DPLLn will be running only when requested by a peripheral and enabled
           (DPLLnCTRLA. ENABLE=1). If there is no peripheral requesting the DPLLn’s clock source, the DPLLn
           will be in a disabled state.
           If On Demand is cleared, the DPLLn will always be running when enabled (DPLLnCTRLA.ENABLE=1).
           In standby sleep mode, the On Demand operation is still active.
           0: The DPLLn is always running.
           1: The DPLLn is running when a peripheral is requesting the DPLLn to be used as a clock source. The
           DPLLn is not running if no peripheral is requesting the clock source.

           Bit 6 – RUNSTDBY Run in Standby
           This bit controls how the DPLLn behaves during standby sleep mode:
           0: The DPLLn is not running in standby sleep mode if no peripheral requests the clock.
           1: The DPLLn is running in standby sleep mode. If ONDEMAND is one, the DPLLn will be running when a
           peripheral is requesting the clock. If ONDEMAND is zero, the clock source will always be running in
           standby sleep mode.

           Bit 1 – ENABLE DPLL Enable
           0: The DPLLn is disabled.
           1: The DPLLn is enabled.
           The software operation of enabling or disabling the DPLLn takes a few clock cycles, so the
           DPLLnSYNCBUSY. ENABLE status bit indicates when the DPLLn is successfully enabled or disabled.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 804
                                                              SAM D5x/E5x Family Data Sheet
                                                                               OSCCTRL – Oscillators Controller

28.8.13 DPLL Ratio Control

           Name:        DPLLRATIO
           Offset:      0x34 + n*0x14 [n=0..1]
           Reset:       0x00000000
           Property:    PAC Write-Protection, Write-Synchronized

           Refer to the Synchronization section in the Clock System Overview chapter for details on the functionality
           of this register.

     Bit        31            30           29            28              27           26          25           24


  Access
   Reset


     Bit        23            22           21            20              19           18          17           16
                                                                                 LDRFRAC[4:0]
  Access                                                R/W              R/W         R/W         R/W          R/W
   Reset                                                 0                0           0           0             0


     Bit        15            14           13            12              11           10          9             8
                                                                                   LDR[12:8]
  Access                                                R/W              R/W         R/W         R/W          R/W
   Reset                                                 0                0           0           0             0


     Bit         7            6             5            4                3           2           1             0
                                                              LDR[7:0]
  Access       R/W           R/W           R/W          R/W              R/W         R/W         R/W          R/W
   Reset         0            0             0            0                0           0           0             0


           Bits 20:16 – LDRFRAC[4:0] Loop Divider Ratio Fractional Part
           Write these bits to set the fractional part of the frequency multiplier. Due to synchronization there is a
           delay between writing to DPLLnRATIO.LDRFRAC[4:0] and the effect on the DPLLn output clock. The
           value written DPLLnRATIO.LDRFRAC[4:0] will be read back immediately and the DPLLRATIO bit in the
           synchronization busy register, DPLLnSYNCBUSY.DPLLRATIO, will be set.
           DPLLnSYNCBUSY.DPLLRATIO will be cleared when the operation is completed.

           Bits 12:0 – LDR[12:0] Loop Divider Ratio
           Write these bits to set the integer part of the frequency multiplier. The value written
           DPLLnRATIO.LDR[3:0] will be read back immediately and the DPLLRATIO bit in the synchronization busy
           register, DPLLnSYNCBUSY.DPLLRATIO, will be set. DPLLnSYNCBUSY.DPLLRATIO will be cleared
           when the operation is completed.




       © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 805
                                                               SAM D5x/E5x Family Data Sheet
                                                                                OSCCTRL – Oscillators Controller

28.8.14 DPLL Control B

           Name:       DPLLCTRLB
           Offset:     0x38 + n*0x14 [n=0..1]
           Reset:      0x00000020
           Property:   PAC Write-Protection, Enable-Protected


     Bit         31          30             29            28              27          26                  25           24
                                                                                                    DIV[10:8]
  Access                                                                              R/W                 R/W         R/W
   Reset                                                                               0                   0           0


     Bit         23          22             21            20              19          18                  17           16
                                                               DIV[7:0]
  Access         R/W         R/W            R/W          R/W              R/W         R/W                 R/W         R/W
   Reset          0           0              0            0                0           0                   0           0


     Bit         15          14             13            12              11          10                   9           8
              DCOEN                    DCOFILTER[2:0]                 LBYPASS                       LTIME[2:0]
  Access         R/W         R/W            R/W          R/W              R/W         R/W                 R/W         R/W
   Reset          0           0              0            0                0           0                   0           0


     Bit          7           6              5            4                3           2                   1           0
                         REFCLK[2:0]                     WUF                                FILTER[3:0]
  Access         R/W         R/W            R/W          R/W              R/W         R/W                 R/W         R/W
   Reset          0           0              1            0                0           0                   0           0


           Bits 26:16 – DIV[10:0] Clock Divider
           These bits are used to set the XOSC clock division factor and can be calculated with following formula:
                     �XOSC
           �DIV =
                  2 × DIV + 1

           Bit 15 – DCOEN DCO Filter Enable
           0: Disable DCO filter controller. Sigma-Delta DAC is automatically set the PLL itself.
           1: Enable DCO filter controller. DCOFILTER[2:0] is used to select sigma-delta DAC filter bandwidth.

           Bits 14:12 – DCOFILTER[2:0] Sigma-Delta DCO Filter Selection
           These bits select the DPLLn sigma-delta DCO filter type, as shown in the table below:
           Table 28-8. Sigma-delta DCO Filter selection

           DCOFILTER[2:0]                         Capacitor (pF)                      Bandwidth Fn (MHz)
           0x0                                    0.5                                 3.21
           0x1                                    1                                   1.6
           0x2                                    1.5                                 1.1
           0x3                                    2                                   0.8
           0x4                                    2.5                                 0.64




       © 2019 Microchip Technology Inc.                         Datasheet                                  DS60001507E-page 806
                                                   SAM D5x/E5x Family Data Sheet
                                                                OSCCTRL – Oscillators Controller

...........continued
 DCOFILTER[2:0]                      Capacitor (pF)                      Bandwidth Fn (MHz)
 0x5                                 3                                   0.55
 0x6                                 3.5                                 0.45
 0x7                                 4                                   0.4

Bit 11 – LBYPASS Lock Bypass

Bits 10:8 – LTIME[2:0] Lock Time
Write these bits to select the lock time-out value, as shown in the figure below:
Value       Name                      Description
0x0         Default                   No time-out. Automatic lock.
0x1         Reserved
0x2         Reserved
0x3         Reserved
0x4         800US                     Time-out if no lock within 800 us
0x5         900US                     Time-out if no lock within 900 us
0x6         1MS                       Time-out if no lock within 1 ms
0x7         1P1MS                     Time-out if no lock within 1.1 ms

Bits 7:5 – REFCLK[2:0] Reference Clock Selection
Write these bits to select the DPLLn clock reference, as shown in the table below:
Value       Name                  Description
0x0         GCLK                  Dedicated GCLK clock reference
0x1         XOSC32                XOSC32K clock reference (default)
0x2         XOSC0                 XOSC0 clock reference
0x3         XOSC1                 XOSC1 clock reference
Other       -                     Reserved

Bit 4 – WUF Wake Up Fast
0: DPLLn clock is output after startup and lock time.
1: DPLLn clock is output after startup time.

Bits 3:0 – FILTER[3:0] Proportional Integral Filter Selection
These bits select the DPLLn digital filter type, as shown in the table below:
Table 28-9. Proportional Integral Filter selection

 FILTER[3:0]                         PLL Bandwidth (fn)                  Damping Factor
 0x0                                 92.7 kHz                            0.76
 0x1                                 131 kHz                             1.08
 0x2                                 46.4 kHz                            0.38
 0x3                                 65.6 kHz                            0.54
 0x4                                 131 kHz                             0.56
 0x5                                 185 kHz                             0.79




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 807
                                              SAM D5x/E5x Family Data Sheet
                                                            OSCCTRL – Oscillators Controller

...........continued
 FILTER[3:0]                       PLL Bandwidth (fn)             Damping Factor
 0x6                               65.6 kHz                       0.28
 0x7                               92.7 kHz                       0.39
 0x8                               46.4 kHz                       1.49
 0x9                               65.6 kHz                       2.11
 0xA                               23.2 kHz                       0.75
 0xB                               32.8 kHz                       1.06
 0xC                               65.6 kHz                       1.07
 0xD                               92.7 kHz                       1.51
 0xE                               32.8 kHz                       0.53
 0xF                               46.4 kHz                       0.75




© 2019 Microchip Technology Inc.                Datasheet                    DS60001507E-page 808
                                                           SAM D5x/E5x Family Data Sheet
                                                                        OSCCTRL – Oscillators Controller

28.8.15 DPLL Synchronization Busy

           Name:       DPLLSYNCBUSY
           Offset:     0x3C + n*0x14 [n=0..1]
           Reset:      0x00000000


     Bit        31           30           29          28           27           26           25              24


  Access
   Reset


     Bit        23           22           21          20           19           18           17              16


  Access
   Reset


     Bit        15           14           13          12           11           10           9               8


  Access
   Reset


     Bit        7             6           5            4            3            2           1               0
                                                                            DPLLRATIO     ENABLE
  Access                                                                        R            R
   Reset                                                                         0           0


           Bit 2 – DPLLRATIO DPLL Loop Divider Ratio Synchronization Status
           0: The DPLLRATIO register has been synchronized.
           1: The DPLLRATIO register value has changed and its synchronization is in progress.

           Bit 1 – ENABLE DPLL Enable Synchronization Status
           0: The DPLLnCTRLA.ENABLE bit has been synchronized.
           1: The DPLLnCTRLA.ENABLE bit value has changed and its synchronization is in progress.




       © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 809
                                                            SAM D5x/E5x Family Data Sheet
                                                                        OSCCTRL – Oscillators Controller

28.8.16 DPLL Status

           Name:       DPLLSTATUS
           Offset:     0x40 + n*0x14 [n=0..1]
           Reset:      0x00000000


     Bit        31           30           29           28          27           26           25           24


  Access
   Reset


     Bit        23           22           21           20          19           18           17           16


  Access
   Reset


     Bit        15           14           13           12          11           10            9            8


  Access
   Reset


     Bit        7             6           5            4            3            2            1            0
                                                                                           CLKRDY        LOCK
  Access                                                                                     R            R
   Reset                                                                                      0            0


           Bit 1 – CLKRDY DPLL Clock Ready
           0: The DPLLn output clock is off.
           1: The DPLLn output clock in on.

           Bit 0 – LOCK DPLL Lock Status
           0: The DPLLn Lock signal is cleared, when the DPLLn is disabled or when the DPLLn is trying to reach
           the target frequency.
           1: The DPLLn Lock signal is asserted when the desired frequency is reached.




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 810
