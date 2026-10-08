# Midas-Displays-MDOB256064D1Y

*Source: `original/display/Midas-Displays-MDOB256064D1Y.pdf` (19 pages)*

<!-- page 1 -->

Electra House, 32 Southtown Road Great Yarmouth, Norfolk NR31 0DU, England 

Telephone +44 (0)1493 602602 Fax +44 (0)1493 665111 Email:sales@midasdisplays.com www.midasdisplays.com 



|MDOB256064D1Y-YS|256|x 64|OLED Module|
|---|---|---|---|
|||**Specification**||
|Version:    1||**Revision**|Date:25/10/2019|
|1|23/10/2019|First Issue||



|Displa|yFeatures||
|---|---|---|
|Resolution|256 x 64||
|Appearance|Yellow on Black||
|Logic Voltage|3.3V||
|Interface|SPI||
|Module Size|70.00 x 22.00 x 1.71mm||
|OperatingTemperature|-40°C ~ +80°C|BoxQuantity<br>Weight / Display|
|Construction|COB|---<br>---|



* - For full design functionality, please use this specification in conjunction with the SSD1362 specification. (Provided Separately) 

|**Display Accessories**|**Optional Variants**|
|---|---|
|**Part Number**<br>**Description**|**Appearance**<br>**Voltage**|





<!-- page 2 -->

# **General Specification** 

The Features is described as follow: 

- Module dimension: 70.0 x 22.0 x 1.71mm 

- Active area: 51.18 x 12.78mm 

- Dot Matrix: 256 x 64 Dots 

- Pixel Size: 0.18 x 0.18 mm 

- Pixel Pitch: 0.20 x 0.20 mm 

- Display Mode: Passive Matrix 

- Duty: 1/64 Duty 

- Gray Scale: 4 Bits 

- Display Color: Yellow 

- IC: SSD1362 

- Interface: SPI 

- Size: 2.08 inch 

# **Interface Pin Function** 

|**No.**|**Symbol**|<br>**Function**|
|---|---|---|
|1|GND|Reserved pin. It should be connected to ground.|
|2|VCC|<sup>Power supply for panel driving voltage. This is also the most positive power</sup><br>voltage supply pin. It is supplied by external high voltage source.|
|3|D0|These pins are bi-directional data bus connecting to the MCU data bus.<br>Unused pins are recommended to tie LOW.|
|4|D1|When serial interface mode is selected, D0 will be the serial clock input:<br>SCLK; D1 will be the serial data input: SID.|
|5|RES#|This pin is reset signal input.<br>When the pin is pulled LOW, initialization of the chip is executed.<br>Keepthispinpull HIGH duringnormal operation.|
|6|D/C#|This pin is Data/Command control pin connecting to the MCU.<br>When the pin is pulled HIGH, the data at D[1:0] will be interpreted as data.<br>When the pin is pulled LOW, the data at D[1:0] will be transferred to a<br>command register.|
|7|CS#|This pin is the chip select input connecting to the MCU.<br>The chip is enabled for MCU communication only when CS# is pulled LOW<br>(activeLOW).|





<!-- page 3 -->



<!-- Start of picture text -->
19¡ Ó0.2<br>18¡ Ó0.2 POL 0.5¡ Ó0.5<br>14.78 VA 2.11<br>12.78 AA 3.11<br>P2.54*6=15.24 3.38<br>1.5¡ Ó0.5<br>2.5 Max.<br>0.2 Dot pitch 13.4 4.3<br>0.18 Dot size 18 2<br>(2.2)<br>P0.7*23=16.1<br>1.5<br>6<br>2<br>22¡ Ó0.5<br>2.5 ¡4.25 Ó0.5<br>2.1 1.1 ¡0.5 Ó0.5<br>2.0 PAD 1.0 PTH<br>51.18 AA 53.18 VA ¡60.5 Ó0.2<br>256*64  2.08" ¡55.9 Ó0.2 POL<br>4- 4-<br>4.0 PAD 2.5 PTH<br>Component area<br>2<br>0.18 Dot size 0.2 Dot pitch<br>Contour Drawing & Block Diagram<br>1 7.5<br>SCALE 1:30   Detail A<br>¡ Ó0.21.71<br>(16.55)<br>256*64 ¡70 Ó0.5<br>()P2.54*=15.247-1<br>S256(SEG255) S2(SEG128) C64(COM63) C1(COM0) S1(SEG0) S255(SEG127)<br>7 6 5 4 3 2 1<br>The non-specified tolerance of dimension is ¡ Ó0.3 mm .<br>CS# D/C# RES# D1 D0 VCC GND<br>SYMBOLPIN<br>   7 1<br>   7 1<br>1 24<br><!-- End of picture text -->



