# 13. Clock System

*Source: `Atmel-SAMD51.pdf`, pages 145-151 — SAMD51 family datasheet*

                                                               SAM D5x/E5x Family Data Sheet
                                                                                                                             Clock System


13.    Clock System
       This chapter summarizes the clock distribution and terminology in the SAM D5x/E5x device. It does not
       explain every detail of its configuration. For in-depth documentation, see the respective peripherals
       descriptions and the Generic Clock documentation.
       Related Links
       14. GCLK - Generic Clock Controller
       15. MCLK – Main Clock



13.1   Clock Distribution
       Figure 13-1. Clock Distribution
                                                                      GCLK_DFLL48M_REF                                  MCLK

                               OSCCTRL             GCLK                                                   GCLK_MAIN         Syncronous Clock
                                                                                                                               Controller
                                  XOSCn                                     Peripheral Channel 0
                                                   GCLK Generator 0
                                                                            (DFLL48M Reference)
                                 DFLL48M

                                                   GCLK Generator 1         Peripheral Channel [2:1]
           GCLK_DPLLn                                                                                       GCLK_DPLLn
           GCLK_DPLLn_32K       FDPLL200M                                   (FDPLL200M Reference)


                                                   GCLK Generator x         Peripheral Channel 3
                                                                                                            GCLK_DPLLn_32K
                                                                            (FDPLL200M lock ref)
                               OSCK32CTRL

                               XOSC32K
                                           32kHz
                                                                             Peripheral Channel 4                  Peripheral 0
                                            1kHz

                                                                                                       Generic
                                                                                                       Clocks
                                           32kHz
                               OSCULP32K 1kHz                                Peripheral Channel y                  Peripheral z




                                                                                                                                       AHB/APB System Clocks
                                                          CLK_RTC_OSC
                                                                                                                       RTC



                                                          CLK_WDT_OSC
                                                                                                                      WDT


                                                           CLK_ULP32K
                                                                                                                      EIC



                                                                                                   Generic Clock      USB


                                                                                                        GTXCK
                                                                                                                     GMAC
                                                                                                        GRXCK


                                                                                                        CLK
                                                                                                                      PCC


       The SAM D5x/E5x clock system consists of:
         • Clock sources, i.e. oscillators controlled by OSCCTRL and OSC32KCTRL
            – A clock source provides a time base that is used by other components, such as Generic Clock
               Generators. Example clock sources are the external crystal oscillator (XOSC) and the Digital
               Frequency Locked Loop (DFLL48M).
         • Generic Clock Controller (GCLK), which generates, controls and distributes the asynchronous clock
           consisting of:




       © 2019 Microchip Technology Inc.                          Datasheet                                              DS60001507E-page 145
                                                           SAM D5x/E5x Family Data Sheet
                                                                                                             Clock System

       – Generic Clock Generators: These are programmable prescalers that can use any of the system
         clock sources as a time base. The Generic Clock Generator 0 generates the clock signal
         GCLK_MAIN, which is used by the Power Manager and the Main Clock (MCLK) module, which
         in turn generates synchronous clocks.
       – Generic Clocks: These are clock signals generated by Generic Clock Generators and output by
         the Peripheral Channels, and serve as clocks for the peripherals of the system. Multiple
         instances of a peripheral will typically have a separate Generic Clock for each instance. Generic
         Clock 0 serves as the clock source for the DFLL48M clock input (when multiplying another clock
         source).
  • Main Clock Controller (MCLK)
     – The MCLK generates and controls the synchronous clocks on the system. This includes the
        CPU, bus clocks (APB, AHB) as well as the synchronous (to the CPU) user interfaces of the
        peripherals. It contains clock masks that can turn on/off the user interface of a peripheral as well
        as prescalers for the CPU and bus clocks.

          The next figure shows an example where SERCOM0 is clocked by the DFLL48M in open
          loop mode. The DFLL48M is enabled, the Generic Clock Generator 1 uses the DFLL48M
          as its clock source and feeds into Peripheral Channel 7. The Generic Clock 7, also called
          GCLK_SERCOM0_CORE, is connected to SERCOM0. The SERCOM0 interface,
          clocked by CLK_SERCOM0_APB, has been unmasked in the APBC Mask register in the
          MCLK.
          Figure 13-2. Example of SERCOM Clock
                                                                                        MCLK

                                                                                          Syncronous Clock
                                                                                             Controller



                                                                              CLK_SERCOM0_APB
                                   GCLK
                  OSCCTRL
                                      Generic Clock   Peripheral    GCLK_SERCOM0_CORE
                    DFLL48M                                                                    SERCOM 0
                                      Generator 1     Channel 7



          To customize the clock distribution, refer to these registers and bit fields:
           • The source oscillator for a generic clock generator n is selected by writing to the
              Source bit field in the Generator Control n register (GCLK.GENCTRLn.SRC).
           • A Peripheral Channel m can be configured to use a specific Generic Clock
              Generator by writing to the Generic Clock Generator bit field in the respective
              Peripheral Channel m register (GCLK.PCHCTRLm.GEN)
           • The Peripheral Channel number, m, is fixed for a given peripheral. See the Mapping
              table in the description of GCLK.PCHCTRLm.
           • The AHB clocks are enabled and disabled by writing to the respective bit in the AHB
              Mask register (MCLK.AHBMASK).
           • The APB clocks are enabled and disabled by writing to the respective bit in the APB
              x Mask registers (MCLK.APBxMASK).

