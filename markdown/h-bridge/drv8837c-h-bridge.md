# drv8837c-h-bridge

*Source: `original/h-bridge/drv8837c-h-bridge.pdf` (23 pages)*

<!-- page 1 -->

Tools & Support & Software Community 

Sample & Buy 

Product Folder 

Technical Documents 

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 



# **DRV8837C 1-A Low-Voltage H-Bridge Driver** 

## **1 Features** 

- 1• H-Bridge Motor Driver 

   - Drives a DC Motor or Other Loads 

   - Low MOSFET On-Resistance: HS + LS 1 Ω 

- 1-A Maximum Drive Current 

- 0- to 11-V Operating Supply-Voltage Range 

- Standard PWM Interface (IN1/IN2) 

- Low-Power Sleep Mode With 120-nA Maximum Sleep Current 

   - nSLEEP pin 

- Small Package and Footprint 

   - 8 WSON (With Thermal Pad) 

   - 2.0 × 2.0 mm 

- Protection Features 

   - VCC Undervoltage Lockout (UVLO) 

   - Overcurrent Protection (OCP) 

   - Thermal Shutdown (TSD) 

## **2 Applications** 

- Cameras 

- DSLR Lenses 

- Consumer Products 

## **3 Description** 

The DRV8837C device provides an integrated motor driver solution for cameras, consumer products, toys, and other low-voltage or battery-powered motion control applications. The device can drive one DC motor or other devices like solenoids. The output driver block consists of N-channel power MOSFETs configured as an H-bridge to drive the motor winding. An internal charge pump generates needed gate drive voltages. 

The DRV8837C device can supply up to 1 A of output current. The device operates on a motor power supply voltage from 0 to 11 V, and control logic can operate on 1.8-V to 5-V rails. 

The DRV8837C device has a PWM (IN/IN) input interface. 

Internal shutdown functions are provided for overcurrent protection, short circuit protection, undervoltage lockout, and overtemperature. 

### **Device Information**<sup>**(1)**</sup> 

|**PART NUMBER**|**PACKAGE**|**BODY SIZE(NOM)**|
|---|---|---|
|DRV8837C|WSON(8)|2.00 mm × 2.00 mm|



   - (1) For all available packages, see the orderable addendum at the end of the data sheet. 

- Toys 

- Robotics 

- Medical Devices 

### **DRV8837C Simplified Diagram** 



<!-- Start of picture text -->
0 to 11 V<br>3.3 or 5.0 V<br>DRV8837C<br>VCC<br>PWM<br>H-Bridge PWM  1 A BLDCBDC<br>Driver<br>nSLEEP Protection<br>Controller<br><!-- End of picture text -->

Copyright © 2016, Texas Instruments Incorporated 

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA. 



<!-- page 2 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **Table of Contents** 

|**1**<br>**Features**.................................................................. 1|**8**<br>**Appl**|**ication and Implementation**........................ 11|
|---|---|---|
|**2**<br>**Applications**........................................................... 1|8.1|Application Information............................................ 11|
|**3**<br>**Description**............................................................. 1|8.2|Typical Application .................................................. 11|
|**4**<br>**Revision History**..................................................... 2|**9**<br>**Pow**<br>|**er Supply Recommendations**...................... 12<br>|
|**5**<br>**Pin Configuration and Functions**......................... 3|9.1<br><br>|Bulk Capacitance .................................................... 12<br>|
|**6**<br>**Specifications**......................................................... 4|**10**<br>**Layo**<br>|**ut**................................................................... 14<br>|
|6.1<br>Absolute Maximum Ratings ...................................... 4|10.1<br>|Layout Guidelines ................................................. 14<br>|
|6.2<br>ESD Ratings.............................................................. 4|10.2<br>|Layout Example .................................................... 14<br>|
|6.3<br>Recommended Operating Conditions....................... 4|10.3<br><br>|Power Dissipation ................................................. 14<br>|
|6.4<br>Thermal Information.................................................. 4|**11**<br>**Devi**|**ce and Documentation Support**................. 15|
|6.5<br>Electrical Characteristics........................................... 5|11.1|Documentation Support ........................................ 15|
|6.6<br>Timing Requirements................................................ 6|11.2|Receiving Notification of Documentation Updates 15|
|6.7<br>Typical Characteristics.............................................. 7|11.3|Community Resources.......................................... 15|
|**7**<br>**Detailed Description**.............................................. 8|11.4<br>|Trademarks........................................................... 15<br>|
|7.1<br>Overview ................................................................... 8|11.5|Electrostatic Discharge Caution............................ 15<br>|
|7.2<br>Functional Block Diagram ......................................... 8|11.6|Glossary................................................................ 15|
|7.3<br>Feature Description................................................... 9|**12**<br>**Mec**<br>|**hanical, Packaging, and Orderable**<br>|
|7.4<br>Device Functional Modes........................................ 10|**Infor**|**mation**........................................................... 15|



