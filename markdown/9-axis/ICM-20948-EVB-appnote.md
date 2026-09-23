# AN-IVS-0001EVB-00-v1-3

*Source: `AN-IVS-0001EVB-00-v1-3.pdf` (19 pages) — converted from PDF*


<!-- page 1 -->

Application Note


        InvenSense Motion Sensor Universal
        Evaluation Board (UEVB) User Guide



PURPOSE
This document describes the hardware and circuitry on the Universal Evaluation Board (UEVB). The UEVB is used to
evaluate most of InvenSense’s current motion sensing (gyroscopes, accelerometers, magnetometers) products. It
covers applying the UEVB to a larger system, and requires the understanding of key signals and circuit functions,
hardware jumper settings, and port connections.

USAGE
This UEVB provides up to nine axes of motion sensing comprised of:

    •     Digital-output of 3-axis gyroscope with user-programmable full-scale ranges
    •     Digital-output of 3-axis accelerometer with user-programmable full-scale ranges
    •     Digital-output of 3-axis magnetometer
    •     On-chip temperature sensor
    •     Data is measured using on-chip ADCs and is transmitted over I²C or SPI interfaces

The UEVB may be used by itself utilizing SPI or I²C serial communications interfaces. Alternatively, it may be
connected to the InvenSense ARM Controller Board for connectivity to a host computer via USB interface.

The UEVB was designed to support up to 9-axis MPUs (Motion Processing Units) with a built-in compass (MPU-
91xx and MPU-92xx). Connecting an external compass board to the UEVB may require the user to connect their
third-party compass to the UEVB via its auxiliary I2C bus. The UEVB is populated with an external compass, and can
access the main or auxiliary I2C bus lines provided by the sensor (AUX_DA and AUX_CL) via resistor options.

The UEVB is lead-free and RoHS compliant.

RELATED DOCUMENTS
Please refer to the product specification of the main motion sensor for electrical characteristics, pinout and
applications details. Sensor product specifications can be found at www.invensense.com. For product specifications
for unreleased parts, please contact the InvenSense sales department at sales@invensense.com.




    InvenSense reserves the right to change the                   InvenSense Inc.
                                                   1745 Technology Drive, San Jose, CA 95110 U.S.A   Document Number: AN-IVS-0001EVB-00
     detail specifications as may be required to
                                                                 +1(408) 988–7339                    Rev Number: 1.3
      permit improvements in the design of its
                                                               www.invensense.com                    Rev Date: 02/24/2016
                       products.

<!-- page 2 -->

UEVB


TABLE OF CONTENTS
PURPOSE ..................................................................................................................................................... 1
   USAGE ...................................................................................................................................................... 1
   RELATED DOCUMENTS .......................................................................................................................... 1
UEVB OVERVIEW ........................................................................................................................................ 3
   TABLE 1A. PARTS FOR UEVB FOOTPRINTS ........................................................................................ 3
   TABLE 1B. RESISTOR OPTIONS ............................................................................................................ 5
   KEY FUNCTIONS AND PINOUTS ............................................................................................................ 7
   I2C/SPI BUS CONNECTIONS ................................................................................................................... 7
SCHEMATIC ................................................................................................................................................. 8
BILL OF MATERIAL (BOM) .......................................................................................................................... 9
   TABLE 2A. BILL OF MATERIAL FOR U1A (e.g. with MPU-92XX)........................................................... 9
   TABLE 2B. BILL OF MATERIAL FOR U1B (e.g. with ITG-35XX)............................................................. 9
   TABLE 2C. BILL OF MATERIAL FOR U1C (e.g. with ITG-1010) ........................................................... 10
   TABLE 2D. BILL OF MATERIAL FOR U1D, OPTION-A (e.g. with MPU-60XX)..................................... 10
   TABLE 2E. BILL OF MATERIAL FOR U1D, OPTION-B (e.g. with MPU-91XX) ..................................... 11
POWER SUPPLY CONNECTIONS............................................................................................................ 12
   TABLE 3. POWER SELECTION JUMPERS (JP1, JP2) ......................................................................... 12
