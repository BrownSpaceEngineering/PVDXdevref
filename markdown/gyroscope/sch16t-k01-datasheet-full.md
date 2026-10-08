# sch16t-k01-datasheet-full

*Source: `original/gyroscope/sch16t-k01-datasheet-full.pdf` (65 pages)*

<!-- page 1 -->



## **6-DOF Gyroscope and Accelerometer with Digital SPI Interface** 

## **Features** 

- Gyroscope measurement range ±300 °/s 

- Accelerometer measurement range ±80 m/s² m/s² with default dynamic range of ±260 m/s² 

- Options for output interpolation and decimation 

- Angular rate and acceleration low pass filters from 13 Hz to 370 Hz cut-off rate 

- Data Ready output, timestamp index and SYNC input functions for clock domain synchronization 

- -40...110 °C operating temperature range 

- 3.0...3.6 V supply voltage, 1.7…3.6 V I/O supply voltage 

- SafeSPI v2.0 interface 

- 20-bit and 16-bit output data, selectable via SPI frame 

- Advanced self-diagnostic system automatically reports sensor status in every SPI frame, leveraging over 200 internal monitoring signals 

- 11.8 mm x 13.4 mm x 2.9 mm (l x w x h) SOIC-24 

- Qualification based on AEC-Q100 standard 

- Supports system level safety classification 

## **Applications** 

SCH16T-K01 is targeted at applications demanding high performance with tough environmental requirements. Typical applications include: 

- Inertial measurement units (IMUs) 

- Inertial navigation and positioning 

- Machine control and guidance 

- Dynamic inclination 

- Robotic control and UAVs 

### Application restriction 

- <u>https://www.murata.com/en-global/support/militaryrestriction</u> 

## **Overview** 

The SCH16T-K01 is a combined high-performance 3-axis angular rate and 3-axis accelerometer. The angular rate and accelerometer sensor elements are based on Murata's proven capacitive 3D-MEMS technology. Signal processing is done by a single mixed-signal ASIC that provides angular rate and acceleration via a flexible SafeSPI v2.0 compliant digital interface. Sensor elements and ASIC are packaged to pre-molded SOIC 24-pin plastic housing that guarantees reliable operation over the product's lifetime. 

The SCH16T-K01 is designed, manufactured, and tested for high stability, reliability, and quality requirements. The component has extremely stable output over temperature, humidity, and vibration. The component has several advanced self-diagnostic features, is suitable for SMD mounting and is compatible with RoHS and ELV directives. 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 2 -->



2 (65) 

# **_TABLE OF CONTENTS_** 

|**1**<br>**Int**|**roduction ................................................................................................................................. 4**|
|---|---|
|**2**<br>**Pr**|**oduct and packing quantity information ............................................................................... 4**|
|**3**<br>**Sp**|**ecifications ............................................................................................................................. 4**|
|3.1|Abbreviations ......................................................................................................................... 4|
|3.2|General specifications ............................................................................................................ 5|
|3.3|Absolute maximum ratings ..................................................................................................... 5<br>|
|3.4<br>|Gyroscope performance specifications .................................................................................. 6<br>|
|3.5|Accelerometer performance specifications ............................................................................. 8|
|3.6|Gyroscope typical performance characteristics .................................................................... 10|
|3.7|Accelerometer typical performance characteristics .............................................................. 11|
|3.8|Temperature sensor performance specifications .................................................................. 12|
|3.9|Gyroscope and accelerometer frequency response and filter characteristics ....................... 13|
|3.10|Pin description ..................................................................................................................... 14|
|3.11|Digital I/O specification ........................................................................................................ 16|
|3.12|<br> SPI AC characteristics ......................................................................................................... 16|
|3.13|Measurement axis and directions......................................................................................... 18|
|3.14|Package outline and dimensions ......................................................................................... 19|
|3.15|PCB footprint ....................................................................................................................... 20|
|**4**<br>**Ge**|**neral product description .................................................................................................... 21**|
|4.1|Component block diagram ................................................................................................... 21|
|4.2|Accelerometer...................................................................................................................... 22|
|4.3|Gyroscope ........................................................................................................................... 22|
|4.4|Factory calibration ............................................................................................................... 22|
|**5**<br>**Co**|**mponent operation, reset and power-up ............................................................................ 22**|
|5.1|Component operation .......................................................................................................... 22|
|5.2|Start-up sequence ............................................................................................................... 22|
|5.3|Component output options ................................................................................................... 24|
|5.4|Solutions for asynchronous clock domains .......................................................................... 25|
|5.4|.1<br>Interpolation .................................................................................................................. 25|
|5.4|.2<br>Decimation .................................................................................................................... 26|
|5.4|.3<br>SYNC input pin ............................................................................................................. 27|
|5.4|.4<br>Data Ready, DRY ......................................................................................................... 28|
|5.4|.5<br>Data counter ................................................................................................................. 29|
|5.4|.6<br>Frequency counter ........................................................................................................ 29|
|5.4|.7<br>Time stamp ................................................................................................................... 29|
|5.5|Recommended reading procedure for sensor data .............................................................. 30|
|5.6|Diagnostics flags and status behavior .................................................................................. 31|
|**6**<br>**Co**|**mponent interfacing ............................................................................................................. 32**|
|6.1|Safe SPI .............................................................................................................................. 32|
|6.2|SPI frame structure .............................................................................................................. 34|
|6.3|Multi-slave operation ............................................................................................................ 35|
|6.4|SPI frame status bits ............................................................................................................ 36|
|6.5|Cyclic redundancy check (CRC) .......................................................................................... 38|
|6.5|<br>.1<br>SPI48BF CRC .............................................................................................................. 39|
|6.5|.2<br>SPI32BF CRC .............................................................................................................. 39|
|6.6|Operations ........................................................................................................................... 40|
|**7**<br>**Re**|<br>**gister definition .................................................................................................................... 41**|
|<br>7.1|<br>Register map user guide ...................................................................................................... 41|
|7.1|<br>.1<br>Value and address formats ........................................................................................... 41|
||**Murata Electronics O**<br>SCH16T<br>DocNo 11624|
||**y**<br> <br>..<br>www.murata.com<br>Rev. 6|



Doc.No. 11624 Rev. 6 



<!-- page 3 -->





|7.1.2|Register map overview ................................................................................................. 42|
|---|---|
|7.2<br>Se<br>|nsor data block ................................................................................................................ 44<br>|
|7.2.1|Example of angular rate data conversion ...................................................................... 45<br>|
|7.2.2|Example of acceleration data conversion ...................................................................... 45|
|7.2.3<br>|Example of temperature data conversion ...................................................................... 46<br>|
|7.3<br>Se|nsor status and counter block .......................................................................................... 47|
|7.3.1|Data counters ............................................................................................................... 47|
|7.3.2<br>|Frequency counter / timestamp ..................................................................................... 48<br>|
|7.3.3<br>|Status summary ............................................................................................................ 48<br>|
|7.3.4|Saturation status summary ........................................................................................... 49|
|7.3.5|Common status............................................................................................................. 49|
|7.3.6|Gyroscope common status ........................................................................................... 50|
|7.3.7|Gyroscope status XYZ .................................................................................................. 50|
|7.3.8|Accelerometer status XYZ ............................................................................................ 51|
|7.3.9<br><br>|Additional status registers ............................................................................................. 53<br>|
|7.4<br>Se|nsor control block ............................................................................................................ 54|
|7.4.1|Filter settings ................................................................................................................ 55|
|7.4.2|Dynamic range and decimation ..................................................................................... 56|
|7.4.3|Saturation flag user control ........................................................................................... 57|
|7.4.4|User interface control .................................................................................................... 59|
|7.4.5<br>|Self-test controls ........................................................................................................... 61<br>|
|7.4.6|Sensor mode control and soft reset .............................................................................. 61|
|7.4.7|Whoami, traceability, identification, and spare registers ................................................ 62|
|**8**<br>**Applic**|**ation information ............................................................................................................ 64**|
|8.1<br>Ap|plication circuitry and external component characteristics................................................ 64|
|8.2<br>G|eneral application PCB layout ........................................................................................... 65|
|8.3<br>As|sembly instructions .......................................................................................................... 65|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 4 -->



4 (65) 

# **1 Introduction** 

This document contains essential technical information about the SCH16T series sensor including specifications, SPI interface descriptions, user-accessible register details, electrical properties, and application information. This document should be used as a reference when designing in the SCH16T series sensor. 

# **2 Product and packing quantity information** 

Table 1 Murata offers products in different packing sizes and types 

|**Product**<br>**series**|**Part number**|**Description**|**Part number with**<br>**packing mark**|**Packing type**|**Quantity**|
|---|---|---|---|---|---|
|||6-DOF Gyroscope and|SCH16T-K01-PCB|Sample package,|1 pc|
|SCH16T|SCH16TK01|<br>Accelerometer with Digital SPI|SCH16T-K01-004|Bulk|4 pcs|
||-|Interface, Gyroscope ±300 °/s,<br>²|SCH16T-K01-1|Tape & Reel|100 pcs|
|||Accelerometer ±80 m/s|SCH16T-K01-10|Tape & Reel|1000 pcs|



# **3 Specifications** 

## **3.1** 

## **Abbreviations** 

|ACC|Accelerometer|
|---|---|
|ARS|Angular Rate Sensor (gyroscope)|
|ASIC|Application Specific Integrated Circuit|
|AEC-Q100|Automotive Electronics Council Failure Mechanism Based Stress Test<br>Qualification For Integrated Circuits|
|CS|Chip Select|
|DOF|Degrees of Freedom|
|DPS|Degrees per Second|
|DRY|Data Ready|
|F_PRIM|Gyroscope Primary Frequency|
|FIFO|First In First Out|
|FREQ|Frequency|
|Gyro|Gyroscope|
|LPM|Low Power Mode|
|LPF|Low-Pass Filter|
|MCLK|Master Clock|
|MCU|Microcontroller Unit|
|MEMS|Micro-Electro-Mechanical System|
|MISO|Master In Slave Out|
|MOSI|Master Out Slave In|
|MSL3|Moisture Sensitivity Level 3 (Moisture and reflow preconditioning)|
|ODR|Output Data Rate|
|PD|Pull Down|
|POR|Power on Reset|
|PU|Pull Up|
|RT|Room Temperature 25 °C|
|SCK|<br>Serial Clock|
|SPI|Serial Peripheral Interface|
|SYNC|<br>Synchronization|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 5 -->



5 (65) 

## **3.2 General specifications** 

Table 2 General specifications 

|**Parameter**|**Min**|**Nom**|**Max**|**Unit**|
|---|---|---|---|---|
|Operating temperature<sup>(1</sup>|-40||110|°C|
|Supply voltage|3.0|3.3|3.6|V|
|Digital I/O supply<sup>(2</sup>|1.7||3.6|V|
|Total supply current|36|41|47|mA|
|Low power mode current consumption|||10|mA|
|Gyro primary frequency, F_PRIM|22.1|23.6|25.1|kHz|
|Output update rate (ODR) - Interpolated outputs (F_PRIM X 16)|353.6|377.6|401.6|kHz|
|Output update rate (ODR) - Decimated outputs||23.6/X<sup>(3</sup>||kHz|
|Component master clock, MCLK||1024 x F_PRIM||kHz|
|Turn on time<sup>(4</sup>|||250|ms|
|Weight||0.612||gram|
|Threshold of Power On Reset (POR) POR_TH_H/L for supply<br>voltage|2.4||2.9|V|
|Threshold of Power On Reset (POR) POR_TH_H/L for digital I/O<br>supply voltage|1.2||1.55|V|
|POR hysteresis window, difference between POR levels when<br>voltage drops or rises. Applies for both supply and digital I/O supply<br>voltage|0.125||0.3|V|



- 1) Specifications are valid within the temperature range 

- 2) Can exceed supply voltage 

- 3) Decimation ratio X is selectable from the following options: 2, 4, 8, 16 and 32 

- 4) After voltage supplies are within specification 

## **3.3 Absolute maximum ratings** 

Murata guarantees sensor operation without parameter related damage or functional deviation within these maximum ratings. However, output values are specified only for conditions specified in the chapters _Gyroscope performance specifications_ and _Accelerometer performance specifications._ All voltages are related to the potential at GND. 

Table 3 Absolute maximum ratings 

|**Parameter**|**Remark**|**Min**|**Nom**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Supply voltage|Supply voltage (pins V3P3, VDDIO)|-0.3||3.63|V|
|Storage<br>temperature|No damage to the component will occur up to max 24 hours within<br>these maximum ratings|-50||150|°C|
|Mechanical shock|t ≤ 0.5 ms, XYZ Axis. Tested according to AEC-Q100 requirements.|3000|||g|
|Drop test|Drop to concrete surface, tested according to AEC-Q100<br>requirements.|1.2|||m|
|ESD_HBM|ESD according to Human Body Model (HBM), Q100-002|2000|||V|
|ESD_CDM center<br>pins|Center pins<br>ESD according to Charged Device Model (CDM), Q100-011|500|||V|
|ESD_CDM corner<br>pins|corner pins<br>ESD according to Charged Device Model (CDM), Q100-011|750|||V|
|Ultrasonic agitation|Cleaning, welding, etc.||Prohibited|||



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 6 -->



6 (65) 

## **3.4 Gyroscope performance specifications** 

Table 4 Performance specifications are valid for all measurement axes, up to ±300 °/s measurement range on all outputs, supply voltage = 3.3 V and at 25 °C unless otherwise specified 

|**Parameter**|**Condition**|**Min**<br>**(-3 σ)**|**Typical**|**Max**<br>**(+3 σ)**|**Unit**|
|---|---|---|---|---|---|
|Dynamic range<sup>A)</sup>|Default sensitivity||±327.68||°/s|
|Offt<sup>B)</sup>|XY axis, -40 °C ... +110 °C|-0.3|±0.1|0.3|°/|
|se|Z axis, -40 °C ... +110 °C|-0.1|±0.01|0.1|s|
|Offset drift over lifetime<sup>C)</sup>|After HTOL 1000 h|-0.05||0.05|°/s|
|ff f<sup>D)</sup>|-40 °C ... +85 °C, 0.5 K/min|-0.01||0.01|°|
|Oset drit velocity|-40 °C ... +85 °C, 5 K/min|-0.05||0.05|(/s)/min|
|<sup>E)</sup>|Nominal value, 16-bit mode||100||°|
|Default sensitivity|Nominal value, 20-bit mode||1600||LSB/(/s)|
|Sensitivity error<sup>F)</sup>|-40 °C ... +110 °C|-0.25|±0.05|0.25|%|
|Sensitivity error drift over<br>lifetime<sup>G)</sup>|After HTOL 1000 h|-0.2||0.2|%|
|Liit<sup>H)</sup>|±300 °/s, -40 °C ... +110 °C|-0.15|±0.05|0.15|°/|
|neary error|±100 °/s, -40 °C ... +110 °C|-0.04|±0.01|0.04|s|
||XY axis||0.0004||°√|
|Noise density|Z axis||0.0006||(/s)/Hz|
|<sup>I)</sup>|XY axis||0.015||°√|
|Angle random walk|Z axis||0.025||/h|
|Bias instability<sup>J)</sup>|Allan deviation minimum divided by 0.664||0.3|0.5|°/h|
|<sup>K)</sup>|-40 °C ... +110 °C, orthogonality error<br>between rate axes|-0.15||0.15||
|Cross-axis sensitivity|-40 °C ... +110 °C, absolute to package<br>reference|-1||1|%|
|G-sensitivity<sup>L)</sup>|For constant gravity input|-0.00075||0.00075|(°/s)/g|



Notes: 

- Specified Min/Max values contain ±3 sigma variation limits of original test population. Typical values are validation population mean (unless otherwise specified). Min/Max and typical values are not guaranteed, values represent validation population characteristics. 

- Specification is valid after 24 hours from reflow. 

- Each system design including SCH16T series component must be evaluated by the customer in advance to guarantee proper functionality during operation. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 7 -->





<!-- Start of picture text -->
7 (65)<br><!-- End of picture text -->

Table 5 Gyroscope parameter definitions 

|**Symbol**<br>A)|**Description**<br>Measurement range is the rotation speed range where the performance specifications are valid.<br>Dynamic range is the sensor output range where the output is not saturated. Output saturation is indicated by<br>saturation flags documented in chapter_7.3.4 Saturation status summary._<br>Dynamic and measurement ranges are affected by user configurable sensitivity settings.|
|---|---|
|B)|Offset is the sensor output deviation from zero at zero rate and acceleration.<br>Offset over temperature is determined over one temperature sweep in the specified temperature range.|
|C)|Offset drift over lifetime is estimated from offset drift from initial offset before MSL3 treatment to offset after 1000<br>hours of high temperature operating life (HTOL) test at 125 °C and maximum supply voltages.|
|D)|Offset drift velocity is the change rate of the zero-rate offset for predefined temperature gradients within a specified<br>temperature range.|
||Default sensitivity used in factory calibration. Sensitivity is affected by user configurable sensitivity settings defined<br>in chapter_7.4.2 Dynamic range and decimation_<br>Sensitivity =<sup>ARmeas(Ωmax) −ARmeas(Ωmin)</sup><br>|
|E)|Ωmax−Ωmin<br>Where:<br>Ωmax= applied angular rate at 100 °/s<br>Ωmin= applied angular rate at -100 °/s<br>ARmeas(Ωn) = measured angular rate at Ωn[LSB]<br>Sensor outputs data in 2’s complement format.|
|F)|Sensitivity error =<sup>Sensitivity −nominal sensitivity</sup><br>nominal sensitivity<br>× 100 %<br>Sensitivity error over temperature is determined over one temperature sweep in specified temperature range.|
|G)|Sensitivity error drift over lifetime is estimated from sensitivity drift during 1000 hours of high temperature operating<br>life (HTOL) test at 125 °C and maximum supply voltages. Drift in percentage points.|
|H)|Linearity error is the maximum deviation from the best fit straight line defined by the measured values at the<br>specified range end points. Best fit linear model uses a least-squares linear fit.|
|I)|Angle random walk is the white noise term estimated from Allan deviation at tau = 1 s.|
|J)|Bias instability is the Allan deviation minimum divided by 0.664. Measured with 13 Hz low pass filter setting, 200 Hz<br>sample rate and fifteen-minute stabilization time before data collection starts to permit full thermal stabilization.|
||Cross-axis sensitivity is the sensitivity on axes other than the intended axis of rotation.<br>Cross −axis sensitivity =<sup>ARmeas</sup><br>Ω𝑜𝑡ℎ𝑒𝑟<br>× 100 %|
|K)|Where:<br>Ωother= applied angular rate along an axis other than the measured axis<br>ARmeas= the measured angular rate<br>Murata calibrates gyroscope and accelerometer axes at component calibration line and therefore orthogonality error<br>is the residual cross-axis error after system level orientation against fixed acceleration (gravity).|
|L)|Angular rate offset sensitivity in respect to orientation in the earth gravitation. This value is only measured from<br>orientations that are not affected by the earth’s rotation (0.004 °/s) and therefore, is not verified in all orientations.<br>Can not be extrapolated beyond gravitation.|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 8 -->



