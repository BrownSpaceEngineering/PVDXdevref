# 56. Electrical Characteristics at 125°C

*Source: `Atmel-SAMD51.pdf`, pages 2053-2071 — SAMD51 family datasheet*

                                                             SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 125°C


56.      Electrical Characteristics at 125°C
         The specifications for 125°C temperature devices are identical to those shown in 54. Electrical
         Characteristics at 85°C, with the exception of the parameters listed in this chapter.



56.1     General Operating Ratings (125°C)
         The device must operate within the ratings listed below in order for all other electrical characteristics and
         typical characteristics of the device to be valid.
Table 56-1. General Operating Conditions

Symbol                 Description                                  Min.            Typ.            Max.         Units
TA                     Temperature range                            -40             25              125          °C
TJ                     Junction temperature                         -               -               145          °C



56.2     Injection Current (125°C)
         Stresses beyond those listed in the table below may cause permanent damage to the device. This is a
         stress rating only and functional operation of the device at these or other conditions beyond those
         indicated in the operational sections of this specification is not implied. Exposure to absolute maximum
         rating conditions for extended periods may affect device reliability.
Table 56-2. Injection Current(1, 2)

Symbol Description                              min Typ. max Unit Comments
IICL      Input Low Injection Current           -15 -         -   mA Note: 1, 4, 5
                                                                     This Parameter applies to all pins.

IICH      Input High Injection Current           -   -       15   mA Note: 2, 3, 4, 5
                                                                     This parameter applies to all pins, with the
                                                                     exception of 5V tolerant pins.

∑IICT     Total Input Injection Current (Sum     -   -       18   mA Absolute instantaneous sum of all ± input injection
          of all I/O and control pins)                               currents from all I/O pins.
          Absolute value of |∑IICT|




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 2053
                                                                SAM D5x/E5x Family Data Sheet
                                                                               Electrical Characteristics at 125°C

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



56.3        Supply Characteristics (125°C)
            Table 56-3. Power Supply Current Requirement

            Symbol              Conditions                                               Current            Units
                                                                                         Max.
            Iinput              Power-up Maximum Current                                 12                 mA

            Note: Iinput is the minimum requirement for the power supply connected to the device.



56.4        Maximum Clock Frequencies (125°C)
Table 56-4. Maximum Peripheral Clock Frequencies(1)

Symbol                                       Description                                                     Max.     Units
fCPU                                         CPU clock frequency                                             100      MHz
fAHB                                         AHB clock frequency                                             100      MHz
fAPBx, x = {A, B, C, D}                      APBA, APBB, APBC and APBD clock frequency                       100      MHz
fGCLK_EIC                                    EIC input clock frequency                                       90       MHz
fGCLK_FREQM_MSR                              FREQM Measure                                                   180      MHz
fGCLK_FREQM_REF                              FREQM Reference                                                 90       MHz
fGCLK_EVSYS_CHANNEL_x, x = {0,.., 11}        EVSYS channel ‘x’ input clock frequency                         90       MHz
fGCLK_SERCOMx_CORE, x = {0, ... , 7}         SERCOMx input clock frequency                                   90       MHz
fGCLK_CANx, x = {0, 1}                       CANx input clock frequency                                      90       MHz
fGCLK_I2S                                    I2S input clock frequency                                       90       MHz
fGCLK_SDHCx_CORE, x = {0, 1}                 SDHCx input clock frequency                                     150      MHz




          © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 2054
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                 Electrical Characteristics at 125°C

...........continued
Symbol                                        Description                                                 Max.     Units
fGCLK_TCCx, x = {0, ... , 4}                  TCCx input clock frequency                                  180      MHz
fGCLK_TCx, x = {0, ... , 3}                   TC0, TC1, TC2, TC3 input clock frequency                    180      MHz
fGCLK_PDEC                                    PDEC input clock frequency                                  180      MHz
fGCLK_CCL                                     CCL input clock frequency                                   90       MHz
fGCLK_CM4_TRACE                               CM4 Trace input clock frequency                             100      MHz
fGCLK_AC                                      AC digital input clock frequency                            90       MHz
fGCLK_ADCx, x = {0, 1}                        ADCx input clock frequency                                  90       MHz
fGCLK_DAC                                     DAC input clock frequency                                   90       MHz

            Note:
             1. These values are based on simulation. They are not covered by production test limits or
                  characterization.



56.5        Power Consumption (125°C)
            The values in this section are measured values of power consumption under the following conditions,
            except where noted:
             • Operating Conditions
                 – CPU is running on Flash with automatic wait state
                 – Low-power cache enabled
                 – BOD33 is disabled
                 – I/Os are inactive input mode with input trigger disabled
             • Oscillators
                 – XOSC0 (crystal oscillator) running with external 32 MHz crystal
                 – XOSC32K (32 kHz crystal oscillator) running with external 32 kHz crystal in LP mode
                 – FDPLL is using XOSC32K as reference on LDO and external clock 32768 on Buck mode
                 – DFLL48M is using XOSC32K as reference




           © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 2055
                                                                  SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 125°C

