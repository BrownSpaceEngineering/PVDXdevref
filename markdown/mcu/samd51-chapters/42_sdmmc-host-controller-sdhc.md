# 40. SD/MMC Host Controller (SDHC)

*Source: `Atmel-SAMD51.pdf`, pages 1311-1392 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                                 SD/MMC Host Controller ...


40.      SD/MMC Host Controller (SDHC)

40.1     Overview
         The SD/MMC Host Controller (SDHC) supports the embedded MultiMedia Card (e.MMC) Specification,
         the SD Memory Card Specification, and the SDIO Specification. It is compliant with the SD Host
         Controller Standard specifications. Refer to 40.1.1 Reference Documents for details.
         The SDHC includes the register set defined in the “SD Host Controller Simplified Specification V3.00” and
         additional registers to manage e.MMC devices and enhanced features.
         The SDHC is clocked by up to three clocks (bus clock, SDHC core clock, and a slow clock for certain
         functions). Both the MCLK and GCLK must be configured before the SDHC can be used.
         The SAM D5x/E5x provides two instances of the SDHC, SDHC0 and SDHC1.
         Related Links
         40.3.1 Block Diagram

40.1.1   Reference Documents

          Name                                                  Link
          SD Host Controller Simplified Specification V3.00     https://www.sdcard.org
          SDIO Simplified Specification V3.00
          Physical Layer Simplified Specification V3.01
          Embedded MultiMedia Card (e.MMC) Electrical           http://www.jedec.org
          Standard 4.51



40.2     Features
           • Compatibility:
              – SD Host Controller Standard Specification
              – MultiMedia Card Specification
              – SD Memory Card Specification
              – SDIO Specification Version
               Refer to 40.1.1 Reference Documents for details.
           •   Support for 1-bit/ 4-bit SD/SDIO Devices
           •   Support for 1-bit/4-bit e.MMC Devices
           •   Support for SD/SDIO Default Speed (Maximum SDCLK Frequency = 25 MHz)
           •   Support for SD/SDIO High Speed (Maximum SDCLK Frequency = 50 MHz)
           •   Support for e.MMC Default Speed (Maximum SDCLK Frequency = 26 MHz)
           •   e.MMC Boot Operation Mode Support
           •   Support for Block Size from 1 to 512 bytes
           •   Support for Stream, Block and Multi-block Data Read and Write – Advanced DMA and SDMA
               Capability




         © 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1311
                                                       SAM D5x/E5x Family Data Sheet
                                                                                SD/MMC Host Controller ...

           • Internal 1024-byte Dual Port RAM
           • Support for both synchronous and asynchronous abort
           • Supports for SDIO Card Interrupt



40.3     Block Diagrams

40.3.1   Block Diagram




                                            SDHC




                                                                   SDCD

                                                                   SDCMD

                                                                   SDWP

                                                                   SDCK

                                                                   SDDAT[3:0]




            CLK_AHB_SDHCx
                GCLK_SDHCx
         GCLK_SDHCx_SLOW




         © 2019 Microchip Technology Inc.               Datasheet                        DS60001507E-page 1312
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                  SD/MMC Host Controller ...

40.3.2   Application Block Diagram

                            Application Layer
                  ex: File System, Audio, Security, etc.




                       Physical Layer
                   SD/MMC Host Controller
                          (SDHC)




            MMC/e.MMC          SDCard               SDIO




40.4     Signal Description
          Signal Name                                      Type                  Description
          SDCD                                             Input                 SD Card / SDIO /e.MMC Card
                                                                                 Detect
          SDCMD                                            I/O                   SD Card / SDIO /e.MMC
                                                                                 Command/Response Line
          SDWP                                             Input                 SD Card Connector Write Protect
                                                                                 Signal
          SDCK                                             Output                SD Card / SDIO /e.MMC Clock
                                                                                 Signal
          SDDAT[3:0]                                       I/O                   SD Card / SDIO /e.MMC data
                                                                                 lines



40.5     Product Dependencies

40.5.1   I/O Lines
         In order to use the I/O lines, the I/O pins must be configured using the IO Pin Controller (PORT).

40.5.2   Power Management
         This peripheral can continue to operate in any sleep mode where its source clock is running. Refer to PM
         – Power Manager for details on the different sleep modes.

40.5.3   Clocks
         The peripheral is using two generic clocks and one bus clock.
         The clock for the SDHC bus interface (CLK_AHB_SDHC) is enabled and disabled by the Main Clock
         Controller. The default state of CLK_AHB_SDHC can be found in the Peripheral Clock Masking section.




         © 2019 Microchip Technology Inc.                           Datasheet                  DS60001507E-page 1313
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

         The two generic clocks are:
          • The core clock GCLK_SDHCx is required to clock the SDHC core.
          • The slow clock GCLK_SDHCx_SLOW is only required for certain functions. When this clock is
             required, GCLK_SDHCx must be enabled.
         These clocks must be configured and enabled in the Generic Clock Controller (GCLK) before using the
         SDHC. The generic clocks are asynchronous to the user interface clock (CLK_SDHCx_AHB). Due to this
         asynchronicity, writing to certain registers will require synchronization between the clock domains.
         Related Links
         15. MCLK – Main Clock

40.5.4   DMA
         Not applicable.

40.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first.

40.5.6   Events
         Not applicable.



40.6     Functional Description

40.6.1   SD/SDIO Operating Mode
         This peripheral is fully compliant with the "SD Host Controller Simplified Specification V3.00" for SD/SDIO
         devices. Refer to this specification for configuration.
         Refer to "Physical Layer Simplified Specification V3.01" and "SDIO Simplified Specification V3.00" for SD/
         SDIO management.
         Related Links
         40.1.1 Reference Documents

40.6.2   e.MMC Operating Mode
         This peripheral supports e.MMC devices management. As the “SD Host Controller Simplified
         Specification V3.00” does not apply to e.MMC devices, some registers have been added to those
         described in this specification in order to manage e.MMC devices. Most of the registers described in the
         “SD Host Controller Simplified Specification V3.00” must be used for e.MMC management, but e.MMC-
         specific features are managed using MC1R and MC2R.
         Related Links
         40.1.1 Reference Documents




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1314
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                                    SD/MMC Host Controller ...


40.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0                                                   ARG2[7:0]
                             15:8                                                  ARG2[15:8]
 0x00          SSAR
                             23:16                                                 ARG2[23:16]
                             31:24                                                 ARG2[31:24]
                              7:0                                                 BLKSIZE[7:0]
 0x04          BSR
                             15:8                              BOUNDARY[2:0]                                               BLKSIZE[9:8]
                              7:0                                                  BLKCNT[7:0]
 0x06          BCR
                             15:8                                                 BLKCNT[15:8]
                              7:0                                                   ARG1[7:0]
                             15:8                                                  ARG1[15:8]
 0x08         ARG1R
                             23:16                                                 ARG1[23:16]
                             31:24                                                 ARG1[31:24]
                              7:0                                 MSBSEL       DTDSEL            ACMDEN[1:0]            BCEN       DMAEN
 0x0C          TMR
                             15:8
                              7:0            CMDTYP[1:0]           DPSEL       CMDICEN   CMDCCEN                           RESPTYP[1:0]
 0x0E           CR
                             15:8                                                                 CMDIDX[5:0]
                              7:0                                                 CMDRESP[7:0]
                             15:8                                                CMDRESP[15:8]
 0x10           RR0
                             23:16                                               CMDRESP[23:16]
                             31:24                                               CMDRESP[31:24]
                              7:0                                                 CMDRESP[7:0]
                             15:8                                                CMDRESP[15:8]
 0x14           RR1
                             23:16                                               CMDRESP[23:16]
                             31:24                                               CMDRESP[31:24]
                              7:0                                                 CMDRESP[7:0]
                             15:8                                                CMDRESP[15:8]
 0x18           RR2
                             23:16                                               CMDRESP[23:16]
                             31:24                                               CMDRESP[31:24]
                              7:0                                                 CMDRESP[7:0]
                             15:8                                                CMDRESP[15:8]
 0x1C           RR3
                             23:16                                               CMDRESP[23:16]
                             31:24                                               CMDRESP[31:24]
                              7:0                                                 BUFDATA[7:0]
                             15:8                                                 BUFDATA[15:8]
 0x20          BDPR
                             23:16                                               BUFDATA[23:16]
                             31:24                                               BUFDATA[31:24]
                              7:0                                                          RTREQ          DLACT        CMDINHD    CMDINHC
                             15:8                                                         BUFRDEN       BUFWREN         RTACT       WTACT
 0x24          PSR
                             23:16                         DATLL[3:0]                      WRPPL         CARDDPL       CARDSS      CARDINS
                             31:24                                                                                                  CMDLL
 0x28          HC1R           7:0     CARDDSEL      CARDDTL                       DMASEL[1:0]              HSEN          DW        LEDCTRL
 0x29          PCR            7:0                                                                      SDBVSEL[2:0]                SDBPWR
 0x2A          BGCR           7:0                                                          INTBG         RWCTRL         CONTR      STPBGR




          © 2019 Microchip Technology Inc.                                 Datasheet                                  DS60001507E-page 1315
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                      SD/MMC Host Controller ...

...........continued

  Offset               Name     Bit Pos.

   0x2B                 WCR       7:0                                                                    WKENCREM WKENCINS             WKENCINT
                                  7:0        USDCLKFSEL[1:0]      CLKGSEL                                 SDCLKEN         INTCLKS      INTCLKEN
   0x2C                 CCR
                                 15:8                                           SDCLKFSEL[7:0]
   0x2E                 TCR       7:0                                                                             DTCVAL[3:0]
   0x2F                 SRR       7:0                                                                    SWRSTDAT SWRSTCMD             SWRSTALL
                                  7:0       CREM          CINS    BRDRDY      BWRRDY         DMAINT         BLKGE          TRFC          CMDC
   0x30                NISTR
                                 15:8      ERRINT       BOOTAR                                                                            CINT
                                  7:0      CURLIM       DATEND    DATCRC      DATTEO        CMDIDX         CMDEND         CMDCRC        CMDTEO
   0x32                EISTR
                                 15:8                                         BOOTAE                                       ADMA          ACMD
                                  7:0       CREM          CINS    BRDRDY      BWRRDY         DMAINT         BLKGE          TRFC          CMDC
   0x34                NISTER
                                 15:8                   BOOTAR                                                                            CINT
                                  7:0      CURLIM       DATEND    DATCRC      DATTEO        CMDIDX         CMDEND         CMDCRC        CMDTEO
   0x36                EISTER
                                 15:8                                         BOOTAE                                       ADMA          ACMD
                                  7:0       CREM          CINS    BRDRDY      BWRRDY         DMAINT         BLKGE          TRFC          CMDC
   0x38                NISIER
                                 15:8                   BOOTAR                                                                            CINT
                                  7:0      CURLIM       DATEND    DATCRC      DATTEO        CMDIDX         CMDEND         CMDCRC        CMDTEO
   0x3A                EISIER
                                 15:8                                         BOOTAE                                       ADMA          ACMD
                                  7:0       CMDNI                             ACMDIDX      ACMDEND        ACMDCRC        ACMDTEO       ACMD12NE
   0x3C                ACESR
                                 15:8
                                  7:0      SCLKSEL       EXTUN        DRVSEL[1:0]                                 HS200EN[3:0]
   0x3E         HC2R - EMMC
                                 15:8      PVALEN
                                  7:0      SCLKSEL       EXTUN        DRVSEL[1:0]            VS18EN                      UHSMS[2:0]
   0x3E        HC2R - DEFAULT
                                 15:8      PVALEN       ASINTEN
                                  7:0      TEOCLKU                                                 TEOCLKF[5:0]
                                 15:8                                               BASECLKF[7:0]
   0x40                CA0R
                                 23:16     SRSUP        SDMASUP    HSSUP                   ADMA2SUP        ED8SUP                      MAXBLKL
                                 31:24           SLTYPE[1:0]      ASINTSUP    SB64SUP                     V18VSUP        V30VSUP       V33VSUP
                                  7:0                   DRVDSUP   DRVCSUP     DRVASUP                     DDR50SUP      SDR104SUP      SDR50SUP
                                 15:8                             TSDR50                                          TCNTRT[3:0]
   0x44                CA1R
                                 23:16                                              CLKMULT[7:0]
                                 31:24
                                  7:0                                           MAXCUR33V[7:0]
                                 15:8                                           MAXCUR30V[7:0]
   0x48                MCCAR
                                 23:16                                          MAXCUR18V[7:0]
                                 31:24
   0x4C
     ...           Reserved
   0x4F
                                  7:0       CMDNI                             ACMDIDX      ACMDEND        ACMDCRC        ACMDTEO       ACMD12NE
   0x50            FERACES
                                 15:8
                                  7:0      CURLIM       DATEND    DATCRC      DATTEO        CMDIDX         CMDEND         CMDCRC        CMDTEO
   0x52                FEREIS
                                 15:8                                         BOOTAE                                       ADMA          ACMD
   0x54                AESR       7:0                                                                       LMIS                 ERRST[1:0]




              © 2019 Microchip Technology Inc.                             Datasheet                                    DS60001507E-page 1316
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

...........continued

  Offset               Name    Bit Pos.

   0x55
     ...           Reserved
   0x57
                                  7:0                                  ADMASA[7:0]
                                 15:8                                  ADMASA[15:8]
   0x58                ASAR
                                 23:16                                ADMASA[23:16]
                                 31:24                                ADMASA[31:24]
   0x5C
     ...           Reserved
   0x5F
                                  7:0                                 SDCLKFSEL[7:0]
   0x60                PVR0
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x62                PVR1
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x64                PVR2
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x66                PVR3
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x68                PVR4
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x6A                PVR5
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x6C                PVR6
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
                                  7:0                                 SDCLKFSEL[7:0]
   0x6E                PVR7
                                 15:8                                                    CLKGSEL       SDCLKFSEL[9:8]
   0x70
     ...           Reserved
   0xFB
                                  7:0                                   INTSSL[7:0]
   0xFC                SISR
                                 15:8
                                  7:0                                   SVER[7:0]
   0xFE                HCVR
                                 15:8                                   VVER[7:0]
  0x0100
     ...           Reserved
  0x01FF
                                  7:0                                                        HDATLL[3:0]
                                 15:8
  0x0200               APSR
                                 23:16
                                 31:24
  0x0204               MC1R       7:0       FCD   RSTN   BOOTA       OPD         DDR                       CMDTYP[1:0]
  0x0205               MC2R       7:0                                                                ABOOT         SRESP
  0x0206
     ...           Reserved
  0x0207




              © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1317
                                                 SAM D5x/E5x Family Data Sheet
                                                                    SD/MMC Host Controller ...

...........continued

  Offset               Name    Bit Pos.

                                  7:0                                              BMAX[1:0]
                                 15:8
  0x0208               ACR
                                 23:16
                                 31:24
                                  7:0                                                    FSDCLKD
                                 15:8
  0x020C               CC2R
                                 23:16
                                 31:24
  0x0210
     ...           Reserved
  0x022F
                                  7:0                                                   CAPWREN
                                 15:8                    KEY[7:0]
  0x0230               CACR
                                 23:16
                                 31:24
                                  7:0                                                     NIDBG
  0x0234               DBGR
                                 15:8




40.8           Register Description




              © 2019 Microchip Technology Inc.   Datasheet                   DS60001507E-page 1318
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.1         SDMA System Address / Argument 2 Register

               Name:       SSAR
               Offset:     0x00
               Reset:      0x00000000
               Property:   -

               This register contains the physical system memory address used for SDMA transfers or the second
               argument for Auto CMD23.

         Bit        31           30            29           28                 27      26           25           24
                                                                 ARG2[31:24]
   Access          R/W           R/W          R/W          R/W                R/W     R/W          R/W           R/W
    Reset            0            0            0             0                 0       0             0            0


         Bit        23           22            21           20                 19      18           17           16
                                                                 ARG2[23:16]
   Access          R/W           R/W          R/W          R/W                R/W     R/W          R/W           R/W
    Reset            0            0            0             0                 0       0             0            0


         Bit        15           14            13           12                 11      10            9            8
                                                                 ARG2[15:8]
   Access          R/W           R/W          R/W          R/W                R/W     R/W          R/W           R/W
    Reset            0            0            0             0                 0       0             0            0


         Bit         7            6            5             4                 3       2             1            0
                                                                  ARG2[7:0]
   Access          R/W           R/W          R/W          R/W                R/W     R/W          R/W           R/W
    Reset            0            0            0             0                 0       0             0            0


               Bits 31:0 – ARG2[31:0] SDMA System Address/Argument 2
               The function of this bit field is depending on the operation mode:
               For a SDMA transfer, this field is the system memory address. When the peripheral stops an SDMA
               transfer, this field points to the system address of the next contiguous data position. This field can be
               accessed only if no transaction is executing (i.e., after a transaction has stopped). Read operations
               during transfers may return an invalid value. An interrupt can be generated to instruct the software to
               update this field. Writing the next system address of the next data position restarts the SDMA transfer.
               When executing Auto CMD23, this field is used with Auto CMD23 to set a 32-bit block count value to the
               CMD23 argument. If Auto CMD23 is used with ADMA, the full 32-bit block count value can be used. If
               Auto CMD23 is used without ADMA, the available block count value is limited by BCR. In this case,
               65535 blocks is the maximum value.




           © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1319
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                         SD/MMC Host Controller ...

