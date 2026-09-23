# SSD1362_v1.0

*Source: `SSD1362_v1.0.pdf` (62 pages) — converted from PDF*


<!-- page 1 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/
SOLOMON SYSTECH
SEMICONDUCTOR TECHNICAL DATA




                                                SSD1362




                                       Advance Information

         256 x 64, 16 Gray Scale Dot Matrix High Power
      OLED/PLED Segment/Common Driver with Controller




This document contains information on a product under development. Solomon Systech reserves the right to change
or discontinue this product without notice.                                                                            §
http://www.solomon-systech.com                                                                                        SOLOMON
SSD1362            Rev 1.0    P 1/62    Feb 2015                    Copyright  2015 Solomon Systech Limited          SYSTECH

<!-- page 2 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                         Appendix: IC Revision history of SSD1362 Specification


Version                                      Change Items                                                 Effective Date
  1.0     Advance Information 1st Release                                                                   17-Feb-15




Solomon Systech                                                           Feb 2015    P 2/62    Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| Version | Change Items | Effective Date |
| --- | --- | --- |
| 1.0 | Advance Information 1st Release | 17-Feb-15 |


<!-- page 3 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




CONTENTS

1       GENERAL DESCRIPTION ....................................................................................................... 7

2       FEATURES................................................................................................................................... 7

3       ORDERING INFORMATION ................................................................................................... 7

4       BLOCK DIAGRAM .................................................................................................................... 8

5       DIE PAD FLOOR PLAN ............................................................................................................ 9

6       PIN DESCRIPTIONS ................................................................................................................ 12

7       FUNCTIONAL BLOCK DESCRIPTIONS ............................................................................ 15

    7.1     MCU Interface selection ..................................................................................................................................... 15
       7.1.1     MCU Parallel 6800-series Interface ........................................................................................................... 15
       7.1.2     MCU Parallel 8080-series Interface ........................................................................................................... 16
       7.1.3     MCU Serial Interface (4-wire SPI) ............................................................................................................. 17
       7.1.4     MCU Serial Interface (3-wire SPI) ............................................................................................................. 18
       7.1.5     MCU I2C Interface ...................................................................................................................................... 19
    7.2     Command    Decoder ............................................................................................................................................. 22
    7.3     Oscillator Circuit  and Display Time Generator .................................................................................................. 22
    7.4     FR synchronization    ............................................................................................................................................. 23
    7.5     Segment  Drivers   / Common         Drivers ................................................................................................................... 24
    7.6     SEG/COM Driving block ................................................................................................................................... 27
    7.7     Graphic Display Data RAM (GDDRAM) .......................................................................................................... 28
    7.8     Gray Scale Decoder ............................................................................................................................................ 31
    7.9     Power ON and OFF sequence ............................................................................................................................. 32
    7.10 VDD Regulator ..................................................................................................................................................... 33
    7.11 Reset Circuit ....................................................................................................................................................... 33
8      COMMAND TABLE ................................................................................................................. 34
    8.1       Data Read / Write ............................................................................................................................................... 39
9      COMMAND DESCRIPTIONS................................................................................................. 40
    9.1     Fundamental Command Description................................................................................................................... 40
       9.1.1    Set Column Address (15h)........................................................................................................................... 40
       9.1.2    Set Row Address (75h) ................................................................................................................................ 40
       9.1.3    Set Contrast Current (81h) ......................................................................................................................... 41
       9.1.4    Set Re-map (A0h) ........................................................................................................................................ 41
      9.1.5     Set Display Start Line (A1h) ....................................................................................................................... 44
      9.1.6     Set Display Offset (A2h).............................................................................................................................. 45
      9.1.7     Set Vertical Scroll area (A3h) ..................................................................................................................... 46
      9.1.8     Set Display Mode (A4h ~ A7h).................................................................................................................... 46
      9.1.9     Set Multiplex Ratio (A8h)............................................................................................................................ 47
      9.1.10    Function Selection A (ABh)......................................................................................................................... 47
      9.1.11    External or Internal IREF Selection (ADh) ................................................................................................... 47
      9.1.12    Set Display ON/OFF (AEh / AFh) .............................................................................................................. 47
      9.1.13    Set Phase Length (B1h) ............................................................................................................................... 48
      9.1.14    Set Front Clock Divider / Oscillator Frequency (B3h) ............................................................................... 48
      9.1.15    Set GPIO (B5h) ........................................................................................................................................... 48
      9.1.16    Set Second Pre-charge period (B6h)........................................................................................................... 49
      9.1.17    Set Gray Scale Table (B8h)......................................................................................................................... 49
      9.1.18    Select Default Linear Gray Scale Table (B9h)............................................................................................ 49
      9.1.19    Set Pre-charge Voltage (BCh) .................................................................................................................... 49
      9.1.20    Pre-charge Voltage Capacitor Selection (BDh) ......................................................................................... 49


SSD1362                      Rev 1.0        P 3/62        Feb 2015                                                                                       Solomon Systech

<!-- page 4 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




     9.1.21      Set VCOMH Voltage (BEh)............................................................................................................................. 49
     9.1.22      Set Command Lock (FDh)........................................................................................................................... 50
     9.1.23      Set Fade In / Out and Blinking (23h) .......................................................................................................... 50
10      MAXIMUM RATINGS .......................................................................................................... 51

11      DC CHARACTERISTICS ..................................................................................................... 52

12      AC CHARACTERISTICS ..................................................................................................... 54
 12.1     AC Characteristics .............................................................................................................................................. 54
 12.2     6800-Series MCU Parallel Interface Timing Characteristics .............................................................................. 55
 12.3     8080-Series MCU Parallel Interface Timing Characteristics .............................................................................. 56
 12.4     Serial Interface Timing Characteristics ............................................................................................................... 57
 12.5     I2C Timing Characteristics .................................................................................................................................. 59
13      APPLICATION EXAMPLE.................................................................................................. 60

14      PACKAGE INFORMATION ................................................................................................ 61
 14.1     SSD1362Z Die Tray Information ....................................................................................................................... 61




 Solomon Systech                                                                                           Feb 2015        P 4/62       Rev 1.0       SSD1362

<!-- page 5 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




TABLES
TABLE 3-1: ORDERING INFORMATION ...................................................................................................................................7
TABLE 5-1 : SSD1362 BUMP DIE PAD COORDINATES ...........................................................................................................9
TABLE 6-1 : SSD1362 PIN DESCRIPTION ............................................................................................................................. 12
TABLE 6-2 : BUS INTERFACE SELECTION ............................................................................................................................. 13
TABLE 7-1 : MCU INTERFACE ASSIGNMENT UNDER DIFFERENT BUS INTERFACE MODE ....................................................... 15
TABLE 7-2 : CONTROL PINS OF 6800 INTERFACE.................................................................................................................. 15
TABLE 7-3 : CONTROL PINS OF 8080 INTERFACE.................................................................................................................. 17
TABLE 7-4 : CONTROL PINS OF 4-WIRE SERIAL INTERFACE .................................................................................................. 17
TABLE 7-5: CONTROL PINS OF 3-WIRE SERIAL INTERFACE................................................................................................... 18
TABLE 7-6 : GDDRAM ADDRESS MAP 1 ............................................................................................................................. 28
TABLE 7-7 : GDDRAM ADDRESS MAP 2 ............................................................................................................................. 28
TABLE 7-8 : GDDRAM ADDRESS MAP 3 ............................................................................................................................. 29
TABLE 7-9 : GDDRAM ADDRESS MAP 4 ............................................................................................................................. 29
TABLE 7-10 : GDDRAM ADDRESS MAP 5 ........................................................................................................................... 30
TABLE 7-11: IO REGULATOR PIN DESCRIPTION .................................................................................................................... 33
TABLE 8-1: COMMAND TABLE ............................................................................................................................................ 34
TABLE 8-2 : ADDRESS INCREMENT TABLE (AUTOMATIC) .................................................................................................... 39
TABLE 9-1 : SEG PINS HARDWARE CONFIGURATION ........................................................................................................ 392
TABLE 10-1 : MAXIMUM RATINGS ...................................................................................................................................... 51
TABLE 11-1 : DC CHARACTERISTICS ................................................................................................................................... 52
TABLE 12-1 : AC CHARACTERISTICS ................................................................................................................................... 54
TABLE 12-2 : 6800-SERIES MCU PARALLEL INTERFACE TIMING CHARACTERISTICS.......................................................... 55
TABLE 12-3 : 8080-SERIES MCU PARALLEL INTERFACE TIMING CHARACTERISTICS.......................................................... 56
TABLE 12-4 : SERIAL INTERFACE TIMING CHARACTERISTICS (4-WIRE SPI) ........................................................................ 57
TABLE 12-5: SERIAL INTERFACE TIMING CHARACTERISTICS (3-WIRE SPI) ......................................................................... 58




SSD1362                    Rev 1.0       P 5/62       Feb 2015                                                                                  Solomon Systech

<!-- page 6 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




FIGURES
FIGURE 4-1: SSD1362 BLOCK DIAGRAM ..............................................................................................................................8
FIGURE 5-1 – SSD1362Z DIE DRAWING ................................................................................................................................9
FIGURE 5-2: SSD1362Z ALIGNMENT MARK DIMENSION ........................................................................................................9
FIGURE 7-1 : DATA READ BACK PROCEDURE - INSERTION OF DUMMY READ ........................................................................ 16
FIGURE 7-2 : EXAMPLE OF WRITE PROCEDURE IN 8080 PARALLEL INTERFACE MODE.......................................................... 16
FIGURE 7-3 : EXAMPLE OF READ PROCEDURE IN 8080 PARALLEL INTERFACE MODE ........................................................... 16
FIGURE 7-4 : DISPLAY DATA READ BACK PROCEDURE - INSERTION OF DUMMY READ .......................................................... 17
FIGURE 7-5 : WRITE PROCEDURE IN 4-WIRE SERIAL INTERFACE MODE ................................................................................ 18
FIGURE 7-6: WRITE PROCEDURE IN 3-WIRE SERIAL INTERFACE MODE................................................................................. 18
FIGURE 7-7 : I2C-BUS DATA FORMAT .................................................................................................................................. 20
FIGURE 7-8 : DEFINITION OF THE START AND STOP CONDITION .......................................................................................... 21
FIGURE 7-9 : DEFINITION OF THE ACKNOWLEDGEMENT CONDITION .................................................................................... 21
FIGURE 7-10 : DEFINITION OF THE DATA TRANSFER CONDITION .......................................................................................... 21
FIGURE 7-11: OSCILLATOR CIRCUIT .................................................................................................................................... 22
FIGURE 7-12: SEGMENT AND COMMON DRIVER BLOCK DIAGRAM ..................................................................................... 24
FIGURE 7-13 : SEGMENT AND COMMON DRIVER SIGNAL WAVEFORM ................................................................................ 25
FIGURE 7-14 : GRAY SCALE CONTROL BY PWM IN SEGMENT ............................................................................................ 26
FIGURE 7-15 : IREF CURRENT SETTING BY RESISTOR VALUE ............................................................................................... 27
FIGURE 7-16 : RELATION BETWEEN GDDRAM CONTENT AND GRAY SCALE TABLE ENTRY (UNDER COMMAND B9H
    ENABLE LINEAR GRAY SCALE TABLE) ........................................................................................................................ 31
FIGURE 7-17 : THE POWER ON SEQUENCE........................................................................................................................... 32
FIGURE 7-18 : THE POWER OFF SEQUENCE ......................................................................................................................... 32
FIGURE 9-1: EXAMPLE OF COLUMN AND ROW ADDRESS POINTER MOVEMENT .................................................................. 40
FIGURE 9-2: ADDRESS POINTER MOVEMENT OF HORIZONTAL ADDRESS INCREMENT MODE .............................................. 41
FIGURE 9-3: ADDRESS POINTER MOVEMENT OF VERTICAL ADDRESS INCREMENT MODE................................................... 41
FIGURE 9-4: EXAMPLE OF SET DISPLAY START LINE WITH NO REMAPPING ........................................................................ 44
FIGURE 9-5: EXAMPLE OF SET DISPLAY OFFSET WITH NO REMAPPING ............................................................................... 45
FIGURE 9-6: EXAMPLE OF NORMAL DISPLAY ...................................................................................................................... 46
FIGURE 9-7: EXAMPLE OF ENTIRE DISPLAY ON .................................................................................................................. 46
FIGURE 9-8 : EXAMPLE OF ENTIRE DISPLAY OFF ................................................................................................................ 46
FIGURE 9-9: EXAMPLE OF INVERSE DISPLAY ....................................................................................................................... 46
FIGURE 9-10: DISPLAY ON SEQUENCE (WHEN INITIAL START)............................................................................................ 47
FIGURE 9-11: DISPLAY OFF SEQUENCE .............................................................................................................................. 47
FIGURE 9-12: DISPLAY ON SEQUENCE (DURING SLEEP MODE AND INTERNAL VDD REGULATOR IS DISABLED) ................... 48
FIGURE 9-13 : EXAMPLE OF GAMMA CORRECTION BY GAMMA LOOK UP TABLE SETTING .................................................. 49
FIGURE 9-14 : EXAMPLE OF FADE OUT MODE...................................................................................................................... 50
FIGURE 9-15 : EXAMPLE OF BLINKING MODE ...................................................................................................................... 50
FIGURE 12-1 : 6800-SERIES MCU PARALLEL INTERFACE CHARACTERISTICS ....................................................................... 55
FIGURE 12-2 : 8080-SERIES MCU PARALLEL INTERFACE CHARACTERISTICS ....................................................................... 56
FIGURE 12-3 : SERIAL INTERFACE CHARACTERISTICS (4-WIRE SPI)..................................................................................... 57
FIGURE 12-4: SERIAL INTERFACE CHARACTERISTICS (3-WIRE SPI) ..................................................................................... 58
FIGURE 12-5: I2C INTERFACE TIMING CHARACTERISTICS.................................................................................................... 59
FIGURE 13-1 : SSD1362Z APPLICATION EXAMPLE FOR 8-BIT 6800-PARALLEL INTERFACE MODE (INTERNAL REGULATED
    VDD) ............................................................................................................................................................................ 60
FIGURE 14-1: SSD1362Z DIE TRAY DRAWING ................................................................................................................... 61




   Solomon Systech                                                                                                 Feb 2015        P 6/62        Rev 1.0        SSD1362

<!-- page 7 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




1     GENERAL DESCRIPTION

     SSD1362 is a single-chip CMOS OLED/PLED driver with controller for organic/polymer light emitting
     diode dot-matrix graphic display. It consists of 256 segments and 64 commons. This IC is designed for
     Common Cathode type OLED/PLED panel.

     SSD1362 displays data directly from its internal 256 x 64 x 4 bits Graphic Display Data RAM
     (GDDRAM). Data/Commands are sent from general MCU through the hardware selectable I2C Interface,
     6800-/8080-series compatible Parallel Interface or Serial Peripheral Interface.

     The 256 steps contrast control and oscillator which embedded in SSD1362 reduces the number of external
     components. SSD1362 is suitable for portable applications requiring a compact size and high output
     brightness, such as set-top box, car audio, wearable electronics, etc.


2     FEATURES

     •   Resolution: 256 x 64 dot matrix panel                  •    For matrix display
     •   Power supply:                                                o Segment maximum source current: 600uA
             o VCC = 10.0V – 20.0V                                    o Common maximum sink current: 128mA
         (Panel driving power supply)                                 o 256 step contrast brightness current
             o VDDIO = 1.65V – VCI                                        control, 16 step master current control
         (MCU interface logic level)                                • 16 gray scale level supported by embedded
             o VCI = 1.65V - 3.5V                                      256 x 64 x 4 bit SRAM display buffer
         (Low voltage power supply)                                 • 8 bit programmable Gray Scale Look Up
             o VDD = 1.65V – 2.6V                                      Table
         (Core VDD power supply)                                    • Hardware selectable MCU Interfaces:
             o When VCI is lower than 2.6V, VDD                       o 8-bit 6800/8080-series parallel interface
                 should be tied to VCI and supplied                   o 3 /4 wire Serial Peripheral Interface
                 by external power source                             o I2C Interface (Up to 400kbit/s)
             o When VCI is higher than 2.6V, VDD                    • Power on reset (POR)
                 is internally regulated and a                      • Internal IREF or external IREF
                 stabilizing capacitor is needed                    • Row Re-mapping and Column Re-mapping
     •   Programmable Frame Rate and                                • Wide range of operating temperatures:
         Multiplexing Ratio
                                                                        -40°C to 85°C
     •   On-Chip Oscillator



3     ORDERING INFORMATION
                                          Table 3-1: Ordering Information
                                          Package Reference
    Ordering Part Number SEG COM                            Remark
                                          Form
                                                            o Min SEG pad pitch : 27um
                                                            o Min COM pad pitch : 45um
          SSD1362Z          256      64     COG    Page 9 o Min I/O pad pitch : 60um
                                                            o Die thickness: 250um
                                                            o Bump height: nominal 9um




SSD1362           Rev 1.0   P 7/62    Feb 2015                                                              Solomon Systech

**Extracted table(s) on this page:**

| Ordering Part Number | SEG | COM | Package Form | Reference | Remark |
| --- | --- | --- | --- | --- | --- |
| SSD1362Z | 256 | 64 | COG | Page 9 | o Min SEG pad pitch : 27um o Min COM pad pitch : 45um o Min I/O pad pitch : 60um o Die thickness: 250um o Bump height: nominal 9um |


<!-- page 8 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