Table 56-5. Active Current Consumption - Active Mode
  Mode             conditions         Regulator       Clock         VDD                   TA                    Typ.   Max.    Units

                                                                    1.8                                         136    229
                                                  FDPLL 100 MHz
                                                                    3.3                                         137    232

                                                                    1.8                                         136    370
                                        LDO        DFLL 48 MHz
                                                                    3.3                                         136    371

                                                                    1.8                                         146    611
                                                  XOSC 32 MHz
                                                                    3.3                                         149    613
  ACTIVE         COREMARK (1)
                                                                    1.8                                         103    215
                                                  FDPLL 120 MHz
                                                                    3.3                                         65     176

                                                                    1.8                                         102    324
                                       BUCK        DFLL 48 MHz
                                                                    3.3                                         63     242

                                                                    1.8                                         110    505
                                                  XOSC 32 MHz
                                                                    3.3                                         73     370
                                                                               Max. at 125°C Typ at 25°C                      uA/Mhz
                                                                    1.8                                         21     114
                                                  FDPLL 100 MHz
                                                                    3.3                                         23     116

                                                                    1.8                                         21     252
                                        LDO        DFLL 48 MHz
                                                                    3.3                                         21     252

                                                                    1.8                                         25     367
                                                  XOSC 32 MHz
                                                                    3.3                                         27     371
   IDLE               NA
                                                                    1.8                                         16     89
                                                  FDPLL 100 MHz
                                                                    3.3                                         11     78

                                                                    1.8                                         16     194
                                       BUCK        DFLL 48 MHz
                                                                    3.3                                         10     147

                                                                    1.8                                         21     287
                                                  XOSC 32 MHz
                                                                    3.3                                         19     223


           Note:
            1. System Configuration used:
                 – MCLK all APB clocks masked except MCLK and NVMCTRL
                 – MCLK.AHBMASK = 0x00C00FFF
                 – CMCC enabled




           © 2019 Microchip Technology Inc.                       Datasheet                                DS60001507E-page 2056
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                   Electrical Characteristics at 125°C

Table 56-6. Standby, Hibernate, Backup and Off Mode Current Consumption
                                                                                   Regulator
  Mode                                        Conditions                                       Vcc            TA            Typ.   Max.   Units
                                                                                     Mode

                                                                                               1.8V                         43     5834
                       fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),             LDO
                                         no peripheral running                                 3.3V                         43     5851
                       No System RAM retained (PM.STDBYCFG.RAMCFG=0x2).
                                                                                               1.8V                         26     3950
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         17     2817

                                                                                               1.8V                         85     8707
                       fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),              LDO
                                        no peripheral running                                  3.3V                         85     8724
                       No System RAM retained (PM.STDBYCFG.RAMCFG=0x2).
                                                                                               1.8V                         65     6766
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         47     5269

                                                                                               1.8V                         43     5843
                       fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),             LDO
                                       RTC running on XOSC32K                                  3.3V                         44     5860
                       No System RAM retained (PM.STDBYCFG.RAMCFG=0x2).
                                                                                               1.8V                         26     3965
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         18     2891

                                                                                               1.8V                         45     6085
                       fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),             LDO
                                       RTC running on XOSC32K                                  3.3V                         46     6102
                                                                                                      Max at 125°C Typ at
 STANDBY                                                                                                                                   µA
                      32KB System RAM retained (PM.STDBYCFG.RAMCFG=0x1).                                     25°C
                                                                                               1.8V                         27     4137
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         19     3012

                                                                                               1.8V                         53     7049
                       fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),             LDO
                                       RTC running on XOSC32K                                  3.3V                         53     7068
                       Full System RAM retained (PM.STDBYCFG.RAMCFG=0x0).
                                                                                               1.8V                         32     4923
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         22     3479

                                                                                               1.8V                         101    5543
                       fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),              LDO
                                        no peripheral running                                  3.3V                         101    5571
                       Full System RAM retained (PM.STDBYCFG.RAMCFG=0x0).
                                                                                               1.8V                         78     4266
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         55     3075

                                                                                               1.8V                         102    5563
                       fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),              LDO
                                      RTC running on XOSC32K                                   3.3V                         103    5588
                       Full System RAM retained (PM.STDBYCFG.RAMCFG=0x0).
                                                                                               1.8V                         79     4270
                                     8KB backup RAM retained                        BUCK
                                                                                               3.3V                         56     3080




           © 2019 Microchip Technology Inc.                            Datasheet                             DS60001507E-page 2057
                                                                               SAM D5x/E5x Family Data Sheet
                                                                                              Electrical Characteristics at 125°C

