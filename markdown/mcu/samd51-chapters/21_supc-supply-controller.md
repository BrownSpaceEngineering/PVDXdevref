# 19. SUPC – Supply Controller

*Source: `Atmel-SAMD51.pdf`, pages 235-264 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                 SUPC – Supply Controller


19.    SUPC – Supply Controller

19.1   Overview
       The Supply Controller (SUPC) manages the voltage reference, power supply and supply monitoring of
       the device. It is also able to control two output pins.
       The SUPC controls the voltage regulators for the core (VDDCORE) and backup (VDDBU) domains. It
       sets the voltage regulators according to the sleep modes, or the user configuration. In active mode, the
       voltage regulators can be selected on the fly between LDO (low-dropout) type regulator or Buck
       converter.
       The SUPC supports connection of a battery backup to the VBAT power pin. It includes functionality that
       enables automatic power switching between main power and battery backup power. This ensures power
       to the backup domain when the main battery or power source is unavailable.
       The SUPC embeds two Brown-Out Detectors. BOD33 monitors the voltage applied to the device (VDD or
       VBAT) and BOD12 monitors the internal voltage to the core (VDDCORE). The BOD33 can monitor the
       supply voltage continuously (continuous mode) or periodically (sampling mode), in normal or low power
       mode.
       The SUPC generates also a selectable reference voltage and a voltage dependent on the temperature
       which can be used by analog modules like the ADC.



19.2   Features
         • Voltage Regulator System
             – Main voltage regulator: LDO or Buck Converter in Active, Standby or Hibernate mode
                (MAINVREG)
             – Low-Power voltage regulator in Backup mode (LPVREG)
             – Controlled VDDCORE voltage slope when changing VDDCORE
         • Battery Backup Power Switch
             – Automatic switching from main power to battery backup power
                 • Automatic entry to backup mode when switched to battery backup power
             – Automatic switching from battery backup power to main power
                 • Automatic exit from backup mode when switched back to main power
                 • Stay in backup mode when switched back to main power
         • Voltage Reference System
             – Reference voltage for ADC and DAC
             – Temperature sensor
         • 3.3V Brown-Out Detector (BOD33)
             – Programmable threshold
             – Threshold value loaded from NVM User Row at startup
             – Triggers resets, interrupts, or Battery Backup Power Switch. Action loaded from NVM User Row
             – Operating modes:
                 • Continuous mode




       © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 235
                                                                                SAM D5x/E5x Family Data Sheet
                                                                                                              SUPC – Supply Controller

                 • Low power and sampled mode for low power applications with programmable sample
                    frequency
             – Hysteresis value from Flash User Calibration
             – Monitor VDD or VBAT
         • 1.2V Brown-Out Detector (BOD12)
         • Output pins
             – Pin toggling on RTC event



19.3   Block Diagram
       Figure 19-1. SUPC Block Diagram
                 VDD       VBAT
                                                    Wakeup from RTC

                                                                                                OUT[1:0]

                                                             BKOUT
                                Battery Backup
                                 Power Switch




                                           Backup Regulator
                                              (LPVREG)


                       BOD33              BOD33

                                                                         BOD12                BOD12
                                             MAINVREG

                                                   LDO
                                                                                              VDDCORE
                         VREG
                                                   Buck
                                                 Converter
                  sleep mode
            PM                                                                                 Core
                                                                                               domain




                                                                          temperature sensor
                                                  VREF
                          VREF                                            reference voltage




19.4   Signal Description
        Signal Name                                            Type                                        Description
        OUT[1:0]                                               Digital Output                              SUPC Outputs

       One signal can be mapped on several pins.
       Related Links
       6. I/O Multiplexing and Considerations



19.5   Product Dependencies
       In order to use this peripheral, other parts of the system must be configured correctly, as described below.




       © 2019 Microchip Technology Inc.                                          Datasheet                                DS60001507E-page 236
                                                             SAM D5x/E5x Family Data Sheet
                                                                                    SUPC – Supply Controller

19.5.1   I/O Lines
         I/O lines are configured by SUPC when the SUPC output (signal OUT) is enabled. The I/O lines need no
         user configuration.

19.5.2   Power Management
         The SUPC can operate in all sleep modes except backup sleep mode. BOD33 and Battery backup Power
         Switch can operate in backup mode.
         Related Links
         18. PM – Power Manager

19.5.3   Clocks
         The SUPC bus clock (CLK_SUPC_APB) can be enabled and disabled in the Main Clock module.
         A 32KHz clock, asynchronous to the user interface clock (CLK_SUPC_APB), is required to run BOD33
         and in sampled mode. Due to this asynchronicity, writing to certain registers will require synchronization
         between the clock domains. Refer to 19.6.7 Synchronization for further details.
         Related Links
         29. OSC32KCTRL – 32KHz Oscillators Controller
         15.6.2.6 Peripheral Clock Masking

19.5.4   DMA
         Not applicable.

19.5.5   Interrupts
         The interrupt request lines are connected to the interrupt controller. Using the SUPC interrupts requires
         the interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

19.5.6   Events
         Not applicable.

19.5.7   Debug Operation
         When the CPU is halted in debug mode, the SUPC continues normal operation. If the SUPC is configured
         in a way that requires it to be periodically serviced by the CPU through interrupts or similar, improper
         operation or data loss may result during debugging.
         If a cold plug-in is detected by the system, BOD33 and BOD12 will use the factory calibration setting
         instead of the user calibration. In hot plug-in, the BODs resets keep running.

19.5.8   Register Access Protection
         Registers with write access can be write-protected optionally by the Peripheral Access Controller (PAC).
         Note: Not all registers with write access can be write-protected.
         PAC write protection is not available for the following registers:
           • Interrupt Flag Status and Clear register (INTFLAG)
         Optional PAC write protection is denoted by the "PAC Write-Protection" property in each individual
         register description.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 237
                                                          SAM D5x/E5x Family Data Sheet
                                                                                  SUPC – Supply Controller

          Related Links
          27. PAC - Peripheral Access Controller

19.5.9    Analog Connections
          Not applicable.



19.6      Functional Description

19.6.1    Voltage Regulator System Operation

