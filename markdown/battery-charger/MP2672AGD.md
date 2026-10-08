# MP2672AGD

*Source: `original/battery-charger/MP2672AGD.pdf` (43 pages)*

<!-- page 1 -->

**_MP2672A_ Boost Charger with Cell Balance for 2-Cell Lithium-Ion Batteries in Series** 

# **DESCRIPTION** 

The MP2672A is a highly integrated, flexible switch-mode battery charger IC for Lithium-ion batteries with two cells in series. This makes it applicable for a wide range of portable applications. 

When an input power supply is present, the MP2672A operates in boost mode to charge the battery with two cells in series. When charging is enabled, the MP2672A automatically detects the battery voltage and charges the battery in three phases: pre-charge, constant current charge, and constant voltage charge. Other features include charge termination and auto-recharge. 

The device also has a narrow voltage DC (NVDC) power structure. With a deeply discharged battery, the MP2672A regulates the system output to a minimum voltage level. This powers the system instantly while simultaneously charging the battery via the battery FET. 

The MP2672A provides a cell balance function. It can monitor the voltage across each cell, then equalize the cell’s voltages if the difference between the two cells exceeds the mismatch threshold. 

The device has two configuration modes: standalone mode and host-control mode. In standalone mode, the charging parameters can be configured by hardware pins. In host-control mode, the charging parameters can be configured by the I<sup>2</sup> C registers. 

Diverse and robust protections include a thermal regulation loop to decrease the charge current in case the junction temperature exceeds the thermal loop threshold, and battery temperature protection that is compliant with JEITA standards. Other safety features include input over-voltage protection (OVP), battery OVP, thermal shutdown, battery temperature monitoring, a watchdog timer, and a configurable backup timer to prevent prolonged charging of a dead battery. 

The MP2672A is available in a QFN-18 (2mmx3mm) package. 

# **FEATURES** 

- 4.0V to 5.75V Operating Input Voltage 

- Up to 14V Sustainable Voltage 

- Up to 2A Configurable Charge Current for Battery with 2 Cells in Series 

- Compatible with Host-Control or Standalone Mode 

- NVDC Power Path Management 

- Configurable Input Voltage Limit 

- Configurable Charge Voltage with 0.5% Accuracy 

- No External Sense Resistor Required 

- Integrated Cell-Balancing Circuit for Mismatched Cells 

- Preconditioning for Fully Depleted Battery 

- Flexible New Charging Cycle Initiation 

- Charging Operation Indicator in Standalone Mode 

- Missing Battery Detection in Host-Control Mode 

- I<sup>2</sup> C Port for Flexible System Parameter Setting and Status Reporting in HostControl Mode 

- Negative Temperature Coefficient (NTC) Pin for Temperature Monitoring Compliant with JEITA Standards 

- Built-In Charging Protection and Configurable Safety Timer 

- MOSFET Cycle-by-Cycle Over-Current Protection (OCP) 

- Thermal Regulation and Thermal Shutdown 

- Available in a QFN-18 (2mmx3mm) Package 

# **APPLICATIONS** 

- Portable Handheld Solutions 

- Point-of-Sale (POS) Machines 

- Bluetooth Speakers 

- E-Cigarettes 

- General 2-Cell Applications 

All MPS parts are lead-free, halogen-free, and adhere to the RoHS directive. For MPS green status, please visit the MPS website under Quality Assurance. “MPS”, the MPS logo, and “Simple, Easy Solutions” are trademarks of Monolithic Power Systems, Inc. or its subsidiaries. 

**1** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 2 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL APPLICATIONS** 

## **Standalone Mode** 

Use a resistor to connect the CV pin to AGND. Set the battery-full voltage according to Table 1. 

**Table 1: Battery Voltage Settings** 



<!-- Start of picture text -->
RVBATT Range  VBATT_REG<br>30kΩ to 35kΩ  8.4V<br>70kΩ to 75kΩ  8.6V<br>100kΩ to 105kΩ  8.7V<br>130kΩ to 135kΩ  8.8V<br><!-- End of picture text -->



<!-- Start of picture text -->
SYS<br>BST<br>Q2 Q3<br>BATT<br>L1<br>VIN SW<br>Q1<br>CIN IN CBATT<br>RH<br>VLIM<br>MID<br>RL MP2672A<br>ACOK<br>VCC<br>STAT<br>VCC<br>AGND RT1<br>CV<br>NTC<br>ISET<br>RT2<br>RVBATT RISET PGND<br>RNTC<br>Figure 1: Typical Application in Standalone Mode<br><!-- End of picture text -->

**2** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 3 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL APPLICATIONS** **_(continued)_** 

## **Host-Control Mode** 

Connect the CV pin to VCC. Set the battery-full voltage according to the I<sup>2</sup> C register (see Figure 2). 



<!-- Start of picture text -->
SYS<br>BST<br>Q2 Q3<br>BATT<br>L1<br>VIN SW<br>Q1<br>CIN IN CBATT<br>RH<br>VLIM<br>MID<br>RL MP2672A<br>ACOK<br>VCC<br>STAT<br>VCC<br>AGND RT1<br>CV<br>SDA<br>NTC<br>MCU<br>SCL<br>RT2<br>ISET<br>PGND<br>RISET RNTC<br><!-- End of picture text -->

**Figure 2: Typical Application in Host Control Mode** 

**3** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 4 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **ORDERING INFORMATION** 

|**Part Number***|**Package**|**Top Marking**|**MSL Rating**|
|---|---|---|---|
|MP2672AGD-xxxx**|QFN-18(2mmx3mm)|_See Below_|1|
|EVKT-MP2672A|Evaluation kit|N/A|N/A|



*For Tape & Reel, add suffix –Z (e.g. MP2672AGD–xxxx–Z). 

**“-xxxx” is the register setting option. The factory default is “-0000”. This content can be viewed in the I<sup>2</sup> C Register Map section starting on page 28. For custom options, contact an MPS FAE to obtain an “-xxxx” value. 

# **TOP MARKING** 



BNJ: Product code Y: Year code WW: Week code LLLL: Lot number 

# **EVALUATION KIT EVKT-MP2672A** 

EVKT-MP2672A kit contents (items below can be ordered separately): 

|**#**|**Part Number**|**Item**|**Quantity**|
|---|---|---|---|
|1|EV2672A-D-00A|MP2672A evaluation board|1|
|2|EVKT-USBI2C-02 bag|Includes one USB to I<sup>2</sup>C communication interface, one<br>USB cable, and one ribbon cable|1|
|3|Online resources|Include datasheet, user guide, product brief, and GUI|1|



## **Order directly from MonolithicPower.com or our distributors.** 



<!-- Start of picture text -->
Input Power<br>Supply<br>Ribbon<br>GUI USB Cable USB to I 2 C  Cable<br>Communication  EV2672A-D-00A Battery<br>Interface<br>Load<br><!-- End of picture text -->

**Figure 3: EVKT-MP2672A Evaluation Kit Set-Up** 

> www.MonolithicPower.com 

**4** 

MP2672A Rev. 1.0 11/10/2020 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 5 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 



<!-- Start of picture text -->
PACKAGE REFERENCE<br>18 17 16 15 14<br>IN 1 13 PGND<br>SW 2 12 SW<br>BST 3 11 SYS<br>VCC 4 10 BATT<br>5 6 7 8 9<br>QFN-18 (2mmx3mm)<br>ACOK CV STAT SDA SCL<br>ISET AGND VLIM NTC MID<br><!-- End of picture text -->

**5** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 6 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **PIN FUNCTIONS** 

|**Pin #**|**Name**|**Type **<sup>(1)</sup>|**Description**|
|---|---|---|---|
|1|IN|P|**Input power pin.**|
|2, 12|SW|P|**Switching node.**The SW pin is the middle point between the MP2672A’s high-side<br>and low-side MOSFETs.|
|3|BST|P|**Bootstrap.**Connect a bootstrap capacitor between the BST and SW pins to provide<br>a floatingsupplyfor the high-side FET driver.|
|4|VCC|P|**Internal LDO output pin.**Bypass a 1µF ceramic capacitor from this pin to AGND.<br>It is not recommended topull more than 20mA from thispin.|
|5|ISET|AI|**Charge current setting.**Connect an external resistor from this pin to AGND to<br>configure the charge current. This also limits the maximum charge current in host-<br>control mode.|
|6|AGND|P|**Analog ground.**|
|7|VLIM|AI|**Input voltage limit feedback pin.**Connect a resistor divider from IN to AGND to<br>configure the minimum input voltage limit threshold.|
|8|NTC|AI|**Battery temperature-sense input.**Connect NTC to a negative temperature<br>coefficient thermistor. Configure the temperature window with a voltage divider<br>connected from VRNTC to NTC to AGND. Configurable JEITA thresholds are<br>supported. See the Negative Temperature Coefficient (NTC) Thermistor section on<br>page 23 for more details.|
|9|MID|P|**Middle point of the high-side and low-side cells.**The MID pin measures the<br>voltage of each cell and provides a balance path for each cell. Connect MID to<br>AGND to disable the cell balance function.|
|10|BATT|P|**Battery positive terminal.**Connect a capacitor from BATT to PGND, and place it<br>as close aspossible to the IC.|
|11|SYS|P|**System output.**Connect a capacitor from SYS to PGND, and place it as close as<br>possible to the IC.|
|13|PGND|P|**Powerground.**|
|14|SCL|DI|**I**<sup>**2**</sup>**C interface clockpin.**Thispin is onlyvalid if the CVpin is connected to VCC.|
|15|SDA|DIO|**I**<sup>**2**</sup>**C interface datapin.**Thispin is onlyvalid if the CVpin is connected to VCC.|
|16|STAT<br>--------------|DO|**Charging operation indicator.**This pin is an open-drain output.|
|17|CV|AI|**Operation mode and battery voltage control pin.**Pull CV to VCC to configure<br>the IC to host-control mode. Connect an external resistor to AGND to configure IC<br>to standalone mode. In standalone mode, configure the battery-full voltage via the<br>CVpin’s resistor.|
|18|ACOK<br>----------------|DO|**Valid input supply indicator.**This pin is an open-drain output. It is pulled low when<br>the input voltage exceeds the under-voltage lockout threshold (VIN_UVLO) and is<br>below the over-voltage lockout threshold(VIN_OVLO).|



