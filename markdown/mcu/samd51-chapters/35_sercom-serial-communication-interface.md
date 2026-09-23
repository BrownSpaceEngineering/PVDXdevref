# 33. SERCOM – Serial Communication Interface

*Source: `Atmel-SAMD51.pdf`, pages 913-921 — SAMD51 family datasheet*

                                                           SAM D5x/E5x Family Data Sheet
                                                             SERCOM – Serial Communication Interface


33.    SERCOM – Serial Communication Interface

33.1   Overview
       There are up to eight instances of the Serial Communication interface (SERCOM) peripheral.
       A SERCOM can be configured to support a number of modes: I2C, SPI, and USART. When an instance
       of SERCOM is configured and enabled, all of the resources of that SERCOM instance will be dedicated
       to the selected mode.
       The SERCOM serial engine consists of a transmitter and receiver, baud-rate generator and address
       matching functionality. It can use the internal generic clock or an external clock. Using an external clock
       allows the SERCOM to be operated in all Sleep modes.
       Related Links
       34. SERCOM USART - SERCOM Synchronous and Asynchronous Receiver and Transmitter
       35. SERCOM SPI – SERCOM Serial Peripheral Interface
       36. SERCOM I2C – Inter-Integrated Circuit
       6.2.6 SERCOM I2C Configurations



33.2   Features
         • Interface for Configuring into one of the Following:
              – Inter-Integrated Circuit (I2C) two-wire serial interface
              – System Management Bus (SMBus™) compatible
              – Serial Peripheral Interface (SPI)
              – Universal Synchronous/Asynchronous Receiver/Transmitter (USART)
         •   Single Transmit Buffer and Double Receive Buffer
         •   Baud-rate Generator
         •   Address Match/mask Logic
         •   Operational in all Sleep modes with an External Clock Source
         •   Can be used with DMA
         •   32-bit Extension for Better System Bus Utilization
       See the Related Links for full feature lists of the interface configurations.
       Related Links
       34. SERCOM USART - SERCOM Synchronous and Asynchronous Receiver and Transmitter
       35. SERCOM SPI – SERCOM Serial Peripheral Interface
       36. SERCOM I2C – Inter-Integrated Circuit
       6.2.6 SERCOM I2C Configurations




       © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 913
                                                            SAM D5x/E5x Family Data Sheet
                                                              SERCOM – Serial Communication Interface


33.3     Block Diagram
         Figure 33-1. SERCOM Block Diagram

                   SERCOM
                       Register Interface

                           CONTROL/STATUS        TX/RX DATA             BAUD/ADDR




                        Mode Specific               Serial Engine

                           Mode n
                                                                             Baud Rate
                              Mode 1                      Transmitter        Generator
                                                                                                 PAD[3:0]
                                    Mode 0


                                                           Receiver           Address
                                                                               Match




33.4     Signal Description
         See the respective SERCOM mode chapters for details.
         Related Links
         34. SERCOM USART - SERCOM Synchronous and Asynchronous Receiver and Transmitter
         35. SERCOM SPI – SERCOM Serial Peripheral Interface
         36. SERCOM I2C – Inter-Integrated Circuit


33.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

33.5.1   I/O Lines
         Using the SERCOM I/O lines requires the I/O pins to be configured using port configuration (PORT).
         The SERCOM has four internal pads, PAD[3:0], and the signals from I2C, SPI and USART are routed
         through these SERCOM pads through a multiplexer. The configuration of the multiplexer is available from
         the different SERCOM modes. Refer to the mode specific chapters for additional information.
         Related Links
         34. SERCOM USART - SERCOM Synchronous and Asynchronous Receiver and Transmitter
         35. SERCOM SPI – SERCOM Serial Peripheral Interface
         36. SERCOM I2C – Inter-Integrated Circuit
         32. PORT - I/O Pin Controller
         34.3 Block Diagram

33.5.2   Power Management
         The SERCOM can operate in any Sleep mode provided the selected clock source is running. SERCOM
         interrupts can be configured to wake the device from sleep modes.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 914
                                                           SAM D5x/E5x Family Data Sheet
                                                            SERCOM – Serial Communication Interface

         Related Links
         18. PM – Power Manager