19.6.1.1 Enabling, Disabling, and Resetting
          The LDO main voltage regulator is enabled after a power-reset. The main voltage regulator output supply
          level is automatically defined by the sleep mode selected in the Power Manager module.
19.6.1.2 Initialization
          After a power-reset, the LDO voltage regulator supplying VDDCORE is enabled.
19.6.1.3 Selecting a Voltage Regulator
          In Active mode, the type of the main voltage regulator supplying VDDCORE can be switched on the fly.
          The two alternatives are a LDO regulator and a Buck converter.
          The main voltage regulator switching sequences are as follows:
           • The user changes the value of the Voltage Regulator Selection bit in the Voltage Regulator System
             Control register (VREG.SEL)
           • The start of the switching sequence is indicated by clearing the Voltage Regulator Ready bit in the
             STATUS register (STATUS.VREGRDY=0)
           • Once the switching sequence is completed, STATUS.VREGRDY will read '1'
          The Voltage Regulator Ready (VREGRDY) interrupt can also be used to detect a zero-to-one transition of
          the STATUS.VREGRDY bit.
19.6.1.4 Voltage Scaling Control
          The VDDCORE supply will change under certain circumstances:
           • When a Sleep mode (Standby, Hibernate, Backup) is entered or exited
           • When a sleepwalking task is requested in Standby Sleep mode
          To prevent high peak current on the main power supply and to have a smooth transition of VDDCORE,
          the Voltage Scaling Period field in VREG (VREG.VSPER) can be controlled: VDDCORE is changed by a
          typical 5 mV of the selected voltage scaling period (2VSPER) * T until the target voltage is reached.
          The smooth transition of VDDCORE is enabled/disabled by setting/clearing the Voltage Scaling Enable
          bit in VREG (VREG.VSEN).
          The following waveform shows an example of exiting the Standby Sleep mode.




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 238
                                                          SAM D5x/E5x Family Data Sheet
                                                                                  SUPC – Supply Controller




          The STATUS.VCORERDY bit is set to '1' as soon as the VDDCORE voltage has reached the target
          voltage. During voltage transition, STATUS.VCORERDY will read '0'. The Voltage Ready interrupt
          (VCORERDY) can be used to detect a 0-to-1 transition of STATUS.VCORERDY, see also 19.5.5
          Interrupts.
          When entering the Standby, Hibernate, or Backup Sleep mode, and when no sleepwalking task is
          requested, the VDDCORE Voltage scaling control is not used.
19.6.1.5 Sleep Mode Operation
          In Standby and Hibernate mode, the main voltage regulator (MAINVREG) operates in low power mode.
          In backup mode, the low-power voltage regulator (LPVREG) is used to supply VDDCORE.

19.6.2    Voltage Reference System Operation
          The reference voltages are generated by a functional block DETREF inside of the SUPC. DETREF is
          providing a fixed-voltage source, BANDGAP=1.1V, and a variable voltage, VREF.
19.6.2.1 Initialization
          The voltage reference output and the temperature sensor are disabled after any Reset.
19.6.2.2 Enabling, Disabling, and Resetting
          The voltage reference output is enabled/disabled by setting/clearing the Voltage Reference Output
          Enable bit in the Voltage Reference register (VREF.VREFOE).
          The temperature sensor is enabled/disabled by setting/clearing the Temperature Sensor Enable bit in the
          Voltage Reference register (VREF.TSEN).
          Note: When VREF.ONDEMAND=0, it is not recommended to enable both voltage reference output and
          temperature sensor at the same time - only the voltage reference output will be present at both ADC
          inputs.
19.6.2.3 Selecting a Voltage Reference
          The Voltage Reference Selection bit field in the VREF register (VREF.SEL) selects the voltage of VREF
          to be applied to analog modules, e.g. the ADC.




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 239
                                                          SAM D5x/E5x Family Data Sheet
                                                                                 SUPC – Supply Controller

19.6.2.4 Sleep Mode Operation
          The Voltage Reference output and the Temperature Sensor output behavior during sleep mode can be
          configured using the Run in Standby bit and the On Demand bit in the Voltage Reference register
          (VREF.RUNSTDBY, VREF.ONDEMAND), see the following table:
          Table 19-1. VREF Sleep Mode Operation

          VREF.ONDEMAND VREF.RUNSTDBY Voltage Reference Sleep behavior
                     -                      -      Disable
                     0                      0      Always run in all sleep modes except standby sleep mode
                     0                      1      Always run in all sleep modes including standby sleep mode
                     1                      0      Only run if requested by the ADC, in all sleep modes except
                                                   standby sleep mode
                     1                      1      Only run if requested by the ADC, in all sleep modes including
                                                   standby sleep mode

19.6.3    Battery Backup Power Switch

19.6.3.1 Initialization
          The Battery Backup Power Switch (BBPS) is disabled at power-up, and the backup domain is supplied by
          main power.

19.6.3.2 Automatic Battery Backup Power Switch
          The supply of the backup domain can be switched automatically to VBAT supply pin by the Battery
          Backup Power Switch when the BOD33 detects that the VDD supply is below the VDD threshold level
          (BOD33.LEVEL). It is switched back to VDD supply pin when the BOD33 detects that VDD is above the
          VDD threshold level (BOD33.LEVEL).
          To enable this feature, the following configuration is required: BOD33.ACTION=BKUP.

19.6.3.3 Sleep Mode Operation
          The Battery Backup Power Switch is not stopped in any sleep mode.
19.6.3.3.1 Entering Battery Backup Mode
          Entering backup mode can be triggered by either:
           • Wait-for-interrupt (WFI) instruction.
           • BOD33 detection: When the BOD33 detects loss of Main Power, the Backup Domain will be powered
             by battery and the device will enter the backup mode. For this trigger, the following register
             configuration is required: BOD33.ACTION=BKUP.
          Related Links
          18. PM – Power Manager

19.6.3.3.2 Leaving Battery Backup Mode
          Leaving backup mode is triggered by the RSTC when a Backup Mode Exit condition occurs. See RSTC
          module for details.
           • BOD33 exit condition: When the BOD33 detects Main Power is restored and
             BOD33.ACTION=BKUP:
              – When BBPS.WAKEEN=1, the device will leave backup mode and wake up.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 240
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  SUPC – Supply Controller

               – When BBPS.WAKEEN=0, the backup domain will be powered by Main Power, but the device will
                  stay in backup mode.
           • For other exit condition (RTC): The device is kept in battery-powered backup mode until Main Power
             is restored to supply the device. Then, the backup domain will be powered by Main Power.

