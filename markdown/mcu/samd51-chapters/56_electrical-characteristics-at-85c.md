# 54. Electrical Characteristics at 85°C

*Source: `Atmel-SAMD51.pdf`, pages 1986-2034 — SAMD51 family datasheet*

                                                             SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 85°C


54.        Electrical Characteristics at 85°C

54.1       Disclaimer
           All typical values are measured at T = 25°C unless otherwise specified. All minimum and maximum
           values are valid across operating temperature and voltage unless otherwise specified.



54.2       Absolute Maximum Ratings
           Stresses beyond those listed in the table below may cause permanent damage to the device. This is a
           stress rating only and functional operation of the device at these or other conditions beyond those
           indicated in the operational sections of this specification is not implied. Exposure to absolute maximum
           rating conditions for extended periods may affect device reliability.
Table 54-1. Absolute Maximum Ratings

Symbol                    Description                              Min.                    Max.                 Units
VDD                       Power supply voltage                     0                       3.8                  V
IVDD                      Current into a VDD pin(1,2)              -                       60                   mA
IGND                      Current out of a GND pin                 -                       45                   mA
VPIN                      Pin voltage with respect to GND and VDD GND-0.6V                 VDD+0.6V             V
Tstorage                  Storage temperature                      -60                     150                  °C

           Note:
            1. For 100-pin packages: IVDD (pin 92) = 360 mA and IVDD (pin 77) = 210 mA.
            2. For 128-pin packages: IVDD (pin 118) = 360 mA and IVDD (pin 97) = 210 mA.



               CAUTION
                          This device is sensitive to electrostatic discharges (ESD). Improper handling may lead to
                          permanent performance degradation or malfunctioning.
                          Handle the device following best practice ESD protection rules: Be aware that the human body
                          can accumulate charges large enough to impair functionality or destroy the device.




54.3       General Operating Ratings
         The device must operate within the ratings listed below in order for all other electrical characteristics and
         typical characteristics of the device to be valid.
Table 54-2. General Operating Conditions

Symbol                   Description                                Min.            Typ.            Max.         Units
VDDIO                    IO Supply Voltage                          1.71(1)         3.3             3.63         V
VDDIOB                   IOB Supply Voltage                         1.71(1)         3.3             3.63         V
VDDANA                   Analog supply voltage                      1.71(1)         3.3             3.63         V




           © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1986
                                                              SAM D5x/E5x Family Data Sheet
                                                                               Electrical Characteristics at 85°C

...........continued
Symbol                  Description                                  Min.            Typ.             Max.         Units
TA                      Temperature range                            -40             25               85           °C
TJ                      Junction temperature                         -               -                105          °C
VBAT                    Battery Supply Voltage                       1.71(1)         3.3              3.63         V

          Note:
           1. With BOD33 disabled.
           2. The same voltage must be applied to VDDIO and VDDANA. VDDIOB should be lower or equal to VDDIO /
                VDDANA. The common voltage is referred to as VDD in the data sheet.
           3. When I/O pads in the VDDIOB cluster are multiplexed as analog pads, VDDANA is used to power the
                I/O. Using this configuration may result in an electrical conflict if the VDDIOB voltage is different from
                that of VDDIO / VDDANA. If the application has such requirements, it is required to power VDDIOB,
                VDDIO and VDDANA from the same supply source to ensure that they are always at the same
                voltage.



54.4      Injection Current
          Stresses beyond those listed in the table below may cause permanent damage to the device. This is a
          stress rating only and functional operation of the device at these or other conditions beyond those
          indicated in the operational sections of this specification is not implied. Exposure to absolute maximum
          rating conditions for extended periods may affect device reliability.
Table 54-3. Injection Current(1, 2)

Symbol Description                               min Typ. max Unit Comments
IICL       Input Low Injection Current           -15 -         -    mA Note: 1, 4, 5
                                                                       This Parameter applies to all pins.

IICH       Input High Injection Current           -    -      15    mA Note: 2, 3, 4, 5
                                                                       This parameter applies to all pins, with the
                                                                       exception of 5V tolerant pins.

∑IICT      Total Input Injection Current (Sum     -    -      45    mA Absolute instantaneous sum of all ± input injection
           of all I/O and control pins)                                currents from all I/O pins.
           Absolute value of |∑IICT|




          © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1987
                                                               SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 85°C

       Note:
        1. VIL source < (VSS - 0.6). Characterized but not tested.
        2. VIH source > (VDDIO + 0.6) for non-5V tolerant pins only.
        3. Digital 5V tolerant pins do not have an internal high side diode to VDDIO, and therefore, cannot
             tolerate any “positive” input injection current.
        4. Injection currents > | 0 | can affect the ADC results by approximately 4 to 6 counts (i.e., VIH Source
             > (VDDIO + 0.6) or VIL source < (GND - 0.6)).
        5. Any number and/or combination of I/O pins not excluded under IICL or IICH conditions are
             permitted provided the “absolute instantaneous” sum of the input injection currents from all pins do
             not exceed the specified ∑IICT limit. To limit the injection current the user must insert a resistor in
             series RS between input source voltage and device pin. The resistor value is calculated according
             to:
               – For negative Input voltages less than (GND-0.6): RS ≥ (((GND - 0.6) - VIL source) / IICL)
               – For positive input voltages greater than (VDDIO+0.6): RS ≥ ((VIH source - VDDIO)/ IICH)
               – For Vpin voltages > VDD and < GND then RS = the larger of the values calculated above



54.5   Supply Characteristics
       Table 54-4. Supply Characteristics

        Symbol                   Conditions           Voltage
                                                      Min.                    Max.                Units
        VDDIO                    Full Voltage Range 1.71                      3.63                V
        VDDIOB
        VDDANA
        VBAT

       Table 54-5. Supply Rates(1)

                                                   Fall Rate                   Rise Rate
             Symbol            Conditions                                                                  Units
                                                     Max.              Min.                Max.
        VDDIO                DC Supply        50                 0.2                 100              mV/µs
                             Peripheral I/Os,
        VDDIOB
                             Internal
        VDDANA               Regulator, and
                             Analog Supply
        VBAT
                             Voltage

       Note: 1. These values are based on simulation. They are not covered by production test limits or
       characterization.




       © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1988
                                                                SAM D5x/E5x Family Data Sheet
                                                                               Electrical Characteristics at 85°C

           Table 54-6. Power Supply Current Requirement

            Symbol               Conditions                                            Current            Units
                                                                                       Max
            Iinput               Power-up Maximum Current                              7                  mA

           Note: Iinput is the minimum requirement for the power supply connected to the device.



54.6       Maximum Clock Frequencies
Table 54-7. Maximum GCLK Generator Output Frequencies (see Notes 1, 2)

Symbol                    Description                                    Conditions        Fmax                   Units
fGCLKGEN0 /               GCLK Generator Output Frequency                undivided         200                    MHz
fGCLK_MAIN (see
Note 2)
FgclkgenX, x={1;7}                                                                         200                    MHz
FgclkgenX, ,                                                                               100                    MHz
x={8;11}

           Note:
            1. These values are based on simulation. They are not covered by production test limits or
                 characterization.
            2. GCLK Generator 0 output frequency must not exceed the AHB clock frequency. The output must be
                 divided in case of the GCLK Generator 0 input frequency is higher than the AHB clock frequency.
Table 54-8. Maximum Peripheral Clock Frequencies(1)

Symbol                                       Description                                                  Max.      Units
fCPU                                         CPU clock frequency                                          120       MHz
fAHB                                         AHB clock frequency                                          120       MHz
fAPBx, x = {A, B, C, D}                      APBA, APBB, APBC and APBD clock frequency                    120       MHz
fGCLK_DPLLx, x = {0,1}                       FDPLL0 and FDPLL1 Reference clock frequency                  3.2       MHz
fGCLK_DPLLx_32K, x = {0,1}                   FDPLL0 and FDPLL1 32k Reference clock frequency              100       kHz
fGCLK_DFLL48M_REF                            DFLL48M Reference clock frequency                            33        kHz
fGCLK_EIC                                    EIC input clock frequency                                    100       MHz
fGCLK_FREQM_MSR                              FREQM Measure                                                200       MHz
fGCLK_FREQM_REF                              FREQM Reference                                              100       MHz
fGCLK_EVSYS_CHANNEL_x, x = {0,.., 11}        EVSYS channel x input clock frequency                        100       MHz
fGCLK_SERCOMx_SLOW, x = {0, ... , 7}         Common SERCOMx slow input clock frequency                    12        MHz
fGCLK_SERCOMx_CORE, x = {0, ... , 7}         SERCOMx input clock frequency                                100       MHz




          © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1989
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                 Electrical Characteristics at 85°C

...........continued
Symbol                                        Description                                                Max.     Units
fGCLK_CANx, x = {0, 1}                        CANx input clock frequency                                 100      MHz
fGCLK_USB                                     USB input clock frequency                                  60       MHz
fGCLK_I2S                                     I2S input clock frequency                                  100      MHz
fGCLK_SDHCx_SLOW, x = {0, 1}                  Common SDHCx slow input clock frequency                    12       MHz
fGCLK_SDHCx_CORE, x = {0, 1}                  SDHCx input clock frequency                                150      MHz
fGCLK_TCCx, x = {0, ... , 4}                  TCCx input clock frequency                                 200      MHz
fGCLK_TCx, x = {0, ... , 3}                   TC0, TC1, TC2, TC3 input clock frequency                   200      MHz
fGCLK_TCx, x = {4, ... , 7}                   TC4, TC5, TC6, TC7 input clock frequency                   100      MHz
fGCLK_PDEC                                    PDEC input clock frequency                                 200      MHz
fGCLK_CCL                                     CCL input clock frequency                                  100      MHz
fGCLK_GCLKIN                                  External GCLK input clock frequency                        50       MHz
fGCLK_CM4_TRACE                               CM4 Trace input clock frequency                            120      MHz
fGCLK_AC                                      AC digital input clock frequency                           100      MHz
fGCLK_ADCx, x = {0, 1}                        ADCx input clock frequency                                 100      MHz
fGCLK_DAC                                     DAC input clock frequency                                  100      MHz

            Note:
             1. These values are based on simulation. They are not covered by production test limits or
                  characterization.



54.7        Power Consumption
            The values in this section are measured values of power consumption under the following conditions,
            except where noted:
             • Operating Conditions
                 – CPU is running on Flash with automatic wait state
                 – Low-power cache enabled.
                 – BOD33 is disabled
                 – I/Os are inactive input mode with input trigger disabled
             • Oscillators
                 – XOSC0 (crystal oscillator) running with external 32 MHz crystal
                 – XOSC32K (32 kHz crystal oscillator) running with external 32 kHz crystal in LP mode
                 – FDPLL is using XOSC32K as reference
                 – DFLL is using XOSC32K as reference




           © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1990
                                                            SAM D5x/E5x Family Data Sheet
                                                                         Electrical Characteristics at 85°C

Table 54-9. Active Current Consumption - Active Mode

 Mode        Conditions         Regulator        Clock        VDD              TA               Typ Max.      Units
                                                              1.8V                              136   162
                                             FDPLL 120 MHz
                                                              3.3V                              137   164
                                                              1.8V                              136   199
                                    LDO       DFLL 48 MHz
                                                              3.3V                              136   199
                                                              1.8V                              146   243
                                             XOSC 32 MHz
                                                              3.3V                              149   245
 Active    COREMARK(1)
                                                              1.8V                              103   127
                                             FDPLL 120 MHz
                                                              3.3V                              65    89
                                                              1.8V                              102   152
                                   BUCK       DFLL 48 MHz
                                                              3.3V                              63    115
                                                              1.8V                              110   205
                                             XOSC 32 MHz
                                                              3.3V                              73    153
                                                                     Max. at 85°C Typ at 25°C               µA/MHz
                                                              1.8V                              21    46
                                             FDPLL 120 MHz
                                                              3.3V                              23    48
                                                              1.8V                              21    84
                                    LDO       DFLL 48 MHz
                                                              3.3V                              21    84
                                                              1.8V                              25    115
                                             XOSC 32 MHz
                                                              3.3V                              27    117
  Idle            N/A
                                                              1.8V                              16    35
                                             FDPLL 120 MHz
                                                              3.3V                              11    28
                                                              1.8V                              16    63
                                   BUCK       DFLL 48 MHz
                                                              3.3V                              10    46
                                                              1.8V                              21    90
                                             XOSC 32 MHz
                                                              3.3V                              19    71

          Note: System Configuration used:
           • MCLK all APB clocks masked except MCLK and NVMCTRL
           • MCLK.AHBMASK = 0x00C00FFF
           • CMCC enabled




          © 2019 Microchip Technology Inc.                   Datasheet                     DS60001507E-page 1991
                                                       SAM D5x/E5x Family Data Sheet
                                                                     Electrical Characteristics at 85°C

