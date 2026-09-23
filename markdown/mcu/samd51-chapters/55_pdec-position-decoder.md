# 53. PDEC – Position Decoder

*Source: `Atmel-SAMD51.pdf`, pages 1946-1985 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                                   PDEC – Position Decoder


53.    PDEC – Position Decoder

53.1   Overview
       The PDEC consists of a Quadrature / Hall decoder, following by a counter, with two compare channels.
       The counter can be split into two parts to report the angular position and the number of revolutions. If the
       quadrature decoder feature is not suitable for specific applications, the PDEC module can be used as an
       additional time base.



53.2   Features
         • Internal prescaler
         • Selectable mode of operation:
             – QDEC, HALL or COUNTER
         • QDEC
             – Angular and revolution counts
             – Synchronous and asynchronous velocity measurements
             – Direction change detection
             – Check valid quadrature transitions
             – Check index position versus angular position
             – Auto correction mode
         • HALL
             – Window validation of Hall transitions
             – Hall code detection
             – Direction change detection
             – Check valid Hall transitions
             – Programmable event generation delay after a Hall transition
         • COUNTER
             – 16-bit counter with two compare channels
             – One of the compare channels can be configured with period settings
             – Counter overflow interrupt and event generation option
             – Compare match interrupt and event generation option




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1946
                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                     PDEC – Position Decoder


53.3     Block Diagram
         Figure 53-1. Block Diagram

                                   0




                                       EVEI
                           EVINV
           QDEC_EV[0]
                                                       Signal 0                                CC1                   MC1 (Interrupt or Event)




                                                                  sync
                                               PINEN
                                                                                               CC0                   MC0 (Interrupt or Event)
                                       PINVE



           PDEC[0]


                                                                                              COUNT                  OVF (Interrupt or Event)


                                   0
                                       EVEI
                           EVINV




           QDEC_EV[1]
                                                       Signal 1
                                               PINEN




                                                                  sync




                                                                                  Control
                                                                         Filter




                                                                                   Logic
                                       PINVE




           PDEC[1]




                                   0
                                                                                                                     VLC (Interrupt or Event)
                                       EVEI
                           EVINV




           QDEC_EV[2]                                                                                                DIR (Interrupt or Event)
                                                       Signal 2
                                               PINEN




                                                                  sync




                                                                                                                     ERR (Interrupt or Event)
                                       PINVE




           PDEC[2]




53.4     Signal Description
          Signal Name                                       Type                                       Description
          PDEC[2:0]                                         Digital input                              PDEC inputs

         Note: One signal can be mapped on one of several pins.
         Related Links
         6. I/O Multiplexing and Considerations



53.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

53.5.1   I/O Lines
         Using the I/O lines requires the I/O pins to be configured using the PORT configuration (PORT).

         Related Links
         32. PORT - I/O Pin Controller

53.5.2   Power Management
         The PDEC can be configured to operate in any sleep mode. The PDEC can wake up the device using
         interrupts from any sleep mode or perform actions through the Event System.
         Related Links




         © 2019 Microchip Technology Inc.                                         Datasheet                   DS60001507E-page 1947
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      PDEC – Position Decoder

         18. PM – Power Manager

53.5.3   Clocks

         A generic clock (GCLK_PDEC) is required to clock the PDEC. This clock must be configured and enabled
         in the generic clock controller before using the PDEC.
         This generic clock is asynchronous to the bus clock (CLK_PDEC_APB). Due to this asynchronicity, writes
         to certain registers will require synchronization between the clock domains.
         Related Links
         14. GCLK - Generic Clock Controller
         13.3 Register Synchronization

53.5.4   DMA
         Not applicable.

53.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first. Refer to Nested Vector Interrupt
         Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller
         10.2.1 Overview
         10.2.2 Interrupt Line Mapping

53.5.6   Events
         The events of this peripheral are connected to the Event System.
         Related Links
         31. EVSYS – Event System

53.5.7   Debug Operation
         When the CPU is halted in debug mode the PDEC will halt normal operation. The PDEC can be forced to
         continue operation during debugging. Refer to DBGCTRL register for details.

53.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           •   Interrupt Flag register (INTFLAG)
           •   Filter register (FILTER)
           •   Precaler register (PRESC)
           •   Compare x Value register (CCx)
           •   Channel x Compare Buffer Value register (CCBUFx)
           •   Status register (STATUS)
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1948
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      PDEC – Position Decoder

          Related Links
          27. PAC - Peripheral Access Controller

53.5.9    Analog Connections
          Not applicable.


53.6      Functional Description

53.6.1    Principle of Operation
          The PDEC control logic can be driven by a set of three inputs signal coming from Event System channels
          or I/O input pins. These three inputs can be filtered prior to down-stream processing. The input polarity,
          phase definition and other factors are configurable. QDEC, HALL or COUNTER mode of operation are
          supported.
          Depending of the mode configuration, specific input sequences can generate:
           •    State change
           •    Counter increment or decrement
           •    Interrupts
           •    Output events

53.6.2    Basic Operation
53.6.2.1 Initialization
          The following PDEC registers are enable-protected, meaning they can only be written when the PDEC is
          disabled (CTRLA.ENABLE is zero):
           • Event Control register (EVCTRL)
          Enable-protected bits in the CTRLA register can be written at the same time as CTRLA.ENABLE is
          written to '1', but not at the same time as CTRLA.ENABLE is written to '0'.
          Enable-protection is denoted by the 'Enable-Protected' property in the register description.
53.6.2.2 Enabling, Disabling, and Resetting
          The PDEC must be configured before it is enabled by the following steps:
           1.    Enable the PDEC bus clock (CLK_PDEC_APB)
           2.    Select the mode of operation by writing the Mode bits in the Control A register (CTRLA.MODE)
           3.    Select the PDEC mode configuration by writing the Configuration bits in the Control A register
                 (CTRLA.CONF)
           4.    Select the PDEC event or pin input signal source by writing the Event Enable Input bit in the Event
                 Control register (EVCTRL.EVEI) or by the Pin Enable bit in Control A register (CTRLA.PINEN)
           5.    Select the angular counter length value by writing the Angular bits in the Control A register
                 (CTRLA.ANGULAR)
          Optionally, the following configurations can be set before enabling PDEC:
           • The GCLK_PDEC clock can be prescaled by writing to the Prescaler register (PRESC)
           • A filter can be applied to the input signal by writing a corresponding value to the Filter register
             (FILTER)
           • If the resolution of the rotary sensor is not a power of 2, an Angular period can be set
             (CTRLA.PEREN and CC0 register)




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1949
                                                                         SAM D5x/E5x Family Data Sheet
                                                                                            PDEC – Position Decoder

         The PDEC is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The
         PDEC is disabled by writing a '0' to CTRLA.ENABLE.
         In QDEC or HALL operation modes, PDEC decoding is enabled writing a START command in the Control
         B Set register (CTRLBSET.CMD=START). The PDEC decoding is disabled writing a STOP command in
         the Control B Set register (CTRLBSET.CMD=STOP).
         The PDEC is reset by writing a '1' to the Software Reset bit in the Control A register (CTRLA.SWRST). All
         registers in the PDEC, except DBGCTRL, will be reset to their initial state, and the PDEC will be disabled.
         The PDEC should be disabled before the PDEC is reset to avoid undefined behavior.
53.6.2.3 Prescaler Selection
         The GCLK_PDEC is fed into the internal prescaler. Prescaler outputs from 1 to 1/1024 are directly
         available for selection by the counter and all selections are available in Prescaler register (PRESC). If the
         prescaler value is higher than 0x01, the counter update condition is executed on the next prescaled clock
         pulse.
         If the counter is set to count events, the internal prescaler is bypassed and the GCLK_PDEC clock is
         automatically selected during operation. The prescaler clock is also enabled when the input filtering is
         required.
         Figure 53-2. Prescaler Selection

                                                                         PRESC           EVACT




           GCLK_PDEC                Prescaler
                                                        GCLK_PDEC /                                                COUNT
                                                    {1,2,4,8,64,256,1024 }       EVENT           CLK_PDEC



