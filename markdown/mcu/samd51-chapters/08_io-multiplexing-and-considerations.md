# 6. I/O Multiplexing and Considerations

*Source: `Atmel-SAMD51.pdf`, pages 32-46 — SAMD51 family datasheet*

                                                                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                                                          I/O Multiplexing and Considerations


6.                             I/O Multiplexing and Considerations

6.1                            Multiplexed Signals
                               By default each pin is controlled by the PORT as a general purpose I/O, and alternatively it can be
                               assigned a different peripheral functions. To enable a peripheral function on a pin, the Peripheral
                               Multiplexer Enable bit in the Pin Configuration register corresponding to that pin (PINCFGn.PMUXEN, n =
                               0-31) in the PORT must be written to '1'. The selection of peripheral functions, A to N, is done by writing
                               to the Peripheral Multiplexing Odd and Even bits in the Peripheral Multiplexing register
                               (PMUXn.PMUXE/O) of the PORT. The table below describes the peripheral signals multiplexed to the
                               PORT I/O pins.


                                                              Important: Not all signals are available on all devices. Refer to the Configuration Summary for
                                                              available peripherals.



Table 6-1. Multiplexed Peripheral Signals
                                           TFBGA                Pad    A       B                                                C     D      E       F     G      H     I        J     K     L      M       N
VQFN 48



          TQFP/VQFN/WLCSP 64



                                TQFP 100




                                                   TQFP 128




                                           120                  Name   EIC     ANARE ADC0      ADC1      AC   DAC      PTC      SERCO SERCO TC       TCC   TCC,   QSPI, SDHC,    I2S   PCC   GMAC   GCLK,   CCL
                                                                               F                                                M     M                    PDEC   CAN1, CAN0                        AC
                                                                                                                                                                  USB,
                                                                                                                                                                  CORTE
                                                                                                                                                                  X_CM4



48        64/C6                 100        B2      128          PB03   EIC/    -      ADC0/ -            -    -        X21/Y2   -     SERCO TC6/     -     -      -     -        -     -     -      -       -
                                                                       EXTIN          AIN[15]                          1              M5/    WO[1]
                                                                       T[3]                                                           PAD[1]
1         01/B8                 1          A1      1            PA00   EIC/    -      -        -         -    -                 -     SERCO TC2/     -     -      -     -        -     -     -      -       -
                                                                       EXTIN                                                          M1/    WO[0]
                                                                       T[0]                                                           PAD[0]
2         02/C8                 2          B1      2            PA01   EIC/    -      -        -         -    -                 -     SERCO TC2/     -     -      -     -        -     -     -      -       -
                                                                       EXTIN                                                          M1/    WO[1]
                                                                       T[1]                                                           PAD[1]
                                3          C1      3            PC00   EIC/    -      -        ADC1/ -        -                 -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[10]
                                                                       T[0]
                                4          C2      4            PC01   EIC/    -      -        ADC1/     -    -                 -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[11]
                                                                       T[1]
                                5          D1      7            PC02   EIC/    -      -        ADC1/     -    -                 -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[4]
                                                                       T[2]
                                6          E2      8            PC03   EIC/    -      -        ADC1/     -    -                 -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[5]
                                                                       T[3]
3         03/C7                 7          E1      9            PA02   EIC/    -      ADC0/    -         -    DAC/              -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN          AIN[0]                  VOUT[0
                                                                       T[2]                                   ]
4         04/D6                 8          F2      10           PA03   EIC/    ANARE ADC0/     -         -    -        X0/Y0    -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN   F/    AIN[1]
                                                                       T[3]    VREFA
          05/D7                 9          F1      11           PB04   EIC/    -      -        ADC1/     -    -        X22/Y2   -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[6]                  2
                                                                       T[4]
          06/D8                 10         G1      12           PB05   EIC/    -      -        ADC1/     -    -        X23/Y2   -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[7]                  3
                                                                       T[5]
                                -          G2      13           PD00   EIC/    -      -        ADC1/ -        -                 -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[14]
                                                                       T[0]
                                -          H1      16           PD01   EIC/    -      -        ADC1/ -        -                 -     -      -       -     -      -     -        -     -     -      -       -
                                                                       EXTIN                   AIN[15]
                                                                       T[1]
          09/E7                 13         H2      17           PB06   EIC/    -      -        ADC1/     -    -        X24/Y2   -     -      -       -     -      -     -        -     -     -      -       CCL/
                                                                       EXTIN                   AIN[8]                  4                                                                                    IN[6]
                                                                       T[6]
          10/E6                 14         J1      18           PB07   EIC/    -      -        ADC1/     -    -        X25/Y2   -     -      -       -     -      -     -        -     -     -      -       CCL/
                                                                       EXTIN                   AIN[9]                  5                                                                                    IN[7]
                                                                       T[7]




                               © 2019 Microchip Technology Inc.                                                           Datasheet                                             DS60001507E-page 32
                                                                                                                          SAM D5x/E5x Family Data Sheet
                                                                                                                                              I/O Multiplexing and Considerations

...........continued
                                            TFBGA              Pad    A       B                                                    C      D      E       F       G       H      I       J        K      L        M       N
VQFN 48



           TQFP/VQFN/WLCSP 64



                                 TQFP 100




                                                    TQFP 128
                                            120                Name   EIC     ANARE ADC0       ADC1     AC       DAC      PTC      SERCO SERCO TC        TCC     TCC,    QSPI, SDHC,    I2S      PCC    GMAC     GCLK,   CCL
                                                                              F                                                    M     M                       PDEC    CAN1, CAN0                              AC
                                                                                                                                                                         USB,
                                                                                                                                                                         CORTE
                                                                                                                                                                         X_CM4



7          11/F5                 15         J2      19         PB08   EIC/    -      ADC0/     ADC1/    -        -        X1/Y1    -      SERCO TC4/     -       -       -      -       -        -      -        -       CCL/
                                                                      EXTIN          AIN[2]    AIN[0]                                     M4/    WO[0]                                                                   IN[8]
                                                                      T[8]                                                                PAD[0]
8          12/F8                 16         K1      20         PB09   EIC/    -      ADC0/     ADC1/    -        -        X2/Y2    -      SERCO TC4/     -       -       -      -       -        -      -        -       CCL/
                                                                      EXTIN          AIN[3]    AIN[1]                                     M4/    WO[1]                                                                   OUT[2]
                                                                      T[9]                                                                PAD[1]
9          13/F7                 17         K2      21         PA04   EIC/    ANARE ADC0/      -        AC/      -        X3/Y3    -      SERCO TC0/     -       -       -      -       -        -      -        -       CCL/
                                                                      EXTIN   F/    AIN[4]              AIN[0]                            M0/    WO[0]                                                                   IN[0]
                                                                      T[4]    VREFB                                                       PAD[0]
10         14/F6                 18         L1      22         PA05   EIC/    -      ADC0/     -        AC/      DAC/              -      SERCO TC0/     -       -       -      -       -        -      -        -       CCL/
                                                                      EXTIN          AIN[5]             AIN[1]   VOUT[1                   M0/    WO[1]                                                                   IN[1]
                                                                      T[5]                                       ]                        PAD[1]
11         15/G7                 19         L2      23         PA06   EIC/    ANARE ADC0/      -        AC/      -        X4/Y4    -      SERCO TC1/     -       -       -      SDHC0/ -         -      -        -       CCL/
                                                                      EXTIN   F/    AIN[6]              AIN[2]                            M0/    WO[0]                          SDCD                                     IN[2]
                                                                      T[6]    VREFC                                                       PAD[2]
