# Atmel-42398-ATREB215-XPRO-Extension-Board_UserGuide

*Source: `original/uhf/Atmel-42398-ATREB215-XPRO-Extension-Board_UserGuide.pdf` (21 pages)*

<!-- page 1 -->

**ATREB215 XPRO Extension Board** 





**ATREB215-XPRO and ATREB215-XPRO-A** 

### **USER GUIDE** 

# **Preface** 

This user guide facilitates how to get started with the Atmel<sup>®</sup> REB215-XPRO and REB215-XPRO-A extension boards. These extension boards are targeted for evaluating the features and performance of the Atmel® AT86RF215 radio transceiver. 



Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 2 -->



# **Table of Contents** 

|Preface|............................................................................................................................ 1|
|---|---|
|1. Intro|duction................................................................................................................3|
|1.1.|Features....................................................................................................................................... 3|
|1.2.|Kit Overview................................................................................................................................. 3|
|2. Gett|ing Started...........................................................................................................5|
|2.1.|Xplained Pro Quick Start.............................................................................................................. 5|
|2.2.|Connecting XPRO with XPRO Extension.....................................................................................5|
|2.3.|Performance Analyzer..................................................................................................................6|
|2.4.|Design Documentation and Relevant Links................................................................................. 8|
|3. Xpla|ined Pro............................................................................................................ 10|
|3.1.|Hardware Identification System..................................................................................................10|
|3.2.|Xplained Pro Standard Extension Header..................................................................................10|
|4. Har|dware Users Guide............................................................................................ 12|
|4.1.|Headers and Connectors............................................................................................................12|
|4.2.|ATREB215-XPRO/XPRO-A Peripherals.................................................................................... 14|
|5. Har|dware Revision History and Known Issues........................................................16|
|5.1.|Identifying Product ID and Revision........................................................................................... 16|
|5.2.|Revision......................................................................................................................................16|
|6. Age|ncy Certifications...............................................................................................17|
|6.1.|FCC Caution...............................................................................................................................17|
|6.2.|European Union (ETSI).............................................................................................................. 17|
|6.3.|IC Warning..................................................................................................................................18|
|7. Eva|luation Board/Kit Important Notice.....................................................................19|
|8. Doc|ument Revision History..................................................................................... 20|



2 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 3 -->



# **1. Introduction** 

## **1.1. Features** 

- Two variants of Xplained PRO Extensions are available based on usable application bands namely **ATREB215-XPRO** and **ATREB215-XPRO-A** 

   - **ATREB215-XPRO** 

      - Two SMA connectors for operation at sub-1 GHz (389.5 - 510MHz, 779 - 1020MHz) and 2.4GHz 

      - Uses a Balun in Sub-1 GHz path and no Harmonic Rejection Filter 

      - Certified for FCC, CE, and IC for 2.4GHz ISM band only. FCC ID is VW4A091980 and IC Certification Number is 11019A-091980 

      - **ATREB215-XPRO-A** 

      - Two SMA connectors for operation at 863 - 928MHz and 2.4GHz 

      - Uses a Filter-Balun in Sub-1 GHz path which has in-built Harmonic Rejection Filter 

      - Certified for FCC/IC for 2.4GHz and 915MHz ISM bands; certified for CE for 2.4GHz and 868MHz ISM bands. FCC ID is VW4A092353 and IC Certification Number is 11019A-092353 

- Atmel® **AT86RF215** : Wireless transceiver compliant to IEEE 802.15.4-2011, IEEE 802.15.4g-2012, and ETSI TS 102 887-1 

- Digital I/O 

   - Xplained Pro extension header comprising the SPI interface of AT86RF215 

   - SATA connectors comprising the I/Q interface of AT86RF215 

   - Current measurement header 

   - One reset button 

   - Two user LEDs 

- Supports with Performance Analyzer in Atmel Studio 

- Operating temperature range -40 to +85°C 

## **1.2. Kit Overview** 

The Atmel REB215-XPRO and REB215-XPRO-A are carrier boards for AT86RF215 chip for the Xplained Pro evaluation platform. They can be connected with any Xplained Pro standard extension header on any Xplained Pro MCU board to provide wireless functionality. 

3 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 4 -->



**Figure 1-1. ATREB215-XPRO** 



**Figure 1-2. ATREB215-XPRO-A** 



4 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 5 -->



# **2. Getting Started** 

## **2.1. Xplained Pro Quick Start** 

