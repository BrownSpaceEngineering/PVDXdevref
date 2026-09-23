# 22. DMAC – Direct Memory Access Controller

*Source: `Atmel-SAMD51.pdf`, pages 374-450 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                            DMAC – Direct Memory Access Controller


22.    DMAC – Direct Memory Access Controller

22.1   Overview
       The Direct Memory Access Controller (DMAC) contains both a Direct Memory Access engine and a
       Cyclic Redundancy Check (CRC) engine. The DMAC can transfer data between memories and
       peripherals, and thus off-load these tasks from the CPU. It enables high data transfer rates with minimum
       CPU intervention, and frees up CPU time. With access to all peripherals, the DMAC can handle
       automatic transfer of data between communication modules.
       The DMA part of the DMAC has several DMA channels which all can receive different types of transfer
       triggers to generate transfer requests from the DMA channels to the arbiter, see also the Block Diagram.
       The arbiter will grant one DMA channel at a time to act as the active channel. When an active channel
       has been granted, the fetch engine of the DMAC will fetch a transfer descriptor from the SRAM and store
       it in the internal memory of the active channel, which will execute the data transmission.
       An ongoing data transfer of an active channel can be interrupted by a higher prioritized DMA channel.
       The DMAC will write back the updated transfer descriptor from the internal memory of the active channel
       to SRAM, and grant the higher prioritized channel to start transfer as the new active channel. Once a
       DMA channel is done with its transfer, interrupts and events can be generated optionally.
       The DMAC has four bus interfaces:
         • The data transfer bus is used for performing the actual DMA transfer.
         • The AHB/APB Bridge bus is used when writing and reading the I/O registers of the DMAC.
         • The descriptor fetch bus is used by the fetch engine to fetch transfer descriptors before data transfer
           can be started or continued.
         • The write-back bus is used to write the transfer descriptor back to SRAM.
       All buses are AHB master interfaces but the AHB/APB Bridge bus, which is an APB slave interface.
       Burst transfer options, buffered active channel to pre-fetch descriptors and advance quality of service
       features ensure low-latency transfers for high-speed peripherals or high-speed operations.
       The CRC engine can be used by software to detect an accidental error in the transferred data and to take
       corrective action, such as requesting the data to be sent again or simply not using the incorrect data.



22.2   Features
         • Data transfer from:
            – Peripheral to peripheral
            – Peripheral to memory
            – Memory to peripheral
            – Memory to memory
         • Transfer trigger sources
            – Software
            – Events from Event System
            – Dedicated requests from peripherals
         • SRAM based transfer descriptors




       © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 374
                                                 SAM D5x/E5x Family Data Sheet
                                                    DMAC – Direct Memory Access Controller

        – Single transfer using one descriptor
        – Multi-buffer or circular buffer modes by linking multiple descriptors
  •   Up to 32channels
        – Enable 32 independent transfers
        – Automatic descriptor fetch for each channel
        – Suspend/resume operation support for each channel
  •   Flexible arbitration scheme
        – 4 configurable priority levels for each channel
        – Fixed or round-robin priority scheme within each priority level
  •   From 1 to 256KB data transfer in a single block transfer
  •   Multiple addressing modes
        – Static
        – Configurable increment scheme
  •   Optional interrupt generation
        – On block transfer complete
        – On error detection
        – On channel suspend
  •   8 event inputs
        – One event input for each of the 8 least significant DMA channels
        – Can be selected to trigger normal transfers, periodic transfers or conditional transfers
        – Can be selected to suspend or resume channel operation
  •   4 event outputs
        – One output event for each of the 4 least significant DMA channels
        – Selectable generation on AHB, block, or transaction transfer complete
  •   Error management supported by write-back function
        – Dedicated Write-Back memory section for each channel to store ongoing descriptor transfer
  •   CRC polynomial software selectable to
        – CRC-16 (CRC-CCITT)
        – CRC-32 (IEEE® 802.3)




© 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 375
                                                                            SAM D5x/E5x Family Data Sheet
                                                                                      DMAC – Direct Memory Access Controller


22.3     Block Diagram
         Figure 22-1. DMAC Block Diagram

                                                                                          CPU


                                                                                                                                                   Optional
           SRAM                                                                             M

                 Transfer                                                             HIGH SPEED                             AHB/APB
                                   Write-Back                S                                                         S
                 Control                                                              BUS MATRIX                              Bridge
                                     Buffer
                Descriptor
                                                                                                                                       Event System
                                                                                  M              M       S
             Descriptor




                                    Write-back




                                                                                                                                       Peripheral




                                                                       Transfer




                                                                                           Transfer
               Fetch




                                                                         Data




                                                                                             Data
                                                                                                       AHB/APB
                                                                                                        Bridge




                                                                                                                                        Request / Ack

                                                                                                                                                        Event Input / Ack
                                                                                                                                                         Event Output
               DMAC Internal Architecture
                                                                           Master
                                                                                                Fifo          Fetch
                                 DMA Channels                             Interface
                                                 Channel n                                                    Engine

                                  Channel 0
                             n                                                                               Pre-Fetch
                                                                                                             Channel
                                                             Arbiter                   Active
                                                                                      Channel

                                                                                                          CRC Engine              Interrupts




22.4     Signal Description
         Not applicable.


22.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

22.5.1   I/O Lines
         Not applicable.

22.5.2   Power Management
         The DMAC will continue to operate in any Sleep mode where the selected source clock is running. The
         DMAC’s interrupts can be used to wake-up the device from Sleep modes. Events connected to the event
         system can trigger other operations in the system without exiting Sleep modes. On hardware or software
         Reset, all registers are set to their Reset value.
         Related Links
         18. PM – Power Manager

22.5.3   Clocks
         An AHB clock (CLK_DMAC_AHB) is required to clock the DMAC. This clock can be configured in the
         Main Clock peripheral (MCLK) before using the DMAC, and the default state of CLK_DMAC_AHB can be
         found in the MCLK.AHBMASK register.
         Related Links




         © 2019 Microchip Technology Inc.                                         Datasheet                                DS60001507E-page 376
                                                           SAM D5x/E5x Family Data Sheet
                                                              DMAC – Direct Memory Access Controller

         15.6.2.6 Peripheral Clock Masking

22.5.4   DMA
         Not applicable.

22.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the DMAC interrupt requires the
         interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller

22.5.6   Events
         The events are connected to the event system.

22.5.7   Debug Operation
         When the CPU is halted in Debug mode the DMAC will halt normal operation. The DMAC can be forced
         to continue operation during debugging. Refer to 22.8.6 DBGCTRL for details.

22.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Pending register (INTPEND)
           • Channel Interrupt Flag Status and Clear register (CHINTFLAG)
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.

22.5.9   Analog Connections
         Not applicable.



22.6     Functional Description

22.6.1   Principle of Operation
         The DMAC consists of a DMA module and a CRC module.
22.6.1.1 DMA
         The DMAC can transfer data between memories and peripherals without interaction from the CPU. The
         data transferred by the DMAC are called transactions, and these transactions can be split into smaller
         data transfers. The following figure shows the relationship between the different transfer sizes:




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 377
                                                                   SAM D5x/E5x Family Data Sheet
                                                                      DMAC – Direct Memory Access Controller

          Figure 22-2. DMA Transfer Sizes
                                 Link Enabled                    Link Enabled                    Link Enabled




                 Beat transfer                  Burst transfer                  Block transfer

                                                             DMA transaction
           • Beat transfer: The size of one data transfer bus access, and the size is selected by writing the Beat
             Size bit group in the Block Transfer Control register (BTCTRL.BEATSIZE)
           • Block transfer: The amount of data one transfer descriptor can transfer, and the amount can range
             from 1 to 64k beats. A block transfer can be interrupted.
           • Transaction: The DMAC can link several transfer descriptors by having the first descriptor pointing to
             the second and so forth, as shown in the figure above. A DMA transaction is the complete transfer of
             all blocks within a linked list.
          A transfer descriptor describes how a block transfer should be carried out by the DMAC, and it must
          remain in SRAM. For further details on the transfer descriptor refer to 22.6.2.3 Transfer Descriptors.
          The figure above shows several block transfers linked together, which are called linked descriptors. For
          further information about linked descriptors, refer to 22.6.3.1 Linked Descriptors.
          A DMA transfer is initiated by an incoming transfer trigger on one of the DMA channels. This trigger can
          be configured to be either a software trigger, an event trigger, or one of the dedicated peripheral triggers.
          The transfer trigger will result in a DMA transfer request from the specific channel to the arbiter. If there
          are several DMA channels with pending transfer requests, the arbiter chooses which channel is granted
          access to become the active channel. The DMA channel granted access as the active channel will carry
          out the transaction as configured in the transfer descriptor. A current transaction can be interrupted by a
          higher prioritized channel, but will resume the block transfer when the according DMA channel is granted
          access as the active channel again.
          For each beat transfer, an optional output event can be generated. For each block transfer, optional
          interrupts and an optional output event can be generated. When a transaction is completed, dependent of
          the configuration, the DMA channel will either be suspended or disabled.
22.6.1.2 CRC
          The internal CRC engine supports two commonly used CRC polynomials: CRC-16 (CRC-CCITT) and
          CRC-32 (IEEE 802.3). It can be used on a selectable DMA channel, or on the I/O interface. Refer to
          22.6.3.8 CRC Operation for details.

22.6.2    Basic Operation

22.6.2.1 Initialization

          DMAC Initialization
          Before DMAC is enabled, it must be configured as defined below:
           • The SRAM address of where the descriptor memory section is located must be written to the
             Description Base Address (BASEADDR) register.
           • The SRAM address of where the write-back section should be located must be written to the Write-
             Back Memory Base Address (WRBADDR) register.




         © 2019 Microchip Technology Inc.                            Datasheet                                  DS60001507E-page 378
                                                    SAM D5x/E5x Family Data Sheet
                                                       DMAC – Direct Memory Access Controller

  • Priority level x of the arbiter can be enabled by setting the Priority Level x Enable bit in the Control
    register (CTRL.LVLENx=1)

DMA Channel Initialization
Before a DMA channel is enabled, the DMA channel and the corresponding first transfer descriptor must
be configured, as defined below:
  • DMA Channel Configuration:
     – The channel number of the DMA channel to configure must be written to the Channel Control A
        (CHCTRLA) register.
     – Trigger action must be selected by writing the Trigger Action bit field in the Channel Control A
        (CHCTRLA.TRIGACT) register.
     – Trigger source must be selected by writing the Trigger Source bit field in the Channel Control A
        (CHCTRLA.TRIGSRC) register.
  • Transfer Descriptor
     – The size of each access of the data transfer bus must be selected by writing the Beat Size bit
        group in the Block Transfer Control (BTCTRL.BEATSIZE) register.
     – The transfer descriptor must be made valid by writing a one to the Valid bit in the Block Transfer
        Control (BTCTRL.VALID) register.
     – Number of beats in the block transfer must be selected by writing the Block Transfer Count
        (BTCNT) register.
     – Source address for the block transfer must be selected by writing the Block Transfer Source
        Address (SRCADDR) register.
     – Destination address for the block transfer must be selected by writing the Block Transfer
        Destination Address (DSTADDR) register.

CRC Calculation
If CRC calculation is needed, the CRC engine must be configured before it is enabled, as described
below:
  • The CRC input source must selected by writing the CRC Input Source bit group in the CRC Control
    (CRCCTRL.CRCSRC) register.
  • The type of CRC calculation must be selected by writing the CRC Polynomial Type bit group in the
    CRC Control (CRCCTRL.CRCPOLY) register.
  • If I/O is selected as input source, the beat size must be selected by writing the CRC Beat Size bit
    group in the CRC Control (CRCCTRL.CRCBEATSIZE) register.

Register Properties
The following DMAC registers are enable-protected, that is, they can only be written when the DMAC is
disabled (CTRL.DMAENABLE=0):
  • The Descriptor Base Memory Address (BASEADDR) register
  • The Write-Back Memory Base Address (WRBADDR) register
The following DMAC bit is enable-protected, that is, it can only be written when the DMAC and CRC are
disabled (CTRL.DMAENABLE=0 and CRCCTRL.CRCSRC=0):
  • The Software Reset bit in the Control (CTRL.SWRST) register




© 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 379
                                                             SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

         The following DMA channel bit is enable-protected, meaning that it can only be written when the
         corresponding DMA channel is disabled:
          • The Channel Software Reset bit in the Channel Control A (CHCTRLA.SWRST) register
         The following CRC registers are enable-protected, that is, they can only be written when the CRC is
         disabled (CRCCTRL.CRCSRC=0):
          • The CRC Control (CRCCTRL) register
          • CRC Checksum (CRCCHKSUM) register
         Enable-protection is denoted by the ‘Enable-Protected’ property in the register description.
22.6.2.2 Enabling, Disabling, and Resetting
         The DMAC is enabled by writing the DMA Enable bit in the Control (CTRL.DMAENABLE) register to '1'.
         The DMAC is disabled by writing a '0' to the CTRL.DMAENABLE register.
         A DMA channel is enabled by writing the Enable bit in the Channel Control A register
         (CHCTRLA.ENABLE) to '1', after the corresponding channel ID to the channel is configured. A DMA
         channel is disabled by writing a '0' to CHCTRLAn.ENABLE.
         The CRC is enabled by writing a value to the CRC Source bits in the Control register
         (CRCCTRL.CRCSRC). The CRC is disabled by writing a '0' to CRCCTRL.CRCSRC.
         The DMAC is reset by writing a '1' to the Software Reset bit in the Control register (CTRL.SWRST) while
         the DMAC and CRC are disabled. All registers in the DMAC except DBGCTRL will be reset to their initial
         state.
         A DMA channel is reset by writing a '1' to the Software Reset bit in the Channel Control A register
         (CHCTRLAn.SWRST), after the corresponding channel is configured. The channel registers will be reset
         to their initial state. The corresponding DMA channel must be disabled in order for the Reset to take
         effect.
22.6.2.3 Transfer Descriptors
         The transfer descriptors, together with the channel configurations, decide how a block transfer should be
         executed. Before a DMA channel is enabled (CHCTRLA.ENABLE is written to one) and receives a
         transfer trigger, its first transfer descriptor must be initialized and valid (BTCTRL.VALID). The first transfer
         descriptor describes the first block transfer of a transaction.
         All transfer descriptors must reside in SRAM. The addresses stored in the Descriptor Memory Section
         Base Address (BASEADDR) and Write-Back Memory Section Base Address (WRBADDR) registers tell
         the DMAC where to find the descriptor memory section and the write-back memory section.
         The descriptor memory section is where the DMAC expects to find the first transfer descriptors for all
         DMA channels. As BASEADDR points only to the first transfer descriptor of channel ‘0’ (see figure below).
         All first transfer descriptors must be stored in a contiguous memory section, where the transfer
         descriptors must be ordered according to their channel number. For further details on linked descriptors,
         refer to 22.6.3.1 Linked Descriptors.
         The write-back memory section is where the DMAC stores the transfer descriptors for the ongoing block
         transfers. WRBADDR points to the ongoing transfer descriptor of channel ‘0’. All ongoing transfer
         descriptors are stored in a contiguous memory section where the transfer descriptors are ordered
         according to their channel number. The figure below shows an example of linked descriptors on DMA
         channel ‘0’. For additional information on linked descriptors, refer to the 22.6.3.1 Linked Descriptors.




        © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 380
                                                                      SAM D5x/E5x Family Data Sheet
                                                                              DMAC – Direct Memory Access Controller

         Figure 22-3. Memory Sections

                                                                                            0x00000000

                                                                                            DSTADDR
                              DESCADDR         Channel 0 – Last Descriptor
                                                                                            SRCADDR

                                                                                             BTCNT
                                                                                             BTCTRL




                                                                                            DESCADDR

                                                                                            DSTADDR
                              DESCADDR         Channel 0 – Descriptor n-1
                                                                                            SRCADDR

                                                                                             BTCNT
                                                                                             BTCTRL


                                            Descriptor Section
                                              Channel n – First Descriptor
                                                                                            DESCADDR
                                               Channel 2 – First Descriptor
                                               Channel 1 – First Descriptor                 DSTADDR
                               BASEADDR        Channel 0 – First Descriptor
                                                                                            SRCADDR

                                                                                             BTCNT
                                                                                             BTCTRL




                                            Write-Back Section
                                                                                             Undefined
                                             Channel n Ongoing Descriptor

                                                                                             Undefined
                                              Channel 2 Ongoing Descriptor
                                              Channel 1 Ongoing Descriptor
                                                                                             Undefined
                               WRBADDR        Channel 0 Ongoing Descriptor
                                                                                             Undefined
                                                                                             Undefined
                                           Device Memory Space

         The size of the descriptor and write-back memory sections are dependent on the number of the most
         significant enabled DMA channel m, as shown below:
         ���� = 128bits ⋅ � + 1
         For memory optimization, it is recommended to use the less significant DMA channels, if not all channels
         are required.
         The descriptor and write-back memory sections can either be two separate memory sections, or they can
         share a memory section (BASEADDR=WRBADDR). The benefit of having them in two separate sections,
         is that the same transaction for a channel can be repeated without having to modify the first transfer
         descriptor. In addition, the latency from fetching the first descriptor of a transaction to the first burst
         transfer is executed, is reduced.
22.6.2.4 Arbitration
         If a DMA channel is enabled and not suspended when it receives a transfer trigger, it will send a transfer
         request to the arbiter. When the arbiter receives the transfer request it will include the DMA channel in the
         queue of channels having pending transfers, and the corresponding Pending Channel x bit in the Pending
         Channels registers (PENDCH.PENDCHx) will be set. Depending on the arbitration scheme, the arbiter
         will choose which DMA channel will be the next active channel. The next transfer descriptor will be
         fetched from SRAM memory and stored internally in the Pre-Fetch Channel. The active channel is the




        © 2019 Microchip Technology Inc.                                 Datasheet                       DS60001507E-page 381
                                                              SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

