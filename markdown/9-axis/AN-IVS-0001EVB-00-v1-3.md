# AN-IVS-0001EVB-00-v1-3

*Source: `original/9-axis/AN-IVS-0001EVB-00-v1-3.pdf` (19 pages)*

<!-- page 1 -->

**_Application Note_** 

# InvenSense Motion Sensor Universal Evaluation Board (UEVB) User Guide 



## **_<mark>PURPOSE</mark>_** 

This document describes the hardware and circuitry on the Universal Evaluation Board (UEVB). The UEVB is used to evaluate most of InvenSense’s current motion sensing (gyroscopes, accelerometers, magnetometers) products. It covers applying the UEVB to a larger system, and requires the understanding of key signals and circuit functions, hardware jumper settings, and port connections. 

### **USAGE** 

This UEVB provides up to nine axes of motion sensing comprised of: 

- Digital-output of 3-axis gyroscope with user-programmable full-scale ranges 

- Digital-output of 3-axis accelerometer with user-programmable full-scale ranges 

- Digital-output of 3-axis magnetometer 

- On-chip temperature sensor 

- Data is measured using on-chip ADCs and is transmitted over I²C or SPI interfaces 

The UEVB may be used by itself utilizing SPI or I²C serial communications interfaces. Alternatively, it may be connected to the InvenSense ARM Controller Board for connectivity to a host computer via USB interface. 

The UEVB was designed to support up to 9-axis MPUs (Motion Processing Units) with a built-in compass (MPU91xx and MPU-92xx). Connecting an external compass board to the UEVB may require the user to connect their third-party compass to the UEVB via its auxiliary I<sup>2</sup> C bus. The UEVB is populated with an external compass, and can access the main or auxiliary I<sup>2</sup> C bus lines provided by the sensor (AUX_DA and AUX_CL) via resistor options. 

The UEVB is lead-free and RoHS compliant. 

### **RELATED DOCUMENTS** 

Please refer to the product specification of the main motion sensor for electrical characteristics, pinout and applications details. Sensor product specifications can be found at <u>www.invensense.com. For product specifications</u> for unreleased parts, please contact the InvenSense sales department at sales@invensense.com. 

**InvenSense Inc.** 

InvenSense reserves the right to change the detail specifications as may be required to permit improvements in the design of its products. 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.3 

1745 Technology Drive, San Jose, CA 95110 U.S.A +1(408) 988–7339 www.invensense.com 

Rev Date: 02/24/2016 



<!-- page 2 -->

**_UEVB_** 

|**_TABLE OF CONTENTS_**|
|---|
|PURPOSE ..................................................................................................................................................... 1|
|USAGE ...................................................................................................................................................... 1|
|RELATED DOCUMENTS .......................................................................................................................... 1|
|UEVB OVERVIEW ........................................................................................................................................ 3|
|TABLE 1A. PARTS FOR UEVB FOOTPRINTS ........................................................................................ 3|
|TABLE 1B. RESISTOR OPTIONS ............................................................................................................ 5|
|KEY FUNCTIONS AND PINOUTS ............................................................................................................ 7|
|I<sup>2</sup>C/SPI BUS CONNECTIONS ................................................................................................................... 7|
|SCHEMATIC ................................................................................................................................................. 8|
|BILL OF MATERIAL (BOM) .......................................................................................................................... 9|
|TABLE 2A. BILL OF MATERIAL FOR U1A (e.g. with MPU-92XX) ........................................................... 9|
|TABLE 2B. BILL OF MATERIAL FOR U1B (e.g. with ITG-35XX) ............................................................. 9|
|TABLE 2C. BILL OF MATERIAL FOR U1C (e.g. with ITG-1010) ........................................................... 10|
|TABLE 2D. BILL OF MATERIAL FOR U1D, OPTION-A (e.g. with MPU-60XX) ..................................... 10|
|TABLE 2E. BILL OF MATERIAL FOR U1D, OPTION-B (e.g. with MPU-91XX) ..................................... 11|
|POWER SUPPLY CONNECTIONS ............................................................................................................ 12|
|TABLE 3. POWER SELECTION JUMPERS (JP1, JP2) ......................................................................... 12|
|UEVB CONNECTOR SIGNALS DESCRIPTION ........................................................................................ 13|
|TABLE 4. USER INTERFACE CONNECTOR SIGNALS (CN1) ............................................................. 13|
|CONNECTING THE FSYNC LINE .......................................................................................................... 14|
|SERIAL BUS LEVELS, SPEEDS, AND TERMINATIONS ...................................................................... 14|
|DATA GATHERING OPTIONS ................................................................................................................... 15|
|CONNECTION TO THE INVENSENSE ARM CONTROLLER BOARD ................................................. 15|
|USE OF THE UEVB WITHOUT AN ARM CONTROLLER BOARD ........................................................ 15|
|SPECIAL INSTRUCTIONS ......................................................................................................................... 16|
|ELECTROSTATIC DISCHARGE SENSITIVITY ..................................................................................... 16|
|BOARD LAYOUT AND FOOTPRINT DISCUSSION .............................................................................. 16|
|REVISION HISTORY .............................................................................................................................. 18|



