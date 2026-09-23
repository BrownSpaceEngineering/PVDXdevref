# 11. CMCC - Cortex M Cache Controller

*Source: `Atmel-SAMD51.pdf`, pages 81-102 — SAMD51 family datasheet*

                                                       SAM D5x/E5x Family Data Sheet
                                                                   CMCC - Cortex M Cache Controller


11.    CMCC - Cortex M Cache Controller

11.1   Overview
       The Cortex M Cache Controller provides an L1 cache to the Cortex M CPU. The CMCC sits transparently
       between the CPU and the cache leading to improved performance.
       The CMCC interfaces with the CPU through the AHB, and is connected to the APB bus interface for its
       configuration.



11.2   Features
         •   Physically addressed and physically tagged
         •   L1 data and instruction cache set to 4 KB
         •   L1 cache line size set to 16 Bytes
         •   L1 cache integrates 32-bit bus master interface
         •   Unified 4-Way set associative cache architecture
         •   Lock-Down feature, which allows cached to be locked per way
         •   Write through cache operations, read allocate
         •   Configurable as data and instruction Tightly Coupled Memory (TCM)
         •   Round Robin victim selection policy
         •   Event Monitoring, with one programmable 32-bit counter
         •   Cache Interface includes cache maintenance operations registers




       © 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 81
                                                           SAM D5x/E5x Family Data Sheet
                                                                             CMCC - Cortex M Cache Controller


11.3   Block Diagram
       Figure 11-1. CMCC Block Diagram

                                                           CM4F



                                                      Cortex M Interface


                                          Cache
                                                                               METADATA RAM
                                         Controller
                                                         RAM
                                                       Interface               DATA RAM


                                     Registers                                TAG RAM
          APB                        Interface
       interface

                                                      Memory Interface



                                                        High-Speed
                                                        Bus Matrix


       Figure 11-2. CMCC Organization

                                                                                                  Line ‘n’

                                                                    Line 0                  4     4     4     4
                                                                                          Bytes Bytes Bytes Bytes
                                                                    Line 1
                                                                    Line 2
                                                                    Line 3
             Base Address + 0x00000000
                                                                    Line 4
                                           WAY 0
                                                                      ...
             Base Address + 0x00000400                                …..
                                           WAY 1                     …….
             Base Address + 0x00000800                             Line 63
                                           WAY 2
             Base Address + 0x00000C00
                                           WAY 3




       © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 82
                                                           SAM D5x/E5x Family Data Sheet
                                                                       CMCC - Cortex M Cache Controller


11.4     Signal Description
         Not applicable.


11.5     Product Dependencies
         Not applicable.

11.5.1   I/O Lines
         Not applicable.

11.5.2   Power Management
         The CMCC will continue to function as long as the CPU is not sleeping and CMCC is enabled.

11.5.3   Clocks
         Not applicable.

11.5.4   DMA
         Not applicable.

11.5.5   Interrupts
         Not applicable.

11.5.6   Events
         Not applicable.

11.5.7   Debug Operation
         When the CPU is halted in debug mode, the CMCC is halted. Any read access by the debugger in
         cached zones are not cached.

11.5.8   Register Access Protection
         Not applicable.

11.5.9   Analog Connections
         Not applicable.


11.6     Functional Description

11.6.1   Principle of Operation

11.6.2   Initialization and Normal Operation
         On reset, the cache controller data entries are all invalidated, and the cache is disabled. The cache is
         transparent to processor operations. The cache controller is activated through the use of its configuration
         registers. The configuration interface is memory mapped in the APB bus.
         Use the following sequence to enable the cache controller:
           • Verify that the CMCC is disabled, reading the value of the SR.CSTS.
           • Enable the CMCC by writing '1' in CTRL.CEN. The MODULE is disabled by writing a '0' in
             CTRL.CEN.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 83
                                                            SAM D5x/E5x Family Data Sheet
                                                                         CMCC - Cortex M Cache Controller

