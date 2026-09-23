# 25. NVMCTRL – Nonvolatile Memory Controller

*Source: `Atmel-SAMD51.pdf`, pages 639-685 — SAMD51 family datasheet*

                                                        SAM D5x/E5x Family Data Sheet
                                                         NVMCTRL – Nonvolatile Memory Controller


25.    NVMCTRL – Nonvolatile Memory Controller

25.1   Overview
       Non-volatile memory (NVM) is a reprogrammable flash memory that retains program and data storage,
       even when powered off. The NVM Controller (NVMCTRL) embeds two banks; one bank can be read
       while the other is programmed (RWW). It is connected to the AHB and APB bus interfaces for system
       access to the NVM block. The AHB interfaces are used for reads and writes to the NVM block, while the
       APB interface is used for commands and configuration.



25.2   Features
         •   Two 32-bit AHB interfaces for reads and writes in the NVM main address space
         •   SmartEEPROM (integrated EEPROM emulation algorithm)
         •   Read while write (Any bank can be read while programming the other one)
         •   All NVM sections are memory mapped to the AHB, including calibration and system configuration
         •   32-bit APB interface for commands and control
         •   Programmable wait states for read optimization
         •   32 regions can be individually protected or unprotected
         •   Additional protection for boot loader
         •   Supports device protection through a security bit
         •   Interface to Power Manager to power-down flash blocks while in sleep modes
         •   Can optionally wake up on exit from sleep or on first access
         •   Single line cache per AHB interface
         •   Dual bank for safer application upgrade
         •   Error Correction Code (ECC)




       © 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 639
                                                           SAM D5x/E5x Family Data Sheet
                                                             NVMCTRL – Nonvolatile Memory Controller


25.3     Block Diagram
         Figure 25-1. Block Diagram
                            NVMCTRL
                                                                                                  NVM Block
               AHB0
                              Cache line 0                                                         PAGE BUFFER




                                                  AHBMUX
               AHB1
                              Cache line 1
                                                                                                      BANKA
               AHB2
                         SmartEEPROM
                                                              NVM Interface


                 APB                Command and
                                      Control                                                         BANKB




25.4     Signal Description
         Not applicable.



25.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described in the
         following sections.

25.5.1   Power Management
         The NVMCTRL will continue to operate in any sleep mode where the selected source clock is running.
         The NVMCTRL interrupts can be used to wake up the device from sleep modes.
         The NVM block can be put into a low-power mode either automatically when the Power Manager enters
         standby mode, or when the SPRM command is issued. The NVMCTRL can wake-up when the Power
         Manager leaves sleep mode or on AHB access or when a command requires the NVM to be active. This
         is based on the Control A register (CTRLA) PRM bit setting. Read the CTRLA register description for
         more details.
         NVM wake-up time can be traded with static power consumption depending on the PM
         STDBYCFG.FASTWKUP setting.
         Related Links
         18. PM – Power Manager

25.5.2   Clocks
         Two synchronous clocks are used by the NVMCTRL. One is provided by the AHB bus
         (CLK_NVMCTRL_AHB) and the other is provided by the APB bus (CLK_NVMCTRL_APB). When
         changing the AHB bus frequency, the user must ensure that the NVM Controller is configured with the




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 640
                                                           SAM D5x/E5x Family Data Sheet
                                                             NVMCTRL – Nonvolatile Memory Controller

         proper number of wait states. Refer to the Electrical Characteristics for the exact number of wait states to
         be used for a particular frequency range. Automatic wait state generation can be use by setting the Auto
         Wait State bit in the Control A register (NVMCTRL.CTRLA.AUTOWS). Alternatively a custom
         programmable number of wait states can be set by writing the NVM Read Wait State bits
         (NVMCTRL.CTRLA.RWS) to optimize performance.
         Related Links
         25.8.1 CTRLA

25.5.3   DMA
         The NVMCTRL supports AHB burst transfers. It is possible to write the page buffer in sequence without
         AHB rearbitration in case of concurrent AHB writes to the page buffer to guarantee data integrity.

25.5.4   Interrupts
         The NVM Controller interrupt request line is connected to the interrupt controller. Using the NVMCTRL
         interrupt requires the interrupt controller to be programmed first.

25.5.5   Debug Operation
         When the CPU is halted in debug mode, the ECC feature of the NVMCTRL will correct and log ECC
         errors based on the table below.
         Table 25-1. ECC Debug Operation

          DBGCTRL.ECCELOG DBGCTRL.ECCDIS DBGCTRL.ECCDIS
          0                            0                 ECC errors from debugger reads are corrected, but not
                                                         logged in INTFLAG.
          1                            0                 ECC errors from debugger reads are corrected and
                                                         logged in INTFLAG.
          X                            1                 ECC errors from debugger reads are neither corrected
                                                         nor logged in INTFLAG.

         Reading the SmartEEPROM configured in buffered mode with a debugger is intrusive, since the
         pagebuffer must be flushed when the read is performed in a page under modification.
         Access to the NVM block can be protected by the security bit. In this case, the NVM block will not be
         accessible. See the section on the NVMCTRL 25.6.10 Security Bit for details.

25.5.6   Register Access Protection
         All registers with write-access are optionally write-protected by the Peripheral Access Controller (PAC),
         except the Interrupt Flag Status and Clear register (INTFLAG).
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.

         Related Links
         27. PAC - Peripheral Access Controller

25.5.7   Analog Connections
         Not applicable.




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 641
                                                         SAM D5x/E5x Family Data Sheet
                                                           NVMCTRL – Nonvolatile Memory Controller


25.6      Functional Description

25.6.1    Principle of Operation
          The NVM Controller is a slave on the AHB (AHB0, AHB1 and AHB2) and APB buses. It responds to
          commands, read requests and write requests, based on user configuration. AHB0 and AHB1 allow
          access to the NVM main address space, the auxiliarry space and the page buffer. AHB2 provides access
          to the SmartEEPROM interface that indirecly accesses the reserved area in the NVM for EEPROM
          emulation.
25.6.1.1 Initialization
          After power-up, the NVM Controller goes through a power-up sequence. During this time, access to the
          NVM Controller from the AHB bus is halted. Upon power-up completion, the NVM Controller is
          operational without any need for user configuration.
25.6.1.2 Software Reset
          Software reset is triggered by the SWRST command, and does the following:
           • NVM (physical memory) reset
           • Device power-up sequence (redo the device calibration)
           • Reset all APB configuration registers (and status)
          Note:
          STATUS.READY goes low when the SWRST command starts to execute.
          STATUS.READY goes high when the SWRST command has completed.
          Any AHB0/1/2 access is stalled until the command has completed.

25.6.2    Memory Organization
          Memory space is divided in two:
           • The main address space where 2 physical NVM banks (BANKA and BANKB) are mapped.
           • The auxiliary space which contains:
              – The User page (USER)
              – The calibration page (CB)
              – Factory and signature pages (FS)
          BANKA and BANKB can be swapped in the address space. For more information, see Memory Bank
          Swapping.
          Refer to the Physical Memory Map for memory sizes and addresses for each device.
          BANKA, BANKB and AUX pages have different erase and write granularities, see the table below.
          Table 25-2. Erase and Write granularity

                                            Erase Granularity                  Write Granularity
          BANKA                             Block                              Quad-Word or Page
          BANKB                             Block                              Quad-Word or Page
          AUX                               Page                               Quad-Word

          The NVM is organized into two banks, each bank is organized into blocks, where each block contains
          sixteen pages.




         © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 642
                                                     SAM D5x/E5x Family Data Sheet
                                                     NVMCTRL – Nonvolatile Memory Controller

The lower blocks in the NVM main address space can be allocated as a boot loader section by using the
BOOTPROT fuses, and the upper rows can be allocated to EEPROM.
The NVM memory is separated into six parts:
  1.   CB space
       Contains factory calibration and system configuration information.
        – Address; 0x00800000
        – Size: 1 page
        – Property: Read-Only
  2.   FS space
       Contains the factory signature information.
        – Address; 0x00806000
        – Size: 4 pages
        – Property: Read-Only.
  3.   USER space
       Contains user defined startup configuration. The first word is reserved, and used during the
       NVMCTRL start-up to automatically configure the device.
         – Address: 0x00804000
         – Size: 1 page
         – Property: Read-Write
  4.   Main address space
       The main address space is divided into 32 equally sized regions. Each region can be protected
       against write or erase operation. The 32-bit RUNLOCK register reflects the protection of each
       region. This register is automatically updated after power-up with the region lock user fuse data; To
       lock or unlock a region, the LR or UR commmands can be issued.
         – Address: 0x00000000
         – Size: PARAM.NVMP pages.
         – Property: Read-Write
  5.   Bootloader space
       The bootloader section starts at the beginning of the main address space; Its size is defined by the
       BOOTPROT[3:0] fuse. It is protected against write or erase operations, except if STATUS.BPDIS is
       set. Issuing a write or erase command at an address inside the BOOTPROT section sets
       STATUS.PROGE and STATUS.LOCKE. STATUS.BPDIS can be set by issuing the Set BOOTPROT
       Disable command (SBPDIS). It is cleared by issuing the Clear BOOTPROT Disable command
       (CBPDIS). This allows to program an new bootloader without changing the user page and issuing a
       new NVMCTRL startup sequence to reload the user configuration. The BOOTPROT section is not
       erased during a Chip-Erase operation even if STATUS.BPDIS is high.
        – Address: 0x00000000
        – Size: (15 - STATUS.BOOTPROT) × 8192
        – Property: Read-Only.
  6.   SmartEEPROM raw data space
       The SmartEEPROM algorithm emulates an EEPROM with a portion of the NVM main. Smart-
       EEPROM raw data is mapped at the end of the main address space. SmartEEPROM allocated
       space in the main address space is not accessible from AHB0/1. Any AHB access throws a




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 643
                                                               SAM D5x/E5x Family Data Sheet
                                                                NVMCTRL – Nonvolatile Memory Controller

                hardfault exception. Any command issued with ADDR pointing in the SmartEEPPROM space is
                discarded, INTFLAG.DONE and INTFLAG.ADDRE are set in this case.
                  – Address: PARAM.NVMP*512-2*SEESTAT.SBLK*8192
                  – Size: 2*SEESTAT.SBLK*8192
                  – Property: Not readable, not writeable
         Each section has different protection status, refer to the table below.
         Table 25-3. Protection status

          Section/Operation                 Write protection       Erase protection          Chip-Erase protection
          Bootloader                        Yes                    Yes                       Yes
          SmartEEPROM                       Configurable           Configurable              No
          Main Array                        Configurable           Configurable              No

         Related Links
         9.2 Physical Memory Map
         12. DSU - Device Service Unit

25.6.3   Memory Bank Swapping
         The two physical banks BANKA and BANKB are mapped in the NVM main address space and can be
         swapped. If STATUS.AFIRST contains '1', then BANKA is mapped to the NVM main address space Base
         Address, otherwise it is BANKB.
         The start address of BANKA & BANKB depends on STATUS.AFIRST and on the size of the Flash. Refer
         to the Physical Memory Map for memory sizes and addresses for each device.
         Related Links
         9.2 Physical Memory Map

