# 16. RSTC – Reset Controller

*Source: `Atmel-SAMD51.pdf`, pages 196-202 — SAMD51 family datasheet*

                                                            SAM D5x/E5x Family Data Sheet
                                                                                  RSTC – Reset Controller


16.    RSTC – Reset Controller

16.1   Overview
       The Reset Controller (RSTC) manages the reset of the microcontroller. It issues a microcontroller reset,
       sets the device to its initial state and allows the reset source to be identified by software.



16.2   Features
         • Reset the microcontroller and set it to an initial state according to the reset source
         • Reset cause register for reading the reset source from the application code
         • Multiple reset sources
            – Power supply reset sources: POR, BOD12, BOD33
            – User reset sources: External reset (RESET), Watchdog reset, and System Reset Request
            – Backup exit sources: Real-Time Counter (RTC) and Battery Backup Power Switch (BBPS)



16.3   Block Diagram
       Figure 16-1. Reset System
                           RESET SOURCES      RESET CONTROLLER                   RTC
                                                                          32KHz clock sources
                                   BOD12                                  WDT with ALWAYSON
                                   BOD33                                  GCLK with WRTLOCK
                                     POR

                                                                               Debug Logic
                               RESET

                                     WDT

                                     CPU                                      Other Modules



                              BACKUP EXIT           RCAUSE


                                     RTC           BKUPEXIT
                                     BBPS
                                    SUPC




16.4   Signal Description
        Signal Name                         Type                            Description
        RESET                               Digital input                   External reset

       One signal can be mapped on several pins.




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 196
                                                           SAM D5x/E5x Family Data Sheet
                                                                                     RSTC – Reset Controller

         Related Links
         6. I/O Multiplexing and Considerations



16.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

16.5.1   I/O Lines
         Not applicable.

16.5.2   Power Management
         The Reset Controller module is always on.

16.5.3   Clocks
         The RSTC bus clock (CLK_RSTC_APB) can be enabled and disabled in the Main Clock Controller.
         Related Links
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking

16.5.4   DMA
         Not applicable.

16.5.5   Interrupts
         Not applicable.

16.5.6   Events
         Not applicable.

16.5.7   Debug Operation
         When the CPU is halted in debug mode, the RSTC continues normal operation.

16.5.8   Register Access Protection
         All registers with write access can be optionally write-protected by the Peripheral Access Controller
         (PAC).
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

16.5.9   Analog Connections
         Not applicable.



16.6     Functional Description

16.6.1   Principle of Operation
         The Reset Controller collects the various Reset sources and generates Reset for the device.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 197
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       RSTC – Reset Controller

16.6.2    Basic Operation

16.6.2.1 Initialization
          After a power-on Reset, the RSTC is enabled and the Reset Cause (RCAUSE) register indicates the
          POR source.

16.6.2.2 Enabling, Disabling, and Resetting
          The RSTC module is always enabled.

