# 14. GCLK - Generic Clock Controller

*Source: `Atmel-SAMD51.pdf`, pages 152-169 — SAMD51 family datasheet*

                                                               SAM D5x/E5x Family Data Sheet
                                                                                GCLK - Generic Clock Controller


14.    GCLK - Generic Clock Controller

14.1   Overview
       Depending on the application, peripherals may require specific clock frequencies to operate correctly. The
       Generic Clock controller (GCLK) features 12 Generic Clock Generators [11:0] that can provide a wide
       range of clock frequencies.
       Generators can be set to use different external and internal oscillators as source. The clock of each
       Generator can be divided. The outputs from the Generators are used as sources for the Peripheral
       Channels, which provide the Generic Clock (GCLK_PERIPH) to the peripheral modules, as shown in
       Figure 14-2. The number of Peripheral Clocks depends on how many peripherals the device has.
       Note: The Generator 0 is always the direct source of the GCLK_MAIN signal.


14.2   Features
         • Provides a device-defined, configurable number of Peripheral Channel clocks
         • Wide frequency range:
            – Various clock sources
            – Embedded dividers


14.3   Block Diagram
       The generation of Peripheral Clock signals (GCLK_PERIPH) and the Main Clock (GCLK_MAIN) can be
       seen in Device Clocking Diagram.
       Figure 14-1. Device Clocking Diagram

                                GENERIC CLOCK CONTROLLER




                                     Generic Clock Generator

        OSCCTRL

            XOSC0

            XOSC1

            DFLL

            FDPLL0                                              Peripheral Channel

            FDPLL1                                                                        GCLK_PERIPH

        OSC32KCTRL                               Clock                          Clock
                                                 Divider &                      Gate                    PERIPHERAL
            XOSC32K
                                                 Masker
          OSCULP32K




        GCLK_IO
                                                                                           GCLK_MAIN
                                                                                                           MCLK




       © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 152
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                        GCLK - Generic Clock Controller

         The GCLK block diagram is shown below:
         Figure 14-2. Generic Clock Controller Block Diagram
                                            Generic Clock Generator 0                                         GCLK_MAIN
                                                                                                                   GCLK_IO[0]
                         Clock Sources                      Clock       GCLKGEN[0]                                 (I/O output)
                                                            Divider &                 Peripheral Channel 0
                            GCLK_IO[0]
                             (I/O input)                    Masker
                                                                                                      Clock    GCLK_PERIPH[0]
                                                                                                      Gate

                                            Generic Clock Generator 1                                              GCLK_IO[1]
                                                                                                                   (I/O output)
                                                                                      Peripheral Channel 1
                                                            Clock       GCLKGEN[1]
                            GCLK_IO[1]                      Divider &                                          GCLK_PERIPH[1]
                                                                                                      Clock
                             (I/O input)                    Masker
                                                                                                      Gate



                                            Generic Clock Generator n
                                                                                                                   GCLK_IO[n]
                                                           Clock                                                   (I/O output)
                                                                        GCLKGEN[n]
                                                           Divider &
                                                           Masker                     Peripheral Channel n
                            GCLK_IO[n]
                             (I/O input)
                                                                                                      Clock    GCLK_PERIPH[n]
                                                                                                      Gate


                                                                              GCLKGEN[n:0]




14.4     Signal Description
         Table 14-1. GCLK Signal Description

          Signal Name                               Type                                          Description
          GCLK_IO[7:0]                              Digital I/O                                   Clock source for Generators
                                                                                                  when input
                                                                                                  Generic Clock signal when output

         Note: One signal can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations


14.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

14.5.1   I/O Lines
         Using the GCLK I/O lines requires the I/O pins to be configured.
         Related Links
         32. PORT - I/O Pin Controller

14.5.2   Power Management
         The GCLK can operate in sleep modes, if required. Refer to the Sleep mode description in the Power
         Manager (PM) section.
         Related Links
         18. PM – Power Manager




         © 2019 Microchip Technology Inc.                               Datasheet                                    DS60001507E-page 153
                                                            SAM D5x/E5x Family Data Sheet
                                                                           GCLK - Generic Clock Controller

