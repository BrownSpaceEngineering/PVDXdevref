# 26. ICM - Integrity Check Monitor

*Source: `Atmel-SAMD51.pdf`, pages 686-724 — SAMD51 family datasheet*

                                                      SAM D5x/E5x Family Data Sheet
                                                                         ICM - Integrity Check Monitor


26.    ICM - Integrity Check Monitor

26.1   Overview
       The Integrity Check Monitor (ICM) is a DMA controller that performs hash calculation over multiple
       memory regions through the use of transfer descriptors located in memory (ICM Descriptor Area). The
       Hash function is based on the Secure Hash Algorithm (SHA). The ICM controller integrates two modes of
       operation. The first one is used to hash a list of memory regions and save the digests to memory (ICM
       Hash Area). The second operation mode is an active monitoring of the memory. In that mode, the hash
       function is evaluated and compared to the digest located at a predefined memory address (ICM Hash
       Area). If a mismatch occurs, an interrupt is raised.



26.2   Features
         • DMA AHB master interface
         • Supports monitoring of up to four non-contiguous memory regions
         • Supports block gathering through the use of linked list
         • Supports Secure Hash Algorithm (SHA1, SHA224, SHA256)
         • Compliant with FIPS Publication 180-2
         • Configurable processing period:
            – When SHA1 algorithm is processed, the run-time period is either 85 or 209 clock cycles.
            – When SHA256 or SHA224 algorithm is processed, the run-time period is either 72 or 194 clock
               cycles.
         • Programmable bus burden




       © 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 686
                                                           SAM D5x/E5x Family Data Sheet
                                                                                 ICM - Integrity Check Monitor


26.3     Block Diagram
         Figure 26-1. Integrity Check Monitor Block Diagram


                                                          Host            Configuration
                                            APB           Interface       Registers




                                                           SHA
                                                           Hash
                                                           Engine




                                                         Context
                                                         Registers




                                                         Monitoring        Integrity
                                                         FSM               Scheduler




                                                       Master
                                                       DMA Interface




                                                         Bus Layer




26.4     Signal Description
         Not applicable.



26.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

26.5.1   Power Management
         The ICM will run only when the source clocks are running, i.e. when the CPU is in Active mode.

26.5.2   Clocks
         The ICM bus clocks (CLK_ICM_AHB and CLK_ICM_APB) can be enabled and disabled in the Main
         Clock module (MCLK) by writing the respective bit in the mask registers (MCLK.AHBMASK.ICM and
         MCLK.APBCMASK.ICM).
         The default states of CLK_ICM_AHB and CLK_ICM_APB are given by the reset values of the respective
         mask registers.
         Related Links
         15.7 Register Summary




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 687
                                                           SAM D5x/E5x Family Data Sheet
                                                                              ICM - Integrity Check Monitor

26.5.3   DMA
         Not applicable.

26.5.4   Interrupts
         The ICM has an interrupt line connected to the Interrupt Controller. Handling the ICM interrupt requires
         programming the interrupt controller before configuring the ICM.
         Related Links
         10.2 Nested Vector Interrupt Controller

26.5.5   Events
         Not applicable.

26.5.6   Debug Operation
         Not applicable.



26.6     Functional Description

26.6.1   Overview
         The Integrity Check Monitor (ICM) is a DMA controller that performs SHA-based memory hashing over
         memory regions. As shown in the Block Diagram, it integrates a DMA interface, a Monitoring Finite State
         Machine (FSM), an integrity scheduler, a set of context registers, a SHA engine, an interface for
         configuration and status registers.
         The SHA engine requires a message padded according to FIPS180-4 specification when used as a SHA
         calculation unit only. Otherwise, if the ICM is used as integrated check for memory content, the padding is
         not mandatory. The SHA module produces an N-bit message digest each time a block is read and a
         processing period ends. N is 160 for SHA1, 224 for SHA224, 256 for SHA256.
         When the ICM module is enabled, it sequentially retrieves a circular list of region descriptors from the
         memory (Main List described in Figure 26-2). Up to four regions may be monitored. Each region
         descriptor is composed of four words indicating the layout of the memory region (see also Example in
         26.6.3 Region Descriptor Structure). It also contains the hashing engine configuration on a per region
         basis. As soon as the descriptor is loaded from the memory and context registers are updated with the
         data structure, the hashing operation starts. A programmable number of blocks (see TRSIZE field of the
         RCTRL structure member) is transferred from the memory to the SHA engine. When the desired number
         of blocks have been transferred, the digest is either moved to memory (Write Back function) or compared
         with a digest reference located in the system memory (Compare function). If a digest mismatch occurs,
         an interrupt is triggered if unmasked. The ICM module passes through the region descriptor list until the
         end of the list marked by an End of List bit set to one. To continuously monitor the list of regions, the
         WRAP bit must be set to one in the last data structure.




         © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 688
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                    ICM - Integrity Check Monitor

Figure 26-2. ICM Region Descriptor and Hash Areas
                                                     Main List               infinite loop
                                                                             when wrap bit is set

                                                                WRAP=1                                         End of Region N
                                                Region N
                                                Descriptor


                   ICM Descriptor                                                             Secondary List
                 Area - Contiguous
                 Read-only Memory
                                                                                        End of Region 1 List
                                                                WRAP=0
                                                Region 1
                                                Descriptor
                                                                                                                        End of Region 0
                                                                WRAP=0
                                                Region 0
                                                Descriptor




                                               Region N Hash

                    ICM Hash Area -
                      Contiguous
                    Read-write once
                       Memory                  Region 1 Hash

                                               Region 0 Hash


Each region descriptor supports gathering of data through the use of the Secondary List. Unlike the Main
List, the Secondary List cannot modify the configuration attributes of the region. When the end of the
Secondary List has been encountered, the ICM returns to the Main List. Memory integrity monitoring can
be considered as a background service and the mandatory bandwidth shall be very limited. In order to
limit the ICM memory bandwidth, use the BBC field of the CFG register to control ICM memory load.
Figure 26-3. Region Descriptor
                                             Main List

                                      Region 3 Descriptor

                                      Region 2 Descriptor
                                                                         Optional Region 0 Secondary List
                                      Region 1 Descriptor

                                      Region 0 Descriptor
                          ICMDSCR
                                                                                                          End of Region 0




                                                            0x00C    Region NEXT              0x00C       Region NEXT


                                                            0x008    Region CTRL              0x008       Region CTRL


                                                            0x004    Region CFG               0x004       Unused


                                                            0x000    Region ADDR              0x000       Region ADDR




© 2019 Microchip Technology Inc.                                    Datasheet                                                 DS60001507E-page 689
                                                            SAM D5x/E5x Family Data Sheet
                                                                               ICM - Integrity Check Monitor

26.6.2   ICM Hash Area
         The ICM Hash Area is a contiguous area of system memory that the controller and the processor can
         access. The physical location is configured in the ICM hash area start address register. This address is a
         multiple of 128 bytes. If the CDWBN bit of the context register is cleared (i.e., Write Back activated), the
         ICM controller performs a digest write operation at the following starting location: *(HASH) + (RID<<5),
         where RID is the current region context identifier. If the CDWBN bit of the context register is set (i.e.,
         Digest Comparison activated), the ICM controller performs a digest read operation at the same address.