12         16/G8                 20         M1      24         PA07   EIC/    -      ADC0/     -        AC/      -        X5/Y5    -      SERCO TC1/     -       -       -      SDHC0/ -         -      -        -       CCL/
                                                                      EXTIN          AIN[7]             AIN[3]                            M0/    WO[1]                          SDWP                                     OUT[0]
                                                                      T[7]                                                                PAD[3]
                                 -          N1      27         PC04   EIC/    -      -         -        -        -                 SERCO -       -       TCC0/   -       -      -       -        -      -        -       -
                                                                      EXTIN                                                        M6/                   WO[0]
                                                                      T[4]                                                         PAD[0]
                                 21         N2      28         PC05   EIC/    -      -         -        -        -                 SERCO -       -       -       -       -      -       -        -      -        -       -
                                                                      EXTIN                                                        M6/
                                                                      T[5]                                                         PAD[1]
                                 22         P1      29         PC06   EIC/    -      -         -        -        -                 SERCO -       -       -       -       -      SDHC0/ -         -      -        -       -
                                                                      EXTIN                                                        M6/                                          SDCD
                                                                      T[6]                                                         PAD[2]
                                 23         P2      30         PC07   EIC/    -      -         -        -        -                 SERCO -       -       -       -       -      SDHC0/ -         -      -        -       -
                                                                      EXTIN                                                        M6/                                          SDWP
                                                                      T[9]                                                         PAD[3]
13         17/H8                 26         R1      33         PA08   EIC/NMI -      ADC0/     ADC1/    -        -        X6/Y6    SERCO SERCO TC0/      TCC0/   TCC1/   QSPI/   SDHC0/ I2S/  -         -        -       CCL/
                                                                                     AIN[8]    AIN[2]                              M0/    M2/    WO[0]   WO[0]   WO[4]   DATA[0] SDCMD MCK[0]                            IN[3]
                                                                                                                                   PAD[0] PAD[1]
14         18/G6                 27         P3      34         PA09   EIC/    -      ADC0/     ADC1/    -        -        X7/Y7    SERCO SERCO TC0/      TCC0/   TCC1/   QSPI/   SDHC0/ I2S/     -      -        -       CCL/
                                                                      EXTIN          AIN[9]    AIN[3]                              M0/    M2/    WO[1]   WO[1]   WO[5]   DATA[1] SDDAT[ FS[0]                            IN[4]
                                                                      T[9]                                                         PAD[1] PAD[0]                                 0]
15         19/H7                 28         R2      35         PA10   EIC/    -      ADC0/ -            -        -        X8/Y8    SERCO SERCO TC1/      TCC0/   TCC1/   QSPI/   SDHC0/ I2S/     -      -        GCLK/   CCL/
                                                                      EXTIN          AIN[10]                                       M0/    M2/    WO[0]   WO[2]   WO[6]   DATA[2] SDDAT[ SCK[0]                   IO[4]   IN[5]
                                                                      T[10]                                                        PAD[2] PAD[2]                                 1]
16         20/G5                 29         P4      36         PA11   EIC/    -      ADC0/     -        -        -        X9/Y9    SERCO SERCO TC1/      TCC0/   TCC1/   QSPI/   SDHC0/ I2S/SD -        -        GCLK/   CCL/
                                                                      EXTIN          AIN[11]                                       M0/    M2/    WO[1]   WO[3]   WO[7]   DATA[3] SDDAT[ O                        IO[5]   OUT[1]
                                                                      T[11]                                                        PAD[3] PAD[3]                                 2]
19         23/H6                 32         R3      39         PB10   EIC/    -      -         -        -        -                 -      SERCO TC5/     TCC0/   TCC1/   QSPI/S SDHC0/ I2S/SDI -        -        GCLK/   CCL/
                                                                      EXTIN                                                               M4/    WO[0]   WO[4]   WO[0]   CK      SDDAT[                          IO[4]   IN[11]
                                                                      T[10]                                                               PAD[2]                                 3]
20         24/G4                 33         P5      40         PB11   EIC/    -      -         -        -        -                 -      SERCO TC5/     TCC0/   TCC1/   QSPI/C SDHC0/ I2S/    -        -        GCLK/   CCL/
                                                                      EXTIN                                                               M4/    WO[1]   WO[5]   WO[1]   S      SDCK    FS[1]                    IO[5]   OUT[1]
                                                                      T[11]                                                               PAD[3]
           25/H5                 34         R4      41         PB12   EIC/    -      -         -        -        -        X26/Y2   SERCO -       TC4/    TCC3/   TCC0/   CAN1/T SDHC0/ I2S/      -      -        GCLK/   -
                                                                      EXTIN                                               6        M4/           WO[0]   WO[0]   WO[0]   X      SDCD SCK[1]                      IO[6]
                                                                      T[12]                                                        PAD[0]
           26/H4                 35         P6      42         PB13   EIC/    -      -         -        -        -        X27/Y2   SERCO -       TC4/    TCC3/   TCC0/   CAN1/R SDHC0/ I2S/ -           -        GCLK/   -
                                                                      EXTIN                                               7        M4/           WO[1]   WO[1]   WO[1]   X      SDWP MCK[1]                      IO[7]
                                                                      T[13]                                                        PAD[1]
           27/G3                 36         R5      43         PB14   EIC/    -      -         -        -        -        X28/Y2   SERCO -       TC5/    TCC4/   TCC0/   CAN1/T -       -        PCC/    GMAC/   GCLK/   CCL/
                                                                      EXTIN                                               8        M4/           WO[0]   WO[0]   WO[2]   X                       DATA[8] GMDC    IO[0]   IN[9]
                                                                      T[14]                                                        PAD[2]
           28/H3                 37         P7      44         PB15   EIC/    -      -         -        -        -        X29/Y2   SERCO -       TC5/    TCC4/   TCC0/   CAN1/R -       -        PCC/    GMAC/ GCLK/     CCL/
                                                                      EXTIN                                               9        M4/           WO[1]   WO[1]   WO[3]   X                       DATA[9] GMDIO IO[1]     IN[10]
                                                                      T[15]                                                        PAD[3]
                                 -          R6      47         PD08   EIC/    -      -         -        -        -                 SERCO SERCO -         TCC0/   -       -      -       -        -      -        -       -
                                                                      EXTIN                                                        M7/    M6/            WO[1]
                                                                      T[3]                                                         PAD[0] PAD[1]
                                 -          P8      48         PD09   EIC/    -      -         -        -        -                 SERCO SERCO -         TCC0/   -       -      -       -        -      -        -       -
                                                                      EXTIN                                                        M7/    M6/            WO[2]
                                                                      T[4]                                                         PAD[1] PAD[0]
                                 -          R7      49         PD10   EIC/    -      -         -        -        -                 SERCO SERCO -         TCC0/   -       -      -       -        -      -        -       -
                                                                      EXTIN                                                        M7/    M6/            WO[3]
                                                                      T[5]                                                         PAD[2] PAD[2]
                                 -          P9      50         PD11   EIC/    -      -         -        -        -                 SERCO SERCO -         TCC0/   -       -      -       -        -      -        -       -
                                                                      EXTIN                                                        M7/    M6/            WO[4]
                                                                      T[6]                                                         PAD[3] PAD[3]
                                 -          R8      51         PD12   EIC/    -      -         -        -        -                 -      -      -       TCC0/   -       -      -       -        -      -        -       -
                                                                      EXTIN                                                                              WO[5]
                                                                      T[7]
                                 40         P10     52         PC10   EIC/    -      -         -        -        -                 SERCO SERCO -         TCC0/   TCC1/   -      -       -        -      -        -       -
                                                                      EXTIN                                                        M6/    M7/            WO[0]   WO[4]
                                                                      T[10]                                                        PAD[2] PAD[2]




                                © 2019 Microchip Technology Inc.                                                             Datasheet                                                 DS60001507E-page 33
                                                                                                             SAM D5x/E5x Family Data Sheet
                                                                                                                                 I/O Multiplexing and Considerations

...........continued
                                            TFBGA              Pad    A       B                                       C      D      E       F       G        H     I        J     K      L         M       N
