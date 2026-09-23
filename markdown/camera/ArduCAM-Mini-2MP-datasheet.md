# ArduCAM_Mini_2MP_Camera_Shield_DS

*Source: `ArduCAM_Mini_2MP_Camera_Shield_DS.pdf` (8 pages) — converted from PDF*


<!-- page 1 -->

ArduCAM-M-2MP Camera Shield
    2MP SPI Camera User Guide
           Rev 1.0, Feb 2015

<!-- page 2 -->

ArduCAM-M-2MP Camera User Guide



Table of Contents
1     Introduction ............................................................................................................................. 2
2     Application............................................................................................................................... 2
3     Features .................................................................................................................................... 3
4     Key Specifications ................................................................................................................... 3
5     Pin Definition ........................................................................................................................... 3
6     Block Diagram ......................................................................................................................... 4
7     Functions .................................................................................................................................. 4
7.1     Single Capture Mode .......................................................................................................... 4
7.2     Multiple Capture Mode ...................................................................................................... 4
7.3     JPEG Compression ............................................................................................................. 4
7.4     Normal Read and Burst Read Operation ......................................................................... 4
7.5     Rewind Read Operation ..................................................................................................... 5
7.6     Low Power Mode................................................................................................................. 5
7.7     Image Sensor Control ......................................................................................................... 5
8     Lens Options ............................................................................................................................ 6
9     Mechanical Dimension ............................................................................................................ 7
10      Order Information .............................................................................................................. 7




                                                                        1                                         www.ArduCAM.com

<!-- page 3 -->

ArduCAM-M-2MP Camera User Guide


1 Introduction
     ArduCAM-M-2MP is optimized version of ArduCAM shield Rev.C, and is a high definition
2MP SPI camera, which reduce the complexity of the camera control interface. It integrates 2MP
CMOS image sensor OV2640, and provides miniature size, as well as the easy to use hardware
interface and open source code library. The ArduCAM mini can be used in any platforms like
Arduino, Raspberry Pi, Maple, Chipkit, Beaglebone black, as long as they have SPI and I2C
interface and can be well mated with standard Arduino boards. ArduCAM mini not only offers the
capability to add a camera interface which doesn’t have in some low cost microcontrollers, but
also provides the capability to add multiple cameras to a single microcontroller.




                               Figure 1 ArduCAM Mini Shield


2 Application
   IoT cameras
   Robot cameras
   Wildlife cameras
   Other battery-powered products
   Can be used in MCU, Raspberry Pi, ARM, DSP, FPGA platforms


                                              2                          www.ArduCAM.com

<!-- page 4 -->

ArduCAM-M-2MP Camera User Guide


3 Features
   2MP image sensor OV2640
   M12 mount or CS mount lens holder with changeable lens options
   IR sensitive with proper lens combination
   I2C interface for the sensor configuration
   SPI interface for camera commands and data stream
   All IO ports are 5V/3.3V tolerant
   Support JPEG compression mode, single and multiple shoot mode, one time capture multiple
    read operation, burst read operation, low power mode and etc.
   Well mated with standard Arduino boards
   Provide open source code library for Arduino, STM32, Chipkit, Raspberry Pi, BeagleBone
    Black
   Small form of factor


4 Key Specifications
   Power supply                                       Active array size: 1600x1200
    Normal :5V/70mA                                    Shutter: rolling shutter
    Low power mode: 5V/20mA                            Lens: 1/4 inch
   SPI speed: 8MHz                                    Resolution support:
   Frame buffer: 384KB                                 UXGA, SVGA,VGA,QVGA,CIF,QCIF
   Size: 34 x 24 mm                                   Format support: RAW, YUV, RGB, JPEG
   Weight: 20g                                        Pixel Size: 2.2µm x 2.2µm
   Temperature: -10℃～+55℃


5 Pin Definition
                             Table 1 ArduCAM-M-2MP Pin Definition
        Pin No.     PIN NAME          TYPE             DESCRIPTION
          1            CS              Input           SPI slave chip select input
          2           MOSI             Input           SPI master output slave input
          3           MISO            Output           SPI master input slave output
          4           SCLK             Input           SPI serial clock
          5           GND            Ground            Power ground
          6            +5V           POWER             5V Power supply
          7            SDA         Bi-directional      Two-Wire Serial Interface Data I/O
          8            SCL             Input           Two-Wire Serial Interface Clock




                                               3                              www.ArduCAM.com

