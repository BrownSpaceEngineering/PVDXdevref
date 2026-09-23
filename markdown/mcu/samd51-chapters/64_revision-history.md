# 62. Revision History

*Source: `Atmel-SAMD51.pdf`, pages 2118-2124 — SAMD51 family datasheet*

                                         SAM D5x/E5x Family Data Sheet
                                                                          Revision History


62.   Revision History
      Table 62-1. Revision E - 06/2019

       Section Name or Type                Change Description
       Introduction                        Updated sections:
                                            • Updated Features
                                            • Updated the Configuration Summary

       Processor and Architecture          Updated Interrupt Line Mapping
       CMCC                                Updated sections:
                                            • Data Cache Disable
                                            • Instruction Cache Disable

       GCLK                                Updated the PCHCTRLm register
       PM                                  Updated Backup Mode
       RTC                                 Count32 Registers updated:
                                            • CTRLA
                                            • EVCTRL
                                            • INTENCLR
                                            • INTENSET
                                            • INTFLAG
                                            • SYNCBUSY
                                            • GPn
                                           Count16 Registers updated:
                                            •   CTRLA
                                            •   EVCTRL
                                            •   INTENCLR
                                            •   INTENSET
                                            •   INTFLAG
                                            •   SYNCBUSY
                                            •   GPn
                                           The following Clock registers were updated:
                                            •   CTRLA
                                            •   EVCTRL
                                            •   INTENCLR
                                            •   INTENSET
                                            •   INTFLAG
                                            •   SYNCBUSY
                                            •   GPn




      © 2019 Microchip Technology Inc.   Datasheet                        DS60001507E-page 2118
                                   SAM D5x/E5x Family Data Sheet
                                                                       Revision History

...........continued
 Section Name or Type                Change Description
 DMAC                                The following topics were updated:
                                      • Initialization
                                      • Enabling, Disabling and Resetting
                                      • Transfer Descriptors
                                     The following registers were updated:
                                      • CTRL
                                      • SWTRIGCTRL
                                      • INTSTATUS
                                      • BUSYCH

 GMAC                                The following topics were updated:
                                      • Features
                                      • Pause Frame Reception

 OSCCTRL                             The following topics were updated:
                                      • Digital Phase Locked Loop (DPLL) Operation

 SERCOM-SPI                          Updated the following topics:
                                      • Clock Generation

 QSPI                                Updated the following topics:
                                      • Continuous Read Mode

 SDMMC                               Updated the following registers:
                                      • PSR
                                      • PCR
                                      • NISTR
                                      • NISTER
                                      • HC2R EMMC
                                      • HC2R SDIO
                                      • CA0R
                                      • CA1R
                                      • MCCAR
                                      • ASAR
                                      • PVRx
                                      • MC1R
                                      • ACR

 ADC                                 Updated the INPUTCTRL register
 AC                                  Updated the following sections:
                                      • Signal Description




© 2019 Microchip Technology Inc.   Datasheet                           DS60001507E-page 2119
                                       SAM D5x/E5x Family Data Sheet
                                                                           Revision History

...........continued
 Section Name or Type                    Change Description
 TC                                      Updated the following sections:
                                          • Counter Mode

 TCC                                     Updated the following sections:
                                          • Capture Operations
                                         Updated the following registers:
                                          • WAVE

 I2S                                     Updated the following sections:
                                          • DMA Operation
                                         Updated the following registers:
                                          • CTRLA
                                          • INTENCLR
                                          • INTENSET
                                          • INTFLAG
                                          • SYNCBUSY
                                          • TXCTRL
                                          • RXCTRL

 Electrical Characteristics at 85°C      Updated the following sections:
                                          • General Operating Ratings
                                          • Injection Current
                                          • Power Consumption
                                          • Analog-to-Digital Characteristics
                                          • Digital-to-Analog Converter Characteristics
                                         Added in new section:
                                          • PTC Characteristics

 Electrical Characteristics at 105°C     Updated the following sections:
                                          • Power Consumption
                                          • Digital-to-Analog Converter Characteristics
                                          • Analog-to-Digital Characteristics
                                         Added new section:
                                          • PTC Characteristics