40.8.2         Block Size Register

               Name:        BSR
               Offset:      0x04
               Reset:       0x0000
               Property:    -


         Bit        15            14            13           12                  11      10            9                  8
                                          BOUNDARY[2:0]                                                    BLKSIZE[9:8]
   Access                                                                                             R/W             R/W
    Reset                          0            0             0                                        0                  0


         Bit         7             6            5             4                  3       2             1                  0
                                                                  BLKSIZE[7:0]
   Access           R/W          R/W           R/W           R/W             R/W        R/W           R/W             R/W
    Reset            0             0            0             0                  0       0             0                  0


               Bits 14:12 – BOUNDARY[2:0] SDMA Buffer Boundary
               This field specifies the size of the contiguous buffer in the system memory. The SDMA transfer waits at
               every boundary specified by this field and the peripheral generates the DMA Interrupt to instruct the
               software to update SSAR. If this field is set to 0 (buffer size = 4 Kbytes), the lowest 12 bits of
               SSAR.ADDRESS point to data in the contiguous buffer, and the upper 20 bits point to the location of the
               buffer in the system memory. This function is active when the DMA Enable bit in the Transfer Mode
               Register (TMR.DMAEN) is '1'.
                Value       Name                      Description
                0           4K                        4-Kbyte boundary
                1           8K                        8-Kbyte boundary
                2           16K                       16-Kbyte boundary
                3           32K                       32-Kbyte boundary
                4           64K                       64-Kbyte boundary
                5           128K                      128-Kbyte boundary
                6           256k                      256-Kbyte boundary
                7           512K                      512-Kbyte boundary

               Bits 9:0 – BLKSIZE[9:0] Transfer Block Size
               This field specifies the block size of data transfers for CMD17, CMD18, CMD24, CMD25 and CMD53.
               Values ranging from 1 to 512 can be set. It can be accessed only if no transaction is executing (i.e., after
               a transaction has stopped). Read operations during transfers may return an invalid value, and write
               operations are ignored.




           © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 1320
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                      SD/MMC Host Controller ...

40.8.3         Block Count Register

               Name:       BCR
               Offset:     0x06
               Reset:      0x0000
               Property:   -


         Bit        15           14            13           12                 11     10            9            8
                                                                BLKCNT[15:8]
   Access          R/W           R/W          R/W          R/W             R/W       R/W           R/W          R/W
    Reset            0            0            0            0                  0       0            0            0


         Bit         7            6            5            4                  3       2            1            0
                                                                 BLKCNT[7:0]
   Access          R/W           R/W          R/W          R/W             R/W       R/W           R/W          R/W
    Reset            0            0            0            0                  0       0            0            0


               Bits 15:0 – BLKCNT[15:0] Block Count for Current Transfer
               This field is used only if TMR.BCEN (Block Count Enable) is set to 1 and is valid only for multiple block
               transfers. BLKCNT is the number of blocks to be transferred and it must be set to a value between 1 and
               the maximum block count. The peripheral decrements the block count after each block transfer and stops
               when the count reaches 0. When this field is set to 0, no data block is transferred.
               This register should be accessed only when no transaction is executing (i.e., after transactions are
               stopped). During data transfer, read operations on this register may return an invalid value and write
               operations are ignored.
               When a suspend command is completed, the number of blocks yet to be transferred can be determined
               by reading this register. Before issuing a resume command, the previously saved block count is restored.




           © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1321
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.4         Argument 1 Register

               Name:       ARG1R
               Offset:     0x08
               Reset:      0x00000000
               Property:   Read/Write


         Bit        31           30           29           28                 27    26           25           24
                                                                ARG1[31:24]
   Access          R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
    Reset           0             0            0           0                  0      0            0            0


         Bit        23           22           21           20                 19    18           17           16
                                                                ARG1[23:16]
   Access          R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
    Reset           0             0            0           0                  0      0            0            0


         Bit        15           14           13           12                 11    10            9            8
                                                                ARG1[15:8]
   Access          R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
    Reset           0             0            0           0                  0      0            0            0


         Bit        7             6            5           4                  3      2            1            0
                                                                 ARG1[7:0]
   Access          R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
    Reset           0             0            0           0                  0      0            0            0


               Bits 31:0 – ARG1[31:0] Argument 1
               This register contains the SD command argument which is specified as the bit 39-8 of Command-Format
               in the “Physical Layer Simplified Specification V3.01” or “Embedded MultiMedia Card (e.MMC) Electrical
               Standard 4.51”.




           © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1322
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                 SD/MMC Host Controller ...

40.8.5         Transfer Mode Register

               Name:        TMR
               Offset:      0x0C
               Reset:       0x0000
               Property:    -

               This register is used to control data transfers. The user shall set this register before issuing a command
               which transfers data (refer to bit DPSEL in CR), or before issuing a Resume command. The user must
               save the value of this register when the data transfer is suspended (as a result of a Suspend command)
               and restore it before issuing a Resume command. To prevent data loss, this register cannot be written
               while data transactions are in progress. Writes to this register are ignored when bit PSR.CMDINHD is '1'.
               Table 40-1. Determining the Transfer Type

               MSBSEL               BCEN                 BCR.BLKCNT                      Function
               0                    Don’t care           Don’t care                      Single Transfer
               1                    0                    Don’t care                      Infinite Transfer
               1                    1                    Not Zero                        Multiple Transfer
               1                    1                    Zero                            Stop Multiple Transfer

         Bit         15            14             13            12             11             10              9            8


   Access
    Reset


         Bit         7              6             5              4             3                 2            1            0
                                               MSBSEL        DTDSEL                ACMDEN[1:0]               BCEN        DMAEN
   Access                                        R/W            R/W           R/W            R/W             R/W          R/W
    Reset                                         0              0             0                 0            0            0


               Bit 5 – MSBSEL Multi/Single Block Selection
               Write this bit to '1' when issuing multiple-block transfer commands using DAT line(s). For any other
               commands, write this bit to 0. If this bit is 0, it is not necessary to write BCR to '1' (refer to Table 1-4).

               Bit 4 – DTDSEL Data Transfer Direction Selection
               This bit defines the direction of the DAT lines data transfers. Write this bit to '1' to transfer data from the
               device (SD Card/SDIO/e.MMC) to the peripheral. Write this bit to '0' for all other commands.
                Value       Name            Description
                0           WRITE           Writes data from the peripheral to the device.
                1           READ            Reads data from the device to the peripheral.

               Bits 3:2 – ACMDEN[1:0] Auto Command Enable
               Two methods can be used to stop Multiple-block read and write operation:
                1. Auto CMD12: when the ACMDEN field is set to 1, the peripheral issues CMD12 automatically when
                     the last block transfer is completed. An Auto CMD12 error is indicated to ACESR. Auto CMD12 is
                     not enabled if the command does not require CMD12.




           © 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 1323
                                                   SAM D5x/E5x Family Data Sheet
                                                                          SD/MMC Host Controller ...

  2.   Auto CMD23: when the ACMDEN field is set to 2, the peripheral issues a CMD23 automatically
       before issuing a command specified in CR.
The following conditions are required to use Auto CMD23:
 • A memory card that supports CMD23 (SCR[33] = 1)
 • If DMA is used, it must be ADMA (SDMA not supported).
 • Only CMD18 or CMD25 is issued.
Note: The peripheral does not check the command index.
Auto CMD23 can be used with or without ADMA. By writing CR, the peripheral issues a CMD23 first and
then issues a command specified by the CR.CMDIDX field. If CMD23 response errors are detected, the
second command is not issued. A CMD23 error is indicated in ACESR. The CMD23 argument (32-bit
block count value) is defined in SSAR.
This field determines the use of auto command functions.
 Value       Name                         Description
 0           DISABLED                     Auto Command Disabled
 1           CMD12                        Auto CMD12 Enabled
 2           CMD23                        Auto CMD23 Enabled
 3           Reserved                     Reserved

Bit 1 – BCEN Block Count Enable
This bit is used to enable BCR, which is only relevant for multiple block transfers. When this bit is 0, BCR
is disabled, which is useful when executing an infinite transfer (refer to Table 1-4). If an ADMA2 transfer is
more than 65535 blocks, this bit is set to 0 and the data transfer length is designated by the Descriptor
Table.
 Value       Name                             Description
 0            DISABLED                        Block count is disabled
 1            ENABLED                         Block count is enabled

Bit 0 – DMAEN DMA Enable
This bit enables the DMA functionality described in section “Supporting DMA” in “SD Host Controller
Simplified Specification V3.00” . DMA can be enabled only if it is supported as indicated by the bit
CA0R.ADMA2SUP. One of the DMA modes can be selected using the field HC1R.DMASEL. If DMA is not
supported, this bit is meaningless and then always reads 0. When this bit is set to 1, a DMA operation
begins when the user writes to the upper byte of CR.
 Value      Name                         Description
 0          DISABLED                     DMA functionality is disabled
 1          ENABLED                      DMA functionality is enabled




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1324
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                 SD/MMC Host Controller ...

40.8.6         Command Register

               Name:          CR
               Offset:        0x0E
               Reset:         0x0000
               Property:      -


         Bit         15                 14       13            12             11                 10        9                  8
                                                                                   CMDIDX[5:0]
   Access                                        R/W          R/W            R/W             R/W          R/W            R/W
    Reset                                         0             0             0                  0         0                  0


         Bit         7                  6         5             4             3                  2         1                  0
                          CMDTYP[1:0]           DPSEL       CMDICEN       CMDCCEN                              RESPTYP[1:0]
   Access           R/W             R/W          R/W                         R/W                          R/W            R/W
    Reset            0                  0         0             0             0                            0                  0


               Bits 13:8 – CMDIDX[5:0] Command Index
               This bit shall be set to the command number (CMD0-63, ACMD0-63) that is specified in bits 45-40 of the
               Command-Format in the “Physical Layer Simplified Specification V3.01”, “SDIO Simplified Specification
               V3.00”, and “Embedded MultiMedia Card (e.MMC) Electrical Standard 4.51”.

               Bits 7:6 – CMDTYP[1:0] Command Type
               Value       Name     Description
               0           NORMAL Other commands
               1           SUSPEND CMD52 to write “Bus Suspend” in the Card Common Control Registers (CCCR)
                                    (for SDIO only)
               2           RESUME CMD52 to write “Function Select” in the Card Common Control Registers
                                    (CCCR) (for SDIO only)
               3           ABORT    CMD12, CMD52 to write “I/O Abort” in the Card Common Control Registers
                                    (CCCR) (for SDIO only)

               Bit 5 – DPSEL Data Present Select
               This bit is set to 1 to indicate that data is present and shall be transferred using the DAT lines. It is set to 0
               for the following:
                 1. Commands using only CMD line (Ex. CMD52)
                 2. Commands with no data transfer but using Busy signal on DAT[0] line (Ex. CMD38)
                 3. Resume command
               Value          Description
               0              No data present
               1              Data present

               Bit 4 – CMDICEN Command Index Check Enable
               If this bit is set to 1, the peripheral checks the Index field in the response to see if it has the same value
               as the command index. If it has not, it is reported as a Command Index Error (CMDIDX) in EISTR. If this
               bit is set to 0, the Index field of the response is not checked.
                Value          Name                   Description
                0              DISABLED               The Command Index Check is disabled.




           © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 1325
                                                     SAM D5x/E5x Family Data Sheet
                                                                              SD/MMC Host Controller ...

 Value        Name                   Description
 1            ENABLED                The Command Index Check is enabled.

Bit 3 – CMDCCEN Command CRC Check Enable
If this bit is set to 1, the peripheral checks the CRC field in the response. If an error is detected, it is
reported as a Command CRC Error (CMDCRC) in EISTR. If this bit is set to 0, the CRC field is not
checked. The position of the CRC field is determined according to the length of the response.
 Value          Name                    Description
 0              DISABLED                The Command CRC Check is disabled.
 1              ENABLED                 The Command CRC Check is enabled.

Bits 1:0 – RESPTYP[1:0] Response Type
This field is set according to the response type expected for the command index (CMDIDX).
 Value        Name                       Description
 0            NORESP                     No Response
 1            RL136                      Response Length 136
 2            RL48                       Response Length 48
 3            RL48BUSY                   Response Length 48 with Busy




© 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1326
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                   SD/MMC Host Controller ...

40.8.7         Response Register n

               Name:       RR
               Offset:     0x10 + n*0x04 [n=0..3]
               Reset:      0x000000000
               Property:   -


         Bit        31           30           29            28          27         26           25           24
                                                            CMDRESP[31:24]
   Access           R              R          R             R           R           R           R            R
    Reset           0              0          0             0           0           0           0            0


         Bit        23           22           21            20          19         18           17           16
                                                            CMDRESP[23:16]
   Access           R              R          R             R           R           R           R            R
    Reset           0              0          0             0           0           0           0            0


         Bit        15           14           13            12          11         10           9            8
                                                            CMDRESP[15:8]
   Access           R              R          R             R           R           R           R            R
    Reset           0              0          0             0           0           0           0            0


         Bit        7              6          5             4           3           2           1            0
                                                             CMDRESP[7:0]
   Access           R              R          R             R           R           R           R            R
    Reset           0              0          0             0           0           0           0            0


               Bits 31:0 – CMDRESP[31:0] Command Response
               The table below describes the mapping of command responses from the SD/SDIO/e.MMC bus to these
               registers for each responses type. In this table, R[] refers to a bit range of the response data as
               transmitted on the SD/SDIO/e.MMC bus.

               Type of response               Meaning of response              Response field Response register
               R1, R1b (normal response)      Card Status                      R[39:8]          RR0[31:0]
               R1b (Auto CMD12 response) Card Status for Auto CMD12            R[39:8]          RR3[31:0]
               R1 (Auto CMD23 response)       Card Status for Auto CMD23       R[39:8]          RR3[31:0]
               R2 (CID, CSD register)         CID or CSD register              R[127:8]         RR0[31:0]
                                                                                                RR1[31:0]
                                                                                                RR2[31:0]
                                                                                                RR3[23:0]

               R3 (OCR register)              OCR register for memory          R[39:8]          RR0[31:0]
               R4 (OCR register)              OCR register for I/O             R[39:8]          RR0[31:0]
               R5, R5b                        SDIO response                    R[39:8]          RR0[31:0]




           © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1327
                                                  SAM D5x/E5x Family Data Sheet
                                                                      SD/MMC Host Controller ...

...........continued
 Type of response                  Meaning of response            Response field Response register
 R6 (Published RCA                 New published RCA[31:16] and   R[39:8]        RR0[31:0]
 response)                         Card status bits




© 2019 Microchip Technology Inc.                   Datasheet                    DS60001507E-page 1328
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.8         Buffer Data Port Register

               Name:       BDPR
               Offset:     0x20
               Reset:      0x00000000
               Property:   -


         Bit        31            30           29           28              27         26             25           24
                                                             BUFDATA[31:24]
   Access          R/W           R/W          R/W           R/W            R/W         R/W            R/W         R/W
    Reset            0            0             0            0                  0       0              0           0


         Bit        23            22           21           20              19         18             17           16
                                                             BUFDATA[23:16]
   Access          R/W           R/W          R/W           R/W            R/W         R/W            R/W         R/W
    Reset            0            0             0            0                  0       0              0           0


         Bit        15            14           13           12              11         10              9           8
                                                              BUFDATA[15:8]
   Access          R/W           R/W          R/W           R/W            R/W         R/W            R/W         R/W
    Reset            0            0             0            0                  0       0              0           0


         Bit         7            6             5            4                  3       2              1           0
                                                                 BUFDATA[7:0]
   Access          R/W           R/W          R/W           R/W            R/W         R/W            R/W         R/W
    Reset            0            0             0            0                  0       0              0           0


               Bits 31:0 – BUFDATA[31:0] Buffer Data
               The peripheral's data buffer can be accessed through this 32-bit Data Port register.




           © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 1329
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                        SD/MMC Host Controller ...

40.8.9         Present State Register

               Name:        PSR
               Offset:      0x24
               Reset:       0x00F80000
               Property:    -


         Bit        31            30                29       28            27           26            25             24
                                                                                                                    CMDLL
   Access                                                                                                            R
    Reset                                                                                                             0


         Bit        23            22                21       20            19           18            17             16
                                       DATLL[3:0]                       WRPPL        CARDDPL       CARDSS       CARDINS
   Access            R            R                 R        R             R            R             R              R
    Reset            1            1                 1        1             1             0            0               0


         Bit        15            14                13       12            11           10            9               8
                                                                       BUFRDEN      BUFWREN         RTACT           WTACT
   Access                                                                  R            R             R              R
    Reset                                                                  0             0            0               0


         Bit         7            6                 5        4             3             2            1               0
                                                                        RTREQ         DLACT       CMDINHD       CMDINHC
   Access                                                                  R            R             R              R
    Reset                                                                  0             0            0               0


               Bit 24 – CMDLL CMD Line Level
               This status is used to check the CMD line level to recover from errors, and for debugging.

               Bits 23:20 – DATLL[3:0] DAT[3:0] Line Level
               This status is used to check the DAT line level to recover from errors, and for debugging. This is
               especially useful in detecting the Busy signal level from DAT[0].

               Bit 19 – WRPPL Write Protect Pin Level
               The Write Protect Switch is supported for memory and combo cards. This bit reflects the WP pin.
                Value     Description
                0         Write protected (WP = 0)
                1         Write enabled (WP = 1)

               Bit 18 – CARDDPL Card Detect Pin Level
               This bit reflects the inverse value of the CD pin. Debouncing is not performed on this bit. This bit may be
               valid when CARDSS is set to 1, but it is not guaranteed because of the propagation delay. Use of this bit
               is limited to testing since it must be debounced by software.
                Value        Description
                0            No card present (CD = 1)
                1            Card present (CD = 0)




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1330
                                                      SAM D5x/E5x Family Data Sheet
                                                                               SD/MMC Host Controller ...

