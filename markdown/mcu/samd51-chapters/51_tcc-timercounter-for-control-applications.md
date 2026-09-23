# 49. TCC – Timer/Counter for Control Applications

*Source: `Atmel-SAMD51.pdf`, pages 1799-1883 — SAMD51 family datasheet*

                                                        SAM D5x/E5x Family Data Sheet
                                                      TCC – Timer/Counter for Control Applications


49.    TCC – Timer/Counter for Control Applications

49.1   Overview
       The device provides five instances of the Timer/Counter for Control applications (TCC) peripheral,
       TCC[4:0].
       Each TCC instance consists of a counter, a prescaler, compare/capture channels and control logic. The
       counter can be set to count events or clock pulses. The counter together with the compare/capture
       channels can be configured to time stamp input events, allowing capture of frequency and pulse-width. It
       can also perform waveform generation, such as frequency generation and pulse-width modulation.
       Waveform extensions are featured for motor control, ballast, LED, H-bridge, power converters, and other
       types of power control applications. They allow for low-side and high-side output with optional dead-time
       insertion. Waveform extensions can also generate a synchronized bit pattern across the waveform output
       pins. The fault options enable fault protection for safe and deterministic handling, disabling and/or shut
       down of external drivers.
       Note: The TCC configurations, such as channel numbers and features, may be reduced for some of the
       TCC instances.
       Related Links
       6.2.7 TCC Configurations



49.2   Features
         • Up to six Compare/Capture Channels (CC) with:
             – Double buffered period setting
             – Double buffered compare or capture channel
             – Circular buffer on period and compare channel registers
         • Waveform Generation:
             – Frequency generation
             – Single-slope pulse-width modulation (PWM)
             – Dual-slope PWM with half-cycle reload capability
         • Input Capture:
             – Event capture
             – Frequency capture
             – Pulse-width capture
         • Waveform Extensions:
             – Configurable distribution of compare channels outputs across port pins
             – Low-side and high-side output with programmable dead-time insertion
             – Waveform swap option with double buffer support
             – Pattern generation with double buffer support
             – Dithering support
         • Fault Protection for Safe Disabling of Drivers:
             – Two recoverable fault sources




       © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1799
                                                                                    SAM D5x/E5x Family Data Sheet
                                                                                   TCC – Timer/Counter for Control Applications

             – Two non-recoverable fault sources
             – Debugger can be a source of non-recoverable fault
         • Input Events:
             – Two input events (EVx) for counter
             – One input event (MCx) for each channel
         • Output Events:
             – Three output events (Count, re-trigger and overflow) are available for counter
             – One compare match/input capture event output for each channel
         • Interrupts:
             – Overflow and re-trigger interrupt
             – Compare match/input capture interrupt
             – Interrupt on fault detection



49.3   Block Diagram
       Figure 49-1. Timer/Counter for Control Applications - Block Diagram
        Base Counter

            BV            PERBUFx


                                PER               Prescaler

                                                      "count"
              Counter                                                                  OVF (INT/Event/DMA Req.)
                                                      "clear"
                                                                                       ERR (INT Req.)
                                                      "load"
                               COUNT                                Control Logic
                                                      "direction"
                                                                                             "TCCx_EV0" (TCE0)
                                                                                             "TCCx_EV1" (TCE1)


                                                         TOP
                                                                         UPDATE




                                            =                                                "TCCx_MCx"             Event
                                                                         "event"




                                                                                                                   System
                                                         BOTTOM
                                       =0



                                                                                                                                                                          WO[7]
                                                                                                                                                                          WO[6]
        Compare/Capture
        (Unit x = {0,1,…,3})
                                                                                                                                                                          WO[5]
                                                                                                                                                        Non-recoverable
                                                                                                                                        Generation




                                                                                                                                                                          WO[4]
                                                                                                                                         Pattern




                                                                                                                                                            Faults
                                                                                                                                 SWAP
                                                                                                          Output
                                                                                                          Matrix




                                            "capture"                                                                                                                     WO[3]
            BV             CCBUFx                                    Control Logic
                                                                                                                                                                          WO[2]
                                                                                                                    Dead-Time
                                                                                                                     Insertion




                                                                                                                                                                          WO[1]
                                                                                            Recoverable




                                CCx
                                                                                              Faults




                                                                      Waveform
                                                                      Generation
                                                                                                                                                                          WO[0]

                                            "match"
                                  =                                                                                                                  MCx (INT/Event/DMA Req.)




49.4   Signal Description
        Pin Name                                        Type                            Description
        TCC/WO[0]                                       Digital output                  Compare channel 0 waveform output
        TCC/WO[1]                                       Digital output                  Compare channel 1 waveform output




       © 2019 Microchip Technology Inc.                                              Datasheet                                               DS60001507E-page 1800
                                                              SAM D5x/E5x Family Data Sheet
                                                             TCC – Timer/Counter for Control Applications

         ...........continued
          Pin Name                          Type                 Description
          …                                 ...                  ...
          TCC/WO[WO_NUM-1]                  Digital output       Compare channel n waveform output

         Refer to I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One signal
         can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



49.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

49.5.1   I/O Lines
         In order to use the I/O lines of this peripheral, the I/O pins must be configured using the I/O Pin Controller
         (PORT).
         Related Links
         32. PORT - I/O Pin Controller

49.5.2   Power Management
         This peripheral can continue to operate in any Sleep mode where its source clock is running. The
         interrupts can wake up the device from Sleep modes. Events connected to the event system can trigger
         other operations in the system without exiting Sleep modes.

49.5.3   Clocks
         The TCC bus clocks (CLK_TCCx_APB) can be enabled and disabled in the Main Clock module. The
         default state of CLK_TCCx_APB can be found in the Peripheral Clock Masking section (see the Related
         Links below).
         A generic clock (GCLK_TCCx) is required to clock the TCC. This clock must be configured and enabled
         in the generic clock controller before using the TCC.
         The generic clocks (GCLK_TCCx) are asynchronous to the bus clock (CLK_TCCx_APB). Due to this
         asynchronicity, writing certain registers will require synchronization between the clock domains. Refer to
         49.6.7 Synchronization for further details.
         Related Links
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller

49.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). In order to use DMA requests with
         this peripheral the DMAC must be configured first. Refer to DMAC – Direct Memory Access Controller for
         details.
         Related Links
         22. DMAC – Direct Memory Access Controller




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1801
                                                             SAM D5x/E5x Family Data Sheet
                                                           TCC – Timer/Counter for Control Applications

49.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first. Refer to Nested Vector Interrupt
         Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

49.5.6   Events
         The events of this peripheral are connected to the Event System.
         Related Links
         31. EVSYS – Event System

49.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will halt normal operation. This peripheral can be
         forced to continue operation during debugging - refer to the Debug Control (DBGCTRL) register for
         details.
         Refer to 49.8.8 DBGCTRL register for details.

49.5.8   Register Access Protection
         Registers with write access can be optionally write-protected by the Peripheral Access Controller (PAC),
         except for the following:
           •   Interrupt Flag register (INTFLAG)
           •   Status register (STATUS)
           •   Period and Period Buffer registers (PER, PERBUF)
           •   Compare/Capture and Compare/Capture Buffer registers (CCx, CCBUFx)
           •   Control Waveform register (WAVE)
           •   Pattern Generation Value and Pattern Generation Value Buffer registers (PATT, PATTBUF)
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

49.5.9   Analog Connections
         Not applicable.



49.6     Functional Description

49.6.1   Principle of Operation
         The following definitions are used throughout the documentation:




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1802
                                                    SAM D5x/E5x Family Data Sheet
                                                  TCC – Timer/Counter for Control Applications

Table 49-1. Timer/Counter for Control Applications - Definitions

 Name                              Description
 TOP                               The counter reaches TOP when it becomes equal to the highest value in
                                   the count sequence. The TOP value can be the same as Period (PER)
                                   or the Compare Channel 0 (CC0) register value depending on the
                                   Waveform Generator mode in 49.6.2.5.1 Waveform Output Generation
                                   Operations.
 ZERO                              The counter reaches ZERO when it contains all zeroes.
 MAX                               The counter reaches maximum when it contains all ones.
 UPDATE                            The timer/counter signals an update when it reaches ZERO or TOP,
                                   depending on the direction settings.
 Timer                             The timer/counter clock control is handled by an internal source.
 Counter                           The clock control is handled externally (e.g., counting external events).
 CC                                For compare operations, the CC are referred to as "compare channels."
                                   For capture operations, the CC are referred to as "capture channels."

Each TCC instance has up to four compare/capture channels (CCx).
The Counter register (COUNT), Period registers with Buffer (PER and PERBUF), and Compare and
Capture registers with buffers (CCx and CCBUFx) are 16- or 24-bit registers, depending on each TCC
instance. Each Buffer register has a Buffer Valid (BUFV) flag that indicates when the buffer contains a
new value.
Under normal operation, the counter value is continuously compared to the TOP or ZERO value to
determine whether the counter has reached TOP or ZERO. In either case, the TCC can generate
interrupt requests or generate events for the Event System. In Waveform Generator mode, these
comparisons are used to set the waveform period or pulse width.
A prescaled generic clock (GCLK_TCCx) and events from the event system can be used to control the
counter. The event system is also used as a source to the input capture.
The Recoverable Fault Unit enables event controlled waveforms by acting directly on the generated
waveforms of the TCC compare channels output. These events can restart, halt the timer/counter period,
shorten the output pulse active time, or disable waveform output as long as the fault condition is present.
This can typically be used for current sensing regulation, and zero-crossing and demagnetization re-
triggering.
The MCE0 and MCE1 asynchronous event sources are shared with the recoverable fault unit. Only
asynchronous events are used internally when fault unit extension is enabled. For further details on how
to configure asynchronous events routing, refer to EVSYS – Event System.
Recoverable fault sources can be filtered and/or windowed to avoid false triggering, for example from I/O
pin glitches, by using digital filtering, input blanking, and qualification options. See also 49.6.3.5
Recoverable Faults.
In order to support applications with different types of motor control, ballast, LED, H-bridge, power
converter, and other types of power switching applications, the following independent units are
implemented in some of the TCC instances as optional and successive units:




© 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1803
                                                             SAM D5x/E5x Family Data Sheet
                                                           TCC – Timer/Counter for Control Applications

           •   Recoverable faults and non-recoverable faults
           •   Output matrix
           •   Dead-time insertion
           •   Swap
           •   Pattern generation
          See also Figure 49-1.
          The output matrix (OTMX) can distribute and route out the TCC waveform outputs across the port pins in
          different configurations, each optimized for different application types. The Dead-Time Insertion (DTI) unit
          splits the four lower OTMX outputs into two non-overlapping signals: the non-inverted Low Side (LS) and
          inverted High Side (HS) of the waveform output with optional dead-time insertion between LS and HS
          switching. The SWAP unit can swap the LS and HS pin outputs, and can be used for fast decay motor
          control.
          The pattern generation unit can be used to generate synchronized waveforms with constant logic level on
          TCC UPDATE conditions. This is useful for easy stepper motor and full bridge control.
          The non-recoverable fault module enables event controlled fault protection by acting directly on the
          generated waveforms of the timer/counter compare channel outputs. When a non-recoverable fault
          condition is detected, the output waveforms are forced to a preconfigured value that is safe for the
          application. This is typically used for instant and predictable shut down and disabling high current or
          voltage drives.
          The count event sources (TCE0 and TCE1) are shared with the non-recoverable fault extension. The
          events can be optionally filtered. If the filter options are not used, the non-recoverable faults provide an
          immediate asynchronous action on waveform output, even for cases where the clock is not present. For
          further details on how to configure asynchronous events routing, refer to section EVSYS – Event System.
          Related Links
          31. EVSYS – Event System

49.6.2    Basic Operation

49.6.2.1 Initialization
          The following registers are enable-protected, meaning that they can only be written when the TCC is
          disabled(CTRLA.ENABLE=0):
            • Control A (CTRLA) register, except Run Standby (RUNSTDBY), Enable (ENABLE) and Software
              Reset (SWRST) bits
            • Recoverable Fault n Control registers (FCTRLA and FCTRLB)
            • Waveform Extension Control register (WEXCTRL)
            • Drive Control register (DRVCTRL)
            • Event Control register (EVCTRL)
          Enable-protected bits in the CTRLA register can be written at the same time as CTRLA.ENABLE is
          written to '1', but not at the same time as CTRLA.ENABLE is written to '0'. Enable-protection is denoted
          by the “Enable-Protected” property in the register description.
          Before the TCC is enabled, it must be configured as outlined by the following steps:
           1. Enable the TCC bus clock (CLK_TCCx_APB).
           2. If Capture mode is required, enable the channel in Capture mode by writing a '1' to the Capture
                Enable bit in the Control A register (CTRLA.CPTEN).




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1804
                                                                 SAM D5x/E5x Family Data Sheet
                                                               TCC – Timer/Counter for Control Applications

         Optionally, the following configurations can be set before enabling TCC:
          1. Select PRESCALER setting in the Control A register (CTRLA.PRESCALER).
          2. Select Prescaler Synchronization setting in Control A register (CTRLA.PRESCSYNC).
          3. If down-counting operation is desired, write the Counter Direction bit in the Control B Set register
               (CTRLBSET.DIR) to '1'.
          4. Select the Waveform Generation operation in the WAVE register (WAVE.WAVEGEN).
          5. Select the Waveform Output Polarity in the WAVE register (WAVE.POL).
          6. The waveform output can be inverted for the individual channels using the Waveform Output Invert
               Enable bit group in the Driver register (DRVCTRL.INVEN).
49.6.2.2 Enabling, Disabling, and Resetting
         The TCC is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The
         TCC is disabled by writing a zero to CTRLA.ENABLE.
         The TCC is reset by writing '1' to the Software Reset bit in the Control A register (CTRLA.SWRST). All
         registers in the TCC, except DBGCTRL, will be reset to their initial state, and the TCC will be disabled.
         Refer to Control A (49.8.1 CTRLA) register for details.
         The TCC should be disabled before the TCC is reset to avoid undefined behavior.
49.6.2.3 Prescaler Selection
         The GCLK_TCCx clock is fed into the internal prescaler.
         The prescaler consists of a counter that counts up to the selected prescaler value, whereupon the output
         of the prescaler toggles.
         If the prescaler value is higher than one, the Counter Update condition can be optionally executed on the
         next GCLK_TCC clock pulse or the next prescaled clock pulse. For further details, refer to the Prescaler
         (CTRLA.PRESCALER) and Counter Synchronization (CTRLA.PRESYNC) descriptions.
         Prescaler outputs from 1 to 1/1024 are available. For a complete list of available prescaler outputs, see
         the register description for the Prescaler bit group in the Control A register (CTRLA.PRESCALER).
         Note: When counting events, the prescaler is bypassed.
         The joint stream of prescaler ticks and event action ticks is called CLK_TCC_COUNT.
         Figure 49-2. Prescaler

                                                              PRESCALER              EVACT 0/1




           GCLK_TCC             PRESCALER
                                                 GCLK_TCC /                                                COUNT
                                            {1,2,4,8,64,256,1024 }      TCCx EV0/1        CLK_TCC_COUNT


49.6.2.4 Counter Operation
         Depending on the mode of operation, the counter is cleared, reloaded, incremented, or decremented at
         each TCC clock input (CLK_TCC_COUNT). A counter clear or reload mark the end of current counter
         cycle and the start of a new one.
         The counting direction is set by the Direction bit in the Control B register (CTRLB.DIR). If the bit is zero,
         it's counting up and one if counting down.




        © 2019 Microchip Technology Inc.                             Datasheet                      DS60001507E-page 1805
                                                  SAM D5x/E5x Family Data Sheet
                                                 TCC – Timer/Counter for Control Applications

The counter will count up or down for each tick (clock or event) until it reaches TOP or ZERO. When it's
counting up and TOP is reached, the counter will be set to zero at the next tick (overflow) and the
Overflow Interrupt Flag in the Interrupt Flag Status and Clear register (INTFLAG.OVF) will be set. When
down-counting, the counter is reloaded with the TOP value when ZERO is reached (underflow), and
INTFLAG.OVF is set.
INTFLAG.OVF can be used to trigger an interrupt, or an event. An overflow/underflow occurrence (i.e. a
compare match with TOP/ZERO) will stop counting if the One-Shot bit in the Control B register is set
(CTRLBSET.ONESHOT). The One-Shot feature is explained in the Additional Features section.
Figure 49-3. Counter Operation
                                                       Direction Change      COUNT written

                         MAX
                                                                                    "reload" update
                                                                                    "clear" update
                          TOP
             COUNT



                         ZERO



                          DIR

It is possible to change the counter value (by writing directly in the COUNT register) even when the
counter is running. The COUNT value will always be ZERO or TOP, depending on direction set by
CTRLBSET.DIR or CTRLBCLR.DIR, when starting the TCC, unless a different value has been written to
it, or the TCC has been stopped at a value other than ZERO. The write access has higher priority than
count, clear, or reload. The direction of the counter can also be changed during normal operation. See
also Figure 49-3.
Stop Command
A stop command can be issued from software by using TCC Command bits in Control B Set register
(CTRLBSET.CMD=0x2, STOP).
When a stop is detected while the counter is running, the counter will maintain its current value. If the
waveform generation (WG) is used, all waveforms are set to a state defined in Non-Recoverable State x
Output Enable bit and Non- Recoverable State x Output Value bit in the Driver Control register
(DRVCTRL.NREx and DRVCTRL.NRVx), and the Stop bit in the Status register is set (STATUS.STOP).
Pause Event Action
A pause command can be issued when the stop event action is configured in the Input Event Action 1 bits
in Event Control register (EVCTRL.EVACT1=0x3, STOP).
When a pause is detected, the counter can stop immediatly maintaining its current value and all
waveforms keep their current state, as long as a start event action is detected: Input Event Action 0 bits in
Event Control register (EVCTRL.EVACT0=0x3, START).
Re-Trigger Command and Event Action
A re-trigger command can be issued from software by using TCC Command bits in Control B Set register
(CTRLBSET.CMD=0x1, RETRIGGER), or from event when the re-trigger event action is configured in the
Input Event 0/1 Action bits in Event Control register (EVCTRL.EVACTn=0x1, RETRIGGER).




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1806
                                                  SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

When the command is detected during counting operation, the counter will be reloaded or cleared,
depending on the counting direction (CTRLBSET.DIR or CTRLBCLR.DIR). The Re-Trigger bit in the
Interrupt Flag Status and Clear register will be set (INTFLAG.TRG). It is also possible to generate an
event by writing a '1' to the Re-Trigger Event Output Enable bit in the Event Control register
(EVCTRL.TRGEO). If the re-trigger command is detected when the counter is stopped, the counter will
resume counting operation from the value in COUNT.
Note:
When a re-trigger event action is configured in the Event Action bits in the Event Control register
(EVCTRL.EVACTn=0x1, RETRIGGER), enabling the counter will not start the counter. The counter will
start on the next incoming event and restart on corresponding following event.
Start Event Action
The start action can be selected in the Event Control register (EVCTRL.EVACT0=0x3, START) and can
start the counting operation when previously stopped. The event has no effect if the counter is already
counting. When the module is enabled, the counter operation starts when the event is received or when a
re-trigger software command is applied.
Note:
When a start event action is configured in the Event Action bits in the Event Control register
(EVCTRL.EVACT0=0x3, START), enabling the counter will not start the counter. The counter will start on
the next incoming event, but it will not restart on subsequent events.
Count Event Action
The TCC can count events. When an event is received, the counter increases or decreases the value,
depending on direction settings (CTRLBSET.DIR or CTRLBCLR.DIR).
The count event action is selected by the Event Action 0 bit group in the Event Control register
(EVCTRL.EVACT0=0x5, COUNT).
Direction Event Action
The direction event action can be selected in the Event Control register (EVCTRL.EVACT1=0x2, DIR).
When this event is used, the asynchronous event path specified in the event system must be configured
or selected. The direction event action can be used to control the direction of the counter operation,
depending on external events level. When received, the event level overrides the Direction settings
(CTRLBSET.DIR or CTRLBCLR.DIR) and the direction bit value is updated accordingly.
Increment Event Action
The increment event action can be selected in the Event Control register (EVCTRL.EVACT0=0x4, INC)
and can change the Counter state when an event is received. When the TCE0 event (TCCx_EV0) is
received, the counter increments, whatever the direction setting (CTRLBSET.DIR or CTRLBCLR.DIR) is.
Decrement Event Action
The decrement event action can be selected in the Event Control register (EVCTRL.EVACT1=0x4, DEC)
and can change the Counter state when an event is received. When the TCE1 (TCCx_EV1) event is
received, the counter decrements, whatever the direction setting (CTRLBSET.DIR or CTRLBCLR.DIR) is.
Non-recoverable Fault Event Action
Non-recoverable fault actions can be selected in the Event Control register (EVCTRL.EVACTn=0x7,
FAULT). When received, the counter will be stopped and the output of the compare channels is




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1807
                                                          SAM D5x/E5x Family Data Sheet
                                                        TCC – Timer/Counter for Control Applications

         overridden according to the Driver Control register settings (DRVCTRL.NREx and DRVCTRL.NRVx).
         TCE0 and TCE1 must be configured as asynchronous events.
         Event Action Off
         If the event action is disabled (EVCTRL.EVACTn=0x0, OFF), enabling the counter will also start the
         counter.
         Related Links
         49.6.3.1 One-Shot Operation

