# 5. Signal Descriptions List

*Source: `Atmel-SAMD51.pdf`, pages 28-31 — SAMD51 family datasheet*

                                                               SAM D5x/E5x Family Data Sheet
                                                                                   Signal Descriptions List


5.   Signal Descriptions List
     The following table gives details on signal names classified by peripheral.
     Table 5-1. Signal Descriptions List

      Signal Name                 Function                            Type              Active Level
      Device Service Unit - DSU
      SWCLK                       SW Clock                            Digital
      SWDIO                       SW Bidirectional Data               Digital
      RESETN                      Reset input                         Digital           Low
      Trace Port Interface Unit - TPIU
      TRACEDATA[3:0]              Trace Data Output                   Digital
      TRACECLK                    Trace Clock                         Digital
      SWO                         Serial Wire Output                  Digital
      Analog Comparators - AC
      CMP[1:0]                    AC Comparator Outputs               Digital
      AIN[3:0]                    AC Analog Inputs                    Analog
      Analog Digital Converter - ADC
      AIN[15:0]                   ADC Analog Inputs                   Analog
      VREFA                       ADC Voltage External Reference      Analog
                                  A
      VREFB                       ADC Voltage External Reference      Analog
                                  B
      VREFC                       ADC Voltage External Reference      Analog
                                  C
      Peripheral Touch Controller - PTC
      XY[31:0]                    PTC X/Y Input/Output                Analog
      Digital Analog Converter - DAC
      VOUT[1:0]                   DAC Voltage output                  Analog
      VREFA                       DAC Voltage External Reference      Analog
      External Interrupt Controller - EIC
      EXTINT[15:0]                External Interrupts inputs          Digital
      NMI                         External Non-Maskable Interrupt     Digital
                                  input
      Generic Clock Generator - GCLK




     © 2019 Microchip Technology Inc.                          Datasheet                   DS60001507E-page 28
                                                       SAM D5x/E5x Family Data Sheet
                                                                                   Signal Descriptions List

...........continued
 Signal Name                 Function                             Type                  Active Level
 GCLK_IO[7:0]                Generic Clock (source clock          Digital
                             inputs or generic clock generator
                             output)
 Custom Control Logic - CCL
 IN[11:0]                    Logic Inputs                         Digital
 OUT[3:0]                    Logic Outputs                        Digital
 Supply Controller - SUPC
 VBAT                        External battery supply Inputs       Analog
 OUT[1:0]                    Logic Outputs                        Digital
 Power Manager - PM
 RESETN                      Reset input                          Digital               Low
 Oscillators Control - OSCCTRL
 XOSCx - XIN                 Crystal or external clock Input      Analog/Digital
 XOSCx - XOUT                Crystal Output                       Analog
 32KHz Oscillators Control - OSC32KCTRL
 XIN32                       32KHz Crystal or external clock      Analog/Digital
                             Input
 XOUT32                      32KHz Crystal Output                 Analog
 General Purpose I/O - PORT
 PA31 - PA30, PA27,          Parallel I/O Controller I/O Port A   Digital
 PA25 - PA00
 PB31 - PB00                 Parallel I/O Controller I/O Port B   Digital
 PC31 - PC30, PC28 - Parallel I/O Controller I/O Port C           Digital
 PC10, PC07 - PC00
 PD21-PD20, PD12 -           Parallel I/O Controller I/O Port D   Digital
 PD08, PD01 - PD00
 Real-Time Counter - RTC
 IN[4:0]                     Tamper / Wake / Active Layer         Digital
                             Protection Input
 OUT                         Active Layer Protection Output       Digital
 Timer Counter - TCx
 WO[1:0]                     Waveform Outputs/Capture             Digital
                             Inputs
 Timer Counter - TCCx




© 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 29
                                                     SAM D5x/E5x Family Data Sheet
                                                                       Signal Descriptions List

...........continued
 Signal Name                 Function                        Type           Active Level
 WO[7:0]                     Waveform Outputs/Capture        Digital
                             Inputs
 Position Decoder - PDEC
 QDI[2:0]                    PDEC Inputs                     Digital
 Parallel Capture Controller - PCC
 DEN1                        Sensor Sync1                    Digital
 DEN2                        Sensor Sync2                    Digital
 CLK                         Sensor Clock                    Digital
 DATA[13:0]                  Sensor Data                     Digital
 Serial Communication Interface - SERCOMx
 PAD[3:0]                    SERCOM Inputs/Outputs Pads      Digital
 Quad Serial Peripheral Interface - QSPI
 SCK                         Serial Clock                    Digital
 CS                          Chip Select                     Digital
 DATA[3:0]                   Data Input/Output               Digital
 Ethernet MAC - GMAC
 GTXEN                       Transmit Enable                 Digital
 GTXCK                       Transmit Clock or Reference     Digital
                             Clock
 GTX[3:0]                    Transmit Data                   Digital
 GTXER                       Transmit Coding Error           Digital
 GRXER                       Receive Error                   Digital
 GRXCK                       Receive Clock                   Digital
 GRX[3:0]                    Receive Data                    Digital
 GRXDV                       Receive Data Valid              Digital
 GCOL                        Collision Detect                Digital
 GCRS                        Carrier Sense and Data Valid    Digital
 GMDIO                       Management Data Input/Output    Digital
 GMDC                        Management Data Clock           Digital
 Universal Serial Bus - USB
 DP                          DP for USB                      Digital
 DM                          DM for USB                      Digital




© 2019 Microchip Technology Inc.                      Datasheet                DS60001507E-page 30
                                                      SAM D5x/E5x Family Data Sheet
                                                                         Signal Descriptions List

...........continued
 Signal Name                 Function                          Type           Active Level
 SOF 1kHz                    USB Start of Frame                Digital
 Control Area Network - CANx
 TX                          CAN Transmit                      Digital
 RX                          CAN Receive                       Digital
 Inter-IC Sound Controller - I2S
 MCK1, MCK0                  Master Clock                      Digital
 SCK1, SCK0                  Serial Clock                      Digital
 FS1, FS0                    I²S Word Select or TDM Frame      Digital
                             Sync
 SDO                         Serial Data Output for Transmit   Digital
                             Serializer
 SDI                         Serial Data Input for Receive     Digital
                             Serializer
 SD/MMC Host Controller - SDHCx
 CD                          SD Card / SDIO / e.MMC Card       Digital
                             Detect
 CMD                         SD Card / SDIO / e.MMC            Digital
                             Command/Response Line
 WP                          SD Card Connector Write Protect Digital
                             Signal
 CK                          SD Card / SDIO / e.MMC Clock      Digital
                             Signal
 DAT[3:0]                    SD Card / SDIO / e.MMC Data       Digital
                             Lines




© 2019 Microchip Technology Inc.                       Datasheet                 DS60001507E-page 31
