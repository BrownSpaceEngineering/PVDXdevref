# 15. MCLK – Main Clock

*Source: `Atmel-SAMD51.pdf`, pages 170-195 — SAMD51 family datasheet*

                                                           SAM D5x/E5x Family Data Sheet
                                                                                            MCLK – Main Clock


15.      MCLK – Main Clock

15.1     Overview
         The Main Clock (MCLK) controls the synchronous clock generation of the device.
         Using a clock provided by the Generic Clock Module (GCLK_MAIN), the Main Clock Controller provides
         synchronous system clocks to the CPU and the modules connected to the AHBx and the APBx bus. The
         synchronous system clocks are divided into a number of clock domains. Each clock domain can run at
         different frequencies, enabling the user to save power by running peripherals at a relatively low clock
         frequency, while maintaining high CPU performance or vice versa. In addition, the clock can be masked
         for individual modules, enabling the user to minimize power consumption.


15.2     Features
           • Generates CPU, AHB, and APB system clocks
              – Clock source and division factor from GCLK
              – Clock prescaler with 1x to 128x division
           • Safe run-time clock switching from GCLK
           • Module-level clock gating through maskable peripheral clocks


15.3     Block Diagram
         Figure 15-1. MCLK Block Diagram



                                                                         CLK_APBx

                                                                         CLK_AHBx
                                  GCLK_MAIN         MAIN                                   PERIPHERALS
                      GCLK
                                              CLOCK CONTROLLER
                                                                         CLK_CPU


                                                                                            CPU




15.4     Signal Description
         Not applicable.


15.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

15.5.1   I/O Lines
         Not applicable.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 170
                                                            SAM D5x/E5x Family Data Sheet
                                                                                            MCLK – Main Clock

15.5.2   Power Management
         The MCLK will operate in all sleep modes if a synchronous clock is required in these modes.
         Related Links
         18. PM – Power Manager

15.5.3   Clocks
         The MCLK bus clock (CLK_MCLK_APB) can be enabled and disabled in the Main Clock module, and the
         default state of CLK_MCLK_APB can be found in the Peripheral Clock Masking section. If this clock is
         disabled, it can only be re-enabled by a reset.
         The Generic Clock GCLK_MAIN is required to generate the Main Clocks. GCLK_MAIN is configured in
         the Generic Clock Controller, and can be re-configured by the user if needed.
         Related Links
         14. GCLK - Generic Clock Controller

15.5.3.1 Main Clock
         The main clock CLK_MAIN is the common source for the synchronous clocks. This is fed into the
         common 8-bit prescaler that is used to generate synchronous clocks to the CPU, AHBx, and APBx
         modules.

15.5.3.2 CPU Clock
         The CPU clock (CLK_CPU) is routed to the CPU. Halting the CPU clock inhibits the CPU from executing
         instructions.

15.5.3.3 APBx and AHBx Clock
         The APBx clocks (CLK_APBx) and the AHBx clocks (CLK_AHBx) are the root clock source used by
         modules requiring a clock on the APBx and the AHBx bus. These clocks are always synchronous to the
         CPU clock, and can run even when the CPU clock is turned off in sleep mode. A clock gater is inserted
         after the common APB clock to gate any APBx clock of a module on APBx bus, as well as the AHBx
         clock.

15.5.3.4 Clock Domains
         The device has these synchronous clock domains:
           • High-Speed synchronous clock domain (HS Clock Domain). Frequency is fHS.
           • CPU synchronous clock domain (CPU Clock Domain). Frequency is fCPU.
         See also the related links for the clock domain partitioning.

15.5.4   DMA
         Not applicable.

15.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. Using the MCLK interrupt requires the
         Interrupt Controller to be configured first.

15.5.6   Events
         Not applicable.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 171
                                                            SAM D5x/E5x Family Data Sheet
                                                                                             MCLK – Main Clock

15.5.7    Debug Operation
          When the CPU is halted in debug mode, the MCLK continues normal operation. In sleep mode, the
          clocks generated from the MCLK are kept running to allow the debugger accessing any module. As a
          consequence, power measurements are incorrect in debug mode.

15.5.8    Register Access Protection
          All registers with write access can be write-protected optionally by the Peripheral Access Controller
          (PAC), except for the following registers:
           • Interrupt Flag register (INTFLAG)
          Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
          Protection" property in each individual register description.
          PAC write protection does not apply to accesses through an external debugger.
          Related Links
          27. PAC - Peripheral Access Controller

15.5.9    Analog Connections
          Not applicable.



15.6      Functional Description

15.6.1    Principle of Operation
          The CLK_MAIN clock signal from the GCLK module is the source for the main clock, which in turn is the
          common root for the synchronous clocks for the CPU, APBx, and AHBx modules. The CLK_MAIN is
          divided by an 8-bit prescaler. Each of the derived clocks can run from any divided or undivided main
          clock, ensuring synchronous clock sources for each clock domain. The clock domain (CPU) can be
          changed on the fly to respond to variable load in the application. The clocks for each module in a clock
          domain can be masked individually to avoid power consumption in inactive modules. Depending on the
          sleep mode, some clock domains can be turned off.

