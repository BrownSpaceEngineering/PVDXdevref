# 35. SERCOM SPI – SERCOM Serial Peripheral Interface

*Source: `Atmel-SAMD51.pdf`, pages 969-1004 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                SERCOM SPI – SERCOM Serial Peripheral Interface


35.    SERCOM SPI – SERCOM Serial Peripheral Interface

35.1   Overview
       The Serial Peripheral Interface (SPI) is one of the available modes in the Serial Communication Interface
       (SERCOM).
       The SPI uses the SERCOM transmitter and receiver configured as shown in 35.3 Block Diagram. Each
       side, master and slave, depicts a separate SPI containing a Shift register, a transmit buffer and a two-
       level receive buffer. In addition, the SPI master uses the SERCOM baud-rate generator, while the SPI
       slave can use the SERCOM address match logic. Labels in capital letters are synchronous to
       CLK_SERCOMx_APB and accessible by the CPU, while labels in lowercase letters are synchronous to
       the SCK clock.
       Related Links
       33. SERCOM – Serial Communication Interface



35.2   Features
       SERCOM SPI includes the following features:
         • Full-duplex, four-wire interface (MISO, MOSI, SCK, SS)
         • One-level transmit buffer, two-level receive buffer
         • Supports all four SPI modes of operation
         • Single data direction operation allows alternate function on MISO or MOSI pin
         • Selectable LSB- or MSB-first data transfer
         • Can be used with DMA
         • 32-bit Extension for better system bus utilization
         • Master operation:
            – Serial clock speed, fSCK=1/tSCK(1)
            – 8-bit clock generator
            – Hardware controlled SS
            – Optional inter-character spacing
         • Slave Operation:
            – Serial clock speed, fSCK=1/tSSCK(1)
            – Optional 8-bit address match operation
            – Operation in all sleep modes
            – Wake on SS transition
         1.   For tSCK and tSSCK values, refer to SPI Timing Characteristics.
       Related Links
       33. SERCOM – Serial Communication Interface
       33.2 Features




       © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 969
                                                                        SAM D5x/E5x Family Data Sheet
                                                              SERCOM SPI – SERCOM Serial Peripheral Interface


35.3     Block Diagram
         Figure 35-1. Full-Duplex SPI Master Slave Interconnection
                                                             Master           Slave
                      BAUD                   Tx DATA                                             Tx DATA            ADDR/ADDRMASK
                                                                      SCK
                                                                      _SS

                                                                      MISO
                baud rate generator         shift register                                      shift register

                                                                      MOSI



                                              rx buffer                                           rx buffer                ==
                                             Rx DATA                                             Rx DATA              Address Match




35.4     Signal Description
         Table 35-1. SERCOM SPI Signals

          Signal Name                           Type                             Description
          PAD[3:0]                              Digital I/O                      General SERCOM pins

         One signal can be mapped to one of several pins.
         Related Links
         6. I/O Multiplexing and Considerations



35.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

35.5.1   I/O Lines
         In order to use the SERCOM’s I/O lines, the I/O pins must be configured using the IO Pin Controller
         (PORT).
         When the SERCOM is configured for SPI operation, the SERCOM controls the direction and value of the
         I/O pins according to the table below. Both PORT Control bits PINCFGn.PULLEN and
         PINCFGn.DRVSTR are still effective. If the receiver is disabled, the data input pin can be used for other
         purposes. In Master mode, the Slave Select line (SS) is hardware controlled when the Master Slave
         Select Enable bit in the Control B register (CTRLB.MSSEN) is '1'.
         Table 35-2. SPI Pin Configuration

          Pin                                    Master SPI                                    Slave SPI
          MOSI                                   Output                                        Input
          MISO                                   Input                                         Output
          SCK                                    Output                                        Input
          SS                                     Output (CTRLB.MSSEN=1)                        Input




         © 2019 Microchip Technology Inc.                                    Datasheet                           DS60001507E-page 970
                                                             SAM D5x/E5x Family Data Sheet
                                                   SERCOM SPI – SERCOM Serial Peripheral Interface

         The combined configuration of PORT, the Data In Pinout and the Data Out Pinout bit groups in the
         Control A register (CTRLA.DIPO and CTRLA.DOPO) define the physical position of the SPI signals in the
         table above.
         Related Links
         32. PORT - I/O Pin Controller

35.5.2   Power Management
         This peripheral can continue to operate in any Sleep mode where its source clock is running. The
         interrupts can wake-up the device from Sleep modes.
         Related Links
         18. PM – Power Manager

35.5.3   Clocks
         The SERCOM bus clock (CLK_SERCOMx_APB) can be enabled and disabled in the Main Clock
         Controller. Refer to Peripheral Clock Masking for details and default status of this clock.
         A generic clock (GCLK_SERCOMx_CORE) is required to clock the SPI. This clock must be configured
         and enabled in the Generic Clock Controller before using the SPI.
         This generic clock is asynchronous to the bus clock (CLK_SERCOMx_APB). Therefore, writes to certain
         registers will require synchronization to the clock domains.
         Related Links
         14. GCLK - Generic Clock Controller
         15.6.2.6 Peripheral Clock Masking
         35.6.6 Synchronization

35.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). In order to use DMA requests with
         this peripheral the DMAC must be configured first. Refer to DMAC – Direct Memory Access Controller for
         details.
         Related Links
         22. DMAC – Direct Memory Access Controller

35.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first. Refer to Nested Vector Interrupt
         Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

35.5.6   Events
         Not applicable.

35.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will continue normal operation. If the peripheral is
         configured to require periodical service by the CPU through interrupts or similar, improper operation or
         data loss may result during debugging. This peripheral can be forced to halt operation during debugging -
         refer to the Debug Control (DBGCTRL) register for details.




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 971
                                                                 SAM D5x/E5x Family Data Sheet
                                                       SERCOM SPI – SERCOM Serial Peripheral Interface

35.5.8       Register Access Protection
             Registers with write access can be write-protected optionally by the Peripheral Access Controller (PAC).
             PAC write protection is not available for the following registers:
              • Interrupt Flag Clear and Status register (INTFLAG)
              • Status register (STATUS)
              • Data register (DATA)
             Optional PAC write protection is denoted by the "PAC Write-Protection" property in each individual
             register description.
             Write-protection does not apply to accesses through an external debugger.
             Related Links
             27. PAC - Peripheral Access Controller

35.5.9       Analog Connections
             Not applicable.


35.6         Functional Description

35.6.1       Principle of Operation
             The SPI is a high-speed synchronous data transfer interface. It allows high-speed communication
             between the device and peripheral devices.
             The SPI can operate as master or slave. As master, the SPI initiates and controls all data transactions.
             The SPI is single buffered for transmitting and double buffered for receiving.
             When transmitting data, the Data register can be loaded with the next character to be transmitted during
             the current transmission.
             When receiving, the data is transferred to the two-level receive buffer, and the receiver is ready for a new
             character.
             The SPI transaction format is shown in SPI Transaction Format. Each transaction can contain one or
             more characters. The character size is configurable, and can be either 8 or 9 bits.
             Figure 35-2. SPI Transaction Format
                                                                  Transaction
                                        Character


         MOSI/MISO                     Character 0                  Character 1                Character 2


       _SS

             The SPI master must pull the slave select line (SS) of the desired slave low to initiate a transaction. The
             master and slave prepare data to send via their respective Shift registers, and the master generates the
             serial clock on the SCK line.
             Data are always shifted from master to slave on the Master Output Slave Input line (MOSI); data is shifted
             from slave to master on the Master Input Slave Output line (MISO).
             Each time character is shifted out from the master, a character will be shifted out from the slave
             simultaneously. To signal the end of a transaction, the master will pull the SS line high




          © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 972
                                                             SAM D5x/E5x Family Data Sheet
                                                   SERCOM SPI – SERCOM Serial Peripheral Interface