DMA channel being granted access to perform its next burst transfer. When the Active Channel has
completed a burst transfer, the descriptor stored in the Pre-Fetch Channel is transferred to the Active
Channel and a new burst will take place.
When the descriptor stored in the Pre-Fetch Channel is transferred to the Active Channel, the
corresponding PENDCH.PENDCHx will be cleared. In the same way, depending on trigger action settings
and if the upcoming burst transfer is the first for the transfer request or not, the corresponding Busy
Channel x bit in the Busy Channels register (BUSYCH.BUSYCHx), will either be set or remain '1'. When
the channel has performed its granted burst transfer(s) it will be either fed into the queue of channels with
pending transfers, set to be waiting for a new transfer trigger, suspended, or disabled. This depends on
the channel and block transfer configuration. If the DMA channel is set to wait for a new transfer trigger,
suspended or disabled, the corresponding BUSYCH.BUSYCHx will be cleared.
If a DMA channel is suspended while it has a pending transfer, it will be removed from the queue of
pending channels, but the corresponding PENDCH.PENDCHx will remain set. The status will also be
indicated in CHINTFLAGn.SUSP. When the same DMA channel is resumed, it will be added to the queue
of pending channels again.
If a DMA channel gets disabled (CHCTRLA.ENABLE=0) while it has a pending transfer, it will be removed
from the queue of pending channels, and the corresponding PENDCH.PENDCHx will be cleared.
Figure 22-4. Arbiter Overview
                                          Arbiter
                 Channel Pending

                                                             Priority
                 Channel Suspend
                                                             decoder
   Channel 0
                 Channel Priority Level
                 Channel Burst Done


                                                                             Channel Number
                 Channel Pending                                                                Empty   Pre-Fetch
                                                                                                        Channel
                 Channel Suspend
   Channel N
                 Channel Priority Level
                 Channel Burst Done                                                                      Active
                                                                                                                     Master
                                                                                   Burst Done




                                            Level Enable   ACTIVE.LVLEXx                                Channel                 Burst Transfer
                                           CTRL.LVLENx     PRICTRLx.LVLPRI                                          Interface



Priority Levels
When a channel level is pending or the channel is transferring data, the corresponding Level Executing
bit is set in the Active Channel and Levels register (ACTIVE.LVLEXx).
Each DMA channel supports up to4-level priority scheme. The number of supported priority levels will
differ from one device family to another.
The priority level for a channel is configured by writing to the Channel Arbitration Level bit group in the
Channel Priority Level register (CHPRILVL.PRILVL). As long as all priority levels are enabled, a channel
with a higher priority level number will have priority over a channel with a lower priority level number. A
priority level is enabled by writing the Priority Level x Enable bit in the Control register (CTRL.LVLENx) to
'1', for the corresponding level.
Within each priority level, the DMAC's arbiter can be configured to prioritize statically or dynamically. For
the arbiter to perform static arbitration within a priority level, the Level X Round-Robin Scheduling Enable
bit in the Priority Control x register (PRICTRL0.RRLVLENx) has to be written to '0'. When static arbitration
is enabled (PRICTRL0.RRLVLENx is '0'), the arbiter will prioritize a low channel number over a high




© 2019 Microchip Technology Inc.                                Datasheet                                           DS60001507E-page 382
                                                    SAM D5x/E5x Family Data Sheet
                                                       DMAC – Direct Memory Access Controller

channel number as shown in Static Priority Scheduling. When using the static scheme, there is a risk of
high channel numbers never being granted access as the active channel. This can be avoided using a
dynamic arbitration scheme.
Figure 22-5. Static Priority Scheduling

                        Lowest Channel            Channel 0               Highest Priority


                                                      .
                                                      .
                                                      .
                                                   Channel x
                                                  Channel x+1

                                                      .
                                                      .
                                                      .

                       Highest Channel            Channel N               Lowest Priority

The dynamic arbitration scheme in the DMAC is round-robin. Round-robin arbitration is enabled by writing
PRICTRL0.RRLVLEN to '1', for a given priority level x. With the round-robin scheme, the channel number
of the last channel being granted access will have the lowest priority the next time the arbiter has to grant
access to a channel within the same priority level, as shown in Figure 22-6. The channel number of the
last channel being granted access as the active channel is stored in the Level x Channel Priority Number
bit group in the Priority Control 0 register (PRICTRL0.LVLPRIx) for the corresponding priority level.
Figure 22-6. Dynamic (Round-Robin) Priority Scheduling
        Channel x last acknowledge request                       Channel (x+1) last acknowledge request

          Channel 0                                               Channel 0



                                                                      .
                                                                      .
                                                                      .
         Channel x             Lowest Priority                    Channel x
        Channel x+1            Highest Priority                  Channel x+1           Lowest Priority
                                                                 Channel x+2           Highest Priority
                                                                      .
                                                                      .
                                                                      .

        Channel N                                                 Channel N




© 2019 Microchip Technology Inc.                     Datasheet                               DS60001507E-page 383
                                                             SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

22.6.2.5 Data Transmission
         Before the DMAC can perform a data transmission, a DMA channel has to be configured and enabled, its
         corresponding transfer descriptor has to be initialized, and the arbiter has to grant the DMA channel
         access as the active channel.
         Once the arbiter has granted a DMA channel access as the active channel (refer to DMA Block Diagram
         section) the transfer descriptor for the DMA channel will be fetched from SRAM using the fetch bus, and
         stored in the internal memory for the active channel. For a new block transfer, the transfer descriptor will
         be fetched from the descriptor memory section (BASEADDR); For an ongoing block transfer, the
         descriptor will be fetched from the write-back memory section (WRBADDR). By using the data transfer
         bus, the DMAC will read the data from the current source address and write it to the current destination
         address. For further details on how the current source and destination addresses are calculated, refer to
         the section on Addressing.
         The arbitration procedure is performed after each burst transfer. If the current DMA channel is granted
         access again, the block transfer counter (BTCNT) of the internal transfer descriptor will be decremented
         by the number of beats in a burst transfer, the optional output event Beat will be generated if configured
         and enabled, and the active channel will perform a new burst transfer. If a different DMA channel than the
         current active channel is granted access, the block transfer counter value will be written to the write-back
         section before the transfer descriptor of the newly granted DMA channel is fetched into the internal
         memory of the active channel.
         When a block transfer has come to its end (BTCNT is zero), the Valid bit in the Block Transfer Control
         register will be cleared (BTCTRL.VALID=0) before the entire transfer descriptor is written to the write-
         back memory. The optional interrupts, Channel Transfer Complete and Channel Suspend, and the
         optional output event Block, will be generated if configured and enabled. After the last block transfer in a
         transaction, the Next Descriptor Address register (DESCADDR) will hold the value 0x00000000, and the
         DMA channel will either be suspended or disabled, depending on the configuration in the Block Action bit
         group in the Block Transfer Control register (BTCTRL.BLOCKACT). If the transaction has further block
         transfers pending, DESCADDR will hold the SRAM address to the next transfer descriptor to be fetched.
         The DMAC will fetch the next descriptor into the internal memory of the active channel and write its
         content to the write-back section for the channel, before the arbiter gets to choose the next active
         channel.
         Related Links
         22.3 Block Diagram

22.6.2.6 Transfer Triggers and Actions
         A DMA transfer through a DMA channel can be started only when a DMA transfer request is detected,
         and the DMA channel has been granted access to the DMA. A transfer request can be triggered from
         software, from a peripheral, or from an event. There are dedicated Trigger Source selections for each
         DMA Channel n Control A (CHCTRLAn.TRIGSRC).
         The trigger actions are available in the Trigger Action bit group in the Channel n Control A register
         (CHCTRLAn.TRIGACT). By default, a trigger generates a request for a block transfer operation. If a
         single descriptor is defined for a channel, the channel is automatically disabled when a block transfer has
         been completed. If a list of linked descriptors is defined for a channel, the channel is automatically
         disabled when the last descriptor in the list is executed. As long as the list still has descriptors to execute,
         the channel will be waiting for the next block transfer trigger. When enabled again, the channel will wait
         for the next block transfer trigger. The trigger actions can also be configured to generate a request for a
         burst transfer (CHCTRLAn.TRIGACT=0x2) or transaction transfer (CHCTRLAn.TRIGACT=0x3) instead of
         a block transfer (CHCTRLAn.TRIGACT=0x0).




        © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 384
                                                                         SAM D5x/E5x Family Data Sheet
                                                                          DMAC – Direct Memory Access Controller

        The following figure shows an example where triggers are used with two linked block descriptors.
        Figure 22-7. Trigger Action and Transfers
                      Beat Trigger Action

                          CHENn
                                                   Trigger Lost

                          Trigger

                         PENDCHn


                         BUSYCHn


                                             Block Transfer                          Block Transfer
                         Data Transfer             BEAT           BEAT    BEAT          BEAT          BEAT   BEAT




                      Block Trigger Action

                          CHENn
                                                   Trigger Lost

                          Trigger

                         PENDCHn


                         BUSYCHn


                                             Block Transfer                          Block Transfer
                          Data Transfer            BEAT           BEAT     BEAT          BEAT         BEAT   BEAT




                      Transaction Trigger Action

                           CHENn
                                                   Trigger Lost

                           Trigger

                         PENDCHn


                         BUSYCHn


                                              Block Transfer                         Block Transfer
                           Data Transfer           BEAT           BEAT     BEAT          BEAT         BEAT   BEAT



        If the trigger source generates a transfer request for a channel during an ongoing transfer, the new
        transfer request will be kept pending (CHSTATUSn.PEND=1), and the new transfer can start after the
        ongoing one is done. Only one pending transfer can be kept per channel. If the trigger source generates
        more transfer requests while one is already pending, the additional ones will be lost. All channels pending
        status flags are also available in the Pending Channels register (PENDCH).
        When the transfer starts, the corresponding Channel Busy status flag is set in Channel n Status register
        (CHSTATUSn.BUSY). When the trigger action is complete, the Channel Busy status flag is cleared. All
        channel busy status flags are also available in the Busy Channels register (BUSYCH) in DMAC.
22.6.2.7 Addressing
        Each block transfer needs to have both a source address and a destination address defined. The source
        address is set by writing the Transfer Source Address (SRCADDR) register, the destination address is set
        by writing the Transfer Destination Address (SRCADDR) register.
        The addressing of this DMAC module can be static or incremental, for either source or destination of a
        block transfer, or both.




       © 2019 Microchip Technology Inc.                                  Datasheet                           DS60001507E-page 385
                                                  SAM D5x/E5x Family Data Sheet
                                                     DMAC – Direct Memory Access Controller

Incrementation for the source address of a block transfer is enabled by writing the Source Address
Incrementation Enable bit in the Block Transfer Control register (BTCTRL.SRCINC=1). The step size of
the incrementation is configurable and can be chosen by writing the Step Selection bit in the Block
Transfer Control register (BTCTRL.STEPSEL=1) and writing the desired step size in the Address
Increment Step Size bit group in the Block Transfer Control register (BTCTRL.STEPSIZE). If
BTCTRL.STEPSEL=0, the step size for the source incrementation will be the size of one beat.
When source address incrementation is configured (BTCTRL.SRCINC=1), SRCADDR is calculated as
follows:
If BTCTRL.STEPSEL=1:

SRCADDR = SRCADDR����� + ����� ⋅ �������� + 1 ⋅ 2STEPSIZE

If BTCTRL.STEPSEL=0:
SRCADDR = SRCADDR����� + ����� ⋅ �������� + 1

  •   SRCADDRSTART is the source address of the first beat transfer in the block transfer
  •   BTCNT is the initial number of beats remaining in the block transfer
  •   BEATSIZE is the configured number of bytes in a beat
  •   STEPSIZE is the configured number of beats for each incrementation
The following figure shows an example where DMA channel 0 is configured to increment the source
address by one beat after each beat transfer (BTCTRL.SRCINC=1), and DMA channel 1 is configured to
increment the source address by two beats (BTCTRL.SRCINC=1, BTCTRL.STEPSEL=1, and
BTCTRL.STEPSIZE=0x1). As the destination address for both channels are peripherals, destination
incrementation is disabled (BTCTRL.DSTINC=0).
Figure 22-8. Source Address Increment

      SRC Data Buffer
                a
                b
                c
                d
                e
                f

Incrementation for the destination address of a block transfer is enabled by setting the Destination
Address Incrementation Enable bit in the Block Transfer Control register (BTCTRL.DSTINC=1). The step
size of the incrementation is configurable by clearing BTCTRL.STEPSEL=0 and writing
BTCTRL.STEPSIZE to the desired step size. If BTCTRL.STEPSEL=1, the step size for the destination
incrementation will be the size of one beat.
When the destination address incrementation is configured (BTCTRL.DSTINC=1), DSTADDR must be
set and calculated as follows:




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 386
                                                           SAM D5x/E5x Family Data Sheet
                                                              DMAC – Direct Memory Access Controller

         ������� = ������������ + ����� • �������� + 1 • 2�������� where BTCTRL.STEPSEL is zero

         ������� = ������������ + ����� • �������� + 1                           where BTCTRL.STEPSEL is one


          •   DSTADDRSTART is the destination address of the first beat transfer in the block transfer
          •   BTCNT is the initial number of beats remaining in the block transfer
          •   BEATSIZE is the configured number of bytes in a beat
          •   STEPSIZE is the configured number of beats for each incrementation
         The following figure shows an example where DMA channel 0 is configured to increment destination
         address by one beat (BTCTRL.DSTINC=1) and DMA channel 1 is configured to increment destination
         address by two beats (BTCTRL.DSTINC=1, BTCTRL.STEPSEL=0, and BTCTRL.STEPSIZE=0x1). As
         the source address for both channels are peripherals, source incrementation is disabled
         (BTCTRL.SRCINC=0).
         Figure 22-9. Destination Address Increment

                                                                                            DST Data Buffer
                                                                                                     a
                                                                                                     b
                                                                                                     c


                                                                                                     d



22.6.2.8 Internal FIFO
         To improve the bandwidth, the DMAC can support FIFO operation. When single-beat burst configuration
         is selected (CHCTRALx.BURSTLEN = SINGLE), the channel waits until the FIFO can transmit or accept
         a single beat transfer before it requests a bus access to write to the destination address. In all other
         cases, the channel waits until the FIFO threshold is reached before it requests a bus access to write to
         the destination address. The threshold is configurable and can be set by writing the THRESHOLD bits in
         the Channel x Control A register.
         If the DMAC completes the read operations before the threshold is reached, the write to the destination is
         automatically enabled. If the FIFO is empty and the read from source is ongoing, the DMA will wait again
         until the FIFO threshold is reached before it requests a bus access to write the destination.
22.6.2.9 Error Handling
         If a bus error is received from an AHB slave during a DMA data transfer, the corresponding active
         channel is disabled and the corresponding Channel Transfer Error Interrupt flag in the Channel Interrupt
         Status and Clear register (CHINTFLAG.TERR) is set. If enabled, the optional transfer error interrupt is
         generated. The transfer counter will not be decremented and its current value is written-back in the write-
         back memory section before the channel is disabled.
         When the DMAC fetches an invalid descriptor (BTCTRL.VALID=0) or when the channel is resumed and
         the DMA fetches the next descriptor with null address (DESCADDR=0x00000000), the corresponding
         channel operation is suspended, the Channel Suspend Interrupt Flag in the Channel Interrupt Flag Status




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 387
                                                             SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

          and Clear register (CHINTFLAG.SUSP) is set, and the Channel Fetch Error bit in the Channel Status
          register (CHSTATUS.FERR) is set. If enabled, the optional suspend interrupt is generated.

22.6.3    Additional Features

22.6.3.1 Linked Descriptors
          A transaction can consist of either a single block transfer or of several block transfers. When a
          transaction consists of several block transfers it is done with the help of linked descriptors.
          Figure 22-3 illustrates how linked descriptors work. When the first block transfer is completed on DMA
          channel 0, the DMAC fetches the next transfer descriptor, which is pointed to by the value stored in the
          Next Descriptor Address (DESCADDR) register of the first transfer descriptor. Fetching the next transfer
          descriptor (DESCADDR) is continued until the last transfer descriptor. When the block transfer for the last
          transfer descriptor is executed and DESCADDR=0x00000000, the transaction is terminated. For further
          details on how the next descriptor is fetched from SRAM, refer to section 22.6.2.5 Data Transmission.
22.6.3.1.1 Adding Descriptor to the End of a List
          To add a new descriptor at the end of the descriptor list, create the descriptor in SRAM, with
          DESCADDR=0x00000000 indicating that it is the new last descriptor in the list, and modify the
          DESCADDR value of the current last descriptor to the address of the newly created descriptor.
22.6.3.1.2 Modifying a Descriptor in a List
          In order to add descriptors to a linked list, the following actions must be performed:
            1.   Enable the Suspend interrupt for the DMA channel.
            2.   Enable the DMA channel.
            3.   Reserve memory space in SRAM to configure a new descriptor.
            4.   Configure the new descriptor:
                  – Set the next descriptor address (DESCADDR)
                  – Set the destination address (DSTADDR)
                  – Set the source address (SRCADDR)
                  – Configure the block transfer control (BTCTRL) including
                       • Optionally enable the suspend block action
                       • Set the descriptor VALID bit
            5.   Clear the VALID bit for the existing list and for the descriptor which has to be updated.
            6.   Read DESCADDR from the write-back memory.
                  – If the DMA has not already fetched the descriptor that requires changes (i.e., DESCADDR is
                     wrong):
                       • Update the DESCADDR location of the descriptor from the list
                       • Optionally clear the suspend block action
                       • Set the descriptor VALID bit to '1'
                       • Optionally enable the Resume Software command
                  – If the DMA is executing the same descriptor as the one that requires changes:
                       • Set the Channel Suspend Software command and wait for the suspend interrupt
                       • Update the next descriptor address (DESCRADDR) in the write-back memory
                       • Clear the interrupt sources and set the Resume Software command
                       • Update the DESCADDR location of the descriptor from the list
                       • Optionally clear the suspend block action
                       • Set the descriptor VALID bit to '1'




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 388
                                                              SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

           7.   Go to step 4 if needed.
22.6.3.1.3 Adding a Descriptor Between Existing Descriptors
         To insert a new descriptor 'C' between two existing descriptors ('A' and 'B'), the descriptor currently
         executed by the DMA must be identified.
           1.   If DMA is executing descriptor B, descriptor C cannot be inserted.
           2.   If DMA has not started to execute descriptor A, follow the steps:
                2.1.    Set the descriptor A VALID bit to '0'.
                2.2.      Set the DESCADDR value of descriptor A to point to descriptor C instead of descriptor B.
                2.3.      Set the DESCADDR value of descriptor C to point to descriptor B.
                2.4.      Set the descriptor A VALID bit to '1'.
           3.   If DMA is executing descriptor A:
                3.1.    Apply the software suspend command to the channel and
                3.2.    Perform steps 2.1 through 2.4.
                3.3.    Apply the software resume command to the channel.