© 2019 Microchip Technology Inc.       Datasheet                        DS60001507E-page 2120
                                       SAM D5x/E5x Family Data Sheet
                                                                         Revision History

...........continued
 Section Name or Type                    Change Description
 Electrical Characteristics at 125°C     Updated the following sections:
                                          • Power Consumption
                                          • Analog-To-Digital Characteristics
                                          • Digital-to-Analog Characteristics
                                         Added new section:
                                          • PTC Characteristics

Table 62-2. Rev. D - 12/2018

 Section Name or Type                    Change Description
 Ordering Information                    Added AEC-Q100 Qualified package type.
 I/O Multiplexing and Considerations     Added information for GRXDV pin for 64-pin
                                         package devices.
 AEC Q-100 Grade 1, 125°C Electrical     Introduced device part numbers with AEC Q-100
 Characteristics                         Grade 1.

Table 62-3. Rev. C - 11/2018

 Section Name or Type                    Change Description
 Ordering Information                    Added ordering information for 105°C and 125°C
                                         temperature grade.
 Pinout                                  Exposed pad info added for VQFN package.
 I/O Multiplexing and Considerations     Corrected typographical errors for pin numbers
                                         PB19 and PB23.
 Memories                                Clarified NVM User Page size in table 9-1.
 Processor and Architecture              Corrected typographical errors in section 10.2.2
                                         Interrupt Line Mapping for SERCOMx interrupt line
                                         7.
 MCLK                                    Corrected typographical errors related to R/W bits
                                         for 15.8.8 APBA Mask Register.
 PM                                      Updated Figure 18-2 Operating Conditions and
                                         SleepWalking to reflect that PL0 is not applicable
                                         to this product.
 SUPC                                    Updated INTENCLR, INTENSET, INTFLAG, and
                                         STATUS Registers to reflect factory
                                         preprogramming of BOD12.
 DMAC                                    Removed CHIP.ID information as it is not
                                         applicable to this product.




© 2019 Microchip Technology Inc.       Datasheet                        DS60001507E-page 2121
                                                SAM D5x/E5x Family Data Sheet
                                                                                  Revision History

...........continued
 Section Name or Type                             Change Description
 EVSYS                                            Corrected typographical errors in the USERm
                                                  Register offset.
 CCL                                               1.   Internal Events Inputs Selection (EVENT)
                                                        section was updated by removing
                                                        ASYNCEVENT related information.
                                                   2.   Alternate 2 TC input source not applicable
                                                        and was removed for LUTCTRL.INSELx bits.

 ADC                                              Added clarification for INTREF to 45.8.6 Reference
                                                  Control(REFCTRL).
 TC                                                1.   48.7.1 Register Summary - 8-bit Mode
                                                          – Updated register bitfield with indexing to
                                                             display usage.
                                                   2.   48.7.2 Register Summary - 16-bit Mode
                                                        2.1.     Updated register bitfield with
                                                                 indexing to display usage.
                                                        2.2.     Removed inapplicable register PER
                                                                 & PERBUF register information.
                                                   3.   48.7.3 Register Summary - 32-bit Mode
                                                        3.1.     Updated register bitfield with
                                                                 indexing to display usage.
                                                        3.2.     Removed inapplicable register PER
                                                                 & PERBUF register information.

 TCC - Timer/Counter for Control Applications      1.   Table 49-4. Output Matrix Channel Pin
                                                        Routing Configuration updated to show all
                                                        supported 6 capture channels.
                                                   2.   Table 49-8. Fault and Capture Action
                                                        updated by adding missing CAPTMARK
                                                        value for CAPTURE bit fields.
                                                   3.   Register INTENCLR, INTENSET, INTFLAG
                                                        updated with missing UFS bit.
                                                   4.   Removed unsupported bit info for the
                                                        register 49.8.15 Pattern (PATT).
                                                   5.   Missing POLx bits added to the register
                                                        49.8.16 Waveform (WAVE).
                                                   6.   49.7 Register Summary
                                                          – Updated register bitfield with indexing to
                                                             display usage.