Bit 17 – CARDSS Card State Stable
This bit is used for testing. If it is 0, the CARDDPL is not stable. If this bit is set to 1, it means that the
CARDDPL is stable. No Card state can be detected if this bit is set to 1 and CARDINS is set to 0.
The Software Reset For All (SWRSTALL) in SRR does not affect this bit.
 Value       Description
 0            Reset or debouncing
 1            No card or card inserted

Bit 16 – CARDINS Card Inserted
This bit indicates whether a card has been inserted. The peripheral debounces this signal so that the user
does not need to wait for it to stabilize.
A change from 0 to 1 rises the Card Insertion (CINS) status flag in NISTR if NISTER.CINS is set to 1. An
interrupt is generated if NISIER.CINS is set to 1.
A change from 1 to 0 rises the Card Removal (CREM) status flag in NISTR if NISTER.CREM is set to 1.
An interrupt is generated if NISIER.CREM is set to 1.
The Software Reset For All (SWRSTALL) in SRR does not affect this bit.

Bit 11 – BUFRDEN Buffer Read Enable
This bit is used for non-DMA read transfers. This flag indicates that valid data exists in the peripheral data
buffer. If this bit is 1, readable data exists in the buffer.
A change from 1 to 0 occurs when all the block data is read from the buffer.
A change from 0 to 1 occurs when block data is ready in the buffer. This rises the Buffer Read Ready
(BRDRDY) status flag in NISTR if NISTER.BRDRDY is set to 1. An interrupt is generated if
NISIER.BRDRDY is set to 1.

Bit 10 – BUFWREN Buffer Write Enable
This bit is used for non-DMA write transfers. This flag indicates if space is available for write data. If this
bit is 1, data can be written to the buffer.
A change from 1 to 0 occurs when all the block data are written to the buffer.
A change from 0 to 1 occurs when top of block data can be written to the buffer. This rises the Buffer
Write Ready (BRWRDY) status flag in NISTR if NISTER.BRWRDY is set to 1. An interrupt is generated if
NISIER.BRWRDY is set to 1.

Bit 9 – RTACT Read Transfer Active
This bit is used to detect completion of a read transfer. Refer to section “Read Transaction Wait /
Continue Timing” in the “SD Host Controller Simplified Specification V3.00” for more details on the
sequence of events.
This bit is set to 1 in either of the following conditions:
 • After the end bit of the read command.
 • When a read operation is restarted by writing a 1 to BGCR.CONTR (Continue Request).
This bit is cleared to 0 in either of the following conditions:
 • When the last data block as specified by Transfer Block Size (BLKSIZE) is transferred to the system.
 • In case of ADMA2, end of read is designated by the descriptor table.
 • When all valid data blocks in the peripheral have been transferred to the system and no current block
    transfers are being sent as a result of the Stop At Block Gap Request (STPBGR) of BGCR being set
    to 1.
A change from 1 to 0 rises the Transfer Complete (TRFC) status flag in NISTR if NISTER.TRFC is set to
1. An interrupt is generated if NISIER.TRFC is set to 1.




© 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 1331
                                                      SAM D5x/E5x Family Data Sheet
                                                                               SD/MMC Host Controller ...

Bit 8 – WTACT Write Transfer Active
This bit indicates a write transfer is active. If this bit is 0, it means no valid write data exists in the
peripheral. Refer to section “Write Transaction Wait / Continue Timing” in the “SD Host Controller
Simplified Specification V3.00” for more details on the sequence of events.
This bit is set to 1 in either of the following conditions:
 • After the end bit of the write command.
 • When a write operation is restarted by writing a 1 to BGCR.CONTR (Continue Request).
This bit is cleared to 0 in either of the following conditions:
 • After getting the CRC status of the last data block as specified by the transfer count (single and
    multiple). In case of ADMA2, transfer count is designated by the descriptor table.
 • After getting the CRC status of any block where a data transmission is about to be stopped by a Stop
    At Block Gap Request (STPBGR) of BGCR.
During a write transaction and as the result of the Stop At Block Gap Request (STPBGR) being set, a
change from 1 to 0 rises the Block Gap Event (BLKGE) status flag in NISTR if NISTER.BLKGE is set to 1.
An interrupt is generated if BLKGE is set to 1 in NISIER. This status is useful to determine whether non-
DAT line commands can be issued during Write Busy.

Bit 3 – RTREQ Retuning Request
The peripheral can instruct the software to execute a re-tuning sequence by setting this bit when the data
window is shifted by a temperature drift and a tuned sampling point does not have a good margin to
receive correct data.
This bit is cleared to 0 when a command is issued by setting Execute Tuning (EXTUN) in HC2R.
A change from 0 to 1 rises the Re-Tuning Event (RTEVT) status flag in NISTR if NISTER.RTEVT is set to
1. An interrupt is generated if NISIER.RTEVT is set to 1.
This bit is not set to 1 if Sampling Clock Select (SCLKSEL) in HC2R is set to 0 (using a fixed sampling
clock). Refer to Re-Tuning Modes (RTMODE) in CA1R.
 Value        Description
 0            Fixed or well-tuned sampling clock
 1            Sampling clock needs re-tuning

Bit 2 – DLACT DAT Line Active
This bit indicates whether one of the DAT lines on the bus is in use.
In the case of read transactions:
This status indicates whether a read transfer is executing on the bus. A change from 1 to 0 resulting from
setting the Stop At Block Gap Request (STPBGR) rises the Block Gap Event (BLKGE) status flag in
NISTR if NISTER.BLKGE is set to 1. An interrupt is generated if NISIER.BLKGE is set to 1. Refer to
section “Read Transaction Wait / Continue Timing” in the “SD Host Controller Simplified Specification
V3.00” for details on timing.
This bit is set in either of the following cases:
  • After the end bit of the read command.
  • When writing 1 to BGCR.CONTR (Continue Request) to restart a read transfer.
This bit is peripheral cleared in either of the following cases:
 • When the end bit of the last data block is sent from the bus to the peripheral. In case of ADMA2, the
    last block is designated by the last transfer of the Descriptor Table.
 • When a read transfer is stopped at the block gap initiated by a Stop At Block Gap Request
    (STPBGR).




© 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 1332
                                                  SAM D5x/E5x Family Data Sheet
                                                                          SD/MMC Host Controller ...

The peripheral stops a read operation at the start of the interrupt cycle by driving the Read Wait (DAT[2]
line) or by stopping the SD Clock. If the Read Wait signal is already driven (due to the fact that the data
buffer cannot receive data), the peripheral can continue to stop the read operation by driving the Read
Wait signal. It is necessary to support the Read Wait in order to use the Suspend/Resume operation.
In the case of write transactions:
This status indicates that a write transfer is executing on the bus. A change from 1 to 0 rises the Transfer
Complete (TRFC) status flag in NISTR if NISTER.TRFC is set to 1. An interrupt is generated if
NISIER.TRFC is set to 1. Refer to section “Write Transaction Wait / Continue Timing” in the “SD Host
Controller Simplified Specification V3.00” for details on timing.
This bit is set in either of the following cases:
  • After the end bit of the write command.
  • When writing 1 to BGCR.CONTR (Continue Request) to continue a write transfer.
This bit is cleared in either of the following cases:
 • When the card releases Write Busy of the last data block. If the card does not drive a Busy signal for
    8 SDCLK, the peripheral considers the card drive “Not Busy”. In the case of ADMA2, the last block is
    designated by the last transfer of the Descriptor Table.
 • When the card releases Write Busy prior to wait for write transfer as a result of a Stop At Block Gap
    Request (STPBGR).
Command with Busy:
This status indicates whether a command that indicates Busy (ex. erase command for memory) is
executing on the bus. This bit is set to 1 after the end bit of the command with Busy and cleared when
Busy is de-asserted. A change from 1 to 0 rises the Transfer Complete (TRFC) status flag in NISTR if
NISTER.TRFC is set to 1. An interrupt is generated if NISIER.TRFC is set to 1. Refer to Figures 2.11 to
2.13 in the “SD Host Controller Simplified Specification V3.00”.
 Value       Description
 0           DAT Line Inactive
 1           DAT Line Active

Bit 1 – CMDINHD Command Inhibit (DAT)
This status bit is 1 if either the DAT Line Active (DLACT) or the Read Transfer Active (RTACT) is set to 1.
If this bit is 0, it indicates that the peripheral can issue the next command. Commands with a Busy signal
belong to Command Inhibit (DAT) (ex. R1b, R5b type). A change from 1 to 0 rises the Transfer Complete
(TRFC) status flag in NISTR if NISTER.TRFC is set to 1. An interrupt is generated if NISIER.TRFC is set
to 1.
Note: The software can save registers in the 000-00Dh range for a suspend transaction after this bit has
changed from 1 to 0.
 Value          Description
 0              Can issue a command which uses the DAT line(s).
 1              Cannot issue a command which uses the DAT line(s).

Bit 0 – CMDINHC Command Inhibit (CMD)
If this bit is 0, it indicates the CMD line is not in use and the peripheral can issue a command using the
CMD line. This bit is set to 1 immediately after CR is written. This bit is cleared when the command
response is received. Auto CMD12 and Auto CMD23 consist of two responses. In this case, this bit is not
cleared by the CMD12 or CMD23 response, but by the Read/Write command response.
Status issuing Auto CMD12 is not read from this bit. So, if a command is issued during Auto CMD12
operation, the peripheral manages to issue both commands: CMD12 and a command set by CR.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1333
                                                 SAM D5x/E5x Family Data Sheet
                                                                       SD/MMC Host Controller ...

Even if the Command Inhibit (DAT) is set to 1, commands using only the CMD line can be issued if this bit
is 0.
A change from 1 to 0 rises the Command Complete (CMDC) status flag in NISTR if NISTER.CMDC is set
to 1. An interrupt is generated if NISIER.CMDC is set to 1.
If the peripheral cannot issue the command because of a command conflict error (refer to CMDCRC in
EISTR) or because of a ‘Command Not Issued By Auto CMD12’ error (refer to Section 1.2.31 “SDMMC
Auto CMD Error Status Register”), this bit remains 1 and Command Complete is not set.
 Value       Description
 0           Can issue a command using only CMD line.
 1           Cannot issue a command.




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1334
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.10 Host Control 1 Register

            Name:        HC1R
            Offset:      0x28
            Reset:       0x00
            Property:    -


      Bit         7             6             5             4                 3         2            1             0
             CARDDSEL       CARDDTL                             DMASEL[1:0]          HSEN           DW          LEDCTRL
  Access         R/W           R/W                                                    R/W           R/W           R/W
   Reset          0             0                           0                 0         0            0             0


            Bit 7 – CARDDSEL Card Detect Signal Selection
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            This bit selects the source for the card detection.
             Value       Description
             0           The CD pin is selected.
             1           The Card Detect Test Level (CARDDTL) is selected (for test purpose).

            Bit 6 – CARDDTL Card Detect Test Level
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            This bit is enabled while the Card Detect Signal Selection (CARDDSEL) is set to 1 and it indicates
            whether the card is inserted or not.
             Value       Description
             0           No card.
             1           Card inserted.

            Bits 4:3 – DMASEL[1:0] DMA Select
            One of the supported DAM modes can be selected. The user must check support of DMA modes by
            referring the CA0R. Use of selected DMA is determined by DMA Enable (DMAEN) in TMR.
             Value       Name                 Description
             0           SDMA                 SDMA is selected
             1           Reserved             Reserved
             2           ADMA32               32-bit Address ADMA2 is selected
             3           Reserved             Reserved

            Bit 2 – HSEN High Speed Enable
            Before setting this bit, the user must check the High Speed Support (HSSUP) in CA0R.
            If this bit is set to 0 (default), the peripheral outputs CMD line and DAT lines at the falling edge of the SD
            clock (up to 25 MHz). If this bit is set to 1, the SDMMC outputs the CMD line and the DAT lines at the
            rising edge of the SD clock (up to 50 MHz).
            If Preset Value Enable (PVALEN) in HC2R is set to 1, the user needs to reset SD Clock Enable
            (SDCLKEN) before changing this bit to avoid generating clock glitches. After setting this bit to 1, the user
            sets SDCLEN to 1 again.
             Value          Description
             0              Normal Speed mode.




        © 2019 Microchip Technology Inc.                           Datasheet                         DS60001507E-page 1335
                                                     SAM D5x/E5x Family Data Sheet
                                                                             SD/MMC Host Controller ...

 Value        Description
 1            High Speed mode.
              Note: 1. This bit is effective only if MC1R.DDR is set to 0.
              2. The clock divider (DIV) in CCR must be set to a value different from 0 when HSEN is 1.

Bit 1 – DW Data Width
This bit selects the data width of the peripheral. It must be set to match the data width of the card.
Note: If the Extended Data Transfer Width is 1, this bit has no effect and the data width is 8-bit mode.
 Value        Name                              Description
 0            1_BIT                             1-bit mode
 1            4_BIT                             4-bit mode

Bit 0 – LEDCTRL LED Control
Note:
This register entry is specific to the SD/SDIO operation mode.
This bit is used to caution the user not to remove the card while it is being accessed. If the software is
going to issue multiple commands, this bit is set to 1 during all transactions.
 Value       Name                              Description
 0            OFF                              LED off
 1            ON                               LED on




© 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1336
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                         SD/MMC Host Controller ...

40.8.11 Power Control Register

            Name:        PCR
            Offset:      0x29
            Reset:       0x0E
            Property:    -


      Bit         7             6              5             4             3             2              1              0
                                                                                   SDBVSEL[2:0]                   SDBPWR
  Access                                                                  R/W           R/W           R/W             R/W
   Reset                                                                   1             1              1              0


            Bits 3:1 – SDBVSEL[2:0] SD Bus Voltage Select
            By setting this bit, the user selects the voltage level for the card. Before setting this register, the user must
            check the Voltage Support in CA0R. If an unsupported voltage is selected, the system does not supply
            the bus voltage.
             Value       Name                                   Description
             0x0-0x4 Reserved                                   Reserved
             0x5         1V8                                    1.8 Volt (Typical)
             0x6         3V0                                    3.0 Volt (Typical)
             0x7         3V3                                    3.3 Volt (Typical)

            Bit 0 – SDBPWR SD Bus Power
            This bit is automatically cleared by the peripheral if the card is removed. If this bit is cleared, the
            peripheral stops driving CMD and DAT[7:0] (tri-state) and drives CK to low level.




        © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 1337
                                                                SAM D5x/E5x Family Data Sheet
                                                                                        SD/MMC Host Controller ...

40.8.12 Block Gap Control Register

            Name:        BGCR
            Offset:      0x2A
            Reset:       0x00
            Property:    -


      Bit         7             6             5             4              3             2             1             0
                                                                        INTBG        RWCTRL         CONTR        STPBGR
  Access                                                                 R/W           R/W           R/W            R/W
   Reset                                                                   0             0             0             0


            Bit 3 – INTBG Interrupt at Block Gap
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            This bit is valid only in 4-bit mode of the SDIO card and selects a sample point in the interrupt cycle.
            Setting to 1 enables interrupt detection at the block gap for a multiple block transfer. If the SDIO card
            cannot signal an interrupt during a multiple block transfer, this bit should be set to 0. When the software
            detects an SDIO card insertion, it sets this bit according to the CCCR of the SDIO card.
             Value        Name                          Description
             0            DISABLED                      Interrupt detection disabled
             1            ENABLED                       Interrupt detection enabled

            Bit 2 – RWCTRL Read Wait Control
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            The Read Wait control is optional for SDIO cards. If the card supports Read Wait, set this bit to enable
            use of the Read Wait protocol to stop read data using the DAT[2] line. Otherwise, the peripheral stops the
            SDCLK to hold read data, which restricts command generation. When the software detects an SD card
            insertion, this bit must be set according to the CCCR of the SDIO card. If the card does not support Read
            Wait, this bit shall never be set to 1, otherwise an DAT line conflict may occur. If this bit is set to 0,
            Suspend/Resume cannot be supported.
             Value        Description
             0            Disables Read Wait control.
             1            Enables Read Wait control.

            Bit 1 – CONTR Continue Request
            This bit is used to restart a transaction which was stopped using a Stop At Block Gap Request
            (STPBGR). To cancel stop at the block gap, set STPBGR to 0 and set this bit to 1 to restart the transfer.
            The peripheral automatically clears this bit in either of the following cases:
              • In the case of a read transaction, the DAT Line Active (DLACT) changes from 0 to 1 as a read
                 transaction restarts.
              • In the case of a write transaction, the Write Transfer Active (WTACT) changes from 0 to 1 as the
                 write transaction restarts.
            Therefore, it is not necessary to set this bit to 0. If STPBGR is set to 1, any write to this bit is ignored.
            Refer to the “Abort Transaction” and “Suspend/Resume” sections in the “SD Host Controller Simplified
            Specification V3.00” for more details.




        © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 1338
                                                   SAM D5x/E5x Family Data Sheet
                                                                           SD/MMC Host Controller ...

 Value        Description
 0            No affect
 1            Restart

