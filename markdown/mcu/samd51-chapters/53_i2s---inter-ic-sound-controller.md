# 51. I2S - Inter-IC Sound Controller

*Source: `Atmel-SAMD51.pdf`, pages 1888-1924 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                            I2S - Inter-IC Sound Controller


51.    I2S - Inter-IC Sound Controller

51.1   Overview
       The Inter-IC Sound Controller (I2S) provides bidirectional, synchronous and digital audio link with external
       audio devices.
       This controller is compliant with the Inter-IC Sound (I2S) bus specification. It supports TDM interface with
       external multi-slot audio codecs. It also supports PDM interface with external MEMS microphones.
       The I2S consists of two Clock Units, one Transmit Serializer, and one Receive Serializer, that can be
       enabled separately, to provide Master, Slave, or controller modes.
       The pins associated with I2S peripheral are SDO,SDI, FSn, SCKn, and MCKn pins.
       Peripheral DMAC channels, separate for each Serializer, allow a continuous high bitrate data transfer
       without processor intervention to the following:
         •   Audio codecs in Master, Slave, or Controller mode
         •   Stereo DAC or ADC through dedicated I2S serial interface
         •   Multi-slot or multiple stereo DACs or ADCs, using the TDM format
         •   Mono or stereo MEMS microphones, using the PDM interface
       Each Serializer supports using either a single DMAC channel for all data channels, or two separate
       DMAC channels for different data channels.
       The I2S supports 8-bit and 16-bit compact stereo format. This helps in reducing the required DMA
       bandwidth by transferring the left and right samples within the same data word.
       Usually, an external audio codec or digital signal processor (DSP) requires a clock which is a multiple of
       the sampling frequency fs (for example, 384×fs). The I2S peripheral in Master Mode and Controller mode
       is capable of outputting an output clock ranging from 16×fs to 1024×fs on the Master Clock pin (MCKn).
       The Master Clock pin cannot output a clock signal when in Slave Mode.



51.2   Features
         • Compliant with Inter-IC Sound (I2S) bus specification
         • Supported data formats:
             – 32-, 24-, 20-, 18-, 16-, and 8-bit mono or stereo format
             – 16- and 8-bit compact stereo format, with left and right samples packed in the same word to
                reduce data transfers
         • Supported data frame formats:
             – 2-channel I2S with Word Select
             – 1- to 8-slot Time Division Multiplexed (TDM) with Frame Sync and individually enabled slots
             – 1- or 2-channel Pulse Density Modulation (PDM) reception for MEMS microphones
             – 1-channel burst transfer with non-periodic Frame Sync
         • 2 independent Clock Units handling either the same clock or separate clocks for the Serializers:
             – Suitable for a wide range of sample frequencies fs, including 32kHz, 44.1kHz, 48kHz, 88.2kHz,
                96kHz, and 192kHz
             – 16×fs to 1024×fs Master Clock generated for external audio CODECs




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1888
                                                                             SAM D5x/E5x Family Data Sheet
                                                                                               I2S - Inter-IC Sound Controller

         • Master, slave, and controller modes:
             – Master: Data received/transmitted based on internally-generated clocks. Output Serial Clock on
                SCKn pin, Master Clock on MCKn pin, and Frame Sync Clock on FSn pin
             – Slave: Data received/transmitted based on external clocks on Serial Clock pin (SCKn) or Master
                Clock pin (MCKn)
             – Controller: Only output internally generated Master clock (MCKn), Serial Clock (SCKn), and
                Frame Sync Clock (FSn)
         • Individual enabling and disabling of Clock Units and Serializers
         • DMA interfaces for each Serializer receiver or transmitter to reduce processor overhead:
             – Either one DMA channel for all data slots or
             – One DMA channel per data channel in stereo
         • Smart Data Holding register management to avoid data slots mix after overrun or underrun



51.3   Block Diagram
       Figure 51-1. I2S Block Diagram

                               2 Generic clocks
                                                                                                   I2S
                                 GCLK_I2S_0
                                 GCLK_I2S_1
               Power
                                                                                                                            MCKn
              Manager
                                 APB clock
                               CLK_I2S_APB                                     2 Clock Units                                SCKn


                                                                                                                            FSn
                                                  Peripheral Bus Interface




                                   APB
           Peripheral Bus
               Bridge
                                                                                                           PORT
                                   Rx
                DMA                                                                                                         SDO
              Controller           Tx                                        Transmit Serializer
                                                                                Serializers
                                                                                   and
                                                                             Receive Serializer
                                                                                                                            SDI
              Interrupt            IRQ
              Controller




51.4   Signal Description
       Table 51-1.

        Pin Name           Pin Description                                                                        Type
        MCKn               Master Clock for Clock Unit n                                                          Input/Output
        SCKn               Serial Clock for Clock Unit n                                                          Input/Output
        FSn                I2S Word Select or TDM Frame Sync for Clock Unit n                                     Input/Output




       © 2019 Microchip Technology Inc.                                      Datasheet                       DS60001507E-page 1889
                                                              SAM D5x/E5x Family Data Sheet
                                                                               I2S - Inter-IC Sound Controller

         ...........continued
          Pin Name          Pin Description                                                         Type
          SDO               Serial Data Output for Transmit Serializer                              Output
          SDI               Serial Data Input for Receive Serializer                                Input

         Note: One signal can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



51.5     Product Dependencies
         In order to use this module, other parts of the system must be configured correctly, as described below.

51.5.1   I/O Lines
         Using the I2S I/O lines requires the I/O pins to be configured.
         The I2S pins may be multiplexed with I/O Controller lines. The user must first program the I/O Controller
         to assign the desired I2S pins to their peripheral function. If the I2S I/O lines are not used by the
         application, they can be used for other purposes by the I/O Controller. It is required to enable only the I2S
         inputs and outputs actually in use.
         Related Links
         32. PORT - I/O Pin Controller

51.5.2   Power Management
         The I2S will continue to operate in any sleep mode where the selected source clocks are running.

51.5.3   Clocks
         The clock for the I2S bus interface (CLK_I2S_APB) is generated by the Power Manager. This clock is
         disabled at reset, and can be enabled in the Power Manager. It is recommended to disable the I2S before
         disabling the clock, to avoid freezing the I2S in an undefined state.
         There are two generic clocks, GCLK_I2S_0 and GCLK_I2S_1, connected to the I2S peripheral, one for
         each I2S clock unit. The generic clocks (GCLK_I2S_n, n=0..1) can be set to a wide range of frequencies
         and clock sources. The GCLK_I2S_n must be enabled and configured before use.
         The GCLK_I2S_n clocks must be enabled and configured before triggering Software Reset, so that the
         logic in all clock domains can be reset.
         The generic clocks are only used in Master mode and Controller mode. In Master mode, the clock from
         clock unit 0 can be used for both Serializers to handle synchronous transfers, or a separate clock from
         different clock units can be used for each Serializer to handle transfers on non-related clocks.
         Related Links
         14. GCLK - Generic Clock Controller

51.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). Using the I2S DMA requests
         requires the DMA Controller to be configured first.
         Related Links




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1890
                                                             SAM D5x/E5x Family Data Sheet
                                                                                 I2S - Inter-IC Sound Controller

         22. DMAC – Direct Memory Access Controller

51.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using I2S interrupts requires the
         interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

51.5.6   Events
         Not applicable.

51.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will continue normal operation. If the peripheral is
         configured to require periodical service by the CPU through interrupts or similar, improper operation or
         data loss may result during debugging. This peripheral can be forced to halt operation during debugging.

51.5.8   Register Access Protection
         Registers with write access can be optionally write-protected by the Peripheral Access Controller (PAC),
         except for the following:
           • DATAm
           • INTFLAG
           • SYNCBUSY
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

51.5.9   Analog Connections
         Not applicable.



51.6     Functional Description

51.6.1   Principle of Operation
         The I2S uses three or four communication lines for synchronous data transfer:
           • SDO output for Transmit Serializer
           • SDI input for Receive Serializer
           • SCKn for the serial clock in Clock Unit n (n=0..1)
           • FSn for the frame synchronization or I2S word select, identifying the beginning of each frame
           • Optionally, MCKn to output an oversampling clock to an external codec
         I2S data transfer is frame based, where a serial frame:
           • Starts with the frame synchronization active edge, and
           • Consists of 1 to 8 data slots, that are 8-, 16-, 24-, or 32-bit wide.
         Each data slot is used to transfer one data sample of 8, 16, 18, 20, 24 or 32 bits.
         Frame based data transfer is described in the following figure:




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1891
                                                  SAM D5x/E5x Family Data Sheet
                                                                     I2S - Inter-IC Sound Controller

Figure 51-2. Data Format: Frames, Slot, Bits and Clocks




I2S supports multiple data formats such as:
  • 32-, 24-, 20-, 18-, 16-, and 8-bit mono or stereo format
  • 16- and 8-bit compact stereo format, with left and right samples packed in the same word to reduce
    data transfers