15.6.2    Basic Operation

15.6.2.1 Initialization
          After a Reset, the default clock source of the CLK_MAIN clock (GCLK_MAIN) is started and calibrated
          before the CPU starts running. The GCLK_MAIN clock is selected as the main clock without any
          prescaler division.
          By default, only the necessary clocks are enabled.

15.6.2.2 Enabling, Disabling, and Resetting
          The MCLK module is always enabled and cannot be reset.

15.6.2.3 Selecting the Main Clock Source
          Refer to the Generic Clock Controller description for details on how to configure the clock source of the
          GCLK_MAIN clock.
          Related Links
          14. GCLK - Generic Clock Controller




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 172
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                            MCLK – Main Clock

15.6.2.4 Selecting the Synchronous Clock Division Ratio
         The main clock GCLK_MAIN feeds an 8-bit prescaler, which can be used to generate the synchronous
         clocks. By default, the synchronous clocks run on the undivided main clock. The user can select a
         prescaler division for the CPU clock domain by writing the Division (DIV) bits in the CPU Clock Division
         register CPUDIV, resulting in a CPU clock domain frequency determined by this equation:
                   �����
         ���� =
                  ������
         Frequencies must never exceed the specified maximum frequency for each clock domain given in the
         electrical characteristics specifications.
         If the application attempts to write forbidden values in CPUDIV register, register is written but these bad
         values are not used and a violation is reported to the PAC module.
         Division bits (DIV) can be written without halting or disabling peripheral modules. Writing DIV bits allows a
         new clock setting to be written to all synchronous clocks belonging to the corresponding clock domain at
         the same time.
         Figure 15-2. Synchronous Clock Selection and Prescaler
                                                     Sleep mode
                                 Sleep Controller
                                                                                                                     HS
                                                                                                                 Clock Domain: fHS

                                                                              MASK
                                                                                                                     PERIPHERALS
                                                                                        gate
                                                                                         Clock     clk_apb_ipn
                                                                  Clock                gate
                                                                                        Clock
                                                                           CLK_APB_HS Clock
                                                                                                 clk_apb_ip1
                                                                  gate                 gate      clk_apb_ip0


                                                    HSDIV



                                                                              MASK                                    CPU
                                                                          CLK_APB_CPU Clock
                                                                                                   clk_apb_ipn    Clock Domain: fCPU
                                                                  Clock                          clk_apb_ip1
                                                                  gate                 gate      clk_apb_ip0

                                                                             MASK                                 PERIPHERALS
                                                                                        gate
                                                                                         Clock     clk_ahb_ipn
                                                                  Clock                gate
                                                                                        Clock
                                                                          CLK_AHB_CPU Clock
                                                                                                 clk_ahb_ip1
                                                                  gate                 gate      clk_ahb_ip0




                                                                           CLK_CPU                                  CPU
                   GCLK_MAIN                                      Clock
           GCLK                 Prescaler                         gate


                                                    CPUDIV

         Note: A FAST clock for QSPI (CLK_QSPI2X_AHB) is derived from high-speed synchronous fHS.
         Related Links
         27. PAC - Peripheral Access Controller

15.6.2.5 Clock Ready Flag
         There is a slight delay between writing to CPUDIV until the new clock settings become effective.
         During this interval, the Clock Ready flag in the Interrupt Flag Status and Clear register
         (INTFLAG.CKRDY) will return zero when read. If CKRDY in the INTENSET register is set to '1', the Clock
         Ready interrupt will be triggered when the new clock setting is effective. The clock settings (CLKCFG)
         must not be re-written while INTFLAG. CKRDY reads '0'. The system may become unstable or hang, and
         a violation is reported to the PAC module.




        © 2019 Microchip Technology Inc.                             Datasheet                                   DS60001507E-page 173
                                                          SAM D5x/E5x Family Data Sheet
                                                                                          MCLK – Main Clock

        Related Links
        27. PAC - Peripheral Access Controller