**Note:** 

1) AI = analog input, DI = digital input, DO = digital output, DIO = digital input and output, P = power. 

**6** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 7 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **ABSOLUTE MAXIMUM RATINGS**<sup>(2)</sup> 

|BATT ............................................. -0.3V to +14V|
|---|
|SW ......................... -0.3V (-2V for 50ns) to +14V|
|SYS ............................................... -0.3V to +14V|
|MID, IN .......................................... -0.3V to +12V|
|BST to SW………….. ...................... -0.3V to +5V|
|All other pins to AGND .................... -0.3V to +5V|
|Continuous power dissipation ....... (TA= 25°C)<sup>(3)</sup><br>................................................................. 1.78W|
|Junction temperature ................................ 150°C|
|Lead temperature (solder) ........................ 260°C|
|Storage temperature…………...-65°C to +150°C|



## **_ESD Ratings_** 

Human body model (HBM)<sup>(5)</sup> .................. 2000V Charged device model (CDM)<sup>(6)</sup> ............... 250V 

**_Thermal Resistance_**<sup>(7)</sup> **_θJA θJC_** QFN-18 (2mmx3mm) .............. 70 ...... 15 ... °C/W 

#### **Notes:** 

- 2) Exceeding these ratings may damage the device. 

- 3)   The maximum allowable power dissipation is a function of the maximum junction temperature, TJ (MAX), the junction-toambient thermal resistance, θJA, and the ambient temperature, TA. The maximum allowable continuous power dissipation at any ambient temperature is calculated by PD (MAX) = (TJ (MAX) - TA) / θJA. Exceeding the maximum allowable power dissipation can cause excessive die temperature, and the regulator may go into thermal shutdown. Internal thermal shutdown circuitry protects the device from permanent damage. 

- 4)    The device is not guaranteed to function outside of its operating conditions. 

- 5) Per ANSI/ESDA/JEDEC JS-001. 

- 6) Per JESD22-C101. 

- 7) Measured on JESD51-7, 4-layer PCB. 

## **_Recommended Operating Conditions_**<sup>(4)</sup> 

|IN to PGND………………………….. 4V to 5.75V|
|---|
|BATT to PGND ..................................... Up to 9V|
|ICC.......................................................... Up to 2A|
|IDSCHG..................................................... Up to 3A|
|ISYS........................................................ Up to 2A|
|Operating junction temp (TJ) .... -40°C to +125°C|



**7** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 8 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **ELECTRICAL CHARACTERISTICS** 

### **VIN = 5V, TA = 25°C, unless otherwise noted.** 

|**Parameter**|**Symbol**|**Condition**|**Min**|**Typ**|**Max**|**Units**|
|---|---|---|---|---|---|---|
|**Input Power Characteristics**|||||||
|Input over-voltage lockout<br>(OVLO)threshold|VIN_OVLO|VINrising|5.75|6.0|6.25|V|
|Input OVLO threshold<br>hysteresis||||150||mV|
|Input under-voltage lockout<br>(UVLO)threshold|VIN_UVLO|VINfalling|3.25|3.45|3.65|V|
|Input UVLO threshold<br>hysteresis||||150||mV|
|**Boost Converter**|||||||
|VCC LDO output|VVCC|VIN = 5V,IVCC = 20mA|3.5|3.6|3.7|V|
|Low-side N-channel MOSFET<br>on resistance|RON_Q1|||54|70|mΩ|
|High-side N-channel MOSFET<br>on resistance|RON_Q2|||28|40|mΩ|
|Peak current limit for low-side<br>N-channel MOSFET|ILS_PK|VIN=5V|6|7||A|
|Valley current limit for high-<br>side N-channel MOSFET|IHS_VL|VIN=5V|5|6||A|
|Operating frequency|fSW|REG07H, bit[7] = 1|1100|1270|1440|kHz|
|System regulation minimum<br>voltage(VBATT_PRE+ VTRACK)||REG00H, bits[3:1] = 100,<br>VBATT = 5V|6.55|6.7|6.85|V|
|Battery track regulation<br>voltage|VTRACK|||300||mV|
|**Battery Charger**|||||||
|||REG00H,bits[3:1]= 000|5.9|6.05|6.2||
|Pre-charge threshold|VBATT_PRE|REG00H,bits[3:1]= 100|6.25|6.4|6.55|V|
|||REG00H,bits[3:1]= 111|6.6|6.75|6.9||
|Pre-charge threshold<br>hysteresis||VBATTfalling||250||mV|
|Pre-charge current|IPRE|VBATT= 5.9V|230|320|410|mA|



**8** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 9 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **ELECTRICAL CHARACTERISTICS** **_(continued)_** 

### **VIN = 5V, TA = 25°C, unless otherwise noted.** 

|**Parameter**|**Symbol**|**Condition**|**Min**|**Typ**|**Max**|**Units**|
|---|---|---|---|---|---|---|
|Ft h t|I|REG01H, bits[3:0] = 0101,<br>RISET= 6kΩ|0.9|1|1.1|A|
|as carge curren|CC|REG01H, bits[3:0] = 1111,<br>RISET= 6kΩ|1.8|2|2.2|A|
|Termination charge current|ITERM|If ICC> 1.5A,<br>as apercentage of ICC|8|11|14|%|
|||If ICC≤ 1.5A(setting)|130|160|190|mA|
|Input minimum voltage<br>regulation reference|VIN_MIN_REF||1.18|1.2|1.22|V|
|||VBATT_REG= 8.3V, host-control<br>mode,REG00H,bits[7:5]= 000|||||
|Battery charge voltage|V|VBATT_REG= 8.4V,<br>host-control mode: REG00H,<br>bits[7:5] = 001,<br>standalone mode:<br>RVBATT= 30kΩ|-050||+050|%|
|regulation|BATT_REG_ACC|VBATT_REG= 8.8V,<br>host-control mode: REG00H,<br>bits[7:5] = 101,<br>standalone mode:<br>RVBATT= 135kΩ|.||.||
|||VBATT_REG= 8.2V, host-control<br>mode,REG00H,bits[7:5]= 111|||||
|Recharge threshold below<br>VBATT_REG|VRECH|||450||mV|
|Battery pack over-voltage<br>protection(OVP)threshold|VBATT_OVP|As a percentage of VBATT_REG|102|104|105|%|
|Battery pack OVP<br>hysteresis||REG00H, bit[0] = 0||150||mV|
|SYS-to-BATT N-channel<br>MOSFET on resistance|RON_Q3||22|31|40|mΩ|
|Battery quiescent current|IBATT_Q|VIN< VIN_UVLO, VBATT= 8.4V,<br>system no load|19|31|42|μA|
|ACOK<br>----------------<br>, STAT<br>--------------<br>, pin output<br>low voltage||Sinking 1.5mA|||400|mV|
|ACOK<br>----------------<br>, STAT<br>---------------<br>, pin leakage<br>current||Connected to 5V|||1|μA|



**9** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 10 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **ELECTRICAL CHARACTERISTICS** **_(continued)_** 

## **VIN = 5V, TA = 25°C, unless otherwise noted.** 

|**Parameter**|**Symbol**|**Condition**|**Min**|**Typ**|**Max**|**Units**|
|---|---|---|---|---|---|---|
|Termination deglitch time|tTERM_DGL|||180||ms|
|Recharge deglitch time|tRECH_DGL|||180||ms|
|**Battery Temperature Monitori**|**ng (JEITA)**||||||
|NTC low temprisingthreshold|VCOLD|As apercentage of VCC|70|71|72|%|
|NTC low temp rising threshold<br>hysteresis||As a percentage of VCC||2.4||%|
|NTC cool temprisingthreshold|VCOOL|As apercentage of VCC|62|63|64|%|
|NTC cool temp rising threshold<br>hysteresis||As a percentage of VCC||2.2||%|
|NTC warm temp falling<br>threshold|VWARM|As a percentage of VCC|39.4|40.4|41.4|%|
|NTC warm temp falling<br>threshold hysteresis||As a percentage of VCC||2.5||%|
|NTC hot tempfallingthreshold|VHOT|As apercentage of VCC|33.5|34.5|35.5|%|
|NTC hot temp falling threshold<br>hi||As a percentage of VCC||2.5||%|
|ysteress|||||||
|**Thermal Regulation and Prote**|**ction**||||||
|Thrml htdwn|||||||
|ea suo<br>temperature|TJ_SHDN|Rising threshold||150||°C|
|Thermal shutdown hysteresis||Temperature falling||20||°C|
|**Cell Balance Function**|||||||
|Internal balance FET on<br>|RON_BHS|||2.1||Ω|
|resistance|RON_BLS|||1.3||Ω|
|Cell balance starting voltage<br>threshold|VCELL_BAL|I<sup>2</sup>C-configurable,<br>REG01H,bit[6]= 0|3.35|3.5|3.65|V|
|Cell voltage high-to-low cell<br>mismatch threshold|VCELL_DIFF_HTL|REG01H, bit[5] = 0||50|70|mV|
|Cell voltage high-to-low cell<br>mismatch threshold hysteresis||||52||mV|
|Cell voltage low-to-high cell<br>mismatch threshold|VCELL_DIFF_LTH|REG01H, bit[4] = 0||50|70|mV|
|Cell voltage low-to-high cell<br>mismatch threshold hysteresis||||58||mV|
|High-side cell OVP threshold|VHCELL_OVP|As a percentage of the<br>battery-full voltage|101|102.5|104|%|
|Low-side OVP threshold|VLCELL_OVP|As a percentage of the<br>battery-full voltage|101|102.5|104|%|



**10** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 11 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **ELECTRICAL CHARACTERISTICS** **_(continued)_** 

## **VIN = 5V, TA = 25°C, unless otherwise noted.** 