In mono format, Transmit mode, data written to the left channel is duplicated to the right output channel.
In mono format, Receiver mode, data received from the right channel is ignored and data received from
the left channel is duplicated in to the right channel.
In mono format, TDM Transmit mode with more than two slots, data written to the even-numbered slots is
duplicated in to the following odd-numbered slot.
In mono format, TDM Receiver mode with more than two slots, data received from the even-numbered
slots is duplicated in to the following odd-numbered slot.
Mono format can be enabled by writing a '1' to the MONO bit in the Serializer m Control register
(SERCTRLm.MONO).
I2S support different data frame formats:
  •   2-channel I2S with Word Select
  •   1- to 8-slot Time Division Multiplexed (TDM) with Frame Sync and individually enabled slots
  •   1- or 2-channel Pulse Density Modulation (PDM) reception for MEMS microphones
  •   1-channel burst transfer with non-periodic Frame Sync
In 2 channel I2S mode, number of slots configured is one or two and successive data words corresponds
to left and right channel. Left and right channel are identified by polarity of Word Select signal (FSn
signal). Each frame consists of one or two data word(s). In the case of compact stereo format, the
number of slots can be one. When 32-bit slot size is used, the number of slots can be two.




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1892
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                   I2S - Inter-IC Sound Controller

          In TDM format, number slots can be configured up to 8 slots. If 4 slots are configured, each frame
          consists of 4 data words.
          In PDM format, continuous 1-bit data samples are available on the SDI line for each SCKn rising and
          SCKn falling edge as in case of a MEMS microphone with PDM interface.
          1-channel burst transfer with non-periodic Frame Sync mode is useful typically for passing control non-
          auto data as in case of DSP. In Burst mode, a single Data transfer starts at each Frame Sync pulse, and
          these pulses are 1-bit wide and occur only when a Data transfer is requested.
          Sections 51.6.4 I2S Format - Reception and Transmission Sequence with Word Select, 51.6.5 TDM
          Format - Reception and Transmission Sequence and 51.7 I2S Application Examples describe more
          about frame/data formats and register settings required for different I2S applications.
          Figure 51-3. I2S Functional Block Diagram
                             MCK0       SCK0       FS0


                                                         Transmit Serializer
               GCLK_I2S_0
                                                             Tx Frame              Tx           Tx
                                    Clock Unit 0             Sequencer            Word        Word           SDO
                                                                                  FSM        Serializer


                                    CLKCTRL0                             TXCTRL                Tx
                                                                                              Word
                                                                         TXDATA             Formatting
               CLK_I2S_APB
                                    APB / DMA
                                     Interface           Receive Serializer
                                                                        RXDATA                  Rx
                                                                                               Word
                                    CLKCTRL1                            RXCTRL               Formatting


            GCLK_I2S_1                                                             Rx           Rx
                                                             Rx Frame
                                    Clock Unit 1                                  Word        Word           SDI
                                                             Sequencer
                                                                                  FSM        Serializer



                             MCK1      SCK1        FS1


51.6.1.1 Initialization
          The I2S features two Clock Units, one Transmit Serializer, and One Receive Serializer. The Transmit
          Serializer uses Clock Unit 0, while the Receive Serializer can either share the same Clock Unit 0 or use
          the Clock Unit 1.
          Before enabling the I2S, the following registers must be configured:
           • Clock Control registers (CLKCTRLn)
           • Serializer Control registers (TXCTRL and/or RXCTRL)
          In Master mode, one of the generic clocks for the I2S must also be configured to operate at the required
          frequency, as described in 51.6.1 Principle of Operation.
           •     fs is the sampling frequency that defines the frame period
           •     CLKCTRLn.NBSLOTS defines the number of slots in each frame
           •     CLKCTRLn.SLOTSIZE defines the number of bits in each slot
           •     SCKn frequency must be fSCKn = fs × number_of_slots × number_of_bits_per_slot)




         © 2019 Microchip Technology Inc.                           Datasheet                     DS60001507E-page 1893
                                                           SAM D5x/E5x Family Data Sheet
                                                                             I2S - Inter-IC Sound Controller

         Once the configuration has been written, the I2S Clock Units and Serializers can be enabled by writing a
         '1' to the CKENn, TXEN, and/or RXEN bits and to the ENABLE bit in the Control register (CTRLA). The
         Clock Unit n can be enabled alone, in Controller Mode, to output clocks to the MCKn, SCKn, and FSn
         pins. The Clock Units must be enabled if Serializers are enabled.
         The Clock Units, the Transmit Serializer and the Receive Serializer can be disabled independently by
         writing a '0' to CTRLA.CKENn, CTRLA.TXEN, and CTRLA.RXEN, respectively. Once requested to stop,
         they will only stop when the pending transmit frames will be completed, if any. When requested to stop,
         the ongoing reception of the current slot will be completed and then the Serializer will be stopped.

                   Example 51-1. Example Requirements: fs=48kHz, MCKn=384×fs
                   If a 384×fs MCKn Master Clock is required (i.e. 18.432MHz), the I2S generic clock could
                   run at 18.432MHz with a Master Clock Output Division Factor of 1 (selected by writing
                   CLKCTRLn.MCKOUTDIV=0x0) in order to obtain the desired MCKn frequency.
                   When using 6 slots per frame (CLKCTRLn.NBSLOTS=0x5) and 32-bit slots
                   (CLKCTRLn.SLOTSIZE=0x3), the desired SCKn frequency is
                   fSCKn = 48kHz × 6 × 32 = 9.216MHz
                   This frequency can be achieved by dividing the I2S generic clock output of 18.432MHz by
                   factor 2: Writing CLKCTRLn.MCKDIV=0x1 will select the correct division factor and
                   output the desired SCKn frequency of 9.216MHz to the SCKn pin.
                   If MCKn is not required, the generic clock could be set to 9.216MHz and
                   CLKCTRLn.MCKDIV=0x0.


51.6.2   Basic Operation
         The Receiver can be operated by reading the Receive Data Holding register (RXDATA), whenever the
         Receive Ready m bit in the Interrupt Flag Status and Clear register (INTFLAG.RXRDYm) is set.
         Successive values read from the RXDATA register will correspond to the samples from the left and right
         audio channels. In TDM mode, the successive values read from RXDATA correspond to the first slot to
         the last slot. For instance, if I2S is configured in TDM mode with 4 slots in a frame, then successive
         values written to RXDATA register correspond to first, second, third, and fourth slot. The number of slots
         in TDM is configured in CLKCTRLn.NBSLOTS.
         The Transmitter can be operated by writing to the Transmit Data Holding register (TXDATA), whenever
         the Transmit Ready m bit in the Interrupt Flag Status and Clear register (INTFLAG.TXRDYm) is set.
         Successive values written to TXDATA register should correspond to the samples from the left and right
         audio channels. In TDM mode, the successive values written to TXDATA correspond to the first, second,
         third, slot to the last slot. The number of slots in TDM is configured in CLKCTRLn.NBSLOTS.
         The Receive Ready and Transmit Ready bits can be polled by reading the INTFLAG register.
         The processor load can be reduced by enabling interrupt-driven operation. The RXRDYm and/or
         TXRDYm interrupt requests can be enabled by writing a '1' to the corresponding bit in the Interrupt
         Enable register (INTENSET). The interrupt service routine associated to the I2S interrupt request will then
         be executed whenever Receive Ready or Transmit Ready status bits are set.
         The processor load can be reduced further by enabling DMA-driven operation. Then, the DMA channels
         support up to four trigger sources from the I2S peripheral. These four trigger sources in DMAC channel
         are
          • I2S RX 0,




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1894
                                                            SAM D5x/E5x Family Data Sheet
                                                                                I2S - Inter-IC Sound Controller

           • I2S RX 1,
           • I2S TX 0, and
           • I2S TX 1.
         For further reference, these are called I2S_DMAC_ID_RX_m and I2S_DMAC_ID_TX_m triggers
         (m=0..1). By using these trigger sources, one DMA data transfer will be executed whenever the Receive
         Ready or Transmit Ready status bits are set.

51.6.2.1 Master Clock, Serial Clock, and Frame Sync Generation
         The generation of clocks in the I2S is described in the next figure.
         Figure 51-4. I2S Clocks Generation




51.6.2.1.1 Slave Mode
         In Slave mode, the Serial Clock and Frame Sync (Word Select in I2S mode and Frame Sync in TDM
         mode) are driven by an external master. SCKn and FSn pins are inputs and no generic clock is required
         by the I2S.




         © 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1895
                                                              SAM D5x/E5x Family Data Sheet
                                                                                 I2S - Inter-IC Sound Controller

