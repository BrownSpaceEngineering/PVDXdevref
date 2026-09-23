# 27. PAC - Peripheral Access Controller

*Source: `Atmel-SAMD51.pdf`, pages 725-762 — SAMD51 family datasheet*

                                                           SAM D5x/E5x Family Data Sheet
                                                                        PAC - Peripheral Access Controller


27.      PAC - Peripheral Access Controller

27.1     Overview
         The Peripheral Access Controller provides an interface for the locking and unlocking of peripheral
         registers within the device. It reports all violations that could happen when accessing a peripheral: write
         protected access, illegal access, enable protected access, access when clock synchronization or
         software reset is on-going. These errors are reported in a unique interrupt flag for a peripheral. The PAC
         module also reports errors occurring at the slave bus level, when an access to a non-existing address is
         detected.



27.2     Features
           • Manages write protection access and reports access errors for the peripheral modules or bridges.



27.3     Block Diagram
         Figure 27-1. PAC Block Diagram

                                                PAC
                        IRQ                                                Slave ERROR
                                                                                             SLAVEs

                        APB                   INTFLAG
                                                                          Peripheral ERROR
                                                                                               PERIPHERAL m

                                                                             BUSn

                                                                                               PERIPHERAL 0
                                                                          WRITE CONTROL




                                            PAC CONTROL                   Peripheral ERROR
                                                                                               PERIPHERAL m

                                                                            BUS0

                                                                                               PERIPHERAL 0
                                                                          WRITE CONTROL




27.4     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

27.4.1   IO Lines
         Not applicable.

27.4.2   Power Management
         The PAC can continue to operate in any Sleep mode where the selected source clock is running. The
         PAC interrupts can be used to wake up the device from Sleep modes. The events can trigger other
         operations in the system without exiting sleep modes.




         © 2019 Microchip Technology Inc.                    Datasheet                             DS60001507E-page 725
                                                            SAM D5x/E5x Family Data Sheet
                                                                        PAC - Peripheral Access Controller

         Related Links
         18. PM – Power Manager

27.4.3   Clocks
         The PAC bus clock (CLK_PAC_APB) can be enabled and disabled in the Main Clock module. The default
         state of CLK_PAC_APB can be found in the related links.
         Related Links
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking

27.4.4   DMA
         Not applicable.

27.4.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. Using the PAC interrupt requires the
         Interrupt Controller to be configured first.
         Table 27-1. Interrupt Lines

          Instances                                             NVIC Line
          PAC                                                   ERR

         Related Links
         10.2 Nested Vector Interrupt Controller

27.4.6   Events
         The events are connected to the Event System, which may need configuration.
         Related Links
         31. EVSYS – Event System

27.4.7   Debug Operation
         When the CPU is halted in Debug mode, write protection of all peripherals is disabled and the PAC
         continues normal operation.

27.4.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Write Control (WRCTRL) register
           • AHB Slave Bus Interrupt Flag Status and Clear (INTFLAGAHB) register
           • Peripheral Interrupt Flag Status and Clear n (INTFLAG A/B/C...) registers
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 726
                                                            SAM D5x/E5x Family Data Sheet
                                                                         PAC - Peripheral Access Controller


27.5     Functional Description

27.5.1   Principle of Operation
         The Peripheral Access Control module allows the user to set a write protection on peripheral modules
         and generate an interrupt in case of a peripheral access violation. The peripheral’s protection can be set,
         cleared or locked at the user discretion. A set of Interrupt Flag and Status registers informs the user on
         the status of the violation in the peripherals. In addition, slaves bus errors can be also reported in the
         cases where reserved area is accessed by the application.

27.5.2   Basic Operation

27.5.2.1 Initialization, Enabling and Resetting
         The PAC is always enabled after reset.
         Only a hardware reset will reset the PAC module.

27.5.2.2 Operations
         The PAC module allows the user to set, clear or lock the write protection status of all peripherals on all
         Peripheral Bridges.
         If a peripheral register violation occurs, the Peripheral Interrupt Flag n registers (INTFLAGn) are updated
         to inform the user on the status of the violation in the peripherals connected to the Peripheral Bridge n (n
         = A,B,C ...). The corresponding Peripheral Write Control Status n register (STATUSn) gives the state of
         the write protection for all peripherals connected to the corresponding Peripheral Bridge n. Refer to
         27.5.2.3 Peripheral Access Errors for details.
         The PAC module also report the errors occurring at slave bus level when an access to reserved area is
         detected. AHB Slave Bus Interrupt Flag register (INTFLAGAHB) informs the user on the status of the
         violation in the corresponding slave. Refer to the 27.5.2.6 AHB Slave Bus Errors for details.

27.5.2.3 Peripheral Access Errors
         The following events will generate a Peripheral Access Error:
           • Protected write: To avoid unexpected writes to a peripheral's registers, each peripheral can be write
             protected. Only the registers denoted as “PAC Write-Protection” in the module’s datasheet can be
             protected. If a peripheral is not write protected, write data accesses are performed normally. If a
             peripheral is write protected and if a write access is attempted, data will not be written and peripheral
             returns an access error. The corresponding interrupt flag bit in the INTFLAGn register will be set.
           • Illegal access: Access to an unimplemented register within the module.
           • Synchronized write error: For write-synchronized registers an error will be reported if the register is
             written while a synchronization is ongoing.
         When any of the INTFLAGn registers bit are set, an interrupt will be requested if the PAC interrupt enable
         bit is set.
         Related Links
         13.3 Register Synchronization

27.5.2.4 Write Access Protection Management
         Peripheral access control can be enabled or disabled by writing to the WRCTRL register.
         The data written to the WRCTRL register is composed of two fields; WRCTRL.PERID and WRCTRL.KEY.
         The WRCTRL.PERID is an unique identifier corresponding to a peripheral. The WRCTRL.KEY is a key




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 727
                                                            SAM D5x/E5x Family Data Sheet
                                                                        PAC - Peripheral Access Controller

         value that defines the operation to be done on the control access bit. These operations can be “clear
         protection”, “set protection” and “set and lock protection bit”.
         The “clear protection” operation will remove the write access protection for the peripheral selected by
         WRCTRL.PERID. Write accesses are allowed for the registers in this peripheral.
         The “set protection” operation will set the write access protection for the peripheral selected by
         WRCTRL.PERID. Write accesses are not allowed for the registers with write protection property in this
         peripheral.
         The “set and lock protection” operation will set the write access protection for the peripheral selected by
         WRCTRL.PERID and locks the access rights of the selected peripheral registers. The write access
         protection will only be cleared by a hardware reset.
         The peripheral access control status can be read from the corresponding STATUSn register.
