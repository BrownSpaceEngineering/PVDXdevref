# 48. TC – Timer/Counter

*Source: `Atmel-SAMD51.pdf`, pages 1710-1798 — SAMD51 family datasheet*

                                                        SAM D5x/E5x Family Data Sheet
                                                                                       TC – Timer/Counter


48.    TC – Timer/Counter

48.1   Overview
       There are up to eight TC peripheral instances.
       Each TC consists of a counter, a prescaler, compare/capture channels and control logic. The counter can
       be set to count events, or clock pulses. The counter, together with the compare/capture channels, can be
       configured to timestamp input events or IO pin edges, allowing for capturing of frequency and/or pulse
       width.
       A TC can also perform waveform generation, such as frequency generation and pulse-width modulation.



48.2   Features
         • Selectable configuration
             – 8-, 16- or 32-bit TC operation, with compare/capture channels
         • 2 compare/capture channels (CC) with:
             – Double buffered timer period setting (in 8-bit mode only)
             – Double buffered compare channel
         • Waveform generation
             – Frequency generation
             – Single-slope pulse-width modulation
         • Input capture
             – Event / IO pin edge capture
             – Frequency capture
             – Pulse-width capture
             – Time-stamp capture
             – Minimum and maximum capture
         • One input event
         • Interrupts/output events on:
             – Counter overflow/underflow
             – Compare match or capture
         • Internal prescaler
         • DMA support




       © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1710
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                                    TC – Timer/Counter


48.3   Block Diagram
       Figure 48-1. Timer/Counter Block Diagram

              Base Counter

                   BUFV          PERBUF



                                   PER                      Prescaler



                                                             "count"                                   OVF (INT/Event/DMA Req.)
                    Counter
                                                              "clear"
                                                                                                       ERR (INT Req.)
                                  COUNT                      "load"       Control Logic
                                                            "direction"                                      TC Input Event        Event
                                                                                                                                  System


                                                                   TOP
                                                   =




                                                                               "event"
                                                                                         UPDATE
                                                                BOTTOM
                                           =0




              Compare/Capture
               (Unit x = {0,1}


                                                       "capture"
                   BUFV           CCBUFx                                   Control Logic


                                                                                                                        WO[1]
                                   CCx                                      Waveform
                                                                            Generation                                  WO[0]



                                                         "match"
                                     =                                                                              MCx (INT/Event/DMA Req.)




48.4   Signal Description
       Table 48-1. Signal Description for TC.

        Signal Name                         Type                                                  Description
        WO[1:0]                             Digital output                                        Waveform output
                                            Digital input                                         Capture input

       Refer to I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One signal
       can be mapped on several pins.




       © 2019 Microchip Technology Inc.                               Datasheet                                          DS60001507E-page 1711
                                                             SAM D5x/E5x Family Data Sheet
                                                                                              TC – Timer/Counter

         Related Links
         6. I/O Multiplexing and Considerations



48.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

48.5.1   I/O Lines
         In order to use the I/O lines of this peripheral, the I/O pins must be configured using the I/O Pin Controller
         (PORT).
         Table 48-2. I/O Lines

          Instance                    Signal          I/O Line            Peripheral Function
          MODULE0                     SIGNAL          PAxx                A

         Related Links
         32. PORT - I/O Pin Controller

48.5.2   Power Management
         This peripheral can continue to operate in any Sleep mode where its source clock is running. The
         interrupts can wake up the device from Sleep modes. Events connected to the event system can trigger
         other operations in the system without exiting Sleep modes.
         Related Links
         18. PM – Power Manager

48.5.3   Clocks
         The TC bus clocks (CLK_TCx_APB) can be enabled and disabled in the Main Clock Module. The default
         state of CLK_TCx_APB can be found in the Peripheral Clock Masking.
         The generic clocks (GCLK_TCx) are asynchronous to the user interface clock (CLK_TCx_APB). Due to
         this asynchronicity, accessing certain registers will require synchronization between the clock domains.
         Refer to Synchronization for further details.
         Note: Two instances of the TC may share a peripheral clock channel. In this case, they cannot be set to
         different clock frequencies. Refer to the peripheral clock channel mapping of the Generic Clock Controller
         (GCLK.PCHTRLm) to identify shared peripheral clocks.
         Related Links
         14.8.4 PCHCTRLm
         15.6.2.6 Peripheral Clock Masking

48.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). In order to use DMA requests with
         this peripheral the DMAC must be configured first. Refer to DMAC – Direct Memory Access Controller for
         details.
         Related Links
         22. DMAC – Direct Memory Access Controller




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1712
                                                             SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first. Refer to Nested Vector Interrupt
         Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

48.5.6   Events
         The events of this peripheral are connected to the Event System.
         Related Links
         31. EVSYS – Event System

48.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will halt normal operation. This peripheral can be
         forced to continue operation during debugging - refer to the Debug Control (DBGCTRL) register for
         details.
         Related Links
         48.7.1.11 DBGCTRL

48.5.8   Register Access Protection
         Registers with write access can be optionally write-protected by the Peripheral Access Controller (PAC),
         except for the following:
           •   Interrupt Flag Status and Clear register (INTFLAG)
           •   Status register (STATUS)
           •   Count register (COUNT)
           •   Period and Period Buffer registers (PER, PERBUF)
           •   Compare/Capture Value registers and Compare/Capture Value Buffer registers (CCx, CCBUFx)
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

48.5.9   Analog Connections
         Not applicable.



48.6     Functional Description

48.6.1   Principle of Operation
         The following definitions are used throughout the documentation:




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1713
                                                    SAM D5x/E5x Family Data Sheet
                                                                                     TC – Timer/Counter

Table 48-3. Timer/Counter Definitions

 Name                              Description
 TOP                               The counter reaches TOP when it becomes equal to the highest value in
                                   the count sequence. The TOP value can be the same as Period (PER)
                                   or the Compare Channel 0 (CC0) register value depending on the
                                   waveform generator mode in 48.6.2.6.1 Waveform Output Operations.
 ZERO                              The counter is ZERO when it contains all zeroes
 MAX                               The counter reaches MAX when it contains all ones
 UPDATE                            The timer/counter signals an update when it reaches ZERO or TOP,
                                   depending on the direction settings.
 Timer                             The timer/counter clock control is handled by an internal source
 Counter                           The clock control is handled externally (e.g. counting external events)
 CC                                For compare operations, the CC are referred to as “compare channels”
                                   For capture operations, the CC are referred to as “capture channels.”

Each TC instance has up to two compare/capture channels (CC0 and CC1).
The counter in the TC can either count events from the Event System, or clock ticks of the GCLK_TCx
clock, which may be divided by the prescaler.
The counter value is passed to the CCx where it can be either compared to user-defined values or
captured.
For optimized timing the CCx and CCBUFx registers share a common resource. When writing into
CCBUFx, lock the access to the corresponding CCx register (SYNCBUSY.CCX = 1) till the CCBUFx
register value is not loaded into the CCx register (BUFVx == 1). Each buffer register has a buffer valid
(BUFV) flag that indicates when the buffer contains a new value.
The Counter register (COUNT) and the Compare and Capture registers with buffers (CCx and CCBUFx)
can be configured as 8-, 16- or 32-bit registers, with according MAX values. Mode settings
(CTRLA.MODE) determine the maximum range of the Counter register.
In 8-bit mode, a Period Value (PER) register and its Period Buffer Value (PERBUF) register are also
available. The counter range and the operating frequency determine the maximum time resolution
achievable with the TC peripheral.
The TC can be set to count up or down. Under normal operation, the counter value is continuously
compared to the TOP or ZERO value to determine whether the counter has reached that value. On a
comparison match the TC can request DMA transactions, or generate interrupts or events for the Event
System.
In compare operation, the counter value is continuously compared to the values in the CCx registers. In
case of a match the TC can request DMA transactions, or generate interrupts or events for the Event
System. In waveform generator mode, these comparisons are used to set the waveform period or pulse
width.
Capture operation can be enabled to perform input signal period and pulse width measurements, or to
capture selectable edges from an IO pin or internal event from Event System.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1714
                                                             SAM D5x/E5x Family Data Sheet
                                                                                              TC – Timer/Counter

48.6.2    Basic Operation

48.6.2.1 Initialization
          The following registers are enable-protected, meaning that they can only be written when the TC is
          disabled (CTRLA.ENABLE =0):
           •   Control A register (CTRLA), except the Enable (ENABLE) and Software Reset (SWRST) bits
           •   Drive Control register (DRVCTRL)
           •   Wave register (WAVE)
           •   Event Control register (EVCTRL)
          Writing to Enable-Protected bits and setting the CTRLA.ENABLE bit can be performed in a single 32-bit
          access of the CTRLA register. Writing to Enable-Protected bits and clearing the CTRLA.ENABLE bit
          cannot be performed in a single 32-bit access.
          Before enabling the TC, the peripheral must be configured by the following steps:
           1. Enable the TC bus clock (CLK_TCx_APB).
           2. Select 8-, 16- or 32-bit counter mode via the TC Mode bit group in the Control A register
                (CTRLA.MODE). The default mode is 16-bit.
           3. Select one wave generation operation in the Waveform Generation Operation bit group in the
                WAVE register (WAVE.WAVEGEN).
           4. If desired, the GCLK_TCx clock can be prescaled via the Prescaler bit group in the Control A
                register (CTRLA.PRESCALER).
                  – If the prescaler is used, select a prescaler synchronization operation via the Prescaler and
                     Counter Synchronization bit group in the Control A register (CTRLA.PRESYNC).
           5. If desired, select one-shot operation by writing a '1' to the One-Shot bit in the Control B Set register
                (CTRLBSET.ONESHOT).
           6. If desired, configure the counting direction 'down' (starting from the TOP value) by writing a '1' to
                the Counter Direction bit in the Control B register (CTRLBSET.DIR).
           7. For capture operation, enable the individual channels to capture in the Capture Channel x Enable
                bit group in the Control A register (CTRLA.CAPTEN).
           8. If desired, enable inversion of the waveform output or IO pin input signal for individual channels via
                the Invert Enable bit group in the Drive Control register (DRVCTRL.INVEN).
48.6.2.2 Enabling, Disabling, and Resetting
          The TC is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The TC is
          disabled by writing a zero to CTRLA.ENABLE.
          The TC is reset by writing a '1' to the Software Reset bit in the Control A register (CTRLA.SWRST). All
          registers in the TC, except DBGCTRL, will be reset to their initial state. Refer to the CTRLA register for
          details.
          The TC should be disabled before the TC is reset in order to avoid undefined behavior.
48.6.2.3 Prescaler Selection
          The GCLK_TCx is fed into the internal prescaler.
          The prescaler consists of a counter that counts up to the selected prescaler value, whereupon the output
          of the prescaler toggles.
          If the prescaler value is higher than one, the Counter Update condition can be optionally executed on the
          next GCLK_TCx clock pulse or the next prescaled clock pulse. For further details, refer to Prescaler
          (CTRLA.PRESCALER) and Counter Synchronization (CTRLA.PRESYNC) description.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1715
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

        Prescaler outputs from 1 to 1/1024 are available. For a complete list of available prescaler outputs, see
        the register description for the Prescaler bit group in the Control A register (CTRLA.PRESCALER).
        Note: When counting events, the prescaler is bypassed.
        The joint stream of prescaler ticks and event action ticks is called CLK_TC_CNT.
        Figure 48-2. Prescaler
                                                            PRESCALER          EVACT

                                               GCLK_TC /
          GCLK_TC            Prescaler     {1,2,4,8,64,256,1024}
                                                                                       CLK_TC_CNT          COUNT
                                                                     EVENT


48.6.2.4 Counter Mode
        The counter mode is selected by the Mode bit group in the Control A register (CTRLA.MODE). By default,
        the counter is enabled in the 16-bit counter resolution. Three counter resolutions are available:
          • COUNT8: The 8-bit TC has its own Period Value and Period Buffer Value registers (PER and
             PERBUF).
          • COUNT16: 16-bit is the default counter mode. There is no dedicated period register in this mode.
          • COUNT32: 32-bit mode is achieved by pairing two 16-bit TC peripherals. TC(2n) is paired with TC(2n
             +1).
             When paired, the TC peripherals are configured using the registers of the even-numbered TC. The
             TC bus clocks (CLK_TCx_APB) for both master and slave TCs need to be enabled.
             The odd-numbered partner will act as a slave, and the Slave bit in the Status register
             (STATUS.SLAVE) will be set. The register values of a slave will not reflect the registers of the 32-bit
             counter. Writing to any of the slave registers will not affect the 32-bit counter. Normal access to the
             slave COUNT and CCx registers is not allowed.
48.6.2.5 Counter Operations
        Depending on the mode of operation, the counter is cleared, reloaded, incremented, or decremented at
        each TC clock input (CLK_TC_CNT). A counter clear or reload marks the end of the current counter cycle
        and the start of a new one.
        The counting direction is set by the Direction bit in the Control B register (CTRLB.DIR). If this bit is zero
        the counter is counting up, and counting down if CTRLB.DIR=1. The counter will count up or down for
        each tick (clock or event) until it reaches TOP or ZERO. When it is counting up and TOP is reached, the
        counter will be set to zero at the next tick (overflow) and the Overflow Interrupt Flag in the Interrupt Flag
        Status and Clear register (INTFLAG.OVF) will be set. When it is counting down, the counter is reloaded
        with the TOP value when ZERO is reached (underflow), and INTFLAG.OVF is set.
        INTFLAG.OVF can be used to trigger an interrupt, a DMA request, or an event. An overflow/underflow
        occurrence (i.e., a compare match with TOP/ZERO) will stop counting if the One-Shot bit in the Control B
        register is set (CTRLBSET.ONESHOT).
        It is possible to change the counter value (by writing directly in the COUNT register) even when the
        counter is running. When starting the TC, the COUNT value will be either ZERO or TOP (depending on
        the counting direction set by CTRLBSET.DIR or CTRLBCLR.DIR), unless a different value has been
        written to it, or the TC has been stopped at a value other than ZERO. The write access has higher priority
        than count, clear, or reload. The direction of the counter can also be changed when the counter is
        running. See also the following figure.




        © 2019 Microchip Technology Inc.                           Datasheet                        DS60001507E-page 1716
                                                            SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

          Figure 48-3. Counter Operation

                                            Period (T)           Direction Change          COUNT written

                          MAX
                                                                                                   "reload" update
                                                                                                   "clear" update
                          TOP
          COUNT



                         ZERO



                          DIR

          Due to asynchronous clock domains, the internal counter settings are written when the synchronization is
          complete. Normal operation must be used when using the counter as timer base for the capture
          channels.
48.6.2.5.1 Stop Command and Event Action
          A Stop command can be issued from software by using Command bits in the Control B Set register
          (CTRLBSET.CMD = 0x2, STOP). When a Stop is detected while the counter is running, the counter will
          not retain its current value. All waveforms are cleared and the Stop bit in the Status register is set
          (STATUS.STOP).
48.6.2.5.2 Re-Trigger Command and Event Action
          A re-trigger command can be issued from software by writing the Command bits in the Control B Set
          register (CTRLBSET.CMD = 0x1, RETRIGGER), or from event when a re-trigger event action is
          configured in the Event Control register (EVCTRL.EVACT = 0x1, RETRIGGER).
          When the command is detected during counting operation, the counter will be reloaded or cleared,
          depending on the counting direction (CTRLBSET.DIR or CTRLBCLR.DIR). When the re-trigger command
          is detected while the counter is stopped, the counter will resume counting from the current value in the
          COUNT register.
          Note: When a re-trigger event action is configured in the Event Action bits in the Event Control register
          (EVCTRL.EVACT=0x1, RETRIGGER), enabling the counter will not start the counter. The counter will
          start on the next incoming event and restart on corresponding following event.
48.6.2.5.3 Count Event Action
          The TC can count events. When an event is received, the counter increases or decreases the value,
          depending on direction settings (CTRLBSET.DIR or CTRLBCLR.DIR). The count event action can be
          selected by the Event Action bit group in the Event Control register (EVCTRL.EVACT=0x2, COUNT).
          Note: If this operation mode is selected, PWM generation is not supported.