35.6.2    Basic Operation

35.6.2.1 Initialization
          The following registers are enable-protected, meaning that they can only be written when the SPI is
          disabled (CTRL.ENABLE=0):
           •   Control A register (CTRLA), except Enable (CTRLA.ENABLE) and Software Reset (CTRLA.SWRST)
           •   Control B register (CTRLB), except Receiver Enable (CTRLB.RXEN)
           •   Baud register (BAUD)
           •   Address register (ADDR)
          When the SPI is enabled or is being enabled (CTRLA.ENABLE=1), any writing to these registers will be
          discarded.
          When the SPI is being disabled, writing to these registers will be completed after the disabling.
          Enable-protection is denoted by the Enable-Protection property in the register description.
          Initialize the SPI by following these steps:
            1. Select SPI mode in master/slave operation in the Operating Mode bit group in the CTRLA register
                  (CTRLA.MODE= 0x2 or 0x3 ).
            2. Select Transfer mode for the Clock Polarity bit and the Clock Phase bit in the CTRLA register
                  (CTRLA.CPOL and CTRLA.CPHA) if desired.
            3. Select the Frame Format value in the CTRLA register (CTRLA.FORM).
            4. Configure the Data In Pinout field in the Control A register (CTRLA.DIPO) for SERCOM pads of the
                  receiver.
            5. Configure the Data Out Pinout bit group in the Control A register (CTRLA.DOPO) for SERCOM
                  pads of the transmitter.
            6. Select the Character Size value in the CTRLB register (CTRLB.CHSIZE).
            7. Write the Data Order bit in the CTRLA register (CTRLA.DORD) for data direction.
            8. If the SPI is used in Master mode:
                  8.1.     Select the desired baud rate by writing to the Baud register (BAUD).
                  8.2.     If Hardware SS control is required, write '1' to the Master Slave Select Enable bit in CTRLB
                           register (CTRLB.MSSEN).
            9. Enable the receiver by writing the Receiver Enable bit in the CTRLB register (CTRLB.RXEN=1).

35.6.2.2 Enabling, Disabling, and Resetting
          This peripheral is enabled by writing '1' to the Enable bit in the Control A register (CTRLA.ENABLE), and
          disabled by writing '0' to it.
          Writing ‘1’ to the Software Reset bit in the Control A register (CTRLA.SWRST) will reset all registers of
          this peripheral to their initial states, except the DBGCTRL register, and the peripheral is disabled.
          Refer to the CTRLA register description for details.

35.6.2.3 Clock Generation
          In the SPI master operation (CTRLA.MODE=0x3), the serial clock (SCK) is generated internally by the
          SERCOM Baud Rate Generator (BRG).
          In SPI mode, the BRG is set to Synchronous mode. The 8-bit Baud register (BAUD) value is used for
          generating SCK and clocking the Shift register. Refer to Clock Generation – Baud-Rate Generator for
          more details.




         © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 973
                                                            SAM D5x/E5x Family Data Sheet
                                                  SERCOM SPI – SERCOM Serial Peripheral Interface

         In SPI slave operation (CTRLA.MODE is 0x2), the clock is provided by an external master on the SCK
         pin. This clock is used to clock the SPI Shift register.
         Related Links
         33.6.2.3 Clock Generation – Baud-Rate Generator

35.6.2.4 Data Register
         The SPI Transmit Data register (TxDATA) and SPI Receive Data register (RxDATA) share the same I/O
         address, referred to as the SPI Data register (DATA). Writing DATA register will update the Transmit Data
         register. Reading the DATA register will return the contents of the Receive Data register.
35.6.2.5 SPI Transfer Modes
         There are four combinations of SCK phase and polarity to transfer serial data. The SPI Data Transfer
         modes are shown in SPI Transfer Modes (Table) and SPI Transfer Modes (Figure).
         SCK phase is configured by the Clock Phase bit in the CTRLA register (CTRLA.CPHA). SCK polarity is
         programmed by the Clock Polarity bit in the CTRLA register (CTRLA.CPOL). Data bits are shifted out and
         latched in on opposite edges of the SCK signal. This ensures sufficient time for the data signals to
         stabilize.
         Table 35-3. SPI Transfer Modes

         Mode            CPOL              CPHA       Leading Edge                  Trailing Edge
         0               0                 0          Rising, sample                Falling, setup
         1               0                 1          Rising, setup                 Falling, sample
         2               1                 0          Falling, sample               Rising, setup
         3               1                 1          Falling, setup                Rising, sample

         Note:
         Leading edge is the first clock edge in a clock cycle.
         Trailing edge is the second clock edge in a clock cycle.




        © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 974
                                                                             SAM D5x/E5x Family Data Sheet
                                                            SERCOM SPI – SERCOM Serial Peripheral Interface

          Figure 35-3. SPI Transfer Modes

                      Mode 0

                      Mode 2


                      SAMPLE I
                      MOSI/MISO

                      CHANGE 0
                      MOSI PIN
                      CHANGE 0
                      MISO PIN


                      SS


                        MSB first (DORD = 0) MSB         Bit 6           Bit 5           Bit 4           Bit 3           Bit 2           Bit 1           LSB
                        LSB first (DORD = 1) LSB         Bit 1           Bit 2           Bit 3           Bit 4           Bit 5           Bit 6           MSB



                      Mode 1

                      Mode 3


                      SAMPLE I
                      MOSI/MISO

                      CHANGE 0
                      MOSI PIN
                      CHANGE 0
                      MISO PIN


                      SS


                        MSB first (DORD = 0)       MSB           Bit 6           Bit 5           Bit 4           Bit 3           Bit 2           Bit 1         LSB
                        LSB first (DORD = 1)       LSB           Bit 1           Bit 2           Bit 3           Bit 4           Bit 5           Bit 6         MSB

35.6.2.6 Transferring Data
35.6.2.6.1 Master
          In Master mode (CTRLA.MODE=0x3), when Master Slave Enable Select (CTRLB.MSSEN) is ‘1’,
          hardware will control the SS line.
          When Master Slave Select Enable (CTRLB.MSSEN) is '0', the SS line must be configured as an output.
          SS can be assigned to any general purpose I/O pin. When the SPI is ready for a data transaction,
          software must pull the SS line low.
          When writing a character to the Data register (DATA), the character will be transferred to the Shift
          register. Once the content of TxDATA has been transferred to the Shift register, the Data Register Empty
          flag in the Interrupt Flag Status and Clear register (INTFLAG.DRE) will be set. And a new character can
          be written to DATA.
          Each time one character is shifted out from the master, another character will be shifted in from the slave
          simultaneously. If the receiver is enabled (CTRLA.RXEN=1), the contents of the Shift register will be




         © 2019 Microchip Technology Inc.                                         Datasheet                                                          DS60001507E-page 975
                                                               SAM D5x/E5x Family Data Sheet
                                                     SERCOM SPI – SERCOM Serial Peripheral Interface

          transferred to the two-level receive buffer. The transfer takes place in the same clock cycle as the last
          data bit is shifted in. And the Receive Complete Interrupt flag in the Interrupt Flag Status and Clear
          register (INTFLAG.RXC) will be set. The received data can be retrieved by reading DATA.
          When the last character has been transmitted and there is no valid data in DATA, the Transmit Complete
          Interrupt flag in the Interrupt Flag Status and Clear register (INTFLAG.TXC) will be set. When the
          transaction is finished, the master must pull the SS line high to notify the slave. If Master Slave Select
          Enable (CTRLB.MSSEN) is set to '0', the software must pull the SS line high.