UEVB CONNECTOR SIGNALS DESCRIPTION ........................................................................................ 13
   TABLE 4. USER INTERFACE CONNECTOR SIGNALS (CN1) ............................................................. 13
   CONNECTING THE FSYNC LINE .......................................................................................................... 14
   SERIAL BUS LEVELS, SPEEDS, AND TERMINATIONS ...................................................................... 14
DATA GATHERING OPTIONS ................................................................................................................... 15
   CONNECTION TO THE INVENSENSE ARM CONTROLLER BOARD ................................................. 15
   USE OF THE UEVB WITHOUT AN ARM CONTROLLER BOARD........................................................ 15
SPECIAL INSTRUCTIONS ......................................................................................................................... 16
   ELECTROSTATIC DISCHARGE SENSITIVITY ..................................................................................... 16
   BOARD LAYOUT AND FOOTPRINT DISCUSSION .............................................................................. 16
   REVISION HISTORY .............................................................................................................................. 18




Document Number: AN-IVS-0001EVB-00                                 Page 2 of 19
Rev Number: 1.3
Rev Date: 02/24/2017

<!-- page 3 -->

UEVB

UEVB OVERVIEW
The UEVB hosts most of InvenSense’s motion sensors and MPUs. To support a number of different products with
the UEVB, resistor options were implemented for easy and flexible circuit configurations. For example, Table 1a
shows the most popular parts that fit on the UEVB. Table 1b lists the resistor options for different configurations.

TABLE 1A. PARTS FOR UEVB FOOTPRINTS

    UEVB                  PART                                               PACKAGE TYPE               PIN
  IDENTIFIER             NUMBER        SENSOR TYPE               FEATURES    & DIMENSIONS              COUNT
                          ITG-3400        3-axis gyro                       QFN, 3 x 3 x 0.9 mm           24
                                          3- axis gyro,
                         MPU-5400                                           QFN, 3 x 3 x 0.9 mm           24
                                       2-axis accel (X, Y)
                         MPU-65xx     6-axis (accel, gyro)                  QFN, 3 x 3 x 0.9 mm           24
                         MPU-68xx     6-axis (accel, gyro)                   QFN, 3 x 3x 0.9 mm           24
                                      9-axis (accel, gyro,          AKM
                         MPU-92xx                                            QFN, 3 x 3 x 1 mm            24
                                           compass)               compass
       U1A
                         ICM-103xx       3-axis accel                       QFN, 3 x 3 x 0.9 mm           24
                          (Most of)
                                      6-axis (accel, gyro)                  QFN, 3 X 3 X 0.75 mm          24
                         ICM-206xx
                                      9-axis (accel, gyro,          AKM
                        ICM-209xx*                                            LGA, 3 x 3 x 1 mm           24
                                          compass)                compass
                          IDG-20xx     2-axis gyro (X, Y)           OIS     QFN, 3 x 3 x 0.75 mm          16
                          IXZ-20xx     2-axis gyro (X, Z)           OIS     QFN, 3 x 3 x 0.75 mm          16
                          IDG-25xx     2-axis gyro (X, Y)                   QFN, 3 x 3 x 0.9 mm           16
                          (Most of)
                                       2-axis gyro (X, Z)                   QFN, 3 x 3 x 0.9 mm           16
                           IXZ-25xx
                          ITG-35xx        3-axis gyro                       QFN, 3 x 3 x 0.9 mm           16
       U1B
                                                                            QFN, 3 x 3 x 0.9 mm
                          ITG-352x        3-axis gyro               OIS                                   16
                                                                            QFN, 3 x 3 x 0.75 mm
                          ITG-3701        3-axis gyro               OIS     QFN, 3 x 3 x 0.75 mm          16
                          ITG-358x        3-axis gyro             Custom    QFN, 3 x 3 x 0.9 mm           16
                          ITG-1010        3-axis gyro                       QFN, 3 x 3 x 0.9 mm           16
                          ISZ-2510      1-axis gyro (Z)                     QFN, 3 x 3 x 0.9 mm           16
                          IXZ-2510     2-axis gyro (X, Z)                   QFN, 3 x 3 x 0.9 mm           16
                         ICM-20608    6-axis (accel, gyro)                  QFN, 3 x 3 x 0.75 mm          16
       U1C               ICG-20660    6-axis (accel, gyro)                  QFN, 3 x 3 x 0.75 mm          16
                         IAM-20680    6-axis (accel,gyro)                   LGA, 3 X 3 X 0.75mm           16
                         IAM-20380       3-axis (accel)                     LGA, 3 X 3 X 0.75mm           16
                          IMU-30xx        3-axis gyro                       QFN, 4 x 4 x 0.9 mm           24
                         MPU-30xx         3-axis gyro                       QFN, 4 x 4 x 0.9 mm           24
                         MPU-33xx         3-axis gyro                       QFN, 4 x 4 x 0.9 mm           24
       U1D
                         MPU-60xx     6-axis (accel, gyro)                   QFN, 4x 4 x 0.9 mm           24
                         MPU-615x     6-axis (accel, gyro)                   QFN, 4 x 4 x 0.9mm           24