48.6.2.5.4 Start Event Action
          The TC can start counting operation on an event when previously stopped. In this configuration, the event
          has no effect if the counter is already counting. When the peripheral is enabled, the counter operation
          starts when the event is received or when a re-trigger software command is applied.
          The Start TC on Event action can be selected by the Event Action bit group in the Event Control register
          (EVCTRL.EVACT=0x3, START).




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1717
                                                          SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

48.6.2.6 Compare Operations
         By default, the Compare/Capture channel is configured for compare operations.
         When using the TC and the Compare/Capture Value registers (CCx) for compare operations, the counter
         value is continuously compared to the values in the CCx registers. This can be used for timer or for
         waveform operation.
         The Channel x Compare Buffer (CCBUFx) registers provide double buffer capability. The double buffering
         synchronizes the update of the CCx register with the buffer value at the UPDATE condition or a forced
         update command (CTRLBSET.CMD=UPDATE). For further details, refer to 48.6.2.7 Double Buffering.
         The synchronization prevents the occurrence of odd-length, non-symmetrical pulses and ensures glitch-
         free output.
48.6.2.6.1 Waveform Output Operations
         The compare channels can be used for waveform generation on output port pins. To make the waveform
         available on the connected pin, the following requirements must be fulfilled:
          1. Choose a Waveform Generation mode in the Waveform Generation Operation bit in Waveform
               register (WAVE.WAVEGEN).
          2. Optionally invert the waveform output WO[x] by writing the corresponding Output Waveform x Invert
               Enable bit in the Driver Control register (DRVCTRL.INVENx).
          3. Configure the pins with the I/O Pin Controller. Refer to PORT - I/O Pin Controller for details.
               Note: Event must not be used when the compare channel is set in waveform output operating
               mode.
         The counter value is continuously compared with each CCx value. On a comparison match, the Match or
         Capture Channel x bit in the Interrupt Flag Status and Clear register (INTFLAG.MCx) will be set on the
         next zero-to-one transition of CLK_TC_CNT (see Normal Frequency Operation). An interrupt/and or
         event can be generated on comparison match if enabled. The same condition generates a DMA request.
         There are four waveform configurations for the Waveform Generation Operation bit group in the
         Waveform register (WAVE.WAVEGEN). This will influence how the waveform is generated and impose
         restrictions on the top value. The configurations are:
           • Normal frequency (NFRQ)
           • Match frequency (MFRQ)
           • Normal pulse-width modulation (NPWM)
           • Match pulse-width modulation (MPWM)
         When using NPWM or NFRQ configuration, the TOP will be determined by the counter resolution. In 8-bit
         Counter mode, the Period register (PER) is used as TOP, and the TOP can be changed by writing to the
         PER register. In 16- and 32-bit Counter mode, TOP is fixed to the maximum (MAX) value of the counter.
         Normal Frequency Generation (NFRQ)
         For Normal Frequency Generation, the period time (T) is controlled by the period register (PER) for 8-bit
         Counter mode and MAX for 16- and 32-bit mode. The waveform generation output (WO[x]) is toggled on
         each compare match between COUNT and CCx, and the corresponding Match or Capture Channel x
         Interrupt Flag (INTFLAG.MCx) will be set.




        © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1718
                                                       SAM D5x/E5x Family Data Sheet
                                                                                        TC – Timer/Counter

Figure 48-4. Normal Frequency Operation
                                   Period (T)     Direction Change   COUNT Written

                MAX                                                                                  "reload" update
                                                                                                     "clear" update
                                                                                                     "match"
 COUNT          TOP

                CCx

               ZERO

               WO[x]
Match Frequency Generation (MFRQ)
For Match Frequency Generation, the period time (T) is controlled by the CC0 register instead of PER or
MAX. WO[0] toggles on each Update condition.
Figure 48-5. Match Frequency Operation

                                     Period (T)              Direction Change        COUNT Written

                MAX
                                                                                            "reload" update
                                                                                            "clear" update
                CC0
 COUNT



               ZERO


              WO[0]

Normal Pulse-Width Modulation Operation (NPWM)
NPWM uses single-slope PWM generation.
For single-slope PWM generation, the period time (T) is controlled by the TOP value, and CCx controls
the duty cycle of the generated waveform output. When up-counting, the WO[x] is set at start or compare
match between the COUNT and TOP values, and cleared on compare match between COUNT and CCx
register values. When down-counting, the WO[x] is cleared at start or compare match between the
COUNT and ZERO values, and set on compare match between COUNT and CCx register values.
The following equation calculates the exact resolution for a single-slope PWM (RPWM_SS) waveform:
             log(TOP+1)
�PWM_SS =
                log(2)
The PWM frequency (fPWM_SS) depends on TOP value and the peripheral clock frequency (fGCLK_TC), and
can be calculated by the following equation:
              �GCLK_TC
�PWM_SS =
             N(TOP+1)
Where N represents the prescaler divider used (1, 2, 4, 8, 16, 64, 256, 1024).
Match Pulse-Width Modulation Operation (MPWM)
In MPWM, the output of WO[1] is depending on CC1 as shown in the figure below. On every overflow/
underflow, a one-TC-clock-cycle negative pulse is put out on WO[0] (not shown in the figure).




© 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 1719
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                 TC – Timer/Counter

        Figure 48-6. Match PWM Operation
                                       Period(T)         CCx= Zero         CCx= TOP
                        MAX                                                                                 " clear" update
                                                                                                            " match"
                        CC0


         COUNT
                              CC1


                        ZERO


                       WO[1]
        The table below shows the Update Counter and Overflow Event/Interrupt Generation conditions in
        different operation modes.
        Table 48-4. Counter Update and Overflow Event/interrupt Conditions in TC

         Name         Operation                    TOP   Update            Output Waveform             OVFIF/Event
                                                                           On Match     On Update      Up       Down
         NFRQ         Normal Frequency             PER   TOP/ ZERO         Toggle       Stable         TOP      ZERO
         MFRQ         Match Frequency              CC0   TOP/ ZERO         Toggle       Stable         TOP      ZERO
         NPWM         Single-slope PWM             PER   TOP/ ZERO         See description above.      TOP      ZERO
         MPWM         Single-slope PWM             CC0   TOP/ ZERO         Toggle       Toggle         TOP      ZERO

        Related Links
        32. PORT - I/O Pin Controller

48.6.2.7 Double Buffering
        The Compare Channels (CCx) registers, and the Period (PER) register in 8-bit mode are double buffered.
        Each buffer register has a buffer valid bit (CCBUFVx or PERBUFV) in the STATUS register, which
        indicates that the buffer register contains a new valid value that can be copied into the corresponding
        register. As long as the respective buffer valid status flag (PERBUFV or CCBUFVx) are set to '1', related
        syncbusy bits are set (SYNCBUSY.PER or SYNCBUSY.CCx), a write to the respective PER/PERBUF or
        CCx/CCBUFx registers will generate a PAC error, and access to the respective PER or CCx register is
        invalid.
        When the buffer valid flag bit in the STATUS register is '1' and the Lock Update bit in the CTRLB register
        is set to '0', (writing CTRLBCLR.LUPD to '1'), double buffering is enabled: the data from buffer registers
        will be copied into the corresponding register under hardware UPDATE conditions, then the buffer valid
        flags bit in the STATUS register are automatically cleared by hardware.
        Note: The software update command (CTRLBSET.CMD=0x3) is acting independently of the LUPD
        value.
        A compare register is double buffered as in the following figure.




        © 2019 Microchip Technology Inc.                             Datasheet                      DS60001507E-page 1720
                                                    SAM D5x/E5x Family Data Sheet
                                                                                      TC – Timer/Counter

Figure 48-7. Compare Channel Double Buffering

                                                  "write enable"      "data write"




                                          CCBUFVx             EN       CCBUFx


                                                              EN          CCx
                        UPDATE
                                                            COUNT

                                                                                  "match"
                                                                         =
Both the registers (PER/CCx) and corresponding buffer registers (PERBUF/CCBUFx) are available in the
I/O register map, and the double buffering feature is not mandatory. The double buffering is disabled by
writing a '1' to CTRLBSET.LUPD.
Note: In NFRQ, MFRQ or PWM down-counting counter mode (CTRLBSET.DIR=1), when double
buffering is enabled (CTRLBCLR.LUPD=1), PERBUF register is continously copied into the PER
independently of update conditions.
Changing the Period
The counter period can be changed by writing a new TOP value to the Period register (PER or CC0,
depending on the waveform generation mode), which is available in 8-bit mode. Any period update on
registers (PER or CCx) is effective after the synchronization delay.
Figure 48-8. Unbuffered Single-Slope Up-Counting Operation

                                                             Counter Wraparound

                MAX
                                                                                            "clear" update
                                                                                            "write"

 COUNT



                ZERO

                                    New TOP written to           New TOP written to
                                    PER that is higher            PER that is lower
                                   than current COUNT           than current COUNT

A counter wraparound can occur in any operation mode when up-counting without buffering, see Figure
48-8.
COUNT and TOP are continuously compared, so when a new TOP value that is lower than current
COUNT is written to TOP, COUNT will wrap before a compare match.




© 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1721
                                                           SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

        Figure 48-9. Unbuffered Single-Slope Down-Counting Operation

                        MAX
                                                                                                  "reload" update
                                                                                                  "write"

         COUNT



                       ZERO

                               New TOP written to             New TOP written to
                               PER that is higher              PER that is lower
                              than current COUNT             than current COUNT

        When double buffering is used, the buffer can be written at any time and the counter will still maintain
        correct operation. The period register is always updated on the update condition, as shown in Figure
        48-10. This prevents wraparound and the generation of odd waveforms.
        Figure 48-10. Changing the Period Using Buffering

                         MAX
                                                                                                   " clear" update
                                                                                                   " write"

         COUNT



                        ZERO

                                            New TOP written to      New TOP written to
                                             PER that is higher      PER that is lower
                                           than currentCOUNT       than currentCOUNT

48.6.2.8 Capture Operations
        To enable and use capture operations, the corresponding Capture Channel x Enable bit in the Control A
        register (CTRLA.CAPTENx) must be written to '1'.
        A capture trigger can be provided by input event line TC_EV or by asynchronous IO pin WO[x] for each
        capture channel or by a TC event. To enable the capture from input event line, Event Input Enable bit in
        the Event Control register (EVCTRL.TCEI) must be written to '1'. To enable the capture from the IO pin,
        the Capture On Pin x Enable bit in CTRLA register (CTRLA.COPENx) must be written to '1'.
        Note:
         1. The RETRIGGER, COUNT and START event actions are available only on an event from the Event
              System.
         2. Event system channels must be configured to operate in asynchronous mode of operation when
              used for capture operations.
        By default, a capture operation is done when a rising edge is detected on the input signal. Capture on
        falling edge is available, its activation is depending on the input source:
          • When the channel is used with a IO pin, write a '1' to the corresponding Invert Enable bit in the Drive
              Control register (DRVCTRL.INVENx).




        © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1722
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          TC – Timer/Counter

           • When the channel is counting events from the Event System, write a '1' to the TC Event Input Invert
             Enable bit in Event Control register (EVCTRL.TCINV).
         Figure 48-11. Capture Double Buffering
                                       "capture"                   COUNT



                                            BV        EN            CCBx


                                            IF        EN             CCx

                                       "INT/DMA
                                        request"                  data read
         For input capture, the buffer register and the corresponding CCx act like a FIFO. When CCx is empty or
         read, any content in CCBUFx is transferred to CCx. The buffer valid flag is passed to set the CCx
         interrupt flag (IF) and generate the optional interrupt, event or DMA request. The CCBUFx register value
         can't be read, all captured data must be read from CCx register.
         Note:
         When up-counting (CTRLBSET.DIR=0), counter values lower than 1 cannot be captured. To capture the
         full range including value 0, the TC must be in down-counting mode (CTRLBSET.DIR=0).
48.6.2.8.1 Event Capture Action
         The compare/capture channels can be used as input capture channels to capture events from the Event
         System and give them a timestamp. The following figure shows four capture events for one capture
         channel.
         Figure 48-12. Input Capture Timing



                      events

                         TOP




         COUNT



                       ZERO

                                       Capture 0   Capture 1   Capture 2           Capture 3

         The TC can detect capture overflow of the input capture channels: When a new capture event is detected
         while the Capture Interrupt flag (INTFLAG.MCx) is still set, the new timestamp will not be stored and
         INTFLAG.ERR will be set.




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 1723
                                                              SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

48.6.2.8.2 Period and Pulse-Width (PPW) Capture Action
         The TC can perform two input captures and restart the counter on one of the edges. This enables the TC
         to measure the pulse width and period and to characterize the frequency f and duty cycle of an input
         signal:
              1
         �=
              �
                        ��
         dutyCycle =
                        �
         Figure 48-13. PWP Capture

                                                        Period (T)

          external signal                   Pulsewitdh (tp)


          events


                          MAX

                                                                                                         "capture"

          COUNT



                         ZERO
                                                          CC0                  CC1       CC0          CC1

         Selecting PWP in the Event Action bit group in the Event Control register (EVCTRL.EVACT) enables the
         TC to perform one capture action on the rising edge and the other one on the falling edge. The period T
         will be captured into CC1 and the pulse width tp in CC0. EVCTRL.EVACT=PPW (period and pulse-width)
         offers identical functionality, but will capture T into CC0 and tp into CC1.
         The TC Event Input Invert Enable bit in the Event Control register (EVCTRL.TCINV) is used to select
         whether the wraparound should occur on the rising edge or the falling edge. If EVCTRL.TCINV=1, the
         wraparound will happen on the falling edge. In case pin capture is enabled, this can also be achieved by
         modifying the value of the DRVCTRL.INVENx bit.
         The TC can detect capture overflow of the input capture channels: When a new capture event is detected
         while the Capture Interrupt flag (INTFLAG.MCx) is still set, the new timestamp will not be stored and
         INTFLAG.ERR will be set.
         Note: The corresponding capture is working only if the channel is enabled in capture mode
         (CTRLA.CAPTENx=1). If not, the capture action is ignored and the channel is enabled in compare mode
         of operation. Consequently, both channels must be enabled in order to fully characterize the input.
48.6.2.8.3 Pulse-Width Capture Action
         The TC performs the input capture on the falling edge of the input signal. When the edge is detected, the
         counter value is cleared and the TC stops counting. When a rising edge is detected on the input signal,
         the counter restarts the counting operation. To enable the operation on opposite edges, the input signal to
         capture must be inverted (refer to DRVCTRL.INVEN or EVCTRL.TCEINV).




         © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1724
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          TC – Timer/Counter

         Figure 48-14. Pulse-Width Capture on Channel 0

          external signal                   Pulsewitdh (tp)


          events


                          MAX

                                                                                                      "capture"

                                                                                                      "restart"
          COUNT



                         ZERO
                                                          CC0                           CC0

         The TC can detect capture overflow of the input capture channels: When a new capture event is detected
         while the Capture Interrupt flag (INTFLAG.MCx) is still set, the new timestamp will not be stored and
         INTFLAG.ERR will be set.

48.6.3   Additional Features

48.6.3.1 One-Shot Operation
         When one-shot is enabled, the counter automatically stops on the next Counter Overflow or Underflow
         condition. When the counter is stopped, the Stop bit in the Status register (STATUS.STOP) is
         automatically set and the waveform outputs are set to zero.
         One-shot operation is enabled by writing a '1' to the One-Shot bit in the Control B Set register
         (CTRLBSET.ONESHOT), and disabled by writing a '1' to CTRLBCLR.ONESHOT. When enabled, the TC
         will count until an overflow or underflow occurs and stops counting operation. The one-shot operation can
         be restarted by a re-trigger software command, a re-trigger event, or a start event. When the counter
         restarts its operation, STATUS.STOP is automatically cleared.
48.6.3.2 Time-Stamp Capture
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




         © 2019 Microchip Technology Inc.                       Datasheet                     DS60001507E-page 1725
                                                          SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

        Figure 48-15. Time-Stamp
        Capture Events

                MAX

                TOP
                                                                                                        "capture"
                                                                                                        "overflow"

        COUNT



                ZERO

          CCx Value             COUNT        COUNT          TOP            COUNT              MAX