33.5.3   Clocks
         The SERCOM bus clock (CLK_SERCOMx_APB) can be enabled and disabled in the Main Clock
         Controller. Refer to Peripheral Clock Masking for details and default status of this clock.
         The SERCOM uses two generic clocks: GCLK_SERCOMx_CORE and GCLK_SERCOMx_SLOW. The
         core clock (GCLK_SERCOMx_CORE) is required to clock the SERCOM while working as a master. The
         slow clock (GCLK_SERCOMx_SLOW) is only required for certain functions. See specific mode chapters
         for details.
         These clocks must be configured and enabled in the Generic Clock Controller (GCLK) before using the
         SERCOM.
         The generic clocks are asynchronous to the user interface clock (CLK_SERCOMx_APB). Due to this
         asynchronicity, writing to certain registers will require synchronization between the clock domains. Refer
         to 33.6.8 Synchronization for details.
         Related Links
         14. GCLK - Generic Clock Controller
         15. MCLK – Main Clock

33.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). The DMAC must be configured
         before the SERCOM DMA requests are used.
         Related Links
         22. DMAC – Direct Memory Access Controller

33.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller (NVIC). The NVIC must be configured
         before the SERCOM interrupts are used.
         Related Links
         10.2 Nested Vector Interrupt Controller

33.5.6   Events
         Not applicable.

33.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will continue normal operation. If the peripheral is
         configured to require periodical service by the CPU through interrupts or similar, improper operation or
         data loss may result during debugging. This peripheral can be forced to halt operation during debugging -
         refer to the Debug Control (DBGCTRL) register for details.

33.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Flag Clear and Status register (INTFLAG)
           • Status register (STATUS)




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 915
                                                                        SAM D5x/E5x Family Data Sheet
                                                                        SERCOM – Serial Communication Interface

           • Data register (DATA)
           • Address register (ADDR)
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller

33.5.9   Analog Connections
         Not applicable.



33.6     Functional Description

33.6.1   Principle of Operation
         The basic structure of the SERCOM serial engine is shown in Figure 33-2. Labels in capital letters are
         synchronous to the system clock and accessible by the CPU; labels in lowercase letters can be
         configured to run on the GCLK_SERCOMx_CORE clock or an external clock.
         Figure 33-2. SERCOM Serial Engine
                                                             Transmitter                             Address Match

                   Selectable               BAUD                                   TX DATA              ADDR/ADDRMASK
                  Internal Clk
                    (GCLK)

                   Ext Clk            Baud Rate Generator

                                               1/- /2- /16


                                                                                 TX Shift Register




                                                             Receiver
                                                                                 RX Shift Register




                                                                                                             Equal
                                                                   Status           RX Buffer


                                 Baud Rate Generator              STATUS           RX DATA



         The transmitter consists of a single write buffer and a Shift register.
         The receiver consists of a one-level (I2C), two-level (USART, SPI) receive buffer and a Shift register.
         The baud-rate generator is capable of running on the GCLK_SERCOMx_CORE clock or an external
         clock.
         Address matching logic is included for SPI and I2C operation.




         © 2019 Microchip Technology Inc.                                  Datasheet                         DS60001507E-page 916
                                                            SAM D5x/E5x Family Data Sheet
                                                                 SERCOM – Serial Communication Interface

33.6.2    Basic Operation

33.6.2.1 Initialization
          The SERCOM must be configured to the desired mode by writing the Operating Mode bits in the Control
          A register (CTRLA.MODE). Refer to table SERCOM Modes for details.
          Table 33-1. SERCOM Modes

          CTRLA.MODE                               Description
          0x0                                      USART with external clock
          0x1                                      USART with internal clock
          0x2                                      SPI in slave operation
          0x3                                      SPI in master operation
          0x4                                      I2C slave operation
          0x5                                      I2C master operation
          0x6-0x7                                  Reserved

          For further initialization information, see the respective SERCOM mode chapters:
          Related Links
          34. SERCOM USART - SERCOM Synchronous and Asynchronous Receiver and Transmitter
          35. SERCOM SPI – SERCOM Serial Peripheral Interface
          36. SERCOM I2C – Inter-Integrated Circuit