22.6.3.2 Transfer Quality of Service
         Each priority level group has dedicated quality of service settings. The setting can be written in the
         corresponding Quality of Service bit group in the Priority Control x register (PRICTRL0.QOSn).
         Figure 22-10. Quality of Service

             Transfer Trigger Channel 0

             Transfer Trigger Channel 1

                        Fetch Operation      CH0      CH1            CH0                                  CH1


                          Data Transfer               Active CH0             Active CH1      Active CH0             Active CH1


                Quality of Service Value
                                            QOS CH0                QOS CH1                QOS CH0               QOS CH1
                ( QOS CH0 < QOS CH1)

         When a channel is stored in the Pre-Fetch or Active Channel, the corresponding PRICTRLx.QOS bits
         value is stored in the respective channel. As shown in Quality of Service, the DMAC will select the
         highest QOS value between Active and Pre-Fetch channels. This value will apply to all DMAC buses.
22.6.3.3 Channel Suspend
         The channel operation can be suspended at any time by software by writing a '1' to the Suspend
         command in the Command bit field of Channel Control B register (CHCTRLB.CMD). After the ongoing
         burst transfer is completed, the channel operation is suspended and the suspend command is
         automatically cleared.
         When suspended, the Channel Suspend Interrupt flag in the Channel Interrupt Status and Clear register
         is set (CHINTFLAG.SUSP=1) and the optional suspend interrupt is generated.
         By configuring the block action to suspend by writing Block Action bit group in the Block Transfer Control
         register (BTCTRL.BLOCKACT is 0x2 or 0x3), the DMA channel will be suspended after it has completed
         a block transfer. The DMA channel will be kept enabled and will be able to receive transfer triggers, but it
         will be removed from the arbitration scheme.




         © 2019 Microchip Technology Inc.                          Datasheet                                DS60001507E-page 389
                                                                                    SAM D5x/E5x Family Data Sheet
                                                                                          DMAC – Direct Memory Access Controller

         If an invalid transfer descriptor (BTCTRL.VALID=0) is fetched from SRAM, the DMA channel will be
         suspended, and the Channel Fetch Error bit in the Channel Status register(CHASTATUS.FERR) will be
         set.
         Note: Only enabled DMA channels can be suspended. If a channel is disabled when it is attempted to
         be suspended, the internal suspend command will be ignored.
         For more details on transfer descriptors, refer to section 22.6.2.3 Transfer Descriptors.

22.6.3.4 Channel Resume and Next Suspend Skip
         A channel operation can be resumed by software by setting the Resume command in the Command bit
         field of the Channel Control B register (CHCTRLB.CMD). If the channel is already suspended, the
         channel operation resumes from where it previously stopped when the Resume command is detected.
         When the Resume command is issued before the channel is suspended, the next suspend action is
         skipped and the channel continues the normal operation.
         Figure 22-11. Channel Suspend/Resume Operation
            CHENn


                                Descriptor 0                      Descriptor 1                     Descriptor 2                              Descriptor 3
         Memory Descriptor   (suspend disabled)                (suspend enabled)                (suspend enabled)                               (last)
                                                                                                                                  Channel
                                                                                                                                 suspended
                               Fetch
                                                    Block                            Block                            Block                                   Block
                 Transfer
                                                  Transfer 0                       Transfer 1                       Transfer 2                              Transfer 3


         Resume Command

                                                                                                      Suspend skipped


22.6.3.5 Event Input Actions
         The event input actions are available only on the least significant DMA channels. For details on channels
         with event input support, refer to the Event System documentation.
         Before using event input actions, the event controller must be configured first according to the following
         table, and the Channel Event Input Enable bit in the Channel Event Control register (CHEVCTRL.EVIE)
         must be written to '1'. Refer also to 22.6.6 Events.
         Table 22-1. Event Input Action

         Action                                                CHEVCTRL.EVACT                                             CHCTRLA.TRIGSRC
         None                                                  NOACT                                                      -
         Normal Transfer                                       TRIG                                                       DISABLE
         Conditional Transfer on Strobe                        TRIG                                                       Any peripheral
         Conditional Transfer                                  CTRIG
         Conditional Block Transfer                            CBLOCK
         Channel Suspend                                       SUSPEND
         Channel Resume                                        RESUME
         Skip Next Block Suspend                               SSKIP
         Increase priority                                     INCPRI


         Normal Transfer
         The event input is used to trigger a beat or burst transfer on peripherals.




        © 2019 Microchip Technology Inc.                                               Datasheet                                              DS60001507E-page 390
                                                                SAM D5x/E5x Family Data Sheet
                                                                 DMAC – Direct Memory Access Controller

The event is acknowledged as soon as the event is received. When received, both the Channel Pending
status bit in the Channel Status register (CHSTATUS.PEND) and the corresponding Channel n bit in the
Pending Channels register (PENDCH.PENDCHn) are set. If the event is received while the channel is
pending, the event trigger is lost.
The figure below shows an example where beat transfers are enabled by internal events.
Figure 22-12. Burst Event Trigger Action


  Peripheral Trigger
                                         Trigger Lost

              Event


       PENDCHn


       BUSYCHn


                                    Block Transfer                          Block Transfer
      Data Transfer                     BURST           BURST     BURST         BURST        BURST             BURST




Conditional Transfer on Strobe
The event input is used to trigger a transfer on peripherals with pending transfer requests. This event
action is intended to be used with peripheral triggers, e.g., for timed communication protocols or periodic
transfers between peripherals: only when the peripheral trigger coincides with the occurrence of a
(possibly cyclic) event the transfer is issued.
The event is acknowledged as soon as the event is received. The peripheral trigger request is stored
internally when the previous trigger action is completed (i.e., the channel is not pending) and when an
active event is received. If the peripheral trigger is active, the DMA will wait for an event before the
peripheral trigger is internally registered. When both event and peripheral transfer trigger are active, both
CHSTATUS.PEND and PENDCH.PENDCHn are set. A software trigger will now trigger a transfer.
The figure below shows an example where the peripheral beat transfer is started by a conditional strobe
event action.
Figure 22-13. Periodic Event with Burst Peripheral Triggers
                                           Trigger Lost                         Trigger Lost

                            Event


             Peripheral Trigger


                       PENDCHn


                                              Block Transfer
                  Data Transfer                                                                      BURST




© 2019 Microchip Technology Inc.                                Datasheet                             DS60001507E-page 391
                                                                  SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

Conditional Transfer
The event input is used to trigger a conditional transfer on peripherals with pending transfer requests. As
example, this type of event can be used for peripheral-to-peripheral transfers, where one peripheral is the
source of event and the second peripheral is the source of the trigger.
Each peripheral trigger is stored internally when the event is received. When the peripheral trigger is
stored internally, the Channel Pending status bit is set (CHSTATUS.PEND), the respective Pending
Channel n Bit in the Pending Channels register is set (PENDCH.PENDCHn), and the event is
acknowledged. A software trigger will now trigger a transfer.
The figure below shows an example where conditional event is enabled with peripheral beat trigger
requests.
Figure 22-14. Conditional Event with Burst Peripheral Triggers

                                   Event


                       Peripheral Trigger


                            PENDCHn



                             Data Transfer       Block Transfer
                                                                           BURST                    BURST




Conditional Block Transfer
The event input is used to trigger a conditional block transfer on peripherals.
Before starting transfers within a block, an event must be received. When received, the event is
acknowledged when the block transfer is completed. A software trigger will trigger a transfer.
The figure below shows an example where conditional event block transfer is started with peripheral beat
trigger requests.
Figure 22-15. Conditional Block Transfer with Burst Peripheral Triggers
              Event


  Peripheral Trigger


       PENDCHn


                               Block Transfer                                      Block Transfer
      Data Transfer                             BURST              BURST               BURST                   BURST




Channel Suspend
The event input is used to suspend an ongoing channel operation. The event is acknowledged when the
current AHB access is completed. For further details on Channel Suspend, refer to 22.6.3.3 Channel
Suspend.




© 2019 Microchip Technology Inc.                                  Datasheet                         DS60001507E-page 392
                                                          SAM D5x/E5x Family Data Sheet
                                                             DMAC – Direct Memory Access Controller

        Channel Resume
        The event input is used to resume a suspended channel operation. The event is acknowledged as soon
        as the event is received and the Channel Suspend Interrupt Flag (CHINTFLAG.SUSP) is cleared. For
        further details refer to 22.6.3.3 Channel Suspend.

        Skip Next Block Suspend
        This event can be used to skip the next block suspend action. If the channel is suspended before the
        event rises, the channel operation is resumed and the event is acknowledged. If the event rises before a
        suspend block action is detected, the event is kept until the next block suspend detection. When the block
        transfer is completed, the channel continues the operation (not suspended) and the event is
        acknowledged.

        Increase priority
        This event can be used to increase a channel priority and to request higher quality of service (QOS),
        when critical transfers must be done. When the event is detected, the channel will have the highest
        priority and the output Quality of Service value is internally forced to the maximum value. The event is
        acknowledged when the trigger action execution is completed. When acknowledged, the channel will
        recover its initial priority level and quality of service settings.

22.6.3.6 Event Output Selection
        The event output selections are available only for channels supporting event outputs.
        The Channel Event Output Enable can be set in the corresponding Channel n Event Control register
        (CHEVCTRL.EVOE). The Event Output Mode bits in Channel n Event Control register
        (CHEVCTRL.EVOMODE) selects the event type the channel should generate.
        The transfer events (CHEVCTRL.EVOMODE = DEFAULT) are strobe events and their duration is one
        CLK_DMAC_AHB clock period. The transfer event type selection is available in each Descriptor Block
        Control location (BTCTRL.EVOSEL). Block or burst event output generation is supported.
        The trigger action event (CHEVCTRL.EVOMODE = TRIGACT) is a level, active while the trigger action
        execution is not completed.

        Block event output
        When the block event output is selected, an event strobe is generated when the block transfer is
        completed. The pulse width of a block event output from a channel is one AHB clock cycle. It is also
        possible to use this event type to generate an event when the transaction is complete. For this type of
        application, the block event selection must be set in the last transfer descriptor only, as shown below.
        Figure 22-16. Block Event Output Generation
                                       Block Transfer                   Block Transfer
                    Data Transfer          BURST         BURST              BURST             BURST




                    Event Output



        Burst event output
        When the burst event output is selected, an event strobe is generated when each burst transfer within the
        corresponding block is completed. The pulse width of a burst event output from a channel is one AHB
        clock cycle. The figure below shows an example where the burst event output is set in the second
        descriptor of a linked list.




        © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 393
                                                                     SAM D5x/E5x Family Data Sheet
                                                                        DMAC – Direct Memory Access Controller

         Figure 22-17. Burst Event Output Generation
                                       Block Transfer                                   Block Transfer
                    Data Transfer          BURST                    BURST                     BURST                  BURST




                    Event Output



         Trigger action event output
         When the trigger action event output is selected, an event level is generated. Then event output is set
         when the transfer trigger occurred, and cleared when the corresponding trigger action is completed. The
         figure below shows an example for each trigger action type.
         Figure 22-18. Trigger Action Event Output Generation
                 Burst Trigger Action Event Output

                  Transfer Trigger

                                           Block Transfer

                                               BURST                   BURST                         BURST
                    Data Transfer


                     Event Output


                 Block Trigger Action Event Output

                  Transfer Trigger

                                           Block Transfer                            Block Transfer

                                               BURST        BURST                            BURST           BURST
                    Data Transfer


                     Event Output



                 Transaction Trigger Action Event Output

                  Transfer Trigger

                                           Block Transfer                   Block Transfer

                                               BURST        BURST               BURST           BURST
                    Data Transfer


                     Event Output


22.6.3.7 Aborting Transfers
         Transfers on any channel can be aborted gracefully by software by disabling the corresponding DMA
         channel. It is also possible to abort all ongoing or pending transfers by disabling the DMAC.
         When a DMA channel disable request or DMAC disable request is detected:
          • Ongoing transfers of the active channel will be disabled when the ongoing beat transfer is completed
            and the write-back memory section is updated. This prevents transfer corruption before the channel
            is disabled.
          • All other enabled channels will be disabled in the next clock cycle.




        © 2019 Microchip Technology Inc.                              Datasheet                                       DS60001507E-page 394
                                                              SAM D5x/E5x Family Data Sheet
                                                                 DMAC – Direct Memory Access Controller

        The corresponding Channel Enable bit in the Channel Control A register is cleared
        (CHCTRLA.ENABLE=0) when the channel is disabled.
        The corresponding DMAC Enable bit in the Control register is cleared (CTRL.DMAENABLE=0) when the
        entire DMAC module is disabled.
22.6.3.8 CRC Operation
        A Cyclic Redundancy Check (CRC) is an error detection technique used to find errors in data. It is
        commonly used to determine whether the data during a transmission, or data present in data and
        program memories has been corrupted or not. A CRC takes a data stream or a block of data as input and
        generates a 16- or 32-bit output that can be appended to the data and used as a checksum.
        When the data is received, the device or application repeats the calculation: If the new CRC result does
        not match the one calculated earlier, the block contains a data error. The application will then detect this
        and may take a corrective action, such as requesting the data to be sent again or simply not using the
        incorrect data.
        The CRC engine in DMAC supports two commonly used CRC polynomials: CRC-16 (CRC-CCITT) and
        CRC-32 (IEEE 802.3). Typically, applying CRC-n (CRC-16 or CRC-32) to a data block of arbitrary length
        will detect any single alteration that is ≤n bits in length, and will detect the fraction 1-2-n of all longer error
        bursts.
         • CRC-16:
            – Polynomial: x16+ x12+ x5+ 1
            – Hex value: 0x1021
         • CRC-32:
            – Polynomial: x32+x26+ x23+ x22+x16+ x12+ x11+ x10+ x8+ x7+ x5+ x4+ x2+ x + 1
            – Hex value: 0x04C11DB7
        The data source for the CRC engine can either be one of the DMA channels or the APB bus interface,
        and must be selected by writing to the CRC Input Source bits in the CRC Control register
        (CRCCTRL.CRCSRC). The CRC engine then takes data input from the selected source and generates a
        checksum based on these data. The checksum is available in the CRC Checksum register
        (CRCCHKSUM). When CRC-32 polynomial is used, the final checksum read is bit reversed and
        complemented, as shown in Figure 22-19.
        The CRC polynomial is selected by writing to the CRC Polynomial Type bit in the CRC Control register
        (CRCCTRL.CRCPOLY), the default is CRC-16. The CRC engine operates on byte only. When the DMA is
        used as data source for the CRC engine, the DMA channel beat size setting will be used. When used
        with APB bus interface, the application must select the CRC Beat Size bit field of CRC Control register
        (CRCCTRL.CRCBEATSIZE). 8-, 16-, or 32-bit bus transfer access type is supported. The corresponding
        number of bytes will be written in the CRCDATAIN register and the CRC engine will operate on the input
        data in a byte by byte manner.




       © 2019 Microchip Technology Inc.                        Datasheet                              DS60001507E-page 395
                                                           SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

        Figure 22-19. CRC Generator Block Diagram
                                                                  DMAC
                                                                 Channels

                                          CRCDATAIN

                                          CRCCTRL



                                                    8      16         8        32


                                                        CRC-16              CRC-32


                                               crc32



                                                           CHECKSUM



                                                            bit-reverse +
                                                            complement


                                                            Checksum
                                                              read

        CRC on CRC-16 or CRC-32 calculations can be performed on data passing through any DMA
        DMA    channel. Once a DMA channel is selected as the source, the CRC engine will continuously
        data   generate the CRC on the data passing through the DMA channel. The checksum is available
               for readout once the DMA transaction is completed or aborted. A CRC can also be generated
               on SRAM, Flash, or I/O memory by passing these data through a DMA channel. If the latter is
               done, the destination register for the DMA data can be the data input (CRCDATAIN) register in
               the CRC engine.

        CRC using the I/O Before using the CRC engine with the I/O interface, the application must set the
        interface         CRC Beat Size bits in the CRC Control register (CRCCTRL.CRCBEATSIZE).
                          8/16/32-bit bus transfer type can be selected.

        CRC can be performed on any data by loading them into the CRC engine using the CPU and writing the
        data to the CRCDATAIN register. Using this method, an arbitrary number of bytes can be written to the
        register by the CPU, and CRC is done continuously for each byte. This means if a 32-bit data is written to
        the CRCDATAIN register the CRC engine takes four cycles to calculate the CRC. The CRC complete is
        signaled by a set CRCBUSY bit in the CRCSTATUS register. New data can be written only when
        CRCBUSY flag is not set.

22.6.3.9 Memory CRC Generation
        When enabled, it is possible to automatically calculate a memory block checksum. When the channel is
        enabled and the descriptor is fetched, the CRC Checksum register (CRCCHKSUM) is reloaded with the




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 396
                                                                               SAM D5x/E5x Family Data Sheet
                                                                                 DMAC – Direct Memory Access Controller

initial checksum value (CHKINIT) stored in the Block Transfer Destination Address register (DSTADDR).
The DMA read and calculate the checksum over the data from the source address.When the checksum
calculation is completed, the CRC value is stored in the CRC Checksum register (CRCCHKSUM), the
Transfer Complete interrupt flag is set (CHINTFLAGn.TCMPL) and optional interrupt is generated.
If linked descriptor is in the list (DESCADDR !=0), the DMA will fetch the next descriptor and CRC
calculation continues as described above. When the last list descriptor is executed, the channel is
automatically disabled.
In order to enable the memory CRC generation, the following actions must be performed:
  1.      The CRC module must be set to be used with a DMA channel (CRCCTRL.CRCSRC)
  2.      Reserve memory space addresses to configure a descriptor or a list of descriptors
  3.      Configure each descriptor:
           – Set the next descriptor address (DESCADDR)
           – Set the destination address with the initial checksum value (DSTADDR = CHKINIT) in the first
              descriptior in a list
           – Set the transfer source address (SRCADDR)
           – Set the block transfer count (BTCNT)
           – Set the memory CRC generation operation mode (CRCCTRL.CRCMODE = CRCGEN)
           – Enable optional interrupts
  4.      Enable the corresponding DMA channel (CHCTRLAn.ENABLE)