4     BLOCK DIAGRAM
                                                   Figure 4-1: SSD1362 Block Diagram


                          VDDIO VCI




              VDD     VDD Regulator
           BGGND                                                                                                                                                         SEG127
                                                                                                                                                                   .
                                                                                                                                                                         SEG126
                                                                                                                                                                   .
                                                                                                                                                                   .
              RES#
                                                                                                                                                                   .
               CS#
                                                                                                                                                                   .
              D/C#




                                                                                                                                              Segment Drivers
                                                                                                                                                                   .
            E(RD#)




                                                                                                     Gray Scale Decoder
                                                                                                                                                                   .
        R/W# (WR#)
                                                                                                                                                                   .
                                                                 GDDRAM
                                                                                                                                                                   .
               BS0
                      Interface




                                                                                                                                                                   .
                        MCU




               BS1
                                                                                                                                                                   .
               BS2
                                                                                                                                                                   .
                                                                                                                                                                         SEG1
                D7                                                                                                                                                       SEG0
                D6
                D5                                                                                                                                                 .
                                                                                                                                                                   .




                                                                                                                                              Common Drivers
                D4                                                                                                                                                       COM0
                D3                                                                                                                                                 .
                                                                                                                                                                   .     COM1
                D2
                D1                                                                                                                                                 .
                                                                                                                                                                   .         |
                D0
                                                                                                                                                                   .
                                                                                                                                                                   .    COM62
                                                                                                                                                                   .    COM63
             VCC                                                                                                                                                   .
              VSS                                                                                                                                                  .
             VLSS                                                                                                                                                  .     SEG128
                                                                                                                                                                         SEG129
                                                                                                                                              Segment Drivers

             VSL
                                                                                                                                                                    .
                                                                                SEG/COM Driving




                                                                                                                                                                    .
                                                     Generator




                                                                                                                                                                    .
                                      Oscillator

                                                      Display
                                                      Timing




                                                                                     Block




                                                                                                                                                                    .
                       Command




                                                                                                                                                                    .
                        Decoder




            GPIO0
            GPIO1                                                                                                                                                   .
                                                                                                                                                                    .
                                                                                                                                                                    .
                                                                                                                                                                    .
                                                                                                                                                                    .    SEG254
                                                                                                                                                                    .    SEG255
                                                                                                                                                                    .
                                   CL
                                  CLS




                                                                               VCOMH
                                                                          VP



                                                                                                  IREF
                                                        FR




    Solomon Systech                                                                                                       Feb 2015   P 8/62              Rev 1.0   SSD1362

<!-- page 9 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




5      DIE PAD FLOOR PLAN


                                              Figure 5-1 – SSD1362Z Die drawing
    Pin 1 ----+I
               I                                                                       11.09 mm +/- 0.05mm x
                                                Die size
                                                                                        0.98 mm+/- 0.05mm
                                                Die thickness                               250 +/- 15um
                                                Min I/O pad pitch                              60um
                                                Min SEG pad pitch                              27um
                                                Min COM pad pitch                              45um
                                                Bump height                                 Nominal 9 um

                                                Bump size
                                                Pad#                                   X[um]             Y[um]
                                                1-8, 141-148                            100               15
               D
                                                9, 22                                    30               100
               n
               ;:;                              10-21                                    15               100
                                                23-140                                   30                67
                                                149-284, 357-492                         12               125
                                                285-356                                  30                60

                                                Alignment
                                                                                 Position                     Size
                                                mark
                                                + shape                        (-3750, -150)            75um x 75um
                     SSD1362Z




                                                T shape                        (3750, -150)             75um x 75um
                                                SSL Logo                    (-3568.5, -144.35)               -

                                               (For details dimension please see Figure 5-2)




                                                                   SSD1362Z           l     Y
                                                                                                                 X


                                                                  t
                                                                   Pad 1,2,3,…->148
                                                                   Gold Bumps face up

                                                         Figure 5-2: SSD1362Z alignment mark dimension

                                                                  15;; 25   25                          75

                                                                  M!• •:• •:
                                                            ""t·······~
                                                                y··--·-v
                                                        10 15




                                                                                                                      37.5 37.5




                                                                  ~
                                                                  25                                  25 25 25

                                                    Center:           (-3750, -150)         Center:    (3750, -150)
                                                    Size:             75 x 75 µm2           Size:      75 x 75 µm2



SSD1362                   Rev 1.0   P 9/62   Feb 2015                                                                             Solomon Systech

<!-- page 10 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                                           Table 5-1 : SSD1362 Bump Die Pad Coordinates
Pin number    Pin name      X       Y      Pin number Pin name      X        Y      Pin number Pin name     X        Y     Pin number Pin name     X        Y
     1          V20       -5356   -452.5        81        CL       210     -426.5       161    SEG117     5017.5   399.5       241     SEG37     2857.5   399.5
     2          V20       -5156   -452.5        82       VLL       270     -426.5       162    SEG116     4990.5   399.5       242     SEG36     2830.5   399.5
     3          V20       -4956   -452.5        83       CLS       330     -426.5       163    SEG115     4963.5   399.5       243     SEG35     2803.5   399.5
     4          V20       -4756   -452.5        84       VLH       390     -426.5       164    SEG114     4936.5   399.5       244     SEG34     2776.5   399.5
     5          V20       -4556   -452.5        85       BS0       450     -426.5       165    SEG113     4909.5   399.5       245     SEG33     2749.5   399.5
     6          V20       -4356   -452.5        86       VLL       510     -426.5       166    SEG112     4882.5   399.5       246     SEG32     2722.5   399.5
    7           V20       -4156   -452.5          87    BS1        570     -426.5        167   SEG111     4855.5   399.5      247      SEG31     2695.5   399.5
    8           V20       -3956   -452.5          88    VLH        630     -426.5        168   SEG110     4828.5   399.5      248      SEG30     2668.5   399.5
    9           NC        -3750    -410           89    BS2        690     -426.5        169   SEG109     4801.5   399.5      249      SEG29     2641.5   399.5
   10           TR0       -3705   -410            90    VLL        750     -426.5        170   SEG108     4774.5   399.5      250      SEG28     2614.5   399.5
   11           TR1       -3675   -410            91   BGGND       810     -426.5        171   SEG107     4747.5   399.5      251      SEG27     2587.5   399.5
   12           TR2       -3645   -410            92    VSS        870     -426.5        172   SEG106     4720.5   399.5      252      SEG26     2560.5   399.5
   13           TR3       -3615   -410            93    VSS        930     -426.5        173   SEG105     4693.5   399.5      253      SEG25     2533.5   399.5
   14           TR4       -3585   -410            94    VSS        990     -426.5        174   SEG104     4666.5   399.5      254      SEG24     2506.5   399.5
   15           TR5       -3555   -410            95    VSS       1050     -426.5        175   SEG103     4639.5   399.5      255      SEG23     2479.5   399.5
   16           VSS       -3525   -410            96   VLSS       1110     -426.5        176   SEG102     4612.5   399.5      256      SEG22     2452.5   399.5
   17           TR6       -3495   -410           97    VLSS       1170     -426.5        177   SEG101     4585.5   399.5      257      SEG21     2425.5   399.5
   18           TR7       -3465   -410           98    VLSS       1230     -426.5        178   SEG100     4558.5   399.5      258      SEG20     2398.5   399.5
   19           TR8       -3435   -410           99    VLSS       1290     -426.5        179   SEG99      4531.5   399.5      259      SEG19     2371.5   399.5
   20           TR9       -3405   -410           100   VLSS       1350     -426.5        180   SEG98      4504.5   399.5      260      SEG18     2344.5   399.5
   21          TR10       -3375   -410           101   VLSS       1410     -426.5        181   SEG97      4477.5   399.5      261      SEG17     2317.5   399.5
   22           NC        -3330   -410           102    VSL       1470     -426.5        182    SEG96     4450.5   399.5      262      SEG16     2290.5   399.5
   23           VCC       -3270   -426.5         103    VSL       1530     -426.5        183    SEG95     4423.5   399.5      263      SEG15     2263.5   399.5
   24           VCC       -3210   -426.5         104    VSL       1590     -426.5        184    SEG94     4396.5   399.5      264      SEG14     2236.5   399.5
   25           VCC       -3150   -426.5         105   VBREF      1650     -426.5        185    SEG93     4369.5   399.5      265      SEG13     2209.5   399.5
   26           VCC       -3090   -426.5         106    VSS       1710     -426.5        186    SEG92     4342.5   399.5      266      SEG12     2182.5   399.5
   27           VCC       -3030   -426.5         107    VSS       1770     -426.5        187    SEG91     4315.5   399.5      267      SEG11     2155.5   399.5
   28           VCC       -2970   -426.5         108   GPIO0      1830     -426.5        188    SEG90     4288.5   399.5      268      SEG10     2128.5   399.5
   29         VCOMH       -2910   -426.5         109   GPIO1      1890     -426.5        189    SEG89     4261.5   399.5      269      SEG9      2101.5   399.5
   30         VCOMH       -2850   -426.5         110   VDDIO      1950     -426.5        190    SEG88     4234.5   399.5      270      SEG8      2074.5   399.5
   31         VCOMH       -2790   -426.5         111   VDDIO      2010     -426.5        191    SEG87     4207.5   399.5      271      SEG7      2047.5   399.5
   32         VCOMH       -2730   -426.5         112    VCI       2070     -426.5        192    SEG86     4180.5   399.5      272      SEG6      2020.5   399.5
   33          VCOMH      -2670   -426.5       113       VCI       2130    -426.5        193    SEG85     4153.5   399.5      273      SEG5      1993.5    399.5
   34          VCOMH      -2610   -426.5       114      VDD        2190    -426.5        194    SEG84     4126.5   399.5      274      SEG4      1966.5    399.5
   35             VP      -2550   -426.5       115      VDD        2250    -426.5     / 195     SEG83     4099.5   399.5      275      SEG3      1939.5    399.5
   36             VP      -2490   -426.5       116       NC        2310    -426.5        196    SEG82     4072.5   399.5      276      SEG2      1912.5    399.5
   37             VP      -2430   -426.5       117      IREF       2370    -426.5   .    197    SEG81     4045.5   399.5      277      SEG1      1885.5    399.5
   38
   39
   40
                  VP
                  VP
                  NC
                          -2370
                          -2310
                          -2250
                                  -426.5
                                  -426.5
                                  -426.5
                                               118
                                               119
                                               120
                                                         VP
                                                         VP
                                                         VP
                                                                   2430
                                                                   2490
                                                                   2550
                                                                           -426.5
                                                                           -426.5
                                                                           -426.5
                                                                                    ,   .,~
                                                                                       / 198
                                                                                         199
                                                                                         200
                                                                                                SEG80
                                                                                                SEG79
                                                                                                SEG78
                                                                                                          4018.5
                                                                                                          3991.5
                                                                                                          3964.5
                                                                                                                   399.5
                                                                                                                   399.5
                                                                                                                   399.5
                                                                                                                              278
                                                                                                                              279
                                                                                                                              280
                                                                                                                                       SEG0
                                                                                                                                       VCC
                                                                                                                                       VCC
                                                                                                                                                 1858.5
                                                                                                                                                 1831.5
                                                                                                                                                 1804.5
                                                                                                                                                           399.5
                                                                                                                                                           399.5
                                                                                                                                                           399.5
   41           VSL       -2190   -426.5       121       VP        2610    -426.5        201    SEG77     3937.5   399.5      281      VCC       1777.5    399.5
   42           VSL       -2130   -426.5       122       VP        2670    -426.5        202    SEG76     3910.5   399.5      282      VCC       1750.5    399.5
   43           VSL       -2070   -426.5       123       VP        2730    -426.5        203    SEG75     3883.5   399.5      283      VCC       1723.5    399.5
   44           VLSS      -2010   -426.5       124     VCOMH       2790    -426.5        204    SEG74     3856.5   399.5      284      VCC       1696.5    399.5
   45           VLSS      -1950   -426.5        ...
                                               125     VCOMH       2850    -426.5   , ..."'
                                                                                         205    SEG73     3829.5   399.5      285     VCOMH      1597.5   383.21



                                           -~~
   46           VLSS      -1890   -426.5       126     VCOMH       2910    -426.5   ,/ -206     SEG72     3802.5   399.5      286     VCOMH      1552.5   383.21
   47           VLSS      -1830   -426.5       127     VCOMH       2970    -426.5        207    SEG71     3775.5   399.5      287     VCOMH      1507.5   383.21
   48           VLSS      -1770   -426.5       128     VCOMH       3030    -426.5   /    208    SEG70     3748.5   399.5      288     VCOMH      1462.5   383.21
   49           VLSS      -1710   -426.5   L '
                                               129     VCOMH       3090    -426.5     .r209     SEG69     3721.5   399.5      289      COM0      1417.5   383.21
   50           VSS       -1650   -426.5       130      VCC        3150    -426.5        210    SEG68     3694.5   399.5      290      COM1      1372.5   383.21
   51           VSS       -1590   -426.5       131      VCC        3210    -426.5        211    SEG67     3667.5   399.5      291      COM2      1327.5   383.21
   52           VSS       -1530   -426.5       132      VCC        3270    -426.5        212    SEG66     3640.5   399.5      292      COM3      1282.5   383.21
   53           VSS       -1470   -426.5    ~'133       VCC        3330    -426.5        213    SEG65     3613.5   399.5      293      COM4      1237.5   383.21
   54          BGGND      -1410   -426.5    o~ 134      VCC        3390    -426.5        214    SEG64     3586.5   399.5      294      COM5      1192.5   383.21
   55           VDD       -1350   -426.5   ..,....,
                                               135      VCC        3450    -426.5        215    SEG63     3559.5   399.5      295      COM6      1147.5   383.21
   56           VDD       -1290   -426.5    -  136      VCC1       3510    -426.5        216    SEG62     3532.5   399.5      296      COM7      1102.5   383.21
   57           VDD       -1230   -426.5       137       NC        3570    -426.5        217    SEG61     3505.5   399.5      297      COM8      1057.5   383.21
   58            VCI      -1170   -426.5   / 138         T0        3630    -426.5        218    SEG60     3478.5   399.5      298      COM9      1012.5   383.21
   59            VCI      -1110   -426.5     .,139       T1        3690    -426.5        219    SEG59     3451.5   399.5      299     COM10      967.5    383.21
   60            VCI      -1050   -426.5       140       NC        3750    -426.5        220    SEG58     3424.5   399.5      300     COM11      922.5    383.21
   61          VDDIO       -990   -426.5       141       V20       3956    -452.5        221    SEG57     3397.5   399.5      301     COM12      877.5    383.21
   62          VDDIO       -930   -426.5       142      V20        4156    -452.5        222    SEG56     3370.5   399.5      302     COM13      832.5    383.21
   63          VDDIO       -870   -426.5       143      V20        4356    -452.5        223    SEG55     3343.5   399.5      303     COM14      787.5    383.21
   64             FR       -810   -426.5       144      V20        4556    -452.5        224    SEG54     3316.5   399.5      304     COM15      742.5    383.21
   65           VLL        -750   -426.5       145      V20        4756    -452.5        225    SEG53     3289.5   399.5      305     COM16      697.5    383.21
   66           CS#        -690   -426.5       146      V20        4956    -452.5        226    SEG52     3262.5   399.5      306     COM17      652.5    383.21
   67           RES#       -630   -426.5       147      V20        5156    -452.5        227    SEG51     3235.5   399.5      307     COM18      607.5    383.21
   68           D/C#       -570   -426.5       148      V20        5356    -452.5        228    SEG50     3208.5   399.5      308     COM19      562.5    383.21
   69           VLL        -510   -426.5       149       NC       5341.5    399.5        229    SEG49     3181.5   399.5      309     COM20      517.5    383.21
   70        R/W# (WR#)    -450   -426.5       150       NC       5314.5    399.5        230    SEG48     3154.5   399.5      310     COM21      472.5    383.21
   71          E (RD#)     -390   -426.5       151     SEG127     5287.5    399.5        231    SEG47     3127.5   399.5      311     COM22      427.5    383.21
   72             D0       -330   -426.5       152     SEG126     5260.5    399.5        232    SEG46     3100.5   399.5      312     COM23      382.5    383.21
   73             D1       -270   -426.5       153     SEG125     5233.5    399.5        233    SEG45     3073.5   399.5      313     COM24      337.5    383.21
   74             D2       -210   -426.5       154     SEG124     5206.5    399.5        234    SEG44     3046.5   399.5      314     COM25      292.5    383.21
   75             D3       -150   -426.5       155     SEG123     5179.5    399.5        235    SEG43     3019.5   399.5      315     COM26      247.5    383.21
   76           VLL         -90   -426.5       156     SEG122     5152.5    399.5        236    SEG42     2992.5   399.5      316     COM27      202.5    383.21
   77             D4        -30   -426.5       157     SEG121     5125.5    399.5        237    SEG41     2965.5   399.5      317     COM28      157.5    383.21
   78             D5        30    -426.5       158     SEG120     5098.5    399.5        238    SEG40     2938.5   399.5      318     COM29      112.5    383.21
   79             D6        90    -426.5       159     SEG119     5071.5    399.5        239    SEG39     2911.5   399.5      319     COM30       67.5    383.21
   80             D7        150   -426.5       160     SEG118     5044.5    399.5        240    SEG38     2884.5   399.5      320     COM31       22.5    383.21




  Solomon Systech                                                                                  Feb 2015 P 10/62         Rev 1.0        SSD1362

**Extracted table(s) on this page:**

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 1 | V20 | -5356 | -452.5 |
| 2 | V20 | -5156 | -452.5 |
| 3 | V20 | -4956 | -452.5 |
| 4 | V20 | -4756 | -452.5 |
| 5 | V20 | -4556 | -452.5 |
| 6 | V20 | -4356 | -452.5 |
| 7 | V20 | -4156 | -452.5 |
| 8 | V20 | -3956 | -452.5 |
| 9 | NC | -3750 | -410 |
| 10 | TR0 | -3705 | -410 |
| 11 | TR1 | -3675 | -410 |
| 12 | TR2 | -3645 | -410 |
| 13 | TR3 | -3615 | -410 |
| 14 | TR4 | -3585 | -410 |
| 15 | TR5 | -3555 | -410 |
| 16 | VSS | -3525 | -410 |
| 17 | TR6 | -3495 | -410 |
| 18 | TR7 | -3465 | -410 |
| 19 | TR8 | -3435 | -410 |
| 20 | TR9 | -3405 | -410 |
| 21 | TR10 | -3375 | -410 |
| 22 | NC | -3330 | -410 |
| 23 | VCC | -3270 | -426.5 |
| 24 | VCC | -3210 | -426.5 |
| 25 | VCC | -3150 | -426.5 |
| 26 | VCC | -3090 | -426.5 |
| 27 | VCC | -3030 | -426.5 |
| 28 | VCC | -2970 | -426.5 |
| 29 | VCOMH | -2910 | -426.5 |
| 30 | VCOMH | -2850 | -426.5 |
| 31 | VCOMH | -2790 | -426.5 |
| 32 | VCOMH | -2730 | -426.5 |
| 33 | VCOMH | -2670 | -426.5 |
| 34 | VCOMH | -2610 | -426.5 |
| 35 | VP | -2550 | -426.5 |
| 36 | VP | -2490 | -426.5 |
| 37 | VP | -2430 | -426.5 |
| 38 | VP | -2370 | -426.5 |
| 39 | VP | -2310 | -426.5 |
| 40 | NC | -2250 | -426.5 |
| 41 | VSL | -2190 | -426.5 |
| 42 | VSL | -2130 | -426.5 |
| 43 | VSL | -2070 | -426.5 |
| 44 | VLSS | -2010 | -426.5 |
| 45 | VLSS | -1950 | -426.5 |
| 46 | VLSS | -1890 | -426.5 |
| 47 | VLSS | -1830 | -426.5 |
| 48 | VLSS | -1770 | -426.5 |
| 49 | VLSS | -1710 | -426.5 |
| 50 | VSS | -1650 | -426.5 |
| 51 | VSS | -1590 | -426.5 |
| 52 | VSS | -1530 | -426.5 |
| 53 | VSS | -1470 | -426.5 |
| 54 | BGGND | -1410 | -426.5 |
| 55 | VDD | -1350 | -426.5 |
| 56 | VDD | -1290 | -426.5 |
| 57 | VDD | -1230 | -426.5 |
| 58 | VCI | -1170 | -426.5 |
| 59 | VCI | -1110 | -426.5 |
| 60 | VCI | -1050 | -426.5 |
| 61 | VDDIO | -990 | -426.5 |
| 62 | VDDIO | -930 | -426.5 |
| 63 | VDDIO | -870 | -426.5 |
| 64 | FR | -810 | -426.5 |
| 65 | VLL | -750 | -426.5 |
| 66 | CS# | -690 | -426.5 |
| 67 | RES# | -630 | -426.5 |
| 68 | D/C# | -570 | -426.5 |
| 69 | VLL | -510 | -426.5 |
| 70 | R/W# (WR#) | -450 | -426.5 |
| 71 | E (RD#) | -390 | -426.5 |
| 72 | D0 | -330 | -426.5 |
| 73 | D1 | -270 | -426.5 |
| 74 | D2 | -210 | -426.5 |
| 75 | D3 | -150 | -426.5 |
| 76 | VLL | -90 | -426.5 |
| 77 | D4 | -30 | -426.5 |
| 78 | D5 | 30 | -426.5 |
| 79 | D6 | 90 | -426.5 |
| 80 | D7 | 150 | -426.5 |

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 81 | CL | 210 | -426.5 |
| 82 | VLL | 270 | -426.5 |
| 83 | CLS | 330 | -426.5 |
| 84 | VLH | 390 | -426.5 |
| 85 | BS0 | 450 | -426.5 |
| 86 | VLL | 510 | -426.5 |
| 87 | BS1 | 570 | -426.5 |
| 88 | VLH | 630 | -426.5 |
| 89 | BS2 | 690 | -426.5 |
| 90 | VLL | 750 | -426.5 |
| 91 | BGGND | 810 | -426.5 |
| 92 | VSS | 870 | -426.5 |
| 93 | VSS | 930 | -426.5 |
| 94 | VSS | 990 | -426.5 |
| 95 | VSS | 1050 | -426.5 |
| 96 | VLSS | 1110 | -426.5 |
| 97 | VLSS | 1170 | -426.5 |
| 98 | VLSS | 1230 | -426.5 |
| 99 | VLSS | 1290 | -426.5 |
| 100 | VLSS | 1350 | -426.5 |
| 101 | VLSS | 1410 | -426.5 |
| 102 | VSL | 1470 | -426.5 |
| 103 | VSL | 1530 | -426.5 |
| 104 | VSL | 1590 | -426.5 |
| 105 | VBREF | 1650 | -426.5 |
| 106 | VSS | 1710 | -426.5 |
| 107 | VSS | 1770 | -426.5 |
| 108 | GPIO0 | 1830 | -426.5 |
| 109 | GPIO1 | 1890 | -426.5 |
| 110 | VDDIO | 1950 | -426.5 |
| 111 | VDDIO | 2010 | -426.5 |
| 112 | VCI | 2070 | -426.5 |
| 113 | VCI | 2130 | -426.5 |
| 114 | VDD | 2190 | -426.5 |
| 115 | VDD | 2250 | -426.5 |
| 116 | NC | 2310 | -426.5 |
| 117 | IREF | 2370 | -426.5 |
| 118 | VP | 2430 | -426.5 |
| 119 | VP | 2490 | -426.5 |
| 120 | VP | 2550 | -426.5 |
| 121 | VP | 2610 | -426.5 |
| 122 | VP | 2670 | -426.5 |
| 123 | VP | 2730 | -426.5 |
| 124 | VCOMH | 2790 | -426.5 |
| ... 125 | VCOMH | 2850 | -426.5 |
| 126 | VCOMH | 2910 | -426.5 |
| -~ 127 | VCOMH | 2970 | -426.5 |
| 128 | VCOMH | 3030 | -426.5 |
| 129 L ' | VCOMH | 3090 | -426.5 |
| ~ 130 | VCC | 3150 | -426.5 |
| 131 | VCC | 3210 | -426.5 |
| 132 | VCC | 3270 | -426.5 |
| ~1'3 3 | VCC | 3330 | -426.5 |
| o~13 4 | VCC | 3390 | -426.5 |
| ..,...., 135 | VCC | 3450 | -426.5 |
| - 136 | VCC1 | 3510 | -426.5 |
| 137 | NC | 3570 | -426.5 |
| / 138 | T0 | 3630 | -426.5 |
| ., 139 | T1 | 3690 | -426.5 |
| 140 | NC | 3750 | -426.5 |
| 141 | V20 | 3956 | -452.5 |
| 142 | V20 | 4156 | -452.5 |
| 143 | V20 | 4356 | -452.5 |
| 144 | V20 | 4556 | -452.5 |
| 145 | V20 | 4756 | -452.5 |
| 146 | V20 | 4956 | -452.5 |
| 147 | V20 | 5156 | -452.5 |
| 148 | V20 | 5356 | -452.5 |
| 149 | NC | 5341.5 | 399.5 |
| 150 | NC | 5314.5 | 399.5 |
| 151 | SEG127 | 5287.5 | 399.5 |
| 152 | SEG126 | 5260.5 | 399.5 |
| 153 | SEG125 | 5233.5 | 399.5 |
| 154 | SEG124 | 5206.5 | 399.5 |
| 155 | SEG123 | 5179.5 | 399.5 |
| 156 | SEG122 | 5152.5 | 399.5 |
| 157 | SEG121 | 5125.5 | 399.5 |
| 158 | SEG120 | 5098.5 | 399.5 |
| 159 | SEG119 | 5071.5 | 399.5 |
| 160 | SEG118 | 5044.5 | 399.5 |

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 161 | SEG117 | 5017.5 | 399.5 |
| 162 | SEG116 | 4990.5 | 399.5 |
| 163 | SEG115 | 4963.5 | 399.5 |
| 164 | SEG114 | 4936.5 | 399.5 |
| 165 | SEG113 | 4909.5 | 399.5 |
| 166 | SEG112 | 4882.5 | 399.5 |
| 167 | SEG111 | 4855.5 | 399.5 |
| 168 | SEG110 | 4828.5 | 399.5 |
| 169 | SEG109 | 4801.5 | 399.5 |
| 170 | SEG108 | 4774.5 | 399.5 |
| 171 | SEG107 | 4747.5 | 399.5 |
| 172 | SEG106 | 4720.5 | 399.5 |
| 173 | SEG105 | 4693.5 | 399.5 |
| 174 | SEG104 | 4666.5 | 399.5 |
| 175 | SEG103 | 4639.5 | 399.5 |
| 176 | SEG102 | 4612.5 | 399.5 |
| 177 | SEG101 | 4585.5 | 399.5 |
| 178 | SEG100 | 4558.5 | 399.5 |
| 179 | SEG99 | 4531.5 | 399.5 |
| 180 | SEG98 | 4504.5 | 399.5 |
| 181 | SEG97 | 4477.5 | 399.5 |
| 182 | SEG96 | 4450.5 | 399.5 |
| 183 | SEG95 | 4423.5 | 399.5 |
| 184 | SEG94 | 4396.5 | 399.5 |
| 185 | SEG93 | 4369.5 | 399.5 |
| 186 | SEG92 | 4342.5 | 399.5 |
| 187 | SEG91 | 4315.5 | 399.5 |
| 188 | SEG90 | 4288.5 | 399.5 |
| 189 | SEG89 | 4261.5 | 399.5 |
| 190 | SEG88 | 4234.5 | 399.5 |
| 191 | SEG87 | 4207.5 | 399.5 |
| 192 | SEG86 | 4180.5 | 399.5 |
| 193 | SEG85 | 4153.5 | 399.5 |
| 194 | SEG84 | 4126.5 | 399.5 |
| / 195 | SEG83 | 4099.5 | 399.5 |
| . 196 | SEG82 | 4072.5 | 399.5 |
| 197 | SEG81 | 4045.5 | 399.5 |
| .. / 198 | SEG80 | 4018.5 | 399.5 |
| , 199 | SEG79 | 3991.5 | 399.5 |
| ,~ 200 | SEG78 | 3964.5 | 399.5 |
| 201 | SEG77 | 3937.5 | 399.5 |
| 202 | SEG76 | 3910.5 | 399.5 |
| 203 | SEG75 | 3883.5 | 399.5 |
| "2 04 | SEG74 | 3856.5 | 399.5 |
| , ... 2 ' 0 5 | SEG73 | 3829.5 | 399.5 |
| ,/ -206 | SEG72 | 3802.5 | 399.5 |
| 207 | SEG71 | 3775.5 | 399.5 |
| / 208 | SEG70 | 3748.5 | 399.5 |
| .r20 9 | SEG69 | 3721.5 | 399.5 |
| 210 | SEG68 | 3694.5 | 399.5 |
| 211 | SEG67 | 3667.5 | 399.5 |
| 212 | SEG66 | 3640.5 | 399.5 |
| 213 | SEG65 | 3613.5 | 399.5 |
| 214 | SEG64 | 3586.5 | 399.5 |
| 215 | SEG63 | 3559.5 | 399.5 |
| 216 | SEG62 | 3532.5 | 399.5 |
| 217 | SEG61 | 3505.5 | 399.5 |
| 218 | SEG60 | 3478.5 | 399.5 |
| 219 | SEG59 | 3451.5 | 399.5 |
| 220 | SEG58 | 3424.5 | 399.5 |
| 221 | SEG57 | 3397.5 | 399.5 |
| 222 | SEG56 | 3370.5 | 399.5 |
| 223 | SEG55 | 3343.5 | 399.5 |
| 224 | SEG54 | 3316.5 | 399.5 |
| 225 | SEG53 | 3289.5 | 399.5 |
| 226 | SEG52 | 3262.5 | 399.5 |
| 227 | SEG51 | 3235.5 | 399.5 |
| 228 | SEG50 | 3208.5 | 399.5 |
| 229 | SEG49 | 3181.5 | 399.5 |
| 230 | SEG48 | 3154.5 | 399.5 |
| 231 | SEG47 | 3127.5 | 399.5 |
| 232 | SEG46 | 3100.5 | 399.5 |
| 233 | SEG45 | 3073.5 | 399.5 |
| 234 | SEG44 | 3046.5 | 399.5 |
| 235 | SEG43 | 3019.5 | 399.5 |
| 236 | SEG42 | 2992.5 | 399.5 |
| 237 | SEG41 | 2965.5 | 399.5 |
| 238 | SEG40 | 2938.5 | 399.5 |
| 239 | SEG39 | 2911.5 | 399.5 |
| 240 | SEG38 | 2884.5 | 399.5 |

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 241 | SEG37 | 2857.5 | 399.5 |
| 242 | SEG36 | 2830.5 | 399.5 |
| 243 | SEG35 | 2803.5 | 399.5 |
| 244 | SEG34 | 2776.5 | 399.5 |
| 245 | SEG33 | 2749.5 | 399.5 |
| 246 | SEG32 | 2722.5 | 399.5 |
| 247 | SEG31 | 2695.5 | 399.5 |
| 248 | SEG30 | 2668.5 | 399.5 |
| 249 | SEG29 | 2641.5 | 399.5 |
| 250 | SEG28 | 2614.5 | 399.5 |
| 251 | SEG27 | 2587.5 | 399.5 |
| 252 | SEG26 | 2560.5 | 399.5 |
| 253 | SEG25 | 2533.5 | 399.5 |
| 254 | SEG24 | 2506.5 | 399.5 |
| 255 | SEG23 | 2479.5 | 399.5 |
| 256 | SEG22 | 2452.5 | 399.5 |
| 257 | SEG21 | 2425.5 | 399.5 |
| 258 | SEG20 | 2398.5 | 399.5 |
| 259 | SEG19 | 2371.5 | 399.5 |
| 260 | SEG18 | 2344.5 | 399.5 |
| 261 | SEG17 | 2317.5 | 399.5 |
| 262 | SEG16 | 2290.5 | 399.5 |
| 263 | SEG15 | 2263.5 | 399.5 |
| 264 | SEG14 | 2236.5 | 399.5 |
| 265 | SEG13 | 2209.5 | 399.5 |
| 266 | SEG12 | 2182.5 | 399.5 |
| 267 | SEG11 | 2155.5 | 399.5 |
| 268 | SEG10 | 2128.5 | 399.5 |
| 269 | SEG9 | 2101.5 | 399.5 |
| 270 | SEG8 | 2074.5 | 399.5 |
| 271 | SEG7 | 2047.5 | 399.5 |
| 272 | SEG6 | 2020.5 | 399.5 |
| 273 | SEG5 | 1993.5 | 399.5 |
| 274 | SEG4 | 1966.5 | 399.5 |
| 275 | SEG3 | 1939.5 | 399.5 |
| 276 | SEG2 | 1912.5 | 399.5 |
| 277 | SEG1 | 1885.5 | 399.5 |
| 278 | SEG0 | 1858.5 | 399.5 |
| 279 | VCC | 1831.5 | 399.5 |
| 280 | VCC | 1804.5 | 399.5 |
| 281 | VCC | 1777.5 | 399.5 |
| 282 | VCC | 1750.5 | 399.5 |
| 283 | VCC | 1723.5 | 399.5 |
| 284 | VCC | 1696.5 | 399.5 |
| 285 | VCOMH | 1597.5 | 383.21 |
| 286 | VCOMH | 1552.5 | 383.21 |
| 287 | VCOMH | 1507.5 | 383.21 |
| 288 | VCOMH | 1462.5 | 383.21 |
| 289 | COM0 | 1417.5 | 383.21 |
| 290 | COM1 | 1372.5 | 383.21 |
| 291 | COM2 | 1327.5 | 383.21 |
| 292 | COM3 | 1282.5 | 383.21 |
| 293 | COM4 | 1237.5 | 383.21 |
| 294 | COM5 | 1192.5 | 383.21 |
| 295 | COM6 | 1147.5 | 383.21 |
| 296 | COM7 | 1102.5 | 383.21 |
| 297 | COM8 | 1057.5 | 383.21 |
| 298 | COM9 | 1012.5 | 383.21 |
| 299 | COM10 | 967.5 | 383.21 |
| 300 | COM11 | 922.5 | 383.21 |
| 301 | COM12 | 877.5 | 383.21 |
| 302 | COM13 | 832.5 | 383.21 |
| 303 | COM14 | 787.5 | 383.21 |
| 304 | COM15 | 742.5 | 383.21 |
| 305 | COM16 | 697.5 | 383.21 |
| 306 | COM17 | 652.5 | 383.21 |
| 307 | COM18 | 607.5 | 383.21 |
| 308 | COM19 | 562.5 | 383.21 |
| 309 | COM20 | 517.5 | 383.21 |
| 310 | COM21 | 472.5 | 383.21 |
| 311 | COM22 | 427.5 | 383.21 |
| 312 | COM23 | 382.5 | 383.21 |
| 313 | COM24 | 337.5 | 383.21 |
| 314 | COM25 | 292.5 | 383.21 |
| 315 | COM26 | 247.5 | 383.21 |
| 316 | COM27 | 202.5 | 383.21 |
| 317 | COM28 | 157.5 | 383.21 |
| 318 | COM29 | 112.5 | 383.21 |
| 319 | COM30 | 67.5 | 383.21 |
| 320 | COM31 | 22.5 | 383.21 |


<!-- page 11 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Pin number Pin name      X         Y      Pin number Pin name      X          Y       Pin number Pin name      X        Y
    321     COM32      -22.5     383.21       401    SEG166     -2884.5      399.5        481    SEG246     -5044.5   399.5
    322     COM33      -67.5     383.21       402    SEG167     -2911.5      399.5        482    SEG247     -5071.5   399.5
    323     COM34     -112.5     383.21       403    SEG168     -2938.5      399.5        483    SEG248     -5098.5   399.5
    324     COM35     -157.5     383.21       404    SEG169     -2965.5      399.5        484    SEG249     -5125.5   399.5
    325     COM36     -202.5     383.21       405    SEG170     -2992.5      399.5        485    SEG250     -5152.5   399.5
    326     COM37     -247.5     383.21       406    SEG171     -3019.5      399.5        486    SEG251     -5179.5   399.5
   327      COM38     -292.5     383.21      407     SEG172     -3046.5      399.5       487     SEG252     -5206.5   399.5
   328      COM39     -337.5     383.21      408     SEG173     -3073.5      399.5       488     SEG253     -5233.5   399.5
   329      COM40     -382.5     383.21      409     SEG174     -3100.5      399.5       489     SEG254     -5260.5   399.5
   330      COM41     -427.5     383.21      410     SEG175     -3127.5      399.5       490     SEG255     -5287.5   399.5
   331      COM42     -472.5     383.21      411     SEG176     -3154.5      399.5       491       NC       -5314.5   399.5
   332      COM43     -517.5     383.21      412     SEG177     -3181.5      399.5       492       NC       -5341.5   399.5
   333      COM44     -562.5     383.21      413     SEG178     -3208.5      399.5
   334      COM45     -607.5     383.21      414     SEG179     -3235.5      399.5
   335      COM46     -652.5     383.21      415     SEG180     -3262.5      399.5
   336      COM47     -697.5     383.21      416     SEG181     -3289.5      399.5
   337      COM48     -742.5     383.21      417     SEG182     -3316.5      399.5
   338      COM49     -787.5     383.21      418     SEG183     -3343.5      399.5
   339      COM50     -832.5     383.21      419     SEG184     -3370.5      399.5
   340      COM51     -877.5     383.21      420     SEG185     -3397.5      399.5
   341      COM52     -922.5     383.21      421     SEG186     -3424.5      399.5
   342      COM53     -967.5     383.21      422     SEG187     -3451.5      399.5
   343      COM54     -1012.5    383.21      423     SEG188     -3478.5      399.5
   344      COM55     -1057.5    383.21      424     SEG189     -3505.5      399.5
   345      COM56     -1102.5    383.21      425     SEG190     -3532.5      399.5
   346      COM57     -1147.5    383.21      426     SEG191     -3559.5      399.5
   347      COM58     -1192.5    383.21      427     SEG192     -3586.5      399.5
   348      COM59     -1237.5    383.21      428     SEG193     -3613.5      399.5
   349      COM60     -1282.5    383.21      429     SEG194     -3640.5      399.5
   350      COM61     -1327.5    383.21      430     SEG195     -3667.5      399.5
   351      COM62     -1372.5    383.21      431     SEG196     -3694.5      399.5
   352      COM63     -1417.5    383.21      432     SEG197     -3721.5      399.5
   353     VCOMH      -1462.5    383.21      433     SEG198     -3748.5      399.5
   354     VCOMH      -1507.5    383.21      434     SEG199     -3775.5      399.5
   355     VCOMH      -1552.5    383.21      435     SEG200     -3802.5      399.5
   356     VCOMH      -1597.5    383.21      436     SEG201     -3829.5      399.5
   357      VCC       -1696.5    399.5       437     SEG202     -3856.5      399.5
   358      VCC       -1723.5    399.5       438     SEG203     -3883.5      399.5
   359      VCC       -1750.5    399.5       439     SEG204     -3910.5      399.5
   360      VCC       -1777.5    399.5       440     SEG205     -3937.5      399.5
   361      VCC       -1804.5    399.5       441     SEG206     -3964.5      399.5
   362      VCC       -1831.5    399.5       442     SEG207     -3991.5      399.5
   363     SEG128     -1858.5    399.5       443     SEG208     -4018.5      399.5
   364     SEG129     -1885.5    399.5       444     SEG209     -4045.5      399.5
   365     SEG130     -1912.5    399.5       445     SEG210     -4072.5      399.5
   366     SEG131     -1939.5    399.5       446     SEG211     -4099.5      399.5
   367     SEG132     -1966.5    399.5       447     SEG212     -4126.5      399.5
   368     SEG133     -1993.5    399.5       448     SEG213     -4153.5      399.5
   369     SEG134     -2020.5    399.5       449     SEG214     -4180.5      399.5
   370     SEG135     -2047.5    399.5       450     SEG215     -4207.5      399.5
   371     SEG136     -2074.5    399.5       451     SEG216     -4234.5      399.5
   372     SEG137     -2101.5    399.5       452     SEG217     -4261.5      399.5
   373     SEG138     -2128.5    399.5       453     SEG218     -4288.5      399.5
   374     SEG139     -2155.5    399.5       454     SEG219     -4315.5      399.5
   375     SEG140     -2182.5    399.5       455     SEG220     -4342.5      399.5
   376     SEG141     -2209.5    399.5       456     SEG221     -4369.5      399.5
   377     SEG142     -2236.5    399.5       457     SEG222     -4396.5      399.5
   378     SEG143     -2263.5    399.5       458     SEG223     -4423.5      399.5
   379     SEG144     -2290.5    399.5       459     SEG224     -4450.5      399.5
   380     SEG145     -2317.5    399.5       460     SEG225     -4477.5      399.5
   381     SEG146     -2344.5    399.5       461     SEG226     -4504.5      399.5
   382     SEG147     -2371.5    399.5       462     SEG227     -4531.5      399.5
   383     SEG148     -2398.5    399.5       463     SEG228     -4558.5      399.5
   384     SEG149     -2425.5    399.5       464     SEG229     -4585.5      399.5
   385     SEG150     -2452.5    399.5       465     SEG230     -4612.5      399.5
   386     SEG151     -2479.5    399.5       466     SEG231     -4639.5      399.5
   387     SEG152     -2506.5    399.5       467     SEG232     -4666.5      399.5
   388     SEG153     -2533.5    399.5       468     SEG233     -4693.5      399.5
   389     SEG154     -2560.5    399.5       469     SEG234     -4720.5      399.5
   390     SEG155     -2587.5    399.5       470     SEG235     -4747.5      399.5
   391     SEG156     -2614.5    399.5       471     SEG236     -4774.5      399.5
   392     SEG157     -2641.5    399.5       472     SEG237     -4801.5      399.5
   393     SEG158     -2668.5    399.5       473     SEG238     -4828.5      399.5
   394     SEG159     -2695.5    399.5       474     SEG239     -4855.5      399.5
   395     SEG160     -2722.5    399.5       475     SEG240     -4882.5      399.5
   396     SEG161     -2749.5    399.5       476     SEG241     -4909.5      399.5
   397     SEG162     -2776.5    399.5       477     SEG242     -4936.5      399.5
   398     SEG163     -2803.5    399.5       478     SEG243     -4963.5      399.5
   399     SEG164     -2830.5    399.5       479     SEG244     -4990.5      399.5
   400     SEG165     -2857.5    399.5       480     SEG245     -5017.5      399.5




SSD1362                         Rev 1.0   P 11/62        Feb 2015                                                                       Solomon Systech

**Extracted table(s) on this page:**

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 321 | COM32 | -22.5 | 383.21 |
| 322 | COM33 | -67.5 | 383.21 |
| 323 | COM34 | -112.5 | 383.21 |
| 324 | COM35 | -157.5 | 383.21 |
| 325 | COM36 | -202.5 | 383.21 |
| 326 | COM37 | -247.5 | 383.21 |
| 327 | COM38 | -292.5 | 383.21 |
| 328 | COM39 | -337.5 | 383.21 |
| 329 | COM40 | -382.5 | 383.21 |
| 330 | COM41 | -427.5 | 383.21 |
| 331 | COM42 | -472.5 | 383.21 |
| 332 | COM43 | -517.5 | 383.21 |
| 333 | COM44 | -562.5 | 383.21 |
| 334 | COM45 | -607.5 | 383.21 |
| 335 | COM46 | -652.5 | 383.21 |
| 336 | COM47 | -697.5 | 383.21 |
| 337 | COM48 | -742.5 | 383.21 |
| 338 | COM49 | -787.5 | 383.21 |
| 339 | COM50 | -832.5 | 383.21 |
| 340 | COM51 | -877.5 | 383.21 |
| 341 | COM52 | -922.5 | 383.21 |
| 342 | COM53 | -967.5 | 383.21 |
| 343 | COM54 | -1012.5 | 383.21 |
| 344 | COM55 | -1057.5 | 383.21 |
| 345 | COM56 | -1102.5 | 383.21 |
| 346 | COM57 | -1147.5 | 383.21 |
| 347 | COM58 | -1192.5 | 383.21 |
| 348 | COM59 | -1237.5 | 383.21 |
| 349 | COM60 | -1282.5 | 383.21 |
| 350 | COM61 | -1327.5 | 383.21 |
| 351 | COM62 | -1372.5 | 383.21 |
| 352 | COM63 | -1417.5 | 383.21 |
| 353 | VCOMH | -1462.5 | 383.21 |
| 354 | VCOMH | -1507.5 | 383.21 |
| 355 | VCOMH | -1552.5 | 383.21 |
| 356 | VCOMH | -1597.5 | 383.21 |
| 357 | VCC | -1696.5 | 399.5 |
| 358 | VCC | -1723.5 | 399.5 |
| 359 | VCC | -1750.5 | 399.5 |
| 360 | VCC | -1777.5 | 399.5 |
| 361 | VCC | -1804.5 | 399.5 |
| 362 | VCC | -1831.5 | 399.5 |
| 363 | SEG128 | -1858.5 | 399.5 |
| 364 | SEG129 | -1885.5 | 399.5 |
| 365 | SEG130 | -1912.5 | 399.5 |
| 366 | SEG131 | -1939.5 | 399.5 |
| 367 | SEG132 | -1966.5 | 399.5 |
| 368 | SEG133 | -1993.5 | 399.5 |
| 369 | SEG134 | -2020.5 | 399.5 |
| 370 | SEG135 | -2047.5 | 399.5 |
| 371 | SEG136 | -2074.5 | 399.5 |
| 372 | SEG137 | -2101.5 | 399.5 |
| 373 | SEG138 | -2128.5 | 399.5 |
| 374 | SEG139 | -2155.5 | 399.5 |
| 375 | SEG140 | -2182.5 | 399.5 |
| 376 | SEG141 | -2209.5 | 399.5 |
| 377 | SEG142 | -2236.5 | 399.5 |
| 378 | SEG143 | -2263.5 | 399.5 |
| 379 | SEG144 | -2290.5 | 399.5 |
| 380 | SEG145 | -2317.5 | 399.5 |
| 381 | SEG146 | -2344.5 | 399.5 |
| 382 | SEG147 | -2371.5 | 399.5 |
| 383 | SEG148 | -2398.5 | 399.5 |
| 384 | SEG149 | -2425.5 | 399.5 |
| 385 | SEG150 | -2452.5 | 399.5 |
| 386 | SEG151 | -2479.5 | 399.5 |
| 387 | SEG152 | -2506.5 | 399.5 |
| 388 | SEG153 | -2533.5 | 399.5 |
| 389 | SEG154 | -2560.5 | 399.5 |
| 390 | SEG155 | -2587.5 | 399.5 |
| 391 | SEG156 | -2614.5 | 399.5 |
| 392 | SEG157 | -2641.5 | 399.5 |
| 393 | SEG158 | -2668.5 | 399.5 |
| 394 | SEG159 | -2695.5 | 399.5 |
| 395 | SEG160 | -2722.5 | 399.5 |
| 396 | SEG161 | -2749.5 | 399.5 |
| 397 | SEG162 | -2776.5 | 399.5 |
| 398 | SEG163 | -2803.5 | 399.5 |
| 399 | SEG164 | -2830.5 | 399.5 |
| 400 | SEG165 | -2857.5 | 399.5 |

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 401 | SEG166 | -2884.5 | 399.5 |
| 402 | SEG167 | -2911.5 | 399.5 |
| 403 | SEG168 | -2938.5 | 399.5 |
| 404 | SEG169 | -2965.5 | 399.5 |
| 405 | SEG170 | -2992.5 | 399.5 |
| 406 | SEG171 | -3019.5 | 399.5 |
| 407 | SEG172 | -3046.5 | 399.5 |
| 408 | SEG173 | -3073.5 | 399.5 |
| 409 | SEG174 | -3100.5 | 399.5 |
| 410 | SEG175 | -3127.5 | 399.5 |
| 411 | SEG176 | -3154.5 | 399.5 |
| 412 | SEG177 | -3181.5 | 399.5 |
| 413 | SEG178 | -3208.5 | 399.5 |
| 414 | SEG179 | -3235.5 | 399.5 |
| 415 | SEG180 | -3262.5 | 399.5 |
| 416 | SEG181 | -3289.5 | 399.5 |
| 417 | SEG182 | -3316.5 | 399.5 |
| 418 | SEG183 | -3343.5 | 399.5 |
| 419 | SEG184 | -3370.5 | 399.5 |
| 420 | SEG185 | -3397.5 | 399.5 |
| 421 | SEG186 | -3424.5 | 399.5 |
| 422 | SEG187 | -3451.5 | 399.5 |
| 423 | SEG188 | -3478.5 | 399.5 |
| 424 | SEG189 | -3505.5 | 399.5 |
| 425 | SEG190 | -3532.5 | 399.5 |
| 426 | SEG191 | -3559.5 | 399.5 |
| 427 | SEG192 | -3586.5 | 399.5 |
| 428 | SEG193 | -3613.5 | 399.5 |
| 429 | SEG194 | -3640.5 | 399.5 |
| 430 | SEG195 | -3667.5 | 399.5 |
| 431 | SEG196 | -3694.5 | 399.5 |
| 432 | SEG197 | -3721.5 | 399.5 |
| 433 | SEG198 | -3748.5 | 399.5 |
| 434 | SEG199 | -3775.5 | 399.5 |
| 435 | SEG200 | -3802.5 | 399.5 |
| 436 | SEG201 | -3829.5 | 399.5 |
| 437 | SEG202 | -3856.5 | 399.5 |
| 438 | SEG203 | -3883.5 | 399.5 |
| 439 | SEG204 | -3910.5 | 399.5 |
| 440 | SEG205 | -3937.5 | 399.5 |
| 441 | SEG206 | -3964.5 | 399.5 |
| 442 | SEG207 | -3991.5 | 399.5 |
| 443 | SEG208 | -4018.5 | 399.5 |
| 444 | SEG209 | -4045.5 | 399.5 |
| 445 | SEG210 | -4072.5 | 399.5 |
| 446 | SEG211 | -4099.5 | 399.5 |
| 447 | SEG212 | -4126.5 | 399.5 |
| 448 | SEG213 | -4153.5 | 399.5 |
| 449 | SEG214 | -4180.5 | 399.5 |
| 450 | SEG215 | -4207.5 | 399.5 |
| 451 | SEG216 | -4234.5 | 399.5 |
| 452 | SEG217 | -4261.5 | 399.5 |
| 453 | SEG218 | -4288.5 | 399.5 |
| 454 | SEG219 | -4315.5 | 399.5 |
| 455 | SEG220 | -4342.5 | 399.5 |
| 456 | SEG221 | -4369.5 | 399.5 |
| 457 | SEG222 | -4396.5 | 399.5 |
| 458 | SEG223 | -4423.5 | 399.5 |
| 459 | SEG224 | -4450.5 | 399.5 |
| 460 | SEG225 | -4477.5 | 399.5 |
| 461 | SEG226 | -4504.5 | 399.5 |
| 462 | SEG227 | -4531.5 | 399.5 |
| 463 | SEG228 | -4558.5 | 399.5 |
| 464 | SEG229 | -4585.5 | 399.5 |
| 465 | SEG230 | -4612.5 | 399.5 |
| 466 | SEG231 | -4639.5 | 399.5 |
| 467 | SEG232 | -4666.5 | 399.5 |
| 468 | SEG233 | -4693.5 | 399.5 |
| 469 | SEG234 | -4720.5 | 399.5 |
| 470 | SEG235 | -4747.5 | 399.5 |
| 471 | SEG236 | -4774.5 | 399.5 |
| 472 | SEG237 | -4801.5 | 399.5 |
| 473 | SEG238 | -4828.5 | 399.5 |
| 474 | SEG239 | -4855.5 | 399.5 |
| 475 | SEG240 | -4882.5 | 399.5 |
| 476 | SEG241 | -4909.5 | 399.5 |
| 477 | SEG242 | -4936.5 | 399.5 |
| 478 | SEG243 | -4963.5 | 399.5 |
| 479 | SEG244 | -4990.5 | 399.5 |
| 480 | SEG245 | -5017.5 | 399.5 |

| Pin number | Pin name | X | Y |
| --- | --- | --- | --- |
| 481 | SEG246 | -5044.5 | 399.5 |
| 482 | SEG247 | -5071.5 | 399.5 |
| 483 | SEG248 | -5098.5 | 399.5 |
| 484 | SEG249 | -5125.5 | 399.5 |
| 485 | SEG250 | -5152.5 | 399.5 |
| 486 | SEG251 | -5179.5 | 399.5 |
| 487 | SEG252 | -5206.5 | 399.5 |
| 488 | SEG253 | -5233.5 | 399.5 |
| 489 | SEG254 | -5260.5 | 399.5 |
| 490 | SEG255 | -5287.5 | 399.5 |
| 491 | NC | -5314.5 | 399.5 |
| 492 | NC | -5341.5 | 399.5 |


<!-- page 12 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




6         PIN DESCRIPTIONS

Key:
                          I = Input                             NC = Not Connected
                          O =Output                             Pull LOW= connect to Ground
                          I/O = Bi-directional (input/output)   Pull HIGH= connect to VDDIO
                          P = Power pin

                                         Table 6-1 : SSD1362 Pin Description
    Pin Name    Pin Type Description
    VDD             P    Power supply for core logic operation.

                           VDD can be supplied externally (within the range of 1.65V to 2.6V) or regulated internally
                           from VCI when VCI is >2.6V.
                           A capacitor should be connected between VDD and VSS under all circumstances.

    VDDIO             P    Power supply for interface logic level. It should match with the MCU interface voltage
                           level and must be connected to external source.

    VCI               P    Low voltage power supply.
                           VCI must always be equal to or higher than VDD and VDDIO.

    VCC               P    Power supply for panel driving voltage. This is also the most positive power voltage
                           supply pin. It is supplied by external high voltage source.

    VCC1              P    Clean power supply for high voltage circuit. It must be connected to VCC externally.

    VSS               P    Ground pin. It must be connected to external ground.

    VLSS              P    Analog system ground pin. It must be connected to external ground.

    BGGND             P    Reserved pin. It should be connected to ground.

    VLH               P    Logic high (same voltage level as VDDIO) for internal connection of input and I/O pins. No
                           need to connect to external power source.

    VLL               P    Logic low (same voltage level as VSS) for internal connection of input and I/O pins. No
                           need to connect to external ground.

    VCOMH             P    COM signal deselected voltage level.

                           A capacitor should be connected between this pin and VSS.
                           No external power supply is allowed to connect to this pin.

    VP                P    This pin is the segment pre-charge voltage reference pin.

                           A capacitor should be connected between this pin and VSS.
                           No external power supply is allowed to connect to this pin.

    IREF              I    This pin is the segment output current reference pin.

                           When external IREF is used, a resistor should be connected between this pin and VSS to
                           maintain current of around 18.75uA. Please refer to section 7.6 for the formula of resistor
                           value.
                           When internal IREF is used, this pin should be kept NC.



    Solomon Systech                                                          Feb 2015 P 12/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| I = Input | NC = Not Connected |
| --- | --- |
| O =Output | Pull LOW= connect to Ground |
| I/O = Bi-directional (input/output) | Pull HIGH= connect to V DDIO |
| P = Power pin |  |

| Pin Name | Pin Type | Description |
| --- | --- | --- |
| V DD | P | Power supply for core logic operation. V can be supplied externally (within the range of 1.65V to 2.6V) or regulated internally DD from V when V is >2.6V. CI CI A capacitor should be connected between V and V under all circumstances. DD SS |
| V DDIO | P | Power supply for interface logic level. It should match with the MCU interface voltage level and must be connected to external source. |
| V CI | P | Low voltage power supply. V must always be equal to or higher than V and V . CI DD DDIO |
| V CC | P | Power supply for panel driving voltage. This is also the most positive power voltage supply pin. It is supplied by external high voltage source. |
| V CC1 | P | Clean power supply for high voltage circuit. It must be connected to V externally. CC |
| V SS | P | Ground pin. It must be connected to external ground. |
| V LSS | P | Analog system ground pin. It must be connected to external ground. |
| BGGND | P | Reserved pin. It should be connected to ground. |
| V LH | P Logic high (same voltage level as V ) for internal connection of input and I/O pins. No DDIO need to connect to external power source. |  |
| V LL | P | Logic low (same voltage level as V ) for internal connection of input and I/O pins. No SS need to connect to external ground. |
| V COMH | P | COM signal deselected voltage level. A capacitor should be connected between this pin and V . SS No external power supply is allowed to connect to this pin. |
| V P | P | This pin is the segment pre-charge voltage reference pin. A capacitor should be connected between this pin and V . SS No external power supply is allowed to connect to this pin. |
| I REF | I | This pin is the segment output current reference pin. When external I is used, a resistor should be connected between this pin and V to REF SS maintain current of around 18.75uA. Please refer to section 7.6 for the formula of resistor value. When internal I is used, this pin should be kept NC. REF |


<!-- page 13 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Pin Name   Pin Type Description
V20            P    This is a reserved pin. It should be kept NC.

GPIO0         I/O      This is a reserved pin. It should be kept NC.

GPIO1         I/O      This is a reserved pin. It should be kept NC.

BS[2:0]        I       MCU bus interface selection pins. Select appropriate logic setting as described in the
                       following table. BS2 and BS1, BS0 are pin select.

                                                     Table 6-2 : Bus Interface selection
                                                BS[2:0]         Interface
                                                000             4 line SPI
                                                001             3 line SPI
                                                110             8-bit 8080 parallel
                                                100             8-bit 6800 parallel
                                                010             I 2C

                       Note
                       (1)
                           0 is connected to VSS
                       (2)
                           1 is connected to VDDIO

VSL            P       This is a reserved pin. It should be connected to VLSS externally.

CL             I       External clock input pin.

                       When internal clock is enable (i.e. pull HIGH in CLS pin), this pin is not used and should
                       be connected to Ground.
                       When internal clock is disable (i.e. pull LOW in CLS pin), this pin is the external clock
                       source input pin.

CLS            I       Internal clock selection pin.

                       When this pin is pulled HIGH, internal oscillator is enabled (normal operation).
                       When this pin is pulled LOW, an external clock signal should be connected to CL.

CS#            I       This pin is the chip select input connecting to the MCU.

                       The chip is enabled for MCU communication only when CS# is pulled LOW (active
                       LOW).
                       In I2C mode, this pin must be connected to VSS.


RES#           I       This pin is reset signal input.

                       When the pin is pulled LOW, initialization of the chip is executed.
                       Keep this pin pull HIGH during normal operation.


D/C#           I       This pin is Data/Command control pin connecting to the MCU.

                       When the pin is pulled HIGH, the data at D[7:0] will be interpreted as data.
                       When the pin is pulled LOW, the data at D[7:0] will be transferred to a command register.

                       In I2C mode, this pin acts as SA0 for slave address selection.
                       When 3-wire serial interface is selected, this pin must be connected to VSS.




SSD1362      Rev 1.0    P 13/62    Feb 2015                                                              Solomon Systech

**Extracted table(s) on this page:**

| Pin Name | Pin Type | Description |
| --- | --- | --- |
| V 20 | P | This is a reserved pin. It should be kept NC. |
| GPIO0 | I/O | This is a reserved pin. It should be kept NC. |
| GPIO1 | I/O | This is a reserved pin. It should be kept NC. |
| BS[2:0] | I | MCU bus interface selection pins. Select appropriate logic setting as described in the following table. BS2 and BS1, BS0 are pin select. Table 6-2 : Bus Interface selection BS[2:0] Interface 000 4 line SPI 001 3 line SPI 110 8-bit 8080 parallel 100 8-bit 6800 parallel 010 I2C Note (1)0 is connected to V SS (2)1 is connected to V DDIO |
| VSL | P | This is a reserved pin. It should be connected to V externally. LSS |
| CL | I | External clock input pin. When internal clock is enable (i.e. pull HIGH in CLS pin), this pin is not used and should be connected to Ground. When internal clock is disable (i.e. pull LOW in CLS pin), this pin is the external clock source input pin. |
| CLS | I Internal clock selection pin. When this pin is pulled HIGH, internal oscillator is enabled (normal operation). When this pin is pulled LOW, an external clock signal should be connected to CL. |  |
| CS# | I | This pin is the chip select input connecting to the MCU. The chip is enabled for MCU communication only when CS# is pulled LOW (active LOW). In I2C mode, this pin must be connected to V . SS |
| RES# | I | This pin is reset signal input. When the pin is pulled LOW, initialization of the chip is executed. Keep this pin pull HIGH during normal operation. |
| D/C# | I | This pin is Data/Command control pin connecting to the MCU. When the pin is pulled HIGH, the data at D[7:0] will be interpreted as data. When the pin is pulled LOW, the data at D[7:0] will be transferred to a command register. In I2C mode, this pin acts as SA0 for slave address selection. When 3-wire serial interface is selected, this pin must be connected to V . SS |

| BS[2:0] | Interface |
| --- | --- |
| 000 | 4 line SPI |
| 001 | 3 line SPI |
| 110 | 8-bit 8080 parallel |
| 100 | 8-bit 6800 parallel |


<!-- page 14 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Pin Name    Pin Type Description
R/W#            I    This pin is read / write control input pin connecting to the MCU interface.
(WR#)
                        When 6800 interface mode is selected, this pin will be used as Read/Write (R/W#)
                        selection input. Read mode will be carried out when this pin is pulled HIGH and write
                        mode when LOW.
                        When 8080 interface mode is selected, this pin will be the Write (WR#) input. Data write
                        operation is initiated when this pin is pulled LOW and the chip is selected.

                        When serial or I2C interface is selected, this pin must be connected to VSS.

E (RD#)            I    This pin is MCU interface input.

                        When 6800 interface mode is selected, this pin will be used as the Enable (E) signal.
                        Read/write operation is initiated when this pin is pulled HIGH and the chip is selected.
                        When 8080 interface mode is selected, this pin receives the Read (RD#) signal. Read
                        operation is initiated when this pin is pulled LOW and the chip is selected.

                        When serial or I2C interface is selected, this pin must be connected to VSS.

D[7:0]            I/O   These pins are bi-directional data bus connecting to the MCU data bus.
                        Unused pins are recommended to tie LOW.

                        When serial interface mode is selected, D0 will be the serial clock input: SCLK; D1 will
                        be the serial data input: SID.

                        When I2C mode is selected, D2, D1 should be tied together and serve as SDAout, SDAin in
                        application and D0 is the serial clock input, SCL.

T0                I/O   This is a reserved pin. It should be kept NC.

T1                I/O   This is a reserved pin. It should be kept NC.

FR                O     This pin outputs RAM write synchronization signal. Proper timing between MCU data
                        writing and frame display timing can be achieved to prevent tearing effect.
                        It should be kept NC if it is not used.
                        Refer to Section 7.4 for details.

VBREF             O     This is a reserved pin. It should be kept NC.

SEG0 ~            O     These pins provide the OLED segment driving signals. These pins are VSS state when
SEG255                  display is OFF.

COM0 ~            O     These pins provide the Common switch signals to the OLED panel. These pins are in high
COM63                   impedance state when display is OFF.

TR0~TR10          I/O   These pins are reserved. Nothing should be connected to these pins, nor are they connected
                        together.

NC                 -    These pins are reserved. Nothing should be connected to these pins, nor are they connected
                        together.




Solomon Systech                                                          Feb 2015 P 14/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| Pin Name | Pin Type | Description |
| --- | --- | --- |
| R/W# (WR#) | I | This pin is read / write control input pin connecting to the MCU interface. When 6800 interface mode is selected, this pin will be used as Read/Write (R/W#) selection input. Read mode will be carried out when this pin is pulled HIGH and write mode when LOW. When 8080 interface mode is selected, this pin will be the Write (WR#) input. Data write operation is initiated when this pin is pulled LOW and the chip is selected. When serial or I2C interface is selected, this pin must be connected to V . SS |
| E (RD#) | I | This pin is MCU interface input. When 6800 interface mode is selected, this pin will be used as the Enable (E) signal. Read/write operation is initiated when this pin is pulled HIGH and the chip is selected. When 8080 interface mode is selected, this pin receives the Read (RD#) signal. Read operation is initiated when this pin is pulled LOW and the chip is selected. When serial or I2C interface is selected, this pin must be connected to V . SS |
| D[7:0] | I/O | These pins are bi-directional data bus connecting to the MCU data bus. Unused pins are recommended to tie LOW. When serial interface mode is selected, D0 will be the serial clock input: SCLK; D1 will be the serial data input: SID. When I2C mode is selected, D2, D1 should be tied together and serve as SDA , SDA in out in application and D0 is the serial clock input, SCL. |
| T0 | I/O | This is a reserved pin. It should be kept NC. |
| T1 | I/O | This is a reserved pin. It should be kept NC. |
| FR | O | This pin outputs RAM write synchronization signal. Proper timing between MCU data writing and frame display timing can be achieved to prevent tearing effect. It should be kept NC if it is not used. Refer to Section 7.4 for details. |
| VBREF | O | This is a reserved pin. It should be kept NC. |
| SEG0 ~ SEG255 | O | These pins provide the OLED segment driving signals. These pins are V state when SS display is OFF. |
| COM0 ~ COM63 | O | These pins provide the Common switch signals to the OLED panel. These pins are in high impedance state when display is OFF. |
| TR0~TR10 | I/O | These pins are reserved. Nothing should be connected to these pins, nor are they connected together. |
| NC | - | These pins are reserved. Nothing should be connected to these pins, nor are they connected together. |


<!-- page 15 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7     FUNCTIONAL BLOCK DESCRIPTIONS

7.1    MCU Interface selection

SSD1362 has four kinds of interface type with MCU: I2C, 3-wire or 4-wire SPI, 8-bit 6800 parallel and 8-bit
8080 parallel bus. Different MCU modes can be set by hardware selection on BS[2:0] pins; refer to Table 6-2
for BS[2:0] setting. This chip MCU interface consists of 8 data pins and 5 control pins. The pin assignment at
different interface mode is summarized in Table 7-1.

                       Table 7-1 : MCU interface assignment under different bus interface mode
    Pin Name Data/Command Interface                                                  Control Signal
Bus
Interface    D7     D6   D5     D4     D3                D2           D1     D0
                                                                             E    R/W#              CS#     D/C#    RES#
8-bit 8080                          D[7:0]                                   RD# WR#                CS#     D/C#    RES#
8-bit 6800                          D[7:0]                                   E    R/W#              CS#     D/C#    RES#
3-wire SPI   Tie LOW                                               SDIN SCLK Tie LOW                CS#     Tie LOW RES#
4-wire SPI   Tie LOW                                               SDIN SCLK Tie LOW                CS#     D/C#    RES#
I 2C         Tie LOW                                    SDAOUT     SDAIN SCL Tie LOW                        SA0     RES#



7.1.1 MCU Parallel 6800-series Interface
The parallel interface consists of 8 bi-directional data pins (D[7:0]), R/W#, D/C#, E and CS#.

A LOW in R/W# indicates WRITE operation and HIGH in R/W# indicates READ operation.
A LOW in D/C# indicates COMMAND read/write and HIGH in D/C# indicates DATA read/write.
The E input serves as data latch signal while CS# is LOW. Data is latched at the falling edge of E signal.



                                     Function           E         R/W#      CS#        D/C#
                                     Write command      ↓         L         L          L
                                     Read status        ↓         H         L          L
                                     Write data         ↓         L         L          H
                                     Read data          ↓         H         L          H

Note
(1)
    ↓ stands for falling edge of signal
    H stands for HIGH in signal
    L stands for LOW in signal

In order to match the operating frequency of display RAM with that of the microprocessor, some pipeline
processing is internally performed which requires the insertion of a dummy read before the first actual display
data read. This is shown in Figure 7-1.




SSD1362              Rev 1.0    P 15/62   Feb 2015                                                               Solomon Systech

**Extracted table(s) on this page:**

|  | ↓ | L | L | L |
| --- | --- | --- | --- | --- |
|  | ↓ | H | L | L |
|  | ↓ | L | L | H |
| Read data | ↓ | H | L | H |


<!-- page 16 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                        Figure 7-1 : Data read back procedure - insertion of dummy read

          R/W#




           E




        Databus              N                                  n                n+1                n+2

                       Write column
                                          Dummy read      Read 1st data      Read 2nd data      Read 3rd data
                         address



7.1.2 MCU Parallel 8080-series Interface
The parallel interface consists of 8 bi-directional data pins (D[7:0]), RD#, WR#, D/C# and CS#.

A LOW in D/C# indicates COMMAND read/write and HIGH in D/C# indicates DATA read/write.
A rising edge of RD# input serves as a data READ latch signal while CS# is kept LOW.
A rising edge of WR# input serves as a data/command WRITE latch signal while CS# is kept LOW.

                    Figure 7-2 : Example of Write procedure in 8080 parallel interface mode
         CS#

         WR#


         D[7:0]


         D/C#
                                             ><                ><                 )--
                      high
         RD#
                      low



                    Figure 7-3 : Example of Read procedure in 8080 parallel interface mode

       CS#

       RD#

       D[7:0]
                                      <        >--<                 >--<               )--
       D/C#

                    high
       WR#
                     low




  Solomon Systech                                                            Feb 2015 P 16/62      Rev 1.0      SSD1362

<!-- page 17 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                                          Table 7-3 : Control pins of 8080 interface
                                   Function            RD#        WR#        CS#       D/C#
                                   Write command       H          ↑          L         L
                                   Read status         ↑          H          L         L
                                   Write data          H          ↑          L         H
                                   Read data           ↑          H          L         H
Note
(1)
    ↑ stands for rising edge of signal
(2)
    H stands for HIGH in signal
(3)
    L stands for LOW in signal

In order to match the operating frequency of display RAM with that of the microprocessor, some pipeline
processing is internally performed which requires the insertion of a dummy read before the first actual display
data read. This is shown in Figure 7-4.

                       Figure 7-4 : Display data read back procedure - insertion of dummy read


  WR#




  RD#




Databus
                         (~)   N

                         Write column
                                             ( )                      n                 n+1
                                                                                                         ( )--
                                                                                                             n+2

                                             Dummy read         Read 1st data       Read 2nd data        Read 3rd data




                       ..,~•-<
               ~
                           address




7.1.3 MCU Serial Interface (4-wire SPI)
The serial interface consists of serial clock SCLK, serial data SDIN, D/C#, CS#. In SPI mode, D0 acts as
SCLK, D1 acts as SDIN. For the unused data pins from D2 to D7, E and R/W# can be connected to an
external ground.

                                     Table 7-4 : Control pins of 4-wire Serial interface
                               Function          E(RD#)       R/W#(WR#)         CS#    D/C#     D0
                               Write command     Tie LOW       Tie LOW           L      L       ↑
                               Write data        Tie LOW       Tie LOW           L      H       ↑
Note
(1)
    H stands for HIGH in signal
(2)
    L stands for LOW in signal

SDIN is shifted into an 8-bit shift register on every rising edge of SCLK in the order of D7, D6, ... D0. D/C#
is sampled on every eighth clock and the data byte in the shift register is written to the Graphic Display Data
RAM (GDDRAM) or command register in the same clock.

Under serial mode, only write operations are allowed.


SSD1362              Rev 1.0    P 17/62   Feb 2015                                                              Solomon Systech

**Extracted table(s) on this page:**

| Function | RD# | WR# | CS# | D/C# |
| --- | --- | --- | --- | --- |
| Write command | H | ↑ | L | L |
| Read status | ↑ | H | L | L |
| Write data | H | ↑ | L | H |
| Read data | ↑ | H | L | H |

| Function | E(RD#) | R/W#(WR#) | CS# | D/C# | D0 |
| --- | --- | --- | --- | --- | --- |
| Write command | Tie LOW | Tie LOW | L | L | ↑ |
| Write data | Tie LOW | Tie LOW | L | H | ↑ |


<!-- page 18 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                              Figure 7-5 : Write procedure in 4-wire Serial interface mode

      CS#
             l)-_-_-_-_-_   I
                         --
     D/C#                                            _ _ )(
     SDIN/
                      DB1           DB2                                DBn
     SCLK




               ..                                     . ............

             .
 SCLK(D0)



 SDIN(D1)             D7       D6              D5         D4                 D3              D2        D1        D0




7.1.4 MCU Serial Interface (3-wire SPI)
The 3-wire serial interface consists of serial clock SCLK, serial data SDIN and CS#.
In 3-wire SPI mode, D0 acts as SCLK, D1 acts as SDIN. For the unused data pins from D3 to D7, R/W#
(WR#), E(RD#) and D/C# can be connected to an external ground.

The operation is similar to 4-wire serial interface while D/C# pin is not used. There are altogether 9-bits will
be shifted into the shift register on every ninth clock in sequence: D/C# bit, D7 to D0 bit. The D/C# bit (first
bit of the sequential data) will determine the following data byte in the shift register is written to the Display
Data RAM (D/C# bit = 1) or the command register (D/C# bit = 0). Under serial mode, only write operations
are allowed.

                                    Table 7-5: Control pins of 3-wire Serial interface
        Function             E(RD#)            R/W#(WR#)               CS#        D/C#            D0
        Write command        Tie LOW            Tie LOW                 L         Tie LOW         ↑     Note
       I-
        Write data           Tie LOW            Tie LOW                 L         Tie LOW         ↑     (1)
                                                                                                            L stands for LOW in signal



                              Figure 7-6: Write procedure in 3-wire Serial interface mode

              CS#


              SDIN/
                              DB1              DB2                                DBn
              SCLK



             SCLK
             (D0)


        SDIN(D1)            D/C#          D7         D6                D5               D4        D3        D2        D1        D0




  Solomon Systech                                                                                 Feb 2015 P 18/62    Rev 1.0   SSD1362

**Extracted table(s) on this page:**

| Function | E(RD#) | R/W#(WR#) | CS# | D/C# | D0 |
| --- | --- | --- | --- | --- | --- |
| Write command | Tie LOW | Tie LOW | L | Tie LOW | ↑ |
| I Write data - | Tie LOW | Tie LOW | L | Tie LOW | ↑ |


<!-- page 19 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.1.5 MCU I2C Interface
The I2C communication interface consists of slave address bit SA0, I2C-bus data signal SDA (SDAOUT/D2 for
output and SDAIN/D1 for input) and I2C-bus clock signal SCL (D0). Both the data and clock signals must be
connected to pull-up resistors. RES# is used for the initialization of device.

   a) Slave address bit (SA0)
      SSD1362 has to recognize the slave address before transmitting or receiving any information by the
      I2C-bus. The device will respond to the slave address following by the slave address bit (“SA0” bit)
      and the read/write select bit (“R/W#” bit) with the following byte format,

       b7 b 6 b 5 b 4 b 3 b 2 b 1 b 0
       0 1 1 1 1 0 SA0 R/W#

       “SA0” bit provides an extension bit for the slave address. Either “0111100” or “0111101”, can be
       selected as the slave address of SSD1362. D/C# pin acts as SA0 for slave address selection.
       “R/W#” bit is used to determine the operation mode of the I2C-bus interface. R/W#=1, it is in read
       mode. R/W#=0, it is in write mode.


   b) I2C-bus data signal (SDA)
      SDA acts as a communication channel between the transmitter and the receiver. The data and the
      acknowledgement are sent through the SDA.

       It should be noticed that the ITO track resistance and the pulled-up resistance at “SDA” pin becomes
       a voltage potential divider. As a result, the acknowledgement would not be possible to attain a valid
       logic 0 level in “SDA”.

       “SDAIN” and “SDAOUT” are tied together and serve as SDA. The “SDAIN” pin must be connected to
       act as SDA. The “SDAOUT” pin may be disconnected. When “SDAOUT” pin is disconnected, the
       acknowledgement signal will be ignored in the I2C-bus.


   c) I2C-bus clock signal (SCL)
      The transmission of information in the I2C-bus is following a clock signal, SCL. Each transmission of
      data bit is taken place during a single clock period of SCL.




SSD1362          Rev 1.0   P 19/62      Feb 2015                                                             Solomon Systech

<!-- page 20 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




 7.1.5.1 I2C-bus Write data
The I2C-bus interface gives access to write data and command into the device. Please refer to Figure 7-7 for
the write mode of I2C-bus in chronological order.
                                              Figure 7-7 : I2C-bus data format


                                                                 Note:    Co – Continuation bit
                                                                          D/C# – Data / Command Selection bit
                                                                          ACK – Acknowledgement
                                                                          SA0 – Slave address bit
                                                                          R/W# – Read / Write Selection bit
         Write mode                                                       S – Start Condition / P – Stop Condition
                      SA0
                      R/W#
                      ACK
                      Co
                      D/C#




                                            ACK




                                                                   ACK
                                                                   Co
                                                                   D/C#




                                                                                            ACK




                                                                                                                        ACK
                                                                                                                          P
                             Control byte            Data byte               Control byte
S




    00 11 111 11 10                                                                                  Data byte



     Slave Address                     m ≥ 0 words                          1 byte                    n ≥ 0 bytes
                                                                                                  MSB ……………….LSB




                                                                                                                        SA0
                                                                                                                        R/W#
                                                                                                    011110

                                                                                                          SSD1362
                                                                                                        Slave Address




                                                                                                  Co
                                                                                                  D/C




                                                                                                                              ACK
                                                                                                         0 0 0 0 0 0


                                                                                                          Control byte



7.1.5.2 Write mode for I2C
    1) The master device initiates the data communication by a start condition. The definition of the start
       condition is shown in Figure 7-8. The start condition is established by pulling the SDA from HIGH to
       LOW while the SCL stays HIGH.
    2) The slave address is following the start condition for recognition use. For the SSD1362, the slave
       address is either “b0111100” or “b0111101” by changing the SA0 to LOW or HIGH (D/C pin acts as
       SA0).
    3) The write mode is established by setting the R/W# bit to logic “0”.
    4) An acknowledgement signal will be generated after receiving one byte of data, including the slave
       address and the R/W# bit. Please refer to the Figure 7-9 for the graphical representation of the
       acknowledge signal. The acknowledge bit is defined as the SDA line is pulled down during the HIGH
       period of the acknowledgement related clock pulse.
    5) After the transmission of the slave address, either the control byte or the data byte may be sent across
       the SDA. A control byte mainly consists of Co and D/C# bits following by six “0”’s.
           a. If the Co bit is set as logic “0”, the transmission of the following information will contain
               data bytes only.
           b. The D/C# bit determines the next data byte is acted as a command or a data. If the D/C# bit is
               set to logic “0”, it defines the following data byte as a command. If the D/C# bit is set to logic
               “1”, it defines the following data byte as a data which will be stored at the GDDRAM. The
               GDDRAM column address pointer will be increased by one automatically after each data
               write.
    6) Acknowledge bit will be generated after receiving each control byte or data byte.
    7) The write mode will be finished when a stop condition is applied. The stop condition is also defined
       in Figure 7-8. The stop condition is established by pulling the “SDA in” from LOW to HIGH while
       the “SCL” stays HIGH.

  Solomon Systech                                                                    Feb 2015 P 20/62         Rev 1.0          SSD1362

<!-- page 21 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                                             Figure 7-8 : Definition of the Start and Stop Condition

                                  tHSTART                                                          tSSTOP



          SDA                                                                                                                           SDA



          SCL                S
                                                                                                                                        SCL
                                                                                                             P
                        1,,. _ _ _ _ _   !                                                                           I


                   START condition                                                                    STOP condition
           - - ~ ~ - - - -                                                                                  ----
                                                                                                          LL-----!

                                         Figure 7-9 : Definition of the acknowledgement condition



              DATA OUTPUT
           BY TRANSMITTER


                                                                                                                     Non-acknowledge
                DATA OUTPUT
                 BY RECEIVER

                                                                                                                      Acknowledge
                                                                                                                                              7
                      SCL FROM
                       MASTER                                     1                 2                            8                  9
                                                    S

                                                  START                                             Clock pulse for acknowledgement
                                                 Condition


Please be noted that the transmission of the data bit has some limitations.
1. The data bit, which is transmitted during each SCL pulse, must keep at a stable state within the “HIGH”
   period of the clock pulse. Please refer to the Figure 7-10 for graphical representations. Except in start or
   stop conditions, the data line can be switched only when the SCL is LOW.
2. Both the data line (SDA) and the clock line (SCL) should be pulled up by external resistors.

                                             Figure 7-10 : Definition of the data transfer condition



                                    ;---r--~ X                                                        \
                SDA


                SCL                                                                            \
                                                  Data line is     Change
                                                  stable           of data




SSD1362               Rev 1.0        P 21/62        Feb 2015                                                                 Solomon Systech

<!-- page 22 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.2   Command Decoder
This module determines whether the input data is interpreted as data or command. Data is interpreted based
upon the input of the D/C# pin.

If D/C# pin is HIGH, the input D[7:0] is written to Graphic Display Data RAM (GDDRAM). If it is LOW,
the input D[7:0] is interpreted as a command which will be decoded and be written to the corresponding
command register.



7.3   Oscillator Circuit and Display Time Generator

This module is an On-Chip low power RC oscillator circuitry (Figure 7-11). The operation clock (CLK) can be
generated either from internal oscillator or external source CL pin. This selection is done by CLS pin. If CLS
pin is HIGH, internal oscillator is chosen and CL should be pulled to LOW. If CLS pin is LOW, external
clock from CL pin will be used for CLK for proper operation. The frequency of internal oscillator FOSC can be
programmed by command B3h.
                                         Figure 7-11: Oscillator Circuit



                             Internal
                            Oscillator
                               Fosc
                                                       M                                           DCLK
                                                            CLK                Divider
                                                       U
             CL                                        X                                         Display
                                                                                                 Clock


                                                     CLS



The display clock (DCLK) for the Display Timing Generator is derived from CLK. The division factor “D”
can be programmed from 1 to 256 by command B3h.

                                               DCLK = FOSC / D

The frame frequency of display is determined by the following formula:
                                                          Fosc
                                         FFRM =
                                                  D × K × No. of Mux
Where
• D stands for clock divide ratio. It is set by command B3h A[3:0]. The divide ratio has the range from 1 to
  256.
• K is the number of display clocks per row. The value is derived by
  K = Phase 1 period + Phase 2 period + X
     = 4 + 16 + 195 = 215 at power on reset
  Default X = GS15 + 15 = 180 + 15 = 195
• Number of multiplex ratio is set by command A8h. The reset value is 63 (i.e. 64MUX).
• Fosc is the oscillator frequency. It can be changed by command B3h A[7:4]. The higher the register setting
  results in higher frequency.

If the frame frequency is set too low, flickering may occur. On the other hand, higher frame frequency leads
to higher power consumption on the whole system.


  Solomon Systech                                                         Feb 2015 P 22/62      Rev 1.0    SSD1362

<!-- page 23 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.4   FR synchronization
FR synchronization signal can be used to prevent tearing effect.

                                      One frame
                   '
                   ,   _
FR          _      ,

                   '

       100%
      Memory
       Access
      Process
           0%
                                                                                                                          Time

                           Fast write MCU
                           Slow write MCU
          SSD1362 displaying memory updates to OLED screen


The starting time to write a new image to OLED driver is depended on the MCU writing speed. If MCU can
finish writing a frame image within one frame period, it is classified as fast write MCU. For MCU needs
longer writing time to complete (more than one frame but within two frames), it is a slow write one.

For fast write MCU: MCU should start to write new frame of ram data just after rising edge of FR pulse and
should be finished well before the rising edge of the next FR pulse.

For slow write MCU: MCU should start to write new frame ram data after the falling edge of the 1st FR pulse
and must be finished before the rising edge of the 3rd FR pulse.




SSD1362                Rev 1.0   P 23/62   Feb 2015                                                             Solomon Systech

<!-- page 24 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.5       Segment Drivers / Common Drivers
Segment drivers deliver 256 current sources to drive the OLED panel. The driving current can be adjusted up
to 600uA by altering the registers of the contrast setting command (81h). Common drivers generate voltage-
scanning pulses. The block diagrams and waveforms of the segment and common driver are shown as follow.

                            Figure 7-12: Segment and Common Driver Block Diagram

                                                           :- -- - - - - - - -
                                                                                                VCC


      :----------                      -,                                                               ISEG
                                        I




                    VCOMH
                                                                                                       I- Current
                                                                                                           Drive
              Non-select
                Row
                          -I
                                                                                                               Reset
                                            OLED
               Selected
                                            Pixel
                Row       -I                                                                 VLSS
                                                                                   Segment Driver
                            VLSS                                                                                          I
                                                                                                                       - _,

               Common Driver
      ---
      I




The commons are scanned sequentially, row by row. If a row is not selected, all the pixels on the row are in
reverse bias by driving those commons to voltage VCOMH as shown in Figure 7-13.

In the scanned row, the pixels on the row will be turned ON or OFF by sending the corresponding data signal
to the segment pins. If the pixel is turned OFF, the segment current is kept at 0. On the other hand, the
segment drives to ISEG when the pixel is turned ON.




  Solomon Systech                                                                Feb 2015 P 24/62   Rev 1.0    SSD1362

<!-- page 25 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                            Figure 7-13 : Segment and Common Driver Signal Waveform


                        One Frame Period                                              Non-selected Row
COM0
     VCOMH



       VLSS
                                                                                Selected Row


                                                                                                               ····ir
COM1
                                                      ••••                                ••••
   VCOMH



       VLSS
                               •• ••
                                       ••••
                                              •• ••
                                                      ••••
                                                             ••••
                                                                    ••••
                                                                           ••   ...
  COM                        This row is selected to
 Voltage                            turn on

 VCOMH




   VLSS
                                                                                                                                     Time
 Segment
 Voltage

                                       Waveform for ON

       VP

                                  Waveform for OFF
   VLSS
                                                                                                                                    Time

There are four phases to driving an OLED a pixel. In phase 1, the pixel is reset by the segment driver to VLSS
in order to discharge the previous data charge stored in the parasitic capacitance along the segment electrode.
The period of phase 1 can be programmed by command B1h A[3:0]. An OLED panel with larger capacitance
requires a longer period for discharging.




SSD1362           Rev 1.0    P 25/62          Feb 2015                                                                     Solomon Systech

<!-- page 26 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




In phase 2, first pre-charge is performed. The pixel is driven to attain the corresponding voltage level VP from
VLSS. The amplitude of VP can be programmed by the command BCh. The period of phase 2 can be
programmed by command B1h A[7:4]. If the capacitance value of the pixel of OLED panel is larger, a longer
period is required to charge up the capacitor to reach the desired voltage.

In phase 3, the OLED pixel is driven to the targeted driving voltage through second pre-charge. The second
pre-charge can control the speed of the charging process. The period of phase 3 can be programmed by
command B6h.

Last phase (phase 4) is current drive stage. The current source in the segment driver delivers constant current
to the pixel. The driver IC employs PWM (Pulse Width Modulation) method to control the gray scale of each
pixel individually. The gray scale can be programmed into different Gamma settings by command B8h/B9h.
The bigger gamma setting (the wider pulse widths) in the current drive stage results in brighter pixels and vice
versa. This is shown in the following figure.

                             Figure 7-14 : Gray Scale Control by PWM in Segment


                                 Phase2

                        Phase1                     Phase4
                                          Phase3
         Segment
         Voltage


            VP



            VLSS

                                                                              Wider pulse width
                                                                             drives pixel brighter



                                                                        OLED
                                                                        Panel



After finishing phase 4, the driver IC will go back to phase 1 to display the next row image data. This four-
step cycle is run continuously to refresh image display on OLED panel.

The length of phase 4 is defined by command B8h or B9h. In the table, the gray scale is defined in
incremental way, with reference to the length of previous table entry.




  Solomon Systech                                                            Feb 2015 P 26/62      Rev 1.0    SSD1362

<!-- page 27 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.6   SEG/COM Driving block
This block is used to derive the incoming power sources into the different levels of internal use voltage and
current.
    • VCC is the most positive voltage supply.
    • VCOMH is the Common deselected level. It is internally regulated.
    • VLSS is the ground path of the analog and panel current.
    • IREF is a reference current source for segment current drivers ISEG. The relationship between reference
         current and segment current of a color is:

                ISEG = Contrast / 256 * IREF * scale factor

                In which
                        the contrast (1~255) is set by Set Contrast command (81h); and
                        the scale factor is 32.


        When internal IREF is used, the IREF pin should be kept NC.
        Bit A[4] of command ADh is used to select external or internal IREF :
        A[4] = ‘0’      Select external IREF [Reset]
        A[4] = ‘1’      Enable internal IREF during display ON


        When external IREF is used, the magnitude of IREF is controlled by the value of resistor, which is
        connected between IREF pin and VSS as shown in Figure 7-15. It is recommended to set IREF to 18.75
        ±2uA so as to achieve ISEG ≈ 600uA at maximum contrast 255.


                               Figure 7-15 : IREF Current Setting by Resistor Value


                                                                SSD1362


                                        IREF ~ 18.75uA        IREF (voltage at
                                                              this pin = VCC
                                                              – 2.4V)
                                                 R1



                                                      VSS



        Since the voltage at IREF pin is VCC – 2.4V, the value of resistor R1 can be found as below:

                For IREF = 18.75uA, VCC =18V:

                R1 = (Voltage at IREF – VSS) / IREF
                   ≈ (18 – 2.4) / 18.75uA
                   = 832kΩ




SSD1362           Rev 1.0   P 27/62   Feb 2015                                                             Solomon Systech

<!-- page 28 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.7     Graphic Display Data RAM (GDDRAM)

The GDDRAM is a bit mapped static RAM holding the bit pattern to be displayed. The size of the RAM is
256x64x4 bits. For mechanical flexibility, re-mapping on both Segment and Common outputs can be selected
by software. The GDDRAM address maps in Table 7-6 to Table 7-10 show some examples on using the
command “Set Re-map” A0h to re-map the GDDRAM. In the following tables, the lower nibble and higher
nibble of D0, D1, D2 … D8189, D8190, D8191 represent the 256x64 data bytes in the GDDRAM.

Table 7-6 shows the GDDRAM map under the following condition:
• Command “Set Re-map” A0h is set to:
                           Disable Column Address Re-map                                                     (A[0]=0)
                           Disable Nibble Re-map                                                             (A[1]=0)
                           Enable Horizontal Address Increment                                               (A[2]=0)
                           Disable COM Re-map                                                                (A[4]=0)
• Display Start Line=00h
• Data byte sequence: D0, D1, D2 … D8191

                                                             Table 7-6 : GDDRAM address map 1

                                 SEG0            SEG1        SEG2           SEG3                  SEG252        SEG253     SEG254        SEG255       SEG Outputs
                                           00                          01                                  7E                       7F               Column Address
        COM0          00         D0[3:0]         D0[7:4]     D1[3:0]        D1[7:4]              D126[3:0]    D126[7:4] D127[3:0]     D127[7:4]          (HEX)
        COM1          01       D128[3:0]        D128[7:4] D129[3:0] D129[7:4]                    D254[3:0]    D254[7:4]    D255[3:0] D255[7:4]

          |           |                                                                  |

       COM62         3E        D7936[3:0] D7936[7:4] D7937[3:0] D7937[7:4]                       D8062[3:0] D8062[7:4] D8063[3:0] D8063[7:4]
       COM63          3F   D8064[3:0] D8064[7:4] D8065[3:0] D8065[7:4]                           D8190[3:0] D8190[7:4] D8191[3:0] D8191[7:4]
        COM          Row
       Outputs     Address
                    (HEX)




                                                                                                                          Nibble re-map A[1]=0

Table 7-7 shows the GDDRAM map under the following condition:
• Command “Set Re-map” A0h is set to:
                            Disable Column Address Re-map     (A[0]=0)
                            Disable Nibble Re-map             (A[1]=0)
                            Enable Vertical Address Increment (A[2]=1)
                            Disable COM Re-map                (A[4]=0)
• Display Start Line=00h
• Data byte sequence: D0, D1, D2 … D8191
                                                             Table 7-7 : GDDRAM address map 2

                                   SEG0            SEG1        SEG2            SEG3                 SEG252        SEG253     SEG254        SEG255       SEG Outputs
                                             00                          01                                  7E                       7F              Column Address
          COM0            00       D0[3:0]         D0[7:4]    D64[3:0]        D64[7:4]             D8064[3:0] D8064[7:4] D8128[3:0] D8128[7:4]              (HEX)
          COM1            01       D1[3:0]         D1[7:4]    D65[3:0]        D65[7:4]             D8065[3:0] D8065[7:4] D8129[3:0] D8129[7:4]

              |            |                                                                 |

         COM62            3E      D62[3:0]        D62[7:4]    D126[3:0] D126[7:4]                  D8126[3:0] D8126[7:4] D8190[3:0] D8190[7:4]
         COM63            3F   D63 [3:0]          D63[7:4]    D127[3:0] D127[7:4]                  D8127[3:0] D8127[7:4] D8191[3:0] D8191[7:4]
                         Row
           COM         Address
          Outputs       (HEX)
      (Display Startline=0)


                                                                                                                            Nibble re-map A[1]=0



  Solomon Systech                                                                                       Feb 2015 P 28/62            Rev 1.0       SSD1362

<!-- page 29 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Table 7-8 shows the GDDRAM map under the following condition:
• Command “Set Re-map” A0h is set to:
                           Enable Column Address Re-map                                                              (A[0]=1)
                           Enable Nibble Re-map                                                                      (A[1]=1)
                           Enable Horizontal Address Increment                                                       (A[2]=0)
                           Disable COM Re-map                                                                        (A[4]=0)
• Display Start Line=00h
• Data byte sequence: D0, D1, D2 … D8191

                                                                  Table 7-8 : GDDRAM address map 3

                                           SEG0            SEG1          SEG2              SEG3                 SEG252           SEG253        SEG254         SEG255            SEG Outputs

                                                     7F                             7E                                      01                           00                    Column Address

            COM0               00         D127[7:4]       D127[3:0]     D126[7:4]        D126[3:0]              D1[7:4]          D1[3:0]       D0[7:4]         D0[3:0]             (HEX)

            COM1               01        D255[7:4]        D255[3:0]     D254[7:4]        D254[3:0]              D129[7:4]        D129[3:0]     D128[7:4]      D128[3:0]


               |                |                                                                      |


           COM62               3E        D8063[7:4]   D8063[3:0] D8062[7:4] D8062[3:0]                         D7937[7:4]    D7937[3:0] D7936[7:4] D7936[3:0]

           COM63               3F        D8191[7:4]   D8191[3:0] D8190[7:4] D8190[3:0]                         D8065[7:4]    D8065[3:0] D8064[7:4] D8064[3:0]
                               Row
            COM
                             Address
           Outputs
                              (HEX)
    (Display Startline=0)
                                                                                                                                             Nibble re-map A[1]=1



Table 7-9 shows the example in which the display start line register is set to 78h with the following condition:
• Command “Set Re-map” A0h is set to:
                             Disable Column Address Re-map              (A[0]=0)
                             Disable Nibble Re-map                      (A[1]=0)
                             Enable Horizontal Address Increment (A[2]=0)
                             Enable COM Re-map                          (A[4]=1)
• Display Start Line=38h (corresponds to COM55)
• Data byte sequence: D0, D1, D2 … D8191

                                                                  Table 7-9 : GDDRAM address map 4

                                             SEG0            SEG1          SEG2             SEG3                  SEG252           SEG253        SEG254            SEG255          SEG Outputs

                                                      00                              01                                     7E                               7F                 Column Address

            COM55                   00      D0[3:0]          D0[7:4]       D1[3:0]          D1[7:4]               D126[3:0]        D126[7:4]     D127[3:0]         D127[7:4]          (HEX)

            COM54                   01      D128[3:0]       D128[7:4]     D129[3:0]        D129[7:4]             D254[3:0]        D254[7:4]     D255[3:0]          D255[7:4]


                   |                |                                                                      |


            COM57                   3E     D7936[3:0] D7936[7:4]         D7937[3:0]       D7937[7:4]             D8062[3:0]       D8062[7:4]    D8063[3:0]     D8063[7:4]

            COM56                   3F     D8064[3:0] D8064[7:4]         D8065[3:0]       D8065[7:4]             D8190[3:0]       D8190[7:4]    D8191[3:0]     D8191[7:4]

              COM
             Outputs

     (Display Startline=38H)
                                 Row
                               Address
                                (HEX)                                                                                                                y
                                                                                                                                               Nibble re-map A[1]=0




SSD1362                     Rev 1.0        P 29/62           Feb 2015                                                                                                 Solomon Systech

<!-- page 30 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Table 7-10 shows the GDDRAM map under the following condition:
• Command “Set Re-map” A0h is set to:
                           Disable Column Address Re-map       (A[0]=0)
                           Disable Nibble Re-map               (A[1]=0)
                           Enable Horizontal Address Increment (A[2]=0)
                           Disable COM Re-map                  (A[4]=0)
• Display Start Line=00h
• Column Start Address=01h
• Column End Address=7Eh
• Row Start Address=01h
• Row End Address=3Eh
• Data byte sequence: D0, D1, D2 … D7811

                                                     Table 7-10 : GDDRAM address map 5

                                       SEG0        SEG1     SEG2            SEG3           SEG252           SEG253      SEG254        SEG255      SEG Outputs
                                              00                       01                              7E                        7F            Column Address
             COM0              00                                                                                                                    (HEX)
             COM1              01                          D0[3:0]          D0[7:4]        D125[3:0]        D125[7:4]


                |               |                                                     |


            COM62              3E                         D7686[3:0]    D7686[7:4]        D7811[3:0]    D7811[7:4]

            COM63              3F
                               Row
             COM
                             Address
            Outputs
                              (HEX)
     (Display Startline=0)
                                                                                           Nibble re-map A[1]=0


Notes:
(1]
    Please refer to Command Table for the details of setting command “Set Re-map”A0h.
(2)
    The “Display Start Line” is set by the command “Set Display Start Line” A1h.
(3)
    The “Column Start/End Address” is set by the command “Set Column Address” 15h.
(4)
    The “Row Start/End Address” is set by the command “Set Row Address” 75h.




  Solomon Systech                                                                         Feb 2015 P 30/62               Rev 1.0        SSD1362

<!-- page 31 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.8   Gray Scale Decoder

The gray scale effect is generated by controlling the pulse width (PW) of current drive phase, except GS0
there is no pre-charge (phase 2, 3) and current drive (phase 4). The driving period is controlled by the gray
scale settings (setting 0 ~ setting 255). The larger the setting, the brighter the pixel will be. The Gray Scale
Table stores the corresponding gray scale setting of the 16 gray scale levels (GS0~GS15) through the
software commands B8h or B9h.

As shown in Figure 7-16, GDDRAM data has 4 bits, represent the 16 gray scale levels from GS0 to GS15.
Note that the frame frequency is affected by GS15 setting.

Figure 7-16 : Relation between GDDRAM content and Gray Scale table entry (under command B9h Enable Linear Gray Scale
                                                      Table)
                                                                               Default Gamma Setting
      GDDRAM data (4 bits)             Gray Scale Table
                                                                                  (Command B9h)
               0000                         GS0 (1)                                   Setting 0
               0001                          GS1                                     Setting 12
               0010                          GS2                                     Setting 24
               0011                          GS3                                     Setting 36
                 :                            :                                           :
                 :                            :                                           :
               1101                         GS13                                    Setting 156
               1110                         GS14                                    Setting 168
               1111                         GS15                                    Setting 180

Note:
(1)
    GS0 has no pre-charge (phase 2, 3) and current drive (phase 4).




SSD1362           Rev 1.0   P 31/62   Feb 2015                                                             Solomon Systech

**Extracted table(s) on this page:**

| GDDRAM data (4 bits) | Gray Scale Table | Default Gamma Setting (Command B9h) |
| --- | --- | --- |
| 0000 | GS0 (1) | Setting 0 |
| 0001 | GS1 | Setting 12 |
| 0010 | GS2 | Setting 24 |
| 0011 | GS3 | Setting 36 |
| : | : | : |
| : | : | : |
| 1101 | GS13 | Setting 156 |
| 1110 | GS14 | Setting 168 |
| 1111 | GS15 | Setting 180 |


<!-- page 32 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




7.9       Power ON and OFF sequence
The following figures illustrate the recommended power ON and power OFF sequence of SSD1362 (assume
VCI and VDDIO are at the same voltage level and internal VDD is used).
Power ON sequence:
   1. Power ON VCI, VDDIO.
   2. After VCI, VDDIO becomes stable, set wait time at least 1ms (t0) for internal VDD become stable. Then
       set RES# pin LOW (logic low) for at least 100us (t1) (4) and then HIGH (logic high).
   3. After set RES# pin LOW (logic low), wait for at least 100us (t2). Then Power ON VCC.
   4. After VCC become stable, send command AFh for display ON. SEG/COM will be ON after 200ms
       (tAF).
   5. After VCI, VDDIO become stable, wait for at least 50ms to send command.
                                             Figure 7-17 : The Power ON sequence.

                          ON VCI, VDDIO       RES#          ON VCC   Send AFh command for Display ON

       VCI, VDDIO
                                             t0
         OFF
                                                  t1

         RES#

         GND
                                                       t2
          VCC

         OFF



                                                                                                    ,---
                                                                                                        I
                                                                                     tAF
                                                                                                   •:                           ON
       SEG/COM
                                                                                                        I- .. - ..
                                                                                                        I                       OFF

Power OFF sequence:
   1. Send command AEh for display OFF.
   2. Power OFF VCC.(1), (2)
   3. Wait for tOFF. Power OFF VCI. (Typical tOFF=100ms(4))
                                             Figure 7-18 : The Power OFF sequence

           Send command AEh for display OFF            OFF VCC               OFF VCI, VDDIO


                                                        ~
                                         I              I
                         VCC             I

                        OFF
                                 _____ !I __ ----- ]\                                  :I
                                         I              I                              I
                                                                     tOFF
                    VCI, VDDIO
                                         I              :~-                            !
                                         I              I
                        OFF ·-. - . - . -·-·r·-·-·-·-·-l
                                            .I         I                             '\
                                                       !-·-·-·-·-·-·-·-·-·-·-·-·-·-·~--.    ----
