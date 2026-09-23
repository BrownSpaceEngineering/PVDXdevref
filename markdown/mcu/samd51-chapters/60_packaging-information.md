# 58. Packaging Information

*Source: `Atmel-SAMD51.pdf`, pages 2073-2095 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                                     Packaging Information


58.      Packaging Information

58.1     Package Marking Information
         All devices are marked with Atmel logo and ordering code.
         Additional marking information is as follows:
           • "YY": Manufacturing year
           • "WW": Manufacturing week
           • "R": Internal Code
           • "XXXXXX": Lot number




58.2     Thermal Considerations

58.2.1   Thermal Resistance Data
         The following table summarizes the thermal resistance data depending on the package.
         Table 58-1. Thermal Resistance Data

          Package Type                       θJA                               θJC
          64-pin TQFP                        57.4°C/W                          10.6°C/W
          100-pin TQFP                       55.0°C/W                          11.1°C/W
          128-pin TQFP                       48.7°C/W                          9.4°C/W
          120-pin TFBGA                      36.63°C/W                         12.2°C/W
          48-pin VQFN                        29.8°C/W                          10.0°C/W
          64-pin VQFN                        30.3°C/W                          9.9°C/W
          64-pin WLCSP                       36.8°C/W                          5.0°C/W

58.2.2   Junction Temperature
         The average chip-junction temperature, TJ, in °C can be obtained from the following equations:
           • Equation 1- TJ = TA + (PD x θJA)
           • Equation 2 - TJ = TA + (PD x (θHEATSINK + θJC))
         where:
           • θJA = Package thermal resistance, Junction-to-ambient (°C/W), see Thermal Resistance Data
           • θJC = Package thermal resistance, Junction-to-case thermal resistance (°C/W), see Thermal
             Resistance Data




         © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 2073
                                                         SAM D5x/E5x Family Data Sheet
                                                                                      Packaging Information

         • θHEATSINK = Thermal resistance (°C/W) specification of the external cooling device
         • PD = Device power consumption (W)
         • TA = Ambient temperature (°C)
       From the first equation, the user can derive the estimated lifetime of the chip and decide whether a
       cooling device is necessary or not. If a cooling device has to be fitted on the chip, the second equation
       must be used to compute the resulting average chip-junction temperature TJ in °C.



58.3   Package Drawings
       Note: For current package drawings, refer to the Microchip Packaging Specification, which is available
       at http://www.microchip.com/packaging.




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 2074
                                                         SAM D5x/E5x Family Data Sheet
                                                                                     Packaging Information

58.3.1   48-Pin VQFN




         Note: The exposed die attach pad is not connected electrically inside the device.
         Table 58-2. Device and Package Maximum Weight

          140                                                 mg

         Table 58-3. Package Characteristics

          Moisture Sensitivity Level                          MSL3




         © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 2075
                                   SAM D5x/E5x Family Data Sheet
                                                 Packaging Information

Table 58-4. Package Reference

 JEDEC Drawing Reference             MO-220
 JESD97 Classification               E3




© 2019 Microchip Technology Inc.   Datasheet          DS60001507E-page 2076
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                 Packaging Information