26.6.2.1 Message Digest Example
         Considering the following 512 bits message (example given in FIPS 180-4):
         “61626380000000000000000000000000000000000000000000000000000000000000000000000000000
         000000000000000000000000000000000000000000018”
         The message is written to memory in a Little Endian (LE) system architecture.

          Memory Address                    Address Offset / Byte Lane
                                            0x3 / 31:24       0x2 / 23:16          0x1 / 15:8         0x0 / 7:0
          0x000                             80                63                   62                 61
          0x004–0x038                       00                00                   00                 00
          0x03C                             18                00                   00                 00

         The digest is stored at the memory location pointed at by the ICM_HASH pointer with a Region Offset.

          Memory Address                    Address Offset / Byte Lane
                                            0x3 / 31:24       0x2 / 23:16          0x1 / 15:8         0x0 / 7:0
          0x000                             36                3e                   99                 a9
          0x004                             6a                81                   06                 47
          0x008                             71                25                   3e                 ba
          0x00C                             6c                c2                   50                 78
          0x010                             9d                d8                   d0                 9c

          Memory Address                    Address Offset / Byte Lane
                                            0x3 / 31:24       0x2 / 23:16          0x1 / 15:8         0x0 / 7:0
          0x000                             22                7d                   09                 23
          0x004                             22                d8                   05                 34
          0x008                             77                a4                   42                 86
          0x00C                             b3                55                   a2                 bd
          0x010                             e4                bc                   ad                 2a
          0x014                             f7                b3                   a0                 bd
          0x018                             a7                9d                   6c                 e3




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 690
                                                             SAM D5x/E5x Family Data Sheet
                                                                             ICM - Integrity Check Monitor

          Memory Address                    Address Offset / Byte Lane
                                            0x3 / 31:24        0x2 / 23:16      0x1 / 15:8        0x0 / 7:0
          0x000                             bf                 16               78                ba
          0x004                             ea                 cf               01                8f
          0x008                             de                 40               41                41
          0x00C                             23                 22               ae                5d
          0x010                             a3                 61               03                b0
          0x014                             9c                 7a               17                96
          0x018                             61                 ff               10                b4
          0x01C                             ad                 15               00                f2

         Considering the following 1024 bits message (example given in FIPS 180-4):
         “6162638000000000000000000000000000000000000000000000000000000000
         0000000000000000000000000000000000000000000000000000000000000000
         0000000000000000000000000000000000000000000000000000000000000000
         0000000000000000000000000000000000000000000000000000000000000018”
         The message is written to memory in a Little Endian (LE) system architecture.

          Memory Address                    Address Offset / Byte Lane
                                            0x3 / 31:24        0x2 / 23:16      0x1 / 15:8        0x0 / 7:0
          0x000                             80                 63               62                61
          0x004–0x078                       00                 00               00                00
          0x07C                             18                 00               00                00

26.6.3   Region Descriptor Structure
         The ICM Region Descriptor Area is a contiguous area of system memory that the controller and the
         processor can access. When the ICM controller is activated, the controller performs a descriptor fetch
         operation at the DSCR address. If the Main List contains more than one descriptor (i.e., more than one
         region is to be moderated), the fetch address is DSCR + RID<<4 where RID is the region identifier.
         Table 26-1. Region Descriptor Structure (Main List)

          Offset                                 Structure Member              Name
          DSCR+0x00+RID*(0x10)                   ICM Region Start Address      RADDR
          DSCR+0x04+RID*(0x10)                   ICM Region Configuration      RCFG
          DSCR+0x08+RID*(0x10)                   ICM Region Control            RCTRL
          DSCR+0x0C+RID*(0x10)                   ICM Region Next Address       RNEXT




         © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 691
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        ICM - Integrity Check Monitor

          Example 26-1. ICM Monitoring of 3 Memory Data Blocks (Defined as 2 Regions)
          The following figure shows the mandatory ICM settings to monitor three memory data
          blocks of the system memory (defined as two regions) with one region being not
          contiguous (two separate areas) and one contiguous memory area. For each said region,
          the SHA algorithm may be independently selected (different for each region). The wrap
          allows continuous monitoring.
          Figure 26-4. Example - Monitoring of 3 Memory Data Blocks (Defined as 2 Regions)
                           System Memory, data areas                System Memory, region descriptor structure


                                                            wrap=1 effect


                                     oc le 1
                                             ta
                                   Bl ing ion
                                       k Da
                 Size of
                                      S eg
                                                                            NEXT=0           @md+28
                                        R


                 region1                                                                                     Region 1
                                                   @r1d                      S1              @md+24
                 block (S1)                                                                                  Single
                                                                            wrap=1, etc @md+20               Descriptor
                                                       3      2              @r1d       @md+16
                                                                            NEXT=@sd @md+12
                 Size of                                                                                    Region 0
                                                                    1        S0B0       @md+8
                                               1
                                        Bl 0




                 region0
                                             k




                                                                                                            Main
                                    at on
                                          oc




                 block 1                                                    wrap=0, etc @md+4
                                   D egi




                                                                                                            Descriptor
                                      a
                                     R




                 (S0B1)                            @r0db1                    @r0db0     @md
                                                                    1
                                                       3      2              NEXT=0          @sd+12
                                                                              S0B1           @sd+8           Region 0
                                                                                                             Second
                                               0
                                        Bl 0




                                                                            don’t care       @sd+4
                                             k




                 Size of                                                                                     Descriptor
                                    at on
                                          oc
                                   D egi




                 region0                                                      @r0db1         @sd
                                      a
                                     R




                 block 0
                 (S0B0)


                                                   @r0db0




© 2019 Microchip Technology Inc.                                  Datasheet                                      DS60001507E-page 692
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     ICM - Integrity Check Monitor

26.6.3.1 Region Descriptor Structure Overview

 Offset        Name        Bit Pos.

                              7:0                                      RADDR[7:0]
                             15:8                                     RADDR[15:8]
  0x00        RADDR0
                             23:16                                    RADDR[23:16]
                             31:24                                    RADDR[31:24]
                              7:0      WCIEN   BEIEN    DMIEN       RHIEN                  EOM       WRAP      CDWBN
                             15:8                      ALGO[2:0]                          PROCDLY    SUIEN      ECIEN
  0x04        RCFG0
                             23:16
                             31:24
                              7:0                                      TRSIZE[7:0]
                             15:8                                     TRSIZE[15:8]
  0x08        RCTRL0
                             23:16
                             31:24
                              7:0                                      RADDR[7:0]
                             15:8                                     RADDR[15:8]
  0x0C        RADDR1
                             23:16                                    RADDR[23:16]
                             31:24                                    RADDR[31:24]
                              7:0
                             15:8
  0x0C        RNEXT0
                             23:16
                             31:24
                              7:0      WCIEN   BEIEN    DMIEN       RHIEN                  EOM       WRAP      CDWBN
                             15:8                      ALGO[2:0]                          PROCDLY    SUIEN      ECIEN
  0x10        RCFG1
                             23:16
                             31:24
                              7:0                                      TRSIZE[7:0]
                             15:8                                     TRSIZE[15:8]
  0x14        RCTRL1
                             23:16
                             31:24
                              7:0                                      RADDR[7:0]
                             15:8                                     RADDR[15:8]
  0x18        RADDR2
                             23:16                                    RADDR[23:16]
                             31:24                                    RADDR[31:24]
                              7:0
                             15:8
  0x18        RNEXT1
                             23:16
                             31:24
                              7:0      WCIEN   BEIEN    DMIEN       RHIEN                  EOM       WRAP      CDWBN
                             15:8                      ALGO[2:0]                          PROCDLY    SUIEN      ECIEN
  0x1C        RCFG2
                             23:16
                             31:24
                              7:0                                      TRSIZE[7:0]
                             15:8                                     TRSIZE[15:8]
  0x20        RCTRL2
                             23:16
                             31:24




          © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 693
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                         ICM - Integrity Check Monitor

