# 55. Electrical Characteristics at 105°C

*Source: `Atmel-SAMD51.pdf`, pages 2035-2052 — SAMD51 family datasheet*

                                                             SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 105°C


55.      Electrical Characteristics at 105°C
         The specifications for 105°C temperature devices are identical to those shown in 54. Electrical
         Characteristics at 85°C, with the exception of the parameters listed in this chapter.



55.1     General Operating Ratings (105°C)
         The device must operate within the ratings listed below in order for all other electrical characteristics and
         typical characteristics of the device to be valid.
Table 55-1. General Operating Conditions

Symbol                 Description                                  Min.            Typ.             Max.           Units
TA                     Temperature range                            -40             25               105            °C
TJ                     Junction temperature                         -               -                125            °C



55.2     Supply Characteristics (105°C)
         Table 55-2. Power Supply Current Requirement

          Symbol               Conditions                                                Current            Units
                                                                                         Max
          Iinput               Power-up Maximum Current                                  10                 mA

         Note: Iinput is the minimum requirement for the power supply connected to the device.



55.3     Power Consumption (105°C)
         The values in this section are measured values of power consumption under the following conditions,
         except where noted:
          • Operating Conditions
              – CPU is running on Flash with automatic wait state
              – Low power cache enabled
              – BOD33 is disabled
              – I/Os are inactive input mode, with input trigger disabled
          • Oscillators
              – XOSC0 (crystal oscillator) running with external 32 MHz crystal
              – XOSC32K (32 kHz crystal oscillator) running with external 32 kHz crystal in LP mode
              – FDPLL is using XOSC32K as reference on LDO and external clock 32768 on Buck mode
              – DFLL48M is using XOSC32K as reference




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 2035
                                                     SAM D5x/E5x Family Data Sheet
                                                                    Electrical Characteristics at 105°C

Table 55-3. Active Current Consumption - Active Mode

 Mode       conditions             Regulator Clock         VDD TA                         Typ. Max Units

                                                FDPLL       1.8                           136 191
                                               120MHz       3.3                           137 193
                                                            1.8                           136 271
                                     LDO     DFLL 48MHz
                                                            3.3                           136 272
                                                            1.8                           146 346
                                             XOSC 32MHz
                                                            3.3                           149 347
 ACTIVE COREMARK (1)
                                                FDPLL       1.8                           103 151
                                               120MHz       3.3                            65   133
                                                            1.8                           102 225
                                    BUCK     DFLL 48MHz
                                                            3.3                            63   169
                                                            1.8                            110 283
                                             XOSC 32MHz
                                                            3.3     Max at 105°C Typ at    73   224
                                                                                                       uA/Mhz
                                                            1.8            25°C            21    78
                                                FDPLL
                                               120MHz       3.3                            23    81
                                                            1.8                            21   156
                                     LDO     DFLL 48MHz
                                                            3.3                            21   156
                                                            1.8                            25   231
                                             XOSC 32MHz
                                                            3.3                            27   233
   IDLE             NA
                                                FDPLL       1.8                            16    59
                                               120MHz       3.3                            11    54
                                                            1.8                            16    119
                                    BUCK     DFLL 48MHz
                                                            3.3                            10    85
                                                            1.8                            21   180
                                             XOSC 32MHz
                                                            3.3                            19   135

Note:
 1. System Configuration used:
      – MCLK all APB clocks masked except MCLK and NVMCTRL
      – MCLK.AHBMASK = 0x00C00FFF
      – CMCC enabled




© 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 2036
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                   Electrical Characteristics at 105°C

Table 55-4. Standby, Hibernate, Backup and OFF Mode Current Consumption
   Mode                              Conditions                         Regulator Mode   VCC              TA               Typ.   Max.   Units

                                                                                         1.8V                              43     3316
                  fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),          LDO
                                    no peripheral running                                3.3V                              43     3322
                 No System RAM retained (PM.STDBYCFG.RAMCFG=0x2).
                                                                                         1.8V                              26     2211
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              17     1581

                                                                                         1.8V                              85     5106
                  fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),           LDO
                                   no peripheral running                                 3.3V                              85     5110
                 No System RAM retained (PM.STDBYCFG.RAMCFG=0x2).
                                                                                         1.8V                              65     3907
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              47     2756

                                                                                         1.8V                              43     3322
                  fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),          LDO
                                  RTC running on XOSC32K                                 3.3V                              44     3329
                 No System RAM retained (PM.STDBYCFG.RAMCFG=0x2).
                                                                                         1.8V                              26     2218
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              18     1587

                                                                                         1.8V                              45     3462
                  fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),          LDO
                              RTC running on XOSC32K 32KB                                3.3V                              46     3469
 STANDBY                                                                                        Max at 105°C Typ at 25°C                  µA
                   System RAM retained (PM.STDBYCFG.RAMCFG=0x1).
                                                                                         1.8V                              27     2311
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              19     1652

                                                                                         1.8V                              53     3997
                  fast wake-up disabled (PM.STDBYCFG.FASTWKUP=0x0),          LDO
                                  RTC running on XOSC32K                                 3.3V                              53     4003
                 Full System RAM retained (PM.STDBYCFG.RAMCFG=0x0).
                                                                                         1.8V                              32     2668
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              22     1903

                                                                                         1.8V                              101    3126
                  fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),           LDO
                                   no peripheral running                                 3.3V                              101    3140
                 Full System RAM retained (PM.STDBYCFG.RAMCFG=0x0).
                                                                                         1.8V                              78     2375
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              55     1659

                                                                                         1.8V                              102    3132
                  fast wake-up enabled (PM.STDBYCFG.FASTWKUP=0x3),           LDO
                                 RTC running on XOSC32K                                  3.3V                              103    3146
                 Full System RAM retained (PM.STDBYCFG.RAMCFG=0x0).
                                                                                         1.8V                              79     2383
                               8KB backup RAM retained                      BUCK
                                                                                         3.3V                              56     1666




          © 2019 Microchip Technology Inc.                            Datasheet                                DS60001507E-page 2037
                                                                                 SAM D5x/E5x Family Data Sheet
                                                                                              Electrical Characteristics at 105°C

