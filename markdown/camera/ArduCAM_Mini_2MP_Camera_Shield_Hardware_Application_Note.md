# ArduCAM_Mini_2MP_Camera_Shield_Hardware_Application_Note

*Source: `original/camera/ArduCAM_Mini_2MP_Camera_Shield_Hardware_Application_Note.pdf` (7 pages)*

<!-- page 1 -->



**ArduCAM-M-2MP Camera Shield** 2MP SPI Camera Hardware Application Note Rev 1.0, Mar 2015 





<!-- page 2 -->

**ArduCAM-M-2MP Hardware Application Note** 

# Table of Contents 

|**1**|**Introduction**............................................................................................................................. 2|
|---|---|
|**2**|**Typical Wiring**......................................................................................................................... 2|
|**2.1**|**Single Camera Wiring**........................................................................................................ 2|
|**2.2**|**Multi Cameras Wiring**........................................................................................................ 2|
|**3**|**I2C Interface**............................................................................................................................ 3|
|**4**|**SPI Slave Interface**.................................................................................................................. 4|
|**5**|**ArduChip Timing Diagram**.................................................................................................... 4|
|**5.1**|**SPI Bus Write Timing**......................................................................................................... 4|
|**5.2**|**SPI Bus Single Read Timing**.............................................................................................. 4|
|**5.3**|**SPI Bus Burst Read Timing**............................................................................................... 5|
|**6**|**Registers Table**......................................................................................................................... 5|



1 

**www.ArduCAM.com** 



<!-- page 3 -->

**ArduCAM-M-2MP Hardware Application Note** 

# **1 Introduction** 

This application note describes the detail hardware operation of ArduCAM-M-2MP camera shield. 

# **2 Typical Wiring** 

## **2.1 Single Camera Wiring** 

The typical connection between ArduCAM shield and Arduino or etc platform is shown in the Figure 1. More typically the Figure 2 shows the wiring for Arduino UNO R3 board. 

















Figure 1 Typical Wiring 



Figure 2 Wiring for Arduino UNO R3 

## **2.2 Multi Cameras Wiring** 

The multi-cameras connection between ArduCAM shield and Arduino or etc platform is shown in the Figure 3. More typically the Figure 4 shows the multi-cameras wiring for Arduino UNO R3 board. 

2 

**www.ArduCAM.com** 



<!-- page 4 -->

**ArduCAM-M-2MP Hardware Application Note** 



Figure 3 Multi-Cameras Wiring 



Figure 4 Mult-Cameras Wiring on Arduino UNO 

# **3 I2C Interface** 

The I2C interface is directly connected to the image sensor OV2640. The OV2640 I2C slave address is 0x60 for write and 0x61 for read. User can use I2C master to read and write all the registers in the OV2640 sensor. For more information about the OV2640 register, please refer the OV2640 datasheet. The Figure 5 shows writing value 0x01 to the OV2640 register 0xFF. The Figure 6 shows reading value 0x26 from the OV2640 register 0x0A. 

3 

**www.ArduCAM.com** 



<!-- page 5 -->

**ArduCAM-M-2MP Hardware Application Note** 













Figure 5 I2C Write Bus Timing 













Figure 6 I2C Read Bus Timing 



# **4 SPI Slave Interface** 

The ArduCAM SPI slave interface is fixed SPI mode 0 with POL = 0 and PHA = 1. The maximum speed of SCLK is designed for 8MHz, care should taken do not over clock the maximum 8MHz. The SPI protocol is designed with a command phase with variable data phase. The chip select signal should always keep asserted during the SPI read or write bus cycle. 

The first bit[7] of the command phase is read/write byte, ‘0’ is for read and ‘1’ is for write, and the bit[6:0] is the address to be read or write in the data phase. ArduChip register table see Table 1. 

# **5 ArduChip Timing Diagram** 

## **5.1 SPI Bus Write Timing** 

The SPI bus write timing composed of a command phase and a data phase during the assertion of the chip select signal CSn. The first 8 bits is command byte which is decoded as a register address, and the second 8 bits is data byte to be written to the ArduChip internal registers. 















Figure 7 SPI Bus Write Timing 