<!-- page 4 -->

## **Application recommendations** 



Recommended components ： 

C1 ： 4.7uF 

### **Note** 

(1) The capacitor value is recommended value. Select appropriate value against module application. 

# **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Supply Voltage|VCC|1.65|5.5|V|1,2|
|Operating Temperature|TOP|-40|+80|°C|—|
|Storage Temperature|TSTG|-40|+85|°C|—|



Note 1: All the above voltages are on the basis of “VSS = 0V”. 

Note 2: When this module is used beyond the above absolute maximum ratings, permanent breakage of the module may occur. Also, for normal operations, it is desirable to use this module under the conditions according to Section 6.“Optics & Electrical Characteristics”. If this module is used beyond these conditions, malfunctioning of the module can occur and the reliability of the module may deteriorate. 



<!-- page 5 -->

# **Electrical Characteristics** 

## **DC Electrical Characteristics** 

|**Item**|**Symbol**|**Condition**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Supply Voltage|VCC|－|2.8|3.3|5.2|V|
|Input High Volt.|VIH|－|0.8×VCC|－|VCC|V|
|Input Low Volt.|VIL|－|0|－|0.2×VCC|V|
|Output High Volt.|VOH|－|0.9×VCC|－|VCC|V|
|Output Low Volt.|VOL|－|0|－|0.1×VCC|V|
|50% Check Board operating<br>Current|ICC|VCC=3.3V|－|90|135|mA|





<!-- page 6 -->

### **Initial code** 