25.6.4   AHBMUX Arbitration
         The AHBMUX arbitrates concurrent AHB0, AHB1 and SmartEEPROM accesses using a fixed priority
         scheme:
           • AHB0 has the highest priority
           • AHB1 has priority over SmartEEPROM
           • AHB2 has the lowest priority
         However, once a transfer has been accepted the AHB data phase must complete, meaning that a
         transaction can be stalled by a previously granted access with a lower priority. This can occur in
         Automatic Wait State mode or in Fixed Wait State mode when the Wait state is greater than zero.
         AHBMUX doesn’t rearbitrate AHB burst transactions. This is useful in case of concurrent write transfers to
         the page buffer. If used in conjunction with the automatic write features (ADW, AQW, APW) and if the
         burst transfer size is a multiple of the automatic write size, several masters can write the NVM without
         implementing any software semaphore checks.
         It is possible to force the rearbitration in case of burst transfers, as follows:
           • on AHB0: by writing a ‘1’ to CTRLA.AHBNS0
           • on AHB1: by writing a ‘1’ to CTRLA.AHBNS1




         © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 644
                                                            SAM D5x/E5x Family Data Sheet
                                                             NVMCTRL – Nonvolatile Memory Controller

         Related Links
         10.3 High-Speed Bus System

25.6.5   Region Lock Bits
         The NVM main address space is accessible through the AHB0 or AHB1 interfaces, and grouped into 32
         equally sized regions regardless of BOOTPROT or SmartEEPROM settings. The region size is
         dependent on the flash memory size, and is given in the table below. Each region has a dedicated lock bit
         preventing writing and erasing pages in the region. After production, all regions will be unlocked.
         Table 25-4. Region Size

          Memory Size [KB]                                       Region Size [KB]
          1024                                                   32
          512                                                    16
          256                                                    8

         To lock or unlock a region, the Lock Region and Unlock Region commands are provided. Writing one of
         these commands will temporarily lock/unlock the region containing the address loaded in the ADDR
         register. ADDR can be written by software, or the automatically loaded value from a AHB write operation
         can be used. The new setting will stay in effect until the next reset, or the setting can be changed again
         using the lock and unlock commands. The current status of the lock can be determined by reading the
         RUNLOCK register.
         To change the default lock/unlock setting for a region, the user page must be written. Writing to the
         auxiliary space will take effect after the next reset. Therefore, a boot of the device is needed for changes
         in the lock/unlock setting to take effect. Refer to the Physical Memory Map for calibration and auxiliary
         space address mapping.
         Related Links
         9.2 Physical Memory Map

25.6.6   Command and Data Interface
         The NVM Controller is addressable from the APB bus, while the NVM main address space is addressable
         from the AHB bus. Read and automatic page write operations are performed by addressing the NVM
         main address space directly, while other operations such as manual page writes and block erase must be
         performed by issuing commands through the NVM Controller.
         To issue a command, the CTRLB.CMD bits must be written along with the CTRLB.CMDEX value.
         STATUS.READY is cleared when a command is issued and set when it has completed. Any command
         written while STATUS.READY is low will be ignored causing INTFLAG.PROGE to rise. Refer to CTRLB
         register description for more details.
         Invalid commands are discarded and will set INTFLAG.PROGE and INTFLAG.DONE when issued.
         The CTRLA register must be used to control the power reduction mode, read wait states and the write
         mode.
         Commands that require an address use the ADDR register as an argument. ADDR APB write access is
         locked by the NVMCTRL while being used internally. For instance if a write operation is started by the
         NVMCTRL, an APB write is discarded so that the write operation is performed at the correct address. The
         discarded APB write is signaled by rising INTFLAG.ADDRE. Commands that needs an address will fail if
         issued while INTFLAG.ADDRE is set, such failure is signaled by rising INTFLAG.PROGE.




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 645
                                                           SAM D5x/E5x Family Data Sheet
                                                            NVMCTRL – Nonvolatile Memory Controller

        The APB ADDR register is updated upon:
         • APB writes to the ADDR register address
         • AHB writes to the page buffer
        ADDR APB writes are discarded and report an INTFLAG.ADDRE error in the following cases:
         • When written from APB while a command is reading it.
         • ADDR APB write access while writing the page buffer (AHB write): ADDR is written upon AHB writes
           and must stay valid until the page buffer has been written and also until automatic write command
           has been issued to the command interface when in automatic write mode (WMODE configured as
           ADW or AQW or AP).
         • ADDR APB write access while the command interface reads it.
         • A command is executed at an illegal address
        All commands that require an address are discarded when INTFLAG.ADDRE is set. INTFLAG.PROGE is
        set in this case. INTFLAG.ADDRE must be cleared before issuing such commands.
25.6.6.1 NVM Read
        Reading from the NVM main address space is performed via the AHB bus by addressing the NVM main
        address space or auxiliary address space directly. Read data is available after the number of read wait
        states has passed as configured in NVMCTRL.CTRLA.RWS.
        The number of cycles data are delayed to the AHB bus is determined by the read wait states.
        It is not possible to read two banks at the same time. In case of simultaneous read operations,
        transactions are arbitrated by the internal matrix. Arbitration scheme is fixed priority, AHB0 has the
        highest priority, AHB1 has priority over AHB2. In case of conflict, AHB interfaces with lower priority are
        stalled.
        Reading in a bank stalls the bus when it is being programmed or erased except when the suspend
        feature is used.
        Reading in a bank does not stall the bus when the other bank is being programmed or erased.
        Related Links
        25.6.6.4 Suspend/Resume

25.6.6.2 NVM Write
        The entire NVM main address space except the BOOTPROT section can be erased by a debugger Chip
        Erase command. Alternatively, blocks or pages can be individually erased using the Erase Page (EP) or
        Erase Block (EB) depending on the targeted address space. The NVM can be programmed using the
        Write Page (WP) or Write Quad Word (WQW) commands depending on the targeted address space. AHB
        writes automatically update the ADDR register. ADDR is write locked by the NVMCTRL until the
        pagebuffer write completes or until the appropriate write command has been passed to the command
        interface when in automatic write mode. Write commands are not supported in all address spaces, see
        the table below. These commands are detailed further in this section.
        Table 25-5. Supported commands per address space

                                          WP               WQW                     EP                    EB
         Main Address                     X                   X                                           X
         Space




       © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 646
                                                  SAM D5x/E5x Family Data Sheet
                                                   NVMCTRL – Nonvolatile Memory Controller

...........continued
                                   WP             WQW                    EP                   EB
 User Page Address                                  X                     X
 Space

Issuing an unsupported command on an address space sets the PROGE interrupt flag.
After programming the NVM main array, the region that the page resides in can be locked to prevent
spurious write or erase sequences. Locking is performed on a per-region basis, and so locking a region
locks all pages inside the region.
Data to be written to the NVM block is written through AHB and stored in an internal buffer called the
page buffer. If the NVMCTRL is busy processing a write command (STATUS.READY=0) then the AHB
bus is stalled upon an AHB write until the ongoing command completes. Writing the page buffer is
allowed during a block erase operation. The page buffer contains the same number of bytes as an NVM
page. Writes to the page buffer must be 32 bits. 16-bit or 8-bit writes to the page buffer is not allowed,
and will cause a PAC error. Internally, writes to the page buffer are on a 64-bit basis through the page
buffer load data registers (PBLDATA[1] and PBLDATA[0]). The PBLDATA register is a holding register for
writes to the same 64-bit page buffer section. Data within a 64-bit section can be written in any order.
Crossing a 64- bit boundary will reset the PBLDATA register to all ones. The following example assumes
startup from reset where the current address is 0 and PBLDATA is all ones. Only 64 bits of the page
buffer are written at a time, but 128 bits are shown for reference.
Sequential 32-bit write example:
  • 32-bit 0x1 written to address 0
     – Page buffer[127:0] = {0xFFFFFFFF_FFFFFFFF, PBLDATA[63:32], 0x00000001}
     – PBLDATA[63:0] = {PBLDATA[63:32], 0x00000001}
  • 32-bit 0x2 written to address 1
     – Page buffer[127:0] = {0xFFFFFFFF_FFFFFFFF, 0x00000002, PBLDATA[31:0]
     – PBLDATA[63:0] = 0x00000002, PBLDATA[31:0]}
  • 32-bit 0x3 written to address 2 (crosses 64-bit boundary)
     – Page buffer[127:0] = 0xFFFFFFFF_00000003_00000002_00000001
     – PBLDATA[63:0] = 0xFFFFFFFF_00000003
Random access writes to 32-bit words within the page buffer will overwrite the opposite word within the
same 64-bit section with ones. In the following example, notice that 0x00000001 is overwritten with
0xFFFFFFFF from the third write due to the 64-bit boundary crossing. Only 64 bits of the page buffer are
written at a time, but 128 bits are shown for reference.
Random access 32-bit AHB write example:
  • 32-bit 0x1 written to address 2
     – Page buffer[127:0] = 0xFFFFFFFF_00000001_FFFFFFFF_FFFFFFFF
     – PBLDATA[63:0] = 0xFFFFFFFF_00000001
  • 32-bit 0x2 written to address 1
     – Page buffer[127:0] = 0xFFFFFFFF_00000001_00000002_FFFFFFFF
     – PBLDATA[63:0] = 0x00000002_FFFFFFFF
  • 32-bit 0x3 written to address 3
     – Page buffer[127:0] = 0x00000003_FFFFFFFF_00000002_FFFFFFFF




© 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 647
                                                 SAM D5x/E5x Family Data Sheet
                                                  NVMCTRL – Nonvolatile Memory Controller

       – PBLDATA[63:0] = 0x00000003_0xFFFFFFFF
BANKA and BANKB share the same page buffer. Writing to the NVM block via the AHB bus is buffered in
the page buffer. For each AHB bus write, the address is stored in the ADDR register. After the page buffer
has been loaded with the required number of bytes, the page can be written to the addressed location by
setting CMD to Write Page to write the NVM main array and setting the key value to CMDEX. The LOAD
bit in the STATUS register indicates whether the page buffer has been loaded or not. Before writing the
page to memory, the accessed block must be erased.
Several write modes are supported and configured through CTRLA.WMODE.
  • Manual (MAN):
This is the default configuration. Because the address is automatically stored in ADDR during AHB write
operations, the last given address will be present in the ADDR register. There is no need to load the
ADDR register manually, unless a different page in memory is to be written. A write should be issued
before writing to a different page.
  • Automatic Write With Double Word Granularity (ADW):
Automatically writes data with double-word granularity. In this case the WQW command is triggered at the
quad-word addressed by ADDR when the last word in a double-word aligned block is written. The other
double-word inside the page buffer must be all one. STATUS.READY goes low during the NVM write
operation. INTFLAG.DONE flag is set upon completion.
  • Automatic Write With Quad Word Granularity (AQW):
Automatically writes data with quad-word granularity. In this case the WQW command is triggered at the
quad-word addressed by ADDR when the last word in a quad-word aligned block is written.
STATUS.READY goes low during the NVM write operation. INTFLAG.DONE flag is set upon completion.
  • Automatic Write With Page Granularity (AP)