Steps to start exploring the Atmel Xplained Pro platform: 

1. Download Atmel Studio. 

2. Launch Atmel Studio. 

3. Connect a USB cable (Standard-A to Micro-B or Micro-AB) between the PC and the DEBUG USB port on the kit. 

When the Xplained Pro MCU kit is connected to your computer for the first time, the operating system will perform a driver software installation. 

Once the Xplained Pro MCU board is powered the green power LED will be lit and Atmel Studio will auto detect which Xplained Pro MCU- and extension board(s) are connected. Atmel Studio will present relevant information like datasheets and kit documentation. The kit landing page in Atmel Studio also has the option to launch Atmel Software Framework (ASF) example applications for the kit. The target device is programmed and debugged by the on-board Embedded Debugger and therefore no external programmer or debugger tool is needed. 

## **2.2. Connecting XPRO with XPRO Extension** 

ATREB215-XPRO and ATREB215-XPRO-A Extension boards have been designed to be connected with an Xplained Pro header marked EXT1. However, it is compatible with all Xplained Pro EXT headers. Refer to the pin-out of your Xplained Pro evaluation kit to find out which Xplained Pro EXT headers can be used. The connection of ATREB215-XPRO wireless extension board with Atmel SAM4L Xplained Pro Evaluation Kit is shown below. Similarly, ATREB215-XPRO-A can also be connected with ATSAM4LXPRO. 

Performance Analyzer Application AT86RF215 (ATREB215-XPRO) firmware are available at "New Example Project from ASF or Extensions" in Atmel Studio for both ATSAM4L-XPRO and ATSAM4SXPRO boards to characterize RF performance of ATREB215-XPRO/XPRO-A. Initially, the corresponding XPRO boards should be programmed with the respective Performance Analyzer firmware. After programming the XPRO, the Performance Analyzer GUI available in Atmel Studio can connect with the wireless chip on the board and allow the user to change the channel, transmit power, modulation scheme,.. etc. to perform RF tests. 

**Figure 2-1. Connecting SAM4L-XPRO with ATREB215-XPRO Extension** 



5 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 6 -->



## **2.3. Performance Analyzer** 

### **2.3.1. Introduction** 

The Performance Analyzer firmware together with a GUI (Wireless Composer Extension) in Atmel Studio provides a way to perform a number of basic RF functional tests. 

A quick-start guide and general help are available in Performance Analyzer once it is started. 

The latest version of Atmel Studio is 7.0. This section guides the user to install necessary wireless extension and programming the wireless assembly (XPRO + REB215-XPRO/XPRO-A) using Atmel Studio 7.0. 

### **2.3.2. Programming wireless assembly using Atmel Studio 7.0** 

The following steps expalin the way to program the wireless assembly and get started. 

1. Connect the Debug USB port of the XPRO board with PC using the USB cable to power on/ program the board. 

2. Program the XPRO board using on-board Embedded Debugger (EDBG) with Performance Analyzer Application AT86RF215 (ATREB215-XPRO) firmware available at "New Example Project from ASF or Extensions" in Atmel Studio. 



3. Connect ATREB215-XPRO/XPRO-A with the programmed XPRO board. 

4. Open the Performance Analyzer GUI from Tools menu in Atmel Studio. 

5. Follow Quick Start guidelines available in Performance Analyzer page. Select COM port and click 'connect'. COM port selection is an important step. The USB cable from the PC should be connected with the Debug USB port for Sub-1 GHz operation and it should be connected with the Target USB port (E.g.: SAM4L USB for SAM4L-XPRO) for 2.4GHz operation. If two USB cables are connected from the PC with two USB ports of the XPRO board, the appropriate COM port should be selected for Sub-1 GHz and 2.4GHz operation. Even though the AT86RF215 allows simultaneous operation at sub-1 GHz and 2.4GHz, the Performance Analyzer software is restricted to operate in one band at a time. 

6. Finally, the Performance Analyzer will allow you to change the parameters like Channel Page, Channel, TX Power Register Value, ... etc. to perform various RF tests. For more details about the usage of Performance Analyzer, click 'help' as shown below in the Performance Analyzer page. 

6 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 7 -->





## **2.3.3. Installing Wireless Composer 7.0 extension in Atmel Studio 7.0** 

The following steps explain the way to install necessary wireless extension tool in Atmel Studio 7.0 

- Install and open Atmel Studio 