VQFN 48



           TQFP/VQFN/WLCSP 64



                                 TQFP 100




                                                    TQFP 128
                                            120                Name   EIC     ANARE ADC0   ADC1   AC   DAC   PTC      SERCO SERCO TC        TCC     TCC,     QSPI, SDHC,    I2S   PCC    GMAC      GCLK,   CCL
                                                                              F                                       M     M                       PDEC     CAN1, CAN0                            AC
                                                                                                                                                             USB,
                                                                                                                                                             CORTE
                                                                                                                                                             X_CM4



                                 41         R9      55         PC11   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   TCC1/    -     -        -     -      GMAC/     -       -
                                                                      EXTIN                                           M6/    M7/            WO[1]   WO[5]                                GMDC
                                                                      T[11]                                           PAD[3] PAD[3]
                                 42         R10     56         PC12   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   TCC1/    -     -        -     PCC/   GMAC/ -           -
                                                                      EXTIN                                           M7/    M6/            WO[2]   WO[6]                         DATA[1 GMDIO
                                                                      T[12]                                           PAD[0] PAD[1]                                               0]
                                 43         P11     57         PC13   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   TCC1/    -     -        -     PCC/   -         -       -
                                                                      EXTIN                                           M7/    M6/            WO[3]   WO[7]                         DATA[1
                                                                      T[13]                                           PAD[1] PAD[0]                                               1]
                                 44         R11     58         PC14   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   TCC1/    -     -        -     PCC/   GMAC/     -       -
                                                                      EXTIN                                           M7/    M6/            WO[4]   WO[0]                         DATA[1 GRX[3]
                                                                      T[14]                                           PAD[2] PAD[2]                                               2]
                                 45         P12     59         PC15   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   TCC1/    -     -        -     PCC/   GMAC/     -       -
                                                                      EXTIN                                           M7/    M6/            WO[5]   WO[1]                         DATA[1 GRX[2]
                                                                      T[15]                                           PAD[3] PAD[3]                                               3]
21         29/F2                 46         R12     60         PA12   EIC/    -     -      -      -    -              SERCO SERCO TC2/      TCC0/   TCC1/    -     SDHC0/ -       PCC/   GMAC/     AC/    -
                                                                      EXTIN                                           M2/    M4/    WO[0]   WO[6]   WO[2]          SDCD           DEN1   GRX[1]    CMP[0]
                                                                      T[12]                                           PAD[0] PAD[1]
22         30/G2                 47         P13     61         PA13   EIC/    -     -      -      -    -              SERCO SERCO TC2/      TCC0/   TCC1/    -     SDHC0/ -       PCC/   GMAC/     AC/    -
                                                                      EXTIN                                           M2/    M4/    WO[1]   WO[7]   WO[3]          SDWP           DEN2   GRX[0]    CMP[1]
                                                                      T[13]                                           PAD[1] PAD[0]
23         31/H1                 48         R13     62         PA14   EIC/    -     -      -      -    -              SERCO SERCO TC3/      TCC2/   TCC1/    -     -        -     PCC/CL GMAC/ GCLK/       -
                                                                      EXTIN                                           M2/    M4/    WO[0]   WO[0]   WO[2]                         K      GTXCK IO[0]
                                                                      T[14]                                           PAD[2] PAD[2]
24         32/H2                 49         R14     63         PA15   EIC/    -     -      -      -    -              SERCO SERCO TC3/      TCC2/   TCC1/    -     -        -     -      GMAC/ GCLK/       -
                                                                      EXTIN                                           M2/    M4/    WO[1]   WO[1]   WO[3]                                GRXER IO[1]
                                                                      T[15]                                           PAD[3] PAD[3]
25         35/G1                 52         R15     66         PA16   EIC/    -     -      -      -    -     X10/Y1   SERCO SERCO TC2/      TCC1/   TCC0/    -     -        -     PCC/    GMAC/ GCLK/      CCL/
                                                                      EXTIN                                  0        M1/    M3/    WO[0]   WO[0]   WO[4]                         DATA[0] GCRS/ IO[2]      IN[0]
                                                                      T[0]                                            PAD[0] PAD[1]                                                       GRXDV
                                                                                                                                                                                          (6)

26         36/F1                 53         P14     67         PA17   EIC/    -     -      -      -    -     X11/Y11 SERCO SERCO TC2/       TCC1/   TCC0/    -     -        -     PCC/    GMAC/ GCLK/      CCL/
                                                                      EXTIN                                          M1/    M3/    WO[1]    WO[1]   WO[5]                         DATA[1] GTXEN IO[3]      IN[1]
                                                                      T[1]                                           PAD[1] PAD[0]
27         37/E1                 54         P15     68         PA18   EIC/    -     -      -      -    -     X12/Y1   SERCO SERCO TC3/      TCC1/   TCC0/    -     -        -     PCC/    GMAC/    AC/    CCL/
                                                                      EXTIN                                  2        M1/    M3/    WO[0]   WO[2]   WO[6]                         DATA[2] GTX[0]   CMP[0] IN[2]
                                                                      T[2]                                            PAD[2] PAD[2]
28         38/E2                 55         N14     69         PA19   EIC/    -     -      -      -    -     X13/Y1   SERCO SERCO TC3/      TCC1/   TCC0/    -     -        -     PCC/    GMAC/    AC/    CCL/
                                                                      EXTIN                                  3        M1/    M3/    WO[1]   WO[3]   WO[7]                         DATA[3] GTX[1]   CMP[1] OUT[0]
                                                                      T[3]                                            PAD[3] PAD[3]
                                 56         N15     70         PC16   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   PDEC/    -     -        -     -      GMAC/     -       -
                                                                      EXTIN                                           M6/    M0/            WO[0]   QDI[0]                               GTX[2]
                                                                      T[0]                                            PAD[0] PAD[1]
                                 57         M14     71         PC17   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   PDEC/    -     -        -     -      GMAC/     -       -
                                                                      EXTIN                                           M6/    M0/            WO[1]   QDI[1]                               GTX[3]
                                                                      T[1]                                            PAD[1] PAD[0]
                                 58         M15     72         PC18   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   PDEC/    -     -        -     -      GMAC/ -           -
                                                                      EXTIN                                           M6/    M0/            WO[2]   QDI[2]                               GRXCK
                                                                      T[2]                                            PAD[2] PAD[2]
                                 59         L14     73         PC19   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   -        -     -        -     -      GMAC/ -           -
                                                                      EXTIN                                           M6/    M0/            WO[3]                                        GTXER
                                                                      T[3]                                            PAD[3] PAD[3]
                                 60         L15     74         PC20   EIC/    -     -      -      -    -              -      -      -       TCC0/   -        -     SDHC1/ -       -      GMAC/ -           CCL/
                                                                      EXTIN                                                                 WO[4]                  SDCD                  GRXDV             IN[9]
                                                                      T[4]
                                 61         K14     75         PC21   EIC/    -     -      -      -    -              -      -      -       TCC0/   -        -     SDHC1/ -       -      GMAC/     -       CCL/
                                                                      EXTIN                                                                 WO[5]                  SDWP                  GCOL              IN[10]
                                                                      T[5]
                                 -          K15     76         PC22   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   -        -     -        -     -      GMAC/     -       -
                                                                      EXTIN                                           M1/    M3/            WO[6]                                        GMDC
                                                                      T[6]                                            PAD[0] PAD[1]
                                 -          J14     77         PC23   EIC/    -     -      -      -    -              SERCO SERCO -         TCC0/   -        -     -        -     -      GMAC/ -           -
                                                                      EXTIN                                           M1/    M3/            WO[7]                                        GMDIO
                                                                      T[7]                                            PAD[1] PAD[0]
                                 -          J15     80         PD20   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -     SDHC1/ -       -      -         -       -
                                                                      EXTIN                                           M1/    M3/            WO[0]                  SDCD
                                                                      T[10]                                           PAD[2] PAD[2]
                                 -          H14     81         PD21   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -     SDHC1/ -       -      -         -       -
                                                                      EXTIN                                           M1/    M3/            WO[1]                  SDWP
                                                                      T[11]                                           PAD[3] PAD[3]
           39/D4                 64         H15     82         PB16   EIC/    -     -      -      -    -              SERCO -       TC6/    TCC3/   TCC0/    -     SDHC1/ I2S/    -      -         GCLK/   CCL/
                                                                      EXTIN                                           M5/           WO[0]   WO[0]   WO[4]          SDCD SCK[0]                     IO[2]   IN[11]
                                                                      T[0]                                            PAD[0]
           40/D1                 65         G15     83         PB17   EIC/    -     -      -      -    -              SERCO -       TC6/    TCC3/   TCC0/    -     SDHC1/ I2S/ -         -         GCLK/   CCL/
                                                                      EXTIN                                           M5/           WO[1]   WO[1]   WO[5]          SDWP MCK[0]                     IO[3]   OUT[3]
                                                                      T[1]                                            PAD[1]
                                 66         G14     84         PB18   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   PDEC/    -     SDHC1/ -       -      -         GCLK/   -
                                                                      EXTIN                                           M5/    M7/            WO[0]   QDI[0]         SDDAT[                          IO[4]
                                                                      T[2]                                            PAD[2] PAD[2]                                0]




                                © 2019 Microchip Technology Inc.                                                Datasheet                                                  DS60001507E-page 34
                                                                                                             SAM D5x/E5x Family Data Sheet
                                                                                                                                 I/O Multiplexing and Considerations

