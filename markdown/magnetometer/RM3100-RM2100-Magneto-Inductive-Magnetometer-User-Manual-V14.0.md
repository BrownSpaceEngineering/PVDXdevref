# RM3100-RM2100-Magneto-Inductive-Magnetometer-User-Manual-V14.0

*Source: `original/magnetometer/RM3100-RM2100-Magneto-Inductive-Magnetometer-User-Manual-V14.0.pdf` (45 pages)*

<!-- page 1 -->





# **User Manual** 

**RM3100 & RM2100** Magneto-Inductive Magnetometer 





<!-- page 2 -->

## **<u>Table of Contents</u>** 

|**1**<br>**Copyright**|**& Warra**|**nty Information .......................................................................................... 3**|
|---|---|---|
|**2**<br>**Introducti**|**on ..........**|**.................................................................................................................... 4**|
|**3**<br>**Specificat**|**ions .......**|**.................................................................................................................... 5**|
|3.1|Magne|tic Sensor Characteristics ......................................................................... 5|
|3.2|Sen-X|Y-f and Sen-Z-f Characteristics .................................................................. 6|
|3.3|MagI2|C Characteristics ......................................................................................... 7|
|3.4|Dimen<br>|sions, Packaging, and Pad & Mask Layout ............................................. 8<br>|
||3.4.1|Sen-XY-f ................................................................................................... 8|
||3.4.2|Sen-Z-f .................................................................................................... 10|
||3.4.3|MagI2C ................................................................................................... 12|
|3.5|Solderi|ng ............................................................................................................. 14|
|**4**<br>**Magnetic**|**Sensor O**|**verview & Set-Up .................................................................................... 16**|
|4.1|Overvi|ew ............................................................................................................. 16|
|4.2|Layout|.................................................................................................................. 19|
||4.2.1|Sensor Orientation .................................................................................. 19|
||4.2.2|Local Magnetic Field Considerations ...................................................... 19|
||4.2.3|Other Layout Considerations .................................................................. 20|
|4.3|MagI2|C Pin-Out .................................................................................................. 21|
||4.3.1|General Pins ........................................................................................... 21|
||4.3.2|SPI Pins .................................................................................................. 23|
||4.3.3|I<sup>2</sup>C Pins ................................................................................................... 24|
|4.4|SPI Ti|ming Requirements ................................................................................... 25|
|4.5|I<sup>2</sup>C Re|quirements............................................................................................... 27|
||4.5.1|I<sup>2</sup>C Register Write ................................................................................... 27|
||4.5.2|I<sup>2</sup>C Register Read ................................................................................... 28|
|**5**<br>**MagI2C O**|**peration .**|**.................................................................................................................. 29**|
|5.1|Set th|e Cycle Count Registers (0x04 – 0x09) .................................................. 29|
|5.2|Initiate|Continuous Measurement Mode (0x01) ............................................... 30|
||5.2.1|Setting the CMM Update Rate with TMRC (0x0B) .................................. 32|
|5.3|Initiate|a Single Measurement (0x00) ............................................................... 33|
|5.4|Confir|m New Data Ready .................................................................................. 34|
||5.4.1|STATUS Register (0x34) ......................................................................... 34|
|5.5|Read t|he Measurement Results ........................................................................ 34|
|5.6|Troubl|eshooting and General Information ......................................................... 35|
||5.6.1|Built-In Self Test Register (0x33) ............................................................ 35|
||5.6.2|HSHAKE Register (0x35) ....................................................................... 38|
||5.6.3|REVID Register (0x36) ........................................................................... 38|
|5.7|Examp|les using the SPI Interface ..................................................................... 39|
||5.7.1|Set the Cycle Count Registers ................................................................ 39|
||5.7.2|<br>Making and Reading Measurements ...................................................... 39|
|5.8|Examp|les using the I<sup>2</sup>C Interface ...................................................................... 42|
||<br>5.8.1|<br>Set the Cycle Count Registers ................................................................ 42|
||5.8.2|Initiate a Single Measurement ................................................................ 42|
||5.8.3|Initiate Continuous Measurement Mode ................................................. 43|
||5.8.4|Read the Measurement Results ............................................................. 43|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 1 of 45** 



<!-- page 3 -->

### **<u>List of Figures</u>** 

|Figure 3-1: Sen-XY-f Sensor Dimensions.....................................................................................8|
|---|
|Figure 3-2: Sen-XY-f Tape and Reel Dimensions........................................................................9|
|Figure 3-3: Sen-XY-f Recommended Solder Pad, Paste, & Mask Layout..................................9|
|Figure 3-4: Sen-Z-f Sensor Dimensions.....................................................................................10|
|Figure 3-5: Sen-Z-f Tape and Reel Dimensions.........................................................................11|
|Figure 3-6: Sen-Z-f Recommended Solder Pad, Paste, & Mask Layout..................................11|
|Figure 3-7: MagI2C MLF Mechanical Drawing...........................................................................12|
|Figure 3-8: MagI2C MLF PCB Pad Pattern .................................................................................... 13|
|Figure 3-9: MagI2C MLF Tape Dimensions.................................................................................... 14|
|Figure 3-10: Recommended Solder Reflow Profile ....................................................................... 15|
|Figure 4-1: RM3100 reference schematic – SPI Configuration .................................................... 16<br>|
|Figure 4-2: RM3100 reference schematic – I<sup>2</sup>C Configuration ..................................................... 17|
|Figure 4-3: LR Oscillator Circuit Biasing Diagram ......................................................................... 18|
|Figure 4-4: RM3100 North-East-Down (NED) Sensor Layout ..................................................... 19|
|Figure 4-5: SPI Timing Diagram, CPOL = CPHA = 0 .................................................................... 26|
|Figure 4-6: SPI Timing Diagram, CPOL = CPHA = 1 .................................................................... 26|
|Figure 5-1: SPI Activity Sequence Diagram ................................................................................... 39|



### **<u>List of Tables</u>** 

|Table 3-1: Magnetic Sensor Performance .................................................................................................. 5|
|---|
|Table 3-2: Sen-XY-f and Sen-Z-f Absolute Maximum Ratings....................................................6|
|Table 3-3: Sen-XY-f and Sen-Z-f Characteristics.........................................................................6|
|Table 3-4: MagI2C Absolute Maximum Ratings...........................................................................7|
|Table 3-5: MagI2C Recommended Operating Conditions...........................................................7|
|Table 3-6: Recommended Solder Processing Parameters .......................................................... 15|
|Table 4-1: MagI2C Pin Assignments ............................................................................................... 22|
|Table 4-2: SPI Timing Specifications ............................................................................................... 27|
|Table 5-1: MagI2C Register Map ..................................................................................................... 29|
|Table 5-2: Cycle Count Registers .................................................................................................... 30|
|Table 5-3: Continuous Mode DRDY Options ................................................................................. 31|
|Table 5-4: CMM Update Rates......................................................................................................... 33|
|Table 5-5: Measurement Results Registers ................................................................................... 35|
|Table 5-6: BIST Timeout Period ....................................................................................................... 36|
|Table 5-7: BIST LR Periods .............................................................................................................. 36|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 2 of 45** 



<!-- page 4 -->

# **1 Copyright & Warranty Information** 

© Copyright 2013 PNI Sensor 

All Rights Reserved. Reproduction, adaptation, or translation without prior written permission is prohibited, except as allowed under copyright laws. 

Revised Dec 2022 PNI Sensor 2331 Circadian Way Santa Rosa, CA 95407, USA Tel: (707) 566-2260 Fax: (707) 566-2261 

**Warranty and Limitation of Liability.** PNI Sensor ("PNI") manufactures its Products from parts and components that are new or equivalent to new in performance. PNI warrants that each Product to be delivered hereunder, if properly used, will, for ninety (90) days following the date of shipment unless a different warranty time period for such Product is specified: (i) in PNI’s Price List in effect at time of order acceptance; or (ii) on PNI’s web site (www.pnicorp.com) at time of order acceptance, be free from defects in material and workmanship and will operate in accordance with PNI’s published specifications and documentation for the Product in effect at time of order. PNI will make no changes to the specifications or manufacturing processes that affect form, fit, or function of the Product without written notice to the Customer, however, PNI may at any time, without such notice, make minor changes to specifications or manufacturing processes that do not affect the form, fit, or function of the Product. This warranty will be void if the Products’ serial number, or other identification marks have been defaced, damaged, or removed. This warranty does not cover wear and tear due to normal use, or damage to the Product as the result of improper usage, neglect of care, alteration, accident, or unauthorized repair. 