- Go to Tools and click "Extensions and Updates... " 



- In "Extensions and Updates" window, Click on "Available Downloads". Next, click on the arrow mark on the left side of "All" and click on "Wireless". Select "Wireless Composer 7.0" and click "Download" which will lead to Atmel Gallery 



- Log in to Atmel Gallery. Click download again and the download will start. 

7 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 8 -->







- Install Wireless Composer 



- Restart Atmel Studio after installation. The Performance Analyzer GUI will be available in Tools menu 



# **2.4. Design Documentation and Relevant Links** 

The following list contains links to the most relevant documents and software for ATREB215-XPRO/ XPRO-A: 

8 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 9 -->



- **Xplained Pro products** - Atmel Xplained Pro is a series of small-sized and easy-to-use evaluation kits for Atmel microcontrollers and other Atmel products. It consists of a series of low-cost MCU boards for evaluation and demonstration of features and capabilities of different MCU families. 

- **ATREB215-XPRO/XPRO-A User Guide** - PDF version of this User Guide. 

- **ATREB215-XPRO Design Documentation** - Package containing schematics, BOM, assembly drawings, 3D plots, layer plots, etc. 

- **ATREB215-XPRO-A Design Documentation** - Package containing schematics, BOM, assembly drawings, 3D plots, layer plots, etc. 

- **Atmel Studio** - Free Atmel IDE for development of C/C++ and assembler code for Atmel microcontrollers. 

- **EDBG User Guide** - User guide containing more information about the on-board Embedded Debugger. 

- **Atmel Data Visualizer** - Atmel Data Visualizer is a program used for processing and visualizing data. Data Visualizer can receive data from various sources such as the Embedded Debugger Data Gateway Interface found on Xplained Pro boards and COM ports. 

- **ATREB215-XPRO** - Product page. 

- **ATREB215-XPRO-A** - Product page. 

- **AT86RF215 Complete** - Wireless chip datasheet. 

- **AT13282: AT86RF215 Chat Application** - Application Note. 

- **AT24MAC602-STUM-T** - Serial EEPROM datasheet. 

9 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 10 -->



# **3. Xplained Pro** 

Xplained Pro is an evaluation platform that provides the full Atmel microcontroller experience. The platform consists of a series of Microcontroller (MCU) boards and extension boards, which are integrated with Atmel Studio, have Atmel Software Framework (ASF) drivers and demo code, support data streaming, and more. Xplained Pro MCU boards support a wide range of Xplained Pro extension boards, which are connected through a set of standardized headers and connectors. Each extension board has an identification (ID) chip to uniquely identify which boards are connected to an Xplained Pro MCU board. This information is used to present relevant user guides, application notes, datasheets, and example code through Atmel Studio. 

## **3.1. Hardware Identification System** 

All Xplained Pro compatible extension boards have an Atmel ATSHA204 CryptoAuthentication™ chip mounted. This chip contains information that identifies the extension with its name and some extra data. When an Xplained Pro extension is connected to an Xplained Pro MCU board the information is read and sent to Atmel Studio. The Atmel Kits extension, installed with Atmel Studio, will give relevant information, code examples, and links to relevant documents. The table below shows the data fields stored in the ID chip with example content. 

**Table 3-1. Xplained Pro ID Chip Content** 

|**Data field**|**Data type**|**Example content**|
|---|---|---|
|Manufacturer|ASCII string|Atmel'\0'|
|Product Name|ASCII string|Segment LCD1 Xplained Pro'\0'|
|Product Revision|ASCII string|02'\0'|
|Product Serial Number|ASCII string|1774020200000010’\0’|
|Minimum Voltage [mV]|uint16_t|3000|
|Maximum Voltage [mV]|uint16_t|3600|
|Maximum Current [mA]|uint16_t|30|



## **3.2. Xplained Pro Standard Extension Header** 

All Xplained Pro kits have one or more dual row, 20-pin, 100mil extension header. Xplained Pro MCU boards have male headers, while Xplained Pro extensions have their female counterparts. Note that all pins are not always connected. All connected pins follow the defined pin-out description in the table below. 

The extension headers can be used to connect a variety of Xplained Pro extensions to Xplained Pro MCU boards or to access the pins of the target MCU on Xplained Pro MCU boards directly. 

**Table 3-2. Xplained Pro Standard Extension Header** 

