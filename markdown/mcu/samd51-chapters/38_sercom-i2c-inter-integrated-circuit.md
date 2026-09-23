# 36. SERCOM I2C – Inter-Integrated Circuit

*Source: `Atmel-SAMD51.pdf`, pages 1005-1065 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                 SERCOM I2C – Inter-Integrated Circuit


36.    SERCOM I2C – Inter-Integrated Circuit

36.1   Overview
       The Inter-Integrated Circuit (I2C) interface is one of the available modes in the Serial Communication
       Interface (SERCOM).
       The I2C interface uses the SERCOM transmitter and receiver configured as shown in Figure 36-1. Labels
       in capital letters are registers accessible by the CPU, while lowercase labels are internal to the SERCOM.
       A SERCOM instance can be configured to be either an I2C master or an I2C slave. Both master and slave
       have an interface containing a Shift register, a transmit buffer and a receive buffer. In addition, the I2C
       master uses the SERCOM baud-rate generator, while the I2C slave uses the SERCOM address match
       logic.
       Related Links
       33. SERCOM – Serial Communication Interface



36.2   Features
       SERCOM I2C includes the following features:
         • Master or Slave Operation
         • Can be used with DMA
         • Philips I2C Compatible
         • SMBus Compatible
         • PMBus™ Compatible
         • Support of 100 kHz and 400 kHz, 1 MHz and 3.4 MHz I2C mode
         • 32-bit Data Extension for better system bus utilization
         • 4-Wire Operation Supported
         • Physical nterface includes:
            – Slew-rate limited outputs
            – Filtered inputs
         • Slave Operation:
            – Operation in all Sleep modes
            – Wake-up on address match
            – 7-bit and 10-bit Address match in hardware for:
            – • Unique address and/or 7-bit general call address
                  • Address range
                  • Two unique addresses can be used with DMA
       Related Links
       33.2 Features




       © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1005
                                                                     SAM D5x/E5x Family Data Sheet
                                                                            SERCOM I2C – Inter-Integrated Circuit


36.3     Block Diagram
         Figure 36-1. I2C Single-Master Single-Slave Interconnection
                                                           Master          Slave
         BAUD                           TxDATA                                                      TxDATA               ADDR/ADDRMASK
                                                                    SCL
                                                       0                           0
                             SCL hold low
   baud rate generator                                                             SCL hold low



                                      shift register                                              shift register
                                                                    SDA
                                                       0                           0




                                        RxDATA                                                      RxDATA                      ==




36.4     Signal Description
          Signal Name                        Type                    Description
          PAD[0]                             Digital I/O             SDA
          PAD[1]                             Digital I/O             SCL
          PAD[2]                             Digital I/O             SDA_OUT (4-wire operation)
          PAD[3]                             Digital I/O             SCL_OUT (4-wire operation)

         One signal can be mapped on several pins.
         Not all the pins are I2C pins. Refer to SERCOM I2C Configurations table for additional information.
         Related Links
         6. I/O Multiplexing and Considerations
         6.2.6 SERCOM I2C Configurations
         36.6.3.3 4-Wire Mode



36.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

36.5.1   I/O Lines
         In order to use the I/O lines of this peripheral, the I/O pins must be configured using the I/O Pin Controller
         (PORT).
         When the SERCOM is used in I2C mode, the SERCOM controls the direction and value of the I/O pins. In
         I2C mode pull-up resistors are disabled. External pull-up resistors are required for proper function.
         Related Links
         32. PORT - I/O Pin Controller




         © 2019 Microchip Technology Inc.                             Datasheet                                DS60001507E-page 1006
                                                             SAM D5x/E5x Family Data Sheet
                                                                     SERCOM I2C – Inter-Integrated Circuit

36.5.2   Power Management
         This peripheral can continue to operate in any Sleep mode where its source clock is running. The
         interrupts can wake-up the device from Sleep modes.
         Related Links
         18. PM – Power Manager

36.5.3   Clocks
         The SERCOM bus clock (CLK_SERCOMx_APB) can be enabled and disabled in the Main Clock
         Controller. Refer to Peripheral Clock Masking for details and default status of this clock.
         Two generic clocks are used by SERCOM, GCLK_SERCOMx_CORE and GCLK_SERCOM_SLOW. The
         core clock (GCLK_SERCOMx_CORE) can clock the I2C when working as a master. The slow clock
         (GCLK_SERCOM_SLOW) is required only for certain functions, e.g. SMBus timing. These two clocks
         must be configured and enabled in the Generic Clock Controller (GCLK) before using the I2C.
         These generic clocks are asynchronous to the bus clock (CLK_SERCOMx_APB). Due to this
         asynchronicity, writes to certain registers will require synchronization between the clock domains. Refer to
         36.6.6 Synchronization for further details.
         Related Links
         14. GCLK - Generic Clock Controller
         15.6.2.6 Peripheral Clock Masking
         18. PM – Power Manager

36.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). In order to use DMA requests with
         this peripheral the DMAC must be configured first. Refer to DMAC – Direct Memory Access Controller for
         details.
         Related Links
         22. DMAC – Direct Memory Access Controller

36.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first. Refer to Nested Vector Interrupt
         Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

36.5.6   Events
         Not applicable.

36.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will continue normal operation. If the peripheral is
         configured to require periodical service by the CPU through interrupts or similar, improper operation or
         data loss may result during debugging. This peripheral can be forced to halt operation during debugging -
         refer to the Debug Control (DBGCTRL) register for details.

36.5.8   Register Access Protection
         Registers with write access can be write-protected optionally by the Peripheral Access Controller (PAC).




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1007
                                                             SAM D5x/E5x Family Data Sheet
                                                                     SERCOM I2C – Inter-Integrated Circuit

         PAC write protection is not available for the following registers:
           •   Interrupt Flag Clear and Status register (INTFLAG)
           •   Status register (STATUS)
           •   Data register (DATA)
           •   Address register (ADDR)
         Optional PAC write protection is denoted by the "PAC Write-Protection" property in each individual
         register description.
         Write-protection does not apply to accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller

36.5.9   Analog Connections
         Not applicable.



36.6     Functional Description

36.6.1   Principle of Operation
         The I2C interface uses two physical lines for communication:
          • Serial Data Line (SDA) for data transfer
          • Serial Clock Line (SCL) for the bus clock
         A transaction starts with the I2C master sending the Start condition, followed by a 7-bit address and a
         direction bit (read or write to/from the slave).
         The addressed I2C slave will then Acknowledge (ACK) the address, and data packet transactions can
         begin. Every 9-bit data packet consists of 8 data bits followed by a one-bit reply indicating whether the
         data was acknowledged or not.
         If a data packet is Not Acknowledged (NACK), whether by the I2C slave or master, the I2C master takes
         action by either terminating the transaction by sending the Stop condition, or by sending a repeated start
         to transfer more data.
         The figure below illustrates the possible transaction formats and Transaction Diagram Symbols explains
         the transaction symbols. These symbols will be used in the following descriptions.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1008
                                                                       SAM D5x/E5x Family Data Sheet
                                                                               SERCOM I2C – Inter-Integrated Circuit

          Figure 36-2. Transaction Diagram Symbols
                          Bus Driver                                                 Special Bus Conditions

                                     Master driving bus                              S         START condition



                                     Slave driving bus                               Sr        repeated START condition



                                     Either Master or Slave driving bus              P         STOP condition



                          Data Package Direction                                     Acknowledge


                              R       Master Read                                    A         Acknowledge (ACK)

                              '1'                                                    '0'

                              W       Master Write                                   A         Not Acknowledge (NACK)

                              '0'                                                    '1'
          Figure 36-3. Basic I2C Transaction Diagram

           SDA

           SCL
                                      6..0                                  7..0                       7..0

                      S             ADDRESS       R/W          ACK        DATA             ACK        DATA       ACK/NACK       P




                          S          ADDRESS         R/W   A            DATA               A          DATA            A/A   P

                                                           Direction

                                         Address Packet                Data Packet #0                Data Packet #1
                                                                       Transaction


36.6.2    Basic Operation

36.6.2.1 Initialization
          The following registers are enable-protected, meaning they can be written only when the I2C interface is
          disabled (CTRLA.ENABLE is ‘0’):
            • Control A register (CTRLA), except Enable (CTRLA.ENABLE) and Software Reset (CTRLA.SWRST)
              bits
            • Control B register (CTRLB), except Acknowledge Action (CTRLB.ACKACT) and Command
              (CTRLB.CMD) bits
            • Baud register (BAUD)
            • Address register (ADDR) in slave operation.
          When the I2C is enabled or is being enabled (CTRLA.ENABLE=1), writing to these registers will be
          discarded. If the I2C is being disabled, writing to these registers will be completed after the disabling.




         © 2019 Microchip Technology Inc.                               Datasheet                                DS60001507E-page 1009
                                                           SAM D5x/E5x Family Data Sheet
                                                                   SERCOM I2C – Inter-Integrated Circuit

         Enable-protection is denoted by the "Enable-Protection" property in the register description.
         Before the I2C is enabled it must be configured as outlined by the following steps:
          1. Select I2C Master or Slave mode by writing 0x4 (Slave mode) or 0x5 (Master mode) to the
               Operating Mode bits in the CTRLA register (CTRLA.MODE).
          2. If desired, select the SDA Hold Time value in the CTRLA register (CTRLA.SDAHOLD).
          3. In Slave mode, the minimum slave setup time for the SDA can be selected in the SDA Setup Time
               bit group in the Control C register (CTRLC.SDASETUP).
          4. If desired, enable smart operation by setting the Smart Mode Enable bit in the CTRLB register
               (CTRLB.SMEN).
          5. If desired, enable SCL low time-out by setting the SCL Low Time-Out bit in the Control A register
               (CTRLA.LOWTOUT).
          6. In Master mode:
               6.1.     Select the inactive bus time-out in the Inactive Time-Out bit group in the CTRLA register
                        (CTRLA.INACTOUT).
               6.2.     Write the Baud Rate register (BAUD) to generate the desired baud rate.
               In Slave mode:
               6.1.    Configure the address match configuration by writing the Address Mode value in the
                       CTRLB register (CTRLB.AMODE).
               6.2.    Set the Address and Address Mask value in the Address register (ADDR.ADDR and
                       ADDR.ADDRMASK) according to the address configuration.
36.6.2.2 Enabling, Disabling, and Resetting
         This peripheral is enabled by writing '1' to the Enable bit in the Control A register (CTRLA.ENABLE), and
         disabled by writing '0' to it.
         Writing ‘1’ to the Software Reset bit in the Control A register (CTRLA.SWRST) will reset all registers of
         this peripheral to their initial states, except the DBGCTRL register, and the peripheral is disabled.
36.6.2.3 I2C Bus State Logic
         The Bus state logic includes several logic blocks that continuously monitor the activity on the I2C bus
         lines in all Sleep modes with running GCLK_SERCOM_x clocks. The start and stop detectors and the bit
         counter are all essential in the process of determining the current Bus state. The Bus state is determined
         according to Bus State Diagram. Software can get the current Bus state by reading the Master Bus State
         bits in the Status register (STATUS.BUSSTATE). The value of STATUS.BUSSTATE in the figure is shown
         in binary.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1010
                                                     SAM D5x/E5x Family Data Sheet
                                                           SERCOM I2C – Inter-Integrated Circuit

Figure 36-4. Bus State Diagram

                                     RESET
                                              UNKNOWN
                                                (0b00)

                         Timeout or Stop Condition


                                             Start Condition
                        IDLE                                                  BUSY
                        (0b01)          Timeout or Stop Condition             (0b11)




                                                                                       Start Condition
                                                                                       Repeated
                                      Stop Condition


                    Write ADDR to generate
                                                           Lost Arbitration
                    Start Condition             OWNER
                                                 (0b10)

                                                       Write ADDR to generate
                                                       Repeated Start Condition
The Bus state machine is active when the I2C master is enabled.
After the I2C master has been enabled, the Bus state is UNKNOWN (0b00). From the UNKNOWN state,
the bus will transition to IDLE (0b01) by either:
  • Forcing by writing 0b01 to STATUS.BUSSTATE
  • A Stop condition is detected on the bus
  • If the inactive bus time-out is configured for SMBus compatibility (CTRLA.INACTOUT) and a time-out
     occurs.
Note: Once a known Bus state is established, the Bus state logic will not re-enter the UNKNOWN state.
When the bus is IDLE it is ready for a new transaction. If a Start condition is issued on the bus by another
I2C master in a multi-master setup, the bus becomes BUSY (0b11). The bus will re-enter IDLE either
when a Stop condition is detected, or when a time-out occurs (inactive bus time-out needs to be
configured).
If a Start condition is generated internally by writing the Address bit group in the Address register
(ADDR.ADDR) while IDLE, the OWNER state (0b10) is entered. If the complete transaction was
performed without interference, i.e., arbitration was not lost, the I2C master can issue a Stop condition,
which will change the Bus state back to IDLE.
However, if a packet collision is detected while in OWNER state, the arbitration is assumed lost and the
Bus state becomes BUSY until a Stop condition is detected. A repeated Start condition will change the
Bus state only if arbitration is lost while issuing a repeated start.
Note: Violating the protocol may cause the I2C to hang. If this happens it is possible to recover from this
state by a software Reset (CTRLA.SWRST='1').
Related Links
36.10.1 CTRLA




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1011
                                                                     SAM D5x/E5x Family Data Sheet
                                                                          SERCOM I2C – Inter-Integrated Circuit

