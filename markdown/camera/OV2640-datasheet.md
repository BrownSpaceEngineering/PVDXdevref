# OV2640DS

*Source: `OV2640DS.pdf` (43 pages) — converted from PDF*


<!-- page 1 -->

Omni                              ision
                                                                                                  Advanced Information
                                                     ®                                            Preliminary Datasheet

                                            OV2640 Color CMOS UXGA (2.0 MegaPixel) CAMERACHIPTM
                                                                  with OmniPixel2TM Technology

General Description                                                   Applications
                                                                          •     Cellular and Camera Phones
   The OV2640 CAMERACHIPTM is a low voltage CMOS image                    •     Toys
   sensor that provides the full functionality of a single-chip           •     PC Multimedia
   UXGA (1632x1232) camera and image processor in a small
   footprint package. The OV2640 provides full-frame,                     •     Digital Still Cameras
   sub-sampled, scaled or windowed 8-bit/10-bit images in a
   wide range of formats, controlled through the Serial Camera        Key Specifications
   Control Bus (SCCB) interface.                                              Array Size       UXGA 1600 x 1200
   This product has an image array capable of operating at up                                   Core 1.2VDC + 5%
   to 15 frames per second (fps) in UXGA resolution with                Power Supply          Analog 2.5 ~ 3.0VDC
   complete user control over image quality, formatting and                                       I/O 1.7V to 3.3V
   output data transfer. All required image processing functions,                                     125 mW (for 15 fps, UXGA
   including exposure control, gamma, white balance, color                                            YUV mode)
   saturation, hue control, white pixel canceling, noise                       Power           Active
                                                                                                      140 mW (for 15 fps, UXGA
   canceling, and more, are also programmable through the               Requirements                  compressed mode)
   SCCB interface. The OV2640 also includes a compression                                   Standby 600 µA
   engine for increased processing power. In addition,
   OmniVision CAMERACHIPS use proprietary sensor technology              Temperature      Operation -30°C to 70°C
   to improve image quality by reducing or eliminating common                  Range Stable Image 0°C to 50°C
   lighting/electrical sources of image contamination, such as                                        • YUV(422/420)/YCbCr422
   fixed pattern noise, smearing, etc., to produce a clean, fully                                     • RGB565/555
   stable color image.                                                        Output Formats (8-bit)
                                                                                                      • 8-bit compressed data
                                                                                                      • 8-/10-bit Raw RGB data
              Note: The OV2640 uses a lead-free                                            Lens Size 1/4"
   Pb         package.                                                              Chief Ray Angle 25° non-linear
                                                                           Maximum UXGA/SXGA 15 fps
                                                                               Image           SVGA 30 fps
Features                                                                Transfer Rate             CIF 60 fps
   •   High sensitivity for low-light operation                                           Sensitivity 0.6 V/Lux-sec
   •   Low operating voltage for embedded portable apps                                    S/N Ratio 40 dB
   •   Standard SCCB interface                                                       Dynamic Range 50 dB
   •   Output support for Raw RGB, RGB (RGB565/555),                                     Scan Mode Progressive
       GRB422, YUV (422/420) and YCbCr (4:2:2) formats                   Maximum Exposure Interval 1247 x tROW
   •   Supports image sizes: UXGA, SXGA, SVGA, and any                            Gamma Correction Programmable
       size scaling down from SXGA to 40x30                                                Pixel Size 2.2 µm x 2.2 µm
   •   VarioPixel® method for sub-sampling                                             Dark Current 15 mV/s at 60°C
   •   Automatic image control functions including Automatic                           Well Capacity 12 Ke
       Exposure Control (AEC), Automatic Gain Control                            Fixed Pattern Noise <1% of VPEAK-TO-PEAK
       (AGC), Automatic White Balance (AWB), Automatic                                   Image Area 3590 µm x 2684 µm
       Band Filter (ABF), and Automatic Black-Level                            Package Dimensions 5725 µm x 6285 µm
       Calibration (ABLC)
   •   Image quality controls including color saturation,             Figure 1 OV2640 Pin Diagram (Top View)
       gamma, sharpness (edge enhancement), lens
       correction, white pixel canceling, noise canceling, and
       50/60 Hz luminance detection
                                                                                           A1    A2      A3     A4     A5     A6
   •   Line optical black level output capability
                                                                                      DOGND EXPST_B AGND SGND VREFN STROBE
   •   Video or snapshot operation
                                                                                           B1    B2      B3     B4     B5     B6
   •   Zooming, panning, and windowing functions
                                                                                       DOVDD FREX       AVDD   SVDD   SVDD   PWDN
   •   Internal/external frame synchronization
   •   Variable frame rate control                                                         C1    C2      C3     C4     C5     C6

   •   Supports LED and flash strobe mode                                              SIO_D SIO_C      HREF XVCLK VREFH RESETB

   •   Supports scaling                                                                          D2     OV2640                D6
   •   Supports compression                                                                     VSYNC                         NC

   •   Embedded microcontroller                                                            E1    E2      E3     E4     E5     E6
                                                                                           Y1    Y0     PCLK   EGND    Y6    DGND
Ordering Information                                                                       F1    F2      F3     F4     F5     F6
                                                                                       EVDD     DVDD     Y2     Y4     Y8    DVDD
                   Product                       Package                                   G1    G2      G3     G4     G5     G6
                                                                                       EVDD     DGND     Y3     Y5     Y7     Y9
       OV02640-VL9A (Color, lead-free)          38-pin CSP2


Version 1.6, February 28, 2006                                      Proprietary to OmniVision Technologies                          1

**Extracted table(s) on this page:**

| Array Size | UXGA | 1600 x 1200 |
| --- | --- | --- |
| Power Supply | Core | 1.2VDC + 5% |
|  | Analog | 2.5 ~ 3.0VDC |
|  | I/O | 1.7V to 3.3V |
| Power Requirements | Active | 125 mW (for 15 fps, UXGA YUV mode) |
|  |  | 140 mW (for 15 fps, UXGA compressed mode) |
|  | Standby | 600 µA |
| Temperature Range | Operation | -30°C to 70°C |
|  | Stable Image | 0°C to 50°C |
| Output Formats (8-bit) |  | • YUV(422/420)/YCbCr422 • RGB565/555 • 8-bit compressed data • 8-/10-bit Raw RGB data |
| Lens Size |  | 1/4" |
| Chief Ray Angle |  | 25° non-linear |
| Maximum Image Transfer Rate | UXGA/SXGA | 15 fps |
|  | SVGA | 30 fps |
|  | CIF | 60 fps |
| Sensitivity |  | 0.6 V/Lux-sec |
| S/N Ratio |  | 40 dB |
| Dynamic Range |  | 50 dB |
| Scan Mode |  | Progressive |
| Maximum Exposure Interval |  | 1247 x t ROW |
| Gamma Correction |  | Programmable |
| Pixel Size |  | 2.2 µm x 2.2 µm |
| Dark Current |  | 15 mV/s at 60°C |
| Well Capacity |  | 12 Ke |
| Fixed Pattern Noise |  | <1% of V PEAK-TO-PEAK |
| Image Area |  | 3590 µm x 2684 µm |
| Package Dimensions |  | 5725 µm x 6285 µm |

| Product | Package |
| --- | --- |
| OV02640-VL9A (Color, lead-free) | 38-pin CSP2 |


<!-- page 2 -->

OV2640                            Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                                                   Omni       ision


Functional Description
    Figure 2 shows the functional block diagram of the OV2640 image sensor. The OV2640 includes:
    •   Image Sensor Array (1632 x 1232 total image array)
    •   Analog Signal Processor
    •   10-Bit A/D Converters
    •   Digital Signal Processor (DSP)
    •   Output Formatter
    •   Compression Engine
    •   Microcontroller
    •   SCCB Interface
    •   Digital Video Port


Figure 2 Functional Block Diagram




                                                                                                                                        Compression Video
                                                                         10-Bit      Channel            Black Level   DSP   Formatter                              Y[9:0]
                         Column Sample/Hold              AMP                                                                              Engine     Port
                                                                          A/D        Balance           Compensation
      Row Select




                             Image Array                  Gain                       Balance
                            (1632 x 1232)                Control                     Control


                                                                                                 Control
                                                                                                 Register
                                                                                                  Bank




                                                                                                SCCB Slave
                   PLL                        Timing Generator and Control Logic                                                 Microcontroller
                                                                                                 Interface




                                                                                               SIO_C   SIO_D
          XVCLK                     HREF      PCLK    VSYNC     STROBE RESETB      PWDN




2                              Proprietary to OmniVision Technologies                                                           Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

|  | Column Sample/Hold |
| --- | --- |
| tceleS woR | Image Array (1632 x 1232) |


<!-- page 3 -->

Omni        ision                                                                                                                  Functional Description



Image Sensor Array                                                                        10-Bit A/D Converters

   The OV2640 sensor has an image array of 1632 columns                                       After the analog amplifier, the bayer pattern Raw signal is
   by 1232 rows (2,010,624 pixels). Figure 3 shows a                                          fed to two 10-bit analog-to-digital (A/D) converters, one for
   cross-section of the image sensor array.                                                   G channel and one shared by the BR channels. These
                                                                                              A/D converters operate at speeds up to 20 MHz and are
Figure 3 Sensor Array Region Color Filter Layout                                              fully synchronous to the pixel rate (actual conversion rate
                                                                                              is related to the frame rate).
      Column



                                    1626

                                           1627

                                                  1628

                                                         1629
                                                                1630

                                                                       1631
    R
            0

                1

                    2

                        3

                            4

                                5




    o 0 B G         B   G   B   G   B      G      B      G      B      G      Dummy
    w 1 G R         G   R   G   R   G      R      G      R      G      R      Dummy
                                                                                          Channel Balance
        2   B   G   B   G   B   G   B      G      B      G      B      G      Dummy
        3   G   R   G   R   G   R   G      R      G      R      G      R      Dummy
        4                                                                                     The amplified signals are then balanced with a channel
        5                                                                     Optical         balance block. In this block, the Red/Blue channel gain is
                                                                              Black
        6                                                                                     increased or decreased to match Green channel
        7
                                                                                              luminance level.
        8   B   G   B   G   B   G   B      G      B      G      B      G      Dummy
        9   G   R   G   R   G   R   G      R      G      R      G      R      Dummy
       10   B   G   B   G   B   G   B      G      B      G      B      G      Dummy
       11   G   R   G   R   G   R   G      R      G      R      G      R      Dummy           Balance Control
       12   B   G   B   G   B   G   B      G      B      G      B      G
       13   G   R   G   R   G   R   G      R      G      R      G      R
                                                                                              Channel Balance can be done manually by the user or by
    1206    B   G   B   G   B   G   B      G      B      G      B      G
                                                                                              the internal automatic white balance (AWB) controller.
                                                                               1220
    1207    G   R   G   R   G   R   G      R      G      R      G      R      Active
    1208    B   G   B   G   B   G   B      G      B      G      B      G      Lines


                                                                                          Black Level Compensation
    1231    G   R   G   R   G   R   G      R      G      R      G      R
                                                                                              After the pixel data has been digitized, black level
                                                                                              calibration can be applied before the data is output. The
   The color filters are arranged in a Bayer pattern. The                                     black level calibration block subtracts the average signal
   primary color BG/GR array is arranged in line-alternating                                  level of optical black pixels to compensate for the dark
   fashion. Of the 2,010,624 pixels, 1,991,040 (1632x1220)                                    current in the pixel output. The user can disable black
   are active. The other pixels are used for black level                                      level calibration.
   calibration and interpolation.

   The sensor array design is based on a field integration                                Windowing
   read-out system with line-by-line transfer and an
   electronic shutter with a synchronous pixel read-out
                                                                                              The OV2640 allows the user to define window size or
   scheme.
                                                                                              region of interest (ROI), as required by the application.
                                                                                              Window size setting (in pixels) ranges from 2 x 4 to
                                                                                              1632 x 1220 (UXGA) or 2 x 2 to 818 x 610 (SVGA), and
Analog Amplifier                                                                              408 x 304 (CIF), and can be anywhere inside the
                                                                                              1632 x 1220 boundary. Note that modifying window size
   When the column sample/hold circuit has sampled one                                        or window position does not alter the frame or pixel rate.
   row of pixels, the pixel data will shift out one-by-one into                               The windowing control merely alters the assertion of the
   an analog amplifier.                                                                       HREF signal to be consistent with the programmed
                                                                                              horizontal and vertical ROI. The default window size is
                                                                                              1600 x 1200. Refer to Figure 4 and registers HREFST,
   Gain Control                                                                               HREFEND, REG32, VSTRT, VEND, and COM1 for
                                                                                              details.
   The amplifier gain can either be programmed by the user
   or controlled by the internal automatic gain control circuit
   (AGC).




Version 1.6, February 28, 2006                                                          Proprietary to OmniVision Technologies                           3

**Extracted table(s) on this page:**

| B | G | B | G | B | G |
| --- | --- | --- | --- | --- | --- |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |

| B | G | B | G | B | G |
| --- | --- | --- | --- | --- | --- |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |
| B | G | B | G | B | G |
| G | R | G | R | G | R |

| B | G | B | G | B | G |
| --- | --- | --- | --- | --- | --- |
| G | R | G | R | G | R |
| B | G | B | G | B | G |

| B | G | B | G | B | G |
| --- | --- | --- | --- | --- | --- |
| G | R | G | R | G | R |
| B | G | B | G | B | G |


<!-- page 4 -->

OV2640                    Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                                              Omni     ision