|**Parameter**|**Symbol**|**Condition**|**Min**|**Typ**|**Max**|**Units**|
|---|---|---|---|---|---|---|
|**I**<sup>**2**</sup>**C Communication Interfac**|**e**||||||
|Input high threshold level|VIH|VPULL UP= 1.8V|1.3|||V|
|Input low threshold level|VIL|VPULL_UP= 1.8V|||0.4|V|
|Output low threshold level|VOL|ISINK= 5mA|||0.4|V|
|I<sup>2</sup>C clock frequency|fSCL||||400|kHz|
|**Timing Characteristics**|||||||
|Clock frequency|fCLK|||131||kHz|
|Watchdogtimer<sup>(8)</sup>|tWTD|REG02H,bits[5:4]= 01||40||sec|
|Safety charge timer|tTMR|I<sup>2</sup>C-configurable,<br>REG02H,bits[2:1]= 11|16|20||hours|
|Pre-charge timer||||1||hours|



### **Note:** 

8) Guaranteed by design 

**11** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 12 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL CHARACTERISTICS** 

**IPRE vs. Junction Temperature** 



<!-- Start of picture text -->
VBATT = 5V<br>600<br>450<br>300<br>150<br>0<br>-50 0 50 100 150<br>TEMPERATURE (°C)<br>ITERM vs. Junction Temperature<br>250<br>200<br>150<br>100<br>50 ICC=1A<br>ICC=2A<br>0<br>-50 0 50 100 150<br>TEMPERATURE (°C)<br>VBATT_PRE vs. Junction Temperature<br>6.5<br>6.4<br>6.3<br>6.2<br>-50 0 50 100 150<br>TEMPERATURE (°C)<br>I(mA)PRE<br>(V)VBATT_PRE<br>I (mA)TERM<br><!-- End of picture text -->



<!-- Start of picture text -->
ICC vs. Junction Temperature<br>2.50<br>2.00<br>1.50 ICC=1A<br>ICC=2A<br>1.00<br>0.50<br>-50 -25 0 25 50 75 100 125 150<br>TEMPERATURE (°C)<br>VBATT_REG vs. Junction Temperature<br>VBATT_REG = 8.4V<br>8.5<br>8.4<br>8.3<br>8.2<br>8.1<br>-50 0 50 100 150<br>TEMPERATURE (°C)<br>Battery Cell OVP vs. Junction<br>Temperature<br>105<br>104<br>103<br>102<br>LS_Cell_OVP<br>101<br>HS_Cell_OVP<br>100<br>-50 0 50 100 150<br>TEMPERATURE (°C)<br>THRESHOLD(%)<br>BATTERY CELL OVP<br>I (A)CC<br>V(V)BATT_REG<br><!-- End of picture text -->

**12** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 13 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL PERFORMANCE CHARACTERISTICS** 

**VIN = 5V, TA = 25°C, unless otherwise noted.** 

## **Constant Current Mode Charge Efficiency** 



<!-- Start of picture text -->
VIN = 5V, fSW = 1200kHz , L = 1.5μH,<br>(DCR = 10mΩ), ISYS = 0A<br>1<br>0.95<br>0.9<br>0.85<br>ICC=2A<br>ICC=1A<br>0.8<br>6.4 6.9 7.4 7.9 8.4<br>VBATT (V)<br>Configurable Charge Current<br>Standalone mode<br>2.5<br>2<br>1.5<br>1<br>0.5<br>0<br>5 10 15 20 25<br>RISET (kΩ)<br>I (A)CC<br>EFFICIENCY<br><!-- End of picture text -->

## **Constant Voltage Mode Charge Efficiency** 



<!-- Start of picture text -->
VIN = 5V, fSW = 1200kHz, L = 1.5μH,<br>(DCR = 10mΩ), VBATT = 8.4V, ISYS = 0A<br>1<br>0.95<br>0.9<br>0.85<br>0.8<br>0 0.5 1 1.5 2<br>IBATT (A)<br>EFFICIENCY<br><!-- End of picture text -->

**13** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 14 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL PERFORMANCE CHARACTERISTICS** **_(continued)_** 

**VIN = 5V, VBATT_PRE = 6.5V, ICC = 2A, ISYS = 0A, VBATT = 0V to 8.4V, CIN = 10μF, CSYS = 44μF, CBATT = 22μF, L = 1.5μH, fSW = 1200kHz, TA = 25°C, unless otherwise noted.** 



<!-- Start of picture text -->
CH2: VSYS<br>2V/div.<br>CH1: VBATT<br>2V/div.<br>CH4: IBATT<br>500mA/div.<br>CH3: STAT ------------------<br>2V/div.<br><!-- End of picture text -->

**Battery Charge Curve** 



<!-- Start of picture text -->
VBATT_REG = 8.4V<br><!-- End of picture text -->



4s/div. 

## **Auto-Recharge** 



<!-- Start of picture text -->
VBATT_REG = 8.4V<br><!-- End of picture text -->



<!-- Start of picture text -->
CH2: VSYS<br>2V/div.<br>CH1: VBATT<br>2V/div.<br>CH4: IBATT<br>500mA/div.<br>CH3: STAT ------------------<br>2V/div.<br>2s/div.<br><!-- End of picture text -->



<!-- Start of picture text -->
CH1: VBATT<br>2V/div.<br>CH3: IBATT<br>500mA/div.<br>CH4: IL<br>1A/div.<br>CH2: VSW<br>5V/div.<br><!-- End of picture text -->

## **Pre-Charge Steady State** 

VBATT = 5V 



1μs/div. 

## **Constant Current Charge Steady State** 

VBATT = 7.4V 



<!-- Start of picture text -->
CH1: VBATT<br>2V/div.<br>CH3: IBATT<br>500mA/div.<br>CH4: IL<br>1A/div.<br>CH2: VSW<br>5V/div.<br>1μs/div.<br><!-- End of picture text -->

## **Constant Voltage Charge Steady State** 

VBATT = 8.4V (1A) 



<!-- Start of picture text -->
CH1: VBATT<br>2V/div.<br>CH3: IBATT<br>500mA/div.<br>CH4: IL<br>1A/div.<br>CH2: VSW<br>5V/div.<br>1μs/div.<br><!-- End of picture text -->

## **Constant Voltage Charge Steady State** 

VBATT = 8.4V (0.5A) 



<!-- Start of picture text -->
CH1: VBATT<br>2V/div.<br>CH3: IBATT<br>500mA/div.<br>CH4: IL<br>1A/div.<br>CH2: VSW<br>5V/div.<br>1μs/div.<br><!-- End of picture text -->

**14** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 15 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL PERFORMANCE CHARACTERISTICS** **_(continued)_** 

**VIN = 5V, VBATT_PRE = 6.5V, ICC = 2A, ISYS = 0A, VBATT = 0V to 8.4V, CIN = 10μF, CSYS = 44μF, CBATT = 22μF, L = 1.5μH, fSW = 1200kHz, TA = 25°C, unless otherwise noted.** 



<!-- Start of picture text -->
Start-Up through VIN<br>VBATT = 7.4V<br>CH1: VIN<br>2V/div.<br>CH2: VBATT<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>CH3: VSW<br>5V/div.<br>40ms/div.<br><!-- End of picture text -->

## **Shutdown through VIN** 



<!-- Start of picture text -->
VBATT = 7.4V<br><!-- End of picture text -->



<!-- Start of picture text -->
CH1: VIN<br>2V/div.<br>CH2: VBATT<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>CH3: VSW<br>5V/div.<br>40ms/div.<br><!-- End of picture text -->

## **Boost Enabled** 



<!-- Start of picture text -->
VBATT = 7.4V<br>CH1: VIN<br>2V/div.<br>CH2: VBATT<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>CH3: VSW<br>5V/div.<br>40ms/div.<br><!-- End of picture text -->

## **Boost Disabled** 



<!-- Start of picture text -->
VBATT = 7.4V<br>CH1: VIN<br>2V/div.<br>CH2: VBATT<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>CH3: VSW<br>5V/div.<br>40ms/div.<br><!-- End of picture text -->

## **Constant Current Charge Enabled** VBATT = 7.4V, MP2672A-0000 

## **Constant Current Charge Disabled** VBATT = 7.4V, MP2672A-0000 



<!-- Start of picture text -->
CH1: VBATT CH1: VBATT<br>2V/div.  2V/div.<br>CH2: VSYS CH2: VSYS<br>2V/div.  2V/div.<br>CH4: IBATT CH4: IBATT<br>1A/div.  1A/div.<br>CH3: VSW CH3: VSW<br>5V/div. 5V/div.<br>20ms/div. 20ms/div.<br><!-- End of picture text -->

**15** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 16 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL PERFORMANCE CHARACTERISTICS** **_(continued)_** 

**VIN = 5V, VBATT = 0V to 8.4V, CIN = 10μF, CSYS = 44μF, CBATT = 22μF, L = 1.5μH, fSW = 1200kHz, TA = 25°C, unless otherwise noted.** 

**Constant Current Charge Enabled** VBATT = 7.4V, MP2672A-000E 



<!-- Start of picture text -->
CH1: VBATT<br>2V/div.<br>CH2: VSYS<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>CH3: VSW<br>5V/div.<br>400μs/div.<br><!-- End of picture text -->

## **Constant Current Charge Disabled** 

VBATT = 7.4V, MP2672A-000E 



<!-- Start of picture text -->
CH1: VBATT<br>2V/div.<br>CH2: VSYS<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>CH3: VSW<br>5V/div.<br>20μs/div.<br><!-- End of picture text -->

## **Standard NTC Protection** 

VBATT = 7.4V, standard NTC, ICC = 2A, vary V_NTC 



<!-- Start of picture text -->
CH2: VBATT<br>2V/div.<br>CH1: VNTC<br>1V/div.<br>CH3: STAT ------------------<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>4s/div.<br><!-- End of picture text -->



<!-- Start of picture text -->
JEITA NTC Protection<br>VBATT = 8.15V, JEITA NTC, ICC = 2A,<br>vary V_NTC<br><!-- End of picture text -->



<!-- Start of picture text -->
CH2: VBATT<br>2V/div.<br>CH1: VNTC<br>1V/div.<br>CH3:<br>------------------ STAT<br>2V/div.<br>CH4: IBATT<br>1A/div.<br>4s/div.<br><!-- End of picture text -->

