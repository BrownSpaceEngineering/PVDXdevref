# 18. PM – Power Manager

*Source: `Atmel-SAMD51.pdf`, pages 214-234 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                        PM – Power Manager


18.    PM – Power Manager
       Related Links
       39.6.9 Sleep Mode Operation



18.1   Overview
       The Power Manager (PM) controls the sleep modes and the power domain gating of the device.
       Various sleep modes are provided in order to fit power consumption requirements. This enables the PM
       to stop unused modules in order to save power. In active mode, the CPU is executing application code.
       When the device enters a sleep mode, program execution is stopped and some modules and clock
       domains are automatically switched off by the PM according to the sleep mode. The application code
       decides which sleep mode to enter and when. Interrupts from enabled peripherals and all enabled reset
       sources can restore the device from a sleep mode to active mode.
       The user manually controls which power domains will be turned on and off in standby, hibernate and
       backup sleep mode.
       In backup and hibernate mode, the PM allows retaining the state of the I/O lines, preventing I/O lines from
       toggling during wake-up.



18.2   Features
         • Power management control
            – Sleep modes: Idle, Hibernate, Standby, Backup, and Off
            – SleepWalking available in standby mode.
            – I/O lines retention in Backup mode



18.3   Block Diagram
       Figure 18-1. PM Block Diagram
                                                     POWER MANAGER
                                                                            POWER LEVEL SWITCHES
                                                      POWER DOMAIN           FOR POWER DOMAINS
                                                       CONTROLLER

                                                       STDBYCFG
                                                       SLEEP MODE
                                  MAIN CLOCK                                       SUPPLY
                                                       CONTROLLER
                                  CONTROLLER                                     CONTROLLER
                                                       SLEEPCFG




18.4   Signal Description
       Not applicable.



18.5   Product Dependencies
       In order to use this peripheral, other parts of the system must be configured correctly, as described below.




       © 2019 Microchip Technology Inc.                    Datasheet                               DS60001507E-page 214
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           PM – Power Manager

18.5.1   I/O Lines
         Not applicable.

18.5.2   Clocks
         The PM bus clock (CLK_PM_APB) can be enabled and disabled in the Main Clock module. If this clock is
         disabled, it can only be re-enabled by a system reset.

18.5.3   DMA
         Not applicable.

18.5.4   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the PM interrupt requires the
         interrupt controller to be configured first.

18.5.5   Events
         Not applicable.

18.5.6   Debug Operation
         When the CPU is halted in debug mode, the PM continues normal operation. If standby sleep mode is
         requested by the system while in debug mode, the power domains are not turned off. As a consequence,
         power measurements while in debug mode are not relevant.
         If Hibernate or Backup sleep mode is requested by the system while in debug mode, the core domains
         are kept on, and the debug modules are kept running to allow the debugger to access internal registers.
         When exiting the hibernate or backup mode upon a reset condition, the core domains are reset except
         the debug logic, allowing users to keep using their current debug session.
         If OFF sleep mode is requested while in debug mode, the core domains are reset.
         Hot plugging in standby mode is supported.
         Hot plugging in Hibernate or backup mode or OFF mode is not supported as the DSU module is not
         powered.
         Cold plugging in Hibernate or backup or OFF mode is supported if the external reset duration is superior
         to the corresponding sleep mode wakeup time (See Electrical characteristic chapter).
         Backup wakeup time is less than 200us in typical case. This value can be higher if voltage scaling in
         SUPC is enabled. Refers to SUPC for details.

18.5.7   Register Access Protection
         Registers with write access can be write-protected optionally by the Peripheral Access Controller (PAC).
         PAC write protection is not available for the following registers:
           • Interrupt Flag register (INTFLAG). Refer to 18.8.5 INTFLAG for details
         Optional PAC write protection is denoted by the "PAC Write-Protection" property in each individual
         register description.
         Write-protection does not apply to accesses through an external debugger.

18.5.8   Analog Connections
         Not applicable.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 215
                                                           SAM D5x/E5x Family Data Sheet
                                                                                        PM – Power Manager


18.6      Functional Description

18.6.1    Terminology
          The following is a list of terms used to describe the Power Managemement features of this
          microcontroller.