Figure 4 Windowing                                                                          CIF Mode
                                     Column                               Column            The OV2640 can also operate at a higher frame rate to
                                      Start                                End
                                                                                            output 400 x 296 sized images. Figure 6 shows the
                          HREF                                                              sub-sampling diagram in both horizontal and vertical
                        R Column                                                            directions for CIF mode.
                        o
                        w

                                                                                          Figure 6 CIF Sub-Sampling Mode
    Row Start
                                                                                                  Column
                 HREF




                                                        Display




                                                                                                    i+10
                                                                                                    i+11
                                                                                                    i+12
                                                                                                    i+13
                                                                                                    i+14
                                                                                                    i+15
                                                                                                    i+16
                                                                                                    i+17
                                                                                                    i+18
                                                                                                    i+19
                                                                                                    i+20
                                                                                                    i+21
                                                                                                    i+22
                                                                                                    i+23
                                                                                                    i+1
                                                                                                    i+2
                                                                                                    i+3
                                                                                                    i+4
                                                                                                    i+5
                                                                                                    i+6
                                                                                                    i+7
                                                                                                    i+8
                                                                                                    i+9
                                                        Window




                                                                                                    i
                                                                                           Row     n B              G     B         G     B         G
                                                                                                 n+1
    Row End                                                                                      n+2
                                                                                                 n+3
                                                                           Sensor Array          n+4
                                                                              Boundary           n+5 G              R     G         R     G         R
                                                                                                 n+6
                                                                                                 n+7
                                                                                              n+8   B               G     B         G     B         G
     Zooming and Panning Mode                                                                 n+9
                                                                                             n+10
                                                                                             n+11
     The OV2640 provides zooming and panning modes. The                                      n+12
     user can select this mode under SVGA/CIF mode timing.                                   n+13   G               R     G         R     G         R
     The related zoom ratios will be 2:1 of UXGA for SVGA and                                n+14
                                                                                             n+15
     4:1 of UXGA for CIF. Registers ZOOMS[7:0] (0x49) and                                    n+16   B               G     B         G     B         G
     COM19[1:0] (0x48) define the vertical line start point.                                 n+17
     Register ARCOM2[2] (0x34) defines the horizontal start                                  n+18
                                                                                             n+19
     point.                                                                                  n+20
                                                                                             n+21   G               R     G         R     G         R
                                                                                             n+22
     Sub-sampling Mode                                                                       n+23


                                                                                                         Skipped Pixels
     The OV2640 supports two sub-sampling modes. Each
     sub-sampling mode has different resolution and maximum
     frame rate. These modes are described in the following
     sections.                                                                            Timing Generator and Control Logic

     SVGA mode                                                                              In general, the timing generator controls the following:
                                                                                            •   Frame Exposure Mode Timing
     The OV2640 can be programmed to output 800 x 600
     (SVGA) sized images for applications where higher                                      •   Frame Rate Adjust
     resolution image capture is not required. In this mode,                                •   Frame Rate Timing
     both horizontal and vertical pixels will be sub-sampled
     with an aspect ratio of 4:2 as shown in Figure 5.
                                                                                            Frame Exposure Mode Timing
Figure 5 SVGA Sub-Sampling Mode
                                                                                            The OV2640 supports frame exposure mode. Typically,
                         Column                                                             the frame exposure mode must work with the aid of an
                               i+1
                                     i+2
                                           i+3
                                                 i+4
                                                       i+5
                                                             i+6
                                                                   i+7
                                                                         i+8
                                                                               i+9




                                                                                            external shutter.
                           i




                Row n      B   G                  B G                    B G
                                                                                            The frame exposure pin, FREX (pin B2), is the frame
                    n+1    G R                    G R                    G R
                                                                                            exposure mode enable pin and the EXPST_B pin (pin A2)
                    n+2
                                                                                            serves as the sensor's exposure start trigger. When the
                    n+3                                                                     external master device asserts the FREX pin high, the
                    n+4    B   G                  B G                    B G                sensor array is quickly pre-charged and stays in reset
                    n+5    G R                    G R                    G R                mode until the EXPST_B pin goes low (sensor exposure
                    n+6                                                                     time can be defined as the period between EXPST_B low
                    n+7                                                                     and shutter close). After the FREX pin is pulled low, the
                                                                                            video data stream is then clocked to the output port in a
                               Skipped Pixels                                               line-by-line manner. After completing one frame of data

4                       Proprietary to OmniVision Technologies                                                                Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| B | G |
| --- | --- |
| G | R |

| B | G |
| --- | --- |
| G | R |

| B | G |
| --- | --- |
| G | R |

| B | G |
| --- | --- |
| G | R |

| B | G |
| --- | --- |
| G | R |

| B | G |
| --- | --- |
| G | R |


<!-- page 5 -->

Omni   ision                                                                                                              Functional Description



   output, the OV2640 will output continuous live video data        Output Formatter
   unless in single frame transfer mode. Figure 18 and
   Figure 19 show the detailed timing and Table 11 shows                This block controls all output and data formatting required
   the timing specifications for this mode.                             prior to sending the image out.


   Frame Rate Adjust                                                    Scaling Image Output
   The OV2640 offers three methods for frame rate                       The OV2640 is capable of scaling down the image size
   adjustment:                                                          from CIF to 40x30. By using SCCB registers, the user can
   •   Clock prescaler: (see “CLKRC” on page 23)                        output the desired image size. At certain image sizes,
       By changing the system clock divide ratio and PLL,               HREF is not consistent in a frame.
       the frame rate and pixel rate will change together.
       This method can be used for dividing the frame/pixel
       rate by: 1/2, 1/3, 1/4 … 1/64 of the input clock rate.       Compression Engine
   •   Line adjustment: (see “REG2A” on page 26 and
       “FRARL” on page 26)                                              As shown in Figure 7, the Compression Engine consists
       By adding a dummy pixel timing in each line                      of three major blocks:
       (between HSYNC and pixel data out), the frame rate               •    DCT
       can be changed while leaving the pixel rate as is.
                                                                        •    QZ
   •   Vertical sync adjustment:
                                                                        •    Entropy Encoder
       By adding dummy line periods to the vertical sync
       period (see “ADDVSL” on page 26 and “ADDVSH”
       on page 26 or see “FLL” on page 27 and “FLH” on              Figure 7 Compression Engine Block Diagram
       page 27), the frame rate can be altered while the
       pixel rate remains the same.                                                               Compression Engine
                                                                                                                                      Compressed
                                                                      Video Data                                                      Stream
                                                                                      DCT             QZ         Entropy Encoder

   Frame Rate Timing
                                                                                   Scale Factor
                                                                                                    Q-Table     H-Table     Marker
   Default frame timing is illustrated in Figure 15, Figure 16,
   and Figure 17. Refer to Table 1 for the actual pixel rate at
   different frame rates.
   Table 1        Frame/Pixel Rates in UXGA Mode                    Microcontroller
 Frame Rate (fps)        15        7.5        2.5      1.25             The OV2640 embeds an 8-bit microcontroller with
 PCLK (MHz)              36         18         6         3              512-byte data memory and 4 KB program memory. It
                                                                        provides the flexibility of decoding protocol commands
                                                                        from the host for controlling the system, as well as the
                                                                        ability to fine tune image quality.
Digital Signal Processor (DSP)

   This block controls the interpolation from Raw data to           SCCB Interface
   RGB and some image quality control.
   •   Edge enhancement (a two-dimensional high pass                    The Serial Camera Control Bus (SCCB) interface controls
       filter)                                                          the CAMERACHIP operation. Refer to OmniVision
   •   Color space converter (can change Raw data to RGB                Technologies Serial Camera Control Bus (SCCB)
       or YUV/YCbCr)                                                    Specification for detailed usage of the serial control port.
   •   RGB matrix to eliminate color cross talk
   •   Hue and saturation control
   •   Programmable gamma control                                       Slave Operation Mode
   •   Transfer 10-bit data to 8-bit
                                                                        The OV2640 can be programmed to operate in slave
   •   White pixel canceling                                            mode (default is master mode).
   •   De-noise
                                                                        When used as a slave device, COM7[3] (0x12), CLKRC[6]
                                                                        (0x11), and COM2[2] (0x09) register bits should be set to

Version 1.6, February 28, 2006                                    Proprietary to OmniVision Technologies                                           5

**Extracted table(s) on this page:**

| Frame Rate (fps) | 15 | 7.5 | 2.5 | 1.25 |
| --- | --- | --- | --- | --- |
| PCLK (MHz) | 36 | 18 | 6 | 3 |


<!-- page 6 -->

OV2640                Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                                      Omni   ision



     "1" and the OV2640 will use PWDN and RESETB pins as            Power Down Mode
     vertical and horizontal synchronization triggers supplied
     by a master device. The master device must provide the           Two methods are available to place the OV2640 into
     following signals:                                               power-down mode: hardware power-down and SCCB
     1.      System clock MCLK to XVCLK pin                           software power-down.

     2.      Horizontal sync MHSYNC to RESETB pin                     To initiate hardware power-down, the PWDN pin (pin B6)
     3.      Vertical frame sync MVSYNC to PWDN pin                   must be tied to high. When this occurs, the OV2640
                                                                      internal device clock is halted and all internal counters are
     See Figure 8 for slave mode connections and Figure 9 for         reset. The current draw is less than 15 µA in this standby
     detailed timing considerations.                                  mode.

                                                                      Executing a software power-down through the SCCB
Figure 8 Slave Mode Connection                                        interface suspends internal circuit activity but does not
                                                                      halt the device clock. The current requirements drop to
                                                                      less than 1 mA in this mode. All register content is
                                                                      maintained in standby mode.
                      Y[9:0]

                   RESETB                     MHSYNC
                                                                    Digital Video Port
                     PWDN                     MVSYNC

                     XVCLK                    MCLK
                                                                      MSB/LSB Swap

                   OV2640                     Master                  The OV2640 has a 10-bit digital video port. The MSB and
                                              Device                  LSB can be swapped with the control registers. Figure 10
                                                                      shows some examples of connections with external
                                                                      devices.
Figure 9 Slave Mode Timing

                                    T frame
                                                                    Figure 10 Connection Examples
    MVSYNC
                                                                              MSB Y9            Y9            LSB Y9          Y0
                       T VS     T line                   T HS
    MHSYNC                                                                        Y8            Y8               Y8           Y1

                                  Tclk                                            Y7            Y7               Y7           Y2
      MCLK                                                                        Y6            Y6               Y6           Y3

                                                                                  Y5            Y5               Y5           Y4
    NOTE:
                                                                                  Y4            Y4               Y4           Y5
    1) THS > 6 Tclk, Tvs > Tline
                                                                                  Y3            Y3               Y3           Y6
    2) Tline = 1922 x Tclk (UXGA); Tline = 1190 x Tclk (SVGA);
                                                                                  Y2            Y2               Y2           Y7
      Tline = 595 x Tclk (CIF)
                                                                                  Y1            Y1               Y1           Y8
    3) Tframe = 1248 x Tline (UXGA); Tframe = 672 x Tline (SVGA);
                                                                              LSB Y0            Y0           MSB Y0           Y9
       Tframe = 336 x Tline (CIF)
                                                                              OV2640            External     OV2640           External
                                                                                                Device                        Device

                                                                               Default 10-bit Connection       Swap 10-bit Connection


Strobe Mode                                                                   MSB Y9            Y7            LSB Y9

                                                                                  Y8            Y6               Y8
     The OV2640 has a Strobe mode that allows it to work with
                                                                                  Y7            Y5               Y7           Y0
     an external flash and LED.
                                                                                  Y6            Y4               Y6           Y1

                                                                                  Y5            Y3               Y5           Y2

                                                                                  Y4            Y2               Y4           Y3
Reset                                                                             Y3            Y1               Y3           Y4

                                                                                  Y2            Y0               Y2           Y5
     The OV2640 includes a RESETB pin (pin C6) that forces                        Y1                             Y1           Y6
     a complete hardware reset when it is pulled low (GND).                   LSB Y0                         MSB Y0           Y7
     The OV2640 clears all registers and resets them to their                 OV2640            External     OV2640           External
     default values when a hardware reset occurs. A reset can                                   Device                        Device

     also be initiated through the SCCB interface.                              Default 8-bit Connection        Swap 8-bit Connection




6                  Proprietary to OmniVision Technologies                                                  Version 1.6, February 28, 2006

<!-- page 7 -->

Omni       ision                                                                                               Functional Description



    Line/Pixel Timing                                                     Pixel Output Pattern

    The OV2640 digital video port can be programmed to                    Table 2 shows the output data order from the OV2640.
    work in either master or slave mode.                                  The data output sequence following the first HREF and
                                                                          after VSYNC is: B0,0 G0,1 B0,2 G0,3… B0,1598 G0,1599.
    In both master and slave modes, pixel data output is                  After the second HREF the output is G1,0 R1,1 G1,2 R1,3…
    synchronous with PCLK (or MCLK if port is a slave),                   G1,1598 R1,1599…, etc. If the OV2640 is programmed to
    HREF, and VSYNC. The default PCLK edge for valid data                 output SVGA resolution data, horizontal and vertical
    is the negative edge but may be programmed using                      sub-sampling will occur. The default output sequence for
    register COM10[4] for the positive edge. Basic line/pixel             the first line of output will be: B0,0 G0,1 B0,4 G0,5… B0,1596
    output timing and pixel timing specifications are shown in            G0,1597. The second line of output will be: G1,0 R1,1 G1,4
    Figure 14 and Table 10.                                               R1,5… G1,1596 R1,1597.

    Also, using register COM10[5], PCLK output can be gated               Table 2           Data Pattern
    by the active video period defined by the HREF signal.
    See Figure 11 for details.                                       R/C        0       1       2       3     ...    1598       1599

Figure 11 PCLK Output Only at Valid Pixels                            0        B0,0    G0,1    B0,2    G0,3   ...   B0,1598    G0,1599

                                                                      1        G1,0    R1,1    G1,2    R1,3   ...   G1,1598    R1,1599
PCLK
PCLK active edge negative
                                                                      2        B2,0    G2,1    B2,2    G2,3   ...   B2,1598    G2,1599
HREF
PCLK                                                                  3        G3,0    R3,1    G3,2    R3,3   ...   G3,1598    R3,1599
PCLK active edge positive
VSYNC                                                                 .                                        .
                                                                      .                                        .

    The specifications shown in Table 10 apply for                  1198 B1198,0 G1198,1 B1198,2 G1198,3 . . . B1198,1598 G1198,1599
    DVDD = +1.2 V, DOVDD = +2.8 V, TA = 25°C, sensor
    working at 15 fps, external loading = 20 pF.                    1199 G1199,0 R1199,1 G1199,2 R1199,3 . . . G1199,1598 R1199,1599




Version 1.6, February 28, 2006                                   Proprietary to OmniVision Technologies                                  7

**Extracted table(s) on this page:**

| R/C | 0 | 1 | 2 | 3 | . . . | 1598 | 1599 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | B 0,0 | G 0,1 | B 0,2 | G 0,3 | . . . | B 0,1598 | G 0,1599 |
| 1 | G 1,0 | R 1,1 | G 1,2 | R 1,3 | . . . | G 1,1598 | R 1,1599 |
| 2 | B 2,0 | G 2,1 | B 2,2 | G 2,3 | . . . | B 2,1598 | G 2,1599 |
| 3 | G 3,0 | R 3,1 | G 3,2 | R 3,3 | . . . | G 3,1598 | R 3,1599 |
| . . |  |  |  |  | . . |  |  |
| 1198 | B 1198,0 | G 1198,1 | B 1198,2 | G 1198,3 | . . . | B 1198,1598 | G 1198,1599 |
| 1199 | G 1199,0 | R 1199,1 | G 1199,2 | R 1199,3 | . . . | G 1199,1598 | R 1199,1599 |


<!-- page 8 -->

OV2640           Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                           Omni    ision


