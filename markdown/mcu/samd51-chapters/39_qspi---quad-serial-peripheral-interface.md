# 37. QSPI - Quad Serial Peripheral Interface

*Source: `Atmel-SAMD51.pdf`, pages 1066-1108 — SAMD51 family datasheet*

                                                        SAM D5x/E5x Family Data Sheet
                                                               QSPI - Quad Serial Peripheral Interface


37.    QSPI - Quad Serial Peripheral Interface

37.1   Overview
       The Quad SPI Interface (QSPI) circuit is a synchronous serial data link that provides communication with
       external devices in Master mode.
       The QSPI can be used in “SPI mode” to interface serial peripherals, such as ADCs, DACs, LCD
       controllers and sensors, or in “Serial Memory Mode” to interface serial Flash memories.
       The QSPI allows the system to execute code directly from a serial Flash memory (XIP) without code
       shadowing to SRAM. The serial Flash memory mapping is seen in the system as other memories (ROM,
       SRAM, DRAM, embedded Flash memories, etc.,).
       With the support of the quad-SPI protocol, the QSPI allows the system to use high performance serial
       Flash memories which are small and inexpensive, in place of larger and more expensive parallel Flash
       memories.



37.2   Features
         • Master SPI Interface:
            – Programmable Clock Phase and Clock Polarity
            – Programmable transfer delays between consecutive transfers, between clock and data, between
               deactivation and activation of chip select (CS)
         • SPI Mode:
            – To use serial peripherals, such as ADCs, DACs, LCD controllers, CAN controllers, and sensors
            – 8-bit, 16-bit, or 32-bit programmable data length
         • Serial Memory Mode:
            – To use serial Flash memories operating in single-bit SPI, Dual SPI and Quad SPI
            – Supports “execute in place” (XIP). The system can execute code directly from a Serial Flash
               memory.
            – Flexible Instruction register, to be compatible with all Serial Flash memories
            – 32-bit Address mode (default is 24-bit address) to support Serial Flash memories larger than 128
               Mbit
            – Continuous Read mode
            – Scrambling/Unscrambling “On-the-Fly”
            – Double data rate support
         • Connection to DMA Channel Capabilities Optimizes Data Transfers
            – One channel for the receiver and one channel for the transmitter
         • Register Write Protection




       © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1066
                                                                             SAM D5x/E5x Family Data Sheet
                                                                                 QSPI - Quad Serial Peripheral Interface


37.3     Block Diagram
         Figure 37-1. QSPI Block Diagram


                                                          Peripheral Clock
                                                   MCLK



                                                                                                               SCK

                                                                                     QSPI                      MOSI/DATA0

                                            Peripheral                APB
                                                                                                               MISO/DATA1
                                             Bridge
            CPU
                                                                                                               DATA2
                           AHB
                          MATRIX                                                                               DATA3

            DMA                                                                                                CS


                                                                                 Interrupt Control




                                                                                  QSPI Interrupt




37.4     Signal Description
         Table 37-1. Quad-SPI Signals

          Signal                       Description                                              Type
          SCK                          Serial Clock                                             Output
          CS                           Chip Select                                              Output
          MOSI(DATA0)                  Data Output (Data Input Output 0)                        Output (Input/Output)
          MISO(DATA1)                  Data Input (Data Input Output 1)                         Input (Input/Output)
          DATA2                        Data Input Output 2                                      Input/Output
          DATA3                        Data Input Output 3                                      Input/Output

         Note: MOSI and MISO are used for single-bit SPI operation
         Note: DATA0-DATA1 are used for Dual SPI operation
         Note: DATA0-DATA3 are used for Quad SPI operation
         Refer to the pinout table for details on the pin mapping for this peripheral. One signal can be mapped to
         one of several pins.



37.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

37.5.1   I/O Lines
         Using the QSPI I/O lines requires the I/O pins to be configured.




         © 2019 Microchip Technology Inc.                                    Datasheet                               DS60001507E-page 1067
                                                         SAM D5x/E5x Family Data Sheet
                                                               QSPI - Quad Serial Peripheral Interface

         Related Links
         32. PORT - I/O Pin Controller

37.5.2   Power Management
         The QSPI will continue to operate in any Sleep mode where the selected source clock is running. The
         QSPI interrupts can be used to wake up the device from sleep modes. Refer to the Power Manager
         chapter for details on the different sleep modes.

37.5.3   Clocks
         The QSPI bus clock (CLK_QSPI_APB) can be enabled and disabled in the Main Clock module, and the
         default state of CLK_QSPI_APB can be found in the Peripheral Clock Masking section in the MCLK
         chapter.
         An AHB clock (CLK_QSPI_AHB) is required to clock the QSPI. This clock can be enabled and disabled in
         the Main Clock module, and the default state of CLK_QSPI_AHB can be found in the Peripheral Clock
         Masking section in the MCLK chapter.
         A FAST clock (CLK_QSPI2X_AHB) is required to clock the QSPI. This clock can be enabled and disabled
         in the Main Clock module, and the default state of CLK_QSPI2X_AHB can be found in the Peripheral
         Clock Masking section in the MCLK chapter. This clock is derived from the High-Speed Clock Domain
         (HS Clock Domain, frequency fHS).
         Figure 37-2. QSPI Clock Organization




                        Important: The CLK_QSPI2x_AHB must be 2 times faster to CLK_QSPI_AHB when the QSPI
                        is operated in DDR mode. In SDR, the CLK_QSPI2x_AHB is not used.



         CLK_QSPI_APB, CLK_QSPI_AHB, and CLK_QSPI2X_AHB, respectively, are all synchronous, but can
         be divided by a prescaler and may run even when the module clock is turned off.
         Related Links
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking




         © 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 1068
                                                             SAM D5x/E5x Family Data Sheet
                                                                    QSPI - Quad Serial Peripheral Interface

37.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). Using the QSPI DMA requests
         requires the DMA Controller to be configured first.
         Note: DMAC write access must be 32-bit aligned. If a single byte is to be written in a 32-bit word, the
         rest of the word must be filled with 'ones'.
         Related Links
         22. DMAC – Direct Memory Access Controller

37.5.5   Interrupts
         The interrupt request lines are connected to the interrupt controller. Using the QSPI interrupts requires
         the interrupt controller to be configured first. Refer to the Nested Vector Interrupt Controller section for
         details.
         Related Links
         10.2 Nested Vector Interrupt Controller

37.5.6   Events
         Not applicable.

37.5.7   Debug Operation
         When the CPU is halted in debug mode the QSPI continues normal operation. If the QSPI is configured in
         a way that requires it to be periodically serviced by the CPU through interrupts or similar, improper
         operation or data loss may result during debugging.