35.6.2.6.2 Slave
          In Slave mode (CTRLA.MODE=0x2), the SPI interface will remain inactive with the MISO line tri-stated as
          long as the SS pin is pulled high. Software may update the contents of DATA at any time as long as the
          Data Register Empty flag in the Interrupt Status and Clear register (INTFLAG.DRE) is set.
          When SS is pulled low and SCK is running, the slave will sample and shift out data according to the
          Transaction mode set. When the content of TxDATA has been loaded into the Shift register,
          INTFLAG.DRE will be set, and new data can be written to DATA.
          Similar to the master, the slave will receive one character for each character transmitted. A character will
          be transferred into the two-level receive buffer within the same clock cycle its last data bit is received. The
          received character can be retrieved from DATA when the Receive Complete interrupt flag
          (INTFLAG.RXC) is set.
          When the master pulls the SS line high, the transaction is done and the Transmit Complete Interrupt flag
          in the Interrupt Flag Status and Clear register (INTFLAG.TXC) will be set.
          After DATA is written it takes up to three SCK clock cycles until the content of DATA is ready to be loaded
          into the Shift register on the next character boundary. As a consequence, the first character transferred in
          a SPI transaction will not be the content of DATA. This can be avoided by using the preloading feature.
          Refer to 35.6.3.2 Preloading of the Slave Shift Register.
          When transmitting several characters in one SPI transaction, the data has to be written into DATA register
          with at least three SCK clock cycles left in the current character transmission. If this criteria is not met, the
          previously received character will be transmitted.
          Once the DATA register is empty, it takes three CLK_SERCOM_APB cycles for INTFLAG.DRE to be set.
35.6.2.7 Receiver Error Bit
          The SPI receiver has one error bit: the Buffer Overflow bit (BUFOVF), which can be read from the Status
          register (STATUS). Once an error happens, the bit will stay set until it is cleared by writing '1' to it. The bit
          is also automatically cleared when the receiver is disabled.
          There are two methods for buffer overflow notification, selected by the immediate Buffer Overflow
          Notification bit in the Control A register (CTRLA.IBON):
          If CTRLA.IBON=1, STATUS.BUFOVF is raised immediately upon buffer overflow. Software can then
          empty the receive FIFO by reading RxDATA until the receiver complete Interrupt flag in the Interrupt Flag
          Status and Clear register (INTFLAG.RXC) goes low.
          If CTRLA.IBON=0, the Buffer Overflow condition travels with data through the receive FIFO. After the
          received data is read, STATUS.BUFOVF and INTFLAG.ERROR will be set along with INTFLAG.RXC,
          and RxDATA will be zero.




         © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 976
                                                                    SAM D5x/E5x Family Data Sheet
                                                        SERCOM SPI – SERCOM Serial Peripheral Interface

35.6.3     Additional Features
35.6.3.1 Address Recognition
           When the SPI is configured for slave operation (CTRLA.MODE=0x2) with address recognition
           (CTRLA.FORM is 0x2), the SERCOM address recognition logic is enabled: the first character in a
           transaction is checked for an address match.
           If there is a match, the Receive Complete Interrupt flag in the Interrupt Flag Status and Clear register
           (INTFLAG.RXC) is set, the MISO output is enabled, and the transaction is processed. If the device is in
           Sleep mode, an address match can wake-up the device in order to process the transaction.
           If there is no match, the complete transaction is ignored.
           If a 9-bit frame format is selected, only the lower 8 bits of the Shift register are checked against the
           Address register (ADDR).
           Preload must be disabled (CTRLB.PLOADEN=0) in order to use this mode.

           Related Links
           33.6.3.1 Address Match and Mask

35.6.3.2 Preloading of the Slave Shift Register
           When starting a transaction, the slave will first transmit the contents of the shift register before loading
           new data from DATA. The first character sent can be either the reset value of the shift register (if this is
           the first transmission since the last reset) or the last character in the previous transmission.
           Preloading can be used to preload data into the shift register while SS is high: this eliminates sending a
           dummy character when starting a transaction. If the shift register is not preloaded, the current contents of
           the shift register will be shifted out.
           Only one data character will be preloaded into the shift register while the synchronized SS signal is high.
           If the next character is written to DATA before SS is pulled low, the second character will be stored in
           DATA until transfer begins.
           For proper preloading, sufficient time must elapse between SS going low and the first SCK sampling
           edge, as in Timing Using Preloading. See also the Electrical Characteristics chapters for timing details.
           Preloading is enabled by writing '1' to the Slave Data Preload Enable bit in the CTRLB register
           (CTRLB.PLOADEN).
           Figure 35-4. Timing Using Preloading
                                         Required _SS-to-SCK time
                                           using PRELOADEN
         _SS


         _SS synchronized
         to system domain


         SCK
                                      Synchronization     MISO to SCK
                                     to system domain      setup time


35.6.3.3 Master with Several Slaves
           Master with multiple slaves in parallel is only available when Master Slave Select Enable
           (CTRLB.MSSEN) is set to zero and hardware SS control is disabled. If the bus consists of several SPI




           © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 977
                                                             SAM D5x/E5x Family Data Sheet
                                                       SERCOM SPI – SERCOM Serial Peripheral Interface

        slaves, an SPI master can use general purpose I/O pins to control the SS line to each of the slaves on
        the bus, as shown in Multiple Slaves in Parallel. In this configuration, the single selected SPI slave will
        drive the tri-state MISO line.
        Figure 35-5. Multiple Slaves in Parallel
                                                   MOSI                     MOSI
                                shift register                                          shift register
                                                   MISO                     MISO
                                                   SCK                      SCK
                                                  _SS[0]                    _SS               SPI Slave 0



                              SPI Master

                                                 _SS[n-1]                   MOSI
                                                                                        shift register
                                                                            MISO
                                                                            SCK
                                                                            _SS               SPI Slave n-1

        Another configuration is multiple slaves in series, as in Multiple Slaves in Series. In this configuration, all
        n attached slaves are connected in series. A common SS line is provided to all slaves, enabling them
        simultaneously. The master must shift n characters for a complete transaction. Depending on the Master
        Slave Select Enable bit (CTRLB.MSSEN), the SS line can be controlled either by hardware or user
        software and normal GPIO.
        Figure 35-6. Multiple Slaves in Series

                              shift register      MOSI                       MOSI        shift register
                                                  MISO                       MISO
                                                  SCK                        SCK
                           SPI Master               _SS                      _SS                SPI Slave 0




                                                                             MOSI        shift register
                                                                             MISO
                                                                             SCK
                                                                             _SS                SPI Slave n-1


35.6.3.4 Loop-Back Mode
        For Loop-back mode, configure the Data In Pinout (CTRLA.DIPO) and Data Out Pinout (CTRLA.DOPO)
        to use the same data pins for transmit and receive. The loop-back is through the pad, so the signal is also
        available externally.