Pin Description

    Table 3      Pin Description

      Pin Location          Name        Pin Type                                 Function/Description

          A1           DOGND             Ground         Ground for digital video port

                                                        Snapshot Exposure Start Trigger
                                                            0:   Sensor starts exposure (only effective in snapshot mode)
          A2           EXPST_B            Input
                                                            1:   Sensor stays in reset mode
                                                        Note: There is no internal pull-up/pull-down resistor.

          A3           AGND              Ground         Ground for analog circuit

          A4           SGND              Ground         Ground for sensor array

          A5           VREFN            Reference       Internal analog reference - connect to ground using a 0.1 µF capacitor

                                                        Flash control output
          A6           STROBE              I/O          Default: Input
                                                        Note: There is no internal pull-up/pull-down resistor.

          B1           DOVDD              Power         Power for digital video port

                                                        Snapshot trigger - use to activate a snapshot sequence
          B2           FREX               Input
                                                        Note: There is no internal pull-up/pull-down resistor.

          B3           AVDD               Power         Power for analog circuit

          B4           SVDD               Power         Power for sensor array

          B5           SVDD               Power         Power for sensor array

                                                        Power-down mode enable, active high
          B6           PWDN               Input
                                                        Note: There is an internal pull-down resistor.

          C1           SIO_D               I/O          SCCB serial interface data I/O

                                                        SCCB serial interface clock input
          C2           SIO_C              Input
                                                        Note: There is no internal pull-up/pull-down resistor.

                                                        Horizontal reference output
          C3           HREF                I/O          Default: Input
                                                        Note: There is no internal pull-up/pull-down resistor.

                                                        System clock input
          C4           XVCLK              Input
                                                        Note: There is no internal pull-up/pull-down resistor.

          C5           VREFH            Reference       Internal analog reference - connect to ground using a 0.1 µF capacitor

                                                        Reset mode, active low
          C6           RESETB             Input
                                                        Note: There is an internal pull-up resistor.

                                                        Vertical synchronization output
          D2           VSYNC               I/O          Default: Input
                                                        Note: There is no internal pull-up/pull-down resistor.

          D6           NC                   –           No connection

                                                        Video port output bit[1]
          E1           Y1                  I/O          Default: Input
                                                        Note: There is no internal pull-up/pull-down resistor.



8              Proprietary to OmniVision Technologies                                             Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Pin Location | Name | Pin Type | Function/Description |
| --- | --- | --- | --- |
| A1 | DOGND | Ground | Ground for digital video port |
| A2 | EXPST_B | Input | Snapshot Exposure Start Trigger 0: Sensor starts exposure (only effective in snapshot mode) 1: Sensor stays in reset mode Note: There is no internal pull-up/pull-down resistor. |
| A3 | AGND | Ground | Ground for analog circuit |
| A4 | SGND | Ground | Ground for sensor array |
| A5 | VREFN | Reference | Internal analog reference - connect to ground using a 0.1 µF capacitor |
| A6 | STROBE | I/O | Flash control output Default: Input Note: There is no internal pull-up/pull-down resistor. |
| B1 | DOVDD | Power | Power for digital video port |
| B2 | FREX | Input | Snapshot trigger - use to activate a snapshot sequence Note: There is no internal pull-up/pull-down resistor. |
| B3 | AVDD | Power | Power for analog circuit |
| B4 | SVDD | Power | Power for sensor array |
| B5 | SVDD | Power | Power for sensor array |
| B6 | PWDN | Input | Power-down mode enable, active high Note: There is an internal pull-down resistor. |
| C1 | SIO_D | I/O | SCCB serial interface data I/O |
| C2 | SIO_C | Input | SCCB serial interface clock input Note: There is no internal pull-up/pull-down resistor. |
| C3 | HREF | I/O | Horizontal reference output Default: Input Note: There is no internal pull-up/pull-down resistor. |
| C4 | XVCLK | Input | System clock input Note: There is no internal pull-up/pull-down resistor. |
| C5 | VREFH | Reference | Internal analog reference - connect to ground using a 0.1 µF capacitor |
| C6 | RESETB | Input | Reset mode, active low Note: There is an internal pull-up resistor. |
| D2 | VSYNC | I/O | Vertical synchronization output Default: Input Note: There is no internal pull-up/pull-down resistor. |
| D6 | NC | – | No connection |
| E1 | Y1 | I/O | Video port output bit[1] Default: Input Note: There is no internal pull-up/pull-down resistor. |


<!-- page 9 -->

Omni    ision                                                                                           Pin Description


   Table 3        Pin Description

       Pin Location         Name    Pin Type                             Function/Description

                                               Video port output bit[0]
            E2         Y0             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

                                               Pixel clock output
            E3         PCLK           I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

            E4         EGND         Ground     Ground for internal regulator

                                               Video port output bit[6]
            E5         Y6             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

            E6         DGND         Ground     Ground for digital core

            F1         EVDD          Power     Power for internal regulator

            F2         DVDD          Power     Sensor digital power (Core)

                                               Video port output bit[2]
            F3         Y2             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

                                               Video port output bit[4]
            F4         Y4             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

                                               Video port output bit[8]
            F5         Y8             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

            F6         DVDD          Power     Sensor digital power (Core)

            G1         EVDD          Power     Power for internal regulator

            G2         DGND         Ground     Ground for digital core

                                               Video port output bit[3]
            G3         Y3             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

                                               Video port output bit[5]
            G4         Y5             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

                                               Video port output bit[7]
            G5         Y7             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.

                                               Video port output bit[9]
            G6         Y9             I/O      Default: Input
                                               Note: There is no internal pull-up/pull-down resistor.




Version 1.6, February 28, 2006                         Proprietary to OmniVision Technologies                        9

**Extracted table(s) on this page:**

| Pin Location | Name | Pin Type | Function/Description |
| --- | --- | --- | --- |
| E2 | Y0 | I/O | Video port output bit[0] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| E3 | PCLK | I/O | Pixel clock output Default: Input Note: There is no internal pull-up/pull-down resistor. |
| E4 | EGND | Ground | Ground for internal regulator |
| E5 | Y6 | I/O | Video port output bit[6] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| E6 | DGND | Ground | Ground for digital core |
| F1 | EVDD | Power | Power for internal regulator |
| F2 | DVDD | Power | Sensor digital power (Core) |
| F3 | Y2 | I/O | Video port output bit[2] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| F4 | Y4 | I/O | Video port output bit[4] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| F5 | Y8 | I/O | Video port output bit[8] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| F6 | DVDD | Power | Sensor digital power (Core) |
| G1 | EVDD | Power | Power for internal regulator |
| G2 | DGND | Ground | Ground for digital core |
| G3 | Y3 | I/O | Video port output bit[3] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| G4 | Y5 | I/O | Video port output bit[5] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| G5 | Y7 | I/O | Video port output bit[7] Default: Input Note: There is no internal pull-up/pull-down resistor. |
| G6 | Y9 | I/O | Video port output bit[9] Default: Input Note: There is no internal pull-up/pull-down resistor. |


<!-- page 10 -->

OV2640           Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                     Omni    ision


Figure 12 Pinout Diagram




                                      A1          A2     A3          A4    A5         A6
                                   DOGND EXPST_B AGND SGND VREFN STROBE

                                      B1          B2     B3          B4    B5         B6
                                    DOVDD FREX          AVDD       SVDD   SVDD       PWDN

                                      C1          C2     C3          C4    C5         C6
                                     SIO_D SIO_C        HREF XVCLK VREFH RESETB

                                                  D2    OV2640                        D6
                                                VSYNC                                 NC

                                       E1         E2     E3          E4    E5         E6
                                       Y1         Y0    PCLK       EGND    Y6        DGND

                                       F1         F2     F3          F4    F5         F6
                                     EVDD        DVDD    Y2          Y4    Y8        DVDD

                                      G1          G2     G3          G4    G5         G6
                                     EVDD       DGND     Y3          Y5    Y7         Y9




     Table 4     Ball Matrix

                         1                  2                  3                 4             5                6
        A             DOGND            EXPST_B            AGND                  SGND        VREFN           STROBE

        B             DOVDD              FREX                 AVDD              SVDD        SVDD             PWDN

        C              SIO_D             SIO_C                HREF          XVCLK           VREFN           RESETB

        D                               VSYNC                                                                  NC

        E                Y1                 Y0                PCLK              EGND          Y6              DGND

        F              EVDD              DVDD                  Y2                Y4           Y8              DVDD

        G              EVDD              DGND                  Y3                75           Y7               Y9




10             Proprietary to OmniVision Technologies                                       Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

|  | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| A | DOGND | EXPST_B | AGND | SGND | VREFN | STROBE |
| B | DOVDD | FREX | AVDD | SVDD | SVDD | PWDN |
| C | SIO_D | SIO_C | HREF | XVCLK | VREFN | RESETB |
| D |  | VSYNC |  |  |  | NC |
| E | Y1 | Y0 | PCLK | EGND | Y6 | DGND |
| F | EVDD | DVDD | Y2 | Y4 | Y8 | DVDD |
| G | EVDD | DGND | Y3 | 75 | Y7 | Y9 |


<!-- page 11 -->

Omni     ision                                                                                                   Electrical Characteristics


Electrical Characteristics
   Table 5            Absolute Maximum Ratings
    Ambient Storage Temperature                                                     -40ºC to +95ºC

                                                                     VDD-A          4.5V

    Supply Voltages (with respect to Ground)                         VDD-C          3V

                                                                     VDD-IO         4.5V

    All Input/Output Voltages (with respect to Ground)                              -0.3V to VDD-IO+1V

    Lead-free Temperature, Surface-mount process                                    245ºC

    ESD Rating, Human Body model                                                    2000V

   NOTE:         Exceeding the Absolute Maximum ratings shown above invalidates all AC and DC electrical specifications and may
                 result in permanent device damage.


   Table 6            DC Characteristics (-30°C < TA < 70°C)

        Symbol                      Parameter                          Min                  Typ                  Max             Unit

    Supply

    VDD-A             Supply voltage                                    2.5                 2.8                  3.0               V

    VDD-D             Supply voltage                                   1.14                 1.2                  1.26              V

    VDD-IO            Supply voltagea                                  1.71                 2.8                  3.3               V

    IDDA-A            Active (Operating) Currentb                                           30                   40               mA

                                                                                    25 (YUV)             35 (YUV)
    IDDA-D            Active (Operating) Currentb                                                                                 mA
                                                                                    35 (Compressed)      50 (Compressed)

    IDDA-IO           Active (Operating) Currentb                                            6                   10               mA

    IDDS-SCCB                                                                                1                    2               mA
                      Standby Currentb
    IDDS-PWDN                                                                               600                  1200             µA

    Digital Inputs

    VIL               Input voltage LOW                                                                          0.54              V

    VIH               Input voltage HIGH                               1.26                                                        V

    CIN               Input capacitor                                                                             10              pF

    Digital Outputs (standard loading 25 pF)

    VOH               Output voltage HIGH                              1.62                                                        V

    VOL               Output voltage LOW                                                                         0.18              V

    Serial Interface Inputs

    VIL               SIO_C and SIO_D                                  -0.5                  0                   0.54              V

    VIH               SIO_C and SIO_D                                  1.26                 1.8                  2.3               V

   a.     1.8V I/O is supported. Contact your local OmniVision FAE for further details.
   b.     VDD-A = 2.8V, VDD-D = 1.2V, and VDD-IO = 1.8V for 15 fps in UXGA mode
          IDDS-SCCB refers to SCCB-initiated Standby, while IDDS-PWDN refers to PWDN pad-initiated Standby


Version 1.6, February 28, 2006                                          Proprietary to OmniVision Technologies                          11

**Extracted table(s) on this page:**

| Ambient Storage Temperature |  | -40ºC to +95ºC |
| --- | --- | --- |
| Supply Voltages (with respect to Ground) | V DD-A | 4.5V |
|  | V DD-C | 3V |
|  | V DD-IO | 4.5V |
| All Input/Output Voltages (with respect to Ground) |  | -0.3V to V +1V DD-IO |
| Lead-free Temperature, Surface-mount process |  | 245ºC |
| ESD Rating, Human Body model |  | 2000V |

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| Supply |  |  |  |  |  |
| V DD-A | Supply voltage | 2.5 | 2.8 | 3.0 | V |
| V DD-D | Supply voltage | 1.14 | 1.2 | 1.26 | V |
| V DD-IO | Supply voltagea | 1.71 | 2.8 | 3.3 | V |
| I DDA-A | Active (Operating) Currentb |  | 30 | 40 | mA |
| I DDA-D | Active (Operating) Currentb |  | 25 (YUV) 35 (Compressed) | 35 (YUV) 50 (Compressed) | mA |
| I DDA-IO | Active (Operating) Currentb |  | 6 | 10 | mA |
| I DDS-SCCB | Standby Currentb |  | 1 | 2 | mA |
| I DDS-PWDN |  |  | 600 | 1200 | µA |
| Digital Inputs |  |  |  |  |  |
| V IL | Input voltage LOW |  |  | 0.54 | V |
| V IH | Input voltage HIGH | 1.26 |  |  | V |
| C IN | Input capacitor |  |  | 10 | pF |
| Digital Outputs (standard loading 25 pF) |  |  |  |  |  |
| V OH | Output voltage HIGH | 1.62 |  |  | V |
| V OL | Output voltage LOW |  |  | 0.18 | V |
| Serial Interface Inputs |  |  |  |  |  |
| V IL | SIO_C and SIO_D | -0.5 | 0 | 0.54 | V |
| V IH | SIO_C and SIO_D | 1.26 | 1.8 | 2.3 | V |


<!-- page 12 -->

OV2640               Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                          Omni       ision


     Table 7          AC Characteristics (TA = 25°C, VDD-A = 2.8V)

          Symbol                                Parameter                Min     Typ           Max         Unit

      ADC Parameters

      B                 Analog bandwidth                                            20                     MHz

      DLE               DC differential linearity error                             0.5                    LSB

      ILE               DC integral linearity error                                  1                     LSB

                        Settling time for hardware reset                                        <1           ms

                        Settling time for software reset                                        <1           ms

                        Settling time for UXGA/SVGA mode change                                 <1           ms

                        Settling time for register setting                                     <300          ms



     Table 8          Timing Characteristics

          Symbol                              Parameter              Min       Typ            Max          Unit

      Oscillator and Clock Input

      fOSC              Frequency (XVCLK)                            6         24                         MHz

      tr, tf            Clock input rise/fall time                                             5             ns

                        Clock input duty cycle                       45        50             55             %




12                 Proprietary to OmniVision Technologies                            Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| Oscillator and Clock Input |  |  |  |  |  |
| f OSC | Frequency (XVCLK) | 6 | 24 |  | MHz |
| t, t r f | Clock input rise/fall time |  |  | 5 | ns |
|  | Clock input duty cycle | 45 | 50 | 55 | % |


<!-- page 13 -->

Omni   ision                                                                                                               Timing Specifications


Timing Specifications