37.5.8   Register Access Protection
         All registers with write-access are optionally write-protected by the peripheral access controller (PAC),
         except the following registers:
           •   Control A (CTRLA) register
           •   Transmit Data (TXDATA) register
           •   Interrupt Flag Status and Clear (INTFLAG) register
           •   Interrupt Flag Status and Clear (INTFLAG) register
         PAC write-protection is denoted by the `'PAC Write-Protection' property in the register description.
         Write-protection does not apply to accesses through an external debugger.



37.6     Functional Description

37.6.1   Principle of Operation
         The QSPI is a high-speed synchronous data transfer interface. It allows high-speed communication
         between the device and peripheral or serial memory devices.
         The QSPI operates as a master. It initiates and controls all data transactions.
         When transmitting, the TXDATA register can be loaded with the next character to be transmitted during
         the current transmission.
         When receiving, the data is transferred to the RXDATA register, and the receiver is ready for a new
         character.




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1069
                                                            SAM D5x/E5x Family Data Sheet
                                                                   QSPI - Quad Serial Peripheral Interface

37.6.2    Basic Operation

37.6.2.1 Initialization
          After Power-On Reset, this peripheral is enabled .
37.6.2.2 Enabling, Disabling, and Resetting
          The peripheral is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE).
          The peripheral is disabled by writing a '0' to CTRLA.ENABLE.
          The peripheral is reset by writing a '1' to the Software Reset bit (CTRLA.SWRST).

37.6.3    Transfer Data Rate
          By default, the QSPI module is enabled in single data rate mode. In this operating mode, the
          CLK_QSPI2X_AHB clock is not used and can be disabled.
          The dual data rate operating mode is enabled by writing a '1' to the Double Data Rate Enable bit in the
          Instruction Frame register (INSTRFRAME.DDREN). This operating mode requires the
          CLK_QSPI2X_AHB clock and must be enabled before writing the DDREN bit.

37.6.4    Serial Clock Baudrate
          The QSPI Baud rate clock is generated by dividing the module clock (CLK_QSPI_AHB) by a value
          between 1 and 255.
          This allows a maximum operating baud rate at up to Master Clock and a minimum operating baud rate of
          CLK_QSPI_AHB divided by 256.

37.6.5    Serial Clock Phase and Polarity
          Four combinations of polarity and phase are available for data transfers. Writing the Clock Polarity bit in
          the QSPI Baud register (BAUD.CPOL) selects the polarity. The Clock Phase bit in the BAUD register
          programs the clock phase (BAUD.CPHA). These two parameters determine the edges of the clock signal
          on which data is driven and sampled. Each of the two parameters has two possible states, resulting in
          four possible combinations
          Note: The polarity/phase combinations are incompatible. Thus, the interfaced slave must use the same
          parameter values to communicate.
          Table 37-2. SPI Transfer Mode

          Clock Mode           BAUD.CPOL      BAUD.CPHA          Shift SCK        Capture SCK       SCK Inactive
                                                                 Edge             Edge              Level
          0                    0              0                  Falling          Rising            Low
          1                    0              1                  Rising           Falling           Low
          2                    1              0                  Rising           Falling           High
          3                    1              1                  Falling          Rising            High




         © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1070
                                                                           SAM D5x/E5x Family Data Sheet
                                                                                      QSPI - Quad Serial Peripheral Interface

         Figure 37-3. QSPI Transfer Modes (BAUD.CPHA = 0, 8-bit transfer)

           SCK Cycle (for reference)        1      2                3            4                5         6           7          8

           SCK
           (CPOL = 0)




           SCK
           (CPOL = 1)




           MOSI                            MSB      6               5            4            3             2               1     LSB
           (from master)




           MISO
           (from slave)
                                           MSB      6               5            4            3             2               1     LSB       *



           CS
           (to slave)

                                                           * Not defined, but normally MSB of previous character received


         Figure 37-4. QSPI Transfer Modes (BAUD.CPHA = 1, 8-bit transfer)
           SCK Cycle (for reference)        1      2                3           4              5            6           7          8

           SCK
           (CPOL = 0)




           MOSI                            MSB         6            5            4            3             2               1     LSB
           (from master)




           MISO
           (from slave)                *   MSB         6            5            4            3             2               1     LSB




           CS
           (to slave)


                                                 * Not defined, but normally LSB of previous character received



37.6.6   Transfer Delays
         The QSPI supports several consecutive transfers while the chip select is active. Three delays can be
         programmed to modify the transfer waveforms:
           • The delay between the inactivation and the activation of CS is programmed by writing the Minimum
             Inactive CS Delay bit field in the Control B register (CTRLB.DLYCS), allowing to tune the minimum
             time of CS at high level.
           • The delay between consecutive transfers is programmed by writing the Delay Between Consecutive
             Transfers bit field in the Control B register (CTRLB.DLYBCT), allowing to insert a delay between two




         © 2019 Microchip Technology Inc.                                    Datasheet                                          DS60001507E-page 1071
                                                            SAM D5x/E5x Family Data Sheet
                                                                    QSPI - Quad Serial Peripheral Interface

             consecutive transfers. In Serial Memory mode, this delay is not programmable and DLYBCT settings
             are ignored.
           • The delay before SCK is programmed by writing the Delay Before SCK bit field in the BAUD register
             (BAUD.DLYBS), allowing to delay the start of SPCK after the chip select has been asserted.
         These delays allow the QSPI to be adapted to the interfaced peripherals and their speed and bus release
         time.
         Figure 37-5. Programmable Delay


                              CS




                               SCK          DLYCS   DLYBS             DLYBCT                    DLYBCT



37.6.7   QSPI SPI Mode
         In this mode, the QSPI acts as a regular SPI Master.
         To activate this mode, the MODE bit in Control B register must be cleared (CTRLB.MODE=0).
37.6.7.1 SPI Mode Operations
         The QSPI in standard SPI mode operates on the clock generated by the internal programmable baud rate
         generator. It fully controls the data transfers to and from the slave connected to the SPI bus. The QSPI
         drives the chip select line to the slave (CS) and the serial clock signal (SCK).
         The QSPI features a single internal shift register and two holding registers: the Transmit Data Register
         (TXDATA) and the Receive Data Register (RXDATA). The holding registers maintain the data flow at a
         constant rate.
         After enabling the QSPI, a data transfer begins when the processor writes to the TXDATA. The written
         data is immediately transferred into the internal shift register and transfer on the SPI bus starts. While the
         data in the internal shift register is shifted on the MOSI line, the MISO line is sampled and shifted into the
         internal shift register. Receiving data cannot occur without transmitting data.
         If new data is written in TXDATA during the transfer, it stays in TXDATA until the current transfer is
         completed. Then, the received data is transferred from the internal shift register to the RXDATA, the data
         in TXDATA is loaded into the internal shift register, and a new transfer starts.
         The transfer of data written in TXDATA in the internal shift register is indicated by the Transmit Data
         Register Empty (DRE) bit in the Interrupt Flag Status and Clear register (INTFLAG.DRE). When new data
         is written in TXDATA, this bit is cleared. The DRE bit is used to trigger the Transmit DMA channel.
         The end of transfer is indicated by the Transmission Complete flag (INTFLAG.TXC). If the transfer delay
         for the last transfer was configured to be greater than 0 (CTRLB.DLYBCT), TXC is set after the
         completion of the delay. The module clock (CLK_QSPI_AHB) can be switched off at this time.
         Ongoing transfer of received data from the internal shift register into RXDATA is indicated by the Receive
         Data Register Full flag (INTFLAG.RXC). When the received data is read, the RXC bit is cleared.
         If the RXDATA has not been read before new data is received, the Overrun Error flag in INTFLAG register
         (INTFLAG.ERROR) is set. As long as this flag is set, data is loaded in RXDATA.
         The SPI Mode Block Diagram shows a flow chart describing how transfers are handled.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1072
                                                                SAM D5x/E5x Family Data Sheet
                                                                         QSPI - Quad Serial Peripheral Interface

37.6.7.2 SPI Mode Block Diagram
        Figure 37-6. SPI Mode Block Diagram
                                            BAUD
                                                     BAUD


                       Peripheral Clock      Baud Rate Generator                                          SCK



                                                                   Serial
                                                                   Clock



                                          BAUD                       RXDATA                      RXC
                                                   CPHA                            DATA         ERROR
                                                   CPOL

                                            LSB               Shift Register              MSB
                       MISO                                                                               MOSI

                                          CTRLB
                                                   DATALEN           TXDATA
                                                                                   DATA         DRE


                                                          Chip Select Controller                           CS

                                          CTRLB
                                                  CSMODE




       © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 1073
                                                   SAM D5x/E5x Family Data Sheet
                                                              QSPI - Quad Serial Peripheral Interface

37.6.7.3 SPI Mode Flow Diagram
        Figure 37-7. SPI Mode Flow Diagram
                                                 QSI Enable




                                                                   1
                                                    DRE ?


                                                    0

                                                     CS = 0



                                                 Delay DLYBS




                                             Serializer = TXDATA
                                                 DRE = 1




                                                Data Transfer



                                             RXDATA = Serializer
                                                RXC = 1



                                               Delay DLYBCT




                                                                   0
                                                    DRE ?



                                                    1

                                                     CS = 1



                                                Delay DLYCS




       © 2019 Microchip Technology Inc.              Datasheet                      DS60001507E-page 1074
                                                               SAM D5x/E5x Family Data Sheet
                                                                           QSPI - Quad Serial Peripheral Interface

        Figure 37-8. Interrupt Flags Behaviour

                                    1      2           3       4              5       6       7               8

                  SCK


                   CS


           MOSI
                                    MSB            6       5           4          3       2           1       LSB
           (from master)



               DRE
                                                                                                                         RXDATA Read
               Write in TXDATA


                RXC


            MISO                   MSB         6       5           4          3       2           1          LSB
            (from slave)



                 TXC

                                                                                                  Shift register empty



37.6.7.4 Peripheral Deselection with DMA
        When the Direct Memory Access Controller is used, the Chip Select line will remain low during the whole
        transfer since the Transmit Data Register Empty flag in the Interrupt Flag Status and Clear register
        (INTFLAG.DRE) is managed by the DMA itself. The reloading of the TXDATA by the DMA is done as
        soon as INTFLAG.DRE flag is set. In this case, setting the Chip Select Mode bit field in the Control B
        register (CTRLB.CSMODE) to 0x1 is not mandatory.
        However, it may happen that when other DMA channels connected to other peripherals are in use as
        well, the QSPI DMA could be delayed by another DMA transfer with a higher priority on the bus. Having
        DMA buffers in slower memories like flash memory or SDRAM (compared to fast internal SRAM), may
        lengthen the reload time of the TXDATA by the DMA as well. This means that TXDATA might not be
        reloaded in time to keep the Chip Select line low. In this case the Chip Select line may toggle between
        data transfer and according to some SPI Slave devices, and the communication might get lost. Writing
        CTRLB.CSMODE=0x1 can prevent this loss.
        When CTRLB.CSMODE=0x0, the CS does not rise in all cases between two transfers on the same
        peripheral. During a transfer on a Chip Select, the INTFLAG.DRE flag is raised as soon as the content of
        the TXDATA is transferred into the internal shifter. When this flag is detected the TXDATA can be
        reloaded. if this reload occurs before the end of the current transfer and if the next transfer is performed
        on the same Chip Select as the current transfer, the Chip Select is not de-asserted between the two
        transfers. This may lead to difficulties for interfacing with some serial peripherals requiring the Chip Select
        to be de-asserted after each transfer. To facilitate interfacing with such devices, it is recommended to
        write CTRLB.CSMODE to 0x2.
37.6.7.5 Peripheral Deselection without DMA
        During multiple data transfers on a Chip Select without the DMA, the TXDATA is loaded by the processor,
        and the Transmit Data Register Empty flag in the Interrupt Flag Status and Clear register (INTFLAG.DRE)
        rises as soon as the content of the RXDATA is transferred into the internal shift register. When this flag is
        detected high, the TXDATA can be reloaded. If this reload-by-processor occurs before the end of the
        current transfer and if the next transfer is performed on the same Chip Select as the current transfer, the
        Chip Select is not de-asserted between the two transfers.




        © 2019 Microchip Technology Inc.                       Datasheet                                   DS60001507E-page 1075
                                                           SAM D5x/E5x Family Data Sheet
                                                                  QSPI - Quad Serial Peripheral Interface

         Depending on the application software handling the flags or servicing other interrupts or other tasks, the
         processor may not reload the TXDATA in time to keep the Chip Select active (low). A null Delay Between
         Consecutive Transfer bit field value in the CTRLB register (CTRLB.DLYBCT) will give even less time for
         the processor to reload the TXDATA. With some SPI slave peripherals, requiring the Chip Select line to
         remain active (low) during a full set of transfers might lead to communication errors.
         To facilitate interfacing with such devices, the Chip Select Mode bit field in the CTRLB register
         (CTRLB.CSMODE) can be written to 0x1. This allows the Chip Select lines to remain in their current state
         (low = active) until the end of transfer is indicated by the Last Transfer bit in the CTRLA register
         (CTRLA.LASTXFER). Even if the TXDATA is not reloaded the Chip Select will remain active. To have the
         Chip Select line rise at the end of the last data transfer, the LASTXFER bit in the CTRLA must be set
         before writing the last data to transmit into the TXDATA.

37.6.8   QSPI Serial Memory Mode
         In this mode the QSPI acts as a serial flash memory controller. The QSPI can be used to read data from
         the serial flash memory allowing the CPU to execute code from it (XIP execute in place). The QSPI can
         also be used to control the serial flash memory (Program, Erase, Lock, etc.) by sending specific
         commands. In this mode, the QSPI is compatible with single-bit SPI, Dual SPI and Quad SPI protocols.
         To activate this mode, the MODE bit in Control B register must be set to one (CTRLB.MODE = 1).
         In serial memory mode, data cannot be transferred by the TXDATA and the RXDATA, but by writing or
         reading the QSPI memory space (0x0400 0000 – 0x0500 0000).
37.6.8.1 Instruction Frame
         In order to control serial flash memories, the QSPI is able to sent instructions by the SPI bus (ex: READ,
         PROGRAM, ERASE, LOCK, etc.). Because instruction set implemented in serial flash memories is
         memory vendor dependant, the QSPI includes a complete instruction registers, which makes it very
         flexible and compatible with all serial flash memories.
         An instruction frame includes:
           • An instruction code (size: 8 bits). The instruction can be optional in some cases.
           • An address (size: 24 bits or 32 bits). The address is optional but is required by instructions such as
             READ, PROGRAM, ERASE, LOCK. By default the address is 24 bits long, but it can be 32 bits long
             to support serial flash memories larger than 128 Mbit (16 Mbyte).
           • An option code (size: 1/2/4/8 bits). The option code is optional but is useful for activate the “XIP
             mode” or the “Continuous Read Mode” for READ instructions, in some serial flash memory devices.
             These modes allow to improve the data read latency.
           • Dummy cycles. Dummy cycles are optional but required by some READ instructions.
           • Data bytes are optional. Data bytes are present for data transfer instructions such as READ or
             PROGRAM.
         The instruction code, the address/option and the data can be sent with Single-bit SPI, Dual SPI or Quad
         SPI protocols.




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1076
                                                                   SAM D5x/E5x Family Data Sheet
                                                                            QSPI - Quad Serial Peripheral Interface

        Figure 37-9. Instruction Frame
                CS

               SCK

              DATA0                                         A20 A16 A12 A8 A4 A0 O4 O0                D4 D0          D4 D0


              DATA1                                         A21 A17 A13 A9 A5 A1 O5 O1                D5 D1          D5 D1


              DATA2                                         A22 A18 A14 A10 A6 A2 O6 O2               D6 D2          D6 D2


              DATA3                                         A23 A19 A15 A11 A7 A3 O7 O3               D7 D3          D7 D3
                                   Instruction EBh                Address       Option Dummy cycles           Data


37.6.8.2 Instruction Frame Sending
        To send an instruction frame, the user must first configure the address to send by writing the field ADDR
        in the Instruction Address Register (INSTRADDR.ADDR). This step is required if the instruction frame
        includes an address and no data. When data is present, the address of the instruction is defined by the
        address of the data accesses in the QSPI memory space, and not by the INSTRADDR register.
        If the instruction frame includes the instruction code and/or the option code, the user must configure the
        instruction code and/or the option code to send by writing the fields INST and OPTCODE bit fields in the
        Instruction Control Register (INSTRCTRL.OPTCODE, INSTRCTRL.INSTR).
        Then, the user must write the Instruction Frame Register (INSTRFRAME) to configure the instruction
        frame depending on which instruction must be sent. If the instruction frame does not include data, writing
        in this register triggers the send of the instruction frame in the QSPI. If the instruction frame includes data,
        the send of the instruction frame is triggered by the first data access in the QSPI memory space.
        The instruction frame is configured by the following bits and fields of INSTRFRAME:
         • WIDTH field is used to configure which data lanes are used to send the instruction code, the
            address, the option code and to transfer the data. It is possible to use two unidirectional data lanes
            (MISO-MOSI Single-bit SPI), two bidirectional data lanes (DATA0 - DATA1 Dual SPI) or four
            bidirectional data lanes (DATA0 - DATA3).
        Table 37-3. WIDTH Encoding

         INSTRFRAME                        Instruction                  Address/Option                Data
         0                                 Single-bit SPI               Single-bit SPI                Single-bit SPI
         1                                 Single-bit SPI               Single-bit SPI                Dual SPI
         2                                 Single-bit SPI               Single-bit SPI                Quad SPI
         3                                 Single-bit SPI               Dual SPI                      Dual SPI
         4                                 Single-bit SPI               Quad SPI                      Quad SPI
         5                                 Dual SPI                     Dual SPI                      Dual SPI
         6                                 Quad SPI                     Quad SPI                      Quad SPI
         7                                 Reserved
          •   INSTREN bit enables sending an instruction code.
          •   ADDREN bit enables sending of an address after the instruction code.
          •   OPTCODEEN bit enables sending of an option code after the address.
          •   DATAEN bit enables the transfer of data (READ or PROGRAM instruction).




        © 2019 Microchip Technology Inc.                             Datasheet                                DS60001507E-page 1077
                                                   SAM D5x/E5x Family Data Sheet
                                                          QSPI - Quad Serial Peripheral Interface

  • OPTCODELEN field configures the option code length (0 -> 1-bit / 1 -> 2-bit / 2 -> 4-bit / 3 -> 8-bit).
    The value written in OPTCODELEN must be consistent with value written in the field WIDTH. For
    example: OPTCODELEN = 0 (1-bit option code) is not coherent with WIDTH = 6 (option code sent
    with QuadSPI protocol, thus the minimum length of the option code is 4-bit).
  • ADDRLEN bit configures the address length (0 -> 24 bits / 1-> 32 bits)
  • TFRTYPE field defines which type of data transfer must be performed.
  • DUMMYLEN field configures the number of dummy cycles when reading data from the serial flash
    memory. Between the address/option and the data, with some instructions, dummy cycles are
    inserted by the serial flash memory.
If data transfer is enabled, the user can access the serial memory by reading or writing the QSPI memory
space following these rules:
  • Reading from the serial memory, but not memory data (for example reading the JEDEC-ID or the
    STATUS), requires TFRTYPE to be written to 0x0.
  • Reading from the serial memory, and particularly memory data, requires TFRTYPE to be written to
    '1'.
  • Writing to the serial memory, but not memory data (for example writing the configuration or STATUS),
    requires TFRTYPE to be written to 0x2.
  • Writing to the serial memory, and particularly memory data, requires TFRTYPE to be written to 0x3.
If TFRTYP has a value other than 0x1 and CTRLB.SMEMREG=0, the address sent in the instruction
frame is the address of the first system bus accesses. The addresses of the subsequent access actions
are not used by the QSPI. At each system bus access, an SPI transfer is performed with the same size.
For example, a half-word system bus access leads to a 16-bit SPI transfer, and a byte system bus access
leads to an 8-bit SPI transfer.
If CTRLB.SMEMREG=1, accesses are made via the QSPI registers and the address sent in the
instruction frame is the address defined in the INSTRADDR register. Each time the INSTRFRAME or
TXDATA registers are written, an SPI transfer is performed with a byte size. Another byte is read each
time RXDATA register is read or written each time TXDATA register is written. The SPI transfer ends by
writing the LASTXFER bit in Control A register (CTRLA.LASTXFER).
If TFRTYP=0x1, the address of the first instruction frame is the one of the first read access in the QSPI
memory space. Each time the read accesses become non-sequential (addresses are not consecutive), a
new instruction frame is sent with the last system bus access address. In this way, the system can read
data at a random location in the serial memory. The size of the SPI transfers may differ from the size of
the system bus read accesses.
When data transfer is not enabled, the end of the instruction frame is indicated when the INSTREND
interrupt flag in the INTFLAG register is set. When data transfer is enabled, the user must indicate when
data transfer is completed in the QSPI memory space by setting the bit LASTXFR in the CTRLA. The end
of the instruction frame is indicated when the INSTREND interrupt flag in the INTFLAG register is set.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1078
                                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                  QSPI - Quad Serial Peripheral Interface

Figure 37-10. Instruction Transmission Flow Diagram
                                                    START




                                              Instruction frame
                                   No
                                                with address
                                                 but no data
                                                       ?
                                                          Yes

                                              Write the address
                                              in INSTRADDR




                                   No          Instruction frame
                                         with instruction code and/or
                                                  option code
                                                        ?
                                                          Yes

                                          Write the instruction code
                                          and/or the option code
                                               in INSTRCTRL




                                        Configure and send instruction
                                        frame by writing INSTRFRAME




                                   No         Instruction frame
                                                  with data
                                                       ?

                                                          Yes

                                             Read INSTRFRAME
                                        to synchronize APB and AHB
                                                  accesses




                                              Instruction frame            No
                                                with address
                                                       ?

                                                          Yes



                                               Read memory                 No
                                                  transfer
                                               (TFRTYP = 1)
                                                     ?
                                                          Yes


                                                                                  Read/Write DATA in the QSPI
                                        Read DATA in the QSPI AHB                      AHB memory space               Read/Write DATA in the QSPI
                                                memory space.                                                            AHB memory space.
                                                                                     (SMEMREG = 0) or APB
                                        If accesses are not sequential                                                Address of accesses are not
                                                                                register space (SMEMREG = 1).
                                            a new instruction is sent                                                     used by the QSPI.
                                                automatically.                   The address of the first access
                                                                                is sent after the instruction code.




                                         Write CTRLA.LASTXFR to 1
                                          when all data have been
                                                 transferred.




                                        Wait for INTFLAG.INSTREND
                                        to rise by polling or interrupt.



                                   Depending on CSMODE configuration
                                        wait for INTFLAG.CSRISE
                                       to rise by polling or interrupt.




                                                    END




© 2019 Microchip Technology Inc.                                                       Datasheet                                                    DS60001507E-page 1079
                                                                                    SAM D5x/E5x Family Data Sheet
                                                                                         QSPI - Quad Serial Peripheral Interface

37.6.8.3 Read Memory Transfer
        The user can access the data of the serial memory by sending an instruction with DATAEN=1 and
        TFRTYP=0x1 in the Instruction Frame register (INSTRFRAME).
        In this mode the QSPI is able to read data at random address into the serial flash memory, allowing the
        CPU to execute code directly from it (XIP execute-in-place).
        In order to fetch data, the user must first configure the instruction frame by writing the INSTRFRAME.
        Then data can be read at any address in the QSPI address space mapping. The address of the system
        bus read accesses match the address of the data inside the serial Flash memory.
        When Fetch Mode is enabled, several instruction frames can be sent before writing the bit LASTXFR in
        the CTRLA. Each time the system bus read accesses become non-sequential (addresses are not
        consecutive), a new instruction frame is sent with the corresponding address.
37.6.8.4 Continuous Read Mode
        The QSPI is compatible with Continuous Read Mode (CRM) which is implemented in some Serial Flash
        memories.
        The CRM allows to reduce the instruction overhead by excluding the instruction code from the instruction
        frame. When CRM is activated in a Serial Flash memory (by a specific option code), the instruction code
        is stored in the memory. For the next instruction frames, the instruction code is not required, as the
        memory uses the stored one.
        In the QSPI, CRM is used when reading data from the memory (INSTFRAME.TFRTYPE=0x1). The
        addresses of the system bus read accesses are often non-sequential, this leads to many instruction
        frames with always the same instruction code. By disabling the sending of the instruction code, the CRM
        reduces the access time of the data.
        To be functional, this mode must be enabled in both the QSPI and the Serial Flash memory. The CRM is
        enabled in the QSPI by setting the CRM bit in the INSTRFRAME register (INSTFRAME.CRMODE=1,
        INSTFRAME.TFRTYPE must be 0x1). The CRM is enabled in the Serial Flash memory by sending a
        specific option code.


            CAUTION
                       If CRM is not supported by the Serial Flash memory or disabled, the CRMODE bit must not be
                       set. Otherwise, data read out the Serial Flash memory is not valid.


        Figure 37-11. Continuous Read Mode
           CS

          SCK

        DATA0                              A20 A16 A12 A8 A4 A0 O4 O0                 D4 D0          D4 D0   A20 A16 A12 A8 A4 A0 O4 O0             D4 D0


        DATA1                              A21 A17 A13 A9 A5 A1 O5 O1                 D5 D1          D5 D1   A21 A17 A13 A9 A5 A1 O5 O1             D5 D1


        DATA2                              A22 A18 A14 A10 A6 A2 O6 O2                D6 D2          D6 D2   A22 A18 A14 A10 A6 A2 O6 O2            D6 D2


        DATA3                              A23 A19 A15 A11 A7 A3 O7 O3                D7 D3          D7 D3   A23 A19 A15 A11 A7 A3 O7 O3            D7 D3
                         Instruction             Address         Option                       Data                  Address            Option           Data
                                                             to activate the                                 Instruction code is not
                                                        Continuous Read Mode                                        required
                                                       in the serial flash memory



37.6.8.5 Instruction Frame Transmission Examples
        All waveforms in the following examples describe SPI transfers in SPI Clock mode 0 (BAUD.CPOL=0 and
        BAUD.CPHA=0). All system bus accesses described below refer to the system bus address phase.
        System bus wait cycles and system bus data phases are not shown.




        © 2019 Microchip Technology Inc.                                            Datasheet                                          DS60001507E-page 1080
                                                           SAM D5x/E5x Family Data Sheet
                                                                 QSPI - Quad Serial Peripheral Interface

          Example 37-1. Example 1
          Instruction in Single-bit SPI, without address, without option, without data.
          Command: CHIP ERASE (C7h).
            • Write 0x0000_00C7 to INSTRCTRL register.
            • Write 0x0000_0010 to INSTRFRAME register.
            • Wait for INTFLAG.INSTREND to rise.
          Figure 37-12. Instruction Transmission Waveform 1
                           Write INSTRFRAME

                                            CS

                                           SCK

                                   MOSI / DATA0
                                                            Instruction C7h
                           INTFLAG.INSTREND



          Example 37-2. Example 2
          Instruction in Quad SPI, without address, without option, without data.
          Command: POWER DOWN (B9h)
            • Write 0x0000_00B9 to INSTRCTRL register.
            • Write 0x0000_0016 to INSTRFRAME register.
            • Wait for INTFLAG.INSTREND to rise.
          Figure 37-13. Instruction Transmission Waveform 2
                                        Write INSTRFRAME

                                                    CS

                                                   SCK

                                                  DATA0

                                                  DATA1

                                                  DATA2

                                                  DATA3
                                                               Instruction B9h
                                       INTFLAG.INSTREND



          Example 37-3. Example 3
          Instruction in Single-bit SPI, with address in Single-bit SPI, without option, without data.
          Command: BLOCK ERASE (20h)
            •   Write the address (of the block to erase) to QSPI_AR.
            •   Write 0x0000_0020 to INSTRCTRL register.
            •   Write 0x0000_0030 toINSTRFRAME register.
            •   Wait for INTFLAG.INSTREND to rise.




© 2019 Microchip Technology Inc.                           Datasheet                       DS60001507E-page 1081
                                                           SAM D5x/E5x Family Data Sheet
                                                                    QSPI - Quad Serial Peripheral Interface

          Figure 37-14. Instruction Transmission Waveform 3
                 Write INSTRADDR

                Write INSTRFRAME

                              CS

                            SCK

                   MOSI / DATA0                                       A23 A22 A21 A20            A3 A2 A1 A0
                                              Instruction 20h                          Address
            INTFLAG.INSTREND



          Example 37-4. Example 4
          Instruction in Single-bit SPI, without address, without option, with data write in Single-bit
          SPI.
          Command: SET BURST (77h)
            • Write 0x0000_0077 to INSTRCTRL register.
            • Write 0x0000_2090 to INSTRFRAME register.
            • Read INSTRFRAME register (dummy read) to synchronize system bus accesses.
            • Write data to the system bus memory space (0x0400_0000–0x0500_0000). The
              address of the system bus write accesses is not used.
            • Write the LASTXFR bit in CTRLA register to '1'.
            • Wait for INTFLAG.INSTREND to rise.
          Figure 37-15. Instruction Transmission Waveform 4
            Write INSTRFRAME

                            CS

                           SCK

                   MOSI / DATA0                             D7 D6 D5 D4 D3 D2 D1 D0          D7 D6 D5 D4 D3 D2 D1 D0
                                        Instruction 77h                               Data
            INTFLAG.INSTREND

                      Write AHB

          Set CTRLA.LASTXFER




          Example 37-5. Example 5
          Instruction in Single-bit SPI, with address in Dual SPI, without option, with data write in
          Dual SPI.
          Command: BYTE/PAGE PROGRAM (02h)
            •    Write 0x0000_0002 to INSTRCTRL register.
            •    Write 0x0000_30B3 to INSTRFRAME register.
            •    Read INSTRFRAME register (dummy read) to synchronize system bus accesses.
            •    Write data to the QSPI system bus memory space (0x040 00000–0x0500_0000).
                 The address of the first system bus write access is sent in the instruction frame.
              The address of the next system bus write accesses is not used.
            • Write LASTXFR bit in CTRLA register to '1'.




© 2019 Microchip Technology Inc.                                Datasheet                                 DS60001507E-page 1082
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                QSPI - Quad Serial Peripheral Interface

            • Wait for INTFLAG.INSTREND to rise.
          Figure 37-16. Instruction Transmission Waveform 5
           Write INSTRFRAME

                             CS

                            SCK

                          DATA0                           A22 A20 A18 A16 A14 A12 A10 A8 A6 A4 A2 A0 D6 D4 D2 D0          D6 D4 D2 D0


                          DATA1                           A23 A21 A19 A17 A15 A13 A11 A9 A7 A5 A3 A1 D7 D5 D3 D1          D7 D5 D3 D1
                                     Instruction 02h                            Address                            Data
           INTFLAG.INSTREND

                       Write AHB

          Set CTRLA.LASTXFER




          Example 37-6. Example 6
          Instruction in Single-bit SPI, with address in Single-bit SPI, without option, with data read
          in Quad SPI, with eight dummy cycles.
          Command: QUAD_OUTPUT READ ARRAY (6Bh)
            •     Write 0x0000_006B to INSTRCTRL register.
            •     Write 0x0008_10B2 ti INSTRFRAME register.
            •     Read QSPI_IR (dummy read) to synchronize system bus accesses.
            •     Read data from the QSPI system bus memory space (0x040 00000–0x0500_0000).
                  The address of the first system bus read access is sent in the instruction frame.
              The address of the next system bus read accesses is not used.
            • Write the LASTXFR bit in CTRLA register to '1'.
            • Wait for INTFLAG.INSTREND to rise.
          Figure 37-17. Instruction Transmission Waveform 6
                Write INSTRFRAME


                             CS

                            SCK

                          DATA0                         A23 A22 A21 A20         A3 A2 A1 A0                         D4 D0          D4 D0


                          DATA1                                                                                     D5 D1          D5 D1


                          DATA2                                                                                     D6 D2          D6 D2


                          DATA3                                                                                     D7 D3          D7 D3
                                      Instruction 6Bh                 Address                 Dummy cycles                  Data
                INTFLAG.INSTREND

                        Read AHB

            Set CTRLA.LASTXFER




          Example 37-7. Example 7
          Instruction in Single-bit SPI, with address and option in Quad SPI, with data read from
          Quad SPI, with four dummy cycles, with fetch and continuous read.
          Command: FAST READ QUAD I/O (EBh) - 8-BIT OPTION (0x30h)
            • Write 0x0030_00EB to INSTRCTRL register.
            • Write 0x0004_33F4 to INSTRFRAME register.
            • Read INSTRFRAME register (dummy read) to synchronize system bus accesses.




© 2019 Microchip Technology Inc.                                    Datasheet                                             DS60001507E-page 1083
                                                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                             QSPI - Quad Serial Peripheral Interface

                     • Read data from the QSPI system bus memory space (0x040 00000–0x0500_0000).
                       Fetch is enabled, the address of the system bus read accesses is always used.
                     • Write LASTXFR bit in CTRLA register to '1'.
                     • Wait for INTFLAG.INSTREND to rise.
                   Figure 37-18. Instruction Transmission Waveform 7
                Write INSTRFRAME

                              CS

                            SCK

                          DATA0                                    A20 A16 A12 A8 A4 A0 O4 O0                D4 D0          D4 D0         A20 A16 A12 A8 A4 A0 O4 O0                D4 D0


                           DATA1                                   A21 A17 A13 A9 A5 A1 O5 O1                D5 D1          D5 D1         A21 A17 A13 A9 A5 A1 O5 O1                D5 D1


                          DATA2                                    A22 A18 A14 A10 A6 A2 O6 O2               D6 D2          D6 D2         A22 A18 A14 A10 A6 A2 O6 O2               D6 D2


                          DATA3                                    A23 A19 A15 A11 A7 A3 O7 O3               D7 D3          D7 D3         A23 A19 A15 A11 A7 A3 O7 O3               D7 D3
                                             Instruction EBh             Address       Option Dummy cycles           Data                       Address       Option Dummy cycles      Data
                         Read AHB




                   Example 37-8. Example 8
                   Instruction in Quad SPI, with address in Quad SPI, without option, with data read from
                   Quad SPI, with two dummy cycles, with fetch.
                   Command: HIGH-SPEED READ (0Bh)
                     •    Write 0x0000_000B to INSTRCTRL register.
                     •    Write 0x0002_20B6 to INSTRFRAME register.
                     •    Read INSTRFRAME register (dummy read) to synchronize system bus accesses.
                     •    Read data in the QSPI system bus memory space (0x040 00000–0x0500_0000).
                       Fetch is enabled, the address of the system bus read accesses is always used.
                     • Write LASTXFR bit in CTRLA register to '1'.
                     • Wait for INTFLAG.INSTREND to rise.
                   Figure 37-19. Instruction Transmission Waveform 8
                    Write INSTRFRAME


                                    CS


                                    SCK


                               DATA0                        A20 A16 A12 A8 A4 A0                 D4 D0          D4 D0                     A20 A16 A12 A8 A4 A0                 D4 D0


                               DATA1                        A21 A17 A13 A9 A5 A1                 D5 D1          D5 D1                     A21 A17 A13 A9 A5 A1                 D5 D1


                               DATA2                        A22 A18 A14 A10 A6 A2                D6 D2          D6 D2                     A22 A18 A14 A10 A6 A2                D6 D2


                               DATA3                        A23 A19 A15 A11 A7 A3                D7 D3          D7 D3                     A23 A19 A15 A11 A7 A3                D7 D3
                                          Instruction 0Bh         Address          Dummy cycles          Data                 Instruction 0Bh      Address        Dummy cycles              Data

                           R ead AHB




37.6.9   Scrambling/Unscrambling Function
         The scrambling/unscrambling function cannot be performed on devices other than memories. Data is
         scrambled when written to memory and unscrambled when data is read.
         The external data lines can be scrambled in order to prevent intellectual property data located in off-chip
         memories from being easily recovered by analyzing data at the package pin level of either the micro-
         controller or the QSPI slave device (e.g. memory).
         The scrambling/unscrambling function can be enabled by writing a '1' to the ENABLE bit in the
         Scrambling Control register (SCRAMBCTRL.ENABLE).




         © 2019 Microchip Technology Inc.                                                          Datasheet                                                            DS60001507E-page 1084
                                                             SAM D5x/E5x Family Data Sheet
                                                                    QSPI - Quad Serial Peripheral Interface

         The scrambling and unscrambling are performed on-the-fly without impacting the throughput.
         The scrambling method depends on the user-configurable Scrambling User Key in the Scrambling Key
         register (SCRAMBKEY.KEY). This register is only accessible in write mode.
         By default, the scrambling and unscrambling algorithm includes the scrambling user key, plus a device-
         dependent random value. This random value is not included when the Scrambling/Unscrambling Random
         Value Disable bit in the Scrambling Mode register (SCRAMBCTRL.RANDOMDIS) is written to ‘1’.
         The random value is neither user configurable nor readable. If SCRAMBCTRL.RANDOMDIS=0, data
         scrambled by a given circuit cannot be unscrambled by a different circuit.
         If SCRAMBCTRL.RANDOMDIS=1, the scrambling/unscrambling algorithm includes only the scrambling
         user key, making it possible to manage data by different circuits. Note that the same key must be used by
         the different circuits.
         The scrambling user key must be securely stored in a reliable non-volatile memory in order to recover
         data from the off-chip memory. Any data scrambled with a given key cannot be recovered if the key is
         lost.

37.6.10 DMA Operation
        The QSPI generates the following DMA requests:
          • Data received (RX): The request is set when data is available in the RXDATA register, and cleared
            when RXDATA is read.
          • Data transmit (TX): The request is set when the transmit buffer (TXDATA) is empty, and cleared
            when TXDATA is written.
         Note: If DMA and RX memory modes are selected, a QSPI memory space read operation is required to
         force the first triggering.
         If the CPU accesses the registers which are source of DMA request set/clear condition, the DMA request
         can be lost or the DMA transfer can be corrupted.

37.6.11 Interrupts
        The QSPI has the following interrupt source:
          • Interrupt Request (INTREQ): Indicates that at least one bit in the Interrupt Flag Status and Clear
            register (INTFLAG) is set to '1'.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable Set (INTENSET)
         register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
         register. An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is
         enabled. The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or
         the QSPI is reset. All interrupt requests from the peripheral are ORed together on system level to
         generate one combined interrupt request to the NVIC. The user must read the INTFLAG register to
         determine which interrupt condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated.




        © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1085
                                              SAM D5x/E5x Family Data Sheet
                                                     QSPI - Quad Serial Peripheral Interface


37.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0                                                       ENABLE     SWRST
                             15:8
 0x00         CTRLA
                             23:16
                             31:24                                                                LASTXFER
                              7:0            CSMODE[1:0]         SMEMREG    WDRBT      LOOPEN      MODE
                             15:8                                              DATALEN[3:0]
 0x04         CTRLB
                             23:16                         DLYBCT[7:0]
                             31:24                         DLYCS[7:0]
                              7:0                                                       CPHA       CPOL
                             15:8                           BAUD[7:0]
 0x08          BAUD
                             23:16                         DLYBS[7:0]
                             31:24
                              7:0                           DATA[7:0]
                             15:8                          DATA[15:8]
 0x0C         RXDATA
                             23:16
                             31:24
                              7:0                           DATA[7:0]
                             15:8                          DATA[15:8]
 0x10         TXDATA
                             23:16
                             31:24
                              7:0                                  ERROR     TXC         DRE        RXC
                             15:8                                          INSTREND                CSRISE
 0x14        INTENCLR
                             23:16
                             31:24
                              7:0                                  ERROR     TXC         DRE        RXC
                             15:8                                          INSTREND                CSRISE
 0x18        INTENSET
                             23:16
                             31:24
                              7:0                                  ERROR     TXC         DRE        RXC
                             15:8                                          INSTREND                CSRISE
 0x1C        INTFLAG
                             23:16
                             31:24
                              7:0                                                       ENABLE
                             15:8                                                      CSSTATUS
 0x20         STATUS
                             23:16
                             31:24
 0x24
   ...       Reserved
 0x2F
                              7:0                           ADDR[7:0]
                             15:8                          ADDR[15:8]
 0x30       INSTRADDR
                             23:16                         ADDR[23:16]
                             31:24                         ADDR[31:24]




          © 2019 Microchip Technology Inc.     Datasheet                              DS60001507E-page 1086
                                                                   SAM D5x/E5x Family Data Sheet
                                                                           QSPI - Quad Serial Peripheral Interface

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                            INSTR[7:0]
                                 15:8
   0x34           INSTRCTRL
                                 23:16                                       OPTCODE[7:0]
                                 31:24
                                  7:0     DATAEN   OPTCODEEN   ADDREN     INSTREN                             WIDTH[2:0]
                                 15:8      DDREN    CRMODE        TFRTYPE[1:0]                  ADDRLEN         OPTCODELEN[1:0]
   0x38         INSTRFRAME
                                 23:16                                                        DUMMYLEN[4:0]
                                 31:24
   0x3C
     ...           Reserved
   0x3F
                                  7:0                                                                     RANDOMDIS        ENABLE
                                 15:8
   0x40         SCRAMBCTRL
                                 23:16
                                 31:24
                                  7:0                                             KEY[7:0]
                                 15:8                                            KEY[15:8]
   0x44          SCRAMBKEY
                                 23:16                                           KEY[23:16]
                                 31:24                                           KEY[31:24]




37.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Refer to the Peripheral Access Controller for more information.
               Some registers are enable-protected, meaning they can only be written when the QSPI is disabled.
               Enable-protection is denoted by the Enable-Protected property in each individual register description.




              © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1087
                                                                    SAM D5x/E5x Family Data Sheet
                                                                           QSPI - Quad Serial Peripheral Interface

37.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00000000
               Property:    -
               Control A


         Bit         31            30            29            28            27            26          25           24
                                                                                                                 LASTXFER
   Access                                                                                                            W
    Reset                                                                                                            0


         Bit         23            22            21            20            19            18          17           16


   Access
    Reset


         Bit         15            14            13            12            11            10          9             8


   Access
    Reset


         Bit         7             6             5              4             3             2          1             0
                                                                                                    ENABLE        SWRST
   Access                                                                                             R/W            W
    Reset                                                                                              0             0


               Bit 24 – LASTXFER Last Transfer
               0: No effect.
               1: The chip select will be de-asserted after the character written in TD has been transferred.

               Bit 1 – ENABLE Enable
               Writing a '0' to this bit disables the QSPI.
               Writing a '1' to this bit enables the QSPI to transfer and receive data.
               As soon as ENABLE is reset, QSPI finishes its transfer.
               All pins are set in input mode and no data is received or transmitted.
               If a transfer is in progress, the transfer is finished before the QSPI is disable.

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit resets the QSPI. A software-triggered hardware reset of the QSPI interface is
               performed.
               DMAC channels are not affected by software reset.




           © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 1088
                                                                      SAM D5x/E5x Family Data Sheet
                                                                              QSPI - Quad Serial Peripheral Interface

37.8.2         Control B

               Name:       CTRLB
               Offset:     0x04
               Reset:      0x00000000
               Property:   PAC Write-Protection
               Control B


         Bit        31           30           29             28                    27    26              25           24
                                                                     DLYCS[7:0]
   Access          R/W          R/W           R/W            R/W                  R/W    R/W             R/W         R/W
    Reset            0            0            0                 0                 0      0                  0        0


         Bit        23           22           21             20                    19    18              17           16
                                                                     DLYBCT[7:0]
   Access          R/W          R/W           R/W            R/W                  R/W    R/W             R/W         R/W
    Reset            0            0            0                 0                 0      0                  0        0


         Bit        15           14           13             12                    11    10                  9        8
                                                                                              DATALEN[3:0]
   Access                                                                         R/W    R/W             R/W         R/W
    Reset                                                                          0      0                  0        0


         Bit         7            6            5                 4                 3      2                  1        0
                                                   CSMODE[1:0]              SMEMREG     WDRBT         LOOPEN        MODE
   Access                                     R/W            R/W                  R/W    R/W             R/W         R/W
    Reset                                      0                 0                 0      0                  0        0


               Bits 31:24 – DLYCS[7:0] Minimum Inactive CS Delay
               This bit field defines the minimum delay between the inactivation and the activation of CS. The DLYCS
               time guarantees the slave minimum deselect time.
               If DLYCS is 0x00, one CLK_QSPI_AHB period will be inserted by default.
               Otherwise, the following equation determines the delay:

               Bits 23:16 – DLYBCT[7:0] Delay Between Consecutive Transfers
               This field defines the delay between two consecutive transfers with the same peripheral without removing
               the chip select. The delay is always inserted after each transfer and before removing the chip select if
               needed.
               When DLYBCT=0x00, no delay between consecutive transfers is inserted and the clock keeps its duty
               cycle over the character transfers. In Serial Memory mode (MODE=1), DLYBCT is ignored and no delay
               is inserted. Otherwise, the following equation determines the delay:

               Bits 11:8 – DATALEN[3:0] Data Length
               The DATALEN field determines the number of data bits transferred. Reserved values should not be used.
                Value      Name                         Description
                0x0        8BITS                        8-bits transfer
                0x1        9BITS                        9-bits transfer
                0x2        10BITS                       10-bits transfer
                0x3        11BITS                       11-bits transfer




           © 2019 Microchip Technology Inc.                             Datasheet                        DS60001507E-page 1089
                                                 SAM D5x/E5x Family Data Sheet
                                                        QSPI - Quad Serial Peripheral Interface

 Value        Name                           Description
 0x4          12BITS                         12-bits transfer
 0x5          13BITS                         13-bits transfer
 0x6          14BITS                         14-bits transfer
 0x7          15BITS                         15-bits transfer
 0x8          16BITS                         16-bits transfer
 0x9-0xF                                     Reserved

Bits 5:4 – CSMODE[1:0] Chip Select Mode
The CSMODE field determines how the chip select is de-asserted.
 Value      Name             Description
 0x0        NORELOAD         The chip select is de-asserted if TD has not been reloaded before the
                             end of the current transfer.
 0x1        LASTXFER         The chip select is de-asserted when the bit LASTXFER is written at 1
                             and the character written in TD has been transferred.
 0x2        SYSTEMATICALLY The chip select is de-asserted systematically after each transfer.
 0x3                         Reserved

Bit 3 – SMEMREG Serial Memory Register Mode
Value      Description
0          Serial memory registers are written via AHB access.
1          Serial memory registers are written via APB access. Reset the QSPI.

Bit 2 – WDRBT Wait Data Read Before Transfer
This bit determines the Wait Data Read Before Transfer option.

Bit 1 – LOOPEN Local Loopback Enable
This bit defines if the Local Loopback is enabled or disabled.
LOOPEN controls the local loopback on the data serializer for testing in SPI Mode only. (MISO is
internally connected on MOSI).
 Value       Description
 0           Local Loopback is disabled.
 1           Local Loopback is enabled.

Bit 0 – MODE Serial Memory Mode
This bit defines if the QSPI is in SPI Mode or Serial Memory Mode.
 Value       Name                      Description
 0           SPI                       SPI operating mode
 1           MEMORY                    Serial Memory operating mode




© 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1090
                                                                 SAM D5x/E5x Family Data Sheet
                                                                        QSPI - Quad Serial Peripheral Interface

37.8.3         Baud Rate

               Name:       BAUD
               Offset:     0x08
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31           30           29          28                 27     26           25           24


   Access
    Reset


         Bit        23           22           21          20                 19     18           17           16
                                                                DLYBS[7:0]
   Access          R/W          R/W           R/W         R/W                R/W   R/W          R/W          R/W
    Reset           0             0            0           0                  0      0           0            0


         Bit        15           14           13          12                 11     10           9            8
                                                                BAUD[7:0]
   Access          R/W          R/W           R/W         R/W                R/W   R/W          R/W          R/W
    Reset           0             0            0           0                  0      0           0            0


         Bit        7             6            5           4                  3      2           1            0
                                                                                               CPHA         CPOL
   Access                                                                                       R/W          R/W
    Reset                                                                                        0            0


               Bits 23:16 – DLYBS[7:0] Delay Before SCK
               This field defines the delay from CS valid to the first valid SCK transition.
               When DLYBS equals zero, the CS valid to SCK transition is 1/2 the SCK clock period.
               Otherwise, the following equation determines the delay:
               Equation 37-1. Delay Before SCK
                                       �����
               ����� ������ ��� =
                                        ���

               Bits 15:8 – BAUD[7:0] Serial Clock Baud Rate
               The QSPI uses a modulus counter to derive the SCK baud rate from the module clock CLK_QSPI_AHB.
               The Baud rate is selected by writing a value from 0 to 255 in the BAUD field. The following equation
               determines the SCK baud rate:
               Equation 37-2. SCK Baud Rate
                                      ���
               ��� ���� ���� =
                                    ���� + 1

               Bit 1 – CPHA Clock Phase
               CPHA determines which edge of SCK causes data to change and which edge causes data to be
               captured. CPHA is used with CPOL to produce the required clock/data relationship between master and
               slave devices.




           © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1091
                                                 SAM D5x/E5x Family Data Sheet
                                                        QSPI - Quad Serial Peripheral Interface

 Value        Description
 0            Data is captured on the leading edge of SCK and changed on the following edge of SCK.
 1            Data is changed on the leading edge of SCK and captured on the following edge of SCK.

Bit 0 – CPOL Clock Polarity
CPOL is used to determine the inactive state value of the serial clock (SCK). It is used with CPHA to
produce the required clock/data relationship between master and slave devices.
 Value     Description
 0         The inactive state value of SCK is logic level zero.
 0         The inactive state value of SCK is logic level 'one'.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1092
                                                                    SAM D5x/E5x Family Data Sheet
                                                                           QSPI - Quad Serial Peripheral Interface

37.8.4         Receive Data

               Name:        RXDATA
               Offset:      0x0C
               Reset:       0x00000000
               Property:    -


         Bit        31            30            29            28                27       26            25           24


   Access
    Reset


         Bit        23            22            21            20                19       18            17           16


   Access
    Reset


         Bit        15            14            13            12                11       10             9           8
                                                                   DATA[15:8]
   Access            R             R            R             R                 R         R             R           R
    Reset            0             0            0             0                 0         0             0           0


         Bit         7             6            5             4                 3         2             1           0
                                                                   DATA[7:0]
   Access            R             R            R             R                 R         R             R           R
    Reset            0             0            0             0                 0         0             0           0


               Bits 15:0 – DATA[15:0] Receive Data
               Data received by the QSPI is stored in this register right-justified. Unused bits read zero.




           © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 1093
                                                                   SAM D5x/E5x Family Data Sheet
                                                                          QSPI - Quad Serial Peripheral Interface

37.8.5         Transmit Data

               Name:        TXDATA
               Offset:      0x10
               Reset:       0x00000000
               Property:    -


         Bit        31            30           29            28                27       26            25            24


   Access
    Reset


         Bit        23            22           21            20                19       18            17            16


   Access
    Reset


         Bit        15            14           13            12                11       10            9             8
                                                                  DATA[15:8]
   Access           W             W             W            W                 W        W             W             W
    Reset            0            0             0             0                0         0            0             0


         Bit         7            6             5             4                3         2            1             0
                                                                  DATA[7:0]
   Access           W             W             W            W                 W        W             W             W
    Reset            0            0             0             0                0         0            0             0


               Bits 15:0 – DATA[15:0] Transmit Data
               Data to be transmitted by the QSPI is stored in this register. Information to be transmitted must be written
               to the transmit data register in a right-justified format.




           © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1094
                                                                    SAM D5x/E5x Family Data Sheet
                                                                          QSPI - Quad Serial Peripheral Interface

37.8.6         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x14
               Reset:       0x00000000
               Property:    PAC Write-Protection


         Bit        31             30            29            28              27       26      25           24


   Access
    Reset


         Bit        23             22            21            20              19       18      17           16


   Access
    Reset


         Bit        15             14            13            12              11       10       9           8
                                                                                     INSTREND             CSRISE
   Access                                                                              R/W                  R/W
    Reset                                                                               0                    0


         Bit         7             6             5             4                3       2        1           0
                                                                          ERROR        TXC      DRE         RXC
   Access                                                                      R/W     R/W      R/W         R/W
    Reset                                                                       0       0        0           0


               Bit 10 – INSTREND Instruction End Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' will clear the corresponding interrupt request.
               Value         Description
               0             The INSTREND interrupt is disabled.
               1             The INSTREND interrupt is enabled.

               Bit 8 – CSRISE Chip Select Rise Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' will clear the corresponding interrupt request.
               Value         Description
               0             The CSRISE interrupt is disabled.
               1             The CSRISE interrupt is enabled.

               Bit 3 – ERROR Overrun Error Interrupt Disable
               Writing a '0' to this bit has no effect.
               Writing a '1' will clear the corresponding interrupt request.
               Value         Description
               0             The ERROR interrupt is disabled.
               1             The ERROR interrupt is enabled.




           © 2019 Microchip Technology Inc.                          Datasheet                  DS60001507E-page 1095
                                                    SAM D5x/E5x Family Data Sheet
                                                           QSPI - Quad Serial Peripheral Interface

Bit 2 – TXC Transmission Complete Interrupt Disable
Writing a '0' to this bit has no effect.
Writing a '1' will clear the corresponding interrupt request.
Value         Description
0             The TXC interrupt is disabled.
1             The TXC interrupt is enabled.

Bit 1 – DRE Transmit Data Register Empty Interrupt Disable
Writing a '0' to this bit has no effect.
Writing a '1' will clear the corresponding interrupt request.
Value         Description
0             The DRE interrupt is disabled.
1             The DRE interrupt is enabled.

Bit 0 – RXC Receive Data Register Full Interrupt Disable
Writing a '0' to this bit has no effect.
Writing a '1' will clear the corresponding interrupt request.
Value         Description
0             The RXC interrupt is disabled.
1             The RXC interrupt is enabled.




© 2019 Microchip Technology Inc.                      Datasheet                  DS60001507E-page 1096
                                                                    SAM D5x/E5x Family Data Sheet
                                                                             QSPI - Quad Serial Peripheral Interface

37.8.7         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x18
               Reset:       0x00000000
               Property:    PAC Write-Protection


         Bit        31             30            29            28             27         26        25           24


   Access
    Reset


         Bit        23             22            21            20             19         18        17           16


   Access
    Reset


         Bit        15             14            13            12             11         10        9            8
                                                                                      INSTREND               CSRISE
   Access                                                                               R/W                    R/W
    Reset                                                                                0                      0


         Bit         7             6             5             4               3         2         1            0
                                                                             ERROR      TXC       DRE          RXC
   Access                                                                     R/W       R/W       R/W          R/W
    Reset                                                                      0         0         0            0


               Bit 10 – INSTREND Instruction End Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' will set the corresponding interrupt request.
               Value         Description
               0             The INSTREND interrupt is disabled.
               1             The INSTREND interrupt is enabled.

               Bit 8 – CSRISE Chip Select Rise Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' will set the corresponding interrupt request.
               Value         Description
               0             The CSRISE interrupt is disabled.
               1             The CSRISE interrupt is enabled.

               Bit 3 – ERROR Overrun Error Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' will set the corresponding interrupt request.
               Value         Description
               0             The ERROR interrupt is disabled.
               1             The ERROR interrupt is enabled.




           © 2019 Microchip Technology Inc.                          Datasheet                     DS60001507E-page 1097
                                                    SAM D5x/E5x Family Data Sheet
                                                              QSPI - Quad Serial Peripheral Interface

Bit 2 – TXC Transmission Complete Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' will set the corresponding interrupt request.
Value         Description
0             The TXC interrupt is disabled.
1             The TXC interrupt is enabled.

Bit 1 – DRE Transmit Data Register Empty Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' will set the corresponding interrupt request.
Value         Description
0             The DRE interrupt is disabled.
1             The DRE interrupt is enabled.

Bit 0 – RXC Receive Data Register Full Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' will set the corresponding interrupt request.
Value         Description
0             The RXC interrupt is disabled.
1             The RXC interrupt is enabled.




© 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1098
                                                                  SAM D5x/E5x Family Data Sheet
                                                                        QSPI - Quad Serial Peripheral Interface

37.8.8         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x1C
               Reset:      0x00000000
               Property:   -


         Bit        31            30           29            28             27          26           25           24


   Access
    Reset


         Bit        23            22           21            20             19          18           17           16


   Access
    Reset


         Bit        15            14           13            12             11          10           9                8
                                                                                    INSTREND                    CSRISE
   Access                                                                              R/W                        R/W
    Reset                                                                               0                             0


         Bit         7            6             5            4              3           2            1                0
                                                                        ERROR          TXC          DRE           RXC
   Access                                                                R/W           R/W          R/W           R/W
    Reset                                                                   0           0            0                0


               Bit 10 – INSTREND Instruction End
               This bit is set when an Instruction End has been detected.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the flag.

               Bit 8 – CSRISE Chip Select Rise
               The bit is set when a Chip Select Rise has been detected.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the flag.

               Bit 3 – ERROR Overrun Error
               This bit is set when an ERROR has occurred.
               An ERROR occurs when RXDATA is loaded at least twice from the serializer.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the flag.

               Bit 2 – TXC Transmission Complete
               0: As soon as data is written in TXDATA.
               1: TXDATA and internal shifter are empty. If a transfer delay has been defined, TXC is set after the
               completion of such delay.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1099
                                                  SAM D5x/E5x Family Data Sheet
                                                         QSPI - Quad Serial Peripheral Interface

Bit 1 – DRE Transmit Data Register Empty
0: Data has been written to TXDATA and not yet transferred to the serializer.
1: The last data written in the TXDATA has been transferred to the serializer.
This bit is '0' when the QSPI is disabled or at reset.
The bit is set as soon as ENABLE bit is set.

Bit 0 – RXC Receive Data Register Full
0: No data has been received since the last read of RXDATA.
1: Data has been received and the received data has been transferred from the serializer to RXDATA
since the last read of RXDATA.




© 2019 Microchip Technology Inc.                    Datasheet                     DS60001507E-page 1100
                                                              SAM D5x/E5x Family Data Sheet
                                                                  QSPI - Quad Serial Peripheral Interface

37.8.9         Status

               Name:       STATUS
               Offset:     0x20
               Reset:      0x00000200
               Property:   -


         Bit        31           30           29         28         27       26         25           24


   Access
    Reset


         Bit        23           22           21         20         19       18         17           16


   Access
    Reset


         Bit        15           14           13         12         11       10         9            8
                                                                                     CSSTATUS
   Access                                                                               R
    Reset                                                                               1


         Bit         7            6            5         4          3         2         1            0
                                                                                      ENABLE
   Access                                                                               R
    Reset                                                                               0


               Bit 9 – CSSTATUS Chip Select
               Value      Description
               0          Chip Select is asserted.
               1          Chip Select is not asserted.

               Bit 1 – ENABLE Enable
               Value      Description
               0          QSPI is disabled.
               1          QSPI is enabled.




           © 2019 Microchip Technology Inc.                   Datasheet                 DS60001507E-page 1101
                                                                SAM D5x/E5x Family Data Sheet
                                                                       QSPI - Quad Serial Peripheral Interface

37.8.10 Instruction Address

            Name:       INSTRADDR
            Offset:     0x30
            Reset:      0x00000000
            Property:   -


      Bit        31            30           29           28                 27     26        25           24
                                                              ADDR[31:24]
  Access        R/W           R/W          R/W           R/W                R/W    R/W      R/W          R/W
   Reset          0            0             0            0                  0      0        0            0


      Bit        23            22           21           20                 19     18        17           16
                                                              ADDR[23:16]
  Access        R/W           R/W          R/W           R/W                R/W    R/W      R/W          R/W
   Reset          0            0             0            0                  0      0        0            0


      Bit        15            14           13           12                 11     10        9            8
                                                               ADDR[15:8]
  Access        R/W           R/W          R/W           R/W                R/W    R/W      R/W          R/W
   Reset          0            0             0            0                  0      0        0            0


      Bit         7            6             5            4                  3      2        1            0
                                                               ADDR[7:0]
  Access        R/W           R/W          R/W           R/W                R/W    R/W      R/W          R/W
   Reset          0            0             0            0                  0      0        0            0


            Bits 31:0 – ADDR[31:0] Instruction Address
            Address to send to the serial flash memory in the instruction frame.




        © 2019 Microchip Technology Inc.                          Datasheet                  DS60001507E-page 1102
                                                                SAM D5x/E5x Family Data Sheet
                                                                       QSPI - Quad Serial Peripheral Interface

37.8.11 Instruction Code

            Name:       INSTRCTRL
            Offset:     0x34
            Reset:      0x00000000
            Property:   -


      Bit        31            30           29            28                27      26       25           24


  Access
   Reset


      Bit        23            22           21            20                19      18       17           16
                                                           OPTCODE[7:0]
  Access        R/W           R/W          R/W           R/W                R/W     R/W     R/W          R/W
   Reset          0            0             0            0                  0       0       0            0


      Bit        15            14           13            12                11      10       9            8


  Access
   Reset


      Bit         7            6             5            4                  3       2       1            0
                                                               INSTR[7:0]
  Access        R/W           R/W          R/W           R/W                R/W     R/W     R/W          R/W
   Reset          0            0             0            0                  0       0       0            0


            Bits 23:16 – OPTCODE[7:0] Option Code
            These bits define the option code to send to the serial flash memory.

            Bits 7:0 – INSTR[7:0] Instruction Code
            Instruction code to send to the serial flash memory.




        © 2019 Microchip Technology Inc.                           Datasheet                 DS60001507E-page 1103
                                                                    SAM D5x/E5x Family Data Sheet
                                                                        QSPI - Quad Serial Peripheral Interface

37.8.12 Instruction Frame

            Name:       INSTRFRAME
            Offset:     0x38
            Reset:      0x00000000
            Property:   -


      Bit        31           30             29             28            27         26            25            24


  Access
   Reset


      Bit        23           22             21             20            19         18            17            16
                                                                                DUMMYLEN[4:0]
  Access                                                   R/W           R/W        R/W            R/W          R/W
   Reset                                                        0         0           0             0            0


      Bit        15           14             13             12            11         10             9            8
               DDREN       CRMODE                TFRTYPE[1:0]                     ADDRLEN          OPTCODELEN[1:0]
  Access        R/W          R/W            R/W            R/W                      R/W            R/W          R/W
   Reset          0            0             0                  0                     0             0            0


      Bit         7            6             5                  4         3           2             1            0
               DATAEN     OPTCODEEN        ADDREN        INSTREN                                WIDTH[2:0]
  Access        R/W          R/W            R/W            R/W                      R/W            R/W          R/W
   Reset          0            0             0                  0                     0             0            0


            Bits 20:16 – DUMMYLEN[4:0] Dummy Cycles Length
            The DUMMYLEN field defines the number of dummy cycles required by the serial Flash memory before
            data transfer.

            Bit 15 – DDREN Double Data Rate Enable
            Value      Description
            0          Double Data Rate operating mode is disabled.
            1          Double Data Rate operating mode is enabled.

            Bit 14 – CRMODE Continuous Read Mode
            This bit defines if the Continuous Read Mode is enabled or disabled.
             Value       Description
             0           Continuous Read Mode is disabled.
             1           Continuous Read Mode is enabled.

            Bits 13:12 – TFRTYPE[1:0] Data Transfer Type
            These bits define the data type transfer.
             Value      Name               Description
             0x0        READ               Read transfer from the serial memory.Scrambling is not performed.Read
                                           at random location (fetch) in the serial flash memory is not possible.




        © 2019 Microchip Technology Inc.                            Datasheet                       DS60001507E-page 1104
                                                   SAM D5x/E5x Family Data Sheet
                                                          QSPI - Quad Serial Peripheral Interface

 Value        Name        Description
 0x1          READMEMORY  Read data transfer from the serial memory.If enabled, scrambling is
                          performed.Read at random location (fetch) in the serial flash memory is
                          possible.
 0x2          WRITE       Write transfer into the serial memory.Scrambling is not performed.
 0x3          WRITEMEMORY Write data transfer into the serial memory. If enabled, scrambling is
                          performed.

Bit 10 – ADDRLEN Address Length
The ADDRLEN bit determines the length of the address.
 Value     Name                   Description
 0x0       24BITS                 24-bits address length
 0x1       32BITS                 32-bits address length

Bits 9:8 – OPTCODELEN[1:0] Option Code Length
The OPTCODELEN field determines the length of the option code. The value written in OPTCODELEN
must be coherent with value written in the field WIDTH. For example: OPTCODELEN=0 (1-bit option
code) is not coherent with WIDTH=6 (option code sent with QuadSPI protocol, thus the minimum length
of the option code is 4-bit).
 Value       Name                 Description
 0x0         1BIT                 1-bit length option code
 0x1         2BITS                2-bits length option code
 0x2         4BITS                4-bits length option code
 0x3         8BITS                8-bits length option code

Bit 7 – DATAEN Data Enable
Value      Description
0          No data is sent/received to/from the serial flash memory.
1          Data is sent/received to/from the serial flash memory.

Bit 6 – OPTCODEEN Option Enable
Value      Description
0          The option is not sent to the serial flash memory
1          The option is sent to the serial flash memory.

Bit 5 – ADDREN Address Enable
Value      Description
0          The transfer address is not sent to the serial flash memory.
1          The transfer address is sent to the serial flash memory.

Bit 4 – INSTREN Instruction Enable
Value       Description
0           The instruction is not sent to the serial flash memory.
1           The instruction is sent to the serial flash memory.

Bits 2:0 – WIDTH[2:0] Instruction Code, Address, Option Code and Data Width
This field defines the width of the instruction code, the address, the option and the data.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1105
                                                  SAM D5x/E5x Family Data Sheet
                                                         QSPI - Quad Serial Peripheral Interface

 Value        Name           Description
 0x0          SINGLE_BIT_SPI Instruction: Single-bit SPI / Address-Option: Single-bit SPI / Data: Single-
                             bit SPI
 0x1          DUAL_OUTPUT Instruction: Single-bit SPI / Address-Option: Single-bit SPI / Data: Dual
                             SPI
 0x2          QUAD_OUTPUT Instruction: Single-bit SPI / Address-Option: Single-bit SPI / Data: Quad
                             SPI
 0x3          DUAL_IO        Instruction: Single-bit SPI / Address-Option: Dual SPI / Data: Dual SPI
 0x4          QUAD_IO        Instruction: Single-bit SPI / Address-Option: Quad SPI / Data: Quad SPI
 0x5          DUAL_CMD       Instruction: Dual SPI / Address-Option: Dual SPI / Data: Dual SPI
 0x6          QUAD_CMD       Instruction: Quad SPI / Address-Option: Quad SPI / Data: Quad SPI
 0x7                         Reserved




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1106
                                                              SAM D5x/E5x Family Data Sheet
                                                                    QSPI - Quad Serial Peripheral Interface

37.8.13 Scrambling Mode

           Name:       SCRAMBCTRL
           Offset:     0x40
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31            30           29            28           27             26      25           24


  Access
   Reset


     Bit        23            22           21            20           19             18      17           16


  Access
   Reset


     Bit        15            14           13            12           11             10       9           8


  Access
   Reset


     Bit         7            6             5            4             3             2        1           0
                                                                                          RANDOMDIS    ENABLE
  Access                                                                                     R/W         R/W
   Reset                                                                                      0           0


           Bit 1 – RANDOMDIS Scrambling/Unscrambling Random Value Disable
           Value      Description
           0          The scrambling/unscrambling algorithm includes the scrambling user key plus a random
                      value that may differ from chip to chip.
           1          The scrambling/unscrambling algorithm includes only the scrambling user key.

           Bit 0 – ENABLE Scrambling/Unscrambling Enable
           This bit defines if the scrambling/unscrambling is enabled or disabled.
            Value       Description
            0           Scrambling/unscrambling is disabled.
            1           Scrambling/unscrambling is enabled.




       © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1107
                                                             SAM D5x/E5x Family Data Sheet
                                                                    QSPI - Quad Serial Peripheral Interface

37.8.14 Scrambling Key

           Name:       SCRAMBKEY
           Offset:     0x44
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31           30           29           28                27    26         25           24
                                                            KEY[31:24]
  Access        W            W            W            W                 W      W         W            W
   Reset        0             0           0            0                 0      0         0            0


     Bit        23           22           21           20                19    18         17           16
                                                            KEY[23:16]
  Access        W            W            W            W                 W      W         W            W
   Reset        0             0           0            0                 0      0         0            0


     Bit        15           14           13           12                11    10         9            8
                                                            KEY[15:8]
  Access        W            W            W            W                 W      W         W            W
   Reset        0             0           0            0                 0      0         0            0


     Bit        7             6           5            4                 3      2         1            0
                                                             KEY[7:0]
  Access        W            W            W            W                 W      W         W            W
   Reset        0             0           0            0                 0      0         0            0


           Bits 31:0 – KEY[31:0] Scrambling User Key
           This field defines the user key value.




       © 2019 Microchip Technology Inc.                       Datasheet                   DS60001507E-page 1108
