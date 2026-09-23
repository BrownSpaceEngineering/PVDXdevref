# 17. RAMECC – RAM Error Correction Code (ECC)

*Source: `Atmel-SAMD51.pdf`, pages 203-213 — SAMD51 family datasheet*

                                                                   SAM D5x/E5x Family Data Sheet
                                                                 RAMECC – RAM Error Correction Code (ECC)


17.      RAMECC – RAM Error Correction Code (ECC)

17.1     Overview
         Single bit error correction and dual bit error detection is available for RAM.



17.2     Features
           • Single bit correction and dual bit detection.
           • Error Interrupt.



17.3     Block Diagram
         Figure 17-1. RAMECC Block Diagram

                                               Write data
                                                                             ECC
                                                                          calculation
                                                       32
                                                                                    4x5


                                              HADDR

                                            ERRADDR
                                                                 RAM Block




                                                             32               4x5




                                                                  ECC logic
                                                                                           ECCERR and
                                                                                          ECCDUAL status
                                              ECCDIS

                                                            32
                                                                   HRDATA




17.4     Signal Description
         Not applicable.



17.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

17.5.1   I/O Lines
         Not applicable.




         © 2019 Microchip Technology Inc.                            Datasheet                             DS60001507E-page 203
                                                           SAM D5x/E5x Family Data Sheet
                                                         RAMECC – RAM Error Correction Code (ECC)

17.5.2   Power Management
         The RAMECC will continue to operate in any sleep mode where the selected source clock is running. The
         RAMECC’s interrupts can be used to wake up the device from sleep modes. Refer to the Power Manager
         chapter for details on the different sleep modes.
         Related Links
         18. PM – Power Manager

17.5.3   Clocks
         The RAMECC bus clock is provided by the Main Clock Controller (MCLK) through the AHB-APB B bridge.
         The clock is enabled and disabled by writing RAMECC bit the in the APB B Mask register
         (MCLK.APBBMASK.RAMECC). See the register description for the default state of the RAMECC bus
         clock.
         Related Links
         15.6.2.6 Peripheral Clock Masking

17.5.4   DMA
         Not applicable.

17.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the RAMECC interrupt(s) requires
         the interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

17.5.6   Events
         Not applicable.

         Related Links
         31. EVSYS – Event System

17.5.7   Debug Operation
         When the CPU is halted in debug mode the RAMECC will correct and log ECC errors based on the table
         below.
         Table 17-1. ECC Debug Operation

          DBGCTRL.ECCELOG                    DBGCTRL.ECCDIS                      Description
          0                                  0                                   ECC errors from debugger reads
                                                                                 are corrected but not logged in
                                                                                 INTFLAG.
          1                                  0                                   ECC errors from debugger reads
                                                                                 are corrected and logged in
                                                                                 INTFLAG.
          X                                  1                                   ECC errors from debugger reads
                                                                                 are not corrected or logged in
                                                                                 INTFLAG.




         © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 204
                                                            SAM D5x/E5x Family Data Sheet
                                                           RAMECC – RAM Error Correction Code (ECC)

         If the RAMECC is configured in a way that requires it to be periodically serviced by the CPU through
         interrupts or similar, improper operation or data loss may result during debugging.

17.5.8   Register Access Protection
         All registers with write-access are optionally write-protected by the peripheral access controller (PAC),
         except the following registers:
           • Interrupt Flag Status and Clear (INTFLAG) register
           • Status (STATUS) register.
         Write-protection is denoted by the Write-Protected property in the register description.
         Write-protection does not apply to accesses through an external debugger. Refer to the Peripheral
         Access Controller chapter for details.

17.5.9   Analog Connections
         Not applicable.



17.6     Functional Description

17.6.1   Principle of Operation
         Error Correcting Code (ECC) is implemented to detect and correct errors that may arise in the RAM
         arrays. The ECC logic is capable of double error detection and single error correction per 8-bit byte.
         Upon single bit error detection, the Single Bit Error interrupt flag is raised (INTFLAG.SINGLEE). If a dual
         error is detected, the Dual Error interrupt flag (INTFLAG.DUALE) is raised. When the first error is
         detected, the ERRADDR register is frozen with the failing address and remains frozen until
         INTFLAG.DUALE and INTFLAG.SINGLEE are cleared. If a dual bit error occurs while
         INTFLAG.SINGLEE is set, the ERRADDR register is updated with the dual bit error information and
         INTFLAG.DUALE is also set.
         The INTFLAG.SINGLEE and INTFLAG.DUALE bits are both cleared on ERRADDR read.
         The block diagram shows the ECC interface. When ECC is disabled (CTRLA.ECCDIS=1), the ECC field
         in RAM is left unchanged on writes. On reads, ECC errors are not corrected or flagged.
         Related Links
         17.3 Block Diagram