53.6.2.4 Input Selection and Filtering
         The QDEC and HALL operations require three inputs, as shown in the Block Diagram. Each input can
         either be a dedicated I/O pin or an Event system channel. This is selected by writing to the corresponding
         Event x Enable bit in the Event Control register (EVCTRL.EVEIx) or Pin x Enable bit in the Control A
         register (CTRLA.PINENx).
         The I/O input pin active level can be inverted by writing to the corresponding Pin x Inversion Enable bit in
         Control A register (CTRLA.PINVENx). In the same way, the event input active level can be inverted by
         writing to the corresponding Inverted Event x Input Enable bit in Event Control register
         (EVCTRL.EVINVx).
         All input signals can be filtered before they are fed into the control logic. The FILTER register is used to
         configure the minimum duration for which the input signal has to be valid. The input signal minimum
         duration must be FILTER* tGCLK_PDEC .
         Figure 53-3. Input Signal Filtering

                    Pescaled Clock

                   (Signal 0, Signal 1, Signal 2)


                    Filter Out




        © 2019 Microchip Technology Inc.                                     Datasheet                      DS60001507E-page 1950
                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                                         PDEC – Position Decoder

         Only the first two input signals can be swapped by writing to the SWAP bit in the Control A register
         (CTRLA.SWAP).
         Related Links
         53.3 Block Diagram

53.6.2.5 Period Control
         The Channel Compare 0 register (CC0) can act as a period register (PER) by writing the PEREN bit in
         the Control A register (CTRLA.PEREN) to '1'. The PER can be used to control the top value (TOP) of the
         counting operation:
         When up-counting and the counter reaches the value of CC0, the counter is cleared to zero. When down-
         counting and the counter reaches zero, the counter is reloaded with the CC0 value.
53.6.2.6 QDEC Operation Mode
         In QDEC mode of operation, Signal 0 and Signal 1 control logic inputs refer to Phase A and Phase B in
         X4 mode, and to count/direction in X2 mode. The Signal 2 control logic input refers to the Index, in both
         X4 and X2 mode of operation. In X4 mode, a simultaneous transition on Phase A and Phase B will cause
         a QDEC error detection (STATUS.QERR).
         Figure 53-4. QDEC Block Diagram

                    Phase A                                                                               CC1                                  MC1 (Interrupt or Event)
                                sync




         Signal 0
                     Count
                                                                                                          CC0                                  MC0 (Interrupt or Event)

                                                             Position Clock                                     ovf
                                                                                   Count
                                                                                             Angular                  Revolution
                                                Quadrature




                                                             Position Direction                                                                OVF (Interrupt or Event)
                                                 Decoder




                                                                                   DIR Reset Counter (n-bits)         Counter (16/32-n-bits)
                                       Filter




                    Phase B
                                sync




         Signal 1                                            First Index Sync
                    Direction
                                                                Revolution Check

                                                             Velocity Clock
                                                                                                                                               VLC (Interrupt or Event)
                                                             Direction Change Detection
                    Index                                                                                                                      DIR (Interrupt or Event)
                                sync




         Signal 2                                            Error Detection
                                                                                                                                               ERR (Interrupt)

         Related Links
         53.3 Block Diagram

53.6.2.6.1 Position and Rotation Measurement
         After filtering, the quadrature signals are analyzed to extract the rotation direction and edges in order to
         be counted by the counter.
         The counter is split in two parts, Angular and Revolution. The Phase A and B edge detections define the
         motor axis position, which is recorded by the Angular part of the counter. The motor revolution is recorded
         by the Revolution part of the counter. The Angular counter is updated each time a QDEC transition is
         detected. The Revolution counter is updated on each angular counter overflow or underflow.




        © 2019 Microchip Technology Inc.                                           Datasheet                                              DS60001507E-page 1951
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     PDEC – Position Decoder

         Figure 53-5. Position and Rotation Measurement


             PhaseA

             PhaseB

             Index

             DIR Event

             Angle OVF

             ERR
             CC0 (LSB)
             CC1 (LSB)



             Anglular
             Counter


             CC1 (MSB)
             Revolution
             Counter

             MC1 Event

         in Q4 and Q4S configuration, a valid index is detected when the three inputs (PhaseA, PhaseB and
         Index) are at low level.
         In Q2 and Q2S configuration, a valid index is detected when the two inputs (Count and Index) are at low
         level.
         in Q2 and Q4 configuration, depending on current detected direction, Index will reset or reload the
         Angular counter and increment or decrement the Revolution counter.
         In Q2S and Q4S configuration, the Angular counter is reset on the first Index occurrence after the PDEC
         decoding is enabled. When any next Index occurrence does not match an Angular counter overflow or
         underflow, the Index Error flag in Status register is set (STATUS.IDXERR). The Error Interrupt Flag is set
         (INTFLAG.ERR) and an optional interrupt can be generated.
         An Index Error is also generated after the PDEC decoding is enabled and no Index has been detected
         after one Angular counter revolution.
53.6.2.6.2 Direction Status and Change Detection
         The direction (DIR) status can be directly read anytime in the STATUS register (STATUS.DIR). The
         polarity of the direction flag status depends of the input signal swap and active level configuration.
         Each time a rotation direction change is detected, the Direction Change Interrupt Flag is set
         (INTFLAG.DIR) and an optional interrupt can be generated. The same interrupt condition is source of
         Direction event output.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1952
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                     PDEC – Position Decoder

         Figure 53-6. Rotation Direction Change


                PhaseA

                PhaseB



                Anglular
                Counter




                DIR Event

                DIRCHG Interrupt

                VLC Event

         To avoid spurious interrupts when coding wheel is stopped, the direction change condition is reported as
         an interrupt, only on the second edge confirming the direction change.
         Velocity output event is generated on each QDEC transition except when the direction changes.
53.6.2.6.3 Speed Measurement
         Three types of speed measurement can be done using velocity event output (VLC) and Timer/Counter
         (TC/TCC) device resources.
          • Continuous velocity measurement: TCz measures the time on which n VLC (TCy) output events
            occur
          • Synchronous Velocity measurement: On a specific motor position TCCz, the time is measured on
            which n VLC (TCCy) output events occur.
          • Slow Velocity measurement: measure the number of VLC output events (TCCy) plus the delay since
            the last VLC output event (TCCz) within a given time slot (TCk).
         Figure 53-7. Speed Measurement
             Continuous Velocity Measurement      Synchronous Velocity Measurement         Slow Velocity Measurement
                        (Figure A)                          (Figure B)                            (Figure C)
            PhaseA     WO[0]          MC1      PhaseA      WO[0]           MC1        PhaseA     WO[0]           MC1
                               QDEC   MC0                          QDEC    MC0                           QDEC    MC0
            PhaseB     WO[1]                   PhaseB      WO[1]                      PhaseB     WO[1]
            Index      EV             OVF      Index       EV              OVF        Index      EV              OVF
                                      VLC                                  VLC                                   VLC




                                      MC1       Count      EV0
                                                                           MC1        Count      EV0
                                                                                                                 MC1
                       EV      TCy    MC0                  EV1
                                                                    TCCy   MC0
                                                                                                 MC0
                                                                                                          TCCy   MC0
             Count                    OVF      Retrigger                   OVF       Capture &                   OVF
                                                                                     Retriger

                                      MC1       Capture                    MC1        Capture                    MC1
                       EV      TCz                         MC0      TCCz   MC0                   MC0      TCCz   MC0
                                      MC0
           Capture &                  OVF      Retrigger
                                                           EV1             OVF       Retrigger
                                                                                                 EV1             OVF
           Retrigger


                                                                                                                 MC1
                                                                                                 EV       TCk    MC0
                                                                                                                 OVF




        © 2019 Microchip Technology Inc.                           Datasheet                          DS60001507E-page 1953
                                                                               SAM D5x/E5x Family Data Sheet
                                                                                                                PDEC – Position Decoder