## **LS Cell Balance** 

## **HS Cell Balance** 



<!-- Start of picture text -->
ICC = 1A, ISYS = 0A, HS cell is 3.6V and LS cell  ICC = 1A, ISYS = 0A, HS cell is 3.8V and LS cell<br>is 3.8V, balance enabled, balance resistor is  is 3.6V, balance enabled, balance resistor is<br>17mΩ 17mΩ<br>CH1: VMID<br>2V/div.<br>CH1: VMID<br>CH3: IBATTH<br>2V/div.<br>500mA/div.<br>CH3: IBATTH<br>500mA/div.<br>CH4: IBATTL CH4: IBATTL<br>500mA/div.  500mA/div.<br>200ms/div. 200ms/div.<br><!-- End of picture text -->

**16** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 17 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **FUNCTIONAL BLOCK DIAGRAM** 



<!-- Start of picture text -->
CSYS<br>SYS<br>SW Q2 Q3 BATT<br>CIN Q1<br>A1<br>BST Charge<br>iHS<br>Pump Balance  MID<br>and<br>VIN Pre- Protection<br>A2 Charge<br>Loop<br>ILS<br>IBATT_FB<br>TJ_FB<br>EA1<br>VIN VCC<br>VLIM TJ_REF Junction Temp Loop LDO<br>VBATT_FB EA2<br>VBATT_REG VCOMP PWM Controller<br>Battery Voltage Loop<br>Charge  IBATT_FB<br>CV Parameter  EA3<br>Setting<br>ISET ICC_REF Charge Current Loop NTC<br>VSYS_FB<br>Protection<br>EA4 NTC<br>VSYS_REF System Voltage Loop<br>VIN_FB<br>EA5<br>1.2V<br>Input Voltage Loop AGND<br>DAC STAT<br>Thermal<br>Shutdown Control Logic ACOK<br>SCL I2C  Block and<br>Timer<br>Register<br>SDA<br>CV<br>PGND<br><!-- End of picture text -->

**Figure 4: Functional Block Diagram** 

**17** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 18 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **OPERATION** 

The MP2672A is a highly integrated switchmode battery charger IC that charges lithium-ion batteries with two cells in series from a 5V input power supply. This means it can be used with an adapter or USB input. 

## **Host-Control Mode and Standalone Mode** 

The MP2672A can operate in either host-control mode or standalone mode. After the input starts up, the MP2672A checks the CV pin’s status. 

If CV is pulled up to logic high, the MP2672A works in host-control mode. If CV is connected to ground through a resistor, the MP2672A works in standalone mode. 

In host-control mode, the charging parameters (VBATT_REG and ICC) can be configured by the I<sup>2</sup> C registers. In standalone mode, they can be set by hardware pins. 

**Table 2: Host-Control Mode vs. Standalone Mode** 

|**CV Pin**|**Mode**|**VBATT_REG**|**ICC**|
|---|---|---|---|
|Connected<br>to AGND<br>via resistor|Standalone|Set by<br>CV<br>resistor|Set by<br>ISET<br>resistor|
|Pulled up<br>to VCC|Host-<br>control|Set by<br>I<sup>2</sup>C<br>register|Set by<br>I<sup>2</sup>C<br>register<sup>(9)</sup>|



**Note:** 

- 9) The maximum charge current is limited by the ISET pin, even in host-control mode. 

## **Internal Power Supply** 

The VCC LDO is powered by the input power supply, and it powers the internal circuit and MOSFET driver. When the input is absent, the VCC LDO is off. An external capacitor must be connected from the VCC pin to AGND. The VCC output is regulated to about 3.6V when VIN is 5V. If VIN is below 3.6V, the LDO enters low-dropout mode, and the LDO FET fully turns on. The VCC output cannot handle current loads exceeding 20mA. 

## **Input Voltage vs. System Voltage Limitation** 

To prevent the MP2672A from entering open-loop operation due to the low-side MOSFET’s minimum on time, the boost converter turns off if VSYS drops below 110% of VIN. The converter restarts, then checks the input voltage and system voltage again. 

The boost converter turns off again if VSYS is still below 110% of VIN after a 1ms soft-start time. 

It is recommended to choose VBATT_PRE and VTRACK to ensure that the minimum output voltage of the boost converter exceeds 110% of the maximum DC input voltage. 

## **Input Power Start-Up** 

When the input voltage is below the undervoltage lockout threshold (VIN_UVLO), SYS is powered by the battery via Q3, which is fully turned on at this time. When input power is connected and VIN exceeds VIN_UVLO, Q3 stops being fully on and enters virtual diode mode. At the same time, the boost converter starts up with a soft start of the system voltage loop. When the system voltage rises to about 20mV above the battery voltage, Q3 turns off. It turns on again with a soft-start charging current after the system’s voltage soft start completes. 

## **Narrow Voltage DC (NVDC) Power Structure** 

The MP2672A features a narrow voltage DC (NVDC) power structure that is comprised of a frond-end boost converter and a rear-end battery FET between the SYS and BATT pins. This allows for separate control between the system and the battery. The system is given the priority to start up, even with a deeply discharged or missing battery. When input power is available and a depleted battery is connected, the system voltage is regulated to the minimum system voltage (VSYS_MIN) which is set via REG00H, bits[3:1]. 

Figure 5 shows the system voltage control, described in detail below: 

- When the battery voltage (VBATT) is below VBATT_PRE, the system voltage is regulated to VSYS_REG_MIN = VBATT_PRE + VTRACK. The battery FET works linearly to charge the battery with the pre-charge current. 

- When VBATT is above VBATT_PRE, the battery FET is fully turned on, and the system voltage always exceeds VBATT by the value calculated with IBATT x RON_Q3. Once battery charging completes, the system output (VSYS) is regulated to VBATT + VTRACK. 

**18** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 19 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

- When charging is disabled and REG00H, bit[4] = 0, VSYS is also regulated to VTRACK, which is greater than the real battery voltage. 



<!-- Start of picture text -->
vSYS<br>VTRACK<br>VBATT_PRE<br>vBATT<br><!-- End of picture text -->

**Figure 5: VSYS Variation with VBATT** 

# **Battery Charge Profile** 

The MP2672A provides three main charging phases: constant current pre-charge, constant current fast charge, and constant voltage charge (see Figure 6). 

<u>Phase 1 (Constant Current Pre-Charge): When</u> VBATT is below the pre-charge to fast charge threshold (VBATT_PRE), the MP2672A regulates the system voltage to VSYS_REG_MIN. The part applies a safe pre-charge current (IPRE) to charge the deeply depleted battery until VBATT reaches 

VBATT_PRE. If VBATT_PRE is not reached before the pre-charge timer (60min) expires, the charge cycle ceases, and a corresponding timeout fault signal is asserted. 

<u>Phase 2 (Constant Current Fast Charge): When</u> VBATT exceeds VBATT_PRE, the MP2672A stops the pre-charge phase and enters the fast charge phase. The fast charge current can be configured via the ISET pin in standalone mode or via the I<sup>2</sup> C register in host-control mode. 



<!-- Start of picture text -->
VTRACK<br>System Voltage<br>VBATT_REG<br>VTRACK Battery Voltage<br>VSYS_REG_MIN<br>ICC<br>Charge<br>Current<br>IPRE<br>ITERM<br>Pre-Charge Fast  Constant Voltage  Charge<br>Charge Charge Termination<br><!-- End of picture text -->

**Figure 6: Battery Charge Profile** 

> MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. 

**19** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 

© 2020 MPS. All Rights Reserved. 



<!-- page 20 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

<u>Phase 3 (Constant Voltage Charge): When VBATT</u> reaches the battery regulation voltage (VBATT_REG), the charge current begins to decrease (see Figure 7). The charge cycle is complete once the constant voltage loop is dominant, and the charge current drops below the charge termination current threshold for a 200ms deglitch time. This 200ms deglitch time is designed to start each charge cycle; after 200ms expires, the charge-full signal asserts whether the termination conditions have been met. 



<!-- Start of picture text -->
VSYS<br>VBATT_REG<br>VBATT<br>ITERM<br>Charge Current<br>200ms<br>Soft Start Forced Charging Time<br>a) Forced Charge Time<br>VSYS<br>VBATT_REG<br>Charge Current VBATT<br>ITERM<br>200ms Charging<br>Constant Voltage Termination Deglitch Time Done<br>b) Termination Deglitch Time<br>Figure 7: Forced Charge Time and Termination<br>Deglitch Time<br><!-- End of picture text -->

If ITERM is not reached before the safety charge timer expires (see the Safety Timer section on page 22), the charging cycle stops and the corresponding timeout fault signal is asserted. 

Charging termination can be manually disabled by pulling the NTC pin up to VCC. A new charging cycle starts when the following conditions are valid: 

- The input power is re-plugged in 

- Auto-recharge is enabled 

- The charging enable bit is toggled (only for host-control mode) 

# **Auto-Recharge** 

When the battery is fully charged and charging is terminated, the battery may be discharged by system consumption or self-discharge (see Figure 8). The MP2672A automatically starts a new charging cycle (without requiring a manual charging cycle restart) when the battery voltage drops below the recharge threshold for 200ms. 



<!-- Start of picture text -->
VBATT<br>VRECH<br>Charge<br>Current<br>200ms<br>Charging<br>Charging  Recharge Deglitch<br>Starts<br>Done Time<br><!-- End of picture text -->

**Figure 8: Recharging Profile** 

# **Charging Enabled (Default Setting)** 

If the battery is not expected to be charged frequently during high state of charge (SOC) conditions, the MP2672A has an one-time programmable (OTP) option (REG05H, bit[7]) to disable charging when the input power is on, and the battery voltage exceeds the recharge voltage threshold. Charging is enabled until the battery voltage falls below the recharge threshold. 

# **Battery-Full Voltage Setting** 

The MP2672A has a CV pin that can configure the battery regulation voltage. 

When CV is pulled up to VCC, the MP2672A operates in host-control mode. The battery regulation voltage is configured through the I<sup>2</sup> C. 