48.6.3.3 Minimum Capture
        The minimum capture is enabled by writing the CAPTMIN mode in the Channel n Capture Mode bits in
        the Control A register (CTRLA.CAPTMODEn = CAPTMIN).
        CCx Content:
        In CAPTMIN operations, CCx keeps the Minimum captured values. Before enabling this mode of capture,
        the user must initialize the corresponding CCx register value to a value different from zero. If the CCx
        register initial value is zero, no captures will be performed using the corresponding channel.
        MCx Behaviour:
        In CAPTMIN operation, capture is performed only when on capture event time, the counter value is lower
        than the last captured value. The MCx interrupt flag is set only when on capture event time, the counter
        value is upper or equal to the value captured on the previous event. So interrupt flag is set when a new
        absolute local Minimum value has been detected.
48.6.3.4 Maximum Capture
        The maximum capture is enabled by writing the CAPTMAX mode in the Channel n Capture Mode bits in
        the Control A register (CTRLA.CAPTMODEn = CAPTMAX).
        CCx Content:
        In CAPTMAX operations, CCx keeps the Maximum captured values. Before enabling this mode of
        capture, the user must initialize the corresponding CCx register value to a value different from TOP. If the
        CCx register initial value is TOP, no captures will be performed using the corresponding channel.
        MCx Behaviour:
        In CAPTMAX operation, capture is performed only when on capture event time, the counter value is
        upper than the last captured value. The MCx interrupt flag is set only when on capture event time, the
        counter value is lower or equal to the value captured on the previous event. So interrupt flag is set when
        a new absolute local Maximum value has been detected.




       © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1726
                                                            SAM D5x/E5x Family Data Sheet
                                                                                              TC – Timer/Counter

         Figure 48-16. Maximum Capture Operation with CC0 Initialized with ZERO Value
                         TOP
                                                                                                         "clear" update
         COUNT            CC0                                                                            "match"

                         ZERO




                    Input event
                    CC0 Event/
                      Interrupt

48.6.4   DMA Operation
         The TC can generate the following DMA requests:
          • Overflow (OVF): the request is set when an update condition (overflow, underflow or re-trigger) is
             detected, the request is cleared by hardware on DMA acknowledge.
          • Match or Capture Channel x (MCx): for a compare channel, the request is set on each compare
             match detection, the request is cleared by hardware on DMA acknowledge. For a capture channel,
             the request is set when valid data is present in the CCx register, and cleared when CCx register is
             read.

48.6.5   Interrupts
         The TC has the following interrupt sources:
           • Overflow/Underflow (OVF)
           • Match or Capture Channel x (MCx)
           • Capture Overflow Error (ERR)
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear register (INTFLAG) is set when the interrupt condition occurs.
         Each interrupt can be individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Set register (INTENSET), and disabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Clear register (INTENCLR).
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until either the interrupt flag is cleared, the interrupt is disabled, or
         the TC is reset. See INTFLAG for details on how to clear interrupt flags.
         The TC has one common interrupt request line for all the interrupt sources. The user must read the
         INTFLAG register to determine which interrupt condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated. Refer to Nested
         Vector Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

48.6.6   Events
         The TC can generate the following output events:
           • Overflow/Underflow (OVF)
           • Match or Capture Channel x (MCx)




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1727
                                                             SAM D5x/E5x Family Data Sheet
                                                                                          TC – Timer/Counter

         Writing a '1' to an Event Output bit in the Event Control register (EVCTRL.MCEOx) enables the
         corresponding output event. The output event is disabled by writing EVCTRL.MCEOx=0.
         One of the following event actions can be selected by the Event Action bit group in the Event Control
         register (EVCTRL.EVACT):
           • Disable event action (OFF)
           • Start TC (START)
           • Re-trigger TC (RETRIGGER)
           • Count on event (COUNT)
           • Capture time stamp (STAMP)
           • Capture Period (PPW and PWP)
           • Capture Pulse Width (PW)
         Writing a '1' to the TC Event Input bit in the Event Control register (EVCTRL.TCEI) enables input events
         to the TC. Writing a '0' to this bit disables input events to the TC. The TC requires only asynchronous
         event inputs. For further details on how configuring the asynchronous events, refer to EVSYS - Event
         System.
         Related Links
         31. EVSYS – Event System

48.6.7   Sleep Mode Operation
         The TC can be configured to operate in any sleep mode. To be able to run in standby, the RUNSTDBY bit
         in the Control A register (CTRLA.RUNSTDBY) must be '1'. This peripheral can wake up the device from
         any sleep mode using interrupts or perform actions through the Event System.
         If the On Demand bit in the Control A register (CTRLA.ONDEMAND) is written to '1', the module stops
         requesting its peripheral clock when the STOP bit in STATUS register (STATUS.STOP) is set to '1'. When
         a re-trigger or start condition is detected, the TC requests the clock before the operation starts.

48.6.8   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset and Enable bits in Control A register (CTRLA.SWRST and CTRLA.ENABLE)
           • Capture Channel Buffer Valid bit in STATUS register (STATUS.CCBUFVx)
         The following registers are synchronized when written:
           •   Control B Clear and Control B Set registers (CTRLBCLR and CTRLBSET)
           •   Count Value register (COUNT)
           •   Period Value and Period Buffer Value registers (PER and PERBUF)
           •   Channel x Compare/Capture Value and Channel x Compare/Capture Buffer Value registers (CCx and
               CCBUFx)
         The following registers are synchronized when read:
           • Count Value register (COUNT): synchronization is done on demand through READSYNC command
             (CTRLBSET.CMD).
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1728
                                                         SAM D5x/E5x Family Data Sheet
                                                                                          TC – Timer/Counter

       Required read synchronization is denoted by the "Read-Synchronized" property in the register
       description.



48.7   Register Description
       Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
       8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
       accessed directly.
       Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
       write protection is denoted by the "PAC Write-Protection" property in each individual register description.
       For details, refer to Register Access Protection.
       Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
       Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
       refer to Synchronization.
       Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
       Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1729
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                     TC – Timer/Counter

48.7.1    Register Summary - 8-bit Mode

 Offset        Name        Bit Pos.

                              7:0     ONDEMAND RUNSTDBY      PRESCSYNC[1:0]              MODE[1:0]          ENABLE        SWRST
                             15:8      DMAOS                                         ALOCK               PRESCALER[2:0]
  0x00        CTRLA
                             23:16                         COPEN1     COPEN0                               CAPTEN1        CAPTEN0
                             31:24                                      CAPTMODE1[1:0]                        CAPTMODE0[1:0]
  0x04       CTRLBCLR         7:0               CMD[2:0]                                       ONESHOT       LUPD           DIR
  0x05       CTRLBSET         7:0               CMD[2:0]                                       ONESHOT       LUPD           DIR
                              7:0                           TCEI       TCINV                               EVACT[2:0]
  0x06        EVCTRL
                             15:8                          MCEO1      MCEO0                                               OVFEO
  0x08       INTENCLR         7:0                           MC1        MC0                                    ERR          OVF
  0x09       INTENSET         7:0                           MC1        MC0                                    ERR          OVF
  0x0A       INTFLAG          7:0                           MC1        MC0                                    ERR          OVF
  0x0B        STATUS          7:0                          CCBUFV1    CCBUFV0       PERBUFV                  SLAVE         STOP
  0x0C         WAVE           7:0                                                                              WAVEGEN[1:0]
  0x0D       DRVCTRL          7:0                                                                           INVEN1        INVEN0
  0x0E       Reserved
  0x0F       DBGCTRL          7:0                                                                                         DBGRUN
                              7:0       CC1       CC0                 COUNT          STATUS     CTRLB       ENABLE        SWRST
                             15:8
  0x10      SYNCBUSY
                             23:16
                             31:24
  0x14        COUNT           7:0                                         COUNT[7:0]
  0x15
   ...       Reserved
  0x1A
  0x1B         PER            7:0                                             PER[7:0]
  0x1C          CC0           7:0                                              CC[7:0]
  0x1D          CC1           7:0                                              CC[7:0]
  0x1E
   ...       Reserved
  0x2E
  0x2F        PERBUF          7:0                                         PERBUF[7:0]
  0x30        CCBUF0          7:0                                         CCBUF[7:0]
  0x31        CCBUF1          7:0                                         CCBUF[7:0]




          © 2019 Microchip Technology Inc.                         Datasheet                              DS60001507E-page 1730
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.7.1.1 Control A

            Name:       CTRLA
            Offset:     0x00
            Reset:      0x00000000
            Property:   PAC Write-Protection, Write-Synchronized, Enable-Protected


      Bit        31           30             29          28          27                26          25           24
                                                         CAPTMODE1[1:0]                            CAPTMODE0[1:0]
   Access                                               R/W          R/W                          R/W           R/W
    Reset                                                0            0                            0             0


      Bit        23           22             21          20          19                18          17           16
                                           COPEN1     COPEN0                                   CAPTEN1        CAPTEN0
   Access                                   R/W         R/W                                       R/W           R/W
    Reset                                    0           0                                         0             0


      Bit        15           14             13          12          11                10          9             8
               DMAOS                                               ALOCK                     PRESCALER[2:0]
   Access       R/W                                                  R/W               R/W        R/W           R/W
    Reset         0                                                   0                 0          0             0


      Bit         7            6             5           4            3                 2          1             0
             ONDEMAND     RUNSTDBY           PRESCSYNC[1:0]                MODE[1:0]            ENABLE        SWRST
   Access       R/W          R/W            R/W         R/W          R/W               R/W        R/W           W
    Reset         0            0             0           0            0                 0          0             0


            Bits 28:27 – CAPTMODE1[1:0] Capture mode Channel 1
            These bits select the channel 1 capture mode.
             Value      Name                              Description
             0x0        DEFAULT                           Default capture
             0x1        CAPTMIN                           Minimum capture
             0x2        CAPTMAX                           Maximum capture
             0x3                                          Reserved

            Bits 25:24 – CAPTMODE0[1:0] Capture mode Channel 0
            These bits select the channel 0 capture mode.
             Value      Name                              Description
             0x0        DEFAULT                           Default capture
             0x1        CAPTMIN                           Minimum capture
             0x2        CAPTMAX                           Maximum capture
             0x3                                          Reserved

            Bits 20, 21 – COPENx Capture On Pin x Enable
            Bit x of COPEN[1:0] selects the trigger source for capture operation, either events or I/O pin input.
            Value       Description
            0           Event from Event System is selected as trigger source for capture operation on channel x.
            1           I/O pin is selected as trigger source for capture operation on channel x.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1731
                                                    SAM D5x/E5x Family Data Sheet
                                                                                    TC – Timer/Counter

Bits 16, 17 – CAPTENx Capture Channel x Enable
Bit x of CAPTEN[1:0] selects whether channel x is a capture or a compare channel.
These bits are not synchronized.
 Value      Description
 0          CAPTEN disables capture on channel x.
 1          CAPTEN enables capture on channel x.

Bit 15 – DMAOS DMA One-Shot Trigger Mode
This bit enables the DMA One-shot Trigger Mode.
Writing a '1' to this bit will generate a DMA trigger on TC cycle following a
TC_CTRLBSET_CMD_DMAOS command.
Writing a '0' to this bit will generate DMA triggers on each TC cycle.
This bit is not synchronized.

Bit 11 – ALOCK Auto Lock
When this bit is set, Lock bit update (LUPD) is set to '1' on each overflow/underflow or re-trigger event.
This bit is not synchronized.
 Value       Description
 0           The LUPD bit is not affected on overflow/underflow, and re-trigger event.
 1           The LUPD bit is set on each overflow/underflow or re-trigger event.

Bits 10:8 – PRESCALER[2:0] Prescaler
These bits select the counter prescaler factor.
These bits are not synchronized.
 Value      Name                     Description
 0x0        DIV1                     Prescaler: GCLK_TC
 0x1        DIV2                     Prescaler: GCLK_TC/2
 0x2        DIV4                     Prescaler: GCLK_TC/4
 0x3        DIV8                     Prescaler: GCLK_TC/8
 0x4        DIV16                    Prescaler: GCLK_TC/16
 0x5        DIV64                    Prescaler: GCLK_TC/64
 0x6        DIV256                   Prescaler: GCLK_TC/256
 0x7        DIV1024                  Prescaler: GCLK_TC/1024

Bit 7 – ONDEMAND Clock On Demand
This bit selects the clock requirements when the TC is stopped.
In standby mode, if the Run in Standby bit (CTRLA.RUNSTDBY) is '0', ONDEMAND is forced to '0'.
This bit is not synchronized.
 Value       Description
 0           The On Demand is disabled. If On Demand is disabled, the TC will continue to request the
             clock when its operation is stopped (STATUS.STOP=1).
 1           The On Demand is enabled. When On Demand is enabled, the stopped TC will not request
             the clock. The clock is requested when a software re-trigger command is applied or when an
             event with start/re-trigger action is detected.

Bit 6 – RUNSTDBY Run in Standby
This bit is used to keep the TC running in standby mode.
This bit is not synchronized.




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1732
                                                     SAM D5x/E5x Family Data Sheet
                                                                                       TC – Timer/Counter

 Value        Description
 0            The TC is halted in standby.
 1            The TC continues to run in standby.

Bits 5:4 – PRESCSYNC[1:0] Prescaler and Counter Synchronization
These bits select whether the counter should wrap around on the next GCLK_TCx clock or the next
prescaled GCLK_TCx clock. It also makes it possible to reset the prescaler.
These bits are not synchronized.
 Value      Name       Description
 0x0        GCLK       Reload or reset the counter on next generic clock
 0x1        PRESC      Reload or reset the counter on next prescaler clock
 0x2        RESYNC Reload or reset the counter on next generic clock. Reset the prescaler counter
 0x3        -          Reserved

Bits 3:2 – MODE[1:0] Timer Counter Mode
These bits select the counter mode.
These bits are not synchronized.
 Value      Name                      Description
 0x0        COUNT16                   Counter in 16-bit mode
 0x1        COUNT8                    Counter in 8-bit mode
 0x2        COUNT32                   Counter in 32-bit mode
 0x3        -                         Reserved

Bit 1 – ENABLE Enable
Due to synchronization, there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately, and the ENABLE
Synchronization Busy bit in the SYNCBUSY register (SYNCBUSY.ENABLE) will be set.
SYNCBUSY.ENABLE will be cleared when the operation is complete.
This bit is not enable protected.
 Value       Description
 0           The peripheral is disabled.
 1           The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the TC, except DBGCTRL, to their initial state, and the TC will
be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence; all other writes in the same write-operation
will be discarded.




