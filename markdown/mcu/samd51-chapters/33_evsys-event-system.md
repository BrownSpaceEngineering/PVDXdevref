# 31. EVSYS – Event System

*Source: `Atmel-SAMD51.pdf`, pages 846-882 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                     EVSYS – Event System


31.    EVSYS – Event System

31.1   Overview
       The Event System (EVSYS) allows autonomous, low-latency and configurable communication between
       peripherals.
       Several peripherals can be configured to generate and/or respond to signals known as events. The exact
       condition to generate an event, or the action taken upon receiving an event, is specific to each peripheral.
       Peripherals that respond to events are called event users. Peripherals that generate events are called
       event generators. A peripheral can have one or more event generators and can have one or more event
       users.
       Communication is made without CPU intervention and without consuming system resources such as bus
       or RAM bandwidth. This reduces the load on the CPU and other system resources, compared to a
       traditional interrupt-based system.



31.2   Features
         • 32 configurable event channels:
            – All channels can be connected to any event generator
            – All channels provide a pure asynchronous path
            – 12 channels (CHANNEL0 to CHANNEL11) provide a resynchronized or synchronous path using
               their dedicated generic clock (GCLK_EVSYS_CHANNEL_n)
         • 119 event generators.
         • 67 event users.
         • Configurable edge detector.
         • Peripherals can be event generators, event users, or both.
         • SleepWalking and interrupt for operation in sleep modes.
         • Software event generation.
         • Each event user can choose which channel to respond to.
         • Optional Static or Round-Robin interrupt priority arbitration.




       © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 846
                                                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                                                                   EVSYS – Event System


31.3     Block Diagram
         Figure 31-1. Event System Block Diagram
                                                               Clock Request [n:0]



                            Event Channel n
                          Event Channel 1                                                                                                           USER m+1

                         Event Channel 0                                                                                                           USER m
                                                                                             Asynchronous Path                                        USERm.CHANNEL

                                                                                                                 CHANNEL0.PATH




                                                                 SleepWalking        Synchronized Path                             Channel_EVT_n
                                                                   Detector                                                  EVT   Channel_EVT_0                                            To Peripheral x
                                                                                                 D Q



          PERIPHERAL0                                           Edge Detector                      R
                                                                                                                                                                                            Peripheral x
                                                                                                                         EVT ACK                       Q       D   Q       D    Q       D
                                                                                                                                                                                            Event Acknowledge
          PERIPHERAL x
                                                                                     Resynchronized Path
                                                                                                                                                           R           R            R
                                                                                      D Q        D Q       D Q
                          CHANNEL0.EVGEN      SWEVT.CHANNEL0   CHANNEL0.EDGSEL



                                                                                        R          R        R

                                                                   GCLK_EVSYS_0




31.4     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

31.4.1   I/O Lines
         Not applicable.

31.4.2   Power Management
         The EVSYS can be used to wake up the CPU from all sleep modes (except BACKUP and OFF Mode),
         even if the clock used by the EVSYS channel and the EVSYS bus clock are disabled. Refer to the PM –
         Power Manager for details on the different sleep modes.
         Although the clock for the EVSYS is stopped, the device still can wake up the EVSYS clock. Some event
         generators can generate an event when their clocks are stopped. The generic clock for the channel
         (GCLK_EVSYS_CHANNEL_n) will be restarted if that channel uses a synchronized path or a
         resynchronized path. It does not need to wake the system from sleep.


                          Important: This generic clock only applies to channels which can be configured as
                          synchronous or resynchronized.


         Related Links
         18. PM – Power Manager

31.4.3   Clocks
         The EVSYS bus clock (CLK_EVSYS_APB) can be enabled and disabled in the Main Clock module, and
         the default state of CLK_EVSYS_APB can be found in Peripheral Clock Masking.
         Each EVSYS channel which can be configured as synchronous or resynchronized has a dedicated
         generic clock (GCLK_EVSYS_CHANNEL_n). These are used for event detection and propagation for
         each channel. These clocks must be configured and enabled in the generic clock controller before using
         the EVSYS. Refer to GCLK - Generic Clock Controller for details.




         © 2019 Microchip Technology Inc.                                                                  Datasheet                                                           DS60001507E-page 847
                                                           SAM D5x/E5x Family Data Sheet
                                                                                       EVSYS – Event System

                        Important: Only EVSYS channel 0 to 11 can be configured as synchronous or resynchronized.




         Related Links
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller

31.4.4   DMA
         Not applicable.

31.4.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the EVSYS interrupts requires the
         interrupt controller to be configured first. Refer to Nested Vector Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

31.4.6   Events
         Not applicable.

31.4.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will continue normal operation. If the peripheral is
         configured to require periodical service by the CPU through interrupts or similar, improper operation or
         data loss may result during debugging. This peripheral can be forced to halt operation during debugging.

31.4.8   Register Access Protection
         Registers with write access can be optionally write-protected by the Peripheral Access Controller (PAC),
         except for the following:
           • Channel Pending Interrupt (INTPEND)
           • Channel n Interrupt Flag Status and Clear (CHINTFLAGn)
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

31.4.9   Analog Connections
         Not applicable.


31.5     Functional Description

31.5.1   Principle of Operation
         The Event System consists of several channels which route the internal events from peripherals
         (generators) to other internal peripherals or I/O pins (users). Each event generator can be selected as
         source for multiple channels, but a channel cannot be set to use multiple event generators at the same
         time.
         A channel path can be configured in asynchronous, synchronous or resynchronized mode of operation.
         The mode of operation must be selected based on the requirements of the application.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 848
                                                              SAM D5x/E5x Family Data Sheet
                                                                                       EVSYS – Event System

          When using synchronous or resynchronized path, the Event System includes options to transfer events to
          users when rising, falling or both edges are detected on event generators.
          For further details, refer to the Channel Path section of this chapter.
          Related Links
          31.5.2.6 Channel Path

31.5.2    Basic Operation

31.5.2.1 Initialization
          Before enabling event routing within the system, the Event Users Multiplexer and Event Channels must
          be selected in the Event System (EVSYS), and the two peripherals that generate and use the event have
          to be configured. The recommended sequence is:
            1. In the event generator peripheral, enable output of event by writing a '1' to the respective Event
                Output Enable bit ("EO") in the peripheral's Event Control register (e.g., TCC.EVCTRL.MCEO1,
                AC.EVCTRL.WINEO0, RTC.EVCTRL.OVFEO).
            2. Configure the EVSYS:
                2.1.      Configure the Event User multiplexer by writing the respective EVSYS.USERm register,
                          see also 31.5.2.3 User Multiplexer Setup.
                2.2.      Configure the Event Channel by writing the respective EVSYS.CHANNELn register, see
                          also 31.5.2.4 Event System Channel.
            3. Configure the action to be executed by the event user peripheral by writing to the Event Action bits
                (EVACT) in the respective Event control register (e.g., TC.EVCTRL.EVACT,
                PDEC.EVCTRL.EVACT). Note: not all peripherals require this step.
            4. In the event user peripheral, enable event input by writing a '1' to the respective Event Input Enable
                bit ("EI") in the peripheral's Event Control register (e.g., AC.EVCTRL.IVEI0,
                ADC.EVCTRL.STARTEI).

31.5.2.2 Enabling, Disabling, and Resetting
          The EVSYS is always enabled.
          The EVSYS is reset by writing a ‘1’ to the Software Reset bit in the Control A register (CTRLA.SWRST).
          All registers in the EVSYS will be reset to their initial state and all ongoing events will be canceled.
          Refer to CTRLA.SWRST register for details.