Note:
(1)
    VCC should be kept float (disable) when it is OFF.
(2)
    Power pins (VCI, VDDIO, VCC) can never be pulled to ground under any circumstance.
(3)
    The register values are reset after t1.
(4)
    VCI and VDDIO should not be Power OFF before VCC Power OFF.




      Solomon Systech                                                           Feb 2015 P 32/62            Rev 1.0   SSD1362

**Extracted table(s) on this page:**

| I !_ _ I ----- ] |  |
| --- | --- |
| I I | I :~- t OFF |
| I rI ·-·-·-·-·-l | I I |


<!-- page 33 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




 7.10 VDD Regulator

 In SSD1362, the power supply pin for core logic operation, VDD, can be supplied by external source or
 internally regulated through the VDD regulator.

 The internal VDD regulator is enabled by setting bit A[0] to 1b in command ABh “Function Selection”.
 VCI should be larger than 2.6V when using the internal VDD regulator. It should be noticed that, no matter VDD
 is supplied by external source or internally regulated; VCI must always be set equivalent to or higher than VDD.

 Table 7-11 summarizes the input / output connection of VCI, VDDIO and VDD.

                                       Table 7-11: IO regulator pin description
Pin Name                VCI≤2.6V Application                                        VCI>2.6V Application
VCI                           1.65V – 2.6V                                                 2.6V – 3.5V
VDDIO                          1.65V – VCI                                                 1.65V – VCI

                                                                                NC with stabilizing capacitor