© 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 1733
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.1.2 Control B Clear

            Name:        CTRLBCLR
            Offset:      0x04
            Reset:       0x00
            Property:    PAC Write-Protection, Read-Synchronized, Write-Synchronized

            This register allows the user to clear bits in the CTRLB register without doing a read-modify-write
            operation. Changes in this register will also be reflected in the Control B Set register (CTRLBSET).

      Bit         7             6             5              4             3               2       1               0
                             CMD[2:0]                                                ONESHOT     LUPD          DIR
   Access        R/W           R/W           R/W                                          R/W     R/W         R/W
    Reset         0             0             0                                            0       0               0


            Bits 7:5 – CMD[2:0] Command
            These bits are used for software control of the TC. The commands are executed on the next prescaled
            GCLK_TC clock cycle. When a command has been executed, the CMD bit group will be read back as
            zero.
            Writing 0x0 to these bits has no effect.
            Writing a '1' to any of these bits will clear the pending command.

            Bit 2 – ONESHOT One-Shot on Counter
            This bit controls one-shot operation of the TC.
            Writing a '0' to this bit has no effect
            Writing a '1' to this bit will disable one-shot operation.
             Value        Description
             0            The TC will wrap around and continue counting on an overflow/underflow condition.
             1            The TC will wrap around and stop on the next underflow/overflow condition.

            Bit 1 – LUPD Lock Update
            This bit controls the update operation of the TC buffered registers.
            When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
            on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
            hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
            can be unlocked.
            This bit has no effect when input capture operation is enabled.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the LUPD bit.
             Value        Description
             0            The CCBUFx and PERBUF buffer registers value are copied into CCx and PER registers on
                          hardware update condition.
             1            The CCBUFx and PERBUF buffer registers value are not copied into CCx and PER registers
                          on hardware update condition.

            Bit 0 – DIR Counter Direction
            This bit is used to change the direction of the counter.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the bit and make the counter count up.




        © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1734
                                                  SAM D5x/E5x Family Data Sheet
                                                                   TC – Timer/Counter

 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                   Datasheet         DS60001507E-page 1735
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.7.1.3 Control B Set

            Name:       CTRLBSET
            Offset:     0x05
            Reset:      0x00
            Property:   PAC Write-Protection, Read-synchronized, Write-Synchronized

            This register allows the user to set bits in the CTRLB register without doing a read-modify-write operation.
            Changes in this register will also be reflected in the Control B Clear register (CTRLBCLR).

      Bit         7            6             5            4             3            2             1            0
                            CMD[2:0]                                             ONESHOT         LUPD          DIR
   Access       R/W           R/W           R/W                                     R/W           R/W          R/W
    Reset         0            0             0                                       0             0            0


            Bits 7:5 – CMD[2:0] Command
            These bits are used for software control of the TC. The commands are executed on the next prescaled
            GCLK_TC clock cycle. When a command has been executed, the CMD bit group will be read back as
            zero.
            Writing 0x0 to these bits has no effect.
            Writing a value different from 0x0 to these bits will issue a command for execution.
             Value      Name                      Description
             0x0        NONE                      No action
             0x1        RETRIGGER                 Force a start, restart or retrigger
             0x2        STOP                      Force a stop
             0x3        UPDATE                    Force update of double buffered registers
             0x4        READSYNC                  Force a read synchronization of COUNT

            Bit 2 – ONESHOT One-Shot on Counter
            This bit controls one-shot operation of the TC.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will enable one-shot operation.
             Value        Description
             0            The TC will wrap around and continue counting on an overflow/underflow condition.
             1            The TC will wrap around and stop on the next underflow/overflow condition.

            Bit 1 – LUPD Lock Update
            This bit controls the update operation of the TC buffered registers.
            When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
            on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
            hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
            can be unlocked.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the LUPD bit.
            This bit has no effect when input capture operation is enabled.
             Value        Description
             0            The CCBUFx and PERBUF buffer registers value are copied into CCx and PER registers on
                          hardware update condition.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1736
                                                     SAM D5x/E5x Family Data Sheet
                                                                              TC – Timer/Counter

 Value        Description
 1            The CCBUFx and PERBUF buffer registers value are not copied into CCx and PER registers
              on hardware update condition.

Bit 0 – DIR Counter Direction
This bit is used to change the direction of the counter.
Writing a '0' to this bit has no effect
Writing a '1' to this bit will clear the bit and make the counter count up.
 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                      Datasheet                  DS60001507E-page 1737
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

48.7.1.4 Event Control

            Name:       EVCTRL
            Offset:     0x06
            Reset:      0x0000
            Property:   PAC Write-Protection, Enable-Protected


      Bit        15           14            13           12           11         10            9            8
                                           MCEO1       MCEO0                                             OVFEO
   Access                                   R/W         R/W                                               R/W
    Reset                                    0           0                                                  0


      Bit         7            6             5           4            3           2            1            0
                                           TCEI        TCINV                               EVACT[2:0]
   Access                                   R/W         R/W                      R/W          R/W         R/W
    Reset                                    0           0                        0            0            0


            Bit 13 – MCEO1 Match or Capture Channel x Event Output Enable [x = 1..0]
            These bits enable the generation of an event for every match or capture on channel x.
             Value      Description
             0          Match/Capture event on channel x is disabled and will not be generated.
             1          Match/Capture event on channel x is enabled and will be generated for every compare/
                        capture.

            Bit 12 – MCEO0 Match or Capture Channel x Event Output Enable [x = 1..0]
            These bits enable the generation of an event for every match or capture on channel x.
             Value      Description
             0          Match/Capture event on channel x is disabled and will not be generated.
             1          Match/Capture event on channel x is enabled and will be generated for every compare/
                        capture.

            Bit 8 – OVFEO Overflow/Underflow Event Output Enable
            This bit enables the Overflow/Underflow event. When enabled, an event will be generated when the
            counter overflows/underflows.
             Value      Description
             0          Overflow/Underflow event is disabled and will not be generated.
             1          Overflow/Underflow event is enabled and will be generated for every counter overflow/
                        underflow.

            Bit 5 – TCEI TC Event Enable
            This bit is used to enable asynchronous input events to the TC.
             Value       Description
             0            Incoming events are disabled.
             1            Incoming events are enabled.

            Bit 4 – TCINV TC Inverted Event Input Polarity
            This bit inverts the asynchronous input event source.
             Value       Description
             0           Input event source is not inverted.




        © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1738
                                                SAM D5x/E5x Family Data Sheet
                                                                                 TC – Timer/Counter

 Value        Description
 1            Input event source is inverted.

Bits 2:0 – EVACT[2:0] Event Action
These bits define the event action the TC will perform on an event.
 Value      Name                    Description
 0x0        OFF                     Event action disabled
 0x1        RETRIGGER               Start, restart or retrigger TC on event
 0x2        COUNT                   Count on event
 0x3        START                   Start TC on event
 0x4        STAMP                   Time stamp capture
 0x5        PPW                     Period captured in CC0, pulse width in CC1
 0x6        PWP                     Period captured in CC1, pulse width in CC0
 0x7        PW                      Pulse width capture




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1739
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                     TC – Timer/Counter

48.7.1.5 Interrupt Enable Clear

            Name:        INTENCLR
            Offset:      0x08
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

      Bit         7              6             5              4             3              2             1              0
                                              MC1           MC0                                         ERR            OVF
   Access                                     R/W           R/W                                         R/W            R/W
    Reset                                      0              0                                          0              0


            Bit 5 – MC1 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will clear the corresponding Match or Capture Channel x Interrupt Enable bit, which
            disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 4 – MC0 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will clear the corresponding Match or Capture Channel x Interrupt Enable bit, which
            disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 1 – ERR Error Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Error Interrupt Enable bit, which disables the Error interrupt.
            Value         Description
            0             The Error interrupt is disabled.
            1             The Error interrupt is enabled.

            Bit 0 – OVF Overflow Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Overflow Interrupt Enable bit, which disables the Overflow interrupt
            request.
             Value        Description
             0            The Overflow interrupt is disabled.
             1            The Overflow interrupt is enabled.




        © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1740
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                    TC – Timer/Counter

48.7.1.6 Interrupt Enable Set

            Name:        INTENSET
            Offset:      0x09
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

      Bit         7              6             5             4              3             2              1           0
                                              MC1           MC0                                        ERR          OVF
   Access                                     R/W           R/W                                        R/W          R/W
    Reset                                      0             0                                           0           0


            Bit 5 – MC1 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will set the corresponding Match or Capture Channel x Interrupt Enable bit, which
            enables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 4 – MC0 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will set the corresponding Match or Capture Channel x Interrupt Enable bit, which
            enables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 1 – ERR Error Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Error Interrupt Enable bit, which enables the Error interrupt.
            Value         Description
            0             The Error interrupt is disabled.
            1             The Error interrupt is enabled.

            Bit 0 – OVF Overflow Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Overflow Interrupt Enable bit, which enables the Overflow interrupt
            request.
             Value        Description
             0            The Overflow interrupt is disabled.
             1            The Overflow interrupt is enabled.




        © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1741
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.1.7 Interrupt Flag Status and Clear

            Name:       INTFLAG
            Offset:     0x0A
            Reset:      0x00
            Property:   -


      Bit         7            6            5             4            3            2             1            0
                                           MC1          MC0                                     ERR          OVF
   Access                                  R/W          R/W                                     R/W           R/W
    Reset                                   0             0                                       0            0


            Bit 5 – MC1 Match or Capture Channel x
            This flag is set on a comparison match, or when the corresponding CCx register contains a valid capture
            value. This flag is set on the next CLK_TC_CNT cycle, and will generate an interrupt request if the
            corresponding Match or Capture Channel x Interrupt Enable bit in the Interrupt Enable Set register
            (INTENSET.MCx) is '1'.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In capture operation, this flag is automatically cleared when CCx register is read.

            Bit 4 – MC0 Match or Capture Channel x
            This flag is set on a comparison match, or when the corresponding CCx register contains a valid capture
            value. This flag is set on the next CLK_TC_CNT cycle, and will generate an interrupt request if the
            corresponding Match or Capture Channel x Interrupt Enable bit in the Interrupt Enable Set register
            (INTENSET.MCx) is '1'.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In capture operation, this flag is automatically cleared when CCx register is read.

            Bit 1 – ERR Error Interrupt Flag
            This flag is set when a new capture occurs on a channel while the corresponding Match or Capture
            Channel x interrupt flag is set, in which case there is nowhere to store the new capture.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Error interrupt flag.

            Bit 0 – OVF Overflow Interrupt Flag
            This flag is set on the next CLK_TC_CNT cycle after an overflow condition occurs, and will generate an
            interrupt request if INTENCLR.OVF or INTENSET.OVF is '1'.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Overflow interrupt flag.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1742
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.1.8 Status

            Name:        STATUS
            Offset:      0x0B
            Reset:       0x01
            Property:    Read-Synchronized


      Bit         7             6             5            4             3             2             1             0
                                           CCBUFV1     CCBUFV0       PERBUFV                      SLAVE          STOP
   Access                                    R/W          R/W           R/W                          R            R
    Reset                                     0            0             0                           0             1


            Bits 4, 5 – CCBUFV Channel x Compare or Capture Buffer Valid
            For a compare channel x, the bit x is set when a new value is written to the corresponding CCBUFx
            register.
            The bit x is cleared by writing a '1' to it when CTRLB.LUPD is set, or it is cleared automatically by
            hardware on UPDATE condition.
            For a capture channel x, the bit x is set when a valid capture value is stored in the CCBUFx register. The
            bit x is cleared automatically when the CCx register is read.

            Bit 3 – PERBUFV Period Buffer Valid
            This bit is set when a new value is written to the PERBUF register. The bit is cleared by writing '1' to the
            corresponding location when CTRLB.LUPD is set, or automatically cleared by hardware on UPDATE
            condition. This bit is available only in 8-bit mode and will always read zero in 16- and 32-bit modes.

            Bit 1 – SLAVE Slave Status Flag
            This bit is only available in 32-bit mode on the slave TC (i.e., TC1 and/or TC3). The bit is set when the
            associated master TC (TC0 and TC2, respectively) is set to run in 32-bit mode.

            Bit 0 – STOP Stop Status Flag
            This bit is set when the TC is disabled, on a Stop command, or on an overflow/underflow condition when
            the One-Shot bit in the Control B Set register (CTRLBSET.ONESHOT) is '1'.
             Value        Description
             0            Counter is running.
             1            Counter is stopped.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1743
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.1.9 Waveform Generation Control

            Name:       WAVE
            Offset:     0x0C
            Reset:      0x00
            Property:   PAC Write-Protection, Enable-Protected


      Bit         7            6             5           4             3            2            1              0
                                                                                                  WAVEGEN[1:0]
  Access                                                                                        R/W            R/W
   Reset                                                                                         0              0


            Bits 1:0 – WAVEGEN[1:0] Waveform Generation Mode
            These bits select the waveform generation operation. They affect the top value, as shown in 48.6.2.6.1
            Waveform Output Operations. They also control whether frequency or PWM waveform generation should
            be used. The waveform generation operations are explained in 48.6.2.6.1 Waveform Output Operations.
            These bits are not synchronized.

            Value          Name            Operation             Top Value         Output              Output Waveform
                                                                                   Waveform            on Wraparound
                                                                                   on Match

            0x0            NFRQ            Normal frequency      PER1 / Max        Toggle              No action
            0x1            MFRQ            Match frequency       CC0               Toggle              No action
            0x2            NPWM            Normal PWM            PER1 / Max        Set                 Clear
            0x3            MPWM            Match PWM             CC0               Set                 Clear

            1) This depends on the TC mode: In 8-bit mode, the top value is the Period Value register (PER). In 16-
            and 32-bit mode it is the respective MAX value.




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1744
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.1.10 Driver Control

            Name:        DRVCTRL
            Offset:      0x0D
            Reset:       0x00
            Property:    PAC Write-Protection, Enable-Protected


      Bit         7             6            5             4             3             2             1           0
                                                                                                  INVEN1       INVEN0
   Access                                                                                          R/W          R/W
    Reset                                                                                            0           0


            Bits 0, 1 – INVENx Output Waveform x Invert Enable
            Bit x of INVEN[1:0] selects inversion of the output or capture trigger input of channel x.
            Value        Description
            0            Disable inversion of the WO[x] output and IO input pin.
            1            Enable inversion of the WO[x] output and IO input pin.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1745
                                                             SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.1.11 Debug Control

            Name:       DBGCTRL
            Offset:     0x0F
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6            5            4             3            2            1            0
                                                                                                           DBGRUN
   Access                                                                                                    R/W
    Reset                                                                                                     0


            Bit 0 – DBGRUN Run in Debug Mode
            This bit is not affected by a software Reset, and should not be changed by software while the TC is
            enabled.
             Value       Description
             0           The TC is halted when the device is halted in debug mode.
             1           The TC continues normal operation when the device is halted in debug mode.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1746
                                                              SAM D5x/E5x Family Data Sheet
                                                                                              TC – Timer/Counter

48.7.1.12 Synchronization Busy

            Name:       SYNCBUSY
            Offset:     0x10
            Reset:      0x00000000
            Property:   -


      Bit        31            30           29           28            27           26            25           24


   Access
    Reset


      Bit        23            22           21           20            19           18            17           16


   Access
    Reset


      Bit        15            14           13           12            11           10            9            8


   Access
    Reset


      Bit         7            6            5             4            3             2            1            0
                CC1           CC0                      COUNT        STATUS        CTRLB        ENABLE        SWRST
   Access         R            R                          R            R             R            R            R
    Reset         0            0                          0            0             0            0            0


            Bits 6, 7 – CCx Compare/Capture Channel x Synchronization Busy
            For details on CC channels number, refer to each TC feature list.
            This bit is set when the synchronization of CCx between clock domains is started.
            This bit is also set when the CCBUFx is written, and cleared on update condition. The bit is automatically
            cleared when the STATUS.CCBUFx bit is cleared.

            Bit 4 – COUNT COUNT Synchronization Busy
            This bit is cleared when the synchronization of COUNT between the clock domains is complete.
            This bit is set when the synchronization of COUNT between clock domains is started.

            Bit 3 – STATUS STATUS Synchronization Busy
            This bit is cleared when the synchronization of STATUS between the clock domains is complete.
            This bit is set when a '1' is written to the Capture Channel Buffer Valid status flags (STATUS.CCBUFVx)
            and the synchronization of STATUS between clock domains is started.

            Bit 2 – CTRLB CTRLB Synchronization Busy
            This bit is cleared when the synchronization of CTRLB between the clock domains is complete.
            This bit is set when the synchronization of CTRLB between clock domains is started.

            Bit 1 – ENABLE ENABLE Synchronization Busy
            This bit is cleared when the synchronization of ENABLE bit between the clock domains is complete.
            This bit is set when the synchronization of ENABLE bit between clock domains is started.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1747
                                                SAM D5x/E5x Family Data Sheet
                                                                               TC – Timer/Counter

