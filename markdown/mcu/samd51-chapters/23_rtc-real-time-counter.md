# 21. RTC – Real-Time Counter

*Source: `Atmel-SAMD51.pdf`, pages 283-373 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                   RTC – Real-Time Counter


21.    RTC – Real-Time Counter

21.1   Overview
       The Real-Time Counter (RTC) is a 32-bit counter with a 10-bit programmable prescaler that typically runs
       continuously to keep track of time. The RTC can wake up the device from sleep modes using the alarm/
       compare wake up, periodic wake up, or overflow wake up mechanisms, or from the wake inputs.
       The RTC can generate periodic peripheral events from outputs of the prescaler, as well as alarm/compare
       interrupts and peripheral events, which can trigger at any counter value. Additionally, the timer can trigger
       an overflow interrupt and peripheral event, and can be reset on the occurrence of an alarm/compare
       match. This allows periodic interrupts and peripheral events at very long and accurate intervals.
       The 10-bit programmable prescaler can scale down the clock source. By this, a wide range of resolutions
       and time-out periods can be configured. With a 32.768kHz clock source, the minimum counter tick
       interval is 30.5µs, and time-out periods can range up to 36 hours. For a counter tick interval of 1s, the
       maximum time-out period is more than 136 years.



21.2   Features
         •   32-bit counter with 10-bit prescaler
         •   Multiple clock sources
         •   32-bit or 16-bit counter mode
         •   Two 32-bit or four 16-bit compare values
         •   Clock/Calendar mode
               – Time in seconds, minutes, and hours (12/24)
               – Date in day of month, month, and year
               – Leap year correction
         •   Digital prescaler correction/tuning for increased accuracy
         •   Overflow, alarm/compare match and prescaler interrupts and events
               – Optional clear on alarm/compare match
         •   8 backup registers with retention capability
         •   Tamper Detection
               – Timestamp on event or up to 5 inputs with debouncing
               – Active layer protection




       © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 283
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter


21.3   Block Diagram
       Figure 21-1. RTC Block Diagram (Mode 0 — 32-Bit Counter)
                                                                                 0x00000000
                                                                                                       MATCHCLR



                                CLK_RTC_OSC                       CLK_RTC_CNT
                 OSC32KCTRL                   PRESCALER                            COUNT                    OVF



                                               Periodic Events
                                                                                                 =          CMPn



                                                                                  COMPn

       Figure 21-2. RTC Block Diagram (Mode 1 — 16-Bit Counter)
                                                                                   0x0000



                                CLK_RTC_OSC                      CLK_RTC_CNT
                 OSC32KCTRL                   PRESCALER                           COUNT



                                                                                                 =         OVF
                                               Periodic Events          PER

                                                                                                 =         CMPn



                                                                                  COMPn


       Figure 21-3. RTC Block Diagram (Mode 2 — Clock/Calendar)
                                                                                0x00000000
                                                                                                       MATCHCLR



                               CLK_RTC_OSC                       CLK_RTC_CNT
                OSC32KCTRL                    PRESCALER                          CLOCK                     OVF



                                                                       MASKn                    =         ALARMn
                                               Periodic Events


                                                                                 ALARMn

       Related Links
       21.6.2.3 32-Bit Counter (Mode 0)
       21.6.2.4 16-Bit Counter (Mode 1)
       21.6.2.5 Clock/Calendar (Mode 2)
       21.6.8.5 Tamper Detection




       © 2019 Microchip Technology Inc.                           Datasheet                          DS60001507E-page 284
                                                           SAM D5x/E5x Family Data Sheet
                                                                                    RTC – Real-Time Counter


21.4     Signal Description
         Table 21-1. Signal Description

          Signal                             Description                         Type
          INn [n=0..4]                       Tamper Detection Input              Digital input
          OUT                                Tamper Detection Output             Digital output

         One signal can be mapped to one of several pins.
         Related Links
         6. I/O Multiplexing and Considerations



21.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

21.5.1   I/O Lines
         For more information on I/O configurations, refer to the "RTC Pinout" section.
         Related Links: I/O Multiplexing and Considerations

21.5.2   Power Management
         The RTC will continue to operate in any sleep mode where the selected source clock is running. The RTC
         interrupts can be used to wake up the device from sleep modes. Events connected to the event system
         can trigger other operations in the system without exiting sleep modes. Refer to the Power Manager for
         details on the different sleep modes.
         The RTC will be reset only at power-on (POR) or by setting the Software Reset bit in the Control A
         register (CTRLA.SWRST=1).
         Related Links
         18. PM – Power Manager

21.5.3   Clocks
         The RTC bus clock (CLK_RTC_APB) can be enabled and disabled in the Main Clock module MCLK, and
         the default state of CLK_RTC_APB can be found in Peripheral Clock Masking section.
         A 32KHz or 1KHz oscillator clock (CLK_RTC_OSC) is required to clock the RTC. This clock must be
         configured and enabled in the 32KHz oscillator controller (OSC32KCTRL) before using the RTC.
         This oscillator clock is asynchronous to the bus clock (CLK_RTC_APB). Due to this asynchronicity,
         writing to certain registers will require synchronization between the clock domains. Refer to 21.6.7
         Synchronization for further details.
         Related Links
         29. OSC32KCTRL – 32KHz Oscillators Controller
         15.6.2.6 Peripheral Clock Masking

21.5.4   DMA
         The DMA request lines (or line if only one request) are connected to the DMA Controller (DMAC). Using
         the RTC DMA requests requires the DMA Controller to be configured first.




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 285
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

         Related Links
         22. DMAC – Direct Memory Access Controller

21.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. Using the RTC interrupt requires the
         Interrupt Controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

21.5.6   Events
         The events are connected to the Event System.
         Related Links
         31. EVSYS – Event System

21.5.7   Debug Operation
         When the CPU is halted in debug mode the RTC will halt normal operation. The RTC can be forced to
         continue operation during debugging. Refer to 21.8.7 DBGCTRL for details.

21.5.8   Register Access Protection
         All registers with write-access are optionally write-protected by the peripheral access controller (PAC),
         except the following registers:
           • Interrupt Flag Status and Clear (INTFLAG) register

         Write-protection is denoted by the "PAC Write-Protection" property in the register description.
         Write-protection does not apply to accesses through an external debugger. Refer to the PAC - Peripheral
         Access Controller for details.
         Related Links
         27. PAC - Peripheral Access Controller

21.5.9   Analog Connections
         A 32.768kHz crystal can be connected to the XIN32 and XOUT32 pins, along with any required load
         capacitors. See the Electrical Characteristics Chapters for details on recommended crystal characteristics
         and load capacitors.



21.6     Functional Description

21.6.1   Principle of Operation
         The RTC keeps track of time in the system and enables periodic events, as well as interrupts and events
         at a specified time. The RTC consists of a 10-bit prescaler that feeds a 32-bit counter. The actual format
         of the 32-bit counter depends on the RTC operating mode.
         The RTC can function in one of these modes:
          • Mode 0 - COUNT32: RTC serves as 32-bit counter
          • Mode 1 - COUNT16: RTC serves as 16-bit counter
          • Mode 2 - CLOCK: RTC serves as clock/calendar with alarm functionality




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 286
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.6.2    Basic Operation

21.6.2.1 Initialization
          The following bits are enable-protected, meaning that they can only be written when the RTC is disabled
          (CTRLA.ENABLE=0):
           •   Operating Mode bits in the Control A register (CTRLA.MODE)
           •   Prescaler bits in the Control A register (CTRLA.PRESCALER)
           •   Clear on Match bit in the Control A register (CTRLA.MATCHCLR)
           •   Clock Representation bit in the Control A register (CTRLA.CLKREP)
          The following registers are enable-protected:
           • Control B register (CTRLB)
           • Event Control register (EVCTRL)
           • Tamper Control register (TAMPCTRL)
          Enable-protected bits and registers can be changed only when the RTC is disabled (CTRLA.ENABLE=0).
          If the RTC is enabled (CTRLA.ENABLE=1), these operations are necessary: first write
          CTRLA.ENABLE=0 and check whether the write synchronization has finished, then change the desired
          bit field value. Enable-protected bits in CTRLA register can be written at the same time as
          CTRLA.ENABLE is written to '1', but not at the same time as CTRLA.ENABLE is written to '0'.
          Enable-protection is denoted by the "Enable-Protected" property in the register description.
          The RTC prescaler divides the source clock for the RTC counter.
          Note: In Clock/Calendar mode, the prescaler must be configured to provide a 1Hz clock to the counter
          for correct operation.
          The frequency of the RTC clock (CLK_RTC_CNT) is given by the following formula:
                           �CLK_RTC_OSC
          �CLK_RTC_CNT =
                            2PRESCALER
          The frequency of the oscillator clock, CLK_RTC_OSC, is given by fCLK_RTC_OSC, and fCLK_RTC_CNT is the
          frequency of the internal prescaled RTC clock, CLK_RTC_CNT.
21.6.2.2 Enabling, Disabling, and Resetting
          The RTC is enabled by setting the Enable bit in the Control A register (CTRLA.ENABLE=1). The RTC is
          disabled by writing CTRLA.ENABLE=0.
          The RTC is reset by setting the Software Reset bit in the Control A register (CTRLA.SWRST=1). All
          registers in the RTC, except DEBUG, will be reset to their initial state, and the RTC will be disabled. The
          RTC must be disabled before resetting it.
21.6.2.3 32-Bit Counter (Mode 0)
          When the RTC Operating Mode bits in the Control A register (CTRLA.MODE) are written to 0x0, the
          counter operates in 32-bit Counter mode. The block diagram of this mode is shown in Figure 21-1. When
          the RTC is enabled, the counter will increment on every 0-to-1 transition of CLK_RTC_CNT. The counter
          will increment until it reaches the top value of 0xFFFFFFFF, and then wrap to 0x00000000. This sets the
          Overflow Interrupt flag in the Interrupt Flag Status and Clear register (INTFLAG.OVF).
          The RTC counter value can be read from or written to the Counter Value register (COUNT) in 32-bit
          format.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 287
                                                          SAM D5x/E5x Family Data Sheet
                                                                                   RTC – Real-Time Counter

         The counter value is continuously compared with the 32-bit Compare registers (COMPn, n=0–1). When a
         compare match occurs, the Compare n Interrupt flag in the Interrupt Flag Status and Clear register
         (INTFLAG.CMPn) is set on the next 0-to-1 transition of CLK_RTC_CNT.
         If the Clear on Match bit in the Control A register (CTRLA.MATCHCLR) is '1', the counter is cleared on
         the next counter cycle when a compare match with COMPn occurs. This allows the RTC to generate
         periodic interrupts or events with longer periods than the prescaler events. Note that when
         CTRLA.MATCHCLR is '1', INTFLAG.CMPn and INTFLAG.OVF will both be set simultaneously on a
         compare match with COMPn.

21.6.2.4 16-Bit Counter (Mode 1)
         When the RTC Operating Mode bits in the Control A register (CTRLA.MODE) are written to 0x1, the
         counter operates in 16-bit Counter mode as shown in Figure 21-2. When the RTC is enabled, the counter
         will increment on every 0-to-1 transition of CLK_RTC_CNT. In 16-bit Counter mode, the 16-bit Period
         register (PER) holds the maximum value of the counter. The counter will increment until it reaches the
         PER value, and then wrap to 0x0000. This sets the Overflow Interrupt flag in the Interrupt Flag Status and
         Clear register (INTFLAG.OVF).
         The RTC counter value can be read from or written to the Counter Value register (COUNT) in 16-bit
         format.
         The counter value is continuously compared with the 16-bit Compare registers (COMPn, n=0..). When a
         compare match occurs, the Compare n Interrupt flag in the Interrupt Flag Status and Clear register
         (INTFLAG.CMPn, n=0..) is set on the next 0-to-1 transition of CLK_RTC_CNT.

21.6.2.5 Clock/Calendar (Mode 2)
         When the RTC Operating Mode bits in the Control A register (CTRLA.MODE) are written to 0x2, the
         counter operates in Clock/Calendar mode, as shown in Figure 21-3. When the RTC is enabled, the
         counter will increment on every 0-to-1 transition of CLK_RTC_CNT. The selected clock source and RTC
         prescaler must be configured to provide a 1Hz clock to the counter for correct operation in this mode.
         The time and date can be read from or written to the Clock Value register (CLOCK) in a 32-bit time/date
         format. Time is represented as:
          • Seconds
          • Minutes
          • Hours
         Hours can be represented in either 12- or 24-hour format, selected by the Clock Representation bit in the
         Control A register (CTRLA.CLKREP). This bit can be changed only while the RTC is disabled.
         The date is represented in this form:
          • Day as the numeric day of the month (starting at 1)
          • Month as the numeric month of the year (1 = January, 2 = February, etc.)
          • Year as a value from 0x00 to 0x3F. This value must be added to a user-defined reference year. The
            reference year must be a leap year (2016, 2020 etc). Example: the year value 0x2D, added to a
            reference year 2016, represents the year 2061.
         The RTC will increment until it reaches the top value of 23:59:59 December 31 of year value 0x3F, and
         then wrap to 00:00:00 January 1 of year value 0x00. This will set the Overflow Interrupt flag in the
         Interrupt Flag Status and Clear registers (INTFLAG.OVF).
         The clock value is continuously compared with the 32-bit Alarm registers (ALARMn, n=0–1). When an
         alarm match occurs, the Alarm n Interrupt flag in the Interrupt Flag Status and Clear registers




        © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 288
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      RTC – Real-Time Counter

         (INTFLAG.ALARMn, n=0..1) is set on the next 0-to-1 transition of CLK_RTC_CNT. E.g. For a 1Hz clock
         counter, it means the Alarm 0 Interrupt flag is set with a delay of 1s after the occurrence of alarm match.
         A valid alarm match depends on the setting of the Alarm Mask Selection bits in the Alarm n Mask register
         (MASKn.SEL). These bits determine which time/date fields of the clock and alarm values are valid for
         comparison and which are ignored.
         If the Clear on Match bit in the Control A register (CTRLA.MATCHCLR) is set, the counter is cleared on
         the next counter cycle when an alarm match with ALARMn occurs. This allows the RTC to generate
         periodic interrupts or events with longer periods than it would be possible with the prescaler events only
         (see 21.6.8.1 Periodic Intervals).
         Note: When CTRLA.MATCHCLR is 1, INTFLAG.ALARM0 and INTFLAG.OVF will both be set
         simultaneously on an alarm match with ALARMn.

21.6.3   DMA Operation
         The RTC generates the following DMA request:
           • Tamper (TAMPER): The request is set on capture of the timestamp. The request is cleared when the
             Timestamp register is read.
         If the CPU accesses the registers which are source for DMA request set/clear condition, the DMA request
         can be lost or the DMA transfer can be corrupted, if enabled.

21.6.4   Interrupts
         The RTC has the following interrupt sources:
           •   Overflow (OVF): Indicates that the counter has reached its top value and wrapped to zero.
           •   Tamper (TAMPER): Indicates detection of valid signal on a tamper input pin or tamper event input.
           •   Compare (CMPn): Indicates a match between the counter value and the compare register.
           •   Alarm (ALARMn): Indicates a match between the clock value and the alarm register.
           •   Period n (PERn): The corresponding bit in the prescaler has toggled. Refer to 21.6.8.1 Periodic
               Intervals for details.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by setting the corresponding bit in the Interrupt Enable Set register (INTENSET=1),
         and disabled by setting the corresponding bit in the Interrupt Enable Clear register (INTENCLR=1).
         An interrupt request is generated when the interrupt flag is raised and the corresponding interrupt is
         enabled. The interrupt request remains active until either the interrupt flag is cleared, the interrupt is
         disabled or the RTC is reset. See the description of the INTFLAG registers for details on how to clear
         interrupt flags.
         All interrupt requests from the peripheral are ORed together on system level to generate one combined
         interrupt request to the NVIC. Refer to the Nested Vector Interrupt Controller for details. The user must
         read the INTFLAG register to determine which interrupt condition is present.
         Note: Interrupts must be globally enabled for interrupt requests to be generated. Refer to the Nested
         Vector Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 289
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.6.5   Events
         The RTC can generate the following output events:
           • Overflow (OVF): Generated when the counter has reached its top value and wrapped to zero.
           • Tamper (TAMPER): Generated on detection of valid signal on a tamper input pin or tamper event
             input.
           • Compare (CMPn): Indicates a match between the counter value and the compare register.
           • Alarm (ALARM): Indicates a match between the clock value and the alarm register.
           • Period n (PERn): The corresponding bit in the prescaler has toggled. Refer to 21.6.8.1 Periodic
             Intervals for details.
           • Periodic Daily (PERD): Generated when the COUNT/CLOCK has incremented at a fixed period of
             time.
         Setting the Event Output bit in the Event Control Register (EVCTRL.xxxEO=1) enables the corresponding
         output event. Writing a zero to this bit disables the corresponding output event. Refer to the EVSYS -
         Event System for details on configuring the event system.
         The RTC can take the following actions on an input event:
           • Tamper (TAMPEVT): Capture the RTC counter to the timestamp register. See Tamper Detection.
         Writing a one to an Event Input bit into the Event Control register (EVCTRL.xxxEI) enables the
         corresponding action on input event. Writing a zero to this bit disables the corresponding action on input
         event.
         Related Links
         31. EVSYS – Event System

21.6.6   Sleep Mode Operation
         The RTC will continue to operate in any sleep mode where the source clock is active. The RTC interrupts
         can be used to wake up the device from a sleep mode. RTC events can trigger other operations in the
         system without exiting the sleep mode.
         An interrupt request will be generated after the wake-up if the Interrupt Controller is configured
         accordingly. Otherwise the CPU will wake up directly, without triggering any interrupt. In this case, the
         CPU will continue executing right from the first instruction that followed the entry into sleep.
         The periodic events can also wake up the CPU through the interrupt function of the Event System. In this
         case, the event must be enabled and connected to an event channel with its interrupt enabled. See Event
         System for more information.