36.6.2.4 I2C Master Operation
            The I2C master is byte-oriented and interrupt based. The number of interrupts generated is kept at a
            minimum by automatic handling of most incidents. The software driver complexity and code size are
            reduced by auto-triggering of operations, and a Special Smart mode, which can be enabled by the Smart
            Mode Enable bit in the Control A register (CTRLA.SMEN).
            The I2C master has two interrupt strategies.
            When SCL Stretch Mode (CTRLA.SCLSM) is '0', SCL is stretched before or after the Acknowledge bit . In
            this mode the I2C master operates according to Master Behavioral Diagram (SCLSM=0). The circles
            labeled "Mn" (M1, M2..) indicate the nodes the bus logic can jump to, based on software or hardware
            interaction.
            This diagram is used as reference for the description of the I2C master operation throughout the
            document.
            Figure 36-5. I2C Master Behavioral Diagram (SCLSM=0)
    APPLICATION                                                                    Master Bus INTERRUPT + SCL HOLD


       M1                M2                 M3                                M4

                BUSY      P        IDLE     S              ADDRESS    R/W BUSY     SW           BUSY               M1

                   Wait for
  SW                                                                  R/W A        SW           P    IDLE          M2
                    IDLE


                                                                      W   A        SW           Sr                 M3          BUSY   M4


                                                                                   SW                       DATA               A/A




                                                                                   Slave Bus INTERRUPT + SCL HOLD



              SW     Software interaction                                          SW      A    BUSY               M4

                     The master provides data on the bus                                  A/A   P    IDLE          M2

                    Addressed slave provides data on the bus
                                                                                          A/A Sr                   M3

                                                                                          A/A


                                                                      R   A                                             DATA


            In the second strategy (CTRLA.SCLSM=1), interrupts only occur after the ACK bit, as in Master
            Behavioral Diagram (SCLSM=1). This strategy can be used when it is not necessary to check DATA
            before acknowledging.
            Note: I2C High-speed (Hs) mode requires CTRLA.SCLSM=1.




        © 2019 Microchip Technology Inc.                             Datasheet                              DS60001507E-page 1012
                                                                 SAM D5x/E5x Family Data Sheet
                                                                       SERCOM I2C – Inter-Integrated Circuit

           Figure 36-6. I2C Master Behavioral Diagram (SCLSM=1)
       APPLICATION                                                             Master Bus INTERRUPT + SCL HOLD


           M1             M2                M3                            M4

                   BUSY    P        IDLE    S          ADDRESS    R/W BUSY     SW           BUSY               M1

                     Wait for
      SW                                                          R/W A        SW           P    IDLE          M2
                      IDLE

                                                                  W   A        SW           Sr                 M3         BUSY   M4


                                                                               SW                       DATA              A/A




                                                                               Slave Bus INTERRUPT + SCL HOLD


              SW     Software interaction
                                                                               SW      BUSY             M4
                    The master provides data on the bus
                                                                                        P   IDLE        M2
                    Addressed slave provides data on the bus
                                                                                       Sr               M3




                                                                  R   A                             DATA            A/A


36.6.2.4.1 Master Clock Generation
           The SERCOM peripheral supports several I2C bidirectional modes:
            • Standard mode (Sm) up to 100 kHz
            • Fast mode (Fm) up to 400 kHz
            • Fast mode Plus (Fm+) up to 1 MHz
            • High-speed mode (Hs) up to 3.4 MHz
           The Master clock configuration for Sm, Fm, and Fm+ are described in Clock Generation (Standard-Mode,
           Fast-Mode, and Fast-Mode Plus). For Hs, refer to Master Clock Generation (High-Speed Mode).
           Clock Generation (Standard-Mode, Fast-Mode, and Fast-Mode Plus)
           In I2C Sm, Fm, and Fm+ mode, the Master clock (SCL) frequency is determined as described in this
           section:
           The low (TLOW) and high (THIGH) times are determined by the Baud Rate register (BAUD), while the rise
           (TRISE) and fall (TFALL) times are determined by the bus topology. Because of the wired-AND logic of the
           bus, TFALL will be considered as part of TLOW. Likewise, TRISE will be in a state between TLOW and THIGH
           until a high state has been detected.




           © 2019 Microchip Technology Inc.                      Datasheet                               DS60001507E-page 1013
                                                            SAM D5x/E5x Family Data Sheet
                                                                      SERCOM I2C – Inter-Integrated Circuit

Figure 36-7. SCL Timing
                                                              TRISE
                   P          S              TLOW                                                 Sr


SCL
                                                            THIGH
                       TBUF                         TFALL



SDA



         TSU;STO                   THD;STA                                              TSU;STA
The following parameters are timed using the SCL low time period TLOW. This comes from the Master
Baud Rate Low bit group in the Baud Rate register (BAUD.BAUDLOW). When BAUD.BAUDLOW=0, or
the Master Baud Rate bit group in the Baud Rate register (BAUD.BAUD) determines it.
  • TLOW – Low period of SCL clock
  • TSU;STO – Set-up time for stop condition
  •   TBUF – Bus free time between stop and start conditions
  •   THD;STA – Hold time (repeated) start condition
  •   TSU;STA – Set-up time for repeated start condition
  •   THIGH is timed using the SCL high time count from BAUD.BAUD
  •   TRISE is determined by the bus impedance; for internal pull-ups.
  •   TFALL is determined by the open-drain current limit and bus impedance; can typically be regarded as
      zero.
The SCL frequency is given by:
                  1
�SCL =
         �LOW + �HIGH + �RISE

When BAUD.BAUDLOW is zero, the BAUD.BAUD value is used to time both SCL high and SCL low. In
this case the following formula will give the SCL frequency:
                  �GCLK
�SCL =
         10 + 2���� + �GCLK ⋅ �RISE

When BAUD.BAUDLOW is non-zero, the following formula determines the SCL frequency:
                       �GCLK
�SCL =
         10 + ���� + ������� + �GCLK ⋅ �RISE

The following formulas can determine the SCL TLOW and THIGH times:
          ������� + 5
�LOW =
             �GCLK

          ���� + 5
�HIGH =
            �GCLK




© 2019 Microchip Technology Inc.                            Datasheet                       DS60001507E-page 1014
                                                             SAM D5x/E5x Family Data Sheet
                                                                     SERCOM I2C – Inter-Integrated Circuit

         Note: The I2C standard Fm+ (Fast-mode plus) requires a nominal high to low SCL ratio of 1:2, and
         BAUD should be set accordingly. At a minimum, BAUD.BAUD and/or BAUD.BAUDLOW must be non-
         zero.
         Startup Timing The minimum time between SDA transition and SCL rising edge is 6 APB cycles when
         the DATA register is written in smart mode. If a greater startup time is required due to long rise times, the
         time between DATA write and IF clear must be controlled by software.
         Note: When timing is controlled by user, the Smart Mode cannot be enabled.
         Master Clock Generation (High-Speed Mode)
         For I2C Hs transfers, there is no SCL synchronization. Instead, the SCL frequency is determined by the
         GCLK_SERCOMx_CORE frequency (fGCLK) and the High-Speed Baud setting in the Baud register
         (BAUD.HSBAUD). When BAUD.HSBAUDLOW=0, the HSBAUD value will determine both SCL high and
         SCL low. In this case the following formula determines the SCL frequency.
                       �GCLK
         �SCL =
                  2 + 2 ⋅ �� ����
         When HSBAUDLOW is non-zero, the following formula determines the SCL frequency.
                            �GCLK
         �SCL =
                  2 + �� ���� + ���������
         Note: The I2C standard Hs (High-speed) requires a nominal high to low SCL ratio of 1:2, and HSBAUD
         should be set accordingly. At a minimum, BAUD.HSBAUD and/or BAUD.HSBAUDLOW must be non-
         zero.
36.6.2.4.2 Transmitting Address Packets
         The I2C master starts a bus transaction by writing the I2C slave address to ADDR.ADDR and the direction
         bit, as described in 36.6.1 Principle of Operation. If the bus is busy, the I2C master will wait until the bus
         becomes idle before continuing the operation. When the bus is idle, the I2C master will issue a start
         condition on the bus. The I2C master will then transmit an address packet using the address written to
         ADDR.ADDR. After the address packet has been transmitted by the I2C master, one of four cases will
         arise according to arbitration and transfer direction.
         Case 1: Arbitration lost or bus error during address packet transmission
         If arbitration was lost during transmission of the address packet, the Master on Bus bit in the Interrupt
         Flag Status and Clear register (INTFLAG.MB) and the Arbitration Lost bit in the Status register
         (STATUS.ARBLOST) are both set. Serial data output to SDA is disabled, and the SCL is released, which
         disables clock stretching. In effect the I2C master is no longer allowed to execute any operation on the
         bus until the bus is idle again. A bus error will behave similarly to the Arbitration Lost condition. In this
         case, the MB Interrupt flag and Master Bus Error bit in the Status register (STATUS.BUSERR) are both
         set in addition to STATUS.ARBLOST.
         The Master Received Not Acknowledge bit in the Status register (STATUS.RXNACK) will always contain
         the last successfully received acknowledge or not acknowledge indication.
         In this case, software will typically inform the application code of the condition and then clear the Interrupt
         flag before exiting the interrupt routine. No other flags have to be cleared at this moment, because all
         flags will be cleared automatically the next time the ADDR.ADDR register is written.
         Case 2: Address packet transmit complete – No ACK received
         If there is no I2C slave device responding to the address packet, then the INTFLAG.MB Interrupt flag and
         STATUS.RXNACK will be set. The clock hold is active at this point, preventing further activity on the bus.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1015
                                                           SAM D5x/E5x Family Data Sheet
                                                                   SERCOM I2C – Inter-Integrated Circuit

         The missing ACK response can indicate that the I2C slave is busy with other tasks or sleeping. Therefore,
         it is not able to respond. In this event, the next step can be either issuing a Stop condition
         (recommended) or resending the address packet by a repeated Start condition. When using SMBus logic,
         the slave must ACK the address. If there is no response, it means that the slave is not available on the
         bus.
         Case 3: Address packet transmit complete – Write packet, Master on Bus set
         If the I2C master receives an acknowledge response from the I2C slave, INTFLAG.MB will be set and
         STATUS.RXNACK will be cleared. The clock hold is active at this point, preventing further activity on the
         bus.
         In this case, the software implementation becomes highly protocol dependent. Three possible actions can
         enable the I2C operation to continue:
           • Initiate a data transmit operation by writing the data byte to be transmitted into DATA.DATA.
           • Transmit a new address packet by writing ADDR.ADDR. A repeated Start condition will automatically
              be inserted before the address packet.
           • Issue a Stop condition, consequently terminating the transaction.
         Case 4: Address packet transmit complete – Read packet, Slave on Bus set
         If the I2C master receives an ACK from the I2C slave, the I2C master proceeds to receive the next byte of
         data from the I2C slave. When the first data byte is received, the Slave on Bus bit in the Interrupt Flag
         register (INTFLAG.SB) will be set and STATUS.RXNACK will be cleared. The clock hold is active at this
         point, preventing further activity on the bus.
         In this case, the software implementation becomes highly protocol dependent. Three possible actions can
         enable the I2C operation to continue:
           • Let the I2C master continue to read data by acknowledging the data received. ACK can be sent by
              software, or automatically in Smart mode.
           • Transmit a new address packet.
           • Terminate the transaction by issuing a Stop condition.
         Note: An ACK or NACK will be automatically transmitted if Smart mode is enabled. The Acknowledge
         Action bit in the Control B register (CTRLB.ACKACT) determines whether ACK or NACK should be sent.
36.6.2.4.3 Transmitting Data Packets
         When an address packet with direction Master Write (see Figure 36-3) was transmitted successfully ,
         INTFLAG.MB will be set. The I2C master will start transmitting data via the I2C bus by writing to
         DATA.DATA, and monitor continuously for packet collisions.
         If a collision is detected, the I2C master will lose arbitration and STATUS.ARBLOST will be set. If the
         transmit was successful, the I2C master will receive an ACK bit from the I2C slave, and
         STATUS.RXNACK will be cleared. INTFLAG.MB will be set in both cases, regardless of arbitration
         outcome.
         It is recommended to read STATUS.ARBLOST and handle the arbitration lost condition in the beginning
         of the I2C Master on Bus interrupt. This can be done as there is no difference between handling address
         and data packet arbitration.
         STATUS.RXNACK must be checked for each data packet transmitted before the next data packet
         transmission can commence. The I2C master is not allowed to continue transmitting data packets if a
         NACK is received from the I2C slave.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1016
                                                             SAM D5x/E5x Family Data Sheet
                                                                     SERCOM I2C – Inter-Integrated Circuit

36.6.2.4.4 Receiving Data Packets (SCLSM=0)
         When INTFLAG.SB is set, the I2C master will already have received one data packet. The I2C master
         must respond by sending either an ACK or NACK. Sending a NACK may be unsuccessful when
         arbitration is lost during the transmission. In this case, a lost arbitration will prevent setting INTFLAG.SB.
         Instead, INTFLAG.MB will indicate a change in arbitration. Handling of lost arbitration is the same as for
         data bit transmission.
36.6.2.4.5 Receiving Data Packets (SCLSM=1)
         When INTFLAG.SB is set, the I2C master will already have received one data packet and transmitted an
         ACK or NACK, depending on CTRLB.ACKACT. At this point, CTRLB.ACKACT must be set to the correct
         value for the next ACK bit, and the transaction can continue by reading DATA and issuing a command if
         not in the Smart mode.
36.6.2.4.6 High-Speed Mode
         High-speed transfers are a multi-step process, see High Speed Transfer.
         First, a master code (0b00001nnn, where 'nnn' is a unique master code) is transmitted in Full-speed
         mode, followed by a NACK since no slaveshould acknowledge. Arbitration is performed only during the
         Full-speed Master Code phase. The master code is transmitted by writing the master code to the Address
         register (ADDR.ADDR) and writing the High-speed bit (ADDR.HS) to '0'.
         After the master code and NACK have been transmitted, the master write interrupt will be asserted. In the
         meanwhile, the slave address can be written to the ADDR.ADDR register together with ADDR.HS=1.
         Now in High-speed mode, the master will generate a repeated start, followed by the slave address with
         RW-direction. The bus will remain in High-speed mode until a stop is generated. If a repeated start is
         desired, the ADDR.HS bit must again be written to '1', along with the new address ADDR.ADDR to be
         transmitted.
         Figure 36-8. High Speed Transfer
                     F/S-mode                                  Hs-mode                                       F/S-mode

            S      Master Code       A      Sr   ADDRESS     R/W A            DATA           A/A   P

                                                                            N Data Packets              Hs-mode continues

                                                                                                   Sr     ADDRESS

         Transmitting in High-speed mode requires the I2C master to be configured in High-speed mode
         (CTRLA.SPEED=0x2) and the SCL Clock Stretch mode (CTRLA.SCLSM) bit set to '1'.