31.5.2.3 User Multiplexer Setup
          The user multiplexer defines the channel to be connected to which event user. Each user multiplexer is
          dedicated to one event user. A user multiplexer receives all event channels output and must be
          configured to select one of these channels, as shown in Block Diagram section. The channel is selected
          with the Channel bit group in the User register (USERm.CHANNEL).
          The user multiplexer must always be configured before the channel. A list of all user multiplexers is found
          in the User (USERm) register description.
          Related Links
          31.3 Block Diagram

31.5.2.4 Event System Channel
          An event channel can select one event from a list of event generators. Depending on configuration, the
          selected event could be synchronized, resynchronized or asynchronously sent to the users. When
          synchronization or resynchronization is required, the channel includes an internal edge detector, allowing




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 849
                                                         SAM D5x/E5x Family Data Sheet
                                                                                    EVSYS – Event System

        the Event System to generate internal events when rising, falling or both edges are detected on the
        selected event generator.
        An event channel is able to generate internal events for the specific software commands. A channel block
        diagram is shown in Block Diagram section.
        Related Links
        31.3 Block Diagram

31.5.2.5 Event Generators
        Each event channel can receive the events form all event generators. All event generators are listed in
        the Event Generator bit field in the Channel n register (CHANNELn.EVGEN). For details on event
        generation, refer to the corresponding module chapter. The channel event generator is selected by the
        Event Generator bit group in the Channel register (CHANNELn.EVGEN). By default, the channels are not
        connected to any event generators (ie, CHANNELn.EVGEN = 0)
31.5.2.6 Channel Path
        There are different ways to propagate the event from an event generator:
          • Asynchronous path
          • Synchronous path
          • Resynchronized path
        The path is decided by writing to the Path Selection bit group of the Channel register (CHANNELn.PATH).

        Asynchronous Path
        When using the asynchronous path, the events are propagated from the event generator to the event
        user without intervention from the Event System. The GCLK for this channel
        (GCLK_EVSYS_CHANNEL_n) is not mandatory, meaning that an event will be propagated to the user
        without any clock latency.
        When the asynchronous path is selected, the channel cannot generate any interrupts, and the Channel x
        Status register (CHSTATUSx) is always zero. The edge detection is not required and must be disabled by
        software. Each peripheral event user has to select which event edge must trigger internal actions. For
        further details, refer to each peripheral chapter description.

        Synchronous Path
        The synchronous path should be used when the event generator and the event channel share the same
        generator for the generic clock. If they do not share the same clock, a logic change from the event
        generator to the event channel might not be detected in the channel, which means that the event will not
        be propagated to the event user.
        When using the synchronous path, the channel is able to generate interrupts. The channel status bits in
        the Channel Status register (CHSTATUS) are also updated and available for use.

        Resynchronized Path
        The resynchronized path are used when the event generator and the event channel do not share the
        same generator for the generic clock. When the resynchronized path is used, resynchronization of the
        event from the event generator is done in the channel.
        When the resynchronized path is used, the channel is able to generate interrupts. The channel status bits
        in the Channel Status register (CHSTATUS) are also updated and available for use.




        © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 850
                                                           SAM D5x/E5x Family Data Sheet
                                                                                       EVSYS – Event System

31.5.2.7 Edge Detection
         When synchronous or resynchronized paths are used, edge detection must be enabled. The event
         system can execute edge detection in three different ways:
          • Generate an event only on the rising edge
          • Generate an event only on the falling edge
          • Generate an event on rising and falling edges.
         Edge detection is selected by writing to the Edge Selection bit group of the Channel register
         (CHANNELn.EDGSEL).
31.5.2.8 Event Latency
         An event from an event generator is propagated to an event user with different latency, depending on
         event channel configuration.
          • Asynchronous Path: The maximum routing latency of an external event is related to the internal
            signal routing and it is device dependent.
          • Synchronous Path: The maximum routing latency of an external event is one
            GCLK_EVSYS_CHANNEL_n clock cycle.
          • Resynchronized Path: The maximum routing latency of an external event is three
            GCLK_EVSYS_CHANNEL_n clock cycles.
         The maximum propagation latency of a user event to the peripheral clock core domain is three peripheral
         clock cycles.
         The event generators, event channel and event user clocks ratio must be selected in relation with the
         internal event latency constraints. Events propagation or event actions in peripherals may be lost if the
         clock setup violates the internal latencies.
31.5.2.9 The Overrun Channel n Interrupt
         The Overrun Channel n Interrupt flag in the Interrupt Flag Status and Clear register (CHINTFLAGn.OVR)
         will be set, and the optional interrupt will be generated in the following cases:
          • One or more event users on channel n is not ready when there is a new event
          • An event occurs when the previous event on channel m has not been handled by all event users
            connected to that channel
         The flag will only be set when using synchronous or resynchronized paths. In the case of asynchronous
         path, the CHINTFLAGn.OVR is always read as zero.
31.5.2.10 The Event Detected Channel n Interrupt
         The Event Detected Channel n Interrupt flag in the Interrupt Flag Status and Clear register
         (CHINTFLAGn.EVD) is set when an event coming from the event generator configured on channel n is
         detected.
         The flag will only be set when using a synchronous or resynchronized path. In the case of an
         asynchronous path, the CHINTFLAGn.EVD is always zero.
31.5.2.11 Channel Status
         The Channel Status register (CHSTATUS) shows the status of the channels when using a synchronous or
         resynchronized path. There are two different status bits in CHSTATUS for each of the available channels:
          • The CHSTATUSn.BUSYCH bit will be set when an event on the corresponding channel n has not
            been handled by all event users connected to that channel.
          • The CHSTATUSn.RDYUSR bit will be set when all event users connected to the corresponding
            channel are ready to handle incoming events on that channel.




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 851
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        EVSYS – Event System

31.5.2.12 Software Event
         A software event can be initiated on a channel by writing a '1' to the Software Event bit in the Channel
         register (CHANNELm.SWEVT). Then the software event can be serviced as any event generator; i.e.,
         when the bit is set to ‘1’, an event will be generated on the respective channel.
31.5.2.13 Interrupt Status and Interrupts Arbitration
         The Interrupt Status register stores all channels with pending interrupts, as shown below.
         Figure 31-2. Interrupt Status Register
                                                    31   30                                   1   0

                                                                                                        INTSTATUS
            CHINTFLAG31.OVR
           CHINTENSET31.OVR


            CHINTFLAG31.EVD
           CHINTENSET31.EVD




             CHINTFLAG0.OVR
            CHINTENSET0.OVR


             CHINTFLAG0.EVD
            CHINTENSET0.EVD


         The Event System can arbitrate between all channels with pending interrupts. The arbiter can be
         configured to prioritize statically or dynamically the incoming events. The priority is evaluated each time a
         new channel has an interrupt pending, or an interrupt has been cleared. The Channel Pending Interrupt
         register (INTPEND) will provide the channel number with the highest interrupt priority, and the
         corresponding channel interrupt flags and status bits.
         By default, static arbitration is enabled (PRICTRL.RRENx is '0'), the arbiter will prioritize a low channel
         number over a high channel number as shown below. When using the status scheme, there is a risk of
         high channel numbers never being granted access by the arbiter. This can be avoided using a dynamic
         arbitration scheme.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 852
                                                     SAM D5x/E5x Family Data Sheet
                                                                                  EVSYS – Event System

Figure 31-3. Static Priority

              Lowest Channel                      Channel 0                      Highest Priority


                                                        .
                                                        .
                                                        .
                                                   Channel x
                                                  Channel x+1

                                                       .
                                                       .
                                                       .

              Highest Channel                     Channel N                      Lowest Priority