18.6.1.1 Power Domains
          Leaving aside the supply domains, such as VDDANA and VDDIO, the device is split into these power
          domains: PDCORESW, PDBACKUP, PDSYSRAM and PDBKUPRAM.
          PDCORESW, PDSYSRAM and PDBKUPRAM are "switchable power domains". In Standby, Hibernate or
          Backup mode, these power domains can be turned OFF to save leakage consumption according to user
          configuration.
           • PDCORESW: contains the CPU and all the peripherals, except those located in the backup power
              domain.
           • PDBACKUP: contains the backup peripherals: OSC32KCTRL, SUPC, RSTC, RTC and the PM itself.
           • PDSYSRAM: contains the system RAM. It can be partially or fully turned OFF in Standby or
              Hibernate mode according to user configuration.
           • PDBKUPRAM: contains the backup RAM. It can be partially or fully turned OFF in Backup mode.

18.6.1.2 Sleep Modes
          The device can be set in a sleep mode. In sleep mode, the CPU is stopped and the peripherals are either
          active or idle, according to the sleep mode depth:
           • Idle sleep mode: The CPU is stopped. Synchronous clocks are stopped except when requested. The
             logic is retained.
           • Standby sleep mode: The CPU is stopped as well as the peripherals. The logic is retained, and
             power domain gating can be used to fully or partially turn off the PDSYSRAM power domain.
           • Hibernate sleep mode: PDCORESW power domain is turned OFF. The backup power domain is kept
             powered to allow few features to run (RTC, 32KHz clock sources, and wake-up from external pins).
             The PDSYSRAM power domain can be retained according to software configuration.
           • Backup sleep mode: Only the backup domain is kept powered to allow few features to run (RTC,
             32KHz clock sources, and wake-up from external pins). The PDBKUPRAM power domain can be
             retained according to software configuration.
           • Off sleep mode: The entire device is powered off.

18.6.2    Principle of Operation
          In active mode, all clock domains and power domains are active, allowing software execution and
          peripheral operation. The PM Sleep Mode Controller allows to save power by choosing between different
          sleep modes depending on application requirements, see 18.6.3.3 Sleep Mode Controller.
          The PM Power Domain Controller allows to reduce the power consumption in standby mode even further.

18.6.3    Basic Operation

18.6.3.1 Initialization
          After a Power-on Reset (POR), the PM is enabled, the device is in Active mode.

18.6.3.2 Enabling, Disabling and Resetting
          The PM is always enabled and can not be reset.




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 216
                                                             SAM D5x/E5x Family Data Sheet
                                                                                                     PM – Power Manager

18.6.3.3 Sleep Mode Controller
          A Sleep mode is entered by executing the Wait For Interrupt instruction (WFI). The Sleep Mode bits in the
          Sleep Configuration register (18.8.2 SLEEPCFG.SLEEPMODE) select the level of the sleep mode.
          Note: A small latency happens between the store instruction and actual writing of the SLEEPCFG.
          18.8.2 SLEEPCFG register due to bridges. Software must ensure that the 18.8.2 SLEEPCFG register
          reads the desired value before issuing a WFI instruction.
          Note: After power-up, the MAINVREG low power mode takes some time to stabilize. Once stabilized,
          the INTFLAG.SLEEPRDY bit is set. Before entering Standby, Hibernate or Backup mode, software must
          ensure that the INTFLAG.SLEEPRDY bit is set.
          Table 18-1. Sleep Mode Entry and Exit Table

          Mode             Mode Entry                                       Wake-Up Sources
          IDLE             SLEEPCFG.SLEEPMODE = IDLE                        Synchronous (2) (APB, AHB), asynchronous
                                                                            (1)


          STANDBY          SLEEPCFG.SLEEPMODE = STANDBY                     Synchronous (3), asynchronous (1)
          HIBERNATE SLEEPCFG.SLEEPMODE = HIBERNATE Hibernate reset detected by the RSTC
          BACKUP           SLEEPCFG.SLEEPMODE = BACKUP                      Backup reset detected by the RSTC
          OFF              SLEEPCFG.SLEEPMODE = OFF                         External Reset

          Note:
           1. Asynchronous: interrupt generated on generic clock, external clock, or external event.
           2. Synchronous: interrupt generated on synchronous (APB or AHB) clock.
           3. Synchronous interrupt only for peripherals configured to run in standby.
          Note: The type of wake-up sources (synchronous or asynchronous) is given in each module interrupt
          section.
          The sleep modes (idle, standby, hibernate, backup, and off) and their effect on the clocks activity, the
          regulator and the NVM state are described in the table and the sections below. Refer to 18.6.3.5 Power
          Domain Controller for the power domain gating effect.