36.6.2.4.7 10-Bit Addressing
         When 10-bit addressing is enabled by the Ten Bit Addressing Enable bit in the Address register
         (ADDR.TENBITEN=1) and the Address bit field ADDR.ADDR is written, the two address bytes will be
         transmitted, see 10-bit Address Transmission for a Read Transaction. The addressed slave
         acknowledges the two address bytes, and the transaction continues. Regardless of whether the
         transaction is a read or write, the master must start by sending the 10-bit address with the direction bit
         (ADDR.ADDR[0]) being zero.
         If the master receives a NACK after the first byte, the Write Interrupt flag will be raised and the
         STATUS.RXNACK bit will be set. If the first byte is acknowledged by one or more slaves, then the master
         will proceed to transmit the second address byte and the master will first see the Write Interrupt flag after
         the second byte is transmitted. If the transaction direction is read-from-slave, the 10-bit address
         transmission must be followed by a repeated start and the first 7 bits of the address with the read/write bit
         equal to '1'.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 1017
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                SERCOM I2C – Inter-Integrated Circuit

         Figure 36-9. 10-bit Address Transmission for a Read Transaction
                                                                            MB INTERRUPT

                                                                                                                          1
                                                                                      S
                S 11110 addr[9:8]          W       A       addr[7:0]        A                    Sr 11110 addr[9:8]       R        A
                                                                                      W
         This implies the following procedure for a 10-bit read operation:
          1. Write the 10-bit address to ADDR.ADDR[10:1]. ADDR.TENBITEN must be '1', the direction bit
               (ADDR.ADDR[0]) must be '0' (can be written simultaneously with ADDR).
          2. Once the Master on Bus interrupt is asserted, Write ADDR[7:0] register to '11110 address[9:8]
               1'. ADDR.TENBITEN must be cleared (can be written simultaneously with ADDR).
          3. Proceed to transmit data.
36.6.2.5 I2C Slave Operation
         The I2C slave is byte-oriented and interrupt-based. The number of interrupts generated is kept at a
         minimum by automatic handling of most events. The software driver complexity and code size are
         reduced by auto-triggering of operations, and a special smart mode, which can be enabled by the Smart
         Mode Enable bit in the Control A register (CTRLA.SMEN).
         The I2C slave has two interrupt strategies.
         When SCL Stretch Mode bit (CTRLA.SCLSM) is '0', SCL is stretched before or after the acknowledge bit.
         In this mode, the I2C slave operates according to I2C Slave Behavioral Diagram (SCLSM=0). The circles
         labelled "Sn" (S1, S2..) indicate the nodes the bus logic can jump to, based on software or hardware
         interaction.
         This diagram is used as reference for the description of the I2C slave operation throughout the document.
         Figure 36-10. I2C Slave Behavioral Diagram (SCLSM=0)
                                           AMATCH INTERRUPT                                        DRDY INTERRUPT


                                                                                                                    P         S2


  S1      S3                                                    A      S1                                           Sr        S3

                                                       S                                                   S
  S2       S                ADDRESS            R
                                                       W
                                                                A
                                                                                                           W
                                                                                                                              DATA     A/A


                                                                                 P    S2

                                                                A      S1        Sr   S3
               PREC INTERRUPT
                                                       S                                                   S
                                             W                  A                         DATA                      A/A
                                                       W                                                   W

        Interrupt on STOP         S
        Condition Enabled         W




         S
               Software interaction
         W

               The master provides data
               on the bus

               Addressed slave provides
               data on the bus




        © 2019 Microchip Technology Inc.                               Datasheet                               DS60001507E-page 1018
                                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            SERCOM I2C – Inter-Integrated Circuit

         In the second strategy (CTRLA.SCLSM=1), interrupts only occur after the ACK bit is sent as shown in
         Slave Behavioral Diagram (SCLSM=1). This strategy can be used when it is not necessary to check
         DATA before acknowledging. For master reads, an address and data interrupt will be issued
         simultaneously after the address acknowledge. However, for master writes, the first data interrupt will be
         seen after the first data byte has been received by the slave and the acknowledge bit has been sent to
         the master.
         Note: For I2C High-speed mode (Hs), SCLSM=1 is required.
         Figure 36-11. I2C Slave Behavioral Diagram (SCLSM=1)
                                              AMATCH INTERRUPT (+ DRDY INTERRUPT in Master Read mode)          DRDY INTERRUPT


                                                                                                                            P        S2


         S1       S3                                                                                                        Sr       S3

                                                                   S
         S2        S                ADDRESS             R   A/A
                                                                   W
                                                                                                                                     DATA       A/A


                                                                                              P         S2

                                                                                             Sr         S3
                        PREC INTERRUPT
                                                                   S                                                   S
                                                        W   A/A                                         DATA    A/A
                                                                   W                                                   W

                Interrupt on STOP         S
                Condition Enabled         W




                 S
                       Software interaction
                 W

                       The master provides data
                       on the bus

                       Addressed slave provides
                       data on the bus



36.6.2.5.1 Receiving Address Packets (SCLSM=0)
         When CTRLA.SCLSM=0, the I2C slave stretches the SCL line according to Figure 36-10. When the I2C
         slave is properly configured, it will wait for a Start condition.
         When a Start condition is detected, the successive address packet will be received and checked by the
         address match logic. If the received address is not a match, the packet will be rejected, and the I2C slave
         will wait for a new Start condition. If the received address is a match, the Address Match bit in the
         Interrupt Flag register (INTFLAG.AMATCH) will be set.
         SCL will be stretched until the I2C slave clears INTFLAG.AMATCH. As the I2C slave holds the clock by
         forcing SCL low, the software has unlimited time to respond.
         The direction of a transaction is determined by reading the Read/Write Direction bit in the Status register
         (STATUS.DIR). This bit will be updated only when a valid address packet is received.
         If the Transmit Collision bit in the Status register (STATUS.COLL) is set, this indicates that the last packet
         addressed to the I2C slave had a packet collision. A collision causes the SDA and SCL lines to be
         released without any notification to software. Therefore, the next AMATCH interrupt is the first indication
         of the previous packet’s collision. Collisions are intended to follow the SMBus Address Resolution
         Protocol (ARP).
         After the address packet has been received from the I2C master, one of two cases will arise based on
         transfer direction.




        © 2019 Microchip Technology Inc.                                           Datasheet                                    DS60001507E-page 1019
                                                            SAM D5x/E5x Family Data Sheet
                                                                    SERCOM I2C – Inter-Integrated Circuit

         Case 1: Address packet accepted – Read flag set
         The STATUS.DIR bit is ‘1’, indicating an I2C master read operation. The SCL line is forced low, stretching
         the bus clock. If an ACK is sent, I2C slave hardware will set the Data Ready bit in the Interrupt Flag
         register (INTFLAG.DRDY), indicating data are needed for transmit. If a NACK is sent, the I2C slave will
         wait for a new Start condition and address match.
         Typically, software will immediately acknowledge the address packet by sending an ACK/NACK bit. The
         I2C slave Command bit field in the Control B register (CTRLB.CMD) can be written to '0x3' for both read
         and write operations as the command execution is dependent on the STATUS.DIR bit. Writing ‘1’ to
         INTFLAG.AMATCH will also cause an ACK/NACK to be sent corresponding to the CTRLB.ACKACT bit.
         Case 2: Address packet accepted – Write flag set
         The STATUS.DIR bit is cleared, indicating an I2C master write operation. The SCL line is forced low,
         stretching the bus clock. If an ACK is sent, the I2C slave will wait for data to be received. Data, repeated
         start or stop can be received.
         If a NACK is sent, the I2C slave will wait for a new Start condition and address match. Typically, software
         will immediately acknowledge the address packet by sending an ACK/NACK. The I2C slave command
         CTRLB.CMD = 3 can be used for both read and write operation as the command execution is dependent
         on STATUS.DIR.
         Writing ‘1’ to INTFLAG.AMATCH will also cause an ACK/NACK to be sent corresponding to the
         CTRLB.ACKACT bit.
36.6.2.5.2 Receiving Address Packets (SCLSM=1)
         When SCLSM=1, the I2C slave will stretch the SCL line only after an ACK, see Slave Behavioral Diagram
         (SCLSM=1). When the I2C slave is properly configured, it will wait for a Start condition to be detected.
         When a Start condition is detected, the successive address packet will be received and checked by the
         address match logic.
         If the received address is not a match, the packet will be rejected and the I2C slave will wait for a new
         Start condition.
         If the address matches, the acknowledge action as configured by the Acknowledge Action bit Control B
         register (CTRLB.ACKACT) will be sent and the Address Match bit in the Interrupt Flag register
         (INTFLAG.AMATCH) is set. SCL will be stretched until the I2C slave clears INTFLAG.AMATCH. As the
         I2C slave holds the clock by forcing SCL low, the software is given unlimited time to respond to the
         address.
         The direction of a transaction is determined by reading the Read/Write Direction bit in the Status register
         (STATUS.DIR). This bit will be updated only when a valid address packet is received.
         If the Transmit Collision bit in the Status register (STATUS.COLL) is set, the last packet addressed to the
         I2C slave had a packet collision. A collision causes the SDA and SCL lines to be released without any
         notification to software. The next AMATCH interrupt is, therefore, the first indication of the previous
         packet’s collision. Collisions are intended to follow the SMBus Address Resolution Protocol (ARP).
         After the address packet has been received from the I2C master, INTFLAG.AMATCH be set to ‘1’ to clear
         it.
36.6.2.5.3 Receiving and Transmitting Data Packets
         After the I2C slave has received an address packet, it will respond according to the direction either by
         waiting for the data packet to be received or by starting to send a data packet by writing to DATA.DATA.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1020
                                                                SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit

         When a data packet is received or sent, INTFLAG.DRDY will be set. After receiving data, the I2C slave
         will send an acknowledge according to CTRLB.ACKACT.
         Case 1: Data received
         INTFLAG.DRDY is set, and SCL is held low, pending for SW interaction.
         Case 2: Data sent
         When a byte transmission is successfully completed, the INTFLAG.DRDY Interrupt flag is set. If NACK is
         received, indicated by STATUS.RXNACK=1, the I2C slave must expect a stop or a repeated start to be
         received. The I2C slave must release the data line to allow the I2C master to generate a stop or repeated
         start. Upon detecting a Stop condition, the Stop Received bit in the Interrupt Flag register
         (INTFLAG.PREC) will be set and the I2C slave will return to IDLE state.
36.6.2.5.4 High-Speed Mode
         When the I2C slave is configured in High-speed mode (Hs, CTRLA.SPEED=0x2) and CTRLA.SCLSM=1,
         switching between Full-speed and High-speed modes is automatic. When the slave recognizes a START
         followed by a master code transmission and a NACK, it automatically switches to High-speed mode and
         sets the High-speed status bit (STATUS.HS). The slave will then remain in High-speed mode until a
         STOP is received.
36.6.2.5.5 10-Bit Addressing
         When 10-bit addressing is enabled (ADDR.TENBITEN=1), the two address bytes following a START will
         be checked against the 10-bit slave address recognition. The first byte of the address will always be
         acknowledged, and the second byte will raise the address Interrupt flag, see 10-bit Addressing.
         If the transaction is a write, then the 10-bit address will be followed by N data bytes.
         If the operation is a read, the 10-bit address will be followed by a repeated START and reception of '11110
         ADDR[9:8] 1', and the second address interrupt will be received with the DIR bit set. The slave matches
         on the second address as it was addressed by the previous 10-bit address.
         Figure 36-12. 10-bit Addressing

                                                            AMATCH INTERRUPT                            AMATCH INTERRUPT


                                                                     S                                           S
            S 11110 addr[9:8]       W       A   addr[7:0]                      A   Sr 11110 addr[9:8]     R
                                                                     W                                           W

36.6.2.5.6 PMBus Group Command
         When the PMBus Group Command bit in the CTRLB register is set (CTRLB.GCMD=1) and 7-bit
         addressing is used, INTFLAG.PREC will be set if the slave has been addressed since the last STOP
         condition. When CTRLB.GCMD=0, a STOP condition without address match will not be set
         INTFLAG.PREC.
         The group command protocol is used to send commands to more than one device. The commands are
         sent in one continuous transmission with a single STOP condition at the end. When the STOP condition
         is detected by the slaves addressed during the group command, they all begin executing the command
         they received.
         PMBus Group Command Example shows an example where this slave, bearing ADDRESS 1, is
         addressed after a repeated START condition. There can be multiple slaves addressed before and after
         this slave. Eventually, at the end of the group command, a single STOP is generated by the master. At
         this point a STOP interrupt is asserted.




         © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1021
                                                               SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit

         Figure 36-13. PMBus Group Command Example

                                                           Command/Data


                           S      ADDRESS 0       W    A       n Bytes        A



                                                 AMATCH INTERRUPT                        DRDY INTERRUPT
                                                                          Command/Data

                                  ADDRESS 1                S                                     S
                           Sr                     W                 A      n Bytes                        A
                                  (this slave)             W                                     W



                                                                                     PREC INTERRUPT
                                                           Command/Data

                                                                                             S
                           Sr     ADDRESS 2       W    A       n Bytes        A      P
                                                                                             W


36.6.3   Additional Features

36.6.3.1 SMBus
         The I2C includes three hardware SCL low time-outs, which allow a time-out to occur for SMBus SCL low
         time-out, master extend time-out, and slave extend time-out. This allows for SMBus functionality These
         time-outs are driven by the GCLK_SERCOM_SLOW clock. The GCLK_SERCOM_SLOW clock is used to
         accurately time the time-out and must be configured to use a 32 KHz oscillator. The I2C interface also
         allows for a SMBus compatible SDA hold time.
           • TTIMEOUT: SCL low time of 25..35ms – Measured for a single SCL low period. It is enabled by
             CTRLA.LOWTOUTEN.
           • TLOW:SEXT: Cumulative clock low extend time of 25 ms – Measured as the cumulative SCL low
             extend time by a slave device in a single message from the initial START to the STOP. It is enabled
             by CTRLA.SEXTTOEN.
           • TLOW:MEXT: Cumulative clock low extend time of 10 ms – Measured as the cumulative SCL low
             extend time by the master device within a single byte from START-to-ACK, ACK-to-ACK, or ACK-to-
             STOP. It is enabled by CTRLA.MEXTTOEN.
36.6.3.2 Smart Mode
         The I2C interface has a Smart mode that simplifies application code and minimizes the user interaction
         needed to adhere to the I2C protocol. The Smart mode accomplishes this by automatically issuing an
         ACK or NACK (based on the content of CTRLB.ACKACT) as soon as DATA.DATA is read.

36.6.3.3 4-Wire Mode
         Writing a '1' to the Pin Usage bit in the Control A register (CTRLA.PINOUT) will enable 4-Wire mode
         operation. In this mode, the internal I2C tri-state drivers are bypassed, and an external I2C compliant tri-
         state driver is needed when connecting to an I2C bus.




         © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 1022
                                                                             SAM D5x/E5x Family Data Sheet
                                                                                       SERCOM I2C – Inter-Integrated Circuit

         Figure 36-14. I2C Pad Interface
                                 SCL_OUT/                                                                     SCL_OUT/
                                 SDA_OUT                                                                      SDA_OUT
                                                            PINOUT                                              pad


                                                                                     I2C                         SCL/SDA
                                                                                    Driver                         pad
                                   SCL_IN/
                                   SDA_IN

                                                                      PINOUT