...........continued

  Offset                Name    Bit Pos.

                                  7:0                                      RADDR[7:0]
                                 15:8                                     RADDR[15:8]
   0x24                RADDR3
                                 23:16                                    RADDR[23:16]
                                 31:24                                    RADDR[31:24]
                                  7:0
                                 15:8
   0x24                RNEXT2
                                 23:16
                                 31:24
                                  7:0      WCIEN   BEIEN    DMIEN       RHIEN                  EOM       WRAP      CDWBN
                                 15:8                      ALGO[2:0]                          PROCDLY    SUIEN      ECIEN
   0x28                RCFG3
                                 23:16
                                 31:24
                                  7:0                                      TRSIZE[7:0]
                                 15:8                                     TRSIZE[15:8]
   0x2C                RCTRL3
                                 23:16
                                 31:24
                                  7:0
                                 15:8
   0x30                RNEXT3
                                 23:16
                                 31:24




              © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 694
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                    ICM - Integrity Check Monitor

26.6.3.1.1 Region Start Address Structure Member

            Name:        RADDR
            Offset:      0x00 + n*0x0C [n=0..3]
            Reset:       0x00000000
            Property:    Read/Write


      Bit        31             30            29            28                 27     26        25           24
                                                                RADDR[31:24]
   Access        R/W           R/W           R/W           R/W             R/W       R/W       R/W          R/W
    Reset         0             0             0             0                  0      0         0            0


      Bit        23             22            21            20                 19     18        17           16
                                                                RADDR[23:16]
   Access        R/W           R/W           R/W           R/W             R/W       R/W       R/W          R/W
    Reset         0             0             0             0                  0      0         0            0


      Bit        15             14            13            12                 11     10        9            8
                                                                 RADDR[15:8]
   Access        R/W           R/W           R/W           R/W             R/W       R/W       R/W          R/W
    Reset         0             0             0             0                  0      0         0            0


      Bit         7             6             5             4                  3      2         1            0
                                                                 RADDR[7:0]
   Access        R/W           R/W           R/W           R/W             R/W       R/W       R/W          R/W
    Reset         0             0             0             0                  0      0         0            0


            Bits 31:0 – RADDR[31:0] Region Start Address
            This field indicates the first byte address of the region




        © 2019 Microchip Technology Inc.                            Datasheet                    DS60001507E-page 695
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                    ICM - Integrity Check Monitor

26.6.3.1.2 Region Configuration Structure Member

            Name:       RCFG
            Offset:     0x04 + n*0x0C [n=0..3]
            Reset:      0x00000000
            Property:   Read/Write


      Bit        31           30              29             28           27           26        25           24


   Access
    Reset


      Bit        23           22              21             20           19           18        17           16


   Access
    Reset


      Bit        15           14              13             12           11           10         9           8
                                           ALGO[2:0]                                PROCDLY     SUIEN       ECIEN
   Access                                                                             R/W       R/W          R/W
    Reset                      0              0               0                        0          1           1


      Bit         7            6              5               4           3            2          1           0
               WCIEN        BEIEN           DMIEN           RHIEN                     EOM       WRAP       CDWBN
   Access       R/W          R/W             R/W             R/W                      R/W       R/W          R/W
    Reset         1            1              1               1                        0          0           0


            Bits 14:12 – ALGO[2:0] User SHA Algorithm
            Value       Name              Description
            0           SHA1               SHA1 algorithm processed
            1           SHA256             SHA256 algorithm processed
            4           SHA224             SHA224 algorithm processed
            Other       -                  Reserved

            Bit 10 – PROCDLY Processing Delay
            For a given SHA algorithm, the runtime period has two possible lengths:
            Table 26-2. SHA Processing Runtime Periods

            Algorithm                               SHORTEST [number of cycles] LONGEST [number of cycles]
            SHA1                                    85                                209
            SHA224                                  72                                194
            SHA256                                  72                                194

            Value       Name                       Description
            0           SHORTEST                   SHA processing runtime is the shortest one
            1           LONGEST                    SHA processing runtime is the longest one




        © 2019 Microchip Technology Inc.                            Datasheet                     DS60001507E-page 696
                                                  SAM D5x/E5x Family Data Sheet
                                                                        ICM - Integrity Check Monitor

Bit 9 – SUIEN Monitoring Status Updated Condition Interrupt Enable
0: The RSU flag is set when the corresponding descriptor is loaded from memory to ICM.
1: The RSU flag remains cleared even if the condition is met.

Bit 8 – ECIEN End Bit Condition Interrupt Enable
0: The REC flag is set when the descriptor having the EOM bit set is processed.
1: The REC flag remains cleared even if the setting condition is met.

Bit 7 – WCIEN Wrap Condition Interrupt Disable
0: The RWC flag is set when the WRAP
1: The RWC flag remains cleared even if the setting condition is met.

Bit 6 – BEIEN Bus Error Interrupt Disable
0: The flag is set when an error is reported on the system bus by the bus MATRIX.
1: The flag remains cleared even if the setting condition is met.

Bit 5 – DMIEN Digest Mismatch Interrupt Disable
0: The RBE flag is set when the hash value just calculated from the processed region dffers from
expected hash value.
1: The RBE flag remains cleared even if the setting condition is met.

Bit 4 – RHIEN Region Hash Completed Interrupt Disable
0: The RHC flag is set when the field NEXT = 0 in a descriptor of the main or second list.
1: The RHC flag remains cleared even if the setting condition is met.

Bit 2 – EOM End of Monitoring
0: The current descriptor does not terminate the monitoring.
1: The current descriptor terminates the Main List. WRAP bit value has no effect.

Bit 1 – WRAP Wrap Command
0: The next region descriptor address loaded is the current region identifier descriptor address
incremented by 0x10.
1: The next region descriptor address loaded is DSCR.

Bit 0 – CDWBN Compare Digest or Write Back Digest
0: The digest is written to the Hash area.
1: The digest value is compared to the digest stored in the Hash area.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 697
                                                              SAM D5x/E5x Family Data Sheet
                                                                                ICM - Integrity Check Monitor