VDD                            1.65V – VCI                                        It is internally regulated

                       VDD Regulator Disable,                                VCI>2.6V, VDD Regulator Enable,
                       Command: ABh A[0]=0b.                                     Command: ABh A[0]=1b.
                 VCI                         VSS   VDD                 VCI                               VSS    VDD
Pin
connection
scheme



                VCI                                VDD                 VCI                               GND
                                           GND


 No RAM access through MCU interface when there is no external / internal VDD.




 7.11 Reset Circuit

 When RES# input is LOW, the chip is initialized with the following status:
   1. Display is OFF
   2. 256 x 64 Display Mode
   3. Normal segment and display data column address and row address mapping (SEG0 mapped to
       address 00h and COM0 mapped to address 00h)
   4. Shift register data clear in serial interface
   5. Display start line is set at display RAM address 0
   6. Column address counter is set at 0
   7. Normal scan direction of the COM outputs
   8. Contrast control register is set at 7Fh
   9. Normal display mode (Equivalent to A4h command)




  SSD1362          Rev 1.0   P 33/62   Feb 2015                                                              Solomon Systech

**Extracted table(s) on this page:**

| Pin Name | V ≤2.6V Application CI | V >2.6V Application CI |
| --- | --- | --- |
| V CI | 1.65V – 2.6V | 2.6V – 3.5V |
| V DDIO | 1.65V – V CI | 1.65V – V CI |
| V DD | 1.65V – V CI | NC with stabilizing capacitor It is internally regulated |
| Pin connection scheme | V Regulator Disable, DD Command: ABh A[0]=0b. V CI V SS V DD V CI GND V DD | V >2.6V, V Regulator Enable, CI DD Command: ABh A[0]=1b. V CI V SS V DD V CI GND |