...........continued
                                            TFBGA              Pad    A       B                                       C      D      E       F       G        H       I      J        K       L       M       N
VQFN 48



           TQFP/VQFN/WLCSP 64



                                 TQFP 100




                                                    TQFP 128
                                            120                Name   EIC     ANARE ADC0   ADC1   AC   DAC   PTC      SERCO SERCO TC        TCC     TCC,     QSPI, SDHC,    I2S      PCC     GMAC    GCLK,   CCL
                                                                              F                                       M     M                       PDEC     CAN1, CAN0                              AC
                                                                                                                                                             USB,
                                                                                                                                                             CORTE
                                                                                                                                                             X_CM4



                                 67         F15     85         PB19   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   PDEC/    -       SDHC1/ -        -       -       GCLK/   -
                                                                      EXTIN                                           M5/    M7/            WO[1]   QDI[1]           SDDAT[                          IO[5]
                                                                      T[3]                                            PAD[3] PAD[3]                                  1]
                                 68         F14     86         PB20   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   PDEC/    -       SDHC1/ -        -       -       GCLK/   -
                                                                      EXTIN                                           M3/    M7/            WO[2]   QDI[2]           SDDAT[                          IO[6]
                                                                      T[4]                                            PAD[0] PAD[1]                                  2]
                                 69         E15     87         PB21   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -       SDHC1/ -        -       -       GCLK/   -
                                                                      EXTIN                                           M3/    M7/            WO[3]                    SDDAT[                          IO[7]
                                                                      T[5]                                            PAD[1] PAD[0]                                  3]
29         41/D2                 70         E14     88         PA20   EIC/    -     -      -      -    -     X14/Y1   SERCO SERCO TC7/      TCC1/   TCC0/    -       SDHC1/ I2S/     PCC/    GMAC/   -       -
                                                                      EXTIN                                  4        M5/    M3/    WO[0]   WO[4]   WO[0]            SDCMD FS[0]     DATA[4] GMDC
                                                                      T[4]                                            PAD[2] PAD[2]
30         42/D3                 71         D15     89         PA21   EIC/    -     -      -      -    -     X15/Y1   SERCO SERCO TC7/      TCC1/   TCC0/    -       SDHC1/ I2S/SD   PCC/    GMAC/ -         -
                                                                      EXTIN                                  5        M5/    M3/    WO[1]   WO[5]   WO[1]            SDCK   O        DATA[5] GMDIO
                                                                      T[5]                                            PAD[3] PAD[3]
31         43/C1                 72         D14     92         PA22   EIC/    -     -      -      -    -     X16/Y1   SERCO SERCO TC4/      TCC1/   TCC0/    -       CAN0/T I2S/SDI PCC/    -        -       CCL/
                                                                      EXTIN                                  6        M3/    M5/    WO[0]   WO[6]   WO[2]            X              DATA[6]                  IN[6]
                                                                      T[6]                                            PAD[0] PAD[1]
32         44/C2                 73         C14     93         PA23   EIC/    -     -      -      -    -     X17/Y1   SERCO SERCO TC4/      TCC1/   TCC0/    USB/    CAN0/R I2S/     PCC/    -       -       CCL/
                                                                      EXTIN                                  7        M3/    M5/    WO[1]   WO[7]   WO[3]    SOF_1   X      FS[1]    DATA[7]                 IN[7]
                                                                      T[7]                                            PAD[1] PAD[0]                          KHZ
33         45/B1                 74         C15     94         PA24   EIC/    -     -      -      -    -              SERCO SERCO TC5/      TCC2/   PDEC/    USB/D   CAN0/T -        -       -       -       CCL/
                                                                      EXTIN                                           M3/    M5/    WO[0]   WO[2]   QDI[0]   M       X                                       IN[8]
                                                                      T[8]                                            PAD[2] PAD[2]
34         46/A1                 75         B15     95         PA25   EIC/    -     -      -      -    -              SERCO SERCO TC5/      -       PDEC/    USB/DP CAN0/R -         -       -       -       CCL/
                                                                      EXTIN                                           M3/    M5/    WO[1]           QDI[1]          X                                        OUT[2]
                                                                      T[9]                                            PAD[3] PAD[3]
37         49/A2                 78         A15     98         PB22   EIC/    -     -      -      -    -              SERCO SERCO TC7/      -       PDEC/    USB/    -      -        -       -       GCLK/   CCL/
                                                                      EXTIN                                           M1/    M5/    WO[0]           QDI[2]   SOF_1                                   IO[0]   IN[0]
                                                                      T[6]                                            PAD[2] PAD[2]                          KHZ