...........continued
     Mode                                    Conditions                            Regulator Mode   VCC              TA               Typ.    Max.   Units

                                                                                                    1.8V                               6      168
                                                                                        LDO
                                       no peripheral running
                                                                                                    3.3V                               6      170
                         No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                         No backup RAM retained (PM.HIBCFG.BRAMCFG=0x2)                             1.8V                               3      111
                                                                                       BUCK
                                                                                                    3.3V                               3      111

                                                                                                    1.8V                               6      169
                                                                                        LDO
                                    RTC is running on XOSC32K
                                                                                                    3.3V                               7      172
                         No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                         No backup RAM retained (PM.HIBCFG.BRAMCFG=0x2)                             1.8V                               3      113
                                                                                       BUCK
                                                                                                    3.3V                               3      112

                                                                                                    1.8V                               7      193
                                                                                        LDO
                                    RTC is running on XOSC32K
                                                                                                    3.3V                               8      196
                         No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                        4KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x1)                             1.8V                               3      129
                                                                                       BUCK
                                                                                                    3.3V                               4      128
  HIBERNATE                                                                                                Max at 105°C Typ at 25°C                   µA
                                                                                                    1.8V                               7      217
                                                                                        LDO
                                    RTC is running on XOSC32K
                                                                                                    3.3V                               8      219
                         No System RAM retained (PM.HIBCFG.RAMCFG=0x2)
                        8KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x0)                             1.8V                               4      144
                                                                                       BUCK
                                                                                                    3.3V                               4      143

                                                                                                    1.8V                               9      350
                                                                                        LDO
                                    RTC is running on XOSC32K
                                                                                                    3.3V                               10     352
                        32KB System RAM retained (PM.HIBCFG.RAMCFG=0x1)
                        8KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x0)                             1.8V                               5      233
                                                                                       BUCK
                                                                                                    3.3V                               4      228

                                                                                                    1.8V                               16     873
                                                                                        LDO
                                      RTC is running on XOSC32K
                                                                                                    3.3V                               17     874
                         Full System RAM retained (PM.HIBCFG.RAMCFG=0x0)
                        8KB backup RAM retained (PM.HIBCFG.BRAMCFG=0x0)                             1.8V                               9      580
                                                                                       BUCK
                                                                                                    3.3V                               7      431

                                         powered by VDDIO,                                          1.8V                               2.1    160
                             no RTC running VDDIO+VDDANA consumption
                        No backup RAM retained (PM.BKUPCFG.BRAMCFG=0x2)                             3.3V                               2.5    162

                                powered by VDDIO with RTC running on                                1.8V                               2.7    161
                               XOSC32K VDDIO+VDDANA consumption
                        No backup RAM retained (PM.BKUPCFG.BRAMCFG=0x2)                             3.3V                               3.3    164

                                         powered by VDDIO,                                          1.8V                               2.4    183
    BACKUP                   no RTC running VDDIO+VDDANA consumption                                                                                  µA

                       4KB backup RAM retained (PM.BKUPCFG.BRAMCFG=0x1)                             3.3V                               2.8    185
                                                                                       BUCK                Max at 105°C Typ at 25°C

                                         powered by VDDIO,                                          1.8V                               2.7    207
                             no RTC running VDDIO+VDDANA consumption
                       8KB backup RAM retained (PM.BKUPCFG.BRAMCFG=0x0)                             3.3V                               3.1    209

                                                                                                    1.8V                               2.7    161
                       Battery Backup mode powered by VBAT with RTC running on
                                                                                                    3.3V                               3.3    164

                                                                                                    1.8V                              0.191    11
      OFF                                         -                                                                                                   µA
                                                                                                    3.3V                              0.331    13




              © 2019 Microchip Technology Inc.                                   Datasheet                                DS60001507E-page 2038
                                                             SAM D5x/E5x Family Data Sheet
                                                                           Electrical Characteristics at 105°C


55.4     Analog Characteristics (105°C)

55.4.1   Power-On Reset (POR) Characteristics (105°C)
         Table 55-5. POR Characteristics

          Symbol          Parameters                                                Min.   Typ.   Max.     Unit
          VPOT+           Voltage threshold Level on VDDIO rising                   1.52   1.58   1.65     V
          VPOT-           Voltage threshold Level on VDDIO falling                  0.97   1.26   1.36     V

         Figure 55-1. POR Operating PrincipleVDD




                                           VPOT+
                                           VPOT-



                                                                                    Time
                                             Reset




         Note: The shaded area indicates that the device is in a Reset state.

55.4.2   Brown-Out Detectors (BOD) Characteristics (105°C)
         Figure 55-2. BOD33 Hysteresis OFF

                                     VCC
                                                      VBOD



                                  RESET

         Figure 55-3. BOD33 Hysteresis ON

                                     VCC                                    VBOD+
                                                     VBOD-



                                  RESET




         © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 2039
                                                   SAM D5x/E5x Family Data Sheet
                                                                 Electrical Characteristics at 105°C