Automatically writes data with page granularity. In this case the WP command is triggered at the page
addressed by ADDR when the last word in a page aligned block is written. STATUS.READY goes low
during the NVM write operation. INTFLAG.DONE flag is set upon completion.
These write modes are supported for writes in the main address space and in the USER page. The
USER page doesn’t support write page, if the AP mode is selected writes in the USER page will be done
in AQW mode. This avoids to change WMODE by software while mixing writes in the main address space
and in the USER page.
Procedure for Manual Page Writes (WMODE=MAN)
The block to be written must be erased before the write command is given.
  • Write to the page buffer by addressing the NVM main address space directly
  • Write the page buffer to memory:
      – CMD=WP (and CMDEX) to write the full content of the page buffer into the NVM at the page
        pointed by ADDR
      – CMD=WQW (and CMDEX) to write into the NVM the page buffer quad word pointed by ADDR
  • The READY bit in the STATUS register will be low while programming is in progress, and access
    through the AHB in the same bank will be stalled.
Procedure for Automatic Writes (WMODE=ADW or AQW or APW)




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 648
                                                          SAM D5x/E5x Family Data Sheet
                                                           NVMCTRL – Nonvolatile Memory Controller

        The block to be written must be erased before the last write to the page buffer is performed. The internal
        write operation will begin when the second word is written for WMODE = ADW, when the fourth word is
        written for WMODE = AQW, and when the last word of the page is written for WMODE = APW.
        Note that partially written pages must be written with a manual write.
        If the command interface is already processing a command, the AHB is stalled until the automatic write
        command is taken. Therefore it is possible to chain write commands without polling STATUS.READY. For
        applications that must not stall the AHB bus the automatic write must be used carefully: STATUS.READY
        must be checked after each double-word or quad-word or page buffer write depending on WMODE
        before chaining with a new write to avoid stalling the bus.
          • Write to the page buffer by addressing the NVM main address space directly.
              – When the word location in the page buffer is written, the double word or quad word or page is
                 automatically written to NVM main address space.
          • STATUS.READY will be zero while programming is in progress and access through the AHB will be
            stalled.
        NVM Write Example (Manual Write mode)
         1. Configure manual write for the NVM using WMODE (NVMCTRL.CTRLA).
         2. Make sure the NVM is ready to accept a new command (NVMCTRL.STATUS).
         3. Clear page buffer ( NVMCTRL.CTRLB).
         4. Make sure NVM is ready to accept a new command (NVMCTRL.STATUS).
         5. Clear the DONE Flag (NVMCTRL.INTFLAG).
         6. Write data to page buffer with 32-bit accesses at the needed address.
         7. Perform page write (NVMCTRL.CTRLB).
         8. Make sure NVM is ready to accept a new command (NVMCTRL.STATUS).
         9. Clear the DONE Flag (NVMCTRL.INTFLAG).
25.6.6.3 Read While Write (RWW)
        This feature makes it possible to program and read the NVM simultaneously without stalling the AHB bus
        independantly from any cache consideration. The basic principle is that NVM is made of two banks, one
        can be read while the other is programmed.
        Limitations:
          • It is not possible to read both banks simultaneously, reads will be prioritized and issued in series.
          • It is not possible to program or erase both banks simultaneously, a new command will be accepted
            only after the completion of the previous one, otherwise the new command is ignored and
            INTFLAG.PROGE is set.
          • RWW is not possible when reading or programming auxilliary pages, any read will result in an AHB
            stall and the command interface doesn’t accept any command until completion of the previous one.
25.6.6.4 Suspend/Resume
        This feature can be enabled by writing a ‘1’ to CTRLA.SUSPEN. Any modify operation, such as write or
        erase can be suspended even those triggered by the SmartEEPROM.
        When enabled, the following commands are suspended by a NVM read request:
          • EB
          • WP




        © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 649
                                                          SAM D5x/E5x Family Data Sheet
                                                            NVMCTRL – Nonvolatile Memory Controller

        If a read occurs while executing one of the command listed above, the NVMCTRL will follow the following
        steps:
          1.     Send a suspend command to the NVM.
          2.     Wait for the NVM to be ready.
          3.     Read the NVM. The NVMCTRL will persist in this step when a new read request occurs, or else
                 proceed.
          4.     Resume the suspended operation.
        A suspend operation will set INTFLAG.SUSP. To clear it write a ‘1’ to INTFLAG.SUSP.
        The NVM suspended state is reflected in STATUS.SUSP.
        Limitations:
          • Suspend is not possible for a read in the page being programmed.
          • Suspend is not possible for a read in a sector (128KB) containing a block under erase.
          • It is not possible to enter power reduction mode when a command is suspended.
25.6.6.5 Page Buffer
        The page buffer is automatically cleared to all-ones after any page write operation (WP or WQW
        command). If a partial page has been written and it is desired to clear the contents of the page buffer, the
        Page Buffer Clear (PBC) command can be used. The status of the page buffer is given by
        STATUS.LOAD. This bit indicates that the NVM page buffer has been loaded with one or more words.
        Immediately after an NVM load has been performed, this flag is set, and it remains set until a WP or
        WQW or a PBC command is given.
        The Page Buffer cannot be written while a write command is executing in the NVM. Trying to do so stalls
        the AHB bus. To avoid stalling the AHB bus, STATUS.READY can by polled prior to issue a write
        command.
        Clearing the page buffer also clears to all ones the PBLDATA0 and PBLDATA1.
25.6.6.6 Erase
        Before a page can be written, it must be erased. The erase granularity depend on the address space
        (block or page). The Erase Block/Page command can be used to erase the desired block or page in the
        NVM main address space. Erasing the block/page sets all bits to ‘1’. If the block/page resides in a region
        that is locked, the erase will not be performed and the Lock Error bit in the INTFLAG register
        (INTFLAG.LOCKE) will be set. INTFLAG.PROGE will also be set since the command didn’t complete.
        The Erase Page command can be issued on the USER page in the auxiliary space.
        The procedure for an Erase Block/Page command is as follows:
          • Write the address of the block/page to erase to ADDR. Any address within the block/page can be
            used.
          • Issue an Erase Block/Page command.
        The page buffer can be written while an erase page or erase block is being performed.
25.6.6.7 Lock and Unlock Region
        The commands LR and UR are used to lock and unlock regions. These commands only update the
        RUNLOCK register but not the corresponding field in the user page.
        Related Links
        25.6.5 Region Lock Bits
        25.8.2 CTRLB




        © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 650
                                                      SAM D5x/E5x Family Data Sheet
                                                       NVMCTRL – Nonvolatile Memory Controller

25.6.6.8 Power Reduction Mode
        The NVM implements a power reduction mode which cuts its static power consumption. If a command or
        a AHB access is issued the NVM is woken-up. The AHB access or the command are processed after the
        NVM wake-up time. The wake-up time can be reduced by enabling the PM fast wake-up feature, this is
        configured through the PM STDBYCFG register.
        The NVM Power Reduction Mode is entered depending on the CTRLA.PRM mode:
         • MANUAL:
            – Power Reduction Mode entering conditions:
               • SPRM command
            – Power Reduction Mode leaving conditions:
               • AHB access (read or write)
               • CPRM or any other command
         • SEMIAUTO:
            – Power Reduction Mode entering conditions:
               • SPRM command
               • System enters standby mode
               • AHB access completes while in standby mode
               • Any command completes while in standby mode
            – Power Reduction Mode leaving conditions:
               • AHB access (read or write)
               • CPRM or any other command
         • FULLAUTO:
            – Power Reduction Mode entering conditions:
               • SPRM command
               • System enters standby mode
               • AHB access completes while in standby mode
               • Any command completes while in standby mode
            – Power Reduction Mode leaving conditions:
               • AHB access (read or write)
               • CPRM or any other command
               • When the system leaves the standby mode
        STATUS.READY is high when the NVM is in Power Reduction Mode indicating that the module can
        accept a command.
        STATUS.PRM is high when the NVM is in Power Reduction Mode.
        Note: It is not possible to enter power reduction mode when a command is suspended. Automatic power
        reduction entry is postponed until the command resumes and completes. The SPRM command is
        discarded when STATUS.SUSP is high and INTFLAG.PROGE is set.
        Related Links
        18. PM – Power Manager
        18.8.7 STDBYCFG




       © 2019 Microchip Technology Inc.                Datasheet                        DS60001507E-page 651
                                                              SAM D5x/E5x Family Data Sheet
                                                                NVMCTRL – Nonvolatile Memory Controller

25.6.7   Safe Flash Update Using Dual Banks
         This feature enables a firmware to execute from the NVM and at the same time program the Flash with a
         new version of itself.
         The new firmware has to be programmed in BANKB if STATUS.AFIRST=1, or BANKA otherwise.
         After programming is completed one can issue the BKSWRST command to swap the banks and to reset
         the device. The information of which BANK is mapped to the NVM main address space base address is
         self contained in the NVM using a special fuse that can be programmed or erased individually. This fuse
         is managed by the BKSWRST command. STATUS.AFIRST reflects the status of this fuse after Reset.
         The BKSWRST command is atomic meaning that no fetch in the NVM can occur while executing this
         command. This command executes with the following steps:
           1.   Stall AHB interfaces.
           2.   If PARAM.SEE is ‘1’ and 0<SEESTAT.SBLK<11, the NVMCTRL starts to reallocate the
                SmartEEPROM data to the first bank. Active SEES remains the same at the end of the reallocation.
           3.   Is STATUS.AFIRST=1: program the AFIRST fuse (new value=0) otherwise erase it (new value=1)
           4.   Resets the device, After reset, RSTC RCAUSE indicates that the reset was triggered by the
                NVMCTRL.
         After Reset the new firmware is executed from the last programmed bank.
         If the SmartEEPROM is configured, the size of the the reserved space in flash must not exceed the bank
         size. In other words 2*SEESTAT.SBLK.8192 must be lower than half the NVM size in Bytes. In situations
         where both the banks contain separate applications (or an application in one bank and a bootloader in the
         other bank), both the banks must have Flash area reserved for SmartEEPROM. This means that the
         usable area for code in each bank is "Size of the Bank", that is, the size of the Flash configured for the
         SmartEEPROM using SBLK Fuse.

25.6.8   SmartEEPROM

25.6.8.1 Principle of Operation
         The SmartEEPROM feature is provided through the AHB2 interface and makes a portion of the NVM
         appear like a RAM. 8-bit, 16-bit, 32-bit access is supported.
         The SmartEEPROM concept relies on the following NVM physical property: It is always possible to write a
         '0' in a NVM word, even if this word has been previously programmed - but it is not possible to write a '1'
         to a bit already programmed (holding a '0').
         The algorithm consists of virtually mapping physical portions of the NVM to logical addresses with an
         indirection mechanism. A physical page is assigned to a virtual page address and is kept as long as no
         bit has to be flipped from '0' to '1', as this operation requires a full block erase. In case such a transition is
         required, a new physical page is assigned to the modified virtual page (placed in the Flash area reserved
         for the SmartEEPROM). Writing the virtual page affects the cycling endurance of the SmartEEPROM.
         A region can overlap the SmartEEPROM region (depending on the allocated space for the
         SmartEEPROM), but SmartEEPROM is independent of the Region Lock Bits.
         If NVMCTRL.STATUS.AFIRST contains '1', BANKA is mapped to the NVM main address space base
         address (0x0000). In this case, SmartEEPROM will be in BANKB. Conversely, when BANKB is mapped
         to the NVM main address space base address, SmartEEPROM will be in BANKA. Thus, the CPU is not
         halted when accessing the SmartEEPROM.
