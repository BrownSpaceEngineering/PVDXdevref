# 12. DSU - Device Service Unit

*Source: `Atmel-SAMD51.pdf`, pages 103-144 — SAMD51 family datasheet*

                                                       SAM D5x/E5x Family Data Sheet
                                                                               DSU - Device Service Unit


12.    DSU - Device Service Unit

12.1   Overview
       The Device Service Unit (DSU) provides a means of detecting debugger probes. It enables the ARM
       Debug Access Port (DAP) to have control over multiplexed debug pads and CPU Reset. The DSU also
       provides system-level services to debug adapters in an ARM debug system. It implements a CoreSight
       Debug ROM that provides device identification as well as identification of other debug components within
       the system. Hence, it complies with the ARM Peripheral Identification specification. The DSU also
       provides system services to applications that need memory testing, as required for IEC60730 Class B
       compliance, for example. The DSU can be accessed simultaneously by a debugger and the CPU, as it is
       connected on the High-Speed Bus Matrix. For security reasons, some of the DSU features will be limited
       or unavailable when the device is protected by the NVMCTRL security bit.
       Related Links
       25. NVMCTRL – Nonvolatile Memory Controller



12.2   Features
         •   CPU Reset Extension
         •   Debugger Probe Detection (Cold- and Hot-Plugging)
         •   Chip-Erase Command and Status
         •   32-Bit Cyclic Redundancy Check (CRC32) of any Memory Accessible Through the Bus Matrix
                              ™
         •   ARM® CoreSight Compliant Device Identification
         •   Two Debug Communications Channels with DMA Connection
         •   Debug Access Port Security Filter
         •   Onboard Memory Built-in Self-test (MBIST)




       © 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 103
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           DSU - Device Service Unit


12.3     Block Diagram
         Figure 12-1. DSU Block Diagram


                                                     DSU

                                                                      debugger_present
                              RESET                                  DMA request
                                              DEBUGGER PROBE
                      SWCLK                      INTERFACE           cpu_reset_extension


                                  DAP                                          CPU
                                             DAP SECURITY FILTER                              DMA         NVMCTRL
                               AHB-AP                                      DBG



                                               CORESIGHT ROM
                                PORT
                                                                                 M             S             S
                                                    CRC-32

                          SWDIO                                                            HIGH-SPEED
                                                    MBIST                  M
                                                                                           BUS MATRIX

                                                  CHIP ERASE




12.4     Signal Description
         The DSU uses three signals to function.

          Signal Name                        Type                                        Description
          RESET                              Digital Input                               External Reset
          SWCLK                              Digital Input                               SW clock
          SWDIO                              Digital I/O                                 SW bidirectional data pin

         Related Links
         6. I/O Multiplexing and Considerations



12.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

12.5.1   I/O Lines
         The SWCLK pin is by default assigned to the DSU module to allow debugger probe detection and to
         stretch the CPU Reset phase. For more information, refer to 12.6.3 Debugger Probe Detection. The Hot-
         Plugging feature depends on the PORT configuration. If the SWCLK pin function is changed in the port or
         if the PORT_MUX is disabled, the Hot-Plugging feature is disabled until a power reset or an external
         Reset is performed.

12.5.2   Power Management
         The DSU will continue to operate in Idle mode.




         © 2019 Microchip Technology Inc.                      Datasheet                                DS60001507E-page 104
                                                           SAM D5x/E5x Family Data Sheet
                                                                                   DSU - Device Service Unit

         Related Links
         18. PM – Power Manager

12.5.3   Clocks
         The DSU bus clocks (CLK_DSU_APB and CLK_DSU_AHB) can be enabled and disabled by the Main
         Clock Controller.
         Related Links
         18. PM – Power Manager
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking

12.5.4   DMA
         The DMA request lines are connected to the DMA Controller (DMAC). In order to use DMA requests with
         this peripheral the DMAC must be configured first. Refer to DMAC – Direct Memory Access Controller for
         details.
         Related Links
         22. DMAC – Direct Memory Access Controller

12.5.5   Interrupts
         Not applicable.

12.5.6   Events
         Not applicable.

12.5.7   Register Access Protection
         Registers with write access can be optionally write-protected by the Peripheral Access Controller (PAC),
         except for the following:
           • Debug Communication Channel 0 register (DCC0)
           • Debug Communication Channel 1 register (DCC1)
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.

         Related Links
         27. PAC - Peripheral Access Controller

12.5.8   Analog Connections
         Not applicable.



12.6     Debug Operation

12.6.1   Principle of Operation
         The DSU provides basic services to allow on-chip debug using the ARM Debug Access Port and the
         ARM processor debug resources:
          • CPU Reset extension




         © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 105
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   DSU - Device Service Unit

           • Debugger probe detection
         For more details on the ARM debug components, refer to the ARM Debug Interface v5 Architecture
         Specification.

12.6.2   CPU Reset Extension
         “CPU Reset extension” refers to the extension of the Reset phase of the CPU core after the external
         Reset is released. This ensures that the CPU is not executing code at start-up while a debugger is
         connects to the system. The debugger is detected on a RESET release event when SWCLK is low. At
         start-up, SWCLK is internally pulled up to avoid false detection of a debugger if the SWCLK pin is left
         unconnected. When the CPU is held in the Reset extension phase, the CPU Reset Extension bit of the
         Status A register (STATUSA.CRSTEXT) is set. To release the CPU, write a '1' to STATUSA.CRSTEXT.
         STATUSA.CRSTEXT will then be set to '0'. Writing a '0' to STATUSA.CRSTEXT has no effect. For
         security reasons, it is not possible to release the CPU Reset extension when the device is protected by
         the NVMCTRL security bit. Trying to do so sets the Protection Error bit (PERR) of the Status A register
         (STATUSA.PERR).
         Figure 12-2. Typical CPU Reset Extension Set and Clear Timing Diagram
                          SWCLK



                           RESET



                  DSU CRSTEXT
                         Clear


                       CPU reset
                       extension


                     CPU_STATE                        reset                           running

         Related Links
         25. NVMCTRL – Nonvolatile Memory Controller

12.6.3   Debugger Probe Detection

12.6.3.1 Cold Plugging
         Cold-Plugging is the detection of a debugger when the system is in Reset. Cold-Plugging is detected
         when the CPU Reset extension is requested, as described above.
12.6.3.2 Hot Plugging
         Hot-Plugging is the detection of a debugger probe when the system is not in Reset. Hot-Plugging is not
         possible under Reset because the detector is reset when POR or RESET are asserted. Hot-Plugging is
         active when a SWCLK falling edge is detected. The SWCLK pad is multiplexed with other functions and
         the user must ensure that its default function is assigned to the debug system. If the SWCLK function is
         changed, the Hot-Plugging feature is disabled until a power reset or external Reset occurs. Availability of
         the Hot-Plugging feature can be read from the Hot-Plugging Enable bit of the Status B register
         (STATUSB.HPE).




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 106
                                                         SAM D5x/E5x Family Data Sheet
                                                                                 DSU - Device Service Unit

       Figure 12-3. Hot-Plugging Detection Timing Diagram
                                     SWCLK



                                      RESET


                                CPU_STATE      reset                   running



                                Hot-Plugging

       The presence of a debugger probe is detected when either Hot-Plugging or Cold-Plugging is detected.
       Once detected, the Debugger Present bit of the Status B register (STATUSB.DBGPRES) is set. For
       security reasons, Hot-Plugging is not available when the device is protected by the NVMCTRL security
       bit.
       This detection requires that pads are correctly powered. Thus, at cold start-up, this detection cannot be
       done until POR is released. If the device is protected, Cold-Plugging is the only way to detect a debugger
       probe, and so the external Reset timing must be longer than the POR timing. If external Reset is
       deasserted before POR release, the user must retry the procedure above until it gets connected to the
       device.
       Related Links
       25. NVMCTRL – Nonvolatile Memory Controller