Table 55-6. BOD33 Characteristics on VDD and VBAT Monitoring in Normal Mode (During Power-up
Phase and Active Mode)

 Symbol                   Parameters         Conditions (3, 4)      Min     Typ       Max        Unit
 VBOD or VBOD- (1) BOD33 threshold           LEVEL[7:0] = 0x00     1.453    1.509     1.554       V
                   level Hysteresis          (min)
                   OFF or BOD33
                                             LEVEL[7:0] = 0x19     1.598    1.658     1.708
                   threshold level
                                             (recommended
                   Hysteresis ON
                                             value)
                                             LEVEL[7:0]= 0x1C      1.616    1.676     1.726
                                             (fuse value)
                                             LEVEL[7:0] = 0xFF     2.925    3.040     3.133
                                             (max)
 VBOD+ (2)                BOD33 threshold    LEVEL[7:0] = 0x00     1.463    1.520     1.565
                          level Hysteresis   (min)
                          ON at power
                                             LEVEL[7:0]= 0x19      1.607    1.669     1.719
                          voltage rising
                                             (recommended
                                             value)
                                             LEVEL[7:0] = 0x1C     1.625    1.687     1.737
                                             (fuse value)
                                             LEVEL[7:0] = 0xFF     2.932    3.041     3.316
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




© 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 2040
                                                  SAM D5x/E5x Family Data Sheet
                                                                 Electrical Characteristics at 105°C