Document Number: AN-IVS-0001EVB-00                Page 3 of 19
Rev Number: 1.3
Rev Date: 02/24/2017

<!-- page 4 -->

UEVB
                                          9-axis (accel, gyro,
                         MPU-91xx                                     LGA, 4 x 4 x 1 mm    24
                                              compass)

* Future Product. Contact InvenSense Sales for availability.




Document Number: AN-IVS-0001EVB-00                     Page 4 of 19
Rev Number: 1.3
Rev Date: 02/24/2017

<!-- page 5 -->

UEVB
TABLE 1B. RESISTOR OPTIONS

                                                                             R18 = 1kΩ (or Open)
                                                 Functions as CS
                                                                                  R22 = 0 Ω
             𝐂𝐂𝐂𝐂/V_LOGIC Pin Resistor
             Option for All Footprints
                                                                                  R18 = 0 Ω
                                                   Functions as
                                                     V_LOGIC
                                                                                 R22 = Open

                                                                             R1, R3, R5, R7 = 0 Ω
                                                     Reserved
                                                                             R2, R4, R6, R8 = Open
                    U1A Resistor
                      Option
                                                                             R1, R3, R5, R7 = Open
                                          MPU-92xx and other QFN24,
                                             3 x 3 x 1 mm parts
                                                                             R2, R4, R6, R8 = 0 Ω


                                                                                 R19 = 10 kΩ
                                                  Pin 15 = High
                                                                                 R20 = Open
                    U1D Resistor
                      Option
                                                                                 R19 = Open
                                                   Pin 15 = Low
                                                                                 R20 = 10 kΩ

                                                                                R11, R13 = 0 Ω
                                                                   2
                                         Connects U2 to primary I C bus
                                                                               R12, R14 = Open
                     U2 Resistor
                       Option                                                  R11, R13 = Open
                                         Connects U2 to U1's auxiliary I2C
                                                bus (if available)
                                                                                R12, R14 = 0 Ω




Document Number: AN-IVS-0001EVB-00             Page 5 of 19
Rev Number: 1.3
Rev Date: 02/24/2017

<!-- page 6 -->