36.6.3.4 Quick Command
         Setting the Quick Command Enable bit in the Control B register (CTRLB.QCEN) enables quick command.
         When quick command is enabled, the corresponding Interrupt flag (INTFLAG.SB or INTFLAG.MB) is set
         immediately after the slave acknowledges the address. At this point, the software can either issue a Stop
         command or a repeated start by writing CTRLB.CMD or ADDR.ADDR.

36.6.3.5 32-bit Extension
         For better system bus utilization, 32-bit data receive and transmit can be enabled by writing to the Data
         32-bit bit field in the Control C register (CTRLC.DATA32B=1). When enabled, write and read transaction
         to/from the DATA register are 32 bit in size.
         If frames are not multiples of 4 Bytes, the Length Counter (LENGTH.LEN) and Length Enable
         (LENGTH.LENEN) must be configured before data transfer begins. LENGTH.LEN must be enabled only
         when CTRLC.DATA32B is enabled.
         The figure below shows the order of transmit and receive when using 32-bit mode. Bytes are transmitted
         or received and stored in order from 0 to 3.
         Figure 36-15. 32-bit Extension Byte Ordering

                                             APB Write/Read          BYTE3     BYTE2         BYTE1   BYTE0
                                             Bit Position       31                                           0



         32-bit Extension Slave Operation
         The figure below shows a transaction with 32-bit Extension enabled (CTRLC.DATA32B=1). In slave
         operation, the Address Match interrupt in the Interrupt Flag Status and Clear register
         (INTFLAG.AMATCH) is set after the address is received and available in the DATA register. The Data
         Ready interrupt (INTFLAG.DRDY) will then be raised for every 4 Bytes transferred.
         Figure 36-16. 32-bit Extension Slave Operation
                                                 SLAVE ADDRESS                                                      SLAVE DATA
                                                 INTERRUPT                                                          INTERRUPT


                                                            S                                                          S
                            S   ADDRESS         W                    A   Byte 0 A    Byte 1 A   Byte 2 A   Byte 3
                                                            W                                                          W

         The LENGTH register can be written before the frame begins, or when the AMATCH interrupt is set. If the
         frame size is not LENGTH.LEN Bytes, the Length Error status bit (STATUS.LENERR) is raised. If
         LENGTH.LEN is not a multiple of 4 Bytes, the final INTFLAG.DRDY interrupt is raised when the last Byte
         is received for master reads. For master writes, the last data byte will be automatically NACKed. On
         address recognition, the internal length counter is reset in preparation for the incoming frame.
         High Speed transactions start with a Full Speed Master Code. When a Master Code is detected, no data
         is received and the next expected operation is a repeated start. For this reason, the length is not counted




        © 2019 Microchip Technology Inc.                                     Datasheet                                     DS60001507E-page 1023
                                                              SAM D5x/E5x Family Data Sheet
                                                                       SERCOM I2C – Inter-Integrated Circuit

         after a Master Code is received. In this case, no Length Error (STATUS.LENERR) is registered,
         regardless of the LENGTH.LENEN setting.
         When SCL clock stretch mode is selected (CTRLA.SCLSM=1) and the transaction is a master write, the
         selected Acknowledge Action (CTRLB.ACKACT) will only be used to ACK/NACK each 4th byte. All other
         bytes are ACKed. This allows the user to write CTRLB.ACKACT=1 in the final interrupt, so that the last
         byte in a 32-bit word will be NACKed.
         Writing to the LENGTH register while a frame is in progress will produce unpredictable results. If
         LENGTH.LENEN is not set and a frame is not a multiple of 4 Bytes, the remainder will be lost.

         32-bit Extension Master Operation
         When using the I2C configured as Master, the Address register must be written with the desired address
         (ADDR.ADDR), and optionally, the transaction Length and transaction Length Enable bits (ADDR.LEN
         and ADDR.LENEN) can be written. When ADDR.LENEN is written to '1' along with ADDR.ADDR,
         ADDR.LEN determines the number of data bytes in the transaction from 0 to 255. Then, the ADDR.LEN
         bytes are transferred, followed by an automatically generated NACK (for master reads) and a STOP.
         The INTFLAG.SB or INTFLAG.MB are raised for every 4 Bytes transferred. If the transaction is a master
         read and ADDR.LEN is not a multiple of 4 Bytes, the final INTFLAG.SB is set when the last byte is
         received.
         When SCL clock stretch mode is enabled (CTRLA.SCLSM=1) and the transaction is a master read, the
         selected Acknowledge Action (CTRLB.ACKACT) will only be used to ACK/NACK each 4th Byte. All other
         bytes are ACKed. This allows the user to set CTRLB.ACKACT=1 in the final interrupt, so that the last byte
         in a 32-bit word will be NACKed.
         If a NACK is received by the slave for a master write transaction before ADDR.LEN bytes, a STOP will be
         automatically generated, and the length error (STATUS.LENERR) is raised along with the
         INTFLAG.ERROR interrupt.

36.6.4   DMA, Interrupts and Events
         Each interrupt source has its own Interrupt flag. The Interrupt flag in the Interrupt Flag Status and Clear
         register (INTFLAG) will be set when the Interrupt condition is meet. Each interrupt can be individually
         enabled by writing ‘1’ to the corresponding bit in the Interrupt Enable Set register (INTENSET), and
         disabled by writing ‘1’ to the corresponding bit in the Interrupt Enable Clear register (INTENCLR). An
         interrupt request is generated when the Interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request is active until the Interrupt flag is cleared, the interrupt is disabled or the I2C is reset.
         See the 36.8.6 INTFLAG (Slave) or 36.10.7 INTFLAG (Master) register for details on how to clear
         Interrupt flags.




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1024
                                                           SAM D5x/E5x Family Data Sheet
                                                                  SERCOM I2C – Inter-Integrated Circuit

         Table 36-1. Module Request for SERCOM I2C Slave

          Condition                          Request
                                             DMA                 Interrupt               Event
          Data needed for transmit (TX)      Yes                                         NA
          (Slave Transmit mode)              (request cleared
                                             when data is
                                             written)

          Data received (RX) (Slave          Yes
          Receive mode)                      (request cleared
                                             when data is
                                             read)

          Data Ready (DRDY)                                      Yes
          Address Match (AMATCH)                                 Yes
          Stop received (PREC)                                   Yes
          Error (ERROR)                                          Yes

         Table 36-2. Module Request for SERCOM I2C Master

          Condition                           Request
                                              DMA                Interrupt                Event
          Data needed for transmit (TX)       Yes                                         NA
          (Master Transmit mode)              (request cleared
                                              when data is
                                              written)

          Data needed for transmit (RX)       Yes
          (Master Transmit mode)              (request cleared
                                              when data is
                                              read)

          Master on Bus (MB)                                     Yes
          Stop received (SB)                                     Yes
          Error (ERROR)                                          Yes

36.6.4.1 DMA Operation
         Smart mode must be enabled for DMA operation in the Control B register by writing CTRLB.SMEN=1.
36.6.4.1.1 Slave DMA
         When using the I2C slave with DMA, an address match will cause the address Interrupt flag
         (INTFLAG.ADDRMATCH) to be raised. After the interrupt has been serviced, data transfer will be
         performed through DMA.
         The I2C slave generates the following requests:
           • Write data received (RX): The request is set when master write data is received. The request is
             cleared when DATA is read.




        © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 1025
                                                              SAM D5x/E5x Family Data Sheet
                                                                       SERCOM I2C – Inter-Integrated Circuit

           • Read data needed for transmit (TX): The request is set when data is needed for a master read
             operation. The request is cleared when DATA is written.
36.6.4.1.2 Master DMA
         When using the I2C master with DMA, the ADDR register must be written with the desired address
         (ADDR.ADDR), transaction length (ADDR.LEN), and transaction length enable (ADDR.LENEN). When
         ADDR.LENEN is written to 1 along with ADDR.ADDR, ADDR.LEN determines the number of data bytes
         in the transaction from 0 to 255. DMA is then used to transfer ADDR.LEN bytes followed by an
         automatically generated NACK (for master reads) and a STOP.
         If a NACK is received by the slave for a master write transaction before ADDR.LEN bytes, a STOP will be
         automatically generated and the length error (STATUS.LENERR) will be raised along with the
         INTFLAG.ERROR interrupt.
         The I2C master generates the following requests:
           • Read data received (RX): The request is set when master read data is received. The request is
             cleared when DATA is read.
           • Write data needed for transmit (TX): The request is set when data is needed for a master write
             operation. The request is cleared when DATA is written.
36.6.4.2 Interrupts
         The I2C slave has the following interrupt sources. These are asynchronous interrupts. They can wake-up
         the device from any Sleep mode:
           •   Error (ERROR)
           •   Data Ready (DRDY)
           •   Address Match (AMATCH)
           •   Stop Received (PREC)
         The I2C master has the following interrupt sources. These are asynchronous interrupts. They can wake-
         up the device from any Sleep mode:
           • Error (ERROR)
           • Slave on Bus (SB)
           • Master on Bus (MB)
         Each interrupt source has its own Interrupt flag. The Interrupt flag in the Interrupt Flag Status and Clear
         register (INTFLAG) will be set when the Interrupt condition is meet. Each interrupt can be individually
         enabled by writing ‘1’ to the corresponding bit in the Interrupt Enable Set register (INTENSET), and
         disabled by writing ‘1’ to the corresponding bit in the Interrupt Enable Clear register (INTENCLR). An
         interrupt request is generated when the Interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request active until the Interrupt flag is cleared, the interrupt is disabled or the I2C is reset.
         See the INTFLAG register for details on how to clear Interrupt flags.
         The value of INTFLAG indicates which interrupt is executed. Note that interrupts must be globally
         enabled for interrupt requests. Refer to Nested Vector Interrupt Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller

36.6.4.3 Events
         Not applicable.




        © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 1026
                                                             SAM D5x/E5x Family Data Sheet
                                                                  SERCOM I2C – Inter-Integrated Circuit

36.6.5   Sleep Mode Operation
         I2C Master Operation
         The generic clock (GCLK_SERCOMx_CORE) will continue to run in idle sleep mode. If the Run In
         Standby bit in the Control A register (CTRLA.RUNSTDBY) is '1', the GLK_SERCOMx_CORE will also run
         in Standby Sleep mode. Any interrupt can wake-up the device.
         If CTRLA.RUNSTDBY=0, the GLK_SERCOMx_CORE will be disabled after any ongoing transaction is
         finished. Any interrupt can wake-up the device.
         I2C Slave Operation
         Writing CTRLA.RUNSTDBY=1 will allow the Address Match interrupt to wake-up the device.
         When CTRLA.RUNSTDBY=0, all receptions will be dropped.

36.6.6   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           •   Software Reset bit in the CTRLA register (CTRLA.SWRST)
           •   Enable bit in the CTRLA register (CTRLA.ENABLE)
           •   Command bits in CTRLB register (CTRLB.CMD)
           •   Write to Bus State bits in the Status register (STATUS.BUSSTATE)
           •   Address bits in the Address register (ADDR.ADDR) when in master operation.
         The following registers are synchronized when written:
           • Data (DATA) when in master operation
           • Length (LENGTH) when in slave operation
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.




         © 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 1027
                                                              SAM D5x/E5x Family Data Sheet
                                                                       SERCOM I2C – Inter-Integrated Circuit


36.7      Register Summary - I2C Slave

 Offset        Name        Bit Pos.

                              7:0     RUNSTDBY                                     MODE[2:0]               ENABLE       SWRST
                             15:8
 0x00         CTRLA
                             23:16    SEXTTOEN               SDAHOLD[1:0]                                               PINOUT
                             31:24                 LOWTOUT                          SCLSM                        SPEED[1:0]
                              7:0
                             15:8            AMODE[1:0]                                        AACKEN      GCMD          SMEN
 0x04         CTRLB
                             23:16                                                             ACKACT             CMD[1:0]
                             31:24
                              7:0                                                                SDASETUP[3:0]
                             15:8
 0x08         CTRLC
                             23:16
                             31:24                                                                                      DATA32B
 0x0C
   ...       Reserved
 0x13
 0x14        INTENCLR         7:0      ERROR                                                   DRDY       AMATCH         PREC
 0x15        Reserved
 0x16        INTENSET         7:0      ERROR                                                   DRDY       AMATCH         PREC
 0x17        Reserved
 0x18        INTFLAG          7:0      ERROR                                                   DRDY       AMATCH         PREC
 0x19        Reserved
                              7:0     CLKHOLD      LOWTOUT             SR                DIR   RXNACK       COLL        BUSERR
 0x1A         STATUS
                             15:8                                                                HS      SEXTTOUT
                              7:0                                    LENGTH                                ENABLE       SWRST
                             15:8
 0x1C       SYNCBUSY
                             23:16
                             31:24
 0x20
   ...       Reserved
 0x21
                              7:0                                            LEN[7:0]
 0x22         LENGTH
                             15:8                                                                                        LENEN
                              7:0                                   ADDR[6:0]                                           GENCEN
                             15:8     TENBITEN                                                            ADDR[9:7]
 0x24          ADDR
                             23:16                                ADDRMASK[6:0]
                             31:24                                                                      ADDRMASK[9:7]
                              7:0                                            DATA[7:0]
                             15:8                                           DATA[15:8]
 0x28          DATA
                             23:16                                          DATA[23:16]
                             31:24                                          DATA[31:24]




          © 2019 Microchip Technology Inc.                      Datasheet                               DS60001507E-page 1028
                                                         SAM D5x/E5x Family Data Sheet
                                                                 SERCOM I2C – Inter-Integrated Circuit


36.8   Register Description - I2C Slave
       Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
       8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
       accessed directly.
       Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
       write protection is denoted by the "PAC Write-Protection" property in each individual register description.
       For details, refer to 36.5.8 Register Access Protection.
       Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
       Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
       refer to 36.6.6 Synchronization.
       Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
       Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1029
                                                                   SAM D5x/E5x Family Data Sheet
                                                                           SERCOM I2C – Inter-Integrated Circuit