21.6.7   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           •   Software Reset bit in Control A register, CTRLA.SWRST
           •   Enable bit in Control A register, CTRLA.ENABLE
           •   Count Read Synchronization bit in Control A register (CTRLA.COUNTSYNC)
           •   Clock Read Synchronization bit in Control A register (CTRLA.COUNTSYNC)
         The following registers are synchronized when written:




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 290
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

           •   Counter Value register, COUNT
           •   Clock Value register, CLOCK
           •   Counter Period register, PER
           •   Compare n Value registers, COMPn
           •   Alarm n Value registers, ALARMn
           •   Frequency Correction register, FREQCORR
           •   Alarm n Mask register, MASKn
           •   The General Purpose n registers (GPn)
         The following registers are synchronized when read:
           • The Counter Value register, COUNT, if the Counter Read Sync Enable bit in CTRLA
             (CTRLA.COUNTSYNC) is '1'
           • The Clock Value register, CLOCK, if the Clock Read Sync Enable bit in CTRLA
             (CTRLA.CLOCKSYNC) is '1'
           • The Timestamp Value register (TIMESTAMP)
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.
         Required read synchronization is denoted by the "Read-Synchronized" property in the register
         description.
         Related Links
         13.3 Register Synchronization

21.6.8   Additional Features

21.6.8.1 Periodic Intervals
         The RTC prescaler can generate interrupts and events at periodic intervals, allowing flexible system tick
         creation. Any of the upper eight bits of the prescaler (bits 2 to 9) can be the source of an interrupt/event.
         When one of the eight Periodic Event Output bits in the Event Control register (EVCTRL.PEREO[n=0..7])
         is '1', an event is generated on the 0-to-1 transition of the related bit in the prescaler, resulting in a
         periodic event frequency of:
                          �CLK_RTC_OSC
         �PERIODIC(n) =
                                 2n+3
         fCLK_RTC_OSC is the frequency of the internal prescaler clock CLK_RTC_OSC, and n is the position of the
         EVCTRL.PEREOn bit. For example, PER0 will generate an event every eight CLK_RTC_OSC cycles,
         PER1 every 16 cycles, etc. This is shown in the figure below.
         Periodic events are independent of the prescaler setting used by the RTC counter, except if
         CTRLA.PRESCALER is zero. Then, no periodic events will be generated.
         Figure 21-4. Example Periodic Events
                   CLK_RTC_OSC

                          PER0
                          PER1
                          PER2
                          PER3




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 291
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.6.8.2 Frequency Correction
        The RTC Frequency Correction module employs periodic counter corrections to compensate for a too-
        slow or too-fast oscillator. Frequency correction requires that CTRLA.PRESCALER is greater than 1.
        The digital correction circuit adds or subtracts cycles from the RTC prescaler to adjust the frequency in
        approximately 1ppm steps. Digital correction is achieved by adding or skipping a single count in the
        prescaler once every 8192 CLK_RTC_OSC cycles. The Value bit group in the Frequency Correction
        register (FREQCORR.VALUE) determines the number of times the adjustment is applied over 128 of
        these periods. The resulting correction is as follows:
                                 FREQCORR.VALUE
        Correction in ppm =                     ⋅ 106ppm
                                    8192 ⋅ 128
        This results in a resolution of 0.95367ppm.
        The Sign bit in the Frequency Correction register (FREQCORR.SIGN) determines the direction of the
        correction. A positive value will add counts and increase the period (reducing the frequency), and a
        negative value will reduce counts per period (speeding up the frequency).
        Digital correction also affects the generation of the periodic events from the prescaler. When the
        correction is applied at the end of the correction cycle period, the interval between the previous periodic
        event and the next occurrence may also be shortened or lengthened depending on the correction value.
21.6.8.3 Backup Registers
        The RTC includes eight Backup registers (BKUPn). These registers maintain their content in Backup
        sleep mode. They can be used to store user-defined values.
        If more user-defined data must be stored than the eight Backup registers can hold, the General Purpose
        registers (GPn) can be used.
        Related Links
        18. PM – Power Manager

21.6.8.4 General Purpose Registers
        The RTC includes four General Purpose registers (GPn). These registers are reset only when the RTC is
        reset or when tamper detection occurs while CTRLA.GPTRST=1, and remain powered while the RTC is
        powered. They can be used to store user-defined values while other parts of the system are powered off.
        The general purpose registers 2*n and 2*n+1 are enabled by writing a '1' to the General Purpose Enable
        bit n in the Control B register (CTRLB.GPnEN).
        The GP registers share internal resources with the COMPARE/ALARM features. Each COMPARE/
        ALARM register have a separate read buffer and write buffer. When the general purpose feature is
        enabled the even GP uses the read buffer while the odd GP uses the write buffer.
        When the COMPARE/ALARM register is written, the write buffer hold temporarily the COMPARE/ALARM
        value until the synchronisation is complete (bit SYNCBUSY.COMPn going to 0). After the write is
        completed the write buffer can be used as a odd general purpose register whithout affecting the
        COMPARE/ALARM function.
        If the COMPARE/ALARM function is not used, the read buffer can be used as an even general purpose
        register. In this case writing the even GP will temporarirely use the write buffer until the synchronisation is
        complete (bit SYNCBUSY.GPn going to 0). Thus an even GP must be written before writing the odd GP.
        Changing or writing an even GP needs to temporarily save the value of the odd GP.
        Before using an even GP, the associated COMPARE/ALARM feature must be disabled by writing a '1' to
        the General Purpose Enable bit in the Control B register (CTRLB.GPnEN). To re-enable the compare/




        © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 292
                                                           SAM D5x/E5x Family Data Sheet
                                                                                    RTC – Real-Time Counter

        alarm, CTRLB.GPnEN must be written to zero and the associated COMPn/ALARMn must be written with
        the correct value.
        An example procedure to write the general purpose registers GP0 and GP1 is:
         1. Wait for any ongoing write to COMP0 to complete (SYNCBUSY.COMP0 = 0). If the RTC is
             operating in Mode 1, wait for any ongoing write to COMP1 to complete as well
             (SYNCBUSY.COMP1 = 0).
         2. Write CTRLB.GP0EN = 1 if GP0 is needed.
         3. Write GP0 if needed.
         4. Wait for any ongoing write to GP0 to complete (SYNCBUSY.GP0 = 0). Note that GP1 will also show
             as busy when GP0 is busy.
         5. Write GP1 if needed.
        The following table provides the correspondence of General Purpose Registers and the COMPARE/
        ALARM read or write buffer in all RTC modes.
        Table 21-2. General Purpose Registers Versus Compare/Alarm Registers: n in 0, 2, 4, 6...

         Register                 Mode 0            Mode 1                Mode 2                Write Before
         GPn                      COMPn/2 write     (COMPn , COMPn        ALARMn/2 write        GPn+1
                                  buffer            +1) write buffer      buffer
         GPn+1                    COMPn/2 read      (COMPn , COMPn        ALARMn/2 read         -
                                  buffer            +1) read buffer       buffer

21.6.8.5 Tamper Detection
        The RTC provides four tamper channels that can be used for tamper detection.
        The action of each tamper channel is configured using the Input n Action bits in the Tamper Control
        register (TAMPCTRL.INnACT):
          • Off: Detection for tamper channel n is disabled.
          • Wake: A transition on INn input (tamper channel n) matching TAMPCTRL.TAMPLVLn will be
             detected and the tamper interrupt flag (INTFLAG.TAMPER) will be set. The RTC value will not be
             captured in the TIMESTAMP register.
          • Capture: A transition on INn input (tamper channel n) matching TAMPCTRL.TAMPLVLn will be
             detected and the tamper interrupt flag (INTFLAG.TAMPER) will be set. The RTC value will be
             captured in the TIMESTAMP register.
          • Active Layer Protection: A mismatch of an internal RTC signal routed between INn and OUTn pins
             will be detected and the tamper interrupt flag (INTFLAG.TAMPER) will be set. The RTC value will be
             captured in the TIMESTAMP register.
        In order to determine which tamper source caused a tamper event, the Tamper ID register (TAMPID)
        provides the detection status of each tamper channel. These bits remain active until cleared by software.
        A single interrupt request (TAMPER) is available for all tamper channels.
        The RTC also supports an input event (TAMPEVT) for generating a tamper condition within the Event
        System. The tamper input event is enabled by the Tamper Input Event Enable bit in the Event Control
        register (EVCTRL.TAMPEVEI).
        Up to four polarity external inputs (INn) can be used for tamper detection. The polarity for each input is
        selected with the Tamper Level bits in the Tamper Control register (TAMPCTRL.TAMPLVLn).




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 293
                                                 SAM D5x/E5x Family Data Sheet
                                                                         RTC – Real-Time Counter

Separate debouncers are embedded for each external input. The debouncer for each input is enabled/
disabled with the Debounce Enable bits in the Tamper Control register (TAMPCTRL.DEBNCn). The
debouncer configuration is fixed for all inputs as set by the Control B register (CTRLB). The debouncing
period duration is configurable using the Debounce Frequency field in the Control B register
(CTRLB.DEBF). The period is set for all debouncers (i.e., the duration cannot be adjusted separately for
each debouncer).
When TAMPCTRL.DEBNCn = 0, INn is detected asynchronously. See Figure 21-5 for an example.
When TAMPCTRL.DEBNCn = 1, the detection time depends on whether the debouncer operates
synchronously or asynchronously, and whether majority detection is enabled or not. Refer to the table
below for more details. Synchronous versus asynchronous stability debouncing is configured by the
Debounce Asynchronous Enable bit in the Control B register (CTRLB.DEBASYNC):
 • Synchronous (CTRLB.DEBASYNC = 0): INn is synchronized in two CLK_RTC periods and then must
    remain stable for four CLK_RTC_DEB periods before a valid detection occurs. See Figure 21-6 for
    an example.
 • Asynchronous (CTRLB.DEBASYNC = 1): The first edge on INn is detected. Further detection is
    blanked until INn remains stable for four CLK_RTC_DEB periods. See Figure 21-7 for an example.
Majority debouncing is configured by the Debounce Majority Enable bit in the Control B register
(CTRLB.DEBMAJ). INn must be valid for two out of three CLK_RTC_DEB periods. See Figure 21-8 for an
example.
Table 21-3. Debouncer Configuration

 TAMPCTRL.          CTRLB.         CTRLB.        Description
 DEBNCn             DEBMAJ         DEBASYNC
 0                  X              X             Detect edge on INn with no debouncing. Every edge
                                                 detected is immediately triggered.
 1                  0              0             Detect edge on INn with synchronous stability
                                                 debouncing. Edge detected is only triggered when INn
                                                 is stable for 4 consecutive CLK_RTC_DEB periods.
 1                  0              1             Detect edge on INn with asynchronous stability
                                                 debouncing. First detected edge is triggered
                                                 immediately. All subsequent detected edges are
                                                 ignored until INn is stable for 4 consecutive
                                                 CLK_RTC_DEB periods.
 1                  1              X             Detect edge on INn with majority debouncing. Pin INn
                                                 is sampled for 3 consecutive CLK_RTC_DEB periods.
                                                 Signal level is determined by majority-rule (LLL, LLH,
                                                 LHL, HLL = '0' and LHH, HLH, HHL, HHH = '1').




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 294
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                                   RTC – Real-Time Counter

Figure 21-5. Edge Detection with Debouncer Disabled

                 CLK_RTC

             CLK_RTC_DEB

                                        PE                                             PE                                      PE
                       IN          NE        NE                                                                           NE


                     OUT

                                                                        TAMLVL=0



                 CLK_RTC

             CLK_RTC_DEB

                                        PE                                             PE                                      PE
                       IN          NE        NE                                                                           NE


                     OUT

                                                                        TAMLVL=1

Figure 21-6. Edge Detection with Synchronous Stability Debouncing

                 CLK_RTC

             CLK_RTC_DEB

                                        PE                                             PE                                      PE
                       IN      NE            NE                                                                           NE




                                                                            Whenever an edge is detected, input must be
                                                                             stable for 4 consecutive CLK_RTC_DEB in
                                                                                order for edge to be considered valid


                     OUT

                                                                        TAMLVL=0



                 CLK_RTC

             CLK_RTC_DEB

                                        PE                                             PE                                      PE
                       IN      NE            NE                                                                           NE




                                                  Whenever an edge is detected, input must be
                                                   stable for 4 consecutive CLK_RTC_DEB in
                                                      order for edge to be considered valid


                     OUT

                                                                        TAMLVL=1




© 2019 Microchip Technology Inc.                                    Datasheet                                                  DS60001507E-page 295
                                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                                            RTC – Real-Time Counter

Figure 21-7. Edge Detection with Asynchronous Stability Debouncing

                 CLK_RTC

             CLK_RTC_DEB

                                               PE                                                  PE                                            PE
                         IN        NE                 NE                                                                                NE



                                    Once a new edge is detected, ignore subsequent edges
                                     until input is stable for 4 consecutive CLK_RTC_DEB

                      OUT

                                                                                        TAMLVL=0



                 CLK_RTC

             CLK_RTC_DEB

                                               PE                                                  PE                                            PE
                         IN        NE                 NE                                                                                NE



                                    Once a new edge is detected, ignore subsequent edges
                                     until input is stable for 4 consecutive CLK_RTC_DEB

                      OUT

                                                                                        TAMLVL=1

Figure 21-8. Edge Detection with Majority Debouncing

                 CLK_RTC

             CLK_RTC_DEB

                                               PE                                                  PE                                            PE
                         IN        NE                 NE                                                                                NE



                  IN shift 0   1        0       1          0           0           0       0   0        1   1           1           1        0        1   1

                  IN shift 1   1        1       0          1           0           0       0   0        0   1           1           1        1        0   1

                  IN shift 2   1        1       1          0           1           0       0   0        0   0           1           1        1        1   0




               MAJORITY3       1        1       1          0           0           0       0   0        0   1           1           1        1        1   1

                                                               1-to-0 transition


                      OUT

                                                                                        TAMLVL=0



                 CLK_RTC

             CLK_RTC_DEB

                                               PE                                                  PE                                            PE
                         IN        NE                 NE                                                                                NE



                  IN shift 0   1        0       1          0           0           0       0   0        1   1           1           1        0        1   1

                  IN shift 1   1        1       0          1           0           0       0   0        0   1           1           1        1        0   1

                  IN shift 2   1        1       1          0           1           0       0   0        0   0           1           1        1        1   0




               MAJORITY3       1        1       1          0           0           0       0   0        0   1           1           1        1        1   1

                                                                                                                0-to-1 transition


                      OUT

                                                                                        TAMLVL=1




© 2019 Microchip Technology Inc.                                                       Datasheet                                                 DS60001507E-page 296
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

          Related Links
          21.3 Block Diagram
          21.6.8.5.1 Timestamp
          21.6.8.5.2 Active Layer Protection

21.6.8.5.1 Timestamp
          As part of tamper detection the RTC can capture the counter value (COUNT/CLOCK) into the
          TIMESTAMP register. Three CLK_RTC periods are required to detect the tampering condition and
          capture the value. The TIMESTAMP value can be read once the Tamper flag in the Interrupt Flag register
          (INTFLAG.TAMPER) is set. If the DMA Enable bit in the Control B register (CTRLB.DMAEN) is ‘1’, a DMA
          request will be triggered by the timestamp. In order to determine which tamper source caused a capture,
          the Tamper ID register (TAMPID) provides the detection status of each tamper channel and the tamper
          input event. A DMA transfer can then read both TIMESTAMP and TAMPID in succession.
          A new timestamp value cannot be captured until the Tamper flag is cleared, either by reading the
          timestamp or by writing a ‘1’ to INTFLAG.TAMPER. If several tamper conditions occur in a short window
          before the flag is cleared, only the first timestamp may be logged. However, the detection of each tamper
          will still be recorded in TAMPID.
          The Tamper Input Event (TAMPEVT) will always perform a timestamp capture. To capture on the external
          inputs (INn), the corresponding Input Action field in the Tamper Control register (TAMPCTRL.INnACT)
          must be written to ‘1’. If an input is set for wake functionality it does not capture the timestamp; however
          the Tamper flag and TAMPID will still be updated.
          Related Links
          21.6.8.5 Tamper Detection

21.6.8.5.2 Active Layer Protection
          The RTC provides a mean of detecting broken traces on the PCB , also known as Active layer Protection.
          In this mode, a generated internal RTC signal can be directly routed over critical components on the
          board using RTC OUT output pin to one RTC INn input pin. A tamper condition is detected if there is a
          mismatch on the generated RTC signal.
          The Active Layer Protection mode and the generation of the RTC signal is enabled by setting the
          RTCOUT bit in the Control B register (CTRLB.RTCOUT).
          Enabling active layer protection requires the following steps:
           • Enable the RTC prescaler output by writing a one to the RTC Out bit in the Control B register
             (CTRLB.RTCOUT). The I/O pins must also be configured to correctly route the signal to the external
             pins.
           • Select the frequency of the output signal by configuring the RTC Active Layer Frequency field in the
             Control B register (CTRLB.ACTF).
                                    CLK_RTC
             GCLK_RTC_OUT = CTRLB.ACTF +1
                                  2
           • Enable the tamper input n (INn) in active layer mode by writing 3 to the corresponding Input Action
             field in the Tamper Control register (TAMPCTRL.INnACT). When active layer protection is enabled
             and INn and OUTn pin are used, the value of INn is sampled on the falling edge of CLK_RTC and
             compared to the expected value of OUTn. Therefore up to one half of a CLK_RTC period is available
             for propagation delay through the trace.
           • Enable Acitive Layer Protection by setting CTRLB.RTCOUT bit.
          Related Links




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 297
                                   SAM D5x/E5x Family Data Sheet
                                               RTC – Real-Time Counter

21.6.8.5 Tamper Detection




© 2019 Microchip Technology Inc.   Datasheet           DS60001507E-page 298
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter


21.7      Register Summary - Mode 0 - 32-Bit Counter

 Offset        Name        Bit Pos.

                              7:0     MATCHCLR                                             MODE[1:0]            ENABLE      SWRST
 0x00         CTRLA
                             15:8     COUNTSYNC    GPTRST     BKTRST                                   PRESCALER[3:0]
                              7:0      DMAEN       RTCOUT    DEBASYNC    DEBMAJ                                 GP2EN       GP0EN
 0x02         CTRLB
                             15:8                            ACTF[2:0]                                         DEBF[2:0]
                              7:0      PEREO7      PEREO6     PEREO5     PEREO4     PEREO3       PEREO2         PEREO1     PEREO0
                             15:8       OVFEO     TAMPEREO                                                      CMPEO1     CMPEO0
 0x04         EVCTRL
                             23:16                                                                                         TAMPEVEI
                             31:24
                              7:0       PER7        PER6       PER5       PER4       PER3          PER2          PER1       PER0
 0x08        INTENCLR
                             15:8        OVF       TAMPER                                                        CMP1       CMP0
                              7:0       PER7        PER6       PER5       PER4       PER3          PER2          PER1       PER0
 0x0A        INTENSET
                             15:8        OVF       TAMPER                                                        CMP1       CMP0
                              7:0       PER7        PER6       PER5       PER4       PER3          PER2          PER1       PER0
 0x0C        INTFLAG
                             15:8        OVF       TAMPER                                                        CMP1       CMP0
 0x0E        DBGCTRL          7:0                                                                                          DBGRUN
 0x0F        Reserved
                              7:0                  COMP1      COMP0                 COUNT       FREQCORR        ENABLE      SWRST
                             15:8     COUNTSYNC
 0x10       SYNCBUSY
                             23:16                                                    GP3          GP2            GP1        GP0
                             31:24
 0x14       FREQCORR          7:0       SIGN                                       VALUE[6:0]
 0x15
   ...       Reserved
 0x17
                              7:0                                            COUNT[7:0]
                             15:8                                           COUNT[15:8]
 0x18         COUNT
                             23:16                                          COUNT[23:16]
                             31:24                                          COUNT[31:24]
 0x1C
   ...       Reserved
 0x1F
                              7:0                                            COMP[7:0]
                             15:8                                            COMP[15:8]
 0x20         COMP0
                             23:16                                          COMP[23:16]
                             31:24                                          COMP[31:24]
                              7:0                                            COMP[7:0]
                             15:8                                            COMP[15:8]
 0x24         COMP1
                             23:16                                          COMP[23:16]
                             31:24                                          COMP[31:24]
 0x28
   ...       Reserved
 0x3F




          © 2019 Microchip Technology Inc.                            Datasheet                                DS60001507E-page 299
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter

...........continued

  Offset               Name     Bit Pos.

                                  7:0                                          GP[7:0]
                                 15:8                                          GP[15:8]
   0x40                 GP0
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
                                  7:0                                          GP[7:0]
                                 15:8                                          GP[15:8]
   0x44                 GP1
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
                                  7:0                                          GP[7:0]
                                 15:8                                          GP[15:8]
   0x48                 GP2
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
                                  7:0                                          GP[7:0]
                                 15:8                                          GP[15:8]
   0x4C                 GP3
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
   0x50
     ...           Reserved
   0x5F
                                  7:0            IN3ACT[1:0]   IN2ACT[1:0]                  IN1ACT[1:0]           IN0ACT[1:0]
                                 15:8                                                                             IN4ACT[1:0]
   0x60           TAMPCTRL
                                 23:16                                TAMLVL4        TAMLVL3       TAMLVL2   TAMLVL1     TAMLVL0
                                 31:24                                 DEBNC4        DEBNC3         DEBNC2   DEBNC1       DEBNC0
                                  7:0                                         COUNT[7:0]
                                 15:8                                        COUNT[15:8]
   0x64          TIMESTAMP
                                 23:16                                       COUNT[23:16]
                                 31:24                                       COUNT[31:24]
                                  7:0                                 TAMPID4        TAMPID3       TAMPID2   TAMPID1     TAMPID0
                                 15:8
   0x68                TAMPID
                                 23:16
                                 31:24     TAMPEVT
   0x6C
     ...           Reserved
   0x7F
                                  7:0                                         BKUP[7:0]
                                 15:8                                         BKUP[15:8]
   0x80                BKUP0
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                         BKUP[15:8]
   0x84                BKUP1
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]




              © 2019 Microchip Technology Inc.                   Datasheet                                   DS60001507E-page 300
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x88                BKUP2
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x8C                BKUP3
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x90                BKUP4
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x94                BKUP5
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x98                BKUP6
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x9C                BKUP7
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]




21.8           Register Description - Mode 0 - 32-Bit Counter
               This Register Description section is valid if the RTC is in COUNT32 mode (CTRLA.MODE=0).
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 301
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                 RTC – Real-Time Counter

21.8.1         Control A in COUNT32 mode (CTRLA.MODE=0)

               Name:       CTRLA
               Offset:     0x00
               Reset:      0x0000
               Property:   PAC Write-Protection, Enable-Protected, Write-Synchronized


         Bit        15            14            13           12           11                10           9           8
               COUNTSYNC       GPTRST         BKTRST                                        PRESCALER[3:0]
   Access          R/W           R/W           R/W                        R/W               R/W         R/W         R/W
    Reset            0            0             0                          0                 0           0           0


         Bit         7            6             5            4             3                 2           1           0
                MATCHCLR                                                        MODE[1:0]              ENABLE      SWRST
   Access          R/W                                                    R/W               R/W         R/W         R/W
    Reset            0                                                     0                 0           0           0


               Bit 15 – COUNTSYNC COUNT Read Synchronization Enable
               The COUNT register requires synchronization when reading. Disabling the synchronization will prevent
               reading valid values from the COUNT register.
               This bit is not enable-protected.
                Value       Description
                0           COUNT read synchronization is disabled
                1           COUNT read synchronization is enabled

               Bit 14 – GPTRST GP Registers Reset On Tamper Enable
               Only GP registers enabled by the CTRLB.GPnEN bits are affected. This bit can be written only when the
               peripheral is disabled.
               This bit is not synchronized.

               Bit 13 – BKTRST BKUP Registers Reset On Tamper Enable
               All BKUPn registers are affected. This bit can be written only when the peripheral is disabled.
               This bit is not synchronized.
                Value       Description
                0           BKUPn registers will not reset when a tamper condition occurs.
                1           BKUPn registers will reset when a tamper condition occurs.

               Bits 11:8 – PRESCALER[3:0] Prescaler
               These bits define the prescaling factor for the RTC clock source (GCLK_RTC) to generate the counter
               clock (CLK_RTC_CNT). Periodic events and interrupts are not available when the prescaler is off. These
               bits are not synchronized.
                Value       Name               Description
                0x0         OFF                CLK_RTC_CNT = GCLK_RTC/1
                0x1         DIV1               CLK_RTC_CNT = GCLK_RTC/1
                0x2         DIV2               CLK_RTC_CNT = GCLK_RTC/2
                0x3         DIV4               CLK_RTC_CNT = GCLK_RTC/4
                0x4         DIV8               CLK_RTC_CNT = GCLK_RTC/8
                0x5         DIV16              CLK_RTC_CNT = GCLK_RTC/16




           © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 302
                                                   SAM D5x/E5x Family Data Sheet
                                                                             RTC – Real-Time Counter

 Value        Name                 Description
 0x6          DIV32                CLK_RTC_CNT = GCLK_RTC/32
 0x7          DIV64                CLK_RTC_CNT = GCLK_RTC/64
 0x8          DIV128               CLK_RTC_CNT = GCLK_RTC/128
 0x9          DIV256               CLK_RTC_CNT = GCLK_RTC/256
 0xA          DIV512               CLK_RTC_CNT = GCLK_RTC/512
 0xB          DIV1024              CLK_RTC_CNT = GCLK_RTC/1024
 0xC-0xF      -                    Reserved

Bit 7 – MATCHCLR Clear on Match
This bit defines if the counter is cleared or not on a match.
This bit is not synchronized.
 Value       Description
 0           The counter is not cleared on a Compare/Alarm 0 match
 1           The counter is cleared on a Compare/Alarm 0 match

Bits 3:2 – MODE[1:0] Operating Mode
This bit group defines the operating mode of the RTC.
This bit is not synchronized.
 Value       Name                         Description
 0x0         COUNT32                      Mode 0: 32-bit counter
 0x1         COUNT16                      Mode 1: 16-bit counter
 0x2         CLOCK                        Mode 2: Clock/calendar
 0x3         -                            Reserved

Bit 1 – ENABLE Enable
Due to synchronization there is a delay between writing CTRLA.ENABLE and until the peripheral is
enabled/disabled. The value written to CTRLA.ENABLE will read back immediately and the Enable bit in
the Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be
cleared when the operation is complete.
 Value     Description
 0         The peripheral is disabled
 1         The peripheral is enabled

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the RTC (except DBGCTRL) to their initial state, and the RTC
will be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
write-operation will be discarded.
Due to synchronization there is a delay between writing CTRLA.SWRST and until the reset is complete.
CTRLA.SWRST will be cleared when the reset is complete.
Value         Description
0             There is not reset operation ongoing
1             The reset operation is ongoing




© 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 303
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

21.8.2         Control B in COUNT32 mode (CTRLA.MODE=0)

               Name:       CTRLB
               Offset:     0x02
               Reset:      0x0000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        15           14              13         12           11            10            9            8
                                              ACTF[2:0]                                          DEBF[2:0]
   Access                        R/W            R/W        R/W                        R/W          R/W           R/W
    Reset                         0              0           0                         0             0            0


         Bit         7            6              5           4            3            2             1            0
                  DMAEN        RTCOUT         DEBASYNC    DEBMAJ                                  GP2EN        GP0EN
   Access          R/W           R/W            R/W        R/W                                     R/W           R/W
    Reset            0            0              0           0                                       0            0


               Bits 14:12 – ACTF[2:0] Active Layer Frequency
               These bits define the prescaling factor for the RTC clock output (OUT) used during active layer protection
               in terms of the CLK_RTC.
                Value       Name              Description
                0x0         DIV2              CLK_RTC_OUT = CLK_RTC / 2
                0x1         DIV4              CLK_RTC_OUT = CLK_RTC / 4
                0x2         DIV8              CLK_RTC_OUT = CLK_RTC / 8
                0x3         DIV16             CLK_RTC_OUT = CLK_RTC / 16
                0x4         DIV32             CLK_RTC_OUT = CLK_RTC / 32
                0x5         DIV64             CLK_RTC_OUT = CLK_RTC / 64
                0x6         DIV128            CLK_RTC_OUT = CLK_RTC / 128
                0x7         DIV256            CLK_RTC_OUT = CLK_RTC / 256

               Bits 10:8 – DEBF[2:0] Debounce Frequency
               These bits define the prescaling factor for the input debouncers in terms of the CLK_RTC.
                Value      Name               Description
                0x0        DIV2               CLK_RTC_DEB = CLK_RTC / 2
                0x1        DIV4               CLK_RTC_DEB = CLK_RTC / 4
                0x2        DIV8               CLK_RTC_DEB = CLK_RTC / 8
                0x3        DIV16              CLK_RTC_DEB = CLK_RTC / 16
                0x4        DIV32              CLK_RTC_DEB = CLK_RTC / 32
                0x5        DIV64              CLK_RTC_DEB = CLK_RTC / 64
                0x6        DIV128             CLK_RTC_DEB = CLK_RTC / 128
                0x7        DIV256             CLK_RTC_DEB = CLK_RTC / 256

               Bit 7 – DMAEN DMA Enable
               The RTC can trigger a DMA request when the timestamp is ready in the TIMESTAMP register.
                Value     Description
                0         Tamper DMA request is disabled. Reading TIMESTAMP has no effect on
                          INTFLAG.TAMPER.
                1         Tamper DMA request is enabled. Reading TIMESTAMP will clear INTFLAG.TAMPER.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 304
                                                SAM D5x/E5x Family Data Sheet
                                                                      RTC – Real-Time Counter

Bit 6 – RTCOUT RTC Output Enable
Value      Description
0          The RTC active layer output is disabled.
1          The RTC active layer output is enabled.

Bit 5 – DEBASYNC Debouncer Asynchronous Enable
Value      Description
0          The tamper input debouncers operate synchronously.
1          The tamper input debouncers operate asynchronously.

Bit 4 – DEBMAJ Debouncer Majority Enable
Value      Description
0          The tamper input debouncers match three equal values.
1          The tamper input debouncers match majority two of three values.

Bit 1 – GP2EN General Purpose 2 Enable
Value      Description
0          COMP1 compare function enabled. GP2/GP3 disabled.
1          COMP1 compare function disabled. GP2/GP3 enabled.

Bit 0 – GP0EN General Purpose 0 Enable
Value      Description
0          COMP0 compare function enabled. GP0/GP1 disabled.
1          COMP0 compare function disabled. GP0/GP1 enabled.




© 2019 Microchip Technology Inc.                 Datasheet                    DS60001507E-page 305
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

21.8.3         Event Control in COUNT32 mode (CTRLA.MODE=0)

               Name:       EVCTRL
               Offset:     0x04
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31            30            29          28            27           26            25              24


   Access
    Reset


         Bit        23            22            21          20            19           18            17              16
                                                                                                                 TAMPEVEI
   Access                                                                                                           R/W
    Reset                                                                                                            0


         Bit        15            14            13          12            11           10            9               8
                  OVFEO       TAMPEREO                                                            CMPEO1          CMPEO0
   Access          R/W           R/W                                                                R/W             R/W
    Reset            0            0                                                                  0               0


         Bit         7            6             5            4            3             2            1               0
                 PEREO7        PEREO6         PEREO5      PEREO4       PEREO3       PEREO2        PEREO1          PEREO0
   Access          R/W           R/W           R/W          R/W          R/W          R/W           R/W             R/W
    Reset            0            0             0            0            0             0            0               0


               Bit 16 – TAMPEVEI Tamper Event Input Enable
               Value      Description
               0          Tamper event input is disabled and incoming events will be ignored.
               1          Tamper event input is enabled and incoming events will capture the COUNT value.

               Bit 15 – OVFEO Overflow Event Output Enable
               Value      Description
               0          Overflow event is disabled and will not be generated.
               1          Overflow event is enabled and will be generated for every overflow.

               Bit 14 – TAMPEREO Tamper Event Output Enable
               Value      Description
               0          Tamper event output is disabled and will not be generated.
               1          Tamper event output is enabled and will be generated for every tamper input.

               Bits 8, 9 – CMPEOn Compare n Event Output Enable [n = 1..0]
               Value       Description
               0            Compare n event is disabled and will not be generated.
               1            Compare n event is enabled and will be generated for every compare match.

               Bits 0, 1, 2, 3, 4, 5, 6, 7 – PEREOn Periodic Interval n Event Output Enable [n = 7..0]




           © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 306
                                                    SAM D5x/E5x Family Data Sheet
                                                                             RTC – Real-Time Counter

 Value        Description
 0            Periodic Interval n event is disabled and will not be generated.
 1            Periodic Interval n event is enabled and will be generated.




© 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 307
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 RTC – Real-Time Counter