UEVB
There are four different footprints on the UEVB PCB (Figures 1A, 1B, 1C and 1D) to fit various motion sensors, but
only one may be populated at a time.

         24

              23

                    22

                            21

                                     20

                                              19




                                                                                         16

                                                                                                  15

                                                                                                            14

                                                                                                                      13
  1                                                18

  2                                                17                      1                                                    12

  3
                  U1A                              16                      2            U1B                                     11
              QFN/LGA24                                                    3
                                                                                    QFN/LGA16                                   10
  4                                                15
               3 x 3 mm                                                              3 x 3 mm
  5                                                14                      4                                                     9

  6                                                13
                               10

                                         11

                                              12
         7

               8

                       9




                                                                                         5

                                                                                                  6

                                                                                                            7

                                                                                                                      8
         Figure 1A: U1A (QFN/LGA24_3x3 mm)                                     Figure 1B: U1B (QFN/LGA16_3x3 mm)
                   16

                           15

                                    14




                                                                               24

                                                                                    23

                                                                                          22

                                                                                                   21

                                                                                                                 20

                                                                                                                           19
  1                                                13                  1                                                        18

  2                                                12                  2                                                        17

  3
                  U1C                              11                  3
                                                                                        U1D                                     16
              QFN/LGA16                                                             QFN/LGA24
  4                                                10                  4                                                        15
               3 x 3 mm                                                              4 x 4 mm
  5                                                9                   5                                                        14

                                                                       6                                                        13
                                                                                                       10

                                                                                                                 11

                                                                                                                           12
                   6

                           7

                                    8




                                                                               7

                                                                                    8

                                                                                              9




   Figure 1C: U1C (QFN/LGA16_3x3 mm)                                    Figure 1D: U1D (QFN/LGA24_4x4 mm)




The UEVB is populated with components only on its top side (Figure 2) to achieve ease of measurement access. A 10
x 2 connector (CN1) is designed to interface with the InvenSense ARM Controller Board, which is a host
microcontroller board useful for programming the registers of the sensor on the UEVB and accessing sensor data via
a PC or laptop through the USB port.

A 3-pin power selection header (JP1) is provided to choose the voltage level for VDD. Similarly, a 3-pin VDDIO
selection header (JP2) allows the user to select the power source for the board’s/sensor’s digital I/O voltage.




Document Number: AN-IVS-0001EVB-00                      Page 6 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 7 -->

UEVB

KEY FUNCTIONS AND PINOUTS

The motion sensing UEVB is a fully assembled and tested evaluation board, allowing for simple and swift
evaluation of the device’s X-/Y-/Z-axis angular rate gyroscope, X-/Y-/Z-axis accelerometer, and X-/Y-/Z-axis
compass. The motion sensing device has a primary interface to talk to the application processor and a secondary
interface that allows a user to communicate with an external sensor, such as a pressure sensor or compass.

The motion sensing device utilizes InvenSense’s proprietary MEMS technology with driven vibrating masses to
produce a functionally complete, low-cost motion sensor. The motion processing unit incorporates X-/Y-/Z-axis
low-pass filters and an EEPROM for on-chip factory calibration of the sensor. Factory-trimmed scale factors
eliminate the need for external active components and end-user calibration. A built-in Proportional-To-Absolute-
Temperature (PTAT) sensor provides temperature compensation information. Refer to the product specification
document for each sensor to obtain more details on specific sensor features.



I2C/SPI BUS CONNECTIONS

The UEVB communicates with a system processor (e.g. InvenSense ARM controller board) through the custom
header using either the I²C or the SPI serial interface. The device always acts as a slave when communicating with
the system processor.




                                     Figure 2. Top Side of the UEVB (e.g. MPU-65xx)




Document Number: AN-IVS-0001EVB-00                     Page 7 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 8 -->

UEVB

SCHEMATIC




                                               Figure 3. UEVB Circuit Schematic



Document Number: AN-IVS-0001EVB-00   Page 8 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 9 -->

UEVB

BILL OF MATERIAL (BOM)
The UEVB offers five different BOMs, which cover most of InvenSense’s sensor (Tables 2A, 2B, 2C, 2D, and 2E.)
There are two BOM versions for U1D, and one each one for U1A, U1B and U1C.