Table 18-2. Sleep Mode Overview
Mode         Main clock CPU AHBx and   GCLK clocks                   Oscillators                     Regulator           NVM
                            APBx clock
                                                      ONDEMAND = 0                ONDEMAND = 1

Active       Run         Run   Run          Run(1)    Run                         Run if requested   MAINVREG            active

IDLE         Run         Stop Stop(2)       Run(1)    Run                         Run if requested   MAINVREG            active

STANDBY      Stop        Stop Stop(2)       Stop(2)   Run if requested or         Run if requested   MAINVREG in low     Ultra Low
                                                      RUNSTDBY=1                                     power mode          power

HIBERNATE Stop           Stop Stop          Stop      Stop                        Stop               MAINVREG in low     Ultra Low
                                                                                                     power mode          power+

BACKUP       Stop        Stop Stop          Stop      Stop                        Stop               Backup regulator    OFF
                                                                                                     (LPVREG)

OFF          Stop        Stop Stop          OFF       OFF                         OFF                OFF                 OFF




         © 2019 Microchip Technology Inc.                      Datasheet                                    DS60001507E-page 217
                                                           SAM D5x/E5x Family Data Sheet
                                                                                          PM – Power Manager

         Note:
          1. Running if requested by peripheral during SleepWalking
          2. Running during SleepWalking
18.6.3.3.1 IDLE Mode
         IDLE mode allows power optimization with the fastest wake-up time.
         The CPU is stopped, and peripherals are still working. As in Active mode, the AHBx and APBx clocks for
         peripheral are still provided if requested. As the main clock source is still running, wake-up time is very
         fast.
           • Entering Idle mode: The Idle mode is entered by executing the WFI instruction. Additionally, if the
             SLEEPONEXIT bit in the Cortex System Control register (SCR) is set, the Idle mode will be entered
             when the CPU exits the lowest priority ISR (Interrupt Service Routine, refer to the ARM Cortex
             documentation for details). This mechanism can be useful for applications that only require the
             processor to run when an interrupt occurs. Before entering the Idle mode, the user must select the
             Idle Sleep mode in the Sleep Configuration register (SLEEPCFG.SLEEPMODE=IDLE).
           • Exiting Idle mode: The processor wakes the system up when it detects any non-masked interrupt
             with sufficient priority to cause exception entry. The system goes back to the Active mode. The CPU
             and affected modules are restarted.
         GCLK clocks, regulators and RAM are not affected by the Idle Sleep mode and operate in normal mode.
18.6.3.3.2 STANDBY Mode
         The STANDBY mode is the lowest power configuration while keeping the state of the logic and the
         content of the RAM.
         In this mode, all clocks are stopped except those configured to be running sleepwalking tasks. The clocks
         can also be active on request or at all times, depending on their on-demand and run-in-standby settings.
         Either synchronous (CLK_APBx or CLK_AHBx) or generic (GCLK_x) clocks or both can be involved in
         sleepwalking tasks. This is the case when for example the SERCOM RUNSTDBY bit is written to '1'.
           • Entering STANDBY mode: This mode is entered by executing the WFI instruction after writing the
             Sleep Mode bit in the Sleep Configuration register (18.8.2 SLEEPCFG.SLEEPMODE=STANDBY).
             The SLEEPONEXIT feature is also available as in IDLE mode.
           • Exiting STANDBY mode: Any peripheral able to generate an asynchronous interrupt can wake up the
             system. For example, a peripheral running on a GCLK clock can trigger an interrupt. When the
             enabled asynchronous wake-up event occurs and the system is woken up, the device will either
             execute the interrupt service routine or continue the normal program execution according to the
             Priority Mask Register (PRIMASK) configuration of the CPU.
         Refer to the section about the Power Domain Controller for the RAM state.
         The regulator operates in low-power mode by default and switches automatically to the normal mode in
         case of a sleepwalking task requiring more power. It returns automatically to low power mode when the
         sleepwalking task is completed.
         Related Links
         18.6.3.5 Power Domain Controller