When CV is connected to AGND via a resistor, the MP2672A operates in standalone mode. The battery regulation voltage is set according to Table 3. 

**Table 3: VBATT_REG vs. RVBATT Resistor** 

|**Resistor Range **|**VBATT_REG**|
|---|---|
|30kΩto 35kΩ|8.4V|
|70kΩto75kΩ|8.6V|
|100kΩto105kΩ|8.7V|
|130kΩto135kΩ|8.8V|



Figure 9 shows the simplified diagram. 

- There is no thermistor fault on the NTC pin 

- There is no safety timer fault 

- There is no battery over-voltage condition 

- Thermal shutdown is not occurring 

**20** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 21 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 



<!-- Start of picture text -->
CV<br>VTH1<br>Battery Voltage<br>VTH2 Reference<br>Decoding DAC<br>VTH3<br>VTH4<br><!-- End of picture text -->

**Figure 9: Simplified Diagram of the VBATT_REG Setting in Standalone Mode** 

# **Charge Current Setting** 

In standalone mode, the charge current (ICC) is set by a resistor connected to the ISET pin (RISET). Calculate ICC with Equation (1): 



In host-control mode, the charge current can be configured via RISET and REG01H, bits[3:0]. RISET determines the full-scale value of the register. For example, if RISET is 6kΩ, the I<sup>2</sup> C-configurable range is between 500mA and 2000mA, with 100mA per step. If RISET is 24kΩ, the I<sup>2</sup> C- configurable range is between 125mA and 500mA, with 25mA per step. RISET is recommended to be between 6kΩ and 24kΩ. 

# **Minimum Input Voltage Limit** 

To avoid overloading the adapter, the MP2672A implements input voltage based power management by continuously monitoring the input voltage (VIN). When the minimum input voltage limit (VIN_MIN) is reached, the charge current is reduced to prevent VIN from dropping further. VIN_MIN can be configured by a voltage divider on the VLIM pin. 

The internal reference of the input voltage loop is 1.2V, and VIN_MIN can be estimated with Equation (2): 



# **Battery Supplement Mode and Virtual Diode Mode** 

When  VIN_MIN is reached, the charge current is reduced to keep VIN from dropping further. However, if the charge current drops to 0A and the input source is still overloaded due to a heavy system load, the system voltage (VSYS) continues dropping. If VSYS falls below VBATT, the MP2672A enters battery supplement mode. The battery starts to supplement the system load along with the boost converter. In supplement mode, the battery FET operates as a virtual diode. 

When VSYS falls 30mV below VBATT, the battery FET turns on, and its source-to-drain voltage is regulated at 24mV. As the battery discharge current rises, the virtual diode loop is saturated and the battery FET fully turns on. The sourceto-drain voltage is the discharge current times the on resistance of the battery FET. 

# **Missing Battery Detection** 

The MP2672A is capable of detecting whether a battery is connected. The device detects a missing battery under the following conditions: 

- Charging is enabled 

- Auto-recharge is triggered 

- Recovery from any fault 

If a battery cannot be found, a 1Hz blinking on the STAT-------------pin indicates the missing battery condition, or the BATTFLOAT_STAT bit is set 1 in host-control mode. Figure 10 shows the battery missing detection flowchart. 

**21** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 22 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 



<!-- Start of picture text -->
Enable Charge<br>Counter A = 0<br>Start charging<br>Timer initiates Has the timer expired?<br>No Yes<br>No<br>Charging terminated?<br>If A < 2, A = A+1<br>A = 0<br>If A = 2, A = A+0<br>Yes<br>Yes<br>A = 2?<br>Battery FET turns off<br>No<br>Yes<br>No<br>VBATT < VRECH? Battery missing Battery is present<br><!-- End of picture text -->

**<mark>Figure 10: Missing Battery Detection Flowchart</mark>** 

# **Battery Over-Voltage Protection** 

The MP2672A is designed with a built-in battery over-voltage protection (OVP) threshold, which is 104% of VBATT_REG. If a battery OV event occurs, the MP2672A turns off the battery FET (Q3) and stops charging. At this time, the boost converter continues operating, and the system voltage tracks the battery voltage with additional VTRACK. 

When the balance function is enabled (the MID pin is not pulled down to AGND), the MP2672A uses the MID pin to monitor each cell’s voltage. Generally, if any one of the cell’s voltages exceeds 102.5% of VBATT_REG / 2, the MP2672A stops charging the battery. 

# **Safety Timer** 

The MP2672A provides both a pre-charge and fast charge cycle safety timer to avoid an extended charging cycle due to abnormal battery conditions. When the battery is below VBATT_PRE, the safety timer for pre-charge is 60 minutes. The fast charge cycle safety timer starts when the battery enters fast charge mode. The fast charge safety timer can be configured or disabled via the I<sup>2</sup> C. 

writing 0 and 1 sequentially to the REG00H, bit[4]. The following actions restart the safety timer: 

- Beginning a new charge cycle 

- Writing REG00H, bit[4] from 0 to 1 (charge enabled) 

- Writing REG02H, bits[2:1] from 00 to 01/10/11 (safety timer enabled) 

- Writing REG02H bit[3] from 0 to 1 (software reset) 

In the event of an NTC hot or cold fault, the charging timer is suspended. Once the NTC fault is removed, the timer continues to count from the value it was at before the NTC fault. 

# **Watchdog Timer** 

When the MP2672A operates in host-control mode, a watchdog timer is provided to reset all the registers to their default values if the watchdog timer is not reset periodically. By doing this, the MP2672A’s register values return to their default settings when no action occurs on the I<sup>2</sup> C bus for a certain time. The watchdog timer duration can be configured and disabled via the I<sup>2</sup> C. 

The safety timer is reset at the beginning of a new charging cycle. It can also be reset by 

**22** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 23 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **Negative Temperature Coefficient (NTC) Thermistor** 

The term thermistor refers to any thermally sensitive resistor, and a negative temperature coefficient (NTC) thermistor is generally called a thermistor. Thermistors can be used for multiple purposes, as their characteristics are different based on their manufacturing method, structure, and shape. Unless otherwise noted, the thermistor resistance values are classified at a standard temperature of 25°C. The resistance of a thermistor is solely a function of its absolute temperature. 

Refer to the thermistor’s datasheet for the mathematic equation that calculates the relationship between resistance and the absolute temperature of the thermistor. It can also be calculated with Equation (3): 



Where R1 is the resistance at the absolute temperature T1, R2 is the resistance at the absolute temperature T2, and β is a constant that depends on the thermistor’s material. 

The MP2672A continuously monitors the battery’s temperature by measuring the voltage on the NTC pins. This voltage is determined by the voltage divider. The voltage divider ratio is determined by the NTC thermistor’s resistance values under different ambient battery temperatures. 

The MP2672A internally sets a predetermined upper and lower bounds of the temperature range. If the voltage at the NTC pin goes out of the hot or cold threshold, the temperature is outside its safe operating limit. At this time, charging ceases until the operating temperature returns to within its safe range. 

To satisfy JEITA requirements, the MP2672A monitors four temperature thresholds: the cold battery threshold (TNTC < 0°C), the cool battery threshold (0°C < TNTC < 10°C), the warm battery threshold (45°C < TNTC < 60°C), and the hot battery threshold (TNTC > 60°C). 

For a given NTC thermistor, these temperatures correspond to the VCOLD, VCOOL, VWARM, and VHOT values. Figure 11 shows the typical JEITA operation when the battery temperature is in a 

different temperature window, described in detail below: 

1. When VNTC < VHOT or VNTC > VCOLD, charging is suspended, and all timers are suspended. 

2. When VHOT < VNTC < VWARM, the battery regulation voltage (VBATT_REG) is reduced by 120mV/cell from the configurable threshold. 

3. When VCOOL < VNTC < VCOLD, the charging current is reduced to half of the configurable charge current. 



<!-- Start of picture text -->
ICC<br>Charge  0.5 x ICC<br>Current<br>VBATT_REG VBATT_REG –<br>Charge  120mV/cell x 2<br>Voltage<br>Cold Cool Warm Hot<br><!-- End of picture text -->

**Figure 11: JEITA Compatible NTC Window** 

For a given thermistor, two of four temperature thresholds can be configured by changing the values of RT1 and RT2. See the Selecting an NTC Sensor Resistor section on page 34 for more details. 

# **Thermal Regulation and Thermal Shutdown** 

To guarantee safe operation, the MP2672A limits the die temperature. If the internal junction temperature reaches the preset threshold, the MP2672A starts to reduce the charge current to prevent greater power dissipation. 

When VBATT > VBATT_PRE, the die temperature limit is always set to 120°C. When VBATT < VBATT_PRE, the die temperature limit can be configured to multiple values (60°C, 80°C, 100°C, or 120°C), which can be configured by the one-time programmable (OTP) register (REG05H, bits[4:3]). 

If the junction temperature reaches 150°C, the boost converter enters shutdown mode. 

**23** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 24 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **Indications** 

The MP2672A has two open-drain pins (ACOK -------------and STAT ) to indicate the input power and charging status. Table 4 shows the behavior for each of these indications. 

**Table 4: Input Power and Charging Statuses** 

|**Charging State**|**ACOK**<br>-----------------|**STAT**<br>----------------|
|---|---|---|
|Charging|Low|Low|
|Charging complete,<br>charging disabled|Low|Open drain|
|Charging<br>suspended<br>due to one of the|||
|following:|||
|Battery OVP<br>Timer fault|Low|1Hz<br>blinking|
|NTC hot fault|||
|NTC cold fault<br>Batteryfloating|||
|Thermalshutdown|Low|Opendrain|



# **Battery Cell Balance and Protection** 

The MP2672A provides battery cell balance and protection for dual-cell applications (see Figure 12). The part can sense the voltage across each cell. Generally, if these two cells have voltages that are mismatched by more than 50mV, the internal discharge path turns on to discharge the cell with the higher voltage until the two cell voltages have a difference that is below 30mV. 

If battery over-voltage protection (OVP) occurs before the two cells are equalized, charging is suspended. 