The figure below shows the CRC computation slots and descriptor configuration when single or linked-
descriptors transfers are enabled.
Figure 22-20. CRC Computation with Single Linked Transfers
                      List with Single Descriptor                                                List with Multiple Linked Descriptors

                                                              Source Memory                                                                       Source Memory



                          Transfer start address: ADDR1 - N      Data ‘ 0’                                Transfer start address: ADDR1 - N                      Data ‘ 0’
 Descriptor 0                                                    Data ‘ 1 ’      Descriptor 0                                                                    Data ‘ 1 ’
   0x0      BTCTRL                                                                 0x0      BTCTRL
           BTCNT = N                                                                       BTCNT = N
                                                                                                                                              CRC Computation




   0x2                                                                             0x2
          SRCADDR =                                                                        SRCADDR =
   0x4                                                                             0x4
            ADDR 1                                                                           ADDR 1
                                      Desc of this buffer                                                              Desc of this buffer
   0x8          CHKINIT                                                            0x8          CHKINIT

           DESCADDR=                                                                     DESCADDR = next
   0xc                                                                             0xc
           0x00000000                                                                         desc

                                                                 Data ‘ N-1’                                                                                     Data ‘ N-1’
                                                    ADDR1        outside                                                             ADDR1                       outside




                                                                                                          Transfer start address: ADDR2 - M                      Data ‘ N’
                                                                                 Descriptor n (last)                                                             Data ‘ N+ 1 ’
                                                                                   0x0       BTCTRL
                                                                                            BTCNT = M
                                                                                                                                              CRC Computation




                                                                                   0x2
                                                                                           SRCADDR =
                                                                                   0x4
                                                                                             ADDR 2
                                                                                                                       Desc of this buffer
                                                                                   0x8     DON’T CARE

                                                                                           DESCADDR=
                                                                                   0xc
                                                                                           0x00000000


 Notes :                                                                                                                                                         Data ‘ M-1’
 Figures assumes that STEPSIZE is 0 (X1)                                                                                             ADDR2                       outside
 T o ease understanding (buffer base address is SRCADDR minus BTCNT ‘items’).




© 2019 Microchip Technology Inc.                                                Datasheet                                                                       DS60001507E-page 397
                                                            SAM D5x/E5x Family Data Sheet
                                                               DMAC – Direct Memory Access Controller

22.6.3.10 Memory CRC Monitor
        When enabled, it is possible to continuously check a a memory block data integrity by calculating and
        checking the CRC checksum. The expected CRC checksum value must be located in the last memory
        block location, as shown in the table below:

         CRCCTRL.CRCPOLY CRCCTRL.CRCBEATSIZE Last Memory Block Byte                              CHECKSUM Result
                                             Locations Value (MSB
                                             Byte First)
         CRC-16                     Byte                        Expected CRC[7:0]                0x00000000
                                    Half-word                   Expected CRC[15:8]

                                    Word                        0x00
                                                                0x00
                                                                Expected CRC[7:0]
                                                                Expected CRC[15:8]

         CRC-32                     Byte                        Expected CRC[31:24]              CRC Magic Number
                                                                                                 (0x2144DF1C)
                                    Half-word                   Expected CRC[23:16]

                                    Word                        Expected CRC[15:8]
                                                                Expected CRC[7:0]

        When the channel is enabled and the descriptor is fetched, the CRC Checksum register (CRCCHKSUM)
        is reloaded with the initial checksum value (CHKINIT), stored in the DSTADDR location of the first
        descriptor. The DMA read and calculate the checksum over the entire data from the source
        address.When the checksum calculation is completed the DMA read the last beat from the memory, the
        calculated CRC value from the CRC Checksum register is compared to zero or CRC magic number,
        depending on CRC polynomial selection.
        If the CHECKSUM does not match the comparison value the DMA channel is disabled, and both and the
        CRC Error bit in the Channel n Status register (CHSTATUSn.CRCERR) and Transfer Error interrupt flag
        (CHINTFLAGn.TERR) are set. If enabled, the Transfer Error interrupt is generated.
        If the calculated checksum value matches the compare value, the Transfer Complete interrupt flag
        (CHINTFLAGn.TCMPL) is set, optional interrupt is generated and the DMA will perform the following
        actions, depending on the descriptor list settings:
         • If the list has only one descriptor, the DMA will re-fetch the descriptor
         • If the current descriptor is the last descriptor from the list, the DMA will fetch the first descriptor from
           the list
        When the fetch is completed, the DMA restarts the operations described above when new triggers are
        detected.
        In order to enable the memory CRC monitor, the following actions must be performed:
         1.   The CRC module must be set to be used with a DMA channel (CRCCTRL.CRCSRC)
         2.   Reserve memory space addresses to configure a descriptor or a list of descriptors
         3.   Configure each descriptor
               – Set the next descriptor address (DESCADDR)




       © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 398
                                                                                                           SAM D5x/E5x Family Data Sheet
                                                                                                            DMAC – Direct Memory Access Controller

                       – In the first list descriptor, set the destination address with the initial checksum value
                         (DSTADDR = CHKINIT)
                       – Set the transfer source address (SRCADDR)
                       – Set the block transfer count (BTCNT)
                       – Set the memory CRC monitor operation mode (CRCCTRL.CRCMODE = CRCMON)
                       – Enable optional interrupts
           4.         Enable the corresponding DMA channel (CHCTRLAn.ENABLE)
         Figure 22-21. CRC Computation and Check with Single or Linked Transfers
                                 List with Single Descriptor                                                                 List with Multiple Linked Descriptors

                                                                                 Source Memory                                                                                  Source Memory



                                     Transfer start address: ADDR1 - N                      Data ‘ 0’                                 Transfer start address: ADDR1 - N                         Data ‘ 0’
            Descriptor 0                                                                    Data ‘ 1 ’       Descriptor 0                                                                       Data ‘ 1 ’
                0x0      BTCTRL                                                                                0x0        BTCTRL
                0x2     BTCNT = N                                                                              0x2       BTCNT = N
                                                                         CRC Computation




                                                                                                                                                                             CRC Computation
                       SRCADDR =                                                                                        SRCADDR =
                0x4                                                                                            0x4
                         ADDR 1                                                                                           ADDR 1
                                                 Desc of this buffer                                                                               Desc of this buffer
                0x8        CHKINIT                                                                             0x8          CHKINIT

                        DESCADDR=                                                                                       DESCADDR
                0xc                                                                                            0xc
                        0x00000000                                                                                   = next desc address
                                                                                            Data ‘ N-2 ’
                                                                                           Expected CRC                                                                                         Data ‘ N-1’
                                                               ADDR1                        outside                                                              ADDR1                          outside




                                                                                                                                      Transfer start address: ADDR2 - M                         Data ‘ N’
                                                                                                             Descriptor n (last)                                                                Data ‘ N+ 1 ’
                                                                                                               0x0       BTCTRL
                                                                                                               0x2      BTCNT = M




                                                                                                                                                                          CRC Computation
                                                                                                                        SRCADDR =
                                                                                                               0x4
                                                                                                                          ADDR 2
                                                                                                                                                   Desc of this buffer
                                                                                                               0x8      DON’T CARE

                                                                                                                        DESCADDR=
                                                                                                               0xc
                                                                                                                        0x00000000
                                                                                                                                                                                                Data ‘ M-2 ’
            Notes :                                                                                                                                                                            Expected CRC
            Figures assumes that STEPSIZE is 0 (X1).                                                                                                             ADDR2                          outside
            T o ease understanding, buffer base address is SRCADDR minus BTCNT ‘items’.



22.6.4   DMA Operation
         Not applicable.

22.6.5   Interrupts
         The DMAC channels have the following interrupt sources:
           • Transfer Complete (TCMPL): Indicates that a block transfer is completed on the corresponding
             channel. Refer to 22.6.2.5 Data Transmission for details.
           • Transfer Error (TERR): Indicates that a bus error has occurred during a burst transfer, or that an
             invalid descriptor has been fetched. Refer to 22.6.2.9 Error Handling for details.
           • Channel Suspend (SUSP): Indicates that the corresponding channel has been suspended. Refer to
             22.6.3.3 Channel Suspend and 22.6.2.5 Data Transmission for details.
         Each interrupt source has an Interrupt flag associated with it. The Interrupt flag in the Channel Interrupt
         Flag Status and Clear (CHINTFLAG) register is set when the Interrupt condition occurs. Each interrupt
         can be individually enabled by setting the corresponding bit in the Channel Interrupt Enable Set register
         (CHINTENSET=1), and disabled by setting the corresponding bit in the Channel Interrupt Enable Clear
         register (CHINTENCLR=1).




         © 2019 Microchip Technology Inc.                                                                  Datasheet                                                                        DS60001507E-page 399
                                                            SAM D5x/E5x Family Data Sheet
                                                               DMAC – Direct Memory Access Controller

         An interrupt request is generated when the Interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the Interrupt flag is cleared, the interrupt is disabled, the DMAC
         is reset or the corresponding DMA channel is reset. See CHINTFLAG for details on how to clear Interrupt
         flags. All interrupt requests are ORed together on system level to generate one combined interrupt
         request to the NVIC.
         The user must read the Channel Interrupt Status (INTSTATUS) register to identify the channels with
         pending interrupts and must read the Channel Interrupt Flag Status and Clear (CHINTFLAG) register to
         determine which Interrupt condition is present for the corresponding channel. It is also possible to read
         the Interrupt Pending register (INTPEND), which provides the lowest channel number with pending
         interrupt and the respective Interrupt flags.
         Note: Interrupts must be globally enabled for interrupt requests to be generated.

22.6.6   Events
         The DMAC can generate the following output events:
           • Channel (CH): Generated when a block transfer for a given channel has been completed, or when a
             beat transfer within a block transfer for a given channel has been completed. Refer to Event Output
             Selection for details.
         Setting the Channel Event Output Enable bit (CHEVCTRLx.EVOE = 1) enables the corresponding output
         event configured in the Event Output Selection bit group in the Block Transfer Control register
         (BTCTRL.EVOSEL). Clearing CHEVCTRLx.EVOE = 0 disables the corresponding output event.
         The DMAC can take the following actions on an input event:
           • Transfer and Periodic Transfer Trigger (TRIG): normal transfer or periodic transfers on peripherals
             are enabled
           • Conditional Transfer Trigger (CTRIG): conditional transfers on peripherals are enabled
           • Conditional Block Transfer Trigger (CBLOCK): conditional block transfers on peripherals are enabled
           • Channel Suspend Operation (SUSPEND): suspend a channel operation
           • Channel Resume Operation (RESUME): resume a suspended channel operation
           • Skip Next Block Suspend Action (SSKIP): skip the next block suspend transfer condition
           • Increase Priority (INCPRI): increase channel priority
         Setting the Channel Event Input Enable bit (CHEVCTRLx.EVIE = 1) enables the corresponding action on
         input event. Clearing this bit disables the corresponding action on input event. Note that several actions
         can be enabled for incoming events. If several events are connected to the peripheral, any enabled action
         will be taken for any of the incoming events. For further details on event input actions, refer to Event Input
         Actions.
         Note: Event input and outputs are not available for every channel. Refer to the Features section for
         more information.
         Related Links
         31. EVSYS – Event System
         22.6.3.6 Event Output Selection
         22.6.3.5 Event Input Actions

22.6.7   Sleep Mode Operation




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 400
                                            SAM D5x/E5x Family Data Sheet
                                             DMAC – Direct Memory Access Controller

22.6.8   Synchronization
         Not applicable.




         © 2019 Microchip Technology Inc.   Datasheet               DS60001507E-page 401
                                                                     SAM D5x/E5x Family Data Sheet
                                                                        DMAC – Direct Memory Access Controller


22.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0                                                                                 DMAENABLE   SWRST
 0x00          CTRL
                             15:8                                                     LVLEN3         LVLEN2        LVLEN1     LVLEN0
                              7:0                                                            CRCPOLY[1:0]           CRCBEATSIZE[1:0]
 0x02        CRCCTRL
                             15:8        CRCMODE[1:0]                                        CRCSRC[5:0]
                              7:0                                           CRCDATAIN[7:0]
                             15:8                                           CRCDATAIN[15:8]
 0x04       CRCDATAIN
                             23:16                                         CRCDATAIN[23:16]
                             31:24                                         CRCDATAIN[31:24]
                              7:0                                           CRCCHKSUM[7:0]
                             15:8                                          CRCCHKSUM[15:8]
 0x08      CRCCHKSUM
                             23:16                                         CRCCHKSUM[23:16]
                             31:24                                         CRCCHKSUM[31:24]
 0x0C       CRCSTATUS         7:0                                                                    CRCERR       CRCZERO     CRCBUSY
 0x0D        DBGCTRL          7:0                                                                                             DBGRUN
 0x0E
   ...       Reserved
 0x0F
                              7:0                                             SWTRIG[7:0]
                             15:8                                            SWTRIG[15:8]
 0x10      SWTRIGCTRL
                             23:16                                           SWTRIG[23:16]
                             31:24                                           SWTRIG[31:24]
                              7:0     RRLVLEN0          QOS00[1:0]                                 LVLPRI0[4:0]
                             15:8     RRLVLEN1          QOS01[1:0]                                 LVLPRI1[4:0]
 0x14        PRICTRL0
                             23:16    RRLVLEN2          QOS02[1:0]                                 LVLPRI2[4:0]
                             31:24    RRLVLEN3          QOS03[1:0]                                 LVLPRI3[4:0]
 0x18
   ...       Reserved
 0x1F
                              7:0                                                                     ID[4:0]
 0x20        INTPEND
                             15:8      PEND       BUSY          FERR      CRCERR                      SUSP          TCMPL      TERR
 0x22
   ...       Reserved
 0x23
                              7:0                                              CHINT[7:0]
                             15:8                                             CHINT[15:8]
 0x24       INTSTATUS
                             23:16                                            CHINT[23:16]
                             31:24                                            CHINT[31:24]
                              7:0                                             BUSYCH[7:0]
                             15:8                                            BUSYCH[15:8]
 0x28         BUSYCH
                             23:16                                           BUSYCH[23:16]
                             31:24                                           BUSYCH[31:24]




          © 2019 Microchip Technology Inc.                             Datasheet                                  DS60001507E-page 402
                                                                      SAM D5x/E5x Family Data Sheet
                                                                            DMAC – Direct Memory Access Controller