## **4 Revision History** 

NOTE: Page numbers for previous revisions may differ from page numbers in the current version. 

**Changes from Original (July 2016) to Revision A** 

|**Changes from Original (July 2016) to Revision A**<br>**Page**|
|---|
|•<br>Changed the device status from_Product Preview_ to _Production Data_.................................................................................. 1|



2 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 3 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **5 Pin Configuration and Functions** 



<!-- Start of picture text -->
DSG Package<br>8-Pin WSON With Exposed Thermal Pad<br>Top View<br>VM 1 8  VCC<br>OUT1 2 7  nSLEEP<br>Thermal<br>Pad<br>OUT2 3 6  IN1<br>GND 4 5  IN2<br>Not to scale<br><!-- End of picture text -->

### **Pin Functions** 

|**PI**|**N**|**TYPE**|**DESCRIPTION**|
|---|---|---|---|
|**NAME**|**NO.**|||
|**POWER AND **|**GROUND**|||
|GND|4|PWR|Device ground<br>Thispin must be connected to the PCBground.|
|VCC|8|PWR|Logic power supply<br>Bypass thispin to the GND pin with a 0.1-µF ceramic capacitor rated for VCC.|
|VM|1|PWR|Motor power supply<br>Bypass thispin to the GND pin with a 0.1-µF ceramic capacitor rated for VM.|
|**CONTROL**||||
|IN1|6|I|IN1 input|
|IN2|5|I|IN2 input|
|nSLEEP|7|I|Sleep mode input<br>When this pin is in logic low, the device enters low-power sleep mode. The device operates<br>normallywhen thispin is logic high. The pin has an internalpulldown resistor to GND.|
|**OUTPUT**||||
|OUT1|2|O|Motor output|
|OUT2|3|O|Connect this pin to the motor winding.|



_Submit Documentation Feedback_ 

3 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 4 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

# **6 Specifications** 

## **6.1 Absolute Maximum Ratings** 

Over operating free-air temperature range (unless otherwise noted)<sup>(1)(2)</sup> 

|||**MIN**|**MAX**|**UNIT**|
|---|---|---|---|---|
|Motorpower-supply voltage|VM|–0.3|12|V|
|Logic power-supply voltage|VCC|–0.3|7|V|
|Control pin voltage|IN1, IN2, nSLEEP|–0.5|7|V|
|Peak drive current|OUT1, OUT2|Internall|ylimited|A|
|Operatingvirtual junction temp|erature, TJ|–40|150|ºC|
|Storage temperature, Tstg||–60|150|ºC|