25.6.8.2 Address Spaces
         The SmartEEPROM address space is divided in two distinct areas:




         © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 652
                                                           SAM D5x/E5x Family Data Sheet
                                                            NVMCTRL – Nonvolatile Memory Controller

          • DATA
             – Starts at offset 0x0
             – Size is 512B, 1KB, 2KB, 4KB, 8KB, 16KB, 32KB, 64KB depending on SEESTAT.PSZ and
               SEESTAT.SBLK (refer to “SmartEEPROM virtual size”)
             – This area is write protected if SEESTAT.LOCK is set. SEESTAT.LOCK is non volatile.
             – Commands LSEE and USEE respectively lock and unlock the SmartEEPROM.
          • REGISTER:
             – Starts at offset 0x10000
             – Size is 20B
             – This area is write protected if either
                 • SEESTAT.LOCK is set (non-volatile)
                 • SEESTAT.RLOCK is set (volatile).
         Commands LSEER and USEER respectively lock and unlock the SmartEEPROM register address space.
         As a consequence both SEESTAT.LOCK and SEESTAT.RLOCK must be low to write the SmartEEPROM
         register address space.
         Related Links
         25.6.8.4 SmartEEPROM Virtual Size

25.6.8.3 Data Structures
         The SmartEEPROM algorithm relies on two virtual sectors (SEES) physically located in the last blocks of:
          • BANKB if STATUS.AFIRST=1
          • BANKA if STATUS.AFIRST=0
         Only one SEES is active at a time, the other must be erased, ready for data reallocation.
         The current active SEES is indicated in SEESTAT.ASEES:
          • 0: SEES0 is active
          • 1: SEES1 is active
         SEESTAT.ASEES is loaded after Reset from a special fuse in the NVM which can be programmed or
         erased individually. This fuse can be set by issuing the ASEES1 command or cleared by issuing the
         ASEES0 command. SEESTAT.ASEES reflects this change immediately.
         The maximum number of virtual pages is limited to 128.
         A page allocation consists of assigning a SEEP to a virtual page for the first time. A page reallocation
         consists of assigning a new SEEP to an already existing virtual page. In both cases the selected virtual
         page index and the next available page are written.
         The SEEP size (PSZ) is configurable. The number of blocks allocated per SEES is configurable.
25.6.8.4 SmartEEPROM Virtual Size
         The SmartEEPROM interface virtual size is the maximum amount of data that can be stored in it. This
         defines the maximum size of this interface. Trying to read or write outside the boundaries throws an
         hardfault exception.
         The SBLK bits indicate the number of blocks allocated per SmartEEPROM virtual sector. The
         SmartEEPROM raw data resides in the upper blocks of the NVM main address space but is not
         accessible through AHB0 nor AHB1. The SmartEEPROM interface maximum size depends on
         SEESTAT.PSZ and SEESTAT.SBLK:




        © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 653
                                                            SAM D5x/E5x Family Data Sheet
                                                            NVMCTRL – Nonvolatile Memory Controller

        Table 25-6. SmartEEPROM Virtual Size in Bytes

        SEESTAT.PSZ: SEESTAT.SBLK                 4     8       16      32     64      128         256         512
        0                                         0     0       0       0      0       0           0           0
        1                                         512   1024    2048    4096   4096    4096        4096        4096
        2                                         512   1024    2048    4096   8192    8192        8192        8192
        3                                         512   1024    2048    4096   8192    16384       16384       16384
        4                                         512   1024    2048    4096   8192    16384       16384       16384
        5                                         512   1024    2048    4096   8192    16384       32768       32768
        6                                         512   1024    2048    4096   8192    16384       32768       32768
        7                                         512   1024    2048    4096   8192    16384       32768       32768
        8                                         512   1024    2048    4096   8192    16384       32768       32768
        9                                         512   1024    2048    4096   8192    16384       32768       65536
        10                                        512   1024    2048    4096   8192    16384       32768       65536

         • The italic cells indicate sub-optimal configurations, unnecessary blocks are allocated.
         • The bold cells indicate optimal valid configurations with the maximum number of SEEP depending
           on SEESTAT.PSZ and SEESTAT.SBLK (see the table below).
         • Other cells indicate valid configurations with the maximum number of SEEP depending on
           SEESTAT.PSZ and SEESTAT.SBLK.
        Table 25-7. Maximum Number of SEEP depending on SEESTAT.PSZ and SEESTAT.SBLK

        SEESTAT.PSZ: SEESTAT.SBLK                       4       8       16     32     64      128        256       512
        0                                               N/A     N/A     N/A    N/A    N/A     N/A        N/A       N/A
        1                                               144     144     144    144    95      47         23        11
        2                                               144     144     144    144    144     111        55        27
        3                                               144     144     144    144    144     144        87        43
        4                                               144     144     144    144    144     144        119       59
        5                                               144     144     144    144    144     144        144       75
        6                                               144     144     144    144    144     144        144       91
        7                                               144     144     144    144    144     144        144       107
        8                                               144     144     144    144    144     144        144       123
        9                                               144     144     144    144    144     144        144       139
        10                                              144     144     144    144    144     144        144       144

25.6.8.5 SmartEEPROM wear leveling
        The wear leveling factor is the minimum ratio per which the access frequency to a physical flash cell is
        divided when the maximum number of SEEP in a SEES is reached. This maximum number is depends




       © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 654
                                                       SAM D5x/E5x Family Data Sheet
                                                           NVMCTRL – Nonvolatile Memory Controller

        on the SEESTAT.PSZ and SEESTAT.SBLK user configuration. As there are two SEES the wear leveling is
        two times the maximum SEEP number.
        Table 25-8. Wear leveling depending on SEESTAT.PSZ and SEESTAT.SBLK

         SEESTAT 4                  8     16          32          64        128        256          512
         .PSZ:
         SEESTAT
         .SBLK
         0            N/A           N/A   N/A         N/A         N/A       N/A        N/A          N/A
         1            288           288   288         288         190       94         46           22
         2            288           288   288         288         288       222        110          54
         3            288           288   288         288         288       288        174          86
         4            288           288   288         288         288       288        238          118
         5            288           288   288         288         288       288        238          150
         6            288           288   288         288         288       288        238          182
         7            288           288   288         288         288       288        238          214
         8            288           288   288         288         288       288        238          246
         9            288           288   288         288         288       288        238          278
         10           288           288   288         288         288       288        238          288

25.6.8.6 Writing and Reading the SmartEEPROM
        SEESTAT.LOCK must be ‘0’; otherwise, writes are discarded and a hardfault exception is thrown.
        SmartEEPROM write access can be locked with the LSEE command and unlocked with the USEE
        command.
         1. Configure SBLK and PSZ fuses to define the SmartEEPROM total size and size of each page.
         2. Define a pointer to the SmartEEPROM area. It can be used for 8-, 16- or 32-bit access.
                volatile uint8_t *SmartEEPROM8 = (uint8_t *) SEEPROM_ADDR; volatile uint16_t
                *SmartEEPROM16 = (uint16_t *) SEEPROM_ADDR; volatile uint32_t *SmartEEPROM32 = (uint32_t
                *) SEEPROM_ADDR;

         3.   Wait until SmartEEPROM is busy.
                while (NVMCTRL->SEESTAT.bit.BUSY);

         4.   Write to the EEPROM like writing a RAM location. Perform an 8-, 16- or 32-bit write.
         5.   If automatic reallocation is disabled with SEECFG.APRDIS, check the SEESFULL interrupt flag to
              ensure that the active SmartEEPROM sector is not full.
         6.   To read back the content, read the location using the defined pointer.
                uint8_t eep_data_8 = 0; while (NVMCTRL->SEESTAT.bit.BUSY); eep_data_8 = SmartEEPROM8[0];

        There are two NVM pagebuffer management modes available, selected by writing the SEECFG.WMODE
        bit field:
          • UNBUFFERED (default): WP command triggered after any pagebuffer update




       © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 655
                                                          SAM D5x/E5x Family Data Sheet
                                                             NVMCTRL – Nonvolatile Memory Controller

         • BUFFERED: WP command triggered only in case of NVM page crossing. This mode increases the
           NVM wear-leveling but is more sensitive to power loss. SEESTAT.LOAD is high when the pagebuffer
           contains unwritten data.
        When SEECFG.WMODE selects the buffered mode, the page buffer can contain unwritten
        SmartEEPROM data. This is reflected by SEESTAT.LOAD. To flush the SmartEEPROM data inside the
        page buffer, issue the SEEFLUSH command.
        INTFLAG.SEEWRC indicates when a AHB write to the SmartEEPROM has completed:
         1.   Unbuffered mode: AHB write has completed, NVM is programmed with correct values except if
              INTFLAG.SEESOVF was thrown.
         2.   Buffered mode: AHB write has completed,
                – if SEESTAT.LOAD = 0: NVM is programmed with correct values, except if INTFLAG.SEESOVF
                  was thrown.
                – otherwise; new data is in the page buffer, but is not yet programmed in the NVM.
25.6.8.7 SmartEEPROM Sector Reallocation
        The SEES reallocation is performed by default in hardware when the the next available page in the
        master index reaches the maximum SEEP number. Automatic reallocation can be disabled by writing a
        one in SEECFG.APRDIS. The sector reallocation can also be trigged manually by issuing the
        SEERALOC command. The SEES reallocation process consists of:
         • Erase the non active sector.
         • Copying the active sector valid data to the other sector, old data is filtered.
         • Swap ASEES either by issuing the ASEES1 command if SEESTAT.ASEES is reading ‘0’ or by
           issuing the ASEES0 command if SEESTAT.ASEES is read as ‘1’.
        This process is by default automatically handled by hardware, and indicated by the SEESTAT.BUSY flag.
        If in buffered mode, the page buffer must be flushed before triggering a reallocation; otherwise, the
        content of the pagebuffer would be lost.
        Note: The BKSWRST command triggers automatically the reallocation algorithm which operates as
        described above except copy is done in the same active sector but in the first bank. This operation is
        atomic, meaning that no modify operation can be issued in the mean time.
        As the total size of the whole SEEP exceeds the SmartEEPROM virtual size for a given configuration
        there is always free SEEP to replace existing data. In the case all addresses have been written, after
        sector reallocation the number of free SEEP is given in the following table.
        Table 25-9. Minimum number of free SEEP after sector reallocation

         SEESTAT 4                  8       16          32          64          128         256          512
         .PSZ:
         SEESTAT
         .SBLK
         0            N/A           N/A     N/A         N/A         N/A         N/A         N/A          N/A
         1            16            16      16          16          31          15          7            3
         2            16            16      16          16          16          47          23           11
         3            16            16      16          16          16          16          23           11
         4            16            16      16          16          16          16          55           27




       © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 656
                                                           SAM D5x/E5x Family Data Sheet
                                                              NVMCTRL – Nonvolatile Memory Controller

         ...........continued
          SEESTAT 4                   8       16         32          64            128       256          512
          .PSZ:
          SEESTAT
          .SBLK
          5             16            16      16         16          16            16        16           11
          6             16            16      16         16          16            16        16           27
          7             16            16      16         16          16            16        16           43
          8             16            16      16         16          16            16        16           59
          9             16            16      16         16          16            16        16           11
          10            16            16      16         16          16            16        16           16