8 (65) 

# **3.5 Accelerometer performance specifications** 

Table 6 Performance specifications are valid for all measurement axes, up to ±80 m/s<sup>2</sup> measurement range on all outputs (default and auxiliary), supply voltage = 3.3 V and at 25 °C unless otherwise specified 

|**Parameter**|**Condition**|**Min**<br>**(-3 σ)**|**Typical**|**Max**<br>**(+3 σ)**|**Unit**|
|---|---|---|---|---|---|
||Default output, default sensitivity||±163.84|||
|Dynamic range<sup>A)</sup>|Auxiliary accelerometer output,<br>default sensitivity|±260|||m/s<sup>2</sup>|
|Offt<sup>B)</sup>|-40 °C ... +110 °C, zeroed drift from 25 °C|-0.04|±0.01|0.04|/<sup>2</sup>|
|se|-40 °C ... +110 °C|-0.06|±0.02|0.06|ms|
|Offset drift over lifetime<sup>C)</sup>|After HTOL 1000 h|-0.02||0.02|m/s<sup>2</sup>|
|Offt dift lit<sup>D)</sup>|-40 °C ... +110 °C, 0.5 K/min|-0.002||0.002|/<sup>2</sup>/i|
|se r veocy|-40 °C ... +110 °C, 5 K/min|-0.005||0.005|(ms)mn|
|Default sensitivit<sup>E)</sup>|Nominal value, 16-bit mode||200||LSB/(m/s<sup>2</sup>)|
|y|Nominal value, 20-bit mode||3200|||
|Default sensitivity for auxiliary|Nominal value, 16-bit mode||100||LSB//<sup>2</sup>|
|accelerometer output<sup>E)</sup>|Nominal value, 20-bit mode||1600||(ms)|
|Sensitivity error<sup>F)</sup>|-40 °C ... +110 °C|-0.1|±0.05|0.1|%|
|Sensitivity error drift over<br>lifetime<sup>G)</sup>|After HTOL 1000 h|-0.03||0.03|%|
|Lii<sup>H)</sup>|±80 m/s<sup>2</sup>, -40 °C ... +110 °C|-0.15|±0.03|0.15|/<sup>2</sup>|
|nearty error|±10 m/s<sup>2</sup>, -40 °C ... +110 °C|-0.01|±0.005|0.01|ms|
|Noise density|||0.8||(mm/s<sup>2</sup>)/√𝐻𝑧|
|Velocity random walk<sup>I)</sup>|||30||(mm/s)/√ℎ|
|Bias instability<sup>J)</sup>|Allan deviation minimum divided by 0.664||0.15|0.3|mm/s<sup>2</sup>|
|<sup>K)</sup>|-40 °C ... +110 °C, orthogonality error<br>between ACC axes|-0.15||0.15||
|Cross-axis sensitivity|-40 °C ... +110 °C, absolute to package<br>reference|-1||1|%|



Notes: 

- Specified Min/Max values contain ±3 sigma variation limits of original test population. Typical values are validation population mean (unless otherwise specified). Min/Max and typical values are not guaranteed, values represent validation population characteristics. 

- Specification is valid after 24 hours from reflow. 

- Each system design including SCH16T series component must be evaluated by the customer in advance to guarantee proper functionality during operation. 

- A factor of 102 can be used when converting m/s<sup>2</sup> to milli-g. Actual gravity depends on sensor location on Earth. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 9 -->



9 (65) 

Table 7 Accelerometer parameter definitions 

|**Symbol**|**Description**|
|---|---|
|A)|Measurement range is the acceleration range where the performance specifications are valid.<br>Dynamic range is the sensor output range where the output is not saturated. Output saturation is indicated by<br>saturation flags documented in chapter_7.3.4 Saturation status summary._<br>Dynamic and measurement ranges are affected by user configurable sensitivity settings.|
|B)|Offset is the sensor output deviation from zero at zero rate and acceleration.<br>Offset over temperature is determined over one temperature sweep in the specified temperature range.<br>Offset =<br>ACCmeas(a+1g)+ ACCmeas(a−1g)<br>2<br>a+1g= applied acceleration at +1 g (i.e., +1 g gravity of manufacturing location)<br>a-1g= applied acceleration at -1 g (i.e., -1 g gravity of manufacturing location)<br>ACCmeas(an) = measured acceleration at an[m/s<sup>2</sup>]|
|C)|Offset drift over lifetime is estimated from offset drift from initial offset before MSL3 treatment to offset after 1000<br>hours of high temperature operating life (HTOL) test at 125 °C and maximum supply voltages.|
|D)|Offset drift velocity is the change rate of the zero-acceleration offset for predefined temperature gradients within a<br>specified temperature range.|
||Default sensitivity used in factory calibration. Sensitivity is affected by user configurable sensitivity settings defined<br>in chapter_7.4.2 Dynamic range and decimation_<br>Sensitivit =<br>ACCmeas(a+1g)−ACCmeas(a−1g)|
|E)|y<br>a+1g−a−1g<br>a+1g= applied acceleration at +1 g (i.e., +1 g gravity of manufacturing location)<br>a-1g= applied acceleration at -1 g (i.e., -1 g gravity of manufacturing location)<br>ACCmeas(an) = measured acceleration at an[LSB]<br>Sensor outputs data in 2’s complement format.|
|F)|Sensitivity error =<sup>Sensitivity −nominal sensitivity</sup><br>nominal sensitivity<br>× 100 %<br>Sensitivity error over temperature is determined over one temperature sweep in specified temperature range.|
|G)|Sensitivity error drift over lifetime is estimated from sensitivity drift during 1000 hours of high temperature operating<br>life (HTOL) test at 125 °C and maximum supply voltages. Drift in percentage points.|
|H)|Linearity error is the maximum deviation from the best fit straight line defined by the measured values at the<br>specified range end points. Best fit linear model uses a least-squares linear fit.|
|I)|Velocity random walk is the white noise term estimated from Allan deviation at tau = 1 s.|
|J)|Bias instability is the Allan deviation minimum divided by 0.664. Measured with 13 Hz low pass filter setting, 200 Hz<br>sample rate and fifteen-minute stabilization time before data collection starts to permit full thermal stabilization.|
||Cross-axis sensitivity is the sensitivity on axes other than the intended axis of acceleration.<br>Cross −axis sensitivity =<sup>ACCmeas</sup><br>a𝑜𝑡ℎ𝑒𝑟<br>× 100 %|
|K)|Where:<br>aother= applied acceleration along an axis other than the measured axis<br>ACCmeas= the measured acceleration<br>Murata calibrates gyroscope and accelerometer axes at component calibration line and therefore orthogonality error<br>is the residual cross-axis error after system level orientation against fixed acceleration (gravity).|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 10 -->



10 (65) 

# **3.6 Gyroscope typical performance characteristics** 



<!-- Start of picture text -->
X-Axis  Y-Axis  Z-Axis<br>Offset (°/s) 3 σ population limits<br>Offset drift over lifetime (HTOL 1000 h) (°/s) 3 σ population limits (25 °C)<br>Sensitivity error (%) 3 σ population limits<br>Allan Deviation (°/h)<br><!-- End of picture text -->

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 11 -->



11 (65) 

# **3.7 Accelerometer typical performance characteristics** 



<!-- Start of picture text -->
X-Axis  Y-Axis  Z-Axis<br>Offset (mg) 3 σ population limits<br>Offset drift over lifetime (HTOL 1000 h) (mg) 3 σ population limits<br>Sensitivity error (%) 3 σ population limits<br>Allan Deviation (mm/s 2 )<br><!-- End of picture text -->

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 12 -->

12 (65) 



# **3.8 Temperature sensor performance specifications** 

Table 8 Temperature sensor performance specification 

|**Parameter**|**Min**|**Nom**|**Max**|**Unit**|
|---|---|---|---|---|
|Measurement range|-50||135|°C|
|Temperature signal sensitivity||100||LSB/°C|
|Total error|-15||15|°C|
|Linearity|-1||1|°C|



Temperature is converted to °C with following equation: 

Temperature [°C] = TEMP / 100, where TEMP is temperature sensor output register content in 2’s complement format. 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 13 -->



13 (65) 

# **3.9 Gyroscope and accelerometer frequency response and filter characteristics** 

Table 9 SCH16T-K01 component low pass filter characteristics. Empty columns are not defined. Group delay is the derivate of the phase in respect to frequency, measured at 10Hz. Settling time is the time for the signal to settle within ±0.1% of input signal. Bypass (LPF7) mode realizes the full bandwidth of the MEMS and therefore requires special reading rate considerations according to chapter 5.5 Recommended reading procedure for sensor data. 

|**Filter**|**Axis**|**Title**|**Type**|**Order**|**Min**|**Nom**|**Max**|**Unit**|
|---|---|---|---|---|---|---|---|---|
|||Cut-off frequency (-3 dB)|Butterworth|4|63.5|68|72.5|Hz|
||Gyroscope|Group Delay||||7|10|ms|
|LPF0||Settling time||||10|20|ms|
|||Cut-off frequency (-3 dB)|Butterworth|4|63.5|68|72.5|Hz|
||Accelerometer|Group Delay||||7|10|ms|
|||Settling time||||||ms|
|||Cut-off Frequency (-3 dB)|Butterworth|4|28|30|32|Hz|
||Gyroscope|Group Delay||||14|22|ms|
|LPF1||Settling time||||25|40|ms|
|||Cut-off Frequency (-3 dB)|Butterworth|4|28|30|32|Hz|
||Accelerometer|Group Delay||||14|16|ms|
|||Settling time||||||ms|
|||Cut-off Frequency (-3 dB)|Butterworth|3|12.2|13|13.8|Hz|
||Gyroscope|Group Delay||||32|35|ms|
|LPF2||Settling time||||65|200|ms|
|||Cut-off Frequency (-3 dB)|Butterworth|3|12.2|13|13.8|Hz|
||Accelerometer|Group Delay||||32|35|ms|
|||Settling time||||||ms|
|||Cut-off Frequency (-3 dB)|Bessel|4|262|280|300|Hz|
||Gyroscope|Group Delay||||1.4|2.5|ms|
|LPF3||Settling time|||||5|ms|
|||Cut-off Frequency (-3 dB)|Bessel|4|200|240|275|Hz|
||Accelerometer|Group Delay||||1.5|1.95|ms|
|||Settling time||||||ms|
|||Cut-off Frequency (-3 dB)|Bessel|3|346|370|394|Hz|
||Gyroscope|Group Delay||||1.1|2|ms|
|LPF4||Settling time||||||ms|
|||Cut-off Frequency (-3 dB)|Bessel|3|234|290|380|Hz|
||Accelerometer|Group Delay||||1.1|1.56|ms|
|||Settling time||||||ms|
|||Cut-off Frequency (-3 dB)|Bessel|3|220|235|250|Hz|
||Gyroscope|Group Delay||||1.5|2.5|ms|
|||Settling time||||||ms|
|LPF5||Cut-off Frequency (-3 dB)|Bessel|3|179|210|235|Hz|
||Accelerometer|Group Delay||||1.6|2.05|ms|
|||Settling time||||||ms|
|LPF7|G|Cut-off Frequency (-3 dB)||||3700||Hz|
||yroscope|Group Delay||||0.2|0.23|ms|



**Murata Electronics Oy** SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 14 -->



14 (65) 

|**Filter**|**Axis**|**Title**|**Type**|**Order**|**Min**|**Nom**|**Max**|**Unit**|
|---|---|---|---|---|---|---|---|---|
|||Settling time||||0.2|0.78|ms|
|||Cut-off Frequency (-3 dB)||||600 (XY)<br>900 (Z)||Hz|
||Accelerometer|Group Delay||||||ms|
|||Settling time|||||0.78|ms|



# **3.10 Pin description** 



## Figure 1 SCH16T series pin layout 

Table 10 SCH16T series pin description 

|**Pin**<br>**#**|**Name**|**Description**|**Type**|**Voltage**<br>**level**|**Default**<br>**state/structure**|
|---|---|---|---|---|---|
|1|HEATSINK|Heatsink connection|GND|0 V||
|2|Reserved|Leave floating|N/A|||
|3|TA9|SPI device selection Address 1 (static). Slave<br>addressing in SafeSPI2. Max four slaves can be<br>addresses by TA9:8. TA on the slave is defined by<br>VDDIO logic level at pins TA9 and TA8. Connect to<br>ground for default ‘0’ address.|DIN|0 V|0/PDR<sup>1)</sup>|
|4|TA8|SPI device selection Address 0 (static). Slave<br>addressing in SafeSPI2. Max four slaves can be<br>addresses by TA9:8. TA on the slave is defined by<br>VDDIO logic level at pins TA9 and TA8. Connect to<br>ground for default ‘0’ address.|DIN|0 V|0/PDR<sup>1)</sup>|
|5|Reserved|Connect to GND|N/A|||
|6|EXTRESN|External reset input (low active) during normal operation.|DIN/AIN|VDDIO|1/PUR<sup>1)</sup>|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 15 -->



15 (65) 

|**Pin**<br>**#**|**Name**|**Description**|**Type**|**Voltage**<br>**level**|**Default**<br>**state/structure**|
|---|---|---|---|---|---|
|7|Reserved|Connect to GND|N/A|||
|8|V3P3|External unregulated inputs for the core supply<br>regulators|SUPPLY|3.3 V||
|9|GND|Ground|GND|0 V||
|10|VREGA2|Regulated core voltage for the analog circuitry. External<br>capacitor connection for positive reference/supply<br>voltage. Connected in PCB.|AIN|2.5 V||
|11|VREGA|Regulated core voltage for the analog circuitry. External<br>capacitor connection for positive reference/supply<br>voltage. Connected in PCB.|AOUT|2.5 V||
|12|GND|Ground|GND|0 V||
|13|GND|Ground|GND|0 V||
|14|VREGD2|Regulated core voltage for the digital circuitry. External<br>capacitor connection for positive reference/supply<br>voltage. Connected in PCB.|AIN|1.5 V||
|15|VREGD|Regulated core voltage for the digital circuitry. External<br>capacitor connection for positive reference/supply<br>voltage. Connected in PCB.|AOUT|1.5 V||
|16|GND|Ground|GND|0 V||
|17|V3P3|External unregulated inputs for the core supply<br>regulators|SUPPLY|3.3 V||
|||||3.3 V||
|18|VDDIO|Digital supply I/O|SUPPLY|(option:<br>1.8 V or<br>2.5 V)||
|19|MISO|Master In Slave Out (SPI)|DOUT|VDDIO|TRI|
|20|DRY_SYNC|SYNC input (active high)<br>DRY (Data Ready) outputs an interrupt signal when the<br>internal output registers (decimated gyroscope and<br>accelerometer) have been updated until the first<br>decimated register is read.|DIN/DOUT|VDDIO|0/PDR|
|21|SCK|Serial Clock (SPI)|DIN|VDDIO|0/PDR|
|22|CS|Chip Select (SPI)|DIN|VDDIO|1/PUR|
|23|MOSI|Master Out Slave In (SPI)|DIN|VDDIO|0/PDR|
|24|HEATSINK|Heatsink connection|GND|0 V||



1) Strong PD/PU resistance during device supply POR reset state, otherwise weak PD/PU. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 16 -->



16 (65) 

# **3.11 Digital I/O specification** 

Table 11 SPI DC characteristics describes DC characteristics of the SCH16T series SPI I/O pins. Current flowing into the circuit has a positive value. 

Table 11 SPI DC characteristics. 

|**Title**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|SPI voltage level|VIO|1.7|3.6|V|
|Input high voltage|VIH|0.7*VIO|VIO|V|
|Input low voltage|VIL|0|0.3*VIO|V|
|Input voltage hysteresis|VHYST|0.05*VIO||V|
|Input/output capacitance|CIO||10|pF|
|Total MISO load capacitance<sup>1)</sup>, <Wide> range|CLWIDE|10|100|pF|
|Input pull-down resistance, strong (default)|RPD|60|140|kOhm|
|Input pull-up resistance, strong (default)|RPU|60|140|kOhm|
|Input pull-down/pull-up resistance, weak (option)|RPD/RPU|200|400|kOhm|
|Output leakage current in case MISO is in high impedance (tri-state)<br>condition|ILEAK|-10|10|µA|



- 1) For maximum supported MISO capacitance see SPI AC specifications 

# **3.12 SPI AC characteristics** 



Figure 2 Timing diagram of SPI communication (SPI mode 0), CPOL = 0, CPHA = 0 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 17 -->

