# MCP23017-MCP23S17-16-Bit-IO-Expander-with-Serial-Interface-DS20001952

*Source: `original/pmb/MCP23017-MCP23S17-16-Bit-IO-Expander-with-Serial-Interface-DS20001952.pdf` (41 pages)*

<!-- page 1 -->



# **MCP23017/MCP23S17** 

### **16-Bit I/O Expander with Serial Interface** 

##### **Features** 

- AEC-Q100 Automotive Qualified, See Product Identification System 

- 16-Bit Remote Bidirectional I/O Port (Pins GPA7, GPB7 are output only for **MCP23017)** : 

- I/O pins default to input 

- High-Speed I<sup>2</sup> C Interface ( **MCP23017** ): 

- 100 kHz 

- 400 kHz 

- 1.7 MHz 

- High-Speed SPI Interface ( **MCP23S17** ): 

- 10 MHz (maximum) 

- Three Hardware Address Pins to Allow Up to Eight Devices On the Bus 

- Configurable Interrupt Output Pins: 

- Configurable as active-high, active-low or open-drain 

- INTA and INTB Can Be Configured to Operate 

Independently or Together 

- Configurable Interrupt Source: 

- Interrupt-on-change from configured register defaults or pin changes 

- Polarity Inversion Register to Configure the Polarity of the Input Port Data 

- External Reset Input 

- Low Standby Current: 1 µA (max.) 

- Operating Voltage: 

- 1.8V to 5.5V @ –40°C to +85°C 

- 2.7V to 5.5V @ –40°C to +85°C 

- 4.5V to 5.5V @ –40°C to +125°C 

##### **Packages** 

- 28-pin QFN, 6 x 6 mm Body 

- 28-pin SOIC, Wide, 7.50 mm Body 

- 28-pin SPDIP, 300 mil Body 

- 28-pin SSOP, 5.30 mm Body 

##### **Package Types** 



<!-- Start of picture text -->
MCP23017 MCP23S17<br>GPB0 • 1 28 GPA7 GPB0 • 1 28 GPA7<br>GPB1 2 27 GPA6 GPB1 2 27 GPA6<br>GPB2 3 26 GPA5 GPB2 3 26 GPA5<br>GPB3 4 25 GPA4 GPB3 4 25 GPA4<br>GPB4 5 24 GPA3 GPB4 5 24 GPA3<br>GPB5 6 23 GPA2 SOIC GPB5 6 23 GPA2<br>GPB6 7 22 GPA1 SPDIP GPB6 7 22 GPA1<br>GPB7 8 21 GPA0 SSOP GPB7 8 21 GPA0<br>VDD 9 20 INTA VDD 9 20 INTA<br>VSS 10 19 INTB VSS 10 19 INTB<br>NC 11 18 RESET CS 11 18 RESET<br>SCK 12 17 A2 SCK 12 17 A2<br>SDA 13 16 A1 SI 13 16 A1<br>NC 14 15 A0 SO 14 15 A0<br>28 2726 25242322 28 2726 25242322<br>1 21 GPB4 1 21 GPA4<br>GPB4 GPA4<br>GPB5 2 20 GPA3 GPB5 2 20 GPA3<br>3 19 GPB6 3 19 GPA2<br>GPB6GPB7VDD 45 EP29 * 1817 GPA2GPA1GPA0 QFN GPB7VDD 45 EP29 * 1817 GPA1GPA0<br>VSS 6 16 INTA VSS 6 16 INTA<br>NC 7 15 INTB CS 7 15 INTB<br>8 9 1011 121314 8 9 1011121314<br>* Includes Exposed Thermal Pad; see Table 2-1.<br>GPB3 GPB2 GPB1 GPB0 GPA7 GPA6 GPA5 GPB3 GPB2 GPB1 GPB0 GPA7 GPA6 GPA5<br>NC A0 A1 A2 SCK SI SO A0 A1 A2<br>SCK SDA<br>RESET RESET<br><!-- End of picture text -->

DS20001952E-page 1 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 2 -->

**MCP23017/MCP23S17** 

##### **Functional Block Diagram** 



<!-- Start of picture text -->
MCP23S17<br>CS<br>SCK<br>SI<br>SPI<br>SO<br>MCP23017<br>GPB7<br>SCL Serializer/<br>GPB6<br>SDA I 2 C  Deserializer<br>GPB5<br>GPB4<br>3 GPIO<br>GPB3<br>A2:A0 Decode<br>GPB2<br>RESET Control GPB1<br>INTA Interrupt 16 GPB0<br>INTB Logic GPA7<br>GPA6<br>8 GPA5<br>GPA4<br>GPIO GPA3<br>Configuration/ GPA2<br>Control GPA1<br>Registers GPA0<br><!-- End of picture text -->

DS20001952E-page 2 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 3 -->

## **MCP23017/MCP23S17** 

#### **1.0 ELECTRICAL CHARACTERISTICS** 

##### **Absolute Maximum Ratings**<sup>**†**</sup> 

|Ambient temperature under bias............................................................................................................ –40°C to +125°C|
|---|
|Storage temperature .............................................................................................................................. –65°C to +150°C|
|Voltage on VDDwith respect to VSS......................................................................................................... –0.3V to +5.5V|
|Voltage on all other pins with respect to VSS(except VDD)............................................................ –0.6V to (VDD+ 0.6V)|
|Total power dissipation.........................................................................................................................................700 mW|
|Maximum current out of VSSpin ...........................................................................................................................150 mA|
|Maximum current into VDDpin ..............................................................................................................................125 mA|
|Input clamp current, IIK(VI< 0 or VI> VDD)..........................................................................................................±20 mA|
|Output clamp current, IOK(VO< 0 or VO> VDD)...................................................................................................±20 mA|
|Maximum output current sunk by any output pin ....................................................................................................25 mA|
|Maximum output current sourced by any output pin ...............................................................................................25 mA|
|ESD protection on all pins (HBM:MM) ..............................................................................................................4 kV:400V|
|**†**<br>**Notice**: Stresses above those listed under “Maximum Ratings” may cause permanent damage to the<br>device. This is a stress rating only, and functional operation of the device at those or any other conditions<br>above those indicated in the operational listings of this specification is not implied. Exposure to maximum<br>rating conditions for extended periods may affect device reliability.|



DS20001952E-page 3 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 4 -->

# **MCP23017/MCP23S17** 

## **1.1 DC Characteristics** 

### **TABLE 1-1: DC CHARACTERISTICS** 

|**Electric**|**al Specifications:**Unless o|therwise|noted, 1.8VV|DD 5.5V|at –40C|TA +1|25C|
|---|---|---|---|---|---|---|---|
|**Param.**<br>**No.**|<br>**Characteristic**|**Sym.**|**Min.**|**Typ.**<sup>**(1)**</sup>|**Max.**|**Units**|**Conditions**|
|D001|SupplyVoltage|VDD|1.8|—|5.5|V||
|D002|VDDStart Voltage to<br>ensure Power-on Reset|VPOR|—|VSS|—|V||
|D003|VDDRise Rate to ensure<br>Power-on Reset|SVDD|0.05|—|—|V/ms|Design guidance only.<br>Not tested.|
|D004|SupplyCurrent|IDD|—|—|1|mA|SCL/SCK = 1 MHz|
|D005|Standby current|IDDS8|—|—|1|µA|–40°CTA +85°C|
||||—|—|3|µA|4.5VVDD 5.5V<br>+85°CTA +125C|
||||||||**(Note 1)**|
|**Input Lo**|**w Voltage**|||||||
|D030|A0, A1, A2(TTL buffer)|VIL|VSS|—|0.15 VDD|V||
|D031|CS<br>, GPIO,SCL/SCK,<br>SDA RESET|VIL|VSS|—|0.2 VDD|V||
||,<br>(Schmitt Trigger)|||||||
|**Input Hi**|**gh Voltage**|||||||
|D040|A0, A1, A2(TTL buffer)|VIH|0.25 VDD+ 0.8|—|VDD|V||
|D041|CS<br>,GPIO, SCL/SCK,<br>|VIH|0.8 VDD|—|VDD|V|For entire VDDrange|
||SDA, RESET<br>(Schmitt Trigger)|||||||
|**Input Le**|**akage Current**|||||||
|D060|I/O port pins|IIL|—|—|±1|µA|VSS VPIN VDD|
|**Output**|**Leakage Current**|||||||
|D065|I/Oportpins|ILO|—|—|±1|µA|VSS VPIN VDD|
|D070|GPIO weak pull-up|IPU|40|75|115|µA|VDD= 5V|
||current||||||GPpins = VSS|
|**Output**|**Low-Voltage**|||||||
|D080|GPIO|VOL|—|—|0.6|V|IOL= 8.0 mA<br>VDD= 4.5V|
||INT|VOL|—|—|0.6|V|IOL= 1.6 mA<br>VDD= 4.5V|
||SO, SDA|VOL|—|—|0.6|V|IOL= 3.0 mA<br>VDD= 1.8V|
||SDA|VOL|—|—|0.8|V|IOL= 3.0 mA|
||||||||VDD= 4.5V|
|**Output**|**High-Voltage**|||||||
|D090|GPIO, INT, SO|VOH|VDD– 0.7|—|—|V|IOH= –3.0 mA<br>VDD= 4.5V|
||||VDD– 0.7|—|—||IOH= –400 µA|
|**Capacit**|**ive Loading Specs on Out**|**put Pins**|||||VDD= 1.8V|
|D101|GPIO, SO, INT|CIO|—|—|50|pF||
|D102|SDA|CB|—|—|400|pF||



**Note 1:** This parameter is characterized, not 100% tested. 

DS20001952E-page 4 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 5 -->

**MCP23017/MCP23S17** 

## **1.2 AC Characteristics** 



<!-- Start of picture text -->
VDD<br>Pin<br>1 k<br>SCL and<br>50 pF<br>SDA pin<br>MCP23017<br>135 pF<br><!-- End of picture text -->



<!-- Start of picture text -->
FIGURE 1-1: Load Conditions for device Timing Specifications.<br><!-- End of picture text -->





<!-- Start of picture text -->
VDD<br>RESET<br>Internal<br>RESET<br>Output pin<br><!-- End of picture text -->



<!-- Start of picture text -->
30 32<br>34<br><!-- End of picture text -->

**_FIGURE 1-2:_** _RESET and Device Reset Timer Timing._ 