58.3.2   48-Pin VQFN Wettable Flanks

           48-Lead Very Thin Plastic Quad Flat, No Lead Package (U5B) - 7x7 mm Body [VQFN]
           With 5.15 mm Exposed Pad and Stepped Wettable Flanks; Atmel Legacy ZLH
            Note:     For the most current package drawings, please see the Microchip Packaging Specification located at
                      http://www.microchip.com/packaging


                                                                                              48X
                                                                                                    0.08 C
                                                   D                       A
                                      D                                                              0.10 C
                                      4                                         B
                                      N


                              E   1
                              4
                                  2




                  NOTE 1
                                                                                E
                  (DATUM B)
                  (DATUM A)


             2X
                    0.10 C

                    2X
                         0.10 C
                                               TOP VIEW                                                                 A1
                                                                       0.10 C A B
                                                                                                                        (A3)
                                                  D2
                                                                                                               A
                                                                                               SEATING
                                                                                                       C
                                                                                    0.10 C A B  PLANE
              DETAIL A
                                                                                                         SIDE VIEW


                                                                 A        A
                                                                           E2                                            A4
                          e
                          2



                                  2                                                                   D3
                                  1

                                                                                                     SECTION A-A
                                      N                                   (K)
                          L                                            48X b
                                          e                                0.10      C A B
                                                                           0.05      C
                                              BOTTOM VIEW

                                                                     Microchip Technology Drawing C04-21493 Rev A Sheet 1 of 2


           © 2018 Microchip Technology Inc.




         © 2019 Microchip Technology Inc.                         Datasheet                                DS60001507E-page 2077
                                                            SAM D5x/E5x Family Data Sheet
                                                                                              Packaging Information

  48-Lead Very Thin Plastic Quad Flat, No Lead Package (U5B) - 7x7 mm Body [VQFN]
  With 5.15 mm Exposed Pad and Stepped Wettable Flanks; Atmel Legacy ZLH
    Note:    For the most current package drawings, please see the Microchip Packaging Specification located at
             http://www.microchip.com/packaging




             DETAIL 1
      ALTERNATE TERMINAL
        CONFIGURATIONS




                                                           Units             MILLIMETERS
                                                Dimension Limits      MIN        NOM     MAX
                          Number of Terminals               N                      48
                          Pitch                              e                 0.50 BSC
                          Overall Height                    A         0,80        0.85   0.90
                          Standoff                          A1        0.00        0.02   0.05
                          Terminal Thickness                A3                0.203 REF
                          Overall Length                    D                  7.00 BSC
                          Exposed Pad Length                D2        5.05        5.15   5.25
                          Overall Width                     E                  7.00 BSC
                          Exposed Pad Width                 E2        5.05        5.15   5.25
                          Terminal Width                     b        0.20        0.25   0.30
                          Terminal Length                    L        0.35        0.40   0.45
                          Terminal-to-Exposed-Pad           K                  0.53 REF
                          Wettable Flank Step Length        D3          -           -    0.085
                          Wettable Flank Step Height        A4        0.10          -    0.19
       Notes:
       1. Pin 1 visual index feature may vary, but must be located within the hatched area.
       2. Package is saw singulated
       3. Dimensioning and tolerancing per ASME Y14.5M
              BSC: Basic Dimension. Theoretically exact value shown without tolerances.
              REF: Reference Dimension, usually without tolerance, for information purposes only.


                                                               Microchip Technology Drawing C04-21493 Rev A Sheet 2 of 2


  © 2018 Microchip Technology Inc.




© 2019 Microchip Technology Inc.                              Datasheet                             DS60001507E-page 2078
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                     Packaging Information

  48-Lead Very Thin Plastic Quad Flat, No Lead Package (U5B) - 7x7 mm Body [VQFN]
  With 5.15 mm Exposed Pad and Stepped Wettable Flanks; Atmel Legacy ZLH
    Note:    For the most current package drawings, please see the Microchip Packaging Specification located at
             http://www.microchip.com/packaging


                                                                   C1
                                                                   X2
                                                                      EV
                                                  48



                                          1
                                                                                                      ØV
                                          2



                                                                                                             G2

                           C2 Y2
                                    EV


                                                                                                        G1


                                                                                                             Y1


                                                                                              X1
                 SILK SCREEN                            E


                                           RECOMMENDED LAND PATTERN
                                                             Units                   MILLIMETERS
                                                  Dimension Limits          MIN          NOM          MAX
                           Contact Pitch                      E                        0.50 BSC
                           Optional Center Pad Width          X2                                      5.25
                           Optional Center Pad Length         Y2                                      5.25
                           Contact Pad Spacing                C1                         6.90
                           Contact Pad Spacing                C2                         6.90
                           Contact Pad Width (X48)            X1                                      0.30
                           Contact Pad Length (X48)           Y1                                      0.85
                           Contact Pad to Center Pad (X48)    G1            0.20
                           Contact Pad to Center Pad (X44)    G2            0.40
                           Thermal Via Diameter               V                          0.30
                           Thermal Via Pitch                  EV                         1.00
        Notes:
        1. Dimensioning and tolerancing per ASME Y14.5M
                BSC: Basic Dimension. Theoretically exact value shown without tolerances.
        2. For best soldering results, thermal vias, if used, should be filled or tented to avoid solder loss during
           reflow process

                                                                                   Microchip Technology Drawing C04-23493 Rev A


  © 2018 Microchip Technology Inc.




© 2019 Microchip Technology Inc.                                  Datasheet                                       DS60001507E-page 2079
                                            SAM D5x/E5x Family Data Sheet
                                                          Packaging Information