Figure 13 SCCB Interface Timing Diagram


                                        tF                           t HIGH                          tR
                                                    t LOW
                 SIOC

                                                   t HD:STA         t HD:DAT                    t SU:DAT
                          t SU:STA                                                                         tSU:STO

               SIOD IN
                                                                                                                                  t BUF
                                                              tAA                        t DH
             SIOD OUT




   Table 9           SCCB InterfaceTiming Specifications

       Symbol                                   Parameter                                          Min               Typ    Max           Unit

    fSIO_C               Clock Frequency                                                                                    400           KHz

    tLOW                 Clock Low Period                                                           1.3                                   µs

    tHIGH                Clock High Period                                                          600                                   ns

    tAA                  SIOC low to Data Out valid                                                 100                     900           ns

    tBUF                 Bus free time before new START                                             1.3                                   µs

    tHD:STA              START condition Hold time                                                  600                                   ns

    tSU:STA              START condition Setup time                                                600                                    ns

    tHD:DAT              Data-in Hold time                                                           0                                    µs

    tSU:DAT              Data-in Setup time                                                        100                                    ns

    tSU:STO              STOP condition Setup time                                                 600                                    ns

    tR, tF               SCCB Rise/Fall times                                                                               300           ns

    tDH                  Data-out Hold time                                                         50                                    ns




Version 1.6, February 28, 2006                                                 Proprietary to OmniVision Technologies                            13

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| f SIO_C | Clock Frequency |  |  | 400 | KHz |
| t LOW | Clock Low Period | 1.3 |  |  | µs |
| t HIGH | Clock High Period | 600 |  |  | ns |
| t AA | SIOC low to Data Out valid | 100 |  | 900 | ns |
| t BUF | Bus free time before new START | 1.3 |  |  | µs |
| t HD:STA | START condition Hold time | 600 |  |  | ns |
| t SU:STA | START condition Setup time | 600 |  |  | ns |
| t HD:DAT | Data-in Hold time | 0 |  |  | µs |
| t SU:DAT | Data-in Setup time | 100 |  |  | ns |
| t SU:STO | STOP condition Setup time | 600 |  |  | ns |
| t t R, F | SCCB Rise/Fall times |  |  | 300 | ns |
| t DH | Data-out Hold time | 50 |  |  | ns |


<!-- page 14 -->

OV2640                Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                                              Omni    ision


Figure 14 UXGA, SVGA, and CIF Line/Pixel Output Timing

                                                                tp              t pr          t pf

                    PCLK or
                      MCLK


                                                   t dphr                                                                         t dphf

                      HREF


                                                             t su        t hd

                                                   Invalid
                      D[9:0]       P1599/799/399                    P0     P1          P2    P 1598/798/398 P1599/799/399
                                                    Data

                                                     t dpd



     Table 10          Pixel Timing Specifications

           Symbol                            Parameter                                 Min            Typ                   Max              Unit

      tp                PCLK period                                                                  27.78                                    ns

      tpr               PCLK rising time                                                              3.5                                     ns

      tpf               PCLK falling time                                                             2.2                                     ns

      tdphr             PCLK negative edge to HREF rising edge                          0                                    5                ns

      tdphf             PCLK negative edge to HREF negative edge                        0                                    5                ns

      tdpd              PCLK negative edge to data output delay                         0                                    5                ns

      tsu               Data bus setup time                                            15                                                     ns

      thd               Data bus hold time                                              8                                                     ns




14                  Proprietary to OmniVision Technologies                                                      Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Symbol | Parameter | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- |
| t p | PCLK period |  | 27.78 |  | ns |
| t pr | PCLK rising time |  | 3.5 |  | ns |
| t pf | PCLK falling time |  | 2.2 |  | ns |
| t dphr | PCLK negative edge to HREF rising edge | 0 |  | 5 | ns |
| t dphf | PCLK negative edge to HREF negative edge | 0 |  | 5 | ns |
| t dpd | PCLK negative edge to data output delay | 0 |  | 5 | ns |
| t su | Data bus setup time | 15 |  |  | ns |
| t hd | Data bus hold time | 8 |  |  | ns |


<!-- page 15 -->

Omni   ision                                                                                                          Timing Specifications


Figure 15 UXGA Frame Timing

                                                                       1248 x tLINE

               VSYNC

                    4 x tLINE                  27193 tP                tLINE = 1922 tP                   57697 tP

                                                                        322 tP

                HREF

                                                            1600 tP
                                                189 tP                                80 tP

               HSYNC



               D[9:0]               Invalid Data
                                              P0 - P1599
                                                            Row 0     Row 1      Row 2        Row 1199



Figure 16 SVGA Frame Timing

                                                                       672 x tLINE

               VSYNC

                    4 x tLINE                   7415 tP                tLINE = 1190 tP                    73895 tP

                                                                        390 tP

                HREF

                                                            800 tP
                                                 179 tP                               80 tP

               HSYNC



               D[9:0]               Invalid Data
                                                P0 - P799
                                                            Row 0     Row 1      Row 2        Row 599



Figure 17 CIF Mode Frame Timing

                                                                       336 x tLINE

               VSYNC

                        4 x tLINE              3707.5 tP               tLINE = 595 tP                    17907.5 tP

                                                                        195 tP

                HREF

                                                            400 tP
                                                89.5 tP                               40 tP

               HSYNC



               D[9:0]               Invalid Data
                                                P0 - P399
                                                            Row 0     Row 1      Row 2        Row 295


Version 1.6, February 28, 2006                                           Proprietary to OmniVision Technologies                         15

<!-- page 16 -->

OV2640                  Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                                               Omni     ision


Figure 18 Frame Exposure Mode Timing with EXPST_B Staying Low

                                      Shutter Open

               Shutter
                                                                       "Flash Turn ON"
                 FREX
                                     t line
                                                                Exposure Time
                                      Sensor
      Sensor Timing                 Precharge

                                     t dfvr     t dfvf          t dvsc
               VSYNC
                                                               t dvh                                      tdhv
                 HREF

                D[9:0]
                                                                                                                       No following live video
                          Row X                                           Row 0     Row 1     Row 1199
                                                                                                                       frame if set to transfer
                                                                                                                            single frame


Figure 19 Frame Exposure Mode Timing with EXPST_B Asserted

                                      Shutter Open

               Shutter

                 FREX
                            t des                tdef
                                                                          "Flash Turn ON"
              EXPST_B
                                     t pre
                                                                Exposure Time
                                      Sensor
      Sensor Timing                 Precharge

                                     t dfvr     t dfvf          t dvsc
               VSYNC
                                                               t dvh                                      tdhv
                 HREF

                D[9:0]
                                                                                                                       No following live video
                          Row X                                           Row 0     Row 1    Row 1199
                                                                                                                       frame if set to transfer
                                                                                                                            single frame


     Table 11            Frame Exposure Timing Specifications

                 Symbol                                  Min                         Typ                         Max                          Unit

      tline                                                                     1922 (UXGA)                                                       tp

      tvs                                                                                4                                                    tline

      tdfvr                                               8                                                       9                               tp

      tdfvf                                                                                                       4                           tline

      tdvsc                                                                                                       2                           tline

      tdhv                                                                     38964 (UXGA)                                                       tp

      tdvh                                                                     15928 (UXGA)                                                       tp

      tdhso                                               0                                                                                       ns

      tdef                                               20                                                                                       tp

      tdes                                                8                                              1900 (UXGA)                              tp

     NOTE       1) FREX must stay high long enough to ensure the entire sensor has been reset.
                2) Shutter must be closed no later then 3896 tp after VSYNC falling edge.


16                 Proprietary to OmniVision Technologies                                                               Version 1.6, February 28, 2006

<!-- page 17 -->

Omni   ision                                                                                                                                                                                        Timing Specifications


OV2640 Light Response

Figure 20 OV2640 Light Response


                                                                                   OV-9620spectrum response
                                                                                   OV2640 Spectrum Response
                             200

                             180

                             160

                             140

                             120
               Sensitivity




                             100

                             80

                             60

                             40

                             20

                              0
                                   300nm

                                           380nm

                                                   420nm

                                                           460nm

                                                                   500nm

                                                                           540nm

                                                                                   580nm

                                                                                           620nm

                                                                                                   660nm

                                                                                                           700nm

                                                                                                                    740nm

                                                                                                                            780nm

                                                                                                                                    820nm

                                                                                                                                                860nm

                                                                                                                                                        900nm

                                                                                                                                                                940nm

                                                                                                                                                                        980nm

                                                                                                                                                                                1020nm

                                                                                                                                                                                         1060nm

                                                                                                                                                                                                  1100nm

                                                                                                                                                                                                           1180nm
                                                                                                            Wavelength

                                                                                                            R               G               B




Version 1.6, February 28, 2006                                                                                     Proprietary to OmniVision Technologies                                                             17

<!-- page 18 -->

OV2640             Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                            Omni    ision


Register Set
     Table 12 and Table 13 provides a list and description of the Device Control registers contained in the OV2640. For all register
     Enable/Disable bits, ENABLE = 1 and DISABLE = 0. The device slave addresses are 60 for write and 61 for read.

     There are two different sets of register banks. Register 0xFF controls which set is accessible. When register 0xFF=00,
     Table 12 is effective. When register 0xFF=01, Table 13 is effective.

     Table 12       Device Control Register List (when 0xFF = 00) (Sheet 1 of 4)

       Address          Register         Default
        (Hex)            Name             (Hex)         R/W                                 Description

        00-04            RSVD               XX            –     Reserved

                                                                Bypass DSP
                                                                    Bit[7:1]:   Reserved
          05          R_BYPASS              0x1           RW        Bit[0]:     Bypass DSP select
                                                                                0: DSP
                                                                                1: Bypass DSP, sensor out directly

        06-43            RSVD               XX            –     Reserved

          44               Qs               0C            RW    Quantization Scale Factor

        45-4F            RSVD               XX            –     Reserved

                                                                    Bit[7]:     LP_DP
                                                                    Bit[6]:     Round
          50           CTRLl[7:0]           00            RW
                                                                    Bit[5:3]:   V_DIVIDER
                                                                    Bit[2:0]:   H_DIVIDER

          51           HSIZE[7:0]           40            RW    H_SIZE[7:0] (real/4)

          52           VSIZE[7:0]           F0            RW    V_SIZE[7:0] (real/4)

          53          XOFFL[7:0]            00            RW    OFFSET_X[7:0]

          54          YOFFL[7:0]            00            RW    OFFSET_Y[7:0]

                                                                    Bit[7]:     V_SIZE[8]
                                                                    Bit[6:4]:   OFFSET_Y[10:8]
          55           VHYX[7:0]            08            RW
                                                                    Bit[3]:     H_SIZE[8]
                                                                    Bit[2:0]:   OFFSET_X[10:8]

                                                                    Bit[7:4]:   DP_SELY
          56           DPRP[7:0]            00            RW
                                                                    Bit[3:0]:   DP_SELX

                                                                    Bit[7]:     H_SIZE[9]
          57           TEST[3:0]            00            RW
                                                                    Bit[6:0]:   Reserved

          5A          ZMOW[7:0]             58            RW    OUTW[7:0] (real/4)

          5B           ZMOH[7:0]            48            RW    OUTH[7:0] (real/4)

                                                                    Bit[7:4]:   ZMSPD (zoom speed)
          5C           ZMHH[1:0]            00            RW        Bit[2]:     OUTH[8]
                                                                    Bit[1:0]:   OUTW[9:8]

        5D-7B            RSVD               XX            –     Reserved

          7C         BPADDR[3:0]            00            RW    SDE Indirect Register Access: Address


18               Proprietary to OmniVision Technologies                                            Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 00-04 | RSVD | XX | – | Reserved |
| 05 | R_BYPASS | 0x1 | RW | Bypass DSP Bit[7:1]: Reserved Bit[0]: Bypass DSP select 0: DSP 1: Bypass DSP, sensor out directly |
| 06-43 | RSVD | XX | – | Reserved |
| 44 | Qs | 0C | RW | Quantization Scale Factor |
| 45-4F | RSVD | XX | – | Reserved |
| 50 | CTRLl[7:0] | 00 | RW | Bit[7]: LP_DP Bit[6]: Round Bit[5:3]: V_DIVIDER Bit[2:0]: H_DIVIDER |
| 51 | HSIZE[7:0] | 40 | RW | H_SIZE[7:0] (real/4) |
| 52 | VSIZE[7:0] | F0 | RW | V_SIZE[7:0] (real/4) |
| 53 | XOFFL[7:0] | 00 | RW | OFFSET_X[7:0] |
| 54 | YOFFL[7:0] | 00 | RW | OFFSET_Y[7:0] |
| 55 | VHYX[7:0] | 08 | RW | Bit[7]: V_SIZE[8] Bit[6:4]: OFFSET_Y[10:8] Bit[3]: H_SIZE[8] Bit[2:0]: OFFSET_X[10:8] |
| 56 | DPRP[7:0] | 00 | RW | Bit[7:4]: DP_SELY Bit[3:0]: DP_SELX |
| 57 | TEST[3:0] | 00 | RW | Bit[7]: H_SIZE[9] Bit[6:0]: Reserved |
| 5A | ZMOW[7:0] | 58 | RW | OUTW[7:0] (real/4) |
| 5B | ZMOH[7:0] | 48 | RW | OUTH[7:0] (real/4) |
| 5C | ZMHH[1:0] | 00 | RW | Bit[7:4]: ZMSPD (zoom speed) Bit[2]: OUTH[8] Bit[1:0]: OUTW[9:8] |
| 5D-7B | RSVD | XX | – | Reserved |
| 7C | BPADDR[3:0] | 00 | RW | SDE Indirect Register Access: Address |


<!-- page 19 -->

Omni    ision                                                                                   Register Set


   Table 12       Device Control Register List (when 0xFF = 00) (Sheet 2 of 4)

       Address       Register      Default
        (Hex)         Name          (Hex)     R/W                               Description

         7D        BPDATA[7:0]       00        RW    SDE Indirect Register Access: Data

        7E-85         RSVD           XX         –    Reserved

                                                     Module Enable
                                                         Bit[7:6]:   Reserved
                                                         Bit[5]:     DCW
                                                         Bit[4]:     SDE
         86           CTRL2          0D        RW
                                                         Bit[3]:     UV_ADJ
                                                         Bit[2]:     UV_AVG
                                                         Bit[1]:     Reserved
                                                         Bit[0]:     CMX

                                                     Module Enable
                                                         Bit[7]:     BPC
         87           CTRL3          50        RW
                                                         Bit[6]:     WPC
                                                         Bit[5:0]:   Reserved

        88-8B         RSVD           XX         –    Reserved

         8C         SIZEL[5:0]       00        RW    {HSIZE[11], HSIZE[2:0], VSIZE[2:0]}

       8D-BF          RSVD           XX         –    Reserved

         C0        HSIZE8[7:0]       80        RW    Image Horizontal Size HSIZE[10:3]

         C1        VSIZE8[7:0]       60        RW    Image Vertical Size VSIZE[10:3]

                                                     Module Enable
                                                         Bit[7]:     AEC_EN
                                                         Bit[6]:     AEC_SEL
                                                         Bit[5]:     STAT_SEL
         C2           CTRL0          0C        RW        Bit[4]:     VFIRST
                                                         Bit[3]:     YUV422
                                                         Bit[2]:     YUV_EN
                                                         Bit[1]:     RGB_EN
                                                         Bit[0]:     RAW_EN

                                                     Module Enable
                                                         Bit[7]:     CIP
                                                         Bit[6]:     DMY
                                                         Bit[5]:     RAW_GMA
         C3           CTRL1          FF        RW        Bit[4]:     DG
                                                         Bit[3]:     AWB
                                                         Bit[2]:     AWB_GAIN
                                                         Bit[1]:     LENC
                                                         Bit[0]:     PRE

       C4-D2          RSVD           XX         –    Reserved