TABLE 2A. BILL OF MATERIAL FOR U1A (e.g. with MPU-92XX)

 ITEM          QUANTITY                         REFERENCE                              PART             PCB FOOTPRINT
                                                                                 Header 10 x 2, M,
   1                 1         CN1                                                                        HDB2X14NRA
                                                                                90D, 2.54 x 2.54 mm
                               C1, C2, C3, C4, C5, C6, C7, C8, C9, C11, C12,
   2                16                                                                   0.1 µF                 C0402
                               C13, C14, C18, C19, C20
   3                 1         C10                                                      2200 pF                 C0402
   4                 2         C15, C17                                                2.2 µF                   C0402
   5                 1         C16                                                    0.033 µF                  C0402
                                                                                3-Pin Header, 2.54 x
   7                 2         JP1, JP2                                                                         SIP-3P
                                                                                  2.54 mm, Male
   9                 8         R9, R10, R15, R19, R21, R23, R24, R25                   10 kΩ                    R0402
  10                 7         R1, R3, R5, R7, R11, R13, R22                              0Ω                    R0402
  11                 1         R18                                                        1 kΩ              R0402
  13                 1         U1A                                                      MPU-92xx        QFN24_3x3 mm
  17                 1         U2                                                       AK8963C         BGA14_2X2 mm
  18                 1         U4                                                XC6210B302MR-G                 SOT25


TABLE 2B. BILL OF MATERIAL FOR U1B (e.g. with ITG-35XX)

 ITEM          QUANTITY                        REFERENCE                                PART            PCB FOOTPRINT
                                                                               Header 10x2, M, 90D,
   1                 1         CN1                                                                     HDB2X14NRA
                                                                               2.54 x 2.54 mm
                               C1, C2, C3, C4, C5, C6, C7, C8, C9, C11,
   2                16                                                         0.1 µF                  C0402
                               C12, C13, C14, C18, C19, C20
   3                 1         C10                                             2200 pF                 C0402
   4                 2         C15, C17                                        2.2 µF                  C0402
   5                 1         C16                                             0.033 µF                C0402
                                                                               3-Pin Header, 2.54 x
   7                 2         JP1, JP2                                                                SIP-3P
                                                                               2.54 mm, Male
   9                 8         R9, R10, R15, R19, R21, R23, R24, R25           10 kΩ                   R0402
  10                 3         R11, R13, R22                                   0Ω                      R0402
  11                 1         R18                                             1 kΩ                    R0402
                                                                                                       QFN16_3X3
  14                 1         U1B                                             ITG-35xx
                                                                                                       (0.5 Pitch)A
                                                                                                       BGA14_2X2
  17                 1         U2                                              AK8963C
                                                                                                       (0.4 Pitch)
  18                 1         U4                                              XC6210B302MR-G          SOT25




Document Number: AN-IVS-0001EVB-00                        Page 9 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 10 -->

UEVB

    TABLE 2C. BILL OF MATERIAL FOR U1C (e.g. with ITG-1010)

      ITEM           QUANTITY                       REFERENCE                         PART             PCB FOOTPRINT
                                                                             Header 10x2, M, 90D,
1                    1               CN1                                                            HDB2X14NRA
                                                                             2.54 x 2.54 mm
                                     C1,C2,C3,C4,C5,C6,C7,C8,C9,C11,
2                    16                                                      0.1 µF                 C0402
                                     C12,C13,C14,C18,C19,C20
3                    1               C10                                     2200 pF                C0402
4                    2               C15,C17                                 2.2 µF                 C0402
5                    1               C16                                     0.033 µF               C0402
                                                                             3-Pin Header, 2.54 x
7                    2               JP1,JP2                                                        SIP-3P
                                                                             2.54 mm, Male
9                    8               R9,R10,R15,R19,R21,R23,R24,R25          10 kΩ                  R0402
10                   3               R11,R13,R22                             0Ω                     R0402
11                   1               R18                                     1 kΩ                   R0402
                                                                                                    QFN16_IT36_3X3
15                   1               U1C                                     ITG-1010
                                                                                                    (0.5PITCH)A
                                                                                                    BGA14_2X2
17                   1               U2                                      AK8963C
                                                                                                    (0.4PITCH)