Page 2 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.3 Rev Date: 02/24/2017 



<!-- page 3 -->

**_UEVB_** 

## **_UEVB OVERVIEW_** 

The UEVB hosts most of InvenSense’s motion sensors and MPUs. To support a number of different products with the UEVB, resistor options were implemented for easy and flexible circuit configurations. For example, Table 1a shows the most popular parts that fit on the UEVB. Table 1b lists the resistor options for different configurations. 

### **TABLE 1A. PARTS FOR UEVB FOOTPRINTS** 

|**UEVB**<br>**IDENTIFIER**|**PART**<br>**NUMBER**|**SENSOR TYPE**|**FEATURES**|**PACKAGE TYPE**<br>**& DIMENSIONS**|**PIN**<br>**COUNT**|
|---|---|---|---|---|---|
||ITG-3400|3-axisgyro||QFN, 3 x 3 x 0.9 mm|24|
||MPU-5400|3- axis gyro,<br>2-axis accel(X,Y)||QFN, 3 x 3 x 0.9 mm|24|
||MPU-65xx|6-axis (accel,gyro)||QFN, 3 x 3 x 0.9 mm|24|
||MPU-68xx|6-axis (accel,gyro)||QFN, 3 x 3x 0.9 mm|24|
|**U1A**|MPU-92xx|9-axis (accel, gyro,<br>compass)|AKM<br>compass|QFN, 3 x 3 x 1 mm|24|
||ICM-103xx|3-axis accel||QFN, 3 x 3 x 0.9 mm|24|
||(Most of)<br>ICM-206xx|6-axis (accel, gyro)||QFN, 3 X 3 X 0.75 mm|24|
||ICM-209xx*|9-axis (accel, gyro,<br>compass)|AKM<br>compass|LGA, 3 x 3 x 1 mm|24|
||IDG-20xx|2-axis gyro (X, Y)|OIS|QFN, 3 x 3 x 0.75 mm|16|
||IXZ-20xx|2-axisgyro (X, Z)|OIS|QFN, 3 x 3 x 0.75 mm|16|
||IDG-25xx|2-axisgyro (X, Y)||QFN, 3 x 3 x 0.9 mm|16|
||(Most of)<br>IXZ-25xx|2-axis gyro (X, Z)||QFN, 3 x 3 x 0.9 mm|16|
|**U1B**|ITG-35xx|3-axisgyro||QFN, 3 x 3 x 0.9 mm|16|
||ITG-352x|3-axis gyro|OIS|QFN, 3 x 3 x 0.9 mm<br>QFN,3 x 3 x 0.75 mm|16|
||ITG-3701|3-axisgyro|OIS|QFN, 3 x 3 x 0.75 mm|16|
||ITG-358x|3-axisgyro|Custom|QFN, 3 x 3 x 0.9 mm|16|
||ITG-1010|3-axisgyro||QFN, 3 x 3 x 0.9 mm|16|
||ISZ-2510|1-axisgyro (Z)||QFN, 3 x 3 x 0.9 mm|16|
||IXZ-2510|2-axisgyro (X, Z)||QFN, 3 x 3 x 0.9 mm|16|
||ICM-20608|6-axis (accel,gyro)||QFN, 3 x 3 x 0.75 mm|16|
|**U1C**|ICG-20660|6-axis(accel,gyro)||QFN, 3 x 3 x 0.75 mm|16|
||IAM-20680|6-axis (accel,gyro)||LGA, 3 X 3 X 0.75mm|16|
||IAM-20380|3-axis (accel)||LGA, 3 X 3 X 0.75mm|16|
||IMU-30xx|3-axisgyro||QFN, 4 x 4 x 0.9 mm|24|
||MPU-30xx|3-axisgyro||QFN, 4 x 4 x 0.9 mm|24|
|**U1D**|MPU-33xx|3-axisgyro||QFN, 4 x 4 x 0.9 mm|24|
||MPU-60xx|6-axis (accel,gyro)||QFN, 4x 4 x 0.9 mm|24|
||MPU-615x|6-axis (accel,gyro)||QFN, 4 x 4 x 0.9mm|24|