18.6.3.3.3 Hibernate and Backup Mode
         Hibernate and Backup mode allow achieving the lowest power consumption aside from OFF. The device
         is entirely powered off except for the backup domain. All peripherals in backup domain are allowed to run,
         for example, the RTC can be clocked by a 32.768 kHz oscillator. All PM registers are retained except
         INTENCLR, INTENSET, INTFLAG, and SLEEPCFG registers.




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 218
                                                            SAM D5x/E5x Family Data Sheet
                                                                                           PM – Power Manager

          • Entering Hibernate or Backup mode: This mode is entered by executing the WFI instruction after
            selecting the Hibernate or Backup mode by writing the Sleep Mode bits in the Sleep Configuration
            register (18.8.2 SLEEPCFG.SLEEPMODE=HIBERNATE or =BACKUP).
          • Exiting Hibernate or Backup mode: is triggered when a Hibernate or Backup Reset is detected by the
            Reset Controller (RSTC).
            Note: In Hibernate mode, the MAINVREG (in low-power mode) regulator is used to allow powering
            the PDRAM power domain which can be fully retained according to software configuration.
             Note: In Backup mode, the backup regulator (LPVREG) is used, unless VREG.RUNBKUP = 1.
             When VREG.RUNBKUP is set, the Main regulator is used in backup mode. The PDBKUPRAM
             power domain can be fully retained according to software configuration.
             Refer to the 18.6.3.5 Power Domain Controller for the RAM state.
18.6.3.3.4 OFF Mode
         In Off mode, the device is entirely powered-off.
          • Entering Off mode: This mode is entered by selecting the Off mode in the Sleep Configuration
            register by writing the Sleep Mode bits (SLEEPCFG.SLEEPMODE=OFF), and subsequent execution
            of the WFI instruction.
          • Exiting Off mode: This mode is left by pulling the RESET pin low, or when a power Reset is done.
18.6.3.4 I/O Lines Retention in HIBERNATE or BACKUP Mode
         When entering HIBERNATE or BACKUP mode, the PORT is powered off but the pin configuration is
         retained. When the device exits the HIBERNATE or BACKUP mode, the I/O line configuration can either
         be released or stretched, based on the I/O Retention bit in the Control A register (CTRLA.IORET).
          • If IORET=0 when exiting HIBERNATE or BACKUP mode, the I/O lines configuration is released and
            driven by the reset value of the PORT.
          • If the IORET=1 when exiting HIBERNATE or BACKUP mode, the configuration of the I/O lines is
            retained until the IORET bit is written to 0. It allows the I/O lines to be retained until the application
            has programmed the PORT.
18.6.3.5 Power Domain Controller
         The Power Domain Controller provides several ways of how power domains are handled while the device
         is in standby, hibernate or backup mode:
          • Standby mode:
            When entering standby mode, the PDSYSRAM power domain can be either fully or partially retained
            or be fully off according to STDBYCFG.RAMCFG bits. When running sleepwalking task, PDSYSRAM
            power domain is active whatever the STDBYCFG.RAMCFG bits are.
          • Hibernate mode:
            When entering hibernate mode, the PDCORESW power domain is off. As in standby mode, the
            PDSYSRAM power domain can be selectively turned ON or OFF by using the HIBCFG.RAMCFG
            bits. PDBKUPRAM power domain can be either fully or partially retained or be fully off according to
            HIBCFG.BRAMCFG bits. If partial option is selected, only the lowest 4KBytes section is retained
          • Backup mode:
            When entering backup mode, the PDCORESW and PDSYSRAM power domains are off.
            PDBACKUP is still active. As in hibernate mode, PDBKUPRAM power domain can be either fully or
            partially retained or be fully off according to BKUPCFG.BRAMCFG bits.
          • OFF mode:
            When entering OFF mode, all the power domains are off.
         The table below illustrates the PDRAM state:




        © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 219
                                              SAM D5x/E5x Family Data Sheet
                                                                      PM – Power Manager

Table 18-3. Sleep Mode versus PDSYSRAM Power Domain State Overview

                                              Power Domain State
 Sleep Mode             STDBYCFG HIBCFG.RA PDCORESW          PDBACKUP      PDSYSRAM
                        .RAMCFG  MCFG
 Active                 N/A        N/A        active         active        active
 Idle                   N/A        N/A        active         active        active
 Standby with           N/A        N/A        active         active        active
 sleepwalking
 Standby - case 1 RET              N/A        active         active        retained
 Standby - case 2 PARTIAL          N/A        active         active        32K retained
 Standby - case 3 OFF              N/A        active         active        off
 Hibernate - case       N/A        RET        off            active        retained
 1
 Hibernate - case       N/A        PARTIAL    off            active        32K retained
 2
 Hibernate - case       N/A        OFF        off            active        off
 3
 Backup                 N/A        N/A        off            active        off
 Off                    N/A        N/A        off            off           off