35.6.3.5 Hardware Controlled SS
        In Master mode, a single SS chip select can be controlled by hardware by writing the Master Slave Select
        Enable (CTRLB.MSSEN) bit to '1'. In this mode, the SS pin is driven low for a minimum of one baud cycle
        before transmission begins, and stays low for a minimum of one baud cycle after transmission completes.
        If back-to-back frames are transmitted, the SS pin will always be driven high for a minimum of one baud
        cycle between frames.
        In Hardware Controlled SS, the time T is between one and two baud cycles depending on the SPI
        Transfer mode.




        © 2019 Microchip Technology Inc.                      Datasheet                                  DS60001507E-page 978
                                                                             SAM D5x/E5x Family Data Sheet
                                                              SERCOM SPI – SERCOM Serial Peripheral Interface

         Figure 35-7. Hardware Controlled SS

                      T                                                      T        T       T                                  T

         _SS

         SCK


               T = 1 to 2 baud cycles
         When CTRLB.MSSEN=0, the SS pin(s) is/are controlled by user software and normal GPIO.

35.6.3.6 Slave Select Low Detection
         In Slave mode, the SPI can wake the CPU when the slave select (SS) goes low. When the Slave Select
         Low Detect is enabled (CTRLB.SSDE=1), a high-to-low transition will set the Slave Select Low Interrupt
         flag (INTFLAG.SSL) and the device will wake-up if applicable.

35.6.3.7 Master Inter-Character Spacing
         When configured as master, inter-character spacing can be increased by writing a non-zero value to the
         Inter-Character Spacing bit field in the Control C register (CTRLC.ICSPACE). When non-zero,
         CTRLC.ICSPACE represents the minimum number of baud cycles that the SCK clock line does not toggle
         and the next character is stalled.
         The figure gives an example for CTRLC.ICSPACE=4; In this case, the SCK is inactive for 4 baud cycles.
         Figure 35-8. Four Cycle Inter-Character Spacing Example
                                                                             T    T       T   T




                      SCK


                            T = 1 baud cycle

35.6.3.8 32-bit Extension
         For better system bus utilization, 32-bit data receive and transmit can be enabled by writing to the Data
         32-bit bit field in the Control C register (CTRLC.DATA32B=1). When enabled, write and read transaction
         to/from the DATA register are 32 bit in size.
         If frames are not multiples of 4 Bytes, the Length Counter (LENGTH.LEN) and Length Enable
         (LENGTH.LENEN) must be configured before data transfer begins. LENGTH.LEN must be enabled only
         when CTRLC.DATA32B is enabled.
         The figure below shows the order of transmit and receive when using 32-bit mode. Bytes are transmitted
         or received and stored in order from 0 to 3.
         Only 8-bit character size is supported.
         Figure 35-9. 32-bit Extension Byte Ordering

                                               APB Write/Read        BYTE3        BYTE2           BYTE1   BYTE0
                                               Bit Position     31                                                0



         32-bit Extension Slave Operation
         The figure below shows a transaction with 32-bit Extension enabled (CTRLC.DATA32B=1). When
         address recognition is enabled (CTRLA.FORM=0x2) and there is an address match, the address is




        © 2019 Microchip Technology Inc.                                         Datasheet                            DS60001507E-page 979
                                                             SAM D5x/E5x Family Data Sheet
                                                 SERCOM SPI – SERCOM Serial Peripheral Interface

loaded into the FIFO as Byte zero and data begins with Byte 1. INTFLAGS.RXC will then be raised for
every 4 Bytes transferred. For transmit, there is a 32-bit holding buffer in the core domain. Once DATA
has been registered in the core domain, INTFLAG.DRE will be raised, so that the next 32 bits can be
written to the DATA register.
Figure 35-10. 32-bit Extension Slave Operation
                                         RXC interrupt                                 RXC interrupt



                                                S                                         S
                               ADDRESS                   Byte 0 Byte 1 Byte 2 Byte 3
                                                W                                         W

When utilizing the length counter, the LENGTH register must be written before the frame begins. If the
frame length while SS is low is not a multiple of LENGTH.LEN Bytes, the Length Error Status bit
(STATUS.LENERR) is raised. If LENGTH.LEN is not a multiple of 4 Bytes, the final INTFLAG.RXC
interrupt will be raised when the last Byte is received.
The length count is based on the received Bytes, or the number of clocks if the receiver is not enabled. If
pre-loading is disabled and DATA is written to for transmit before SCK starts, transmitted data will be
delayed by one Byte, but the length counter will still increment for the first (empty) Byte transmission.
When the counter reaches LENGTH.LEN, the internal length counter, Rx Byte counter, and Tx Byte
counter are reset. If multiple lengths are to be transmitted, INTFLAG.TXC must go high before writing
DATA for subsequent lengths.
If there is a Length Error (STATUS.LENERR), the remaining Bytes in the length will be transmitted at the
beginning of the next frame. If this is not desired, the SERCOM must be disabled and re-enabled in order
to flush the Tx and Rx pipelines.
Writing the LENGTH register while a frame is in progress will produce unpredictable results. If
LENGTH.LENEN is not configured and a frame is not a multiple of 4 Bytes (while SS is low), the
remainder will be transmitted in the next frame.

32-bit Extension Master Operation
When using the SPI configured as Master, the Length and the Length Enable bit fields (LENGTH.LEN
and LENGTH.LENEN) must be written before the frame begins. When LENGTH.LENEN is written to '1',
the value of LENGTH.LEN determines the number of data bytes in the transaction from 1 to 255.
For receive data, INTFLAG.RXC is raised every 4 Bytes received. If LENGTH.LEN is not a multiple of 4
Bytes, the final INTFLAG.RXC is set when the final byte is received.
For transmit, there is a holding buffer for the 32-bit data in the core domain. Once DATA has been
registered in the core domain, INTFLAG.DRE will be raised so that the next 32 bits can be written to the
DATA register.
If multiple lengths are to be transmitted, INTFLAG.TXC must go high before writing DATA for subsequent
lengths.




© 2019 Microchip Technology Inc.                               Datasheet                               DS60001507E-page 980
                                                             SAM D5x/E5x Family Data Sheet
                                                    SERCOM SPI – SERCOM Serial Peripheral Interface

35.6.4   DMA, Interrupts, and Events
         Table 35-4. Module Request for SERCOM SPI

          Condition                            Request
                                               DMA                                                Interrupt     Event
          Data Register Empty (DRE)            Yes                                                Yes           NA
                                               (request cleared when data is written)

          Receive Complete (RXC)               Yes                                                Yes
                                               (request cleared when data is read)

          Transmit Complete (TXC)              NA                                                 Yes
          Slave Select low (SSL)               NA                                                 Yes
          Error (ERROR)                        NA                                                 Yes

35.6.4.1 DMA Operation
         The SPI generates the following DMA requests:
           • Data received (RX): The request is set when data is available in the receive FIFO. The request is
             cleared when DATA is read.
           • Data transmit (TX): The request is set when the transmit buffer (TX DATA) is empty. The request is
             cleared when DATA is written.

35.6.4.2 Interrupts
         The SPI has the following interrupt sources. These are asynchronous interrupts, and can wake-up the
         device from any Sleep mode:
           •   Data Register Empty (DRE)
           •   Receive Complete (RXC)
           •   Transmit Complete (TXC)
           •   Slave Select Low (SSL)
           •   Error (ERROR)
         Each interrupt source has its own Interrupt flag. The Interrupt flag in the Interrupt Flag Status and Clear
         register (INTFLAG) will be set when the Interrupt condition is met. Each interrupt can be individually
         enabled by writing '1' to the corresponding bit in the Interrupt Enable Set register (INTENSET), and
         disabled by writing '1' to the corresponding bit in the Interrupt Enable Clear register (INTENCLR).
         An interrupt request is generated when the Interrupt flag is set and if the corresponding interrupt is
         enabled. The interrupt request remains active until either the Interrupt flag is cleared, the interrupt is
         disabled, or the SPI is reset. For details on clearing Interrupt flags, refer to the INTFLAG register
         description.
         The value of INTFLAG indicates which interrupt is executed. Note that interrupts must be globally
         enabled for interrupt requests. Refer to Nested Vector Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