Page 3 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.3 Rev Date: 02/24/2017 



<!-- page 4 -->

**_UEVB_** 



|MPU-91xx|9-axis (accel, gyro,<br>compass)|LGA, 4 x 4 x 1 mm|24|
|---|---|---|---|



_* Future Product. Contact InvenSense Sales for availability._ 

Page 4 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.3 Rev Date: 02/24/2017 



<!-- page 5 -->

**_UEVB_** 

### **TABLE 1B. RESISTOR OPTIONS** 

|||R18 = 1kΩ (or Open)|
|---|---|---|
||Functions asCS||
|𝐂<br>**/V_LOGIC Pin Resistor**||R22 = 0 Ω|
|**Option for All  Footprints**|Functions as|R18 = 0 Ω|
||V_LOGIC|R22 = Open|
||Reserved|R1, R3, R5, R7 = 0 Ω|
|**U1A Resistor**||R2, R4, R6, R8 = Open|
|**Option**|MPU-92xx and other QFN24,|R1, R3, R5, R7 = Open|
||3 x 3 x 1 mm parts|R2, R4, R6, R8 = 0 Ω|
||i 1  ih|R19 = 10 kΩ|
|**U1D Resistor**|Pn 5 = Hg|R20 = Open|
|**Option**||R19 = Open|
||Pin 15 = Low|R20 = 10 kΩ|
||Ct U2 t i I<sup>2</sup>C b|R11, R13 = 0 Ω|
|**i**|onnecs  o prmaryus|R12, R14 = Open|
|**U2 Resstor**<br>**Option**|Connects U2 to U1's auxiliary I<sup>2</sup>C|R11, R13 = Open|
||bus (if available)|R12, R14 = 0 Ω|



Page 5 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.3 Rev Date: 02/24/2017 



<!-- page 6 -->

**_UEVB_** 

There are four different footprints on the UEVB PCB (Figures 1A, 1B, 1C and 1D) to fit various motion sensors, but only one may be populated at a time. 



<!-- Start of picture text -->
1 18<br>2 17<br>U1A<br>3 16<br>QFN/LGA24<br>4 15<br>3 x 3 mm<br>5 14<br>6 13<br>24 23 22 21 20 19<br>7 8 9 10 11 12<br><!-- End of picture text -->



