# 30. FREQM – Frequency Meter

*Source: `Atmel-SAMD51.pdf`, pages 831-845 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                FREQM – Frequency Meter


30.    FREQM – Frequency Meter

30.1   Overview
       The Frequency Meter (FREQM) can be used to accurately measure the frequency of a clock by
       comparing it to a known reference clock.



30.2   Features
         •   Ratio can be measured with 24-bit accuracy
         •   Accurately measures the frequency of an input clock with respect to a reference clock
         •   Reference clock can be selected from the available GCLK_FREQM_REF sources
         •   Measured clock can be selected from the available GCLK_FREQM_MSR sources



30.3   Block Diagram
       Figure 30-1. FREQM Block Diagram




                                                    CLK_MSR
                    GCLK_FREQM_MSR                                  COUNTER                   VALUE
                                              EN



                                                                START




                                                    CLK_REF                                   DONE
                    GCLK_FREQM_REF                                    TIMER
                                              EN




                                            ENABLE                   REFNUM                  INTFLAG




30.4   Signal Description
       Not applicable.



30.5   Product Dependencies
       In order to use this peripheral, other parts of the system must be configured correctly, as described below.




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 831
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  FREQM – Frequency Meter

30.5.1   I/O Lines
         The GCLK I/O lines (GCLK_IO[7:0]) can be used as measurement or reference clock sources. This
         requires the I/O pins to be configured.

30.5.2   Power Management
         The FREQM will continue to operate in idle sleep mode where the selected source clock is running. The
         FREQM’s interrupts can be used to wake up the device from idle sleep mode. Refer to the Power
         Manager chapter for details on the different sleep modes.
         Related Links
         18. PM – Power Manager

30.5.3   Clocks
         The clock for the FREQM bus interface (CLK_APB_FREQM) is enabled and disabled by the Main Clock
         Controller, the default state of CLK_APB_FREQM can be found in Peripheral Clock Masking.
         Two generic clocks are used by the FREQM: Reference Clock (GCLK_FREQM_REF) and Measurement
         Clock (GCLK_FREQM_MSR).
         GCLK_FREQM_REF is required to clock the internal reference timer, which acts as the frequency
         reference.
         GCLK_FREQM_MSR is required to clock a ripple counter for frequency measurement. These clocks
         must be configured and enabled in the generic clock controller before using the FREQM.
         Related Links
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller

30.5.4   DMA
         Not applicable.

30.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using FREQM interrupt requires the
         interrupt controller to be configured first.
         Related Links
         10.2.2 Interrupt Line Mapping

30.5.6   Events
         Not applicable

30.5.7   Debug Operation
         When the CPU is halted in debug mode the FREQM continues its normal operation. The FREQM cannot
         be halted when the CPU is halted in debug mode. If the FREQM is configured in a way that requires it to
         be periodically serviced by the CPU, improper operation or data loss may result during debugging.

30.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except the following registers:




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 832
                                                            SAM D5x/E5x Family Data Sheet
                                                                                  FREQM – Frequency Meter

           • Control B register (CTRLB)
           • Interrupt Flag Status and Clear register (INTFLAG)
           • Status register (STATUS)
          Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
          Protection" property in each individual register description.
          Write-protection does not apply to accesses through an external debugger.
          Related Links
          27. PAC - Peripheral Access Controller



30.6      Functional Description

30.6.1    Principle of Operation
          FREQM counts the number of periods of the measured clock (GCLK_FREQM_MSR) with respect to the
          reference clock (GCLK_FREQM_REF). The measurement is done for a period of REFNUM/fCLK_REF and
          stored in the Value register (VALUE.VALUE). REFNUM is the number of Reference clock cycles selected
          in the Configuration A register (CFGA.REFNUM).
          The frequency of the measured clock, �CLK_MSR, is calculated by

                           VALUE
          �CLK_MSR =             �
                          REFNUM CLK_REF

30.6.2    Basic Operation

