# 46. AC – Analog Comparators

*Source: `Atmel-SAMD51.pdf`, pages 1640-1670 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                               AC – Analog Comparators


46.    AC – Analog Comparators

46.1   Overview
       The Analog Comparator (AC) supports two individual comparators. Each comparator (COMP) compares
       the voltage levels on two inputs, and provides a digital output based on this comparison. Each
       comparator may be configured to generate interrupt requests and/or peripheral events upon several
       different combinations of input change.
       Hysteresis can be adjusted to achieve the optimal operation for each application.
       The input selection includes four shared analog port pins and several internal signals. Each Comparator
       Output state can also be output on a pin for use by external devices.
       The comparators are grouped in pairs on each port. The AC peripheral implements one pair of
       comparators . These are called Comparator 0 (COMP0) and Comparator 1 (COMP1) . They have
       identical behaviors, but separate Control registers. The pair can be set in Window mode to compare a
       signal to a voltage range instead of a single voltage level.



46.2   Features
         •   Up to Two individual comparators
         •   Selectable hysteresis: 3-level On, or Off
         •   Hysteresis: On or Off
         •   Analog comparator outputs available on pins
               – Asynchronous or synchronous
         •   Flexible input selection:
               – Four pins selectable for positive or negative inputs
               – Ground (for zero crossing)
               – Bandgap reference voltage
               – 64-level programmable VDD scaler per comparator
               – DAC
         •   Interrupt generation on:
               – Rising or falling edge
               – Toggle
               – End of comparison
         •   Window function interrupt generation on:
               – Signal above window
               – Signal inside window
               – Signal below window
               – Signal outside window
         •   Event generation on:
               – Comparator output
               – Window function inside/outside window
         •   Optional digital filter on comparator output




       © 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 1640
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                        AC – Analog Comparators


46.3     Block Diagram
         Figure 46-1. Analog Comparator Block Diagram

           AIN0
                                                      +

                                                                                                               CMP0
                                                          COMP0
           AIN1

                                                      -             HYSTERESIS
           VDD
                                                                                                              INTERRUPTS
           SCALER
                                                           ENABLE                               INTERRUPT
                                                                       INTERRUPT MODE           SENSITIVITY
           DAC                                                                                   CONTROL
                                                          COMPCTRLn               WINCTRL            &        EVENTS
                                                                                                  WINDOW
                                                           ENABLE                                FUNCTION     GCLK_AC
           BANDGAP

                                                                    HYSTERESIS
           AIN2                                       +

                                                                                                               CMP1
                                                          COMP1
           AIN3
                                                      -




46.4     Signal Description
          Signal                        Description                        Type
          AIN[3..0]                     Analog input                       Comparator inputs
          CMP[1..0]                     Digital output                     Comparator outputs

         Refer to I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One signal
         can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



46.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

46.5.1   I/O Lines
         Using the AC’s I/O lines requires the I/O pins to be configured. Refer to PORT - I/O Pin Controller for
         details.




         © 2019 Microchip Technology Inc.                           Datasheet                     DS60001507E-page 1641
                                                              SAM D5x/E5x Family Data Sheet
                                                                                    AC – Analog Comparators

         Table 46-1. I/O Lines

          Instance                  Signal         I/O Line           Peripheral Function
          AC0                       AIN0           PAxx               A
          AC0                       AIN1           PAxx               A
          AC0                       AIN2           PAxx               A
          AC0                       AIN3           PAxx               A
          AC0                       CMP0           PAxx               A
          AC0                       CMP1           PAxx               A

         Related Links
         32. PORT - I/O Pin Controller

46.5.2   Power Management
         The AC will continue to operate in any Sleep mode where the selected source clock is running. The AC’s
         interrupts can be used to wake up the device from Sleep modes. Events connected to the Event System
         can trigger other operations in the system without exiting Sleep modes.