58.3.3   64-Ball WLCSP




         © 2019 Microchip Technology Inc.   Datasheet          DS60001507E-page 2080
                                         SAM D5x/E5x Family Data Sheet
                                                       Packaging Information

Table 58-5. Device and Package Maximum Weight

 14                                             mg

Table 58-6. Package Characteristics

 Moisture Sensitivity Level                     MSL1

Table 58-7. Package Reference

 JEDEC Drawing Reference                        N/A
 JESD97 Classification                          e1




© 2019 Microchip Technology Inc.          Datasheet         DS60001507E-page 2081
                                                         SAM D5x/E5x Family Data Sheet
                                                                                     Packaging Information

58.3.4   64-Pin VQFN




         Note: The exposed die attach pad is not connected electrically inside the device.
         Table 58-8. Device and Package Maximum Weight

          200                                                 mg




         © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 2082
                                     SAM D5x/E5x Family Data Sheet
                                                   Packaging Information

Table 58-9. Package Charateristics

 Moisture Sensitivity Level            MSL3

Table 58-10. Package Reference

 JEDEC Drawing Reference               MO-220
 JESD97 Classification                 E3




© 2019 Microchip Technology Inc.     Datasheet          DS60001507E-page 2083
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                       Packaging Information

58.3.5   64-Pin VQFN Wettable Flanks

           64-Lead Very Thin Plastic Quad Flat, No Lead Package (U6B) - 9x9 mm Body [VQFN]
           With 4.7 mm Exposed Pad and Stepped Wettable Flanks; Atmel Legacy ZRB
            Note:     For the most current package drawings, please see the Microchip Packaging Specification located at
                      http://www.microchip.com/packaging

                                                                                            64X
                                                                                                  0.08 C

                                                                                                       0.10 C
             NOTE 1                                D                      A    B
                                      N


                                 1
                                 2




                                                                               E
                  (DATUM B)
                  (DATUM A)


             2X
                    0.10 C

                    2X
                             0.10 C
                                                TOP VIEW                                                              0.05
                                                                                                                      0.20
                                                                 0.10     C A B                                       0.90
                                                   D2                                         SEATING
                                                                                                      C
                                                                                               PLANE
                                                                                                         SIDE VIEW
              DETAIL A
                                                                                     0.10     C A B




                                                                          E2
                                                                                                                    A4
                         e       A    A
                         2




                                 2                                             (K)                D3                 STEPPED
                                 1                                                                                   WETTABLE
                                                                                            SECTION A-A              FLANK
                                      N

                             L                                          64X b
                                            e                               0.10       C A B
                                                                            0.05       C
                                            BOTTOM VIEW
                                                                   Microchip Technology Drawing C04-21497 Rev A Sheet 1 of 2


           © 2018 Microchip Technology Inc.




         © 2019 Microchip Technology Inc.                         Datasheet                                     DS60001507E-page 2084
                                                           SAM D5x/E5x Family Data Sheet
                                                                                             Packaging Information


  64-Lead Very Thin Plastic Quad Flat, No Lead Package (U6B) - 9x9 mm Body [VQFN]
  With 4.7 mm Exposed Pad and Stepped Wettable Flanks; Atmel Legacy ZRB
   Note:     For the most current package drawings, please see the Microchip Packaging Specification located at
             http://www.microchip.com/packaging




               DETAIL 1
      ALTERNATE TERMINAL
        CONFIGURATIONS




                                                          Units             MILLIMETERS
                                               Dimension Limits      MIN        NOM     MAX
                         Number of Terminals               N                      64
                         Pitch                              e                 0.50 BSC
                         Overall Height                    A         0.80        0.85   0.90
                         Standoff                          A1        0.00       0.035   0.05
                         Terminal Thickness                A3                0.203 REF
                         Overall Length                    D                  9.00 BSC
                         Exposed Pad Length                D2        4.60        4.70   4.80
                         Overall Width                     E                  9.00 BSC
                         Exposed Pad Width                 E2        4.60        4.70   4.80
                         Terminal Width                     b        0.15        0.20   0.25
                         Terminal Length                    L        0.35        0.40   0.45
                         Terminal-to-Exposed-Pad           K                  1.75 REF
                         Wettable Flank Step Length        D3          -           -    0.085
                         Wettable Flank Step Height        A4        0.10          -    0.19
      Notes:
      1. Pin 1 visual index feature may vary, but must be located within the hatched area.
      2. Package is saw singulated
      3. Dimensioning and tolerancing per ASME Y14.5M
             BSC: Basic Dimension. Theoretically exact value shown without tolerances.
             REF: Reference Dimension, usually without tolerance, for information purposes only.


                                                              Microchip Technology Drawing C04-21497 Rev A Sheet 1 of 2


  © 2018 Microchip Technology Inc.