51.6.2.1.2 Master Mode and Controller Mode
         In Master Mode, the Master Clock (MCKn), the Serial Clock (SCKn), and the Frame Sync Clock (FSn) are
         generated by the I2S controller. The user can configure the Master Clock, Serial Clock, and Word Select
         Frame Sync signal (Word Select in I2S mode and Frame Sync in TDM mode) using the Clock Unit n
         Control register (CLKCTRLn). MCKn, SCKn, and FSn pins are outputs and a generic clock is used to
         derive the I2S clocks.
         In some applications, audio CODECs connected to the I2S pins may require a Master Clock signal with a
         frequency multiple of the audio sample frequency fs, such as 256×fs.
         In Controller mode, only the Clock generation unit needs to be configured by writing to the CTRLA and
         CLKCTRLn registers, where parameters such as clock division factors, Number of slots, Slot size, Frame
         Sync signal, clock enable are selected.
51.6.2.1.3 MCKn Clock Frequency
         When the I2S is in Master mode, writing a '1' to CLKCTRLn.MCKEN will output GCLK_I2S_n as Master
         Clock to the MCKn pin. The Master Clock to MCKn pin can be divided by writing to CLKCTRLn.MCKSEL
         and CLKCTRLn.MCKOUTDIV. The Master Clock (MCKn) frequency is GCLK_I2S_n frequency divided by
         (MCLKOUTDIV+1).
                        � GCLK_�2�_�
         � MCKn =
                        MCKOUTDIV+1
51.6.2.1.4 SCKn Clock Frequency
         When the Serial Clock (SCKn) is generated from GCLK_I2S_n and both CLKCTRLn.MCKSEL and
         CLKCTRLn.SCKSEL are zero, the Serial Clock (SCKn) frequency is GCLK_I2S_n frequency divided by
         (MCKDIV+1).
         i.e.
                      � GCLK_�2�_�
         � �CKn =
                        MCKDIV+1
51.6.2.1.5 Relation Between MCKn, SCKn, and Sampling Frequency fs
         Based on sampling frequency fs, the SCKn frequency requirement can be calculated:
          • SCKn frequency: �SCKn = �� × total_number_of_bits_per_frame,
           • Where total_number_of_bits_per_frame = number_of_slots × number_of_bits_per_slots.
           • The number of slots is selected by writing to the Number of Slots in Frame bit field in the Clock Unit n
             Control (CLKCTRLn) register: number_of_slots = NBSLOTS + 1.
           • The number of bits per slot (8, 16, 24, or 32 bit) is selected by writing to the Slot Size bit field in
             CLKCTRLn: .
           • Consequently, �SCKn = 8 × �� × NBSLOTS + 1 × SLOTSIZE + 1 .

         The clock frequencies �SCKn and �MCKn are derived from the generic clock frequency �GCLK_I2S_n :
                �GCLK_I2S_n = �SCKn × CLKCTRLn.MCKDIV + 1
           •
                           = 8 × �� × NBSLOTS + 1 × SLOTSIZE + 1 × MCKDIV + 1
             , and
           • �GCLK_I2S_n = �MCKn × MCKOUTDIV + 1 .

         Substituting the right hand sides of the two last equations yields:
                      �GCLK_I2S_n
         �MCKn =
                    MCKOUTDIV+1




        © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 1896
                                                            SAM D5x/E5x Family Data Sheet
                                                                               I2S - Inter-IC Sound Controller

                    8 ⋅ SLOTSIZE+1 ⋅ NBSLOTS+1 ⋅ MCKDIV+1
         �MCKn =
                                  MCKOUTDIV+1
         If a Master Clock output is not required, the GCLK_I2S generic clock can be configured as SCKn by
         writing a '0'to CLKCTRLn.MCKDIV. Alternatively, if the frequency of the generic clock is a multiple of the
         required SCKn frequency, the MCKn-to-SCKn divider can be used with the ratio defined by writing the
         CLKCTRLn.MCKDIV field.
         The FSn pin is used as Word Select in I2S format and as Frame Synchronization in TDM format, as
         described in 51.6.4 I2S Format - Reception and Transmission Sequence with Word Select and 51.6.5
         TDM Format - Reception and Transmission Sequence, respectively.
51.6.2.2 Data Holding Registers
         For both the Transmit and the Receive Serializer, the I2S user interface includes a Data register (TXDATA
         and RXDATA, respectively). They are used to access data samples for all data slots.
51.6.2.2.1 Data Reception Mode
         In receiver mode, the RXDATA register stores the received data.
         When a new data word is available in the RXDATA register, the Receive Ready bit (RXRDYm) in the
         Interrupt Flag Status and Clear register (INTFLAG) is set. Reading the RXDATA register will clear this bit.
         A receive overrun condition occurs if a new data word becomes available before the previous data word
         has been read from the RXDATA register. Then, the Receive Overrun bit in INTFLAG will be set
         (INTFLAG.RXORm). This interrupt can be cleared by writing a '1' to it.
51.6.2.2.2 Data Transmission Mode
         In Transmitter mode, the TXDATA register contains the data to be transmitted.
         when TXDATA is empty, the Transmit Ready bit in the Interrupt Flag Status and Clear register is set
         (INTFLAG.TXRDYm). Writing to TXDATA will clear this bit.
         A transmit underrun condition occurs if data present in TXDATA is sent and no new data is written to
         TXDATA register before the next time slot. Then, the Transmit Underrun bit in INTFLAG will be set
         (INTFLAG.TXURm). This interrupt can be cleared by writing a '1' to it. The Transmit Data when Underrun
         bit in the Tx Serializer Control register (TXCTRL.TXSAME) configures whether a zero data word is
         transmitted in case of underrun (TXCTRL.TXSAME=0), or the previous data word for the current transmit
         slot number is transmitted again (TXCTRL.TXSAME=1).

51.6.3   Master, Controller, and Slave Modes
         In Master and Controller modes, the I2S provides the Serial Clock, a Word Select/Frame Sync signal and
         optionally a Master Clock.
         In Controller mode, the I2S Serializers are disabled. Only the clocks are enabled and output for external
         receivers and/or transmitters.
         In Slave mode, the I2S receives the Serial Clock and the Word Select/Frame Sync Signal from an
         external master. SCKn and FSn pins are inputs.

51.6.4   I2S Format - Reception and Transmission Sequence with Word Select
         As specified in the I2S protocol, data bits are left-adjusted in the Word Select slot, with the MSB
         transmitted first, starting one clock period after the transition on the Word Select line.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1897
                                                              SAM D5x/E5x Family Data Sheet
                                                                                  I2S - Inter-IC Sound Controller

         Figure 51-5. I2S Reception and Transmission Sequence

         Bit Serial Clock
                    SCKn

             Word Select
                    FSn

                    Data
                                                MSB                                           LSB      MSB
                 SDO/SDI
                                                                  Left Channel                    Right Channel
         Data bits are sent on the falling edge of the Serial Clock and sampled on the rising edge of the Serial
         Clock. The Word Select line indicates the channel in transmission, a low level for the left channel and a
         high level for the right channel.
         In I2S format, typical configurations are described below. These configurations do not list all necessary
         settings, but only basic ones. Other configuration settings are to be done as per requirement such as
         clock and DMA configurations.

         Case 1: I2S 16-bit compact stereo receiver
          • Slot size configured as 16 bits (CLKCTRL0.SLOTSIZE = 0x1)
          • Number of slots configured as 2 (CLKCTRL0.NBSLOTS = 0x1)
          • Data size configured as 16-bit compact stereo (RXCTRL.DATASIZE = 0x05)
          • Data delay from Frame Sync configured as 1-bit delay (CLKCTRLn.BITDELAY = 0x01)
          • Frame Sync Width configured as HALF frame (CLKCTRLn.FSWIDTH = 0x01)

         Case 2: I2S 24-bit stereo Transmitterwith 24-bit slot
          • Slot size configured as 24 bits (CLKCTRL0.SLOTSIZE = 0x2)
          • Number of slots configured as 2 (CLKCTRL0.NBSLOTS = 0x1)
          • Data size configured as 24 bits (TXCTRL.DATASIZE = 0x01)
          • Data delay from Frame Sync configured as 1-bit delay (CLKCTRLn.BITDELAY = 0x01)
          • Frame Sync Width configured as HALF frame (CLKCTRLn.FSWIDTH = 0x01)
         In both cases, it will ensure that Word select signal is 'low level' for the left channel and 'high level' for the
         right channel.
         The length of transmitted words can be chosen among 8, 16, 18, 20, 24, and 32 bits by writing the Data
         Word Size bit group in the Serializer Control register (RXCTRL.DATASIZE or TXCTRL.DATASIZE,
         respectively).
         If the slot allows for more data bits than the number of bits specified in the respective DATASIZE field,
         additional bits are appended to the transmitted or received data word as specified in the RXCTRL/
         TXCTRL.EXTEND field. If the slot allows less data bits than programmed, the extra bits are not
         transmitted, or received data word is extended based on the EXTEND field value.