...........continued
                                                                                              Regulator
    Mode                                           Conditions                                             Vcc            TA            Typ.   Max.    Units
                                                                                                Mode

                                                                                                          1.8V                          6     316
                                                                                                LDO
                                              no peripheral running
                                                                                                          3.3V                          6     320
                                No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                                No backup RAM retained (PM.HIBCFG.BRAMCFG=0x2)                            1.8V                          3     216
                                                                                               BUCK
                                                                                                          3.3V                          3     221

                                                                                                          1.8V                          6     318
                                                                                                LDO
                                           RTC is running on XOSC32K
                                                                                                          3.3V                          7     322
                                No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                                No backup RAM retained (PM.HIBCFG.BRAMCFG=0x2)                            1.8V                          3     217
                                                                                               BUCK
                                                                                                          3.3V                          3     223

                                                                                                          1.8V                          7     359
                                                                                                LDO
                                           RTC is running on XOSC32K
                                                                                                          3.3V                          8     364
                                No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                               4 KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x1)                           1.8V                          3     244
                                                                                               BUCK
                                                                                                          3.3V   Max at 125°C Typ at    4     250
 HIBERNATE                                                                                                                                             µA
                                                                                                          1.8V          25°C            7     400
                                                                                                LDO
                                           RTC is running on XOSC32K
                                                                                                          3.3V                          8     405
                                No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                               8 KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x0)                           1.8V                          4     273
                                                                                               BUCK
                                                                                                          3.3V                          4     279

                                                                                                          1.8V                          9     636
                                                                                                LDO
                                            RTC is running on XOSC32K
                                                                                                          3.3V                          10    641
                               32 KB System RAM retained (PM.HIBCFG.RAMCFG=0x1)
                               8KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x0)                            1.8V                          5     430
                                                                                               BUCK
                                                                                                          3.3V                          4     434

                                                                                                          1.8V                          16    1574
                                                                                                LDO
                                             RTC is running on XOSC32K
                                                                                                          3.3V                          17    1578
                                Full System RAM retained (PM.HIBCFG.RAMCFG=0x0)
                               8 KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x0)                           1.8V                          9     1061
                                                                                               BUCK
                                                                                                          3.3V                          7     1084

                                               powered by VDDIO,                                          1.8V                          2.1   303.5
                                   no RTC running VDDIO+VDDANA consumption
                               No backup RAM retained (PM.BKUPCFG.BRAMCFG=0x2)                            3.3V                          2.5   307.8

                                               powered by VDDIO with                                      1.8V                          2.7   304.8
                               RTC running on XOSC32K VDDIO+VDDANA consumption
                               No backup RAM retained (PM.BKUPCFG.BRAMCFG=0x2)                            3.3V                          3.3   309.5

                                               powered by VDDIO,                                          1.8V                          2.4   344.6
                                   no RTC running VDDIO+VDDANA consumption
   BACKUP                                                                                                 3.3V                          2.8   348.7
                              4 KB backup RAM retained (PM.BKUPCFG.BRAMCFG=0x1)
                                                                                                                 Max at 125°C Typ at
                                                                                                                                                       µA
                                               powered by VDDIO,                                          1.8V          25°C            2.7   385.1
                                   no RTC running VDDIO+VDDANA consumption
                              8 KB backup RAM retained (PM.BKUPCFG.BRAMCFG=0x0)                           3.3V                          3.1   389.6

                         Battery backup mode powered by VBAT with RTC running on XOSC32K                  1.8V                          2.7   305
                                                VBAT consumption
                       No backup RAM retained (PM.BKUPCFG.BRAMCFG=0x2), BOD33 enabled in                  3.3V                          3.3   310
                                   sampled mode PSEL prescaler set to 0x7 (div 256)

                                                                                                          1.8V                         0.191 26.35
     OFF                                                -
                                                                                                          3.3V                         0.331 31.07




              © 2019 Microchip Technology Inc.                                    Datasheet                             DS60001507E-page 2058
                                                             SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 125°C


56.6     Analog Characteristics (125°C)

56.6.1   Power-On Reset (POR) Characteristics (125°C)
         Table 56-7. POR Characteristics

          Symbol          Parameters                                                Min.   Typ.   Max.     Unit
          VPOT+           Voltage threshold Level on VDDIO rising                   1.52   1.58   1.65     V
          VPOT-           Voltage threshold Level on VDDIO falling                  0.97   1.26   1.36     V

         Figure 56-1. POR Operating PrincipleVDD




                                           VPOT+
                                           VPOT-



                                                                                    Time
                                             Reset




         Note: The shaded area indicates that the device is in a Reset state.

56.6.2   Brown-Out Detectors (BOD) Characteristics (125°C)
         Figure 56-2. BOD33 Hysteresis OFF

                                     VCC
                                                      VBOD



                                  RESET

         Figure 56-3. BOD33 Hysteresis ON

                                     VCC                                    VBOD+
                                                     VBOD-



                                  RESET




         © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 2059
                                                  SAM D5x/E5x Family Data Sheet
                                                                 Electrical Characteristics at 125°C

Table 56-8. BOD33 Characteristics on VDD and VBAT Monitoring in Normal Mode (During Power-up
Phase and Active Mode)

 Symbol                   Parameters         Conditions (see        Min     Typ       Max        Unit
                                             Notes 3, 4)
 VBOD or VBOD-            BOD33 threshold    LEVEL[7:0] = 0x00      1.45    1.50      1.55        V
 ( see Note 1)            level Hysteresis   (min)
                          OFF or BOD33
                                             LEVEL[7:0] = 0x19      1.6     1.65      1.71
                          threshold level
                                             (recommended
                          Hysteresis ON
                                             value)
                                             LEVEL[7:0]= 0x1C       1.62    1.67      1.73
                                             (fuse value)
                                             LEVEL[7:0] = 0xFF      2.93    3.040     3.13
                                             (max)
 VBOD+ (see Note          BOD33 threshold    LEVEL[7:0] = 0x00      1.46    1.520     1.57
 2)                       level Hysteresis   (min)
                          ON at power
                                             LEVEL[7:0]= 0x19       1.61    1.669     1.72
                          voltage rising
                                             (recommended
                                             value)
                                             LEVEL[7:0] = 0x1C      1.63    1.687     1.74
                                             (fuse value)
                                             LEVEL[7:0] = 0xFF      2.93    3.041     3.32
                                             (max)

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




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 2060
                                                  SAM D5x/E5x Family Data Sheet
                                                                 Electrical Characteristics at 125°C