15.6.2.6 Peripheral Clock Masking
        It is possible to disable/enable the AHB or APB clock for a peripheral by writing the corresponding bit in
        the Clock Mask registers (APBxMASK) to '0'/'1'. The default state of the peripheral clocks is shown here.
        Table 15-1. Peripheral Clock Default State

         CPU Clock Domain
         Peripheral Clock                                     Default State
         CLK_AC_APB                                           Disabled
         CLK_ADC0_APB                                         Enabled
         CLK_ADC1_APB                                         Enabled
         CLK_AES_APB                                          Disabled
         CLK_BRIDGE_A_AHB                                     Enabled
         CLK_BRIDGE_B_AHB                                     Enabled
         CLK_BRIDGE_C_AHB                                     Enabled
         CLK_BRIDGE_D_AHB                                     Enabled
         CLK_CAN0_AHB                                         Enabled
         CLK_CAN1_AHB                                         Enabled
         CLK_CMCC_AHB                                         Enabled
         CLK_DMAC_AHB                                         Enabled
         CLK_DSU_AHB                                          Enabled
         CLK_EIC_APB                                          Enabled
         CLK_EVSYS_APB                                        Disabled
         CLK_FREQM_APB                                        Disabled
         CLK_GCLK_APB                                         Enabled
         CLK_GMAC_AHB                                         Enabled
         CLK_GMAC_APB                                         Disabled
         CLK_ICM_AHB                                          Enabled
         CLK_I2S_AHB                                          Disabled
         CLK_MCLK_APB                                         Enabled
         CLK_NVMCTRL_AHB                                      Enabled
         CLK_NVMCTRL_APB                                      Enabled
         CLK_OSCCTRL_APB                                      Enabled
         CLK_PAC_AHB                                          Enabled




        © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 174
                                   SAM D5x/E5x Family Data Sheet
                                                     MCLK – Main Clock

...........continued
 CPU Clock Domain
 Peripheral Clock                    Default State
 CLK_PAC_APB                         Enabled
 CLK_PDEC_APB                        Disabled
 CLK_PORT_APB                        Enabled
 CLK_PTC_APB                         Enabled
 CLK_PUKCC_AHB                       Enabled
 CLK_QSPI_AHB                        Enabled
 CLK_QSPI2X_AHB                      Enabled
 CLK_SDHC0_AHB                       Enabled
 CLK_SDHC1_AHB                       Enabled
 CLK_SERCOM0_APB                     Disabled
 CLK_SERCOM1_APB                     Disabled
 CLK_SERCOM2_APB                     Disabled
 CLK_SERCOM3_APB                     Disabled
 CLK_SERCOM4_APB                     Disabled
 CLK_SERCOM5_APB                     Disabled
 CLK_SERCOM6_APB                     Disabled
 CLK_SERCOM7_APB                     Disabled
 CLK_TC0_APB                         Disabled
 CLK_TC1_APB                         Disabled
 CLK_TC2_APB                         Disabled
 CLK_TC3_APB                         Disabled
 CLK_TC4_APB                         Disabled
 CLK_TC5_APB                         Disabled
 CLK_TC6_APB                         Disabled
 CLK_TC7_APB                         Disabled
 CLK_TCC0_APB                        Disabled
 CLK_TCC1_APB                        Disabled
 CLK_TCC2_APB                        Disabled
 CLK_TCC3_APB                        Disabled
 CLK_TCC4_APB                        Disabled




© 2019 Microchip Technology Inc.   Datasheet            DS60001507E-page 175
                                                             SAM D5x/E5x Family Data Sheet
                                                                                              MCLK – Main Clock

         ...........continued
          CPU Clock Domain
          Peripheral Clock                                       Default State
          CLK_USB_AHB                                            Enabled
          CLK_USB_APB                                            Disabled
          CLK_WDT_APB                                            Enabled
          CLK_DAC_APB                                            Disabled
          CLK_DSU_APB                                            Enabled
          CLK_CCL_APB                                            Disabled
          CLK_QSPI_APB                                           Enabled
          CLK_ICM_APB                                            Disabled
          CLK_TRNG_APB                                           Disabled

          Backup Clock Domain
          Peripheral Clock                                       Default State
          CLK_OSC32KCTRL_APB                                     Enabled
          CLK_PM_APB                                             Enabled
          CLK_SUPC_APB                                           Enabled
          CLK_RSTC_APB                                           Enabled
          CLK_RTC_APB                                            Enabled

         When the APB clock is not provided to a module, its registers cannot be read or written. The module can
         be re-enabled later by writing the corresponding mask bit to '1'.
         A module may be connected to several clock domains (for instance, AHB and APB), in which case it will
         have several mask bits.
         Note that clocks should only be switched off if it is certain that the module will not be used: Switching off
         the clock for the NVM Controller (NVMCTRL) will cause a problem if the CPU needs to read from the
         Flash Memory. Switching off the clock to the MCLK module (which contains the mask registers) or the
         corresponding APBx bridge, will make it impossible to write the mask registers again. In this case, they
         can only be re-enabled by a system reset.

15.6.3   DMA Operation
         Not applicable.