12.7   Chip Erase
       Chip erase consists of removing all sensitive information stored in the chip and clearing the NVMCTRL
       security bit. Therefore, all volatile memories and the Flash memory (including the EEPROM emulation
       area) will be erased. The Flash auxiliary rows, including the user row, will not be erased.
       When the device is protected, the debugger must first reset the device in order to be detected. This
       ensures that internal registers are reset after the Protected state is removed. The chip erase operation is
       triggered by writing a '1' to the chip erase bit in the Control register (CTRL.CE). This command will be
       discarded if the DSU is protected by the Peripheral Access Controller (PAC). Once issued, the module
       clears volatile memories prior to erasing the Flash array. To ensure that the chip erase operation is
       completed, check the Done bit of the Status A register (STATUSA.DONE).
       The chip erase operation depends on clocks and power management features that can be altered by the
       CPU. For that reason, it is recommended to issue a chip erase after a Cold-Plugging procedure to ensure
       that the device is in a known and Safe state.
       The recommended sequence is as follows:
        1. Issue the Cold-Plugging procedure (refer to 12.6.3.1 Cold Plugging). The device then:
             1.1.  Detects the debugger probe.
             1.2.  Holds the CPU in Reset.
        2. Issue the chip erase command by writing a '1' to CTRL.CE. The device then:
              2.1.      Clears the system volatile memories.
              2.2.      Erases the whole Flash array (including the EEPROM emulation area, not including
                        auxiliary rows).




       © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 107
                                                        SAM D5x/E5x Family Data Sheet
                                                                                DSU - Device Service Unit

              2.3.    Erases the lock row, removing the NVMCTRL security bit protection.
         3.   Check for completion by polling STATUSA.DONE (read as '1' when completed).
         4.   Reset the device to let the NVMCTRL update the fuses.



12.8   Programming
       Programming the Flash or RAM memories is only possible when the device is not protected by the
       NVMCTRL security bit. The programming procedure is as follows:
        1. At power-up, RESET is driven low by a debugger. The on-chip regulator holds the system in a POR
            state until the input supply is above the POR threshold (refer to Power-on Reset (POR)
            characteristics). The system continues to be held in this Static state until the internally regulated
            supplies have reached a safe Operating state.
        2. The PM starts, clocks are switched to the slow clock (Core Clock, System Clock, Flash Clock and
            any Bus Clocks that do not have clock gate control). Internal Resets are maintained due to the
            external Reset.
        3. The debugger maintains a low level on SWCLK. RESET is released, resulting in a debugger Cold-
            Plugging procedure.
        4. The debugger generates a clock signal on the SWCLK pin, the Debug Access Port (DAP) receives
            a clock.
        5. The CPU remains in Reset due to the Cold-Plugging procedure; meanwhile, the rest of the system
            is released.
        6. A chip erase is issued to ensure that the Flash is fully erased prior to programming.
        7. Programming is available through the AHB-AP.
        8. After the operation is completed, the chip can be restarted either by asserting RESET or toggling
            power. Make sure that the SWCLK pin is high when releasing RESET to prevent extending the
            CPU Reset.
       Related Links
       25. NVMCTRL – Nonvolatile Memory Controller