Bit 0 – SWRST SWRST Synchronization Busy
This bit is cleared when the synchronization of SWRST bit between the clock domains is complete.
This bit is set when the synchronization of SWRST bit between clock domains is started.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 1748
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.1.13 Counter Value, 8-bit Mode

            Name:       COUNT
            Offset:     0x14
            Reset:      0x00
            Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized

            Note: Prior to any read access, this register must be synchronized by user by writing the according TC
            Command value to the Control B Set register (CTRLBSET.CMD=READSYNC).

      Bit         7            6            5               4                3     2            1            0
                                                                COUNT[7:0]
   Access       R/W           R/W          R/W          R/W              R/W     R/W          R/W          R/W
    Reset         0            0            0               0                0     0            0            0


            Bits 7:0 – COUNT[7:0] Counter Value
            These bits contain the current counter value.




        © 2019 Microchip Technology Inc.                           Datasheet                   DS60001507E-page 1749
                                                              SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.1.14 Period Value, 8-bit Mode

            Name:       PER
            Offset:     0x1B
            Reset:      0xFF
            Property:   Write-Synchronized


      Bit         7            6             5           4                3        2            1            0
                                                              PER[7:0]
   Access       R/W          R/W           R/W          R/W              R/W      R/W          R/W          R/W
    Reset         0            0             0           0                0        0            0            1


            Bits 7:0 – PER[7:0] Period Value
            These bits hold the value of the Period Buffer register PERBUF. The value is copied to PER register on
            UPDATE condition.




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1750
                                                            SAM D5x/E5x Family Data Sheet
                                                                                         TC – Timer/Counter

48.7.1.15 Channel x Compare/Capture Value, 8-bit Mode

            Name:       CCx
            Offset:     0x1C + x*0x01 [x=0..1]
            Reset:      0x00
            Property:   Write-Synchronized, Read-Synchronized


      Bit        7             6            5          4               3        2            1           0
                                                            CC[7:0]
   Access       R/W          R/W           R/W        R/W             R/W      R/W         R/W          R/W
    Reset        0             0            0          0               0        0            0           0


            Bits 7:0 – CC[7:0] Channel x Compare/Capture Value
            These bits contain the compare/capture value in 8-bit TC mode. In Match frequency (MFRQ) or Match
            PWM (MPWM) waveform operation (WAVE.WAVEGEN), the CC0 register is used as a period register.




        © 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1751
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.1.16 Period Buffer Value, 8-bit Mode

            Name:       PERBUF
            Offset:     0x2F
            Reset:      0xFF
            Property:   Write-Synchronized


      Bit         7            6             5           4                 3        2            1            0
                                                             PERBUF[7:0]
   Access       R/W           R/W          R/W          R/W            R/W        R/W          R/W           R/W
    Reset         0            0             0           0                 0        0            0            1


            Bits 7:0 – PERBUF[7:0] Period Buffer Value
            These bits hold the value of the period buffer register. The value is copied to PER register on UPDATE
            condition.




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1752
                                                              SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.1.17 Channel x Compare Buffer Value, 8-bit Mode

            Name:       CCBUFx
            Offset:     0x30 + x*0x01 [x=0..1]
            Reset:      0x00
            Property:   Write-Synchronized


      Bit         7            6            5            4                3        2            1            0
                                                             CCBUF[7:0]
   Access       R/W          R/W           R/W          R/W           R/W         R/W          R/W          R/W
    Reset         0            0            0            0                0        0            0            0


            Bits 7:0 – CCBUF[7:0] Channel x Compare Buffer Value
            These bits hold the value of the Channel x Compare Buffer Value. When the buffer valid flag is '1' and
            double buffering is enabled (CTRLBCLR.LUPD=1), the data from buffer registers will be copied into the
            corresponding CCx register under UPDATE condition (CTRLBSET.CMD=0x3), including the software
            update command.




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1753
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                     TC – Timer/Counter

48.7.2    Register Summary - 16-bit Mode

 Offset        Name        Bit Pos.

                              7:0     ONDEMAND RUNSTDBY      PRESCSYNC[1:0]              MODE[1:0]          ENABLE        SWRST
                             15:8      DMAOS                                         ALOCK               PRESCALER[2:0]
  0x00        CTRLA
                             23:16                         COPEN1     COPEN0                               CAPTEN1        CAPTEN0
                             31:24                                      CAPTMODE1[1:0]                        CAPTMODE0[1:0]
  0x04       CTRLBCLR         7:0               CMD[2:0]                                       ONESHOT       LUPD           DIR
  0x05       CTRLBSET         7:0               CMD[2:0]                                       ONESHOT       LUPD           DIR
                              7:0                           TCEI       TCINV                               EVACT[2:0]
  0x06        EVCTRL
                             15:8                          MCEO1      MCEO0                                               OVFEO
  0x08       INTENCLR         7:0                           MC1        MC0                                    ERR          OVF
  0x09       INTENSET         7:0                           MC1        MC0                                    ERR          OVF
  0x0A       INTFLAG          7:0                           MC1        MC0                                    ERR          OVF
  0x0B        STATUS          7:0                          CCBUFV1    CCBUFV0       PERBUFV                  SLAVE         STOP
  0x0C         WAVE           7:0                                                                              WAVEGEN[1:0]
  0x0D       DRVCTRL          7:0                                                                           INVEN1        INVEN0
  0x0E       Reserved
  0x0F       DBGCTRL          7:0                                                                                         DBGRUN
                              7:0       CC1       CC0                 COUNT          STATUS     CTRLB       ENABLE        SWRST
                             15:8
  0x10      SYNCBUSY
                             23:16
                             31:24
                              7:0                                         COUNT[7:0]
  0x14        COUNT
                             15:8                                         COUNT[15:8]
  0x16
   ...       Reserved
  0x1B
                              7:0                                              CC[7:0]
  0x1C          CC0
                             15:8                                             CC[15:8]
                              7:0                                              CC[7:0]
  0x1E          CC1
                             15:8                                             CC[15:8]
  0x20
   ...       Reserved
  0x2F
                              7:0                                         CCBUF[7:0]
  0x30        CCBUF0
                             15:8                                         CCBUF[15:8]
                              7:0                                         CCBUF[7:0]
  0x32        CCBUF1
                             15:8                                         CCBUF[15:8]




          © 2019 Microchip Technology Inc.                         Datasheet                              DS60001507E-page 1754
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.7.2.1 Control A

            Name:       CTRLA
            Offset:     0x00
            Reset:      0x00000000
            Property:   PAC Write-Protection, Write-Synchronized, Enable-Protected


      Bit        31           30             29          28          27                26          25           24
                                                         CAPTMODE1[1:0]                            CAPTMODE0[1:0]
   Access                                               R/W          R/W                          R/W           R/W
    Reset                                                0            0                            0             0


      Bit        23           22             21          20          19                18          17           16
                                           COPEN1     COPEN0                                   CAPTEN1        CAPTEN0
   Access                                   R/W         R/W                                       R/W           R/W
    Reset                                    0           0                                         0             0


      Bit        15           14             13          12          11                10          9             8
               DMAOS                                               ALOCK                     PRESCALER[2:0]
   Access       R/W                                                  R/W               R/W        R/W           R/W
    Reset         0                                                   0                 0          0             0


      Bit         7            6             5           4            3                 2          1             0
             ONDEMAND     RUNSTDBY           PRESCSYNC[1:0]                MODE[1:0]            ENABLE        SWRST
   Access       R/W          R/W            R/W         R/W          R/W               R/W        R/W           W
    Reset         0            0             0           0            0                 0          0             0


            Bits 28:27 – CAPTMODE1[1:0] Capture mode Channel 1
            These bits select the channel 1 capture mode.
             Value      Name                              Description
             0x0        DEFAULT                           Default capture
             0x1        CAPTMIN                           Minimum capture
             0x2        CAPTMAX                           Maximum capture
             0x3                                          Reserved

            Bits 25:24 – CAPTMODE0[1:0] Capture mode Channel 0
            These bits select the channel 0 capture mode.
             Value      Name                              Description
             0x0        DEFAULT                           Default capture
             0x1        CAPTMIN                           Minimum capture
             0x2        CAPTMAX                           Maximum capture
             0x3                                          Reserved

            Bits 20, 21 – COPENx Capture On Pin x Enable
            Bit x of COPEN[1:0] selects the trigger source for capture operation, either events or I/O pin input.
            Value       Description
            0           Event from Event System is selected as trigger source for capture operation on channel x.
            1           I/O pin is selected as trigger source for capture operation on channel x.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1755
                                                    SAM D5x/E5x Family Data Sheet
                                                                                    TC – Timer/Counter

Bits 16, 17 – CAPTENx Capture Channel x Enable
Bit x of CAPTEN[1:0] selects whether channel x is a capture or a compare channel.
These bits are not synchronized.
 Value      Description
 0          CAPTEN disables capture on channel x.
 1          CAPTEN enables capture on channel x.

Bit 15 – DMAOS DMA One-Shot Trigger Mode
This bit enables the DMA One-shot Trigger Mode.
Writing a '1' to this bit will generate a DMA trigger on TC cycle following a
TC_CTRLBSET_CMD_DMAOS command.
Writing a '0' to this bit will generate DMA triggers on each TC cycle.
This bit is not synchronized.

Bit 11 – ALOCK Auto Lock
When this bit is set, Lock bit update (LUPD) is set to '1' on each overflow/underflow or re-trigger event.
This bit is not synchronized.
 Value       Description
 0           The LUPD bit is not affected on overflow/underflow, and re-trigger event.
 1           The LUPD bit is set on each overflow/underflow or re-trigger event.

Bits 10:8 – PRESCALER[2:0] Prescaler
These bits select the counter prescaler factor.
These bits are not synchronized.
 Value      Name                     Description
 0x0        DIV1                     Prescaler: GCLK_TC
 0x1        DIV2                     Prescaler: GCLK_TC/2
 0x2        DIV4                     Prescaler: GCLK_TC/4
 0x3        DIV8                     Prescaler: GCLK_TC/8
 0x4        DIV16                    Prescaler: GCLK_TC/16
 0x5        DIV64                    Prescaler: GCLK_TC/64
 0x6        DIV256                   Prescaler: GCLK_TC/256
 0x7        DIV1024                  Prescaler: GCLK_TC/1024

Bit 7 – ONDEMAND Clock On Demand
This bit selects the clock requirements when the TC is stopped.
In standby mode, if the Run in Standby bit (CTRLA.RUNSTDBY) is '0', ONDEMAND is forced to '0'.
This bit is not synchronized.
 Value       Description
 0           The On Demand is disabled. If On Demand is disabled, the TC will continue to request the
             clock when its operation is stopped (STATUS.STOP=1).
 1           The On Demand is enabled. When On Demand is enabled, the stopped TC will not request
             the clock. The clock is requested when a software re-trigger command is applied or when an
             event with start/re-trigger action is detected.

Bit 6 – RUNSTDBY Run in Standby
This bit is used to keep the TC running in standby mode.
This bit is not synchronized.




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1756
                                                     SAM D5x/E5x Family Data Sheet
                                                                                       TC – Timer/Counter

 Value        Description
 0            The TC is halted in standby.
 1            The TC continues to run in standby.

Bits 5:4 – PRESCSYNC[1:0] Prescaler and Counter Synchronization
These bits select whether the counter should wrap around on the next GCLK_TCx clock or the next
prescaled GCLK_TCx clock. It also makes it possible to reset the prescaler.
These bits are not synchronized.
 Value      Name       Description
 0x0        GCLK       Reload or reset the counter on next generic clock
 0x1        PRESC      Reload or reset the counter on next prescaler clock
 0x2        RESYNC Reload or reset the counter on next generic clock. Reset the prescaler counter
 0x3        -          Reserved

Bits 3:2 – MODE[1:0] Timer Counter Mode
These bits select the counter mode.
These bits are not synchronized.
 Value      Name                      Description
 0x0        COUNT16                   Counter in 16-bit mode
 0x1        COUNT8                    Counter in 8-bit mode
 0x2        COUNT32                   Counter in 32-bit mode
 0x3        -                         Reserved

Bit 1 – ENABLE Enable
Due to synchronization, there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately, and the ENABLE
Synchronization Busy bit in the SYNCBUSY register (SYNCBUSY.ENABLE) will be set.
SYNCBUSY.ENABLE will be cleared when the operation is complete.
This bit is not enable protected.
 Value       Description
 0           The peripheral is disabled.
 1           The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the TC, except DBGCTRL, to their initial state, and the TC will
be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence; all other writes in the same write-operation
will be discarded.




© 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 1757
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.2.2 Control B Clear

            Name:        CTRLBCLR
            Offset:      0x04
            Reset:       0x00
            Property:    PAC Write-Protection, Read-Synchronized, Write-Synchronized

            This register allows the user to clear bits in the CTRLB register without doing a read-modify-write
            operation. Changes in this register will also be reflected in the Control B Set register (CTRLBSET).

      Bit         7             6             5              4             3               2       1               0
                             CMD[2:0]                                                ONESHOT     LUPD          DIR
   Access        R/W           R/W           R/W                                          R/W     R/W         R/W
    Reset         0             0             0                                            0       0               0


            Bits 7:5 – CMD[2:0] Command
            These bits are used for software control of the TC. The commands are executed on the next prescaled
            GCLK_TC clock cycle. When a command has been executed, the CMD bit group will be read back as
            zero.
            Writing 0x0 to these bits has no effect.
            Writing a '1' to any of these bits will clear the pending command.

            Bit 2 – ONESHOT One-Shot on Counter
            This bit controls one-shot operation of the TC.
            Writing a '0' to this bit has no effect
            Writing a '1' to this bit will disable one-shot operation.
             Value        Description
             0            The TC will wrap around and continue counting on an overflow/underflow condition.
             1            The TC will wrap around and stop on the next underflow/overflow condition.

            Bit 1 – LUPD Lock Update
            This bit controls the update operation of the TC buffered registers.
            When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
            on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
            hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
            can be unlocked.
            This bit has no effect when input capture operation is enabled.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the LUPD bit.
             Value        Description
             0            The CCBUFx and PERBUF buffer registers value are copied into CCx and PER registers on
                          hardware update condition.
             1            The CCBUFx and PERBUF buffer registers value are not copied into CCx and PER registers
                          on hardware update condition.

            Bit 0 – DIR Counter Direction
            This bit is used to change the direction of the counter.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the bit and make the counter count up.




        © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1758
                                                  SAM D5x/E5x Family Data Sheet
                                                                   TC – Timer/Counter

 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                   Datasheet         DS60001507E-page 1759
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.7.2.3 Control B Set

            Name:       CTRLBSET
            Offset:     0x05
            Reset:      0x00
            Property:   PAC Write-Protection, Read-synchronized, Write-Synchronized

            This register allows the user to set bits in the CTRLB register without doing a read-modify-write operation.
            Changes in this register will also be reflected in the Control B Clear register (CTRLBCLR).

      Bit         7            6             5            4             3            2             1            0
                            CMD[2:0]                                             ONESHOT         LUPD          DIR
   Access       R/W           R/W           R/W                                     R/W           R/W          R/W
    Reset         0            0             0                                       0             0            0


            Bits 7:5 – CMD[2:0] Command
            These bits are used for software control of the TC. The commands are executed on the next prescaled
            GCLK_TC clock cycle. When a command has been executed, the CMD bit group will be read back as
            zero.
            Writing 0x0 to these bits has no effect.
            Writing a value different from 0x0 to these bits will issue a command for execution.
             Value      Name                      Description
             0x0        NONE                      No action
             0x1        RETRIGGER                 Force a start, restart or retrigger
             0x2        STOP                      Force a stop
             0x3        UPDATE                    Force update of double buffered registers
             0x4        READSYNC                  Force a read synchronization of COUNT

            Bit 2 – ONESHOT One-Shot on Counter
            This bit controls one-shot operation of the TC.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will enable one-shot operation.
             Value        Description
             0            The TC will wrap around and continue counting on an overflow/underflow condition.
             1            The TC will wrap around and stop on the next underflow/overflow condition.

            Bit 1 – LUPD Lock Update
            This bit controls the update operation of the TC buffered registers.
            When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
            on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
            hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
            can be unlocked.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the LUPD bit.
            This bit has no effect when input capture operation is enabled.
             Value        Description
             0            The CCBUFx and PERBUF buffer registers value are copied into CCx and PER registers on
                          hardware update condition.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1760
                                                     SAM D5x/E5x Family Data Sheet
                                                                              TC – Timer/Counter

 Value        Description
 1            The CCBUFx and PERBUF buffer registers value are not copied into CCx and PER registers
              on hardware update condition.

