# Features

*Source: `Atmel-SAMD51.pdf`, pages 1-4 — SAMD51 family datasheet*

                                   SAM D5x/E5x Family Data
                                                     Sheet
    32-bit ARM® Cortex®-M4F MCUs with 1 Msps 12-bit ADC,
                QSPI, USB, Ethernet, and PTC

Features
Operating Conditions:
 • 1.71V to 3.63V, -40°C to +125°C, DC to 100 MHz
 • 1.71V to 3.63V, -40°C to +105°C, DC to 120 MHz
 • 1.71V to 3.63V, -40°C to +85°C, DC to 120 MHz
Core: 120 MHz Arm Cortex-M4
 • 403 CoreMark® at 120 MHz
 • 4 KB combined instruction cache and data cache
 • 8-Zone Memory Protection Unit (MPU)
 • Thumb®-2 instruction set
 • Embedded Trace Module (ETM) with instruction trace stream
 • Core Sight Embedded Trace Buffer (ETB)
 • Trace Port Interface Unit (TPIU)
 • Floating Point Unit (FPU)
Memories
 • 1 MB/512 KB/256 KB in-system self-programmable Flash with:
     – Error Correction Code (ECC)
     – Dual bank with Read-While-Write (RWW) support
     – EEPROM hardware emulation
 • 128 KB, 192 KB, 256 KB SRAM main memory
     – 64 KB, 96 KB, 128 KB of Error Correction Code (ECC) RAM option
 • Up to 4 KB of Tightly Coupled Memory (TCM)
 • Up to 8 KB additional SRAM
     – Can be retained in backup mode
 • Eight 32-bit backup registers
System
 • Power-on Reset (POR) and Brown-out detection (BOD)
 • Internal and external clock options
 • External Interrupt Controller (EIC)
 • 16 external interrupts
 • One non-maskable interrupt
 • Two-pin Serial Wire Debug (SWD) programming, test, and debugging interface
Power Supply



© 2019 Microchip Technology Inc.               Datasheet                        DS60001507E-page 1
                                                SAM D5x/E5x Family Data Sheet

  •   Idle, Standby, Hibernate, Backup, and Off sleep modes
  •   SleepWalking peripherals
  •   Battery backup support
  •   Embedded Buck/LDO regulator supporting on-the-fly selection
High-Performance Peripherals
 • 32-channel Direct Memory Access Controller (DMAC)
     – Built-in CRC with memory CRC generation/monitor hardware support
 • Up to two SD/MMC Host Controller (SDHC)
     – Up to 50 MHz operation
     – 4-bit or 1-bit interface
     – Compatibility with SD and SDHC memory card specification version 3.01
     – Compatibility with SDIO specification version 3.0
     – Compliant with JDEC specification, MMC memory cards V4.51
 • One Quad I/O Serial Peripheral Interface (QSPI)
     – eXecute-In-Place (XIP) support
     – Dedicated AHB memory zone
 • One Ethernet MAC (SAM E53 and SAM E54)
     – 10/100 Mbps in MII and RMII with dedicated DMA
             ®
     – IEEE 1588 Precision Time Protocol (PTP) support
     – IEEE 1588 Time Stamping Unit (TSU) support
     – IEEE802.3AZ energy efficiency support
     – Support for 802.1AS and 1588 precision clock synchronization protocol
     – Wake on LAN support
 • Up to two Controller Area Network (CAN) (that is., SAM E51 and SAM E54)
     – Support for CAN 2.0A/CAN 2.0B and CAN-FD (ISO 11898-1:2016)
 • One Full-Speed (12 Mbps) Universal Serial Bus (USB) 2.0 interface
     – Embedded host and device function
     – Eight endpoints
     – On-chip transceiver with integrated serial resistor