11.6.3   Change Cache Size
         It is possible to change the cache size by writing to the Cache Size Configured By Software bits in the
         Cache Configuration register (CFG.CSIZESW).
         Use the following sequence to change the cache size:
           • Disable the CMCC controller by writing a zero to the Cache Controller Enable bit in the Cache
             Control register (CTRL.CEN=0).
           • Check the Cache Controller Status bit in the Cache Status register to verify that the CMCC is
             successfully disabled (SR.CSTS=0).
           • Change CFG.CSIZESW to its new value.
           • Enable the CMCC by writing CTRL.CEN=1.

11.6.4   Data Cache Disable
         The Instructions alone can be cached by disabling the Data cache, as described in the following steps:
           1.   Disable the cache controller by writing a ‘0’ to CTRL.CEN.
           2.   Check SR.CSTS to verify whether the CMCC is successfully disabled.
           3.   Write CFG.DCDIS = 1.
           4.   Enable the CMCC by writing CTRL.CEN = 1.

11.6.5   Instruction Cache Disable
         The Data alone can be cached by disabling the Instruction cache, as described in the following steps:
           1.   Disable the cache controller by writing CTRL.CEN = 0.
           2.   Check SR.CSTS to verify that the CMCC is successfully disabled.
           3.   Write CFG.ICDIS = 1.
           4.   Enable the CMCC by writing CTRL.CEN = 1.

11.6.6   Cache Load and Lock
         It is possible to lock a specific way for code optimization by writing the Lock Way register
         (LCKWAY.LCKWAY). The locked way will not be updated by the CMCC as part of cache operations.
         The load and lock mechanism can be implemented to use cache memory in a deterministic way. Follow
         these steps to load and lock a way:
           1. Disable cache controller by clearing the CTRL.CEN bit.
           2. Invalidate the desired WAY line by line. This will reset the round robin algorithm of the invalidated
               line, that will become eligible for the next load operation.
           3. Disable the Instruction cache, but keep the Data cache enabled.
           4. Enable the cache by setting the CTRL.CEN bit.
           5. Place the respective piece of code and/or data to the corresponding WAY due to simple LOAD
               operations. Loading the piece of code and/or data will force the cache to refill the previous
               invalidated line in the right way. No need to load all the bytes of the line, only the first byte. The
               cache will automatically refill the complete line.
           6. Lock the specific WAY by setting LCKWAY.LCKWAY[3:0].
           7. Re-enable the instruction cache. The locked WAY is now loaded and ready to operate. The
               remaining WAYS can be used as I-cache or D-cache as required.




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 84
                                                           SAM D5x/E5x Family Data Sheet
                                                                        CMCC - Cortex M Cache Controller

11.6.7   Tightly Coupled Memory
         Users can use a part of the cache as Tightly Coupled Memory (TCM). The cache size is determined by
         the Cache Size Configuration by Software bits in the Cache Configuration register (CFG.CSIZESW). The
         relation between cache and TCM is as given below:
         TCM size = maximum Cache size - configured Cache size.
         The TCM start address can be obtained from the product memory mapping. The cache memory starts
         first from the address followed by the TCM memory. Size of the Way is fixed and the number of ways
         varies according to the available size for the cache memory. For additional information, refer to the
         section Product Memory Mapping.
         Table 11-1. TCM Sizes

                     Max. Cache                         Configured Cache                           TCM Size
                         4 KB                                  4 KB                                  0 KB
                         4 KB                                  1 KB                                  3 KB
                         4 KB                                  2 KB                                  2 KB
                         4 KB                                  0 KB                                  4 KB

         The TCM is also accessible in its maximum size when the CMCC is disabled. The TCM does not need to
         be locked in order to operate.
         Note: Writing into the cache DATA RAM region through the CPU can overwrite the valid cache lines.
         This can result in data corruption when the cache controller is accessing the data for cache transactions.
         Access the DATA RAM region only after configuring it as TCM.

11.6.8   Cache Maintenance

11.6.8.1 Cache Invalidate by Line Operation
         When an invalidate by line command is issued, the CMCC resets the valid bit information of the decoded
         cache line. As the line is no longer valid, the replacement counter points to that line.
           • Disable the cache controller by writing a zero to the Cache Controller Enable bit in the Cache Control
             register (CTRL.CEN).
           • Check SR.CSTS to verify that the CMCC is successfully disabled.
           • Perform an invalidate by line by writing the set {index,way} in the Cache Maintenance 1 register
             (MAINT1.INDEX, MAINT1.WAY).
           • Enable the CMCC by writing a '1' to CTRL.CEN.