The dynamic arbitration scheme available in the Event System is round-robin. Round-robin arbitration is
enabled by writing PRICTRL.RREN to one. With the round-robin scheme, the channel number of the last
channel being granted access will have the lowest priority the next time the arbiter has to grant access to
a channel, as shown below. The channel number of the last channel being granted access, will be stored
in the Channel Priority Number bit group in the Priority Control register (PRICTRL.PRI).
Figure 31-4. Round-Robin Scheduling
        Channel x last acknowledge request                         Channel (x+1) last acknowledge request

          Channel 0                                                  Channel 0



                                                                         .
                                                                         .
                                                                         .
         Channel x             Lowest Priority                      Channel x
        Channel x+1            Highest Priority                    Channel x+1           Lowest Priority
                                                                   Channel x+2           Highest Priority
                                                                         .
                                                                         .
                                                                         .

        Channel N                                                   Channel N

The Channel Pending Interrupt register (INTPEND) also offers the possibility to indirectly clear the
interrupt flags of a specific channel. Writing a flag to one in this register, will clear the corresponding
interrupt flag of the channel specified by the INTPEND.ID bits.




© 2019 Microchip Technology Inc.                      Datasheet                               DS60001507E-page 853
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         EVSYS – Event System

31.5.3   Interrupts
         The EVSYS has the following interrupt sources for each channel:
           • Overrun Channel n interrupt (OVR)
           • Event Detected Channel n interrupt (EVD)
         These interrupts events are asynchronous wake-up sources.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the corresponding
         Channel n Interrupt Flag Status and Clear (CHINTFLAG) register is set when the interrupt condition
         occurs.
         Note: Interrupts must be globally enabled to allow the generation of interrupt requests.
         Each interrupt can be individually enabled by writing a '1' to the corresponding bit in the Channel n
         Interrupt Enable Set (CHINTENSET) register, and disabled by writing a '1' to the corresponding bit in the
         Channel n Interrupt Enable Clear (CHINTENCLR) register. An interrupt request is generated when the
         interrupt flag is set and the corresponding interrupt is enabled. The interrupt request remains active until
         the interrupt flag is cleared, the interrupt is disabled or the Event System is reset. All interrupt requests
         are ORed together on system level to generate one combined interrupt request to the NVIC.
         The user must read the Channel Interrupt Status (INTSTATUS) register to identify the channels with
         pending interrupts, and must read the Channel n Interrupt Flag Status and Clear (CHINTFLAG) register
         to determine which interrupt condition is present for the corresponding channel. It is also possible to read
         the Interrupt Pending register (INTPEND), which provides the highest priority channel with pending
         interrupt and the respective interrupt flags.

31.5.4   Sleep Mode Operation
         The Event System can generate interrupts to wake up the device from IDLE or STANDBY sleep mode.
         To be able to run in standby, the Run in Standby bit in the Channel register (CHANNELn.RUNSTDBY)
         must be set to '1'. When the Generic Clock On Demand bit in Channel register
         (CHANNELn.ONDEMAND) is set to '1' and the event generator is detected, the event channel will
         request its clock (GCLK_EVSYS_CHANNEL_n). The event latency for a resynchronized channel path will
         increase by two GCLK_EVSYS_CHANNEL_n clock (i.e., up to five GCLK_EVSYS_CHANNEL_n clock
         cycles).
         A channel will behave differently in different sleep modes regarding to CHANNELn.RUNSTDBY and
         CHANNELn.ONDEMAND:
         Table 31-1. Event Channel Sleep Behavior

          CHANNELn.PAT             CHANNELn.        CHANNELn.         Sleep Behavior
               H                   ONDEMAND         RUNSTDBY
                ASYNC                       0             0           Only run in IDLE sleep modes if an event
                                                                      must be propagated. Disabled in STANDBY
                                                                      sleep mode.
           SYNC/RESYNC                      0             1           Run in both IDLE and STANDBY sleep
                                                                      modes.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 854
                                               SAM D5x/E5x Family Data Sheet
                                                                      EVSYS – Event System

...........continued
 CHANNELn.PAT             CHANNELn.    CHANNELn.     Sleep Behavior
      H                   ONDEMAND     RUNSTDBY
  SYNC/RESYNC                      1       0         Only run in IDLE sleep modes if an event
                                                     must be propagated. Disabled in STANDBY
                                                     sleep mode. Two GCLK_EVSYS_n latency
                                                     added in RESYNC path before the event is
                                                     propagated internally.
  SYNC/RESYNC                      1       1         Run in both IDLE and STANDBY sleep
                                                     modes. Two GCLK_EVSYS_n latency added
                                                     in RESYNC path before the event is
                                                     propagated internally.




© 2019 Microchip Technology Inc.               Datasheet                      DS60001507E-page 855
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                      EVSYS – Event System


31.6      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                                                                                                SWRST
 0x01
   ...       Reserved
 0x03
                              7:0     CHANNEL7   CHANNEL6   CHANNEL5    CHANNEL4   CHANNEL3         CHANNEL2     CHANNEL1      CHANNEL0
                             15:8     CHANNEL15 CHANNEL14 CHANNEL13 CHANNEL12 CHANNEL11 CHANNEL10                CHANNEL9      CHANNEL8
 0x04         SWEVT
                             23:16    CHANNEL23 CHANNEL22 CHANNEL21 CHANNEL20 CHANNEL19 CHANNEL18 CHANNEL17 CHANNEL16
                             31:24    CHANNEL31 CHANNEL30 CHANNEL29 CHANNEL28 CHANNEL27 CHANNEL26 CHANNEL25 CHANNEL24
 0x08        PRICTRL          7:0       RREN                                                          PRI[4:0]
 0x09
   ...       Reserved
 0x0F
                              7:0                                                                     ID[4:0]
 0x10        INTPEND
                             15:8       BUSY      READY                                                             EVD           OVR
 0x12
   ...       Reserved
 0x13
                              7:0      CHINT7     CHINT6     CHINT5      CHINT4     CHINT3            CHINT2      CHINT1         CHINT0
                             15:8                                                   CHINT11          CHINT10      CHINT9         CHINT8
 0x14       INTSTATUS
                             23:16
                             31:24
                              7:0     BUSYCHx7   BUSYCHx6   BUSYCHx5    BUSYCHx4   BUSYCHx3         BUSYCHx2     BUSYCHx1      BUSYCHx0
                             15:8                                                  BUSYCHx11 BUSYCHx10           BUSYCHx9      BUSYCHx8
 0x18         BUSYCH
                             23:16
                             31:24
                              7:0     READYUSR7 READYUSR6 READYUSR5 READYUSR4 READYUSR3 READYUSR2 READYUSR1 READYUSR0
                                                                                   READYUSR1 READYUSR1
                             15:8                                                                                READYUSR9 READYUSR8
 0x1C       READYUSR                                                                      1                 0
                             23:16
                             31:24
                              7:0                                            EVGEN[7:0]
                             15:8     ONDEMAND RUNSTDBY                                       EDGSEL[1:0]                 PATH[1:0]
 0x20       CHANNEL0
                             23:16
                             31:24
 0x24      CHINTENCLR0        7:0                                                                                   EVD           OVR
 0x25      CHINTENSET0        7:0                                                                                   EVD           OVR
 0x26       CHINTFLAG0        7:0                                                                                   EVD           OVR
 0x27       CHSTATUS0         7:0                                                                                 BUSYCH        RDYUSR
                              7:0                                            EVGEN[7:0]
                             15:8     ONDEMAND RUNSTDBY                                       EDGSEL[1:0]                 PATH[1:0]
 0x28       CHANNEL1
                             23:16
                             31:24
 0x2C      CHINTENCLR1        7:0                                                                                   EVD           OVR




          © 2019 Microchip Technology Inc.                            Datasheet                                  DS60001507E-page 856
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          EVSYS – Event System