25.6.9   NVM User Configuration
         The NVM user configuration resides in the auxiliary space. Refer to the Physical Memory Map and
         Product Mapping of the device for calibration and auxiliary space address mapping.
         The NVM user configuration is:
           • The boot loader size. The bootloader resides in the main array starting at offset zero. The allocated
             boot loader section is protected against erase or write operations including the chip erase operation.
           • The SmartEEPROM number of blocks per SEES (SBLK bits). This configuration is loaded after a
             reset into SEESTAT.SBLK bits.
           • The SmartEEPROM virtual page size (PSZ bits). This configuration is loaded after a reset into
             SEESTAT.PSZ bits.
           • The region lock bits (reflected in the RUNLOCK register)
           • The SmartEEPROM RUNLOCK bit (reflected in SEESTAT.LOCK)
         Table 25-10. Boot Loader Size

          BOOTPROT [3:0]              Rows Protected by BOOTPROT              Boot Loader Size in KBytes
          15                          None                                    0
          14                          1                                       8
          13                          2                                       16
          12                          3                                       24
          11                          4                                       32
          10                          5                                       40
          9                           6                                       48
          8                           7                                       56
          7                           8                                       64
          6                           9                                       72
          5                           10                                      80




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 657
                                                    SAM D5x/E5x Family Data Sheet
                                                    NVMCTRL – Nonvolatile Memory Controller

...........continued
 BOOTPROT [3:0]              Rows Protected by BOOTPROT           Boot Loader Size in KBytes
 4                           11                                   88
 3                           12                                   96
 2                           13                                   104
 1                           14                                   112
 0                           15                                   120

Table 25-11. SmartEEPROM Allocated Space

 SBLK[4:0]                           Total Blocks                      Bytes
 10                                  20                                163840
 9                                   18                                147456
 8                                   16                                131072
 7                                   14                                114688
 6                                   12                                98304
 5                                   10                                81920
 4                                   8                                 65536
 3                                   6                                 49152
 2                                   4                                 32768
 1                                   2                                 16384
 0                                   0                                 0

Table 25-12. SmartEEPROM Virtual Page Size

 PSZ[2:0]                                             Page Size
 7                                                    512
 6                                                    256
 5                                                    128
 4                                                    64
 3                                                    32
 2                                                    16
 1                                                    8
 0                                                    4

Related Links
9.2 Physical Memory Map
8. Product Memory Mapping Overview




© 2019 Microchip Technology Inc.                    Datasheet                    DS60001507E-page 658
                                                            SAM D5x/E5x Family Data Sheet
                                                              NVMCTRL – Nonvolatile Memory Controller

25.6.10 Security Bit
        The security bit allows the entire chip to be locked from external access for code security.
         Related Links
         12. DSU - Device Service Unit

25.6.10.1 Security Bit Set Procedure
           1.   Issue the Set Security Bit command (SSB)
                This command changes the NVM security bits. The device shadow registers are not changed at
                that point. If a debugger was connected, it will still have access to the device after issuing this
                command (DSU.STATUSB.PROT will still read ‘0’).
           2.   Check NVMNCTRL.INTFLAG.PROGE and NVMNCTRL.INTFLAG.DONE.
           3.   Reset the NVMCTRL peripheral or the device.
         To reflect the NVM security bits’ state correctly, the NVMCTRL needs to replay the start-up procedure.
         This is done by issuing a SWRST command or by resetting the device.
         Related Links
         12. DSU - Device Service Unit

25.6.10.2 Security Bit Clear Procedure
         The only way to clear the security bit is through a debugger Chip Erase command. The NVM security bit
         is cleared after all internal volatile and NVM have been cleared. The device protection status is updated
         at the end of the command meaning that no reset is necessary.
         Related Links
         12. DSU - Device Service Unit

25.6.11 Line Cache
        NVM reads 128-bit at a time. AHB0 and AHB1 interfaces implement each a 128-bit cache line.This
        reduces the device power consumption when reading continuous data and improves system performance
        when wait states are required. Line cache are enabled by default and can be individually disabled per
        AHB interface by writing a one in the CACHEDIS[0] or CACHEDIS[1] bit in the CTRLA register
        (CTRLA.CACHEDIS[1:0]). Refer to CTRLA register description for more details. Commands affecting
        NVM content automatically invalidate cache lines.


25.6.12 Error Correction Code (ECC)
        Error Correcting Code (ECC) is implemented to detect and correct errors that may arise in the NVM array.
        ECC is by default enabled and cannot be disabled by the user.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 659
                                                                      SAM D5x/E5x Family Data Sheet
                                                                           NVMCTRL – Nonvolatile Memory Controller

25.6.12.1 Block Diagram
         Figure 25-2. ECC Diagram
                                 PBLDATA[63:0]


                                                   ECC
                                                calculation
                                    64               8



                            HADDR

                       ECCERR.ADDR                                    NVM Block



                                                                      144


                                           64               8                          64               8


                                                ECC logic                                   ECC logic
                                                                INTFLAG.ECCERR                              INTFLAG.ECCERR
                                                                ECCERR.TYPEH                                ECCERR.TYPEL

                                                64                                          64


                                                                      MATRIX

                                                128                  128

                                      CACHE LINE AHB0           CACHE LINE AHB1         SmartEEPROM

                                                32                    32

         Note that the ECC correction is disabled when access is performed by the SmartEEPROM interface.
25.6.12.2 ECC Error Detection
         The NVM physical block fetches 128-bit quad-word and ECC checking is performed on a 64-bit basis
         independently on the low and high double-words. Therefore two ECC decoders operate in parallel. An
         ECC failure may be present in any of the four words from the NVM, not necessarily the word that is
         addressed on the bus. Any ECC error in a double-word will be reported the first time the quad-word
         access. The ECC logic in the read data path is capable of double error detection and single error
         correction on the fly per 64-bit double-word.
         Upon detection:
          • INTFLAG ECC error flags are updated:
              – The ECC single error interrupt flag is raised (INTFLAG.ECCSE) in case of single error
              – The ECC dual error interrupt flag is raised (INTFLAG.ECCDE) in case of dual error
          • ECCERR.ADDR is updated with the faulty quad-word byte address in the main address space.
          • ECCERR.TYPEL is updated with the error type (NONE, SINGLE, DUAL) detected on the low 64-bit
            double word.
          • ECCERR.TYPEH is updated with the error type (NONE, SINGLE, DUAL) detected on the high 64-bit
            double word.
         INTFLAG.ECCSE and INTFLAG.ECCDE are automatically cleared when ECCERR is read.




        © 2019 Microchip Technology Inc.                                   Datasheet                            DS60001507E-page 660
                                                          SAM D5x/E5x Family Data Sheet
                                                           NVMCTRL – Nonvolatile Memory Controller

         ECCERR.TYPEL and ECCERR.TYPEH are reset to the NONE value when ECCERR is read. If an error
         occurs while reading ECCERR, the previous error information is sent to the APB and ECCERR is
         updated with the next error information.
         If a single-error has been detected and INTFLAG.ECCSE or INTFLAG.ECCDE is not clear:
           • Any incoming single-errors is ignored
           • First incoming dual-error overrides ECCERR.ADDR, ECCERR.TYPEL and ECCERR.TYPEH
         If a dual-error has been detected and INTFLAG.ECCDE is not clear:
           • incoming single-errors are ignored
           • incoming dual-errors are ignored
         ECCERR.ADDR is always quad-word aligned. If jumping to a word that is not quad-word aligned, e.g.
         jumping to address 0x100C, INTFLAG.ECCDE and INTFLAG.ECCSE are updated according to the types
         of detected errors, and ECCERR.ADDR will read 0x1000, irrespective of whether the ECC error was in
         address 0x1000, 0x1004, 0x1008, or 0x100C.

25.6.13 Reset During Operation
        Program or erase operations must not be interrupted. The content of a block or a page is unpredictable in
        case of reset during either an erase or a write operation. To reduce the risk of having a BOD reset due to
        a power loss one can monitor the external voltage before issuing any program or erase operation. The
        user can also prefer the WQW command instead of the WP command as a short command is more likely
        to complete successfully than a long one with a given external decoupling capacitor. In case of reset
        during a write or erase operation the impacted block must be erased before being read or programmed
        as its content is unknown.

25.6.14 Chip Erase
        The Chip Erase operation is system-wide, and issued through the DSU.
         Chip-Erase procedure:
           1.   Volatile memories are cleared and NVM array is erased simultaneously (except the BOOTPROT
                section)
           2.   Special individual fuses are set as follow:
                 – If no BOOTPROT section is defined then NVMCTRL STATUS.AFIRST=1 otherwise it is left
                     unchanged
                 – NVMCTRL SEESTAT.ASEES=1
                 – NVMCTRL SEESTAT.LOCK=0
                 – DSU STATUSB.CELCK=0
           3.   Security bit is cleared provided no internal error has been detected in the previous steps
                 – If all internal NVM verify operations succeeded: goto 4
                 – otherwise set DSU.STATUSA.DONE and DSU.STATUSA.FAIL and exit.
           4.   DSU STATUSB.PROT is cleared, system is no more protected
         Note: CB, FS, USER pages (in the auxiliary address space) and the section allocated as a boot loader
         using BOOTPROT are not affected by the Chip-Erase operation.




        © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 661
                                                                SAM D5x/E5x Family Data Sheet
                                                                    NVMCTRL – Nonvolatile Memory Controller


25.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0             PRM[1:0]         WMODE[1:0]              SUSPEN    AUTOWS
 0x00         CTRLA
                             15:8     CACHEDIS1 CACHEDIS0   AHBNS1     AHBNS0                        RWS[3:0]
 0x02
   ...       Reserved
 0x03
                              7:0                                                     CMD[6:0]
 0x04         CTRLB
                             15:8                                              CMDEX[7:0]
 0x06
   ...       Reserved
 0x07
                              7:0                                              NVMP[7:0]
                             15:8                                              NVMP[15:8]
 0x08         PARAM
                             23:16                                                                         PSZ[2:0]
                             31:24      SEE
                              7:0       SUSP         NVME   ECCDE       ECCSE          LOCKE     PROGE      ADDRE      DONE
 0x0C        INTENCLR
                             15:8                                                                SEEWRC    SEESOVF    SEESFULL
                              7:0       SUSP         NVME   ECCDE       ECCSE          LOCKE     PROGE      ADDRE      DONE
 0x0E        INTENSET
                             15:8                                                                SEEWRC    SEESOVF    SEESFULL
                              7:0       SUSP         NVME   ECCDE       ECCSE          LOCKE     PROGE      ADDRE      DONE
 0x10        INTFLAG
                             15:8                                                                SEEWRC    SEESOVF    SEESFULL
                              7:0                           BPDIS      AFIRST           SUSP      LOAD          PRM    READY
 0x12         STATUS
                             15:8                                                                  BOOTPROT[3:0]
                              7:0                                              ADDR[7:0]
                             15:8                                              ADDR[15:8]
 0x14          ADDR
                             23:16                                            ADDR[23:16]
                             31:24
                              7:0                                            RUNLOCK[7:0]
                             15:8                                            RUNLOCK[15:8]
 0x18        RUNLOCK
                             23:16                                           RUNLOCK[23:16]
                             31:24                                           RUNLOCK[31:24]
                              7:0                                               DATA[7:0]
                             15:8                                              DATA[15:8]
 0x1C       PBLDATAn0
                             23:16                                             DATA[23:16]
                             31:24                                             DATA[31:24]
                              7:0                                               DATA[7:0]
                             15:8                                              DATA[15:8]
 0x20       PBLDATAn1
                             23:16                                             DATA[23:16]
                             31:24                                             DATA[31:24]
                              7:0                                              ADDR[7:0]
                             15:8                                              ADDR[15:8]
 0x24        ECCERR
                             23:16                                            ADDR[23:16]
                             31:24           TYPEH[1:0]         TYPEL[1:0]
 0x28        DBGCTRL          7:0                                                                         ECCELOG      ECCDIS




          © 2019 Microchip Technology Inc.                          Datasheet                             DS60001507E-page 662
                                                                  SAM D5x/E5x Family Data Sheet
                                                                    NVMCTRL – Nonvolatile Memory Controller