<!-- Start of picture text -->
1 12<br>U1B<br>2 11<br>QFN/LGA16<br>3 10<br>3 x 3 mm<br>4 9<br>16 15 14 13<br>5 6 7 8<br><!-- End of picture text -->

**Figure 1A: U1A (QFN/LGA24_3x3 mm)** 

**Figure 1B: U1B (QFN/LGA16_3x3 mm)** 



<!-- Start of picture text -->
1 13<br>2 12<br>U1C<br>3 11<br>QFN/LGA16<br>4 10<br>3 x 3 mm<br>5 9<br>16 15 14<br>6 7 8<br><!-- End of picture text -->



<!-- Start of picture text -->
1 18<br>2 17<br>U1D<br>3 16<br>QFN/LGA24<br>4 15<br>4 x 4 mm<br>5 14<br>6 13<br>24 23 22 21 20 19<br>7 8 9 10 11 12<br><!-- End of picture text -->

**Figure 1C: U1C (QFN/LGA16_3x3 mm)** 

**Figure 1D: U1D (QFN/LGA24_4x4 mm)** 

The UEVB is populated with components only on its top side (Figure 2) to achieve ease of measurement access. A 10 x 2 connector (CN1) is designed to interface with the InvenSense ARM Controller Board, which is a host microcontroller board useful for programming the registers of the sensor on the UEVB and accessing sensor data via a PC or laptop through the USB port. 

A 3-pin power selection header (JP1) is provided to choose the voltage level for VDD. Similarly, a 3-pin VDDIO selection header (JP2) allows the user to select the power source for the board’s/sensor’s digital I/O voltage. 

Page 6 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 7 -->

**_UEVB_** 

## **KEY FUNCTIONS AND PINOUTS** 

The motion sensing UEVB is a fully assembled and tested evaluation board, allowing for simple and swift evaluation of the device’s X-/Y-/Z-axis angular rate gyroscope, X-/Y-/Z-axis accelerometer, and X-/Y-/Z-axis compass. The motion sensing device has a primary interface to talk to the application processor and a secondary interface that allows a user to communicate with an external sensor, such as a pressure sensor or compass. 

The motion sensing device utilizes InvenSense’s proprietary MEMS technology with driven vibrating masses to produce a functionally complete, low-cost motion sensor.  The motion processing unit incorporates X-/Y-/Z-axis low-pass filters and an EEPROM for on-chip factory calibration of the sensor.  Factory-trimmed scale factors eliminate the need for external active components and end-user calibration.  A built-in Proportional-To-AbsoluteTemperature (PTAT) sensor provides temperature compensation information. Refer to the product specification document for each sensor to obtain more details on specific sensor features. 

## **I**<sup>**2**</sup> **C/SPI BUS CONNECTIONS** 

The UEVB communicates with a system processor (e.g. InvenSense ARM controller board) through the custom header using either the I²C or the SPI serial interface. The device always acts as a slave when communicating with the system processor. 



**Figure 2. Top Side of the UEVB (e.g. MPU-65xx)** 

Page 7 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 8 -->

**_UEVB_** 

# **_SCHEMATIC_** 



Figure 3. UEVB Circuit Schematic 

Page 8 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 9 -->

**_UEVB_** 

# **_BILL OF MATERIAL (BOM)_** 

The UEVB offers five different BOMs, which cover most of InvenSense’s sensor (Tables 2A, 2B, 2C, 2D, and 2E.) There are two BOM versions for U1D, and one each one for U1A, U1B and U1C. 

**TABLE 2A. BILL OF MATERIAL FOR U1A (e.g. with MPU-92XX)** 