15.6.4   Interrupts
         The peripheral has the following interrupt sources:
           • Clock Ready (CKRDY): indicates that CPU clocks are ready. This interrupt is a synchronous wake-up
             source.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be enabled




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 176
                                                            SAM D5x/E5x Family Data Sheet
                                                                                             MCLK – Main Clock

         individually by writing a '1' to the corresponding enabling bit in the Interrupt Enable Set (INTENSET)
         register, and disabled by writing a '1' to the corresponding clearing bit in the Interrupt Enable Clear
         (INTENCLR) register.
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled or the
         peripheral is reset. An interrupt flag is cleared by writing a '1' to the corresponding bit in the INTFLAG
         register. Each peripheral can have one interrupt request line per interrupt source or one common interrupt
         request line for all the interrupt sources.If the peripheral has one common interrupt request line for all the
         interrupt sources, the user must read the INTFLAG register to determine which interrupt condition is
         present.
         Related Links
         18. PM – Power Manager
         10.2.1 Overview

15.6.5   Events
         Not applicable.

15.6.6   Sleep Mode Operation
         In IDLE sleep mode, the MCLK is still running on the selected main clock.
         In STANDBY sleep mode, the MCLK is frozen if no synchronous clock is required.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 177
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                          MCLK – Main Clock


15.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0
 0x01        INTENCLR         7:0                                                                                       CKRDY
 0x02        INTENSET         7:0                                                                                       CKRDY
 0x03        INTFLAG          7:0                                                                                       CKRDY
 0x04          HSDIV          7:0                                               DIV[7:0]
 0x05         CPUDIV          7:0                                               DIV[7:0]
 0x06
   ...       Reserved
 0x0F
                              7:0      Reserved   NVMCTRL    Reserved     DSU          HPBn3       HPBn2      HPBn1      HPBn0
                             15:8      SDHCn0      GMAC       QSPI        PAC         Reserved      USB       DMAC       CMCC
 0x10        AHBMASK                  NVMCTRL_C NVMCTRL_S
                             23:16                           QSPI_2X     PUKCC             ICM     CANn1      CANn0     SDHCn1
                                        ACHE      MEEPROM
                             31:24
                                                            OSC32KCTR
                              7:0       GCLK       SUPC                 OSCCTRL            RSTC    MCLK        PM         PAC
                                                                L
 0x14       APBAMASK         15:8       TCn1       TCn0     SERCOM1     SERCOM0        FREQM        EIC        RTC       WDT
                             23:16
                             31:24
                              7:0       EVSYS                            PORT                     NVMCTRL      DSU        USB
                             15:8                  TCn3       TCn2       TCCn1         TCCn0      SERCOM3    SERCOM2
 0x18       APBBMASK
                             23:16                                                                                      RAMECC
                             31:24
                              7:0       PDEC       TCn5       TCn4       TCCn3         TCCn2       GMAC
                             15:8                   CCL       QSPI                         ICM     TRNG        AES        AC
 0x1C       APBCMASK
                             23:16
                             31:24
                              7:0       ADCn0       TC7        TC6       TCC4        SERCOM7      SERCOM6    SERCOM5   SERCOM4
                             15:8                                                          PCC      I2S        DAC       ADCn1
 0x20       APBDMASK
                             23:16
                             31:24




15.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
          the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers can be write-protected optionally by the Peripheral Access Controller (PAC). This is
          denoted by the property "PAC Write-Protection" in each individual register description. Refer to the
          15.5.8 Register Access Protection for details.




          © 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 178
                                                             SAM D5x/E5x Family Data Sheet
                                                                             MCLK – Main Clock

15.8.1         Control A

               Name:         CTRLA
               Offset:       0x00
               Reset:        0x00
               Property:     PAC Write-Protection

               All bits in this register are reserved.

         Bit         7              6             5      4         3     2     1            0


   Access
    Reset




           © 2019 Microchip Technology Inc.                  Datasheet          DS60001507E-page 179
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                 MCLK – Main Clock

15.8.2         Interrupt Enable Clear

               Name:       INTENCLR
               Offset:     0x01
               Reset:      0x00
               Property:   PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

         Bit         7            6             5            4            3             2            1             0
                                                                                                                CKRDY
   Access                                                                                                        R/W
    Reset                                                                                                          0


               Bit 0 – CKRDY Clock Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Clock Ready Interrupt Enable bit and the corresponding interrupt
               request.
                Value        Description
                0            The Clock Ready interrupt is enabled and will generate an interrupt request when the Clock
                             Ready Interrupt Flag is set.
                1            The Clock Ready interrupt is disabled.




           © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 180
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                   MCLK – Main Clock

15.8.3         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x02
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         7             6             5            4             3             2             1             0
                                                                                                                   CKRDY
   Access                                                                                                           R/W
    Reset                                                                                                             0


               Bit 0 – CKRDY Clock Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Clock Ready Interrupt Enable bit and enable the Clock Ready interrupt.
               Value         Description
               0             The Clock Ready interrupt is disabled.
               1             The Clock Ready interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 181
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             MCLK – Main Clock