|**Pin number**|**Name**|**Description**|
|---|---|---|
|1|ID|Communication line to the ID chip on an extension board|
|2|GND|Ground|



Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 10 Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 11 -->



|**Pin number**|**Name**|**Description**|
|---|---|---|
|3|ADC(+)|Analog to digital converter, alternatively positive part of differential<br>ADC|
|4|ADC(-)|Analog to digital converter, alternatively negative part of differential<br>ADC|
|5|GPIO1|General purpose I/O|
|6|GPIO2|General purpose I/O|
|7|PWM(+)|Pulse width modulation, alternatively positive part of differential<br>PWM|
|8|PWM(-)|Pulse width modulation, alternatively negative part of differential<br>PWM|
|9|IRQ/GPIO|Interrupt request line and/or general purpose I/O|
|10|SPI_SS_B/<br>GPIO|Slave select for SPI and/or general purpose I/O|
|11|I<sup>2</sup>C_SDA|Data line for I<sup>2</sup>C interface. Always implemented, bus type.|
|12|I<sup>2</sup>C_SCL|Clock line for I<sup>2</sup>C interface. Always implemented, bus type.|
|13|UART_RX|Receiver line of target device UART|
|14|UART_TX|Transmitter line of target device UART|
|15|SPI_SS_A|Slave select for SPI. Should preferably be unique.|
|16|SPI_MOSI|Master out slave in line of serial peripheral interface. Always<br>implemented, bus type.|
|17|SPI_MISO|Master in slave out line of serial peripheral interface. Always<br>implemented, bus type.|
|18|SPI_SCK|Clock for serial peripheral interface. Always implemented, bus type.|
|19|GND|Ground|
|20|VCC|Power for extension board|



11 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 12 -->



# **4. Hardware Users Guide** 

## **4.1. Headers and Connectors** 

### **4.1.1. ATREB215-XPRO/XPRO-A Extension Header** 

ATREB215-XPRO/XPRO-A has an Xplained Pro Standard Extension Header (J100) marked with EXT in PCB silkscreen. This header makes it possible to connect the board to any Xplained Pro MCU board. The pin-out definition for the extension header is shown below. 

**Table 4-1. ATREB215-XPRO/XPRO-A Extension Header J100** 

|**Pin on EXT**|**Function**|**Description**|
|---|---|---|
|1|ID_DATA|Communication line to ID chip|
|2|GND|Ground|
|3|ADC(+)|NC|
|4|ADC(-)|NC|
|5|GPIO|LED D2 Yellow for user function|
|6|GPIO|LED D1 Green for user function|
|7|PWM(+)|RESET to RF215|
|8|PWM(-)|NC|
|9|IRQ/GPIO|Interrupt request line to MCU on Xplained Pro board|
|10|SPI_SS_B/GPIO|NC|
|11|TWI_SDA|Data line for I2C interface to serial EEPROM|
|12|TWI_SCL|Data line for I2C interface to serial EEPROM|
|13|UART_RX|NC|
|14|UART_TX|NC|
|15|SPI_SS_A|Slave select for SPI. Should be unique if possible.|
|16|SPI_MOSI|Master out slave in line of Serial peripheral interface.<br>Always implemented, bus type.|
|17|SPI_MISO|Master in slave out line of Serial peripheral interface.<br>Always implemented, bus type.|
|18|SPI_SCK|Clock for Serial peripheral interface. Always implemented,<br>bus type.|
|19|GND|Ground|
|20|VCC_TARGET|Power for extension board|



### **4.1.2. Current Measurement Header** 

Current measurement header (J1) can be used to measure the current consumed by the board by removing the jumper and connecting an Ammeter/Multimeter across the two pins of J1. 

12 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 13 -->



## **4.1.3. Serial I/Q Data Interface (J101, J102 and J103)** 

Low voltage differential signalling (LVDS) interface is used for the data transfer between the AT86RF215 and an external baseband processor through SATA connectors (J101, J102, and J103). 

**Table 4-2. J101- I/Q Data Receiver 2.4GHz** 

|**Pin on connector**|**RF215 signal**|**Function**|
|---|---|---|
|1||Ground|
|2|RXDP24|B+ (Receive)|
|3|RXDN24|B- (Receive)|
|4||Ground|
|5|RXCLKP|A+ (Receive)|
|6|RXCLKN|A- (Receive)|
|7||Ground|



**Table 4-3. J102- I/Q Data Receiver Sub-1 GHz** 