27.5.2.5 Write Access Protection Management Errors
         Only word-wise writes to the WRCTRL register will effectively change the access protection. Other type of
         accesses will have no effect and will cause a PAC write access error. This error is reported in the
         INTFLAGn.PAC bit corresponding to the PAC module.
         PAC also offers an additional safety feature for correct program execution with an interrupt generated on
         double write clear protection or double write set protection. If a peripheral is write protected and a
         subsequent set protection operation is detected then the PAC returns an error, and similarly for a double
         clear protection operation.
         In addition, an error is generated when writing a “set and lock” protection to a write-protected peripheral
         or when a write access is done to a locked set protection. This can be used to ensure that the application
         follows the intended program flow by always following a write protect with an unprotect and conversely.
         However in applications where a write protected peripheral is used in several contexts, e.g. interrupt, care
         should be taken so that either the interrupt can not happen while the main application or other interrupt
         levels manipulates the write protection status or when the interrupt handler needs to unprotect the
         peripheral based on the current protection status by reading the STATUS register.
         The errors generated while accessing the PAC module registers (eg. key error, double protect error...) will
         set the INTFLAGn.PAC flag.
27.5.2.6 AHB Slave Bus Errors
         The PAC module reports errors occurring at the AHB Slave bus level. These errors are generated when
         an access is performed at an address where no slave (bridge or peripheral) is mapped . These errors are
         reported in the corresponding bits of the INTFLAGAHB register.
27.5.2.7 Generating Events
         The PAC module can also generate an event when any of the Interrupt Flag registers bit are set. To
         enable the PAC event generation, the control bit EVCTRL.ERREO must be set a '1'.

27.5.3   DMA Operation
         Not applicable.

27.5.4   Interrupts
         The PAC has the following interrupt source:
           • Error (ERR): Indicates that a peripheral access violation occurred in one of the peripherals controlled
             by the PAC module, or a bridge error occurred in one of the bridges reported by the PAC
              – This interrupt is a synchronous wake-up source.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 728
                                                            SAM D5x/E5x Family Data Sheet
                                                                         PAC - Peripheral Access Controller

         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAGAHB and INTFLAGn) registers is set when the interrupt condition occurs. Each
         interrupt can be individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable Set
         (INTENSET) register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable Clear
         (INTENCLR) register. An interrupt request is generated when the interrupt flag is set and the
         corresponding interrupt is enabled. The interrupt request remains active until the interrupt flag is cleared,
         the interrupt is disabled, or the PAC is reset. All interrupt requests from the peripheral are ORed together
         on system level to generate one combined interrupt request to the NVIC. The user must read the
         INTFLAGAHB and INTFLAGn registers to determine which interrupt condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated.
         Related Links
         10.2 Nested Vector Interrupt Controller

27.5.5   Events
         The PAC can generate the following output event:
          • Error (ERR): Generated when one of the interrupt flag registers bits is set
         Writing a '1' to an Event Output bit in the Event Control Register (EVCTRL.ERREO) enables the
         corresponding output event. Writing a '0' to this bit disables the corresponding output event.

27.5.6   Sleep Mode Operation
         In Sleep mode, the PAC is kept enabled if an available bus master (CPU, DMA) is running. The PAC will
         continue to catch access errors from the module and generate interrupts or events.

27.5.7   Synchronization
         Not applicable.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 729
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                PAC - Peripheral Access Controller


27.6      Register Summary

 Offset        Name        Bit Pos.

                              7:0                                          PERID[7:0]
                             15:8                                          PERID[15:8]
 0x00        WRCTRL
                             23:16                                             KEY[7:0]
                             31:24
 0x04         EVCTRL          7:0                                                                                       ERREO
 0x05
   ...       Reserved
 0x07
 0x08        INTENCLR         7:0                                                                                        ERR
 0x09        INTENSET         7:0                                                                                        ERR
 0x0A
   ...       Reserved
 0x0F
                                               RAMDMACIC
                              7:0      HPB0                RAMDMAWR RAMPPPDSU RAMCM4S            NVMCTRL2   NVMCTRL1   NVMCTRL0
                                                  M
 0x10       INTFLAGAHB       15:8                QSPI       SDHC1       SDHC0         PUKCC        HPB3       HPB2       HPB1
                             23:16
                             31:24
                                                           OSC32KCTR
                              7:0      GCLK      SUPC                  OSCCTRL        RSTC        MCLK        PM         PAC
                                                               L
 0x14        INTFLAGA        15:8       TC1       TC0      SERCOM1     SERCOM0        FREQM        EIC        RTC        WDT
                             23:16
                             31:24
                              7:0      EVSYS                 DMAC       PORT          CMCC       NVMCTRL      DSU        USB
                             15:8                 TC3         TC2       TCC1              TCC0   SERCOM3    SERCOM2
 0x18        INTFLAGB
                             23:16                                                                                     RAMECC
                             31:24
                              7:0      PDEC       TC5         TC4       TCC3              TCC2    GMAC        CAN1       CAN0
                             15:8                 CCL        QSPI       PUKCC             ICM     TRNG        AES
 0x1C        INTFLAGC
                             23:16
                             31:24
                              7:0      ADC0       TC7         TC6       TCC4        SERCOM7      SERCOM6    SERCOM5    SERCOM4
                             15:8                                                         PCC      I2S        DAC        ADC1
 0x20        INTFLAGD
                             23:16
                             31:24
 0x24
   ...       Reserved
 0x33
                                                           OSC32KCTR
                              7:0      GCLK      SUPC                  OSCCTRL        RSTC        MCLK        PM         PAC
                                                               L
 0x34        STATUSA         15:8       TC1       TC0      SERCOM1     SERCOM0        FREQM        EIC                   WDT
                             23:16
                             31:24




          © 2019 Microchip Technology Inc.                          Datasheet                               DS60001507E-page 730
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                PAC - Peripheral Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0      EVSYS              DMAC       PORT       CMCC    NVMCTRL      DSU        USB
                                 15:8               TC3       TC2        TCC1       TCC0    SERCOM3    SERCOM2
   0x38            STATUSB
                                 23:16                                                                            RAMECC
                                 31:24
                                  7:0      PDEC     TC5       TC4        TCC3       TCC2      GMAC       CAN1       CAN0
                                 15:8               CCL       QSPI      PUKCC       ICM       TRNG       AES         AC
   0x3C            STATUSC
                                 23:16
                                 31:24
                                  7:0      ADC0     TC7       TC6        TCC4     SERCOM7   SERCOM6    SERCOM5    SERCOM4
                                 15:8                                               PCC        I2S       DAC        ADC1
   0x40            STATUSD
                                 23:16
                                 31:24