System Peripherals
 • 32-channel Event System
 • Up to eight Serial Communication Interfaces (SERCOM), each configurable to operate as either:
     – USART with full-duplex and single-wire half-duplex configuration
     – ISO7816
     – I2C up to 3.4 MHz
     – SPI
     – LIN master/slave
     – RS485
     – SPI inter-byte space
 • Up to eight 16-bit Timers/Counters (TC) each configurable as:
     – 16-bit TC with two compare/capture channels
     – 8-bit TC with two compare/capture channels




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 2
                                                  SAM D5x/E5x Family Data Sheet

       – 32-bit TC with two compare/capture channels, by pairing two TCs
  •   Two 24-bit Timer/Counters for Control (TCC), with extended functions:
       – Up to six compare channels with optional complementary output
       – Generation of synchronized pulse width modulation (PWM) pattern across port pins
       – Deterministic fault protection, fast decay and configurable dead-time between complementary
          output
       – Dithering that increase resolution with up to 5 bit and reduce quantization error
  •   Up to Three 16-bit Timer/Counters for Control (TCC) with extended functions:
       – Up to three compare channels with optional complementary output
  •   32-bit Real Time Counter (RTC) with clock/calendar function
  •   Up to 4 wake-up pins with tamper detection and debouncing filter
  •   Watchdog Timer (WDT) with Window mode
  •   CRC-32 generator
  •   One two-channel Inter-IC Sound Interface (I2S)
  •   Position Decoder (PDEC)
  •   Frequency meter (FREQM)
  •   Four Configurable Custom Logic (CCL)
  •   Dual 12-bit, 1 MSPS Analog-to-Digital Converter (ADC) with up to 16 channels each:
       – Differential and single-ended input
       – Automatic offset and gain error compensation
       – Oversampling and decimation in hardware to support 13-bit, 14-bit, 15-bit, or 16-bit resolution
  •   Dual 12-bit, 1 MSPS output Digital-to-Analog Converter (DAC)
  •   Two Analog Comparators (AC) with Window Compare function
  •   One temperature sensor
  •   Parallel Capture Controller (PCC)
       – Up to 14-bit parallel capture mode
  •   Peripheral Touch Controller (PTC)
       – Capacitive Touch buttons, sliders, and wheels
       – Wake-up on touch
       – Up to 32 self-capacitance and up to 256 mutual-capacitance channels
Cryptography
 • One Advanced Encryption System (AES) with 256-bit key length and up to 2 MB/s data rate
      – Five confidential modes of operation (ECB, CBC, CFB, OFB, CTR)
      – Supports counter with CBC-MAC mode
      – Galois Counter Mode (GCM)
 • True Random Number Generator (TRNG)
 • Public Key Cryptography Controller (PUKCC) and associated Classical Public Key Cryptography
    Library (PUKCL)
      – RSA, DSA
      – Elliptic Curves Cryptography (ECC) ECC GF(2n), ECC GF(p)
 • Integrity Check Module (ICM) based on Secure Hash Algorithm (SHA1, SHA224, SHA256), DMA
    assisted
Oscillators




© 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 3
                                                             SAM D5x/E5x Family Data Sheet

           • 32.768 kHz crystal oscillator (XOSC32K)
              – Clock failure detection
           • Up to two 8 MHz to 48 MHz crystal oscillator (XOSC)
              – Clock failure detection
           • 32.768 kHz ultra low-power internal oscillator (OSCULP32K)
           • 48 MHz Digital Frequency Locked Loop (DFLL48M)
           • Two 96-200 MHz Fractional Digital Phased Locked Loop (FDPLL200M)
         I/O
           • Up to 99 programmable I/O pins
         Qualification
           • AEC-Q100 Grade 1 (-40°C to 125°C)
         Packages
Table 1. Package Types

    Parameter                                                   Package Type
                                VQFN                           TQFP                  TFBGA             WLCSP
    Pin Count              48              64       64         100         128        120                 64
  I/O Pins (up to)         37              51       51          81          99         90                 51
  Contact/Lead            0.5              0.5      0.5         0.5         0.4        0.5               0.4
     Pitch
    Dimension          7x7x0.9        9x9x0.9    10x10x1.2   14x14x1.2   14x14x1.2   8x8x1.2       3.59x3.51x0.53

         Note: All dimensions are in millimeter (mm) unless specified.




        © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 4