THE ABOVE WARRANTY IS IN LIEU OF ANY OTHER WARRANTY, WHETHER EXPRESS, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY OF MERCHANTABILITY, FITNESS FOR ANY PARTICULAR PURPOSE, OR ANY WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL, SPECIFICATION, OR SAMPLE. PNI NEITHER ASSUMES NOR AUTHORIZES ANY PERSON TO ASSUME FOR IT ANY OTHER LIABILITY. 

If any Product furnished hereunder fails to conform to the above warranty, Customer’s sole and exclusive remedy and PNI’s sole and exclusive liability will be, at PNI’s option, to repair, replace, or credit Customer’s account with an amount equal to the price paid for any such Product which fails during the applicable warranty period provided that (i) Customer promptly notifies PNI in writing that such Product is defective and furnishes an explanation of the deficiency; (ii) such Product is returned to PNI’s service facility at Customer’s risk and expense; and (iii) PNI is satisfied that claimed deficiencies exist and were not caused by accident, misuse, neglect, alteration, repair, improper installation, or improper testing. If a Product is defective, transportation charges for the return of the Product to Customer within the United States and Canada will be paid by PNI. For all other locations, the warranty excludes all costs of shipping, customs clearance, and other related charges. PNI will have a reasonable time to make repairs or to replace the Product or to credit Customer’s account. PNI warrants any such repaired or replacement Product to be free from defects in material and workmanship on the same terms as the Product originally purchased. 

Except for the breach of warranty remedies set forth herein, or for personal injury, PNI shall have no liability for any indirect or speculative damages (including, but not limited to, consequential, incidental, punitive and special damages) relating to the use of or inability to use this Product, whether arising out of contract, negligence, tort, or under any warranty theory, or for infringement of any other party’s intellectual property rights, irrespective of whether PNI had advance notice of the possibility of any such damages, including, but not limited to, loss of use, revenue or profit. In no event shall PNI’s total liability for all claims regarding a Product exceed the price paid for the Product. PNI neither assumes nor authorizes any person to assume for it any other liabilities. 

Some states and provinces do not allow limitations on how long an implied warranty lasts or the exclusion or limitation of incidental or consequential damages, so the above limitations or exclusions may not apply to you. This warranty gives you specific legal rights and you may have other rights that vary by state or province. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 3 of 45** 



<!-- page 5 -->

# **2 Introduction** 

Thank you for purchasing PNI Sensor’s RM2100 or RM3100 Magnetic Sensor, pn 90052 or pn 90053, respectively. The RM2100 is comprised of two Sen-XY-f sensors, pn 13104, and a MagI2C ASIC controller, pn 13156, which forms the basis for a 2-axis digital compass. The RM3100 is the same as the RM2100 but adds a Sen-Z-f sensor, pn 13101, such that compassing measurements are not constricted to the horizontal plane. 

PNI’s magnetic sensor technology provides high resolution, low power consumption, large signal noise immunity, a large dynamic range, and high sampling rates. Measurements are stable over temperature and inherently free from offset drift. The RM3100’s MagI2C ASIC features both continuous measurement mode and single measurement polling, software-configurable resolution and sample rate, and the ability to operate one, two, or three PNI sensors. And it incorporates both I<sup>2</sup> C and SPI interfaces for system design flexibility. 

When implementing an RM3100 or RM2100 Magnetic Sensor, each sensor serves as the inductive element in a simple LR relaxation oscillation circuit, where the sensor’s effective inductance is proportional to the magnetic field parallel to the sensor axis. The LR circuit is driven by the MagI2C ASIC, and the MagI2C’s internal clock is used to measure the circuit’s oscillation frequency, and hence the magnetic field. Since PNI’s Magnetic Sensor works in the frequency domain, resolution and noise are established cleanly by the number of MagI2C internal clock counts (cycle counts). In comparison, fluxgate and MR technologies require expensive and complex signal processing to obtain similar resolution and noise, and in many respects the magnetic sensor’s performance simply cannot be matched. Also, the output from the MagI2C is inherently digital and can be fed directly into a microprocessor, eliminating the need for signal conditioning or an analog/digital interface between the sensor and a microprocessor. The simplicity of PNI’s magnetic sensor combined with the lack of signal conditioning makes it easier and less expensive to implement than alternative fluxgate or magneto-resistive (MR) technologies. 

For more information on PNI’s magneto-inductive sensor technology, see PNI’s whitepaper “Magneto-Inductive Technology Overview” at http://www.pnicorp.com/technology/papers. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 4 of 45** 



<!-- page 6 -->

# **3 Specifications** 

## **3.1 Magnetic Sensor Characteristics** 

**Table 3-1: Magnetic Sensor Performance**<sup>**1**</sup> 

|**Parameter**|**Cy **<br>**50**|**cle Counts**<br>**100**|<sup>**2**</sup><br>**200**|**Units**|
|---|---|---|---|---|
|Field Measurement Range<sup>3</sup>|-|800 to +800||μT|
|Gain|20|38|75|LSB/μT|
|Sensitivity|50|26|13|nT|
|Noise|30|20|15|nT|
|Noise Density @ Max. Single-Axis Sample Rate||1.2||nT/`√`Hz|
|Repeatability over ±200 μT|15|8|8|nT|
|Hysteresis over ±200 μT||15||nT|
|Linearity over ±200 μT||0.5||%|
|Maximum Single-Axis Sample Rate<br>(divide by 3 for max. 3-axis sample rate)|1600|850|440|Hz|
|Single-Axis Average Current @ 24 Hz Sample<br>Rate (equivalent to 3-axis @ 8 Hz)|70|135|260|µA|
|Bias Resistor, Rb||121||`Ω`|
|External Timing Resistor for Clock, REXT||33||k`Ω`|
|Circuit Oscillation Frequency||180||kHz|
|OperatingTemperature||-40 to +85||C|



### **<u>Footnotes:</u>** 

1. Performance values are typical. Performance specifications established with a supply voltage of 3.0 V, a bias resistor of 121 Ω, an external timing resistor of 33 kΩ, and with measurements taken at room temperature. Other bias resistors, external timing resistors and operating voltages may be used, but performance will differ from the values listed. Contact PNI for additional information. 

2. The cycle count setting (eg. 50 ,100, and 200) is user-configurable and set in the Cycle Count Registers. See Section 4.1 for a discussion on how the RM3100 works, and Section 5.1 for how to set the Cycle Count Registers. 

3. Field measurement range is defined as the monotonic region of the output characteristic curve. Field measurement range can be extended using different bias resistors. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 5 of 45** 



<!-- page 7 -->

# **3.2 Sen-XY-f and Sen-Z-f Characteristics** 

**Table 3-2: Sen-XY-f and Sen-Z-f Absolute Maximum Ratings** 

|**Parameter**|**Minimum**|**Maximum**|**Units**|
|---|---|---|---|
|Input Pin Current @ 25 C||50|mA|
|Voltage Across Sensor||2.0|VDC|
|Storage Temperature|-40|+85|C|



### **CAUTION:** 

Stresses beyond those listed above may cause permanent damage to the device. These are stress ratings only. Assuming operation with the MagI2C per the guidelines in this manual, these maximum ratings will not be violated. 

**Table 3-3: Sen-XY-f and Sen-Z-f Characteristics** 

|**Parameter**||**Min**|**Typical**|**Max**|**Units**|
|---|---|---|---|---|---|
|Inductance<sup>1</sup>|||500-600||μH|
|DC resistance|@ 25C ±15C|30||45|`Ω`|
|Resistance ver<br>temperature|sus||0.4||%/C|
|Weiht|Sen-XY-f||0.06 [0.002]||gm [oz]|
|g|Sen-Z-f||0.09 [0.003]||gm [oz]|
|OperatingTem|perature|-40||+85|C|



**<u>Footnote:</u>** 

1. 1 V peak-to-peak across the sensor @ 100 kHz sinewave. No DC bias resistance. Measured orthogonal to Earth’s magnetic field. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 6 of 45** 



