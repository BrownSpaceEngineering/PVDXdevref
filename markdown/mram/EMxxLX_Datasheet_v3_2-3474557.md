# EMxxLX_Datasheet_v3_2-3474557

*Source: `original/mram/EMxxLX_Datasheet_v3_2-3474557.pdf` (80 pages)*

<!-- page 1 -->

**_EMxxLX_** 





# **Expanded Serial Peripheral Interface (xSPI) Industrial STT-MRAM Persistent Memory** 1.8V, 200MHz Octal SPI interface (STR & DTR) with SPI, DSPI and QSPI 

Extended Temperature Range of -40ºC to 105ºC added for 32Mb and 64Mb part numbers 

## **Features** 

- Expanded SPI bus interface supporting 

- Octal, Quad, Dual and Single SPI protocol 

- • Up to 200MHz single and double transfer rate (STR/DTR) for Octal SPI 

- Up to 133MHz, SPI, DSPI, QSPI 

- • Data endurance: Unlimited read, write and erase operations for supported life of product 

- 

- Data retention: 10 Years minimum across temperature 

   - JEDEC compliant: JESD251, JESD251-1 

- 

- Byte level writes and reads with no erase required as persistent memory 

   - Data integrity: No external ECC required. 

- 

- Low Power Modes: 

   - Standby  350µA 

   - Deep power down 300 µA 

- SPI compatibility: NVSRAM, FRAM, NOR, Toggle 

   - MRAM 

- SPI, xSPI Commands for Program/Erase emulated NOR compatible Execute-in-place (XIP) 

- Volatile and nonvolatile configuration settings 

- Nonvolatile settings are not reflow protected 

- • Dedicated  256-byte  OTP area  outside main memory 

   - Readable and user-lockable 

   - Permanent lock with WRITE OTP command 

   - Not reflow protected 

- Erase capability 

   - Chip / bulk erase and sector erase 

   - Subsector erase 4KB, 32KB granularity 

- Voltage 

   - 1.65–2.0V (1.8V) 

- Density EM008LX 8Mb, EM016LX 16Mb, EM032LX 32Mb, EM064LX 64Mb 

- 400MBps sustained throughput with OSPI at 200MHz , DTR, for reads and writes 

   - Boot mode configurations 

- 

- Boot in x1, x2, x4, x8 

- • Software reset and hardware reset pin available 

- 3-byte and 4-byte address modes 

   - Sequential (burst) read and writes 

- 

   - Electronic signature 

- 

   - JEDEC-standard 3-byte signature 

- JEDEC standard, RoHS compliant packages: 

   - 24-ball BGA, 6mm x 8mm (5 x 5 array) 

   - 8-pin DFN, 6mm x 8mm 

   - Operating temperature range 

- 

   - Commercial: From 0°C to +70°C 

   - Industrial: From -40°C to +85°C 

   - Extended: From -40°C to +105°C for 32Mb and 64Mb (see OPN table) 

   - Security and write protection 

- 

- 16 configurable hardware write protected regions plus top/bottom select 

- Program/erase protection during power-up 

- CRC command to detect accidental changes to user data 

©2024 Everspin Technologies 

EMxxLX  v3.2 

1 



<!-- page 2 -->

**_EMxxLX_** 



## **Table of Contents** 

|**Section**|**Content**|**Page**|
|---|---|---|
|1|Device Description with Block Diagrams ..............................................................................................................|.<br>5|
|2|Device Pin Assignments ..............................................................................................................................................|.<br>7|
||2.1<br>24-Ball BGA||
||2.2<br>Signal Ball Assignment||
||2.3<br>8-Lead DFN Package||
||2.4<br>DFN Signal Pinout||
|3|Signal Descriptions  .......................................................................................................................................................|<br>10|
|4|xSPI Signal Protocol  .....................................................................................................................................................|<br>11|
|5|Registers  ...........................................................................................................................................................................|<br>13|
||5.1<br>Status Register||
||5.2<br>Hardware Write Protection||
||5.3<br>Flag Status Register||
||5.4<br>Configuration Registers||
||5.5<br>Nonvolatile Configuration Register||
||5.6<br>Volatile Configuration Register||
||5.7<br>Interrupt mask and Status Register||
||5.8<br>Device Factory Initialization Mode||
||5.9<br>Tuning Data Pattern Register||
||5.10<br>Supported Clock Frequencies||
|6|Register Operations  .....................................................................................................................................................|<br>26|
|7|Memory Organization  .................................................................................................................................................|<br>31|
|8|xSPI Commands and OpCodes  ................................................................................................................................|<br>32|
|9|Read and Write Operations  ......................................................................................................................................|.<br>34|
|10|READ Operations  ..........................................................................................................................................................|.<br>35|
|11|WRITE (Program) Operations  ...................................................................................................................................|<br>42|
|12|XIP (Execute-in-Place) Mode  ....................................................................................................................................|<br>47|
|13|ERASE Operations  .........................................................................................................................................................|<br>49|
|14|OTP Operation  ...............................................................................................................................................................|<br>50|
|15|Extended Address Operation  ...................................................................................................................................|<br>52|
|16|Deep Power Down Operation  ..................................................................................................................................|<br>54|
|17|Initialization Considerations  .....................................................................................................................................|.<br>56|
|18|Reset Operations  ...........................................................................................................................................................|<br>57|
|19|Tuning Data Pattern  .....................................................................................................................................................|<br>60|
|20|CRC  .....................................................................................................................................................................................|<br>61|
|21|Package Information  ...................................................................................................................................................|.<br>63|
|22|Electrical Specifications and Operating Conditions  ........................................................................................|.<br>66|
|23|Orderable Part Numbers  ............................................................................................................................................|<br>77|
||Revision History  .............................................................................................................................................................|<br>79|



©2024 Everspin Technologies 

EMxxLX  v3.2 

2 



<!-- page 3 -->

**_EMxxLX_** 



## **List of Figures** 

|Figure 1:|Block Diagram .............................................................................................................................................................................|6|
|---|---|---|
|Figure 2:|Logic Diagram .............................................................................................................................................................................|6|
|Figure 3:|Device Pin Assignments 24-ball BGA .................................................................................................................................|7|
|Figure 4:|8-Pin DFN Package Signal Assignments ...........................................................................................................................|9|
|Figure 5:|READ Status Register with STR  ............................................................................................................................................|26|
|Figure 6:|Read Nonvolatile/Volatile Register......................................................................................................................................|27|
|Figure 7:|READ General Purpose Register with STR ........................................................................................................................|28|
|Figure 8:|Write Status Register ................................................................................................................................................................|30|
|Figure 9:|Write Nonvolatile/Volatile Register ....................................................................................................................................|30|
|<br>Figure 10:|<br>Opcode Timing Diagram ........................................................................................................................................................|34|
|Figure 11:|READ ID Diagram ......................................................................................................................................................................|36|
|<br>Figure 12:|<br>Read ID Diagram (Octal DTR Mode) ..................................................................................................................................|36|
|<br>Figure 13:|<br>Read Diagram ..............................................................................................................................................................................|38|
|<br>Figure 14:|<br>Read Fast Diagram ....................................................................................................................................................................|39|
|Figure 15:|Read Fast Dual Input/Output ................................................................................................................................................|39|
|Figure 16:|Read Fast Quad Input/Output ..............................................................................................................................................|39|
|<br>Figure 17:|<br>Read Fast Octal Output ...........................................................................................................................................................|40|
|<br>Figure 18:|<br>Read Fast Octal Input/Output ...............................................................................................................................................|40|
|Figure 19:|Read Fast DTR  SPI, Dual SPI, Quad SPI, Octal SPI ........................................................................................................|41|
|Figure 20:|Read Word Quad Input/Output (no DTR) (E7h) ............................................................................................................|41|
|Figure 21:|Write Enable/Disable Operation ..........................................................................................................................................|42|
|Figure 22:|Write (Program) ..........................................................................................................................................................................|44|
|Figure 23:|Write Fast Dual Input................................................................................................................................................................|44|
|Figure 24:|Write Fast Quad Input ..............................................................................................................................................................|45|
|Figure 25:|Write Fast Octal Input ..............................................................................................................................................................|45|
|Figure 26:|Write Fast with DTR Configured ..........................................................................................................................................|46|
|Figure 27:|Read Fast (XIP) ............................................................................................................................................................................|48|
|Figure 28:|Erase Operations ........................................................................................................................................................................|49|
|Figure 29:|OTP Write ......................................................................................................................................................................................|51|
|Figure 30:|OTP Read ......................................................................................................................................................................................|52|
|Figure 31:|4-Byte Address Mode Enter ..................................................................................................................................................|53|
|Figure 32:|Read 4-Byte Address ................................................................................................................................................................|54|
|Figure 33:|Deep Power Down Enter  ........................................................................................................................................................|55|
|Figure 34:|Deep Power Down Exit ............................................................................................................................................................|56|
|Figure 35:|Software Reset ............................................................................................................................................................................|57|
|Figure 36:|Hardware Reset Timing ...........................................................................................................................................................|58|
|Figure 37:|Reset with Signal Sequence ...................................................................................................................................................|59|
|Figure 38:|CRC Operation  ...........................................................................................................................................................................|62|
|Figure 39:|24-Ball TBGA Package ..............................................................................................................................................................|63|
|Figure 40:|8-PIN DFN  Package .................................................................................................................................................................|64|
|Figure 41:|Power-On Timing  .....................................................................................................................................................................|66|
|<br>Figure 42:|<br>AC Timing Input/Output Reference Levels ......................................................................................................................|69|
|<br>Figure 43:|<br>Serial Input Timing STR in SPI Mode  ................................................................................................................................|73|
|<br>Figure 44:|<br>Serial Input Timing STR in Dual, Quad, and Octal SPI Modes  .................................................................................|73|
|<br>Figure 45:|<br>Serial Input Timing DTR in SPI Mode  ................................................................................................................................|74|
|<br>Figure 46:|<br>Serial Input Timing DTR in Dual, Quad, or Octal SPI Mode  .....................................................................................|74|
|Figure 47:|Serial Output Timing STR  ......................................................................................................................................................|75|
|Figure 48:|Serial Output Timing DTR  .....................................................................................................................................................|75|
|Figure 49:|Data Strobe (DS) Timing  ........................................................................................................................................................|76|
|Figure 50:|Write Protect Setup and Hold Timing  ..............................................................................................................................|76|



©2024 Everspin Technologies 

EMxxLX  v3.2 

3 



<!-- page 4 -->

**_EMxxLX_** 



# **List of Tables** 

|Table 1:|Signal Ball Assignments 24 Ball BGA ....................................................................................................................................|8|
|---|---|---|
|Table 2:|Signal Pinout 8-DFN ....................................................................................................................................................................|9|
|Table 3:|Signal Descriptions ......................................................................................................................................................................|10|
|Table 4:|1S-1S-1S Bit Positions ................................................................................................................................................................|12|
|Table 5:|8D-8D-8D Bit Positions ..............................................................................................................................................................|12|
|Table 6:|Status Register ...............................................................................................................................................................................|13|
|Table 7:|Write Protection ............................................................................................................................................................................|15|
|Table 8:|Block Protection ............................................................................................................................................................................|15|
|Table 9:|Flag Status Register .....................................................................................................................................................................|16|
|Table 10:|Nonvolatile Configuration Register ......................................................................................................................................|18|
|Table 11:|Volatile Configuration Register ..............................................................................................................................................|20|
|Table 12:|Interrupt Mask ...............................................................................................................................................................................|22|
|Table 13:|Interrupt Status .............................................................................................................................................................................|22|
|Table 14:|Device Factory Initialization Mode ........................................................................................................................................|23|
|Table 15:|TDP Register ...................................................................................................................................................................................|23|
|Table 16:|STR – Supported Frequency .....................................................................................................................................................|24|
|Table 17:|DTR – Supported Frequency  ...................................................................................................................................................|25|
|Table 18:|Read Register Operations .........................................................................................................................................................|26|
|Table 19:|Write Register Operations ........................................................................................................................................................|29|
|Table 20:|Memory Organization ................................................................................................................................................................|31|
|Table 21:|Instruction Command Table ....................................................................................................................................................|32|
|Table 22:|Device ID Data  .............................................................................................................................................................................|35|
|Table 23:|XIP Bit Settings ..............................................................................................................................................................................|47|
|Table 24:|Hardware Reset Timing ..............................................................................................................................................................|58|
|Table 25:|CRC operation on entire device  ............................................................................................................................................|61|
|Table 26:|CRC operation on a range  .......................................................................................................................................................|62|
|Table 27:|Power-On Timing .........................................................................................................................................................................|66|
|Table 28:|Absolute Maximum Ratings  ....................................................................................................................................................|67|
|Table 29:|Recommended Operating Conditions  ................................................................................................................................|67|
|Table 30:|Device Pin Loading  .....................................................................................................................................................................|68|
|Table 31:|MRAM Characteristics  ...............................................................................................................................................................|68|
|Table 32:|AC IO Timing Conditions  .........................................................................................................................................................|68|
|Table 33:|DC Current Characteristics  ......................................................................................................................................................|69|
|Table 34:|DC Voltage Characteristics  ......................................................................................................................................................|70|
|Table 35:|AC Specifications  .........................................................................................................................................................................|71|



©2024 Everspin Technologies 

EMxxLX  v3.2 

4 



<!-- page 5 -->

**_EMxxLX_** 



# **Device Description** 

The EMxxLX is the industry’s first xSPI serial interface persistent memory based on Everspin’s unique industrial STT MRAM technology. It is a high-performance, multiple I/O, SPI-compatible MRAM device featuring a high-speed, low pin count SPI compatible bus interface with a clock frequency of up to 200 MHz and a single 1.8V power supply. The EMxxLX delivers up to 400MBps reads and writes via eight I/O signals with a clock frequency of 200MHz. 

The **EMxxLX** brings a new era of universal memory applications, replacing products such as SRAM, BBSRAM, NVSRAM and overprovisioned NOR devices and targets applications in Industrial Automation, Datacenter, Engineering Emulation, Automotive and Transportation, and Gaming. It is a great choice for the following application usage models: 



©2024 Everspin Technologies 

EMxxLX  v3.2 

5 



<!-- page 6 -->

**_EMxxLX_** 



# BLOCK DIAGRAM 



Figure 1 

LOGIC DIAGRAM 



**OSPI, QSPI, DSPI, XSPI (24-PIN BGA)** 



**QSPI, DSPI, SPI (8-PIN DFN)** 

Figure 2 

©2024 Everspin Technologies 

EMxxLX  v3.2 

6 



<!-- page 7 -->

**_EMxxLX_** 



# **2. Device Pin Assignments** 

# 2.1 24 BALL BGA, 5 X 5 (BALLS DOWN) 



> _Figure 3a Octal SPI with Quad, Dual and Single SPI modes_ 



> _Figure 3b Quad SPI with Single SPI mode_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

7 



<!-- page 8 -->

**_EMxxLX_** 



# 2.2 SIGNAL BALL ASSIGNMENT 

|**TABLE1:** 24 B <br>|ALLBGAXSPI, <br>SPI <br>|OCTAL, QUAD, D <br>MODES<br>|UAL ANDSINGLE<br>|
|---|---|---|---|
|**Ball Location**|**xSPI Signal**|**Ball Location**|**xSPI Signal**|
|**A1**|No Ball|**C4**|IO2 / WP#|
|**A2**|NC|**C5**|RFU|
|**A3**|RFU|**D1**|VDD|
|**A4**|RESET#|**D2**|IO1|
|**A5**|INT#|**D3**|IO0|
|**B1**|RFU|**D4**|IO3|
|**B2**|CK|**D5**|IO4|
|**B3**|VSS|**E1**|IO7|
|**B4**|VDD|**E2**|IO6|
|**B5**|RFU|**E3**|IO5|
|**C1**|VSS|**E4**|VDD|
|**C2**|CS#|**E5**|VSS|
|**C3**<br>**Notes**:|DS|||



- The signals which show a “/” indicates that the pin or ball is dual function 