33.6.2.2 Enabling, Disabling, and Resetting
          This peripheral is enabled by writing '1' to the Enable bit in the Control A register (CTRLA.ENABLE), and
          disabled by writing '0' to it.
          Writing ‘1’ to the Software Reset bit in the Control A register (CTRLA.SWRST) will reset all registers of
          this peripheral to their initial states, except the DBGCTRL register, and the peripheral is disabled.
          Refer to the CTRLA register description for details.
33.6.2.3 Clock Generation – Baud-Rate Generator
          The baud-rate generator, as shown in Figure 33-3, generates internal clocks for asynchronous and
          synchronous communication. The output frequency (fBAUD) is determined by the Baud register (BAUD)
          setting and the baud reference frequency (fref). The baud reference clock is the serial engine clock, and it
          can be internal or external.
          For asynchronous communication, the /16 (divide-by-16) output is used when transmitting, whereas
          the /1 (divide-by-1) output is used while receiving.
          For synchronous communication, the /2 (divide-by-2) output is used.
          This functionality is automatically configured, depending on the selected operating mode.




         © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 917
                                                                           SAM D5x/E5x Family Data Sheet
                                                                           SERCOM – Serial Communication Interface

         Figure 33-3. Baud Rate Generator
                                 Selectable
                                Internal Clk
                                                           Baud Rate Generator
                                  (GCLK)
                                               1    fref          Base
                               Ext Clk                                             /2            /8
                                               0                  Period

                         CTRLA.MODE[0]                                        /1        /2              /16




                                                                                                              0   Tx Clk

                                                                                                              1

                                                                                             1                    CTRLA.MODE

                                                                                             0


                                                                                                              1   Rx Clk
                                                                                                  Clock
                                                                                                              0
                                                                                                 Recovery


         Table 33-2 contains equations for the baud rate (in bits per second) and the BAUD register value for each
         operating mode.
         For asynchronous operation, there is one mode: arithmetic mode, the BAUD register value is 16 bits (0 to
         65,535).fractional mode, the BAUD register value is 13 bits, while the fractional adjustment is 3 bits. In
         this mode the BAUD setting must be greater than or equal to 1.
         For synchronous operation, the BAUD register value is 8 bits (0 to 255).
Table 33-2. Baud Rate Equations

Operating Mode        Condition                    Baud Rate (Bits Per Second)                         BAUD Register Value Calculation
Asynchronous                     ����                        ����    ����                                                              �����
                      ����� ≤                      ����� =        1−                                   ���� = 65536 ⋅ 1 − 16 ⋅
Arithmetic                        16                          16     65536                                                              ����

Asynchronous                     ����                                  ����                                          ����     ��
                      ����� ≤                      ����� =                                             ���� =               −
Fractional                        S                                       ��                                      � ⋅ �����    8
                                                             S⋅    ���� + 8

Synchronous                      ����                             ����                                               ����
                      ����� ≤                      ����� =                                             ���� =               −1
                                  2                          2 ⋅ ���� + 1                                         2 ⋅ �����

         S - Number of samples per bit, which can be 16, 8, or 3.
         The Asynchronous Fractional option is used for auto-baud detection.
         The baud rate error is represented by the following formula:
                        ExpectedBaudRate
         Error = 1 −
                         ActualBaudRate
33.6.2.3.1 Asynchronous Arithmetic Mode BAUD Value Selection
         The formula given for fBAUD calculates the average frequency over 65536 fref cycles. Although the BAUD
         register can be set to any value between 0 and 65536, the actual average frequency of fBAUD over a
         single frame is more granular. The BAUD register values that will affect the average frequency over a
         single frame lead to an integer increase in the cycles per frame (CPF)
                  ����
         ��� =         �+�
                 �����




        © 2019 Microchip Technology Inc.                                   Datasheet                                       DS60001507E-page 918
                                                                 SAM D5x/E5x Family Data Sheet
                                                                  SERCOM – Serial Communication Interface

         where
           • D represent the data bits per frame
           • S represent the sum of start and first stop bits, if present.
         Table 33-3 shows the BAUD register value versus baud frequency fBAUD at a serial engine frequency of
         48 MHz. This assumes a D value of 8 bits and an S value of 2 bits (10 bits, including start and stop bits).
         Table 33-3. BAUD Register Value vs. Baud Frequency

          BAUD Register Value               Serial Engine CPF    fBAUD at 100MHz Serial Engine Frequency (fREF)
          0 – 406                           161                  6.211 MHz
          407 – 808                         162                  6.211 MHz
          809 – 1205                        163                  6.173 MHz
          ...                               ...                  ...
          65206                             31775                31.47 kHz
          65207                             31872                31.38 kHz
          65208                             31969                31.28 kHz