53.6.2.6.4 Missing Pulse Detection and Auto-Correction
          The PDEC embeds circuitry to detect and correct errors that may result from contamination on optical
          disks or other sources producing quadrature phase signals.
          The auto-correction works in QDEC X4 mode only. A missing pulse on a phase signal is automatically
          detected, and the pulse count reported in the Angular part of COUNT is automatically corrected.
          There is no autocorrection if both phase signals are affected at the same location on the input signals,
          because the autocorrection requires a valid phase signal to detect contamination on the other phase
          signal.
          If the quadrature source is undamaged, the number of pulses counted for a predefined period of time
          must be the same with or without detection and auto-correction. Therefore, if the measurement results
          differ, a contamination exists on the source producing the quadrature signals. This does not substitute the
          measurements of the number of pulses between two index pulses (if available) but provides an additional
          method to detect damaged quadrature sources.
          When the source providing quadrature signals is strongly damaged, potentially leading to a number of
          consecutive missing pulses greater than 1, the quadrature decoder processing may be affected.
          The Maximum Consecutive Missing Pulses bits in Control A register (CTRLA.MAXCMP) define the
          maximum acceptable number of consecutive missing pulses. If the limit is reached, the Missing Pulse
          Error flag in Status register (STATUS.MPERR) is set. The Error Interrupt flag is set (INTFLAG.ERR) and
          an optional interrupt can be generated.
          Note: When the MAXCMP value is zero, the MPERR error flag is never set.

53.6.3    Additional Features

53.6.3.1 HALL Operation Mode
          In HALL operation mode, control logic signal 0, 1 and 2 inputs represent the phase A, B and C of a Hall
          sensor, respectively.
          A programmable delayed event can be generated to update a TCC pattern generator.
          Figure 53-8. HALL Block Diagram

                                                                                        CC1(MSB)             CC1[2:0]
                       Phase A                                                                               (Unused)        MC1 (Interrupt/Event)
                                 sync




                                                                                        Window Max
            Signal 0

                                                                                        CC0(MSB)              CC0[2:0]
                                                                                        Window Min       Hall Code Trigger   MC0 (Interrupt/Event)


                                                                                        COUNT(MSB)          COUNT(LSB)
                                                 Decoder




                                                                                Reset                                        OVF (Interrupt/Event)
                                        Filter




                       Phase B
                                                   Hall




                                                                                                            Delay Counter
                                 sync




                                                                                        Window Counter
            Signal 1



                                                           Velocity Clock
                                                                                                                             VLC (Interrupt/Event)
                                                           Direction Change Detection
                       Phase C                                                                                               DIR (Interrupt/Event)
                                 sync




            Signal 2                                       Error Detection
                                                                                                                             ERR (Interrupt/Event)



          Related Links
          53.3 Block Diagram

53.6.3.1.1 Hall Sensor Control
          On any update of the filter output:




         © 2019 Microchip Technology Inc.                                         Datasheet                                  DS60001507E-page 1954
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       PDEC – Position Decoder

         • The filter output value is checked to be a valid Hall value. If an invalid Hall code is reported, the Hall
           Error bit in Status register will be set (STATUS.HERR).
         • The MC0 Interrupt Flag bit is set (INTFLAG.MC0) if CC0[2:0] matches the filter output value. An
           optional compare match interrupt or Event output is generated on the same condition detection.
         • The window counter is checked to be between CC0[MSB] and CC1[MSB] value, and reset to 0 value.
           If an error is detected, the Window Error bit in Status register (STATUS.WINERR) is set.
         • The delay counter is started, and MC0 optional interrupt or event is generated when the delay
           counter matches CC0[LSB].
        Any error condition will set the Error Interrupt Flag (INTFLAG.ERR). An optional interrupt or event output
        is generated on the same condition detection.
        Figure 53-9. Hall Waveforms


                     State                101   001   101      100               110      010   011   000




                     CC1(MSB)

                     CC0(MSB)
                     Counter(MSB)


                     ERR

                     VLC Event

                     MC0 Event

                     OVF Event

                     DIR Event

                     DIR Interrupt


53.6.3.2 Counter Operation Mode
        Depending on the mode of operation, the counter (Counter Value register COUNT) is cleared, reloaded,
        or incremented at each counter clock input.
        The counter will count for each clock tick until it reaches TOP. When TOP is reached, the counter will be
        set to zero on the next clock input.
        This comparison will set the Overflow Interrupt Flag in the Interrupt Flag Status and Clear register
        (INTFLAG.OVF) and can be used to trigger an interrupt or an event.
        It is possible to change the counter value when the counter is running. The write access has higher
        priority than count, or clear. The COUNT value will always be zero when starting the PDEC, unless a
        different value has been written to it, or the PDEC has been disabled at a value other than zero. Due to
        asynchronous clock domains, the internal counter settings are written once the synchronization is
        complete.
        Related Links
        14. GCLK - Generic Clock Controller




       © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 1955
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       PDEC – Position Decoder

53.6.3.3 Register Lock Update
         Prescaler (PRESC), FILTER, and CCx registers are buffered (PRESCBUF, FILTERBUF, CCBUFx
         registers, respectively). When a new value is written in a buffer register, the corresponding Buffer Valid bit
         is set in the Buffer Status register (STATUS.FILTERBUFV, STATUS.PRESCBUFV, STATUS.CCBUFVx).
         By default, a register is updated with the its buffer register's value on UPDATE condition, which
         represents:
           • The next filter transition in QDEC and HALL mode of operation
           • The overflow/underflow or re-trigger event detection in COUNT mode of operation
         The buffer valid flags in the STATUS register are automatically cleared by hardware when the data is
         copied from the buffer to the corresponding register.
         It is possible to lock the updates by writing a '1' to the Lock Update bit in Control B Set register
         (CTRLBSET.LUPD).
         The lock feature is disabled by writing a '1' to the Lock Update bit in Control B Clear register
         (CTRLBCLR.LUPD). When a buffer valid status flag is '1' and updating is not locked, the data from the
         buffer register will be copied into the corresponding register on UPDATE condition.
         It is also possible to modify the LUPD bit behavior by hardware, by writing a '1' to the Auto-lock bit in
         Control A register (CTRLA.ALOCK). When the bit is '1', the Lock Update bit in Control B register
         (CTRLBSET.LUPD) is set when the UPDATE condition is detected.
53.6.3.4 Software Command and Event Actions
         The PDEC peripheral supports software commands and event actions. The software commands are
         applied by the Software Command bit field in the Control B register (CTRLBSET.CMD,
         CTRLBCLR.CMD). The event actions are available in the Event Action bit-field in Event Control register
         (EVCTRL.EVACT).
53.6.3.4.1 Re-trigger Software Command or Event Action
         A re-trigger command can be issued from software by using PDEC Command bits in Control B Set
         register (CTRLBSET.CMD = RETRIGGER) or when the re-trigger event action is configured in the Input
         Event Action bits in Event Control register (EVCTRL.EVACT = RETRIGGER) and an event is detected by
         hardware.
         When the re-trigger command is detected during counting operation, the counter will be reloaded or
         cleared, depending on the counting direction (DIR). If the re-trigger command is detected when the
         counter is stopped, the counter will resume counting operation from the value in the COUNT register.
         Note: When re-trigger event action is enabled, enabling the counter will not start the counter. The
         counter will start on the next incoming event and restart on any following event.