49.6.2.5 Compare Operations
         By default, the Compare/Capture channel is configured for compare operations. To perform capture
         operations, it must be re-configured.
         When using the TCC with the Compare/Capture Value registers (CCx) for compare operations, the
         counter value is continuously compared to the values in the CCx registers. This can be used for timer or
         for waveform operation.
         The Channel x Compare/Capture Buffer Value (CCBUFx) registers provide double buffer capability. The
         double buffering synchronizes the update of the CCx register with the buffer value at the UPDATE
         condition or a force update command (CTRLBSET.CMD=0x3, UPDATE). For further details, refer to
         49.6.2.6 Double Buffering. The synchronization prevents the occurrence of odd-length, non-symmetrical
         pulses and ensures glitch-free output.
49.6.2.5.1 Waveform Output Generation Operations
         The compare channels can be used for waveform generation on output port pins. To make the waveform
         available on the connected pin, the following requirements must be fulfilled:
          1. Choose a Waveform Generation mode in the Waveform Generation Operation bit in Waveform
               register (WAVE.WAVEGEN).
          2. Optionally invert the waveform output WO[x] by writing the corresponding Waveform Output x
               Inversion bit in the Driver Control register (DRVCTRL.INVENx).
          3. Configure the pins with the I/O Pin Controller. Refer to PORT - I/O Pin Controller for details.
               Note: Event must not be used when the compare channel is set in waveform output operating
               mode.
         The counter value is continuously compared with each CCx value. On a comparison match, the Match or
         Capture Channel x bit in the Interrupt Flag Status and Clear register (INTFLAG.MCx) will be set on the
         next zero-to-one transition of CLK_TCC_COUNT (see Normal Frequency Operation). An interrupt and/or
         event can be generated on the same condition if Match/Capture occurs, i.e. INTENSET.MCx and/or
         EVCTRL.MCEOx is '1'. Both interrupt and event can be generated simultaneously.
         There are seven waveform configurations for the Waveform Generation Operation bit group in the
         Waveform register (WAVE.WAVEGEN). This will influence how the waveform is generated and impose
         restrictions on the top value. The configurations are:
           • Normal Frequency (NFRQ)
           • Match Frequency (MFRQ)
           • Normal Pulse-Width Modulation (NPWM)
           • Dual-slope, interrupt/event at TOP (DSTOP)
           • Dual-slope, interrupt/event at ZERO (DSBOTTOM)
           • Dual-slope, interrupt/event at Top and ZERO (DSBOTH)
           • Dual-slope, critical interrupt/event at ZERO (DSCRITICAL)




        © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1808
                                                           SAM D5x/E5x Family Data Sheet
                                                        TCC – Timer/Counter for Control Applications

         When using MFRQ configuration, the TOP value is defined by the CC0 register value. For the other
         waveform operations, the TOP value is defined by the Period (PER) register value.
         For dual-slope waveform operations, the update time occurs when the counter reaches ZERO. For the
         other Waveforms Generation modes, the update time occurs on counter wraparound, on overflow,
         underflow, or re-trigger.
         The table below shows the update counter and overflow event/interrupt generation conditions in different
         operation modes.
         Table 49-2. Counter Update and Overflow Event/interrupt Conditions

          Name              Operation      TOP    Update        Output Waveform           OVFIF/Event
                                                                On Match     On Update Up             Down
          NFRQ              Normal         PER    TOP/          Toggle       Stable       TOP         ZERO
                            Frequency             ZERO
          MFRQ              Match          CC0    TOP/          Toggle       Stable       TOP         ZERO
                            Frequency             ZERO
          NPWM              Single-   PER         TOP/          See section 'Output       TOP         ZERO
                            slope PWM             ZERO          Polarity' below
          DSCRITICAL        Dual-slope     PER    ZERO                                    -           ZERO
                            PWM
          DSBOTTOM          Dual-slope     PER    ZERO                                    -           ZERO
                            PWM
          DSBOTH            Dual-slope     PER    TOP(1) &                                TOP         ZERO
                            PWM                   ZERO
          DSTOP             Dual-slope     PER    ZERO                                    TOP         –
                            PWM

          1.   The UPDATE condition on TOP only will occur when circular buffer is enabled for the channel.
         Related Links
         49.6.3.2 Circular Buffer
         32. PORT - I/O Pin Controller

49.6.2.5.2 Normal Frequency (NFRQ)
         For Normal Frequency generation, the period time (T) is controlled by the period register (PER). The
         waveform generation output (WO[x]) is toggled on each compare match between COUNT and CCx, and
         the corresponding Match or Capture Channel x Interrupt Flag (EVCTRL.MCEOx) will be set.




        © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1809
                                                           SAM D5x/E5x Family Data Sheet
                                                        TCC – Timer/Counter for Control Applications

         Figure 49-4. Normal Frequency Operation
                                    Period (T)       Direction Change     COUNT Written

                      MAX                                                                           "reload" update
                                                                                                    "clear" update
                                                                                                    "match"
         COUNT        TOP

                       CCx

                      ZERO

                     WO[x]

49.6.2.5.3 Match Frequency (MFRQ)
         For Match Frequency generation, the period time (T) is controlled by CC0 register instead of PER. WO[0]
         toggles on each update condition.
         Figure 49-5. Match Frequency Operation

                                                                   Direction Change       COUNT Written

                        MAX
                                                                                                 "reload" update
                                                                                                 "clear" update
                        CC0
         COUNT



                       ZERO


                      WO[0]

49.6.2.5.4 Normal Pulse-Width Modulation (NPWM)
         NPWM uses single-slope PWM generation.
49.6.2.5.5 Single-Slope PWM Operation
         For single-slope PWM generation, the period time (T) is controlled by Top value, and CCx controls the
         duty cycle of the generated waveform output. When up-counting, the WO[x] is set at start or compare
         match between the COUNT and TOP values, and cleared on compare match between COUNT and CCx
         register values. When down-counting, the WO[x] is cleared at start or compare match between the
         COUNT and ZERO values, and set on compare match between COUNT and CCx register values.
         Figure 49-6. Single-Slope PWM Operation
                                                  CCx=ZERO              CCx=TOP
                        MAX                                                                         "clear" update
                                                                                                    "match"
                        TOP


         COUNT
                              CCx


                       ZERO


                      WO[x]




        © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1810
                                                          SAM D5x/E5x Family Data Sheet
                                                         TCC – Timer/Counter for Control Applications

         The following equation calculates the exact resolution for a single-slope PWM (RPWM_SS) waveform:
                     log(TOP+1)
         �PWM_SS =
                        log(2)
         The PWM frequency depends on the Period register value (PER) and the peripheral clock frequency
         (fGCLK_TCC), and can be calculated by the following equation:
                     �GCLK_TCC
         �PWM_SS =
                     N(TOP+1)
         Where N represents the prescaler divider used (1, 2, 4, 8, 16, 64, 256, 1024).
49.6.2.5.6 Dual-Slope PWM Generation
         For dual-slope PWM generation, the period setting (TOP) is controlled by PER, while CCx control the
         duty cycle of the generated waveform output. The figure below shows how the counter repeatedly counts
         from ZERO to PER and then from PER to ZERO. The waveform generator output is set on compare
         match when up-counting, and cleared on compare match when down-counting. An interrupt and/or event
         is generated on TOP (when counting upwards) and/or ZERO (when counting up or down).
         In DSBOTH operation, the circular buffer must be enabled to enable the update condition on TOP.
         Figure 49-7. Dual-Slope Pulse Width Modulation
                                                      CCx=ZERO       CCx=TOP                      "update"
                                                                                                  "match"
                     MAX

                                       CCx

                      TOP
         COUNT



                     ZERO


                    WO[x]
         Using dual-slope PWM results in a lower maximum operation frequency compared to single-slope PWM
         generation. The period (TOP) defines the PWM resolution. The minimum resolution is 1 bit
         (TOP=0x00000001).
         The following equation calculates the exact resolution for dual-slope PWM (RPWM_DS):
                      log(PER+1)
         �PWM_DS =               .
                         log(2)
         The PWM frequency fPWM_DS depends on the period setting (TOP) and the peripheral clock frequency
         fGCLK_TCC, and can be calculated by the following equation:
                     �GCLK_TCC
         �PWM_DS =
                     2� ⋅ PER
         N represents the prescaler divider used. The waveform generated will have a maximum frequency of half
         of the TCC clock frequency (fGCLK_TCC) when TOP is set to 0x00000001 and no prescaling is used.
         The pulse width (PPWM_DS) depends on the compare channel (CCx) register value and the peripheral
         clock frequency (fGCLK_TCC), and can be calculated by the following equation:
                      2� ⋅ TOP − CCx
         �PWM_DS =
                          �GCLK_TCC




        © 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 1811
                                                                     SAM D5x/E5x Family Data Sheet
                                                                    TCC – Timer/Counter for Control Applications

          N represents the prescaler divider used.
          Note: In DSTOP, DSBOTTOM and DSBOTH operation, when TOP is lower than MAX/2, the CCx MSB
          bit defines the ramp on which the CCx Match interrupt or event is generated. (Rising if CCx[MSB] = 0,
          falling if CCx[MSB] = 1.)
          Related Links
          49.6.3.2 Circular Buffer

49.6.2.5.7 Dual-Slope Critical PWM Generation
          Critical mode generation allows generation of non-aligned centered pulses. In this mode, the period time
          is controlled by PER while CCx control the generated waveform output edge during up-counting and
          CC(x+CC_NUM/2) control the generated waveform output edge during down-counting.
          Figure 49-8. Dual-Slope Critical Pulse Width Modulation (N=CC_NUM)
                                                                                                          "reload" update
                                                                                                          "match"
                      MAX

                                      CCx       CC(x+N/2)     CCx     CC(x+N/2)   CCx   CC(x+N/2)

                       TOP
          COUNT



                      ZERO


                     WO[x]



49.6.2.5.8 Output Polarity
          The polarity (WAVE.POLx) is available in all waveform output generation. In single-slope and dual-slope
          PWM operation, it is possible to invert the pulse edge alignment individually on start or end of a PWM
          cycle for each compare channels. The table below shows the waveform output set/clear conditions,
          depending on the settings of timer/counter, direction, and polarity.
          Table 49-3. Waveform Generation Set/Clear Conditions

           Waveform Generation              DIR POLx Waveform Generation Output Update
           Operation
                                                            Set                           Clear
           Single-Slope PWM                 0     0         Timer/counter matches TOP     Timer/counter matches CCx
                                                  1         Timer/counter matches CC      Timer/counter matches TOP
                                            1     0         Timer/counter matches CC      Timer/counter matches ZERO
                                                  1         Timer/counter matches ZERO    Timer/counter matches CC
           Dual-Slope PWM                   x     0         Timer/counter matches CC      Timer/counter matches CC
                                                            when counting up              when counting down
                                                  1         Timer/counter matches CC      Timer/counter matches CC
                                                            when counting down            when counting up




         © 2019 Microchip Technology Inc.                             Datasheet                     DS60001507E-page 1812
                                                          SAM D5x/E5x Family Data Sheet
                                                        TCC – Timer/Counter for Control Applications

        In Normal and Match Frequency, the WAVE.POLx value represents the initial state of the waveform
        output.
49.6.2.6 Double Buffering
        The Pattern (PATT), Period (PER) and Compare Channels (CCx) registers are all double buffered. Each
        buffer register has a buffer valid (PATTBUFV, PERBUFV and CCBUFVx) bit in the STATUS register,
        which indicates that the Buffer register contains a valid value that can be copied into the corresponding
        register. As long as the respective Buffer Valid Status flag (PATTBUFV, PERBUFV or CCBUFVx) are set
        to '1', the related SYNCBUSY bits are set (SYNCBUSY.PATT, SYNCBUSY.PER or SYNCBUSY.CCx), a
        write to the respective PATT/PATTBUF, PER/PERBUF or CCx/CCBUFx registers will generate a PAC
        error, and read access to the respective PATT, PER or CCx register is invalid.
        When the Buffer Valid Flag bit in the STATUS register is '1' and the Lock Update bit in the CTRLB register
        is set to '0', (writing CTRLBCLR.LUPD to '1'), double buffering is enabled: the data from buffer registers
        will be copied into the corresponding register under hardware UPDATE conditions, then the Buffer Valid
        flags bit in the STATUS register are automatically cleared by hardware.
        Note: Software update command (CTRLBSET.CMD=0x3) act independently of LUPD value.
        A compare register is double buffered as in the following figure.
        Figure 49-9. Compare Channel Double Buffering
                                                  "APB write enable"        "data write"




                                                BV                EN          CCBUFx



                                                                  EN              CCx
                      UPDATE
                                                              COUNT
                                                                                        "match"
                                                                              =
        Both the registers (PATT/PER/CCx) and corresponding Buffer registers (PATTBUFPERBUF/CCBUFx) are
        available in the I/O register map, and the double buffering feature is not mandatory. The double buffering
        is disabled by writing a '1' to CTRLSET.LUPD.
        Note: In NFRQ, MFRQ or PWM Down-Counting Counter mode (CTRLBSET.DIR=1), when double
        buffering is enabled (CTRLBCLR.LUPD=1), PERBUF register is continuously copied into the PER
        independently of update conditions.

        Changing the Period
        The counter period can be changed by writing a new Top value to the Period register (PER or CC0,
        depending on the Waveform Generation mode), any period update on registers (PER or CCx) is effective
        after the synchronization delay, whatever double buffering enabling is.




        © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1813
                                                      SAM D5x/E5x Family Data Sheet
                                                    TCC – Timer/Counter for Control Applications

Figure 49-10. Unbuffered Single-Slope Up-Counting Operation
                                                               Counter Wraparound

                MAX
                                                                                           "clear" update
                                                                                           "write"

COUNT



               ZERO

                                   New value written to           New value written to
                                    PER that is higher              PER that is lower
                                   than current COUNT             than current COUNT

Figure 49-11. Unbuffered Single-Slope Down-Counting Operation

               MAX
                                                                                            "reload" update
                                                                                            "write"

COUNT



              ZERO

                      New value written to                New value written to
                       PER that is higher                   PER that is lower
                      than current COUNT                  than current COUNT

A counter wraparound can occur in any operation mode when up-counting without buffering, see Figure
49-10. COUNT and TOP are continuously compared, so when a new value that is lower than the current
COUNT is written to TOP, COUNT will wrap before a compare match.
Figure 49-12. Unbuffered Dual-Slope Operation
                                                          Counter Wraparound

                MAX
                                                                                           "reload" update
                                                                                           "write"

COUNT



               ZERO

                      New value written to                   New value written to
                       PER that is higher                      PER that is lower
                      than current COUNT                     than current COUNT

When double buffering is used, the buffer can be written at any time and the counter will still maintain
correct operation. The period register is always updated on the update condition, as shown in Figure
49-13. This prevents wraparound and the generation of odd waveforms.




© 2019 Microchip Technology Inc.                          Datasheet                      DS60001507E-page 1814
                                                               SAM D5x/E5x Family Data Sheet
                                                              TCC – Timer/Counter for Control Applications

        Figure 49-13. Changing the Period Using Buffering

                        MAX
                                                                                                  "reload" update
                                                                                                  "write"

        COUNT



                       ZERO

                                   New value written to          New value written to
                                                                                         PER is updated with
                                   PERBUF that is higher         PERBUF that is lower
                                                                                         PERBUF value
                                   than current COUNT            than current COUNT

49.6.2.7 Capture Operations
        To enable and use capture operations, the Match or Capture Channel x Event Input Enable bit in the
        Event Control register (EVCTRL.MCEIx) must be written to '1'. The capture channels to be used must
        also be enabled in the Capture Channel x Enable bit in the Control A register (CTRLA.CPTENx) before
        capturing can be performed.
        Event Capture Action
        The compare/capture channels can be used as input capture channels to capture events from the Event
        System, and give them a timestamp. The following figure shows four capture events for one capture
        channel. Event system channels must be configured to operate in asynchronous mode when used for
        capture operations.
        Figure 49-14. Input Capture Timing


                     events

                        MAX




        COUNT



                       ZERO

                                      Capture 0   Capture 1     Capture 2          Capture 3

        For input capture, the Buffer register and the corresponding CCx act like a FIFO. When CCx is empty or
        read, any content in CCBUFx is transferred to CCx. The Buffer Valid flag is passed to set the CCx
        Interrupt flag (IF) and generate the optional interrupt, event, or DMA request. The CCBUFx register value
        cannot be read, all captured data must be read from the CCx register.




        © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1815
                                                   SAM D5x/E5x Family Data Sheet
                                                 TCC – Timer/Counter for Control Applications

Figure 49-15. Capture Double Buffering
                              "capture"                    COUNT



                                   BUFV    EN            CCBUFx


                                    IF     EN               CCx

                              "INT/DMA
                               request"                   data read
The TCC can detect capture overflow of the input capture channels. When a new capture event is
detected while the Capture Buffer Valid flag (STATUS.CCBUFV) is still set, the new timestamp will not be
stored and INTFLAG.ERR will be set.
Period and Pulse-Width (PPW) Capture Action
The TCC can perform two input captures and restart the counter on one of the edges. This enables the
TCC to measure the pulse-width and period and to characterize the frequency f and dutyCycle of an input
signal, as shown below:

     1                             ��
�=           ,    ��������� =
     �                             �
Figure 49-16. PWP Capture
                                          Period (T)
    external
    signal /event

    capture times


                  MAX

                                                                                                 "capture"


    COUNT



                 ZERO
                                           CC0                 CC1    CC0        CC1
Selecting PWP or PPW in the Timer/Counter Event Input 1 Action bit group in the Event Control register
(EVCTRL.EVACT1) enables the TCC to perform one capture action on the rising edge and the other one
on the falling edge. When using PPW event action, period T will be captured into CC0 and the pulse-
width tp into CC1. The PWP (Pulse-width and Period) event action offers the same functionality, but T will
be captured into CC1 and tp into CC0.
The Timer/Counter Event x Invert Enable bit in Event Control register (EVCTRL.TCEINVx) is used for
event source x to select whether the wraparound should occur on the rising edge or the falling edge. If
EVCTRL.TCEINVx=1, the wraparound will happen on the falling edge.




© 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1816
                                                                 SAM D5x/E5x Family Data Sheet
                                                                TCC – Timer/Counter for Control Applications

         The corresponding capture is done only if the channel is enabled in Capture mode (CTRLA.CPTENx=1).
         If not, the capture action will be ignored and the channel will be enabled in compare mode of operation.
         When only one of these channel is required, the other channel can be used for other purposes.
         The TCC can detect capture overflow of the input capture channels. When a new capture event is
         detected while the INTFLAG.MCx is still set, the new timestamp will not be stored and INTFLAG.ERR will
         be set.
         Note: When up-counting (CTRLBSET.DIR=0), counter values lower than 1 cannot be captured in
         Capture Minimum mode (FCTRLn.CAPTURE=CAPTMIN). To capture the full range including value 0, the
         TCC must be configured in Down-counting mode (CTRLBSET.DIR=0).
         Note: In dual-slope PWM operation, and when TOP is lower than MAX/2, the CCx MSB captures the
         CTRLB.DIR state to identify the ramp on which the capture has been done. For rising ramps CCx[MSB] is
         zero, for falling ramps CCx[MSB]=1.