...........continued

  Offset               Name    Bit Pos.

   0x2D         CHINTENSET1       7:0                                                             EVD           OVR
   0x2E          CHINTFLAG1       7:0                                                             EVD           OVR
   0x2F          CHSTATUS1        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x30           CHANNEL2
                                 23:16
                                 31:24
   0x34         CHINTENCLR2       7:0                                                             EVD           OVR
   0x35         CHINTENSET2       7:0                                                             EVD           OVR
   0x36          CHINTFLAG2       7:0                                                             EVD           OVR
   0x37          CHSTATUS2        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x38           CHANNEL3
                                 23:16
                                 31:24
   0x3C         CHINTENCLR3       7:0                                                             EVD           OVR
   0x3D         CHINTENSET3       7:0                                                             EVD           OVR
   0x3E          CHINTFLAG3       7:0                                                             EVD           OVR
   0x3F          CHSTATUS3        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x40           CHANNEL4
                                 23:16
                                 31:24
   0x44         CHINTENCLR4       7:0                                                             EVD           OVR
   0x45         CHINTENSET4       7:0                                                             EVD           OVR
   0x46          CHINTFLAG4       7:0                                                             EVD           OVR
   0x47          CHSTATUS4        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x48           CHANNEL5
                                 23:16
                                 31:24
   0x4C         CHINTENCLR5       7:0                                                             EVD           OVR
   0x4D         CHINTENSET5       7:0                                                             EVD           OVR
   0x4E          CHINTFLAG5       7:0                                                             EVD           OVR
   0x4F          CHSTATUS5        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x50           CHANNEL6
                                 23:16
                                 31:24
   0x54         CHINTENCLR6       7:0                                                             EVD           OVR
   0x55         CHINTENSET6       7:0                                                             EVD           OVR
   0x56          CHINTFLAG6       7:0                                                             EVD           OVR
   0x57          CHSTATUS6        7:0                                                           BUSYCH        RDYUSR




              © 2019 Microchip Technology Inc.                Datasheet                         DS60001507E-page 857
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          EVSYS – Event System

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x58           CHANNEL7
                                 23:16
                                 31:24
   0x5C         CHINTENCLR7       7:0                                                             EVD           OVR
   0x5D         CHINTENSET7       7:0                                                             EVD           OVR
   0x5E          CHINTFLAG7       7:0                                                             EVD           OVR
   0x5F          CHSTATUS7        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x60           CHANNEL8
                                 23:16
                                 31:24
   0x64         CHINTENCLR8       7:0                                                             EVD           OVR
   0x65         CHINTENSET8       7:0                                                             EVD           OVR
   0x66          CHINTFLAG8       7:0                                                             EVD           OVR
   0x67          CHSTATUS8        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x68           CHANNEL9
                                 23:16
                                 31:24
   0x6C         CHINTENCLR9       7:0                                                             EVD           OVR
   0x6D         CHINTENSET9       7:0                                                             EVD           OVR
   0x6E          CHINTFLAG9       7:0                                                             EVD           OVR
   0x6F          CHSTATUS9        7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x70          CHANNEL10
                                 23:16
                                 31:24
   0x74        CHINTENCLR10       7:0                                                             EVD           OVR
   0x75        CHINTENSET10       7:0                                                             EVD           OVR
   0x76         CHINTFLAG10       7:0                                                             EVD           OVR
   0x77          CHSTATUS10       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x78          CHANNEL11
                                 23:16
                                 31:24
   0x7C        CHINTENCLR11       7:0                                                             EVD           OVR
   0x7D        CHINTENSET11       7:0                                                             EVD           OVR
   0x7E         CHINTFLAG11       7:0                                                             EVD           OVR
   0x7F          CHSTATUS11       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x80          CHANNEL12
                                 23:16
                                 31:24
   0x84        CHINTENCLR12       7:0                                                             EVD           OVR




              © 2019 Microchip Technology Inc.                Datasheet                         DS60001507E-page 858
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          EVSYS – Event System

...........continued

  Offset               Name    Bit Pos.

   0x85        CHINTENSET12       7:0                                                             EVD           OVR
   0x86         CHINTFLAG12       7:0                                                             EVD           OVR
   0x87          CHSTATUS12       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x88          CHANNEL13
                                 23:16
                                 31:24
   0x8C        CHINTENCLR13       7:0                                                             EVD           OVR
   0x8D        CHINTENSET13       7:0                                                             EVD           OVR
   0x8E         CHINTFLAG13       7:0                                                             EVD           OVR
   0x8F          CHSTATUS13       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x90          CHANNEL14
                                 23:16
                                 31:24
   0x94        CHINTENCLR14       7:0                                                             EVD           OVR
   0x95        CHINTENSET14       7:0                                                             EVD           OVR
   0x96         CHINTFLAG14       7:0                                                             EVD           OVR
   0x97          CHSTATUS14       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0x98          CHANNEL15
                                 23:16
                                 31:24
   0x9C        CHINTENCLR15       7:0                                                             EVD           OVR
   0x9D        CHINTENSET15       7:0                                                             EVD           OVR
   0x9E         CHINTFLAG15       7:0                                                             EVD           OVR
   0x9F          CHSTATUS15       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xA0          CHANNEL16
                                 23:16
                                 31:24
   0xA4        CHINTENCLR16       7:0                                                             EVD           OVR
   0xA5        CHINTENSET16       7:0                                                             EVD           OVR
   0xA6         CHINTFLAG16       7:0                                                             EVD           OVR
   0xA7          CHSTATUS16       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xA8          CHANNEL17
                                 23:16
                                 31:24
   0xAC        CHINTENCLR17       7:0                                                             EVD           OVR
   0xAD        CHINTENSET17       7:0                                                             EVD           OVR
   0xAE         CHINTFLAG17       7:0                                                             EVD           OVR
   0xAF          CHSTATUS17       7:0                                                           BUSYCH        RDYUSR




              © 2019 Microchip Technology Inc.                Datasheet                         DS60001507E-page 859
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          EVSYS – Event System

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xB0          CHANNEL18
                                 23:16
                                 31:24
   0xB4        CHINTENCLR18       7:0                                                             EVD           OVR
   0xB5        CHINTENSET18       7:0                                                             EVD           OVR
   0xB6         CHINTFLAG18       7:0                                                             EVD           OVR
   0xB7          CHSTATUS18       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xB8          CHANNEL19
                                 23:16
                                 31:24
   0xBC        CHINTENCLR19       7:0                                                             EVD           OVR
   0xBD        CHINTENSET19       7:0                                                             EVD           OVR
   0xBE         CHINTFLAG19       7:0                                                             EVD           OVR
   0xBF          CHSTATUS19       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xC0          CHANNEL20
                                 23:16
                                 31:24
   0xC4        CHINTENCLR20       7:0                                                             EVD           OVR
   0xC5        CHINTENSET20       7:0                                                             EVD           OVR
   0xC6         CHINTFLAG20       7:0                                                             EVD           OVR
   0xC7          CHSTATUS20       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xC8          CHANNEL21
                                 23:16
                                 31:24
   0xCC        CHINTENCLR21       7:0                                                             EVD           OVR
   0xCD        CHINTENSET21       7:0                                                             EVD           OVR
   0xCE         CHINTFLAG21       7:0                                                             EVD           OVR
   0xCF          CHSTATUS21       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xD0          CHANNEL22
                                 23:16
                                 31:24
   0xD4        CHINTENCLR22       7:0                                                             EVD           OVR
   0xD5        CHINTENSET22       7:0                                                             EVD           OVR
   0xD6         CHINTFLAG22       7:0                                                             EVD           OVR
   0xD7          CHSTATUS22       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xD8          CHANNEL23
                                 23:16
                                 31:24
   0xDC        CHINTENCLR23       7:0                                                             EVD           OVR




              © 2019 Microchip Technology Inc.                Datasheet                         DS60001507E-page 860
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          EVSYS – Event System