Table 54-10. Standby Mode Current Consumption

                                                                     Regulator
 Mode                                 Conditions                               VDD(1)    TA      Typ. Max. Units
                                                                       Mode
                                                                                1.8V             43     870
             Fast wake-up disabled (PM.STDBYCFG.FASTWKUP =             LDO
              0x0), no peripheral running No System RAM retained                3.3V             43     869
             (PM.STDBYCFG.RAMCFG = 0x2). 8 KB backup RAM                        1.8V             26     570
                                     retained                         BUCK
                                                                                3.3V             17     440
                                                                                1.8V             85     1388
             Fast wake-up enabled (PM.STDBYCFG.FASTWKUP =              LDO
              0x3), no peripheral running No System RAM retained                3.3V             85     1392
             (PM.STDBYCFG.RAMCFG = 0x2). 8 KB backup RAM                        1.8V             65     1047
                                     retained                         BUCK              Max at
                                                                                3.3V    85°C     47     738
Standby                                                                                                         µA
                                                                                1.8V    Typ at   43     870
            Fast wake-up disabled (PM.STDBYCFG.FASTWKUP =              LDO              25°C
           0x0), RTC running on XOSC32K No System RAM retained                  3.3V             44     870
             (PM.STDBYCFG.RAMCFG = 0x2). 8 KB backup RAM                        1.8V             26     571
                                  retained                            BUCK
                                                                                3.3V             18     443
                                                                                1.8V             45     912
             Fast wake-up disabled (PM.STDBYCFG.FASTWKUP =             LDO
              0x0), RTC running on XOSC32K 32 KB System RAM                     3.3V             46     911
            retained (PM.STDBYCFG.RAMCFG = 0x1). 8 KB backup                    1.8V             27     598
                                 RAM retained                         BUCK
                                                                                3.3V             19     462
                                                                                1.8V             53     1068
             Fast wake-up disabled (PM.STDBYCFG.FASTWKUP =             LDO
           0x0), RTC running on XOSC32K Full System RAM retained                3.3V             53     1067
             (PM.STDBYCFG.RAMCFG = 0x0). 8 KB backup RAM                        1.8V             32     702
                                   retained                           BUCK
                                                                                3.3V             22     537
                                                                                1.8V             101 1716
                                                                       LDO              Max at
           Fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),                     3.3 V   85°C     101 1722
Standby                                                                                                         µA
                no peripheral running Full System RAM retained.                 1.8V    Typ at   78     1298
                                                                      BUCK              25°C
                                                                                3.3V             55     911
                                                                                1.8V             102 1724
                                                                       LDO
           Fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),                     3.3V             103 1732
             RTC running on XOSC32K Full System RAM retained.                   1.8V             79     1305
                                                                      BUCK
                                                                                3.3V             56     915

          Note:
           1. VDD is defined as the common voltage applied to VDDIO and VDDANA. Refer to Acronyms and
                Abbreviations for additional information on terminology.




        © 2019 Microchip Technology Inc.                 Datasheet                      DS60001507E-page 1992
                                                      SAM D5x/E5x Family Data Sheet
                                                                    Electrical Characteristics at 85°C

Table 54-11. Hibernate Mode Current Consumption

                                                                  Regulator
  Mode                                Conditions                            VDD(1)     TA       Typ. Max. Units
                                                                    Mode
                                                                              1.8V               6    47
                                                                    LDO
               No peripheral running No System RAM retained                   3.3V               6    48
            (PM.HIBCFG.RAMCFG = 0x2) No backup RAM retained
                      (PM.HIBCFG.BRAMCFG = 0x2)                               1.8V               3    29
                                                                    BUCK
                                                                              3.3V               3    29
                                                                              1.8V               6    48
                                                                    LDO
             RTC is running on XOSC32K No System RAM retained                 3.3V               7    49
            (PM.HIBCFG.RAMCFG = 0x2) No backup RAM retained
                        (PM.HIBCFG.BRAMCFG = 0x2)                             1.8V               3    30
                                                                    BUCK
                                                                              3.3V               3    30
                                                                              1.8V               7    55
                                                                    LDO
             RTC is running on XOSC32K No System RAM retained                 3.3V               8    56
               (PM.HIBCFG.RAMCFG = 0x2) 4 KB backup RAM
                   retained (PM.HIBCFG.BRAMCFG = 0x1)                         1.8V               3    35
                                                                    BUCK
                                                                              3.3V    Max. at    4    33
Hibernate                                                                            85°C Typ                  µA
                                                                              1.8V    at 25°C    7    61
                                                                    LDO
             RTC is running on XOSC32K No System RAM retained                 3.3V               8    63
               (PM.HIBCFG.RAMCFG = 0x2) 8 KB backup RAM
                   retained (PM.HIBCFG.BRAMCFG = 0x0)                         1.8V               4    39
                                                                    BUCK
                                                                              3.3V               4    31
                                                                              1.8V               9    100
                                                                    LDO
                RTC is running on XOSC32K 32 KB System RAM                    3.3V              10    101
              retained (PM.HIBCFG.RAMCFG = 0x1) 8 KB backup
                 RAM retained (PM.HIBCFG.BRAMCFG = 0x0)                       1.8V               5    65
                                                                    BUCK
                                                                              3.3V               4    48
                                                                              1.8V              16    255
                                                                    LDO
             RTC is running on XOSC32K Full System RAM retained               3.3V              17    255
               (PM.HIBCFG.RAMCFG = 0x0) 8 KB backup RAM
                    retained (PM.HIBCFG.BRAMCFG = 0x0)                        1.8V               9    166
                                                                    BUCK
                                                                              3.3V               7    121

         Note:
          1. VDD is defined as the common voltage applied to VDDIO and VDDANA Refer to Acronyms and
               Abbreviations for additional information on terminology.




         © 2019 Microchip Technology Inc.               Datasheet                      DS60001507E-page 1993
                                                           SAM D5x/E5x Family Data Sheet
                                                                         Electrical Characteristics at 85°C

Table 54-12. Backup and Off Mode Current Consumption

 Mode                                       Conditions                        VDD(1)       TA          Typ. Max. Units
              Powered by VDDIO, no RTC running VDDIO+VDDANA     1.8V                                    2.1   41.7
         consumption No backup RAM retained (PM.BKUPCFG.BRAMCFG
                                   = 0x2)                       3.3V                                    2.5   42.5

               Powered by VDDIO with RTC running on XOSC32K VDDIO              1.8V                     2.7   42.6
                  +VDDANA consumption No backup RAM retained
                          (PM.BKUPCFG.BRAMCFG = 0x2)                           3.3V                     3.3   43.6

                 Powered by VDDIO, no RTC running VDDIO+VDDANA                 1.8V    Max. at 85°C     2.4   48.4
Backup                 consumption 4 KB backup RAM retained                                                             µA
                                                                                       Typ at 25°C
                          (PM.BKUPCFG.BRAMCFG = 0x1)                           3.3V                     2.8   49.1

                 Powered by VDDIO, no RTC running VDDIO+VDDANA                 1.8V                     2.7   55.1
                       consumption 8 KB backup RAM retained
                          (PM.BKUPCFG.BRAMCFG = 0x0)                           3.3V                     3.1   55.8

               Battery backup mode powered by VBAT with RTC running on         1.8V                     2.7   42.6
                                      XOSC32K                                  3.3V                     3.3   43.6
                                                                               1.8V    Max at 85°C     0.191 2.30
 OFF                                            -                                                                       µA
                                                                               3.3V    Typ at 25°C     0.331 3.35

         Note:
          1. VDD is defined as the common voltage applied to VDDIO and VDDANA. Refer to Acronyms and
               Abbreviations for additional information on terminology.



54.8     Wake-Up Time
         Conditions:
           •    VDD = 3.3V
           •    LDO Regulation mode (default mode)
           •    CPU clock = DFLL48 in open loop (default configuration)
           •    NVM automatic wait state and cache enabled (default configuration)
         Measurement Methods
         For IDLE and STANDBY, the exit of mode is done through asynchronous EIC wake-up. The wake-up time
         is measured between the toggle of the EIC pin and the set of the IO pin done by the first executed
         instructions in EIC interrupt handler.
         For Backup and hibernate, the exit of mode is done through RTC wake-up. The wake-up time is
         measured between the toggle of the RTC pin (SUPC_BKOUT_RTCTGL) and the set of the IO done by
         the first executed instructions after reset.
         For OFF mode, the exit of mode is done through Reset pin, the time is measured between the rising edge
         of the RESETN signal and the set of the IO done by the first executed instructions after Reset.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1994
                                                               SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 85°C

         Table 54-13. Wake-Up Timing

          Sleep Mode Conditions                                                                                 Typ Unit
          IDLE                                                                                                  230 ns
          STANDBY          STDBYCFG.FASTWKUP = 0                                                                110 µs
                           STDBYCFG.FASTWKUP = 1 Fast Wakeup is enabled on NVM.                                 92       µs
                           STDBYCFG.FASTWKUP = 2 Fast Wakeup is enabled on the main voltage                     25       µs
                           regulator.
                           STDBYCFG.FASTWKUP = 3 Fast Wakeup is enabled on both NVM and                         5        µs
                           MAINVREG.
          Hibernate                                                                                             320 µs
          BACKUP                                                                                                350 µs
          OFF                                                                                                   210 µs



54.9     I/O Pin Characteristics
         The pins have two different speeds controlled by the Drive Strength bit located in the Pin Configuration
         register PORT (PORT.PINCFG.DRVSTR).
Table 54-14. I/O Pins Common Characteristics

Symbol Parameter                                           Conditions                        Min.     Typ.          Max.      Units
VIL       Input Low-Level Voltage                          VDD = 1.71V-3.6V                   -         -      0.3 × VDD       V
VIH       Input High-Level Voltage                         VDD = 1.71V-3.6V             0.7 × VDD       -            -
VOL       Output Low-Level Voltage                         VDD > 1.71V, IOL max               -     0.1 × VDD 0.2 × VDD
VOH       Output High-Level Voltage                        VDD > 1.71V, IOH max         0.8 × VDD 0.9 × VDD          -
RPULL     Pull-up - Pull-down Resistance                   -                                  20       40            60        kΩ
          Pull-down resistance on pads PA24 and            -                                  14       23            28
          PA25
ILEAK     Input Leakage Current                            Pull-up resistors disabled         -1     ±0.015          1         µA

Table 54-15. I/O Pins Maximum Output Current(2,3)

                                                                                  Backup and            Backup and
                                                           Backup Pins in                                                     Units
Symbol             Parameter                 Conditions                           Normal Pins           Normal Pins
                                                           Backup Mode
                                                                                  DRVSTR=0                  DRVSTR=1

             Maximum Output low-            VDD=1.71V-3V        0.005                   0.5                    3
   IOL
                 level current              VDD=3V-3.63V         0.01                    2                     8
                                                                                                                              mA
            Maximum Output high-            VDD=1.71V-3V        0.005                   0.5                    3
  IOH
                level current               VDD=3V-3.63V         0.01                    2                     8




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1995
                                                             SAM D5x/E5x Family Data Sheet
                                                                             Electrical Characteristics at 85°C

Table 54-16. I/O Pins Dynamic Characteristics (see Notes 1, 2, and 3)

Symbol Parameter                   Conditions          Backup Pins in         Backup and                 Backup and         Units
                                                       Backup Mode            Normal Pins                Normal Pins
                                                                                DRVSTR=0                 DRVSTR=1
tRISE    Maximum Rise Time CLOAD = 30 pF                     4                      0.04                    0.01             µs
tFALL    Maximum Fall Time         CLOAD = 30 pF             4                      0.04                    0.01

         The pins with I2C alternative mode available are compliant with I2C specification.
         All I2C pins support Standard mode (Sm), Fast mode (Fm), Fast plus mode (Fm+), and High speed mode
         (Hs). The available I2C pins are listed in the I/O Multiplexing section. When an I/O pin multiplexing value
         is set to an I2C function, internal pull-up/pull-down resistors are disabled.
         Note:
          1. These values are based on simulation. They are not covered by production test limits or
               characterization.
          2. The pins PA08, PA09, PA12, PA13, PA16, PA17, PA22, PA23, PD08, PD09 have faster fall-time in
               I2C Fast Plus mode (Fm+) and High Speed mode (HS). The fall-time can be in 1 ns range in Fm+
               mode and in 5 ns range in HS mode.
          3. The following pins are Backup pins and have different properties than normal pins: PA00, PA01,
               PB00, PB01, PB02, PB03, PC00, PC01.
          4. USB pads PA24, PA25 are compliant to the USB standard in USB mode.



54.10    Analog Characteristics

54.10.1 Voltage Regulator Characteristics