<!-- page 8 -->

# **3.3 MagI2C Characteristics** 

**Table 3-4: MagI2C Absolute Maximum Ratings** 

|**Parameter**|**Minimum**|**Maximum**|**Units**|
|---|---|---|---|
|Analog/Digital DC Supply Voltage, AVDD& DVDD|-0.3|+3.7|VDC|
|Input Pin Voltage|-0.3|AVDDor DVDD|VDC|
|Input Pin Current @ 25C|-10.0|+10.0|mA|
|Storage Temperature|-40°|+125°|C|



### **CAUTION:** 

Stresses beyond those listed above may cause permanent damage to the device. These are stress ratings only. Operation of the device at these or other conditions beyond those indicated in the operational sections of the specifications is not implied. 

**Table 3-5: MagI2C Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|
|---|---|---|---|---|---|
|Analog/Digital DC Supply Voltage<sup>1</sup>|AVDD,<br>DVDD|2.0|3.0|3.6|VDC|
|Supply Voltage<br>During Operation<br>|∆VDD_OP|-0.1|0|+0.1|VDC|
|Difference<br>(DVDD-AVDD)<br>Analog Unpowered|∆VDD_OFF|DVDD-0.1|DVDD|DVDD+0.1|VDC|
|Voltage Ripple on AVDDor DVDD|VDD_ripple|||0.05|VPP|
|High level input voltage|VIH|0.7*DVDD||DVDD|VDC|
|Low level input voltage|VIL|0||0.3*DVDD|VDC|
|High level output current|IOH|||-1|mA|
|Low level output current|IOL|1|||mA|
|Idle Mode Current||||1|µA|
|Leakage Current @ DVDDpin<br>(AVDD=AVSS=DVSS=0V, DVDD=3.6V)||||100|nA|
|OperatingTemperature|TOP|-40||+85|C|



#### **<u>Footnote:</u>** 

1.  Please contact PNI if operation at <2.0 V is required. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 7 of 45** 



<!-- page 9 -->

# **3.4 Dimensions, Packaging, and Pad & Mask Layout** 

## **3.4.1 Sen-XY-f** 



_Figure 3-1: Sen-XY-f Sensor Dimensions_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 8 of 45** 



<!-- page 10 -->





<!-- Start of picture text -->
Dimensions in mm<br>Full reel is 5000 pcs. Smaller quantities on cut tape.<br>Tape & reel meets ANSI/EIA standard EIA-418-B<br><!-- End of picture text -->

_Figure 3-2: Sen-XY-f Tape and Reel Dimensions_ 



**_Note:_** _PNI recommends a 5 mil stencil. The solder paste area is much smaller than the pad to reduce sensor tilt and misalignment. The above layout allows for rework: for minimal footprint, contact PNI._ 

_Figure 3-3: Sen-XY-f Recommended Solder Pad, Paste, & Mask Layout_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 9 of 45** 



<!-- page 11 -->

# **3.4.2 Sen-Z-f** 



_Figure 3-4: Sen-Z-f Sensor Dimensions_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 10 of 45** 



<!-- page 12 -->



**Dimensions in mm** Full reel is 1200 pcs. Smaller quantities on cut tape. Tape & reel meets ANSI/EIA standard EIA-418-B 

_Figure 3-5: Sen-Z-f Tape and Reel Dimensions_ 



**_Note:_** _PNI recommends a 5 mil stencil. The solder paste area is much smaller than the pad to reduce sensor tilt and misalignment. The above layout allows for rework: for minimal footprint, contact PNI._ 

_Figure 3-6: Sen-Z-f Recommended Solder Pad, Paste, & Mask Layout_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 11 of 45** 



<!-- page 13 -->

## **3.4.3 MagI2C** 



_Figure 3-7: MagI2C MLF Mechanical Drawing_ 

**_Note_** _: PNI recommends not soldering to the exposed die pad in the center of the ASIC_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 12 of 45** 



<!-- page 14 -->



_Figure 3-8: MagI2C MLF PCB Pad Pattern_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 13 of 45** 



<!-- page 15 -->



**Dimensions: mm** Full reel is 5000 pcs. Smaller quantities on cut-tape. Tape & Reel meets ANSI/EIA standard EIA-418 

_Figure 3-9: MagI2C MLF Tape Dimensions_ 

# **3.5 Soldering** 

Figure 3-10 and Table 3-6 provide the recommended solder reflow profile and processing parameters for RM3100 components. After soldering PNI components to a board, it is possible to wave solder the opposite side of the PCB. 

**_IMPORTANT: PNI sensors require the use of halide-free solder pastes and processes for reflow and cleaning. Contact PNI if you would like recommendations._** 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 14 of 45** 



<!-- page 16 -->



<!-- Start of picture text -->
PB<br><!-- End of picture text -->

_Figure 3-10: Recommended Solder Reflow Profile_ 

**Table 3-6: Recommended Solder Processing Parameters**<sup>**1**</sup> 

|**Parameter**|**Symbol**|**Value**|
|---|---|---|
|Preheat Temperature, Minimum|TSmin|150°C|
|Preheat Temperature, Maximum|TSmax|200°C|
|Preheat Time (TSminto TSmax)||60 – 180 seconds|
|Solder Melt Temperature|TL|>218°C|
|Ramp-Up Rate (TSmaxto TL)||3°C/secondmaximum|
|Peak Temperature|TP|<260°C|
|Time from 25°C to Peak (TP)||6 minutes maximum|
|Time above TL|tL|60 – 120 seconds|
|Soak Time (within 5°C of TP)|tP|10 – 20 seconds|
|RampdownRate||4°C/secondmaximum|



### **<u>Footnote:</u>** 

1. Meets IPC/JEDEC J-STD-020 profile recommendations. Sen-XY-f and SenZ-f classified as moisture sensitivity level 1. MagI2C MLF classified as moisture sensitivity level 3. 

**PNI Sensor** 

**Doc 1017252 V14.0 Page 15 of 45** 

**RM3100 & RM2100 Magneto-Inductive Magnetometer** 



<!-- page 17 -->

# **4 Magnetic Sensor Overview & Set-Up** 

## **4.1 Overview** 

Figure 4-1 and Figure 4-2 provide basic schematics for implementing the RM3100 Sensor Suite when using the SPI interface and I<sup>2</sup> C interface, respectively. The MagI2C is at the center of the schematic, as it ties the user’s host controller, on the left, to the three sensors, on the right. Unused sensor connections should remain floating. 

**_Note:_** _RM3100 and RM2100 Magnetic Sensors typically are used in compassing applications, where each channel represents a Cartesian coordinate axis, X, Y, or Z. For this reason, the term “axis”_ _<u>generally is used instead of “channel”.</u>_ 



_Figure 4-1: RM3100 reference schematic – SPI Configuration Note: The RM2100 Pins 6, 7, 8, and 9 are no-connect._ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 16 of 45** 



<!-- page 18 -->



_Figure 4-2: RM3100 reference schematic – I_<sup>_2_</sup> _C Configuration Note: The RM2100 Pins 6, 7, 8, and 9 are no-connect._ 

A Sen-XY-f or Sen-Z-f sensor serves as the inductive element in a simple LR relaxation oscillation circuit which is composed of an external bias resistor along with digital gates and a comparator internal to the MagI2C. The sensor’s inductance is a function of the magnetic field strength. As such, the frequency of oscillation of the circuit varies with the strength of the total magnetic field parallel to the sensor. To make a measurement, one side of the sensor is grounded while the other side is alternately driven with positive and negative current through the oscillator. The circuit is driven for a set number of circuit oscillations, and the time to complete the oscillations is measured using the MagI2C’s internal high-speed clock. The MagI2C next switches the bias connection to the sensor and makes another measurement. The side that was previously grounded is now charged and discharged while the other is now grounded. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 17 of 45** 



<!-- page 19 -->

Because: 

- the total magnetic field represents the sum of the local field and the circuit-induced field, and 

- the circuit-induced magnetic field has the same magnitude but opposite direction for the two bias polarities, 

the local magnetic field is proportional to the difference in the time to complete the measurement for each bias. The difference in the number of clock oscillations between the forward and reverse bias directions is output from the MagI2C, and this number is directly proportional to the strength of the local magnetic field in the direction of the sensor. 

