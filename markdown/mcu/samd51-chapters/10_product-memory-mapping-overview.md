# 8. Product Memory Mapping Overview

*Source: `Atmel-SAMD51.pdf`, pages 52-53 — SAMD51 family datasheet*

                                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 Product Memory Mapping Overview


        8.             Product Memory Mapping Overview
                       Figure 8-1. Product Mapping
Global Memory Space                                       Code                                         AHB-APB Bridge A
0x00000000                              0x00000000                                                   0x40000000
                                                                                                                     PAC
                Code                                   Internal Flash
                                                                                                     0x40000400
                                                                                                                     PM
0x20000000                              [Flash size]
                                                                                                     0x40000800
                                                        Reserved
                                                                                                                    MCLK
               SRAM                     0x03000000      Reserved
                                                                                                     0x40000C00
                                                         CMCC                                                       RSTC
0x20040000                              0x04000000
                                                                                                     0x40001000                       AHB-APB Bridge C
             Undefined                                     QSPI                                                    OSCCTRL          0x42000000
                                                                                                     0x40001400                                   CAN0
0x40000000                              0x05000000                                                                OSC32KCTRL        0x42000400
                                                                                                     0x40001800                                   CAN1
             Peripherals                                 Reserved                                                   SUPC            0x42000800
                                       0x1FFFFFFF                                                    0x40001C00                                   GMAC
0x48000000
                                                                                                                    GCLK            0x42000C00
                                                         SRAM                                                                                     TCC2
              Reserved                                                                               0x40002000
                                        0x20000000                                                                   WDT            0x42001000
0xE0000000                                             System RAM                                    0x40002400                                   TCC3
                                                                                                                     RTC            0x42001400
               System                   0x2003FFFF                                                   0x40002800                                    TC4
                                                                                                                     EIC            0x42001800
0xFFFFFFFF
                                                                                                     0x40002C00                                    TC5
                                                                                                                    FREQM           0x42001C00
                                                                                                     0x40003000                                   PDEC
                                                                                                                   SERCOM0          0x42002000
                       System                                                                        0x40003400                                    AC
                                                                                     AHB-APB                       SERCOM1
        0xE0000000                                                                                                                  0x42002400
                       Reserved                                         0x40000000                   0x40003800                                    AES
       0xE000E000                                                                     Bridge A                       TC0            0x42002800
                           SCS
                                            AHB-APB Bridge B                                                                                      TRNG
                                                                                                     0x40003C00
                                         0x41000000                                                                  TC1
        0xE000F000                                                      0x41000000                                                  0x42002C00
                                                             USB                                                                                   ICM
                       Reserved                                                                      0x40004000
                                         0x41002000                                   Bridge B                     Reserved
       0xE00FF000                                                                                                                   0x42003000
                                                            DSU                                      0x40FFFFFF                                  PUKCC
                     ROMTable
                                         0x41004000                     0x42000000
        0xE0100000                                                                                                                  0x42003400
                                                         NVMCTRL                                                                                  QSPI
                       Reserved
       0xFFFFFFFF                        0x41006000                                   Bridge C
                                                                                                                                    0x42003800
                                                           CMCC                                                                                    CCL
                                         0x41008000                     0x43000000
                                                            PORT                                       AHB-APB Bridge D             0x42003C00
                                                                                      Bridge D       0x43000000                                  Reserved
                                         0x4100A000                                                                                0x42FFFFFF
                                                                                                                   SERCOM4
                                                           DMAC
                                                                        0x44000000                   0x43000400
                                         0x4100C000
                                                                                                                   SERCOM5
                                                          Reserved                    SEEPROM
                                                                                                     0x43000800
                                         0x4100E000
                                                                                                                   SERCOM6
                                                           EVSYS        0x45000000
                                                                                                     0x43000C00
                                         0x41010000
                                                                                       SDHC0                       SERCOM7
                                                          Reserved
                                                                                                     0x43001000
                                         0x41012000
                                                                                                                     TCC4
                                                         SERCOM2        0x46000000
                                                                                                     0x43001400
                                         0x41014000
                                                                                       SDHC1                         TC6
                                                         SERCOM3
                                                                                                     0x43001800
                                         0x41016000                     0x47000000                                   TC7
                                                            TCC0
                                                                                                     0x43001C00
                                         0x41018000                                  Backup RAM
                                                                                                                    ADC0
                                                            TCC1
                                                                        0x47FFFFFF                   0x43002000
                                         0x4101A000
                                                                                                                    ADC1
                                                             TC2
                                                                                                     0x43002400
                                         0x4101C000
                                                                                                                     DAC
                                                             TC3
                                                                                                     0x43002800
                                         0x4101E000
                                                                                                                     I2S
                                                          Reserved
                                                                                                     0x43002C00
                                         0x41020000
                                                                                                                     PCC
                                                          RAMECC
                                                                                                     0x43003000
                                         0x41022000
                                                                                                                   Reserved
                                                          Reserved                                   0x43FFFFFF
                                         0x41FFFFFF




                     © 2019 Microchip Technology Inc.                                Datasheet                                 DS60001507E-page 52
                                   SAM D5x/E5x Family Data Sheet
                                          Product Memory Mapping Overview

Related Links
9. Memories




© 2019 Microchip Technology Inc.   Datasheet               DS60001507E-page 53