|**ITEM**|**QUANTITY**|**REFERENCE**|**PART**|**PCB FOOTPRINT**|
|---|---|---|---|---|
|1|1|CN1|Header 10 x 2, M,<br>90D,2.54 x 2.54 mm|HDB2X14NRA|
|2|16|C1, C2, C3, C4, C5, C6, C7, C8, C9, C11, C12,<br>C13,C14,C18,C19,C20|0.1 µF|C0402|
|3|1|C10|2200pF|C0402|
|4|2|C15, C17|2.2µF|C0402|
|5|1|C16|0.033µF|C0402|
|7|2|JP1, JP2|3-Pin Header, 2.54 x<br>2.54 mm,Male|SIP-3P|
|9|8|R9, R10, R15, R19, R21, R23, R24, R25|10 kΩ|R0402|
|10|7|R1, R3, R5, R7, R11, R13, R22|0 Ω|R0402|
|11|1|R18|1 kΩ|R0402|
|13|1|U1A|MPU-92xx|QFN24_3x3 mm|
|17|1|U2|AK8963C|BGA14_2X2 mm|
|18|1|U4|XC6210B302MR-G|SOT25|



**TABLE 2B. BILL OF MATERIAL FOR U1B (e.g. with ITG-35XX)** 

|**ITEM**|**QUANTITY**|**REFERENCE**|**PART**|**PCB FOOTPRINT**|
|---|---|---|---|---|
|1|1|CN1|Header 10x2, M, 90D,<br>2.54 x 2.54 mm|HDB2X14NRA|
|2|16|C1, C2, C3, C4, C5, C6, C7, C8, C9, C11,<br>C12,C13,C14,C18,C19,C20|0.1 µF|C0402|
|3|1|C10|2200pF|C0402|
|4|2|C15, C17|2.2µF|C0402|
|5|1|C16|0.033µF|C0402|
|7|2|JP1, JP2|3-Pin Header, 2.54 x<br>2.54 mm,Male|SIP-3P|
|9|8|R9, R10, R15, R19, R21, R23, R24, R25|10 kΩ|R0402|
|10|3|R11, R13, R22|0 Ω|R0402|
|11|1|R18|1 kΩ|R0402|
|14|1|U1B|ITG-35xx|QFN16_3X3<br>(0.5 Pitch)A|
|17|1|U2|AK8963C|BGA14_2X2<br>(0.4 Pitch)|
|18|1|U4|XC6210B302MR-G|SOT25|



Page 9 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 10 -->

**_UEVB_** 

**TABLE 2C. BILL OF MATERIAL FOR U1C (e.g. with ITG-1010)** 

|**ITEM**|**QUANTITY**|**REFERENCE**|**PART**|**PCB FOOTPRINT**|
|---|---|---|---|---|
|1|1|CN1|Header 10x2, M, 90D,<br>2.54 x 2.54 mm|HDB2X14NRA|
|2|16|C1,C2,C3,C4,C5,C6,C7,C8,C9,C11,<br>C12,C13,C14,C18,C19,C20|0.1 µF|C0402|
|3|1|C10|2200 pF|C0402|
|4|2|C15,C17|2.2 µF|C0402|
|5|1|C16|0.033 µF|C0402|
|7|2|JP1,JP2|3-Pin Header, 2.54 x<br>2.54 mm,Male|SIP-3P|
|9|8|R9,R10,R15,R19,R21,R23,R24,R25|10 kΩ|R0402|
|10|3|R11,R13,R22|0 Ω|R0402|
|11|1|R18|1 kΩ|R0402|
|15|1|U1C|ITG-1010|QFN16_IT36_3X3<br>(0.5PITCH)A|
|17|1|U2|AK8963C|BGA14_2X2<br>(0.4PITCH)|
|18|1|U4|YB1210ST25R300|SOT235|



**TABLE 2D. BILL OF MATERIAL FOR U1D, OPTION-A (e.g. with MPU-60XX)** 