19.6.4    Output Pins
          The SUPC can drive two outputs. By writing a '1' to the corresponding Output Enable bit in the Backup
          Output Control register (BKOUT.EN), the OUTx pin is driven by the SUPC.
          The OUT pin can be set by writing a '1' to the corresponding Set Output bit in the Backup Output Control
          register (BKOUT.SETx).
          The OUT pin can be cleared by writing a '1' to the corresponding CLR bit (BKOUT.CLRx).
          If a RTC Toggle Enable bit is written to '1' (BKOUT.RTCTGLx), the corresponding OUTx pin will toggle
          when an RTC event occurs.

19.6.5    Brown-Out Detectors

19.6.5.1 Initialization
          Before a Brown-Out Detector (BOD33) is enabled, it must be configured, as outlined by the following:
           • Set the BOD threshold level (BOD33.LEVEL)
           • Set the configuration in Active, Standby, Hibernate, and Backup modes (BOD33.ACTION,
              BOD33.STDBYCFG, BOD33.BKUP, BOD33.RUNHIB, and BOD33.RUNBKUP)
           • Set the prescaling value if the BOD will run in sampling mode (BOD33.PSEL)
           • Set the action and hysteresis (BOD33.ACTION and BOD33.HYST)
          The BOD33 register is Enable-Protected, meaning that they can only be written when the BOD is
          disabled (BOD33.ENABLE=0 and STATUS.B33SRDY=0). As long as the Enable bit is '1', any writes to
          Enable-Protected registers will be discarded, and an APB error will be generated. The Enable bits are not
          Enable-Protected.
19.6.5.2 Enabling, Disabling, and Resetting
          After power or user reset, the BOD33 and BOD12 register values are loaded from the NVM User Page.
          The BOD33 is enabled by writing a '1' to the Enable bit in the BOD control register (BOD33.ENABLE).
          The BOD33 is disabled by writing a '0' to the BOD33.ENABLE.
          Related Links
          18. PM – Power Manager
          9.4 NVM User Page Mapping

19.6.5.3 3.3V Brown-Out Detector (BOD33)
          The 3.3V Brown-Out Detector (BOD33) is able to monitor either the VDD or the VBAT supply and
          compares the voltage with the brown-out threshold levels.
          In all mode except battery backup mode, the BOD33 compares the VDD voltage with the brown-out
          threshold level. This level is set in the BOD33 Level field in the BOD33 register (BOD33.LEVEL). When
          VDD crosses below the brown-out threshold level, the BOD33 can generate either an interrupt,or a
          Reset, or an Automatic Battery Backup Power Switch, depending on the BOD33 Action bit field
          (BOD33.ACTION).
          In battery backup mode, the BOD33 monitors both the VBAT and VDD supplies alternatively. When VBAT
          crosses below the backup brown-out threshold level (BOD33.VBATLEVEL), the BOD33 generates a




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 241
                                                           SAM D5x/E5x Family Data Sheet
                                                                                    SUPC – Supply Controller

         Power Supply Reset. When VDD crosses above the brown-out threshold level (BOD33.LEVEL), the
         device will leave battery backup mode and will wakeup from backup mode if the BBPS.WAKEEN bit is
         set.
         The BOD33 detection status can be read from the BOD33 Detection bit in the Status register
         (STATUS.BOD33DET).
         At start-up or at Power-On Reset (POR), the BOD33 register values are loaded from the NVM User Row.
         Related Links
         9.4 NVM User Page Mapping

19.6.5.3.1 BOD33 Sampling Mode
         The Sampling Mode is a low-power mode where the BOD33 is being repeatedly enabled on a sampling
         clock’s ticks. The BOD33 will monitor the supply voltage (VDD or VBAT) for a short period of time and
         then go to a low-power disabled state until the next sampling clock tick.
         Sampling mode is enabled in Backup or Hibernate mode by writing to the BOD33 bits (BOD33.BKUPCFG
         = 1 or BOD33.HIBCFG = 1). The frequency of the clock ticks (Fclksampling) is controlled by the Prescaler
         Select bit groups in the BOD33 register (BOD33.PSEL).
                          �������������
         ������������ =
                           2 PSEL+1
         The prescaler signal (Fclkprescaler) is a 32 kHz clock, output by the 32 kHz Ultra Low-Power Oscillator
         OSCULP32K.
         Note: If (BOD33.PSEL) is 0, sampling mode is disabled.
         As the sampling clock is different from the APB clock domain, synchronization among the clocks is
         necessary. See 19.6.7 Synchronization for additional information.
         Related Links
         9.4 NVM User Page Mapping

19.6.5.3.2 BOD33 Low Power Mode
         BOD33 Low Power mode is automatically enabled in Backup or Hibernate sleep mode.
         BOD33 Low Power mode can be enabled in Standby sleep mode by writting to '1' the
         BOD33.STDBYCFG bit.
         Related Links
         9.4 NVM User Page Mapping

19.6.5.3.3 BOD33 Hysteresis
         A hysteresis on the trigger threshold of a BOD will reduce the sensitivity to ripples on the monitored
         voltage: instead of switching RESET at each crossing of VBOD, the thresholds for switching RESET on
         and off are separated (VBOD- and VBOD+, respectively).
         Figure 19-2. BOD Hysteresis Principle
         Hysteresis OFF:




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 242
                                                          SAM D5x/E5x Family Data Sheet
                                                                                    SUPC – Supply Controller


                                     VCC
                                                  VBOD



                                  RESET

         Hysteresis ON:


                                     VCC                                 VBOD+
                                                  VBOD-



                                  RESET

         Enabling the BOD33 hysteresis by writing the Hysteresis bit field in the BOD33 register (BOD33.HYST) to
         a non-null value will add hysteresis to the BOD33 threshold level.
         The hysteresis functionality can be used in Sampling Mode.
         Related Links
         9.4 NVM User Page Mapping