The table below illustrates the PDBKUPRAM state:
Table 18-4. Sleep Mode versus PDBKUPRAM Power Domain State Overview

                                              Power Domain State
 Sleep Mode             HIBCFG.BR BKUPCFG.    PDCORESW       PDBACKUP      PDBKUPRAM
                        AMCFG     BRAMCFG
 Active                 N/A        N/A        active         active        active
 Idle                   N/A        N/A        active         active        active
 Standby                N/A        N/A        active         active        retained
 Hibernate - case       RET        N/A        off            active        retained
 1
 Hibernate - case       PARTIAL    N/A        off            active        4KB retained
 2
 Hibernate - case       OFF        N/A        off            active        off
 3
 Backup                 N/A        RET        off            active        retained
 Backup                 N/A        PARTIAL    off            active        4KB retained
 Backup                 N/A        OFF        off            active        off




© 2019 Microchip Technology Inc.                Datasheet                 DS60001507E-page 220
                                                            SAM D5x/E5x Family Data Sheet
                                                                                         PM – Power Manager

        ...........continued
                                                            Power Domain State
         Sleep Mode             HIBCFG.BR BKUPCFG.          PDCORESW         PDBACKUP          PDBKUPRAM
                                AMCFG     BRAMCFG
         Off                    N/A         N/A             off              off               off

18.6.3.6 Regulators, RAMs, and NVM State in Sleep Mode
        By default, in standby sleep mode and backup sleep mode, the RAMs, NVM, and regulators are
        automatically set in low-power mode in order to reduce power consumption:
          • The RAM is in low-power mode if the device is in standby mode.
          • Non-Volatile Memory - the NVM is automatically set in low power mode in these conditions:
             – When the device is in standby sleep mode and the NVM is not accessed. This behavior can be
                changed by software by configuring the SLEEPPRM bit group of the CTRLB register in the
                NVMCTRL peripheral.
             – When the device is in idle sleep mode and the NVM is not accessed. This behavior can be
                changed by software by configuring the SLEEPPRM bit group of the CTRLB register in the
                NVMCTRL peripheral.
          • Regulators: by default, in standby sleep mode, the PM analyzes the device activity to use either the
            main or the low-power voltage regulator to supply the VDDCORE.
        GCLK clocks, regulators and RAM are not affected in idle sleep mode and will operate as normal.
        Table 18-5. Regulators, RAMs, and NVM state in Sleep Mode

         Sleep Mode             SRAM Mode         NVM              Regulators
                                                                   VDDCORE                     VDDBU
                                                                   main            ULP
         Active                 normal            normal           on              on          on
         Idle                   auto(1)           on               on              on          on
         Standby - case 1       normal            auto(1)          auto(2)         on          on
         Standby - case 2       low power         low power        auto(2)         on          on
         Standby - case 3       low power         low power        auto(2)         on          on
         Standby - case 4       low power         low power        off             on          on
         Backup                 off               off              off             off         on
         OFF                    off               off              off             off         off

        Note:
         1. auto: by default, NVM is in low-power mode if not accessed.
         2. auto: by default, the main voltage regulator is on if GCLK, APBx, or AHBx clock is running during
              SleepWalking.
        Related Links
        18.6.3.5 Power Domain Controller




        © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 221
                                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                                       PM – Power Manager

18.6.4   Advanced Features

18.6.4.1 SleepWalking
         SleepWalking is the capability for a device to temporarily wake up clocks for a peripheral to perform a
         task without waking up the CPU from STANDBY sleep mode. At the end of the sleepwalking task, the
         device can either be woken p by an interrupt (from a peripheral involved in SleepWalking) or enter again
         into STANDBY sleep mode. In this device, SleepWalking is supported only on GCLK clocks by using the
         on-demand clock principle of the clock sources.
         In standby, when SleepWalking is ongoing:
               • All the power domains are turned ON including PDRAM power domain.
               • The MAINVREG regulator used to execute the sleepwalking task is the selected regulator used in
                 active mode (LDO or Buck converter). Low power mode of the MAINVREG is not activated during
                 sleepwalking.
         These are illustrated in the figure below.
         Figure 18-2. Operating Conditions and SleepWalking
                       Sleep modes                               Regulator modes                        System RAM Backup RAM PDCORESW
                         RESET                                   RESET


                                                                             SUPC.
                                                                            VREG.SEL
                                    ACTIVE                                                                ACTIVE        ACTIVE             ACTIVE


                                                                   LDO                    BUCK


                            IRQ                                                                            ACTIVE        ACTIVE             ACTIVE
                                     IDLE
                                                 Sleep Mode
          Sleep Mode




                            IRQ                                    LDO                                     ACTIVE       ACTIVE             ACTIVE
                                  SleepWalking                                                BUCK




                           IRQ
                                   STANDBY                          LDO                    BUCK
                                                              (low power mode)       (low power mode)    SELECTABLE
                                                                                                         0/32KB/FULL    ACTIVE
                                                                                                          Retention
                         RESET                                       LDO                   BUCK
                                  HIBERNATE                   (low power mode)       (low power mode)
                                                                                                                                             OFF

                         RESET                                                                                         SELECTABLE
                                   BACKUP                                    LPVREG                        OFF           0/4/8KB
                                                                                                                        Retention

                                     OFF                                 Regulators are OFF                OFF           OFF