36.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00000000
               Property:    PAC Write-Protection, Enable-Protected, Write-Synchronized


         Bit        31            30            29            28            27            26            25                24
                               LOWTOUT                                    SCLSM                              SPEED[1:0]
   Access                        R/W                                       R/W                         R/W                R/W
    Reset                          0                                         0                          0                  0


         Bit        23            22            21            20            19            18            17                16
                SEXTTOEN                          SDAHOLD[1:0]                                                       PINOUT
   Access           R/W                        R/W           R/W                                                          R/W
    Reset            0                           0             0                                                           0


         Bit        15            14            13            12            11            10            9                  8


   Access
    Reset


         Bit         7             6             5             4             3            2             1                  0
                RUNSTDBY                                                MODE[2:0]                    ENABLE          SWRST
   Access           R/W                                      R/W           R/W           R/W           R/W                R/W
    Reset            0                                         0             0            0             0                  0


               Bit 30 – LOWTOUT SCL Low Time-Out
               This bit enables the SCL low time-out. If SCL is held low for 25ms-35ms, the slave will release its clock
               hold, if enabled, and reset the internal state machine. Any interrupt flags set at the time of time-out will
               remain set.
                Value       Description
                0           Time-out disabled.
                1           Time-out enabled.

               Bit 27 – SCLSM SCL Clock Stretch Mode
               This bit controls when SCL will be stretched for software interaction.
               This bit is not synchronized.
                Value       Description
                0           SCL stretch according to Figure 36-10
                1           SCL stretch only after ACK bit according to Figure 36-11

               Bits 25:24 – SPEED[1:0] Transfer Speed
               These bits define bus speed.
               These bits are not synchronized.
                Value      Description
                0x0        Standard-mode (Sm) up to 100 kHz and Fast-mode (Fm) up to 400 kHz
                0x1        Fast-mode Plus (Fm+) up to 1 MHz




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1030
                                                   SAM D5x/E5x Family Data Sheet
                                                            SERCOM I2C – Inter-Integrated Circuit

 Value        Description
 0x2          High-speed mode (Hs-mode) up to 3.4 MHz
 0x3          Reserved

Bit 23 – SEXTTOEN Slave SCL Low Extend Time-Out
This bit enables the slave SCL low extend time-out. If SCL is cumulatively held low for greater than 25ms
from the initial START to a STOP, the slave will release its clock hold if enabled and reset the internal
state machine. Any interrupt flags set at the time of time-out will remain set. If the address was
recognized, PREC will be set when a STOP is received.
This bit is not synchronized.
 Value       Description
 0           Time-out disabled
 1           Time-out enabled

Bits 21:20 – SDAHOLD[1:0] SDA Hold Time
These bits define the SDA hold time with respect to the negative edge of SCL.
These bits are not synchronized.
 Value      Name                   Description
 0x0        DIS                    Disabled
 0x1        75                     50-100ns hold time
 0x2        450                    300-600ns hold time
 0x3        600                    400-800ns hold time

Bit 16 – PINOUT Pin Usage
This bit sets the pin usage to either two- or four-wire operation:
This bit is not synchronized.
 Value       Description
 0           4-wire operation disabled
 1           4-wire operation enabled

Bit 7 – RUNSTDBY Run in Standby
This bit defines the functionality in standby sleep mode.
This bit is not synchronized.
 Value       Description
 0           Disabled – All reception is dropped.
 1           Wake on address match, if enabled.

Bits 4:2 – MODE[2:0] Operating Mode
These bits must be written to 0x04 to select the I2C slave serial communication interface of the SERCOM.
These bits are not synchronized.

Bit 1 – ENABLE Enable
Due to synchronization, there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRL.ENABLE will read back immediately and the Enable Synchronization
Busy bit in the Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE
will be cleared when the operation is complete.
This bit is not enable-protected.
 Value       Description
 0           The peripheral is disabled or being disabled.




© 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1031
                                                  SAM D5x/E5x Family Data Sheet
                                                          SERCOM I2C – Inter-Integrated Circuit

 Value        Description
 1            The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing '0' to this bit has no effect.
Writing '1' to this bit resets all registers in the SERCOM, except DBGCTRL, to their initial state, and the
SERCOM will be disabled.
Writing '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
write-operation will be discarded. Any register write access during the ongoing reset will result in an APB
error. Reading any register will return the reset value of the register.
Due to synchronization, there is a delay from writing CTRLA.SWRST until the reset is complete.
CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
This bit is not enable-protected.
 Value        Description
 0            There is no reset operation ongoing.
 1            The reset operation is ongoing.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1032
                                                                  SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit

36.8.2         Control B

               Name:          CTRLB
               Offset:        0x04
               Reset:         0x00000000
               Property:      PAC Write-Protection, Enable-Protected, Write-Synchronized


         Bit         31                30       29           28           27            26           25               24


   Access
    Reset


         Bit         23                22       21           20           19            18           17               16
                                                                                     ACKACT               CMD[1:0]
   Access                                                                              R/W           W                W
    Reset                                                                               0             0               0


         Bit         15                14       13           12           11            10            9               8
                          AMODE[1:0]                                                 AACKEN        GCMD              SMEN
   Access            R/W           R/W                                                 R/W          R/W              R/W
    Reset             0                0                                                0             0               0


         Bit          7                6         5           4             3            2             1               0


   Access
    Reset


               Bit 18 – ACKACT Acknowledge Action
               This bit defines the slave's acknowledge behavior after an address or data byte is received from the
               master. The acknowledge action is executed when a command is written to the CMD bits. If smart mode
               is enabled (CTRLB.SMEN=1), the acknowledge action is performed when the DATA register is read.
               ACKACT shall not be updated more than once between each peripheral interrupts request.
               This bit is not enable-protected.
                Value       Description
                0           Send ACK
                1           Send NACK

               Bits 17:16 – CMD[1:0] Command
               This bit field triggers the slave operation as the below. The CMD bits are strobe bits, and always read as
               zero. The operation is dependent on the slave interrupt flags, INTFLAG.DRDY and INTFLAG.AMATCH,
               in addition to STATUS.DIR.
               All interrupt flags (INTFLAG.DRDY, INTFLAG.AMATCH and INTFLAG.PREC) are automatically cleared
               when a command is given.
               This bit is not enable-protected.
               Table 36-3. Command Description

               CMD[1:0] DIR                   Action
               0x0           X                (No action)




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1033
                                                   SAM D5x/E5x Family Data Sheet
                                                            SERCOM I2C – Inter-Integrated Circuit

...........continued
 CMD[1:0] DIR                      Action
 0x1          X                    (Reserved)
 0x2          Used to complete a transaction in response to a data interrupt (DRDY)
              0 (Master write) Execute acknowledge action succeeded by waiting for any start (S/Sr)
                               condition
              1 (Master read) Wait for any start (S/Sr) condition
 0x3          Used in response to an address interrupt (AMATCH)
              0 (Master write) Execute acknowledge action succeeded by reception of next byte
              1 (Master read) Execute acknowledge action succeeded by slave data interrupt
              Used in response to a data interrupt (DRDY)
              0 (Master write) Execute acknowledge action succeeded by reception of next byte
              1 (Master read) Execute a byte read operation followed by ACK/NACK reception

Bits 15:14 – AMODE[1:0] Address Mode
These bits set the addressing mode.
These bits are not write-synchronized.
 Value      Name         Description
 0x0        MASK         The slave responds to the address written in ADDR.ADDR masked by the value
                         in ADDR.ADDRMASK.
                         See SERCOM – Serial Communication Interface for additional information.
 0x1        2_ADDRS The slave responds to the two unique addresses in ADDR.ADDR and
                         ADDR.ADDRMASK.
 0x2        RANGE        The slave responds to the range of addresses between and including
                         ADDR.ADDR and ADDR.ADDRMASK. ADDR.ADDR is the upper limit.
 0x3        -            Reserved.

Bit 10 – AACKEN Automatic Acknowledge Enable
This bit enables the address to be automatically acknowledged if there is an address match.
This bit is not write-synchronized.
 Value       Description
 0           Automatic acknowledge is disabled.
 1           Automatic acknowledge is enabled.

Bit 9 – GCMD PMBus Group Command
This bit enables PMBus group command support. When enabled, the Stop Recived interrupt flag
(INTFLAG.PREC) will be set when a STOP condition is detected if the slave has been addressed since
the last STOP condition on the bus.
This bit is not write-synchronized.
 Value       Description
 0           Group command is disabled.
 1           Group command is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1034
                                              SAM D5x/E5x Family Data Sheet
                                                    SERCOM I2C – Inter-Integrated Circuit

Bit 8 – SMEN Smart Mode Enable
When smart mode is enabled, data is acknowledged automatically when DATA.DATA is read.
This bit is not write-synchronized.
 Value       Description
 0           Smart mode is disabled.
 1           Smart mode is enabled.

Related Links
33. SERCOM – Serial Communication Interface




© 2019 Microchip Technology Inc.               Datasheet                      DS60001507E-page 1035
                                                                  SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit

36.8.3         Control C

               Name:       CTRLC
               Offset:     0x08
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        31            30           29            28           27              26          25           24
                                                                                                                DATA32B
   Access                                                                                                         R/W
    Reset                                                                                                          0


         Bit        23            22           21            20           19              18          17           16


   Access
    Reset


         Bit        15            14           13            12           11              10           9           8


   Access
    Reset


         Bit         7            6             5            4            3                2           1           0
                                                                                           SDASETUP[3:0]
   Access                                                                R/W              R/W         R/W         R/W
    Reset                                                                 0                0           0           0


               Bit 24 – DATA32B Data 32 Bit
               This bit enables 32-bit data writes and reads to/from the DATA register.
                Value      Description
                0          Data transaction to/from DATA are 8-bit in size
                1          Data transaction to/from DATA are 32-bit in size

               Bits 3:0 – SDASETUP[3:0] SDA Setup Time
               These bits select the minimum SDA-to-SCL setup time, measured from the release of SDA to the release
               of SCL:
               �SU:DAT = CLK_SERCOMx × APB period × 6 + 16 × SDASETUP




           © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1036
                                                                     SAM D5x/E5x Family Data Sheet
                                                                             SERCOM I2C – Inter-Integrated Circuit

36.8.4         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x14
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit         7              6             5              4             3              2             1            0
                  ERROR                                                                     DRDY         AMATCH         PREC
   Access           R/W                                                                     R/W            R/W          R/W
    Reset            0                                                                        0             0            0


               Bit 7 – ERROR Error Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Error Interrupt Enable bit, which disables the Error interrupt.
               Value         Description
               0             Error interrupt is disabled.
               1             Error interrupt is enabled.

               Bit 2 – DRDY Data Ready Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Data Ready bit, which disables the Data Ready interrupt.
               Value         Description
               0             The Data Ready interrupt is disabled.
               1             The Data Ready interrupt is enabled.

               Bit 1 – AMATCH Address Match Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Address Match Interrupt Enable bit, which disables the Address Match
               interrupt.
                Value        Description
                0            The Address Match interrupt is disabled.
                1            The Address Match interrupt is enabled.

               Bit 0 – PREC Stop Received Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Stop Received Interrupt Enable bit, which disables the Stop Received
               interrupt.
                Value        Description
                0            The Stop Received interrupt is disabled.
                1            The Stop Received interrupt is enabled.




           © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1037
                                                                     SAM D5x/E5x Family Data Sheet
                                                                             SERCOM I2C – Inter-Integrated Circuit

36.8.5         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x16
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

         Bit         7              6             5              4             3             2              1           0
                  ERROR                                                                    DRDY         AMATCH        PREC
   Access           R/W                                                                     R/W           R/W          R/W
    Reset            0                                                                       0              0           0


               Bit 7 – ERROR Error Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Error Interrupt Enable bit, which enables the Error interrupt.
               Value         Description
               0             Error interrupt is disabled.
               1             Error interrupt is enabled.

               Bit 2 – DRDY Data Ready Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Data Ready bit, which enables the Data Ready interrupt.
               Value         Description
               0             The Data Ready interrupt is disabled.
               1             The Data Ready interrupt is enabled.

               Bit 1 – AMATCH Address Match Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Address Match Interrupt Enable bit, which enables the Address Match
               interrupt.
                Value        Description
                0            The Address Match interrupt is disabled.
                1            The Address Match interrupt is enabled.

               Bit 0 – PREC Stop Received Interrupt Enable
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will set the Stop Received Interrupt Enable bit, which enables the Stop Received
               interrupt.
                Value        Description
                0            The Stop Received interrupt is disabled.
                1            The Stop Received interrupt is enabled.




           © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1038
                                                                     SAM D5x/E5x Family Data Sheet
                                                                              SERCOM I2C – Inter-Integrated Circuit

36.8.6         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x18
               Reset:       0x00
               Property:    -


         Bit         7              6             5              4             3           2             1             0
                  ERROR                                                                  DRDY        AMATCH          PREC
   Access           R/W                                                                   R/W          R/W           R/W
    Reset            0                                                                     0             0             0


               Bit 7 – ERROR Error
               This bit is set when any error is detected. Errors that will set this flag have corresponding status flags in
               the STATUS register. The corresponding bits in STATUS are LENERR, SEXTTOUT, LOWTOUT, COLL,
               and BUSERR.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the flag.

               Bit 2 – DRDY Data Ready
               This flag is set when a I2C slave byte transmission is successfully completed.
               The flag is cleared by hardware when either:
                • Writing to the DATA register.
                • Reading the DATA register with Smart mode enabled.
                • Writing a valid command to the CMD register.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Data Ready Interrupt flag.

               Bit 1 – AMATCH Address Match
               This flag is set when the I2C slave address match logic detects that a valid address has been received.
               The flag is cleared by hardware when CTRL.CMD is written.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Address Match Interrupt flag. When cleared, an ACK/NACK will be sent
               according to CTRLB.ACKACT.

               Bit 0 – PREC Stop Received
               This flag is set when a Stop condition is detected for a transaction being processed. A Stop condition
               detected between a bus master and another slave will not set this flag, unless the PMBus Group
               Command is enabled in the Control B register (CTRLB.GCMD=1).
               This flag is cleared by hardware after a command is issued on the next address match.
               Writing '0' to this bit has no effect.
               Writing '1' to this bit will clear the Stop Received Interrupt flag.




           © 2019 Microchip Technology Inc.                            Datasheet                        DS60001507E-page 1039
                                                                   SAM D5x/E5x Family Data Sheet
                                                                           SERCOM I2C – Inter-Integrated Circuit