...........continued

  Offset               Name    Bit Pos.

   0xDD        CHINTENSET23       7:0                                                             EVD           OVR
   0xDE         CHINTFLAG23       7:0                                                             EVD           OVR
   0xDF          CHSTATUS23       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xE0          CHANNEL24
                                 23:16
                                 31:24
   0xE4        CHINTENCLR24       7:0                                                             EVD           OVR
   0xE5        CHINTENSET24       7:0                                                             EVD           OVR
   0xE6         CHINTFLAG24       7:0                                                             EVD           OVR
   0xE7          CHSTATUS24       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xE8          CHANNEL25
                                 23:16
                                 31:24
   0xEC        CHINTENCLR25       7:0                                                             EVD           OVR
   0xED        CHINTENSET25       7:0                                                             EVD           OVR
   0xEE         CHINTFLAG25       7:0                                                             EVD           OVR
   0xEF          CHSTATUS25       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xF0          CHANNEL26
                                 23:16
                                 31:24
   0xF4        CHINTENCLR26       7:0                                                             EVD           OVR
   0xF5        CHINTENSET26       7:0                                                             EVD           OVR
   0xF6         CHINTFLAG26       7:0                                                             EVD           OVR
   0xF7          CHSTATUS26       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
   0xF8          CHANNEL27
                                 23:16
                                 31:24
   0xFC        CHINTENCLR27       7:0                                                             EVD           OVR
   0xFD        CHINTENSET27       7:0                                                             EVD           OVR
   0xFE         CHINTFLAG27       7:0                                                             EVD           OVR
   0xFF          CHSTATUS27       7:0                                                           BUSYCH        RDYUSR
                                  7:0                                EVGEN[7:0]
                                 15:8     ONDEMAND RUNSTDBY                       EDGSEL[1:0]           PATH[1:0]
  0x0100         CHANNEL28
                                 23:16
                                 31:24
  0x0104       CHINTENCLR28       7:0                                                             EVD           OVR
  0x0105       CHINTENSET28       7:0                                                             EVD           OVR
  0x0106        CHINTFLAG28       7:0                                                             EVD           OVR
  0x0107         CHSTATUS28       7:0                                                           BUSYCH        RDYUSR




              © 2019 Microchip Technology Inc.                Datasheet                         DS60001507E-page 861
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                   EVSYS – Event System

...........continued

  Offset               Name     Bit Pos.

                                  7:0                                        EVGEN[7:0]
                                 15:8      ONDEMAND RUNSTDBY                               EDGSEL[1:0]           PATH[1:0]
  0x0108         CHANNEL29
                                 23:16
                                 31:24
  0x010C       CHINTENCLR29       7:0                                                                      EVD           OVR
  0x010D       CHINTENSET29       7:0                                                                      EVD           OVR
  0x010E        CHINTFLAG29       7:0                                                                      EVD           OVR
  0x010F         CHSTATUS29       7:0                                                                    BUSYCH        RDYUSR
                                  7:0                                        EVGEN[7:0]
                                 15:8      ONDEMAND RUNSTDBY                               EDGSEL[1:0]           PATH[1:0]
  0x0110         CHANNEL30
                                 23:16
                                 31:24
  0x0114       CHINTENCLR30       7:0                                                                      EVD           OVR
  0x0115       CHINTENSET30       7:0                                                                      EVD           OVR
  0x0116        CHINTFLAG30       7:0                                                                      EVD           OVR
  0x0117         CHSTATUS30       7:0                                                                    BUSYCH        RDYUSR
                                  7:0                                        EVGEN[7:0]
                                 15:8      ONDEMAND RUNSTDBY                               EDGSEL[1:0]           PATH[1:0]
  0x0118         CHANNEL31
                                 23:16
                                 31:24
  0x011C       CHINTENCLR31       7:0                                                                      EVD           OVR
  0x011D       CHINTENSET31       7:0                                                                      EVD           OVR
  0x011E        CHINTFLAG31       7:0                                                                      EVD           OVR
  0x011F         CHSTATUS31       7:0                                                                    BUSYCH        RDYUSR
                                  7:0                                       CHANNEL[7:0]
                                 15:8
  0x0120               USER0
                                 23:16
                                 31:24
     ...
                                  7:0                                       CHANNEL[7:0]
                                 15:8
  0x0228               USER66
                                 23:16
                                 31:24




31.7           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Refer to Register Access Protection and PAC - Peripheral Access Controller.

               Related Links
               27. PAC - Peripheral Access Controller




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 862
                                    SAM D5x/E5x Family Data Sheet
                                                 EVSYS – Event System

31.4.8 Register Access Protection




© 2019 Microchip Technology Inc.    Datasheet          DS60001507E-page 863
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                  EVSYS – Event System

31.7.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7              6             5             4              3             2              1             0
                                                                                                                       SWRST
   Access                                                                                                                 W
    Reset                                                                                                                 0


               Bit 0 – SWRST Software Reset
               Writing '0' to this bit has no effect.
               Writing '1' to this bit resets all registers in the EVSYS to their initial state. It will always take precedence,
               meaning that all other writes in the same write-operation will be discarded.
               Note: Before applying a Software Reset it is recommended to disable the event generators.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 864
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                  EVSYS – Event System

31.7.2         Software Event

               Name:        SWEVT
               Offset:      0x04
               Reset:       0x00000000
               Property:    PAC Write-Protection


         Bit         31            30            29             28            27             26            25            24
                CHANNEL31     CHANNEL30       CHANNEL29    CHANNEL28     CHANNEL27      CHANNEL26     CHANNEL25      CHANNEL24
   Access            W             W              W             W             W              W             W             W
    Reset            0              0             0             0              0             0             0              0


         Bit         23            22            21             20            19             18            17            16
                CHANNEL23     CHANNEL22       CHANNEL21    CHANNEL20     CHANNEL19      CHANNEL18     CHANNEL17      CHANNEL16
   Access            W             W              W             W             W              W             W             W
    Reset            0              0             0             0              0             0             0              0


         Bit         15            14            13             12            11             10            9              8
                CHANNEL15     CHANNEL14       CHANNEL13    CHANNEL12     CHANNEL11      CHANNEL10      CHANNEL9      CHANNEL8
   Access            W             W              W             W             W              W             W             W
    Reset            0              0             0             0              0             0             0              0


         Bit         7              6             5             4              3             2             1              0
                CHANNEL7       CHANNEL6       CHANNEL5      CHANNEL4      CHANNEL3      CHANNEL2       CHANNEL1      CHANNEL0
   Access            W             W              W             W             W              W             W             W
    Reset            0              0             0             0              0             0             0              0


               Bits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31 – CHANNELx Channel x Software Selection [x=0..7]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will trigger a software event for channel x.
               These bits always return '0' when read.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 865
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                 EVSYS – Event System

31.7.3         Priority Control

               Name:        PRICTRL
               Offset:      0x08
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7            6             5            4             3             2               1           0
                   RREN                                                               PRI[4:0]
   Access           RW                                      RW            RW            RW            RW            RW
    Reset            0                                       0             0             0               0           0


               Bit 7 – RREN Round-Robin Scheduling Enable
               For details on scheduling schemes, refer to Interrupt Status and Interrupts Arbitration
                Value       Description
                0           Static scheduling scheme for channels with level priority
                1           Round-robin scheduling scheme for channels with level priority

               Bits 4:0 – PRI[4:0] Channel Priority Number
               When round-robin arbitration is enabled (PRICTRL.RREN=1) for priority level, this register holds the
               channel number of the last EVSYS channel being granted access as the active channel with priority level.
               The value of this bit group is updated each time the INTPEND or any of CHINTFLAG registers are
               written.
               When static arbitration is enabled (PRICTRL.RREN=0) for priority level, and the value of this bit group is
               nonzero, it will not affect the static priority scheme.
               This bit group is not reset when round-robin scheduling gets disabled (PRICTRL.RREN written to zero).




           © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 866
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                     EVSYS – Event System

