# Midas-Displays-MDOB256064D1Y

*Source: `Midas-Displays-MDOB256064D1Y.pdf` (19 pages) — converted from PDF*


<!-- page 1 -->

Electra House, 32 Southtown Road     Telephone +44 (0)1493 602602
                                  Great Yarmouth, Norfolk              Fax +44 (0)1493 665111
                                  NR31 0DU, England                    Email:sales@midasdisplays.com
                                                                       www.midasdisplays.com




MDOB256064D1Y-YS                         256 x 64                     OLED Module
                                                Specification
              Version:    1                                      Date: 25/10/2019
                                                     Revision
                           1    23/10/2019     First Issue




                     Display Features
Resolution                                256 x 64
Appearance                            Yellow on Black
Logic Voltage                               3.3V
Interface                                   SPI
Module Size                      70.00 x 22.00 x 1.71mm
Operating Temperature                 -40°C ~ +80°C                  Box Quantity     Weight / Display
Construction                               COB                           ---                ---

* - For full design functionality, please use this
specification in conjunction with the SSD1362
specification. (Provided Separately)

              Display Accessories                                      Optional Variants
   Part Number                 Description                             Appearance              Voltage

**Extracted table(s) on this page:**

| Display Accessories |  |
| --- | --- |
| Part Number | Description |

| Optional Variants |  |
| --- | --- |
| Appearance | Voltage |


<!-- page 2 -->

General Specification
 The Features is described as follow:
      Module dimension: 70.0 x 22.0 x 1.71mm
      Active area: 51.18 x 12.78mm
      Dot Matrix: 256 x 64 Dots
      Pixel Size: 0.18 x 0.18 mm
      Pixel Pitch: 0.20 x 0.20 mm
      Display Mode: Passive Matrix
      Duty: 1/64 Duty
      Gray Scale: 4 Bits
      Display Color: Yellow
      IC: SSD1362
      Interface: SPI
      Size: 2.08 inch




Interface Pin Function
 No. Symbol                                     Function
  1   GND Reserved pin. It should be connected to ground.
            Power supply for panel driving voltage. This is also the most positive power
  2   VCC
            voltage supply pin. It is supplied by external high voltage source.
            These pins are bi-directional data bus connecting to the MCU data bus.
  3    D0
            Unused pins are recommended to tie LOW.
            When serial interface mode is selected, D0 will be the serial clock input:
  4    D1
            SCLK; D1 will be the serial data input: SID.
            This pin is reset signal input.
  5   RES# When the pin is pulled LOW, initialization of the chip is executed.
            Keep this pin pull HIGH during normal operation.
            This pin is Data/Command control pin connecting to the MCU.
            When the pin is pulled HIGH, the data at D[1:0] will be interpreted as data.
  6   D/C#
            When the pin is pulled LOW, the data at D[1:0] will be transferred to a
            command register.
            This pin is the chip select input connecting to the MCU.
  7   CS# The chip is enabled for MCU communication only when CS# is pulled LOW
            (active LOW).

**Extracted table(s) on this page:**

| No. | Symbol | Function |
| --- | --- | --- |
| 1 | GND | Reserved pin. It should be connected to ground. |
| 2 | VCC | Power supply for panel driving voltage. This is also the most positive power voltage supply pin. It is supplied by external high voltage source. |
| 3 | D0 | These pins are bi-directional data bus connecting to the MCU data bus. Unused pins are recommended to tie LOW. When serial interface mode is selected, D0 will be the serial clock input: SCLK; D1 will be the serial data input: SID. |
| 4 | D1 |  |
| 5 | RES# | This pin is reset signal input. When the pin is pulled LOW, initialization of the chip is executed. Keep this pin pull HIGH during normal operation. |
| 6 | D/C# | This pin is Data/Command control pin connecting to the MCU. When the pin is pulled HIGH, the data at D[1:0] will be interpreted as data. When the pin is pulled LOW, the data at D[1:0] will be transferred to a command register. |
| 7 | CS# | This pin is the chip select input connecting to the MCU. The chip is enabled for MCU communication only when CS# is pulled LOW (active LOW). |


<!-- page 3 -->

Contour Drawing & Block Diagram
                                                               60.5¡ Ó
                                                                     0.2                                                                                                                                                                         PIN SYMBOL
                             0.5¡ Ó
                                  0.5                        55.9¡ Ó
                                                                   0.2 POL                                                                                                                                                                       1   GND
                                  1.1                         53.18 VA
                                                                                                                                                                                                                                                 2   VCC
                                  2.1                         51.18 AA
                                                                                                              2                         1.71¡ Ó
                                                                                                                                              0.2
                                                                                                                                                                                          70¡ Ó
                                                                                                                                                                                              0.5                                                3    D0
                4.25¡ Ó
                      0.5
               0.5
          0.5¡ Ó




                                                                                                                                                    (2.2)   (16.55)                                                                              4    D1
                                                                                                4.3
          2.11




                                                                                                                                       7.5
          3.11




                                                                                                2




                                                                                                                                                                                                                                                 5   RES#
                                                                                                                                                                                                                                                 6   D/C#




                                                                                                                                                                      24
                                               1




                                                                                                                                                                           P0.7*23=16.1
                                                                                                                                                                                                                                                 7   CS#
              0.2 POL

           12.78 AA
           14.78 VA


                                         0.5




                                                                                                                                                                                                                                          0.5
    0.2




                                    1.5¡ Ó




                                                                                                                                                                                                                                      22¡ Ó