...........continued

  Offset                Name    Bit Pos.

   0x29            Reserved
   0x2A                SEECFG     7:0                                                                      APRDIS     WMODE
   0x2B            Reserved
                                  7:0                                    RLOCK       LOCK       BUSY        LOAD      ASEES
                                 15:8                                                               SBLK[3:0]
   0x2C            SEESTAT
                                 23:16                                                                     PSZ[2:0]
                                 31:24




25.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 663
                                                                       SAM D5x/E5x Family Data Sheet
                                                                       NVMCTRL – Nonvolatile Memory Controller

25.8.1         Control A

               Name:        CTRLA
               Offset:      0x0
               Reset:       0x0004
               Property:    PAC Write-Protection


         Bit        15              14          13                12         11        10                9           8
                CACHEDIS1     CACHEDIS0       AHBNS1        AHBNS0                           RWS[3:0]
   Access          R/W              R/W        R/W            R/W           R/W        R/W              R/W         R/W
    Reset            0               0          0                 0          0          0                0           0


         Bit         7               6          5                 4          3          2                1           0
                         PRM[1:0]                    WMODE[1:0]           SUSPEN    AUTOWS
   Access          R/W              R/W        R/W            R/W           R/W        R/W
    Reset            0               0          0                 0          0          1


               Bit 15 – CACHEDIS1 AHB1 Cache Disable
               AHB1 interface cache disable.
               0: cache line is enabled
               1: cache line is disabled
               Cache lines are automatically invalidated when a write or erase operation is started in the NVM.

               Bit 14 – CACHEDIS0 AHB0 Cache Disable
               AHB0 interface cache disable.
               0: cache line is enabled
               1: cache line is disabled
               Cache lines are automatically invalidated when a write or erase operation is started in the NVM.

               Bit 13 – AHBNS1 Force AHB1 access to Non-Sequential
               This bit forces AHB1 communication to be non-sequential.
                Value       Description
                0           AHB sequential accesses remain sequential.
                1           AHB sequential accesses are forced to non-sequential, therefore forcing rearbitration for
                            each access.

               Bit 12 – AHBNS0 Force AHB0 access to Non-Sequential
               This bit forces AHB0 communication to be non-sequential.
                Value       Description
                0           AHB sequential accesses remain sequential.
                1           AHB sequential accesses are forced to non-sequential, therefore forcing rearbitration for
                            each access.

               Bits 11:8 – RWS[3:0] NVM Read Wait States
               These bits give the number of wait states for a read operation when AUTOWS=0. Zero indicates zero
               wait states, one indicates one wait state, etc., up to 15 wait states.
               This register is initialized to 0 wait states. Software can change this value based on the NVM access time
               and system frequency.




           © 2019 Microchip Technology Inc.                            Datasheet                         DS60001507E-page 664
                                                 SAM D5x/E5x Family Data Sheet
                                                  NVMCTRL – Nonvolatile Memory Controller

Bits 7:6 – PRM[1:0] Power Reduction Mode during Sleep
Indicates the power reduction mode during sleep.
 Value      Name        Description
 0x0        SEMIAUTO NVM block enters low-power mode when entering standby mode. NVM block
                        enters low-power mode when SPRM command is issued. NVM block exits low-
                        power mode upon first access.
 0x1        FULLAUTO NVM block enters low-power mode when entering standby mode. NVM block
                        enters low-power mode when SPRM command is issued. NVM block exits low-
                        power mode when system is not in standby mode.
 0x2                    Reserved
 0x3        MANUAL      NVM block does not enter low-power mode when entering standby mode. NVM
                        block enters low-power mode when SPRM command is issued. NVM block
                        exits low-power mode upon first access.

Bits 5:4 – WMODE[1:0] Write Mode
Write commands can be generated automatically when crossing address boundaries while writing to the
NVM. Boundaries depend on the settings below.
Value       Name           Description
0x0         MAN            Manual Write
0x1         ADW            Automatic Double Word Write
0x2         AQW            Automatic Quad Word
0x3         AP             Automatic Page Write

Bit 3 – SUSPEN Suspend Enable
0: The write and erase suspend resume feature is disabled.
1: A write or erase operation can be suspended in case of a read in the same bank.

Bit 2 – AUTOWS Auto Wait State Enable
0: Automatic wait state generation is disabled. The number of wait states used is given by RWS.
1: Automatic wait state generation is enabled. The number of wait states used is automatically detected
therefore the module can operate at any frequency up to the device maximum frequency. A minimum of
one cycle latency is induced.




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 665
                                                                    SAM D5x/E5x Family Data Sheet
                                                                        NVMCTRL – Nonvolatile Memory Controller

25.8.2         Control B

               Name:          CTRLB
               Offset:        0x04
               Reset:         0x0000
               Property:      PAC Write-Protection


         Bit        15             14            13           12                11         10            9            8
                                                                   CMDEX[7:0]
   Access        PAC Write-     PAC Write-    PAC Write-   PAC Write-      PAC Write-   PAC Write-   PAC Write-   PAC Write-
                 Protection     Protection    Protection   Protection      Protection   Protection   Protection   Protection
    Reset            0              0             0            0                0           0            0            0


         Bit         7              6             5            4                3           2            1            0
                                                                           CMD[6:0]
   Access                           W             W            W                W           W            W            W
    Reset                           0             0            0                0           0            0            0


               Bits 15:8 – CMDEX[7:0] Command Execution
               This bit group should be written with the key value 0xA5 to enable the command written to CMD to be
               executed. If the bit group is written with a different key value, the write is not performed and
               INTFLAG.PROGE is set. PROGE is also set if the a previously written command is not complete.
               The key value must be written at the same time as CMD. If a command is issued through the APB bus on
               the same cycle as an AHB bus access, the AHB bus access will be given priority. The command will then
               be executed when the NVM block and the AHB bus are idle.
               STATUS.READY must be one when the command is issued.
               INTFLAG.DONE is set when the command completes.
                Value       Name                             Description
                0xA5        KEY                              Execution Key
                Other       -                                Reserved

               Bits 6:0 – CMD[6:0] Command
               These bits define the command to be executed when the CMDEX key is written.
                Value      Name         Description
                0x0        EP           Erase Page - Only supported in the User page in the auxiliary space.
                0x1        EB           Erase Block - Erases the block addressed by the ADDR register, not supported
                                        in the user page
                0x2                     Reserved
                0x3        WP           Write Page - Writes the contents of the page buffer to the page addressed by
                                        the ADDR register, not supported in the user page
                0x4        WQW          Write Quad Word - Writes a 128-bit word at the location addressed by the
                                        ADDR register.
                0x5-0xF                 Reserved
                0x10       SWRST        Software Reset - Power-Cycle the NVM memory and replay the device
                                        automatic calibration procedure and resets the module configuration registers
                0x11       LR           Lock Region - Locks the region containing the address location in the ADDR
                                        register until next reset.




           © 2019 Microchip Technology Inc.                             Datasheet                        DS60001507E-page 666
                                                    SAM D5x/E5x Family Data Sheet
                                                     NVMCTRL – Nonvolatile Memory Controller

 Value        Name            Description
 0x12         UR              Unlock Region - Unlocks the region containing the address location in the
                              ADDR register until next reset.
 0x13         SPRM            Sets the power reduction mode.
 0x14         CPRM            Clears the power reduction mode.
 0x15         PBC             Page Buffer Clear - Clears the page buffer.
 0x16         SSB             Set Security Bit
 0x17         BKSWRST         Bank swap and system reset, if SmartEEPROM is used also reallocate its data
                              into the opposite BANK
 0x18         CELCK           Chip Erase Lock - DSU.CTRL.CE command is not available
 0x19         CEULCK          Chip Erase Unlock - DSU.CTRL.CE command is available
 0x1A         SBPDIS          Sets STATUS.BPDIS, Boot loader protection is discarded until CBPDIS is
                              issued or next start-up sequence
 0x1B         CBPDIS          Clears STATUS.BPDIS, Boot loader protection is not discarded
 0x1C-0x                      Reserved
 2F
 0x30         ASEES0   Configure SmartEEPROM to use Sector 0
 0x31         ASEES1   Configure SmartEEPROM to use Sector 1
 0x32         SEERALOC Starts SmartEEPROM sector reallocation algorithm
 0x33         SEEFLUSH Flush SmartEEPROM data when in buffered mode
 0x34         LSEE     Lock access to SmartEEPROM data from any means
 0x35         USEE     Unlock access to SmartEEPROM data
 0x36         LSEER    Lock access to the SmartEEPROM Register Address Space (above 64KB)
 0x37         USEER    Unock access to the SmartEEPROM Register Address Space (above 64KB)
 0x38-0x               Reserved
 7F




© 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 667
                                                                    SAM D5x/E5x Family Data Sheet
                                                                     NVMCTRL – Nonvolatile Memory Controller

25.8.3         NVM Parameter

               Name:        PARAM
               Offset:      0x08
               Property:    -


         Bit        31            30            29            28                27        26            25            24
                    SEE
   Access            R
    Reset


         Bit        23            22            21            20                19        18            17            16
                                                                                                      PSZ[2:0]
   Access                                                                                  R             R                R
    Reset


         Bit        15            14            13            12                11        10             9                8
                                                                   NVMP[15:8]
   Access            R             R             R             R                R          R             R                R
    Reset


         Bit         7             6             5             4                3          2             1                0
                                                                   NVMP[7:0]
   Access            R             R             R             R                R          R             R                R
    Reset


               Bit 31 – SEE SmartEEPROM Supported
               0: No SmartEEPROM support
               1: SmartEEPROM is supported.

               Bits 18:16 – PSZ[2:0] Page Size
               Indicates the page size. Not all device families will provide all the page sizes indicated in the table.
                Value      Name                               Description
                0x0        8                                  8 bytes
                0x1        16                                 16 bytes
                0x2        32                                 32 bytes
                0x3        64                                 64 bytes
                0x4        128                                128 bytes
                0x5        256                                256 bytes
                0x6        512                                512 bytes
                0x7        1024                               1024 bytes

               Bits 15:0 – NVMP[15:0] NVM Pages
               Indicates the number of pages in the NVM main address space




           © 2019 Microchip Technology Inc.                           Datasheet                          DS60001507E-page 668
                                                                   SAM D5x/E5x Family Data Sheet
                                                                   NVMCTRL – Nonvolatile Memory Controller