14.5.3    Clocks
          The GCLK bus clock (CLK_GCLK_APB) can be enabled and disabled in the Main Clock Controller.
          Related Links
          15.6.2.6 Peripheral Clock Masking
          29. OSC32KCTRL – 32KHz Oscillators Controller

14.5.4    DMA
          Not applicable.

14.5.5    Interrupts
          Not applicable.

14.5.6    Events
          Not applicable.

14.5.7    Debug Operation
          When the CPU is halted in debug mode the GCLK continues normal operation. If the GCLK is configured
          in a way that requires it to be periodically serviced by the CPU through interrupts or similar, improper
          operation or data loss may result during debugging.

14.5.8    Register Access Protection
          All registers with write access can be optionally write-protected by the Peripheral Access Controller
          (PAC).
          Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
          description.
          Write protection does not apply for accesses through an external debugger.

          Related Links
          27. PAC - Peripheral Access Controller

14.5.9    Analog Connections
          Not applicable.



14.6      Functional Description

14.6.1    Principle of Operation
          The GCLK module is comprised of twelve Generic Clock Generators (Generators) sourcing up to 64
          Peripheral Channels and the Main Clock signal CLK_MAIN.
          A clock source selected as input to a Generator can either be used directly, or it can be prescaled in the
          Generator. A generator output is used by one or more Peripheral Channels to provide a peripheral
          generic clock signal (GCLK_PERIPH) to the peripherals.

14.6.2    Basic Operation

14.6.2.1 Initialization
          Before a Generator is enabled, the corresponding clock source should be enabled. The Peripheral clock
          must be configured as outlined by the following steps:




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 154
                                                           SAM D5x/E5x Family Data Sheet
                                                                          GCLK - Generic Clock Controller

          1.   The Generator must be enabled (GENCTRLn.GENEN=1) and the division factor must be set
               (GENTRLn.DIVSEL and GENCTRLn.DIV) by performing a single 32-bit write to the Generator
               Control register (GENCTRLn).
          2.   The Generic Clock for a peripheral must be configured by writing to the respective Peripheral
               Channel Control register (PCHCTRLm). The Generator used as the source for the Peripheral Clock
               must be written to the GEN bit field in the Peripheral Channel Control register (PCHCTRLm.GEN).
         Note: Each Generator n is configured by one dedicated register GENCTRLn.
         Note: Each Peripheral Channel m is configured by one dedicated register PCHCTRLm.
14.6.2.2 Enabling, Disabling, and Resetting
         The GCLK module has no enable/disable bit to enable or disable the whole module.
         The GCLK is reset by setting the Software Reset bit in the Control A register (CTRLA.SWRST) to 1. All
         registers in the GCLK will be reset to their initial state, except for Peripheral Channels and associated
         Generators that have their Write Lock bit set to 1 (PCHCTRLm.WRTLOCK). For further details, refer to
         14.6.3.4 Configuration Lock.
14.6.2.3 Generic Clock Generator
         Each Generator (GCLK_GEN) can be set to run from one of eight different clock sources except
         GCLK_GEN[1], which can be set to run from one of seven sources. GCLK_GEN[1] is the only Generator
         that can be selected as source to others Generators.
         Each generator GCLK_GEN[x] can be connected to one specific pin GCLK_IO[x]. A pin GCLK_IO[x] can
         be set either to act as source to GCLK_GEN[x] or to output the clock signal generated by GCLK_GEN[x].
         The selected source can be divided. Each Generator can be enabled or disabled independently.
         Each GCLK_GEN clock signal can then be used as clock source for Peripheral Channels. Each
         Generator output is allocated to one or several Peripherals.
         GCLK_GEN[0] is used as GCLK_MAIN for the synchronous clock controller inside the Main Clock
         Controller. Refer to the Main Clock Controller description for details on the synchronous clock generation.
         Figure 14-3. Generic Clock Generator




         Related Links
         15. MCLK – Main Clock

14.6.2.4 Enabling a Generator
         A Generator is enabled by writing a '1' to the Generator Enable bit in the Generator Control register
         (GENCTRLn.GENEN=1).




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 155
                                                           SAM D5x/E5x Family Data Sheet
                                                                          GCLK - Generic Clock Controller

14.6.2.5 Disabling a Generator
         A Generator is disabled by writing a '0' to GENCTRLn.GENEN. When GENCTRLn.GENEN=0, the
         GCLK_GEN[n] clock is disabled and gated.