11.6.8.2 Cache Invalidate All Operation
         Use the following sequence to invalidate all cache entries.
           • Disable the cache controller by writing a zero to the Cache Enable bit in the Cache Control register
             (CTRL.CEN).
           • Check SR.CSTS to verify that the CMCC is successfully disabled.
           • Perform a full invalidate operation by writing a '1' to the Cache Controller Invalidate All bit in the
             Cache Maintenance 0 register (MAINT0.INVALL).
           • Enable the CMCC by writing a '1' to CTRL.CEN.




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 85
                                                           SAM D5x/E5x Family Data Sheet
                                                                        CMCC - Cortex M Cache Controller

11.6.9   Cache Performance Monitoring
         The Cortex M cache controller includes a programmable monitor/32-bit counter. The monitor can be
         configured to count the number of clock cycles, the number of data hit or the number of instruction hit.
         It is important to know that the Cortex-M4 processor prefetches instructions ahead of execution. It
         performs only 32-bit read access on the Instruction Bus, which means:
            • One arm instruction is fetched per bus access
            • Two thumb instructions are fetched per bus access
         As a consequence, two thumb instructions (e.g., NOP) need one bus access, which results in the HIT
         counter incrementing by 1.
         Use the following sequence to activate the counter:
           • Configure the monitor counter by writing the MCFG.MODE.
                – CYCLE_COUNT is used to increment the counter along with the program counter, to count the
                  number of cycles.
                – IHIT_COUNT is the instruction Hit counter, which increments the counter when there is a hit for
                  the instruction in the cache.
                – DHIT_COUNT is the data Hit counter which increments the counter when there is a hit for the
                  data in the cache.
           • Enable the counter by writing a '1' to the Cache Controller Monitor Enable bit in the Cache Monitor
             Enable register (MEN.MENABLE).
           • If required, reset the counter by writing a '1' to the Cache Controller Software Reset bit in the Cache
             Monitor Control register (MCTRL.SWRST).
           • Check the value of the monitor counter by reading the MSR.EVENT_CNT bit field.



11.7     DEBUG Mode
         In Debug mode, TAG and METADATA RAM blocks content is read/written through the AHB bus interface
         if the CMCC is disabled. When the CMCC is enabled, the TAG and METADATA RAM blocks are non
         readable.
         Debug access has the same R/W properties as the CPU access for the DATA RAM block.
         The TAG, METADATA and DATA RAM blocks' R/W properties are summarized in RAM Properties.
         Use the following sequence to perform read access with the Debugger to the three RAM blocks:
           • Disable the cache controller by writing a zero to the Cache Controller Enable bit in the Cache Control
             register (CTRL.CEN).
           • Check the Cache Controller Status bit in the Cache Status register (SR.CSTS) to verify that the
             CMCC is successfully disabled.
           • Perform a read or write access through Debugger:
                – @ CMCC_AHB_ADDR for DATA RAM,
                – @ CMCC_AHB_ADDR_TAG for TAG RAM,
                – @ CMCC_AHB_ADDR_MTDATA for METADATA RAM.
           • If a write access has been performed in the TAG, METADATA, or DATA RAM in the cache section, an
             invalid operation must be performed before re-enabling the CMCC.
         Related Links
         11.8 RAM Properties




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 86
                                                         SAM D5x/E5x Family Data Sheet
                                                                     CMCC - Cortex M Cache Controller


11.8   RAM Properties
       The following table shows the different access properties of the three RAM blocks, according the different
       modes described in the previous chapters.
       Table 11-2. Access to RAM

        Access Condition                  DATA RAM                        TAG RAM             METADATARAM
        CPU access when CMCC              R/W                             no R/W - hardfault no R/W - hardfault
        DISABLED
        CPU access when CMCC              CACHE section configured: R/    no R/W - hardfault no R/W - hardfault
        ENABLED                           W(1)
                                          TCM section configured: R/W

        Debugger access when              R/W                             R/W                 R/W
        CMCC DISABLED
        Debugger access when              CACHE section configured: R/    no R/W              no R/W
        CMCC ENABLED                      W(1)
                                          TCM section configured: R/W

       Note:
        1. A write operation in this zone can corrupt the coherency of the cache. An invalidate operation may
             be needed.
       Related Links
       11.7 DEBUG Mode




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 87
                                                              SAM D5x/E5x Family Data Sheet
                                                                              CMCC - Cortex M Cache Controller