53.6.3.4.2 Count Event Action
         The count action can be selected in the Event Control register (EVCTRL.EVACT) and can be used to
         count external events. When an event is received, the counter increments the value.
53.6.3.4.3 Force Update Software Command
         A Force Update command can be issued by writing the PDEC Command bits in Control B Set register
         (CTRLBSET.CMD = UPDATE). When the command is issued, the buffered registers will be updated.
53.6.3.4.4 Force Read Synchronization Software Command
         A Force Read Synchronization command can be issued writing the PDEC Command bits in Control B Set
         register (CTRLBSET.CMD = READSYNC). When the command is issued, a COUNT register read
         synchronization is forced.
         Note: This command should be used to read the most updated COUNT internal value.




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1956
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      PDEC – Position Decoder

53.6.4   Interrupts
         The PDEC has the following interrupt sources:
           •   Overflow/Underflow: OVF
           •   Compare Channels: COMPx
           •   Error: ERR
           •   Velocity: VLC. This interrupt is available only in QDEC and HALL operation modes.
           •   Direction: DIR. This interrupt is available only in QDEC and HALL operation modes.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear register (INTFLAG) is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable Set register
         (INTENSET), and disabled by writing a '1' to the corresponding bit in the Interrupt Enable Clear register
         (INTENCLR).
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled or the
         PDEC is reset. See the INTFLAG register description for details on how to clear interrupt flags.
         The user must read the INTFLAG register to determine which interrupt condition is present.
         Note: Interrupts must be globally enabled for interrupt requests to be generated.

53.6.5   Events
         The PDEC can generate the following output events:
           •   Overflow/Underflow: OVF
           •   Channel x Compare Match: MCx
           •   Error: ERR
           •   Velocity: VLC. This interrupt is available only in QDEC and HALL operation modes.
           •   Direction: DIR. This interrupt is available only in QDEC and HALL operation modes.
         Writing a '1' to an Event Output bit in the Event Control register (EVCTRL.MCEO) enables the
         corresponding output event. Writing a '0' to this bit disables the corresponding output event.

         Related Links
         31. EVSYS – Event System

53.6.6   Sleep Mode Operation
         The PDEC can be configured to operate in any sleep mode. To be able to run in standby, the RUNSTDBY
         bit in the Control A register (CTRLA.RUNSTDBY) must be written to '1'. The PDEC can wake up the
         device using interrupts from any sleep mode or perform actions through the Event System.

53.6.7   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset bit in the Control A register (CTRLA.SWRST)
           • Enable bit in the Control A register (CTRLA.ENABLE)
         The following registers need synchronization when written:




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1957
                                                 SAM D5x/E5x Family Data Sheet
                                                                         PDEC – Position Decoder

  •   Control B Clear and Control B Set registers (CTRLBCLR and CTRLBSET)
  •   Status register (STATUS)
  •   Prescaler and Prescaler Buffer registers (PRESC and PRESCBUF)
  •   Compare Value x and Compare Value x Buffer registers (CCx and CCBUFx)
  •   Filter Value and Filter Buffer Value registers (FILTER and FILTERBUF)
  •   Counter Value register (COUNT)
Required write synchronization is denoted by the "Write-Synchronized" property in the register
description.
The following registers are synchronized when read:
  • Counter Value register (COUNT): the synchronization is done on demand through READSYNC
    software command (CTRLBSET.CMD)
Required read synchronization is denoted by the "Read-Synchronized" property in the register
description.
Related Links
13.3 Register Synchronization




© 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1958
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                PDEC – Position Decoder


53.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0              RUNSTDBY                                    MODE[1:0]           ENABLE         SWRST
                             15:8      PEREN    SWAP                                 ALOCK                     CONF[2:0]
 0x00         CTRLA
                             23:16             PINVEN2     PINVEN1     PINVEN0                    PINEN2        PINEN1        PINEN0
                             31:24                 MAXCMP[3:0]                                               ANGULAR[2:0]
 0x04        CTRLBCLR         7:0              CMD[2:0]                                                         LUPD
 0x05        CTRLBSET         7:0              CMD[2:0]                                                         LUPD
                              7:0              EVEI[2:0]                           EVINV[2:0]                          EVACT[1:0]
 0x06         EVCTRL
                             15:8                          MCEO1       MCEO0         VLCEO        DIREO         ERREO         OVFEO
 0x08        INTENCLR         7:0                           MC1         MC0              VLC       DIR           ERR            OVF
 0x09        INTENSET         7:0                           MC1         MC0              VLC       DIR           ERR            OVF
 0x0A        INTFLAG          7:0                           MC1         MC0              VLC       DIR           ERR            OVF
 0x0B        Reserved
                              7:0       DIR      STOP       HERR       WINERR                     MPERR         IDXERR         QERR
 0x0C         STATUS
                             15:8                          CCBUFV1     CCBUFV0                                FILTERBUFV PRESCBUFV
 0x0E        Reserved
 0x0F        DBGCTRL          7:0                                                                                             DBGRUN
                              7:0       CC0     COUNT      FILTER      PRESC        STATUS        CTRLB        ENABLE         SWRST
                             15:8                                                                                               CC1
 0x10       SYNCBUSY
                             23:16
                             31:24
 0x14         PRESC           7:0                                                                       PRESC[3:0]
 0x15         FILTER          7:0                                          FILTER[7:0]
 0x16
   ...       Reserved
 0x17
 0x18       PRESCBUF          7:0                                                                      PRESCBUF[3:0]
 0x19       FILTERBUF         7:0                                        FILTERBUF[7:0]
 0x1A
   ...       Reserved
 0x1B
                              7:0                                          COUNT[7:0]
                             15:8                                         COUNT[15:8]
 0x1C         COUNT
                             23:16
                             31:24
                              7:0                                             CC[7:0]
                             15:8                                             CC[15:8]
 0x20           CC0
                             23:16
                             31:24
                              7:0                                             CC[7:0]
                             15:8                                             CC[15:8]
 0x24           CC1
                             23:16
                             31:24




          © 2019 Microchip Technology Inc.                          Datasheet                                DS60001507E-page 1959
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                          PDEC – Position Decoder

...........continued

  Offset               Name     Bit Pos.

   0x28
     ...           Reserved
   0x2F
                                  7:0                                       CCBUF[7:0]
                                 15:8                                      CCBUF[15:8]
   0x30                CCBUF0
                                 23:16
                                 31:24
                                  7:0                                       CCBUF[7:0]
                                 15:8                                      CCBUF[15:8]
   0x34                CCBUF1
                                 23:16
                                 31:24




53.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to 53.5.8 Register Access Protection.
               Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
               Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
               refer to 53.6.7 Synchronization.




              © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1960
                                                                SAM D5x/E5x Family Data Sheet
                                                                                             PDEC – Position Decoder