14.6.2.6 Selecting a Clock Source for the Generator
         Each Generator can individually select a clock source by setting the Source Select bit group in the
         Generator Control register (GENCTRLn.SRC).
         Changing from one clock source, for example A, to another clock source, B, can be done on the fly: If
         clock source B is not ready, the Generator will continue using clock source A. As soon as source B is
         ready, the Generator will switch to it. During the switching operation, the Generator maintains clock
         requests to both clock sources A and B, and will release source A as soon as the switch is done. The
         according bit in SYNCBUSY register (SYNCBUSY.GENCTRLn) will remain '1' until the switch operation is
         completed.
         The available clock sources are device dependent (usually the oscillators, RC oscillators, DPLL). Only
         Generator 1 can be used as a common source for all other generators.
14.6.2.7 Changing the Clock Frequency
         The selected source for a Generator can be divided by writing a division value in the Division Factor bit
         field of the Generator Control register (GENCTRLn.DIV). How the actual division factor is calculated is
         depending on the Divide Selection bit (GENCTRLn.DIVSEL).
         If GENCTRLn.DIVSEL=0 and GENCTRLn.DIV is either 0 or 1, the output clock will be undivided.
         Note: The number of available DIV bits may vary from Generator to Generator.
14.6.2.8 Duty Cycle
         When dividing a clock with an odd division factor, the duty-cycle will not be 50/50. Setting the Improve
         Duty Cycle bit of the Generator Control register (GENCTRLn.IDC) will result in a 50/50 duty cycle.
14.6.2.9 External Clock
         The output clock (GCLK_GEN) of each Generator can be sent to I/O pins (GCLK_IO).
         If the Output Enable bit in the Generator Control register is set (GENCTRLn.OE = 1) and the generator is
         enabled (GENCTRLn.GENEN=1), the Generator requests its clock source and the GCLK_GEN clock is
         output to an I/O pin.
         Note: The I/O pin (GCLK/IO[n]) must first be configured as output by writing the corresponding PORT
         registers.
         If GENCTRLn.OE is 0, the according I/O pin is set to an Output Off Value, which is selected by
         GENCTRLn.OOV: If GENCTRLn.OOV is '0', the output clock will be low. If this bit is '1', the output clock
         will be high.
         In Standby mode, if the clock is output (GENCTRLn.OE=1), the clock on the I/O pin is frozen to the OOV
         value if the Run In Standby bit of the Generic Control register (GENCTRLn.RUNSTDBY) is zero. If
         GENCTRLn.RUNSTDBY is '1', the GCLKGEN clock is kept running and output to the I/O pin.
         Related Links
         18.6.3.5 Power Domain Controller




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 156
                                                           SAM D5x/E5x Family Data Sheet
                                                                           GCLK - Generic Clock Controller

14.6.3   Peripheral Clock
         Figure 14-4. Peripheral Clock




14.6.3.1 Enabling a Peripheral Clock
         Before a Peripheral Clock is enabled, one of the Generators must be enabled (GENCTRLn.GENEN) and
         selected as source for the Peripheral Channel by setting the Generator Selection bits in the Peripheral
         Channel Control register (PCHCTRL.GEN). Any available Generator can be selected as clock source for
         each Peripheral Channel.
         When a Generator has been selected, the peripheral clock is enabled by setting the Channel Enable bit in
         the Peripheral Channel Control register, PCHCTRLm.CHEN = 1. The PCHCTRLm.CHEN bit must be
         synchronized to the generic clock domain. PCHCTRLm.CHEN will continue to read as its previous state
         until the synchronization is complete.
14.6.3.2 Disabling a Peripheral Clock
         A Peripheral Clock is disabled by writing PCHCTRLm.CHEN=0. The PCHCTRLm.CHEN bit must be
         synchronized to the Generic Clock domain. PCHCTRLm.CHEN will stay in its previous state until the
         synchronization is complete. The Peripheral Clock is gated when disabled.
         Related Links
         14.8.4 PCHCTRLm

