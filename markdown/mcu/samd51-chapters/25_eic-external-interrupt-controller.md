# 23. EIC – External Interrupt Controller

*Source: `Atmel-SAMD51.pdf`, pages 451-476 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                       EIC – External Interrupt Controller


23.    EIC – External Interrupt Controller

23.1   Overview
       The External Interrupt Controller (EIC) allows external pins to be configured as interrupt lines. Each
       interrupt line can be individually masked and can generate an interrupt on rising, falling, both edges, or on
       high or low levels. Each external pin has a configurable filter to remove spikes. Also, each external pin
       can be configured to be asynchronous in order to wake-up the device from Sleep modes where all clocks
       have been disabled. External pins can generate an event.
       A separate Non-Maskable Interrupt (NMI) is supported. It has properties similar to the other external
       interrupts, but is connected to the NMI request of the CPU, enabling it to interrupt any other Interrupt
       mode.



23.2   Features
         •   Up to 16 external pins (EXTINTx), plus one non-maskable pin (NMI)
         •   Dedicated, Individually Maskable Interrupt for Each Pin
         •   Interrupt on Rising, Falling, or Both Edges
         •   Synchronous or Asynchronous Edge Detection mode
         •   Interrupt pin Debouncing
         •   Interrupt on High or Low Levels
         •   Asynchronous Interrupts for Sleep Modes Without Clock
         •   Filtering of External Pins
         •   Event Generation from EXTINTx



23.3   Block Diagram
       Figure 23-1. EIC Block Diagram
                                      FILTENx            SENSEx[2:0]
                                                                                              intreq_extint
                                                                                  Interrupt
                  EXTINTx
                                                                                              inwake_extint
                                                          Edge/Level
                                          Filter                                   Wake
                                                          Detection

                                                                                              evt_extint
                                                                                   Event

                                     NMIFILTEN         NMISENSE[2:0]
                                                                                              intreq_nmi
                                                                                  Interrupt
                   NMI
                                                          Edge/Level
                                          Filter
                                                          Detection
                                                                                              inwake_nmi
                                                                                   Wake




       © 2019 Microchip Technology Inc.                    Datasheet                             DS60001507E-page 451
                                                            SAM D5x/E5x Family Data Sheet
                                                                         EIC – External Interrupt Controller


23.4     Signal Description
          Signal Name                       Type                Description
          EXTINT[15..0]                     Digital Input       External interrupt pin
          NMI                               Digital Input       Non-maskable interrupt pin

         One signal may be available on several pins.



23.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

23.5.1   I/O Lines
         Using the EIC’s I/O lines requires the I/O pins to be configured.
         Related Links
         32. PORT - I/O Pin Controller

23.5.2   Power Management
         All interrupts are available down to STANDBY Sleep mode, but the EIC can be configured to
         automatically mask some interrupts in order to prevent device wake-up.
         The EIC will continue to operate in any Sleep mode where the selected source clock is running. The
         EIC’s interrupts can be used to wake up the device from Sleep modes. Events connected to the Event
         System can trigger other operations in the system without exiting Sleep modes.
         Related Links
         18. PM – Power Manager

23.5.3   Clocks
         The EIC bus clock (CLK_EIC_APB) can be enabled and disabled by the Main Clock Controller, the
         default state of CLK_EIC_APB can be found in the Peripheral Clock Masking section.
         Some optional functions need a peripheral clock, which can either be a generic clock (GCLK_EIC, for
         wider frequency selection) or a Ultra Low-Power 32 KHz clock (CLK_ULP32K, for highest power
         efficiency). One of the clock sources must be configured and enabled before using the peripheral:
         GCLK_EIC is configured and enabled in the Generic Clock Controller.
         CLK_ULP32K is provided by the internal Ultra Low-Power (OSCULP32K) Oscillator in the OSC32KCTRL
         module.
         Both GCLK_EIC and CLK_ULP32K are asynchronous to the user interface clock (CLK_EIC_APB). Due
         to this asynchronicity, writes to certain registers will require synchronization between the clock domains.
         Refer to Synchronization for further details.
         Related Links
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller
         29. OSC32KCTRL – 32KHz Oscillators Controller




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 452
                                                            SAM D5x/E5x Family Data Sheet
                                                                          EIC – External Interrupt Controller

23.5.4   DMA
         Not applicable.

23.5.5   Interrupts
         There are several interrupt request lines, at least one for the external interrupts (EXTINT) and one for
         Non-Maskable Interrupt (NMI).
         The EXTINT interrupt request line is connected to the interrupt controller. Using the EIC interrupt requires
         the interrupt controller to be configured first.
         The NMI interrupt request line is connected to the interrupt controller, but does not require the interrupt to
         be configured.
         Related Links
         10.2 Nested Vector Interrupt Controller

23.5.6   Events
         The events are connected to the Event System. Using the events requires the Event System to be
         configured first.
         Related Links
         31. EVSYS – Event System

23.5.7   Debug Operation
         When the CPU is halted in Debug mode, the EIC continues normal operation. If the EIC is configured in a
         way that requires it to be periodically serviced by the CPU through interrupts or similar, improper
         operation or data loss may result during debugging.

23.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Flag Status and Clear register (INTFLAG)
           • Non-Maskable Interrupt Flag Status and Clear register (NMIFLAG)
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller

23.5.9   Analog Connections
         Not applicable.



23.6     Functional Description

23.6.1   Principle of Operation
         The EIC detects edge or level condition to generate interrupts to the CPU interrupt controller or events to
         the Event System. Each external interrupt pin (EXTINT) can be filtered using majority vote filtering,
         clocked by GCLK_EIC or by CLK_ULP32K.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 453
                                                                SAM D5x/E5x Family Data Sheet
                                                                             EIC – External Interrupt Controller

          Related Links
          23.6.3 External Pin Processing

23.6.2    Basic Operation

23.6.2.1 Initialization
          The EIC must be initialized in the following order:
           1.    Enable CLK_EIC_APB
           2.    If required, configure the NMI by writing the Non-Maskable Interrupt Control register (NMICTRL)
           3.    Enable GCLK_EIC or CLK_ULP32K when one of the following configuration is selected:
                    – the NMI uses edge detection or filtering.
                    – one EXTINT uses filtering.
                    – one EXTINT uses synchronous edge detection.
                    – one EXTINT uses debouncing.
                 GCLK_EIC is used when a frequency higher than 32KHz is required for filtering.
                 CLK_ULP32K is recommended when power consumption is the priority. For CLK_ULP32K write a
                 '1' to the Clock Selection bit in the Control A register (CTRLA.CKSEL).
           4.    Configure the EIC input sense and filtering by writing the Configuration n register (CONFIG).
           5.    Optionally, enable the asynchronous mode.
           6.    Optionally, enable the debouncer mode.
           7.    Enable the EIC by writing a ‘1’ to CTRLA.ENABLE.
          The following bits are enable-protected, meaning that it can only be written when the EIC is disabled
          (CTRLA.ENABLE=0):
           • Clock Selection bit in Control A register (CTRLA.CKSEL)
          The following registers are enable-protected:
           •    Event Control register (EVCTRL)
           •    Configuration n register (CONFIG).
           •    External Interrupt Asynchronous Mode register (23.8.9 ASYNCH)
           •    Debouncer Enable register (23.8.11 DEBOUNCEN)
           •    Debounce Prescaler register (23.8.12 DPRESCALER)
          Enable-protected bits in the CTRLA register can be written at the same time when setting
          CTRLA.ENABLE to '1', but not at the same time as CTRLA.ENABLE is being cleared.
          Enable-protection is denoted by the "Enable-Protected" property in the register description.
          Related Links
          23.8.10 CONFIG

23.6.2.2 Enabling, Disabling, and Resetting
          The EIC is enabled by writing a '1' the Enable bit in the Control A register (CTRLA.ENABLE). The EIC is
          disabled by writing CTRLA.ENABLE to '0'.
          The EIC is reset by setting the Software Reset bit in the Control register (CTRLA.SWRST). All registers in
          the EIC will be reset to their initial state, and the EIC will be disabled.
          Refer to the CTRLA register description for details.




         © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 454
                                                            SAM D5x/E5x Family Data Sheet
                                                                            EIC – External Interrupt Controller

23.6.3   External Pin Processing
         Each external pin can be configured to generate an interrupt/event on edge detection (rising, falling or
         both edges) or level detection (high or low). The sense of external interrupt pins is configured by writing
         the Input Sense x bits in the Config n register (CONFIG.SENSEx). The corresponding interrupt flag
         (INTFLAG.EXTINT[x]) in the Interrupt Flag Status and Clear register (23.8.8 INTFLAG) is set when the
         interrupt condition is met.
         When the interrupt flag has been cleared in edge-sensitive mode, INTFLAG.EXTINT[x] will only be set if a
         new interrupt condition is met.
         In level-sensitive mode, when interrupt has been cleared, INTFLAG.EXTINT[x] will be set immediately if
         the EXTINTx pin still matches the interrupt condition.
         Each external pin can be filtered by a majority vote filtering, clocked by GCLK_EIC or CLK_ULP32K.
         Filtering is enabled if bit Filter Enable x in the Configuration n register (CONFIG.FILTENx) is written to '1'.
         The majority vote filter samples the external pin three times with GCLK_EIC or CLK_ULP32K and outputs
         the value when two or more samples are equal.
         Table 23-1. Majority Vote Filter

          Samples [0, 1, 2]                                             Filter Output
          [0,0,0]                                                       0
          [0,0,1]                                                       0
          [0,1,0]                                                       0
          [0,1,1]                                                       1
          [1,0,0]                                                       0
          [1,0,1]                                                       1
          [1,1,0]                                                       1
          [1,1,1]                                                       1

         When an external interrupt is configured for level detection and when filtering is disabled, detection is
         done asynchronously. Level detection and asynchronous edge detection does not require GCLK_EIC or
         CLK_ULP32K, but interrupt and events can still be generated.
         If filtering or synchronous edge detection or debouncing is enabled, the EIC automatically requests
         GCLK_EIC or CLK_ULP32K to operate. The selection between these two clocks is done by writing the
         Clock Selection bits in the Control A register (CTRLA.CKSEL). GCLK_EIC must be enabled in the GCLK
         module. In these modes the external pin is sampled at the EIC clock rate, thus pulses with duration lower
         than two EIC clock periods may not be properly detected.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 455
                                                                         SAM D5x/E5x Family Data Sheet
                                                                                     EIC – External Interrupt Controller

         Figure 23-2. Interrupt Detection Latency by modes (Rising Edge)
                     GCLK_EIC


                     CLK_EIC_APB


                     EXTINTx

                     intreq_extint[x]
                     (level detection / no filter)

                     intreq_extint[x]                                                                     No interrupt
                     (level detection / filter)

                     intreq_extint[x]
                     (edge detection / no filter)

                     intreq_extint[x]                                                                     No interrupt
                     (edge detection / filter)


                                                                               clear INTFLAG.EXTINT[x]

         The detection latency depends on the detection mode.
         Table 23-2. Detection Latency

          Detection mode                          Latency (worst case)
          Level without filter                    Five CLK_EIC_APB periods
          Level with filter                       Four GCLK_EIC/CLK_ULP32K periods + five CLK_EIC_APB periods
          Edge without filter                     Four GCLK_EIC/CLK_ULP32K periods + five CLK_EIC_APB periods
          Edge with filter                        Six GCLK_EIC/CLK_ULP32K periods + five CLK_EIC_APB periods

         Related Links
         14. GCLK - Generic Clock Controller
         23.8.10 CONFIG