18                   1               U4                                      YB1210ST25R300         SOT235


    TABLE 2D. BILL OF MATERIAL FOR U1D, OPTION-A (e.g. with MPU-60XX)

    ITEM          QUANTITY                         REFERENCE                          PART            PCB FOOTPRINT
                                                                             Header 10x2, M, 90D,
       1                  1       CN1                                                               HDB2X14NRA
                                                                             2.54 x 2.54 mm
                                  C1, C2, C3, C4, C5, C6, C7, C8, C9, C11,
       2                 16                                                  0.1 µF                 C0402
                                  C12, C13, C14, C18, C19, C20
       3                  1       C10                                        2200 pF                C0402
       4                  2       C15, C17                                   2.2 µF                 C0402
       5                  1       C16                                        0.033 µF               C0402
                                                                             3-Pin Header, 2.54 x
       7                  2       JP1, JP2                                                          SIP-3P
                                                                             2.54 mm, Male
       9                  8       R9, R10, R15, R19, R21, R23, R24, R25      10 kΩ                  R0402
      10                  3       R11, R13, R22                              0Ω                     R0402
      11                  1       R18                                        1 kΩ                   R0402
      16                  1       U1D                                        MPU-60xx               QFN24_4X4(0.5 Pitch)
      17                  1       U2                                         AK8963C                BGA14_2X2(0.4Pitch)
      18                  1       U4                                         XC6210B302MR-G         SOT25




    Document Number: AN-IVS-0001EVB-00                       Page 10 of 19
    Rev Number: 1.2
    Rev Date: 11/07/2014

<!-- page 11 -->

UEVB

TABLE 2E. BILL OF MATERIAL FOR U1D, OPTION-B (e.g. with MPU-91XX)

ITEM          QUANTITY                        REFERENCE                           PART            PCB FOOTPRINT
                                                                         Header 10x2, M, 90D,
   1                1         CN1                                                               HDB2X14NRA
                                                                         2.54 x 2.54 mm
                              C1, C2, C3, C4, C5, C6, C7, C8, C9, C11,
   2               16                                                    0.1 µF                 C0402
                              C12, C13, C14, C18, C19, C20
   3                1         C10                                        2200 pF                C0402
   4                2         C15, C17                                   2.2 µF                 C0402
   5                1         C16                                        0.033 µF               C0402
                                                                         3-Pin Header, 2.54 x
   7                2         JP1, JP2                                                          SIP-3P
                                                                         2.54 mm, Male
   9                6         R9, R10, R15, R21, R24, R25                10 kΩ                  R0402
  10                5         R11, R13, R20, R22, R23                    0Ω                     R0402
  11                1         R18                                        1 kΩ                   R0402
  16                1         U1D                                        MPU-91xx               QFN24_4X4(0.5 Pitch)
  17                1         U2                                         AK8963C                BGA14_2X2(0.4 Pitch)
  18                1         U4                                         XC6210B302MR-G         SOT25




Document Number: AN-IVS-0001EVB-00                       Page 11 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 12 -->

UEVB

POWER SUPPLY CONNECTIONS
JP1 and JP2 are 3-pin headers, which allow the user to select between an on-board LDO (Low-Voltage Dropout
Regulator, U4) and an external DC supply (VIN) to power the motion sensor. For details, please refer to Table 3.

TABLE 3. POWER SELECTION JUMPERS (JP1, JP2)

         JP1 PIN NUMBER              SIGNAL DESCRIPTION
           1-2 Shunted               VDD = 3V (from LDO, VIN > 3.1V, net name 3V0)
           2-3 Shunted               VDD = VIN (from an external source)
         JP2 PIN NUMBER              SIGNAL DESCRIPTION
           1-2 Shunted               VDDIO = VDD
           2-3 Shunted               VDDIO = 1.8V (from an external source, net name 1V8)


The on-board low-noise 3V LDO offers an output that is called 3V0 (Figure 3). Using this will ensure that the sensor
performance will meet data sheet specifications.

Selecting VIN to power the chip/board is generally done while designing and evaluating an embedded platform,
where the host processor and related electronics need full control over the motion processing chipset’s power
supply.

If a user intends to use the on-board 3V power source, an external VIN must be provided within the range of
3.1~6.0V to ensure the LDO works properly.

If the user provides a VIN power level of ≥3.6V, JP1 and JP2 must be shunted across pins 1-2, since the motion
sensors’ VDD and VDDIO operational ranges are ≤3.6V.