14.6.3.3 Selecting the Clock Source for a Peripheral
         When changing a peripheral clock source by writing to PCHCTRLm.GEN, the peripheral clock must be
         disabled before re-enabling it with the new clock source setting. This prevents glitches during the
         transition:
           1. Disable the Peripheral Channel by writing PCHCTRLm.CHEN=0
           2. Assert that PCHCTRLm.CHEN reads '0'
           3. Change the source of the Peripheral Channel by writing PCHCTRLm.GEN
           4. Re-enable the Peripheral Channel by writing PCHCTRLm.CHEN=1
         Related Links
         14.8.4 PCHCTRLm

14.6.3.4 Configuration Lock
         The peripheral clock configuration can be locked for further write accesses by setting the Write Lock bit in
         the Peripheral Channel Control register PCHCTRLm.WRTLOCK=1). All writing to the PCHCTRLm
         register will be ignored. It can only be unlocked by a Power Reset.
         The Generator source of a locked Peripheral Channel will be locked, too: The corresponding GENCTRLn
         register is locked, and can be unlocked only by a Power Reset.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 157
                                                                SAM D5x/E5x Family Data Sheet
                                                                            GCLK - Generic Clock Controller

         There is one exception concerning the Generator 0. As it is used as GCLK_MAIN, it cannot be locked. It
         is reset by any Reset and will start up in a known configuration. The software reset (CTRLA.SWRST) can
         not unlock the registers.
         In case of an external Reset, the Generator source will be disabled. Even if the WRTLOCK bit is written to
         '1' the peripheral channels are disabled (PCHCTRLm.CHEN set to '0') until the Generator source is
         enabled again. Then, the PCHCTRLm.CHEN are set to '1' again.
         Related Links
         14.8.1 CTRLA

14.6.4   Additional Features

14.6.4.1 Peripheral Clock Enable after Reset
         The Generic Clock Controller must be able to provide a generic clock to some specific peripherals after a
         Reset. That means that the configuration of the Generators and Peripheral Channels after Reset is
         device-dependent.
         Refer to GENCTRLn.SRC for details on GENCTRLn reset.
         Refer to PCHCTRLm.SRC for details on PCHCTRLm reset.

14.6.5   Sleep Mode Operation

14.6.5.1 SleepWalking
         The GCLK module supports the SleepWalking feature.
         If the system is in a sleep mode where the Generic Clocks are stopped, a peripheral that needs its clock
         in order to execute a process must request it from the Generic Clock Controller.
         The Generic Clock Controller receives this request, determines which Generic Clock Generator is
         involved and which clock source needs to be awakened. It then wakes up the respective clock source,
         enables the Generator and Peripheral Channel stages successively, and delivers the clock to the
         peripheral.
         The RUNSTDBY bit in the Generator Control register controls clock output to pin during standby sleep
         mode. If the bit is cleared, the Generator output is not available on pin. When set, the GCLK can
         continuously output the generator output to GCLK_IO. Refer to 14.6.2.9 External Clock for details.
         Related Links
         18. PM – Power Manager

14.6.5.2 Minimize Power Consumption in Standby
         The following table identifies when a Clock Generator is off in Standby Mode, minimizing the power
         consumption:
         Table 14-2. Clock Generator n Activity in Standby Mode
          Request for Clock n present       GENCTRLn.RUNSTDBY     GENCTRLn.OE            Clock Generator n

          yes                               -                     -                      active

          no                                1                     1                      active

          no                                1                     0                      OFF

          no                                0                     1                      OFF

          no                                0                     0                      OFF




         © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 158
                                                          SAM D5x/E5x Family Data Sheet
                                                                          GCLK - Generic Clock Controller

14.6.5.3 Entering Standby Mode
         There may occur a delay when the device is put into Standby, until the power is turned off. This delay is
         caused by running Clock Generators: if the Run in Standby bit in the Generator Control register
         (GENCTRLn.RUNSTDBY) is '0', GCLK must verify that the clock is turned of properly. The duration of this
         verification is frequency-dependent.
         Related Links
         18. PM – Power Manager