27.7           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to the related links.
               Related Links
               13.3 Register Synchronization




              © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 731
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                     PAC - Peripheral Access Controller

27.7.1         Write Control

               Name:        WRCTRL
               Offset:      0x00
               Reset:       0x00000000
               Property:    –


         Bit        31            30           29            28                 27          26         25          24


   Access
    Reset


         Bit        23            22           21            20                 19          18         17          16
                                                                   KEY[7:0]
   Access           RW           RW            RW           RW                  RW          RW        RW          RW
    Reset            0            0             0            0                  0            0         0           0


         Bit        15            14           13            12                 11          10         9           8
                                                                  PERID[15:8]
   Access           RW           RW            RW           RW                  RW          RW        RW          RW
    Reset            0            0             0            0                  0            0         0           0


         Bit         7            6             5            4                  3            2         1           0
                                                                  PERID[7:0]
   Access           RW           RW            RW           RW                  RW          RW        RW          RW
    Reset            0            0             0            0                  0            0         0           0


               Bits 23:16 – KEY[7:0] Peripheral Access Control Key
               These bits define the peripheral access control key:
                Value      Name       Description
                0x0        OFF        No action
                0x1        CLEAR Clear the peripheral write control
                0x2        SET        Set the peripheral write control
                0x3        LOCK       Set and lock the peripheral write control until the next hardware reset

               Bits 15:0 – PERID[15:0] Peripheral Identifier
               The PERID represents the peripheral whose control is changed using the WRCTRL.KEY. The Peripheral
               Identifier is calculated following formula:
               ����� = 32* BridgeNumber + N
               Where BridgeNumber represents the Peripheral Bridge Number (0 for Peripheral Bridge A, 1 for
               Peripheral Bridge B, etc). N represents the peripheral index from the respective Bridge Number:
               Table 27-2. PERID Values

               Periph. Bridge Name                  BridgeNumber                            PERID Values
               A                                    0                                       0+N
               B                                    1                                       32+N
               C                                    2                                       64+N




           © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 732
                                             SAM D5x/E5x Family Data Sheet
                                                      PAC - Peripheral Access Controller

...........continued
 Periph. Bridge Name               BridgeNumber              PERID Values
 D                                 3                         96+N
 E                                 4                         128+N




© 2019 Microchip Technology Inc.              Datasheet                 DS60001507E-page 733
                                                                SAM D5x/E5x Family Data Sheet
                                                                             PAC - Peripheral Access Controller

27.7.2         Event Control

               Name:       EVCTRL
               Offset:     0x04
               Reset:      0x00
               Property:   -


         Bit         7            6            5            4            3             2            1            0
                                                                                                              ERREO
   Access                                                                                                       RW
    Reset                                                                                                        0


               Bit 0 – ERREO Peripheral Access Error Event Output
               This bit indicates if the Peripheral Access Error Event Output is enabled or disabled. When enabled, an
               event will be generated when one of the interrupt flag registers bits (INTFLAGAHB, INTFLAGn) is set:
                Value       Description
                0            Peripheral Access Error Event Output is disabled.
                1            Peripheral Access Error Event Output is enabled.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 734
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                PAC - Peripheral Access Controller

27.7.3         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x08
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit         7             6            5             4             3             2             1             0
                                                                                                                    ERR
   Access                                                                                                            RW
    Reset                                                                                                             0


               Bit 0 – ERR Peripheral Access Error Interrupt Disable
               This bit indicates that the Peripheral Access Error Interrupt is disabled and an interrupt request will be
               generated when one of the interrupt flag registers bits (INTFLAGAHB, INTFLAGn) is set:
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Peripheral Access Error interrupt Enable bit and disables the
               corresponding interrupt request.
                Value        Description
                0            Peripheral Access Error interrupt is disabled.
                1            Peripheral Access Error interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 735
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                PAC - Peripheral Access Controller

27.7.4         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x09
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENCLR).

         Bit         7             6            5             4             3            2             1             0
                                                                                                                   ERR
   Access                                                                                                           RW
    Reset                                                                                                            0


               Bit 0 – ERR Peripheral Access Error Interrupt Enable
               This bit indicates that the Peripheral Access Error Interrupt is enabled and an interrupt request will be
               generated when one of the interrupt flag registers bits (INTFLAGAHB, INTFLAGn) is set:
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Peripheral Access Error interrupt Enable bit and enables the
               corresponding interrupt request.
                Value        Description
                0            Peripheral Access Error interrupt is disabled.
                1            Peripheral Access Error interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 736
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                PAC - Peripheral Access Controller