31.7.4         Channel Pending Interrupt

               Name:        INTPEND
               Offset:      0x10
               Reset:       0x4000

               An interrupt that handles several channels should consult the INTPEND register to find out which channel
               number has priority (ignoring/filtering each channel that has its own interrupt line). An interrupt dedicated
               to only one channel must not use the INTPEND register.

         Bit         15            14             13            12             11            10             9              8
                   BUSY          READY                                                                     EVD           OVR
   Access            R              R                                                                      RW             RW
    Reset            0              1                                                                       0              0


         Bit         7              6             5              4             3              2             1              0
                                                                                           ID[4:0]
   Access                                                       RW            RW             RW            RW             RW
    Reset                                                        0             0              0             0              0


               Bit 15 – BUSY Busy
               This bit is read '1' when the event on a channel selected by Channel ID field (ID) has not been handled by
               all the event users connected to this channel.

               Bit 14 – READY Ready
               This bit is read '1' when all event users connected to the channel selected by Channel ID field (ID) are
               ready to handle incoming events on this channel.

               Bit 9 – EVD Channel Event Detected
               This flag is set on the next CLK_EVSYS_APB cycle when an event is being propagated through the
               channel, and an interrupt request will be generated if CHINTENCLR/SET.EVD is '1'.
               When the event channel path is asynchronous, the EVD bit will not be set.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear it. It will also clear the corresponding flag in the Channel n Interrupt Flag
               Status and Clear register (CHINTFLAGn) of this peripheral, where n is determined by the Channel ID bit
               field (ID) in this register.

               Bit 8 – OVR Channel Overrun
               This flag is set on the next CLK_EVSYS cycle after an overrun channel condition occurs, and an interrupt
               request will be generated if CHINTENCLR/SET.OVRx is '1'.
               There are two possible overrun channel conditions:
                 • One or more of the event users on channel selected by Channel ID field (ID) are not ready when a
                    new event occurs
                 • An event happens when the previous event on channel selected by Channel ID field (ID) has not yet
                    been handled by all event users
               When the event channel path is asynchronous, the OVR interrupt flag will not be set.
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                            Datasheet                             DS60001507E-page 867
                                                      SAM D5x/E5x Family Data Sheet
                                                                                    EVSYS – Event System

Writing a '1' to this bit will clear it. It will also clear the corresponding flag in the Channel n Interrupt Flag
Status and Clear register (CHINTFLAGn) of this peripheral, where n is determined by the Channel ID bit
field (ID) in this register.

Bits 4:0 – ID[4:0] Channel ID
These bits store the channel number of the highest priority.
When the bits are written, indirect access to the corresponding Channel Interrupt Flag register is enabled.




© 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 868
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                              EVSYS – Event System

31.7.5         Interrupt Status

               Name:       INTSTATUS
               Offset:     0x14
               Reset:      0x00000000


         Bit        31            30            29          28            27           26            25           24


   Access
    Reset


         Bit        23            22            21          20            19           18            17           16


   Access
    Reset


         Bit        15            14            13          12            11           10            9             8
                                                                       CHINT11      CHINT10       CHINT9        CHINT8
   Access                                                                 R             R            R            R
    Reset                                                                 0             0            0             0


         Bit         7            6             5            4            3             2            1             0
                  CHINT7       CHINT6         CHINT5      CHINT4        CHINT3       CHINT2       CHINT1        CHINT0
   Access            R            R             R            R            R             R            R            R
    Reset            0            0             0            0            0             0            0             0


               Bits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 – CHINT Channel x Pending Interrupt
               This bit is set when Channel x has a pending interrupt.
               This bit is cleared when the corresponding Channel x interrupts are disabled, or the source interrupt
               sources are cleared.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 869
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            EVSYS – Event System

31.7.6         Busy Channels

               Name:       BUSYCH
               Offset:     0x18
               Reset:      0x00000000


         Bit        31           30              29         28            27           26           25           24


   Access
    Reset


         Bit        23           22              21         20            19           18           17           16


   Access
    Reset


         Bit        15           14              13         12            11           10            9            8
                                                                      BUSYCHx11    BUSYCHx10    BUSYCHx9      BUSYCHx8
   Access                                                                 R            R            R             R
    Reset                                                                 0            0             0            0


         Bit         7            6              5           4            3            2             1            0
                BUSYCHx7      BUSYCHx6        BUSYCHx5   BUSYCHx4      BUSYCHx3    BUSYCHx2     BUSYCHx1      BUSYCHx0
   Access            R            R              R          R             R            R            R             R
    Reset            0            0              0           0            0            0             0            0


               Bits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 – BUSYCHx Busy Channel x
               This bit is set if an event occurs on channel x has not been handled by all event users connected to
               channel x.
               This bit is cleared when channel x is idle.
               When the event channel x path is asynchronous, this bit is always read '0'.




           © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 870
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                           EVSYS – Event System

31.7.7         Ready Users

               Name:        READYUSR
               Offset:      0x1C
               Reset:       111111111111


         Bit        31           30              29          28           27          26           25           24


   Access           R             R              R           R            R           R            R            R
    Reset            1            1               1           1           1           1            1            1


         Bit        23           22              21          20           19          18           17           16


   Access           R             R              R           R            R           R            R            R
    Reset            1            1               1           1           1           1            1            1


         Bit        15           14              13          12           11          10           9            8
                                                                      READYUSR11 READYUSR10 READYUSR9      READYUSR8
   Access           R             R              R           R            R           R            R            R
    Reset            1            1               1           1           1           1            1            1


         Bit         7            6               5           4           3           2            1            0
                READYUSR7    READYUSR6        READYUSR5   READYUSR4   READYUSR3   READYUSR2   READYUSR1    READYUSR0
   Access           R             R              R           R            R           R            R            R
    Reset            1            1               1           1           1           1            1            1


               Bits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 – READYUSR Ready User for Channel n
               This bit is set when all event users connected to channel n are ready to handle incoming events on
               channel n.
               This bit is cleared when at least one of the event users connected to the channel is not ready.
               When the event channel n path is asynchronous, this bit is always read zero.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 871
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                         EVSYS – Event System

31.7.8         Channel n Control

               Name:        CHANNEL
               Offset:      0x20 + n*0x08 [n=0..31]
               Reset:       0x00008000
               Property:    PAC Write-Protection

               This register allows the user to configure channel n. To write to this register, do a single, 32-bit write of all
               the configuration data.

         Bit         31            30            29            28                27                 26        25               24


   Access
    Reset


         Bit         23            22            21            20                19                 18        17               16


   Access
    Reset


         Bit         15            14            13            12                11                 10        9                8
                ONDEMAND       RUNSTDBY                                               EDGSEL[1:0]                  PATH[1:0]
   Access           RW            RW                                             RW             RW            RW               RW
    Reset            1             0                                             0                  0         0                0


         Bit         7             6              5             4                3                  2         1                0
                                                                    EVGEN[7:0]
   Access           RW            RW             RW            RW                RW             RW            RW               RW
    Reset            0             0              0             0                0                  0         0                0


               Bit 15 – ONDEMAND Generic Clock On Demand
               Value      Description
               0          Generic clock for a channel is always on, if the channel is configured and generic clock
                          source is enabled.
               1          Generic clock is requested on demand while an event is handled

               Bit 14 – RUNSTDBY Run in Standby
               This bit is used to define the behavior during standby sleep mode.
                Value       Description
                0            The channel is disabled in standby sleep mode.
                1            The channel is not stopped in standby sleep mode and depends on the
                             CHANNEL.ONDEMAND bit.

               Bits 11:10 – EDGSEL[1:0] Edge Detection Selection
               These bits set the type of edge detection to be used on the channel.
               These bits must be written to zero when using the asynchronous path.
                Value      Name                 Description
                0x0        NO_EVT_OUTPUT No event output when using the resynchronized or synchronous path
                0x1        RISING_EDGE          Event detection only on the rising edge of the signal from the event
                                                generator




           © 2019 Microchip Technology Inc.                            Datasheet                               DS60001507E-page 872
                                                    SAM D5x/E5x Family Data Sheet
                                                                                EVSYS – Event System

 Value        Name                  Description
 0x2          FALLING_EDGE          Event detection only on the falling edge of the signal from the event
                                    generator
 0x3          BOTH_EDGES            Event detection on rising and falling edges of the signal from the event
                                    generator