© 2019 Microchip Technology Inc.                             Datasheet                             DS60001507E-page 2085
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                      Packaging Information


  64-Lead Very Thin Plastic Quad Flat, No Lead Package (U6B) - 9x9 mm Body [VQFN]
  With 4.7 mm Exposed Pad and Stepped Wettable Flanks; Atmel Legacy ZRB
   Note:     For the most current package drawings, please see the Microchip Packaging Specification located at
             http://www.microchip.com/packaging


                                                                  C1
                                                                  X2
                                                                       EV
                                                 64



                                          1
                                          2
                                                                                                      ØV


                                                                                                           G2

                  C2       Y2       EV




                                                                                                 G1

                                                                                                           Y1


                                                                                                X1
                SILK SCREEN                           E


                                          RECOMMENDED LAND PATTERN
                                                             Units                   MILLIMETERS
                                                  Dimension Limits          MIN          NOM          MAX
                          Contact Pitch                       E                        0.50 BSC
                          Optional Center Pad Width           X2                                      4.80
                          Optional Center Pad Length          Y2                                      4.80
                          Contact Pad Spacing                 C1                         8.90
                          Contact Pad Spacing                 C2                         8.90
                          Contact Pad Width (X64)             X1                                      0.30
                          Contact Pad Length (X64)            Y1                                      0.85
                          Contact Pad to Center Pad (X64)     G1            1.63
                          Contact Pad to Contact Pad (X60)    G2            0.20
                          Thermal Via Diameter                V                          0.33
                          Thermal Via Pitch                   EV                         1.20
       Notes:
       1. Dimensioning and tolerancing per ASME Y14.5M
               BSC: Basic Dimension. Theoretically exact value shown without tolerances.
       2. For best soldering results, thermal vias, if used, should be filled or tented to avoid solder loss during
          reflow process

                                                                                   Microchip Technology Drawing C04-23497 Rev A


  © 2018 Microchip Technology Inc.




© 2019 Microchip Technology Inc.                                 Datasheet                                      DS60001507E-page 2086
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                                         Packaging Information

58.3.6   64-pin TQFP
              64-Lead Plastic Thin Quad Flatpack (PT)-10x10x1 mm Body, 2.00 mm Footprint [TQFP]

                Note:    For the most current package drawings, please see the Microchip Packaging Specification located at
                         http://www.microchip.com/packaging



                                                                          D
                                                                          D1


                                                                  D1/2
                                                                               D

                                        NOTE 2


                                                                                                        E1/2
                                                A                                                   B

                                                                                                               E1     E
                                                                                      A         A
                          SEE DETAIL 1
                                                         N

                                  4X N/4 TIPS
                                       0.20 C A-B D              1 3
                                                                  2
                                                                                           4X
                                                NOTE 1
                                                                                                0.20 H A-B D

                                                                       TOP VIEW




                                                                                                               A2
                                                    A
                                            C                                                                        0.05
                               SEATING
                                PLANE
                                                                                                 A1
                                                                                     64 X b
                                        0.08 C                                           0.08       C A-B D
                                                             e


                                                                   SIDE VIEW




                                                                                   Microchip Technology Drawing C04-085C Sheet 1 of 2




         © 2019 Microchip Technology Inc.                                Datasheet                                  DS60001507E-page 2087
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                      Packaging Information

     64-Lead Plastic Thin Quad Flatpack (PT)-10x10x1 mm Body, 2.00 mm Footprint [TQFP]

       Note:       For the most current package drawings, please see the Microchip Packaging Specification located at
                   http://www.microchip.com/packaging




         H

                                                     c


               
                                      L          
                               (L1)              X=A—B OR D

                    SECTION A-A                            X


                                                     e/2



                                                                  DETAIL 1

                                                               Units              MILLIMETERS
                                                    Dimension Limits       MIN        NOM             MAX
                              Number of Leads                   N                       64
                              Lead Pitch                         e                  0.50 BSC
                              Overall Height                    A            -           -            1.20
                              Molded Package Thickness          A2         0.95        1.00           1.05
                              Standoff                          A1         0.05          -            0.15
                              Foot Length                        L         0.45        0.60           0.75
                              Footprint                         L1                  1.00 REF
                              Foot Angle                                   0°         3.5°            7°
                              Overall Width                     E                  12.00 BSC
                              Overall Length                    D                  12.00 BSC
                              Molded Package Width              E1                 10.00 BSC
                              Molded Package Length             D1                 10.00 BSC
                              Lead Thickness                     c         0.09          -            0.20
                              Lead Width                         b         0.17        0.22           0.27
                              Mold Draft Angle Top                        11°         12°            13°
        Notes:                Mold Draft Angle Bottom                     11°         12°            13°

        1. Pin 1 visual index feature may vary, but must be located within the hatched area.
        2. Chamfers at corners are optional; size may vary.
        3. Dimensions D1 and E1 do not include mold flash or protrusions. Mold flash or
            protrusions shall not exceed 0.25mm per side.
        4. Dimensioning and tolerancing per ASME Y14.5M
                BSC: Basic Dimension. Theoretically exact value shown without tolerances.
                REF: Reference Dimension, usually without tolerance, for information purposes only.
                                                                          Microchip Technology Drawing C04-085C Sheet 2 of 2