51.6.5   TDM Format - Reception and Transmission Sequence
         In Time Division Multiplexed (TDM) format, the number of data slots sent or received within each frame
         will be (CLKCTRLn.NBSLOTS + 1).
         By configuring the CLKCTRLn register (CLKCTRLn.FSWIDTH and CLKCTRLn.FSINV), the Frame Sync
         pulse width and polarity can be modified.




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1898
                                                           SAM D5x/E5x Family Data Sheet
                                                                              I2S - Inter-IC Sound Controller

         By configuring RXCTRL and/or TXCTRL, data bits can be left-adjusted or right-adjusted in the slot. It can
         also configure the data transmission/reception with either the MSB or the LSB transmitted/received first
         and starting the transmission/reception either at the transition of the FSn pin or one clock period after.
         Figure 51-6. TDM Format Reception and Transmission Sequence




         Data bits are sent on the falling edge of the Serial Clock and sampled on the rising edge of the Serial
         Clock. The FSn pin provides a frame synchronization signal, at the beginning of slot 0. The delay
         between the frame start and the first data bit is defined by writing the CLKCTRLn.BITDELAY field.
         The Frame Sync pulse can be either one SCKn period (BIT), one slot (SLOT), or one half frame (HALF).
         This selection is done by writing the CLKCTRLn.FSWIDTH field.
         The number of slots is selected by writing the CLKCTRLn.NBSLOTS field.
         The number of bits in each slot is selected by writing the CLKCTRLn.SLOTSIZE field.
         The length of transmitted words can be chosen among 8, 16, 18, 20, 24, and 32 bits by writing the
         DATASIZE field in the Serializer Control register (RXCTRL and/or TXCTRL).
         If the slot allows more data bits than the number of bits specified in the RXCTRL. and/or
         TXCTRL.DATASIZE bit field, additional bits are appended to the transmitted or received data word as
         specified in the RXCTRL. and/or TXCTRL.EXTEND bit field. If the slot allows less data bits than
         programmed, the extra bits are not transmitted, or received data word is extended based on the EXTEND
         field value.

51.6.6   PDM Reception
         In Pulse Density Modulation (PDM) reception mode, continuous 1-bit data samples are available on the
         SDI line on each SCKn rising edge, e.g. by a MEMS microphone with PDM interface. When using two
         channel PDM microphones, the second one (right channel) is configured to output data on each SCKn
         falling edge.
         For one PDM microphone, the I2S controller should be configured in normal Receive mode with one slot
         and 16- or 32-bit data size, so that 16 or 32 samples of the microphone are stored into each data word.
         For two PDM microphones, the I2S controller should be configured in PDM2 mode with one slot and 32-
         bit data size. The Rx Serializer will store 16 samples of each microphone in one half of the data word,
         with left microphone bits in lower half and right microphone bits in upper half, like in compact stereo
         format.
         Based on oversampling frequency requirement from PDM microphone, the SCKn frequency must be
         configured in the I2S controller.

                   A microphone that requires a sampling frequency of fs = 48 kHz and an oversampling
                   frequency of fo=64 × fs would require an SCKn frequency of 3.072 MHz.

         After selecting a proper frequency for GCLK_I2S_n and according Master Clock Division Factor in the
         Clock Unit n Control register (CLKCTRLn.MCKDIV), SCKn must be selected as per required frequency.
         In PDM mode, only the clock and data line (SCKn and SDIn) pins are used.




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1899
                                                               SAM D5x/E5x Family Data Sheet
                                                                                      I2S - Inter-IC Sound Controller

         To configure PDM2 mode, set SLOTSIZE = 0x01 (16-bits), NBSLOTS = 0x00 (1 slots) and
         RXCTRL.DATASIZE = 0x00 (32-bit).

51.6.7   Data Formatting Unit
         To allow more flexibility, data words received by the Receive Serializer will be formatted by the Receive
         Formatting Unit before being stored into the Data Holding register (DATAm). The data words written into
         DATAm register will be formatted by the Transmit Formatting Unit before transmission by the Transmit
         Serializer .
         The formatting options are defined in RXCTRL and TXCTRL:
           •   SLOTADJ for left or right justification in the slot
           •   BITREV for bit reversal
           •   WORDADJ for left or right justification in the data word
           •   EXTEND for extension to the word size

51.6.8   DMA, Interrupts and Events
         Table 51-2. Module Request for I2S

          Condition                         DMA             DMA request is cleared          Interrupt     Event input/
                                            request                                         request       output
          Receive Ready                     YES             When data is read               YES
          Transmit Ready (Buffer            YES             When data is written            YES
          empty)
          Receive Overrun                                                                   YES
          Transmit Underrun                                                                 YES

51.6.8.1 DMA Operation
         Each Serializer can be connected either to one single DMAC channel or to one DMAC channel per data
         slot in Stereo mode. This is selected by writing the RXCTRL/TXCTRL.DMA bit.
         Table 51-3. I2C DMA Request Generation

          SERCTRLm.DMA                            Mode                    Slot Parity          DMA Request Trigger
          0                                    Receiver                         all            I2S_DMAC_ID_RX_m
                                              Transmitter                       all            I2S_DMAC_ID_TX_m
          1                                    Receiver                      even              I2S_DMAC_ID_RX_m
                                                                             odd               I2S_DMAC_ID_TX_m
                                              Transmitter                    even              I2S_DMAC_ID_TX_m
                                                                             odd               I2S_DMAC_ID_RX_m

         The DMAC reads from the RXDATA register and writes to the TXDATA register for all data slots,
         successively.
         The DMAC transfers may use 32-bit, 16-bit, or or 8-bit transactions according to the value of the
         TXCTRL/RXCTRL.DATASIZE field. 8-bit compact stereo uses 16-bit and 16-bit compact stereo uses 32-
         bit transactions.




         © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1900
                                                             SAM D5x/E5x Family Data Sheet
                                                                                I2S - Inter-IC Sound Controller

51.6.8.2 Interrupts
         The I2S has the following interrupt sources:
           • Receive Ready (RXRDYm): This is an asynchronous interrupt and can be used to wake-up the
             device from any sleep mode.
           • Receive Overrun (RXORm): This is an asynchronous interrupt and can be used to wake-up the
             device from any sleep mode.
           • Transmit Ready (TXRDYm): This is an asynchronous interrupt and can be used to wake-up the
             device from any sleep mode.
           • Transmit Underrun (TXURm): This is an asynchronous interrupt and can be used to wake-up the
             device from any sleep mode.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a one to the corresponding bit in the Interrupt Enable Set (INTENSET)
         register, and disabled by writing a one to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
         register. An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is
         enabled. The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or
         the I2S is reset. Refer to the INTFLAG register for details on how to clear interrupt flags. All interrupt
         requests from the peripheral are ORed together on system level to generate one combined interrupt
         request to the NVIC. Refer to the “Nested Vector Interrupt Controller” for details. The user must read the
         INTFLAG register to determine which interrupt condition is present.
         Note: Interrupts must be globally enabled for interrupt requests to be generated. Refer to Nested Vector
         Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

51.6.8.3 Events
         Not applicable.

51.6.9   Sleep Mode Operation
         The I2S continues to operate in all sleep modes that still provide its clocks.

51.6.10 Synchronization
        Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
        need to be synchronized when written or read.
         When executing an operation that requires synchronization, the corresponding Synchronization Busy bit
         in the Synchronization Busy register (SYNCBUSY) will be set immediately, and cleared when
         synchronization is complete.
         If an operation that requires synchronization is executed while the corresponding SYNCBUSY bit is '1', a
         peripheral bus error is generated.
         The following bits are synchronized when written:
           • Software Reset bit in the Control A register (CTRLA.SWRST). SYNCBUSY.SWRST is set to '1' while
             synchronization is in progress.
           • Enable bit in the Control A register (CTRLA.ENABLE). SYNCBUSY.ENABLE is set to '1' while
             synchronization is in progress.




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1901
                                                             SAM D5x/E5x Family Data Sheet
                                                                           I2S - Inter-IC Sound Controller

          • Clock Unit x Enable bits in the Control A register (CTRLA.CKENx). SYNCBUSY.CKENx is set to '1'
            while synchronization is in progress.
          • Serializer Enable bits in the Control A register (CTRLA.TXEN and CTRLA.RXEN).
            SYNCBUSY.TXEN/RXEN is set to '1' while synchronization is in progress.
         The following registers require synchronization when read or written:
          • Transmit Data register (TXDATA) is Write-Synchronized. SYNCBUSY.TXDATA is set to '1' while
             synchronization is in progress.
          • Receive Data register (RXDATA) is Read-Synchronized. SYNCBUSY.RXDATA is set to '1' while
             synchronization is in progress.
         Synchronization is denoted by the Read-Synchronized or Write-Synchronized property in the register
         description.

51.6.11 Loop-Back Mode
        For debugging purposes, the I2S can be configured to loop back the Transmitter to the Receiver. Writing a
        '1' to the Loop-Back Test Mode bit in the Rx Serializer Control register (RXCTRL.RXLOOP)will connect
        SDO to SDI, so that transmitted data is also received.
         Writing RXCTRL.RXLOOP=0 will restore the normal behavior and connection between Receive Serializer
         and SDI pin input. As for other changes to the Serializers configuration, the Receive Serializer must be
         disabled before writing the TXCTRL register to update TXCTRL.RXLOOP.