Figure 4-3 provides a detail of the biasing circuit. For more on PNI’s magneto-inductive technology, refer to the “Magneto-Inductive Technology Overview” white paper found on PNI’s website. 



_Figure 4-3: LR Oscillator Circuit Biasing Diagram_ 

Since PNI’s Magnetic Sensor Suite works in the frequency domain, resolution is cleanly established by the number of circuit oscillations. Also, the output from the MagI2C is inherently digital and can be fed directly into a microprocessor, which eliminates the need for signal conditioning or an analog/digital interface between the sensor and host processor. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 18 of 45** 



<!-- page 20 -->

# **4.2 Layout** 

## **4.2.1 Sensor Orientation** 

Figure 4-4 indicates how the three sensors in a RM3100 Magnetic Sensor should be oriented for a system referenced as north-east-down (NED). The arrow represents the direction of travel or pointing. The Sen-XY-f is insensitive to the location of the polarity indicator, while the location of the polarity indicator is critical for the Sen-Z-f. 



_Figure 4-4: RM3100 North-East-Down (NED) Sensor Layout_ 

If the Sen-Z-f sensor is flipped to the bottom of the board such that the polarity indicator still points back or the curved portion of the sensor still points forward, then to retain NED the Sen-Z-f’s ZDRVN and ZDRVP pads should be as shown above, except on the bottom of the board. As the pads on the Sen-Z-f have switched positions, the connections to the Sen-Z-f sensor will be reversed. 

## **4.2.2 Local Magnetic Field Considerations** 

Because the RM3100 sensor measure magnetic field, it is important to consider what items in the vicinity of the sensors can affect the sensor readings. Note that magnetic field drops off as (1/distance)<sup>3</sup> . Specific issues to consider include: 

- The sensors have a specified linear regime of ± 200 μ T. (Earth’s field is ~50 μ T.) To ensure the sensors operate in their linear regime, do not place the sensors close to large electric currents, large masses of ferrous material, or devices incorporating permanent magnets, such as speakers and electric motors. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 19 of 45** 



<!-- page 21 -->

- Locate the sensors away from changing magnetic fields. If this is not possible, but the local magnetic field is known to have multiple states, try to take readings only when the field is in a known state. For instance, if a motor runs part of the time, take readings only when the motor is in a known state. 

- If you are uncertain about the effect a specific component may have on the system, the RM3100 Evaluation Board can be used to help ascertain this. Place the RM3100 Evaluation Board on a firm surface and gradually bring the component in question close to the board, then note when the magnetic field starts to change. If the component cannot be moved, then gradually move the RM3100 Evaluation Board towards the component, carefully ensuring the orientation of the board remains constant while doing this. 

- If an RM3100 Evaluation Board is not available, gradually bring the component in question closer to one of the sensors and observe when the sensor reading from the MagI2C starts to change. 

## **4.2.3 Other Layout Considerations** 

Other design considerations include: 

- To minimize the effect of gradients in the magnetic field, position the sensors as close to each other as possible. 

- To reduce coupling to and from other signals, keep the two traces from the MagI2C to each sensor as close as possible to each other. PNI recommends locating the MagI2C within 10 cm from the sensors. 

- Keep capacitors, especially tantalum capacitors, far away from the sensors. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 20 of 45** 



<!-- page 22 -->

# **4.3 MagI2C Pin-Out** 

The MagI2C’s pin-out is summarized on the following page in Table 4-1. Pin numbers run counterclockwise, when looking from the top, starting at the Pin 1 designator as shown in Figure 3-7. 

## **4.3.1 General Pins** 

### **AVDD and DVDD (pins 4, 14, & 26)** 

AVDD and DVDD should be tied to the analog and digital supply voltages, respectively. The recommend voltages are defined in Table 3-5, and the maximum voltages are given in Table 3-4. DVDD must be on whenever AVDD is on, so DVDD should either be brought up first or at precisely the same time as AVDD. AVDD can be turned off when not making a measurement to conserve power, since all other operations are supported with DVDD. Under this condition, register values will be retained as long as DVDD is powered. Also, AVDD must be within 0.1 V of DVDD when AVDD is on. 

### **AVSS and DVSS (pins 5 & 19)** 

AVSS and DVSS should be tied to the analog and digital ground, respectively. Assuming the ground plane is clean, they may share a common ground. Alternatively, they may have their own ground planes if this is more convenient. DVSS and AVSS should be within 0.1 V of each other. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 21 of 45** 



<!-- page 23 -->

**Table 4-1: MagI2C Pin Assignments** 

|**Pin#**|**Pin Name**|**Description**|
|---|---|---|
|1|MOSI /<br>SDA|SPI interface (MOSI)–Master Output, Slave Input Serial Data<br>I<sup>2</sup>C interface (SDA) – Serial Data Line|
|2|RES|Reserved – connect to ground|
|3|SSN /<br>SA0|SPI interface–Active low to select port<br>I<sup>2</sup>C interface – Bit 0 of MagI2C’s slave address|
|4|AVDD|Supply voltage for analog section of ASIC|
|5|AVSS|Ground pin for analog section of ASIC|
|6|ZDRVP|Z sensor drive output|
|7|ZINP|Z sensor measurement input|
|8|ZINN|Z sensor measurement input|
|9|ZDRVN|Z sensor drive output|
|10|YDRVP|Y sensor drive output|
|11|YINP|Y sensor measurement input|
|12|YINN|Y sensor measurement input|
|13|YDRVN|Y sensor drive output|
|14|DVDD|Supply voltage for digital section of ASIC.|
|15|XDRVP|X sensor drive output|
|16|XINP|X sensor measurement input|
|17|XINN|X sensor measurement input|
|18|XDRVN|X sensor drive output|
|19|DVSS|Ground pin for digital section of ASIC|
|20|RES|Reserved – connect to ground|
|21|NC|Do not connect|
|22|I2CEN|I<sup>2</sup>C enable pin (HIGH = I<sup>2</sup>C, LOW = SPI)|
|23|DRDY|Status line|
|24|NC|Do not connect|
|25|REXT|External timing resistor for high speed clock.|
|26|DVDD|Supply voltage for digital section of ASIC.|
|27|SCLK /<br>SCL|SPI interface (SCLK)–Serial clock input<br>I<sup>2</sup>C interface (SCL) – Serial clock line|
|28|MISO /<br>SA1|SPI interface (MISO)–Master Input, Slave Output<br>I<sup>2</sup>C interface – Bit 1 of MagI2C’s slave address|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 22 of 45** 



<!-- page 24 -->

### **Sensor Drive and Measurement Pins (pins 6 – 13 & 15 – 18)** 

The various sensor drive and measurement pins should be connected to the sensors. For a north-east-down (NED) reference frame, the connections should be as defined in Figure 4-4. 

### **I2CEN (pin 22)** 

This pin should be pulled LOW when using the SPI interface or pulled HIGH when using the I<sup>2</sup> C interface. 

### **DRDY (pin 23)** 

DRDY is used to ensure data is read from the MagI2C only when it is available. The DRDY pin will go HIGH when the measurement is complete. This signals the host that data is ready to be read. The DRDY pin automatically is set LOW when the Measurement Result registers are read or a write operation is performed. 

It is not mandatory to use the DRDY pin, as alternative methods exist to determine if data is available. Specifically, the STATUS register provides this information. And, if using the SPI interface where CPHA=CPOL=1, the MISO line also indicates if data is available when SSN is LOW. 

### **REXT (pin 25)** 

REXT ties to the external timing resistor for the high-speed clock. The recommended value for the resistor and associated clock speed are defined in Table 3-1. 

## **4.3.2 SPI Pins** 

### **MOSI (pin 1)** 

MOSI is an SPI input that provides data from the master device to the MagI2C. Data is transferred most significant bit first. Data must be presented at least 50 ns before the rising edge of SCLK, and remain valid for 50 ns after the edge. New data typically is presented to the MOSI pin on the falling edge of SCLK. 

### **SSN (pin 3)** 

This signal sets the MagI2C as the operating slave device on the SPI bus. The SSN pin must be LOW prior to data transfer in either direction, and must stay LOW during the entire transfer. 

The SSN pin must transition from HIGH to LOW prior to reading from or writing to the registers. It must stay LOW for the remainder of the operation. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 23 of 45** 