### **TABLE 1-2: DEVICE RESET SPECIFICATIONS** 

**AC Characteristics:** Unless otherwise noted, 1.8V VDD  5.5V at -40C  TA  +125C 

|**Param.**<br>**No.**|**Characteristic**|**Sym.**|**Min.**|**Typ.**<sup>**(1)**</sup>|**Max.**|**Units**|**Conditions**|
|---|---|---|---|---|---|---|---|
|30|RESET<br>Pulse Width<br>(Low)|TRSTL|1|—|—|µs||
|32|Device Active After Reset<br>high|THLD|—|0|—|ns|VDD= 5.0V|
|34|Output High-Impedance<br>From RESET<br>Low|TIOZ|—|—|1|µs||



**Note 1:** This parameter is characterized, not 100% tested. 

DS20001952E-page 5 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 6 -->

# **MCP23017/MCP23S17** 

|SCL|91||||93|
|---|---|---|---|---|---|
||90||||92|
|SDA|Start<br>Condition||||Stop<br>Condition|
|**_FIGURE_**|**_1-3:_**<br>_I_<sup>_2_</sup>_C Bus Start/Stop Bits Tim_|_ing._||||
||100<br>103||||102|
||SCL|101||||
||90<br>91<br>10<br>|6<br>10|7||92|
||SDA<br>In|||||
||109|109|||110|
||SDA<br>Out|||||
|**_FIGURE_**<br>**TABLE**|**_1-4:_**<br>_I_<sup>_2_</sup>_C Bus Data Timing._<br>**1-3:**<br>**I**<sup>**2**</sup>**C BUS DATA REQUIREMEN**|**TS**||||
|**I**<sup>**2**</sup>**C Inte**<br>SDA) =<br>**P**|**rface AC Characteristics:**Unless otherwis<br>1 k, CL(SCL, SDA) = 135 pF|e noted, 1.8VVD|D 5.|5V at –|40CTA +125C**,**RPU(|
|**aram.**<br>**No.**|**Characteristic**<br>**Sym.**|**Min.**|**Typ.**|**Max.**|**Units**<br>**Conditions**|
|100|Clock High Time:<br>THIGH|||||
||100 kHz mode|4.0|—|—|µs<br>1.8V – 5.5V|
||400 kHz mode|0.6|—|—|µs<br>2.7V – 5.5V|
||1.7 MHz mode|0.12|—|—|µs<br>4.5V – 5.5V|
|101|Clock Low Time:<br>TLOW|||||
||100 kHz mode|4.7|—|—|µs<br>1.8V – 5.5V|
||400 kHz mode|1.3|—|—|µs<br>2.7V – 5.5V|
||1.7 MHz mode|0.32|—|—|µs<br>4.5V – 5.5V|
|102|SDA and SCL Rise Time:<br>TR<br>**(1)**|||||
||100 kHz mode|—|—|1000|ns<br>1.8V – 5.5V|
||400 kHz mode|20 + 0.1 CB <sup>**(2)**</sup>|—|300|ns<br>2.7V – 5.5V|
||1.7 MHz mode|20|—|160|ns<br>4.5V – 5.5V|
|103|SDA and SCL Fall Time:<br>TF<br>**(1)**|||||
||100 kHz mode|—|—|300|ns<br>1.8V – 5.5V|
||400 kHz mode|20 + 0.1 CB<br>**(2)**|—|300|ns<br>2.7V – 5.5V|
||1.7 MHz mode|20|—|80|ns<br>4.5V – 5.5V|
|**Note 1:**|This parameter is characterized, not 100|% tested.||||
|**2:**|CBis specified to be from 10 to 400 pF.|||||



**I**<sup>**2**</sup> **C Interface AC Characteristics:** Unless otherwise noted, 1.8V VDD  5.5V at –40C  TA  +125C **,** RPU (SCL, SDA) = 1 k, CL (SCL, SDA) = 135 pF 

DS20001952E-page 6 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 7 -->

# **MCP23017/MCP23S17** 

**TABLE 1-3: I**<sup>**2**</sup> **C BUS DATA REQUIREMENTS (CONTINUED)** 

|**I**<sup>**2**</sup>**C Inte**<br>SDA) =<br>**P**|**rface AC Characteristics:**Unles<br>1 k, CL(SCL, SDA) = 135 pF|s otherwise n|oted, 1.8V|VDD 5.|5V at –|40C|TA +125C**,**RPU(SCL,|
|---|---|---|---|---|---|---|---|
|**aram.**<br>|**Characteristic**|**Sym.**|**Min.**|**Typ.**|**Max.**|**Units**|**Conditions**|
|**No.**||||||||
|90|START Condition Setup Time:|TSU:STA||||||
||100 kHz mode||4.7|—|—|µs|1.8V – 5.5V|
||400 kHz mode||0.6|—|—|µs|2.7V – 5.5V|
||1.7 MHz mode||0.16|—|—|µs|4.5V – 5.5V|
|91|START Condition Hold Time:|THD:STA||||||
||100 kHz mode||4.0|—|—|µs|1.8V – 5.5V|
||400 kHz mode||0.6|—|—|µs|2.7V – 5.5V|
||1.7 MHz mode||0.16|—|—|µs|4.5V – 5.5V|
|106|Data Input Hold Time:|THD:DAT||||||
||100 kHz mode||0|—|3.45|µs|1.8V – 5.5V|
||400 kHz mode||0|—|0.9|µs|2.7V – 5.5V|
||1.7 MHz mode||0|—|0.15|µs|4.5V – 5.5V|
|107|Data Input Setup Time:|TSU:DAT||||||
||100 kHz mode||250|—|—|ns|1.8V – 5.5V|
||400 kHz mode||100|—|—|ns|2.7V – 5.5V|
||1.7 MHz mode||0.01|—|—|µs|4.5V – 5.5V|
|92|Stop Condition Setup Time:|TSU:STO||||||
||100 kHz mode||4.0|—|—|µs|1.8V – 5.5V|
||400 kHz mode||0.6|—|—|µs|2.7V – 5.5V|
||1.7 MHz mode||0.16|—|—|µs|4.5V–5.5V|
|109|Output Valid From Clock:|TAA||||||
||100 kHz mode||—|—|3.45|µs|1.8V – 5.5V|
||400 kHz mode||—|—|0.9|µs|2.7V – 5.5V|
||1.7 MHz mode||—|—|0.18|µs|4.5V – 5.5V|
|110|Bus Free Time:|TBUF||||||
||100 kHz mode||4.7|—|—|µs|1.8V – 5.5V|
||400 kHz mode||1.3|—|—|µs|2.7V – 5.5V|
||1.7 MHz mode||N/A|—|N/A|µs|4.5V – 5.5V|
|111|Bus Capacitive Loading:|CB||||||
||100 kHz and 400 kHz||—|—|400|pF|**Note 1**|
||1.7 MHz||—|—|100|pF|**Note 1**|
|112|Input Filter Spike Suppression<br>(SDA and SCL):|TSP||||||
||100 kHz and 400 kHz||—|—|50|ns||
||1.7 MHz||—|—|10|ns|Spike suppression off|



**Note 1:** This parameter is characterized, not 100% tested. 

**2:** CB is specified to be from 10 to 400 pF. 

DS20001952E-page 7 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 8 -->

**MCP23017/MCP23S17** 



<!-- Start of picture text -->
CS (1) 3<br>11<br>1 6 10<br>Mode 1,1 7 2<br>SCK Mode 0,0<br>4 5<br>SI<br>MSB in LSB in<br>SO High-Impedance<br>Note 1:  When using SPI Mode 1,1 the CS pin needs to be toggled once before the first communication after<br>power-up.<br><!-- End of picture text -->



<!-- Start of picture text -->
FIGURE 1-5: SPI Input Timing.<br><!-- End of picture text -->



<!-- Start of picture text -->
CS<br>2<br>8 9<br>SCK Mode 1,1<br>Mode 0,0<br>12<br>14<br>13<br>SO<br>MSB out LSB out<br>Don’t Care<br>SI<br><!-- End of picture text -->

**_FIGURE 1-6:_** _SPI Output Timing._ 

**TABLE 1-4: SPI INTERFACE REQUIREMENTS** 

**SPI Interface AC Characteristics:** Unless otherwise noted, 1.8V VDD  5.5V at –40C  TA  +125C 

|**Param.**<br>**No.**|**Characteristic**|**Sym.**|**Min.**|**Typ.**|**Max.**|**Units**|**Conditions**|
|---|---|---|---|---|---|---|---|
|—|Clock Frequency|FCLK|—|—|5|MHz|1.8V – 5.5V|
||||—|—|10|MHz|2.7V – 5.5V|
||||—|—|10|MHz|4.5V – 5.5V|
|1|CS<br>SetupTime|TCSS|50|—|—|ns||
|2|CS<br>Hold Time|TCSH|100|—|—|ns|1.8V – 5.5V|
||||50|—|—|ns|2.7V – 5.5V|
|3|CS<br>Disable Time|TCSD|100|—|—|ns|1.8V – 5.5V|
||||50|—|—|ns|2.7V – 5.5V|
|4|Data Setup Time|TSU|20|—|—|ns|1.8V – 5.5V|
||||10|—|—|ns|2.7V – 5.5V|



**Note 1:** This parameter is characterized, not 100% tested. 

DS20001952E-page 8 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 9 -->

# **MCP23017/MCP23S17** 

**TABLE 1-4: SPI INTERFACE REQUIREMENTS (CONTINUED)** 

**SPI Interface AC Characteristics:** Unless otherwise noted, 1.8V VDD  5.5V at –40C  TA  +125C 

|**Param.**<br>**No.**|**Characteristic**|**Sym.**|**Min.**|**Typ.**|**Max.**<br>**Units**|**Conditions**|
|---|---|---|---|---|---|---|
|5|Data Hold Time|THD|20|—|—<br>ns|1.8V – 5.5V|
||||10|—|—<br>ns|2.7V – 5.5V|
|6|CLK Rise Time|TR|—|—|2<br>µs|**Note 1**|
|7|CLK Fall Time|TF|—|—|2<br>µs|**Note 1**|
|8|Clock High Time|THI|90|—|—<br>ns|1.8V – 5.5V|
||||45|—|—<br>ns|2.7V – 5.5V|
|9|Clock Low Time|TLO|90|—|—<br>ns|1.8V – 5.5V|
||||45|—|—<br>ns|2.7V – 5.5V|
|10|Clock DelayTime|TCLD|50|—|—<br>ns||
|11|Clock Enable Time|TCLE|50|—|—<br>ns||
|12|Output Valid from Clock Low|TV|—|—|90<br>ns|1.8V – 5.5V|
||||—|—|45<br>ns|2.7V – 5.5V|
|13|Output Hold Time|THO|0|—|—<br>ns||
|14|Output Disable Time|TDIS|—|—|100<br>ns||
|**Note 1:**|This parameter is characterize|d, not 100|% teste|d.|||
|SCL|/SCK||||||
|S|DA/SI<br>In<br>D1|D0|||||
||LSb of<br>during<br>comma<br>on para|data byte ze<br>a write or re<br>nd, dependi<br>meter|ro<br>ad<br>ng|50|||
|O|GPn<br><br>utput||||||
||Pin|||51|||
||INT<br>Pin<br>||||||
||INT Pin<br>GPn|ctive|||Inactive<br>53||
||Inut||||||
||Pin<br>p||||||
||||||52||
|Re<br>Lo|gister<br>aded||||||



**_FIGURE 1-7:_** _GPIO and INT Timing._ 

DS20001952E-page 9 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 10 -->

# **MCP23017/MCP23S17** 

**TABLE 1-5: GP AND INT PINS REQUIREMENTS** 

|**GP and IN**<br>**P**|**T Pins AC Characteristics:**|Unless oth|erwise|noted, 1.|8VVD|D 5.5V|at –40CTA +125C|
|---|---|---|---|---|---|---|---|
|**aram.**<br>**No.**|**Characteristic**|**Sym.**|**Min.**|**Typ.**|**Max.**|**Units**|**Conditions**|
|50|Serial Data to Output Valid|TGPOV|—|—|500|ns||
|51|Interrupt Pin Disable Time|TINTD|—|—|600|ns||
|52|GP Input Change to<br>Register Valid|TGPIV|—|—|450|ns||
|53|IOC Event to INT Active|TGPINT|—|—|600|ns||
||Glitch Filter on GP Pins|TGLITCH|—|—|150|ns|**Note 1**|



**Note 1:** This parameter is characterized, not 100% tested. 

DS20001952E-page 10 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 11 -->

**MCP23017/MCP23S17** 

## **2.0 PIN DESCRIPTIONS** 

The descriptions of the pins are listed in Table 2-1. 

|**TABLE**|**2-1:**|**PINO**|**UT D**|**ESCRIPTION**|
|---|---|---|---|---|
|**Pin**<br>**Name**|**QFN**|**SOIC**<br>**SPDIP**<br>**SSOP**|**Pin**<br>**Type**|**Function**|
|GPB0|25|1|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB1|26|2|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB2|27|3|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB3|28|4|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB4|1|5|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB5|2|6|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB6|3|7|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPB7|4|8|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor./<br>Output only (**MCP23017**).|
|VDD|5|9|P|Power|
|VSS|6|10|P|Ground|
|NC/CS|7|11|I|NC (**MCP23017**)/Chip Select (**MCP23S17**)|
|SCK|8|12|I|Serial clock input|
|SDA/SI|9|13|I/O|Serial data I/O(**MCP23017**)/Serial data input(**MCP23S17**)|
|NC/SO|10|14|O|NC (**MCP23017**)/Serial data out (**MCP23S17**)|
|A0|11|15|I|Hardware address pin. Must be externallybiased.|
|A1|12|16|I|Hardware addresspin. Must be externallybiased.|
|A2|13|17|I|Hardware address pin. Must be externally biased.|
|RESET|14|18|I|Hardware reset. Must be externallybiased.|
|INTB|15|19|O|Interrupt output for PORTB. Can be configured as active-high, active-low or open-drain.|
|INTA|16|20|O|Interrupt output for PORTA. Can be configured as active-high, active-low or open-drain.|
|GPA0|17|21|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPA1|18|22|I/O|Bidirectional I/Opin. Can be enabled for interrupt-on-change and/or internal weakpull-upresistor.|
|GPA2|19|23|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPA3|20|24|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPA4|21|25|I/O|Bidirectional I/Opin. Can be enabled for interrupt-on-change and/or internal weakpull-upresistor.|
|GPA5|22|26|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPA6|23|27|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor.|
|GPA7|24|28|I/O|Bidirectional I/O pin. Can be enabled for interrupt-on-change and/or internal weak pull-up resistor./<br>Output only (**MCP23017**).|
|EP|29|—|—|Exposed Thermal Pad. Either connect to VSS, or leave unconnected.|



DS20001952E-page 11 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 12 -->

**MCP23017/MCP23S17** 

## **3.0 DEVICE OVERVIEW** 

MCP23017/MCP23S17 (MCP23X17) device family provides 16-bit, general purpose parallel I/O expansion for I<sup>2</sup> C bus or SPI applications. The two devices differ only in the serial interface: 

- MCP23017 – I<sup>2</sup> C interface 

- MCP23S17 – SPI interface 

MCP23X17 consists of multiple 8-bit configuration registers for input, output and polarity selection. The system host can enable the I/Os as either inputs or outputs by writing the I/O configuration bits (IODIRA/B). The data for each input or output is kept in the corresponding input or output register. The polarity of the Input Port register can be inverted with the Polarity Inversion register. All registers can be read by the system host. 

The 16-bit I/O port functionally consists of two 8-bit ports (PORTA and PORTB). MCP23X17 can be configured to operate in the 8-bit or 16-bit modes via IOCON.BANK. 

There are two interrupt pins, INTA and INTB, that can be associated with their respective ports, or can be logically OR’ed together so that both pins will activate if either port causes an interrupt. 

The interrupt output can be configured to activate under two conditions (mutually exclusive): 

1. When any input state differs from its corresponding Input Port register state. This is used to indicate to the system host that an input state has changed. 

2. When an input state differs from a preconfigured register value (DEFVAL register). 

The Interrupt Capture register captures port values at the time of the interrupt, thereby saving the condition that caused the interrupt. 

### **3.2 Serial Interface** 

This block handles the functionality of the I<sup>2</sup> C ( **MCP23017** ) or SPI ( **MCP23S17** ) interface protocol. MCP23X17 contains 22 individual registers (11 register pairs) that can be addressed through the Serial Interface block, as shown in Table 3-1. 

**TABLE 3-1: REGISTER ADDRESSES** 

|**Address**<br>**IOCON.BANK =1**|**Address**<br>**IOCON.BANK =0**|**Access to:**|
|---|---|---|
|00h|00h|IODIRA|
|10h|01h|IODIRB|
|01h|02h|IPOLA|
|11h|03h|IPOLB|
|02h|04h|GPINTENA|
|12h|05h|GPINTENB|
|03h|06h|DEFVALA|
|13h|07h|DEFVALB|
|04h|08h|INTCONA|
|14h|09h|INTCONB|
|05h|0Ah|IOCON|
|15h|0Bh|IOCON|
|06h|0Ch|GPPUA|
|16h|0Dh|GPPUB|
|07h|0Eh|INTFA|
|17h|0Fh|INTFB|
|08h|10h|INTCAPA|
|18h|11h|INTCAPB|
|09h|12h|GPIOA|
|19h|13h|GPIOB|
|0Ah|14h|OLATA|
|1Ah|15h|OLATB|



The Power-on Reset (POR) sets the registers to their default values and initializes the device state machine. The hardware address pins are used to determine the device address. 

### **3.1 Power-on Reset (POR)** 

The on-chip POR circuit holds the device in reset until VDD has reached a high enough voltage to deactivate the POR circuit (i.e., release the device from reset). The maximum VDD rise time is specified in **Section 1.0 “Electrical Characteristics”** . 

When the device exits the POR condition (releases reset), device operating parameters (i.e., voltage, temperature, serial bus frequency, etc.) must be met to ensure proper operation. 

DS20001952E-page 12 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 13 -->

**MCP23017/MCP23S17** 

### 3.2.1 BYTE MODE AND SEQUENTIAL MODE 

MCP23X17 family has the ability to operate in Byte mode or Sequential mode (IOCON.SEQOP). 

**Byte mode** disables automatic Address Pointer incrementing. When operating in Byte mode, MCP23X17 family does not increment its internal address counter after each byte during the data transfer. This gives the ability to continually access the same address by providing extra clocks (without additional control bytes). This is useful for polling the GPIO register for data changes or for continually writing to the output latches. 

A special mode **(Byte mode with IOCON.BANK = 0)** causes the address pointer to toggle between associated A/B register pairs. For example, if the BANK bit is cleared and the Address Pointer is initially set to address 12h (GPIOA) or 13h (GPIOB), the pointer will toggle between GPIOA and GPIOB. Note that the Address Pointer can initially point to either address in the register pair. 

**Sequential mode** enables automatic address pointer incrementing. When operating in Sequential mode, MCP23X17 family increments its address counter after each byte during the data transfer. The Address Pointer automatically rolls over to address 00h after accessing the last register. 

These two modes are not to be confused with single writes/reads and continuous writes/reads that are serial protocol sequences. For example, the device may be configured for Byte mode and the host may perform a continuous read. In this case, MCP23X17 would not increment the Address Pointer and would repeatedly drive data from the same location. 

### 3.2.2 I<sup>2</sup> C INTERFACE 

### 3.2.2.1 I<sup>2</sup> C Write Operation 

The I<sup>2</sup> C write operation includes the control byte and register address sequence, as shown in Figure 3-1. This sequence is followed by eight bits of data from the host and an Acknowledge (ACK) from the MCP23017. The operation is ended with a Stop (P) or Restart (SR) condition being generated by the host. 

Data is written to MCP23017 after every byte transfer. If a Stop or Restart condition is generated during a data transfer, the data will not be written to MCP23017. 

Both “byte writes” and “sequential writes” are supported by MCP23017. If Sequential mode is enabled (IOCON, SEQOP = 0) (default), MCP23017 increments its address counter after each ACK during the data transfer. 



<!-- Start of picture text -->
S - Start Byte S OP W ADDR D IN P<br>SR - Restart Sequential S OP W ADDR D IN .... D IN P<br>P - Stop<br>W - Write<br>R - Read<br>OP - Device opcode<br>ADDR - Device register address<br>D OUT - Data out from MCP23017<br>D IN - Data in to MCP23017<br><!-- End of picture text -->

**_FIGURE 3-1:_** _Byte and Sequential Write._ 

DS20001952E-page 13 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 14 -->

# **MCP23017/MCP23S17** 

### 3.2.2.2 I<sup>2</sup> C Read Operation 

I<sup>2</sup> C Read operations include the control byte sequence, as shown in Figure 3-2. This sequence is followed by another control byte (including the Start condition and ACK) with the R/W bit set (R/W = 1). The MCP23017 then transmits the data contained in the addressed register. The sequence is ended with the host generating a Stop or Restart condition. 



<!-- Start of picture text -->
Byte S OP W ADDR SR OP R DOUT P<br>Sequential S OP W ADDR SR OP R D OUT .... D OUT P<br><!-- End of picture text -->

### **_FIGURE 3-2:_** _Byte and Sequential Read._ 

### 3.2.2.3 I<sup>2</sup> C Sequential Write/Read 

For sequential operations (Write or Read), instead of transmitting a Stop or Restart condition after the data transfer, the host clocks the next byte pointed to by the address pointer (see **Section 3.2.1 “Byte Mode and Sequential Mode”** for details regarding sequential operation control). 

The sequence ends with the host sending a Stop or Restart condition. 

MCP23017 Address Pointer will roll over to address zero after reaching the last register address. Refer to Figure 3-3. 



<!-- Start of picture text -->
S OP W ADDR D IN .... D IN P<br>SR OP R D OUT .... D  OUT P<br>SR OP W D IN .... D IN P<br>P<br>S OP R D OUT .... D OUT P<br>SR OP R D OUT .... D OUT P<br>SR OP W ADDR D IN .... D IN P<br>P<br><!-- End of picture text -->

**_FIGURE 3-3:_** _MCP23017 I_<sup>_2_</sup> _C Device Protocol._ 

DS20001952E-page 14 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 15 -->

**MCP23017/MCP23S17** 

### 3.2.3 SPI INTERFACE 

### 3.2.3.1 SPI Write Operation 

The SPI write operation is started by lowering CS. The Write command (client address with R/W bit cleared) is then clocked into the device. The opcode is followed by an address and at least one data byte. 

### 3.2.3.2 SPI Read Operation 

The SPI read operation is started by lowering CS. The SPI read command (client address with R/W bit set) is then clocked into the device. The opcode is followed by an address, with at least one data byte being clocked out of the device. 

### 3.2.3.3 SPI Sequential Write/Read 

For sequential operations, instead of deselecting the device by raising CS, the host clocks the next byte pointed to by the Address Pointer. (see **Section 3.2.1 “Byte Mode and Sequential Mode”** for details regarding sequential operation control). 

The sequence ends by the raising of CS. 

MCP23S17 Address Pointer will roll over to address zero after reaching the last register address. 

## **3.3 Hardware Address Decoder** 

The hardware address pins are used to determine the device address. To address a device, the corresponding address bits in the control byte must match the pin state. The pins must be biased externally. 

### 3.3.1 ADDRESSING I<sup>2</sup> C DEVICES ( **MCP23017** ) 

MCP23017 is a client I<sup>2</sup> C interface device that supports 7-bit client addressing, with the read/write bit filling out the control byte. The client address contains four fixed 

bits and three user-defined hardware address bits (pins A2, A1 and A0). Figure 3-4 shows the control byte format. 

### 3.3.2 ADDRESSING SPI DEVICES ( **MCP23S17** ) 

MCP23S17 is a client SPI device. The client address contains four fixed bits and three user-defined hardware address bits (if enabled via IOCON.HAEN) (pins A2, A1 and A0) with the read/write bit filling out the control byte. Figure 3-5 shows the control byte format. The address pins should be externally biased even if disabled (IOCON.HAEN = 0). 



<!-- Start of picture text -->
Control Byte<br>S 0 1 0 0 A2 A1 A0 R/W ACK<br>Client Address<br>Start R/W bit<br>bit ACK bit<br>R/W = 0 = write<br>R/W = 1 = read<br>FIGURE 3-4: I 2 C Control Byte Format.<br>CS<br>Control Byte<br>0 1 0 0 A2 A1 A0 R/W<br>Client Address<br>R/W bit<br>R/W = 0 = write<br>R/W = 1 = read<br><!-- End of picture text -->



<!-- Start of picture text -->
FIGURE 3-4: I 2 C Control Byte Format.<br><!-- End of picture text -->



<!-- Start of picture text -->
FIGURE 3-5: SPI Control Byte Format.<br><!-- End of picture text -->



<!-- Start of picture text -->
S 0 1 0 0 A2 A1 A0 0 ACK  * A7 A6 A5 A4 A3 A2 A1 A0 ACK  *<br>R/W = 0<br>Device Opcode Register Address<br>*The ACKs are provided by the MCP23017.<br><!-- End of picture text -->

**_FIGURE 3-6:_** _I_<sup>_2_</sup> _C Addressing Registers._ 

DS20001952E-page 15 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 16 -->

# **MCP23017/MCP23S17** 



<!-- Start of picture text -->
CS<br>0 1 0 0 A2  * A1 * A0 * R/W A7 A6 A5 A4 A3 A2 A1 A0<br>Device Opcode Register Address<br><!-- End of picture text -->



<!-- Start of picture text -->
*  Address pins are enabled/disabled via IOCON.HAEN.<br><!-- End of picture text -->

**_FIGURE 3-7:_** _SPI Addressing Registers._ 

## **3.4 GPIO Port** 

The GPIO module is a general purpose, 16-bit wide, bidirectional port that is functionally split into two 8-bit wide ports. 

The GPIO module contains the data ports (GPIOn), internal pull-up resistors and the output latches (OLATn). 

Reading the GPIOn register reads the value on the port. Reading the OLATn register only reads the latches, not the actual value on the port. 

Writing to the GPIOn register actually causes a write to the latches (OLATn). Writing to the OLATn register forces the associated output drivers to drive to the level in OLATn. Pins configured as inputs turn off the associated output driver and put it in high-impedance. 

**TABLE 3-2: SUMMARY OF REGISTERS ASSOCIATED WITH THE GPIO PORTS (BANK = 1)** 

|**Register**<br>**Name**|**Address**<br>**(hex)**|**bit 7**|**bit 6**|**bit 5**|**bit 4**|**bit 3**|**bit 2**|**bit 1**|**bit 0**|**POR/RST**<br>**value**|
|---|---|---|---|---|---|---|---|---|---|---|
|IODIRA|00|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IPOLA|01|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|GPINTENA|02|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|GPPUA|06|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|GPIOA|09|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|OLATA|0A|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|
|IODIRB|10|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IPOLB|11|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|GPINTENB|12|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|GPPUB|16|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|GPIOB|19|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|OLATB|1A|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|



**TABLE 3-3: SUMMARY OF REGISTERS ASSOCIATED WITH THE GPIO PORTS (BANK = 0)** 

|**Register**<br>**Name**|**Address**<br>**(hex)**|**bit 7**|**bit 6**|**bit 5**|**bit 4**|**bit 3**|**bit 2**|**bit 1**|**bit 0**|**POR/RST**<br>**value**|
|---|---|---|---|---|---|---|---|---|---|---|
|IODIRA|00|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IODIRB|01|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IPOLA|02|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|IPOLB|03|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|GPINTENA|04|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|GPINTENB|05|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|GPPUA|0C|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|GPPUB|0D|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|GPIOA|12|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|GPIOB|13|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|OLATA|14|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|
|OLATB|15|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|



DS20001952E-page 16 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 17 -->

**MCP23017/MCP23S17** 

## **3.5 Configuration and Control Registers** 

There are 21 registers associated with the MCP23X17, as shown in Tables 3-4 and 3-5. The two tables show the register mapping with the two BANK bit values. Ten registers are associated with PORTA and ten are 

associated with PORTB. One register (IOCON) is shared between the two ports. The PORTA registers are identical to the PORTB registers, therefore, they will be referred to without differentiating between the port designation (i.e., they will not have the “A” or “B” designator assigned) in the register tables. 

**TABLE 3-4: CONTROL REGISTER SUMMARY (IOCON.BANK = 1)** 

|**Register**<br>**Name**|**Address**<br>**(hex)**|**bit 7**|**bit 6**|**bit 5**|**bit 4**|**bit 3**|**bit 2**|**bit 1**|**bit 0**|**POR/RST**<br>**value**|
|---|---|---|---|---|---|---|---|---|---|---|
|IODIRA|00|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IPOLA|01|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|GPINTENA|02|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|DEFVALA|03|DEF7|DEF6|DEF5|DEF4|DEF3|DEF2|DEF1|DEF0|0000 0000|
|INTCONA|04|IOC7|IOC6|IOC5|IOC4|IOC3|IOC2|IOC1|IOC0|0000 0000|
|IOCON|05|BANK|MIRROR|SEQOP|DISSLW|HAEN|ODR|INTPOL|—|0000 0000|
|GPPUA|06|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|INTFA|07|INT7|INT6|INT5|INT4|INT3|INT2|INT1|INTO|0000 0000|
|INTCAPA|08|ICP7|ICP6|ICP5|ICP4|ICP3|ICP2|ICP1|ICP0|0000 0000|
|GPIOA|09|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|OLATA|0A|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|
|IODIRB|10|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IPOLB|11|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|GPINTENB|12|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|DEFVALB|13|DEF7|DEF6|DEF5|DEF4|DEF3|DEF2|DEF1|DEF0|0000 0000|
|INTCONB|14|IOC7|IOC6|IOC5|IOC4|IOC3|IOC2|IOC1|IOC0|0000 0000|
|IOCON|15|BANK|MIRROR|SEQOP|DISSLW|HAEN|ODR|INTPOL|—|0000 0000|
|GPPUB|16|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|INTFB|17|INT7|INT6|INT5|INT4|INT3|INT2|INT1|INTO|0000 0000|
|INTCAPB|18|ICP7|ICP6|ICP5|ICP4|ICP3|ICP2|ICP1|ICP0|0000 0000|
|GPIOB|19|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|OLATB|1A|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|



### **TABLE 3-5: CONTROL REGISTER SUMMARY (IOCON.BANK = 0)** 

|**Register**<br>**Name**|**Address**<br>**(hex)**|**bit 7**|**bit 6**|**bit 5**|**bit 4**|**bit 3**|**bit 2**|**bit 1**|**bit 0**|**POR/RST**<br>**value**|
|---|---|---|---|---|---|---|---|---|---|---|
|IODIRA|00|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IODIRB|01|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|1111 1111|
|IPOLA|02|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|IPOLB|03|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|0000 0000|
|GPINTENA|04|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|GPINTENB|05|GPINT7|GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|0000 0000|
|DEFVALA|06|DEF7|DEF6|DEF5|DEF4|DEF3|DEF2|DEF1|DEF0|0000 0000|
|DEFVALB|07|DEF7|DEF6|DEF5|DEF4|DEF3|DEF2|DEF1|DEF0|0000 0000|
|INTCONA|08|IOC7|IOC6|IOC5|IOC4|IOC3|IOC2|IOC1|IOC0|0000 0000|
|INTCONB|09|IOC7|IOC6|IOC5|IOC4|IOC3|IOC2|IOC1|IOC0|0000 0000|
|IOCON|0A|BANK|MIRROR|SEQOP|DISSLW|HAEN|ODR|INTPOL|—|0000 0000|
|IOCON|0B|BANK|MIRROR|SEQOP|DISSLW|HAEN|ODR|INTPOL|—|0000 0000|
|GPPUA|0C|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|
|GPPUB|0D|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|0000 0000|



DS20001952E-page 17 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 18 -->

# **MCP23017/MCP23S17** 

|**TABLE 3-5**<br>**Register**<br>**Name**|**:**<br>**CON**<br>**Address**<br>**(hex)**|**TROL R**<br>**bit 7**|**EGISTE**<br>**bit 6**|**R SUMMA**<br>**bit 5**|**RY(IOC**<br>**bit 4**|**ON.BAN**<br>**bit 3**|**K =0) (C**<br>**bit 2**|**ONTINUE**<br>**bit 1**|**D)**<br>**bit 0**|**POR/RST**<br>**value**|
|---|---|---|---|---|---|---|---|---|---|---|
|INTFA|0E|INT7|INT6|INT5|INT4|INT3|INT2|INT1|INTO|0000 0000|
|INTFB|0F|INT7|INT6|INT5|INT4|INT3|INT2|INT1|INTO|0000 0000|
|INTCAPA|10|ICP7|ICP6|ICP5|ICP4|ICP3|ICP2|ICP1|ICP0|0000 0000|
|INTCAPB|11|ICP7|ICP6|ICP5|ICP4|ICP3|ICP2|ICP1|ICP0|0000 0000|
|GPIOA|12|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|GPIOB|13|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|0000 0000|
|OLATA|14|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|
|OLATB|15|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|0000 0000|



### 3.5.1 I/O DIRECTION REGISTER 

Controls the direction of the data I/O. 

When a bit is set, the corresponding pin becomes an input. When a bit is clear, the corresponding pin becomes an output. 

### **IODIR: I/O DIRECTION REGISTER (ADDR 0x00)** 

|R/W-1|R/W-1|R/W-1|R/W-1|R/W-1|R/W-1|R/W-1|R/W-1|
|---|---|---|---|---|---|---|---|
|IO7|IO6|IO5|IO4|IO3|IO2|IO1|IO0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimple|mented bit, re|ad as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unk|nown|



bit 7-0 **IO<7:0>:** Controls the direction of data I/O <7:0> 

- 1 = Pin is configured as an input. 

- 0 = Pin is configured as an output. 

**Note:** For **MCP23017** , IO7 must be set via I<sup>2</sup> C interface to "0" (output). 

### 3.5.2 INPUT POLARITY REGISTER 

This register allows the user to configure the polarity on the corresponding GPIO port bits. 

If a bit is set, the corresponding GPIO register bit will reflect the inverted value on the pin. 

### **REGISTER 3-1: IPOL: INPUT POLARITY PORT REGISTER (ADDR 0x01)** 

|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|---|
|IP7|IP6|IP5|IP4|IP3|IP2|IP1|IP0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unk|nown|



bit 7-0 **IP<7:0>:** Controls the polarity inversion of the input pins <7:0> 

- 1 = GPIO register bit reflects the opposite logic state of the input pin. 

- 0 = GPIO register bit reflects the same logic state of the input pin. 

DS20001952E-page 18 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 19 -->

**MCP23017/MCP23S17** 

# 3.5.3 INTERRUPT-ON-CHANGE CONTROL REGISTER 

The GPINTEN register controls the interrupt-on-change feature for each pin. 

If a bit is set, the corresponding pin is enabled for interrupt-on-change. The DEFVAL and INTCON registers must also be configured if any pins are enabled for interrupt-on-change. 

# **REGISTER 3-2:** 

# **GPINTEN: INTERRUPT-ON-CHANGE PINS (ADDR 0x02) (Note 1)** 

|R/W-0<br>R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|
|GPINT7<br>GPINT6|GPINT5|GPINT4|GPINT3|GPINT2|GPINT1|GPINT0|
|bit 7||||||bit 0|
|**Legend:**|||||||
|R = Readable bit|W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR|‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unkn|own|



bit 7-0 **GPINT<7:0>:** General purpose I/O interrupt-on-change bits <7:0> 

   - 1 = Enables GPIO input pin for interrupt-on-change event. 

   - 0 = Disables GPIO input pin for interrupt-on-change event. 

- **Note 1:** Refer to INTCON. 

# 3.5.4 DEFAULT COMPARE REGISTER FOR INTERRUPT-ON-CHANGE 

The default comparison value is configured in the DEFVAL register. If enabled (via GPINTEN and INTCON) to compare against the DEFVAL register, an opposite value on the associated pin will cause an interrupt to occur. 

# **REGISTER 3-3: DEFVAL: DEFAULT VALUE REGISTER (ADDR 0x03)** 

|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|---|
|DEF7|DEF6|DEF5|DEF4|DEF3|DEF2|DEF1|DEF0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unkn|own|



bit 7-0 **DEF<7:0>:** Sets the compare value for pins configured for interrupt-on-change from defaults <7:0> **(Note 1)** 

If the associated pin level is the opposite from the register bit, an interrupt occurs. **(Note 2)** 

- **Note 1:** Refer to INTCON. 

   - **2:** Refer to INTCON and GPINTEN. 

DS20001952E-page 19 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 20 -->

**MCP23017/MCP23S17** 

# 3.5.5 INTERRUPT CONTROL REGISTER 

The INTCON register controls how the associated pin value is compared for the interrupt-on-change feature. If a bit is set, the corresponding I/O pin is compared against the associated bit in the DEFVAL register. If a bit value is clear, the corresponding I/O pin is compared against the previous value. 

# **REGISTER 3-4: INTCON: INTERRUPT-ON-CHANGE CONTROL REGISTER (ADDR 0x04) (Note 1)** 

|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|---|
|IOC7|IOC6|IOC5|IOC4|IOC3|IOC2|IOC1|IOC0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unk|nown|



bit 7-0 **IOC<7:0>:** Controls how the associated pin value is compared for interrupt-on-change <7:0> 1 = Pin value is compared against the associated bit in the DEFVAL register. 

0 = Pin value is compared against the previous pin value. 

## **Note 1:** Refer to INTCON and GPINTEN. 

# 3.5.6 CONFIGURATION REGISTER 

The IOCON register contains several bits for configuring the device: 

The BANK bit changes how the registers are mapped (see Tables 3-4 and 3-5 for more details). 

- If BANK = 1, the registers associated with each port are segregated. Registers associated with PORTA are mapped from address 00h - 0Ah and registers associated with PORTB are mapped from 10h - 1Ah. 

- If BANK = 0, the A/B registers are paired. For example, IODIRA is mapped to address 00h and IODIRB is mapped to the next address (address 01h). The mapping for all registers is from 00h -15h. 

It is important to take care when changing the BANK bit as the address mapping changes after the byte is clocked into the device. The address pointer may point to an invalid location after the bit is modified. 

For example, if the device is configured to automatically increment its internal Address Pointer, the following scenario would occur: 

- BANK = 0 

- Write 80h to address 0Ah (IOCON) to set the BANK bit 

- Once the write completes, the internal address now points to 0Bh which is an invalid address when the BANK bit is set. 

For this reason, when changing the BANK bit, it is advised to only perform byte writes to this register. The **MIRROR** bit controls how the INTA and INTB pins function with respect to each other. 

- When MIRROR = 1, the INTn pins are functionally OR’ed so that an interrupt on either port will cause both pins to activate. 

- When MIRROR = 0, the INT pins are separated. Interrupt conditions on a port will cause its respective INT pin to activate. 

The Sequential Operation ( **SEQOP** ) controls the incrementing function of the Address Pointer. If the address pointer is disabled, the Address Pointer does not automatically increment after each byte is clocked during a serial transfer. This feature is useful when it is desired to continuously poll (read) or modify (write) a register. 

The Slew Rate ( **DISSLW** ) bit controls the slew rate function on the SDA pin. If enabled, the SDA slew rate will be controlled when driving from a high to low. 

The Hardware Address Enable ( **HAEN** ) bit enables/disables hardware addressing on the MCP23S17 only. The address pins (A2, A1 and A0) must be externally biased, regardless of the HAEN bit value. 

If enabled (HAEN = 1), the device’s hardware address matches the address pins. 

If disabled (HAEN = 0), the device’s hardware address is A2 = A1 = A0 = 0. 

DS20001952E-page 20 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 21 -->

**MCP23017/MCP23S17** 

The Open-Drain ( **ODR** ) control bit enables/disables the INT pin for open-drain configuration. Setting this bit overrides the INTPOL bit. 

The Interrupt Polarity ( **INTPOL** ) sets the polarity of the INT pin. This bit is functional only when the ODR bit is cleared, configuring the INT pin as active push-pull. 

**REGISTER 3-5:** 

# **IOCON: I/O EXPANDER CONFIGURATION REGISTER (ADDR 0x05)** 

|R/W-0<br>BANK|R/W-0<br>R/W-0<br>R/W-0<br>R/W-0<br>R/W-0<br>MIRROR<br>SEQOP<br>DISSLW<br>HAEN<br>ODR|R/W-0<br>U-0<br>INTPOL<br>—|
|---|---|---|
|bit 7||bit 0|
|**Legend:**|||
|R = Readabl|e bit<br>W = Writable bit<br>U = Unimplemented bit, read|as ‘0’|
|-n = Value at|POR<br>‘1’ = Bit is set<br>‘0’ = Bit is cleared|x = Bit is unknown|
|bit 7|**BANK:**Controls how the registers are addressed<br>1= The registers associated with each port are separated into different b<br>0= The registers are in the same bank (addresses are sequential).|anks.|
|bit 6|**MIRROR:**INT Pins Mirror bit<br>1= The INT pins are internally connected<br>0= The INT pins are not connected. INTA is associated with PORTA and<br>PORTB|INTB is associated with|
|bit 5|**SEQOP:**Sequential Operation mode bit<br>1= Sequential operation disabled, address pointer does not increment.<br>0= Sequential operation enabled, address pointer increments.||
|bit 4|**DISSLW:**Slew Rate control bit for SDA output<br>1= Slew rate disabled<br>0= Slew rate enabled||
|bit 3|**HAEN:**Hardware Address Enable bit (**MCP23S17**only)**(Note 1)**<br>1= Enables the MCP23S17 address pins.<br>0= Disables the MCP23S17 address pins.||
|bit 2|**ODR:**Configures the INT pin as an open-drain output<br>1= Open-drain output (overrides the INTPOL bit.)<br>0= Active driver output (INTPOL bit sets the polarity.)||
|bit 1|**INTPOL:**This bit sets the polarity of the INT output pin<br>1= Active-high<br>0= Active-low||
|bit 0|**Unimplemented:**Read as ‘0’||



**Note 1:** Address pins are always enabled on the MCP23017. 

DS20001952E-page 21 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 22 -->

# **MCP23017/MCP23S17** 

### 3.5.7 PULL-UP RESISTOR CONFIGURATION REGISTER 

The GPPU register controls the pull-up resistors for the port pins. If a bit is set and the corresponding pin is configured as an input, the corresponding port pin is internally pulled up with a 100 k resistor. 

### **REGISTER 3-6: GPPU: GPIO PULL-UP RESISTOR REGISTER (ADDR 0x06)** 

|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|---|
|PU7|PU6|PU5|PU4|PU3|PU2|PU1|PU0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unk|nown|



bit 7-0 **PU<7:0>** Controls the weak pull-up resistors on each pin (when configured as an input) 1 = Pull-up enabled 0 = Pull-up disabled 

### 3.5.8 INTERRUPT FLAG REGISTER 

The INTF register reflects the interrupt condition on the port pins of any pin that is enabled for interrupts via the GPINTEN register. A set bit indicates that the associated pin caused the interrupt. 

This register is read-only. Writes to this register will be ignored. 

### **REGISTER 3-7: INTF: INTERRUPT FLAG REGISTER (ADDR 0x07)** 

|R-0|R-0|R-0|R-0|R-0|R-0|R-0|R-0|
|---|---|---|---|---|---|---|---|
|INT7|INT6|INT5|INT4|INT3|INT2|INT1|INT0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, re|ad as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unkn|own|



- bit 7-0 **INT<7:0>:** Reflects the interrupt condition on the port. It reflects the change only if interrupts are enabled per GPINTEN<7:0>. 

   - 1 = Pin caused interrupt. 

   - 0 = Interrupt not pending 

DS20001952E-page 22 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 23 -->

**MCP23017/MCP23S17** 

### 3.5.9 INTERRUPT CAPTURED REGISTER 

The INTCAP register captures the GPIO port value at the time the interrupt occurred. The register is read-only and is updated only when an interrupt occurs. The register remains unchanged until the interrupt is cleared via a read of INTCAP or GPIO. 

**REGISTER 3-8: INTCAP: INTERRUPT CAPTURED VALUE FOR PORT REGISTER (ADDR 0x08)** 

|R-x|R-x|R-x|R-x|R-x|R-x|R-x|R-x|
|---|---|---|---|---|---|---|---|
|ICP7|ICP6|ICP5|ICP4|ICP3|ICP2|ICP1|ICP0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, re|ad as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unkn|own|



bit 7-0 **ICP<7:0>:** Reflects the logic level on the port pins at the time of interrupt due to pin change <7:0> 

- 1 = Logic-high 0 = Logic-low 

### 3.5.10 PORT REGISTER 

The GPIO register reflects the value on the port. Reading from this register reads the port. Writing to this register modifies the Output Latch (OLAT) register. 

### **REGISTER 3-9: GPIO: GENERAL PURPOSE I/O PORT REGISTER (ADDR 0x09)** 

|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|---|
|GP7|GP6|GP5|GP4|GP3|GP2|GP1|GP0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unk|nown|



bit 7-0 **GP<7:0>:** Reflects the logic level on the pins <7:0> 

1 = Logic-high 0 = Logic-low 

DS20001952E-page 23 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 24 -->

**MCP23017/MCP23S17** 

### 3.5.11 OUTPUT LATCH REGISTER (OLAT) 

The OLAT register provides access to the output latches. A read from this register results in a read of the OLAT and not the port itself. A write to this register modifies the output latches that modifies the pins configured as outputs. 

### **REGISTER 3-10: OLAT: OUTPUT LATCH REGISTER 0 (ADDR 0x0A)** 

|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|R/W-0|
|---|---|---|---|---|---|---|---|
|OL7|OL6|OL5|OL4|OL3|OL2|OL1|OL0|
|bit 7|||||||bit 0|
|**Legend:**||||||||
|R = Readable bit||W = Writable bit||U = Unimplem|ented bit, rea|d as ‘0’||
|-n = Value at POR||‘1’ = Bit is set||‘0’ = Bit is cle|ared|x = Bit is unk|nown|



bit 7-0 **OL<7:0>:** Reflects the logic level on the output latch <7:0> 

1 = Logic-high 

0 = Logic-low 

## **3.6 Interrupt Logic** 

If enabled, MCP23X17 activates the INTn interrupt output when one of the port pins changes state or when a pin does not match the preconfigured default. Each pin is individually configurable as follows: 

- Enable/disable interrupt via GPINTEN. 

- Can interrupt on either pin change or change from default as configured in DEFVAL. 

Both conditions are referred to as Interrupt-on-Change (IOC). 

The interrupt control module uses the following registers/bits: 

- IOCON.MIRROR – controls if the two interrupt pins mirror each other. 

- GPINTEN – Interrupt enable register. 

- INTCON – controls the source for the IOC. 

- DEFVAL – contains the register default for IOC operation. 

### 3.6.1 INTA AND INTB 

There are two interrupt pins: INTA and INTB. By default, INTA is associated with GPAn pins (PORTA) and INTB is associated with GPBn pins (PORTB). Each port has an independent signal which is cleared if its associated GPIO or INTCAP register is read. 

If IOCON.MIRROR = 1, the internal signals are OR’ed together and routed to the INTn pads. In this case, the interrupt will only be cleared if the associated GPIO or INTCAP is read (see Table 3-6). 

**TABLE 3-6: INTERRUPT OPERATION** **<u>(IOCON.MIRROR = 1)</u>** 

|**Interrupt**<br>**Condition**|**Read PORTn**<sup>**(1)**</sup>|**Interrupt**<br>**Result**|
|---|---|---|
|GPIOA|PORTA|Clear|
||PORTB|Unchanged|
|GPIOB|PORTA|Unchanged|
||PORTB|Clear|
||PORTA|Unchanged|
|GPIOA and|PORTB|Unchanged|
|GPIOB|Both PORTA and<br>PORTB|Clear|



**Note 1:** PORTn = GPIOn or INTCAPn 

### 3.6.2 IOC FROM PIN CHANGE 

If enabled, MCP23X17 generates an interrupt if a mismatch condition exists between the current port value and the previous port value. Only IOC-enabled pins will be compared. Refer to Registers 3-2 and 3-4. 

### 3.6.3 IOC FROM REGISTER DEFAULT 

### 3.6.1.1 Mirroring the INT pins 

Additionally, the INTn pins can be configured to mirror each other so that any interrupt will cause both pins to go active. This is controlled via IOCON.MIRROR. 

If enabled, MCP23X17 generates an interrupt if a mismatch occurs between the DEFVAL register and the port. Only IOC enabled pins are compared. Refer to Registers 3-2, 3-3 and 3-4. 

If IOCON.MIRROR = 0, the internal signals are routed independently to the INTA and INTB pads. 

DS20001952E-page 24 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 25 -->

# **MCP23017/MCP23S17** 

#### 3.6.4 INTERRUPT OPERATION 

The INTn interrupt output can be configured as active-low, active-high or open-drain via the IOCON register. 

Only those pins that are configured as an input (IODIR register) with Interrupt-On-Change (IOC) enabled (IOINTEN register) can cause an interrupt. Pins defined as an output have no effect on the interrupt output pin. 

Input change activity on a port input pin that is enabled for IOC generates an internal device interrupt and the device <mark>capt</mark> ures the value of the port and copies it into INTCAP. The interrupt remains active until the INTCAP or GPIO register is read. Writing to these registers does not affect the interrupt. The interrupt condition is cleared after the LSb of the data is clocked out during a read command of GPIO or INTCAP. 

The first interrupt event causes the port contents to be copied into the INTCAP register. Subsequent interrupt conditions on the port will not cause an interrupt to occur as long as the interrupt is not cleared by a read of INTCAP or GPIO. 

**Note:** The value in INTCAP can be lost if GPIO is read before INTCAP while another IOC is pending. After reading GPIO, the interrupt will clear and then set due to the pending IOC, causing the INTCAP register to update. 

#### 3.6.5 INTERRUPT CONDITIONS 

There are two possible configurations that cause interrupts (configured via INTCON): 

1. Pins configured for **interrupt-on-pin change** will cause an interrupt to occur if a pin changes to the opposite state. The default state is reset after an interrupt occurs and after clearing the interrupt condition (i.e., after reading GPIO or INTCAP). For example, an interrupt occurs by an input changing from ‘1’ to ‘0’. The new initial state for the pin is a logic ‘0’ after the interrupt is cleared. 



<!-- Start of picture text -->
GPx<br>INT ACTIVE ACTIVE<br>Port value Read GPIO Port value<br>is captured or INTCAP is captured<br>into INTCAP into INTCAP<br><!-- End of picture text -->

**_FIGURE 3-8:_** _Interrupt-on-Pin Change._ 



<!-- Start of picture text -->
DEFVAL REGISTER<br>GPx<7:0> 7 6 5 4 3 2 1 0<br>X X X X X 0 X X<br>GP2<br>Pin<br>INT ACTIVE ACTIVE<br>Pin<br>Port value<br>is captured Read GPIO<br>into INTCAP or INTCAP<br>(INT clears only if interrupt<br>condition does not exist.)<br><!-- End of picture text -->

**_FIGURE 3-9:_** _Interrupt-on-Change from Register Default._ 

2. Pins configured for **interrupt-on-change from register value** will cause an interrupt to occur if the corresponding input pin differs from the register bit. The interrupt condition will remain as long as the condition exists, regardless if the INTCAP or GPIO is read. 

See Figures 3-8 and 3-9 for more information on interrupt operations. 

DS20001952E-page 25 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 26 -->

**MCP23017/MCP23S17** 

## **4.0 PACKAGING INFORMATION** 

### **4.1 Package Marking Information** 

##### 28-Lead QFN 



Example: 



<!-- Start of picture text -->
23017<br>E/ML e3<br>1628256<br><!-- End of picture text -->

##### 28-Lead SOIC 



Example: 



<!-- Start of picture text -->
MCP23017-E/SO e3<br>1628256<br><!-- End of picture text -->

##### 28-Lead SPDIP 



<!-- Start of picture text -->
XXXXXXXXXXXXXXXXX<br>XXXXXXXXXXXXXXXXX<br>YYWWNN<br><!-- End of picture text -->

##### Example: 



<!-- Start of picture text -->
MCP23017-E/SP e3<br>1628256<br><!-- End of picture text -->

##### 28-Lead SSOP 

##### Example: 



<!-- Start of picture text -->
XXXXXXXXXXXX MCP23017<br>XXXXXXXXXXXX E/SS e3<br>YYWWNNN 1628256<br><!-- End of picture text -->



<!-- Start of picture text -->
Legend: XX...X Product Code or Customer-specific information<br>Y Year code (last digit of calendar year)<br>YY Year code (last 2 digits of calendar year)<br>WW Week code (week of January 1 is week ‘01’)<br>NNN Alphanumeric traceability code<br>e3 Pb-free JEDEC designator for Matte Tin (Sn)<br>* This package is Pb-free. The Pb-free JEDEC designator ( e3 )<br>can be found on the outer packaging for this package.<br>Note : In the event the full Microchip part number cannot be marked on one line,<br>it will be carried over to the next line, thus limiting the number of available<br>characters for customer-specific information. Package may or not include the<br>corporate logo.<br><!-- End of picture text -->

DS20001952E-page 26 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 27 -->

**MCP23017/MCP23S17** 

### **28-Lead Very-Thin Quad Flat No-Lead Package (ML) - 6x6x1.0 mm Body [VQFN] With 4.10x4.10mm Exposed Pad** 

**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 



<!-- Start of picture text -->
28X<br>0.08 C<br>0.10 C<br>D A<br>B<br>NOTE1<br>28<br>1<br>2<br>E<br>(DATUM B)<br>(DATUM A)<br>2X<br>0.10 C<br>2X TOP VIEW<br>A1<br>0.10 C<br>(A3)<br>0.10 C A B<br>D2 A<br>SEATING<br>C<br>PLANE<br>SIDE VIEW<br>0.10 C A B<br>E2<br>2<br>1<br>K<br>28<br>L<br>28X b<br>NOTE 1 e 0.10 C A B<br>0.05 C<br>BOTTOM VIEW<br><!-- End of picture text -->

Microchip Technology Drawing C04-00105-ML Rev D Sheet 1 of 2 

DS20001952E-page 27 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 28 -->

**MCP23017/MCP23S17** 

# **28-Lead Very-Thin Quad Flat No-Lead Package (ML) - 6x6x1.0 mm Body [VQFN] With 4.10x4.10mm Exposed Pad** 

**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 



||Units||MILLIMETERS||
|---|---|---|---|---|
|Dimen|sion Limits|MIN|NOM|MAX|
|Number of Pins|N||28||
|Pitch|e||0.65 BSC||
|Overall Height|A|0.80|0.90|1.00|
|Standoff|A1|0.00|0.02|0.05|
|Terminal Thickness|A3||0.20 REF||
|Overall Width|E||6.00 BSC||
|Exposed Pad Width|E2|4.00|4.10|4.20|
|Overall Length|D||6.00 BSC||
|Exposed Pad Length|D2|4.00|4.10|4.20|
|Terminal Width|b|0.23|0.30|0.35|
|Terminal Length|L|0.50|0.60|0.70|
|Terminal-to-Exposed Pad|K|0.20|-|-|



## **Notes:** 

1. Pin 1 visual index feature may vary, but must be located within the hatched area. 2. Package is saw singulated 3. Dimensioning and tolerancing per ASME Y14.5M. BSC:  Basic Dimension. Theoretically exact value shown without tolerances. 

REF:  Reference Dimension, usually without tolerance, for information purposes only. 

Microchip Technology Drawing C04-00105-ML Rev D Sheet 2 of 2 

DS20001952E-page 28 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 29 -->

**MCP23017/MCP23S17** 

# **28-Lead Very-Thin Quad Flat No-Lead Package (ML) - 6x6x1.0 mm Body [VQFN] With 4.10x4.10mm Exposed Pad** 

**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 



<!-- Start of picture text -->
C1<br>X2<br>EV<br>2 8<br>ØV<br>1<br>2 G2<br>C2 Y2<br>EV<br>G1<br>Y1<br>E X1<br>SILK SCREEN<br><!-- End of picture text -->

# RECOMMENDED LAND PATTERN 

||Units||MILLIMETER|S|
|---|---|---|---|---|
|Dimension|Limits|MIN|NOM|MAX|
|Contact Pitch|E||0.65 BSC||
|Center Pad Width|X2|||4.20|
|Center Pad Length|Y2|||4.20|
|Contact Pad Spacing|C1||5.80||
|Contact Pad Spacing|C2||5.80||
|Contact Pad Width(Xnn)|X1|||0.35|
|Contact Pad Length(Xnn)|Y1|||0.95|
|Contact Pad to Center Pad(X28)|G1|0.33|||
|Contact Pad to Contact Pad(X24)|G2|0.30|||
|Thermal Via Diameter|V||0.30||
|Thermal Via Pitch|EV||1.00||



Notes: 

1. Dimensioning and tolerancing per ASME Y14.5M 

BSC: Basic Dimension. Theoretically exact value shown without tolerances. 

2. For best soldering results, pleease refer to current industry standard IPC-7093. 

Microchip Technology Drawing C04-02105-ML Rev D 

DS20001952E-page 29 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 30 -->

**MCP23017/MCP23S17** 



<!-- Start of picture text -->
Note: For the most current package drawings, please see the Microchip Packaging Specification located at<br>http://www.microchip.com/packaging<br><!-- End of picture text -->

DS20001952E-page 30 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 31 -->

**MCP23017/MCP23S17** 



**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 



DS20001952E-page 31 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 32 -->

**MCP23017/MCP23S17** 



**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 







DS20001952E-page 32 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 33 -->

**MCP23017/MCP23S17** 

# **28-Lead Skinny Plastic Dual In-Line (M3X) - 300 mil Body [SPDIP]** 

**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 



<!-- Start of picture text -->
D<br>N<br>E1<br>1 2<br>(DATUM A)<br>(DATUM B)<br>TOP VIEW<br>A<br>C<br>A A2<br>SEATING<br>PLANE<br>L<br>A1<br>A<br>28X b1<br>e 28X b<br>0.010 C<br>SIDE VIEW<br><!-- End of picture text -->



<!-- Start of picture text -->
E<br>c<br>eB<br>VIEW A-A<br><!-- End of picture text -->

Microchip Technology Drawing  C04-00070 Rev D (M3X) Sheet 1 of 2 

DS20001952E-page 33 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 34 -->

**MCP23017/MCP23S17** 

# **28-Lead Skinny Plastic Dual In-Line (M3X) - 300 mil Body [SPDIP]** 

**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at http://www.microchip.com/packaging 



||Units||INCHES||M|ILLIMETER|S|
|---|---|---|---|---|---|---|---|
|Dimension Li|mits|MIN|NOM|MAX|MIN|NOM|MAX|
|Number of Pins|N||28|||28||
|Pitch|e||.100 BSC|||2.54 BSC||
|Topto SeatingPlane|A|-|-|.200|-|-|5.08|
|Molded Package Thickness|A2|.120|.135|.150|3.05|3.43|3.81|
|Base to SeatingPlane|A1|.015|-|-|0.38|-|-|
|Shoulder to Shoulder Width|E|.290|.310|.335|7.37|7.87|8.51|
|Molded Package Width|E1|.240|.285|.295|6.10|7.24|7.49|
|Overall Length|D|1.345|1.365|1.400|34.16|34.67|35.56|
|Tipto SeatingPlane|L|.110|.130|.150|2.79|3.30|3.81|
|Lead Thickness|c|.008|.010|.015|0.203|0.254|0.381|
|Upper Lead Width|b1|.045|.050|.070|1.14|1.27|1.78|
|Lower Lead Width|b|.014|.018|.022|0.36|0.46|0.56|
|Overall Row Spacing<br>§|eB|-|-|.430|-|-|10.92|



Notes: 

1. The Pin 1 visual index feature may vary, but it must be located within the hatched area. 

2. § Significant Characteristic 

3. Dimensions D and E do not include mold flash or protrusions.  Mold flash or protrusions shall not exceed .005" per side. 

4. Dimensioning and tolerancing per ASME Y14.5M 

BSC: Basic Dimension. The theoretically exact value is shown without tolerances. 

Microchip Technology Drawing  C04-00070 Rev D (M3X) Sheet 2 of 2 

DS20001952E-page 34 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 35 -->

**MCP23017/MCP23S17** 

# **���������������������������������������������������������������** 



<!-- Start of picture text -->
����� ��������������������������������������������������������������������������������������������������<br>����������������������������������<br>� �<br>�<br>�<br>���������<br>���������<br>�� �<br>� �<br>�����<br>� ���� � � �<br>��������<br>�<br>��<br>� � ��<br>�������<br>�����<br>���<br>���� � �<br>���������<br>�<br>� �<br>����<br>��������<br><!-- End of picture text -->

�������������������������������������������������������� 

DS20001952E-page 35 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 36 -->

**MCP23017/MCP23S17** 

# **���������������������������������������������������������������** 

**�����** �������������������������������������������������������������������������������������������������� ���������������������������������� 



||�����||�����������||
|---|---|---|---|---|
|��������|���������|���|���|���|
|��������������|�||��||
|�����|�||��������||
|��������������|�|�|�|����|
|������������������������|��|����|����|����|
|��������|��|����|�|�|
|�������������|�|����|����|����|
|��������������������|��|����|����|����|
|��������������|�|����|�����|�����|
|�����������|�|����|����|����|
|���������|��||��������||
|��������������|�|����|�|����|
|����������||��|��|��|
|����������|�|����|�|����|



## Notes: 

- ������������������������������������������������������������������������������������ 

- ������������������������������������������������������������������������������ 

   - ��������������������������������������������� 

- ����������������������������������������������� 

      - ������������������������������������������������������������������������� 

      - ����������������������������������������������������������������������������������� 

         - �������������������������������������������������������� 

DS20001952E-page 36 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 37 -->

**MCP23017/MCP23S17** 

## **���������������������������������������������������������������** 

**�����** �������������������������������������������������������������������������������������������������� ���������������������������������� 



<!-- Start of picture text -->
��<br>��<br>�����������<br>�<br>��<br>��<br>��<br>�<br><!-- End of picture text -->

## ������������������������ 

||�����||����������|�|
|---|---|---|---|---|
|����������|�������|���|���|���|
|�������������|�||��������||
|�������������������|�||����||
|�����������������������|��|||����|
|������������������������|��|||����|
|�������������������������������|��|����|||



������ 

- �� �������������������������������������������� ������������������������������������������������������������������������� 

- �� ��������������������������������������������������������������������������������������������������������� �������������� 

������������������������������������������� 

DS20001952E-page 37 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 38 -->

**MCP23017/MCP23S17** 

### **NOTES:** 

DS20001952E-page 38 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 39 -->

**MCP23017/MCP23S17** 

# **APPENDIX A: REVISION HISTORY** 

## **Revision E (July 2026)** 

- Updated **Figure 3-2** . 

- Small changes to document layout. 

## **Revision D (June 2022)** 

- Updated description in **Section “Features”** . 

- Updated **Table 2-1** . 

- Updated drawings for MCP23017 in **Section “Package Types”** . 

- Updated **Section 3.5.1 “I/O Direction Register”** . 

- Updated **Section 4.1 “Package Marking Information”** . 

- Updated **Section “Product Identification System”** , with Automotive Qualified devices. 

- Minor text and format changes throughout. 

## **Revision C (July 2016)** 

- Added ESD data to **Section 1.0 “Electrical Characteristics”** . 

- Updated **Table 2-1** . 

- Updated package outline drawings. 

- Minor typographical errors 

## **Revision B (February 2007)** 

- Changed Byte and Sequential Read in **Figure 1-1** from “R” to “W”. 

- Table 2-4, Parameter No. 51 and 53: Changed from 450 to 600 and 500 to 600, respectively. 

- Added disclaimers to package outline drawings. 

- Updated package outline drawings. 

## **Revision A (June 2005)** 

- Original release of this document. 

DS20001952E-page 39 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 40 -->

**MCP23017/MCP23S17** 

## **PRODUCT IDENTIFICATION SYSTEM** 

To order or obtain information, e.g., on pricing or delivery, refer to the factory or the listed sales office. 

|**PART NO.**<br>**Device**|**[X**<br> **]**<sup>**(1)**</sup><br>**Tape and Reel**<br>**Option**|**-**<br>**X**<br>**/XX**<br>**Package**<br>**Temperature**<br>**Range**<br>**XX**<br>**X**<br>**Qualification**|**Examples:**<br>a)<br>MCP23017-E/ML:<br>b)<br>MCP23017T-E/ML:|Extended Temperature,<br>28-Lead QFN package<br>Tape<br>and<br>Reel,<br>Extended temperature,|
|---|---|---|---|---|
|||||28-Lead QFN package|
|**Device:**|MCP23017:<br>MCP23S17:|16-Bit I/O Expander with I<sup>2</sup>C Interface<br>16-Bit I/O Expander with SPI Interface|c)<br>MCP23017-E/SP:<br>d)<br>MCP23017-E/SO:|Extended Temperature ,<br>28-Lead SPDIP package<br>Extended Temperature,<br>28-Lead SOIC package|
|**Tape and Reel**<br>**Option:**|T<br>=<br>Blank<br>=|Tape and Reel<sup>(1)</sup><br>Tube|e)<br>MCP23017T-E/SO:|<br>Tape and Reel,<br>Extended Temperature,<br>28-Lead SOIC package|
|**Temperature**<br>**Range:**|E<br>=<br>* While thes<br>range, the d<br>temperature<br>**Characteris**|–40C to +125C (Extended) *<br>e devices are only offered in the “E” temperature<br>evice will operate at different voltages and<br>s as identified in**Section 1.0 “Electrical**<br>**tics”**|f)<br>MCP23017-E/SS:<br>g)<br>MCP23017T-E/SS:<br>h)<br>MCP23017-E/SSVAO:|Extended Temperature,<br>28-Lead SSOP package<br>Tape and Reel,<br>Extended Temperature,<br>28-Lead SSOP package<br>Extended<br>Temperature,<br>28-Lead SSOP package,<br>AEC-Q100<br>Automotive|
|||||Qualified|
|**Package:**|ML<br>=<br>SO<br>=<br>SP<br>=|Plastic Quad Flat, No Lead Package, 6x6 mm<br>Body, QFN, 28-Lead<br>Plastic Small Outline, Wide, 7.50 mm Body,<br>SOIC, 28-Lead<br>Skinny Plastic Dual In-Line, 300 mil Body, SPDIP,<br>|i)<br>MCP23017T-E/SSVAO|: Tape<br>and<br>Reel,<br>Extended<br>Temperature,<br>28-Lead SSOP package,<br>AEC-Q100<br>Automotive<br>Qualified|
||SS<br>=|28-Lead<br>Plastic Shrink Small Outline, 5.30 mm Body,<br>SSOP, 28-Lead|j)<br>MCP23S17-E/ML:<br>k)<br>MCP23S17T-E/ML:|Extended<br>Temperature,<br>28-Lead QFN package<br>Tape<br>and<br>Reel<br> <br>|
|**Qualification:**|<Blank> =<br>VAO<br>=|Standard Part<br>AEC-Q100 Automotive Qualified|l)<br>MCP23S17-E/SP:<br>m)<br>MCP23S17-E/SO:<br>n)<br>MCP23S17T-E/SO:<br>o)<br>MCP23S17-E/SS:|Extended<br>Temperature,<br>28-Lead QFN package<br>Extended<br>Temperature,<br>28-Lead SPDIP package<br>Extended<br>Temperature,<br>28-Lead SOIC package<br>Tape<br>and<br>Reel,<br>Extended<br>Temperature,<br>28-Lead SOIC package<br>Extended<br>Temperature,<br>28-Lead SSOP package|
||||p)<br>MCP23S17T-E/SS:<br>q)<br>MCP23S17-E/SSVAO: <br>r)<br>MCP23S17T-E/SSVAO|<br>Tape<br>and<br>Reel,<br>Extended<br>Temperature,<br>28-Lead SSOP package<br> Extended<br>Temperature,<br>28-Lead SSOP package,<br>AEC-Q100<br>Automotive<br>Qualified<br>: Tape<br>and<br>Reel,<br>Extended<br>Temperature,<br>28-Lead SSOP package,<br>AEC-Q100<br>Automotive<br>Qualified|
||||**Note 1:**<br>Tape and Reel i<br>catalog part num<br>is used for orderi<br>on the device<br>Microchip Sales<br>with the Tape and|dentifier only appears in the<br>ber description. This identifier<br>ng purposes and is not printed<br>package. Check with your<br>Office for package availability<br>Reel option.|