<!-- page 34 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




      8     COMMAND TABLE

                                                  Table 8-1: Command Table
                                 (R/W# (WR#) = 0, E(RD#) = 1 unless specific setting is stated)

1. Fundamental Command Table
D/C#     Hex      D7 D6 D5            D4     D3    D2     D1     D0      Command          Description
   0      15       0    0    0        1      0     1      0      1       Set Column       Setup Column start and end address
   0    A[6:0]     *   A6    A5       A4     A3    A2     A1     A0       Address         A[6:0]: Start Address, range:00h~7Fh,
   0    B[6:0]     *   B6    B5       B4     B3    B2     B1     B0                       (RESET = 00h)

                                                                                          B[6:0]: End Address, range:00h~7Fh,
                                                                                          (RESET = 7Fh)

 0         75         0     1    1     1     0      1     0      1 Set Row Address Setup Row start and end address
 0        A[5:0]      *     *    A5    A4    A3     A2    A1     A0                A[5:0]: Start Address, range:00h~3Fh,
 0        B[5:0]      *     *    B5    B4    B3     B2    B1     B0                (RESET = 00h)

                                                                                          B[5:0]: End Address, range:00h~3Fh,
                                                                                          (RESET = 3Fh)

 0         81         1     0    0     0     0      0     0      1       Set Contrast     Double byte command to select one of the
 0        A[7:0]      A7    A6   A5    A4    A3     A2    A1     A0        Control        contrast steps. Contrast increases as the value
                                                                                          increases.
                                                                                          (RESET = 7Fh )


 00        A0         1     0    1     0      0     0     0      0       Set Re-map       Re-map setting in Graphic Display Data RAM
  0       A[7:0]      A7    A6   0     A4     0     A2    A1     A0                       (GDDRAM)

                                                                                          A[0] = 0b, Disable Column Address Re-map
                                                                                          (RESET)
                                                                                          A[0] = 1b, Enable Column Address Re-map

                                                                                          A[1] = 0b, Disable Nibble Re-map (RESET)
                                                                                          A[1] = 1b, Enable Nibble Re-map

                                                                                          A[2] = 0b, Enable Horizontal Address
                                                                                          Increment (RESET)
                                                                                          A[2] = 1b, Enable Vertical Address Increment

                                                                                          A[4] = 0b, Disable COM Re-map (RESET)
                                                                                          A[4] = 1b, Enable COM Re-map

                                                                                          A[6] = 0b, Disable SEG Split Odd Even
                                                                                          A[6] = 1b, Enable SEG Split Odd Even
                                                                                          (RESET)

                                                                                          A[7] = 0b, Disable SEG left/right remap
                                                                                          (RESET)
                                                                                          A[7] = 1b, Enable SEG left/right remap

 0         A1         1     0    1     0     0      0     0      1 Set Display Start A[5:0]: Vertical shift by setting the starting
 0        A[5:0]      *     *    A5    A4    A3     A2    A1     A0      Line                address of display RAM from 0 ~ 63
                                                                                             (RESET = 00h)




          Solomon Systech                                                        Feb 2015 P 34/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| 1.Fundamental Command Table |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D/C# | Hex | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Command | Description |
| 0 0 0 | 15 A[6:0] B[6:0] | 0 * * | 0 A 6 B 6 | 0 A 5 B 5 | 1 A 4 B 4 | 0 A 3 B 3 | 1 A 2 B 2 | 0 A 1 B 1 | 1 A 0 B 0 | Set Column Address | Setup Column start and end address A[6:0]: Start Address, range:00h~7Fh, (RESET = 00h) B[6:0]: End Address, range:00h~7Fh, (RESET = 7Fh) |
| 0 0 0 | 75 A[5:0] B[5:0] | 0 * * | 1 * * | 1 A 5 B 5 | 1 A 4 B 4 | 0 A 3 B 3 | 1 A 2 B 2 | 0 A 1 B 1 | 1 A 0 B 0 | Set Row Address | Setup Row start and end address A[5:0]: Start Address, range:00h~3Fh, (RESET = 00h) B[5:0]: End Address, range:00h~3Fh, (RESET = 3Fh) |
| 0 0 | 81 A[7:0] | 1 A 7 | 0 A 6 | 0 A 5 | 0 A 4 | 0 A 3 | 0 A 2 | 0 A 1 | 1 A 0 | Set Contrast Control | Double byte command to select one of the contrast steps. Contrast increases as the value increases. (RESET = 7Fh ) |
| 00 0 | A0 A[7:0] | 1 A 7 | 0 A 6 | 1 0 | 0 A 4 | 0 0 | 0 A 2 | 0 A 1 | 0 A 0 | Set Re-map | Re-map setting in Graphic Display Data RAM (GDDRAM) A[0] = 0b, Disable Column Address Re-map (RESET) A[0] = 1b, Enable Column Address Re-map A[1] = 0b, Disable Nibble Re-map (RESET) A[1] = 1b, Enable Nibble Re-map A[2] = 0b, Enable Horizontal Address Increment (RESET) A[2] = 1b, Enable Vertical Address Increment A[4] = 0b, Disable COM Re-map (RESET) A[4] = 1b, Enable COM Re-map A[6] = 0b, Disable SEG Split Odd Even A[6] = 1b, Enable SEG Split Odd Even (RESET) A[7] = 0b, Disable SEG left/right remap (RESET) A[7] = 1b, Enable SEG left/right remap |
| 0 0 | A1 A[5:0] | 1 * | 0 * | 1 A 5 | 0 A 4 | 0 A 3 | 0 A 2 | 0 A 1 | 1 A 0 | Set Display Start Line | A[5:0]: Vertical shift by setting the starting address of display RAM from 0 ~ 63 (RESET = 00h) |


<!-- page 35 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




1. Fundamental Command Table
D/C#     Hex      D7 D6 D5            D4    D3        D2   D1   D0       Command         Description
   0      A2       1    0    1        0     0         0    1    0        Set Display     A[5:0]: Set vertical offset by COM from 0 ~
   0    A[5:0]     *    *    A5       A4    A3        A2   A1   A0         Offset                63 (RESET = 00h)

                                                                                         e.g. Set A[5:0] to 010000b to move COM16
                                                                                              towards COM0 direction for 16 row

 0       A3        1     0       1    0      0        0    1    1       Set Vertical     A[5:0]: Number of rows in top fixed area. The
 0      A[5:0]     *     *       A5   A4     A3       A2   A1   A0      Scroll Area              No. of rows in top fixed area is
 0      B[6:0]     *     B6      B5   B4     B3       B2   B1   B0                               referenced to the top of the
                                                                                                 GDDRAM (i.e. row 0).
                                                                                                 (RESET = 00h)
                                                                                         B[6:0]: Number of rows in the scroll area.
                                                                                                 This is the number of rows to be used
                                                                                                 for vertical scrolling. The scroll area
                                                                                                 starts in the first row below the top
                                                                                                 fixed area. (RESET = 40h)

                                                                                         Note
                                                                                         (1)
                                                                                             A[5:0]+B[6:0] <= MUX ratio
                                                                                         (2)
                                                                                             B[6:0] <= MUX ratio
                                                                                         (3)
                                                                                             Set Display Start Line (A[5:0] in A1h) <
                                                                                             B[6:0]
                                                                                         (4)
                                                                                             The last row of the scroll area shifts to the
                                       0     0        1    X1   X0                       first row of the scroll area.
                                                                                         (5)
                                                                                             For 64d MUX display
                                                                                             A[5:0] = 0, B[5:0]=64 : whole area scrolls
                                                                                             A[5:0]= 0, B[5:0] < 64 : top area scrolls
                                                                                             A[5:0] + B[5:0] < 64 : central area scrolls
                                                                                             A[5:0] + B[5:0] = 64 : bottom area scrolls

 0     A4 ~ A7     1      0      1                                       Set Display     A4h = Normal display (RESET)
                                                                            Mode
                                                                                         A5h = All ON (All pixels have gray scale of
                                                                                               15, GS15)

                                                                                         A6h = All OFF (All pixels have gray scale of
                                                                                               0, GS0)

                                                                                         A7h = Inverse Display (GS0    GS15, GS1
                                                                                                  GS14, GS2      GS13, …)

 0       A8        1      0      1    0      1        0    0    0     Set MUX Ratio A[5:0]: Set MUX ratio from 4MUX ~
 0      A[5:0]     *      *      A5   A4     A3       A2   A1   A0                  64MUX:
                                                                                    A[5:0] = 3 represents 4MUX
                                                                                    A[5:0] = 4 represents 5MUX
                                                                                            :
                                                                                    A[5:0] = 62 represents 63MUX
                                                                                    A[5:0] = 63 represents 64MUX (RESET)

                                                                                         It should be noted that A[5:0]=0~2 is not
                                                                                         allowed

 0       AB        1      0      1     0     1        0    1    1        Function        A[0]=0b, Select external VDD (i.e. Disable
 0       A[0]      0      0      0     0     0        0    0    A0      Selection A      internal VDD regulator)

                                                                                         A[0]=1b, Enable internal VDD regulator
                                                                                         (RESET)



      SSD1362          Rev 1.0   P 35/62   Feb 2015                                                             Solomon Systech

**Extracted table(s) on this page:**

| 1.Fundamental Command Table |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D/C# | Hex | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Command | Description |
| 0 0 | A2 A[5:0] | 1 * | 0 * | 1 A 5 | 0 A 4 | 0 A 3 | 0 A 2 | 1 A 1 | 0 A 0 | Set Display Offset | A[5:0]: Set vertical offset by COM from 0 ~ 63 (RESET = 00h) e.g. Set A[5:0] to 010000b to move COM16 towards COM0 direction for 16 row |
| 0 0 0 | A3 A[5:0] B[6:0] | 1 * * | 0 * B 6 | 1 A 5 B 5 | 0 A 4 B 4 0 | 0 A 3 B 3 0 | 0 A 2 B 2 1 | 1 A 1 B 1 X 1 | 1 A 0 B 0 X 0 | Set Vertical Scroll Area | A[5:0]: Number of rows in top fixed area. The No. of rows in top fixed area is referenced to the top of the GDDRAM (i.e. row 0). (RESET = 00h) B[6:0]: Number of rows in the scroll area. This is the number of rows to be used for vertical scrolling. The scroll area starts in the first row below the top fixed area. (RESET = 40h) Note (1)A[5:0]+B[6:0] <= MUX ratio (2) B[6:0] <= MUX ratio (3)Set Display Start Line (A[5:0] in A1h) < B[6:0] (4)The last row of the scroll area shifts to the first row of the scroll area. (5)For 64d MUX display A[5:0] = 0, B[5:0]=64 : whole area scrolls A[5:0]= 0, B[5:0] < 64 : top area scrolls A[5:0] + B[5:0] < 64 : central area scrolls A[5:0] + B[5:0] = 64 : bottom area scrolls |
| 0 | A4 ~ A7 | 1 | 0 | 1 |  |  |  |  |  | Set Display Mode | A4h = Normal display (RESET) A5h = All ON (All pixels have gray scale of 15, GS15) A6h = All OFF (All pixels have gray scale of 0, GS0) A7h = Inverse Display (GS0 (cid:1) GS15, GS1 (cid:1) GS14, GS2 (cid:1) GS13, …) |
| 0 0 | A8 A[5:0] | 1 * | 0 * | 1 A 5 | 0 A 4 | 1 A 3 | 0 A 2 | 0 A 1 | 0 A 0 | Set MUX Ratio | A[5:0]: Set MUX ratio from 4MUX ~ 64MUX: A[5:0] = 3 represents 4MUX A[5:0] = 4 represents 5MUX : A[5:0] = 62 represents 63MUX A[5:0] = 63 represents 64MUX (RESET) It should be noted that A[5:0]=0~2 is not allowed |
| 0 0 | AB A[0] | 1 0 | 0 0 | 1 0 | 0 0 | 1 0 | 0 0 | 1 0 | 1 A 0 | Function Selection A | A[0]=0b, Select external V (i.e. Disable DD internal V regulator) DD A[0]=1b, Enable internal V regulator DD (RESET) |


<!-- page 36 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




1. Fundamental Command Table
D/C#     Hex      D7 D6 D5         D4   D3   D2     D1     D0       Command         Description
   0     AD        1    0    1     0    1    1      0      1         External /     Select external or internal IREF :
   0     A[4]      1    0    0     A4   1    1      1      0       Internal IREF    A[4] = ‘0’ Select external IREF (RESET)
                                                                     Selection      A[4] = ‘1’ Enable internal IREF during display
                                                                                    ON

 0     AE / AF     1     0    1    0    1     1      1     X0       Set Display     AEh = Display OFF (sleep mode) (RESET)
                                                                     ON/OFF         AFh = Display ON in normal mode

 0       B1        1     0    1    1    0    0      0      1 Set Phase Length A[3:0]: Phase 1 period of 2~30 DCLK’s
 0      A[7:0]     A7    A6   A5   A4   A3   A2     A1     A0                         (i.e. 2, 4, 6, 8…30)
                                                                                      (RESET = 0010b)

                                                                                    A[7:4]: Phase 2 period of 2~30 DCLK’s
                                                                                             (i.e. 2, 4, 6, 8…30)
                                                                                             (RESET = 1000b)

                                                                                    Note
                                                                                    (1)
                                                                                        GS15 level pulse width must be set larger
                                                                                    than the period of phase 1 + phase 2

 0       B3        1     0    1    1    0    0      1      1     Set Front Clock A[3:0]: Define divide ratio (D) of display
 0      A[7:0]     A7    A6   A5   A4   A3   A2     A1     A0        Divider            clock (DCLK)
                                                                   /Oscillator          (i.e. 1, 2, 4, 8…256)
                                                                   Frequency            (RESET is 0001b, i.e. divide ratio = 2)

                                                                                    A[7:4]: Set the Oscillator Frequency, FOSC.
                                                                                            Oscillator Frequency increases with
                                                                                            the value of A[7:4] and vice versa.
                                                                                            (Range:0000b~1111b)
                                                                                             (RESET = 1010b)


 0       B5        1     0    1    1    0    1      0      1           GPIO         A[1:0] = 00b represents GPIO0 pin HiZ,
 0      A[3:0]     0     0    0    0    A3   A2     A1     A0                               input disable (always read as low)
                                                                                    A[1:0] = 01b represents GPIO0 pin HiZ,
                                                                                            input enable
                                                                                    A[1:0] = 10b represents GPIO0 pin output
                                                                                            Low (RESET)
                                                                                    A[1:0] = 11b represents GPIO0 pin output
                                                                                            High
                                                                                    A[3:2] = 00b represents GPIO1 pin HiZ,
                                                                                            input disable (always read as low)
                                                                                    A[3:2] = 01b represents GPIO1 pin HiZ,
                                                                                            input enable
                                                                                    A[3:2] = 10b represents GPIO1 pin output
                                                                                            Low (RESET)
                                                                                    A[3:2] = 11b represents GPIO1 pin output
                                                                                            High


 0       B6        1     0    1    1    0    1      1      0     Set Second pre- A[3:0]: Second Pre-charge period of 1~15
 0      A[3:0]     *     *    *    *    A3   A2     A1     A0     charge Period           DCLK’s
                                                                                          e.g. A[3:0] = 1111b, 15 DCLK
                                                                                          Clock
                                                                                           (RESET = 0100b)




       Solomon Systech                                                     Feb 2015 P 36/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| 1.Fundamental Command Table |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D/C# | Hex | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Command | Description |
| 0 0 | AD A[4] | 1 1 | 0 0 | 1 0 | 0 A 4 | 1 1 | 1 1 | 0 1 | 1 0 | External / Internal I REF Selection | Select external or internal I : REF A[4] = ‘0’ Select external I (RESET) REF A[4] = ‘1’ Enable internal I during display REF ON |
| 0 | AE / AF | 1 | 0 | 1 | 0 | 1 | 1 | 1 | X 0 | Set Display ON/OFF | AEh = Display OFF (sleep mode) (RESET) AFh = Display ON in normal mode |
| 0 0 | B1 A[7:0] | 1 A 7 | 0 A 6 | 1 A 5 | 1 A 4 | 0 A 3 | 0 A 2 | 0 A 1 | 1 A 0 | Set Phase Length | A[3:0]: Phase 1 period of 2~30 DCLK’s (i.e. 2, 4, 6, 8…30) (RESET = 0010b) A[7:4]: Phase 2 period of 2~30 DCLK’s (i.e. 2, 4, 6, 8…30) (RESET = 1000b) Note (1)GS15 level pulse width must be set larger than the period of phase 1 + phase 2 |
| 0 0 | B3 A[7:0] | 1 A 7 | 0 A 6 | 1 A 5 | 1 A 4 | 0 A 3 | 0 A 2 | 1 A 1 | 1 A 0 | Set Front Clock Divider /Oscillator Frequency | A[3:0]: Define divide ratio (D) of display clock (DCLK) (i.e. 1, 2, 4, 8…256) (RESET is 0001b, i.e. divide ratio = 2) A[7:4]: Set the Oscillator Frequency, F . OSC Oscillator Frequency increases with the value of A[7:4] and vice versa. (Range:0000b~1111b) (RESET = 1010b) |
| 0 0 | B5 A[3:0] | 1 0 | 0 0 | 1 0 | 1 0 | 0 A 3 | 1 A 2 | 0 A 1 | 1 A 0 | GPIO | A[1:0] = 00b represents GPIO0 pin HiZ, input disable (always read as low) A[1:0] = 01b represents GPIO0 pin HiZ, input enable A[1:0] = 10b represents GPIO0 pin output Low (RESET) A[1:0] = 11b represents GPIO0 pin output High A[3:2] = 00b represents GPIO1 pin HiZ, input disable (always read as low) A[3:2] = 01b represents GPIO1 pin HiZ, input enable A[3:2] = 10b represents GPIO1 pin output Low (RESET) A[3:2] = 11b represents GPIO1 pin output High |
| 0 0 | B6 A[3:0] | 1 * | 0 * | 1 * | 1 * | 0 A 3 | 1 A 2 | 1 A 1 | 0 A 0 | Set Second pre- charge Period | A[3:0]: Second Pre-charge period of 1~15 DCLK’s e.g. A[3:0] = 1111b, 15 DCLK Clock (RESET = 0100b) |


<!-- page 37 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




1. Fundamental Command Table
D/C#      Hex      D7 D6 D5 D4 D3 D2 D1 D0                 Command Description
   0      B8        1    0    1    1    1   0    0     0  Set Gray Scale The next 15 data bytes set the gray scale pulse
   0    A1[7:0]   A17 A16 A15 A14 A13 A12 A11 A10             Table      width in unit of DCLK’s.
   0    A2[7:0]   A27 A26 A25 A24 A23 A22 A21 A20
  …       …        ...  ...  ...  ...  ...  ...  ...  ...                A1[7:0], value for GS1 level Pulse width
  …       …        ...  ...  ...  ...  ...  ...  ...  ...                A2[7:0], value for GS2 level Pulse width
                                                                                     …
  …       …        ...  ...  ...  ...  ...  ...  ...  ...
                                                                         A14[7:0], value for GS14 level Pulse width
   0    A14[7:0]  A147 A146 A145 A144 A143 A142 A141 A140                A15[7:0], value for GS15 level Pulse width
   0    A15[7:0]  A157 A156 A155 A154 A153 A152 A151 A150
                                                                                           Note
                                                                                           (1)
                                                                                               The pulse width value of GS1, GS2, .... ,
                                                                                           GS15 should not be equal. i.e.
                                                                                           0<GS1<GS2 … <GS15
                                                                                           (2)
                                                                                               GS15 level pulse width must be set larger
                                                                                           than the period of phase 1 + phase 2
                                                                                           (3)
                                                                                               GS15 level must be set larger than 140 (ie.
                                                                                           8Ch)

 0        B9         1      0      1     1     1        0    0     1      Linear LUT       The default Linear Gray Scale table is set in
                                                                                           unit of DCLK’s as follow

                                                                                           GS0 level pulse width = 0;
                                                                                           GS1 level pulse width = 12;
                                                                                           GS2 level pulse width =24;
                                                                                           GS3 level pulse width = 36;
                                                                                                   :
                                                                                           GS14 level pulse width = 168;
                                                                                           GS15 level pulse width = 180

 0        BC         1      0      1    1      1        1    0    0      Set Pre-charge Set pre-charge voltage level.
 0       A[4:0]      0      0      0    A4     A3       A2   A1   A0         voltage
                                                                                          A[4:0]      Hex Pre-charge voltage
                                                                                                      code
                                                                                            00000     00h           0.10 x VCC
                                                                                               :        :                :
                                                                                            00100     04h     0.15 x VCC (RESET)
                                                                                               :        :                :
                                                                                            11111     1Fh           0.51 x VCC



 0       BD          1      0      1     1     1        1    0    0     Pre-charge A[0]=0b, Without external VP capacitor
 0       A[0]        0      0      0     0     0        0    0    A0 voltage capacitor (RESET)
                                                                         Selection
                                                                                       A[0]=1b, With external VP capacitor

 0        BE         1      0      1     1     1        1    1    0        Set VCOMH       Set COM deselect voltage level.
 0       A[3:0]      0      0      0     0     A3       A2   A1   A0                        A[3:0] Hex          V COMH
                                                                                                    code
                                                                                             0000     00h             0.72 x VCC
                                                                                               :        :                  :
                                                                                             0101     05h       0.82 x VCC (RESET)
                                                                                               :        :                  :
                                                                                             0111     07h             0.86 x VCC




      SSD1362            Rev 1.0   P 37/62   Feb 2015                                                             Solomon Systech

**Extracted table(s) on this page:**

| A[3:0] | Hex code |
| --- | --- |
| 0000 | 00h |
| : | : |
| 0101 | 05h |
| : | : |
| 0111 | 07h |


<!-- page 38 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




1. Fundamental Command Table
D/C#     Hex      D7 D6 D5              D4   D3   D2     D1     D0      Command Description
   0      FD       1    1    1          1    1    1      0      1      Set Command A[2]: MCU protection status.
   0     A[2]      0    0    0          1    0    A2     1      0          Lock
                                                                                   A[2] = 0b, Unlock OLED driver IC MCU
                                                                                   interface from entering command (RESET)
                                                                                   A[2] = 1b, Lock OLED driver IC MCU
                                                                                   interface from entering command

                                                                                         Note
                                                                                         (1)
                                                                                             The locked OLED driver IC MCU
                                                                                         interface prohibits all commands and memory
                                                                                         access except the FDh command

 0       23          0     0     1      0    0    0      1      1 Set Fade In / Out A[5:4] = 00b, Disable fade mode (RESET)
 0      A[5:0]       *     *     A5     A4   A3   A2     A1     A0 and Blinking
                                                                                    A[5:4] = 01b, Enable fade in mode, Once
                                                                                    Fade In Mode is enabled, enter a new contrast
                                                                                    setting by 81h command and contrast will
                                                                                    increase gradually to the target contrast
                                                                                    setting. Output follows the latest contrast
                                                                                    setting when Fade mode is disabled.

                                                                                         Note:
                                                                                         (1) The new contrast setting must be larger
                                                                                         than the original contrast setting before Fade
                                                                                         In Mode is enabled.


                                                                                         A[5:4] = 10b, Enable fade out mode, Once
                                                                                         Fade Out Mode is enabled, contrast decrease
                                                                                         gradually to all pixels OFF. Output follows
                                                                                         RAM content when Fade mode is disabled.

                                                                                         A[5:4] = 11b Enable Blinking mode.
                                                                                         Once Blinking Mode is enabled, contrast
                                                                                         decrease gradually to all pixels OFF and then
                                                                                         contrast increase gradually to normal display.
                                                                                         This process loop continuously until the
                                                                                         Blinking mode is disabled.


                                                                                         A[3:0], Set the time interval for each fade step
                                                                                                 A[3:0] Time interval / step
                                                                                                  0000           8 frames
                                                                                                  0001          16 frames
                                                                                                  0010          24 frames
                                                                                                   …                …
                                                                                                  1110         120 frames
                                                                                                  1111         128 frames


     Note
     (1) “*” stands for “Don’t care”.




       Solomon Systech                                                          Feb 2015 P 38/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| 1.Fundamental Command Table |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D/C# | Hex | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Command | Description |
| 0 0 | FD A[2] | 1 0 | 1 0 | 1 0 | 1 1 | 1 0 | 1 A 2 | 0 1 | 1 0 | Set Command Lock | A[2]: MCU protection status. A[2] = 0b, Unlock OLED driver IC MCU interface from entering command (RESET) A[2] = 1b, Lock OLED driver IC MCU interface from entering command Note (1) The locked OLED driver IC MCU interface prohibits all commands and memory access except the FDh command |
| 0 0 | 23 A[5:0] | 0 * | 0 * | 1 A 5 | 0 A 4 | 0 A 3 | 0 A 2 | 1 A 1 | 1 A 0 | Set Fade In / Out and Blinking | A[5:4] = 00b, Disable fade mode (RESET) A[5:4] = 01b, Enable fade in mode, Once Fade In Mode is enabled, enter a new contrast setting by 81h command and contrast will increase gradually to the target contrast setting. Output follows the latest contrast setting when Fade mode is disabled. Note: The new contrast setting must be larger (1) than the original contrast setting before Fade In Mode is enabled. A[5:4] = 10b, Enable fade out mode, Once Fade Out Mode is enabled, contrast decrease gradually to all pixels OFF. Output follows RAM content when Fade mode is disabled. A[5:4] = 11b Enable Blinking mode. Once Blinking Mode is enabled, contrast decrease gradually to all pixels OFF and then contrast increase gradually to normal display. This process loop continuously until the Blinking mode is disabled. A[3:0], Set the time interval for each fade step A[3:0] Time interval / step 0000 8 frames 0001 16 frames 0010 24 frames … … 1110 120 frames 1111 128 frames |

| A[3:0] | Time interval / step |
| --- | --- |
| 0000 | 8 frames |
| 0001 | 16 frames |
| 0010 | 24 frames |
| … | … |
| 1110 | 120 frames |
| 1111 | 128 frames |


<!-- page 39 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




8.1   Data Read / Write

To read data from the GDDRAM, select HIGH for both the R/W# (WR#) pin and the D/C# pin for 6800-
series parallel mode and select LOW for the E (RD#) pin and HIGH for the D/C# pin for 8080-series parallel
mode. No data read is provided in serial mode operation.
In normal data read mode the GDDRAM column address pointer will be increased automatically by one after
each data read.
Also, a dummy read is required before the first data read.
To write data to the GDDRAM, select LOW for the R/W# (WR#) pin and HIGH for the D/C# pin for both
6800-series parallel mode and 8080-series parallel mode. The serial interface mode is always in write mode.
The GDDRAM column address pointer will be increased automatically by one after each data write.


                                Table 8-2 : Address increment table (Automatic)
                     D/C#      R/W# (WR#)       Comment                 Address Increment
                     0         0                Write Command           No
                     0         1                Read Status             No
                     1         0                Write Data              Yes
                     1         1                Read Data               Yes




SSD1362          Rev 1.0   P 39/62   Feb 2015                                                             Solomon Systech

**Extracted table(s) on this page:**

| D/C# | R/W# (WR#) | Comment | Address Increment |
| --- | --- | --- | --- |
| 0 | 0 | Write Command | No |
| 0 | 1 | Read Status | No |
| 1 | 0 | Write Data | Yes |
| 1 | 1 | Read Data | Yes |


<!-- page 40 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9     COMMAND DESCRIPTIONS

9.1     Fundamental Command Description

9.1.1 Set Column Address (15h)
This triple byte command specifies column start address and end address of the display data RAM. This
command also sets the column address pointer to column start address. This pointer is used to define the
current read/write column address in graphic display data RAM. If horizontal address increment mode is
enabled by command A0h, after finishing read/write one column data, it is incremented automatically to the
next column address. Whenever the column address pointer finishes accessing the end column address, it is
reset back to start column address and the row address is incremented to the next row.


9.1.2 Set Row Address (75h)
This triple byte command specifies row start address and end address of the display data RAM. This
command also sets the row address pointer to row start address. This pointer is used to define the current
read/write row address in graphic display data RAM. If vertical address increment mode is enabled by
command A0h, after finishing read/write one row data, it is incremented automatically to the next row address.
Whenever the row address pointer finishes accessing the end row address, it is reset back to start row address.

The diagram below shows the way of column and row address pointer movement through the example:
column start address is set to 2 and column end address is set to 125, row start address is set to 1 and row end
address is set to 62; horizontal address increment mode is enabled by command A0h. In this case, the graphic
display data RAM column accessible range is from column 2 to column 125 and from row 1 to row 62 only.
In addition, the column address pointer is set to 2 and row address pointer is set to 1. After finishing
read/write one pixel of data, the column address is increased automatically by 1 to access the next RAM
location for next read/write operation (solid line in Figure 9-1). Whenever the column address pointer finishes
accessing the end column 125, it is reset back to column 2 and row address is automatically increased by 1
(solid line in Figure 9-1). While the end row 62 and end column 125 RAM location is accessed, the row
address is reset back to 1 and the column address is reset back to 2 (dotted line in Figure 9-1).

                                   Figure 9-1: Example of Column and Row Address Pointer Movement
                        0                  1                 2              …..       …….           125               126                 127          Column address
                                                                                                                                                       SEG outputs
                                                                                               SEG250


                                                                                                          SEG251

                                                                                                                   SEG252

                                                                                                                            SEG253

                                                                                                                                     SEG254

                                                                                                                                              SEG255
                 SEG0


                            SEG1


                                    SEG2


                                               SEG3


                                                      SEG4


                                                                 SEG5

                                                                           :

                                                                                :

                                                                                      :

                                                                                          :




       Row 0                                                                      :
       Row 1
       Row 2
         :
         :                                                                        :
         :
       Row 61
       Row 62
       Row 63                                                                     :




    Solomon Systech                                                                                            Feb 2015 P 40/62                        Rev 1.0   SSD1362

<!-- page 41 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.3 Set Contrast Current (81h)
This double byte command is used to set Contrast Setting of the display with a valid range from 01h to FFh.
The segment output current ISEG increases linearly with the contrast step, which results in brighter display.


9.1.4 Set Re-map (A0h)
This double byte command has multiple configurations and each bit setting is described as follows:


    •   Column Address Remapping (A[0])
        This bit is made for increase the flexibility layout of segment signals in OLED module with segment
        arranged from left to right (when A[0] is set to 0) or from right to left (when A[0] is set to 1).


    •   Nibble Remapping (A[1])
        When A[1] is set to 1, the two nibbles of the data bus for RAM access are re-mapped, such that
        (D7, D6, D5, D4, D3, D2, D1, D0) acts like (D3, D2, D1, D0, D7, D6, D5, D4).
        If this feature works together with Column Address Re-map, it would produce an effect of flipping
        the outputs from SEG0~255 to SEG255~SEG0.


    •   Address increment mode (A[2])
        When A[2] is set to 0, the driver is set as horizontal address increment mode. After the display RAM
        is read / written, the column address pointer is increased automatically by 1. If the column address
        pointer reaches column end address, the column address pointer is reset to column start address and
        row address pointer is increased by 1. The sequence of movement of the row and column address
        point for horizontal address increment mode is shown in Figure 9-2.

                    Figure 9-2: Address Pointer Movement of Horizontal Address Increment Mode
                              0         1            …..         126          127            Column address
              Row 0
              Row 1
                :             :          :            :           :             :
              Row 62
              Row 63

        When A[2] is set to 1, the driver is set to vertical address increment mode. After the display RAM is
        read / written, the row address pointer is increased automatically by 1. If the row address pointer
        reaches the row end address, the row address pointer is reset to row start address and column address
        pointer is increased by 1. The sequence of movement of the row and column address point for vertical
        address increment mode is shown in Figure 9-3.

                       Figure 9-3: Address Pointer Movement of Vertical Address Increment Mode
                                  0          1            …..         126           127     Column address
                 Row 0                                    …..
                 Row 1                                    …..
                   :                                       :
                 Row 62                                   …..
                 Row 63                                   …..




SSD1362          Rev 1.0    P 41/62   Feb 2015                                                                 Solomon Systech

<!-- page 42 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




 •    COM Remapping (A[4])
      This bit defines the scanning direction of the common for flexible layout of common signals in OLED
      module either from up to down (when A[4] is set to 0) or from bottom to up (when A[4] is set to 1).


 •    Splitting of Odd / Even SEG Signals (A[6])
      This bit is made to match the SEG layout connection on the panel.

      When A[6] is set to 0, no splitting odd / even of the SEG signal is performed.
      When A[6] is set to 1, splitting odd / even of the SEG signal is performed.


 •    SEG Left / Right Remapping (A[7])
      This bit is made to enable left SEG and right SEG remapping.

      When A[7] is set to 1, the remapping of left SEG and right SEG is enabled. Examples for the
      different combination use of SEG remap are shown as below.


                                                   Table 9-1 : SEG Pins Hardware Configuration


     Case no.      Oddeven (1) / Sequential (0)                     SEG Remap           Nibble Remap                Left / Right Swap     Remark
                             A[6]                                      A[0]                 A[1]                           A[7]
        1                       0                                       0                     0                              0
        2                       0                                       0                     0                              1
        3                       0                                       1                     1                              0
        4                       0                                       1                     1                              1
        5                       1                                       0                     0                              0            Default
        6                       1                                       0                     0                              1
        7                       1                                       1                     1                              0
        8                       1                                       1                     1                              1



                          COL255                                                                                    COL255
                          COL254                                                                                    COL254
                             .                                                                                         .

                             .                                                                                         .

                             .                                                                                      COL128

                          COL128                                                                    COL127

                                         CO127                                                      COL126
                                           .                                                              .
                                           ..                                                             .
                                         COL1                                                             .
                                         COL0                                                        COL0




                   255 …
                       …128 63…0           0…127
                                           0…
                                            …                                                   255 …
                                                                                                    …128 63…0 0…
                                                                                                              0…127
                                                                                                               …
                                                                                                                      SEG
                                                                                                              COM
                                   COM




                                                                                                    SEG




                                                                                                       M
                    SEG




                                                 SEG




                    G    M     G                                                                  G         G
                    E    O     E                                                                  E    O    E
                         C
                    S SSD1362Z S                                                                       C
                                                                                                  S SSD1362ZS

                (1) Sequential SEG                                                   (2) Sequential SEG & left / right swap




Solomon Systech                                                                           Feb 2015 P 42/62                   Rev 1.0   SSD1362

**Extracted table(s) on this page:**

| Case no. | Oddeven (1) / Sequential (0) A[6] | SEG Remap A[0] | Nibble Remap A[1] | Left / Right Swap A[7] | Remark |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 |  |
| 2 | 0 | 0 | 0 | 1 |  |
| 3 | 0 | 1 | 1 | 0 |  |
| 4 | 0 | 1 | 1 | 1 |  |
| 5 | 1 | 0 | 0 | 0 | Default |
| 6 | 1 | 0 | 0 | 1 |  |
| 7 | 1 | 1 | 1 | 0 |  |
| 8 | 1 | 1 | 1 | 1 |  |


<!-- page 43 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                                                       COL0                                                                 I         ~ COL0
                                                                                                                            , ~
                                                                                                                            I
                                                                                                                                                        COL1




                                                                                                                           ·~
                                                       COL1

                                                         .

                                                         .
                                                                                                                            : ~
                                                                                                                            I         ~
                                                                                                                                                            .
                                                                                                                                                          .
                                                         .                                                                                              COL127
                                                   COL127                                                                           COL128 ~
                                    COL128                                                                                          COL129 ~
                                      .                                                                                                     .   ~
                                      .
                                                                                                                                            .   ~
                                   COL254
                                                                                                                                            .   ~
                                   COL255
                                                                                                                                    COL255



                         255 …
                             …128 63…0                       0…
                                                              … 127                                                        255 … 128 63…0                       0…127
                                                                                                                                                                0…
                                                                                                                                                                 …
                                                             SEG
                                 M
                                    SEG

                                               COM


                            G          G                                                                                             M




                                                                                                                                                 COM

                                                                                                                                                            SEG
                                                                                                                                      SEG
                                 O                                                                                              G          G
                            E          E                                                                                        E    O     E
                                 C
                            S SSD1362Z S                                                                                             C
                                                                                                                                S SSD1362Z S


   (3) Sequential SEG & SEG remap (with nibble remap)                                               (4) Sequential SEG & SEG remap (with nibble
                                                                                                    remap) & left / right swap
                                    COL255
                                                                                                                                                        COL255
                                       .               COL254                                                                       COL254
                                                                                                                                                                .
                                       .                          .                                                                        .            COL253
                                       .                          .                                                                        .                    .
                                       .                          .                                                                        .                    .
                                       .                          .                                                                        .                    .
                                       .                          .                                                                        .                    .
                                    COL3                          .                                                                        .                    .
                                                             COL2                                                                     COL2
                                    COL1                                                                                                                  COL1
                                                             COL0                                                                     COL0




                            255…
                            127 …64   M 00…
                                 128 38…0
                                     63…0 …127
                                            63                                                                             127 …64 63…0
                                                                                                                           255…128  M 00…
                                                                                                                                   38…0 … 127
                                                                                                                                          63
                               G                                      G                                                         G                                   G
                                                                                                                                                 COM
                                                                                                                                SEG
                                SEG


                                                 COM




                                                                                                                                                                    SEG
                                                                       SEG




                               E               O                      E                                                         E               O                   E
                               S               C                      S                                                         S               C                   S
                                    SSD1362Z                                                                                          SSD1362Z
                         (5) Odd / even SEG                                                                  (6) Odd / even SEG & left / right swap
                            COL0                                                                                                                COL0
                               .                                                                                           COL1
                                                       COL1
                            COL2                         .                                                                  .                   COL2
                               .                                                                                            .                       .
                                                       COL3
                               ..                            ..                                                             .                       .
                               .                             .                                                              .                       .
                               .                             .                                                              .                       .
                               .                             .                                                              .                       .
                               .                             .                                                          COL253

                            COL254                           .                                                                                  COL254

                                                     COL255                                                             COL255




                                                                                                                  127
                                                                                                                  255 … 128
                                                                                                                        64 63…0
                                                                                                                             M
                                                                                                                            38…0                  00 … 127
                                                                                                                                                       63
                      127
                      255 …128
                        G       M
                          … 64 63…0
                               38…0                     00 …127
                                                           …6
                                                            63
                                                                 G                                                  G                                   G
                                                                                                                     SEG




                                                                                                                                                         SEG
                                                                                                                                          COM




                                                                                                                    E               O                   E
                                           COM
                         SEG




                                                                      SEG




                        E                  O                     E                                                                  C                   S
                        S                  C                     S                                                  S
                               SSD1362Z                                                                                    SSD1362Z


                                                                                                         (8) Odd / even SEG & SEG remap (with nibble
   (7) Odd / even SEG & SEG remap (with nibble remap)
                                                                                                                   remap) & left / right swap

Note:
        (1)
              The above eight figures are all with bump pads being faced up.




SSD1362                Rev 1.0              P 43/62                          Feb 2015                                                                                     Solomon Systech

**Extracted table(s) on this page:**

| COL0 COL1 ... ... ... COL127 COL128 ... ... COL254 COL255 2 55 ……1 28 6 3…0 00…… 1 27 … … GG MM GG SEG COM SEG EE OO EE SS CC SS SSD1362Z (3)Sequential SEG & SEG remap (with nibble remap) | COL0 ·,I ~~~ COL1 I : ~ ... ... I ~ COL127 COL128 ~ COL129 ~ ... ~ ... ~ ... ~ COL255 2 55 …… 1 28 6 3…0 00……1 27 … … GG M GG COM SEG SEG EE OO EE SS CC SS SSD1362Z (4)Sequential SEG & SEG remap (with nibble remap) & left / right swap |
| --- | --- |
| COL255 ... COL254 ... ... ... ... ... ... ... ... ... ... COL3 ... COL2 COL1 COL0 12GG7 ……6644 33MM88……00 00……GG6 3 255… 12863…0 0… 127 E OO EE COM SEG SEG SS CC SS SSD1362Z (5)Odd / even SEG | COL255 COL254 ... ... COL253 ... ... ... ... ... ... ... ... ... ... COL2 COL1 COL0 12GG7 …… 6644 33MM88…… 00 00……GG 6 3 255…128 63…0 0… 127 EE OO EE COM SEG SEG SS CC SS SSD1362Z (6)Odd / even SEG & left / right swap |
| COL0 ... COL 1 COL2 ... ... COL3 ...... ...... ... ... ... ... ... ... ... ... COL254 ... COL255 127GG …… 6644 33MM88…… 00 00 ……GG 66 3 255 …1 28 63…0 0 …1 27 EE OO EE SEG COM SEG SS CC SS SSD1362Z (7)Odd / even SEG & SEG remap (with nibble remap) | COL0 COL1 ... COL2 ... ... ... ... ... ... ... ... ... ... COL253 COL254 COL255 127GG …… 6644 33MM88…… 00 00 ……GG 66 33 255 … 128 63…0 0 … 127 E OO EE COM SEG SEG S CC SS SSD1362Z (8)Odd / even SEG & SEG remap (with nibble remap) & left / right swap |

| 2 55 ……… | 1 2 |
| --- | --- |
| GG M GG SEG COM SEG EE OO EE SS CC SS SSD1362Z |  |


<!-- page 44 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.5   Set Display Start Line (A1h)

This double byte command is to set Display Start Line register for determining the starting address of display
RAM to be displayed by selecting a value from 0 to 63. Figure 9-4 shows an example using this command
when MUX ratio= 64 and MUX ratio= 44 and Display Start Line = 20. In there, “ROW” means the graphic
display data RAM row.

                          Figure 9-4: Example of Set Display Start Line with no Remapping
         MUX ratio (A8h) = 64     MUX ratio (A8h) = 64     MUX ratio (A8h) = 44     MUX ratio (A8h) = 44
 COM Pin Display Start Line (A1h) Display Start Line (A1h) Display Start Line (A1h) Display Start Line (A1h)
         =0                       =20                      =0                       =20
 COM0 ROW0                        ROW20                    ROW0                     ROW20
 COM1 ROW1                        ROW21                    ROW1                     ROW21
 COM2 ROW2                        ROW22                    ROW2                     ROW22
 COM3 ROW3                        ROW23                    ROW3                     :
 :       :                        :                        :                        :
 :       :                        :                        :                        :
 COM21 ROW21                      ROW41                    ROW21                    ROW41
 COM22 ROW22                      ROW42                    ROW22                    ROW42
 COM23 ROW23                      ROW43                    ROW23                    ROW43
 COM24 ROW24                      ROW44                    ROW24                    ROW43
 COM25 ROW25                      ROW45                    ROW25                    ROW44
 :       :                        :                        :                        ROW45
 :       :                        :                        :                        :
 COM41 ROW41                      ROW61                    ROW41                    ROW61
 COM42 ROW42                      ROW62                    ROW42                    ROW62
 COM43 ROW43                      ROW63                    ROW43                    ROW63
 COM44 ROW44                      ROW0                     -                        -
 COM45 ROW45                      ROW1                     -                        -
 :       :                        :                        :                        :
 :       :                        :                        :                        :
 COM60 ROW60                      ROW16                    -                        -
 COM61 ROW61                      ROW17                    -                        -
 COM62 ROW62                      ROW18                    -                        -
 COM63 ROW63                      ROW19                    -                        -

 Display
 Example

              ,
             SOLOMON
                                        ~
                                       SOLOMON
                                        SVSTECH                              .  -   -
                                                                                    '
                                                                                        ~

                                                                                        &




              SVSTECH                    J   ;,a:;




  Solomon Systech                                                          Feb 2015 P 44/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

|  | MUX ratio (A8h) = 64 | MUX ratio (A8h) = 64 | MUX ratio (A8h) = 44 | MUX ratio (A8h) = 44 |
| --- | --- | --- | --- | --- |
| COM Pin | Display Start Line (A1h) = 0 | Display Start Line (A1h) =20 | Display Start Line (A1h) = 0 | Display Start Line (A1h) =20 |
| COM0 | ROW0 | ROW20 | ROW0 | ROW20 |
| COM1 | ROW1 | ROW21 | ROW1 | ROW21 |
| COM2 | ROW2 | ROW22 | ROW2 | ROW22 |
| COM3 | ROW3 | ROW23 | ROW3 | : |
| : | : | : | : | : |
| : | : | : | : | : |
| COM21 | ROW21 | ROW41 | ROW21 | ROW41 |
| COM22 | ROW22 | ROW42 | ROW22 | ROW42 |
| COM23 | ROW23 | ROW43 | ROW23 | ROW43 |
| COM24 | ROW24 | ROW44 | ROW24 | ROW43 |
| COM25 | ROW25 | ROW45 | ROW25 | ROW44 |
| : | : | : | : | ROW45 |
| : | : | : | : | : |
| COM41 | ROW41 | ROW61 | ROW41 | ROW61 |
| COM42 | ROW42 | ROW62 | ROW42 | ROW62 |
| COM43 | ROW43 | ROW63 | ROW43 | ROW63 |
| COM44 | ROW44 | ROW0 | - | - |
| COM45 | ROW45 | ROW1 | - | - |
| : | : | : | : | : |
| : | : | : | : | : |
| COM60 | ROW60 | ROW16 | - | - |
| COM61 | ROW61 | ROW17 | - | - |
| COM62 | ROW62 | ROW18 | - | - |
| COM63 | ROW63 | ROW19 | - | - |
| Display Example | , SOLOMON SVSTECH | ~ SOLOMON SVSTECH ;,a:; J | . - - ' &~ |  |


<!-- page 45 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.6   Set Display Offset (A2h)

This double byte command specifies the mapping of display start line (it is assumed that COM0 is the display
start line, display start line register equals to 0) to one of COM0~COM63.

Figure 9-5 shows an example using this command when MUX ratio= 64 and MUX ratio= 44 and Display
Offset = 20. In there, “Row” means the graphic display data RAM row.

                            Figure 9-5: Example of Set Display Offset with no Remapping
         MUX ratio (A8h) = 64        MUX ratio (A8h) = 64       MUX ratio (A8h) = 44          MUX ratio (A8h) = 44
 COM Pin Display Offset (A2h)=0      Display Offset (A2h)=20    Display Offset (A2h)=0        Display Offset (A2h)=20
 COM0 ROW0                           ROW20                      ROW0                          ROW20
 COM1 ROW1                           ROW21                      ROW1                          ROW21
 COM2 ROW2                           ROW22                      ROW2                          ROW22
 COM3 ROW3                           ROW23                      ROW3                          ROW23
 :       :                           :                          :                             :
 :       :                           :                          :                             :
 COM21 ROW21                         ROW41                      ROW21                         ROW41
 COM22 ROW22                         ROW42                      ROW22                         ROW42
 COM23 ROW23                         ROW43                      ROW23                         ROW43
 COM24 ROW24                         ROW44                      ROW24                         -
 COM25 ROW25                         ROW45                      ROW25                         -
 :       :                           :                          :                             -
 :       :                           :                          :                             -
 COM41 ROW41                         ROW61                      ROW41                         -
 COM42 ROW42                         ROW62                      ROW42                         -
 COM43 ROW43                         ROW63                      ROW43                         -
 COM44 ROW44                         ROW0                       -                             ROW0
 COM45 ROW45                         ROW1                       -                             ROW1
 :       :                           :                          :                             :
 :       :                           :                          :                             :
 COM60 ROW60                         ROW16                      -                             ROW16
 COM61 ROW61                         ROW17                      -                             ROW17
 COM62 ROW62                         ROW18                      -                             ROW18
 COM63 ROW63                         ROW19                      -                             ROW19

 Display
 Example

              ,
             SOLOMON
                                         ~
                                        SOLOMON
                                         SVSTECH
              SVSTECH                     J;,;




SSD1362          Rev 1.0   P 45/62   Feb 2015                                                              Solomon Systech

**Extracted table(s) on this page:**

|  | MUX ratio (A8h) = 64 | MUX ratio (A8h) = 64 | MUX ratio (A8h) = 44 | MUX ratio (A8h) = 44 |
| --- | --- | --- | --- | --- |
| COM Pin | Display Offset (A2h)=0 | Display Offset (A2h)=20 | Display Offset (A2h)=0 | Display Offset (A2h)=20 |
| COM0 | ROW0 | ROW20 | ROW0 | ROW20 |
| COM1 | ROW1 | ROW21 | ROW1 | ROW21 |
| COM2 | ROW2 | ROW22 | ROW2 | ROW22 |
| COM3 | ROW3 | ROW23 | ROW3 | ROW23 |
| : | : | : | : | : |
| : | : | : | : | : |
| COM21 | ROW21 | ROW41 | ROW21 | ROW41 |
| COM22 | ROW22 | ROW42 | ROW22 | ROW42 |
| COM23 | ROW23 | ROW43 | ROW23 | ROW43 |
| COM24 | ROW24 | ROW44 | ROW24 | - |
| COM25 | ROW25 | ROW45 | ROW25 | - |
| : | : | : | : | - |
| : | : | : | : | - |
| COM41 | ROW41 | ROW61 | ROW41 | - |
| COM42 | ROW42 | ROW62 | ROW42 | - |
| COM43 | ROW43 | ROW63 | ROW43 | - |
| COM44 | ROW44 | ROW0 | - | ROW0 |
| COM45 | ROW45 | ROW1 | - | ROW1 |
| : | : | : | : | : |
| : | : | : | : | : |
| COM60 | ROW60 | ROW16 | - | ROW16 |
| COM61 | ROW61 | ROW17 | - | ROW17 |
| COM62 | ROW62 | ROW18 | - | ROW18 |
| COM63 | ROW63 | ROW19 | - | ROW19 |
| Display Example | , SOLOMON SVSTECH | ~ SOLOMON SVSTECH J;,; |  |  |


<!-- page 46 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.7 Set Vertical Scroll area (A3h)
This triple byte command specifies the vertical scroll area. The number of rows for top fixed area plus scroll
area should be smaller than or equating to the MUX ratio.

9.1.8 Set Display Mode (A4h ~ A7h)
These are single byte commands (A4h ~ A7h) and are used to set display status to Normal Display, Entire
Display ON, Entire Display OFF or Inverse Display, respectively.
    • Normal Display (A4h)
        Reset the “Entire Display ON, Entire Display OFF or Inverse Display” effects and turn the data to
        ON at the corresponding gray level. Figure 9-6 shows an example of Normal Display.



                                         ,. ,.
                                          Figure 9-6: Example of Normal Display




                                        SOLOMON
                                         SVSTECH
                                                                     SOLOMON
                                                                      SVSTECH
                                           Memory                       Display

      •    Set Entire Display ON (A5h)
           Force the entire display to be at gray scale level GS15, regardless of the contents of the display data
           RAM, as shown on Figure 9-7.
                                        Figure 9-7: Example of Entire Display ON




                                        SOLOMON
                                         SVSTECH
                                           Memory                       Display

  •       Set Entire Display OFF (A6h)
          Force the entire display to be at gray scale level GS0, regardless of the contents of the display data
          RAM, as shown on Figure 9-8.
                                        Figure 9-8 : Example of Entire Display OFF




                                         ~
                                        SOLOMON
                                         SVSTECH
                                           Memory                       Display

      •    Inverse Display (A7h)
           The gray scale level of display data are swapped such that “GS0” <-> “GS15”, “GS1” <-> “GS14”,
           etc. Figure 9-9 shows an example of inverse display.
                                          Figure 9-9: Example of Inverse Display




                                         ~
                                        SOLOMON
                                         SVSTECH
                                           Memory                       Display


  Solomon Systech                                                             Feb 2015 P 46/62      Rev 1.0    SSD1362

<!-- page 47 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.9 Set Multiplex Ratio (A8h)
This double byte command sets multiplex ratio (MUX ratio) from 4MUX to 64MUX. In RESET, multiplex
ratio is 64MUX. Please refer to Figure 9-4 and Figure 9-5 for the example of setting different MUX ratio.


9.1.10 Function Selection A (ABh)
This double byte command is used to enable or disable the VDD regulator.
Internal VDD regulator is enabled when the bit A[0] is set to 1b, while internal VDD regulator is disabled when
A[0] is set to 0b.


9.1.11 External or Internal IREF Selection (ADh)
This double byte command is used to select external or internal IREF.
External IREF is selected when the bit A[4] is set to 0b, while internal IREF is selected when A[4] is set to 1b.


9.1.12 Set Display ON/OFF (AEh / AFh)
These single byte commands are used to turn the OLED panel display ON or OFF.
When the display is OFF (command AEh), the segment pins are in VSS state and common pins are in high
impedance state.

                                 Figure 9-10: Display ON Sequence (when initial start)


                                           Power supply setting (1)



                                           Send command AFh to
                                           turn the panel display ON (2)



                    ..,~                 Display _
                                        I_       on and start
                                                          _   to write_
                                                                      RAM I

                                         Figure 9-11: Display OFF Sequence


                                           Display on (2)



                                          Send command AEh to
                                          turn the panel display OFF (2)



                                           Display off at Sleep mode (3)



                                           Set command ABh to 00h to disable
                                           the internal VDD regulator (3) (4)



SSD1362           Rev 1.0   P 47/62   Feb 2015                                                              Solomon Systech

<!-- page 48 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Note:
(1)
    Please follow the power ON sequence as suggested
(2)
    Internal VDD regulator is ON as default
(3)
    The RAM content is kept during display off at both sleep mode and the case that internal VDD regulator is disabled.
(4)
    It is recommended to disable internal VDD regulator during Sleep mode for power save.
               Figure 9-12: Display ON Sequence (During Sleep mode and internal VDD regulator is disabled)


                                             Display off at Sleep mode
                                             and internal VDD regulator
                                             is disabled (1)


                                            Set command ABh to 01h to enable
                                            the internal VDD regulator



                                             Send command AFh to
                                             turn the panel display ON



                                             Display on and start to write RAM


Note:
(1)
    The RAM content is kept during display off at sleep mode and internal VDD regulator is disabled.



9.1.13 Set Phase Length (B1h)
This double byte command sets the length of phase 1 and 2 of segment waveform of the driver.
    • Phase 1 (A[3:0]): Set the period from 2 to 30 in the unit of DCLKs. A larger capacitance of the
       OLED pixel may require longer period to discharge the previous data charge completely.

    •    Phase 2 (A[7:4]): Set the period from 2 to 30 in the unit of DCLKs. A longer period is needed to
         charge up a larger capacitance of the OLED pixel to the target voltage VP.


9.1.14 Set Front Clock Divider / Oscillator Frequency (B3h)
This double byte command consists of two functions:
    • Front Clock Divide Ratio (A[3:0])
       Set the divide ratio to generate DCLK (Display Clock) from CLK. The divide ratio is from 1 to 256,
       with reset value = 0001b.

    •    Oscillator Frequency (A[7:4])
         Program the oscillator frequency Fosc which is the source of CLK if CLS pin is pulled HIGH. The 4-
         bit value results in 16 different frequency settings being available. The default setting is 1010b.


9.1.15 Set GPIO (B5h)
This double byte command is used to set the states of GPIO0 and GPIO1 pins. Refer to Table 8-1 for details.




  Solomon Systech                                                             Feb 2015 P 48/62      Rev 1.0    SSD1362

<!-- page 49 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.16 Set Second Pre-charge period (B6h)
This double byte command is used to set the phase 3 second pre-charge period. The period of phase 3 can be
programmed by command B6h and it is ranged from 1 to 15 DCLK's.


9.1.17 Set Gray Scale Table (B8h)
This command is used to set each individual gray scale level for the display. Except gray scale levels GS0
that has no pre-charge and current drive, each gray scale level is programmed in the length of current drive
stage pulse width with unit of DCLK. The longer the length of the pulse width, the brighter the OLED pixel
when it’s turned ON. Following the command B8h, the user has to set the gray scale setting for GS1, GS2…
GS14, GS15 one by one in sequence. Note that GS15 level must be set larger than 140 (ie. 8Ch).

The setting of gray scale table entry can perform gamma correction on OLED panel display. Since the
perception of the brightness scale shall match the image data value in display data RAM, appropriate gray
scale table setting like the example shown below (Figure 9-13) can compensate this effect.

                    Figure 9-13 : Example of Gamma correction by Gamma Look Up table setting

                                     Brightness                              Brightness
 Gamma
 Setting   Gamma Look Up
           table setting
                                                          Panel
                                                          response
                                                                                                      Result in linear
                                                                                                      response

                   Gray Scale Table                         Gamma Setting                              Gray Scale Table



9.1.18 Select Default Linear Gray Scale Table (B9h)
This single byte command reloads the preset linear Gray Scale table as GS0 = Gamma Setting 0, GS1 =
Gamma Setting 12, GS2 = Gamma Setting24., GS14 = Gamma Setting 168, GS15 = Gamma Setting 180.


9.1.19 Set Pre-charge Voltage (BCh)
This double byte command sets the first pre-charge voltage (phase 2) level of segment pins. The level of pre-
charge voltage is programmed with reference to VCC. Refer to Table 8-1 for details.


9.1.20 Pre-charge Voltage Capacitor Selection (BDh)
This double byte command is used to select the pre-charge voltage capacitor.
VP should be connected with an external capacitor when the bit A[0] is set to 1b, while there is no external
capacitor for VP when A[0] is set to 0b.


9.1.21 Set VCOMH Voltage (BEh)
This double byte command sets the high voltage level of common pins, VCOMH. The level of VCOMH is
programmed with reference to VCC. Refer to Table 8-1 for details.




SSD1362          Rev 1.0   P 49/62    Feb 2015                                                             Solomon Systech

<!-- page 50 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




9.1.22 Set Command Lock (FDh)
This double byte command is used to lock the OLED driver IC from accepting any command except itself.
After entering FDh 16h (A[2]=1b), the OLED driver IC will not respond to any newly-entered command
(except FDh 12h A[2]=0b) and there will be no memory access. This is call “Lock” state. That means the
OLED driver IC ignore all the commands (except FDh 12h A[2]=0b) during the “Lock” state.

Entering FDh 12h (A[2]=0b) can unlock the OLED driver IC. That means the driver IC resume from the
“Lock” state. And the driver IC will then respond to the command and memory access.


9.1.23 Set Fade In / Out and Blinking (23h)
This command allows to set the fade mode and adjust the time interval for each fade step. Below figures show
the example of Fade Out mode and blinking mode.

                                    Figure 9-14 : Example of Fade Out mode




                                    Figure 9-15 : Example of Blinking mode




  Solomon Systech                                                       Feb 2015 P 50/62      Rev 1.0    SSD1362

<!-- page 51 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




10 MAXIMUM RATINGS
                                                      Table 10-1 : Maximum Ratings
(Voltage Reference to VSS)
        Symbol                     Parameter                                                 Value                                 Unit
          VDD                                                                            -0.5 to 2.75                               V
          VCC                                                                            -0.5 to 21.0                               V
                                 Supply Voltage
         VDDIO                                                                            -0.5 to 5.5                               V
          VCI                                                                             -0.3 to 5.5                               V
          VSEG                 SEG output voltage                                          0 to VCC                                 V
          VCOM                 COM output voltage                                        0 to 0.9*VCC                               V
          Vin                     Input voltage                                      Vss-0.3 to VDDIO+0.3                           V
           TA                Operating Temperature                                        -40 to +85                                ºC
          Tstg             Storage Temperature Range                                     -65 to +150                                ºC

*Maximum Ratings are those values beyond which damage to the device may occur. Functional operation should be restricted to the limits in the
Electrical Characteristics tables or Pin Description.

*This device may be light sensitive. Caution should be taken to avoid exposure of this device to any light source during normal operation. This device
is not radiation protected.




SSD1362                 Rev 1.0      P 51/62     Feb 2015                                                                         Solomon Systech

**Extracted table(s) on this page:**

| Symbol | Parameter | Value | Unit |
| --- | --- | --- | --- |
| V DD | Supply Voltage | -0.5 to 2.75 | V |
| V CC |  | -0.5 to 21.0 | V |
| V DDIO |  | -0.5 to 5.5 | V |
| V CI |  | -0.3 to 5.5 | V |
| V SEG | SEG output voltage | 0 to V CC | V |
| V COM | COM output voltage | 0 to 0.9*V CC | V |
| V in | Input voltage | Vss-0.3 to V +0.3 DDIO | V |
| T A | Operating Temperature | -40 to +85 | ºC |
| T stg | Storage Temperature Range | -65 to +150 | ºC |


<!-- page 52 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




11 DC CHARACTERISTICS
Condition (Unless otherwise specified):
       Voltage referenced to VSS,
       VDDIO = 1.65V to 3.5V
       TA = 25°C
                                             Table 11-1 : DC Characteristics
Symbol       Parameter                   Test Condition                                  Min         Typ         Max       Unit
VCC          Operating Voltage           -                                               10           -          20        V
VCI          Low voltage power supply    -                                               1.65          -          3.5      V
VDDIO        Power supply for I/O pins   -                                               1.65          -          VCI      V
VDD          Logic Supply Voltage        -                                               1.65          -          2.6      V
                                                                                        0.9 x
VOH          High Logic Output Level     IOUT = 100uA, 3.3MHz                                          -           -       V
                                                                                        VDDIO
                                                                                                                 0.1 x
VOL          Low Logic Output Level      IOUT = 100uA, 3.3MHz                              -           -                   V
                                                                                                                 VDDIO
                                                                                        0.8 x
VIH          High Logic Input Level      -                                                             -           -       V
                                                                                        VDDIO
                                                                                                                 0.2 x
VIL          Low Logic Input Level       -                                                 -           -                   V
                                                                                                                 VDDIO

                                         VCI = VDDIO = 2.8V, VCC = OFF
ISLP_VDD     VDD Sleep mode Current      VDD (external) = 2.5V, Display OFF,               -           -          10       uA
                                         No panel attached

                                         VCI = VDDIO = 2.8V, VCC = OFF
ISLP_VDDIO   VDDIO Sleep mode Current    VDD (external) = 2.5V, Display OFF,               -           -          10       uA
                                         No panel attached

                                         VCI = VDDIO = 2.8V, VCC =OFF
                                         VDD (external) = 2.5V, Display OFF,               -           -          10       uA
                                         No panel attached

                                                                 Enable Internal
                                                                 VDD during                -           -          60       uA
ISLP VCI     VCI Sleep mode Current      VCI = VDDIO =           Sleep mode
                                         2.8V,
                                         VCC =OFF                Disable Internal
                                         Display OFF,            VDD during
                                         No panel attached       Sleep mode                -           -          10       uA
                                                                 (Deep Sleep
                                                                 mode)

                                         VCC = 10~20V,
ISLP_VCC     VCC Sleep mode Current      VCI = VDDIO = 2.8V, Internal VDD                  -           -          10       uA
                                         Display OFF, No panel attached

                                             VCI = VDDIO = 2.8V, Internal VDD,
                                             VCC =12V, Contrast = FFh,
ICC          VCC Supply Current                                                            -         1500        2000      uA
                                             IREF =18.75uA, No loading,
                                             Display ON, All ON




  Solomon Systech                                                              Feb 2015 P 52/62      Rev 1.0    SSD1362

**Extracted table(s) on this page:**

| Symbol | Parameter | Test Condition |  | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V CC | Operating Voltage | - |  | 10 | - | 20 | V |
| V CI | Low voltage power supply | - |  | 1.65 | - | 3.5 | V |
| V DDIO | Power supply for I/O pins | - |  | 1.65 | - | V CI | V |
| V DD | Logic Supply Voltage | - |  | 1.65 | - | 2.6 | V |
| V OH | High Logic Output Level | I = 100uA, 3.3MHz OUT |  | 0.9 x V DDIO | - | - | V |
| V OL | Low Logic Output Level | I = 100uA, 3.3MHz OUT |  | - | - | 0.1 x V DDIO | V |
| V IH | High Logic Input Level | - |  | 0.8 x V DDIO | - | - | V |
| V IL | Low Logic Input Level | - |  | - | - | 0.2 x V DDIO | V |
| I SLP_VDD | V Sleep mode Current DD | V = V = 2.8V, V = OFF CI DDIO CC V (external) = 2.5V, Display OFF, DD No panel attached |  | - | - | 10 | uA |
| I SLP_VDDIO | V Sleep mode Current DDIO | V = V = 2.8V, V = OFF CI DDIO CC V (external) = 2.5V, Display OFF, DD No panel attached |  | - | - | 10 | uA |
| I SLP VCI | V = V = 2.8V, V =OFF CI DDIO CC V (external) = 2.5V, Display OFF, DD No panel attached Enable Internal V during DD V CI Sleep mode Current V CI = V DDIO = Sleep mode 2.8V, V =OFF CC Disable Internal Display OFF, V during DD No panel attached Sleep mode (Deep Sleep mode) |  |  | - | - | 10 | uA |
|  |  | V = V = CI DDIO 2.8V, V =OFF CC Display OFF, No panel attached | Enable Internal V during DD Sleep mode | - | - | 60 | uA |
|  |  |  | Disable Internal V during DD Sleep mode (Deep Sleep mode) | - | - | 10 | uA |
| I SLP_VCC | V Sleep mode Current CC | V = 10~20V, CC V = V = 2.8V, Internal V CI DDIO DD Display OFF, No panel attached |  | - | - | 10 | uA |
| I CC | V Supply Current CC | V = V = 2.8V, Internal V , CI DDIO DD V =12V, Contrast = FFh, CC I =18.75uA, No loading, REF Display ON, All ON |  | - | 1500 | 2000 | uA |


<!-- page 53 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Symbol     Parameter                       Test Condition                              Min         Typ         Max       Unit

                                           VCI = VDDIO = 2.8V, Internal VDD
           VDDIO Supply Current            VCC = 12V, Contrast = FFh,
IDDIO                                                                                    -          0.5         10       uA
                                           IREF = 18.75uA, No loading,
                                           Display ON, All ON


                                           VCI = VDDIO = 2.8V, Internal VDD
                                           VCC = 12V, Contrast = FFh,
ICI        VCI Supply Current                                                            -          250         350      uA
                                           IREF = 18.75uA, No loading,
                                           Display ON, All ON

                                            VCI = VDDIO = 2.8V,
                                            VDD (external) = 2.5V,
IDD        VDD Supply Current               VCC = 12V, Contrast = FFh,                   -          230         330      uA
                                            IREF = 18.75uA, No loading,
                                            Display ON, All ON
                                           Contrast=FFh                                  -          600          -
           Segment Output Current,
           VCI = VDDIO = 2.8V,             Contrast=AFh                                  -        412.5          -
ISEG       VCC = 12V,                      Contrast=7Fh                                  -          300          -       uA
           IREF (external) = 18.75uA,      Contrast=3Fh                                  -          150          -
           Display ON
                                           Contrast=0Fh                                  -         37.5          -
                                           Contrast=FFh                                  -          280          -
           Segment Output Current,
           VCI = VDDIO = 2.8V,             Contrast=AFh                                  -        192.5          -
ISEG       VCC = 12V, Internal IREF        Contrast=7Fh                                  -          140          -       uA
           (command ADh 9Eh),              Contrast=3Fh                                  -          70           -
           Display ON
                                           Contrast=0Fh                                  -         17.5          -

                                           Dev = (ISEG – IMID)/IMID
           Segment output current          IMID = (IMAX + IMIN)/2
Dev                                                                                     -3           -           3       %
           uniformity                      ISEG[0:255] = Segment current
                                           at contrast setting = FFh

           Adjacent pin output current
                                           Adj Dev = (I[n]-I[n+1]) /
Adj. Dev   uniformity (contrast setting                                                 -2           -           2       %
                                           (I[n]+I[n+1])
           = FFh)




SSD1362           Rev 1.0   P 53/62     Feb 2015                                                             Solomon Systech

**Extracted table(s) on this page:**

| Symbol | Parameter | Test Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| I DDIO | V Supply Current DDIO | V = V = 2.8V, Internal V CI DDIO DD V = 12V, Contrast = FFh, CC I = 18.75uA, No loading, REF Display ON, All ON | - | 0.5 | 10 | uA |
| I CI | V Supply Current CI | V = V = 2.8V, Internal V CI DDIO DD V = 12V, Contrast = FFh, CC I = 18.75uA, No loading, REF Display ON, All ON | - | 250 | 350 | uA |
| I DD | V Supply Current DD | V = V = 2.8V, CI DDIO V (external) = 2.5V, DD V = 12V, Contrast = FFh, CC I = 18.75uA, No loading, REF Display ON, All ON | - | 230 | 330 | uA |
| I SEG | Segment Output Current, V = V = 2.8V, CI DDIO V = 12V, CC I (external) = 18.75uA, REF Display ON | Contrast=FFh | - | 600 | - | uA |
|  |  | Contrast=AFh | - | 412.5 | - |  |
|  |  | Contrast=7Fh | - | 300 | - |  |
|  |  | Contrast=3Fh | - | 150 | - |  |
|  |  | Contrast=0Fh | - | 37.5 | - |  |
| I SEG | Segment Output Current, V = V = 2.8V, CI DDIO V = 12V, Internal I CC REF (command ADh 9Eh), Display ON | Contrast=FFh | - | 280 | - | uA |
|  |  | Contrast=AFh | - | 192.5 | - |  |
|  |  | Contrast=7Fh | - | 140 | - |  |
|  |  | Contrast=3Fh | - | 70 | - |  |
|  |  | Contrast=0Fh | - | 17.5 | - |  |
| Dev | Segment output current uniformity | Dev = (I – I )/I SEG MID MID I = (I + I )/2 MID MAX MIN I [0:255] = Segment current SEG at contrast setting = FFh | -3 | - | 3 | % |
| Adj. Dev | Adjacent pin output current uniformity (contrast setting = FFh) | Adj Dev = (I[n]-I[n+1]) / (I[n]+I[n+1]) | -2 | - | 2 | % |


<!-- page 54 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




12 AC CHARACTERISTICS


12.1 AC Characteristics

Conditions:
       Voltage referenced to VSS
       VDDIO = 1.65V to 3.5V
       TA = 25°C

                                               Table 12-1 : AC Characteristics
Symbol               Parameter                 Test Condition              Min.                Typ.               Max. Unit
             Oscillation Frequency of   VCI = 2.8V, internal VDD
FOSC (1)     Display Timing Generator
                                                                           1260                1400               1540   kHz
                                        256x64 Graphic Display Mode,
             Frame Frequency for 64
FFRM                                    Display ON, Internal Oscillator       -      FOSC * 1 / (D * K * 64)(2)    -     Hz
             MUX Mode
                                        Enabled


Note
(1)
    FOSC stands for the frequency value of the internal oscillator and the value is measured when command B3h A[7:4] is
in default value.
(2)
      D: divide ratio
      K: Phase 1 period + Phase 2 period + X
      X: DCLKs in current drive period.
      Default K is 4 + 16 + 195 = 215




      Solomon Systech                                                             Feb 2015 P 54/62      Rev 1.0   SSD1362

**Extracted table(s) on this page:**

| Symbol | Parameter | Test Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| FOSC (1) | Oscillation Frequency of Display Timing Generator | V = 2.8V, internal V CI DD | 1260 | 1400 | 1540 | kHz |
| FFRM | Frame Frequency for 64 MUX Mode | 256x64 Graphic Display Mode, Display ON, Internal Oscillator Enabled | - | FOSC * 1 / (D * K * 64)(2) | - | Hz |


<!-- page 55 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




  12.2 6800-Series MCU Parallel Interface Timing Characteristics

                          Table 12-2 : 6800-Series MCU Parallel Interface Timing Characteristics


  VCI - VSS = 1.65V to 3.5V (TA = 25°C)
   Symbol         Parameter                                                                  Min           Typ   Max      Unit
   tcycle         Clock Cycle Time                                                           320            -      -       ns
   tAS            Address Setup Time                                                         25             -      -       ns
   tAH            Address Hold Time                                                           0             -      -       ns
   tDSW           Write Data Setup Time                                                      40             -      -       ns
   tDHW           Write Data Hold Time                                                       45             -      -       ns
   tDHR           Read Data Hold Time                                                        20             -      -       ns
   tOH            Output Disable Time                                                          -            -     70       ns
   tACC           Access Time                                                                  -            -    250       ns
                  Chip Select Low Pulse Width (read)                                         160
   PWCSL                                                                                                    -     -        ns
                  Chip Select Low Pulse Width (write)                                         60
                  Chip Select High Pulse Width (read)                                         60
   PWCSH                                                                                                    -     -        ns
                  Chip Select High Pulse Width (write)                                        60
   tR             Rise Time                                                                    -            -    15        ns
   tF             Fall Time                                                                    -            -    15        ns



                                 Figure 12-1 : 6800-series MCU parallel interface characteristics


        D/C#

                                       tAS                                         tAH

R/W#(WR#)#



     E(RD#)
                                                                                   tcycle
                                                                                                   PWCSH
                                                        PWCSL
         CS#                                                       tR

                              tF                                                            tDHW
                                                            tDSW

 D[7:0] (WRITE)
                                                            Valid Data

                                               tACC                                     tDHR
 D[7:0] (READ)
                                                                    Valid Data

                                                                                                     tOH




   SSD1362             Rev 1.0     P 55/62   Feb 2015                                                                 Solomon Systech

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| t cycle | Clock Cycle Time | 320 | - | - | ns |
| t AS | Address Setup Time | 25 | - | - | ns |
| t AH | Address Hold Time | 0 | - | - | ns |
| t DSW | Write Data Setup Time | 40 | - | - | ns |
| t DHW | Write Data Hold Time | 45 | - | - | ns |
| t DHR | Read Data Hold Time | 20 | - | - | ns |
| t OH | Output Disable Time | - | - | 70 | ns |
| t ACC | Access Time | - | - | 250 | ns |
| PW CSL | Chip Select Low Pulse Width (read) Chip Select Low Pulse Width (write) | 160 60 | - | - | ns |
| PW CSH | Chip Select High Pulse Width (read) Chip Select High Pulse Width (write) | 60 60 | - | - | ns |
| t R | Rise Time | - | - | 15 | ns |
| t F | Fall Time | - | - | 15 | ns |


<!-- page 56 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




12.3 8080-Series MCU Parallel Interface Timing Characteristics

                          Table 12-3 : 8080-Series MCU Parallel Interface Timing Characteristics

VCI - VSS = 1.65V to 3.5V (TA = 25°C)
Symbol         Parameter                                                                    Min           Typ              Max          Unit
tcycle         Clock Cycle Time                                                             300            -                 -           ns
tAS            Address Setup Time                                                           30             -                 -           ns
tAH            Address Hold Time                                                             0             -                 -           ns
tDSW           Write Data Setup Time                                                        40             -                 -           ns
tDHW           Write Data Hold Time                                                          40            -                 -           ns
tDHR           Read Data Hold Time                                                           20            -                 -           ns
tOH            Output Disable Time                                                            -            -               70            ns
tACC           Access Time                                                                    -            -               180           ns
tPWLR          Read Low Time                                                                150            -                 -           ns
tPWLW          Write Low Time                                                                60            -                 -           ns
tPWHR          Read High Time                                                                60            -                 -           ns
tPWHW          Write High Time                                                               60            -                 -           ns
tR             Rise Time                                                                      -            -               15            ns
tF             Fall Time                                                                      -            -                15           ns
tCS            Chip select setup time                                                        0             -                 -           ns
tCSH           Chip select hold time to read signal                                          0             -                 -           ns
tCSF           Chip select hold time                                                        20             -                 -           ns



                                 Figure 12-2 : 8080-series MCU parallel interface characteristics

                          Write cycle                                                              Read cycle
CS#                                                                              CS#                                                     tCSH
                    tCS                                           tCSF
                                                                                                      tCS

D/C#                                                                             D/C#
                 tAS                           tAH
                                                                                                    tAS                           tAH
                            tF           tR                                                                                 tR
                                                     tcycle                                                 tF                            tcycle
                                 tPWLW                    tPWHW                                                    tPWLR
R/W#(WR#)                                                                                                                                       tPWHR
                                                                                 E(RD#)
                                    tDSW      tDHW                                                          tACC                 tDHR
D[7:0]
                                                                                D[7:0]

                                                                                                                                        tOH




  Solomon Systech                                                                           Feb 2015 P 56/62               Rev 1.0      SSD1362

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| t cycle | Clock Cycle Time | 300 | - | - | ns |
| t AS | Address Setup Time | 30 | - | - | ns |
| t AH | Address Hold Time | 0 | - | - | ns |
| t DSW | Write Data Setup Time | 40 | - | - | ns |
| t DHW | Write Data Hold Time | 40 | - | - | ns |
| t DHR | Read Data Hold Time | 20 | - | - | ns |
| t OH | Output Disable Time | - | - | 70 | ns |
| t ACC | Access Time | - | - | 180 | ns |
| t PWLR | Read Low Time | 150 | - | - | ns |
| t PWLW | Write Low Time | 60 | - | - | ns |
| t PWHR | Read High Time | 60 | - | - | ns |
| t PWHW | Write High Time | 60 | - | - | ns |
| t R | Rise Time | - | - | 15 | ns |
| t F | Fall Time | - | - | 15 | ns |
| t CS | Chip select setup time | 0 | - | - | ns |
| t CSH | Chip select hold time to read signal | 0 | - | - | ns |
| t CSF | Chip select hold time | 20 | - | - | ns |


<!-- page 57 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




 12.4 Serial Interface Timing Characteristics

                         Table 12-4 : Serial Interface Timing Characteristics (4-wire SPI)

 VCI - VSS = 1.65V to 3.5V (TA = 25°C)
  Symbol        Parameter                                                             Min             Typ          Max      Unit
  tcycle        Clock Cycle Time                                                      100               -           -        ns
  tAS           Address Setup Time                                                    15                -           -        ns
  tAH           Address Hold Time                                                     40                -           -        ns
  tCSS          Chip Select Setup Time                                                20                -           -        ns
  tCSH          Chip Select Hold Time                                                  10               -           -        ns
  tDSW          Write Data Setup Time                                                 15                -           -        ns
  tDHW          Write Data Hold Time                                                   30               -           -        ns
  tCLKL         Clock Low Time                                                         25               -           -        ns
  tCLKH         Clock High Time                                                        20               -           -        ns
  tR            Rise Time                                                               -               -          15        ns
  tF            Fall Time                                                               -              /-          15        ns
                                                                                                      /



                             Figure 12-3 : Serial interface characteristics (4-wire SPI)

       D/C#

                                                              t AS                         t AH

                                          t CSS                                            t CSH
        CS#

                                                                        t cycle
                                                  t CLKL                                                  t CLKH

SCLK
(D0)                tF                                                                tR
                                                      t DSW                                   t DHW

SDIN                                                       Valid Data
(D1)




        CS#



       SCLK
       (D0)

   SDIN(D1)                   D7            D6                D5        D4         D3              D2              D1         D0




 SSD1362           Rev 1.0   P 57/62     Feb 2015                                                                       Solomon Systech

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| t cycle | Clock Cycle Time | 100 | - | - | ns |
| t AS | Address Setup Time | 15 | - | - | ns |
| t AH | Address Hold Time | 40 | - | - | ns |
| t CSS | Chip Select Setup Time | 20 | - | - | ns |
| t CSH | Chip Select Hold Time | 10 | - | - | ns |
| t DSW | Write Data Setup Time | 15 | - | - | ns |
| t DHW | Write Data Hold Time | 30 | - | - | ns |
| t CLKL | Clock Low Time | 25 | - | - | ns |
| t CLKH | Clock High Time | 20 | - | - | ns |
| t R | Rise Time | - | - | 15 | ns |
| t F | Fall Time | - | - / | 15 | ns |


<!-- page 58 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




                                Table 12-5: Serial Interface Timing Characteristics (3-wire SPI)
      VCI - VSS = 1.65V to 3.5V (TA = 25°C)
       Symbol          Parameter                                                                      Min      Typ       Max      Unit
       tcycle          Clock Cycle Time                                                               100       -         -        ns
       tCSS            Chip Select Setup Time                                                         20        -         -        ns
       tCSH            Chip Select Hold Time                                                          45        -         -        ns
       tDSW            Write Data Setup Time                                                          15        -         -        ns
       tDHW            Write Data Hold Time                                                           30        -         -        ns
       tCLKL           Clock Low Time                                                                  25       -         -        ns
       tCLKH           Clock High Time                                                                 35       -         -        ns
       tR              Rise Time                                                                        -       -        15        ns
       tF              Fall Time                                                                        -       -        15        ns



                                    Figure 12-4: Serial interface characteristics (3-wire SPI)

                                        t CSS                                                  t CSH
      CS#

                                                                           t CYCLE
                                                                                                            t CLKH
                                                t CLKL
      SCLK
       (D0)
                  tF                                                                      tR
                                                    t DSW                                         t
                                                                                                      DHW

       SDIN                                              Valid Data
       (D1)


CS#


SCLK
(D0)


SDIN
                  D/C#        D7        D6               D5           D4             D3          D2            D1         D0
(D1)




        Solomon Systech                                                                    Feb 2015 P 58/62          Rev 1.0   SSD1362

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| t cycle | Clock Cycle Time | 100 | - | - | ns |
| t CSS | Chip Select Setup Time | 20 | - | - | ns |
| t CSH | Chip Select Hold Time | 45 | - | - | ns |
| t DSW | Write Data Setup Time | 15 | - | - | ns |
| t DHW | Write Data Hold Time | 30 | - | - | ns |
| t CLKL | Clock Low Time | 25 | - | - | ns |
| t CLKH | Clock High Time | 35 | - | - | ns |
| t R | Rise Time | - | - | 15 | ns |
| t F | Fall Time | - | - | 15 | ns |


<!-- page 59 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




12.5 I2C Timing Characteristics

(VCI - VSS = 1.65V to 3.5V, TA = 25°C)
 Symbol     Parameter                                                         Min        Typ       Max            Unit
 tcycle     Clock Cycle Time                                                   2.5         -         -             us
 tHSTART    Start condition Hold Time                                          0.6         -         -             us
 tHD        Data Hold Time (for “SDAOUT” pin)                                      0       -         -             ns
            Data Hold Time (for “SDAIN” pin)                                   300         -         -             ns
 tSD        Data Setup Time                                                    100         -         -             ns
 tSSTART    Start condition Setup Time (Only relevant for a repeated           0.6         -         -             us
            Start condition)
 tSSTOP     Stop condition Setup Time                                          0.6         -         -             us
 tR         Rise Time for data and clock pin                                       -       -       300             ns
 tF         Fall Time for data and clock pin                                       -       -       300             ns
 tIDLE      Idle Time before a new transmission can start                      1.3         -         -             us




                                   Figure 12-5: I2C interface Timing characteristics



                                                             //                            //
      SDA

                                  tHD       tF                                                                tIDLE
               tHSTART                                                   tSSTART                         tSSTOP
                                    tR              tSD

      SCL

                         tCYCLE




SSD1362            Rev 1.0    P 59/62    Feb 2015                                                                  Solomon Systech

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| t cycle | Clock Cycle Time | 2.5 | - | - | us |
| t HSTART | Start condition Hold Time | 0.6 | - | - | us |
| t HD | Data Hold Time (for “SDA ” pin) OUT | 0 | - | - | ns |
|  | Data Hold Time (for “SDA ” pin) IN | 300 | - | - | ns |
| t SD | Data Setup Time | 100 | - | - | ns |
| t SSTART | Start condition Setup Time (Only relevant for a repeated Start condition) | 0.6 | - | - | us |
| t SSTOP | Stop condition Setup Time | 0.6 | - | - | us |
| t R | Rise Time for data and clock pin | - | - | 300 | ns |
| t F | Fall Time for data and clock pin | - | - | 300 | ns |
| t IDLE | Idle Time before a new transmission can start | 1.3 | - | - | us |


<!-- page 60 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




13 APPLICATION EXAMPLE
                 Figure 13-1 : SSD1362Z application example for 8-bit 6800-parallel interface mode (Internal regulated VDD)

The configuration for 8-bit 6800-parallel interface mode, externally VCC is shown in the following diagram:
(VCI =VDDIO=2.8V, Internal regulated VDD, external VCC = 18V, IREF = 18.75uA)




                                                           OLED Panel
                                                             256x64
                             SEG255
                             SEG253




                                                                                                           SEG252
                                                                                                           SEG254
                                                   COM63
                                                   COM62




                                                   COM 1
                                                   COM0
                             SEG3
                             SEG1




                                                                                                           SEG0
                                                                                                           SEG2
                                :




                                                      :
                                                      :
                                                      :
                                                      :
                                                      :
                                                      :
                                                      :
                                                      :
                                                      :




                                                                                                              :
                                                           SSD1362Z
                                                                            R/W#(WR#)




                                                                                                                                BGGND
                                                                            E(RD#)




                                                                                                      GPIO0
                                                                                                      GPIO1
                             VCOMH




                                                                                                      D[0:7]
                                                   VDDIO




                                                                            RES#
                                                                            D/C#
          VCC1




                                                                                                                                VSL
                                                                                                                                VLSS
                                                                            CS#
                                      VDD
                    VCC




                                                                                                                    IREF




                                                                                                                                VSS
                                             VCI
                             VP




                                                                                                                     R1

                                                                                                                           C1
                                                                                                                           C2
                                                                                                                           C3
                                                                                                                           C4
                                                                                                                           C5
                                                                          R/W#(WR#)
                                                                             E(RD#)



                                                                                                  D[0:7]
                                                                                CS#
                                                                               RES#
                                                                               D/C#




                  18V                       2.8V 2.8V                                                                           GND
                  VCC                        VCI VDDIO
    Voltage at IREF ≈ VCC – 2.4V. For VCC = 18V, IREF = 18.75uA:
    R1 = (Voltage at IREF - VSS) / IREF
       ≈ (18 – 2.4)V / 18.75uA = 832kΩ
    C1 = C2 = C3: 1uF (1), C4 = C5: 4.7uF (1)

    COG connection recommendations:
    Pin connected to MCU interface: D0~D7, E, R/W#, D/C#, CS#, RES#
    Pin internally connected to VLH: CLS, BS2
    Pin internally connected to VLL: CL, BS1, BS0
    Pin internally connected to VSS: BGGND
    Pin internally connected to VLSS: VSL
    Pin floated: GPIO0, GPIO1, VP (2), FR, TR[10:0]
    Notes
    (1)
        The value is recommended value. Select appropriate value against module application.
    (2)
        Depends on module application, note that VP may connect with a capacitor to VSS.
    (3)
        VLSS of IC pad no. 44 to 49 are recommended to be connected to the VLSS of pad no. 96 to 101 to form a larger area of GND.
    (4)
        VLSS and VSS are not recommended to be connected on the ITO routing, but connected together in the PCB level at one common ground
    point for better grounding and noise insulation.

   Solomon Systech                                                                       Feb 2015 P 60/62      Rev 1.0      SSD1362

<!-- page 61 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




14       PACKAGE INFORMATION

14.1 SSD1362Z Die Tray Information
                                        Figure 14-1: SSD1362Z Die Tray Drawing
                                                                                                        • W3
                 -   .ci
                                                                                                             I
                                                           >,
                                                           ~                                                 I

                                                                                                             I
                                                                   z                                         I
                     m-
                     =~~
                        - t                          A                    'Tl
                                                                          P=li
                                                                          z --
                                                                                                             I
                                                                                                             I
                                                                                                             I
                     ·$==
                     =~~
                                                           ~              su           ----------,-----------
                                                                                                             I
                     ~ - .                                                O')
                                                                                                             I
                     =~~                                                                                     I
 ~J                                                                                                          I
     t                                                                                                       i
                            L25

                 -   a=-             __h_
                                                                                          S)'m .   Spec mm       (mil}
                         D \iVl                       v;
                                                      0
                                                            0
                                                            ,--,

                         • W2                        ! i
                                                                                           WI      76.oo±o.10    (299'2)




           ~
                                                                                           W2      6S . .I       (2f,77)
                                                     sq
                                                            .ef-                           W3      6S            (26119
                                                                                            Dx


                                         '0
                                                                   !
                                         r-<
                                  A-A
                                                    I J        •
                                               ----1,. . -!9
                                                   I/                                       z
                                                                                                    l.Ols±:(W5    (43



                                   ~
                                                                                                    OJ +          (14J
                                                                                            N       125(!)0Ck~t ~umoor)




                                                                                 Remark
                                                                                 1. Depth of text: Max. 0.1mm
                                                                                 2. Tray material: ABS
                                                                                 3. Tray color code: Black
                                                                                 4. Surface resistance 109 ~ 1012 Ω/SQ
                                                                                 5. Tray Warpage: Max. +/- 0.1mm
                                                                                 6. Pocket bottom: Rough Surface




SSD1362        Rev 1.0     P 61/62      Feb 2015                                                                    Solomon Systech

<!-- page 62 -->

This datasheet was downloaded from https://www.crystalfontz.com/controllers/




Solomon Systech reserves the right to make changes without notice to any products herein. Solomon Systech makes no warranty,
representation or guarantee regarding the suitability of its products for any particular purpose, nor does Solomon Systech assume any
liability arising out of the application or use of any product or circuit, and specifically disclaims any, and all, liability, including without
limitation consequential or incidental damages. “Typical” parameters can and do vary in different applications. All operating parameters,
including “Typical” must be validated for each customer application by the customer’s technical experts. Solomon Systech does not con-
vey any license under its patent rights nor the rights of others. Solomon Systech products are not designed, intended, or authorized for use
as components in systems intended for surgical implant into the body, or other applications intended to support or sustain life, or for any
other application in which the failure of the Solomon Systech product could create a situation where personal injury or death may occur.
Should Buyer purchase or use Solomon Systech products for any such unintended or unauthorized application, Buyer shall indemnify and
hold Solomon Systech and its offices, employees, subsidiaries, affiliates, and distributors harmless against all claims, costs, damages, and
expenses, and reasonable attorney fees arising out of, directly or indirectly, any claim of personal injury or death associated with such
unintended or unauthorized use, even if such claim alleges that Solomon Systech was negligent regarding the design or manufacture of the
part.



      The product(s) listed in this datasheet comply with Directive 2011/65/EU of the European Parliament and of the council of 8 June 2011 on the
restriction of the use of certain hazardous substances in electrical and electronic equipment and People’s Republic of China Electronic Industry
Standard SJ/T 11363-2006 “Requirements for concentration limits for certain hazardous substances in electronic information products (电子信息产品
中有毒有害物质的限量要求)”. Hazardous Substances test report is available upon request.



http://www.solomon-systech.com




   Solomon Systech                                                                                Feb 2015 P 62/62          Rev 1.0     SSD1362