38         50/A3                 79         A14     99         PB23   EIC/    -     -      -      -    -              SERCO SERCO TC7/      -       PDEC/    -       -      -        -       -       GCLK/   CCL/
                                                                      EXTIN                                           M1/    M5/    WO[1]           QDI[0]                                           IO[1]   OUT[0]
                                                                      T[7]                                            PAD[3] PAD[3]
                                 80         B14     100        PB24   EIC/    -     -      -      -    -              SERCO SERCO -         -       PDEC/    -       -      -        -       -       AC/    -
                                                                      EXTIN                                           M0/    M2/                    QDI[1]                                           CMP[0]
                                                                      T[8]                                            PAD[0] PAD[1]
                                 81         B13     101        PB25   EIC/    -     -      -      -    -              SERCO SERCO -         -       PDEC/    -       -      -        -       -       AC/    -
                                                                      EXTIN                                           M0/    M2/                    QDI[2]                                           CMP[1]
                                                                      T[9]                                            PAD[1] PAD[0]
                                 -          A13     102        PB26   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -       -      -        -       -       -       -
                                                                      EXTIN                                           M2/    M4/            WO[2]
                                                                      T[12]                                           PAD[0] PAD[1]
                                 -          B12     103        PB27   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -       -      -        -       -       -       -
                                                                      EXTIN                                           M2/    M4/            WO[3]
                                                                      T[13]                                           PAD[1] PAD[0]
                                 -          A12     104        PB28   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -       -      I2S/     -       -       -       -
                                                                      EXTIN                                           M2/    M4/            WO[4]                           SCK[1]
                                                                      T[14]                                           PAD[2] PAD[2]
                                 -          B11     105        PB29   EIC/    -     -      -      -    -              SERCO SERCO -         TCC1/   -        -       -      I2S/   -         -       -       -
                                                                      EXTIN                                           M2/    M4/            WO[5]                           MCK[1]
                                                                      T[15]                                           PAD[3] PAD[3]
                                 82         A11     108        PC24   EIC/    -     -      -      -    -              SERCO SERCO -         -       -        CORTE -        -        -       -       -       -
                                                                      EXTIN                                           M0/    M2/                             X_CM4/
                                                                      T[8]                                            PAD[2] PAD[2]                          TRACE
                                                                                                                                                             DATA[3]
                                 83         B10     109        PC25   EIC/    -     -      -      -    -              SERCO SERCO -         -       -        CORTE -        -        -       -       -       -
                                                                      EXTIN                                           M0/    M2/                             X_CM4/
                                                                      T[9]                                            PAD[3] PAD[3]                          TRACE
                                                                                                                                                             DATA[2]
                                 84         A10     110        PC26   EIC/    -     -      -      -    -              -      -      -       -       -        CORTE -        -        -       -       -       -
                                                                      EXTIN                                                                                  X_CM4/
                                                                      T[10]                                                                                  TRACE
                                                                                                                                                             DATA[1]
                                 85         A9      111        PC27   EIC/    -     -      -      -    -              SERCO -       -       -       -        CORTE -        -        -       -       CORTE CCL/
                                                                      EXTIN                                           M1/                                    X_CM4/                                  X_M4/S IN[4]
                                                                      T[11]                                           PAD[0]                                 TRACE                                   WO
                                                                                                                                                             CLK
                                 86         B9      112        PC28   EIC/    -     -      -      -    -              SERCO -       -       -       -        CORTE -        -        -       -       -       CCL/
                                                                      EXTIN                                           M1/                                    X_CM4/                                          IN[5]
                                                                      T[12]                                           PAD[1]                                 TRACE
                                                                                                                                                             DATA[0]
39         51/B3                 87         B8      113        PA27   EIC/    -     -      -      -    -     X18/Y1   -      -      -       -       -                -      -        -       -       GCLK/   -
                                                                      EXTIN                                  8                                                                                       IO[1]
                                                                      T[11]
40         52/B4                 88         A8      114        RESET -        -     -      -      -    -              -      -      -       -       -        -       -      -        -       -       -       -
                                                               _N
45         57/C5                 93         B7      119        PA30   EIC/    -     -      -      -    -     X19/Y1   -      SERCO TC6/     TCC2/   -        CORTE -        -        -       -       GCLK/   CCL/
                                                                      EXTIN                                  9               M1/    WO[0]   WO[0]            X_CM4/                                  IO[0]   IN[3]
                                                                      T[14]                                                  PAD[2]                          SWCLK




                                © 2019 Microchip Technology Inc.                                                Datasheet                                                  DS60001507E-page 35
                                                                                                               SAM D5x/E5x Family Data Sheet
                                                                                                                                  I/O Multiplexing and Considerations

...........continued
                                            TFBGA                Pad    A       B                                       C     D      E       F       G       H     I        J     K     L      M       N
VQFN 48



           TQFP/VQFN/WLCSP 64



                                 TQFP 100




                                                    TQFP 128
                                            120                  Name   EIC     ANARE ADC0   ADC1   AC   DAC   PTC      SERCO SERCO TC       TCC     TCC,    QSPI, SDHC,    I2S   PCC   GMAC   GCLK,   CCL
                                                                                F                                       M     M                      PDEC    CAN1, CAN0                        AC
                                                                                                                                                             USB,
                                                                                                                                                             CORTE
                                                                                                                                                             X_CM4



46         58/D5                 94         B6      120          PA31   EIC/    -     -      -      -    -              -     SERCO TC6/     TCC2/   -       CORTE -        -     -     -      -       CCL/
                                                                        EXTIN                                                 M1/    WO[1]   WO[1]           X_CM4/                                    OUT[1]
                                                                        T[15]                                                 PAD[3]                         SWDIO-
           59/A6                 95         A5      121          PB30   EIC/    -     -      -      -    -              -     SERCO TC0/     TCC4/   TCC0/   CORTE -        -     -     -      -       -
                                                                        EXTIN                                                 M5/    WO[0]   WO[0]   WO[6]   X_CM4/
                                                                        T[14]                                                 PAD[1]                         SWO
           60/B6                 96         B5      122          PB31   EIC/    -     -      -      -    -              -     SERCO TC0/     TCC4/   TCC0/         -        -     -     -      -       -
                                                                        EXTIN                                                 M5/    WO[1]   WO[1]   WO[7]
                                                                        T[15]                                                 PAD[0]
                                 -          A4      123          PC30   EIC/    -     -      ADC1/ -     -              -     -      -       -       -       -     -        -     -     -      -       -
                                                                        EXTIN                AIN[12]
                                                                        T[14]
                                 -          B4      124          PC31   EIC/    -     -      ADC1/ -     -              -     -      -       -       -       -     -        -     -     -      -       -
                                                                        EXTIN                AIN[13]
                                                                        T[15]
           61/A7                 97         A3      125          PB00   EIC/    -     ADC0/ -       -    -     X30/Y3   -     SERCO TC7/     -       -       -     -        -     -     -      -       CCL/
                                                                        EXTIN         AIN[12]                  0              M5/    WO[0]                                                             IN[1]
                                                                        T[0]                                                  PAD[2]
           62/B7                 98         B3      126          PB01   EIC/    -     ADC0/ -       -    -     X31/Y3   -     SERCO TC7/     -       -       -     -        -     -     -      -       CCL/
                                                                        EXTIN         AIN[13]                  1              M5/    WO[1]                                                             IN[2]
                                                                        T[1]                                                  PAD[3]
47         63/A8                 99         A2      127          PB02   EIC/    -     ADC0/ -       -    -     X20/Y2   -     SERCO TC6/     TCC2/   -       -     -        -     -     -      -       CCL/
                                                                        EXTIN         AIN[14]                  0              M5/    WO[0]   WO[2]                                                     OUT[0]
                                                                        T[2]                                                  PAD[0]



                                Note:
                                 1. All analog pin functions are on the peripheral function B. The peripheral function B must be
                                      selected to disable the digital control of the pin. The AC has analog signals on the peripheral
                                      function B and digital signals on the peripheral function M.
                                 2. The pins used by the SERCOM in I2C mode are listed in section SERCOM I2C Configurations.
                                 3. The following High Sink pins have different properties than the regular pins:
                                      PA08, PA09, PA12, PA13, PA16, PA17, PA22, PA23, PD08, PD09.
                                 4. Clusters of multiple GPIO pins are sharing the same supply pin.
                                 5. When TRACE is used in single-wire debug mode, PC27 assumes the role of SWO. In other debug
                                      modes, PB30 assumes the SWO functionality.
                                 6. GRXDV is available on PA16 for the 64-pin package only.


                                                               Important: Not all signals are available on all devices. Refer to the Configuration Summary for
                                                               available peripherals.


                                Related Links
                                6.2.6 SERCOM I2C Configurations
                                6.2.9 GPIO Clusters



6.2                             Other Functions

6.2.1                           Oscillator Pinout
                                The oscillators are not mapped to the normal PORT functions and their multiplexing is controlled by
                                registers in the Oscillators Controller (OSCCTRL) and in the 32K Oscillators Controller (OSC32KCTRL).




                                © 2019 Microchip Technology Inc.                                                  Datasheet                                                DS60001507E-page 36
                                                             SAM D5x/E5x Family Data Sheet
                                                                       I/O Multiplexing and Considerations

        Table 6-2. Oscillator Pinout

         Oscillator                        Supply              Signal                    I/O pin
         XOSC0                             VDDIO               XIN                       PA14
                                                               XOUT                      PA15
         XOSC1                             VDDIO               XIN                       PB22
                                                               XOUT                      PB23
         XOSC32K                           VSWOUT              XIN32                     PA00
                                                               XOUT32                    PA01

        Note: To guarantee the XOSC32K behavior in crystal mode, PC00 must be static.
        Table 6-3. XOSC32K Jitter Minimization

         Package Pin Count                                     Steady Signal Recommended
         128                                                   PB00, PB01, PB02, PB03, PC00, PC01
         100                                                   PB00, PB01, PB02, PB03, PC00, PC01
         120                                                   PB00, PB01, PB02, PB03, PC00, PC01
         64                                                    PB00,PB01,PB02,PB03, PA02,PA03
         48                                                    PB02, PB03,PA02,PA03