...........continued

  Offset               Name     Bit Pos.

                                  7:0      PENDCH7    PENDCH6    PENDCH5     PENDCH4       PENDCH3    PENDCH2    PENDCH1        PENDCH0
                                 15:8      PENDCH15   PENDCH14   PENDCH13    PENDCH12      PENDCH11   PENDCH10   PENDCH9        PENDCH8
   0x2C            PENDCH
                                 23:16     PENDCH23   PENDCH22   PENDCH21    PENDCH20      PENDCH19   PENDCH18   PENDCH17      PENDCH16
                                 31:24     PENDCH31   PENDCH30   PENDCH29    PENDCH28      PENDCH27   PENDCH26   PENDCH25      PENDCH24
                                  7:0                                                       LVLEX3     LVLEX2     LVLEX1         LVLEX0
                                 15:8       ABUSY                                                      ID[4:0]
   0x30                ACTIVE
                                 23:16                                               BTCNT[7:0]
                                 31:24                                              BTCNT[15:8]
                                  7:0                                           BASEADDR[7:0]
                                 15:8                                          BASEADDR[15:8]
   0x34           BASEADDR
                                 23:16                                         BASEADDR[23:16]
                                 31:24                                         BASEADDR[31:24]
                                  7:0                                           WRBADDR[7:0]
                                 15:8                                           WRBADDR[15:8]
   0x38           WRBADDR
                                 23:16                                         WRBADDR[23:16]
                                 31:24                                         WRBADDR[31:24]
   0x3C
     ...           Reserved
   0x3F
                                  7:0                 RUNSTDBY                                                    ENABLE         SWRST
                                 15:8                                               TRIGSRC[7:0]
   0x40           CHCTRLA0
                                 23:16                               TRIGACT[1:0]
                                 31:24                             THRESHOLD[1:0]                        BURSTLEN[3:0]
   0x44           CHCTRLB0        7:0                                                                                     CMD[1:0]
   0x45           CHPRILVL0       7:0                                                                                    PRILVL[1:0]
   0x46          CHEVCTRL0        7:0       EVOE        EVIE        EVOMODE[1:0]                                 EVACT[2:0]
   0x47
     ...           Reserved
   0x4B
   0x4C         CHINTENCLR0       7:0                                                                  SUSP       TCMPL           TERR
   0x4D         CHINTENSET0       7:0                                                                  SUSP       TCMPL           TERR
   0x4E          CHINTFLAG0       7:0                                                                  SUSP       TCMPL           TERR
   0x4F          CHSTATUS0        7:0                                                       CRCERR     FERR        BUSY           PEND
                                  7:0                 RUNSTDBY                                                    ENABLE         SWRST
                                 15:8                                               TRIGSRC[7:0]
   0x50           CHCTRLA1
                                 23:16                               TRIGACT[1:0]
                                 31:24                             THRESHOLD[1:0]                        BURSTLEN[3:0]
   0x54           CHCTRLB1        7:0                                                                                     CMD[1:0]
   0x55           CHPRILVL1       7:0                                                                                    PRILVL[1:0]
   0x56          CHEVCTRL1        7:0       EVOE        EVIE        EVOMODE[1:0]                                 EVACT[2:0]
   0x57
     ...           Reserved
   0x5B
   0x5C         CHINTENCLR1       7:0                                                                  SUSP       TCMPL           TERR
   0x5D         CHINTENSET1       7:0                                                                  SUSP       TCMPL           TERR




              © 2019 Microchip Technology Inc.                          Datasheet                                DS60001507E-page 403
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

   0x5E          CHINTFLAG1       7:0                                                         SUSP      TCMPL           TERR
   0x5F          CHSTATUS1        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0x60           CHCTRLA2
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0x64           CHCTRLB2        7:0                                                                           CMD[1:0]
   0x65           CHPRILVL2       7:0                                                                          PRILVL[1:0]
   0x66          CHEVCTRL2        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0x67
     ...           Reserved
   0x6B
   0x6C         CHINTENCLR2       7:0                                                         SUSP      TCMPL           TERR
   0x6D         CHINTENSET2       7:0                                                         SUSP      TCMPL           TERR
   0x6E          CHINTFLAG2       7:0                                                         SUSP      TCMPL           TERR
   0x6F          CHSTATUS2        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0x70           CHCTRLA3
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0x74           CHCTRLB3        7:0                                                                           CMD[1:0]
   0x75           CHPRILVL3       7:0                                                                          PRILVL[1:0]
   0x76          CHEVCTRL3        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0x77
     ...           Reserved
   0x7B
   0x7C         CHINTENCLR3       7:0                                                         SUSP      TCMPL           TERR
   0x7D         CHINTENSET3       7:0                                                         SUSP      TCMPL           TERR
   0x7E          CHINTFLAG3       7:0                                                         SUSP      TCMPL           TERR
   0x7F          CHSTATUS3        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0x80           CHCTRLA4
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0x84           CHCTRLB4        7:0                                                                           CMD[1:0]
   0x85           CHPRILVL4       7:0                                                                          PRILVL[1:0]
   0x86          CHEVCTRL4        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0x87
     ...           Reserved
   0x8B
   0x8C         CHINTENCLR4       7:0                                                         SUSP      TCMPL           TERR
   0x8D         CHINTENSET4       7:0                                                         SUSP      TCMPL           TERR
   0x8E          CHINTFLAG4       7:0                                                         SUSP      TCMPL           TERR
   0x8F          CHSTATUS4        7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 404
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0x90           CHCTRLA5
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0x94           CHCTRLB5        7:0                                                                           CMD[1:0]
   0x95           CHPRILVL5       7:0                                                                          PRILVL[1:0]
   0x96          CHEVCTRL5        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0x97
     ...           Reserved
   0x9B
   0x9C         CHINTENCLR5       7:0                                                         SUSP      TCMPL           TERR
   0x9D         CHINTENSET5       7:0                                                         SUSP      TCMPL           TERR
   0x9E          CHINTFLAG5       7:0                                                         SUSP      TCMPL           TERR
   0x9F          CHSTATUS5        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0xA0           CHCTRLA6
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0xA4           CHCTRLB6        7:0                                                                           CMD[1:0]
   0xA5           CHPRILVL6       7:0                                                                          PRILVL[1:0]
   0xA6          CHEVCTRL6        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0xA7
     ...           Reserved
   0xAB
   0xAC         CHINTENCLR6       7:0                                                         SUSP      TCMPL           TERR
   0xAD         CHINTENSET6       7:0                                                         SUSP      TCMPL           TERR
   0xAE          CHINTFLAG6       7:0                                                         SUSP      TCMPL           TERR
   0xAF          CHSTATUS6        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0xB0           CHCTRLA7
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0xB4           CHCTRLB7        7:0                                                                           CMD[1:0]
   0xB5           CHPRILVL7       7:0                                                                          PRILVL[1:0]
   0xB6          CHEVCTRL7        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0xB7
     ...           Reserved
   0xBB
   0xBC         CHINTENCLR7       7:0                                                         SUSP      TCMPL           TERR
   0xBD         CHINTENSET7       7:0                                                         SUSP      TCMPL           TERR
   0xBE          CHINTFLAG7       7:0                                                         SUSP      TCMPL           TERR
   0xBF          CHSTATUS7        7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 405
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0xC0           CHCTRLA8
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0xC4           CHCTRLB8        7:0                                                                           CMD[1:0]
   0xC5           CHPRILVL8       7:0                                                                          PRILVL[1:0]
   0xC6          CHEVCTRL8        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0xC7
     ...           Reserved
   0xCB
   0xCC         CHINTENCLR8       7:0                                                         SUSP      TCMPL           TERR
   0xCD         CHINTENSET8       7:0                                                         SUSP      TCMPL           TERR
   0xCE          CHINTFLAG8       7:0                                                         SUSP      TCMPL           TERR
   0xCF          CHSTATUS8        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0xD0           CHCTRLA9
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0xD4           CHCTRLB9        7:0                                                                           CMD[1:0]
   0xD5           CHPRILVL9       7:0                                                                          PRILVL[1:0]
   0xD6          CHEVCTRL9        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0xD7
     ...           Reserved
   0xDB
   0xDC         CHINTENCLR9       7:0                                                         SUSP      TCMPL           TERR
   0xDD         CHINTENSET9       7:0                                                         SUSP      TCMPL           TERR
   0xDE          CHINTFLAG9       7:0                                                         SUSP      TCMPL           TERR
   0xDF          CHSTATUS9        7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0xE0          CHCTRLA10
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0xE4          CHCTRLB10        7:0                                                                           CMD[1:0]
   0xE5          CHPRILVL10       7:0                                                                          PRILVL[1:0]
   0xE6         CHEVCTRL10        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0xE7
     ...           Reserved
   0xEB
   0xEC        CHINTENCLR10       7:0                                                         SUSP      TCMPL           TERR
   0xED        CHINTENSET10       7:0                                                         SUSP      TCMPL           TERR
   0xEE         CHINTFLAG10       7:0                                                         SUSP      TCMPL           TERR
   0xEF          CHSTATUS10       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 406
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
   0xF0          CHCTRLA11
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
   0xF4          CHCTRLB11        7:0                                                                           CMD[1:0]
   0xF5          CHPRILVL11       7:0                                                                          PRILVL[1:0]
   0xF6          CHEVCTRL11       7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
   0xF7
     ...           Reserved
   0xFB
   0xFC        CHINTENCLR11       7:0                                                         SUSP      TCMPL           TERR
   0xFD        CHINTENSET11       7:0                                                         SUSP      TCMPL           TERR
   0xFE         CHINTFLAG11       7:0                                                         SUSP      TCMPL           TERR
   0xFF          CHSTATUS11       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0100         CHCTRLA12
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0104         CHCTRLB12        7:0                                                                           CMD[1:0]
  0x0105         CHPRILVL12       7:0                                                                          PRILVL[1:0]
  0x0106        CHEVCTRL12        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0107
     ...           Reserved
  0x010B
  0x010C       CHINTENCLR12       7:0                                                         SUSP      TCMPL           TERR
  0x010D       CHINTENSET12       7:0                                                         SUSP      TCMPL           TERR
  0x010E        CHINTFLAG12       7:0                                                         SUSP      TCMPL           TERR
  0x010F         CHSTATUS12       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0110         CHCTRLA13
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0114         CHCTRLB13        7:0                                                                           CMD[1:0]
  0x0115         CHPRILVL13       7:0                                                                          PRILVL[1:0]
  0x0116        CHEVCTRL13        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0117
     ...           Reserved
  0x011B
  0x011C       CHINTENCLR13       7:0                                                         SUSP      TCMPL           TERR
  0x011D       CHINTENSET13       7:0                                                         SUSP      TCMPL           TERR
  0x011E        CHINTFLAG13       7:0                                                         SUSP      TCMPL           TERR
  0x011F         CHSTATUS13       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 407
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0120         CHCTRLA14
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0124         CHCTRLB14        7:0                                                                           CMD[1:0]
  0x0125         CHPRILVL14       7:0                                                                          PRILVL[1:0]
  0x0126        CHEVCTRL14        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0127
     ...           Reserved
  0x012B
  0x012C       CHINTENCLR14       7:0                                                         SUSP      TCMPL           TERR
  0x012D       CHINTENSET14       7:0                                                         SUSP      TCMPL           TERR
  0x012E        CHINTFLAG14       7:0                                                         SUSP      TCMPL           TERR
  0x012F         CHSTATUS14       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0130         CHCTRLA15
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0134         CHCTRLB15        7:0                                                                           CMD[1:0]
  0x0135         CHPRILVL15       7:0                                                                          PRILVL[1:0]
  0x0136        CHEVCTRL15        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0137
     ...           Reserved
  0x013B
  0x013C       CHINTENCLR15       7:0                                                         SUSP      TCMPL           TERR
  0x013D       CHINTENSET15       7:0                                                         SUSP      TCMPL           TERR
  0x013E        CHINTFLAG15       7:0                                                         SUSP      TCMPL           TERR
  0x013F         CHSTATUS15       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0140         CHCTRLA16
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0144         CHCTRLB16        7:0                                                                           CMD[1:0]
  0x0145         CHPRILVL16       7:0                                                                          PRILVL[1:0]
  0x0146        CHEVCTRL16        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0147
     ...           Reserved
  0x014B
  0x014C       CHINTENCLR16       7:0                                                         SUSP      TCMPL           TERR
  0x014D       CHINTENSET16       7:0                                                         SUSP      TCMPL           TERR
  0x014E        CHINTFLAG16       7:0                                                         SUSP      TCMPL           TERR
  0x014F         CHSTATUS16       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 408
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0150         CHCTRLA17
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0154         CHCTRLB17        7:0                                                                           CMD[1:0]
  0x0155         CHPRILVL17       7:0                                                                          PRILVL[1:0]
  0x0156        CHEVCTRL17        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0157
     ...           Reserved
  0x015B
  0x015C       CHINTENCLR17       7:0                                                         SUSP      TCMPL           TERR
  0x015D       CHINTENSET17       7:0                                                         SUSP      TCMPL           TERR
  0x015E        CHINTFLAG17       7:0                                                         SUSP      TCMPL           TERR
  0x015F         CHSTATUS17       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0160         CHCTRLA18
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0164         CHCTRLB18        7:0                                                                           CMD[1:0]
  0x0165         CHPRILVL18       7:0                                                                          PRILVL[1:0]
  0x0166        CHEVCTRL18        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0167
     ...           Reserved
  0x016B
  0x016C       CHINTENCLR18       7:0                                                         SUSP      TCMPL           TERR
  0x016D       CHINTENSET18       7:0                                                         SUSP      TCMPL           TERR
  0x016E        CHINTFLAG18       7:0                                                         SUSP      TCMPL           TERR
  0x016F         CHSTATUS18       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0170         CHCTRLA19
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0174         CHCTRLB19        7:0                                                                           CMD[1:0]
  0x0175         CHPRILVL19       7:0                                                                          PRILVL[1:0]
  0x0176        CHEVCTRL19        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0177
     ...           Reserved
  0x017B
  0x017C       CHINTENCLR19       7:0                                                         SUSP      TCMPL           TERR
  0x017D       CHINTENSET19       7:0                                                         SUSP      TCMPL           TERR
  0x017E        CHINTFLAG19       7:0                                                         SUSP      TCMPL           TERR
  0x017F         CHSTATUS19       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 409
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0180         CHCTRLA20
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0184         CHCTRLB20        7:0                                                                           CMD[1:0]
  0x0185         CHPRILVL20       7:0                                                                          PRILVL[1:0]
  0x0186        CHEVCTRL20        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0187
     ...           Reserved
  0x018B
  0x018C       CHINTENCLR20       7:0                                                         SUSP      TCMPL           TERR
  0x018D       CHINTENSET20       7:0                                                         SUSP      TCMPL           TERR
  0x018E        CHINTFLAG20       7:0                                                         SUSP      TCMPL           TERR
  0x018F         CHSTATUS20       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0190         CHCTRLA21
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0194         CHCTRLB21        7:0                                                                           CMD[1:0]
  0x0195         CHPRILVL21       7:0                                                                          PRILVL[1:0]
  0x0196        CHEVCTRL21        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0197
     ...           Reserved
  0x019B
  0x019C       CHINTENCLR21       7:0                                                         SUSP      TCMPL           TERR
  0x019D       CHINTENSET21       7:0                                                         SUSP      TCMPL           TERR
  0x019E        CHINTFLAG21       7:0                                                         SUSP      TCMPL           TERR
  0x019F         CHSTATUS21       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x01A0         CHCTRLA22
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x01A4         CHCTRLB22        7:0                                                                           CMD[1:0]
  0x01A5         CHPRILVL22       7:0                                                                          PRILVL[1:0]
  0x01A6        CHEVCTRL22        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x01A7
     ...           Reserved
  0x01AB
  0x01AC       CHINTENCLR22       7:0                                                         SUSP      TCMPL           TERR
  0x01AD       CHINTENSET22       7:0                                                         SUSP      TCMPL           TERR
  0x01AE        CHINTFLAG22       7:0                                                         SUSP      TCMPL           TERR
  0x01AF         CHSTATUS22       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 410
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x01B0         CHCTRLA23
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x01B4         CHCTRLB23        7:0                                                                           CMD[1:0]
  0x01B5         CHPRILVL23       7:0                                                                          PRILVL[1:0]
  0x01B6        CHEVCTRL23        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x01B7
     ...           Reserved
  0x01BB
  0x01BC       CHINTENCLR23       7:0                                                         SUSP      TCMPL           TERR
  0x01BD       CHINTENSET23       7:0                                                         SUSP      TCMPL           TERR
  0x01BE        CHINTFLAG23       7:0                                                         SUSP      TCMPL           TERR
  0x01BF         CHSTATUS23       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x01C0         CHCTRLA24
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x01C4         CHCTRLB24        7:0                                                                           CMD[1:0]
  0x01C5         CHPRILVL24       7:0                                                                          PRILVL[1:0]
  0x01C6        CHEVCTRL24        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x01C7
     ...           Reserved
  0x01CB
  0x01CC       CHINTENCLR24       7:0                                                         SUSP      TCMPL           TERR
  0x01CD       CHINTENSET24       7:0                                                         SUSP      TCMPL           TERR
  0x01CE        CHINTFLAG24       7:0                                                         SUSP      TCMPL           TERR
  0x01CF         CHSTATUS24       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x01D0         CHCTRLA25
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x01D4         CHCTRLB25        7:0                                                                           CMD[1:0]
  0x01D5         CHPRILVL25       7:0                                                                          PRILVL[1:0]
  0x01D6        CHEVCTRL25        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x01D7
     ...           Reserved
  0x01DB
  0x01DC       CHINTENCLR25       7:0                                                         SUSP      TCMPL           TERR
  0x01DD       CHINTENSET25       7:0                                                         SUSP      TCMPL           TERR
  0x01DE        CHINTFLAG25       7:0                                                         SUSP      TCMPL           TERR
  0x01DF         CHSTATUS25       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 411
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x01E0         CHCTRLA26
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x01E4         CHCTRLB26        7:0                                                                           CMD[1:0]
  0x01E5         CHPRILVL26       7:0                                                                          PRILVL[1:0]
  0x01E6        CHEVCTRL26        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x01E7
     ...           Reserved
  0x01EB
  0x01EC       CHINTENCLR26       7:0                                                         SUSP      TCMPL           TERR
  0x01ED       CHINTENSET26       7:0                                                         SUSP      TCMPL           TERR
  0x01EE        CHINTFLAG26       7:0                                                         SUSP      TCMPL           TERR
  0x01EF         CHSTATUS26       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x01F0         CHCTRLA27
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x01F4         CHCTRLB27        7:0                                                                           CMD[1:0]
  0x01F5         CHPRILVL27       7:0                                                                          PRILVL[1:0]
  0x01F6        CHEVCTRL27        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x01F7
     ...           Reserved
  0x01FB
  0x01FC       CHINTENCLR27       7:0                                                         SUSP      TCMPL           TERR
  0x01FD       CHINTENSET27       7:0                                                         SUSP      TCMPL           TERR
  0x01FE        CHINTFLAG27       7:0                                                         SUSP      TCMPL           TERR
  0x01FF         CHSTATUS27       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0200         CHCTRLA28
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0204         CHCTRLB28        7:0                                                                           CMD[1:0]
  0x0205         CHPRILVL28       7:0                                                                          PRILVL[1:0]
  0x0206        CHEVCTRL28        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0207
     ...           Reserved
  0x020B
  0x020C       CHINTENCLR28       7:0                                                         SUSP      TCMPL           TERR
  0x020D       CHINTENSET28       7:0                                                         SUSP      TCMPL           TERR
  0x020E        CHINTFLAG28       7:0                                                         SUSP      TCMPL           TERR
  0x020F         CHSTATUS28       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 412
                                                               SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

...........continued

  Offset               Name    Bit Pos.

                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0210         CHCTRLA29
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0214         CHCTRLB29        7:0                                                                           CMD[1:0]
  0x0215         CHPRILVL29       7:0                                                                          PRILVL[1:0]
  0x0216        CHEVCTRL29        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0217
     ...           Reserved
  0x021B
  0x021C       CHINTENCLR29       7:0                                                         SUSP      TCMPL           TERR
  0x021D       CHINTENSET29       7:0                                                         SUSP      TCMPL           TERR
  0x021E        CHINTFLAG29       7:0                                                         SUSP      TCMPL           TERR
  0x021F         CHSTATUS29       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0220         CHCTRLA30
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0224         CHCTRLB30        7:0                                                                           CMD[1:0]
  0x0225         CHPRILVL30       7:0                                                                          PRILVL[1:0]
  0x0226        CHEVCTRL30        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0227
     ...           Reserved
  0x022B
  0x022C       CHINTENCLR30       7:0                                                         SUSP      TCMPL           TERR
  0x022D       CHINTENSET30       7:0                                                         SUSP      TCMPL           TERR
  0x022E        CHINTFLAG30       7:0                                                         SUSP      TCMPL           TERR
  0x022F         CHSTATUS30       7:0                                                CRCERR   FERR      BUSY            PEND
                                  7:0             RUNSTDBY                                             ENABLE          SWRST
                                 15:8                                        TRIGSRC[7:0]
  0x0230         CHCTRLA31
                                 23:16                        TRIGACT[1:0]
                                 31:24                       THRESHOLD[1:0]                    BURSTLEN[3:0]
  0x0234         CHCTRLB31        7:0                                                                           CMD[1:0]
  0x0235         CHPRILVL31       7:0                                                                          PRILVL[1:0]
  0x0236        CHEVCTRL31        7:0      EVOE     EVIE     EVOMODE[1:0]                             EVACT[2:0]
  0x0237
     ...           Reserved
  0x023B
  0x023C       CHINTENCLR31       7:0                                                         SUSP      TCMPL           TERR
  0x023D       CHINTENSET31       7:0                                                         SUSP      TCMPL           TERR
  0x023E        CHINTFLAG31       7:0                                                         SUSP      TCMPL           TERR
  0x023F         CHSTATUS31       7:0                                                CRCERR   FERR      BUSY            PEND




              © 2019 Microchip Technology Inc.                   Datasheet                            DS60001507E-page 413
                                                         SAM D5x/E5x Family Data Sheet
                                                            DMAC – Direct Memory Access Controller


22.8   Register Description
       Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
       8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
       accessed directly.
       Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
       write protection is denoted by the "PAC Write-Protection" property in each individual register description.
       For details, refer to 22.5.8 Register Access Protection.
       Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
       Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




       © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 414
                                                                   SAM D5x/E5x Family Data Sheet
                                                                      DMAC – Direct Memory Access Controller