<!-- page 25 -->

After communication between the MagI2C and master device is finished, the SPI bus can be freed up (SSN pin set HIGH) to communicate with other slave devices while the MagI2C takes a measurement or is idle. 

### **SCLK (pin 27)** 

SCLK is a SPI input used to synchronize the data sent in and out through the MISO and MOSI pins. SCLK is generated by the customer-supplied master device and should be 1 MHz or less. One byte of data is exchanged over eight clock cycles. Data is captured by the master device on the rising edge of SCLK. Data is shifted out and presented to the MagI2C on the MOSI pin on the falling edge of SCLK, except for the first bit (MSB) which must be present before the first rising edge of SCLK. 

### **MISO (pin 28)** 

MISO is an SPI output that sends data from the MagI2C to the master device. Data is transferred most significant bit first and is captured by the master device on the rising edge of SCLK. The MISO pin is placed in a high impedance state if the MagI2C is not selected (i.e. if SSN=1). 

## **4.3.3 I**<sup>**2**</sup> **C Pins** 

### **SDA (pin 1)** 

The SDA line is a bi-directional line used to send commands to the MagI2C and used to transmit data from the MagI2C. Data is transferred most significant bit first. All communication between the host and the MagI2C occurs on this line when implementing the I2C interface. 

### **SA0 (pin 3)** 

SA0 represents the second-least significant bit in the MagI2C’s slave address. Pulling this HIGH represents a ‘1’ and pulling it low represents a ‘0’. Along with pin 28 (bit 1) and the higher 5 bits (0b01000), which are pre-defined in hardware, SA0 establishes the 7-bit slave address of the MagI2C on the I<sup>2</sup> C bus. 

### **SCL (pin 27)** 

SCL is used to synchronize the data sent in and out through the SDA pin. SCL is generated by the customer-supplied master device and should be 1 MHz or less. Data is captured by the master device on the rising edge of SCL. Data is shifted out and presented to the MagI2C on the SDA pin on the falling edge of SCL, except for the first bit which must be present before the first rising edge of SCL. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 24 of 45** 



<!-- page 26 -->

### **SA1 (pin 28)** 

SA1 represents the least significant bit in the MagI2C’s slave address. Pulling this HIGH represents a ‘1’ and pulling it low represents a ‘0’. Along with pin 3 (bit 0) and the higher 5 bits (0b01000), which are pre-defined in hardware, SA1 establishes the 7-bit slave address of the MagI2C on the I<sup>2</sup> C bus. 

# **4.4 SPI Timing Requirements** 

The MagI2C can act as a slave device on a SPI bus. The SPI interface consists of four signals, as carried on SCLK, MOSI, MISO, and SSN. The SPI clock, SCLK, should run at 1 MHz or less. Data sent out on MOSI is considered valid while SCLK is HIGH, and data is in transition when SCLK is LOW.  The first byte sent to the MagI2C contains the Read/Write bit (Write=0) followed by the 7-bit register address. When the register address byte is received the MagI2C returns the STATUS register contents. Assuming SSN stays low and SCLK continues, multiple registers can be written to or read from as the MagI2C will automatically increment to the next register address. The clock polarity when the bus is idle can either be LOW (CPOL=CPHA=0) or HIGH (CPOL=CPHA=1). 

As long as SSN is LOW data can transfer to or from the MagI2C. Generally it is a good idea to pull SSN to HIGH after a read or write operation has completed such that the SPI bus can be freed up for other devices. The MagI2C can perform measurements while the SSN line is HIGH, as this does not involve communication with the master. Pulling the SSN to HIGH during a data read or write will terminate the transaction. 

The timing parameters, defined in Figure 4-5 or Figure 4-6 and specified in Table 4-2, must be met to ensure reliable communication. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 25 of 45** 



<!-- page 27 -->



_Figure 4-5: SPI Timing Diagram, CPOL = CPHA = 0_ 



_Figure 4-6: SPI Timing Diagram, CPOL = CPHA = 1_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 26 of 45** 



<!-- page 28 -->

**Table 4-2: SPI Timing Specifications** 

|**Symbol**|**Description**|**Min**|**Max**|**Units**|
|---|---|---|---|---|
|tSHZD|SSN LOW to data output||100|ns|
|tSSDV|SSN LOW to Command Byte|100||ns|
|tDBSH|Setup data before active edge|50||ns|
|tDASH|Hold data after active edge|50||ns|
|tDRDV|Clock falling edge to valid data||20|ns|
|tSSH|Final clock cycle falling edge to SSN HIGH|100||ns|
|tSHDZ|SSN HIGH to output data tri-state||100|ns|
|tSSW|SSN HIGH to LOW (time between transactions)|100|||



## **4.5 I**<sup>**2**</sup> **C Requirements** 

The MagI2C can operate as a slave device on an I<sup>2</sup> C bus. It is identified by a 7-bit slave address. The higher 5 bits of the slave address are pre-defined in hardware and the same for all MagI2C devices. PNI has registered these first 5 bits as 0b01000. The lower 2 bits of the slave address are user-configurable, using pins 3 and 28. As such, 4 different slave addresses are possible. For example, setting pin 3 HIGH and pin 28 LOW results in an address of 0b0100001. 

The MagI2C’s I<sup>2</sup> C interface complies with NXP’s UM10204 specification and user manual, revision 03. Standard, fast, fast plus, and high speed modes of the I<sup>2</sup> C protocol are supported. Below is a link to this document. 

<u>http://www.nxp.com/documents/user_manual/UM10204.pdf</u> 

### **4.5.1 I**<sup>**2**</sup> **C Register Write** 

A generic Write transaction is given below. 

|START<br>S<br>|MagI2C ADDRESS<br>A6 A5 A4 A3 A2 A1 A0|RW ACK MagI2C REG. ADDRESS (N) ACK<br> <br>0<br>0<br>A7 A6 A5 A4 A3 A2 A1 A0<br>0|<br>DATA TO REGISTER (N)<br>A7 A6 A5 A4 A3 A2 A1 A0|ACK DATA TO REGISTER (N+1) ACK <br> <br>0<br>A7 A6 A5 A4 A3 A2 A1 A0<br>0|STOP<br>P|
|---|---|---|---|---|---|
||From Host to MagI2C<br>From MagI2C to Host||------------ Data Transferre|d (n bytes + acknowledge) ------------||



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 27 of 45** 



<!-- page 29 -->

All communication is on the SDA line. The transaction is initiated by the host, or master, sending the Start condition followed by the MagI2C’s slave address, and then the RW bit is set to ‘0’, indicating a Write operation. The slave address is acknowledged by the MagI2C by setting SDA to LOW. This is followed by the desired 7-bit register address and then the register data. The register value automatically increments after every received data byte. The transaction is terminated by the host sending the Stop condition. 

The MagI2C will always acknowledge the start of an I<sup>2</sup> C Write transaction by sending a ‘0’ (i.e. the ACK signal). But if the Write command cannot be executed for some reason the MagI2C will send a ‘1’ instead (i.e. the NACK signal). The reasons a NACK signal might be sent are established by the HSHAKE register, and include writing to an undefined register or writing to the POLL register while CMM is in progress, or vice versa. See Section 0 for more information. 

### **4.5.2 I**<sup>**2**</sup> **C Register Read** 

To perform a Read transaction, it is first necessary for the master to Write the desired register address, and then to Read the register data. A generic transaction is given below. 



<!-- Start of picture text -->
START  SLAVE ADDRESS  RW ACK  REGISTER ADDRESS (N)  ACK STOP<br>S A6 A5 A4 A3 A2 A1 A0  0 0 A7 A6 A5 A4 A3 A2 A1 A0  0 P<br>From Host to MagI2C<br>From MagI2C to Host<br>START  SLAVE ADDRESS  RW ACK  DATA FROM REG. (N)  ACK  DATA FROM REG. (N+1)  NACK STOP<br>S A6 A5 A4 A3 A2 A1 A0  1 0 A7 A6  A5  A4 A3 A2  A1  A0  0 A7 A6  A5  A4  A3 A2  A1  A0  1 P<br>-------------- Data Transferred (n bytes + acknowledge) --------------<br><!-- End of picture text -->