|**Pin on connector**|**RF215 signal**|**Function**|
|---|---|---|
|1||Ground|
|2|RXDP09|B+ (Receive)|
|3|RXDN09|B- (Receive)|
|4||Ground|
|5||A+ (Receive)|
|6||A- (Receive)|
|7||Ground|



**Table 4-4. J103- I/Q Data Transmitter** 

|**Pin on connector**|**RF215 signal**|**Function**|
|---|---|---|
|1||Ground|
|2|TXDP|B+ (Receive)|
|3|TXDN|B- (Receive)|
|4||Ground|
|5|TXCLKP|A+ (Receive)|
|6|TXCLKN|A- (Receive)|
|7||Ground|



## **4.1.4. J104 and J105** 

When connecting ATREB215-XPRO/XPRO-A with RF Frontend modules (PA, LNA, and switches) to increase the output power/range, the digital signals available in J104 and J05 connectors from AT86RF215 are used to control the switches in the external RF Frontend. By controlling the switches, the Frontends can be operated in the following modes: 

13 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 14 -->



1. TX mode (switches make connection with only PA). 

2. RX mode (switches make connection with only LNA). 

3. All off (neither connected with PA nor with LNA). 

**Table 4-5. J104** 

|**Pin on connector**|**RF215 signal**|**Function**|
|---|---|---|
|1|FEB24|External Frontend Control for 2.4GHz|
|2|FEA24|External Frontend Control for 2.4GHz|



**Table 4-6. J105** 

|**Pin on connector**|**RF215 signal**|**Function**|
|---|---|---|
|1|FEB09|External Frontend Control for Sub-1 GHz|
|2|FEA09|External Frontend Control for Sub-1 GHz|



# **4.2. ATREB215-XPRO/XPRO-A Peripherals** 

## **4.2.1. Baluns** 

The 2.4GHz RF path has a Filter-Balun (2450FB15A050 from Johanson Technology) to convert differential RF signals from pins REP24/RFN24 of AT86RF215 into a single ended RF signal and viceversa. The 2.4GHz RF path is common for both the ATREB215-XPRO and the ATREB215-XPRO-A. 

The sub-1 GHz RF path is not common for ATREB215-XPRO and ATREB215-XPRO-A. The ATREB215XPRO's RF path has a Balun (DLW21SN900SQ2 from muRata) to convert the differential RF signals from pins RFP09/RFN09 of AT86RF215 into a single ended RF signal and vice-versa. As this Balun doesn't have an in-built Filter to suppress higher order Harmonics, the ATREB215-XPRO is recommended for conducted lab measurements across the complete sub-1 GHz band, i.e. 389.5 - 510MHz and 779 - 1020MHz. 

The ATREB215-XPRO-A's RF path has a Filter-Balun (0896BM15E0025E from Johanson Technology) to convert the differential RF signals from pins RFP09/RFN09 of AT86RF215 into a single ended RF signal and vice-versa. This Filter-Balun has an in-built harmonic suppression for 863 - 870MHz and 915MHz ISM bands. Therefore, the ATREB215-XPRO-A is recommended for use in these two Sub-1 GHz bands, including radiated measurements. 

## **4.2.2. SMA Connectors** 

There are two SMA connectors available. One is for 2.4GHz transmit/receive and the other one is for Sub-1 GHz transmit/receive. 

**Table 4-7. SMA Connectors** 

|**Connector**|**Function**|
|---|---|
|SMA-1|RF input/output for Sub-1 GHz|
|SMA-2|RF input/output for 2.4GHz|



## **4.2.3. EEPROM** 

The board contains the AT24MAC602, a serial EEPROM, which has a factory programmed unique MAC address available for read through the I<sup>2</sup> C interface of the J100. 

14 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 15 -->



## **4.2.4. LED** 

There are two LEDs (Green and Red colors) on the board that are controlled by host MCU available in XPRO board. These LEDs are used for status indication. Green LED is for Power and Red LED is for user application. 

## **4.2.5. Button** 

There is a button SW1 to reset the AT86RF215 device. 

15 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 16 -->



# **5. Hardware Revision History and Known Issues** 

## **5.1. Identifying Product ID and Revision** 

The revision and product identifier of the ATREB215-XPRO/XPRO-A can be found by looking at the sticker on the bottom side of the PCB. The identifier and revision are printed in plain text as A09-nnnn\rr, where nnnn is the identifier and rr is the revision. Also the label contains a 10-digit serial number unique to each board. 