26.6.3.1.3 Region Control Structure Member

            Name:       RCTRL
            Offset:     0x08 + n*0x0C [n=0..3]
            Reset:      0x00000000
            Property:   R/W


      Bit        31           30           29          28                  27      26       25           24


   Access
    Reset


      Bit        23           22           21          20                  19      18       17           16


   Access
    Reset


      Bit        15           14           13          12                  11      10       9            8
                                                            TRSIZE[15:8]
   Access       R/W          R/W           R/W        R/W              R/W         R/W     R/W          R/W
    Reset        0             0            0          0                   0        0       0            0


      Bit        7             6            5          4                   3        2       1            0
                                                            TRSIZE[7:0]
   Access       R/W          R/W           R/W        R/W              R/W         R/W     R/W          R/W
    Reset        0             0            0          0                   0        0       0            0


            Bits 15:0 – TRSIZE[15:0] Transfer Size for the Current Chunk of Data




        © 2019 Microchip Technology Inc.                       Datasheet                     DS60001507E-page 698
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                      ICM - Integrity Check Monitor

26.6.3.1.4 Region Next Address Structure Member

               Name:        RNEXT
               Offset:      0x0C + n*0x0C [n=0..3]
               Reset:       0x00000000
               Property:    Read/Write


         Bit        31            30            29           28            27            26            25           24


   Access
    Reset


         Bit        23            22            21           20            19            18            17           16


   Access
    Reset


         Bit        15            14            13           12            11            10            9             8


   Access
    Reset


         Bit         7             6            5             4             3            2             1             0


   Access
    Reset


26.6.4         Using ICM as an SHA Engine
               The ICM can be configured to only calculate a SHA1, SHA224, SHA256 digest value.
26.6.4.1 Settings for Simple SHA Calculation
               The start address of the system memory containing the data to hash must be configured in the transfer
               descriptor of the DMA embedded in the ICM.
               The transfer descriptor is a system memory area integer multiple of 4 x 32-bit word and the start address
               of the descriptor must be configured in DSCR (the start address must be aligned on 64-bytes; six LSB
               must be cleared). If the data to hash is already padded according to SHA standards, only a single
               descriptor is required, and the EOM bit of RCFGn must be written to 1. If the data to hash does not
               contain a padding area, it is possible to define the padding area in another system memory location, the
               ICM can be configured to automatically jump from a memory area to another one by writing the descriptor
               register RNEXT with a value that differs from 0. Writing the RNEXT register with the start address of the
               padding area forces the ICM to concatenate both areas, thus providing the SHA result from the start
               address of the hash area configured in HASH.
               Whether the system memory is configured as a single or multiple data block area, the bits CDWBN and
               WRAP must be cleared in the region descriptor structure member RCFGn. The bits WBDIS, EOMDIS,
               SLBDIS must be cleared in CFG.
               Write the bits RHIEN and ECIEN in the Region Configuration Structure Member (RCFGn) to ‘0’:
                • The flag RHC[i], i being the region index, is set (if RHIEN is ‘0’) when the hash result is available at
                   address defined in HASH.




           © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 699
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   ICM - Integrity Check Monitor

           • The flag REC[i], i being the region index, is set (if ECIEN is ‘0’) when the hash result is available at
             the address defined in HASH.
         An interrupt is generated if the bit RHC[i] is written to ‘1’ in the IER (if RHC[i] is set in RCTRL of region i)
         or if the bit REC[i] is written to 1 in the IER (if REC[i] is set in RCTRL of region i).
26.6.4.2 Processing Period
         The SHA engine processing period can be configured by writing to the Region Configuration Structure
         Member register (RCFGn).
         The short processing period allows to allocate bandwidth to the SHA module whereas the long
         processing period allocates more bandwidth on the system bus to other applications.
         In SHA mode, the shortest processing period is 85 clock cycles + 2 clock cycles for start command
         synchronization. The longest period is 209 clock cycles + 2 clock cycles.
         In SHA256 and SHA224 modes, the shortest processing period is 72 clock cycles + 2 clock cycles for
         start command synchronization. The longest period is 194 clock cycles + 2 clock cycles.

26.6.5   ICM Automatic Monitoring Mode
         The ASCD bit of the CFG register is used to activate the ICM Automatic Mode. When CFG.ASCD is set,
         the ICM performs the following actions:
           • The ICM controller passes through the Main List once with CDWBN bit in RCFGn at 0 (i.e., Write
             Back activated) and EOM bit in the RCFGn context register at 0.
           • When RCFGn.WRAP=1, the ICM controller enters active monitoring, with CDWBN bit in context
             register now set, and EOM bit in context register cleared. Writing to the CDWBN and EOM bits in
             RCFGn has no effect.




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 700
                                                          SAM D5x/E5x Family Data Sheet
                                                                            ICM - Integrity Check Monitor

26.6.6   ICM Configuration Parameters

          Transfer Type                     Main   RCFG                        RNEXT        Comments
                                            List
                                                   CDWBN WRAP         EOM      NEXT
          Single       Contiguous list      1 item 0      0           1        0            The Main List
          Region       of blocks                                                            contains only one
                                                                                            descriptor. The
                       Digest written to                                                    Secondary List is
                       memory                                                               empty for that
                                                                                            descriptor. The
                       Monitoring                                                           digest is
                       disabled                                                             computed and
                                                                                            saved to memory.
                       Non-contiguous       1 item 0      0           1        Secondary The Main List
                       list of blocks                                          List address contains only one
                                                                               of the       descriptor. The
                       Digest written to                                       current      Secondary List
                       memory                                                  region       describes the
                                                                               identifier   layout of the non-
                       Monitoring                                                           contiguous
                       disabled                                                             region.
                       Contiguous list      1 item 1      1           0        0            When the hash
                       of blocks                                                            computation is
                       Digest                                                               terminated, the
                       comparison                                                           digest is
                       enabled                                                              compared with
                       Monitoring                                                           the one saved in
                       enabled                                                              memory.




         © 2019 Microchip Technology Inc.                     Datasheet                    DS60001507E-page 701
                                                          SAM D5x/E5x Family Data Sheet
                                                                              ICM - Integrity Check Monitor

         ...........continued
          Transfer Type                     Main   RCFG                           RNEXT         Comments
                                            List
                                                   CDWBN WRAP         EOM         NEXT
          Multiple     Contiguous list      More   0      0           1 for the   0             ICM passes
          Regions      of blocks            than                      last, 0                   through the list
                       Digest written to    one                       otherwise                 once.
                       memory               item
                       Monitoring
                       disabled
                       Contiguous list      More   1      1 for the   0           0             ICM performs
                       of blocks            than          last, 0                               active monitoring
                                            one           otherwise                             of the regions. If a
                       Digest               item                                                mismatch occurs,
                       comparison is                                                            an interrupt is
                       enabled                                                                  raised.

                       Monitoring is
                       enabled
                       Non-contiguous       More   0      0           1           Secondary ICM performs
                       list of blocks       than                                  List address hashing and
                       Digest is written    one                                                saves digests to
                       to memory            item                                               the Hash area.
                       Monitoring is
                       disabled
                       Non-contiguous       More   1      1           0           Secondary ICM performs
                       list of blocks       than                                  List address data gathering on
                       Digest               one                                                a per region
                       comparison is        item                                               basis.
                       enabled

                       Monitoring is
                       enabled