17 (65) 



Table 12 SPI AC electrical characteristics. Default mode is MISO_HI_SPD = 0. If MISO_HI_SPD = 1 setting is used it must be set up first after startup. 

|**Title**|**Remark**|**Symbol**|**MISO_**<br>**= 0 (De**|**HI_SPD**<br>**fault)**|**MISO_**<br>**= 1**|**HI_SPD**|**Unit**|
|---|---|---|---|---|---|---|---|
||||**Min**|**Max**|**Min**|**Max**||
|SCK operating<br>frequency|||0.095|10.5|0.095|25.5|MHz|
|MISO data valid<br>time (CS)|Time delay from the falling edge of CS to<br>data valid at MISO|A||40||17|ns|
|MISO data valid<br>time (SCK)|Time delay from the falling edge of SCK to<br>data valid at MISO|B||32||14|ns|
|MOSI data hold time|Hold time of MOSI after rising edge of SCK|C|20||8||ns|
|MISO rise and fall<br>time|MISO rise and fall time is not defined during<br>transition between high impedance and<br>active mode (MISO load max 200 pF)|D|2|10|NA|NA|ns|
|MISO rise and fall<br>time|MISO rise and fall time is not defined during<br>transition between high impedance and<br>active mode (MISO load max 100 pF)|D|2|9|0.3|5|ns|
|MISO rise and fall<br>time|MISO rise and fall time is not defined during<br>transition between high impedance and<br>active mode (MISO load max 50 pF)|D|2|9|0.3|4|ns|
|MISO data disable<br>lag time|Time between the rising edge of CS to<br>MISO in Tri-state|E||50||21|ns|
|MOSI data setup<br>time|Setup time of MOSI before the rising edge<br>of SCK|F|10||4||ns|
|SCK disable lead<br>time|Time between the falling edge of SCK and<br>the falling edge of CS|1|10||10||ns|
|SCK enable lead<br>time|Time between the falling edge of CS and<br>the rising edge of SCK|2|40||17||ns|
|SCK rise and fall<br>time|Rise and fall time of SCK signals|3||9||3.5||
|SCK high time|Duration of logical high level at SCK|4|37||16||ns|
|SCK low time|Duration of logical low level at SCK|5|37||16||ns|
|SCK enable lag time|Time between the falling edge of SCK and<br>the rising edge of CS|6|20||8||ns|
|SCK disable lag<br>time|Time between the rising edge of CS and the<br>rising edge of SCK|7|10||10||ns|
|Sequential transfer<br>delay|In case of MOSI write commands (RW=1)|9|750||450||ns|
|Sequential transfer<br>delay|In case of MOSI read commands (RW=0)|9|450||450||ns|
|MOSI rise and fall<br>time|Rise and fall time of MOSI signals|10||9||3.5|ns|
|MISO data setup<br>time|Setup time of MISO before the rising edge<br>of SCK|11|5||2||ns|
|MISO data hold time|Hold time of MISO after rising edge of SCK|12|X<sup>1)</sup>||X<sup>1)</sup>||ns|
|MOSI valid time|Valid time of MOSI after the falling edge of<br>SCK|13||10||4|ns|
|CS rise and fall time|Rise and fall time of CS signals|10||9||3.5|ns|



1) MISO data is guaranteed to be stable until the next SCK shift edge 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 18 -->



18 (65) 

# **3.13 Measurement axis and directions** 



Figure 3 SCH16T series measurement directions for gyroscope and accelerometer. Output is showing positive value when component is moved in the direction of the arrow. 



Figure 4 SCH16T series accelerometer measurement directions and outputs. 1 g indicates direction of gravity. Note: Pin 1 is marked in blue only in this data sheet to emphasize location. 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 19 -->



19 (65) 

## **3.14 Package outline and dimensions** 



Figure 5 Outline of SOIC package. All dimensions are in millimeters. All angles are in degrees. Tolerances unless otherwise specified according to ISO2768-f. A sample part number for reference only. Shapes and dimensions of non-specified features are subject to change. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 20 -->



20 (65) 

## **3.15 PCB footprint** 

SCH16T series PCB footprint dimensions are presented in the figure below. 



Figure 6 Recommended PCB pad layout for SCH16T series. All dimensions are in millimeters. 

# **This is the end of the short data sheet. For full version of the data sheet and an assembly instructions document, please contact Murata.** 

_Murata reserves all rights to modify this document without prior notice._ 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 21 -->

21 (65) 

**CONFIDENTIAL** 



# **4 General product description** 

The SCH16T series consists of independent acceleration and angular rate sensing elements, and an Application-Specific Integrated Circuit (ASIC) used to sense and control those elements. The angular rate and acceleration sensing elements are manufactured using Murata's proprietary High Aspect Ratio (HAR) 3D-MEMS process, which enables making robust, extremely stable, and low noise capacitive sensors. 

## **4.1 Component block diagram** 



<!-- Start of picture text -->
RATE<br>ACC12<br>ACC3<br><!-- End of picture text -->

Figure 7 SCH16T series block diagram. Note<sup>A</sup> : gyro Y- and Z- channels are identical to X- channel. 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 22 -->

22 (65) 

**CONFIDENTIAL** 



## **4.2 Accelerometer** 

The acceleration sensing element consists of three acceleration-sensitive masses. Acceleration causes a capacitance change that is converted into a voltage change in the signal conditioning ASIC. 

## **4.3 Gyroscope** 

The angular rate sensing element consists of moving masses that are intentionally exited to in-plane drive motion. Rotation in a sensitive direction causes in-plane (Z) or out-of-plane (XY) movement that can be measured as capacitance change with the signal conditioning ASIC. 

## **4.4 Factory calibration** 

Sensors are factory calibrated and there is no need for separate calibration in most applications. Factory calibrated parameters include offset, sensitivity, internal fault monitoring signals and cross-axis sensitivity for gyroscope and accelerometer. 

Sensors are calibrated over temperature in three measurement points at -40 °C, +25 °C, and +110 °C. Offset and sensitivity are calibrated with 2nd order polynomial and cross-axis with linear function. Calibration variables are stored in non-volatile memory during manufacturing and are read automatically during the start-up. 

It is important to acknowledge that PCB assembly can introduce offset errors to the sensor output. If feasible, system-level offset calibration (zeroing) post-assembly is recommended. 

# **5 Component operation, reset and power-up** 

## **5.1 Component operation** 

The SCH16T series has an internal power-on reset circuit. After release of EXTRESN and once the power supplies are within the specified range, the component reads configuration and calibration data from the non-volatile memory to volatile registers. After the memory is read, the sensor goes to low power mode and an external SPI command, EN_SENSOR, is needed to continue to the initialization phase and to start the measurement. 

Start-up time is dependent on the low pass filter setting. After power-on or reset (release of EXTRESN or EN_SENSOR command) the sensor provides valid acceleration and angular rate data after the specified power-on start-up time. 

SCH16T series LPF0 (68 Hz) low pass filter setting by default and the filter can be changed by SPI command. SCH16T series has extensive internal fault diagnostics to detect possible over range and internal failures. Diagnostic status can be monitored via status bits included in SPI frame and status registers. 

## **5.2 Start-up sequence** 

The purpose of the start-up sequence is to guide the component to normal operation mode and verify that the functions (accelerometer, angular rate, and temperature) are working as intended. During this sequence, the component also performs tests to ensure that the monitoring circuits are operating normally. This is intended to prevent potential latent failures in the component due to malfunctions in the monitoring circuits. 

The internal start-up tests will set various intended error flags in the sensor status registers. To clear these flags, it is necessary to read the status registers after the start-up sequence is complete. When reading the status registers, user must consider that the state of status flags is not defined during Low Power Mode (LPM) and during the 215 ms wait state after issuing an EN_SENSOR command. Once the start-up sequence is completed and the End of Initialization bit (EOI bit) has been set to '1', the SPI frame Return Status bits (S bits) indicate sensor operation status. Normal operation is indicated by an S status content of 0b00. 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 23 -->

23 (65) 

**CONFIDENTIAL** 





Figure 8 Example of SCH16T series start-up sequence 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 24 -->

24 (65) 

**CONFIDENTIAL** 



## **5.3 Component output options** 

The SCH16T component has several output options for the user to choose from. The component has two outputs for reading gyroscope data and a total of three outputs for reading acceleration data. Each output consists of separate X-, Y- and Z-axis output data registers and each output and axis have separate status flags. The first gyroscope data output RATE_XYZ1 has interpolation filter and the second RATE_XYZ2 has decimation filter. The first acceleration output ACC_XYZ1 has interpolation filter, second ACC_XYZ2 has decimation filter and the third output ACC_XYZ3 has also interpolation filter but with larger dynamic range compared to the first one. Interpolation and decimation are explained in more detail in the next chapter 5.4 Solutions for asynchronous clock domains. 

The user may choose to utilize multiple outputs simultaneously and adjust output settings separately according to the users’ needs. Dynamic range can be individually set for each output, but lowpass filter settings are shared between interpolated and decimated outputs. However, different filters can be applied between gyroscope, accelerometer, and auxiliary accelerometer X-, Y- and Z-axis if desired. For example, the user can read ACC_XYZ1 with nominal ±164 m/s2 dynamic range and 68 Hz filter, and ACC_XYZ3 with nominal ±260 m/s2 dynamic range and 290 Hz filter. The output options are presented in the table below. 

Table 13 SCH16T series output options. Rounded dynamic range values. 

|**Output**|**Description**|**Dynamic range**<br>**configuration bits**|**Dynamic**<br>**range**<br>**options**|**Output**<br>**axis**|**Low pass filter**<br>**configuration bits**|**Low pass**<br>**filter**<br>**options**|
|---|---|---|---|---|---|---|
|||||RATE_X1|FILT_SEL_RATE_X||
|RATE_XYZ1|Interpolated<br>gyroscope output|DYN_RATE_XYZ1|±328 °/s|RATE_Y1|FILT_SEL_RATE_Y|13, 30, 68|
||||(default)|RATE_Z1|FILT_SEL_RATE_Z|<br>(default),|
||||±164, ±82<br>|RATE_X2|FILT_SEL_RATE_X|235, 280<br>|
|RATE_XYZ2|Decimated<br>gyroscope output|DYN_RATE_XYZ2|°/s|RATE_Y2|FILT_SEL_RATE_Y|and 370 Hz|
|||||RATE_Z2|FILT_SEL_RATE_Z||
||Interpolated|||ACC_X1|FILT_SEL_ACC_X12||
|ACC_XYZ1|accelerometer|DYN_ACC_XYZ1|±164 m/s<sup>2</sup>|ACC_Y1|FILT_SEL_ACC_Y12|13 30 68|
||output||(default)<br>|ACC_Z1|FILT_SEL_ACC_Z12|, ,<br>(default),|
||Decimated||±82, ±41<br>and ±20.5|ACC_X2|FILT_SEL_ACC_X12|210, 240<br>|
|ACC_XYZ2|accelerometer|DYN_ACC_XYZ2|m/s<sup>2</sup>|ACC_Y2|FILT_SEL_ACC_Y12|and 290 Hz|
||output|||ACC_Z2|FILT_SEL_ACC_Z12||
||Auxiliary||±260 m/s<sup>2</sup><br>|ACC_X3|FILT_SEL_ACC_X3|13, 30, 68|
|ACC_XYZ3|interpolated<br>|DYN_ACC_XYZ3|(default)<br>±164, ±82,|ACC_Y3|FILT_SEL_ACC_Y3|(default),<br>|
||accelerometer<br>output||±41 and<br>±20.5 m/s<sup>2</sup>|ACC_Z3|FILT_SEL_ACC_Z3|210, 240<br>and 290 Hz|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 25 -->

25 (65) 

**CONFIDENTIAL** 



# **5.4 Solutions for asynchronous clock domains** 

Several features have been introduced to enhance synchronization between the product's internal clock and the application system clock. Although most systems can typically handle standard continuous polling of the SPI peripheral, precise time-domain synchronization is crucial for certain highperformance applications. The table below outlines these synchronization features, while additional usecase examples and recommendations are provided in chapter 5.5 Recommended reading procedure for sensor data. 

Table 14 Solutions for asynchronous clock domains 

|**Feature**|**Use case**|**Value**||
|---|---|---|---|
|Interpolation|This should be used by default. Interpolation<br>is applied in outputs RATE_XYZ1,<br>ACC_XYZ1, and ACC_XYZ3.|•<br>•<br>•|Minimized sampling jitter.<br>Minimized timing difference reads.<br>No missing samples|
|Decimation|This function averages the sample data rate<br>down to 737.5 Hz segments. Decimation is<br>applied in outputs RATE_XYZ2 and<br>ACC_XYZ2|•<br>•|Gives the host more time to read each sample.<br>Data is available over a longer time window that<br>is helpful if host system sampling rate is<br>inconsistent.|
|SYNC input|Special case. Recommended if there is a<br>need to sync between multiple SCH16T<br>series sensors or if sample time consistency<br>is valued over jitter|•<br>•|Synchronization between multiple sensors.<br>Data can be received with consistent rate even if<br>host system sampling rate is inconsistent.|
|DRY output<br>(Data Ready<br>Interrupt)|Special case. Recommended only if<br>decimated, low update rate outputs<br>RATE_XYZ2 and ACC_XYZ2 are used.<br>Decimated outputs are typically used if MCU<br>bandwidth is limited.|•<br>•|Minimized sampling jitter. With decimated<br>outputs, the maximum data jitter depends on the<br>decimation ratio and interrupt use removes this<br>jitter totally.<br>No missing samples.|
|Data counter|Special case. Recommended only if Data<br>Ready is not preferred in application.|•<br>•<br>•<br>•|Data counter is index for the component data<br>output values. The application can monitor that:<br>Data is updating.<br>Every wanted sample has been acquired.<br>The same sample has not been read twice.|
|Data counter<br>with frequency<br>counter|Special case. Recommended if integration<br>operation is performed to sensor data and<br>timing uncertainty or data jitter of the<br>interpolated data do not fulfill the system<br>accuracy requirements.|•|Data counter together with frequency counter<br>can be used for more accurate integration.|



SYNC and DRY (Data Ready) are implemented on a single hardware pin. Therefore, simultaneous use of these functions is not possible. Controlling the behavior of SYNC and DRY is explained in chapters _5.4.3 SYNC input pin_ and _5.4.4 Data Ready, DRY_ . 

# **5.4.1 Interpolation** 

The purpose of interpolation is to minimize time uncertainty (sampling jitter) by increasing artificially the internal sample rate.  The natural output data rate of all data outputs is F_PRIM/2, which is 11.8 kHz with nominal primary frequency. This means that a time-uncertainty between sensor register update and system sampling time could be theoretically anything between 0...85 µs. 

To minimize this jitter, a fixed interpolation factor of 32 is applied to outputs RATE_XYZ1, ACC_XYZ1, and ACC_XYZ3. With nominal primary frequency it corresponds to a 377.6 kHz refresh rate of register content. 

The sample rate is increased by adding a one (1) cycle latency delay to the initial sample. The delay corresponds to the maximum time uncertainty which with nominal primary frequency is 85 µs. A linear interpolation is then applied between the initial sample and the new sample, and this interpolation is divided into time segments by the artificially increased update rate 32 x F_PRIM/2. Time uncertainty is 

**Murata Electronics Oy** SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 26 -->

26 (65) 

**CONFIDENTIAL** 



now reduced to the length of this segment, which is max (85 µs)/32 = 2.6 µs (with nominal primary frequency). 



Figure 9 Interpolation (8 kHz system sampling rate is used in this illustration) 

# **5.4.2 Decimation** 

Certain systems need to utilize every available sample and for example acquire samples from all axis at the same time instant. As the natural output data rate with nominal primary frequency is 11.8 kHz, this can create excessive load for the MCU. The purpose of decimation is to decrease the internal update rate to give the host system enough time to read same sample from all axis without the need of use of SYNC. The decimation is done by a non-recursive moving averager CIC decimation filter that uses F_PRIM/2 sample rate. Final decimated output is the average of all the samples that sensor has updated during the last decimated output cycle. 

During start-up, the user can select a suitable decimation from the options presented in the table below. The selected decimation ratio is applied to outputs RATE_XYZ2 and ACC_XYZ2. 

Table 15 Selectable decimation ratios and corresponding ODR 

|**Decimation factor**|**Output data rate**|**Output data rate with**<br>**nominal F_PRIM (kHz)**|**Data reading time with**<br>**nominal F_PRIM (ms)**|
|---|---|---|---|
|1|F_PRIM/2|11.8|0.085|
|2|F_PRIM/4|5.9|0.17|
|4|F_PRIM/8|2.95|0.34|
|8|F_PRIM/16|1.475|0.68|
|16|F_PRIM/32|0.7375|1.36|



Drawback of decimation is that sampling jitter is increased with the same ratio as the decimation factor. With nominal primary frequency and decimation ratio of 16, the sampling jitter will be up to 85 µs x 16 = 1.36 ms. This means that sample age can be anything between 0 and 1.36 ms. To address this issue, the user can combine decimation with the Data Ready function. Data Ready is explained in chapter _Data Ready, DRY_ . 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 27 -->

**CONFIDENTIAL** 



27 (65) 

# **5.4.3 SYNC input pin** 

High-performance systems may benefit from using multiple SCH16T series components. Depending on application SPI master clock conditions, the read operation of multiple parallel sensors can take longer than sensor internal register update period if individual MISO line is not used for each component. As a result of this, samples are being acquired from different time instants for each parallel sensor. In certain real-world inputs, this can lead to a significant apparent disagreement of sensors, as different timeinstants are being sampled. 