23.6.4   Additional Features

23.6.4.1 Non-Maskable Interrupt (NMI)
         The non-maskable interrupt pin can also generate an interrupt on edge or level detection, but it is
         configured with the dedicated NMI Control register (NMICTRL). To select the sense for NMI, write to the
         NMISENSE bit group in the NMI Control register (NMICTRL.NMISENSE). NMI filtering is enabled by
         writing a '1' to the NMI Filter Enable bit (NMICTRL.NMIFILTEN).
         If edge detection or filtering is required, enable GCLK_EIC or CLK_ULP32K.
         NMI detection is enabled only by the NMICTRL.NMISENSE value, and the EIC is not required to be
         enabled.
         When an NMI is detected, the Non-maskable Interrupt flag in the NMI Flag Status and Clear register is
         set (NMIFLAG.NMI). NMI interrupt generation is always enabled, and NMIFLAG.NMI generates an
         interrupt request when set.
23.6.4.2 Asynchronous Edge Detection Mode (No Debouncing)
         The EXTINT edge detection can be operated synchronously or asynchronously, selected by the
         Asynchronous Control Mode bit for external pin x in the External Interrupt Asynchronous Mode register
         (ASYNCH.ASYNCH[x]). The EIC edge detection is operated synchronously when the Asynchronous
         Control Mode bit (ASYNCH.ASYNCH[x]) is '0' (default value). It is operated asynchronously when
         ASYNCH.ASYNCH[x] is written to '1'.




         © 2019 Microchip Technology Inc.                                Datasheet                       DS60001507E-page 456
                                                          SAM D5x/E5x Family Data Sheet
                                                                        EIC – External Interrupt Controller

        In Synchronous Edge Detection Mode, the external interrupt (EXTINT) or the non-maskable interrupt
        (NMI) pins are sampled using the EIC clock as defined by the Clock Selection bit in the Control A register
        (CTRLA.CKSEL). The External Interrupt flag (INTFLAG.EXTINT[x]) or Non-Maskable Interrupt flag
        (NMIFLAG.NMI) is set when the last sampled state of the pin differs from the previously sampled state. In
        this mode, the EIC clock is required.
        The Synchronous Edge Detection Mode can be used in Idle and Standby sleep modes.
        In Asynchronous Edge Detection Mode, the external interrupt (EXTINT) pins or the non-maskable
        interrupt (NMI) pins set the External Interrupt flag or Non-Maskable Interrupt flag (INTFLAG.EXTINT[x] or
        NMIFLAG) directly. In this mode, the EIC clock is not requested.
        The asynchronous edge detection mode can be used in Idle and Standby sleep modes.