The MP2672A integrates the balance path and control circuit. An external power dissipation resistor is also required to limit the balance current. If the cell balance function is not used, connect MID directly to AGND. 



<!-- Start of picture text -->
BATT<br>MID Balance<br>and<br>Protection<br>PGND<br><!-- End of picture text -->

**Figure 12: Battery Balance Block Diagram** 

# **Balancing Algorithm** 

The balance block only operates in charge mode. Balancing starts when any cell voltage exceeds the balance start point (VCELL_BAL). 

The voltage difference between cells should exceed VCELL_DIFF. The MP2672A detects the cell voltages in the pack, then checks the voltage difference between two cells. If the differential voltage exceeds VCELL_DIFF, the corresponding balance MOSFET turns on. 

To measure the open-circuit voltage of the cell, balancing is frequently suspended for a short duration. Charging always operates independently of the balance algorithm if no other charging fault occurs. The cell voltage is measured for 200µs when cell balancing is suspended. Then cell balancing operates for 249.8ms each 250ms cycle (see Figure 13). 



<!-- Start of picture text -->
On On On<br>Balance<br>MOSFET<br>Off Off<br>On On On<br>Cell Voltage<br>Measurement<br>Off Off Off<br>200µs 249.8ms<br><!-- End of picture text -->

**Figure 13: Battery Balance Clock** 

Figure 14 shows the battery balance flowchart. 



<!-- Start of picture text -->
POR<br>Turn off balancing path<br>and measure the cell<br>voltage<br>Any cell > VCELL_BAL? No<br>Yes<br> VCELL > VCELL_DIFF? No<br>Yes<br>Turn on the balancing<br>path<br><!-- End of picture text -->

**Figure 14: Battery Balance Flowchart** 

**24** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 25 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

For extremely unbalanced dual-cell batteries, the charger takes a few cycles to balance the battery voltages. For some applications, such as removable dual-cell batteries, a charger is required to balance two cells in one charge cycle. In this case, an external cell-balance circuit is recommended (see Figure 15). 

The MP2672A also has an option to automatically disable termination if cell balancing is active. By doing this, the two cells are better matched once charging is terminated. 

The cell voltage measured within the 200µs time is also delivered to the battery cell OVP block. If OVP occurs, charging is suspended (the battery FET turns off) until the measured cell voltage drops below the recovery threshold, which is set by REG00H, bit[0]. 

**Boost Converter Suspend Mode** 

The MP2672A offers suspend mode to turn off the boost converter even when the input is present. In this mode, the SYS pin is powered by the battery through the internal battery FET, and the input quiescent current is optimized. 

The MP2672A enters this mode by setting REG02H, bit[0] to 0. The MP2672A-000E is preset to this mode. The boost is suspended if any of the following conditions occur: 

- Charging terminated 

- Charging disabled 

- An NTC fault has occurred 

- A timer fault has occurred 

- Battery over-voltage protection (OVP) has occurred 



<!-- Start of picture text -->
BATT<br>Balance  MID<br>Control<br>PGND<br><!-- End of picture text -->

**Figure 15: External Cell-Balancing Circuit** 

# **Series Interface** 

The IC uses two wires: a serial data (SDA) wire and serial clock (SCL) wire. All I<sup>2</sup> C master and slave devices are connected with these two wires. The master (e.g. a microcontroller or digital signal processor) generates the bus clock and initiates communication on the bus. The slave devices receive and respond to the bus commands from the master device. To communicate with a specific device, each slave device must have a unique bus address. 

The I<sup>2</sup> C interface supports both standard mode (up to 100kbits), and fast mode (up to 400kbits). The SDA and SCL pins are open drains. Both the 

SDA and SCL are connected to the positive supply voltage via a current source or pull-up resistor. When the bus is free, both lines are pulled high. 

The MP2672A’s SDA is a bidirectional line, and SCL is a unidirectional line. 

The data on the SDA line must be stable during the high period of the clock (see Figure 16). The high or low state of the data line can only change when the clock signal on the SCL line is low. One clock pulse is generated for each data bit transferred. 

**25** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 26 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 



<!-- Start of picture text -->
SDA<br>Change of<br>SCL Data line stable;  data allowed<br>data valid<br><!-- End of picture text -->

**Figure 16: Bit Transfer on the I**<sup>**2**</sup> **C Bus** 

All transactions begin with a start (S) command and can be terminated by a stop (P) command. A start condition is defined as a high-to-low transition on the SDA line while SCL is high. A stop condition is defined as a low-to-high 

transition on the SDA line when the SCL is high (see Figure 17). Start and stop conditions are always generated by the master. The bus is considered busy after a start condition, and free after a stop condition. 



<!-- Start of picture text -->
SDA<br>SCL<br>Start (S) Stop (P)<br><!-- End of picture text -->

**Figure 17: Start and Stop Conditions** 

Data on the I<sup>2</sup> C bus is transferred in 8-bit packets (bytes) (see Figure 18). Each byte must be followed by an acknowledge bit (ACK). Data is transferred with the most significant bit (MSB) first. 

An acknowledgement occurs after every byte. The acknowledge bit allows the receiver to signal to the transmitter that the byte was successfully received and another byte may be sent. All clock pulses, including the 9th acknowledge clock pulse, are generated by the master. 



<!-- Start of picture text -->
Acknowledgement  Acknowledgement<br>SDA Signal from Slave Signal from Receiver<br>MSB<br>SCL<br>Start or  1 2 7 8 9 1 2 8 9 Stop or<br>Repeated  ACK ACK Repeated<br>Start Start<br><!-- End of picture text -->

**Figure 18: Data Transfer on the I**<sup>**2**</sup> **C Bus** 

**26** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 27 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

The transmitter releases the SDA line during the acknowledge clock pulse so the receiver can pull the SDA line low. If it remains high during the 9th clock pulse, this is called a not acknowledge (NACK) signal. The master can then generate either a stop condition to abort the transfer, or a repeated start (S) to start a new transfer. 

After the start condition is received, a slave address is sent. This address is 7 bits long followed by an 8th data direction bit (R/W). A 0 

indicates a transmission (write) and a 1 indicates a request for data (read). Figure 19 shows the complete data transfer. 

If the register address is not defined, the charger IC sends back a NACK signal and returns to the idle state. 

The MP2672A operates as a slave device with the address 4BH. The MP2672A supports single-byte R/W (see Figure 20 and Figure 21). 



<!-- Start of picture text -->
SDA<br>SCL<br>Start 1–7 8 9 1–7 8 9 1–7 8 9<br>Stop<br>Address R/W ACK Data ACK Data ACK<br>Figure 19: Complete Data Transfer<br>1 bit 7 bits 1 bit 1 bit 8 bits 1 bit 8 bits 1 bit 1 bit<br>S Slave Address 0 A Register Address A Data A P<br>From Master to Slave From Slave to Master A = Acknowledge (SDA Low) S = Start P = Stop<br>Figure 20: I 2 C Single Write<br>1 bit 7 bits 1 bit 1 bit 8 bits 1 bit 1 bit 7 bits 1 bit 1 bit 8 bits 1 bit 1 bit<br>S Slave Address 0 A Register Address A S Slave Address 1 A Data /A P<br>From Master to Slave A = Acknowledge (SDA Low) S = Start<br>From Slave to Master /A = not Acknowledge (SDA High) P = Stop<br><!-- End of picture text -->

**Figure 21: I**<sup>**2**</sup> **C Single Read** 

**27** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 28 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **I**<sup>**2**</sup> **C REGISTER MAP** 

## **IC Address 4BH** 

|**Register Name**|**Address**|**R/W**|**Description**|**Default**|
|---|---|---|---|---|
|REG00H|0x00|R/W|Battery regulation voltage, charge configuration,<br>and SYS voltage settingregister.|0011 1000|
|REG01H|0x01|R/W|Cell balance setting and charge current setting<br>register.|1000 1111|
|REG02H|0x02|R/W|Timer settingregister.|1001 0101|
|REG03H|0x03|R|Status register.|0000 0000|
|REG04H|0x04|R|Fault register.|0000 0000|



## **REG 00H (Default: 0011 1000)** 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|VBATT_REG[2]|0|Y|Y|R/W|000: 8.3V<br>001: 8.4V<br>010 85V|These bits set the battery|
|6|VBATT_REG[1]|0|Y|Y|R/W|: .<br>011: 8.6V<br>100: 8.7V<br>101: 88V|regulation voltage. They<br>are set to 001 by default.<br>They<br>are<br>OTP-<br>|
|5|VBATT_REG[0]|1|Y|Y|R/W|.<br>110: 8.9V<br>111: 8.2V|configurable.|
|4|CHG_CON<br>FIG|1|Y|Y|R/W|0: Charging disabled<br>1: Charging enabled|This bit is set to 1 by<br>default.|
|3|VBATT_PRE[2]|1|Y|N|R/W|0.4V|These bits set the system<br>minimum voltage offset. It<br>has a 6.0V offset, ranges|
|2|VBATT_PRE[1]|0|Y|N|R/W|0.2V|between 6.0V and 6.7V,<br>and is set to 6.4V by<br>default.<br>This threshold is also|
|1|VBATT_PRE[0]|0|Y|N|R/W|0.1V|used as the pre-charge<br>battery voltage threshold.<br>It is OTP-configurable.|
|0|CELL_OVP<br>_<br>HYS|0|Y|N|R/W|0: 80mV<br>1: 0mV|The bit sets the cell over-<br>voltage protection (OVP)<br>hysteresis.|



**28** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. 

© 2020 MPS. All Rights Reserved. 



<!-- page 29 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