Version 1.6, February 28, 2006                         Proprietary to OmniVision Technologies            19

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 7D | BPDATA[7:0] | 00 | RW | SDE Indirect Register Access: Data |
| 7E-85 | RSVD | XX | – | Reserved |
| 86 | CTRL2 | 0D | RW | Module Enable Bit[7:6]: Reserved Bit[5]: DCW Bit[4]: SDE Bit[3]: UV_ADJ Bit[2]: UV_AVG Bit[1]: Reserved Bit[0]: CMX |
| 87 | CTRL3 | 50 | RW | Module Enable Bit[7]: BPC Bit[6]: WPC Bit[5:0]: Reserved |
| 88-8B | RSVD | XX | – | Reserved |
| 8C | SIZEL[5:0] | 00 | RW | {HSIZE[11], HSIZE[2:0], VSIZE[2:0]} |
| 8D-BF | RSVD | XX | – | Reserved |
| C0 | HSIZE8[7:0] | 80 | RW | Image Horizontal Size HSIZE[10:3] |
| C1 | VSIZE8[7:0] | 60 | RW | Image Vertical Size VSIZE[10:3] |
| C2 | CTRL0 | 0C | RW | Module Enable Bit[7]: AEC_EN Bit[6]: AEC_SEL Bit[5]: STAT_SEL Bit[4]: VFIRST Bit[3]: YUV422 Bit[2]: YUV_EN Bit[1]: RGB_EN Bit[0]: RAW_EN |
| C3 | CTRL1 | FF | RW | Module Enable Bit[7]: CIP Bit[6]: DMY Bit[5]: RAW_GMA Bit[4]: DG Bit[3]: AWB Bit[2]: AWB_GAIN Bit[1]: LENC Bit[0]: PRE |
| C4-D2 | RSVD | XX | – | Reserved |


<!-- page 20 -->

OV2640            Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                         Omni   ision


     Table 12     Device Control Register List (when 0xFF = 00) (Sheet 3 of 4)

      Address         Register         Default
       (Hex)           Name             (Hex)        R/W                                 Description

                                                                 Bit[7]:     Auto mode
                                                                 Bit[6:0]:   DVP output speed control
         D3          R_DVP_SP             82             RW
                                                                             DVP PCLK = sysclk (48)/[6:0] (YUV0);
                                                                                       = sysclk (48)/(2*[6:0]) (RAW)

       D4-D9           RSVD               XX             –    Reserved

                                                              Image Output Format Select
                                                                 Bit[7]:   Reserved
                                                                 Bit[6]:   Y8 enable for DVP
                                                                 Bit[5]:   Reserved
                                                                 Bit[4]:   JPEG output enable
                                                                           0: Non-compressed
                                                                           1: JPEG output
                                                                 Bit[3:2]: DVP output format
                                                                           00: YUV422
         DA        IMAGE_MODE             00                               01: RAW10 (DVP)
                                                                           10: RGB565
                                                                           11: Reserved
                                                                 Bit[1]:   HREF timing select in DVP JPEG output mode
                                                                           0: HREF is same as sensor
                                                                           1: HREF = VSYNC
                                                                 Bit[0]:   Byte swap enable for DVP
                                                                           0: High byte first YUYV (C2[4]=0)
                                                                               YVYU (C2[4] = 1)
                                                                           1: Low byte first UYVY (C2[4] =0)
                                                                               VYUY (C2[4] =1)

       DB-DF           RSVD               XX             –    Reserved

                                                              Reset
                                                                 Bit[7]:     Reserved
                                                                 Bit[6]:     Microcontroller
                                                                 Bit[5]:     SCCB
         E0            RESET              04             RW      Bit[4]:     JPEG
                                                                 Bit[3]:     Reserved
                                                                 Bit[2]:     DVP
                                                                 Bit[1]:     IPU
                                                                 Bit[0]:     CIF

       E1-EF           RSVD               XX             –    Reserved

         F0            MS_SP              04             RW   SCCB Master Speed

       F1-F6           RSVD               XX             –    Reserved

         F7            SS_ID                             RW   SCCB Slave ID




20              Proprietary to OmniVision Technologies                                          Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| D3 | R_DVP_SP | 82 | RW | Bit[7]: Auto mode Bit[6:0]: DVP output speed control DVP PCLK = sysclk (48)/[6:0] (YUV0); = sysclk (48)/(2*[6:0]) (RAW) |
| D4-D9 | RSVD | XX | – | Reserved |
| DA | IMAGE_MODE | 00 |  | Image Output Format Select Bit[7]: Reserved Bit[6]: Y8 enable for DVP Bit[5]: Reserved Bit[4]: JPEG output enable 0: Non-compressed 1: JPEG output Bit[3:2]: DVP output format 00: YUV422 01: RAW10 (DVP) 10: RGB565 11: Reserved Bit[1]: HREF timing select in DVP JPEG output mode 0: HREF is same as sensor 1: HREF = VSYNC Bit[0]: Byte swap enable for DVP 0: High byte first YUYV (C2[4]=0) YVYU (C2[4] = 1) 1: Low byte first UYVY (C2[4] =0) VYUY (C2[4] =1) |
| DB-DF | RSVD | XX | – | Reserved |
| E0 | RESET | 04 | RW | Reset Bit[7]: Reserved Bit[6]: Microcontroller Bit[5]: SCCB Bit[4]: JPEG Bit[3]: Reserved Bit[2]: DVP Bit[1]: IPU Bit[0]: CIF |
| E1-EF | RSVD | XX | – | Reserved |
| F0 | MS_SP | 04 | RW | SCCB Master Speed |
| F1-F6 | RSVD | XX | – | Reserved |
| F7 | SS_ID |  | RW | SCCB Slave ID |


<!-- page 21 -->

Omni    ision                                                                                                      Register Set


   Table 12       Device Control Register List (when 0xFF = 00) (Sheet 4 of 4)

       Address       Register          Default
        (Hex)         Name              (Hex)       R/W                                 Description

                                                            SCCB Slave Control
                                                                Bit[7:6]:   Reserved
                                                                Bit[5]:     Address auto-increase enable
                                                                Bit[4]:     Reserved
         F8          SS_CTRL             01         RW
                                                                Bit[3]:     SCCB enable
                                                                Bit[2]:     Delay SCCB master clock
                                                                Bit[1]:     Enable SCCB master access
                                                                Bit[0]:     Enable sensor pass through access

                                                                Bit[7]:     Microcontroller Reset
                                                                Bit[6]:     Boot ROM select
                                                                Bit[5]:     R/W 1 error for 12K-byte memory
                                                                Bit[4]:     R/W 0 error for 12K-byte memory
         F9          MC_BIST                        RW          Bit[3]:     R/W 1 error for 512-byte memory
                                                                Bit[2]:     R/W 0 error for 512-byte memory
                                                                Bit[1]:     BIST busy bit for read; One-shot reset of
                                                                            microcontroller for write
                                                                Bit[0]:     Launch BIST

         FA           MC_AL                         RW      Program Memory Pointer Address Low Byte

         FB           MC_AH                         RW      Program Memory Pointer Address High Byte

                                                            Program Memory Pointer Access Address
         FC            MC_D              80         RW
                                                            Boundary of register address to separate DSP and sensor register

         FD           P_CMD              00         RW      SCCB Protocol Command Register

         FE         P_STATUS             00         RW      SCCB Protocol Status Register

                                                            Register Bank Select
                                                                Bit[7:1]:   Reserved
         FF          RA_DLMT             7F         RW          Bit[0]:     Register bank select
                                                                            0: DSP address
                                                                            1: Sensor address

    NOTE: All other registers are factory-reserved. Please contact OmniVision Technologies for reference register settings.




Version 1.6, February 28, 2006                                Proprietary to OmniVision Technologies                          21

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| F8 | SS_CTRL | 01 | RW | SCCB Slave Control Bit[7:6]: Reserved Bit[5]: Address auto-increase enable Bit[4]: Reserved Bit[3]: SCCB enable Bit[2]: Delay SCCB master clock Bit[1]: Enable SCCB master access Bit[0]: Enable sensor pass through access |
| F9 | MC_BIST |  | RW | Bit[7]: Microcontroller Reset Bit[6]: Boot ROM select Bit[5]: R/W 1 error for 12K-byte memory Bit[4]: R/W 0 error for 12K-byte memory Bit[3]: R/W 1 error for 512-byte memory Bit[2]: R/W 0 error for 512-byte memory Bit[1]: BIST busy bit for read; One-shot reset of microcontroller for write Bit[0]: Launch BIST |
| FA | MC_AL |  | RW | Program Memory Pointer Address Low Byte |
| FB | MC_AH |  | RW | Program Memory Pointer Address High Byte |
| FC | MC_D | 80 | RW | Program Memory Pointer Access Address Boundary of register address to separate DSP and sensor register |
| FD | P_CMD | 00 | RW | SCCB Protocol Command Register |
| FE | P_STATUS | 00 | RW | SCCB Protocol Status Register |
| FF | RA_DLMT | 7F | RW | Register Bank Select Bit[7:1]: Reserved Bit[0]: Register bank select 0: DSP address 1: Sensor address |
| NOTE: All other registers are factory-reserved. Please contact OmniVision Technologies for reference register settings. |  |  |  |  |


<!-- page 22 -->

OV2640            Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                              Omni     ision


     Table 13     Device Control Register List (when 0xFF = 01) (Sheet 1 of 7)

      Address      Register       Default
       (Hex)        Name           (Hex)        R/W                                     Description

                                                         AGC Gain Control LSBs
                                                             Bit[7:0]:  Gain setting
        00           GAIN            00         RW                      •    Range: 1x to 32x
                                                         Gain = (Bit[7]+1) x (Bit[6]+1) x (Bit[5]+1) x (Bit[4]+1) x (1+Bit[3:0]/16)
                                                         Note: Set COM8[2] = 0 to disable AGC.

       01-02        RSVD             XX          –       Reserved

                                                         Common Control 1
                                                             Bit[7:6]:   Dummy frame control
                                                                         00: Reserved
                                                                         01: Allow 1 dummy frame
                                0F (UXGA)                                10: Allow 3 dummy frames
        03          COM1        0A (SVGA),      RW                       11: Allow 7 dummy frames
                                06 (CIF)                     Bit[5:4]:   Reserved
                                                             Bit[3:2]:   Vertical window end line control 2 LSBs
                                                                         (8 MSBs in VEND[7:0] (0x1A))
                                                             Bit[1:0]:   Vertical window start line control 2 LSBs
                                                                         (8 MSBs in VSTRT[7:0] (0x19))

                                                         Register 04
                                                             Bit[7]:     Horizontal mirror
                                                             Bit[6]:     Vertical flip
                                                             Bit[4]:     VREF bit[0]
        04          REG04            20         RW           Bit[3]:     HREF bit[0]
                                                             Bit[2]:     Reserved
                                                             Bit[1:0]:   AEC[1:0]
                                                                         (AEC[15:10] is in register REG45[5:0] (0x45),
                                                                         AEC[9:2] is in register AEC[7:0] (0x10))

       05-07        RSVD             XX          –       Reserved

        08          REG08            40         RW       Frame Exposure One-pin Control Pre-charge Row Number

                                                         Common Control 2
                                                             Bit[7:5]:   Reserved
                                                             Bit[4]:     Standby mode enable
                                                                         0: Normal mode
                                                                         1: Standby mode
                                                             Bit[3]:     Reserved
        09          COM2             00         RW
                                                             Bit[2]:     Pin PWDN/RESETB used as SLVS/SLHS
                                                             Bit[1:0]:   Output drive select
                                                                         00: 1x capability
                                                                         01: 3x capability
                                                                         10: 2x capability
                                                                         11: 4x capability

        0A           PIDH            26          R       Product ID Number MSB (Read only)

        0B           PIDL            41          R       Product ID Number LSB (Read only)




22              Proprietary to OmniVision Technologies                                              Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 00 | GAIN | 00 | RW | AGC Gain Control LSBs Bit[7:0]: Gain setting • Range: 1x to 32x Gain =(Bit[7]+1) x (Bit[6]+1) x (Bit[5]+1) x (Bit[4]+1) x (1+Bit[3:0]/16) Note: Set COM8[2] = 0 to disable AGC. |
| 01-02 | RSVD | XX | – | Reserved |
| 03 | COM1 | 0F (UXGA) 0A (SVGA), 06 (CIF) | RW | Common Control 1 Bit[7:6]: Dummy frame control 00: Reserved 01: Allow 1 dummy frame 10: Allow 3 dummy frames 11: Allow 7 dummy frames Bit[5:4]: Reserved Bit[3:2]: Vertical window end line control 2 LSBs (8 MSBs in VEND[7:0] (0x1A)) Bit[1:0]: Vertical window start line control 2 LSBs (8 MSBs in VSTRT[7:0] (0x19)) |
| 04 | REG04 | 20 | RW | Register 04 Bit[7]: Horizontal mirror Bit[6]: Vertical flip Bit[4]: VREF bit[0] Bit[3]: HREF bit[0] Bit[2]: Reserved Bit[1:0]: AEC[1:0] (AEC[15:10] is in register REG45[5:0] (0x45), AEC[9:2] is in register AEC[7:0] (0x10)) |
| 05-07 | RSVD | XX | – | Reserved |
| 08 | REG08 | 40 | RW | Frame Exposure One-pin Control Pre-charge Row Number |
| 09 | COM2 | 00 | RW | Common Control 2 Bit[7:5]: Reserved Bit[4]: Standby mode enable 0: Normal mode 1: Standby mode Bit[3]: Reserved Bit[2]: Pin PWDN/RESETB used as SLVS/SLHS Bit[1:0]: Output drive select 00: 1x capability 01: 3x capability 10: 2x capability 11: 4x capability |
| 0A | PIDH | 26 | R | Product ID Number MSB (Read only) |
| 0B | PIDL | 41 | R | Product ID Number LSB (Read only) |


<!-- page 23 -->