22.8.1         Control

               Name:        CTRL
               Offset:      0x00
               Reset:       0x0000
               Property:    PAC Write-Protection, Enable-Protected


         Bit        15            14            13            12            11            10            9             8
                                                                          LVLEN3       LVLEN2        LVLEN1        LVLEN0
   Access                                                                  R/W           R/W           R/W           R/W
    Reset                                                                    0            0             0             0


         Bit         7             6             5             4             3            2             1             0
                                                                                                   DMAENABLE       SWRST
   Access                                                                                              R/W           R/W
    Reset                                                                                               0             0


               Bits 8, 9, 10, 11 – LVLENx Priority Level x Enable
               When this bit is set, all requests with the corresponding level will be fed into the arbiter block. When
               cleared, all requests with the corresponding level will be ignored.
               For details on arbitration schemes, refer to the Arbitration section.
               These bits are not enable-protected.
                Value        Description
                0            Transfer requests for Priority level x will not be handled.
                1            Transfer requests for Priority level x will be handled.

               Bit 1 – DMAENABLE DMA Enable
               Setting this bit will enable the DMA module.
               Writing a '0' to this bit will disable the DMA module. When writing a '0' during an ongoing transfer, the bit
               will not be cleared until the internal data transfer buffer is empty and the DMA transfer is aborted. The
               internal data transfer buffer will be empty once the ongoing burst transfer is completed.
               This bit is not enable-protected.
                Value        Description
                0            The peripheral is disabled.
                1            The peripheral is enabled.

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit when both the DMAC and the CRC module are disabled (DMAENABLE and
               CRCENABLE are '0') resets all registers in the DMAC (except DBGCTRL) to their initial state. If either the
               DMAC or CRC module is enabled, the Reset request will be ignored and the DMAC will return an access
               error.
                Value        Description
                0            There is no Reset operation ongoing.
                1            A Reset operation is ongoing.




           © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 415
                                                                  SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

22.8.2         CRC Control

               Name:       CRCCTRL
               Offset:     0x02
               Reset:      0x0000
               Property:   PAC Write-Protection, Enable-Protected


         Bit        15            14           13           12            11             10          9             8
                     CRCMODE[1:0]                                              CRCSRC[5:0]
   Access          R/W           R/W          R/W           R/W          R/W             R/W        R/W          R/W
    Reset            0            0             0            0            0                  0       0             0


         Bit         7            6             5            4            3                  2       1             0
                                                                              CRCPOLY[1:0]          CRCBEATSIZE[1:0]
   Access                                                                R/W             R/W        R/W          R/W
    Reset                                                                 0                  0       0             0


               Bits 15:14 – CRCMODE[1:0] CRC Operating Mode
               These bits define the block transfer mode.
                Value      Name                 Description
                0x0        DEFAULT              Default operating mode
                0x1                             Reserved
                0x2        CRCMON               Memory CRC monitor operating mode
                0x3        CRCGEN               Memory CRC generation operating mode

               Bits 13:8 – CRCSRC[5:0] CRC Input Source
               These bits select the input source for generating the CRC. The selected source is locked until either the
               CRC generation is completed or the CRC module is disabled. This means the CRCSRC cannot be
               modified when the CRC operation is ongoing. The lock is signaled by the CRCBUSY status bit. CRC
               generation complete is generated and signaled from the selected source when used with the DMA
               channel.
                Value      Name                             Description
                0x00       NOACT                            No action
                0x01       IO                               I/O interface
                0x02 -                                      Reserved
                0x1F
                0x20       CH0                              DMA channel 0
                0x21       CH1                              DMA channel 1
                0x22       CH2                              DMA channel 2
                0x23       CH3                              DMA channel 3
                0x24       CH4                              DMA channel 4
                0x25       CH5                              DMA channel 5
                0x26       CH6                              DMA channel 6
                0x27       CH7                              DMA channel 7
                0x28       CH8                              DMA channel 8
                0x29       CH9                              DMA channel 9
                0x2A       CH10                             DMA channel 10
                0x2B       CH11                             DMA channel 11




           © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 416
                                                 SAM D5x/E5x Family Data Sheet
                                                    DMAC – Direct Memory Access Controller

 Value        Name                         Description
 0x2C         CH12                         DMA channel 12
 0x2D         CH13                         DMA channel 13
 0x2E         CH14                         DMA channel 14
 0x2F         CH15                         DMA channel 15
 0x30         CH16                         DMA channel 16
 0x31         CH17                         DMA channel 17
 0x32         CH18                         DMA channel 18
 0x33         CH19                         DMA channel 19
 0x34         CH20                         DMA channel 20
 0x35         CH21                         DMA channel 21
 0x36         CH22                         DMA channel 22
 0x37         CH23                         DMA channel 23
 0x38         CH24                         DMA channel 24
 0x39         CH25                         DMA channel 25
 0x3A         CH26                         DMA channel 26
 0x3B         CH27                         DMA channel 27
 0x3C         CH28                         DMA channel 28
 0x3D         CH29                         DMA channel 29
 0x3E         CH30                         DMA channel 30
 0x3F         CH31                         DMA channel 31

Bits 3:2 – CRCPOLY[1:0] CRC Polynomial Type
These bits select the CRC polynomial type.
 Value      Name                   Description
 0x0        CRC16                   CRC-16 (CRC-CCITT)
 0x1        CRC32                   CRC32 (IEEE 802.3)
 0x2-0x3                            Reserved

Bits 1:0 – CRCBEATSIZE[1:0] CRC Beat Size
These bits define the size of the data transfer for each bus access when the CRC is used with I/O
interface.
 Value      Name                              Description
 0x0        BYTE                              8-bit bus transfer
 0x1        HWORD                             16-bit bus transfer
 0x2        WORD                              32-bit bus transfer
 0x3                                          Reserved




© 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 417
                                                              SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

22.8.3         CRC Data Input

               Name:       CRCDATAIN
               Offset:     0x04
               Reset:      0x00000000
               Property:   PAC Write Protection


         Bit        31           30           29         28           27         26           25          24
                                                        CRCDATAIN[31:24]
   Access          R/W          R/W           R/W       R/W          R/W         R/W         R/W         R/W
    Reset           0             0            0         0            0           0           0           0


         Bit        23           22           21         20           19         18           17          16
                                                        CRCDATAIN[23:16]
   Access          R/W          R/W           R/W       R/W          R/W         R/W         R/W         R/W
    Reset           0             0            0         0            0           0           0           0


         Bit        15           14           13         12           11         10           9           8
                                                         CRCDATAIN[15:8]
   Access          R/W          R/W           R/W       R/W          R/W         R/W         R/W         R/W
    Reset           0             0            0         0            0           0           0           0


         Bit        7             6            5         4            3           2           1           0
                                                         CRCDATAIN[7:0]
   Access          R/W          R/W           R/W       R/W          R/W         R/W         R/W         R/W
    Reset           0             0            0         0            0           0           0           0


               Bits 31:0 – CRCDATAIN[31:0] CRC Data Input
               These bits store the data for which the CRC checksum is computed. A new CRC checksum is ready
               (CRCBEAT+ 1) clock cycles after the CRCDATAIN register is written.




           © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 418
                                                                  SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

22.8.4         CRC Checksum

               Name:        CRCCHKSUM
               Offset:      0x08
               Reset:       0x00000000
               Property:    PAC Write Protection, Enable-Protected

               The CRCCHKSUM represents the 16- or 32-bit checksum value and the generated CRC. The register is
               reset to zero by default, but it is possible to reset all bits to one by writing the CRCCHKSUM register
               directly. It is possible to write this register only when the CRC module is disabled. If CRC-32 is selected
               and the CRC Status Busy flag is cleared (i.e., CRC generation is completed or aborted), the bit reversed
               (bit 31 is swapped with bit 0, bit 30 with bit 1, etc.) and complemented result will be read from
               CRCCHKSUM. If CRC-16 is selected or the CRC Status Busy flag is set (i.e., CRC generation is
               ongoing), CRCCHKSUM will contain the actual content.

         Bit        31            30           29            28            27           26            25           24
                                                            CRCCHKSUM[31:24]
   Access          R/W           R/W           R/W          R/W           R/W          R/W           R/W           R/W
    Reset            0            0             0             0            0             0            0             0


         Bit        23            22           21            20            19           18            17           16
                                                            CRCCHKSUM[23:16]
   Access          R/W           R/W           R/W          R/W           R/W          R/W           R/W           R/W
    Reset            0            0             0             0            0             0            0             0


         Bit        15            14           13            12            11           10            9             8
                                                            CRCCHKSUM[15:8]
   Access          R/W           R/W           R/W          R/W           R/W          R/W           R/W           R/W
    Reset            0            0             0             0            0             0            0             0


         Bit         7            6             5             4            3             2            1             0
                                                             CRCCHKSUM[7:0]
   Access          R/W           R/W           R/W          R/W           R/W          R/W           R/W           R/W
    Reset            0            0             0             0            0             0            0             0


               Bits 31:0 – CRCCHKSUM[31:0] CRC Checksum
               These bits store the generated CRC result. The 16 MSB bits are always read zero when CRC-16 is
               enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 419
                                                                SAM D5x/E5x Family Data Sheet
                                                                  DMAC – Direct Memory Access Controller

22.8.5         CRC Status

               Name:        CRCSTATUS
               Offset:      0x0C
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7            6            5            4            3            2            1           0
                                                                                  CRCERR    CRCZERO        CRCBUSY
   Access                                                                             R            R          R/W
    Reset                                                                             0            0           0


               Bit 2 – CRCERR CRC Error
               This bit is read '1' when the memory CRC monitor detects data corruption.

               Bit 1 – CRCZERO CRC Zero
               This bit is cleared when a new CRC source is selected.
               This bit is set when the CRC generation is complete and the CRC Checksum is zero.

               Bit 0 – CRCBUSY CRC Module Busy
               When used with an I/O interface (CRCCTRL.CRCSRC=0x1):
                • This bit is cleared by writing a '1' to it
                • This bit is set when the CRC Data Input (CRCDATAIN) register is written
                • Writing a '1' to this bit will clear the CRC Module Busy bit
                • Writing a '0' to this bit has no effect
               When used with a DMA channel (CRCCTRL.CRCSRC=0x20..,0x3F):
                • This bit is cleared when the corresponding DMA channel is disabled
                • This bit is set when the corresponding DMA channel is enabled
                • Writing a '1' to this bit has no effect
                • Writing a '0' to this bit has no effect




           © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 420
                                                              SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

22.8.6         Debug Control

               Name:       DBGCTRL
               Offset:     0x0D
               Reset:      0x00
               Property:   PAC Write Protection


         Bit        7             6           5           4            3           2            1           0
                                                                                                         DBGRUN
   Access                                                                                                  R/W
    Reset                                                                                                   0


               Bit 0 – DBGRUN Debug Run
               This bit is not reset by a Software Reset.
               This bit controls the functionality when the CPU is halted by an external debugger.
                Value       Description
                0           The DMAC is halted when the CPU is halted by an external debugger.
                1           The DMAC continues normal operation when the CPU is halted by an external debugger.




           © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 421
                                                                SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

22.8.7         Software Trigger Control

               Name:       SWTRIGCTRL
               Offset:     0x10
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31           30           29          28                 27    26           25           24
                                                           SWTRIG[31:24]
   Access          R/W          R/W           R/W        R/W             R/W       R/W         R/W          R/W
    Reset           0             0            0          0                  0      0            0           0


         Bit        23           22           21          20                 19    18           17           16
                                                           SWTRIG[23:16]
   Access          R/W          R/W           R/W        R/W             R/W       R/W         R/W          R/W
    Reset           0             0            0          0                  0      0            0           0


         Bit        15           14           13          12                 11    10            9           8
                                                              SWTRIG[15:8]
   Access          R/W          R/W           R/W        R/W             R/W       R/W         R/W          R/W
    Reset           0             0            0          0                  0      0            0           0


         Bit        7             6            5          4                  3      2            1           0
                                                               SWTRIG[7:0]
   Access          R/W          R/W           R/W        R/W             R/W       R/W         R/W          R/W
    Reset           0             0            0          0                  0      0            0           0


               Bits 31:0 – SWTRIG[31:0] Channel n Software Trigger [n = 31..0]
               This bit is cleared when the Channel Pending bit in the Channel Status register (CHSTATUS.PEND) for
               the corresponding channel is either set, or by writing a '1' to it.
               This bit is set if CHSTATUS.PEND is already '1' when writing a '1' to that bit.
               Writing a '0' to this bit will clear the bit.
               Writing a '1' to this bit will generate a DMA software trigger on channel x, if CHSTATUS.PEND=0 for
               channel x. CHSTATUS.PEND will be set and SWTRIGn will remain cleared.




           © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 422
                                                                   SAM D5x/E5x Family Data Sheet
                                                                     DMAC – Direct Memory Access Controller

22.8.8         Priority Control 0

               Name:        PRICTRL0
               Offset:      0x14
               Reset:       0x40404040
               Property:    PAC Write-Protection


         Bit        31              30                29     28            27            26        25           24
                 RRLVLEN3                QOS03[1:0]                                 LVLPRI3[4:0]
   Access           R/W          R/W                  R/W    R/W          R/W           R/W        R/W          R/W
    Reset            0              1                  0      0             0            0          0            0


         Bit        23              22                21     20            19            18        17           16
                 RRLVLEN2                QOS02[1:0]                                 LVLPRI2[4:0]
   Access           R/W          R/W                  R/W    R/W          R/W           R/W        R/W          R/W
    Reset            0              1                  0      0             0            0          0            0


         Bit        15              14                13     12            11            10         9            8
                 RRLVLEN1                QOS01[1:0]                                 LVLPRI1[4:0]
   Access           R/W          R/W                  R/W    R/W          R/W           R/W        R/W          R/W
    Reset            0              1                  0      0             0            0          0            0


         Bit         7              6                  5      4             3            2          1            0
                 RRLVLEN0                QOS00[1:0]                                 LVLPRI0[4:0]
   Access           R/W          R/W                  R/W    R/W          R/W           R/W        R/W          R/W
    Reset            0              1                  0      0             0            0          0            0


               Bits 7, 15, 23, 31 – RRLVLEN Level Round-Robin Scheduling Enable
               For details on arbitration schemes, refer to 22.6.2.4 Arbitration.
                Value       Description
                0           Static arbitration scheme for channels with level 0 priority.
                1           Round-robin arbitration scheme for channels with level 0 priority.

               Bits 5:6, 13:14, 21:22, 29:30 – QOS Level Quality of Service QoS Name Description 0x0 DISABLE
               Background (no sensitive operation) 0x1 LOW Sensitive to bandwidth 0x2 MEDIUM Sensitive to latency
               0x3 Critical Latency Critical Latency

               Bits 0:4, 8:12, 16:20, 24:28 – LVLPRI Level Channel Priority Number
               When round-robin arbitration is enabled (PRICTRL0.RRLVLEN0=1) for priority level 0, this register holds
               the channel number of the last DMA channel being granted access as the active channel with priority
               level 0.
               When static arbitration is enabled (PRICTRL0.RRLVLEN0=0) for priority level 0, and the value of this bit
               group is non-zero, it will not affect the static priority scheme.
               This bit group is not reset when round-robin arbitration gets disabled (PRICTRL0.RRLVLEN0 written to
               '0').




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 423
                                                                      SAM D5x/E5x Family Data Sheet
                                                                        DMAC – Direct Memory Access Controller

22.8.9         Interrupt Pending

               Name:         INTPEND
               Offset:       0x20
               Reset:        0x0000
               Property:     -

               This register allows the user to identify the lowest DMA channel with pending interrupt.
               An interrupt that handles several channels should consult the INTPEND register to find out which channel
               number has priority (ignoring/filtering each channel that has its own interrupt line). An interrupt dedicated
               to only one channel must not use the INTPEND register.

         Bit         15            14             13             12            11             10             9             8
                   PEND           BUSY          FERR         CRCERR                         SUSP          TCMPL          TERR
   Access            R              R             R             R/W                          R/W           R/W            R/W
    Reset            0              0             0              0                            0              0             0


         Bit         7              6             5              4              3             2              1             0
                                                                                            ID[4:0]
   Access                                                       R/W           R/W            R/W           R/W            R/W
    Reset                                                        0              0             0              0             0


               Bit 15 – PEND Pending
               This bit will read '1' when the channel selected by Channel ID field (ID) is pending.

               Bit 14 – BUSY Busy
               This bit will read '1' when the channel selected by Channel ID field (ID) is busy.

               Bit 13 – FERR Fetch Error
               This bit will read '1' when the channel selected by Channel ID field (ID) fetched an invalid descriptor.

               Bit 12 – CRCERR CRC Error
               This bit will read '1' when the channel selected by Channel ID field (ID) has a CRC Error Status Flag bit
               set, and is set when the CRC monitor detects data corruption.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear it. It will also clear the corresponding flag in the Channel n Interrupt Flag
               Status and Clear register (CHINTFLAGn), where n is determined by the Channel ID bit field (ID).

               Bit 10 – SUSP Channel Suspend
               This bit will read '1' when the channel selected by Channel ID field (ID) has pending Suspend interrupt.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear it. It will also clear the corresponding flag in the Channel n Interrupt Flag
               Status and Clear register (CHINTFLAGn), where n is determined by the Channel ID bit field (ID).

               Bit 9 – TCMPL Transfer Complete
               This bit will read '1' when the channel selected by Channel ID field (ID) has pending Transfer Complete
               interrupt.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear it. It will also clear the corresponding flag in the Channel n Interrupt Flag
               Status and Clear register (CHINTFLAGn), where n is determined by the Channel ID bit field (ID).




           © 2019 Microchip Technology Inc.                            Datasheet                             DS60001507E-page 424
                                                      SAM D5x/E5x Family Data Sheet
                                                         DMAC – Direct Memory Access Controller

Bit 8 – TERR Transfer Error
This bit will read '1' when the channel selected by Channel ID field (ID) has pending Transfer Error
interrupt.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear it. It will also clear the corresponding flag in the Channel n Interrupt Flag
Status and Clear register (CHINTFLAGn), where n is determined by the Channel ID bit field (ID).

Bits 4:0 – ID[4:0] Channel ID
These bits store the lowest channel number with pending interrupts. The number is valid if Suspend
(SUSP), Transfer Complete (TCMPL) or Transfer Error (TERR) bits are set. The Channel ID field is
refreshed when a new channel (with channel number less than the current one) with pending interrupts is
detected, or when the application clears the corresponding channel interrupt sources. When no pending
channels interrupts are available, these bits will always return zero value when read.
When the bits are written, indirect access to the corresponding Channel Interrupt Flag register is enabled.




© 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 425
                                                                SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