27.7.5         Bridge Interrupt Flag Status

               Name:        INTFLAGAHB
               Offset:      0x10
               Reset:       0x00000000
               Property:    -

               These flags are cleared by writing a '1' to the corresponding bit.
               These flags are set when an access error is detected by the corresponding AHB slave, and will generate
               an interrupt request if INTENCLR/SET.ERR is '1'.

         Bit        31            30            29            28           27          26           25           24


   Access
    Reset


         Bit        23            22            21            20           19          18           17           16


   Access
    Reset


         Bit        15            14            13            12           11          10           9            8
                                 QSPI         SDHC1        SDHC0         PUKCC        HPB3        HPB2          HPB1
   Access                         RW           RW            RW            RW          RW          RW           RW
    Reset                          0            0             0             0           0           0            0


         Bit         7             6            5             4             3           2           1            0
                   HPB0      RAMDMACICM RAMDMAWR         RAMPPPDSU      RAMCM4S     NVMCTRL2    NVMCTRL1     NVMCTRL0
   Access           RW            RW           RW            RW            RW          RW          RW           RW
    Reset            0             0            0             0             0           0           0            0


               Bit 14 – QSPI Interrupt Flag for QSPI
               This flag is set when an access error is detected by the QSPI AHB slave, and will generate an interrupt
               request if INTENCLR/SET.ERR is '1'.
               Writing a '0' has no effect.
               Writing a '1' to this bit will clear the QSPI interrupt flag.

               Bit 13 – SDHC1 Interrupt Flag for SDHC1
               This flag is set when an access error is detected by the SDHC1 AHB slave, and will generate an interrupt
               request if INTENCLR/SET.ERR is '1'.
               Writing a '0' has no effect.
               Writing a '1' to this bit will clear the SDHC1 interrupt flag.

               Bit 12 – SDHC0 Interrupt Flag for SDHC0
               This flag is set when an access error is detected by the SDHC0 AHB slave, and will generate an interrupt
               request if INTENCLR/SET.ERR is '1'.
               Writing a '0' has no effect.
               Writing a '1' to this bit will clear the SDHC0 interrupt flag.




           © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 737
                                                 SAM D5x/E5x Family Data Sheet
                                                             PAC - Peripheral Access Controller

Bit 11 – PUKCC Interrupt Flag for PUKCC
This flag is set when an access error is detected by the PUKCC AHB slave, and will generate an interrupt
request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the PUKCC interrupt flag.

Bit 10 – HPB3 Interrupt Flag for HPB3
This flag is set when an access error is detected by the HPB3 AHB slave, and will generate an interrupt
request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the HPB3 interrupt flag.

Bit 9 – HPB2 Interrupt Flag for HPB2
This flag is set when an access error is detected by the HPB2 AHB slave, and will generate an interrupt
request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the HPB2 interrupt flag.

Bit 8 – HPB1 Interrupt Flag for HPB1
This flag is set when an access error is detected by the HPB1 AHB slave, and will generate an interrupt
request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the HPB1 interrupt flag.

Bit 7 – HPB0 Interrupt Flag for HPB0
This flag is set when an access error is detected by the HPB0 AHB slave, and will generate an interrupt
request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the HPB0 interrupt flag.

Bit 6 – RAMDMACICM Interrupt Flag for RAMDMACICM
This flag is set when an access error is detected by the RAMDMACICM AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the RAMDMACICM interrupt flag.

Bit 5 – RAMDMAWR Interrupt Flag for RAMDMAWR
This flag is set when an access error is detected by the RAMDMAWR AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the RAMDMAWR interrupt flag.

Bit 4 – RAMPPPDSU Interrupt Flag for RAMPPPDSU:
This flag is set when an access error is detected by the RAMPPPDSU AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the RAMPPPDSU interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 738
                                               SAM D5x/E5x Family Data Sheet
                                                           PAC - Peripheral Access Controller

Bit 3 – RAMCM4S Interrupt Flag for RAMCM4S
This flag is set when an access error is detected by the RAMCM4S AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the RAMCM4S interrupt flag.

Bit 2 – NVMCTRL2 Interrupt Flag for NVMCTRL2
This flag is set when an access error is detected by the NVMCTRL2 AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the NVMCTRL2 interrupt flag.

Bit 1 – NVMCTRL1 Interrupt Flag for NVMCTRL1
This flag is set when an access error is detected by the NVMCTRL1 AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the NVMCTRL1 interrupt flag.

Bit 0 – NVMCTRL0 Interrupt Flag for NVMCTRL0
This flag is set when an access error is detected by the NVMCTRL0 AHB slave, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' has no effect.
Writing a '1' to this bit will clear the NVMCTRL0 interrupt flag.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 739
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                 PAC - Peripheral Access Controller

27.7.6         Peripheral Interrupt Flag Status - Bridge A

               Name:        INTFLAGA
               Offset:      0x14
               Reset:       0x00000000
               Property:    –

               These flags are set when a Peripheral Access Error occurs while accessing the peripheral associated
               with the respective INTFLAGx bit, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the corresponding INTFLAGx interrupt flag.

         Bit         31            30             29          28            27           26        25           24


   Access
    Reset


         Bit         23            22             21          20            19           18        17           16


   Access
    Reset


         Bit         15            14             13          12            11           10         9            8
                    TC1           TC0          SERCOM1      SERCOM0       FREQM          EIC       RTC         WDT
   Access           RW            RW             RW           RW           RW            RW        RW           RW
    Reset            0              0             0            0            0             0         0            0


         Bit         7              6             5            4            3             2         1            0
                   GCLK          SUPC         OSC32KCTRL    OSCCTRL       RSTC          MCLK       PM          PAC
   Access           RW            RW             RW           RW           RW            RW        RW           RW
    Reset            0              0             0            0            0             0         0            0


               Bit 15 – TC1 Interrupt Flag for TC1
               This bit is set when a Peripheral Access Error occurs while accessing the TC1, and will generate an
               interrupt request if SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the flag.

               Bit 14 – TC0 Interrupt Flag for TC0
               This bit is set when a Peripheral Access Error occurs while accessing the TC0, and will generate an
               interrupt request if SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the flag.

               Bit 13 – SERCOM1 Interrupt Flag for SERCOM1
               This bit is set when a Peripheral Access Error occurs while accessing the SERCOM1, and will generate
               an interrupt request if SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the flag.




           © 2019 Microchip Technology Inc.                           Datasheet                     DS60001507E-page 740
                                                 SAM D5x/E5x Family Data Sheet
                                                             PAC - Peripheral Access Controller

Bit 12 – SERCOM0 Interrupt Flag for SERCOM0
This bit is set when a Peripheral Access Error occurs while accessing the SERCOM0, and will generate
an interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 11 – FREQM Interrupt Flag for FREQM
This bit is set when a Peripheral Access Error occurs while accessing the FREQM, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 10 – EIC Interrupt Flag for EIC
This bit is set when a Peripheral Access Error occurs while accessing the EIC, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 9 – RTC Interrupt Flag for RTC
This bit is set when a Peripheral Access Error occurs while accessing the RTC, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 8 – WDT Interrupt Flag for WDT
This bit is set when a Peripheral Access Error occurs while accessing the WDT, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 7 – GCLK Interrupt Flag for GCLK
This bit is set when a Peripheral Access Error occurs while accessing the GCLK, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 6 – SUPC Interrupt Flag for SUPC
This bit is set when a Peripheral Access Error occurs while accessing the SUPC, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 5 – OSC32KCTRL Interrupt Flag for OSC32KCTRL
This bit is set when a Peripheral Access Error occurs while accessing the OSC32KCTRL, and will
generate an interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 741
                                                 SAM D5x/E5x Family Data Sheet
                                                            PAC - Peripheral Access Controller