35.6.4.3 Events
         Not applicable.




         © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 981
                                                             SAM D5x/E5x Family Data Sheet
                                                 SERCOM SPI – SERCOM Serial Peripheral Interface

35.6.5   Sleep Mode Operation
         The behavior in Sleep mode is depending on the master/slave configuration and the Run In Standby bit in
         the Control A register (CTRLA.RUNSTDBY):
           • Master operation, CTRLA.RUNSTDBY=1: The peripheral clock GCLK_SERCOM_CORE will
             continue to run in Idle Sleep mode and in Standby Sleep mode. Any interrupt can wake-up the
             device.
           • Master operation, CTRLA.RUNSTDBY=0: GLK_SERCOMx_CORE will be disabled after the ongoing
             transaction is finished. Any interrupt can wake up the device.
           • Slave operation, CTRLA.RUNSTDBY=1: The Receive Complete interrupt can wake-up the device.
           • Slave operation, CTRLA.RUNSTDBY=0: All reception will be dropped, including the ongoing
             transaction.

35.6.6   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset bit in the CTRLA register (CTRLA.SWRST)
           • Enable bit in the CTRLA register (CTRLA.ENABLE)
           • Receiver Enable bit in the CTRLB register (CTRLB.RXEN)
         Note: CTRLB.RXEN is write-synchronized somewhat differently. See also CTRLB register for details.
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 982
                                                                   SAM D5x/E5x Family Data Sheet
                                                            SERCOM SPI – SERCOM Serial Peripheral Interface


35.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0     RUNSTDBY                                         MODE[2:0]                   ENABLE       SWRST
                             15:8                                                                                                IBON
 0x00         CTRLA
                             23:16                                 DIPO[1:0]                                             DOPO[1:0]
                             31:24                   DORD       CPOL       CPHA                              FORM[3:0]
                              7:0                  PLOADEN                                                        CHSIZE[2:0]
                             15:8            AMODE[1:0]        MSSEN                                                 SSDE
 0x04         CTRLB
                             23:16                                                                                   RXEN
                             31:24
                              7:0                                                             ICSPACE[5:0]
                             15:8
 0x08         CTRLC
                             23:16
                             31:24                                                                                              DATA32B
 0x0C          BAUD           7:0                                                BAUD[7:0]
 0x0D
   ...       Reserved
 0x13
 0x14        INTENCLR         7:0      ERROR                                                 SSL        RXC          TXC         DRE
 0x15        Reserved
 0x16        INTENSET         7:0      ERROR                                                 SSL        RXC          TXC         DRE
 0x17        Reserved
 0x18        INTFLAG          7:0      ERROR                                                 SSL        RXC          TXC         DRE
 0x19        Reserved
                              7:0                                                                     BUFOVF
 0x1A         STATUS
                             15:8                                                       LENERR
                              7:0                                         LENGTH                       CTRLB       ENABLE       SWRST
                             15:8
 0x1C       SYNCBUSY
                             23:16
                             31:24
 0x20
   ...       Reserved
 0x21
                              7:0                                                 LEN[7:0]
 0x22         LENGTH
                             15:8                                                                                               LENEN
                              7:0                                                ADDR[7:0]
                             15:8
 0x24          ADDR
                             23:16                                             ADDRMASK[7:0]
                             31:24
                              7:0                                                DATA[7:0]
                             15:8                                                DATA[15:8]
 0x28          DATA
                             23:16                                              DATA[23:16]
                             31:24                                              DATA[31:24]




          © 2019 Microchip Technology Inc.                             Datasheet                                  DS60001507E-page 983
                                                                  SAM D5x/E5x Family Data Sheet
                                                         SERCOM SPI – SERCOM Serial Peripheral Interface

...........continued

  Offset               Name    Bit Pos.

   0x2C
     ...           Reserved
   0x2F
   0x30            DBGCTRL        7:0                                                                               DBGSTOP




35.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Refer to 35.6.6 Synchronization
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Refer to 35.5.8 Register Access Protection.




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 984
                                                                         SAM D5x/E5x Family Data Sheet
                                                           SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00000000
               Property:    PAC Write-Protection, Enable-Protected, Write-Synchronized


         Bit        31            30            29                 28          27         26               25                24
                                 DORD          CPOL               CPHA                         FORM[3:0]
   Access                        R/W           R/W                R/W         R/W        R/W               R/W               R/W
    Reset                          0             0                 0           0          0                 0                 0


         Bit        23            22            21                 20          19         18               17                16
                                                      DIPO[1:0]                                                  DOPO[1:0]
   Access                                      R/W                R/W                                      R/W               R/W
    Reset                                        0                 0                                        0                 0


         Bit        15            14            13                 12          11         10                9                 8
                                                                                                                         IBON
   Access                                                                                                                    R/W
    Reset                                                                                                                     0


         Bit         7             6             5                 4           3          2                 1                 0
                RUNSTDBY                                                    MODE[2:0]                 ENABLE            SWRST
   Access           R/W                                           R/W         R/W        R/W               R/W               R/W
    Reset            0                                             0           0          0                 0                 0


               Bit 30 – DORD Data Order
               This bit selects the data order when a character is shifted out from the Shift register.
               This bit is not synchronized.
                Value       Description
                0           MSB is transferred first.
                1           LSB is transferred first.

               Bit 29 – CPOL Clock Polarity
               In combination with the Clock Phase bit (CPHA), this bit determines the SPI Transfer mode.
               This bit is not synchronized.
                Value       Description
                0           SCK is low when idle. The leading edge of a clock cycle is a rising edge, while the trailing
                            edge is a falling edge.
                1           SCK is high when idle. The leading edge of a clock cycle is a falling edge, while the trailing
                            edge is a rising edge.

               Bit 28 – CPHA Clock Phase
               In combination with the Clock Polarity bit (CPOL), this bit determines the SPI Transfer mode.
               This bit is not synchronized.




           © 2019 Microchip Technology Inc.                              Datasheet                          DS60001507E-page 985
                                                         SAM D5x/E5x Family Data Sheet
                                                SERCOM SPI – SERCOM Serial Peripheral Interface

 Mode            CPOL                  CPHA         Leading Edge                 Trailing Edge
 0x0             0                     0            Rising, sample               Falling, change
 0x1             0                     1            Rising, change               Falling, sample
 0x2             1                     0            Falling, sample              Rising, change
 0x3             1                     1            Falling, change              Rising, sample

 Value        Description
 0            The data is sampled on a leading SCK edge and changed on a trailing SCK edge.
 1            The data is sampled on a trailing SCK edge and changed on a leading SCK edge.

Bits 27:24 – FORM[3:0] Frame Format
This bit field selects the various frame formats supported by the SPI in Slave mode. When the 'SPI frame
with address' format is selected, the first byte received is checked against the ADDR register.

 FORM[3:0]                         Name                       Description
 0x0                               SPI                        SPI frame
 0x1                               -                          Reserved
 0x2                               SPI_ADDR                   SPI frame with address
 0x3-0xF                           -                          Reserved

Bits 21:20 – DIPO[1:0] Data In Pinout
These bits define the Data In (DI) pad configurations.
In master operation, DI is MISO.
In slave operation, DI is MOSI.
These bits are not synchronized.

 DIPO[1:0]               Name                             Description
 0x0                     PAD[0]                           SERCOM PAD[0] is used as data input
 0x1                     PAD[1]                           SERCOM PAD[1] is used as data input
 0x2                     PAD[2]                           SERCOM PAD[2] is used as data input
 0x3                     PAD[3]                           SERCOM PAD[3] is used as data input