49.6.3   Additional Features

49.6.3.1 One-Shot Operation
         When one-shot is enabled, the counter automatically stops on the next Counter Overflow or Underflow
         condition. When the counter is stopped, the Stop bit in the Status register (STATUS.STOP) is set and the
         waveform outputs are set to the value defined by DRVCTRL.NREx and DRVCTRL.NRVx.
         One-shot operation can be enabled by writing a '1' to the One-Shot bit in the Control B Set register
         (CTRLBSET.ONESHOT) and disabled by writing a '1' to CTRLBCLR.ONESHOT. When enabled, the TCC
         will count until an overflow or underflow occurs and stop counting. The one-shot operation can be
         restarted by a re-trigger software command, a re-trigger event or a start event. When the counter restarts
         its operation, STATUS.STOP is automatically cleared.

49.6.3.2 Circular Buffer
         The Period register (PER) and the Compare Channels register (CC0 toCC5) support circular buffer
         operation. When circular buffer operation is enabled, the PER or CCx values are copied into the
         corresponding buffer registers at each update condition. Circular buffering is dedicated to RAMP2,
         RAMP2A, and DSBOTH operations.
         Figure 49-17. Circular Buffer on Channel 0
                                               "write enable"      "data write"




                                                                                              UPDATE
                                            BUFV         EN         CCBUF0
                                                                                              CIRCC0EN


                                                         EN           CC0
                    UPDATE
                                                      COUNT

                                                                              "ma tch"
                                                                     =

49.6.3.3 Dithering Operation
         The TCC supports dithering on Pulse-width or Period on a 16, 32 or 64 PWM cycles frame.




         © 2019 Microchip Technology Inc.                         Datasheet                   DS60001507E-page 1817
                                                    SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

Dithering consists in adding some extra clocks cycles in a frame of several PWM cycles, and can improve
the accuracy of the average output pulse width and period. The extra clock cycles are added on some of
the compare match signals, one at a time, through a "blue noise" process that minimizes the flickering on
the resulting dither patterns.
Dithering is enabled by writing the corresponding configuration in the Enhanced Resolution bits in CTRLA
register (CTRLA.RESOLUTION):
  • DITH4 enable dithering every 16 PWM frames
  • DITH5 enable dithering every 32 PWM frames
  • DITH6 enable dithering every 64 PWM frames
The DITHERCY bits of COUNT, PER and CCx define the number of extra cycles to add into the frame
(DITHERCY bits from the respective COUNT, PER or CCx registers). The remaining bits of COUNT, PER,
CCx define the compare value itself.
The pseudo code, giving the extra cycles insertion regarding the cycle is:

  int extra_cycle(resolution, dithercy, cycle){
     int MASK;
     int value
     switch (resolution){
       DITH4: MASK = 0x0f;
       DITH5: MASK = 0x1f;
       DITH6: MASK = 0x3f;
     }
     value = cycle * dithercy;
     if (((MASK & value) + dithercy) > MASK)
       return 1;
    return 0;
  }

Dithering on Period
Writing DITHERCY in PER will lead to an average PWM period configured by the following formulas.
DITH4 mode:
                   DITHERCY           1
��������� =                 + PER
                      16          �GCLK_TCC

Note: If DITH4 mode is enabled, the last 4 significant bits from PER/CCx or COUNT register correspond
to the DITHERCY value, rest of the bits corresponds to PER/CCx or COUNT value.
DITH5 mode:
                   DITHERCY           1
��������� =                 + PER
                      32          �GCLK_TCC

DITH6 mode:
                   DITHERCY           1
��������� =                 + PER
                      64          �GCLK_TCC

Dithering on Pulse-Width
Writing DITHERCY in CCx will lead to an average PWM pulse width configured by the following formula.
DITH4 mode:
                         DITHERCY           1
������������ℎ =                   + CCx
                            16          �GCLK_TCC




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 1818
                                                                SAM D5x/E5x Family Data Sheet
                                                               TCC – Timer/Counter for Control Applications

        DITH5 mode:
                                DITHERCY           1
        ������������ℎ =                  + CCx
                                   32          �GCLK_TCC

        DITH6 mode:
                                DITHERCY           1
        ������������ℎ =                  + CCx
                                   64          �GCLK_TCC

        Note: The PWM period will remain static in this case.
49.6.3.4 Ramp Operations
        Three ramp operation modes are supported. All of them require the timer/counter running in single-slope
        PWM generation. The Ramp mode is selected by writing to the Ramp Mode bits in the Waveform Control
        register (WAVE.RAMP).

        RAMP1 Operation
        This is the default PWM operation, described in Single-Slope PWM Generation.

        RAMP2 Operation
        These operation modes are dedicated for power factor correction (PFC), Half-Bridge and Push-Pull
        SMPS topologies, where two consecutive timer/counter cycles are interleaved, see Figure 49-18. In cycle
        A, odd channel output is disabled, and in cycle B, even channel output is disabled. The ramp index
        changes after each update, but can be software modified using the Ramp index command bits in Control
        B Set register (CTRLBSET.IDXCMD).

        Standard RAMP2 (RAMP2) Operation
        Ramp A and B periods are controlled by the PER register value. The PER value can be different on each
        ramp by the Circular Period buffer option in the Wave register (WAVE.CIPEREN=1). This mode uses a
        two-channel TCC to generate two output signals, or one output signal with another CC channel enabled
        in Capture mode.
        Figure 49-18. RAMP2 Standard Operation
                           Ramp             A             B              A                B                      "clear" update
                                                                                                                 "match"

                                                                TOP(B)       Retrigger         TOP(B)
                                                TOP(A)                          on                                CIPEREN = 1
                                                                              FaultA
                                                         CC1                             CC1
            COUNT
                                          CC0                        CC0



                           ZERO

                          WO[0]                                                                                   POL0 = 1

                          WO[1]                                                                 Keep on FaultB    POL1 = 1


                   FaultA input

                   FaultB input




       © 2019 Microchip Technology Inc.                          Datasheet                                 DS60001507E-page 1819
                                                          SAM D5x/E5x Family Data Sheet
                                                         TCC – Timer/Counter for Control Applications

Alternate RAMP2 (RAMP2A) Operation
Alternate RAMP2 operation is similar to RAMP2, but CC0 controls both WO[0] and WO[1] waveforms
when the corresponding circular buffer option is enabled (CIPEREN=1). The waveform polarity is the
same on both outputs. Channel 1 can be used in capture mode.
Figure 49-19. RAMP2 Alternate Operation
                Ramp                 A             B               A                B                       "clear" update
                                                                                                            "match"

                                                          TOP(B)       Retrigger         TOP(B)
                                         TOP(A)                           on                                 CIPEREN = 1
                                                                        FaultA
                                                CC0(B)                        CC0(B)
COUNT                                                                                                        CICCEN0 = 1
                              CC0(A)                         CC0(A)



                ZERO

                WO[0]
                                                                                           Keep on FaultB    POL0 = 1
                WO[1]

         FaultA input

         FaultB input


Critical RAMP2 (RAMP2C) Operation
Critical RAMP2 operation provides a way to cover RAMP2 operation requirements without the update
constraint associated with the use of circular buffers. In this mode, CC0 is controlling the period of ramp A
and PER is controlling the period of ramp B. When using more than two channels, WO[0] output is
controlled by CC2 (HIGH) and CC0 (LOW). On TCC with 2 channels, a pulse on WO[0] will last the entire
period of ramp A, if WAVE.POL0=0.
Figure 49-20. RAMP2 Critical Operation With More Than 2 Channels

                 Ramp                A             B               A                B                       "clear" update
                                                                                                            "match"

                                                           TOP         Retrigger          TOP
                                          CC0                             on
                                                                        FaultA
                                                  CC1                              CC1
 COUNT
                                   CC2                           CC2



                 ZERO

               WO[0]                                                                                         POL2 = 1

               WO[1]                                                                       Keep on FaultB    POL1 = 1

        FaultA input

        FaultB input




© 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 1820
                                                              SAM D5x/E5x Family Data Sheet
                                                             TCC – Timer/Counter for Control Applications

        Figure 49-21. RAMP2 Critical Operation With 2 Channels

                          Ramp             A             B            A                B                     "clear" update
                                                                                                             "match"

                                                                TOP       Retrigger         TOP
                                                CC0                          on
                                                                           FaultA
                                                       CC1                            CC1
          COUNT



                          ZERO

                        WO[0]                                                                                 POL0 = 0

                        WO[1]                                                               Keep on FaultB    POL1 = 1

                 FaultA input

                 FaultB input

49.6.3.5 Recoverable Faults
        Recoverable faults can restart or halt the timer/counter. Two faults, called Fault A and Fault B, can trigger
        recoverable fault actions on the compare channels CC0 and CC1 of the TCC. The compare channels'
        outputs can be clamped to inactive state either as long as the fault condition is present, or from the first
        valid fault condition detection on until the end of the timer/counter cycle.

        Fault Inputs
        The first two channel input events (TCCxMC0 and TCCxMC1) can be used as Fault A and Fault B inputs,
        respectively. Event system channels connected to these fault inputs must be configured as
        asynchronous. The TCC must work in a PWM mode.

        Fault Filtering
        There are three filters available for each input Fault A and Fault B. They are configured by the
        corresponding Recoverable Fault n Configuration registers (FCTRLA and FCTRLB). The three filters can
        either be used independently or in any combination.

         Input         By default, the event detection is asynchronous. When the event occurs, the fault system
         Filtering     will immediately and asynchronously perform the selected fault action on the compare
                       channel output, also in device power modes where the clock is not available. To avoid false
                       fault detection on external events (e.g. due to a glitch on an I/O port) a digital filter can be
                       enabled and configured by the Fault B Filter Value bits in the Fault n Configuration registers
                       (FCTRLn.FILTERVAL). If the event width is less than FILTERVAL (in clock cycles), the
                       event will be discarded. A valid event will be delayed by FILTERVAL clock cycles.
         Fault         This ignores any fault input for a certain time just after a selected waveform output edge.
         Blanking      This can be used to prevent false fault triggering due to signal bouncing, as shown in the
                       figure below. Blanking can be enabled by writing an edge triggering configuration to the
                       Fault n Blanking Mode bits in the Recoverable Fault n Configuration register
                       (FCTRLn.BLANK). The desired duration of the blanking must be written to the Fault n
                       Blanking Time bits (FCTRLn.BLANKVAL).
                       The blanking time tbis calculated by




        © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1821
                                                                                      SAM D5x/E5x Family Data Sheet
                                                                                    TCC – Timer/Counter for Control Applications

                    1 + BLANKVAL
               �� =
                    �GCLK_TCCx_PRESC
               Here, fGCLK_TCCx_PRESC is the frequency of the prescaled peripheral clock frequency
               fGCLK_TCCx.
               The prescaler is enabled by writing '1' to the Fault n Blanking Prescaler bit
               (FCTRLn.BLANKPRESC). When disabled, fGCLK_TCCx_PRESC=fGCLK_TCCx. When enabled,
               fGCLK_TCCx_PRESC=fGCLK_TCCx/64.
               The maximum blanking time (FCTRLn.BLANKVAL=
               255) at fGCLK_TCCx=96MHz is 2.67µs (no prescaler) or 170µs (prescaling). For
               fGCLK_TCCx=1MHz, the maximum blanking time is either 170µs (no prescaling) or 10.9ms
               (prescaling enabled).

Figure 49-22. Fault Blanking in RAMP1 Operation with Inverted Polarity
                                                                                                                                                       "clear" update
                                                                                                                                                       "match"
               TOP
                                                                                                                                               "Fault input enabled"
                                                                                                                                              - "Fault input disabled"
               CC0                                                                                                                             x


COUNT                                                                                                                                                  "Fault discarded"


              ZERO


              CMP0

                      FCTRLA.BLANKVAL = 0         FCTRLA.BLANKVAL > 0               FCTRLA.BLANKVAL > 0

    FaultA Blanking                                                        -                             -                  
                                                                            x                              xxx




         FaultA Input

               WO[0]

 Fault                  This is enabled by writing a '1' to the Fault n Qualification bit in the Recoverable Fault
 Qualification          n Configuration register (FCTRLn.QUAL). When the recoverable fault qualification is
                        enabled (FCTRLn.QUAL=1), the fault input is disabled all the time the corresponding
                        channel output has an inactive level, as shown in the figures below.

Figure 49-23. Fault Qualification in RAMP1 Operation
                MAX
                                                                                                                                                        "clear" update
                TOP
                                                                                                                                                       "match"

  COUNT         CC0                                                                                                                                     "Fault input enabled"

                CC1                                                                                                                            - "Fault input disabled"
                                                                                                                                                   x


                                                                                                                                                        "Fault discarded"
               ZERO

    Fault A Input Qual      -                     -                             -                         -                      -
                                                                                                          x x x             x x x x x x



          Fault Input A

    Fault B Input Qual      -                 -                         -                            -                       -            -
                                      x x x                       x x x x x                       x x x x x x x   x x x x



          Fault Input B




© 2019 Microchip Technology Inc.                                                         Datasheet                                            DS60001507E-page 1822
                                                                                     SAM D5x/E5x Family Data Sheet
                                                                                    TCC – Timer/Counter for Control Applications

Figure 49-24. Fault Qualification in RAMP2 Operation with Inverted Polarity
                 Cycle
                                                                                                                                                                                               "clear" update
                  MAX
                                                                                                                                                                                               "match"
                  TOP
                                                                                                                                                                                           "Fault input enabled"
    COUNT         CC0                                                                                                                                                                     - "Fault input disabled"
                                                                                                                                                                                           x
                  CC1                                                                                                                                                                          "Fault discarded"

                 ZERO

        Fault A Input Qual         -                                           -                                                                     -                          
                                                                   x   x    x                                                              x   x   x   x   x   x   x   x   x




            Fault Input A

      Fault B Input Qual                               -                                          -                                                                             -
                               x       x   x   x   x                                       x   x   x   x       x       x       x   x   x   x




            Fault Input B


Fault Actions
Different fault actions can be configured individually for Fault A and Fault B. Most fault actions are not
mutually exclusive; hence two or more actions can be enabled at the same time to achieve a result that is
a combination of fault actions.

 Keep         This is enabled by writing the Fault n Keeper bit in the Recoverable Fault n Configuration
 Action       register (FCTRLn.KEEP) to '1'. When enabled, the corresponding channel output will be
              clamped to zero as long as the fault condition is present. The clamp will be released on the
              start of the first cycle after the fault condition is no longer present, see next Figure.

Figure 49-25. Waveform Generation with Fault Qualification and Keep Action
              MAX
                                                                                                                                                                                                     "clear" update
              TOP
                                                                                                                                                                                                     "match"

COUNT         CC0                                                                                                                                                                                "Fault input enabled"
                                                                                                                                                                                                - "Fault input disabled"
                                                                                                                                                                                                 x

                                                                                                                                                                                                     "Fault discarded"
              ZERO

  Fault A Input Qual     -                            -                       -                             -                                                          -          
                                                                                                           x       x       x                                       x




        Fault Input A

               WO[0]                                                       KEEP                                                                                            KEEP




 Restart     This is enabled by writing the Fault n Restart bit in Recoverable Fault n Configuration register
 Action      (FCTRLn.RESTART) to '1'. When enabled, the timer/counter will be restarted as soon as the
             corresponding fault condition is present. The ongoing cycle is stopped and the timer/counter
             starts a new cycle, see Figure 49-26. In Ramp 1 mode, when the new cycle starts, the
             compare outputs will be clamped to inactive level as long as the fault condition is present.
             Note: For RAMP2 operation, when a new timer/counter cycle starts the cycle index will
             change automatically, see Figure 49-27. Fault A and Fault B are qualified only during the
             cycle A and cycle B respectively: Fault A is disabled during cycle B, and Fault B is disabled
             during cycle A.




© 2019 Microchip Technology Inc.                                                      Datasheet                                                                                                DS60001507E-page 1823
                                                          SAM D5x/E5x Family Data Sheet
                                                      TCC – Timer/Counter for Control Applications

Figure 49-26. Waveform Generation in RAMP1 mode with Restart Action
                MAX
                                                                                                   "clear" update
                TOP
                                                                                                   "match"

                CC0
COUNT
                CC1

               ZERO

                                              Restart                            Restart

         Fault Input A

              WO[0]

              WO[1]
Figure 49-27. Waveform Generation in RAMP2 mode with Restart Action
              Cycle
                                                                                                   "clear" update
                                          CCx=ZERO                          CCx=TOP                "match"

               MAX
               TOP


COUNT
              CC0/CC1

              ZERO

                                            No fault A action
                                               in cycle B                   Restart

        Fault Input A

             WO[0]

             WO[1]

 Capture       Several capture actions can be selected by writing the Fault n Capture Action bits in the
 Action        Fault n Control register (FCTRLn.CAPTURE). When one of the capture operations is
               selected, the counter value is captured when the fault occurs. These capture operations are
               available:
                • CAPT - the equivalent to a standard capture operation, for further details refer to
                    49.6.2.7 Capture Operations
                • CAPTMIN - gets the minimum time stamped value: on each new local minimum
                    captured value, an event or interrupt is issued.
                • CAPTMAX - gets the maximum time stamped value: on each new local maximum
                    captured value, an event or interrupt (IT) is issued, see Figure 49-28.
                • LOCMIN - notifies by event or interrupt when a local minimum captured value is
                    detected.
                • LOCMAX - notifies by event or interrupt when a local maximum captured value is
                    detected.
                • DERIV0 - notifies by event or interrupt when a local extreme captured value is detected,
                    see Figure 49-29.




© 2019 Microchip Technology Inc.                                Datasheet                  DS60001507E-page 1824
                                                    SAM D5x/E5x Family Data Sheet
                                                  TCC – Timer/Counter for Control Applications

               CCx Content:
               In CAPTMIN and CAPTMAX operations, CCx keeps the respective extremum captured
               values, see Figure 49-28. In LOCMIN, LOCMAX or DERIV0 operation, CCx follows the
               counter value at fault time, see Figure 49-29.
               Before enabling CAPTMIN or CAPTMAX mode of capture, the user must initialize the
               corresponding CCx register value to a value different from zero (for CAPTMIN) top (for
               CAPTMAX). If the CCx register initial value is zero (for CAPTMIN) top (for CAPTMAX), no
               captures will be performed using the corresponding channel.
               MCx Behaviour:
               In LOCMIN and LOCMAX operation, capture is performed on each capture event. The MCx
               interrupt flag is set only when the captured value is above or equal (for LOCMIN) or below or
               equal (for LOCMAX) to the previous captured value. So interrupt flag is set when a new
               relative local Minimum (for CAPTMIN) or Maximum (for CAPTMAX) value has been
               detected. DERIV0 is equivalent to an OR function of (LOCMIN, LOCMAX).
               In CAPT operation, capture is performed on each capture event. The MCx interrupt flag is
               set on each new capture.
               In CAPTMIN and CAPTMAX operation, capture is performed only when on capture event
               time, the counter value is lower (for CAPTMIN) or higher (for CAPMAX) than the last
               captured value. The MCx interrupt flag is set only when on capture event time, the counter
               value is higher or equal (for CAPTMIN) or lower or equal (for CAPTMAX) to the value
               captured on the previous event. So interrupt flag is set when a new absolute local Minimum
               (for CAPTMIN) or Maximum (for CAPTMAX) value has been detected.
               Interrupt Generation
               In CAPT mode, an interrupt is generated on each filtered Fault n and each dedicated CCx
               channel capture counter value. In other modes, an interrupt is only generated on an extreme
               captured value.

Figure 49-28. Capture Action “CAPTMAX”
                TOP
                                                                                              "clear" update
COUNT            CC0

                ZERO




          FaultA Input
           CC0 Event/
             Interrupt




© 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1825
                                                     SAM D5x/E5x Family Data Sheet
                                                   TCC – Timer/Counter for Control Applications

Figure 49-29. Capture Action “DERIV0”

                TOP
                                                                                                      "update"