26.6.7   Security Features
         When an undefined register access occurs, the URAD bit in the Interrupt Status Register (ISR) is set if
         unmasked. Its source is then reported in the Undefined Access Status Register (UASR). Only the first
         undefined register access is available through the UASR.URAT field.
         Several kinds of unspecified register accesses can occur:
           •   Unspecified structure member set to one detected when the descriptor is loaded
           •   Configuration register (CFG) modified during active monitoring
           •   Descriptor register (DSCR) modified during active monitoring
           •   Hash register (HASH) modified during active monitoring
           •   Write-only register read access
         The URAD bit and the URAT field can only be reset by writing a 1 to the CTRL.SWRST bit.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 702
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                           ICM - Integrity Check Monitor


26.7      Register Summary - ICM

 Offset        Name        Bit Pos.

                              7:0                         BBC[3:0]                               SLBDIS     EOMDIS      WBDIS
                             15:8                 UALGO[2:0]              UIHASH                           DUALBUFF     ASCD
 0x00          CFG
                             23:16
                             31:24
                              7:0                        REHASH[3:0]                             SWRST      DISABLE     ENABLE
                             15:8                         RMEN[3:0]                                  RMDIS[3:0]
 0x04          CTRL
                             23:16
                             31:24
                              7:0                                                                                       ENABLE
                             15:8                        RMDIS[3:0]                                RAWRMDIS[3:0]
 0x08           SR
                             23:16
                             31:24
 0x0C
   ...       Reserved
 0x0F
                              7:0                         RDM[3:0]                                    RHC[3:0]
                             15:8                         RWC[3:0]                                    RBE[3:0]
 0x10           IER
                             23:16                        RSU[3:0]                                    REC[3:0]
                             31:24                                                                                      URAD
                              7:0                         RDM[3:0]                                    RHC[3:0]
                             15:8                         RWC[3:0]                                    RBE[3:0]
 0x14           IDR
                             23:16                        RSU[3:0]                                    REC[3:0]
                             31:24                                                                                      URAD
                              7:0                         RDM[3:0]                                    RHC[3:0]
                             15:8                         RWC[3:0]                                    RBE[3:0]
 0x18           IMR
                             23:16                        RSU[3:0]                                    REC[3:0]
                             31:24                                                                                      URAD
                              7:0                         RDM[3:0]                                    RHC[3:0]
                             15:8                         RWC[3:0]                                    RBE[3:0]
 0x1C           ISR
                             23:16                        RSU[3:0]                                    REC[3:0]
                             31:24                                                                                      URAD
                              7:0                                                                           URAT[2:0]
                             15:8
 0x20          UASR
                             23:16
                             31:24
 0x24
   ...       Reserved
 0x2F
                              7:0            DASA[1:0]
                             15:8                                             DASA[9:2]
 0x30          DSCR
                             23:16                                           DASA[17:10]
                             31:24                                           DASA[25:18]




          © 2019 Microchip Technology Inc.                             Datasheet                           DS60001507E-page 703
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                         ICM - Integrity Check Monitor

...........continued

  Offset               Name    Bit Pos.

                                  7:0     HASA[0:0]
                                 15:8                                       HASA[8:1]
   0x34                HASH
                                 23:16                                      HASA[16:9]
                                 31:24                                     HASA[24:17]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x38            UIHVALx0
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x3C            UIHVALx1
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x40            UIHVALx2
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x44            UIHVALx3
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x48            UIHVALx4
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x4C            UIHVALx5
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x50            UIHVALx6
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]
                                  7:0                                        VAL[7:0]
                                 15:8                                        VAL[15:8]
   0x54            UIHVALx7
                                 23:16                                      VAL[23:16]
                                 31:24                                      VAL[31:24]




26.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to 22.5.8 Register Access Protection.




              © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 704
                                                 SAM D5x/E5x Family Data Sheet
                                                                     ICM - Integrity Check Monitor

Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
Enable-protection is denoted by the "Enable-Protected" property in each individual register description.
Related Links
26.6.3 Region Descriptor Structure




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 705
                                                                SAM D5x/E5x Family Data Sheet
                                                                                 ICM - Integrity Check Monitor

26.8.1         Configuration Register

               Name:       CFG
               Offset:     0x00
               Reset:      0x0
               Property:   -


         Bit        31            30               29      28           27          26          25           24


   Access
    Reset


         Bit        23            22               21      20           19          18          17           16


   Access
    Reset


         Bit        15            14               13      12           11          10           9               8
                             UALGO[2:0]                  UIHASH                              DUALBUFF       ASCD
   Access                                                                                                    R/W
    Reset           0              0                0      0                                     0               0


         Bit        7              6                5      4            3           2            1               0
                                        BBC[3:0]                                  SLBDIS      EOMDIS       WBDIS
   Access          R/W            R/W              R/W    R/W                      R/W          R/W          R/W
    Reset           0              0                0      0                        0            0               0


               Bits 15:13 – UALGO[2:0] User SHA Algorithm
               Value       Name              Description
               0           SHA1              SHA1 algorithm processed
               1           SHA256            SHA256 algorithm processed
               4           SHA224            SHA224 algorithm processed
               Other       -                 Reserved

               Bit 12 – UIHASH User Initial Hash Value
               Value       Description
               0           The secure hash standard provides the initial hash value.
               1           The initial hash value is programmable. Field UALGO provides the SHA algorithm. The
                           ALGO field of the RCFGn structure member has no effect.

               Bit 9 – DUALBUFF Dual Input Buffer
               Value      Description
               0          Dual Input buffer mode is disabled.
               1          Dual Input buffer mode is enabled (Better performances, higher bandwidth required on
                          system bus).

               Bit 8 – ASCD Automatic Switch To Compare Digest




           © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 706
                                                   SAM D5x/E5x Family Data Sheet
                                                                      ICM - Integrity Check Monitor

 Value        Description
 0            Automatic mode is disabled.
 1            When this mode is enabled, the ICM controller automatically switches to active monitoring
              after the first Main List pass. Both CDWBN and WBDIS bits have no effect. A '1' must be
              written to the End of Monitoring bit in the Region Configuration register (RCFG.EOM) to
              terminate the monitoring.

Bits 7:4 – BBC[3:0] Bus Burden Control
This field is used to control the burden of the ICM system bus. The number of system clock cycles
between the end of the current processing and the next block transfer is set to 2BBC. Up to 32768 cycles
can be inserted.

Bit 2 – SLBDIS Secondary List Branching Disable
Value      Description
0          Branching to the Secondary List is permitted.
1          Branching to the Secondary List is forbidden. The NEXT field of the RNEXT structure
           member has no effect and is always considered as zero.

Bit 1 – EOMDIS End of Monitoring Disable
Value      Description
0          End of Monitoring is permitted.
1          End of Monitoring is forbidden. The EOM bit of the RCFG structure member has no effect.

Bit 0 – WBDIS Write Back Disable
1:
When the Automatic Switch to Compare Digest bit of this register (CFG.ASCD) is written to '1', this bit
value has no effect.
 Value     Description
 0         Write Back Operations are permitted.
 1         Write Back Operations are forbidden: Context register CDWBN bit is internally set to '1' and
           cannot be modified by a linked list element. The CDWBN bit of the RCFG structure member
           has no effect.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 707
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                        ICM - Integrity Check Monitor