51.7     I2S Application Examples
         The I2S can support several serial communication modes used in audio or high-speed serial links. Some
         standard applications are shown in the following figures.
         Note: The following examples are not a complete list of serial link applications supported by the I2S.
         Figure 51-7. Audio Application Block Diagram
                                    Serial Clock
                     SCKn
                                    Word Select              EXTERNAL
           I2S         FSn                                      I2S
                                                             RECEIVER
                                    Serial Data Out
                    SDOm


                                              Serial Clock


                                              Word Select


                                           Serial Data Out      MSB                          LSB   MSB

                                                                            Left Channel           Right Channel




        © 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1902
                                                                SAM D5x/E5x Family Data Sheet
                                                                                           I2S - Inter-IC Sound Controller

Figure 51-8. Time Slot Application Block Diagram
                                    Master Clock
                  MCKn

                                    Serial Clock
                   SCKn                                                           EXTERNAL
                                                                                    AUDIO
                                    Frame Sync
   I2S               FSn                                                            CODEC
                                                                                    for First
                                    Serial Data Out                                Time Slot
                    SDO

                                    Serial Data In
                     SDI




                                                                                  EXTERNAL
                                                                                    AUDIO
                                                                                    CODEC
                                                                                  for Second
                                                                                   Time Slot




                                      Serial Clock


                                      Frame Sync                         First Time Slot                          Second Time Slot

                                                                         Dstart                            Dend
                                   Serial Data Out


                                    Serial Data In


Figure 51-9. Codec Application Block Diagram
                                       Master Clock
                   MCKn

                                       Serial Clock
                   SCKn

                                       Frame Sync                                 EXTERNAL
    I2S              FSn                                                            AUDIO
                                                                                   CODEC
                                       Serial Data Out
                     SDO

                                       Serial Data In
                     SDI


                                                         Serial Clock

                                                         Frame Sync                          First Time Slot
                                                                                           Dstart                        Dend
                                                     Serial Data Out


                                                        Serial Data In




© 2019 Microchip Technology Inc.                                  Datasheet                                    DS60001507E-page 1903
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  I2S - Inter-IC Sound Controller

Figure 51-10. PDM Microphones Application Block Diagram

                   MCKn

                                   64 fs Serial Clock
                   SCKn
    2
   IS                                                                   EXTERNAL PDM
                                                                         MICROPHONE
                     FSn
                                                                            for Left
                                   Serial Data In                           Channel
                     SDI

                                                                                  L/RSEL         VDD




                                                                        EXTERNAL PDM
                                                                         MICROPHONE
                                                                            for Right
                                                                            Channel


                                                                                  L/RSEL         GND




                                    Serial Clock

                                   Serial Data In       Right    Left   Right   Left   Right   Left   Right   Left   Right




© 2019 Microchip Technology Inc.                                Datasheet                              DS60001507E-page 1904
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                         I2S - Inter-IC Sound Controller


51.8      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                              RXEN        TXEN        CKEN1         CKEN0       ENABLE         SWRST
 0x01
   ...       Reserved
 0x03
                              7:0     BITDELAY        FSWIDTH[1:0]                   NBSLOTS[2:0]                    SLOTSIZE[1:0]
                             15:8     MCKOUTINV    MCKEN      MCKSEL     SCKOUTINV     SCKSEL       FSOUTINV      FSINV         FSSEL
 0x04        CLKCTRL0
                             23:16                                                         MCKDIV[5:0]
                             31:24                                                       MCKOUTDIV[5:0]
                              7:0     BITDELAY        FSWIDTH[1:0]                   NBSLOTS[2:0]                    SLOTSIZE[1:0]
                             15:8     MCKOUTINV    MCKEN      MCKSEL     SCKOUTINV     SCKSEL       FSOUTINV      FSINV         FSSEL
 0x08        CLKCTRL1
                             23:16                                                         MCKDIV[5:0]
                             31:24                                                       MCKOUTDIV[5:0]
                              7:0                             RXOR1        RXOR0                                 RXRDY1        RXRDY0
 0x0C        INTENCLR
                             15:8                              TXUR1       TXUR0                                 TXRDY1        TXRDY0
 0x0E
   ...       Reserved
 0x0F
                              7:0                             RXOR1        RXOR0                                 RXRDY1        RXRDY0
 0x10        INTENSET
                             15:8                              TXUR1       TXUR0                                 TXRDY1        TXRDY0
 0x12
   ...       Reserved
 0x13
                              7:0                             RXOR1        RXOR0                                 RXRDY1        RXRDY0
 0x14        INTFLAG
                             15:8                              TXUR1       TXUR0                                 TXRDY1        TXRDY0
 0x16
   ...       Reserved
 0x17
                              7:0                              RXEN        TXEN        CKEN1         CKEN0       ENABLE         SWRST
 0x18       SYNCBUSY
                             15:8                                                                                RXDATA        TXDATA
 0x1A
   ...       Reserved
 0x1F
                              7:0      SLOTADJ                            TXSAME          TXDEFAULT[1:0]
                             15:8      BITREV         EXTEND[1:0]        WORDADJ                               DATASIZE[2:0]
 0x20         TXCTRL
                             23:16    SLOTDIS7    SLOTDIS6   SLOTDIS5     SLOTDIS4    SLOTDIS3      SLOTDIS2    SLOTDIS1       SLOTDIS0
                             31:24                                                                                 DMA          MONO
                              7:0      SLOTADJ                CLKSEL                                                 SERMODE[1:0]
                             15:8      BITREV         EXTEND[1:0]        WORDADJ                               DATASIZE[2:0]
 0x24         RXCTRL
                             23:16    SLOTDIS7    SLOTDIS6   SLOTDIS5     SLOTDIS4    SLOTDIS3      SLOTDIS2    SLOTDIS1       SLOTDIS0
                             31:24                                                                  RXLOOP         DMA          MONO
 0x28
   ...       Reserved
 0x2F




          © 2019 Microchip Technology Inc.                             Datasheet                               DS60001507E-page 1905
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                          I2S - Inter-IC Sound Controller

...........continued

  Offset               Name     Bit Pos.

                                  7:0                                         DATA[7:0]
                                 15:8                                        DATA[15:8]
   0x30                TXDATA
                                 23:16                                       DATA[23:16]
                                 31:24                                       DATA[31:24]
                                  7:0                                         DATA[7:0]
                                 15:8                                        DATA[15:8]
   0x34                RXDATA
                                 23:16                                       DATA[23:16]
                                 31:24                                       DATA[31:24]




51.9           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1906
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                       I2S - Inter-IC Sound Controller

51.9.1         Control A

               Name:         CTRLA
               Offset:       0x00
               Reset:        0x00
               Property:     PAC Write-Protection


         Bit         7              6              5                4            3         2             1             0
                                                 RXEN           TXEN           CKEN1     CKEN0        ENABLE        SWRST
   Access                                         R/W            R/W            R/W       R/W           R/W           R/W
    Reset                                          0                0            0         0             0             0


               Bit 5 – RXEN Rx Serializer Enable
               Writing a '0' to this bit will disable the Rx Serializer.
               Writing a '1' to this bit will enable the Rx Serializer.
               Value         Description
               0             The Rx Serializer is disabled.
               1             The Rx Serializer is enabled.

               Bit 4 – TXEN Tx Serializer Enable
               Writing a '0' to this bit will disable the Tx Serializer.
               Writing a '1' to this bit will enable the Tx Serializer.
               Value         Description
               0             The Tx Serializer is disabled.
               1             The Tx Serializer is enabled.

               Bits 2, 3 – CKENx Clock Unit x Enable [x=1..0]
               Writing a '0' to this bit will disable the Clock Unit x.
               Writing a '1' to this bit will enable the Clock Unit x.
               Value         Description
               0             The Clock Unit x is disabled.
               1             The Clock Unit x is enabled.

               Bit 1 – ENABLE Enable
               Writing a '0' to this bit will disable the module.
               Writing a '1' to this bit will enable the module.
               Value         Description
               0             The peripheral is disabled.
               1             The peripheral is enabled.

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit resets all registers to their initial state, and the peripheral will be disabled.
               Writing a '1' to CTRL.SWRST will always take precedence, meaning that all other writes in the same
               write-operation will be discarded.
               The I2S generic clocks must be enabled before triggering Software Reset, hence the logic in all clock
               domains can be reset.
                Value        Description
                0            There is no reset operation ongoing.




           © 2019 Microchip Technology Inc.                                Datasheet                     DS60001507E-page 1907
                                                SAM D5x/E5x Family Data Sheet
                                                            I2S - Inter-IC Sound Controller

 Value        Description
 1            The reset operation is ongoing.




© 2019 Microchip Technology Inc.                Datasheet                DS60001507E-page 1908
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                         I2S - Inter-IC Sound Controller