COUNT           CC0                                                                                   "match"

               ZERO

                 WO[0]

         FaultA Input
           CC0 Event/
             Interrupt

 Hardware    This is configured by writing 0x1 to the Fault n Halt mode bits in the Recoverable Fault n
 Halt Action Configuration register (FCTRLn.HALT). When enabled, the timer/counter is halted and the
             cycle is extended as long as the corresponding fault is present.
                 The next figure ('Waveform Generation with Halt and Restart Actions') shows an example
                 where both restart action and hardware halt action are enabled for Fault A. The compare
                 channel 0 output is clamped to inactive level as long as the timer/counter is halted. The
                 timer/counter resumes the counting operation as soon as the fault condition is no longer
                 present. As the restart action is enabled in this example, the timer/counter is restarted
                 after the fault condition is no longer present.
                 The figure after that ('Waveform Generation with Fault Qualification, Halt, and Restart
                 Actions') shows a similar example, but with additionally enabled fault qualification. Here,
                 counting is resumed after the fault condition is no longer present.
                 Note that in RAMP2 and RAMP2A operations, when a new timer/counter cycle starts, the
                 cycle index will automatically change.
                 Figure 49-30. Waveform Generation with Halt and Restart Actions
                             MAX
                                                                                                  "clear" update
                             TOP
                                                                                                  "match"

                             CC0
                 COUNT

                                                         HALT
                             ZERO

                                                                 Restart      Restart

                       Fault Input A

                             WO[0]




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1826
                                                                     SAM D5x/E5x Family Data Sheet
                                                                  TCC – Timer/Counter for Control Applications

                         Figure 49-31. Waveform Generation with Fault Qualification, Halt, and Restart
                         Actions
                                     MAX
                                                                                                                                           "update"
                                     TOP
                                                                                                                                           "match"

                         COUNT       CC0

                                                                             HALT
                                     ZERO

                                                                             Resume

                          Fault A Input Qual   -          -                                  -                  -               -
                                                                                                               x       x   x




                               Fault Input A

                                     WO[0]                                                KEEP


         Software         This is configured by writing 0x2 to the Fault n Halt mode bits in the Recoverable Fault n
         Halt Action      configuration register (FCTRLn.HALT). Software halt action is similar to hardware halt
                          action, but in order to restart the timer/counter, the corresponding fault condition must not
                          be present anymore, and the corresponding FAULT n bit in the STATUS register must be
                          cleared by software.

        Figure 49-32. Waveform Generation with Software Halt, Fault Qualification, Keep and Restart
        Actions

                      MAX
                                                                                                                                         "update"
                      TOP
                                                                                                                                         "match"

        COUNT         CC0

                                                               HALT
                      ZERO

                                                           Restart                      Restart

         Fault A Input Qual      -                -                                                    -                  -
                                                                                                   x   x




               Fault Input A

             Software Clear

                                                                                  NO
                      WO[0]                                       KEEP
                                                                                 KEEP


                                                           FCTRLA.KEEP = 1   FCTRLA.KEEP = 0



49.6.3.6 Non-Recoverable Faults
        The non-recoverable fault action will force all the compare outputs to a pre-defined level programmed into
        the Driver Control register (DRVCTRL.NRE and DRVCTRL.NRV). The non-recoverable fault input (EV0
        and EV1) actions are enabled in Event Control register (EVCTRL.EVACT0 and EVCTRL.EVACT1).
        To avoid false fault detection on external events (e.g. a glitch on an I/O port) a digital filter can be enabled
        using Non-Recoverable Fault Input x Filter Value bits in the Driver Control register




        © 2019 Microchip Technology Inc.                                 Datasheet                                             DS60001507E-page 1827
                                                         SAM D5x/E5x Family Data Sheet
                                                       TCC – Timer/Counter for Control Applications

        (DRVCTRL.FILTERVALn). Therefore, the event detection is synchronous, and event action is delayed by
        the selected digital filter value clock cycles.
        When the Fault Detection on Debug Break Detection bit in Debug Control register (DGBCTRL.FDDBD) is
        written to '1', a non-recoverable Debug Faults State and an interrupt (DFS) is generated when the system
        goes in debug operation.
        In RAMP2, RAMP2A, or DSBOTH operation, when the Lock Update bit in the Control B register is set by
        writing CTRLBSET.LUPD=1 and the ramp index or counter direction changes, a non-recoverable Update
        Fault State and the respective interrupt (UFS) are generated.
49.6.3.7 Time-Stamp Capture
        This feature is enabled when the Capture Time Stamp (STAMP) Event Action in Event Control register
        (EVCTRL.EVACT) is selected. The counter TOP value must be smaller than MAX.
        When a capture event is detected, the COUNT value is copied into the corresponding Channel x
        Compare/Capture Value (CCx) register. In case of an overflow, the MAX value is copied into the
        corresponding CCx register.
        When a valid captured value is present in the capture channel register, the corresponding Capture
        Channel x Interrupt Flag (INTFLAG.MCx) is set.
        The timer/counter can detect capture overflow of the input capture channels: When a new capture event
        is detected while the Capture Channel interrupt flag (INTFLAG.MCx) is still set, the new time-stamp will
        not be stored and INTFLAG.ERR will be set.
        Figure 49-33. Time-Stamp
        Capture Events

                MAX

                TOP
                                                                                                      "capture"
                                                                                                      "overflow"

        COUNT



                ZERO

          CCx Value             COUNT       COUNT         TOP             COUNT             MAX

49.6.3.8 Waveform Extension
        Figure 49-34 shows a schematic diagram of actions of the four optional units that follow the recoverable
        fault stage on a port pin pair: Output Matrix (OTMX), Dead-Time Insertion (DTI), SWAP and Pattern
        Generation. The DTI and SWAP units can be seen as a four port pair slices:
          • Slice 0 DTI0 / SWAP0 acting on port pins (WO[0], WO[WO_NUM/2 +0])
          • Slice 1 DTI1 / SWAP1 acting on port pins (WO[1], WO[WO_NUM/2 +1])
        And generally:
         • Slice n DTIx / SWAPx acting on port pins (WO[x], WO[WO_NUM/2 +x])




       © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1828
                                                            SAM D5x/E5x Family Data Sheet
                                                           TCC – Timer/Counter for Control Applications

Figure 49-34. Waveform Extension Stage Details
                                            WEX                                               PORTS




                 OTMX                      DTI                   SWAP         PATTERN




          OTMX[x+WO_NUM/2]                                              PGV[x+WO_NUM/2]
                                                                                                                     P[x+WO_NUM/2]
                                      LS
                                                                        PGO[x+WO_NUM/2]               INV[x+WO_NUM/2]
  OTMX                             DTIx          DTIxEN                  SWAPx
                                                                              PGO[x]                        INV[x]
                                      HS
                                                                                                                     P[x]
                OTMX[x]                                                       PGV[x]



The output matrix (OTMX) unit distributes compare channels, according to the selectable configurations
in the following table.
Table 49-4. Output Matrix Channel Pin Routing Configuration

 Value     OTMX[7]        OTMX[6]         OTMX[5]         OTMX[4]       OTMX[3]         OTMX[2]       OTMX[1]        OTMX[0]
 0x0       CC1            CC0             CC5             CC4           CC3             CC2           CC1            CC0
 0x1       CC1            CC0             CC2             CC1           CC0             CC2           CC1            CC0
 0x2       CC0            CC0             CC0             CC0           CC0             CC0           CC0            CC0
 0x3       CC1            CC1             CC1             CC1           CC1             CC1           CC1            CC0

  • Configuration 0x0 is the default configuration. The channel location is the default one and channels
    are distributed on outputs modulo the number of channels. Channel 0 is routed to the Output matrix
    output OTMX[0], and Channel 1 to OTMX[1]. If there are more outputs than channels, then channel 0
    is duplicated to the Output matrix output OTMX[CC_NUM], channel 1 to OTMX[CC_NUM+1] and so
    on.
  • Configuration 0x1 distributes the channels on output modulo half the number of channels. This
    assigns twice the number of output locations to the lower channels than the default configuration.
    This can be used, for example, to control the four transistors of a full bridge using only two compare
    channels.
    Using pattern generation, some of these four outputs can be overwritten by a constant level, enabling
    flexible drive of a full bridge in all quadrant configurations.
  • Configuration 0x2 distributes compare channel 0 (CC0) to all port pins. With pattern generation, this
    configuration can control a stepper motor.
  • Configuration 0x3 distributes the compare channel CC0 to the first output, and the channel CC1 to all
    other outputs. Together with pattern generation and the fault extension, this configuration can control
    up to seven LED strings, with a boost stage.
The table below is an example showing four compare channels on four outputs.
Table 49-5. Four Compare Channels on Four Outputs

 Value             OTMX[3]                        OTMX[2]                 OTMX[1]                      OTMX[0]
 0x0               CC3                            CC2                     CC1                          CC0
 0x1               CC1                            CC0                     CC1                          CC0




© 2019 Microchip Technology Inc.                                Datasheet                               DS60001507E-page 1829
                                                          SAM D5x/E5x Family Data Sheet
                                                         TCC – Timer/Counter for Control Applications

   ...........continued
    Value             OTMX[3]                   OTMX[2]            OTMX[1]                OTMX[0]
    0x2               CC0                       CC0                CC0                    CC0
    0x3               CC1                       CC1                CC1                    CC0

   The dead-time insertion (DTI) unit generates OFF time with the non-inverted low side (LS) and inverted
   high side (HS) of the wave generator output forced at low level. This OFF time is called dead time. Dead-
   time insertion ensures that the LS and HS will never switch simultaneously.
   The DTI stage consists of four equal dead-time insertion generators; one for each of the first four
   compare channels. Figure 49-35 shows the block diagram of one DTI generator. The four channels have
   a common register which controls the dead time, which is independent of high side and low side setting.
   Figure 49-35. Dead-Time Generator Block Diagram
                                                        DTLS                           DTHS

                      Dead Time Generator




                                                                         LOAD
                                                                                  Counter
                                                                         EN


                                                                                     =0

                                                                                                             "DTLS"
OTMX output                   D       Q                                                                      (To PORT)


                                                                                                             "DTHS"
                                          Edge Detect                                                        (To PORT)

   As shown in Figure 49-36, the 8-bit dead-time counter is decremented by one for each peripheral clock
   cycle until it reaches zero. A non-zero counter value will force both the low side and high side outputs into
   their OFF state. When the output matrix (OTMX) output changes, the dead-time counter is reloaded
   according to the edge of the input. When the output changes from low to high (positive edge) it initiates a
   counter reload of the DTLS register. When the output changes from high to low (negative edge) it reloads
   the DTHS register.




   © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1830
                                                               SAM D5x/E5x Family Data Sheet
                                                              TCC – Timer/Counter for Control Applications

         Figure 49-36. Dead-Time Generator Timing Diagram


                           "dti_cnt"



                                                                          T
                                                         tP
                                                tDTILS                t DTIHS
                        "OTMX output"

                           "DTLS"

                           "DTHS"
         The pattern generator unit produces a synchronized bit pattern across the port pins it is connected to.
         The pattern generation features are primarily intended for handling the commutation sequence in
         brushless DC motors (BLDC), stepper motors, and full bridge control. See also Figure 49-37.
         Figure 49-37. Pattern Generator Block Diagram
                        COUNT
                        UPDATE



                              BV            PGEB[7:0]           BV              PGVB[7:0]              SWAP output




                                   EN       PGE[7:0]                 EN         PGV[7:0]




                                                                                            WOx[7:0]

         As with other double-buffered timer/counter registers, the register update is synchronized to the UPDATE
         condition set by the timer/counter waveform generation operation. If synchronization is not required by
         the application, the software can simply access directly the PATT.PGE, PATT.PGV bits registers.

49.6.4   Master/Slave Operation
         Two or more TCC instances sharing the same GCLK_TCC clock, can be linked to provide more
         synchronized CC channels. The operation is enabled by setting the Master Synchronization bit in Control
         A register (CTRLA.MSYNC) in the Slave instance. When the bit is set, the slave TCC instance will
         synchronize the CC channels to the Master counter.
         Related Links
         49.8.1 CTRLA




         © 2019 Microchip Technology Inc.                       Datasheet                               DS60001507E-page 1831
                                                               SAM D5x/E5x Family Data Sheet
                                                              TCC – Timer/Counter for Control Applications

49.6.5   DMA, Interrupts, and Events
         Table 49-6. Module Requests for TCC

          Condition                         Interrupt   Event        Event    DMA       DMA request is
                                            request     output       input    request   cleared
          Overflow / Underflow              Yes         Yes                   Yes(1)    On DMA acknowledge
          Channel Compare                   Yes         Yes          Yes(2)   Yes(3)    For circular buffering:
          Match or Capture                                                              on DMA acknowledge
                                                                                        For capture channel:
                                                                                        when CCx register is
                                                                                        read

          Retrigger                         Yes         Yes
          Count                             Yes         Yes
          Capture Overflow Error            Yes
          Debug Fault State                 Yes
          Recoverable Faults                Yes
          Non-Recoverable Faults Yes
          TCCx Event 0 input                                         Yes(4)
          TCCx Event 1 input                                         Yes(5)

         Notes:
          1. DMA request set on Overflow, Underflow or Re-trigger conditions.
          2. Can perform capture or generate recoverable fault on an event input.
          3. In Capture or Circular modes.
          4. On event input, either action can be executed:
                – re-trigger counter
                – control counter direction
                – stop the counter
                – decrement the counter
                – perform period and pulse width capture
                – generate non-recoverable fault
          5. On event input, either action can be executed:
                – re-trigger counter
                – increment or decrement counter depending on direction
                – start the counter
                – increment or decrement counter based on direction
                – increment counter regardless of direction
                – generate non-recoverable fault
49.6.5.1 DMA Operation
         The TCC can generate the following DMA requests:




         © 2019 Microchip Technology Inc.                        Datasheet                DS60001507E-page 1832
                                                    SAM D5x/E5x Family Data Sheet
                                                  TCC – Timer/Counter for Control Applications

 Counter          If the One-shot Trigger mode in the control A register (CTRLA.DMAOS) is written to '0',
 overflow         the TCC generates a DMA request on each cycle when an update condition (Overflow,
 (OVF)            Underflow or Re-trigger) is detected.
                  When an update condition (Overflow, Underflow or Re-trigger) is detected while
                  CTRLA.DMAOS=1, the TCC generates a DMA trigger on the cycle following the DMA
                  One-Shot Command written to the Control B register (CTRLBSET.CMD=DMAOS).
                  In both cases, the request is cleared by hardware on DMA acknowledge.

 Channel     A DMA request is set only on a compare match if CTRLA.DMAOS=0. The request is
 Match (MCx) cleared by hardware on DMA acknowledge.
             When CTRLA.DMAOS=1, the DMA requests are not generated.

 Channel          For a capture channel, the request is set when valid data is present in the CCx register,
 Capture          and cleared once the CCx register is read.
 (MCx)            In this operation mode, the CTRLA.DMAOS bit value is ignored.


DMA Operation with Circular Buffer
When circular buffer operation is enabled, the Buffer registers must be written in a correct order and
synchronized to the update times of the timer. The DMA triggers of the TCC provide a way to ensure a
safe and correct update of circular buffers.
Note: Circular buffer are intended to be used with RAMP2, RAMP2A and DSBOTH operation only.
DMA Operation with Circular Buffer in RAMP2 and RAMP2A Mode
When a CCx channel is selected as a circular buffer, the related DMA request is not set on a compare
match detection, but on start of ramp B.
If at least one circular buffer is enabled, the DMA overflow request is conditioned to the start of ramp A
with an effective DMA transfer on previous ramp B (DMA acknowledge).
The update of all circular buffer values for ramp A can be done through a DMA channel triggered on a MC
trigger. The update of all circular buffer values for ramp B, can be done through a second DMA channel
triggered by the overflow DMA request.




© 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1833
                                                                    SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

         Figure 49-38. DMA Triggers in RAMP and RAMP2 Operation Mode and Circular Buffer Enabled

                           Ramp            A          B         A                B          A            B


                           Cycle               N-2                        N-1                      N




                                                                                                                               "update"
          COUNT

                          ZERO


                       STATUS.IDX

                      DMA_CCx_req
                                                                          DMA Channel i

                                                                          Update ramp A
                    DMA_OVF_req                                                          DMA Channel j

                                                                                         Update ramp B

         DMA Operation with Circular Buffer in DSBOTH Mode
         When a CC channel is selected as a circular buffer, the related DMA request is not set on a compare
         match detection, but on start of down-counting phase.
         If at least one circular buffer is enabled, the DMA overflow request is conditioned to the start of up-
         counting phase with an effective DMA transfer on previous down-counting phase (DMA acknowledge).
         When up-counting, all circular buffer values can be updated through a DMA channel triggered by MC
         trigger. When down-counting, all circular buffer values can be updated through a second DMA channel,
         triggered by the OVF DMA request.
         Figure 49-39. DMA Triggers in DSBOTH Operation Mode and Circular Buffer Enabled

                              Cycle
                                                N-2                             N-1                      N
                                                      Old Parameter Set                          New Parameter Set



                                                                                                                            "update"
            COUNT


                          ZERO


                          CTRLB.DIR

                         DMA_CCx_req                                              DMA Channel i

                                                                                 Update Rising
                         DMA_OVF_req
                                                                                             DMA Channel j

                                                                                             Update Rising


49.6.5.2 Interrupts
         The TCC has the following interrupt sources:
          • Overflow/Underflow (OVF)
          • Retrigger (TRG)




        © 2019 Microchip Technology Inc.                              Datasheet                                      DS60001507E-page 1834
                                                            SAM D5x/E5x Family Data Sheet
                                                          TCC – Timer/Counter for Control Applications

          •   Count (CNT) - refer also to description of EVCTRL.CNTSEL.
          •   Capture Overflow Error (ERR)
          •   Non-Recoverable Update Fault (UFS)
          •   Debug Fault State (DFS)
          •   Recoverable Faults (FAULTn)
          •   Non-recoverable Faults (FAULTx)
          •   Compare Match or Capture Channels (MCx)
        These interrupts are asynchronous wake-up sources. See Sleep Mode Entry and Exit Table in PM/Sleep
        Mode Controller section for details.
        Each interrupt source has an Interrupt flag associated with it. The Interrupt flag in the Interrupt Flag
        Status and Clear (INTFLAG) register is set when the Interrupt condition occurs. Each interrupt can be
        individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable Set (INTENSET)
        register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
        register. An interrupt request is generated when the Interrupt flag is set and the corresponding interrupt is
        enabled. The interrupt request remains active until the Interrupt flag is cleared, the interrupt is disabled, or
        the TCC is reset. See 49.8.12 INTFLAG for details on how to clear Interrupt flags. The TCC has one
        common interrupt request line for all the interrupt sources. The user must read the INTFLAG register to
        determine which Interrupt condition is present.
        Note: Interrupts must be globally enabled for interrupt requests to be generated. Refer to Nested Vector
        Interrupt Controller for details.
        Related Links
        10.2 Nested Vector Interrupt Controller

49.6.5.3 Events
        The TCC can generate the following output events:
         • Overflow/Underflow (OVF)
         • Trigger (TRG)
         • Counter (CNT) For further details, refer to EVCTRL.CNTSEL description.
         • Compare Match or Capture on compare/capture channels: MCx
        Writing a '1' ('0') to an Event Output bit in the Event Control Register (EVCTRL.xxEO) enables (disables)
        the corresponding output event. Refer also to EVSYS – Event System.
        The TCC can take the following actions on a channel input event (MCx):
         • Capture event
         • Generate a recoverable or non-recoverable fault
        The TCC can take the following actions on counter Event 1 (TCCx EV1):
         • Counter re-trigger
         • Counter direction control
         • Stop the counter
         • Decrement the counter on event
         • Period and pulse width capture
         • Non-recoverable fault
        The TCC can take the following actions on counter Event 0 (TCCx EV0):
         • Counter re-trigger




        © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1835
                                                             SAM D5x/E5x Family Data Sheet
                                                          TCC – Timer/Counter for Control Applications

           • Count on event (increment or decrement, depending on counter direction)
           • Counter start - start counting on the event rising edge. Further events will not restart the counter; the
             counter will keep on counting using prescaled GCLK_TCCx, until it reaches TOP or ZERO,
             depending on the direction.
           • Counter increment on event. This will increment the counter, irrespective of the counter direction.
           • Count during active state of an asynchronous event (increment or decrement, depending on counter
             direction). In this case, the counter will be incremented or decremented on each cycle of the
             prescaled clock, as long as the event is active.
           • Non-recoverable fault
         The counter Event Actions are available in the Event Control registers (EVCTRL.EVACT0 and
         EVCTRL.EVACT1). For further details, refer to EVCTRL.
         Writing a '1' ('0') to an Event Input bit in the Event Control register (EVCTRL.MCEIx or EVCTRL.TCEIx)
         enables (disables) the corresponding action on input event.
         Note: When several events are connected to the TCC, the enabled action will apply for each of the
         incoming events. Refer to EVSYS – Event System for details on how to configure the event system.
         Related Links
         31. EVSYS – Event System

49.6.6   Sleep Mode Operation
         The TCC can be configured to operate in any Sleep mode. To be able to run in standby the RUNSTDBY
         bit in the Control A register (CTRLA.RUNSTDBY) must be '1'. The MODULE can in any Sleep mode
         wake-up the device using interrupts or perform actions through the Event System.

49.6.7   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset and Enable bits in Control A register (CTRLA.SWRST and CTRLA.ENABLE)
         The following registers are synchronized when written:
           •   Control B Clear and Control B Set registers (CTRLBCLR and CTRLBSET)
           •   Status register (STATUS)
           •   Pattern and Pattern Buffer registers (PATT and PATTBUF)
           •   Waveform register (WAVE)
           •   Count Value register (COUNT)
           • Period Value and Period Buffer Value registers (PER and PERBUF)
           • Compare/Capture Channel x and Channel x Compare/Capture Buffer Value registers (CCx and
             CCBUFx)
         The following registers are synchronized when read:
           • Control B Clear and Control B Set registers (CTRLBCLR and CTRLBSET)
           • Count Value register (COUNT): synchronization is done on demand through READSYNC command
             (CTRLBSET.CMD)
           • Pattern and Pattern Buffer registers (PATT and PATTBUF)
           • Waveform register (WAVE)




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1836
                                                 SAM D5x/E5x Family Data Sheet
                                               TCC – Timer/Counter for Control Applications

  • Period Value and Period Buffer Value registers (PER and PERBUF)
  • Compare/Capture Channel x and Channel x Compare/Capture Buffer Value registers (CCx and
    CCBUFx)
Required write synchronization is denoted by the "Write-Synchronized" property in the register
description.
Required read synchronization is denoted by the "Read-Synchronized" property in the register
description.
Related Links
13.3 Register Synchronization




© 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1837
                                                                          SAM D5x/E5x Family Data Sheet
                                                                        TCC – Timer/Counter for Control Applications


49.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0                     RESOLUTION[1:0]                                                        ENABLE         SWRST
                             15:8      MSYNC         ALOCK              PRESCYNC[1:0]        RUNSTDBY                    PRESCALER[2:0]
 0x00         CTRLA
                             23:16     DMAOS
                             31:24                                CPTEN5        CPTEN4         CPTEN3        CPTEN2          CPTEN1         CPTEN0
 0x04        CTRLBCLR         7:0                   CMD[2:0]                         IDXCMD[1:0]            ONESHOT           LUPD               DIR
 0x05        CTRLBSET         7:0                   CMD[2:0]                         IDXCMD[1:0]            ONESHOT           LUPD               DIR
 0x06
   ...       Reserved
 0x07
                              7:0       PER           WAVE          PATT         COUNT         STATUS         CTRLB          ENABLE         SWRST
                             15:8                                   CC5           CC4               CC3        CC2             CC1               CC0
 0x08       SYNCBUSY
                             23:16
                             31:24
                              7:0      RESTART             BLANK[1:0]            QUAL           KEEP                                 SRC[1:0]
                                      BLANKPRES
                             15:8                              CAPTURE[2:0]                           CHSEL[1:0]                     HALT[1:0]
 0x0C         FCTRLA                     C
                             23:16                                                  BLANKVAL[7:0]
                             31:24                                                                                 FILTERVAL[3:0]
                              7:0      RESTART             BLANK[1:0]            QUAL           KEEP                                 SRC[1:0]
                                      BLANKPRES
                             15:8                              CAPTURE[2:0]                           CHSEL[1:0]                     HALT[1:0]
 0x10        FCTRLBA                     C
                             23:16                                                  BLANKVAL[7:0]
                             31:24                                                                                 FILTERVAL[3:0]
                              7:0                                                                                                    OTMX[1:0]
                             15:8                                                              DTIEN3        DTIEN2          DTIEN1         DTIEN0
 0x14        WEXCTRL
                             23:16                                                      DTLS[7:0]
                             31:24                                                      DTHS[7:0]
                              7:0       NRE7          NRE6         NRE5          NRE4           NRE3          NRE2            NRE1           NRE0
                             15:8       NRV7          NRV6         NRV5          NRV4           NRV3          NRV2            NRV1           NRV0
 0x18        DRVCTRL
                             23:16     INVEN7        INVEN6       INVEN5         INVEN4        INVEN3        INVEN2          INVEN1         INVEN0
                             31:24                     FILTERVAL1[3:0]                                             FILTERVAL0[3:0]
 0x1C
   ...       Reserved
 0x1D
 0x1E        DBGCTRL          7:0                                                                             FDDBD                        DBGRUN
 0x1F        Reserved
                              7:0            CNTSEL[1:0]                       EVACT1[2:0]                                 EVACT0[2:0]
                             15:8       TCEI1         TCEI0       TCINV1         TCINV0                      CNTEO           TRGEO          OVFEO
 0x20         EVCTRL
                             23:16                                                              MCEI3         MCEI2          MCEI1           MCEI0
                             31:24                                                             MCEO3         MCEO2           MCEO1          MCEO0




          © 2019 Microchip Technology Inc.                                 Datasheet                                      DS60001507E-page 1838
                                                                      SAM D5x/E5x Family Data Sheet
                                                                    TCC – Timer/Counter for Control Applications

...........continued

  Offset               Name     Bit Pos.

                                  7:0                                                            ERR        CNT          TRG          OVF
                                 15:8      FAULT1       FAULT0    FAULTB      FAULTA             DFS        UFS
   0x24           INTENCLR
                                 23:16                                                           MCx3       MCx2        MCx1         MCx0
                                 31:24
                                  7:0                                                            ERR        CNT          TRG          OVF
                                 15:8      FAULT1       FAULT0    FAULTB      FAULTA             DFS        UFS
   0x28           INTENSET
                                 23:16                                                           MC3        MC2          MC1          MC0
                                 31:24
                                  7:0                                                            ERR        CNT          TRG          OVF
                                 15:8      FAULT1       FAULT0    FAULTB      FAULTA             DFS        UFS
   0x2C            INTFLAG
                                 23:16                                                           MC3        MC2          MC1          MC0
                                 31:24
                                  7:0      PERBUFV               PATTBUFV      SLAVE             DFS        UFS          IDX         STOP
                                 15:8      FAULT1       FAULT0    FAULTB      FAULTA        FAULT1IN      FAULT0IN    FAULTBIN      FAULTAIN
   0x30                STATUS
                                 23:16                                                      CCBUFV3       CCBUFV2     CCBUFV1       CCBUFV0
                                 31:24                                                           CMP3       CMP2        CMP1         CMP0
                                  7:0                                              COUNT[7:0]
                                 15:8                                             COUNT[15:8]
   0x34                COUNT
                                 23:16                                            COUNT[23:16]
                                 31:24
                                  7:0                                                 PGE[7:0]
   0x38                 PATT
                                 15:8                                                 PGV[7:0]
   0x3A
     ...           Reserved
   0x3B
                                  7:0      CIPEREN                    RAMP[1:0]                                      WAVEGEN[2:0]
                                 15:8                                                       CICCEN3       CICCEN2      CICCEN1      CICCEN0
   0x3C                WAVE
                                 23:16                            POL5         POL4              POL3       POL2        POL1         POL0
                                 31:24                                                       SWAP3         SWAP2        SWAP1        SWAP0
                                  7:0            PER[1:0]                                          DITHER[5:0]
                                 15:8                                                 PER[9:2]
   0x40                 PER
                                 23:16                                             PER[17:10]
                                 31:24
                                  7:0            CC[1:0]                                           DITHER[5:0]
                                 15:8                                                  CC[9:2]
   0x44                 CC0
                                 23:16                                             CC[17:10]
                                 31:24
                                  7:0            CC[1:0]                                           DITHER[5:0]
                                 15:8                                                  CC[9:2]
   0x48                 CC1
                                 23:16                                             CC[17:10]
                                 31:24
                                  7:0            CC[1:0]                                           DITHER[5:0]
                                 15:8                                                  CC[9:2]
   0x4C                 CC2
                                 23:16                                             CC[17:10]
                                 31:24




              © 2019 Microchip Technology Inc.                             Datasheet                                 DS60001507E-page 1839
                                                                SAM D5x/E5x Family Data Sheet
                                                               TCC – Timer/Counter for Control Applications

...........continued

  Offset               Name     Bit Pos.

                                  7:0              CC[1:0]                            DITHER[5:0]
                                 15:8                                    CC[9:2]
   0x50                 CC3
                                 23:16                                  CC[17:10]
                                 31:24
                                  7:0              CC[1:0]                            DITHER[5:0]
                                 15:8                                    CC[9:2]
   0x54                 CC4
                                 23:16                                  CC[17:10]
                                 31:24
                                  7:0              CC[1:0]                            DITHER[5:0]
                                 15:8                                    CC[9:2]
   0x58                 CC5
                                 23:16                                  CC[17:10]
                                 31:24
   0x5C
     ...           Reserved
   0x63
                                  7:0                                   PGEB0[7:0]
   0x64            PATTBUF
                                 15:8                                   PGVB0[7:0]
   0x66
     ...           Reserved
   0x6B
                                  7:0            PERBUF[1:0]                         DITHERBUF[5:0]
                                 15:8                                  PERBUF[9:2]
   0x6C                PERBUF
                                 23:16                                PERBUF[17:10]
                                 31:24
                                  7:0            CCBUF[1:0]                          DITHERBUF[5:0]
                                 15:8                                   CCBUF[9:2]
   0x70                CCBUF0
                                 23:16                                 CCBUF[17:10]
                                 31:24
                                  7:0            CCBUF[1:0]                          DITHERBUF[5:0]
                                 15:8                                   CCBUF[9:2]
   0x74                CCBUF1
                                 23:16                                 CCBUF[17:10]
                                 31:24
                                  7:0            CCBUF[1:0]                          DITHERBUF[5:0]
                                 15:8                                   CCBUF[9:2]
   0x78                CCBUF2
                                 23:16                                 CCBUF[17:10]
                                 31:24
                                  7:0            CCBUF[1:0]                          DITHERBUF[5:0]
                                 15:8                                   CCBUF[9:2]
   0x7C                CCBUF3
                                 23:16                                 CCBUF[17:10]
                                 31:24
                                  7:0            CCBUF[1:0]                          DITHERBUF[5:0]
                                 15:8                                   CCBUF[9:2]
   0x80                CCBUF4
                                 23:16                                 CCBUF[17:10]
                                 31:24




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 1840
                                                                  SAM D5x/E5x Family Data Sheet
                                                                TCC – Timer/Counter for Control Applications

...........continued

  Offset               Name     Bit Pos.

                                  7:0            CCBUF[1:0]                               DITHERBUF[5:0]
                                 15:8                                        CCBUF[9:2]
   0x84                CCBUF5
                                 23:16                                      CCBUF[17:10]
                                 31:24




49.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                              DS60001507E-page 1841
                                                                    SAM D5x/E5x Family Data Sheet
                                                                   TCC – Timer/Counter for Control Applications

49.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00000000
               Property:    PAC Write-Protection, Enable-Protected, Write-Synchronized (ENABLE, SWRST)


         Bit        31            30             29           28            27           26           25           24
                                               CPTEN5      CPTEN4        CPTEN3        CPTEN2      CPTEN1        CPTEN0
   Access                                       R/W          R/W           R/W           R/W         R/W          R/W
    Reset                                        0            0             0             0           0            0


         Bit        23            22             21           20            19           18           17           16
                  DMAOS
   Access           R/W
    Reset            0


         Bit        15            14             13           12            11           10           9            8
                  MSYNC         ALOCK            PRESCYNC[1:0]          RUNSTDBY                PRESCALER[2:0]
   Access           R/W          R/W            R/W          R/W           R/W           R/W         R/W          R/W
    Reset            0             0             0            0             0             0           0            0


         Bit         7             6             5            4             3             2           1            0
                                  RESOLUTION[1:0]                                                  ENABLE        SWRST
   Access                        R/W            R/W                                                  R/W          R/W
    Reset                          0             0                                                    0            0


               Bits 24, 25, 26, 27, 28, 29 – CPTEN Capture Channel x Enable
               These bits are used to select the capture or compare operation on channel x.
               Writing a '1' to CPTENx enables capture on channel x.
               Writing a '0' to CPTENx disables capture on channel x.

               Bit 23 – DMAOS DMA One-Shot Trigger Mode
               This bit enables the DMA One-shot Trigger Mode.
               Writing a '1' to this bit will generate a DMA trigger on TCC cycle following a
               TCC_CTRLBSET_CMD_DMAOS command.
               Writing a '0' to this bit will generate DMA triggers on each TCC cycle.
               This bit is not synchronized.

               Bit 15 – MSYNC Master Synchronization (only for TCC slave instance)
               This bit must be set if the TCC counting operation must be synchronized on its Master TCC.
               This bit is not synchronized.
                Value       Description
                0           The TCC controls its own counter.
                1           The counter is controlled by its Master TCC.

               Bit 14 – ALOCK Auto Lock
               This bit is not synchronized.




           © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1842
                                                  SAM D5x/E5x Family Data Sheet
                                                 TCC – Timer/Counter for Control Applications

 Value        Description
 0            The Lock Update bit in the Control B register (CTRLB.LUPD) is not affected by overflow/
              underflow, and re-trigger events
 1            CTRLB.LUPD is set to '1' on each overflow/underflow or re-trigger event.

Bits 13:12 – PRESCYNC[1:0] Prescaler and Counter Synchronization
These bits select if on re-trigger event, the Counter is cleared or reloaded on either the next GCLK_TCCx
clock, or on the next prescaled GCLK_TCCx clock. It is also possible to reset the prescaler on re-trigger
event.
These bits are not synchronized.

 Value                     Name         Description
                                        Counter Reloaded                      Prescaler
 0x0                       GCLK         Reload or reset Counter on next       -
                                        GCLK
 0x1                       PRESC        Reload or reset Counter on next       -
                                        prescaler clock
 0x2                       RESYNC       Reload or reset Counter on next       Reset prescaler counter
                                        GCLK
 0x3                       Reserved

Bit 11 – RUNSTDBY Run in Standby
This bit is used to keep the TCC running in Standby mode.
This bit is not synchronized.
 Value       Description
 0            The TCC is halted in standby.
 1            The TCC continues to run in standby.

Bits 10:8 – PRESCALER[2:0] Prescaler
These bits select the Counter prescaler factor.
These bits are not synchronized.
 Value      Name                   Description
 0x0        DIV1                   Prescaler: GCLK_TCC
 0x1        DIV2                   Prescaler: GCLK_TCC/2
 0x2        DIV4                   Prescaler: GCLK_TCC/4
 0x3        DIV8                   Prescaler: GCLK_TCC/8
 0x4        DIV16                  Prescaler: GCLK_TCC/16
 0x5        DIV64                  Prescaler: GCLK_TCC/64
 0x6        DIV256                 Prescaler: GCLK_TCC/256
 0x7        DIV1024                Prescaler: GCLK_TCC/1024

Bits 6:5 – RESOLUTION[1:0] Dithering Resolution
These bits increase the TCC resolution by enabling the dithering options.
These bits are not synchronized.




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1843
                                                   SAM D5x/E5x Family Data Sheet
                                                 TCC – Timer/Counter for Control Applications

Table 49-7. Dithering

 Value                             Name                 Description
 0x0                               NONE                 The dithering is disabled.
 0x1                               DITH4                Dithering is done every 16 PWM frames. PER[3:0]
                                                        and CCx[3:0] contain dithering pattern selection.
 0x2                               DITH5                Dithering is done every 32 PWM frames. PER[4:0]
                                                        and CCx[4:0] contain dithering pattern selection.
 0x3                               DITH6                Dithering is done every 64 PWM frames. PER[5:0]
                                                        and CCx[5:0] contain dithering pattern selection.

Bit 1 – ENABLE Enable
Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately and the ENABLE bit in the
SYNCBUSY register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be cleared when the
operation is complete.
 Value      Description
 0           The peripheral is disabled.
 1           The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the TCC (except DBGCTRL) to their initial state, and the TCC
will be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence; all other writes in the same write-operation
will be discarded.
Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
Value         Description
0             There is no Reset operation ongoing.
1             The Reset operation is ongoing.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1844
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.2         Control B Clear

               Name:       CTRLBCLR
               Offset:     0x04
               Reset:      0x00
               Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized

               This register allows the user to change this register without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Control B Set (CTRLBSET) register.

         Bit         7            6            5             4                 3       2            1             0
                               CMD[2:0]                          IDXCMD[1:0]       ONESHOT         LUPD          DIR
   Access          R/W           R/W          R/W          R/W             R/W        R/W          R/W          R/W
    Reset            0            0            0             0                 0       0            0             0


               Bits 7:5 – CMD[2:0] TCC Command
               These bits can be used for software control of re-triggering and stop commands of the TCC. When a
               command has been executed, the CMD bit field will read back zero. The commands are executed on the
               next prescaled GCLK_TCC clock cycle.
               Writing zero to this bit group has no effect.
               Writing a '1' to any of these bits will clear the pending command.
                Value        Name                       Description
                0x0          NONE                       No action
                0x1          RETRIGGER                  Clear start, restart or retrigger
                0x2          STOP                       Force stop
                0x3          UPDATE                     Force update of double buffered registers
                0x4          READSYNC                   Force COUNT read synchronization
                0x5          DMAOS                      One-shot DMA trigger

               Bits 4:3 – IDXCMD[1:0] Ramp Index Command
               These bits can be used to force cycle A and cycle B changes in RAMP2 and RAMP2A operation. On
               timer/counter update condition, the command is executed, the IDX flag in STATUS register is updated
               and the IDXCMD command is cleared.
               Writing zero to these bits has no effect.
               Writing a '1' to any of these bits will clear the pending command.
                Value        Name         Description
                0x0          DISABLE      DISABLE Command disabled: IDX toggles between cycles A and B
                0x1          SET          Set IDX: cycle B will be forced in the next cycle
                0x2          CLEAR        Clear IDX: cycle A will be forced in next cycle
                0x3          HOLD         Hold IDX: the next cycle will be the same as the current cycle.

               Bit 2 – ONESHOT One-Shot
               This bit controls one-shot operation of the TCC. When one-shot operation is enabled, the TCC will stop
               counting on the next overflow/underflow condition or on a stop command.
               Writing a '0' to this bit has no effect
               Writing a '1' to this bit will disable the one-shot operation.
                Value        Description
                0            The TCC will update the counter value on overflow/underflow condition and continue
                             operation.




           © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1845
                                                     SAM D5x/E5x Family Data Sheet
                                                   TCC – Timer/Counter for Control Applications

 Value        Description
 1            The TCC will stop counting on the next underflow/overflow condition.

Bit 1 – LUPD Lock Update
This bit controls the update operation of the TCC buffered registers.
When CTRLB.LUPD is cleared, the hardware UPDATE registers with value from their buffered registers is
enabled.
This bit has no effect when input capture operation is enabled.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will enable the registers updates on hardware UPDATE condition.
 Value        Description
 0            The CCBx, PERB, PGVB, PGOB, and SWAPBx buffer registers values are copied into the
              corresponding CCx, PER, PGV, PGO and SWAPx registers on hardware update condition.
 1            The CCBx, PERB, PGVB, PGOB, and SWAPBx buffer registers values are not copied into
              the corresponding CCx, PER, PGV, PGO and SWAPx registers on hardware update
              condition.

Bit 0 – DIR Counter Direction
This bit is used to change the direction of the counter.
Writing a '0' to this bit has no effect
Writing a '1' to this bit will clear the bit and make the counter count up.
 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1846
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.3         Control B Set

               Name:       CTRLBSET
               Offset:     0x05
               Reset:      0x00
               Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized

               This register allows the user to change this register without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Control B Set (CTRLBCLR) register.

         Bit         7            6            5             4                 3       2            1             0
                               CMD[2:0]                          IDXCMD[1:0]       ONESHOT         LUPD          DIR
   Access          R/W           R/W          R/W          R/W             R/W        R/W          R/W          R/W
    Reset            0            0            0             0                 0       0            0             0


               Bits 7:5 – CMD[2:0] TCC Command
               These bits can be used for software control of re-triggering and stop commands of the TCC. When a
               command has been executed, the CMD bit field will be read back as zero. The commands are executed
               on the next prescaled GCLK_TCC clock cycle.
               Writing zero to this bit group has no effect
               Writing a valid value to this bit group will set the associated command.
                Value      Name                       Description
                0x0        NONE                       No action
                0x1        RETRIGGER                  Force start, restart or retrigger
                0x2        STOP                       Force stop
                0x3        UPDATE                     Force update of double buffered registers
                0x4        READSYNC                   Force a read synchronization of COUNT
                0x5        DMAOS                      One-shot DMA trigger

               Bits 4:3 – IDXCMD[1:0] Ramp Index Command
               These bits can be used to force cycle A and cycle B changes in RAMP2 and RAMP2A operation. On
               timer/counter update condition, the command is executed, the IDX flag in STATUS register is updated
               and the IDXCMD command is cleared.
               Writing a zero to these bits has no effect.
               Writing a valid value to these bits will set a command.
                Value      Name            Description
                0x0        DISABLE         Command disabled: IDX toggles between cycles A and B
                0x1        SET             Set IDX: cycle B will be forced in the next cycle
                0x2        CLEAR           Clear IDX: cycle A will be forced in next cycle
                0x3        HOLD            Hold IDX: the next cycle will be the same as the current cycle.

               Bit 2 – ONESHOT One-Shot
               This bit controls one-shot operation of the TCC. When in one-shot operation, the TCC will stop counting
               on the next overflow/underflow condition or a stop command.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will enable the one-shot operation.
                Value        Description
                0            The TCC will count continuously.
                1            The TCC will stop counting on the next underflow/overflow condition.




           © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1847
                                                     SAM D5x/E5x Family Data Sheet
                                                   TCC – Timer/Counter for Control Applications

Bit 1 – LUPD Lock Update
This bit controls the update operation of the TCC buffered registers.
When CTRLB.LUPD is set, the hardware UPDATE registers with value from their buffered registers is
disabled. Disabling the update ensures that all buffer registers are valid before an hardware update is
performed. After all the buffer registers are loaded correctly, the buffered registers can be unlocked.
This bit has no effect when input capture operation is enabled.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will disable the registers updates on hardware UPDATE condition.
 Value        Description
 0            The CCBx, PERB, PGVB, PGOB, and SWAPBx buffer registers values are copied into the
              corresponding CCx, PER, PGV, PGO and SWAPx registers on hardware update condition.
 1            The CCBx, PERB, PGVB, PGOB, and SWAPBx buffer registers values are not copied into
              CCx, PER, PGV, PGO and SWAPx registers on hardware update condition.

Bit 0 – DIR Counter Direction
This bit is used to change the direction of the counter.
Writing a '0' to this bit has no effect
Writing a '1' to this bit will clear the bit and make the counter count up.
 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1848
                                                                 SAM D5x/E5x Family Data Sheet
                                                                TCC – Timer/Counter for Control Applications

49.8.4         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x08
               Reset:      0x00000000
               Property:   -


         Bit        31           30            29          28           27           26           25             24


   Access
    Reset


         Bit        23           22            21          20           19           18           17             16


   Access
    Reset


         Bit        15           14            13          12           11           10            9              8
                                              CC5         CC4          CC3          CC2          CC1             CC0
   Access                                      R            R            R            R            R              R
    Reset                                      0            0            0            0            0              0


         Bit         7            6            5            4            3            2            1              0
                   PER          WAVE          PATT       COUNT        STATUS       CTRLB        ENABLE          SWRST
   Access           R             R            R            R            R            R            R              R
    Reset            0            0            0            0            0            0            0              0


               Bits 8, 9, 10, 11, 12, 13 – CC Compare/Capture Channel x Synchronization Busy
               This bit is cleared when the synchronization of Compare/Capture Channel x register between the clock
               domains is complete.
               This bit is set when the synchronization of Compare/Capture Channel x register between clock domains
               is started.
               CCx bit is available only for existing Compare/Capture Channels. For details on CC channels number,
               refer to each TCC feature list.
               This bit is set when the synchronization of CCx register between clock domains is started.

               Bit 7 – PER PER Synchronization Busy
               This bit is cleared when the synchronization of PER register between the clock domains is complete.
               This bit is set when the synchronization of PER register between clock domains is started.

               Bit 6 – WAVE WAVE Synchronization Busy
               This bit is cleared when the synchronization of WAVE register between the clock domains is complete.
               This bit is set when the synchronization of WAVE register between clock domains is started.

               Bit 5 – PATT PATT Synchronization Busy
               This bit is cleared when the synchronization of PATTERN register between the clock domains is
               complete.
               This bit is set when the synchronization of PATTERN register between clock domains is started.




           © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1849
                                                SAM D5x/E5x Family Data Sheet
                                              TCC – Timer/Counter for Control Applications

Bit 4 – COUNT COUNT Synchronization Busy
This bit is cleared when the synchronization of COUNT register between the clock domains is complete.
This bit is set when the synchronization of COUNT register between clock domains is started.

Bit 3 – STATUS STATUS Synchronization Busy
This bit is cleared when the synchronization of STATUS register between the clock domains is complete.
This bit is set when the synchronization of STATUS register between clock domains is started.

Bit 2 – CTRLB CTRLB Synchronization Busy
This bit is cleared when the synchronization of CTRLB register between the clock domains is complete.
This bit is set when the synchronization of CTRLB register between clock domains is started.

Bit 1 – ENABLE ENABLE Synchronization Busy
This bit is cleared when the synchronization of ENABLE bit between the clock domains is complete.
This bit is set when the synchronization of ENABLE bit between clock domains is started.

Bit 0 – SWRST SWRST Synchronization Busy
This bit is cleared when the synchronization of SWRST bit between the clock domains is complete.
This bit is set when the synchronization of SWRST bit between clock domains is started.




© 2019 Microchip Technology Inc.                 Datasheet                         DS60001507E-page 1850
                                                                    SAM D5x/E5x Family Data Sheet
                                                                   TCC – Timer/Counter for Control Applications

49.8.5         Fault Control A and B

               Name:       FCTRLA, FCTRLB
               Offset:     0x0C + n*0x04 [n=0..1]
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31            30                29        28           27                26            25               24
                                                                                              FILTERVAL[3:0]
   Access                                                                 R/W                R/W          R/W               R/W
    Reset                                                                  0                  0            0                 0


         Bit        23            22                21        20           19                18            17               16
                                                               BLANKVAL[7:0]
   Access          R/W           R/W                R/W      R/W          R/W                R/W          R/W               R/W
    Reset            0            0                  0        0            0                  0            0                 0


         Bit        15            14                13        12           11                10            9                 8
               BLANKPRESC                     CAPTURE[2:0]                      CHSEL[1:0]                      HALT[1:0]
   Access          R/W           R/W                R/W      R/W          R/W                R/W          R/W               R/W
    Reset            0            0                  0        0            0                  0            0                 0


         Bit         7            6                  5        4            3                  2            1                 0
                 RESTART               BLANK[1:0]            QUAL         KEEP                                  SRC[1:0]
   Access          R/W           R/W                R/W      R/W          R/W                             R/W               R/W
    Reset            0            0                  0        0            0                               0                 0


               Bits 27:24 – FILTERVAL[3:0] Recoverable Fault n Filter Value
               These bits define the filter value applied on MCEx (x=0,1) event input line. The value must be set to zero
               when MCEx event is used as synchronous event.

               Bits 23:16 – BLANKVAL[7:0] Recoverable Fault n Blanking Value
               These bits determine the duration of the blanking of the fault input source. Activation and edge selection
               of the blank filtering are done by the BLANK bits (FCTRLn.BLANK).
               When enabled, the fault input source is internally disabled for BLANKVAL* prescaled GCLK_TCC periods
               after the detection of the waveform edge.

               Bit 15 – BLANKPRESC Recoverable Fault n Blanking Value Prescaler
               This bit enables a factor 64 prescaler factor on used as base frequency of the BLANKVAL value.
                Value      Description
                0          Blank time is BLANKVAL* prescaled GCLK_TCC.
                1          Blank time is BLANKVAL* 64 * prescaled GCLK_TCC.

               Bits 14:12 – CAPTURE[2:0] Recoverable Fault n Capture Action
               These bits select the capture and Fault n interrupt/event conditions.




           © 2019 Microchip Technology Inc.                          Datasheet                             DS60001507E-page 1851
                                                       SAM D5x/E5x Family Data Sheet
                                                   TCC – Timer/Counter for Control Applications

Table 49-8. Fault n Capture Action

 Value       Name         Description
  0x0      DISABLE        Capture on valid recoverable Fault n is disabled
  0x1         CAPT        On rising edge of a valid recoverable Fault n, capture counter value on channel
                          selected by CHSEL[1:0]. INTFLAG.FAULTn flag rises on each new captured value.
  0x2      CAPTMIN        On rising edge of a valid recoverable Fault n, capture counter value on channel
                          selected by CHSEL[1:0], if COUNT value is lower than the last stored capture
                          value (CC). INTFLAG.FAULTn flag rises on each local minimum detection.
  0x3      CAPTMAX        On rising edge of a valid recoverable Fault n, capture counter value on channel
                          selected by CHSEL[1:0], if COUNT value is higher than the last stored capture
                          value (CC). INTFLAG.FAULTn flag rises on each local maximun detection.
  0x4       LOCMIN        On rising edge of a valid recoverable Fault n, capture counter value on channel
                          selected by CHSEL[1:0]. INTFLAG.FAULTn flag rises on each local minimum
                          value detection.
  0x5      LOCMAX         On rising edge of a valid recoverable Fault n, capture counter value on channel
                          selected by CHSEL[1:0]. INTFLAG.FAULTn flag rises on each local maximun
                          detection.
  0x6       DERIV0        On rising edge of a valid recoverable Fault n, capture counter value on channel
                          selected by CHSEL[1:0]. INTFLAG.FAULTn flag rises on each local maximun or
                          minimum detection.
  0x7     CAPTMARK Capture with ramp index as MSB value.

Bits 11:10 – CHSEL[1:0] Recoverable Fault n Capture Channel
These bits select the channel for capture operation triggered by recoverable Fault n.
 Value      Name              Description
 0x0        CC0               Capture value stored into CC0
 0x1        CC1               Capture value stored into CC1
 0x2        CC2               Capture value stored into CC2
 0x3        CC3               Capture value stored into CC3

Bits 9:8 – HALT[1:0] Recoverable Fault n Halt Operation
These bits select the halt action for recoverable Fault n.
 Value      Name                            Description
 0x0        DISABLE                         Halt action disabled
 0x1        HW                              Hardware halt action
 0x2        SW                              Software halt action
 0x3        NR                              Non-recoverable fault

Bit 7 – RESTART Recoverable Fault n Restart
Setting this bit enables restart action for Fault n.
Value        Description
0            Fault n restart action is disabled.
1            Fault n restart action is enabled.




© 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1852
                                                  SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

Bits 6:5 – BLANK[1:0] Recoverable Fault n Blanking Operation
These bits, select the blanking start point for recoverable Fault n.
 Value      Name         Description
 0x0        START        Blanking applied from start of the Ramp period
 0x1        RISE         Blanking applied from rising edge of the waveform output
 0x2        FALL         Blanking applied from falling edge of the waveform output
 0x3        BOTH         Blanking applied from each toggle of the waveform output

Bit 4 – QUAL Recoverable Fault n Qualification
Setting this bit enables the recoverable Fault n input qualification.
Value        Description
0            The recoverable Fault n input is not disabled on CMPx value condition.
1            The recoverable Fault n input is disabled when output signal is at inactive level (CMPx == 0).

Bit 3 – KEEP Recoverable Fault n Keep
Setting this bit enables the Fault n keep action.
Value        Description
0            The Fault n state is released as soon as the recoverable Fault n is released.
1            The Fault n state is released at the end of TCC cycle.

Bits 1:0 – SRC[1:0] Recoverable Fault n Source
These bits select the TCC event input for recoverable Fault n.
Event system channel connected to MCEx event input, must be configured to route the event
asynchronously, when used as a recoverable Fault n input.
 Value      Name           Description
 0x0        DISABLE        Fault input disabled
 0x1        ENABLE         MCEx (x=0,1) event input
 0x2        INVERT         Inverted MCEx (x=0,1) event input
 0x3        ALTFAULT       Alternate fault (A or B) state at the end of the previous period.




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1853
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.6         Waveform Extension Control

               Name:       WEXCTRL
               Offset:     0x14
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31           30           29            28               27       26           25               24
                                                                 DTHS[7:0]
   Access          R/W           R/W          R/W          R/W               R/W     R/W          R/W               R/W
    Reset            0            0            0            0                 0       0             0                0


         Bit        23           22           21            20               19       18           17               16
                                                                 DTLS[7:0]
   Access          R/W           R/W          R/W          R/W               R/W     R/W          R/W               R/W
    Reset            0            0            0            0                 0       0             0                0


         Bit        15           14           13            12               11       10            9                8
                                                                         DTIEN3     DTIEN2       DTIEN1        DTIEN0
   Access                                                                    R/W     R/W          R/W               R/W
    Reset                                                                     0       0             0                0


         Bit         7            6            5            4                 3       2             1                0
                                                                                                        OTMX[1:0]
   Access                                                                                         R/W               R/W
    Reset                                                                                           0                0


               Bits 31:24 – DTHS[7:0] Dead-Time High Side Outputs Value
               This register holds the number of GCLK_TCC clock cycles for the dead-time high side.

               Bits 23:16 – DTLS[7:0] Dead-time Low Side Outputs Value
               This register holds the number of GCLK_TCC clock cycles for the dead-time low side.

               Bits 8, 9, 10, 11 – DTIEN Dead-time Insertion Generator x Enable
               Setting any of these bits enables the dead-time insertion generator for the corresponding output matrix.
               This will override the output matrix [x] and [x+WO_NUM/2], with the low side and high side waveform
               respectively.
                Value       Description
                0           No dead-time insertion override.
                1           Dead time insertion override on signal outputs[x] and [x+WO_NUM/2], from matrix outputs[x]
                            signal.

               Bits 1:0 – OTMX[1:0] Output Matrix
               These bits define the matrix routing of the TCC waveform generation outputs to the port pins, according
               to 49.6.3.8 Waveform Extension.




           © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1854
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.7         Driver Control

               Name:       DRVCTRL
               Offset:     0x18
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31            30            29          28            27           26            25              24
                                  FILTERVAL1[3:0]                                       FILTERVAL0[3:0]
   Access          R/W           R/W           R/W          R/W          R/W          R/W           R/W           R/W
    Reset            0            0             0            0            0             0             0              0


         Bit        23            22            21          20            19           18            17              16
                  INVEN7        INVEN6        INVEN5      INVEN4       INVEN3        INVEN2        INVEN1        INVEN0
   Access          R/W           R/W           R/W          R/W          R/W          R/W           R/W           R/W
    Reset            0            0             0            0            0             0             0              0


         Bit        15            14            13          12            11           10             9              8
                   NRV7         NRV6          NRV5         NRV4         NRV3          NRV2          NRV1         NRV0
   Access          R/W           R/W           R/W          R/W          R/W          R/W           R/W           R/W
    Reset            0            0             0            0            0             0             0              0


         Bit         7            6             5            4            3             2             1              0
                   NRE7         NRE6          NRE5         NRE4         NRE3          NRE2          NRE1         NRE0
   Access          R/W           R/W           R/W          R/W          R/W          R/W           R/W           R/W
    Reset            0            0             0            0            0             0             0              0


               Bits 31:28 – FILTERVAL1[3:0] Non-Recoverable Fault Input 1 Filter Value
               These bits define the filter value applied on TCE1 event input line. When the TCE1 event input line is
               configured as a synchronous event, this value must be 0x0.

               Bits 27:24 – FILTERVAL0[3:0] Non-Recoverable Fault Input 0 Filter Value
               These bits define the filter value applied on TCE0 event input line. When the TCE0 event input line is
               configured as a synchronous event, this value must be 0x0.

               Bits 16, 17, 18, 19, 20, 21, 22, 23 – INVEN Waveform Output x Inversion
               These bits are used to select inversion on the output of channel x.
               Writing a '1' to INVENx inverts output from WO[x].
               Writing a '0' to INVENx disables inversion of output from WO[x].

               Bits 8, 9, 10, 11, 12, 13, 14, 15 – NRV NRVx Non-Recoverable State x Output Value
               These bits define the value of the enabled override outputs, under non-recoverable fault condition.

               Bits 0, 1, 2, 3, 4, 5, 6, 7 – NRE Non-Recoverable State x Output Enable
               These bits enable the override of individual outputs by NRVx value, under non-recoverable fault
               condition.
                Value       Description
                0           Non-recoverable fault tri-state the output.
                1           Non-recoverable faults set the output to NRVx level.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1855
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.8         Debug control

               Name:       DBGCTRL
               Offset:     0x1E
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6             5            4            3             2            1             0
                                                                                     FDDBD                     DBGRUN
   Access                                                                             R/W                        R/W
    Reset                                                                               0                          0


               Bit 2 – FDDBD Fault Detection on Debug Break Detection
               This bit is not affected by software Reset and should not be changed by software while the TCC is
               enabled.
               By default this bit is zero, and the on-chip debug (OCD) fault protection is disabled. When this bit is
               written to ‘1’, OCD break request from the OCD system will trigger non-recoverable fault. When this bit is
               set, OCD fault protection is enabled and OCD break request from the OCD system will trigger a non-
               recoverable fault.
                Value        Description
                0            No faults are generated when TCC is halted in Debug mode.
                1            A non recoverable fault is generated and FAULTD flag is set when TCC is halted in Debug
                             mode.

               Bit 0 – DBGRUN Debug Running State
               This bit is not affected by software Reset and should not be changed by software while the TCC is
               enabled.
                Value       Description
                0           The TCC is halted when the device is halted in Debug mode.
                1           The TCC continues normal operation when the device is halted in Debug mode.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1856
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.9         Event Control

               Name:         EVCTRL
               Offset:       0x20
               Reset:        0x00000000
               Property:     PAC Write-Protection, Enable-Protected


         Bit        31                 30       29          28           27            26           25           24
                                                                       MCEO3        MCEO2         MCEO1        MCEO0
   Access                                                                R/W          R/W          R/W          R/W
    Reset                                                                 0            0            0             0


         Bit        23                 22       21          20           19            18           17           16
                                                                        MCEI3        MCEI2        MCEI1        MCEI0
   Access                                                                R/W          R/W          R/W          R/W
    Reset                                                                 0            0            0             0


         Bit        15                 14       13          12           11            10           9             8
                   TCEI1          TCEI0       TCINV1      TCINV0                    CNTEO         TRGEO        OVFEO
   Access          R/W             R/W         R/W         R/W                        R/W          R/W          R/W
    Reset            0                 0        0            0                         0            0             0


         Bit         7                 6        5            4            3            2            1             0
                         CNTSEL[1:0]                    EVACT1[2:0]                             EVACT0[2:0]
   Access          R/W             R/W         R/W         R/W           R/W          R/W          R/W          R/W
    Reset            0                 0        0            0            0            0            0             0


               Bits 24, 25, 26, 27 – MCEO Match or Capture Channel x Event Output Enable
               These bits control if the match/capture event on channel x is enabled and will be generated for every
               match or capture.
                Value      Description
                0          Match/capture x event is disabled and will not be generated.
                1          Match/capture x event is enabled and will be generated for every compare/capture on
                           channel x.

               Bits 16, 17, 18, 19 – MCEI Match or Capture Channel x Event Input Enable
               These bits indicate if the match/capture x incoming event is enabled
               These bits are used to enable match or capture input events to the CCx channel of TCC.
                Value      Description
                0          Incoming events are disabled.
                1          Incoming events are enabled.

               Bits 14, 15 – TCEI Timer/Counter Event Input x Enable
               This bit is used to enable input event x to the TCC.
                Value       Description
                0            Incoming event x is disabled.
                1            Incoming event x is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1857
                                                 SAM D5x/E5x Family Data Sheet
                                               TCC – Timer/Counter for Control Applications

Bits 12, 13 – TCINV Timer/Counter Event x Invert Enable
This bit inverts the event x input.
 Value       Description
 0           Input event source x is not inverted.
 1           Input event source x is inverted.

Bit 10 – CNTEO Timer/Counter Event Output Enable
This bit is used to enable the counter cycle event. When enabled, an event will be generated on begin or
end of counter cycle depending of CNTSEL[1:0] settings.
 Value       Description
 0            Counter cycle output event is disabled and will not be generated.
 1            Counter cycle output event is enabled and will be generated depend of CNTSEL[1:0] value.

Bit 9 – TRGEO Retrigger Event Output Enable
This bit is used to enable the counter retrigger event. When enabled, an event will be generated when the
counter retriggers operation.
 Value       Description
 0            Counter retrigger event is disabled and will not be generated.
 1            Counter retrigger event is enabled and will be generated for every counter retrigger.

Bit 8 – OVFEO Overflow/Underflow Event Output Enable
This bit is used to enable the overflow/underflow event. When enabled an event will be generated when
the counter reaches the TOP or the ZERO value.
 Value       Description
 0            Overflow/underflow counter event is disabled and will not be generated.
 1            Overflow/underflow counter event is enabled and will be generated for every counter
              overflow/underflow.

Bits 7:6 – CNTSEL[1:0] Timer/Counter Interrupt and Event Output Selection
These bits define on which part of the counter cycle the counter event output is generated.
 Value      Name          Description
 0x0        BEGIN         An interrupt/event is generated at begin of each counter cycle
 0x1        END           An interrupt/event is generated at end of each counter cycle
 0x2        BETWEEN An interrupt/event is generated between each counter cycle.
 0x3        BOUNDARY An interrupt/event is generated at begin of first counter cycle, and end of last
                          counter cycle.

Bits 5:3 – EVACT1[2:0] Timer/Counter Event Input 1 Action
These bits define the action the TCC will perform on TCE1 event input.
 Value      Name                   Description
 0x0        OFF                    Event action disabled.
 0x1        RETRIGGER              Start, restart or re-trigger TC on event
 0x2        DIR (asynch)           Direction control
 0x3        STOP                   Stop TC on event
 0x4        DEC                    Decrement TC on event
 0x5        PPW                    Period captured into CC0 Pulse Width on CC1
 0x6        PWP                    Period captured into CC1 Pulse Width on CC0
 0x7        FAULT                  Non-recoverable Fault




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1858
                                               SAM D5x/E5x Family Data Sheet
                                             TCC – Timer/Counter for Control Applications

Bits 2:0 – EVACT0[2:0] Timer/Counter Event Input 0 Action
These bits define the action the TCC will perform on TCE0 event input 0.
 Value      Name                     Description
 0x0        OFF                      Event action disabled.
 0x1        RETRIGGER                Start, restart or re-trigger TC on event
 0x2        COUNTEV                  Count on event.
 0x3        START                    Start TC on event
 0x4        INC                      Increment TC on EVENT
 0x5        COUNT (async)            Count on active state of asynchronous event
 0x6        STAMP                    Capture overflow times (Max value)
 0x7        FAULT                    Non-recoverable Fault




© 2019 Microchip Technology Inc.                 Datasheet                         DS60001507E-page 1859
                                                                 SAM D5x/E5x Family Data Sheet
                                                                TCC – Timer/Counter for Control Applications

49.8.10 Interrupt Enable Clear

            Name:        INTENCLR
            Offset:      0x24
            Reset:       0x00000000
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

      Bit        31            30            29            28            27            26            25           24


  Access
   Reset


      Bit        23            22            21            20            19            18            17           16
                                                                       MCx3          MCx2          MCx1          MCx0
  Access                                                                R/W           R/W           R/W           R/W
   Reset                                                                 0             0             0             0


      Bit        15            14            13            12            11            10            9             8
               FAULT1        FAULT0        FAULTB        FAULTA         DFS           UFS
  Access         R/W          R/W           R/W           R/W           R/W           R/W
   Reset          0             0             0            0             0             0


      Bit         7             6             5            4             3             2             1             0
                                                                        ERR           CNT           TRG           OVF
  Access                                                                R/W           R/W           R/W           R/W
   Reset                                                                 0             0             0             0


            Bits 16, 17, 18, 19 – MCx Match or Capture Channel x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the corresponding Match or Capture Channel x Interrupt Disable/Enable
            bit, which disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 15 – FAULT1 Non-Recoverable Fault x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Non-Recoverable Fault x Interrupt Disable/Enable bit, which disables
            the Non-Recoverable Fault x interrupt.
             Value        Description
             0            The Non-Recoverable Fault x interrupt is disabled.
             1            The Non-Recoverable Fault x interrupt is enabled.

            Bit 14 – FAULT0 Non-Recoverable Fault x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Non-Recoverable Fault x Interrupt Disable/Enable bit, which disables
            the Non-Recoverable Fault x interrupt.




        © 2019 Microchip Technology Inc.                          Datasheet                          DS60001507E-page 1860
                                                    SAM D5x/E5x Family Data Sheet
                                                  TCC – Timer/Counter for Control Applications

 Value        Description
 0            The Non-Recoverable Fault x interrupt is disabled.
 1            The Non-Recoverable Fault x interrupt is enabled.

Bit 13 – FAULTB Recoverable Fault B Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Recoverable Fault B Interrupt Disable/Enable bit, which disables the
Recoverable Fault B interrupt.
Value         Description
0             The Recoverable Fault B interrupt is disabled.
1             The Recoverable Fault B interrupt is enabled.

Bit 12 – FAULTA Recoverable Fault A Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Recoverable Fault A Interrupt Disable/Enable bit, which disables the
Recoverable Fault A interrupt.
Value         Description
0             The Recoverable Fault A interrupt is disabled.
1             The Recoverable Fault A interrupt is enabled.

Bit 11 – DFS Non-Recoverable Debug Fault Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Debug Fault State Interrupt Disable/Enable bit, which disables the
Debug Fault State interrupt.
Value         Description
0             The Debug Fault State interrupt is disabled.
1             The Debug Fault State interrupt is enabled.

Bit 10 – UFS Non-Recoverable Update Fault Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Non-Recoverable Update Fault Interrupt Disable/Enable bit, which
disables the Non-Recoverable Update Fault interrupt.
Note: This bit is only available on variant L devices. Refer to the Configuration Summary for more
information.
 Value        Description
 0            The Non-Recoverable Update Fault interrupt is disabled.
 1            The Non-Recoverable Update Fault interrupt is enabled.

Bit 3 – ERR Error Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Error Interrupt Disable/Enable bit, which disables the Compare
interrupt.
 Value        Description
 0            The Error interrupt is disabled.
 1            The Error interrupt is enabled.

Bit 2 – CNT Counter Interrupt Enable
Writing a '0' to this bit has no effect.




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1861
                                                    SAM D5x/E5x Family Data Sheet
                                                  TCC – Timer/Counter for Control Applications

Writing a '1' to this bit will clear the Counter Interrupt Disable/Enable bit, which disables the Counter
interrupt.
 Value        Description
 0            The Counter interrupt is disabled.
 1            The Counter interrupt is enabled.

Bit 1 – TRG Retrigger Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Retrigger Interrupt Disable/Enable bit, which disables the Retrigger
interrupt.
 Value        Description
 0            The Retrigger interrupt is disabled.
 1            The Retrigger interrupt is enabled.

Bit 0 – OVF Overflow Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Overflow Interrupt Disable/Enable bit, which disables the Overflow
interrupt request.
 Value        Description
 0            The Overflow interrupt is disabled.
 1            The Overflow interrupt is enabled.




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1862
                                                                 SAM D5x/E5x Family Data Sheet
                                                                TCC – Timer/Counter for Control Applications

49.8.11 Interrupt Enable Set

            Name:        INTENSET
            Offset:      0x28
            Reset:       0x00000000
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

      Bit        31            30            29            28            27            26            25           24


  Access
   Reset


      Bit        23            22            21            20            19            18            17           16
                                                                        MC3           MC2           MC1          MC0
  Access                                                                R/W           R/W           R/W           R/W
   Reset                                                                 0             0             0             0


      Bit        15            14            13            12            11            10            9             8
               FAULT1        FAULT0        FAULTB        FAULTA         DFS           UFS
  Access         R/W          R/W           R/W           R/W           R/W           R/W
   Reset          0             0             0            0             0             0


      Bit         7             6             5            4             3             2             1             0
                                                                        ERR           CNT           TRG           OVF
  Access                                                                R/W           R/W           R/W           R/W
   Reset                                                                 0             0             0             0


            Bits 16, 17, 18, 19 – MC Match or Capture Channel x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the corresponding Match or Capture Channel x Interrupt Disable/Enable bit,
            which enables the Match or Capture Channel x interrupt.
            Value         Description
            0             The Match or Capture Channel x interrupt is disabled.
            1             The Match or Capture Channel x interrupt is enabled.

            Bit 15 – FAULT1 Non-Recoverable Fault x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Non-Recoverable Fault x Interrupt Disable/Enable bit, which enables the
            Non-Recoverable Fault x interrupt.
            Value         Description
            0             The Non-Recoverable Fault x interrupt is disabled.
            1             The Non-Recoverable Fault x interrupt is enabled.

            Bit 14 – FAULT0 Non-Recoverable Fault x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Non-Recoverable Fault x Interrupt Disable/Enable bit, which disables
            the Non-Recoverable Fault x interrupt.




        © 2019 Microchip Technology Inc.                          Datasheet                          DS60001507E-page 1863
                                                    SAM D5x/E5x Family Data Sheet
                                                  TCC – Timer/Counter for Control Applications

 Value        Description
 0            The Non-Recoverable Fault x interrupt is disabled.
 1            The Non-Recoverable Fault x interrupt is enabled.

Bit 13 – FAULTB Recoverable Fault B Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Recoverable Fault B Interrupt Disable/Enable bit, which enables the
Recoverable Fault B interrupt.
Value         Description
0             The Recoverable Fault B interrupt is disabled.
1             The Recoverable Fault B interrupt is enabled.

Bit 12 – FAULTA Recoverable Fault A Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Recoverable Fault A Interrupt Disable/Enable bit, which enables the
Recoverable Fault A interrupt.
Value         Description
0             The Recoverable Fault A interrupt is disabled.
1             The Recoverable Fault A interrupt is enabled.

Bit 11 – DFS Non-Recoverable Debug Fault Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Debug Fault State Interrupt Disable/Enable bit, which enables the
Debug Fault State interrupt.
Value         Description
0             The Debug Fault State interrupt is disabled.
1             The Debug Fault State interrupt is enabled.

Bit 10 – UFS Non-Recoverable Update Fault Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Non-Recoverable Update Fault Interrupt Disable/Enable bit, which
enables the Non-Recoverable Update Fault interrupt.
Note: This bit is only available on variant L devices. Refer to the Configuration Summary for more
information.
 Value        Description
 0            The Non-Recoverable Update Fault interrupt is disabled.
 1            The Non-Recoverable Update Fault interrupt is enabled.

Bit 3 – ERR Error Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Error Interrupt Disable/Enable bit, which enables the Compare interrupt.
Value         Description
0             The Error interrupt is disabled.
1             The Error interrupt is enabled.

Bit 2 – CNT Counter Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Retrigger Interrupt Disable/Enable bit, which enables the Counter
interrupt.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1864
                                                    SAM D5x/E5x Family Data Sheet
                                                   TCC – Timer/Counter for Control Applications

 Value        Description
 0            The Counter interrupt is disabled.
 1            The Counter interrupt is enabled.

Bit 1 – TRG Retrigger Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Retrigger Interrupt Disable/Enable bit, which enables the Retrigger
interrupt.
 Value        Description
 0            The Retrigger interrupt is disabled.
 1            The Retrigger interrupt is enabled.

Bit 0 – OVF Overflow Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Overflow Interrupt Disable/Enable bit, which enables the Overflow
interrupt request.
 Value        Description
 0            The Overflow interrupt is disabled.
 1            The Overflow interrupt is enabled.




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1865
                                                                 SAM D5x/E5x Family Data Sheet
                                                                TCC – Timer/Counter for Control Applications

49.8.12 Interrupt Flag Status and Clear

            Name:        INTFLAG
            Offset:      0x2C
            Reset:       0x00000000
            Property:    -


      Bit        31            30            29            28            27            26            25           24


  Access
    Reset


      Bit        23            22            21            20            19            18            17           16
                                                                        MC3           MC2           MC1          MC0
  Access                                                                R/W           R/W           R/W           R/W
    Reset                                                                0             0             0             0


      Bit        15            14            13            12            11            10            9             8
               FAULT1        FAULT0        FAULTB        FAULTA         DFS           UFS
  Access         R/W          R/W           R/W           R/W           R/W           R/W
    Reset         0             0             0            0             0             0


      Bit         7             6             5            4             3             2             1             0
                                                                        ERR           CNT           TRG           OVF
  Access                                                                R/W           R/W           R/W           R/W
    Reset                                                                0             0             0             0


            Bits 16, 17, 18, 19 – MC Match or Capture Channel x Interrupt Flag
            This flag is set on the next CLK_TCC_COUNT cycle after a match with the compare condition or once
            CCx register contain a valid capture value.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In Capture operation, this flag is automatically cleared when CCx register is read.

            Bit 15 – FAULT1 Non-Recoverable Fault x Interrupt Flag
            This flag is set on the next CLK_TCC_COUNT cycle after a Non-Recoverable Fault x occurs.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Non-Recoverable Fault x interrupt flag.

            Bit 14 – FAULT0 Non-Recoverable Fault x Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Non-Recoverable Fault x Interrupt Disable/Enable bit, which disables
            the Non-Recoverable Fault x interrupt.
             Value        Description
             0            The Non-Recoverable Fault x interrupt is disabled.
             1            The Non-Recoverable Fault x interrupt is enabled.

            Bit 13 – FAULTB Recoverable Fault B Interrupt Flag
            This flag is set on the next CLK_TCC_COUNT cycle after a Recoverable Fault B occurs.




        © 2019 Microchip Technology Inc.                          Datasheet                          DS60001507E-page 1866
                                                     SAM D5x/E5x Family Data Sheet
                                                   TCC – Timer/Counter for Control Applications

Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the Recoverable Fault B interrupt flag.

Bit 12 – FAULTA Recoverable Fault A Interrupt Flag
This flag is set on the next CLK_TCC_COUNT cycle after a Recoverable Fault B occurs.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the Recoverable Fault B interrupt flag.

Bit 11 – DFS Non-Recoverable Debug Fault State Interrupt Flag
This flag is set on the next CLK_TCC_COUNT cycle after an Debug Fault State occurs.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the Debug Fault State interrupt flag.

Bit 10 – UFS Non-Recoverable Update Fault
This flag is set when the RAMP index changes and the Lock Update bit is set (CTRLBSET.LUPD).
Writing a zero to this bit has no effect.
Writing a one to this bit clears the Non-Recoverable Update Fault interrupt flag.
Note: This bit is only available on variant L devices. Refer to the Configuration Summary for more
information.

Bit 3 – ERR Error Interrupt Flag
This flag is set if a new capture occurs on a channel when the corresponding Match or Capture Channel x
interrupt flag is one. In which case there is nowhere to store the new capture.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the error interrupt flag.

Bit 2 – CNT Counter Interrupt Flag
This flag is set on the next CLK_TCC_COUNT cycle after a counter event occurs.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the CNT interrupt flag.

Bit 1 – TRG Retrigger Interrupt Flag
This flag is set on the next CLK_TCC_COUNT cycle after a counter retrigger occurs.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the re-trigger interrupt flag.

Bit 0 – OVF Overflow Interrupt Flag
This flag is set on the next CLK_TCC_COUNT cycle after an overflow condition occurs.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the Overflow interrupt flag.




© 2019 Microchip Technology Inc.                       Datasheet                     DS60001507E-page 1867
                                                                SAM D5x/E5x Family Data Sheet
                                                               TCC – Timer/Counter for Control Applications

49.8.13 Status

           Name:        STATUS
           Offset:      0x30
           Reset:       0x00000001
           Property:    -


     Bit        31            30             29           28            27           26            25            24
                                                                      CMP3          CMP2          CMP1         CMP0
  Access                                                               R/W           R/W          R/W           R/W
   Reset                                                                0             0             0            0


     Bit        23            22             21           20            19           18            17            16
                                                                    CCBUFV3       CCBUFV2       CCBUFV1       CCBUFV0
  Access                                                               R/W           R/W          R/W           R/W
   Reset                                                                0             0             0            0


     Bit        15            14             13           12            11           10             9            8
              FAULT1        FAULT0         FAULTB      FAULTA       FAULT1IN      FAULT0IN      FAULTBIN      FAULTAIN
  Access        R/W          R/W            R/W          R/W            R             R             R            R
   Reset         0             0             0            0             0             0             0            0


     Bit         7             6             5            4             3             2             1            0
             PERBUFV                      PATTBUFV      SLAVE          DFS           UFS           IDX         STOP
  Access        R/W                         R/W           R            R/W           R/W            R            R
   Reset         0                           0            0             0             0             0            1


           Bits 24, 25, 26, 27 – CMP Channel x Compare Value
           This bit reflects the channel x output compare value.
            Value        Description
            0            Channel compare output value is 0.
            1            Channel compare output value is 1.

           Bits 16, 17, 18, 19 – CCBUFV Channel x Compare or Capture Buffer Valid
           For a compare channel, this bit is set when a new value is written to the corresponding CCBUFx register.
           The bit is cleared either by writing a '1' to the corresponding location when CTRLB.LUPD is set, or
           automatically on an UPDATE condition.
           For a capture channel, the bit is set when a valid capture value is stored in the CCBUFx register. The bit
           is automatically cleared when the CCx register is read.

           Bits 14, 15 – FAULT Non-recoverable Fault x State
           This bit is set by hardware as soon as non-recoverable Fault x condition occurs.
           This bit is cleared by writing a one to this bit and when the corresponding FAULTxIN status bit is low.
           Once this bit is clear, the timer/counter will restart from the last COUNT value. To restart the timer/counter
           from BOTTOM, the timer/counter restart command must be executed before clearing the corresponding
           STATEx bit. For further details on timer/counter commands, refer to available commands description
           (49.8.3 CTRLBSET.CMD).




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 1868
                                                   SAM D5x/E5x Family Data Sheet
                                                 TCC – Timer/Counter for Control Applications

Bit 13 – FAULTB Recoverable Fault B State
This bit is set by hardware as soon as recoverable Fault B condition occurs.
This bit can be clear by hardware when Fault B action is resumed, or by writing a '1' to this bit when the
corresponding FAULTBIN bit is low. If software halt command is enabled (FAULTB.HALT=SW), clearing
this bit will release the timer/counter.

Bit 12 – FAULTA Recoverable Fault A State
This bit is set by hardware as soon as recoverable Fault A condition occurs.
This bit can be clear by hardware when Fault A action is resumed, or by writing a '1' to this bit when the
corresponding FAULTAIN bit is low. If software halt command is enabled (FAULTA.HALT=SW), clearing
this bit will release the timer/counter.

Bit 11 – FAULT1IN Non-Recoverable Fault 1 Input
This bit is set while an active Non-Recoverable Fault 1 input is present.

Bit 10 – FAULT0IN Non-Recoverable Fault 0 Input
This bit is set while an active Non-Recoverable Fault 0 input is present.

Bit 9 – FAULTBIN Recoverable Fault B Input
This bit is set while an active Recoverable Fault B input is present.

Bit 8 – FAULTAIN Recoverable Fault A Input
This bit is set while an active Recoverable Fault A input is present.

Bit 7 – PERBUFV Period Buffer Valid
This bit is set when a new value is written to the PERBUF register. This bit is automatically cleared by
hardware on UPDATE condition when CTRLB.LUPD is set, or by writing a '1' to this bit.

Bit 5 – PATTBUFV Pattern Generator Value Buffer Valid
This bit is set when a new value is written to the PATTBUF register. This bit is automatically cleared by
hardware on UPDATE condition when CTRLB.LUPD is set, or by writing a '1' to this bit.

Bit 4 – SLAVE Slave
This bit is set when TCC is set in Slave mode. This bit follows the CTRLA.MSYNC bit state.

Bit 3 – DFS Debug Fault State
This bit is set by hardware in Debug mode when DDBGCTRL.FDDBD bit is set. The bit is cleared by
writing a '1' to this bit and when the TCC is not in Debug mode.
When the bit is set, the counter is halted and the Waveforms state depend on DRVCTRL.NRE and
DRVCTRL.NRV registers.

Bit 2 – UFS Non-recoverable Update Fault State
This bit is set by hardware when the RAMP index changes and the Lock Update bit is set
(CTRLBSET.LUPD). The bit is cleared by writing a one to this bit.
When the bit is set, the waveforms state depend on DRVCTRL.NRE and DRVCTRL.NRV registers.

Bit 1 – IDX Ramp Index
In RAMP2 and RAMP2A operation, the bit is cleared during the cycle A and set during the cycle B. In
RAMP1 operation, the bit always reads zero. For details on ramp operations, refer to 49.6.3.4 Ramp
Operations.




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1869
                                              SAM D5x/E5x Family Data Sheet
                                            TCC – Timer/Counter for Control Applications

Bit 0 – STOP Stop
This bit is set when the TCC is disabled either on a STOP command or on an UPDATE condition when
One-Shot operation mode is enabled (CTRLBSET.ONESHOT=1).
This bit is clear on the next incoming counter increment or decrement.
 Value        Description
 0            Counter is running.
 1            Counter is stopped.




© 2019 Microchip Technology Inc.               Datasheet                       DS60001507E-page 1870
                                                               SAM D5x/E5x Family Data Sheet
                                                             TCC – Timer/Counter for Control Applications

49.8.14 Counter Value

           Name:       COUNT
           Offset:     0x34
           Reset:      0x00000000
           Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized

           Note: Prior to any read access, this register must be synchronized by user by writing the according TCC
           Command value to the Control B Set register (CTRLBSET.CMD=READSYNC).

     Bit        31            30           29           28                 27          26         25           24


  Access
   Reset


     Bit        23            22           21           20                 19          18         17           16
                                                             COUNT[23:16]
  Access       R/W           R/W          R/W           R/W            R/W             R/W        R/W         R/W
   Reset         0            0             0            0                  0           0          0           0


     Bit        15            14           13           12                 11          10          9           8
                                                             COUNT[15:8]
  Access       R/W           R/W          R/W           R/W            R/W             R/W        R/W         R/W
   Reset         0            0             0            0                  0           0          0           0


     Bit         7            6             5            4                  3           2          1           0
                                                              COUNT[7:0]
  Access       R/W           R/W          R/W           R/W            R/W             R/W        R/W         R/W
   Reset         0            0             0            0                  0           0          0           0


           Bits 23:0 – COUNT[23:0] Counter Value
           These bits hold the value of the Counter register.
           Note: When the TCC is configured as 16-bit timer/counter, the excess bits are read zero.
           Note: This bit field occupies the MSB of the register, [23:m]. m is dependent on the Resolution bit in the
           Control A register (CTRLA.RESOLUTION):

           CTRLA.RESOLUTION                                                     Bits [23:m]
           0x0 - NONE                                                           23:0 (depicted)
           0x1 - DITH4                                                          23:4
           0x2 - DITH5                                                          23:5
           0x3 - DITH6                                                          23:6




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 1871
                                                                SAM D5x/E5x Family Data Sheet
                                                               TCC – Timer/Counter for Control Applications

49.8.15 Pattern

            Name:        PATT
            Offset:      0x38
            Reset:       0x0000
            Property:    Write-Synchronized


      Bit        15            14            13           12               11         10            9             8
                                                                PGV[7:0]
  Access         R/W          R/W           R/W           R/W              R/W       R/W           R/W          R/W
   Reset          0             0             0            0                0         0             0             0


      Bit         7             6             5            4                3         2             1             0
                                                                PGE[7:0]
  Access         R/W          R/W           R/W           R/W              R/W       R/W           R/W          R/W
   Reset          0             0             0            0                0         0             0             0


            Bits 15:8 – PGV[7:0] Pattern Generation Output Value
            This register holds the values of pattern for each waveform output.

            Bits 7:0 – PGE[7:0] Pattern Generation Output Enable
            This register holds the enable status of pattern generation for each waveform output. A bit written to '1'
            will override the corresponding SWAP output with the corresponding PGVn value.




        © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1872
                                                                  SAM D5x/E5x Family Data Sheet
                                                                 TCC – Timer/Counter for Control Applications

49.8.16 Waveform

           Name:       WAVE
           Offset:     0x3C
           Reset:      0x00000000
           Property:   Write-Synchronized


     Bit        31            30           29               28           27        26           25            24
                                                                       SWAP3     SWAP2        SWAP1         SWAP0
  Access                                                                R/W       R/W           R/W          R/W
   Reset                                                                 0          0            0            0


     Bit        23            22           21               20           19        18           17            16
                                          POL5          POL4            POL3      POL2         POL1         POL0
  Access                                  R/W               R/W         R/W       R/W           R/W          R/W
   Reset                                    0                0           0          0            0            0


     Bit        15            14           13               12           11        10            9            8
                                                                      CICCEN3   CICCEN2      CICCEN1       CICCEN0
  Access                                                                R/W       R/W           R/W          R/W
   Reset                                                                 0          0            0            0


     Bit         7            6             5                4           3          2            1            0
             CIPEREN                            RAMP[1:0]                                  WAVEGEN[2:0]
  Access       R/W                        R/W               R/W                   R/W           R/W          R/W
   Reset         0                          0                0                      0            0            0


           Bits 24, 25, 26, 27 – SWAP Swap DTI Output Pair x
           Setting these bits enables output swap of DTI outputs [x] and [x+WO_NUM/2]. Note the DTIxEN settings
           will not affect the swap operation.

           Bits 16, 17, 18, 19, 20, 21 – POL Channel Polarity x
           Setting these bits enables the output polarity in single-slope and dual-slope PWM operations.
           Value       Name                             Description
           0           (single-slope PWM waveform Compare output is initialized to ~DIR and set to DIR when
                       generation)                      TCC counter matches CCx value
           1           (single-slope PWM waveform Compare output is initialized to DIR and set to ~DIR when
                       generation)                      TCC counter matches CCx value.
           0           (dual-slope PWM waveform Compare output is set to ~DIR when TCC counter matches
                       generation)                      CCx value
           1           (dual-slope PWM waveform Compare output is set to DIR when TCC counter matches
                       generation)                      CCx value.

           Bits 8, 9, 10, 11 – CICCEN Circular CC Enable x
           Setting this bits enables the compare circular buffer option on the first four Compare/Capture channels.
           When the bit is set, CCx register value is copied-back into the CCx register on UPDATE condition.




       © 2019 Microchip Technology Inc.                            Datasheet                    DS60001507E-page 1873
                                                         SAM D5x/E5x Family Data Sheet
                                                      TCC – Timer/Counter for Control Applications

Bit 7 – CIPEREN Circular Period Enable
Setting this bits enable the period circular buffer option. When the bit is set, the PER register value is
copied-back into the PERB register on UPDATE condition.

Bits 5:4 – RAMP[1:0] Ramp Operation
These bits select Ramp operation (RAMP). These bits are not synchronized.
 Value      Name                   Description
 0x0        RAMP1                  RAMP1 operation
 0x1        RAMP2A                 Alternative RAMP2 operation
 0x2        RAMP2                  RAMP2 operation
 0x3        RAMP2C                 Critical RAMP2 operation
 0x4        -                      Reserved

Bits 2:0 – WAVEGEN[2:0] Waveform Generation Operation
These bits select the waveform generation operation. The settings impact the top value and control if
frequency or PWM waveform generation should be used. These bits are not synchronized.
 Value   Name            Description

                         Operation          Top   Update       Waveform Output   Waveform Output   OVFIF/Event
                                                               On Match          On Update         Up Down

 0x0     NFRQ            Normal Frequency   PER   TOP/Zero     Toggle            Stable            TOP   Zero

 0x1     MFRQ            Match Frequency    CC0   TOP/Zero     Toggle            Stable            TOP   Zero

 0x2     NPWM            Normal PWM         PER   TOP/Zero     Set               Clear             TOP   Zero

 0x3     Reserved        -                  -     -            -                 -                 -     -

 0x4     DSCRITICAL      Dual-slope PWM     PER   Zero         ~DIR              Stable            –     Zero

 0x5     DSBOTTOM        Dual-slope PWM     PER   Zero         ~DIR              Stable            –     Zero

 0x6     DSBOTH          Dual-slope PWM     PER   TOP & Zero   ~DIR              Stable            TOP   Zero

 0x7     DSTOP           Dual-slope PWM     PER   Zero         ~DIR              Stable            TOP   –




© 2019 Microchip Technology Inc.                           Datasheet                      DS60001507E-page 1874
                                                                SAM D5x/E5x Family Data Sheet
                                                              TCC – Timer/Counter for Control Applications

49.8.17 Period Value

            Name:        PER
            Offset:      0x40
            Reset:       0xFFFFFFFF
            Property:    Write-Synchronized


      Bit        31              30         29           28                 27                 26     25           24


  Access
   Reset


      Bit        23              22         21           20                 19                 18     17           16
                                                               PER[17:10]
  Access        R/W              R/W       R/W           R/W                R/W            R/W        R/W         R/W
   Reset          1               1           1           1                  1                 1       1           1


      Bit        15              14         13           12                 11                 10      9           8
                                                                PER[9:2]
  Access        R/W              R/W       R/W           R/W                R/W            R/W        R/W         R/W
   Reset          1               1           1           1                  1                 1       1           1


      Bit         7               6           5           4                  3                 2       1           0
                      PER[1:0]                                                   DITHER[5:0]
  Access        R/W              R/W       R/W           R/W                R/W            R/W        R/W         R/W
   Reset          1               1           1           1                  1                 1       1           1


            Bits 23:6 – PER[17:0] Period Value
            These bits hold the value of the Period Buffer register.
            Note: When the TCC is configured as 16-bit timer/counter, the excess bits are read zero.
            Note: This bit field occupies the MSB of the register, [23:m]. m is dependent on the Resolution bit in the
            Control A register (CTRLA.RESOLUTION):

            CTRLA.RESOLUTION                                                        Bits [23:m]
            0x0 - NONE                                                              23:0
            0x1 - DITH4                                                             23:4
            0x2 - DITH5                                                             23:5
            0x3 - DITH6                                                             23:6 (depicted)

            Bits 5:0 – DITHER[5:0] Dithering Cycle Number
            These bits hold the number of extra cycles that are added on the PWM pulse period every 64 PWM
            frames.




        © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 1875
                                                  SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

Note: This bit field consists of the n LSB of the register. n is dependent on the value of the Resolution
bits in the Control A register (CTRLA.RESOLUTION):

 CTRLA.RESOLUTION                                                  Bits [n:0]
 0x0 - NONE                                                        -
 0x1 - DITH4                                                       3:0
 0x2 - DITH5                                                       4:0
 0x3 - DITH6                                                       5:0 (depicted)




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1876
                                                              SAM D5x/E5x Family Data Sheet
                                                             TCC – Timer/Counter for Control Applications

49.8.18 Compare/Capture Channel x

           Name:         CC
           Offset:       0x44 + n*0x04 [n=0..5]
           Reset:        0x00000000
           Property:     Write-Synchronized, Read-Synchronized

           The CCx register represents the 16-, 24- bit value, CCx. The register has two functions, depending of the
           mode of operation.
           For capture operation, this register represents the second buffer level and access point for the CPU and
           DMA.
           For compare operation, this register is continuously compared to the counter value. Normally, the output
           form the comparator is then used for generating waveforms.
           CCx register is updated with the buffer value from their corresponding CCBUFx register when an
           UPDATE condition occurs.
           In addition, in match frequency operation, the CC0 register controls the counter period.

     Bit        31               30        29           28                27                 26   25           24


  Access
   Reset


     Bit        23               22        21           20                19                 18   17           16
                                                              CC[17:10]
  Access       R/W               R/W      R/W           R/W               R/W            R/W      R/W         R/W
   Reset         0                0         0            0                 0                 0     0           0


     Bit        15               14        13           12                11                 10    9           8
                                                               CC[9:2]
  Access       R/W               R/W      R/W           R/W               R/W            R/W      R/W         R/W
   Reset         0                0         0            0                 0                 0     0           0


     Bit         7                6         5            4                 3                 2     1           0
                       CC[1:0]                                                 DITHER[5:0]
  Access       R/W               R/W      R/W           R/W               R/W            R/W      R/W         R/W
   Reset         0                0         0            0                 0                 0     0           0


           Bits 23:6 – CC[17:0] Channel x Compare/Capture Value
           These bits hold the value of the Channel x compare/capture register.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1877
                                                  SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

Note:
 1. When the TCC is configured as a 16-bit timer/counter, the excess bits are read as zero.
 2. This bit field occupies the MSB of the register, [23:m]. m is dependent on the Resolution bit in the
      Control A register (CTRLA.RESOLUTION):

 CTRLA.RESOLUTION                                                Bits [23:m]
 0x0 - NONE                                                      23:0
 0x1 - DITH4                                                     23:4
 0x2 - DITH5                                                     23:5
 0x3 - DITH6                                                     23:6 (depicted)

Bits 5:0 – DITHER[5:0] Dithering Cycle Number
These bits hold the number of extra cycles that are added on the PWM pulse width every 64 PWM
frames.
Note: This bit field consists of the n LSB of the register. n is dependent on the value of the Resolution
bits in the Control A register (CTRLA.RESOLUTION):

 CTRLA.RESOLUTION                                                  Bits [n:0]
 0x0 - NONE                                                        -
 0x1 - DITH4                                                       3:0
 0x2 - DITH5                                                       4:0
 0x3 - DITH6                                                       5:0 (depicted)




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1878
                                                                   SAM D5x/E5x Family Data Sheet
                                                                  TCC – Timer/Counter for Control Applications

49.8.19 Pattern Buffer

            Name:        PATTBUF
            Offset:      0x64
            Reset:       0x0000
            Property:    Write-Synchronized, Read-Synchronized


      Bit         15            14            13             12                11        10             9             8
                                                                  PGVB0[7:0]
  Access         R/W           R/W           R/W            R/W                R/W      R/W            R/W           R/W
   Reset          0             0              0             0                  0         0             0             0


      Bit         7             6              5             4                  3         2             1             0
                                                                  PGEB0[7:0]
  Access         R/W           R/W           R/W            R/W                R/W      R/W            R/W           R/W
   Reset          0             0              0             0                  0         0             0             0


            Bits 8:15, 16:23, 24:31, 32:39, 40:47, 48:55, 56:63, 64:71 – PGVB Pattern Generation Output Value
            Buffer
            This register is the buffer for the PGV register. If double buffering is used, valid content in this register is
            copied to the PGV register on an UPDATE condition.

            Bits 0:7, 8:15, 16:23, 24:31, 32:39, 40:47, 48:55, 56:63 – PGEB Pattern Generation Output Enable
            Buffer
            This register is the buffer of the PGE register. If double buffering is used, valid content in this register is
            copied into the PGE register at an UPDATE condition.




        © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 1879
                                                               SAM D5x/E5x Family Data Sheet
                                                              TCC – Timer/Counter for Control Applications

49.8.20 Period Buffer Value

            Name:         PERBUF
            Offset:       0x6C
            Reset:        0xFFFFFFFF
            Property:     Write-Synchronized, Read-Synchronized


      Bit        31                 30      29           28                 27          26         25           24


  Access
   Reset


      Bit        23                 22      21           20                 19          18         17           16
                                                           PERBUF[17:10]
  Access        R/W             R/W        R/W           R/W            R/W             R/W        R/W         R/W
   Reset          1                 1        1            1                 1            1          1           1


      Bit        15                 14      13           12                 11          10          9           8
                                                              PERBUF[9:2]
  Access        R/W             R/W        R/W           R/W            R/W             R/W        R/W         R/W
   Reset          1                 1        1            1                 1            1          1           1


      Bit         7                 6        5            4                 3            2          1           0
                      PERBUF[1:0]                                           DITHERBUF[5:0]
  Access        R/W             R/W        R/W           R/W            R/W             R/W        R/W         R/W
   Reset          1                 1        1            1                 1            1          1           1


            Bits 23:6 – PERBUF[17:0] Period Buffer Value
            These bits hold the value of the Period Buffer register. The value is copied to PER register on UPDATE
            condition.
            Note: When the TCC is configured as 16-bit timer/counter, the excess bits are read zero.
            Note: This bit field occupies the MSB of the register, [23:m]. m is dependent on the Resolution bit in the
            Control A register (CTRLA.RESOLUTION):

            CTRLA.RESOLUTION                                                     Bits [23:m]
            0x0 - NONE                                                           23:0
            0x1 - DITH4                                                          23:4
            0x2 - DITH5                                                          23:5
            0x3 - DITH6                                                          23:6 (depicted)

            Bits 5:0 – DITHERBUF[5:0] Dithering Buffer Cycle Number
            These bits represent the PER.DITHER bits buffer. When the double buffering is enabled, the value of this
            bit field is copied to the PER.DITHER bits on an UPDATE condition.




        © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1880
                                                  SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

Note: This bit field consists of the n LSB of the register. n is dependent on the value of the Resolution
bits in the Control A register (CTRLA.RESOLUTION):

 CTRLA.RESOLUTION                                                  Bits [n:0]
 0x0 - NONE                                                        -
 0x1 - DITH4                                                       3:0
 0x2 - DITH5                                                       4:0
 0x3 - DITH6                                                       5:0 (depicted)




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1881
                                                              SAM D5x/E5x Family Data Sheet
                                                             TCC – Timer/Counter for Control Applications

49.8.21 Channel x Compare/Capture Buffer Value

           Name:         CCBUF
           Offset:       0x70 + n*0x04 [n=0..5]
           Reset:        0x00000000
           Property:     Write-Synchronized, Read-Synchronized

           CCBUFx is copied into CCx at TCC update time

     Bit        31                30      29            28                27           26        25           24


  Access
   Reset


     Bit        23                22      21            20                19           18        17           16
                                                            CCBUF[17:10]
  Access       R/W            R/W         R/W          R/W            R/W             R/W        R/W         R/W
   Reset         0                0        0            0                  0            0         0           0


     Bit        15                14      13            12                11           10         9           8
                                                             CCBUF[9:2]
  Access       R/W            R/W         R/W          R/W            R/W             R/W        R/W         R/W
   Reset         0                0        0            0                  0            0         0           0


     Bit         7                6        5            4                  3            2         1           0
                     CCBUF[1:0]                                            DITHERBUF[5:0]
  Access       R/W            R/W         R/W          R/W            R/W             R/W        R/W         R/W
   Reset         0                0        0            0                  0            0         0           0


           Bits 23:6 – CCBUF[17:0] Channel x Compare/Capture Buffer Value
           These bits hold the value of the Channel x Compare/Capture Buffer Value register. The register serves as
           the buffer for the associated compare or capture registers (CCx). Accessing this register using the CPU
           or DMA will affect the corresponding CCBUFVx status bit.
           Note:
             1. When the TCC is configured as a 16-bit timer/counter, the excess bits are read as zero.
             2. This bit field occupies the MSB of the register, [23:m]. m is dependent on the Resolution bit in the
                 Control A register (CTRLA.RESOLUTION):

           CTRLA.RESOLUTION                                                    Bits [23:m]
           0x0 - NONE                                                          23:0
           0x1 - DITH4                                                         23:4
           0x2 - DITH5                                                         23:5
           0x3 - DITH6                                                         23:6 (depicted)

           Bits 5:0 – DITHERBUF[5:0] Dithering Buffer Cycle Number
           These bits represent the CCx.DITHER bits buffer. When the double buffering is enable, DITHERBUF bits
           value is copied to the CCx.DITHER bits on an UPDATE condition.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 1882
                                                  SAM D5x/E5x Family Data Sheet
                                                TCC – Timer/Counter for Control Applications

Note: This bit field consists of the n LSB of the register. n is dependent on the value of the Resolution
bits in the Control A register (CTRLA.RESOLUTION):

 CTRLA.RESOLUTION                                                  Bits [n:0]
 0x0 - NONE                                                        -
 0x1 - DITH4                                                       3:0
 0x2 - DITH5                                                       4:0
 0x3 - DITH6                                                       5:0 (depicted)




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1883