Bits 9:8 – PATH[1:0] Path Selection
These bits are used to choose which path will be used by the selected channel.
Note: The path choice can be limited by the channel source, see the table in 31.7.13 USERm.


               Important: Only EVSYS channel 0 to 11 can be configured as synchronous or resynchronized.




 Value        Name                                            Description
 0x0          SYNCHRONOUS                                     Synchronous path
 0x1          RESYNCHRONIZED                                  Resynchronized path
 0x2          ASYNCHRONOUS                                    Asynchronous path
 Other        -                                               Reserved

Bits 7:0 – EVGEN[7:0] Event Generator Selection
These bits are used to choose the event generator to connect to the selected channel.

 Value                 Name                                         Description
 0x00                  NONE                                         No event generator selected
 0x01 - 0x02           OSCCTRL_XOSC_FAILx                           XOSC fail detection x=0..1
 0x03                  OSC32KCTRL_XOSC32K_FAIL                      XOSC32K fail detection
 0x04 - 0x0B           RTC_PERx                                     RTC period x=0..7
 0x0C - 0x0F           RTC_CMP                                      RTC comparison x=0..3
 0x10                  RTC_TAMPER                                   RTC tamper detection
 0x11                  RTC_OVF                                      RTC overflow
 0x12 - 0x21           EIC_EXTINT                                   EIC external interrupt x=0..15
 0x22 - 0x25           DMAC_CH                                      DMA channel x=0..3
 0x26                  PAC_ACCERR                                   PAC Acc. error
 0x27                  Reserved                                     -
 0x28                  Reserved                                     -
 0x29                  TCC0_OVF                                     TCC0 Overflow
 0x2A                  TCC0_TRG                                     TCC0 Trigger Event
 0x2B                  TCC0_CNT                                     TCC0 Counter
 0x2C - 0x31           TCC0_MCx                                     TCC0 Match/Compare x=0..5
 0x32                  TCC1_OVF                                     TCC1 Overflow




© 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 873
                                   SAM D5x/E5x Family Data Sheet
                                                         EVSYS – Event System

...........continued
 Value                 Name                    Description
 0x33                  TCC1_TRG                TCC1 Trigger Event
 0x34                  TCC1_CNT                TCC1 Counter
 0x35 - 0x38           TCC1_MCx                TCC1 Match/Compare x=0..3
 0x39                  TCC2_OVF                TCC2 Overflow
 0x3A                  TCC2_TRG                TCC2 Trigger Event
 0x3B                  TCC2_CNT                TCC2 Counter
 0x3C - 0x3E           TCC2_MCx                TCC2 Match/Compare x=0..2
 0x3F                  TCC3_OVF                TCC3 Overflow
 0x40                  TCC3_TRG                TCC3 Trigger Event
 0x41                  TCC3_CNT                TCC3 Counter
 0x42 - 0x43           TCC3_MCx                TCC3 Match/Compare x=0..1
 0x44                  TCC4_OVF                TCC4 Overflow
 0x45                  TCC4_TRG                TCC4 Trigger Event
 0x46                  TCC4_CNT                TCC4 Counter
 0x47 - 0x48           TCC4_MCx                TCC4 Match/Compare x=0..1
 0x49                  TC0_OVF                 TC0 Overflow
 0x4A - 0x4B           TC0_MCx                 TC0 Match/Compare x=0..1
 0x4C                  TC1_OVF                 TC1 Overflow
 0x4D - 0x4E           TC1_MCx                 TC1 Match/Compare x=0..1
 0x4F                  TC2_OVF                 TC2 Overflow
 0x50 - 0x51           TC2_MCx                 TC2 Match/Compare x=0..1
 0x52                  TC3_OVF                 TC3 Overflow
 0x53 - 0x54           TC3_MCx                 TC3 Match/Compare x=0..1
 0x55                  TC4_OVF                 TC4 Overflow
 0x56 - 0x57           TC4_MCx                 TC4 Match/Compare x=0..1
 0x58                  TC5_OVF                 TC5 Overflow
 0x59 - 0x5A           TC5_MCx                 TC5 Match/Compare x=0..1
 0x5B                  TC6_OVF                 TC6 Overflow
 0x5C - 0x5D           TC6_MCx                 TC6 Match/Compare x=0..1
 0x5E                  TC7_OVF                 TC7 Overflow
 0x5F - 0x60           TC7_MCx                 TC7 Match/Compare x=0..1




© 2019 Microchip Technology Inc.   Datasheet                        DS60001507E-page 874
                                      SAM D5x/E5x Family Data Sheet
                                                             EVSYS – Event System

...........continued
 Value                 Name                       Description
 0x61                  PDEC_OVF                   PDEC Overflow
 0x62                  PDEC_ERR                   PDEC Error
 0x63                  PDEC_DIR                   PDEC Direction
 0x64                  PDEC_VLC                   PDEC VLC
 0x65 - 0x66           PDEC_MCx                   PDEC MCx x=0..1
 0x67                  ADC0_RESRDY                ADC0 RESRDY
 0x68                  ADC0_WINMON                ADC0 Window Monitor
 0x69                  ADC1_RESRDY                ADC1 RESRDY
 0x6A                  ADC1_WINMON                ADC1 Window Monitor
 0x6B - 0x6C           AC_COMPx                   AC Comparator, x=0..1
 0x6D                  AC_WIN                     AC0 Window
 0x6E - 0x6F           DAC_EMPTYx                 DAC empty, x=0..1
 0x70 - 0x71           DAC_RESRDYx                DAC RSRDY, x=0..1
 0x72                  GMAC_TSU_CMP               GMAC Timestamp CMP
 0x73                  TRNG_READY                 TRNG ready
 0x74 - 0x77           CCL_LUTOUT                 CCL LUTOUT




© 2019 Microchip Technology Inc.      Datasheet                       DS60001507E-page 875
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                              EVSYS – Event System

31.7.9         Channel n Interrupt Enable Clear

               Name:        CHINTENCLR
               Offset:      0x24 + n*0x08 [n=0..31]
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7             6            5             4             3             2             1             0
                                                                                                      EVD           OVR
   Access                                                                                              RW           RW
    Reset                                                                                               0             0


               Bit 1 – EVD Channel Event Detected Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Event Detected Channel Interrupt Enable bit, which disables the Event
               Detected Channel interrupt.
               Value         Description
               0             The Event Detected Channel interrupt is disabled.
               1             The Event Detected Channel interrupt is enabled.

               Bit 0 – OVR Channel Overrun Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Overrun Channel Interrupt Enable bit, which disables the Overrun
               Channel interrupt.
               Value         Description
               0             The Overrun Channel interrupt is disabled.
               1             The Overrun Channel interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 876
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           EVSYS – Event System