To mitigate this issue, a SYNC input pin has been introduced. When the master issues SYNC signal to all sensors in the system, the sensors' internal updates for RATE_XYZ1/2 and ACC_XYZ1/2/3 are frozen until SYNC pin is set LOW, or after time out period set by CTRL_SYNC_TOC_TH time-out counter. This allows enough time for the master to read all sensor data from a single time instant. CTRL_SYNC_TOC_TH is user-selectable with typical values ranging from 1.2 ms to 11.6 ms. Please refer to chapter 7.4.6 Sensor mode control and soft reset for user controls. 

SYNC is only feasible on interpolated outputs RATE_XYZ1 and ACC_XYZ1/3. With decimated outputs and a decimation factor of 2 or above, most masters should have enough time to read the output registers before they are updated again. 

Additionally, SYNC helps ensure that all 6-axis data is captured at the same time instant. In cases of slow SPI master clocks, even a single sensor might update its internal registers during slow read operations, resulting in different axes reflecting various timestamps. SYNC can also assist when system load is high and consistent sampling frequency cannot be maintained. 

Please refer to illustration below. 



Figure 10 Illustration of SYNC usage when 3 slave sensors are read by single a master 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 28 -->

28 (65) 

**CONFIDENTIAL** 



# **5.4.4 Data Ready, DRY** 

In some system implementations, the rate at which the host processor can read peripherals may be limited. In such cases, using decimated outputs with an appropriate decimation factor can help ensure that the host system has enough time to read same sample from all axes. However, lowering the sensor update rate through decimation increases sampling jitter. As mentioned in chapter _5.4.1 Interpolation_ , the worst-case sampling jitter can reach up to 85 µs with a decimation factor of 1; this jitter increases proportionally as the decimation factor rises. 

In case jitter minimization is critical to the application, the user should utilize the data ready output pin (DRY_SYNC). When all sensor output channels are updated, DRY_SYNC triggers a rising edge to indicate that new samples are available. This rising edge can serve as a direct interrupt to initiate the sensor read operation, or the host can monitor this signal and ensure that data is read in bursts before the next expected internal update from the sensor. This approach helps prevent missing samples and avoids reading any samples twice. It’s important to note that a new data ready pulse is generated only after all sensor data has been read. 

Data Ready function is available for decimated outputs. If different data rate is selected for the outputs, the DRY_SYNC-pin operates with the lowest data rate of the decimated outputs. 



Figure 11 Illustration of Data Ready output signal. In this example, data is read in a burst between sensor internal updates. Note that sensor data must be read to clear Data Ready signal. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 29 -->

29 (65) 

**CONFIDENTIAL** 



# **5.4.5 Data counter** 

Data counter is supported for decimated outputs RATE_XYZ2 and ACC_XYZ2. Value of data counter is increased by one when a new sample is available from corresponding RATE/ACC output. It can be understood as an index for the data output values. Using the data counter, the user can monitor that every wanted sample has been acquired and that the same sample has not been read twice. 

When using 48-bit SPI protocol, 4-bit data counter value is included in MISO response frame. Data counter can be also used in 32-bit mode by reading DCNT_RATE and DCNT_ACC register values via SPI command. Register locations are described in chapter _7.3.1 Data counters._ 

# **5.4.6 Frequency counter** 

Using frequency counter (FREQ_CNTR), user can acquire accurate clock information from component internal MCLK via SPI. The value of frequency counter register is increased by one with every 16<sup>th</sup> rising edge of master clock. 

- MCLK = 1024 * F_PRIM. 

- Nominal FREQ_CNTR = MCLK/16 = 1510 kHz 

- If counter reaches 16383 (14b11 1111 1111 1111) it rolls back to zero 

- Nominal counter reset frequency = 92 Hz 

# **5.4.7 Time stamp** 

The component itself does not provide a time stamp; it must be generated by the host system. However, the SCH16T series provides an array of features allowing creation of accurate time stamps. The simplest approach to time stamping is utilizing the DRY_SYNC pin. When using data ready, the host system can issue a read command to the component after a defined time delay from receiving the DRY_SYNC interrupt signal and calculate the time stamp utilizing the host systems MCLK. 

When SYNC is used, the host system has control over the sample update rate and can freeze the output by issuing a signal through the DRY_SYNC pin. This allows time stamp creation based on host system MCLK and SYNC input. 

If the DRY_SYNC pin is not used, the user can define each components individual update rate with the frequency counter and then monitor with the data counter when the sample index has changed. 

**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 30 -->

30 (65) 

**CONFIDENTIAL** 



# **5.5 Recommended reading procedure for sensor data** 

Table 16 Default reading procedure bolded. For maximum performance 6300 Hz gyroscope and 4200 Hz accelerometer reading rate is recommended with LPF3, LPF4 and LPF5 settings. Minimum recommended reading rate depends on the decimation factor with LPF7 option. 

|**Axis**|**Output**|**Minimize jitter**|**Decimation**<br>**factors**|**ODR**<br>**(Hz)**|**LPF**|**Cut-off**<br>**frequency**<br>**Nom (-3 dB)**<br>**(Hz)**|**Minimum**<br>**recommended**<br>**reading rate (Hz)**|
|---|---|---|---|---|---|---|---|
||||||LPF2|13|150|
||||||LPF1|30|200|
|||Read at minimum<br>|||**LPF0**|**68**|**500**|
||Interpolated|recommended<br>reading rate (max|Not<br>applicable|377000|LPF5|235|1000|
|||<br>jitter always <2.6 µs)|||LPF3|280|1000|
||||||LPF4|370|2000|
||||||LPF7|Not defined|11800|
|Gyroscope|||||LPF2|13|150|
||||||LPF1|30|200|
||||||LPF0|68|500|
||Decimated|Read at Data Ready|1-16|11800<br>- 740|LPF5|235|ODR-1000|
||||||LPF3|280|ODR-1000|
||||||LPF4|370|ODR-2000|
||||||LPF7|Not defined|ODR|
||||||LPF2|13|150|
||||||LPF1|30|200|
|||Read at minimum<br>|||**LPF0**|**68**|**500**|
||Interpolated|recommended<br>reading rate (max|Not<br>applicable|377000|LPF5|210|1000|
|||<br>jitter always <2.6 µs)|||LPF3|240|1000|
||||||LPF4|290|2000|
||||||LPF7|600-900|4200|
|Accelerometer|||||LPF2|13|150|
||||||LPF1|30|200|
||||||LPF0|68|500|
||Decimated|Read at Data Ready|1-16|11800<br>- 740|LPF5|210|ODR-1000|
||||||LPF3|240|ODR-1000|
||||||LPF4|290|ODR-2000|
||||||LPF7|600-900|ODR-4200|



The optimal reading configuration depends on application, system timing requirements and hardware. High level examples of reading configurations are given below: 

- Reading inertial data for leveling or positioning IMU. 

   - Use default settings at minimum recommended reading rate. 

- Maximum performance for dead reckoning. 

   - Use an LPF setting with high bandwidth (LPF3, LPF4 and LPF5) and read the interpolated outputs with a minimum reading rate of 6300 Hz. 

- Maximizing dead reckoning performance with limited bandwidth. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 31 -->

31 (65) 

**CONFIDENTIAL** 



   - Select a decimation ratio matching to systems bandwidth limits and read decimated outputs with minimum recommended reading rate. 

- Synchronizing IMU signal with another low frequency signal while collecting every generated sample (e.g., Create FIFO buffer for GPS 1 Hz signal in host) 

   - If necessary, reduce required memory to store samples at host by output decimation (Available typical ODR range on decimated outputs 740 Hz - 11800 Hz). 

   - Read decimated outputs at Data Ready signal (monitor DRY_SYNC pin in Data Ready mode or use it directly as trigger signal for read command). 

   - Store the samples in host for processing (samples can be timestamped in the host memory based on Data Ready pulse). 

DCNT function and/or FREQ_CNTR register can be used to keep track of sensor time. 

## **5.6 Diagnostics flags and status behavior** 

The primary way to determine the status of the sensor is to use status (S) bits S0 and S1 that are received with every response MISO SPI communication. If the S bits are not “00” signifying normal operation the data of the MISO frame is potentially not reliable. S bits generate for each axis and output option separately. 

Status bits are acknowledged and cleared by reading the data registers normally. Status bits can be cleared also by reading corresponding 1<sup>st</sup> level status registers (all other status registers but STAT_SUM or STAT_SUM_SAT). Clearing time is determined by FTREE_TDEL. 

Table 17 Fault clearing logic by reading data register 

|**Read Sensor Data Register**|**Status registers that are cleared after FTREE_TDEL delay**|
|---|---|
|RATE_X1 | RATE_X2|STAT_COM & STAT_RATE_COM & STAT_RATE_X|
|RATE_Y1 | RATE_Y2|STAT_COM & STAT_RATE_COM & STAT_RATE_Y|
|RATE_Z1 | RATE_Z2|STAT_COM & STAT_RATE_COM & STAT_RATE_Z|
|ACC_X1 | ACC_X2 | ACC_X3|STAT_COM & STAT_ACC_X|
|ACC_Y1 | ACC_Y2 | ACC_Y3|STAT_COM & STAT_ACC_Y|
|ACC_Z1 | ACC_Z2 | ACC_Z3|STAT_COM & STAT_ACC_Z|
|TEMP|STAT_COM|



In some applications saturation events can be frequent due to harsh low frequency vibration. Therefore, saturation flag filtering can be used to lower the sensitivity to the saturation events. 

Table 18 Saturation Flag detection and clearing time. More information about the saturation flag filter and clearing time in chapters 7.4.3 Saturation flag user control and 7.4.4 User interface control 

|**Saturation detection time (typical)**|**Saturation clearing time (typical)**|
|---|---|
|0.08 ms (default) to 42 ms.||
|Detection time is controlled by how many consecutive|0.078 ms to 5 ms. 2.5 ms (default)|
|saturation events are needed for detection. Event count is|Clearing time is determined by FTREE_TDEL|
|filtered from 1 (default) to 496.||



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 32 -->

32 (65) 

**CONFIDENTIAL** 



# **6 Component interfacing** 

## **6.1 Safe SPI** 

Product supports Safe SPI v2.0 protocol to transfer data between SPI master and registers of SCH16T series ASIC. The product always operates as a slave device in master-slave operation mode. 3-wire SPI connection cannot be used. Communication between master and slave is done with pins described below in _Table 19 SPI interface pins._ 

Table 19 SPI interface pins 

|**SPI interface pin**|**Description**|**Communication direction**|
|---|---|---|
|CS|Chip Select (active low)|MCU to ASIC|
|SCK|Serial Clock|MCU to ASIC|
|MOSI|Master Out Slave In|MCU to ASIC|
|MISO|Master In Slave Out|ASIC to MCU|



SPI communication uses out-of-frame protocol, so each transfer has two phases. The first phase contains the SPI command (request) and the data (response) of the previous command. The second phase contains the next request and the response to the request of the first phase. The first response after reset is undefined and can be discarded. 



Figure 12 SPI protocol example 

Product SPI block implements two different SPI protocol types. Both protocol types can be used during operation by defining the SPI frame bit length. 

- SafeSPI2 32-bit frame, SPI32BF 

- SafeSPI2 48-bit frame, SPI48BF 

SPI block does not implement the complete SafeSPI v2.0 specification. Summary of supported features can be seen in table below. For Safe SPI standard, please refer to www.SafeSPI.org 

Table 20 SCH16T series supported features of SafeSPI v2.0 

|**Supported feature**|**Description**|
|---|---|
|<48/32oof>|Block receives and transmits 32-bit and 48-bit Out-of-frame SPI frames. In-frame protocols are not<br>supported.|
|<FrTyp>|MOSI frame width is defined by received frame length. Frame is effective only if width is 32-bits or 48-<br>bits and the CRC is valid.|
|<SelBitWidthByAdr >|Next MISO frame width is decided by <FrTyp>|
|<Sel4SlaveByAdrPin>|Two MSB address bits can be used to select one of four slaves when one CS signal pin is in use.<br>Slave compares the two MSBs to a reference value defined by two input pins.|
|<FixedSensorFrame>|Frame content is well defined and fixed.|
|<CLWide>|Wide range for “total signal load capacitance”|
|<DCnt>|Block updates a wrapping 4-bit sample counter each time new sensor data is generated.|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 33 -->

**CONFIDENTIAL** 



33 (65) 

|**Supported feature**|**Description**|
|---|---|
|<IDS>|Internal Data Status field includes additional status information for sensor data.|
|<CAP>|Not implemented and replaced with fixed value.|



The SPI transmission is always started with the CS falling edge and terminated with the CS rising edge. The data is captured on the SCK's rising edge (MOSI line) and it is propagated on the SCK’s falling edge (MISO line). This equals to SPI Mode 0 (CPOL = 0 and CPHA = 0), an example with 32-bit frame can be seen in _Figure 13 SPI frame format example (32-bit)._ 



Figure 13 SPI frame format example (32-bit) 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 34 -->

34 (65) 

**CONFIDENTIAL** 



# **6.2 SPI frame structure** 

SPI Frame format is explained in figure below and Table 21 SPI bit definitions 



Figure 14 SPI frame format for 48-bit and 32-bit frames 

Table 21 SPI bit definitions 

|**Symbol**|**Description**|
|---|---|
|D|D=1 condition:<br>Gyro data register read<br>ACC data register read<br>Temperature data register read<br>D=0 condition:<br>Any other register than data registers listed above|
|TA|Defines the**Target Address**for SCH16T series<br>TA[9:8] bits are used as Chip Select information, and thus they are not part of the effective address.<br>TA[7:0] are used as effective address within the chip.|
|SA|Contains the**Source Address**. It has the same content as TA.|
|RW|**Read/write**access selector. Read is selected with 0 and write with 1.|
|FT (FrTyp)|Frame Type for next MISO frame: 0 for SPI32BF, 1 for SPI48BF. MOSI frame width is defined by the MOSI<br>frame itself, hence this field should match the next incoming MOSI frame since out-of-frame responses are in<br>use.|
|AE|Reserved. Bits should be ignored.|
|DATAI|MOSI line input**data**from SPI host. This field is 20-bits wide for SPI48BF and 16-bits for SPI32BF.|
|SENSOR|MISO line**sensor type output data**towards SPI host.|
|INFO|MISO line**non-sensor type output data**towards SPI host. This field is 20-bits wide for SPI48BF and 16-bits<br>for SPI32BF. 20-bit data is clipped from LSB end to 16-bit with SPI32BF, i.e. data is MSB aligned.|
|*|Unused field that is ignored for receive and set to all-zeros for transmit.|
|S1:0, S1, S0|**Sensor status**indication.|
|CE|**Command Error**indication. SCH16T series reports only semantically invalid frame content using this field. SPI<br>protocol level errors are indicated with High-Z on MISO pin.|
|IDS|**Internal Data Status**indication. SCH16T series uses this field to indicate common cause error. This is<br>redundant, more accurate info is seen from sensor status (S1:S0).|
|DCNT|A wrapping 4-bit sensor data counter.|
|CRC8<br>(C7:0)|8-bit CRC reference for SPI48BF. Calculated over bits 47 to 8.|
|CRC3<br>(C2:0)|3-bit CRC reference for SPI32BF. Calculated over bits 31 to 3.|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 35 -->

35 (65) 

**CONFIDENTIAL** 



# **6.3 Multi-slave operation** 

SCH16T series SPI supports up to four slave devices on single bus by using either multiple Chip Select lines, one for each slave, or with one common Chip Select (CS) and using TA9 and TA8 pins to enable logical addressing. 

Pin 3 (TA9) and pin 4 (TA8) correspond to the bits TA9:9 and TA8:8 included in the SPI MOSI frame. 

Issuing a pull-up signal to either pin flips the corresponding component logic level -bit to ‘1’. All options for addressing four slaves are shown in figure below. 

Example: Compose MOSI frame targeted to component #3 

1. Set pin 3 (TA9) low and pin 4 (TA8) high 

2. Send MOSI frame in which TA9:8 is written as ‘01’ 



Figure 15 Multi-slave operation 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 36 -->

36 (65) 

**CONFIDENTIAL** 



# **6.4 SPI frame status bits** 

Status bits indicate functional status of the sensor. See table below for definitions of bits S[1:0] S[1:0] priority order is 11 (Initialization) `→` 01 (Error) `→` 10 (Saturation) `→` 00 (Normal operation) 

Note that the Status bits S[1:0] are always '00' on the response frame for register write commands. 

Table 22 Status bit description 

|**Status bits S[1:0]**|**Description**|
|---|---|
|00|Normal operation|
|01|Error status|
|10|Saturation error|
|11|Initialization running|



IDS, or Internal Data Status bit is redundant error status bit for S[1:0] in case of common status error. See table below for definitions of IDS bit. 

Table 23 IDS bit description 

|**Status bits IDS**|**Description**|
|---|---|
|0|Normal operation|
|1|Common Error|



CE status bit reports Command Errors. See table below for definitions of CE bit. 

The following access errors are detected and reported by CE bit: 

- Write request when EOI is active, excluding write to reset activation register. 

- Read or write request to unused/undefined address. 

- Write request to read-only register. 

Table 24 CE bit description 

|**Status bits CE**|**Description**|
|---|---|
|0|Normal operation|
|1|Command Error|



The SPI frame status bit generation logic is explained in the figure below. Internal safety mechanism status signals trigger component internal 2nd level safety flags. These 2nd level status flags then trigger the 1st level status register flags after assessment against user defined flag settings and flag grouping logic assessment. Flags in status summary registers STAT_SUM and STAT_SUM_SAT are generated based on triggered 1st level status registers. The summary status flags are then reflected to SPI frame status bits with the logic explained above. Note that fault state is indicated by '0' in component internal registers and '1' in SPI frame status bits. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 37 -->

**CONFIDENTIAL** 



37 (65) 



Figure 16 Status flag flow chart 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 38 -->

38 (65) 

**CONFIDENTIAL** 



# **6.5 Cyclic redundancy check (CRC)** 