|**ITEM**|**QUANTITY**|**REFERENCE**|**PART**|**PCB FOOTPRINT**|
|---|---|---|---|---|
|1|1|CN1|Header 10x2, M, 90D,<br>2.54 x 2.54 mm|HDB2X14NRA|
|2|16|C1, C2, C3, C4, C5, C6, C7, C8, C9, C11,<br>C12,C13,C14,C18,C19,C20|0.1 µF|C0402|
|3|1|C10|2200pF|C0402|
|4|2|C15, C17|2.2µF|C0402|
|5|1|C16|0.033µF|C0402|
|7|2|JP1,  JP2|3-Pin Header, 2.54 x<br>2.54 mm,Male|SIP-3P|
|9|8|R9, R10, R15, R19, R21, R23, R24, R25|10 kΩ|R0402|
|10|3|R11, R13, R22|0 Ω|R0402|
|11|1|R18|1 kΩ|R0402|
|16|1|U1D|MPU-60xx|QFN24_4X4(0.5 Pitch)|
|17|1|U2|AK8963C|BGA14_2X2(0.4Pitch)|
|18|1|U4|XC6210B302MR-G|SOT25|



Page 10 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 11 -->

**_UEVB_** 

**TABLE 2E. BILL OF MATERIAL FOR U1D, OPTION-B (e.g. with MPU-91XX)** 

|**ITEM**|**QUANTITY**|**REFERENCE**|**PART**|**PCB FOOTPRINT**|
|---|---|---|---|---|
|1|1|CN1|Header 10x2, M, 90D,<br>2.54 x 2.54 mm|HDB2X14NRA|
|2|16|C1, C2, C3, C4, C5, C6, C7, C8, C9, C11,<br>C12,C13,C14,C18,C19,C20|0.1 µF|C0402|
|3|1|C10|2200pF|C0402|
|4|2|C15, C17|2.2µF|C0402|
|5|1|C16|0.033µF|C0402|
|7|2|JP1, JP2|3-Pin Header, 2.54 x<br>2.54 mm,Male|SIP-3P|
|9|6|R9, R10, R15, R21, R24, R25|10 kΩ|R0402|
|10|5|R11, R13, R20, R22, R23|0 Ω|R0402|
|11|1|R18|1 kΩ|R0402|
|16|1|U1D|MPU-91xx|QFN24_4X4(0.5 Pitch)|
|17|1|U2|AK8963C|BGA14_2X2(0.4 Pitch)|
|18|1|U4|XC6210B302MR-G|SOT25|



Page 11 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 12 -->

**_UEVB_** 

# **_POWER SUPPLY CONNECTIONS_** 

JP1 and JP2 are 3-pin headers, which allow the user to select between an on-board LDO (Low-Voltage Dropout Regulator, U4) and an external DC supply (VIN) to power the motion sensor. For details, please refer to Table 3. 

**TABLE 3. POWER SELECTION JUMPERS (JP1, JP2)** 

|**JP1 PIN NUMBER**|**SIGNAL DESCRIPTION**|
|---|---|
|1-2 Shunted|VDD = 3V(from LDO,VIN > 3.1V,net name 3V0)|
|2-3 Shunted|VDD = VIN(from an external source)|
|**JP2 PIN NUMBER**|**SIGNAL DESCRIPTION**|
|1-2 Shunted|VDDIO = VDD|
|2-3 Shunted|VDDIO = 1.8V(from an external source,net name 1V8)|



The on-board low-noise 3V LDO offers an output that is called 3V0 (Figure 3). Using this will ensure that the sensor performance will meet data sheet specifications. 

Selecting VIN to power the chip/board is generally done while designing and evaluating an embedded platform, where the host processor and related electronics need full control over the motion processing chipset’s power supply. 

If a user intends to use the on-board 3V power source, an external VIN must be provided within the range of 3.1~6.0V to ensure the LDO works properly. 

If the user provides a VIN power level of ≥3.6V, JP1 and JP2 must be shunted across pins 1-2, since the motion sensors’ VDD and VDDIO operational ranges are ≤3.6V. 

Page 12 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 13 -->

**_UEVB_** 