Related Links
13.7 Clocks after Reset




© 2019 Microchip Technology Inc.                              Datasheet                                DS60001507E-page 146
                                                            SAM D5x/E5x Family Data Sheet
                                                                                                   Clock System


13.2     Synchronous and Asynchronous Clocks
         As the CPU and the peripherals can be in different clock domains, i.e. they are clocked from different
         clock sources and/or with different clock speeds, some peripheral accesses by the CPU need to be
         synchronized. In this case the peripheral includes a Synchronization Busy (SYNCBUSY) register that can
         be used to check if a sync operation is in progress.
         For a general description, see 13.3 Register Synchronization. Some peripherals have specific properties
         described in their individual sub-chapter “Synchronization”.
         In the datasheet, references to Synchronous Clocks are referring to the CPU and bus clocks (MCLK),
         while asynchronous clocks are generated by the Generic Clock Controller (GCLK).
         Related Links
         14.6.6 Synchronization



13.3     Register Synchronization

13.3.1   Overview
         All peripherals are composed of one digital bus interface connected to the APB or AHB bus and running
         from a corresponding clock in the Main Clock domain, and one peripheral core running from the
         peripheral Generic Clock (GCLK).
         Communication between these clock domains must be synchronized. This mechanism is implemented in
         hardware, so the synchronization process takes place even if the peripheral generic clock is running from
         the same clock source and on the same frequency as the bus interface.
         All registers in the bus interface are accessible without synchronization.
         All registers in the peripheral core are synchronized when written. Some registers in the peripheral core
         are synchronized when read.
         Each individual register description will have the properties "Read-Synchronized" and/or "Write-
         Synchronized" if a register is synchronized.
         As shown in the figure below, each register that requires synchronization has its individual synchronizer
         and its individual synchronization status bit in the Synchronization Busy register (SYNCBUSY).
         Note: For registers requiring both read- and write-synchronization, the corresponding bit in SYNCBUSY
         is shared.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 147
                                                           SAM D5x/E5x Family Data Sheet
                                                                                                    Clock System

         Figure 13-3. Register Synchronization Overview
                       Synchronous Domain                                 Asynchronous Domain
                            (CLK_APB)                                           (GCLK)

                               Non Sync’d reg

                                 SYNCBUSY




                                                           Sync
                                                                             Write-Sync’d reg Write-only register




                                                           Sync
                                                                             Read-Sync’d reg Read-only register




                                                           Sync
              Periperal Bus                                                   R/W-Sync’d reg       R/W register



                                                                             Write-Sync’d reg R/W register
                                                           Sync




                                                                              Non Sync’d reg       Read-only register
                                                           Sync




                                   INTFLAG