Table 56-9. BOD33 Characteristics on VDD and VBAT Monitoring in Low-Power Mode (During
Standby/Backup/Hibernate Modes)

 Symbol                   Parameters         Conditions (see        Min     Typ       Max        Unit
                                             Notes 3, 4)
 VBOD or VBOD-            BOD33 threshold    LEVEL[7:0] = 0x00      1.39    1.510     1.62        V
 ( see Note 1)            level Hysteresis   (min)
                          OFF or BOD33
                                             LEVEL[7:0]= 0x19       1.52    1.659     1.79
                          threshold level
                                             (recommended
                          Hysteresis ON
                                             value)
                                             LEVEL[7:0] = 0x1C      1.54    1.677     1.80
                                             (fuse value)
                                             LEVEL[7:0] = 0xFF      2.80    3.045     3.28
                                             (max)
 VBOD+ (see Note          BOD33 threshold    LEVEL[7:0] = 0x00      1.40    1.522     1.63
 2)                       level Hysteresis   (min)
                          ON at power
                                             LEVEL[7:0]= 0x19       1.54    1.672     1.80
                          voltage rising
                                             (recommended
                                             value)
                                             LEVEL[7:0] = 0x1C      1.56    1.690     1.82
                                             (fuse value)
                                             LEVEL[7:0] = 0xFF      2.80    3.045     3.28
                                             (max)

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




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 2061
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                        Electrical Characteristics at 125°C

          Table 56-10. BOD33 Power Consumption

           Symbol CPU Mode                                            Conditions TA                                       Typ.       Max Units
           IDD          Active / Idle                                 VCC = 1.8V Max 125°C Typ 25°C 8.52                             13.9 µA
                                                                      VCC = 3.3V                                          10.10 16.5
                        Standby with BOD continuous normal VCC = 1.8V                                                     4.71       6.7
                        mode
                                                           VCC = 3.3V                                                     6.01       8.6
                        Standby with BOD continuous low               VCC = 1.8V                                          0.15       0.27
                        power mode or Hibernate mode
                                                                      VCC = 3.3V                                          0.21       0.35

56.6.3    Analog-to-Digital Converter (ADC) Characteristics (125°C)
          Analog-to-Digital Converter conditions table is the same as 105°C.
Table 56-11. Differential Mode (1)
                                                                                                                                     Measurement
Symbol                       Parameter                                              Conditions                                                            Unit
                                                                                                                             Min        Typ      Max
                                                                                             Vddana=3.0V Vref=Vddana         10.5      10.8      11.2
 ENOB                 Effective Number of bits          Fadc = 1Msps - R2R disabled                                                                       bits
                                                                                             Vddana=3.0V ExtVref=2.0V        10.5      10.8      11.0
                                                                                             Vddana=3.0V Vref=Vddana             -     +/-2.3   +/-5.2
  TUE                Total Unadjusted Error (3)         Fadc = 1Msps - R2R disabled
                                                                                             Vddana=3.0V ExtVref=2.0V            -     +/-2.7   +/-5.8
                                                                                             Vddana=3.0V Vref=Vddana             -     +/-1.2   +/-1.8
  INL                  Integral Non Linearity           Fadc = 1Msps - R2R disabled                                                                       LSB
                                                                                             Vddana=3.0V ExtVref=2.0V            -     +/-1.2   +/-1.9
                                                                                             Vddana=3.0V Vref=Vddana             -    +/-0.98   -1/+1
  DNL                 Differential Non Linearity        Fadc = 1Msps - R2R disabled
                                                                                             Vddana=3.0V ExtVref=2.0V            -    +/-0.96   -1/+1.2
                                                                                             Vddana=3.0V Vref=Vddana         -0.21     -0.02     +0.2
                                                                                             Vddana=3.0V ExtVref=2.0V        -0.13     +0.03    +0.21
  Gain        Gain Error with REFCTRL.REFCOMP=1                Fadc = 1Msps                                                                                %
                                                                                            Vddana=3.0V 1V internal Ref      -10           -1    +6.7
                                                                                            Vddana=3.0V Vref=Vddana/2        -0.48     +0.2     +0.75
                                                                                             Vddana=3.0V Vref=Vddana         -0.3      -0.001    +0.2
                                                                                             Vddana=3.0V ExtVref=2.0V        -0.94     -0.05    +0.71
  Gain        Gain Error with REFCTRL.REFCOMP=0                Fadc = 1Msps                                                                               mV
                                                                                            Vddana=3.0V 1V internal Ref      -10           -1    +6.7
                                                                                            Vddana=3.0V Vref=Vddana/2        -1.2      +0.11    +1.28
                                                                                             Vddana=3.0V Vref=Vddana         -3.6      -0.24     +3.1
                                                                                             Vddana=3.0V ExtVref=2.0V        -3.3       -0.2     +2.7
 Offset      Offset Error with SAMPCTRL.OFFCOMP=1              Fadc = 1Msps                                                                                %
                                                                                            Vddana=3.0V 1V internal Ref      -3.6       -0.2     +2.9
                                                                                            Vddana=3.0V Vref=Vddana/2        -3.6      -0.34     +3.3
                                                                                             Vddana=3.0V Vref=Vddana         -11.9     +0.03    +/-12.3
                                                                                             Vddana=3.0V ExtVref=2.0V        -12.2     -0.03    +12.4
 Offset      Offset Error with SAMPCTRL.OFFCOMP=0              Fadc = 1Msps                                                                               mV
                                                                                            Vddana=3.0V 1V internal Ref      -14.3     +0.5     +14.7
                                                                                            Vddana=3.0V Vref=Vddana/2        -13.6     +0.5      +14
 SFDR              Spurious Free Dynamic Range                                                                               76.6      79.6      83.5
 SINAD           Signal to Noise and Distortion ratio                                                                        65.3      67.2      68.9
                                                        Fs = 1Msps Fin = 14kHz (2)           Vddana=3.0V Vref=Vddana                                      dB
  SNR                   Signal to Noise ratio                                                                                64.7      66.5      68.2
  THD                Total Harmonic Distortion                                                                               -91.6     -82.9    -78.3
                                                                                             Vddana=3.0V ExtVref=2.0V        0.2        0.4      2.4
 Nrms                        Noise RMS                     constant input voltage                                                                         mV
                                                                                             Vddana=3.0V Vref=Vddana         0.15      0.25      2.5




          © 2019 Microchip Technology Inc.                             Datasheet                                     DS60001507E-page 2062
                                                  SAM D5x/E5x Family Data Sheet
                                                                Electrical Characteristics at 125°C