14.6.6   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         An exception is the Channel Enable bit in the Peripheral Channel Control registers (PCHCTRLm.CHEN).
         When changing this bit, the bit value must be read-back to ensure the synchronization is complete and to
         assert glitch free internal operation. Note that changing the bit value under ongoing synchronization will
         not generate an error.
         The following registers are synchronized when written:
           • Generic Clock Generator Control register (GENCTRLn)
           • Control A register (CTRLA)
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.
         Related Links
         14.8.1 CTRLA
         14.8.4 PCHCTRLm




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 159
                                                            SAM D5x/E5x Family Data Sheet
                                                                               GCLK - Generic Clock Controller


14.7      Register Summary

 Offset        Name        Bit Pos.

  0x00        CTRLA           7:0                                                                                      SWRST
  0x01
   ...       Reserved
  0x03
                              7:0                          GENCTRL[5:0]                                                SWRST
                             15:8                                                     GENCTRL[11:6]
  0x04      SYNCBUSY
                             23:16
                             31:24
  0x08
   ...       Reserved
  0x1F
                              7:0                                                             SRC[4:0]
                             15:8                      RUNSTDBY    DIVSEL             OE        OOV              IDC   GENEN
  0x20      GENCTRL0
                             23:16                                        DIV[7:0]
                             31:24                                        DIV[15:8]
   ...
                              7:0                                                             SRC[4:0]
                             15:8                      RUNSTDBY    DIVSEL             OE        OOV              IDC   GENEN
 0x4C       GENCTRL11
                             23:16                                        DIV[7:0]
                             31:24                                        DIV[15:8]
  0x50
   ...       Reserved
  0x7F
                              7:0     WRTLOCK   CHEN                                                  GEN[3:0]
                             15:8
  0x80       PCHCTRL0
                             23:16
                             31:24
   ...
                              7:0     WRTLOCK   CHEN                                                  GEN[3:0]
                             15:8
 0x013C     PCHCTRL47
                             23:16
                             31:24




14.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 14.5.8 Register Access Protection.




          © 2019 Microchip Technology Inc.                    Datasheet                                    DS60001507E-page 160
                                                 SAM D5x/E5x Family Data Sheet
                                                                GCLK - Generic Clock Controller

Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
refer to 14.6.6 Synchronization.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 161
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                     GCLK - Generic Clock Controller

14.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection, Write-Synchronized


         Bit         7              6             5             4              3             2             1              0
                                                                                                                       SWRST
   Access                                                                                                               R/W
    Reset                                                                                                                 0


               Bit 0 – SWRST Software Reset
               Writing a zero to this bit has no effect.
               Setting this bit to 1 will reset all registers in the GCLK to their initial state after a Power Reset, except for
               generic clocks and associated Generators that have their WRTLOCK bit in PCHCTRLm set to 1.
               Refer to GENCTRL Reset Value for details on GENCTRL register reset.
               Refer to PCHCTRL Reset Value for details on PCHCTRL register reset.
               Due to synchronization, there is a waiting period between setting CTRLA.SWRST and a completed
               Reset. CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
                Value       Description
                0           There is no Reset operation ongoing.
                1           A Reset operation is ongoing.




           © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 162
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                 GCLK - Generic Clock Controller

14.8.2         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x04
               Reset:      0x00000000
               Property:   –


         Bit        31           30           29             28            27           26       25           24


   Access
    Reset


         Bit        23           22           21             20            19           18       17           16


   Access
    Reset


         Bit        15           14           13             12            11           10        9            8
                                                                            GENCTRL[11:6]
   Access                                     R              R             R            R         R            R
    Reset                                     0                  0         0            0         0            0


         Bit        7             6           5                  4         3            2         1            0
                                                  GENCTRL[5:0]                                              SWRST
   Access           R             R           R              R             R            R                      R
    Reset           0             0           0                  0         0            0                      0


               Bits 13:2 – GENCTRL[11:0] Generator Control n Synchronization Busy
               This bit is cleared when the synchronization of the Generator Control n register (GENCTRLn) between
               clock domains is complete, or when clock switching operation is complete.
               This bit is set when the synchronization of the Generator Control n register (GENCTRLn) between clock
               domains is started.

               Bit 0 – SWRST Software Reset Synchronization Busy
               This bit is cleared when the synchronization of the CTRLA.SWRST register bit between clock domains is
               complete.
               This bit is set when the synchronization of the CTRLA.SWRST register bit between clock domains is
               started.




           © 2019 Microchip Technology Inc.                          Datasheet                    DS60001507E-page 163
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                       GCLK - Generic Clock Controller