53.8.1         Control A

               Name:       CTRLA
               Offset:     0x00
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit         31          30             29         28           27               26           25          24
                                      MAXCMP[3:0]                                                ANGULAR[2:0]
   Access            RW          RW             RW        RW                             RW          RW          RW
    Reset            0            0                 0      0                             0            0           0


         Bit         23          22             21         20           19               18           17          16
                              PINVEN2         PINVEN1   PINVEN0                     PINEN2         PINEN1       PINEN0
   Access                        RW             RW        RW                             RW          RW          RW
    Reset                         0                 0      0                             0            0           0


         Bit         15          14             13         12           11               10           9           8
                  PEREN        SWAP                                   ALOCK                       CONF[2:0]
   Access            RW          RW                                    RW                RW          RW          RW
    Reset            0            0                                     0                0            0           0


         Bit         7            6                 5      4            3                2            1           0
                             RUNSTDBY                                        MODE[1:0]             ENABLE       SWRST
   Access                        RW                                    RW                RW          RW           W
    Reset                         0                                     0                0            0           0


               Bits 31:28 – MAXCMP[3:0] Maximum Consecutive Missing Pulses
               These bits define the threshold for the maximum consecutive missing pulses in AUTOC configuration of
               the QDEC mode.
               Outside of AUTOC configuration of QDEC mode, these bits have no effect.
               These bits are not synchronized.

               Bits 26:24 – ANGULAR[2:0] Angular Counter Length
               In QDEC mode, these bits define the size of the Angular counter within COUNT. Angular counter size is
               equal to CTRLA.ANGULAR+9. The remaining MSB of the COUNTER register are used for counting
               revolutions.
               For example, CTRLA.ANGULAR=0 defines the 9 LSB of COUNT as Angular counter and the residual 7
               MSB of COUNT as Revolution counter. CTRLA.ANGULAR=7 will define a 16-bit Angular counter and no
               Revolution counter.
               Outside of QDEC mode, these bits have no effect.
               These bits are not synchronized.
               Table 53-1. Angular and Revolution Counters in COUNTER Register

               ANGULAR[2:0]                     Angular counter                  Revolution counter
               0x0                              COUNTER[0:8]                     COUNTER[9:15]
               0x1                              COUNTER[0:9]                     COUNTER[10:15]




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1961
                                                     SAM D5x/E5x Family Data Sheet
                                                                               PDEC – Position Decoder

...........continued
 ANGULAR[2:0]                      Angular counter                     Revolution counter
 0x2                               COUNTER[0:10]                       COUNTER[11:15]
 0x3                               COUNTER[0:11]                       COUNTER[12:15]
 0x4                               COUNTER[0:12]                       COUNTER[13:15]
 0x5                               COUNTER[0:13]                       COUNTER[14:15]
 0x6                               COUNTER[0:14]                       COUNTER[15]
 0x7                               COUNTER[0:15]                       no revolution counter

Bits 20, 21, 22 – PINVEN IO Pin x Invert Enable
When this bit is written to '1', the corresponding input pin active level is inverted. This bit has no effect if
PINENx bit is zero.
In COUNTER mode only PINVEN[0] is significant.
This bit is not synchronized.
 Value       Description
 0           Pin active level is not inverted.
 1           Pin active level is inverted.

Bits 16, 17, 18 – PINEN PDEC Input From Pin x Enable
This bit enables the IO pin x as signal input.
In COUNTER mode, only PINVEN[0] is significant.
This bit is not synchronized.
 Value       Description
 0           Event line is the signal input.
 1           I/O pin is the signal input.

Bit 15 – PEREN Period Enable
This bit is used to enable the CC0 register as counter period.
This bit is not synchronized.
 Value       Description
 0            Period register function is disabled.
 1            CC0 is acting as counter period register.

Bit 14 – SWAP PDEC Phase A and B Swap
This bit is used to swap input source of signal 0 and 1.
In COUNTER mode this bit has no effect.
This bit is not synchronized.
 Value       Description
 0            The input sources of signal 0 and 1 are not swapped.
 1            The input sources of signal 0 and 1 are swapped.

Bit 11 – ALOCK Auto Lock
When this bit is set, the Lock Update bit in Control B register (CTRLB.LUPD) is set by hardware when an
UPDATE condition is detected.
This bit is not synchronized.




© 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1962
                                                   SAM D5x/E5x Family Data Sheet
                                                                            PDEC – Position Decoder

 Value        Description
 0            Auto Lock is disabled.
 1            Auto Lock is enabled.

Bits 10:8 – CONF[2:0] PDEC Configuration
These bits define the PDEC configuration.
Outside of QDEC mode, these bits have no effect.
These bits are not synchronized.
 Value      Name              Description
 0          X4                Quadrature decoder direction
 1          X4S               Secure Quadrature decoder direction
 2          X2                Decoder direction
 3          X2S               Secure decoder direction
 4          AUTOC             Auto correction mode

Bit 6 – RUNSTDBY Run in Standby
This bit is used to keep the PDEC running in standby mode.
This bit is not synchronized.
 Value       Description
 0            The PDEC is halted in standby.
 1            The PDEC continues to run in standby.

Bits 3:2 – MODE[1:0] Operation Mode
These bits select one of the QDEC, HALL, COUNTER modes.
These bits are not synchronized.
 Value      Name                      Description
 0x0        QDEC                      QDEC operating mode
 0x1        HALL                      HALL operating mode
 0x2        COUNTER                   COUNTER operating mode

Bit 1 – ENABLE Enable
Due to synchronization, there is delay between writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately, and the Enable
Synchronization Busy bit in the Synchronization Busy register (SYNCBUSY.ENABLE) will be set.
SYNCBUSY.ENABLE will be cleared when the operation is complete.
 Value      Description
 0          The peripheral is disabled.
 1          The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the PDEC (except DBGCTRL) to their initial state, and the
PDEC will be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence; all other writes in the same write-operation
will be discarded.
Due to synchronization, there is a delay from writing CTRLA.SWRST until the Reset is complete.
CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the Reset is complete.
Value         Description
0             There is no Reset operation ongoing.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1963
                                              SAM D5x/E5x Family Data Sheet
                                                          PDEC – Position Decoder

 Value        Description
 1            A Reset operation is ongoing.




© 2019 Microchip Technology Inc.              Datasheet          DS60001507E-page 1964
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                           PDEC – Position Decoder

53.8.2         Control B Clear

               Name:       CTRLBCLR
               Offset:     0x04
               Reset:      0x00
               Property:   PAC Write-Protection, Read-Synchronized, Write-Synchronized

               This register allows the user to change this register without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Control B Set (CTRLBSET) register.

         Bit         7            6            5             4            3            2             1            0
                               CMD[2:0]                                                            LUPD
   Access           RW           RW           RW                                                    RW
    Reset            0            0            0                                                     0


               Bits 7:5 – CMD[2:0] Command
               These bits can be used for software control of the PDEC. When a command has been executed, the
               CMD bit group will read back zero. The commands are executed on the next prescaled GCLK_PDEC
               clock cycle.
               Writing a zero to this bit group has no effect.
               Writing a valid value to these bits will clear the corresponding pending command.
               Writing a '0' to these bits has no effect.
               Writing a '1' to an individual bit will clear the corresponding bit.
                Value        Name                        Description
                0            NONE                        No action
                1            RETRIGGER                   Force a counter restart or re-trigger
                2            UPDATE                      Force update of double buffered registers
                3            READSYNC                    Force a read synchronization of COUNT
                4            START                       Start QDEC/HALL
                5            STOP                        Stop QDEC/HALL

               Bit 1 – LUPD Lock Update
               This bit controls the update operation of the PDEC buffered registers.
               When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
               on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
               hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
               can be unlocked.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this will disable the lock update.
                Value        Description
                0            The PRESCBUF, FILTERBUF and CCBUFx buffer registers value are copied into CCx and
                             PER registers on hardware update condition.
                1            The PRESCBUF, FILTERBUF and CCBUFx buffer registers value are not copied into CCx
                             and PER registers on hardware update condition.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1965
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                           PDEC – Position Decoder