18.6.4.2 Wake-Up Time
         As shown in the figure below, total wake-up time depends on:
               • Latency due to Power Domain Gating:
                 Usually, wake-up time is measured with the assumption that the power domains are already in active
                 state. When using Power Domain Gating, changing a power domain from OFF to active state will
                 take a certain time, refer to Electrical Characteristics. If all power domains were already in active
                 state in standby sleep mode, this latency is zero.
               • Latency due to Regulator effect:




         © 2019 Microchip Technology Inc.                                               Datasheet                                 DS60001507E-page 222
                                                                              SAM D5x/E5x Family Data Sheet
                                                                                                                          PM – Power Manager

             As example, if the device is in standby sleep mode using the main voltage regulator (MAINVREG) in
             low power mode, the voltage level is lower than the one used in active mode. When the device
             wakes up, it takes a certain amount of time for the main regulator to transition to the voltage level
             corresponding to active mode, causing additional wake-up time.
           • Latency due to the CPU clock source wake-up time.
           • Latency due to the NVM memory access.
             Note: NVM and MAINVREG latencies can be reduced by setting the Fast Wake-Up bits in the
             Standby Configuration register (STDBYCFG.FASTWKUP).
         Figure 18-3. Total Wake-up Time from Standby Sleep Mode
                                1: latency due to power domain gating
                                2: latency due to regulator wakeup time
                                3: latency due to clock source wakeup time            IRQ from module
                                4: latency due to flash memory code access




                                   PDRAM           active                       OFF                         active
                                                                                               1
                                   VDDCORE
                                                 Main regulator         Main regulator                      Main regulator
                                                 Normal mode           Low Power mode                       Normal mode
                                                                                                        2
                                                                                                              3

                                    CLK_CPU        ON                           OFF                                      ON
                                                                                                                     3


                                                 WFI instruction                                                  interrupt handler
                                CPU state         run                   standby sleep mode                                    run


         Related Links
         18.6.1.1 Power Domains

18.6.5   DMA Operation
         Not applicable.

18.6.6   Interrupts
         The peripheral has the following interrupt sources:
           • Sleep Mode Entry Ready (SLEEPRDY): indicates that the device is ready to enter standby, hibernate
             or backup sleep mode.
             This interrupt is a synchronous wake-up source.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable Set (INTENSET)
         register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
         register.
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled or the
         peripheral is reset.
         An interrupt flag is cleared by writing a '1' to the corresponding bit in the INTFLAG register. Each
         peripheral can have one interrupt request line per interrupt source or one common interrupt request line
         for all the interrupt sources. If the peripheral has one common interrupt request line for all the interrupt
         sources, the user must read the INTFLAG register to determine which interrupt condition is present.




         © 2019 Microchip Technology Inc.                                       Datasheet                                             DS60001507E-page 223
                                               SAM D5x/E5x Family Data Sheet
                                                              PM – Power Manager

18.6.7   Events
         Not applicable.

18.6.8   Sleep Mode Operation
         The Power Manager is always active.




         © 2019 Microchip Technology Inc.      Datasheet          DS60001507E-page 224
                                                            SAM D5x/E5x Family Data Sheet
                                                                                            PM – Power Manager