51.9.2         Clock Unit n Control

               Name:        CLKCTRL
               Offset:      0x04 + n*0x04 [n=0..1]
               Reset:       0x00000000
               Property:    Enable-Protected, PAC Write-Protection


         Bit        31            30              29         28             27                  26    25            24
                                                                             MCKOUTDIV[5:0]
   Access                                        R/W         R/W            R/W             R/W       R/W          R/W
    Reset                                             0       0              0                  0      0            0


         Bit        23            22              21         20             19                  18    17            16
                                                                                  MCKDIV[5:0]
   Access                                        R/W         R/W            R/W             R/W       R/W          R/W
    Reset                                             0       0              0                  0      0            0


         Bit        15            14              13         12              11                 10     9            8
                MCKOUTINV       MCKEN          MCKSEL     SCKOUTINV       SCKSEL         FSOUTINV    FSINV        FSSEL
   Access          R/W            R/W            R/W         R/W            R/W             R/W       R/W          R/W
    Reset            0             0                  0       0              0                  0      0            0


         Bit         7             6                  5       4              3                  2      1            0
                 BITDELAY              FSWIDTH[1:0]                     NBSLOTS[2:0]                    SLOTSIZE[1:0]
   Access          R/W            R/W            R/W         R/W            R/W             R/W       R/W          R/W
    Reset            0             0                  0       0              0                  0      0            0


               Bits 29:24 – MCKOUTDIV[5:0] Master Clock Output Division Factor
               The generic clock selected by MCKSEL is divided by (MCKOUTDIV + 1) to obtain the Master Clock n
               output.

               Bits 21:16 – MCKDIV[5:0] Master Clock Division Factor
               The Master Clock n is divided by (MCKDIV + 1) to obtain the Serial Clock n.

               Bit 15 – MCKOUTINV Master Clock Output Invert
               Value      Description
               0          The Master Clock n is output without inversion.
               1          The Master Clock n is inverted before being output.

               Bit 14 – MCKEN Master Clock Enable
               Note: MCKEN will not enable the clock output when in Slave mode.
               Value        Description
               0            The Master Clock n division and output is disabled.
               1            The Master Clock n division and output is enabled.

               Bit 13 – MCKSEL Master Clock Select
               This field selects the source of the Master Clock n.




           © 2019 Microchip Technology Inc.                           Datasheet                       DS60001507E-page 1909
                                                          SAM D5x/E5x Family Data Sheet
                                                                              I2S - Inter-IC Sound Controller

 MCKSEL             Name                 Description
 0x0                GCLK                 GCLK_I2S_n is used as Master Clock n source
 0x1                MCKPIN               MCKn input pin is used as Master Clock n source

Bit 12 – SCKOUTINV Serial Clock Output Invert
Value      Description
0          The Serial Clock n is output without inversion.
1          The Serial Clock n is inverted before being output.

Bit 11 – SCKSEL Serial Clock Select
This field selects the source of the Serial Clock n.

 SCKSEL           Name              Description
 0x0              MCKDIV            Divided Master Clock n is used as Serial Clock n source
 0x1              SCKPIN            SCKn input pin is used as Serial Clock n source

Bit 10 – FSOUTINV Frame Sync Output Invert
Value      Description
0          The Frame Sync n is output without inversion.
1          The Frame Sync n is inverted before being output.

Bit 9 – FSINV Frame Sync Invert
Value       Description
0           The Frame Sync n is used without inversion.
1           The Frame Sync n is inverted before being used.

Bit 8 – FSSEL Frame Sync Select
This field selects the source of the Frame Sync n.

 FSSEL          Name               Description
 0x0            SCKDIV             Divided Serial Clock n is used as Frame Sync n source
 0x1            FSPIN              FSn input pin is used as Frame Sync n source

Bit 7 – BITDELAY Data Delay from Frame Sync

 BITDELAY                           Name               Description
 0x0                                LJ                 Left Justified (0 Bit Delay)
 0x1                                I2S                I2S (1 Bit Delay)

Bits 6:5 – FSWIDTH[1:0] Frame Sync Width
This field selects the duration of the Frame Sync output pulses.
When not in Burst mode, the Clock unit n operates in continuous mode when enabled, with periodic
Frame Sync pulses and Data samples.
In Burst mode, a single Data transfer starts at each Frame Sync pulse; these pulses are 1-bit wide and
occur only when a Data transfer is requested. Note that the compact stereo modes (16C and 8C) are not
supported in the Burst mode.




© 2019 Microchip Technology Inc.                            Datasheet                      DS60001507E-page 1910
                                                      SAM D5x/E5x Family Data Sheet
                                                                         I2S - Inter-IC Sound Controller

 FSWIDTH[1:0] Name             Description
 0x0                SLOT       Frame Sync Pulse is 1 Slot wide (default for I2S protocol)
 0x1                HALF       Frame Sync Pulse is half a Frame wide
 0x2                BIT        Frame Sync Pulse is 1 Bit wide
 0x3                BURST Clock Unit n operates in Burst mode, with a 1-bit wide Frame Sync pulse per
                          Data sample, only when Data transfer is requested

Bits 4:2 – NBSLOTS[2:0] Number of Slots in Frame
Each Frame for Clock Unit n is composed of (NBSLOTS + 1) Slots.

Bits 1:0 – SLOTSIZE[1:0] Slot Size
Each Slot for Clock Unit n is composed of a number of bits specified by SLOTSIZE.

 SLOTSIZE[1:0]                          Name           Description
 0x0                                    8              8-bit Slot for Clock Unit n
 0x1                                    16             16-bit Slot for Clock Unit n
 0x2                                    24             24-bit Slot for Clock Unit n
 0x3                                    32             32-bit Slot for Clock Unit n




© 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1911
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                      I2S - Inter-IC Sound Controller

51.9.3         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x0C
               Reset:       0x0000
               Property:    PAC Write-Protection


         Bit        15            14            13            12            11            10             9            8
                                              TXUR1         TXUR0                                    TXRDY1        TXRDY0
   Access                                      R/W           R/W                                       R/W           R/W
    Reset                                        0             0                                         0            0


         Bit         7             6             5             4             3             2             1            0
                                              RXOR1         RXOR0                                    RXRDY1        RXRDY0
   Access                                      R/W           R/W                                       R/W           R/W
    Reset                                        0             0                                         0            0


               Bits 12, 13 – TXURx Transmit Underrun x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Transmit Underrun x Interrupt Enable bit, which disables the Transmit
               Underrun x interrupt.
               Value         Description
               0             The Transmit Underrun x interrupt is disabled.
               1             The Transmit Underrun x interrupt is enabled.

               Bits 8, 9 – TXRDYx Transmit Ready x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Transmit Ready x Interrupt Enable bit, which disables the Transmit
               Ready x interrupt.
               Value         Description
               0             The Transmit Ready x interrupt is disabled.
               1             The Transmit Ready x interrupt is enabled.

               Bits 4, 5 – RXORx Receive Overrun x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Receive Overrun x Interrupt Enable bit, which disables the Receive
               Overrun x interrupt.
               Value         Description
               0             The Receive Overrun x interrupt is disabled.
               1             The Receive Overrun x interrupt is enabled.

               Bits 0, 1 – RXRDYx Receive Ready x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Receive Ready x Interrupt Enable bit, which disables the Receive
               Ready x interrupt.
               Value         Description
               0             The Receive Ready x interrupt is disabled.
               1             The Receive Ready x interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1912
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                     I2S - Inter-IC Sound Controller

51.9.4         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x10
               Reset:       0x0000
               Property:    PAC Write-Protection


         Bit        15            14            13            12            11            10            9               8
                                              TXUR1         TXUR0                                    TXRDY1       TXRDY0
   Access                                      R/W           R/W                                       R/W          R/W
    Reset                                        0            0                                         0               0


         Bit         7             6             5            4             3             2             1               0
                                              RXOR1         RXOR0                                    RXRDY1       RXRDY0
   Access                                      R/W           R/W                                       R/W          R/W
    Reset                                        0            0                                         0               0


               Bits 12, 13 – TXURx Transmit Underrun x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Transmit Underrun Interrupt Enable bit, which enables the Transmit
               Underrun interrupt.
               Value         Description
               0             The Transmit Underrun interrupt is disabled.
               1             The Transmit Underrun interrupt is enabled.

               Bits 8, 9 – TXRDYx Transmit Ready x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Transmit Ready Interrupt Enable bit, which enables the Transmit Ready
               interrupt.
                Value        Description
                0            The Transmit Ready interrupt is disabled.
                1            The Transmit Ready interrupt is enabled.

               Bits 4, 5 – RXORx Receive Overrun x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Receive Overrun Interrupt Enable bit, which enables the Receive
               Overrun interrupt.
               Value         Description
               0             The Receive Overrun interrupt is disabled.
               1             The Receive Overrun interrupt is enabled.

               Bits 0, 1 – RXRDYx Receive Ready x Interrupt Enable [x=1..0]
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Receive Ready Interrupt Enable bit, which enables the Receive Ready
               interrupt.
                Value        Description
                0            The Receive Ready interrupt is disabled.
                1            The Receive Ready interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1913
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                  I2S - Inter-IC Sound Controller