Bit 0 – STPBGR Stop At Block Gap Request
This bit is used to stop executing read and write transactions at the next block gap for non-DMA, SDMA,
and ADMA transfers. The user must leave this bit set to 1 until Transfer Complete (TRFC) in NISTR.
Clearing both Stop At Block Gap Request and Continue Request does not cause the transaction to
restart. This bit can be set whether the card supports the Read Wait signal or not.
During read transfers, the peripheral stops the transaction by using the Read Wait signal (DAT[2]) if
supported, or by stopping the SD clock otherwise.
In case of write transfers in which the user writes data to BDPR, this bit must be set to 1 after all the block
of data is written. If this bit is set to 1, the user does not write data to BDPR.
This bit affects Read Transfer Active (RTACT), Write Transfer Active (WTACT), DAT Line Active (DLACT)
and Command Inhibit (DAT) (CMDINHD) in PSR.
Refer to the “Abort Transaction” and “Suspend/Resume” sections in the “SD Host Controller Simplified
Specification V3.00” for more details.
 Value       Description
 0            Transfer
 1            Stop




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1339
                                                            SAM D5x/E5x Family Data Sheet
                                                                                 SD/MMC Host Controller ...

40.8.13 Wakeup Control Register: SD/SDIO

           Name:       WCR
           Offset:     0x2B
           Reset:      0x00
           Property:   -


     Bit         7            6            5            4            3            2            1            0
                                                                             WKENCREM     WKENCINS      WKENCINT
  Access                                                                         R/W          R/W          R/W
   Reset                                                                          0            0            0


           Bit 2 – WKENCREM Wake-up Event Enable on Card Removal
           This bit enables a wake-up event via Card Removal (CREM) in NISTR. FN_WUS (Wake-Up Support) in
           the CIS (Card Information Structure) does not affect this bit.
            Value      Name                          Description
            0          DISABLED                      Wake-Up Event disabled
            1          ENABLED                       Wake-Up Event enabled

           Bit 1 – WKENCINS Wake-Up Event Enable on Card Insertion
           This bit enables a wake-up event via Card Insertion (CINS) in NISTR. FN_WUS (Wake-Up Support) in
           the CIS (Card Information Structure) does not affect this bit.
            Value      Name                          Description
            0          DISABLED                      Wake-Up Event disabled
            1          ENABLED                       Wake-Up Event enabled

           Bit 0 – WKENCINT Wake-Up Event Enable on Card Interrupt
           This bit enables a wake-up event via Card Interrupt (CINT) in NISTR. This bit can be set to 1 if FN_WUS
           (Wake-Up Support) in the CIS (Card Information Structure) is set to 1 in the SDIO card.
            Value      Name                          Description
            0          DISABLED                      Wake-Up Event disabled
            1          ENABLED                       Wake-Up Event enabled




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1340
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.14 Clock Control Register

            Name:       CCR
            Offset:     0x2C
            Reset:      0x0000
            Property:   -


      Bit        15             14           13          12            11           10            9            8
                                                          SDCLKFSEL[7:0]
  Access        R/W             R/W          R/W         R/W          R/W           R/W          R/W          R/W
   Reset          0              0            0           0            0             0            0            0


      Bit         7              6            5           4            3             2            1            0
                 USDCLKFSEL[1:0]           CLKGSEL                               SDCLKEN       INTCLKS     INTCLKEN
  Access        R/W             R/W          R/W                                    R/W          R/W          R/W
   Reset          0              0            0                                      0            0            0


            Bits 15:8 – SDCLKFSEL[7:0] SDCLK Frequency Select
            This register is used to select the frequency of the SDCLK pin. There are two SDCLK Frequency modes
            according to Clock Generator Select (CLKGSEL).
            The length of the clock divider (DIV) is extended to 10 bits (DIV[9:8] = USDCLKFSEL, DIV[7:0] =
            SDCLKFSEL)
            – 10-bit Divided Clock Mode (CLKGSEL = 0):
            �SDCLK = �BASECLK / 2 × DIV

            . If DIV = 0 then
            �SDCLK = �BASECLK

            – Programmable Clock Mode (CLKGSEL = 1):
            �SDCLK = �MULTCLK / DIV+1

            This field depends on the setting of Preset Value Enable (PVALEN) in HC2R.
            If HC2R.PVALEN = 0, this field is set by the user.
            If HC2R.PVALEN = 1, this field is automatically set to a value specified in one of the PVR.

            Bits 7:6 – USDCLKFSEL[1:0] Upper Bits of SDCLK Frequency Select
            These bits expand the SDCLK Frequency Select (SDCLKFSEL) to 10 bits. These two bits are assigned
            to bit 09-08 of the clock divider as described in SDCLKFSEL.

            Bit 5 – CLKGSEL Clock Generator Select
            This bit is used to select the clock generator mode in the SDCLK Frequency Select field. If the
            Programmable mode is not supported (CA1R.CLKMULT (Clock Multiplier) set to 0), then this bit cannot
            be written and is always read at 0.
            This bit depends on the setting of Preset Value Enable (PVALEN) in HC2R.
            If HC2R.PVALEN = 0, this bit is set by the user.
            If HC2R.PVALEN = 1, this bit is automatically set to a value specified in one of the PVRx.
             Value       Description
             0            Divided Clock mode (BASECLK is used to generate SDCLK).
             1            Programmable Clock mode (MULTCLK is used to generate SDCLK).




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1341
                                                    SAM D5x/E5x Family Data Sheet
                                                                            SD/MMC Host Controller ...

Bit 2 – SDCLKEN SD Clock Enable
The peripheral stops the SD Clock when writing this bit to 0. SDCLK Frequency Select (SDCLKFSEL)
can be changed when this bit is 0. Then, the peripheral maintains the same clock frequency until SDCLK
is stopped (Stop at SDCLK=0). If Card Inserted (CARDINS) in PSR is cleared, this bit is also cleared.
 Value      Description
 0          SD Clock disabled
 1          SD Clock enabled

Bit 1 – INTCLKS Internal Clock Stable
This bit is set to 1 when the SD clock is stable after setting CCR.INTCLKEN (Internal Clock Enable) to 1.
The user must wait to set SD Clock Enable (SDCLKEN) until this bit is set to 1.
 Value        Description
 0            Internal clock not ready
 1            Internal clock ready

Bit 0 – INTCLKEN Internal Clock Enable
This bit is set to 0 when the peripheral is not used or is awaiting a wakeup interrupt. In this case, its
internal clock is stopped to reach a very low power state. Registers are still able to be read and written.
The clock starts to oscillate when this bit is set to 1. Once the clock oscillation is stable, the peripheral
sets Internal Clock Stable (INTCLKS) in this register to 1.
This bit does not affect card detection.
 Value        Description
 0            The internal clock stops.
 1            The internal clock oscillates.




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1342
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   SD/MMC Host Controller ...

40.8.15 Timeout Control Register

            Name:       TCR
            Offset:     0x2E
            Reset:      0x00
            Property:   -


      Bit         7            6            5            4            3            2                 1            0
                                                                                       DTCVAL[3:0]
  Access                                                             R/W          R/W            R/W             R/W
   Reset                                                              0            0                 0            0


            Bits 3:0 – DTCVAL[3:0] Data Timeout Counter Value
            This value determines the interval at which DAT line timeouts are detected. For more information about
            timeout generation, refer to Data Timeout Error (DATTEO) in EISTR. When setting this register, the user
            can prevent inadvertent timeout events by clearing the Data Timeout Error Status Enable (in EISTER).
                            213 + DTCVAL
            TIMEOUT μS =
                           �BASECLK MHz

            Note: DTCVAL = F(Hexa) is reserved.




        © 2019 Microchip Technology Inc.                      Datasheet                              DS60001507E-page 1343
                                                                SAM D5x/E5x Family Data Sheet
                                                                                SD/MMC Host Controller ...

40.8.16 Software Reset Register

            Name:        SRR
            Offset:      0x2F
            Reset:       0x00
            Property:    -


      Bit         7             6             5             4           3       2            1           0
                                                                             SWRSTDAT   SWRSTCMD     SWRSTALL
  Access                                                                       R/W          R/W         R/W
   Reset                                                                        0            0           0


            Bit 2 – SWRSTDAT Software reset for DAT line
            Only part of a data circuit is reset. The DMA circuit is also reset.
            The following registers and bits are cleared by this bit:
             • Buffer Data Port Register 40.8.8 BDPR: BUFDATA is cleared and initialized.
             • Present State Register 40.8.9 PSR:
                  – Buffer Read Enable (BUFRDEN)
                  – Buffer Write Enable (BUFWREN)
                  – Read Transfer Active (RTACT)
                  – Write Transfer Active (WTACT)
                  – DAT Line Active (DATLL)
                  – Command Inhibit - DAT (CMDINHD)
             • Block Gap Control Register 40.8.12 BGCR:
                  – Continue Request (CONTR)
                  – Stop At Block Gap Request (STPBGR)
             • Normal Interrupt Status Register 40.8.17 NISTR:
                  – Buffer Read Ready (BRDRDY)
                  – Buffer Write Ready (BWRRDY)
                  – DMA Interrupt (DMAINT)
                  – Block Gap Event (BLKGE)
                  – Transfer Complete (TRFC)
            Value       Description
            0           Work
            1           Reset

            Bit 1 – SWRSTCMD Software reset for CMD line
            Only part of a command circuit is reset.
            The following registers and bits are cleared by this bit:
             • Present State Register 40.8.9 PSR:
                  – Command Inhibit (CMD) (CMDINHC)
             • Normal Interrupt Status Register 40.8.17 NISTR:
                  – Command Complete (CMDC)




        © 2019 Microchip Technology Inc.                         Datasheet                  DS60001507E-page 1344
                                                    SAM D5x/E5x Family Data Sheet
                                                                            SD/MMC Host Controller ...

 Value        Description
 0            Work
 1            Reset

Bit 0 – SWRSTALL Software reset for All
This reset affects the entire peripheral except the card detection circuit. During initialization, the peripheral
must be reset by setting this bit to 1. This bit is automatically cleared to 0 when CA0R and CA1R are valid
and the user can read them. If this bit is set to 1, the user should issue a reset command and reinitialize
the card.
List of registers cleared to 0:
  • SDMA System Address / Argument 2 Register 40.8.1 SSAR
  • Block Size Register 40.8.2 BSR
  • Block Count Register 40.8.3 BCR
  • Argument 1 Register 40.8.4 ARG1R
  • Transfer Mode Register 40.8.5 TMR
  • Command Register 40.8.6 CR
  • Response Register n 40.8.7 RR
  • Buffer Data Port Register 40.8.8 BDPR
  • Present State Register 40.8.9 PSR (except CMDLL, DATLL, WRPPL, CARDDDPL, CARDSS,
     CARDINS)
  • Host Control 1 Register 40.8.10 HC1R
  • Power Control Register 40.8.11 PCR
  • Block Gap Control Register 40.8.12 BGCR
  • Wakeup Control Register 40.8.13 WCR
  • Clock Control Register 40.8.14 CCR
  • Timeout Control Register 40.8.15 TCR
  • Normal Interrupt Status Register 40.8.17 NISTR
  • Error Interrupt Status Register 40.8.18 EISTR
  • Normal Interrupt Status Enable Register 40.8.19 NISTER
  • Error Interrupt Status Enable Register 40.8.20 EISTER
  • Normal Interrupt Signal Enable Register 40.8.21 NISIER
  • Error Interrupt Signal Enable Register 40.8.22 EISIER
  • Auto CMD Error Status Register 40.8.23 ACESR
  • Host Control 2 Register 40.8.25 HC2R - DEFAULT
  • ADMA Error Status Register 40.8.31 AESR
  • ADMA System Address Registers 40.8.32 ASAR
  • Slot Interrupt Status Register 40.8.34 SISR
  • e.MMC Control 1 Register 40.8.37 MC1R
  • e.MMC Control 2 Register 40.8.38 MC2R
  • AHB Control Register 40.8.39 ACR
  • Clock Control 2 Register 40.8.40 CC2R
  • Capabilities Control Register 40.8.41 CACR (except KEY)
 Value        Description
 0            Work




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1345
                                   SAM D5x/E5x Family Data Sheet
                                               SD/MMC Host Controller ...

 Value        Description
 1            Reset




© 2019 Microchip Technology Inc.   Datasheet            DS60001507E-page 1346
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                          SD/MMC Host Controller ...

40.8.17 Normal Interrupt Status Register

            Name:        NISTR
            Offset:      0x30
            Reset:       0x0000
            Property:    -


      Bit         15            14            13             12            11             10             9             8
               ERRINT        BOOTAR                                                                                  CINT
  Access         R/W           R/W                                                                                    R/W
   Reset          0              0                                                                                     0


      Bit         7              6             5             4              3             2              1             0
                CREM           CINS        BRDRDY         BWRRDY         DMAINT        BLKGE          TRFC           CMDC
  Access         R/W           R/W            R/W           R/W           R/W            R/W           R/W            R/W
   Reset          0              0             0             0              0             0              0             0


            Bit 15 – ERRINT Error Interrupt
            If any of the bits in EISTR are set, then this bit is set. Therefore, the user can efficiently test for an error
            by checking this bit first. This bit is read-only.
             Value       Description
             0           No error
             1           Error

            Bit 14 – BOOTAR Boot Acknowledge Received
            Note: This register entry is specific to the e.MMC operation mode.
            This bit is set to 1 when the peripheral received a Boot Acknowledge pattern from the e.MMC.
            This bit can only be set to 1 if NISTER.BOOTAR is set to 1. An interrupt can only be generated if
            NISIER.BOOTAR is set to 1.
            Writing this bit to 1 clears this bit.
             Value        Description
             0            Boot Acknowledge pattern not received.
             1            Boot Acknowledge pattern received.

            Bit 8 – CINT Card Interrupt
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            Writing this bit to 1 does not clear this bit. It is cleared by resetting the SD card interrupt factor. In 1-bit
            mode, the peripheral detects the Card Interrupt without SDCLK to support wake-up. In 4-bit mode, the
            Card Interrupt signal is sampled during the interrupt cycle, so there are some sample delays between the
            interrupt signal from the SD card and the interrupt to the system.
            When this bit has been set to 1 and the user needs to start this interrupt service, Card Interrupt Status
            Enable (CINT) in NISTER may be set to 0 in order to clear the card interrupt statuses latched in the
            peripheral and to stop driving the interrupt signal to the system. After completion of the card interrupt
            service (it should reset interrupt factors in the SD card and the interrupt signal may not be asserted), set
            NISTER.CINT to 1 and start sampling the interrupt signal again.
            Interrupt detected by DAT[1] is supported when there is one card per slot. In case of a shared bus,
            interrupt pins are used to detect interrupts. If 0 is set to Interrupt Pin Select (INTPSEL) in SBCR, this




        © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1347
                                                 SAM D5x/E5x Family Data Sheet
                                                                        SD/MMC Host Controller ...

status is effective. If a non-zero value is set to INTPSEL, INT_A, INT_B or INT_C is used as device
interrupts.
This bit can only be set to 1 if NISTER.CREM is set to 1. An interrupt can only be generated if
NISIER.CREM is set to 1.
 Value       Description
 0            No card interrupt
 1            Card interrupt

Bit 7 – CREM Card Removal
Note:
This register entry is specific to the SD/SDIO operation mode.
This status is set to 1 if Card Inserted (CARDINS) in PSR changes from 1 to 0. When the user writes this
bit to 1 to clear this status, the status of PSR.CARDINS must be confirmed because the card detect state
may possibly be changed when the user clears this bit and no interrupt event can be generated.
This bit can only be set to 1 if NISTER.CREM is set to 1. An interrupt can only be generated if
NISIER.CREM is set to 1.
Writing this bit to 1 clears this bit.
 Value        Description
 0            Card state unstable or card inserted
 1            Card removed

Bit 6 – CINS Card Insertion
Note:
This register entry is specific to the SD/SDIO operation mode.
This status is set if Card Inserted (CARDINS) in PSR changes from 0 to 1. When the user writes this bit to
1 to clear this status, the status of PSR.CARDINS must be confirmed because the card detect state may
possibly be changed when the user clears this bit and no interrupt event can be generated.
This bit can only be set to 1 if NISTER.CINS is set to 1. An interrupt can only be generated if
NISIER.CINS is set to 1.
Writing this bit to 1 clears this bit.
 Value       Description
 0           Card state unstable or card removed
 1           Card inserted

Bit 5 – BRDRDY Buffer Read Ready
This status is set to 1 if the Buffer Read Enable (BUFRDEN) changes from 0 to 1. Refer to BUFRDEN in
PSR.
This bit can only be set to 1 if NISTER.BRDRDY is set to 1. An interrupt can only be generated if
NISIER.BRDRDY is set to 1.
Writing this bit to 1 clears this bit.
 Value       Description
 0           Not ready to read buffer
 1           Ready to read buffer

Bit 4 – BWRRDY Buffer Write Ready
This status is set to 1 if the Buffer Write Enable (BUFWREN) changes from 0 to 1. Refer to BUFWREN in
PSR.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1348
                                                    SAM D5x/E5x Family Data Sheet
                                                                           SD/MMC Host Controller ...

This bit can only be set to 1 if NISTER.BWRRDY is set to 1. An interrupt can only be generated if
NISIER.BWRRDY is set to 1.
Writing this bit to 1 clears this bit.
 Value       Description
 0           Not ready to write buffer
 1           Ready to write buffer

Bit 3 – DMAINT DMA Interrupt
This status is set if the peripheral detects the Host SDMA Buffer boundary during transfer. Refer to SDMA
Buffer Boundary (BOUNDARY) in BSR.
In case of ADMA, by setting the “int” field in the descriptor table, the peripheral rises this status flag when
the descriptor line is completed. This status flag does not rise after Transfer Complete (TRFC).
This bit can only be set to 1 if NISTER.DMAINT is set to 1. An interrupt can only be generated if
NISIER.DMAINT is set to 1.
Writing this bit to 1 clears this bit.
 Value       Description
 0           No DMA Interrupt
 1           DMA Interrupt