15.8.4         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x03
               Reset:      0x01
               Property:   –


         Bit        7             6           5           4            3            2            1           0
                                                                                                           CKRDY
   Access                                                                                                   R/W
    Reset                                                                                                    1


               Bit 0 – CKRDY Clock Ready
               This flag is cleared by writing a '1' to the flag.
               This flag is set when the synchronous CPU, APBx, and AHBx clocks have frequencies as indicated in the
               CLKCFG registers and will generate an interrupt if INTENCLR/SET.CKRDY is '1'.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the Clock Ready interrupt flag.




           © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 182
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                 MCLK – Main Clock

15.8.5         High-Speed Clock Division

               Name:       HSDIV
               Offset:     0x04
               Reset:      0x01


         Bit         7            6            5             4              3           2            1            0
                                                                 DIV[7:0]
   Access            R            R            R             R              R          R             R            R
    Reset            0            0            0             0              0           0            0            1


               Bits 7:0 – DIV[7:0] HS Clock Division Factor
               These bits define the division ratio of the main clock prescaler related to the HS clock domain (HSDIV).
                Value      Name                               Description
                0x01       DIV1                               Divide by 1
                others -                                      Reserved




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 183
                                                                SAM D5x/E5x Family Data Sheet
                                                                                               MCLK – Main Clock

15.8.6         CPU Clock Division

               Name:       CPUDIV
               Offset:     0x05
               Reset:      0x01
               Property:   PAC Write-Protection


         Bit         7            6            5            4               3         2            1            0
                                                                DIV[7:0]
   Access          R/W          R/W           R/W         R/W              R/W      R/W           R/W          R/W
    Reset            0            0            0            0               0         0            0            1


               Bits 7:0 – DIV[7:0] CPU Clock Division Factor
               These bits define the division ratio of the main clock prescaler related to the CPU clock domain
               (CPUDIV).
               To ensure correct operation, frequencies must be selected so that fHS ≥ fCPU (i.e. CPUDIV ≥ HSDIV).
               Frequencies must never exceed the specified maximum frequency for each clock domain.
                Value      Name                                 Description
                0x01       DIV1                                  Divide by 1
                0x02       DIV2                                  Divide by 2
                0x04       DIV4                                  Divide by 4
                0x08       DIV8                                  Divide by 8
                0x10       DIV16                                 Divide by 16
                0x20       DIV32                                 Divide by 32
                0x40       DIV64                                 Divide by 64
                0x80       DIV128                                Divide by 128
                others -                                         Reserved




           © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 184
                                                                SAM D5x/E5x Family Data Sheet
                                                                                       MCLK – Main Clock

15.8.7         AHB Mask

               Name:        AHBMASK
               Offset:      0x10
               Reset:       0x00FFFFFF
               Property:    PAC Write-Protection


         Bit        31           30             29        28           27       26       25           24


   Access
    Reset


         Bit        23           22             21        20           19       18       17           16
               NVMCTRL_CA NVMCTRL_SM          QSPI_2X    PUKCC         ICM     CANn1    CANn0      SDHCn1
                   CHE         EEPROM
   Access          R/W           R/W            R/W       R/W         R/W      R/W      R/W          R/W
    Reset           1             1              1         1            1        1        1           1


         Bit        15           14             13        12           11       10        9           8
                 SDHCn0         GMAC           QSPI       PAC       Reserved   USB      DMAC        CMCC
   Access          R/W           R/W            R/W       R/W          R       R/W      R/W          R/W
    Reset           1             1              1         1            1        1        1           1


         Bit        7             6              5         4            3        2        1           0
                 Reserved     NVMCTRL         Reserved   DSU          HPBn3    HPBn2    HPBn1       HPBn0
   Access           R            R/W             R        R/W         R/W      R/W      R/W          R/W
    Reset           1             1              1         1            1        1        1           1


               Bit 23 – NVMCTRL_CACHE NVMCTRL_CACHE AHB Clock Enable
               Value      Description
               0          The AHB clock for the NVMCTRL_CACHE is stopped.
               1          The AHB clock for the NVMCTRL_CACHE is enabled.

               Bit 22 – NVMCTRL_SMEEPROM NVMCTRL_SMEEPROM AHB Clock Enable
               Value      Description
               0          The AHB clock for the NVMCTRL_SMEEPROM is stopped.
               1          The AHB clock for the NVMCTRL_SMEEPROM is enabled.

               Bit 21 – QSPI_2X QSPI_2X AHB Clock Enable
               Value      Description
               0          The AHB clock for the QSPI_2X is stopped.
               1          The AHB clock for the QSPI_2X is enabled.

               Bit 20 – PUKCC PUKCC AHB Clock Enable
               Value      Description
               0          The AHB clock for the PUKCC is stopped.
               1          The AHB clock for the PUKCC is enabled.

               Bit 19 – ICM ICM AHB Clock Enable




           © 2019 Microchip Technology Inc.                      Datasheet                DS60001507E-page 185
                                                  SAM D5x/E5x Family Data Sheet
                                                                                 MCLK – Main Clock

 Value        Description
 0            The AHB clock for the ICM is stopped.
 1            The AHB clock for the ICM is enabled.