18.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                                                         IORET
 0x01       SLEEPCFG          7:0                                                                 SLEEPMODE[2:0]
 0x02
   ...       Reserved
 0x03
 0x04        INTENCLR         7:0                                                                              SLEEPRDY
 0x05        INTENSET         7:0                                                                              SLEEPRDY
 0x06        INTFLAG          7:0                                                                              SLEEPRDY
 0x07        Reserved
 0x08       STDBYCFG          7:0                         FASTWKUP[1:0]                                  RAMCFG[1:0]
 0x09         HIBCFG          7:0                                                BRAMCFG[1:0]            RAMCFG[1:0]
 0x0A        BKUPCFG          7:0                                                                       BRAMCFG[1:0]
 0x0B        Reserved
 0x0C       PWSAKDLY          7:0     IGNACK                                DLYVAL[6:0]




18.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to Register Access Protection section.
          Related Links
          18.5.7 Register Access Protection




          © 2019 Microchip Technology Inc.                    Datasheet                             DS60001507E-page 225
                                                                SAM D5x/E5x Family Data Sheet
                                                                                              PM – Power Manager

18.8.1         Control A

               Name:       CTRLA
               Offset:     0x00
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6            5            4            3             2            1            0
                                                                                    IORET
   Access                                                                            R/W
    Reset                                                                              0


               Bit 2 – IORET I/O Retention
               Note: This bit is not reset by a hibernate or backup reset. When the IORET feature is used, the
               debugger access to the chip will not be allowed until the IORET bit is cleared after waking up from
               hibernate or backup sleep. When the IORET is set in active mode, the PORT can still be controlled by
               peripherals and the PORT registers. It is only when the device wakes up from hibernate or backup sleep
               mode that the IORET= 1 will prevent the PORT from being controlled by the peripherals or PORT
               registers. POR and BOD33 resets can clear the IORET bit.
               Value       Description
               0           After waking up from Hibernate or Backup mode, I/O lines are not held.
               1           After waking up from Hibernate or Backup mode, I/O lines are held until IORET is written to
                           0.




           © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 226
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          PM – Power Manager

18.8.2         Sleep Configuration

               Name:       SLEEPCFG
               Offset:     0x01
               Reset:      0x02
               Property:   PAC Write-Protection


         Bit         7            6           5            4           3            2           1            0
                                                                                          SLEEPMODE[2:0]
   Access                                                                         R/W          R/W          R/W
    Reset                                                                           0           0            0


               Bits 2:0 – SLEEPMODE[2:0] Sleep Mode
               Note: A small latency happens between the store instruction and actual writing of the SLEEPCFG
               register due to bridges. Software has to make sure the SLEEPCFG register reads the wanted value
               before issuing WFI instruction.

               Value       Name               Definition
               0x0         Reserved           -
               0x1         Reserved           -
               0x2         IDLE               CPU, AHBx, and APBx clocks are OFF
               0x3         Reserved           Reserved
               0x4         STANDBY            All Clocks are OFF
               0x5         HIBERNATE          Backup domain is ON as well as some PDRAMs
               0x6         BACKUP             Only Backup domain is powered ON
               0x7         OFF                All power domains are powered OFF




           © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 227
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                PM – Power Manager

18.8.3         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x04
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

         Bit         7            6             5             4            3             2            1             0
                                                                                                                SLEEPRDY
   Access                                                                                                           W
    Reset                                                                                                           0


               Bit 0 – SLEEPRDY Sleep Mode Entry Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Sleep Mode Entry Ready Interrupt Enable bit and the corresponding
               interrupt request.
                Value        Description
                0            The Sleep Mode Entry Ready interrupt is disabled.
                1            The Sleep Mode Entry Ready interrupt is enabled and will generate an interrupt request
                             when the Sleep Mode Entry Ready Interrupt Flag is set.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 228
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                PM – Power Manager

18.8.4         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x05
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

         Bit         7            6             5             4            3             2            1             0
                                                                                                                SLEEPRDY
   Access                                                                                                          R/W
    Reset                                                                                                           0


               Bit 0 – SLEEPRDY Sleep Mode Entry Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Sleep Mode Entry Ready Interrupt Enable bit and enable the Sleep
               Mode Entry Ready interrupt.
               Value         Description
               0             The Sleep Mode Entry Ready interrupt is disabled.
               1             The Sleep Mode Entry Ready interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 229
                                                                SAM D5x/E5x Family Data Sheet
                                                                                             PM – Power Manager