Omni    ision                                                                                               Register Set


   Table 13       Device Control Register List (when 0xFF = 01) (Sheet 2 of 7)

     Address      Register       Default
      (Hex)        Name           (Hex)    R/W                                 Description

                                                 Common Control 3
                                                     Bit[7:3]:   Reserved
                                                     Bit[2]:     Set banding manually
                                                                 0: 60 Hz
        0C         COM3            38      RW                    1: 50 Hz
                                                     Bit[1]:     Auto set banding
                                                     Bit[0]:     Snapshot option
                                                                 0: Enable live video output after snapshot sequence
                                                                 1: Output single frame only

                                                 Common Control 4
                                                     Bit[7:3]:   Reserved
                                                     Bit[2]:     Clock output power-down pin status
        0D         COM4            07      RW
                                                                 0: Tri-state data output pin upon power-down
                                                                 1: Data output pin hold at last state before power-down
                                                     Bit[1:0]:   Reserved

       0E-0F       RSVD            XX       –    Reserved

                                                 Automatic Exposure Control 8 bits for AEC[9:2] (AEC[15:10] is in
                                                 register REG45[5:0] (0x45), AEC[1:0] is in register REG04[1:0] (0x04))
                                                     AEC[15:0]: Exposure time
        10          AEC            33      RW
                                                 TEX = tLINE x AEC[15:0]

                                                 Note: The maximum exposure time is 1 frame period even if TEX is
                                                 longer than 1 frame period.

                                                 Clock Rate Control
                                                     Bit[7]:     Internal frequency doublers ON/OFF selection
                                                                 0: OFF
                                                                 1: ON
        11         CLKRC           00      RW
                                                     Bit[6]:     Reserved
                                                     Bit[5:0]:   Clock divider

                                                 CLK = XVCLK/(decimal value of CLKRC[5:0] + 1)




Version 1.6, February 28, 2006                          Proprietary to OmniVision Technologies                         23

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 0C | COM3 | 38 | RW | Common Control 3 Bit[7:3]: Reserved Bit[2]: Set banding manually 0: 60 Hz 1: 50 Hz Bit[1]: Auto set banding Bit[0]: Snapshot option 0: Enable live video output after snapshot sequence 1: Output single frame only |
| 0D | COM4 | 07 | RW | Common Control 4 Bit[7:3]: Reserved Bit[2]: Clock output power-down pin status 0: Tri-state data output pin upon power-down 1: Data output pin hold at last state before power-down Bit[1:0]: Reserved |
| 0E-0F | RSVD | XX | – | Reserved |
| 10 | AEC | 33 | RW | Automatic Exposure Control 8 bits for AEC[9:2] (AEC[15:10] is in register REG45[5:0] (0x45), AEC[1:0] is in register REG04[1:0] (0x04)) AEC[15:0]: Exposure time T = t x AEC[15:0] EX LINE Note: The maximum exposure time is 1 frame period even if TEX is longer than 1 frame period. |
| 11 | CLKRC | 00 | RW | Clock Rate Control Bit[7]: Internal frequency doublers ON/OFF selection 0: OFF 1: ON Bit[6]: Reserved Bit[5:0]: Clock divider CLK = XVCLK/(decimal value of CLKRC[5:0] + 1) |


<!-- page 24 -->

OV2640            Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                             Omni     ision


     Table 13     Device Control Register List (when 0xFF = 01) (Sheet 3 of 7)

      Address      Register       Default
       (Hex)        Name           (Hex)        R/W                                    Description

                                                         Common Control 7
                                                            Bit[7]:     SRST
                                                                        1: Initiates system reset. All registers are set to factory
                                                                            default values after which the chip resumes normal
                                                                            operation
                                                            Bit[6:4]:   Resolution selection
                                                                        000: UXGA (full size) mode
        12          COM7             00         RW                      001: CIF mode
                                                                        100: SVGA mode
                                                            Bit[3]:     Reserved
                                                            Bit[2]:     Zoom mode
                                                            Bit[1]:     Color bar test pattern
                                                                        0: OFF
                                                                        1: ON
                                                            Bit[0]:     Reserved

                                                         Common Control 8
                                                            Bit[7:6]:   Reserved
                                                            Bit[5]:     Banding filter selection
                                                                        0: OFF
                                                                        1: ON, set minimum exposure time to 1/120s
                                                            Bit[4:3]:   Reserved
        13          COM8             C7         RW          Bit[2]:     AGC auto/manual control selection
                                                                        0: Manual
                                                                        1: Auto
                                                            Bit[1]:     Reserved
                                                            Bit[0]:     Exposure control
                                                                        0: Manual
                                                                        1: Auto

                                                         Common Control 9
                                                            Bit[7:5]:   AGC gain ceiling, GH[2:0]
                                                                        000: 2x
                                                                        001: 4x
                                                                        010: 8x
        14          COM9             50         RW
                                                                        011: 16x
                                                                        100: 32x
                                                                        101: 64x
                                                                        11x: 128x
                                                            Bit[4:0]:   Reserved




24              Proprietary to OmniVision Technologies                                             Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 12 | COM7 | 00 | RW | Common Control 7 Bit[7]: SRST 1: Initiates system reset. All registers are set to factory default values after which the chip resumes normal operation Bit[6:4]: Resolution selection 000: UXGA (full size) mode 001: CIF mode 100: SVGA mode Bit[3]: Reserved Bit[2]: Zoom mode Bit[1]: Color bar test pattern 0: OFF 1: ON Bit[0]: Reserved |
| 13 | COM8 | C7 | RW | Common Control 8 Bit[7:6]: Reserved Bit[5]: Banding filter selection 0: OFF 1: ON, set minimum exposure time to 1/120s Bit[4:3]: Reserved Bit[2]: AGC auto/manual control selection 0: Manual 1: Auto Bit[1]: Reserved Bit[0]: Exposure control 0: Manual 1: Auto |
| 14 | COM9 | 50 | RW | Common Control 9 Bit[7:5]: AGC gain ceiling, GH[2:0] 000: 2x 001: 4x 010: 8x 011: 16x 100: 32x 101: 64x 11x: 128x Bit[4:0]: Reserved |


<!-- page 25 -->

Omni    ision                                                                                                   Register Set


   Table 13       Device Control Register List (when 0xFF = 01) (Sheet 4 of 7)

     Address      Register        Default
      (Hex)        Name            (Hex)      R/W                                 Description

                                                    Common Control 10 (if Bypass DSP is selected)
                                                        Bit[7]:     CHSYNC pin output swap
                                                                    0: CHSYNC
                                                                    1: HREF
                                                        Bit[6]:     HREF pin output swap
                                                                    0: HREF
                                                                    1: CHSYNC
                                                        Bit[5]:     PCLK output selection
                                                                    0: PCLK always output
                                                                    1: PCLK output qualified by HREF
                                                        Bit[4]:     PCLK edge selection
                                                                    0: Data is updated at the falling edge of PCLK (user
                                                                       can latch data at the next rising edge of PCLK)
        15         COM10            00        RW
                                                                    1: Data is updated at the rising edge of PCLK (user can
                                                                       latch data at the next falling edge of PCLK)
                                                        Bit[3]:     HREF output polarity
                                                                    0: Output positive HREF
                                                                    1: Output negative HREF, HREF negative for data
                                                                       valid
                                                        Bit[2]:     Reserved
                                                        Bit[1]:     VSYNC polarity
                                                                    0: Positive
                                                                    1: Negative
                                                        Bit[0]:     HSYNC polarity
                                                                    0: Positive
                                                                    1: Negative

        16         RSVD             XX         –    Reserved

                                                    Horizontal Window Start MSB 8 bits (3 LSBs in REG32[2:0] (0x32))
        17        HREFST             11       RW        Bit[10:0]: Selects the start of the horizontal window, each LSB
                                                                   represents two pixels

                                 75 (UXGA),         Horizontal Window End MSB 8 bits (3 LSBs in REG32[5:3] (0x32))
        18       HREFEND         43 (SVGA,    RW        Bit[10:0]: Selects the end of the horizontal window, each LSB
                                    CIF)                           represents two pixels

                                 01 (UXGA),         Vertical Window Line Start MSB 8 bits (2 LSBs in COM1[1:0] (0x03))
        19         VSTRT         00 (SVGA,    RW        Bit[9:0]:   Selects the start of the vertical window, each LSB
                                    CIF)                            represents two scan lines.

                                                    Vertical Window Line End MSB 8 bits (2 LSBs in COM1[3:2] (0x03))
        1A         VEND             97        RW        Bit[9:0]:   Selects the end of the vertical window, each LSB
                                                                    represents two scan lines.

        1B         RSVD             XX         –    Reserved

        1C          MIDH            7F        R     Manufacturer ID Byte – High      (Read only = 0x7F)

        1D          MIDL            A2        R     Manufacturer ID Byte – Low       (Read only = 0xA2)

       1E-23       RSVD             XX         –    Reserved




Version 1.6, February 28, 2006                             Proprietary to OmniVision Technologies                         25

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 15 | COM10 | 00 | RW | Common Control 10 (if Bypass DSP is selected) Bit[7]: CHSYNC pin output swap 0: CHSYNC 1: HREF Bit[6]: HREF pin output swap 0: HREF 1: CHSYNC Bit[5]: PCLK output selection 0: PCLK always output 1: PCLK output qualified by HREF Bit[4]: PCLK edge selection 0: Data is updated at the falling edge of PCLK (user can latch data at the next rising edge of PCLK) 1: Data is updated at the rising edge of PCLK (user can latch data at the next falling edge of PCLK) Bit[3]: HREF output polarity 0: Output positive HREF 1: Output negative HREF, HREF negative for data valid Bit[2]: Reserved Bit[1]: VSYNC polarity 0: Positive 1: Negative Bit[0]: HSYNC polarity 0: Positive 1: Negative |
| 16 | RSVD | XX | – | Reserved |
| 17 | HREFST | 11 | RW | Horizontal Window Start MSB 8 bits (3 LSBs in REG32[2:0] (0x32)) Bit[10:0]: Selects the start of the horizontal window, each LSB represents two pixels |
| 18 | HREFEND | 75 (UXGA), 43 (SVGA, CIF) | RW | Horizontal Window End MSB 8 bits (3 LSBs in REG32[5:3] (0x32)) Bit[10:0]: Selects the end of the horizontal window, each LSB represents two pixels |
| 19 | VSTRT | 01 (UXGA), 00 (SVGA, CIF) | RW | Vertical Window Line Start MSB 8 bits (2 LSBs in COM1[1:0] (0x03)) Bit[9:0]: Selects the start of the vertical window, each LSB represents two scan lines. |
| 1A | VEND | 97 | RW | Vertical Window Line End MSB 8 bits (2 LSBs in COM1[3:2] (0x03)) Bit[9:0]: Selects the end of the vertical window, each LSB represents two scan lines. |
| 1B | RSVD | XX | – | Reserved |
| 1C | MIDH | 7F | R | Manufacturer ID Byte – High (Read only = 0x7F) |
| 1D | MIDL | A2 | R | Manufacturer ID Byte – Low (Read only = 0xA2) |
| 1E-23 | RSVD | XX | – | Reserved |


<!-- page 26 -->

OV2640            Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                               Omni     ision


     Table 13     Device Control Register List (when 0xFF = 01) (Sheet 5 of 7)

      Address      Register       Default
       (Hex)        Name           (Hex)        R/W                                     Description

                                                         Luminance Signal High Range for AEC/AGC Operation
        24           AEW             78         RW       AEC/AGC values will decrease in auto mode when average luminance
                                                         is greater than AEW[7:0]

                                                         Luminance Signal Low Range for AEC/AGC Operation
        25           AEB             68         RW       AEC/AGC values will increase in auto mode when average luminance
                                                         is less than AEB[7:0]

                                                         Fast Mode Large Step Range Threshold - effective only in AEC/AGC
                                                         fast mode (COM8[7] = 1)
                                                             Bit[7:4]: High threshold
        26            VV             D4         RW           Bit[3:0]:Low threshold

                                                         Note: AEC/AGC may change in larger steps when luminance average
                                                         is greater than VV[7:4] or less than VV[3:0].

       27-29        RSVD             XX          –       Reserved

                                                         Register 2A
                                                             Bit[7:4]:   Line interval adjust value 4 MSBs (LSBs in FRARL[7:0]
                                                                         (0x2B))
        2A          REG2A            00         RW           Bit[3:2]:   HSYNC timing end point adjustment MSB 2 bits
                                                                         (LSBs in register HEDY[7:0] (0x31))
                                                             Bit[1:0]:   HSYNC timing start point adjustment MSB 2 bits
                                                                         (LSBs in register HSDY[7:0] (0x30))

                                                         Line Interval Adjustment Value LSB 8 bits (MSBs in REG2A[7:4]
                                                         (0x2A))

        2B          FRARL            00         RW
                                                         The frame rate will be adjusted by changing the line interval. Each LSB
                                                         will add 1/1922 Tframe in UXGA and 1/1190 Tframe in SVGA mode to te
                                                         frame period.

        2C          RSVD             XX          –       Reserved

                                                         VSYNC Pulse Width LSB 8 bits
        2D         ADDVSL            00         RW           Bit[7:0]:   Line periods added to VSYNC width. Default VSYNC
                                                                         output width is 4 x tline. Each LSB count will add 1 x tline
                                                                         to the VSYNC active period.

                                                         VSYNC Pulse Width MSB 8 bits
        2E         ADDVSH            00         RW           Bit[7:0]:   Line periods added to VSYNC width. Default VSYNC
                                                                         output width is 4 x tline. Each MSB count will add
                                                                         256 x tline to the VSYNC active period.

                                                         Luminance Average (this register will auto update)
                                                         Average Luminance is calculated from the B/Gb/Gr/R channel average
                                                         as follows:
        2F           YAVG            00         RW

                                                         B/Gb/Gr/R channel average =
                                                         (BAVG[7:0] + (2 x GbAVG[7:0]) + RAVG[7:0]) x 0.25

                                                         HSYNC Position and Width, Start Point LSB 8 bits
        30          HSDY             08         RW       This register and REG2A[1:0] (0x2A) define HSYNC start position,
                                                         each LSB will shift HSYNC start by 2 pixel period