Bit 0 – DIR Counter Direction
This bit is used to change the direction of the counter.
Writing a '0' to this bit has no effect
Writing a '1' to this bit will clear the bit and make the counter count up.
 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                      Datasheet                  DS60001507E-page 1761
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

48.7.2.4 Event Control

            Name:       EVCTRL
            Offset:     0x06
            Reset:      0x0000
            Property:   PAC Write-Protection, Enable-Protected


      Bit        15           14            13           12           11         10            9            8
                                           MCEO1       MCEO0                                             OVFEO
   Access                                   R/W         R/W                                               R/W
    Reset                                    0           0                                                  0


      Bit         7            6             5           4            3           2            1            0
                                           TCEI        TCINV                               EVACT[2:0]
   Access                                   R/W         R/W                      R/W          R/W         R/W
    Reset                                    0           0                        0            0            0


            Bit 13 – MCEO1 Match or Capture Channel x Event Output Enable [x = 1..0]
            These bits enable the generation of an event for every match or capture on channel x.
             Value      Description
             0          Match/Capture event on channel x is disabled and will not be generated.
             1          Match/Capture event on channel x is enabled and will be generated for every compare/
                        capture.

            Bit 12 – MCEO0 Match or Capture Channel x Event Output Enable [x = 1..0]
            These bits enable the generation of an event for every match or capture on channel x.
             Value      Description
             0          Match/Capture event on channel x is disabled and will not be generated.
             1          Match/Capture event on channel x is enabled and will be generated for every compare/
                        capture.

            Bit 8 – OVFEO Overflow/Underflow Event Output Enable
            This bit enables the Overflow/Underflow event. When enabled, an event will be generated when the
            counter overflows/underflows.
             Value      Description
             0          Overflow/Underflow event is disabled and will not be generated.
             1          Overflow/Underflow event is enabled and will be generated for every counter overflow/
                        underflow.

            Bit 5 – TCEI TC Event Enable
            This bit is used to enable asynchronous input events to the TC.
             Value       Description
             0            Incoming events are disabled.
             1            Incoming events are enabled.

            Bit 4 – TCINV TC Inverted Event Input Polarity
            This bit inverts the asynchronous input event source.
             Value       Description
             0           Input event source is not inverted.




        © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1762
                                                SAM D5x/E5x Family Data Sheet
                                                                                 TC – Timer/Counter

 Value        Description
 1            Input event source is inverted.

Bits 2:0 – EVACT[2:0] Event Action
These bits define the event action the TC will perform on an event.
 Value      Name                    Description
 0x0        OFF                     Event action disabled
 0x1        RETRIGGER               Start, restart or retrigger TC on event
 0x2        COUNT                   Count on event
 0x3        START                   Start TC on event
 0x4        STAMP                   Time stamp capture
 0x5        PPW                     Period captured in CC0, pulse width in CC1
 0x6        PWP                     Period captured in CC1, pulse width in CC0
 0x7        PW                      Pulse width capture




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1763
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                     TC – Timer/Counter

48.7.2.5 Interrupt Enable Clear

            Name:        INTENCLR
            Offset:      0x08
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

      Bit         7              6             5              4             3              2             1              0
                                              MC1           MC0                                         ERR            OVF
   Access                                     R/W           R/W                                         R/W            R/W
    Reset                                      0              0                                          0              0


            Bit 5 – MC1 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will clear the corresponding Match or Capture Channel x Interrupt Enable bit, which
            disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 4 – MC0 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will clear the corresponding Match or Capture Channel x Interrupt Enable bit, which
            disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 1 – ERR Error Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Error Interrupt Enable bit, which disables the Error interrupt.
            Value         Description
            0             The Error interrupt is disabled.
            1             The Error interrupt is enabled.

            Bit 0 – OVF Overflow Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Overflow Interrupt Enable bit, which disables the Overflow interrupt
            request.
             Value        Description
             0            The Overflow interrupt is disabled.
             1            The Overflow interrupt is enabled.




        © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1764
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                    TC – Timer/Counter

48.7.2.6 Interrupt Enable Set

            Name:        INTENSET
            Offset:      0x09
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

      Bit         7              6             5             4              3             2              1           0
                                              MC1           MC0                                        ERR          OVF
   Access                                     R/W           R/W                                        R/W          R/W
    Reset                                      0             0                                           0           0


            Bit 5 – MC1 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will set the corresponding Match or Capture Channel x Interrupt Enable bit, which
            enables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 4 – MC0 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will set the corresponding Match or Capture Channel x Interrupt Enable bit, which
            enables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 1 – ERR Error Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Error Interrupt Enable bit, which enables the Error interrupt.
            Value         Description
            0             The Error interrupt is disabled.
            1             The Error interrupt is enabled.

            Bit 0 – OVF Overflow Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Overflow Interrupt Enable bit, which enables the Overflow interrupt
            request.
             Value        Description
             0            The Overflow interrupt is disabled.
             1            The Overflow interrupt is enabled.




        © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1765
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.2.7 Interrupt Flag Status and Clear

            Name:       INTFLAG
            Offset:     0x0A
            Reset:      0x00
            Property:   -


      Bit         7            6            5             4            3            2             1            0
                                           MC1          MC0                                     ERR          OVF
   Access                                  R/W          R/W                                     R/W           R/W
    Reset                                   0             0                                       0            0


            Bit 5 – MC1 Match or Capture Channel x
            This flag is set on a comparison match, or when the corresponding CCx register contains a valid capture
            value. This flag is set on the next CLK_TC_CNT cycle, and will generate an interrupt request if the
            corresponding Match or Capture Channel x Interrupt Enable bit in the Interrupt Enable Set register
            (INTENSET.MCx) is '1'.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In capture operation, this flag is automatically cleared when CCx register is read.

            Bit 4 – MC0 Match or Capture Channel x
            This flag is set on a comparison match, or when the corresponding CCx register contains a valid capture
            value. This flag is set on the next CLK_TC_CNT cycle, and will generate an interrupt request if the
            corresponding Match or Capture Channel x Interrupt Enable bit in the Interrupt Enable Set register
            (INTENSET.MCx) is '1'.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In capture operation, this flag is automatically cleared when CCx register is read.

            Bit 1 – ERR Error Interrupt Flag
            This flag is set when a new capture occurs on a channel while the corresponding Match or Capture
            Channel x interrupt flag is set, in which case there is nowhere to store the new capture.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Error interrupt flag.

            Bit 0 – OVF Overflow Interrupt Flag
            This flag is set on the next CLK_TC_CNT cycle after an overflow condition occurs, and will generate an
            interrupt request if INTENCLR.OVF or INTENSET.OVF is '1'.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Overflow interrupt flag.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1766
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.2.8 Status

            Name:        STATUS
            Offset:      0x0B
            Reset:       0x01
            Property:    Read-Synchronized


      Bit         7             6             5            4             3             2             1             0
                                           CCBUFV1     CCBUFV0       PERBUFV                      SLAVE          STOP
   Access                                    R/W          R/W           R/W                          R            R
    Reset                                     0            0             0                           0             1


            Bits 4, 5 – CCBUFV Channel x Compare or Capture Buffer Valid
            For a compare channel x, the bit x is set when a new value is written to the corresponding CCBUFx
            register.
            The bit x is cleared by writing a '1' to it when CTRLB.LUPD is set, or it is cleared automatically by
            hardware on UPDATE condition.
            For a capture channel x, the bit x is set when a valid capture value is stored in the CCBUFx register. The
            bit x is cleared automatically when the CCx register is read.

            Bit 3 – PERBUFV Period Buffer Valid
            This bit is set when a new value is written to the PERBUF register. The bit is cleared by writing '1' to the
            corresponding location when CTRLB.LUPD is set, or automatically cleared by hardware on UPDATE
            condition. This bit is available only in 8-bit mode and will always read zero in 16- and 32-bit modes.

            Bit 1 – SLAVE Slave Status Flag
            This bit is only available in 32-bit mode on the slave TC (i.e., TC1 and/or TC3). The bit is set when the
            associated master TC (TC0 and TC2, respectively) is set to run in 32-bit mode.

            Bit 0 – STOP Stop Status Flag
            This bit is set when the TC is disabled, on a Stop command, or on an overflow/underflow condition when
            the One-Shot bit in the Control B Set register (CTRLBSET.ONESHOT) is '1'.
             Value        Description
             0            Counter is running.
             1            Counter is stopped.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1767
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.2.9 Waveform Generation Control

            Name:       WAVE
            Offset:     0x0C
            Reset:      0x00
            Property:   PAC Write-Protection, Enable-Protected


      Bit         7            6             5           4             3            2            1              0
                                                                                                  WAVEGEN[1:0]
  Access                                                                                        R/W            R/W
   Reset                                                                                         0              0


            Bits 1:0 – WAVEGEN[1:0] Waveform Generation Mode
            These bits select the waveform generation operation. They affect the top value, as shown in 48.6.2.6.1
            Waveform Output Operations. They also control whether frequency or PWM waveform generation should
            be used. The waveform generation operations are explained in 48.6.2.6.1 Waveform Output Operations.
            These bits are not synchronized.

            Value          Name            Operation             Top Value         Output              Output Waveform
                                                                                   Waveform            on Wraparound
                                                                                   on Match

            0x0            NFRQ            Normal frequency      PER1 / Max        Toggle              No action
            0x1            MFRQ            Match frequency       CC0               Toggle              No action
            0x2            NPWM            Normal PWM            PER1 / Max        Set                 Clear
            0x3            MPWM            Match PWM             CC0               Set                 Clear

            1) This depends on the TC mode: In 8-bit mode, the top value is the Period Value register (PER). In 16-
            and 32-bit mode it is the respective MAX value.




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1768
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.2.10 Driver Control

            Name:        DRVCTRL
            Offset:      0x0D
            Reset:       0x00
            Property:    PAC Write-Protection, Enable-Protected


      Bit         7             6            5             4             3             2             1           0
                                                                                                  INVEN1       INVEN0
   Access                                                                                          R/W          R/W
    Reset                                                                                            0           0


            Bits 0, 1 – INVENx Output Waveform x Invert Enable
            Bit x of INVEN[1:0] selects inversion of the output or capture trigger input of channel x.
            Value        Description
            0            Disable inversion of the WO[x] output and IO input pin.
            1            Enable inversion of the WO[x] output and IO input pin.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1769
                                                             SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.2.11 Debug Control

            Name:       DBGCTRL
            Offset:     0x0F
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6            5            4             3            2            1            0
                                                                                                           DBGRUN
   Access                                                                                                    R/W
    Reset                                                                                                     0


            Bit 0 – DBGRUN Run in Debug Mode
            This bit is not affected by a software Reset, and should not be changed by software while the TC is
            enabled.
             Value       Description
             0           The TC is halted when the device is halted in debug mode.
             1           The TC continues normal operation when the device is halted in debug mode.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1770
                                                              SAM D5x/E5x Family Data Sheet
                                                                                              TC – Timer/Counter

48.7.2.12 Synchronization Busy

            Name:       SYNCBUSY
            Offset:     0x10
            Reset:      0x00000000
            Property:   -


      Bit        31            30           29           28            27           26            25           24


   Access
    Reset


      Bit        23            22           21           20            19           18            17           16


   Access
    Reset


      Bit        15            14           13           12            11           10            9            8


   Access
    Reset


      Bit         7            6            5             4            3             2            1            0
                CC1           CC0                      COUNT        STATUS        CTRLB        ENABLE        SWRST
   Access         R            R                          R            R             R            R            R
    Reset         0            0                          0            0             0            0            0


            Bits 6, 7 – CCx Compare/Capture Channel x Synchronization Busy
            For details on CC channels number, refer to each TC feature list.
            This bit is set when the synchronization of CCx between clock domains is started.
            This bit is also set when the CCBUFx is written, and cleared on update condition. The bit is automatically
            cleared when the STATUS.CCBUFx bit is cleared.

            Bit 4 – COUNT COUNT Synchronization Busy
            This bit is cleared when the synchronization of COUNT between the clock domains is complete.
            This bit is set when the synchronization of COUNT between clock domains is started.

            Bit 3 – STATUS STATUS Synchronization Busy
            This bit is cleared when the synchronization of STATUS between the clock domains is complete.
            This bit is set when a '1' is written to the Capture Channel Buffer Valid status flags (STATUS.CCBUFVx)
            and the synchronization of STATUS between clock domains is started.

            Bit 2 – CTRLB CTRLB Synchronization Busy
            This bit is cleared when the synchronization of CTRLB between the clock domains is complete.
            This bit is set when the synchronization of CTRLB between clock domains is started.

            Bit 1 – ENABLE ENABLE Synchronization Busy
            This bit is cleared when the synchronization of ENABLE bit between the clock domains is complete.
            This bit is set when the synchronization of ENABLE bit between clock domains is started.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1771
                                                SAM D5x/E5x Family Data Sheet
                                                                               TC – Timer/Counter

Bit 0 – SWRST SWRST Synchronization Busy
This bit is cleared when the synchronization of SWRST bit between the clock domains is complete.
This bit is set when the synchronization of SWRST bit between clock domains is started.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 1772
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.2.13 Counter Value, 16-bit Mode

            Name:       COUNT
            Offset:     0x14
            Reset:      0x00
            Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized

            Note: Prior to any read access, this register must be synchronized by user by writing the according TC
            Command value to the Control B Set register (CTRLBSET.CMD=READSYNC).

      Bit        15           14            13              12                 11   10          9            8
                                                                 COUNT[15:8]
   Access       R/W           R/W          R/W          R/W                R/W      R/W       R/W          R/W
    Reset         0            0            0               0                  0     0          0            0


      Bit         7            6            5               4                  3     2          1            0
                                                                 COUNT[7:0]
   Access       R/W           R/W          R/W          R/W                R/W      R/W       R/W          R/W
    Reset         0            0            0               0                  0     0          0            0


            Bits 15:0 – COUNT[15:0] Counter Value
            These bits contain the current counter value.




        © 2019 Microchip Technology Inc.                            Datasheet                  DS60001507E-page 1773
                                                            SAM D5x/E5x Family Data Sheet
                                                                                         TC – Timer/Counter

48.7.2.14 Channel x Compare/Capture Value, 16-bit Mode

            Name:       CCx
            Offset:     0x1C + x*0x02 [x=0..1]
            Reset:      0x0000
            Property:   Write-Synchronized


      Bit        15           14           13          12              11       10           9           8
                                                            CC[15:8]
   Access       R/W          R/W           R/W        R/W              R/W     R/W         R/W          R/W
    Reset        0             0            0          0                0       0            0           0


      Bit        7             6            5          4                3       2            1           0
                                                            CC[7:0]
   Access       R/W          R/W           R/W        R/W              R/W     R/W         R/W          R/W
    Reset        0             0            0          0                0       0            0           0


            Bits 15:0 – CC[15:0] Channel x Compare/Capture Value
            These bits contain the compare/capture value in 16-bit TC mode. In Match frequency (MFRQ) or Match
            PWM (MPWM) waveform operation (WAVE.WAVEGEN), the CC0 register is used as a period register.




        © 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1774
                                                              SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.2.15 Channel x Compare Buffer Value, 16-bit Mode

            Name:       CCBUFx
            Offset:     0x30 + x*0x02 [x=0..1]
            Reset:      0x0000
            Property:   Write-Synchronized


      Bit        15           14           13           12                 11      10           9            8
                                                             CCBUF[15:8]
   Access       R/W          R/W           R/W          R/W            R/W        R/W          R/W          R/W
    Reset         0            0            0            0                 0       0            0            0


      Bit         7            6            5            4                 3       2            1            0
                                                             CCBUF[7:0]
   Access       R/W          R/W           R/W          R/W            R/W        R/W          R/W          R/W
    Reset         0            0            0            0                 0       0            0            0


            Bits 15:0 – CCBUF[15:0] Channel x Compare Buffer Value
            These bits hold the value of the Channel x Compare Buffer Value. When the buffer valid flag is '1' and
            double buffering is enabled (CTRLBCLR.LUPD=1), the data from buffer registers will be copied into the
            corresponding CCx register under UPDATE condition (CTRLBSET.CMD=0x3), including the software
            update command.




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1775
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                      TC – Timer/Counter