26.8.2         Control Register

               Name:        CTRL
               Offset:      0x04
               Property:    -


         Bit        31             30                 29       28            27            26                25           24


   Access
    Reset


         Bit        23             22                 21       20            19            18                17           16


   Access
    Reset


         Bit        15             14                 13       12            11            10                9            8
                                         RMEN[3:0]                                              RMDIS[3:0]
   Access            W             W                  W        W             W             W                 W            W
    Reset


         Bit         7             6                  5        4             3              2                1            0
                                        REHASH[3:0]                                      SWRST         DISABLE        ENABLE
   Access            W             W                  W        W                           W                 W            W
    Reset                                                                                                    0            0


               Bits 15:12 – RMEN[3:0] Region Monitoring Enable
               Value       Description
               0           No effect.
               1           When bit RMEN[i] is written to '1', the monitoring of region with identifier i is activated.

               Bits 11:8 – RMDIS[3:0] Region Monitoring Disable
               Value       Description
               0           No effect.
               1           When REHASH[i] is written to '1', Region i digest is re-computed. This bit is only available
                           when region monitoring is disabled.

               Bits 7:4 – REHASH[3:0] Recompute Internal Hash
               Value       Description
               0           No effect.
               1           When REHASH[i] is written to '1', Region i digest is re-computed. This bit is only available
                           when region monitoring is disabled.

               Bit 2 – SWRST Software Reset
               Value      Description
               0          No effect.
               1          Resets the ICM controller.

               Bit 1 – DISABLE ECM Disable




           © 2019 Microchip Technology Inc.                          Datasheet                               DS60001507E-page 708
                                                     SAM D5x/E5x Family Data Sheet
                                                                         ICM - Integrity Check Monitor

 Value        Description
 0            No effect.
 1            The ICM controller is disabled. If a region is activated, the region is terminated.

Bit 0 – ENABLE ICM Enable
Value      Description
0          No effect.
1          The ICM controller is activated.




© 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 709
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                   ICM - Integrity Check Monitor

26.8.3         Status Register

               Name:       SR
               Offset:     0x08
               Property:   Read-Only


         Bit        31           30                29       28           27           26           25            24


   Access
    Reset


         Bit        23           22                21       20           19           18           17            16


   Access
    Reset


         Bit        15           14                13       12           11           10            9            8
                                      RMDIS[3:0]                                       RAWRMDIS[3:0]
   Access           R             R                R        R            R             R            R            R
    Reset            0            0                0        0             0            0            0            0


         Bit         7            6                5        4             3            2            1            0
                                                                                                              ENABLE
   Access                                                                                                        R
    Reset                                                                                                        0


               Bits 15:12 – RMDIS[3:0] Region Monitoring Disabled Status
               Value       Description
               0           Region i is being monitored (occurs after integrity check value has been calculated and
                           written to Hash area).
               1           Region i is not being monitored.

               Bits 11:8 – RAWRMDIS[3:0] Region Monitoring Disabled Raw Status
               Value       Description
               0           Region i monitoring has been activated by writing a 1 in RMEN[i] of CTRL
               1           Region i monitoring has been deactivated by writing a 1 in RMDIS[i] of CTRL

               Bit 0 – ENABLE ICM Controller Enable Register
               Value      Description
               0          ICM controller is disabled.
               1          ICM controller is activated.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 710
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                       ICM - Integrity Check Monitor

26.8.4         Interrupt Enable Register

               Name:        IER
               Offset:      0x10
               Reset:       0x00000000
               Property:    Write-Only


         Bit        31            30              29          28            27            26              25           24
                                                                                                                     URAD
   Access                                                                                                              W
    Reset                                                                                                              0


         Bit        23            22              21          20            19            18              17           16
                                       RSU[3:0]                                                REC[3:0]
   Access            W             W              W            W            W             W               W            W
    Reset            0             0              0            0             0             0              0            0


         Bit        15            14              13          12            11            10              9            8
                                       RWC[3:0]                                                RBE[3:0]
   Access            W             W              W            W            W             W               W            W
    Reset            0             0              0            0             0             0              0            0


         Bit         7             6              5            4             3             2              1            0
                                       RDM[3:0]                                                RHC[3:0]
   Access            W             W              W            W            W             W               W            W
    Reset            0             0              0            0             0             0              0            0


               Bit 24 – URAD Undefined Register Access Detection Interrupt Enable
               0: No effect
               1: The Undefined Register Access interrupt is enabled.

               Bits 23:20 – RSU[3:0] Region Status Updated Interrupt Enable
               0: No effect
               1: When RSU[i] is written to ‘1’, the region i Status Updated interrupt is enabled.

               Bits 19:16 – REC[3:0] Region End bit Condition Detected Interrupt Enable
               0: No effect
               1: When REC[i] is written to ‘1’, the region i End bit Condition interrupt is enabled.

               Bits 15:12 – RWC[3:0] Region Wrap Condition detected Interrupt Enable
               0: No effect
               1: When RWC[i] is written to ‘1’, the Region i Wrap Condition interrupt is enabled.

               Bits 11:8 – RBE[3:0] Region Bus Error Interrupt Enable
               Value       Description
               0           No effect.
               1           When RBE[i] is written to '1', the Region i Bus Error interrupt is enabled.

               Bits 7:4 – RDM[3:0] Region Digest Mismatch Interrupt Enable




           © 2019 Microchip Technology Inc.                         Datasheet                              DS60001507E-page 711
                                                    SAM D5x/E5x Family Data Sheet
                                                                       ICM - Integrity Check Monitor

 Value        Description
 0            No effect.
 1            When RDM[i] is written to '1', the Region i Digest Mismatch interrupt is enabled.

Bits 3:0 – RHC[3:0] Region Hash Completed Interrupt Enable
Value       Description
0           No effect.
1           When RHC[i] is written to '1', the Region i Hash Completed interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 712
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                       ICM - Integrity Check Monitor

26.8.5         Interrupt Disable Register

               Name:        IDR
               Offset:      0x14
               Property:    Write-Only


         Bit        31            30              29          28            27            26              25          24
                                                                                                                    URAD
   Access                                                                                                             W
    Reset


         Bit        23            22              21          20            19            18              17          16
                                       RSU[3:0]                                                REC[3:0]
   Access            W            W               W           W             W             W               W           W
    Reset


         Bit        15            14              13          12            11            10              9           8
                                       RWC[3:0]                                                RBE[3:0]
   Access            W            W               W           W             W             W               W           W
    Reset


         Bit         7             6              5            4             3             2              1           0
                                       RDM[3:0]                                                RHC[3:0]
   Access            W            W               W           W             W             W               W           W
    Reset


               Bit 24 – URAD Undefined Register Access Detection Interrupt Disable
               Value      Description
               0          No effect.
               1          Undefined Register Access Detection interrupt is disabled.

               Bits 23:20 – RSU[3:0] Region Status Updated Interrupt Disable
               Value       Description
               0           No effect.
               1           When RSU[i] is written to '1', the region i Status Updated interrupt is disabled.

               Bits 19:16 – REC[3:0] Region End bit Condition detected Interrupt Disable
               Value       Description
               0           No effect.
               1           When REC[i] is written to '1', the region i End bit Condition interrupt is disabled.

               Bits 15:12 – RWC[3:0] Region Wrap Condition Detected Interrupt Disable
               Value       Description
               0           No effect.
               1           When RWC[i] is written to '1', the Region i Wrap Condition interrupt is disabled.

               Bits 11:8 – RBE[3:0] Region Bus Error Interrupt Disable




           © 2019 Microchip Technology Inc.                         Datasheet                             DS60001507E-page 713
                                                     SAM D5x/E5x Family Data Sheet
                                                                         ICM - Integrity Check Monitor

 Value        Description
 0            No effect.
 1            When RBE[i] is written to '1', the Region i Bus Error interrupt is disabled.