uint8_t CRC8(uint64_t SPIframe) { uint64_t data = SPIframe & 0xFFFFFFFFFF00LL; uint8_t crc = 0xFF; for (int i = 47; i >= 0; i--) { uint8_t data_bit = (data >> i) & 0x01; crc = crc & 0x80 ? (uint8_t)((crc << 1) ^ 0x2F) ^ data_bit : (uint8_t)(crc << 1) | data_bit; } return crc; } uint8_t CRC3(uint32_t SPIframe) { uint32_t data = SPIframe & 0xFFFFFFF8; uint8_t crc = 0x05; for (int i = 31; i >= 0; i--) { uint8_t data_bit = (data >> i) & 0x01; crc = crc & 0x4 ? (uint8_t)((crc << 1) ^ 0x3) ^ data_bit : (uint8_t)(crc << 1) | data_bit; crc &= 0x7; } return crc; <u>}</u> 

Figure 17 C-programming language example for CRC calculation. For more information about headers and SPI communications, please refer to SCH1600 C-code example. Example code is not performance optimized. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 39 -->

39 (65) 

**CONFIDENTIAL** 



# **6.5.1 SPI48BF CRC** 

SPI48BF uses 8-bit CRC (CRC8). CRC is calculated from MSB towards LSB i.e., from bit 47 to 0. Bits from 7 to 0 are set initially as 0. 

Generator polynomial is 0x97 + 1 (b1001 0111 1) (X<sup>8</sup> +X<sup>5</sup> +X<sup>3</sup> +X<sup>2</sup> +X+1). 

Calculation is initialized with start value of 0xFF and a target value of 0x00 (no inversion of CRC result). 

Final CRC is the direct value of the calculation. 

For further information please refer to chapter 4.4.4 “48Bit frame CRC Definition” of the original “SafeSPI – Serial Peripheral Interface for Automotive Safety Rev 2.0” specification. 

Table 25 CRC definition for 48-bit frames 

|**Parameter**|**Value**|
|---|---|
|Name|CRC-8|
|Width|8-bit|
|Generator polynomial<br>(Koopman notation)|0x97 (X<sup>8</sup>+X<sup>5</sup>+X<sup>3</sup>+X<sup>2</sup>+X+1)|
|Initial|0xFF|
|XOR out|0x00 (no inversion of CRC result)|



# **6.5.2 SPI32BF CRC** 

SPI32BF uses 3-bit CRC (CRC3). CRC is calculated from MSB towards LSB i.e., from bit 31 to 0. Bits from 2 to 0 are set initially as 0. 

Generator polynomial is 0x5 +1 (b1011) (X<sup>3</sup> +X+1) 

Calculation is initialized with start value of 0x5 and a target value of 0x0 (no inversion of CRC result). 

Final CRC is the direct value of the calculation. 

For further information please refer to chapter 4.3.5 “32Bit CRC Definition” of the original “SafeSPI – Serial Peripheral Interface for Automotive Safety Rev 2.0” specification. 

Table 26 CRC definition for 32-bit frames 

|**Parameter**|**Value**|
|---|---|
|Name|CRC-3|
|Width|3-bit|
|Generator polynomial<br>(Koopman notation)|0x5 (X<sup>3</sup>+X+1)|
|Initial|0x5|
|XOR out|0x0 (no inversion of CRC result)|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 40 -->

40 (65) 

**CONFIDENTIAL** 



## **6.6** 

## **Operations** 

This chapter lists some common SPI operations. Default ‘00’ TA chip select address is used for example operations. For more detailed component operation description, please refer to SCH1600 C- code example. For frame construction please refer to the chapter _6.2 SPI frame structure._ 

Table 27 Common operations and their equivalent SPI frames 

|**Command**|**Register name**|**Register public**<br>**address**|**32-bit SPI Hex**<br>**frame**|**48-bit SPI Hex**<br>**frame**|
|---|---|---|---|---|
|Set Operation mode EN_SENSOR|CTRL_MODE|15h0035|0x0D60000A|0x0D68000001D3|
|Set EOI bit|CTRL_MODE|15h0035|0x0D60001C|0x0D680000038D|
|Reset via SPI|CTRL_RESET|15h0036|0x0DA00054|0x0DA800000AC3|
|Read RATE filter setting|CTRL_FILT_RATE|15h0025|0x09400007|0x0948000000FA|
|Select LPF0 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x09600006|0x096800000016|
|Select LPF1 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x0960024C|0x096800004988|
|Select LPF2 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x09600492|0x096800009205|
|Select LPF3 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x096006D8|0x09680000DB9B|
|Select LPF4 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x09600925|0x096800012430|
|Select LPF5 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x09600B6F|0x096800016DAE|
|Select LPF6 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x09600DB1|0x09680001B623|
|Select LPF7 filter for RATE_XYZ|CTRL_FILT_RATE|15h0025|0x09600FFB|0x09680001FFBD|
|Select LPF0 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A00000|0x09A800000020|
|Select LPF1 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A0024A|0x09A8000049BE|
|Select LPF2 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A00494|0x09A800009233|
|Select LPF3 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A006DE|0x09A80000DBAD|
|Select LPF4 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A00923|0x09A800012406|
|Select LPF5 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A00B69|0x09A800016D98|
|Select LPF6 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A00DB7|0x09A80001B615|
|Select LPF7 filter for ACC 1/2|CTRL_FILT_ACC12|15h0026|0x09A00FFD|0x09A80001FF8B|
|Read ACC 1/2 filter setting|CTRL_FILT_ACC12|15h0026|0x09800001|0x0988000000CC|
|Select LPF0 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00002|0x09E8000000D7|
|Select LPF1 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00248|0x09E800004949|
|Select LPF2 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00496|0x09E8000092C4|
|Select LPF3 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E006DC|0x09E80000DB5A|
|Select LPF4 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00921|0x09E8000124F1|
|Select LPF5 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00B6B|0x09E800016D6F|
|Select LPF6 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00DB5|0x09E80001B6E2|
|Select LPF7 filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09E00FFF|0x09E80001FF7C|
|Read filter for ACC 3|CTRL_FILT_ACC3|15h0027|0x09C00003|0x09C80000003B|
|Read RATE_X1|RATE_X1|15h0001|0x00400001|0x0048000000AC|
|Read RATE_Y1|RATE_Y1|15h0002|0x00800007|0x00880000009A|
|Read RATE_Z1|RATE_Z1|15h0003|0x00C00005|0x00C80000006D|
|Read RATE_X2|RATE_X2|15h000A|0x02800001|0x0288000000EF|
|Read RATE_Y2|RATE_Y2|15h000B|0x02C00003|0x02C800000018|
|Read RATE_Z2|RATE_Z2|15h000C|0x03000006|0x030800000083|
|Read ACC_X1|ACC_X1|15h0004|0x01000000|0x0108000000F6|
|Read ACC_Y1|ACC_Y1|15h0005|0x01400002|0x014800000001|
|Read ACC_Z1|ACC_Z1|15h0006|0x01800004|0x018800000037|



Doc.No. 11624 Rev. 6 

**Murata Electronics Oy** SCH16T 

www.murata.com 



<!-- page 41 -->



41 (65) 

## **CONFIDENTIAL** 

|**Command**|**Register name**|**Register public**<br>**address**|**32-bit SPI Hex**<br>**frame**|**48-bit SPI Hex**<br>**frame**|
|---|---|---|---|---|
|Read ACC_X2|ACC_X2|15h000D|0x03400004|0x034800000074|
|Read ACC_Y2|ACC_Y2|15h000E|0x03800002|0x038800000042|
|Read ACC_Z2|ACC_Z2|15h000F|0x03C00000|0x03C8000000B5|
|Read ACC_X3|ACC_X3|15h0007|0x01C00006|0x01C8000000C0|
|Read ACC_Y3|ACC_Y3|15h0008|0x02000005|0x02080000002E|
|Read ACC_Z3|ACC_Z3|15h0009|0x02400007|0x0248000000D9|
|Read Temperature|TEMP|15h0010|0x04000004|0x0408000000B1|
|Read Summary Status|STAT_SUM|15h0014|0x05000007|0x05080000001C|
|Read Saturation Summary Status|STAT_SUM_SAT|15h0015|0x05400005|0x0548000000EB|
|Read Level-1 Common Status|STAT_COM|15h0016|0x05800003|0x0588000000DD|
|Read Level-1 Rate common Status|STAT_RATE_COM|15h0017|0x05C00001|0x05C80000002A|
|Read Level-1 Rate X Status|STAT_RATE_X|15h0018|0x06000002|0x0608000000C4|
|Read Level-1 Rate Y Status|STAT_RATE_Y|15h0019|0x06400000|0x064800000033|
|Read Level-1 Rate Z Status|STAT_RATE_Z|15h001A|0x06800006|0x068800000005|
|Read Level-1 ACC X Status|STAT_ACC_X|15h001B|0x06C00004|0x06C8000000F2|
|Read Level-1 ACC Y Status|STAT_ACC_Y|15h001C|0x07000001|0x070800000069|
|Read Level-1 ACC Z Status|STAT_ACC_Z|15h001D|0x07400003|0x07480000009E|
|Read SYNC_ACTIVE Status|STAT_SYNC_ACTIVE|15h001E|0x07800005|0x0788000000A8|
|Read Low Power Mode Status|STAT_INFO|15h001F|0x07C00007|0x07C80000005F|



# **7 Register definition** 

SPI frame bit D1/D0 is specified according to Safe SPI standard. 

The sensor data bit D identifies if SPI response frame contains sensor data (i.e., identifies response frame format). The frame bit for registers defined in SPI frame bit D column in this chapter. 

D=0: no sensor data, e.g., status data or read back of configuration data 

D=1: sensor data 

## **7.1 Register map user guide** 

## **7.1.1 Value and address formats** 

Several value formats are used in this data sheet. These are described in table below. 

Table 28 Value formats 

|**Decimal**|**5-bit decimal**|**5-bit signed hex**|**5-bit binary**|
|---|---|---|---|
|13|13d|0Dh|5b01101|
|-13|-13d|13h|5b10011|



All essential register content of SCH16T series ASIC is mirrored to public memory banks 0-3. The register address is a 4-bit offset within a memory bank. final public address is formed by adding address offset to public bank address, for example STAT_SUM register: 

- Bank address: 15h0010 

- Address offset: 4h4 

- Public Address: 15h0010 + 4h4 = 15h0014 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 42 -->

42 (65) 

**CONFIDENTIAL** 



## **7.1.2 Register map overview** 

Table 29 Register map overview with memory banks, address offsets and data widths 

|**Register name**|**Bank**|**Bank**<br>**address**|**Address**<br>**offset**|**Data**<br>**width**|**Register type**|**SPI frame**<br>**bit D**|**Public address**|
|---|---|---|---|---|---|---|---|
|Reserved|0|15h0000|4h0|-|-|-|15h0000|
|RATE_X1|0|15h0000|4h1|20-bit|Data|D1|15h0001|
|RATE_Y1|0|15h0000|4h2|20-bit|Data|D1|15h0002|
|RATE_Z1|0|15h0000|4h3|20-bit|Data|D1|15h0003|
|ACC_X1|0|15h0000|4h4|20-bit|Data|D1|15h0004|
|ACC_Y1|0|15h0000|4h5|20-bit|Data|D1|15h0005|
|ACC_Z1|0|15h0000|4h6|20-bit|Data|D1|15h0006|
|ACC_X3|0|15h0000|4h7|20-bit|Data|D1|15h0007|
|ACC_Y3|0|15h0000|4h8|20-bit|Data|D1|15h0008|
|ACC_Z3|0|15h0000|4h9|20-bit|Data|D1|15h0009|
|RATE_X2|0|15h0000|4hA|20-bit|Data|D1|15h000A|
|RATE_Y2|0|15h0000|4hB|20-bit|Data|D1|15h000B|
|RATE_Z2|0|15h0000|4hC|20-bit|Data|D1|15h000C|
|ACC_X2|0|15h0000|4hD|20-bit|Data|D1|15h000D|
|ACC_Y2|0|15h0000|4hE|20-bit|Data|D1|15h000E|
|ACC_Z2|0|15h0000|4hF|20-bit|Data|D1|15h000F|
|TEMP|1|15h0010|4h0|16-bit|Data|D1|15h0010|
|RATE_DCNT|1|15h0010|4h1|12-bit|Counter|D0|15h0011|
|ACC_DCNT|1|15h0010|4h2|14-bit|Counter|D0|15h0012|
|FREQ_CNTR|1|15h0010|4h3|16-bit|Counter|D0|15h0013|
|STAT_SUM|1|15h0010|4h4|16-bit|Status|D0|15h0014|
|STAT_SUM_SAT|1|15h0010|4h5|16-bit|Status|D0|15h0015|
|STAT_COM|1|15h0010|4h6|16-bit|Status|D0|15h0016|
|STAT_RATE_COM|1|15h0010|4h7|16-bit|Status|D0|15h0017|
|STAT_RATE_X|1|15h0010|4h8|16-bit|Status|D0|15h0018|
|STAT_RATE_Y|1|15h0010|4h9|16-bit|Status|D0|15h0019|
|STAT_RATE_Z|1|15h0010|4hA|16-bit|Status|D0|15h001A|
|STAT_ACC_X|1|15h0010|4hB|16-bit|Status|D0|15h001B|
|STAT_ACC_Y|1|15h0010|4hC|16-bit|Status|D0|15h001C|
|STAT_ACC_Z|1|15h0010|4hD|16-bit|Status|D0|15h001D|
|STAT_SYNC_ACTIVE|1|15h0010|4hE|12-bit|Status|D0|15h001E|
|STAT_INFO|1|15h0010|4hF|9-bit|Status|D0|15h001F|
|Reserved|2|15h0020|4h0|-|-|-|15h0020|
|Reserved|2|15h0020|4h1|-|-|-|15h0021|
|Reserved|2|15h0020|4h2|-|-|-|15h0022|
|Reserved|2|15h0020|4h3|-|-|-|15h0023|
|Reserved|2|15h0020|4h4|-|-|-|15h0024|
|CTRL_FILT_RATE|2|15h0020|4h5|9-bit|Control|D0|15h0025|
|CTRL_FILT_ACC12|2|15h0020|4h6|9-bit|Control|D0|15h0026|
|CTRL_FILT_ACC3|2|15h0020|4h7|9-bit|Control|D0|15h0027|
|CTRL_RATE|2|15h0020|4h8|15-bit|Control|D0|15h0028|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 43 -->

43 (65) 

**CONFIDENTIAL** 



|**Register name**|**Bank**|**Bank**<br>**address**|**Address**<br>**offset**|**Data**<br>**width**|**Register type**|**SPI frame**<br>**bit D**|**Public address**|
|---|---|---|---|---|---|---|---|
|CTRL_ACC12|2|15h0020|4h9|15-bit|Control|D0|15h0029|
|CTRL_ACC3|2|15h0020|4hA|3-bit|Control|D0|15h002A|
|CTRL_RATE_FLAG_1|2|15h0020|4hB|15-bit|Control|D0|15h002B|
|CTRL_RATE_FLAG_2|2|15h0020|4hC|15-bit|Control|D0|15h002C|
|CTRL_ACC_FLAG_1|2|15h0020|4hD|15-bit|Control|D0|15h002D|
|CTRL_ACC_FLAG_2|2|15h0020|4hE|15-bit|Control|D0|15h002E|
|Reserved|2|15h0020|4hF|-|-|-|15h002F|
|Reserved|3|15h0030|4h0|-|-|-|15h0030|
|Reserved|3|15h0030|4h1|-|-|-|15h0031|
|Reserved|3|15h0030|4h2|-|-|-|15h0032|
|CTRL_USER_IF|3|15h0030|4h3|16-bit|Control|D0|15h0033|
|CTRL_ST|3|15h0030|4h4|13-bit|Control|D0|15h0034|
|CTRL_MODE|3|15h0030|4h5|4-bit|Control|D0|15h0035|
|CTRL_RESET|3|15h0030|4h6|4-bit|Control|D0|15h0036|
|SYS_TEST|3|15h0030|4h7|16-bit|Other|D0|15h0037|
|SPARE_1|3|15h0030|4h8|16-bit|Other|D0|15h0038|
|SPARE_2|3|15h0030|4h9|16-bit|Other|D0|15h0039|
|SPARE_3|3|15h0030|4hA|16-bit|Other|D0|15h003A|
|ASIC_ID|3|15h0030|4hB|12-bit|Other|D0|15h003B|
|COMP_ID|3|15h0030|4hC|16-bit|Other|D0|15h003C|
|SN_ID1|3|15h0030|4hD|16-bit|Other|D0|15h003D|
|SN_ID2|3|15h0030|4hE|16-bit|Other|D0|15h003E|
|SN_ID3|3|15h0030|4hF|16-bit|Other|D0|15h003F|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 44 -->



44 (65) 

# **CONFIDENTIAL** 

# **7.2 Sensor data block** 

Table 30 Overview of registers for sensor data. The data is in 2’s complement format 