51.9.5         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x14
               Reset:      0x0000
               Property:   -


         Bit        15           14            13           12           11           10            9            8
                                              TXUR1       TXUR0                                  TXRDY1       TXRDY0
   Access                                      R/W         R/W                                     R/W          R/W
    Reset                                       0           0                                       0            0


         Bit         7            6             5           4             3            2            1            0
                                              RXOR1       RXOR0                                  RXRDY1       RXRDY0
   Access                                      R/W         R/W                                     R/W          R/W
    Reset                                       0           0                                       0            0


               Bits 12, 13 – TXURx Transmit Underrun x [x=1..0]
               This flag is cleared by writing a '1' to it.
               This flag is set when a Transmit Underrun condition occurs in Sequencer x, and will generate an interrupt
               request if INTENCLR/SET.TXURx is set to '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Transmit Underrun x interrupt flag.

               Bits 8, 9 – TXRDYx Transmit Ready x [x=1..0]
               This flag is cleared by writing to DATAx register or writing a '1' to it.
               This flag is set when Sequencer x is ready to accept a new data word to be transmitted, and will generate
               an interrupt request if INTENCLR/SET.TXRDYx is set to '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Transmit Ready x interrupt flag.

               Bits 4, 5 – RXORx Receive Overrun x [x=1..0]
               This flag is cleared by writing a '1' to it.
               This flag is set when a Receive Overrun condition occurs in Sequencer x, and will generate an interrupt
               request if INTENCLR/SET.RXORx is set to '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Receive Overrun x interrupt flag.

               Bits 0, 1 – RXRDYx Receive Ready x [x=1..0]
               This flag is cleared by reading from DATAx register or writing a '1' to it.
               This flag is set when a Sequencer x has received a new data word, and will generate an interrupt request
               if INTENCLR/SET.RXRDYx is set to '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Receive Ready x interrupt flag.




           © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1914
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                 I2S - Inter-IC Sound Controller

51.9.6         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x18
               Reset:      0x0000
               Property:   -


         Bit        15           14            13          12           11           10           9            8
                                                                                               RXDATA        TXDATA
   Access                                                                                         R            R
    Reset                                                                                         0            0


         Bit         7            6            5           4            3            2            1            0
                                              RXEN        TXEN        CKEN1        CKEN0       ENABLE        SWRST
   Access                                      R           R            R            R            R            R
    Reset                                      0           0            0            0            0            0


               Bit 9 – RXDATA Rx Data Synchronization Status
               This bit is cleared when the synchronization of the Rx DATA Holding (RXDATA) register between the
               clock domains is complete.
               This bit is set when the synchronization of the Rx DATA Holding (RXDATA) register between the clock
               domains is started.

               Bit 8 – TXDATA Tx Data Synchronization Status
               This bit is cleared when the synchronization of the Tx DATA Holding (TXDATA) register between the clock
               domains is complete.
               This bit is set when the synchronization of the Tx DATA Holding (TXDATA) register between the clock
               domains is started.

               Bit 5 – RXEN Rx Serializer Enable Synchronization Status
               This bit is cleared when the synchronization of the CTRLA.RXEN bit between the clock domains is
               complete.
               This bit is set when the synchronization of the CTRLA.RXEN bit between the clock domains is started.

               Bit 4 – TXEN Tx Serializer Enable Synchronization Status
               This bit is cleared when the synchronization of the CTRLA.TXEN bit between the clock domains is
               complete.
               This bit is set when the synchronization of the CTRLA.TXEN bit between the clock domains is started.

               Bits 2, 3 – CKENx Clock Unit x Enable Synchronization Status [x=1..0]
               Bit CKENx is cleared when the synchronization of the CTRLA.CKENx bit between the clock domains is
               complete.
               Bit CKENx is set when the synchronization of the CTRLA.CKENx bit between the clock domains is
               started.

               Bit 1 – ENABLE Enable Synchronization Status
               This bit is cleared when the synchronization of the CTRLA.ENABLE bit between the clock domains is
               complete.
               This bit is set when the synchronization of the CTRLA.ENABLE bit between the clock domains is started.




           © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1915
                                                SAM D5x/E5x Family Data Sheet
                                                                 I2S - Inter-IC Sound Controller

Bit 0 – SWRST Software Reset Synchronization Status
This bit is cleared when the synchronization of the CTRLA.SWRST bit between the clock domains is
complete.
This bit is set when the synchronization of the CTRLA.SWRST bit between the clock domains is started.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 1916
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                        I2S - Inter-IC Sound Controller

51.9.7         Tx Serializer Control

               Name:        TXCTRL
               Offset:      0x20
               Reset:       0x00000000
               Property:    Enable-Protected, Write-Protection


         Bit         31           30                 29          28            27           26           25            24
                                                                                                        DMA          MONO
   Access                                                                                               R/W           R/W
    Reset                                                                                                0             0


         Bit         23           22                 21          20            19           18           17            16
                 SLOTDIS7      SLOTDIS6       SLOTDIS5        SLOTDIS4      SLOTDIS3     SLOTDIS2    SLOTDIS1       SLOTDIS0
   Access            R/W         R/W             R/W             R/W           R/W         R/W          R/W           R/W
    Reset             0            0                 0            0             0            0           0             0


         Bit         15           14                 13          12            11           10           9             8
                  BITREV               EXTEND[1:0]            WORDADJ                               DATASIZE[2:0]
   Access            R/W         R/W             R/W             R/W                       R/W          R/W           R/W
    Reset             0            0                 0            0                          0           0             0


         Bit          7            6                 5            4             3            2           1             0
                 SLOTADJ                                       TXSAME           TXDEFAULT[1:0]
   Access            R/W                                         R/W           R/W         R/W
    Reset             0                                           0             0            0


               Bit 25 – DMA Single or Multiple DMA Channels
               This bit selects whether even-numbered and odd-numbered slots use separate DMA channels or the
               same DMA channel.

               DMA          Name                          Description
               0x0          SINGLE                        Single DMA channel
               0x1          MULTIPLE                      One DMA channel per data channel

               Bit 24 – MONO Mono Mode.

               MONO          Name                Description
               0x0           STEREO              Normal mode
               0x1           MONO                Left channel data is duplicated to right channel

               Bits 16, 17, 18, 19, 20, 21, 22, 23 – SLOTDISx Slot x Disabled for this Serializer [x=7..0]
               This field allows disabling some slots in each transmit frame:
                Value        Description
                0            Slot x is used for data transfer.
                1            Slot x is not used for data transfer and will be output as specified in the TXDEFAULT field.




           © 2019 Microchip Technology Inc.                              Datasheet                       DS60001507E-page 1917
                                                        SAM D5x/E5x Family Data Sheet
                                                                            I2S - Inter-IC Sound Controller

Bit 15 – BITREV Data Formatting Bit Reverse
This bit allows changing the order of data bits in the word in the Formatting Unit.

 BITREV        Name       Description
 0x0           MSBIT      Transfer Data Most Significant Bit (MSB) first (default for I2S protocol)
 0x1           LSBIT      Transfer Data Least Significant Bit (LSB) first

Bits 14:13 – EXTEND[1:0] Data Formatting Bit Extension
This field defines the bit value used to extend data samples in the Formatting Unit.

 EXTEND[1:0]                        Name           Description
 0x0                                ZERO           Extend with zeros
 0x1                                ONE            Extend with ones
 0x2                                MSBIT          Extend with Most Significant Bit
 0x3                                LSBIT          Extend with Least Significant Bit

Bit 12 – WORDADJ Data Word Formatting Adjust
This field defines left or right adjustment of data samples in the word in the Formatting Unit. for details.

 WORDADJ                           Name            Description
 0x0                               RIGHT           Data is right adjusted in word
 0x1                               LEFT            Data is left adjusted in word

Bits 10:8 – DATASIZE[2:0] Data Word Size
This field defines the number of bits in each data sample. For 8-bit compact stereo, two 8-bit data
samples are packed in bits 15 to 0 of the DATAm register. For 16-bit compact stereo, two 16-bit data
samples are packed in bits 31 to 0 of the DATAm register.

 DATASIZE[2:0]                              Name             Description
 0x0                                        32               32 bits
 0x1                                        24               24 bits
 0x2                                        20               20 bits
 0x3                                        18               18 bits
 0x4                                        16               16 bits
 0x5                                        16C              16 bits compact stereo
 0x6                                        8                8 bits
 0x7                                        8C               8 bits compact stereo

Bit 7 – SLOTADJ Data Slot Formatting Adjust
This field defines left or right adjustment of data samples in the slot.




© 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1918
                                                      SAM D5x/E5x Family Data Sheet
                                                                          I2S - Inter-IC Sound Controller

 SLOTADJ                       Name              Description
 0x0                           RIGHT             Data is right adjusted in slot
 0x1                           LEFT              Data is left adjusted in slot