30.6.2.1 Initialization
          Before enabling FREQM, the device and peripheral must be configured:
           • Each of the generic clocks (GCLK_FREQM_REF and GCLK_FREQM_MSR) must be configured and
              enabled.
           •
                             Important: The reference clock must be slower than the measurement clock.




           • Write the number of Reference clock cycles for which the measurement is to be done in the
             Configuration A register (CFGA.REFNUM). This must be a non-zero number.
          The following register is enable-protected, meaning that it can only be written when the FREQM is
          disabled (CTRLA.ENABLE=0):
           • Configuration A register (CFGA)
          Enable-protection is denoted by the "Enable-Protected" property in the register description.
          Related Links
          14. GCLK - Generic Clock Controller

30.6.2.2 Enabling, Disabling and Resetting
          The FREQM is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The
          peripheral is disabled by writing CTRLA.ENABLE=0.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 833
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  FREQM – Frequency Meter

         The FREQM is reset by writing a '1' to the Software Reset bit in the Control A register (CTRLA.SWRST).
         On software reset, all registers in the FREQM will be reset to their initial state, and the FREQM will be
         disabled.
         Then ENABLE and SWRST bits are write-synchronized.
         Related Links
         30.6.7 Synchronization

30.6.2.3 Measurement
         In the Configuration A register, the Number of Reference Clock Cycles field (CFGA.REFNUM) selects the
         duration of the measurement. The measurement is given in number of GCLK_FREQM_REF periods.
         Note: The REFNUM field must be written before the FREQM is enabled.
         After the FREQM is enabled, writing a '1' to the START bit in the Control B register (CTRLB.START)
         starts the measurement. The BUSY bit in Status register (STATUS.BUSY) is set when the measurement
         starts, and cleared when the measurement is complete.
         There is also an interrupt request for Measurement Done: When the Measurement Done bit in Interrupt
         Enable Set register (INTENSET.DONE) is '1' and a measurement is finished, the Measurement Done bit
         in the Interrupt Flag Status and Clear register (INTFLAG.DONE) will be set and an interrupt request is
         generated.
         The result of the measurement can be read from the Value register (VALUE.VALUE). The frequency of
         the measured clock GCLK_FREQM_MSR is then:
                         VALUE
         �CLK_MSR =            �
                        REFNUM CLK_REF
         Note: In order to make sure the measurement result (VALUE.VALUE[23:0]) is valid, the overflow status
         (STATUS.OVF) should be checked.
         In case an overflow condition occurred, indicated by the Overflow bit in the STATUS register
         (STATUS.OVF), either the number of reference clock cycles must be reduced (CFGA.REFNUM), or a
         faster reference clock must be configured. Once the configuration is adjusted, clear the overflow status by
         writing a '1' to STATUS.OVF. Then another measurement can be started by writing a '1' to CTRLB.START.

30.6.3   DMA Operation
         Not applicable.

30.6.4   Interrupts
         The FREQM has one interrupt source:
           • DONE: A frequency measurement is done.
         The interrupt flag in the Interrupt Flag Status and Clear (30.8.6 INTFLAG) register is set when the
         interrupt condition occurs. The interrupt can be enabled by writing a '1' to the corresponding bit in the
         Interrupt Enable Set (30.8.5 INTENSET) register, and disabled by writing a '1' to the corresponding bit in
         the Interrupt Enable Clear (30.8.4 INTENCLR) register.
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or the
         FREQM is reset. See 30.8.6 INTFLAG for details on how to clear interrupt flags. All interrupt requests
         from the peripheral are ORed together on system level to generate one combined interrupt request to the
         NVIC. The user must read the 30.8.6 INTFLAG register to determine which interrupt condition is present.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 834
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  FREQM – Frequency Meter

         This interrupt is a synchronous wake-up source.
         Note that interrupts must be globally enabled for interrupt requests to be generated.

30.6.5   Events
         Not applicable.

30.6.6   Sleep Mode Operation
         The FREQM will continue to operate in idle sleep mode where the selected source clock is running. The
         FREQM’s interrupts can be used to wake up the device from idle sleep mode.
         For lowest chip power consumption in sleep modes, FREQM should be disabled before entering a sleep
         mode.
         Related Links
         18. PM – Power Manager