13.3.2   General Write Synchronization
         Write-Synchronization is triggered by writing to a register in the peripheral clock domain (GCLK). The
         respective bit in the Synchronization Busy register (SYNCBUSY) will be set when the write-
         synchronization starts and cleared when the write-synchronization is complete. Refer also to 13.3.7
         Synchronization Delay.
         When write-synchronization is ongoing for a register, any subsequent write attempts to this register will be
         discarded, and an error will be reported though the Peripheral Access Controller (PAC).
         Example:
         REGA, REGB are 8-bit core registers. REGC is a 16-bit core register.

                                Offset                  Register
                                 0x00                   REGA
                                 0x01                   REGB
                                 0x02                   REGC
                                 0x03

         Synchronization is per register, so multiple registers can be synchronized in parallel. Consequently, after
         REGA (8-bit access) was written, REGB (8-bit access) can be written immediately without error.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 148
                                                           SAM D5x/E5x Family Data Sheet
                                                                                                   Clock System

         REGC (16-bit access) can be written without affecting REGA or REGB. If REGC is written to in two
         consecutive 8-bit accesses without waiting for synchronization, the second write attempt will be discarded
         and an error is generated through the PAC.
         A 32-bit access to offset 0x00 will write all three registers. Note that REGA, REGB and REGC can be
         updated at different times because of independent write synchronization.

13.3.3   General Read Synchronization
         Read-synchronized registers are synchronized each time the register value is updated but the
         corresponding SYNCBUSY bits are not set. Reading a read-synchronized register does not start a new
         synchronization, it returns the last synchronized value.
         Note: The corresponding bits in SYNCBUSY will automatically be set when the device wakes up from
         sleep because read-synchronized registers need to be synchronized. Therefore reading a read-
         synchronized register before its corresponding SYNCBUSY bit is cleared will return the last synchronized
         value before sleep mode.
         However, if a register is also write-synchronized, any write access while the SYNCBUSY bit is set will be
         executed successfully. If concurrent read and write access is detected, the read is discarded and a new
         synchronization will start.

13.3.4   Completion of Synchronization
         In order to check if synchronization is complete, the user can either poll the relevant bits in SYNCBUSY
         or use the Synchronisation Ready interrupt (if available). The Synchronization Ready interrupt flag will be
         set when all ongoing synchronizations are complete, i.e. when all bits in SYNCBUSY are '0'.

13.3.5   Write Synchronization for CTRLA.ENABLE
         Setting the Enable bit in a module's Control A register (CTRLA.ENABLE) will trigger write-synchronization
         and set SYNCBUSY.ENABLE.
         CTRLA.ENABLE will read its new value immediately after being written.
         SYNCBUSY.ENABLE will be cleared by hardware when the operation is complete.
         The Synchronization Ready interrupt (if available) cannot be used to enable write-synchronization.

13.3.6   Write-Synchronization for Software Reset Bit
         Setting the Software Reset bit in CTRLA (CTRLA.SWRST=1) will trigger write-synchronization and set
         SYNCBUSY.SWRST. When writing a ‘1’ to the CTRLA.SWRST bit it will immediately read as ‘1’.
         CTRL.SWRST and SYNCBUSY.SWRST will be cleared by hardware when the peripheral has been reset.
         Writing a '0' to the CTRL.SWRST bit has no effect.
         The Ready interrupt (if available) cannot be used for Software Reset write-synchronization.
         Note: Not all peripherals have the SWRST bit in the respective CTRLA register.

13.3.7   Synchronization Delay
         The synchronization will delay write and read accesses by a certain amount. This delay D is within the
         range of:
         5×PGCLK + 2×PAPB < D < 6×PGCLK + 3×PAPB
         Where PGCLK is the period of the generic clock and PAPB is the period of the peripheral bus clock. A
         normal peripheral bus register access duration is 2×PAPB.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 149
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                               Clock System