53.8.3         Control B Set

               Name:       CTRLBSET
               Offset:     0x05
               Reset:      0x00
               Property:   PAC Write-Protection, Read-Synchronized, Write-Synchronized

               This register allows the user to change this register without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Control B Clear (CTRLBCLR) register.

         Bit         7            6            5             4            3            2             1            0
                               CMD[2:0]                                                            LUPD
   Access           RW           RW           RW                                                    RW
    Reset            0            0            0                                                     0


               Bits 7:5 – CMD[2:0] Command
               These bits can be used for software control of the PDEC. When a command has been executed, the
               CMD bit group will read back zero. The commands are executed on the next prescaled GCLK_PDEC
               clock cycle.
               Writing a zero to this bit group has no effect.
               Writing a valid value to these bits will set the associated command.
                Value       Name                      Description
                0           NONE                      No action
                1           RETRIGGER                 Force a counter restart or retrigger
                2           UPDATE                    Force update of double buffered registers
                3           READSYNC                  Force a read synchronization of COUNT
                4           START                     Start QDEC/HALL
                5           STOP                      Stop QDEC/HALL

               Bit 1 – LUPD Lock Update
               This bit controls the update operation of the PDEC buffered registers.
               When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
               on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
               hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
               can be unlocked.
               Writing a '1' to this will enable the Lock Update.
                Value        Description
                0            The PRESCBUF, FILTERBUF and CCBUFx buffer registers value are copied into CCx and
                             PER registers on hardware update condition.
                1            The PRESCBUF, FILTERBUF and CCBUFx buffer registers value are not copied into CCx
                             and PER registers on hardware update condition.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1966
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            PDEC – Position Decoder

53.8.4         Event Control

               Name:       EVCTRL
               Offset:     0x06
               Reset:      0x0000
               Property:   Enable-Protected, PAC Write-Protection


         Bit        15            14           13           12            11           10            9                8
                                              MCEO1       MCEO0         VLCEO        DIREO        ERREO          OVFEO
   Access                                      RW           RW            RW           RW           RW                RW
    Reset                                       0            0             0            0            0                0


         Bit         7            6             5            4             3            2            1                0
                               EVEI[2:0]                               EVINV[2:0]                        EVACT[1:0]
   Access           RW           RW            RW           RW            RW           RW           RW                RW
    Reset            0            0             0            0             0            0            0                0


               Bits 12, 13 – MCEO Match Channel x Event Output Enable
               These bits control whether event match on channel x is enabled or not and generated for every match.
                Value      Description
                0          Match event on channel x is disabled and will not be generated.
                1          Match event on channel x is enabled and will be generated for every compare.

               Bit 11 – VLCEO Velocity Output Event Enable
               This bit is used to enable the velocity event. When enabled, an event level will be generated for each
               change on the qualified PDEC phases.
               This bit has no effect when COUNTER operation mode is selected.
                Value       Description
                0            VLC output event is disabled and will not be generated.
                1            VLC output is enabled and will be generated for every valid velocity condition.

               Bit 10 – DIREO Direction Output Event Enable
               This bit is used to enable the Direction event. When enabled, an event level output is generated to report
               the rotation direction.
                Value       Description
                0            DIR output event is disabled and will not be generated.
                1            DIR output is enabled and changes the level when the rotation direction changes.

               Bit 9 – ERREO Error Output Event Enable
               This bit enables the output of the Error event (ERR).
                Value      Description
                0          ERR Event output is disabled.
                1          ERR Event output is enabled.

               Bit 8 – OVFEO Overflow/Underflow Output Event Enable
               This bit is used to enable the Overflow/Underflow event. When enabled, an event will be generated when
               the Counter overflows/underflows.
                Value       Description
                0            Overflow/Underflow event is disabled and will not be generated.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1967
                                                  SAM D5x/E5x Family Data Sheet
                                                                          PDEC – Position Decoder

 Value        Description
 1            Overflow/Underflow event is enabled and will be generated for every counter overflow/
              underflow.

Bits 7:5 – EVEI[2:0] Event Input Enable
This bit is used to enable asynchronous input event to the counter.
 Value       Description
 0            Incoming events are disabled.
 1            Incoming events are enabled.

Bits 4:2 – EVINV[2:0] Inverted Event Input Enable
This bit inverts the asynchronous input event to the counter.
 Value       Description
 0           Input event source is not inverted.
 1           Input event source is inverted.

Bits 1:0 – EVACT[1:0] Event Action
These bits have an effect only when COUNTER operation mode is selected, and ignored in all other
operation modes.
These bits define the event action the counter will perform on an event.
 Value      Name                         Description
 0          OFF                          Event action disabled
 1          RETRIGGER                    Start, restart or retrigger on event
 2          COUNT                        Count on event




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1968
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 PDEC – Position Decoder

53.8.5         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x08
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to change this register without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

         Bit         7              6             5             4              3             2             1              0
                                                MC1            MC0           VLC            DIR           ERR           OVF
   Access                                        RW            RW             RW            RW            RW             RW
    Reset                                         0             0              0             0             0              0


               Bits 4, 5 – MC Channel x Compare Match Disable
               Writing a '0' to MCx has no effect.
               Writing a '1' to MCx will clear the corresponding Match Channel x Interrupt Disable/Enable bit, which
               disables the Match Channel x interrupt.
                Value        Description
                0            The Match Channel x interrupt is disabled.
                1            The Match Channel x interrupt is enabled.

               Bit 3 – VLC Velocity Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Velocity Interrupt Disable/Enable bit, which disables the Velocity
               interrupt.
               This bit has no effect when COUNTER operation mode is selected.
                Value        Description
                0            The Velocity interrupt is disabled.
                1            The Velocity interrupt is enabled.

               Bit 2 – DIR Direction Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Direction Change Interrupt Disable/Enable bit, which disables the
               Direction Change interrupt.
               This bit has no effect when COUNTER operation mode is selected.
                Value        Description
                0            The Direction Change interrupt is disabled.
                1            The Direction Change interrupt is enabled.

               Bit 1 – ERR Error Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Error Interrupt Disable/Enable bit, which disables the Error interrupt.
               Value         Description
               0             The Error interrupt is disabled.
               1             The Error interrupt is enabled.

               Bit 0 – OVF Overflow/Underflow Interrupt Disable
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1969
                                                    SAM D5x/E5x Family Data Sheet
                                                                             PDEC – Position Decoder

Writing a '1' to this bit will clear the Overflow Interrupt Disable/Enable bit, which disables the Overflow
interrupt.
 Value        Description
 0            The Overflow interrupt is disabled.
 1            The Overflow interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1970
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 PDEC – Position Decoder

53.8.6         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x09
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to change this register without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         7             6              5             4             3              2             1               0
                                                MC1            MC0           VLC            DIR          ERR              OVF
   Access                                        RW            RW            RW             RW            RW              RW
    Reset                                         0             0             0              0             0               0


               Bits 4, 5 – MC Channel x Compare Match Enable
               Writing a '0' to MCx has no effect.
               Writing a '1' to MCx will set the corresponding Match Channel x Interrupt Disable/Enable bit, which
               enables the Match Channel x interrupt.
                Value        Description
                0            The Match Channel x interrupt is disabled.
                1            The Match Channel x interrupt is enabled.

               Bit 3 – VLC Velocity Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Velocity Interrupt Disable/Enable bit, which enables the Velocity
               interrupt.
               This bit has no effect when COUNTER operation mode is selected.
                Value        Description
                0            The Velocity interrupt is disabled.
                1            The Velocity interrupt is enabled.

               Bit 2 – DIR Direction Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Direction Change Interrupt Disable/Enable bit, which enables the
               Direction Change interrupt.
               This bit has no effect when COUNTER operation mode is selected.
                Value        Description
                0            The Direction Change interrupt is disabled.
                1            The Direction Change interrupt is enabled.

               Bit 1 – ERR Error Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Error Interrupt Disable/Enable bit, which enables the Error interrupt.
               Value         Description
               0             The Error interrupt is disabled.
               1             The Error interrupt is enabled.

               Bit 0 – OVF Overflow/Underflow Interrupt Enable
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 1971
                                                    SAM D5x/E5x Family Data Sheet
                                                                             PDEC – Position Decoder