25.8.4         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x0C
               Reset:       0x0000
               Property:    PAC Write-Protection


         Bit        15            14            13           12            11             10        9           8
                                                                                        SEEWRC   SEESOVF    SEESFULL
   Access                                                                                R/W       R/W         R/W
    Reset                                                                                  0        0           0


         Bit         7            6             5             4            3               2        1           0
                   SUSP         NVME          ECCDE        ECCSE         LOCKE          PROGE    ADDRE        DONE
   Access           R/W          R/W           R/W          R/W           R/W            R/W       R/W         R/W
    Reset            0            0             0             0            0               0        0           0


               Bit 10 – SEEWRC SEE Write Completed Interrupt Clear
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the SEEWRC interrupt enable.
               This bit will read as the current value of the SEEWRC interrupt enable.

               Bit 9 – SEESOVF Active SEES Overflow Interrupt Clear
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the SEESOVF interrupt enable.
               This bit will read as the current value of the SEESOVF interrupt enable.

               Bit 8 – SEESFULL Active SEES Full Interrupt Clear
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the SEESFULL interrupt enable.
               This bit will read as the current value of the SEESFULL interrupt enable.

               Bit 7 – SUSP Suspended Write Or Erase Interrupt Clear
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the SUSP interrupt enable.
               This bit will read as the current value of the SUSP interrupt enable.

               Bit 6 – NVME NVM Error Interrupt Clear
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the NVME interrupt enable.
               This bit will read as the current value of the NVME interrupt enable.

               Bit 5 – ECCDE ECC Dual Error Interrupt Clear
               Writing a zero to this bit has no effect.
               Writing a '1' to this bit clears the ECCDE interrupt enable.
               This bit will read as the current value of the ECCDE interrupt enable.

               Bit 4 – ECCSE ECC Single Error Interrupt Clear
               Writing a zero to this bit has no effect.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 669
                                                  SAM D5x/E5x Family Data Sheet
                                                    NVMCTRL – Nonvolatile Memory Controller

Writing a '1' to this bit clears the ECCSE interrupt enable.
This bit will read as the current value of the ECCSE interrupt enable.

Bit 3 – LOCKE Lock Error Interrupt Clear
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the LOCKE interrupt enable.
This bit will read as the current value of the LOCKE interrupt enable.

Bit 2 – PROGE Programming Error Interrupt Clear
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the PROGE interrupt enable.
This bit will read as the current value of the PROGE interrupt enable.

Bit 1 – ADDRE Address Error Interrupt Clear
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the ADDRE interrupt enable.
This bit will read as the current value of the ADDRE interrupt enable.

Bit 0 – DONE Command Done Interrupt Clear
Writing a zero to this bit has no effect.
Writing a '1' to this bit clears the DONE interrupt enable.
This bit will read as the current value of the DONE interrupt enable.




© 2019 Microchip Technology Inc.                    Datasheet               DS60001507E-page 670
                                                                   SAM D5x/E5x Family Data Sheet
                                                                   NVMCTRL – Nonvolatile Memory Controller

25.8.5         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x0E
               Reset:       0x0000
               Property:    PAC Write-Protection


         Bit        15            14            13           12            11             10        9           8
                                                                                        SEEWRC   SEESOVF    SEESFULL
   Access                                                                                R/W       R/W         R/W
    Reset                                                                                  0        0           0


         Bit         7            6             5             4            3               2        1           0
                   SUSP         NVME          ECCDE        ECCSE         LOCKE          PROGE    ADDRE        DONE
   Access           R/W          R/W           R/W          R/W           R/W            R/W       R/W         R/W
    Reset            0            0             0             0            0               0        0           0


               Bit 10 – SEEWRC SEE Write Completed Interrupt Enable
               Writing a zero to this bit has no effect.
               Writing a one to this bit sets the SEEWRC interrupt enable.
               This bit will read as the current value of the SEEWRC interrupt enable.

               Bit 9 – SEESOVF Active SEES Overflow Interrupt Enable
               Writing a zero to this bit has no effect.
               Writing a one to this bit sets the SEESOVF interrupt enable.
               This bit will read as the current value of the SEESOVF interrupt enable.

               Bit 8 – SEESFULL Active SEES Full Interrupt Enable
               Writing a zero to this bit has no effect.
               Writing a one to this bit sets the SEESFULL interrupt enable.
               This bit will read as the current value of the SEESFULL interrupt enable.

               Bit 7 – SUSP Suspended Write Or Erase Interrupt Enable
               Writing a zero to this bit has no effect.
               Writing a one to this bit sets the SUSP interrupt enable.
               This bit will read as the current value of the SUSP interrupt enable.

               Bit 6 – NVME NVM Error Interrupt Enable
               Writing a zero to this bit has no effect.
               Writing a one to this bit sets the NVME interrupt enable.
               This bit will read as the current value of the NVME interrupt enable.

               Bit 5 – ECCDE ECC Dual Error Interrupt Enable
               Writing a zero to this bit has no effect.
               Writing a one to this bit sets the ECCDE interrupt enable.
               This bit will read as the current value of the ECCDE interrupt enable.

               Bit 4 – ECCSE ECC Single Error Interrupt Enable
               Writing a zero to this bit has no effect.




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 671
                                                  SAM D5x/E5x Family Data Sheet
                                                    NVMCTRL – Nonvolatile Memory Controller

Writing a one to this bit sets the ECCSE interrupt enable.
This bit will read as the current value of the ECCSE interrupt enable.

Bit 3 – LOCKE Lock Error Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit sets the LOCKE interrupt enable.
This bit will read as the current value of the LOCKE interrupt enable.

Bit 2 – PROGE Programming Error Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit sets the PROGE interrupt enable.
This bit will read as the current value of the PROGE interrupt enable.

Bit 1 – ADDRE Address Error Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit sets the ADDRE interrupt enable.
This bit will read as the current value of the ADDRE interrupt enable.

Bit 0 – DONE Command Done Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit sets the DONE interrupt enable.
This bit will read as the current value of the DONE interrupt enable.




© 2019 Microchip Technology Inc.                    Datasheet               DS60001507E-page 672
                                                                     SAM D5x/E5x Family Data Sheet
                                                                     NVMCTRL – Nonvolatile Memory Controller

25.8.6         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x10
               Reset:       0x0000
               Property:    -


         Bit        15             14            13            12            11            10             9             8
                                                                                        SEEWRC        SEESOVF       SEESFULL
   Access                                                                                 R/W            R/W           R/W
    Reset                                                                                   0             0             0


         Bit         7             6             5             4              3             2             1             0
                   SUSP          NVME         ECCDE          ECCSE         LOCKE         PROGE         ADDRE          DONE
   Access           R/W           R/W            R             R            R/W           R/W            R/W           R/W
    Reset            0             0             0             0              0             0             0             0


               Bit 10 – SEEWRC SEE Write Completed
                • Unbuffered mode:
                    0: AHB write is pending.
                  1: AHB write has completed, and NVM is programmed with correct values.
                • Buffered mode:
                  0: AHB write is pending.
                   1: AHB write has completed.
                   If SEESTAT.LOAD=0, then the NVM is programmed with correct values.
                   If SEESTAT.LOAD=1, then data is still pending in the Page Buffer.

               Bit 9 – SEESOVF Active SEES Overflow
               0: No SEES overflow have been detected since the last clear.
               1: At least SEES overflow has been detected since the last clear.
               This bit can be cleared by writing a one to its bit location.

               Bit 8 – SEESFULL Active SEES Full
               0: The active SEES is not full
               1: The active SEES is Full, meaning that the next write will fail if the active sector is not reallocated.
               This bit can be cleared by writing a one to its bit location.

               Bit 7 – SUSP Suspended Write Or Erase Operation
               0: No write/suspend has occurred since the last clear.
               1: A write or erase operation has been suspended since the last clear.
               This bit can be cleared by writing a one to its bit location.

               Bit 6 – NVME NVM Error
               0: No NVM errors have been received since the last clear.
               1: At least one NVM error has occurred since the last clear.
               This bit can be cleared by writing a one to its bit location.




           © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 673
                                                  SAM D5x/E5x Family Data Sheet
                                                   NVMCTRL – Nonvolatile Memory Controller

Bit 5 – ECCDE ECC Dual Error
0: No ECC dual errors have been received since the last ECCERR register read.
1: At least one ECC error has occurred since the last ECCERR register read.
This bit is cleared when the ECCERR register is read.

Bit 4 – ECCSE ECC Single Error
0: No ECC single errors have been received since the last ECCERR register read.
1: At least one ECC error has occurred since the last ECCERR register read.
This bit is cleared when the ECCERR register is read.

Bit 3 – LOCKE Lock Error
0: No LOCK errors have been received since the last clear.
1: At least one LOCK error has occurred since the last clear.
This bit can be cleared by writing a one to its bit location.

Bit 2 – PROGE Programming Error
0: No PROG errors have been received since the last clear.
1: At least one PROG error has occurred since the last clear.
This bit can be cleared by writing a one to its bit location.

Bit 1 – ADDRE Address Error
0: No ADDRE error has been detected since the last clear.
1: At least one ADDRE error has been detected since the last clear.
This bit can be cleared by writing a one to its bit location.

Bit 0 – DONE Command Done
0: The NVM controller has not completed any command since the last clear.
1: At least one command has completed since the last clear.
This bit can be cleared by writing a one to its bit location.




© 2019 Microchip Technology Inc.                   Datasheet                      DS60001507E-page 674
                                                                 SAM D5x/E5x Family Data Sheet
                                                                   NVMCTRL – Nonvolatile Memory Controller

25.8.7         Status

               Name:       STATUS
               Offset:     0x12
               Reset:      0x0000
               Property:   Read-Only


         Bit        15            14           13           12            11           10            9            8
                                                                                        BOOTPROT[3:0]
   Access                                                                 R            R             R            R
    Reset                                                                 0             0            0            x


         Bit         7            6             5            4            3             2            1            0
                                              BPDIS       AFIRST        SUSP          LOAD         PRM          READY
   Access                                      R             R            R            R             R            R
    Reset                                       0            0            0             0            0            0


               Bits 11:8 – BOOTPROT[3:0] Boot Loader Protection Size
               This bitfield is loaded from the USER page during the device startup.
               Defines the size of the BOOTPROT region which is protected against write or erase or Chip-Erase
               operations. This size is given by the following formula (15-BOOTPROT)*8KB.

               Bit 5 – BPDIS Boot Loader Protection Disable
               0: Boot loader protection is not discarded.
               1: Boot loader protection against modify operations is discarded until CBPDIS is issued or next start-up
               sequence except for Chip-Erase.

               Bit 4 – AFIRST BANKA First
               0: Start address of bank B is mapped at 0x0000_0000.
               1: Start address of bank A is mapped at 0x0000_0000.

               Bit 3 – SUSP NVM Write Or Erase Operation Is Suspended
               0: The NVM controller is not in suspended state.
               1: The NVM controller is in suspended state.

               Bit 2 – LOAD NVM Page Buffer Active Loading
               This bit indicates that the NVM page buffer has been loaded with one or more words. Immediately after
               an NVM load has been performed, this flag is set, and it remains set until a Write Page (WP), Write Quad
               Word (WQW) or a page buffer clear (PBCLR) command is given.

               Bit 1 – PRM Power Reduction Mode
               This bit indicates the current NVM power reduction state. The NVM block can be set in power reduction
               mode in two ways: through the command interface or automatically when entering sleep with
               CTRLA.PRM set accordingly. PRM can be cleared in three ways: through AHB access to the NVM block,
               through the command interface (SPRM and CPRM) or when exiting sleep with CTRLA.PRM set
               accordingly.
               0: NVM is not in power reduction mode
               1: NVM is in power reduction mode.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 675
                                              SAM D5x/E5x Family Data Sheet
                                               NVMCTRL – Nonvolatile Memory Controller