14.8.3         Generator Control

               Name:       GENCTRLn
               Offset:     0x20 + n*0x04 [n=0..11]
               Reset:      0x00000106
               Property:   PAC Write-Protection, Write-Synchronized

               GENCTRLn controls the settings of Generic Generator n (n=[11:0]). The reset value is 0x00000106 for
               Generator n=0, else 0x00000000

         Bit        31            30             29             28               27           26         25           24
                                                                     DIV[15:8]
   Access          R/W            R/W           R/W            R/W               R/W          R/W       R/W          R/W
    Reset           0              0             0              0                 0            0          0           0


         Bit        23            22             21             20               19           18         17           16
                                                                      DIV[7:0]
   Access          R/W            R/W           R/W            R/W               R/W          R/W       R/W          R/W
    Reset           0              0             0              0                 0            0          0           0


         Bit        15            14             13             12               11           10          9           8
                                              RUNSTDBY       DIVSEL              OE          OOV         IDC        GENEN
   Access
    Reset                                        0              0                 0            0          0           1


         Bit        7              6             5              4                 3            2          1           0
                                                                                            SRC[4:0]
   Access                                                      R/W               R/W          R/W       R/W          R/W
    Reset                                                       0                 0            0          0           0


               Bits 31:16 – DIV[15:0] Division Factor
               These bits represent a division value for the corresponding Generator. The actual division factor is
               dependent on the state of DIVSEL. The number of relevant DIV bits for each Generator can be seen in
               this table. Written bits outside of the specified range will be ignored.
               Table 14-3. Division Factor Bits

               Generic Clock Generator                Division Factor Bits                    Maximum Division Factor
               Generator 0                            8 division factor bits - DIV[7:0]       512
               Generator 1                            16 division factor bits - DIV[15:0]     131072
               Generator 2 - 11                       8 division factor bits - DIV[7:0]       512

               Bit 13 – RUNSTDBY Run in Standby
               This bit is used to keep the Generator running in Standby as long as it is configured to output to a
               dedicated GCLK_IO pin. If GENCTRLn.OE is zero, this bit has no effect and the generator will only be
               running if a peripheral requires the clock.
                Value       Description
                0            The Generator is stopped in Standby and the GCLK_IO pin state (one or zero) will be
                             dependent on the setting in GENCTRL.OOV.




           © 2019 Microchip Technology Inc.                            Datasheet                          DS60001507E-page 164
                                                   SAM D5x/E5x Family Data Sheet
                                                                  GCLK - Generic Clock Controller

 Value        Description
 1            The Generator is kept running and output to its dedicated GCLK_IO pin during Standby
              mode.

Bit 12 – DIVSEL Divide Selection
This bit determines how the division factor of the clock source of the Generator will be calculated from
DIV. If the clock source should not be divided, DIVSEL must be 0 and the GENCTRLn.DIV value must be
either 0 or 1.
 Value        Description
 0            The Generator clock frequency equals the clock source frequency divided by
              GENCTRLn.DIV.
 1            The Generator clock frequency equals the clock source frequency divided by 2^(N+1), where
              N is the Division Factor Bits for the selected generator (refer to GENCTRLn.DIV).

Bit 11 – OE Output Enable
This bit is used to output the Generator clock output to the corresponding pin (GCLK_IO), as long as
GCLK_IO is not defined as the Generator source in the GENCTRLn.SRC bit field.
 Value       Description
 0            No Generator clock signal on pin GCLK_IO.
 1            The Generator clock signal is output on the corresponding GCLK_IO, unless GCLK_IO is
              selected as a generator source in the GENCTRLn.SRC bit field.

Bit 10 – OOV Output Off Value
This bit is used to control the clock output value on pin (GCLK_IO) when the Generator is turned off or the
OE bit is zero, as long as GCLK_IO is not defined as the Generator source in the GENCTRLn.SRC bit
field.
 Value       Description
 0            The GCLK_IO will be LOW when generator is turned off or when the OE bit is zero.
 1            The GCLK_IO will be HIGH when generator is turned off or when the OE bit is zero.