36.8.7         Status

               Name:        STATUS
               Offset:      0x1A
               Reset:       0x0000
               Property:    -


         Bit        15            14            13            12            11            10             9             8
                                                                                          HS        SEXTTOUT
   Access                                                                                R/W           R/W
    Reset                                                                                  0             0


         Bit         7             6             5             4             3             2             1             0
                 CLKHOLD       LOWTOUT                        SR            DIR        RXNACK          COLL        BUSERR
   Access            R            R/W                          R             R             R           R/W            R/W
    Reset            0             0                           0             0             0             0             0


               Bit 10 – HS High-speed
               This bit is set if the slave detects a START followed by a Master Code transmission.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the status. However, this flag is automatically cleared when a STOP is
               received.

               Bit 9 – SEXTTOUT Slave SCL Low Extend Time-Out
               This bit is set if a slave SCL low extend time-out occurs.
               This bit is cleared automatically if responding to a new start condition with ACK or NACK (write 3 to
               CTRLB.CMD) or when INTFLAG.AMATCH is cleared.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the status.
                Value        Description
                0            No SCL low extend time-out has occurred.
                1            SCL low extend time-out has occurred.

               Bit 7 – CLKHOLD Clock Hold
               The slave Clock Hold bit (STATUS.CLKHOLD) is set when the slave is holding the SCL line low,
               stretching the I2C clock. Software should consider this bit a read-only status flag that is set when
               INTFLAG.DRDY or INTFLAG.AMATCH is set.
               This bit is automatically cleared when the corresponding interrupt is also cleared.

               Bit 6 – LOWTOUT SCL Low Time-out
               This bit is set if an SCL low time-out occurs.
               This bit is cleared automatically if responding to a new start condition with ACK or NACK (write 3 to
               CTRLB.CMD) or when INTFLAG.AMATCH is cleared.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the status.
                Value        Description
                0            No SCL low time-out has occurred.
                1            SCL low time-out has occurred.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1040
                                                   SAM D5x/E5x Family Data Sheet
                                                           SERCOM I2C – Inter-Integrated Circuit

Bit 4 – SR Repeated Start
When INTFLAG.AMATCH is raised due to an address match, SR indicates a repeated start or start
condition.
This flag is only valid while the INTFLAG.AMATCH flag is one.
 Value       Description
 0           Start condition on last address match
 1           Repeated start condition on last address match

Bit 3 – DIR Read / Write Direction
The Read/Write Direction (STATUS.DIR) bit stores the direction of the last address packet received from
a master.
 Value      Description
 0          Master write operation is in progress.
 1          Master read operation is in progress.

Bit 2 – RXNACK Received Not Acknowledge
This bit indicates whether the last data packet sent was acknowledged or not.
 Value       Description
 0            Master responded with ACK.
 1            Master responded with NACK.

Bit 1 – COLL Transmit Collision
If set, the I2C slave was not able to transmit a high data or NACK bit, the I2C slave will immediately
release the SDA and SCL lines and wait for the next packet addressed to it.
This flag is intended for the SMBus address resolution protocol (ARP). A detected collision in non-ARP
situations indicates that there has been a protocol violation, and should be treated as a bus error.
Note that this status will not trigger any interrupt, and should be checked by software to verify that the
data were sent correctly. This bit is cleared automatically if responding to an address match with an ACK
or a NACK (writing 0x3 to CTRLB.CMD), or INTFLAG.AMATCH is cleared.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the status.
 Value        Description
 0            No collision detected on last data byte sent.
 1            Collision detected on last data byte sent.

Bit 0 – BUSERR Bus Error
The Bus Error bit (STATUS.BUSERR) indicates that an illegal bus condition has occurred on the bus,
regardless of bus ownership. An illegal bus condition is detected if a protocol violating start, repeated
start or stop is detected on the I2C bus lines. A start condition directly followed by a stop condition is one
example of a protocol violation. If a time-out occurs during a frame, this is also considered a protocol
violation, and will set STATUS.BUSERR.
This bit is cleared automatically if responding to an address match with an ACK or a NACK (writing 0x3 to
CTRLB.CMD) or INTFLAG.AMATCH is cleared.
Writing a '1' to this bit will clear the status.
Writing a '0' to this bit has no effect.
 Value        Description
 0            No bus error detected.
 1            Bus error detected.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1041
                                                               SAM D5x/E5x Family Data Sheet
                                                                      SERCOM I2C – Inter-Integrated Circuit

36.8.8         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x1C
               Reset:      0x00000000
               Property:   -


         Bit        31           30           29          28           27          26           25           24


   Access
    Reset


         Bit        23           22           21          20           19          18           17           16


   Access
    Reset


         Bit        15           14           13          12           11          10           9            8


   Access
    Reset


         Bit        7             6           5           4            3           2            1            0
                                                       LENGTH                                ENABLE        SWRST
   Access                                                 R                                     R            R
    Reset                                                 0                                     0            0


               Bit 4 – LENGTH LENGTH Synchronization Busy
               Writing LENGTH requires synchronization. When written, this bit will be set until synchronization is
               complete. If LENGTH is written while SYNCBUSY.LENGTH is asserted, an APB error will be generated.
               Note: In slave mode, the clock is only running during data transfer, so SYNCBUSY.LENGTH will remain
               asserted until the next data transfer begins.
               Value       Description
               0           LENGTH synchronization is not busy.
               1           LENGTH synchronization is busy.

               Bit 1 – ENABLE SERCOM Enable Synchronization Busy
               Enabling and disabling the SERCOM (CTRLA.ENABLE) requires synchronization. When written, the
               SYNCBUSY.ENABLE bit will be set until synchronization is complete.
               Value      Description
               0          Enable synchronization is not busy.
               1          Enable synchronization is busy.

               Bit 0 – SWRST Software Reset Synchronization Busy
               Resetting the SERCOM (CTRLA.SWRST) requires synchronization. When written, the
               SYNCBUSY.SWRST bit will be set until synchronization is complete.
               Value       Description
               0           SWRST synchronization is not busy.




           © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1042
                                               SAM D5x/E5x Family Data Sheet
                                                    SERCOM I2C – Inter-Integrated Circuit

 Value        Description
 1            SWRST synchronization is busy.




© 2019 Microchip Technology Inc.               Datasheet                DS60001507E-page 1043
                                                                  SAM D5x/E5x Family Data Sheet
                                                                             SERCOM I2C – Inter-Integrated Circuit

36.8.9         Length

               Name:       LENGTH
               Offset:     0x22
               Reset:      0x0000
               Property:   PAC Write-Protection, Write-Synchronized


         Bit        15            14           13           12               11        10            9            8
                                                                                                                LENEN
   Access                                                                                                        R/W
    Reset                                                                                                         0


         Bit         7            6            5             4                3         2            1            0
                                                                  LEN[7:0]
   Access          R/W           R/W          R/W           R/W              R/W       R/W          R/W          R/W
    Reset            0            0            0             0                0         0            0            0


               Bit 8 – LENEN Data Length Enable
               In 32-bit Extension mode (CTRLC.DATA32B=1), this bit field enables the length counter.
                Value       Description
                0           Length counter is disabled.
                1           Length counter is enabled.

               Bits 7:0 – LEN[7:0] Data Length
               In 32-bit Extension mode (CTRLC.DATA32B=1) with Data Length counting enabled (LENGTH.LENEN),
               this bit field configures the data length from 0 to 255 Bytes after which the flag INTFLAG.DRDY is raised.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1044
                                                               SAM D5x/E5x Family Data Sheet
                                                                       SERCOM I2C – Inter-Integrated Circuit

36.8.10 Address

           Name:        ADDR
           Offset:      0x24
           Reset:       0x00000000
           Property:    PAC Write-Protection, Enable-Protected


     Bit        31            30            29            28            27           26            25            24
                                                                                             ADDRMASK[9:7]
  Access                                                                             R/W           R/W          R/W
   Reset                                                                              0             0             0


     Bit        23            22            21            20            19           18            17            16
                                                    ADDRMASK[6:0]
  Access        R/W          R/W           R/W           R/W           R/W           R/W           R/W
   Reset         0             0             0            0             0             0             0


     Bit        15            14            13            12            11           10             9             8
             TENBITEN                                                                           ADDR[9:7]
  Access        R/W                                                                  R/W           R/W          R/W
   Reset         0                                                                    0             0             0


     Bit         7             6             5            4             3             2             1             0
                                                      ADDR[6:0]                                               GENCEN
  Access        R/W          R/W           R/W           R/W           R/W           R/W           R/W          R/W
   Reset         0             0             0            0             0             0             0             0


           Bits 26:17 – ADDRMASK[9:0] Address Mask
           These bits act as a second address match register, an address mask register or the lower limit of an
           address range, depending on the CTRLB.AMODE setting.

           Bit 15 – TENBITEN Ten Bit Addressing Enable
           Value      Description
           0          10-bit address recognition disabled.
           1          10-bit address recognition enabled.

           Bits 10:1 – ADDR[9:0] Address
           These bits contain the I2C slave address used by the slave address match logic to determine if a master
           has addressed the slave.
           When using 7-bit addressing, the slave address is represented by ADDR[6:0].
           When using 10-bit addressing (ADDR.TENBITEN=1), the slave address is represented by ADDR[9:0]
           When the address match logic detects a match, INTFLAG.AMATCH is set and STATUS.DIR is updated to
           indicate whether it is a read or a write transaction.

           Bit 0 – GENCEN General Call Address Enable
           A general call address is an address consisting of all-zeroes, including the direction bit (master write).
           Value      Description
           0          General call address recognition disabled.
           1          General call address recognition enabled.




       © 2019 Microchip Technology Inc.                           Datasheet                        DS60001507E-page 1045
                                                            SAM D5x/E5x Family Data Sheet
                                                                        SERCOM I2C – Inter-Integrated Circuit

36.8.11 Data

           Name:       DATA
           Offset:     0x28
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31           30           29          28                 27       26        25           24
                                                           DATA[31:24]
  Access       R/W          R/W           R/W        R/W                R/W       R/W       R/W         R/W
   Reset        0             0            0           0                 0         0         0           0


     Bit        23           22           21          20                 19       18        17           16
                                                           DATA[23:16]
  Access       R/W          R/W           R/W        R/W                R/W       R/W       R/W         R/W
   Reset        0             0            0           0                 0         0         0           0


     Bit        15           14           13          12                 11       10         9           8
                                                           DATA[15:8]
  Access       R/W          R/W           R/W        R/W                R/W       R/W       R/W         R/W
   Reset        0             0            0           0                 0         0         0           0


     Bit        7             6            5           4                 3         2         1           0
                                                            DATA[7:0]
  Access       R/W          R/W           R/W        R/W                R/W       R/W       R/W         R/W
   Reset        0             0            0           0                 0         0         0           0


           Bits 31:0 – DATA[31:0] Data
           The slave data register I/O location (DATA.DATA) provides access to the master transmit and receive
           data buffers. Reading valid data or writing data to be transmitted can be successfully done only when
           SCL is held low by the slave (STATUS.CLKHOLD is set). An exception occurs when reading the last data
           byte after the stop condition has been received.
           Accessing DATA.DATA auto-triggers I2C bus operations. The operation performed depends on the state
           of CTRLB.ACKACT, CTRLB.SMEN and the type of access (read/write).
           When CTRLC.DATA32B=1, read and write transactions from/to the DATA register are 32 bit in size.
           Otherwise, reads and writes are 8 bit.




       © 2019 Microchip Technology Inc.                       Datasheet                     DS60001507E-page 1046
                                                               SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit


36.9      Register Summary - I2C Master

 Offset        Name        Bit Pos.

                              7:0     RUNSTDBY                                       MODE[2:0]              ENABLE       SWRST
                             15:8
 0x00         CTRLA
                             23:16    SEXTTOEN   MEXTTOEN     SDAHOLD[1:0]                                               PINOUT
                             31:24               LOWTOUT      INACTOUT[1:0]           SCLSM                     SPEED[1:0]
                              7:0
                             15:8                                                                           QCEN          SMEN
 0x04         CTRLB
                             23:16                                                               ACKACT            CMD[1:0]
                             31:24
                              7:0
                             15:8
 0x08         CTRLC
                             23:16
                             31:24                                                                                       DATA32B
                              7:0                                              BAUD[7:0]
                             15:8                                         BAUDLOW[7:0]
 0x0C          BAUD
                             23:16                                            HSBAUD[7:0]
                             31:24                                       HSBAUDLOW[7:0]
 0x10
   ...       Reserved
 0x13
 0x14        INTENCLR         7:0      ERROR                                                                  SB              MB
 0x15        Reserved
 0x16        INTENSET         7:0      ERROR                                                                  SB              MB
 0x17        Reserved
 0x18        INTFLAG          7:0      ERROR                                                                  SB              MB
 0x19        Reserved
                              7:0     CLKHOLD    LOWTOUT      BUSSTATE[1:0]                      RXNACK    ARBLOST       BUSERR
 0x1A         STATUS
                             15:8                                                                LENERR   SEXTTOUT      MEXTTOUT
                              7:0                                                                SYSOP      ENABLE       SWRST
                             15:8
 0x1C       SYNCBUSY
                             23:16
                             31:24
 0x20
   ...       Reserved
 0x23
                              7:0                                              ADDR[7:0]
                             15:8     TENBITEN     HS       LENEN                                         ADDR[10:8]
 0x24          ADDR
                             23:16                                             LEN[7:0]
                             31:24
                              7:0                                              DATA[7:0]
                             15:8                                             DATA[15:8]
 0x28          DATA
                             23:16                                            DATA[23:16]
                             31:24                                            DATA[31:24]




          © 2019 Microchip Technology Inc.                          Datasheet                             DS60001507E-page 1047
                                                                 SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit

...........continued

  Offset               Name    Bit Pos.

   0x2C
     ...           Reserved
   0x2F
   0x30            DBGCTRL        7:0                                                                             DBGSTOP




36.10          Register Description - I2C Master
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to 36.5.8 Register Access Protection.
               Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
               Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
               refer to 36.6.6 Synchronization.
               Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
               Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1048
                                                               SAM D5x/E5x Family Data Sheet
                                                                      SERCOM I2C – Inter-Integrated Circuit