Bit 4 – OSCCTRL Interrupt Flag for OSCCTRL
This bit is set when a Peripheral Access Error occurs while accessing the OSCCTRL, and will generate
an interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 3 – RSTC Interrupt Flag for RSTC
This bit is set when a Peripheral Access Error occurs while accessing the RSTC, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 2 – MCLK Interrupt Flag for MCLK
This bit is set when a Peripheral Access Error occurs while accessing the MCLK, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 1 – PM Interrupt Flag for PM
This bit is set when a Peripheral Access Error occurs while accessing the PM, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.

Bit 0 – PAC Interrupt Flag for PAC
This bit is set when a Peripheral Access Error occurs while accessing the PAC, and will generate an
interrupt request if SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the flag.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 742
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                 PAC - Peripheral Access Controller

27.7.7         Peripheral Interrupt Flag Status - Bridge B

               Name:        INTFLAGB
               Offset:      0x18
               Reset:       0x00000000
               Property:    –

               These flags are set when a Peripheral Access Error occurs while accessing the peripheral associated
               with the respective INTFLAGx bit, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the corresponding INTFLAGx interrupt flag.

         Bit         31            30            29           28            27           26          25           24


   Access
    Reset


         Bit         23            22            21           20            19           18          17           16
                                                                                                               RAMECC
   Access                                                                                                        RW
    Reset                                                                                                         0


         Bit         15            14            13           12            11           10           9           8
                                  TC3            TC2        TCC1          TCC0        SERCOM3      SERCOM2
   Access                         RW             RW          RW            RW            RW          RW
    Reset                           0             0           0             0             0           0


         Bit         7              6             5           4             3             2           1           0
                  EVSYS                         DMAC        PORT          CMCC        NVMCTRL        DSU         USB
   Access           RW                           RW          RW            RW            RW          RW          RW
    Reset            0                            0           0             0             0           0           0


               Bit 16 – RAMECC Interrupt Flag for RAMECC
               This flag is set when a Peripheral Access Error occurs while accessing the RAMECC, and will generate
               an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the RAMECC interrupt flag.

               Bit 14 – TC3 Interrupt Flag for TC3
               This flag is set when a Peripheral Access Error occurs while accessing the TC3, and will generate an
               interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the TC3 interrupt flag.

               Bit 13 – TC2 Interrupt Flag for TC2
               This flag is set when a Peripheral Access Error occurs while accessing the TC2, and will generate an
               interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the TC2 interrupt flag.




           © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 743
                                                SAM D5x/E5x Family Data Sheet
                                                            PAC - Peripheral Access Controller

Bit 12 – TCC1 Interrupt Flag for TCC1
This flag is set when a Peripheral Access Error occurs while accessing the TCC1, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TCC1 interrupt flag.

Bit 11 – TCC0 Interrupt Flag for TCC0
This flag is set when a Peripheral Access Error occurs while accessing the TCC0, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TCC0 interrupt flag.

Bit 10 – SERCOM3 Interrupt Flag for SERCOM3
This flag is set when a Peripheral Access Error occurs while accessing the SERCOM3, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the SERCOM3 interrupt flag.

Bit 9 – SERCOM2 Interrupt Flag for SERCOM2
This flag is set when a Peripheral Access Error occurs while accessing the SERCOM2, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the SERCOM2 interrupt flag.

Bit 7 – EVSYS Interrupt Flag for EVSYS
This flag is set when a Peripheral Access Error occurs while accessing the EVSYS, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the EVSYS interrupt flag.

Bit 5 – DMAC Interrupt Flag for DMAC
This flag is set when a Peripheral Access Error occurs while accessing the DMAC, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the DMAC interrupt flag.

Bit 4 – PORT Interrupt Flag for PORT
This flag is set when a Peripheral Access Error occurs while accessing the PORT, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the PORT interrupt flag.

Bit 3 – CMCC Interrupt Flag for CMCC
This flag is set when a Peripheral Access Error occurs while accessing the CMCC, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the CMCC interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 744
                                                SAM D5x/E5x Family Data Sheet
                                                            PAC - Peripheral Access Controller

Bit 2 – NVMCTRL Interrupt Flag for NVMCTRL
This flag is set when a Peripheral Access Error occurs while accessing the NVMCTRL, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the NVMCTRL interrupt flag.

Bit 1 – DSU Interrupt Flag for DSU
This flag is set when a Peripheral Access Error occurs while accessing the DSU, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the DSU interrupt flag.

Bit 0 – USB Interrupt Flag for USB
This flag is set when a Peripheral Access Error occurs while accessing the USB, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the USB interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 745
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                 PAC - Peripheral Access Controller

27.7.8         Peripheral Interrupt Flag Status - Bridge C

               Name:        INTFLAGC
               Offset:      0x1C
               Reset:       0x00000000
               Property:    –

               These flags are set when a Peripheral Access Error occurs while accessing the peripheral associated
               with the respective INTFLAGx bit, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the corresponding INTFLAGx interrupt flag.

         Bit         31            30            29           28            27           26         25          24


   Access
    Reset


         Bit         23            22            21           20            19           18         17          16


   Access
    Reset


         Bit         15            14            13           12            11           10         9            8
                                  CCL           QSPI        PUKCC          ICM          TRNG       AES
   Access                         RW             RW          RW            RW            RW        RW
    Reset                           0             0           0             0             0         0


         Bit         7              6             5           4             3             2         1            0
                   PDEC           TC5            TC4        TCC3          TCC2          GMAC       CAN1        CAN0
   Access           RW            RW             RW          RW            RW            RW        RW           RW
    Reset            0              0             0           0             0             0         0            0


               Bit 14 – CCL Interrupt Flag for CCL
               This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
               the CCL, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the CCL interrupt flag.

               Bit 13 – QSPI Interrupt Flag for QSPI
               This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
               the QSPI, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the QSPI interrupt flag.

               Bit 12 – PUKCC Interrupt Flag for PUKCC
               This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
               the PUKCC, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the PUKCC interrupt flag.




           © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 746
                                                 SAM D5x/E5x Family Data Sheet
                                                             PAC - Peripheral Access Controller