Bits 7:4 – RDM[3:0] Region Digest Mismatch Interrupt Disable
Value       Description
0           No effect.
1           When RDM[i] is written to '1', the Region i Digest Mismatch interrupt is disabled.

Bits 3:0 – RHC[3:0] Region Hash Completed Interrupt Disable
Value       Description
0           No effect.
1           When RHC[i] is written to '1', the Region i Hash Completed interrupt is disabled.




© 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 714
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                       ICM - Integrity Check Monitor

26.8.6         Interrupt Mask Register

               Name:        IMR
               Offset:      0x18
               Reset:       0x00000000
               Property:    Read-Only


         Bit        31            30              29          28            27            26                25          24
                                                                                                                      URAD
   Access                                                                                                               R
    Reset                                                                                                               0


         Bit        23            22              21          20            19            18                17          16
                                       RSU[3:0]                                                  REC[3:0]
   Access            R             R              R            R             R            R                 R           R
    Reset            0             0              0            0             0             0                0           0


         Bit        15            14              13          12            11            10                9           8
                                       RWC[3:0]                                                  RBE[3:0]
   Access            R             R              R            R             R            R                 R           R
    Reset            0             0              0            0             0             0                0           0


         Bit         7             6              5            4             3             2                1           0
                                       RDM[3:0]                                                  RHC[3:0]
   Access            R             R              R            R             R            R                 R           R
    Reset            0             0              0            0             0             0                0           0


               Bit 24 – URAD Undefined Register Access Detection Interrupt Mask
               Value      Description
               0          The interrupt is disabled.
               1          The interrupt is enabled.

               Bits 23:20 – RSU[3:0] Region Status Updated Interrupt Mask
               Value       Description
               0           When RSU[i] is reading '0', the interrupt is disabled for region i.
               1           When RSU[i] is reading '1', the interrupt is enabled for region i.

               Bits 19:16 – REC[3:0] Region End bit Condition Detected Interrupt Mask
               Value       Description
               0           When REC[i] is reading '0', the interrupt is disabled for region i.
               1           When REC[i] is reading '1', the interrupt is enabled for region i.

               Bits 15:12 – RWC[3:0] Region Wrap Condition Detected Interrupt Mask
               Value       Description
               0           When RWC[i] is reading '0', the interrupt is disabled for region i.
               1           When RWC[i] is reading '1', the interrupt is enabled for region i.

               Bits 11:8 – RBE[3:0] Region Bus Error Interrupt Mask




           © 2019 Microchip Technology Inc.                         Datasheet                               DS60001507E-page 715
                                                     SAM D5x/E5x Family Data Sheet
                                                                          ICM - Integrity Check Monitor

 Value        Description
 0            When RBE[i] is reading '0', the interrupt is disabled for region i.
 1            When RBE[i] is reading '1', the interrupt is enabled for region i.

Bits 7:4 – RDM[3:0] Region Digest Mismatch Interrupt Mask
Value       Description
0           When RDM[i] is reading '0', the interrupt is disabled for region i.
1           When RDM[i] is reading '1', the interrupt is enabled for region i.

Bits 3:0 – RHC[3:0] Region Hash Completed Interrupt Mask
Value       Description
0           When RHC[i] is reading '0', the interrupt is disabled for region i.
1           When RHC[i] is reading '1', the interrupt is enabled for region i.




© 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 716
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                   ICM - Integrity Check Monitor

26.8.7         Interrupt Status Register

               Name:       ISR
               Offset:     0x1C
               Reset:      0x0
               Property:   Read-Only


         Bit        31           30              29         28           27           26              25          24
                                                                                                                URAD
   Access                                                                                                         R
    Reset                                                                                                         0


         Bit        23           22              21         20           19           18              17          16
                                      RSU[3:0]                                             REC[3:0]
   Access           R             R              R          R             R           R               R           R
    Reset            0            0              0           0            0           0               0           0


         Bit        15           14              13         12           11           10              9           8
                                      RWC[3:0]                                             RBE[3:0]
   Access           R             R              R          R             R           R               R           R
    Reset            0            0              0           0            0           0               0           0


         Bit         7            6              5           4            3           2               1           0
                                      RDM[3:0]                                             RHC[3:0]
   Access           R             R              R          R             R           R               R           R
    Reset            0            0              0           0            0           0               0           0


               Bit 24 – URAD Undefined Register Access Detection Status
               The URAD bit is only reset by the SWRST bit in the CTRL register.
               The Undefined Register Access Trace bit field in the Undefined Access Status Register (UASR.URAT)
               indicates the unspecified access type.
                Value      Description
                0          No undefined register access has been detected since the last SWRST.
                1          At least one undefined register access has been detected since the last SWRST.

               Bits 23:20 – RSU[3:0] Region Status Updated Detected
               RSU[i] is set when a region status updated condition is detected.

               Bits 19:16 – REC[3:0] Region End bit Condition Detected
               REC[i] is set when an end bit condition is detected.

               Bits 15:12 – RWC[3:0] Region Wrap Condition Detected
               RWC[i] is set when a wrap condition is detected.

               Bits 11:8 – RBE[3:0] Region Bus Error
               RBE[i] is set when a bus error is detected while hashing memory region i.




           © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 717
                                                  SAM D5x/E5x Family Data Sheet
                                                                     ICM - Integrity Check Monitor

Bits 7:4 – RDM[3:0] Region Digest Mismatch
RDM[i] is set when there is a digest comparison mismatch between the hash value of region i and the
reference value located in the Hash Area.

Bits 3:0 – RHC[3:0] Region Hash Completed
RHC[i] is set when the ICM has completed the region with identifier i.




© 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 718
                                                            SAM D5x/E5x Family Data Sheet
                                                                              ICM - Integrity Check Monitor