DS20001952E-page 40 

 2005-2026 Microchip Technology Inc. and its subsidiaries 



<!-- page 41 -->

# **Microchip Information** 

## **Trademarks** 

The “Microchip” name and logo, the “M” logo, and other names, logos, and brands are registered and unregistered trademarks of Microchip Technology Incorporated or its affiliates and/or subsidiaries in the United States and/or other countries (“Microchip Trademarks”). Information regarding Microchip Trademarks can be found at https://www.microchip.com/en-us/about/legal-information/microchiptrademarks. 

## **Legal Notice** 

This publication and the information herein may be used only with Microchip products, including to design, test, and integrate Microchip products with your application. Use of this information in any other manner violates these terms. Information regarding device applications is provided only for your convenience and may be superseded by updates. It is your responsibility to ensure that your application meets with your specifications. Contact your local Microchip sales office for additional support or, obtain additional support at www.microchip.com/en-us/support/design-help/client-support-services. 

THIS INFORMATION IS PROVIDED BY MICROCHIP "AS IS". MICROCHIP MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED, WRITTEN OR ORAL, STATUTORY OR OTHERWISE, RELATED TO THE INFORMATION INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE, OR WARRANTIES RELATED TO ITS CONDITION, QUALITY, OR PERFORMANCE. 

IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL, OR CONSEQUENTIAL LOSS, DAMAGE, COST, OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE INFORMATION OR ITS USE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THE INFORMATION OR ITS USE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THE INFORMATION. 

Use of Microchip devices in life support and/or safety applications is entirely at the buyer's risk, and the buyer agrees to defend, indemnify and hold harmless Microchip from any and all damages, claims, suits, or expenses resulting from such use. No licenses are conveyed, implicitly or otherwise, under any Microchip intellectual property rights unless otherwise stated. 

## **Microchip Devices Code Protection Feature** 

Note the following details of the code protection feature on Microchip products: 

- Microchip products meet the specifications contained in their particular Microchip Data Sheet. 

- Microchip believes that its family of products is secure when used in the intended manner, within operating specifications, and under normal conditions. 

- Microchip values and aggressively protects its intellectual property rights. Attempts to breach the code protection features of Microchip product is strictly prohibited and may violate the Digital Millennium Copyright Act. 

- Neither Microchip nor any other semiconductor manufacturer can guarantee the security of its code. Code protection does not mean that we are guaranteeing the product is “unbreakable”. Code protection is constantly evolving. Microchip is committed to continuously improving the code protection features of our products. 

DS20001952E-page 41 

 2005-2026 Microchip Technology Inc. and its subsidiaries 