Bits 17:16 – DOPO[1:0] Data Out Pinout
This bit defines the available pad configurations for Data Out (DO) and the Serial Clock (SCK). In slave
operation, the Slave Select (SS) line is controlled by DOPO, while in master operation the SS line is
controlled by the port configuration.
In master operation, DO is MOSI.
In slave operation, DO is MISO.
These bits are not synchronized.

 DOPO DO             SCK      Slave SS Master SS
 0x0       PAD[0] PAD[1] PAD[2]               PAD[2] Master SS pin when MSSEN = 1 otherwise System
                                              configuration




© 2019 Microchip Technology Inc.                           Datasheet                       DS60001507E-page 986
                                                        SAM D5x/E5x Family Data Sheet
                                           SERCOM SPI – SERCOM Serial Peripheral Interface

...........continued
 DOPO DO             SCK      Slave SS Master SS
 0x1       Reserved
 0x2       PAD[3] PAD[1] PAD[2]         PAD[2] Master SS pin when MSSEN = 1 otherwise System
                                        configuration
 0x3       Reserved

Bit 8 – IBON Immediate Buffer Overflow Notification
This bit controls when the Buffer Overflow Status bit (STATUS.BUFOVF) is set when a buffer overflow
occurs.
This bit is not synchronized.
 Value       Description
 0           STATUS.BUFOVF is set when it occurs in the data stream.
 1           STATUS.BUFOVF is set immediately upon buffer overflow.

Bit 7 – RUNSTDBY Run In Standby
This bit defines the functionality in Standby Sleep mode.
These bits are not synchronized.

 RUNSTDBY Slave                                              Master
 0x0              Disabled. All reception is dropped,        Generic clock is disabled when ongoing
                  including the ongoing transaction.         transaction is finished. All interrupts can wake-
                                                             up the device.
 0x1              Ongoing transaction continues, wake on     Generic clock is enabled while in sleep modes.
                  Receive Complete interrupt.                All interrupts can wake-up the device.

Bits 4:2 – MODE[2:0] Operating Mode
These bits must be written to 0x2 or 0x3 to select the SPI of the SERCOM.
0x2: SPI slave operation
0x3: SPI master operation
These bits are not synchronized.

Bit 1 – ENABLE Enable
Due to synchronization, there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRL.ENABLE will read back immediately and the Synchronization Enable
Busy bit in the Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE is
cleared when the operation is complete.
This bit is not enable-protected.
 Value       Description
 0           The peripheral is disabled or being disabled.
 1           The peripheral is enabled or being enabled.

Bit 0 – SWRST Software Reset
Writing '0' to this bit has no effect.
Writing '1' to this bit resets all registers in the SERCOM, except DBGCTRL, to their initial state, and the
SERCOM will be disabled.




© 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 987
                                                  SAM D5x/E5x Family Data Sheet
                                         SERCOM SPI – SERCOM Serial Peripheral Interface

Writing ''1' to CTRL.SWRST will always take precedence, meaning that all other writes in the same write-
operation will be discarded. Any register write access during the ongoing Reset will result in an APB error.
Reading any register will return the Reset value of the register.
Due to synchronization, there is a delay from writing CTRLA.SWRST until the Reset is complete.
CTRLA.SWRST and SYNCBUSY. SWRST will both be cleared when the Reset is complete.
This bit is not enable-protected.
 Value        Description
 0            There is no Reset operation ongoing.
 1            The Reset operation is ongoing.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 988
                                                                    SAM D5x/E5x Family Data Sheet
                                                            SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.2         Control B

               Name:          CTRLB
               Offset:        0x04
               Reset:         0x00000000
               Property:      PAC Write-Protection, Enable-Protected, Write-Synchronized


         Bit         31                30         29           28           27            26            25            24


   Access
    Reset


         Bit         23                22         21           20           19            18            17            16
                                                                                                       RXEN
   Access                                                                                               R/W
    Reset                                                                                                0


         Bit         15                14         13           12            11           10             9             8
                          AMODE[1:0]            MSSEN                                                  SSDE
   Access            R/W           R/W           R/W                                                    R/W
    Reset             0                0          0                                                      0


         Bit          7                6          5            4             3             2             1             0
                                 PLOADEN                                                            CHSIZE[2:0]
   Access                          R/W                                                    R/W           R/W           R/W
    Reset                              0                                                   0             0             0


               Bit 17 – RXEN Receiver Enable
               Writing '0' to this bit will disable the SPI receiver immediately. The receive buffer will be flushed, data from
               ongoing receptions will be lost and STATUS.BUFOVF will be cleared.
               Writing '1' to CTRLB.RXEN when the SPI is disabled will set CTRLB.RXEN immediately. When the SPI is
               enabled, CTRLB.RXEN will be cleared, SYNCBUSY.CTRLB will be set and remain set until the receiver is
               enabled. When the receiver is enabled CTRLB.RXEN will read back as '1'.
               Writing '1' to CTRLB.RXEN when the SPI is enabled will set SYNCBUSY.CTRLB, which will remain set
               until the receiver is enabled, and CTRLB.RXEN will read back as '1'.
               This bit is not enable-protected.
                Value        Description
                0            The receiver is disabled or being enabled.
                1            The receiver is enabled or it will be enabled when SPI is enabled.

               Bits 15:14 – AMODE[1:0] Address Mode
               These bits set the Slave Addressing mode when the frame format (CTRLA.FORM) with address is used.
               They are unused in Master mode.

               AMODE[1:0] Name                Description
               0x0               MASK         ADDRMASK is used as a mask to the ADDR register
               0x1               2_ADDRS The slave responds to the two unique addresses in ADDR and ADDRMASK




           © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 989
                                                          SAM D5x/E5x Family Data Sheet
                                                 SERCOM SPI – SERCOM Serial Peripheral Interface

...........continued
 AMODE[1:0] Name                   Description
 0x2              RANGE            The slave responds to the range of addresses between and including ADDR
                                   and ADDRMASK. ADDR is the upper limit
 0x3              -                Reserved

Bit 13 – MSSEN Master Slave Select Enable
This bit enables hardware Slave Select (SS) control.
 Value      Description
 0          Hardware SS control is disabled.
 1          Hardware SS control is enabled.

Bit 9 – SSDE Slave Select Low Detect Enable
This bit enables wake-up when the Slave Select (SS) pin transitions from high to low.
 Value      Description
 0          SS low detector is disabled.
 1          SS low detector is enabled.

Bit 6 – PLOADEN Slave Data Preload Enable
Setting this bit will enable preloading of the Slave Shift register when there is no transfer in progress. If
the SS line is high when DATA is written, it will be transferred immediately to the Shift register.

Bits 2:0 – CHSIZE[2:0] Character Size

 CHSIZE[2:0]                                       Name               Description
 0x0                                               8BIT               8 bits
 0x1                                               9BIT               9 bits
 0x2-0x7                                           -                  Reserved