11.9      Register Summary

 Offset        Name        Bit Pos.

                              7:0     LCKDOWN   WAYNUM[1:0]             RRP        LRUP   RANDP      GCLK             AP
                             15:8                                    CLSIZE[2:0]                   CSIZE[2:0]
 0x00          TYPE
                             23:16
                             31:24
                              7:0                     CSIZESW[2:0]                        DCDIS      ICDIS
                             15:8
 0x04          CFG
                             23:16
                             31:24
                              7:0                                                                                 CEN
                             15:8
 0x08          CTRL
                             23:16
                             31:24
                              7:0                                                                                 CSTS
                             15:8
 0x0C           SR
                             23:16
                             31:24
                              7:0                                                           LCKWAY[3:0]
                             15:8
 0x10         LCKWAY
                             23:16
                             31:24
 0x14
   ...       Reserved
 0x1F
                              7:0                                                                                INVALL
                             15:8
 0x20         MAINT0
                             23:16
                             31:24
                              7:0                INDEX[3:0]
                             15:8                                                            INDEX[7:4]
 0x24         MAINT1
                             23:16
                             31:24               WAY[3:0]
                              7:0                                                                         MODE[1:0]
                             15:8
 0x28          MCFG
                             23:16
                             31:24
                              7:0                                                                               MENABLE
                             15:8
 0x2C          MEN
                             23:16
                             31:24
                              7:0                                                                                SWRST
                             15:8
 0x30         MCTRL
                             23:16
                             31:24




          © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 88
                                                 SAM D5x/E5x Family Data Sheet
                                                           CMCC - Cortex M Cache Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0                 EVENT_CNT[7:0]
                                 15:8                 EVENT_CNT[15:8]
   0x34                MSR
                                 23:16               EVENT_CNT[23:16]
                                 31:24               EVENT_CNT[31:24]




11.10          Register Description




              © 2019 Microchip Technology Inc.   Datasheet                   DS60001507E-page 89
                                                                SAM D5x/E5x Family Data Sheet
                                                                             CMCC - Cortex M Cache Controller

11.10.1 Cache Type

           Name:        TYPE
           Offset:      0x00
           Reset:       0x000012D2
           Property:    R


     Bit        31            30             29            28           27            26        25              24


  Access
   Reset


     Bit        23            22             21            20           19            18        17              16


  Access
   Reset


     Bit        15            14             13            12           11            10         9              8
                                                       CLSIZE[2:0]                           CSIZE[2:0]
  Access                                         R         R            R             R          R              R
   Reset                                         0         1            0              0         1              0


     Bit         7             6                 5         4            3              2         1              0
             LCKDOWN               WAYNUM[1:0]            RRP          LRUP          RANDP     GCLK             AP
  Access         R             R                 R         R            R             R          R              R
   Reset         1             1                 0         1            0              0         1              0


           Bits 13:11 – CLSIZE[2:0] Cache Line Size
           This field configures the Cache Line Size.
            Value       Name                          Description
            0x2         CLSIZE_16B                    Cache Line Size is 16 bytes
            0x3-0x7 -                                 Reserved

           Bits 10:8 – CSIZE[2:0] Cache Size
           This bit field configures the cache size.
            Value        Name                                   Description
            0x0          CSIZE_1KB                              Cache Size is 1 KB
            0x1          CSIZE_2KB                              Cache Size is 2 KB
            0x2          CSIZE_4KB                              Cache Size is 4 KB
            0x3-0x7 -                                           Reserved

           Bit 7 – LCKDOWN Lock Down Supported
           Writing a '0' to this bit disables the Lock Down feature.
           Writing a '1' to this bit enables the Lock Down feature.
           Value         Description
           0             Lock Down feature is not supported.
           1             Lock Down feature is supported.




       © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 90
                                                    SAM D5x/E5x Family Data Sheet
                                                                CMCC - Cortex M Cache Controller