Document Number: AN-IVS-0001EVB-00                     Page 12 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 13 -->

UEVB

UEVB CONNECTOR SIGNALS DESCRIPTION
TABLE 4. USER INTERFACE CONNECTOR SIGNALS (CN1)

    CN1 PIN
   NUMBER              CN1 SIGNAL NAME                          SIGNAL DESCRIPTION
                                                                  2
         1                  AUX_DA       AUX_DA. Auxiliary I C serial data signal.
   2, 4, 9, 12,
   14, 16, 19,
                                N.C.     N.C. Do not connect to these pins.
   25, 26, 27,
       28
        3                     AUX_CL     AUX_CL. Auxiliary I2C serial clock signal.

                                         1V8 Power. Receive power from InvenSense ARM controller board or
        5                       1V8
                                         an external source.

        6                      DRDY      DRDY. Data ready and FIFO interrupt signals.

        7                       INT      INT. Interrupt output signal to controller.

        8                        CS      Test Signal. Not used in I2C mode; used as chip-select pin in SPI mode.

       10                   DRDY-CMP     Compass (U2) DRDY. Compass data ready signal.

       11                       TP0      Test Signal

       13                       VPP      Test Signal

     15, 17                    GND       GND. Ground connection.

       18                    REGOUT      REGOUT. Sensor’s on-chip regulator output.

       20                    SCL_SCLK    SCL/SCLK. I2C or SPI primary serial clock signal.

       21                     FSYNC      FSYNC. Frame synchronization input for camera applications.
       22                    SDA_SDI     SDA/MOSI. I²C primary data or SPI MOSI signal.
                                         Power. Receive power from InvenSense ARM controller board or an
       23                       VIN
                                         external source.
                                         AD0/MISO. Lowest (LSB) address bit in I2C mode or SPI MISO signal in
       24                   AD0_SDO
                                         SPI mode.




Document Number: AN-IVS-0001EVB-00                Page 13 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 14 -->

UEVB
CONNECTING THE FSYNC LINE
The FSYNC line is intended for use in a camera’s image-stabilization system. It is an input from the camera platform
to the UEVB, and is intended to synchronize the motion-sensor serial-bus transfer with the master timing set by
the camera system.

SERIAL BUS LEVELS, SPEEDS, AND TERMINATIONS
The UEVB supports I²C communications up to 400 kHz, or SPI communications up to 1MHz clock rates for writing.
In SPI mode, it can be operated at up to 20 MHz for reading. The I²C bus open-drain pull-up resistors (10 kΩ) are
connected to VDDIO.




Document Number: AN-IVS-0001EVB-00                  Page 14 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 15 -->

UEVB

DATA GATHERING OPTIONS
The motion sensor’s digital sensor data is available on the UEVB’s header CN1. Alternatively, for connectivity with
a host PC, an InvenSense ARM controller board may be used.

CONNECTION TO THE INVENSENSE ARM CONTROLLER BOARD
For communications via USB with a host computer, the UEVB can be connected to the InvenSense ARM controller
board. InvenSense provides a software tool to support the collection of sensor data through the UEVB/ARM
controller board combo connected to a PC/laptop via a USB port. Please refer to the InvenSense Data Logger (IDL)
Application Notes document for additional instructions on how to use the software to obtain sensor data. This
information can be provided by your local field team on an as-needed basis.

Figure 4 shows the connection of the UEVB to the InvenSense ARM controller board. Connections between the two
boards are made via header CN1 on the UEVB and connector JP6 on the InvenSense ARM Controller Board.




                            Figure 4. UEVB connected to the InvenSense ARM Controller Board



USE OF THE UEVB WITHOUT AN ARM CONTROLLER BOARD
I²C and SPI signals are made available on header CN1. Users may develop their own tools to communicate with the
UEVB as there is no bus mode selection setting required.




Document Number: AN-IVS-0001EVB-00                    Page 15 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 16 -->