Bit 11 – ICM Interrupt Flag for ICM
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the ICM, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the ICM interrupt flag.

Bit 10 – TRNG Interrupt Flag for TRNG
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the TRNG, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TRNG interrupt flag.

Bit 9 – AES Interrupt Flag for AES
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the AES, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the AES interrupt flag.

Bit 7 – PDEC Interrupt Flag for PDEC
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the PDEC, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the PDEC interrupt flag.

Bit 6 – TC5 Interrupt Flag for TC5
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the TC5, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TC5 interrupt flag.

Bit 5 – TC4 Interrupt Flag for TC4
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the TC4, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TC4 interrupt flag.

Bit 4 – TCC3 Interrupt Flag for TCC3
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the TCC3, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TCC3 interrupt flag.

Bit 3 – TCC2 Interrupt Flag for TCC2
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the TCC2, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the TCC2 interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 747
                                                 SAM D5x/E5x Family Data Sheet
                                                             PAC - Peripheral Access Controller

Bit 2 – GMAC Interrupt Flag for GMAC
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the GMAC, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the GMAC interrupt flag.

Bit 1 – CAN1 Interrupt Flag for CAN1
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the CAN1, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the CAN1 interrupt flag.

Bit 0 – CAN0 Interrupt Flag for CAN0
This flags is set when a Peripheral Access Error occurs while accessing the peripheral associated with
the CAN0, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the CAN0 interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 748
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                 PAC - Peripheral Access Controller

27.7.9         Peripheral Interrupt Flag Status - Bridge D

               Name:        INTFLAGD
               Offset:      0x20
               Reset:       0x00000000
               Property:    –

               These flags are set when a Peripheral Access Error occurs while accessing the peripheral associated
               with the respective INTFLAGx bit, and will generate an interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the corresponding INTFLAGx interrupt flag.

         Bit         31            30            29           28            27           26          25           24


   Access
    Reset


         Bit         23            22            21           20            19           18          17           16


   Access
    Reset


         Bit         15            14            13           12            11           10           9           8
                                                                           PCC           I2S         DAC        ADC1
   Access                                                                  RW            RW          RW          RW
    Reset                                                                   0             0           0           0


         Bit         7              6             5           4             3             2           1           0
                   ADC0           TC7            TC6        TCC4        SERCOM7       SERCOM6      SERCOM5    SERCOM4
   Access           RW            RW             RW          RW            RW            RW          RW          RW
    Reset            0              0             0           0             0             0           0           0


               Bit 11 – PCC Interrupt Flag for PCC
               This flag is set when a Peripheral Access Error occurs while accessing the PCC, and will generate an
               interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the PCC interrupt flag.

               Bit 10 – I2S Interrupt Flag for I2S
               This flag is set when a Peripheral Access Error occurs while accessing the I2S, and will generate an
               interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the I2S interrupt flag.

               Bit 9 – DAC Interrupt Flag for DAC
               This flag is set when a Peripheral Access Error occurs while accessing the DAC, and will generate an
               interrupt request if INTENCLR/SET.ERR is '1'.
               Writing a '0' to these bits has no effect.
               Writing a '1' to these bits will clear the DAC interrupt flag.




           © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 749
                                                SAM D5x/E5x Family Data Sheet
                                                            PAC - Peripheral Access Controller

Bit 8 – ADC1 Interrupt Flag for ADC1
This flag is set when a Peripheral Access Error occurs while accessing the ADC1, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the ADC1 interrupt flag.

Bit 7 – ADC0 Interrupt Flag for ADC0
This flag is set when a Peripheral Access Error occurs while accessing the ADC0, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the ADC0 interrupt flag.

Bit 6 – TC7 Interrupt Flag for TC7
This flag is set when a Peripheral Access Error occurs while accessing the TC6, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the TC7 interrupt flag.

Bit 5 – TC6 Interrupt Flag for TC6
This flag is set when a Peripheral Access Error occurs while accessing the TC6, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the TC6 interrupt flag.

Bit 4 – TCC4 Interrupt Flag for TCC4
This flag is set when a Peripheral Access Error occurs while accessing the TCC4, and will generate an
interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the TCC4 interrupt flag.

Bit 3 – SERCOM7 Interrupt Flag for SERCOM7
This flag is set when a Peripheral Access Error occurs while accessing the SERCOM7, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the SERCOM7 interrupt flag.

Bit 2 – SERCOM6 Interrupt Flag for SERCOM6
This flag is set when a Peripheral Access Error occurs while accessing the SERCOM6, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the SERCOM6 interrupt flag.

Bit 1 – SERCOM5 Interrupt Flag for SERCOM5
This flag is set when a Peripheral Access Error occurs while accessing the SERCOM5, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the SERCOM5 interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 750
                                               SAM D5x/E5x Family Data Sheet
                                                           PAC - Peripheral Access Controller

Bit 0 – SERCOM4 Interrupt Flag for SERCOM4
This flag is set when a Peripheral Access Error occurs while accessing the SERCOM4, and will generate
an interrupt request if INTENCLR/SET.ERR is '1'.
Writing a '0' to these bits has no effect.
Writing a '1' to these bits will clear the SERCOM4 interrupt flag.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 751
                                                                  SAM D5x/E5x Family Data Sheet
                                                                             PAC - Peripheral Access Controller