22.8.10 Interrupt Status

            Name:       INTSTATUS
            Offset:     0x24
            Reset:      0x00000000
            Property:   -


      Bit        31           30            29           28                  27     26           25           24
                                                              CHINT[31:24]
  Access         R             R            R            R                   R      R            R             R
   Reset          0            0            0             0                  0      0             0            0


      Bit        23           22            21           20                  19     18           17           16
                                                              CHINT[23:16]
  Access         R             R            R            R                   R      R            R             R
   Reset          0            0            0             0                  0      0             0            0


      Bit        15           14            13           12                  11     10            9            8
                                                              CHINT[15:8]
  Access         R             R            R            R                   R      R            R             R
   Reset          0            0            0             0                  0      0             0            0


      Bit         7            6            5             4                  3      2             1            0
                                                               CHINT[7:0]
  Access         R             R            R            R                   R      R            R             R
   Reset          0            0            0             0                  0      0             0            0


            Bits 31:0 – CHINT[31:0] Channel n Pending Interrupt [n=31..0]
            This bit is set when Channel n has a pending interrupt/the interrupt request is received.
            This bit is cleared when the corresponding Channel n interrupts are disabled or the interrupts sources are
            cleared.




        © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 426
                                                               SAM D5x/E5x Family Data Sheet
                                                                  DMAC – Direct Memory Access Controller

22.8.11 Busy Channels

           Name:       BUSYCH
           Offset:     0x28
           Reset:      0x00000000
           Property:   -


     Bit        31           30            29           28                 27     26            25           24
                                                         BUSYCH[31:24]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


     Bit        23           22            21           20                 19     18            17           16
                                                         BUSYCH[23:16]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


     Bit        15           14            13           12                 11     10            9             8
                                                            BUSYCH[15:8]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


     Bit         7            6            5            4                  3       2            1             0
                                                             BUSYCH[7:0]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


           Bits 31:0 – BUSYCH[31:0] Busy Channel n [x=31..0]
           This bit is cleared when the channel trigger action for DMA channel n is complete, when a bus error for
           DMA channel n is detected, or when DMA channel n is disabled.
           This bit is set when DMA channel n starts a DMA transfer.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 427
                                                                 SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

22.8.12 Pending Channels

           Name:        PENDCH
           Offset:      0x2C
           Reset:       0x00000000
           Property:    -


     Bit         31            30            29             28            27             26            25            24
            PENDCH31       PENDCH30       PENDCH29      PENDCH28      PENDCH27      PENDCH26       PENDCH25      PENDCH24
  Access         R             R              R             R              R             R             R              R
   Reset         0              0             0             0              0             0             0              0


     Bit         23            22            21             20            19             18            17            16
            PENDCH23       PENDCH22       PENDCH21      PENDCH20      PENDCH19      PENDCH18       PENDCH17      PENDCH16
  Access         R             R              R             R              R             R             R              R
   Reset         0              0             0             0              0             0             0              0


     Bit         15            14            13             12            11             10            9              8
            PENDCH15       PENDCH14       PENDCH13      PENDCH12      PENDCH11      PENDCH10       PENDCH9        PENDCH8
  Access         R             R              R             R              R             R             R              R
   Reset         0              0             0             0              0             0             0              0


     Bit         7              6             5             4              3             2             1              0
             PENDCH7       PENDCH6        PENDCH5       PENDCH4        PENDCH3       PENDCH2       PENDCH1        PENDCH0
  Access         R             R              R             R              R             R             R              R
   Reset         0              0             0             0              0             0             0              0


           Bits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31 – PENDCH Pending Channel n [n=31..0]
           This bit is cleared when trigger execution defined by channel trigger action settings for DMA channel n is
           started, when a bus error for DMA channel n is detected or when DMA channel n is disabled. For details
           on trigger action settings, refer to CHCTRLB.TRIGACT.
           This bit is set when a transfer is pending on DMA channel n.




       © 2019 Microchip Technology Inc.                           Datasheet                             DS60001507E-page 428
                                                                SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

22.8.13 Active Channel and Levels

            Name:        ACTIVE
            Offset:      0x30
            Reset:       0x00000000
            Property:    -


      Bit        31            30           29            28                 27      26            25              24
                                                               BTCNT[15:8]
  Access          R            R             R            R                  R        R            R               R
   Reset          0            0             0             0                 0        0            0               0


      Bit        23            22           21            20                 19      18            17              16
                                                               BTCNT[7:0]
  Access          R            R             R            R                  R        R            R               R
   Reset          0            0             0             0                 0        0            0               0


      Bit        15            14           13            12                 11      10            9               8
               ABUSY                                                               ID[4:0]
  Access          R                                       R                  R        R            R               R
   Reset          0                                        0                 0        0            0               0


      Bit         7            6             5             4                 3        2            1               0
                                                                       LVLEX3      LVLEX2       LVLEX1        LVLEX0
  Access                                                                     R        R            R               R
   Reset                                                                     0        0            0               0


            Bits 31:16 – BTCNT[15:0] Active Channel Block Transfer Count
            These bits hold the 16-bit block transfer count of the ongoing transfer. This value is stored in the active
            channel and written back in the corresponding Write-Back channel memory location when the arbiter
            grants a new channel access. The value is valid only when the active channel Active Busy flag (ABUSY)
            is set.

            Bit 15 – ABUSY Active Channel Busy
            This bit is cleared when the active transfer count is written back in the write-back memory section.
            This bit is set when the next descriptor transfer count is read from the write-back memory section.

            Bits 12:8 – ID[4:0] Active Channel ID
            These bits hold the channel index currently stored in the active channel registers. The value is updated
            each time the arbiter grants a new channel transfer access request.

            Bits 0, 1, 2, 3 – LVLEXx Level x Channel Trigger Request Executing [x=3..0]
            This bit is set when a level-x channel trigger request is executing or pending.
            This bit is cleared when no request is pending or being executed.




        © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 429
                                                            SAM D5x/E5x Family Data Sheet
                                                              DMAC – Direct Memory Access Controller

22.8.14 Descriptor Memory Section Base Address

           Name:       BASEADDR
           Offset:     0x34
           Reset:      0x00000000
           Property:   PAC Write Protection, Enable-Protected


     Bit        31           30           29           28          27           26           25              24
                                                      BASEADDR[31:24]
  Access       R/W          R/W           R/W         R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0           0            0            0            0              0


     Bit        23           22           21           20          19           18           17              16
                                                      BASEADDR[23:16]
  Access       R/W          R/W           R/W         R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0           0            0            0            0              0


     Bit        15           14           13           12           11          10            9              8
                                                       BASEADDR[15:8]
  Access       R/W          R/W           R/W         R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0           0            0            0            0              0


     Bit        7             6            5           4            3            2            1              0
                                                       BASEADDR[7:0]
  Access       R/W          R/W           R/W         R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0           0            0            0            0              0


           Bits 31:0 – BASEADDR[31:0] Descriptor Memory Base Address
           These bits store the Descriptor memory section base address. The value must be 128-bit aligned.




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 430
                                                           SAM D5x/E5x Family Data Sheet
                                                             DMAC – Direct Memory Access Controller

22.8.15 Write-Back Memory Section Base Address

           Name:       WRBADDR
           Offset:     0x38
           Reset:      0x00000000
           Property:   PAC Write Protection, Enable-Protected


     Bit        31           30           29          28           27          26           25           24
                                                      WRBADDR[31:24]
  Access       R/W          R/W           R/W        R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0          0            0            0            0           0


     Bit        23           22           21          20           19          18           17           16
                                                      WRBADDR[23:16]
  Access       R/W          R/W           R/W        R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0          0            0            0            0           0


     Bit        15           14           13          12           11          10            9           8
                                                       WRBADDR[15:8]
  Access       R/W          R/W           R/W        R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0          0            0            0            0           0


     Bit        7             6            5          4            3            2            1           0
                                                       WRBADDR[7:0]
  Access       R/W          R/W           R/W        R/W          R/W          R/W         R/W          R/W
   Reset        0             0            0          0            0            0            0           0


           Bits 31:0 – WRBADDR[31:0] Write-Back Memory Base Address
           These bits store the Write-Back memory base address. The value must be 128-bit aligned.




       © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 431
                                                                    SAM D5x/E5x Family Data Sheet
                                                                       DMAC – Direct Memory Access Controller

22.8.16 Channel Control A

           Name:       CHCTRLA
           Offset:     0x40 + n*0x10 [n=0..31]
           Reset:      0x00000000
           Property:   PAC Write-Protection, Enable-Protected


     Bit        31           30            29             28                 27      26           25          24
                                           THRESHOLD[1:0]                             BURSTLEN[3:0]
  Access                                  R/W             R/W               R/W      R/W         R/W         R/W
   Reset                                   0                  0                  0    0           0           0


     Bit        23           22            21             20                 19      18           17          16
                                               TRIGACT[1:0]
  Access                                  R/W             R/W
   Reset                                   0                  0


     Bit        15           14            13             12                 11      10           9           8
                                                                  TRIGSRC[7:0]
  Access       R/W           R/W          R/W             R/W               R/W      R/W         R/W         R/W
   Reset         0            0            0                  0                  0    0           0           0


     Bit         7            6            5                  4                  3    2           1           0
                         RUNSTDBY                                                              ENABLE       SWRST
  Access                     R/W                                                                 R/W         R/W
   Reset                      0                                                                   0           0


           Bits 29:28 – THRESHOLD[1:0] FIFO Threshold
           These bits define the threshold from which the DMA starts to write to the destination. These bits have no
           effect in the case of single beat transfers.
           These bits are not enable-protected.
            Value        Name         Description
            0x0          1BEAT        Destination write starts after each beat source addess read
            0x1          2BEATS       Destination write starts after 2-beats source address read
            0x2          4BEATS       Destination write starts after 4-beats source address read
            0x3          8BEATS       Destination write starts after 8-beats source address read

           Bits 27:24 – BURSTLEN[3:0] Burst Length
           These bits define the burst mode.
           These bits are not enable-protected.
            Value      Name                     Description
            0x0        SINGLE                   Single-beat burst
            0x1        2BEAT                    2-beats burst length
            0x2        3BEAT                    3-beats burst length
            0x3        4BEAT                    4-beats burst length
            0x4        5BEAT                    5-beats burst length
            0x5        6BEAT                    6-beats burst length
            0x6        7BEAT                    7-beats burst length




       © 2019 Microchip Technology Inc.                               Datasheet                   DS60001507E-page 432
                                                    SAM D5x/E5x Family Data Sheet
                                                       DMAC – Direct Memory Access Controller

 Value        Name                        Description
 0x7          8BEAT                       8-beats burst length
 0x8          9BEAT                       9-beats burst length
 0x9          10BEAT                      10-beats burst length
 0xA          11BEAT                      11-beats burst length
 0xB          12BEAT                      12-beats burst length
 0xC          13BEAT                      13-beats burst length
 0xD          14BEAT                      14-beats burst length
 0xE          15BEAT                      15-beats burst length
 0xF          16BEAT                      16-beats burst length

Bits 21:20 – TRIGACT[1:0] Trigger Action
These bits define the trigger action used for a transfer.
These bits are not enable-protected.
 Value      Name                        Description
 0x0        BLOCK                       One trigger required for each block transfer
 0x1                                    Reserved
 0x2        BURST                       One trigger required for each burst transfer
 0x3        TRANSACTION                 One trigger required for each transaction

Bits 15:8 – TRIGSRC[7:0] Trigger Source
These bits define the peripheral that will be the source of a trigger.

 Index                Instance      Channel            Presentation
 0x00                 DISABLE                          Only software/event triggers
 0x01                 RTC           TIMESTAMP          DMA RTC timestamp trigger
 0x02                 DSU           DCC0               DMAC ID for DCC0 register
 0x03                 DSU           DCC1               DMAC ID for DCC1 register
 0x04                 SERCOM0       RX                 Index of DMA RX trigger
 0x05                 SERCOM0       TX                 Index of DMA TX trigger
 0x06                 SERCOM1       RX                 Index of DMA RX trigger
 0x07                 SERCOM1       TX                 Index of DMA TX trigger
 0x08                 SERCOM2       RX                 Index of DMA RX trigger
 0x09                 SERCOM2       TX                 Index of DMA TX trigger
 0x0A                 SERCOM3       RX                 Index of DMA RX trigger
 0x0B                 SERCOM3       TX                 Index of DMA TX trigger
 0x0C                 SERCOM4       RX                 Index of DMA RX trigger
 0x0D                 SERCOM4       TX                 Index of DMA TX trigger
 0x0E                 SERCOM5       RX                 Index of DMA RX trigger
 0x0F                 SERCOM5       TX                 Index of DMA TX trigger
 0x10                 SERCOM6       RX                 Index of DMA RX trigger




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 433
                                             SAM D5x/E5x Family Data Sheet
                                              DMAC – Direct Memory Access Controller

...........continued
 Index                 Instance    Channel    Presentation
 0x11                  SERCOM6     TX         Index of DMA TX trigger
 0x12                  SERCOM7     RX         Index of DMA RX trigger
 0x13                  SERCOM7     TX         Index of DMA TX trigger
 0x14                  CAN0        DEBUG      DMA CAN Debug Req
 0x15                  CAN1        DEBUG      DMA CAN Debug Req
 0x16                  TCC0        OVF        DMA overflow/underflow/retrigger trigger
 0x1C - 0x17           TCC0        MC         Indexes of DMA Match/Compare triggers
 0x1D                  TCC1        OVF        DMA overflow/underflow/retrigger trigger
 0x21- 0x1E            TCC1        MC         Indexes of DMA Match/Compare triggers
 0x22                  TCC2        OVF        DMA overflow/underflow/retrigger trigger
 0x25 - 0x23           TCC2        MC         Indexes of DMA Match/Compare triggers
 0x26                  TCC3        OVF        DMA overflow/underflow/retrigger trigger
 0x28 - 0x27           TCC3        MC         Indexes of DMA Match/Compare triggers
 0x29                  TCC4        OVF        DMA overflow/underflow/retrigger trigger
 0x2B - 0x2A           TCC4        MC         Indexes of DMA Match/Compare triggers
 0x2C                  TC0         OVF        Indexes of DMA Overflow trigger
 0x2E - 0x2D           TC0         MC         Indexes of DMA Match/Compare triggers
 0x2F                  TC1         OVF        Indexes of DMA Overflow trigger
 0x31 - 0x30           TC1         MC         Indexes of DMA Match/Compare triggers
 0x32                  TC2         OVF        Indexes of DMA Overflow trigger
 0x34 - 0x33           TC2         MC         Indexes of DMA Match/Compare triggers
 0x35                  TC3         OVF        Indexes of DMA Overflow trigger
 0x37 - 0x36           TC3         MC         Indexes of DMA Match/Compare triggers
 0x38                  TC4         OVF        Indexes of DMA Overflow trigger
 0x3A - 0x39           TC4         MC         Indexes of DMA Match/Compare triggers
 0x3B                  TC5         OVF        Indexes of DMA Overflow trigger
 0x3D:0x3C             TC5         MC         Indexes of DMA Match/Compare triggers
 0x3E                  TC6         OVF        Indexes of DMA Overflow trigger
 0x40 - 0x3F           TC6         MC         Indexes of DMA Match/Compare triggers
 0x41                  TC7         OVF        Indexes of DMA Overflow trigger
 0x43 - 0x41           TC7         MC         Indexes of DMA Match/Compare triggers




© 2019 Microchip Technology Inc.             Datasheet                          DS60001507E-page 434
                                                     SAM D5x/E5x Family Data Sheet
                                                         DMAC – Direct Memory Access Controller

...........continued
 Index                 Instance      Channel             Presentation
 0x44                  ADC0          RESRDY              index of DMA RESRDY trigger
 0x45                  ADC0          SEQ                 Index of DMA SEQ trigger
 0x46                  ADC1          RESRDY              Index of DMA RESRDY trigger
 0x47                  ADC1          SEQ                 Index of DMA SEQ trigger
 0x49 - 0x48           DAC           EMPTY               DMA DAC Empty Req
 0x4B - 0x4A           DAC           RESRDY              DMA DAC Result Ready Req
 0x4D - 0x4C           I2S           RX                  Indexes of DMA RX triggers
 0x4F - 0x4E           I2S           TX                  Indexes of DMA TX triggers
 0x50                  PCC           RX                  Indexes of PCC RX trigger
 0x51                  AES           WR                  DMA DATA Write trigger
 0x52                  AES           RD                  DMA DATA Read trigger
 0x53                  QSPI          RX                  Indexes of QSPI RX trigger
 0x54                  QSPI          TX                  Indexes of QSPI TX trigger

Bit 6 – RUNSTDBY Channel run in standby
This bit is used to keep the DMAC channel running in standby mode.
This bit is not enable-protected.
 Value       Description
 0            The DMAC channel is halted in standby.
 1            The DMAC channel continues to run in standby.

Bit 1 – ENABLE Channel Enable
Writing a '0' to this bit during an ongoing transfer, the bit will not be cleared until the internal data transfer
buffer is empty and the DMA transfer is aborted. The internal data transfer buffer will be empty once the
ongoing burst transfer is completed.
Writing a '1' to this bit will enable the DMA channel.
This bit is not enable-protected.
 Value        Description
 0            DMA channel is disabled.
 1            DMA channel is enabled.

Bit 0 – SWRST Channel Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets the channel registers to their initial state. The bit can be set when the
channel is disabled (ENABLE=0). Writing a '1' to this bit will be ignored as long as ENABLE=1. This bit is
automatically cleared when the reset is completed.
 Value        Description
 0            There is no reset operation ongoing.
 1            The reset operation is ongoing.




© 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 435
                                                         SAM D5x/E5x Family Data Sheet
                                                           DMAC – Direct Memory Access Controller

22.8.17 Channel Control B

           Name:       CHCTRLB
           Offset:     0x44 + n*0x10 [n=0..31]
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit         7            6             5        4           3            2           1                0
                                                                                               CMD[1:0]
  Access                                                                                 R/W              R/W
   Reset                                                                                  0                0


           Bits 1:0 – CMD[1:0] Software Command
           These bits define the software commands. Refer to 22.6.3.3 Channel Suspend and 22.6.3.4 Channel
           Resume and Next Suspend Skip.
           These bits are not enable-protected.

           CMD[1:0]                  Name                Description
           0x0                       NOACT               No action
           0x1                       SUSPEND             Channel suspend operation
           0x2                       RESUME              Channel resume operation
           0x3                       -                   Reserved




       © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 436
                                                             SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