19¡ Ó




                                                                                                13.4
                                                                                                 18




                                                             256*64 2.08"
          18¡ Ó



                                               7




                                                                                                                                                                      1
                                                                             4- 2.5 PTH                                                  1
                                                                             4- 4.0 PAD
                                                                                                                                                                                                                                  S255(SEG127)
                                                                                                                                                                                                                                  S1(SEG0)
                                                                                                                                                                                                                                  C1(COM0)
                                                                                 Component area
                                                                  2.5 Max.




                                                                                                                                                                                          256*64
                                                                                                       0.2 Dot pitch                                                                                                              C64(COM63)
                    3.38




                                                                                                              0.18 Dot size                                                                                                       S2(SEG128)
                                     2.5
                                                                                                                                                                                                                                  S256(SEG255)
                                                   1.0 PTH
                                               1




                                                   2.0 PAD
                    P2.54*6=15.24




                                                                                                                                                                                                          P2.54*(7-1)=15.24




                                                                                                                                                                                                    1.5




                                                                                                                                                                                                                              6
                                                                                                                  0.18 Dot size
                                                                                              0.2 Dot pitch
                                               7                                                                                   Detail A




                                                                                                                                                                                                                              2
                                                                                                                                  SCALE 1:30
                                                                                                                                                                The non-specified tolerance of dimension is ¡ Ó
                                                                                                                                                                                                              0.3 mm .

**Extracted table(s) on this page:**

| 5 | 4 | 3 | 2 | 1 | PIN |
| --- | --- | --- | --- | --- | --- |
| RES# | D1 | D0 | VCC | GND | SYMBOL |


<!-- page 4 -->

Application recommendations




Recommended components：
C1：4.7uF

Note
(1) The capacitor value is recommended value. Select appropriate value against module
application.


Absolute Maximum Ratings

          Parameter               Symbol         Min       Max        Unit      Notes

        Supply Voltage              VCC         1.65        5.5         V         1,2

   Operating Temperature            TOP          -40        +80        °C         —

    Storage Temperature            TSTG          -40        +85        °C         —
Note 1: All the above voltages are on the basis of “VSS = 0V”.
Note 2: When this module is used beyond the above absolute maximum ratings, permanent
breakage of the module may occur. Also, for normal operations, it is desirable to use this
module under the conditions according to Section 6.“Optics & Electrical Characteristics”. If this
module is used beyond these conditions, malfunctioning of the module can occur and the
reliability of the module may deteriorate.

**Extracted table(s) on this page:**

| Parameter | Symbol | Min | Max | Unit | Notes |
| --- | --- | --- | --- | --- | --- |
| Supply Voltage | VCC | 1.65 | 5.5 | V | 1,2 |
| Operating Temperature | TOP | -40 | +80 | °C | — |
| Storage Temperature | TSTG | -40 | +85 | °C | — |


<!-- page 5 -->

Electrical Characteristics
 DC Electrical Characteristics
            Item            Symbol   Condition     Min     Typ    Max      Unit

Supply Voltage               VCC        －          2.8     3.3     5.2      V

Input High Volt.             VIH        －        0.8×VCC   －      VCC       V

Input Low Volt.              VIL        －           0      －     0.2×VCC    V

Output High Volt.            VOH        －        0.9×VCC   －      VCC       V

Output Low Volt.             VOL        －           0      －     0.1×VCC    V
50% Check Board operating                          －
                             ICC     VCC=3.3V              90      135     mA
Current

**Extracted table(s) on this page:**

| Item | Symbol | Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Supply Voltage | VCC | － | 2.8 | 3.3 | 5.2 | V |
| Input High Volt. | VIH | － | 0.8×VCC | － | VCC | V |
| Input Low Volt. | VIL | － | 0 | － | 0.2×VCC | V |
| Output High Volt. | VOH | － | 0.9×VCC | － | VCC | V |
| Output Low Volt. | VOL | － | 0 | － | 0.1×VCC | V |
| 50% Check Board operating Current | ICC | VCC=3.3V | － | 90 | 135 | mA |


<!-- page 6 -->