- (1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under _Recommended Operating Conditions_ is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. 

(2) All voltage values are with respect to network ground pin. 

## **6.2 ESD Ratings** 

||||**VALUE**|**UNIT**|
|---|---|---|---|---|
|V|Electrostatic|Human-bodymodel(HBM),per ANSI/ESDA/JEDEC JS-001<sup>(1)</sup>|±4000|V|
|(ESD)|discharge|Charged-device model(CDM),per JEDEC specification JESD22-C101<sup>(2)</sup>|±1000||



- (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. 

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. 

## **6.3 Recommended Operating Conditions** 

Over operating free-air temperature range (unless otherwise noted) 

|||**MIN**|**MAX**|**UNIT**|
|---|---|---|---|---|
|VVM|Motorpower-supply voltage|0|11|V|
|VCC|Logic power-supply voltage|1.8|7|V|
|IOUT|Motorpeak current|0|1|A|
|fPWM|Externallyapplied PWM frequency|0|250|kHz|
|VLOGIC|Logic level input voltage|0|5.5|V|
|TA|Operatingambient temperature|–40|85|°C|



## **6.4 Thermal Information** 

over operating free-air temperature range (unless otherwise noted) 

|||**DRV8837C**||
|---|---|---|---|
||**THERMAL METRIC **<sup>**(1)**</sup>|**DSG(WSON)**|**UNIT**|
|||**8 PINS**||
|RθJA|Junction-to-ambient thermal resistance|60.9|°C/W|
|RθJC(top)|Junction-to-case(top)thermal resistance|71.4|°C/W|
|RθJB|Junction-to-board thermal resistance|32.2|°C/W|
|ψJT|Junction-to-top characterization parameter|1.6|°C/W|
|ψJB|Junction-to-board characterization parameter|32.8|°C/W|
|RθJC(bot)|Junction-to-case(bottom) thermal resistance|9.8|°C/W|



- (1) For more information about traditional and new thermal metrics, see the _Semiconductor and IC Package Thermal Metrics_ application report. 

4 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 5 -->

**DRV8837C** SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **6.5 Electrical Characteristics** 

TA = 25°C, over recommended operating conditions unless otherwise noted 

||**PARAMETER**|**TEST CONDITIONS**|**MIN**|**TYP**|**MAX**|**UNIT**|
|---|---|---|---|---|---|---|
|**POWER**|**SUPPLIES(VM, VCC)**||||||
|VVM|VM operatingvoltage||0||11|V|
|I|VM oeratin slcrrent|VVM = 5 V; VCC= 3 V;<br>No PWM||40|100|μA|
|VM|pg uppy u|VVM = 5 V; VCC= 3 V;<br>50 kHz PWM||0.8|1.5|mA|
|IVMQ|VM sleep mode supply current|VVM = 5 V; VCC= 3 V;<br>nSLEEP = 0||30|95|nA|
|VCC|VCC operatingvoltage||1.8||7|V|
|||VVM = 5 V; VCC= 3 V;<br>No PWM||300|500|μA|
|IVCC|VCCoperating supply current|VVM = 5 V; VCC= 3 V;<br>50 kHz PWM||0.7|1.5|mA|
|IVCCQ|VCCsleep mode supply current|VVM = 5 V; VCC= 3 V;<br>||5|25|nA|
|||nSLEEP = 0|||||
|**CONTR**|**OL INPUTS(IN1/PH, IN2/EN, nSLEEP**|**)**|||||
|VIL|Input logic-low voltage||||0.25 × VCC|V|
|VIH|Input logic-high voltage||0.5 × VCC|||V|
|VHYS|Input logic hysteresis|||0.08 × VCC||V|
|IIL|Input logic-low current|VINx = 0 V|–5||5|μA|
|IIH|Input logic-high current|VINx = 3.3 V|||50|μA|
|RPD|Pulldown resistance|||100||kΩ|
|**MOTOR**|**DRIVER OUTPUTS(OUT1, OUT2)**||||||
|RDS(ON)|HS + LS FET on-resistance|VVM = 5 V; VCC= 3.3 V;<br>IO = 200 mA; TJ = 25°C||1000||mΩ|
|IOFF|Off-state leakage current|VOUTx = 0 V|–200||200|nA|
|**PROTE**|**CTION CIRCUITS**||||||
|||VCC falling|||1.7|V|
|VUVLO|VCCundervoltage lockout|VCC rising|||1.8|V|
|IOCP|Overcurrent protection triplevel||1.2|||A|
|tDEG|Overcurrent deglitch time|||1||μs|
|tRETRY|Overcurrent retrytime|||1||ms|
|TTSD <sup>(1)</sup>|Thermal shutdown temperature|Die temperature TJ|150|160|180|°C|



(1) Not tested in production; limits are based on characterization data 

_Submit Documentation Feedback_ 

5 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 6 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **6.6 Timing Requirements** 

TA = 25°C, VVM = 5 V, VCC = 3 V, RL = 20 Ω 

|**NO.**||||**MIN**|**MAX**|**UNIT**|
|---|---|---|---|---|---|---|
|1|t7|Output enable time|||300|ns|
|2|t8|Output disable time|||300|ns|
|3|t9|Delay time, INx high to OUTx high|SFi 1||160|ns|
|4|t10|Delay time, INx low to OUTx low|eegure.||160|ns|
|5|t11|Output rise time||20|188|ns|
|6|t12|Output fall time||20|188|ns|
|—|twake|Wake time, nSLEEP risingedge topart active|||30|μs|





<!-- Start of picture text -->
IN1<br>IN2<br>1 4 2<br>OUT1 z z<br>3<br>OUT2 z z<br>DRV8837C<br>80% 80%<br>OUTx<br>20% 20%<br>5<br>6<br><!-- End of picture text -->

**Figure 1. Input and Output Timing for DRV8837C** 

6 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 7 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **6.7 Typical Characteristics** 

Plots generated using characterization data. 



<!-- Start of picture text -->
70 100<br>65<br>80<br>60<br>55 60<br>50<br>40<br>45<br>40<br>20<br>35<br>30 0<br>-40 -20 0 20 40 60 80 100 -40 -20 0 20 40 60 80 100<br>Ambient Temperature ( q C) D001 Ambient Temperature (°C) D002<br>VVM = 5 V VCC = 3 V VVM = 5 V VCC = 3 V<br>Figure 2. VM Sleep Current vs Ambient Temperature Figure 3. VCC Sleep Current vs Ambient Temperature<br>0.575 0.58<br>0.57 0.56<br>0.565<br>0.54<br>0.56<br>0.52<br>0.555<br>0.5<br>0.55<br>0.48<br>0.545<br>0.54 0.46<br>0.535 0.44<br>-40 -20 0 20 40 60 80 100 -40 -20 0 20 40 60 80 100<br>Ambient Temperature ( q C) D003 Ambient Temperature ( q C) D004<br>VVM = 5 V VCC = 3 V VVM = 5 V VCC = 3 V<br>Figure 4. VM Operating Current vs Ambient Temperature Figure 5. VCC Operating Current vs Ambient Temperature<br>2.75<br>VM = 2 V, VCC = 2 V<br>2.5 VM = 5 V, VCC = 3 V<br>VM = 11 V, VCC = 7 V<br>2.25<br>2<br>1.75<br>1.5<br>1.25<br>1<br>0.75<br>0.5<br>-40 -20 0 20 40 60 80 100<br>Ambient Temperature (°C) D005<br>Figure 6. HS + LS RDS(ON) vs Ambient Temperature<br>VM Sleep Current (nA) VCC Sleep Current (nA)<br>VM Operating Current, 50 kHz PWM (mA) VCC Operating Current, 50 KHz PWM (mA)<br> HS+LS (R) : DS(ON)<br><!-- End of picture text -->

_Submit Documentation Feedback_ 7 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 8 -->

**DRV8837C** SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

# **7 Detailed Description** 

## **7.1 Overview** 

The DRV8837C device is an H-bridge driver that can drive one DC motor or other devices like solenoids. The outputs are controlled using a PWM interface (IN1/IN2). 

A low-power sleep mode is included, which can be enabled using the nSLEEP pin. 

This device greatly reduces the component count of motor driver systems by integrating the necessary driver FETs and FET control circuitry into a single device. In addition, the DRV8837C device adds protection features beyond traditional discrete implementations: undervoltage lockout, overcurrent protection, and thermal shutdown. 

## **7.2 Functional Block Diagram** 



<!-- Start of picture text -->
VM<br>Power<br>VM<br>VM<br>Charge Pump<br>VCC<br>Gate  OUT1<br>VCC Drive<br>Logic<br>nSLEEP VM BDCBDC<br>Core Logic<br>IN1<br>Gate  OUT2<br>Control Inputs<br>Drive<br>Overcurrent<br>IN2<br>Undervoltage<br>Thermal<br>GND PPAD<br><!-- End of picture text -->

Copyright © 2016, Texas Instruments Incorporated 

8 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 9 -->

**DRV8837C** SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **7.3 Feature Description** 

### **7.3.1 Bridge Control** 

The DRV8837C device is controlled using a PWM input interface, also called an IN/IN interface. Each output is controlled by a corresponding input pin. 

Table 1 shows the logic for the DRV8837C device. 

**Table 1. DRV8837C Device Logic** 

|**nSLEEP**|**IN1**|**IN2**|**OUT1**|**OUT2**|**FUNCTION (DC MOTOR)**|
|---|---|---|---|---|---|
|0|X|X|Z|Z|Coast|
|1|0|0|Z|Z|Coast|
|1|0|1|L|H|Reverse|
|1|1|0|H|L|Forward|
|1|1|1|L|L|Brake|



### **7.3.2 Sleep Mode** 

If the nSLEEP pin is brought to a logic-low state, the DRV8837C device enters a low-power sleep mode. In this state, all unnecessary internal circuitry is powered down. 

### **7.3.3 Power Supplies and Input Pins** 

The input pins can be driven within the recommended operating conditions with or without the VCC, VM, or both power supplies present. No leakage current path exists to the supply. Each input pin has a weak pulldown resistor (approximately 100 k Ω ) to ground. 

The VCC and VM supplies can be applied and removed in any order. When the VCC supply is removed, the device enters a low-power state and draws very little current from the VM supply. The VCC and VM pins can be connected together if the supply voltage is between 1.8 and 7 V. 

The VM voltage supply does not have any undervoltage-lockout protection (UVLO). As long as VCC > 1.8 V, the internal device logic remains active which means that the VM pin voltage can drop to 0 V, however, the load may not be sufficiently driven at low VM voltages. 

### **7.3.4 Protection Circuits** 

The DRV8837C is fully protected against VCC undervoltage, overcurrent, and overtemperature events. 

- **VCC undervoltage lockout** If at any time the voltage on the VCC pin falls below the undervoltage lockout threshold voltage, all FETs in the H-bridge are disabled. Operation resumes when the VCC pin voltage rises above the UVLO threshold. 

- **Overcurrent protection (OCP)** An analog current-limit circuit on each FET limits the current through the FET by removing the gate drive. If this analog current limit persists for longer than tDEG, all FETs in the H- bridge are disabled. Operation resumes automatically after tRETRY has elapsed. Overcurrent conditions are detected on both the high-side and low-side devices. A short to the VM pin, GND, or from the OUT1 pin to theOUT2 pin results in an overcurrent condition. 

- **Thermal shutdown (TSD)** If the die temperature exceeds safe limits, all FETs in the H-bridge are disabled. After the die temperature falls to a safe level, operation automatically resumes. 

**Table 2. Fault Behavior** 

|**FAULT**|**CONDITION**|**H-BRIDGE**|**RECOVERY**|
|---|---|---|---|
|VCC undervoltage (UVLO)|VCC < 1.7 V|Disabled|VCC > 1.8 V|
|Overcurrent (OCP)|IOUT> 1.2 A (MIN)|Disabled (retries<br>automatically)|tRETRYelapses|
|Thermal Shutdown (TSD)|TJ> 150°C (MIN)|Disabled (retries<br>automatically)|TJ< 150°C|



_Submit Documentation Feedback_ 

9 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 10 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **7.4 Device Functional Modes** 

The DRV8837C device is active unless the nSLEEP pin is brought logic low. In sleep mode the H-bridge FETs are disabled Hi-Z. The DRV8837C device is brought out of sleep mode automatically if nSLEEP is brought logic high. 

The H-bridge outputs are disabled during undervoltage lockout, overcurrent, and overtemperature fault conditions. 

**Table 3. Operation Modes** 

|**MODE**|**CONDITION**|**H-BRIDGE**|
|---|---|---|
|Operating|nSLEEP pin = 1|Operating|
|Sleep mode|nSLEEP pin = 0|Disabled|
|Fault encountered|Any fault condition met|Disabled(retries automatically)|



10 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 11 -->

**DRV8837C** SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

# **8 Application and Implementation** 

### **NOTE** 

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality. 

## **8.1 Application Information** 

The DRV8837C device is device is used to drive one DC motor or other devices like solenoids. The following design procedure can be used to configure the DRV8837C device. 

## **8.2 Typical Application** 



<!-- Start of picture text -->
VM<br>DRV8837C<br>0.1 µF 1 8 VCC<br>VM VCC<br>2 7 0.1 µF<br>OUT1 nSLEEP<br>3 6<br>OUT2 IN1<br>4 5<br>M<br>GND IN2<br>Copyright © 2016, Texas Instruments Incorporated<br>Thermal Pad<br><!-- End of picture text -->

**Figure 7. Schematic of DRV8837C Application** 

### **8.2.1 Design Requirements** 

Table 4 lists the required parameters for a typical usage case. 

**Table 4. System Design Requirements** 

|**DESIGN PARAMETER**|**REFERENCE**|**EXAMPLE VALUE**|
|---|---|---|
|Motor supply voltage|VM|9 V|
|Logic supply voltage|VCC|3.3 V|
|Target RMS current|IOUT|0.8 A|



### **8.2.2 Detailed Design Procedure** 

### **_8.2.2.1 Motor Voltage_** 

The appropriate motor voltage depends on the ratings of the motor selected and the desired RPM. A higher voltage spins a brushed dc motor faster with the same PWM duty cycle applied to the power FETs. A higher voltage also increases the rate of current change through the inductive motor windings. 

### **_8.2.2.2 Low-Power Operation_** 

When entering sleep mode, TI recommends setting all inputs as a logic low to minimize system power. 

_Submit Documentation Feedback_ 

11 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 12 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

### **8.2.3 Application Curves** 



<!-- Start of picture text -->
Figure 8. 50% Duty Cycle, Forward Direction Figure 9. 50% Duty Cycle, Reverse Direction<br>Figure 10. 20% Duty Cycle, Forward Direction Figure 11. 20% Duty Cycle, Reverse Direction<br><!-- End of picture text -->

# **9 Power Supply Recommendations** 

## **9.1 Bulk Capacitance** 

Having appropriate local bulk capacitance is an important factor in motor-drive system design. It is generally beneficial to have more bulk capacitance, while the disadvantages are increased cost and physical size. 

The amount of local capacitance needed depends on a variety of factors, including: 

- The highest current required by the motor system 

- The power-supply capacitance and ability to source current 

- The amount of parasitic inductance between the power supply and motor system 

- The acceptable voltage ripple 

- The type of motor used (brushed dc, brushless dc, stepper) 

- The motor braking method 

The inductance between the power supply and motor drive system limits the rate at which current can change from the power supply. If the local bulk capacitance is too small, the system responds to excessive current demands or dumps from the motor with a change in voltage. When adequate bulk capacitance is used, the motor voltage remains stable and high current can be quickly supplied. 

The data sheet generally provides a recommended value, but system-level testing is required to determine the appropriate size of bulk capacitor. 

12 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 13 -->

**DRV8837C** SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

## **Bulk Capacitance (continued)** 



<!-- Start of picture text -->
Parasitic Wire<br>Inductance<br>Power Supply Motor Drive System<br>VM<br>+ + Motor<br>– Driver<br>GND<br>Local IC Bypass<br>Bulk Capacitor Capacitor<br><!-- End of picture text -->

**Figure 12. Example Setup of Motor Drive System With External Power Supply** 

The voltage rating for bulk capacitors should be higher than the operating voltage, to provide margin for cases when the motor transfers energy to the supply 

_Submit Documentation Feedback_ 

13 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 14 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

# **10 Layout** 

## **10.1 Layout Guidelines** 

The VM and VCC pins should be bypassed to GND using low-ESR ceramic bypass capacitors with a recommended value of 0.1 µF rated for the VM and VCC supplies. These capacitors should be placed as close to the VM and VCC pins as possible with a thick trace or ground plane connection to the device GND pin. In addition bulk capacitance is required on the VM pin. 

## **10.2 Layout Example** 



<!-- Start of picture text -->
0.1 µF 0.1 µF<br>VM VCC<br>OUT1 SLEEPn<br>OUT2 IN1<br>GND IN2<br><!-- End of picture text -->

**Figure 13. Simplified Layout Example** 

## **10.3 Power Dissipation** 

Power dissipation in the DRV8837C device is dominated by the power dissipated in the output FET resistance, or RDS(ON). Use Equation 1 to estimate the average power dissipation when running a brushed-DC motor. 

- 2 

- PTOT � RDS(ON) � (IOUT(RMS) ) 

where 

- PTOT is the total power dissipation 

- RDS(ON) is the resistance of the HS plus LS FETs 

- IOUT(RMS) is the RMS or DC output current being supplied to the load 

- (1) 

The maximum amount of power that can be dissipated in the device is dependent on ambient temperature and heatsinking. 

### **NOTE** 

The value of RDS(ON) increases with temperature, so as the device heats, the power dissipation increases. 

The DRV8837C device has thermal shutdown protection. If the die temperature exceeds approximately 150°C, the device is disabled until the temperature drops to a safe level. 

Any tendency of the device to enter thermal shutdown is an indication of either excessive power dissipation, insufficient heatsinking, or too high an ambient temperature. 

14 _Submit Documentation Feedback_ 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 15 -->

**DRV8837C** 

SLVSD61A –JULY 2016–REVISED JULY 2016 

**www.ti.com** 

# **11 Device and Documentation Support** 

## **11.1 Documentation Support** 

### **11.1.1 Related Documentation** 

For related documentation see the following: 

- _Calculating Motor Driver Power Dissipation_ (SLVA504) 

- _DRV8837C Evaluation Module User's Guide_ (SLVUAS3) 

- _Understanding Motor Driver Current Ratings_ (SLVA505) 

## **11.2 Receiving Notification of Documentation Updates** 

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper right corner, click on _Alert me_ to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document. 

## **11.3 Community Resources** 

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use. 

**TI E2E™Online Community** **_TI's Engineer-to-Engineer (E2E) Community._** Created to foster collaboration among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers. 

- **Design Support** **_TI's Design Support_** Quickly find helpful E2E forums along with design support tools and contact information for technical support. 

## **11.4 Trademarks** 

E2E is a trademark of Texas Instruments. 

All other trademarks are the property of their respective owners. 

## **11.5 Electrostatic Discharge Caution** 



This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage. 

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. 

## **11.6 Glossary** 

SLYZ022 — _TI Glossary_ . 

This glossary lists and explains terms, acronyms, and definitions. 

# **12 Mechanical, Packaging, and Orderable Information** 

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation. 

_Submit Documentation Feedback_ 

15 

Copyright © 2016, Texas Instruments Incorporated 

Product Folder Links: _DRV8837C_ 



<!-- page 16 -->

**PACKAGE OPTION ADDENDUM** 

www.ti.com 

10-Nov-2025 

## **PACKAGING INFORMATION** 

|**Orderable part number**<br>DRV8837CDSGR|**Status**<br>(1)<br>Active|**Material type**<br>(2)<br>Production|**Package | Pins**<br>WSON(DSG) |8|**Package qty | Carrier**<br>3000|LARGE T&R|**RoHS**<br>(3)<br>Yes|**Lead finish/**<br>**Ball material**<br>(4)<br>NIPDAU|**MSL rating/**<br>**Peak reflow**<br>(5)<br>Level-1-260C-UNLIM|**Op temp (°C)**<br>-40 to 85|**Part marking**<br>(6)<br>837C|
|---|---|---|---|---|---|---|---|---|---|
|DRV8837CDSGR.B|Active|Production|WSON(DSG) |8|3000|LARGE T&R|Yes|NIPDAU|Level-1-260C-UNLIM|-40 to 85|837C|
|DRV8837CDSGRG4|Active|Production|WSON(DSG) |8|3000|LARGE T&R|Yes|NIPDAU|Level-1-260C-UNLIM|-40 to 85|837C|
|DRV8837CDSGRG4.B|Active|Production|WSON(DSG) |8|3000|LARGE T&R|Yes|NIPDAU|Level-1-260C-UNLIM|-40 to 85|837C|
|DRV8837CDSGT|Obsolete|Production|WSON(DSG) |8|-|-|Call TI|Call TI|-40 to 85|837C|



> **(1) Status:** For more details on status, see our product life cycle. 

> **(2) Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind. 

> **(3) RoHS values:** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition. 

> **(4) Lead finish/Ball material:** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width. 

> **(5) MSL rating/Peak reflow:** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board. 

> **(6) Part marking:** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. 

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. 

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. 

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. 

Addendum-Page 1 



<!-- page 17 -->

3-Sep-2026 

www.ti.com 

# **PACKAGE MATERIALS INFORMATION** 

## **TAPE AND REEL INFORMATION** 



<!-- Start of picture text -->
REEL DIMENSIONS TAPE DIMENSIONS<br>K0  P1<br>W<br>B0<br>Reel<br>Diameter<br>Cavity A0<br>A0 Dimension designed to accommodate the component width<br>B0 Dimension designed to accommodate the component length<br>K0 Dimension designed to accommodate the component thickness<br>W Overall width of the carrier tape<br>P1 Pitch between successive cavity centers<br>Reel Width (W1)<br>QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE<br>Sprocket Holes<br>Q1 Q2 Q1 Q2<br>Q3 Q4 Q3 Q4 User Direction of Feed<br>Pocket Quadrants<br><!-- End of picture text -->

*All dimensions are nominal 

|**Device**|**Package**<br>**Type**|**Package**<br>**Drawing**|**Pins**|**SPQ**|**Reel**<br>**Diameter**<br>**(mm)**|**Reel**<br>**Width**<br>**W1(mm)**|**A0**<br>**(mm)**|**B0**<br>**(mm)**|**K0**<br>**(mm)**|**P1**<br>**(mm)**|**W**<br>**(mm)**|**Pin1**<br>**Quadrant**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DRV8837CDSGR|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|DRV8837CDSGR|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|DRV8837CDSGRG4|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|



Pack Materials-Page 1 



<!-- page 18 -->

3-Sep-2026 

www.ti.com 

# **PACKAGE MATERIALS INFORMATION** 



<!-- Start of picture text -->
TAPE AND REEL BOX DIMENSIONS<br>Width (mm) H<br>W L<br><!-- End of picture text -->

*All dimensions are nominal 

|**Device**|**Package Type**|**Package Drawing**|**Pins**|**SPQ**|**Length (mm)**|**Width (mm)**|**Height (mm)**|
|---|---|---|---|---|---|---|---|
|DRV8837CDSGR|WSON|DSG|8|3000|182.0|182.0|20.0|
|DRV8837CDSGR|WSON|DSG|8|3000|210.0|185.0|35.0|
|DRV8837CDSGRG4|WSON|DSG|8|3000|210.0|185.0|35.0|



Pack Materials-Page 2 



<!-- page 19 -->

**GENERIC PACKAGE VIEW** 

**DSG 8** 

**WSON - 0.8 mm max height** 

**2 x 2, 0.5 mm pitch** 

PLASTIC SMALL OUTLINE - NO LEAD 

This image is a representation of the package family, actual package may vary. Refer to the product data sheet for package details. 









4224783/A 

www.ti.com 



<!-- page 20 -->

**PACKAGE OUTLINE** 

**DSG0008A** 



# **WSON - 0.8 mm max height** 

PLASTIC SMALL OUTLINE - NO LEAD 



<!-- Start of picture text -->
2.1 B<br>A<br>1.9<br>0.32<br>PIN 1 INDEX AREA 0.18<br>2.1<br>1.9<br>0.4<br>0.2<br>ALTERNATIVE TERMINAL SHAPE<br>TYPICAL<br>0.8<br>C<br>0.7<br>SEATING PLANE<br>0.05 0.08 C SIDE WALL<br>0.00 METAL THICKNESS<br>DIM A<br>OPTION 1 OPTION 2<br>0.1 0.2<br>EXPOSED<br>THERMAL PAD 0.9 0.1 (DIM A) TYP<br>4 5<br>6X 0.5<br>2X<br>9<br>1.5 1.6 0.1<br>8<br>1<br>PIN 1 ID 8X  0.32<br>(45 X 0.25) 8X  0.4 0.18<br>0.2 0.1 C A B<br>0.05 C<br>4218900/E   08/2022<br><!-- End of picture text -->

## NOTES: 

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M. 

2. This drawing is subject to change without notice. 

3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance. 

www.ti.com 



<!-- page 21 -->

**EXAMPLE BOARD LAYOUT** 

**DSG0008A** 

**WSON - 0.8 mm max height** 

PLASTIC SMALL OUTLINE - NO LEAD 



<!-- Start of picture text -->
(0.9) ( 0.2) VIA<br>8X (0.5) TYP<br>1<br>8<br>8X (0.25)<br>(0.55)<br>SYMM 9<br>(1.6)<br>6X (0.5)<br>5<br>4<br>(R0.05) TYP SYMM<br>(1.9)<br>LAND PATTERN EXAMPLE<br>SCALE:20X<br>0.07 MAX 0.07 MIN<br>ALL AROUND ALL AROUND<br>SOLDER MAS K M ETAL METAL UNDER S OLDER MASK<br>OPENING SOLDER MASK OPENING<br>NON SOLDER MASK<br>SOLDER MASK<br>DEFINED<br>DEFINED<br>(PREFERRED)<br>SOLDER MASK DETAILS<br>4218900/E   08/2022<br><!-- End of picture text -->

## NOTES: (continued) 

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271). 

5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown on this view. It is recommended that vias under paste be filled, plugged or tented. 

www.ti.com 



<!-- page 22 -->

**EXAMPLE STENCIL DESIGN** 

**DSG0008A** 

**WSON - 0.8 mm max height** 

PLASTIC SMALL OUTLINE - NO LEAD 



<!-- Start of picture text -->
8X (0.5) SYMM M ETAL<br>1<br>8<br>8X (0.25)<br>(0.45)<br>SYMM<br>9<br>(0.7)<br>6X (0.5)<br>5<br>4<br>(R0.05) TYP (0.9)<br>(1.9)<br>SOLDER PASTE EXAMPLE<br>BASED ON 0.125 mm THICK STENCIL<br>EXPOSED PAD 9:<br> 87% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE<br>SCALE:25X<br>4218900/E   08/2022<br><!-- End of picture text -->

NOTES: (continued) 

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations. 

www.ti.com 



<!-- page 23 -->

# **IMPORTANT NOTICE AND DISCLAIMER** 

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS” AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS. 

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements. 

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources. TI’s products are provided subject to TI’s Terms of Sale, TI’s General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices. 

TI objects to and rejects any additional or different terms you may propose. 

Copyright © 2026, Texas Instruments Incorporated 

Last updated 10/2025 