Note:
 1. These values are based on characterization. These values are not covered by test limits in
      production.
 2. All values expressed in decibel refer to the full scale input and are tested with an input signal
      0.35dB below full scale; THD measured on the first seven harmonics of the input signal.
 3. With REFCTRL.REFCOMP=1 and SAMPCTRL.OFFCOMP=1.
Table 56-12. Single Ended Mode (1)

                                                                                     Measurement
 Symbol                 Parameter                     Conditions                                          Unit
                                                                               Min      Typ      Max
                                                             Vddana=3.0V
                                                Fadc =                         8.9      9.25      9.9
                                                             Vref=Vddana
  ENOB           Effective Number of bits    1Msps - R2R                                                  bits
                                               disabled      Vddana=3.0V
                                                                               8.9      9.5       9.7
                                                             ExtVref=2.0V
                                                             Vddana=3.0V
                                                Fadc =                           -     +/-10.9   +/-21
                                                             Vref=Vddana
   TUE          Total Unadjusted Error (3)   1Msps - R2R
                                               disabled      Vddana=3.0V
                                                                                 -     +/-10.5 +/-19.7
                                                             ExtVref=2.0V
                                                             Vddana=3.0V
                                                Fadc =                           -     +/-2.3    +/-3.2
                                                             Vref=Vddana
    INL           Integral Non Linearity     1Msps - R2R                                                  LSB
                                               disabled      Vddana=3.0V
                                                                                 -     +/-2.3    +/-3.9
                                                             ExtVref=2.0V
                                                             Vddana=3.0V
                                                Fadc =                           -     +/-0.99   -1/+1
                                                             Vref=Vddana
   DNL          Differential Non Linearity   1Msps - R2R
                                               disabled      Vddana=3.0V
                                                                                 -     +/-0.98 -1/+1.5
                                                             ExtVref=2.0V
                                                             Vddana=3.0V
                                                                               -0.3    -0.01     +0.3
                                                             Vref=Vddana
                                                             Vddana=3.0V
                                                                               -0.16 +0.02       +0.3
                   Gain Error with             Fadc =        ExtVref=2.0V
   Gain                                                                                                    %
                REFCTRL.REFCOMP=1              1Msps         Vddana=3.0V
                                                                               -11      -1.1      +7
                                                             1V internal Ref
                                                            Vddana=3.0V
                                                                               -0.5    +0.13     +0.7
                                                            Vref=Vddana/2




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 2063
                                                    SAM D5x/E5x Family Data Sheet
                                                                  Electrical Characteristics at 125°C

...........continued
                                                                                    Measurement
 Symbol                 Parameter                        Conditions                                      Unit
                                                                                 Min     Typ     Max
                                                               Vddana=3.0V
                                                                                 -21     -7.2    +9.3
                                                               Vref=Vddana
                                                               Vddana=3.0V
                                                                                 -21     -3.3    +17
                  Offset Error with              Fadc =        ExtVref=2.0V
  Offset                                                                                                 mV
               SAMPCTRL.OFFCOMP=1                1Msps         Vddana=3.0V
                                                                                 -25     -4.2    +26
                                                               1V internal Ref
                                                               Vddana=3.0V
                                                                                 -27     -3.1    +24
                                                               Vref=Vddana/2
  SFDR       Spurious Free Dynamic Range                                         67.9    69.2    76.3
             Signal to Noise and Distortion   Fs = 1Msps
  SINAD                                                        Vddana=3.0V       55.6    57.5    61.1
                          ratio               Fin = 14kHz                                                dB
                                                   (2)         Vref=Vddana
   SNR             Signal to Noise ratio                                         54.7    56.9    60.6
   THD          Total Harmonic Distortion                                        -73.7   -68.2   -65.8
                                                               Vddana=3.0V
                                                                                 0.3     1.0      2.3
                                              constant input   ExtVref=2.0V
   Nrms                 Noise RMS                                                                        mV
                                                 voltage       Vddana=3.0V
                                                                                 0.1     0.35    2.45
                                                               Vref=Vddana