48.7.3    Register Summary - 32-bit Mode

 Offset        Name        Bit Pos.

                              7:0     ONDEMAND RUNSTDBY      PRESCSYNC[1:0]               MODE[1:0]          ENABLE        SWRST
                             15:8      DMAOS                                         ALOCK                PRESCALER[2:0]
  0x00        CTRLA
                             23:16                         COPEN1     COPEN0                                CAPTEN1        CAPTEN0
                             31:24                                      CAPTMODE1[1:0]                         CAPTMODE0[1:0]
  0x04       CTRLBCLR         7:0               CMD[2:0]                                        ONESHOT       LUPD           DIR
  0x05       CTRLBSET         7:0               CMD[2:0]                                        ONESHOT       LUPD           DIR
                              7:0                           TCEI       TCINV                                EVACT[2:0]
  0x06        EVCTRL
                             15:8                          MCEO1      MCEO0                                                OVFEO
  0x08       INTENCLR         7:0                           MC1        MC0                                     ERR          OVF
  0x09       INTENSET         7:0                           MC1        MC0                                     ERR          OVF
  0x0A       INTFLAG          7:0                           MC1        MC0                                     ERR          OVF
  0x0B        STATUS          7:0                          CCBUFV1    CCBUFV0       PERBUFV                   SLAVE         STOP
  0x0C         WAVE           7:0                                                                               WAVEGEN[1:0]
  0x0D       DRVCTRL          7:0                                                                            INVEN1        INVEN0
  0x0E       Reserved
  0x0F       DBGCTRL          7:0                                                                                          DBGRUN
                              7:0       CC1       CC0                 COUNT          STATUS      CTRLB       ENABLE        SWRST
                             15:8
  0x10      SYNCBUSY
                             23:16
                             31:24
                              7:0                                         COUNT[7:0]
                             15:8                                         COUNT[15:8]
  0x14        COUNT
                             23:16                                       COUNT[23:16]
                             31:24                                       COUNT[31:24]
  0x18
   ...       Reserved
  0x1B
                              7:0                                              CC[7:0]
                             15:8                                             CC[15:8]
  0x1C          CC0
                             23:16                                            CC[23:16]
                             31:24                                            CC[31:24]
                              7:0                                              CC[7:0]
                             15:8                                             CC[15:8]
  0x20          CC1
                             23:16                                            CC[23:16]
                             31:24                                            CC[31:24]
  0x24
   ...       Reserved
  0x2F
                              7:0                                         CCBUF[7:0]
                             15:8                                         CCBUF[15:8]
  0x30        CCBUF0
                             23:16                                       CCBUF[23:16]
                             31:24                                       CCBUF[31:24]




          © 2019 Microchip Technology Inc.                         Datasheet                               DS60001507E-page 1776
                                                 SAM D5x/E5x Family Data Sheet
                                                                      TC – Timer/Counter

...........continued

  Offset               Name     Bit Pos.

                                  7:0                   CCBUF[7:0]
                                 15:8                  CCBUF[15:8]
   0x34                CCBUF1
                                 23:16                 CCBUF[23:16]
                                 31:24                 CCBUF[31:24]




              © 2019 Microchip Technology Inc.   Datasheet              DS60001507E-page 1777
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.7.3.1 Control A

            Name:       CTRLA
            Offset:     0x00
            Reset:      0x00000000
            Property:   PAC Write-Protection, Write-Synchronized, Enable-Protected


      Bit        31           30             29          28          27                26          25           24
                                                         CAPTMODE1[1:0]                            CAPTMODE0[1:0]
   Access                                               R/W          R/W                          R/W           R/W
    Reset                                                0            0                            0             0


      Bit        23           22             21          20          19                18          17           16
                                           COPEN1     COPEN0                                   CAPTEN1        CAPTEN0
   Access                                   R/W         R/W                                       R/W           R/W
    Reset                                    0           0                                         0             0


      Bit        15           14             13          12          11                10          9             8
               DMAOS                                               ALOCK                     PRESCALER[2:0]
   Access       R/W                                                  R/W               R/W        R/W           R/W
    Reset         0                                                   0                 0          0             0


      Bit         7            6             5           4            3                 2          1             0
             ONDEMAND     RUNSTDBY           PRESCSYNC[1:0]                MODE[1:0]            ENABLE        SWRST
   Access       R/W          R/W            R/W         R/W          R/W               R/W        R/W           W
    Reset         0            0             0           0            0                 0          0             0


            Bits 28:27 – CAPTMODE1[1:0] Capture mode Channel 1
            These bits select the channel 1 capture mode.
             Value      Name                              Description
             0x0        DEFAULT                           Default capture
             0x1        CAPTMIN                           Minimum capture
             0x2        CAPTMAX                           Maximum capture
             0x3                                          Reserved

            Bits 25:24 – CAPTMODE0[1:0] Capture mode Channel 0
            These bits select the channel 0 capture mode.
             Value      Name                              Description
             0x0        DEFAULT                           Default capture
             0x1        CAPTMIN                           Minimum capture
             0x2        CAPTMAX                           Maximum capture
             0x3                                          Reserved

            Bits 20, 21 – COPENx Capture On Pin x Enable
            Bit x of COPEN[1:0] selects the trigger source for capture operation, either events or I/O pin input.
            Value       Description
            0           Event from Event System is selected as trigger source for capture operation on channel x.
            1           I/O pin is selected as trigger source for capture operation on channel x.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1778
                                                    SAM D5x/E5x Family Data Sheet
                                                                                    TC – Timer/Counter

Bits 16, 17 – CAPTENx Capture Channel x Enable
Bit x of CAPTEN[1:0] selects whether channel x is a capture or a compare channel.
These bits are not synchronized.
 Value      Description
 0          CAPTEN disables capture on channel x.
 1          CAPTEN enables capture on channel x.

Bit 15 – DMAOS DMA One-Shot Trigger Mode
This bit enables the DMA One-shot Trigger Mode.
Writing a '1' to this bit will generate a DMA trigger on TC cycle following a
TC_CTRLBSET_CMD_DMAOS command.
Writing a '0' to this bit will generate DMA triggers on each TC cycle.
This bit is not synchronized.

Bit 11 – ALOCK Auto Lock
When this bit is set, Lock bit update (LUPD) is set to '1' on each overflow/underflow or re-trigger event.
This bit is not synchronized.
 Value       Description
 0           The LUPD bit is not affected on overflow/underflow, and re-trigger event.
 1           The LUPD bit is set on each overflow/underflow or re-trigger event.

Bits 10:8 – PRESCALER[2:0] Prescaler
These bits select the counter prescaler factor.
These bits are not synchronized.
 Value      Name                     Description
 0x0        DIV1                     Prescaler: GCLK_TC
 0x1        DIV2                     Prescaler: GCLK_TC/2
 0x2        DIV4                     Prescaler: GCLK_TC/4
 0x3        DIV8                     Prescaler: GCLK_TC/8
 0x4        DIV16                    Prescaler: GCLK_TC/16
 0x5        DIV64                    Prescaler: GCLK_TC/64
 0x6        DIV256                   Prescaler: GCLK_TC/256
 0x7        DIV1024                  Prescaler: GCLK_TC/1024

Bit 7 – ONDEMAND Clock On Demand
This bit selects the clock requirements when the TC is stopped.
In standby mode, if the Run in Standby bit (CTRLA.RUNSTDBY) is '0', ONDEMAND is forced to '0'.
This bit is not synchronized.
 Value       Description
 0           The On Demand is disabled. If On Demand is disabled, the TC will continue to request the
             clock when its operation is stopped (STATUS.STOP=1).
 1           The On Demand is enabled. When On Demand is enabled, the stopped TC will not request
             the clock. The clock is requested when a software re-trigger command is applied or when an
             event with start/re-trigger action is detected.

Bit 6 – RUNSTDBY Run in Standby
This bit is used to keep the TC running in standby mode.
This bit is not synchronized.




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1779
                                                     SAM D5x/E5x Family Data Sheet
                                                                                       TC – Timer/Counter

 Value        Description
 0            The TC is halted in standby.
 1            The TC continues to run in standby.

Bits 5:4 – PRESCSYNC[1:0] Prescaler and Counter Synchronization
These bits select whether the counter should wrap around on the next GCLK_TCx clock or the next
prescaled GCLK_TCx clock. It also makes it possible to reset the prescaler.
These bits are not synchronized.
 Value      Name       Description
 0x0        GCLK       Reload or reset the counter on next generic clock
 0x1        PRESC      Reload or reset the counter on next prescaler clock
 0x2        RESYNC Reload or reset the counter on next generic clock. Reset the prescaler counter
 0x3        -          Reserved

Bits 3:2 – MODE[1:0] Timer Counter Mode
These bits select the counter mode.
These bits are not synchronized.
 Value      Name                      Description
 0x0        COUNT16                   Counter in 16-bit mode
 0x1        COUNT8                    Counter in 8-bit mode
 0x2        COUNT32                   Counter in 32-bit mode
 0x3        -                         Reserved

Bit 1 – ENABLE Enable
Due to synchronization, there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately, and the ENABLE
Synchronization Busy bit in the SYNCBUSY register (SYNCBUSY.ENABLE) will be set.
SYNCBUSY.ENABLE will be cleared when the operation is complete.
This bit is not enable protected.
 Value       Description
 0           The peripheral is disabled.
 1           The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the TC, except DBGCTRL, to their initial state, and the TC will
be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence; all other writes in the same write-operation
will be discarded.




© 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 1780
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.3.2 Control B Clear

            Name:        CTRLBCLR
            Offset:      0x04
            Reset:       0x00
            Property:    PAC Write-Protection, Read-Synchronized, Write-Synchronized

            This register allows the user to clear bits in the CTRLB register without doing a read-modify-write
            operation. Changes in this register will also be reflected in the Control B Set register (CTRLBSET).

      Bit         7             6             5              4             3               2       1               0
                             CMD[2:0]                                                ONESHOT     LUPD          DIR
   Access        R/W           R/W           R/W                                          R/W     R/W         R/W
    Reset         0             0             0                                            0       0               0


            Bits 7:5 – CMD[2:0] Command
            These bits are used for software control of the TC. The commands are executed on the next prescaled
            GCLK_TC clock cycle. When a command has been executed, the CMD bit group will be read back as
            zero.
            Writing 0x0 to these bits has no effect.
            Writing a '1' to any of these bits will clear the pending command.

            Bit 2 – ONESHOT One-Shot on Counter
            This bit controls one-shot operation of the TC.
            Writing a '0' to this bit has no effect
            Writing a '1' to this bit will disable one-shot operation.
             Value        Description
             0            The TC will wrap around and continue counting on an overflow/underflow condition.
             1            The TC will wrap around and stop on the next underflow/overflow condition.

            Bit 1 – LUPD Lock Update
            This bit controls the update operation of the TC buffered registers.
            When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
            on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
            hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
            can be unlocked.
            This bit has no effect when input capture operation is enabled.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the LUPD bit.
             Value        Description
             0            The CCBUFx and PERBUF buffer registers value are copied into CCx and PER registers on
                          hardware update condition.
             1            The CCBUFx and PERBUF buffer registers value are not copied into CCx and PER registers
                          on hardware update condition.

            Bit 0 – DIR Counter Direction
            This bit is used to change the direction of the counter.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the bit and make the counter count up.




        © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1781
                                                  SAM D5x/E5x Family Data Sheet
                                                                   TC – Timer/Counter

 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                   Datasheet         DS60001507E-page 1782
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               TC – Timer/Counter

48.7.3.3 Control B Set

            Name:       CTRLBSET
            Offset:     0x05
            Reset:      0x00
            Property:   PAC Write-Protection, Read-synchronized, Write-Synchronized

            This register allows the user to set bits in the CTRLB register without doing a read-modify-write operation.
            Changes in this register will also be reflected in the Control B Clear register (CTRLBCLR).

      Bit         7            6             5            4             3            2             1            0
                            CMD[2:0]                                             ONESHOT         LUPD          DIR
   Access       R/W           R/W           R/W                                     R/W           R/W          R/W
    Reset         0            0             0                                       0             0            0


            Bits 7:5 – CMD[2:0] Command
            These bits are used for software control of the TC. The commands are executed on the next prescaled
            GCLK_TC clock cycle. When a command has been executed, the CMD bit group will be read back as
            zero.
            Writing 0x0 to these bits has no effect.
            Writing a value different from 0x0 to these bits will issue a command for execution.
             Value      Name                      Description
             0x0        NONE                      No action
             0x1        RETRIGGER                 Force a start, restart or retrigger
             0x2        STOP                      Force a stop
             0x3        UPDATE                    Force update of double buffered registers
             0x4        READSYNC                  Force a read synchronization of COUNT

            Bit 2 – ONESHOT One-Shot on Counter
            This bit controls one-shot operation of the TC.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will enable one-shot operation.
             Value        Description
             0            The TC will wrap around and continue counting on an overflow/underflow condition.
             1            The TC will wrap around and stop on the next underflow/overflow condition.

            Bit 1 – LUPD Lock Update
            This bit controls the update operation of the TC buffered registers.
            When CTRLB.LUPD is set, no any update of the registers with value of its buffered register is performed
            on hardware UPDATE condition. Locking the update ensures that all buffer registers are valid before an
            hardware update is performed. After all the buffer registers are loaded correctly, the buffered registers
            can be unlocked.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the LUPD bit.
            This bit has no effect when input capture operation is enabled.
             Value        Description
             0            The CCBUFx and PERBUF buffer registers value are copied into CCx and PER registers on
                          hardware update condition.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1783
                                                     SAM D5x/E5x Family Data Sheet
                                                                              TC – Timer/Counter

 Value        Description
 1            The CCBUFx and PERBUF buffer registers value are not copied into CCx and PER registers
              on hardware update condition.

Bit 0 – DIR Counter Direction
This bit is used to change the direction of the counter.
Writing a '0' to this bit has no effect
Writing a '1' to this bit will clear the bit and make the counter count up.
 Value        Description
 0            The timer/counter is counting up (incrementing).
 1            The timer/counter is counting down (decrementing).




© 2019 Microchip Technology Inc.                      Datasheet                  DS60001507E-page 1784
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           TC – Timer/Counter

48.7.3.4 Event Control

            Name:       EVCTRL
            Offset:     0x06
            Reset:      0x0000
            Property:   PAC Write-Protection, Enable-Protected


      Bit        15           14            13           12           11         10            9            8
                                           MCEO1       MCEO0                                             OVFEO
   Access                                   R/W         R/W                                               R/W
    Reset                                    0           0                                                  0


      Bit         7            6             5           4            3           2            1            0
                                           TCEI        TCINV                               EVACT[2:0]
   Access                                   R/W         R/W                      R/W          R/W         R/W
    Reset                                    0           0                        0            0            0


            Bit 13 – MCEO1 Match or Capture Channel x Event Output Enable [x = 1..0]
            These bits enable the generation of an event for every match or capture on channel x.
             Value      Description
             0          Match/Capture event on channel x is disabled and will not be generated.
             1          Match/Capture event on channel x is enabled and will be generated for every compare/
                        capture.

            Bit 12 – MCEO0 Match or Capture Channel x Event Output Enable [x = 1..0]
            These bits enable the generation of an event for every match or capture on channel x.
             Value      Description
             0          Match/Capture event on channel x is disabled and will not be generated.
             1          Match/Capture event on channel x is enabled and will be generated for every compare/
                        capture.

            Bit 8 – OVFEO Overflow/Underflow Event Output Enable
            This bit enables the Overflow/Underflow event. When enabled, an event will be generated when the
            counter overflows/underflows.
             Value      Description
             0          Overflow/Underflow event is disabled and will not be generated.
             1          Overflow/Underflow event is enabled and will be generated for every counter overflow/
                        underflow.

            Bit 5 – TCEI TC Event Enable
            This bit is used to enable asynchronous input events to the TC.
             Value       Description
             0            Incoming events are disabled.
             1            Incoming events are enabled.

            Bit 4 – TCINV TC Inverted Event Input Polarity
            This bit inverts the asynchronous input event source.
             Value       Description
             0           Input event source is not inverted.




        © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1785
                                                SAM D5x/E5x Family Data Sheet
                                                                                 TC – Timer/Counter

 Value        Description
 1            Input event source is inverted.