18.8.5         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x06
               Reset:      0x00
               Property:   –


         Bit         7            6            5            4            3            2            1            0
                                                                                                           SLEEPRDY
   Access                                                                                                     R/W
    Reset                                                                                                       0


               Bit 0 – SLEEPRDY Sleep Mode Entry Ready
               This flag is set when the main very low power mode is ready and will generate an interrupt if INTENCLR/
               SET.SLEEPRDY is '1'. See this Note for details.
               Writing a '1' to this bit has no effect.
               Writing a '1' to this bit clears the Performance Ready interrupt flag.




           © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 230
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          PM – Power Manager

18.8.6         Hibernate Configuration

               Name:       HIBCFG
               Offset:     0x09
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5           4            3           2            1                 0
                                                                        BRAMCFG[1:0]                RAMCFG[1:0]
   Access                                                             R/W         R/W          R/W            R/W
    Reset                                                              0           0            0                 0


               Bits 3:2 – BRAMCFG[1:0] Backup RAM Configuration
               Value       Name     Description
               0x0         RET      In hibernate mode, all the backup RAM is retained.
               0x1         PARTIAL In hibernate mode, only the first 4Kbytes of the backup RAM is retained.
               0x2         OFF      In hibernate mode, all the backup RAM is turned OFF.
               0x3         Reserved Reserved.

               Bits 1:0 – RAMCFG[1:0] RAM Configuration
               Value       Name     Description
               0x0         RET      In hibernate mode, all the system RAM is retained.
               0x1         PARTIAL In hibernate mode, only the first 32Kbytes of the system RAM is retained.
               0x2         OFF      In hibernate mode, all the system RAM is turned OFF.
               0x3         Reserved Reserved.




           © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 231
                                                                SAM D5x/E5x Family Data Sheet
                                                                                          PM – Power Manager

18.8.7         Standby Configuration

               Name:       STDBYCFG
               Offset:     0x08
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6            5           4          3            2           1                 0
                                               FASTWKUP[1:0]                                       RAMCFG[1:0]
   Access                                     R/W         R/W                                 R/W            R/W
    Reset                                      0           0                                   0                 0


               Bits 5:4 – FASTWKUP[1:0] Fast Wakeup
               Value       Name       Description
               0x0         NO         Fast Wakeup is disabled.
               0x1         NVM        Fast Wakeup is enabled on NVM.
               0x2         MAINVREG Fast Wakeup is enabled on the main voltage regulator (MAINVREG).
               0x3         BOTH       Fast Wakeup is enabled on both NVM and MAINVREG..

               Bits 1:0 – RAMCFG[1:0] RAM Configuration
               Value       Name     Description
               0x0         RET      In standby mode, all the system RAM is retained.
               0x1         PARTIAL In standby mode, only the first 32Kbytes of the system RAM is retained.
               0x2         OFF      In standby mode, all the system RAM is turned OFF.
               0x3         Reserved Reserved.




           © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 232
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          PM – Power Manager

18.8.8         Backup Configuration

               Name:       BKUPCFG
               Offset:     0x0A
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5           4            3           2            1            0
                                                                                                BRAMCFG[1:0]
   Access                                                                                     R/W           R/W
    Reset                                                                                       0            0


               Bits 1:0 – BRAMCFG[1:0] Backup RAM Configuration
               Value       Name     Description
               0x0         RET      In backup mode, all the backup RAM is retained.
               0x1         PARTIAL  In backup mode, only the first 4Kbytes of the backup RAM is retained.
               0x2         OFF      In backup mode, all the backup RAM is turned OFF.
               0x3         Reserved Reserved.




           © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 233
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                PM – Power Manager

18.8.9         Global Status

               Name:        PWSAKDLY
               Offset:      0xC [ID-00000a2f]
               Reset:       0x00
               Property:    –


         Bit         7            6             5            4             3            2             1             0
                  IGNACK                                              DLYVAL[6:0]
   Access            R            R             R            R             R            R             R            R
    Reset            0            0             0            0             0            0             0             0


               Bit 7 – IGNACK Ignore Acknowledge signal
               Value      Description
               0          Power Switch acknowledge signal is taken into account when entering/exiting retention
                          mode. According to the DLYVAL field, a supplementary delay is also added (from 0 to 127
                          digital ring oscillator period).
               1          Power Switch acknowledge signal is ignored when entering/exiting retention mode, and is
                          replaced by a overflow counter signal clocked on internal digital ring oscillator. The overflow
                          counter is programmable by using the DLYVAL field.

               Bits 6:0 – DLYVAL[6:0] Delay value
               Value of the counter overflow. See the IGNACK bit description to get more details.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 234