12.9   Intellectual Property Protection
       Intellectual property protection consists of restricting access to internal memories from external tools
       when the device is protected, and this is accomplished by setting the NVMCTRL security bit. This
       Protected state can be removed by issuing a chip erase (refer to 12.7 Chip Erase). When the device is
       protected, read/write accesses using the AHB-AP are limited to the DSU address range and DSU
       commands are restricted. When issuing a chip erase, sensitive information is erased from volatile
       memory and Flash.
       The DSU implements a security filter that monitors the AHB transactions inside the DAP. If the device is
       protected, then AHB-AP read/write accesses outside the DSU external address range are discarded,
       causing an error response that sets the ARM AHB-AP sticky error bits (refer to the ARM Debug Interface
       v5 Architecture Specification on http://www.arm.com).
       The DSU is intended to be accessed either:
        • Internally from the CPU, without any limitation, even when the device is protected
        • Externally from a debug adapter, with some restrictions when the device is protected




       © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 108
                                                 SAM D5x/E5x Family Data Sheet
                                                                          DSU - Device Service Unit

For security reasons, DSU features have limitations when used from a debug adapter. To differentiate
external accesses from internal ones, the first 0x100 bytes of the DSU register map has been mirrored at
offset 0x100:
  • The first 0x100 bytes form the internal address range
  • The next 0x100 bytes form the external address range
When the device is protected, the DAP can only issue MEM-AP accesses in the DSU range
0x0100-0x2000.
The DSU Operating registers are located in the 0x0000-0x00FF area and remapped in 0x0100-0x01FF to
differentiate accesses coming from a debugger and the CPU. If the device is protected and an access is
issued in the region 0x0100-0x01FF, it is subject to security restrictions. For more information, refer to
Table 12-1.
Figure 12-4. APB Memory Mapping
     0x0000

                        DSU operating       Internal address range
                          registers         (cannot be accessed from debug tools when the device is
                                            protected by the NVMCTRL security bit)
     0x00FF
     0x0100

                           Mirrored
                        DSU operating
                          registers

     0x01FF

                                            External address range
                             Empty
                                            (can be accessed from debug tools with some restrictions)
     0x1000


                        DSU CoreSight
                            ROM


     0x1FFF

Some features not activated by APB transactions are not available when the device is protected:
Table 12-1. Feature Availability Under Protection

 Features                                            Availability When the Device is Protected
 CPU Reset Extension                                 Yes
 Clear CPU Reset Extension                           No
 Debugger Cold-Plugging                              Yes
 Debugger Hot-Plugging                               No

Related Links
25. NVMCTRL – Nonvolatile Memory Controller




© 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 109
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         DSU - Device Service Unit


12.10    Device Identification
         Device identification relies on the ARM CoreSight component identification scheme, which allows the chip
         to be identified as a SAM device implementing a DSU. The DSU contains identification registers to
         differentiate the device.

12.10.1 CoreSight Identification
        A system-level ARM® CoreSight™ ROM table is present in the device to identify the vendor and the chip
        identification method. Its address is provided in the MEM-AP BASE register inside the ARM Debug
        Access Port. The CoreSight ROM implements a 64-bit conceptual ID composed as follows from the PID0
        to PID7 CoreSight ROM Table registers:
         Figure 12-5. Conceptual 64-bit Peripheral ID




         Table 12-2. Conceptual 64-Bit Peripheral ID Bit Descriptions

          Field                 Size Description                                                             Location
          JEP-106 CC code 4            Continuation code: 0x0                                                PID4
          JEP-106 ID code       7      Device ID: 0x1F                                                       PID1+PID2
          4KB count             4      Indicates that the CoreSight component is a ROM: 0x0                  PID4
          RevAnd                4      Not used; read as 0                                                   PID3

          CUSMOD                4      Not used; read as 0                                                   PID3

          PARTNUM               12     Contains 0xCD0 to indicate that DSU is present                        PID0+PID1
          REVISION              4      DSU revision (starts at 0x0 and increments by 1 at both major         PID2
                                       and minor revisions). Identifies DSU identification method
                                       variants. If 0x0, this indicates that device identification can be
                                       completed by reading the Device Identification register (DID)

         For more information, refer to the ARM Debug Interface Version 5 Architecture Specification.

12.10.2 Chip Identification Method
        The DSU DID register identifies the device by implementing the following information:
           •   Processor identification
           •   Product family identification
           •   Product series identification
           •   Device select




        © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 110
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                        DSU - Device Service Unit


12.11     Functional Description

12.11.1 Principle of Operation
          The DSU provides memory services, such as CRC32 or MBIST that require almost the same interface.
          Hence, the Address, Length and Data registers (ADDR, LENGTH, DATA) are shared. These shared
          registers must be configured first; then a command can be issued by writing the Control register. When a
          command is ongoing, other commands are discarded until the current operation is completed. Hence, the
          user must wait for the STATUSA.DONE bit to be set prior to issuing another one.

12.11.2 Basic Operation

12.11.2.1 Initialization
          The module is enabled by enabling its clocks. For more details, refer to 12.5.3 Clocks. The DSU registers
          can be PAC write-protected.
          Related Links
          27. PAC - Peripheral Access Controller

12.11.2.2 Operation From a Debug Adapter
          Debug adapters should access the DSU registers in the external address range 0x100 – 0x2000. If the
          device is protected by the NVMCTRL security bit, accessing the first 0x100 bytes causes the system to
          return an error. Refer to 12.9 Intellectual Property Protection.
          Related Links
          25. NVMCTRL – Nonvolatile Memory Controller

12.11.2.3 Operation From the CPU
          There are no restrictions when accessing DSU registers from the CPU. However, the user should access
          DSU registers in the internal address range (0x0 – 0x100) to avoid external security restrictions. Refer to
          12.9 Intellectual Property Protection.

12.11.3 32-bit Cyclic Redundancy Check CRC32
          The DSU unit provides support for calculating a cyclic redundancy check (CRC32) value for a memory
          area (including Flash and AHB RAM).
          When the CRC32 command is issued from:
           • The internal range, the CRC32 can be operated at any memory location
           • The external range, the CRC32 operation is restricted; DATA, ADDR, and LENGTH values are forced
             (see below)
          Table 12-3. AMOD Bit Descriptions when Operating CRC32

           AMOD[1:0] Short name External range restrictions
           0               ARRAY            CRC32 is restricted to the full Flash array area (EEPROM emulation area not
                                            included) DATA forced to 0xFFFFFFFF before calculation (no seed)
           1               EEPROM           CRC32 of the whole EEPROM emulation area DATA forced to 0xFFFFFFFF
                                            before calculation (no seed)
           2-3             Reserved




         © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 111
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     DSU - Device Service Unit

         The algorithm employed is the industry standard CRC32 algorithm using the generator polynomial
         0xEDB88320 (reversed representation).

12.11.3.1 Starting CRC32 Calculation
         CRC32 calculation for a memory range is started after writing the start address into the Address register
         (ADDR) and the size of the memory range into the Length register (LENGTH). Both must be word-
         aligned.
         The initial value used for the CRC32 calculation must be written to the Data register (DATA). This value
         will usually be 0xFFFFFFFF, but can be, for example, the result of a previous CRC32 calculation if
         generating a common CRC32 of separate memory blocks.
         Once completed, the calculated CRC32 value can be read out of the Data register. The read value must
         be complemented to match standard CRC32 implementations or kept noninverted if used as starting
         point for subsequent CRC32 calculations.
         The actual test is started by writing a '1' in the 32-bit Cyclic Redundancy Check bit of the Control register
         (CTRL.CRC). A running CRC32 operation can be canceled by resetting the module (writing '1' to
         CTRL.SWRST).
         Related Links
         25. NVMCTRL – Nonvolatile Memory Controller

12.11.3.2 Interpreting the Results
         The user should monitor the Status A register. When the operation is completed, STATUSA.DONE is set.
         Then the Bus Error bit of the Status A register (STATUSA.BERR) must be read to ensure that no bus
         error occurred.

12.11.4 Debug Communication Channels
         The Debug Communication Channels (DCCO and DCC1) consist of a pair of registers with associated
         handshake logic, accessible by both CPU and debugger even if the device is protected by the NVMCTRL
         security bit. The registers can be used to exchange data between the CPU and the debugger, during run
         time as well as in Debug mode. This enables the user to build a custom debug protocol using only these
         registers.
         The DCC0 and DCC1 registers are accessible when the Protected state is active. When the device is
         protected, however, it is not possible to connect a debugger while the CPU is running
         (STATUSA.CRSTEXT is not writable and the CPU is held under Reset).
         Two Debug Communication Channel status bits in the Status B registers (STATUS.DCCDx) indicate
         whether a new value has been written in DCC0 or DCC1. These bits, DCC0D and DCC1D, are located in
         the STATUSB registers. They are automatically set on write and cleared on read.
         Note: The DCC0 and DCC1 registers are shared with the on-board memory testing logic (MBIST).
         Accordingly, DCC0 and DCC1 must not be used while performing MBIST operations.
         Related Links
         25. NVMCTRL – Nonvolatile Memory Controller

12.11.5 Debug Communication Channels DMA connection
         The DCC0 and DCC1 registers can be used as a source or a destination of a DMA channel. The DSU
         generates one DMA request per Debug Communication Channels. The level of this DMA request is
         selectable writing the CFG.DCCDMALEVELx bit. Writing a 0 to this bit will configure the DMA request to




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 112
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          DSU - Device Service Unit

        trig on DCCx register empty. Writing a 1 to this bit will configure the DMA request to trig on DCCx register
        full.

12.11.6 Testing of On-Board Memories MBIST
        The DSU implements a feature for automatic testing of memory, also known as MBIST (memory built-in
        self test). This is primarily intended for production test of on-board memories. MBIST cannot be operated
        from the external address range when the device is protected by the NVMCTRL security bit. If an MBIST
        command is issued when the device is protected, a protection error is reported in the Protection Error bit
        in the Status A register (STATUSA.PERR).
         1.   Algorithm
              The algorithm used for testing is a type of March algorithm called "March LR". This algorithm is able
              to detect a wide range of memory defects, while still keeping a linear run time. The algorithm is:
              1.1.      Write entire memory to '0', in any order.
              1.2.      Bit by bit read '0', write '1', in descending order.
              1.3.      Bit by bit read '1', write '0', read '0', write '1', in ascending order.
              1.4.      Bit by bit read '1', write '0', in ascending order.
              1.5.      Bit by bit read '0', write '1', read '1', write '0', in ascending order.
              1.6.      Read '0' from entire memory, in ascending order.
              The specific implementation used as a run time which depends on the CPU clock frequency and
              the number of bytes tested in the RAM. The detected faults are:
               – Address decoder faults
               – Stuck-at faults
               – Transition faults
               – Coupling faults
               – Linked Coupling faults
         2.   Starting MBIST
              To test a memory, you need to write the start address of the memory to the ADDR.ADDR bit field,
              and the size of the memory into the Length register.
              For best test coverage, an entire physical memory block should be tested at once. It is possible to
              test only a subset of a memory, but the test coverage will then be somewhat lower.
              The actual test is started by writing a '1' to CTRL.MBIST. A running MBIST operation can be
              canceled by writing a '1' to CTRL.SWRST.
         3.   Interpreting the Results
              The tester should monitor the STATUSA register. When the operation is completed,
              STATUSA.DONE is set. There are two different modes:
                – ADDR.AMOD=0: exit-on-error (default)
                  In this mode, the algorithm terminates either when a fault is detected or on successful
                  completion. In both cases, STATUSA.DONE is set. If an error was detected, STATUSA.FAIL
                  will be set. User then can read the DATA and ADDR registers to locate the fault.
                – ADDR.AMOD=1: pause-on-error
                  In this mode, the MBIST algorithm is paused when an error is detected. In such a situation,
                  only STATUSA.FAIL is asserted. The state machine waits for user to clear STATUSA.FAIL by
                  writing a '1' in STATUSA.FAIL to resume. Prior to resuming, user can read the DATA and
                  ADDR registers to locate the fault.




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 113
                                                          SAM D5x/E5x Family Data Sheet
                                                                                       DSU - Device Service Unit

  4.     Locating Faults
         If the test stops with STATUSA.FAIL set, one or more bits failed the test. The test stops at the first
         detected error. The position of the failing bit can be found by reading the following registers:
             – ADDR: Address of the word containing the failing bit
             – DATA: contains data to identify which bit failed, and during which phase of the test it failed. The
               DATA register will in this case contains the following bit groups:
Figure 12-6. DATA bits Description When MBIST Operation Returns an Error
       Bit        31          30          29          28           27              26         25            24




       Bit        23          22          21          20           19              18         17            16




       Bit        15          14          13          12           11              10          9            8
                                                                                            phase


       Bit        7            6          5           4            3               2           1            0
                                                                             bit_index

  • bit_index: contains the bit number of the failing bit
  • phase: indicates which phase of the test failed and the cause of the error, as listed in the following
    table.
Table 12-4. MBIST Operation Phases

 Phase                                                       Test actions
 0                                                           Write all bits to zero. This phase cannot fail.
 1                                                           Read '0', write '1', increment address

 2                                                           Read '1', write '0'

 3                                                           Read '0', write '1', decrement address

 4                                                           Read '1', write '0', decrement address

 5                                                           Read '0', write '1'

 6                                                           Read '1', write '0', decrement address

 7                                                           Read all zeros. bit_index is not used

Table 12-5. AMOD Bit Descriptions for MBIST

 AMOD[1:0]                                                   Description
 0x0                                                         Exit on Error
 0x1                                                         Pause on Error
 0x2, 0x3                                                    Reserved




© 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 114
                                                       SAM D5x/E5x Family Data Sheet
                                                                              DSU - Device Service Unit

        Related Links
        25. NVMCTRL – Nonvolatile Memory Controller
        8. Product Memory Mapping Overview

12.11.7 System Services Availability when Accessed Externally and Device is Protected
        External access: Access performed in the DSU address offset 0x200-0x1FFF range.
        Internal access: Access performed in the DSU address offset 0x000-0x100 range.
        Table 12-6. Available Features when Operated From The External Address Range and Device is
        Protected

         Features                                          Availability From The External Address Range
                                                           and Device is Protected
         Chip erase command and status                     Yes
         CRC32                                             Yes, only full array or full EEPROM
         CoreSight Compliant Device identification         Yes
         Debug communication channels                      Yes
         Testing of onboard memories (MBIST)               No
         STATUSA.CRSTEXT clearing                          No (STATUSA.PERR is set when attempting to do
                                                           so)




        © 2019 Microchip Technology Inc.                Datasheet                          DS60001507E-page 115
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                         DSU - Device Service Unit


12.12     Register Summary

 Offset        Name        Bit Pos.

 0x00          CTRL           7:0                                                CE           MBIST          CRC                         SWRST
 0x01        STATUSA          7:0                                            PERR                 FAIL       BERR         CRSTEXT         DONE
 0x02        STATUSB          7:0                             CELCK          HPE              DCCD1         DCCD0         DBGPRES         PROT
 0x03        Reserved
                              7:0                                    ADDR[5:0]                                                    AMOD[1:0]
                             15:8                                                  ADDR[13:6]
 0x04          ADDR
                             23:16                                                ADDR[21:14]
                             31:24                                                ADDR[29:22]
                              7:0                                 LENGTH[5:0]
                             15:8                                                 LENGTH[13:6]
 0x08         LENGTH
                             23:16                                               LENGTH[21:14]
                             31:24                                               LENGTH[29:22]
                              7:0                                                     DATA[7:0]
                             15:8                                                     DATA[15:8]
 0x0C          DATA
                             23:16                                                DATA[23:16]
                             31:24                                                DATA[31:24]
                              7:0                                                     DATA[7:0]
                             15:8                                                     DATA[15:8]
 0x10          DCC0
                             23:16                                                DATA[23:16]
                             31:24                                                DATA[31:24]
                              7:0                                                     DATA[7:0]
                             15:8                                                     DATA[15:8]
 0x14          DCC1
                             23:16                                                DATA[23:16]
                             31:24                                                DATA[31:24]
                              7:0                                                 DEVSEL[7:0]
                             15:8                      DIE[3:0]                                                   REVISION[3:0]
 0x18           DID
                             23:16    FAMILY[0:0]                                                   SERIES[5:0]
                             31:24                  PROCESSOR[3:0]                                                 FAMILY[4:1]
                              7:0                                         ETBRAMEN            DCCDMALEVEL[1:0]                    LQOS[1:0]
                             15:8
 0x1C          CFG
                             23:16
                             31:24
 0x20
   ...       Reserved
 0xEF
                              7:0                                                     DCFG[7:0]
                             15:8                                                  DCFG[15:8]
 0xF0         DCFG0
                             23:16                                                DCFG[23:16]
                             31:24                                                DCFG[31:24]
                              7:0                                                     DCFG[7:0]
                             15:8                                                  DCFG[15:8]
 0xF4         DCFG1
                             23:16                                                DCFG[23:16]
                             31:24                                                DCFG[31:24]




          © 2019 Microchip Technology Inc.                            Datasheet                                           DS60001507E-page 116
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    DSU - Device Service Unit

...........continued

  Offset               Name     Bit Pos.

   0xF8
     ...           Reserved
  0x0FFF
                                  7:0                                                             FMT     EPRES
                                 15:8            ADDOFF[3:0]
  0x1000               ENTRY0
                                 23:16                               ADDOFF[11:4]
                                 31:24                              ADDOFF[19:12]
                                  7:0                                                             FMT     EPRES
                                 15:8            ADDOFF[3:0]
  0x1004               ENTRY1
                                 23:16                               ADDOFF[11:4]
                                 31:24                              ADDOFF[19:12]
                                  7:0                                  END[7:0]
                                 15:8                                 END[15:8]
  0x1008                END
                                 23:16                                END[23:16]
                                 31:24                                END[31:24]
  0x100C
     ...           Reserved
  0x1FCB
                                  7:0                                                                     SMEMP
                                 15:8
 0x1FCC           MEMTYPE
                                 23:16
                                 31:24
                                  7:0             FKBC[3:0]                              JEPCC[3:0]
                                 15:8
  0x1FD0                PID4
                                 23:16
                                 31:24
                                  7:0
                                 15:8
  0x1FD4                PID5
                                 23:16
                                 31:24
                                  7:0
                                 15:8
  0x1FD8                PID6
                                 23:16
                                 31:24
                                  7:0
                                 15:8
 0x1FDC                 PID7
                                 23:16
                                 31:24
                                  7:0                                PARTNBL[7:0]
                                 15:8
  0x1FE0                PID0
                                 23:16
                                 31:24




              © 2019 Microchip Technology Inc.                 Datasheet                       DS60001507E-page 117
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                           DSU - Device Service Unit

...........continued

  Offset               Name    Bit Pos.

                                  7:0                 JEPIDCL[3:0]                              PARTNBH[3:0]
                                 15:8
  0x1FE4               PID1
                                 23:16
                                 31:24
                                  7:0                REVISION[3:0]                  JEPU              JEPIDCH[2:0]
                                 15:8
  0x1FE8               PID2
                                 23:16
                                 31:24
                                  7:0                 REVAND[3:0]                                CUSMOD[3:0]
                                 15:8
  0x1FEC               PID3
                                 23:16
                                 31:24
                                  7:0                                    PREAMBLEB0[7:0]
                                 15:8
  0x1FF0               CID0
                                 23:16
                                 31:24
                                  7:0                 CCLASS[3:0]                               PREAMBLE[3:0]
                                 15:8
  0x1FF4               CID1
                                 23:16
                                 31:24
                                  7:0                                    PREAMBLEB2[7:0]
                                 15:8
  0x1FF8               CID2
                                 23:16
                                 31:24
                                  7:0                                    PREAMBLEB3[7:0]
                                 15:8
  0x1FFC               CID3
                                 23:16
                                 31:24




12.13          Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to 12.5.7 Register Access Protection.




              © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 118
                                                                SAM D5x/E5x Family Data Sheet
                                                                                      DSU - Device Service Unit

12.13.1 Control

           Name:        CTRL
           Offset:      0x0000
           Reset:       0x00
           Property:    PAC Write-Protection


     Bit         7             6              5             4              3          2        1           0
                                                           CE            MBIST       CRC                SWRST
  Access                                                   W              W          W                     W
   Reset                                                    0              0          0                    0


           Bit 4 – CE Chip-Erase
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit starts the Chip-Erase operation.

           Bit 3 – MBIST Memory Built-In Self-Test
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit starts the memory BIST algorithm.

           Bit 2 – CRC 32-bit Cyclic Redundancy Check
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit starts the cyclic redundancy check algorithm.

           Bit 0 – SWRST Software Reset
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit resets the module.




       © 2019 Microchip Technology Inc.                          Datasheet                     DS60001507E-page 119
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                     DSU - Device Service Unit

12.13.2 Status A

           Name:         STATUSA
           Offset:       0x0001
           Reset:        0x00
           Property:     PAC Write Protection


     Bit         7              6              5                 4         3        2            1           0
                                                           PERR           FAIL    BERR        CRSTEXT      DONE
  Access                                                    R/W           R/W      R/W          R/W         R/W
   Reset                                                         0         0        0            0           0


           Bit 4 – PERR Protection Error
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Protection Error bit.
           This bit is set when a command that is not allowed in Protected state is issued.

           Bit 3 – FAIL Failure
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Failure bit.
           This bit is set when a DSU operation failure is detected.

           Bit 2 – BERR Bus Error
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Bus Error bit.
           This bit is set when a bus error is detected.

           Bit 1 – CRSTEXT CPU Reset Phase Extension
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the CPU Reset Phase Extension bit.
           This bit is set when a debug adapter Cold-Plugging is detected, which extends the CPU Reset phase.

           Bit 0 – DONE Done
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit clears the Done bit.
           This bit is set when a DSU operation is completed.




       © 2019 Microchip Technology Inc.                              Datasheet                   DS60001507E-page 120
                                                              SAM D5x/E5x Family Data Sheet
                                                                                  DSU - Device Service Unit

12.13.3 Status B

           Name:       STATUSB
           Offset:     0x0002
           Reset:      0x0x
           Property:   PAC Write-Protection


     Bit         7            6             5            4               3       2            1            0
                                          CELCK         HPE            DCCD1   DCCD0       DBGPRES       PROT
  Access                                    R            R              R        R            R            R
   Reset                                    0            0               0       0            x            x


           Bit 5 – CELCK Chip Erase Locked
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit has no effect.
           This bit is set when Chip Erase is locked.
           This bit is cleared when Chip Erase is unlocked.

           Bit 4 – HPE Hot-Plugging Enable
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit has no effect.
           This bit is set when Hot-Plugging is enabled.
           This bit is cleared when Hot-Plugging is disabled. This is the case when the SWCLK function is changed.
           Only a power-reset or a external reset can set it again.

           Bits 2, 3 – DCCD Debug Communication Channel x Dirty
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit has no effect.
           This bit is set when DCC is written.
           This bit is cleared when DCC is read.

           Bit 1 – DBGPRES Debugger Present
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit has no effect.
           This bit is set when a debugger probe is detected.
           This bit is never cleared.

           Bit 0 – PROT Protected
           Writing a '0' to this bit has no effect.
           Writing a '1' to this bit has no effect.
           This bit is set at power-up when the device is protected.
           This bit is never cleared.




       © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 121
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                      DSU - Device Service Unit

12.13.4 Address

           Name:       ADDR
           Offset:     0x0004
           Reset:      0x00000000
           Property:   PAC Write Protection


     Bit        31           30           29                28                 27    26       25                24
                                                                 ADDR[29:22]
  Access       R/W          R/W           R/W               R/W                R/W   R/W      R/W               R/W
   Reset         0            0            0                 0                  0     0        0                 0


     Bit        23           22           21                20                 19    18       17                16
                                                                 ADDR[21:14]
  Access       R/W          R/W           R/W               R/W                R/W   R/W      R/W               R/W
   Reset         0            0            0                 0                  0     0        0                 0


     Bit        15           14           13                12                 11    10        9                 8
                                                                  ADDR[13:6]
  Access       R/W          R/W           R/W               R/W                R/W   R/W      R/W               R/W
   Reset         0            0            0                 0                  0     0        0                 0


     Bit         7            6            5                 4                  3     2        1                 0
                                                ADDR[5:0]                                           AMOD[1:0]
  Access       R/W          R/W           R/W               R/W                R/W   R/W      R/W               R/W
   Reset         0            0            0                 0                  0     0        0                 0


           Bits 31:2 – ADDR[29:0] Address
           Initial word start address needed for memory operations.

           Bits 1:0 – AMOD[1:0] Access Mode
           The functionality of these bits is dependent on the operation mode.
           Bit description when operating CRC32: refer to 12.11.3 32-bit Cyclic Redundancy Check CRC32
           Bit description when testing onboard memories (MBIST): refer to 12.11.6 Testing of On-Board Memories
           MBIST




       © 2019 Microchip Technology Inc.                              Datasheet                 DS60001507E-page 122
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                     DSU - Device Service Unit

12.13.5 Length

           Name:       LENGTH
           Offset:     0x0008
           Reset:      0x00000000
           Property:   PAC Write Protection


     Bit        31           30           29                 28             27      26       25           24
                                                              LENGTH[29:22]
  Access       R/W          R/W           R/W            R/W               R/W      R/W      R/W         R/W
   Reset        0             0            0                 0                  0    0        0           0


     Bit        23           22           21                 20             19      18       17           16
                                                              LENGTH[21:14]
  Access       R/W          R/W           R/W            R/W               R/W      R/W      R/W         R/W
   Reset        0             0            0                 0                  0    0        0           0


     Bit        15           14           13                 12             11      10        9           8
                                                                 LENGTH[13:6]
  Access       R/W          R/W           R/W            R/W               R/W      R/W      R/W         R/W
   Reset        0             0            0                 0                  0    0        0           0


     Bit        7             6            5                 4                  3    2        1           0
                                               LENGTH[5:0]
  Access       R/W          R/W           R/W            R/W               R/W      R/W
   Reset        0             0            0                 0                  0    0


           Bits 31:2 – LENGTH[29:0] Length
           Length in words needed for memory operations.




       © 2019 Microchip Technology Inc.                              Datasheet                DS60001507E-page 123
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                     DSU - Device Service Unit

12.13.6 Data

           Name:        DATA
           Offset:      0x000C
           Reset:       0x00000000
           Property:    PAC Write Protection


     Bit        31            30            29           28                    27   26       25           24
                                                                 DATA[31:24]
  Access        R/W          R/W           R/W          R/W                   R/W   R/W      R/W         R/W
   Reset         0            0             0                0                 0     0        0           0


     Bit        23            22            21           20                    19   18       17           16
                                                                 DATA[23:16]
  Access        R/W          R/W           R/W          R/W                   R/W   R/W      R/W         R/W
   Reset         0            0             0                0                 0     0        0           0


     Bit        15            14            13           12                    11   10        9           8
                                                                 DATA[15:8]
  Access        R/W          R/W           R/W          R/W                   R/W   R/W      R/W         R/W
   Reset         0            0             0                0                 0     0        0           0


     Bit         7            6             5                4                 3     2        1           0
                                                                  DATA[7:0]
  Access        R/W          R/W           R/W          R/W                   R/W   R/W      R/W         R/W
   Reset         0            0             0                0                 0     0        0           0


           Bits 31:0 – DATA[31:0] Data
           Memory operation initial value or result value.




       © 2019 Microchip Technology Inc.                             Datasheet                 DS60001507E-page 124
                                                       SAM D5x/E5x Family Data Sheet
                                                                          DSU - Device Service Unit

12.13.7 Debug Communication Channel x

           Name:       DCC
           Offset:     0x10 + n*0x04 [n=0..1]
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29    28                 27    26       25           24
                                                     DATA[31:24]
  Access       R/W          R/W           R/W   R/W                R/W   R/W      R/W         R/W
   Reset        0             0            0     0                  0     0        0           0


     Bit        23           22           21    20                 19    18       17           16
                                                     DATA[23:16]
  Access       R/W          R/W           R/W   R/W                R/W   R/W      R/W         R/W
   Reset        0             0            0     0                  0     0        0           0


     Bit        15           14           13    12                 11    10        9           8
                                                      DATA[15:8]
  Access       R/W          R/W           R/W   R/W                R/W   R/W      R/W         R/W
   Reset        0             0            0     0                  0     0        0           0


     Bit        7             6            5     4                  3     2        1           0
                                                      DATA[7:0]
  Access       R/W          R/W           R/W   R/W                R/W   R/W      R/W         R/W
   Reset        0             0            0     0                  0     0        0           0


           Bits 31:0 – DATA[31:0] Data
           Data register.




       © 2019 Microchip Technology Inc.                 Datasheet                  DS60001507E-page 125
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                     DSU - Device Service Unit

12.13.8 Device Identification

            Name:          DID
            Offset:        0x0018
            Property:      PAC Write Protection

            The information in this register is related to the Ordering Information.

      Bit        31             30              29         28                 27                 26                 25           24
                                PROCESSOR[3:0]                                                        FAMILY[4:1]
   Access         R              R              R           R                 R                  R                  R            R
    Reset         p              p              p           p                 f                  f                   f            f


      Bit        23             22              21         20                 19                 18                 17           16
             FAMILY[0:0]                                                           SERIES[5:0]
   Access         R                             R           R                 R                  R                  R            R
    Reset         f                             s           s                 s                  s                   s           s


      Bit        15             14              13         12                 11                 10                  9           8
                                     DIE[3:0]                                                        REVISION[3:0]
   Access         R              R              R           R                 R                  R                  R            R
    Reset         d              d              d           d                 r                  r                   r           r


      Bit         7              6              5           4                 3                  2                   1           0
                                                                DEVSEL[7:0]
   Access         R              R              R           R                 R                  R                  R            R
    Reset         x              x              x           x                 x                  x                   x           x


            Bits 31:28 – PROCESSOR[3:0] Processor
            The value of this field defines the processor used on the device.

            Bits 27:23 – FAMILY[4:0] Product Family
            The value of this field corresponds to the product family part of the ordering code.

            Bits 21:16 – SERIES[5:0] Product Series
            The value of this field corresponds to the product series part of the ordering code.

            Bits 15:12 – DIE[3:0] Die Number
            Identifies the die family.

            Bits 11:8 – REVISION[3:0] Revision Number
            Identifies the die revision number. Refer the product family silicon errata and data sheet clarification
            document for further information.
            Note: The device variant (last letter of the ordering number) is independent of the die revision
            (DSU.DID.REVISION): The device variant denotes functional differences, whereas the die revision marks
            evolution of the die.

            Bits 7:0 – DEVSEL[7:0] Device Selection
            This bit field identifies a device within a product family and product series.
            Related Links




        © 2019 Microchip Technology Inc.                           Datasheet                                         DS60001507E-page 126
                                   SAM D5x/E5x Family Data Sheet
                                               DSU - Device Service Unit

2. Ordering Information




© 2019 Microchip Technology Inc.   Datasheet            DS60001507E-page 127
                                                              SAM D5x/E5x Family Data Sheet
                                                                                    DSU - Device Service Unit

12.13.9 Configuration

            Name:       CFG
            Offset:     0x1C
            Reset:      0x00000002
            Property:   PAC Write-Protection


      Bit        31           30           29           28           27           26            25               24


  Access
   Reset


      Bit        23           22           21           20           19           18            17               16


  Access
   Reset


      Bit        15           14           13           12           11           10            9                 8


  Access
   Reset


      Bit         7            6            5            4            3            2            1                 0
                                                    ETBRAMEN        DCCDMALEVEL[1:0]                 LQOS[1:0]
  Access                                                R/W          R/W          R/W          R/W               R/W
   Reset                                                 0            0            0            1                 0


            Bit 4 – ETBRAMEN Trace Control
            ETB Ram Enable Writing a one to this bit will reserve the first 32KB of the RAM for the Trace ETB ram
            buffer. Refer to Memories / SRAM Memory Configuration section for details.

            Bits 3:2 – DCCDMALEVEL[1:0] DMA Trigger Level
            Value       Description
            0x0         DMA Trigger rises when DCC is empty.
            0x1         DMA Trigger rises when DCC is full.
            0x2 -       Reserved
            0x3

            Bits 1:0 – LQOS[1:0] Latency Quality Of Service
            These bits define the priority access during the memory access. Refer to SRAM Quality of Service.




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 128
                                                           SAM D5x/E5x Family Data Sheet
                                                                              DSU - Device Service Unit

12.13.10 Device Configuration

            Name:       DCFG
            Offset:     0xF0 + n*0x04 [n=0..1]
            Reset:      0x00000000
            Property:   PAC Write-Protection


      Bit        31           30           29        28                 27   26       25           24
                                                          DCFG[31:24]
  Access
   Reset         0             0           0          0                 0    0         0           0


      Bit        23           22           21        20                 19   18       17           16
                                                          DCFG[23:16]
  Access
   Reset         0             0           0          0                 0    0         0           0


      Bit        15           14           13        12                 11   10        9           8
                                                          DCFG[15:8]
  Access
   Reset         0             0           0          0                 0    0         0           0


      Bit        7             6           5          4                 3    2         1           0
                                                           DCFG[7:0]
  Access
   Reset         0             0           0          0                 0    0         0           0


            Bits 31:0 – DCFG[31:0] Device Configuration




        © 2019 Microchip Technology Inc.                     Datasheet                 DS60001507E-page 129
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                         DSU - Device Service Unit

12.13.11 CoreSight ROM Table Entry x

            Name:        ENTRY
            Offset:      0x1000 + n*0x04 [n=0..1]
            Reset:       0xxxxxx00x
            Property:    PAC Write-Protection


      Bit        31             30                 29       28             27           26            25            24
                                                             ADDOFF[19:12]
  Access          R             R                  R        R                  R        R             R             R
   Reset          x             x                  x        x                  x        x             x              x


      Bit        23             22                 21       20             19           18            17            16
                                                                ADDOFF[11:4]
  Access          R             R                  R        R                  R        R             R             R
   Reset          x             x                  x        x                  x        x             x              x


      Bit        15             14                 13       12             11           10            9              8
                                     ADDOFF[3:0]
  Access          R             R                  R        R
   Reset          x             x                  x        x


      Bit         7             6                  5        4                  3        2             1              0
                                                                                                     FMT           EPRES
  Access                                                                                              R             R
   Reset                                                                                              1              x


            Bits 31:12 – ADDOFF[19:0] Address Offset
            The base address of the component, relative to the base address of this ROM table.

            Bit 1 – FMT Format
            Always reads as '1', indicating a 32-bit ROM table.

            Bit 0 – EPRES Entry Present
            This bit indicates whether an entry is present at this location in the ROM table.
            This bit is set at power-up if the device is not protected indicating that the entry is not present.
            This bit is cleared at power-up if the device is not protected indicating that the entry is present.




        © 2019 Microchip Technology Inc.                            Datasheet                          DS60001507E-page 130
                                                             SAM D5x/E5x Family Data Sheet
                                                                               DSU - Device Service Unit

12.13.12 CoreSight ROM Table End

           Name:       END
           Offset:     0x1008
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29           28                27   26       25           24
                                                            END[31:24]
  Access        R             R           R             R                R    R         R           R
   Reset         0            0            0            0                0    0         0           0


     Bit        23           22           21           20                19   18       17           16
                                                            END[23:16]
  Access        R             R           R             R                R    R         R           R
   Reset         0            0            0            0                0    0         0           0


     Bit        15           14           13           12                11   10        9           8
                                                            END[15:8]
  Access        R             R           R             R                R    R         R           R
   Reset         0            0            0            0                0    0         0           0


     Bit         7            6            5            4                3    2         1           0
                                                             END[7:0]
  Access        R             R           R             R                R    R         R           R
   Reset         0            0            0            0                0    0         0           0


           Bits 31:0 – END[31:0] End Marker
           Indicates the end of the CoreSight ROM table entries.




       © 2019 Microchip Technology Inc.                        Datasheet                DS60001507E-page 131
                                                              SAM D5x/E5x Family Data Sheet
                                                                                      DSU - Device Service Unit

12.13.13 CoreSight ROM Table Memory Type

           Name:        MEMTYPE
           Offset:      0x1FCC
           Reset:       0x0000000x
           Property:    -


     Bit        31            30            29           28            27            26           25            24


  Access
   Reset


     Bit        23            22            21           20            19            18           17            16


  Access
   Reset


     Bit        15            14            13           12            11            10            9            8


  Access
   Reset


     Bit         7            6             5             4            3             2             1            0
                                                                                                             SMEMP
  Access                                                                                                        R
   Reset                                                                                                        x


           Bit 0 – SMEMP System Memory Present
           This bit indicates whether system memory is present on the bus that connects to the ROM table.
           This bit is set at power-up if the device is not protected, indicating that the system memory is accessible
           from a debug adapter.
           This bit is cleared at power-up if the device is protected, indicating that the system memory is not
           accessible from a debug adapter.




       © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 132
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   DSU - Device Service Unit

12.13.14 Peripheral Identification 4

            Name:       PID4
            Offset:     0x1FD0
            Reset:      0x00000000
            Property:   -


      Bit        31           30               29       28           27          26                25          24


   Access
    Reset


      Bit        23           22               21       20           19          18                17          16


   Access
    Reset


      Bit        15           14               13       12           11          10                9           8


   Access
    Reset


      Bit        7             6               5        4            3            2                1           0
                                   FKBC[3:0]                                          JEPCC[3:0]
   Access        R             R               R        R            R            R                R           R
    Reset        0             0               0        0            0            0                0           0


            Bits 7:4 – FKBC[3:0] 4KB Count
            These bits will always return zero when read, indicating that this debug component occupies one 4KB
            block.

            Bits 3:0 – JEPCC[3:0] JEP-106 Continuation Code
            These bits will always return zero when read.




        © 2019 Microchip Technology Inc.                     Datasheet                             DS60001507E-page 133
                                                     SAM D5x/E5x Family Data Sheet
                                                                  DSU - Device Service Unit

12.13.15 Peripheral Identification 7

            Name:       PID7
            Offset:     0x1FDC
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31           30           29   28         27    26       25           24


   Access
    Reset


      Bit        23           22           21   20         19    18       17           16


   Access
    Reset


      Bit        15           14           13   12         11    10        9           8


   Access
    Reset


      Bit        7             6           5    4          3     2         1           0


   Access
    Reset




        © 2019 Microchip Technology Inc.             Datasheet             DS60001507E-page 134
                                                     SAM D5x/E5x Family Data Sheet
                                                                  DSU - Device Service Unit

12.13.16 Peripheral Identification 6

            Name:       PID6
            Offset:     0x1FD8
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31           30           29   28         27    26       25           24


   Access
    Reset


      Bit        23           22           21   20         19    18       17           16


   Access
    Reset


      Bit        15           14           13   12         11    10        9           8


   Access
    Reset


      Bit        7             6           5    4          3     2         1           0


   Access
    Reset




        © 2019 Microchip Technology Inc.             Datasheet             DS60001507E-page 135
                                                     SAM D5x/E5x Family Data Sheet
                                                                  DSU - Device Service Unit

12.13.17 Peripheral Identification 5

            Name:       PID5
            Offset:     0x1FD4
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31           30           29   28         27    26       25           24


   Access
    Reset


      Bit        23           22           21   20         19    18       17           16


   Access
    Reset


      Bit        15           14           13   12         11    10        9           8


   Access
    Reset


      Bit        7             6           5    4          3     2         1           0


   Access
    Reset




        © 2019 Microchip Technology Inc.             Datasheet             DS60001507E-page 136
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   DSU - Device Service Unit

12.13.18 Peripheral Identification 0

            Name:       PID0
            Offset:     0x1FE0
            Reset:      0x00000000
            Property:   -


      Bit        31           30           29           28             27        26           25           24


   Access
    Reset


      Bit        23           22           21           20             19        18           17           16


   Access
    Reset


      Bit        15           14           13           12             11        10            9            8


   Access
    Reset


      Bit        7             6           5            4                  3      2            1            0
                                                            PARTNBL[7:0]
   Access        R             R           R            R                  R      R            R            R
    Reset        0             0           0            0                  0      0            0            0


            Bits 7:0 – PARTNBL[7:0] Part Number Low
            These bits will always return 0xD0 when read, indicating that this device implements a DSU module
            instance.




        © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 137
                                                             SAM D5x/E5x Family Data Sheet
                                                                                    DSU - Device Service Unit

12.13.19 Peripheral Identification 1

            Name:       PID1
            Offset:     0x1FE4
            Reset:      0x000000FC
            Property:   -


      Bit        31           30                  29    28            27           26             25              24


   Access
    Reset


      Bit        23           22                  21    20            19           18             17              16


   Access
    Reset


      Bit        15           14                  13    12            11           10                 9           8


   Access
    Reset


      Bit         7            6                  5      4            3            2                  1           0
                                   JEPIDCL[3:0]                                        PARTNBH[3:0]
   Access        R             R                  R      R            R            R              R               R
    Reset         1            1                  1      1            1            1                  0           0


            Bits 7:4 – JEPIDCL[3:0] Low Part of the JEP-106 Identity Code
            These bits will always return 0xF when read (JEP-106 identity code is 0x1F).

            Bits 3:0 – PARTNBH[3:0] Part Number High
            These bits will always return 0xC when read, indicating that this device implements a DSU module
            instance.




        © 2019 Microchip Technology Inc.                      Datasheet                               DS60001507E-page 138
                                                              SAM D5x/E5x Family Data Sheet
                                                                                     DSU - Device Service Unit

12.13.20 Peripheral Identification 2

            Name:       PID2
            Offset:     0x1FE8
            Reset:      0x00000009
            Property:   -


      Bit        31            30              29        28            27           26             25            24


   Access
    Reset


      Bit        23            22              21        20            19           18             17            16


   Access
    Reset


      Bit        15            14              13        12            11           10              9            8


   Access
    Reset


      Bit         7            6                   5      4            3            2               1            0
                                   REVISION[3:0]                     JEPU                      JEPIDCH[2:0]
   Access         R            R               R          R            R            R               R            R
    Reset         0            0                   0      0            1            0               0            1


            Bits 7:4 – REVISION[3:0] Revision Number
            Revision of the peripheral. Starts at 0x0 and increments by one at both major and minor revisions.

            Bit 3 – JEPU JEP-106 Identity Code is Used
            This bit will always return one when read, indicating that JEP-106 code is used.

            Bits 2:0 – JEPIDCH[2:0] JEP-106 Identity Code High
            These bits will always return 0x1 when read, (JEP-106 identity code is 0x1F).




        © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 139
                                                                SAM D5x/E5x Family Data Sheet
                                                                             DSU - Device Service Unit

12.13.21 Peripheral Identification 3

            Name:       PID3
            Offset:     0x1FEC
            Reset:      0x00000000
            Property:   -


      Bit        31           30                 29        28         27    26            25              24


   Access
    Reset


      Bit        23           22                 21        20         19    18            17              16


   Access
    Reset


      Bit        15           14                 13        12         11    10                9           8


   Access
    Reset


      Bit         7            6                 5         4          3     2                 1           0
                                   REVAND[3:0]                                  CUSMOD[3:0]
   Access        R             R                 R         R          R     R                 R           R
    Reset         0            0                 0         0          0     0                 0           0


            Bits 7:4 – REVAND[3:0] Revision Number
            These bits will always return 0x0 when read.

            Bits 3:0 – CUSMOD[3:0] ARM CUSMOD
            These bits will always return 0x0 when read.




        © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 140
                                                            SAM D5x/E5x Family Data Sheet
                                                                         DSU - Device Service Unit

12.13.22 Component Identification 0

            Name:       CID0
            Offset:     0x1FF0
            Reset:      0x0000000D
            Property:   -


      Bit        31           30           29          28         27    26       25           24


  Access
   Reset


      Bit        23           22           21          20         19    18       17           16


  Access
   Reset


      Bit        15           14           13          12         11    10        9           8


  Access
   Reset


      Bit        7             6           5           4           3    2         1           0
                                                      PREAMBLEB0[7:0]
  Access         R             R           R           R           R    R         R           R
   Reset         0             0           0           0           1    1         0           1


            Bits 7:0 – PREAMBLEB0[7:0] Preamble Byte 0
            These bits will always return 0x0000000D when read.




        © 2019 Microchip Technology Inc.                    Datasheet             DS60001507E-page 141
                                                                SAM D5x/E5x Family Data Sheet
                                                                                  DSU - Device Service Unit

12.13.23 Component Identification 1

            Name:       CID1
            Offset:     0x1FF4
            Reset:      0x00000010
            Property:   -


      Bit        31           30                 29     28            27         26           25           24


  Access
   Reset


      Bit        23           22                 21     20            19         18           17           16


  Access
   Reset


      Bit        15           14                 13     12            11         10           9            8


  Access
   Reset


      Bit         7            6                 5          4         3          2            1            0
                                   CCLASS[3:0]                                    PREAMBLE[3:0]
  Access         R             R                 R      R             R          R            R            R
   Reset          0            0                 0          1         0          0            0            0


            Bits 7:4 – CCLASS[3:0] Component Class
            These bits will always return 0x1 when read indicating that this ARM CoreSight component is ROM table
            (refer to the ARM Debug Interface v5 Architecture Specification at http://www.arm.com).

            Bits 3:0 – PREAMBLE[3:0] Preamble
            These bits will always return 0x00 when read.




        © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 142
                                                            SAM D5x/E5x Family Data Sheet
                                                                          DSU - Device Service Unit

12.13.24 Component Identification 2

            Name:       CID2
            Offset:     0x1FF8
            Reset:      0x00000005
            Property:   -


      Bit        31           30           29          28          27    26       25           24


  Access
   Reset


      Bit        23           22           21          20          19    18       17           16


  Access
   Reset


      Bit        15           14           13          12          11    10        9           8


  Access
   Reset


      Bit        7             6           5           4            3    2         1           0
                                                       PREAMBLEB2[7:0]
  Access         R             R           R           R            R    R         R           R
   Reset         0             0           0           0            0    1         0           1


            Bits 7:0 – PREAMBLEB2[7:0] Preamble Byte 2
            These bits will always return 0x00000005 when read.




        © 2019 Microchip Technology Inc.                    Datasheet              DS60001507E-page 143
                                                            SAM D5x/E5x Family Data Sheet
                                                                          DSU - Device Service Unit

12.13.25 Component Identification 3

            Name:       CID3
            Offset:     0x1FFC
            Reset:      0x000000B1
            Property:   -


      Bit        31           30           29          28          27    26       25           24


  Access
   Reset


      Bit        23           22           21          20          19    18       17           16


  Access
   Reset


      Bit        15           14           13          12          11    10        9           8


  Access
   Reset


      Bit        7             6           5           4            3    2         1           0
                                                       PREAMBLEB3[7:0]
  Access         R             R           R           R            R    R         R           R
   Reset         1             0           1           1            0    0         0           1


            Bits 7:0 – PREAMBLEB3[7:0] Preamble Byte 3
            These bits will always return 0x000000B1 when read.




        © 2019 Microchip Technology Inc.                    Datasheet              DS60001507E-page 144