23.6.4.3 Interrupt Pin Debouncing
        The external interrupt pin (EXTINT) edge detection can use a debouncer to improve input noise immunity.
        When selected, the debouncer can work in the synchronous mode or the asynchronous mode, depending
        on the configuration of the ASYNCH.ASYNCH[x] bit for the pin. The debouncer uses the EIC clock as
        defined by the bit CTRLA.CKSEL to clock the debouncing circuitry. The debouncing time frame is set with
        the debouncer prescaler DPRESCALER.DPRESCALERn, which provides the low frequency clock tick
        that is used to reject higher frequency signals.
        The debouncing mode for pin EXTINT x can be selected only if the Sense bits in the Configuration y
        register (CONFIGy.SENSEx) are set to RISE, FALL or BOTH. If the debouncing mode for pin EXTINT x is
        selected, the filter mode for that pin (CONFIGy.FILTENx) can not be selected.
        The debouncer manages an internal “valid pin state” that depends on the external interrupt (EXTINT) pin
        transitions, the debouncing mode and the debouncer prescaler frequency. The valid pin state reflects the
        pin value after debouncing. The external interrupt pin (EXTINT) is sampled continously on EIC clock. The
        sampled value is evaluated on each low frequency clock tick to detect a transitional edge when the
        sampled value is different of the current valid pin state. The sampled value is evaluated on each EIC
        clock when DPRESCALER.TICKON=0 or on each low frequency clock tick when
        DPRESCALER.TICKON=1, to detect a bounce when the sampled value is equal to the current valid pin
        state. Transitional edge detection increments the transition counter of the EXTINT pin, while bounce
        detection resets the transition counter. The transition counter must exceed the transition count threshold
        as defined by the DPRESCALER.STATESn bitfield. In the synchronous mode the threshold is 4 when
        DPRESCALER.STATESn=0 or 8 when DPRESCALER.STATESn=1. In the asynchronous mode the
        threshold is 4.
        The valid pin state for the pins can be accessed by reading the register PINSTATE for both synchronous
        or asynchronous debouncing mode.
        Synchronous edge detection In this mode the external interrupt (EXTINT) pin is sampled continously on
        EIC clock.
          1.   A pin edge transition will be validated when the sampled value is consistently different of the
               current valid pin state for 4 (or 8 depending on bit DPRESCALER.STATESn) consecutive ticks of
               the low frequency clock.
          2.   Any pin sample, at the low frequency clock tick rate, with a value opposite to the current valid pin
               state will increment the transition counter.
          3.   Any pin sample, at EIC clock rate (when DPRESCALER.TICKON=0) or the low frequency clock tick
               (when DPRESCALER.TICKON=1), with a value identical to the current valid pin state will return the
               transition counter to zero.




        © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 457
                                                                SAM D5x/E5x Family Data Sheet
                                                                                 EIC – External Interrupt Controller

           4.   When the transition counter meets the count threshold, the pin edge transition is validated and the
                pin state PINSTATE.PINSTATE[x] is changed to the detected level.
           5.   The external interrupt flag (INTFLAG.EXTINT[x]) is set when the pin state PINSTATE.PINSTATE[x]
                is changed.
         Figure 23-3. EXTINT Pin Synchronous Debouncing (Rising Edge)
                               CLK_EIC

                                  CLK_PRESCALER


                               EXTINTx

                                PIN_STATE


                               INTGLAG
                                                  LOW           TRANSITION                 HIGH

                                                                             Set INTFLAG

         In the synchronous edge detection mode, the EIC clock is required. The synchronous edge detection
         mode can be used in Idle and Standby sleep modes.
         Asynchronous edge detection In this mode, the external interrupt (EXTINT) pin directly drives an
         asynchronous edges detector which triggers any rising or falling edge on the pin:
          1. Any edge detected that indicates a transition from the current valid pin state will immediately set the
              valid pin state PINSTATE.PINSTATE[x] to the detected level.
          2. The external interrupt flag (INTFLAG.EXTINT[x] is immediately changed.
          3. The edge detector will then be idle until no other rising or falling edge transition is detected during 4
              consecutive ticks of the low frequency clock.
          4. Any rising or falling edge transition detected during the idle state will return the transition counter to
              0.
          5. After 4 consecutive ticks of the low frequency clock without bounce detected, the edge detector is
              ready for a new detection.
         Figure 23-4. EXTINT Pin Asynchronous Debouncing (Rising Edge)
                               CLK_EIC

                                  CLK_PRESCALER


                               EXTINTx

                                PIN_STATE


                               INTGLAG
                                            LOW             TRANSITION                     HIGH

                                              Set INTFLAG

         In this mode, the EIC clock is requested. The asynchronous edge detection mode can be used in Idle and
         Standby sleep modes.

23.6.5   DMA Operation
         Not applicable.

23.6.6   Interrupts
         The EIC has the following interrupt sources:
           • External interrupt pins (EXTINTx). See 23.6.2 Basic Operation.
           • Non-maskable interrupt pin (NMI). See 23.6.4 Additional Features.




         © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 458
                                                                   SAM D5x/E5x Family Data Sheet
                                                                               EIC – External Interrupt Controller

         Each interrupt source has an associated Interrupt flag. The interrupt flag in the Interrupt Flag Status and
         Clear register (INTFLAG) is set when an Interrupt condition occurs (NMIFLAG for NMI). Each interrupt,
         except NMI, can be individually enabled by setting the corresponding bit in the Interrupt Enable Set
         register (INTENSET=1), and disabled by setting the corresponding bit in the Interrupt Enable Clear
         register (INTENCLR=1).
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or the EIC
         is reset. See the INTFLAG register for details on how to clear Interrupt flags. The EIC has one interrupt
         request line for each external interrupt (EXTINTx) and one line for NMI. The user must read the INTFLAG
         (or NMIFLAG) register to determine which Interrupt condition is present.
         Note:
          1. Interrupts must be globally enabled for interrupt requests to be generated.
          2. If an external interrupts (EXTINT) is common on two or more I/O pins, only one will be active (the
               first one programmed).
         Related Links
         10. Processor and Architecture

23.6.7   Events
         The EIC can generate the following output events:
           • External event from pin (EXTINTx).
         Setting an Event Output Control register (EVCTRL.EXTINTEO) enables the corresponding output event.
         Clearing this bit disables the corresponding output event. Refer to Event System for details on configuring
         the Event System.
         When the condition on pin EXTINTx matches the configuration in the CONFIGn register, the
         corresponding event is generated, if enabled.
         Related Links
         31. EVSYS – Event System

23.6.8   Sleep Mode Operation
         In sleep modes, an EXTINTx pin can wake up the device if the corresponding condition matches the
         configuration in the CONFIG register, and the corresponding bit in the Interrupt Enable Set register
         (23.8.7 INTENSET) is written to '1'.
         Figure 23-5. Wake-up Operation Example (High-Level Detection, No Filter, Interrupt Enable Set)
                   CLK_EIC_APB


                   EXTINTx


                   intwake_extint[x]


                   intreq_extint[x]



                                            wake from sleep mode                  clear INTFLAG.EXTINT[x]

         Related Links
         23.8.10 CONFIG




         © 2019 Microchip Technology Inc.                          Datasheet                                DS60001507E-page 459
                                                             SAM D5x/E5x Family Data Sheet
                                                                         EIC – External Interrupt Controller

23.6.9   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset bit in control register (CTRLA.SWRST)
           • Enable bit in control register (CTRLA.ENABLE)
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 460
                                                       SAM D5x/E5x Family Data Sheet
                                                                        EIC – External Interrupt Controller


23.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                               CKSEL                      ENABLE        SWRST
 0x01        NMICTRL          7:0                             NMIASYNCH   NMIFILTEN      NMISENSE[2:0]
                              7:0                                                                         NMI
 0x02        NMIFLAG
                             15:8
                              7:0                                                          ENABLE        SWRST
                             15:8
 0x04       SYNCBUSY
                             23:16
                             31:24
                              7:0                                 EXTINTEO[7:0]
                             15:8                                EXTINTEO[15:8]
 0x08         EVCTRL
                             23:16
                             31:24
                              7:0                                  EXTINT[7:0]
                             15:8                                 EXTINT[15:8]
 0x0C        INTENCLR
                             23:16
                             31:24
                              7:0                                  EXTINT[7:0]
                             15:8                                 EXTINT[15:8]
 0x10        INTENSET
                             23:16
                             31:24
                              7:0                                  EXTINT[7:0]
                             15:8                                 EXTINT[15:8]
 0x14        INTFLAG
                             23:16
                             31:24
                              7:0                                 ASYNCH[7:0]
                             15:8                                 ASYNCH[15:8]
 0x18         ASYNCH
                             23:16
                             31:24
                              7:0     FILTEN1   SENSE1[2:0]                FILTEN0        SENSE0[2:0]
                             15:8     FILTEN3   SENSE3[2:0]                FILTEN2        SENSE2[2:0]
 0x1C        CONFIG0
                             23:16    FILTEN5   SENSE5[2:0]                FILTEN4        SENSE4[2:0]
                             31:24    FILTEN7   SENSE7[2:0]                FILTEN6        SENSE6[2:0]
                              7:0     FILTEN1   SENSE1[2:0]                FILTEN0        SENSE0[2:0]
                             15:8     FILTEN3   SENSE3[2:0]                FILTEN2        SENSE2[2:0]
 0x20        CONFIG1
                             23:16    FILTEN5   SENSE5[2:0]                FILTEN4        SENSE4[2:0]
                             31:24    FILTEN7   SENSE7[2:0]                FILTEN6        SENSE6[2:0]
 0x24
   ...       Reserved
 0x2F
                              7:0                                DEBOUNCEN[7:0]
                             15:8                               DEBOUNCEN[15:8]
 0x30      DEBOUNCEN
                             23:16
                             31:24




          © 2019 Microchip Technology Inc.              Datasheet                         DS60001507E-page 461
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                 EIC – External Interrupt Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0     STATES1         PRESCALER1[2:0]            STATES0          PRESCALER0[2:0]
                                 15:8
   0x34         DPRESCALER
                                 23:16                                                                                  TICKON
                                 31:24
                                  7:0                                       PINSTATE[7:0]
                                 15:8                                       PINSTATE[15:8]
   0x38            PINSTATE
                                 23:16
                                 31:24




23.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 462
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                   EIC – External Interrupt Controller

23.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection, Write-Synchronized


         Bit         7              6             5              4             3             2              1             0
                                                              CKSEL                                      ENABLE        SWRST
   Access                                                      RW                                          RW             W
    Reset                                                        0                                          0             0


               Bit 4 – CKSEL Clock Selection
               The EIC can be clocked either by GCLK_EIC (when a frequency higher than 32KHz is required for
               filtering) or by CLK_ULP32K (when power consumption is the priority).
               This bit is not Write-Synchronized.
                Value         Description
                0             The EIC is clocked by GCLK_EIC.
                1             The EIC is clocked by CLK_ULP32K.

               Bit 1 – ENABLE Enable
               Due to synchronization there is a delay between writing to CTRLA.ENABLE until the peripheral is
               enabled/disabled. The value written to CTRLA.ENABLE will read back immediately and the Enable bit in
               the Synchronization Busy register will be set (SYNCBUSY.ENABLE=1). SYNCBUSY.ENABLE will be
               cleared when the operation is complete.
               This bit is not Enable-Protected.
               This bit is Write-Synchronized.
                Value       Description
                0           The EIC is disabled.
                1           The EIC is enabled.

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit resets all registers in the EIC to their initial state, and the EIC will be disabled.
               Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
               write operation will be discarded.
               Due to synchronization there is a delay from writing CTRLA.SWRST until the Reset is complete.
               CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the Reset is complete.
               This bit is not Enable-Protected.
               This bit is Write-Synchronized.
                Value        Description
                0            There is no ongoing reset operation.
                1            The reset operation is ongoing.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 463
                                                               SAM D5x/E5x Family Data Sheet
                                                                              EIC – External Interrupt Controller

23.8.2         Non-Maskable Interrupt Control

               Name:       NMICTRL
               Offset:     0x01
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5           4              3           2          1            0
                                                     NMIASYNCH     NMIFILTEN               NMISENSE[2:0]
   Access                                                R/W            R/W         R/W        R/W          R/W
    Reset                                                 0              0           0          0            0


               Bit 4 – NMIASYNCH Asynchronous Edge Detection Mode
               The NMI edge detection can be operated synchronously or asynchronously to the EIC clock.
                Value     Description
                0         The NMI edge detection is synchronously operated.
                1         The NMI edge detection is asynchronously operated.

               Bit 3 – NMIFILTEN Non-Maskable Interrupt Filter Enable
               Value      Description
               0          NMI filter is disabled.
               1          NMI filter is enabled.

               Bits 2:0 – NMISENSE[2:0] Non-Maskable Interrupt Sense Configuration
               These bits define on which edge or level the NMI triggers.
                Value      Name                   Description
                0x0        NONE                   No detection
                0x1        RISE                   Rising-edge detection
                0x2        FALL                   Falling-edge detection
                0x3        BOTH                   Both-edge detection
                0x4        HIGH                   High-level detection
                0x5        LOW                    Low-level detection
                0x6 -      -                      Reserved
                0x7




           © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 464
                                                                 SAM D5x/E5x Family Data Sheet
                                                                              EIC – External Interrupt Controller

23.8.3         Non-Maskable Interrupt Flag Status and Clear

               Name:       NMIFLAG
               Offset:     0x02
               Reset:      0x0000


         Bit        15           14            13           12           11           10            9            8


   Access
    Reset


         Bit         7            6            5            4            3             2            1            0
                                                                                                                NMI
   Access                                                                                                       RW
    Reset                                                                                                        0


               Bit 0 – NMI Non-Maskable Interrupt
               This flag is cleared by writing a '1' to it.
               This flag is set when the NMI pin matches the NMI sense configuration, and will generate an interrupt
               request.
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 465
                                                              SAM D5x/E5x Family Data Sheet
                                                                           EIC – External Interrupt Controller

23.8.4         Synchronization Busy

               Name:      SYNCBUSY
               Offset:    0x04
               Reset:     0x00000000


         Bit        31           30           29         28          27             26      25           24


   Access
    Reset


         Bit        23           22           21         20          19             18      17           16


   Access
    Reset


         Bit        15           14           13         12           11            10       9           8


   Access
    Reset


         Bit        7             6           5           4           3             2        1           0
                                                                                          ENABLE       SWRST
   Access                                                                                    R           R
    Reset                                                                                    0           0


               Bit 1 – ENABLE Enable Synchronization Busy Status
               Value      Description
               0          Write synchronization for CTRLA.ENABLE bit is complete.
               1          Write synchronization for CTRLA.ENABLE bit is ongoing.

               Bit 0 – SWRST Software Reset Synchronization Busy Status
               Value      Description
               0          Write synchronization for CTRLA.SWRST bit is complete.
               1          Write synchronization for CTRLA.SWRST bit is ongoing.




           © 2019 Microchip Technology Inc.                   Datasheet                      DS60001507E-page 466
                                                               SAM D5x/E5x Family Data Sheet
                                                                            EIC – External Interrupt Controller

23.8.5         Event Control

               Name:       EVCTRL
               Offset:     0x08
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31           30           29          28           27          26          25           24


   Access
    Reset


         Bit        23           22           21          20           19          18          17           16


   Access
    Reset


         Bit        15           14           13          12           11          10           9           8
                                                          EXTINTEO[15:8]
   Access          R/W          R/W           R/W        R/W          R/W         R/W          R/W         R/W
    Reset           0             0            0          0            0           0            0           0


         Bit        7             6            5          4            3           2            1           0
                                                           EXTINTEO[7:0]
   Access          R/W          R/W           R/W        R/W          R/W         R/W          R/W         R/W
    Reset           0             0            0          0            0           0            0           0


               Bits 15:0 – EXTINTEO[15:0] External Interrupt Event Output Enable
               The bit x of EXTINTEO enables the event associated with the EXTINTx pin.
                Value       Description
                0           Event from pin EXTINTx is disabled.
                1           Event from pin EXTINTx is enabled and will be generated when EXTINTx pin matches the
                            external interrupt sensing configuration.




           © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 467
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                        EIC – External Interrupt Controller

23.8.6         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x0C
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit         31            30            29            28                  27          26         25             24


   Access
    Reset


         Bit         23            22            21            20                  19          18         17             16


   Access
    Reset


         Bit         15            14            13            12                  11          10          9             8
                                                                    EXTINT[15:8]
   Access           R/W           R/W           R/W            R/W             R/W            R/W         R/W           R/W
    Reset            0             0              0             0                  0           0           0             0


         Bit         7             6              5             4                  3           2           1             0
                                                                    EXTINT[7:0]
   Access           R/W           R/W           R/W            R/W             R/W            R/W         R/W           R/W
    Reset            0             0              0             0                  0           0           0             0


               Bits 15:0 – EXTINT[15:0] External Interrupt Enable
               The bit x of EXTINT disables the interrupt associated with the EXTINTx pin.
               Writing a '0' to bit x has no effect.
               Writing a '1' to bit x will clear the External Interrupt Enable bit x, which disables the external interrupt
               EXTINTx.
                Value        Description
                0            The external interrupt x is disabled.
                1            The external interrupt x is enabled.




           © 2019 Microchip Technology Inc.                            Datasheet                           DS60001507E-page 468
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                        EIC – External Interrupt Controller

23.8.7         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x10
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         31            30            29            28                  27          26         25               24


   Access
    Reset


         Bit         23            22            21            20                  19          18         17               16


   Access
    Reset


         Bit         15            14            13            12                  11          10         9                8
                                                                    EXTINT[15:8]
   Access           R/W           R/W           R/W           R/W              R/W            R/W        R/W           R/W
    Reset            0             0              0             0                  0           0          0                0


         Bit         7             6              5             4                  3           2          1                0
                                                                    EXTINT[7:0]
   Access           R/W           R/W           R/W           R/W              R/W            R/W        R/W           R/W
    Reset            0             0              0             0                  0           0          0                0


               Bits 15:0 – EXTINT[15:0] External Interrupt Enable
               The bit x of EXTINT enables the interrupt associated with the EXTINTx pin.
               Writing a '0' to bit x has no effect.
               Writing a '1' to bit x will set the External Interrupt Enable bit x, which enables the external interrupt
               EXTINTx.
                Value        Description
                0            The external interrupt x is disabled.
                1            The external interrupt x is enabled.




           © 2019 Microchip Technology Inc.                            Datasheet                           DS60001507E-page 469
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    EIC – External Interrupt Controller

23.8.8         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x14
               Reset:      0x00000000
               Property:   -


         Bit        31           30           29           28                  27          26        25           24


   Access
    Reset


         Bit        23           22           21           20                  19          18        17           16


   Access
    Reset


         Bit        15           14           13           12                  11          10         9           8
                                                                EXTINT[15:8]
   Access          R/W          R/W           R/W          R/W             R/W            R/W        R/W         R/W
    Reset            0            0            0            0                  0           0          0           0


         Bit         7            6            5            4                  3           2          1           0
                                                                EXTINT[7:0]
   Access          R/W          R/W           R/W          R/W             R/W            R/W        R/W         R/W
    Reset            0            0            0            0                  0           0          0           0


               Bits 15:0 – EXTINT[15:0] External Interrupt
               The flag bit x is cleared by writing a '1' to it.
               This flag is set when EXTINTx pin matches the external interrupt sense configuration and will generate an
               interrupt request if INTENCLR/SET.EXTINT[x] is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the External Interrupt x flag.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 470
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                  EIC – External Interrupt Controller

23.8.9         External Interrupt Asynchronous Mode

               Name:       ASYNCH
               Offset:     0x18
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31           30           29          28                 27          26        25           24


   Access
    Reset


         Bit        23           22           21          20                 19          18        17           16


   Access
    Reset


         Bit        15           14           13          12                 11          10         9           8
                                                               ASYNCH[15:8]
   Access          RW            RW           RW          RW              RW            RW         RW          RW
    Reset           0             0           0            0                  0          0          0           0


         Bit        7             6           5            4                  3          2          1           0
                                                               ASYNCH[7:0]
   Access          RW            RW           RW          RW              RW            RW         RW          RW
    Reset           0             0           0            0                  0          0          0           0


               Bits 15:0 – ASYNCH[15:0] Asynchronous Edge Detection Mode
               The bit x of ASYNCH set the Asynchronous Edge Detection Mode for the interrupt associated with the
               EXTINTx pin.
                Value       Description
                0           The EXTINT x edge detection is synchronously operated.
                1           The EXTINT x edge detection is asynchronously operated.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 471
                                                                SAM D5x/E5x Family Data Sheet
                                                                              EIC – External Interrupt Controller

23.8.10 External Interrupt Sense Configuration n

            Name:        CONFIG
            Offset:      0x1C + n*0x04 [n=0..1]
            Reset:       0x00000000
            Property:    PAC Write-Protection, Enable-Protected


      Bit        31             30             29          28            27          26         25           24
               FILTEN7                     SENSE7[2:0]                 FILTEN6              SENSE6[2:0]
  Access         RW            RW             RW          RW             RW         RW         RW           RW
   Reset          0             0              0           0              0          0          0            0


      Bit        23             22             21          20            19          18         17           16
               FILTEN5                     SENSE5[2:0]                 FILTEN4              SENSE4[2:0]
  Access         RW            RW             RW          RW             RW         RW         RW           RW
   Reset          0             0              0           0              0          0          0            0


      Bit        15             14             13          12            11          10         9            8
               FILTEN3                     SENSE3[2:0]                 FILTEN2              SENSE2[2:0]
  Access         RW            RW             RW          RW             RW         RW         RW           RW
   Reset          0             0              0           0              0          0          0            0


      Bit         7             6              5           4              3          2          1            0
               FILTEN1                     SENSE1[2:0]                 FILTEN0              SENSE0[2:0]
  Access         RW            RW             RW          RW             RW         RW         RW           RW
   Reset          0             0              0           0              0          0          0            0


            Bits 3, 7, 11, 15, 19, 23, 27, 31 – FILTENx Filter Enable x [x=7..0]
            Note: The filter must be disabled if the asynchronous detection is enabled.
            Value        Description
            0            Filter is disabled for EXTINT[n*8+x] input.
            1            Filter is enabled for EXTINT[n*8+x] input.

            Bits 0:2, 4:6, 8:10, 12:14, 16:18, 20:22, 24:26, 28:30 – SENSEx Input Sense Configuration x [x=7..0]
            These bits define on which edge or level the interrupt or event for EXTINT[n*8+x] will be generated.
             Value      Name                     Description
             0x0        NONE                     No detection
             0x1        RISE                     Rising-edge detection
             0x2        FALL                     Falling-edge detection
             0x3        BOTH                     Both-edge detection
             0x4        HIGH                     High-level detection
             0x5        LOW                      Low-level detection
             0x6 -      -                        Reserved
             0x7




        © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 472
                                                          SAM D5x/E5x Family Data Sheet
                                                                       EIC – External Interrupt Controller

23.8.11 Debouncer Enable

           Name:       DEBOUNCEN
           Offset:     0x30
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31           30           29         28           27          26          25           24


  Access
   Reset


     Bit        23           22           21         20           19          18          17           16


  Access
   Reset


     Bit        15           14           13         12           11          10           9           8
                                                     DEBOUNCEN[15:8]
  Access       RW            RW           RW         RW          RW           RW          RW          RW
   Reset        0             0           0           0           0            0           0           0


     Bit        7             6           5           4           3            2           1           0
                                                     DEBOUNCEN[7:0]
  Access       RW            RW           RW         RW          RW           RW          RW          RW
   Reset        0             0           0           0           0            0           0           0


           Bits 15:0 – DEBOUNCEN[15:0] Debouncer Enable
           The bit x of DEBOUNCEN set the Debounce mode for the interrupt associated with the EXTINTx pin.
            Value       Description
            0           The EXTINT x edge input is not debounced.
            1           The EXTINT x edge input is debounced.




       © 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 473
                                                              SAM D5x/E5x Family Data Sheet
                                                                            EIC – External Interrupt Controller

23.8.12 Debouncer Prescaler

           Name:        DPRESCALER
           Offset:      0x34
           Reset:       0x00000000
           Property:    PAC Write-Protection, Enable-Protected


     Bit        31            30           29            28            27           26               25          24


  Access
   Reset


     Bit        23            22           21            20            19           18               17          16
                                                                                                              TICKON
  Access                                                                                                        RW
   Reset                                                                                                         0


     Bit        15            14           13            12            11           10               9           8


  Access
   Reset


     Bit         7            6             5             4            3             2               1           0
             STATES1                 PRESCALER1[2:0]                STATES0                PRESCALER0[2:0]
  Access        RW           RW            RW            RW           RW            RW           RW             RW
   Reset         0            0             0             0            0             0               0           0


           Bit 16 – TICKON Pin Sampler frequency selection
           This bit selects the clock used for the sampling of bounce during transition detection.
            Value       Description
            0           The bounce sampler is using GCLK_EIC.
            1           The bounce sampler is using the low frequency clock.

           Bits 3, 7 – STATESx Debouncer number of states x
           This bit selects the number of samples by the debouncer low frequency clock needed to validate a
           transition from current pin state to next pin state in synchronous debouncing mode for pins
           EXTINT[7+(8x):8x].
            Value        Description
            0            The number of low frequency samples is 3.
            1            The number of low frequency samples is 7.

           Bits 0:2, 4:6 – PRESCALERx Debouncer Prescaler x
           These bits select the debouncer low frequency clock for pins EXTINT[7+(8x):8x].
            Value      Name                 Description
            0x0        F/2                  EIC clock divided by 2
            0x1        F/4                  EIC clock divided by 4
            0x2        F/8                  EIC clock divided by 8
            0x3        F/16                 EIC clock divided by 16




       © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 474
                                                  SAM D5x/E5x Family Data Sheet
                                                                EIC – External Interrupt Controller

 Value        Name                 Description
 0x4          F/32                 EIC clock divided by 32
 0x5          F/64                 EIC clock divided by 64
 0x6          F/128                EIC clock divided by 128
 0x7          F/256                EIC clock divided by 256




© 2019 Microchip Technology Inc.                    Datasheet                     DS60001507E-page 475
                                                                SAM D5x/E5x Family Data Sheet
                                                                                  EIC – External Interrupt Controller

23.8.13 Pin State

            Name:       PINSTATE
            Offset:     0x38
            Reset:      0x00000000


      Bit        31            30           29           28               27             26        25            24


  Access
   Reset


      Bit        23            22           21           20               19             18        17            16


  Access
   Reset


      Bit        15            14           13           12               11             10          9           8
                                                          PINSTATE[15:8]
  Access          R            R            R             R               R              R           R           R
   Reset          0            0            0             0                   0          0           0           0


      Bit         7            6            5             4                   3          2           1           0
                                                              PINSTATE[7:0]
  Access          R            R            R             R               R              R           R           R
   Reset          0            0            0             0                   0          0           0           0


            Bits 15:0 – PINSTATE[15:0] Pin State
            These bits return the valid pin state of the debounced external interrupt pin EXTINTx.




        © 2019 Microchip Technology Inc.                          Datasheet                          DS60001507E-page 476