27.7.10 Peripheral Write Protection Status A

            Name:        STATUSA
            Offset:      0x34
            Reset:       0x00010000
            Property:    PAC Write-Protection

            Writing to this register has no effect.
            Reading STATUS register returns peripheral write protection status:

            Value                Description
            0                    Peripheral is not write protected.
            1                    Peripheral is write protected.

      Bit         31            30             29          28           27          26        25           24


  Access
   Reset


      Bit         23            22             21          20           19          18        17           16


  Access
   Reset


      Bit         15            14             13          12           11          10         9           8
                 TC1           TC0          SERCOM1     SERCOM0       FREQM         EIC                   WDT
  Access          R             R              R            R           R            R                     R
   Reset          0             0              0            0           0            0                     0


      Bit         7             6              5            4           3            2         1           0
                GCLK          SUPC         OSC32KCTRL   OSCCTRL       RSTC         MCLK       PM          PAC
  Access          R             R              R            R           R            R         R           R
   Reset          0             0              0            0           0            0         0           0


            Bit 15 – TC1 TC1 APB Protect Enable
            Value      Description
            0          TC1 is not write protected
            1          TC1 is write protected

            Bit 14 – TC0 TC0 APB Protect Enable
            Value      Description
            0          TC0 is not write protected
            1          TC0 is write protected

            Bit 13 – SERCOM1 SERCOM1 APB Protect Enable
            Value      Description
            0          SERCOM1 is not write protected
            1          SERCOM1 is write protected




        © 2019 Microchip Technology Inc.                          Datasheet                    DS60001507E-page 752
                                          SAM D5x/E5x Family Data Sheet
                                                     PAC - Peripheral Access Controller

Bit 12 – SERCOM0 SERCOM0 APB Protect Enable
Value      Description
0          SERCOM0 is not write protected
1          SERCOM0 is write protected

Bit 11 – FREQM FREQM APB Protect Enable
Value      Description
0          FREQM is not write protected
1          FREQM is write protected

Bit 10 – EIC EIC APB Protect Enable
Value       Description
0           EIC is not write protected
1           EIC is write protected

Bit 8 – WDT WDT APB Protect Enable
Value      Description
0          WDT is not write protected
1          WDT is write protected

Bit 7 – GCLK GCLK APB Protect Enable
Value      Description
0          GCLK is not write protected
1          GCLK is write protected

Bit 6 – SUPC SUPC APB Protect Enable
Value      Description
0          SUPC is not write protected
1          SUPC is write protected

Bit 5 – OSC32KCTRL OSC32KCTRL APB Protect Enable
Value      Description
0          OSC32KCTRL is not write protected
1          OSC32KCTRL is write protected

Bit 4 – OSCCTRL OSCCTRL APB Protect Enable
Value      Description
0          OSCCTRL is not write protected
1          OSCCTRL is write protected

Bit 3 – RSTC RSTC APB Protect Enable
Value      Description
0          RSTC is not write protected
1          RSTC is write protected

Bit 2 – MCLK MCLK APB Protect Enable
Value      Description
0          MCLK is not write protected
1          MCLK is write protected




© 2019 Microchip Technology Inc.             Datasheet                 DS60001507E-page 753
                                        SAM D5x/E5x Family Data Sheet
                                                PAC - Peripheral Access Controller

Bit 1 – PM PM APB Protect Enable
Value      Description
0          PM is not write protected
1          PM is write protected

Bit 0 – PAC PAC APB Protect Enable
Value      Description
0          PAC is not write protected
1          PAC is write protected




© 2019 Microchip Technology Inc.        Datasheet                 DS60001507E-page 754
                                                                  SAM D5x/E5x Family Data Sheet
                                                                             PAC - Peripheral Access Controller

27.7.11 Peripheral Write Protection Status - Bridge B

            Name:        STATUSB
            Offset:      0x38
            Reset:       0x00000002
            Property:    PAC Write-Protection

            Writing to this register has no effect.
            Reading STATUS register returns peripheral write protection status:

            Value                Description
            0                    Peripheral is not write protected.
            1                    Peripheral is write protected.

      Bit         31            30            29           28           27          26        25           24


   Access
    Reset


      Bit         23            22            21           20           19          18        17           16
                                                                                                        RAMECC
   Access                                                                                                  R
    Reset                                                                                                  0


      Bit         15            14            13           12           11          10         9           8
                               TC3           TC2          TCC1         TCC0       SERCOM3   SERCOM2
   Access                       R              R            R           R            R         R
    Reset                       0              0            0           0            0         0


      Bit         7             6              5            4           3            2         1           0
                EVSYS                       DMAC          PORT        CMCC        NVMCTRL     DSU         USB
   Access         R                            R            R           R            R         R           R
    Reset         0                            0            0           0            0         1           0


            Bit 16 – RAMECC RAMECC APB Protect Enable
            Value      Description
            0          RAMECC peripheral is not write protected
            1          RAMECC peripheral is write protected

            Bit 14 – TC3 TC3 APB Protect Enable
            Value      Description
            0          TC3 peripheral is not write protected
            1          TC3 peripheral is write protected

            Bit 13 – TC2 TC2 APB Protect Enable
            Value      Description
            0          TC2 peripheral is not write protected
            1          TC2 peripheral is write protected




        © 2019 Microchip Technology Inc.                          Datasheet                    DS60001507E-page 755
                                                   SAM D5x/E5x Family Data Sheet
                                                            PAC - Peripheral Access Controller

Bit 12 – TCC1 TCC1 APB Protect Enable
Value      Description
0          TCC1 peripheral is not write protected
1          TCC1 peripheral is write protected

Bit 11 – TCC0 TCC0 APB Protect Enable
Value      Description
0          TCC0 peripheral is not write protected
1          TCC0 peripheral is write protected

Bit 10 – SERCOM3 SERCOM3 APB Protect Enable
Value      Description
0          SERCOM3 peripheral is not write protected
1          SERCOM3 peripheral is write protected

Bit 9 – SERCOM2 SERCOM2 APB Protect Enable
Value      Description
0          SERCOM2 peripheral is not write protected
1          SERCOM2 peripheral is write protected

Bit 7 – EVSYS EVSYS APB Protect Enable
Value      Description
0          EVSYS peripheral is not write protected
1          EVSYS peripheral is write protected

Bit 5 – DMAC DMAC APB Protect Enable
Value      Description
0          DMAC peripheral is not write protected
1          DMAC peripheral is write protected

Bit 4 – PORT PORT APB Protect Enable
Value      Description
0          PORT peripheral is not write protected
1          PORT peripheral is write protected

Bit 3 – CMCC CMCC APB Protect Enable
Value      Description
0          CMCC peripheral is not write protected
1          CMCC peripheral is write protected

Bit 2 – NVMCTRL NVMCTRL APB Protect Enable
Value      Description
0          NVMCTRL peripheral is not write protected
1          NVMCTRL peripheral is write protected