Note:
 1. These values are based on characterization. These values are not covered by test limits in
      production.
 2. All values expressed in decibel refer to the full scale input and are tested with an input signal
      0.35dB below full scale; THD measured on the first seven harmonics of the input signal.
 3. With REFCTRL.REFCOMP=1 and SAMPCTRL.OFFCOMP=1.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 2064
                                                               SAM D5x/E5x Family Data Sheet
                                                                            Electrical Characteristics at 125°C

         Table 56-13. Power Consumption

          Symbol         Parameters         Conditions                                   Ta         Typ. Max Units
          IDD VDDANA Differential           fs = 1 Msps / Reference buffer disabled / Max 125°C 279 848         µA
                     mode                   BIASREFBUF = '111', BIASREFCOMP = Typ 25°C
                                            '111' VDDANA = VREF = 3.0V
                                            fs = 1 Msps / Reference buffer enabled /                482 1381
                                            BIASREFBUF = '111', BIASREFCOMP =
                                            '111' VDDANA = VREF = 3.0V
                                            fs = 10 ksps / Reference buffer disabled /              28    91
                                            BIASREFBUF = '111', BIASREFCOMP =
                                            '111' VDDANA = VREF = 3.0V
                                            fs = 10 ksps / Reference buffer enabled /               241 807
                                            BIASREFBUF = '111', BIASREFCOMP =
                                            '111' VDDANA = VREF = 3.0V
                         Single Ended       fs = 1 Msps / Reference buffer disabled / Max 125°C 307 820         µA
                         mode               BIASREFBUF = '111', BIASREFCOMP = Typ 25°C
                                            '111' VDDANA = VREF = 3.0V
                                            fs = 1 Msps / Reference buffer enabled /                499 1156
                                            BIASREFBUF = '111', BIASREFCOMP =
                                            '111' VDDANA = VREF = 3.0V
                                            fs = 10 ksps / Reference buffer disabled /              38    108
                                            BIASREFBUF = '111', BIASREFCOMP =
                                            '111' VDDANA = VREF = 3.0V
                                            fs = 10 ksps / Reference buffer enabled /               245 881
                                            BIASREFBUF = '111', BIASREFCOMP =
                                            '111' VDDANA = VREF = 3.0V

56.6.4   Digital-to-Analog Converter (DAC) Characteristics (125°C)
Table 56-14. Differential Mode (1)

Symbol                Parameters                                  Conditions                      Min. Typ. Max.      Unit
                                                 i12clk = 12 MHz, VDDANA = 3.0V, External Ref.
               Integral Non Linearity,                                                             -     ±2.4 ±4.1
                                                             = 2.0V, CLOAD = 50 pF
  INL        Best-fit curve from 0x080 to                                                                             LSB
                         0xF7F                   i12clk = 12 MHz, VDDANA = 3.0V, Internal Ref ,
                                                                                                   -     ±3.2 ±4.2
                                                                CLOAD = 50 pF
                                                i12clk = 12 MHz, VDDANA = 3.0V,External Ref. =
              Differential Non Linearity,                                                          -     ±2.4 ±4.5
                                                             2.0V, CLOAD = 50 pF
  DNL        Best-fit curve from 0x080 to                                                                             LSB
                         0xF7F                   i12clk = 12 MHz, VDDANA = 3.0V, Internal Ref ,
                                                                                                   -     ±3.5 ±5.4
                                                                CLOAD = 50 pF
                                                           External Reference voltage              -     ±0.4 ±1.9
  Gerr                 Gain Error                                                                                    % FSR
                                                         1.0V Internal Reference voltage           -     ±0.8 ±8.5




         © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 2065
                                                           SAM D5x/E5x Family Data Sheet
                                                                         Electrical Characteristics at 125°C

...........continued
Symbol                  Parameters                             Conditions                     Min. Typ. Max.        Unit
                                                       External Reference voltage               -    ±13     ±47
  Offerr                Offset Error                                                                                  mV
                                                     1.0V Internal Reference voltage            -     ±8     ±79
 ENOB            Effective Number of Bits                                                      9.9   10.7 10.9
  SNR              Signal to Noise ratio         Fs = 1Ms/s - External Ref - CCTRL=0x2        63.5 68.6 72.6          dB
  THD            Total Harmonic Distortion                                                    -79.1 -72.5 -61.0

           Note:
            1. These values are based on characterization. These values are not covered by test limits in
                 production.
Table 56-15. Single-Ended Mode (1)

Symbol                  Parameters                             Conditions                     Min. Typ. Max.        Unit
                                              i12clk = 12 MHz, VDDANA = 3.0V External Ref.
                 Integral Non Linearity,                                                        -    ±2.7   ±6.0
                                                          = 2.0V, CLOAD = 50 pF
   INL         Best-fit curve from 0x080 to                                                                          LSB
                           0xF7F              i12clk = 12 MHz VDDANA = 3.0V, Internal Ref ,
                                                                                                -    ±5.2 ±11.2
                                                            CLOAD = 50 pF
                                              i12clk = 12 MHz, VDDANA = 3.0V External Ref =
                Differential Non Linearity,                                                     -    ±3.5   ±8.1
                                                           2.0V, CLOAD = 50 pF
  DNL          Best-fit curve from 0x080 to                                                                          LSB
                           0xF7F               i12clk = 12 MHz VDDANA = 3.0V, Internal Ref,
                                                                                                -    ±6.4 ±12.1
                                                             CLOAD = 50 pF
                                                       External Reference voltage               -    ±0.3   ±1.6
  Gerr                   Gain Error                                                                                 % FSR
                                                     1.0V Internal Reference voltage            -    ±0.8   ±8.6
                                                       External Reference voltage               -    ±7     ±25.5
  Offerr                 Offset Error                                                                                 mV
                                                     1.0V Internal Reference voltage            -    ±2     ±19
 ENOB            Effective Number of Bits                                                     9.1    10.3   10.7
  SNR              Signal to Noise ratio         Fs = 1Ms/s - External Ref - CCTRL=0x2        63.5 68.6     72.6      dB
  THD            Total Harmonic Distortion                                                    -79.1 -72.8 -61.0

           Note:
            1. These values are based on characterization. These values are not covered by test limits in
                 production.




           © 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 2066
                                                            SAM D5x/E5x Family Data Sheet
                                                                        Electrical Characteristics at 125°C