19.6.5.3.4 Standby Sleep Mode
         The BOD33 can be used in standby mode if the BOD is enabled and the Run in Standby bit is written to
         '1' (BOD33.RUNSTDBY).
         It is set in Low Power mode if the BOD33.STDBYCFG bit is written to '1'.
         Related Links
         9.4 NVM User Page Mapping

19.6.5.3.5 Backup and Hibernate sleep Modes
         To enable the BOD33 in Backup or Hibernate sleep mode, the Run in Backup or Hibernate sleep mode
         bits in the BOD33 register (BOD33.RUNBKUP, BOD33.RUNHIB) must be written to '1'. The BOD33 is
         automatically set in BOD33 Ultra Low-Power mode. Additionnaly, the BOD33 will operate in Sampling
         mode if the BOD33.PSEL bit is non-null. In this state, the voltage monitored by BOD33 is always the
         supply of the backup domain, i.e. VDD or VBAT.
         Related Links
         9.4 NVM User Page Mapping

19.6.5.4 1.2V Brown-Out Detector (BOD12)
         The BOD12 is calibrated in production and its calibration configuration is stored in the NVM User Row.
         This configuration must not be changed to assure the correct behavior of the BOD12. The BOD12
         generates a reset when 1.2V crosses below the preset brown-out level. The BOD12 is always disabled in
         Standby, Hibernate, and Backup Sleep modes.
         Related Links
         9.4 NVM User Page Mapping

19.6.6   Interrupts
         The SUPC has the following interrupt sources, which are either synchronous or asynchronous wake-up
         sources:
           • VDDCORE Voltage Ready (VCORERDY), asynchronous




         © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 243
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     SUPC – Supply Controller

           •   Voltage Regulator Ready (VREGRDY) asynchronous
           •   BOD33 Ready (BOD33RDY), synchronous
           •   BOD33 Detection (BOD33DET), asynchronous
           •   BOD33 Synchronization Ready (B33SRDY), synchronous
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear register (INTFLAG) is set when the interrupt condition occurs.
         Each interrupt can be individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Set register (INTENSET), and disabled by writing a '1' to the corresponding bit in the Interrupt Enable
         Clear register (INTENCLR).
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until either the interrupt flag is cleared, the interrupt is disabled, or
         the SUPC is reset. See the INTFLAG register for details on how to clear interrupt flags. The user must
         read the INTFLAG register to determine which interrupt condition is present.
         Note: Interrupts must be globally enabled for interrupt requests to be generated.

19.6.7   Synchronization
         The prescaler counters that are used to trigger brown-out detections operate asynchronously from the
         peripheral bus. As a consequence, the BOD33 Enable bit (BOD33.ENABLE) need synchronization when
         written.
         The Write-Synchronization of the Enable bit is triggered by writing a '1' to the Enable bit of the BOD33
         Control register. The Synchronization Ready bit (STATUS.B33SRDY) in the STATUS register will be
         cleared when the Write-Synchronization starts, and set again when the Write-Synchronization is
         complete. Writing to the same register while the Write-Synchronization is ongoing (STATUS.B33SRDY is
         '0') will generate a PAC error without stalling the APB bus.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 244
                                                                SAM D5x/E5x Family Data Sheet
                                                                                            SUPC – Supply Controller


19.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0                                                              B33SRDY       BOD33DET     BOD33RDY
                             15:8                                                             VCORERDY                    VREGRDY
 0x00        INTENCLR
                             23:16
                             31:24
                              7:0                                                              B33SRDY       BOD33DET     BOD33RDY
                             15:8                                                             VCORERDY                    VREGRDY
 0x04        INTENSET
                             23:16
                             31:24
                              7:0                                                              B33SRDY       BOD33DET     BOD33RDY
                             15:8                                                             VCORERDY                    VREGRDY
 0x08        INTFLAG
                             23:16
                             31:24
                              7:0                                                              B33SRDY       BOD33DET     BOD33RDY
                             15:8                                                             VCORERDY                    VREGRDY
 0x0C         STATUS
                             23:16
                             31:24
                              7:0     RUNBKUP   RUNHIB    RUNSTDBY    STDBYCFG          ACTION[1:0]            ENABLE
                             15:8                         PSEL[2:0]                                     HYST[3:0]
 0x10         BOD33
                             23:16                                         LEVEL[7:0]
                             31:24                                       VBATLEVEL[7:0]
 0x14
   ...       Reserved
 0x17
                              7:0     RUNBKUP                                                     SEL          ENABLE
                             15:8
 0x18          VREG
                             23:16                                                                                         VSEN
                             31:24                                                                           VSPER[2:0]
                              7:0     ONDEMAND RUNSTDBY                            TSSEL       VREFOE              TSEN
                             15:8
 0x1C          VREF
                             23:16                                                                      SEL[3:0]
                             31:24
                              7:0                                                              WAKEEN                      CONF
                             15:8
 0x20          BBPS
                             23:16
                             31:24
                              7:0                                                                                   EN1     EN0
                             15:8                                                                                  CLR1     CLR0
 0x24         BKOUT
                             23:16                                                                                 SET1     SET0
                             31:24                                                                            RTCTGL1     RTCTGL0
                              7:0                                                                               BKIN1      BKIN0
                             15:8
 0x28          BKIN
                             23:16
                             31:24




          © 2019 Microchip Technology Inc.                        Datasheet                                  DS60001507E-page 245
                                                          SAM D5x/E5x Family Data Sheet
                                                                                   SUPC – Supply Controller


19.8   Register Description
       Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
       the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
       accessed directly.
       Some registers are optionally write-protected by the Peripheral Access Controller (PAC). PAC Write-
       protection is denoted by the "PAC Write-Protection" property in each individual register description. Refer
       to 19.5.8 Register Access Protection for details.
       Some registers require synchronization when read and/or written. Synchronization is denoted by the
       "Write-Synchronized" or the "Read-Synchronized" property in each individual register description. Refer
       to 19.6.7 Synchronization for details.




       © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 246
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                        SUPC – Supply Controller