## **5.2 SPI Bus Single Read Timing** 

The SPI bus single read timing is for read operation of ArduChip internal registers and single FIFO read function. It is composed of a command phase and a data phase during the assertion of chip select signal CSn. The first 8 bits is command byte which is decoded as a register address, the second 8 bits is dummy byte written to the SPI bus MOSI signal, and the content read back from register is appeared on the SPI bus MISO signal. 

4 

**www.ArduCAM.com** 



<!-- page 6 -->

**ArduCAM-M-2MP Hardware Application Note** 













Figure 8 SPI Bus Single Read Timing 

## **5.3 SPI Bus Burst Read Timing** 

The SPI bus burst read timing is only for burst FIFO read operation. It is composed of a burst read command phase and multiple data phases in order to get double throughput compared to the single FIFO read operation. The first byte read from the FIFO is a dummy byte, and the following bytes are valid bytes. 























Figure 9 SPI Bus Burst Read Timing 

# **6 Registers Table** 

Sensor and FIFO timing is controlled with a set of registers which is implemented in the ArduChip. User can send capture commands and read image data with a simple SPI slave interface. The detail description of registers’ bits can be found in the software section in this document. 

As mentioned earlier the first bit[7] of the command phase is read/write byte, ‘0’ is for read and ‘1’ is for write, and the bit[6:0] is the address to be read or write in the data phase. So user has to combine the 8 bits address according to the read or write commands they want to issue. 

Table 1 ArduChip Register Table 

|Register Address|<br>Register Type|Description|
|---|---|---|
|bit[6:0]|||
|0x00|RW|Test Register|
|0x01|RW|Capture Control Register|
|||Bit[2:0]: Number of frames to be captured|
|0x02|RW|Reserved|
|0x03|RW|Sensor Interface Timing Register|
|||Bit[0]: Sensor Hsync Polarity,|



5 **www.ArduCAM.com** 



<!-- page 7 -->

**ArduCAM-M-2MP Hardware Application Note** 

|||0 = active high, 1 = active low<br>Bit[1]: Sensor Vsync Polarity<br>0 = active high, 1 = active low<br>Bit[3]: Sensor data delay<br>0 = no delay, 1= delay 1 PCLK<br>Bit[4]: FIFO mode control<br>0 = FIFO mode disable, 1 = enable FIFO mode<br>Bit[6]: low power mode control<br>0 = normal mode, 1 = lowpower mode|
|---|---|---|
|0x04|RW|FIFO control Register<br>Bit[0]: write ‘1’ to clear FIFO write done flag<br>Bit[1]: write ‘1’ to start capture<br>Bit[4]: write ‘1’ to reset FIFO write pointer<br>Bit[5]: write ‘1’ to reset FIFO readpointer|
|0x05|RW|GPIO Direction Register<br>Bit[0]: Sensor reset IO direction<br>Bit[1]: Sensor power down IO direction<br>Bit[2]: Sensor power enable IO direction<br>0 = input, 1 = output|
|0x06|RW|GPIO Write Register<br>Bit[0]: Sensor reset IO value<br>Bit[1]: Sensor power down IO value<br>Bit[1]: Sensorpower enable IO value|
|0x3B|RO|Reserved|
|0x3C|RO|Burst FIFO read operation|
|0x3D|RO|Single FIFO read operation|
|0x3E|RO|Reserved|
|0x3F|RO|Reserved|
|0x40|RO|ArduChip version, constant value 0x40 for 2MP<br>model<br>Bit[7:4]: integer part of the revision number<br>Bit[3:0]: decimalpart of the revision number|
|0x41|RO|Bit[0]: camera vsync pin status<br>Bit[3]: camera write FIFO done flag|
|0x42|RO|Camera write FIFO size[7:0]|
|0x43|RO|Camera write FIFO size[15:8]|
|0x44|RO|Camera write FIFO size[18:16]|
|0x45|RO|GPIO Read Register<br>Bit[0]: Sensor reset IO value<br>Bit[1]: Sensor power down IO value<br>Bit[1]: Sensorpower enable IO value|



6 

**www.ArduCAM.com** 