Bit 2 – BLKGE Block Gap Event
If the Stop At Block Gap Request (STPBGR) in BGCR is set to 1, this bit is set when either a read or a
write transaction is stopped at a block gap. If STPBGR is not set to 1, this bit is not set to 1.
In the case of a Read transaction:
This bit is set at the falling edge of the DAT Line Active (DLACT) status (when the transaction is stopped
at SD bus timing). The Read Wait must be supported in order to use this function. Refer to section “Read
Transaction Wait / Continue Timing” in the “SD Host Controller Simplified Specification V3.00” about the
detailed timing.
In the case of a Write transaction:
This bit is set at the falling edge of the Write Transfer Active (WTACT) status (after getting the CRC status
at SD bus timing). Refer to section “Write Transaction Wait / Continue Timing” in the “SD Host Controller
Simplified Specification V3.00” for more details on the sequence of events.
This bit can only be set to 1 if NISTER.BLKGE is set to 1. An interrupt can only be generated if
NISIER.BLKGE is set to 1.
Writing this bit to 1 clears this bit.
 Value        Description
 0            No block gap event
 1            Transaction stopped at block gap

Bit 1 – TRFC Transfer Complete
This bit is set when a read/write transfer and a command with Busy is completed.
In the case of a Read Transaction:
This bit is set at the falling edge of the Read Transfer Active Status. The interrupt is generated in two
cases. The first is when a data transfer is completed as specified by the data length (after the last data
has been read to the system). The second is when data has stopped at the block gap and completed the
data transfer by setting the Stop At Block Gap Request (STPBGR) in BGCR (after valid data has been
read to the system). Refer to section “Read Transaction Wait / Continue Timing” in the “SD Host
Controller Simplified Specification V3.00” for more details on the sequence of events.
In the case of a Write Transaction:




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1349
                                                   SAM D5x/E5x Family Data Sheet
                                                                          SD/MMC Host Controller ...

This bit is set at the falling edge of the DAT Line Active (DLACT) status. This interrupt is generated in two
cases. The first is when the last data is written to the card as specified by the data length and the Busy
signal is released. The second is when data transfers are stopped at the block gap by setting Stop At
Block Gap Request (STPBGR) in BGCR and data transfers are completed. (After valid data is written to
the card and the Busy signal is released). Refer to section “Write Transaction Wait / Continue Timing” in
the “SD Host Controller Simplified Specification V3.00” for more details on the sequence of events.
In the case of command with Busy:
This bit is set when Busy is de-asserted. Refer to DAT Line Active (DLACT) and Command Inhibit (DAT)
(CMDINHD) in PSR.
This bit can only be set to 1 if NISTER.TRFC is set to 1. An interrupt can only be generated if
NISIER.TRFC is set to 1.
Writing this bit to 1 clears this bit.
The table below shows that Transfer Complete (TRFC) has a higher priority than Data Timeout Error
(DATTEO). If both bits are set to 1, execution of a command can be considered to be completed.

 TRFC             DATTEO                 Meaning of the status
 0                0                      Interrupted by another factor
 0                1                      Timeout occurred during transfer
 1                Don’t Care             Command execution complete

 Value        Description
 0            Command execution is not complete.
 1            Command execution is complete.