46.5.3   Clocks
         The AC bus clock (CLK_AC_APB) can be enabled and disabled in the Main Clock module, MCLK (see
         MCLK - Main Clock, and the default state of CLK_AC_APB can be found in Peripheral Clock Masking.
         A generic clock (GCLK_AC) is required to clock the AC. This clock must be configured and enabled in the
         generic clock controller before using the AC. Refer to the Generic Clock Controller chapter for details.
         This generic clock is asynchronous to the bus clock (CLK_AC_APB). Due to this asynchronicity, writes to
         certain registers will require synchronization between the clock domains. Refer to Synchronization for
         further details.
         Related Links
         15.6.2.6 Peripheral Clock Masking
         15. MCLK – Main Clock

46.5.4   DMA
         Not applicable.

46.5.5   Interrupts
         The interrupt request lines are connected to the interrupt controller. Using the AC interrupts requires the
         interrupt controller to be configured first. Refer to Nested Vector Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

46.5.6   Events
         The events are connected to the Event System. Refer to EVSYS – Event System for details on how to
         configure the Event System.
         Related Links
         31. EVSYS – Event System




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1642
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     AC – Analog Comparators

46.5.7    Debug Operation
          When the CPU is halted in debug mode, the AC will halt normal operation after any on-going comparison
          is completed. The AC can be forced to continue normal operation during debugging. Refer to DBGCTRL
          for details. If the AC is configured in a way that requires it to be periodically serviced by the CPU through
          interrupts or similar, improper operation or data loss may result during debugging.

46.5.8    Register Access Protection
          All registers with write access can be write-protected optionally by the Peripheral Access Controller
          (PAC), except for the following registers:
           • Control B register (CTRLB)
           • Interrupt Flag register (INTFLAG)
          Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
          Protection" property in each individual register description.
          PAC write protection does not apply to accesses through an external debugger.
          Related Links
          27. PAC - Peripheral Access Controller

46.5.9    Analog Connections
          Each comparator has up to four I/O pins that can be used as analog inputs. Each pair of comparators
          shares the same four pins. These pins must be configured for analog operation before using them as
          comparator inputs.
          Any internal reference source, such as a bandgap voltage reference, or DAC must be configured and
          enabled prior to its use as a comparator input.

46.5.10 Calibration
          The BIAS calibration value from the production test must be loaded from the NVM Software Calibration
          Area into the AC Calibration register (CALIB) by software to achieve specified accuracy.



46.6      Functional Description

46.6.1    Principle of Operation
          Each comparator has one positive input and one negative input. Each positive input may be chosen from
          a selection of analog input pins. Each negative input may be chosen from a selection of both analog input
          pins and internal inputs, such as a bandgap voltage reference.
          The digital output from the comparator is '1' when the difference between the positive and the negative
          input voltage is positive, and '0' otherwise.
          The individual comparators can be used independently (Normal mode) or paired to form a window
          comparison (Window mode).

46.6.2    Basic Operation

46.6.2.1 Initialization
          Some registers are enable-protected, meaning they can only be written when the module is disabled.
          The following register is enable-protected:




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1643
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     AC – Analog Comparators

          • Event Control register (EVCTRL)
         Enable-protection is denoted by the "Enable-Protected" property in each individual register description.
46.6.2.2 Enabling, Disabling and Resetting
         The AC is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The AC is
         disabled writing a '0' to CTRLA.ENABLE.
         The AC is reset by writing a '1' to the Software Reset bit in the Control A register (CTRLA.SWRST). All
         registers in the AC will be reset to their initial state, and the AC will be disabled. Refer to CTRLA for
         details.
46.6.2.3 Comparator Configuration
         Each individual comparator must be configured by its respective Comparator Control register
         (COMPCTRLx) before that comparator is enabled. These settings cannot be changed while the
         comparator is enabled.
          • Select the desired measurement mode with COMPCTRLx.SINGLE. See Starting a Comparison for
            more details.
          • Select the desired hysteresis with COMPCTRLx.HYSTEN and COMPCTRLx.HYST. See Input
            Hysteresis for more details.
          • Write COMPCTRLx.SPEED to 0x3.
          • Select the interrupt source with COMPCTRLx.INTSEL.
          • Select the positive and negative input sources with the COMPCTRLx.MUXPOS and
            COMPCTRLx.MUXNEG bits. See Selecting Comparator Inputs for more details.
          • Select the filtering option with COMPCTRLx.FLEN.
          • Select standby operation with Run in Standby bit (COMPCTRLx.RUNSTDBY).
         The individual comparators are enabled by writing a '1' to the Enable bit in the Comparator x Control
         registers (COMPCTRLx.ENABLE). The individual comparators are disabled by writing a '0' to
         COMPCTRLx.ENABLE. Writing a '0' to CTRLA.ENABLE will also disable all the comparators, but will not
         clear their COMPCTRLx.ENABLE bits.
46.6.2.4 Starting a Comparison
         Each comparator channel can be in one of two different measurement modes, determined by the Single
         bit in the Comparator x Control register (COMPCTRLx.SINGLE):
          • Continuous measurement
          • Single-shot
         After being enabled, a start-up delay is required before the result of the comparison is ready. This start-up
         time is measured automatically to account for environmental changes, such as temperature or voltage
         supply level, and is specified in the Electrical Characteristics chapters. During the start-up time, the
         COMP output is not available.
         The comparator can be configured to generate interrupts when the output toggles, when the output
         changes from '0' to '1' (rising edge), when the output changes from '1' to '0' (falling edge) or at the end of
         the comparison. An end-of-comparison interrupt can be used with the Single-Shot mode to chain further
         events in the system, regardless of the state of the comparator outputs. The Interrupt mode is set by the
         Interrupt Selection bit group in the Comparator Control register (COMPCTRLx.INTSEL). Events are
         generated using the comparator output state, regardless of whether the interrupt is enabled or not.




        © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1644
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                    AC – Analog Comparators

46.6.2.4.1 Continuous Measurement
          Continuous measurement is selected by writing COMPCTRLx.SINGLE to zero. In continuous mode, the
          comparator is continuously enabled and performing comparisons. This ensures that the result of the
          latest comparison is always available in the Current State bit in the Status A register (STATUSA.STATEx).
          After the start-up time has passed, a comparison is done and STATUSA is updated. The Comparator x
          Ready bit in the Status B register (STATUSB.READYx) is set, and the appropriate peripheral events and
          interrupts are also generated. New comparisons are performed continuously until the
          COMPCTRLx.ENABLE bit is written to zero. The start-up time applies only to the first comparison.
          In continuous operation, edge detection of the comparator output for interrupts is done by comparing the
          current and previous sample. The sampling rate is the GCLK_AC frequency. An example of continuous
          measurement is shown in the Figure 46-2.
          Figure 46-2. Continuous Measurement Example
                   GCLK_AC
                            Write ‘1’
          COMPCTRLx.ENABLE                  2-3 cycles

                                                         tSTARTUP
            STATUSB.READYx

                    Sampled
            Comparator Output


          For low-power operation, comparisons can be performed during sleep modes without a clock. The
          comparator is enabled continuously, and changes of the comparator state are detected asynchronously.
          When a toggle occurs, the Power Manager will start GCLK_AC to register the appropriate peripheral
          events and interrupts. The GCLK_AC clock is then disabled again automatically, unless configured to
          wake up the system from sleep.
46.6.2.4.2 Single-Shot
          Single-shot operation is selected by writing COMPCTRLx.SINGLE to '1'. During single-shot operation, the
          comparator is normally idle. The user starts a single comparison by writing '1' to the respective Start
          Comparison bit in the write-only Control B register (CTRLB.STARTx). The comparator is enabled, and
          after the start-up time has passed, a single comparison is done and STATUSA is updated. Appropriate
          peripheral events and interrupts are also generated. No new comparisons will be performed.
          Writing '1' to CTRLB.STARTx also clears the Comparator x Ready bit in the Status B register
          (STATUSB.READYx). STATUSB.READYx is set automatically by hardware when the single comparison
          has completed.
          A single-shot measurement can also be triggered by the Event System. Setting the Comparator x Event
          Input bit in the Event Control Register (EVCTRL.COMPEIx) enables triggering on incoming peripheral
          events. Each comparator can be triggered independently by separate events. Event-triggered operation is
          similar to user-triggered operation; the difference is that a peripheral event from another hardware module
          causes the hardware to automatically start the comparison and will not clear STATUSB.READYx.
          To detect an edge of the comparator output in single-shot operation for the purpose of interrupts, the
          result of the current measurement is compared with the result of the previous measurement (one
          sampling period earlier). An example of single-shot operation is shown in Figure 46-3.




         © 2019 Microchip Technology Inc.                           Datasheet                   DS60001507E-page 1645
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          AC – Analog Comparators

         Figure 46-3. Single-Shot Example
                 GCLK_AC
                          Write ‘1’                            Write ‘1’
            CTRLB.STARTx               2-3 cycles                            2-3 cycles

                                                    tSTARTUP                                 tSTARTUP
         STATUSB.READYx

                  Sampled
          Comparator Output


         For low-power operation, event-triggered measurements can be performed during sleep modes. When
         the event occurs, the Power Manager will start GCLK_AC. The comparator is enabled, and after the
         startup time has passed, a comparison is done and appropriate peripheral events and interrupts are also
         generated. The comparator and GCLK_AC are then disabled again automatically, unless configured to
         wake up the system from sleep.

46.6.3   Selecting Comparator Inputs
         Each comparator has one positive and one negative input. The positive input is one of the external input
         pins (AINx). The negative input can be fed either from an external input pin (AINx) or from one of the
         several internal reference voltage sources common to all comparators. The user selects the input source
         as follows:
           • The positive input is selected by the Positive Input MUX Select bit group in the Comparator Control
             register (COMPCTRLx.MUXPOS)
           • The negative input is selected by the Negative Input MUX Select bit group in the Comparator Control
             register (COMPCTRLx.MUXNEG)
         In the case of using an external I/O pin, the selected pin must be configured for analog use in the PORT
         Controller by disabling the digital input and output. The switching of the analog input multiplexers is
         controlled to minimize crosstalk between the channels. The input selection must be changed only while
         the individual comparator is disabled.
         Note: For internal use of the comparison results by the CCL, this bit must be 0x1 or 0x2.

46.6.4   Window Operation
         Each comparator pair can be configured to work together in Window mode. In this mode, a voltage range
         is defined, and the comparators give information about whether an input signal is within this range or not.
         Window mode is enabled by the Window Enable x bit in the Window Control register (WINCTRL.WENx).
         Both comparators in a pair must have the same measurement mode setting in their respective
         Comparator Control Registers (COMPCTRLx.SINGLE).
         To physically configure the pair of comparators for Window mode, the same I/O pin must be chosen as
         positive input for each comparator, providing a shared input signal. The negative inputs define the range
         for the window. In Figure 46-4, COMP0 defines the upper limit and COMP1 defines the lower limit of the
         window, as shown but the window will also work in the opposite configuration with COMP0 lower and
         COMP1 higher. The current state of the window function is available in the Window x State bit group of
         the Status register (STATUS.WSTATEx).
         Window mode can be configured to generate interrupts when the input voltage changes to below the
         window, when the input voltage changes to above the window, when the input voltage changes into the
         window or when the input voltage changes outside the window. The interrupt selections are set by the
         Window Interrupt Selection bit field in the Window Control register (WINCTRL.WINTSEL). Events are
         generated using the inside/outside state of the window, regardless of whether the interrupt is enabled or
         not. Note that the individual comparator outputs, interrupts and events continue to function normally
         during Window mode.




         © 2019 Microchip Technology Inc.                        Datasheet                              DS60001507E-page 1646
                                                          SAM D5x/E5x Family Data Sheet
                                                                                 AC – Analog Comparators

         When the comparators are configured for Window mode and Single-shot mode, measurements are
         performed simultaneously on both comparators. Writing '1' to either Start Comparison bit in the Control B
         register (CTRLB.STARTx) will start a measurement. Likewise either peripheral event can start a
         measurement.
         Figure 46-4. Comparators in Window Mode


                                                    +

                                                                                                         STATE0
                                                        COMP0

          UPPER LIMIT OF WINDOW                     -
                                                                                                        WSTATE[1:0]

                                                                                          INTERRUPT
                                                                                          SENSITIVITY
                                                                                                        INTERRUPTS
                                                                                           CONTROL
                      INPUT SIGNAL                                                             &
                                                                                            WINDOW
                                                                                           FUNCTION     EVENTS


                                                    +

                                                                                                         STATE1
                                                        COMP1

         LOWER LIMIT OF WINDOW                      -



46.6.5   VDD Scaler
         The VDD scaler generates a reference voltage that is a fraction of the device’s supply voltage, with 64
         levels. One independent voltage channel is dedicated for each comparator. The scaler of a comparator is
         enabled when the Negative Input Mux bit field or the Positive Input Mux in the respective Comparator
         Control register (COMPCTRLx) is set to VSCALE as an input and the comparator is enabled. The voltage
         of each channel is selected by the Value bit field in the SCALERx registers (SCALERx.VALUE).




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1647
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                   AC – Analog Comparators

         Figure 46-5. VDD Scaler


                                            COMPCTRLx.MUXNEG == 5      SCALERx.
                                                     OR                 VALUE
                                            COMPCTRLx.MUXPOS == 4
                                                                         6


                                                                                     to
                                                                                     COMPx




46.6.6   Input Hysteresis
         Application software can selectively enable/disable hysteresis for the comparison. Applying hysteresis will
         help prevent constant toggling of the output, which can be caused by noise when the input signals are
         close to each other.
         Hysteresis is enabled for each comparator individually by the Hysteresis Enable bit in the Comparator x
         Control register (COMPCTRLx.HYSTEN). Furthermore, when enabled, the level of hysteresis is
         programmable through the Hysteresis Level bits also in the Comparator x Control register
         (COMPCTRLx.HYST). Hysteresis is available only in Continuous mode (COMPCTRLx.SINGLE=0).

46.6.7   Filtering
         The output of the comparators can be filtered digitally to reduce noise. The filtering is determined by the
         Filter Length bits in the Comparator Control x register (COMPCTRLx.FLEN), and is independent for each
         comparator. Filtering is selectable from none, 3-bit majority (N=3) or 5-bit majority (N=5) functions. Any
         change in the comparator output is considered valid only if N/2+1 out of the last N samples agree. The
         filter sampling rate is the GCLK_AC frequency.
         Note that filtering creates an additional delay of N-1 sampling cycles from when a comparison is started
         until the comparator output is validated. For Continuous mode, the first valid output will occur when the
         required number of filter samples is taken. Subsequent outputs will be generated every cycle based on
         the current sample plus the previous N-1 samples, as shown in Figure 46-6. For Single-shot mode, the
         comparison completes after the Nth filter sample, as shown in Figure 46-7.
         Figure 46-6. Continuous Mode Filtering
            Sampling Clock

                 Sampled
         Comparator Output

              3-bit Majority
              Filter Output

              5-bit Majority
              Filter Output




         © 2019 Microchip Technology Inc.                           Datasheet                  DS60001507E-page 1648
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                         AC – Analog Comparators

         Figure 46-7. Single-Shot Filtering
            Sampling Clock


                      Start
                                            tSTARTUP
             3-bit Sampled
         Comparator Output

              3-bit Majority
              Filter Output

             5-bit Sampled
         Comparator Output

              5-bit Majority
              Filter Output

         During Sleep modes, filtering is supported only for single-shot measurements. Filtering must be disabled
         if continuous measurements will be done during Sleep modes, or the resulting interrupt/event may be
         generated incorrectly.

46.6.8   Comparator Output
         The output of each comparator can be routed to an I/O pin by setting the Output bit group in the
         Comparator Control x register (COMPCTRLx.OUT). This allows the comparator to be used by external
         circuitry. Either the raw, non-synchronized output of the comparator or the CLK_AC-synchronized version,
         including filtering, can be used as the I/O signal source. The output appears on the corresponding CMP[x]
         pin.

46.6.9   Offset Compensation
         The Swap bit in the Comparator Control registers (COMPCTRLx.SWAP) controls switching of the input
         signals to a comparator's positive and negative terminals. When the comparator terminals are swapped,
         the output signal from the comparator is also inverted, as shown in Figure 46-8. This allows the user to
         measure or compensate for the comparator input offset voltage. As part of the input selection,
         COMPCTRLx.SWAP can be changed only while the comparator is disabled.
         Figure 46-8. Input Swapping for Offset Compensation

                                                              +

                                     MUXPOS
                                                                  COMPx                           CMPx



                                                              -             HYSTERESIS

                                                                   ENABLE
                                                       SWAP
                                                                                 SWAP
                                      MUXNEG                      COMPCTRLx


46.6.10 DMA Operation
         Not applicable.

46.6.11 Interrupts
         The AC has the following interrupt sources:
           • Comparator (COMP0, COMP1): Indicates a change in comparator status.
           • Window (WIN0): Indicates a change in the window status.




         © 2019 Microchip Technology Inc.                          Datasheet                     DS60001507E-page 1649
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      AC – Analog Comparators

         Comparator interrupts are generated based on the conditions selected by the Interrupt Selection bit group
         in the Comparator Control registers (COMPCTRLx.INTSEL). Window interrupts are generated based on
         the conditions selected by the Window Interrupt Selection bit group in the Window Control register
         (WINCTRL.WINTSEL[1:0]).
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a one to the corresponding bit in the Interrupt Enable Set (INTENSET)
         register, and disabled by writing a one to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
         register. An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is
         enabled. The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or
         the AC is Reset. See INFLAG register for details on how to clear interrupt flags. All interrupt requests
         from the peripheral are ORed together on system level to generate one combined interrupt request to the
         NVIC. The user must read the INTFLAG register to determine which interrupt condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated.
         Related Links
         10.2 Nested Vector Interrupt Controller

46.6.12 Events
        The AC can generate the following output events:
           • Comparator (COMP0, COMP1): Generated as a copy of the comparator status
           • Window (WIN0): Generated as a copy of the window inside/outside status
         Writing a one to an Event Output bit in the Event Control Register (EVCTRL.xxEO) enables the
         corresponding output event. Writing a zero to this bit disables the corresponding output event. Refer to
         the Event System chapter for details on configuring the event system.
         The AC can take the following action on an input event:
           • Start comparison (START0, START1): Start a comparison.
         Writing a one to an Event Input bit into the Event Control register (EVCTRL.COMPEIx) enables the
         corresponding action on input event. Writing a zero to this bit disables the corresponding action on input
         event. Note that if several events are connected to the AC, the enabled action will be taken on any of the
         incoming events. Refer to the Event System chapter for details on configuring the event system.
         When EVCTRL.COMPEIx is one, the event will start a comparison on COMPx after the start-up time
         delay. In normal mode, each comparator responds to its corresponding input event independently. For a
         pair of comparators in window mode, either comparator event will trigger a comparison on both
         comparators simultaneously.

46.6.13 Sleep Mode Operation
        The Run in Standby bits in the Comparator x Control registers (COMPCTRLx.RUNSTDBY) control the
        behavior of the AC during standby sleep mode. Each RUNSTDBY bit controls one comparator. When the
        bit is zero, the comparator is disabled during sleep, but maintains its current configuration. When the bit is
        one, the comparator continues to operate during sleep. Note that when RUNSTDBY is zero, the analog
        blocks are powered off for the lowest power consumption. This necessitates a start-up time delay when
        the system returns from sleep.
         For Window Mode operation, both comparators in a pair must have the same RUNSTDBY configuration.




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1650
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                           AC – Analog Comparators

         When RUNSTDBY is one, any enabled AC interrupt source can wake up the CPU. The AC can also be
         used during sleep modes where the clock used by the AC is disabled, provided that the AC is still
         powered (not in shutdown). In this case, the behavior is slightly different and depends on the
         measurement mode, as listed in Table 46-2.
         Table 46-2. Sleep Mode Operation

          COMPCTRLx.MODE RUNSTDBY=0                        RUNSTDBY=1
          0 (Continuous)                COMPx disabled GCLK_AC stopped, COMPx enabled
          1 (Single-shot)               COMPx disabled GCLK_AC stopped, COMPx enabled only when triggered by
                                                       an input event

46.6.13.1 Continuous Measurement during Sleep
         When a comparator is enabled in continuous measurement mode and GCLK_AC is disabled during
         sleep, the comparator will remain continuously enabled and will function asynchronously. The current
         state of the comparator is asynchronously monitored for changes. If an edge matching the interrupt
         condition is found, GCLK_AC is started to register the interrupt condition and generate events. If the
         interrupt is enabled in the Interrupt Enable registers (INTENCLR/SET), the AC can wake up the device;
         otherwise GCLK_AC is disabled until the next edge detection. Filtering is not possible with this
         configuration.
         Figure 46-9. Continuous Mode SleepWalking
                    GCLK_AC
                            Write ‘1’
         COMPCTRLx.ENABLE                   2-3 cycles

                                                         tSTARTUP
            STATUSB.READYx

                    Sampled
            Comparator Output



46.6.13.2 Single-Shot Measurement during Sleep
         For low-power operation, event-triggered measurements can be performed during sleep modes. When
         the event occurs, the Power Manager will start GCLK_AC. The comparator is enabled, and after the start-
         up time has passed, a comparison is done, with filtering if desired, and the appropriate peripheral events
         and interrupts are also generated, as shown in Figure 46-10. The comparator and GCLK_AC are then
         disabled again automatically, unless configured to wake the system from sleep. Filtering is allowed with
         this configuration.
         Figure 46-10. Single-Shot SleepWalking
             GCLK_AC

                                         tSTARTUP                               tSTARTUP
             Input Event


            Comparator
         Output or Event




46.6.14 Synchronization
        Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
        need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset bit in Control register (CTRLA.SWRST)




        © 2019 Microchip Technology Inc.                            Datasheet                      DS60001507E-page 1651
                                                 SAM D5x/E5x Family Data Sheet
                                                                        AC – Analog Comparators

  • Enable bit in Control register (CTRLA.ENABLE)
  • Enable bit in Comparator Control register (COMPCTRLn.ENABLE)
The following registers are synchronized when written:
  • Window Control register (WINCTRL)
Required write synchronization is denoted by the "Write-Synchronized" property in the register
description.
Related Links
13.3 Register Synchronization




© 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1652
                                                               SAM D5x/E5x Family Data Sheet
                                                                                              AC – Analog Comparators


46.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                                                                                ENABLE         SWRST
 0x01         CTRLB           7:0                                                                                START1         START0
                              7:0                                       WINEO0                                  COMPEO1       COMPEO0
 0x02         EVCTRL
                             15:8                          INVEI1        INVEI0                                 COMPEI1        COMPEI0
 0x04        INTENCLR         7:0                                          WIN0                                  COMP1          COMP0
 0x05        INTENSET         7:0                                          WIN0                                  COMP1          COMP0
 0x06        INTFLAG          7:0                                          WIN0                                  COMP1          COMP0
 0x07        STATUSA          7:0                             WSTATE0[1:0]                                       STATE1         STATE0
 0x08        STATUSB          7:0                                                                               READY1         READY0
 0x09        DBGCTRL          7:0                                                                                              DBGRUN
 0x0A        WINCTRL          7:0                                                                       WINTSEL0[1:0]           WEN0
 0x0B        Reserved
 0x0C        SCALER0          7:0                                                          VALUE[5:0]
 0x0D        SCALER1          7:0                                                          VALUE[5:0]
 0x0E
   ...       Reserved
 0x0F
                              7:0             RUNSTDBY                       INTSEL[1:0]          SINGLE         ENABLE
                             15:8      SWAP              MUXPOS[2:0]                                          MUXNEG[2:0]
 0x10       COMPCTRL0
                             23:16                              HYST[1:0]            HYSTEN                             SPEED[1:0]
                             31:24                              OUT[1:0]                                        FLEN[2:0]
                              7:0             RUNSTDBY                       INTSEL[1:0]          SINGLE         ENABLE
                             15:8      SWAP              MUXPOS[2:0]                                          MUXNEG[2:0]
 0x14       COMPCTRL1
                             23:16                              HYST[1:0]            HYSTEN                             SPEED[1:0]
                             31:24                              OUT[1:0]                                        FLEN[2:0]
 0x18
   ...       Reserved
 0x1F
                              7:0                                      COMPCTRL1 COMPCTRL0        WINCTRL        ENABLE         SWRST
                             15:8
 0x20       SYNCBUSY
                             23:16
                             31:24
                              7:0                                                                                       BIAS0[1:0]
 0x24          CALIB
                             15:8




46.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to Register Access Protection.




          © 2019 Microchip Technology Inc.                          Datasheet                                 DS60001507E-page 1653
                                                 SAM D5x/E5x Family Data Sheet
                                                                         AC – Analog Comparators

Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
refer to Synchronization.
Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1654
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                             AC – Analog Comparators

46.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection, Write-Synchronized


         Bit         7             6             5              4             3             2             1             0
                                                                                                       ENABLE        SWRST
   Access                                                                                                R/W            W
    Reset                                                                                                 0             0


               Bit 1 – ENABLE Enable
               Due to synchronization, there is delay from updating the register until the peripheral is enabled/disabled.
               The value written to CTRL.ENABLE will read back immediately and the corresponding bit in the
               Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE is cleared when
               the peripheral is enabled/disabled.
                Value      Description
                0          The AC is disabled.
                1          The AC is enabled. Each comparator must also be enabled individually by the Enable bit in
                           the Comparator Control register (COMPCTRLn.ENABLE).

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit resets all registers in the AC to their initial state, and the AC will be disabled.
               Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
               write-operation will be discarded.
               Due to synchronization, there is a delay from writing CTRLA.SWRST until the reset is complete.
               CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
               Value         Description
               0             There is no reset operation ongoing.
               1             The reset operation is ongoing.




           © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 1655
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                         AC – Analog Comparators

46.8.2         Control B

               Name:        CTRLB
               Offset:      0x01
               Reset:       0x00
               Property:    -


         Bit         7            6             5            4             3            2             1             0
                                                                                                   START1        START0
   Access                                                                                            R/W          R/W
    Reset                                                                                             0             0


               Bits 0, 1 – STARTx Comparator x Start Comparison
               Writing a '0' to this field has no effect.
               Writing a '1' to STARTx starts a single-shot comparison on COMPx if both the Single-Shot and Enable
               bits in the Comparator x Control Register are '1' (COMPCTRLx.SINGLE and COMPCTRLx.ENABLE). If
               comparator x is not implemented, or if it is not enabled in single-shot mode, Writing a '1' has no effect.
               This bit always reads as zero.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1656
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                         AC – Analog Comparators

46.8.3         Event Control

               Name:        EVCTRL
               Offset:      0x02
               Reset:       0x0000
               Property:    PAC Write-Protection, Enable-Protected


         Bit        15            14           13            12            11           10            9             8
                                              INVEI1       INVEI0                                 COMPEI1       COMPEI0
   Access                                      R/W          R/W                                      R/W          R/W
    Reset                                       0            0                                        0             0


         Bit         7            6             5            4             3             2            1             0
                                                          WINEO0                                  COMPEO1       COMPEO0
   Access                                                   R/W                                      R/W          R/W
    Reset                                                    0                                        0             0


               Bits 12, 13 – INVEIx Inverted Event Input Enable x
               Value       Description
               0           Incoming event is not inverted for comparator x.
               1           Incoming event is inverted for comparator x.

               Bits 8, 9 – COMPEIx Comparator x Event Input
               Note that several actions can be enabled for incoming events. If several events are connected to the
               peripheral, the enabled action will be taken for any of the incoming events. There is no way to tell which
               of the incoming events caused the action.
               These bits indicate whether a comparison will start or not on any incoming event.
                Value       Description
                0           Comparison will not start on any incoming event.
                1           Comparison will start on any incoming event.

               Bit 4 – WINEO0 Window 0 Event Output Enable
               These bits indicate whether the window 0 function can generate a peripheral event or not.
                Value      Description
                0          Window 0 Event is disabled.
                1          Window 0 Event is enabled.

               Bits 0, 1 – COMPEOx Comparator x Event Output Enable
               These bits indicate whether the comparator x output can generate a peripheral event or not.
                Value      Description
                0           COMPx event generation is disabled.
                1           COMPx event generation is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1657
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                          AC – Analog Comparators

46.8.4         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x04
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit         7            6             5            4             3              2          1            0
                                                            WIN0                                  COMP1        COMP0
   Access                                                   R/W                                     R/W          R/W
    Reset                                                    0                                       0            0


               Bit 4 – WIN0 Window 0 Interrupt Enable
               Reading this bit returns the state of the Window 0 interrupt enable.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit disables the Window 0 interrupt.
               Value         Description
               0             The Window 0 interrupt is disabled.
               1             The Window 0 interrupt is enabled.

               Bits 0, 1 – COMPx Comparator x Interrupt Enable
               Reading this bit returns the state of the Comparator x interrupt enable.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit disables the Comparator x interrupt.
               Value         Description
               0             The Comparator x interrupt is disabled.
               1             The Comparator x interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1658
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                            AC – Analog Comparators

46.8.5         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x05
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

         Bit         7             6             5              4             3             2                1           0
                                                              WIN0                                     COMP1           COMP0
   Access                                                     R/W                                           R/W         R/W
    Reset                                                       0                                            0           0


               Bit 4 – WIN0 Window 0 Interrupt Enable
               Reading this bit returns the state of the Window 0 interrupt enable.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit enables the Window 0 interrupt.
               Value         Description
               0             The Window 0 interrupt is disabled.
               1             The Window 0 interrupt is enabled.

               Bits 0, 1 – COMPx Comparator x Interrupt Enable
               Reading this bit returns the state of the Comparator x interrupt enable.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Ready interrupt bit and enable the Ready interrupt.
               Value         Description
               0             The Comparator x interrupt is disabled.
               1             The Comparator x interrupt is enabled.




           © 2019 Microchip Technology Inc.                          Datasheet                              DS60001507E-page 1659
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                         AC – Analog Comparators

46.8.6         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x06
               Reset:       0x00
               Property:    –


         Bit         7            6             5             4            3             2            1             0
                                                            WIN0                                   COMP1          COMP0
   Access                                                   R/W                                      R/W           R/W
    Reset                                                     0                                       0             0


               Bit 4 – WIN0 Window 0
               This flag is set according to the Window 0 Interrupt Selection bit group in the WINCTRL register
               (WINCTRL.WINTSELx) and will generate an interrupt if INTENCLR/SET.WINx is also one.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Window 0 interrupt flag.

               Bits 0, 1 – COMPx Comparator x
               Reading this bit returns the status of the Comparator x interrupt flag. If comparator x is not implemented,
               COMPx always reads as zero.
               This flag is set according to the Interrupt Selection bit group in the Comparator x Control register
               (COMPCTRLx.INTSEL) and will generate an interrupt if INTENCLR/SET.COMPx is also one.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Comparator x interrupt flag.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1660
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                      AC – Analog Comparators

46.8.7         Status A

               Name:       STATUSA
               Offset:     0x07
               Reset:      0x00
               Property:   -


         Bit         7            6            5                  4         3         2            1           0
                                                   WSTATE0[1:0]                                 STATE1       STATE0
   Access                                     R                   R                               R            R
    Reset                                      0                  0                                0           0


               Bits 5:4 – WSTATE0[1:0] Window 0 Current State
               These bits show the current state of the signal if the window 0 mode is enabled.
               These values may change in during startup and measurement cycles. When polling for sample
               completion use the STATUSB.READY bit to signal completion.
                Value      Name                       Description
                0x0        ABOVE                      Signal is above window
                0x1        INSIDE                     Signal is inside window
                0x2        BELOW                      Signal is below window
                0x3                                   Reserved

               Bits 0, 1 – STATEx Comparator x Current State
               This bit shows the current state of the output signal from COMPx. STATEx is valid only when
               STATUSB.READYx is one.




           © 2019 Microchip Technology Inc.                           Datasheet                   DS60001507E-page 1661
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                AC – Analog Comparators

46.8.8         Status B

               Name:       STATUSB
               Offset:     0x08
               Reset:      0x00
               Property:   -


         Bit         7            6             5            4             3    2       1            0
                                                                                      READY1      READY0
   Access                                                                               R            R
    Reset                                                                               0            0


               Bits 0, 1 – READYx Comparator x Ready
               This bit is cleared when the comparator x output is not ready.
               This bit is set when the comparator x output is ready.




           © 2019 Microchip Technology Inc.                       Datasheet             DS60001507E-page 1662
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    AC – Analog Comparators

46.8.9         Debug Control

               Name:       DBGCTRL
               Offset:     0x09
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5            4           3            2            1            0
                                                                                                          DBGRUN
   Access                                                                                                   R/W
    Reset                                                                                                     0


               Bit 0 – DBGRUN Debug Run
               This bit is not reset by a software reset.
               This bits controls the functionality when the CPU is halted by an external debugger.
                Value       Description
                0           The AC is halted when the CPU is halted by an external debugger. Any on-going comparison
                            will complete.
                1           The AC continues normal operation when the CPU is halted by an external debugger.




           © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 1663
                                                           SAM D5x/E5x Family Data Sheet
                                                                                 AC – Analog Comparators

46.8.10 Window Control

           Name:       WINCTRL
           Offset:     0x0A
           Reset:      0x00
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        7             6           5            4            3           2            1            0
                                                                                 WINTSEL0[1:0]          WEN0
  Access                                                                       R/W          R/W          R/W
   Reset                                                                        0            0            0


           Bits 2:1 – WINTSEL0[1:0] Window 0 Interrupt Selection
           These bits configure the interrupt mode for the comparator window 0 mode.
            Value      Name                    Description
            0x0        ABOVE                   Interrupt on signal above window
            0x1        INSIDE                  Interrupt on signal inside window
            0x2        BELOW                   Interrupt on signal below window
            0x3        OUTSIDE                 Interrupt on signal outside window

           Bit 0 – WEN0 Window 0 Mode Enable
           Value      Description
           0          Window mode is disabled for comparators 0 and 1.
           1          Window mode is enabled for comparators 0 and 1.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1664
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          AC – Analog Comparators

46.8.11 Scaler n

            Name:       SCALER
            Offset:     0x0C + n*0x01 [n=0..1]
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6             5            4             3                 2        1            0
                                                                            VALUE[5:0]
  Access                                   R/W           R/W          R/W                R/W     R/W           R/W
   Reset                                     0            0             0                 0        0            0


            Bits 5:0 – VALUE[5:0] Scaler Value
            These bits define the scaling factor for channel n of the VDD voltage scaler. The output voltage, VSCALE,
            is:
                      �DD ⋅ VALUE+1
            �SCALE =
                             64




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1665
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                         AC – Analog Comparators

46.8.12 Comparator Control n

           Name:       COMPCTRL
           Offset:     0x10 + n*0x04 [n=0..1]
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31           30               29               28                 27     26         25                24
                                                   OUT[1:0]                                      FLEN[2:0]
  Access                                     R/W               R/W                      R/W        R/W                R/W
   Reset                                       0                0                        0           0                 0


     Bit        23           22               21               20                 19     18         17                16
                                                   HYST[1:0]                HYSTEN                       SPEED[1:0]
  Access                                     R/W               R/W            R/W                  R/W                R/W
   Reset                                       0                0                 0                  0                 0


     Bit        15           14               13               12                 11     10          9                 8
              SWAP                        MUXPOS[2:0]                                           MUXNEG[2:0]
  Access       R/W          R/W              R/W               R/W                      R/W        R/W                R/W
   Reset        0             0                0                0                        0           0                 0


     Bit        7             6                5                4                 3      2           1                 0
                         RUNSTDBY                                   INTSEL[1:0]        SINGLE     ENABLE
  Access                    R/W                                R/W            R/W       R/W        R/W
   Reset                      0                                 0                 0      0           0


           Bits 29:28 – OUT[1:0] Output
           These bits configure the output selection for comparator n. COMPCTRLn.OUT can be written only while
           COMPCTRLn.ENABLE is zero.
           Note: For internal use of the comparison results by the CCL, this bit must be 0x1 or 0x2.
           These bits are not synchronized.
            Value      Name Description
            0x0        OFF      The output of COMPn is not routed to the COMPn I/O port
            0x1        ASYNC The asynchronous output of COMPn is routed to the COMPn I/O port
            0x2        SYNC The synchronous output (including filtering) of COMPn is routed to the COMPn I/O
                                port
            0x3        N/A      Reserved

           Bits 26:24 – FLEN[2:0] Filter Length
           These bits configure the filtering for comparator n. COMPCTRLn.FLEN can only be written while
           COMPCTRLn.ENABLE is zero.
           These bits are not synchronized.
            Value      Name                 Description
            0x0        OFF                  No filtering
            0x1        MAJ3                 3-bit majority function (2 of 3)
            0x2        MAJ5                 5-bit majority function (3 of 5)
            0x3-0x7 N/A                     Reserved




       © 2019 Microchip Technology Inc.                                Datasheet                    DS60001507E-page 1666
                                                  SAM D5x/E5x Family Data Sheet
                                                                          AC – Analog Comparators

Bits 21:20 – HYST[1:0] Hysteresis Level
These bits indicate the hysteresis level of comparator n when hysteresis is enabled
(COMPCTRLn.HYSTEN=1). Hysteresis is available only for continuous mode (COMPCTRLn.SINGLE=0).
COMPCTRLn.HYST can be written only while COMPCTRLn.ENABLE is zero.
These bits are not synchronized.
 Value      Name                                       Description
 0x0        HYST50                                     50mV
 0x1        HYST100                                    100mV
 0x2        HYST150                                    150mV
 0x3        N/A                                        Reserved

Bit 19 – HYSTEN Hysteresis Enable
This bit indicates the hysteresis mode of comparator n. Hysteresis is available only for continuous mode
(COMPCTRLn.SINGLE=0).
This bit is not synchronized.
 Value       Description
 0            Hysteresis is disabled.
 1            Hysteresis is enabled.

Bits 17:16 – SPEED[1:0] Speed Selection
This bit must be written to 0x3 for each comparator n. COMPCTRLn.SPEED can be written only while
COMPCTRLn.ENABLE is zero.
These bits are not synchronized.
 Value      Name                             Description
 0x3        HIGH                             High speed
 Other      -                                Reserved

Bit 15 – SWAP Swap Inputs and Invert
This bit swaps the positive and negative inputs to COMPn and inverts the output. This function can be
used for offset cancellation. COMPCTRLn.SWAP can be written only while COMPCTRLn.ENABLE is
zero.
These bits are not synchronized.
 Value       Description
 0           The output of MUXPOS connects to the positive input, and the output of MUXNEG connects
             to the negative input.
 1           The output of MUXNEG connects to the positive input, and the output of MUXPOS connects
             to the negative input.

Bits 14:12 – MUXPOS[2:0] Positive Input Mux Selection
These bits select which input will be connected to the positive input of comparator n.
COMPCTRLn.MUXPOS can be written only while COMPCTRLn.ENABLE is zero.
These bits are not synchronized.
 Value      Name                                     Description
 0x0        PIN0                                     I/O pin 0
 0x1        PIN1                                     I/O pin 1
 0x2        PIN2                                     I/O pin 2
 0x3        PIN3                                     I/O pin 3
 0x4        VSCALE                                   VDD scaler
 0x5–0x7 -                                           Reserved




© 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 1667
                                                  SAM D5x/E5x Family Data Sheet
                                                                         AC – Analog Comparators

Bits 10:8 – MUXNEG[2:0] Negative Input Mux Selection
These bits select which input will be connected to the negative input of comparator n.
COMPCTRLn.MUXNEG can only be written while COMPCTRLn.ENABLE is zero.
These bits are not synchronized.
 Value      Name                           Description
 0x0        PIN0                           I/O pin 0
 0x1        PIN1                           I/O pin 1
 0x2        PIN2                           I/O pin 2
 0x3        PIN3                           I/O pin 3
 0x4        GND                            Ground
 0x5        VSCALE                         VDD scaler
 0x6        BANDGAP                        Internal bandgap voltage
 0x7        DAC                            DAC output

Bit 6 – RUNSTDBY Run in Standby
This bit controls the behavior of the comparator during standby sleep mode.
This bit is not synchronized
 Value       Description
 0           The comparator is disabled during sleep.
 1           The comparator continues to operate during sleep.

Bits 4:3 – INTSEL[1:0] Interrupt Selection
These bits select the condition for comparator n to generate an interrupt or event. COMPCTRLn.INTSEL
can be written only while COMPCTRLn.ENABLE is zero.
These bits are not synchronized.
 Value      Name            Description
 0x0        TOGGLE          Interrupt on comparator output toggle
 0x1        RISING          Interrupt on comparator output rising
 0x2        FALLING         Interrupt on comparator output falling
 0x3        EOC             Interrupt on end of comparison (single-shot mode only)

Bit 2 – SINGLE Single-Shot Mode
This bit determines the operation of comparator n. COMPCTRLn.SINGLE can be written only while
COMPCTRLn.ENABLE is zero.
These bits are not synchronized.
 Value       Description
 0           Comparator n operates in continuous measurement mode.
 1           Comparator n operates in single-shot mode.

Bit 1 – ENABLE Enable
Writing a zero to this bit disables comparator n.
Writing a one to this bit enables comparator n.
Due to synchronization, there is delay from updating the register until the comparator is enabled/disabled.
The value written to COMPCTRLn.ENABLE will read back immediately after being written.
SYNCBUSY.COMPCTRLn is set. SYNCBUSY.COMPCTRLn is cleared when the peripheral is enabled/
disabled.
Writing a one to COMPCTRLn.ENABLE will prevent further changes to the other bits in COMPCTRLn.
These bits remain protected until COMPCTRLn.ENABLE is written to zero and the write is synchronized.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1668
                                                            SAM D5x/E5x Family Data Sheet
                                                                                  AC – Analog Comparators

46.8.13 Synchronization Busy

           Name:       SYNCBUSY
           Offset:     0x20
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29           28           27           26           25           24


  Access
   Reset


     Bit        23           22           21           20           19           18           17           16


  Access
   Reset


     Bit        15           14           13           12           11           10            9            8


  Access
   Reset


     Bit         7            6            5            4            3            2            1            0
                                                   COMPCTRL1    COMPCTRL0     WINCTRL       ENABLE       SWRST
  Access                                                R            R            R            R            R
   Reset                                                0            0            0            0            0


           Bits 3, 4 – COMPCTRLx COMPCTRLx Synchronization Busy
           This bit is cleared when the synchronization of the COMPCTRLx register between the clock domains is
           complete.
           This bit is set when the synchronization of the COMPCTRLx register between clock domains is started.

           Bit 2 – WINCTRL WINCTRL Synchronization Busy
           This bit is cleared when the synchronization of the WINCTRL register between the clock domains is
           complete.
           This bit is set when the synchronization of the WINCTRL register between clock domains is started.

           Bit 1 – ENABLE Enable Synchronization Busy
           This bit is cleared when the synchronization of the CTRLA.ENABLE bit between the clock domains is
           complete.
           This bit is set when the synchronization of the CTRLA.ENABLE bit between clock domains is started.

           Bit 0 – SWRST Software Reset Synchronization Busy
           This bit is cleared when the synchronization of the CTRLA.SWRST bit between the clock domains is
           complete.
           This bit is set when the synchronization of the CTRLA.SWRST bit between clock domains is started.




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1669
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   AC – Analog Comparators

46.8.14 Calibration Register

            Name:       CALIB
            Offset:     0x24
            Reset:      0x0101
            Property:   Enable-Protect, PAC Write-Protection


      Bit        15           14           13           12           11           10            9                  8


  Access
   Reset


      Bit         7            6            5            4            3            2            1                  0
                                                                                                     BIAS0[1:0]
  Access                                                                                       R/W                R/W
   Reset                                                                                        0                  1


            Bits 1:0 – BIAS0[1:0] COMP0/1 Bias Scaling
            This value from production test must be loaded from the NVM software calibration row into the CALIB
            register by software to achieve the specified accuracy.The value must be copied only, and must not be
            changed




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1670