Bit 9 – IDC Improve Duty Cycle
This bit is used to improve the duty cycle of the Generator output to 50/50 for odd division factors.
 Value       Description
 0            Generator output clock duty cycle is not balanced to 50/50 for odd division factors.
 1            Generator output clock duty cycle is 50/50.

Bit 8 – GENEN Generator Enable
This bit is used to enable and disable the Generator.
 Value       Description
 0            Generator is disabled.
 1            Generator is enabled.

Bits 4:0 – SRC[4:0] Generator Clock Source Selection
These bits select the Generator clock source, as shown in this table.
Table 14-4. Generator Clock Source Selection

 Value                    Name                   Description
 0x00                     XOSC0                  XOSC 0 oscillator output




© 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 165
                                                    SAM D5x/E5x Family Data Sheet
                                                                   GCLK - Generic Clock Controller

...........continued
 Value                    Name                    Description
 0x01                     XOSC1                   XOSC 1 oscillator output
 0x02                     GCLK_IN                 Generator input pad (GCLK_IO)
 0x03                     GCLK_GEN1               Generic clock generator 1 output
 0x04                     OSCULP32K               OSCULP32K oscillator output
 0x05                     XOSC32K                 XOSC32K oscillator output
 0x06                     DFLL                    DFLL oscillator output
 0x07                     DPLL0                   DPLL0 output
 0x08                     DPLL1                   DPLL1 output
 0x09-0x1F                Reserved                Reserved for future use

A Power Reset will reset all GENCTRLn registers. the Reset values of the GENCTRLn registers are
shown in table below.
Table 14-5. GENCTRLn Reset Value after a Power Reset

 GCLK Generator                          Reset Value after a Power Reset
 0                                       0x00000106
 others                                  0x00000000

A User Reset will reset the associated GENCTRL register unless the Generator is the source of a locked
Peripheral Channel (PCHCTRLm.WRTLOCK=1). The reset values of the GENCTRL register are as
shown in the table below.
Table 14-6. GENCTRLn Reset Value after a User Reset

 GCLK Generator Reset Value after a User Reset
 0                      0x00000106
 others                 No change if the generator is used by a Peripheral Channel m with
                        PCHCTRLm.WRTLOCK=1
                        else 0x00000000

Related Links
14.8.4 PCHCTRLm




© 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 166
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                   GCLK - Generic Clock Controller

14.8.4         Peripheral Channel Control

               Name:        PCHCTRLm
               Offset:      0x80 + m*0x04 [m=0..47]
               Reset:       0x00000000
               Property:    PAC Write-Protection

               PCHTRLm controls the settings of Peripheral Channel number m (m=[47:0]).

         Bit        31            30            29            28            27            26               25           24


   Access
    Reset


         Bit        23            22            21            20            19            18               17           16


   Access
    Reset


         Bit        15            14            13            12             11           10                9           8


   Access
    Reset


         Bit         7             6             5             4             3             2                1           0
                 WRTLOCK         CHEN                                                           GEN[3:0]
   Access           R/W           R/W                                       R/W           R/W              R/W         R/W
    Reset            0             0                                         0             0                0           0


               Bit 7 – WRTLOCK Write Lock
               After this bit is set to '1', further writes to the PCHCTRLm register will be discarded. The control register of
               the corresponding Generator n (GENCTRLn), as assigned in PCHCTRLm.GEN, will also be locked. It can
               only be unlocked by a Power Reset.
               Note that Generator 0 cannot be locked.
                Value        Description
                0            The Peripheral Channel register and the associated Generator register are not locked
                1            The Peripheral Channel register and the associated Generator register are locked

               Bit 6 – CHEN Channel Enable
               This bit is used to enable and disable a Peripheral Channel.
                Value       Description
                0            The Peripheral Channel is disabled
                1            The Peripheral Channel is enabled

               Bits 3:0 – GEN[3:0] Generator Selection
               This bit field selects the Generator to be used as the source of a peripheral clock, as shown in the table
               below:




           © 2019 Microchip Technology Inc.                          Datasheet                              DS60001507E-page 167
                                                SAM D5x/E5x Family Data Sheet
                                                                 GCLK - Generic Clock Controller