54.10.1.1 Buck Converter
         Table 54-17. Buck Converter Electrical Characteristics

         Symbol           Parameter                     Conditions              Min.       Typ.     Max.           Units
         PEFF             Power Efficiency              IOUT = 100µA            -          66       -              %
                                                        IOUT = 100mA            -          74       -              %

         Note: To obtain the best power efficiency with buck regulator, the following components references must
         be used: Lext = LQH3NPN100MJOL, Cout = GRM21BR71A475KA73.
         Table 54-18. External Components Requirements in Switching Mode(1)

         Symbol            Parameter                               Conditions                   Min. Typ. Max. Units
         CIN(2)            Input regulator capacitor                                            -    10      -         µF
                                                                   Ceramic dielectric X7R       -    100     -         nF
         COUT(3)           Output regulator capacitor                                           3.76 4.7     -         µF
                                                                   Ceramic dielectric X7R       -    100     -         nF
         ESR COUT          External Series Resistance of COUT      -                            -    -       0.5       Ω




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1996
                                                               SAM D5x/E5x Family Data Sheet
                                                                            Electrical Characteristics at 85°C

        ...........continued
         Symbol            Parameter                                Conditions              Min. Typ. Max. Units
         LEXT              External inductance                                              -              10     -         µH
         RSERIES_LEXT ESR of LEXT                                   -                       -              -      0.36      Ω
         ISAT_LEXT         Saturation current                       -                       500            -      -         mA

        Note:
         1. These values are based on simulation. They are not covered by production test limits or
              characterization.
         2. It is recommended to use ceramic X7R capacitor with low-series resistance. Refer to Power Supply
              Connections for a typical circuit connections.
         3. It is recommended to use ceramic or solid tantalum capacitor with low ESR.
54.10.1.2 LDO Regulator
        Table 54-19. Decoupling Requirements

         Symbol             Parameter                      Conditions       Min.     Typ.              Max.            Units
         CIN(1)             Input regulator capacitor      -                -        10                -               µF
                                                           Ceramic        -          100               -               nF
                                                           dielectric X7R
         COUT(2)            Output regulator capacitor     -                3.76     4.7               -               µF
                                                           Ceramic        -          100               -               nF
                                                           dielectric X7R
         ESR COUT           External Series Resistance of -                 -        -                 0.5             Ω
                            COUT

        Note:
         1. It is recommended to use ceramic X7R capacitor with low-series resistance. Refer to Power Supply
              Connections for a typical circuit connections.
         2. It is recommended to use ceramic or solid tantalum capacitor with low ESR.

54.10.2 Power-On Reset (POR) Characteristics
        Table 54-20. POR Characteristics

         Symbol          Parameters                                                Min.         Typ.            Max.       Unit
         VPOT+           Voltage threshold Level on VDDIO rising                   1.53         1.58            1.64       V
         VPOT-           Voltage threshold Level on VDDIO falling                  0.97         1.26            1.35       V




        © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1997
                                                           SAM D5x/E5x Family Data Sheet
                                                                       Electrical Characteristics at 85°C

        Figure 54-1. POR Operating Principle




                                           VDD
                                         VPOT+
                                         VPOT-



                                           Reset                                Time




        Note: The shaded area indicates that the device is in a Reset state.

54.10.3 Brown-Out Detectors (BOD) Characteristics
        Figure 54-3. BOD33 Hysteresis OFF

                                   VCC
                                                   VBOD



                                RESET

        Figure 54-4. BOD33 Hysteresis ON

                                   VCC                                  VBOD+
                                                   VBOD-



                                RESET




       © 2019 Microchip Technology Inc.                    Datasheet                   DS60001507E-page 1998
                                                   SAM D5x/E5x Family Data Sheet
                                                                  Electrical Characteristics at 85°C

Table 54-21. BOD33 Characteristics on VDD and VBAT Monitoring in Normal Mode (During Power-
up Phase and Active Mode)

 Symbol                   Parameters          Conditions (see       Min     Typ       Max       Unit
                                              Notes 3, 4)
 VBOD or VBOD- (1) BOD33 threshold            LEVEL[7:0] = 0x00    1.463   1.509     1.544       V
                   level Hysteresis           (min)
                   OFF or BOD33
                                              LEVEL[7:0] = 0x19    1.609   1.658     1.697
                   threshold level
                                              (recommended
                   Hysteresis ON
                                              value)
                                              LEVEL[7:0]= 0x1C     1.627   1.676     1.715
                                              (fuse value)
                                              LEVEL[7:0] = 0xFF    2.946   3.040     3.112
                                              (max)
 VBOD+ (2)                BOD33 threshold     LEVEL[7:0] = 0x00    1.473   1.520     1.555
                          level Hysteresis    (min)
                          ON at power
                                              LEVEL[7:0]= 0x19     1.618   1.669     1.707
                          voltage rising
                                              (recommended
                                              value)
                                              LEVEL[7:0] = 0x1C    1.636   1.687     1.725
                                              (fuse value)
                                              LEVEL[7:0] = 0xFF    2.953   3.041     3.116
                                              (max)
 Level_Step               DC threshold step           -              -      6.00       -         mV
 Tstart                   Startup time (6)    Time from enable       -       27        -         μs
                                                  to RDY

Note:
 1. VBOD = VBOD- = 1.5 + LEVEL[7:0) * Level_Step LEVEL[7:0] is calibration setting bus of threshold
      level.
 2. VBOD+ = VBOD- + N * HYST_STEP N = 0 to 15 according to HYST[3:0] value HYST_STEP =
      Level_Step.
 3. Hysteresis OFF mode, HYST[3:0] = 0x0.
 4. Hysteresis ON mode, HYST[3:0] = 0x1 to 0xf; Min/Typ/Max values given for 0x2.
 5. At the upper side of LEVEL[7:0] values depending on the Hysteresis value chosen with HYST[3:0],
      the VBOD+ level reaches an overflow, e.g., for HYST[3:0] = 0d2 the hysteresis is 2 x Level_Step =
      12 mV up to position 253 and position 254 to 255 above must not be used.
 6. These are based on design simulation. They are not covered by production test limits or
      characterization.




© 2019 Microchip Technology Inc.                     Datasheet                     DS60001507E-page 1999
                                                   SAM D5x/E5x Family Data Sheet
                                                                  Electrical Characteristics at 85°C

Table 54-22. BOD33 Characteristics on VDD and VBAT Monitoring in Low-Power Mode (During
Standby/Backup/Hibernate Modes)

 Symbol                   Parameters          Conditions (see       Min     Typ       Max       Unit
                                              Notes 3, 4)
 VBOD or VBOD- (1) BOD33 threshold            LEVEL[7:0] = 0x00    1.413   1.510     1.599       V
                   level Hysteresis           (min)
                   OFF or BOD33
                                              LEVEL[7:0]= 0x19     1.551   1.659     1.760
                   threshold level
                                              (recommended
                   Hysteresis ON
                                              value)
                                              LEVEL[7:0] = 0x1C    1.569   1.677     1.778
                                              (fuse value)
                                              LEVEL[7:0] = 0xFF    2.845   3.045     3.229
                                              (max)
 VBOD+ (2)                BOD33 threshold     LEVEL[7:0] = 0x00    1.426   1.522     1.611
                          level Hysteresis    (min)
                          ON at power
                                              LEVEL[7:0]= 0x19     1.564   1.672     1.773
                          voltage rising
                                              (recommended
                                              value)
                                              LEVEL[7:0] = 0x1C    1.582   1.690     1.791
                                              (fuse value)
                                              LEVEL[7:0] = 0xFF    2.848   3.045     3.230
                                              (max)
 Level_Step               DC threshold step           -              -      6.00       -         mV
 Tstart                   Startup time (6)    Time from enable       -       27        -         μs
                                                  to RDY

Note:
 1. VBOD = VBOD- = 1.5 + LEVEL[7:0) * Level_Step LEVEL[7:0] is calibration setting bus of threshold
      level.
 2. VBOD+ = VBOD- + N * HYST_STEP N = 0 to 15 according to HYST[3:0] value HYST_STEP =
      Level_Step.
 3. Hysteresis OFF mode, HYST[3:0] = 0x0.
 4. Hysteresis ON mode, HYST[3:0] = 0x1 to 0xf; Min/Typ/Max values given for 0x2.
 5. At the upper side of LEVEL[7:0] values depending on the Hysteresis value chosen with HYST[3:0],
      the VBOD+ level reaches an overflow, e.g., for HYST[3:0] = 0d2 the hysteresis is 2 x Level_Step =
      12 mV up to position 253 and position 254 to 255 above must not be used.
 6. These are based on design simulation. They are not covered by production test limits or
      characterization.




© 2019 Microchip Technology Inc.                     Datasheet                     DS60001507E-page 2000
                                                                          SAM D5x/E5x Family Data Sheet
                                                                                             Electrical Characteristics at 85°C

             Table 54-23. BOD33 Power Consumption

              Symbol CPU Mode                                              Conditions TA                               Typ.    Max     Units
              IDD           Active / Idle                                  VCC = 1.8V Max 85°C Typ 25°C 8.52                   12.07 µA
                                                                           VCC = 3.3V                                  10.10 14.28
                            Standby with BOD continuous normal VCC = 1.8V                                              4.71    6.34
                            mode
                                                               VCC = 3.3V                                              6.01    8.06
                            Standby with BOD continuous low                VCC = 1.8V                                  0.15    0.22
                            power mode or Hibernate mode
                                                                           VCC = 3.3V                                  0.21    0.30

54.10.4 Analog-to-Digital Converter (ADC) Characteristics
Table 54-24. Operating Conditions(1)
Symbol              Parameters                                     Conditions                           Min.    Typ.          Max.             Unit

Res                 Resolution                                                                          -       -             12               bits