6.2.2   Serial Wire Debug Interface Pinout
        Only the SWCLK pin is mapped to the normal PORT functions. A debugger cold-plugging or hot-plugging
        detection will automatically switch the SWDIO port to the SWDIO function.
        Table 6-4. Serial Wire Debug Interface Pinout

         Signal                                     Supply                     I/O pin
         SWCLK                                      VDDIO                      PA30
         SWDIO                                      VDDIO                      PA31

6.2.3   Trace Port Interface Unit Pinout
        The Embedded Trace Module (ETM) is leaning on Trace Port Interface Unit (TPIU) to export data out of
        the system.
        Table 6-5. Trace Port Interface Unit Pinout

         Signal                                     Supply                     I/O pin
         TRACE DATA[3]                              VDDIO                      PC24
         TRACE DATA[2]                              VDDIO                      PC25
         TRACE DATA[1]                              VDDIO                      PC26
         TRACE DATA[0]                              VDDIO                      PC28
         TRACE CLK                                  VDDIO                      PC27




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 37
                                                          SAM D5x/E5x Family Data Sheet
                                                                     I/O Multiplexing and Considerations

        ...........continued
         Signal                              Supply                             I/O pin
         SWO                                 VDDIO                              PB30, PC27

6.2.4   Supply Controller Pinout
        The outputs of the Supply Controller (SUPC) are not mapped to the normal PORT functions. They are
        controlled by registers in the SUPC.
        Table 6-6. SUPC Pinout

         Signal                                               I/O pin
         OUT0                                                 PB01
         OUT1                                                 PB02

        Note: If the RTC is enabled to use the pins shared with the SUPC, the RTC will have higher priority.

6.2.5   RTC Pinout
        The pins used for Tamper Detection by the Real Time Counter (RTC) are not mapped to the regular
        PORT functions. These pins and their multiplexing is controlled by register settings of the RTC. If many
        pins of the tamper detection feature is not used by the RTC, then the pin could be used for other I/O
        functions, by ensuring the corresponding TAMPCTRL.INACT function is disabled.
        Table 6-7. RTC Pinout

                                RTC Signal                                          I/O Pin
                                     IN0                                             PB00
                                     IN1                                             PB02
                                     IN2                                             PA02
                                     IN3                                             PC00
                                     IN4                                             PC01
                                    OUT                                              PB01


                       Important: If Supply Controller (SUPC) and RTC are configured to drive pin PB1 or pin PB2,
                       then the RTC has priority.




6.2.6   SERCOM I2C Configurations
        The SAM D5x/E5x has up to eight instances of the serial communication interface (SERCOM) peripheral.
        All instances support USART, including RS485 and ISO7816, SPI and I²C protocols. The following table
        lists the I²C pins location.




        © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 38
                                                                 SAM D5x/E5x Family Data Sheet
                                                                          I/O Multiplexing and Considerations

         Table 6-8. SERCOM I²C Pinout

          Package Pin Count                      Supply                              I/O pins with I²C Support
          128                                    VDDIOB                              PA08, PA09
                                                 VDDIO                               PA12, PA13, PA16, PA17, PA22,
                                                                                     PA23, PD08, PD09
          120                                    VDDIOB                              PA08, PA09
                                                 VDDIO                               PA12, PA13, PA16, PA17, PA22,
                                                                                     PA23, PD08, PD09
          100                                    VDDIOB                              PA08, PA09
                                                 VDDIO                               PA12, PA13, PA16, PA17, PA22,
                                                                                     PA23
          64                                     VDDIOB                              PA08, PA09
                                                 VDDIO                               PA12, PA13, PA16, PA17, PA22,
                                                                                     PA23
          48                                     VDDIO                               PA08, PA09, PA12, PA13, PA16,
                                                                                     PA17, PA22, PA23

6.2.7    TCC Configurations
         The SAM D5x/E5x has five instances of the Timer/Counter for Control applications (TCC) peripheral,
         TCC[4:0]. The following table lists the features for each TCC instance.
Table 6-9. TCC Configuration Summary
  TCC#        Channels         Waveform     Counter      Fault    Dithering   Output     Dead Time       SWAP       Pattern
             (CC_NUM)           Output       size                             matrix      Insertion                generation
                              (WO_NUM)                                                      (DTI)

    0             6               8          24-bit       Yes       Yes        Yes          Yes           Yes         Yes

    1             4               8          24-bit       Yes       Yes        Yes          Yes           Yes         Yes

    2             3               3          16-bit       Yes         -        Yes           -             -            -

    3             2               2          16-bit       Yes         -         -            -             -            -

    4             2               2          16-bit       Yes         -         -            -             -            -


         Note: The number of CC registers (CC_NUM) for each TCC corresponds to the number of compare/
         capture channels, so that a TCC can have more Waveform Outputs (WO_NUM) than CC registers.

6.2.8    IOSET Configurations
         The SAM D5x/E5x has multiple peripheral instances, mapped to different IO locations. Each peripheral IO
         location is called IOSET and for a given peripheral, signals from different IOSET cannot be mixed.

                      For a given peripheral with two pads PAD0 and PAD1:
                       • Valid: PAD0 and PAD1 in the same IOSETn.
                       • Invalid: PAD0 in IOSETx and PAD1 in IOSETy.




         © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 39
                                                         SAM D5x/E5x Family Data Sheet
                                                                     I/O Multiplexing and Considerations