Writing a '1' to this bit will set the Overflow Interrupt Disable/Enable bit, which enable the Overflow
interrupt.
 Value        Description
 0            The Overflow interrupt is disabled.
 1            The Overflow interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1972
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 PDEC – Position Decoder

53.8.7         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x0A
               Reset:       0x00
               Property:    -


         Bit         7             6              5             4              3             2             1              0
                                                MC1            MC0           VLC            DIR           ERR           OVF
   Access                                        RW            RW            RW             RW            RW             RW
    Reset                                         0             0              0             0             0              0


               Bits 4, 5 – MC Channel x Compare Match
               This flag is set on the next CLK_PDEC_CNT cycle after a match with the compare condition, and will
               generate an interrupt request if the corresponding Match Channel x Interrupt Enable bit in the Interrupt
               Enable Set register (INTENSET.MCx) is '1'.
               Writing a '0' to one of these bits has no effect.
               Writing a '1' to one of these bits will clear the corresponding Match Channel x interrupt flag.

               Bit 3 – VLC Velocity
               This flag is set if a velocity transition occurs, and will generate an interrupt request if the Velocity Interrupt
               Enable bit in Interrupt Enable Set register (INTENSET.VLC) is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Velocity transition interrupt flag.
               This flag is never set when COUNTER operation mode is selected.

               Bit 2 – DIR Direction Change
               This flag is set if a direction change occurs, and will generate an interrupt request if the Direction Change
               Interrupt Enable bit in Interrupt Enable Set register (INTENSET.DIR) is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Velocity transition interrupt flag.
               This flag is never set when COUNTER operation mode is selected.

               Bit 1 – ERR Error
               This flag is set when an error condition is detected, and will generate an interrupt request if the Error
               Interrupt Enable bit in the Interrupt Enable Set register (INTENSET.ERR) is '1'. The error source can be
               identified by reading the Status (STATUS) register.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Error interrupt flag.

               Bit 0 – OVF Overflow/Underflow
               This flag is set on the next CLK_TC_CNT cycle after an overflow condition occurs, and will generate an
               interrupt request if the Overflow Interrupt Enable bit in the Interrupt Enable Set register (INTENSET.OVF)
               is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Overflow interrupt flag.




           © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1973
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                           PDEC – Position Decoder

53.8.8         Status

               Name:       STATUS
               Offset:     0x0C
               Reset:      0x0040
               Property:   Read-Synchronized, Write-Synchronized


         Bit        15           14             13          12            11           10            9            8
                                              CCBUFV1    CCBUFV0                                FILTERBUFV   PRESCBUFV
   Access                                       R           R                                       R             R
    Reset                                        0           0                                       0            0


         Bit         7            6              5           4            3            2             1            0
                    DIR         STOP           HERR      WINERR                      MPERR        IDXERR        QERR
   Access            R            R             RW          RW                        RW            RW           RW
    Reset            0            1              0           0                         0             0            0


               Bits 12, 13 – CCBUFV Compare Channel x Buffer Valid
               The bit is set when a new value is written to the corresponding CCBUF register.
               The bit is cleared by writing a '1' to the corresponding location or automatically cleared on an UPDATE
               condition.

               Bit 9 – FILTERBUFV Filter Buffer Valid
               This bit is set when a new value is written to the PRESCALERBUF register.
               The bit is cleared by writing a '1' to the corresponding location or automatically cleared on an UPDATE
               condition.
               This bit is always read '0' when COUNTER operation mode is selected.

               Bit 8 – PRESCBUFV Prescaler Buffer Valid
               This bit is set when a new value is written to the PRESC register.
               The bit is cleared by writing a '1' to the corresponding location or automatically cleared on an UPDATE
               condition.

               Bit 7 – DIR Direction Status Flag
               This bit reflects the HALL/QDEC direction.
               in COUNTER mode, this bits is always read '0'.
                Value        Description
                0            Clockwise direction.
                1            Counter-clockwise direction.

               Bit 6 – STOP Stop
               This bit reflects the HALL/QDEC decoding status.
               In COUNTER mode, this bits is always read '0'.
                Value        Description
                0            PDEC/HALL decoding is running.
                1            PDEC/HALL decoding is stopped.

               Bit 5 – HERR Hall Error Flag
               This flag is set when an invalid HALL code is detected.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1974
                                                       SAM D5x/E5x Family Data Sheet
                                                                     PDEC – Position Decoder

The flag is cleared by writing a '1' to this bit location.
Outside of HALL mode, this bits is always read '0'.

Bit 4 – WINERR Window Error Flag
This flag is set when the counter is outside the window monitor.
The flag is cleared by writing a '1' to this bit location.
Outside of HALL mode, this bits is always read '0'.

Bit 2 – MPERR Missing Pulse Error flag
This flag is set when a missing pulse error condition is detected.
The flag is cleared by writing a '1' to this bit location.
Outside of QDEC mode, this bits is always read '0'.

Bit 1 – IDXERR Index Error Flag
This flag is set when an index error condition is detected.
The flag is cleared by writing a '1' to this bit location.
Outside of QDEC mode, this bits is always read '0'.

Bit 0 – QERR Quadrature Error Flag
This flag is set when an invalid QDEC transition is detected.
The flag is cleared by writing a '1' to this bit location.
Outside of QDEC mode, this bits is always read '0'.




© 2019 Microchip Technology Inc.                        Datasheet           DS60001507E-page 1975
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         PDEC – Position Decoder

53.8.9         Debug Control

               Name:       DBGCTRL
               Offset:     0x0F
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5            4            3            2            1            0
                                                                                                           DBGRUN
   Access                                                                                                     RW
    Reset                                                                                                      0


               Bit 0 – DBGRUN Debug Run Mode
               This bit is not affected by software reset and should not be changed by software while the PDEC module
               is enabled.
                Value       Description
                0           The PDEC module is halted when the device is halted in debug mode.
                1           The PDEC module continues normal operation when the device is halted in debug mode.




           © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1976
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         PDEC – Position Decoder

53.8.10 Synchronization Status

            Name:       SYNCBUSY
            Offset:     0x10
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31            30            29          28            27           26            25           24


  Access
   Reset


      Bit        23            22            21          20            19           18            17           16


  Access
   Reset


      Bit        15            14            13          12            11           10            9            8
                                                                                                              CC1
  Access                                                                                                       R
   Reset                                                                                                       0


      Bit         7            6             5            4            3             2            1            0
                CC0         COUNT          FILTER      PRESC        STATUS        CTRLB        ENABLE        SWRST
  Access          R            R             R            R            R            R             R            R
   Reset          0            0             0            0            0             0            0            0


            Bits 7, 8 – CC Compare Channel x Synchronization Busy
            This bit is cleared when the synchronization of Compare Channel x (CCx) register between the clock
            domains is complete.
            This bit is set when the synchronization of Compare Channel x (CCx) register between clock domains is
            started.

            Bit 6 – COUNT Count Synchronization Busy
            This bit is cleared when the synchronization of Count register between the clock domains is complete.
            This bit is set when the synchronization of Count register between clock domains is started.

            Bit 5 – FILTER Filter Synchronization Busy
            This bit is cleared when the synchronization of Filter register between the clock domains is complete.
            This bit is set when the synchronization of Filter register between clock domains is started.
            This bit is always read '0' when COUNTER operation mode is selected.

            Bit 4 – PRESC Prescaler Synchronization Busy
            This bit is cleared when the synchronization of Prescaler register between the clock domains is complete.
            This bit is set when the synchronization of Prescaler register between clock domains is started.

            Bit 3 – STATUS Status Synchronization Busy
            This bit is cleared when the synchronization of Status register between the clock domains is complete.
            This bit is set when the synchronization of Status register between clock domains is started.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1977
                                                  SAM D5x/E5x Family Data Sheet
                                                                          PDEC – Position Decoder