The Write sequence is described in the prior section, except for this case there is no data to send. For the Read sequence the host again sends the MagI2C’s slave address, but this time sets the RW bit is set to ‘1’. The MagI2C acknowledges that it is has been addressed and then sends data from the register address that was previously sent. The host acknowledges receipt of the data, and then the MagI2C increments the register address and sends data from this register. This continues until the host sends the NACK command followed by the Stop command, which terminates the transaction. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 28 of 45** 



<!-- page 30 -->

# **5 MagI2C Operation** 

The primary functions of the MagI2C are: 

- Set the Cycle Count Registers if the default is not desired. 

- Initiate either a Single Measurement or Continuous Measurement. 

- Confirm New Data Ready. 

- Read the Measurement Results Registers. 

Each of these steps is discussed in detail in the following sections. 

**_Note:_** _The MagI2C incorporates an Idle Mode to reduce power consumption. The device automatically idles when not exchanging data or taking a measurement. The MagI2C starts in Idle Mode at power-up._ 

The MagI2C’s register map is given in Table 5-1. Register addresses are 7 bits. To Write to a register, a ‘0’ followed by the 7-bit register number should be sent, followed by the register value. **_To Read from a register, a ‘1’ followed by the 7-bit register number should be sent, effectively adding 0x80 to the register number._** 

**Table 5-1: MagI2C Register Map** 

|**Name**|**Register #**<br>**(Hex)**|**R/W**|**Default**<br>**(Hex)**|**Payload**<br>**Format**|**Description**|
|---|---|---|---|---|---|
|POLL|00|RW|00|[7:0]|Polls for a Single Measurement|
|CMM|01|RW|00|[7:0]|Initiates Continuous Measurement Mode|
|CCX|04 – 05|RW|00C8|UInt16|Cycle Count Register – X Axis|
|CCY|06 – 07|RW|00C8|UInt16|Cycle Count Register – Y Axis|
|CCZ|08 – 09|RW|00C8|Uint16|Cycle Count Register – Z Axis|
|TMRC|0B|RW|96|[7:0]|Sets Continuous Measurement Mode Data Rate|
|MX|24 – 26|R|000000|Uint24|Measurement Results – X Axis|
|MY|27 – 29|R|000000|Uint24|Measurement Results – Y Axis|
|MZ|2A – 2C|R|000000|Uint24|Measurement Results – Z Axis|
|BIST|33|RW|00|[7:0]|Built-In Self Test|
|STATUS|34|R|00|[7:0]|Status of DRDY|
|HSHAKE|35|RW|1B|[7:0]|HandshakeRegister|
|REVID|36|R|--|Unit8|MagI2C Revision Identification|



## **5.1 Set the Cycle Count Registers (0x04 – 0x09)** 

The Cycle Count Registers establish the number of sensor oscillation cycles (cycle counts) that will be counted for each sensor in both the forward and reverse bias directions during a measurement sequence. Each sensor has its own cycle count value, and each can be different. Increasing the cycle count value increases measurement gain and resolution. Lowering the cycle count value reduces acquisition time, which increases maximum 

**PNI Sensor** 

**Doc 1017252 V14.0 Page 29 of 45** 

**RM3100 & RM2100 Magneto-Inductive Magnetometer** 



<!-- page 31 -->

achievable sample rate or, with a fixed sample rate, decreases power consumption. The Cycle Count read and write addresses, plus their default values, are given in Table 5-2 

**Table 5-2: Cycle Count Registers** 

|**Register Description**|**Default**<br>**Value (Hex)**|**Write Address**<br>**(Hex)**|**Read Address**<br>**(Hex)**|
|---|---|---|---|
|X Axis Cycle Count Value - MSB|0x00|04|84|
|X Axis Cycle Count Value - LSB|0xC8|05|85|
|Y Axis Cycle Count Value - MSB|0x00|06|86|
|Y Axis Cycle Count Value - LSB|0xC8|07|87|
|Z Axis Cycle Count Value - MSB|0x00|08|88|
|Z Axis Cycle Count Value - LSB|0xC8|09|89|



Since the registers are adjacent, it is not necessary to send multiple register addresses, as the MagI2C automatically will read/write to the next adjacent register. 

The default values for the Cycle Count Registers are 0xC8 in the LSB and 0x0 in the MSB, or 200D. This default value provides a good trade-off between acquisition time and resolution, but favors resolution. If the user is more interested in low power consumption or running at high data rates, a lower cycle count value of (ex. 50D or 100D) would be more appropriate. To estimate the appropriate cycle count value for your application review the specifications given at 50, 100, and 200 cycle counts in Table 3-1. Note that these 3 cycle counts by no means represent all the cycle count options, as the minimum value is ‘0’ and the maximum is 65,536. Having said this, quantization issues generally dictate working above a cycle count value of ~30, while noise limits the useful upper range to ~400 cycle counts. 

Assuming a non-default cycle count value is desired, then prior to sending a command to take a sensor measurement it is necessary to Write values to the Cycle Count Registers. Once the Cycle Count Registers are set, they do not need to be repopulated unless the user wants to change the values or the system is powered down, in which case the default value repopulates the register fields when powered up again. 

# **5.2 Initiate Continuous Measurement Mode (0x01)** 

The MagI2C can either take measurements automatically on a regular frequency (Continuous Measurement Mode) or by polling for single measurement. This section discusses Continuous Measurement Mode. See Section 5.3 for polling a single measurement. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 30 of 45** 



<!-- page 32 -->

To initiate Continuous Measurement Mode, write to the CMM register address, 0x01, followed by the CMM register contents. To set the rate of data acquisition in Continuous Measurement Mode, see Section 5.2.1. Below are the contents of the CMM register. 

|Bit #|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|Value|Reserved|CMZ|CMY|CMX|0|DRDM|Reserved|START|
||Set to 0||||||Set to 0||



Where: 

- START – A “1” in this bit position initiates Continuous Measurement Mode. To turn off Continuous Measurement Mode it is necessary to write a “0” to this bit position. Note that writing to POLL (i.e. initiating a single measurement command) while operating in Continuous Measurement Mode results in the single measurement command being ignored. 

- DRDM – These two bits establish the required condition to trigger the DRDY pin to HIGH. There are 4 possible conditions, as set out in Table 5-3. 

**Table 5-3: Continuous Mode DRDY Options** 

|**DRDY Requirements**|**DRDM**|
|---|---|
|DRDY to HIGH after a full measurement<br>sequence is completed, as established by<br>CMX, CMY, and CMZ.|0|
|DRDY to HIGH after the completion of a<br>measurement on any axis.|1|



- CMX, CMY, CMZ – A “1” in either of these three bit positions indicates a measurement will be taken on that sensor axis when operating in Continuous Measurement Mode. For instance, to take measurements on all three axis, CMX = CMY = CMZ = 1. 

To read from the CMM register, send 0x81. The return byte will provide the same information as above. 

**_Note:_** _Certain commands, such as reading from the CMM register or writing to the TMRC register, will terminate Continuous Measurement Mode._ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 31 of 45** 



<!-- page 33 -->

## **5.2.1 Setting the CMM Update Rate with TMRC (0x0B)** 

The time between measurements in Continuous Measurement Mode is established with the TMRC register. The TMRC register is defined below. 

|Bit #|7<br>6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Value|1<br>0|0|1|TMRC3|TMRC2|TMRC1|TMRC0|



The LSB is used set the CMM updatee rate. The MSB should be 0x9, as indicated above. The larger the TMRC value, the longer the interval between measurements. Available data rates are given in Table 5-4. Note that the update rates are approximate, and have a one standard deviation tolerance of about ~7%. The default value for TMRC is 0x96, establishing a data update rate of ~37 Hz. 

To set the TMRC register, send the register address, 0x0B, followed by the desired TMRC register value. To read the TMRC register, send 0x8B. 

**_Note:_** _The Cycle Count Registers establish the maximum data rate of the sensors. For instance, if the cycle count is set to 200D, then the maximum 3-axis update rate is ~430 Hz. If TMRC is set to 0x92, indicating an update rate of ~600 Hz, the rate established by the cycle count will override the TMRC request, and the actual update rate will be ~430 Hz._ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 32 of 45** 



<!-- page 34 -->

**Table 5-4: CMM Update Rates** 