6.2.8.1   SERCOM IOSET Configurations
          The following tables lists each IOSET Pins for each SERCOM instance.
          Table 6-10. SERCOM0 IO SET Configuration
               SERCOM Signal           IOSET 1 PINs   IOSET 2 PINs         IOSET 3 PINs     IOSET 4 PINs

                     PAD0              PA08           PB24                       PA04            PC17

                     PAD1              PA09           PB25                       PA05            PC16

                     PAD2              PA10           PC24                       PA06            PC18

                     PAD3              PA11           PC25                       PA07            PC19

          Table 6-11. SERCOM1 IO SET Configuration

              SERCOM Signal            IOSET 1 PINs   IOSET 2 PINs        IOSET 3 PINs     IOSET 4 PINs
                     PAD0              PA16           PC22                       PC27            PA00
                     PAD1              PA17           PC23                       PC28            PA01
                     PAD2              PA18           PD20                       PB22            PA30
                     PAD3              PA19           PD21                       PB23            PA31

          Table 6-12. SERCOM2 IO SET Configuration

              SERCOM Signal            IOSET 1 PINs   IOSET 2 PINs        IOSET 3 PINs     IOSET 4 PINs
                     PAD0              PA12           PB26                       PA09            PB25
                     PAD1              PA13           PB27                       PA08            PB24
                     PAD2              PA14           PB28                       PA10            PC24
                     PAD3              PA15           PB29                       PA11            PC25

          Table 6-13. SERCOM3 IO SET Configuration

              SERCOM Signal            IOSET 1 PINs   IOSET 2 PINs        IOSET 3 PINs     IOSET 4 PINs
                     PAD0              PA22           PB20                       PA17            PC23
                     PAD1              PA23           PB21                       PA16            PC22
                     PAD2              PA24           PA20                       PA18            PD20
                     PAD3              PA25           PA21                       PA19            PD21

          Table 6-14. SERCOM4 IO SET Configuration

              SERCOM Signal            IOSET 1 PINs   IOSET 2 PINs        IOSET 3 PINs    IOSET 4 PINs
                     PAD0              PB12           PB08                       PA13     PB27
                     PAD1              PB13           PB09                       PA12     PB26
                     PAD2              PB14           PB10                       PA14     PB28
                     PAD3              PB15           PB11                       PA15     PB29




          © 2019 Microchip Technology Inc.                   Datasheet                    DS60001507E-page 40
                                                                 SAM D5x/E5x Family Data Sheet
                                                                            I/O Multiplexing and Considerations

          Table 6-15. SERCOM5 IO SET Configuration

              SERCOM           IOSET 1         IOSET 2           IOSET 3       IOSET 4           IOSET 5        IOSET 6
               Signal          PINs            PINs                PINs          PINs              PINs           PINs
                 PAD0          PB16            PA23               PA23             PA23           PB31           PB02
                 PAD1          PB17            PA22               PA22             PA22           PB30           PB03
                 PAD2          PB18            PA20               PA24             PB22           PB00           PB00
                 PAD3          PB19            PA21               PA25             PB23           PB01           PB01

          Table 6-16. SERCOM6 IO SET Configuration

              SERCOM            IOSET 1 PINs        IOSET 2 PINs IOSET 3 PINs             IOSET 4 PINs      IOSET 5 PINs
               Signal
                PAD0                 PC16                PC04        PD09                 PC13                  PC13
                PAD1                 PC17                PC05        PD08                 PC12                  PC12
                PAD2                 PC18                PC06        PD10                 PC14                  PC10
                PAD3                 PC19                PC07        PD11                 PC15                  PC11

          Table 6-17. SERCOM7 IO SET Configuration

            SERCOM Signal IOSET 1 PINs                IOSET 2 PINs    IOSET 3 PINs        IOSET 4 PINs      IOSET 5 PINs
                   PAD0            PC12               PD08                  PC12              PB21              PB30
                   PAD1            PC13               PD09                  PC13              PB20              PB31
                   PAD2            PC14               PD10                  PC10              PB18              PA30
                   PAD3            PC15               PD11                  PC11              PB19              PA31

6.2.8.2   GMAC IOSET Configurations
          The following tables lists each IOSET pins for GMDIO and GMDC signals. All other GMAC signals can be
          used with all available IOSET configurations.
          Table 6-18. GMAC IO SET Configuration

              GMAC Signal           IOSET 1 PINs          IOSET 2 PINs             IOSET 3 PINs            IOSET 4 PINs
                   GMDC             PB14                  PC11                        PC22                    PA20
                  GMDIO             PB15                  PC12                        PC23                    PA21

6.2.8.3   I²S Configurations
          The following tables lists each IOSET Pins for I²S instance.
          Table 6-19. I²S IO SET Configuration

                     I²S Signal              IOSET 1 PINs                           IOSET 2 PINs
                       MCK0                  PA08                                   PB17
                         FS0                 PA09                                   PA20




          © 2019 Microchip Technology Inc.                        Datasheet                              DS60001507E-page 41
                                                                SAM D5x/E5x Family Data Sheet
                                                                           I/O Multiplexing and Considerations

          ...........continued
                     I²S Signal               IOSET 1 PINs                         IOSET 2 PINs
                        SCK0                  PA10                                 PB16
                        SDO                   PA11                                 PA21
                         SDI                  PB10                                 PA22
                         FS1                  PB11                                 PA23
                        SCK1                  PB12                                 PB28
                       MCK1                   PB13                                 PB29

6.2.8.4   TC IOSET Configurations
          The following tables lists each IOSET Pins for each TC instance.
          Table 6-20. TC0 IOSET Configuration

                 TC Signal          IOSET 1 PINs                IOSET 2 PINs                      IOSET 3 PINs
                    WO0             PA04                        PA08                                  PB30
                    WO1             PA05                        PA09                                  PB31

          Table 6-21. TC1 IOSET Configuration

           TC Signal                                 IOSET 1 PINs                            IOSET 2 PINs
           WO0                                       PA06                                         PA10
           WO1                                       PA07                                         PA11

          Table 6-22. TC2 IOSET Configuration

           TC Signal                         IOSET 1 PINs                 IOSET 2 PINs            IOSET 3 PINs
           WO0                               PA00                               PA12                  PA16
           WO1                               PA01                               PA13                  PA17

          Table 6-23. TC3 IOSET Configuration

           TC Signal                                 IOSET 1 PINs                            IOSET 2 PINs
           WO0                                       PA14                                         PA18
           WO1                                       PA15                                         PA19

          Table 6-24. TC4 IOSET Configuration

           TC Signal                         IOSET 1 PINs                 IOSET 2 PINs            IOSET 3 PINs
           WO0                               PB08                               PB12                  PA22
           WO1                               PB09                               PB13                  PA23




          © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 42
                                                                   SAM D5x/E5x Family Data Sheet
                                                                           I/O Multiplexing and Considerations

          Table 6-25. TC5 IOSET Configuration

           TC Signal                         IOSET 1 PINs                 IOSET 2 PINs                IOSET 3 PINs
           WO0                               PB10                              PB14                      PA24
           WO1                               PB11                              PB15                      PA25

          Table 6-26. TC6 IOSET Configuration

           TC Signal                         IOSET 1 PINs                 IOSET 2 PINs                IOSET 3 PINs
           WO0                               PB16                               PA30                     PB02
           WO1                               PB03                              PB17                      PA31

          Table 6-27. TC7 IOSET Configuration

           TC Signal                         IOSET 1 PINs                 IOSET 2 PINs                IOSET 3 PINs
           WO0                               PA20                              PB22                      PB00
           WO1                               PA21                              PB23                      PB01

6.2.8.5   TCC IOSET Configurations
          The following tables lists each IOSET Pins for each TCC instance.
          Table 6-28. TCC0 IO SET Configuration

           TCC Signal         IOSET 1           IOSET 2     IOSET 3        IOSET 4       IOSET 5 PINs IOSET 6 PINs
                                PINs              PINs      PINs           PINs
           WO0                  PA08                PC04    PC10           PC16              PB12              PA20
           WO1                  PA09                PD08    PC11           PC17              PB13              PA21
           WO2                  PA10                PD09    PC12           PC18              PB14              PA22
           WO3                  PA11                PD10    PC13           PC19              PB15              PA23
           WO4                  PB10                PD11    PC14           PC20              PA16              PB16
           WO5                  PB11                PD12    PC15           PC21              PA17              PB17
           WO6                  PA12                PC22    PA18           PB30              N/A(1)            N/A(1)
           WO7                  PA13                PC23    PA19           PB31              N/A(1)            N/A(1)

          Note: 1. The signal is available, but the edges are not aligned wrt. the other signals as specified.
          Table 6-29. TCC1 IO SET Configuration

            TCC Signal       IOSET 1 PINs           IOSET 2 PINs      IOSET 3 PINs     IOSET 4 PINs     IOSET 5 PINs
                WO0          PA16                   PD20                 PB18             PB10          PC14
                WO1          PA17                   PD21                 PB19             PB11          PC15
                WO2          PA18                   PB20                 PB26             PA12          PA14
                WO3          PA19                   PB21                 PB27             PA13          PA15




          © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 43
                                                                SAM D5x/E5x Family Data Sheet
                                                                         I/O Multiplexing and Considerations

          ...........continued
            TCC Signal       IOSET 1 PINs    IOSET 2 PINs          IOSET 3 PINs    IOSET 4 PINs     IOSET 5 PINs
                WO4          PA20            PB28                       PA08           PC10         N/A(1)
                WO5          PA21            PB29                       PA09           PC11         N/A(1)
                WO6          PA22            PA10                       PC12           N/A(1)       N/A(1)
                WO7          PA23            PA11                       PC13           N/A(1)       N/A(1)

          Note: 1. The signal is available, but the edges are not aligned wrt. the other signals as specified.
          Table 6-30. TCC2 IO SET Configuration

           TCC Signal                             IOSET 1 PINs                                IOSET 2 PINs
           WO0                                    PA14                                           PA30
           WO1                                    PA15                                           PA31
           WO2                                    PA24                                           PB02

          Table 6-31. TCC3 IO SET Configuration

           TCC Signal                             IOSET 1 PINs                                IOSET 2 PINs
           WO0                                    PB12                                           PB16
           WO1                                    PB13                                           PB17

          Table 6-32. TCC4 IO SET Configuration

           TCC Signal                             IOSET 1 PINs                                IOSET 2 PINs
           WO0                                    PB14                                           PB30
           WO1                                    PB15                                           PB31