Bit 2 – CTRLB Control B Synchronization Busy
This bit is cleared when the synchronization of Control B register between the clock domains is complete.
This bit is set when the synchronization of Control B register between clock domains is started.

Bit 1 – ENABLE Enable Synchronization Busy
This bit is cleared when the synchronization of Enable register bit between the clock domains is
complete.
This bit is set when the synchronization of Enable register bit between clock domains is started.

Bit 0 – SWRST Software Reset Synchronization Busy
This bit is cleared when the synchronization of Software Reset register bit between the clock domains is
complete.
This bit is set when the synchronization of Software Reset register bit between clock domains is started.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1978
                                                                SAM D5x/E5x Family Data Sheet
                                                                                    PDEC – Position Decoder

53.8.11 Prescaler Value

            Name:       PRESC
            Offset:     0x14
            Reset:      0x00
            Property:   Write-Synchronized


      Bit         7            6             5             4            3       2                 1            0
                                                                                     PRESC[3:0]
  Access                                                                RW      RW                RW          RW
   Reset                                                                0       0                 0            0


            Bits 3:0 – PRESC[3:0] Prescaler Value
            These bits select the GCLK prescaler factor.
             Value      Name                                   Description
             0          DIV1                                   No division
             1          DIV2                                   Divide by 2
             2          DIV4                                   Divide by 4
             3          DIV8                                   Divide by 8
             4          DIV16                                  Divide by 16
             5          DIV32                                  Divide by 32
             6          DIV64                                  Divide by 64
             7          DIV128                                 Divide by 128
             8          DIV256                                 Divide by 256
             9          DIV512                                 Divide by 512
             10         DIV1024                                Divide by 1024




        © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 1979
                                                           SAM D5x/E5x Family Data Sheet
                                                                                     PDEC – Position Decoder

53.8.12 Filter Value

            Name:       FILTER
            Offset:     0x15
            Reset:      0x00
            Property:   Write-Synchronized


      Bit        7             6             5        4                 3        2           1           0
                                                          FILTER[7:0]
   Access       RW            RW           RW        RW                 RW   RW             RW          RW
    Reset        0             0             0        0                 0        0           0           0


            Bits 7:0 – FILTER[7:0] Filter Value
            These bits select the PDEC inputs filter length.
            These bits have no effect when COUNTER operation mode is selected.




        © 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1980
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         PDEC – Position Decoder

53.8.13 Prescaler Buffer Value

            Name:       PRESCBUF
            Offset:     0x18
            Reset:      0x00
            Property:   Write-Synchronized


      Bit         7            6             5            4             3            2             1               0
                                                                                      PRESCBUF[3:0]
  Access                                                               RW           RW            RW           RW
   Reset                                                                0            0             0               0


            Bits 3:0 – PRESCBUF[3:0] Prescaler Buffer Value
            These bits hold the value of the prescaler buffer register. The value is copied in the corresponding
            PRESC register on UPDATE condition.
             Value      Name                                  Description
             0          DIV1                                  No division
             1          DIV2                                  Divide by 2
             2          DIV4                                  Divide by 4
             3          DIV8                                  Divide by 8
             4          DIV16                                 Divide by 16
             5          DIV32                                 Divide by 32
             6          DIV64                                 Divide by 64
             7          DIV128                                Divide by 128
             8          DIV256                                Divide by 256
             9          DIV512                                Divide by 512
             10         DIV1024                               Divide by 1024




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1981
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          PDEC – Position Decoder

53.8.14 Filter Buffer Value

            Name:        FILTERBUF
            Offset:      0x19
            Reset:       0x00
            Property:    Write-Synchronized


      Bit         7            6              5            4            3             2             1            0
                                                           FILTERBUF[7:0]
   Access        RW           RW            RW            RW           RW            RW            RW           RW
    Reset         0            0              0            0            0             0             0            0


            Bits 7:0 – FILTERBUF[7:0] Filter Buffer Value
            These bits hold the value of the filter buffer register. The value is copied in the corresponding FILTER
            register on UPDATE condition.
            These bits have no effect when COUNTER operation mode is selected.




        © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1982
                                                            SAM D5x/E5x Family Data Sheet
                                                                                   PDEC – Position Decoder

53.8.15 Counter Value

           Name:       COUNT
           Offset:     0x1C
           Reset:      0x00000000
           Property:   PAC Write-Protection, Read-Synchronized, Write-Synchronized


     Bit        31           30           29         28                 27     26          25           24


  Access
   Reset


     Bit        23           22           21         20                 19     18          17           16


  Access
   Reset


     Bit        15           14           13         12                 11     10           9           8
                                                          COUNT[15:8]
  Access       RW            RW           RW         RW                RW     RW           RW          RW
   Reset        0             0           0           0                 0      0            0           0


     Bit        7             6           5           4                 3      2            1           0
                                                          COUNT[7:0]
  Access       RW            RW           RW         RW                RW     RW           RW          RW
   Reset        0             0           0           0                 0      0            0           0


           Bits 15:0 – COUNT[15:0] Counter Value
           These bits contain the counter value. To read the most updated counter value, the READSYNC software
           command must be applied first (CTRLBSET.CMD = READSYNC).




       © 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1983
                                                             SAM D5x/E5x Family Data Sheet
                                                                                 PDEC – Position Decoder

53.8.16 Channel x Compare Value

           Name:       CCx
           Offset:     0x20 + x*0x04 [x=0..1]
           Reset:      0x00000000
           Property:   Read-Synchronized, Write-Synchronized


     Bit        31           30           29            28              27   26         25           24


  Access
   Reset


     Bit        23           22           21            20              19   18         17           16


  Access
   Reset


     Bit        15           14           13            12              11   10          9           8
                                                             CC[15:8]
  Access        RW           RW           RW           RW               RW   RW         RW          RW
   Reset         0            0            0            0               0    0           0           0


     Bit         7            6            5            4               3    2           1           0
                                                             CC[7:0]
  Access        RW           RW           RW           RW               RW   RW         RW          RW
   Reset         0            0            0            0               0    0           0           0


           Bits 15:0 – CC[15:0] Channel Compare Value
           These bits hold value of the channel x compare register.




       © 2019 Microchip Technology Inc.                       Datasheet                 DS60001507E-page 1984
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         PDEC – Position Decoder

53.8.17 Channel x Compare Buffer Value

           Name:        CCBUFx
           Offset:      0x30 + x*0x04 [x=0..1]
           Reset:       0x00000000
           Property:    Write-Synchronized


     Bit        31            30           29            28                 27      26            25           24


  Access
   Reset


     Bit        23            22           21            20                 19      18            17           16


  Access
   Reset


     Bit        15            14           13            12                 11      10            9             8
                                                              CCBUF[15:8]
  Access        RW           RW            RW            RW                RW       RW           RW            RW
   Reset         0            0             0             0                 0        0            0             0


     Bit         7            6             5             4                 3        2            1             0
                                                              CCBUF[7:0]
  Access        RW           RW            RW            RW                RW       RW           RW            RW
   Reset         0            0             0             0                 0        0            0             0


           Bits 15:0 – CCBUF[15:0] Channel Compare Buffer Value
           These bits hold the value of the channel x compare buffer register. The register is used as buffer for the
           associated compare register (CCx). Accessing this register using the CPU will affect the corresponding
           CCBVx status bit (STATUS.CCBUFVx).




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 1985