22.8.18 Channel Priority Level

            Name:       CHPRILVL
            Offset:     0x45 + n*0x10 [n=0..31]
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6            5            4             3            2            1                   0
                                                                                                      PRILVL[1:0]
  Access                                                                                        R/W                 R/W
   Reset                                                                                         0                   0


            Bits 1:0 – PRILVL[1:0] Channel Priority Level
            These bits define the priority level used for the DMA channel. The available levels are shown below,
            where a high level has priority over a low level. These bits are not enable-protected.
             Value      Name            Description
             0x0        LVL0            Channel Priority Level 0 (Lowest Level)
             0x1        LVL1            Channel Priority Level 1
             0x2        LVL2            Channel Priority Level 2
             0x3        LVL3            Channel Priority Level 3 (Highest Level)




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 437
                                                              SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

22.8.19 Channel Event Control

           Name:       CHEVCTRL
           Offset:     0x46 + n*0x10 [n=0..31]
           Reset:      0x00
           Property:   PAC Write-Protection, Enable-Protected


     Bit         7            6             5            4             3            2             1               0
               EVOE          EVIE            EVOMODE[1:0]                                     EVACT[2:0]
  Access       R/W           R/W           R/W          R/W                        R/W           R/W          R/W
   Reset         0            0             0            0                          0             0               0


           Bit 7 – EVOE Channel Event Output Enable
           This bit indicates if the Channel event generation is enabled. The event will be generated for every
           condition defined in the Channel Event Output Selection bits (CHEVCTRL.EVOMODE).
            Value       Description
            0            Channel event generation is disabled.
            1            Channel event generation is enabled.

           Bit 6 – EVIE Channel Event Input Enable
           Value       Description
           0           Channel event action will not be executed on any incoming event.
           1           Channel event action will be executed on any incoming event.

           Bits 5:4 – EVOMODE[1:0] Channel Event Output Mode
           These bits define the channel event output selection. For details on event output generation, refer to
           22.6.3.6 Event Output Selection.
            Value      Name        Description
            0x0        DEFAULT Block event output selection. Refer to BTCTRL.EVOSEL for available selections.
            0x1        TRIGACT Ongoing trigger action
            0x2-0x3                Reserved

           Bits 2:0 – EVACT[2:0] Channel Event Input Action
           These bits define the event input action. The action is executed only if the corresponding EVIE bit in the
           CHEVCTRL register of the channel is set. For details on event actions, refer to 22.6.3.5 Event Input
           Actions. These bits are available only for channels with event input support.
            Value      Name                    Description
            0x0        NOACT                   No action
            0x1        TRIG                    Transfer and periodic transfer trigger
            0x2        CTRIG                   Conditional transfer trigger
            0x3        CBLOCK                  Conditional block transfer
            0x4        SUSPEND                 Channel suspend operation
            0x5        RESUME                  Channel resume operation
            0x6        SSKIP                   Skip next block suspend action
            0x7        INCPRI                  Increase priority




       © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 438
                                                                SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

22.8.20 Channel Interrupt Enable Clear

            Name:        CHINTENCLR
            Offset:      0x4C + n*0x10 [n=0..31]
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Channel Interrupt Enable Set (CHINTENSET) register.

      Bit         7             6             5             4             3             2              1               0
                                                                                      SUSP          TCMPL          TERR
  Access                                                                               R/W           R/W           R/W
   Reset                                                                                0              0               0


            Bit 2 – SUSP Channel Suspend Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Channel Suspend Interrupt Enable bit, which disables the Channel
            Suspend interrupt.
            Value         Description
            0             The Channel Suspend interrupt is disabled.
            1             The Channel Suspend interrupt is enabled.

            Bit 1 – TCMPL Channel Transfer Complete Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Channel Transfer Complete Interrupt Enable bit, which disables the
            Channel Transfer Complete interrupt.
            Value         Description
            0             The Channel Transfer Complete interrupt is disabled. When block action is set to none, the
                          TCMPL flag will not be set when a block transfer is completed.
            1             The Channel Transfer Complete interrupt is enabled.

            Bit 0 – TERR Channel Transfer Error Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Channel Transfer Error Interrupt Enable bit, which disables the
            Channel Transfer Error interrupt.
            Value         Description
            0             The Channel Transfer Error interrupt is disabled.
            1             The Channel Transfer Error interrupt is enabled.




        © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 439
                                                               SAM D5x/E5x Family Data Sheet
                                                                  DMAC – Direct Memory Access Controller

22.8.21 Channel Interrupt Enable Set

            Name:        CHINTENSET
            Offset:      0x4D + n*0x10 [n=0..31]
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Channel Interrupt Enable Clear (CHINTENCLR) register.

      Bit         7             6            5             4             3             2             1             0
                                                                                     SUSP         TCMPL         TERR
  Access                                                                              R/W          R/W           R/W
   Reset                                                                               0             0             0


            Bit 2 – SUSP Channel Suspend Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Channel Suspend Interrupt Enable bit, which enables the Channel
            Suspend interrupt.
            Value         Description
            0             The Channel Suspend interrupt is disabled.
            1             The Channel Suspend interrupt is enabled.

            Bit 1 – TCMPL Channel Transfer Complete Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Channel Transfer Complete Interrupt Enable bit, which enables the
            Channel Transfer Complete interrupt.
            Value         Description
            0             The Channel Transfer Complete interrupt is disabled.
            1             The Channel Transfer Complete interrupt is enabled.

            Bit 0 – TERR Channel Transfer Error Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Channel Transfer Error Interrupt Enable bit, which enables the Channel
            Transfer Error interrupt.
             Value        Description
             0            The Channel Transfer Error interrupt is disabled.
             1            The Channel Transfer Error interrupt is enabled.




        © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 440
                                                                SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

22.8.22 Channel Interrupt Flag Status and Clear

            Name:        CHINTFLAG
            Offset:      0x4E + n*0x10 [n=0..31]
            Reset:       0x00
            Property:    -


      Bit         7             6             5             4             3             2             1                0
                                                                                      SUSP         TCMPL          TERR
  Access                                                                               R/W           R/W           R/W
   Reset                                                                                0             0                0


            Bit 2 – SUSP Channel Suspend
            This flag is cleared by writing a '1' to it.
            This flag is set when a block transfer with suspend block action is completed, when a software suspend
            command is executed, when a suspend event is received or when an invalid descriptor is fetched by the
            DMA.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Channel Suspend interrupt flag for the corresponding channel.
            For details on available software commands, refer to CHCTRLB.CMD.
            For details on available event input actions, refer to CHCTRLB.EVACT.
            For details on available block actions, refer to BTCTRL.BLOCKACT.

            Bit 1 – TCMPL Channel Transfer Complete
            This flag is cleared by writing a '1' to it.
            This flag is set when a block transfer is completed and the corresponding interrupt block action is
            enabled.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Transfer Complete interrupt flag for the corresponding channel.

            Bit 0 – TERR Channel Transfer Error
            This flag is cleared by writing a '1' to it.
            This flag is set when a bus error is detected during a beat transfer or when the DMAC fetches an invalid
            descriptor.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Transfer Error interrupt flag for the corresponding channel.




        © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 441
                                                               SAM D5x/E5x Family Data Sheet
                                                                  DMAC – Direct Memory Access Controller

22.8.23 Channel Status

           Name:        CHSTATUS
           Offset:      0x4F + n*0x10 [n=0..31]
           Reset:       0x00
           Property:    -


     Bit         7             6             5             4             3             2             1             0
                                                                     CRCERR          FERR          BUSY          PEND
  Access                                                                R/W            R             R             R
   Reset                                                                 0             0             0             0


           Bit 3 – CRCERR Channel CRC Error
           This bit is set when the CRC monitor detects data corruption. This bit is cleared bu writing '1' to it, or by
           clearing the CRC Error bit in the INTPEND register (INTPEND.CRCERR).

           Bit 2 – FERR Channel Fetch Error
           This bit is cleared when a software resume command is executed.
           This bit is set when an invalid descriptor is fetched.

           Bit 1 – BUSY Channel Busy
           This bit is cleared when the channel trigger action is completed, when a bus error is detected or when the
           channel is disabled.
           This bit is set when the DMA channel starts a DMA transfer.

           Bit 0 – PEND Channel Pending
           This bit is cleared when the channel trigger action is started, when a bus error is detected or when the
           channel is disabled. For details on trigger action settings, refer to CHCTRLB.TRIGACT.
           This bit is set when a transfer is pending on the DMA channel, as soon as the transfer request is
           received.




       © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 442
                                                             SAM D5x/E5x Family Data Sheet
                                                               DMAC – Direct Memory Access Controller


22.9      Register Summary - SRAM

 Offset        Name        Bit Pos.

                              7:0                                    BLOCKACT[1:0]          EVOSEL[1:0]             VALID
 0x00         BTCTRL
                             15:8            STEPSIZE[2:0]        STEPSEL     DSTINC    SRCINC            BEATSIZE[1:0]
                              7:0                                      BTCNT[7:0]
 0x02         BTCNT
                             15:8                                     BTCNT[15:8]
                              7:0                                     SRCADDR[7:0]
                             15:8                                    SRCADDR[15:8]
 0x04        SRCADDR
                             23:16                                   SRCADDR[23:16]
                             31:24                                   SRCADDR[31:24]
                              7:0                                     DSTADDR[7:0]
                             15:8                                    DSTADDR[15:8]
 0x08        DSTADDR
                             23:16                                   DSTADDR[23:16]
                             31:24                                   DSTADDR[31:24]
                              7:0                                    DESCADDR[7:0]
                             15:8                                    DESCADDR[15:8]
 0x0C       DESCADDR
                             23:16                                  DESCADDR[23:16]
                             31:24                                  DESCADDR[31:24]




22.10     Register Description - SRAM
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 22.5.8 Register Access Protection.
          Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
          Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




          © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 443
                                                                SAM D5x/E5x Family Data Sheet
                                                                  DMAC – Direct Memory Access Controller

22.10.1 Block Transfer Control

            Name:        BTCTRL
            Offset:      0x00
            Property:    -

            The BTCTRL register offset is relative to (BASEADDR or WRBADDR) + Channel Number * 0x10

      Bit        15            14            13            12           11            10                 9                   8
                          STEPSIZE[2:0]                STEPSEL        DSTINC        SRCINC                   BEATSIZE[1:0]
  Access
   Reset


      Bit         7             6            5             4             3             2                 1                   0
                                                            BLOCKACT[1:0]                  EVOSEL[1:0]                 VALID
  Access
   Reset


            Bits 15:13 – STEPSIZE[2:0] Address Increment Step Size
            These bits select the address increment step size. The setting apply to source or destination address,
            depending on STEPSEL setting.
             Value      Name         Description
             0x0        X1           Next ADDR = ADDR + (Beat size in byte) * 1
             0x1        X2           Next ADDR = ADDR + (Beat size in byte) * 2
             0x2        X4           Next ADDR = ADDR + (Beat size in byte) * 4
             0x3        X8           Next ADDR = ADDR + (Beat size in byte) * 8
             0x4        X16          Next ADDR = ADDR + (Beat size in byte) * 16
             0x5        X32          Next ADDR = ADDR + (Beat size in byte) * 32
             0x6        X64          Next ADDR = ADDR + (Beat size in byte) * 64
             0x7        X128         Next ADDR = ADDR + (Beat size in byte) * 128

            Bit 12 – STEPSEL Step Selection
            This bit selects if source or destination addresses are using the step size settings.
             Value       Name         Description
             0x0         DST          Step size settings apply to the destination address
             0x1         SRC          Step size settings apply to the source address

            Bit 11 – DSTINC Destination Address Increment Enable
            Writing a '0' to this bit will disable the destination address incrementation. The address will be kept fixed
            during the data transfer.
            Writing a '1' to this bit will enable the destination address incrementation. By default, the destination
            address is incremented by 1. If the STEPSEL bit is cleared, flexible step-size settings are available in the
            STEPSIZE register.
             Value       Description
             0           The Destination Address Increment is disabled
             1           The Destination Address Increment is enabled




        © 2019 Microchip Technology Inc.                         Datasheet                               DS60001507E-page 444
                                                       SAM D5x/E5x Family Data Sheet
                                                           DMAC – Direct Memory Access Controller

Bit 10 – SRCINC Source Address Increment Enable
Writing a '0' to this bit will disable the source address incrementation. The address will be kept fixed
during the data transfer.
Writing a '1' to this bit will enable the source address incrementation. By default, the source address is
incremented by 1. If the STEPSEL bit is set, flexible step-size settings are available in the STEPSIZE
register.
 Value       Description
 0           The Source Address Increment is disabled
 1           The Source Address Increment is enabled

Bits 9:8 – BEATSIZE[1:0] Beat Size
These bits define the size of one beat. A beat is the size of one data transfer bus access, and the setting
apply to both read and write accesses.
 Value      Name                             Description
 0x0        BYTE                             8-bit bus transfer
 0x1        HWORD                            16-bit bus transfer
 0x2        WORD                             32-bit bus transfer
 other                                       Reserved

Bits 4:3 – BLOCKACT[1:0] Block Action
These bits define what actions the DMAC should take after a block transfer has completed.

 BLOCKACT[1:0] Name                  Description
 0x0                   NOACT         Channel will be disabled if it is the last block transfer in the transaction
 0x1                   INT           Channel will be disabled if it is the last block transfer in the transaction
                                     and block interrupt
 0x2                   SUSPEND Channel suspend operation is completed
 0x3                   BOTH          Both channel suspend operation and block interrupt

Bits 2:1 – EVOSEL[1:0] Event Output Selection
These bits define the event output selection.

 EVOSEL[1:0]                 Name            Description
 0x0                         DISABLE         Event generation disabled
 0x1                         BLOCK           Event strobe when block transfer complete
 0x2                                         Reserved
 0x3                         BEAT            Event strobe when beat transfer complete

Bit 0 – VALID Descriptor Valid
Writing a '0' to this bit in the Descriptor or Write-Back memory will suspend the DMA channel operation
when fetching the corresponding descriptor.
The bit is automatically cleared in the Write-Back memory section when channel is aborted, when an
error is detected during the block transfer, or when the block transfer is completed.
 Value       Description
 0           The descriptor is not valid




© 2019 Microchip Technology Inc.                         Datasheet                             DS60001507E-page 445
                                        SAM D5x/E5x Family Data Sheet
                                         DMAC – Direct Memory Access Controller

 Value        Description
 1            The descriptor is valid




© 2019 Microchip Technology Inc.        Datasheet               DS60001507E-page 446
                                                                SAM D5x/E5x Family Data Sheet
                                                                    DMAC – Direct Memory Access Controller

22.10.2 Block Transfer Count

            Name:       BTCNT
            Offset:     0x02
            Property:   -

            The BTCNT register offset is relative to (BASEADDR or WRBADDR) + Channel Number * 0x10

      Bit        15            14           13            12                 11      10            9            8
                                                               BTCNT[15:8]
  Access
   Reset


      Bit         7            6             5            4                  3       2             1            0
                                                               BTCNT[7:0]
  Access
   Reset


            Bits 15:0 – BTCNT[15:0] Block Transfer Count
            This bit group holds the 16-bit block transfer count.
            During a transfer, the internal counter value is decremented by one after each beat transfer. The internal
            counter is written to the corresponding write-back memory section for the DMA channel when the DMA
            channel loses priority, is suspended or gets disabled. The DMA channel can be disabled by a complete
            transfer, a transfer error or by software.




        © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 447
                                                             SAM D5x/E5x Family Data Sheet
                                                               DMAC – Direct Memory Access Controller

22.10.3 Block Transfer Source Address

           Name:       SRCADDR
           Offset:     0x04
           Property:   -

           The SRCADDR register offset is relative to (BASEADDR or WRBADDR) + Channel Number * 0x10

     Bit        31           30            29           28            27           26           25            24
                                                         SRCADDR[31:24]
  Access
   Reset


     Bit        23           22            21           20            19           18           17            16
                                                         SRCADDR[23:16]
  Access
   Reset


     Bit        15           14            13           12            11           10            9            8
                                                         SRCADDR[15:8]
  Access
   Reset


     Bit         7            6            5             4            3            2             1            0
                                                          SRCADDR[7:0]
  Access
   Reset


           Bits 31:0 – SRCADDR[31:0] Transfer Source Address
           This bit group holds the source address corresponding to the last beat transfer address in the block
           transfer.




       © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 448
                                                                SAM D5x/E5x Family Data Sheet
                                                                   DMAC – Direct Memory Access Controller

22.10.4 Block Transfer Destination Address

            Name:       DSTADDR
            Offset:     0x08
            Property:   -

            The DSTADDR register offset is relative to (BASEADDR or WRBADDR) + Channel Number * 0x10

      Bit        31            30           29            28             27         26            25           24
                                                          DSTADDR[31:24]
  Access
   Reset


      Bit        23            22           21            20             19         18            17           16
                                                          DSTADDR[23:16]
  Access
   Reset


      Bit        15            14           13            12             11         10            9             8
                                                           DSTADDR[15:8]
  Access
   Reset


      Bit         7            6             5            4                  3       2            1             0
                                                              DSTADDR[7:0]
  Access
   Reset


            Bits 31:0 – DSTADDR[31:0] Transfer Destination Address
            This bit group holds the destination address corresponding to the last beat transfer address in the block
            transfer.




        © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 449
                                                              SAM D5x/E5x Family Data Sheet
                                                                DMAC – Direct Memory Access Controller

22.10.5 Next Descriptor Address

            Name:       DESCADDR
            Offset:     0x0C
            Property:   -

            The DESCADDR register offset is relative to (BASEADDR or WRBADDR) + Channel Number * 0x10

      Bit        31           30            29           28           27           26            25           24
                                                         DESCADDR[31:24]
  Access
   Reset


      Bit        23           22            21           20           19           18            17           16
                                                         DESCADDR[23:16]
  Access
   Reset


      Bit        15           14            13           12           11           10            9             8
                                                         DESCADDR[15:8]
  Access
   Reset


      Bit         7            6            5            4             3            2            1             0
                                                          DESCADDR[7:0]
  Access
   Reset


            Bits 31:0 – DESCADDR[31:0] Next Descriptor Address
            This bit group holds the SRAM address of the next descriptor. The value must be 128-bit aligned. If the
            value of this SRAM register is 0x00000000, the transaction will be terminated when the DMAC tries to
            load the next transfer descriptor.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 450