16.6.2.3 Reset Causes and Effects
          The latest Reset cause is available in RCAUSE register, and can be read during the application boot
          sequence in order to determine proper action.
          These are the groups of Reset sources:
           • Power supply Reset: Resets caused by an electrical issue. It covers POR and BODs Resets
           • User Reset: Resets caused by the application. It covers external Resets, system Reset requests and
             watchdog Resets
           • Backup reset: Resets caused by a Backup Mode exit condition
          The following table lists the parts of the device that are reset, depending on the Reset type.
          Table 16-1. Effects of the Different Reset Causes

                                            Power Supply Reset User Reset
                                            POR, BOD33, BOD12 External Reset WDT Reset, System Reset
                                                                             Request, NVM Reset
          RTC, OSC32KCTRL, RSTC Y                                 N                N
          GCLK with WRTLOCK                 Y                     N                N
          Debug logic                       Y                     Y                N
          Others                            Y                     Y                Y

          The external Reset is generated when pulling the RESET pin low.
          The POR, BOD12, and BOD33 Reset sources are generated by their corresponding module in the
          Supply Controller Interface (SUPC).
          The WDT Reset is generated by the Watchdog Timer.
          The System Reset Request is a Reset generated by the CPU when asserting the SYSRESETREQ bit
                                                                                                ™
          located in the Reset Control register of the CPU (for details refer to the ARM® Cortex Technical
          Reference Manual on http://www.arm.com).
          The NVM Reset is a Reset generated by the NVMCTRL when for example a BKSWRST command is
          performed (for details refer to NVMCTRL chapter).
          From Backup Mode, the chip can be waken-up upon these conditions:
           • Battery Backup Power Switch (BBPS): generated by the SUPC controller when the 3.3V VDDIO is
             restored.
           • Real-Time Counter interrupt. For details refer to the applicable INTFLAG in the RTC for details.
          If one of these conditions is triggered in Backup Mode, the RCAUSE.BACKUP bit is set and the Backup
          Exit Register (BKUPEXIT) is updated.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 198
                                                           SAM D5x/E5x Family Data Sheet
                                                                                     RSTC – Reset Controller

         Note: Refer to the Timing Characteristics section of the Electrical Characteristics chapter.
         Related Links
         20. WDT – Watchdog Timer
         19. SUPC – Supply Controller
         19.6.3 Battery Backup Power Switch

16.6.3   Additional Features
         Not applicable.

16.6.4   DMA Operation
         Not applicable.

16.6.5   Interrupts
         Not applicable.

16.6.6   Events
         Not applicable.

16.6.7   Sleep Mode Operation
         The RSTC module is active in all sleep modes.




         © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 199
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       RSTC – Reset Controller


16.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         RCAUSE          7:0     BACKUP   SYST      WDT        EXT        NVM       BOD33     BOD12       POR
 0x01        Reserved
 0x02        BKUPEXIT         7:0       HIB                                              BBPS       RTC




16.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 16.5.8 Register Access Protection.




          © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 200
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                             RSTC – Reset Controller

16.8.1         Reset Cause

               Name:        RCAUSE
               Offset:      0x00
               Property:    –

               When a Reset occurs, the bit corresponding to the Reset source is set to '1' and all other bits are written
               to '0'.

         Bit         7             6             5             4           3             2             1            0
                  BACKUP         SYST          WDT           EXT          NVM         BOD33         BOD12          POR
   Access            R             R            R              R           R             R            R             R
    Reset            x             x             x             x           x             x             x            x


               Bit 7 – BACKUP Backup Reset
               This bit is set if either a Backup or Hibernate Reset has occurred. Refer to BKUPEXIT register to identify
               the source of the Backup Reset.

               Bit 6 – SYST System Reset Request
               This bit is set if a System Reset Request has occurred. Refer to the Cortex processor documentation for
               more details.

               Bit 5 – WDT Watchdog Reset
               This bit is set if a Watchdog Timer Reset has occurred.

               Bit 4 – EXT External Reset
               This bit is set if an external Reset has occurred.

               Bit 3 – NVM NVM Reset
               This bit is set if an NVM Reset has occurred.

               Bit 2 – BOD33 Brown Out 33 Detector Reset
               This bit is set if a BOD33 Reset has occurred.

               Bit 1 – BOD12 Brown Out 12 Detector Reset
               This bit is set if a BOD12 Reset has occurred.

               Bit 0 – POR Power On Reset
               This bit is set if a POR has occurred.




           © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 201
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                RSTC – Reset Controller

16.8.2         Backup Exit Source

               Name:        BKUPEXIT
               Offset:      0x02
               Property:    –

               When either a Hibernate ora Backup Reset occurs, the bit corresponding to the exit condition is set to '1',
               the other bits are written to '0'.
               In some specific cases, the RTC and BBPS bits can be set together, e.g. when the device leaves the
               battery Backup Mode caused by a BBPS condition, and a RTC event was generated during the Battery
               Backup Mode period.

         Bit         7             6             5             4             3              2              1           0
                    HIB                                                                  BBPS             RTC
   Access            R                                                                     R              R
    Reset            x                                                                      x              x


               Bit 7 – HIB Hibernate
               This bit is set if an Hibernate reset occurs. This bit is zero if a backup reset occurs.

               Bit 2 – BBPS Battery Backup Power Switch
               This bit is set if the Battery Backup Power Switch of the Supply Controller changes back from battery
               mode to main power mode.

               Bit 1 – RTC Real Timer Counter Interrupt
               This bit is set if an RTC interrupt flag is set in Backup Mode.
               Related Links
               19. SUPC – Supply Controller
               21. RTC – Real-Time Counter




           © 2019 Microchip Technology Inc.                          Datasheet                             DS60001507E-page 202