30.6.7   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits and registers are write-synchronized:
           • Software Reset bit in Control A register (CTRLA.SWRST)
           • Enable bit in Control A register (CTRLA.ENABLE)
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.
         Related Links
         13.3 Register Synchronization




         © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 835
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      FREQM – Frequency Meter


30.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                                                                    ENABLE     SWRST
 0x01         CTRLB           7:0                                                                               START
                              7:0                                      REFNUM[7:0]
 0x02          CFGA
                             15:8
 0x04
   ...       Reserved
 0x07
 0x08        INTENCLR         7:0                                                                               DONE
 0x09        INTENSET         7:0                                                                               DONE
 0x0A        INTFLAG          7:0                                                                               DONE
 0x0B         STATUS          7:0                                                                     OVF        BUSY
                              7:0                                                                    ENABLE     SWRST
                             15:8
 0x0C       SYNCBUSY
                             23:16
                             31:24
                              7:0                                       VALUE[7:0]
                             15:8                                       VALUE[15:8]
 0x10         VALUE
                             23:16                                     VALUE[23:16]
                             31:24




30.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
          the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers require synchronization when read and/or written. Synchronization is denoted by the
          "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
          Some registers are enable-protected, meaning they can only be written when the module is disabled.
          Enable protection is denoted by the "Enable-Protected" property in each individual register description.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.




          © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 836
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                          FREQM – Frequency Meter

30.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7             6            5             4             3             2             1            0
                                                                                                    ENABLE         SWRST
   Access                                                                                             R/W           R/W
    Reset                                                                                               0            0


               Bit 1 – ENABLE Enable
               Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
               disabled. The value written to CTRLA.ENABLE will read back immediately and the ENABLE bit in the
               Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be cleared
               when the operation is complete.
               This bit is not enable-protected.
                Value       Description
                0           The peripheral is disabled.
                1           The peripheral is enabled.

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit resets all registers in the FREQM to their initial state, and the FREQM will be
               disabled. Writing a '1' to this bit will always take precedence, meaning that all other writes in the same
               write-operation will be discarded.
               Due to synchronization there is a delay from writing CTRLA.SWRST until the Reset is complete.
               CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the Reset is complete.
               This bit is not enable-protected.
                Value        Description
                0            There is no ongoing Reset operation.
                1            The Reset operation is ongoing.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 837
                                                                SAM D5x/E5x Family Data Sheet
                                                                            FREQM – Frequency Meter

30.8.2         Control B

               Name:       CTRLB
               Offset:     0x01
               Reset:      0x00
               Property:   –


         Bit        7             6           5            4          3     2       1            0
                                                                                               START
   Access                                                                                        W
    Reset                                                                                        0


               Bit 0 – START Start Measurement
               Value      Description
               0          Writing a '0' has no effect.
               1          Writing a '1' starts a measurement.




           © 2019 Microchip Technology Inc.                     Datasheet            DS60001507E-page 838
                                                                SAM D5x/E5x Family Data Sheet
                                                                                 FREQM – Frequency Meter

30.8.3         Configuration A

               Name:       CFGA
               Offset:     0x02
               Reset:      0x0000
               Property:   PAC Write-Protection, Enable-protected


         Bit        15           14           13          12                11   10          9           8


   Access
    Reset


         Bit        7             6            5          4                 3     2          1           0
                                                              REFNUM[7:0]
   Access          R/W           R/W          R/W        R/W            R/W      R/W        R/W         R/W
    Reset           0             0            0          0                 0     0          0           0


               Bits 7:0 – REFNUM[7:0] Number of Reference Clock Cycles
               Selects the duration of a measurement in number of CLK_FREQM_REF cycles. This must be a non-zero
               value, i.e. 0x01 (one cycle) to 0xFF (255 cycles).




           © 2019 Microchip Technology Inc.                      Datasheet                   DS60001507E-page 839
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                         FREQM – Frequency Meter