## **REG 01H (Default: 1000 1111)** 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|NTC_TYPE|1|Y|Y|R/W|0: Standard<br>1: JEITA|This bit is set to 0 by<br>default.<br>It<br>is<br>OTP-<br>configurable.|
|6|VCELL_BAL|0|Y|Y|R/W|0: 3.5V<br>1: 3.7V|This bit sets the cell-<br>balance start point. It is set<br>to 0 by default, and is OTP-<br>configurable.|
|5|BALANCE_<br>THRESHOLD_<br>H2L|0|Y|Y|R/W|0: 50mV<br>1: 70mV|This bit sets the cell-<br>balance threshold. It is set<br>to 0 by default, and is OTP-<br>configurable.|
|4|BALANCE_<br>THRESHOLD_<br>L2H|0|Y|Y|R/W|0: 50mV<br>1: 70mV|This bit sets the cell-<br>balance threshold. It is set<br>to 0 by default, and is OTP-<br>configurable.|
|3|ICC[2]|1|Y|Y|R/W|800mA|These bits set the fast<br>charge current setting.<br>If RISETis 6kΩ:|
|2|ICC[2]|1|Y|Y|R/W|400mA|These bits have a 500mA<br>offset,<br>a<br>500mA<br>to<br>2000mA range, and are<br>set to 1111 by default.|
|1|ICC[1]|1|Y|Y|R/W|200mA|If RISETis 24kΩ:<br>These bits have a 125mA<br>offset, a 125mA to 500mA<br>range, are set to 1111 by|
|0|ICC[0]|1|Y|Y|R/W|100mA|<br>default, and are OTP-<br>configurable.|



**29** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 30 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

**REG 02H (Default: 1001 0101)** 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|fSW|1|Y|Y|R/W|0: 600kHz<br>1: 1200kHz|This bit is set to 1 by<br>default.<br>It<br>is<br>OTP-<br>configurable.|
|6|I<sup>2</sup>C_WD_<br>TIMER_<br>RESET|0|Y|N|R/W|0: Normal<br>1: Reset|This bit is set to 0 by<br>default.|
|5|WD_TIMER<br>[1]|0|Y|N|R/W|00: Disable timer<br>01: 40s|These bits set the I<sup>2</sup>C<br>watchdog timer limit. They|
|4|WD_TIMER<br>[0]|1|Y|N|R/W|10: 80s<br>11: 160s|are set to 01 by default,<br>and are OTP-configurable.|
|3|REGISTER_<br>RESET|0|Y|N|R/W|0: Keep current<br>setting<br>1: Reset|This bit is set to 0 by<br>default. After a reset, this<br>bit<br>returns<br>to<br>0<br>automatically.|
|2|CHG_TMR[1]|1|Y|Y|R/W|00: Disable charge<br>timer<br>01: 8 hors|These bits are set to 10 by|
|1|CHG_TMR[0]|0|Y|Y|R/W|u<br>10: 20 hours<br>11: 12 hours|default.|
|0|EN_SUSP|1|Y|Y|R/W|0: Enable<br>suspended mode<br>(disable the boost)<br>1: Disable<br>suspended mode<br>(enable the boost)|This bit is set to 1 by<br>default.|



**30** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 31 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **REG 03H (Default: 0000 0000)** 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|RESERVED|N/A|N/A|N/A|R|Reserved.|Reserved.|
|6|RESERVED|N/A|N/A|N/A|R|Reserved.|Reserved.|
|5|CHG_STAT[1]|0|N/A|N/A|R|00: Not charging<br>01: Pre-charge<br>10: Constant current<br>tt lt|These bits are set to 00|
|4|CHG_STAT[0]|0|N/A|N/A|R|or consan voage<br>charge<br>11: Charging<br>complete|by default.|
|3|PPM_STAT|0|N/A|N/A|R|0: Not in PPM<br>1: in VIN PPM|This bit is set to 0 by<br>default.|
|2|BATTFLOAT_<br>STAT|0|N/A|N/A|R|0: Battery present<br>1: Battery missing|This bit is set to 0 by<br>default.|
|1|THERM_<br>STAT|0|N/A|N/A|R|0: Normal<br>1: Thermal<br>regulation|This bit is set to 0 by<br>default.|
|0|VSYS_STAT|0|N/A|N/A|R|0: Not in VSYSMIN<br>regulation<br>1: In VSYSMIN<br>regulation|This bit is set to 0 by<br>default.|



**31** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 32 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **REG 04H (Default: 0000 0000)** 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|WD_FAULT|0|N/A|N/A|R|0: Normal operation<br>1: The watchdog<br>timer has expired|This bit is set to 0 by<br>default.|
|6|INPUT_FAULT|0|N/A|N/A|R|0: Normal operation<br>1: Input OVP has<br>occurred|This bit is set to 0 by<br>default.|
|5|THERMSD_<br>FAULT|0|N/A|N/A|R|0: Normal operation<br>1: Thermal<br>shutdown|This bit is set to 0 by<br>default.|
|4|TIMER_FAULT|0|N/A|N/A|R|0: Normal operation<br>1: The safety timer<br>has expired|This bit is set to 0 by<br>default.|
|3|BAT_FAULT|0|N/A|N/A|R|0: Normal operation<br>1: Battery OVP has<br>occurred|This bit is set to 0 by<br>default.|
|2|NTC_FAULT[2]|0|N/A|N/A|R|000: Normal<br>operation<br>001: An NTC cold<br>||
|1|NTC_FAULT[1]|0|N/A|N/A|R|fault has occurred<br>010: An NTC cool<br>fault has occurred<br>011: An NTC warm|These bits are set to<br>000 by default.|
|0|NTC_FAULT[0]|0|N/A|N/A|R|fault has occurred<br>100: An NTC hot<br>fault has occurred||



**32** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 33 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **REG 05H (Default: 1110 0000)**<sup>(10)</sup> 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|RCHG|1|N/A|N/A|N/A|0: No charging after<br>input start-up when<br>VBATT> VRECH<br>1: Automatic<br>charging after input<br>start-up when VBATT<br>> VRECH|This bit is set to 1 by<br>default.|
|6|RESERVED|1|N/A|N/A|N/A|Reserved.|Reserved.|
|5|BALANCE_<br>EOC_EN|1|N/A|N/A|N/A|0: Do not suspend<br>termination when<br>cell balancing is<br>active<br>1: Suspend<br>termination when<br>cell balancing is<br>active|This bit is set to 1 by<br>default.|
|4|TJ_REG[1]|0|N/A|N/A|N/A|00: 120°C<br>01: 100°C|This bit is set to 00 by|
|3|TJ_REG[0]|0|N/A|N/A|N/A|10: 80°C<br>11: 60°C|default.|
|2|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|1|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|0|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|



**33** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 34 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

## **REG 06H (Default: 0000 0011)**<sup>(10)</sup> 

|**Bit**|**Name**|**POR**|**Reset by**<br>**REG_RST**|**Reset**<br>**by WTD**|**R/W**|**Description**|**Comment**|
|---|---|---|---|---|---|---|---|
|7|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|6|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|5|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|4|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|3|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|2|RESERVED|N/A|N/A|N/A|N/A|Reserved.|Reserved.|
|1|RESERVED|1|N/A|N/A|N/A|Reserved.|Reserved.|
|0|NVDC_MODE_<br>EN|1|N/A|N/A|N/A|When charging is<br>suspended:<br>0: Disable DC/DC<br>switching<br>1: Enable DC/DC<br>switching|This bit is set to 1 by<br>default.|



**Note:** 

10) This register is for OTP only. It is not accessible. 

**34** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 35 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **OTP MAP** 

|**#**|**Bit[7]**|**Bit[6]**|**Bit[5]**|**Bit[4]**|**Bit[3]**|**Bit[2]**|**Bit[1]**|**Bit[0]**|
|---|---|---|---|---|---|---|---|---|
|00H|VB|ATT_REG: 8.2V-|8.9V|N/A|VBA|TT_PRE: 6.0V to|6.7V|N/A|
|01H|NTC Type|VCELL_BAL|VCELL_DIFF_HL|VCELL_DIFF_LH|ICC: 500m|A to 2000mA/|100mA step|(RISET= 6kΩ)|
|02H|FSW|N/A|WATC|HDOG|N/A|N/A|N/A|N/A|
|05H<sup>(10)</sup>|RCHG|N/A|BALANCE_<br>EOC_EN|TJ_REG: 60°C<br>100°C , or 1|, 80°C,<br>20°C|N/A|N/A|N/A|
|06H<sup>(10)</sup>|N/A|N/A|N/A|N/A||N/A|N/A|NVDC<br>Mode_EN|



**Note:** 

10) This register is for OTP only. It is not accessible. 

# **OTP DEFAULT** 

|**OTP Items**|**Default**|
|---|---|
|VBATT_REG|8.4V|
|VBATT_PRE|6.4V|
|NTC Type|JEITA|
|VCELL_BAL|3.5V|
|Balance Threshold H2L|50mV|
|Balance Threshold L2H|50mV|
|ICC|2000mA|
|SW FREQ|1200kHz|
|WATCHDOG|40s|
|RCHG|New charge cycle starts after start-upwhen VBATT> VRECH|
|BALANCE_EOC_EN|Enabled (if the two cells are not balanced, EOC is not<br>asserted,even all conditions are met)|
|Thermal Regulation Threshold|120°C|
|NVDC Mode_EN|Enable DC/DC switchingwhen chargingis suspended|



**35** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 36 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **APPLICATION INFORMATION** 

## **Setting the Charge Current in Standalone Mode** 

In standalone mode, the MP2672A’s charge current (ICC) can be set by an external resistor (RISET). Estimate ICC with Equation (4): 



The charge current can be configured up to 2.0A. Table 5 shows the expected RISET value for typical charge currents. 

**Table 5: Charge Current Setting Table** 

|**RISET (kΩ)**|**ICC (A)**|
|---|---|
|24|0.5|
|12|1.0|
|6|2.0|



## **Setting the Minimum Input Voltage Limit** 

In charge mode, connect a voltage divider from IN to AGND, then tap it to VLIM to configure the minimum input voltage. Calculate the minimum input voltage with Equation (5): 



Where 1.2V is the reference of the minimum input voltage loop. With a given RL, RH can be estimated with Equation (6): 



For example, if a 4.675V minimum input voltage limit is expected, RL = 10kΩ and RH = 28.7kΩ. 

## **Selecting an NTC Sensor Resistor** 

Figure 22 shows an internal voltage divider reference circuit that limits the high and low temperature thresholds for VHOT and VCOLD, respectively. 