© 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 990
                                                                  SAM D5x/E5x Family Data Sheet
                                                        SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.3         Control C

               Name:       CTRLC
               Offset:     0x08
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31            30           29            28           27              26         25              24
                                                                                                                  DATA32B
   Access                                                                                                           R/W
    Reset                                                                                                            0


         Bit        23            22           21            20           19              18         17              16


   Access
    Reset


         Bit        15            14           13            12           11              10             9           8


   Access
    Reset


         Bit         7            6             5            4             3                  2          1           0
                                                                               ICSPACE[5:0]
   Access                                      R/W          R/W           R/W             R/W        R/W            R/W
    Reset                                       0            0             0                  0          0           0


               Bit 24 – DATA32B Data 32 Bit
               This bit enables 32-bit Extension for read and write transactions to the DATA register.
               When disabled, access is according to CTRLB.CHSIZE.
                Value      Description
                0          Transactions from and to DATA register are 8-bit
                1          Transactions from and to DATA register are 32-bit

               Bits 5:0 – ICSPACE[5:0] Inter-Character Spacing
               When non-zero, CTRLC.ICSPACE selects the minimum number of baud cycles the SCK line will not
               toggle between characters.
                Value      Description
                0x00       Inter-Character Spacing is disabled
                0x01-0x The minimum Inter-Character Spacing
                3F




           © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 991
                                                               SAM D5x/E5x Family Data Sheet
                                                     SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.4         Baud Rate

               Name:       BAUD
               Offset:     0x0C
               Reset:      0x00
               Property:   PAC Write-Protection, Enable-Protected


         Bit        7             6            5          4                 3      2            1           0
                                                               BAUD[7:0]
   Access          R/W          R/W           R/W        R/W               R/W    R/W          R/W         R/W
    Reset           0             0            0          0                 0      0            0           0


               Bits 7:0 – BAUD[7:0] Baud Register
               These bits control the clock generation, as described in the SERCOM Clock Generation – Baud-Rate
               Generator.
               Related Links
               33.6.2.3 Clock Generation – Baud-Rate Generator




           © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 992
                                                                     SAM D5x/E5x Family Data Sheet
                                                           SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.5         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x14
               Reset:       0x00
               Property:    PAC Write-Protection
               This register allows the user to disable an interrupt without read-modify-write operation. Changes in this
               register will also be reflected in the Interrupt Enable Set register (INTENSET).


         Bit         7              6             5              4             3              2             1            0
                  ERROR                                                       SSL           RXC            TXC          DRE
   Access           R/W                                                       R/W           R/W            R/W          R/W
    Reset            0                                                         0              0             0            0


               Bit 7 – ERROR Error Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Error Interrupt Enable bit, which disables the Error interrupt.
               Value         Description
               0             Error interrupt is disabled.
               1             Error interrupt is enabled.

               Bit 3 – SSL Slave Select Low Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Slave Select Low Interrupt Enable bit, which disables the Slave Select
               Low interrupt.
                Value        Description
                0            Slave Select Low interrupt is disabled.
                1            Slave Select Low interrupt is enabled.

               Bit 2 – RXC Receive Complete Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Receive Complete Interrupt Enable bit, which disables the Receive
               Complete interrupt.
               Value         Description
               0             Receive Complete interrupt is disabled.
               1             Receive Complete interrupt is enabled.

               Bit 1 – TXC Transmit Complete Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Transmit Complete Interrupt Enable bit, which disable the Transmit
               Complete interrupt.
               Value         Description
               0             Transmit Complete interrupt is disabled.
               1             Transmit Complete interrupt is enabled.

               Bit 0 – DRE Data Register Empty Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Data Register Empty Interrupt Enable bit, which disables the Data
               Register Empty interrupt.




           © 2019 Microchip Technology Inc.                            Datasheet                             DS60001507E-page 993
                                                   SAM D5x/E5x Family Data Sheet
                                          SERCOM SPI – SERCOM Serial Peripheral Interface

 Value        Description
 0            Data Register Empty interrupt is disabled.
 1            Data Register Empty interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet            DS60001507E-page 994
                                                                     SAM D5x/E5x Family Data Sheet
                                                          SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.6         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x16
               Reset:       0x00
               Property:    PAC Write-Protection
               This register allows the user to disable an interrupt without read-modify-write operation. Changes in this
               register will also be reflected in the Interrupt Enable Clear register (INTENCLR).


         Bit         7              6             5              4             3             2              1           0
                  ERROR                                                       SSL           RXC           TXC          DRE
   Access           R/W                                                       R/W           R/W           R/W          R/W
    Reset            0                                                         0             0              0           0


               Bit 7 – ERROR Error Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Error Interrupt Enable bit, which enables the Error interrupt.
               Value         Description
               0             Error interrupt is disabled.
               1             Error interrupt is enabled.

               Bit 3 – SSL Slave Select Low Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Slave Select Low Interrupt Enable bit, which enables the Slave Select Low
               interrupt.
                Value        Description
                0            Slave Select Low interrupt is disabled.
                1            Slave Select Low interrupt is enabled.

               Bit 2 – RXC Receive Complete Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Receive Complete Interrupt Enable bit, which enables the Receive
               Complete interrupt.
               Value         Description
               0             Receive Complete interrupt is disabled.
               1             Receive Complete interrupt is enabled.

               Bit 1 – TXC Transmit Complete Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Transmit Complete Interrupt Enable bit, which enables the Transmit
               Complete interrupt.
               Value         Description
               0             Transmit Complete interrupt is disabled.
               1             Transmit Complete interrupt is enabled.

               Bit 0 – DRE Data Register Empty Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Data Register Empty Interrupt Enable bit, which enables the Data Register
               Empty interrupt.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 995
                                                   SAM D5x/E5x Family Data Sheet
                                          SERCOM SPI – SERCOM Serial Peripheral Interface

 Value        Description
 0            Data Register Empty interrupt is disabled.
 1            Data Register Empty interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet            DS60001507E-page 996
                                                                   SAM D5x/E5x Family Data Sheet
                                                         SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.7         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x18
               Reset:       0x00
               Property:    -


         Bit         7             6             5             4             3             2            1             0
                  ERROR                                                    SSL           RXC           TXC           DRE
   Access           R/W                                                    R/W            R            R/W            R
    Reset            0                                                       0             0            0             0


               Bit 7 – ERROR Error
               This flag is cleared by writing '1' to it.
               This bit is set when any error is detected. Errors that will set this flag have corresponding Status flags in
               the STATUS register. The BUFOVF error and the LENERR error will set this Interrupt flag.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the flag.

               Bit 3 – SSL Slave Select Low
               This flag is cleared by writing '1' to it.
               This bit is set when a high to low transition is detected on the _SS pin in Slave mode and Slave Select
               Low Detect (CTRLB.SSDE) is enabled.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the flag.

               Bit 2 – RXC Receive Complete
               This flag is cleared by reading the Data (DATA) register or by disabling the receiver.
               This flag is set when there are unread data in the receive buffer. If address matching is enabled, the first
               data received in a transaction will be an address.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit has no effect.

               Bit 1 – TXC Transmit Complete
               This flag is cleared by writing '1' to it or by writing new data to DATA.
               In Master mode, this flag is set when the data have been shifted out and there are no new data in DATA.
               In Slave mode, this flag is set when the _SS pin is pulled high. If address matching is enabled, this flag is
               only set if the transaction was initiated with an address match.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the flag.

               Bit 0 – DRE Data Register Empty
               This flag is cleared by writing new data to DATA.
               This flag is set when DATA is empty and ready for new data to transmit.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit has no effect.




           © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 997
                                                                SAM D5x/E5x Family Data Sheet
                                                      SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.8         Status

               Name:       STATUS
               Offset:     0x1A
               Reset:      0x0000
               Property:   –


         Bit        15           14           13           12            11           10           9            8
                                                                      LENERR
   Access                                                               R/W
    Reset                                                                0


         Bit         7            6            5            4            3            2            1            0
                                                                                   BUFOVF
   Access                                                                            R/W
    Reset                                                                             0


               Bit 11 – LENERR Transaction Length Error
               This bit is set in slave mode when the length counter is enabled (LENGTH.LENEN=1) and the transfer
               length while SS is low is not a multiple of LENGTH.LEN.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear it.
                Value        Description
                0            No Length Error has occurred.
                1            A Length Error has occurred.

               Bit 2 – BUFOVF Buffer Overflow
               Reading this bit before reading DATA will indicate the error status of the next character to be read.
               This bit is cleared by writing '1' to the bit or by disabling the receiver.
               This bit is set when a Buffer Overflow condition is detected. See also CTRLA.IBON for overflow handling.
               When set, the corresponding RxDATA will be zero.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear it.
                Value        Description
                0            No Buffer Overflow has occurred.
                1            A Buffer Overflow has occurred.




           © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 998
                                                               SAM D5x/E5x Family Data Sheet
                                                     SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.9         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x1C
               Reset:      0x00000000
               Property:   -


         Bit        31           30           29          28           27         26           25           24


   Access
    Reset


         Bit        23           22           21          20           19         18           17           16


   Access
    Reset


         Bit        15           14           13          12           11         10           9            8


   Access
    Reset


         Bit        7             6           5           4            3           2           1            0
                                                       LENGTH                   CTRLB       ENABLE        SWRST
   Access                                                 R                        R           R            R
    Reset                                                 0                        0           0            0


               Bit 4 – LENGTH LENGTH Synchronization Busy
               Writing to the LENGTH register requires synchronization. When writing to LENGTH,
               SYNCBUSY.LENGTH will be set until synchronization is complete. If the LENGTH register is written to
               while SYNCBUSY.LENGTH is asserted, an APB error is generated.
               Note: In slave mode, the clock is only running during data transfer, so SYNCBUSY.LENGTH will remain
               asserted until the next data transfer begins.
               Value       Description
               0           LENGTH synchronization is not busy.
               1           LENGTH synchronization is busy.

               Bit 2 – CTRLB CTRLB Synchronization Busy
               Writing to the CTRLB when the SERCOM is enabled requires synchronization. Ongoing synchronization
               is indicated by SYNCBUSY.CTRLB=1 until synchronization is complete. If CTRLB is written while
               SYNCBUSY.CTRLB=1, an APB error will be generated.
                Value       Description
                0           CTRLB synchronization is not busy.
                1           CTRLB synchronization is busy.

               Bit 1 – ENABLE SERCOM Enable Synchronization Busy
               Enabling and disabling the SERCOM (CTRLA.ENABLE) requires synchronization. Ongoing
               synchronization is indicated by SYNCBUSY.ENABLE=1 until synchronization is complete.




           © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 999
                                                    SAM D5x/E5x Family Data Sheet
                                         SERCOM SPI – SERCOM Serial Peripheral Interface

 Value        Description
 0            Enable synchronization is not busy.
 1            Enable synchronization is busy.