The product identifier for the ATREB215-XPRO is A09-1982. 

The product identifier for the ATREB215-XPRO-A is A09-2353. 

## **5.2. Revision** 

Revision 5 is the initially released revision and Revision 7 is the latest revision for the ATREB215-XPRO. Revision 4 is the initially released revision for the ATREB215-XPRO-A. There are no known issues. 

**Table 5-1. Released Board and Chip Revisions** 

|**Board**|**Board revision**|**AT86RF215 version**|
|---|---|---|
|ATREB215-XPRO (A09-1982)|5|1|
||6|1|
||7|3|
|ATREB215-XPRO-A (A09-2353)|4|3|



16 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 17 -->



# **6. Agency Certifications** 

## **6.1. FCC Caution** 

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment. 

### **Important:** 

These devices comply with part 15 of the FCC Rules. Operation is subject to the following two conditions: 

- (1) These devices may not cause harmful interference, and 

- (2) These devices must accept any interference received, including interference that may cause undesired operation. 

The ATREB215-XPRO/XPRO-A kit will be used by professional users in lab environment. If these modules are intended for OEM integrator, the OEM integrator is still responsible for the FCC compliance requirement of the end product, which integrates these modules. The final end product must be labeled in a visible area with the following respective FCC IDs: VW4A091980 for ATREB215-XPRO applicable only for 2.4GHz ISM band and FCC ID: VW4A092353 for ATREB215-XPRO-A applicable only for 2.4GHz and 915MHz ISM bands. 

**Important: FCC Radiation Exposure Statement:** These equipments comply with FCC radiation exposure limits set forth for uncontrolled environment. These equipments should be installed and operated with minimum distance 20cm between the radiator and your body. These transmitters must not be co-located or operating in conjunction with any other antenna or transmitter. 

## **6.2. European Union (ETSI)** 

The ATREB215-XPRO Module has been certified for use in European Union countries at 2.4GHz ISM Band. The ATREB215-XPRO-A Module has been certified for use in European Union countries at 863MHz - 870MHz and 2.4GHz ISM Bands. If these modules are incorporated into a product, the manufacturer must ensure compliance of the final product to the European harmonized EMC and low voltage/safety standards. A Declaration of Conformity must be issued for each of these standards and kept on file as described in Annex II of the R&TTE Directive. 

Furthermore, the manufacturer must maintain a copy of the modules' documentation and ensure the final product does not exceed the specified power ratings, antenna specifications, and/or installation requirements as specified in the user manual. If any of these specifications are exceeded in the final product, a submission must be made to a notified body for compliance testing to all required standards. 

17 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 18 -->



### **Important:** 

The 'CE' marking must be affixed to a visible location on the OEM product. The CE mark shall consist of the initials "CE" taking the following form: 

The CE marking must have a height of at least 5mm except where this is not possible on account of the nature of the apparatus. The CE marking must be affixed visibly, legibly, and indelibly. More detailed information about CE marking requirements can be found at "DIRECTIVE 1999/5/EC OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL" on 9 March 1999 at section 12. 

## **6.3. IC Warning** 

These devices comply with Industry Canada licence-exempt RSS standard(s). 

### **Important:** 

Operation is subject to the following two conditions: 

(1) These devices may not cause interference, and 

(2) These devices must accept any interference, including interference that may cause undesired operation of the device. 

### **Important:** 

Ces appareils sont conformes avec Industrie Canada exempts de licence standard RSS (s). L'exploitation est autorisée aux deux conditions suivantes : 

(1) Ces appareils ne doit pas produire de brouillage, et 

(2) ces appareils doit accepter tout brouillage radioélectrique subi, même si le brouillage que susceptible d'en compromettre le fonctionnement. 

**Warning:** These devices been tested are compliance with RF field strength limits. The users can obtain Canadian information on RF exposure and compliance. The minimum distance from the body to use the device is 20cm. 

**Warning:** Ces appareils conformer aux des limites d'intensité de champ RF . Les utilisateurs peuvent obtenir des informations canadienne sur l'exposition aux RF et la conformité. La distance minimale du corps à utiliser le dispositif est de 20cm. 

Contain transmitter module IC: 11019A-091980 on ATREB215-XPRO applicable only for 2.4GHz ISM band and 11019A-092353 on ATREB215-XPRO-A applicable only for 2.4GHz and 915MHz ISM bands. Where 11019A-091980 and 11019A-092353 are the module’s certification numbers. 