33.6.3   Additional Features

33.6.3.1 Address Match and Mask
         The SERCOM address match and mask feature is capable of matching either one address, two unique
         addresses, or a range of addresses with a mask, based on the mode selected. The match uses seven or
         eight bits, depending on the mode.
33.6.3.1.1 Address With Mask
         An address written to the Address bits in the Address register (ADDR.ADDR), and a mask written to the
         Address Mask bits in the Address register (ADDR.ADDRMASK) will yield an address match. All bits that
         are masked are not included in the match. Note that writing the ADDR.ADDRMASK to 'all zeros' will
         match a single unique address, while writing ADDR.ADDRMASK to 'all ones' will result in all addresses
         being accepted.
         Figure 33-4. Address With Mask

                                                  ADDR


                                                                                    Match
                                              ADDRMASK                        ==



                                             rx shift register


33.6.3.1.2 Two Unique Addresses
         The two addresses written to ADDR and ADDRMASK will cause a match.




         © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 919
                                                                     SAM D5x/E5x Family Data Sheet
                                                                       SERCOM – Serial Communication Interface

         Figure 33-5. Two Unique Addresses

                                                ADDR
                                                                        ==

                                            rx shift register                             Match

                                                                        ==
                                             ADDRMASK


33.6.3.1.3 Address Range
         The range of addresses between and including ADDR.ADDR and ADDR.ADDRMASK will cause a match.
         ADDR.ADDR and ADDR.ADDRMASK can be set to any two addresses, with ADDR.ADDR acting as the
         upper limit and ADDR.ADDRMASK acting as the lower limit.
         Figure 33-6. Address Range

                              ADDRMASK                    rx shift register        ADDR           == Match


33.6.4   DMA Operation
         The available DMA interrupts and their depend on the operation mode of the SERCOM peripheral. Refer
         to the Functional Description sections of the respective SERCOM mode.
         Related Links
         34. SERCOM USART - SERCOM Synchronous and Asynchronous Receiver and Transmitter
         35. SERCOM SPI – SERCOM Serial Peripheral Interface
         36. SERCOM I2C – Inter-Integrated Circuit

33.6.5   Interrupts
         Interrupt sources are mode specific. See the respective SERCOM mode chapters for details.
         Each interrupt source has its own Interrupt flag.
         The Interrupt flag in the Interrupt Flag Status and Clear register (INTFLAG) will be set when the Interrupt
         condition is met.
         Each interrupt can be individually enabled by writing '1' to the corresponding bit in the Interrupt Enable
         Set register (INTENSET), and disabled by writing '1' to the corresponding bit in the Interrupt Enable Clear
         register (INTENCLR).
         An interrupt request is generated when the Interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until either the Interrupt flag is cleared, the interrupt is disabled, or
         the SERCOM is reset. For details on clearing Interrupt flags, refer to the INTFLAG register description.
         The value of INTFLAG indicates which Interrupt condition occurred. The user must read the INTFLAG
         register to determine which Interrupt condition is present.
         Note: Interrupts must be globally enabled for interrupt requests.
         Related Links
         10.2 Nested Vector Interrupt Controller




         © 2019 Microchip Technology Inc.                              Datasheet                      DS60001507E-page 920
                                                          SAM D5x/E5x Family Data Sheet
                                                           SERCOM – Serial Communication Interface

33.6.6   Events
         Not applicable.

33.6.7   Sleep Mode Operation
         The peripheral can operate in any Sleep mode where the selected serial clock is running. This clock can
         be external or generated by the internal baud-rate generator.
         The SERCOM interrupts can be used to wake-up the device from Sleep modes. Refer to the different
         SERCOM mode chapters for details.

33.6.8   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.
         Required read synchronization is denoted by the "Read-Synchronized" property in the register
         description.
         Related Links
         13.3 Register Synchronization




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 921