Table 56-16. Power Consumption

Symbol Parameters                              Conditions                          Ta           Min. Typ. Max. Unit
IDDANA    Differential Mode, DC supply         fs = 1 Msps, CCTR L= 0x2, VREF >    Max. 125°C     -    384   634     µA
          current, 2 output channels -         2.4V, VCC = 3.3V                    Typ. 25°C
          without load
                                               fs = 10 ksps, CCTRL = 0x0, VREF <                  -    283   482
                                               2.4V, VCC = 3.3V
          Single-Ended Mode, DC supply         fs = 1 Msps, CCTRL = 0x2, VREF >                   -    306   517     µA
          current, 2 output channels -         2.4V, VCC = 3.3V
          without load
                                               fs = 10 ksps, CCTRL = 0x0, VREF <                  -    230   389
                                               2.4V, VCC = 3.3V

56.6.5   Analog Comparator (AC) Characteristics (125°C)
         Table 56-17. Analog Comparator Characteristics

          Symbol Parameters                         Conditions                           Min Typ Max Unit
          Off(1)     Offset                         High speed COMPCTRLn.SPEED =         -22 ±3        22    mV
                                                    0x3
          Tpd        Propagation Delay              High speed COMPCTRLn.SPEED =         -       24.1 42     ns
                     Vcm=Vddana/2, Vin =            0x3
                     +/-100mV overdrive from
                     Vcm
          Tstart     Startup time                   High speed COMPCTRLn.SPEED =         -       4.7   8     µs
                                                    0x3

         Note:
          1. Hysteresis disabled.
Table 56-18. Power Consumption

Symbol Parameters                                    Conditions                         Ta             Typ. Max. Unit
IDDANA    Current consumption for                    COMPCTRLn.SPEED=0x3,               Max.125°C 59         106     µA
          One AC enabled,                            VDDANA=3.3V                        Typ.25°C
          Hysteresis disabled
          voltage scaler disabled
          Current consumption Voltage Scaler only VDDANA=3.3V                                          11    23.3

56.6.6   PTC Characteristics
         The values in the following Power Consumption table are measured values of power consumption under
         the following conditions:
         Operating Conditions:
         VDD = 3.0V
         Clocks
         DFLL48M used as main clock source, running undivided at 48 MHz




         © 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 2067
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                Electrical Characteristics at 125°C

       CPU is running on Flash with 2 wait states, at 48 MHz
       PTC running at 4 MHz
       PTC Configuration
       Mutual Capacitance mode
       One touch channel
       System Configuration
       Standby Sleep mode enabled
       RTC running on ULP32K: used to define the PTC scan rate, through the event system
       RTC interrupts (wake up) the CPU to perform PTC scans
       Table 56-19. Power Consumption (1)

                                               PTC scan
        Symbol           Parameters                             Oversamples                TA           Typ. Max. Units
                                              rate (msec)
                                                                       4                                137 3960
                                                    10
                                                                      16                                146 3989
                                                                       4                                 77      3882
                                                    50
                                                                      16           Max. 125°C Typ        79      3893
           IDD     Current Consumption                                                                                    µA
                                                                       4                25°C             68      3877
                                                   100
                                                                      16                                 69      3885
                                                                       4                                 64      3870
                                                   200
                                                                      16                                 65      3872

       Note:
        1. These values are based on characterization.



56.7   NVM Characteristics (125°C)
       Table 56-20. NVM Flash Read Wait States for Worst Case Conditions

         CPU Fmax (MHz)           0 WS       1 WS         2 WS        3 WS       4 WS       5 WS       6 WS       Auto WS
          Read Operations         1 cycle   2 cycles     3 cycles    4 cycles   5 cycles   6 cycles   7 cycles     n cycles
            VDD > 1.71V             19        38           57          76         95            100     100             100

       Maximum operating frequencies are given in the table above, but are limited by the Embedded Flash
       access time when the processor is fetching code out of it. Theses tables provide the device maximum
       operating frequency defined by the field RWS of the NVMCTRL CTRLA register when automatic wait
       states (AUTOWS) is disabled. This field defines the number of Wait states required to access the
       Embedded Flash Memory.




       © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 2068
                                                              SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 125°C


56.8     Oscillators Characteristics (125°C)

56.8.1   Crystal Oscillator (XOSC) Characteristics (125°C)
         Table 56-21. Multiple Crystal Oscillator Characteristics

          Symbol Parameter           Conditions                                        Min. Typ.     Max       Units
                                     F = 8MHz - CL=20 pF - Cshunt = 2 pF -             -      39700 72200
                                     IMULT=0x3
                                     F = 16MHz - CL=20 pF - Cshunt = 1,5 pF -          -      37550 73000
                                     IMULT=0x4
            Tstart   Startup time                                                                              Cycles
                                     F = 24MHz - CL=20 pF - Cshunt = 2,5 pF -          -      32700 71000
                                     IMULT=0x5
                                     F = 48MHz - CL=13 pF - Cshunt = 5 pF -            -      18400 38500
                                     IMULT=0x6

         Table 56-22. Power Consumption

          Symbol Parameters                 Conditions                          Ta                 Typ. Max. Units
          IDD        Current                F = 8 MHz - CL = 20 pF - IMULT =    Max. 125°C,        0.43 2.27     mA
                     Consumption            0x3, ENALC = OFF                    Typ. 25°C
                                            ENALC = ON                                             0.16 1.87
                                            F = 16 MHz - CL = 20 pF - IMULT =                      1.31 3.72
                                            0x5, ENALC = OFF
                                            ENALC = ON                                             0.25 2.23
                                            F = 32 MHz - CL = 13 pF - IMULT =                      2.92 6.49
                                            0x5, ENALC = OFF
                                            ENALC = ON                                             0.40 2.43
                                            F = 48 MHz - CL = 13 pF - IMULT =                      2.70 6.71
                                            0x6, ENALC = OFF
                                            ENALC = ON                                             0.76 3.52