|**TMRC Value**|**Time Between**|**Update**|
|---|---|---|
|**(Hex)**|**Readings**|**Rate**|
|92|~1.7 ms|~600 Hz|
|93|~3 ms|~300 Hz|
|94|~7 ms|~150 Hz|
|95|~13 ms|~75 Hz|
|96|~27 ms|~37 Hz|
|97|~55 ms|~18 Hz|
|98|~110 ms|~9 Hz|
|99|~220 ms|~4.5 Hz|
|9A|~440 ms|~2.3 Hz|
|9B|~0.8 s|~1.2 Hz|
|9C|~1.6 s|~0.6 Hz|
|9D|~3.3 s|~0.3 Hz|
|9E|~6.7 s|~0.15 Hz|
|9F|~13 s|~0.075 Hz|



# **5.3 Initiate a Single Measurement (0x00)** 

The MagI2C can operate in either a continuous measurement mode or a polling mode. This section discusses the Single Measurement Command used in a polling mode. See Section 5.2 for operation in continuous measurement mode. 

To make a single measurement it is necessary to write the POLL address register, 0x00, and follow this by the POLL register byte which establishes which axes are to be measured. It is defined as shown below, where a “1” for PMX, PMY, and/or PMZ indicates the X, Y, and/or Z axis, respectively, is to be measured. Note that the DRDY line will go HIGH after all measurements requested in the Single Measurement Command byte have been completed. 

|Bit #|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|Value|0|PMZ|PMY|PMX|0|0|0|0|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 33 of 45** 



<!-- page 35 -->

# **5.4 Confirm New Data Ready** 

There are several ways to determine if a measurement has been completed and data is available in the Measurement Results Registers. One method is monitoring the DRDY line for it to go HIGH. Recall that for continuous measurement mode, the DRDM bits of the Continuous Measurement Command byte establish the conditions for DRDY to go HIGH. Another option when using the SPI interface is monitoring the MISO pin for it to go HIGH. (The MISO pin is unavailable when using the I<sup>2</sup> C interface, as it is used to set the slave address of the device.) Another option is to read from the STATUS register, as discussed below. Only one method need be used. 

## **5.4.1 STATUS Register (0x34)** 

To read the Status Register, first send a read command to the STATUS register, 0xB4. 

The return byte provides the contents of the Status Register: 

|Bit #|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|Value|DRDY|-|-|-|-|-|-|-|



Bit 7 will be HIGH if data is available and LOW if it is unavailable. Bits 0 – 6 are indeterminate and should be ignored. 

# **5.5 Read the Measurement Results** 

Each sensor reading consists of 3 bytes of data which are stored in 2’s complement format (range: -8388608 to 8388607) in the Results Registers within the MagI2C and this number is directly proportional to the strength of the local magnetic field in the direction of the specified axis. Note that the greater the Period Select value, the higher the resolution of the measurement and the longer the sample time. These registers are read by sending the Read Results byte, as defined below, where the values of A, B, C, and D establish the register to be addressed, as given in Table 5-5. 

|Bit #|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|Value|1|0|1|0|A|B|C|D|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 34 of 45** 



<!-- page 36 -->

**Table 5-5: Measurement Results Registers** 

|**Register Description**|**Write Address**<br>**(Hex)**|**Read Address**<br>**(Hex)**|
|---|---|---|
|X Axis Measurement (2)|24|A4|
|X Axis Measurement (1)|25|A5|
|X Axis Measurement (0)|26|A6|
|Y Axis Measurement (2)|27|A7|
|Y Axis Measurement (1)|28|A8|
|Y Axis Measurement (0)|29|A9|
|Z Axis Measurement (2)|2A|AA|
|Z Axis Measurement (1)|2B|AB|
|Z Axis Measurement (0)|2C|AC|



Normally it is only necessary to send “A4H”, since the register value automatically increments on the clock cycles such that after sending “A4H” all 3 bytes for the X axis measurement would be clocked out, then the 3 bytes for the Y axis measurement, then the 3 bytes for the Z axis measurement. After these 9 bytes have been clocked out, the subsequent output data has no relevance. 

# **5.6 Troubleshooting and General Information** 

The MagI2C incorporates several registers that can be used to help troubleshoot the system or device. These include the Built-In Self Test (BIST) register, the Handshake register, and the RevID register. 

## **5.6.1 Built-In Self Test Register (0x33)** 

The Built-In Self Test (BIST) register checks the status of the internal LR circuit oscillator. Write to the BIST register by sending 0x33 followed by the BIST register values, and request a read from the BIST register by sending 0xB3. The register contents are defined below. 

|Bit #|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|Value|STE|ZOK|YOK|XOK|BW1|BW0|BP1|BP0|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 35 of 45** 



<!-- page 37 -->

Where: 

- STE – Setting this to ‘1’ commands the MagI2C to run the built-in self test when the POLL register is written to. The end of the built-in self test sequence will be indicated by DRDY going HIGH. 

- ZOK, YOK, and XOK – These read-only bits indicate whether or not the X, Y, and Z LR oscillators functioned correctly during the built-in self test. A ‘1’ indicates a properly function oscillator. Note that STE also should be HIGH when this is read, or the reading is invalid. 

- BW – These two bits define the timeout period for the LR oscillator periods, as given in Table 5-6. 

**Table 5-6: BIST Timeout Period** 

|**BIST Wait Time**|**BW1**|**BW0**|
|---|---|---|
|Unused|0|0|
|1 Sleep Oscillation Cycle (30 µs)|0|1|
|2 Sleep Oscillation Cycles (60 µs)|1|0|
|4 Sleep Oscillation Cycles (120 µs)|1|1|



- BP – These two bits define the number of LR periods for measurement during the built-in self test, as given in Table 5-7. 

**Table 5-7: BIST LR Periods** 

|**BIST LR Periods**|**BW1**|**BW0**|
|---|---|---|
|Unused|0|0|
|1 LR Period|0|1|
|2 LR Periods|1|0|
|4 LR Periods|1|1|



- An example of the register read and write sequence for a complete BIST operation is given in the flowchart, figure 5-1, below. Note that in this example a 10ms delay is used as an alternative to polling the DRDY pin or DRDY bit in the STATUS register. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 36 of 45** 



<!-- page 38 -->



_Figure 5-1: - Full BIST sequence using a timer to wait for BIST completion_ 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 37 of 45** 



<!-- page 39 -->

# **5.6.2 HSHAKE Register (0x35)** 

The HSHAKE register is used to set conditions for clearing the DRDY pin and for determining why a register command was not fulfilled. Write to the HSHAKE register by sending 0x35 followed by the BIST register values, and request a read from the HSHAKE register by sending 0xB5. The register contents are defined below. 

|Bit #|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|Value|0|NACK2|NACK1|NACK0|1|0|DRC1|DRC0|



Where: 

- DRC0 – Setting this to ‘1’ means DRDY is cleared by any device register write. Clearing occurs during reception of the register address byte for the write transaction on either the SPI or I<sup>2</sup> C interface. This is the default setting. 

- DRC1 – Setting this to ‘1’ means DRDY is cleared by reading the Measurement Results registers. Clearing occurs when the MagI2C sends back the first byte of data. This is the default setting. 

- NACK0 – This read-only bit is set to ‘1’ when writing to an undefined register. 

- NACK1 – This read-only bit is set to ‘1’ when writing into POLL when CMM is in progress or when writing to CMM when POLL is in progress. 

- NACK2 – This read-only bit is set to ‘1’ when a read for the Measurement Results registers is requested but data is not ready (DRDY = 0). 

# **5.6.3 REVID Register (0x36)** 

The REVID register provides revision identification of the MagI2C. This is a single byte, read-only register. To read the REVID register, send 0xB6. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 38 of 45** 



<!-- page 40 -->

# **5.7 Examples using the SPI Interface** 

## **5.7.1 Set the Cycle Count Registers** 

A sample command sequence is provided below which sets the cycle count value to 100D (64H) for all 3 axes. This is purely for illustrative purposes and the value could be different and/or the number of axes to be addressed could be different. 

- Start with SSN set HIGH, then set SSN to LOW. 

- Send 04H (this is the Write Command Byte to address the MSB for the X axis) 

- Send 0 (value for the MSB for the X axis) 

- Send 64H (value for the LSB for the X axis - pointer automatically increments) 

- Send 0 (value for the MSB for the Y axis - pointer automatically increments) 