Bit 4 – TXSAME Transmit Data when Underrun.

 TXSAME                Name           Description
 0x0                   ZERO           Zero data transmitted in case of underrun
 0x1                   SAME           Last data transmitted in case of underrun

Bits 3:2 – TXDEFAULT[1:0] Line Default Line when Slot Disabled
This field defines the default value driven on the SDn output pin during all disabled Slots.

 TXDEFAULT[1:0]                    Name        Description
 0x0                               ZERO        Output Default Value is 0
 0x1                               ONE         Output Default Value is 1
 0x2                                           Reserved
 0x3                               HIZ         Output Default Value is high impedance




© 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1919
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                       I2S - Inter-IC Sound Controller

51.9.8         Rx Serializer Control

               Name:        RXCTRL
               Offset:      0x24
               Reset:       0x00000000
               Property:    Enable-Protected, PAC Write-Protection


         Bit         31           30                 29          28            27         26             25            24
                                                                                        RXLOOP          DMA          MONO
   Access                                                                                 R/W           R/W           R/W
    Reset                                                                                  0             0             0


         Bit         23           22                 21          20            19         18             17            16
                 SLOTDIS7      SLOTDIS6       SLOTDIS5        SLOTDIS4      SLOTDIS3   SLOTDIS2      SLOTDIS1       SLOTDIS0
   Access            R/W         R/W             R/W             R/W           R/W        R/W           R/W           R/W
    Reset             0            0                 0            0             0          0             0             0


         Bit         15           14                 13          12            11         10             9             8
                  BITREV               EXTEND[1:0]            WORDADJ                               DATASIZE[2:0]
   Access            R/W         R/W             R/W             R/W                      R/W           R/W           R/W
    Reset             0            0                 0            0                        0             0             0


         Bit          7            6                 5            4             3          2             1             0
                 SLOTADJ                       CLKSEL                                                     SERMODE[1:0]
   Access            R/W                         R/W                                                    R/W           R/W
    Reset             0                              0                                                   0             0


               Bit 26 – RXLOOP Loop-back Test Mode
               This bit enables a loop-back test mode:
                Value      Description
                0          Each Receiver uses its SDn pin as input (default mode).
                1          Receiver uses as input the transmitter output of the other Serializer in the pair: e.g. SD1 for
                           SD0 or SD0 for SD1.

               Bit 25 – DMA Single or Multiple DMA Channels
               This bit selects whether even- and odd-numbered slots use separate DMA channels or the same DMA
               channel.

               DMA          Name                          Description
               0x0          SINGLE                        Single DMA channel
               0x1          MULTIPLE                      One DMA channel per data channel

               Bit 24 – MONO Mono Mode.

               MONO          Name                Description
               0x0           STEREO              Normal mode
               0x1           MONO                Left channel data is duplicated to right channel




           © 2019 Microchip Technology Inc.                              Datasheet                       DS60001507E-page 1920
                                                        SAM D5x/E5x Family Data Sheet
                                                                            I2S - Inter-IC Sound Controller

Bits 16, 17, 18, 19, 20, 21, 22, 23 – SLOTDISx Slot x Disabled for this Serializer [x=7..0]
This field allows disabling some slots in each transmit frame:
 Value        Description
 0            Slot x is used for data transfer.
 1            Slot x is not used for data transfer and will be output as specified in the TXDEFAULT field.

Bit 15 – BITREV Data Formatting Bit Reverse
This bit allows changing the order of data bits in the word in the Formatting Unit.

 BITREV        Name       Description
 0x0           MSBIT      Transfer Data Most Significant Bit (MSB) first (default for I2S protocol)
 0x1           LSBIT      Transfer Data Least Significant Bit (LSB) first

Bits 14:13 – EXTEND[1:0] Data Formatting Bit Extension
This field defines the bit value used to extend data samples in the Formatting Unit.

 EXTEND[1:0]                        Name           Description
 0x0                                ZERO           Extend with zeros
 0x1                                ONE            Extend with ones
 0x2                                MSBIT          Extend with Most Significant Bit
 0x3                                LSBIT          Extend with Least Significant Bit

Bit 12 – WORDADJ Data Word Formatting Adjust
This field defines left or right adjustment of data samples in the word in the Formatting Unit. for details.

 WORDADJ                           Name            Description
 0x0                               RIGHT           Data is right adjusted in word
 0x1                               LEFT            Data is left adjusted in word

Bits 10:8 – DATASIZE[2:0] Data Word Size
This field defines the number of bits in each data sample. For 8-bit compact stereo, two 8-bit data
samples are packed in bits 15 to 0 of the DATAm register. For 16-bit compact stereo, two 16-bit data
samples are packed in bits 31 to 0 of the DATAm register.

 DATASIZE[2:0]                              Name             Description
 0x0                                        32               32 bits
 0x1                                        24               24 bits
 0x2                                        20               20 bits
 0x3                                        18               18 bits
 0x4                                        16               16 bits
 0x5                                        16C              16 bits compact stereo
 0x6                                        8                8 bits




© 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1921
                                                      SAM D5x/E5x Family Data Sheet
                                                                           I2S - Inter-IC Sound Controller

...........continued
 DATASIZE[2:0]                            Name              Description
 0x7                                      8C                8 bits compact stereo

Bit 7 – SLOTADJ Data Slot Formatting Adjust
This field defines left or right adjustment of data samples in the slot.

 SLOTADJ                       Name              Description
 0x0                           RIGHT             Data is right adjusted in slot
 0x1                           LEFT              Data is left adjusted in slot

Bit 5 – CLKSEL Clock Unit Selection.

 CLKSEL                            Name                    Description
 0x0                               CLK0                    Use Clock Unit 0
 0x1                               CLK1                    Use Clock Unit 1

Bits 1:0 – SERMODE[1:0] Serializer Mode.

 SERMODE[1:0]                 Name     Description
 0x0                          RX       Receive
 0x1                                   Reserved
 0x2                          PDM2     Receive one PDM data on each serial clock edge
 0x3                                   Reserved




© 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1922
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                     I2S - Inter-IC Sound Controller

51.9.9         Tx Data

               Name:       TXDATA
               Offset:     0x30
               Reset:      0x00000000
               Property:   Write-Synchronized


         Bit        31            30           29           28                 27       26          25               24
                                                                 DATA[31:24]
   Access          R/W           R/W          R/W           R/W                R/W     R/W          R/W          R/W
    Reset            0            0             0            0                  0       0            0               0


         Bit        23            22           21           20                 19       18          17               16
                                                                 DATA[23:16]
   Access          R/W           R/W          R/W           R/W                R/W     R/W          R/W          R/W
    Reset            0            0             0            0                  0       0            0               0


         Bit        15            14           13           12                 11       10           9               8
                                                                  DATA[15:8]
   Access          R/W           R/W          R/W           R/W                R/W     R/W          R/W          R/W
    Reset            0            0             0            0                  0       0            0               0


         Bit         7            6             5            4                  3       2            1               0
                                                                  DATA[7:0]
   Access          R/W           R/W          R/W           R/W                R/W     R/W          R/W          R/W
    Reset            0            0             0            0                  0       0            0               0


               Bits 31:0 – DATA[31:0] Sample Data
               This register is used to transfer data to the Tx Serializer.
               Data samples written to TXDATA register will be sent to Tx Serializer for transmission, through the
               Transmit Formatting Unit that will apply the formatting specified in the TXCTRL register.




           © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1923
                                                              SAM D5x/E5x Family Data Sheet
                                                                                I2S - Inter-IC Sound Controller

51.9.10 Rx Data

           Name:       RXDATA
           Offset:     0x34
           Reset:      0x00000000
           Property:   Read-Synchronized


     Bit        31           30           29           28                 27       26          25           24
                                                            DATA[31:24]
  Access       R/W          R/W           R/W          R/W                R/W     R/W         R/W          R/W
   Reset         0            0            0            0                  0       0           0            0


     Bit        23           22           21           20                 19       18          17           16
                                                            DATA[23:16]
  Access       R/W          R/W           R/W          R/W                R/W     R/W         R/W          R/W
   Reset         0            0            0            0                  0       0           0            0


     Bit        15           14           13           12                 11       10          9            8
                                                             DATA[15:8]
  Access       R/W          R/W           R/W          R/W                R/W     R/W         R/W          R/W
   Reset         0            0            0            0                  0       0           0            0


     Bit         7            6            5            4                  3       2           1            0
                                                             DATA[7:0]
  Access       R/W          R/W           R/W          R/W                R/W     R/W         R/W          R/W
   Reset         0            0            0            0                  0       0           0            0


           Bits 31:0 – DATA[31:0] Sample Data
           This register is used to transfer data from the Rx Serializer.
           Data samples received by Rx Serializer will be available for reading from RXDATA register, through the
           Receive Formatting Unit, according to formatting information for Rx Serializer in the RXCTRL register.




       © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1924