17.6.2   Interrupts
         The RAMECC has the following interrupt sources:
           • Dual Bit Error (DUALE): Indicates that a dual bit error has been detected.
           • Single Bit Error (SINGLEE): Indicates that a single bit error has been detected.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs.
         Each interrupt can be individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Set (INTENSET) register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Clear (INTENCLR) register.




         © 2019 Microchip Technology Inc.                     Datasheet                             DS60001507E-page 205
                                                  SAM D5x/E5x Family Data Sheet
                                                RAMECC – RAM Error Correction Code (ECC)

An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
The interrupt request remains active until the ERRADDR register is read, the interrupt is disabled, or the
RAMECC is reset.
All interrupt requests from the peripheral are ORed together on system level to generate one combined
interrupt request to the NVIC. The user must read the INTFLAG register to determine which interrupt
condition is present.
Note: Interrupts must be globally enabled for interrupt requests to be generated.
Related Links
10.2 Nested Vector Interrupt Controller
17.8.3 INTFLAG




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 206
                                                            SAM D5x/E5x Family Data Sheet
                                                           RAMECC – RAM Error Correction Code (ECC)


17.7      Register Summary

 Offset        Name        Bit Pos.

 0x00        INTENCLR         7:0                                                                  DUALE     SINGLEE
 0x01        INTENSET         7:0                                                                  DUALE     SINGLEE
 0x02        INTFLAG          7:0                                                                  DUALE     SINGLEE
 0x03         STATUS          7:0                                                                             ECCDIS
                              7:0                                     ERRADDR[7:0]
                             15:8                                    ERRADDR[15:8]
 0x04        ERRADDR                                                                                        ERRADDR[16
                             23:16
                                                                                                                :16]
                             31:24
 0x08
   ...       Reserved
 0x0E
 0x0F        DBGCTRL          7:0                                                                 ECCELOG     ECCDIS




17.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 17.5.8 Register Access Protection.




          © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 207
                                                                     SAM D5x/E5x Family Data Sheet
                                                                    RAMECC – RAM Error Correction Code (ECC)

17.8.1         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

         Bit         7              6             5             4              3             2              1             0
                                                                                                         DUALE        SINGLEE
   Access                                                                                                 R/W            R/W
    Reset                                                                                                   0             0


               Bit 1 – DUALE Dual Bit Error Interrupt Enable Clear
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Dual Bit Error Interrupt Enable bit, which disables the Dual Bit Error
               interrupt.
                Value        Description
                0            The Dual Bit Error interrupt is disabled.
                1            The Dual Bit Error interrupt is enabled.

               Bit 0 – SINGLEE Single Bit Error Interrupt Enable Clear
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Single Bit Error Interrupt Enable bit, which disables the Single Bit Error
               interrupt.
                Value        Description
                0            The Single Bit Error interrupt is disabled.
                1            The Single Bit Error interrupt is enabled.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 208
                                                                     SAM D5x/E5x Family Data Sheet
                                                                    RAMECC – RAM Error Correction Code (ECC)

17.8.2         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x01
               Reset:       0x00
               Property:    Write-Protected

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         7              6             5             4              3             2              1             0
                                                                                                         DUALE        SINGLEE
   Access                                                                                                 R/W            R/W
    Reset                                                                                                   0             0


               Bit 1 – DUALE Dual Bit Error Interrupt Enable Set
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Dual Bit Error Interrupt Enable bit, which enables the Dual Bit Error
               interrupt.
                Value        Description
                0            The Dual Bit Error interrupt is disabled.
                1            The Dual Bit Error interrupt is enabled.

               Bit 0 – SINGLEE Single Bit Error Interrupt Enable Set
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Single Bit Error Interrupt Enable bit, which disables the Single Bit Error
               interrupt.
                Value        Description
                0            The Single Bit Error interrupt is disabled.
                1            The Single Bit Error interrupt is enabled.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 209
                                                                   SAM D5x/E5x Family Data Sheet
                                                                  RAMECC – RAM Error Correction Code (ECC)