26.8.8         Undefined Access Status Register

               Name:       UASR
               Offset:     0x20
               Reset:      0x0
               Property:   Read-Only


         Bit        31           30           29       28          27            26           25           24


   Access
    Reset


         Bit        23           22           21       20          19            18           17           16


   Access
    Reset


         Bit        15           14           13       12           11           10            9            8


   Access
    Reset


         Bit        7             6           5        4            3            2             1            0
                                                                                           URAT[2:0]
   Access                                                                        R            R             R
    Reset                                                                        0             0            0


               Bits 2:0 – URAT[2:0] Undefined Register Access Trace
               Only the first Undefined Register Access Trace is available through the URAT field.
               The URAT field is only reset by the Software Reset bit in the Control register (CTRL.SWRST).
                Value       Name                           Description
                0           UNSPEC_STRUCT_MEMBER Unspecified structure member set to '1' detected when the
                                                           descriptor is loaded.
                1           ICM_CFG_MODIFIED               CFG modified during active monitoring.
                2           ICM_DSCR_MODIFIED              DSCR modified during active monitoring.
                3           ICM_HASH_MODIFIED              HASH modified during active monitoring
                4           READ_ACCESS                    Write-only register read access
                                                      Only the first Undefined Register Access Trace is available
                                                      through the URAT field.
                                                      The URAT field is only reset by the SWRST bit in the CTRL
                                                      register.




           © 2019 Microchip Technology Inc.                 Datasheet                          DS60001507E-page 719
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                        ICM - Integrity Check Monitor

26.8.9         Descriptor Area Start Address Register

               Name:         DSCR
               Offset:       0x30
               Reset:        0x0
               Property:     -


         Bit        31                30         29            28                 27       26        25           24
                                                                    DASA[25:18]
   Access           R/W               R/W       R/W           R/W                R/W      R/W        R/W         R/W
    Reset            0                 0         0             0                  0        0          0           0


         Bit        23                22         21            20                 19       18        17           16
                                                                    DASA[17:10]
   Access           R/W               R/W       R/W           R/W                R/W      R/W        R/W         R/W
    Reset            0                 0         0             0                  0        0          0           0


         Bit        15                14         13            12                 11       10         9           8
                                                                     DASA[9:2]
   Access           R/W               R/W       R/W           R/W                R/W      R/W        R/W         R/W
    Reset            0                 0         0             0                  0        0          0           0


         Bit         7                 6         5             4                  3        2          1           0
                          DASA[1:0]
   Access           R/W               R/W
    Reset            0                 0


               Bits 31:6 – DASA[25:0] Descriptor Area Start Address
               The start address is a multiple of the total size of the data structure (64 bytes).




           © 2019 Microchip Technology Inc.                            Datasheet                      DS60001507E-page 720
                                                               SAM D5x/E5x Family Data Sheet
                                                                                 ICM - Integrity Check Monitor

26.8.10 Hash Area Start Address Register

            Name:         HASH
            Offset:       0x34
            Reset:        0x00000000
            Property:     -


      Bit        31           30           29           28                 27      26           25           24
                                                             HASA[24:17]
  Access        R/W           R/W          R/W          R/W                R/W    R/W          R/W          R/W
   Reset          0            0            0            0                  0      0            0            0


      Bit        23           22           21           20                 19      18           17           16
                                                              HASA[16:9]
  Access        R/W           R/W          R/W          R/W                R/W    R/W          R/W          R/W
   Reset          0            0            0            0                  0      0            0            0


      Bit        15           14           13           12                 11      10           9            8
                                                              HASA[8:1]
  Access        R/W           R/W          R/W          R/W                R/W    R/W          R/W          R/W
   Reset          0            0            0            0                  0      0            0            0


      Bit         7            6            5            4                  3      2            1            0
              HASA[0:0]
  Access        R/W
   Reset          0


            Bits 31:7 – HASA[24:0] Hash Area Start Address
            This field points at the Hash memory location. The address must be a multiple of 128 bytes.




        © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 721
                                                              SAM D5x/E5x Family Data Sheet
                                                                                ICM - Integrity Check Monitor

26.8.11 User Initial Hash Value Register

            Name:       UIHVALx
            Offset:     0x38 + x*0x04 [x=0..7]
            Reset:      0
            Property:   -


      Bit        31              30        29           28                27      26           25              24
                                                             VAL[31:24]
   Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W             R/W
    Reset        0               0          0           0                  0      0            0               0


      Bit        23              22        21           20                19      18           17              16
                                                             VAL[23:16]
   Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W             R/W
    Reset        0               0          0           0                  0      0            0               0


      Bit        15              14        13           12                11      10           9               8
                                                             VAL[15:8]
   Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W             R/W
    Reset        0               0          0           0                  0      0            0               0


      Bit        7               6          5           4                  3      2            1               0
                                                              VAL[7:0]
   Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W             R/W
    Reset        0               0          0           0                  0      0            0               0


            Bits 31:0 – VAL[31:0] Initial Hash Value
            When UIHASH bit of CFG register is set, the Initial Hash Value is user-programmable.
            To meet the desired standard, use the following example values.
            For UIHVAL0 field:

            Example                                      Comment
            0x67452301                                   SHA1 algorithm
            0xC1059ED8                                   SHA224 algorithm
            0x6A09E667                                   SHA256 algorithm

            For UIHVAL1 field:

            Example                                         Comment
            0xEFCDAB89                                      SHA1 algorithm
            0x367CD507                                      SHA224 algorithm
            0xBB67AE85                                      SHA256 algorithm

            For UIHVAL2 field:




        © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 722
                                                    SAM D5x/E5x Family Data Sheet
                                                                     ICM - Integrity Check Monitor

 Example                                          Comment
 0x98BADCFE                                       SHA1 algorithm
 0x3070DD17                                       SHA224 algorithm
 0x3C6EF372                                       SHA256 algorithm

For UIHVAL3 field:

 Example                                         Comment
 0x10325476                                      SHA1 algorithm
 0xF70E5939                                      SHA224 algorithm
 0xA54FF53A                                      SHA256 algorithm

For UIHVAL4 field:

 Example                                         Comment
 0xC3D2E1F0                                      SHA1 algorithm
 0xFFC00B31                                      SHA224 algorithm
 0x510E527F                                      SHA256 algorithm

For UIHVAL5 field:

 Example                                         Comment
 0x68581511                                      SHA224 algorithm
 0x9B05688C                                      SHA256 algorithm

For UIHVAL6 field:

 Example                                         Comment
 0x64F98FA7                                      SHA224 algorithm
 0x1F83D9AB                                      SHA256 algorithm

For UIHVAL7 field:

 Example                                         Comment
 0xBEFA4FA4                                      SHA224 algorithm
 0x5BE0CD19                                      SHA256 algorithm

Example of Initial Value for SHA-1 Algorithm

 Register Address                  Address Offset / Byte Lane
                                   0x3 / 31:24        0x2 / 23:16      0x1 / 15:8       0x0 / 7:0
 0x000 UIHVAL0                     01                 23               45               67




© 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 723
                                                  SAM D5x/E5x Family Data Sheet
                                                                   ICM - Integrity Check Monitor

...........continued
 Register Address                  Address Offset / Byte Lane
                                   0x3 / 31:24       0x2 / 23:16     0x1 / 15:8       0x0 / 7:0
 0x004 UIHVAL1                     89                ab              cd               ef
 0x008 UIHVAL2                     fe                dc              ba               98
 0x00C UIHVAL3                     76                54              32               10
 0x010 UIHVAL4                     f0                e1              d2               c3




© 2019 Microchip Technology Inc.                    Datasheet                     DS60001507E-page 724