Bits 17, 18 – CANn CANn AHB Clock Enable
Value       Description
0           The AHB clock for the CANn is stopped.
1           The AHB clock for the CANn is enabled.

Bits 15, 16 – SDHCn SDHCn AHB Clock Enable
Value       Description
0           The AHB clock for the SDHCn is stopped.
1           The AHB clock for the SDHCn is enabled.

Bit 14 – GMAC GMAC AHB Clock Enable
Value      Description
0          The AHB clock for the GMAC is stopped.
1          The AHB clock for the GMAC is enabled.

Bit 13 – QSPI QSPI AHB Clock Enable
Value      Description
0          The AHB clock for the QSPI is stopped.
1          The AHB clock for the QSPI is enabled.

Bit 12 – PAC PAC AHB Clock Enable
Value      Description
0          The AHB clock for the PAC is stopped.
1          The AHB clock for the PAC is enabled.

Bits 11,7,5 – Reserved Reserved bits
Reserved bits are unused and reserved for future use. For compatibility with future devices, always write
reserved bits to their reset value. If no reset value is given, write 0.

Bit 10 – USB USB AHB Clock Enable
Value      Description
0          The AHB clock for the USB is stopped.
1          The AHB clock for the USB is enabled.

Bit 9 – DMAC DMAC AHB Clock Enable
Value      Description
0          The AHB clock for the DMAC is stopped.
1          The AHB clock for the DMAC is enabled.

Bit 8 – CMCC CMCC AHB Clock Enable
Value      Description
0          The AHB clock for the CMCC is stopped.
1          The AHB clock for the CMCC is enabled.

Bit 6 – NVMCTRL NVMCTRL AHB Clock Enable




© 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 186
                                                SAM D5x/E5x Family Data Sheet
                                                                MCLK – Main Clock

 Value        Description
 0            The AHB clock for the NVMCTRL is stopped.
 1            The AHB clock for the NVMCTRL is enabled.

Bit 4 – DSU DSU AHB Clock Enable
Value      Description
0          The AHB clock for the DSU is stopped.
1          The AHB clock for the DSU is enabled.

Bits 0, 1, 2, 3 – HPBn HPBn AHB Clock Enable
Value        Description
0            The AHB clock for the HPBn is stopped.
1            The AHB clock for the APBn is enabled.




© 2019 Microchip Technology Inc.                 Datasheet         DS60001507E-page 187
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                        MCLK – Main Clock

15.8.8         APBA Mask

               Name:       APBAMASK
               Offset:     0x14
               Reset:      0x000007FF
               Property:   PAC Write-Protection


         Bit        31           30               29         28            27     26      25           24


   Access
    Reset


         Bit        23           22               21         20            19     18      17           16


   Access
    Reset


         Bit        15           14               13         12            11     10      9            8
                   TCn1         TCn0           SERCOM1     SERCOM0       FREQM   EIC     RTC          WDT
   Access          R/W          R/W              R/W         R/W          R/W    R/W     R/W          R/W
    Reset           0             0               0           0            0      1       1            1


         Bit        7             6               5           4            3      2       1            0
                   GCLK        SUPC           OSC32KCTRL   OSCCTRL       RSTC    MCLK     PM          PAC
   Access          R/W          R/W              R/W         R/W          R/W    R/W     R/W          R/W
    Reset           1             1               1           1            1      1       1            1


               Bits 14, 15 – TCn TCn APBA Clock Enable
               Value       Description
               0           The APBA clock for the TCn is stopped.
               1           The APBA clock for the TCn is enabled.

               Bits 12, 13 – SERCOM SERCOMn APBA Clock Enable
               Value       Description
               0           The APBA clock for the SERCOMn is stopped.
               1           The APBA clock for the SERCOMn is enabled.

               Bit 11 – FREQM FREQM APBA Clock Enable
               Value      Description
               0          The APBA clock for the FREQM is stopped.
               1          The APBA clock for the FREQM is enabled.

               Bit 10 – EIC EIC APBA Clock Enable
               Value       Description
               0           The APBA clock for the EIC is stopped.
               1           The APBA clock for the EIC is enabled.

               Bit 9 – RTC RTC APBA Clock Enable




           © 2019 Microchip Technology Inc.                          Datasheet             DS60001507E-page 188
                                                 SAM D5x/E5x Family Data Sheet
                                                                 MCLK – Main Clock

 Value        Description
 0            The APBA clock for the RTC is stopped.
 1            The APBA clock for the RTC is enabled.

Bit 8 – WDT WDT APBA Clock Enable
Value      Description
0          The APBA clock for the WDT is stopped.
1          The APBA clock for the WDT is enabled.

Bit 7 – GCLK GCLK APBA Clock Enable
Value      Description
0          The APBA clock for the GCLK is stopped.
1          The APBA clock for the GCLK is enabled.