Bits 6:5 – WAYNUM[1:0] Number of Way
This bit field configures the mapping of the cache.
 Value        Name                              Description
 0x0          DMAPPED                           Direct Mapped Cache
 0x1          ARCH2WAY                          2-WAY set associative
 0x2          ARCH4WAY                          4-WAY set associative
 0x3          ARCH8WAY                          8-WAY set associative

Bit 4 – RRP Round Robin Policy Supported
Writing a '0' to this bit disables Round Robin Policy.
Writing a '1' to this bit enables Round Robin Policy.
Value         Description
0             Round Robin Policy is disabled.
1             Round Robin Policy is enabled.

Bit 3 – LRUP Least Recently Used Policy Supported
Writing a '0' to this bit disables the Least Recently Used Policy Supported.
Writing a '1' to this bit enables the Least Recently Used Policy Supported.

Bit 2 – RANDP Random Selection Policy Supported
Writing a '0' to this bit disables the Random Selection Policy Supported.
Writing a '1' to this bit enables the Random Selection Policy Supported.

Bit 1 – GCLK Dynamic Clock Gating
Writing a '0' to this bit disables the Dynamic Clock Gating feature.
Writing a '1' to this bit enables the Dynamic Clock Gating feature.
Value         Description
0             Dynamic Clock Gating is disabled.
1             Dynamic Clock Gating is enabled.

Bit 0 – AP Access Port Access Allowed
Writing a '0' to this bit disables the Access Port Access Allowed.
Writing a '1' to this bit enables the Access Port Access Allowed.




© 2019 Microchip Technology Inc.                     Datasheet                    DS60001507E-page 91
                                                                    SAM D5x/E5x Family Data Sheet
                                                                               CMCC - Cortex M Cache Controller

11.10.2 Cache Configuration

           Name:        CFG
           Offset:      0x04
           Reset:       0x00000020
           Property:    R/W


     Bit         31            30             29              28          27          26       25              24


  Access
   Reset


     Bit         23            22             21              20          19          18       17              16


  Access
   Reset


     Bit         15            14             13              12          11          10        9              8


  Access
   Reset


     Bit         7             6               5               4          3           2         1              0
                                          CSIZESW[2:0]                              DCDIS     ICDIS
  Access                      R/W             R/W             R/W                    R/W       R/W
   Reset                       0               1               0                      0         0


           Bits 6:4 – CSIZESW[2:0] Cache Size Configured by Software
           This field configures the cache size.
            Value       Name                        Description
            0x0         CONF_CSIZE_1KB               The Cache Size is configured to 1KB
            0x1         CONF_CSIZE_2KB               The Cache Size is configured to 2KB
            0x2         CONF_CSIZE_4KB               The Cache Size is configured to 4KB
            0x3         CONF_CSIZE_8KB               The Cache Size is configured to 8KB
            0x4         CONF_CSIZE_16KB              The Cache Size is configured to 16KB
            0x5         CONF_CSIZE_32KB              The Cache Size is configured to 32KB
            0x6         CONF_CSIZE_64KB              The Cache Size is configured to 64KB
            0x7                                      Reserved

           Bit 2 – DCDIS Data Cache Disable
           Writing a '0' to this bit enables data caching.
           Writing a '1' to this bit disables data caching.
           Value         Description
           0             Data caching is enabled.
           1             Data caching is disabled.

           Bit 1 – ICDIS Instruction Cache Disable
           Writing a '0' to this bit enables instruction caching.




       © 2019 Microchip Technology Inc.                             Datasheet                       DS60001507E-page 92
                                                      SAM D5x/E5x Family Data Sheet
                                                                  CMCC - Cortex M Cache Controller

Writing a '1' to this bit disables instruction caching.
Value         Description
0             Instruction caching is enabled.
1             Instruction caching is disabled.




© 2019 Microchip Technology Inc.                          Datasheet                 DS60001507E-page 93
                                                               SAM D5x/E5x Family Data Sheet
                                                                          CMCC - Cortex M Cache Controller