- • For C4 pin, the write protect feature (WP#) can only be used when device is in single SPI mode • See WP# signal description for detail • Signals IO4, IO5, IO6, IO7 are NC on Quad SPI part number options 

_Table 1_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

8 



<!-- page 9 -->

**_EMxxLX_** 



# 2.3 8-PIN DFN PACKAGE 



_Figure 4_ 

# 2.4 SIGNAL PINOUT IN DFN PACKAGE 

# **TABLE 2:** QUAD, DUAL AND SINGLE SPI MODES 



<!-- Start of picture text -->
Pin Location  Signal<br>1  CS#<br>2  IO1<br>3  WP#/IO2<br>4  VSS<br>5  IO0<br>6  CK<br>7  IO3/RESET#<br>8  VDD<br>Note:<br>1. Pin 7 will be IO3 in Quad SPI mode and RESET#<br>in SPI mode or Dual SPI mode.<br>2. When using SPI and Dual SPI commands, IO3<br>must be driven high before CS# goes high to<br>avoid an unintended reset.<br><!-- End of picture text -->

_Table 2_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

9 



<!-- page 10 -->

**_EMxxLX_** 



# 3. **Signal Descriptions** 

|**Signal**<br>**Name**|**Type**|**Description**|
|---|---|---|
|CS#|Input|**Chip Select.**Bus transactions are initiated with a HIGH to LOW transition. Bus transactions<br>are terminated with a LOW to HIGH transition.|
|CK|Input|**Clock.**Command, Address and Data information is transferred from controller to memory<br>with respect to the rising or falling edge of the CK. The clock is not required to be free<br>running.|
|IO[7:0]|Input / Output|**Data Input/Output.**Command, Address, and Data information is transferred on these<br>signals during Read and Write transactions.|
|DS|Output|**Data Strobe.**Strobe signal to capture read data sent by the memory.  DS is used by a limited<br>set of xSPI commands.|
|VDD|Power Supply|**Power.**|
|VSS|Power Supply|**Ground.**|
|RESET#|Input|**Hardware Reset.**When LOW, the memory will self-initialize and return the device to the<br>ready state. DS and IO[7:0] are placed into the High-Z state when RESET# is LOW. The RESET#<br>signal should not be allowed to float ; an external pull-up should be used on the PCB for a<br>BGA package. IO3 and RESET# share Pin 7 in the DFN package. See section 18.2 for more<br>detail.|
|INT#|Output<br>(Open Drain)|**Interrupt**. When LOW, the memory indicates that an internal event has occurred. This signal<br>is intended to be used as a system level interrupt for the device to indicate that an on-chip<br>event has occurred. INT# is an open-drain output.|
|WP#|Input|**Write Protect**. Locks the status register in conjunction with the enable/disable bit [7] of the<br>status register. This signal does not have internal pull-ups, it cannot be left floating and must<br>be driven, even if neither of WP#/IO2 function is used.|
|RFU|Undefined|**Reserved for Future Use.**The package terminal may be connected to a circuit in the device.<br>The function of the terminal is not currently defined or may be used for an optional signal. It<br>is recommended to leave the terminal open and unconnected to external circuits.|
|NC|No Connection|**No Connection.**The package terminal has no connection to circuits in the device.|
|DNU|Undefined|**Do Not Use.**The package terminal must remain open and unconnected to external circuits.|



_Table 3_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

10 



<!-- page 11 -->

**_EMxxLX_** 



# 4. **xSPI Signal Protocol** 

During the time that CS# is active (LOW) the clock signal (CK) is toggled while command information is first transferred on the data (IO) signals. The clock must be active during any period required for information access or transfer to the memory. The clock continues active during the transfer of read data from the memory to the controller or write data from the controller to the memory. When the controller has transferred the desired amount of data, CS# is driven inactive (HIGH). The period during which CS# is active is called a transaction on the bus. 

While CS# is inactive, the CK is not required to toggle. CK may stop toggling when CS# is LOW as a means of lowering power consumption or inserting delay within a transaction for flow control. CK must always complete at least one rising edge and one falling edge before stopping at LOW. This requirement for a minimum of one rising and falling edge in turn requires that DTR transfers always occur in two transfer increments, e.g., two bytes (word) for 8-bit wide transfers in 8D mode. STR transfers must occur in one byte increments. 

There are up to four phases of activity within each transaction: 

- **Command transfer** from controller to memory 

- **Command Modifier** (Address) transfer from controller to memory 

- **Initial Access Latency** (also used for IO signal direction turn around in a read transaction) 

- **Data transfer** (memory to controller in a read transaction or controller to memory in a write transaction) 

The command transfer occurs at the beginning of every transaction. The command modifier, initial access latency, and data transfer phases are optional, and their presence depends on the protocol mode or command transferred. The number of parallel IO signals used during the command modifier and data phases depends on the current protocol mode or command transferred. The initial access latency phase does not use the IO signals for information transfer. The protocol mode options are described by the data rate and the IO width (number of IO signals) used during the command, command modifier (address), and data phases in the following nomenclature (format): 

## _WR-WR-WR_ where: 

The first _WR_ is the command bit width and rate 

The second _WR_ is the command modifier (address) bit width and rate The third _WR_ is the data bit width and rate. 

The bit width _W_ value may be 1, 2, 4 or 8. R has a value of S for STR, or D for DTR. STR has the same transfer value during the rising and falling edge of a clock cycle. DTR may have different transfer values during the rising and falling edges of each clock. 

1S-1S-1S means that the command is 1-bit wide STR, the command modifier is 1-bit wide STR, and the data is one bit wide STR. 8D-8D-8D means that the command, the command modifier, and data transfers are always 8 bits wide DTR. The EMxxLX allows the option to repeat the command opcode which makes an 8D command look like an 8S command, but it is not required to repeat the command opcode. 

Example protocol modes supported for the EMxxLX are: 

1S-1S-1S; 1S-1D-1D 2S-2S-2S; 2S-2D-2D 4S-4S-4S; 4S-4D-4D 8S-8S-8S; 8D-8D-8D 

**Note** : For full list of opcodes and modes supported by EMxxLX, please refer to section “xSPI Command Opcodes and Modes”. 

The EMxxLX must be configured during the factory initialization to select the mode in which the device will boot following Power-On-Reset (POR). Supported boot modes are x1, x2, x4 or x8.  For example, 8D-8D-8D mode can be made the default 

©2024 Everspin Technologies 

EMxxLX  v3.2 

11 



<!-- page 12 -->

**_EMxxLX_** 



mode if so desired. The controller must determine the default protocol mode of the memory after POR. This may be done through prior knowledge of the system design. The controller may later reconfigure the memory to use other supported modes. 

A protocol mode phase using single bit transfer uses IO[0] to transfer information from controller to memory and IO[1] to transfer information from memory to controller. On each IO, information is placed on the IO line in Most Significant bit (MSb) to Least Significant bit (LSb) order within each u. Sequential command modifier bytes are transferred in highest order to lowest order sequence. Sequential data bytes are transferred in lowest address to highest address order. 

**Table 4: 1S-1S-1S Bit Positions for 4 (and 3) Byte addressing** 

|**IO**|**Command Bits**|**Address Bits**|**Latency**|**Data Byte 0**|**Data Byte 1**|
|---|---|---|---|---|---|
|0|7, 6, 5, 4, 3, 2, 1, 0|31 (23), 30 (22), … 1, 0|X …|X …|X …|
|1|X …|X …|X …|7, 6, 5, 4, 3, 2, 1, 0|7, 6, 5, 4, 3, 2, 1, 0|
|2|X …|X …|X …|X …|X …|
|3|X …|X …|X …|X …|X …|
|4|X …|X …|X …|X …|X …|
|5|X …|X …|X …|X …|X …|
|6|X …|X …|X …|X …|X …|
|7|X …|X …|X …|X …|X …|



_Table 4_ 

A protocol mode phase using two IO signals uses IO[1:0], four IO signals using IO[3:0] and eight IO signals uses IO[7:0]. The LSb of each byte is placed on IO[0] with each higher order bit on the successively higher numbered IO signals. Sequential command modifier bytes are transferred in highest order to lowest order sequence. Sequential data bytes in STR are transferred in lowest address to highest address order. While in 8D mode, sequential data bytes in DTR are transferred only in byte pairs (words) where the byte order depends on the order in which the bytes are written or programmed in that protocol mode. Sequential data bytes are transferred in lowest address to highest address order. In 8D mode, the starting address must be even. 

**Table 5: 8D-8D-8D Bit Positions for 4 (and 3) Byte addressing** 

|**IO**|**Comma**|**nd Bits**||**Addre**|**ss Bits**||**Latency**|**Data W**|**ord 0**|**Data**|**Word 1**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|24|16|8|0|X …|0|0|0|0|
|1|1|1|25|17|9|1|X …|1|1|1|1|
|2|2|2|26|18|10|2|X …|2|2|2|2|
|3|3|3|27|19|11|3|X …|3|3|3|3|
|4|4|4|28|20|12|4|X …|4|4|4|4|
|5|5|5|29|21|13|5|X …|5|5|5|5|
|6|6|6|30|22|14|6|X …|6|6|6|6|
|7|7|7|31|23|15|7|X …|7|7|7|7|



_Table 5_ 

IO signals not in use in a particular phase are undefined and may or may not be driven by the controller or memory, i.e., these signals may be in a high impedance state (floating and indicated by X in the bit position tables). 

**Note** : 

- In single and dual bit transfers the IO[7:2] signals may be high impedance, unless they are dual purpose such as WP# or RESET# in the DFN package 

©2024 Everspin Technologies 

EMxxLX  v3.2 

12 



<!-- page 13 -->

**_EMxxLX_** 



• In quad bit transfers the IO[7:4] signals may be high impedance 

During the data transfer period of a read memory transaction, the Data Strobe (DS) signal is driven by the memory device and transitions edge aligned with the IO signal data transitions. DS is used as an additional output signal with the same timing characteristics as other data outputs but with the guarantee of transitioning with every data bit transferred. The DS signal transitions can be received and internally phase shifted by the controller to be used as an internal read clock/strobe to capture each data bit transferred. Data Strobe is the return of the clock, CK. It is available in all modes and makes it easier to achieve higher clock frequencies. It is required to achieve the maximum clock frequencies. DS goes low when CS# is driven low by the host controller and is driven until CS# is pulled high. DS stays low while the device is receiving command, address, and data. DS will toggle while the device is transmitting data out. 

# **5. Registers** 

The EMxxLX supports various status and configuration registers for device status updates and configuration settings. These registers and their access details are discussed in the following sections. 

# 5.1 STATUS REGISTER 

Read Status Register or Write Status Register commands are used to read from or write to the Status Register bits, respectively. When the status register enable/disable bit (bit 7) is set to 1 and WP# is driven LOW, the status register nonvolatile bits become read-only and the Write Status Register operation will not execute. This hardware-protected mode is exited by driving WP# high. 

||||**Table 6: Status Register**|||
|---|---|---|---|---|---|
|**Bit**|**Name**|**Settings **|**Description**|**Type**|**Notes**|
|0|WIP: Write in<br>progress|0 = Ready<br>1 = Busy|Status bit to determine if a Write Status Register,<br>Write Nonvolatile Configuration Register, Write<br>(Program), CRC, or Erase operation is in progress.<br>This bit is Read Only.|Volatile|2|
|1|WEL: Write enable<br>latch|0 = Clear (Default)<br>1 = Set|The device powers up with the Write enable latch<br>(WEL) cleared to prevent inadvertent Write<br>(Program), or Erase operations. To enable these<br>operations, the Write Enable command must be<br>executed to set this bit. The Write Disable<br>command clears this bit. This bit is Read Only.|Volatile||
|2|BP[0]|Refer to Protected<br>Area tables|Defines memory area to be software protected<br>against Write (Program) or Erase operations. When<br>one or more block protect bits are set to 1, a<br>designated memory area is protected. This bit is<br>writable.|Non-<br>volatile|1|
|3|BP[1]|Refer to Protected<br>Area tables|Defines memory area to be software protected<br>against Write (Program) or Erase operations. When<br>one or more block protect bits are set to 1, a<br>designated memory area is protected. This bit is<br>writable.|Non-<br>volatile|1|
|4|BP[2]|Refer to Protected<br>Area tables|Defines memory area to be software protected<br>against Write (Program) or Erase operations. When<br>one or more block protect bits are set to 1, a<br>designated memory area is protected. This bit is<br>writable.|Non-<br>volatile|1|



©2024 Everspin Technologies 

EMxxLX  v3.2 

13 



<!-- page 14 -->

**_EMxxLX_** 



|5|Top/Bottom|0 = Top (Default)<br>1 = Bottom|Determines whether the top or bottom of the<br>memory array is where the protected area as<br>defined by the block protect bits starts from. This<br>bit is writable.|Non-<br>volatile||
|---|---|---|---|---|---|
|6|BP[3]|Refer to Protected<br>Area tables|Defines memory area to be software protected<br>against Write (Program) or Erase operations. When<br>one or more block protect bits are set to 1, a<br>designated memory area is protected. This bit is<br>writable.|Non-<br>volatile|1|
|7|Status Register Write<br>Enable/Disable|0 = Enabled (Default)<br>1 = Disabled|Used with WP# to enable or disable writing to the<br>status register. This bit is writable.|Non-<br>volatile||



### Notes 

1. All BP bits must be set to 0 for the Bulk Erase command execution 

2. Bit 0 is the inverse of Flag Status Register Bit 7 

_Table 6_ 

### **Status Register Write Enable/Disable  Bit [7]** 

This bit enables write protect for the Status register when set to ’1’ and the write protect (WP#) pin is driven LOW. In this mode, any instruction that changes the status register content is ignored, effectively locking the state of the device. If SR Bit [7] is set to ‘0’, irrespective of the WP# status (LOW or HIGH), status register write protection remains disabled. Refer to Table 7 for the memory and status register protection options. 

### **Top/ Bottom Protection  Bit [5]** 

This bit defines the operation of the Block Protection bits BP3, BP2, BP1, and BP0. This bit controls the starting point of the memory array (from top or bottom) that gets protected by the Block protection bits. 

### **Block Protection (BP3, BP2, BP1 and BP0)  [6,4:2]** 

These bits define the memory array to be write-protected against memory write commands. When one or more of the BP bits is set to  ‘1’, the respective memory address is protected from writes. The Block Protect bits (BP3, BP2, BP1, and BP0) in combination with the T/B bit can be used to protect an address or sector range of the memory array. The size of the range is determined by the value of the BP bits and the upper or lower starting point of the range which is selected by the T/B. Table xx shows EMxxLX protected address range for BP[3:0] bits setting. 

### **Write Enable Latch (WEL)  Bit [1]** 

The WEL bit must be set to 1 to enable write operations to the memory array or registers, as shown in Table xx. This bit is set to ’1’ only by executing the Write Enable (WREN) command. The WEL bit (SR1[1]) automatically clears to ‘0’ after a Write Disable (04h) command is executed. Write (Program) commands will not reset WEL at the completion of the command allowing for back-to-back writes to memory without loading the WREN command again. The WEL bit is volatile and returns to its default ‘0’ state after POR, software RESET, and hardware RESET (via the RESET# pin when available). 

# 5.2 HARDWARE WRITE PROTECTION 

Designated protected blocks as set by SR Bits [6:2], (BP3:0 and TB) are hardware protected with the WP# pin. When the enable/disable bit of the status register is set to 1 and the WP# signal is driven LOW, the status register nonvolatile bits become read-only and the Write Status Register command (01h) operation will not execute. During the extended-SPI protocol with Quad Output Fast Read, Quad IO Fast Read, Octal Output Fast Read, Octal IO Fast Read commands, and with Quad SPI and Octal SPI protocols, this pin function is an input/output with IO2 functionality.  Table 7 below explains how the Write Protection is enabled or disabled with the Status register write enable/disable bit 7, the WEL bit 1 and the WP# signal. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

14 



<!-- page 15 -->

**_EMxxLX_** 



**Table 7: Write Protection** 

|**SR**<br>**Bit[7]**|**WP#**|**WEL**<br>**Bit[1]**|**Protected**<br>**Blocks**|**Unprotected**<br>**Blocks**|**Status Register**|
|---|---|---|---|---|---|
|X|X|0|Protected|Protected|Protected|
|0|X|1|Protected|Writable|Writable|
|1|Low|1|Protected|Writable|Protected|
|1|High|1|Protected|Writable|Writable|



_Table 7_ 

## _Block Protection Settings_ 

Sectors can be protected from Program and Erase operations by setting the TB and BP[3:0] bits corresponding to those sectors as shown in Table 8. If the address of a Write(Program) command is within a protected area, the Write will not execute. Writing will not resume until a new write command is issued with an address in an unprotected area. In other words, a write operation will not skip over a protected area and resume in the next unprotected area. A new Write command is required once an ongoing write aborts. 

**Table 8: Block Protection- Protected Areas** 

||||||**Pr**<br>**forg**|**otected 6**<br>**ivenpart**|**4KB Secto**<br>**density (**|**rs**<br>**Mb)**|
|---|---|---|---|---|---|---|---|---|
|**Top/Bottom**|**BP3**|**BP2**|**BP1**|**BP0**|**64**|**32**|**16**|**8**|
|0|0|0|0|0|**None**|**None**|**None**|**None**|
|0|0|0|0|1|127:127|63:63|31:31|15:15|
|0|0|0|1|0|127:126|63:62|31:30|15:14|
|0|0|0|1|1|127:125|63:61|31:29|15:13|
|0|0|1|0|0|127:124|63:60|31:28|15:12|
|0|0|1|0|1|127:123|63:59|31:27|15:11|
|0|0|1|1|0|127:122|63:58|31:26|15:10|
|0|0|1|1|1|127:121|63:57|31:25|15:9|
|0|1|0|0|0|127:120|63:56|31:24|15:8|
|0|1|0|0|1|127:112|63:48|31:16|15:0|
|0|1|0|1|0|127:96|63:32|31:0|15:0|
|0|1|0|1|1|127:64|63:0|31:0|15:0|
|0|1|1|0|0|127:0|63:0|31:0|15:0|
|0|1|1|0|1|127:0|63:0|31:0|15:0|
|0|1|1|1|0|127:0|63:0|31:0|15:0|
|0|1|1|1|1|127:0|63:0|31:0|15:0|
|**1**|**0**|**0**|**0**|**0**|**None**|**None**|**None**|**None**|
|1|0|0|0|1|0:0|0:0|0:0|0:0|
|1|0|0|1|0|1:0|1:0|1:0|1:0|
|1|0|0|1|1|2:0|2:0|2:0|2:0|
|1|0|1|0|0|3:0|3:0|3:0|3:0|



©2024 Everspin Technologies 

EMxxLX  v3.2 

15 



<!-- page 16 -->

**_EMxxLX_** 



|1|0|1|0|1|4:0|4:0|4:0|4:0|
|---|---|---|---|---|---|---|---|---|
|1|0|1|1|0|5:0|5:0|5:0|5:0|
|1|0|1|1|1|6:0|6:0|6:0|6:0|
|1|1|0|0|0|7:0|7:0|7:0|7:0|
|1|1|0|0|1|15:0|15:0|15:0|15:0|
|1|1|0|1|0|31:0|31:0|31:0|15:0|
|1|1|0|1|1|63:0|63:0|31:0|15:0|
|1|1|1|0|0|127:0|63:0|31:0|15:0|
|1|1|1|0|1|127:0|63:0|31:0|15:0|
|1|1|1|1|0|127:0|63:0|31:0|15:0|
|1|1|1|1|1|127:0|63:0|31:0|15:0|



_Table 8_ 

# 5.3 FLAG STATUS REGISTER 

The Read Flag Status Register command is used to read the Flag status register bits. Flag status registers bits are volatile and are reset to zero on power-up. They are set and reset automatically by the internal controller. Error bits must be cleared through the Clear Flag Status Register command. For Soft Reset, Hardware Reset and Reset with signal sequence, bits 1, 3, 4, and 5 are set to “0”; bit 7 is set to “1”. In a Reset with signal sequence, bit 0 is set to “0”. 

|||**Table 9: Fl**|**ag Status Register**||
|---|---|---|---|---|
|**Bit**|**Name**|**Settings **|**Description**|**Type**|
|0|Addressing|0 = 3-byte addressing<br>1 = 4-byte addressing|Indicates whether 3-byte or 4-byte address mode is<br>enabled.|Status|
|1|Protection|0 = Clear<br>1 = Protection Error|Indicates whether an Erase or Program operation has<br>attempted to modify the protected array sector as<br>configured by Block Protection, or whether a OTP Write<br>operation has attempted to access the locked OTP space.|Error|
|2|Reserved||||
|3|CRC|0 = Clear<br>1 = Failure|Indicates that the Computed CRC did not match the user<br>provided CRC Code.|Error|
|4|Write (Program)|0 = Clear<br>1 = Program Error|Indicates whether a Program operation has succeeded or<br>failed. A PROGRAM or OTP Write operation will fail if<br>WREN  is not set.|Error|
|5|Erase|0 = Clear<br>1 = Erase Error|Indicates whether an Erase operation has succeeded or<br>failed. An Erase operation will fail if WREN is not set.|Error|
|6|Reserved||||
|7|Write (Program) or<br>Erase|0 = Busy<br>1 = Ready|Indicates whether one of the following command cycles is<br>in progress: Write Status Register, Write Nonvolatile<br>Configuration Register, Write (Program), Erase, or CRC<br>Check.|Status|



_Table 9_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

16 



<!-- page 17 -->

**_EMxxLX_** 



# 5.4 CONFIGURATION REGISTERS 

The memory configuration is set by an internal configuration register that is not directly accessible to users. The user can change the default configuration at power up by using the WRITE NONVOLATILE CONFIGURATION REGISTER. Information from the nonvolatile configuration register overwrites the internal configuration register during power on or after a reset. The user can change the configuration during device operation using the WRITE VOLATILE CONFIGURATION REGISTER command. Information from the volatile configuration registers overwrite the internal configuration register immediately after the WRITE command completes. 



<!-- Start of picture text -->
Nonvolatile Configuration Register  Volatile Configuration Register<br>Register download is executed only during  Register download is executed after a WRITE<br>the power-on phase or after a reset,  VOLATILE CONFIGURATION REGISTER command,<br>overwriting configuration register settings  overwriting configuration register settings on the<br>on the internal configuration register. internal configuration register.<br>Internal Configuration Register<br>Device Behavior<br><!-- End of picture text -->

©2024 Everspin Technologies 

EMxxLX  v3.2 

17 



<!-- page 18 -->

**_EMxxLX_** 



# 5.5 NONVOLATILE CONFIGURATION REGISTER 

|**Nonvolatile**<br>**Address**<sup>**5**</sup>|**Configur**<br>**0x0000**|**ation Register 0**<br>||||
|---|---|---|---|---|---|
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|I/O Mode|1111_1111 (0xFF) <br>1101_1111 (0xDF) <br>1111_1101 (0xFD) <br>1101_1101 (0xDD) <br>1111_1011 (0xFB) <br>1101_1011 (0xDB)<br>1110_1011 (0xEB) <br>1100_1011 (0xCB)<br>1110_0111 (0xE7) <br>1100_0111 (0xC7)<br>1011_0111 (0xB7)<br>1001_0111 (0x97)<br>Others|SPI with DS (default)<br>SPI w/o DS<br>Dual with DS<br>Dual w/o DS<br>Quad with DS<br>Quad w/o DS<br>Quad DTR with DS<br>Quad DTR w/o DS<br>Octal DTR with DS<br>Octal DTR w/o DS<br>Octal with DS<br>Octal w/o DS<br>SPI with DS (same as default)|6|
|**Nonvolatile**|**Configur**|**ation Register 1**||||
|**Address**|**0x0001**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Dummy Cycle<br>Configuration|0000_0000<br>0000_0001<br>0000_0010<br>. . .<br>0000_1111<br>0001_0000<br>. . .<br>0001_1110<br>0001_1111<br>1111_1111|16 Dummy cycles<br>1 Dummy cycles<br>2 Dummy cycles<br>...<br>15 Dummy cycles<br>16 Dummy cycles<br>...<br>30 Dummy cycles<br>31 Dummy cycles<br>16 Dummy cycles||
||||Others|<br>16 Dummy cycles (default)||
|**Nonvolatile**<br>**Address**|**Configur**<br>**0x0002**|**ation Register 2**<br>||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Reserved|TBD|||
|**Nonvolatile**<br>|**Configur**<br>|**ation Register 3**<br>||||
|**Address**|**0x0003**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Driver Strength<br>Configuration|1111_1111<br>1111_1110<br>1111_1101<br>1111_1100|50 Ohm (default)<br>35 Ohm<br>25 Ohm<br>18 Ohm||
|**Nonvolatile**<br>**Address**|**Configur**<br>**0x0004**|**ation Register 4**<br>|Others|50 Ohm||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:4|RW|TBD|TBD|||
|3:0|RW|DS Delay|1111<br>1110<br>1101|Zero added DS delay (Default)<br>100pS added DS delay<br>200pS added DS delay|7|
||||...<br>0000|...<br>1500pS added DS delay||
|**Nonvolatile**|**Configur**|**ation Register 5**||||



©2024 Everspin Technologies 

EMxxLX  v3.2 

18 



<!-- page 19 -->

**_EMxxLX_** 



|**Address**|**0x000**|**5**||||
|---|---|---|---|---|---|
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Address Mode|1111_1111<br>1111_1110|3-Byte Address (default)<br>4-Byte Address||
||||Others|3-Byte Address||
|**Nonvolatile**|**Configur**|**ation Register 6**||||
|**Address**|**0x000**|**6**||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Execute-in-Place<br>(XIP) Configuration|1111_1111<br>1111_1110|XIP Disabled (default)<br>XIP Enable- Activated if XIP confirmation bit = 0 during FAST READ<br>|1|
||||11111100|XIP BOOT- Activated at boot time||
|**Nonvolatile**<br>|**Configur**|**ation Register 7**|_<br>Others|XIP Disabled||
|**Address**|**0x000**|**7**||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Wrap Configuration|1111_1111<br>1111_1110<br>1111_1101<br>1111_1100|Continuous (default)<br>64-byte wrap<br>32-byte wrap<br>16-byte wrap|2|
||||Others|Continuous||
|**Nonvolatile**|**Configur**|**ation Register 8**||||
|**Address**|**0x000**|**8**||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7|RW|Erase Bit Value|1 = Erase with ‘1’<br>(default)<br>0 = Erase with ‘0’|Determines data state for Erase operations||
|6:2|RW|TBD|TBD|||
|1|RW|RPE|1 = Reset Pin Enabled<br>(default)<br>0 = Reset Pin Disabled|When the Reset pin is disabled, the RESET # will be ignored. The<br>device may be reset with Soft Reset or JESD Reset. In the DFN<br>package option, the RESET# signal is disabled automatically when<br>the device is configured inQuad SPI mode(Register 0).||
|0<br>**Nonvolatile**|RW<br>**Configur**|Write mode<br>**ation Registers 9,10,11**|1 = Persistent Memory<br>Mode enabled<br>(default)<br>0 = Persistent memory<br>mode disabled<br>**,12**|Persistent Memory mode or NOR Flash like mode is selected with<br>this bit.|3|
|**Address**|**0x000**|**9, 0x000A, 0x000B, 0x0**|**00C**|||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Non Volatile user<br>scratch register|1111_1111 (default)|Four 8 bit registers available for storing any user data.<br>_Table 10_|4|



Notes: 

1. Only FAST READ (0Bh) supports XIP operation. 

2. Wrap length affects READ commands. WRITE wrap length will depend on the mode selected in Register 8. 

3. Used to select the mode for writing to the memory 

4. These registers may be used for storing user configuration data that will be used for device recovery if necessary. 

5. Register addresses may be either 3-byte or 4-byte depending on user selection 

6. When configuring the I/O mode, the unused IO’s, if any, will be left floating. For example, if a user intends to use only the Quad SPI mode in a Octal SPI in a BGA package, IO4-7 will be floating or Hi-Z. These balls may be left unconnected on the PCB if the user never intends to activate Octal SPI. If an Octal SPI BGA device is configured in the Dual SPI mode, IO0 and IO1 will be active and the remaining IO’s will be floating except for ball C4 which is dual purpose IO2/WP#. A Quad SPI device in a DFN package which is configured as Dual SPI will use IO2 and IO3 as WP# and RESET# respectively. Similarly, if the same device is configured as SPI mode, IO1 is left floating. Octal configurations in Quad SPI only devices are not valid. 

7. Register 4 provides the user a means to tune the DS timing to compensate for PCB layout or system timing offsets to better align with valid data output on the IO’s. The amount of delay is configurable. Actual delay can vary +/- 30ps per delay setting, the user should confirm the data strobe timing once it is configured. (Refer to App Note EST 3001 for a tuning sequence) 

©2024 Everspin Technologies 

EMxxLX  v3.2 

19 



<!-- page 20 -->

**_EMxxLX_** 



# 5.6 VOLATILE CONFIGURATION REGISTER 

|**Volatile Co**|**nfiguration R**|**egister 0**||||
|---|---|---|---|---|---|
|**Address**<sup>**4**</sup>|**0x0000**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|I/O Mode|1111_1111 (0xFF)<br>1101_1111 (0xDF)<br>1111_1101 (0xFD)<br>1101_1101 (0xDD)<br>1111_1011 (0xFB)<br>1101_1011 (0xDB)<br>1110_1011 (0xEB)<br>1100_1011 (0xCB)<br>1110_0111 (0xE7)<br>1100_0111 (0xC7)<br>1011_0111 (0xB7)<br>|SPI with DS (default)<br>SPI w/o DS<br>Dual with DS<br>Dual w/o DS<br>Quad with DS<br>Quad w/o DS<br>Quad DTR with DS<br>Quad DTR w/o DS<br>Octal DTR with DS<br>Octal DTR w/o DS<br>Octal with DS<br>|5|
||||1001_0111 (0x97)|Octal w/o DS||
|**Volatile Co**|**nfiguration R**|**egister 1**|Others|SPI with DS (same as default)||
|**Address**|**0x0001**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Dummy Cycle<br>Configuration|0000_0000<br>0000_0001<br>0000_0010<br>. . .<br>0000_1111<br>0001_0000<br>. . .<br>0001_1110<br>0001_1111|16 Dummy cycles<br>1 Dummy cycles<br>2 Dummy cycles<br>...<br>15 Dummy cycles<br>16 Dummy cycles<br>...<br>30 Dummy cycles<br>31 Dummy cycles||
|**Volatile Co**<br>**Address**|**nfiguration R**<br>**0x0002**|**egister 2**|Others|16 Dummycycles||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0<br>**Volatile Co**|RW<br>**nfiguration R**|Reserved<br>**egister 3**|TBD|||
|**Address**|**0x0003**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Driver Strength<br>Configuration|1111_1111<br>1111_1110<br>1111_1101|50 Ohm (default)<br>35 Ohm<br>25 Ohm||
||||1111_1100<br>|18 Ohm<br>||
|**Volatile Co**|**nfiguration R**|**egister 4**|Others|50 Ohm||
|**Address**|**0x0004**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:4|RW|Reserved|TBD|||
|3:0|RW|DS Delay|1111<br>1110<br>1101|Zero added DS delay (Default)<br>100pS added DS delay<br>200pS added DS delay|7|
||||...<br>0000|...<br>1500pS added DS delay||
|**Volatile Co**|**nfiguration R**|**egister 5**||||
|**Address**|**0x0005**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|



©2024 Everspin Technologies 

EMxxLX  v3.2 

20 



<!-- page 21 -->

**_EMxxLX_** 



|7:0|RW|Address Mode|1111_1111<br>1111_1110<br>Others|3-Byte Address (default)<br>4-Byte Address<br>3-Byte Address||
|---|---|---|---|---|---|
|**Volatile Co**<br>|**nfiguration Re**<br>|**gister 6**||||
|**Address**|**0x0006**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0<br>**Volatile Co**<br>|RW<br>**nfiguration Re**<br>|Execute-in-Place<br>(XIP) Configuration<br>**gister 7**|1111_1111<br>1111_1110<br>Others|XIP Disabled (default)<br>XIP Enable- Activated if XIP confirmation bit = 0<br>during FAST READ<br>XIP Disabled|1|
|**Address**|**0x0007**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:0|RW|Wrap Configuration|1111_1111<br>1111_1110<br>1111_1101<br>1111_1100<br>Oth|Continuous (default)<br>64-byte wrap<br>32-byte wrap<br>16-byte wrap<br>Cti|2|
|**Volatile Co**<br>|**nfiguration Re**<br>|**gister 8**|ers|onnuous||
|**Address**|**0x0008**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7|RW|Erase Bit Value|1 = Erase with ‘1’ (default)<br>0 = Erase with ‘0’|Determines data state for Erase operations||
|6:3|RW|Reserved||||
|2|RW|OTP Unlock|1 = OTP Lock Enable (default)<br>0 = OTP Lock Disable”|When OTP Lock is disabled this will override the<br>OTP Lock Byte settingand unlock the OTP array.||
|1|RW|RPE|1 = Reset Pin Enabled (default)<br>0 = Reset Pin Disabled|When the Reset pin is disabled, the RESET # will<br>be ignored. The device may be reset with Soft<br>Reset or JESD Reset. In the DFN package option,<br>the RESET# signal is disabled automatically when<br>the device is configured in Quad SPI mode<br>(Register 0).||
|0|RW|Write mode|1 = Persistent Memory Mode enabled<br>(default)<br>0 = Persistent memory mode disabled<br>_Table 11_|Persistent Memory mode or NOR Flash like<br>mode is selected with this bit.|3|



Notes: 

1. Only FAST READ (0Bh) supports XIP operation. 

2. Wrap length affects READ commands. WRITE wrap length will depend on the mode selected in Register 8. 

3. Used to select the mode for writing to the memory 

4. Register addresses may be either 3-byte or 4-byte depending on user selection 

5. When, configuring the I/O mode, the unused IO’s, if any, will be left floating. For example, if a user intends to use only the Quad SPI mode in a Octal SPI in a BGA package, IO4-7 will be floating or Hi-Z. These balls may be left unconnected on the PCB is the user never intends to activate Octal SPI. If an Octal SPI BGA device is configured in the Dual SPI mode, IO0 and IO1 will be active and the remaining IO’s will be floating except for ball C4 which is dual purpose IO2/WP#. A Quad SPI device in a DFN package which is configured as Dual SPI will leave IO2 and IO3 as WP# and RESET# respectively. Similarly, if the same device is configured as SPI mode, IO1 is left floating. Octal configurations are not valid in Quad SPI only devices. 

6. Default settings are power-on reset defaults. 

7. Register 4 provides the user a means to tune the DS timing to compensate for PCB layout or system timing offsets to better align with valid data output on the IO’s. The amount of delay is configurable. Actual delay can vary +/- 30ps per delay setting, the user should confirm the data strobe timing once it is configured. (Refer to App Note EST 3001 for a tuning sequence) 

©2024 Everspin Technologies 

EMxxLX  v3.2 

21 



<!-- page 22 -->

**_EMxxLX_** 



# 5.7 INTERRUPT MASK AND STATUS REGISTERS, INT# SIGNAL FUNCTION 

The Interrupt Mask and Status registers are used together to provide the status of certain operations or indicate errors in particular operations as shown in the tables below. The mask register provides the option to receive an interrupt signal on the INT# pin. INT# is intended to be used as a system level interrupt for the device to indicate that an on-chip event has occurred. The INT# is available on the 24-ball BGA, ball A5, but is not available on the 8-DFN package.  Power on errors, CRC completion and Erase completion are the operations that generate a status bit. CRC completion and Erase completion result in an output signal, INT#, if the Interrupt Mask register bits 1 and 0 respectively are set to 1 (enabled). The INT# signal will go from a high impedance state to a low state. If a Configuration error occurs, INT# will be enabled regardless of the Interrupt Mask settings. The Interrupt registers are accessed with the Read Volatile Configuration Register and Write Volatile Configuration Register commands. 

|**Interrupt M**|**ask**|||||
|---|---|---|---|---|---|
|**Address**|**0x000F**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:2|RO|Reserved|0|||
|1|RW|CRC Done|0 = Masked (default)<br>1 = Interrupt enabled|Enable interrupt on CRC Check Done||
|0|RW|Erase Done|0 = Masked (default)<br>1 = Interrupt enabled|Enable interrupt on Erase Done<br>0=Masked – no interrupt is generated||



_Table 12_ 

|**Interrupt S**|**tatus**|||||
|---|---|---|---|---|---|
|**Address**|**0x0010**|||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:3|RO|Reserved|0|||
|2|RW1C|Power On Error|0 = No error<br>1 = Error|Read, Write 1 to Clear, Power on error|1,2|
|1|RW1C|CRC Done|0 = Not done (Reset Value)<br>1 = Done|Read, Write 1 to Clear||
|0|RW1C|Erase Done|0 = Not done (Reset Value)<br>1 = Done|Read, Write 1 to Clear||



_Table 13_ 

Note 1. Bit 2 does not get reset with a hardware reset. 

Note 2. For detailed information on the device recovery procedure when a Power On Error is detected, please refer to Everspin Application Note EST 3000, _Device Initialization, Power Cycle, System Reset and Recovery for EMxxLX MRAM._ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

22 



<!-- page 23 -->

**_EMxxLX_** 



# 5.8 DEVICE FACTORY INITIALIZATION MODE 

The EMxxLX device must go through an initialization after system or PCB assembly. This is required to ensure that critical internal device settings are in their proper state after solder reflow processing. The DFIM register is used to enter and exit Device Factory Initialization  (DFIM) mode. To enter DFIM mode, use the Write Volatile Configuration Register (81) command, address 1Eh, with the Manufacturer ID code 6Bh. To exit DFIM mode, write the DFIM register with any data other than 6Bh. This will disable DFIM mode. Please refer to Sec. 17, Initialization Requirements, for details on proper device initialization procedure. 

|||||**DFIM Register**||
|---|---|---|---|---|---|
|**Addr**|**ess**|**0x001E**||||
|**Bit**||**Name**|**Settings **|**Description**|**Notes**|
|7:0|RW|DFIM|0 = (Reset Value)|**Device Factory Initialize Mode:**<br>Write 0x6B to enter mode ( Manufacturer ID)<br>Read back 0x00 DFIM Not Enabled<br>Read back 0x01 DFIM Enabled|Volatile|



_Table 14_ 

# 5.9 TUNING DATA PATTERN REGISTER 

|||||**TDP Register**||
|---|---|---|---|---|---|
|**Address**|**0x00**|**00 - 0x003F**||||
|**Byte Addr**|**Op**|**Name**|**Settings **|**Description**|**Notes**|
|0x00|RW|TDP Byte 0|0xDE|Power On Reset Value||
|0x01|RW|TDP Byte 1|0x7B|Power On Reset Value||
|0x02|RW|TDP Byte 2|0x7F|Power On Reset Value||
|...|RW|...|...|Power On Reset Value||
|0x3E|RW|TDP Byte 62|0x0F|Power On Reset Value||
|0x3F|RW|TDP Byte 63|0xFF|Power On Reset Value||



_Table 15_ 

Note: For full contents and description of TDP, refer to Everspin Application Note EST 3001. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

23 



<!-- page 24 -->

**_EMxxLX_** 



# 5.10 SUPPORTED CLOCK FREQUENCIES 

The table below specifies the maximum frequency supported for a given number of dummy cycles. The number of dummy cycles is set in the Nonvolatile Configuration Register 1 and the Volatile Configuration Register 1. The frequency supported is shown in the respective tables below for STR and DTR modes. The maximum frequency is fCK1=133MHz for SPI, Dual SPI and Quad SPI mode. The maximum frequency is fCK2=200MHz for Octal SPI mode. There is also a frequency limitation in the DFN package, which is offered for a Quad SPI version of the EMxxLX as a result of not having a data strobe signal available. As a result, the maximum frequency in the DFN package is fCK = 133MHz when configured in for STR operation and fCK = 90MHz when configured for DTR operation. 

|||**STR – Freq**|**uency (MHz**|**)**||
|---|---|---|---|---|---|
|**Dummy**<br>**Clock Cycles**|**SPI**<br>1s-1s-1s<br>1s-1s-2s<br>1s-1s-4s<br>1s-1s-8s|**DUAL**<br>1s-2s-2s<br>2s-2s-2s|**QUAD**<br>1s-4s-4s<br>4s-4s-4s|**Octal**<br>1s-8s-8s*<br>8s-8s-8s|**OpCode**|
|0|66|~|~|~|READ|
|1|83|~|~|~|READ FAST|
|2|100|16|16|~|READ FAST|
|3|116|33|33|33|READ FAST|
|4|133|50|50|50|READ FAST|
|5|133|66|66|66|READ FAST|
|6|133|83|83|83|READ FAST|
|7|133|100|100|100|READ FAST|
|8|133|116|116|116|READ FAST|
|9|133|133|133|133|READ FAST|
|10|133|133|133|150|READ FAST|
|11|133|133|133|166|READ FAST|
|12|133|133|133|183|READ FAST|
|13|133|133|133|200|READ FAST|
|14|133|133|133|200|READ FAST|
|15|133|133|133|200|READ FAST|
|16|133|133|133|200|READ FAST|



* Limited to 133MHz maximum 

_Table 16_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

24 



<!-- page 25 -->

**_EMxxLX_** 



|||**DTR – Freq**|**uency (MHz**|**)**||
|---|---|---|---|---|---|
|**Dummy**<br>**Clock Cycles**|**SPI**<br>1s-1d-1d<br>1s-1d-2d<br>1s-1d-4d<br>1s-1d-8d|**DUAL**<br>1s-2d-2d<br>2d-2d-2d|**QUAD**<br>1s-4d-4d<br>4d-4d-4d|**Octal**<br>1s-8d-8d*<br>8d-8d-8d|**OpCode**|
|0|~|~|~|~||
|1|~|~|~|~||
|2|16|16|16|~|READ FAST|
|3|33|33|33|33|READ FAST|
|4|50|50|50|50|READ FAST|
|5|66|66|66|66|READ FAST|
|6|83|83|83|83|READ FAST|
|7|90|90|90|100|READ FAST|
|8|90|90|90|116|READ FAST|
|9|90|90|90|133|READ FAST|
|10|90|90|90|150|READ FAST|
|11|90|90|90|166|READ FAST|
|12|90|90|90|183|READ FAST|
|13|90|90|90|200|READ FAST|
|14|90|90|90|200|READ FAST|
|15|90|90|90|200|READ FAST|
|16|90|90|90|200|READ FAST|



* Limited to 133MHz maximum 

_Table 17_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

25 



<!-- page 26 -->

**_EMxxLX_** 



# **6. Register Operations** 

# 6.1 READ REGISTER OPERATIONS 

|**Command**|**Description**|**Note**|
|---|---|---|
|Read Status Register (05h)|Can be read continuously and at any time, including during<br>a PROGRAM, ERASE, or WRITE operation. If one of these||
|Read Flag Status Register (70h)|operations is in progress, checking the write in progress bit<br>(bit 0 in Status register) or P/E bit (bit 7 in Flag Status<br>register)is recommended before executinga new command.||
|Read Nonvolatile Configuration Register (B5h) and<br>Read Volatile Configuration Register (85h)|Register contents of the selected register address will be<br>output on the IO’s. If an address is selected beyond the<br>defined address range of the configuration register, the data<br>output will be undefined.||
|Read General Purpose Register (96h)|The GPR will contain CRC results. Refer to the CRC Operation<br>section.||



_Table 18_ 





_Figure 5: Read Status Register with STR_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

26 



<!-- page 27 -->

**_EMxxLX_** 





_Figure 6: Read Nonvolatile/Volatile Register_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

27 



<!-- page 28 -->

**_EMxxLX_** 





_Figure 7: READ General Purpose Register with STR_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

28 



<!-- page 29 -->

**_EMxxLX_** 



# 6.2 WRITE REGISTER OPERATIONS 

|**Command**|**Description**|**Note**|
|---|---|---|
|Write Status Register (01h)|The WRITE STATUS REGISTER command writes new values<br>to status register bits 7:2, enabling software data protection.|1,2|
|Write Nonvolatile Configuration Register (B1h)|The status register can also be combined with the WP#<br>signal to provide hardware data protection. This command<br>has no effect on status register bits 1:0.<br>For the WRITE STATUS REGISTER and WRITE NONVOLATILE<br>CONFIGURATION REGISTER commands, when the operation<br>is in progress, the write in progress bit is set to 1. The write<br>enable latch bit is not cleared to 0, whether the operation is<br>successful or not. The status register and flag status register<br>can be polled for the operation status.<br>When the operation completes, the write in progress bit is<br>cleared to 0,whether the operation is successful or not.||
|Write Volatile Configuration Register (81h)|Because register bits are volatile, change to the bits is<br>immediate. Reserved bits are not affected bythis command.|2|
|Clear Flag Status Register (50h)|This command will clear ( set to “0”) flag status register bits<br>5, 4,3 and 1 in the Flag Status Register. These are the error<br>status bits.||
||_Table 19_||



## Notes: 

1. The WRITE NONVOLATILE CONFIGURATION REGISTER operation must have input data starting from the least significant byte. 

2. When writing to the Status Register or to a single Nonvolatile or Volatile Configuration Register in 8d mode (DTR), the first data byte gets written into the register. When writing to the Nonvolatile and Volatile registers, the register address will increment sequentially if the write operation is continued, and additional bytes will be written. This may be different than some NOR Flash devices in which only one byte of data is accepted. In the case of Nonvolatile and Volatile configuration register writes, in 8d mode, the start address must be even. Single writes with odd addresses are not allowed. In 8d mode, two data bytes will be written, it is not possible to write only one byte. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

29 



<!-- page 30 -->



<!-- Start of picture text -->
EMxxLX<br><!-- End of picture text -->





<!-- Start of picture text -->
Figure 8:  Write Status Register<br><!-- End of picture text -->



_Figure 9:  Write Nonvolatile/Volatile Register_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

30 



<!-- page 31 -->

**_EMxxLX_** 



## **7. Memory Organization** 

||**Sector**|||**Address**|**Range**|
|---|---|---|---|---|---|
|**Capacity**|**(64KB)**|**Subsector(32KB)**|**Subsector(4KB)**|**Start**|**End**|
|64Mb|127|255|2047<br>⋮|007F F000h<br>⋮|007F FFFFh<br>⋮|
||||2040|007F 8000h|007F 8FFFh|
|||254|2039<br>⋮|007F 7000h<br>⋮|007F 7FFFh<br>⋮|
||⋮|⋮|<br>2032<br>⋮|<br>007F 0000h<br>⋮|<br>007F 0FFFh<br>⋮|
|32Mb|<br>63|<br>127|<br>1023<br>⋮|<br>003F 0000h<br>⋮|<br>003F FFFFh<br>⋮|
||||<br>1016|<br>003F 8000h|<br>003F 8FFFh|
|||126|1015<br>⋮|003F 7000h<br>⋮|003F 7FFFh<br>⋮|
||⋮|⋮|<br>1008<br>⋮|<br>003F 0000h<br>⋮|<br>003F 0FFFh<br>⋮|
|16Mb|31|63|511<br>⋮|001F F000h<br>⋮|001F FFFFh<br>⋮|
||||<br>504|<br>001F 8000h|<br>001F 8FFFh|
|||62|503<br>⋮|001F 7000h<br>⋮|001F 7FFFh<br>⋮|
||⋮|⋮|<br>496<br>⋮|<br>001F 0000h<br>⋮|<br>001F 0FFFh<br>⋮|
|8Mb|15|31|255<br>⋮|000F F000h<br>⋮|000F FFFFh<br>⋮|
||||<br>248|<br>000F 8000h|<br>000F 8FFFh|
|||30|247<br>⋮|000F 7000h<br>⋮|000F 7FFFh<br>⋮|
||⋮|⋮|<br>240<br>⋮|<br>000F 0000h<br>⋮|<br>000F 0FFFh<br>⋮|
||<br>0|<br>1|<br>15<br>⋮|<br>0000 F000h<br>⋮|<br>0000 FFFFh<br>⋮|
||||<br>8|<br>0000 8000h|<br>0000 8FFFh|
|||0|7<br>⋮|0000 7000h<br>⋮|0000 7FFFh<br>⋮|
||||<br>0|<br>0000 0000h|<br>0000 0FFFh|



_Table 20_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

31 



<!-- page 32 -->

**_EMxxLX_** 



## **8. xSPI Command Opcodes and Modes** 

All commands, addresses and data are shifted in and out of the device, beginning with the most significant bit on the first rising edge of CK after CS# is driven low. Command sequences starts with a one-byte command code. The one-byte command code is shifted into the device on the IO’s, and each bit is latched on the rising edges of CK. Depending on the command, this might be followed by address bytes or by data bytes, or by both or neither. CS# must be driven high after the last bit of the command sequence has been completed. For the commands Read, Read Fast, Read Status Register or Deep Power-Down exit, and Read ID, the shifted-in command sequence is followed by a data-out sequence. All read instructions can be completed after any bit of the dataout sequence is being shifted out, then CS# must be driven high to return to deselected status. 

**Table 21: Instruction Command Table** 

|**INSTRUCTION COMMAND SET**|**OPCODE**<br>**HEX **|**SPI**<br>**MODE**|**DSPI**<br>**MODE**|**QS**<br>**MO**|**PI**<br>**DE**|**O**<br>**M**|**SPI**<br>**ODE**|**ADDRESS**<br>**BYTES**<sup>**6**</sup>|**LATENCY**<sup>**4**</sup><br>**DMMY**|
|---|---|---|---|---|---|---|---|---|---|
||**() **|||**STR**|**DTR**|**STR**|**DTR**||**(U)**|
|RESET Enable|66|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|RESET Memory|99|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|Read ID|9E|1s-0-1s|~|~|~|8s-0-8s|8d-0-8d|0|0,0,0,8|
|Read ID|9F|1s-0-1s|~|~|~|8s-0-8s|8d-0-8d|0|0,0,0,8|
|Read ID MIO|AF|1s-0-1s|2s-0-2s|4s-0-4s|4s-0-4d|8s-0-8s|8d-0-8d|0|0,0,0,8|
|Read|03|1s-1s-1s|~|~|~|~|~|3/4|0|
|Read Fast (XIP)|0B|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|DCC|
|Read Fast Dual Output|3B|1s-1s-2s|2s-2s-2s|~|~|~|~|3/4|DCC|
|Read Fast Dual I/O|BB|1s-2s-2s|2s-2s-2s|~|~|~|~|3/4|DCC|
|Read Fast Quad Output|6B|1s-1s-4s|~|4s-4s-4s|4s-4d-4d|~|~|3/4|DCC|
|Read Fast Quad I/O|EB|1s-4s-4s|~|4s-4s-4s|4s-4d-4d|~|~|3/4|DCC|
|Read Fast DTR|0D|1s-1d-1d|2s-2d-2d|4s-4d-4d|4s-4d-4d|~|~|3/4|DCC|
|Read Fast Dual Output DTR|3D|1s-1d-2d|2s-2d-2d|~|~|~|~|3/4|DCC|
|Read Fast Dual I/O DTR|BD|1s-2d-2d|2s-2d-2d|~|~|~|~|3/4|DCC|
|Read Fast Quad Output DTR|6D|1s-1d-4d|~|4s-4d-4d|4s-4d-4d|~|~|3/4|DCC|
|Read Fast Quad I/O DTR|ED|1s-4d-4d|~|4s-4d-4d|4s-4d-4d|~|~|3/4|DCC|
|Read Word Quad I/O (no DTR)|E7|1s-4s-4s|~|4s-4s-4s|~|~|~|3/4|4|
|Read Fast Octal Output<sup>3</sup>|8B|1s-1s-8s|~|~|~|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|DCC|
|Read Fast Octal I/O<sup>3</sup>|CB|1s-8s-8s|~|~|~|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|DCC|
|Read Fast Octal Output DTR<sup>3</sup>|9D|1s-1d-8d|~|~|~|8d-8d-8d|8d-8d-8d|3/4<sup>5</sup>|DCC|
|Read Fast Octal I/O DTR<sup>3</sup>|FD|1s-8d-8d|~|~|~|8d-8d-8d|8d-8d-8d|4<sup>5</sup>|DCC|
|Read 4-byte address|13|1s-1s-1s|~|~|~|~|~|4|0|
|Read Fast 4-byte address|0C|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|4<sup>5</sup>|DCC|
|Read Fast Dual Output 4-Byte Address|3C|1s-1s-2s|2s-2s-2s|~|~|~|~|4|DCC|
|Read Fast Dual I/O 4-byte Address|BC|1s-2s-2s|2s-2s-2s|~|~|~|~|4|DCC|
|Read Fast Quad Output 4-Byte Address|6C|1s-1s-4s|~|4s-4s-4s|4s-4d-4d|~|~|4|DCC|
|Read Fast Quad I/O 4-Byte Address|EC|1s-4s-4s|~|4s-4s-4s|4s-4d-4d|~|~|4|DCC|
|Read Fast DTR 4-Byte Address|0E|1s-1d-1d|2s-2d-2d|4s-4d-4d|4s-4d-4d|~|~|4|DCC|
|Read Fast Dual I/O DTR 4-Byte Address|BE|1s-2d-2d|2s-2d-2d|~|~|~|~|4|DCC|
|Read Fast Quad I/O DTR 4-Byte Address|EE|1s-4d-4d|~|4s-4d-4d|4s-4d-4d|~|~|4|DCC|
|Read Fast Octal Output 4-byte address<sup>3</sup>|7C|1s-1s-8s|~|~|~|8s-8s-8s|8d-8d-8d|4<sup>5</sup>|DCC|
|Read Fast Octal I/O 4-byte address<sup>3</sup>|CC|1s-8s-8s|~|~|~|8s-8s-8s|8d-8d-8d|4<sup>5</sup>|DCC|
|Write Enable|06|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|



©2024 Everspin Technologies 

EMxxLX  v3.2 

32 



<!-- page 33 -->



# **_EMxxLX_** 

|**I**|**OPCODE**|**SPI**|**DSPI**|**QS**<br>**MO**|**PI**<br>**DE**|**O**<br>**M**|**SPI**<br>**ODE**|**ADDRESS**|**LATENCY**<sup>**4**</sup>|
|---|---|---|---|---|---|---|---|---|---|
|**NSTRUCTION COMMAND SET**|**(HEX) **|**MODE**|**MODE**|||||**BYTES**<sup>**6**</sup>|**(DUMMY)**|
|||||**STR**|**DTR**|**STR**|**DTR**|||
|Write Disable|04|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|Read Status Register|05|1s-0-1s|2s-0-2s|4s-0-4s|4s-0-4d|8s-0-8s|8d-0-8d|0|0,0,0,8|
|Read FlagStatus Register|70|1s-0-1s|2s-0-2s|4s-0-4s|4s-0-4d|8s-0-8s|8d-0-8d|0|0,0,0,8|
|Read Nonvolatile Configuration Register|B5|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0,0,0,8|
|Read Volatile Configuration Register|85|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0,0,0,8|
|Read General Purpose Register|96|1s-0-1s|2s-0-2s|4s-0-4s|4s-0-4d|8s-0-8s|8d-0-8d|0|8,8,8,8|
|Write Status Register<sup>1</sup>|01|1s-0-1s|2s-0-2s|4s-0-4s|4s-0-4d|8s-0-8s|8d-0-8d|0|0|
|Write Nonvolatile Configuration Register<sup>1</sup>|B1|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|Write Volatile Configuration Register<sup>1</sup>|81|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|Clear FlagStatus Register|50|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|Write (Program Page)<sup>1,2</sup>|02|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|Write (Program) Fast Dual Input<sup>1,2</sup>|A2|1s-1s-2s|2s-2s-2s|~|~|~|~|3/4|0|
|Write (Program) Fast Dual Input Extended<sup>1,2</sup>|D2|1s-2s-2s|2s-2s-2s|~|~|~|~|3/4|0|
|Write (Program) Fast Quad Input<sup>1,2</sup>|32|1s-1s-4s|~|4s-4s-4s|4s-4d-4d|~|~|3/4|0|
|Write (Program) Fast Quad Input Extended<sup>1,2</sup>|38|1s-4s-4s|~|4s-4s-4s|4s-4d-4d|~|~|3/4|0|
|Write (Program) Fast Octal Input<sup>1,2,3</sup>|82|1s-1s-8s|~|~|~|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|Write (Program) Fast Octal Input Extended<sup>1,2,3</sup>|C2|1s-8s-8s|~|~|~|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|Write (Program) 4-byte address<sup>1,2</sup>|12|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|4<sup>5</sup>|0|
|Write (Program) Fast Quad Input 4-byte<sup>1,2</sup>|34|1s-1s-4s|~|4s-4s-4s|4s-4d-4d|~|~|4|0|
|Write (Program) Fast Quad Input Ext. 4-byte<sup>1,2</sup>|<br>3E|1s-4s-4s|~|4s-4s-4s|4s-4d-4d|~|~|4|0|
|Write (Program) Fast Octal Input 4-byte<sup>1,2,3</sup>|84|1s-1s-8s|~|~|~|8s-8s-8s|8d-8d-8d|4<sup>5</sup>|0|
|Write (Prog) Fast Octal Input Extended 4-<br>byte<sup>1,2,3</sup>|8E|1s-8s-8s|~|~|~|8s-8s-8s|8d-8d-8d|4<sup>5</sup>|0|
|Erase 32kB<sup>1</sup>|52|1s-1s-0|2s-2s-0|4s-4s-0|4s-4d-0|8s-8s-0|8d-8d-0|3/4<sup>5</sup>|0|
|Erase 4kB<sup>1</sup>|20|1s-1s-0|2s-2s-0|4s-4s-0|4s-4d-0|8s-8s-0|8d-8d-0|3/4<sup>5</sup>|0|
|Erase Sector<sup>1</sup>|D8|1s-1s-0|2s-2s-0|4s-4s-0|4s-4d-0|8s-8s-0|8d-8d-0|3/4<sup>5</sup>|0|
|Erase/Bulk Chip<sup>1</sup>|C7|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|Erase/Bulk Chip<sup>1</sup>|60|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|Erase Sector 4-byte address<sup>1</sup>|DC|1s-1s-0|2s-2s-0|4s-4s-0|4s-4d-0|8s-8s-0|8d-8d-0|4<sup>5</sup>|0|
|Erase 4kB 4-byte address<sup>1</sup>|21|1s-1s-0|2s-2s-0|4s-4s-0|4s-4d-0|8s-8s-0|8d-8d-0|4<sup>5</sup>|0|
|Erase 32kB 4-byte address<sup>1</sup>|5C|1s-1s-0|2s-2s-0|4s-4s-0|4s-4d-0|8s-8s-0|8d-8d-0|4<sup>5</sup>|0|
|OTP Read|4B|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|DCC|
|OTP Write<sup>1</sup>|42|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|4-byte address mode Enter|B7|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|4-byte address mode Exit|E9|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|DeepPower Down Enter|B9|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|DeepPower Down Exit|AB|1s-0-0|2s-0-0|4s-0-0|4s-0-0|8s-0-0|8d-0-0|0|0|
|CRC Operation|9B|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|Note 7,8|0|
|TDP Write<sup>1</sup>|F0|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|0|
|TDP Read|F1|1s-1s-1s|2s-2s-2s|4s-4s-4s|4s-4d-4d|8s-8s-8s|8d-8d-8d|3/4<sup>5</sup>|DCC|
|TDP Read DTR|F2|1s-1d-1d|2s-2d-2d|4s-4d-4d|4s-4d-4d|~|~|3/4|DCC|



_Table 21_ 

**Notes** : 

©2024 Everspin Technologies 

EMxxLX  v3.2 

33 



<!-- page 34 -->

**_EMxxLX_** 



1. A Write Enable command is needed to set the WEL bit prior to this command but memory writes only require WREN the first time, subsequent writes do not require a WREN. 

2. WREN is only required one time, subsequent writes do not require another WREN command 

3. Octal commands are treated as a NOP in part numbers that are QSPI, including QSPI in the DFN package 

4. Latency: Positions in this column, A,B,C,D, are defined as: A=SPI, B=Dual, C=Quad, D={8S|8D|4D} 

5. Octal SPI with DTR operations or commands all require 4-byte address input. 4-byte addressing does not need to be enabled. 

6. A “0” indicates that there is no address byte required. 

7. CRC command has a command modifier . The second byte input is a sub-command , not an address. 

8. CRC operation on 8Mb, 16Mb and 32Mb part numbers may not be done on the entire memory space using modifier FFh in Byte 3. For those part numbers, a CRC operation may only be done on a specified address range with modifier Feh, however this range can cover the entire memory space if desired. See Sec. 20. 

- “~” indicates mode not supported . 

- DCC = Dummy Clock Cycles from Configuration Register 

# XSPI OPCODE TIMING REPRESENTATION 

Please refer to the modular timing waveform below to understand the full timing for any opcode for EMxxLX shown in section “xSPI Command Opcodes and Modes”. Timing of each supported opcode can be decomposed into three key items. Command, Address, and Data as shown below: 



_Figure 10: Opcode Timing Diagram_ 

# **9. Read and Write Operations** 

The EMxxLX has the unique ability to operate as a persistent memory with random, byte addressability for reads and writes with no erase required, but also follows the JESD 251 conventions for programming and erase operations should the user prefer this mode. Nonvolatile Configuration Register 8 or Volatile Configuration Register 8 (TBD) is designated to select persistent memory operation or xSPI compatible operation. 

In persistent memory mode, a write to the array is accomplished with the Write command. Data bytes are written to an internal cache after the command and address bytes are received, and then written to the MRAM array continuously until CS# is driven high (end of Write operation). There is no limit to the number of bytes that can be written. The write address will wrap at the top of memory and will continue incrementing from address 0x00000000. Once CS# is driven high, the Write in Progress bit (WIP) can be read from the Status Register. WIP will indicate “Busy”, (WIP=1) for a very short period after the last byte written. Writes to the MRAM array are very fast relative to NOR Flash devices. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

34 



<!-- page 35 -->

**_EMxxLX_** 



# **10. Read Operations** 

# READ ID 

The Read ID command allows the 8-bit manufacturer identification to be read, with two additional device identification bytes following. The device identification indicates the memory type in the second byte, and the memory capacity of the device in the third byte. 

The device is first selected by driving CS# low. Then, the 8-bit command code for the command is shifted in. This is followed by the 24-bit device identification, stored in the memory. Each bit is shifted out on the falling edge of Serial Clock. The command sequence is shown below. The Read Identification (RDID) command is terminated by driving CS# high at any time during data output. When CS# is driven high, the device is in the Standby Mode. 

The Read ID command is not decoded while an Erase or Program cycle is in progress and has no effect on the cycle that is in progress. The Read Identification (RDID) command should not be issued while the device is in Deep Power-Down Mode. 

|**Operation Name**|**Description/Conditions**|
|---|---|
|Read ID (9Eh/9Fh)|Outputs information shown in the Device ID Data tables. If an ERASE or PROGRAM cycle is in<br>progress when the command is initiated, the command is not decoded and the command cycle<br>inprogress is not affected.|



## _Device ID Data_ 

The device ID data in the table below is read by the Read ID and Read ID Multiple IO commands. 

**Table 22: Device ID Data** 

|**Byte #**|**Description**|**Value**|**Byte**<br>**Address**|**Assigned By**|
|---|---|---|---|---|
|1|Manufacturer ID|0x6B|0x00|JEDEC|
|2|Memory Type (Voltage)|0xBB = 1.8V|0x01|Everspin|
|3|Memory Capacity|0x19 = 256Mb<br>0x18 = 128Mb<br>0x17 = 64Mb<br>0x16 = 32Mb<br>0x15 = 16Mb<br>0x14 = 8Mb|0x02|Everspin|
|4 – 20|Reserved|Reserved|0x04-0x13|Everspin|



_Table 22_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

35 



<!-- page 36 -->

**_EMxxLX_** 



_Read ID Diagram_ 



_Figure 11_ 

_Read ID Diagram (Octal DTR Mode)_ 



_Figure 12_ 

# READ ID MULTIPLE IO 

|**Operation Name**|**Description/Conditions**|
|---|---|
|Read ID Multiple IO (AFh)|Outputs Device ID Data tables on 1, 2, 4 or 8 IO’s. If an ERASE or PROGRAM cycle is in progress<br>when the command is initiated, the command is not decoded and the command cycle in<br>progress is not affected.|



©2024 Everspin Technologies 

EMxxLX  v3.2 

36 



<!-- page 37 -->

**_EMxxLX_** 



# READ 

|**Operation Name**|**Description/Conditions**|
|---|---|
|Read (03h)|The device supports 3-byte addressing (default), with<br>A[23:0] input during address cycle. After any READ|
|Read Fast (0Bh)|command is executed, the device will output data from<br>the selected address. After the boundary is reached, the|
|Read Fast Dual Output (3Bh)|device will start reading again from the beginning address.<br>Each address bit is latched in during the rising edge of the|
|Read Fast Dual Input/Output (BBh)|clock. The addressed byte can be at any location, and the<br>address automatically increments to the next address after<br>|
|Read Fast Quad Output (6Bh)|each byte of data is shifted out; this means the entire array<br>can be read with a single command.|
|Read Fast Quad Input/Output (EBh)|READ FAST can operate at a higher frequency (fCK)|
|Read Fast DTR (0Dh)|DTR commands function in DTR protocol regardless of<br>settings in the nonvolatile configuration register or|
|Read Fast DTR Dual Output (3Dh)|volatile configuration register; other commands function<br>in DTR protocol only after DTR protocol is enabled by the<br>|
|Read Fast DTR Dual Input/Output (BDh)|register settings. In DTR, address bits are latched on both<br>edges of the clock.|
|Read Fast DTR Quad Output (6Dh)|E7h is similar to the READ FAST QUAD I/O command<br>except that the lowest address bit (A0) must equal 0 and|
|Read Fast DTR Quad Input/Output (EDh)|only four dummy clocks are required prior to the data<br>output. This command is supported in SPI and Quad SPI|
|Read Word Quad Input/Output No DTR (E7h)|protocols, but not in the DTR protocol; it is ignored it in<br>Dual SPI protocol.|
|Read Fast Octal Output (8Bh)|4-BYTE commands and DTR 4-BYTE commands function in 4-<br>BYTE and DTR 4-BYTE protocol regardless of settings in the|
|Read Fast Octal Input/Output (CBh)|nonvolatile configuration register or volatile configuration<br>register; other commands function in 4-BYTE and DTR protocols|
|Read Fast DTR Octal Output (9Dh)|only after the specific protocol is enabled by the register settings.<br>The device will ignore address bits that are above the specified|
|Read Fast DTR Octal Input/Output (FDh)|range. It is recommended to keep address bits above the<br>specified range at “0”.|



©2024 Everspin Technologies 

EMxxLX  v3.2 

37 



<!-- page 38 -->

**_EMxxLX_** 





<!-- Start of picture text -->
READ Diagram<br><!-- End of picture text -->



_Figure 13_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

38 



<!-- page 39 -->

**_EMxxLX_** 



## _READ FAST Diagram_ 



_Figure 14_ 

## _READ FAST Dual Input/Output_ 



_Figure 15_ 

## _READ FAST Quad Input/Output_ 



_Figure 16_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

39 



<!-- page 40 -->

**_EMxxLX_** 



## _READ FAST Octal Output_ 



_Figure 17_ 

## _READ FAST Octal Input/Output_ 



_Figure 18_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

40 



<!-- page 41 -->

**_EMxxLX_** 



_READ FAST DTR  SPI, Dual SPI, Quad SPI, Octal SPI_ 



_Figure 19_ 

Note: In Octal SPI DTR mode, the address input is always 4-byte. _READ WORD QUAD INPUT/OUTPUT (no DTR) (E7h)_ 



_Figure 20_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

41 



<!-- page 42 -->

**_EMxxLX_** 



# **11. Write Operations** 

The EMxxLX can be configured to be written to as a persistent memory or be programmed similar to a NOR Flash device. The Nonvolatile Configuration Register 8 can be set to have the device operate as persistent memory ( Bit 0=1) or to emulate NOR PROGRAM commands ( Bit 0=0). 

# WRITE ENABLE/DISABLE OPERATIONS 

|**Operation Name**|**Description**|
|---|---|
|Write Enable ( 06h)|Sets the write enable latch bit, WEL. This command is required before each WRITE (Program)<br>and ERASE operation. For subsequent memory write operations, WRITE enable does not need<br>to be loaded, saving cycle overhead for back to back write operations to memory. ( For these<br>commands,the WEL bit is not reset at the completion of the write command)|
|Write Disable(04h)|Clears the write enable latch bit,WEL.|





_Figure 21_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

42 



<!-- page 43 -->

**_EMxxLX_** 



# WRITE (PROGRAM) OPERATIONS 

|**Operation Name**|**Description/Conditions**|
|---|---|
|Write (Program) (02h)|Write Operations are similar to PROGRAM except that data can change from<br>1 to 0 or 0 to 1 at any address location. No ERASE is required. There is no|
|Write (Program) FAST Dual Input (A2h)|limit to the number of bytes that can be written.<br>In persistent memory mode, the write address will wrap at the top of|
|Write (Program) FAST Dual Input Extended<br>(D2h)|memory and will continue incrementing from address 0x00000000. Unlike<br>NOR Flash, there is no page restriction.|
|Write (Program) FAST Quad Input (32h)|In NOR Flash mode, a 256 byte page can be written. Address Control wraps|
||the write address at 0xFF (wrap back to 0, address bits A[31:8] remain|
|Write (Program) FAST Quad Input<br>Extended(38h)|unchanged during the write operation). If more than 256 bytes are written,<br>since address wraps, data will be overwritten.|
|Write (Program) FAST Octal Input (82h)|<br>The “Write in Progress” WIP status bit, Status Register Bit 0 can be polled to|
|Write (Program) FAST Octal Input Extended<br>(C2h)|indicate whether or not the write has completed. Writes occur very fast,<br>please refer to the timing specification. The WEL is not reset to “0” after<br> <br>|
|Write (Program) 4-byte address (12h)|completion of a write.<br>WRITE operations can be extended to a 4-byte address range, with [A31:0]|
|Write (Program) FAST Quad Input 4-byte<br>(34h)|input during address cycle. Selection of the 3-byte or 4-byte address range<br>can be enabled through the ENABLE 4-BYTE ADDRESS MODE/EXIT 4-BYTE<br>|
|Write (Program) FAST Quad Input 4-byte<br>Extended(3Eh)|ADDRESS MODE commands.<br>4-BYTE commands and DTR 4-BYTE commands function in 4-BYTE and|
|Write (Program) FAST Octal Input 4-byte<br>(84h)|DTR 4-BYTE protocol regardless of settings in the nonvolatile configuration<br>register or volatile configuration register; other commands function in 4-|
|Write (Program) FAST Octal Input 4-byte<br>Extended (8Eh)|BYTE and DTR protocols only after the specific protocol is enabled by the<br>register settings. The device will ignore address bits that are above the<br>specified range. It is recommended to keep address bits above the specified<br>range at “0”.|



©2024 Everspin Technologies 

EMxxLX  v3.2 

43 



<!-- page 44 -->

**_EMxxLX_** 



_Write (Program) (02h)_ * 



- Persistent memory mode allows writing “0” or “1” to any number of bytes. In Page program mode, writes are confined to the selected 256 byte page and the address wraps within the page. The mode is selected with Bit 0 in the volatile and nonvolatile configuration register 8. _Figure 22_ 

## _Write Fast Dual Input (A2h)_ 

### SPI Mode 





<!-- Start of picture text -->
Dual SPI Mode<br><!-- End of picture text -->



_Figure 23_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

44 



<!-- page 45 -->

**_EMxxLX_** 



_Write Fast Quad Input (32h)_ 

SPI Mode 



Quad SPI Mode 



_Figure 24_ 

_Write Fast Octal Input (82h)_ SPI Mode 





<!-- Start of picture text -->
Octal SPI Mode<br><!-- End of picture text -->



_Figure 25_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

45 



<!-- page 46 -->

**_EMxxLX_** 



## _Write Fast with DTR Configured_ 



Note: In Octal SPI DTR mode, the address input is always 4-byte. 

_Figure 26_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

46 



<!-- page 47 -->

**_EMxxLX_** 



# **12. XIP (Execute-in-Place) Mode** 

XIP (Execute-in-Place) mode allows the memory to be read by sending an address to the device without a command code and then receives the data on one, two, four or eight pins in parallel, depending on the configuration. XIP mode saves instruction overhead and reduces random access time. 

# ACTIVATE AND TERMINATE XIP USING VOLATILE CONFIGURATION REGISTER 

Applications that boot in SPI and then switch to XIP should use the volatile configuration register. XIP provides faster memory read operations by requiring only an address to execute, rather than a command code and an address. 

To activate XIP requires two steps. First, enable XIP by setting volatile configuration register address 6 bits [7:0] as shown in the Volatile configuration table. Next, drive the XIP confirmation bit to 0 during the next READ FAST (0Bh) operation. XIP is then active. Once in XIP, READ FAST command (0Bh) that occurs after CS# is toggled requires only address bits to execute; a command code is not necessary. Device operations use the SPI protocol that is enabled. XIP is terminated by driving the XIP confirmation bit to 1 and the device automatically resets volatile configuration register bit 0 to 1. 

# ACTIVATE AND TERMINATE XIP USING NONVOLATILE CONFIGURATION REGISTER 

Applications that must boot directly in XIP use the nonvolatile configuration register. To enable a device to power-up in XIP using this register, set nonvolatile configuration register address 6  bits [7:0] as shown in the Nonvolatile configuration register table. Because the device boots directly in XIP, after the power cycle, no command code is necessary. The XIP confirmation bit is set to 0. XIP is terminated by driving the XIP confirmation bit to 1. 

# CONFIRMATION BIT SETTINGS REQUIRED TO ACTIVATE OR TERMINATE XIP 

The XIP confirmation bit setting activates or terminates XIP after XIP has been enabled in the configuration register. This bit is the value on IO0 during the first dummy clock cycle in the READ FAST operation. In Dual SPI XIP mode, the value of IO1 during the first dummy clock cycle after the addresses is always “Don’t Care.” In Quad SPI XIP mode, the values of IO3, IO2, and IO1 during the first dummy clock cycle after the addresses are always “Don’t Care.” In Octal SPI XIP mode, the values of IO7-1 during the first dummy clock cycle are always “Don’t Care”. 

|**Bit Value**|**Description**|
|---|---|
|0|Activates XIP: While this bit is 0, XIP remains activated.|
|1|Terminate XIP: When this bit is set to 1, XIP is terminated, and the device returns to SPI.|



_Table 23_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

47 



<!-- page 48 -->

**_EMxxLX_** 



_READ FAST with XIP_ 



_Figure 27_ 

TERMINATING XIP AFTER A MEMORY RESET 

A Power-On Reset or Hardware Reset will terminate XIP mode and cause the device to enter the mode configured in the nonvolatile configuration register (including XIP Boot mode). Software Reset is not applicable during XIP mode. A Reset with a signal sequence (JESD252 Reset) will exit XIP mode, but the volatile and nonvolatile configuration registers remain unchanged. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

48 



<!-- page 49 -->

**_EMxxLX_** 



# **13.ERASE Operations** 

ERASE operations on the EMxxLX are not required because any bit in the MRAM array can be written to a 1 or 0 at any time regardless of the previous state of the bit. However, for user convenience, the EMxxLX will recognize ERASE opcodes and perform sub sector, sector and chip erase operations. The WRITE ENABLE command must be executed to set the write enable latch bit to 1 before any ERASE command is initiated ; otherwise, the device ignores the command and no error bits are set to indicate operation failure. Erase operations do not reset the write enable latch at the end of the operation. 

For ERASE commands, CS# is driven LOW and held LOW until the eighth bit of the last address byte has been latched in, after which it must be driven HIGH. Any address inside the sector is a valid address for the Erase Subsector or Sector command. The operations are self-timed, and duration is tSSE, tSE, or tBE according to the command. 

If CS# is not driven HIGH, the command is not executed, flag status register error bits 1 and 5 are not set. No ERASE is performed on a protected subsector. Instead, the write enable latch bit remains set to 1, and flag status register error bits 1 and 5 are set. When an ERASE is in progress, the program or erase status bit 7 of the flag status register is set to 0. In addition, the WIP bit 0 of the status register is set to 1. When the operation completes, the status register bit 0, WIP, is cleared to 0 and the flag status register bit 7 is set to 1 (Ready). The write enable latch bit is not cleared to 0, whether the operation is successful or not. If the operation times out, the erase error bit 5 in the flag status register is set to 1. The status and flag status registers can be polled for the operation status. For the ERASE Chip command, the sequence is CS# Low, Command bits loaded > CS# High. No Address bits are loaded. CS# must remain high for tBE for the chip erase to complete. 

|**Operation Name**|**Description**|
|---|---|
|ERASE Subsector 4kB(20h)|Erases the selected subsector or sector bits to 1, or FFh. Any address within the subsector is|
|ERASE Subsector 32kB(52h)|valid for entry. Each address bit is latched in during the rising edge of the clock.|
|ERASE Sector  64kB(D8h)||
|ERASE Bulk/Chip (C7h/60h)|Erases all the device bits to 1, or FFh. The command is not executed if any sector is locked.<br>Instead,the write enable latch bit remains set to 1,and flagstatus register bits 1 and 5 are set.|





_Figure 28   Erase Operations_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

49 



<!-- page 50 -->

**_EMxxLX_** 



# **14.OTP Operation** 

|**Operation Name**|**Description**|
|---|---|
|OTP Read (4Bh)|OTP Data is shifted out on the Ios, beginning from the specified address. The address<br>increments automatically to the next address after each byte of data is shifted out. There is no<br>rollover mechanism; therefore, if read continuously, after location 0x40, the device continues<br>to output data at location 0x40.|
|OTP  Write (42h)|The 256 byte OTP data is written to the designated OTP location if the WEL bit is set by the<br>WRITE Enable command.|



# OTP READ AND WRITE OPERATION 

A dedicated area of 256 bytes outside of the memory array is provided to allow specific user information to be stored on a nonvolatile basis. To write to the OTP, the WRITE ENABLE command must be issued to set the write enable latch bit to 1. The command code is input on the IO’s, followed by address bytes and at least one data byte. There is no rollover mechanism; therefore, after a maximum of 257 bytes are latched in, the subsequent bytes are discarded. The OTP WRITE command writes, at most, 256 bytes to the OTP memory area and one OTP control byte. When the operation is in progress, the write in progress bit is set to 1. The write enable latch bit is not cleared to 0, whether the operation is successful or not, and the status register can be polled for the operation status. When the operation completes, the WIP bit 0 in the status register is cleared to 0. CS# must be driven HIGH to complete the OTP WRITE. When CS# is driven high, the self-timed operation is initiated. The duration of the operation is tPOTP. The operation is considered complete once bit 7 of the flag status register outputs 1 with at least one byte output. The OTP control byte (byte 256) is used to lock the OTP memory array. The OTP will be unlocked during a device recovery sequence and can be reprogrammed if needed. The OTP may also be unlocked by setting Volatile Configuration register 8, bit 2 to “0”, which will override the OTP Lock Byte setting and unlock the OTP array for rewriting. Once the OTP has been unlocked and updated, bit 2 should be set to “1” to enable the lock. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

50 



<!-- page 51 -->

**_EMxxLX_** 



## _OTP WRITE (42h) w/ 3-Byte Address_ 





<!-- Start of picture text -->
Figure 29<br><!-- End of picture text -->

## _OTP Control Byte_ 

The OTP control byte is used to lock the OTP memory area. It is written with the OTP WRITE command at OTP address 256. 

|**Nonvolatil**|**e OTP Con**|**trol Byte**||||
|---|---|---|---|---|---|
|**Address**|**OTP R**|**ead/Write Byte 256**||||
|**Bit**|**Op**|**Name**|**Settings**|**Description**|**Notes**|
|7:1|RO|Reserved||||
|0|RW|Lock Bit|0 = Locked<br>1 = Unlocked (default)|Used to lock the 256-byte OTP array. When bit 0 = 1, the 256-byte<br>OTP array can be programmed. When bit 0 = 0, the OTP array is<br>read only.<br>Once bit 0 has been programmed to 0, it can no longer be<br>changed to 1. Program OTP array is ignored, the write enable latch<br>bit remains set, and flag status register bits 1 and 4 are set. If there<br>is a need to unlock the OTP, Volatile register 8, bit 2, can be set to<br>“0” to override the OTP control byte lock bit.||



©2024 Everspin Technologies 

EMxxLX  v3.2 

51 



<!-- page 52 -->

**_EMxxLX_** 



## _OTP READ (4Bh)_ 



_Figure 30_ 

# **15.Extended Address Operation** 

Extended Address operation provides an extension of the 3-byte address range [A23: 0] to a 4-byte range [A31:0]. This allows the addressability to be extended from 128Mb to 256Mb.  Selection of the 3-byte or 4-byte address range can be enabled in two ways: 1) through the nonvolatile and volatile configuration register or 2), through the 4-BYTE ADDRESS MODE ENTER/EXIT commands. Each address bit is latched in during the rising edge of the clock. The addressed byte can be at any location, and the address automatically increments to the next address after each byte of data is shifted out; With 4-byte enabled, a 256Mb device can be read with a single command. 

4-BYTE commands function in 4-BYTE protocol regardless of settings in the nonvolatile configuration register; other commands function in 4-BYTE protocol only after the specific protocol is enabled by the register settings. WRITE operations can be extended to a 4-byte address range, with [A31:0] input during the address cycle. 

|**Operation Name**|**Description**|
|---|---|
|4-BYTE MODE ENTER (B7h)|This enables address length of 32 bits for the memory area needed for density larger than<br>128Mb. The default is 24-bit address mode. The Flag Status register bit 0 will be set to 1 to<br>indicate the 4-byte address mode has been enabled. Once the 4-byte mode is enabled, the<br>address length becomes 32 bits instead of the default 24 bits.|
|4-BYTE MODE EXIT (E9h)|The 4-byte mode exit will disable 4-byte mode. Reset or Power-off will also disable 4-byte<br>mode. The Flag Status register bit 0 will be reset to 0 to indicate a return to the 3-byte<br>address mode.|



©2024 Everspin Technologies 

EMxxLX  v3.2 

52 



<!-- page 53 -->

**_EMxxLX_** 



## _4-Byte Mode Enter (B7h)/ Exit (E9h)_ 



_Figure 31  4-BYTE Enter/Exit_ 

# 4-BYTE COMMANDS 

The following commands will enable extended address operation regardless of the Nonvolatile Configuration Register setting. These commands operate in the same manner as their 3-byte mode equivalents, but the address cycle portion of the command input must comprehend the added clock cycles need to accommodate the 4-byte address. Other commands function in the 4-byte mode only after the protocol is enabled by the register setting. 

|**4-BYTE Command**|**OPCODE(HEX)**|
|---|---|
|Read 4-byte address|13|
|Read Fast 4-byte address|0C|
|Read Fast DTR 4-Byte Address|0E|
|Read Fast Quad I/O DTR 4-Byte Address|EE|
|Read Fast Octal Output 4-byte address|7C|
|Read Fast Octal I/O 4-byte address|CC|
|Write (Program) 4-byte address|12|
|Write (Program) Fast Quad Input 4-byte|34|
|Write (Program) Fast Quad Input Extended 4-byte|3E|
|Write (Program) Fast Octal Input 4-byte|84|



©2024 Everspin Technologies 

EMxxLX  v3.2 

53 



<!-- page 54 -->

**_EMxxLX_** 



|Write (Program) Fast Octal Input Extended 4-byte|8E|
|---|---|
|Erase Sector 4-byte address|DC|
|Erase 4kB 4-byte address|21|
|Erase 32kB 4-byte address|5C|



## _READ 4-Byte Address Command -  showing the 32 bit address clock timing_ 



_Figure 32_ 

# **16.Deep Power Down Operation** 

Executing the Deep Power Down Enter command will put the device in the lowest power consumption mode . In this mode the device ignores all Write (Program) and Erase commands which can serve as a software protection mode while the device is not in use. In Deep Power Down mode all commands are ignored except Deep Power Down Exit, Reset Enable, and Reset. These commands will release the device from Deep Power Down mode. 

The Deep Power Down Mode automatically stops at Power-down. The device is in the Standby Mode after Power-up. Any Deep Power-Down (DP) command while an Erase or Write cycle is in progress is rejected without having any effects on the cycle that is in progress. 

The Deep Power Down Exit (Abh) is used to release the device from Deep Power down mode. Release from Power Down will take the time duration of tRDP before the device will resume normal operation and other commands are accepted. The CS# pin must remain high during the tRDP time duration. The device is also released from Deep Power mode with a Power-down, a hardware or software Reset. 

|**Operation Name**|**Description**|
|---|---|
|Deep Power Down Enter (B9h)|This command is used to have the device enter deep power down and reduce the power,<br>after a specified time,tDP,to the level of IDD2.|
|Deep Power Down Exit (Abh)|This command will cause the device to exit the deep power down mode and return to normal<br>operation after a specified time,tRDP.|



©2024 Everspin Technologies 

EMxxLX  v3.2 

54 



<!-- page 55 -->

**_EMxxLX_** 





<!-- Start of picture text -->
Deep Power Down  Enter (B9h)<br><!-- End of picture text -->





<!-- Start of picture text -->
Figure 33 Deep Power Down Enter<br><!-- End of picture text -->

©2024 Everspin Technologies 

EMxxLX  v3.2 

55 



<!-- page 56 -->

**_EMxxLX_** 



## _Deep Power Down  Exit (Abh)_ 



_Figure 34_ 

# **17.Initialization Requirements** 

It is a requirement to follow the DFIM factory initialization procedure to ensure proper operation of the EMxxLX. Please refer to Everspin Application Note EST 3000 _, Device Initialization, Power Cycle, System Reset and Recovery for EMxxLX MRAM._ The DFIM factory initialization procedure is intended to be a one-time event after soldering the EMxxLX to the PCB, i.e. after solder reflow, during system setup. If there are any subsequent solder reflow or extreme temperature exposures, the DFIM factory initialization procedure will need to be completed prior to device operation. In this case, extreme temperature exposure is 125ºC for one hour or more. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

56 



<!-- page 57 -->

**_EMxxLX_** 



# **18.Reset Operations** 

The device may be reset in hardware by enabling the RESET# signal or in software by the Reset Enable and Reset Memory commands. As described in section 3, Signal Descriptions, The RESET# signal is available on the 24-BGA package on ball A4 and is a shared signal with IO3 on the 8-DFN package on pin 7. In the 8-DFN package RESET# is available only in SPI or Dual SPI modes since it is shared with IO3. ( IO3 is needed as an input/output pin in Quad SPI mode ). 

# 18.1 SOFTWARE RESET 

|**Operation Name**|**Description**|
|---|---|
|RESET Enable(66h)|To reset the device in software, the**RESET Enable**command is issued, followed by the**RESET**|
|RESET Memory (99h)|**Memory**command. The device then enters a power-on reset condition.  The CS# deselect<br>time tSHSL3 must be observed between commands. The volatile configuration register, status<br>registers, and CRC are reset to the power-on reset default condition according to nonvolatile<br>configuration register settings.<br>It is recommended to exit XIP mode before executing these two commands.<br>If a reset is initiated while a WRITE, PROGRAM, or ERASE operation is in progress, the<br>operation is aborted, and data may be corrupted. Reset will be effective after the flag status<br>register bit 7 outputs 1 (Ready) .<br>A**RESET Enable**command is not accepted during WRITE STATUS REGISTER and WRITE<br>NONVOLATILE CONFIGURATION REGISTER operations.|



## _Reset Enable and Reset Memory_ 



_Figure 35  Software Reset_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

57 



<!-- page 58 -->

**_EMxxLX_** 



# 18.2 HARDWARE RESET 

A hardware reset is initiated by bringing RESET# low when CS# is high. 

|**Parameter**|**Symbol**|**Data**<br>**Transfer**<br>**Rate**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|Hardware RESET|tSHRL||60|–|–|ns||
|Hardware RESET recoverytime|tRHSL||40|–|–|ns||
|Hardware RESETpulse width|tRLRH||100|–|–|ns||



_Table 24 Hardware Reset Timing_ 

A hardware reset will reset Volatile configuration registers, extended address register, CRC and status registers, and erase, read, write, or program, and a register write in progress. 



_Figure 36   Hardware Reset Timing_ 

Note: A Hardware Reset is only allowed when CS# is high to avoid potential data corruption. IO3 and RESET# share a common pin, Pin 7, in part numbers using the DFN package. Steps should be taken to ensure that data on IO3 does not induce a RESET when CS# is brought high. Under SPI mode configuration, while using a command that changes the mode to Quad SPI “on-the-fly”, such as Read Fast Quad Output, a low state on Pin 7 may result, IO3, when CS# is brought high. It is important to ensure that IO3/RESET# is brought high before CS# goes low to avoid an unintended hardware reset. 

# 18.3 RESET WITH SIGNAL SEQUENCE 

The device may be reset in hardware by sequencing CS#, CK# and IO0 in a specific manner shown below which follows the JESD252 procedure for Serial Flash Reset Signaling Protocol. Use this Reset if the controller and memory device configuration is believed to be out of synchronization.  The following items are reset: Device control logic and internal registers are reset.  The device will be configured as follows:  SPI Mode with DS, 3-Byte Address Mode, DCC setting = 0 (16 dummy cycles), XIP Mode = Off, Wrap = Off, Memory Mode = Persistent Memory Mode, Erase Value = ‘1’. 

The following operations will not be reset: 

Erase in progress CRC check in progress 

Non-Volatile or Volatile Registers (left unchanged and user can read out to recover any previously written configuration if so desired) 

The Non-Volatile and Volatile Registers should be reconfigured to desired values after JESD Reset. After JESD Reset the device is in a known state and user can issue a Hard or Soft Reset if so desired. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

58 



<!-- page 59 -->

**_EMxxLX_** 





Note: CK should be kept stable high (mode 3) or low (mode 0) to prevent any confusion with commands 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|
|---|---|---|---|---|
|CS# high time|tSL|500|-|ns|
|CS# high time|tSH|500|-|ns|
|Setup time data to CS# for Reset|tDVSR|5|-|ns|
|Hold time data to CS# for Reset|tSDVR|5|-|ns|



_Figure 37  Reset with Signal Sequence (JESD 252)_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

59 



<!-- page 60 -->

**_EMxxLX_** 



# **19.Tuning Data Pattern** 

The EMxxLX provides a tuning technique to align the Data Strobe to ensure IO timing accuracy which is useful for higher speed operation. A fixed tuning data pattern (TDP) is programmed in the device which can be used to tune the system data output receiver with a known pattern. A custom pattern can be written and stored in the device as well. Please refer to Everspin application note EST 3001 for details of using the TDP function. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

60 



<!-- page 61 -->

**_EMxxLX_** 



# **20.Cyclic Redundancy Check (CRC) Operation** 

<mark>A CYCLIC REDUNDANCY CHECK (CRC) operation is designed to detect accidental changes to user data. The CRCenabled memory calculates a short, fixed-length binary sequence, known as the CRC code for each block of data. CRC can be a higher performance alternative to reading data directly in order to verify recently programmed data. CRC can be used to periodically check the data integrity of a large block of data against a stored CRC reference over the life of the product. No system hardware changes are required to enable CRC. The CRC-64 operation follows the ECMA standard.</mark> 

<mark>The CRC operation generates the CRC result of the entire memory space or of an address range specified by the operation. The CRC result is then compared with the expected CRC data provided in the sequence. The memory indicates a pass or fail with bit 3 of the Flag Status Register. If the CRC fails, it is possible to take corrective action such as verifying with a normal read mode or by rewriting the array data. CRC operation supports CRC data read back when CRC check fails; the CRC data generated from the target address range or entire device will be stored in the general purpose register (GPR) only when CRC check fails, and it can be read out through the GPR read sequence with command 96h, least significant byte first. GPR is reset to default all 0 at the beginning of the CRC operation, and so the user will read all 0 if CRC operation passes. Note that the GPR is a volatile register. It is cleared to all 0 on power-up and hardware/software reset. Read GPR starts from the first location and when clocked continuously will output 00h after location 64. The CYCLIC REDUNDANCY CHECK operation command sequences are shown in the tables below, for an entire memory space or for a selected address range. In the case of a selected address range, 3 bytes of address, bytes 12, 13, and 14, are sufficient to select a given range. For devices for which there is more than one die in the package and that utilize the Die Select command, the CRC address range works in conjunction with the selected die to check the proper address range.</mark> 

<mark>The CRC is initiated after CS# is driven high at the end of the command sequence. The status of the CRC can be checked in the Interrupt Status register bit 1. Bit 1 = 0 is CRC not complete, 1 = CRC Done. This interrupt is maskable, refer to Bit 1 in the Interrupt Mask register.</mark> 

CRC operation on 8Mb, 16Mb and 32Mb part numbers may not be done on the entire memory space using modifier FFh in Byte 3 of the command sequence. For those part numbers, a CRC operation may only be done on a specified address range with modifier FEh (as seen in Table 26), however this range can cover the entire memory space if desired. 

|**Com**|**mand Sequence**||
|---|---|---|
|**Byte#**|**Data**|**Description**|
|1|9Bh|Command code for interface activation|
|2|27h|Sub-command code for CRC operation|
|3|FFh|CRC operation option selection (CRC operation on entire device)|
|4|CRC[7:0]|1<sup>st</sup>byte of expected CRC value|
|5–10|CRC[55:8]|2<sup>nd</sup>to 7<sup>th</sup>byte of expected CRC value|
|11|CRC[63:56]|8<sup>th</sup>byte of expected CRC value|
|CS#|HIGH|Operation sequence confirmed; CRC operation starts|



_Table 25 Entire Memory Space_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

61 



<!-- page 62 -->

**_EMxxLX_** 





<!-- Start of picture text -->
Command Sequence<br>Byte# Data Description<br>1 9Bh Command code for interface activation<br>2 27h Sub-command code for CRC operation<br>3 FEh CRC operation option selection (CRC operation on a range)<br>4 CRC[7:0] 1 st  byte of expected CRC value<br>5–10 CRC[55:8] 2 nd  to 7 th  byte of expected CRC value<br>11 CRC[63:56] 8 th  byte of expected CRC value<br>12 Start Address [7:0] Specifies the starting byte address for CRC operation<br>13–14 Start Address [23:8]<br>15   Not used<br>16 Stop Address [7:0] Specifies the ending byte address for CRC operation<br>17–18 Stop Address [23:8]<br>19   Not used<br>CS# HIGH Operation sequence confirmed; CRC operation starts<br><!-- End of picture text -->

_Table 26 Specific Address Range_ 





<!-- Start of picture text -->
Figure 38 CRC Operation with full range selected (FF) using STR<br><!-- End of picture text -->

Notes:   1.  Waveform in Fig 38 is for Command 9Bh, full memory CRC using STR timings .Command 9Bh with a selected range requires the input of start and stop addresses to define the CRC range following the CRC Value bytes as described in Table 26. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

62 



<!-- page 63 -->

**_EMxxLX_** 



# **21.Package Information** 

## **24-Ball TBGA, 5 x 5 ball array** 



_Figure 39_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

63 



<!-- page 64 -->

**_EMxxLX_** 



### **8-PIN DFN PACKAGE** 







_Figure 40_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

64 



<!-- page 65 -->

**_EMxxLX_** 



## **Initial Delivery State** 

The device is delivered to the customer in the following state 

- **Memory array** : entire array is erased with all the bits set to 1 i.e. each byte contains 0xFF 

- **Status Registers** : All the status registers have value of 0x00 

- **Non-Volatile Registers** : All the non-volatile configuration registers are erased and set to 0xFFFF 

**Important Note** : The device is delivered with the memory array erased but after the assembly reflow process the memory array may need to be re-initialized. To ensure a known state of the device, please follow the procedure shown in Application Note EST 3000, _Device Initialization, Power Cycle, System Reset and Recovery for EM064LX MRAM_ , at the factory after solder reflow. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

65 



<!-- page 66 -->

**_EMxxLX_** 



# **22.Electrical Specifications and Operating Conditions** 

# 22.1 POWER-ON TIMING 

During initial power up or when recovering from brownout or power loss, a power up delay time (tPU) must be added to the time required for voltages to rise to their specified minimum voltages (VDD(min)) before normal operations may commence. This time is required to ensure that device internal voltages have stabilized. Power up time, tPU is measured from the time that VDD has reached the specified minimum voltage. See “Figure xx – Power-Up Timing” for an illustration of the timing. 

During initial startup or power loss recovery, the CS# pin should always track VDD or VIH, whichever is lower, and remain high for the total startup time, tPU. In most systems, this means that CS# should be pulled up to VDD with a resistor. Any logic that drives other inputs or Ios should hold the signals at VDD until normal operation can commence. To provide protection for data during initial power up, power loss or brownout, whenever VDD falls below VWI, the device cannot be selected (CS# must remain high), the device is inhibited from Read or Write operations, and a device reset is initiated. 



_Figure 41_ 

Note: CS# may not be enabled until tPU startup or recover time is met. 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|VWI|Reset voltage|1.0|1.5|V|-|
|tPU|VDD(min) to device operation|300||µS|-|



_Table 27_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

66 



<!-- page 67 -->

**_EMxxLX_** 



# 22.2 ABSOLUTE MAXIMUM RATINGS 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|TSTG|Storage Temperature|-65|150|ºC|-|
|TLEAD|Storage Temperature|-|See Note 3|ºC|3|
|VIO|I/O Voltage (reference to ground)|-0.6|VDD+0.6|V|1, 2|
|VDD|Supply voltage|-0.6|2.4|V|1, 2|
|VESD|Electrostatic discharge voltage (human body model)|-2000|+2000|V|1, 2|
|Hmax|Maximum Magnetic Field during read/write operation||350|Oe|4,5|



_Table 28_ 

**Notes** : 

1. All specified voltages are with respect to ground (Vss) 

2. JEDEC Standard JESD22-A114A (C1 = 100pF, R1 = 1500Ω, R2 = 500Ω 

3. Compliant with JEDEC Standard J-STD-020C (for small-body, Sn-Pb or Pb assembly), RoHS, and the European directive on Restrictions on Hazardous Substances (RoHS) 2002/95/EU 

4. Device characterized with a magnet positioned above the package with the magnetic field at 90° to surface for a time of 10 seconds. Magnetic field immunity is affected by many factors such as device operating state, distance from the package surface, length of exposure, and angle of the field. Please refer to Everspin Application Note 3004 for further details. 

5. Magnetic field immunity is higher, >1000 Oe, while device is in Standby or Read operations. 

6. These parameters are verified by design and characterization. The capacitance is measured according to JEP147 (“PROCEDURE FOR MEASURING INPUT CAPACITANCE USING A VECTOR NETWORK ANALYZER (VNA)”) with VDD and VSS applied and all other pins floating (except the pin under test), VBIAS = VDD/2, TA = 25°C, Frequency = 200 MHz 

# 22.3 RECOMMENDED OPERATING CONDITIONS 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|VDD|Supply voltage|1.65|2.0|V|-|
|TA|Ambient operating temperature (Commercial range)|0|70|°C|-|
|TA|Ambient operating temperature (Industrial range)|–40|85|°C|-|
|TA|Ambient operating temperature (Extended range)|–40|105|°C||



_Table 29_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

67 



<!-- page 68 -->

**_EMxxLX_** 



# 22.4 DEVICE PIN  LOADING 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|CIN/OUT|**I/O capacitance (IO0-IO7)**|||||
||8Mb to 64Mb|–|8|pF|6|
|CIN|**Input capacitance (otherpins)**|||||
||8Mb to 64Mb|–|6|pF|6|
|C|**Input/Chip select capacitance**|||||
|IN(CS#)|8Mb to 64Mb|–|10|pF|6|
|C|**Load capacitance**|||||
|L|8Mb to 64Mb|–|12|pF|6|



_Table 30_ 

# 22.5 MRAM CHARACTERISTICS 

|**Parameter**|**Condition**|**Unit**|**Notes**|
|---|---|---|---|
|Endurance Cycles|Reads|Unlimited|1|
||Writes|10<sup>14</sup>|1|
|Data Retention|Industrial Grade 85ºC|10 Years||
||Extended Grade 105ºC|10 Years||



_Table 31_ 

Note 1.   There is no limitation on Read cycles. Write cycles are limited for any given memory location. For purposes of endurance, a memory location is a 32 byte unit determined by device architecture. Serial writes within a 32 byte unit are considered to be one endurance cycle. Most memory use cases will utilize the entire memory array in a distributed manner which results in the ability to write to the memory without concern for wear-out for more than 10 years of continuous usage. 

# 22.6 AC TIMING IO CONDITIONS 

## **A/C TIMING I/O CONDITIONS** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|-|Input rise and fall times|–|1.5|ns|-|
|-|Input pulse voltages|0.2VDDt|o 0.8VDD|V|-|
|-|Input timing reference voltages|0.3VDDt|o 0.7VDD|V|-|
|-|Output timing reference voltages|VD|D/2|V||



_Table 32_ 

**Notes** : 

These parameters are verified by design and characterization 

©2024 Everspin Technologies 

EMxxLX  v3.2 

68 



<!-- page 69 -->

**_EMxxLX_** 



### **AC Timing Input/Output Reference Levels** 



_Figure 42_ 

# 22.7 DC CURRENT CHARACTERISTICS AND CONDITIONS 

|**Symbol**|**Parameter**|**Test Conditions**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|
|ILI|Input Leakage Current|||±2|μA|
|ILO|Output Leakage Current|||±2|μA|
|IDD1|Standby Current|CS#=VDD; VIn=VDDor VSSfor 85ºC|300|1,330|μA|
|IDD1A|Standby Current|CS#=VDD; VIn=VDDor VSSfor 105ºC|300|1870|μA|
|IDD2|Deep Power-Down Current|CS#=VDD; VIN=VDDor VSS|290|1,210|μA|
|IDD2A|Deep Power-Down Current|CS#=VDD; VIN=VDDor VSSfor 105ºC|290|1,630|μA|
|IDD3|Operating Current (Read)|CK=0.1VDD/ 0.9VDDat 200MHz (DTR),<br>IO=Open(*1,*8 I/O)|124|161|mA|
|||CK=0.1VDD/ 0.9VDDat 133MHz,<br>IO=Open(*1,*8 I/O)|50|64|mA|
|IDD4|Operating Current (Write)|CK=0.1VDD/ 0.9VDDat 200MHz (DTR),<br>IO=Open(*1,*8 I/O)|156|199|mA|
|||CK=0.1VDD/ 0.9VDDat 133MHz,<br>IO=Open(*1,*8 I/O)|59|78|mA|
|IDD5|Operating Current(WRSR)|Execute Write Status Register command,<br>then CS# = VDD|8|13|mA|
|IDD6|Operating Current (Erase<br>Subsector or Sector)|Execute Erase, then CS# = VDD|35|55|mA|
|IDD7|Operating Current (Block Erase)|Execute Erase (4Kb, 32kB), then CS# = VDD|29|48|mA|
|IDD8|Operating Current (Chip Erase)|Execute Erase (Chip), then CS#=VDD|33|50|mA|



_Table 32_ 

**Notes** : 

1. All currents are RMS unless noted. Typical values at typical VDD (1.8V); VIO = 0V/VDD; TC = +25°C. 

2. Standby current is the average current measured over any time interval 5µs after CS de-assertion (and any internal operations are complete). 

©2024 Everspin Technologies 

EMxxLX  v3.2 

69 



<!-- page 70 -->

**_EMxxLX_** 



3. Deep power-down current is the average current measured over any 5ms time interval, 100µs after the ENTER DEEP POWER-DOWN operation (and any internal operations are complete). 

4. All read currents are the average current measured over any 1KB continuous read. No load, checkerboard pattern. 

5. All write currents are the average current measured over any 256-byte typical data program. 

## 22.8 DC VOLTAGE CHARACTERISTICS AND CONDITIONS 

|**Symbol**|**Parameter**|**Test Conditions**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|VIL|Input Low Voltage||-0.5||0.2VDD|V|
|VIH|Input High Voltage||0.7VDD||VDD+0.4|V|
|VOL|Output Low Voltage|IOL =100uA|||0.4|V|
|VOH|Output High Voltage|IOH =-100μA|VDD-0.2|||V|



_Table 34_ 

## 22.9 AC SPECIFICATIONS 

|**Parameter**|**Symbol**|**Data**<br>**Transfer**<br>**Rate**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|Clock frequency for READ command|fR|STR|1|–|66|MHz||
|Clock frequency for other commands<br>|fCK1|STR|1|–|133|MHz||
|SPI, Dual SPI and Quad SPI||DTR|1||90|||
|Clock frequency for other commands|fCK2|STR|1|–|200|MHz||
|Octal SPI||DTR|1|–|200|||
|Clock HIGH time|tCH|STR|45% (1/fCK)|–|–|ns|1|
|||DTR|45% (1/fCK)|–|–|||
|Clock LOW time|tCL|STR|45% (1/fCK)|–|–|ns|1|
|||DTR|45% (1/fCK)|–|–|||
|Clock rise time (peak-to-peak)|tCLCH|STR/DTR|0.1|–|–|V/ns|2, 3|
|Clock fall time (peak-to-peak)|tCHCL|STR/DTR|0.1|–|–|V/ns|2, 3|
|CS# active setup time (relative to clock)|tSLCH|STR/DTR|4|–|–|ns||
|CS# not active hold time (relative to<br>clock)|tCHSL|STR/DTR|1|–|–|ns||
|Data in setup time|tDVCH|STR/DTR|0.5|–|–|ns||
||tDVCL|DTR only|0.5|–|–|ns||
|Data in hold time|tCHDX|STR|0.5|–|–|ns||
|||DTR|0.5|–|–|ns||
||tCLDX|DTR only|0.5|–|–|ns||
|CS# active hold time (relative to clock)|tCHSH|STR|2.5|–|–|ns|9|



©2024 Everspin Technologies 

EMxxLX  v3.2 

70 



<!-- page 71 -->



# **_EMxxLX_** 

|**Parameter**|**Symbol**|**Data**<br>**Transfer**<br>**Rate**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|||DTR|4.5|–|–|||
|CS# not active setup time (relative to|tSHCH|STR|2.5|–|–|ns||
|clock)||DTR|0.5|–|–|ns|9|
|CS# deselect time after a READ<br>command|tSHSL1|STR/DTR|50|–|–|ns|7|
|CS# deselect time after an incomplete or<br>aborted command|tSHSL1i|STR/DTR|60|–|–|ns|6|
|CS# deselect time after a non-READ<br>command|tSHSL2|STR/DTR|60|–|–|ns|4,7|
|CS# deselect time after a Soft or Hard<br>Reset.|tSHSL3|STR/DTR|200|–|–|ns||
|Output disable time|tSHQZ|STR/DTR|–|–|6|ns|2|
|Data valid window|tDVW|DTR|1.3|||ns||
|Clock LOW to output valid under 30pF|tCLQV|STR/DTR|–|–|7|ns|10|
|Clock LOW to output valid under 10pF||STR/DTR|–|–|7|ns||
|Clock HIGH to output valid under 30pF|tCHQV|DTR only|–|–|7|ns|10|
|Clock HIGH to output valid under 10pF||DTR only|–|–|7|ns||
|Output hold time|tCLQX|STR/DTR|2|–|–|ns||
|Output hold time|tCHQX|DTR only|2|–|–|ns||
|IO hold skew factor (12pF)|tQHS|DTR only|–|–|0.4|ns||
|IO valid skew related to DS (12pF)|tDSQ|DTR only|_|_|0.4|ns||
|Clock LOW to DS valid|tCLDS|DTR only|-|-|7.5|ns|8|
|CRC check time: 64 KByte block|tCRC|STR/DTR|–|2|–|ms||
|CRC check time: full chip (64Mb)|tCRC|STR/DTR|–|250|–|ms||
|Writeprotect setuptime|tWHSL|STR/DTR|20|–|–|ns|5|
|Writeprotect hold time|tSHWL|STR/DTR|100|–|–|ns|5|
|CS# HIGH to deep power-down|tDP|STR/DTR|3|–|–|µs||
|CS# HIGH to standby mode (DPD exit<br>time)|tRDP|STR/DTR|350|–|–|µs||
|WRITE STATUS REGISTER cycle time|tW|STR/DTR|–|–|1.5|µs||
|WRITE NONVOLATILE CONFIGURATION<br>REGISTER cycle time(per Address)|tWNVCR|STR/DTR|–|–|1.5|µs||
|PROGRAM OTP cycle time|tPOTP|STR/DTR|–|–|1.5|µs||
|Sector erase time|tSE|STR/DTR|–|–|960|µs||
|4KB subsector erase time|tSSE|STR/DTR|–|–|60|µs||
|32KB subsector erase time|tSSE|STR/DTR|–|–|500|µs||
|64Mb bulk erase time|tBE|STR/DTR|–|–|125|ms||
|32Mb bulk erase time|tBE|STR/DTR|–|–|64|ms||
|16Mb bulk erase time|tBE|STR/DTR|–|–|32|ms||
|8Mb bulk erase time|tBE|STR/DTR|–|–|16|ms||
|Power Uptime to device accessible|tPU||350|–|–|µs||



_Table 35_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

71 



<!-- page 72 -->

**_EMxxLX_** 



### **Notes** : 

1. tCH+ tCL must add up to 1/ fCK 

2. Value verified by characterization; not 100% tested. 

3. Expressed as a slew rate. 

4. Any non-READ command 

5. Applicable as a constraint for a Write Status Register command when Status Register Write is set to 1. 

6. Incomplete command occurs if CS# brought high prior to required timing. 

7. tSHSL2 and tSHSL1 = 75ns when device is in Octal SPI, both STR and DTR mode. 

8. DS will be driven after the first clock falling edge after CS# low. 

9. In Quad SPI DTR mode, tCHSH=5.5ns min , tSHCH=5.5ns min 

10. These specifications only apply when DS is disabled. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

72 



<!-- page 73 -->

**_EMxxLX_** 



# **Serial Input Timing STR in SPI Mode** 



_Figure 43_ 

# **Serial Input Timing STR in Dual, Quad, and Octal SPI Modes** 



_Figure 44_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

73 



<!-- page 74 -->

**_EMxxLX_** 



# **Serial Input Timing DTR in SPI Mode** 



_Figure 45_ 

# **Serial Input Timing DTR in Dual, Quad, or Octal SPI Mode** 



_Figure 46_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

74 



<!-- page 75 -->

**_EMxxLX_** 



# **Serial Output Timing STR** 



_Figure 47_ 

# **Serial Output Timing DTR** 



_Figure 48_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

75 



<!-- page 76 -->

**_EMxxLX_** 



## **Data Strobe (DS) Timing** 





<!-- Start of picture text -->
Figure 49<br><!-- End of picture text -->

Note: The device should be deselected ( CS# brought high) while CK is high to ensure that even counts of data are output. If not, the next IO or DS output may present on the output if CK goes low before CS# is high. 

## **Write Protect Setup and Hold Timing during a Write Status Register Operation** 



_Figure 50_ 

©2024 Everspin Technologies 

EMxxLX  v3.2 

76 



<!-- page 77 -->

**Expanded Serial Peripheral Interface (xSPI) Industrial STT-MRAM Datasheet** 8Mb, 16Mb, 32Mb, and 64Mb SPI, QSPI and OSPI interfaces (STR & DTR) 

# **23. Orderable Part Numbers**<sup>**1**</sup> 

|Density|IO|Package|Temperature|Pack/Ship||OPN<sup>1</sup>|
|---|---|---|---|---|---|---|
|8Mb|Quad|8-DFN|Commercial|Tray|EM008LXQADG13CS1T||
|||||Tape and Reel|EM008LXQADG13CS1R||
|||24-BGA|Commercial|Tray|EM008LXQAB313CS1T||
|||||Tape and Reel|EM008LXQAB313CS1R||
|||8-DFN|Industrial|Tray|EM008LXQADG13IS1T||
|||||Tape and Reel|EM008LXQADG13IS1R||
|||24-BGA|Industrial|Tray|EM008LXQAB313IS1T||
|||||Tape and Reel|EM008LXQAB313IS1R||
||Octal|24-BGA|Commercial|Tray|EM008LXOAB320CS1T||
|||||Tape and Reel|EM008LXOAB320CS1R||
|||24-BGA|Industrial|Tray|EM008LXOAB320IS1T||
|||||Tape and Reel|EM008LXOAB320IS1R||
|16Mb|Quad|8-DFN|Commercial|Tray|EM016LXQADG13CS1T||
|||||Tape and Reel|EM016LXQADG13CS1R||
|||24-BGA|Commercial|Tray|EM016LXQAB313CS1T||
|||||Tape and Reel|EM016LXQAB313CS1R||
|||8-DFN|Industrial|Tray|EM016LXQADG13IS1T||
|||||Tape and Reel|EM016LXQADG13IS1R||
|||24-BGA|Industrial|Tray|EM016LXQAB313IS1T||
|||||Tape and Reel|EM016LXQAB313IS1R||
||Octal|24-BGA|Commercial|Tray|EM016LXOAB320CS1T||
|||||Tape and Reel|EM016LXOAB320CS1R||
|||24-BGA|Industrial|Tray|EM016LXOAB320IS1T||
|||||Tape and Reel|EM016LXOAB320IS1R||
|32Mb|Quad|8-DFN|Commercial|Tray|EM032LXQADG13CS1T|EM032LXQADG13CS2T|
|||||Tape and Reel|EM032LXQADG13CS1R|EM032LXQADG13CS2R|
|||24-BGA|Commercial|Tray|EM032LXQAB313CS1T|EM032LXQAB313CS2T|
|||||Tape and Reel|EM032LXQAB313CS1R|EM032LXQAB313CS2R|
|||8-DFN|Industrial|Tray|EM032LXQADG13IS1T|EM032LXQADG13IS2T|
|||||Tape and Reel|EM032LXQADG13IS1R|EM032LXQADG13IS2R|
|||24-BGA|Industrial|Tray|EM032LXQAB313IS1T|EM032LXQAB313IS2T|
|||||Tape and Reel|EM032LXQAB313IS1R|EM032LXQAB313IS2R|
|||8-DFN|Extended|Tray|EM032LXQADG13ES1T|EM032LXQADG13ES2T|
|||||Tape and Reel|EM032LXQADG13ES1R|EM032LXQADG13ES2R|
|||24-BGA|Extended|Tray|EM032LXQAB313ES1T|EM032LXQAB313ES2T|
|||||Tape and Reel|EM032LXQAB313ES1R|EM032LXQAB313ES2R|
||Octal|24-BGA|Commercial|Tray|EM032LXOAB320CS1T|EM032LXOAB320CS2T|
|||||Tape and Reel|EM032LXOAB320CS1R|EM032LXOAB320CS2R|
|||24-BGA|Industrial|Tray|EM032LXOAB320IS1T|EM032LXOAB320IS2T|
|||||Tape and Reel|EM032LXOAB320IS1R|EM032LXOAB320IS2R|
|||24-BGA|Extended|Tray|EM032LXOAB320ES1T|EM032LXOAB320ES2T|
|||||Tape and Reel|EM032LXOAB320ES1R|EM032LXOAB320ES2R|



**Note 1:** The OPN table is updated to reflect the addition of the S2 version which eliminates the errata condition for the previous version, S1. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

77 



<!-- page 78 -->

**Expanded Serial Peripheral Interface (xSPI) Industrial STT-MRAM Datasheet** 8Mb, 16Mb, 32Mb, and 64Mb SPI, QSPI and OSPI interfaces (STR & DTR) 

|Density|IO|Package|Temperature|Pack/Ship|O|PN<sup>1</sup>|
|---|---|---|---|---|---|---|
|64Mb|Quad|8-DFN|Commercial|Tray|EM064LXQADG13CS1T|EM064LXQADG13CS2T|
|||||Tape and Reel|EM064LXQADG13CS1R|EM064LXQADG13CS2R|
|||24-BGA|Commercial|Tray|EM064LXQAB313CS1T|EM064LXQAB313CS2T|
|||||Tape and Reel|EM064LXQAB313CS1R|EM064LXQAB313CS2R|
|||8-DFN|Industrial|Tray|EM064LXQADG13IS1T|EM064LXQADG13IS2T|
|||||Tape and Reel|EM064LXQADG13IS1R|EM064LXQADG13IS2R|
|||24-BGA|Industrial|Tray|EM064LXQAB313IS1T|EM064LXQAB313IS2T|
|||||Tape and Reel|EM064LXQAB313IS1R|EM064LXQAB313IS2R|
|||8-DFN|Extended|Tray|EM064LXQADG13ES1T|EM064LXQADG13ES2T|
|||||Tape and Reel|EM064LXQADG13ES1R|EM064LXQADG13ES2R|
|||24-BGA|Extended|Tray|EM064LXQAB313ES1T|EM064LXQAB313ES2T|
|||||Tape and Reel|EM064LXQAB313ES1R|EM064LXQAB313ES2R|
||Octal|24-BGA|Commercial|Tray|EM064LXOAB320CS1T|EM064LXOAB320CS2T|
|||||Tape and Reel|EM064LXOAB320CS1R|EM064LXOAB320CS2R|
|||24-BGA|Industrial|Tray|EM064LXOAB320IS1T|EM064LXOAB320IS2T|
|||||Tape and Reel|EM064LXOAB320IS1R|EM064LXOAB320IS2R|
|||24-BGA|Extended|Tray|EM064LXOAB320ES1T|EM064LXOAB320ES2T|
|||||Tape and Reel|EM064LXOAB320ES1R|EM064LXOAB320ES2R|



**Note 1:** The OPN table is updated to reflect the addition of the S2 version which eliminates the errata condition for the previous version, S1. 

©2024 Everspin Technologies 

EMxxLX  v3.2 

78 



<!-- page 79 -->

**Expanded Serial Peripheral Interface (xSPI) Industrial STT-MRAM Datasheet** 8Mb, 16Mb, 32Mb, and 64Mb SPI, QSPI and OSPI interfaces (STR & DTR) 

## **Revision History** 

|**Rev**|**Date**|**Description**|
|---|---|---|
|1.0|May 1, 2020|Preliminary datasheet first release.|
|2.5|April 27, 2022|Updates to Fig 48, DS timings updated, Table 10,11,19, XIP updated, removed Quad IO<br>Entryand Exit command.|
|2.6|July 15, 2022|Based on WV 2.6 07062022. NDA required. Fig 12 updates. Table 34, AC Timings, updated<br>tCHSH ,tSHCH, removed tCLSH. Fig 44, 45 updated. App note references updated. Fig 38<br>added for CRC waveform, GPRR renamed to GPR, Table 21 updated for CRC signals. PN<br>EMxxLX used to reflect multiple densities.|
|2.7|September 9, 2022|Note 7 , Table 34 to include tSHSL2. Table 3 and Section 18.2 updated to advise on<br>IO3/RESET# in DFN package. CRC operation for 8Mb, 16Mb and 32Mb part numbers is<br>restricted,see note 8,Table 21.|
|2.8|October 1, 2022|Updated Sec.15 4-Byte commands list. Formatting on Read table in sec. 10. Added OPN<br>table in Sec 23. Added Clear Flag Status command added to Sec 6.2. Quad SPI BGA<br>package option added, Fig 3b; Table 1 note added to include NC of Quad SPI BGA option;<br>Notes added in Sec 5.5 and 5.6 to include that Octal configs are not valid in Quad SPI<br>options. Updated Table 32 for IDD1-7parameters. Table 28 updated with Hmax.|
|2.9|December 21, 2022|Table 32 IDD values updated. Table 34 erase timings updated; tCRC, tW, tWNVCR, tPOTP<br>updated. Volatile and Nonvolatile configuration register 4,DS delay,added.|
|3.0|July 10, 2023|Format on feature list updated, Note 4 on Table 28 corrected app note reference to 3004.<br>Added 105ºC Extended temperature range for 32Mb and 64Mb Quad SPI part numbers.<br>For 105ºC, leakage and standby currents may increase from 85ºC. Sec. 22 Notes updated.<br>Sec. 23 OPN table updated.|
|3.1|February 14, 2024|105ºC Extended temperature range for 32Mb and 64Mb Octal SPI part numbers added,<br>Sec.23, Orderable Part Numbers. Note 7 on Table 34, tSHSL1,2 75ns. Table 34, added tBE<br>for all densities. Added Table 31 with MRAM Characteristics. Sec 5.8 now refers to Sec 17<br>onproper device initialization. Added IDD2A to Table 32.|
|3.2|May 10,2024|Fig. 37 JESD reset signal sequence diagram updated and timing table added.<br>Sec. 23 Orderable Part Numbers table updated to add S2 versions.|



©2024 Everspin Technologies 

EMxxLX  v3.2 

79 



<!-- page 80 -->

# **Mouser Electronics** 

Authorized Distributor 

Click to View Pricing, Inventory, Delivery & Lifecycle Information: 

## Everspin Technologies: 

EM008LXOAB320IS1R EM008LXOAB320IS1T EM008LXQAB313CS1R EM008LXQAB313CS1T EM008LXQAB313IS1R EM008LXQAB313IS1T EM064LXQAB313IS1R EM064LXQAB313IS1T EM064LXQADG13CS1R EM064LXQADG13CS1T EM064LXQADG13IS1R EM064LXQADG13IS1T EM064LXOAB320CS1R EM064LXOAB320CS1T EM064LXOAB320IS1R EM064LXOAB320IS1T EM064LXQAB313CS1R EM064LXQAB313CS1T EM032LXQADG13CS1R EM032LXQADG13CS1T EM032LXQADG13IS1R EM008LXOAB320CS1R EM008LXOAB320CS1T EM032LXQADG13IS1T 

EM032LXOAB320IS1R EM032LXOAB320IS1T EM032LXQAB313CS1R EM032LXQAB313CS1T EM032LXQAB313IS1R EM032LXQAB313IS1T EM016LXQADG13CS1R EM016LXQADG13CS1T EM016LXQADG13IS1R EM016LXQADG13IS1T EM032LXOAB320CS1R EM032LXOAB320CS1T EM016LXOAB320IS1R EM016LXOAB320IS1T EM016LXQAB313CS1R EM016LXQAB313CS1T EM016LXQAB313IS1R EM016LXQAB313IS1T EM008LXQADG13CS1R EM008LXQADG13CS1T 

EM008LXQADG13IS1R EM008LXQADG13IS1T EM016LXOAB320CS1R EM016LXOAB320CS1T EM004LXOBB320IS1R EM004LXQBDH13CS1R EM004LXQBDH13CS1T EM004LXQBDH13IS1R EM004LXQBDH13IS1T EM008LXOBB320CS1R EM008LXOBB320CS1T EM008LXOBB320IS1T EM008LXQBB313CS1R EM008LXQBB313CS1T EM008LXQBB313IS1R EM008LXQBB313IS1T EM008LXQBDH13CS1R EM008LXQBDH13CS1T EM008LXQBDH13IS1R EM008LXQBDH13IS1T EM016LXOBB320CS1R EM016LXOBB320CS1T EM016LXOBB320IS1R EM016LXOBB320IS1T 

EM016LXQBB313CS1R EM016LXQBB313CS1T EM016LXQBB313IS1R EM016LXQBB313IS1T EM016LXQBDH13CS1R EM016LXQBDH13CS1T EM016LXQBDH13IS1R EM016LXQBDH13IS1T EM064LXOAB320ES1T EM008LXOBB320ES1R EM008LXOBB320ES1T EM016LXOBB320ES1T EM032LXOAB320ES1R EM064LXOAB320ES1R EM004LXOBB320ES1T EM032LXOAB320ES1T EM016LXOBB320ES1R EM004LXOBB320ES1R EM064LXQAB313IS2T EM032LXQADG13ES1T EM064LXQAB313ES2T EM064LXQADG13ES2T EM064LXOAB320ES2T EM064LXOAB320IS2T EM064LXQADG13IS2T EM032LXQAB313ES1T EM064LXQADG13IS2R EM032LXQAB313ES2T EM004LXQBB313IS1T EM008LXQBDH13ES1R EM004LXQBDH13ES2T EM008LXOBB320IS1R 