Bit 6 – SUPC SUPC APBA Clock Enable
Value      Description
0          The APBA clock for the SUPC is stopped.
1          The APBA clock for the SUPC is enabled.

Bit 5 – OSC32KCTRL OSC32KCTRL APBA Clock Enable
Value      Description
0          The APBA clock for the OSC32KCTRL is stopped.
1          The APBA clock for the OSC32KCTRL is enabled.

Bit 4 – OSCCTRL OSCCTRL APBA Clock Enable
Value      Description
0          The APBA clock for the OSCCTRL is stopped.
1          The APBA clock for the OSCCTRL is enabled.

Bit 3 – RSTC RSTC APBA Clock Enable
Value      Description
0          The APBA clock for the RSTC is stopped.
1          The APBA clock for the RSTC is enabled.

Bit 2 – MCLK MCLK APBA Clock Enable
Value      Description
0          The APBA clock for the MCLK is stopped.
1          The APBA clock for the MCLK is enabled.

Bit 1 – PM PM APBA Clock Enable
Value      Description
0          The APBA clock for the PM is stopped.
1          The APBA clock for the PM is enabled.

Bit 0 – PAC PAC APBA Clock Enable
Value      Description
0          The APBA clock for the PAC is stopped.
1          The APBA clock for the PAC is enabled.




© 2019 Microchip Technology Inc.                  Datasheet         DS60001507E-page 189
                                                                SAM D5x/E5x Family Data Sheet
                                                                                       MCLK – Main Clock

15.8.9         APBB Mask

               Name:       APBBMASK
               Offset:     0x18
               Reset:      0x00018056
               Property:   PAC Write-Protection


         Bit        31           30            29         28          27       26        25           24


   Access
    Reset


         Bit        23           22            21         20          19       18        17           16
                                                                                                   RAMECC
   Access                                                                                            R/W
    Reset                                                                                             1


         Bit        15           14            13         12          11       10         9           8
                                TCn3          TCn2      TCCn1        TCCn0   SERCOM3   SERCOM2
   Access                       R/W           R/W        R/W          R/W      R/W       R/W
    Reset                         0            0           0            0       0         0


         Bit        7             6            5           4            3       2         1           0
                  EVSYS                                  PORT                NVMCTRL     DSU         USB
   Access          R/W                                   R/W                   R/W       R/W         R/W
    Reset           0                                      1                    1         1           0


               Bit 16 – RAMECC RAMECC APBB Clock Enable
               Value      Description
               0          The APBB clock for the RAMECC is stopped.
               1          The APBB clock for the RAMECC is enabled.

               Bits 13, 14 – TCn TCn APBB Clock Enable
               Value       Description
               0           The APBB clock for the TCn is stopped.
               1           The APBB clock for the TCn is enabled.

               Bits 11, 12 – TCCn TCCn APBB Clock Enable
               Value       Description
               0           The APBB clock for the TCCn is stopped.
               1           The APBB clock for the TCCn is enabled.

               Bits 9, 10 – SERCOM SERCOMn APBB Clock Enable
               Value       Description
               0           The APBB clock for the SERCOMn is stopped.
               1           The APBB clock for the SERCOMn is enabled.

               Bit 7 – EVSYS EVSYS APBB Clock Enable




           © 2019 Microchip Technology Inc.                     Datasheet                 DS60001507E-page 190
                                                SAM D5x/E5x Family Data Sheet
                                                                MCLK – Main Clock

 Value        Description
 0            The APBB clock for the EVSYS is stopped.
 1            The APBB clock for the EVSYS is enabled.

Bit 4 – PORT PORT APBB Clock Enable
Value      Description
0          The APBB clock for the PORT is stopped.
1          The APBB clock for the PORT is enabled.

Bit 2 – NVMCTRL NVMCTRL APBB Clock Enable
Value      Description
0          The APBB clock for the NVMCTRL is stopped.
1          The APBB clock for the NVMCTRL is enabled.

Bit 1 – DSU DSU APBB Clock Enable
Value      Description
0          The APBB clock for the DSU is stopped.
1          The APBB clock for the DSU is enabled.

Bit 0 – USB USB APBB Clock Enable
Value      Description
0          The APBB clock for the USB is stopped.
1          The APBB clock for the USB is enabled.




© 2019 Microchip Technology Inc.                  Datasheet        DS60001507E-page 191
                                                            SAM D5x/E5x Family Data Sheet
                                                                               MCLK – Main Clock