30.8.4         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x08
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7             6            5             4             3            2             1             0
                                                                                                                    DONE
   Access                                                                                                           R/W
    Reset                                                                                                            0


               Bit 0 – DONE Measurement Done Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Measurement Done Interrupt Enable bit, which disables the
               Measurement Done interrupt.
               Value         Description
               0             The Measurement Done interrupt is disabled.
               1             The Measurement Done interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 840
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                         FREQM – Frequency Meter

30.8.5         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x09
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7            6             5             4            3             2             1           0
                                                                                                                 DONE
   Access                                                                                                         R/W
    Reset                                                                                                          0


               Bit 0 – DONE Measurement Done Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Measurement Done Interrupt Enable bit, which enables the
               Measurement Done interrupt.
               Value         Description
               0             The Measurement Done interrupt is disabled.
               1             The Measurement Done interrupt is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 841
                                                                SAM D5x/E5x Family Data Sheet
                                                                                     FREQM – Frequency Meter

30.8.6         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x0A
               Reset:      0x00
               Property:   –


         Bit         7            6            5            4            3               2   1            0
                                                                                                        DONE
   Access                                                                                                R/W
    Reset                                                                                                 0


               Bit 0 – DONE Mesurement Done
               This flag is cleared by writing a '1' to it.
               This flag is set when the STATUS.BUSY bit has a one-to-zero transition.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the DONE interrupt flag.




           © 2019 Microchip Technology Inc.                      Datasheet                    DS60001507E-page 842
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                         FREQM – Frequency Meter

30.8.7         Status

               Name:       STATUS
               Offset:     0x0B
               Reset:      0x00
               Property:   –


         Bit         7            6             5            4             3             2        1           0
                                                                                                 OVF        BUSY
   Access                                                                                        R/W          R
    Reset                                                                                         0           0


               Bit 1 – OVF Sticky Count Value Overflow
               This bit is cleared by writing a '1' to it.
               This bit is set when an overflow condition occurs to the value counter.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the OVF status.

               Bit 0 – BUSY FREQM Status
               Value      Description
               0          No ongoing frequency measurement.
               1          Frequency measurement is ongoing.




           © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 843
                                                               SAM D5x/E5x Family Data Sheet
                                                                                   FREQM – Frequency Meter

30.8.8         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x0C
               Reset:      0x00000000
               Property:   –


         Bit        31           30           29          28          27           26        25          24


   Access
    Reset


         Bit        23           22           21          20          19           18        17          16


   Access
    Reset


         Bit        15           14           13          12          11           10        9           8


   Access
    Reset


         Bit        7             6           5           4            3           2         1           0
                                                                                           ENABLE      SWRST
   Access                                                                                    R           R
    Reset                                                                                    0           0


               Bit 1 – ENABLE Enable
               This bit is cleared when the synchronization of CTRLA.ENABLE is complete.
               This bit is set when the synchronization of CTRLA.ENABLE is started.

               Bit 0 – SWRST Synchronization Busy
               This bit is cleared when the synchronization of CTRLA.SWRST is complete.
               This bit is set when the synchronization of CTRLA.SWRST is started.




           © 2019 Microchip Technology Inc.                    Datasheet                     DS60001507E-page 844
                                                             SAM D5x/E5x Family Data Sheet
                                                                               FREQM – Frequency Meter

30.8.9         Value

               Name:       VALUE
               Offset:     0x10
               Reset:      0x00000000
               Property:   –


         Bit        31           30           29      28                 27    26      25           24


   Access
    Reset


         Bit        23           22           21      20                 19    18      17           16
                                                           VALUE[23:16]
   Access              R          R           R        R                  R    R       R            R
    Reset              0          0           0        0                  0    0       0            0


         Bit        15           14           13      12                  11   10      9            8
                                                           VALUE[15:8]
   Access              R          R           R        R                  R    R       R            R
    Reset              0          0           0        0                  0    0       0            0


         Bit           7          6           5        4                  3    2       1            0
                                                            VALUE[7:0]
   Access              R          R           R        R                  R    R       R            R
    Reset              0          0           0        0                  0    0       0            0


               Bits 23:0 – VALUE[23:0] Measurement Value
               Result from measurement.




           © 2019 Microchip Technology Inc.                    Datasheet                DS60001507E-page 845