Initial code
void Initial_SSD1362()
{
      LCM_CS1=0;

Write_command(0XFD); //Set Command Lock
Write_command(0X12); //(12H=Unlock,16H=Lock)

Write_command(0XAE); //Display OFF(Sleep Mode)

Write_command(0X15); //Set column Address
Write_command(0X00); //Start column Address
Write_command(0X7F); //End column Address

Write_command(0X75); //Set Row Address
Write_command(0X00); //Start Row Address
Write_command(0X3F); //End Row Address

Write_command(0X81); //Set contrast
Write_command(0x2f);

Write_command(0XA0); //Set Remap
Write_command(0Xc3);

Write_command(0XA1); //Set Display Start Line
Write_command(0X00);

Write_command(0XA2); //Set Display Offset
Write_command(0X00);

Write_command(0XA4); //Normal Display

Write_command(0XA8); //Set Multiplex Ratio
Write_command(0X3F);

Write_command(0XAB); //Set VDD regulator
Write_command(0X01); //Regulator Enable

Write_command(0XAD); //External /Internal IREF Selection
Write_command(0X8E);

Write_command(0XB1); //Set Phase Length
Write_command(0X22);

Write_command(0XB3); //Display clock Divider
Write_command(0XA0);

Write_command(0XB6); //Set Second pre-charge Period
Write_command(0X04);

<!-- page 7 -->

Write_command(0XB9); //Set Linear LUT

Write_command(0XBc); //Set pre-charge voltage level
Write_command(0X10); //0.5*Vcc

Write_command(0XBD); //Pre-charge voltage capacitor Selection
Write_command(0X01);

Write_command(0XBE); //Set COM deselect voltage level
Write_command(0X07); //0.82*Vcc

 Write_command(0XAF); //Display ON
}

<!-- page 8 -->

Optical Characteristics
       Item            Symbol          Condition        Min        Typ        Max       Unit

                         (V)θ             －             160         －          －         deg
   View Angle
                         (H)φ             －             160         －          －         deg

  Contrast Ratio          CR             Dark         2000:1        －          －         －

                         T rise           －             －           10         －         μs
 Response Time
                         T fall           －             －           10         －         μs

   Display with 100% check Board Brightness             100        120         －        cd/m2

          CIEx(Yellow)              x,y(CIE1931)       0.45        0.47       0.49       －

          CIEy(Yellow)              x,y(CIE1931)       0.48        0.50       0.52       －




OLED Lifetime


     ITEM                 Conditions                  Min            Typ             Remark


                   Ta=25°C
   Operating
                   / Initial 50% check board       50,000 Hrs            -            Note
   Life Time
                   brightness 100cd/ m2
Notes:
1. Life time is defined the amount of time when the luminance has decayed to <50% of the
   initial value.
2. This analysis method uses life data obtained under accelerated conditions to extrapolate
   an estimated probability density function (pdf) for the product under normal use conditions.
3. Screen saving mode will extend OLED lifetime.

**Extracted table(s) on this page:**

| Item | Symbol | Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| View Angle | (V)θ | － | 160 | － | － | deg |
|  | (H)φ | － | 160 | － | － | deg |
| Contrast Ratio | CR | Dark | 2000:1 | － | － | － |
| Response Time | T rise | － | － | 10 | － | μs |
|  | T fall | － | － | 10 | － | μs |
| Display with 100% check Board Brightness |  |  | 100 | 120 | － | cd/m2 |
| CIEx(Yellow) |  | x,y(CIE1931) | 0.45 | 0.47 | 0.49 | － |
| CIEy(Yellow) |  | x,y(CIE1931) | 0.48 | 0.50 | 0.52 | － |

| ITEM | Conditions | Min | Typ | Remark |
| --- | --- | --- | --- | --- |
| Operating Life Time | Ta=25°C / Initial 50% check board brightness 100cd/ m2 | 50,000 Hrs | - | Note |


<!-- page 9 -->

Reliability
 Content of Reliability Test
  Environmental Test
                                                                                      Applicable
  Test Item          Content of Test                            Test Condition
                                                                                      Standard
  High
                     Endurance test applying the high           85°C
  Temperature                                                                         ——
                     storage temperature for a long time.       240hrs
  storage
  Low
                     Endurance test applying the low storage -40°C
  Temperature                                                                         ——
                     temperature for a long time.            240hrs
  storage
                     Endurance test applying the electric
  High
                     stress (Voltage & Current) and the         80°C
  Temperature                                                                         ——
                     thermal stress to the element for a long   240hrs
  Operation
                     time.
  Low                Endurance test applying the electric
                                                                -40°C
  Temperature        stress under low temperature for a long                          ——
                                                                240hrs
  Operation          time.
  High
                     Endurance test applying the high
  Temperature/                                                  60°C,90%RH
                     temperature and high humidity storage                            ——
  Humidity                                                      240hrs
                     for a long time.
  Storage
  High
                     Endurance test applying the high
  Temperature/                                                  60°C,90%RH
                     temperature and high humidity                                    ——
  Humidity                                                      120hrs
                     Operation for a long time.
  Operation
                     Endurance test applying the low and
                     high temperature cycle.
  Temperature           -40°C     25°C       80°C               -40°C /80°C
                                                                                      ——
  Cycle                                                         30 cycles
                        30min      5min       30min
                                 1 cycle
  Mechanical Test
                                                                Frequency:10~55Hz
                     Endurance test applying the vibration      amplitude:1.5mm
  Vibration test                                                                  ——
                     during transportation and using.           Time:0.5hrs/axis
                                                                Test axis:X,Y,Z
  Others


  Static             Endurance test applying the electric       Air Discharge model
                                                                                        ——
  electricity test   stress to the finished product housing.    ±4kv,10 times