18 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] 

Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 19 -->



# **7. Evaluation Board/Kit Important Notice** 

This evaluation board/kit is intended for use for **FURTHER ENGINEERING, DEVELOPMENT, DEMONSTRATION, OR EVALUATION PURPOSES ONLY.** It is not a finished product and may not (yet) comply with some or any technical or legal requirements that are applicable to finished products, including, without limitation, directives regarding electromagnetic compatibility, recycling (WEEE), FCC, CE or UL (except as may be otherwise noted on the board/kit). Atmel supplied this board/kit "AS IS", without any warranties, with all faults, at the buyer's and further users' sole risk. The user assumes all responsibility and liability for proper and safe handling of the goods. Further, the user indemnifies Atmel from all claims arising from the handling or use of the goods. Due to the open construction of the product, it is the user's responsibility to take any and all appropriate precautions with regard to electrostatic discharge and any other technical or legal concerns. 

EXCEPT TO THE EXTENT OF THE INDEMNITY SET FORTH ABOVE, NEITHER USER NOR ATMEL SHALL BE LIABLE TO EACH OTHER FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES. 

No license is granted under any patent right or other intellectual property right of Atmel covering or relating to any machine, process, or combination in which such Atmel products or services might be or are used. 

**Mailing Address:** `Atmel Corporation 1600 Technology Drive San Jose, CA 95110 USA` 

19 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 20 -->



# **8. Document Revision History** 

|**Doc. rev.**|**Date**|**Comment**|
|---|---|---|
|42398B|02/2016|ATREB215-XPRO-A added revision.|
|42398A|03/2015|Initial document release.|



20 

Atmel ATREB215-XPRO and ATREB215-XPRO-A [USER GUIDE] Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 



<!-- page 21 -->



**Atmel Corporation** 1600 Technology Drive, San Jose, CA 95110 USA **T:** (+1)(408) 441.0311 **F:** (+1)(408) 436.4200 **| www.atmel.com** 

© 2016 Atmel Corporation. / Rev.: Atmel-42398B-ATREB215-XPRO-Extension-Board_User Guide-02/2016 

Atmel®, Atmel logo and combinations thereof, Enabling Unlimited Possibilities®, and others are registered trademarks or trademarks of Atmel Corporation in U.S. and other countries. Other terms and product names may be trademarks of others. 

DISCLAIMER: The information in this document is provided in connection with Atmel products. No license, express or implied, by estoppel or otherwise, to any intellectual property right is granted by this document or in connection with the sale of Atmel products. EXCEPT AS SET FORTH IN THE ATMEL TERMS AND CONDITIONS OF SALES LOCATED ON THE ATMEL WEBSITE, ATMEL ASSUMES NO LIABILITY WHATSOEVER AND DISCLAIMS ANY EXPRESS, IMPLIED OR STATUTORY WARRANTY RELATING TO ITS PRODUCTS INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. IN NO EVENT SHALL ATMEL BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE, SPECIAL OR INCIDENTAL DAMAGES (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS AND PROFITS, BUSINESS INTERRUPTION, OR LOSS OF INFORMATION) ARISING OUT OF THE USE OR INABILITY TO USE THIS DOCUMENT, EVEN IF ATMEL HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. Atmel makes no representations or warranties with respect to the accuracy or completeness of the contents of this document and reserves the right to make changes to specifications and products descriptions at any time without notice. Atmel does not make any commitment to update the information contained herein. Unless specifically provided otherwise, Atmel products are not suitable for, and shall not be used in, automotive applications. Atmel products are not intended, authorized, or warranted for use as components in applications intended to support or sustain life. 

SAFETY-CRITICAL, MILITARY, AND AUTOMOTIVE APPLICATIONS DISCLAIMER: Atmel products are not designed for and will not be used in connection with any applications where the failure of such products would reasonably be expected to result in significant personal injury or death (“Safety-Critical Applications”) without an Atmel officer's specific written consent. Safety-Critical Applications include, without limitation, life support devices and systems, equipment or systems for the operation of nuclear facilities and weapons systems. Atmel products are not designed nor intended for use in military or aerospace applications or environments unless specifically designated by Atmel as military-grade. Atmel products are not designed nor intended for use in automotive applications unless specifically designated by Atmel as automotive-grade. 