11.10.3 Cache Control

           Name:        CTRL
           Offset:      0x08
           Reset:       0x00000000
           Property:    Write-only


     Bit        31            30            29            28         27          26       25             24


  Access
   Reset


     Bit        23            22            21            20         19          18       17             16


  Access
   Reset


     Bit        15            14            13            12         11          10       9              8


  Access
   Reset


     Bit         7             6             5            4          3           2        1              0
                                                                                                        CEN
  Access                                                                                                 W
   Reset                                                                                                 0


           Bit 0 – CEN Cache Controller Enable
           Writing a '0' to this bit disables the CMCC.
           Writing a '1' to this bit enables the CMCC.




       © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 94
                                                       SAM D5x/E5x Family Data Sheet
                                                                  CMCC - Cortex M Cache Controller

11.10.4 Cache Status

           Name:       SR
           Offset:     0x0C
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29      28         27          26       25             24


  Access
   Reset


     Bit        23           22           21      20         19          18       17             16


  Access
   Reset


     Bit        15           14           13      12         11          10       9              8


  Access
   Reset


     Bit        7             6           5       4          3           2        1              0
                                                                                               CSTS
  Access                                                                                         R
   Reset                                                                                         0


           Bit 0 – CSTS Cache Controller Status
           Writing to this bit has no effect.




       © 2019 Microchip Technology Inc.                Datasheet                      DS60001507E-page 95
                                                       SAM D5x/E5x Family Data Sheet
                                                                     CMCC - Cortex M Cache Controller

11.10.5 Cache Lock per Way

           Name:       LCKWAY
           Offset:     0x10
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31           30           29      28            27          26                 25             24


  Access
   Reset


     Bit        23           22           21      20            19          18                 17             16


  Access
   Reset


     Bit        15           14           13      12            11          10                 9              8


  Access
   Reset


     Bit        7             6           5       4             3           2                  1              0
                                                                                 LCKWAY[3:0]
  Access                                                       R/W         R/W             R/W               R/W
   Reset                                                        0           0                  0              0


           Bits 3:0 – LCKWAY[3:0] Lockdown Way Register
           This field selects which way is locked.




       © 2019 Microchip Technology Inc.                   Datasheet                                DS60001507E-page 96
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                 CMCC - Cortex M Cache Controller

11.10.6 Cache Maintenance 0

           Name:         MAINT0
           Offset:       0x20
           Reset:        0x00000000
           Property:     Write-only


     Bit         31            30             29             28             27          26       25             24


  Access
   Reset


     Bit         23            22             21             20             19          18       17             16


  Access
   Reset


     Bit         15            14             13             12             11          10       9              8


  Access
   Reset


     Bit         7              6              5              4             3           2        1              0
                                                                                                              INVALL
  Access                                                                                                        W
   Reset                                                                                                        0


           Bit 0 – INVALL Cache Controller Invalidate All
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit invalidates all cache entries.




       © 2019 Microchip Technology Inc.                               Datasheet                      DS60001507E-page 97
                                                                 SAM D5x/E5x Family Data Sheet
                                                                            CMCC - Cortex M Cache Controller

11.10.7 Cache Maintenance 1

           Name:        MAINT1
           Offset:      0x24
           Reset:       0x00000000
           Property:    Write-only


     Bit        31             30                29        28          27          26                25             24
                                    WAY[3:0]
  Access         W             W                 W         W
   Reset         0             0                 0         0


     Bit        23             22                21        20          19          18                17             16


  Access
   Reset


     Bit        15             14                13        12          11          10                9              8
                                                                                        INDEX[7:4]
  Access                                                               W           W                 W              W
   Reset                                                               0           0                 0              0


     Bit         7             6                 5         4           3           2                 1              0
                                    INDEX[3:0]
  Access         W             W                 W         W
   Reset         0             0                 0         0


           Bits 31:28 – WAY[3:0] Invalidate Way
           Value       Name         Description
           0x0         WAY0         Way 0 is selection for index invalidation
           0x1         WAY1         Way 1 is selection for index invalidation
           0x2         WAY2         Way 2 is selection for index invalidation
           0x3         WAY3         Way 3 is selection for index invalidation
           0x4-0xF                  Reserved

           Bits 11:4 – INDEX[7:0] Invalidate Index
           This field selects the index value for invalidation




       © 2019 Microchip Technology Inc.                          Datasheet                               DS60001507E-page 98
                                                            SAM D5x/E5x Family Data Sheet
                                                                        CMCC - Cortex M Cache Controller