15.8.10 APBC Mask

           Name:       APBCMASK
           Offset:     0x1C
           Reset:      0x00002000
           Property:   PAC Write-Protection


     Bit        31           30            29         28          27     26      25           24


  Access
   Reset


     Bit        23           22            21         20          19     18      17           16


  Access
   Reset


     Bit        15           14            13         12          11     10      9            8
                            CCL           QSPI                   ICM    TRNG    AES           AC
  Access                    R/W           R/W                    R/W    R/W     R/W          R/W
   Reset                      0            1                      0      0       0            0


     Bit        7             6            5           4          3      2       1            0
              PDEC          TCn5          TCn4      TCCn3       TCCn2   GMAC
  Access       R/W          R/W           R/W        R/W         R/W    R/W
   Reset        0             0            1           0          0      1


           Bit 14 – CCL CCL APBC Mask Clock Enable
           Value      Description
           0          The APBC clock for the CCL is stopped.
           1          The APBC clock for the CCL is enabled.

           Bit 13 – QSPI QSPI APBC Mask Clock Enable
           Value      Description
           0          The APBC clock for the QSPI is stopped.
           1          The APBC clock for the QSPI is enabled.

           Bit 11 – ICM ICM APBC Mask Clock Enable
           Value       Description
           0           The APBC clock for the ICM is stopped.
           1           The APBC clock for the ICM is enabled.

           Bit 10 – TRNG TRNG APBC Mask Clock Enable
           Value      Description
           0          The APBC clock for the TRNG is stopped.
           1          The APBC clock for the TRNG is enabled.

           Bit 9 – AES AES APBC Mask Clock Enable




       © 2019 Microchip Technology Inc.                     Datasheet             DS60001507E-page 192
                                                 SAM D5x/E5x Family Data Sheet
                                                                 MCLK – Main Clock

 Value        Description
 0            The APBC clock for the AES is stopped.
 1            The APBC clock for the AES is enabled.

Bit 8 – AC AC APBC Mask Clock Enable
Value      Description
0          The APBC clock for the AC is stopped.
1          The APBC clock for the AC is enabled.

Bit 7 – PDEC PDEC APBC Mask Clock Enable
Value      Description
0          The APBC clock for the PDEC is stopped.
1          The APBC clock for the PDEC is enabled.

Bits 5, 6 – TCn TCn APBC Mask Clock Enable
Value        Description
0            The APBC clock for the TCn is stopped.
1            The APBC clock for the TCn is enabled.

Bits 3, 4 – TCCn TCCn APBC Mask Clock Enable
Value        Description
0            The APBC clock for the TCCn is stopped.
1            The APBC clock for the TCCn is enabled.

Bit 2 – GMAC GMAC APBC Mask Clock Enable
Value      Description
0          The APBC clock for the GMAC is stopped.
1          The APBC clock for the GMAC is enabled.




© 2019 Microchip Technology Inc.                   Datasheet        DS60001507E-page 193
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      MCLK – Main Clock

15.8.11 APBD Mask

           Name:       APBDMASK
           Offset:     0x20
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31           30           29           28           27        26        25           24


  Access
   Reset


     Bit        23           22           21           20           19        18        17           16


  Access
   Reset


     Bit        15           14           13           12           11        10         9           8
                                                                    PCC       I2S       DAC        ADCn1
  Access                                                            R/W       R/W       R           R/W
   Reset                                                             0         0         0           0


     Bit        7             6            5           4             3         2         1           0
              ADCn0         TC7           TC6        TCC4         SERCOM7   SERCOM6   SERCOM5    SERCOM4
  Access       R/W          R/W           R/W         R/W           R/W       R/W       R/W         R/W
   Reset        0             0            0           0             0         0         0           0


           Bit 11 – PCC PCC APBD Mask Clock Enable
           Value      Description
           0          The APBD clock for the PCC is stopped.
           1          The APBD clock for the PCC is enabled.

           Bit 10 – I2S I2S APBD Mask Clock Enable
           Value       Description
           0           The APBD clock for the I2S is stopped.
           1           The APBD clock for the I2S is enabled.

           Bit 9 – DAC DAC APBD Mask Clock Enable
           Value      Description
           0          The APBD clock for the DAC is stopped.
           1          The APBD clock for the DAC is enabled.

           Bits 7, 8 – ADCn ADCn APBD Mask Clock Enable
           Value       Description
           0            The APBD clock for the ADCn is stopped.
           1            The APBD clock for the ADCn is enabled.

           Bits 5, 6 – TC TCn APBD Mask Clock Enable




       © 2019 Microchip Technology Inc.                     Datasheet                    DS60001507E-page 194
                                                 SAM D5x/E5x Family Data Sheet
                                                                 MCLK – Main Clock

 Value        Description
 0            The APBD clock for the TCn is stopped.
 1            The APBD clock for the TCn is enabled.

Bit 4 – TCC4 TCC4 APBD Mask Clock Enable
Value      Description
0          The APBD clock for the TCC4 is stopped.
1          The APBD clock for the TCC4 is enabled.

Bits 0, 1, 2, 3 – SERCOM SERCOMn APBD Mask Clock Enable
Value        Description
0            The APBD clock for the SERCOMn is stopped.
1            The APBD clock for the SERCOMn is enabled.




© 2019 Microchip Technology Inc.                   Datasheet        DS60001507E-page 195