Bits 2:0 – EVACT[2:0] Event Action
These bits define the event action the TC will perform on an event.
 Value      Name                    Description
 0x0        OFF                     Event action disabled
 0x1        RETRIGGER               Start, restart or retrigger TC on event
 0x2        COUNT                   Count on event
 0x3        START                   Start TC on event
 0x4        STAMP                   Time stamp capture
 0x5        PPW                     Period captured in CC0, pulse width in CC1
 0x6        PWP                     Period captured in CC1, pulse width in CC0
 0x7        PW                      Pulse width capture




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1786
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                     TC – Timer/Counter

48.7.3.5 Interrupt Enable Clear

            Name:        INTENCLR
            Offset:      0x08
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

      Bit         7              6             5              4             3              2             1              0
                                              MC1           MC0                                         ERR            OVF
   Access                                     R/W           R/W                                         R/W            R/W
    Reset                                      0              0                                          0              0


            Bit 5 – MC1 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will clear the corresponding Match or Capture Channel x Interrupt Enable bit, which
            disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 4 – MC0 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will clear the corresponding Match or Capture Channel x Interrupt Enable bit, which
            disables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 1 – ERR Error Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Error Interrupt Enable bit, which disables the Error interrupt.
            Value         Description
            0             The Error interrupt is disabled.
            1             The Error interrupt is enabled.

            Bit 0 – OVF Overflow Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Overflow Interrupt Enable bit, which disables the Overflow interrupt
            request.
             Value        Description
             0            The Overflow interrupt is disabled.
             1            The Overflow interrupt is enabled.




        © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1787
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                    TC – Timer/Counter

48.7.3.6 Interrupt Enable Set

            Name:        INTENSET
            Offset:      0x09
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

      Bit         7              6             5             4              3             2              1           0
                                              MC1           MC0                                        ERR          OVF
   Access                                     R/W           R/W                                        R/W          R/W
    Reset                                      0             0                                           0           0


            Bit 5 – MC1 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will set the corresponding Match or Capture Channel x Interrupt Enable bit, which
            enables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 4 – MC0 Match or Capture Channel x Interrupt Enable
            Writing a '0' to these bits has no effect.
            Writing a '1' to MCx will set the corresponding Match or Capture Channel x Interrupt Enable bit, which
            enables the Match or Capture Channel x interrupt.
             Value        Description
             0            The Match or Capture Channel x interrupt is disabled.
             1            The Match or Capture Channel x interrupt is enabled.

            Bit 1 – ERR Error Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Error Interrupt Enable bit, which enables the Error interrupt.
            Value         Description
            0             The Error interrupt is disabled.
            1             The Error interrupt is enabled.

            Bit 0 – OVF Overflow Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Overflow Interrupt Enable bit, which enables the Overflow interrupt
            request.
             Value        Description
             0            The Overflow interrupt is disabled.
             1            The Overflow interrupt is enabled.




        © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1788
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.3.7 Interrupt Flag Status and Clear

            Name:       INTFLAG
            Offset:     0x0A
            Reset:      0x00
            Property:   -


      Bit         7            6            5             4            3            2             1            0
                                           MC1          MC0                                     ERR          OVF
   Access                                  R/W          R/W                                     R/W           R/W
    Reset                                   0             0                                       0            0


            Bit 5 – MC1 Match or Capture Channel x
            This flag is set on a comparison match, or when the corresponding CCx register contains a valid capture
            value. This flag is set on the next CLK_TC_CNT cycle, and will generate an interrupt request if the
            corresponding Match or Capture Channel x Interrupt Enable bit in the Interrupt Enable Set register
            (INTENSET.MCx) is '1'.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In capture operation, this flag is automatically cleared when CCx register is read.

            Bit 4 – MC0 Match or Capture Channel x
            This flag is set on a comparison match, or when the corresponding CCx register contains a valid capture
            value. This flag is set on the next CLK_TC_CNT cycle, and will generate an interrupt request if the
            corresponding Match or Capture Channel x Interrupt Enable bit in the Interrupt Enable Set register
            (INTENSET.MCx) is '1'.
            Writing a '0' to one of these bits has no effect.
            Writing a '1' to one of these bits will clear the corresponding Match or Capture Channel x interrupt flag
            In capture operation, this flag is automatically cleared when CCx register is read.

            Bit 1 – ERR Error Interrupt Flag
            This flag is set when a new capture occurs on a channel while the corresponding Match or Capture
            Channel x interrupt flag is set, in which case there is nowhere to store the new capture.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Error interrupt flag.

            Bit 0 – OVF Overflow Interrupt Flag
            This flag is set on the next CLK_TC_CNT cycle after an overflow condition occurs, and will generate an
            interrupt request if INTENCLR.OVF or INTENSET.OVF is '1'.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Overflow interrupt flag.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1789
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.3.8 Status

            Name:        STATUS
            Offset:      0x0B
            Reset:       0x01
            Property:    Read-Synchronized


      Bit         7             6             5            4             3             2             1             0
                                           CCBUFV1     CCBUFV0       PERBUFV                      SLAVE          STOP
   Access                                    R/W          R/W           R/W                          R            R
    Reset                                     0            0             0                           0             1


            Bits 4, 5 – CCBUFV Channel x Compare or Capture Buffer Valid
            For a compare channel x, the bit x is set when a new value is written to the corresponding CCBUFx
            register.
            The bit x is cleared by writing a '1' to it when CTRLB.LUPD is set, or it is cleared automatically by
            hardware on UPDATE condition.
            For a capture channel x, the bit x is set when a valid capture value is stored in the CCBUFx register. The
            bit x is cleared automatically when the CCx register is read.

            Bit 3 – PERBUFV Period Buffer Valid
            This bit is set when a new value is written to the PERBUF register. The bit is cleared by writing '1' to the
            corresponding location when CTRLB.LUPD is set, or automatically cleared by hardware on UPDATE
            condition. This bit is available only in 8-bit mode and will always read zero in 16- and 32-bit modes.

            Bit 1 – SLAVE Slave Status Flag
            This bit is only available in 32-bit mode on the slave TC (i.e., TC1 and/or TC3). The bit is set when the
            associated master TC (TC0 and TC2, respectively) is set to run in 32-bit mode.

            Bit 0 – STOP Stop Status Flag
            This bit is set when the TC is disabled, on a Stop command, or on an overflow/underflow condition when
            the One-Shot bit in the Control B Set register (CTRLBSET.ONESHOT) is '1'.
             Value        Description
             0            Counter is running.
             1            Counter is stopped.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1790
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.3.9 Waveform Generation Control

            Name:       WAVE
            Offset:     0x0C
            Reset:      0x00
            Property:   PAC Write-Protection, Enable-Protected


      Bit         7            6             5           4             3            2            1              0
                                                                                                  WAVEGEN[1:0]
  Access                                                                                        R/W            R/W
   Reset                                                                                         0              0


            Bits 1:0 – WAVEGEN[1:0] Waveform Generation Mode
            These bits select the waveform generation operation. They affect the top value, as shown in 48.6.2.6.1
            Waveform Output Operations. They also control whether frequency or PWM waveform generation should
            be used. The waveform generation operations are explained in 48.6.2.6.1 Waveform Output Operations.
            These bits are not synchronized.

            Value          Name            Operation             Top Value         Output              Output Waveform
                                                                                   Waveform            on Wraparound
                                                                                   on Match

            0x0            NFRQ            Normal frequency      PER1 / Max        Toggle              No action
            0x1            MFRQ            Match frequency       CC0               Toggle              No action
            0x2            NPWM            Normal PWM            PER1 / Max        Set                 Clear
            0x3            MPWM            Match PWM             CC0               Set                 Clear

            1) This depends on the TC mode: In 8-bit mode, the top value is the Period Value register (PER). In 16-
            and 32-bit mode it is the respective MAX value.




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1791
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                TC – Timer/Counter

48.7.3.10 Driver Control

            Name:        DRVCTRL
            Offset:      0x0D
            Reset:       0x00
            Property:    PAC Write-Protection, Enable-Protected


      Bit         7             6            5             4             3             2             1           0
                                                                                                  INVEN1       INVEN0
   Access                                                                                          R/W          R/W
    Reset                                                                                            0           0


            Bits 0, 1 – INVENx Output Waveform x Invert Enable
            Bit x of INVEN[1:0] selects inversion of the output or capture trigger input of channel x.
            Value        Description
            0            Disable inversion of the WO[x] output and IO input pin.
            1            Enable inversion of the WO[x] output and IO input pin.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1792
                                                             SAM D5x/E5x Family Data Sheet
                                                                                             TC – Timer/Counter

48.7.3.11 Debug Control

            Name:       DBGCTRL
            Offset:     0x0F
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6            5            4             3            2            1            0
                                                                                                           DBGRUN
   Access                                                                                                    R/W
    Reset                                                                                                     0


            Bit 0 – DBGRUN Run in Debug Mode
            This bit is not affected by a software Reset, and should not be changed by software while the TC is
            enabled.
             Value       Description
             0           The TC is halted when the device is halted in debug mode.
             1           The TC continues normal operation when the device is halted in debug mode.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1793
                                                              SAM D5x/E5x Family Data Sheet
                                                                                              TC – Timer/Counter

48.7.3.12 Synchronization Busy

            Name:       SYNCBUSY
            Offset:     0x10
            Reset:      0x00000000
            Property:   -


      Bit        31            30           29           28            27           26            25           24


   Access
    Reset


      Bit        23            22           21           20            19           18            17           16


   Access
    Reset


      Bit        15            14           13           12            11           10            9            8


   Access
    Reset


      Bit         7            6            5             4            3             2            1            0
                CC1           CC0                      COUNT        STATUS        CTRLB        ENABLE        SWRST
   Access         R            R                          R            R             R            R            R
    Reset         0            0                          0            0             0            0            0


            Bits 6, 7 – CCx Compare/Capture Channel x Synchronization Busy
            For details on CC channels number, refer to each TC feature list.
            This bit is set when the synchronization of CCx between clock domains is started.
            This bit is also set when the CCBUFx is written, and cleared on update condition. The bit is automatically
            cleared when the STATUS.CCBUFx bit is cleared.

            Bit 4 – COUNT COUNT Synchronization Busy
            This bit is cleared when the synchronization of COUNT between the clock domains is complete.
            This bit is set when the synchronization of COUNT between clock domains is started.

            Bit 3 – STATUS STATUS Synchronization Busy
            This bit is cleared when the synchronization of STATUS between the clock domains is complete.
            This bit is set when a '1' is written to the Capture Channel Buffer Valid status flags (STATUS.CCBUFVx)
            and the synchronization of STATUS between clock domains is started.

            Bit 2 – CTRLB CTRLB Synchronization Busy
            This bit is cleared when the synchronization of CTRLB between the clock domains is complete.
            This bit is set when the synchronization of CTRLB between clock domains is started.

            Bit 1 – ENABLE ENABLE Synchronization Busy
            This bit is cleared when the synchronization of ENABLE bit between the clock domains is complete.
            This bit is set when the synchronization of ENABLE bit between clock domains is started.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1794
                                                SAM D5x/E5x Family Data Sheet
                                                                               TC – Timer/Counter

Bit 0 – SWRST SWRST Synchronization Busy
This bit is cleared when the synchronization of SWRST bit between the clock domains is complete.
This bit is set when the synchronization of SWRST bit between clock domains is started.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 1795
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.3.13 Counter Value, 32-bit Mode

            Name:       COUNT
            Offset:     0x14
            Reset:      0x00
            Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized

            Note: Prior to any read access, this register must be synchronized by user by writing the according TC
            Command value to the Control B Set register (CTRLBSET.CMD=READSYNC).

      Bit        31           30            29              28                 27   26         25           24
                                                                COUNT[31:24]
   Access       R/W           R/W          R/W          R/W                R/W      R/W       R/W          R/W
    Reset         0            0            0               0                  0     0          0            0


      Bit        23           22            21              20                 19   18         17           16
                                                                COUNT[23:16]
   Access       R/W           R/W          R/W          R/W                R/W      R/W       R/W          R/W
    Reset         0            0            0               0                  0     0          0            0


      Bit        15           14            13              12                 11   10          9            8
                                                                 COUNT[15:8]
   Access       R/W           R/W          R/W          R/W                R/W      R/W       R/W          R/W
    Reset         0            0            0               0                  0     0          0            0


      Bit         7            6            5               4                  3     2          1            0
                                                                 COUNT[7:0]
   Access       R/W           R/W          R/W          R/W                R/W      R/W       R/W          R/W
    Reset         0            0            0               0                  0     0          0            0


            Bits 31:0 – COUNT[31:0] Counter Value
            These bits contain the current counter value.




        © 2019 Microchip Technology Inc.                            Datasheet                  DS60001507E-page 1796
                                                            SAM D5x/E5x Family Data Sheet
                                                                                         TC – Timer/Counter

48.7.3.14 Channel x Compare/Capture Value, 32-bit Mode

            Name:       CCx
            Offset:     0x1C + x*0x04 [x=0..1]
            Reset:      0x00000000
            Property:   Write-Synchronized


      Bit        31           30           29          28               27      26          25           24
                                                            CC[31:24]
   Access       R/W          R/W           R/W        R/W               R/W    R/W         R/W          R/W
    Reset        0             0            0          0                 0      0            0           0


      Bit        23           22           21          20               19      18          17           16
                                                            CC[23:16]
   Access       R/W          R/W           R/W        R/W               R/W    R/W         R/W          R/W
    Reset        0             0            0          0                 0      0            0           0


      Bit        15           14           13          12               11      10           9           8
                                                            CC[15:8]
   Access       R/W          R/W           R/W        R/W               R/W    R/W         R/W          R/W
    Reset        0             0            0          0                 0      0            0           0


      Bit        7             6            5          4                 3      2            1           0
                                                             CC[7:0]
   Access       R/W          R/W           R/W        R/W               R/W    R/W         R/W          R/W
    Reset        0             0            0          0                 0      0            0           0


            Bits 31:0 – CC[31:0] Channel x Compare/Capture Value
            These bits contain the compare/capture value in 32-bit TC mode. In Match frequency (MFRQ) or Match
            PWM (MPWM) waveform operation (WAVE.WAVEGEN), the CC0 register is used as a period register.




        © 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1797
                                                               SAM D5x/E5x Family Data Sheet
                                                                                            TC – Timer/Counter

48.7.3.15 Channel x Compare Buffer Value, 32-bit Mode

            Name:       CCBUFx
            Offset:     0x30 + x*0x04 [x=0..1]
            Reset:      0x00000000
            Property:   Write-Synchronized


      Bit        31           30           29           28                 27      26           25           24
                                                             CCBUF[31:24]
   Access       R/W          R/W           R/W          R/W            R/W        R/W          R/W          R/W
    Reset         0            0            0            0                  0      0            0            0


      Bit        23           22           21           20                 19      18           17           16
                                                             CCBUF[23:16]
   Access       R/W          R/W           R/W          R/W            R/W        R/W          R/W          R/W
    Reset         0            0            0            0                  0      0            0            0


      Bit        15           14           13           12                 11      10           9            8
                                                             CCBUF[15:8]
   Access       R/W          R/W           R/W          R/W            R/W        R/W          R/W          R/W
    Reset         0            0            0            0                  0      0            0            0


      Bit         7            6            5            4                  3      2            1            0
                                                              CCBUF[7:0]
   Access       R/W          R/W           R/W          R/W            R/W        R/W          R/W          R/W
    Reset         0            0            0            0                  0      0            0            0


            Bits 31:0 – CCBUF[31:0] Channel x Compare Buffer Value
            These bits hold the value of the Channel x Compare Buffer Value. When the buffer valid flag is '1' and
            double buffering is enabled (CTRLBCLR.LUPD=1), the data from buffer registers will be copied into the
            corresponding CCx register under UPDATE condition (CTRLBSET.CMD=0x3), including the software
            update command.




        © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1798