Bit 0 – READY Ready to accept a command
0: The NVM controller is busy programming or erasing.
1: The NVM controller is ready to accept a new command.




© 2019 Microchip Technology Inc.                Datasheet              DS60001507E-page 676
                                                                  SAM D5x/E5x Family Data Sheet
                                                                   NVMCTRL – Nonvolatile Memory Controller

25.8.8         Address

               Name:       ADDR
               Offset:     0x14
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31           30           29           28                 27      26           25           24


   Access
    Reset


         Bit        23           22           21           20                 19      18           17           16
                                                                ADDR[23:16]
   Access          R/W          R/W           R/W          R/W                R/W    R/W          R/W          R/W
    Reset            0            0            0            0                  0      0            0            0


         Bit        15           14           13           12                 11      10           9            8
                                                                 ADDR[15:8]
   Access          R/W          R/W           R/W          R/W                R/W    R/W          R/W          R/W
    Reset            0            0            0            0                  0      0            0            0


         Bit         7            6            5            4                  3      2            1            0
                                                                 ADDR[7:0]
   Access          R/W          R/W           R/W          R/W                R/W    R/W          R/W          R/W
    Reset            0            0            0            0                  0      0            0            0


               Bits 23:0 – ADDR[23:0] NVM Address
               ADDR drives the hardware address to the NVM when a command is executed using CMDEX. It is a Byte
               address. This register is also automatically updated when writing to the page buffer or when writing the
               SmartEEPROM.




           © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 677
                                                                  SAM D5x/E5x Family Data Sheet
                                                                  NVMCTRL – Nonvolatile Memory Controller

25.8.9         Lock Section

               Name:       RUNLOCK
               Offset:     0x18
               Reset:      0xXXXXXXXX
               Property:   -


         Bit        31            30           29            28           27         26   25          24
                                                             RUNLOCK[31:24]
   Access            R            R             R            R             R         R    R           R
    Reset            x            x             x            x             x         x    x           x


         Bit        23            22           21            20           19         18   17          16
                                                             RUNLOCK[23:16]
   Access            R            R             R            R             R         R    R           R
    Reset            x            x             x            x             x         x    x           x


         Bit        15            14           13            12           11         10   9           8
                                                              RUNLOCK[15:8]
   Access            R            R             R            R             R         R    R           R
    Reset            x            x             x            x             x         x    x           x


         Bit         7            6             5            4             3         2    1           0
                                                              RUNLOCK[7:0]
   Access            R            R             R            R             R         R    R           R
    Reset            x            x             x            x             x         x    x           x


               Bits 31:0 – RUNLOCK[31:0] Region Un-Lock Bits
               In order to set or clear these bits, the CMD register must be used.
               0: The corresponding region is locked.
               1: The corresponding region is not locked.




           © 2019 Microchip Technology Inc.                        Datasheet              DS60001507E-page 678
                                                            SAM D5x/E5x Family Data Sheet
                                                              NVMCTRL – Nonvolatile Memory Controller

25.8.10 Page Buffer Load Data x

            Name:       PBLDATAn
            Offset:     0x1C + n*0x04 [n=0..1]
            Reset:      0xFFFFFFFF
            Property:   -


      Bit        31           30           29         28                 27   26     25           24
                                                           DATA[31:24]
  Access         R             R           R          R                  R    R       R           R
   Reset         0             0           0          0                  0    0       0           0


      Bit        23           22           21         20                 19   18     17           16
                                                           DATA[23:16]
  Access         R             R           R          R                  R    R       R           R
   Reset         0             0           0          0                  0    0       0           0


      Bit        15           14           13         12                 11   10      9           8
                                                           DATA[15:8]
  Access         R             R           R          R                  R    R       R           R
   Reset         0             0           0          0                  0    0       0           0


      Bit        7             6           5          4                  3    2       1           0
                                                            DATA[7:0]
  Access         R             R           R          R                  R    R       R           R
   Reset         0             0           0          0                  0    0       0           1


            Bits 31:0 – DATA[31:0] Page Buffer Data




        © 2019 Microchip Technology Inc.                      Datasheet               DS60001507E-page 679
                                                                     SAM D5x/E5x Family Data Sheet
                                                                       NVMCTRL – Nonvolatile Memory Controller

25.8.11 ECC Error Status

           Name:          ECCERR
           Offset:        0x24
           Reset:         0x00000000
           Property:      -

           This register tracks errors on the NVM read path.
           ECC error tracking is active until an error is detected. It is still active in case of single error but no dual
           error. In this case only a dual error can override this register status as a dual error is more critical than a
           single error. Error tracking resumes as soon as this register is read.

     Bit         31                30        29                28                 27   26            25             24
                      TYPEH[1:0]                  TYPEL[1:0]
  Access         R                 R         R                 R
   Reset         0                 0         0                 0


     Bit         23                22        21                20                 19   18            17             16
                                                                    ADDR[23:16]
  Access         R                 R         R                 R                  R     R             R             R
   Reset         0                 0         0                 0                  0     0             0             0


     Bit         15                14        13                12                 11   10             9             8
                                                                    ADDR[15:8]
  Access         R                 R         R                 R                  R     R             R             R
   Reset         0                 0         0                 0                  0     0             0             0


     Bit         7                 6         5                 4                  3     2             1             0
                                                                     ADDR[7:0]
  Access         R                 R         R                 R                  R     R             R             R
   Reset         0                 0         0                 0                  0     0             0             0


           Bits 31:30 – TYPEH[1:0] High Double-Word Error Type
           Indicates the type of error detected on the NVM 64-bit most significant read word. It is reset to None
           when this register is read except if an error occurs in the same cycle.
            Value      Name         Description
            0x0        None         No Error Detected Since Last Read
            0x1        Single       At Least One Single Error Detected Since last Read
            0x2        Dual         At Least One Dual Error Detected Since Last Read
            0x3                     Reserved

           Bits 29:28 – TYPEL[1:0] Low Double-Word Error Type
           Indicates the type of error detected on the NVM 64-bit less significant read word. It is reset to None when
           this register is read except if an error occurs in the same cycle.
            Value       Name         Description
            0x0          None        No Error Detected Since Last Read
            0x1          Single      At Least One Single Error Detected Since last Read
            0x2          Dual        At Least One Dual Error Detected Since Last Read
            0x3                      Reserved




       © 2019 Microchip Technology Inc.                                Datasheet                       DS60001507E-page 680
                                                  SAM D5x/E5x Family Data Sheet
                                                    NVMCTRL – Nonvolatile Memory Controller

Bits 23:0 – ADDR[23:0] Error Address
Indicates the Byte address of the last detected error.




© 2019 Microchip Technology Inc.                    Datasheet               DS60001507E-page 681
                                                            SAM D5x/E5x Family Data Sheet
                                                             NVMCTRL – Nonvolatile Memory Controller

25.8.12 Debug Control

           Name:       DBGCTRL
           Offset:     0x28
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit         7            6            5            4            3            2           1           0
                                                                                          ECCELOG      ECCDIS
  Access                                                                                     R/W         R/W
   Reset                                                                                      0           0


           Bit 1 – ECCELOG Debugger ECC Error Tracking Mode
           0: ECC errors detected during a read initiated by a debugger are not logged.
           1: ECC errors detected during a read initiated by a debugger are logged.

           Bit 0 – ECCDIS Debugger ECC Read Disable
           Value      Description
           0          ECC errors for debugger reads are corrected and logged in INTFLAG
           1          ECC errors for debugger reads are not corrected or logged in INTFLAG




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 682
                                                           SAM D5x/E5x Family Data Sheet
                                                            NVMCTRL – Nonvolatile Memory Controller

25.8.13 SmartEEPROM Configuration

           Name:       SEECFG
           Offset:     0x2A
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit        7             6           5            4            3            2           1            0
                                                                                           APRDIS      WMODE
  Access                                                                                    R/W          R/W
   Reset                                                                                     0            0


           Bit 1 – APRDIS Automatic Page Reallocation Disable
           0: enables the Automatic page Reallocation.
           1: disables the Automatic page Reallocation.

           Bit 0 – WMODE Write Mode
           Indicates the type of bufferization used.
            Value      Name               Description
            0x0        UNBUFFERED A NVM write command is issued after each write in the pagebuffer
            0x1        BUFFERED           A NVM write command is issued when a write to a new page is requested




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 683
                                                                SAM D5x/E5x Family Data Sheet
                                                                NVMCTRL – Nonvolatile Memory Controller

25.8.14 SmartEEPROM Status

           Name:        SEESTAT
           Offset:      0x2C
           Reset:       0x00000000
           Property:    Read-Only


     Bit        31            30            29            28            27             26                25          24


  Access
   Reset


     Bit        23            22            21            20            19             18                17          16
                                                                                                   PSZ[2:0]
  Access                                                                               R                 R            R
   Reset                                                                               0                 0            x


     Bit        15            14            13            12             11            10                9            8
                                                                                            SBLK[3:0]
  Access                                                                 R             R                 R            R
   Reset                                                                 0             0                 0            x


     Bit         7             6             5             4             3             2                 1            0
                                                        RLOCK          LOCK          BUSY               LOAD       ASEES
  Access                                                   R             R             R                 R            R
   Reset                                                   0             x             0                 0            x


           Bits 18:16 – PSZ[2:0] SmartEEPROM Page Size
           This bit field is automatically loaded from the user page during startup.
           Indicates the page size. Not all device families will provide all the page sizes indicated in the table.

           Bits 11:8 – SBLK[3:0] Blocks Number In a Sector
           This bit field is automatically loaded from the user page during startup.
           Indicates the number of blocks allocated to a SEES.

           Bit 4 – RLOCK RLOCK
           SmartEEPROM Write Access To Register Address Space Is Locked

           Bit 3 – LOCK SmartEEPROM Section Locked
           This bit field is automatically loaded from the user page during startup.
           Access to the SmartEEPROM data is locked. Writes to AHB2 throws hardfault exceptions.
           0: SmartEEPROM access is not locked
           1: SmartEEPROM access is locked

           Bit 2 – BUSY Busy
           0: SmartEEPROM is ready.
           1: SmartEEPROM is busy processing a read or a write operation.




       © 2019 Microchip Technology Inc.                          Datasheet                               DS60001507E-page 684
                                                   SAM D5x/E5x Family Data Sheet
                                                    NVMCTRL – Nonvolatile Memory Controller

Bit 1 – LOAD Page Buffer Loaded
0: SmartEEPROM has not left unwritten data in the page buffer.
1: SmartEEPROM has left unwritten data in the page buffer.

Bit 0 – ASEES Active SmartEEPROM Sector
This bit field is automatically loaded during startup from a special fuse in the NVM.
Indicates the active SEES
0: SEES0 is active
1: SEES1 is active




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 685