|**Register**<br>**name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|RATE_X1|Output, x-axis gyroscope, interpolation, common low pass filter with<br>RATE_X2|R|D1|15h0001|
|RATE_Y1|Output, y-axis gyroscope, interpolation, common low pass filter with<br>RATE_Y2|R|D1|15h0002|
|RATE_Z1|Output, z-axis gyroscope, interpolation, common low pass filter with<br>RATE_Z2|R|D1|15h0003|
|ACC_X1|Output, x-axis accelerometer, interpolation, common low pass filter with<br>ACC_X2|R|D1|15h0004|
|ACC_Y1|Output, y-axis accelerometer, interpolation, common low pass filter with<br>ACC_Y2|R|D1|15h0005|
|ACC_Z1|Output, z-axis accelerometer, interpolation, common low pass filter with<br>ACC_Z2|R|D1|15h0006|
|ACC_X3|Output, x-axis accelerometer, auxiliary signal path with interpolation<br>and individually configurable low pass filter setting.|R|D1|15h0007|
|ACC_Y3|Output, y-axis accelerometer, auxiliary signal path with interpolation<br>and individually configurable low pass filter setting.|R|D1|15h0008|
|ACC_Z3|Output, z-axis accelerometer, auxiliary signal path with interpolation<br>and individually configurable low pass filter setting.|R|D1|15h0009|
|RATE_X2|Output, x-axis gyroscope, configurable decimation filter, common low<br>pass filter with RATE_X1|R|D1|15h000A|
|RATE_Y2|Output, y-axis gyroscope, configurable decimation filter, common low<br>pass filter with RATE_Y1|R|D1|15h000B|
|RATE_Z2|Output, z-axis gyroscope, configurable decimation filter, common low<br>pass filter with RATE_Z1|R|D1|15h000C|
|ACC_X2|Output, x-axis accelerometer, configurable decimation filter, common<br>low pass filter with ACC_X1|R|D1|15h000D|
|ACC_Y2|Output, y-axis accelerometer, configurable decimation filter, common<br>low pass filter with ACC_Y1|R|D1|15h000E|
|ACC_Z2|Output, z-axis accelerometer, configurable decimation filter, common<br>low pass filter with ACC_Z1|R|D1|15h000F|
|TEMP|Output, temperature sensor|R|D1|15h0010|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 45 -->

45 (65) 

**CONFIDENTIAL** 



# **7.2.1 Example of angular rate data conversion** 

Interpolated output of Rate X is used as example. Data is in 2’s complement format. 

## **16-bit data from 32-bit frames** 

In 16-bit mode, default sensitivity is 100 LSB/(°/s) 

If Rate X register (15h0001) read result is Rate X = 802 **FFE0** 7h, content is converted to angular rate as follows: 

- 802h = 1 0 0 0000 0001 0b (contains D bit, address bits and first status bit) 

- FFE0h = 1111 1111 1110 0000b (Rate X register content) 

- FFE0h in 2’s complement format = -32d 

- Angular rate = -32 LSB/sensitivity = -32 LSB/ (100 LSB/(°/s)) = -0.32 °/s 

- 7h = CRC of 802FFE0h 

## **20-bit data from 48-bit frames** 

In 20-bit mode, default sensitivity is 1600 LSB/(°/s) 

If Rate X register (15h0001) read result is Rate X = 80200 **FFE00** ADh, content is converted to angular rate as follows: 

- 80200h = 1 0 0 0000 0001 0 0 00 0000 0b (contains D-bit, address-, status- and DCNT bits and one empty bit) 

- FFE00h = 1111 1111 1110 0000 0000b (Rate X register content) 

- FFE00h in 2’s complement format = -512d 

- Angular rate = -512 LSB/sensitivity = -512 LSB/ (1600 LSB/(°/s)) = -0.32 °/s 

- ADh = CRC of 80200FFE00h 

# **7.2.2 Example of acceleration data conversion** 

Interpolated output of ACC Y is used as example. Data is in 2’s complement format. 

## **16-bit data from 32-bit frames** 

In 16-bit mode, default sensitivity is 200 LSB/(m/s<sup>2</sup> ) 

If ACC Y register (15h0005) read result is ACC Y = 80A **00DC** 6h, content is converted to acceleration as follows: 

- 80Ah = 1 0 0 0000 0101 0b (contains D bit, address bits and first status bit) 

- 00DCh = 0000 0000 1101 1100b (ACC Y register content) 

- 00DCh in 2’s complement format = 220d 

- Acceleration = 220 LSB/sensitivity = 220 LSB/ (200 LSB/(m/s<sup>2</sup> )) ≈ 1.1 m/s<sup>2</sup> 

- 6h = CRC of 80A00DC0h 

## **20-bit data from 48-bit frames** 

In 20-bit mode, default sensitivity is 3200 LSB/(m/s<sup>2</sup> ) 

If ACC Y register (15h0005) read result is ACC Y = 80A00 **00DC0** DBh, content is converted to acceleration as follows: 

- 80A00h = 1 0 0 0000 0101 0 0 00 0000 0b (contains D-bit, address-, status- and DCNT bits and one empty bit) 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 46 -->

46 (65) 

**CONFIDENTIAL** 



- 00DC0h = 0000 0000 1101 1100 0000b (ACC Y register content) 

- 00DC0h in 2’s complement format = 3520d 

- Acceleration= 3520 LSB/sensitivity = 3520 LSB/ (3200 LSB/(m/s<sup>2</sup> )) ≈ 1.1 m/s<sup>2</sup> 

- DBh = CRC of 80A00DC000h 

# **7.2.3 Example of temperature data conversion** 

## **16-bit data from 32-bit frames** 

Temperature signal sensitivity is 100 LSB/°C 

If TEMP register (15h0010) read result is TEMP = 820 **00DC** 5h, content is converted to temperature as follows: 

- 820h = 1 0 0 0001 0000 0b (contains D bit, address bits and first status bit) 

- 00DCh =0000 0000 1101 1100b (TEMP register content) 

- 00DCh in 2’s complement format = 220d 

- Temperature= 220 LSB/sensitivity = 220 LSB/ (100 LSB/°C) = 2.2°C 

- 5h = CRC of 82000DC0h 

## **20-bit data from 48-bit frames** 

The temperature data is always 16-bit wide. In 20-bit mode, this needs to be considered. The user has two options: 

1. Change frame type for temperature register read to 32-bit by changing FT bit of previous MOSI frame from 1 to 0. Then, convert TEMP data as explained in 16-bit mode. 

2. Read TEMP register in 20-bit mode. As data is only 16-bits wide, the remaining LSBs will be all zeroes and they need to be discarded. After that, register content can be converted in similar manner as explained in 16-bit mode. 

If TEMP register (15h0010) read result is TEMP = 82000 **00DC0** EAh, content is converted to temperature (°C) as follows: 

- 82000h = 1 0 0 0001 0000 0 0 00 0000 0b (contains D-bit, address-, status- and DCNT bits and one empty bit) 

- Discard last byte ( **0** h). 

- 00DCh =0000 0000 1101 1100b (TEMP register content) 

- 00DCh in 2’s complement format = 220d 

- Temperature= 220 LSB/sensitivity = 220 LSB/ (100 LSB/°C) = 2.2°C 

- EAh = CRC of 82000DC000h 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 47 -->

47 (65) 

**CONFIDENTIAL** 



# **7.3 Sensor status and counter block** 

Table 31 Overview of registers for sensor status and counters 

|**Register name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|RATE_DCNT|Data counter for RATE_XYZ2|R|D0|15h0011|
|ACC_DCNT|Data counter for ACC_XYZ|R|D0|15h0012|
|FREQ_CNTR|Frequency / sample time counter|R|D0|15h0013|
|STAT_SUM|Status summary for non-saturation related flags|R|D0|15h0014|
|STAT_SUM_SAT|Status summary for saturation flags|R|D0|15h0015|
|STAT_COM|Common status flags, incl. TEMP, 1<sup>st</sup>level status register|R|D0|15h0016|
|STAT_RATE_COM|Common gyro status flags (primary channel), 1<sup>st</sup>level<br>status register|R|D0|15h0017|
|STAT_RATE_X|RATE_X status flags, 1<sup>st</sup>level status register|R|D0|15h0018|
|STAT_RATE_Y|RATE_Y status flags, 1<sup>st</sup>level status register|R|D0|15h0019|
|STAT_RATE_Z|RATE_Z status flags, 1<sup>st</sup>level status register|R|D0|15h001A|
|STAT_ACC_X|ACC_X status flags, 1<sup>st</sup>level status register|R|D0|15h001B|
|STAT_ACC_Y|ACC_Y status flags, 1<sup>st</sup>level status register|R|D0|15h001C|
|STAT_ACC_Z|ACC_Z status flags, 1<sup>st</sup>level status register|R|D0|15h001D|
|STAT_SYNC_ACTIVE|Status of SYNC on each channel|R|D0|15h001E|
|STAT_INFO|Low power mode indications|R|D0|15h001F|



# **7.3.1 Data counters** 

Table 32 Data counter registers 

|**Register name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|RATE_DCNT|Data counter for RATE_XYZ2 output|R|D0|15h0011|
|ACC_DCNT|Data counter for ACC_XYZ2 output|R|D0|15h0012|



Table 33 RATE_DCNT register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|RATE_Z_DCNT|4-bit data counter for RATE_Z output. Data counter value is updated (+1) when a new<br>sample is available from corresponding RATE/ACC output. When counter reaches<br>4b1111, it rolls back to zero.|[11:8]|4b0000|
|RATE_Y_DCNT|4-bit data counter for RATE_Y output. Data counter value is updated (+1) when a new<br>sample is available from corresponding RATE/ACC output. When counter reaches<br>4b1111, it rolls back to zero.|[7:4]|4b0000|
||4-bit data counter for RATE_X output. Data counter value is updated (+1) when a new|||
|RATE_X_DCNT|sample is available from corresponding RATE/ACC output. When counter reaches<br>4b1111, it rolls back to zero.|[3:0]|4b0000|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 48 -->

48 (65) 



# **CONFIDENTIAL** 

Table 34 ACC_DCNT register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|ACC_Z_DCNT|4-bit data counter for ACC_Z output. Data counter value is updated (+1) when a new<br>sample is available from corresponding RATE/ACC output. When counter reaches<br>4b1111, it rolls back to zero.|[11:8]|4b0000|
|ACC_Y_DCNT|4-bit data counter for ACC_Y output. Data counter value is updated (+1) when a new<br>sample is available from corresponding RATE/ACC output. When counter reaches<br>4b1111, it rolls back to zero.|[7:4]|4b0000|
||4-bit data counter for ACC_X output Data counter value is updated (+1) when a new|||
|ACC_X_DCNT|sample is available from corresponding RATE/ACC output. When counter reaches<br>4b1111, it rolls back to zero.|[3:0]|4b0000|



# **7.3.2 Frequency counter / timestamp** 

Table 35 Frequency counter register 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|FREQ_CNTR|Frequency / sample time counter|R|D0|15h0013|



Table 36 FREQ_CNTR register bit description 

|**Bit name**|**Bit description**|**Bits**|
|---|---|---|
||14-bit counter. The value of frequency counter register is increased by one with every 16th rising<br>edge of master clock.||
|FREQ_CNTR_BIT|•<br>MCLK = 1024 * F_PRIM.<br>•<br>Nominal FREQ_CNTR = MCLK/16 = 1510 kHz|[13:0]|
||•<br>If counter reaches 16383 (14b11 1111 1111 1111) it rolls back to zero<br>•<br>Nominal counter reset frequency = 92 Hz||



# **7.3.3 Status summary** 

Table 37 Status summary register 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|STAT_SUM|Status summary for non-saturation related flags|R|D0|15h0014|



Table 38 STAT_SUM register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:8]|8b11111111|
|STAT_SUM_CMN|Common Status|[7:7]|1b1|
|STAT_SUM_RATE_X|RATE_X Status|[6:6]|1b1|
|STAT_SUM_RATE_Y|RATE_Y Status|[5:5]|1b1|
|STAT_SUM_RATE_Z|RATE_Z Status|[4:4]|1b1|
|STAT_SUM_ACC_X|ACC_X Status|[3:3]|1b1|
|STAT_SUM_ACC_Y|ACC_Y Status|[2:2]|1b1|
|STAT_SUM_ACC_Z|ACC_Z Status|[1:1]|1b1|
|STAT_SUM_INIT_RDY|Initialization Ready|[0:0]|1b1|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 49 -->

49 (65) 

**CONFIDENTIAL** 



# **7.3.4 Saturation status summary** 

Table 39 Saturation summary register 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|STAT_SUM_SAT|Status summary for saturation flags|R|D0|15h0015|



Table 40 STAT_SUM_SAT register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:15]|1b1|
|STAT_SUM_SAT_RATE_X1|Saturation status for output RATE_X1|[14:14]|1b1|
|STAT_SUM_SAT_RATE_Y1|Saturation status for output RATE_Y1|[13:13]|1b1|
|STAT_SUM_SAT_RATE_Z1|Saturation status for output RATE_Z1|[12:12]|1b1|
|STAT_SUM_SAT_ACC_X1|Saturation status for output ACC_X1|[11:11]|1b1|
|STAT_SUM_SAT_ACC_Y1|Saturation status for output ACC_Y1|[10:10]|1b1|
|STAT_SUM_SAT_ACC_Z1|Saturation status for output ACC_Z1|[9:9]|1b1|
|STAT_SUM_SAT_ACC_X3|Saturation status for output ACC_X3|[8:8]|1b1|
|STAT_SUM_SAT_ACC_Y3|Saturation status for output ACC_Y3|[7:7]|1b1|
|STAT_SUM_SAT_ACC_Z3|Saturation status for output ACC_Z3|[6:6]|1b1|
|STAT_SUM_SAT_RATE_X2|Saturation status for output RATE_X2|[5:5]|1b1|
|STAT_SUM_SAT_RATE_Y2|Saturation status for output RATE_Y2|[4:4]|1b1|
|STAT_SUM_SAT_RATE_Z2|Saturation status for output RATE_Z2|[3:3]|1b1|
|STAT_SUM_SAT_ACC_X2|Saturation status for output ACC_X2|[2:2]|1b1|
|STAT_SUM_SAT_ACC_Y2|Saturation status for output ACC_Y2|[1:1]|1b1|
|STAT_SUM_SAT_ACC_Z2|Saturation status for output ACC_Z2|[0:0]|1b1|



# **7.3.5 Common status** 

Table 41 Common status register 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|STAT_COM|Common Status flags|R|D0|15h0016|



Table 42 STAT_COM register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:11]|5b11111|
|MCLK_OK|Status of ASIC master clock.|[10:10]|1b1|
|DUAL_CLOCK_OK|Clock reference status flag|[9:9]|1b1|
|DSP_OK|Register content integrity status flag|[8:8]|1b1|
|SVM_OK|SVM self-test status flag|[7:7]|1b1|
|HV_CP_OK|HV charge pump status flag|[6:6]|1b1|
|SUPPLY_OK|Voltage supply status flag|[5:5]|1b1|
|TEMP_OK|Temperature sensor status flag|[4:4]|1b1|
|NMODE_OK|Normal mode status flag|[3:3]|1b1|
|NVM_STS_OK|NVM start-up memory-test status flag|[2:2]|1b1|
|CMN_STS_OK|Start-up self-test status for TEMP and common digital blocks.|[1:1]|1b1|
|CMN_STS_RDY|Start-up self-test ready for TEMP and common digital blocks.|[0:0]|1b1|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 50 -->

50 (65) 

**CONFIDENTIAL** 



# **7.3.6 Gyroscope common status** 

Table 43 Gyroscope common status register 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|STAT_RATE_COM|Common gyro status flags (primary channel)|R|D0|15h0017|



Table 44 STAT_RATE_COM register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:8]|8b11111111|
|PRI_AGC_OK|Gyro primary loop status|[7:7]|1b1|
|GYRO_PRI_OK|Gyro primary loop status|[6:6]|1b1|
|PRI_START_OK|Gyro primary loop start-up status|[5:5]|1b1|
|GYRO_HV_OK|Gyro high voltage status|[4:4]|1b1|
|Reserved|Reserved|[3:3]|1b1|
|GYRO_SD_STS_OK|Gyro shield detection start-up self-test status|[2:2]|1b1|
|GYRO_BOND_STS_OK|Gyro bond wire start-up self-test status|[1:1]|1b1|
|GYRO_STS_RDY_OK|Gyro start-up self-test ready status flag|[0:0]|1b1|



# **7.3.7 Gyroscope status XYZ** 

Table 45 Gyroscope status registers 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|STAT_RATE_X|RATE_X status flags|R|D0|15h0018|
|STAT_RATE_Y|RATE_Y status flags|R|D0|15h0019|
|STAT_RATE_Z|RATE_Z status flags|R|D0|15h001A|



Table 46 STAT_RATE_X register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:10]|6b111111|
|RATE_DEC_X_SAT_OK|Decimated Rate (X2) Output saturation.|[9:9]|1b1|
|RATE_INTP_X_SAT_OK|Interpolated Rate (X1) Output saturation.|[8:8]|1b1|
|Reserved|Reserved|[7:7]|1b1|
|RATE_X_STC_DIG_OK|Status of RATE X Digital Continuous Self-test|[6:6]|1b1|
|RATE_X_STC_ANA_OK|Status of RATE X Analog Continuous Self-test|[5:5]|1b1|
|RATE_X_QC_OK|Status of rate X signal|[4:4]|1b1|
|Reserved|Reserved|[3:2]|1b11|
|Reserved|Reserved|[1:1]|1b1|
|Reserved|Reserved|[0:0]|1b1|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 51 -->



51 (65) 

# **CONFIDENTIAL** 

Table 47 STAT_RATE_Y register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:10]|6b111111|
|RATE_DEC_Y_SAT_OK|Decimated Rate (Y2) Output saturation.|[9:9]|1b1|
|RATE_INTP_Y_SAT_OK|Interpolated Rate (Y1) Output saturation.|[8:8]|1b1|
|Reserved|Reserved|[7:7]|1b1|
|RATE_Y_STC_DIG_OK|Status of RATE Y Digital Continuous Self-test|[6:6]|1b1|
|RATE_Y_STC_ANA_OK|Status of RATE Y Analog Continuous Self-test|[5:5]|1b1|
|RATE_Y_QC_OK|Status of rate Y signal|[4:4]|1b1|
|Reserved|Reserved|[3:2]|1b11|
|Reserved|Reserved|[1:1]|1b1|
|Reserved|Reserved|[0:0]|1b1|