void Initial_SSD1362() { LCM_CS1=0; 

Write_command(0XFD); //Set Command Lock Write_command(0X12); //(12H=Unlock,16H=Lock) 

Write_command(0XAE); //Display OFF(Sleep Mode) 

Write_command(0X15); //Set column Address Write_command(0X00); //Start column Address Write_command(0X7F); //End column Address 

Write_command(0X75); //Set Row Address Write_command(0X00); //Start Row Address Write_command(0X3F); //End Row Address 

Write_command(0X81); //Set contrast Write_command(0x2f); 

Write_command(0XA0); //Set Remap Write_command(0Xc3); 

Write_command(0XA1); //Set Display Start Line Write_command(0X00); 

Write_command(0XA2); //Set Display Offset Write_command(0X00); 

Write_command(0XA4); //Normal Display 

Write_command(0XA8); //Set Multiplex Ratio Write_command(0X3F); 

Write_command(0XAB); //Set VDD regulator Write_command(0X01); //Regulator Enable 

Write_command(0XAD); //External /Internal IREF Selection Write_command(0X8E); 

Write_command(0XB1); //Set Phase Length Write_command(0X22); 

Write_command(0XB3); //Display clock Divider Write_command(0XA0); 

Write_command(0XB6); //Set Second pre-charge Period Write_command(0X04); 



<!-- page 7 -->

Write_command(0XB9); //Set Linear LUT 

Write_command(0XBc); //Set pre-charge voltage level Write_command(0X10); //0.5*Vcc 

Write_command(0XBD); //Pre-charge voltage capacitor Selection Write_command(0X01); 

Write_command(0XBE); //Set COM deselect voltage level Write_command(0X07); //0.82*Vcc 

Write_command(0XAF); //Display ON } 



<!-- page 8 -->

# **Optical Characteristics** 

|**Item**|**Symbol**|**Condition**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Vi Al|(V)θ|－|160|－|－|deg|
|ew nge|(H)φ|－|160|－|－|deg|
|Contrast Ratio|CR|Dark|2000:1|－|－|－|
|R Ti|T rise|－|－|10|－|μs|
|esponse me|T fall|－|－|10|－|μs|
|Display with 100|% check Boa|rd Brightness|100|120|－|cd/m2|
|CIEx(Yell|ow)|x,y(CIE1931)|0.45|0.47|0.49|－|
|CIEy(Yell|ow)|x,y(CIE1931)|0.48|0.50|0.52|－|



## **OLED Lifetime** 



|**ITEM**|**Conditions**|**Min**|**Typ**|**Remark**|
|---|---|---|---|---|
|Operating<br>Life Time|Ta=25°C<br>/ Initial 50% check board<br>brightness 100cd/ m<sup>2</sup>|50,000 Hrs|-|Note|



Notes: 

1. Life time is defined the amount of time when the luminance has decayed to <50% of the initial value. 

2. This analysis method uses life data obtained under accelerated conditions to extrapolate an estimated probability density function ( _pdf_ ) for the product under normal use conditions. 

3. Screen saving mode will extend OLED lifetime. 



<!-- page 9 -->

# **Reliability** 

#### **<u>Content of Reliability Test</u>** 

##### **Environmental Test** 

|**Test Item**|**Content of Test**|**Test Condition**|**Applicable**<br>**Standard**|
|---|---|---|---|
|High<br>Temperature<br>storage|Endurance test applying the high<br>storage temperature for a long time.|85°C<br>240hrs|——|
|Low<br>Temperature<br>storage|Endurance test applying the low storage<br>temperature for a long time.|<br>-40°C<br>240hrs|——|
|High<br>Temperature<br>Operation|Endurance test applying the electric<br>stress (Voltage & Current) and the<br>thermal stress to the element for a long<br>time.|80°C<br>240hrs|——|
|Low<br>Temperature<br>Operation|Endurance test applying the electric<br>stress under low temperature for a long<br>time.|-40°C<br>240hrs|——|
|High<br>Temperature/<br>Humidity<br>Storage|Endurance test applying the high<br>temperature and high humidity storage<br>for a long time.|60°C,90%RH<br>240hrs|——|
|High<br>Temperature/<br>Humidity<br>Operation|Endurance test applying the high<br>temperature and high humidity<br>Operation for a long time.|60°C,90%RH<br>120hrs|——|
|Temperature|Endurance test applying the low and<br>high temperature cycle.<br>-40°C25°C80°C|-40°C /80°C||
|<br>Cycle||30 cycles|——|
||30min    5min     30min|||
||1cycle|||
|Mechanical Te|st|||
|Vibration test|Endurance test applying the vibration<br>during transportation and using.|Frequency:10~55Hz<br>amplitude:1.5mm<br>Time:0.5hrs/axis|——|
|||Test axis:X,Y,Z||
|Others||||
|Static<br>electricity test|Endurance test applying the electric<br>stress to the finished product housing.|Air Discharge model<br>±4kv,10 times|——|



*** Supply voltage for OLED system =Operating voltage at 25°C 



<!-- page 10 -->

#### **Test and measurement conditions** 

1. All measurements shall not be started until the specimens attain to temperature stability. After the completion of the described reliability test, the samples were left at room temperature for 2 hrs prior to conducting the failure test at 23±5°C; 55±15% RH. 

2. All-pixels on/off exchange is used as operation test pattern. 

3. The degradation of Polarizer are ignored for High Temperature storage, High Temperature/ Humidity Storage, Temperature Cycle 

#### **Evaluation criteria** 

1. The function test is OK. 

2. No observable defects. 

3. Luminance: > 50% of initial value. 

4. Current consumption: within ± 50% of initial value. 

#### **APPENDIX:** 

#### **RESIDUE IMAGE** 

Because the pixels are lighted in different time, the luminance of active pixels may reduce or differ from inactive pixels. Therefore, the residue image will occur. To avoid the residue image, every pixel needs to be lighted up uniformly. 



<!-- page 11 -->

# **Inspection specification Inspection Standard:** 

MIL-STD-105E table normal inspection single sample level II. 

## **Definition** 

- 1 Major defect : The defect that greatly affect the usability of product. 

- 2 Minor defect : The other defects, such as cosmetic defects, etc. Definition of inspection zone: 

|C<br>B<br>A|
|---|



Zone A: Active Area 

Zone B: Viewing Area except Zone A Zone C: Outside Viewing Area 

- Note: As a general rule, visual defects in Zone C are permissible, when it is no trouble of quality and assembly to customer`s product. 

## **Inspection Methods** 

- 1 The general inspection : Under fluorescent light illumination: 750~1500 Lux, about 30cm viewing distance, within 45º viewing angle, under 25±5°C. 

- 2 The luminance and color coordinate inspection : By SR-3 or BM-7 or the equal equipments, in the dark room, under 25±5°C. 

|NO|Item|Criterion|AQL|
|---|---|---|---|
|01|Electrical<br>Testing|1.1 Missing vertical, horizontal segment, segment contrast defect.<br>1.2 Missing character , dot or icon.<br>1.3 Display malfunction.<br>1.4 No function or no display.<br>1.5 Current consumption exceeds product specifications.<br>1.6 OLED viewing angle defect.<br>1.7 Mixed product types.<br>1.8 Contrast defect.|0.65|
|02|Black or<br>white<br>spots on<br>OLED<br>(display<br>only)|2.1 White and black spots on display≦0.25mm, no more than<br>three white or black spots present.<br>2.2 Densely spaced: No more than two spots or lines within 3mm.|2.5|





<!-- page 12 -->

|NO|Item|Criterion|||AQL|
|---|---|---|---|---|---|
||OLED|3.1 Round type :<br>As following<br> <br>||||
||black|drawing<br> <br>SIZE<br>|Acceptable QTY<br>|Zone||
||<br>spots,<br>|Φ=( x + y ) / 2<br>Φ≦0.10|Accept no<br>dense|A+ B,||
||white<br>spots,|0.10＜Φ≦0.20<br>|2|A+ B|2.5|
||<br>contamin|0.20＜Φ≦0.25|1|A+ B||
||ation|0.25＜Φ|0|A+ B||
||(non-display)|||||
|03||3.2 Line type : (As following drawing)||||
|||Length<br>Width|Acceptable<br>Q TY|Zone|2.5|
|||---<br>W≦0.02|Accept no<br>dense|A+B||
|||L≦3.0<br>0.02＜W≦0.03|<br>|A+B||
|||L≦2.5<br>0.03＜W≦0.05|2<br>|A+B||
|||---<br>0.05＜W|As round type|||
|||If bubbles are<br>Size Φ|Acceptable Q TY|Zone||
|||visible, judge<br> <br>Φ≦0.20|Accept no dense|A+B||
||Pli|using black spot<br> <br>0.20＜Φ≦0.50|3|A+B||
|04|oarzer<br>bubbles|specifications,<br>nt  t find<br>0.50＜Φ≦1.00|2|A+B|2.5|
|||o easy o ,<br>must check in<br>1.00＜Φ|0|A+B||
|||<br>specify direction.<br>Total Q TY|3|||
|05|Scratches|Follow NO.3 OLED black spots, white|spots, contaminati|on.||





<!-- page 13 -->



<!-- Start of picture text -->
NO  Item  Criterion  AQL<br>Symbols Define:<br>x: Chip length      y: Chip width     z: Chip thickness<br>k: Seal width       t: Glass thickness  a: OLED side length<br>L: Electrode pad length:<br>6.1 General glass chip :<br>6.1.1 Chip on panel surface and crack between panels:<br>2.5<br>z: Chip thickness  y: Chip width  x: Chip length<br>Z ≦ 1/2t  Not over viewing area  x ≦ 1/8a<br>Chipped  1/2t ＜ z ≦ 2t  Not exceed 1/3k  x ≦ 1/8a<br>glass  ☉ If there are 2 or more chips, x is total length of each chip.<br>6.1.2 Corner crack:<br>06<br>2.5<br>z: Chip thickness  y: Chip width  x: Chip length<br>Z ≦ 1/2t  Not over viewing area  x ≦ 1/8a<br>1/2t ＜ z ≦ 2t  Not exceed 1/3k  x ≦ 1/8a<br>☉ If there are 2 or more chips, x is the total length of each chip.<br>Symbols :<br>x: Chip length      y: Chip width     z: Chip thickness<br>k: Seal width       t: Glass thickness  a: OLED side length<br>L: Electrode pad length<br>6.2 Protrusion over terminal :<br>6.2.1 Chip on electrode pad :<br>Glass<br>2.5<br>crack<br>y: Chip width  x: Chip length  z: Chip thickness<br>y ≦ 0.5mm  x ≦ 1/8a  0  ＜  z  ≦  t<br><!-- End of picture text -->



<!-- page 14 -->

|NO|Item|Criterion|AQL|
|---|---|---|---|
|||6.2.2 Non-conductive portion:||
|06|Glass<br>crack|y: Chip width<br>x: Chip length<br>z: Chip thickness<br>y≦L<br>x≦1/8a<br>0＜z≦t<br>☉If the chipped area touches the ITO terminal, over 2/3 of the ITO<br>must remain and be inspected according to electrode terminal<br>specifications.<br>☉If the product will be heat sealed by the customer, the alignment<br>mark not be damaged.<br>6.2.3 Substrate protuberanc~~e and internal crack.~~<br>y: width<br>x: length<br>y≦1/3L<br>x≦a|2.5|
|07|Cracked<br>glass|The OLED with extensive crack is not acceptable.|2.5|
|08|Backlight<br>elements|8.1 Illumination source flickers when lit.<br>8.2 Spots or scratched that appear when lit must be judged. Using<br>OLED spot, lines and contamination standards.<br>8.3 Backlight doesn’t light or color wrong.|0.65<br>2.5<br>0.65|
|09|Bezel|9.1 Bezel may not have rust, be deformed or have fingerprints,<br>stains or other contamination.<br>9.2 Bezel must comply with job specifications.|2.5<br>0.65|





<!-- page 15 -->

|NO|Item|Criterion|AQL|
|---|---|---|---|
|10|PCB , COB|10.1 COB seal may not have pinholes larger than 0.2mm or<br>contamination.<br>10.2 COB seal surface may not have pinholes through to the IC.<br>10.3 The height of the COB should not exceed the height<br>indicated in the assembly diagram.<br>10.4 There may not be more than 2mm of sealant outside the<br>seal area on the PCB. And there should be no more than<br>three places.<br>10.5 No oxidation or contamination PCB terminals.<br>10.6 Parts on PCB must be the same as on the production<br>characteristic chart. There should be no wrong parts,<br>missing parts or excess parts.<br>10.7 The jumper on the PCB should conform to the product<br>characteristic chart.<br>10.8 If solder gets on bezel tab pads, OLED pad, zebra pad or<br>screw hold pad, make sure it is smoothed down.|2.5<br>2.5<br>0.65<br>2.5<br>2.5<br>0.65<br>0.65<br>2.5|
|11|Soldering|11.1 No un-melted solder paste may be present on the PCB.<br>11.2 No cold solder joints, missing solder connections, oxidation<br>or icicle.<br>11.3 No residue or solder balls on PCB.<br>11.4 No short circuits in components on PCB.|2.5<br>2.5<br>2.5<br>0.65|
|12|General<br>appearance|12.1 No oxidation, contamination, curves or, bends on interface<br>Pin (OLB) of TCP.<br>12.2 No cracks on interface pin (OLB) of TCP.<br>12.3 No contamination, solder residue or solder balls on<br>product.<br>12.4 The IC on the TCP may not be damaged, circuits.<br>12.5 The uppermost edge of the protective strip on the interface<br>pin must be present or look as if it cause the interface pin to<br>sever.<br>12.6 The residual rosin or tin oil of soldering (component or chip<br>component) is not burned into brown or black color.<br>12.7 Sealant on top of the ITO circuit has not hardened.<br>12.8 Pin type must match type in specification sheet.<br>12.9 OLED pin loose or missing pins.<br>12.10 Product packaging must the same as specified on<br>packaging specification sheet.<br>12.11 Product dimension and structure must conform to product<br>specification sheet.|2.5<br>0.65<br>2.5<br>2.5<br>2.5<br>2.5<br>2.5<br>0.65<br>0.65<br>0.65<br>0.65|





<!-- page 16 -->

|**Check Item**<br>**Classification**|**Criteria**|
|---|---|
|No Display<br>Major||
|Missing Line<br>Major||
|Pixel Short<br>Major<br>Darker Short<br>Major||
|Wrong Display<br>Major<br>Un-uniform<br>B/A x 100% < 70%<br>A/C x 100% < 70%<br>Major||





<!-- page 17 -->

# **Precautions in use of OLED Modules** 

- (1) Avoid applying excessive shocks to module or making any alterations or modifications to it. (2) Don’t make extra holes on the printed circuit board, change the components or modify its shape of OLED display module. 

- (3) Don’t disassemble the OLED display module. 

- (4) Do not apply input signals while the logic power is off. 

- (5) Don’t operate it above the absolute maximum rating. 

- (6) Don’t drop, bend or twist OLED display module. 

- (7) Soldering: only to the I/O terminals. 

- (8) Hot-Bar FPC soldering condition: 280~350C, less than 5 seconds. 

- (9) Midas has the right to change the passive components (Resistors, capacitors and other passive components will have different appearance and color caused by the different supplier.) and change the PCB Rev. (In order to satisfy the supplying stability, management optimization and the best product performance...etc, under the premise of not affecting the electrical characteristics and external dimensions, Midas have the right to modify the version.) 

- (10) Midas has the right to upgrade or modify the product function. 

## **1. Handling Precautions** 

- (1) Since the display panel is being made of glass, do not apply mechanical impacts such as dropping from a high position. 

- (2) If the display panel is broken by some accident and the internal organic substance leaks out, be careful not to inhale nor lick the organic substance. 

- (3) If pressure is applied to the display surface or its neighborhood of the OLED display module, the cell structure may be damaged. So, be careful not to apply pressure to these sections. 

- (4) The polarizer covering the surface of the OLED display module is soft and easily scratched. (5) When the surface of the polarizer of the OLED display module has soil, clean the surface. It takes advantage by using following adhesion tape. 

* Scotch Mending Tape No. 810 or an equivalent Never try to breathe upon the soiled surface nor wipe the surface using cloth containing solvent such as ethyl alcohol, since the surface of the polarizer will become cloudy. Also, pay attention that the following liquid and solvent may spoil the polarizer: 

   - Water 

   - Ketone 

   - Aromatic Solvents 

- (6) Protection film is being applied to the surface of the display panel and removes the protection film before assembling it. At this time, if the OLED display module has been stored for a long period of time, residue adhesive material of the protection film may remain on the surface of the display panel after removed of the film. In such case, remove the residue material by the method introduced in the above Section 5. 

- (7) Do not touch the following sections whenever possible while handling the OLED display modules. 

   - Pins and electrodes 

   - Pattern layouts such as the TCP & FPC 

- (8) Hold OLED display module very carefully when placing OLED display module into the System housing. Do not apply excessive stress or pressure to OLED display module. And, do not over bend the film with electrode pattern layouts. These stresses will influence the display performance. Also, secure sufficient rigidity for the outer cases. 



<!-- page 18 -->



- (9) Do not apply stress to the LSI chips and the surrounding molded sections. 

- (10) Pay sufficient attention to the working environments when handing OLED display modules to prevent occurrence of element breakage accidents by static electricity. 

   - Be sure to make human body grounding when handling OLED display modules. 

   - Be sure to ground tools to use or assembly such as soldering irons. 

   - To suppress generation of static electricity, avoid carrying out assembly work under dry 

   - environments. 

   - Protective film is being applied to the surface of the display panel of the OLED display 

   - module. Be careful since static electricity may be generated when exfoliating the protective film. 

## **2. Storage Precautions** 

- (1) When storing OLED display modules, put them in static electricity preventive bags to avoid be directly exposed to sun or lights of fluorescent lamps. (We recommend you to store these modules in the packaged state when they were shipped from Midas Displays. At that time, be careful not to let water drops adhere to the packages or bags.) 

- (2) When the OLED display module is being dewed or when it is placed under high temperature or high humidity environments, the electrodes may be corroded if electric current is applied. Please store it in clean environment. 

## **3. Designing Precautions** 

- (1) The absolute maximum ratings are the ratings which cannot be exceeded for OLED display module, and if these values are exceeded, OLED display module may be damaged. 

- (2) To prevent occurrence of malfunctioning by noise, pay attention to satisfy the VIL and VIH specification and to make the signal line cable as short as possible. 

- (3) We recommend you to install excess current preventive unit (fuses, etc.) to the power circuit (VDD / VCC). (Recommend value: 0.5A) 

- (4) Pay sufficient attention to avoid occurrence of mutual noise interference with the nearby devices. 

- (5) As for EMI, take necessary measures on the equipment side basically. 

- (6) If the power supplied to the OLED display module is forcibly shut down by such errors as taking out the main battery while the OLED display panel is in operation, we cannot guarantee the quality of this OLED display module. 

- Connection (contact) to any other potential than the above may lead to rupture of the IC. 

- (7) If this OLED driver is exposed to light, malfunctioning may occur and semiconductor elements may change their characteristics. 

- (8) The internal status may be changed, if excessive external noise enters into the module. Therefore, it is necessary to take appropriate measures to suppress noise generation or to protect module from influences of noise on the system design. 

- (9) We recommend you to make periodical refreshment of the operation statuses (re-setting of 



<!-- page 19 -->

- the commands and re-transference of the display data) to cope with catastrophic noise. 

- (10) It's pretty common to use "Screen Saver" to extend the lifetime and Don't use the same image for long time in real application. When an OLED display module is operated for a long of time with fixed pattern, an afterimage or slight contrast deviation may occur. 

- (11) The limitation of FPC and Film bending. 



- (12) The module should be fixed balanced into the housing, or the module may be twisted. 

- <mark>0.1</mark> 

- **4. Precautions when disposing of the OLED display modules** (1) Request the qualified companies to handle industrial wastes when disposing of the OLED display modules. Or, when burning them, be sure to observe the environmental and hygienic laws and regulations. 

## **4. Precautions when disposing of the OLED display modules** 