31.7.10 Channel n Interrupt Enable Set

            Name:        CHINTENSET
            Offset:      0x25 + n*0x08 [n=0..31]
            Reset:       0x00
            Property:    PAC Write-Protection


      Bit         7             6            5             4             3            2             1                0
                                                                                                   EVD          OVR
  Access                                                                                           RW            RW
   Reset                                                                                            0                0


            Bit 1 – EVD Channel Event Detected Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Event Detected Channel Interrupt Enable bit, which enables the Event
            Detected Channel interrupt.
            Value         Description
            0             The Event Detected Channel interrupt is disabled.
            1             The Event Detected Channel interrupt is enabled.

            Bit 0 – OVR Channel Overrun Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Overrun Channel Interrupt Enable bit, which enables the Overrun
            Channel interrupt.
            Value         Description
            0             The Overrun Channel interrupt is disabled.
            1             The Overrun Channel interrupt is enabled.




        © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 877
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        EVSYS – Event System

31.7.11 Channel n Interrupt Flag Status and Clear

            Name:       CHINTFLAG
            Offset:     0x26 + n*0x08 [n=0..31]
            Reset:      0x00


      Bit         7            6            5            4            3            2               1           0
                                                                                               EVD            OVR
  Access                                                                                       RW             RW
   Reset                                                                                           0           0


            Bit 1 – EVD Channel Event Detected
            This flag is set on the next CLK_EVSYS_APB cycle when an event is being propagated through the
            channel, and an interrupt request will be generated if CHINTENCLR/SET.EVD is '1'.
            When the event channel path is asynchronous, the EVD interrupt flag will not be set.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Event Detected Channel interrupt flag.

            Bit 0 – OVR Channel Overrun
            This flag is set on the next CLK_EVSYS cycle after an overrun channel condition occurs, and an interrupt
            request will be generated if CHINTENCLR/SET.OVRx is '1'.
            There are two possible overrun channel conditions:
              • One or more of the event users on the channel are not ready when a new event occurs.
              • An event happens when the previous event on channel has not yet been handled by all event users.
            When the event channel path is asynchronous, the OVR interrupt flag will not be set.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Overrun Channel interrupt flag.




        © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 878
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        EVSYS – Event System

31.7.12 Channel n Status

           Name:       CHSTATUSn
           Offset:     0x27 + n*0x08 [n=0..31]
           Reset:      0x01


     Bit         7            6            5             4            3            2            1             0
                                                                                             BUSYCH       RDYUSR
  Access                                                                                        R             R
   Reset                                                                                        0             0


           Bit 1 – BUSYCH Busy Channel
           This bit is cleared when channel is idle.
           This bit is set if an event on channel has not been handled by all event users connected to channel.
           When the event channel path is asynchronous, this bit is always read '0'.

           Bit 0 – RDYUSR Ready User
           This bit is cleared when at least one of the event users connected to the channel is not ready.
           This bit is set when all event users connected to channel are ready to handle incoming events on the
           channel.
           When the event channel path is asynchronous, this bit is always read zero.




       © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 879
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          EVSYS – Event System

31.7.13 Event User m

           Name:        USERm
           Offset:      0x0120 + m*0x04 [m=0..66]
           Reset:       0x00000000
           Property:    PAC Write-Protection


     Bit        31               30        29            28             27          26            25            24


  Access
   Reset


     Bit        23               22        21            20             19          18            17            16


  Access
   Reset


     Bit        15               14        13            12             11          10            9              8


  Access
   Reset


     Bit         7               6          5            4                  3        2            1              0
                                                             CHANNEL[7:0]
  Access       R/W           R/W           R/W          R/W            R/W          R/W          R/W            R/W
   Reset         0               0          0            0                  0        0            0              0


           Bits 7:0 – CHANNEL[7:0] Channel Event Selection
           These bits select channel n to connect to the event user m. The following table lists all of the Event Users
           and the associated 'm' value to determine which USERm register to define the desired Event Channel.
           Note: A value x of this bit field selects channel n = x-1.
           Table 31-2. User Multiplexer Number m

           USERm             User Multiplexer                   Description                           Path Type(1)
           m=0               RTC_TAMPER                         RTC Tamper                            A
           m = 1..4          PORT_EV0..3                        PORT Event 0..3                       A
           m = 5..12         DMAC_CH0..7                        Channel 0..7                          S, R
           m = 13            -                                  Reserved                              -
           m = 14            CM4_TRACE_START                    CM4 trace start                       S, R
           m = 15            CM4_TRACE_STOP                     CM4 trace stop                        S, R
           m = 16            CM4_TRACE_TRIG                     CM4 trace trigger                     S, R
           m = 17..18        TCC0 EV0..1                        TCC0 EVx                              A, S, R
           m = 19..24        TCC0 MC0..5                        TCC0 MCx                              A, S, R




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 880
                                            SAM D5x/E5x Family Data Sheet
                                                                        EVSYS – Event System

...........continued
 USERm               User Multiplexer        Description                       Path Type(1)
 m = 25..26          TCC1 EV0..1             TCC1 EVx                          A, S, R
 m = 27..30          TCC1 MC0..3             TCC1 MCx                          A, S, R
 m = 31..32          TCC2 EV0..1             TCC2 EVx                          A, S, R
 m = 33..35          TCC2 MC0..2             TCC2 MCx                          A, S, R
 m = 36..37          TCC3 EV0..1             TCC3 EVx                          A, S, R
 m = 38..39          TCC3 MC0..1             TCC3 MCx                          A, S, R
 m = 40..41          TCC4 EV0..1             TCC4 EVx                          A, S, R
 m = 42..43          TCC4 MC0..1             TCC4 MCx                          A, S, R
 m = 44..51          TC0..7 EVU              TC0..7 EVU                        A, S, R
 m = 52..54          PDEC_EVU 0..2           PDEC EVU x                        A, S, R
 m = 55              ADC0 START              ADC0 start conversion             A, S, R
 m = 56              ADC0 SYNC               Flush ADC0                        A, S, R
 m = 57              ADC1 START              ADC1 start conversion             A, S, R
 m = 58              ADC1 SYNC               Flush ADC1                        A, S, R
 m = 59..60          AC_SOC 0..1             AC SOC x                          A
 m = 61..62          DAC_START0..1           DAC0..1 start conversion          A
 m = 63..66          CCL_LUTIN 0..3          CCL input                         A
 others              Reserved                -                                 -

Note:
 1. A = Asynchronous path, S = Synchronous path, R = Resynchronized path
 Value        Description
 0x00         No channel selected
 0x01         Channel 0 selected
 0x02         Channel 1 selected
 0x03         Channel 2 selected
 0x04         Channel 3 selected
 0x05         Channel 4 selected
 0x06         Channel 5 selected
 0x07         Channel 6 selected
 0x08         Channel 7 selected
 0x09         Channel 8 selected
 0x0A         Channel 9 selected
 0x0B         Channel 10 selected
 0x0C         Channel 11 selected
 0x0D         Channel 12 selected
 0x0E         Channel 13 selected




© 2019 Microchip Technology Inc.                 Datasheet                    DS60001507E-page 881
                                    SAM D5x/E5x Family Data Sheet
                                                 EVSYS – Event System

 Value        Description
 0x0F         Channel 14 selected
 0x10         Channel 15 selected
 0x11         Channel 16 selected
 0x12         Channel 17 selected
 0x13         Channel 18 selected
 0x14         Channel 19 selected
 0x15         Channel 20 selected
 0x16         Channel 21 selected
 0x17         Channel 22 selected
 0x18         Channel 23 selected
 0x19         Channel 24 selected
 0x1A         Channel 25 selected
 0x1B         Channel 26 selected
 0x1C         Channel 27 selected
 0x1D         Channel 28 selected
 0x1E         Channel 29 selected
 0x1F         Channel 30 selected
 0x20         Channel 31 selected
 other        Reserved




© 2019 Microchip Technology Inc.    Datasheet          DS60001507E-page 882