19.8.1         Interrupt Enable Clear

               Name:       INTENCLR
               Offset:     0x00
               Reset:      0x00000000
               Property:   PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit        31            30           29           28            27           26           25            24


   Access
    Reset


         Bit        23            22           21           20            19           18           17            16


   Access
    Reset


         Bit        15            14           13           12            11           10            9            8
                                                                                   VCORERDY                   VREGRDY
   Access                                                                             R/W                        R/W
    Reset                                                                              0                          0


         Bit         7            6            5             4            3            2             1            0
                                                                                    B33SRDY      BOD33DET     BOD33RDY
   Access                                                                             R/W           R/W          R/W
    Reset                                                                              0             0            0


               Bit 10 – VCORERDY VDDCORE Voltage Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the VDDCORE Ready Interrupt Enable bit, which disables the VDDCORE
               Ready interrupt.
               Value         Description
               0             The VDDCORE Ready interrupt is disabled.
               1             The VDDCORE Ready interrupt is enabled and an interrupt request will be generated when
                             the VCORERDY Interrupt Flag is set.

               Bit 8 – VREGRDY Voltage Regulator Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Voltage Regulator Ready Interrupt Enable bit, which disables the
               Voltage Regulator Ready interrupt.
                Value        Description
                0            The Voltage Regulator Ready interrupt is disabled.
                1            The Voltage Regulator Ready interrupt is enabled and an interrupt request will be generated
                             when the Voltage Regulator Ready Interrupt Flag is set.

               Bit 2 – B33SRDY BOD33 Synchronization Ready Interrupt Enable
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 247
                                                  SAM D5x/E5x Family Data Sheet
                                                                           SUPC – Supply Controller

Writing a '1' to this bit will clear the BOD33 Synchronization Ready Interrupt Enable bit, which disables
the BOD33 Synchronization Ready interrupt.
 Value        Description
 0            The BOD33 Synchronization Ready interrupt is disabled.
 1            The BOD33 Synchronization Ready interrupt is enabled, and an interrupt request will be
              generated when the BOD33 Synchronization Ready Interrupt flag is set.

Bit 1 – BOD33DET BOD33 Detection Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the BOD33 Detection Interrupt Enable bit, which disables the BOD33
Detection interrupt.
Value         Description
0             The BOD33 Detection interrupt is disabled.
1             The BOD33 Detection interrupt is enabled, and an interrupt request will be generated when
              the BOD33 Detection Interrupt flag is set.

Bit 0 – BOD33RDY BOD33 Ready Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the BOD33 Ready Interrupt Enable bit, which disables the BOD33 Ready
interrupt.
 Value        Description
 0            The BOD33 Ready interrupt is disabled.
 1            The BOD33 Ready interrupt is enabled, and an interrupt request will be generated when the
              BOD33 Ready Interrupt flag is set.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 248
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                           SUPC – Supply Controller

19.8.2         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x04
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

         Bit        31            30            29            28           27            26            25            24


   Access
    Reset


         Bit        23            22            21            20           19            18            17            16


   Access
    Reset


         Bit        15            14            13            12            11           10             9            8
                                                                                     VCORERDY                    VREGRDY
   Access                                                                               R/W                         R/W
    Reset                                                                                 0                          0


         Bit         7             6            5             4             3             2             1            0
                                                                                      B33SRDY      BOD33DET      BOD33RDY
   Access                                                                               R/W           R/W           R/W
    Reset                                                                                 0             0            0


               Bit 10 – VCORERDY VDDCORE Voltage Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the VDDCORE Ready Interrupt Enable bit, which enables the VDDCORE
               Ready interrupt.
               Value         Description
               0             The VDDCORE Ready interrupt is disabled.
               1             The VDDCORE Ready interrupt is enabled and an interrupt request will be generated when
                             the VCORERDY Interrupt Flag is set.

               Bit 8 – VREGRDY Voltage Regulator Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Voltage Regulator Ready Interrupt Enable bit, which enables the Voltage
               Regulator Ready interrupt.
               Value         Description
               0             The Voltage Regulator Ready interrupt is disabled.
               1             The Voltage Regulator Ready interrupt is enabled and an interrupt request will be generated
                             when the Voltage Regulator Ready Interrupt Flag is set.

               Bit 2 – B33SRDY BOD33 Synchronization Ready Interrupt Enable
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 249
                                                  SAM D5x/E5x Family Data Sheet
                                                                          SUPC – Supply Controller

Writing a '1' to this bit will set the BOD33 Synchronization Ready Interrupt Enable bit, which enables the
BOD33 Synchronization Ready interrupt.
Value         Description
0             The BOD33 Synchronization Ready interrupt is disabled.
1             The BOD33 Synchronization Ready interrupt is enabled, and an interrupt request will be
              generated when the BOD33 Synchronization Ready Interrupt flag is set.

Bit 1 – BOD33DET BOD33 Detection Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the BOD33 Detection Interrupt Enable bit, which enables the BOD33
Detection interrupt.
Value         Description
0             The BOD33 Detection interrupt is disabled.
1             The BOD33 Detection interrupt is enabled, and an interrupt request will be generated when
              the BOD33 Detection Interrupt flag is set.

Bit 0 – BOD33RDY BOD33 Ready Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the BOD33 Ready Interrupt Enable bit, which enables the BOD33 Ready
interrupt.
 Value        Description
 0            The BOD33 Ready interrupt is disabled.
 1            The BOD33 Ready interrupt is enabled, and an interrupt request will be generated when the
              BOD33 Ready Interrupt flag is set.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 250
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                           SUPC – Supply Controller