Bit 0 – SWRST Software Reset Synchronization Busy
Resetting the SERCOM (CTRLA.SWRST) requires synchronization. Ongoing synchronization is indicated
by SYNCBUSY.SWRST=1 until synchronization is complete.
 Value      Description
 0          SWRST synchronization is not busy.
 1          SWRST synchronization is busy.




© 2019 Microchip Technology Inc.                    Datasheet                 DS60001507E-page 1000
                                                               SAM D5x/E5x Family Data Sheet
                                                    SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.10 Length

           Name:        LENGTH
           Offset:      0x22
           Reset:       0x0000
           Property:    PAC Write-Protection, Write-Synchronized


     Bit        15            14            13            12              11       10            9            8
                                                                                                           LENEN
  Access                                                                                                     R/W
   Reset                                                                                                      0


     Bit         7             6            5             4                3       2             1            0
                                                               LEN[7:0]
  Access        R/W          R/W           R/W           R/W              R/W     R/W          R/W           R/W
   Reset         0             0            0             0                0       0             0            0


           Bit 8 – LENEN Data Length Enable
           In 32-bit Extension mode, this bit field enables the length counter.
            Value       Description
            0           Length counter disabled
            1           Length counter enabled

           Bits 7:0 – LEN[7:0] Data Length
           In 32-bit Extension mode, this bit field configures the data length after which the flags INTFLAG.RCX or
           INTFLAG.DRE are raised.
            Value       Description
            0x00        Reserved if LENEN=0x1
            0x01-0x Data Length
            FF




       © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1001
                                                           SAM D5x/E5x Family Data Sheet
                                                 SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.11 Address

           Name:       ADDR
           Offset:     0x24
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31           30           29         28                27     26           25           24


  Access
   Reset


     Bit        23           22           21         20                19     18           17           16
                                                      ADDRMASK[7:0]
  Access       R/W          R/W           R/W        R/W               R/W    R/W         R/W          R/W
   Reset        0             0            0          0                 0      0           0            0


     Bit        15           14           13         12                11     10           9            8


  Access
   Reset


     Bit        7             6            5          4                 3      2           1            0
                                                           ADDR[7:0]
  Access       R/W          R/W           R/W        R/W               R/W    R/W         R/W          R/W
   Reset        0             0            0          0                 0      0           0            0


           Bits 23:16 – ADDRMASK[7:0] Address Mask
           These bits hold the address mask when the transaction format with address is used (CTRLA.FORM,
           CTRLB.AMODE).

           Bits 7:0 – ADDR[7:0] Address
           These bits hold the address when the transaction format with address is used (CTRLA.FORM,
           CTRLB.AMODE).




       © 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1002
                                                                SAM D5x/E5x Family Data Sheet
                                                    SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.12 Data

           Name:        DATA
           Offset:      0x28
           Reset:       0x0000
           Property:    –


     Bit        31            30            29           28                 27       26            25           24
                                                              DATA[31:24]
  Access        R/W          R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0            0             0                  0       0             0             0


     Bit        23            22            21           20                 19       18            17           16
                                                              DATA[23:16]
  Access        R/W          R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0            0             0                  0       0             0             0


     Bit        15            14            13           12                 11       10            9             8
                                                               DATA[15:8]
  Access        R/W          R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0            0             0                  0       0             0             0


     Bit         7             6            5             4                  3       2             1             0
                                                               DATA[7:0]
  Access        R/W          R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0            0             0                  0       0             0             0


           Bits 31:0 – DATA[31:0] Data
           Reading these bits will return the contents of the receive data buffer. The register should be read only
           when the Receive Complete Interrupt Flag bit in the Interrupt Flag Status and Clear register
           (INTFLAG.RXC) is set.
           Writing these bits will write the transmit data buffer. This register should be written only when the Data
           Register Empty Interrupt Flag bit in the Interrupt Flag Status and Clear register (INTFLAG.DRE) is set.
           Reads and writes are 32-bit or CTLB.CHSIZE based on the CTRLC.DATA32B setting.




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 1003
                                                           SAM D5x/E5x Family Data Sheet
                                                  SERCOM SPI – SERCOM Serial Peripheral Interface

35.8.13 Debug Control

           Name:       DBGCTRL
           Offset:     0x30
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit        7             6           5            4            3            2            1            0
                                                                                                       DBGSTOP
  Access                                                                                                 R/W
   Reset                                                                                                   0


           Bit 0 – DBGSTOP Debug Stop Mode
           This bit controls the functionality when the CPU is halted by an external debugger.
            Value       Description
            0           The baud-rate generator continues normal operation when the CPU is halted by an external
                        debugger.
            1           The baud-rate generator is halted when the CPU is halted by an external debugger.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1004