FCNV                Sampling rate - Differential mode              resolution 12 bit (CTRLB.RESSEL=0)   10      -             1231             ksps
                    SAMPCTRL.OFFCOMP = 0
                                                                   resolution 10 bit (CTRLB.RESSEL=2)   14.55   -             1455
                    REFCTRL.REFCOMP = 0
                                                                   resolution 8 bit (CTRLB.RESSEL=3     17.78   -             1778

                    Sampling rate - Single-Ended mode              resolution 12 bit (CTRLB.RESSEL=0)   10      -             1231             ksps
                    SAMPCTRL.OFFCOMP = 0
                                                                   resolution 10 bit (CTRLB.RESSEL=2)   13.33   -             1333
                    REFCTRL.REFCOMP = 0
                                                                   resolution 8 bit (CTRLB.RESSEL=3     16      -             1600

Conversion          Differential mode Number of ADC clock cycles   resolution 12 bit (CTRLB.RESSEL=0)   16                                     cycles
delay               SAMPCTRL.OFFCOMP=1 and/or
                    REFCTRL.REFCOMP=1                              resolution 10 bit (CTRLB.RESSEL=2)   14

                                                                   resolution 8 bit (CTRLB.RESSEL=3)    12

                    Differential mode Number of ADC clock cycles   resolution 12 bit (CTRLB.RESSEL=0)   SAMPLEN+13                             cycles
                    SAMPCTRL.OFFCOMP=0 REFCTRL.REFCOMP=0
                    SAMPLEN corresponds to the decimal value of    resolution 10 bit (CTRLB.RESSEL=2)   SAMPLEN+11
                    SAMPCTRL.SAMPLEN[5:0] register
                                                                   resolution 8 bit (CTRLB.RESSEL=3)    SAMPLEN+9

                    Single-ended mode Number of ADC clock cycles   resolution 12 bit (CTRLB.RESSEL=0)   16                                     cycles
                    SAMPCTRL.OFFCOMP=1 and/or
                    REFCTRL.REFCOMP=1                              resolution 10 bit (CTRLB.RESSEL=2)   15

                                                                   resolution 8 bit (CTRLB.RESSEL=3)    13

                    Single-ended mode Number of ADC clock cycles   resolution 12 bit (CTRLB.RESSEL=0)   SAMPLEN+13                             cycles
                    SAMPCTRL.OFFCOMP=0 REFCTRL.REFCOMP=0
                    SAMPLEN corresponds to the decimal value of    resolution 10 bit (CTRLB.RESSEL=2)   SAMPLEN+12
                    SAMPCTRL.SAMPLEN[5:0] register
                                                                   resolution 8 bit (CTRLB.RESSEL=3)    SAMPLEN+10

FADC                ADC Clock frequency                                                                 160     Fcnv*Nb_cycles 16000           kHz




             © 2019 Microchip Technology Inc.                               Datasheet                                  DS60001507E-page 2001
                                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                  Electrical Characteristics at 85°C

...........continued
 Symbol                Parameters                                           Conditions                    Min.    Typ.          Max.                Unit

 TS                    Sampling time                                        SAMPCTRL.OFFCOMP=1                              4                       Cycles
                                                                            REFCTRL.REFCOMP=1 CTRLC.R2R
                                                                            =1

                                                                            SAMPCTRL.OFFCOMP=0(3)         1       -             65
                                                                            REFCTRL.REFCOMP=0
                                                                            CTRLC.R2R=0

                       Sampling time with DAC as input                      SAMPCTRL.OFFCOMP=1            (4)                                       ns
                                                                            REFCTRL.REFCOMP=1
                                                                            CTRLC.R2R=1

                                                                            SAMPCTRL.OFFCOMP=0 (3)
                                                                            REFCTRL.REFCOMP=0
                                                                            CTRLC.R2R=0

                       Sampling time with Temp Sensor or Bandgap as input   SAMPCTRL.OFFCOMP=1            10000   -             4/fadcmin = 25000
                                                                            REFCTRL.REFCOMP=1
                                                                            CTRLC.R2R=1

                                                                            SAMPCTRL.OFFCOMP=0 (3)        10000   -             65/fadcmin =
                                                                            REFCTRL.REFCOMP=0                                   406250
                                                                            CTRLC.R2R=0

 VCNV                  Conversion range                                     Differential mode             -VREF -               +VREF               V

                       Conversion range                                     Single-ended mode             0       -             VREF

 VREF                  Reference input                                      -                             1.0     -             VDDANA-0.4          V

 VIN                   Input channel range                                  -                             0       -             VDDANA              V

 VCMIN                 Input common mode voltage                            CTRLA.R2R=1                   0       -             VDDANA              V

                                                                            CTRLA.R2R=0                   See Note 2                                V

 CSAMPLE               Input sampling capacitance                                                         2       2.5           3                   pF

 RSAMPLE               Input sampling on-resistance                                                       -                     2000                Ω

 RREF                  Reference source resistance                                                                -             2.5                 kΩ


               Note:
                1. These values are based on simulation. They are not covered by production test limits or
                     characterization.
                2. Limit the input common mode voltage using the following equations (where, VCM_IN is the input
                     channel common mode voltage):
                     When CTRLA.R2R = 0:
                           – VCM_IN < 0.75*VREF
                           – VCM_IN > Maximum of (0, VREF-VDDANA-0.7, 1.25*VREF-VDDANA)
                 3.      When SAMPCTRL.OFFCOMP is disabled, Ts is a function of the SAMPLEN[5:0] register value.
                 4.      See TS specified in DAC Electrical Characteristics.




              © 2019 Microchip Technology Inc.                                        Datasheet                          DS60001507E-page 2002
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                   Electrical Characteristics at 85°C

          Figure 54-5. ADC Analog Input AINx




          The minimum sampling time tsamplehold for a given Rsource can be found using a general formula:

          �samplehold ≥ �sample + �source × �sample × � + 2 × ln 2
          For 12-bit accuracy, this turns into:

          �samplehold ≥ �sample + �source × �sample × 9.7
                                  1
          where �samplehold ≥           .
                              2 × �ADC

Table 54-25. Differential Mode (1)
                                                                                                                            Measurement
 Symbol                    Parameter                                       Conditions                                                            Unit
                                                                                                                    Min        Typ        Max

                                                                                   Vddana=3.0V Vref=Vddana          10.5       10.8       11.2
 ENOB                Effective Number of bits      Fadc = 1Msps - R2R disabled                                                                   bits
                                                                                   Vddana=3.0V ExtVref=2.0V         10.5       10.8       11.0

                                                                                   Vddana=3.0V Vref=Vddana            -       +/-2.3    +/-5.2
  TUE               Total Unadjusted Error (2)     Fadc = 1Msps - R2R disabled
                                                                                   Vddana=3.0V ExtVref=2.0V           -       +/-2.7    +/-5.6

                                                                                   Vddana=3.0V Vref=Vddana            -       +/-1.2    +/-1.5
  INL                 Integral Non Linearity       Fadc = 1Msps - R2R disabled                                                                   LSB
                                                                                   Vddana=3.0V ExtVref=2.0V           -       +/-1.2    +/-1.5

                                                                                   Vddana=3.0V Vref=Vddana            -       +/-0.98   -1/+1
  DNL               Differential Non Linearity     Fadc = 1Msps - R2R disabled
                                                                                   Vddana=3.0V ExtVref=2.0V           -       +/-0.95   -1/+1

                                                                                   Vddana=3.0V Vref=Vddana          -0.18      -0.02    +0.16

                                                                                   Vddana=3.0V ExtVref=2.0V         -0.09      +0.03    +0.18
              Gain Error with REFCTRL.REFCOMP=1           Fadc = 1Msps
                                                                                   Vddana=3.0V 1V internal Ref      -4.3        -1      +1.8

                                                                                   Vddana=3.0V Vref=Vddana/2        -0.35      +0.2     +0.65
  Gain                                                                                                                                            %
                                                                                   Vddana=3.0V Vref=Vddana          -0.2      -0.001    +0.16

                                                                                   Vddana=3.0V ExtVref=2.0V         -0.74      -0.05      0.66
              Gain Error with REFCTRL.REFCOMP=0           Fadc = 1Msps
                                                                                   Vddana=3.0V 1V internal Ref      -4.9        -1      +1.6

                                                                                   Vddana=3.0V Vref=Vddana/2         -1        +0.11      +1

                                                                                   Vddana=3.0V Vref=Vddana          -2.9       -0.3     +2.4

                                                                                   Vddana=3.0V ExtVref=2.0V         -2.6       -0.2     +2.1
            Offset Error with SAMPCTRL.OFFCOMP=1          Fadc = 1Msps
                                                                                   Vddana=3.0V 1V internal Ref      -2.3       -0.2     +2.3

                                                                                   Vddana=3.0V Vref=Vddana/2        -2.9       -0.3     +2.6
 Offset                                                                                                                                          mV
                                                                                   Vddana=3.0V Vref=Vddana          -9.5       +0.03    +9.9

                                                                                   Vddana=3.0V ExtVref=2.0V         -9.9       -0.03    +9.8
            Offset Error with SAMPCTRL.OFFCOMP=0          Fadc = 1Msps
                                                                                   Vddana=3.0V 1V internal Ref       -5        +0.5        -5

                                                                                   Vddana=3.0V Vref=Vddana/2        -10.8      +0.5     +11.3




          © 2019 Microchip Technology Inc.                         Datasheet                                     DS60001507E-page 2003
                                                                              SAM D5x/E5x Family Data Sheet
                                                                                                   Electrical Characteristics at 85°C

...........continued
                                                                                                                                            Measurement
 Symbol                            Parameter                                               Conditions                                                            Unit
                                                                                                                                     Min        Typ       Max

   SFDR                  Spurious Free Dynamic Range                                                                                76.6        79.6      83.5

  SINAD                Signal to Noise and Distortion ratio                                                                         65.3        67.2      68.9
                                                               Fs = 1Msps Fin = 14kHz (2)           Vddana=3.0V Vref=Vddana                                      dB
   SNR                        Signal to Noise ratio                                                                                 64.7        66.5      68.2

   THD                      Total Harmonic Distortion                                                                               -91.6      -82.9     -78.6

                                                                                                    Vddana=3.0V ExtVref=2.0V         0.2        0.4       2.4
   Nrms                            Noise RMS                      constant input voltage                                                                         mV
                                                                                                    Vddana=3.0V Vref=Vddana         0.15        0.25      2.5


               Note:
                1. These values are based on characterization. These values are not covered by test limits in
                     production.
                2. All values expressed in decibel refer to the full scale input and are tested with an input signal
                     0.35dB below full scale; THD measured on the first seven harmonics of the input signal.
Table 54-26. Single Ended Mode (1)
                                                                                                                                           Measurement
 Symbol                            Parameter                                               Conditions                                                            Unit
                                                                                                                                    Min        Typ      Max

                                                                                                   Vddana=3.0V Vref=Vddana          8.9       9.25        9.9
  ENOB                      Effective Number of bits          Fadc = 1Msps - R2R disabled                                                                        bits
                                                                                                   Vddana=3.0V ExtVref=2.0V         8.9        9.5        9.7

                                                                                                   Vddana=3.0V Vref=Vddana           -       +/-10.9   +/-18.3
   TUE                     Total Unadjusted Error (2)         Fadc = 1Msps - R2R disabled
                                                                                                   Vddana=3.0V ExtVref=2.0V          -        +/-9.7   +/-19.1

                                                                                                   Vddana=3.0V Vref=Vddana           -        +/-2.3   +/-3.2
    INL                      Integral Non Linearity           Fadc = 1Msps - R2R disabled                                                                        LSB
                                                                                                   Vddana=3.0V ExtVref=2.0V          -        +/-2.3     +/-3

                                                                                                   Vddana=3.0V Vref=Vddana           -       +/-0.98   -1/+1
   DNL                      Differential Non Linearity        Fadc = 1Msps - R2R disabled
                                                                                                   Vddana=3.0V ExtVref=2.0V          -       +/-0.97   -1/+1.1

                                                                                                   Vddana=3.0V Vref=Vddana          -0.3      -0.01     +0.3

                                                                                                   Vddana=3.0V ExtVref=2.0V         -0.2      +0.02    +0.25
   Gain            Gain Error with REFCTRL.REFCOMP=1                 Fadc = 1Msps                                                                                 %
                                                                                                   Vddana=3.0V 1V internal Ref      -4.2       -1.1     +1.8

                                                                                                   Vddana=3.0V Vref=Vddana/2        -0.4      +0.1      +0.6

                                                                                                   Vddana=3.0V Vref=Vddana          -18        -7.2       +7

                                                                                                   Vddana=3.0V ExtVref=2.0V        -18.6       -2.9      +13
   Offset         Offset Error with SAMPCTRL.OFFCOMP=1               Fadc = 1Msps                                                                                mV
                                                                                                   Vddana=3.0V 1V internal Ref      -24        -4.2      +19

                                                                                                   Vddana=3.0V Vref=Vddana/2        -22        -3.1      +24

   SFDR                  Spurious Free Dynamic Range                                                                               67.9       69.2      76.3

  SINAD                Signal to Noise and Distortion ratio                                                                        55.7       57.5      61.1
                                                              Fs = 1Msps Fin = 14kHz (2)           Vddana=3.0V Vref=Vddana                                       dB
   SNR                        Signal to Noise ratio                                                                                54.7       56.9      60.6

   THD                     Total Harmonic Distortion                                                                               -73.7      -68.2    -65.8

                                                                                                   Vddana=3.0V ExtVref=2.0V        0.35        1.0        2.1
   Nrms                            Noise RMS                     constant input voltage                                                                          mV
                                                                                                   Vddana=3.0V Vref=Vddana          0.3       0.35        1.7




              © 2019 Microchip Technology Inc.                                  Datasheet                                        DS60001507E-page 2004
                                                                          SAM D5x/E5x Family Data Sheet
                                                                                              Electrical Characteristics at 85°C

          Note:
           1. These values are based on characterization. These values are not covered by test limits in
                production.
           2. All values expressed in decibel refer to the full scale input and are tested with an input signal
                0.35dB below full scale; THD measured on the first seven harmonics of the input signal.
Table 54-27. Power Consumption
Symbol       Parameters         Conditions                                                                           Ta                Typ. Max Units

IDD VDDANA Differential mode    fs = 1 Msps / Reference buffer disabled / BIASREFBUF = '111', BIASREFCOMP = '111'    Max 85°C Typ 25°C 279   318   µA
                                VDDANA = VREF = 3.0V

                                fs = 1 Msps / Reference buffer enabled / BIASREFBUF = '111', BIASREFCOMP = '111'                       482   653
                                VDDANA = VREF = 3.0V

                                fs = 10 ksps / Reference buffer disabled / BIASREFBUF = '111', BIASREFCOMP = '111'                     28    45
                                VDDANA = VREF = 3.0V

                                fs = 10 ksps / Reference buffer enabled / BIASREFBUF = '111', BIASREFCOMP = '111'                      241   397
                                VDDANA = VREF = 3.0V

             Single Ended mode fs = 1 Msps / Reference buffer disabled / BIASREFBUF = '111', BIASREFCOMP = '111'     Max 85°C Typ 25°C 307   348   µA
                               VDDANA = VREF = 3.0V

                                fs = 1 Msps / Reference buffer enabled / BIASREFBUF = '111', BIASREFCOMP = '111'                       499   681
                                VDDANA = VREF = 3.0V

                                fs = 10 ksps / Reference buffer disabled / BIASREFBUF = '111', BIASREFCOMP = '111'                     38    60
                                VDDANA = VREF = 3.0V

                                fs = 10 ksps / Reference buffer enabled / BIASREFBUF = '111', BIASREFCOMP = '111'                      245   400
                                VDDANA = VREF = 3.0V


54.10.5 Digital to Analog Converter (DAC) Characteristics
Table 54-28. Operating Conditions (1)
Symbol       Parameters                           Conditions                                                  Min.         Typ.      Max.          Unit

Res          Resolution                           -                                                             -           -         12           bits

clk          Internal DAC Clock frequency -                                                                     -           -         12           MHz

fs_dac       Sampling frequency                   clk/12, CCTRL=0x0 (Low Power)                                 -           -         10           ksps

                                                  clk/12, CCTRL=0x2 (High Power)                                -           -          1           Msps

VOUTmin      Min. Output Voltage                  -                                                             -           -        0.15           V

VOUTmax Max. Output Voltage                       -                                                     VDDANA-0.15         -          -

VREF         External Reference input             CTRLB.REFSEL[1:0]=0x2 (VREFAB)                                1           -     VDDANA-0.15       V

                                                  CTRLB.REFSEL[1:0]=0x0 (VREFAU)                                1           -      VDDANA

CVREF        External decoupling capacitor -                                                                    -          220         -            nF

CLOAD        Output capacitor load                -                                                             -           -         50            pF

RLOAD        Output resistance load               -                                                             5           -          -           kΩ

ts           Settling time                        For reaching ±1LSB of the final value.                        -           -          1            µs
                                                  Step size < 500 LSB - Cload = 50pF

ts_FS        Settling time 0x080 to 0xF7F         For reaching ±1LSB of the final value.                        -           5          7            µs
                                                  Step size from 0% to 100% - Cload = 50pF




         © 2019 Microchip Technology Inc.                                   Datasheet                                     DS60001507E-page 2005
                                                          SAM D5x/E5x Family Data Sheet
                                                                         Electrical Characteristics at 85°C

         Note:
          1. These values are based on simulation. They are not covered by production test limits or
               characterization.
Table 54-29. Differential Mode (1)

Symbol Parameters                           Conditions                                        Min. Typ. Max.      Unit
INL       Integral Non Linearity,           i12clk = 12 MHz, VDDANA = 3.0V, External Ref. =     -   ±2.4 ±3.4     LSB
          Best-fit curve from 0x080 to      2.0V, CLOAD = 50 pF
          0xF7F
                                            i12clk = 12 MHz, VDDANA = 3.0V, Internal Ref,       -   ±3.2 ±4.2
                                            CLOAD = 50 pF
DNL       Differential Non Linearity,       i12clk = 12 MHz, VDDANA = 3.0V, External Ref. =     -   ±2.4 ±3.6     LSB
          Best-fit curve from 0x080 to      2.0V, CLOAD = 50 pF
          0xF7F
                                            i12clk = 12 MHz, VDDANA = 3.0V, Internal Ref,       -   ±3.5 ±5.4
                                            CLOAD = 50 pF
Gerr      Gain Error                        External Reference voltage                          -   ±0.4 ±1.7 % FSR
                                            1.0V Internal Reference voltage                     -   ±0.8 ±7.0
Offerr    Offset Error                      External Reference voltage                          -   ±13    ±40        mV
                                            1.0V Internal Reference voltage                     -    ±8    ±64
ENOB      Effective Number Of Bits          Fs = 1 Ms/s - External Ref - CCTRL = 0x2          9.9   10.7 10.9         Bits
SNR       Signal to Noise ratio                                                               63.5 68.6 72.6          dB
THD       Total Harmonic Distortion                                                           -79.1 -72.5 -61.0       dB

         Note:
          1. These values are based on characterization. These values are not covered by test limits in
               production.
Table 54-30. Single-Ended Mode (1)

Symbol Parameters                           Conditions                                        Min. Typ. Max.      Unit
INL       Integral Non Linearity,           i12clk = 12 MHz, VDDANA = 3.0V External Ref. =      -   ±2.7 ±4.0     LSB
          Best-fit curve from 0x080 to      2.0V, CLOAD = 50 pF
          0xF7F
                                            i12clk = 12 MHz VDDANA = 3.0V, Internal Ref,        -   ±5.2   8.2
                                            CLOAD = 50 pF
DNL       Differential Non Linearity,       i12clk = 12 MHz, VDDANA = 3.0V External Ref =       -   ±3.5 ±6.1     LSB
          Best-fit curve from 0x080 to      2.0V, CLOAD = 50 pF
          0xF7F
                                            i12clk = 12 MHz VDDANA = 3.0V, Internal Ref,        -   ±6.4 ±9.4
                                            CLOAD = 50 pF
Gerr      Gain Error                        External Reference voltage                          -   ±0.3 ±1.5 % FSR
                                            1.0V Internal Reference voltage                     -   ±0.8 ±6.9




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 2006
                                                              SAM D5x/E5x Family Data Sheet
                                                                          Electrical Characteristics at 85°C

...........continued
Symbol Parameters                            Conditions                                             Min. Typ. Max.               Unit
Offerr     Offset Error                      External Reference voltage                               -        ±7     ±21        mV
                                             1.0V Internal Reference voltage                          -        ±2     ±16
ENOB       Effective Number of Bits          Fs = 1 Ms/s - External Ref - CCTRL = 0x2               9.1        10.3 10.7         Bits
SNR        Signal to Noise Ratio                                                                    63.5 68.6 72.6               dB
THD        Total Harmonic Distortion                                                                -79.1 -72.8 -61.0            dB

          Note:
           1. These values are based on characterization. These values are not covered by test limits in
                production.
Table 54-31. Power Consumption

Symbol Parameters                                Conditions                              Ta               Min. Typ. Max. Unit
IDDANA     Differential Mode, DC supply          fs = 1 Msps, CCTR L= 0x2, VREF >        Max. 85°C         -        384   540     µA
           current, 2 output channels -          2.4V, VCC = 3.3V                        Typ. 25°C
           without load
                                                 fs = 10 ksps, CCTRL = 0x0, VREF <                         -        283   411
                                                 2.4V, VCC = 3.3V
           Single-Ended Mode, DC supply          fs = 1 Msps, CCTRL = 0x2, VREF >                          -        306   443     µA
           current, 2 output channels -          2.4V, VCC = 3.3V
           without load
                                                 fs = 10 ksps, CCTRL = 0x0, VREF <                         -        230   332
                                                 2.4V, VCC = 3.3V

54.10.6 Analog Comparator (AC) Characteristics
          Table 54-32. Analog Comparator Characteristics

           Symbol      Parameters                   Conditions                       Min Typ Max                          Unit
           PNIVR(1) Positive and Negative input                                      0        -      VDDANA               V
                    range voltage
           ICMR(1)     Input common mode range                                       0        -      VDDANA-0.2 V
           Off(2)      Offset                       High speed                       -18 ±3          18                   mV
                                                    COMPCTRLn.SPEED = 0x3
           Tpd         Propagation Delay            High speed                       -        24.1 39                     ns
                       Vcm=Vddana/2, Vin =          COMPCTRLn.SPEED = 0x3
                       +/-100mV overdrive from
                       Vcm
           Tstart      Startup time                 High speed                       -        4.7    7.5                  µs
                                                    COMPCTRLn.SPEED = 0x3




          © 2019 Microchip Technology Inc.                    Datasheet                             DS60001507E-page 2007
                                                        SAM D5x/E5x Family Data Sheet
                                                                        Electrical Characteristics at 85°C

         Note:
          1. These values are based on simulation. They are not covered by production test limits or
               characterization.
          2. Hysteresis disabled.
Table 54-33. Power Consumption

Symbol Parameters                                 Conditions                                  Ta           Typ. Max. Unit
IDDANA    Current consumption for                 COMPCTRLn.SPEED=0x3,                        Max.85°C 59           93   µA
          One AC enabled,                         VDDANA=3.3V                                 Typ.25°C
          Hysteresis disabled
          voltage scaler disabled
          Current consumption Voltage Scaler only VDDANA=3.3V                                              11       21

54.10.7 Voltage References
Table 54-34. Reference Voltage Characteristics

Symbol           Parameter                                   Conditions                Min.        Typ.         Max. Units
ADC/DAC          ADC/DAC internal reference                  nom. 1.0V,           0.954 1.0                     1.044 V
Ref              ADC.REFCTRL.REFSEL = INTREF                 VDDANA=3.3V, T= 25°C
                 DAC.CTRLB.REFSEL = INTREF
                                                             nom. 1.1V,           1.060 1.1                     1.139
                 AC.COMPCTRLn.MUXNEG = BANDGAP
                                                             VDDANA=3.3V, T= 25°C
                                                             nom. 1.2V,           1.150 1.2                     1.248
                                                             VDDANA=3.3V, T= 25°C
                                                             nom. 1.25V,          1.207 1.3                     1.291
                                                             VDDANA=3.3V, T= 25°C
                                                             nom. 2.0V,           1.893 2.0                     2.102
                                                             VDDANA=3.3V, T= 25°C
                                                             nom. 2.2V,           2.092 2.2                     2.303
                                                             VDDANA=3.3V, T= 25°C
                                                             nom. 2.4V,           2.282 2.4                     2.513
                                                             VDDANA=3.3V, T= 25°C
                                                             nom. 2.5V,           2.380 2.5                     2.615
                                                             VDDANA=3.3V, T= 25°C
                 Ref Temperature coefficient                 drift over [-40, +25]°C   -           -0.01/+0.03 -         %/°C
                                                             drift over [+25, +85]°C   -           -0.02/+0.02 -
                 Ref Supply coefficient                      drift over [1.71, 3.6]V   -           -0.2/+0.7    -        %/V
AC Ref           AC Internal Bandgap Reference               nom.1.1V, VDDANA =        1.074 1.1                1.125
                                                             3.3V, T = 25°C




         © 2019 Microchip Technology Inc.                 Datasheet                            DS60001507E-page 2008
                                                       SAM D5x/E5x Family Data Sheet
                                                                     Electrical Characteristics at 85°C


54.11   PTC Characteristics
        Table 54-35. Sensor Load Capacitance
             Symbol                    Mode           PTC channel          Max Sensor Load (1)          Units

                                                          Y0

                                                          Y1

                                                          Y2

                                                          Y3

                                                          Y4

                                                          Y5

                                                          Y6

                                                          Y7
                                                                                   54
                                                          Y8

                                                          Y9

                                                         Y10

                                                         Y11

                                                         Y12

                                                         Y13

                                                         Y14

                                                         Y15
                                  Self-capacitance
              Cload                                      Y16                       51                    pF

                                                         Y17

                                                         Y18
                                                                                   54
                                                         Y19

                                                         Y20

                                                         Y21                       51

                                                         Y22

                                                         Y23

                                                         Y24

                                                         Y25

                                                         Y26
                                                                                   54
                                                         Y27

                                                         Y28

                                                         Y29

                                                         Y30

                                                         Y31

                                 Mutual-capacitance       All                      31


        Note:
         1. Capacitance load that the PTC circuitry can compensate for each channel.




        © 2019 Microchip Technology Inc.                 Datasheet                         DS60001507E-page 2009
                                                 SAM D5x/E5x Family Data Sheet
                                                              Electrical Characteristics at 85°C

Table 54-36. Analog Gain Settings (1) (2)

               Symbol                          Setting                          Average
                                               GAIN_1                               1
                                               GAIN_2                               2.0
                                               GAIN_4                               4.2
                 Gain
                                               GAIN_8                               9.1
                                              GAIN_16                             15.4
                                              GAIN_32                                -

Note:
 1. Analog Gain is a parameter of the QTouch Library. Refer to the “QTouch Library Peripheral Touch
      Controller User Guide” for additional information.
 2. The GAIN_16 and GAIN_32 settings are not recommended; otherwise, the PTC measurements
      might become unstable.
The values in the following Power Consumption table are measured values of power consumption under
the following conditions:
Operating Conditions:
VDD = 3.0V
Clocks:
DFLL48M used as main clock source, running undivided at 48 MHz
CPU is running on flash with 2 wait states, at 48 MHz
PTC running at 4 MHz
PTC Configuration
Mutual-Capacitance mode
One touch channel
System Configuration
Standby Sleep mode enabled
RTC running on ULP32K: used to define the PTC scan rate, through the event system
RTC interrupts (wake up) the CPU to perform PTC scans




© 2019 Microchip Technology Inc.                  Datasheet                      DS60001507E-page 2010
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    Electrical Characteristics at 85°C

        Table 54-37. Power Consumption (1)

                                                   PTC scan
         Symbol           Parameters                              Oversamples                    Ta              Typ. Max Units
                                                  rate (msec)
                                                                           4                                     137 1164
                                                      10
                                                                           16                                    146 1179
                                                                           4                                         77    1094
                                                      50
                                                                           16                                        79    1100
            IDD     Current Consumption                                                 Max 85°C Typ 25°C                            µA
                                                                           4                                         68    1086
                                                     100
                                                                           16                                        69    1089
                                                                           4                                         64    1085
                                                     200
                                                                           16                                        65    1087

        Note:
         1. These values are based on characterization.



54.12   NVM Characteristics
Table 54-38. NVM Flash Read Wait States for Worst Case Conditions (EFP part numbers)

  CPU Fmax (Mhz)            0 WS           1 WS          2 WS          3 WS             4 WS          5 WS             6 WS          Auto WS
  Read Operations         1 Cycle      2 Cycles       3 Cycles      4 Cycles        5 Cycles       6 Cycles          7 Cycles        n Cycles
     VDD>1.71V               19             38            57            76               95            100                120             120

        Table 54-39. NVM Flash Read Wait States for Worst Case Conditions (non-EFP part numbers)

           CPU Fmax(MHz)             0 WS          1 WS          2 WS            3 WS           4 WS          5 WS          Auto WS
           Read Operations          1 Cycle       2 Cycles      3 Cycles        4 Cycles      5 Cycles       6 Cycles       N Cycles
                VDD > 2.7V             24           51            77              101           119            120          120
               VDD > 1.71V             22           44            67              89            111            120          120

        Maximum operating frequencies are given in the table above in MHz, but are limited by the Embedded
        Flash access time when the processor is fetching code out of it. Theses tables provide the device
        maximum operating frequency defined by the field RWS of the NVMCTRL CTRLA register when
        automatic wait states (AUTOWS) is disabled. This field defines the number of Wait states required to
        access the Embedded Flash Memory.
        Table 54-40. Flash Timing Characteristics

         Symbol           Parameter                             Conditions               Min.     Typ.        Max.              Units
         tFPW             Program Cycle Time                    Write Page                        1.5         3(1)              ms
         tCE                                                    Chip Erase                        6.4         25 (1)            s
         tFEB                                                   Erase Block                       50          200 (1)           ms




        © 2019 Microchip Technology Inc.                            Datasheet                                  DS60001507E-page 2011
                                                            SAM D5x/E5x Family Data Sheet
                                                                          Electrical Characteristics at 85°C

        Note:
         1. These are based on simulation. They are not covered by production test limits or characterization.
        Table 54-41. Flash Endurance and Data Retention

         Symbol              Parameter                             Conditions              Min.       Typ.      Units
         RetNVM10k           Retention after up to 10k             At TA = 85°C            20         -         Years
         CycNVM              Cycling Endurance(1)                  At TA = 85°C            10K        -         Cycles

        Note:
         1. An endurance cycle is a write-and-erase operation.
        Table 54-42. Flash Erase and Programming Current(1)

         Symbol       Parameter                                                                   Typ.       Max.   Units
         IFAP         Active Current current during whole programming operation                   8                 mA
         IFAE         Active Current current during Erase operation                               8                 mA

        Note:
         1. These values are based on simulation. They are not covered by production test limits or
              characterization.



54.13   Oscillators Characteristics

54.13.1 Crystal Oscillator (XOSC) Characteristics

        Digital Clock Characteristics
        The following table describes the characteristics for the oscillator when a digital clock is applied on XIN.
        Table 54-43. Digital Clock Characteristics

         Symbol                             Parameter                        Min.      Typ.           Max.      Units
         FXIN                               XIN clock frequency              -         -              48        MHz
         DCXIN (see Note 1)                 XIN clock duty cycle             40                       60        %

        Note:
         1. These values are based on simulation. They are not covered by production test limits or
              characterization.

        Chrystal Oscillator Characteristics
        The following Table describes the characteristics for the oscillator when a crystal is connected between
        XIN and XOUT.




        © 2019 Microchip Technology Inc.                     Datasheet                                DS60001507E-page 2012
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                            Electrical Characteristics at 85°C

         Figure 54-6. Oscillator Connection
                                                                                        DEVICE


                                                                                 XIN
                                                             Crystal
                                                                        CLEXT
                                                       LM


                                                        RM     CSHUNT
                                                        CM


                                                                                 XOUT

                                                                        CLEXT


         The user must choose a crystal oscillator where the crystal load capacitance CL is within the range given
         in the Table. The exact value of CL can be found in the crystal datasheet. The capacitance of the external
         capacitors (CLEXT) can then be computed as follows:
         CLEXT = 2 * (CL - CPARA - CPCB - CSHUNT)
         Where:
          • CPARA is the internal load capacitor parasitic between XIN and XOUT and can be computed as
            following:
            Equation 54-1.
                       ���� * �����
            ����� =
                       ���� + �����
           • CPCB is the capacitance of the PCB
           • CSHUNT is the shunt capacitance of the crystal as specified by the crystal manufacturer
Table 54-44. Multi-Crystal Oscillator Electrical Characteristics
Symbol   Parameter                                     Conditions                                                Min.   Typ.   Max.    Units

FOUT     Crystal oscillator frequency                                                                             8       -     48     MHz

CL       Crystal Load                                  F = 8 MHz                                                  -       -     20      pF

                                                       F = 16 MHz                                                 -       -     20

                                                       F = 32 MHz                                                 -       -     13

                                                       F = 48 MHz                                                 -       -     13

ESR      Crystal Equivalent Series Resistance - SF=3   F = 8 MHz, CL=20 pF - IMULT = 0x3                          -       -    181      Ω

                                                       F = 16 MHz, CL = 20 pF - IMULT = 0x4                       -       -    180

                                                       F= 24 MHz, CL = 20 pF - IMULT = 0x5                        -       -     70

                                                       F = 48 MHz, CL = 13 pF - IMULT = 0x6                       -       -     70

CXIN     Parasitic load capacitor                                                       -                         -      6.3    -       pF

CXOUT                                                                                   -                         -      5.9    -

DL       Drive Level (1)                               ENALC = ON                                                 -       -    100     μW

TSTART Startup time                                    F = 8 MHz, CL = 20 pF, CSHUNT = 2 pF - IMULT = 0x3         -     39700 72200 Cycles

                                                       F = 16 MHz, CL = 20 pF, CSHUNT = 1.5 pF - IMULT = 0x4      -     37550 62000

                                                       F = 24 MHz, CL = 20 pF, CSHUNT = 2.5 pF - IMULT = 0x5      -     32700 68500

                                                       F = 48 MHz, CL = 13 pF, CSHUNT = 5 pF - IMULT = 0x6        -     18400 38500




         © 2019 Microchip Technology Inc.                                   Datasheet                          DS60001507E-page 2013
                                                            SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 85°C

        Note:
         1. To ensure that the crystal is not overdriven, the automatic loop control is recommended to be
              turned ON (ENALC = 1).
        Table 54-45. Power Consumption

         Symbol Parameters                 Conditions                          Ta                 Typ. Max. Units
         IDD        Current                F = 8 MHz - CL = 20 pF - IMULT =    Max. 85°C, Typ. 0.43 1.02         mA
                    Consumption            0x3, ENALC = OFF                    25°C
                                           ENALC = ON                                             0.16 0.66
                                           F = 16 MHz - CL = 20 pF - IMULT =                      1.31 2.39
                                           0x5, ENALC = OFF
                                           ENALC = ON                                             0.25 0.81
                                           F = 32 MHz - CL = 13 pF - IMULT =                      2.92 4.75
                                           0x5, ENALC = OFF
                                           ENALC = ON                                             0.40 1.09
                                           F = 48 MHz - CL = 13 pF - IMULT =                      2.70 4.79
                                           0x6, ENALC = OFF
                                           ENALC = ON                                             0.76 1.46

54.13.2 External 32 kHz Crystal Oscillator (XOSC32K) Characteristics

        Digital Clock Characteristics
        The following table describes the characteristics for the oscillator when a digital clock is applied on XIN32
        pin.
        Table 54-46. Digital Clock Characteristics(1)

         Symbol             Parameter                               Min.       Typ.           Max.       Units
         fCPXIN32           XIN32 clock frequency                              32.768                    kHz
         DCXIN              XIN32 clock duty cycle                             50                        %

        Note: 1.These values are based on simulation. They are not covered by production test limits or
        characterization.

        Crystal Oscillator Characteristics
        The following section describes the characteristics for the oscillator when a crystal is connected between
        XIN32 and XOUT32 pins.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 2014
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                          Electrical Characteristics at 85°C

          Figure 54-7. Oscillator Crystal Connection
                                                                                       DEVICE


                                                                               XIN32
                                                          Crystal
                                                                     CLEXT
                                                   LM


                                                    RM      CSHUNT
                                                    CM


                                                                               XOUT32

                                                                     CLEXT


          The user must choose a crystal oscillator where the crystal load capacitance CL is within the range given
          in the table. The exact value of CL can be found in the crystal data sheet. The capacitance of the external
          capacitors (CLEXT) can then be computed as follows:
          CLEXT = 2 * (CL - CPARA - CPCB - CSHUNT)
          Where:
           • CPARA is the internal load capacitor parasitic between XIN32 and XOUT32 and can be computed as
             following:
             Equation 54-2.
                        ����32� * �����32�
             ����� =
                        ����32� + �����32�
            • CPCB is the capacitance of the PCB
            • CSHUNT is the shunt capacitance of the crystal as specified by the crystal manufacturer
Table 54-47. 32 kHz Crystal Oscillator Electrical Characteristics
Symbol           Parameter                                     Conditions                          Min.   Typ.        Max.      Units

FOUT(1)          Crystal oscillator frequency                  -                                   -      32.768      -         kHz

CL(1)            Crystal load capacitance                      -                                   -      -           12.5      pF

CSHUNT(1)        Crystal shunt capacitance                     -                                   -      -           1.7       pF

CM(1)            Motional capacitance                          -                                   2      -           7         fF

ESR              Crystal Equivalent Series Resistance -        f=32.768      Std. Gain             -      -           58        kΩ
                 SF=3                                          kHz,
                                                                             High Gain             -      -           90
                                                               CL=12.5
                                                               pF

CXIN32k          Parasitic load capacitor                      -                                   -      3.1         -         pF

CXOUT32k                                                       -                                   -      3.2         -

tSTARTUP         Startup time                                  f=32.768  Std. Gain                 -      12          28        kCycles
                                                               kHz,
                                                                         High Gain                 -      9           23
                                                               CL=12.5
                                                               pF,
                                                               CM=2.0 fF

          Note:
           1. These values are based on simulation. They are not covered by production test limits or
                characterization.




          © 2019 Microchip Technology Inc.                               Datasheet                            DS60001507E-page 2015
                                                                SAM D5x/E5x Family Data Sheet
                                                                             Electrical Characteristics at 85°C

          Table 54-48. Power Consumption

           Symbol          Parameter Condition        Ta           Gain Mode Typ.           Max.              Units
                                     s
           IDD             Current    VDD=3.0V        Max 85°C     Std.        1.5          2                 µA
                           consumptio                 Typ 25°C
                                                                   High        1.9          3
                           n

54.13.3 Internal Ultra Low Power 32 kHz RC Oscillator (OSCULP32K) Characteristics
Table 54-49. Ultra-Low-Power Internal 32 kHz RC Oscillator Electrical Characteristics

Symbol           Parameter              Calibration             Conditions                      Min.    Typ.       Max     Units
FOUT             Output frequency       Factory default and     At +25°C , VDDANA = 3.0V        32.10 32.768 33.42 kHz
                                        without user software
                                                                [-40, +85]°C, VDDANA>1.71V 27.12 32.768 37.68 kHz
                                        calibration
                                        With user software      Recalibrate using XOSC as       32.28              33.26
                                        calibration             reference Clock source
                                                                Recalibrate using DFLL as       31.29              33.75
                                                                reference Clock source
Step             Calibration step                                                               -       1.5        -       %FOUT
Duty(1)          Duty Cycle                                                                     -       50         -       %
RuntimeCal Run-time                                             CPU clock on DFLL (48 MHz) -            -          5       ms
           Calibration

          Note: These values are based on simulation. They are not covered by production test limits or
          characterization.




          © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 2016
                                                           SAM D5x/E5x Family Data Sheet
                                                                          Electrical Characteristics at 85°C

            Figure 54-8. Average Frequency Versus Calibration Code Value, VDD = 3V




54.13.4 Digital Frequency Locked Loop (DFLL48M) Characteristics
Table 54-50. DFLL48M Characteristics - Open Loop Mode (1)
Symbol                    Parameter           Conditions                              Min.      Typ.    Max.        Units

FOpenOUT                  Output frequency    DFLLVAL after Reset                     45.8      48      49.3        MHz
                                              LDO Regulator mode, [-40, 85]°C

                                              DFLLVAL after Reset                     47.2      48      48.81
                                              LDO Regulator mode, [0, 60]°C

TOpenSTARTUP              Startup time        DFLLVAL after Reset                     -         4.3     7           µs
                                              FOUT within 90% of final value


            Note:
             1. DFLL48 in open loop can be used only with LDO regulator.
Table 54-51. DFLL48M Characteristics - Closed Loop Mode

Symbol         Parameter                     Conditions                               Min.      Typ.        Max.     Units
FCloseOUT      Average Output frequency      fREF = XTAL, 32.768 kHz, 100 ppm             -    47.972         -      MHz
                                             DFLLMUL = 1464

FREF(1,2)      Input reference frequency                          -                   732       32768       33000        Hz




         © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 2017
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                   Electrical Characteristics at 85°C

...........continued
Symbol              Parameter                         Conditions                                      Min.       Typ.              Max.    Units
FCloseJitter        Period Jitter                     fREF = XTAL, 32.768 kHz, 100 ppm                 -                 -         0.42     ns
                                                      DFLLMUL = 1464

TLock               Lock time                         FREF = XTAL, 32.768 kHz, 100 ppm                 -             429           1145     µs
                                                      DFLLMUL = 1464
                                                      DFLLVAL after Reset
                                                      DFLLCTRL.BPLCKC = 1
                                                      DFLLCTRL.QLDIS = 0
                                                      DFLLCTRL.CCDIS = 1
                                                      DFLLMUL.FSTEP = 10

           Note:
            1. These values are based on simulation. They are not covered by production test limits or
                 characterization.
            2. To ensure that the device stays within the maximum allowed clock frequency, any reference clock
                 for the DFLL in close loop must be within 2% error accuracy.
Table 54-52. DFLL48M Power Consumption

Symbol Parameter                        Conditions                                             Ta                Min. Typ. Max. Units
IDD            Current Consumption Open Loop mode - DFLLVAL after reset VCC =                  Max. 85°C -                   400 854       µA
                                   3.3V                                                        Typ. 25°C
                                        Closed Loop mode - fREF = 32 .768 kHz VCC =                              -           404 851       µA
                                        3.3V

54.13.5 Fractional Digital Phase Lock Loop (FDPLL) Characteristics
           Table 54-53. Fractional Digital Phase Lock Loop Characteristics (2)

               Symbol Parameter                         Conditions                                     Min. Typ. Max. Units
               fIN(1)      Input Frequency                                                              32           -       3200    kHz
               fOUT(1)     Output Frequency                                                             96           -       200     MHz
               Jp          Period jitter (Peak-Peak     fIN = 32 kHz, fOUT = 96 MHz                        -     1.9         2.7      %
                           value)
                                                        fIN = 32 kHz, fOUT = 200 MHz                       -     3.4         4.9
                                                        fIN = 3.2 MHz, fOUT = 96 MHz                       -     2.0         3.0
                                                        fIN = 3.2 MHz, fOUT = 200 MHz                      -     4.3         6.6
               tLOCK       Lock Time                    After startup, time to get lock signal. fIN        -      54          95      μs
                                                        = 3.2 MHz
               Duty (1)    Duty cycle                                        -                             -      50          -       %




          © 2019 Microchip Technology Inc.                           Datasheet                                 DS60001507E-page 2018
                                                                  SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 85°C

         Note:
          1. These values are based on simulation. They are not covered by production test limits or
               characterization.
          2. These FDPLL200M characteristics are applicable with LDO regulator and a direct reference (i.e.,
               REFCLK is XOSC or XOSC32K, not GCLK).
Table 54-54. Power Consumption

Symbol       Parameter                           Conditions                         TA            Typ.    Max.    Units
IDD          Current Consumption                 Clk = 96 MHz, VDD = 3.3V           Max. 85°C     0.9     1.3     mA
                                                                                    Typ. 25°C
                                                 Clk = 200 MHz, VDD = 3.3V                        2       2.3



54.14    Timing Characteristics

54.14.1 External Reset Characteristics
        Table 54-55. External Reset Characteristics(1)

          Symbol                            Parameter               Min.                  Units
          tEXT                              Minimum Reset pulse     1                     µs
                                            width

         Note:
          1. These values are based on simulation. They are not covered by production test limits or
               characterization.
         Related Links
         6.1 Multiplexed Signals




         © 2019 Microchip Technology Inc.                         Datasheet                     DS60001507E-page 2019
                                                         SAM D5x/E5x Family Data Sheet
                                                                        Electrical Characteristics at 85°C

54.14.2 SERCOM in SPI Mode Timing
        Table 54-56. SPI Timing Characteristics and Requirements(1)

         Symbol Parameter                  Conditions            Min.               Typ.         Max.    Units
         tSCK(10)   SCK period             Master Reception      2*(tMIS            -            -       ns
                                                                 +tSLAVE_OUT)(3)
                                           Master Transmission   2*(tMOV+tSLAVE_IN) -            -
                                                                 (4)


         tSCKW      SCK high/low width     Master                -                  0.5*tSCK     -
         tSCKR      SCK rise time(2)       Master                -                  0.25*tSCK    -
         tSCKF      SCK fall time(2)       Master                -                  0.25*tSCK    -
         tMIS       MISO setup to SCK      Master, VDD>2.70V     18                 -            -
                                           Master, VDD>1.71V     19                 -            -
         tMIH       MISO hold after        Master,VDD>2.70V      0                  -            -
                    SCK
                                           Master, VDD>1.71V     0                  -            -
         tMOV       MOSI output valid      Master, VDD>2.70V     -                  -            9
                    SCK
                                           Master, VDD>1.71V     -                  -            14
         tMOH       MOSI hold after        Master, VDD>2.70V     -                  -            -
                    SCK
                                           Master, VDD>1.71V     -                  -            -




        © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 2020
                                                  SAM D5x/E5x Family Data Sheet
                                                                 Electrical Characteristics at 85°C

...........continued
 Symbol Parameter                  Conditions             Min.                Typ.         Max.      Units
 tSSCK      Slave SCK Period       Slave   Reception      2*(tSIS             -            -         ns
                                                          +tMASTER_OUT)(5)
                                   Slave   Transmission   2*(tSOV             -            -
                                                          +tMASTER_IN)(6)
 tSSCKW     SCK high/low width     Slave                  -                   0.5*tSSCK    -
 tSSCKR     SCK rise time(2)       Slave                  -                   0.25*tSSCK -
 tSSCKF     SCK fall time(2)       Slave                  -                   0.25*tSSCK -
 tSIS       MOSI setup to SCK      Slave, VDD>2.70V       7.5                 -            -
                                   Slave, VDD>1.71V       8.5                 -            -
 tSIH       MOSI hold after        Slave, VDD>2.70V       4                   -            -
            SCK
                                   Slave, VDD>1.71V       4                   -            -
 tSSS       SS setup to SCK        Slave   PRELOADEN=1 tSOSS+tEXT_MIS         -            -
                                                       +2*tAPBC(8)(9)
                                           PRELOADEN=0 tSOSS+tEXT_MIS(8)      -            -
 tSSH       SS hold after SCK      Slave                  0.5*tSSCK           -            -
 tSOV       MISO output valid      Slave, VDD>2.70V       15                  -            -
            SCK
                                   Slave, VDD>1.71V       24                  -            -
 tSOH       MISO hold after        Slave, VDD>2.70V       0                   -            -
            SCK
                                   Slave, VDD>1.71V       0                   -            -
 tSOSS      MISO setup after SS Slave, VDD>2.70V          -                   -            1* tSCK
            low
                                Slave, VDD>1.71V          -                   -            1* tSCK

  1.  These values are based on simulation, with capacitance load between 5pF and 20pF. These values
      are not covered by test limits in production.
  2. See I/O Pin Characteristics.
  3. Where tSLAVE_OUT is the slave external device output response time, generally tEXT_SOV+tLINE_DELAY
      (7).

  4. Where tSLAVE_IN is the slave external device input constraint, generally tEXT_SIS+tLINE_DELAY (7).
  5. Where tMASTER_OUT is the master external device output response time, generally tEXT_MOV
      +tLINE_DELAY (7).
  6. Where tMASTER_IN is the master external device input constraint, generally tEXT_MIS+tLINE_DELAY (7).
  7. tLINE_DELAY is the transmission line time delay.
  8. tEXT_MIS is the input constraint for the master external device.
  9. tAPBC is the APB period for SERCOM.
  10. When the integrity of communication is required to maintain both transmission and reception, the
      maximum SPI clock frequency should be the lower value of the reception or transmission mode
      maximum frequency as shown in the following equations.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 2021
                                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                Electrical Characteristics at 85°C

                – Reception: tSCK = 2*(tMIS+tSLAVE_OUT) = 2*(18 + 8) = 52nS
                – Transmission: tSCK = 2*(tMOV+tSLAVE_IN) = 2*(9 + 20) = 58nS
        Figure 54-9. SPI Timing Requirements in Master Mode
                         SS


                                                                                                   tSCKR               tSCKF


                      SCK
                 (CPOL = 0)


                                                                                                                    tSCKW
                      SCK
                 (CPOL = 1)
                                                                                                tSCKW
                                              tMIS     tMIH                                                tSCK

                       MISO
                                                     MSB                                                   LSB
                 (Data Input)
                                                                             tMOV
                                                                                                                            tMOH
                                                                  tMOH

                      MOSI
                                                       MSB                                                    LSB
               (Data Output)




        Figure 54-10. SPI Timing Requirements in Slave Mode

                         SS


                                       tSSS                                                        tSCKR               tSCKF
                                                                                                                                    tSSH

                      SCK
                 (CPOL = 0)


                                                                                                                    tSSCKW
                      SCK
                 (CPOL = 1)
                                                                                                tSSCKW
                                              tSIS         tSIH                                            tSSCK

                        MOSI
                                                      MSB                                                     LSB
                 (Data Input)
                                                                                                                                    tSOSH
                            tSOSS                                  tSOV                                                      tSOH

                      MISO
                                                       MSB                                                    LSB
                (Data Output)




54.14.3 QSPI Characteristics
        Figure 54-11. QSPI SDR Master Mode 0


                                QSCK


                                                                                        QSPI0            QSPI1

                            QIOx_DIN



                                                                          QSPI2

                          QIOx_DOUT




       © 2019 Microchip Technology Inc.                                             Datasheet                                       DS60001507E-page 2022
                                              SAM D5x/E5x Family Data Sheet
                                                           Electrical Characteristics at 85°C

Figure 54-12. QSPI SDR Master Mode 1

                      QSCK


                                               QSPI3        QSPI4

                    QIOx_DIN


                                   QSPI5

                  QIOx_DOUT


Figure 54-13. QSPI SDR Master Mode 2

                      QSCK


                                               QSPI6        QSPI7

                    QIOx_DIN


                                   QSPI8

                  QIOx_DOUT


Figure 54-14. QSPI SDR Master Mode 3


                     QSCK


                                                   QSPI9            QSPI10

                  QIOx_DIN



                                     QSPI11


                 QIOx_DOUT


Figure 54-15. QSPI DDR Mode 0 READ




© 2019 Microchip Technology Inc.              Datasheet                      DS60001507E-page 2023
                                                SAM D5x/E5x Family Data Sheet
                                                              Electrical Characteristics at 85°C

Figure 54-16. QSPI DDR Mode 0 WRITE




Table 54-57. QSPI Timing Characteristics (see Note 1)

 Name           Description           Mode                        VDD = 1.8V            VDD = 3.3V       Units
                                                             Min. Typ. Max. Min. Typ. Max.
 fSDR_m0_m2 QSPI SDR Frequency Master SDR Mode 0/2            -       -   50.0      -       -    75      MHz
 fSDR_m1_m3 QSPI SDR Frequency Master SDR Mode 1/3            -       -   50.0      -       -    50
 fDDR           QSPI DDR Frequency Master mode                -       -   37.5      -       -    66
 tSDR_QSPI0     Input Setup Time      Master SDR mode 0      3.86     -        -   3.85     -        -    ns
 tSDR_QSPI1     Input Hold Time       Master SDR mode 0      0.00     -        -   0.19     -        -
 tSDR_QSPI2     Data Out Valid Time   Master SDR mode 0       -       -   3.33      -       -   2.67

 tSDR_QSPI3     Input Setup Time      Master SDR mode 1      3.79     -        -   3.59     -        -    ns
 tSDR_QSPI4     Input Hold Time       Master SDR mode 1      0.06     -        -   0.19     -        -
 tSDR_QSPI5     Data Out Valid Time   Master SDR mode 1       -       -   2.71      -       -   2.71

 tSDR_QSPI6     Input Setup Time      Master SDR mode 2      3.79     -        -   3.58     -        -    ns
 tSDR_QSPI7     Input Hold Time       Master SDR mode 2      0.06     -        -   0.19     -        -
 tSDR_QSPI8     Data Out Valid Time   Master SDR mode 2       -       -   2.74      -       -   2.65

 tSDR_QSPI9     Input Setup Time      Master SDR mode 3      3.86     -        -   3.86     -        -    ns
 tSDR_QSPI10 Input Hold Time          Master SDR mode 3   -0.10       -        -   0.19     -        -
 tSDR_QSPI11 Data Out Valid Time      Master SDR mode 3       -       -   3.22      -       -   2.60




© 2019 Microchip Technology Inc.                 Datasheet                              DS60001507E-page 2024
                                                      SAM D5x/E5x Family Data Sheet
                                                                    Electrical Characteristics at 85°C

...........continued
 Name           Description                 Mode                        VDD = 1.8V                VDD = 3.3V       Units
                                                                   Min. Typ. Max. Min. Typ. Max.
 tDDR_QSPI0f Input Setup Time               Master DDR mode 0      3.87     -        -       3.85     -        -    ns
                                            fall edge
 tDDR_QSPI1f Input Hold Time                Master DDR mode 0      0.00     -        -       0.19     -        -
                                            fall edge
 tDDR_QSPI2f Data Out Valid Time            Master DDR mode 0       -       -    2.1          -       -   2.03
                                            fall edge
 tDDR_QSPI0r Input Setup Time               Master DDR mode 0      3.81     -        -       3.57     -     -
                                            rise edge
 tDDR_QSPI1r Input Hold Time                Master DDR mode 0      0.06     -        -       0.19     -        -
                                            rise edge
 tDDR_QSPI2r Data Out Valid Time            Master DDR mode 0       -       -   3.13          -       -   2.12
                                            rise edge

Note:
 1. These values are based on simulation. They are not covered by production test limits or
      characterization.
 2. All timing characteristics are given for 20pF capacitive load.
Table 54-58. QSPI Maximum Frequency examples(1)

 QSPI           CLK_QSPI2          CLK_QSPI        Max.         Max. QSPI                Conditions
 Mode           X _AHB             _AHB            CPU_CLK      Speed
 SDR            X                  120 MHz         120 MHz      60 MHz                   BAUD -> BAUD[7:0]
                                                                                         must be greater than 0 to
                                                                                         ensure QSPI clock
                                                                                         frequency is as per
                                                                                         electrical specifications
                                                                                         provided in table 54-52.
                X                  75 MHz          75 MHz       75 MHz                   -
 DDR            132 MHz            66 MHz          66 MHz       66 MHz                   -

Note: 1. Examples shown do not supersede the electrical specifications shown in Table 54-52. QSPI
Timing Characteristics.




© 2019 Microchip Technology Inc.                       Datasheet                                  DS60001507E-page 2025
                                                                SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 85°C

54.14.4 GMAC Characteristics

        Timing Conditions
        Table 54-59. GMAC Load Capacitance on Data, Clock Pads

        Symbol               Description        Condition           Min.              Max.                Units
        CL                   Load               VDD=3.3V            0                 20                  pF
                             Capacitance


        Timing Constraints
        The GMAC must be constrained so as to satisfy the timings of standards given the following two tables, in
        MAX corner.
        Table 54-60. Minimum and Maximum Access Time of GMAC Output Signals

        Symbol                   Parameter               Min.                 Max.                   Units
        GMAC1                    Setup for GMDIO         10                   -                      ns
                                 from GMDC rising
        GMAC2                    Hold for GMDIO          10                   -
                                 from GMDC rising
        GMAC3                    GMDIO toggling          0(1)                 10(1)
                                 from GMDC falling

        Note:
         1. For GMAC output signals, min. and max. access times are defined:
              – The min. access time is the time between the GMDC falling edge and the signal change.
              – The max. access time is the time between the GMDC falling edge and the signal stabilizes.
        Figure 54-17. Minimum and Maximum Access Time of GMAC Output Signals

                        GMDC
                                              GMAC1       GMAC2                               GMAC3 max


                        GMDIO
                                      GMAC4      GMAC5
                                                                                             GMAC3 min




       © 2019 Microchip Technology Inc.                           Datasheet                         DS60001507E-page 2026
                                                 SAM D5x/E5x Family Data Sheet
                                                                 Electrical Characteristics at 85°C

MII Mode
Table 54-61. GMAC MII Mode Timings

 Symbol             Parameter                                               Min     Max       Unit
 GMAC4              Setup for GCOL from GTXCK rising                        10      –         ns
 GMAC5              Hold for GCOL from GTXCK rising                         10      –
 GMAC6              Setup for GCRS from GTXCK rising                        10      –
 GMAC7              Hold for GCRS from GTXCK rising                         10      –
 GMAC8              GTXER toggling from GTXCK rising                        10      25
 GMAC9              GTXEN toggling from GTXCK rising                        10      25
 GMAC10             GTX toggling from GTXCK rising                          10      25
 GMAC11             Setup for GRX from GRXCK                                10      –
 GMAC12             Hold for GRX from GRXCK                                 10      –
 GMAC13             Setup for GRXER from GRXCK                              10      –
 GMAC14             Hold for GRXER from GRXCK                               10      –
 GMAC15             Setup for GRXDV from GRXCK                              10      –
 GMAC16             Hold for GRXDV from GRXCK                               10      –




© 2019 Microchip Technology Inc.                     Datasheet                    DS60001507E-page 2027
                                                           SAM D5x/E5x Family Data Sheet
                                                                            Electrical Characteristics at 85°C

Figure 54-18. GMAC MII Mode Signals

                  EMDC
                                            GMAC1       GMAC2                               GMAC3

                  EMDIO
                                   GMAC4       GMAC5

                   ECOL
                                   GMAC6       GMAC7

                   ECRS


                 ETXCK
                                                                                    GMAC8

                 ETXER
                                                                                    GMAC9

                 ETXEN
                                                                                    GMAC10

                ETX[3:0]




                 ERXCK
                                   GMAC11      GMAC12

                ERX[3:0]
                                   GMAC13      GMAC14

                 ERXER
                                   GMAC15      GMAC16

                 ERXDV




© 2019 Microchip Technology Inc.                                Datasheet                      DS60001507E-page 2028
                                                       SAM D5x/E5x Family Data Sheet
                                                                   Electrical Characteristics at 85°C

RMIII Mode
Table 54-62. GMAC RMII Mode Timings

 Symbol                    Parameter            Min.               Max.             Units
 GMAC21                    ETXEN toggling       2                  16               ns
                           from EREFCK
                           rising
 GMAC22                    ETX toggling from    2                  16
                           EREFCK rising
 GMAC23                    Setup for ERX from 4                    -
                           EREFCK rising
 GMAC24                    Hold for ERX from    2                  -
                           EREFCK rising
 GMAC25                    Setup for ERXER      4                  -
                           from EREFCK
                           rising
 GMAC26                    Hold for ERXER       2                  -
                           from EREFCK
                           rising
 GMAC27                    Setup for ECRSDV 4                      -
                           from EREFCK
                           rising
 GMAC28                    Hold for ECRSDV      2                  -
                           from EREFCK
                           rising

Figure 54-19. GMAC RMII Mode Signals

                EREFCK
                                                                           GMAC21

                 ETXEN
                                                                           GMAC22

                ETX[1:0]
                                   GMAC23   GMAC24

                ERX[1:0]
                                   GMAC25   GMAC26

                 ERXER
                                   GMAC27   GMAC28

                ECRSDV




© 2019 Microchip Technology Inc.                       Datasheet                    DS60001507E-page 2029
                                                            SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 85°C

54.14.5 I2S Characteristics
        Table 54-63. I2S Timing Characteristics and Requirements (see Note 1)

         Name         Description             Mode                            VDD = 1.8V            VDD = 3.3V       Units
                                                                        Min. Typ. Max. Min. Typ. Max.
         tM_MCKOR I2S MCK rise time(2)        Master mode /               -       -    5.41     -        -    2.68    ns
                                              Capacitive load CL = 20
                                              pF
         tM_MCKOF I2S MCK fall time (2)       Master mode /               -       -    5.84     -        -    2.81    ns
                                              Capacitive load CL = 20
                                              pF
         dM_MCKO      I2S MCK duty cycle      Master mode                 -     50.0     -      -      50.0    -      %
         dM_MCKI      I2S MCK duty cycle      Master mode, pin is         -     50.0     -      -      50.0    -      %
                                              input (1b)
         tM_SCKOR I2S SCK rise time (2)       Master mode /               -       -    5.06     -        -    2.51    ns
                                              Capacitive load CL = 20
                                              pF
         tM_SCKOF     I2S SCK fall time (2)   Master mode /               -       -    5.46     -        -    2.64    ns
                                              Capacitive load CL = 20
                                              pF
         dM_SCKO      I2S SCK duty cycle      Master mode                 -     50.0     -      -      50.0    -      %
         fM_SCKO I2S SCK frequency            Master mode                 -       -    32.07    -        -    43.73 MHz
         1/tM_SCKO                            Supposing external
                                              device response delay
                                              is 0ns
                                              Master mode                 -       -    10.97    -        -    12.07 MHz
                                              Supposing external
                                              device response delay
                                              is 30ns
         fS_SCKI      I2S SCK frequency       Slave mode Supposing        -       -    15.63    -        -    15.87 MHz
         1/tS_SCKI                            external device
                                              response delay is 30ns
         dS_SCKO      I2S SCK duty cycle      Slave mode                  -     50.0     -      -      50.0    -      %
         tM_FSOV      FS valid time           Master mode                 -       -     5.4     -        -    4.2     ns
         tM_FSOH      FS hold time            Master mode               -0.3      -      -     -0.3      -     -      ns
         tS_FSIS      FS setup time           Slave mode                 7.8      -      -     7.5       -     -      ns
         tS_FSIH      FS hold time            Slave mode                 0.0      -      -     0.0       -     -      ns
         tM_SDIS      Data input setup time Master mode                 15.8      -      -     11.6      -     -      ns
         tM_SDIH      Data input hold time    Master mode                3.4      -      -     3.4       -     -      ns
         tS_SDIS      Data input setup time Slave mode                   2.4      -      -     1.9       -     -      ns




        © 2019 Microchip Technology Inc.                     Datasheet                                DS60001507E-page 2030
                                                   SAM D5x/E5x Family Data Sheet
                                                                      Electrical Characteristics at 85°C

...........continued
 Name         Description            Mode                             VDD = 1.8V          VDD = 3.3V      Units
                                                               Min. Typ. Max. Min. Typ. Max.
 tS_SDIH      Data input hold time   Slave mode                -1.1       -     -    -1.0      -     -      ns
 tM_SDOV      Data output valid time Master transmitter           -       -    3.7    -        -    3.0     ns
 tM_SDOH      Data output hold time Master transmitter         -0.5       -     -    -0.5      -     -      ns
 tS_SDOV      Data output valid time Slave transmitter            -       -   16.4    -        -   12.1     ns
 tS_SDOH      Data output hold time Slave transmitter            4.1      -     -    4.1       -     -      ns
 tPDM2LS      Data input setup time Master mode PDM2           15.8       -     -    11.6      -     -      ns
                                    Left
 tPDM2LH      Data input hold time   Master mode PDM2            3.4      -     -    3.4       -     -      ns
                                     Left
 tPDM2RS      Data input setup time Master mode PDM2           15.1       -     -    11.6      -     -      ns
                                    Right
 tPDM2RH      Data input hold time   Master mode PDM2            3.4      -     -    3.4       -     -      ns
                                     Right


               Notice: All timing values are given for 20pF capacitive load.




Note:
 1. These values are based on simulation. They are not covered by production test limits or
      characterization.
 2. See I/O Pin Characteristics.




© 2019 Microchip Technology Inc.                     Datasheet                              DS60001507E-page 2031
                                           SAM D5x/E5x Family Data Sheet
                                                         Electrical Characteristics at 85°C

Figure 54-20. Master Mode: SCK, FX, and MCK are Output




Figure 54-21. Slave Mode: SCK and FS are Input




Figure 54-22. PDM2 Mode




© 2019 Microchip Technology Inc.             Datasheet                   DS60001507E-page 2032
                                                          SAM D5x/E5x Family Data Sheet
                                                                      Electrical Characteristics at 85°C

54.14.6 PCC Characteristics
        Speed requirements for all 8/10/12/14-bits are:
         • pclk: 48 MHz at 3.3V
         • pclk: 28 MHz at 1.8V
         APB clock minimum is 2 × N pclk
         Figure 54-23. PCC Signaling




54.15    USB Characteristics
         The USB on-chip buffers comply with the Universal Serial Bus (USB) v2.0 standard. All AC parameters
         related to these buffers can be found within the USB 2.0 electrical specifications.
         The USB interface is USB-IF certified:
          • TID 40001782 - Peripheral Silicon > Low/Full Speed > Silicon Building Blocks
          • TID 120000724 - Embedded Hosts > Full Speed
         Electrical configuration required to be USB-compliant:
          • the CPU frequency must be higher than 16 MHz when USB is active (No constraint for USB suspend
             mode)
          • the operating voltages must be 3.3V (Min. 3.0V, Max. 3.6V).
          • the GCLK_USB frequency accuracy source must be less than:
                – in USB device mode, 48MHz +/-0.25%
                – in USB host mode, 48MHz +/-0.05%




        © 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 2033
                                                         SAM D5x/E5x Family Data Sheet
                                                                     Electrical Characteristics at 85°C

Table 54-64. GCLK_USB Clock Setup Recommendations

Clock setup                                                                   USB Device         USB Host
DFLL48M          Open loop                                                    No                 No
                 Close loop, Ref. internal OSC source                         No                 No
                 Close loop, Ref. external XOSC source                        Yes                No
                 Close loop, Ref. SOF (USB recovery mode)(1)                  Yes(2)             N/A
FDPLL            internal OSC (32K, 8M…)                                      No                 No
                 external OSC (<1MHz)                                         Yes                No
                 external OSC (>1MHz)                                         Yes(3)             Yes

        Note:
         1. When using DFLL48M in USB recovery mode, the Fine Step value must be 0xA to guarantee a
              USB clock at +/-0.25% before 11ms after a resume. Only usable in LDO regulator mode.
         2. Very high signal quality and crystal-less. It is the best setup for USB Device mode.
         3. FDPLL lock time is short when the clock frequency source is high (> 1 MHz). Thus, FDPLL and
              external OSC can be stopped during USB suspend mode to reduce consumption and guarantee a
              USB wake-up time (See TDRSMDN in the USB 2.0 specification).




        © 2019 Microchip Technology Inc.                 Datasheet                     DS60001507E-page 2034