19.8.3         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x08
               Reset:       0x0000010X
               Property:    -
               In the reset value: X= determined from NVM User Row (0xX=0bx00y)


         Bit        31            30            29            28           27            26            25               24


   Access
    Reset


         Bit        23            22            21            20           19            18            17               16


   Access
    Reset


         Bit        15            14            13            12           11            10            9                8
                                                                                     VCORERDY                    VREGRDY
   Access                                                                               R/W                         R/W
    Reset                                                                                 0                             0


         Bit         7             6            5             4             3             2            1                0
                                                                                      B33SRDY      BOD33DET      BOD33RDY
   Access                                                                               R/W           R/W           R/W
    Reset                                                                                 0            0                y


               Bit 10 – VCORERDY VDDCORE Voltage Ready
               This flag is cleared by writing a '1 to it.
               This flag is set on a zero-to-one transition of the VDDCORE Ready bit in the Status register
               (STATUS.VCORERDY) and will generate an interrupt request if INTENSET.VCORERDY=1.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the VCORERDY interrupt flag.

               Bit 8 – VREGRDY Voltage Regulator Ready
               This flag is cleared by writing a '1' to it.
               This flag is set on a zero-to-one transition of the Voltage Regulator Ready bit in the Status register
               (STATUS.VREGRDY) and will generate an interrupt request if INTENSET.VREGRDY=1.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the VREGRDY interrupt flag.

               Bit 2 – B33SRDY BOD33 Synchronization Ready
               This flag is cleared by writing a '1' to it.
               This flag is set on a zero-to-one transition of the BOD33 Synchronization Ready bit in the Status register
               (STATUS.B33SRDY) and will generate an interrupt request if INTENSET.B33SRDY=1.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit clears the BOD33 Synchronization Ready interrupt flag.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 251
                                                   SAM D5x/E5x Family Data Sheet
                                                                            SUPC – Supply Controller

Bit 1 – BOD33DET BOD33 Detection
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the BOD33 Detection bit in the Status register
(STATUS.BOD33DET) and will generate an interrupt request if INTENSET.BOD33DET=1.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the BOD33 Detection interrupt flag.

Bit 0 – BOD33RDY BOD33 Ready
This flag is cleared by writing a '1' to it.
This flag is set on a zero-to-one transition of the BOD33 Ready bit in the Status register
(STATUS.BOD33RDY) and will generate an interrupt request if INTENSET.BOD33RDY=1.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit clears the BOD33 Ready interrupt flag.
The BOD33 can be enabled.
Related Links
9.4 NVM User Page Mapping




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 252
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     SUPC – Supply Controller

19.8.4         Status

               Name:       STATUS
               Offset:     0x0C
               Reset:      Determined from NVM User Row
               Property:   -


         Bit        31           30           29          28           27          26           25           24


   Access
    Reset


         Bit        23           22           21          20           19          18           17           16


   Access
    Reset


         Bit        15           14           13          12           11          10            9           8
                                                                               VCORERDY                  VREGRDY
   Access                                                                           R                        R
    Reset                                                                           1                        1


         Bit        7             6           5           4            3            2            1           0
                                                                                B33SRDY     BOD33DET     BOD33RDY
   Access                                                                           R           R            R
    Reset                                                                           1            0           y


               Bit 10 – VCORERDY VDDCORE Voltage Ready
               Value      Description
               0          the VDDCORE voltage is not as expected.
               1          the VDDCORE voltage is the target voltage.

               Bit 8 – VREGRDY Voltage Regulator Ready
               Value      Description
               0          The selected voltage regulator in VREG.SEL is not ready.
               1          The voltage regulator selected in VREG.SEL is ready and the core domain is supplied by
                          this voltage regulator.

               Bit 2 – B33SRDY BOD33 Synchronization Ready
               Value      Description
               0          BOD33 synchronization is ongoing.
               1          BOD33 synchronization is complete.

               Bit 1 – BOD33DET BOD33 Detection
               Value      Description
               0          No BOD33 detection.
               1          BOD33 has detected that the I/O power supply is going below the BOD33 reference value.




           © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 253
                                            SAM D5x/E5x Family Data Sheet
                                                          SUPC – Supply Controller

Bit 0 – BOD33RDY BOD33 Ready
The BOD33 can be enabled at start-up from NVM User Row.
 Value     Description
 0         BOD33 is not ready.
 1         BOD33 is ready.

Related Links
9.4 NVM User Page Mapping




© 2019 Microchip Technology Inc.              Datasheet            DS60001507E-page 254
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                   SUPC – Supply Controller

19.8.5         3.3V Brown-Out Detector (BOD33) Control

               Name:       BOD33
               Offset:     0x10
               Reset:      Determined from NVM User Row
               Property:   Write-Synchronized, PAC Write-Protection


         Bit        31           30              29          28                27                 26               25           24
                                                             VBATLEVEL[7:0]
   Access          R/W          R/W             R/W         R/W                R/W            R/W                  R/W         R/W
    Reset           0             0              0           0                  0                 0                 0           0


         Bit        23           22              21          20                19                 18               17           16
                                                                  LEVEL[7:0]
   Access          R/W          R/W             R/W         R/W                R/W            R/W                  R/W         R/W
    Reset           0             0               x          x                  x                 x                 x           x


         Bit        15           14              13          12                11                 10                9           8
                                              PSEL[2:0]                                                HYST[3:0]
   Access                       R/W             R/W         R/W                R/W            R/W                  R/W         R/W
    Reset                         0              0           0                  x                 x                 x           x


         Bit        7             6              5           4                  3                 2                 1           0
                 RUNBKUP       RUNHIB         RUNSTDBY    STDBYCFG                  ACTION[1:0]               ENABLE
   Access          R/W          R/W             R/W         R/W                R/W            R/W                  R/W
    Reset           0             0              0           0                  y                 y                 z


               Bits 31:24 – VBATLEVEL[7:0] BOD33 Threshold Level on VBAT
               This field sets the triggering voltage threshold for the BOD33 when the BOD33 monitors VBAT in battery
               backup sleep mode.
               This field is not synchronized.

               Bits 23:16 – LEVEL[7:0] BOD33 Threshold Level on VDD
               This field sets the triggering voltage threshold for the BOD33 when the BOD33 monitors VDD. If an
               hysteresis value is programmed (BOD33.HYST), this field corresponds to the lower threshold (VBOD-).
               These bits are loaded from NVM User Row at start-up.
               This field is not synchronized.
               The VBOD- input voltage can be calculated as follows: VBOD- = 1.5 + LEVEL[7:0) x Level_Step
               And the upper threshold (VBOD+) is then: VBOD+ = VBOD- + N x HYST_STEP, With N=0 to 15
               according to HYST[3:0] value and HYST_STEP = Level_Step, (refer to Bits 11:8 – HYST[3:0]: BOD33
               Hysteresis voltage value on VDD).
               At the upper side of Level[7:0] values depending on the Hysteresis value chosen with HYST[3:0], the
               VBOD+ level reaches an overflow, e.g., for HYST[3:0] = 0d2 the hysteresis is 2 x Level_Step = 12 mV up
               to position 253 and position 254 to 255 above must not be used.

               Bits 14:12 – PSEL[2:0] Prescaler Select
               Selects the prescaler divide-by output for the BOD33 sampling mode available in hibernate, backup or
               battery backup mode. The input clock comes from the OSCULP32K 32KHz output.




           © 2019 Microchip Technology Inc.                         Datasheet                                       DS60001507E-page 255
                                                    SAM D5x/E5x Family Data Sheet
                                                                        SUPC – Supply Controller

 Value        Name                 Description
 0x0          NODIV                Not divided: Sampling mode is OFF.
 0x1          DIV4                 Divide clock by 4
 0x2          DIV8                 Divide clock by 8
 0x3          DIV16                Divide clock by 16
 0x4          DIV32                Divide clock by 32
 0x5          DIV64                Divide clock by 64
 0x6          DIV128               Divide clock by 128
 0x7          DIV256               Divide clock by 256