26              Proprietary to OmniVision Technologies                                              Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 24 | AEW | 78 | RW | Luminance Signal High Range for AEC/AGC Operation AEC/AGC values will decrease in auto mode when average luminance is greater than AEW[7:0] |
| 25 | AEB | 68 | RW | Luminance Signal Low Range for AEC/AGC Operation AEC/AGC values will increase in auto mode when average luminance is less than AEB[7:0] |
| 26 | VV | D4 | RW | Fast Mode Large Step Range Threshold - effective only in AEC/AGC fast mode (COM8[7] = 1) Bit[7:4]: High threshold Bit[3:0]:Low threshold Note: AEC/AGC may change in larger steps when luminance average is greater than VV[7:4] or less than VV[3:0]. |
| 27-29 | RSVD | XX | – | Reserved |
| 2A | REG2A | 00 | RW | Register 2A Bit[7:4]: Line interval adjust value 4 MSBs (LSBs in FRARL[7:0] (0x2B)) Bit[3:2]: HSYNC timing end point adjustment MSB 2 bits (LSBs in register HEDY[7:0] (0x31)) Bit[1:0]: HSYNC timing start point adjustment MSB 2 bits (LSBs in register HSDY[7:0] (0x30)) |
| 2B | FRARL | 00 | RW | Line Interval Adjustment Value LSB 8 bits (MSBs in REG2A[7:4] (0x2A)) The frame rate will be adjusted by changing the line interval. Each LSB will add 1/1922 T in UXGA and 1/1190 T in SVGA mode to te frame frame frame period. |
| 2C | RSVD | XX | – | Reserved |
| 2D | ADDVSL | 00 | RW | VSYNC Pulse Width LSB 8 bits Bit[7:0]: Line periods added to VSYNC width. Default VSYNC output width is 4 x t . Each LSB count will add 1 x t line line to the VSYNC active period. |
| 2E | ADDVSH | 00 | RW | VSYNC Pulse Width MSB 8 bits Bit[7:0]: Line periods added to VSYNC width. Default VSYNC output width is 4 x t . Each MSB count will add line 256xt to the VSYNC active period. line |
| 2F | YAVG | 00 | RW | Luminance Average (this register will auto update) Average Luminance is calculated from the B/Gb/Gr/R channel average as follows: B/Gb/Gr/R channel average = (BAVG[7:0] + (2 x GbAVG[7:0]) + RAVG[7:0]) x 0.25 |
| 30 | HSDY | 08 | RW | HSYNC Position and Width, Start Point LSB 8 bits This register and REG2A[1:0] (0x2A) define HSYNC start position, each LSB will shift HSYNC start by 2 pixel period |


<!-- page 27 -->

Omni    ision                                                                                                  Register Set


   Table 13       Device Control Register List (when 0xFF = 01) (Sheet 6 of 7)

     Address      Register        Default
      (Hex)        Name            (Hex)      R/W                                  Description

                                                    HSYNC Position and Width, End Point LSB 8 bits
        31         HEDY             30        RW        This register and REG2A[3:2] (0x2A) define HSYNC end position,
                                                        each LSB will shift HSYNC end by 2 pixel period

                                                    Common Control 32
                                                        Bit[7:6]:   Pixel clock divide option
                                                                    00: No effect on PCLK
                                 36 (UXGA),                         01: No effect on PCLK
        32         REG32         09 (SVGA,    RW                    10: PCLK frequency divide by 2
                                    CIF)                            11: PCLK frequency divide by 4
                                                        Bit[5:3]:   Horizontal window end position 3 LSBs (8 MSBs in
                                                                    register HREFEND[7:0] (0x18))
                                                        Bit[2:0]:   Horizontal window start position 3 LSBs (8 MSBs in
                                                                    register HREFST[7:0] (0x17))

        33         RSVD             XX         –    Reserved

                                                        Bit[7:3]:   Reserved
        34        ARCOM2            20        RW        Bit[2]:     Zoom window horizontal start point
                                                        Bit[1:0]:   Reserved

       35-44       RSVD             XX         –    Reserved

                                                    Register 45
        45         REG45            00        RW        Bit[7:6]:   AGC[9:8], AGC highest gain control
                                                        Bit[5:0]:   AEC[15:10], AEC MSBs

                                                    Frame Length Adjustment LSBs
        46           FLL            00        RW
                                                    Each bit will add 1 horizontal line timing in frame

                                                    Frame Length Adjustment MSBs
        47          FLH             00        RW
                                                    Each bit will add 256 horizontal lines timing in frame

                                                    Common Control 19
        48         COM19            00        RW        Bit[7:2]:   Reserved
                                                        Bit[1:0]:   Zoom mode vertical window start point 2 LSBs

        49        ZOOMS             00        RW    Zoom Mode Vertical Window Start Point 8 MSBs

        4A         RSVD             XX         –    Reserved

                                                    Common Control 22
        4B         COM22            20        RW
                                                        Bit[7:0]:   Flash light control

       4C-4D       RSVD             XX         –    Reserved

                                                    Common Control 25 - reserved for banding
                                                        Bit[7:6]:   50Hz Banding AEC 2 MSBs
        4E         COM25            00        RW
                                                        Bit[5:4]:   60HZ Banding AEC 2 MSBs
                                                        Bit[3:0]:   Reserved

        4F          BD50            CA        RW    50Hz Banding AEC 8 LSBs

        50          BD60            A8        RW    60Hz Banding AEC 8 LSBs

       51-5C       RSVD             XX         –    Reserved


Version 1.6, February 28, 2006                              Proprietary to OmniVision Technologies                       27

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 31 | HEDY | 30 | RW | HSYNC Position and Width, End Point LSB 8 bits This register and REG2A[3:2] (0x2A) define HSYNC end position, each LSB will shift HSYNC end by 2 pixel period |
| 32 | REG32 | 36 (UXGA), 09 (SVGA, CIF) | RW | Common Control 32 Bit[7:6]: Pixel clock divide option 00: No effect on PCLK 01: No effect on PCLK 10: PCLK frequency divide by 2 11: PCLK frequency divide by 4 Bit[5:3]: Horizontal window end position 3 LSBs (8 MSBs in register HREFEND[7:0] (0x18)) Bit[2:0]: Horizontal window start position 3 LSBs (8 MSBs in register HREFST[7:0] (0x17)) |
| 33 | RSVD | XX | – | Reserved |
| 34 | ARCOM2 | 20 | RW | Bit[7:3]: Reserved Bit[2]: Zoom window horizontal start point Bit[1:0]: Reserved |
| 35-44 | RSVD | XX | – | Reserved |
| 45 | REG45 | 00 | RW | Register 45 Bit[7:6]: AGC[9:8], AGC highest gain control Bit[5:0]: AEC[15:10], AEC MSBs |
| 46 | FLL | 00 | RW | Frame Length Adjustment LSBs Each bit will add 1 horizontal line timing in frame |
| 47 | FLH | 00 | RW | Frame Length Adjustment MSBs Each bit will add 256 horizontal lines timing in frame |
| 48 | COM19 | 00 | RW | Common Control 19 Bit[7:2]: Reserved Bit[1:0]: Zoom mode vertical window start point 2 LSBs |
| 49 | ZOOMS | 00 | RW | Zoom Mode Vertical Window Start Point 8 MSBs |
| 4A | RSVD | XX | – | Reserved |
| 4B | COM22 | 20 | RW | Common Control 22 Bit[7:0]: Flash light control |
| 4C-4D | RSVD | XX | – | Reserved |
| 4E | COM25 | 00 | RW | Common Control 25 - reserved for banding Bit[7:6]: 50Hz Banding AEC 2 MSBs Bit[5:4]: 60HZ Banding AEC 2 MSBs Bit[3:0]: Reserved |
| 4F | BD50 | CA | RW | 50Hz Banding AEC 8 LSBs |
| 50 | BD60 | A8 | RW | 60Hz Banding AEC 8 LSBs |
| 51-5C | RSVD | XX | – | Reserved |


<!-- page 28 -->

OV2640            Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                         Omni    ision


     Table 13      Device Control Register List (when 0xFF = 01) (Sheet 7 of 7)

      Address      Register        Default
       (Hex)        Name            (Hex)       R/W                                   Description

                                                         Register 5D
        5D          REG5D            00         RW
                                                             Bit[7:0]:   AVGsel[7:0], 16-zone average weight option

                                                         Register 5E
         5E         REG5E            00         RW
                                                             Bit[7:0]:   AVGsel[15:8], 16-zone average weight option

                                                         Register 5F
         5F         REG5F            00         RW
                                                             Bit[7:0]:   AVGsel[23:16], 16-zone average weight option

                                                         Register 60
         60         REG60            00         RW
                                                             Bit[7:0]:   AVGsel[31:24], 16-zone average weight option

         61      HISTO_LOW           80         RW       Histogram Algorithm Low Level

         62      HISTO_HIGH          90         RW       Histogram Algorithm High Level

       63-7E         RSVD            XX          –       Reserved

     NOTE: All other registers are factory-reserved. Please contact OmniVision Technologies for reference register settings.




28              Proprietary to OmniVision Technologies                                           Version 1.6, February 28, 2006

**Extracted table(s) on this page:**

| Address (Hex) | Register Name | Default (Hex) | R/W | Description |
| --- | --- | --- | --- | --- |
| 5D | REG5D | 00 | RW | Register 5D Bit[7:0]: AVGsel[7:0], 16-zone average weight option |
| 5E | REG5E | 00 | RW | Register 5E Bit[7:0]: AVGsel[15:8], 16-zone average weight option |
| 5F | REG5F | 00 | RW | Register 5F Bit[7:0]: AVGsel[23:16], 16-zone average weight option |
| 60 | REG60 | 00 | RW | Register 60 Bit[7:0]: AVGsel[31:24], 16-zone average weight option |
| 61 | HISTO_LOW | 80 | RW | Histogram Algorithm Low Level |
| 62 | HISTO_HIGH | 90 | RW | Histogram Algorithm High Level |
| 63-7E | RSVD | XX | – | Reserved |
| NOTE: All other registers are factory-reserved. Please contact OmniVision Technologies for reference register settings. |  |  |  |  |


<!-- page 29 -->

Omni   ision                                                                                                                                                Package Specifications


Package Specifications
   The OV2640 uses a 38-ball Chip Scale Package 2 (CSP2). Refer to Figure 11 for package information, Table 9 for package
   dimensions and Figure 12 for the array center on the chip.

                                  Note: For OVT devices that are lead-free, all part marking letters are
                                  lower case. Underlining the last digit of the lot number indicates CSP2 is
                                  used.

Figure 21 OV2640 Package Specifications

                                                        A                                              S1       J1
                                       1    2       3       4         5    6                                6        5     4        3   2     1


                                                                                    A           S2                                                      A


                                                                                    B                                                                   B
                                                                                                J2
                                                                                    C                                                                   C

                                                                                                                         wxyz
                                                                                                                         abcd
                         B                                                          D                                                                   D


                                                                                    E                                                                   E


                                                                                    F                                                                   F


                                                                                    G                                                                   G




                                           Top View (Bumps Down)                                                     Bottom View (Bumps Up)
                                                                               Center of BGA (die) =
                                                                               Center of the package

                                            Glass
                                                                Die                                             Part Marking Code:
                             C2
                                                                                                                w      - OVT Product Version
                                                                                   C3                           x      - Year the part is assembled
                                                                                           C                    y      - Month the part is assembled
                                                                                                                z      - Wafer number
                                                                                    C4                          abcd - Last four digits of lot number
                                  C1                Side View



   Table 14          OV2640 Package Dimensions

                   Parameter                                          Symbol             Minimum                          Nominal                 Maximum                Unit
 Package Body Dimension X                                                 A                  5700                           5725                        5750              µm
 Package Body Dimension Y                                                 B                  6260                           6285                        6310              µm
 Package Height                                                           C                    845                             905                          965           µm
 Ball Height                                                              C1                   150                             180                          210           µm
 Package Body Thickness                                                   C2                   680                             725                          770           µm
 Cover Glass Thickness                                                    C3                   375                             400                          425           µm
 Airgap Between Cover Glass and Sensor                                    C4                   30                              45                           60            µm
 Ball Diameter                                                            D                    320                             350                          380           µm
 Total Pin Count                                                          N                                              38 (1 NC)
 Pin Count X-axis                                                         N1                                                    6
 Pin Count Y-axis                                                         N2                                                    7
 Pins Pitch X-axis                                                        J1                                                   800                                        µm
 Pins Pitch Y-axis                                                        J2                                                   800                                        µm
 Edge-to-Pin Center Distance Analog X                                     S1                   833                             863                          893           µm
 Edge-to-Pin Center Distance Analog Y                                     S2                   713                             743                          773           µm

Version 1.6, February 28, 2006                                                            Proprietary to OmniVision Technologies                                                29

**Extracted table(s) on this page:**

| Parameter | Symbol | Minimum | Nominal | Maximum | Unit |
| --- | --- | --- | --- | --- | --- |
| Package Body Dimension X | A | 5700 | 5725 | 5750 | µm |
| Package Body Dimension Y | B | 6260 | 6285 | 6310 | µm |
| Package Height | C | 845 | 905 | 965 | µm |
| Ball Height | C1 | 150 | 180 | 210 | µm |
| Package Body Thickness | C2 | 680 | 725 | 770 | µm |
| Cover Glass Thickness | C3 | 375 | 400 | 425 | µm |
| Airgap Between Cover Glass and Sensor | C4 | 30 | 45 | 60 | µm |
| Ball Diameter | D | 320 | 350 | 380 | µm |
| Total Pin Count | N |  | 38 (1 NC) |  |  |
| Pin Count X-axis | N1 |  | 6 |  |  |
| Pin Count Y-axis | N2 |  | 7 |  |  |
| Pins Pitch X-axis | J1 |  | 800 |  | µm |
| Pins Pitch Y-axis | J2 |  | 800 |  | µm |
| Edge-to-Pin Center Distance Analog X | S1 | 833 | 863 | 893 | µm |
| Edge-to-Pin Center Distance Analog Y | S2 | 713 | 743 | 773 | µm |


<!-- page 30 -->

OV2640       Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                                                      Omni    ision


Sensor Array Center

Figure 22 OV2640 Sensor Array Center




                                          A1     A2      A3     A4     A5      A6




                                                                                               A rray C enter
                                                              3590.4 μm                        (469.6 μm, 145 μm)

                                                  2684 μm



                                                                          S ens or
                                                                            A rray




                                                                             OV 2640

                                      P ac kage C enter
                                            (0, 0)
                                                      T op V iew

               NOT E S : 1. T his drawing is not to s cale and is for reference only.
                         2. As mos t optical as s emblies invert and mirror the image, the chip is typically mounted
                            with pins A1 to A6 oriented down on the P C B .




30         Proprietary to OmniVision Technologies                                                        Version 1.6, February 28, 2006

<!-- page 31 -->

Omni                         ision                                                                                                                                         Package Specifications


IR Reflow Ramp Rate Requirements

                     OV2640 Lead-Free Packaged Devices

                                                             Note: For OVT devices that are lead-free, all part marking letters are
                                                             lower case