11.10.8 Cache Monitor Configuration

            Name:       MCFG
            Offset:     0x28
            Reset:      0x00000000
            Property:   Read/Write


      Bit        31           30           29          28          27           26      25                24


  Access
   Reset


      Bit        23           22           21          20          19           18      17                16


  Access
   Reset


      Bit        15           14           13          12          11           10       9                 8


  Access
   Reset


      Bit        7             6           5           4            3           2        1                 0
                                                                                              MODE[1:0]
  Access                                                                                R/W               R/W
   Reset                                                                                 0                 0


            Bits 1:0 – MODE[1:0] Cache Controller Monitor Counter Mode
            This field selects the type of data monitored.
             Value       Name                                Description
             0x0         CYCLE_COUNT                         Cycle counter
             0x1         IHIT_COUNT                          Instruction hit counter
             0x2         DHIT_COUNT                          Data hit counter
             0x3                                             Reserved




        © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 99
                                                               SAM D5x/E5x Family Data Sheet
                                                                           CMCC - Cortex M Cache Controller

11.10.9 Cache Monitor Enable

           Name:        MEN
           Offset:      0x2C
           Reset:       0x00000000
           Property:    Read/Write


     Bit        31            30            29            28          27          26       25           24


  Access
   Reset


     Bit        23            22            21            20          19          18       17           16


  Access
   Reset


     Bit        15            14            13            12          11          10       9            8


  Access
   Reset


     Bit         7             6             5            4           3           2        1            0
                                                                                                    MENABLE
  Access                                                                                               R/W
   Reset                                                                                                0


           Bit 0 – MENABLE Cache Controller Monitor Enable
           Writing a '0' to this bit disables the monitor counter.
           Writing a '1' to this bit enables the monitor counter.
           Value         Description
           0             The Monitor counter is disabled.
           1             The Monitor counter is enabled.




       © 2019 Microchip Technology Inc.                         Datasheet                   DS60001507E-page 100
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                CMCC - Cortex M Cache Controller

11.10.10 Cache Monitor Control

            Name:        MCTRL
            Offset:      0x30
            Reset:       0x00000000
            Property:    Write-only


      Bit         31            30             29            28            27          26       25           24


  Access
   Reset


      Bit         23            22             21            20            19          18       17           16


  Access
   Reset


      Bit         15            14             13            12            11          10       9            8


  Access
   Reset


      Bit         7              6             5              4            3           2        1            0
                                                                                                           SWRST
  Access                                                                                                     W
   Reset                                                                                                     0


            Bit 0 – SWRST Cache Controller Software Reset
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit resets the event counter register.




        © 2019 Microchip Technology Inc.                           Datasheet                     DS60001507E-page 101
                                                            SAM D5x/E5x Family Data Sheet
                                                                         CMCC - Cortex M Cache Controller

11.10.11 Cache Monitor Status

            Name:       MSR
            Offset:     0x34
            Reset:      0x00000000
            Property:   Read-only


      Bit        31           30           29          28           27          26       25           24
                                                      EVENT_CNT[31:24]
  Access         R             R           R           R            R           R        R            R
   Reset         0             0           0           0            0           0        0            0


      Bit        23           22           21          20           19          18       17           16
                                                      EVENT_CNT[23:16]
  Access         R             R           R           R            R           R        R            R
   Reset         0             0           0           0            0           0        0            0


      Bit        15           14           13          12           11          10       9            8
                                                       EVENT_CNT[15:8]
  Access         R             R           R           R            R           R        R            R
   Reset         0             0           0           0            0           0        0            0


      Bit        7             6           5           4            3           2        1            0
                                                       EVENT_CNT[7:0]
  Access         R             R           R           R            R           R        R            R
   Reset         0             0           0           0            0           0        0            0


            Bits 31:0 – EVENT_CNT[31:0] Monitor Event Counter
            This field indicates the Monitor Event Counter value.




        © 2019 Microchip Technology Inc.                    Datasheet                     DS60001507E-page 102