17.8.3         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x02
               Reset:       0x00


         Bit         7             6            5             4             3             2       1           0
                                                                                                DUALE      SINGLEE
   Access                                                                                        R/W         R/W
    Reset                                                                                         0           0


               Bit 1 – DUALE Dual Bit ECC Error Interrupt
               This flag is set on the occurrence of a dual bit ECC error.
               Writing a '0' to this bit has no effect.
               Reading the ECCADDR register will clear the Dual Bit Error interrupt flag.
                Value        Description
                0            No dual bit errors have been received since the last clear.
                1            At least one dual bit error has occurred since the last clear.

               Bit 0 – SINGLEE Single Bit ECC Error Interrupt
               This flag is set on the occurrence of a single bit ECC error.
               Writing a '0' to this bit has no effect.
               Reading the ECCADDR register will clear the Single Bit Error interrupt flag.
                Value        Description
                0            No errors have been received since the last clear.
                1            At least one single bit error has occurred since the last clear.




           © 2019 Microchip Technology Inc.                         Datasheet                     DS60001507E-page 210
                                                                 SAM D5x/E5x Family Data Sheet
                                                                RAMECC – RAM Error Correction Code (ECC)

17.8.4         Status

               Name:       STATUS
               Offset:     0x03
               Reset:      0x00
               Property:   Read Only, Write-Protected


         Bit         7            6            5            4            3             2            1            0
                                                                                                              ECCDIS
   Access                                                                                                        R
    Reset                                                                                                        0


               Bit 0 – ECCDIS ECC Disable
               This bit is fuse updated at startup. When enabled, the calculated ECC is written to RAM along with data.
               ECC correction and detection is enabled for reads.
                Value        Description
                0            ECC detection and correction is enabled.
                1            ECC detection and correction is disabled.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 211
                                                                     SAM D5x/E5x Family Data Sheet
                                                                    RAMECC – RAM Error Correction Code (ECC)

17.8.5         Error Address

               Name:        ERRADDR
               Offset:      0x04
               Reset:       0x00000000
               Property:    R


         Bit        31             30            29            28            27            26            25            24


   Access
    Reset


         Bit        23             22            21            20            19            18            17            16
                                                                                                                  ERRADDR[16:1
                                                                                                                        6]
   Access
    Reset                                                                                                               0


         Bit        15             14            13            12            11            10             9             8
                                                                ERRADDR[15:8]
   Access
    Reset            0             0             0             0              0             0             0             0


         Bit         7             6             5             4              3             2             1             0
                                                                ERRADDR[7:0]
   Access
    Reset            0             0             0             0              0             0             0             0


               Bits 16:0 – ERRADDR[16:0] ECC Error Address
               The RAM address offset from RAM start that caused an ECC error. If a single bit error is followed by a
               dual bit error, this register will be updated with the address of the dual bit error, otherwise it stalls on the
               first error occurrence. This register will read as zero unless INTFLAG.SINGLEE and/or INTFLAG.DUALE
               are 1.




           © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 212
                                                              SAM D5x/E5x Family Data Sheet
                                                             RAMECC – RAM Error Correction Code (ECC)

17.8.6         Debug Control

               Name:       DBGCTRL
               Offset:     0x0F
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5          4           3           2           1            0
                                                                                          ECCELOG      ECCDIS
   Access                                                                                   R/W          R/W
    Reset                                                                                    0            0


               Bit 1 – ECCELOG ECC Error Log
               When DBGCTRL.ECCDIS=0, This bit controls whether ECC errors are logged in the INTFLAG register.
               When DBGCTRL.ECCDIS=1, this bit has no meaning.
               Value      Description
               0          ECC errors for debugger reads are not logged.
               1          ECC errors for debugger reads are logged if DBGCTRL.ECCDIS=0.

               Bit 0 – ECCDIS ECC Disable
               By default, ECC errors during debugger reads are corrected and logged based on DBGCTRL.ECCELOG.
               Setting this bit will disable ECC correction and logging.
               Value        Description
               0            ECC errors are are corrected for debugger reads and logged based on
                            DBGCTRL.ECCELOG.
               1            ECC errors are masked for debugger reads.




           © 2019 Microchip Technology Inc.                    Datasheet                      DS60001507E-page 213