© 2019 Microchip Technology Inc.                                  Datasheet                                  DS60001507E-page 2088
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               Packaging Information

    64-Lead Plastic Thin Quad Flatpack (PT)-10x10x1 mm Body, 2.00 mm Footprint [TQFP]

      Note:       For the most current package drawings, please see the Microchip Packaging Specification located at
                  http://www.microchip.com/packaging




                                                                  C1




                                                                                                     E




                                  C2

                                                                                                         G




                                                                                                Y1


                                                                                       X1



                                           RECOMMENDED LAND PATTERN




                                                              Units            MILLIMETERS
                                                   Dimension Limits     MIN        NOM        MAX
                           Contact Pitch                       E                 0.50 BSC
                           Contact Pad Spacing                 C1                  11.40
                           Contact Pad Spacing                 C2                  11.40
                           Contact Pad Width (X28)             X1                             0.30
                           Contact Pad Length (X28)            Y1                             1.50
                           Distance Between Pads               G        0.20
         Notes:
         1. Dimensioning and tolerancing per ASME Y14.5M
                BSC: Basic Dimension. Theoretically exact value shown without tolerances.
                                                                   Microchip Technology Drawing C04-2085B Sheet 1 of 1




© 2019 Microchip Technology Inc.                                Datasheet                                DS60001507E-page 2089
                                                  SAM D5x/E5x Family Data Sheet
                                                                            Packaging Information

58.3.7   100 pin TQFP




         Table 58-11. Device and Package Maximum Weight

          520                                         mg

         Table 58-12. Package Characteristics

          Moisture Sensitivity Level                  MSL3

         Table 58-13. Package Reference

          JEDEC Drawing Reference                     MS-026, variant AED
          JESD97 Classification                       e3




         © 2019 Microchip Technology Inc.          Datasheet                     DS60001507E-page 2090
                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                                                           Packaging Information