© 2019 Microchip Technology Inc.                Datasheet                        DS60001507E-page 2122
                                          SAM D5x/E5x Family Data Sheet
                                                                           Revision History

...........continued
 Section Name or Type                       Change Description
 54. Electrical Characteristics at 85°C      1.   Clarified how CLEXT can be computed in
                                                  section 54.12.1 Crystal Oscillator (XOSC)
                                                  Characteristics and 54.12.2 External 32 kHz
                                                  Crystal Oscillator (XOSC32K) Characteristics
                                             2.   Clarified capacitor requirements in Table
                                                  54-18. External Components Requirements
                                                  in Switching Mode and Table 54-19
                                                  Decoupling Requirements.
                                             3.   Condition shown for VREF parameter is
                                                  removed in table 54-24. Operating
                                                  Conditions.
                                             4.   Conditions specified for table 54-29
                                                  Differential Mode is clarified for INL & DNL
                                                  with Internal voltage reference.
                                             5.   Table 54-35. Flash Timing Characteristics is
                                                  updated for Chip Erase maximum time.
                                             6.   Added the missing note in Table 54-44. Ultra-
                                                  Low-Power Internal 32kHz Oscillator
                                                  Electrical Characteristics.
                                             7.   Added the missing note in Table 54-48.
                                                  Fractional Digital Phase Lock Loop
                                                  Characteristics
                                             8.   Typo for the maximum value of tMOH in the
                                                  Table 54-51. SPI Timing Characteristics and
                                                  Requirements addressed.
                                             9.   Table 54-53. QSPI Maximum Frequency
                                                  examples updated.

 Electrical Characteristics at 105°C        Introduced device part numbers with Electrical
                                            Characteristics for 105°C temperature grade.
 Electrical Characteristics at 125°C        Introduced device part numbers with Electrical
                                            Characteristics for 125°C temperature grade.

Table 62-4. Rev. B - 4/2018

 Section Name or Type                       Change Description
 Features                                   Updated CAN FD reference.
                                            Added 120-ball TFBGA package.

 Configuration Summary                      Added 120-ball TFBGA to the family feature tables.

 Ordering Information                       Updated the notes for devices in WLCSP
                                            packages.
                                            Updated Package Type, adding CT = TFBGA.




© 2019 Microchip Technology Inc.          Datasheet                        DS60001507E-page 2123
                                                SAM D5x/E5x Family Data Sheet
                                                                                Revision History

...........continued
 Section Name or Type                             Change Description
 Pinout                                           Added the 120-ball TFBGA package pinout
                                                  diagram.

 Multiplexed Signals                              Added 120-ball TFBGA and updated Note 3 (see
                                                  Table 6-1.

 OSC32KCTRL - 32 kHz Oscillators Controller       Added the EN1K and EN32K bits to the
                                                  OSCULP32K register (see 29.8.9 OSCULP32K).

 SERCOM - Serial Communication Interface          Added Fractional Baud information to the Baud
                                                  Rate Equations (see Table 33-2).

 QSPI - Quad Serial Peripheral Interface          Added equations to the BAUD register (see 37.8.3
                                                  BAUD).

 CAN - Control Area Network                       Updated the Overview.
                                                  Updated ISO 11898 references throughout the
                                                  chapter.

 Public Key Cryptography Controller (PUKCC)       Added the Public Key Cryptography Library
                                                  (PUKCL) Application Programmer Interface (API)
                                                  section.

 TCC - Timer/Counter for Control Applications     Updated the number of TCC instances to 5 (4:0).
 54. Electrical Characteristics at 85°C           (1) Improved SPI maximum speed information in
                                                  Table 54-56.
                                                  (2). Added example for QSPI maximum frequency
                                                  examples Table 54-58.

 Packaging Information                            Added the 120-ball TFBGA package (see 58.3.8
                                                  120-ball TFBGA).

Table 62-5. Rev. A - 07/2017

 This is the initial release of the document.




© 2019 Microchip Technology Inc.                Datasheet                       DS60001507E-page 2124