UEVB
SPECIAL INSTRUCTIONS
ELECTROSTATIC DISCHARGE SENSITIVITY
The motion sensors can be permanently damaged by electrostatic discharge (ESD). ESD precautions for handling
and storage must be taken to avoid damage to the devices.

BOARD LAYOUT AND FOOTPRINT DISCUSSION
The UEVB is a 4-layer FR-4 PCB design with the dimensions: 38.1 x 38.1 x 1.6 mm (1500 x 1500 x 62 mil). See Figure
5 and Figure 6 for a detailed top and bottom view of the UEVB.

The MPU footprint on the UEVB supports both QFN and LGA packages. Footprints and sensor land patterns were
chosen large enough, so they offer ease of use, reliable contact with the sensor, hand-solder and debugging
capabilities for both packages.

Note that to avoid potential shorting/clearance issues at the corner pins for LGA packages, the land pattern shapes
for the individual pins in this design were chosen to be oblong rather than square. The dimensions for the pin pads
are 0.225 x 0.7 mm.

Solder mask (also called solder resist is a layer of protective coating for PCB’s copper traces, which helps to prevent
undesired solder bridges and shorts) dimensions will not be provided as they are dependent upon the manufacturing
process and the clearance capabilities of the chosen fabrication house. Contact your PCB vendor to determine the
minimum required clearance between pin pads (usually 4 mil to 6 mil or 0.102 mm to 0.152 mm) and traces allowing
them enough room to print an adequate solder mask.




Document Number: AN-IVS-0001EVB-00                    Page 16 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 17 -->

UEVB




                            Figure 5 & Figure 6.Top & Bottom View of the UEVB Board Layout




Document Number: AN-IVS-0001EVB-00                    Page 17 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 18 -->

UEVB
REVISION HISTORY
                   DATE              REVISION                    DESCRIPTION
                  1/22/14               1.0          Initial Release
                  1/31/14               1.1          Updated parts list and BOM tables.
                                                     Updated parts list, corrected text
                                                     and updated references to existing
                  11/7/14                1.2
                                                     documentation listed in this user
                                                     guide.
                 02/24/17                1.3         Update parts list




Document Number: AN-IVS-0001EVB-00   Page 18 of 19
Rev Number: 1.2
Rev Date: 11/07/2014

<!-- page 19 -->

UEVB




This information furnished by InvenSense is believed to be accurate and reliable. However, no responsibility is assumed by InvenSense for its
use, or for any infringements of patents or other rights of third parties that may result from its use. Specifications are subject to change without
notice. InvenSense reserves the right to make changes to this product, including its circuits and software, in order to improve its design and/or
performance, without prior notice. InvenSense makes no warranties, neither expressed nor implied, regarding the information and
specifications contained in this document. InvenSense assumes no responsibility for any claims or damages arising from information contained
in this document, or from the use of products and services detailed therein. This includes, but is not limited to, claims or damages based on the
infringement of patents, copyrights, mask work and/or other intellectual property rights.

Certain intellectual property owned by InvenSense and described in this document is patent protected. No license is granted by implication or
otherwise under any patent or patent rights of InvenSense. This publication supersedes and replaces all information previously supplied.
Trademarks that are registered trademarks are the property of their respective companies. InvenSense sensors should not be used or sold in
the development, storage, production or utilization of any conventional or mass-destructive weapons or for any other weapons or life
threatening applications, as well as in any other life critical applications such as medical equipment, transportation, aerospace and nuclear
instruments, undersea equipment, power plant equipment, disaster prevention and crime prevention equipment.

©2014 InvenSense, Inc. All rights reserved. InvenSense, MotionTracking, MotionProcessing, MotionProcessor, MotionFusion, MotionApps,
DMP, AAR, and the InvenSense logo are trademarks of InvenSense, Inc. Other company and product names may be trademarks of the
respective companies with which they are associated.
.




                                                    ©2014 InvenSense, Inc. All rights reserved.




Document Number: AN-IVS-0001EVB-00                                 Page 19 of 19
Rev Number: 1.2
Rev Date: 11/07/2014