6.2.8.6   PDEC IOSET Configurations
          The following tables lists each IOSET Pins for PDEC instance.
          Table 6-33. PDEC IO SET Configuration

              PDEC Signal          IOSET 1 PINs          IOSET 2 PINs          IOSET 3 PINs         IOSET 4 PINs
                  QDI[0]           PC16                  PB18                     PA24                  PB23
                  QDI[1]           PC17                  PB19                     PA25                  PB24
                  QDI[2]           PC18                  PB20                     PB22                  PB25




          © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 44
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                     I/O Multiplexing and Considerations

6.2.9    GPIO Clusters
Table 6-34. GPIO Clusters (1)
Package         Cluster        GPIO                                                                                  Supply/GND Pins Connected to
                                                                                                                     the Cluster

128pins         VDDIOB         PA11, PA10, PA09, PA08                                                                VDDIOB pins 32 and 37
                                                                                                                     GND pins 31 and 38
                               PB11, PB10

                               PC07, PC06, PC05, PC04

                VDDIO          PA31, PA30, PA27, PA25, PA24, PA23, PA22, PA21, PA20, PA19, PA18, PA17, PA16, PA15, VDDIO pins 46, 54, 65, 79, 91, 97,
                               PA14, PA13, PA12                                                                    107, 118
                                                                                                                   GND pins 45, 53, 64, 78, 90, 96,
                               PB31, PB30, PB29, PB28, PB27, PB26, PB25, PB24, PB23, PB22, PB21, PB20, PB19, PB18, 106, 116
                               PB17, PB16, PB15, PB14, PB13, PB12,

                               PC31, PC30, PC28, PC27, PC26, PC25, PC24, PC23, PC22, PC21, PC20, PC19, PC18,
                               PC17, PC16, PC15, PC14, PC13, PC12, PC11, PC10

                               PD21, PD20, PD12, PD11, PD10, PD09, PD08

                VDDANA         PA07, PA06, PA05, PA04, PA03, PA02                                                    VDDANA pins 6, 15, 26
                                                                                                                     GNDANA pins 5, 14, 25
                               PB09, PB08, PB07, PB06, PB05, PB04

                               PC03, PC02

                               PD01, PD00

                VSWOUT         PA01, PA00                                                                            VSWOUT

                               PB03, PB02, PB01, PB00

                               PC01, PC00

120pins         VDDIOB         PA11, PA10, PA09, PA08                                                                VDDIOB pins K6, K7 GND pins J6,
                                                                                                                     K8
                               PB11, PB10

                               PC07, PC06, PC05, PC04

                VDDIO          PA31, PA30, PA27, PA25, PA24, PA23, PA22, PA21, PA20, PA19, PA18, PA17, PA16, PA15,   VDDIO pins K10,H10,F10,F8,F7
                               PA14, PA13, PA12                                                                      GND pins K8,K9,J10,G10,F9,F6

                               PB31, PB30, PB29, PB28, PB27, PB26, PB25, PB24, PB23, PB22, PB21, PB20, PB19, PB18,
                               PB17, PB16, PB15, PB14, PB13, PB12,

                               PC31, PC30, PC28, PC27, PC26, PC25, PC24, PC23, PC22, PC21, PC20, PC19, PC18,
                               PC17, PC16, PC15, PC14, PC13, PC12, PC11, PC10

                               PD21, PD20, PD12, PD11, PD10, PD09, PD08

                VDDANA         PA07, PA06, PA05, PA04, PA03, PA02                                                    VDDANA pin M2 GNDANA pin H6

                               PB09, PB08, PB07, PB06, PB05, PB04

                               PC03, PC02

                               PD01, PD00

                VSWOUT         PA01, PA00                                                                            VSWOUT

                               PB03, PB02, PB01, PB00

                               PC01, PC00




          © 2019 Microchip Technology Inc.                               Datasheet                                     DS60001507E-page 45
                                                                           SAM D5x/E5x Family Data Sheet
                                                                                         I/O Multiplexing and Considerations

...........continued
 Package               Cluster     GPIO                                                                                  Supply/GND Pins Connected to
                                                                                                                         the Cluster

 100pins               VDDIOB      PA11, PA10, PA09, PA08                                                                VDDIOB pins 25 and 30
                                                                                                                         GND pins 24 and 31
                                   PB11, PB10

                                   PC07, PC06, PC05

                       VDDIO       PA31, PA30, PA27, PA25, PA24, PA23, PA22, PA21, PA20, PA19, PA18, PA17, PA16, PA15,   VDDIO pins 39, 51, 63, 77, 92
                                   PA14, PA13, PA12                                                                      GND pins 38, 50, 62, 76, 90

                                   PB31, PB30, PB25, PB24, PB23, PB22, PB21, PB20, PB19, PB18, PB17, PB16, PB15, PB14,
                                   PB13, PB12, PB11, PB10

                                   PC28, PC27, PC26, PC25, PC24, PC21, PC20, PC19, PC18, PC17, PC16, PC15, PC14,
                                   PC13, PC12, PC11, PC10

                       VDDANA      PA07, PA06, PA05, PA04, PA03, PA02                                                    VDDANA pin 12
                                                                                                                         GNDANA pin 11
                                   PB09, PB08, PB07, PB06, PB05, PB04

                                   PC03, PC02

                       VSWOUT      PA01, PA00                                                                            VSWOUT

                                   PB03, PB02, PB01, PB00

                                   PC01, PC00

 64 Pins               VDDIOB      PA11, PA10, PA09, PA08                                                                VDDIOB pin 21
                                                                                                                         GND pin 22
                                   PB11, PB10

                       VDDIO       PB12,PB13,PB14,PB15,PB16,PB17,PB30,PB31                                               VDDIO pins 34,48, 56
                                                                                                                         GND pins 33,47,54
                                   PA12,PA13,PA16,PA17,PA18,PA19, PA20, PA21,PA22,PA23,PA24,PA25,PA27,PA30,PA31

                                   PA14,PA15,PB22,PB23

                       VDDANA      PA2,PA3,PB4,PB5,PB6,PB7,PB8,PB9,PA4,PA5,PA6,PA7                                       VDDANA pin 8
                                                                                                                         GNDANA pin 7

                       VSWOUT      PB0,PB1,PB2,PB3,PA0,PA1                                                               VSWOUT

 48 pins               VDDIO       PA8, PA9,PA10,PA11                                                                    VDDIO pins 17, 36, 44
                                                                                                                         GND pins 18, 35, 42
                                   PB10,PB11,PA12,PA13,PA14,PA15

                                   PA16,PA17,PA18,P19,PA20,PA21,PA22,PA23,PA24,PA25

                                   PB22,PB23

                                   PA27

                                   PA30, PA31

                       VDDANA      PA2,PA3,PB8,PB9,PA4,PA5,PA6,PA7                                                       VDDANA pin 6
                                                                                                                         GNDANA pin 5

                       VSWOUT      PB2,PB3,PA0,PA1                                                                       VSWOUT


               Note:
                1. The RESETN pin in all packages are connected to the VDDIO cluster.




              © 2019 Microchip Technology Inc.                               Datasheet                                    DS60001507E-page 46