21.8.4         Interrupt Enable Clear in COUNT32 mode (CTRLA.MODE=0)

               Name:        INTENCLR
               Offset:      0x08
               Reset:       0x0000
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

         Bit         15            14            13             12            11            10             9             8
                    OVF         TAMPER                                                                   CMP1          CMP0
   Access           R/W           R/W                                                                     R/W           R/W
    Reset            0             0                                                                       0             0


         Bit         7             6              5             4             3              2             1             0
                   PER7          PER6           PER5          PER4          PER3           PER2          PER1          PER0
   Access           R/W           R/W           R/W            R/W           R/W           R/W            R/W           R/W
    Reset            0             0              0             0             0              0             0             0


               Bit 15 – OVF Overflow Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Overflow Interrupt Enable bit, which disables the Overflow interrupt.
               Value         Description
               0             The Overflow interrupt is disabled.
               1             The Overflow interrupt is enabled.

               Bit 14 – TAMPER Tamper Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this but will clear the Tamper Interrupt Enable bit, which disables the Tamper interrupt.
               Value         Description
               0             The Tamper interrupt is disabled.
               1             The Tamper interrupt is enabled.

               Bits 8, 9 – CMPn Compare n Interrupt Enable [n = 1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Compare n Interrupt Enable bit, which disables the Compare n
               interrupt.
                Value        Description
                0            The Compare n interrupt is disabled
                1            The Compare n interrupt is enabled.

               Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n Interrupt Enable [n = 7..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Periodic Interval n Interrupt Enable bit, which disables the Periodic
               Interval n interrupt.
                Value        Description
                0            Periodic Interval n interrupt is disabled.
                1            Periodic Interval n interrupt is enabled.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 308
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 RTC – Real-Time Counter

21.8.5         Interrupt Enable Set in COUNT32 mode (CTRLA.MODE=0)

               Name:        INTENSET
               Offset:      0x0A
               Reset:       0x0000
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         15            14            13            12             11            10             9             8
                    OVF         TAMPER                                                                   CMP1          CMP0
   Access           R/W           R/W                                                                    R/W            R/W
    Reset            0             0                                                                       0             0


         Bit         7             6              5             4             3             2              1             0
                   PER7          PER6           PER5          PER4          PER3          PER2           PER1          PER0
   Access           R/W           R/W           R/W            R/W           R/W           R/W           R/W            R/W
    Reset            0             0              0             0             0             0              0             0


               Bit 15 – OVF Overflow Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Overflow Interrupt Enable bit, which enables the Overflow interrupt.
               Value         Description
               0             The Overflow interrupt is disabled.
               1             The Overflow interrupt is enabled.

               Bit 14 – TAMPER Tamper Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Tamper Interrupt Enable bit, which enables the Tamper interrupt.
               Value         Description
               0             The Tamper interrupt is disabled.
               1             The Tamper interrupt is enabled.

               Bits 8, 9 – CMPn Compare n Interrupt Enable [n = 1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Compare n Interrupt Enable bit, which and enables the Compare n
               interrupt.
                Value        Description
                0            The Compare n interrupt is disabled.
                1            The Compare n interrupt is enabled.

               Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n Interrupt Enable [n = 7..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Periodic Interval n Interrupt Enable bit, which enables the Periodic
               Interval n interrupt.
                Value        Description
                0            Periodic Interval n interrupt is disabled.
                1            Periodic Interval n interrupt is enabled.




           © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 309
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter

21.8.6         Interrupt Flag Status and Clear in COUNT32 mode (CTRLA.MODE=0)

               Name:        INTFLAG
               Offset:      0x0C
               Reset:       0x0000
               Property:    -


         Bit        15             14            13            12            11            10             9             8
                    OVF         TAMPER                                                                  CMP1          CMP0
   Access           R/W           R/W                                                                    R/W           R/W
    Reset            0             0                                                                      0             0


         Bit         7             6             5             4              3             2             1             0
                   PER7          PER6          PER5           PER4          PER3          PER2          PER1          PER0
   Access           R/W           R/W           R/W           R/W           R/W           R/W            R/W           R/W
    Reset            0             0             0             0              0             0             0             0


               Bit 15 – OVF Overflow
               This flag is cleared by writing a '1' to the flag.
               This flag is set on the next CLK_RTC_CNT cycle after an overflow condition occurs, and an interrupt
               request will be generated if INTENCLR/SET.OVF is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Overflow interrupt flag.

               Bit 14 – TAMPER Tamper event
               This flag is set after a damper condition occurs, and an interrupt request will be generated if
               INTENCLR.TAMPER/INTENSET.TAMPER is '1'. Writing a '0' to this bit has no effect. Writing a '1' to this
               bit clears the Tamper interrupt flag.

               Bits 8, 9 – CMPn Compare n [n = 1..0]
               This flag is cleared by writing a '1' to the flag.
               This flag is set on the next CLK_RTC_CNT cycle after a match with the compare condition, and an
               interrupt request will be generated if INTENCLR/SET.COMPn is one.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Compare n interrupt flag.

               Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n [n = 7..0]
               This flag is cleared by writing a '1' to the flag.
               This flag is set on the 0-to-1 transition of prescaler bit [n+2], and an interrupt request will be generated if
               INTENCLR/SET.PERn is one.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Periodic Interval n interrupt flag.




           © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 310
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.8.7         Debug Control

               Name:       DBGCTRL
               Offset:     0x0E
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5           4            3            2            1           0
                                                                                                          DBGRUN
   Access                                                                                                   R/W
    Reset                                                                                                    0


               Bit 0 – DBGRUN Debug Run
               This bit is not reset by a software reset.
               This bit controls the functionality when the CPU is halted by an external debugger.
                Value       Description
                0           The RTC is halted when the CPU is halted by an external debugger.
                1           The RTC continues normal operation when the CPU is halted by an external debugger.




           © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 311
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           RTC – Real-Time Counter

21.8.8         Synchronization Busy in COUNT32 mode (CTRLA.MODE=0)

               Name:       SYNCBUSY
               Offset:     0x10
               Reset:      0x00000000
               Property:   -


         Bit        31           30            29         28           27           26             25          24


   Access
    Reset


         Bit        23           22            21         20           19           18             17          16
                                                                      GP3           GP2           GP1         GP0
   Access                                                              R               R           R           R
    Reset                                                              0               0           0           0


         Bit        15           14            13         12           11           10             9           8
               COUNTSYNC
   Access           R
    Reset           0


         Bit        7             6             5         4            3               2           1           0
                               COMP1          COMP0                 COUNT      FREQCORR          ENABLE      SWRST
   Access                         R            R                       R               R           R           R
    Reset                         0             0                      0               0           0           0


               Bits 16, 17, 18, 19 – GPn General Purpose n Synchronization Busy Status
               Value       Description
               0           Write synchronization for GPn register is complete.
               1           Write synchronization for GPn register is ongoing.

               Bit 15 – COUNTSYNC Count Read Sync Enable Synchronization Busy Status
               Value      Description
               0          Write synchronization for CTRLA.COUNTSYNC bit is complete.
               1          Write synchronization for CTRLA.COUNTSYNC bit is ongoing.

               Bits 5, 6 – COMPn Compare n Synchronization Busy Status [n = 1..0]
               Value       Description
               0            Write synchronization for COMPx register is complete.
               1            Write synchronization for COMPx register is ongoing.

               Bit 3 – COUNT Count Value Synchronization Busy Status
               Value      Description
               0          Read/write synchronization for COUNT register is complete.
               1          Read/write synchronization for COUNT register is ongoing.

               Bit 2 – FREQCORR Frequency Correction Synchronization Busy Status




           © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 312
                                                 SAM D5x/E5x Family Data Sheet
                                                                         RTC – Real-Time Counter

 Value        Description
 0            Write synchronization for FREQCORR register is complete.
 1            Write synchronization for FREQCORR register is ongoing.

Bit 1 – ENABLE Enable Synchronization Busy Status
Value      Description
0          Write synchronization for CTRLA.ENABLE bit is complete.
1          Write synchronization for CTRLA.ENABLE bit is ongoing.

Bit 0 – SWRST Software Reset Synchronization Busy Status
Value      Description
0          Write synchronization for CTRLA.SWRST bit is complete.
1          Write synchronization for CTRLA.SWRST bit is ongoing.




© 2019 Microchip Technology Inc.                  Datasheet                      DS60001507E-page 313
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

21.8.9         Frequency Correction

               Name:       FREQCORR
               Offset:     0x14
               Reset:      0x00
               Property:   PAC Write-Protection, Write-Synchronized


         Bit         7            6             5            4             3            2           1           0
                   SIGN                                               VALUE[6:0]
   Access          R/W           R/W          R/W           R/W          R/W           R/W         R/W         R/W
    Reset            0            0             0            0             0            0           0           0


               Bit 7 – SIGN Correction Sign
               Value      Description
               0          The correction value is positive, i.e., frequency will be decreased.
               1          The correction value is negative, i.e., frequency will be increased.

               Bits 6:0 – VALUE[6:0] Correction Value
               These bits define the amount of correction applied to the RTC prescaler.
                Value      Description
                0          Correction is disabled and the RTC frequency is unchanged.
                1 - 127 The RTC frequency is adjusted according to the value.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 314
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.8.10 Counter Value in COUNT32 mode (CTRLA.MODE=0)

           Name:       COUNT
           Offset:     0x18
           Reset:      0x00000000
           Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized


     Bit        31           30           29            28                 27   26          25           24
                                                            COUNT[31:24]
  Access       R/W           R/W          R/W          R/W             R/W      R/W         R/W         R/W
   Reset         0            0            0            0                  0     0           0           0


     Bit        23           22           21            20                 19   18          17           16
                                                            COUNT[23:16]
  Access       R/W           R/W          R/W          R/W             R/W      R/W         R/W         R/W
   Reset         0            0            0            0                  0     0           0           0


     Bit        15           14           13            12                 11   10           9           8
                                                             COUNT[15:8]
  Access       R/W           R/W          R/W          R/W             R/W      R/W         R/W         R/W
   Reset         0            0            0            0                  0     0           0           0


     Bit         7            6            5            4                  3     2           1           0
                                                             COUNT[7:0]
  Access       R/W           R/W          R/W          R/W             R/W      R/W         R/W         R/W
   Reset         0            0            0            0                  0     0           0           0


           Bits 31:0 – COUNT[31:0] Counter Value
           These bits define the value of the 32-bit RTC counter in mode 0.




       © 2019 Microchip Technology Inc.                         Datasheet                    DS60001507E-page 315
                                                              SAM D5x/E5x Family Data Sheet
                                                                                       RTC – Real-Time Counter

21.8.11 Compare n Value in COUNT32 mode (CTRLA.MODE=0)

           Name:       COMP
           Offset:     0x20 + n*0x04 [n=0..1]
           Reset:      0x00000000
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        31           30           29           28                 27      26           25           24
                                                            COMP[31:24]
  Access       R/W          R/W           R/W          R/W               R/W     R/W          R/W          R/W
   Reset         0            0            0            0                 0       0            0            0


     Bit        23           22           21           20                 19      18           17           16
                                                            COMP[23:16]
  Access       R/W          R/W           R/W          R/W               R/W     R/W          R/W          R/W
   Reset         0            0            0            0                 0       0            0            0


     Bit        15           14           13           12                 11      10           9            8
                                                            COMP[15:8]
  Access       R/W          R/W           R/W          R/W               R/W     R/W          R/W          R/W
   Reset         0            0            0            0                 0       0            0            0


     Bit         7            6            5            4                 3       2            1            0
                                                             COMP[7:0]
  Access       R/W          R/W           R/W          R/W               R/W     R/W          R/W          R/W
   Reset         0            0            0            0                 0       0            0            0


           Bits 31:0 – COMP[31:0] Compare Value
           The 32-bit value of COMPn is continuously compared with the 32-bit COUNT value. When a match
           occurs, the Compare n interrupt flag in the Interrupt Flag Status and Clear register (INTFLAG.CMPn) is
           set on the next counter cycle, and the counter value is cleared if CTRLA.MATCHCLR is one.




       © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 316
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.8.12 General Purpose n

           Name:       GPn
           Offset:     0x40 + n*0x04 [n=0..3]
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29          28                27      26           25           24
                                                            GP[31:24]
  Access       R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset        0             0            0           0                 0      0            0             0


     Bit        23           22           21          20                19      18           17           16
                                                            GP[23:16]
  Access       R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset        0             0            0           0                 0      0            0             0


     Bit        15           14           13          12                11      10           9             8
                                                            GP[15:8]
  Access       R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset        0             0            0           0                 0      0            0             0


     Bit        7             6            5           4                 3      2            1             0
                                                             GP[7:0]
  Access       R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset        0             0            0           0                 0      0            0             0


           Bits 31:0 – GP[31:0] General Purpose
           These bits are for user-defined general purpose use, see 21.6.8.4 General Purpose Registers.




       © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 317
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                   RTC – Real-Time Counter

21.8.13 Tamper Control

           Name:         TAMPCTRL
           Offset:       0x60
           Reset:        0x00000000
           Property:     PAC Write-Protection, Enable-Protected


     Bit        31                 30        29                 28         27                 26          25                 24
                                                          DEBNC4        DEBNC3          DEBNC2          DEBNC1         DEBNC0
  Access
   Reset                                                        0          0                  0            0                 0


     Bit        23                 22        21                 20         19                 18          17                 16
                                                          TAMLVL4       TAMLVL3         TAMLVL2         TAMLVL1        TAMLVL0
  Access
   Reset                                                        0          0                  0            0                 0


     Bit        15                 14        13                 12         11                 10           9                 8
                                                                                                               IN4ACT[1:0]
  Access
   Reset                                                                                                   0                 0


     Bit        7                  6         5                  4          3                  2            1                 0
                     IN3ACT[1:0]                  IN2ACT[1:0]                   IN1ACT[1:0]                    IN0ACT[1:0]
  Access
   Reset        0                  0         0                  0          0                  0            0                 0


           Bits 24, 25, 26, 27, 28 – DEBNC Debounce Enable of Tamper Input INn
           Note: Debounce feature does not apply to the Active Layer Protection mode (TAMPCTRL.INACT =
           ACTL).
           Value         Description
           0             Debouncing is disabled for Tamper input INn
           1             Debouncing is enabled for Tamper input INn

           Bits 16, 17, 18, 19, 20 – TAMLVL Tamper Level Select of Tamper Input INn
           Note: Tamper Level feature does not apply to the Active Layer Protection mode (TAMPCTRL.INACT =
           ACTL).
           Value         Description
           0             A falling edge condition will be detected on Tamper input INn.
           1             A rising edge condition will be detected on Tamper input INn.

           Bits 0:1, 2:3, 4:5, 6:7, 8:9 – INACT Tamper Channel n Action
           These bits determine the action taken by Tamper Channel n.
            Value      Name          Description
            0x0        OFF           Off (Disabled)
            0x1        WAKE          Wake and set Tamper flag
            0x2        CAPTURE Capture timestamp and set Tamper flag




       © 2019 Microchip Technology Inc.                              Datasheet                             DS60001507E-page 318
                                                   SAM D5x/E5x Family Data Sheet
                                                                         RTC – Real-Time Counter

 Value        Name           Description
 0x3          ACTL           Compare RTC signal routed between INn and OUT pins . When a mismatch
                             occurs, capture timestamp and set Tamper flag




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 319
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  RTC – Real-Time Counter

21.8.14 Timestamp

           Name:       TIMESTAMP
           Offset:     0x64
           Reset:      0x0
           Property:   Read-Only


     Bit        31           30           29        28                 27    26          25           24
                                                         COUNT[31:24]
  Access       RO            RO           RO        RO                 RO   RO           RO          RO
   Reset        0             0           0          0                  0    0            0           0


     Bit        23           22           21        20                 19    18          17           16
                                                         COUNT[23:16]
  Access       RO            RO           RO        RO                 RO   RO           RO          RO
   Reset        0             0           0          0                  0    0            0           0


     Bit        15           14           13        12                 11    10           9           8
                                                         COUNT[15:8]
  Access       RO            RO           RO        RO                 RO   RO           RO          RO
   Reset        0             0           0          0                  0    0            0           0


     Bit        7             6           5          4                  3    2            1           0
                                                          COUNT[7:0]
  Access       RO            RO           RO        RO                 RO   RO           RO          RO
   Reset        0             0           0          0                  0    0            0           0


           Bits 31:0 – COUNT[31:0] Count Timestamp Value
           The 32-bit value of COUNT is captured by the TIMESTAMP when a tamper condition occurs




       © 2019 Microchip Technology Inc.                      Datasheet                    DS60001507E-page 320
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                               RTC – Real-Time Counter

21.8.15 Tamper ID

           Name:         TAMPID
           Offset:       0x68
           Reset:        0x00000000


     Bit         31            30             29             28             27            26             25           24
             TAMPEVT
  Access        R/W
   Reset         0


     Bit         23            22             21             20             19            18             17           16


  Access
   Reset


     Bit         15            14             13             12             11            10              9           8


  Access
   Reset


     Bit         7              6              5             4              3              2              1           0
                                                          TAMPID4       TAMPID3        TAMPID2        TAMPID1      TAMPID0
  Access                                                    R/W            R/W           R/W            R/W          R/W
   Reset                                                     0              0              0              0           0


           Bit 31 – TAMPEVT Tamper Event Detected
           Writing a '0' to this bit has no effect. Writing a '1' to this bit clears the tamper detection bit.
           Value         Description
           0             A tamper input event has not been detected
           1             A tamper input event has been detected

           Bits 0, 1, 2, 3, 4 – TAMPID Tamper on Channel n Detected
           Writing a '0' to this bit has no effect. Writing a '1' to this bit clears the tamper detection bit.
           Value         Description
           0             A tamper condition has not been detected on Channel n
           1             A tamper condition has been detected on Channel n




       © 2019 Microchip Technology Inc.                             Datasheet                             DS60001507E-page 321
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.8.16 Backup n

           Name:       BKUP
           Offset:     0x80 + n*0x04 [n=0..7]
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31           30           29           28                 27    26          25           24
                                                            BKUP[31:24]
  Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset        0             0            0           0                  0      0           0           0


     Bit        23           22           21           20                 19    18          17           16
                                                            BKUP[23:16]
  Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset        0             0            0           0                  0      0           0           0


     Bit        15           14           13           12                 11    10           9           8
                                                            BKUP[15:8]
  Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset        0             0            0           0                  0      0           0           0


     Bit        7             6            5           4                  3      2           1           0
                                                             BKUP[7:0]
  Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset        0             0            0           0                  0      0           0           0


           Bits 31:0 – BKUP[31:0] Backup
           These bits are user-defined for general purpose use in the Backup domain.




       © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 322
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                   RTC – Real-Time Counter


21.9      Register Summary - Mode 1 - 16-Bit Counter

 Offset        Name        Bit Pos.

                              7:0                                                              MODE[1:0]            ENABLE      SWRST
 0x00         CTRLA
                             15:8     COUNTSYNC    GPTRST     BKTRST                                       PRESCALER[3:0]
                              7:0      DMAEN       RTCOUT    DEBASYNC    DEBMAJ                                     GP2EN       GP0EN
 0x02         CTRLB
                             15:8                            ACTF[2:0]                                             DEBF[2:0]
                              7:0      PEREO7      PEREO6     PEREO5     PEREO4        PEREO3        PEREO2         PEREO1     PEREO0
                             15:8       OVFEO     TAMPEREO                             CMPEO3        CMPEO2         CMPEO1     CMPEO0
 0x04         EVCTRL
                             23:16                                                                                             TAMPEVEI
                             31:24
                              7:0       PER7        PER6       PER5       PER4              PER3       PER2          PER1       PER0
 0x08        INTENCLR
                             15:8        OVF       TAMPER                               CMP3          CMP2           CMP1       CMP0
                              7:0       PER7        PER6       PER5       PER4              PER3       PER2          PER1       PER0
 0x0A        INTENSET
                             15:8        OVF       TAMPER                               CMP3          CMP2           CMP1       CMP0
                              7:0       PER7        PER6       PER5       PER4              PER3       PER2          PER1       PER0
 0x0C        INTFLAG
                             15:8        OVF       TAMPER                               CMP3          CMP2           CMP1       CMP0
 0x0E        DBGCTRL          7:0                                                                                              DBGRUN
 0x0F        Reserved
                              7:0      COMP2       COMP1      COMP0       PER           COUNT       FREQCORR        ENABLE      SWRST
                             15:8     COUNTSYNC                                                                                 COMP3
 0x10       SYNCBUSY
                             23:16                                                          GP3        GP2            GP1        GP0
                             31:24
 0x14       FREQCORR          7:0       SIGN                                          VALUE[6:0]
 0x15
   ...       Reserved
 0x17
                              7:0                                            COUNT[7:0]
 0x18         COUNT
                             15:8                                           COUNT[15:8]
 0x1A
   ...       Reserved
 0x1B
                              7:0                                                PER[7:0]
 0x1C          PER
                             15:8                                               PER[15:8]
 0x1E
   ...       Reserved
 0x1F
                              7:0                                            COMP[7:0]
 0x20         COMP0
                             15:8                                            COMP[15:8]
                              7:0                                            COMP[7:0]
 0x22         COMP1
                             15:8                                            COMP[15:8]
                              7:0                                            COMP[7:0]
 0x24         COMP2
                             15:8                                            COMP[15:8]
                              7:0                                            COMP[7:0]
 0x26         COMP3
                             15:8                                            COMP[15:8]




          © 2019 Microchip Technology Inc.                            Datasheet                                    DS60001507E-page 323
                                                               SAM D5x/E5x Family Data Sheet
                                                                                               RTC – Real-Time Counter

...........continued

  Offset               Name     Bit Pos.

   0x28
     ...           Reserved
   0x3F
                                  7:0                                          GP[7:0]
                                 15:8                                         GP[15:8]
   0x40                 GP0
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
                                  7:0                                          GP[7:0]
                                 15:8                                         GP[15:8]
   0x44                 GP1
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
                                  7:0                                          GP[7:0]
                                 15:8                                         GP[15:8]
   0x48                 GP2
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
                                  7:0                                          GP[7:0]
                                 15:8                                         GP[15:8]
   0x4C                 GP3
                                 23:16                                        GP[23:16]
                                 31:24                                        GP[31:24]
   0x50
     ...           Reserved
   0x5F
                                  7:0            IN3ACT[1:0]   IN2ACT[1:0]                 IN1ACT[1:0]           IN0ACT[1:0]
                                 15:8                                                                            IN4ACT[1:0]
   0x60           TAMPCTRL
                                 23:16                                TAMLVL4       TAMLVL3       TAMLVL2   TAMLVL1     TAMLVL0
                                 31:24                                 DEBNC4        DEBNC3        DEBNC2   DEBNC1       DEBNC0
                                  7:0                                        COUNT[7:0]
                                 15:8                                        COUNT[15:8]
   0x64          TIMESTAMP
                                 23:16
                                 31:24
                                  7:0                                 TAMPID4       TAMPID3       TAMPID2   TAMPID1     TAMPID0
                                 15:8
   0x68                TAMPID
                                 23:16
                                 31:24     TAMPEVT
   0x6C
     ...           Reserved
   0x7F
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x80                BKUP0
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x84                BKUP1
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]




              © 2019 Microchip Technology Inc.                   Datasheet                                  DS60001507E-page 324
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x88                BKUP2
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x8C                BKUP3
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x90                BKUP4
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x94                BKUP5
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x98                BKUP6
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x9C                BKUP7
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]




21.10          Register Description - Mode 1 - 16-Bit Counter
               This Register Description section is valid if the RTC is in COUNT16 mode (CTRLA.MODE=1).
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 325
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             RTC – Real-Time Counter

21.10.1 Control A in COUNT16 mode (CTRLA.MODE=1)

           Name:       CTRLA
           Offset:     0x00
           Reset:      0x0000
           Property:   PAC Write-Protection, Enable-Protected, Write-Synchronized


     Bit        15            14            13           12           11                10           9           8
           COUNTSYNC       GPTRST         BKTRST                                        PRESCALER[3:0]
  Access       R/W           R/W           R/W                        R/W               R/W         R/W         R/W
   Reset         0            0             0                          0                 0           0           0


     Bit         7            6             5            4             3                 2           1           0
                                                                            MODE[1:0]              ENABLE      SWRST
  Access                                                              R/W               R/W         R/W         R/W
   Reset                                                               0                 0           0           0


           Bit 15 – COUNTSYNC COUNT Read Synchronization Enable
           The COUNT register requires synchronization when reading. Disabling the synchronization will prevent
           reading valid values from the COUNT register.
           This bit is not enable-protected.
            Value       Description
            0           COUNT read synchronization is disabled
            1           COUNT read synchronization is enabled

           Bit 14 – GPTRST GP Registers Reset On Tamper Enable
           Only GP registers enabled by the CTRLB.GPnEN bits are affected. This bit can be written only when the
           peripheral is disabled.
           This bit is not synchronized.
            Value       Description
            0           GPn registers will not reset when a tamper condition occurs.
            1           GPn registers will reset when a tamper condition occurs.

           Bit 13 – BKTRST BKUP Registers Reset On Tamper Enable
           All BKUPn registers are affected. This bit can be written only when the peripheral is disabled.
           This bit is not synchronized.
            Value       Description
            0           BKUPn registers will not reset when a tamper condition occurs.
            1           BKUPn registers will reset when a tamper condition occurs.

           Bits 11:8 – PRESCALER[3:0] Prescaler
           These bits define the prescaling factor for the RTC clock source (GCLK_RTC) to generate the counter
           clock (CLK_RTC_CNT). Periodic events and interrupts are not available when the prescaler is off. These
           bits are not synchronized.
            Value       Name               Description
            0x0         OFF                CLK_RTC_CNT = GCLK_RTC/1
            0x1         DIV1               CLK_RTC_CNT = GCLK_RTC/1
            0x2         DIV2               CLK_RTC_CNT = GCLK_RTC/2




       © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 326
                                                   SAM D5x/E5x Family Data Sheet
                                                                             RTC – Real-Time Counter

 Value        Name                 Description
 0x3          DIV4                 CLK_RTC_CNT = GCLK_RTC/4
 0x4          DIV8                 CLK_RTC_CNT = GCLK_RTC/8
 0x5          DIV16                CLK_RTC_CNT = GCLK_RTC/16
 0x6          DIV32                CLK_RTC_CNT = GCLK_RTC/32
 0x7          DIV64                CLK_RTC_CNT = GCLK_RTC/64
 0x8          DIV128               CLK_RTC_CNT = GCLK_RTC/128
 0x9          DIV256               CLK_RTC_CNT = GCLK_RTC/256
 0xA          DIV512               CLK_RTC_CNT = GCLK_RTC/512
 0xB          DIV1024              CLK_RTC_CNT = GCLK_RTC/1024
 0xC-0xF      -                    Reserved

Bits 3:2 – MODE[1:0] Operating Mode
This field defines the operating mode of the RTC. This bit is not synchronized.
 Value       Name                          Description
 0x0         COUNT32                       Mode 0: 32-bit counter
 0x1         COUNT16                       Mode 1: 16-bit counter
 0x2         CLOCK                         Mode 2: Clock/calendar
 0x3         -                             Reserved

Bit 1 – ENABLE Enable
Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately and the Enable bit in the
Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be cleared
when the operation is complete.
 Value      Description
 0          The peripheral is disabled
 1          The peripheral is enabled

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the RTC (except DBGCTRL) to their initial state, and the RTC
will be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
write-operation will be discarded.
Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
CTRLA.SWRST will be cleared when the reset is complete.
Value         Description
0             There is not reset operation ongoing
1             The reset operation is ongoing




© 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 327
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.10.2 Control B in COUNT16 mode (CTRLA.MODE=1)

           Name:       CTRLB
           Offset:     0x02
           Reset:      0x0000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        15           14              13         12           11            10            9            8
                                          ACTF[2:0]                                          DEBF[2:0]
  Access                     R/W            R/W        R/W                        R/W          R/W           R/W
   Reset                      0              0           0                         0             0            0


     Bit         7            6              5           4            3            2             1            0
              DMAEN        RTCOUT         DEBASYNC    DEBMAJ                                  GP2EN        GP0EN
  Access       R/W           R/W            R/W        R/W                                     R/W           R/W
   Reset         0            0              0           0                                       0            0


           Bits 14:12 – ACTF[2:0] Active Layer Frequency
           These bits define the prescaling factor for the RTC clock output (OUT) used during active layer protection
           in terms of the CLK_RTC.
            Value       Name              Description
            0x0         DIV2              CLK_RTC_OUT = CLK_RTC / 2
            0x1         DIV4              CLK_RTC_OUT = CLK_RTC / 4
            0x2         DIV8              CLK_RTC_OUT = CLK_RTC / 8
            0x3         DIV16             CLK_RTC_OUT = CLK_RTC / 16
            0x4         DIV32             CLK_RTC_OUT = CLK_RTC / 32
            0x5         DIV64             CLK_RTC_OUT = CLK_RTC / 64
            0x6         DIV128            CLK_RTC_OUT = CLK_RTC / 128
            0x7         DIV256            CLK_RTC_OUT = CLK_RTC / 256

           Bits 10:8 – DEBF[2:0] Debounce Frequency
           These bits define the prescaling factor for the input debouncers in terms of the CLK_RTC.
            Value      Name               Description
            0x0        DIV2               CLK_RTC_DEB = CLK_RTC / 2
            0x1        DIV4               CLK_RTC_DEB = CLK_RTC / 4
            0x2        DIV8               CLK_RTC_DEB = CLK_RTC / 8
            0x3        DIV16              CLK_RTC_DEB = CLK_RTC / 16
            0x4        DIV32              CLK_RTC_DEB = CLK_RTC / 32
            0x5        DIV64              CLK_RTC_DEB = CLK_RTC / 64
            0x6        DIV128             CLK_RTC_DEB = CLK_RTC / 128
            0x7        DIV256             CLK_RTC_DEB = CLK_RTC / 256

           Bit 7 – DMAEN DMA Enable
           The RTC can trigger a DMA request when the timestamp is ready in the TIMESTAMP register.
            Value     Description
            0         Tamper DMA request is disabled. Reading TIMESTAMP has no effect on
                      INTFLAG.TAMPER.
            1         Tamper DMA request is enabled. Reading TIMESTAMP will clear INTFLAG.TAMPER.




       © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 328
                                                SAM D5x/E5x Family Data Sheet
                                                                      RTC – Real-Time Counter

Bit 6 – RTCOUT RTC Output Enable
Value      Description
0          The RTC active layer output is disabled.
1          The RTC active layer output is enabled.

Bit 5 – DEBASYNC Debouncer Asynchronous Enable
Value      Description
0          The tamper input debouncers operate synchronously.
1          The tamper input debouncers operate asynchronously.

Bit 4 – DEBMAJ Debouncer Majority Enable
Value      Description
0          The tamper input debouncers match three equal values.
1          The tamper input debouncers match majority two of three values.

Bit 1 – GP2EN General Purpose 2 Enable
Value      Description
0          COMP1 compare function enabled. GP2/GP3 disabled.
1          COMP1 compare function disabled. GP2/GP3 enabled.

Bit 0 – GP0EN General Purpose 0 Enable
Value      Description
0          COMP0 compare function enabled. GP0/GP1 disabled.
1          COMP0 compare function disabled. GP0/GP1 enabled.




© 2019 Microchip Technology Inc.                 Datasheet                    DS60001507E-page 329
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.10.3 Event Control in COUNT16 mode (CTRLA.MODE=1)

           Name:       EVCTRL
           Offset:     0x04
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31            30            29          28            27           26            25              24


  Access
   Reset


     Bit        23            22            21          20            19           18            17              16
                                                                                                             TAMPEVEI
  Access                                                                                                        R/W
   Reset                                                                                                         0


     Bit        15            14            13          12            11           10            9               8
              OVFEO       TAMPEREO                                 CMPEO3       CMPEO2        CMPEO1          CMPEO0
  Access       R/W           R/W                                     R/W          R/W           R/W             R/W
   Reset         0            0                                       0             0            0               0


     Bit         7            6             5            4            3             2            1               0
             PEREO7        PEREO6         PEREO5      PEREO4       PEREO3       PEREO2        PEREO1          PEREO0
  Access       R/W           R/W           R/W          R/W          R/W          R/W           R/W             R/W
   Reset         0            0             0            0            0             0            0               0


           Bit 16 – TAMPEVEI Tamper Event Input Enable
           Value      Description
           0          Tamper event input is disabled, and incoming events will be ignored
           1          Tamper event input is enabled, and incoming events will capture the COUNT value

           Bit 15 – OVFEO Overflow Event Output Enable
           Value      Description
           0          Overflow event is disabled and will not be generated.
           1          Overflow event is enabled and will be generated for every overflow.

           Bit 14 – TAMPEREO Tamper Event Output Enable
           Value      Description
           0          Tamper event output is disabled, and will not be generated.
           1          Tamper event output is enabled, and will be generated for every tamper input.

           Bits 8, 9, 10, 11 – CMPEOn Compare n Event Output Enable [n = 3..0]
           Value        Description
           0            Compare n event is disabled and will not be generated.
           1            Compare n event is enabled and will be generated for every compare match.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PEREOn Periodic Interval n Event Output Enable [n = 7..0]




       © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 330
                                                    SAM D5x/E5x Family Data Sheet
                                                                             RTC – Real-Time Counter

 Value        Description
 0            Periodic Interval n event is disabled and will not be generated.
 1            Periodic Interval n event is enabled and will be generated.




© 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 331
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter

21.10.4 Interrupt Enable Clear in COUNT16 mode (CTRLA.MODE=1)

           Name:         INTENCLR
           Offset:       0x08
           Reset:        0x0000
           Property:     PAC Write-Protection

           This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
           in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

     Bit         15             14             13             12             11            10              9                 8
                OVF          TAMPER                                        CMP3           CMP2           CMP1           CMP0
  Access        R/W            R/W                                          R/W            R/W            R/W           R/W
   Reset         0              0                                            0              0              0                 0


     Bit         7              6              5              4              3              2              1                 0
               PER7           PER6           PER5           PER4           PER3           PER2           PER1           PER0
  Access        R/W            R/W            R/W            R/W            R/W            R/W            R/W           R/W
   Reset         0              0              0              0              0              0              0                 0


           Bit 15 – OVF Overflow Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Overflow Interrupt Enable bit,
           which disables the Overflow interrupt.
           Value         Description
           0             The Overflow interrupt is disabled.
           1             The Overflow interrupt is enabled.

           Bit 14 – TAMPER Tamper Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Tamper Interrupt Enable bit, which
           disables the Tamper interrupt.
            Value        Description
            0            The Tamper interrupt is disabled.
            1            The Tamper interrupt is enabled.

           Bits 8, 9, 10, 11 – CMPn Compare n Interrupt Enable [n = 3..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Compare n Interrupt Enable bit,
           which disables the Compare n interrupt.
           Value         Description
           0             The Compare n interrupt is disabled.
           1             The Compare n interrupt is enabled.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n Interrupt Enable [n = 7..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Periodic Interval n Interrupt
           Enable bit, which disables the Periodic Interval n interrupt.
           Value         Description
           0             Periodic Interval n interrupt is disabled.
           1             Periodic Interval n interrupt is enabled.




       © 2019 Microchip Technology Inc.                             Datasheet                              DS60001507E-page 332
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                               RTC – Real-Time Counter

21.10.5 Interrupt Enable Set in COUNT16 mode (CTRLA.MODE=1)

           Name:         INTENSET
           Offset:       0x0A
           Reset:        0x0000
           Property:     PAC Write-Protection

           This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
           in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

     Bit         15            14             13             12             11            10              9             8
                OVF         TAMPER                                        CMP3           CMP2          CMP1           CMP0
  Access        R/W            R/W                                         R/W            R/W           R/W            R/W
   Reset         0              0                                           0              0              0             0


     Bit         7              6              5              4             3              2              1             0
               PER7           PER6           PER5          PER4           PER3           PER2           PER1          PER0
  Access        R/W            R/W           R/W            R/W            R/W            R/W           R/W            R/W
   Reset         0              0              0              0             0              0              0             0


           Bit 15 – OVF Overflow Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Overflow Interrupt Enable bit, which
           enables the Overflow interrupt.
            Value        Description
            0            The Overflow interrupt is disabled.
            1            The Overflow interrupt is enabled.

           Bit 14 – TAMPER Tamper Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Tamper Interrupt Enable bit, which
           enables the Tamper interrupt.
            Value        Description
            0            The Tamper interrupt is disabled.
            1            The Tamper interrupt is enabled.

           Bits 8, 9, 10, 11 – CMPn Compare n Interrupt Enable [n = 3..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Compare n Interrupt Enable bit,
           which and enables the Compare n interrupt.
           Value         Description
           0             The Compare n interrupt is disabled.
           1             The Compare n interrupt is enabled.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n Interrupt Enable [n = 7..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Periodic Interval n Interrupt Enable
           bit, which enables the Periodic Interval n interrupt.
            Value        Description
            0            Periodic Interval n interrupt is disabled.
            1            Periodic Interval n interrupt is enabled.




       © 2019 Microchip Technology Inc.                            Datasheet                              DS60001507E-page 333
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

21.10.6 Interrupt Flag Status and Clear in COUNT16 mode (CTRLA.MODE=1)

           Name:        INTFLAG
           Offset:      0x0C
           Reset:       0x0000
           Property:    -


     Bit        15             14            13            12            11            10             9             8
                OVF         TAMPER                                     CMP3           CMP2          CMP1          CMP0
  Access        R/W           R/W                                       R/W           R/W            R/W           R/W
   Reset         0             0                                          0             0             0             0


     Bit         7             6             5             4              3             2             1             0
               PER7          PER6          PER5           PER4          PER3          PER2          PER1          PER0
  Access        R/W           R/W           R/W           R/W           R/W           R/W            R/W           R/W
   Reset         0             0             0             0              0             0             0             0


           Bit 15 – OVF Overflow
           This flag is cleared by writing a '1' to the flag.
           This flag is set on the next CLK_RTC_CNT cycle after an overflow condition occurs, and an interrupt
           request will be generated if INTENCLR/SET.OVF is '1'.
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Overflow interrupt flag.

           Bit 14 – TAMPER Tamper
           This flag is set after a tamper condition occurs, and an interrupt request will be generated if
           INTENCLR.TAMPER/ INTENSET.TAMPER is one.
           Writing a '0' to this bit has no effect.
           Writing a one to this bit clears the Tamper interrupt flag.

           Bits 8, 9, 10, 11 – CMPn Compare n [n = 3..0]
           This flag is cleared by writing a '1' to the flag.
           This flag is set on the next CLK_RTC_CNT cycle after a match with the compare condition, and an
           interrupt request will be generated if INTENCLR/SET.COMPn is one.
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Compare n interrupt flag.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n [n = 7..0]
           This flag is cleared by writing a '1' to the flag.
           This flag is set on the 0-to-1 transition of prescaler bit [n+2], and an interrupt request will be generated if
           INTENCLR/SET.PERx is one.
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Periodic Interval n interrupt flag.




       © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 334
                                                          SAM D5x/E5x Family Data Sheet
                                                                                    RTC – Real-Time Counter

21.10.7 Debug Control

           Name:       DBGCTRL
           Offset:     0x0E
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit        7             6           5           4            3            2            1           0
                                                                                                      DBGRUN
  Access                                                                                                R/W
   Reset                                                                                                 0


           Bit 0 – DBGRUN Debug Run
           This bit is not reset by a software reset.
           This bit controls the functionality when the CPU is halted by an external debugger.
            Value       Description
            0           The RTC is halted when the CPU is halted by an external debugger.
            1           The RTC continues normal operation when the CPU is halted by an external debugger.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 335
                                                            SAM D5x/E5x Family Data Sheet
                                                                                    RTC – Real-Time Counter

21.10.8 Synchronization Busy in COUNT16 mode (CTRLA.MODE=1)

           Name:       SYNCBUSY
           Offset:     0x10
           Reset:      0x00000000
           Property:   -


     Bit        31           30            29          28           27         26           25          24


  Access
   Reset


     Bit        23           22            21          20           19         18           17          16
                                                                   GP3        GP2          GP1         GP0
  Access                                                            R          R            R           R
   Reset                                                            0          0            0           0


     Bit        15           14            13          12           11         10           9           8
           COUNTSYNC                                                                                  COMP3
  Access        R                                                                                       R
   Reset         0                                                                                      0


     Bit         7            6             5           4           3          2            1           0
              COMP2        COMP1          COMP0       PER         COUNT     FREQCORR      ENABLE      SWRST
  Access        R             R            R           R            R          R            R           R
   Reset         0            0             0           0           0          0            0           0


           Bits 16, 17, 18, 19 – GPn General Purpose n Synchronization Busy Status
           Value       Description
           0           Write synchronization for GPn register is complete.
           1           Write synchronization for GPn register is ongoing.

           Bit 15 – COUNTSYNC Count Read Sync Enable Synchronization Busy Status
           Value      Description
           0          Write synchronization for CTRLA.COUNTSYNC bit is complete.
           1          Write synchronization for CTRLA.COUNTSYNC bit is ongoing.

           Bits 5, 6, 7, 8 – COMPn Compare n Synchronization Busy Status [n = 3..0]
           Value        Description
           0            Write synchronization for COMPn register is complete.
           1            Write synchronization for COMPn register is ongoing.

           Bit 4 – PER Period Synchronization Busy Status
           Value      Description
           0          Write synchronization for PER register is complete.
           1          Write synchronization for PER register is ongoing.

           Bit 3 – COUNT Count Value Synchronization Busy Status




       © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 336
                                                  SAM D5x/E5x Family Data Sheet
                                                                           RTC – Real-Time Counter

 Value        Description
 0            Read/write synchronization for COUNT register is complete.
 1            Read/write synchronization for COUNT register is ongoing.

Bit 2 – FREQCORR Frequency Correction Synchronization Busy Status
Value      Description
0          Write synchronization for FREQCORR register is complete.
1          Write synchronization for FREQCORR register is ongoing.

Bit 1 – ENABLE Enable Synchronization Busy Status
Value      Description
0          Write synchronization for CTRLA.ENABLE bit is complete.
1          Write synchronization for CTRLA.ENABLE bit is ongoing.

Bit 0 – SWRST Software Reset Synchronization Busy Status
Value      Description
0          Write synchronization for CTRLA.SWRST bit is complete.
1          Write synchronization for CTRLA.SWRST bit is ongoing.




© 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 337
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.10.9 Frequency Correction

           Name:       FREQCORR
           Offset:     0x14
           Reset:      0x00
           Property:   PAC Write-Protection, Write-Synchronized


     Bit         7            6             5            4             3            2           1           0
               SIGN                                               VALUE[6:0]
  Access       R/W           R/W          R/W           R/W          R/W           R/W         R/W         R/W
   Reset         0            0             0            0             0            0           0           0


           Bit 7 – SIGN Correction Sign
           Value      Description
           0          The correction value is positive, i.e., frequency will be decreased.
           1          The correction value is negative, i.e., frequency will be increased.

           Bits 6:0 – VALUE[6:0] Correction Value
           These bits define the amount of correction applied to the RTC prescaler.
            Value      Description
            0          Correction is disabled and the RTC frequency is unchanged.
            1 - 127 The RTC frequency is adjusted according to the value.




       © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 338
                                                            SAM D5x/E5x Family Data Sheet
                                                                                  RTC – Real-Time Counter

21.10.10 Counter Value in COUNT16 mode (CTRLA.MODE=1)

           Name:       COUNT
           Offset:     0x18
           Reset:      0x0000
           Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized


     Bit        15           14           13         12                 11   10           9           8
                                                          COUNT[15:8]
  Access       R/W          R/W           R/W       R/W             R/W      R/W         R/W         R/W
   Reset        0             0            0         0                  0     0           0           0


     Bit        7             6            5         4                  3     2           1           0
                                                          COUNT[7:0]
  Access       R/W          R/W           R/W       R/W             R/W      R/W         R/W         R/W
   Reset        0             0            0         0                  0     0           0           0


           Bits 15:0 – COUNT[15:0] Counter Value
           These bits define the value of the 16-bit RTC counter in COUNT16 mode (CTRLA.MODE=1).




       © 2019 Microchip Technology Inc.                      Datasheet                    DS60001507E-page 339
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  RTC – Real-Time Counter

21.10.11 Counter Period in COUNT16 mode (CTRLA.MODE=1)

           Name:       PER
           Offset:     0x1C
           Reset:      0x0000
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        15           14           13         12                11    10           9           8
                                                           PER[15:8]
  Access       R/W          R/W           R/W        R/W               R/W   R/W         R/W         R/W
   Reset        0             0            0          0                 0     0           0           0


     Bit        7             6            5          4                 3     2           1           0
                                                           PER[7:0]
  Access       R/W          R/W           R/W        R/W               R/W   R/W         R/W         R/W
   Reset        0             0            0          0                 0     0           0           0


           Bits 15:0 – PER[15:0] Counter Period
           These bits define the value of the 16-bit RTC period in COUNT16 mode (CTRLA.MODE=1).




       © 2019 Microchip Technology Inc.                      Datasheet                    DS60001507E-page 340
                                                              SAM D5x/E5x Family Data Sheet
                                                                                       RTC – Real-Time Counter

21.10.12 Compare n Value in COUNT16 mode (CTRLA.MODE=1)

           Name:       COMP
           Offset:     0x20 + n*0x02 [n=0..3]
           Reset:      0x0000
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        15           14           13           12                11       10           9            8
                                                            COMP[15:8]
  Access       R/W          R/W           R/W          R/W               R/W     R/W          R/W          R/W
   Reset         0            0            0            0                 0       0            0            0


     Bit         7            6            5            4                 3       2            1            0
                                                             COMP[7:0]
  Access       R/W          R/W           R/W          R/W               R/W     R/W          R/W          R/W
   Reset         0            0            0            0                 0       0            0            0


           Bits 15:0 – COMP[15:0] Compare Value
           The 16-bit value of COMPn is continuously compared with the 16-bit COUNT value. When a match
           occurs, the Compare n interrupt flag in the Interrupt Flag Status and Clear register (INTFLAG.CMPn) is
           set on the next counter cycle.




       © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 341
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      RTC – Real-Time Counter

21.10.13 General Purpose n

            Name:       GPn
            Offset:     0x40 + n*0x04 [n=0..3]
            Reset:      0x00000000
            Property:   -


      Bit        31           30           29          28                27      26           25           24
                                                             GP[31:24]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


      Bit        23           22           21          20                19      18           17           16
                                                             GP[23:16]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


      Bit        15           14           13          12                11      10           9             8
                                                             GP[15:8]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


      Bit        7             6            5           4                 3      2            1             0
                                                              GP[7:0]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


            Bits 31:0 – GP[31:0] General Purpose
            These bits are for user-defined general purpose use, see 21.6.8.4 General Purpose Registers.




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 342
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                    RTC – Real-Time Counter

21.10.14 Tamper Control

            Name:         TAMPCTRL
            Offset:       0x60
            Reset:        0x00000000
            Property:     PAC Write-Protection, Enable-Protected


      Bit        31                 30        29                 28         27                 26          25                 24
                                                           DEBNC4        DEBNC3          DEBNC2          DEBNC1         DEBNC0
  Access
   Reset                                                         0          0                  0            0                 0


      Bit        23                 22        21                 20         19                 18          17                 16
                                                           TAMLVL4       TAMLVL3         TAMLVL2         TAMLVL1        TAMLVL0
  Access
   Reset                                                         0          0                  0            0                 0


      Bit        15                 14        13                 12         11                 10           9                 8
                                                                                                                IN4ACT[1:0]
  Access
   Reset                                                                                                    0                 0


      Bit        7                  6         5                  4          3                  2            1                 0
                      IN3ACT[1:0]                  IN2ACT[1:0]                   IN1ACT[1:0]                    IN0ACT[1:0]
  Access
   Reset         0                  0         0                  0          0                  0            0                 0


            Bits 24, 25, 26, 27, 28 – DEBNC Debounce Enable of Tamper Input INn
            Note: Debounce feature does not apply to the Active Layer Protection mode (TAMPCTRL.INACT =
            ACTL).
            Value         Description
            0             Debouncing is disabled for Tamper input INn
            1             Debouncing is enabled for Tamper input INn

            Bits 16, 17, 18, 19, 20 – TAMLVL Tamper Level Select of Tamper Input INn
            Note: Tamper Level feature does not apply to the Active Layer Protection mode (TAMPCTRL.INACT =
            ACTL).
            Value         Description
            0             A falling edge condition will be detected on Tamper input INn.
            1             A rising edge condition will be detected on Tamper input INn.

            Bits 0:1, 2:3, 4:5, 6:7, 8:9 – INACT Tamper Channel n Action
            These bits determine the action taken by Tamper Channel n.
             Value      Name          Description
             0x0        OFF           Off (Disabled)
             0x1        WAKE          Wake and set Tamper flag
             0x2        CAPTURE Capture timestamp and set Tamper flag




        © 2019 Microchip Technology Inc.                              Datasheet                             DS60001507E-page 343
                                                   SAM D5x/E5x Family Data Sheet
                                                                         RTC – Real-Time Counter

 Value        Name           Description
 0x3          ACTL           Compare RTC signal routed between INn and OUT pins . When a mismatch
                             occurs, capture timestamp and set Tamper flag




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 344
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  RTC – Real-Time Counter

21.10.15 Timestamp

           Name:       TIMESTAMP
           Offset:     0x64
           Reset:      0x0000
           Property:   Read-Only


     Bit        31           30           29        28                 27    26          25           24


  Access
   Reset


     Bit        23           22           21        20                 19    18          17           16


  Access
   Reset


     Bit        15           14           13        12                 11    10           9           8
                                                         COUNT[15:8]
  Access        R             R           R          R                 R     R            R           R
   Reset        0             0           0          0                 0     0            0           0


     Bit        7             6           5          4                 3     2            1           0
                                                         COUNT[7:0]
  Access        R             R           R          R                 R     R            R           R
   Reset        0             0           0          0                 0     0            0           0


           Bits 15:0 – COUNT[15:0] Count Timestamp Value
           The 16-bit value of COUNT is captured by the TIMESTAMP when a tamper condition occurs.




       © 2019 Microchip Technology Inc.                     Datasheet                     DS60001507E-page 345
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter

21.10.16 Tamper ID

            Name:         TAMPID
            Offset:       0x68
            Reset:        0x00000000


      Bit         31            30             29             28             27            26             25           24
              TAMPEVT
  Access         R/W
   Reset          0


      Bit         23            22             21             20             19            18             17           16


  Access
   Reset


      Bit         15            14             13             12             11            10              9           8


  Access
   Reset


      Bit         7              6              5             4              3              2              1           0
                                                           TAMPID4       TAMPID3        TAMPID2        TAMPID1      TAMPID0
  Access                                                     R/W            R/W           R/W            R/W          R/W
   Reset                                                      0              0              0              0           0


            Bit 31 – TAMPEVT Tamper Event Detected
            Writing a '0' to this bit has no effect. Writing a '1' to this bit clears the tamper detection bit.
            Value         Description
            0             A tamper input event has not been detected
            1             A tamper input event has been detected

            Bits 0, 1, 2, 3, 4 – TAMPID Tamper on Channel n Detected
            Writing a '0' to this bit has no effect. Writing a '1' to this bit clears the tamper detection bit.
            Value         Description
            0             A tamper condition has not been detected on Channel n
            1             A tamper condition has been detected on Channel n




        © 2019 Microchip Technology Inc.                             Datasheet                             DS60001507E-page 346
                                                              SAM D5x/E5x Family Data Sheet
                                                                                      RTC – Real-Time Counter

21.10.17 Backup n

            Name:       BKUP
            Offset:     0x80 + n*0x04 [n=0..7]
            Reset:      0x00000000
            Property:   PAC Write-Protection


      Bit        31           30           29           28                 27    26          25           24
                                                             BKUP[31:24]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


      Bit        23           22           21           20                 19    18          17           16
                                                             BKUP[23:16]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


      Bit        15           14           13           12                 11    10           9           8
                                                             BKUP[15:8]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


      Bit        7             6            5           4                  3      2           1           0
                                                              BKUP[7:0]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


            Bits 31:0 – BKUP[31:0] Backup
            These bits are user-defined for general purpose use in the Backup domain.




        © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 347
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                   RTC – Real-Time Counter


21.11     Register Summary - Mode 2 - Clock/Calendar

 Offset        Name        Bit Pos.

                              7:0     MATCHCLR      CLKREP                                  MODE[1:0]            ENABLE       SWRST
 0x00         CTRLA
                             15:8     CLOCKSYNC     GPTRST       BKTRST                                 PRESCALER[3:0]
                              7:0      DMAEN        RTCOUT      DEBASYNC     DEBMAJ                              GP2EN        GP0EN
 0x02         CTRLB
                             15:8                                ACTF[2:0]                                      DEBF[2:0]
                              7:0      PEREO7       PEREO6       PEREO5      PEREO4    PEREO3       PEREO2       PEREO1       PEREO0
                             15:8      OVFEO       TAMPEREO                                                     ALARMEO1     ALARMEO0
 0x04         EVCTRL
                             23:16                                                                                           TAMPEVEI
                             31:24
                              7:0       PER7          PER6         PER5        PER4     PER3         PER2         PER1         PER0
 0x08        INTENCLR
                             15:8        OVF        TAMPER                                                       ALARM1       ALARM0
                              7:0       PER7          PER6         PER5        PER4     PER3         PER2         PER1         PER0
 0x0A        INTENSET
                             15:8        OVF        TAMPER                                                       ALARM1       ALARM0
                              7:0       PER7          PER6         PER5        PER4     PER3         PER2         PER1         PER0
 0x0C        INTFLAG
                             15:8        OVF        TAMPER                                                       ALARM1       ALARM0
 0x0E        DBGCTRL          7:0                                                                                             DBGRUN
 0x0F        Reserved
                              7:0                   ALARM1       ALARM0                CLOCK       FREQCORR      ENABLE       SWRST
                             15:8     CLOCKSYNC                               MASK1    MASK0
 0x10       SYNCBUSY
                             23:16                                                       GP3         GP2           GP1          GP0
                             31:24
 0x14       FREQCORR          7:0       SIGN                                          VALUE[6:0]
 0x15
   ...       Reserved
 0x17
                              7:0            MINUTE[1:0]                                   SECOND[5:0]
                             15:8                          HOUR[3:0]                                     MINUTE[5:2]
 0x18         CLOCK
                             23:16           MONTH[1:0]                                DAY[4:0]                              HOUR[4:4]
                             31:24                                     YEAR[5:0]                                       MONTH[3:2]
 0x1C
   ...       Reserved
 0x1F
                              7:0            MINUTE[1:0]                                   SECOND[5:0]
                             15:8                          HOUR[3:0]                                     MINUTE[5:2]
 0x20         ALARM0
                             23:16           MONTH[1:0]                                DAY[4:0]                              HOUR[4:4]
                             31:24                                     YEAR[5:0]                                       MONTH[3:2]
 0x24         MASK0           7:0                                                                                SEL[2:0]
 0x25
   ...       Reserved
 0x27
                              7:0            MINUTE[1:0]                                   SECOND[5:0]
                             15:8                          HOUR[3:0]                                     MINUTE[5:2]
 0x28         ALARM1
                             23:16           MONTH[1:0]                                DAY[4:0]                              HOUR[4:4]
                             31:24                                     YEAR[5:0]                                       MONTH[3:2]




          © 2019 Microchip Technology Inc.                                Datasheet                             DS60001507E-page 348
                                                                           SAM D5x/E5x Family Data Sheet
                                                                                                            RTC – Real-Time Counter

...........continued

  Offset               Name     Bit Pos.

   0x2C                MASK1      7:0                                                                                        SEL[2:0]
   0x2D
     ...           Reserved
   0x3F
                                  7:0                                                      GP[7:0]
                                 15:8                                                     GP[15:8]
   0x40                 GP0
                                 23:16                                                    GP[23:16]
                                 31:24                                                    GP[31:24]
                                  7:0                                                      GP[7:0]
                                 15:8                                                     GP[15:8]
   0x44                 GP1
                                 23:16                                                    GP[23:16]
                                 31:24                                                    GP[31:24]
                                  7:0                                                      GP[7:0]
                                 15:8                                                     GP[15:8]
   0x48                 GP2
                                 23:16                                                    GP[23:16]
                                 31:24                                                    GP[31:24]
                                  7:0                                                      GP[7:0]
                                 15:8                                                     GP[15:8]
   0x4C                 GP3
                                 23:16                                                    GP[23:16]
                                 31:24                                                    GP[31:24]
   0x50
     ...           Reserved
   0x5F
                                  7:0            IN3ACT[1:0]               IN2ACT[1:0]                 IN1ACT[1:0]                 IN0ACT[1:0]
                                 15:8                                                                                              IN4ACT[1:0]
   0x60           TAMPCTRL
                                 23:16                                            TAMLVL4       TAMLVL3       TAMLVL2       TAMLVL1       TAMLVL0
                                 31:24                                             DEBNC4        DEBNC3        DEBNC2       DEBNC1         DEBNC0
                                  7:0            MINUTE[1:0]                                           SECOND[5:0]
                                 15:8                          HOUR[3:0]                                             MINUTE[5:2]
   0x64          TIMESTAMP
                                 23:16           MONTH[1:0]                                      DAY[4:0]                                 HOUR[4:4]
                                 31:24                                     YEAR[5:0]                                               MONTH[3:2]
                                  7:0                                             TAMPID4       TAMPID3       TAMPID2       TAMPID1       TAMPID0
                                 15:8
   0x68                TAMPID
                                 23:16
                                 31:24     TAMPEVT
   0x6C
     ...           Reserved
   0x7F
                                  7:0                                                     BKUP[7:0]
                                 15:8                                                    BKUP[15:8]
   0x80                BKUP0
                                 23:16                                                   BKUP[23:16]
                                 31:24                                                   BKUP[31:24]




              © 2019 Microchip Technology Inc.                               Datasheet                                     DS60001507E-page 349
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            RTC – Real-Time Counter

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x84                BKUP1
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x88                BKUP2
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x8C                BKUP3
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x90                BKUP4
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x94                BKUP5
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x98                BKUP6
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]
                                  7:0                                         BKUP[7:0]
                                 15:8                                        BKUP[15:8]
   0x9C                BKUP7
                                 23:16                                       BKUP[23:16]
                                 31:24                                       BKUP[31:24]




21.12          Register Description - Mode 2 - Clock/Calendar
               This Register Description section is valid if the RTC is in Clock/Calendar mode (CTRLA.MODE=2).
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 350
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             RTC – Real-Time Counter

21.12.1 Control A in Clock/Calendar mode (CTRLA.MODE=2)

           Name:        CTRLA
           Offset:      0x00
           Reset:       0x0000
           Property:    PAC Write-Protection, Enable-Protected, Write-Synchronized


     Bit        15            14            13           12           11                10           9           8
            CLOCKSYNC      GPTRST         BKTRST                                        PRESCALER[3:0]
  Access       R/W           R/W           R/W                        R/W               R/W         R/W         R/W
   Reset         0            0             0                          0                 0           0           0


     Bit         7            6             5            4             3                 2           1           0
            MATCHCLR       CLKREP                                           MODE[1:0]              ENABLE      SWRST
  Access       R/W           R/W                                      R/W               R/W         R/W         R/W
   Reset         0            0                                        0                 0           0           0


           Bit 15 – CLOCKSYNC CLOCK Read Synchronization Enable
           The CLOCK register requires synchronization when reading. Disabling the synchronization will prevent
           reading valid values from the CLOCK register.
           This bit is not enable-protected.
            Value       Description
            0           CLOCK read synchronization is disabled
            1           CLOCK read synchronization is enabled

           Bit 14 – GPTRST GP Registers Reset On Tamper Enable
           Only GP registers enabled by the CTRLB.GPnEN bits are affected. This bit can be written only when the
           peripheral is disabled.
           This bit is not synchronized.

           Bit 13 – BKTRST BKUP Registers Reset On Tamper Enable
           All BKUPn registers are affected. This bit can be written only when the peripheral is disabled.
           This bit is not synchronized.
            Value       Description
            0           BKUPn registers will not reset when a tamper condition occurs.
            1           BKUPn registers will reset when a tamper condition occurs.

           Bits 11:8 – PRESCALER[3:0] Prescaler
           These bits define the prescaling factor for the RTC clock source (GCLK_RTC) to generate the counter
           clock (CLK_RTC_CNT). Periodic events and interrupts are not available when the prescaler is off. These
           bits are not synchronized.
            Value       Name               Description
            0x0         OFF                CLK_RTC_CNT = GCLK_RTC/1
            0x1         DIV1               CLK_RTC_CNT = GCLK_RTC/1
            0x2         DIV2               CLK_RTC_CNT = GCLK_RTC/2
            0x3         DIV4               CLK_RTC_CNT = GCLK_RTC/4
            0x4         DIV8               CLK_RTC_CNT = GCLK_RTC/8
            0x5         DIV16              CLK_RTC_CNT = GCLK_RTC/16




       © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 351
                                                   SAM D5x/E5x Family Data Sheet
                                                                             RTC – Real-Time Counter

 Value        Name                 Description
 0x6          DIV32                CLK_RTC_CNT = GCLK_RTC/32
 0x7          DIV64                CLK_RTC_CNT = GCLK_RTC/64
 0x8          DIV128               CLK_RTC_CNT = GCLK_RTC/128
 0x9          DIV256               CLK_RTC_CNT = GCLK_RTC/256
 0xA          DIV512               CLK_RTC_CNT = GCLK_RTC/512
 0xB          DIV1024              CLK_RTC_CNT = GCLK_RTC/1024
 0xC-0xF      -                    Reserved

Bit 7 – MATCHCLR Clear on Match
This bit is valid only in Mode 0 (COUNT32) and Mode 2 (CLOCK). This bit can be written only when the
peripheral is disabled. This bit is not synchronized.
 Value        Description
 0            The counter is not cleared on a Compare/Alarm 0 match
 1            The counter is cleared on a Compare/Alarm 0 match

Bit 6 – CLKREP Clock Representation
This bit is valid only in Mode 2 and determines how the hours are represented in the Clock Value
(CLOCK) register. This bit can be written only when the peripheral is disabled. This bit is not
synchronized.
 Value        Description
 0            24 Hour
 1            12 Hour (AM/PM)

Bits 3:2 – MODE[1:0] Operating Mode
This field defines the operating mode of the RTC. This bit is not synchronized.
 Value       Name                          Description
 0x0         COUNT32                       Mode 0: 32-bit counter
 0x1         COUNT16                       Mode 1: 16-bit counter
 0x2         CLOCK                         Mode 2: Clock/calendar
 0x3         -                             Reserved

Bit 1 – ENABLE Enable
Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRLA.ENABLE will read back immediately and the Enable bit in the
Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be cleared
when the operation is complete.
 Value      Description
 0          The peripheral is disabled
 1          The peripheral is enabled

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the RTC, except DBGCTRL, to their initial state, and the RTC
will be disabled.
Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
write-operation will be discarded.
Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
CTRLA.SWRST will be cleared when the reset is complete.




© 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 352
                                                     SAM D5x/E5x Family Data Sheet
                                                                 RTC – Real-Time Counter

 Value        Description
 0            There is not reset operation ongoing
 1            The reset operation is ongoing




© 2019 Microchip Technology Inc.                     Datasheet           DS60001507E-page 353
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.12.2 Control B in Clock/Calendar mode (CTRLA.MODE=2)

           Name:       CTRLB
           Offset:     0x2
           Reset:      0x0000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        15           14              13         12           11            10            9            8
                                          ACTF[2:0]                                          DEBF[2:0]
  Access                     R/W            R/W        R/W                        R/W          R/W           R/W
   Reset                      0              0           0                         0             0            0


     Bit         7            6              5           4            3            2             1            0
              DMAEN        RTCOUT         DEBASYNC    DEBMAJ                                  GP2EN        GP0EN
  Access       R/W           R/W            R/W        R/W                                     R/W           R/W
   Reset         0            0              0           0                                       0            0


           Bits 14:12 – ACTF[2:0] Active Layer Frequency
           These bits define the prescaling factor for the RTC clock output (OUT) used during active layer protection
           in terms of the CLK_RTC.
            Value       Name              Description
            0x0         DIV2              CLK_RTC_OUT = CLK_RTC / 2
            0x1         DIV4              CLK_RTC_OUT = CLK_RTC / 4
            0x2         DIV8              CLK_RTC_OUT = CLK_RTC / 8
            0x3         DIV16             CLK_RTC_OUT = CLK_RTC / 16
            0x4         DIV32             CLK_RTC_OUT = CLK_RTC / 32
            0x5         DIV64             CLK_RTC_OUT = CLK_RTC / 64
            0x6         DIV128            CLK_RTC_OUT = CLK_RTC / 128
            0x7         DIV256            CLK_RTC_OUT = CLK_RTC / 256

           Bits 10:8 – DEBF[2:0] Debounce Frequency
           These bits define the prescaling factor for the input debouncers in terms of the CLK_RTC.
            Value      Name               Description
            0x0        DIV2               CLK_RTC_DEB = CLK_RTC / 2
            0x1        DIV4               CLK_RTC_DEB = CLK_RTC / 4
            0x2        DIV8               CLK_RTC_DEB = CLK_RTC / 8
            0x3        DIV16              CLK_RTC_DEB = CLK_RTC / 16
            0x4        DIV32              CLK_RTC_DEB = CLK_RTC / 32
            0x5        DIV64              CLK_RTC_DEB = CLK_RTC / 64
            0x6        DIV128             CLK_RTC_DEB = CLK_RTC / 128
            0x7        DIV256             CLK_RTC_DEB = CLK_RTC / 256

           Bit 7 – DMAEN DMA Enable
           The RTC can trigger a DMA request when the timestamp is ready in the TIMESTAMP register.
            Value     Description
            0         Tamper DMA request is disabled. Reading TIMESTAMP has no effect on
                      INTFLAG.TAMPER.
            1         Tamper DMA request is enabled. Reading TIMESTAMP will clear INTFLAG.TAMPER.




       © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 354
                                                SAM D5x/E5x Family Data Sheet
                                                                      RTC – Real-Time Counter

Bit 6 – RTCOUT RTC Out Enable
Value      Description
0          The RTC active layer output is disabled.
1          The RTC active layer output is enabled.

Bit 5 – DEBASYNC Debouncer Asynchronous Enable
Value      Description
0          The tamper input debouncers operate synchronously.
1          The tamper input debouncers operate asynchronously.

Bit 4 – DEBMAJ Debouncer Majority Enable
Value      Description
0          The tamper input debouncers match three equal values.
1          The tamper input debouncers match majority two of three values.

Bit 1 – GP2EN General Purpose 2 Enable
Value      Description
0          COMP1 compare function enabled. GP2/GP3 disabled.
1          COMP1 compare function disabled. GP2/GP3 enabled.

Bit 0 – GP0EN General Purpose 0 Enable
Value      Description
0          COMP0 compare function enabled. GP0 disabled.
1          COMP0 compare function disabled. GP0 enabled.




© 2019 Microchip Technology Inc.                 Datasheet                    DS60001507E-page 355
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.12.3 Event Control in Clock/Calendar mode (CTRLA.MODE=2)

           Name:       EVCTRL
           Offset:     0x04
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31            30            29          28            27           26            25              24


  Access
   Reset


     Bit        23            22            21          20            19           18            17              16
                                                                                                             TAMPEVEI
  Access                                                                                                        R/W
   Reset                                                                                                         0


     Bit        15            14            13          12            11           10             9              8
              OVFEO       TAMPEREO                                                           ALARMEO1        ALARMEO0
  Access       R/W           R/W                                                                R/W             R/W
   Reset         0            0                                                                   0              0


     Bit         7            6             5            4            3             2             1              0
             PEREO7        PEREO6         PEREO5      PEREO4       PEREO3       PEREO2        PEREO1          PEREO0
  Access       R/W           R/W           R/W          R/W          R/W          R/W           R/W             R/W
   Reset         0            0             0            0            0             0             0              0


           Bit 16 – TAMPEVEI Tamper Event Input Enable
           Value      Description
           0          Tamper event input is disabled, and incoming events will be ignored.
           1          Tamper event input is enabled, and all incoming events will capture the CLOCK value.

           Bit 15 – OVFEO Overflow Event Output Enable
           Value      Description
           0          Overflow event is disabled and will not be generated.
           1          Overflow event is enabled and will be generated for every overflow.

           Bit 14 – TAMPEREO Tamper Event Output Enable
           Value      Description
           0          Tamper event output is disabled, and will not be generated
           1          Tamper event output is enabled, and will be generated for every tamper input.

           Bits 8, 9 – ALARMEOn Alarm n Event Output Enable [n = 1..0]
           Value       Description
           0            Alarm n event is disabled and will not be generated.
           1            Alarm n event is enabled and will be generated for every compare match.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PEREOn Periodic Interval n Event Output Enable [n = 7..0]




       © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 356
                                                    SAM D5x/E5x Family Data Sheet
                                                                             RTC – Real-Time Counter

 Value        Description
 0            Periodic Interval n event is disabled and will not be generated.
 1            Periodic Interval n event is enabled and will be generated.




© 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 357
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter

21.12.4 Interrupt Enable Clear in Clock/Calendar mode (CTRLA.MODE=2)

           Name:         INTENCLR
           Offset:       0x08
           Reset:        0x0000
           Property:     PAC Write-Protection

           This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
           in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

     Bit         15             14             13             12             11            10              9                 8
                OVF          TAMPER                                                                    ALARM1         ALARM0
  Access        R/W            R/W                                                                        R/W           R/W
   Reset         0              0                                                                          0                 0


     Bit         7              6              5              4              3              2              1                 0
               PER7           PER6           PER5           PER4           PER3           PER2           PER1           PER0
  Access        R/W            R/W            R/W            R/W            R/W            R/W            R/W           R/W
   Reset         0              0              0              0              0              0              0                 0


           Bit 15 – OVF Overflow Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Overflow Interrupt Enable bit,
           which disables the Overflow interrupt.
           Value         Description
           0             The Overflow interrupt is disabled.
           1             The Overflow interrupt is enabled.

           Bit 14 – TAMPER Tamper Interrupt Enable

           Bits 8, 9 – ALARMn Alarm n Interrupt Enable [n = 1..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Alarm n Interrupt Enable bit, which
           disables the Alarm n interrupt.
            Value        Description
            0            The Alarm n interrupt is disabled.
            1            The Alarm n interrupt is enabled.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n Interrupt Enable [n = 7..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Periodic Interval n Interrupt
           Enable bit, which disables the Periodic Interval n interrupt.
           Value         Description
           0             Periodic Interval n interrupt is disabled.
           1             Periodic Interval n interrupt is enabled.




       © 2019 Microchip Technology Inc.                             Datasheet                              DS60001507E-page 358
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                               RTC – Real-Time Counter

21.12.5 Interrupt Enable Set in Clock/Calendar mode (CTRLA.MODE=2)

           Name:         INTENSET
           Offset:       0x0A
           Reset:        0x0000
           Property:     PAC Write-Protection

           This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
           in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

     Bit         15            14             13             12             11            10              9             8
                OVF         TAMPER                                                                    ALARM1         ALARM0
  Access        R/W            R/W                                                                      R/W            R/W
   Reset         0              0                                                                         0             0


     Bit         7              6              5              4             3              2              1             0
               PER7           PER6           PER5          PER4           PER3           PER2           PER1          PER0
  Access        R/W            R/W           R/W            R/W            R/W            R/W           R/W            R/W
   Reset         0              0              0              0             0              0              0             0


           Bit 15 – OVF Overflow Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Overflow Interrupt Enable bit, which
           enables the Overflow interrupt.
            Value        Description
            0            The Overflow interrupt is disabled.
            1            The Overflow interrupt is enabled.

           Bit 14 – TAMPER Tamper Interrupt Enable
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Tamper Interrupt Enable bit, which
           enables the Tamper interrupt.
            Value        Description
            0            The Tamper interrupt it disabled.
            1            The Tamper interrupt is enabled.

           Bits 8, 9 – ALARMn Alarm n Interrupt Enable [n = 1..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Alarm n Interrupt Enable bit, which
           and enables the Alarm n interrupt.
            Value        Description
            0            The Alarm n interrupt is disabled.
            1            The Alarm n interrupt is enabled.

           Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n Interrupt Enable [n = 7..0]
           Writing a '0' to this bit has no effect. Writing a '1' to this bit will set the Periodic Interval n Interrupt Enable
           bit, which enables the Periodic Interval n interrupt.
            Value        Description
            0            Periodic Interval n interrupt is disabled.
            1            Periodic Interval n interrupt is enabled.




       © 2019 Microchip Technology Inc.                            Datasheet                              DS60001507E-page 359
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                             RTC – Real-Time Counter

21.12.6 Interrupt Flag Status and Clear in Clock/Calendar mode (CTRLA.MODE=2)

            Name:        INTFLAG
            Offset:      0x0C
            Reset:       0x0000
            Property:    -


      Bit        15             14            13            12            11            10             9             8
                 OVF         TAMPER                                                                 ALARM1        ALARM0
  Access         R/W           R/W                                                                    R/W           R/W
   Reset          0             0                                                                      0             0


      Bit         7             6             5             4              3             2             1             0
                PER7          PER6          PER5           PER4          PER3          PER2          PER1          PER0
  Access         R/W           R/W           R/W           R/W           R/W           R/W            R/W           R/W
   Reset          0             0             0             0              0             0             0             0


            Bit 15 – OVF Overflow
            This flag is cleared by writing a '1' to the flag.
            This flag is set on the next CLK_RTC_CNT cycle after an overflow condition occurs, and an interrupt
            request will be generated if INTENCLR/SET.OVF is '1'.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Overflow interrupt flag.

            Bit 14 – TAMPER Tamper
            This flag is set after a tamper condition occurs, and an interrupt request will be generated if
            INTENCLR.TAMPER/INTENSET.TAMPER is '1'. Writing a '0' to this bit has no effect. Writing a '1' to this
            bit clears the Tamper interrupt flag.

            Bits 8, 9 – ALARMn Alarm n [n = 1..0]
            This flag is cleared by writing a '1' to the flag.
            This flag is set on the next CLK_RTC_CNT cycle after a match with the compare condition, and an
            interrupt request will be generated if INTENCLR/SET.ALARMn is one.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Alarm n interrupt flag.

            Bits 0, 1, 2, 3, 4, 5, 6, 7 – PERn Periodic Interval n [n = 7..0]
            This flag is cleared by writing a '1' to the flag.
            This flag is set on the 0-to-1 transition of prescaler bit [n+2], and an interrupt request will be generated if
            INTENCLR/SET.PERx is '1'.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Periodic Interval n interrupt flag.




        © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 360
                                                          SAM D5x/E5x Family Data Sheet
                                                                                    RTC – Real-Time Counter

21.12.7 Debug Control

           Name:       DBGCTRL
           Offset:     0x0E
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit        7             6           5           4            3            2            1           0
                                                                                                      DBGRUN
  Access                                                                                                R/W
   Reset                                                                                                 0


           Bit 0 – DBGRUN Debug Run
           This bit is not reset by a software reset.
           This bit controls the functionality when the CPU is halted by an external debugger.
            Value       Description
            0           The RTC is halted when the CPU is halted by an external debugger.
            1           The RTC continues normal operation when the CPU is halted by an external debugger.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 361
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      RTC – Real-Time Counter

21.12.8 Synchronization Busy in Clock/Calendar mode (CTRLA.MODE=2)

           Name:       SYNCBUSY
           Offset:     0x10
           Reset:      0x00000000
           Property:   -


     Bit        31           30             29         28           27           26           25          24


  Access
   Reset


     Bit        23           22             21         20           19           18           17          16
                                                                   GP3           GP2         GP1         GP0
  Access                                                            R            R            R           R
   Reset                                                            0             0           0           0


     Bit        15           14             13         12           11           10           9           8
           CLOCKSYNC                                 MASK1        MASK0
  Access        R                                      R            R
   Reset        0                                      0            0


     Bit        7             6             5          4            3             2           1           0
                          ALARM1          ALARM0                  CLOCK     FREQCORR        ENABLE      SWRST
  Access                      R             R                       R            R            R           R
   Reset                      0             0                       0             0           0           0


           Bits 16, 17, 18, 19 – GPn General Purpose n Synchronization Busy Status
           Value       Description
           0           Write synchronization for GPn register is complete.
           1           Write synchronization for GPn register is ongoing.

           Bit 15 – CLOCKSYNC Clock Read Sync Enable Synchronization Busy Status
           Value      Description
           0          Write synchronization for CTRLA.CLOCKSYNC bit is complete.
           1          Write synchronization for CTRLA.CLOCKSYNC bit is ongoing.

           Bits 11, 12 – MASKn Mask n Synchronization Busy Status [n = 1..0]
           Value       Description
           0           Write synchronization for MASKx register is complete.
           1           Write synchronization for MASKx register is ongoing.

           Bits 5, 6 – ALARMn Alarm n Synchronization Busy Status [n = 1..0]
           Value       Description
           0            Write synchronization for ALARMx register is complete.
           1            Write synchronization for ALARMx register is ongoing.

           Bit 3 – CLOCK Clock Register Synchronization Busy Status




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 362
                                                  SAM D5x/E5x Family Data Sheet
                                                                           RTC – Real-Time Counter

 Value        Description
 0            Read/write synchronization for CLOCK register is complete.
 1            Read/write synchronization for CLOCK register is ongoing.

Bit 2 – FREQCORR Frequency Correction Synchronization Busy Status
Value      Description
0          Write synchronization for FREQCORR register is complete.
1          Write synchronization for FREQCORR register is ongoing.

Bit 1 – ENABLE Enable Synchronization Busy Status
Value      Description
0          Write synchronization for CTRLA.ENABLE bit is complete.
1          Write synchronization for CTRLA.ENABLE bit is ongoing.

Bit 0 – SWRST Software Reset Synchronization Busy Status
Value      Description
0          Write synchronization for CTRLA.SWRST bit is complete.
1          Write synchronization for CTRLA.SWRST bit is ongoing.




© 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 363
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        RTC – Real-Time Counter

21.12.9 Frequency Correction

           Name:       FREQCORR
           Offset:     0x14
           Reset:      0x00
           Property:   PAC Write-Protection, Write-Synchronized


     Bit         7            6             5            4             3            2           1           0
               SIGN                                               VALUE[6:0]
  Access       R/W           R/W          R/W           R/W          R/W           R/W         R/W         R/W
   Reset         0            0             0            0             0            0           0           0


           Bit 7 – SIGN Correction Sign
           Value      Description
           0          The correction value is positive, i.e., frequency will be decreased.
           1          The correction value is negative, i.e., frequency will be increased.

           Bits 6:0 – VALUE[6:0] Correction Value
           These bits define the amount of correction applied to the RTC prescaler.
            Value      Description
            0          Correction is disabled and the RTC frequency is unchanged.
            1 - 127 The RTC frequency is adjusted according to the value.




       © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 364
                                                                            SAM D5x/E5x Family Data Sheet
                                                                                                         RTC – Real-Time Counter

21.12.10 Clock Value in Clock/Calendar mode (CTRLA.MODE=2)

           Name:         CLOCK
           Offset:       0x18
           Reset:        0x00000000
           Property:     PAC Write-Protection, Write-Synchronized, Read-Synchronized


     Bit        31                 30               29                28          27             26                    25                24
                                                          YEAR[5:0]                                                         MONTH[3:2]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset         0                 0                 0                 0           0                 0                 0                 0


     Bit        23                 22               21                20          19             18                    17                16
                     MONTH[1:0]                                                 DAY[4:0]                                           HOUR[4:4]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset         0                 0                 0                 0           0                 0                 0                 0


     Bit        15                 14               13                12          11             10                    9                 8
                                        HOUR[3:0]                                                        MINUTE[5:2]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset         0                 0                 0                 0           0                 0                 0                 0


     Bit         7                 6                 5                 4           3                 2                 1                 0
                     MINUTE[1:0]                                                       SECOND[5:0]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset         0                 0                 0                 0           0                 0                 0                 0


           Bits 31:26 – YEAR[5:0] Year
           The year offset with respect to the reference year (defined in software).
           The year is considered a leap year if YEAR[1:0] is zero.

           Bits 25:22 – MONTH[3:0] Month
           1 – January
           2 – February
           ...
           12 – December

           Bits 21:17 – DAY[4:0] Day
           Day starts at 1 and ends at 28, 29, 30, or 31, depending on the month and year.

           Bits 16:12 – HOUR[4:0] Hour
           When CTRLA.CLKREP=0, the Hour bit group is in 24-hour format, with values 0-23. When
           CTRLA.CLKREP=1, HOUR[3:0] has values 1-12, and HOUR[4] represents AM (0) or PM (1).

           Bits 11:6 – MINUTE[5:0] Minute
           0 – 59

           Bits 5:0 – SECOND[5:0] Second
           0 – 59




       © 2019 Microchip Technology Inc.                                     Datasheet                                  DS60001507E-page 365
                                                                            SAM D5x/E5x Family Data Sheet
                                                                                                         RTC – Real-Time Counter

21.12.11 Alarm n Value in Clock/Calendar mode (CTRLA.MODE=2)

           Name:         ALARM
           Offset:       0x20 + n*0x08 [n=0..1]
           Reset:        0x00000000
           Property:     PAC Write-Protection, Write-Synchronized

           The 32-bit value of ALARMn is continuously compared with the 32-bit CLOCK value, based on the
           masking set by MASKn.SEL. When a match occurs, the Alarm n interrupt flag in the Interrupt Flag Status
           and Clear register (INTFLAG.ALARMn) is set on the next counter cycle, and the counter is cleared if
           CTRLA.MATCHCLR is '1'.

     Bit        31                 30               29                28          27             26                    25                24
                                                          YEAR[5:0]                                                         MONTH[3:2]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset        0                  0                 0                 0           0                 0                 0                 0


     Bit        23                 22               21                20          19             18                    17                16
                     MONTH[1:0]                                                 DAY[4:0]                                           HOUR[4:4]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset        0                  0                 0                 0           0                 0                 0                 0


     Bit        15                 14               13                12          11             10                    9                 8
                                        HOUR[3:0]                                                        MINUTE[5:2]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset        0                  0                 0                 0           0                 0                 0                 0


     Bit        7                  6                 5                 4           3                 2                 1                 0
                     MINUTE[1:0]                                                       SECOND[5:0]
  Access       R/W             R/W                  R/W               R/W         R/W            R/W               R/W               R/W
   Reset        0                  0                 0                 0           0                 0                 0                 0


           Bits 31:26 – YEAR[5:0] Year
           The alarm year. Years are only matched if MASKn.SEL is 6

           Bits 25:22 – MONTH[3:0] Month
           The alarm month. Months are matched only if MASKn.SEL is greater than 4.

           Bits 21:17 – DAY[4:0] Day
           The alarm day. Days are matched only if MASKn.SEL is greater than 3.

           Bits 16:12 – HOUR[4:0] Hour
           The alarm hour. Hours are matched only if MASKn.SEL is greater than 2.

           Bits 11:6 – MINUTE[5:0] Minute
           The alarm minute. Minutes are matched only if MASKn.SEL is greater than 1.

           Bits 5:0 – SECOND[5:0] Second
           The alarm second. Seconds are matched only if MASKn.SEL is greater than 0.




       © 2019 Microchip Technology Inc.                                     Datasheet                                  DS60001507E-page 366
                                                           SAM D5x/E5x Family Data Sheet
                                                                                     RTC – Real-Time Counter

21.12.12 Alarm n Mask in Clock/Calendar mode (CTRLA.MODE=2)

           Name:       MASK
           Offset:     0x24 + n*0x08 [n=0..1]
           Reset:      0x00
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        7             6           5            4            3            2            1            0
                                                                                           SEL[2:0]
  Access                                                                       R/W          R/W           R/W
   Reset                                                                         0            0            0


           Bits 2:0 – SEL[2:0] Alarm Mask Selection
           These bits define which bit groups of Alarm n are valid.
            Value      Name                      Description
            0x0        OFF                       Alarm Disabled
            0x1        SS                        Match seconds only
            0x2        MMSS                      Match seconds and minutes only
            0x3        HHMMSS                    Match seconds, minutes, and hours only
            0x4        DDHHMMSS                  Match seconds, minutes, hours, and days only
            0x5        MMDDHHMMSS                Match seconds, minutes, hours, days, and months only
            0x6        YYMMDDHHMMSS              Match seconds, minutes, hours, days, months, and years
            0x7        -                         Reserved




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 367
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      RTC – Real-Time Counter

21.12.13 General Purpose n

            Name:       GPn
            Offset:     0x40 + n*0x04 [n=0..3]
            Reset:      0x00000000
            Property:   -


      Bit        31           30           29          28                27      26           25           24
                                                             GP[31:24]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


      Bit        23           22           21          20                19      18           17           16
                                                             GP[23:16]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


      Bit        15           14           13          12                11      10           9             8
                                                             GP[15:8]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


      Bit        7             6            5           4                 3      2            1             0
                                                              GP[7:0]
  Access        R/W          R/W           R/W         R/W               R/W    R/W          R/W           R/W
   Reset         0             0            0           0                 0      0            0             0


            Bits 31:0 – GP[31:0] General Purpose
            These bits are for user-defined general purpose use, see 21.6.8.4 General Purpose Registers.




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 368
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                    RTC – Real-Time Counter

21.12.14 Tamper Control

            Name:         TAMPCTRL
            Offset:       0x60
            Reset:        0x00000000
            Property:     PAC Write-Protection, Enable-Protected


      Bit        31                 30        29                 28         27                 26          25                 24
                                                           DEBNC4        DEBNC3          DEBNC2          DEBNC1         DEBNC0
  Access
   Reset                                                         0          0                  0            0                 0


      Bit        23                 22        21                 20         19                 18          17                 16
                                                           TAMLVL4       TAMLVL3         TAMLVL2         TAMLVL1        TAMLVL0
  Access
   Reset                                                         0          0                  0            0                 0


      Bit        15                 14        13                 12         11                 10           9                 8
                                                                                                                IN4ACT[1:0]
  Access
   Reset                                                                                                    0                 0


      Bit        7                  6         5                  4          3                  2            1                 0
                      IN3ACT[1:0]                  IN2ACT[1:0]                   IN1ACT[1:0]                    IN0ACT[1:0]
  Access
   Reset         0                  0         0                  0          0                  0            0                 0


            Bits 24, 25, 26, 27, 28 – DEBNC Debounce Enable of Tamper Input INn
            Note: Debounce feature does not apply to the Active Layer Protection mode (TAMPCTRL.INACT =
            ACTL).
            Value         Description
            0             Debouncing is disabled for Tamper input INn
            1             Debouncing is enabled for Tamper input INn

            Bits 16, 17, 18, 19, 20 – TAMLVL Tamper Level Select of Tamper Input INn
            Note: Tamper Level feature does not apply to the Active Layer Protection mode (TAMPCTRL.INACT =
            ACTL).
            Value         Description
            0             A falling edge condition will be detected on Tamper input INn.
            1             A rising edge condition will be detected on Tamper input INn.

            Bits 0:1, 2:3, 4:5, 6:7, 8:9 – INACT Tamper Channel n Action
            These bits determine the action taken by Tamper Channel n.
             Value      Name          Description
             0x0        OFF           Off (Disabled)
             0x1        WAKE          Wake and set Tamper flag
             0x2        CAPTURE Capture timestamp and set Tamper flag




        © 2019 Microchip Technology Inc.                              Datasheet                             DS60001507E-page 369
                                                   SAM D5x/E5x Family Data Sheet
                                                                         RTC – Real-Time Counter

 Value        Name           Description
 0x3          ACTL           Compare RTC signal routed between INn and OUT pins . When a mismatch
                             occurs, capture timestamp and set Tamper flag




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 370
                                                                          SAM D5x/E5x Family Data Sheet
                                                                                                       RTC – Real-Time Counter

21.12.15 Timestamp Value

           Name:         TIMESTAMP
           Offset:       0x64
           Reset:        0
           Property:     R


     Bit        31                 30               29               28         27             26                    25                24
                                                         YEAR[5:0]                                                        MONTH[3:2]
  Access        R                  R                R                R           R                 R                 R                 R
   Reset        0                  0                0                0           0                 0                 0                 0


     Bit        23                 22               21               20         19             18                    17                16
                     MONTH[1:0]                                               DAY[4:0]                                           HOUR[4:4]
  Access        R                  R                R                R           R                 R                 R                 R
   Reset        0                  0                0                0           0                 0                 0                 0


     Bit        15                 14               13               12         11             10                    9                 8
                                        HOUR[3:0]                                                      MINUTE[5:2]
  Access        R                  R                R                R           R                 R                 R                 R
   Reset        0                  0                0                0           0                 0                 0                 0


     Bit        7                  6                5                4           3                 2                 1                 0
                     MINUTE[1:0]                                                     SECOND[5:0]
  Access        R                  R                R                R           R                 R                 R                 R
   Reset        0                  0                0                0           0                 0                 0                 0


           Bits 31:26 – YEAR[5:0] Year
           The year value is captured by the TIMESTAMP when a tamper condition occurs.

           Bits 25:22 – MONTH[3:0] Month
           The month value is captured by the TIMESTAMP when a tamper condition occurs.

           Bits 21:17 – DAY[4:0] Day
           The day value is captured by the TIMESTAMP when a tamper condition occurs.

           Bits 16:12 – HOUR[4:0] Hour
           The hour value is captured by the TIMESTAMP when a tamper condition occurs.

           Bits 11:6 – MINUTE[5:0] Minute
           The minute value is captured by the TIMESTAMP when a tamper condition occurs.

           Bits 5:0 – SECOND[5:0] Second
           The second value is captured by the TIMESTAMP when a tamper condition occurs.




       © 2019 Microchip Technology Inc.                                   Datasheet                                  DS60001507E-page 371
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                RTC – Real-Time Counter

21.12.16 Tamper ID

            Name:         TAMPID
            Offset:       0x68
            Reset:        0x00000000


      Bit         31            30             29             28             27            26             25           24
              TAMPEVT
  Access         R/W
   Reset          0


      Bit         23            22             21             20             19            18             17           16


  Access
   Reset


      Bit         15            14             13             12             11            10              9           8


  Access
   Reset


      Bit         7              6              5             4              3              2              1           0
                                                           TAMPID4       TAMPID3        TAMPID2        TAMPID1      TAMPID0
  Access                                                     R/W            R/W           R/W            R/W          R/W
   Reset                                                      0              0              0              0           0


            Bit 31 – TAMPEVT Tamper Event Detected
            Writing a '0' to this bit has no effect. Writing a '1' to this bit clears the tamper detection bit.
            Value         Description
            0             A tamper input event has not been detected
            1             A tamper input event has been detected

            Bits 0, 1, 2, 3, 4 – TAMPID Tamper on Channel n Detected
            Writing a '0' to this bit has no effect. Writing a '1' to this bit clears the tamper detection bit.
            Value         Description
            0             A tamper condition has not been detected on Channel n
            1             A tamper condition has been detected on Channel n




        © 2019 Microchip Technology Inc.                             Datasheet                             DS60001507E-page 372
                                                              SAM D5x/E5x Family Data Sheet
                                                                                      RTC – Real-Time Counter

21.12.17 Backup n

            Name:       BKUP
            Offset:     0x80 + n*0x04 [n=0..7]
            Reset:      0x00000000
            Property:   PAC Write-Protection


      Bit        31           30           29           28                 27    26          25           24
                                                             BKUP[31:24]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


      Bit        23           22           21           20                 19    18          17           16
                                                             BKUP[23:16]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


      Bit        15           14           13           12                 11    10           9           8
                                                             BKUP[15:8]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


      Bit        7             6            5           4                  3      2           1           0
                                                              BKUP[7:0]
  Access        R/W          R/W           R/W         R/W                R/W   R/W          R/W         R/W
   Reset         0             0            0           0                  0      0           0           0


            Bits 31:0 – BKUP[31:0] Backup
            These bits are user-defined for general purpose use in the Backup domain.




        © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 373