Table 55-7. BOD33 Characteristics on VDD and VBAT Monitoring in Low-Power Mode (During
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




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 2041
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                         Electrical Characteristics at 105°C

            Table 55-8. BOD33 Power Consumption

             Symbol CPU Mode                                           Conditions TA                                    Typ.    Max      Units
             IDD         Active / Idle                                 VCC = 1.8V Max 105°C Typ 25°C 8.52                       13.26 µA
                                                                       VCC = 3.3V                                       10.10 15.70
                         Standby with BOD continuous                   VCC = 1.8V                                       4.71    6.74
                         normal mode
                                                                       VCC = 3.3V                                       6.01    8.59
                         Standby with BOD continuous low               VCC = 1.8V                                       0.15    0.25
                         power mode or Hibernate mode
                                                                       VCC = 3.3V                                       0.21    0.33

55.4.3 Analog-to-Digital Converter (ADC) Characteristics (105°C)
Table 55-9. Operating Conditions (1)
 Symbol                           Parameters                                Conditions                Min          Typ                 Max       Unit

  Res                              Resolution                                                           -           -                  12         bits

                                                                 resolution 12 bit (CTRLC.RESSEL=0)    20           -                  1231      ksps
                        Sampling rate - Differential mode
                          SAMPCTRL.OFFCOMP = 0                   resolution 10 bit (CTRLC.RESSEL=2)   29.09         -                  1455      ksps
                           REFCTRL.REFCOMP = 0
                                                                 resolution 8 bit (CTRLC.RESSEL=3)    35.56         -                  1778      ksps
  Fcnv
                                                                 resolution 12 bit (CTRLC.RESSEL=0)    20           -                  1231      ksps
                       Sampling rate - Single-Ended mode
                          SAMPCTRL.OFFCOMP = 0                   resolution 10 bit (CTRLC.RESSEL=2)   26.67         -                  1333      ksps
                           REFCTRL.REFCOMP = 0
                                                                 resolution 8 bit (CTRLC.RESSEL=3)     32           -                  1600      ksps

                                                                 resolution 12 bit (CTRLC.RESSEL=0)                        16
                 Differential mode Number of ADC clock cycles
                                                                 resolution 10 bit (CTRLC.RESSEL=2)                        14                    cycles
             SAMPCTRL.OFFCOMP=1 and/or REFCTRL.REFCOMP=1
                                                                 resolution 8 bit (CTRLC.RESSEL=3)                         12

                  Differential mode Number of ADC clock cycles   resolution 12 bit (CTRLC.RESSEL=0)                 SAMPLEN+13
                SAMPCTRL.OFFCOMP=0 REFCTRL.REFCOMP=0
                                                                 resolution 10 bit (CTRLC.RESSEL=2)                 SAMPLEN+11                   cycles
                  SAMPLEN corresponds to the decimal value of
                        SAMPCTRL.SAMPLEN[5:0] register           resolution 8 bit (CTRLC.RESSEL=3)                  SAMPLEN+9
Nb_cycles
                                                                 resolution 12 bit (CTRLC.RESSEL=0)                        16
                Single-ended mode Number of ADC clock cycles
                                                                 resolution 10 bit (CTRLC.RESSEL=2)                        15                    cycles
             SAMPCTRL.OFFCOMP=1 and/or REFCTRL.REFCOMP=1
                                                                 resolution 8 bit (CTRLC.RESSEL=3)                         13

                 Single-ended mode Number of ADC clock cycles    resolution 12 bit (CTRLC.RESSEL=0)                 SAMPLEN+13
                SAMPCTRL.OFFCOMP=0 REFCTRL.REFCOMP=0
                                                                 resolution 10 bit (CTRLC.RESSEL=2)                 SAMPLEN+12                   cycles
                  SAMPLEN corresponds to the decimal value of
                       SAMPCTRL.SAMPLEN[5:0] register            resolution 8 bit (CTRLC.RESSEL=3)                  SAMPLEN+10

  fadc                       ADC Clock frequency                                                      320     Fcnv*Nb_cycles       16000          kHz

                                                                     SAMPCTRL.OFFCOMP=1
                                                                      REFCTRL.REFCOMP=1                                    4
                                                                         CTRLC.R2R=1
   Ts                            Sampling time                                                                                                   cycles
                                                                    SAMPCTRL.OFFCOMP=0 (3)
                                                                      REFCTRL.REFCOMP=0                1            -                   65
                                                                         CTRLC.R2R=0




            © 2019 Microchip Technology Inc.                             Datasheet                                      DS60001507E-page 2042
                                                                                SAM D5x/E5x Family Data Sheet
                                                                                                  Electrical Characteristics at 105°C

...........continued
  Symbol                              Parameters                                     Conditions                  Min         Typ                       Max               Unit

                                                                              SAMPCTRL.OFFCOMP=1
                                                                               REFCTRL.REFCOMP=1
                                                                                  CTRLC.R2R=1
     Ts                     Sampling time with DAC as input                                                                             (4)                              ns
                                                                            SAMPCTRL.OFFCOMP=0 (3)
                                                                              REFCTRL.REFCOMP=0
                                                                                 CTRLC.R2R=0

                                                                              SAMPCTRL.OFFCOMP=1
                                                                               REFCTRL.REFCOMP=1                10000            -              4/fadcmin=25000
                                                                                  CTRLC.R2R=1
     Ts            Sampling time with Temp Sensor or Bandgap as input                                                                                                    ns
                                                                            SAMPCTRL.OFFCOMP=0 (3)
                                                                              REFCTRL.REFCOMP=0                 10000            -             65/fadcmin=406250
                                                                                 CTRLC.R2R=0

                                                                                  Differential mode             -VREF            -                   +VREF
    Vcnv                            Conversion range                                                                                                                      V
                                                                                 Single-ended mode                0              -                    VREF

    Vref                             Reference input                                                              1              -                VDDANA-0.4              V

     Vin                           Input channel range                                                            0              -                  VDDANA                V

                                                                                   CTRLC.R2R=1                    0        +VREF/2                  VDDANA                V
   Vcmin                      Input common mode voltage
                                                                                   CTRLC.R2R=0                                       See Note 2                           V

 CSAMPLE                       Input sampling capacitance                                                         2          2.5                           3             pF

 RSAMPLE                      Input sampling on-resistance                                                         -                                  2000                Ω

    Rref                      Reference source resistance                                                                        -                        2.5            kΩ


               Note:
                1. These are based on simulation. These values are not covered by test or characterization.
                2. Limit the input common mode voltage using following equations (where VCM_IN is the input
                     channel common mode voltage):
                     When CTRLC.R2R=0,
                         – VCM_IN < 0.75*VREF
                         – VCM_IN > Maximum of (0, VREF-VDDANA-0.7, 1.25*VREF-VDDANA)
                 3.    When OFFCOMP is disabled, Ts is function of SAMPLEN[5:0] register value, ie Ts=(SAMPLEN+1)/
                       fadc.
                 4.    See Ts specified in DAC electrical characteristic.
Table 55-10. Differential Mode (1)
                                                                                                                                               Measurement
 Symbol                          Parameter                                               Conditions                                                                      Unit
                                                                                                                                        Min        Typ          Max

                                                                                                      Vddana=3.0V Vref=Vddana           10.5       10.8         11.2
  ENOB                     Effective Number of bits              Fadc = 1Msps - R2R disabled
                                                                                                      Vddana=3.0V ExtVref=2.0V          10.5       10.8         11.0

                                                                                                      Vddana=3.0V Vref=Vddana            -        +/-2.3        +/-5.2
   TUE                    Total Unadjusted Error (3)             Fadc = 1Msps - R2R disabled
                                                                                                      Vddana=3.0V ExtVref=2.0V           -        +/-2.7        +/-5.7

                                                                                                      Vddana=3.0V Vref=Vddana            -        +/-1.2        +/-1.7
    INL                     Integral Non Linearity               Fadc = 1Msps - R2R disabled
                                                                                                      Vddana=3.0V ExtVref=2.0V           -        +/-1.2        +/-1.5

                                                                                                      Vddana=3.0V Vref=Vddana            -        +/-0.98       -1/+1
   DNL                    Differential Non Linearity             Fadc = 1Msps - R2R disabled
                                                                                                      Vddana=3.0V ExtVref=2.0V           -        +/-0.96       -1/+1




              © 2019 Microchip Technology Inc.                                    Datasheet                                          DS60001507E-page 2043
                                                                             SAM D5x/E5x Family Data Sheet
                                                                                                Electrical Characteristics at 105°C

...........continued
                                                                                                                                          Measurement
 Symbol                            Parameter                                              Conditions                                                           Unit
                                                                                                                                   Min       Typ      Max

                                                                                                  Vddana=3.0V Vref=Vddana         -0.21     -0.02     +0.2

                                                                                                  Vddana=3.0V ExtVref=2.0V        -0.12     +0.03    -0.21
   Gain            Gain Error with REFCTRL.REFCOMP=1                 Fadc = 1Msps                                                                               %
                                                                                                  Vddana=3.0V 1V internal Ref      -10        -1      +6.7

                                                                                                  Vddana=3.0V Vref=Vddana/2       -0.48     +0.2     +0.75

                                                                                                  Vddana=3.0V Vref=Vddana          -0.3     -0.001    +0.2

                                                                                                  Vddana=3.0V ExtVref=2.0V        -0.94     -0.05       -0.7
   Gain            Gain Error with REFCTRL.REFCOMP=0                 Fadc = 1Msps                                                                              mV
                                                                                                  Vddana=3.0V 1V internal Ref      -10        -1      +5.9

                                                                                                  Vddana=3.0V Vref=Vddana/2        -1.2     +0.11    +1.28

                                                                                                  Vddana=3.0V Vref=Vddana          -3.6     -0.24     +3.1

                                                                                                  Vddana=3.0V ExtVref=2.0V         -3.3      -0.2     +2.7
   Offset         Offset Error with SAMPCTRL.OFFCOMP=1               Fadc = 1Msps                                                                               %
                                                                                                  Vddana=3.0V 1V internal Ref      -3.6      -0.2     +2.9

                                                                                                  Vddana=3.0V Vref=Vddana/2        -3.6     -0.34     +3.3

                                                                                                  Vddana=3.0V Vref=Vddana         -11.9     +0.03    +/-12.3

                                                                                                  Vddana=3.0V ExtVref=2.0V        -12.2     -0.03    +12.4
   Offset         Offset Error with SAMPCTRL.OFFCOMP=0               Fadc = 1Msps                                                                              mV
                                                                                                  Vddana=3.0V 1V internal Ref     -14.3     +0.5     +14.7

                                                                                                  Vddana=3.0V Vref=Vddana/2       -13.6     +0.5        +14

   SFDR                  Spurious Free Dynamic Range                                                                              76.6      79.6      83.5

  SINAD                Signal to Noise and Distortion ratio                                                                       65.2      67.2      68.9
                                                              Fs = 1Msps Fin = 14kHz (2)          Vddana=3.0V Vref=Vddana                                      dB
   SNR                        Signal to Noise ratio                                                                               64.6      66.5      68.2

   THD                     Total Harmonic Distortion                                                                              -91.6     -82.9    -78.6

                                                                                                  Vddana=3.0V ExtVref=2.0V         0.2       0.4        2.4
   Nrms                            Noise RMS                     constant input voltage                                                                        mV
                                                                                                  Vddana=3.0V Vref=Vddana         0.15      0.25        2.5


               Note:
                1. These values are based on characterization. These values are not covered by test limits in
                     production.
                2. All values expressed in decibel refer to the full scale input and are tested with an input signal
                     0.35dB below full scale; THD measured on the first seven harmonics of the input signal.
                3. With REFCTRL.REFCOMP=1 and SAMPCTRL.OFFCOMP=1.
Table 55-11. Single Ended Mode (1)
                                                                                                                                          Measurement
 Symbol                            Parameter                                              Conditions                                                           Unit
                                                                                                                                   Min       Typ      Max

                                                                                                  Vddana=3.0V Vref=Vddana          8.9      9.25        9.9
  ENOB                      Effective Number of bits          Fadc = 1Msps - R2R disabled                                                                      bits
                                                                                                  Vddana=3.0V ExtVref=2.0V        8.85      9.49      9.71




              © 2019 Microchip Technology Inc.                                  Datasheet                                       DS60001507E-page 2044
                                                                             SAM D5x/E5x Family Data Sheet
                                                                                                Electrical Characteristics at 105°C

...........continued
                                                                                                                                          Measurement
 Symbol                            Parameter                                              Conditions                                                           Unit
                                                                                                                                   Min       Typ      Max

                                                                                                  Vddana=3.0V Vref=Vddana           -      +/-10.9   +/-18.3
   TUE                     Total Unadjusted Error (3)         Fadc = 1Msps - R2R disabled
                                                                                                  Vddana=3.0V ExtVref=2.0V          -      +/-10.5   +/-19.1

                                                                                                  Vddana=3.0V Vref=Vddana           -       +/-2.3   +/-3.2
    INL                      Integral Non Linearity           Fadc = 1Msps - R2R disabled                                                                      LSB
                                                                                                  Vddana=3.0V ExtVref=2.0V          -       +/-2.3      +/-3

                                                                                                  Vddana=3.0V Vref=Vddana           -      +/-0.98   -1/+1
   DNL                      Differential Non Linearity        Fadc = 1Msps - R2R disabled
                                                                                                  Vddana=3.0V ExtVref=2.0V          -      +/-0.97   -1/+1.2

                                                                                                  Vddana=3.0V Vref=Vddana          -0.3     -0.01     +0.3

                                                                                                  Vddana=3.0V ExtVref=2.0V        -0.16     +0.02     +0.3
   Gain            Gain Error with REFCTRL.REFCOMP=1                 Fadc = 1Msps                                                                               %
                                                                                                  Vddana=3.0V 1V internal Ref      -11       -1.1       +7

                                                                                                  Vddana=3.0V Vref=Vddana/2        -0.5     +0.13     +0.7

                                                                                                  Vddana=3.0V Vref=Vddana          -19       -7.2     +9.3

                                                                                                  Vddana=3.0V ExtVref=2.0V        -20.7      -3.3       +17
   Offset         Offset Error with SAMPCTRL.OFFCOMP=1               Fadc = 1Msps                                                                              mV
                                                                                                  Vddana=3.0V 1V internal Ref      -24       -4.2       +26

                                                                                                  Vddana=3.0V Vref=Vddana/2        -27       -3.1       +24

   SFDR                  Spurious Free Dynamic Range                                                                              67.9      69.2      76.3

  SINAD                Signal to Noise and Distortion ratio                                                                       55.7      57.5      61.1
                                                              Fs = 1Msps Fin = 14kHz (2)          Vddana=3.0V Vref=Vddana                                      dB
   SNR                        Signal to Noise ratio                                                                               54.7      56.9      60.6

   THD                     Total Harmonic Distortion                                                                              -73.7     -68.2    -65.8

                                                                                                  Vddana=3.0V ExtVref=2.0V        0.35       1.0        2.1
   Nrms                            Noise RMS                     constant input voltage                                                                        mV
                                                                                                  Vddana=3.0V Vref=Vddana          0.3      0.35        1.7


               Note:
                1. These values are based on characterization. These values are not covered by test limits in
                     production.
                2. All values expressed in decibel refer to the full scale input and are tested with an input signal
                     0.35dB below full scale; THD measured on the first seven harmonics of the input signal.
                3. With REFCTRL.REFCOMP=1 and SAMPCTRL.OFFCOMP=1.




              © 2019 Microchip Technology Inc.                                  Datasheet                                       DS60001507E-page 2045
                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                     Electrical Characteristics at 105°C

           Table 55-12. Power Consumption
              Symbol           Parameters                                       Conditions                                        Ta              Typ. Max Units

                                                       fs = 1 Msps / Reference buffer disabled / BIASREFBUF = '111',
                                                                                                                                                  279       326
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V

                                                       fs = 1 Msps / Reference buffer enabled / BIASREFBUF = '111',
                                                                                                                                                  482       686
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V                       Max 105°C Typ
                            Differential mode                                                                                                                        µA
                                                       fs = 10 ksps / Reference buffer disabled / BIASREFBUF = '111',            25°C
                                                                                                                                                  28        85
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V

                                                       fs = 10 ksps / Reference buffer enabled / BIASREFBUF = '111',
                                                                                                                                                  241       435
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V
            IDD VDDANA
                                                       fs = 1 Msps / Reference buffer disabled / BIASREFBUF = '111',
                                                                                                                                                  307       361
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V

                                                       fs = 1 Msps / Reference buffer enabled / BIASREFBUF = '111',
                                                                                                                                                  499       730
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V                       Max 105°C Typ
                           Single Ended mode                                                                                                                         µA
                                                       fs = 10 ksps / Reference buffer disabled / BIASREFBUF = '111',            25°C
                                                                                                                                                  38        126
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V

                                                       fs = 10 ksps / Reference buffer enabled / BIASREFBUF = '111',
                                                                                                                                                  245       448
                                                              BIASREFCOMP = '111' VDDANA = VREF = 3.0V


55.4.4     Digital to Analog Converter (DAC) Characteristics (105°C)
Table 55-13. Differential Mode (1)
 Symbol                                Parameters                                                       Conditions                        Min.      Typ.          Max.    Unit

                                                                                                    i12clk=12 MHz
                                                                                           VDDANA = 3.0V - External Ref = 2.0V               -      ±2.4          ±3.4
                                                                                                       Cload = 50pF
   INL          Integral Non Linearity, Best Fit curve from 0x080 to 0xF7F
                                                                                                   i12clk=12 MHz
                                                                                             VDDANA = 3.0V - 1V Internal Ref                 -      ±3.2          ±4.2
                                                                                                       Cload = 50pF
                                                                                                                                                                           LSB
                                                                                                    i12clk=12 MHz
                                                                                           VDDANA = 3.0V - External Ref = 2.0V               -      ±2.4          ±3.6
                                                                                                       Cload = 50pF
  DNL          Differential Non Linearity, Best Fit curve from 0x080 to 0xF7F
                                                                                                   i12clk=12 MHz
                                                                                             VDDANA = 3.0V - 1V Internal Ref                 -      ±3.5          ±5.4
                                                                                                       Cload = 50pF

                                                                                                External Reference voltage                   -      ±0.4          ±1.7
  Gerr                                  Gain Error                                                                                                                        % FSR
                                                                                              1.0V Internal Reference voltage                -      ±0.8          ±8.5

                                                                                                External Reference voltage                   -      ±13           ±44
  Offerr                                Offset Error                                                                                                                       mV
                                                                                              1.0V Internal Reference voltage                -         ±8         ±64

 ENOB                            Effective Number Of Bits                                                                                 9.7       10.7          11.0     Bits

  SNR                              Signal to Noise ratio                                 Fs = 1 Ms/s - External Ref - CCTRL = 0x2         61.3      68.6          74.5     dB

  THD                            Total Harmonic Distortion                                                                                -82.3     -72.5         -58.9    dB


           Note:
            1. These values are based on characterization. These values are not covered by test limits in
                 production.




           © 2019 Microchip Technology Inc.                                          Datasheet                                         DS60001507E-page 2046
                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                    Electrical Characteristics at 105°C

Table 55-14. Single-Ended Mode (1)
 Symbol                                  Parameters                                                    Conditions                            Min.    Typ.    Max.          Unit

                                                                                                   i12clk=12 MHz
                                                                                          VDDANA = 3.0V - External Ref = 2.0V                  -     ±2.7     ±4.0
                                                                                                      Cload = 50pF
   INL            Integral Non Linearity, Best Fit curve from 0x080 to 0xF7F
                                                                                                  i12clk=12 MHz
                                                                                            VDDANA = 3.0V - 1V Internal Ref                    -     ±5.2     ±8.7
                                                                                                      Cload = 50pF
                                                                                                                                                                           LSB
                                                                                                   i12clk=12 MHz
                                                                                          VDDANA = 3.0V - External Ref = 2.0V                  -     ±3.5     ±6.1
                                                                                                      Cload = 50pF
  DNL            Differential Non Linearity, Best Fit curve from 0x080 to 0xF7F
                                                                                                  i12clk=12 MHz
                                                                                            VDDANA = 3.0V - 1V Internal Ref                    -     ±6.4     ±9.4
                                                                                                      Cload = 50pF

                                                                                                External Reference voltage                     -     ±0.3     ±1.6
  Gerr                                    Gain Error                                                                                                                   % FSR
                                                                                             1.0V Internal Reference voltage                   -     ±0.8     ±8.6

                                                                                                External Reference voltage                     -      ±7      ±25
  Offerr                                  Offset Error                                                                                                                     mV
                                                                                             1.0V Internal Reference voltage                   -      ±2      ±19

 ENOB                              Effective Number of Bits                                                                                  9.1     10.3     10.8         Bits

  SNR                                Signal to Noise Ratio                               Fs = 1 Ms/s - External Ref - CCTRL = 0x2            63.5    68.6     74.5         dB

  THD                              Total Harmonic Distortion                                                                                 -82.3   -72.8   -61.0         dB


            Note:
             1. These values are based on characterization. These values are not covered by test limits in
                  production.
Table 55-15. Power Consumption
Symbol     Parameters                                                       Conditions                                                  Ta           Min. Typ. Max. Unit

IDDANA Differential Mode, DC supply current, 2 output channels -            fs = 1 Msps, CCTR L= 0x2, VREF > 2.4V, VCC = 3.3V           Max. 105°C     -     384     593     µA
       without load                                                                                                                     Typ. 25°C
                                                                            fs = 10 ksps, CCTRL = 0x0, VREF < 2.4V, VCC = 3.3V                         -     283     457

           Single-Ended Mode, DC supply current, 2 output channels -        fs = 1 Msps, CCTRL = 0x2, VREF > 2.4V, VCC = 3.3V                          -     306     493     µA
           without load
                                                                            fs = 10 ksps, CCTRL = 0x0, VREF < 2.4V, VCC = 3.3V                         -     230     369


55.4.5      Analog Comparator (AC) Characteristics (105°C)
            Table 55-16. Analog Comparator Characteristics

             Symbol Parameters                                          Conditions                                                  Min Typ Max Unit
             Off(1)        Offset                                       High speed COMPCTRLn.SPEED =                                -22 ±3            22      mV
                                                                        0x3
             Tpd           Propagation Delay                            High speed COMPCTRLn.SPEED =                                -         24.1 42         ns
                           Vcm=Vddana/2, Vin =                          0x3
                           +/-100mV overdrive from
                           Vcm
             Tstart        Startup time                                 High speed COMPCTRLn.SPEED =                                -         4.7     8       µs
                                                                        0x3




            © 2019 Microchip Technology Inc.                                        Datasheet                                           DS60001507E-page 2047
                                                         SAM D5x/E5x Family Data Sheet
                                                                       Electrical Characteristics at 105°C

         Note:
          1. Hysteresis disabled.
Table 55-17. Power Consumption

Symbol Parameters                                  Conditions                         Ta            Typ. Max. Unit
IDDANA    Current consumption for                  COMPCTRLn.SPEED=0x3,               Max.105°C 59        103      µA
          One AC enabled,                          VDDANA=3.3V                        Typ.25°C
          Hysteresis disabled
          voltage scaler disabled
          Current consumption Voltage Scaler only VDDANA=3.3V                                       11    18

55.4.6   PTC Characteristics
         The values in the following Power Consumption table are measured values of power consumption under
         the following conditions:
         Operating Conditions:
         VDD = 3.0V
         Clocks
         DFLL48M used as main clock source, running undivided at 48MHz
         CPU is running on flash with 2 wait states, at 48MHz
         PTC running at 4MHz
         PTC Configuration
         Mutual-capacitance mode
         One touch channel
         System Configuration
         Standby sleep mode enabled
         RTC running on ULP32K: used to define the PTC scan rate, through the event system
         RTC interrupts (wakeup) the CPU to perform PTC scans




         © 2019 Microchip Technology Inc.                  Datasheet                       DS60001507E-page 2048
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                Electrical Characteristics at 105°C

       Table 55-18. Power Consumption (1)

                                               PTC scan
        Symbol           Parameters                             Oversamples                Ta           Typ. Max Units
                                              rate (msec)
                                                                       4                                137 2174
                                                    10
                                                                      16                                146 2194
                                                                       4                                 77      2098
                                                    50
                                                                      16                                 79      2104
           IDD     Current Consumption                                           Max 105°C Typ 25°C                       µA
                                                                       4                                 68      2092
                                                   100
                                                                      16                                 69      2095
                                                                       4                                 64      2086
                                                   200
                                                                      16                                 65      2089

       Note:
        1. These are based on characterization.



55.5   NVM Characteristics
       Table 55-19. NVM Flash Read Wait States for Worst Case Conditions

         CPU Fmax (MHz)           0 WS       1 WS         2 WS        3 WS       4 WS       5 WS       6 WS       Auto WS
          Read Operations         1 cycle   2 cycles     3 cycles    4 cycles   5 cycles   6 cycles   7 cycles     n cycles
            VDD > 1.71V             19        38           57          76         95            100     120             120

       Maximum operating frequencies are given in the table above, but are limited by the Embedded Flash
       access time when the processor is fetching code out of it. Theses tables provide the device maximum
       operating frequency defined by the field RWS of the NVMCTRL CTRLA register when automatic wait
       states (AUTOWS) is disabled. This field defines the number of Wait states required to access the
       Embedded Flash Memory.




       © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 2049
                                                             SAM D5x/E5x Family Data Sheet
                                                                          Electrical Characteristics at 105°C


55.6     Oscillators Characteristics (105°C)

55.6.1   Crystal Oscillator (XOSC) Characteristics (105°C)
         Table 55-20. Multiple Crystal Oscillator Electrical Characteristics

          Symbol Parameter           Conditions                                         Min. Typ.      Max      Units
                                     F = 8MHz - CL=20 pF - Cshunt = 2 pF -              -      39700 72200
                                     IMULT=0x3
                                     F = 16MHz - CL=20 pF - Cshunt = 1,5 pF -           -      37550 73000
                                     IMULT=0x4
            Tstart   Startup time                                                                               Cycles
                                     F = 24MHz - CL=20 pF - Cshunt = 2,5 pF -           -      32700 68500
                                     IMULT=0x5
                                     F = 48MHz - CL=13 pF - Cshunt = 5 pF -             -      18400 38500
                                     IMULT=0x6

         Table 55-21. Power Consumption

          Symbol Parameters                 Conditions                           Ta                 Typ. Max. Units
          IDD        Current                F = 8 MHz - CL = 20 pF - IMULT =     Max. 105°C,        0.43 1.56     mA
                     Consumption            0x3, ENALC = OFF                     Typ. 25°C
                                            ENALC = ON                                              0.16 1.16
                                            F = 16 MHz - CL = 20 pF - IMULT =                       1.31 3.23
                                            0x5, ENALC = OFF
                                            ENALC = ON                                              0.25 1.33
                                            F = 32 MHz - CL = 13 pF - IMULT =                       2.92 5.74
                                            0x5, ENALC = OFF
                                            ENALC = ON                                              0.40 1.92
                                            F = 48 MHz - CL = 13 pF - IMULT =                       2.70 5.82
                                            0x6, ENALC = OFF
                                            ENALC = ON                                              0.76 2.64

55.6.2   External 32 kHz Crystal Oscillator (XOSC32K) Characteristics (105°C)
         Table 55-22. Power Consumption

          Symbol          Parameter Condition       Ta           Gain Mode Typ.             Max.          Units
                                    s
          IDD             Current    VDD=3.0V       Max 105°C Std.              1.5         2.5           µA
                          consumptio                Typ 25°C
                                                              High              1.9         3.3
                          n




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 2050
                                                                SAM D5x/E5x Family Data Sheet
                                                                                Electrical Characteristics at 105°C

55.6.3 Internal Ultra Low Power 32 kHz RC Oscillator (OSCULP32K) Characteristics (105°C)
Table 55-23. Ultra-Low-Power Internal 32 kHz RC Oscillator Electrical Characteristics

Symbol Parameter                Calibration                    Conditions                             Min.     Typ.            Max     Units
FOUT      Output frequency Factory default & without           [-40, +105]°C, VDDANA>1.71V            26.00 32.768 39.50 kHz
                           user software calibration
                                With user software             Recalibrate using XOSC as              32.28                    33.25
                                calibration                    reference Clock source
                                                               Recalibrate using DFLL as              31.29                    33.91
                                                               reference Clock source

55.6.4 Digital Frequency Locked Loop (DFLL48M) Characteristics (105°C)
Table 55-24. DFLL48M Characteristics - Open Loop Mode (1)
Symbol                   Parameter                Conditions                                  Min.           Typ.        Max.        Units

FOpenOUT                 Output frequency         DFLLVAL after Reset                         45.57          48          50.09       MHz
                                                  LDO Regulator mode, [-40, 105]°C

                                                  DFLLVAL after Reset                         47.12          48          48.9
                                                  LDO Regulator mode, [0, 60]°C

TOpenSTARTUP             Startup time             DFLLVAL after Reset                         -              4.3         6.5         µs
                                                  FOUT within 90% of final value


         Note:
          1. DFLL48 in open loop can be used only with LDO regulator.
Table 55-25. DFLL48M Power Consumption

Symbol Parameter                     Conditions                                          Ta              Min. Typ. Max. Units
IDD       Current Consumption Open Loop mode - DFLLVAL after reset VCC =                 Max. 105°C -               400 1400 µA
                              3.3V                                                       Typ. 25°C
                                     Closed Loop mode - fREF = 32 .768 kHz VCC =                         -          404 1390 µA
                                     3.3V

55.6.5   Fractional Digital Phase Lock Loop (FDPLL) Characteristics (105°C)
         Table 55-26. Fractional Digital Phase Lock Loop Characteristics (2)

          Symbol Parameter                                 Conditions                         Min. Typ. Max. Units
          Jp          Period jitter (Peak-Peak value)      fIN = 32 kHz, fOUT = 96 MHz            -     1.9         2.9          %
                                                           fIN = 32 kHz, fOUT = 200 MHz           -     3.4         5.6
                                                           fIN = 3.2 MHz, fOUT = 96 MHz           -     2.0         3.1
                                                           fIN = 3.2 MHz, fOUT = 200 MHz          -     4.3         7.1
          Duty (1)    Duty cycle                                            -                     -      50          -           %




         © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 2051
                                                          SAM D5x/E5x Family Data Sheet
                                                                       Electrical Characteristics at 105°C

         Note:
          1. These are based on simulation. These values are not covered by test or characterization.
          2. These FDPLL200M characteristics are applicable with LDO regulator and a direct reference (i.e.,
               REFCLK is XOSC or XOSC32K, not GCLK).
Table 55-27. Power Consumption

Symbol       Parameter                      Conditions                       TA              Typ.   Max.       Units
IDD          Current Consumption            Ck = 96 MHz, VDD = 3.3V          Max. 105°C      0.9    1.8        mA
                                                                             Typ. 25°C
                                            Ck = 200 MHz, VDD = 3.3V                         2.0    2.6




         © 2019 Microchip Technology Inc.                  Datasheet                      DS60001507E-page 2052