# **_UEVB CONNECTOR SIGNALS DESCRIPTION_** 

## **TABLE 4. USER INTERFACE CONNECTOR SIGNALS (CN1)** 

|**CN1 PIN**<br>**NUMBER**|**CN1 SIGNAL NAME**|**SIGNAL DESCRIPTION**|
|---|---|---|
|1|AUX_DA|AUX_DA.  AuxiliaryI<sup>2</sup>C serial data signal.|
|2, 4, 9, 12,|||
|14, 16, 19,<br>25, 26, 27,<br>28|N.C.|N.C. Do not connect to these pins.|
|3|AUX_CL|AUX_CL. Auxiliary I<sup>2</sup>C serial clock signal.|
|5|1V8|1V8 Power. Receive power from InvenSense ARM controller board or<br>an external source.|
|6|DRDY|DRDY. Data ready and FIFO interrupt signals.|
|7|INT|INT. Interrupt output signal to controller.|
|8|CS|Test Signal. Not used in I<sup>2</sup>C mode; used as chip-select pin in SPI mode.|
|10|DRDY-CMP|Compass (U2) DRDY. Compass data ready signal.|
|11|TP0|Test Signal|
|13|VPP|Test Signal|
|15, 17|GND|GND. Ground connection.|
|18|REGOUT|REGOUT. Sensor’s on-chip regulator output.|
|20|SCL_SCLK|SCL/SCLK. I<sup>2</sup>C or SPI primary serial clock signal.|
|21|FSYNC|FSYNC. Frame synchronization input for camera applications.|
|22|SDA_SDI|SDA/MOSI. I²C primary data or SPI MOSI signal.|
|23|VIN|Power. Receive power from InvenSense ARM controller board or an<br>external source.|
|24|AD0_SDO|AD0/MISO. Lowest (LSB) address bit in I<sup>2</sup>C mode or SPI MISO signal in<br>SPI mode.|



Page 13 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 14 -->

**_UEVB_** 

## **CONNECTING THE FSYNC LINE** 

The FSYNC line is intended for use in a camera’s image-stabilization system. It is an input from the camera platform to the UEVB, and is intended to synchronize the motion-sensor serial-bus transfer with the master timing set by the camera system. 

## **SERIAL BUS LEVELS, SPEEDS, AND TERMINATIONS** 

The UEVB supports I²C communications up to 400 kHz, or SPI communications up to 1MHz clock rates for writing. In SPI mode, it can be operated at up to 20 MHz for reading. The I²C bus open-drain pull-up resistors (10 kΩ) are connected to VDDIO. 

Page 14 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 15 -->

**_UEVB_** 

# **_DATA GATHERING OPTIONS_** 

The motion sensor’s digital sensor data is available on the UEVB’s header CN1.  Alternatively, for connectivity with a host PC, an InvenSense ARM controller board may be used. 

## **CONNECTION TO THE INVENSENSE ARM CONTROLLER BOARD** 

For communications via USB with a host computer, the UEVB can be connected to the InvenSense ARM controller board. InvenSense provides a software tool to support the collection of sensor data through the UEVB/ARM controller board combo connected to a PC/laptop via a USB port. Please refer to the _InvenSense Data Logger (IDL) Application Notes_ document for additional instructions on how to use the software to obtain sensor data. This information can be provided by your local field team on an as-needed basis. 

Figure 4 shows the connection of the UEVB to the InvenSense ARM controller board. Connections between the two boards are made via header CN1 on the UEVB and connector JP6 on the InvenSense ARM Controller Board. 



**Figure 4. UEVB connected to the InvenSense ARM Controller Board** 

## **USE OF THE UEVB WITHOUT AN ARM CONTROLLER BOARD** 

I²C and SPI signals are made available on header CN1. Users may develop their own tools to communicate with the UEVB as there is no bus mode selection setting required. 

Page 15 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 16 -->

**_UEVB_** 