Bits 11:8 – HYST[3:0] BOD33 Hysteresis Voltage Value on VDD
This field sets the hysteresis voltage value related to "BOD33 Threshold Level on VDD" field when the
BOD33 monitors VDD.
These bits are loaded from NVM User Row at start-up.
This field is not synchronized.
 Value        Description
 0            No hysteresis.
 N            Hysteresis value is set to N*HYST_STEP.
              See the Electrical Characteristics section for the HYST_STEP voltage level.

Bit 7 – RUNBKUP BOD33 Configuration in Backup Sleep Mode
This field is not synchronized.
 Value        Description
 0            In backup sleep mode, the BOD33 is disabled.
 1            In backup sleep mode, the BOD33 is enabled and configured in sampling mode.

Bit 6 – RUNHIB BOD33 Configuration in Hibernate Sleep Mode
This field is not synchronized.
 Value        Description
 0            In hibernate sleep mode, the BOD33 is disabled.
 1            In hibernate sleep mode, the BOD33 is enabled and configured in sampling mode.

Bit 5 – RUNSTDBY Run in Standby
This bit is not synchronized.
 Value       Description
 0           In standby sleep mode, the BOD33 is disabled.
 1           In standby sleep mode, the BOD33 is enabled.

Bit 4 – STDBYCFG BOD33 Configuration in Standby Sleep Mode
If the RUNSTDBY bit is set to '1', the STDBYCFG bit sets the BOD33 configuration in standby sleep
mode.
This field is not synchronized.
 Value        Description
 0            In standby sleep mode, the BOD33 is enabled and configured in normal mode.
 1            In standby sleep mode, the BOD33 is enabled and configured in low power mode.

Bits 3:2 – ACTION[1:0] BOD33 Action
These bits are used to select the BOD33 action when the supply voltage crosses below the BOD33
threshold.




© 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 256
                                                    SAM D5x/E5x Family Data Sheet
                                                                          SUPC – Supply Controller

These bits are loaded from NVM User Row at start-up.
This field is not synchronized.

   Value        Name        Description
    0x0         NONE        No action
    0x1        RESET        The BOD33 generates a reset
    0x2          INT        The BOD33 generates an interrupt
    0x3        BKUP-        The BOD33 puts the device in battery backup sleep mode.


Bit 1 – ENABLE Enable
This bit is loaded from NVM User Row at start-up.
This bit is not enable-protected.
 Value        Description
 0            BOD33 is disabled.
 1            BOD33 is enabled.

Related Links
9.4 NVM User Page Mapping




© 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 257
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                      SUPC – Supply Controller

19.8.6         Voltage Regulator System (VREG) Control

               Name:       VREG
               Offset:     0x18
               Reset:      0x00000002
               Property:   PAC Write-Protection


         Bit        31           30           29             28         27           26             25          24
                                                                                              VSPER[2:0]
   Access                                                                           R/W            R/W         R/W
    Reset                                                                            0              0           0


         Bit        23           22           21             20         19           18             17          16
                                                                                                              VSEN
   Access                                                                                                      R/W
    Reset                                                                                                       0


         Bit        15           14           13             12         11           10             9           8


   Access
    Reset


         Bit         7            6            5             4          3            2              1           0
                 RUNBKUP                                                            SEL           ENABLE
   Access          R/W                                                              R/W            R/W
    Reset            0                                                               0              1


               Bits 26:24 – VSPER[2:0] Voltage Scaling Period
               This bitfield defines the time between the voltage steps when the VDDCORE voltage scaling is enabled.
               The time is (2VSPER) * T, where T is an internal period (typ 250 ns).

               Bit 16 – VSEN Voltage Scaling Enable
               Value      Description
               0          The voltage scaling is disabled.
               1          The voltage scaling is enabled.

               Bit 7 – RUNBKUP Run in Backup
               This bit controls how the main voltage regulator behaves in backup sleep mode.
                Value       Description
                0           The main voltage regulator is halted during backup sleep mode.
                1           The main voltage regulator is not stopped during backup sleep mode.

               Bit 2 – SEL Voltage Regulator Selection
               This bit is loaded from NVM User Row at start-up. Refer to NVM User Row Mapping section for more
               details.
                Value        Description
                0            The main voltage regulator is a LDO voltage regulator.
                1            The main voltage regulator is a buck converter.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 258
                                   SAM D5x/E5x Family Data Sheet
                                               SUPC – Supply Controller

Bit 1 – ENABLE Must be set to 1.
Related Links
9.4 NVM User Page Mapping




© 2019 Microchip Technology Inc.   Datasheet            DS60001507E-page 259
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                        SUPC – Supply Controller