58.3.8   120-ball TFBGA

           120-Ball Thin Fine Pitch Ball Grid Array Package (DGB) - 8x8 mm Body [TFBGA]

            Note:     For the most current package drawings, please see the Microchip Packaging Specification located at
                      http://www.microchip.com/packaging


                                                                                          D                                      A    B
                                   NOTE 1
                                                                  2       4       6       8       10        12        14
                                                              1       3       5       7       9        11        13        15

                                                          A
                                                          B
                                                          C
                                                          D
                                                          E
                                    (DATUM A)             F
                                                          G
                                                          H                                                                           E
                                                          J
                                                          K
                                                          L
                                    (DATUM B)             M
                                                          N
                                   2X                     P
                                            0.10 C        R



                                            2X
                                                     0.10 C                   TOP VIEW

                                                                                                                                          SEE DETAIL A
                                                 C
                                 SEATING              A
                                  PLANE

                                                                          SIDE VIEW

                                                                                          D1
                                                                  2       4       6       8       10        12        14
                                                              1       3       5       7       9        11        13         15

                                                          R
                                                          P
                                                          N
                                                          M
                                                          L
                                                          K
                                                          J
                                                          H                                                                      E1
                                                          G
                                                          F
                                                          E
                                                          D
                                                          C
                                                          B
                                                          A

                                    NOTE 1
                                                                                                                           120X Øb
                                                                          e                                                    0.15       C A B
                                                                                                                               0.08       C
                                                                      BOTTOM VIEW
                                                                                          Microchip Technology Drawing C04-21465 Rev A Sheet 1 of 2




         © 2019 Microchip Technology Inc.                                             Datasheet                                                   DS60001507E-page 2091
                                                           SAM D5x/E5x Family Data Sheet
                                                                                             Packaging Information

 120-Ball Thin Fine Pitch Ball Grid Array Package (DGB) - 8x8 mm Body [TFBGA]

   Note:      For the most current package drawings, please see the Microchip Packaging Specification located at
              http://www.microchip.com/packaging




                                                   0.10 C


       (A3)


           (A2)                                      A1


                                   120X
                                          0.08 C
                       DETAIL A




                                                        Units               MILLIMETERS
                                             Dimension Limits        MIN        NOM          MAX
                         Number of Terminals             N                       120
                         Pitch                            e                   0.50 BSC
                         Overall Height                  A             -          -          1.20
                         Standoff                        A1          0.11         -          0.21
                         Substrate Thickness             A2                   2.10 REF
                         Mold Cap Thickness              A3                   0.70 REF
                         Overall Length                  D                    8.00 BSC
                         Overall Ball Pitch              D1                   7.00 BSC
                         Overall Width                   E                    8.00 BSC
                         Exposed Pad Width               E1                   7.00 BSC
                         Terminal Width                   b          0.20         -          0.30
      Notes:
      1. Pin 1 visual index feature may vary, but must be located within the hatched area.
      2. Package is saw singulated
      3. Dimensioning and tolerancing per ASME Y14.5M
             BSC: Basic Dimension. Theoretically exact value shown without tolerances.
             REF: Reference Dimension, usually without tolerance, for information purposes only.

                                                              Microchip Technology Drawing C04-21465 Rev A Sheet 1 of 2




© 2019 Microchip Technology Inc.                             Datasheet                              DS60001507E-page 2092
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                        Packaging Information


  120-Ball Thin Fine Pitch Ball Grid Array Package (DGB) - 8x8 mm Body [TFBGA]

   Note:     For the most current package drawings, please see the Microchip Packaging Specification located at
             http://www.microchip.com/packaging




                                                                     C1

                                         1   2   3   4   5   6   7       8   9   10 11 12 13 14   15
                                     A

                                     B
                                     C
                                     D
                                     E
                                     F
                                     G

                             C2      H
                                     J
                                     K
                                     L
                                     M
                                                                                                         ØX
                                     N
                                     P

                                     R




           SILK SCREEN                                               E


                                         RECOMMENDED LAND PATTERN




                                                           Units                          MILLIMETERS
                                                Dimension Limits                  MIN         NOM        MAX
                         Contact Pitch                      E                               0.50 BSC
                         Contact Pad Spacing                C1                              7.00 BSC
                         Contact Pad Spacing                C2                              7.00 BSC
                         Contact Pad Width (X20)            X                                  0.25




        Notes:
        1. Dimensioning and tolerancing per ASME Y14.5M
              BSC: Basic Dimension. Theoretically exact value shown without tolerances.

                                                                                        Microchip Technology Drawing C04-23465 Rev A




© 2019 Microchip Technology Inc.                                     Datasheet                                   DS60001507E-page 2093
                                                  SAM D5x/E5x Family Data Sheet
                                                                Packaging Information

58.3.9   128 pin TQFP




         Table 58-14. Device and Package Maximum Weight

          520                                        mg

         Table 58-15. Package Characteristics

          Moisture Sensitivity Level                 MSL3




         © 2019 Microchip Technology Inc.          Datasheet         DS60001507E-page 2094
                                                      SAM D5x/E5x Family Data Sheet
                                                                                    Packaging Information

       Table 58-16. Package Reference

        JEDEC Drawing Reference                           MS-026
        JESD97 Classification                             E3



58.4   Soldering Profile
       The following table gives the recommended soldering profile from J-STD-20.
       Table 58-17. Recommended Soldering Profile

        Profile Feature                                   Green Package
        Average Ramp-up Rate (217°C to peak)              3°C/s max.
        Preheat Temperature 175°C ±25°C                   150-200°C
        Time Maintained Above 217°C                       60-150s
        Time within 5°C of Actual Peak Temperature        30s
        Peak Temperature Range                            260°C
        Ramp-down Rate                                    6°C/s max.
        Time 25°C to Peak Temperature                     8 minutes max.

       A maximum of three reflow passes is allowed per component.




       © 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 2095