56.8.2   External 32 kHz Crystal Oscillator (XOSC32K) Characteristics (125°C)
Table 56-23. 32 kHz Crystal Oscillator Electrical Characteristics
Symbol          Parameter                                Conditions                    Min.   Typ.      Max.       Units

tSTARTUP        Startup time                             f=32.768  Std. Gain           -      12        32         kCycles
                                                         kHz,
                                                         CL=12.5
                                                         pF,
                                                         CM=2.0 fF




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 2069
                                                                SAM D5x/E5x Family Data Sheet
                                                                              Electrical Characteristics at 125°C

         Table 56-24. Power Consumption

          Symbol          Parameter Condition         Ta            Gain Mode Typ.            Max.            Units
                                    s
          IDD             Current    VDD=3.0V         Max 125°C Std.             1.5          2.6             µA
                          consumptio                  Typ 25°C
                                                                High             1.9          3.4
                          n

56.8.3 Internal Ultra Low Power 32 kHz RC Oscillator (OSCULP32K) Characteristics (125°C)
Table 56-25. Ultra-Low-Power Internal 32 kHz RC Oscillator Electrical Characteristics

Symbol Parameter                Calibration                   Conditions                            Min.    Typ.      Max      Units
FOUT      Output frequency Factory default & without          [-40, +125]°C, VDDANA>1.71V           26.00 32.768 40.92 kHz
                           user software calibration
                                With user software            Recalibrate using XOSC as             32.28             33.4
                                calibration                   reference Clock source
                                                              Recalibrate using DFLL as             31.29             34.24
                                                              reference Clock source

56.8.4   Digital Frequency Locked Loop (DFLL48M) Characteristics (125°C)
Table 56-26. DFLL48M Characteristics - Open Loop Mode (1)
Symbol            Parameter                   Conditions                                    Min.       Typ.    Max.          Units

FOpenOUT          Output frequency            DFLLVAL after Reset                           45.57      48      50.63         MHz
                                              LDO Regulator mode, [-40, 125]°C

                                              DFLLVAL after Reset                           47.12      48      48.9
                                              LDO Regulator mode, [0, 60]°C


         Note:
          1. DFLL48 in open loop can be used only with LDO regulator.
Table 56-27. DFLL48M Power Consumption

Symbol Parameter                     Conditions                                        Ta              Min. Typ. Max. Units
IDD       Current Consumption Open Loop mode - DFLLVAL after reset VCC =               Max. 125°C -           400 2129 µA
                              3.3V                                                     Typ. 25°C
                                     Closed Loop mode - fREF = 32 .768 kHz VCC =                       -      404 2113 µA
                                     3.3V




         © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 2070
                                                              SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 125°C

56.8.5   Fractional Digital Phase Lock Loop (FDPLL) Characteristics (125°C)
         Table 56-28. Fractional Digital Phase Lock Loop Characteristics (1)

          Symbol Parameter                                Conditions                           Min. Typ. Max. Units
          Jp          Period jitter (Peak-Peak value)     fIN = 32 kHz, fOUT = 96 MHz           -      1.9     3.0        %
                                                          fIN = 32 kHz, fOUT = 200 MHz          -      3.4     6.0
                                                          fIN = 3.2 MHz, fOUT = 96 MHz          -      2.0     3.1
                                                          fIN = 3.2 MHz, fOUT = 200 MHz         -      4.3     7.2

         Note:
          1. These FDPLL200M characteristics are applicable with LDO regulator and a direct reference (i.e.,
               REFCLK is XOSC or XOSC32K, not GCLK).
Table 56-29. Power Consumption

Symbol          Parameter                    Conditions                           TA                    Typ.     Max.         Units
IDD             Current Consumption          Ck = 96 MHz, VDD = 3.3V              Max. 125°C            0.9      2.5          mA
                                                                                  Typ. 25°C
                                             Ck = 200 MHz, VDD = 3.3V                                   2.0      3.4



56.9     Timing Characteristics (125°C)

56.9.1   SERCOM in SPI Mode Timing (125°C)
         Table 56-30. SPI Timing Characteristics and Requirements(1)

          Symbol         Parameter                        Conditions                    Min.    Typ.     Max.        Units
          tMIS           MISO setup to SCK                Master, VDD>2.70V             19.5    -        -           ns
                                                          Master, VDD>1.71V             20      -        -
          tSOV           MISO output valid SCK            Slave, VDD>2.70V              16.5    -        -           ns
                                                          Slave, VDD>1.71V              25      -        -

           1.     These values are based on simulation, with capacitance load between 5pF and 20pF. These values
                  are not covered by test limits in production.




         © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 2071