Table 48 STAT_RATE_Z register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation value**|
|---|---|---|---|
|Reserved|Reserved|[15:10]|6b111111|
|RATE_DEC_Z_SAT_OK|Decimated Rate (Z2) Output saturation.|[9:9]|1b1|
|RATE_INTP_Z_SAT_OK|Interpolated Rate (Z1) Output saturation.|[8:8]|1b1|
|Reserved|Reserved|[7:7]|1b1|
|RATE_Z_STC_DIG_OK|Status of RATE Z Digital Continuous Self-test|[6:6]|1b1|
|RATE_Z_STC_ANA_OK|Status of RATE Z Analog Continuous Self-test|[5:5]|1b1|
|RATE_Z_QC_OK|Status of rate Z signal|[4:4]|1b1|
|Reserved|Reserved|[3:2]|1b11|
|Reserved|Reserved|[1:1]|1b1|
|Reserved|Reserved|[0:0]|1b1|



# **7.3.8 Accelerometer status XYZ** 

Table 49 Accelerometer status registers 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|STAT_ACC_X|ACC_X status flags|R|D0|15h001B|
|STAT_ACC_Y|ACC_Y status flags|R|D0|15h001C|
|STAT_ACC_Z|ACC_Z status flags|R|D0|15h001D|



Table 50 STAT_ACC_X register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation**<br>**value**|
|---|---|---|---|
|Reserved|Reserved|[15:11]|5b11111|
|ACC_X3_SAT_OK|ACC_X3 output saturation.|[10:10]|1b1|
|ACC_X_DEC_SAT_OK|Decimated ACC (X2) output saturation.|[9:9]|1b1|
|ACC_X_INTP_SAT_OK|Interpolated ACC (X1) output saturation.|[8:8]|1b1|
|ACC_X_STC_DIG_OK|Accelerometer X Axis Continuous Self-test status 4|[7:7]|1b1|
|ACC_X_STC_TCAP_OK|Accelerometer X Axis Test-Cap Continuous Self-test status|[6:6]|1b1|
|ACC_X_STC_SDD_OK|Accelerometer X Axis Continuous Self-test status 2|[5:5]|1b1|
|ACC_X_STC_N_OK|Accelerometer X Axis Tone Continuous Self-test status|[4:4]|1b1|
|Reserved|Reserved|[3:3]|1b1|
|**Murata Electronics**<br>www.murata.co|**Oy**<br>SCH16T<br>m|Doc.No. 116<br>Rev. 6|24|





<!-- page 52 -->

52 (65) 

**CONFIDENTIAL** 



|**Bit name**|**Bit description**|**Bits**|**Normal operation**<br>**value**|
|---|---|---|---|
|ACC_X_SD_STS_OK|Accelerometer X Axis Shield Detection Start-up Self-test<br>status|[2:2]|1b1|
|ACC_X_STS_OK|Accelerometer X Axis Start-up Self-test status|[1:1]|1b1|
|ACC_X_STS_RDY_OK|Accelerometer X Axis Start-up Self-test ready|[0:0]|1b1|



Table 51 STAT_ACC_Y register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation**<br>**value**|
|---|---|---|---|
|Reserved|Reserved|[15:11]|5b11111|
|ACC_Y3_SAT_OK|ACC_Y3 output saturation.|[10:10]|1b1|
|ACC_Y_DEC_SAT_OK|Decimated ACC (Y2) output saturation.|[9:9]|1b1|
|ACC_Y_INTP_SAT_OK|Interpolated ACC (Y1) output saturation.|[8:8]|1b1|
|ACC_Y_STC_DIG_OK|Accelerometer Y Axis Continuous Self-test status 4|[7:7]|1b1|
|ACC_Y_STC_TCAP_OK|Accelerometer Y Axis Test-Cap Continuous Self-test status|[6:6]|1b1|
|ACC_Y_STC_SDD_OK|Accelerometer Y Axis Continuous Self-test status 2|[5:5]|1b1|
|ACC_Y_STC_N_OK|Accelerometer Y Axis Tone Continuous Self-test status|[4:4]|1b1|
|Reserved|Reserved|[3:3]|1b1|
|ACC_Y_SD_STS_OK|Accelerometer Y Axis Shield Detection Start-up Self-test<br>status|[2:2]|1b1|
|ACC_Y_STS_OK|Accelerometer Y Axis Start-up Self-test status|[1:1]|1b1|
|ACC_Y_STS_RDY_OK|Accelerometer Y Axis Start-up Self-test ready|[0:0]|1b1|



Table 52 STAT_ACC_Z register bit description 

|**Bit name**|**Bit description**|**Bits**|**Normal operation**<br>**value**|
|---|---|---|---|
|Reserved|Reserved|[15:11]|5b11111|
|ACC_Z3_SAT_OK|ACC_Z3 output saturation.|[10:10]|1b1|
|ACC_Z_DEC_SAT_OK|Decimated ACC (Z2) output saturation.|[9:9]|1b1|
|ACC_Z_INTP_SAT_OK|Interpolated ACC (Z1) output saturation.|[8:8]|1b1|
|ACC_Z_STC_DIG_OK|Accelerometer Z Axis Continuous Self-test status 4|[7:7]|1b1|
|ACC_Z_STC_TCAP_OK|Accelerometer Z Axis Test-Cap Continuous Self-test status|[6:6]|1b1|
|ACC_Z_STC_SDD_OK|Accelerometer Z Axis Continuous Self-test status 2|[5:5]|1b1|
|ACC_Z_STC_N_OK|Accelerometer Z Axis Tone Continuous Self-test status|[4:4]|1b1|
|Reserved|Reserved|[3:3]|1b1|
|ACC_Z_SD_STS_OK|Accelerometer Z Axis Shield Detection Start-up Self-test<br>status|[2:2]|1b1|
|ACC_Z_STS_OK|Accelerometer Z Axis Start-up Self-test status|[1:1]|1b1|
|ACC_Z_STS_RDY_OK|Accelerometer Z Axis Start-up Self-test ready|[0:0]|1b1|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 53 -->

53 (65) 

**CONFIDENTIAL** 



# **7.3.9 Additional status registers** 

Table 53 Additional status registers 

|**Register name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|STAT_SYNC_ACTIVE|Status of SYNC on each channel|R|D0|15h001E|
|STAT_INFO|Low power mode indications|R|D0|15h001F|
|Reserved|Reserved|-|D0|15h0020|



Table 54 STAT_SYNC_ACTIVE register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|SYNC_ACTIVE_ACC_Z2|SYNC active in output ACC_Z2|[11:11]|1b0|
|SYNC_ACTIVE_ACC_Y2|SYNC active in output ACC_Y2|[10:10]|1b0|
|SYNC_ACTIVE_ACC_X2|SYNC active in output ACC_X2|[9:9]|1b0|
|SYNC_ACTIVE_RATE_Z2|SYNC active in output RATE_Z2|[8:8]|1b0|
|SYNC_ACTIVE_RATE_Y2|SYNC active in output RATE_Y2|[7:7]|1b0|
|SYNC_ACTIVE_RATE_X2|SYNC active in output RATE_X2|[6:6]|1b0|
|SYNC_ACTIVE_ACC_Z1|SYNC active in output ACC_Z1|[5:5]|1b0|
|SYNC_ACTIVE_ACC_Y1|SYNC active in output ACC_Y1|[4:4]|1b0|
|SYNC_ACTIVE_ACC_X1|SYNC active in output ACC_X1|[3:3]|1b0|
|SYNC_ACTIVE_RATE_Z1|SYNC active in output RATE_Z1|[2:2]|1b0|
|SYNC_ACTIVE_RATE_Y1|SYNC active in output RATE_Y1|[1:1]|1b0|
|SYNC_ACTIVE_RATE_X1|SYNC active in output RATE_X1|[0:0]|1b0|



Table 55 STAT_INFO register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|Reserved|Reserved|[8:7]|1b0|
|Reserved|Reserved|[4:3]|1b0|
|Reserved|Reserved|[6:5]|1b0|
|ACC_LPM_OK|Accelerometer in Low Power Mode|[2:2]|1b0|
|RATE_LPM_OK|Gyroscope in Low Power Mode|[1:1]|1b0|
|SENSOR_LPM_OK|Start-up State Machine in Sensor Low Power Mode|[0:0]|1b0|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 54 -->

54 (65) 



# **CONFIDENTIAL** 

# **7.4 Sensor control block** 

Table 56 Sensor control block register overview 

|**Register name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|Reserved|Reserved|-|D0|15h0021|
|CTRL_FILT_RATE|RATE_XYZ Filter settings. Common filter for each axis X1/X2,<br>Y1/Y2, Z1/Z2.|RW|D0|15h0025|
|CTRL_FILT_ACC12|ACC filter setting. Common filter for each ACC axis X1/X2,<br>Y1/Y2, Z1/Z2.|RW|D0|15h0026|
|CTRL_FILT_ACC3|Filter setting for ACC_X3, ACC_Y3 and ACC_Z3.|RW|D0|15h0027|
|CTRL_RATE|Settings for Gyro post-processing decimation ratio and dynamic<br>range|RW|D0|15h0028|
|CTRL_ACC12|Settings for ACC_X12, ACC_Y12, ACC_Z12 post-processing<br>decimation ratio and dynamic range|RW|D0|15h0029|
|CTRL_ACC3|Settings for ACC_X3, ACC_Y3, ACC_Z3 post-processing shift<br>dynamic range|RW|D0|15h002A|
|Reserved|Reserved|-|D0|15h002B|
|Reserved|Reserved|-|D0|15h002C|
|Reserved|Reserved|-|D0|15h002D|
|Reserved|Reserved|-|D0|15h002E|
|CTRL_USER_IF|User controls for SYNC, Data Ready, Strength of SPI PD/PU,<br>slew rate ctrl, hi-speed|RW|D0|15h0033|
|CTRL_ST|Self-test controls (enable ST and/or request STS)|RW|D0|15h0034|
|CTRL_MODE|Test mode, EOI, EN_SENSOR|RW|D0|15h0035|
|CTRL_RESET|SPI soft reset command|RW|D0|15h0036|
|SYS_TEST|Empty register for testing read/write access|RW|D0|15h0037|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 55 -->

55 (65) 

**CONFIDENTIAL** 



# **7.4.1 Filter settings** 

Table 57 Filter setting registers 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|CTRL_FILT_RATE|RATE_XYZ Filter settings.<br>Common filter for each axis X1/X2, Y1/Y2, Z1/Z2.|RW|D0|15h0025|
|CTRL_FILT_ACC12|ACC filter setting.<br>Common filter for each ACC axis X1/X2, Y1/Y2, Z1/Z2.|RW|D0|15h0026|
|CTRL_FILT_ACC3|Filter setting for ACC_X3, ACC_Y3 and ACC_Z3.|RW|D0|15h0027|



Table 58 Bits for setting of filters. For detailed filter characteristics, please refer 

Table 9 SCH16T-K01 component low pass filter characteristics. 

|**Name**|**Bits**|**Nominal digital cut-off frequency (-3dB)**|
|---|---|---|
|LPF0|'000'|68 Hz (default)|
|LPF1|'001'|30 Hz|
|LPF2|'010'|13 Hz|
|LPF3|'011'|280 Hz|
|LPF4|'100'|370 Hz|
|LPF5|'101'|235 Hz|
|LPF6|'110'|Reserved|
|LPF7|'111'|Bypass|



Table 59 CTRL_FILT_RATE register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|FILT_SEL_RATE_Z|Filter setting for RATE_Z1 and RATE_Z2 outputs|[8:6]|3b000|
|FILT_SEL_RATE_Y|Filter setting for RATE_Y1 and RATE_Y2 outputs|[5:3]|3b000|
|FILT_SEL_RATE_X|Filter setting for RATE_X1 and RATE_X2 outputs|[2:0]|3b000|



Table 60 CTRL_FILT_ACC12 register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|FILT_SEL_ACC_Z12|Filter setting for ACC_Z1 and ACC_Z2 outputs|[8:6]|3b000|
|FILT_SEL_ACC_Y12|Filter setting for ACC_Y1 and ACC_Y2 outputs|[5:3]|3b000|
|FILT_SEL_ACC_X12|Filter setting for ACC_X1 and ACC_X2 outputs|[2:0]|3b000|



Table 61 CTRL_FILT_ACC3 register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|FILT_SEL_ACC_Z3|Filter setting for ACC_Z3 output|[8:6]|3b000|
|FILT_SEL_ACC_Y3|Filter setting for ACC_Y3 output|[5:3]|3b000|
|FILT_SEL_ACC_X3|Filter setting for ACC_X3 output|[2:0]|3b000|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 56 -->

56 (65) 

**CONFIDENTIAL** 



# **7.4.2 Dynamic range and decimation** 

Table 62 Registers for dynamic range and decimation setting 

|**Register**<br>**name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|CTRL_RATE|Settings for Gyro post-processing decimation ratio and shift value<br>(dynamic range)|RW|D0|15h0028|
|CTRL_ACC12|Settings for ACC_X12, ACC_Y12, ACC_Z12 post-processing<br>decimation ratio and shift value (dynamic range)|RW|D0|15h0029|
|CTRL_ACC3|Settings for ACC_X3, ACC_Y3, ACC_Z3 post-processing shift value<br>(dynamic range)|RW|D0|15h002A|



Table 63 RATE nominal dynamic range settings (CTRL_RATE) 

|**Name**|**Bits**|**Measurement**<br>**range (°/s)**|**Dynamic range**<br>**(°/s)**|**Electrical**<br>**headroom(°/s)**|**Sensitivity, 16-**<br>**bit(LSB/(°/s))**|**Sensitivity, 20-**<br>**bit(LSB/(°/s))**|
|---|---|---|---|---|---|---|
|Undefined|'000'|-|-|-|-|-|
|DYN1 (default)|'001'|±300|±327.68|±327.68|100|1600|
|DYN2|'010'|±300|±327.68|±327.68|100|1600|
|DYN3|'011'|±125|±163.84|±163.84|200|3200|
|DYN4|'100'|±62.5|±81.92|±81.92|400|6400|



Table 64 ACC12 nominal dynamic range settings (CTRL_ACC12) 

|**Name**|**Bits**|**Measurement**<br>**range (m/s**<sup>**2**</sup>**)**|**Dynamic range**<br>**(m/s**<sup>**2**</sup>**)**|**Electrical**<br>**headroom (m/s**<sup>**2**</sup>**)**|**Sensitivity, 16-**<br>**bit (LSB/(m/s**<sup>**2**</sup>**))**|**Sensitivity, 20-**<br>**bit (LSB/(m/s**<sup>**2**</sup>**))**|
|---|---|---|---|---|---|---|
|Undefined|'000'|-|-|-|-|-|
|DYN1 (default)|'001'|±80|±163.84|±163.84|200|3200|
|DYN2|'010'|±60|±81.92|±81.92|400|6400|
|DYN3|'011'|±30|±40.96|±40.96|800|12800|
|DYN4|'100'|±15|±20.48|±20.48|1600|25600|



Table 65 ACC3 nominal dynamic range settings (CTRL_ACC3) 

|**Name**|**Bits**|**Measurement**<br>**range (m/s**<sup>**2**</sup>**)**|**Dynamic range**<br>**(m/s**<sup>**2**</sup>**)**|**Electrical**<br>**headroom (m/s**<sup>**2**</sup>**)**|**Sensitivity, 16-**<br>**bit (LSB/(m/s**<sup>**2**</sup>**))**|**Sensitivity, 20-**<br>**bit (LSB/(m/s**<sup>**2**</sup>**))**|
|---|---|---|---|---|---|---|
|DYN0 (default)|'000'|±80|±260 (-3 σ)|±327.68|100|1600|
|DYN1|'001'|±80|±163.84|±163.84|200|3200|
|DYN2|'010'|±60|±81.92|±81.92|400|6400|
|DYN3|'011'|±30|±40.96|±40.96|800|12800|
|DYN4|'100'|±15|±20.48|±20.48|1600|25600|



Table 66 Decimation ratio settings (CTRL_RATE, CTRL_ACC12) 

|**Name**|**Bits**|**Reduction factor**|**Output sample rate**|**With nominal F_PRIM (kHz)**|
|---|---|---|---|---|
|DEC1|'000' (no decimation)|1|F_PRIM/2|11.8|
|DEC2|'001'|2|F_PRIM/4|5.9|
|DEC3|'010'|4|F_PRIM/8|2.95|
|DEC4|'011'|8|F_PRIM/16|1.475|
|DEC5|'100'|16|F_PRIM/32|0.7375|



Table 67 CTRL_RATE Register bit description 

**Murata Electronics Oy** SCH16T 

Doc.No. 11624 Rev. 6 

www.murata.com 



<!-- page 57 -->

57 (65) 

**CONFIDENTIAL** 



|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|DYN_RATE_XYZ1|Dynamic Range for RATE_X1/Y1/Z1 outputs.|[14:12]|3b001|
|DYN_RATE_XYZ2|Dynamic Range for RATE_X2/Y2/Z2 outputs.|[11:9]|3b001|
|DEC_RATE_Z2|Decimation ratio for RATE_Z2 output|[8:6]|3b000|
|DEC_RATE_Y2|Decimation ratio for RATE_Y2 output|[5:3]|3b000|
|DEC_RATE_X2|Decimation ratio for RATE_X2 output|[2:0]|3b000|



Table 68 CTRL_ACC12 Register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|DYN_ACC_XYZ1|Dynamic Range for ACC_X1/Y1/Z1 outputs.|[14:12]|3b001|
|DYN_ACC_XYZ2|Dynamic Range for ACC_X2/Y2/Z2 outputs.|[11:9]|3b001|
|DEC_ACC_Z2|Decimation ratio for ACC_Z2 output|[8:6]|3b000|
|DEC_ACC_Y2|Decimation ratio for ACC_Y2 output|[5:3]|3b000|
|DEC_ACC_X2|Decimation ratio for ACC_X2 output|[2:0]|3b000|