*** Supply voltage for OLED system =Operating voltage at 25°C

<!-- page 10 -->

Test and measurement conditions
1. All measurements shall not be started until the specimens attain to temperature stability.
   After the completion of the described reliability test, the samples were left at room
   temperature for 2 hrs prior to conducting the failure test at 23±5°C; 55±15% RH.
2. All-pixels on/off exchange is used as operation test pattern.
3. The degradation of Polarizer are ignored for High Temperature storage, High Temperature/
   Humidity Storage, Temperature Cycle
Evaluation criteria
1. The function test is OK.
2. No observable defects.
3. Luminance: > 50% of initial value.
4. Current consumption: within ± 50% of initial value.
APPENDIX:
RESIDUE IMAGE
Because the pixels are lighted in different time, the luminance of active pixels
may reduce or differ from inactive pixels. Therefore, the residue image will occur.
To avoid the residue image, every pixel needs to be lighted up uniformly.

<!-- page 11 -->

Inspection specification
Inspection Standard:
MIL-STD-105E table normal inspection single sample level II.
Definition
1 Major defect : The defect that greatly affect the usability of product.
2 Minor defect : The other defects, such as cosmetic defects, etc.
  Definition of inspection zone:
                                C
                                B

                                A




Zone A: Active Area
Zone B: Viewing Area except Zone A
Zone C: Outside Viewing Area
Note: As a general rule, visual defects in Zone C are permissible, when it is no trouble of
     quality and assembly to customer`s product.

Inspection Methods
1 The general inspection : Under fluorescent light illumination: 750~1500 Lux, about 30cm
 viewing distance, within 45º viewing angle, under 25±5°C.
2 The luminance and color coordinate inspection : By SR-3 or BM-7 or the equal
 equipments, in the dark room, under 25±5°C.

NO       Item                                      Criterion                              AQL
                     1.1 Missing vertical, horizontal segment, segment contrast defect.
                     1.2 Missing character , dot or icon.
                     1.3 Display malfunction.
        Electrical   1.4 No function or no display.
01                                                                                        0.65
         Testing     1.5 Current consumption exceeds product specifications.
                     1.6 OLED viewing angle defect.
                     1.7 Mixed product types.
                     1.8 Contrast defect.
        Black or
         white
                     2.1 White and black spots on display ≦0.25mm, no more than
        spots on
02                   three white or black spots present.                                      2.5
         OLED        2.2 Densely spaced: No more than two spots or lines within 3mm.
        (display
          only)

**Extracted table(s) on this page:**

| NO | Item | Criterion | AQL |
| --- | --- | --- | --- |
| 01 | Electrical Testing | 1.1 Missing vertical, horizontal segment, segment contrast defect. 1.2 Missing character , dot or icon. 1.3 Display malfunction. 1.4 No function or no display. 1.5 Current consumption exceeds product specifications. 1.6 OLED viewing angle defect. 1.7 Mixed product types. 1.8 Contrast defect. | 0.65 |
| 02 | Black or white spots on OLED (display only) | 2.1 White and black spots on display 0.25mm, no more than three white or black spots present. 2.2 Densely spaced: No more than tw≦o spots or lines within 3mm. | 2.5 |


<!-- page 12 -->

NO      Item                                       Criterion                             AQL

                      3.1 Round type :
                      As following
      OLED
                      drawing                   SIZE           Acceptable QTY    Zone
      black
                      Φ=( x + y ) / 2       Φ≦0.10               Accept no
      spots,                                                                     A+ B,
                                                                   dense
      white
                                            0.10＜Φ≦0.20               2          A+ B    2.5
      spots,
      contamin                              0.20＜Φ≦0.25               1          A+ B
      ation                                 0.25＜Φ                    0          A+ B
      (non-display)




                      3.2 Line type : (As following drawing)
03




                                   Length          Width          Acceptable
                                                                                 Zone
                                                                    Q TY                 2.5
                                      ---     W≦0.02              Accept no
                                                                                 A+B
                                                                    dense
                                   L≦3.0      0.02＜W≦0.03                        A+B
                                                                       2
                                   L≦2.5      0.03＜W≦0.05                        A+B
                                    ---       0.05＜W             As round type



                      If bubbles are             Size Φ        Acceptable Q TY   Zone
                      visible, judge        Φ≦0.20             Accept no dense   A+B
                      using black spot      0.20＜Φ≦0.50                3         A+B
      Polarizer       specifications,
04
      bubbles                               0.50＜Φ≦1.00                2         A+B     2.5
                      not easy to find,
                      must check in         1.00＜Φ                     0         A+B
                      specify direction.    Total Q TY                 3



05   Scratches        Follow NO.3 OLED black spots, white spots, contamination.

**Extracted table(s) on this page:**

| NO | Item | Criterion | AQL |
| --- | --- | --- | --- |
| 03 | OLED black spots, white spots, contamin ation (non-display) | 3.1 Round type : As following drawing SIZE Acceptable QTY Zone Φ=( x + y ) / 2 Φ≦0.10 Accept no A+ B, dense 0.10＜Φ≦0.20 2 A+ B 0.20＜Φ≦0.25 1 A+ B 0.25＜Φ 0 A+ B | 2.5 |
|  |  | 3.2 Line type : (As following drawing) Length Width Acceptable Zone Q TY --- W≦0.02 Accept no A+B dense L≦3.0 0.02＜W≦0.03 A+B 2 L≦2.5 0.03＜W≦0.05 A+B --- 0.05＜W As round type | 2.5 |
| 04 | Polarizer bubbles | If bubbles are Size Φ Acceptable Q TY Zone visible, judge Φ≦0.20 Accept no dense A+B using black spot 0.20＜Φ≦0.50 3 A+B specifications, 0.50＜Φ≦1.00 2 A+B not easy to find, 1.00＜Φ 0 A+B must check in Total Q TY 3 specify direction. | 2.5 |
| 05 | Scratches | Follow NO.3 OLED black spots, white spots, contamination. |  |

| SIZE | Acceptable QTY | Zone |
| --- | --- | --- |
| Φ≦0.10 | Accept no dense | A+ B, |
| 0.10＜Φ≦0.20 | 2 | A+ B |
| 0.20＜Φ≦0.25 | 1 | A+ B |
| 0.25＜Φ | 0 | A+ B |

| Length | Width | Acceptable Q TY | Zone |
| --- | --- | --- | --- |
| --- | W≦0.02 | Accept no dense | A+B |
| L≦3.0 | 0.02＜W≦0.03 | 2 | A+B |
| L≦2.5 | 0.03＜W≦0.05 |  | A+B |
| --- | 0.05＜W | As round type |  |

| Size Φ | Acceptable Q TY | Zone |
| --- | --- | --- |
| Φ≦0.20 | Accept no dense | A+B |
| 0.20＜Φ≦0.50 | 3 | A+B |
| 0.50＜Φ≦1.00 | 2 | A+B |
| 1.00＜Φ | 0 | A+B |
| Total Q TY | 3 |  |


<!-- page 13 -->

NO    Item                                   Criterion                               AQL
               Symbols Define:
               x: Chip length      y: Chip width     z: Chip thickness
               k: Seal width       t: Glass thickness a: OLED side length
               L: Electrode pad length:
               6.1 General glass chip :
               6.1.1 Chip on panel surface and crack between panels:


                                                                                     2.5



                z: Chip thickness         y: Chip width          x: Chip length
                      Z≦1/2t         Not over viewing area           x≦1/8a
     Chipped        1/2t＜z≦2t           Not exceed 1/3k              x≦1/8a
      glass    ☉If there are 2 or more chips, x is total length of each chip.

               6.1.2 Corner crack:



06
                                                                                     2.5
                z: Chip thickness        y: Chip width           x: Chip length
                     Z≦1/2t         Not over viewing area           x≦1/8a
                   1/2t＜z≦2t           Not exceed 1/3k              x≦1/8a
                ☉If there are 2 or more chips, x is the total length of each chip.

               Symbols :
               x: Chip length       y: Chip width     z: Chip thickness
               k: Seal width        t: Glass thickness a: OLED side length
               L: Electrode pad length
               6.2 Protrusion over terminal :
               6.2.1 Chip on electrode pad :
     Glass
                                                                                     2.5
     crack


                   y: Chip width         x: Chip length      z: Chip thickness
                    y≦0.5mm                 x≦1/8a              0 ＜ z≦t

**Extracted table(s) on this page:**

| NO | Item | Criterion | AQL |
| --- | --- | --- | --- |
| 06 | Chipped glass | Symbols Define: x: Chip length y: Chip width z: Chip thickness k: Seal width t: Glass thickness a: OLED side length L: Electrode pad length: 6.1 General glass chip : 6.1.1 Chip on panel surface and crack between panels: z: Chip thickness y: Chip width x: Chip length Z≦1/2t Not over viewing area x≦1/8a 1/2t＜z≦2t Not exceed 1/3k x≦1/8a ☉If there are 2 or more chips, x is total length of each chip. | 2.5 |
|  |  | 6.1.2 Corner crack: z: Chip thickness y: Chip width x: Chip length Z≦1/2t Not over viewing area x≦1/8a 1/2t＜z≦2t Not exceed 1/3k x≦1/8a ☉If there are 2 or more chips, x is the total length of each chip. | 2.5 |
|  | Glass crack | Symbols : x: Chip length y: Chip width z: Chip thickness k: Seal width t: Glass thickness a: OLED side length L: Electrode pad length 6.2 Protrusion over terminal : 6.2.1 Chip on electrode pad : y: Chip width x: Chip length z: Chip thickness y≦0.5mm x≦1/8a 0 ＜ z ≦ t | 2.5 |

| z: Chip thickness | y: Chip width | x: Chip length |
| --- | --- | --- |
| Z≦1/2t | Not over viewing area | x≦1/8a |
| 1/2t＜z≦2t | Not exceed 1/3k | x≦1/8a |

| z: Chip thickness | y: Chip width | x: Chip length |
| --- | --- | --- |
| Z≦1/2t | Not over viewing area | x≦1/8a |
| 1/2t＜z≦2t | Not exceed 1/3k | x≦1/8a |

| y: Chip width | x: Chip length | z: Chip thickness |
| --- | --- | --- |
| y≦0.5mm | x≦1/8a | 0 ＜ z ≦ t |


<!-- page 14 -->

NO     Item                                  Criterion                                AQL

                 6.2.2 Non-conductive portion:




                          y: Chip width        x: Chip length    z: Chip thickness
                              y≦ L                x≦1/8a            0 ＜ z≦t
                 ☉If the chipped area touches the ITO terminal, over 2/3 of the ITO
     Glass
06                must remain and be inspected according to electrode terminal        2.5
     crack
                  specifications.
                 ☉If the product will be heat sealed by the customer, the alignment
                   mark not be damaged.

                 6.2.3 Substrate protuberance and internal crack.
                                                  y: width          x: length
                                                 y≦1/3L              x≦a




     Cracked
07               The OLED with extensive crack is not acceptable.                     2.5
      glass


                 8.1 Illumination source flickers when lit.                           0.65
     Backlight   8.2 Spots or scratched that appear when lit must be judged. Using     2.5
08
     elements       OLED spot, lines and contamination standards.
                 8.3 Backlight doesn’t light or color wrong.                          0.65


                 9.1 Bezel may not have rust, be deformed or have fingerprints,       2.5
09     Bezel        stains or other contamination.
                 9.2 Bezel must comply with job specifications.                       0.65

**Extracted table(s) on this page:**

| NO | Item | Criterion | AQL |
| --- | --- | --- | --- |
| 06 | Glass crack | 6.2.2 Non-conductive portion: y: Chip width x: Chip length z: Chip thickness y≦ L x≦1/8a 0 ＜ z ≦ t ☉If the chipped area touches the ITO terminal, over 2/3 of the ITO must remain and be inspected according to electrode terminal specifications. ☉If the product will be heat sealed by the customer, the alignment mark not be damaged. 6.2.3 Substrate protuberance and internal crack. y: width x: length y≦1/3L x ≦ a | 2.5 |
| 07 | Cracked glass | The OLED with extensive crack is not acceptable. | 2.5 |
| 08 | Backlight elements | 8.1 Illumination source flickers when lit. 8.2 Spots or scratched that appear when lit must be judged. Using OLED spot, lines and contamination standards. 8.3 Backlight doesn’t light or color wrong. | 0.65 2.5 0.65 |
| 09 | Bezel | 9.1 Bezel may not have rust, be deformed or have fingerprints, stains or other contamination. 9.2 Bezel must comply with job specifications. | 2.5 0.65 |

| y: Chip width | x: Chip length | z: Chip thickness |
| --- | --- | --- |
| y≦ L | x≦1/8a | 0 ＜ z ≦ t |

| and internal crac y: width | k. x: length |
| --- | --- |
| y≦1/3L | x ≦ a |


<!-- page 15 -->

NO      Item                                   Criterion                                AQL

                  10.1 COB seal may not have pinholes larger than 0.2mm or
                                                                                  2.5
                     contamination.
                  10.2 COB seal surface may not have pinholes through to the IC.
                                                                                  2.5
                  10.3 The height of the COB should not exceed the height
                                                                                 0.65
                     indicated in the assembly diagram.
                  10.4 There may not be more than 2mm of sealant outside the
                                                                                  2.5
                     seal area on the PCB. And there should be no more than
                     three places.
10   PCB , COB
                  10.5 No oxidation or contamination PCB terminals.
                                                                                  2.5
                  10.6 Parts on PCB must be the same as on the production
                                                                                 0.65
                     characteristic chart. There should be no wrong parts,
                     missing parts or excess parts.
                  10.7 The jumper on the PCB should conform to the product
                                                                                 0.65
                     characteristic chart.
                  10.8 If solder gets on bezel tab pads, OLED pad, zebra pad or
                                                                                  2.5
                     screw hold pad, make sure it is smoothed down.

                  11.1 No un-melted solder paste may be present on the PCB.          2.5
                  11.2 No cold solder joints, missing solder connections, oxidation 2.5
11   Soldering        or icicle.
                  11.3 No residue or solder balls on PCB.                            2.5
                  11.4 No short circuits in components on PCB.                      0.65


                  12.1 No oxidation, contamination, curves or, bends on interface       2.5
                      Pin (OLB) of TCP.
                  12.2 No cracks on interface pin (OLB) of TCP.                         0.65
                  12.3 No contamination, solder residue or solder balls on               2.5
                      product.
                  12.4 The IC on the TCP may not be damaged, circuits.                  2.5
                  12.5 The uppermost edge of the protective strip on the interface      2.5
                      pin must be present or look as if it cause the interface pin to
     General
12                    sever.
     appearance
                  12.6 The residual rosin or tin oil of soldering (component or chip    2.5
                      component) is not burned into brown or black color.
                  12.7 Sealant on top of the ITO circuit has not hardened.               2.5
                  12.8 Pin type must match type in specification sheet.                 0.65
                  12.9 OLED pin loose or missing pins.                                  0.65
                  12.10 Product packaging must the same as specified on                 0.65
                      packaging specification sheet.
                  12.11 Product dimension and structure must conform to product         0.65
                      specification sheet.

**Extracted table(s) on this page:**

| NO | Item | Criterion | AQL |
| --- | --- | --- | --- |
| 10 | PCB , COB | 10.1 COB seal may not have pinholes larger than 0.2mm or contamination. 10.2 COB seal surface may not have pinholes through to the IC. 10.3 The height of the COB should not exceed the height indicated in the assembly diagram. 10.4 There may not be more than 2mm of sealant outside the seal area on the PCB. And there should be no more than three places. 10.5 No oxidation or contamination PCB terminals. 10.6 Parts on PCB must be the same as on the production characteristic chart. There should be no wrong parts, missing parts or excess parts. 10.7 The jumper on the PCB should conform to the product characteristic chart. 10.8 If solder gets on bezel tab pads, OLED pad, zebra pad or screw hold pad, make sure it is smoothed down. | 2.5 2.5 0.65 2.5 2.5 0.65 0.65 2.5 |
| 11 | Soldering | 11.1 No un-melted solder paste may be present on the PCB. 11.2 No cold solder joints, missing solder connections, oxidation or icicle. 11.3 No residue or solder balls on PCB. 11.4 No short circuits in components on PCB. | 2.5 2.5 2.5 0.65 |
| 12 | General appearance | 12.1 No oxidation, contamination, curves or, bends on interface Pin (OLB) of TCP. 12.2 No cracks on interface pin (OLB) of TCP. 12.3 No contamination, solder residue or solder balls on product. 12.4 The IC on the TCP may not be damaged, circuits. 12.5 The uppermost edge of the protective strip on the interface pin must be present or look as if it cause the interface pin to sever. 12.6 The residual rosin or tin oil of soldering (component or chip component) is not burned into brown or black color. 12.7 Sealant on top of the ITO circuit has not hardened. 12.8 Pin type must match type in specification sheet. 12.9 OLED pin loose or missing pins. 12.10 Product packaging must the same as specified on packaging specification sheet. 12.11 Product dimension and structure must conform to product specification sheet. | 2.5 0.65 2.5 2.5 2.5 2.5 2.5 0.65 0.65 0.65 0.65 |


<!-- page 16 -->

Check Item       Classification   Criteria



    No Display           Major




    Missing Line         Major




    Pixel Short          Major




   Darker Short          Major




   Wrong Display         Major




     Un-uniform
B/A x 100% < 70%         Major
  A/C x 100% < 70%

**Extracted table(s) on this page:**

| Check Item | Classification | Criteria |
| --- | --- | --- |
| No Display | Major |  |
| Missing Line | Major |  |
| Pixel Short | Major |  |
| Darker Short | Major |  |
| Wrong Display | Major |  |
| Un-uniform B/A x 100% < 70% A/C x 100% < 70% | Major |  |


<!-- page 17 -->

Precautions in use of OLED Modules
(1) Avoid applying excessive shocks to module or making any alterations or modifications to it.
(2) Don’t make extra holes on the printed circuit board, change the components or modify its
     shape of OLED display module.
(3) Don’t disassemble the OLED display module.
(4) Do not apply input signals while the logic power is off.
(5) Don’t operate it above the absolute maximum rating.
(6) Don’t drop, bend or twist OLED display module.
(7) Soldering: only to the I/O terminals.
(8) Hot-Bar FPC soldering condition: 280~350C, less than 5 seconds.
(9) Midas has the right to change the passive components (Resistors, capacitors and other
     passive components will have different appearance and color caused by the different
     supplier.) and change the PCB Rev. (In order to satisfy the supplying stability, management
     optimization and the best product performance...etc, under the premise of not affecting the
     electrical characteristics and external dimensions, Midas have the right to modify the
     version.)
(10) Midas has the right to upgrade or modify the product function.

1. Handling Precautions
(1) Since the display panel is being made of glass, do not apply mechanical impacts such as
    dropping from a high position.
(2) If the display panel is broken by some accident and the internal organic substance leaks out,
     be careful not to inhale nor lick the organic substance.
(3) If pressure is applied to the display surface or its neighborhood of the OLED display module,
     the cell structure may be damaged. So, be careful not to apply pressure to these sections.
(4) The polarizer covering the surface of the OLED display module is soft and easily scratched.
(5) When the surface of the polarizer of the OLED display module has soil, clean the surface. It
     takes advantage by using following adhesion tape.
     * Scotch Mending Tape No. 810 or an equivalent
     Never try to breathe upon the soiled surface nor wipe the surface using cloth containing
     solvent such as ethyl alcohol, since the surface of the polarizer will become cloudy.
     Also, pay attention that the following liquid and solvent may spoil the polarizer:
     * Water
     * Ketone
     * Aromatic Solvents
(6) Protection film is being applied to the surface of the display panel and removes the
     protection film before assembling it. At this time, if the OLED display module has been
     stored for a long period of time, residue adhesive material of the protection film may remain
     on the surface of the display panel after removed of the film. In such case, remove the
     residue material by the method introduced in the above Section 5.
(7) Do not touch the following sections whenever possible while handling the OLED display
     modules.
     * Pins and electrodes
     * Pattern layouts such as the TCP & FPC
(8) Hold OLED display module very carefully when placing OLED display module into the
     System housing. Do not apply excessive stress or pressure to OLED display module. And,
     do not over bend the film with electrode pattern layouts. These stresses will influence the
     display performance. Also, secure sufficient rigidity for the outer cases.

<!-- page 18 -->

(9) Do not apply stress to the LSI chips and the surrounding molded sections.
(10) Pay sufficient attention to the working environments when handing OLED display modules
     to prevent occurrence of element breakage accidents by static electricity.
     * Be sure to make human body grounding when handling OLED display modules.
     * Be sure to ground tools to use or assembly such as soldering irons.
     * To suppress generation of static electricity, avoid carrying out assembly work under dry
     environments.
     * Protective film is being applied to the surface of the display panel of the OLED display
     module. Be careful since static electricity may be generated when exfoliating the protective
     film.

2. Storage Precautions
(1) When storing OLED display modules, put them in static electricity preventive bags to avoid
     be directly exposed to sun or lights of fluorescent lamps. (We recommend you to store these
     modules in the packaged state when they were shipped from Midas Displays. At that
     time, be careful not to let water drops adhere to the packages or bags.)

(2) When the OLED display module is being dewed or when it is placed under high temperature
    or high humidity environments, the electrodes may be corroded if electric current is applied.
    Please store it in clean environment.

3. Designing Precautions
(1) The absolute maximum ratings are the ratings which cannot be exceeded for OLED display
    module, and if these values are exceeded, OLED display module may be damaged.
(2) To prevent occurrence of malfunctioning by noise, pay attention to satisfy the VIL and VIH
     specification and to make the signal line cable as short as possible.
(3) We recommend you to install excess current preventive unit (fuses, etc.) to the power circuit
     (VDD / VCC). (Recommend value: 0.5A)
(4) Pay sufficient attention to avoid occurrence of mutual noise interference with the nearby
     devices.
(5) As for EMI, take necessary measures on the equipment side basically.
(6) If the power supplied to the OLED display module is forcibly shut down by such errors as
     taking out the main battery while the OLED display panel is in operation, we cannot
     guarantee the quality of this OLED display module.
     * Connection (contact) to any other potential than the above may lead to rupture of the IC.
(7) If this OLED driver is exposed to light, malfunctioning may occur and semiconductor
     elements may change their characteristics.
(8) The internal status may be changed, if excessive external noise enters into the module.
     Therefore, it is necessary to take appropriate measures to suppress noise generation or to
     protect module from influences of noise on the system design.
(9) We recommend you to make periodical refreshment of the operation statuses (re-setting of

<!-- page 19 -->

the commands and re-transference of the display data) to cope with catastrophic noise.
(10) It's pretty common to use "Screen Saver" to extend the lifetime and Don't use the same
     image for long time in real application. When an OLED display module is operated for a long
     of time with fixed pattern, an afterimage or slight contrast deviation may occur.
(11) The limitation of FPC and Film bending.




(12) The module should be fixed balanced into the housing, or the module may be twisted.
             (0.1 Max.)




                                                           0.1




4. Precautions when disposing of the OLED display modules
(1) Request the qualified companies to handle industrial wastes when disposing of the OLED
     display modules. Or, when burning them, be sure to observe the environmental and hygienic
     laws and regulations.