<!-- page 5 -->

ArduCAM-M-2MP Camera User Guide


6 Block Diagram
     Figure 2 shows the block diagram of ArduCAM mini shield which is composed by lens,
image sensor and an ArduChip. The lens is changeable and can be mounted by S-mount (M12x0.5)
or CS-mount lens holder. The image sensor is 2MP CMOS OV2640 from Omnivision. The
ArduChip uses ArduCAM proprietary third generation camera controller technology which
handles the complex camera, memory and user interface hardware timing and provides a user
friendly SPI interface.




                            Figure 2 ArduCAM Mini Shield Block Diagram

7 Functions
     7.1     Single Capture Mode
      Single capture mode is the default capture mode of the camera. After issuing a capture
command via SPI port, the ArduCAM will wait for a new frame and buffer the one entire image
data to the frame buffer, and then assert the completion flag bit in the register. User only needs to
poll the flag bit from the register to check out if the capture is done.
     7.2 Multiple Capture Mode
     Multiple capture mode is advanced capture mode. By setting the number of frames in the
capture register, the ArduCAM will capture consequent frames after issuing capture command.
Note that number of frames should be set properly and make sure do not exceed the maximum
memory space.
     7.3    JPEG Compression
      The JPEG compression function is implemented in the image sensor. With proper register
settings to the sensor, user can get different resolution with JPEG image stream output. It is
recommended to use JPEG output to get higher resolution than RGB mode, due to the limitation
of frame buffer.
     7.4 Normal Read and Burst Read Operation
     Normal read operation reads each image data by sending a read command in one SPI read
operation cycle. While burst read operation only need to send a read command then read multiple
image data in one SPI read operation cycle. It is recommended to use burst read operation to get
better throughput performance.

                                                 4                           www.ArduCAM.com

<!-- page 6 -->

ArduCAM-M-2MP Camera User Guide


     7.5 Rewind Read Operation
     Sometimes user wants to read the same frame of image data multiple times for processing,
the rewind read operation is designed for this purpose. By resetting the read pointer to the
beginning of the image data, user can read the same image data from the start point again.
    7.6   Low Power Mode
    Some battery power device need save power when in the idle status, the ArduCAM offers the
low power mode to reduce power consumption, by shutdown the sensor and memory circuits.
    7.7     Image Sensor Control
     Image sensor control function is implemented in the image sensor. By setting proper set of
register settings, user can control the exposure, white balance, brightness, contrast, color
saturation and etc.
     More technical information about ArduCAM mini shield, please read ArduCAM-M-2MP
Hardware Application Note.pdf and ArduCAM-M-2MP Software Application Note.pdf for detail.




                                              5                          www.ArduCAM.com

<!-- page 7 -->

ArduCAM-M-2MP Camera User Guide


8 Lens Options
      The ArduCAM-M-2MP camera shield is shipped with default LS-4011 (S mount) or
LS-6018 (CS mount), lenses specification list as follows. S mount lenses normally have build IR
cut filter, while the CS mount lenses doesn’t have build in IR cut filter.
      Please contact us admin@arducam.com for more lens options.
      LS-4011 Lens Specification




                                Figure 3 S Mount Lens Specification

    LS-6018 Lens Specification




                               Figure 4 CS Mount Lens Specification


                                              6                          www.ArduCAM.com

<!-- page 8 -->

ArduCAM-M-2MP Camera User Guide


9 Mechanical Dimension




10 Order Information
    Part Number           Description
    ArduCAM-M-2MP-SM01    S Mount Preinstalled Pin Header
    ArduCAM-M-2MP-SM02    S Mount Without Preinstalled Pin Header
    ArduCAM-M-2MP-CSM01   CS Mount Preinstalled Pin Header
    ArduCAM-M-2MP-CSM02   CS Mount Without Preinstalled Pin Header




                              7                         www.ArduCAM.com

**Extracted table(s) on this page:**

| Part Number | Description |
| --- | --- |
| ArduCAM-M-2MP-SM01 | S Mount Preinstalled Pin Header |
| ArduCAM-M-2MP-SM02 | S Mount Without Preinstalled Pin Header |
| ArduCAM-M-2MP-CSM01 | CS Mount Preinstalled Pin Header |
| ArduCAM-M-2MP-CSM02 | CS Mount Without Preinstalled Pin Header |