Table 14-7. Generator Selection

 Value                                                 Description
 0x0                                                   Generic Clock Generator 0
 0x1                                                   Generic Clock Generator 1
 0x2                                                   Generic Clock Generator 2
 0x3                                                   Generic Clock Generator 3
 0x4                                                   Generic Clock Generator 4
 0x5                                                   Generic Clock Generator 5
 0x6                                                   Generic Clock Generator 6
 0x7                                                   Generic Clock Generator 7
 0x8                                                   Generic Clock Generator 8
 0x9                                                   Generic Clock Generator 9
 0xA                                                   Generic Clock Generator 10
 0xB                                                   Generic Clock Generator 11

Table 14-8. Reset Value after a User Reset or a Power Reset

 Reset             PCHCTRLm.GEN                PCHCTRLm.CHEN                   PCHCTRLm.WRTLOCK
 Power Reset 0x0                               0x0                             0x0
 User Reset        If WRTLOCK = 0              If WRTLOCK = 0                  No change
                   : 0x0                       : 0x0
                   If WRTLOCK = 1: no change   If WRTLOCK = 1: no change

A Power Reset will reset all the PCHCTRLm registers.
A User Reset will reset a PCHCTRL if WRTLOCK=0, or else, the content of that PCHCTRL remains
unchanged.
The PCHCTRL register Reset values are shown in the table below, PCHCTRLm Mapping.
Table 14-9. PCHCTRLm Mapping

 index(m)       Name                                   Description
 0              GCLK_OSCCTRL_DFLL48                    DFLL48 input clock source
 1              GCLK_OSCCTRL_FDPLL0                    Reference clock for FDPLL0
 2              GCLK_OSCCTRL_FDPLL1                    Reference clock for FDPLL1
 3              GCLK_OSCCTRL_FDPLL0_32K                FDPLL0 32KHz clock for internal lock timer
                GCLK_OSCCTRL_FDPLL1_32K                FDPLL1 32KHz clock for internal lock timer
                GCLK_SDHC0_SLOW                        SDHC0 Slow
                GCLK_SDHC1_SLOW                        SDHC1 Slow
                GCLK_SERCOM[0..7]_SLOW                 SERCOM[0..7] Slow
 4              GCLK_EIC                               EIC




© 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 168
                                       SAM D5x/E5x Family Data Sheet
                                                    GCLK - Generic Clock Controller

...........continued
 index(m)       Name                     Description
 5              GCLK_FREQM_MSR           FREQM Measure
 6              GCLK_FREQM_REF           FREQM Reference
 7              GCLK_SERCOM0_CORE        SERCOM0 Core
 8              GCLK_SERCOM1_CORE        SERCOM1 Core
 9              GCLK_TC0, GCLK_TC1       TC0, TC1
 10             GCLK_USB                 USB
 22:11          GCLK_EVSYS[0..11]        EVSYS[0..11]
 23             GCLK_SERCOM2_CORE        SERCOM2 Core
 24             GCLK_SERCOM3_CORE        SERCOM3 Core
 25             GCLK_TCC0, GCLK_TCC1     TCC0, TCC1
 26             GCLK_TC2, GCLK_TC3       TC2, TC3
 27             GCLK_CAN0                CAN0
 28             GCLK_CAN1                CAN1
 29             GCLK_TCC2, GCLK_TCC3     TCC2, TCC3
 30             GCLK_TC4, GCLK_TC5       TC4, TC5
 31             GCLK_PDEC                PDEC
 32             GCLK_AC                  AC
 33             GCLK_CCL                 CCL
 34             GCLK_SERCOM4_CORE        SERCOM4 Core
 35             GCLK_SERCOM5_CORE        SERCOM5 Core
 36             GCLK_SERCOM6_CORE        SERCOM6 Core
 37             GCLK_SERCOM7_CORE        SERCOM7 Core
 38             GCLK_TCC4                TCC4
 39             GCLK_TC6, GCLK_TC7       TC6, TC7
 40             GCLK_ADC0                ADC0
 41             GCLK_ADC1                ADC1
 42             GCLK_DAC                 DAC
 44:43          GCLK_I2S                 I2S
 45             GCLK_SDHC0               SDHC0
 46             GCLK_SDHC1               SDHC1
 47             GCLK_CM4_TRACE           CM4 Trace




© 2019 Microchip Technology Inc.       Datasheet                   DS60001507E-page 169