Bit 0 – CMDC Command Complete
This bit is set when getting the end bit of the command response. Auto CMD12 and Auto CMD23 consist
of two responses. Command Complete is not generated by the response of CMD12 or CMD23, but it is
generated by the response of a read/write command. Refer to Command Inhibit (CMD) in PSR for details
on how to control this bit.
This bit can only be set to 1 if NISTER.CMDC is set to 1. An interrupt can only be generated if
NISIER.CMDC is set to 1.
Writing this bit to 1 clears this bit.
The table below shows that Command Timeout Error (CMDTEO) has a higher priority than Command
Complete (CMDC). If both bits are set to 1, it can be considered that the response was not received
correctly.

 CMDC                 CMDTEO       Meaning of the status
 0                    0            Interrupted by another factor
 Don’t care           1            Response not received within 64 SDCLK cycles
 1                    0            Response received

 Value        Description
 0            No command complete
 1            Command complete




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1350
                                                                SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.18 Error Interrupt Status Register

            Name:        EISTR
            Offset:      0x32
            Reset:       0x0000
            Property:    -


      Bit        15            14            13            12            11           10             9             8
                                                        BOOTAE                                     ADMA         ACMD
   Access                                                 R/W                                      R/W           R/W
    Reset                                                  0                                         0             0


      Bit         7             6             5            4             3             2             1             0
               CURLIM       DATEND         DATCRC       DATTEO        CMDIDX       CMDEND        CMDCRC        CMDTEO
   Access        R/W          R/W           R/W           R/W           R/W           R/W          R/W           R/W
    Reset         0             0             0            0             0             0             0             0


            Bit 12 – BOOTAE Boot Acknowledge Error
            Note: This register entry is specific to the e.MMC operation mode.
            This bit is set to 1 when detecting that the e.MMC Boot Acknowledge Status has a value other than “010”.
            This bit can only be set to 1 if EISTER.BOOTAE is set to 1. An interrupt can only be generated if
            EISIER.BOOTAE is set to 1.
            Writing this bit to 1 clears this bit.
             Value        Description
             0            No error
             1            Error

            Bit 9 – ADMA ADMA Error
            This bit is set to 1 when the peripheral detects errors during an ADMA-based data transfer. The state of
            the ADMA at an error occurrence is saved in AESR.
            In addition, the peripheral rises this status bit when it detects some invalid description data (Valid=0) at
            the ST_FDS state (refer to section “Advanced DMA” in the “SD Host Controller Simplified Specification
            V3.00”. ADMA Error Status (ERRST) in AESR indicates that an error occurs in ST_FDS state. The user
            may find that the Valid bit is not set at the error descriptor.
            This bit can only be set to 1 if EISTER.ADMA is set to 1. An interrupt can only be generated if
            EISIER.ADMA is set to 1.
            Writing this bit to 1 clears this bit.
             Value        Description
             0            No error
             1            Error

            Bit 8 – ACMD Auto CMD Error
            Auto CMD12 and Auto CMD23 use this error status. This bit is set to 1 when detecting that one of the 0 to
            4 bits in AESR (ACESR[4:0]) has changed from 0 to 1. In the case of Auto CMD12, this bit is set to 1, not
            only when errors occur in Auto CMD12, but also when Auto CMD12 is not executed due to the previous
            command error.
            This bit can only be set to 1 if EISTER.ACMD is set to 1. An interrupt can only be generated if
            EISIER.ACMD is set to 1.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1351
                                                   SAM D5x/E5x Family Data Sheet
                                                                          SD/MMC Host Controller ...

Writing this bit to 1 clears this bit.
Value        Description
0            No error
1            Error

Bit 7 – CURLIM Current Limit Error
By setting SD Bus Power (SDBPWR) in PCR, the peripheral is requested to supply power for the SD Bus.
The peripheral is protected from an illegal card by stopping power supply to the card, in which case this
bit indicates a failure status. Reading 1 means the peripheral is not supplying power to the card due to
some failure. Reading 0 means that the peripheral is supplying power and no error has occurred. The
peripheral may require some sampling time to detect the current limit.
This bit can only be set to 1 if EISTER.CURLIM is set to 1. An interrupt can only be generated if
EISIER.CURLIM is set to 1.
Writing this bit to 1 clears this bit.
 Value       Description
 0           No error
 1           Error

Bit 6 – DATEND Data End Bit Error
This bit is set to 1 either when detecting 0 at the end bit position of read data which uses the DAT line or
at the end bit position of the CRC Status.
This bit can only be set to 1 if EISTER.DATEND is set to 1. An interrupt can only be generated if
EISIER.DATEND is set to 1.
Writing this bit to 1 clears this bit.
 Value        Description
 0            No error
 1            Error

Bit 5 – DATCRC Data CRC Error
This bit is set to 1 when detecting a CRC error during a transfer of read data which uses the DAT line or
when detecting that the Write CRC Status has a value other than '010'.
This bit can only be set to 1 if EISTER. DATCRC is set to 1. An interrupt can only be generated if EISIER.
DATCRC is set to 1.
Writing this bit to 1 clears this bit.
 Value        Description
 0            No error
 1            Error

Bit 4 – DATTEO Data Timeout error
This bit is set to 1 when detecting one of following timeout conditions:
 • Busy timeout for R1b, R5b response type (see “Physical Layer Simplified Specification V3.01” and
     “SDIO Simplified Specification V3.00” ).
 • Busy timeout after Write CRC Status.
 • Write CRC Status timeout.
 • Read data timeout.
This bit can only be set to 1 if EISTER.DATTEO is set to 1. An interrupt can only be generated if
EISIER.DATTEO is set to 1.
Writing this bit to 1 clears this bit.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1352
                                                  SAM D5x/E5x Family Data Sheet
                                                                        SD/MMC Host Controller ...

 Value        Description
 0            No error
 1            Error

Bit 3 – CMDIDX Command Index Error
This bit is set to 1 if a Command Index error occurs in the command response.
This bit can only be set to 1 if EISTER.CMDIDX is set to 1. An interrupt can only be generated if
EISIER.CMDIDX is set to 1.
Writing this bit to 1 clears this bit.
 Value        Description
 0            No error
 1            Error

Bit 2 – CMDEND Command End Bit Error
This bit is set to 1 when detecting that the end bit of a command response is 0.
This bit can only be set to 1 if EISTER.CMDEND is set to 1. An interrupt can only be generated if
EISIER.CMDEND is set to 1.
Writing this bit to 1 clears this bit.
 Value        Description
 0            No error
 1            Error

Bit 1 – CMDCRC Command CRC Error
The Command CRC Error is generated in two cases.
If a response is returned and Command Timeout Error (CMDTEO) is set to 0 (indicating no command
timeout), this bit is set to 1 when detecting a CRC error in the command response.
The peripheral detects a CMD line conflict by monitoring the CMD line when a command is issued. If the
peripheral drives the CMD line to 1 level, but detects 0 level on the CMD line at the next SDCLK edge,
then the peripheral aborts the command (stops driving the CMD line) and sets this bit to 1. CMDTEO is
also set to 1 to indicate a CMD line conflict (refer to Table 40-2).
This bit can only be set to 1 if EISTER.CMDCRC is set to 1. An interrupt can only be generated if
EISIER.CMDCRC is set to 1.
Writing this bit to 1 clears this bit.

Bit 0 – CMDTEO Command Timeout Error
This bit is set to 1 only if no response is returned within 64 SDCLK cycles from the end bit of the
command. If the peripheral detects a CMD line conflict, in which case Command CRC Error (CMDCRC)
is also set to 1 (refer to Table 40-2), this bit is set without waiting for 64 SDCLK cycles because the
command is aborted by the peripheral.
This bit can only be set to 1 if EISTER.CMDTEO is set to 1. An interrupt can only be generated if
EISIER.CMDTEO is set to 1.
Writing this bit to 1 clears this bit.
Table 40-2. CMD Error Types

 CMDCRC                        CMDTEO              Types of error
 0                             0                   No error
 0                             1                   Response timeout error
 1                             0                   Response CRC error




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1353
                                        SAM D5x/E5x Family Data Sheet
                                                            SD/MMC Host Controller ...

...........continued
 CMDCRC                        CMDTEO   Types of error
 1                             1        CMD line conflict




© 2019 Microchip Technology Inc.        Datasheet                    DS60001507E-page 1354
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                        SD/MMC Host Controller ...

40.8.19 Normal Interrupt Status Enable Register: e.MMC

            Name:        NISTER
            Offset:      0x34
            Reset:       0x0000
            Property:    -


      Bit        15             14            13            12            11            10             9             8
                             BOOTAR                                                                                CINT
  Access                       R/W                                                                                  R/W
   Reset                        0                                                                                    0


      Bit         7             6             5             4              3             2             1             0
                CREM          CINS         BRDRDY        BWRRDY        DMAINT         BLKGE          TRFC          CMDC
  Access         R/W           R/W           R/W           R/W           R/W           R/W            R/W           R/W
   Reset          0             0             0             0              0             0             0             0


            Bit 14 – BOOTAR Boot Acknowledge Received Status Enable
            Note: This register entry is specific to the e.MMC operation mode.
            Value       Name                 Description
            0           MASKED               The BOOTAR status flag in NISTR is masked.
            1           ENABLED              The BOOTAR status flag in NISTR is enabled.

            Bit 8 – CINT Card Interrupt Status Enable
            If this bit is set to 0, the peripheral clears interrupt requests to the system. The Card Interrupt detection is
            stopped when this bit is cleared and restarted when this bit is set to 1. The user may clear this bit before
            servicing the Card Interrupt and may set this bit again after all interrupt requests from the card are
            cleared to prevent inadvertent interrupts.
             Value          Name                 Description
             0              MASKED               The CINT status flag in NISTR is masked.
             1              ENABLED              The CINT status flag in NISTR is enabled.

            Bit 7 – CREM Card Removal Status Enable
            Value      Name            Description
            0          MASKED          The CREM status flag in NISTR is masked.
            1          ENABLED         The CREM status flag in NISTR is enabled.

            Bit 6 – CINS Card Insertion Status Enable
            Value      Name                Description
            0          MASKED              The CINS status flag in NISTR is masked.
            1          ENABLED             The CINS status flag in NISTR is enabled.

            Bit 5 – BRDRDY Buffer Read Ready Status Enable
            Value      Name            Description
            0          MASKED          The BRDRDY status flag in NISTR is masked.
            1          ENABLED         The BRDRDY status flag in NISTR is enabled.

            Bit 4 – BWRRDY Buffer Write Ready Status Enable




        © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 1355
                                                    SAM D5x/E5x Family Data Sheet
                                                                        SD/MMC Host Controller ...

 Value        Name                 Description
 0            MASKED               The BWRRDY status flag in NISTR is masked.
 1            ENABLED              The BWRRDY status flag in NISTR is enabled.

Bit 3 – DMAINT DMA Interrupt Status Enable
Value      Name             Description
0          MASKED           The DMAINT status flag in NISTR is masked.
1          ENABLED          The DMAINT status flag in NISTR is enabled.

Bit 2 – BLKGE Block Gap Event Status Enable
Value      Name            Description
0          MASKED          The BLKGE status flag in NISTR is masked.
1          ENABLED         The BLKGE status flag in NISTR is enabled.

Bit 1 – TRFC Transfer Complete Status Enable
Value      Name              Description
0          MASKED            The TRFC status flag in NISTR is masked.
1          ENABLED           The TRFC status flag in NISTR is enabled.

Bit 0 – CMDC Command Complete Status Enable
Value      Name          Description
0          MASKED        The CMDC status flag in NISTR is masked.
1          ENABLED       The CMDC status flag in NISTR is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                   DS60001507E-page 1356
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   SD/MMC Host Controller ...

40.8.20 Error Interrupt Status Enable Register

            Name:       EISTER
            Offset:     0x36
            Reset:      0x0000
            Property:   -


      Bit        15           14             13          12          11            10        9           8
                                                      BOOTAE                               ADMA        ACMD
  Access                                                R/W                                 R/W         R/W
    Reset                                                0                                   0           0


      Bit        7             6             5           4            3            2         1           0
               CURLIM      DATEND          DATCRC     DATTEO       CMDIDX        CMDEND   CMDCRC      CMDTEO
  Access        R/W          R/W            R/W         R/W         R/W           R/W       R/W         R/W
    Reset        0             0             0           0            0            0         0           0


            Bit 12 – BOOTAE Boot Acknowledge Error Status Enable
            Note: This register entry is specific to the e.MMC operation mode.
            Value       Name                Description
            0           MASKED              The BOOTAE status flag in EISTR is masked.
            1           ENABLED             The BOOTAE status flag in EISTR is enabled.

            Bit 9 – ADMA ADMA Error Status Enable
            Value      Name             Description
            0          MASKED           The ADMA status flag in EISTR is masked.
            1          ENABLED          The ADMA status flag in EISTR is enabled.

            Bit 8 – ACMD Auto CMD Error Status Enable
            Value      Name             Description
            0          MASKED           The ACMD status flag in EISTR is masked.
            1          ENABLED          The ACMD status flag in EISTR is enabled.

            Bit 7 – CURLIM Current Limit Error Status Enable
            Value      Name              Description
            0          MASKED            The CURLIM status flag in EISTR is masked.
            1          ENABLED           The CURLIM status flag in EISTR is enabled.

            Bit 6 – DATEND Data End Bit Error Status Enable
            Value      Name             Description
            0          MASKED           The DATEND status flag in EISTR is masked.
            1          ENABLED          The DATEND status flag in EISTR is enabled.

            Bit 5 – DATCRC Data CRC Error Status Enable
            Value      Name           Description
            0          MASKED         The DATCRC status flag in EISTR is masked.
            1          ENABLED        The DATCRC status flag in EISTR is enabled.




        © 2019 Microchip Technology Inc.                       Datasheet                    DS60001507E-page 1357
                                            SAM D5x/E5x Family Data Sheet
                                                                 SD/MMC Host Controller ...

Bit 4 – DATTEO Data Timeout Error Status Enable
Value      Name            Description
0          MASKED          The DATTEO status flag in EISTR is masked.
1          ENABLED         The DATTEO status flag in EISTR is enabled.

Bit 3 – CMDIDX Command Index Error Status Enable
Value      Name           Description
0          MASKED         The CMDIDX status flag in EISTR is masked.
1          ENABLED        The CMDIDX status flag in EISTR is enabled.

Bit 2 – CMDEND Command End Bit Error Status Enable
Value      Name         Description
0          MASKED       The CMDEND status flag in EISTR is masked.
1          ENABLED      The CMDEND status flag in EISTR is enabled.

Bit 1 – CMDCRC Command CRC Error Status Enable
Value      Name         Description
0          MASKED       The CMDCRC status flag in EISTR is masked.
1          ENABLED      The CMDCRC status flag in EISTR is enabled.

Bit 0 – CMDTEO Command Timeout Error Status Enable
Value      Name         Description
0          MASKED        The CMDTEO status flag in EISTR is masked.
1          ENABLED       The CMDTEO status flag in EISTR is enabled.




© 2019 Microchip Technology Inc.              Datasheet                   DS60001507E-page 1358
                                                               SAM D5x/E5x Family Data Sheet
                                                                                   SD/MMC Host Controller ...

40.8.21 Normal Interrupt Signal Enable Register

            Name:       NISIER
            Offset:     0x38
            Reset:      0x0000
            Property:   -


      Bit        15           14              13          12          11           10             9           8
                            BOOTAR                                                                           CINT
  Access                      R/W                                                                            R/W
   Reset                       0                                                                              0


      Bit         7            6              5           4            3           2              1           0
               CREM          CINS          BRDRDY      BWRRDY       DMAINT       BLKGE         TRFC         CMDC
  Access        R/W           R/W            R/W         R/W          R/W         R/W            R/W         R/W
   Reset          0            0              0           0            0           0              0           0


            Bit 14 – BOOTAR Boot Acknowledge Received Signal Enable
            Note: This register entry is specific to the e.MMC operation mode.
            Value       Name               Description
            0           MASKED             No interrupt is generated when NISTR.BOOTAR is set.
            1           ENABLED            An interrupt is generated when NISTR.BOOTAR is set.

            Bit 8 – CINT Card Interrupt Signal Enable
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            Value       Name               Description
            0           MASKED             No interrupt is generated when NISTR.CINT is set.
            1           ENABLED            An interrupt is generated when NISTR.CINT is set.

            Bit 7 – CREM Card Removal Signal Enable
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            Value       Name               Description
            0           MASKED             No interrupt is generated when NISTR.CREM is set.
            1           ENABLED            An interrupt is generated when NISTR.CREM is set.

            Bit 6 – CINS Card Insertion Signal Enable
            Note:
            This register entry is specific to the SD/SDIO operation mode.
            Value       Name               Description
            0           MASKED             No interrupt is generated when NISTR.CINS is set.
            1           ENABLED            An interrupt is generated when NISTR.CINS is set.

            Bit 5 – BRDRDY Buffer Read Ready Signal Enable
            Value      Name          Description
            0          MASKED        No interrupt is generated when NISTR.BRDRDY is set.




        © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1359
                                                      SAM D5x/E5x Family Data Sheet
                                                                           SD/MMC Host Controller ...

 Value        Name                 Description
 1            ENABLED              An interrupt is generated when NISTR.BRDRDY is set.

Bit 4 – BWRRDY Buffer Write Ready Signal Enable
Value     Name          Description
0          MASKED        No interrupt is generated when NISTR.BWRRDY is set.
1          ENABLED       An interrupt is generated when NISTR.BWRRDY is set.

Bit 3 – DMAINT DMA Interrupt Signal Enable
Value      Name          Description
0          MASKED        No interrupt is generated when NISTR.DMAINT is set.
1          ENABLED       An interrupt is generated when NISTR.DMAINT is set.

Bit 2 – BLKGE Block Gap Event Signal Enable
Value      Name          Description
0          MASKED        No interrupt is generated when NISTR.BLKGE is set.
1          ENABLED       An interrupt is generated when NISTR.BLKGE is set.

Bit 1 – TRFC Transfer Complete Signal Enable
Value      Name           Description
0          MASKED         No interrupt is generated when NISTR.TRFC is set.
1          ENABLED        An interrupt is generated when NISTR.TRFC is set.

Bit 0 – CMDC Command Complete Signal Enable
Value      Name        Description
0          MASKED      No interrupt is generated when NISTR.CMDC is set.
1          ENABLED     An interrupt is generated when NISTR.CMDC is set.




© 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1360
                                                               SAM D5x/E5x Family Data Sheet
                                                                                   SD/MMC Host Controller ...

40.8.22 Error Interrupt Signal Enable Register

            Name:       EISIER
            Offset:     0x3A
            Reset:      0x0000
            Property:   -


      Bit        15           14              13          12           11          10             9           8
                                                       BOOTAE                                ADMA           ACMD
   Access                                                R/W                                     R/W         R/W
    Reset                                                 0                                       0           0


      Bit        7             6              5           4            3           2              1           0
               CURLIM      DATEND          DATCRC       DATTEO       CMDIDX      CMDEND     CMDCRC         CMDTEO
   Access       R/W          R/W             R/W         R/W          R/W         R/W            R/W         R/W
    Reset        0             0              0           0            0           0              0           0


            Bit 12 – BOOTAE Boot Acknowledge Error Signal Enable
            Note: This register entry is specific to the e.MMC operation mode.
            Value       Name               Description
            0           MASKED             No interrupt is generated when EISTR.BOOTAE is set.
            1           ENABLED            An interrupt is generated when EISTR.BOOTAE is set.

            Bit 9 – ADMA ADMA Error Signal Enable
            Value      Name          Description
            0          MASKED        No interrupt is generated when EISTR.ADMA is set.
            1          ENABLED       An interrupt is generated when EISTR.ADMA is set.

            Bit 8 – ACMD Auto CMD Error Signal Enable
            Value      Name          Description
            0          MASKED        No interrupt is generated when EISTR.ACMD is set.
            1          ENABLED       An interrupt is generated when EISTR.ACMD is set.

            Bit 7 – CURLIM Current Limit Error Signal Enable
            Value      Name           Description
            0          MASKED         No interrupt is generated when EISTR.CURLIM is set.
            1          ENABLED        An interrupt is generated when EISTR.CURLIM is set.

            Bit 6 – DATEND Data End Bit Error Signal Enable
            Value      Name          Description
            0          MASKED        No interrupt is generated when EISTR.DATEND is set.
            1          ENABLED       An interrupt is generated when EISTR.DATEND is set.

            Bit 5 – DATCRC Data CRC Error Signal Enable
            Value      Name         Description
            0          MASKED       No interrupt is generated when EISTR.DATCRC is set.
            1          ENABLED      An interrupt is generated when EISTR.DATCRC is set.




        © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1361
                                             SAM D5x/E5x Family Data Sheet
                                                                 SD/MMC Host Controller ...

Bit 4 – DATTEO Data Timeout Error Signal Enable
Value      Name          Description
0          MASKED        No interrupt is generated when EISTR.DATTEO is set.
1          ENABLED       An interrupt is generated when EISTR.DATTEO is set.

Bit 3 – CMDIDX Command Index Error Signal Enable
Value      Name        Description
0          MASKED      No interrupt is generated when EISTR.CMDIDX is set.
1          ENABLED     An interrupt is generated when EISTR.CMDIDX is set.

Bit 2 – CMDEND Command End Bit Error Signal Enable
Value      Name       Description
0          MASKED     No interrupt is generated when EISTR.CMDEND is set.
1          ENABLED    An interrupt is generated when EISTR.CMDEND is set.

Bit 1 – CMDCRC Command CRC Error Signal Enable
Value      Name       Description
0          MASKED     No interrupt is generated when EISTR.CMDCRC is set.
1          ENABLED    An interrupt is generated when EISTR.CMDCRC is set.

Bit 0 – CMDTEO Command Timeout Error Signal Enable
Value      Name       Description
0          MASKED     No interrupt is generated when EISTR.CMDTEO is set.
1          ENABLED    An interrupt is generated when EISTR.CMDTEO is set.




© 2019 Microchip Technology Inc.              Datasheet                        DS60001507E-page 1362
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.23 Auto CMD Error Status Register

            Name:       ACESR
            Offset:     0x3C
            Reset:      0x0000
            Property:   -


      Bit        15            14              13         12           11           10              9           8


  Access
   Reset


      Bit         7            6               5          4             3            2              1           0
                CMDNI                                 ACMDIDX      ACMDEND       ACMDCRC         ACMDTEO    ACMD12NE
  Access          R                                       R            R             R             R            R
   Reset          0                                       0             0            0              0           0


            Bit 7 – CMDNI Command Not Issued by Auto CMD12 Error
            Setting this bit to 1 means CMD_wo_DAT is not executed due to an Auto CMD12 error (ACESR[4:1]).
            This bit is set to 0 when Auto CMD Error is generated by Auto CMD23.
             Value        Description
             0            No error
             1            Error

            Bit 4 – ACMDIDX Auto CMD Index Error
            This bit is set to 1 when the Command Index error occurs in response to a command.
             Value        Description
             0            No error
             1            Error

            Bit 3 – ACMDEND Auto CMD End Bit Error
            This bit is set to 1 when detecting that the end bit of the command response is 0.
             Value        Description
             0            No error
             1            Error

            Bit 2 – ACMDCRC Auto CMD CRC Error
            This bit is set to 1 when detecting a CRC error in the command response (refer to Table 1-7 for more
            details).

            Bit 1 – ACMDTEO Auto CMD Timeout Error
            This bit is set to 1 if no response is returned within 64 SDCLK cycles from the end bit of the command. If
            this bit is set to 1, the other error status bits (ACESR[4:2]) are meaningless.

            ACMDCRC                        ACMDTEO                Types of error
            0                              0                      No error
            0                              1                      Response Timeout error




        © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1363
                                                  SAM D5x/E5x Family Data Sheet
                                                                          SD/MMC Host Controller ...

...........continued
 ACMDCRC                           ACMDTEO            Types of error
 1                                 0                  Response CRC error
 1                                 1                  CMD line conflict

Bit 0 – ACMD12NE Auto CMD12 Not Executed
If a memory multiple block data transfer is not started due to a command error, this bit is not set to 1
because it is not necessary to issue Auto CMD12. Setting this bit to 1 means the peripheral cannot issue
Auto CMD12 to stop a memory multiple block data transfer due to some error. If this bit is set to 1, other
error status bits (ACESR[4:1]) are meaningless.
This bit is set to 0 when an Auto CMD error is generated by Auto CMD23.
 Value        Description
 0            No error
 1            Error




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1364
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.24 Host Control 2 Register: e.MMC

            Name:        HC2R - EMMC
            Offset:      0x3E
            Reset:       0x0000
            Property:    -

            Note: The content of the HC2R register is depending on the mode. This description is for e.MMC mode.
            For SD/SDIO mode, see 40.8.25 HC2R - DEFAULT.

      Bit        15            14           13                 12         11         10                  9        8
               PVALEN
  Access        R/W
   Reset          0


      Bit         7            6             5                 4          3           2                  1        0
              SCLKSEL        EXTUN               DRVSEL[1:0]                              HS200EN[3:0]
  Access        R/W           R/W           R/W            R/W           R/W        R/W              R/W         R/W
   Reset          0            0             0                 0          0           0                  0        0


            Bit 15 – PVALEN Preset Value Enable
            As the operating SDCLK frequency depends on the system implementation, it is difficult to determine
            these parameters in the standard host driver. When Preset Value Enable (PVALEN) is set to 1, automatic
            SDCLK frequency generationis performed without considering system-specific conditions. This bit
            enables the functions defined in PVR.
            If this bit is written to 0, the Clock Generator Select bit (CCR.CLKGSEL) and the SDCLK Frequency
            Select bit (CCR.SDCLKFSEL) in the Clock Control Register (CCR) are selected by the user.
            If this bit is set to 1, CCR.SDCLKFSEL and .CLKGSEL and HC2R.DRVSEL are set by the peripheral as
            specified in the Preset Value Register (PVR).
             Value          Description
             0              CCR.SDCLK, CCR.SDCLKFSEL controlled by the user.
             1              Automatic selection by Preset Value is enabled.

            Bit 7 – SCLKSEL Sampling Clock Select
            The peripheral uses this bit to select the sampling clock to receive CMD and DAT.
            This bit is set by the tuning procedure and is valid after completion of tuning (when EXTUN is cleared).
            Setting 1 means that tuning is completed successfully and setting 0 means that tuning has failed.
            Writing 1 to this bit is meaningless and ignored. A tuning circuit is reset by writing to 0. This bit can be
            cleared by setting EXTUN to 1. Once the tuning circuit is reset, it takes time to complete a tuning
            sequence. Therefore, the user should keep this bit to 1 to perform a re-tuning sequence to complete a re-
            tuning sequence in a short time. Changing this bit is not allowed while the peripheral is receiving a
            response or a read data block. Refer to Figure 2.29 in the “SD Host Controller Simplified Specification
            V3.00” .
             Value        Description
             0            The fixed clock is used to sample data.
             1            The tuned clock is used to sample data.




        © 2019 Microchip Technology Inc.                            Datasheet                        DS60001507E-page 1365
                                                     SAM D5x/E5x Family Data Sheet
                                                                             SD/MMC Host Controller ...

Bit 6 – EXTUN Execute Tuning
This bit is set to 1 to start the tuning procedure and is automatically cleared when the tuning procedure is
completed. The result of tuning is indicated to Sampling Clock Select (SCLKSEL). The tuning procedure
is aborted by writing 0. Refer to Figure 2.29 in the “SD Host Controller Simplified Specification V3.00” .
 Value        Description
 0            Not tuned or tuning completed
 1            Execute tuning

Bits 5:4 – DRVSEL[1:0] Driver Strength Select
The peripheral output driver in 1.8V signaling is selected by this bit. In 3.3V signaling, this field is not
effective. This field can be set according to the Driver Type A, C and D support bits in CA1R.
This field depends on setting of Preset Value Enable (PVALEN):
  • PVALEN=0 - This field is set by the user.
  • PVALEN=1 - This field is automatically set by a value specified in one of the PVRx.
 Value        Name                 Description
 0            TYPEB                Driver Type B is selected (Default)
 1            TYPEA                Driver Type A is selected
 2            TYPEC                Driver Type C is selected
 3            TYPED                Driver Type D is selected

Bits 3:0 – HS200EN[3:0] HS200 Mode Enable
This field is used to select the e.MMC HS200 mode. When HS200EN is set to B(hexa), the HS200 mode is
enabled. Any other value except 0 is forbidden when interfacing an e.MMC device.
If Preset Value Enable is set to 1, peripheral sets SDCLK Frequency Select (SDCLKFSEL), Clock
Generator Select (CLKGSEL) in CCR and Driver Strength Select (DRVSEL) according to PVR. In this
case, one of the preset value registers is selected by this field. The user needs to reset SD Clock Enable
(SDCLKEN) before changing this field to avoid generating a clock glitch. After setting this field, the user
sets SDCLKEN to 1 again.
Note: This field is effective only if MC1R.DDR is written to 0.




© 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1366
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                      SD/MMC Host Controller ...

40.8.25 Host Control 2 Register: SD/SDIO

            Name:        HC2R - DEFAULT
            Offset:      0x3E
            Reset:       0x0000
            Property:    -

            Note: The content of the HC2R register is depending on the mode. This description is for SD/SDIO
            mode. For e.MMC mode, see 40.8.24 HC2R - EMMC.

      Bit        15            14            13                 12         11        10             9            8
               PVALEN       ASINTEN
  Access         R/W          R/W
   Reset          0            0


      Bit         7            6             5                  4          3          2             1            0
              SCLKSEL        EXTUN                DRVSEL[1:0]            VS18EN                UHSMS[2:0]
  Access         R/W          R/W           R/W             R/W           R/W        R/W          R/W           R/W
   Reset          0            0             0                  0          0          0             0            0


            Bit 15 – PVALEN Preset Value Enable
            As the operating SDCLK frequency depends on the system implementation, it is difficult to determine
            these parameters in the standard host driver. When Preset Value Enable (PVALEN) is set to 1, automatic
            SDCLK frequency generationis performed without considering system-specific conditions. This bit
            enables the functions defined in PVR.
            If this bit is written to 0, the Clock Generator Select bit (CCR.CLKGSEL) and the SDCLK Frequency
            Select bit (CCR.SDCLKFSEL) in the Clock Control Register (CCR) are selected by the user.
            If this bit is set to 1, CCR.SDCLKFSEL and .CLKGSEL and HC2R.DRVSEL are set by the peripheral as
            specified in the Preset Value Register (PVR).
             Value          Description
             0              CCR.SDCLK, CCR.SDCLKFSEL controlled by the user.
             1              Automatic selection by Preset Value is enabled.

            Bit 14 – ASINTEN Asynchronous Interrupt Enable
            This bit can be set to 1 if a card support asynchronous interrupts and Asynchronous Interrupt Support
            (ASINTSUP) is set to 1 in CA0R. Asynchronous interrupt is effective when DAT[1] interrupt is used in 4-bit
            SD mode. If this bit is set to 1, the user can stop the SDCLK during the asynchronous interrupt period to
            save power. During this period, the peripheral continues to deliver the Card Interrupt to the host when it is
            asserted by the card.
             Value       Description
             0           Disabled
             1           Enabled

            Bit 7 – SCLKSEL Sampling Clock Select
            The peripheral uses this bit to select the sampling clock to receive CMD and DAT.
            This bit is set by the tuning procedure and is valid after completion of tuning (when EXTUN is cleared).
            Setting 1 means that tuning is completed successfully and setting 0 means that tuning has failed.
            Writing 1 to this bit is meaningless and ignored. A tuning circuit is reset by writing to 0. This bit can be
            cleared by setting EXTUN to 1. Once the tuning circuit is reset, it takes time to complete the tuning
            sequence. Therefore, the user should keep this bit to 1 to perform a re-tuning sequence to complete a re-




        © 2019 Microchip Technology Inc.                             Datasheet                     DS60001507E-page 1367
                                                     SAM D5x/E5x Family Data Sheet
                                                                             SD/MMC Host Controller ...

tuning sequence in a short time. Changing this bit is not allowed while the peripheral is receiving a
response or a read data block. Refer to Figure 2.29 in the “SD Host Controller Simplified Specification
V3.00” .
 Value     Description
 0         The fixed clock is used to sample data.
 1         The tuned clock is used to sample data.

Bit 6 – EXTUN Execute Tuning
This bit is set to 1 to start the tuning procedure and is automatically cleared when the tuning procedure is
completed. The result of tuning is indicated to Sampling Clock Select (SCLKSEL). The tuning procedure
is aborted by writing 0. Refer to Figure 2.29 in the “SD Host Controller Simplified Specification V3.00” .
 Value        Description
 0            Not tuned or tuning completed
 1            Execute tuning

Bits 5:4 – DRVSEL[1:0] Driver Strength Select
The peripheral output driver in 1.8V signaling is selected by this bit. In 3.3V signaling, this field is not
effective. This field can be set according to the Driver Type A, C and D support bits in CA1R.
This field depends on setting of Preset Value Enable (PVALEN):
  • PVALEN=0 - This field is set by the user.
  • PVALEN=1 - This field is automatically set by a value specified in one of the PVRx.
 Value        Name                 Description
 0            TYPEB                Driver Type B is selected (Default)
 1            TYPEA                Driver Type A is selected
 2            TYPEC                Driver Type C is selected
 3            TYPED                Driver Type D is selected

Bit 3 – VS18EN 1.8V Signaling Enable
This bit controls the voltage regulator for the I/O cell. 3.3V is supplied to the card regardless of the
signaling voltage.
Setting this bit from 0 to 1 starts changing the signal voltage from 3.3V to 1.8V. The 1.8V regulator output
must be stable within 5 ms.
Clearing this bit from 1 to 0 starts changing the signal voltage from 1.8V to 3.3V. The 3.3V regulator
output must be stable within 5ms.
The user can set this bit to 1 when the peripheral supports 1.8V signaling (one of the support bits is set to
1: SDR50SUP, SDR104SUP or DDR50SUP in CA1R) and the card or device supports UHS-I (S18A = 1.
Refer to “Bus Switch Voltage Switch Sequence in the “Physical Layer Simplified Specification V3.01” ).
 Value       Description
 0           3.3V signaling
 1           1.8V signaling

Bits 2:0 – UHSMS[2:0] UHS Mode Select
This field is used to select one of the UHS-I modes and is effective when 1.8V Signal Enable (VS18EN) is
set to 1.
If Preset Value Enable is set to 1, the peripheral sets SDCLK Frequency Select (SDCLKFSEL), Clock
Generator Select (CLKGSEL) in CCR and Driver Strength Select (DRVSEL) according to PVR. In this
case, one of the preset value registers is selected by this field. The user needs to reset SD Clock Enable
(SDCLKEN) before changing this field to avoid generating a clock glitch. After setting this field, the user
sets SDCLKEN to 1 again.




© 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1368
                                                       SAM D5x/E5x Family Data Sheet
                                                                               SD/MMC Host Controller ...

 Value        Name             Description
 0            SDR12            UHS SDR12 Mode
 1            SDR25            UHS SDR25 Mode
 2            SDR50            UHS SDR50 Mode
 3            SDR104           UHS SDR104 Mode
 4            DDR50            UHS DDR50 Mode
                               Note: This field is effective only if MC1R.DDR is set to 0.




© 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1369
                                                                SAM D5x/E5x Family Data Sheet
                                                                                        SD/MMC Host Controller ...

40.8.26 Capabilities 0 Register

            Name:         CA0R
            Offset:       0x40
            Reset:        0x27E80080
            Property:     -

            Note: The Capabilities 0 Register is not supposed to be written by the user.

      Bit        31                 30        29          28            27              26          25           24
                      SLTYPE[1:0]          ASINTSUP    SB64SUP                       V18VSUP    V30VSUP       V33VSUP
   Access        R/W            R/W          R/W          R/W                          R/W         R/W          R/W
    Reset         0                 0         1            0                                1       1             1


      Bit        23                 22        21          20            19              18          17           16
               SRSUP         SDMASUP        HSSUP                   ADMA2SUP          ED8SUP                  MAXBLKL
   Access        R/W            R/W          R/W                       R/W             R/W                      R/W
    Reset         1                 1         1                          1                  0                     0


      Bit        15                 14        13          12            11              10          9             8
                                                            BASECLKF[7:0]
   Access        R/W            R/W          R/W          R/W          R/W             R/W         R/W          R/W
    Reset         0                 0         0            0             0                  0       0             0


      Bit         7                 6         5            4             3                  2       1             0
              TEOCLKU                                                        TEOCLKF[5:0]
   Access        R/W                         R/W          R/W          R/W             R/W         R/W          R/W
    Reset         1                           0            0             0                  0       0             0


            Bits 31:30 – SLTYPE[1:0] Slot Type
            This field indicates usage of a slot by a specific system. An peripheral control register set is defined per
            slot.
            Embedded Slot for One Device means that only one non-removable device is connected to a bus slot.
            The Standard Host Driver controls a removable card (SLTYPE = 0) or one embedded device (SLTYPE =
            1) connected to an SD bus slot.
             Value       Name
             0           Removable Card Slot
             1           Embedded Slot for One Device
             2           Shared Bus Slot
             2           Reserved
             3           Reserved

            Bit 29 – ASINTSUP Asynchronous Interrupt Support
            Refer to section “Asynchronous Interrupt” in the “SDIO Simplified Specification V3.00”.
            Value       Description
            0           Asynchronous interrupt not supported
            1           Asynchronous interrupt supported




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1370
                                                   SAM D5x/E5x Family Data Sheet
                                                                          SD/MMC Host Controller ...

Bit 28 – SB64SUP 64-Bit System Bus Support
This bit indicates if the peripheral supports the 64-bit Address Descriptor mode and is connected to the
64-bit address system bus.
 Value       Description
 0            64-bit address bus not supported
 1            64-bit address bus supported

Bit 26 – V18VSUP Voltage Support 1.8V
Value      Description
0          1.8V Voltage supply not supported
1          1.8V Voltage supply supported

Bit 25 – V30VSUP Voltage Support 3.0V
Note: The signal and supply voltages of the peripheral are limited by the supply voltage of the device.
 Value        Description
 0            3.0V Voltage supply not supported
 1            3.0V Voltage supply supported

Bit 24 – V33VSUP Voltage Support 3.3V
Note: The signal and supply voltages of the peripheral are limited by the supply voltage of the device.
 Value        Description
 0            3.3V Voltage supply not supported
 1            3.3V Voltage supply supported

Bit 23 – SRSUP Suspend/Resume Support
This bit indicates whether the peripheral supports the Suspend/Resume functionality. If this bit is set to 0,
the user does not issue either Suspend or Resume commands because the Suspend and Resume
mechanism (refer to “Suspend and Resume Mechanism” in the “SD Host Controller Simplified
Specification V3.00” ) is not supported.
 Value       Description
 0            Suspend/Resume not supported
 1            Suspend/Resume supported

Bit 22 – SDMASUP SDMA Support
This bit indicates whether the peripheral is capable of using SDMA to transfer data between system
memory and the peripheral directly.
 Value       Description
 0            SDMA not supported
 1            SDMA supported

Bit 21 – HSSUP High Speed Support
This bit indicates whether the peripheral and the system support High Speed mode and they can supply
SDCLK frequency from 25MHz to 50MHz.
 Value       Description
 0            High Speed not supported
 1            High Speed supported




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1371
                                                 SAM D5x/E5x Family Data Sheet
                                                                        SD/MMC Host Controller ...

Bit 19 – ADMA2SUP ADMA2 Support
This bit indicates whether the peripheral is capable of using ADMA2.
 Value       Description
 0            ADMA2 not supported
 1            ADMA2 supported

Bit 18 – ED8SUP 8-Bit Support for Embedded Device
This bit indicates whether the peripheral is capable of using the 8-bit Bus Width mode.
 Value       Description
 0            8-bit bus width not supported
 1            8-bit bus width supported

Bit 16 – MAXBLKL Max Block Length
This field indicates the maximum block size that the user can read and write to the buffer in the
peripheral.
Note: For SD Memory Cards, the transfer block length is always 512 bytes, regardless of this field.
 Value        Name                             Description
 0            512                              512 bytes
 1            NONE                             Reserved

Bits 15:8 – BASECLKF[7:0] Base Clock Frequency
This value indicates the frequency of the base clock (BASECLK). The user uses this value to calculate
the clock divider value (refer to SDCLK Frequency Select (SDCLKFSEL) in CCR).
If this field is set to 0, the user must get the information via another method.
�BASECLK = BASECLKFMHz

Bit 7 – TEOCLKU Timeout Clock Unit
This bit shows the unit of the base clock frequency used to detect Data Timeout Error.
 Value      Description
 0          kHz
 1          MHz

Bits 5:0 – TEOCLKF[5:0] Timeout Clock Frequency
This bit shows the timeout clock frequency (TEOCLK) used to detect Data Timeout Error.
If this field is set to 0, the user must get the information via another method.
The Timeout Clock Unit (TEOCLKU) defines the unit of this field’s value.
– TEOCLKU = 0:
�TEOCLK = TEOCLKFKHz

– TEOCLKU = 1:
�TEOCLK = TEOCLKFMHz




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1372
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.27 Capabilities 1 Register

            Name:        CA1R
            Offset:      0x44
            Reset:       0x00000070
            Property:    -

            Note: The Capabilities 1 Register is not supposed to be written by the user.

      Bit        31            30            29            28             27          26                 25           24


   Access
    Reset


      Bit        23            22            21            20             19          18                 17           16
                                                               CLKMULT[7:0]
   Access        R/W          R/W            R/W          R/W            R/W          R/W            R/W             R/W
    Reset         0             0             0            0                  0        0                 0            0


      Bit        15            14            13            12             11          10                 9            8
                                           TSDR50                                          TCNTRT[3:0]
   Access                                    R/W                         R/W          R/W            R/W             R/W
    Reset                                     0                               0        0                 0            0


      Bit         7             6             5            4                  3        2                 1            0
                            DRVDSUP        DRVCSUP     DRVASUP                    DDR50SUP       SDR104SUP        SDR50SUP
   Access                     R/W            R/W          R/W                         R/W            R/W             R/W
    Reset                       0             0            0                           0                 0            0


            Bits 23:16 – CLKMULT[7:0] Clock Multiplier
            This field indicates the multiplier factor between the Base Clock (BASECLK) used for the Divided Clock
            Mode and the Multiplied Clock (MULTCLK) used for the Programmable Clock mode (refer to CCR).
            Reading this field to 0 means that the Programmable Clock mode is not supported.
            �MULTCLK = �BASECLK × CLKMULT+1

            Bit 13 – TSDR50 Use Tuning for SDR50
            If this bit is set to 1, the peripheral requires tuning to operate SDR50 (tuning is always required to operate
            SDR104).
             Value          Description
             0              SDR50 does not require tuning.
             1              SDR50 requires tuning.

            Bits 11:8 – TCNTRT[3:0] Timer Count For Re-Tuning
            This field indicates an initial value of the Re-Tuning Timer for Re-Tuning Mode (RTMODE) 1 to 3.
            Reading this field at 0 means that the Re-Tuning Timer is disabled. The Re-Tuning Timer initial value
            ranges from 0 to 1024 seconds.
            �TIMER = 2 TCNTRT+ − 1 Seconds

            Bit 6 – DRVDSUP Driver Type D Support




        © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 1373
                                                SAM D5x/E5x Family Data Sheet
                                                            SD/MMC Host Controller ...

 Value        Description
 0            Driver type D is not supported.

Bit 5 – DRVCSUP Driver Type C Support
Value      Description
0          Driver type C is not supported.

Bit 4 – DRVASUP Driver Type A Support
Value      Description
0          Driver type A is not supported.

Bit 2 – DDR50SUP DDR50 Support
Value      Description
0          DDR50 mode is not supported.

Bit 1 – SDR104SUP SDR104 Support
Value      Description
0          SDR104 mode is not supported.
1          SDR104 mode is supported.

Bit 0 – SDR50SUP SDR50 Support
Value      Description
0          SDR50 mode is not supported.
1          SDR50 mode is supported.




© 2019 Microchip Technology Inc.                Datasheet            DS60001507E-page 1374
                                                               SAM D5x/E5x Family Data Sheet
                                                                                      SD/MMC Host Controller ...

40.8.28 Maximum Current Capabilities Register

            Name:        MCCAR
            Offset:      0x48
            Reset:       0x00000000
            Property:    -


      Bit        31            30           29            28            27           26            25            24


  Access
   Reset


      Bit        23            22           21            20            19           18            17            16
                                                          MAXCUR18V[7:0]
  Access          R            R             R            R             R             R            R             R
   Reset          0            0             0             0            0             0            0             0


      Bit        15            14           13            12            11           10            9             8
                                                          MAXCUR30V[7:0]
  Access          R            R             R            R             R             R            R             R
   Reset          0            0             0             0            0             0            0             0


      Bit         7            6             5             4            3             2            1             0
                                                          MAXCUR33V[7:0]
  Access          R            R             R            R             R             R            R             R
   Reset          0            0             0             0            0             0            0             0


            Bits 23:16 – MAXCUR18V[7:0] Maximum Current for 1.8V
            This field indicates the maximum current capability for 1.8V voltage. This value is meaningful only if
            V18VSUP is set to 1 in CA0RCA1R. Reading MAXCUR18V at 0 means that the user must get
            information via another method.
            ImaxmA = 4 × MAXCURR18�

            Bits 15:8 – MAXCUR30V[7:0] Maximum Current for 3.0V
            This field indicates the maximum current capability for 3.0V voltage. This value is meaningful only if
            V30VSUP is set to 1 in CA0R. Reading MAXCUR30V at 0 means that the user must get information via
            another method.
            ImaxmA = 4 × MAXCURR30�

            Bits 7:0 – MAXCUR33V[7:0] Maximum Current for 3.3V
            This field indicates the maximum current capability for 3.3V voltage. This value is meaningful only if
            V33VSUP is set to 1 in CA0R. Reading MAXCUR33V at 0 means that the user must get information via
            another method.
            ImaxmA = 4 × MAXCURR33�




        © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1375
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.29 Force Event Register for Auto CMD Error Status

            Name:       FERACES
            Offset:     0x50
            Reset:      0x0000
            Property:   -


      Bit        15            14           13            12           11            10            9            8


  Access
   Reset


      Bit         7            6             5            4             3            2             1            0
               CMDNI                                  ACMDIDX      ACMDEND       ACMDCRC      ACMDTEO        ACMD12NE
  Access         W                                        W            W             W            W             W
   Reset          0                                       0             0            0             0            0


            Bit 7 – CMDNI Force Event for Command Not Issued by Auto CMD12 Error
            For testing purposes, the user can write this bit to 1 to rise the CMDNI status flag in ACESR.
            Writing this bit to 0 has no effect.

            Bit 4 – ACMDIDX Force Event for Auto CMD Index Error
            For testing purposes, the user can write this bit to 1 to rise the ACMDIDX status flag in ACESR.
            Writing this bit to 0 has no effect.

            Bit 3 – ACMDEND Force Event for Auto CMD End Bit Error
            For testing purposes, the user can write this bit to 1 to rise the ACMDEND status flag in ACESR.
            Writing this bit to 0 has no effect.

            Bit 2 – ACMDCRC Force Event for Auto CMD CRC Error
            For testing purposes, the user can write this bit to 1 to rise the ACMDCRC status flag in ACESR.
            Writing this bit to 0 has no effect.

            Bit 1 – ACMDTEO Force Event for Auto CMD Timeout Error
            For testing purposes, the user can write this bit to 1 to rise the ACMDTEO status flag in ACESR.
            Writing this bit to 0 has no effect.

            Bit 0 – ACMD12NE Force Event for Auto CMD12 Not Executed
            For testing purposes, the user can write this bit to 1 to rise the ACMD12NE status flag in ACESR.
            Writing this bit to 0 has no effect.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1376
                                                               SAM D5x/E5x Family Data Sheet
                                                                                      SD/MMC Host Controller ...

40.8.30 Force Event Register for Error Interrupt Status

            Name:        FEREIS
            Offset:      0x52
            Reset:       0x0000
            Property:    -


      Bit        15            14            13           12            11           10            9            8
                                                       BOOTAE                                    ADMA         ACMD
   Access                                                 W                                        W            W
    Reset                                                  0                                       0            0


      Bit         7            6             5             4            3             2            1            0
               CURLIM       DATEND         DATCRC      DATTEO        CMDIDX       CMDEND        CMDCRC        CMDTEO
   Access        W             W             W            W             W             W            W            W
    Reset         0            0             0             0            0             0            0            0


            Bit 12 – BOOTAE Force Event for Boot Acknowledge Error
            For testing purposes, the user can write this bit to 1 to rise the BOOTAE status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 9 – ADMA Force Event for ADMA Error
            For testing purposes, the user can write this bit to 1 to rise the ADMA status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 8 – ACMD Force Event for Auto CMD Error
            For testing purposes, the user can write this bit to 1 to rise the ACMD status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 7 – CURLIM Force Event for Current Limit Error
            For testing purposes, the user can write this bit to 1 to rise the CURLIM status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 6 – DATEND Force Event for Data End Bit Error
            For testing purposes, the user can write this bit to 1 to rise the DATEND status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 5 – DATCRC Force Event for Data CRC error
            For testing purposes, the user can write this bit to 1 to rise the DATCRC status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 4 – DATTEO Force Event for Data Timeout error
            For testing purposes, the user can write this bit to 1 to rise the DATTEO status flag in EISTR.
            Writing this bit to 0 has no effect.

            Bit 3 – CMDIDX Force Event for Command Index Error
            For testing purposes, the user can write this bit to 1 to rise the CMDIDX status flag in EISTR.
            Writing this bit to 0 has no effect.




        © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1377
                                                  SAM D5x/E5x Family Data Sheet
                                                                         SD/MMC Host Controller ...

Bit 2 – CMDEND Force Event for Command End Bit Error
For testing purposes, the user can write this bit to 1 to rise the CDMEND status flag in EISTR.
Writing this bit to 0 has no effect.

Bit 1 – CMDCRC Force Event for Command CRC Error
For testing purposes, the user can write this bit to 1 to rise the CMDCRC status flag in EISTR.
Writing this bit to 0 has no effect.

Bit 0 – CMDTEO Force Event for Command Timeout Error
For testing purposes, the user can write this bit to 1 to rise the CMDTEO status flag in EISTR.
Writing this bit to 0 has no effect.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1378
                                                            SAM D5x/E5x Family Data Sheet
                                                                                  SD/MMC Host Controller ...

40.8.31 ADMA Error Status Register

           Name:       AESR
           Offset:     0x54
           Reset:      0x00
           Property:   -


     Bit         7            6            5            4            3            2            1                0
                                                                                LMIS               ERRST[1:0]
  Access                                                                          R            R                R
   Reset                                                                          0            0                0


           Bit 2 – LMIS ADMA Length Mismatch Error
           This error occurs in the following two cases:
            • While Block Count Enable (BCEN) is being set, the total data length specified by the Descriptor table
                is different from that specified by the Block Count (BLKCNT) and Transfer Block Size (BLKSIZE).
            • The total data length cannot be divided by the Transfer Block Size (BLKSIZE).
           Value       Description
           0           No error
           1           Error

           Bits 1:0 – ERRST[1:0] ADMA Error State
           This field indicates the state of ADMA when an error has occurred during an ADMA data transfer. This
           field never indicates 2 because ADMA never stops in this state.
            Value       Name                            Description
            0x0         ST_STOP (Stop DMA)              Points to the descriptor following the error descriptor
            0x1         ST_FDS (Fetch Descriptor)       Points to the error descriptor
            0x2         -                               Reserved
            0x3         ST_TRF (Transfer Data)          Points to the descriptor following the error descriptor




       © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1379
                                                                SAM D5x/E5x Family Data Sheet
                                                                                    SD/MMC Host Controller ...

40.8.32 ADMA System Address Register

           Name:       ASAR
           Offset:     0x58
           Reset:      0x00000000
           Property:   -


     Bit        31            30           29            28                 27     26            25           24
                                                          ADMASA[31:24]
  Access       R/W           R/W          R/W           R/W             R/W        R/W          R/W           R/W
   Reset         0            0             0            0                  0       0            0             0


     Bit        23            22           21            20                 19     18            17           16
                                                          ADMASA[23:16]
  Access       R/W           R/W          R/W           R/W             R/W        R/W          R/W           R/W
   Reset         0            0             0            0                  0       0            0             0


     Bit        15            14           13            12                 11     10            9             8
                                                             ADMASA[15:8]
  Access       R/W           R/W          R/W           R/W             R/W        R/W          R/W           R/W
   Reset         0            0             0            0                  0       0            0             0


     Bit         7            6             5            4                  3       2            1             0
                                                              ADMASA[7:0]
  Access       R/W           R/W          R/W           R/W             R/W        R/W          R/W           R/W
   Reset         0            0             0            0                  0       0            0             0


           Bits 31:0 – ADMASA[31:0] ADMA System Address
           This field holds the byte address of the executing command of the descriptor table. At the start of ADMA,
           the user must set the start address of the descriptor table. The ADMA increments this register address,
           which points to the next Descriptor line to be fetched.
           When the ADMA Error (ADMA) status flag rises, this field holds a valid descriptor address depending on
           the ADMA Error State (ERRST). The user must program Descriptor Table on 32-bit boundary and set 32-
           bit boundary address to this register. ADMA2 ignores the lower 2 bits of this register and assumes it to be
           0.




       © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1380
                                                        SAM D5x/E5x Family Data Sheet
                                                                               SD/MMC Host Controller ...

40.8.33 Preset Value Register

        Name:         PVR
        Offset:       0x60 + n*0x02 [n=0..7]
        Reset:        0x0000
        Property:     Read/Write

        One of the Preset Value Registers is effective based on the selected bus speed mode. The table below
        defines the conditions to select one of the PVRs.
        Table 40-3. Preset Value Register Select Condition

         Selected Bus Speed Mode               VS18EN       HSEN                               UHSMS
                                               (HC2R)       (HC1R)                             (HC2R)

         Default Speed                         0            0                                  don’t care
         High Speed                            0            Response Timeout Error             don’t care
         Reserved                              1            don’t care                         Other values

        The following table shows the effective Preset Value Register according to the Selected Bus Speed
        mode.
        Table 40-4. Preset Value Registers

         PVRx            Selected Bus Speed Mode                                Signal Voltage
         PVR0            Initialization                                         3.3V or 1.8V
         PVR1            Default Speed                                          3.3V
         PVR2            High Speed                                             3.3V

        When Preset Value Enable (PVALEN) in HC2R is set to 1, SDCLK Frequency Select (SDLCKFSEL) and
        Clock Generator Select (CLKGSEL) in CCR are automatically set based on the Selected Bus Speed
        mode. This means that the user does not need to set these fields when preset is enabled. A Preset Value
        Register for Initialization (PVR0) is not selected by Bus Speed mode. Before starting the initialization
        sequence, the user needs to set a clock preset value to SDCLKFSEL in CCR. PVALEN can be set to 1
        after the initialization is completed.
        Note: Preset Values in PVRx registers are not supposed to be written by the user. However, the user
        can modify preset values only if Capabilities Write Enable (CAPWREN) is written to 1 in CACR.




       © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1381
                                                         SAM D5x/E5x Family Data Sheet
                                                                       SD/MMC Host Controller ...

   Bit       15            14           13         12           11     10        9            8
                                                                     CLKGSEL     SDCLKFSEL[9:8]
Access                                                                 R/W      R/W         R/W
 Reset                                                                  0        0            0


   Bit        7             6            5          4            3      2        1            0
                                                    SDCLKFSEL[7:0]
Access       R/W          R/W           R/W        R/W         R/W     R/W      R/W         R/W
 Reset        0             0            0          0            0      0        0            0


         Bit 10 – CLKGSEL Clock Generator Select
         Refer to CGGSEL in CCR.

         Bits 9:0 – SDCLKFSEL[9:0] SDCLK Frequency Select
         Refer to SDCLKFSEL in CCR.




     © 2019 Microchip Technology Inc.                    Datasheet              DS60001507E-page 1382
                                                              SAM D5x/E5x Family Data Sheet
                                                                                  SD/MMC Host Controller ...

40.8.34 Slot Interrupt Status Register

            Name:       SISR
            Offset:     0xFC
            Reset:      0x0000
            Property:   -


      Bit        15           14           13           12                 11     10            9            8


   Access
    Reset


      Bit         7            6            5            4                 3       2            1            0
                                                             INTSSL[7:0]
   Access        R             R           R            R                  R      R            R            R
    Reset         0            0            0            0                 0       0            0            0


            Bits 7:0 – INTSSL[7:0] Interrupt Signal for Each Slot
            These status bits indicate the logical OR of Interrupt Signals and WakeUp Signal for each peripheral
            instance in the device. INTSSL[x] corresponds to instance SDHCx. There are 2 instances in this device.




        © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1383
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   SD/MMC Host Controller ...

40.8.35 Host Controller Version Register

            Name:       HCVR
            Offset:     0xFE
            Reset:      0x1802
            Property:   -


      Bit        15           14           13            12               11       10            9            8
                                                              VVER[7:0]
  Access         R             R            R            R                R        R            R             R
   Reset          0            0            0            1                1        0             0            0


      Bit         7            6            5            4                3        2             1            0
                                                              SVER[7:0]
  Access         R             R            R            R                R        R            R             R
   Reset          0            0            0            0                0        0             1            0


            Bits 15:8 – VVER[7:0] Vendor Version Number
            Reserved. Value subject to change. No functionality associated.

            Bits 7:0 – SVER[7:0] Specification Version Number
            This status indicates the SD Host Controller Specification Version.
             Value       Name
             0           SD Host Specification Version 1.00
             1           SD Host Specification Version 2.00, including the feature of the ADMA and Test Register
             2           SD Host Specification Version 3.00




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1384
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.36 Additional Present State Register

            Name:       APSR
            Offset:     0x200
            Reset:      0x0000000F
            Property:   -


      Bit        31            30           29            28           27            26                 25           24


  Access
   Reset


      Bit        23            22           21            20           19            18                 17           16


  Access
   Reset


      Bit        15            14           13            12           11            10                 9            8


  Access
   Reset


      Bit         7            6             5            4             3            2                  1            0
                                                                                          HDATLL[3:0]
  Access                                                                R            R                  R            R
   Reset                                                                1            1                  1            1


            Bits 3:0 – HDATLL[3:0] High Line Level
            This status is used to check the DAT[7:4] line level to recover from errors, and for debugging.




        © 2019 Microchip Technology Inc.                        Datasheet                               DS60001507E-page 1385
                                                               SAM D5x/E5x Family Data Sheet
                                                                                  SD/MMC Host Controller ...

40.8.37 e.MMC Control 1 Register

            Name:       MC1R
            Offset:     0x204
            Reset:      0x00
            Property:   R/W


      Bit         7             6            5             4          3            2            1                 0
                FCD          RSTN          BOOTA        OPD         DDR                             CMDTYP[1:0]
  Access        R/W           R/W           R/W         R/W         R/W                       R/W             R/W
   Reset          0             0            0             0          0                         0                 0


            Bit 7 – FCD e.MMC Force Card Detect
            When using e.MMC, the user can set this bit to 1 to bypass the card detection procedure using the CD
            signal.
             Value     Name       Description
             0         DISABLED e.MMC Forced Card Detect is disabled. The CD signal is used and debounce
                                  timing is applied.
             1         ENABLED e.MMC Forced Card Detect is enabled.

            Bit 6 – RSTN e.MMC Reset Signal
            This bit controls the e.MMC reset signal.
             Value       Description
             0           Reset signal is inactive.
             1           Reset signal is active.

            Bit 5 – BOOTA e.MMC Boot Acknowledge Enable
            This bit must be set according to the value of BOOT_ACK in the Extended CSD Register (refer to
            “Embedded MultiMedia Card (e.MMC) Electrical Standard 4.51” ).
            When this bit is set to 1, the peripheral waits for boot acknowledge pattern from the e.MMC before
            receiving boot data.
            If the boot acknowledge pattern is wrong, the BOOTAE status flag rises in EISTR if BOOTAE is set in
            EISTER. An interrupt is generated if BOOTAE is set in EISIER.
            If the no boot acknowledge pattern is received, the DATTEO status flag rises in EISTR if DATTEO is set
            in EISTER. An interrupt is generated if DATTEO is set in EISIER.

            Bit 4 – OPD e.MMC Open Drain Mode
            This bit sets the command line in open drain.
             Value       Description
             0           The command line is in push-pull.
             1           The command line is in open drain.

            Bit 3 – DDR e.MMC HSDDR Mode
            This bit selects the High Speed DDR mode.
             Value       Description
             0           High Speed DDR is not selected.




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1386
                                                  SAM D5x/E5x Family Data Sheet
                                                                        SD/MMC Host Controller ...

 Value        Description
 1            High Speed DDR is selected.
              Note: The clock divider (DIV) in CCR must be set to a value different from 0 when HSEN is
              1.

Bits 1:0 – CMDTYP[1:0] e.MMC Command Type
Value       Name    Description
0           NORMAL The command is not an e.MMC specific command.
1           WAITIRQ This bit must be set to 1 when the e.MMC is in Interrupt mode (CMD40). Refer to
                    “Interrupt Mode” in the “Embedded MultiMedia Card (e.MMC) Electrical Standard
                    4.51” .
2           STREAM This bit must be set to 1 in the case of Stream Read(CMD11) or Stream Write
                    (CMD20). Only effective for e.MMC up to revision 4.41.
3           BOOT    Starts a Boot Operation mode at the next write to CR. Boot data are read directly
                    from e.MMC device.




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1387
                                                                SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.38 e.MMC Control 2 Register

            Name:        MC2R
            Offset:      0x205
            Reset:       0x00
            Property:    -


      Bit         7              6            5             4             3            2             1             0
                                                                                                   ABOOT         SRESP
  Access                                                                                             W             W
   Reset                                                                                             0             0


            Bit 1 – ABOOT e.MMC Abort Boot
            This bit is used to exit from Boot mode. Writing this bit to 1 exits the Boot Operation mode. Writing 0 is
            ignored.

            Bit 0 – SRESP e.MMC Abort Wait IRQ
            This bit is used to exit from the Interrupt mode. When this bit is written to 1, the peripheral sends the
            CMD40 response automatically. This brings the e.MMC from Interrupt mode to the standard Data
            Transfer mode. Writing this bit to 0 is ignored.
            Note: This bit is only effective when CMD_TYP in MC1R is set to WAITIRQ.




        © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1388
                                                           SAM D5x/E5x Family Data Sheet
                                                                                SD/MMC Host Controller ...

40.8.39 AHB Control Register

           Name:       ACR
           Offset:     0x208
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29          28          27            26       25                24


  Access
   Reset


     Bit        23           22           21          20          19            18       17                16


  Access
   Reset


     Bit        15           14           13          12          11            10        9                 8


  Access
   Reset


     Bit        7             6           5           4            3            2         1                 0
                                                                                               BMAX[1:0]
  Access                                                                                 R/W               R/W
   Reset                                                                                  0                 0


           Bits 1:0 – BMAX[1:0] AHB Maximum Burst
           This field selects the maximum burst size in case of DMA transfer.
            Value       Name             Description
            0           INCR16           The maximum burst size is INCR16.
            1           INCR8            The maximum burst size is INCR8.
            2           INCR4            The maximum burst size is INCR4.
            3           SINGLE           Only SINGLE transfers are performed.




       © 2019 Microchip Technology Inc.                    Datasheet                     DS60001507E-page 1389
                                                                SAM D5x/E5x Family Data Sheet
                                                                                       SD/MMC Host Controller ...

40.8.40 Clock Control 2 Register

            Name:        CC2R
            Offset:      0x20C
            Reset:       0x00000000
            Property:    -


      Bit        31            30            29            28            27           26            25            24


  Access
   Reset


      Bit        23            22            21            20            19           18            17            16


  Access
   Reset


      Bit        15            14            13            12            11           10             9             8


  Access
   Reset


      Bit         7             6             5            4             3             2             1             0
                                                                                                               FSDCLKD
  Access                                                                                                         R/W
   Reset                                                                                                           0


            Bit 0 – FSDCLKD Force SDCLK Disabled
            The user can choose to maintain the SDCLK during 8 SDCLK cycles after the end bit of the last data
            block in case of a read transaction, or after the end bit of the CRC status in case of a write transaction.
             Value      Description
             0          The SDCLK is forced and it cannot be stopped immediately after the transaction.
             1          The SDCLK is not forced and it can be stopped immediately after the transaction.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1390
                                                              SAM D5x/E5x Family Data Sheet
                                                                                     SD/MMC Host Controller ...

40.8.41 Capabilities Control Register

            Name:       CACR
            Offset:     0x230
            Reset:      0x00000000
            Property:   -


      Bit        31           30           29           28               27          26       25           24


  Access
   Reset


      Bit        23           22           21           20               19          18       17           16


  Access
   Reset


      Bit        15           14           13           12               11          10        9            8
                                                              KEY[7:0]
  Access        R/W          R/W           R/W          R/W              R/W         R/W      R/W          R/W
   Reset          0            0            0            0                0           0        0            0


      Bit         7            6            5            4                3           2        1            0
                                                                                                        CAPWREN
  Access                                                                                                   R/W
   Reset                                                                                                    0


            Bits 15:8 – KEY[7:0] Key
            Value       Name Description
            46h         KEY Writing any other value in this field aborts the write operation of the CAPWREN bit.
                               Always reads as 0.

            Bit 0 – CAPWREN Capabilities Write Enable
            This bit can only be written if KEY correspond to 46h.
             Value       Description
             0           Capabilities registers (CA0R and CA1R) cannot be written.
             1           Capabilities registers (CA0R and CA1R) can be written.




        © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1391
                                                         SAM D5x/E5x Family Data Sheet
                                                                            SD/MMC Host Controller ...

40.8.42 Debug Register

           Name:       DBGR
           Offset:     0x234
           Reset:      0x00
           Property:   -


     Bit        15           14           13        12          11          10          9            8


  Access
   Reset


     Bit        7              6          5         4           3           2           1            0
                                                                                                   NIDBG
  Access                                                                                            R/W
   Reset                                                                                             0


           Bit 0 – NIDBG Non-Intrusive Debug
           Value      Name        Description
           0          DISABLED Reading the BDPR via debugger increments the dual port RAM read pointer.
           1          ENABLED Reading the BDPR via debugger does not increment the dual port RAM read
                                  pointer.




       © 2019 Microchip Technology Inc.                  Datasheet                      DS60001507E-page 1392