Bit 1 – DSU DSU APB Protect Enable
Value      Description
0          DSU peripheral is not write protected
1          DSU peripheral is write protected




© 2019 Microchip Technology Inc.                    Datasheet                 DS60001507E-page 756
                                                   SAM D5x/E5x Family Data Sheet
                                                           PAC - Peripheral Access Controller

Bit 0 – USB USB APB Protect Enable
Value      Description
0          USB peripheral is not write protected
1          USB peripheral is write protected




© 2019 Microchip Technology Inc.                   Datasheet                 DS60001507E-page 757
                                                                  SAM D5x/E5x Family Data Sheet
                                                                             PAC - Peripheral Access Controller

27.7.12 Peripheral Write Protection Status - Bridge C

            Name:        STATUSC
            Offset:      0x3C
            Reset:       0x00000000
            Property:    PAC Write-Protection

            Writing to this register has no effect.
            Reading STATUS register returns peripheral write protection status:

            Value                Description
            0                    Peripheral is not write protected.
            1                    Peripheral is write protected.

      Bit         31            30            29            28          27          26        25           24


   Access
    Reset


      Bit         23            22            21            20          19          18        17           16


   Access
    Reset


      Bit         15            14            13            12          11          10         9           8
                               CCL           QSPI        PUKCC         ICM         TRNG       AES          AC
   Access                       R              R            R           R            R         R           R
    Reset                       0              0            0           0            0         0           0


      Bit         7             6              5            4           3            2         1           0
                PDEC           TC5           TC4           TCC3        TCC2        GMAC      CAN1        CAN0
   Access         R             R              R            R           R            R         R           R
    Reset         0             0              0            0           0            0         0           0


            Bit 14 – CCL CCL APB Protection Enable
            Value      Description
            0          Peripheral is not write protected
            1          Peripheral is write protected

            Bit 13 – QSPI QSPI APB Protection Enable
            Value      Description
            0          Peripheral is not write protected
            1          Peripheral is write protected

            Bit 12 – PUKCC PUKCC APB Protection Enable
            Value      Description
            0          Peripheral is not write protected
            1          Peripheral is write protected




        © 2019 Microchip Technology Inc.                          Datasheet                    DS60001507E-page 758
                                                SAM D5x/E5x Family Data Sheet
                                                        PAC - Peripheral Access Controller

Bit 11 – ICM ICM APB Protection Enable
Value       Description
0           Peripheral is not write protected
1           Peripheral is write protected

Bit 10 – TRNG TRNG APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 9 – AES AES APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 8 – AC AC APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 7 – PDEC PDEC APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 6 – TC5 TC5 APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 5 – TC4 TC4 APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 4 – TCC3 TCC3 APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 3 – TCC2 TCC2 APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 2 – GMAC GMAC APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected




© 2019 Microchip Technology Inc.                Datasheet                 DS60001507E-page 759
                                               SAM D5x/E5x Family Data Sheet
                                                       PAC - Peripheral Access Controller

Bit 1 – CAN1 CAN1 APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected

Bit 0 – CAN0 CAN0 APB Protection Enable
Value      Description
0          Peripheral is not write protected
1          Peripheral is write protected




© 2019 Microchip Technology Inc.               Datasheet                 DS60001507E-page 760
                                                                  SAM D5x/E5x Family Data Sheet
                                                                             PAC - Peripheral Access Controller

27.7.13 Peripheral Write Protection Status - Bridge D

            Name:        STATUSD
            Offset:      0x40
            Reset:       0x00000000
            Property:    PAC Write-Protection, Read-Only

            Writing to this register has no effect.
            Reading STATUS register returns peripheral write protection status:

            Value                Description
            0                    Peripheral is not write protected.
            1                    Peripheral is write protected.

      Bit         31            30            29           28           27          26        25           24


   Access
    Reset


      Bit         23            22            21           20           19          18        17           16


   Access
    Reset


      Bit         15            14            13           12           11          10         9           8
                                                                        PCC         I2S       DAC        ADC1
   Access                                                               R            R         R           R
    Reset                                                                0           0         0           0


      Bit         7             6              5            4            3           2         1           0
                ADC0           TC7           TC6          TCC4        SERCOM7     SERCOM6   SERCOM5    SERCOM4
   Access         R             R              R            R           R            R         R           R
    Reset         0             0              0            0            0           0         0           0


            Bit 11 – PCC PCC APB Protect Enable
            Value      Description
            0          PCC is not write protected
            1          PCC is write protected

            Bit 10 – I2S I2S APB Protect Enable
            Value       Description
            0           I2S is not write protected
            1           I2S is write protected

            Bit 9 – DAC DAC APB Protect Enable
            Value      Description
            0          DAC is not write protected
            1          DAC is write protected




        © 2019 Microchip Technology Inc.                          Datasheet                    DS60001507E-page 761
                                         SAM D5x/E5x Family Data Sheet
                                                 PAC - Peripheral Access Controller

Bit 8 – ADC1 ADC1 APB Protect Enable
Value      Description
0          ADC1 is not write protected
1          ADC1 is write protected

Bit 7 – ADC0 ADC0 APB Protect Enable
Value      Description
0          ADC0 is not write protected
1          ADC0 is write protected

Bit 6 – TC7 TC7 APB Protect Enable
Value      Description
0          TC7 is not write protected
1          TC7 is write protected

Bit 5 – TC6 TC6 APB Protect Enable
Value      Description
0          TC6 is not write protected
1          TC6 is write protected

Bit 4 – TCC4 TCC4 APB Protect Enable
Value      Description
0          TCC4 is not write protected
1          TCC4 is write protected

Bit 3 – SERCOM7 SERCOM7 APB Protect Enable
Value      Description
0          SERCOM7 is not write protected
1          SERCOM7 is write protected

Bit 2 – SERCOM6 SERCOM6 APB Protect Enable
Value      Description
0          SERCOM6 is not write protected
1          SERCOM6 is write protected

Bit 1 – SERCOM5 SERCOM5 APB Protect Enable
Value      Description
0          SERCOM5 is not write protected
1          SERCOM5 is write protected

Bit 0 – SERCOM4 SERCOM4 APB Protect Enable
Value      Description
0          SERCOM4 is not write protected
1          SERCOM4 is write protected




© 2019 Microchip Technology Inc.         Datasheet                 DS60001507E-page 762