19.8.7         Voltage References System (VREF) Control

               Name:       VREF
               Offset:     0x1C
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31           30            29           28           27            26               25          24


   Access
    Reset


         Bit        23           22            21           20           19            18               17          16
                                                                                            SEL[3:0]
   Access                                                                R/W          R/W              R/W         R/W
    Reset                                                                 0            0                0           0


         Bit        15           14            13           12           11            10               9           8


   Access
    Reset


         Bit         7            6            5             4            3            2                1           0
                ONDEMAND     RUNSTDBY                                   TSSEL       VREFOE             TSEN
   Access          R/W           R/W                                     R/W          R/W              R/W
    Reset            0            0                                       0            0                0


               Bits 19:16 – SEL[3:0] Voltage Reference Selection
               These bits select the Voltage Reference for the ADC/DAC.
                Value      Name            Description
                0x0        1V0             1.0V voltage reference typical value
                0x1        1V1             1.1V voltage reference typical value
                0x2        1V2             1.2V voltage reference typical value
                0x3        1V25            1.25V voltage reference typical value
                0x4        2V0             2.0V voltage reference typical value
                0x5        2V2             2.2V voltage reference typical value
                0x6        2V4             2.4V voltage reference typical value
                0x7        2V5             2.5V voltage reference typical value
                Others                     Reserved

               Bit 7 – ONDEMAND On Demand Control
               The On Demand operation mode allows to enable or disable the voltage reference depending on
               peripheral requests.
                Value      Description
                0          The voltage reference is always on, if enabled.
                1          The voltage reference is enabled when a peripheral is requesting it. The voltage reference is
                           disabled if no peripheral is requesting it.




           © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 260
                                               SAM D5x/E5x Family Data Sheet
                                                                      SUPC – Supply Controller

Bit 6 – RUNSTDBY Run In Standby
The bit controls how the voltage reference behaves during standby sleep mode.
 Value      Description
 0          The voltage reference is halted during standby sleep mode.
 1          The voltage reference is not stopped in standby sleep mode. If VREF.ONDEMAND=1, the
            voltage reference will be running when a peripheral is requesting it. If VREF.ONDEMAND=0,
            the voltage reference will always be running in standby sleep mode.

Bit 3 – TSSEL Temperature Sensor Channel Selection
Value      Description
0          The Temperature Sensor PTAT channel is selected.
1          The Temperature Sensor CTAT channel is selected.

Bit 2 – VREFOE Voltage Reference Output Enable
Value      Description
0          The Voltage Reference output (INTREF) is not available as an ADC input channel.
1          The Voltage Reference output (INTREF) is routed to an ADC input channel.

Bit 1 – TSEN Temperature Sensor Enable
Value      Description
0          Temperature Sensor is disabled.
1          Temperature Sensor is enabled and routed to an ADC input channel.




© 2019 Microchip Technology Inc.                 Datasheet                         DS60001507E-page 261
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   SUPC – Supply Controller

19.8.8         Battery Backup Power Switch (BBPS) Control

               Name:       BBPS
               Offset:     0x20
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31           30           29         28          27           26          25              24


   Access
    Reset


         Bit        23           22           21         20          19           18          17              16


   Access
    Reset


         Bit        15           14           13         12           11          10           9              8


   Access
    Reset


         Bit        7             6           5          4            3           2            1              0
                                                                               WAKEEN                    CONF
   Access                                                                        R/W                      R/W
    Reset                                                                         0                           0


               Bit 2 – WAKEEN Wake Enable
               Value      Description
               0          The device is not woken up when switched from battery backup power to Main Power.
               1          The device is woken up when switched from battery backup power to Main Power.

               Bit 0 – CONF Battery Backup Power Switch Configuration
               Value      Name      Description
               0x0        BOD33     The power switch is handled by the BOD33 according to the BOD33.ACTION bit
                                    field.
               0x1        FORCED In backup sleep mode, the backup domain is always supplied by Battery Backup
                                    Power.




           © 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 262
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                   SUPC – Supply Controller

19.8.9         Backup Output (BKOUT) Control

               Name:        BKOUT
               Offset:      0x24
               Reset:       0x00000000
               Property:    PAC Write-Protection


         Bit         31            30            29            28            27   26       25           24
                                                                                         RTCTGL1     RTCTGL0
   Access                                                                                  R/W         R/W
    Reset                                                                                   0           0


         Bit         23            22            21            20            19   18       17           16
                                                                                          SET1         SET0
   Access                                                                                  W            W
    Reset                                                                                   0           0


         Bit         15            14            13            12            11   10        9           8
                                                                                          CLR1        CLR0
   Access                                                                                  W            W
    Reset                                                                                   0           0


         Bit         7             6              5             4            3    2         1           0
                                                                                          EN1          EN0
   Access                                                                                  R/W         R/W
    Reset                                                                                   0           0


               Bits 24, 25 – RTCTGL RTC Toggle Output
               Value       Description
               0           The output will not toggle on RTC event.
               1           The output will toggle on RTC event.

               Bits 16, 17 – SET Set Output
               Writing a '0' to a bit has no effect.
               Writing a '1' to a bit will set the corresponding output.
               Reading this bit returns '0'.

               Bits 8, 9 – CLR Clear Output
               Writing a '0' to a bit has no effect.
               Writing a '1' to a bit will clear the corresponding output.
               Reading this bit returns '0'.

               Bits 0, 1 – EN Enable Output
               Value        Description
               0            The output is not enabled.
               1            The output is enabled and driven by the SUPC.




           © 2019 Microchip Technology Inc.                           Datasheet             DS60001507E-page 263
                                                              SAM D5x/E5x Family Data Sheet
                                                                                     SUPC – Supply Controller

19.8.10 Backup Input (BKIN) Value

            Name:       BKIN
            Offset:     0x28
            Reset:      0x00000000
            Property:   -


      Bit        31           30            29           28           27           26            25           24


  Access
   Reset


      Bit        23           22            21           20           19           18            17           16


  Access
   Reset


      Bit        15           14            13           12           11           10            9            8


  Access
   Reset


      Bit         7            6            5            4             3            2            1            0
                                                                                               BKIN1        BKIN0
  Access                                                                                         R            R
   Reset                                                                                         0            0


            Bits 0, 1 – BKIN Backup Input Value
            These bits are cleared when the corresponding backup I/O pin detects a logical low level on the input pin
            or when the backup I/O is not enabled.
            These bits are set when the corresponding backup I/O pin detects a logical high level on the input pin
            when the backup I/O is enabled.
             Value      Name      Description
             BKIN[0] OUT[0] If BKOUT.EN[0]=1, BKIN[0] will give the input value of the OUT[0] pin
             BKIN[1] OUT[1] If BKOUT.EN[1]=1, BKIN[1] will give the input value of the OUT[1] pin




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 264