For a given NTC thermistor, select the appropriate RT1 and RT2 values to set the NTC window. Calculate RT1 and RT2 using Equation (7) and Equation (8), respectively: 





Where VHOT is the high temperature threshold, VCOLD is the low temperature threshold, RH is the value of the NTC resistor at high temperatures within the required temperature operation range, and RL is the value of the NTC resistor at low temperatures. 



<!-- Start of picture text -->
VCC<br>RT1<br>VCOLD<br>NTC  VCOOL NTC<br>Protection<br>RT2<br>VWARM<br>RNTC<br>VHOT<br>AGND<br><!-- End of picture text -->

**Figure 22: NTC Protection Block** 

RT1 and RT2 allow the high temperature limit and low temperature limit to be configured independently. With this feature, the MP2672A can use most types of NTC resistors with different temperature operation range requirements. 

The RT1 and RT2 values depend on the type of the NTC resistor. For example, the 103AT thermistor has the following electrical characteristics: 

- At 0°C, RNTC_COLD = 27.28kΩ 

- At 60°C, RNTC_HOT = 3.02kΩ 

Based on Equations (7) and Equation (8), as well as the VHOT and VCOLD values from the electrical characteristics mentioned above, RT1 = 12.62kΩ, and RT2 = 3.63kΩ. 

Apply the spreadsheet for RT1 and RT2 calculation if required. 

**36** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 37 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

## **Selecting the Inductor** 

Inductor selection is a tradeoff between cost, size, and efficiency. A lower-value inductor results in lower DCR for components of a similar size, but results in higher current ripple, magnetic hysteretic losses, and output capacitances. The inductor ripple current should not exceed 30% of the maximum input current under the worst-case conditions. 

Choose an inductor that does not saturate under the worst-case load conditions. The inductor’s saturation current should be greater than the peak current limit of the low-side MOSFET. 

When the MP2672A works in charge mode, estimate the required inductance with Equation (9): 



Where VSYS is the system’s minimum regulation voltage, fSW is the switching frequency, and ∆IL_MAX is the peak-to-peak inductor ripple current, calculated with Equation (10): 



Where IL_PK is the expected inductor peak current, and IIN(MAX) is maximum input current, estimated with Equation (11): 



Where ISYS(MAX) is the maximum boost output current, and Ƞ is the boost efficiency. 

With an 8.4V battery voltage, 2A maximum charge current, 8.7V system voltage, typical input voltage (VIN = 5V), 1.2MHz switching frequency, 90% efficiency, and expected 4.5A inductor peak current, the inductance is calculated to be about 1.5μH. 

A 1.5µH inductor with >5A saturation current is recommended for applications with a 1.2MHz switching frequency. A 2.5µH inductor with >5A saturation current is recommended for applications with a 600kHz switching frequency. 

## **Selecting the Input Capacitor** 

CIN is the boost converter’s input capacitor in charge mode. Calculate CIN with Equation (12): 



Where ∆VIN / VIN can be estimated with Equation (13): 



Assume the maximum input voltage ripple is 1%. When VSYS is 9.2V, VIN is 5V, L is 1µH, and fSW is 1200kHz, then CIN is calculated to be 4.7µF. 

Place one >4.7µF ceramic capacitor with X5R or X7R dielectrics at the IN terminal. 

## **Selecting the System Capacitor** 

In charge mode, CSYS is the output capacitor of the boost converter. CSYS keeps the VSYS ripple small (<0.5%) and ensures feedback loop stability. Select the system capacitor based on the ripple current. For the best results, X5R or X7R dielectric ceramic capacitors are recommended for their low ESR and small temperature coefficients. For most applications, two 22µF capacitors and one 1µF capacitor are sufficient. Place these capacitors as close as possible to the IC. 

**37** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 38 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

## **PCB Layout Guidelines** 

Efficient PCB layout is critical for meeting specified noise, efficiency, and stability requirements. For the best results, refer to Figure 23 and follow the guidelines below: 

1. Place the output capacitor as close to SYS and PGND as possible. 

2. Place the local power input capacitors as close as possible to the IN and PGND pins. 

3. Minimize the length of the high-side switching node (SW, inductor) trace that carries the high current. 

4. Keep the switching node short, and route it away from all control signals, especially the feedback network. 

5. Route the power stages adjacent to their grounds. 



**Top Layer** 



**Bottom Layer** 

**Figure 23: Recommended PCB Layout** 

**38** 

MP2672A Rev. 1.0 11/10/2020 

www.MonolithicPower.com MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 39 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL APPLICATION CIRCUITS** 



<!-- Start of picture text -->
DC/DC MCU<br>CVCC CSYS<br>1μF<br>2 x 22μF<br>Other Rails<br>100nF BST VCC SYS<br>Optional Q2 Q3 BATT<br>L1 22μF<br>SW<br>Amplifier<br>CIN 1.5μH CBATT<br>10μF Q1<br>Motor<br>ACOK MID<br>Driver<br>VIN MP2672A<br>VLIM<br>SDA  STAT<br>VCC<br>SCL<br>RT1<br>NTC<br>CV ISET PGND AGND<br>RT2<br>RISET<br>RNTC<br><!-- End of picture text -->

**Figure 24: MP2672A-0000 Application Reference Circuit for NVDC Applications** 

**Table 6: Key BOM from Figure 24** 

|**Qty**|**Ref**|**Value**|**Description**|**Package **|**Manufacturer**|
|---|---|---|---|---|---|
|1|CIN|10µF|Ceramic capacitor,16V,X5R or X7R|0805|Any|
|2|CSYS|22µF|Ceramic capacitor,16V,X5R or X7R|0805|Any|
|1|CBATT|22µF|Ceramic capacitor,16V,X5R or X7R|1206|Any|
|1|CVCC|1µF|Ceramic capacitor,10V,X5R or X7R|0603|Any|
|1|CBST|100nF|Ceramic capacitor,25V,X5R or X7R|0603|Any|
|1|L1|1.5µH|Inductor, 1.5µH, saturation current >8A, low<br>DCR|SMD|Any|



**39** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 40 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **TYPICAL APPLICATION CIRCUITS** **_(continued)_** 



<!-- Start of picture text -->
CVCC CSYS<br>1μF 4.7μF<br>100nF VCC SYS<br>BST<br>CBST<br>Optional Q2 Q3<br>L1 BATT 22μF<br>SW<br>1.5μH<br>CIN CBATT<br>10μF Q1<br>ACO K MID<br>VIN MP2672A<br>VLIM<br>SDA  STAT<br>VCC<br>SCL<br>RT1<br>NTC<br>CV ISET PGND AGND<br>RT2<br>RISET<br>NTC<br><!-- End of picture text -->

**Figure 25: MP2672A-000E Application Reference Circuit for Charge Only Applications** 

**Table 7: Key BOM from Figure 25** 

|**Qty**|**Ref**|**Value**|**Description**|**Package **|**Manufacturer**|
|---|---|---|---|---|---|
|1|CIN|10µF|Ceramic capacitor,16V,X5R or X7R|0805|Any|
|1|CSYS|4.7µF|Ceramic capacitor,16V,X5R or X7R|0805|Any|
|1|CBATT|22µF|Ceramic capacitor,16V,X5R or X7R|1206|Any|
|1|CVCC|1µF|Ceramic capacitor,10V,X5R or X7R|0603|Any|
|1|CBST|100nF|Ceramic capacitor,25V,X5R or X7R|0603|Any|
|1|L1|1.5µH|Inductor; 1.5µH, saturation current >8A, low<br>DCR|SMD|Any|



**40** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 41 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **PACKAGE INFORMATION** 

## **QFN-18 (2mmx3mm)** 



<!-- Start of picture text -->
PIN 1 ID<br>MARKING PIN 1 ID<br>0.15X0.10 TYP<br>PIN 1 ID<br>INDEX AREA<br>TOP VIEW BOTTOM VIEW<br><!-- End of picture text -->

<u>SIDE VIEW</u> 



<!-- Start of picture text -->
0.15X0.10<br>RECOMMENDED LAND PATTERN<br><!-- End of picture text -->

## <u>NOTE:</u> 



<!-- Start of picture text -->
1) ALL DIMENSIONS ARE IN<br>MILLIMETERS.<br>2) EXPOSED PADDLE SIZE DOES NOT<br>INCLUDE MOLD FLASH.<br>3) LEAD COPLANARITY SHALL BE 0.10<br>MILLIMETERS MAX.<br>4) JEDEC REFERENCE IS MO-220.<br>5) DRAWING IS NOT TO SCALE.<br><!-- End of picture text -->

**41** 

MP2672A Rev. 1.0 www.MonolithicPower.com 11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 42 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **CARRIER INFORMATION** 





<!-- Start of picture text -->
Pin1 1 1 1 1<br>ABCD ABCD ABCD ABCD<br>Feed Direction<br><!-- End of picture text -->

|**Part Number**|**Package**<br>**Description**|**Quantity/**<br>**Reel**|**Quantity/**<br>**Tube**|**Quantity/**<br>**Tray**|**Reel**<br>**Diameter**|**Carrier**<br>**Tape**<br>**Width**|**Carrier**<br>**Tape**<br>**Pitch**|
|---|---|---|---|---|---|---|---|
|MP2672AGD-<br>xxxx–Z|QFN-18<br>(2mmx3mm)|5000|N/A|N/A|13in|12mm|8mm|



**42** 

MP2672A Rev. 1.0 12/1/2020 

www.MonolithicPower.com 

MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. © 2020 MPS. All Rights Reserved. 



<!-- page 43 -->

**MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER** 

# **Revision History** 

|**Revision #**|**Revision**<br>**Date**|**Description**|**Pages**<br>**Updated**|
|---|---|---|---|
|1.0|11/10/2020|Initial Release|-|



**Notice:** The information in this document is subject to change without notice. Users should warrant and guarantee that thirdparty Intellectual Property rights are not infringed upon when integrating MPS products into any application. MPS will not assume any legal responsibility for any said applications. 

**43** 

MP2672A Rev. 1.0 

www.MonolithicPower.com 

11/10/2020 MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited. 

© 2020 MPS. All Rights Reserved. 