# **_SPECIAL INSTRUCTIONS_** 

## **ELECTROSTATIC DISCHARGE SENSITIVITY** 

The motion sensors can be permanently damaged by electrostatic discharge (ESD). ESD precautions for handling and storage must be taken to avoid damage to the devices. 

## **BOARD LAYOUT AND FOOTPRINT DISCUSSION** 

The UEVB is a 4-layer FR-4 PCB design with the dimensions: 38.1 x 38.1 x 1.6 mm (1500 x 1500 x 62 mil). See Figure 5 and Figure 6 for a detailed top and bottom view of the UEVB. 

The MPU footprint on the UEVB supports both QFN and LGA packages. Footprints and sensor land patterns were chosen large enough, so they offer ease of use, reliable contact with the sensor, hand-solder and debugging capabilities for both packages. 

Note that to avoid potential shorting/clearance issues at the corner pins for LGA packages, the land pattern shapes for the individual pins in this design were chosen to be oblong rather than square. The dimensions for the pin pads are 0.225 x 0.7 mm. 

Solder mask (also called solder resist is a layer of protective coating for PCB’s copper traces, which helps to prevent undesired solder bridges and shorts) dimensions will not be provided as they are dependent upon the manufacturing process and the clearance capabilities of the chosen fabrication house. Contact your PCB vendor to determine the minimum required clearance between pin pads (usually 4 mil to 6 mil or 0.102 mm to 0.152 mm) and traces allowing them enough room to print an adequate solder mask. 



Page 16 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 17 -->

**_UEVB_** 



**Figure 5 & Figure 6.Top & Bottom View of the UEVB Board Layout** 

Page 17 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 18 -->

**_UEVB_** 

## **REVISION HISTORY** 

|**DATE**|**REVISION**|**DESCRIPTION**|
|---|---|---|
|1/22/14|1.0|Initial Release|
|1/31/14|1.1|Updatedparts list and BOM tables.|
|11/7/14|1.2|Updated parts list, corrected text<br>and updated references to existing<br>documentation listed in this user<br>guide.|
|02/24/17|1.3|Updateparts list|



Page 18 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 



<!-- page 19 -->

**_UEVB_** 

This information furnished by InvenSense is believed to be accurate and reliable. However, no responsibility is assumed by InvenSense for its use, or for any infringements of patents or other rights of third parties that may result from its use. Specifications are subject to change without notice. InvenSense reserves the right to make changes to this product, including its circuits and software, in order to improve its design and/or performance, without prior notice. InvenSense makes no warranties, neither expressed nor implied, regarding the information and specifications contained in this document. InvenSense assumes no responsibility for any claims or damages arising from information contained in this document, or from the use of products and services detailed therein. This includes, but is not limited to, claims or damages based on the infringement of patents, copyrights, mask work and/or other intellectual property rights. 

Certain intellectual property owned by InvenSense and described in this document is patent protected. No license is granted by implication or otherwise under any patent or patent rights of InvenSense. This publication supersedes and replaces all information previously supplied. Trademarks that are registered trademarks are the property of their respective companies. InvenSense sensors should not be used or sold in the development, storage, production or utilization of any conventional or mass-destructive weapons or for any other weapons or life threatening applications, as well as in any other life critical applications such as medical equipment, transportation, aerospace and nuclear instruments, undersea equipment, power plant equipment, disaster prevention and crime prevention equipment. 

©2014 InvenSense, Inc. All rights reserved. InvenSense, MotionTracking, MotionProcessing, MotionProcessor, MotionFusion, MotionApps, DMP, AAR, and the InvenSense logo are trademarks of InvenSense, Inc. Other company and product names may be trademarks of the respective companies with which they are associated. 

©2014 InvenSense, Inc. All rights reserved. 

Page 19 of 19 

Document Number: **AN-IVS-0001EVB-00** Rev Number: 1.2 Rev Date: 11/07/2014 