- Send 64H (value for the LSB for the Y axis - pointer automatically increments) 

- Send 0 (value for the MSB for the Z axis - pointer automatically increments) 

- Send 64H (value for the LSB for the Z axis - pointer automatically increments) 

- Set SSN to HIGH 

## **5.7.2 Making and Reading Measurements** 

Figure 5-1 gives the SPI activity sequence for initiating a single measurement and reading the results. The MagI2C works for either CPOL=CPHA=0 or CPOL=CPHA=1, so both cases are given. The assumption in the diagram is that the DRDY pin or the MISO line is used to establish when data is ready, but a query of the Status Register could be used instead. SPI timing requirements are discussed in Section 4.4. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 39 of 45** 



<!-- page 41 -->



_Figure 5-2: SPI Activity Sequence Diagram_ 

The steps to make measurements in Continuous Measurement Mode are given below. 

- Start with SSN set HIGH, then set SSN to LOW. 

- Initiate Continuous Measurement Mode by writing to the CMM register address, 0x01, followed by the CMM register value. This value defines which axes are to be measured, how the DRDY line will be set HIGH. Assuming all 3 axes are to be measured, DRDY goes HIGH after completing measurements on all axes, the CMM value would be 0x79. 

- The RM3100 Evaluation Board will now initiate Continuous Measurement Mode. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 40 of 45** 



<!-- page 42 -->

- Return SSN to HIGH. This will not affect the measurement process, but will free up the host to communicate with other devices and ensure the next write command sent to the module is interpreted properly. 

- Once the measurement sequence is completed on all axes the MISO pin goes low and the DRDY pin is set HIGH, assuming 0x79 is the CMM register value. The module will be placed in Idle Mode until it is time to take another measurement, as defined by the TMRC register. 

- When the host is ready to read the measured values, set SSN to LOW. If SSN already is LOW, then toggle SSN from LOW to HIGH to LOW. 

- Assuming the X axis was one of the axes to be measured, send the MX2 Read address, 0xA4, to begin reading the Measurement Results registers. The measurement readings will now clock out, with the 3 bytes of X-axis data presented first, then Y-axis data, then Z-axis data. The first nine (9) bytes represent a complete 3-axis measurement. This will clear the DRDY line. 

- Return SSN to HIGH to free up the host to communicate with other devices and to ensure the next Command Byte sent to the module is interpreted properly. 

The steps to make a single measurement are given as follows. 

- Start with SSN set HIGH, then set SSN to LOW. 

- Initiate a single measurement by writing to the POLL register address, 0x00, followed the register address with either the POLL register value. This defines which axes are to be measured, and should be 0x70 if measurements on all three axes are desired. 

- The MagI2C will now take the prescribed measurements. 

- Return SSN to HIGH. This will not affect the measurement process, but will free up the host to communicate with other devices and ensure the next write command sent to the MagI2C is interpreted properly. 

- Once the measurement sequence is completed on all desired axes, the DRDY pin is set HIGH and the MISO pin goes low, indicating data is read. The MagI2C is placed in Idle Mode. 

- When the host is ready to read the measured values, set SSN to LOW. If SSN already is LOW, then toggle SSN from LOW to HIGH to LOW. 

- Assuming the X axis was one of the axes to be measured, send the MX2 Read address, 0xA4, to begin reading the Measurement Results registers. The measurement readings will now clock out, with the 3 bytes of X-axis data presented first, then Y-axis data, then Z-axis data. The first nine (9) bytes represent a complete 3-axis measurement. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 41 of 45** 



<!-- page 43 -->

- Return SSN to HIGH to free up the host to communicate with other devices and to ensure the next Command Byte sent to the MagI2C is interpreted properly. 

# **5.8 Examples using the I**<sup>**2**</sup> **C Interface** 

### **5.8.1 Set the Cycle Count Registers** 

A sample command sequence is provided below which sets the cycle count value to 100D (64H) for all 3 axes. This is for illustrative purposes and the value could be different and/or the number of axes to be addressed could be different. Note only the initial Cycle Count register address needs to be sent, as the MagI2C automatically increments to the next register. 



From Host to MagI2C From MagI2C to Host 



### **5.8.2 Initiate a Single Measurement** 

The I<sup>2</sup> C transactions to initiate a single measurement on all 3 axes are given below. 

START MagI2C ADDRESS RW ACK POLL REG. ADDRESS (N) ACK DATA TO POLL REG (N) ACK STOP S 0 1 0 0 0 X X 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 P 

From Host to MagI2C From MagI2C to Host 

After this transaction sequence the MagI2C will initiate a measurement sequence, and this can run in the background. At the end of the measurement sequence the DRDY pin is set HIGH and the Status Register will have a “1” in bit 7, indicating data is ready. The MagI2C will be placed in Idle Mode. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 42 of 45** 



<!-- page 44 -->

### **5.8.3 Initiate Continuous Measurement Mode** 

A sample I<sup>2</sup> C transaction to initiate continuous measurement mode is given below. 



<!-- Start of picture text -->
START  MagI2C ADDRESS  RW ACK  CMM REG. ADDRESS (N)  ACK  DATA TO CMM REG (N)  ACK STOP<br>S 0 1 0 0 0 X X 0 0 0 0 0 0 0 0 0 1 0 0 1 1 1 1 0 0 1 0 P<br><!-- End of picture text -->

From Host to MagI2C From MagI2C to Host 

In this example, the CMM register is set to initiate measurements on all 3 axes, and to set DRDY to HIGH after all three measurements are made. 

### **5.8.4 Read the Measurement Results** 

When the host is ready to read the Measurement Results registers, the following transactions should occur. Note only the initial Measurement Results register address needs to be sent, as the MagI2C automatically increments to the subsequent registers. 



From Host to MagI2C From MagI2C to Host 



DATA FROM MX0 REG (N+2) ACK DATA FROM MY2 REG (N+3) ACK DATA FROM MY1 REG (N+4) ACK DATA FROM MY0 REG (N+5) ACK X X X X X X X X 0 X X X X X X X X 0 X X X X X X X X 0 X X X X X X X X 0 

DATA FROM MZ2 REG (N+6) ACK DATA FROM MZ1 REG (N+7) ACK DATA FROM MZ0 REG (N+8) NACK STOP 



The final NACK is optional, as communication will stop by simply implementing the Stop condition. 

**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 43 of 45** 



<!-- page 45 -->

## Revision Control Block 

|**Revision**|**Description of Change**|**Effective Date**|**Approval**|
|---|---|---|---|
|R03|Added Revision Control Block. On Figures 4-1 and 4-2,<br>changed pins 2 and 20 to “RES” from “GND”, and changed<br>Table 4-1 appropriately. In Section 4.2.3, indicated the<br>MagI2C should be within 10 cm of the sensors, not 0.5 m||A. Leuzinger|
|R04|Correction to cycle count command example|06/05/15|D. McKenzie|
|R05|Removal of “Alarm” feature described in section 5.2.2 of<br>previous revision|02/01/16|D. McKenzie|
|R06|Updated Figure 3-7 to indicate that the exposed die pad in the<br>center of the ASIC should not be soldered and should remain<br>unconnected|02/24/16|D. McKenzie|
|R07|Correction to Figure 4-4: RM3100 North-East-Down (NED)<br>Sensor Layout|06/24/16|J. Back|
|R08|Added information to document about RM2100|09/14/22|H. Nguyen|
|R09|Revised<sup>t</sup>DRDV|12/14/22|J. Miller|
|R10|Added MagI2C PCB Pad Pattern and updated logo|2/26/24|H. Nguyen|
|R11|Updated Table 5-4 to fix a typo for data rate at TMRC value 9E|4/8/24|H. Nguyen|
|R12|Changed name of document from RM3100 Sensor Suite to<br>RM3100 Magneto-Inductive Magnetometer|4/9/24|H. Nguyen|
|R13|Updated Section 4.3.3 to fix error with SA0 and SA1 pins|6/5/24|H. Nguyen|
|R14|Updated Figure 3-6 to change 0.325mm clearance to corrected<br>0.3mm|7/31/25|H. Nguyen|



**PNI Sensor RM3100 & RM2100 Magneto-Inductive Magnetometer** 

**Doc 1017252 V14.0 Page 44 of 45** 