36.10.1 Control A

           Name:        CTRLA
           Offset:      0x00
           Reset:       0x00000000
           Property:    PAC Write-Protection, Enable-Protected, Write-Synchronized


     Bit        31            30            29            28            27            26           25                 24
                           LOWTOUT           INACTOUT[1:0]            SCLSM                              SPEED[1:0]
  Access                     R/W           R/W           R/W           R/W                         R/W                R/W
   Reset                       0             0            0             0                           0                  0


     Bit        23            22            21            20            19            18           17                 16
            SEXTTOEN      MEXTTOEN            SDAHOLD[1:0]                                                       PINOUT
  Access        R/W          R/W           R/W           R/W                                                          R/W
   Reset         0             0             0            0                                                            0


     Bit        15            14            13            12            11            10            9                  8


  Access
   Reset


     Bit         7             6             5            4             3             2             1                  0
            RUNSTDBY                                                MODE[2:0]                    ENABLE          SWRST
  Access        R/W                                      R/W           R/W           R/W           R/W                R/W
   Reset         0                                        0             0             0             0                  0


           Bit 30 – LOWTOUT SCL Low Time-Out
           This bit enables the SCL low time-out. If SCL is held low for 25ms-35ms, the master will release its clock
           hold, if enabled, and complete the current transaction. A stop condition will automatically be transmitted.
           INTFLAG.SB or INTFLAG.MB will be set as normal, but the clock hold will be released. The
           STATUS.LOWTOUT and STATUS.BUSERR status bits will be set.
           This bit is not synchronized.
            Value       Description
            0           Time-out disabled.
            1           Time-out enabled.

           Bits 29:28 – INACTOUT[1:0] Inactive Time-Out
           If the inactive bus time-out is enabled and the bus is inactive for longer than the time-out setting, the bus
           state logic will be set to idle. An inactive bus arise when either an I2C master or slave is holding the SCL
           low.
           Enabling this option is necessary for SMBus compatibility, but can also be used in a non-SMBus set-up.
           Calculated time-out periods are based on a 100kHz baud rate.
           These bits are not synchronized.
            Value        Name               Description
            0x0          DIS                Disabled
            0x1          55US               5-6 SCL cycle time-out (50-60µs)
            0x2          105US              10-11 SCL cycle time-out (100-110µs)




       © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1049
                                                      SAM D5x/E5x Family Data Sheet
                                                              SERCOM I2C – Inter-Integrated Circuit

 Value        Name                 Description
 0x3          205US                20-21 SCL cycle time-out (200-210µs)

Bit 27 – SCLSM SCL Clock Stretch Mode
This bit controls when SCL will be stretched for software interaction.
This bit is not synchronized.
 Value       Description
 0           SCL stretch according to Figure 36-5.
 1           SCL stretch only after ACK bit, Figure 36-6.

Bits 25:24 – SPEED[1:0] Transfer Speed
These bits define bus speed.
These bits are not synchronized.
 Value      Description
 0x0        Standard-mode (Sm) up to 100 kHz and Fast-mode (Fm) up to 400 kHz
 0x1        Fast-mode Plus (Fm+) up to 1 MHz
 0x2        High-speed mode (Hs-mode) up to 3.4 MHz
 0x3        Reserved

Bit 23 – SEXTTOEN Slave SCL Low Extend Time-Out
This bit enables the slave SCL low extend time-out. If SCL is cumulatively held low for greater than 25ms
from the initial START to a STOP, the master will release its clock hold if enabled, and complete the
current transaction. A STOP will automatically be transmitted.
SB or MB will be set as normal, but CLKHOLD will be release. The MEXTTOUT and BUSERR status bits
will be set.
This bit is not synchronized.
 Value       Description
 0           Time-out disabled
 1           Time-out enabled

Bit 22 – MEXTTOEN Master SCL Low Extend Time-Out
This bit enables the master SCL low extend time-out. If SCL is cumulatively held low for greater than
10ms from START-to-ACK, ACK-to-ACK, or ACK-to-STOP the master will release its clock hold if
enabled, and complete the current transaction. A STOP will automatically be transmitted.
SB or MB will be set as normal, but CLKHOLD will be released. The MEXTTOUT and BUSERR status
bits will be set.
This bit is not synchronized.
 Value        Description
 0            Time-out disabled
 1            Time-out enabled

Bits 21:20 – SDAHOLD[1:0] SDA Hold Time
These bits define the SDA hold time with respect to the negative edge of SCL.
These bits are not synchronized.
 Value      Name                     Description
 0x0        DIS                      Disabled
 0x1        75NS                     50-100ns hold time
 0x2        450NS                    300-600ns hold time
 0x3        600NS                    400-800ns hold time




© 2019 Microchip Technology Inc.                        Datasheet                   DS60001507E-page 1050
                                                    SAM D5x/E5x Family Data Sheet
                                                            SERCOM I2C – Inter-Integrated Circuit

Bit 16 – PINOUT Pin Usage
This bit set the pin usage to either two- or four-wire operation:
This bit is not synchronized.
 Value        Description
 0            4-wire operation disabled.
 1            4-wire operation enabled.

Bit 7 – RUNSTDBY Run in Standby
This bit defines the functionality in standby sleep mode.
This bit is not synchronized.
 Value       Description
 0           GCLK_SERCOMx_CORE is disabled and the I2C master will not operate in standby sleep
             mode.
 1           GCLK_SERCOMx_CORE is enabled in all sleep modes.

Bits 4:2 – MODE[2:0] Operating Mode
These bits must be written to 0x5 to select the I2C master serial communication interface of the
SERCOM.
These bits are not synchronized.

Bit 1 – ENABLE Enable
Due to synchronization, there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRL.ENABLE will read back immediately and the Synchronization Enable
Busy bit in the Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE
will be cleared when the operation is complete.
This bit is not enable-protected.
 Value       Description
 0           The peripheral is disabled or being disabled.
 1           The peripheral is enabled.

Bit 0 – SWRST Software Reset
Writing '0' to this bit has no effect.
Writing '1' to this bit resets all registers in the SERCOM, except DBGCTRL, to their initial state, and the
SERCOM will be disabled.
Writing '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
write-operation will be discarded. Any register write access during the ongoing reset will result in an APB
error. Reading any register will return the reset value of the register.
Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
This bit is not enable-protected.
 Value        Description
 0            There is no reset operation ongoing.
 1            The reset operation is ongoing.




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1051
                                                             SAM D5x/E5x Family Data Sheet
                                                                    SERCOM I2C – Inter-Integrated Circuit

36.10.2 Control B

           Name:       CTRLB
           Offset:     0x04
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected, Write-Synchronized


     Bit        31            30           29           28            27           26           25                24


  Access
   Reset


     Bit        23            22           21           20            19           18           17                16
                                                                                ACKACT                CMD[1:0]
  Access                                                                          R/W            W                W
   Reset                                                                            0            0                0


     Bit        15            14           13           12            11           10            9                8
                                                                                               QCEN              SMEN
  Access                                                                                        R/W              R/W
   Reset                                                                                         0                0


     Bit         7            6            5             4            3             2            1                0


  Access
   Reset


           Bit 18 – ACKACT Acknowledge Action
           This bit defines the I2C master's acknowledge behavior after a data byte is received from the I2C slave.
           The acknowledge action is executed when a command is written to CTRLB.CMD, or if Smart mode is
           enabled (CTRLB.SMEN is written to one), when DATA.DATA is read.
           This bit is not enable-protected.
           This bit is not write-synchronized.
            Value       Description
            0           Send ACK.
            1           Send NACK.

           Bits 17:16 – CMD[1:0] Command
           Writing these bits triggers a master operation as described below. The CMD bits are strobe bits, and
           always read as zero. The acknowledge action is only valid in Master Read mode. In Master Write mode, a
           command will only result in a repeated Start or Stop condition. The CTRLB.ACKACT bit and the CMD bits
           can be written at the same time, and then the acknowledge action will be updated before the command is
           triggered.
           Commands can only be issued when either the Slave on Bus Interrupt flag (INTFLAG.SB) or Master on
           Bus Interrupt flag (INTFLAG.MB) is '1'.
           If CMD 0x1 is issued, a repeated start will be issued followed by the transmission of the current address
           in ADDR.ADDR. If another address is desired, ADDR.ADDR must be written instead of the CMD bits.
           This will trigger a repeated start followed by transmission of the new address.




       © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1052
                                                        SAM D5x/E5x Family Data Sheet
                                                               SERCOM I2C – Inter-Integrated Circuit

Issuing a command will set the System Operation bit in the Synchronization Busy register
(SYNCBUSY.SYSOP).
Table 36-4. Command Description

 CMD[1:0]       Direction          Action
 0x0            X                  (No action)
 0x1            X                  Execute acknowledge action succeeded by repeated Start
 0x2            0 (Write)          No operation
                1 (Read)           Execute acknowledge action succeeded by a byte read operation
 0x3            X                  Execute acknowledge action succeeded by issuing a Stop condition

These bits are not enable-protected.

Bit 9 – QCEN Quick Command Enable
This bit is not write-synchronized.
 Value       Description
 0           Quick Command is disabled.
 1           Quick Command is enabled.

Bit 8 – SMEN Smart Mode Enable
When Smart mode is enabled, acknowledge action is sent when DATA.DATA is read.
This bit is not write-synchronized.
 Value       Description
 0           Smart mode is disabled.
 1           Smart mode is enabled.




© 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1053
                                                              SAM D5x/E5x Family Data Sheet
                                                                     SERCOM I2C – Inter-Integrated Circuit

36.10.3 Control C

           Name:       CTRLC
           Offset:     0x08
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31            30           29            28           27              26   25           24
                                                                                                     DATA32B
  Access                                                                                               R/W
   Reset                                                                                                0


     Bit        23            22           21            20           19              18   17           16


  Access
   Reset


     Bit        15            14           13            12           11              10   9            8


  Access
   Reset


     Bit         7            6             5            4            3               2    1            0


  Access
   Reset


           Bit 24 – DATA32B Data 32 Bit
           This bit enables 32-bit data writes and reads to/from the DATA register.
            Value      Description
            0          Data transactions to/from DATA are 8-bit in size
            1          Data transactions to/from DATA are 32-bit in size




       © 2019 Microchip Technology Inc.                       Datasheet                    DS60001507E-page 1054
                                                              SAM D5x/E5x Family Data Sheet
                                                                         SERCOM I2C – Inter-Integrated Circuit

36.10.4 Baud Rate

           Name:       BAUD
           Offset:     0x0C
           Reset:      0x0000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31           30           29           28                 27       26          25           24
                                                        HSBAUDLOW[7:0]
  Access       R/W          R/W           R/W          R/W               R/W       R/W        R/W          R/W
   Reset         0            0            0            0                 0         0          0             0


     Bit        23           22           21           20                 19       18          17           16
                                                            HSBAUD[7:0]
  Access       R/W          R/W           R/W          R/W               R/W       R/W        R/W          R/W
   Reset         0            0            0            0                 0         0          0             0


     Bit        15           14           13           12                 11       10          9             8
                                                         BAUDLOW[7:0]
  Access       R/W          R/W           R/W          R/W               R/W       R/W        R/W          R/W
   Reset         0            0            0            0                 0         0          0             0


     Bit         7            6            5            4                 3         2          1             0
                                                             BAUD[7:0]
  Access       R/W          R/W           R/W          R/W               R/W       R/W        R/W          R/W
   Reset         0            0            0            0                 0         0          0             0


           Bits 31:24 – HSBAUDLOW[7:0] High Speed Master Baud Rate Low
           HSBAUDLOW non-zero: HSBAUDLOW indicates the SCL low time in High-speed mode according to
           HSBAUDLOW = �GCLK ⋅ �LOW − 1
           HSBAUDLOW equal to zero: The HSBAUD register is used to time TLOW, THIGH, TSU;STO, THD;STA and
           TSU;STA.. TBUF is timed by the BAUD register.

           Bits 23:16 – HSBAUD[7:0] High Speed Master Baud Rate
           This bit field indicates the SCL high time in High-speed mode according to the following formula. When
           HSBAUDLOW is zero, TLOW, THIGH, TSU;STO, THD;STA and TSU;STA are derived using this formula. TBUF is
           timed by the BAUD register.
           HSBAUD = �GCLK ⋅ �HIGH − 1

           Bits 15:8 – BAUDLOW[7:0] Master Baud Rate Low
           If this bit field is non-zero, the SCL low time will be described by the value written.
           For more information on how to calculate the frequency, see SERCOM 33.6.2.3 Clock Generation –
           Baud-Rate Generator.

           Bits 7:0 – BAUD[7:0] Master Baud Rate
           This bit field is used to derive the SCL high time if BAUD.BAUDLOW is non-zero. If BAUD.BAUDLOW is
           zero, BAUD will be used to generate both high and low periods of the SCL.
           For more information on how to calculate the frequency, see SERCOM 33.6.2.3 Clock Generation –
           Baud-Rate Generator.




       © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1055
                                                                  SAM D5x/E5x Family Data Sheet
                                                                          SERCOM I2C – Inter-Integrated Circuit

36.10.5 Interrupt Enable Clear

            Name:        INTENCLR
            Offset:      0x14
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

      Bit         7              6             5              4             3              2             1            0
               ERROR                                                                                     SB          MB
  Access         R/W                                                                                    R/W          R/W
   Reset          0                                                                                      0            0


            Bit 7 – ERROR Error Interrupt Enable
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will clear the Error Interrupt Enable bit, which disables the Error interrupt.
            Value         Description
            0             Error interrupt is disabled.
            1             Error interrupt is enabled.

            Bit 1 – SB Slave on Bus Interrupt Enable
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will clear the Slave on Bus Interrupt Enable bit, which disables the Slave on Bus
            interrupt.
             Value        Description
             0            The Slave on Bus interrupt is disabled.
             1            The Slave on Bus interrupt is enabled.

            Bit 0 – MB Master on Bus Interrupt Enable
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will clear the Master on Bus Interrupt Enable bit, which disables the Master on Bus
            interrupt.
             Value        Description
             0            The Master on Bus interrupt is disabled.
             1            The Master on Bus interrupt is enabled.




        © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1056
                                                                  SAM D5x/E5x Family Data Sheet
                                                                          SERCOM I2C – Inter-Integrated Circuit

36.10.6 Interrupt Enable Set

            Name:        INTENSET
            Offset:      0x16
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

      Bit         7              6             5              4             3             2              1           0
               ERROR                                                                                    SB           MB
  Access         R/W                                                                                   R/W          R/W
   Reset          0                                                                                      0           0


            Bit 7 – ERROR Error Interrupt Enable
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will set the Error Interrupt Enable bit, which enables the Error interrupt.
            Value         Description
            0             Error interrupt is disabled.
            1             Error interrupt is enabled.

            Bit 1 – SB Slave on Bus Interrupt Enable
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will set the Slave on Bus Interrupt Enable bit, which enables the Slave on Bus
            interrupt.
             Value        Description
             0            The Slave on Bus interrupt is disabled.
             1            The Slave on Bus interrupt is enabled.

            Bit 0 – MB Master on Bus Interrupt Enable
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will set the Master on Bus Interrupt Enable bit, which enables the Master on Bus
            interrupt.
             Value        Description
             0            The Master on Bus interrupt is disabled.
             1            The Master on Bus interrupt is enabled.




        © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1057
                                                                 SAM D5x/E5x Family Data Sheet
                                                                          SERCOM I2C – Inter-Integrated Circuit