Table 69 CTRL_ACC3 Register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset value**|
|---|---|---|---|
|DYN_ACC_XYZ3|Dynamic Range for ACC_X3/Y3/Z3 outputs.|[2:0]|3b000|



# **7.4.3 Saturation flag user control** 

Table 70 Registers for saturation flag user control 

|**Register Name**|**Register Description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|CTRL_RATE_FLAG_1|RATE_XYZ Pre PP SAT_OK Filter user configuration|RW|D0|15h002B|
|CTRL_RATE_FLAG_2|RATE_XYZ PP SAT_OK Filter user configuration|RW|D0|15h002C|
|CTRL_ACC_FLAG_1|ACC_XYZ Pre PP SAT_OK Filter user configuration|RW|D0|15h002D|
|CTRL_ACC_FLAG_2|ACC_XYZ PP SAT_OK Filter user configuration|RW|D0|15h002E|



Any change to the saturation flag user control registers must be verified on system level to ensure that the desired safety functionality can be achieved with selected settings. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 58 -->

58 (65) 

**CONFIDENTIAL** 



Table 71 CTRL_RATE_FLAG_1 register bit description 

|**Bit Name**|**Bit Description**|**Bits**|**Reset**<br>**Value**|
|---|---|---|---|
|RATE_Z_SAT_CTRL1|User configuration for filtering saturation status flags based on consecutive flag<br>count before post-processing blocks:|[14:10]|5d00000|
||Analog saturation filter parameters:|||
|RATE_Y_SAT_CTRL1|Fault count range = 1-60<br>Fault count = (4-bit decimal string [4:1]) * 4, (Min = 1)<br>Nominal flag detection frequency = 1.5 kHz|[9:5]|5d00000|
|RATE_X_SAT_CTRL1|Digital saturation filter parameters:<br>Fault count range = 1-496<br>Fault count = (5-bit decimal string [4:0]) * 16, (Min = 1)<br>Nominal flag detection frequency = 11.8 kHz|[4:0]|5d00000|



Table 72 CTRL_RATE_FLAG_2 register bit description 

|**Bit Name**|**Bit Description**|**Bits**|**Reset**<br>**Value**|
|---|---|---|---|
|RATE_Z_SAT_CTRL2|User configuration for filtering saturation status flags based on consecutive flag<br>count for post-processing blocks (low pass filter, dynamic range scaling and<br>decimation/interpolation):|[14:10]|5d00000|
|RATE_Y_SAT_CTRL2|Digital saturation filter parameters:|[9:5]|5d00000|
|RATE_X_SAT_CTRL2|Fault count range = 1-496<br>Fault count = (5-bit decimal string [4:0]) * 16, (Min = 1)<br>Nominal flag detection frequency = 11.8 kHz|[4:0]|5d00000|



Table 73 CTRL_ACC_FLAG_1 register bit description 

|**Bit Name**|**Bit Description**|**Bits**|**Reset**<br>**Value**|
|---|---|---|---|
|ACC_Z_SAT_CTRL1|User configuration for filtering saturation status flags based on consecutive flag<br>count before post-processing blocks:|[14:10]|5d00000|
|ACC_Y_SAT_CTRL1|Digital saturation filter parameters:<br>Fault count range = 1-496|[9:5]|5d00000|
|ACC_X_SAT_CTRL1|Fault count = (5-bit decimal string [4:0]) * 16, (Min = 1)<br>Nominal flag detection frequency = 11.8 kHz|[4:0]|5d00000|



Table 74 CTRL_ACC_FLAG_2 register bit description 

|**Bit Name**|**Bit Description**|**Bits**|**Reset**<br>**Value**|
|---|---|---|---|
|ACC_Z_SAT_CTRL2|User configuration for filtering saturation status flags based on consecutive flag<br>count for post-processing blocks (low pass filter, dynamic range scaling and<br>decimation/interpolation):|[14:10]|5d00000|
|ACC_Y_SAT_CTRL2<br>ACC_X_SAT_CTRL2|Digital saturation filter parameters:<br>Fault count range = 1-496<br>Fault count = (5-bit decimal string [4:0]) * 16, (Min = 1)<br>Nominal flag detection frequency = 11.8 kHz|[9:5]<br>[4:0]|5d00000<br>5d00000|



**Murata Electronics Oy** 

SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 59 -->

59 (65) 

**CONFIDENTIAL** 



# **7.4.4 User interface control** 

Table 75 User interface control register 

|**Register name**|**Register description**|**R/RW**|**SPI frame**<br>**bit D**|**Public**<br>**address**|
|---|---|---|---|---|
|CTRL_USER_IF|User controls for SYNC, Data Ready, Strength of SPI PD/PU,<br>slew rate ctrl, hi-speed|RW|D0|15h0033|



Table 76 CTRL_USER_IF register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|SPI_SUPPLY|SPI_MISO and DRY buffer supply range:<br>x0 - 3.3 V+/-10% or 2.5 V+/-10% (default)<br>01 - 1.8 V+/-8%<br>User must write bits to ‘01’ if 1.8V VDDIO voltage is used.|[15:14]|2b00|
|FTREE_TDEL|Typical delay time of 1st level status clearance. When user reads data register, the<br>associated 1st level status register is cleared after TDEL.<br>00 - 0.078 ms<br>01 - 0.625 ms<br>10 - 2.5 ms (default)<br>11 – 5 ms|[13:12]|2b10|
|SYNC_POL|SYNC polarity control.<br>0 - high active (rising edge) (default)<br>1 - low active (falling edge).|[11:11]|1b0|
|SYNC_TOC_TH|SYNC time-out counter control. Counter starts to increase value after rising edge of<br>DRY_SYNC. When counter reaches threshold value selected by SYNC_TOC_TH,<br>data collection is restarted. Counter is reset by falling edge of DRY_SYNC.<br>00 - 2^15 x MCLK (1.275...1.448 ms)<br>01 - 2^16 x MCLK (2.550...2.896 ms)<br>10 - 2^17 x MCLK (5.100...5.792 ms)<br>11 - 2^18 x MCLK (10.199...11.584 ms)|[10:9]|2b00|
|SYNC_DEC_EN|Enables data freezing for Decimated output registers and their corresponding data<br>counter registers. Can be set both simultaneously and separately with<br>SYNC_INTP_EN. If user enables SYNC and Data Ready simultaneously, Data<br>Ready takes priority.<br>0 - Disable<br>1 - Enable|[8:8]|1b0|
|SYNC_INTP_EN|Enables data freezing for interpolated output registers and their corresponding data<br>counter registers. Can be set both simultaneously and separately with<br>SYNC_DEC_EN. If user enables SYNC and Data Ready simultaneously, Data<br>Ready takes priority.<br>0 - Disable<br>1 - Enable|[7:7]|1b0|
|DRY_POL|Data Ready polarity control.<br>0 - high active (default)<br>1 - low active|[6:6]|1b0|
|DRY_DRV_EN|Enables Data Ready function. Writing this bit to 1 disables SYNC function, as they<br>cannot be used simultaneously due to shared I/O pin.<br>1 - DRY buffer enabled<br>0 - DRY buffer disabled.|[5:5]|1b0|
|SPI_PULL_WEAK|Control of SPI pull-down resistor strength<br>0- strong pull-down (default)<br>1 - weak pull-down.|[4:4]|1b0|
|MISO_SR_CTRL|MISO Slew Rate control<br>0 - SR control disabled without static current (fast rise/fall time ~<1ns). (This option|[3:3]|1b1|



**Murata Electronics Oy** SCH16T 

Doc.No. 11624 

Rev. 6 

www.murata.com 



<!-- page 60 -->

**CONFIDENTIAL** 



# 60 (65) 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
||is not supported by Murata)<br>1 - SR control enabled with static current (default)|||
|DRY_SR_CTRL|DRY Slew Rate control<br>0 - SR control disabled without static current (fast rise/fall time ~<1ns). (This option<br>is not supported by Murata)<br>1 - SR control enabled with static current (default)|[2:2]|1b1|
|DRY_HI_SPD|DRY High-Speed mode control<br>0 – 10 MHz mode, SafeSPI2 standard<br>1 – 25 MHz mode, non-standard high-speed SPI|[1:1]|1b0|
|MISO_HI_SPD|MISO High Speed mode control<br>0 – 10 MHz mode, SafeSPI2 standard<br>1 – 25 MHz mode, non-standard high-speed SPI|[0:0]|1b0|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 61 -->

61 (65) 



# **CONFIDENTIAL** 

# **7.4.5 Self-test controls** 

Table 77 Register for self-test controls 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|CTRL_ST|Self-test controls (enable ST and/or request STS)|RW|D0|15h0034|



Table 78 CTRL_ST register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|Reserved|Reserved|[12:12]|1b0|
|RATE_STC_CTRL|Disable RATE_Z, RATE_Y and RATE_X continuous self-tests by writing bits to<br>'000'|[11:9]|3b111|
|ACC_Z_STC_MASK1|Mask ACC_Z continuous self-test flag (STC_N) by writing bit to '0'|[8:8]|1b1|
|ACC_Y_STC_MASK1|Mask ACC_Y continuous self-test flag (STC_N) by writing bit to '0'|[7:7]|1b1|
|ACC_X_STC_MASK1|Mask ACC_X continuous self-test flag (STC_N) by writing bit to '0'|[6:6]|1b1|
|ACC_Z_STC_MASK2|Mask ACC_Z continuous self-test flag (STC_SDD) by writing bit to '0'|[5:5]|1b1|
|ACC_Y_STC_MASK2|Mask ACC_Y continuous self-test flag (STC_SDD) by writing bit to '0'|[4:4]|1b1|
|ACC_X_STC_MASK2|Mask ACC_X continuous self-test flag (STC_SDD) by writing bit to '0'|[3:3]|1b1|
|ACC_STS_CTRL|Disable ACC start-up self-test by writing bit to '0'|[2:2]|1b1|
|Reserved|Reserved|[1:1]|1b1|
|ACC_STS_REQ|Request ACC start-up self-test by writing bit to '1'. The user must write bit back<br>to '0' after test is completed. Recommended wait time before writing '0' is<br>155ms. Test is done automatically during start-up.|[0:0]|1b0|



# **7.4.6 Sensor mode control and soft reset** 

Table 79 Registers for setting EN_SENSOR, EOI and soft reset 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|CTRL_MODE|EOI, EN_SENSOR|RW|D0|15h0035|
|CTRL_RESET|SPI soft reset command|RW|D0|15h0036|



Table 80 CTRL_MODE register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|Reserved|Reserved|[3:2]|2b00|
||End of Initialization. Writing bit to '1' locks all R/W registers except soft reset control and|||
|EOI_CTRL|SYS_TEST. Freezes also start-up status flag status in 1st level status registers. Reset of<br>component is needed to set EOI back to '0'.|[1:1]|1b0|
|EN_SENSOR|Enable RATE and ACC measurement. Write bit to '1' according to start-up sequence.|[0:0]|1b0|



Table 81 CTRL_RESET register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|SOFTRESET_CTRL|Writing 0x0000A (4b1010) to this field generates a SPI soft reset. SPI<br>Communication is not allowed during 2ms after SPI SOFTRESET.|[3:0]|4b0000|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 Rev. 6 



<!-- page 62 -->

62 (65) 

**CONFIDENTIAL** 



# **7.4.7 Whoami, traceability, identification, and spare registers** 

Table 82 Miscellaneous registers 

|**Register name**|**Register description**|**R/RW**|**SPI frame bit D**|**Public address**|
|---|---|---|---|---|
|SYS_TEST|Empty register for testing read/write access|RW|D0|15h0037|
|SPARE_1|Reserved|R|D0|15h0038|
|SPARE_2|Reserved|R|D0|15h0039|
|SPARE_3|Reserved|R|D0|15h003A|
|ASIC_ID|ASIC revision|R|D0|15h003B|
|COMP_ID|Component type|R|D0|15h003C|
|SN_ID1|Component Serial Number field 1|R|D0|15h003D|
|SN_ID2|Component Serial Number field 2|R|D0|15h003E|
|SN_ID3|Component Serial Number field 3|R|D0|15h003F|



The component is traceable by a unique electronically readable serial number that matches to the component markings. Serial number is stored in NVM registers SN_ID1, SN_ID2 and SN_ID3. Serial number string format: <mark>DDDYYFHHHHH</mark> 01 

Table 83 Serial number calculation example where final serial number result: <mark>3542301497H</mark> 01 

|**Symbol**|DDDYY|F|HHHH|H01|
|---|---|---|---|---|
|**Meaning**|Date code|-|Running number|Product code|
|**Register and bits**|SN_ID2 [15:0]|SN_ID1 [3:0]|SN_ID3 [15:0]|Not stored to<br>register|
|**Example register**<br>**content**|0x8A5F|0x0|0x1497|-|
|**Processing**|16-bit unsigned integer to decimal<br>string, 0....65535|4-bit hex to<br>string, 0...F|16-bit hexadecimal<br>running number|Fixed value|
|**Result**|35423|0|1497|H01|



Table 84 SYS_TEST register bit description 

|**Bit name**|**Bit description**|**Bits**|**Reset**<br>**value**|
|---|---|---|---|
|SYS_TEST|16-bit read/write register which can be used to check accessibility of the device, or if<br>multiple devices are connected to the SPI bus to check if CS signals are working properly.<br>Due to off-frame protocol, test sequence should be as follows:<br>1. Write data into SYS_TEST register<br>2. Read SYS_TEST register content<br>3. Issue a dummy read command to receive response from previous frame<br>SYS_TEST register is not locked by EOI bit.|[15:0]|16h0000|



Table 85 ASIC_ID register bit description 

|**Bit name**|**Bit description**|**Bits**|
|---|---|---|
|ASIC_TYPE|ASIC type|[11:8]|
|ASIC_REV|ASIC major revision|[7:4]|
|ASIC_REV_MINOR|ASIC minor revision|[3:0]|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 63 -->

63 (65) 

**CONFIDENTIAL** 



Table 86 COMP_ID register bit description 

|**Bit name**|**Bit description**|**Bits**|
|---|---|---|
|COMP_ID|Component version. e.g., SCH16T-K01 = 0000000000100011|[15:0]|



## Table 87 SN_ID1 register bit description 

|**Bit name**|**Bit description**|**Bits**|
|---|---|---|
|SN_ID1|“F” part of component serial number (4-bit hex to string, 0...F)<br>Format: DDDYYFHHHHH01|[3:0]|



## Table 88 SN_ID2 register bit description 

|**Bit name**|**Bit description**|**Bits**|
|---|---|---|
||“DDDYY” part of serial number (16-bit unsigned integer to decimal string, 0....65535). DDD is the||
|SN_ID2|production day as ordinal number from the beginning of the year and YY is production year.<br>Format: DDDYYFHHHHH01|[15:0]|



Table 89 SN_ID3 register bit description 

|**Bit name**|**Bit description**|**Bits**|
|---|---|---|
|SN_ID3|“HHHH” part of component serial number (16-bit hexadecimal running number)<br>Format: DDDYYFHHHHH01|[15:0]|



**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 64 -->

64 (65) 

**CONFIDENTIAL** 



# **8 Application information** 

## **8.1 Application circuitry and external component characteristics** 



Figure 18 Application schematic 

Table 90 External component description for SCH16T series 

|**Symbol**|**Description**|**Min**|**Nom**|**Max**|**Unit**|
|---|---|---|---|---|---|
|C1<br>C3|Decoupling capacitor between VREGD/VREGD2 (C1)/3p3 pin17 (C3) and GND<br>(ESR <100 mOhm @ 1 MHz)|0.7|1|1.3|uF|
|C2|Decoupling capacitor between VREGA/VREGA2 and GND<br>(ESR <100 mOhm @ 1 MHz)|4.6|10|15|uF|
|C4<br>C5|Decoupling capacitor between V3p3 pin8 (C4)/VDDIO (C5) and GND<br>(ESR <100 mOhm @ 1 MHz)|70|100|130|nF|



All GND and I/O needs to be connected as shown in the schematic above. Additional notes about the pin connections: 

- TA8 and TA9 must be connected to ground if they are not used by MCU because TA chip select address needs to be defined. Default ‘00’ TA chip select address is used for example operations. 

- If EXTRESN pin is not driven by MCU, it must be connected to VDDIO directly or with max 20kohm PU resistor. 

- DRY_SYNC must be left floating if these features are not used. 

- N.C. pin 2 must be left floating as indicated by schematic. 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 



<!-- page 65 -->

65 (65) 

**CONFIDENTIAL** 



## **8.2 General application PCB layout** 

A PCB layout example of the SCH16T series component is presented in _Figure 19 Reference PCB layout_ . The presented layout can be used as such or only as reference. When designing the PCB, it is advised to follow general layout guidelines below: 

- Connect SMD decoupling capacitors right next to the component on top layer. 

- Each ground pin should be connected to the ground directly. 

- A ground plane under the component is not recommended due to possible electromagnetic interference effect to the SCH16T series component (ground vias and lines can be freely routed). 

- Signal lines of this component can be freely routed under the component. It is expected that signal lines of other components have also no effect on the SCH16T series component, but the user is advised to verify functionality before implementation. 

- Keep all routing as low resistance as possible. 



Figure 19 Reference PCB layout 

## **8.3 Assembly instructions** 

Application PCB design, conformal coating, mechanical shocks, material selection, environment and component assembly process can impact the sensor performance. Please refer to Assembly instructions for SCH1000 series (Murata APP 10871) for related details. 

_Murata reserves all rights to modify this document without prior notice._ 

**Murata Electronics Oy** www.murata.com 

SCH16T 

Doc.No. 11624 

Rev. 6 