Figure 23 IR Reflow Ramp Rate Requirements

                     300.0
                                          Z1                 Z2              Z3               Z4                  Z5                Z6                Z7                  end
                     280.0

                     260.0

                     240.0

                     220.0

                     200.0

                     180.0
 Temperature ( C )




                     160.0

                     140.0

                     120.0

                     100.0

                      80.0

                      60.0

                      40.0

                      20.0
                                          0.0                0.6             1.1              1.6                 2.2               2.8               3.3           3.9
                       0.0
                             -22     -2          18     38         58   78         98   118         138     158         178   198         218   238     258   278         298   318   338   358 369
                                                                                                              Time (sec)




                     Table 15                   Reflow Conditions

                                                      Condition                                                                                 Exposure
                      Average Ramp-up Rate (30°C to 217°C)                                          Less than 3°C per second
                      > 100°C                                                                       Between 330 - 600 seconds
                      > 150°C                                                                       At least 210 seconds
                      > 217°C                                                                       At least 30 seconds (30 ~ 120 seconds)
                      Peak Temperature                                                              245°C
                      Cool-down Rate (Peak to 50°C)                                                 Less than 6°C per second
                      Time from 30°C to 245°C                                                       No greater than 390 seconds




Version 1.6, February 28, 2006                                                                                Proprietary to OmniVision Technologies                                             31

**Extracted table(s) on this page:**

| Condition | Exposure |
| --- | --- |
| Average Ramp-up Rate (30°C to 217°C) | Less than 3°C per second |
| > 100°C | Between 330 - 600 seconds |
| > 150°C | At least 210 seconds |
| > 217°C | At least 30 seconds (30 ~ 120 seconds) |
| Peak Temperature | 245°C |
| Cool-down Rate (Peak to 50°C) | Less than 6°C per second |
| Time from 30°C to 245°C | No greater than 390 seconds |


<!-- page 32 -->

OV2640           Color CMOS UXGA (2.0 MegaPixel) OmniPixel2™ CAMERACHIP™                             Omni     ision


     Note:

     •   All information shown herein is current as of the revision and publication date. Please refer
         to the OmniVision web site (http://www.ovt.com) to obtain the current versions of all
         documentation.


     •   OmniVision Technologies, Inc. reserves the right to make changes to their products or to
         discontinue any product or service without further notice (It is advisable to obtain current product
         documentation prior to placing orders).


     •   Reproduction of information in OmniVision product documentation and specifications is
         permissible only if reproduction is without alteration and is accompanied by all associated
         warranties, conditions, limitations and notices. In such cases, OmniVision is not responsible
         or liable for any information reproduced.


     •   This document is provided with no warranties whatsoever, including any warranty of
         merchantability, non-infringement, fitness for any particular purpose, or any warranty
         otherwise arising out of any proposal, specification or sample. Furthermore, OmniVision
         Technologies Inc. disclaims all liability, including liability for infringement of any proprietary
         rights, relating to use of information in this document. No license, expressed or implied, by
         estoppels or otherwise, to any intellectual property rights is granted herein.


     •   ‘OmniVision’, ‘VarioPixel’, and ’OmniPixel2’ are trademarks of OmniVision Technologies, Inc.
         All other trade, product or service names referenced in this release may be trademarks or
         registered trademarks of their respective holders. Third-party brands, names, and trademarks are
         the property of their respective owners.




     For further information, please feel free to contact OmniVision at info@ovt.com.




     OmniVision Technologies, Inc.
     1341 Orleans Drive
     Sunnyvale, CA USA
     (408) 542-3000




32             Proprietary to OmniVision Technologies                               Version 1.6, February 28, 2006

<!-- page 33 -->

Omni                ision      TM




                       REVISION CHANGE LIST

Document Title: OV2640 Datasheet              Version: 1.0

                     DESCRIPTION OF CHANGES
Initial Release

<!-- page 34 -->

Omni                       ision      TM




                              REVISION CHANGE LIST
Document Title: OV2640 Datasheet                                Version: 1.01

                            DESCRIPTION OF CHANGES
The following changes were made to version 1.0:
   • Under Key Specifications on page 1, changed specification for Core Power Supply from
       “1.2VDC + 10%” to “1.2VDC + 5%”
   • Under Key Specifications on page 1, changed specification for Analog Power Supply
       from “2.8VDC + 10%” to “2.5 ~ 3.0VDC”
   • Under Key Specifications on page 1, changed specification for I/O Power Supply from
       “1.8V to 3.3V” to “1.7V to 3.3V”
   • On pages 17 to 20, changed title of Table 12 from “Device Control Register (for 0x00 ~
       0xFF at 0xF8 = 00 and 0xFF = 00)” to “Device Control Register (when 0xFF = 00)”
   • On pages 21 to 27, changed title of Table 13 from “Device Control Register (for 0x00 ~
       0x7E at 0xF8 = 01 and 0xFF = 7F)” to “Device Control Register (when 0xFF = 01)”
   • In Table 12 on pages 18, changed description of register CTRL3 (0x87) from:
        Module Enable
            Bit[7:6]:   Reserved
            Bit[5]:     DCW
            Bit[4]:     SDE
            Bit[3]:     UV_ADJ
            Bit[2]:     UV_AVG
            Bit[1]:     Reserved
            Bit[0]:     CMX
       to
        Module Enable
           Bit[7]:   BPC
           Bit[6]:   WPC
           Bit[5:0]: Reserved
   •   In Table 15 on page 30, changed specification for Peak Temperature from “Greater than
       245°C” to “245°C”

<!-- page 35 -->

Omni                     ision         TM




                             REVISION CHANGE LIST

Document Title: OV2640 Datasheet                                  Version: 1.1

                          DESCRIPTION OF CHANGES
The following changes were made to version 1.01:
   • Under Features on page 1, changed bulleted item from “Supports image sizes: UXGA,
       SVGA, and any size scaling down from SVGA to 40x30” to “Supports image sizes:
       UXGA, SXGA, SVGA, and any size scaling down from SXGA to 40x30”
   • Under Key Specifications on page 1, deleted specifications for SVGA and CIF Array Size
   • Under Key Specifications on page 1, changed Standby Power Requirements specification
       to “TBD”
   • Under Key Specifications on page 1, changed specification for Chief Ray Angle from
       “TBD” to “25° non-linear”
   • Under Key Specifications on page 1, changed specification for Well Capacity from
       “TBD” to “12 Ke”
   • Under Electrical Characteristics on page 10, changed title of Table 6 from “DC
       Characteristics (-20°C < TA < 70°C)” to “DC Characteristics (-30°C < TA < 70°C)”
   •   In Table 6 on page 10, changed specification for Typ Standby Current from “10” to
       “TBD”
   •   In Table 6 on page 10, changed specification for Max Input voltage LOW (VIL) from
       “0.8” to “0.54”
   •   In Table 6 on page 10, changed specification for Min Input voltage HIGH (VIH) from “2”
       to “1.26”
   •   In Table 6 on page 10, changed subtitle “Digital Outputs (standard loading 25 pF, 1.2 KΩ
       to 2.8V)” to “Digital Outputs (standard loading 25 pF)”
   •   In Table 6 on page 10, changed specification for Min Output voltage HIGH (VOH) from
       “2.2” to “1.62”
   •   In Table 6 on page 10, changed specification for Max Output voltage LOW (VOL) from
       “0.6” to “0.18”
   •   In Table 6 on page 10, changed specification for Serial Interface Inputs Max SIO_C and
       SIO_D (VIL) from “1” to “0.54”
   •   In Table 6 on page 10, changed specification for Serial Interface Inputs Min, Typ, and
       Max SIO_C and SIO_D (VIH) from “2.5, 2.8, and VDD-IO + 0.5” to “1.26, 1.8, and 2.3”,
       respectively
   •   In Table 6 on page 10, changed table footnote b from “...VDD-IO = 2.8V” to
       “...VDD-IO = 1.8V”

<!-- page 36 -->

Omni                   ision         TM




             DESCRIPTION OF CHANGES (CONTINUED)
 •   In Figure 21 on page 28, changed callout C3 to measure from thickness of glass and added
     callout C4 to measure airgap from glass to die.
 •   In Table 14 on page 28, changed C3 parameter name from “Thickness of Glass Surface to
     Wafer” to “Cover Glass Thickness”
 •   In Table 14 on page 28, changed C3 Minimum, Nominal, and Maximum specifications
     from “425, 445, and 465” to “375, 400, and 425”
 •   In Table 14 on page 28, added C4 parameter, Airgap Between Cover Glass and Sensor,
     and Minimum, Nominal, and Maximum specifications “30, 45, and 60”, respectively

<!-- page 37 -->

Omni                     ision        TM




                             REVISION CHANGE LIST
Document Title: OV2640 Datasheet                                 Version: 1.2

                          DESCRIPTION OF CHANGES
The following changes were made to version 1.1:
   • Under Key Specifications on page 1, changed Active Power Requirements specification to
       “TBD” to “125 mW (for 15 fps, UXGA YUV mode)” and “140 mW (for 15 fps, UXGA
       compressed mode)”
   • Under Key Specifications on page 1, changed Standby Power Requirements specification
       to “TBD” to “600 µA”
   • Under Key Specifications on page 1, deleted Preview (CIF) Power Requirements
       specification
   • In Table 6 on page 10, changed specification for Typ Active (Operating) Current (IDDA-A)
       from “TBD” to “30”
   • In Table 6 on page 10, changed specification for Typ Active (Operating) Current (IDDA-D)
       from “TBD” to “25 (YUV)” and “35 (Compressed)”
   • In Table 6 on page 10, changed specification for Typ Active (Operating) Current (IDDA-
       IO) from “TBD” to “6”
   •   IIn Table 6 on page 10, changed specification for Typ Standby Current from “10” to “600”
   •   In Table 6 on page 10, changed table footnote b from “...VDD-IO = 1.8V” to
       “...VDD-IO = 1.8V for 15 fps in UXGA mode”

<!-- page 38 -->

Omni                     ision         TM




                             REVISION CHANGE LIST
Document Title: OV2640 Datasheet                                  Version: 1.21

                           DESCRIPTION OF CHANGES
The following changes were made to version 1.2:
   • In Figure 1 on page 21, corrected the bottom view of the package by correcting the column
       numbers corresponding to the ball locations from (left to right) “1”, “2”, “3”, “4”, “5”,
       and “6” to (left to right) “6”, “5”, “4”, “3”, “2”, and “1”, respectively

<!-- page 39 -->

Omni                     ision         TM




                             REVISION CHANGE LIST
Document Title: OV2640 Datasheet                                 Version: 1.3

                          DESCRIPTION OF CHANGES
The following changes were made to version 1.21:
   • In Table 1 on page 8, made the following changes/corrections:
       – Corrected pin type of pin A1 from Power to Ground
       – Corrected pin type of pin A2 from I/O to Input and added “Note: There is no internal
          pull-up/pull-down resistor”
       – Corrected pin type of pin A3 from Power to Ground
       – Corrected pin type of pin A4 from Power to Ground
       – Corrected pin type of pin A5 from I/O to Reference
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin A6
       – Corrected pin type of pin B2 from Power to Input and added “Note: There is no
          internal pull-up/pull-down resistor”
       – Corrected pin type of pin B3 from Input to Power
       – Corrected pin type of pin B4 from I/O to Power
       – Corrected pin type of pin B5 from Input to Power
       – Corrected pin type of pin B6 from I/O to Input and “Note: There is an internal pull-
          down resistor”
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin C3
       – Added “Note: There is no internal pull-up/pull-down resistor” to description of pin C4
       – Added “Note: There is an internal pull-up resistor” to description of pin C6
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin D2
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin E1
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin E2
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin E3
       – Corrected pin type of pin E4 from Power to Ground
       – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
          description of pin E5
       – Corrected pin type of pin E6 from Power to Ground

<!-- page 40 -->

Omni                   ision        TM




             DESCRIPTION OF CHANGES (CONTINUED)
 •   In Table 1 on page 8, made the following changes/corrections:
     – Corrected pin type of pin F2 from Analog to Power and changed description to
         “Sensor digital power (Core)”
     – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
         description of pins F3, F4, and F5
     – Corrected pin type of pin F6 from Analog to Power and changed description to be the
         same as pin F2
     – Corrected pin type of pin G2 from Power to Ground
     – Added “Default: Input” and “Note: There is no internal pull-up/pull-down resistor” to
         description of pins G3, G4, G5, and G6

<!-- page 41 -->

Omni                   ision       TM




                          REVISION CHANGE LIST
Document Title: OV2640 Datasheet                               Version: 1.4

                        DESCRIPTION OF CHANGES
The following changes were made to version 1.3:
   • In Table 6 on page 11, made the following changes:
       – Added “40 mA” for Maximum specification of IDDA-A
      –   Added “35 mA (YUV)” and “50 mA (Compressed)” for Maximum specification of
          IDDA-D
      –   Added “10 mA” for Maximum specification of IDDA-IO
      –   Added “2 mA” for Maximum specification of IDDS-SCCB
      –   Added “1200 µA” for Maximum specification of IDDS-PWDN

<!-- page 42 -->

Omni                     ision         TM




                             REVISION CHANGE LIST
Document Title: OV2640 Datasheet                                  Version: 1.5

                          DESCRIPTION OF CHANGES
The following changes were made to version 1.4:
   • Under Register Set section on page 18, changed the second paragraph from
       “There are two different sets for register address from 0x00 to 0x7E. Both register 0xF8
       and register 0xFF control which set is accessible. When 0xF8=00 and 0xFF=00, Table 12
       is effective. When 0xF8=01, 0xFF=7F, Table 13 is effective.”
       to
       “There are two different sets of register banks. Register 0xFF controls which set is
       accessible. When register 0xFF=00, Table 12 is effective. When register 0xFF=01, Table
       13 is effective.”

<!-- page 43 -->

Omni                        ision             TM




                                REVISION CHANGE LIST
Document Title: OV2640 Datasheet                                   Version: 1.6

                             DESCRIPTION OF CHANGES
The following changes were made to version 1.5:
   • In Table 12 on page 18, changed name, default, R/W, and description of register 0x44
       from “RSVD”, “XX”, “–”, and “Reserved” to “Qs”, “0C”, “RW”, and “Quantization Scale
       Factor”
   • In Table 12 on page 21, changed description of register RA_DLMT (0xFF) from:
         Sensor/Device Register Address Delimiter
         <(value of register 0xFF): Sensor address
          (value of register 0xFF): DSP address
       to:
             Register Bank Select
                Bit[7:1]: Reserved
                Bit[0]:   Register bank select
                          0: DSP address
                          1: Sensor address
   •   In Table 13 on page 22, changed default value for register REG08 (0x08) from
       “00” to “40”
   •   In Table 13 on page 22, changed description of register bits COM2[1:0] (0x09) from:
                          00: Weakest
                          01: Double capability
                          10: Double capability
                          11: Triple drive capability
       to:
                          00: 1x capability
                          01: 3x capability
                          10: 2x capability
                          11: 4x capability
   •   In Table 13 on page 22, changed default value for register PIDL (0x0B) from
       “40” to “41”
   •   In Table 13 on page 23, changed description of register bit CLKRC[6] (0x11) to
       “Reserved”
   •   In Table 13 on page 25, added “(if Bypass DSP is selected)” to description of register
       COM10 (0x15)