36.10.7 Interrupt Flag Status and Clear

            Name:        INTFLAG
            Offset:      0x18
            Reset:       0x00
            Property:    -


      Bit         7             6              5             4             3              2             1             0
               ERROR                                                                                   SB            MB
  Access         R/W                                                                                   R/W           R/W
    Reset         0                                                                                     0             0


            Bit 7 – ERROR Error
            This flag is cleared by writing '1' to it.
            This bit is set when any error is detected. Errors that will set this flag have corresponding status bits in the
            STATUS register. These status bits are LENERR, SEXTTOUT, MEXTTOUT, LOWTOUT, ARBLOST, and
            BUSERR.
            Writing '0' to this bit has no effect.
            Writing '1' to this bit will clear the flag.

            Bit 1 – SB Slave on Bus
            The Slave on Bus flag (SB) is set when a byte is successfully received in Master Read mode, for
            example, no arbitration lost or bus error occurred during the operation. When this flag is set, the master
            forces the SCL line low, stretching the I2C clock period. The SCL line will be released and SB will be
            cleared on one of the following actions:
              • Writing to ADDR.ADDR
              • Writing to DATA.DATA
              • Reading DATA.DATA when Smart mode is enabled (CTRLB.SMEN)
              • Writing a valid command to CTRLB.CMD
            Writing '1' to this bit location will clear the SB flag. The transaction will not continue or be terminated until
            one of the above actions is performed.
            Writing '0' to this bit has no effect.

            Bit 0 – MB Master on Bus
            This flag is set when a byte is transmitted in Master Write mode. The flag is set regardless of the
            occurrence of a bus error or an Arbitration Lost condition. MB is also set when arbitration is lost during
            sending of NACK in Master Read mode, or when issuing a Start condition if the bus state is unknown.
            When this flag is set and arbitration is not lost, the master forces the SCL line low, stretching the I2C clock
            period. The SCL line will be released and MB will be cleared on one of the following actions:
             • Writing to ADDR.ADDR
             • Writing to DATA.DATA
             • Reading DATA.DATA when Smart mode is enabled (CTRLB.SMEN)
             • Writing a valid command to CTRLB.CMD
            Writing '1' to this bit location will clear the MB flag. The transaction will not continue or be terminated until
            one of the above actions is performed.
            Writing '0' to this bit has no effect.




        © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 1058
                                                              SAM D5x/E5x Family Data Sheet
                                                                      SERCOM I2C – Inter-Integrated Circuit

36.10.8 Status

           Name:        STATUS
           Offset:      0x1A
           Reset:       0x0000
           Property:    Write-Synchronized


     Bit        15            14            13           12            11            10            9            8
                                                                                  LENERR      SEXTTOUT      MEXTTOUT
  Access                                                                            R/W          R/W           R/W
   Reset                                                                             0             0            0


     Bit         7            6              5            4            3             2             1            0
             CLKHOLD      LOWTOUT            BUSSTATE[1:0]                        RXNACK       ARBLOST       BUSERR
  Access         R           R/W           R/W          R/W                          R           R/W           R/W
   Reset         0            0              0            0                          0             0            0


           Bit 10 – LENERR Transaction Length Error
           This bit is set when automatic length is used for a DMA and/or 32-bit transaction and the slave sends a
           NACK before ADDR.LEN bytes have been written by the master.
           Writing '1' to this bit location will clear STATUS.LENERR. This flag is automatically cleared when writing
           to the ADDR register.
           Writing '0' to this bit has no effect.
           This bit is not write-synchronized.

           Bit 9 – SEXTTOUT Slave SCL Low Extend Time-Out
           This bit is set if a slave SCL low extend time-out occurs.
           This bit is automatically cleared when writing to the ADDR register.
           Writing '1' to this bit location will clear SEXTTOUT. Normal use of the I2C interface does not require the
           SEXTTOUT flag to be cleared by this method.
           Writing '0' to this bit has no effect.
           This bit is not write-synchronized.

           Bit 8 – MEXTTOUT Master SCL Low Extend Time-Out
           This bit is set if a master SCL low time-out occurs.
           Writing '1' to this bit location will clear STATUS.MEXTTOUT. This flag is automatically cleared when
           writing to the ADDR register.
           Writing '0' to this bit has no effect.
           This bit is not write-synchronized.

           Bit 7 – CLKHOLD Clock Hold
           This bit is set when the master is holding the SCL line low, stretching the I2C clock. Software should
           consider this bit when INTFLAG.SB or INTFLAG.MB is set.
           This bit is cleared when the corresponding Interrupt flag is cleared and the next operation is given.
           Writing '0' to this bit has no effect.
           Writing '1' to this bit has no effect.
           This bit is not write-synchronized.




       © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1059
                                                     SAM D5x/E5x Family Data Sheet
                                                             SERCOM I2C – Inter-Integrated Circuit

Bit 6 – LOWTOUT SCL Low Time-Out
This bit is set if an SCL low time-out occurs.
Writing '1' to this bit location will clear this bit. This flag is automatically cleared when writing to the ADDR
register.
Writing '0' to this bit has no effect.
This bit is not write-synchronized.

Bits 5:4 – BUSSTATE[1:0] Bus State
These bits indicate the current I2C Bus state.
When in UNKNOWN state, writing 0x1 to BUSSTATE forces the bus state into the IDLE state. The bus
state cannot be forced into any other state.
Writing BUSSTATE to idle will set SYNCBUSY.SYSOP.
 Value      Name          Description
 0x0        UNKNOWN The Bus state is unknown to the I2C master and will wait for a Stop condition to
                          be detected or wait to be forced into an Idle state by software
 0x1        IDLE          The Bus state is waiting for a transaction to be initialized
 0x2        OWNER         The I2C master is the current owner of the bus
 0x3        BUSY          Some other I2C master owns the bus

Bit 2 – RXNACK Received Not Acknowledge
This bit indicates whether the last address or data packet sent was acknowledged or not.
Writing '0' to this bit has no effect.
Writing '1' to this bit has no effect.
This bit is not write-synchronized.
 Value        Description
 0            Slave responded with ACK.
 1            Slave responded with NACK.

Bit 1 – ARBLOST Arbitration Lost
This bit is set if arbitration is lost while transmitting a high data bit or a NACK bit, or while issuing a Start
or Repeated Start condition on the bus. The Master on Bus Interrupt flag (INTFLAG.MB) will be set when
STATUS.ARBLOST is set.
Writing the ADDR.ADDR register will automatically clear STATUS.ARBLOST.
Writing '0' to this bit has no effect.
Writing '1' to this bit will clear it.
This bit is not write-synchronized.

Bit 0 – BUSERR Bus Error
This bit indicates that an illegal Bus condition has occurred on the bus, regardless of bus ownership. An
illegal Bus condition is detected if a protocol violating start, repeated start or stop is detected on the I2C
bus lines. A Start condition directly followed by a Stop condition is one example of a protocol violation. If a
time-out occurs during a frame, this is also considered a protocol violation, and will set BUSERR.
If the I2C master is the bus owner at the time a bus error occurs, STATUS.ARBLOST and INTFLAG.MB
will be set in addition to BUSERR.
Writing the ADDR.ADDR register will automatically clear the BUSERR flag.
Writing '0' to this bit has no effect.
Writing '1' to this bit will clear it.
This bit is not write-synchronized.




© 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1060
                                                           SAM D5x/E5x Family Data Sheet
                                                                  SERCOM I2C – Inter-Integrated Circuit

36.10.9 Synchronization Busy

           Name:       SYNCBUSY
           Offset:     0x1C
           Reset:      0x00000000


     Bit        31           30           29          28           27           26           25           24


  Access
   Reset


     Bit        23           22           21          20           19           18           17           16


  Access
   Reset


     Bit        15           14           13          12           11           10           9            8


  Access
   Reset


     Bit        7             6           5            4            3           2            1            0
                                                                              SYSOP       ENABLE        SWRST
  Access                                                                        R            R            R
   Reset                                                                        0            0            0


           Bit 2 – SYSOP System Operation Synchronization Busy
           Writing CTRLB.CMD, STATUS.BUSSTATE, ADDR, or DATA when the SERCOM is enabled requires
           synchronization. When written, the SYNCBUSY.SYSOP bit will be set until synchronization is complete.
            Value     Description
            0         System operation synchronization is not busy.
            1         System operation synchronization is busy.

           Bit 1 – ENABLE SERCOM Enable Synchronization Busy
           Enabling and disabling the SERCOM (CTRLA.ENABLE) requires synchronization. When written, the
           SYNCBUSY.ENABLE bit will be set until synchronization is complete.
           Value      Description
           0          Enable synchronization is not busy.
           1          Enable synchronization is busy.

           Bit 0 – SWRST Software Reset Synchronization Busy
           Resetting the SERCOM (CTRLA.SWRST) requires synchronization. When written, the
           SYNCBUSY.SWRST bit will be set until synchronization is complete.
           Value       Description
           0           SWRST synchronization is not busy.
           1           SWRST synchronization is busy.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1061
                                                               SAM D5x/E5x Family Data Sheet
                                                                           SERCOM I2C – Inter-Integrated Circuit

36.10.10 Address

            Name:        ADDR
            Offset:      0x24
            Reset:       0x0000
            Property:    Write-Synchronized


      Bit        31            30           29           28                27        26           25           24


  Access
   Reset


      Bit        23            22           21           20                19        18           17           16
                                                               LEN[7:0]
  Access        R/W           R/W           R/W          R/W               R/W       R/W         R/W          R/W
   Reset          0            0              0           0                 0         0           0             0


      Bit        15            14           13           12                11        10           9             8
              TENBITEN        HS           LENEN                                              ADDR[10:8]
  Access        R/W           R/W           R/W                                      R/W         R/W          R/W
   Reset          0            0              0                                       0           0             0


      Bit         7            6              5           4                 3         2           1             0
                                                               ADDR[7:0]
  Access        R/W           R/W           R/W          R/W               R/W       R/W         R/W          R/W
   Reset          0            0              0           0                 0         0           0             0


            Bits 23:16 – LEN[7:0] Transaction Length
            These bits define the transaction length of a DMA and/or 32-bit transaction from 0 to 255 bytes. The
            Transfer Length Enable (LENEN) bit must be written to '1' in order to use DMA.

            Bit 15 – TENBITEN Ten Bit Addressing Enable
            This bit enables 10-bit addressing. This bit can be written simultaneously with ADDR to indicate a 10-bit
            or 7-bit address transmission.
             Value       Description
             0           10-bit addressing disabled.
             1           10-bit addressing enabled.

            Bit 14 – HS High Speed
            This bit enables High-speed mode for the current transfer from repeated START to STOP. This bit can be
            written simultaneously with ADDR for a high speed transfer.
             Value      Description
             0          High-speed transfer disabled.
             1          High-speed transfer enabled.

            Bit 13 – LENEN Transfer Length Enable
            Value      Description
            0          Automatic transfer length disabled.
            1          Automatic transfer length enabled.




        © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 1062
                                                 SAM D5x/E5x Family Data Sheet
                                                         SERCOM I2C – Inter-Integrated Circuit

Bits 10:0 – ADDR[10:0] Address
When ADDR is written, the consecutive operation will depend on the bus state:
UNKNOWN: INTFLAG.MB and STATUS.BUSERR are set, and the operation is terminated.
BUSY: The I2C master will await further operation until the bus becomes IDLE.
IDLE: The I2C master will issue a start condition followed by the address written in ADDR. If the address
is acknowledged, SCL is forced and held low, and STATUS.CLKHOLD and INTFLAG.MB are set.
OWNER: A repeated start sequence will be performed. If the previous transaction was a read, the
acknowledge action is sent before the repeated start bus condition is issued on the bus. Writing ADDR to
issue a repeated start is performed while INTFLAG.MB or INTFLAG.SB is set.
STATUS.BUSERR, STATUS.ARBLOST, INTFLAG.MB and INTFLAG.SB will be cleared when ADDR is
written.
The ADDR register can be read at any time without interfering with ongoing bus activity, as a read access
does not trigger the master logic to perform any bus protocol related operations.
The I2C master control logic uses bit 0 of ADDR as the bus protocol’s read/write flag (R/W); 0 for write
and 1 for read.




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1063
                                                               SAM D5x/E5x Family Data Sheet
                                                                           SERCOM I2C – Inter-Integrated Circuit

36.10.11 Data

            Name:       DATA
            Offset:     0x28
            Reset:      0x00000000
            Property:   Read/Write


      Bit        31           30           29            28                 27       26         25           24
                                                              DATA[31:24]
  Access        R/W          R/W           R/W          R/W                R/W       R/W       R/W          R/W
   Reset          0            0            0            0                  0         0         0             0


      Bit        23           22           21            20                 19       18         17           16
                                                              DATA[23:16]
  Access        R/W          R/W           R/W          R/W                R/W       R/W       R/W          R/W
   Reset          0            0            0            0                  0         0         0             0


      Bit        15           14           13            12                 11       10         9             8
                                                              DATA[15:8]
  Access        R/W          R/W           R/W          R/W                R/W       R/W       R/W          R/W
   Reset          0            0            0            0                  0         0         0             0


      Bit         7            6            5            4                  3         2         1             0
                                                               DATA[7:0]
  Access        R/W          R/W           R/W          R/W                R/W       R/W       R/W          R/W
   Reset          0            0            0            0                  0         0         0             0


            Bits 31:0 – DATA[31:0] Data
            The master data register I/O location (DATA) provides access to the master transmit and receive data
            buffers. Reading valid data or writing data to be transmitted can be successfully done only when SCL is
            held low by the master (STATUS.CLKHOLD is set). An exception is reading the last data byte after the
            stop condition has been sent.
            Accessing DATA.DATA auto-triggers I2C bus operations. The operation performed depends on the state
            of CTRLB.ACKACT, CTRLB.SMEN and the type of access (read/write).
            When CTRLC.DATA32B=1, read and write transactions from/to the DATA register are 32 bit in size.
            Otherwise, reads and writes are 8 bit.




        © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1064
                                                            SAM D5x/E5x Family Data Sheet
                                                                   SERCOM I2C – Inter-Integrated Circuit

36.10.12 Debug Control

            Name:       DBGCTRL
            Offset:     0x30
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit        7             6           5            4            3            2            1            0
                                                                                                        DBGSTOP
  Access                                                                                                  R/W
   Reset                                                                                                    0


            Bit 0 – DBGSTOP Debug Stop Mode
            This bit controls functionality when the CPU is halted by an external debugger.
             Value       Description
             0           The baud-rate generator continues normal operation when the CPU is halted by an external
                         debugger.
             1           The baud-rate generator is halted when the CPU is halted by an external debugger.




        © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1065