13.4   Enabling a Peripheral
       In order to enable a peripheral that is clocked by a Generic Clock, the following parts of the system needs
       to be configured:
         • A running Clock Source
         • A clock from the Generic Clock Generator must be configured to use one of the running Clock
           Sources, and the Generator must be enabled.
         • The Peripheral Channel that provides the Generic Clock signal to the peripheral must be configured
           to use a running Generic Clock Generator, and the Generic Clock must be enabled.
         • The user interface of the peripheral needs to be unmasked in the PM. If this is not done the
           peripheral registers will read all 0’s and any writing attempts to the peripheral will be discarded.



13.5   On Demand Clock Requests
       Figure 13-4. Clock Request Routing
                           Clock request                   Clock request                     Clock request
                                           Generic Clock                   Generic Clock
              DFLL48M                                                                                             Peripheral
                                           Generator                       Periph. Channel


               ENABLE                         GENEN                           CLKEN                               ENABLE

             RUNSTDBY                       RUNSTDBY                                                            RUNSTDBY

             ONDEMAND

       All clock sources in the system can be run in an on-demand mode: the clock source is in a stopped state
       unless a peripheral is requesting the clock source. Clock requests propagate from the peripheral, via the
       GCLK, to the clock source. If one or more peripheral is using a clock source, the clock source will be
       started/kept running. As soon as the clock source is no longer needed and no peripheral has an active
       request, the clock source will be stopped until requested again.
       The clock request can reach the clock source only if the peripheral, the generic clock and the clock from
       the Generic Clock Generator in-between are enabled. The time taken from a clock request being
       asserted to the clock source being ready is dependent on the clock source startup time, clock source
       frequency as well as the divider used in the Generic Clock Generator. The total startup time Tstart from a
       clock request until the clock is available for the peripheral is between:
       Tstart_max = Clock source startup time + 2 × clock source periods + 2 × divided clock source periods
       Tstart_min = Clock source startup time + 1 × clock source period + 1 × divided clock source period
       The time between the last active clock request stopped and the clock is shut down, Tstop, is between:
       Tstop_min = 1 × divided clock source period + 1 × clock source period
       Tstop_max = 2 × divided clock source periods + 2 × clock source periods
       The On-Demand function can be disabled individually for each clock source by clearing the ONDEMAND
       bit located in each clock source controller. Consequently, the clock will always run whatever the clock
       request status is. This has the effect of removing the clock source startup time at the cost of power
       consumption.
       The clock request mechanism can be configured to work in standby mode by setting the RUNSDTBY bits
       of the modules, see Figure 13-4.




       © 2019 Microchip Technology Inc.                          Datasheet                                   DS60001507E-page 150
                                                          SAM D5x/E5x Family Data Sheet
                                                                                                  Clock System


13.6   Power Consumption vs. Speed
       When targeting for either a low-power or a fast acting system, some considerations have to be taken into
       account due to the nature of the asynchronous clocking of the peripherals:
       If clocking a peripheral with a very low clock, the active power consumption of the peripheral will be lower.
       At the same time the synchronization to the synchronous (CPU) clock domain is dependent on the
       peripheral clock speed, and will take longer with a slower peripheral clock. This will cause worse
       response times and longer synchronization delays.



13.7   Clocks after Reset
       On any Reset the synchronous clocks start to their initial state:
         • DFLL48M is enabled and configured to run at 48MHz
         • Generic Generator 0 uses DFLL48M as source and generates GCLK_MAIN
         • CPU and BUS clocks are undivided
       On a Power-on Reset, the 32KHz clock sources are reset and the GCLK module starts to its initial state:
         • All Generic Clock Generators are disabled except
            – Generator 0 is using DFLL48M at 48MHz as source and generates GCLK_MAIN
         • All Peripheral Channels in GCLK are disabled.
       On a User Reset the GCLK module starts to its initial state, except for:
         • Generic Clocks that are write-locked, i.e., the according WRTLOCK is set to 1 prior to Reset
       Related Links
       16. RSTC – Reset Controller




       © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 151
