# 24. GMAC - Ethernet MAC

*Source: `Atmel-SAMD51.pdf`, pages 477-638 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                     GMAC - Ethernet MAC


24.    GMAC - Ethernet MAC
       The description and registers of this peripheral are using the 'GMAC' designation although the device
       does not support Gigabit Ethernet functionality.



24.1   Description
       The Ethernet Media Access Controller (GMAC) module implements a 10/100 Mbps Ethernet MAC,
       compatible with the IEEE 802.3 standard. The GMAC can operate in either half or full duplex mode at all
       supported speeds.



24.2   Features
         •   Compatible with IEEE Standard 802.3
         •   10, 100 Mbps operation
         •   Full and half duplex operation at all supported speeds of operation
         •   Statistics Counter Registers for RMON/MIB
         •   MII/RMII interface to the physical layer
         •   Integrated physical coding
         •   Direct memory access (DMA) interface to external memory
         •   Programmable burst length and endianism for DMA
         •   Interrupt generation to signal receive and transmit completion, errors or other events
         •   Automatic pad and cyclic redundancy check (CRC) generation on transmitted frames
         •   Automatic discard of frames received with errors
         •   Receive and transmit IP, TCP and UDP checksum offload. Both IPv4 and IPv6 packet types
             supported
         •   Address checking logic for four specific 48-bit addresses, four type IDs, promiscuous mode, hash
             matching of unicast and multicast destination addresses and Wake-on-LAN
         •   Management Data Input/Output (MDIO) interface for physical layer management
         •   Support for jumbo frames up to 10240 Bytes
         •   Full duplex flow control with recognition of incoming pause frames and hardware generation of
             transmitted pause frames
         •   Half duplex flow control by forcing collisions on incoming frames
         •   Support for 802.1Q VLAN tagging with recognition of incoming VLAN and priority tagged frames
         •   Programmable Inter Packet Gap (IPG) Stretch
         •   Recognition of IEEE 1588 PTP frames
         •   IEEE 1588 time stamp unit (TSU) and TSU event generation
         •   Support for 802.1AS timing and synchronization
         •   Supports 802.1Qav traffic shaping on two highest priority queues
         •   Support for 802.3az Energy Efficient Ethernet




       © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 477
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                              GMAC - Ethernet MAC


24.3   Block Diagram
       Figure 24-1. Block Diagram

                                                       Status &
                                                        Statistic
                                                       Registers
                                     Register
                      APB
                                     Interface
                                                                                                   MDIO
                                                        Control
                                                       Registers




                                                                         MAC Transmitter
                                     AHB DMA             FIFO
                      AHB                                                                          Media Interface
                                     Interface         Interface
                                                                          MAC Receiver




                                                                          Frame Filtering
                                   Packet Buffer
                                    Memories




24.4   Signal Description
       The GMAC includes the following signal interfaces:
         •   MII, RMII to an external PHY
         •   MDIO interface for external PHY management
         •   Slave APB interface for accessing GMAC registers
         •   Master AHB interface for memory access
         •   GTSUCOMP signal for TSU timer count value comparison
       Table 24-1. GMAC Connections in Different Modes

        Signal Name               Function                                                  MII              RMII
        GTXCK                     Transmit Clock or Reference Clock                         TXCK             REFCK
        GTXEN                     Transmit Enable                                           TXEN             TXEN
        GTX[3..0]                 Transmit Data                                             TXD[3:0]         TXD[1:0]
        GTXER                     Transmit Coding Error                                     TXER             Not Used
        GRXCK                     Receive Clock                                             RXCK             Not Used
        GRXDV                     Receive Data Valid                                        RXDV             CRSDV
        GRX[3..0]                 Receive Data                                              RXD[3:0]         RXD[1:0]
        GRXER                     Receive Error                                             RXER             RXER
        GCRS                      Carrier Sense and Data Valid                              CRS              Not Used
        GCOL                      Collision Detect                                          COL              Not Used




       © 2019 Microchip Technology Inc.                             Datasheet                          DS60001507E-page 478
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

         ...........continued
          Signal Name               Function                                        MII             RMII
          GMDC                      Management Data Clock                           MDC             MDC
          GMDIO                     Management Data Input/Output                    MDIO            MDIO
           •


24.5     Product Dependencies

24.5.1   I/O Lines
         Using the GMAC I/O lines requires the I/O pins to be configured using the port configuration (PORT).
         Related Links
         6. I/O Multiplexing and Considerations
         32. PORT - I/O Pin Controller

24.5.2   Power Management
         The GMAC continues to operate in IDLE and Standby sleep modes if REF_CLK or GRXCK is running.
         All GMAC interrupts can be used to wake up the device from IDLE sleep mode.
         In Standby sleep mode, only the WOL interrupt can wake up the CPU, and the corresponding ISR flags
         will not be set.
         Related Links
         18. PM – Power Manager

24.5.3   Clocks
         The GMAC peripheral relies on a system clock from the Main Clock Controller (MCLK) for register access
         and GMAC MCK.
         In MII mode, the actual Transmit or Reference Clock (GTXCK) and Receive Clock (GRXCK) are external
         signals.
         In RMII mode, the actual Reference Clock (REF_CLK) are external signals.
         The respective pins are configured in the PORT peripheral.
         Related Links
         6. I/O Multiplexing and Considerations
         32. PORT - I/O Pin Controller

24.5.4   Interrupt Sources
         The GMAC interrupt line is connected to the interrupt controller. Using the GMAC interrupt requires to
         configure the interrupt controller first.
         Related Links
         10.2 Nested Vector Interrupt Controller

24.5.5   Events
         The event GMAC Timestamp Comparison is connected to the Event System.
         Related Links




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 479
                                                           SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

         31. EVSYS – Event System


24.6     Functional Description

24.6.1   Media Access Controller
         The Transmit Block of the Media Access Controller (MAC) takes data from FIFO, adds preamble, checks
         and adds padding and frame check sequence (FCS). Both half duplex and full duplex Ethernet modes of
         operation are supported.
         When operating in half duplex mode, the MAC Transmit Block generates data according to the Carrier
         Sense Multiple Access with Collision Detect (CSMA/CD) protocol. The start of transmission is deferred if
         Carrier Sense (CRS) is active. If Collision (COL) is detected during transmission, a jam sequence is
         asserted and the transmission is retried after a random back off. The CRS and COL signals have no
         effect in full duplex mode.
         The Receive Block of the MAC checks for valid preamble, FCS, alignment and length, and presents
         received frames to the MAC address checking block and FIFO. Software can configure the GMAC to
         receive jumbo frames of up to 10240 Bytes. It can optionally strip CRC (Cyclic Redundancy Check) from
         the received frame before transferring it to FIFO.
         The Address Checker recognizes four specific 48-bit addresses, can recognize four different types of ID
         values, and contains a 64-bit Hash register for matching multicast and unicast addresses as required. It
         can recognize the broadcast address all-'1' (0xFFFFFFFFFFFF) and copy all frames. The MAC can also
         reject all frames that are not VLAN tagged, and recognize Wake on LAN events.
         The MAC Receive Block supports offloading of IP, TCP and UDP checksum calculations (both IPv4 and
         IPv6 packet types supported), and can automatically discard bad checksum frames.

24.6.2   IEEE 1588 Time Stamp Unit
         The IEEE 1588 time stamp unit (TSU) is implemented as a 94-bit timer.
           • The 48 upper bits [93:46] of the timer count seconds and are accessible in the GMAC 1588 Timer
             Seconds High Register” (TSH) and GMAC 1588 Timer Seconds Low Register (TSL).
           • The 30 lower bits [45:16] of the timer count nanoseconds and are accessible in the GMAC 1588
             Timer Nanoseconds Register (TN).
           • The lowest 16 bits [15:0] of the timer count sub-nanoseconds.
         The 46 lower bits roll over when they have counted to 1s. The timer increments by a programmable
         period (to approximately 15.2fs resolution) with each MCK period and can also be adjusted in 1ns
         resolution (incremented or decremented) through APB register accesses.

24.6.3   AHB Direct Memory Access Interface
         The GMAC DMA controller is connected to the MAC FIFO interface and provides a scatter-gather type
         capability for packet data storage.
         The DMA implements packet buffering where dual-port memories are used to buffer multiple frames.
24.6.3.1 Packet Buffer DMA
           • Easier to guarantee maximum line rate due to the ability to store multiple frames in the packet buffer,
             where the number of frames is limited by the amount of packet buffer memory and Ethernet frame
             size
           • Full store and forward, or partial store and forward programmable options (partial store will cater for
             shorter latency requirements)




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 480
                                                            SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

          • Support for Transmit TCP/IP checksum offload
          • Support for priority queuing
          • When a collision on the line occurs during transmission, the packet will be automatically replayed
            directly from the packet buffer memory rather than having to re-fetch through the AHB (full store and
            forward ONLY)
          • Received erroneous packets are automatically dropped before any of the packet is presented to the
            AHB (full store and forward ONLY), thus reducing AHB activity
          • Supports manual RX packet flush capabilities
          • Optional RX packet flush when there is lack of AHB resource
24.6.3.2 Partial Store and Forward Using Packet Buffer DMA
        The DMA uses SRAM-based packet buffers, and can be programmed into a low latency mode, known as
        Partial Store and Forward. This mode allows for a reduced latency as the full packet is not buffered
        before forwarding.
        Note: This option is only available when the device is configured for full duplex operation.
        This feature is enabled via the programmable TX and RX Partial Store and Forward registers (TPSF and
        RPSF). When the transmit Partial Store and Forward mode is activated, the transmitter will only begin to
        forward the packet to the MAC when there is enough packet data stored in the packet buffer. Likewise,
        when the receive Partial Store and Forward mode is activated, the receiver will only begin to forward the
        packet to the AHB when enough packet data is stored in the packet buffer. The amount of packet data
        required to activate the forwarding process is programmable via watermark registers. These registers are
        located at the same address as the partial store and forward enable bits.
        Note: The minimum operational value for the TX partial store and forward watermark is 20. There is no
        operational limit for the RX partial store and forward watermark.
        Enabling Partial Store and Forward is a useful means to reduce latency, but there are performance
        implications. The GMAC DMA uses separate transmit and receive lists of buffer descriptors, with each
        descriptor describing a buffer area in memory. This allows Ethernet packets to be broken up and
        scattered around the AHB memory space.
24.6.3.3 Receive AHB Buffers
        Received frames, optionally including FCS, are written to receive AHB buffers stored in memory. The
        receive buffer depth is programmable in the range of 64 Bytes to 16 KBytes through the DMA
        Configuration register (DCFGR), with the default being 128 Bytes.
        The start location for each receive AHB buffer is stored in memory in a list of receive buffer descriptors at
        an address location pointed to by the receive buffer queue pointer. The base address for the receive
        buffer queue pointer is configured in software using the Receive Buffer Queue Base Address register
        (RBQB).
        Each list entry consists of two words. The first is the address of the receive AHB buffer and the second
        the receive status.
        If the length of a receive frame exceeds the AHB buffer length, the status word for the used buffer is
        written with zeroes except for the “Start of Frame” bit, which is always set for the first buffer in a frame.
        Bit zero of the address field is written to 1 to show that the buffer has been used. The receive buffer
        manager then reads the location of the next receive AHB buffer and fills that with the next part of the
        received frame data. AHB buffers are filled until the frame is complete and the final buffer descriptor
        status word contains the complete frame status. See the following table for details of the receive buffer
        descriptor list.




        © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 481
                                                   SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

Table 24-2. Receive Buffer Descriptor Entry

 Bit     Function
 Word 0
 31:2    Address of beginning of buffer
 1       Wrap—marks last descriptor in receive buffer descriptor list.
 0       Ownership—needs to be zero for the GMAC to write data to the receive buffer. The GMAC sets
         this to one once it has successfully written a frame to memory.
         Software has to clear this bit before the buffer can be used again.

 Word 1
 31      Global all ones broadcast address detected
 30      Multicast hash match
 29      Unicast hash match
 28      –
 27      Specific Address Register match found, bit 25 and bit 26 indicate which Specific Address
         Register causes the match.
 26:25 Specific Address Register match. Encoded as follows:
       00: Specific Address Register 1 match
         01: Specific Address Register 2 match
         10: Specific Address Register 3 match
         11: Specific Address Register 4 match
         If more than one specific address is matched only one is indicated with priority 4 down to 1.

 24      This bit has a different meaning depending on whether RX checksum offloading is enabled.
         With RX checksum offloading disabled: (bit 24 clear in Network Configuration Register)
         Type ID register match found, bit 22 and bit 23 indicate which type ID register causes the match.
         With RX checksum offloading enabled: (bit 24 set in Network Configuration Register)
         0: The frame was not SNAP encoded and/or had a VLAN tag with the Canonical Format
         Indicator (CFI) bit set.
         1: The frame was SNAP encoded and had either no VLAN tag or a VLAN tag with the CFI bit not
         set.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 482
                                                      SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

...........continued
 Bit     Function
 23:22 This bit has a different meaning depending on whether RX checksum offloading is enabled.
       With RX checksum offloading disabled: (bit 24 clear in Network Configuration)
         Type ID register match. Encoded as follows:
         00: Type ID register 1 match
         01: Type ID register 2 match
         10: Type ID register 3 match
         11: Type ID register 4 match
         If more than one Type ID is matched only one is indicated with priority 4 down to 1.
         With RX checksum offloading enabled: (bit 24 set in Network Configuration Register)
         00: Neither the IP header checksum nor the TCP/UDP checksum was checked.
         01: The IP header checksum was checked and was correct. Neither the TCP nor UDP checksum
         was checked.
         10: Both the IP header and TCP checksum were checked and were correct.
         11: Both the IP header and UDP checksum were checked and were correct.

 21      VLAN tag detected—type ID of 0x8100. For packets incorporating the stacked VLAN processing
         feature, this bit will be set if the second VLAN tag has a type ID of 0x8100
 20      Priority tag detected—type ID of 0x8100 and null VLAN identifier. For packets incorporating the
         stacked VLAN processing feature, this bit will be set if the second VLAN tag has a type ID of
         0x8100 and a null VLAN identifier.
 19:17 VLAN priority—only valid if bit 21 is set.
 16      Canonical format indicator (CFI) bit (only valid if bit 21 is set).
 15      End of frame—when set the buffer contains the end of a frame. If end of frame is not set, then
         the only valid status bit is start of frame (bit 14).
 14      Start of frame—when set the buffer contains the start of a frame. If both bits 15 and 14 are set,
         the buffer contains a whole frame.
 13      This bit has a different meaning depending on whether jumbo frames and ignore FCS modes are
         enabled. If neither mode is enabled this bit will be zero.
         With jumbo frame mode enabled: (bit 3 set in Network Configuration Register) Additional bit for
         length of frame (bit[13]), that is concatenated with bits[12:0]
         With ignore FCS mode enabled and jumbo frames disabled: (bit 26 set in Network Configuration
         Register and bit 3 clear in Network Configuration Register) This indicates per frame FCS status
         as follows:
         0: Frame had good FCS
         1: Frame had bad FCS, but was copied to memory as ignore FCS enabled.




© 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 483
                                                    SAM D5x/E5x Family Data Sheet
                                                                                  GMAC - Ethernet MAC

...........continued
 Bit     Function
 12:0    These bits represent the length of the received frame which may or may not include FCS
         depending on whether FCS discard mode is enabled.
         With FCS discard mode disabled: (bit 17 clear in Network Configuration Register)
         Least significant 12 bits for length of frame including FCS. If jumbo frames are enabled, these 12
         bits are concatenated with bit[13] of the descriptor above.
         With FCS discard mode enabled: (bit 17 set in Network Configuration Register)
         Least significant 12 bits for length of frame excluding FCS. If jumbo frames are enabled, these
         12 bits are concatenated with bit[13] of the descriptor above.

Each receive AHB buffer start location is a word address. The start of the first AHB buffer in a frame can
be offset by up to three Bytes, depending on the value written to bits 14 and 15 of the Network
Configuration register (NCFGR). If the start location of the AHB buffer is offset, the available length of the
first AHB buffer is reduced by the corresponding number of Bytes.
To receive frames, the AHB buffer descriptors must be initialized by writing an appropriate address to bits
31:2 in the first word of each list entry. Bit 0 must be written with zero. Bit 1 is the wrap bit and indicates
the last entry in the buffer descriptor list.
The start location of the receive buffer descriptor list must be written with the receive buffer queue base
address before reception is enabled (receive enable in the Network Control register NCR). Once
reception is enabled, any writes to the Receive Buffer Queue Base Address register (RBQB) are ignored.
When read, it will return the current pointer position in the descriptor list, though this is only valid and
stable when receive is disabled.
If the filter block indicates that a frame should be copied to memory, the receive data DMA operation
starts writing data into the receive buffer. If an error occurs, the buffer is recovered.
An internal counter within the GMAC represents the receive buffer queue pointer and it is not visible
through the CPU interface. The receive buffer queue pointer increments by two words after each buffer
has been used. It re-initializes to the receive buffer queue base address if any descriptor has its wrap bit
set.
As receive AHB buffers are used, the receive AHB buffer manager sets bit zero of the first word of the
descriptor to logic one indicating the AHB buffer has been used.
Software should search through the “used” bits in the AHB buffer descriptors to find out how many frames
have been received, checking the start of frame and end of frame bits.
When the DMA is configured in the packet buffer Partial Store And Forward mode, received frames are
written out to the AHB buffers as soon as enough frame data exists in the packet buffer. For both cases,
this may mean several full AHB buffers are used before some error conditions can be detected. If a
receive error is detected the receive buffer currently being written will be recovered. Previous buffers will
not be recovered. As an example, when receiving frames with cyclic redundancy check (CRC) errors or
excessive length, it is possible that a frame fragment might be stored in a sequence of AHB receive
buffers. Software can detect this by looking for start of frame bit set in a buffer following a buffer with no
end of frame bit set.
To function properly, a 10/100 Ethernet system should have no excessive length frames or frames greater
than 128 Bytes with CRC errors. Collision fragments will be less than 128 Bytes long, therefore it will be a




© 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 484
                                                            SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

        rare occurrence to find a frame fragment in a receive AHB buffer, when using the default value of 128
        Bytes for the receive buffers size.
        When in packet buffer full store and forward mode, only good received frames are written out of the DMA,
        so no fragments will exist in the AHB buffers due to MAC receiver errors. There is still the possibility of
        fragments due to DMA errors, for example used bit read on the second buffer of a multi-buffer frame.
        If bit zero of the receive buffer descriptor is already set when the receive buffer manager reads the
        location of the receive AHB buffer, the buffer has been already used and cannot be used again until
        software has processed the frame and cleared bit zero. In this case, the “buffer not available” bit in the
        receive status register is set and an interrupt triggered. The receive resource error statistics register is
        also incremented.
        When the DMA is configured in the packet buffer full store and forward mode, the user can optionally
        select whether received frames should be automatically discarded when no AHB buffer resource is
        available. This feature is selected via the DMA Discard Receive Packets bit in the DMA Configuration
        register (DCFGR.DDRP). By default, the received frames are not automatically discarded. If this feature is
        off, then received packets will remain to be stored in the SRAM-based packet buffer until AHB buffer
        resource next becomes available. This may lead to an eventual packet buffer overflow if packets continue
        to be received when bit zero (used bit) of the receive buffer descriptor remains set.
        Note: After a used bit has been read, the receive buffer manager will re-read the location of the receive
        buffer descriptor every time a new packet is received. When the DMA is not configured in the packet
        buffer full store and forward mode and a used bit is read, the frame currently being received will be
        automatically discarded.
        When the DMA is configured in the packet buffer full store and forward mode, a receive overrun condition
        occurs when the receive SRAM-based packet buffer is full, or because HRESP was not OK. In all other
        modes, a receive overrun condition occurs when either the AHB bus was not granted quickly enough, or
        because HRESP was not OK, or because a new frame has been detected by the receive block, but the
        status update or write back for the previous frame has not yet finished. For a receive overrun condition,
        the receive overrun interrupt is asserted and the buffer currently being written is recovered. The next
        frame that is received whose address is recognized reuses the buffer.
        In any packet buffer mode, writing a '1' to the Flush Next Package bit in the NCR register (NCR.FNP) will
        force a packet from the external SRAM-based receive packet buffer to be flushed. This feature is only
        acted upon when the RX DMA is not currently writing packet data out to AHB, i.e., it is in an IDLE state. If
        the RX DMA is active, NCR.FNP=1 is ignored.

24.6.3.4 Transmit AHB Buffers
        Frames to transmit are stored in one or more transmit AHB buffers. Transmit frames can be between 1
        and 16384 Bytes long, so it is possible to transmit frames longer than the maximum length specified in
        the IEEE 802.3 standard. It should be noted that zero length AHB buffers are allowed and that the
        maximum number of buffers permitted for each transmit frame is 128.
        The start location for each transmit AHB buffer is stored in memory in a list of transmit buffer descriptors
        at a location pointed to by the transmit buffer queue pointer. The base address for this queue pointer is
        set in software using the Transmit Buffer Queue Base Address register. Each list entry consists of two
        words. The first is the Byte address of the transmit buffer and the second containing the transmit control
        and status. For the packet buffer DMA, the start location for each AHB buffer is a Byte address, the
        bottom bits of the address being used to offset the start of the data from the data-word boundary (i.e., bits
        2,1 and 0 are used to offset the address for 64-bit data paths).
        Frames can be transmitted with or without automatic Cyclic Redundancy Checksum (CRC) generation. If
        CRC is automatically generated, pad will also be automatically generated to take frames to a minimum




        © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 485
                                                     SAM D5x/E5x Family Data Sheet
                                                                                 GMAC - Ethernet MAC

length of 64 Bytes. When CRC is not automatically generated (as defined in word 1 of the transmit buffer
descriptor), the frame is assumed to be at least 64 Bytes long and pad is not generated.
An entry in the transmit buffer descriptor list is described in this table:
Table 24-3. Transmit Buffer Descriptor Entry

 Bit     Function
 Word 0
 31:0    Byte address of buffer
 Word 1
 31      Used—must be zero for the GMAC to read data to the transmit buffer. The GMAC sets this to
         one for the first buffer of a frame once it has been successfully transmitted. Software must clear
         this bit before the buffer can be used again.
 30      Wrap—marks last descriptor in transmit buffer descriptor list. This can be set for any buffer within
         the frame.
 29      Retry limit exceeded, transmit error detected
 28      Reserved.

 27      Transmit frame corruption due to AHB error—set if an error occurs while midway through reading
         transmit frame from the AHB, including HRESP errors and buffers exhausted mid frame (if the
         buffers run out during transmission of a frame then transmission stops, FCS shall be bad and
         GTXER asserted).
         Also set if single frame is too large for configured packet buffer memory size.

 26      Late collision, transmit error detected.
 25:23 Reserved
 22:20 Transmit IP/TCP/UDP checksum generation offload errors:
       000: No Error.
         001: The Packet was identified as a VLAN type, but the header was not fully complete, or had an
         error in it.
         010: The Packet was identified as a SNAP type, but the header was not fully complete, or had an
         error in it.
         011: The Packet was not of an IP type, or the IP packet was invalidly short, or the IP was not of
         type IPv4/IPv6.
         100: The Packet was not identified as VLAN, SNAP or IP.
         101: Non supported packet fragmentation occurred. For IPv4 packets, the IP checksum was
         generated and inserted.
         110: Packet type detected was not TCP or UDP. TCP/UDP checksum was therefore not
         generated. For IPv4 packets, the IP checksum was generated and inserted.
         111: A premature end of packet was detected and the TCP/UDP checksum could not be
         generated.

 19:17 Reserved




© 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 486
                                                     SAM D5x/E5x Family Data Sheet
                                                                                    GMAC - Ethernet MAC

...........continued
 Bit      Function
 16       No CRC to be appended by MAC. When set, this implies that the data in the buffers already
          contains a valid CRC, hence no CRC or padding is to be appended to the current frame by the
          MAC.
          This control bit must be set for the first buffer in a frame and will be ignored for the subsequent
          buffers of a frame.
          Note that this bit must be clear when using the transmit IP/TCP/UDP checksum generation
          offload, otherwise checksum generation and substitution will not occur.

 15       Last buffer, when set this bit will indicate the last buffer in the current frame has been reached.
 14       Reserved
 13:0     Length of buffer

To transmit frames, the buffer descriptors must be initialized by writing an appropriate Byte address to bits
[31:0] of the first word of each descriptor list entry.
The second word of the transmit buffer descriptor is initialized with control information that indicates the
length of the frame, whether or not the MAC is to append CRC and whether the buffer is the last buffer in
the frame.
After transmission the status bits are written back to the second word of the first buffer along with the
used bit. Bit 31 is the used bit which must be zero when the control word is read if transmission is to take
place. It is written to '1' once the frame has been transmitted. Bits[29:20] indicate various transmit error
conditions. Bit 30 is the wrap bit which can be set for any buffer within a frame. If no wrap bit is
encountered the queue pointer continues to increment.
The Transmit Buffer Queue Base Address register can only be updated while transmission is disabled or
halted; otherwise any attempted write will be ignored. When transmission is halted the transmit buffer
queue pointer will maintain its value. Therefore when transmission is restarted the next descriptor read
from the queue will be from immediately after the last successfully transmitted frame. As long as transmit
is disabled by writing a '0' to the Transmit Enable bit in the Network Control register (NCR.TXEN), the
transmit buffer queue pointer resets to point to the address indicated by the Transmit Buffer Queue Base
Address register (TBQB).
Note: Disabling receive does not have the same effect on the receive buffer queue pointer.
Once the transmit queue is initialized, transmit is activated by writing a '1' to the Start Transmission bit of
the Network Control register (NCR.TSTART). Transmit is halted when a buffer descriptor with its used bit
set is read, a transmit error occurs, or by writing to the Transmit Halt bit of the Network Control register
(NCR.THALT). Transmission is suspended if a pause frame is received while the Transmit Pause Frame
bit is '1' in the Network Configuration register (NCR.TXPF). Rewriting the Start bit (NCR.TSTART) while
transmission is active is allowed. This is implemented by the Transmit Go variable which is readable in
the Transmit Status register (TSR.TXGO). The TXGO variable is reset when:
  •    Transmit is disabled.
  •    A buffer descriptor with its ownership bit set is read.
  •    Bit 10, THALT, of the Network Control register is written.
  •    There is a transmit error such as too many retries or a transmit underrun.




© 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 487
                                                           SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

        To set TXGO, write a '1' to NCR.TSTART. Transmit halt does not take effect until any ongoing transmit
        finishes.
        If the DMA is configured for packet buffer Partial Store and Forward mode and a collision occurs during
        transmission of a multi-buffer frame, transmission will automatically restart from the first buffer of the
        frame. For packet buffer mode, the entire contents of the frame are read into the transmit packet buffer
        memory, so the retry attempt will be replayed directly from the packet buffer memory rather than having to
        re-fetch through the AHB.
        If a used bit is read midway through transmission of a multi-buffer frame, this is treated as a transmit
        error. Transmission stops, GTXER is asserted and the FCS will be bad.
        If transmission stops due to a transmit error or a used bit being read, transmission restarts from the first
        buffer descriptor of the frame being transmitted when the transmit start bit is rewritten.
24.6.3.5 DMA Bursting on the AHB
        The DMA will always use SINGLE, or INCR type AHB accesses for buffer management operations. When
        performing data transfers, the AHB burst length is selected by the Fixed Burst Length for DMA Data
        Operations bit field in the DMA Configuration register (DCFGR.FBLDO) so that either SINGLEor fixed
        length incrementing bursts (INCR4, INCR8 or INCR16) are used where possible:
        When there is enough space and enough data to be transferred, the programmed fixed length bursts will
        be used. If there is not enough data or space available, for example when at the beginning or the end of a
        buffer, SINGLE type accesses are used. Also SINGLE type accesses are used at 1024 Byte boundaries,
        so that the 1 KByte boundaries are not burst over as per AHB requirements.
        The DMA will not terminate a fixed length burst early, unless an error condition occurs on the AHB or if
        receive or transmit are disabled in the Network Control register (NCR).
24.6.3.6 DMA Packet Buffer
        The DMA uses packet buffers for both transmit and receive paths. This mode allows multiple packets to
        be buffered in both transmit and receive directions. This allows the DMA to withstand far greater access
        latencies on the AHB and make more efficient use of the AHB bandwidth. There are two modes of
        operation—Full Store and Forward and Partial Store and Forward.
        As described above, the DMA can be programmed into a low latency mode, known as Partial Store and
        Forward. For further details of this mode, see the related Links.
        When the DMA is in full store and forward mode, full packets are buffered which provides the possibility
        to:
          • Discard packets with error on the receive path before they are partially written out of the DMA, thus
            saving AHB bus bandwidth and driver processing overhead,
          • Retry collided transmit frames from the buffer, thus saving AHB bus bandwidth,
          • Implement transmit IP/TCP/UDP checksum generation offload.
        With the packet buffers included, the structure of the GMAC data paths is shown in this image:




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 488
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                 GMAC - Ethernet MAC

         Figure 24-2. Data Paths with Packet Buffers Included

                                                                                                      TX GMII
                                                                              MAC Transmitter




                                                                                                                TX Packet
                                                                TX Packet
                                                                                                                  Buffer
                                                                  Buffer
                                                                                                                DPSRAM




                                                                                TX DMA
                          APB                  Status
                                  Register       and                                                            AHB
                                                                                                AHB
                                  Interface    Statistic                                        DMA
                                              Registers
                                                                                RX DMA




                          MDIO                                                                                  RX Packet
                                                                RX Packet
                                   Control                                                                       Buffer
                                                                 Buffer
                                  Interface                                                                     DPSRAM




                                                                                                      RX GMII
                                                                            MAC Receiver




                                                                            Frame Filtering
                                                           Ethernet MAC


24.6.3.7 Transmit Packet Buffer
         The transmitter packet buffer will continue attempting to fetch frame data from the AHB system memory
         until the packet buffer itself is full, at which point it will attempt to maintain its full level.
         To accommodate the status and statistics associated with each frame, three words per packet (or two if
         the GMAC is configured in 64-bit data path mode) are reserved at the end of the packet data. If the
         packet is bad and requires to be dropped, the status and statistics are the only information held on that
         packet. Storing the status in the DPRAM is required in order to decouple the DMA interface of the buffer
         from the MAC interface, to update the MAC status/statistics and to generate interrupts in the order in
         which the packets that they represent were fetched from the AHB memory.
         If any errors occur on the AHB while reading the transmit frame, the fetching of packet data from AHB
         memory is halted. The MAC transmitter will continue to fetch packet data, thereby emptying the packet
         buffer and allowing any good (non-erroneous) frames to be transmitted successfully. Once these have
         been fully transmitted, the status/statistics for the erroneous frame will be updated and software will be
         informed via an interrupt that an AHB error occurred. This way, the error is reported in the correct packet
         order.
         The transmit packet buffer will only attempt to read more frame data from the AHB when space is
         available in the packet buffer memory. If space is not available it must wait until the a packet fetched by
         the MAC completes transmission and is subsequently removed from the packet buffer memory.




        © 2019 Microchip Technology Inc.                          Datasheet                                     DS60001507E-page 489
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

        Note: If full store and forward mode is active and if a single frame is fetched that is too large for the
        packet buffer memory, the frame is flushed and the DMA halted with an error status. This is because a
        complete frame must be written into the packet buffer before transmission can begin, and therefore the
        minimum packet buffer memory size should be chosen to satisfy the maximum frame to be transmitted in
        the application.
        In full store and forward mode, once the complete transmit frame is written into the packet buffer memory,
        a trigger is sent across to the MAC transmitter, which will then begin reading the frame from the packet
        buffer memory. Since the whole frame is present and stable in the packet buffer memory an underflow of
        the transmitter is not possible. The frame is kept in the packet buffer until notification is received from the
        MAC that the frame data has either been successfully transmitted or can no longer be retransmitted (too
        many retries in half duplex mode). When this notification is received the frame is flushed from memory to
        make room for a new frame to be fetched from AHB system memory.
        In Partial Store and Forward mode, a trigger is sent across to the MAC transmitter as soon as sufficient
        packet data is available, which will then begin fetching the frame from the packet buffer memory. If, after
        this point, the MAC transmitter is able to fetch data from the packet buffer faster than the AHB DMA can
        fill it, an underflow of the transmitter is possible. In this case, the transmission is terminated early, and the
        packet buffer is completely flushed. Transmission can only be restarted by writing a '1' to the Transmit
        Start bit in the Network Control register (NCR.TSTART).
        In half duplex mode, the frame is kept in the packet buffer until notification is received from the MAC that
        the frame data has either been successfully transmitted or can no longer be retransmitted (too many
        retries in half duplex mode). When this notification is received the frame is flushed from memory to make
        room for a new frame to be fetched from AHB system memory.
        In full duplex mode, the frame is removed from the packet buffer on the fly.
        Other than underflow, the only MAC related errors that can occur are due to collisions during half duplex
        transmissions. When a collision occurs the frame still exists in the packet buffer memory so can be retried
        directly from there. After sixteen failed transmit attempts, the frame will be flushed from the packet buffer.

24.6.3.8 Receive Packet Buffer
        The receive packet buffer stores frames from the MAC receiver along with their status and statistics.
        Frames with errors are flushed from the packet buffer memory, while good frames are pushed onto the
        DMA AHB interface.
        The receiver packet buffer monitors the FIFO write interface from the MAC receiver and translates the
        FIFO pushes into packet buffer writes. At the end of the received frame the status and statistics are
        buffered so that the information can be used when the frame is read out. When programmed in full store
        and forward mode and the frame has an error, the frame data is immediately flushed from the packet
        buffer memory allowing subsequent frames to utilize the freed up space. The status and statistics for bad
        frames are still used to update the GMAC registers.
        To accommodate the status and statistics associated with each frame, three words per packet (or two if
        configured in 64-bit datapath mode) are reserved at the end of the packet data. If the packet is bad and
        requires to be dropped, the status and statistics are the only information held on that packet.
        The receiver packet buffer will also detect a full condition so that an overflow condition can be detected. If
        this occurs, subsequent packets are dropped and an RX overflow interrupt is raised.
        For full store and forward, the DMA only begins packet fetches once the status and statistics for a frame
        are available. If the frame has a bad status due to a frame error, the status and statistics are passed on to
        the GMAC registers. If the frame has a good status, the information is used to read the frame from the
        packet buffer memory and burst onto the AHB using the DMA buffer management protocol. Once the last




        © 2019 Microchip Technology Inc.                      Datasheet                             DS60001507E-page 490
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

         frame data has been transferred to the packet buffer, the status and statistics are updated to the GMAC
         registers.
         If Partial Store and Forward mode is active, the DMA will begin fetching the packet data before the status
         is available. As soon as the status becomes available, the DMA will fetch this information as soon as
         possible before continuing to fetch the remainder of the frame. Once the last frame data has been
         transferred to the packet buffer, the status and statistics are updated to the GMAC registers.

24.6.4   MAC Transmit Block
         The MAC transmitter can operate in either half duplex or full duplex mode and transmits frames in
         accordance with the Ethernet IEEE 802.3 standard. In half duplex mode, the CSMA/CD protocol of the
         IEEE 802.3 specification is followed.
         A small input buffer receives data through the FIFO interface which will extract data in 32-bit form. All
         subsequent processing prior to the final output is performed in bytes.
         Transmit data can be output using the MII interface.
         Frame assembly starts by adding preamble and the start frame delimiter. Data is taken from the transmit
         FIFO interface a word at a time.
         If necessary, padding is added to take the frame length to 60 bytes. CRC is calculated using an order 32-
         bit polynomial. This is inverted and appended to the end of the frame taking the frame length to a
         minimum of 64 bytes. If the no CRC bit is set in the second word of the last buffer descriptor of a transmit
         frame, neither pad nor CRC are appended. The no CRC bit can also be set through the FIFO interface.
         In full duplex mode (at all data rates), frames are transmitted immediately. Back to back frames are
         transmitted at least 96 bit times apart to guarantee the interframe gap.
         In half duplex mode, the transmitter checks carrier sense. If asserted, the transmitter waits for the signal
         to become inactive, and then starts transmission after the interframe gap of 96 bit times. If the collision
         signal is asserted during transmission, the transmitter will transmit a jam sequence of 32 bits taken from
         the data register and then retry transmission after the back off time has elapsed. If the collision occurs
         during either the preamble or Start Frame Delimiter (SFD), then these fields will be completed prior to
         generation of the jam sequence.
         The back off time is based on an XOR of the 10 least significant bits of the data coming from the transmit
         FIFO interface and a 10-bit pseudo random number generator. The number of bits used depends on the
         number of collisions seen. After the first collision 1 bit is used, then the second 2 bits and so on up to the
         maximum of 10 bits. All 10 bits are used above ten collisions. An error will be indicated and no further
         attempts will be made if 16 consecutive attempts cause collision. This operation is compliant with the
         description in Clause 4.2.3.2.5 of the IEEE 802.3 standard which refers to the truncated binary
         exponential back off algorithm.
         In 10/100 mode, both collisions and late collisions are treated identically, and back off and retry will be
         performed up to 16 times. This condition is reported in the transmit buffer descriptor word 1 (late collision,
         bit 26) and also in the Transmit Status register (late collision, bit 7). An interrupt can also be generated (if
         enabled) when this exception occurs, and bit 5 in the Interrupt Status register will be set.
         In all modes of operation, if the transmit DMA underruns, a bad CRC is automatically appended using the
         same mechanism as jam insertion and the GTXER signal is asserted. For a properly configured system
         this should never happen and also it is impossible if configured to use the DMA with packet buffers, as
         the complete frame is buffered in local packet buffer memory.




         © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 491
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

         By setting when bit 28 is set in the Network Configuration register, the Inter Packet Gap (IPG) may be
         stretched beyond 96 bits depending on the length of the previously transmitted frame and the value
         written to the IPG Stretch register (IPGS). The least significant 8 bits of the IPG Stretch register multiply
         the previous frame length (including preamble). The next significant 8 bits (+1 so as not to get a divide by
         zero) divide the frame length to generate the IPG. IPG stretch only works in full duplex mode and when
         bit 28 is set in the Network Configuration register. The IPG Stretch register cannot be used to shrink the
         IPG below 96 bits.
         If the back pressure bit is set in the Network Control register, or if the HDFC configuration bit is set in the
         UR register (10M or 100M half duplex mode), the transmit block transmits 64 bits of data, which can
         consist of 16 nibbles of 1011 or in bit rate mode 64 1s, whenever it sees an incoming frame to force a
         collision. This provides a way of implementing flow control in half duplex mode.

24.6.5   MAC Receive Block
         All processing within the MAC receive block is implemented using a 16-bit data path. The MAC receive
         block checks for valid preamble, FCS, alignment and length, presents received frames to the FIFO
         interface and stores the frame destination address for use by the address checking block.
         If, during the frame reception, the frame is found to be too long, a bad frame indication is sent to the FIFO
         interface. The receiver logic ceases to send data to memory as soon as this condition occurs.
         At end of frame reception the receive block indicates to the DMA block whether the frame is good or bad.
         The DMA block will recover the current receive buffer if the frame was bad.
         Ethernet frames are normally stored in DMA memory complete with the FCS. Setting the FCS remove bit
         in the network configuration (bit 17) causes frames to be stored without their corresponding FCS. The
         reported frame length field is reduced by four bytes to reflect this operation.
         The receive block signals to the register block to increment the alignment, CRC (FCS), short frame, long
         frame, jabber or receive symbol errors when any of these exception conditions occur.
         If bit 26 is set in the network configuration, CRC errors will be ignored and CRC errored frames will not be
         discarded, though the Frame Check Sequence Errors statistic register will still be incremented.
         Additionally, if not enabled for jumbo frames mode, then bit[13] of the receiver descriptor word 1 will be
         updated to indicate the FCS validity for the particular frame. This is useful for applications such as
         EtherCAT whereby individual frames with FCS errors must be identified.
         Received frames can be checked for length field error by setting the length field error frame discard bit of
         the Network Configuration register (bit-16). When this bit is set, the receiver compares a frame's
         measured length with the length field (bytes 13 and 14) extracted from the frame. The frame is discarded
         if the measured length is shorter. This checking procedure is for received frames between 64 bytes and
         1518 bytes in length.
         Each discarded frame is counted in the 10-bit length field error statistics register. Frames where the
         length field is greater than or equal to 0x0600 hex will not be checked.

24.6.6   Checksum Offload for IP, TCP and UDP
         The GMAC can be programmed to perform IP, TCP and UDP checksum offloading in both receive and
         transmit directions, which is enabled by setting bit 24 in the Network Configuration register for receive
         and bit 11 in the DMA Configuration register for transmit.
         IPv4 packets contain a 16-bit checksum field, which is the 16-bit 1’s complement of the 1’s complement
         sum of all 16-bit words in the header. TCP and UDP packets contain a 16-bit checksum field, which is the
         16-bit 1’s complement of the 1’s complement sum of all 16-bit words in the header, the data and a
         conceptual IP pseudo header.




         © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 492
                                                           SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

        To calculate these checksums in software requires each byte of the packet to be processed. For TCP and
        UDP this can use a large amount of processing power. Offloading the checksum calculation to hardware
        can result in significant performance improvements.
        For IP, TCP or UDP checksum offload to be useful, the operating system containing the protocol stack
        must be aware that this offload is available so that it can make use of the fact that the hardware can
        either generate or verify the checksum.

24.6.6.1 Receiver Checksum Offload
        When receive checksum offloading is enabled in the GMAC Network Configuration Register
        (NCFGR.RXCOEN), the IPv4 header checksum is checked as per RFC 791, where the packet meets the
        following criteria:
          •   If present, the VLAN header must be four octets long and the CFI bit must not be set.
          •   Encapsulation must be RFC 894 Ethernet Type Encoding or RFC 1042 SNAP Encoding.
          •   IPv4 packet
          •   IP header is of a valid length
        The GMAC also checks the TCP checksum as per RFC 793, or the UDP checksum as per RFC 768, if
        the following criteria are met:
          •   IPv4 or IPv6 packet
          •   Good IP header checksum (if IPv4)
          •   No IP fragmentation
          •   TCP or UDP packet
        When an IP, TCP or UDP frame is received, the receive buffer descriptor gives an indication if the GMAC
        was able to verify the checksums. There is also an indication if the frame had SNAP encapsulation.
        These indication bits will replace the type ID match indication bits when the receive checksum offload is
        enabled. For details of these indication bits refer to “Receive Buffer Descriptor Entry”.
        If any of the checksums are verified as incorrect by the GMAC, the packet is discarded and the
        appropriate statistics counter incremented.

24.6.6.2 Transmitter Checksum Offload
        The transmitter checksum offload is only available if the full store and forward mode is enabled. This is
        because the complete frame to be transmitted must be read into the packet buffer memory before the
        checksum can be calculated and written back into the headers at the beginning of the frame.
        Transmitter checksum offload is enabled by setting bit [11] in the DMA Configuration register. When
        enabled, it will monitor the frame as it is written into the transmitter packet buffer memory to automatically
        detect the protocol of the frame. Protocol support is identical to the receiver checksum offload.
        For transmit checksum generation and substitution to occur, the protocol of the frame must be recognized
        and the frame must be provided without the FCS field, by making sure that bit [16] of the transmit
        descriptor word 1 is clear. If the frame data already had the FCS field, this would be corrupted by the
        substitution of the new checksum fields.
        If these conditions are met, the transmit checksum offload engine will calculate the IP, TCP and UDP
        checksums as appropriate. Once the full packet is completely written into packet buffer memory, the
        checksums will be valid and the relevant DPRAM locations will be updated for the new checksum fields
        as per standard IP/TCP and UDP packet structures.
        If the transmitter checksum engine is prevented from generating the relevant checksums, bits [22:20] of
        the transmitter DMA writeback status will be updated to identify the reason for the error. Note that the




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 493
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

         frame will still be transmitted but without the checksum substitution, as typically the reason that the
         substitution did not occur was that the protocol was not recognized.

24.6.7   MAC Filtering Block
         The filter block determines which frames should be written to the FIFO interface and on to the DMA.
         Whether a frame is passed depends on what is enabled in the Network Configuration register, the state of
         the external matching pins, the contents of the specific address, type and Hash registers and the frame's
         destination address and type field.
         If bit 25 of the Network Configuration register is not set, a frame will not be copied to memory if the GMAC
         is transmitting in half duplex mode at the time a destination address is received.
         Ethernet frames are transmitted a byte at a time, least significant bit first. The first six bytes (48 bits) of an
         Ethernet frame make up the destination address. The first bit of the destination address, which is the LSB
         of the first byte of the frame, is the group or individual bit. This is one for multicast addresses and zero for
         unicast. The all ones address is the broadcast address and a special case of multicast.
         The GMAC supports recognition of four specific addresses. Each specific address requires two registers,
         Specific Address register Bottom and Specific Address register Top. Specific Address register Bottom
         stores the first four bytes of the destination address and Specific Address register Top contains the last
         two bytes. The addresses stored can be specific, group, local or universal.
         The destination address of received frames is compared against the data stored in the Specific Address
         registers once they have been activated. The addresses are deactivated at reset or when their
         corresponding Specific Address register Bottom is written. They are activated when Specific Address
         register Top is written. If a receive frame address matches an active address, the frame is written to the
         FIFO interface and on to DMA memory.
         Frames may be filtered using the type ID field for matching. Four type ID registers exist in the register
         address space and each can be enabled for matching by writing a one to the MSB (bit 31) of the
         respective register. When a frame is received, the matching is implemented as an OR function of the
         various types of match.
         The contents of each type ID register (when enabled) are compared against the length/type ID of the
         frame being received (e.g., bytes 13 and 14 in non-VLAN and non-SNAP encapsulated frames) and
         copied to memory if a match is found. The encoded type ID match bits (Word 0, Bit 22 and Bit 23) in the
         receive buffer descriptor status are set indicating which type ID register generated the match, if the
         receive checksum offload is disabled.
         The reset state of the type ID registers is zero, hence each is initially disabled.
         The following example illustrates the use of the address and type ID match registers for a MAC address
         of 21:43:65:87:A9:CB:

          Preamble                                                         55
          SFD                                                              D5
          DA (Octet 0 - LSB)                                               21
          DA (Octet 1)                                                     43
          DA (Octet 2)                                                     65
          DA (Octet 3)                                                     87




         © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 494
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

          DA (Octet 4)                                                      A9
          DA (Octet 5 - MSB)                                                CB
          SA (LSB)                                                          00 (see Note)
          SA                                                                00(see Note)
          SA                                                                00(see Note)
          SA                                                                00(see Note)
          SA                                                                00(see Note)
          SA (MSB)                                                          00(see Note)
          Type ID (MSB)                                                     43
          Type ID (LSB)                                                     21

         Note: Contains the address of the transmitting device.
         The previous sequence shows the beginning of an Ethernet frame. Byte order of transmission is from top
         to bottom, as shown. For a successful match to specific address 1, the following address matching
         registers must be set up:
         Specific Address 1 Bottom register (SAB1) (Address 0x088) 0x87654321
         Specific Address 1 Top register (SAT1) (Address 0x08C) 0x0000CBA9
         For a successful match to the type ID, the following Type ID Match 1 register must be set up:
         Type ID Match 1 register (TIDM1) (Address 0x0A8) 0x80004321

24.6.8   Broadcast Address
         Frames with the broadcast address of 0xFFFFFFFFFFFF are stored to memory only if the 'no broadcast'
         bit in the Network Configuration register is set to zero.

24.6.9   Hash Addressing
         The hash address register is 64 bits long and takes up two locations in the memory map. The least
         significant bits are stored in Hash Register Bottom and the most significant bits in Hash Register Top.
         The unicast hash enable and the multicast hash enable bits in the Network Configuration register enable
         the reception of hash matched frames. The destination address is reduced to a 6-bit index into the 64-bit
         Hash register using the following hash function: The hash function is an XOR of every sixth bit of the
         destination address.
         hash_index[05] = da[05] ^ da[11] ^ da[17] ^ da[23] ^ da[29] ^ da[35] ^ da[41] ^ da[47]
         hash_index[04] = da[04] ^ da[10] ^ da[16] ^ da[22] ^ da[28] ^ da[34] ^ da[40] ^ da[46]
         hash_index[03] = da[03] ^ da[09] ^ da[15] ^ da[21] ^ da[27] ^ da[33] ^ da[39] ^ da[45]
         hash_index[02] = da[02] ^ da[08] ^ da[14] ^ da[20] ^ da[26] ^ da[32] ^ da[38] ^ da[44]
         hash_index[01] = da[01] ^ da[07] ^ da[13] ^ da[19] ^ da[25] ^ da[31] ^ da[37] ^ da[43]
         hash_index[00] = da[00] ^ da[06] ^ da[12] ^ da[18] ^ da[24] ^ da[30] ^ da[36] ^ da[42]
         da[0] represents the least significant bit of the first byte received, that is, the multicast/unicast indicator,
         and da[47] represents the most significant bit of the last byte received.




         © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 495
                                                               SAM D5x/E5x Family Data Sheet
                                                                                              GMAC - Ethernet MAC

         If the hash index points to a bit that is set in the Hash register then the frame will be matched according to
         whether the frame is multicast or unicast.
         A multicast match will be signaled if the multicast hash enable bit is set, da[0] is logic 1 and the hash
         index points to a bit set in the Hash register.
         A unicast match will be signaled if the unicast hash enable bit is set, da[0] is logic 0 and the hash index
         points to a bit set in the Hash register.
         To receive all multicast frames, the Hash register should be set with all ones and the multicast hash
         enable bit should be set in the Network Configuration register.

24.6.10 Copy all Frames (Promiscuous Mode)
        If the Copy All Frames bit is set in the Network Configuration register then all frames (except those that
        are too long, too short, have FCS errors or have GRXER asserted during reception) will be copied to
        memory. Frames with FCS errors will be copied if bit 26 is set in the Network Configuration register.

24.6.11 Disable Copy of Pause Frames
        Pause frames can be prevented from being written to memory by setting the disable copying of pause
        frames control bit 23 in the Network Configuration register. When set, pause frames are not copied to
        memory regardless of the Copy All Frames bit, whether a hash match is found, a type ID match is
        identified or if a destination address match is found.

24.6.12 VLAN Support
        The following table describes an Ethernet encoded 802.1Q VLAN tag.
         Table 24-4. 802.1Q VLAN Tag

          TPID (Tag Protocol Identifier) 16 bits            TCI (Tag Control Information) 16 bits
          0x8100                                            First 3 bits priority, then CFI bit, last 12 bits VID

         The VLAN tag is inserted at the 13th byte of the frame adding an extra four bytes to the frame. To support
         these extra four bytes, the GMAC can accept frame lengths up to 1536 bytes by setting bit 8 in the
         Network Configuration register.
         If the VID (VLAN identifier) is null (0x000) this indicates a priority-tagged frame.
         The following bits in the receive buffer descriptor status word give information about VLAN tagged
         frames:-
           • Bit 21 set if receive frame is VLAN tagged (i.e., type ID of 0x8100).
           • Bit 20 set if receive frame is priority tagged (i.e., type ID of 0x8100 and null VID). (If bit 20 is set, bit
             21 will be set also.)
           • Bit 19, 18 and 17 set to priority if bit 21 is set.
           • Bit 16 set to CFI if bit 21 is set.
         The GMAC can be configured to reject all frames except VLAN tagged frames by setting the discard non-
         VLAN frames bit in the Network Configuration register.

24.6.13 Wake on LAN Support
        The receive block supports Wake on LAN by detecting the following events on incoming receive frames:
           • Magic packet
           • Address Resolution Protocol (ARP) request to the device IP address




         © 2019 Microchip Technology Inc.                       Datasheet                              DS60001507E-page 496
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               GMAC - Ethernet MAC

         • Specific address 1 filter match
         • Multicast hash filter match
        These events can be individually enabled through bits [19:16] of the Wake on LAN register. Also, for
        Wake on LAN detection to occur, receive enable must be set in the Network Control register, however a
        receive buffer does not have to be available.
        In case of an ARP request, specific address 1 or multicast filter events will occur even if the frame is
        errored. For magic packet events, the frame must be correctly formed and error free.
        A magic packet event is detected if all of the following are true:
         •   Magic packet events are enabled through bit 16 of the Wake on LAN register
         •   The frame's destination address matches specific address 1
         •   The frame is correctly formed with no errors
         •   The frame contains at least 6 bytes of 0xFF for synchronization
         •   There are 16 repetitions of the contents of Specific Address 1 register immediately following the
             synchronization
        An ARP request event is detected if all of the following are true:
         •   ARP request events are enabled through bit 17 of the Wake on LAN register
         •   Broadcasts are allowed by bit 5 in the Network Configuration register
         •   The frame has a broadcast destination address (bytes 1 to 6)
         •   The frame has a type ID field of 0x0806 (bytes 13 and 14)
         •   The frame has an ARP operation field of 0x0001 (bytes 21 and 22)
         •   The least significant 16 bits of the frame's ARP target protocol address (bytes 41 and 42) match the
             value programmed in bits[15:0] of the Wake on LAN register
        The decoding of the ARP fields adjusts automatically if a VLAN tag is detected within the frame. The
        reserved value of 0x0000 for the Wake on LAN target address value will not cause an ARP request event,
        even if matched by the frame.
        A specific address 1 filter match event will occur if all of the following are true:
         • Specific address 1 events are enabled through bit 18 of the Wake on LAN register
         • The frame's destination address matches the value programmed in the Specific Address 1 registers
        A multicast filter match event will occur if all of the following are true:
         •   Multicast hash events are enabled through bit 19 of the Wake on LAN register
         •   Multicast hash filtering is enabled through bit 6 of the Network Configuration register
         •   The frame destination address matches against the multicast hash filter
         •   The frame destination address is not a broadcast

24.6.14 IEEE 1588 Support
        IEEE 1588 is a standard for precision time synchronization in local area networks. It works with the
        exchange of special Precision Time Protocol (PTP) frames. The PTP messages can be transported over
        IEEE 802.3/Ethernet, over Internet Protocol Version 4 or over Internet Protocol Version 6 as described in
        the annex of IEEE P1588.D2.1.
        GMAC output pins indicate the message time-stamp point (asserted on the start packet delimiter and de-
        asserted at end of frame) for all frames and the passage of PTP event frames (asserted when a PTP
        event frame is detected and de-asserted at end of frame).




       © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 497
                                                 SAM D5x/E5x Family Data Sheet
                                                                              GMAC - Ethernet MAC

IEEE 802.1AS is a subset of IEEE 1588. One difference is that IEEE 802.1AS uses the Ethernet multicast
address 0180C200000E for sync frame recognition whereas IEEE 1588 does not. GMAC is designed to
recognize sync frames with both IEEE 802.1AS and IEEE 1588 addresses and so can support both 1588
and 802.1AS frame recognition simultaneously.
Synchronization between master and slave clocks is a two stage process.
First, the offset between the master and slave clocks is corrected by the master sending a sync frame to
the slave with a follow up frame containing the exact time the sync frame was sent. Hardware assist
modules at the master and slave side detect exactly when the sync frame was sent by the master and
received by the slave. The slave then corrects its clock to match the master clock.
Second, the transmission delay between the master and slave is corrected. The slave sends a delay
request frame to the master which sends a delay response frame in reply. Hardware assist modules at
the master and slave side detect exactly when the delay request frame was sent by the slave and
received by the master. The slave will now have enough information to adjust its clock to account for
delay. For example, if the slave was assuming zero delay, the actual delay will be half the difference
between the transmit and receive time of the delay request frame (assuming equal transmit and receive
times) because the slave clock will be lagging the master clock by the delay time already.
The time-stamp is taken when the message time-stamp point passes the clock time-stamp point. This can
generate an interrupt if enabled (IER). However, MAC Filtering configuration is needed to actually ‘copy’
the message to memory. For Ethernet, the message time-stamp point is the SFD and the clock time-
stamp point is the MII interface. (The IEEE 1588 specification refers to sync and delay_req messages as
event messages as these require time-stamping. These events are captured in the registers TSSx, EFTx
and EFRx, respectively. Follow up, delay response and management messages do not require time-
stamping and are referred to as general messages.)
1588 version 2 defines two additional PTP event messages. These are the peer delay request
(Pdelay_Req) and peer delay response (Pdelay_Resp) messages. These events are captured in the
registers PEFTx and PEFRx, respectively. These messages are used to calculate the delay on a link.
Nodes at both ends of a link send both types of frames (regardless of whether they contain a master or
slave clock). The Pdelay_Resp message contains the time at which a Pdelay_Req was received and is
itself an event message. The time at which a Pdelay_Resp message is received is returned in a
Pdelay_Resp_Follow_Up message.
1588 version 2 introduces transparent clocks of which there are two kinds, peer-to-peer (P2P) and end-
to-end (E2E). Transparent clocks measure the transit time of event messages through a bridge and
amend a correction field within the message to allow for the transit time. P2P transparent clocks
additionally correct for the delay in the receive path of the link using the information gathered from the
peer delay frames. With P2P transparent clocks delay_req messages are not used to measure link delay.
This simplifies the protocol and makes larger systems more stable.
The GMAC recognizes four different encapsulations for PTP event messages:
 1. 1588 version 1 (UDP/IPv4 multicast)
 2. 1588 version 2 (UDP/IPv4 multicast)
 3. 1588 version 2 (UDP/IPv6 multicast)
 4. 1588 version 2 (Ethernet multicast)
Table 24-5. Example of Sync Frame in 1588 Version 1 Format

 Frame Segment                                                 Value
 Preamble/SFD                                                  55555555555555D5




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 498
                                           SAM D5x/E5x Family Data Sheet
                                                                       GMAC - Ethernet MAC

...........continued
 Frame Segment                                           Value
 DA (Octets 0–5)                                         —
 SA (Octets 6–11)                                        —
 Type (Octets 12–13)                                     0800
 IP stuff (Octets 14–22)                                 —
 UDP (Octet 23)                                          11
 IP stuff (Octets 24–29)                                 —
 IP DA (Octets 30–32)                                    E00001
 IP DA (Octet 33)                                        81 or 82 or 83 or 84
 Source IP port (Octets 34–35)                           —
 Dest IP port (Octets 36–37)                             013F
 Other stuff (Octets 38–42)                              —
 Version PTP (Octet 43)                                  01
 Other stuff (Octets 44–73)                              —
 Control (Octet 74)                                      00
 Other stuff (Octets 75–168)                             —

Table 24-6. Example of Delay Request Frame in 1588 Version 1 Format

 Frame Segment                                           Value
 Preamble/SFD                                            55555555555555D5
 DA (Octets 0–5)                                         —
 SA (Octets 6–11)                                        —
 Type (Octets 12–13)                                     0800
 IP stuff (Octets 14–22)                                 —
 UDP (Octet 23)                                          11
 IP stuff (Octets 24–29)                                 —
 IP DA (Octets 30–32)                                    E00001
 IP DA (Octet 33)                                        81 or 82 or 83 or 84
 Source IP port (Octets 34–35)                           —
 Dest IP port (Octets 36–37)                             013F
 Other stuff (Octets 38–42)                              —
 Version PTP (Octet 43)                                  01
 Other stuff (Octets 44–73)                              —




© 2019 Microchip Technology Inc.             Datasheet                          DS60001507E-page 499
                                                 SAM D5x/E5x Family Data Sheet
                                                                               GMAC - Ethernet MAC

...........continued
 Frame Segment                                                 Value
 Control (Octet 74)                                            01
 Other stuff (Octets 75–168)                                   —

For 1588 version 1 messages, sync and delay request frames are indicated by the GMAC if the frame
type field indicates TCP/IP, UDP protocol is indicated, the destination IP address is 224.0.1.129/130/131
or 132, the destination UDP port is 319 and the control field is correct.
The control field is 0x00 for sync frames and 0x01 for delay request frames.
For 1588 version 2 messages, the type of frame is determined by looking at the message type field in the
first byte of the PTP frame. Whether a frame is version 1 or version 2 can be determined by looking at the
version PTP field in the second byte of both version 1 and version 2 PTP frames.
In version 2 messages sync frames have a message type value of 0x0, delay_req have 0x1, Pdelay_Req
have 0x2 and Pdelay_Resp have 0x3.
Table 24-7. Example of Sync Frame in 1588 Version 2 (UDP/IPv4) Format

 Frame Segment                                                 Value
 Preamble/SFD                                                  55555555555555D5
 DA (Octets 0–5)                                               —
 SA (Octets 6–11)                                              —
 Type (Octets 12–13)                                           0800
 IP stuff (Octets 14–22)                                       —
 UDP (Octet 23)                                                11
 IP stuff (Octets 24–29)                                       —
 IP DA (Octets 30–33)                                          E0000181
 Source IP port (Octets 34–35)                                 —
 Dest IP port (Octets 36–37)                                   013F
 Other stuff (Octets 38–41)                                    —
 Message type (Octet 42)                                       00
 Version PTP (Octet 43)                                        02

Table 24-8. Example of Pdelay_Req Frame in 1588 Version 2 (UDP/IPv4) Format

 Frame Segment                                                 Value
 Preamble/SFD                                                  55555555555555D5
 DA (Octets 0–5)                                               —
 SA (Octets 6–11)                                              —
 Type (Octets 12–13)                                           0800




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 500
                                           SAM D5x/E5x Family Data Sheet
                                                                        GMAC - Ethernet MAC

...........continued
 Frame Segment                                           Value
 IP stuff (Octets 14–22)                                 —
 UDP (Octet 23)                                          11
 IP stuff (Octets 24–29)                                 —
 IP DA (Octets 30–33)                                    E000006B
 Source IP port (Octets 34–35)                           —
 Dest IP port (Octets 36–37)                             013F
 Other stuff (Octets 38–41)                              —
 Message type (Octet 42)                                 02
 Version PTP (Octet 43)                                  02

Table 24-9. Example of Sync Frame in 1588 Version 2 (UDP/IPv6) Format

 Frame Segment                                           Value
 Preamble/SFD                                            55555555555555D5
 DA (Octets 0–5)                                         —
 SA (Octets 6–11)                                        —
 Type (Octets 12–13)                                     86dd
 IP stuff (Octets 14–19)                                 —
 UDP (Octet 20)                                          11
 IP stuff (Octets 21–37)                                 —
 IP DA (Octets 38–53)                                    FF0X00000000018
 Source IP port (Octets 54–55)                           —
 Dest IP port (Octets 56–57)                             013F
 Other stuff (Octets 58–61)                              —
 Message type (Octet 62)                                 00
 Other stuff (Octets 63–93)                              —
 Version PTP (Octet 94)                                  02

Table 24-10. Example of Pdelay_Resp Frame in 1588 Version 2 (UDP/IPv6) Format

 Frame Segment                                           Value
 Preamble/SFD                                            55555555555555D5
 DA (Octets 0–5)                                         —
 SA (Octets 6–11)                                        —




© 2019 Microchip Technology Inc.             Datasheet                       DS60001507E-page 501
                                                SAM D5x/E5x Family Data Sheet
                                                                           GMAC - Ethernet MAC

...........continued
 Frame Segment                                               Value
 Type (Octets 12–13)                                         86dd
 IP stuff (Octets 14–19)                                     —
 UDP (Octet 20)                                              11
 IP stuff (Octets 21–37)                                     —
 IP DA (Octets 38–53)                                        FF0200000000006B
 Source IP port (Octets 54–55)                               —
 Dest IP port (Octets 56–57)                                 013F
 Other stuff (Octets 58–61)                                  —
 Message type (Octet 62)                                     03
 Other stuff (Octets 63–93)                                  —
 Version PTP (Octet 94)                                      02

For the multicast address 011B19000000 sync and delay request frames are recognized depending on
the message type field, 00 for sync and 01 for delay request.
Table 24-11. Example of Sync Frame in 1588 Version 2 (Ethernet Multicast) Format

 Frame Segment                                          Value
 Preamble/SFD                                           55555555555555D5
 DA (Octets 0–5)                                        011B19000000
 SA (Octets 6–11)                                       —
 Type (Octets 12–13)                                    88F7
 Message type (Octet 14)                                00
 Version PTP (Octet 15)                                 02

Pdelay request frames need a special multicast address so they can pass through ports blocked by the
spanning tree protocol. For the multicast address 0180C200000E sync, Pdelay_Req and Pdelay_Resp
frames are recognized depending on the message type field, 00 for sync, 02 for pdelay request and 03
for pdelay response.
Table 24-12. Example of Pdelay_Req Frame in 1588 Version 2 (Ethernet Multicast) Format

 Frame Segment                                          Value
 Preamble/SFD                                           55555555555555D5
 DA (Octets 0–5)                                        0180C200000E
 SA (Octets 6–11)                                       —
 Type (Octets 12–13)                                    88F7
 Message type (Octet 14)                                00




© 2019 Microchip Technology Inc.                 Datasheet                         DS60001507E-page 502
                                                          SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

        ...........continued
        Frame Segment                                              Value
        Version PTP (Octet 15)                                     02

24.6.15 Time Stamp Unit

        Overview
        The TSU consists of a timer and registers to capture the time at which PTP event frames cross the
        message timestamp point. An interrupt is issued when a capture register is updated.
        The 1588 time stamp unit (TSU) is implemented as a 94-bit timer.
         • The 48 upper bits [93:46] of the timer count seconds and are accessible in the GMAC 1588 Timer
           Seconds High Register” (TSH) and GMAC 1588 Timer Seconds Low Register (TSL).
         • The 30 lower bits [45:16] of the timer count nanoseconds and are accessible in the GMAC 1588
           Timer Nanoseconds Register (TN).
         • The lowest 16 bits [15:0] of the timer count sub-nanoseconds.

        The 46 lower bits roll over when they have counted to 1s. An interrupt is generated when the seconds
        increment. The timer increments by a programmable period (to approximately 15.2fs resolution) with each
        MCK period. The timer value can be read, written and adjusted with 1ns resolution (incremented or
        decremented) through the APB interface.

        Timer Adjustment
        The amount by which the timer increments each clock cycle is controlled by the Timer Increment register
        (TI). Bits [7:0] are the default increment value in nanoseconds. Additional 16 bits of sub-nanosecond
        resolution are available using the Timer Increment Sub-Nanoseconds register (TISUBN). If the rest of the
        register is written with zero, the timer increments by the value in [7:0], plus the value of the TISUBN for
        each clock cycle.
        The TISUBN allows a resolution of approximately 15fs.
        Bits [15:8] of the increment register are the alternative increment value in nanoseconds, and bits [23:16]
        are the number of increments after which the alternative increment value is used. If [23:16] are zero the
        alternative increment value will never be used.

                 Taking the example of 10.2MHz, there are 102 cycles every 10µs or 51 cycles every 5µs.
                 So a timer with a 10.2MHz clock source is constructed by incrementing by 98ns for fifty
                 cycles and then incrementing by 100ns (98ns × 50 + 100ns = 5000ns). This is
                 programmed by writing the value 0x00326462 to the Timer Increment register (TI).


                 In a second example, a 49.8 MHz clock source requires 20ns for 248 cycles, followed by
                 an increment of 40ns (20ns × 248 + 40ns = 5000ns). This is programmed by writing the
                 value 0x00F82814 to the TI register.
        The Number of Increments bit field in the TI register is 8 bit in size, so frequencies up to 50MHz are
        supported with 200kHz resolution.
        Without the alternative increment field the period of the clock would be limited to an integer number of
        nanoseconds, resulting in supported clock frequencies of 8, 10, 20, 25, 40, 50, 100, 125, 200 and 250
        MHz.




       © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 503
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

         There are eight additional 80-bit registers that capture the time at which PTP event frames are
         transmitted and received. An interrupt is issued when these registers are updated. The TSU timer count
         value can be compared to a programmable comparison value. For the comparison, the 48 bits of the
         seconds value and the upper 22 bits of the nanoseconds value are used. A signal (GTSUCOMP) is
         output from the core to indicate when the TSU timer count value is equal to the comparison value stored
         in the TSU timer comparison value registers (GMAC.NSC, GMAC.SCL, and GMAC.SCH). An interrupt
         can also be generated (if enabled) when the TSU timer count value and comparison value are equal,
         mapped to bit 29 of the interrupt status register.

24.6.16 MAC 802.3 Pause Frame Support
        Note: Refer to the Clause 31, and Annex 31A and 31B of the IEEE standard 802.3 for a full description
        of MAC 802.3 pause operation.
         The following table shows the start of a MAC 802.3 pause frame.
         Table 24-13. Start of an 802.3 Pause Frame

         Address                                      Type                                  Pause
                                                      (MAC Control Frame)
         Destination                       Source                                           Opcode          Time
         0x0180C2000001                    6 bytes    0x8808                                0x0001          2 bytes

         The GMAC supports both hardware controlled pause of the transmitter, upon reception of a pause frame,
         and hardware generated pause frame transmission.
24.6.16.1 802.3 Pause Frame Reception
         The bit 13 of the Network Configuration register is the pause enable control for reception. If this bit is set,
         transmission will pause if a non zero pause quantum frame is received.
         If a valid pause frame is received, then the Pause Time register is updated with the new frame's pause
         time, regardless of whether a previous pause frame is active or not. An interrupt (either bit 12 or bit 13 of
         the Interrupt Status register) is triggered when a pause frame is received, but only if the interrupt has
         been enabled (bit 12 and bit 13 of the Interrupt Mask register). Pause frames received with non zero
         quantum are indicated through the interrupt bit 12 of the Interrupt Status register. Pause frames received
         with zero quantum are indicated on bit 13 of the Interrupt Status register.
         Once the Pause Time register is loaded and the frame currently being transmitted has been sent, no new
         frames are transmitted until the pause time reaches zero. The loading of a new pause time, and hence
         the pausing of transmission, only occurs when the GMAC is configured for full duplex operation. If the
         GMAC is configured for half duplex there will be no transmission pause, but the pause frame received
         interrupt will still be triggered. A valid pause frame is defined as having a destination address that
         matches either the address stored in Specific Address register ‘1’ or if it matches the reserved address of
         0x0180C2000001. It must also have the MAC control frame type ID of 0x8808 and have the pause
         opcode of 0x0001.
         Pause frames that have frame check sequence (FCS) or other errors will be treated as invalid and will be
         discarded. Valid pause frames received will increment the pause frames received statistic register.
         The pause time register decrements every 512 bit times once the transmission has stopped. For test
         purposes, the retry test bit can be set (bit 12 in the Network Configuration register) which causes the
         Pause Time register to decrement every GTXCK cycle once transmission has stopped.




        © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 504
                                                              SAM D5x/E5x Family Data Sheet
                                                                                            GMAC - Ethernet MAC

         The interrupt (bit 13 in the Interrupt Status register) is asserted whenever the Pause Time register
         decrements to zero (assuming it has been enabled by bit 13 in the Interrupt Mask register). This interrupt
         is also set when a zero quantum pause frame is received.
24.6.16.2 802.3 Pause Frame Transmission
         Automatic transmission of pause frames is supported through the transmit pause frame bits of the
         Network Control register. If either bit 11 or bit 12 of the Network Control register is written with logic 1, an
         802.3 pause frame will be transmitted, providing full duplex is selected in the Network Configuration
         register and the transmit block is enabled in the Network Control register.
         Pause frame transmission will happen immediately if transmit is inactive or if transmit is active between
         the current frame and the next frame due to be transmitted.
         Transmitted pause frames comprise the following:
          •   A destination address of 01-80-C2-00-00-01
          •   A source address taken from Specific Address register 1
          •   A type ID of 88-08 (MAC control frame)
          •   A pause opcode of 00-01
          •   A pause quantum register
          •   Fill of 00 to take the frame to minimum frame length
          •   Valid FCS
         The pause quantum used in the generated frame will depend on the trigger source for the frame as
         follows:
          • If bit 11 is written with a '1', the pause quantum will be taken from the Transmit Pause Quantum
            register. The Transmit Pause Quantum register resets to a value of 0xFFFF giving maximum pause
            quantum as default.
          • If bit 12 is written with a '1', the pause quantum will be zero.
         After transmission, a pause frame transmitted interrupt will be generated (bit 14 of the Interrupt Status
         register) and the only statistics register that will be incremented will be the Pause Frames Transmitted
         register.
         Pause frames can also be transmitted by the MAC using normal frame transmission methods.

24.6.17 Energy Efficient Ethernet Support
        Features
         • Energy Efficient Ethernet according to IEEE 802.3az
         • A system’s transmit path can enter a low power mode if there is nothing to transmit.
         • A PHY can detect whether its link partner’s transmit path is in low power mode, and configure its own
            receive path to enter low power mode.
         • Link remains up during lower power mode and no frames are dropped.
         • Asymmetric, one direction can be in low power mode while the other is transmitting normally.
         • LPI (Low Power Idle) signaling is used to control entry and exit to and from low power modes.
            Note: LPI signaling can only take place if both sides have indicated support for it through auto-
            negotiation.
         Operation
          • Low power control is done at the MII (reconciliation sublayer).




        © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 505
                                                           SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

           • As an architectural convenience in writing the 802.3az it is assumed that transmission is deferred by
             asserting carrier sense - in practice it will not be done this way. This system will know when it has
             nothing to transmit and only enter low power mode when it is not transmitting.
           • LPI should not be requested unless the link has been up for at least one second.
           • LPI is signaled on the MII transmit path by asserting 0x01 on txd with tx_en low and tx_er high.
           • A PHY on seeing LPI requested on the MII will send the sleep signal before going quiet. After going
             quiet it will periodically emit refresh signals.
           • The sleep, quiet and refresh periods are defined in 802.3az, Table 78-2.
           • LPI mode ends by transmitting normal idle for the wake time. There is a default time for this but it can
             be adjusted in software using the Link Layer Discovery Protocol (LLDP) described in 802.3az, Clause
             79.
           • LPI is indicated at the receive side when sleep and refresh signaling has been detected.

24.6.18 802.1Qav Support - Credit-based Shaping
        A credit-based shaping algorithm is available on the two highest priority queues and is defined in the
        standard 802.1Qav: Forwarding and Queuing Enhancements for Time-Sensitive Streams. This allows
        traffic on these queues to be limited and to allow other queues to transmit.
         Traffic shaping is enabled via the CBS (Credit Based Shaping) Control register. This enables a counter
         which stores the amount of transmit 'credit', measured in bytes that a particular queue has. A queue may
         only transmit if it has non-negative credit. If a queue has data to send, but is held off from doing as
         another queue is transmitting, then credit will accumulate in the credit counter at the rate defined in the
         IdleSlope register (CBSISQx) for that queue.
         portTransmitRate is the transmission rate, in bits per second, that the underlying MAC service that
         supports transmission through the Port provides. The value of this parameter is determined by the
         operation of the MAC. IdleSlope is the rate of change of increasing credit when waiting to transmit and
         must be less than the value of the portTransmitRate.
         IdleSlope is the rate of change of credit when waiting to transmit and must be less than the value of the
         portTransmitRate.
         The max value of IdleSlope (or sendSlope) is (portTransmitRate / bits_per_MII_Clock).
         In case of 100 Mbps, maximum IdleSlope = (100 Mbps / 4) = 0x17D7840.
         When this queue is transmitting the credit counter is decremented at the rate of sendSlope which is
         defined as (portTransmitRate - IdleSlope). A queue can accumulate negative credit when transmitting
         which will hold off any other transfers from that queue until credit returns to a non-negative value. No
         transfers are halted when a queue's credit becomes negative; it will accumulate negative credit until the
         transfer completes.
         The highest priority queue always has priority regardless of which queue has the most credit.

24.6.19 PHY Interface
        Different PHY interfaces are supported by the Ethernet MAC:
           • MII
           • RMII
         The MII interface is provided for 10/100 operation and uses txd[3:0] and rxd[3:0]. The RMII interface is
         provided for 10/100 operation and uses txd[1:0] and rxd[1:0].




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 506
                                                              SAM D5x/E5x Family Data Sheet
                                                                                                   GMAC - Ethernet MAC

24.6.20 10/100 Operation
        The 10/100 Mbps speed bit in the Network Configuration register is used to select between 10 Mbps and
        100 Mbps.

24.6.21 Jumbo Frames
        The jumbo frames enable bit in the Network Configuration register allows the GMAC, in its default
        configuration, to receive jumbo frames up to 10240 bytes in size. This operation does not form part of the
        IEEE 802.3 specification and is normally disabled. When jumbo frames are enabled, frames received with
        a frame size greater than 10240 bytes are discarded.


24.7     Programming Interface

24.7.1   Initialization
24.7.1.1 Configuration
         Initialization of the GMAC configuration (e.g., loop back mode, frequency ratios) must be done while the
         transmit and receive circuits are disabled. See the description of the Network Control register and
         Network Configuration register earlier in this document.
         To change loop back mode, the following sequence of operations must be followed:
           1.   Write to Network Control register to disable transmit and receive circuits.
           2.   Write to Network Control register to change loop back mode.
           3.   Write to Network Control register to re-enable transmit or receive circuits.
                Note: These writes to the Network Control register cannot be combined in any way.
24.7.1.2 Receive Buffer List
         Receive data is written to areas of data (i.e., buffers) in system memory. These buffers are listed in
         another data structure that also resides in main memory. This data structure (receive buffer queue) is a
         sequence of descriptor entries as defined in Table 1-6 “Receive Buffer Descriptor Entry”.
         The Receive Buffer Queue Pointer register points to this data structure.
         Figure 24-3. Receive Buffer List
                                                                                               Receive Buffer 0
                               Receive Buffer Queue Pointer
                                     (MAC Register)
                                                                                               Receive Buffer 1




                                                                                               Receive Buffer N

                                                              Receive Buffer Descriptor List
                                                                                                (In memory)
                                                                      (In memory)


         To create the list of buffers:
           1.   Allocate a number (N) of buffers of X bytes in system memory, where X is the DMA buffer length
                programmed in the DMA Configuration register.
           2.   Allocate an area 8N bytes for the receive buffer descriptor list in system memory and create N
                entries in this list. Mark all entries in this list as owned by GMAC, i.e., bit 0 of word 0 set to 0.




         © 2019 Microchip Technology Inc.                       Datasheet                                         DS60001507E-page 507
                                                             SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

          3.   Mark the last descriptor in the queue with the wrap bit (bit 1 in word 0 set to 1).
          4.   Write address of receive buffer descriptor list and control information to GMAC register receive
               buffer queue pointer
          5.   The receive circuits can then be enabled by writing to the address recognition registers and the
               Network Control register.
24.7.1.3 Transmit Buffer List
         Transmit data is read from areas of data (the buffers) in system memory. These buffers are listed in
         another data structure that also resides in main memory. This data structure (Transmit Buffer Queue) is a
         sequence of descriptor entries as defined in Table 1-7 “Transmit Buffer Descriptor Entry”.
         The Transmit Buffer Queue Pointer register points to this data structure.
         To create this list of buffers:
          1.   Allocate a number (N) of buffers of between 1 and 2047 bytes of data to be transmitted in system
               memory. Up to 128 buffers per frame are allowed.
          2.   Allocate an area 8N bytes for the transmit buffer descriptor list in system memory and create N
               entries in this list. Mark all entries in this list as owned by GMAC, i.e., bit 31 of word 1 set to 0.
          3.   Mark the last descriptor in the queue with the wrap bit (bit 30 in word 1 set to 1).
          4.   Write address of transmit buffer descriptor list and control information to GMAC register transmit
               buffer queue pointer.
          5.   The transmit circuits can then be enabled by writing to the Network Control register.
24.7.1.4 Address Matching
         The GMAC register pair hash address and the four Specific Address register pairs must be written with
         the required values. Each register pair comprises of a bottom register and top register, with the bottom
         register being written first. The address matching is disabled for a particular register pair after the bottom
         register has been written and re-enabled when the top register is written. Each register pair may be
         written at any time, regardless of whether the receive circuits are enabled or disabled.
         As an example, to set Specific Address register 1 to recognize destination address 21:43:65:87:A9:CB,
         the following values are written to Specific Address register 1 bottom and Specific Address register 1 top:
          • Specific Address register 1 bottom bits 31:0 (0x98): 0x8765_4321.
          • Specific Address register 1 top bits 31:0 (0x9C): 0x0000_CBA9.
24.7.1.5 PHY Maintenance
         The PHY Maintenance register is implemented as a shift register. Writing to the register starts a shift
         operation which is signalled as complete when bit two is set in the Network Status register (about 2000
         MCK cycles later when bits 18:16 are set to 010 in the Network Configuration register). An interrupt is
         generated as this bit is set.
         During this time, the MSB of the register is output on the MDIO pin and the LSB updated from the MDIO
         pin with each Management Data Clock (MDC) cycle. This causes the transmission of a PHY management
         frame on MDIO. See section 22.2.4.5 of the IEEE 802.3 standard.
         Reading during the shift operation will return the current contents of the shift register. At the end of the
         management operation the bits will have shifted back to their original locations. For a read operation the
         data bits are updated with data read from the PHY. It is important to write the correct values to the register
         to ensure a valid PHY management frame is produced.




        © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 508
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

         The Management Data Clock (MDC) should not toggle faster than 2.5 MHz (minimum period of 400 ns),
         as defined by the IEEE 802.3 standard. MDC is generated by dividing down MCK. Three bits in the
         Network Configuration register determine by how much MCK should be divided to produce MDC.

24.7.1.6 Interrupts
         There are 18 interrupt conditions that are detected within the GMAC. The conditions are ORed to make a
         single interrupt. Depending on the overall system design this may be passed through a further level of
         interrupt collection (interrupt controller). On receipt of the interrupt signal, the CPU enters the interrupt
         handler. Refer to the device interrupt controller documentation to identify that it is the GMAC that is
         generating the interrupt. To ascertain which interrupt, read the Interrupt Status register. Note that in the
         default configuration this register will clear itself after being read, though this may be configured to be
         write-one-to-clear if desired.
         At reset all interrupts are disabled. To enable an interrupt, write to Interrupt Enable register with the
         pertinent interrupt bit set to 1. To disable an interrupt, write to Interrupt Disable register with the pertinent
         interrupt bit set to 1. To check whether an interrupt is enabled or disabled, read Interrupt Mask register. If
         the bit is set to 1, the interrupt is disabled.

24.7.1.7 Transmitting Frames
         The procedure to set up a frame for transmission is the following:
          1.    Enable transmit in the Network Control register.
          2.    Allocate an area of system memory for transmit data. This does not have to be contiguous, varying
                byte lengths can be used if they conclude on byte borders.
          3.    Set-up the transmit buffer list by writing buffer addresses to word zero of the transmit buffer
                descriptor entries and control and length to word one.
          4.    Write data for transmission into the buffers pointed to by the descriptors.
          5.    Write the address of the first buffer descriptor to transmit buffer descriptor queue pointer.
          6.    Enable appropriate interrupts.
          7.    Write to the transmit start bit (TSTART) in the Network Control register.

24.7.1.8 Receiving Frames
         When a frame is received and the receive circuits are enabled, the GMAC checks the address and, in the
         following cases, the frame is written to system memory:
          •    If it matches one of the four Specific Address registers.
          •    If it matches one of the four type ID registers.
          •    If it matches the hash address function.
          •    If it is a broadcast address (0xFFFFFFFFFFFF) and broadcasts are allowed.
          •    If the GMAC is configured to “copy all frames”.
         The register receive buffer queue pointer points to the next entry in the receive buffer descriptor list and
         the GMAC uses this as the address in system memory to write the frame to.
         Once the frame has been completely and successfully received and written to system memory, the
         GMAC then updates the receive buffer descriptor entry (see Table 1-6 “Receive Buffer Descriptor Entry”)
         with the reason for the address match and marks the area as being owned by software. Once this is
         complete, a receive complete interrupt is set. Software is then responsible for copying the data to the
         application area and releasing the buffer (by writing the ownership bit back to 0).
         If the GMAC is unable to write the data at a rate to match the incoming frame, then a receive overrun
         interrupt is set. If there is no receive buffer available, i.e., the next buffer is still owned by software, a




        © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 509
                                                              SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

         receive buffer not available interrupt is set. If the frame is not successfully received, a statistics register is
         incremented and the frame is discarded without informing software.

24.7.2   Statistics Registers
         Statistics registers are described in the User Interface beginning with Section 1.8.48 ”GMAC Octets
         Transmitted Low Register” and ending with Section 1.8.92 ”GMAC UDP Checksum Errors Register”.
         The statistics register block begins at 0x100 and runs to 0x1B0, and comprises the registers listed below.

          Octets Transmitted Low Register                           Broadcast Frames Received Register
          Octets Transmitted High Register                          Multicast Frames Received Register
          Frames Transmitted Register                               Pause Frames Received Register
          Broadcast Frames Transmitted Register                     64 Byte Frames Received Register
          Multicast Frames Transmitted Register                     65 to 127 Byte Frames Received Register
          Pause Frames Transmitted Register                         128 to 255 Byte Frames Received Register
          64 Byte Frames Transmitted Register                       256 to 511 Byte Frames Received Register
          65 to 127 Byte Frames Transmitted Register                512 to 1023 Byte Frames Received Register
          128 to 255 Byte Frames Transmitted Register               1024 to 1518 Byte Frames Received Register
          256 to 511 Byte Frames Transmitted Register               1519 to Maximum Byte Frames Received
                                                                    Register
          512 to 1023 Byte Frames Transmitted Register              Undersize Frames Received Register
          1024 to 1518 Byte Frames Transmitted Register             Oversize Frames Received Register
          Greater Than 1518 Byte Frames Transmitted                 Jabbers Received Register
          Register
          Transmit Underruns Register                               Frame Check Sequence Errors Register
          Single Collision Frames Register                          Length Field Frame Errors Register
          Multiple Collision Frames Register                        Receive Symbol Errors Register
          Excessive Collisions Register                             Alignment Errors Register
          Late Collisions Register                                  Receive Resource Errors Register
          Deferred Transmission Frames Register                     Receive Overrun Register
          Carrier Sense Errors Register                             IP Header Checksum Errors Register
          Octets Received Low Register                              TCP Checksum Errors Register
          Octets Received High Register                             UDP Checksum Errors Register
          Frames Received Register

         These registers reset to zero on a read and stick at all ones when they count to their maximum value.
         They should be read frequently enough to prevent loss of data.
         The receive statistics registers are only incremented when the receive enable bit (RXEN) is set in the
         Network Control register.




         © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 510
                                                 SAM D5x/E5x Family Data Sheet
                                                                              GMAC - Ethernet MAC

Once a statistics register has been read, it is automatically cleared. When reading the Octets Transmitted
and Octets Received registers, bits 31:0 should be read prior to bits 47:32 to ensure reliable operation.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 511
                                                                         SAM D5x/E5x Family Data Sheet
                                                                                                          GMAC - Ethernet MAC


24.8      Register Summary

 Offset        Name        Bit Pos.

                              7:0     WESTAT        INCSTAT       CLRSTAT        MPE          TXEN        RXEN         LBL
                             15:8      SRTSM                                    TXZQPF        TXPF        THALT       TSTART       BP
 0x00          NCR
                             23:16                                                                LPI      FNP        TXPBPF     ENPBPR
                             31:24
                              7:0     UNIHEN         MTIHEN            NBC       CAF        JFRAME       DNVLAN         FD         SPD
                             15:8            RXBUFO[1:0]               PEN       RTY                                             MAXFS
 0x04         NCFGR
                             23:16     DCPF                 DBW[1:0]                         CLK[2:0]                 RFCS        LFERD
                             31:24                   IRXER         RXBP         IPGSEN                   IRXFCS       EFRHD      RXCOEN
                              7:0                                                                         IDLE         MDIO
                             15:8
 0x08          NSR
                             23:16
                             31:24
                              7:0                                                                                                  MII
                             15:8
 0x0C           UR
                             23:16
                             31:24
                              7:0       ESPA         ESMA                                               FBLDO[4:0]
                             15:8                                                           TXCOEN       TXPBMS           RXBMS[1:0]
 0x10         DCFGR
                             23:16                                                    DRBS[7:0]
                             31:24                                                                                                DDRP
                              7:0                     UND         TXCOMP         TFC          TXGO         RLE         COL         UBR
                             15:8                                                                                                HRESP
 0x14           TSR
                             23:16
                             31:24
                              7:0                                        ADDR[5:0]
                             15:8                                                    ADDR[13:6]
 0x18          RBQB
                             23:16                                                   ADDR[21:14]
                             31:24                                                   ADDR[29:22]
                              7:0                                        ADDR[5:0]
                             15:8                                                    ADDR[13:6]
 0x1C          TBQB
                             23:16                                                   ADDR[21:14]
                             31:24                                                   ADDR[29:22]
                              7:0                                                             HNO        RXOVR         REC         BNA
                             15:8
 0x20          RSR
                             23:16
                             31:24
                              7:0      TCOMP          TFC          RLEX          TUR         TXUBR       RXUBR        RCOMP        MFS
                             15:8                     PFTR             PTZ       PFNZ        HRESP        ROVR
 0x24           ISR
                             23:16    PDRSFR        PDRQFR             SFT      DRQFT         SFR        DRQFR
                             31:24                                TSUCMP         WOL                       SRI       PDRSFT      PDRQFT




          © 2019 Microchip Technology Inc.                                   Datasheet                               DS60001507E-page 512
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                                 GMAC - Ethernet MAC

...........continued

  Offset               Name    Bit Pos.

                                  7:0      TCOMP       TFC      RLEX             TUR           TXUBR            RXUBR             RCOMP           MFS
                                 15:8      EXINT       PFTR     PTZ              PFNZ          HRESP             ROVR
   0x28                 IER
                                 23:16    PDRSFR      PDRQFR    SFT          DRQFT                 SFR          DRQFR
                                 31:24                         TSUCMP            WOL                                 SRI          PDRSFT     PDRQFT
                                  7:0      TCOMP       TFC      RLEX             TUR           TXUBR            RXUBR             RCOMP           MFS
                                 15:8      EXINT       PFTR     PTZ              PFNZ          HRESP             ROVR
   0x2C                 IDR
                                 23:16    PDRSFR      PDRQFR    SFT          DRQFT                 SFR          DRQFR
                                 31:24                         TSUCMP            WOL         RXLPISBC                SRI          PDRSFT     PDRQFT
                                  7:0      TCOMP       TFC      RLEX             TUR           TXUBR            RXUBR             RCOMP           MFS
                                 15:8      EXINT       PFTR     PTZ              PFNZ          HRESP             ROVR
   0x30                 IMR
                                 23:16    PDRSFR      PDRQFR    SFT          DRQFT                 SFR          DRQFR
                                 31:24                         TSUCMP            WOL                                 SRI          PDRSFT     PDRQFT
                                  7:0                                                  DATA[7:0]
                                 15:8                                               DATA[15:8]
   0x34                MAN
                                 23:16    PHYA[0:0]                         REGA[4:0]                                                  WTN[1:0]
                                 31:24      WZO       CLTTO            OP[1:0]                                             PHYA[4:1]
                                  7:0                                                  RPQ[7:0]
                                 15:8                                               RPQ[15:8]
   0x38                RPQ
                                 23:16
                                 31:24
                                  7:0                                                   TPQ[7:0]
                                 15:8                                                  TPQ[15:8]
   0x3C                TPQ
                                 23:16
                                 31:24
                                  7:0                                              TPB1ADR[7:0]
                                 15:8                                                                                 TPB1ADR[11:8]
   0x40                TPSF
                                 23:16
                                 31:24     ENTXP
                                  7:0                                             RPB1ADR[7:0]
                                 15:8                                                                                 RPB1ADR[11:8]
   0x44                RPSF
                                 23:16
                                 31:24     ENRXP
                                  7:0                                                   FML[7:0]
                                 15:8                                                                    FML[13:8]
   0x48                RJFML
                                 23:16
                                 31:24
   0x4C
     ...           Reserved
   0x7F
                                  7:0                                               ADDR[7:0]
                                 15:8                                               ADDR[15:8]
   0x80                HRB
                                 23:16                                             ADDR[23:16]
                                 31:24                                             ADDR[31:24]




              © 2019 Microchip Technology Inc.                         Datasheet                                                DS60001507E-page 513
                                                   SAM D5x/E5x Family Data Sheet
                                                                       GMAC - Ethernet MAC

...........continued

  Offset               Name    Bit Pos.

                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x84                HRT
                                 23:16                   ADDR[23:16]
                                 31:24                   ADDR[31:24]
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x88                SAB0
                                 23:16                   ADDR[23:16]
                                 31:24                   ADDR[31:24]
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x8C                SAT0
                                 23:16
                                 31:24
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x90                SAB1
                                 23:16                   ADDR[23:16]
                                 31:24                   ADDR[31:24]
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x94                SAT1
                                 23:16
                                 31:24
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x98                SAB2
                                 23:16                   ADDR[23:16]
                                 31:24                   ADDR[31:24]
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0x9C                SAT2
                                 23:16
                                 31:24
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0xA0                SAB3
                                 23:16                   ADDR[23:16]
                                 31:24                   ADDR[31:24]
                                  7:0                     ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0xA4                SAT3
                                 23:16
                                 31:24
                                  7:0                      TID[7:0]
                                 15:8                      TID[15:8]
   0xA8                TIDM0
                                 23:16
                                 31:24     ENIDn
                                  7:0                      TID[7:0]
                                 15:8                      TID[15:8]
   0xAC                TIDM1
                                 23:16
                                 31:24     ENIDn




              © 2019 Microchip Technology Inc.     Datasheet                DS60001507E-page 514
                                                   SAM D5x/E5x Family Data Sheet
                                                                                  GMAC - Ethernet MAC

...........continued

  Offset               Name    Bit Pos.

                                  7:0                       TID[7:0]
                                 15:8                      TID[15:8]
   0xB0                TIDM2
                                 23:16
                                 31:24     ENIDn
                                  7:0                       TID[7:0]
                                 15:8                      TID[15:8]
   0xB4                TIDM3
                                 23:16
                                 31:24     ENIDn
                                  7:0                       IP[7:0]
                                 15:8                       IP[15:8]
   0xB8                WOL
                                 23:16                                 MTI        SA1           ARP       MAG
                                 31:24
                                  7:0                       FL[7:0]
                                 15:8                       FL[15:8]
   0xBC                IPGS
                                 23:16
                                 31:24
                                  7:0                   VLAN_TYPE[7:0]
                                 15:8                   VLAN_TYPE[15:8]
   0xC0                SVLAN
                                 23:16
                                 31:24    ESVLAN
   0xC4
     ...           Reserved
   0xC7
                                  7:0                      ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0xC8                SAMB1
                                 23:16                    ADDR[23:16]
                                 31:24                    ADDR[31:24]
                                  7:0                      ADDR[7:0]
                                 15:8                     ADDR[15:8]
   0xCC                SAMT1
                                 23:16
                                 31:24
   0xD0
     ...           Reserved
   0xDB
                                  7:0                    NANOSEC[7:0]
                                 15:8                   NANOSEC[15:8]
   0xDC                NSC
                                 23:16                                       NANOSEC[20:16]
                                 31:24
                                  7:0                      SEC[7:0]
                                 15:8                      SEC[15:8]
   0xE0                 SCL
                                 23:16                    SEC[23:16]
                                 31:24                    SEC[31:24]




              © 2019 Microchip Technology Inc.     Datasheet                                  DS60001507E-page 515
                                                 SAM D5x/E5x Family Data Sheet
                                                                     GMAC - Ethernet MAC

...........continued

  Offset               Name     Bit Pos.

                                  7:0                    SEC[7:0]
                                 15:8                   SEC[15:8]
   0xE4                 SCH
                                 23:16
                                 31:24
                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
   0xE8                EFTSH
                                 23:16
                                 31:24
                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
   0xEC                EFRSH
                                 23:16
                                 31:24
                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
   0xF0                PEFTSH
                                 23:16
                                 31:24
                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
   0xF4                PEFRSH
                                 23:16
                                 31:24
   0xF8
     ...           Reserved
   0xFF
                                  7:0                    TXO[7:0]
                                 15:8                   TXO[15:8]
  0x0100               OTLO
                                 23:16                  TXO[23:16]
                                 31:24                  TXO[31:24]
                                  7:0                    TXO[7:0]
                                 15:8                   TXO[15:8]
  0x0104                OTHI
                                 23:16
                                 31:24
                                  7:0                    FTX[7:0]
                                 15:8                   FTX[15:8]
  0x0108                 FT
                                 23:16                  FTX[23:16]
                                 31:24                  FTX[31:24]
                                  7:0                   BFTX[7:0]
                                 15:8                   BFTX[15:8]
  0x010C                BCFT
                                 23:16                 BFTX[23:16]
                                 31:24                 BFTX[31:24]
                                  7:0                   MFTX[7:0]
                                 15:8                   MFTX[15:8]
  0x0110                MFT
                                 23:16                 MFTX[23:16]
                                 31:24                 MFTX[31:24]




              © 2019 Microchip Technology Inc.   Datasheet                DS60001507E-page 516
                                                 SAM D5x/E5x Family Data Sheet
                                                                     GMAC - Ethernet MAC

...........continued

  Offset                Name     Bit Pos.

                                   7:0                  PFTX[7:0]
                                  15:8                  PFTX[15:8]
  0x0114                PFT
                                  23:16
                                  31:24
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x0118               BFT64
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x011C           TBFT127
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x0120           TBFT255
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x0124               TBFT511
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x0128           TBFT1023
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x012C           TBFT1518
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  NFTX[7:0]
                                  15:8                  NFTX[15:8]
  0x0130          GTBFT1518
                                  23:16                NFTX[23:16]
                                  31:24                NFTX[31:24]
                                   7:0                  TXUNR[7:0]
                                  15:8                                         TXUNR[9:8]
  0x0134                TUR
                                  23:16
                                  31:24
                                   7:0                  SCOL[7:0]
                                  15:8                  SCOL[15:8]
  0x0138                SCF
                                  23:16                                       SCOL[17:16]
                                  31:24
                                   7:0                  MCOL[7:0]
                                  15:8                  MCOL[15:8]
  0x013C                MCF
                                  23:16                                       MCOL[17:16]
                                  31:24




              © 2019 Microchip Technology Inc.   Datasheet                DS60001507E-page 517
                                                 SAM D5x/E5x Family Data Sheet
                                                                     GMAC - Ethernet MAC

...........continued

  Offset               Name    Bit Pos.

                                  7:0                   XCOL[7:0]
                                 15:8                                          XCOL[9:8]
  0x0140                EC
                                 23:16
                                 31:24
                                  7:0                   LCOL[7:0]
                                 15:8                                          LCOL[9:8]
  0x0144                LC
                                 23:16
                                 31:24
                                  7:0                   DEFT[7:0]
                                 15:8                   DEFT[15:8]
  0x0148               DTF
                                 23:16                                        DEFT[17:16]
                                 31:24
                                  7:0                    CSR[7:0]
                                 15:8                                           CSR[9:8]
  0x014C               CSE
                                 23:16
                                 31:24
                                  7:0                    RXO[7:0]
                                 15:8                   RXO[15:8]
  0x0150               ORLO
                                 23:16                  RXO[23:16]
                                 31:24                  RXO[31:24]
                                  7:0                    RXO[7:0]
                                 15:8                   RXO[15:8]
  0x0154               ORHI
                                 23:16
                                 31:24
                                  7:0                    FRX[7:0]
                                 15:8                   FRX[15:8]
  0x0158                FR
                                 23:16                  FRX[23:16]
                                 31:24                  FRX[31:24]
                                  7:0                   BFRX[7:0]
                                 15:8                   BFRX[15:8]
  0x015C               BCFR
                                 23:16                 BFRX[23:16]
                                 31:24                 BFRX[31:24]
                                  7:0                   MFRX[7:0]
                                 15:8                   MFRX[15:8]
  0x0160               MFR
                                 23:16                 MFRX[23:16]
                                 31:24                 MFRX[31:24]
                                  7:0                   PFRX[7:0]
                                 15:8                   PFRX[15:8]
  0x0164               PFR
                                 23:16
                                 31:24
                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x0168               BFR64
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]




              © 2019 Microchip Technology Inc.   Datasheet                DS60001507E-page 518
                                                 SAM D5x/E5x Family Data Sheet
                                                                     GMAC - Ethernet MAC

...........continued

  Offset                Name    Bit Pos.

                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x016C           TBFR127
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]
                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x0170           TBFR255
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]
                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x0174           TBFR511
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]
                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x0178           TBFR1023
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]
                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x017C           TBFR1518
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]
                                  7:0                   NFRX[7:0]
                                 15:8                   NFRX[15:8]
  0x0180               TMXBFR
                                 23:16                 NFRX[23:16]
                                 31:24                 NFRX[31:24]
                                  7:0                   UFRX[7:0]
                                 15:8                                          UFRX[9:8]
  0x0184                UFR
                                 23:16
                                 31:24
                                  7:0                   OFRX[7:0]
                                 15:8                                          OFRX[9:8]
  0x0188                OFR
                                 23:16
                                 31:24
                                  7:0                    JRX[7:0]
                                 15:8                                           JRX[9:8]
  0x018C                 JR
                                 23:16
                                 31:24
                                  7:0                   FCKR[7:0]
                                 15:8                                          FCKR[9:8]
  0x0190                FCSE
                                 23:16
                                 31:24
                                  7:0                   LFER[7:0]
                                 15:8                                          LFER[9:8]
  0x0194                LFFE
                                 23:16
                                 31:24




              © 2019 Microchip Technology Inc.   Datasheet                DS60001507E-page 519
                                                 SAM D5x/E5x Family Data Sheet
                                                                      GMAC - Ethernet MAC

...........continued

  Offset               Name     Bit Pos.

                                  7:0                   RXSE[7:0]
                                 15:8                                           RXSE[9:8]
  0x0198                RSE
                                 23:16
                                 31:24
                                  7:0                    AER[7:0]
                                 15:8                                            AER[9:8]
  0x019C                AE
                                 23:16
                                 31:24
                                  7:0                   RXRER[7:0]
                                 15:8                  RXRER[15:8]
  0x01A0                RRE
                                 23:16                                         RXRER[17:16]
                                 31:24
                                  7:0                   RXOVR[7:0]
                                 15:8                                           RXOVR[9:8]
  0x01A4                ROE
                                 23:16
                                 31:24
                                  7:0                   HCKER[7:0]
                                 15:8
  0x01A8                IHCE
                                 23:16
                                 31:24
                                  7:0                   TCKER[7:0]
                                 15:8
  0x01AC                TCE
                                 23:16
                                 31:24
                                  7:0                   UCKER[7:0]
                                 15:8
  0x01B0                UCE
                                 23:16
                                 31:24
  0x01B4
     ...           Reserved
  0x01BB
                                  7:0                   LSBTIR[7:0]
                                 15:8                  LSBTIR[15:8]
  0x01BC               TISUBN
                                 23:16
                                 31:24
                                  7:0                    TCS[7:0]
                                 15:8                   TCS[15:8]
  0x01C0                TSH
                                 23:16
                                 31:24
  0x01C4
     ...           Reserved
  0x01C7




              © 2019 Microchip Technology Inc.   Datasheet                 DS60001507E-page 520
                                                  SAM D5x/E5x Family Data Sheet
                                                                                 GMAC - Ethernet MAC

...........continued

  Offset               Name     Bit Pos.

                                  7:0                     VTS[7:0]
                                 15:8                    VTS[15:8]
  0x01C8               TSSSL
                                 23:16                   VTS[23:16]
                                 31:24                   VTS[31:24]
                                  7:0                     VTN[7:0]
                                 15:8                    VTN[15:8]
  0x01CC               TSSN
                                 23:16                   VTN[23:16]
                                 31:24                                 VTN[29:24]
                                  7:0                     TCS[7:0]
                                 15:8                    TCS[15:8]
  0x01D0                TSL
                                 23:16                   TCS[23:16]
                                 31:24                   TCS[31:24]
                                  7:0                     TNS[7:0]
                                 15:8                    TNS[15:8]
  0x01D4                TN
                                 23:16                   TNS[23:16]
                                 31:24                                 TNS[29:24]
                                  7:0                     ITDT[7:0]
                                 15:8                    ITDT[15:8]
  0x01D8                 TA
                                 23:16                   ITDT[23:16]
                                 31:24      ADJ                        ITDT[29:24]
                                  7:0                     CNS[7:0]
                                 15:8                    ACNS[7:0]
  0x01DC                 TI
                                 23:16                    NIT[7:0]
                                 31:24
                                  7:0                     RUD[7:0]
                                 15:8                    RUD[15:8]
  0x01E0               EFTSL
                                 23:16                   RUD[23:16]
                                 31:24                   RUD[31:24]
                                  7:0                     RUD[7:0]
                                 15:8                    RUD[15:8]
  0x01E4               EFTN
                                 23:16                   RUD[23:16]
                                 31:24                                 RUD[29:24]
                                  7:0                     RUD[7:0]
                                 15:8                    RUD[15:8]
  0x01E8               EFRSL
                                 23:16                   RUD[23:16]
                                 31:24                   RUD[31:24]
                                  7:0                     RUD[7:0]
                                 15:8                    RUD[15:8]
  0x01EC               EFRN
                                 23:16                   RUD[23:16]
                                 31:24                                 RUD[29:24]
                                  7:0                     RUD[7:0]
                                 15:8                    RUD[15:8]
  0x01F0               PEFTSL
                                 23:16                   RUD[23:16]
                                 31:24                   RUD[31:24]




              © 2019 Microchip Technology Inc.    Datasheet                           DS60001507E-page 521
                                                 SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

...........continued

  Offset               Name     Bit Pos.

                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
  0x01F4               PEFTN
                                 23:16                  RUD[23:16]
                                 31:24                                 RUD[29:24]
                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
  0x01F8               PEFRSL
                                 23:16                  RUD[23:16]
                                 31:24                  RUD[31:24]
                                  7:0                    RUD[7:0]
                                 15:8                   RUD[15:8]
  0x01FC               PEFRN
                                 23:16                  RUD[23:16]
                                 31:24                                 RUD[29:24]
  0x0200
     ...           Reserved
  0x026F
                                  7:0                   RLPITR[7:0]
                                 15:8                  RLPITR[15:8]
  0x0270               RLPITR
                                 23:16
                                 31:24
                                  7:0                   RLPITI[7:0]
                                 15:8                  RLPITI[15:8]
  0x0274               RLPITI
                                 23:16                 RLPITI[23:16]
                                 31:24
                                  7:0                   TLPITR[7:0]
                                 15:8                  TLPITR[15:8]
  0x0278               TLPITR
                                 23:16
                                 31:24
                                  7:0                   RLPITI[7:0]
                                 15:8                  RLPITI[15:8]
  0x027C               TLPITI
                                 23:16                 RLPITI[23:16]
                                 31:24




24.9           Register Description




              © 2019 Microchip Technology Inc.   Datasheet                           DS60001507E-page 522
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                GMAC - Ethernet MAC

24.9.1         GMAC Network Control Register

               Name:        NCR
               Offset:      0x000
               Reset:       0x00000000
               Property:    -


         Bit        31            30            29            28           27            26            25            24


   Access
    Reset


         Bit        23            22            21            20           19            18            17            16
                                                                           LPI          FNP         TXPBPF        ENPBPR
   Access                                                                  R/W          R/W           R/W           R/W
    Reset                                                                   0             0             0            0


         Bit        15            14            13            12            11           10             9            8
                  SRTSM                                    TXZQPF         TXPF         THALT        TSTART           BP
   Access           R/W                                      R/W           R/W          R/W           R/W           R/W
    Reset            0                                        0             0             0             0            0


         Bit         7             6             5            4             3             2             1            0
                  WESTAT       INCSTAT        CLRSTAT        MPE          TXEN          RXEN          LBL
   Access           R/W          R/W           R/W           R/W           R/W          R/W           R/W
    Reset            0             0             0            0             0             0             0


               Bit 19 – LPI Low Power Idle Enable
               Writing a '1' to this bit will enable low power idle (LPI) transmission, immediately transmitted on txd and
               tx_er.

               Bit 18 – FNP Flush Next Packet
               Writing a '1' to this bit will flush the next packet from the external RX DPRAM. Flushing the next packet
               will only take effect if the DMA is not currently writing a packet already stored in the DPRAM to memory.

               Bit 17 – TXPBPF Transmit PFC Priority-based Pause Frame
               Takes the values stored in the Transmit PFC Pause Register.

               Bit 16 – ENPBPR Enable PFC Priority-based Pause Reception
               Writing a '1' to this bit enables PFC Priority Based Pause Reception capabilities, enabling PFC
               negotiation and recognition of priority-based pause frames.
                Value        Description
                0            Normal operation
                1            PFC Priority-based Pause frames are recognized

               Bit 15 – SRTSM Store Receive Time Stamp to Memory
               Writing a '1' to this bit causes the CRC of every received frame to be replaced with the value of the
               nanoseconds field of the 1588 timer that was captured as the receive frame passed the message time
               stamp point.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 523
                                                      SAM D5x/E5x Family Data Sheet
                                                                                    GMAC - Ethernet MAC

 Value        Description
 0            Normal operation
 1            All received frames' CRC is replaced with a time stamp

Bit 12 – TXZQPF Transmit Zero Quantum Pause Frame
Writing a '1' to this bit causes a pause frame with zero quantum to be transmitted.
Writing a '0' to this bit has no effect.

Bit 11 – TXPF Transmit Pause Frame
Writing one to this bit causes a pause frame to be transmitted.
Writing a '0' to this bit has no effect.

Bit 10 – THALT Transmit Halt
Writing a '1' to this bit halts transmission as soon as any ongoing frame transmission ends.
Writing a '0' to this bit has no effect.

Bit 9 – TSTART Start Transmission
Writing a '1' to this bit starts transmission.
Writing a '0' to this bit has no effect.

Bit 8 – BP Back Pressure
In 10M or 100M half duplex mode, writing a '1' to this bit forces collisions on all received frames. Ignored
in gigabit half duplex mode.
 Value       Description
 0           Frame collisions are not forced
 1           Frame collisions are forced in 10M and 100M half duplex mode

Bit 7 – WESTAT Write Enable for Statistics Registers
Writing a '1' to this bit makes the statistics registers writable for functional test purposes.
Value         Description
0             Statistics Registers are write-protected
1             Statistics Registers are write-enabled

Bit 6 – INCSTAT Increment Statistics Registers
Writing a '1' to this bit increments all Statistics Registers by one for test purposes.
Writing a '0' to this bit has no effect.
This bit will always read '0'.

Bit 5 – CLRSTAT Clear Statistics Registers
Writing a '1' to this bit clears the Statistics Registers.
Writing a '0' to this bit has no effect.
This bit will always read '0'.

Bit 4 – MPE Management Port Enable
Writing a '1' to this bit enables the Management Port.
Writing a '0' to this bit disables the Management Port, and forces MDIO to high impedance state and
MDC to low impedance.
Value         Description
0             Management Port is disabled
1             Management Port is enabled




© 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 524
                                                   SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

Bit 3 – TXEN Transmit Enable
Writing a '1' to this bit enables the GMAC transmitter to send data.
Writing a '0' to this bit stops transmission immediately, the transmit pipeline and control registers is
cleared, and the Transmit Queue Pointer Register will be set to point to the start of the transmit descriptor
list.
 Value        Description
 0            Transmit is disabled
 1            Transmit is enabled

Bit 2 – RXEN Receive Enable
Writing a '1' to this bit enables the GMAC to receive data.
Writing a '0' to this bit stops frame reception immediately, and the receive pipeline is cleared. The Receive
Queue Pointer Register is not affected.
Value         Description
0             Receive is disabled
1             Receive is enabled

Bit 1 – LBL Loop Back Local
Writing '1' to this bit connects GTX to GRX, GTXEN to GRXDV, and forces full duplex mode.
GRXCK and GTXCK may malfunction as the GMAC is switched into and out of internal loop back. It is
important that receive and transmit circuits have already been disabled when making the switch into and
out of internal loop back.
 Value        Description
 0            Loop back local is disabled
 1            Loop back local is enabled




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 525
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                  GMAC - Ethernet MAC

24.9.2         GMAC Network Configuration Register

               Name:          NCFGR
               Offset:        0x004
               Reset:         0x00080000
               Property:      R/W


         Bit         31                 30               29      28           27           26            25             24
                                   IRXER                RXBP   IPGSEN                    IRXFCS        EFRHD         RXCOEN
   Access                           R/W                 R/W     R/W                        R/W           R/W           R/W
    Reset                               0                0       0                          0             0             0


         Bit         23                 22               21      20           19           18            17             16
                   DCPF                      DBW[1:0]                       CLK[2:0]                    RFCS          LFERD
   Access           R/W             R/W                 R/W     R/W           R/W          R/W           R/W           R/W
    Reset            0                  0                0       0             1            0             0             0


         Bit         15                 14               13      12           11           10             9             8
                          RXBUFO[1:0]                   PEN     RTY                                                  MAXFS
   Access           R/W             R/W                 R/W     R/W                                                    R/W
    Reset            0                  0                0       0                                                      0


         Bit         7                  6                5       4             3            2             1             0
                  UNIHEN          MTIHEN                NBC     CAF         JFRAME      DNVLAN           FD            SPD
   Access           R/W             R/W                 R/W     R/W           R/W          R/W           R/W           R/W
    Reset            0                  0                0       0             0            0             0             0


               Bit 30 – IRXER Ignore IPG GRXER
               When this bit is written to '1', the Receive Error signal (GRXER) has no effect on the GMAC operation
               when Receive Data Valid signal (GRXDV) is low.

               Bit 29 – RXBP Receive Bad Preamble
               When written to '1', frames with non-standard preamble are not rejected.

               Bit 28 – IPGSEN IP Stretch Enable
               Writing a '1' to this bit allows the transmit IPG to increase above 96 bit times, depending on the previous
               frame length using the IPG Stretch Register.

               Bit 26 – IRXFCS Ignore RX FCS
               For normal operation this bit must be written to zero.
               When this bit is written to '1', frames with FCS/CRC errors will not be rejected. FCS error statistics will still
               be collected for frames with bad FCS, and FCS status will be recorded in the DMA descriptor of the
               frame.

               Bit 25 – EFRHD Enable Frames Received in half-duplex
               Writing a '1' to this bit enables frames to be received in half-duplex mode while transmitting.




           © 2019 Microchip Technology Inc.                             Datasheet                          DS60001507E-page 526
                                                    SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

Bit 24 – RXCOEN Receive Checksum Offload Enable
Writing a '1' to this bit enables the receive checksum engine, and frames with bad IP, TCP or UDP
checksums are discarded.

Bit 23 – DCPF Disable Copy of Pause Frames
Writing a '1' to this bit prevents valid pause frames from being copied to memory. Pause frames are not
copied regardless of the state of the Copy All Frames (CAF) bit, whether a hash match is found or
whether a type ID match is identified.
If a destination address match is found, the pause frame will be copied to memory. Note that valid pause
frames received will still increment pause statistics and pause the transmission of frames, as required.

Bits 22:21 – DBW[1:0] Data Bus Width
The default value for this register is 64 bits.
 Value      Name                           Description
 0          DBW32                          32-bit data bus width
 1          DBW64                          64-bit data bus width

Bits 20:18 – CLK[2:0] MDC Clock Division
These bits must be set according to MCK speed, and determine the number MCK will be divided by to
generate Management Data Clock (MDC). For conformance with the 802.3 specification, MDC must not
exceed 2.5MHz.
Note: MDC is only active during MDIO read and write operations.
 Value        Name                 Description
 0            MCK_8                MCK divided by 8 (MCK up to 20MHz)
 1            MCK_16               MCK divided by 16 (MCK up to 40MHz)
 2            MCK_32               MCK divided by 32 (MCK up to 80MHz)
 3            MCK_48               MCK divided by 48 (MCK up to 120MHz)
 4            MCK_64               MCK divided by 64 (MCK up to 160MHz)
 5            MCK_96               MCK divided by 96 (MCK up to 240MHz)

Bit 17 – RFCS Remove FCS
Writing this bit to '1' will cause received frames to be written to memory without their frame check
sequence (last 4 bytes). The indicated frame length will be reduced by four bytes in this mode.

Bit 16 – LFERD Length Field Error Frame Discard
Writing a '1' to this bit discards frames with a measured length shorter than the extracted length field (as
indicated by bytes 13 and 14 in a non-VLAN tagged frame). This only applies to frames with a length field
less than 0x0600.

Bits 15:14 – RXBUFO[1:0] Receive Buffer Offset
These bits determine the number of bytes by which the received data is offset from the start of the receive
buffer.

Bit 13 – PEN Pause Enable
When written to '1', transmission will pause if a non-zero 802.3 classic pause frame is received and PFC
has not been negotiated.

Bit 12 – RTY Retry Test
This bit must be written to '0' for normal operation.




© 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 527
                                                      SAM D5x/E5x Family Data Sheet
                                                                                  GMAC - Ethernet MAC

When writing a '1' to this bit, the back-off between collisions will always be one slot time. This setting
helps testing the too many retries condition. This setting is also useful for pause frame tests by reducing
the pause counter's decrement time from "512 bit times" to "every GRXCK cycle".

Bit 8 – MAXFS 1536 Maximum Frame Size
Writing a '1' to this bit increases the maximum accepted frame size to 1536 bytes in length. When written
to '0', any frame above 1518 bytes in length is rejected.

Bit 7 – UNIHEN Unicast Hash Enable
When writing a '1' to this bit, unicast frames will be accepted when the 6-bit hash function of the
destination address points to a bit that is set in the Hash Register.
Writing a '0' to this bit disables unicast hashing.

Bit 6 – MTIHEN Multicast Hash Enable
When writing a '1' to this bit, multicast frames will be accepted when the 6-bit hash function of the
destination address points to a bit that is set in the Hash Register.
Writing a '0' to this bit disables multicast hashing.

Bit 5 – NBC No Broadcast
Writing a '1' to this bit will reject frames addressed to the broadcast address 0xFFFFFFFFFFFF (all '1').
Writing a '0' to this bit allows broadcasting to 0xFFFFFFFFFFFF.

Bit 4 – CAF Copy All Frames
When writing a '1' to this bit, all valid frames will be accepted.

Bit 3 – JFRAME Jumbo Frame Size
Writing a '1' to this bit enables jumbo frames of up to 10240 bytes to be accepted. The default length is
10240 bytes.

Bit 2 – DNVLAN Discard Non-VLAN Frames
Writing a '1' to this bit allows only VLAN-tagged frames to pass to the address matching logic.
Writing a '0' to this bit allows both VLAN_tagged and untagged frames to pass to the address matching
logic.

Bit 1 – FD Full Duplex
Writing a '1' enables full duplex operation, so the transmit block ignores the state of collision and carrier
sense and allows receive while transmitting.
Writing a '0' disables full duplex operation.

Bit 0 – SPD Speed
Writing a '1' selects 100Mbps operation.
Writing a '0' to this bit selects 10Mbps operation.




© 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 528
                                                                SAM D5x/E5x Family Data Sheet
                                                                                     GMAC - Ethernet MAC

24.9.3         GMAC Network Status Register

               Name:       NSR
               Offset:     0x008
               Reset:      0x00000004
               Property:   -


         Bit        31           30           29           28            27   26         25           24


   Access
    Reset


         Bit        23           22           21           20            19   18         17           16


   Access
    Reset


         Bit        15           14           13           12            11   10          9           8


   Access
    Reset


         Bit        7             6           5            4             3     2          1           0
                                                                              IDLE      MDIO
   Access                                                                      R         R
    Reset                                                                      1          0


               Bit 2 – IDLE PHY Management Logic Idle
               The PHY management logic is idle (i.e., has completed).

               Bit 1 – MDIO MDIO Input Status
               Returns status of the MDIO pin.




           © 2019 Microchip Technology Inc.                     Datasheet                 DS60001507E-page 529
                                                        SAM D5x/E5x Family Data Sheet
                                                                         GMAC - Ethernet MAC

24.9.4         GMAC User Register

               Name:       UR
               Offset:     0x00C
               Reset:      0x00000000
               Property:   -


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
                                                                                          MII
   Access                                                                                R/W
    Reset                                                                                 0


               Bit 0 – MII Reduced MII Mode
               Value       Description
               0           RMII mode is selected
               1           MII mode is selected




           © 2019 Microchip Technology Inc.             Datasheet             DS60001507E-page 530
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                     GMAC - Ethernet MAC

24.9.5         GMAC DMA Configuration Register

               Name:        DCFGR
               Offset:      0x010
               Reset:       0x00020004
               Property:    Read/Write


         Bit        31            30             29            28                  27      26            25                24
                                                                                                                       DDRP
   Access
    Reset                                                                                                                  0


         Bit        23            22             21            20                  19      18            17                16
                                                                       DRBS[7:0]
   Access
    Reset            0             0             0                 0               0        0             1                0


         Bit        15            14             13            12                  11      10             9                8
                                                                              TXCOEN     TXPBMS               RXBMS[1:0]
   Access
    Reset                                                                          0        0             0                0


         Bit         7             6             5                 4               3        2             1                0
                   ESPA          ESMA                                                   FBLDO[4:0]
   Access
    Reset            0             0                               0               0        1             0                0


               Bit 24 – DDRP DMA Discard Receive Packets
               A write to this bit is ignored if the DMA is not configured in the packet buffer full store and forward mode.
               Value        Description
               0            Received packets are stored in the SRAM based packet buffer until next AHB buffer
                            resource becomes available.
               1            Receive packets from the receiver packet buffer memory are automatically discarded when
                            no AHB resource is available.

               Bits 23:16 – DRBS[7:0] DMA Receive Buffer Size
               These bits defined by these bits determines the size of buffer to use in main AHB system memory when
               writing received data.
               The value is defined in multiples of 64 bytes. For example:
                • 0x02: 128 bytes
                • 0x18: 1536 bytes (1 × max length frame/buffer)
                • 0xA0: 10240 bytes (1 × 10K jumbo frame/buffer)


                  WARNING
                            Do not write 0x00 to this bit field.




           © 2019 Microchip Technology Inc.                              Datasheet                        DS60001507E-page 531
                                                  SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

 Value   Description
 0x00    Reserved
 0x01-0x 1..255 x 64 byte buffer
 FF

Bit 11 – TXCOEN Transmitter Checksum Generation Offload Enable
Transmitter IP, TCP and UDP checksum generation offload enable.
 Value      Description
 0          Frame data is unaffected.
 1          The transmitter checksum generation engine calculates and substitutes checksums for
            transmit frames.

Bit 10 – TXPBMS Transmitter Packet Buffer Memory Size Select
When written to zero, the amount of memory used for the transmit packet buffer is reduced by 50%. This
reduces the amount of memory used by the GMAC.
It is important to write this bit to '1' if the full configured physical memory is available. The value in
parentheses represents the size that would result for the default maximum configured memory size of
4KBytes.
 Value       Description
 0           Top address bits not used. (2KByte used.)
 1           Full configured addressable space (4KBytes) used.

Bits 9:8 – RXBMS[1:0] Receiver Packet Buffer Memory Size Select
The default receive packet buffer size is FULL=RECEIVE_BUFFER_SIZE Kbytes. The table below shows
how to configure this memory to FULL, HALF, QUARTER or EIGHTH of the default size.
 Value      Name              Description
 0          EIGHTH            RECEIVE_BUFFER_SIZE/8 Kbyte Memory Size
 1          QUARTER           RECEIVE_BUFFER_SIZE/4 Kbytes Memory Size
 2          HALF              RECEIVE_BUFFER_SIZE/2 Kbytes Memory Size
 3          FULL              RECEIVE_BUFFER_SIZE Kbytes Memory Size

Bit 7 – ESPA Endian Swap Mode Enable for Packet Data Accesses
Value      Description
0          Little endian mode for AHB transfers selected.
1          Big endian mode for AHB transfers selected.

Bit 6 – ESMA Endian Swap Mode Enable for Management Descriptor Accesses
Value      Description
0          Little endian mode for AHB transfers selected.
1          Big endian mode for AHB transfers selected.

Bits 4:0 – FBLDO[4:0] Fixed Burst Length for DMA Data Operations
Selects the burst length to attempt to use on the AHB when transferring frame data. Not used for DMA
management operations and only used where space and data size allow. Otherwise SINGLE type AHB
transfers are used.
One-hot priority encoding enforced automatically on register writes as follows. ‘x’ represents don’t care.
 Value      Name            Description
 0          -               Reserved
 1          SINGLE          00001: Always use SINGLE AHB bursts




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 532
                                                        SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

 Value        Name                 Description
 2            -                    Reserved
 4            INCR4                001xx: Attempt to use INCR4 AHB bursts (Default)
 8            INCR8                01xxx: Attempt to use INCR8 AHB bursts
 16           INCR16               1xxxx: Attempt to use INCR16 AHB bursts




© 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 533
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                               GMAC - Ethernet MAC

24.9.6         GMAC Transmit Status Register

               Name:        TSR
               Offset:      0x014
               Reset:       0x00000000
               Property:    -


         Bit         31            30            29          28            27            26           25            24


   Access
    Reset


         Bit         23            22            21          20            19            18           17            16


   Access
    Reset


         Bit         15            14            13          12            11            10            9            8
                                                                                                                  HRESP
   Access                                                                                                          R/W
    Reset                                                                                                           0


         Bit         7             6             5            4            3             2             1            0
                                  UND         TXCOMP         TFC         TXGO           RLE          COL           UBR
   Access                         R/W           R/W          R/W          R/W           R/W          R/W           R/W
    Reset                          0             0            0            0             0             0            0


               Bit 8 – HRESP HRESP Not OK
               Set when the DMA block sees HRESP not OK.
               This bit is cleared by writing a '1' to it.

               Bit 6 – UND Transmit Underrun
               This bit is set if the transmitter was forced to terminate the transmission of a frame due to further data
               being unavailable.
               This bit is also set if a transmitter status write back has not completed when another status write back is
               attempted.
               When using the DMA interface configured for internal FIFO mode, this bit is also set when the transmit
               DMA has written the SOP data into the FIFO and either the AHB bus was not granted in time for further
               data, or an AHB not OK response was returned, or a used bit was read.
               This bit is cleared by writing a '1' to it.

               Bit 5 – TXCOMP Transmit Complete
               Set when a frame has been transmitted.
               This bit is cleared by writing a '1' to it.

               Bit 4 – TFC Transmit Frame Corruption Due to AHB Error
               This bit is set when an error occurs during reading transmit frame from the AHB. Error causes include
               HRESP errors and buffers exhausted mid frame. (If the buffers run out during transmission of a frame
               then transmission stops, FCS shall be bad and GTXER asserted).




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 534
                                                     SAM D5x/E5x Family Data Sheet
                                                                                   GMAC - Ethernet MAC

In DMA packet buffer mode, this bit is also set if a single frame is too large for the configured packet
buffer memory size.
This bit is cleared by writing a '1' to it.

Bit 3 – TXGO Transmit Go
This bit is '1' when transmit is active. When using the DMA interface this bit represents the TXGO variable
as specified in the transmit buffer description.

Bit 2 – RLE Retry Limit Exceeded
This bit is cleared by writing a '1' to it.

Bit 1 – COL Collision Occurred
When operating in 10/100Mbps mode, this bit is set by the assertion of either a collision or a late collision.
This bit is cleared by writing a '1' to it.

Bit 0 – UBR Used Bit Read
This bit is set when a transmit buffer descriptor is read with its used bit set.
This bit is cleared by writing a '1' to it.




© 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 535
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                                GMAC - Ethernet MAC

24.9.7         GMAC Receive Buffer Queue Base Address Register

               Name:        RBQB
               Offset:      0x018
               Reset:       0x00000000
               Property:    Read/Write

               This register holds the start address of the receive buffer queue (receive buffers descriptor list). The
               receive buffer queue base address must be initialized before receive is enabled through bit 2 of the
               Network Control Register. Once reception is enabled, any write to the Receive Buffer Queue Base
               Address Register is ignored. Reading this register returns the location of the descriptor currently being
               accessed. This value increments as buffers are used. Software should not use this register for
               determining where to remove received frames from the queue as it constantly changes as new frames
               are received. Software should instead work its way through the buffer descriptor queue checking the
               “used” bits.
               In terms of AMBA AHB operation, the descriptors are read from memory using a single 32-bit AHB
               access. The descriptors should be aligned at 32-bit boundaries and the descriptors are written to using
               two individual non sequential accesses.

         Bit        31            30           29                28                 27    26          25            24
                                                                      ADDR[29:22]
   Access          R/W           R/W           R/W               R/W                R/W   R/W        R/W           R/W
    Reset            0            0             0                 0                  0     0          0             0


         Bit        23            22           21                20                 19    18          17            16
                                                                      ADDR[21:14]
   Access          R/W           R/W           R/W               R/W                R/W   R/W        R/W           R/W
    Reset            0            0             0                 0                  0     0          0             0


         Bit        15            14           13                12                 11    10          9             8
                                                                       ADDR[13:6]
   Access          R/W           R/W           R/W               R/W                R/W   R/W        R/W           R/W
    Reset            0            0             0                 0                  0     0          0             0


         Bit         7            6             5                 4                  3     2          1             0
                                                     ADDR[5:0]
   Access          R/W           R/W           R/W               R/W                R/W   R/W
    Reset            0            0             0                 0                  0     0


               Bits 31:2 – ADDR[29:0] Receive Buffer Queue Base Address
               Written with the address of the start of the receive queue.




           © 2019 Microchip Technology Inc.                               Datasheet                    DS60001507E-page 536
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                               GMAC - Ethernet MAC

24.9.8         GMAC Transmit Buffer Queue Base Address Register

               Name:       TBQB
               Offset:     0x01C
               Reset:      0x00000000
               Property:   -

               This register holds the start address of the transmit buffer queue (transmit buffers descriptor list). The
               Transmit Buffer Queue Base Address Register must be initialized before transmit is started through bit 9
               of the Network Control Register. Once transmission has started, any write to the Transmit Buffer Queue
               Base Address Register is illegal and therefore ignored.
               Note that due to clock boundary synchronization, it takes a maximum of four MCK cycles from the writing
               of the transmit start bit before the transmitter is active. Writing to the Transmit Buffer Queue Base
               Address Register during this time may produce unpredictable results.
               Reading this register returns the location of the descriptor currently being accessed. Since the DMA
               handles two frames at once, this may not necessarily be pointing to the current frame being transmitted.
               In terms of AMBA AHB operation, the descriptors are written to memory using a single 32-bit AHB
               access. The descriptors should be aligned at 32-bit boundaries and the descriptors are read from
               memory using two individual non sequential accesses.

         Bit        31            30           29               28                 27    26          25            24
                                                                     ADDR[29:22]
   Access          R/W           R/W          R/W               R/W                R/W   R/W        R/W           R/W
    Reset            0            0             0                0                  0     0           0            0


         Bit        23            22           21               20                 19    18          17            16
                                                                     ADDR[21:14]
   Access          R/W           R/W          R/W               R/W                R/W   R/W        R/W           R/W
    Reset            0            0             0                0                  0     0           0            0


         Bit        15            14           13               12                 11    10           9            8
                                                                      ADDR[13:6]
   Access          R/W           R/W          R/W               R/W                R/W   R/W        R/W           R/W
    Reset            0            0             0                0                  0     0           0            0


         Bit         7            6             5                4                  3     2           1            0
                                                    ADDR[5:0]
   Access          R/W           R/W          R/W               R/W                R/W   R/W
    Reset            0            0             0                0                  0     0


               Bits 31:2 – ADDR[29:0] Transmit Buffer Queue Base Address
               Written with the address of the start of the transmit queue.




           © 2019 Microchip Technology Inc.                              Datasheet                    DS60001507E-page 537
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                GMAC - Ethernet MAC

24.9.9         GMAC Receive Status Register

               Name:        RSR
               Offset:      0x020
               Reset:       0x00000000
               Property:    -

               This register, when read, provides receive status details. Once read, individual bits may be cleared by
               writing a '1' to them. It is not possible to set a bit to '1' by writing to this register.

         Bit        31            30            29            28            27            26            25            24


   Access
    Reset


         Bit        23            22            21            20            19            18            17            16


   Access
    Reset


         Bit        15            14            13            12            11            10             9            8


   Access
    Reset


         Bit         7             6             5             4             3             2             1            0
                                                                           HNO          RXOVR          REC           BNA
   Access                                                                  R/W           R/W           R/W           R/W
    Reset                                                                    0             0             0            0


               Bit 3 – HNO HRESP Not OK
               This bit is set when the DMA block sees HRESP not OK.
               This bit is cleared by writing a '1' to it.

               Bit 2 – RXOVR Receive Overrun
               This bit is set if the receive status was not taken at the end of the frame. The buffer will be recovered if an
               overrun occurs.
               This bit is cleared by writing a '1' to it.

               Bit 1 – REC Frame Received
               This bit is set to when one or more frames have been received and placed in memory.
               This bit is cleared by writing a '1' to it.

               Bit 0 – BNA Buffer Not Available
               When this bit is set, an attempt was made to get a new buffer and the pointer indicated that it was owned
               by the processor. The DMA will re-read the pointer each time an end of frame is received until a valid
               pointer is found. This bit is set following each descriptor read attempt that fails, even if consecutive
               pointers are unsuccessful and software has in the mean time cleared the status flag.
               This bit is cleared by writing a '1' to it.




           © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 538
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                              GMAC - Ethernet MAC

24.9.10 GMAC Interrupt Status Register

            Name:        ISR
            Offset:      0x024
            Reset:       0x00000000
            Property:    -

            This register indicates the source of the interrupt. An interrupt source must be enabled in the mask
            register first so the corresponding bits of this register will be set and the GMAC interrupt signal will be
            asserted in the system.

      Bit        31            30            29            28            27            26            25            24
                                           TSUCMP         WOL                          SRI         PDRSFT       PDRQFT
  Access                                      W             R                           R             R             R
   Reset                                      0             0                           0             0             0


      Bit        23            22            21            20            19            18            17            16
               PDRSFR       PDRQFR           SFT         DRQFT           SFR         DRQFR
  Access          R             R             R             R             R             R
   Reset          0             0             0             0             0             0


      Bit        15            14            13            12            11            10             9             8
                              PFTR           PTZ          PFNZ         HRESP          ROVR
  Access                        R             R             R             R             R
   Reset                        0             0             0             0             0


      Bit         7             6             5             4             3             2             1             0
               TCOMP           TFC          RLEX           TUR         TXUBR         RXUBR         RCOMP          MFS
  Access          R             R             R             R             R             R             R             R
   Reset          0             0             0             0             0             0             0             0


            Bit 29 – TSUCMP TSU Timer Comparison
            Indicates TSU times count and comparison value are equal.

            Bit 28 – WOL Wake On LAN
            WOL interrupt. Indicates a WOL message has been received.

            Bit 26 – SRI TSU Seconds Register Increment
            Indicates the register has incremented.
            Cleared on read.

            Bit 25 – PDRSFT PDelay Response Frame Transmitted
            Indicates a PTP pdelay_resp frame has been transmitted.
            Cleared on read.

            Bit 24 – PDRQFT PDelay Request Frame Transmitted
            Indicates a PTP pdelay_req frame has been transmitted.
            Cleared on read.




        © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 539
                                                  SAM D5x/E5x Family Data Sheet
                                                                             GMAC - Ethernet MAC

Bit 23 – PDRSFR PDelay Response Frame Received
Indicates a PTP pdelay_resp frame has been received.
Cleared on read.

Bit 22 – PDRQFR PDelay Request Frame Received
Indicates a PTP pdelay_req frame has been received.
Cleared on read.

Bit 21 – SFT PTP Sync Frame Transmitted
Indicates a PTP sync frame has been transmitted.
Cleared on read.

Bit 20 – DRQFT PTP Delay Request Frame Transmitted
Indicates a PTP delay_req frame has been transmitted.
Cleared on read.

Bit 19 – SFR PTP Sync Frame Received
Indicates a PTP sync frame has been received.
Cleared on read.

Bit 18 – DRQFR PTP Delay Request Frame Received
Indicates a PTP delay_req frame has been received.
Cleared on read.

Bit 14 – PFTR Pause Frame Transmitted
Indicates a pause frame has been successfully transmitted after being initiated from the Network Control
Register.
Cleared on read.

Bit 13 – PTZ Pause Time Zero
Set when either the Pause Time Register at address 0x38 decrements to zero, or when a valid pause
frame is received with a zero pause quantum field.
Cleared on read.

Bit 12 – PFNZ Pause Frame with Non-zero Pause Quantum Received
Indicates a valid pause has been received that has a non-zero pause quantum field.
Cleared on read.

Bit 11 – HRESP HRESP Not OK
Set when the DMA block sees HRESP not OK.
Cleared on read.

Bit 10 – ROVR Receive Overrun
Set when the receive overrun status bit is set.
Cleared on read.

Bit 7 – TCOMP Transmit Complete
Set when a frame has been transmitted.
Cleared on read.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 540
                                                   SAM D5x/E5x Family Data Sheet
                                                                                GMAC - Ethernet MAC

Bit 6 – TFC Transmit Frame Corruption Due to AHB Error
Transmit frame corruption due to AHB error. Set if an error occurs during reading a transmit frame from
the AHB, including HRESP errors and buffers exhausted mid frame.

Bit 5 – RLEX Retry Limit Exceeded
Retry Limit Exceeded Transmit error.
Cleared on read.

Bit 4 – TUR Transmit Underrun
This interrupt is set if the transmitter was forced to terminate an ongoing frame transmission due to further
data being unavailable.
This interrupt is also set if a transmitter status write back has not completed when another status write
back is attempted.
This interrupt is also set when the transmit DMA has written the SOP data into the FIFO and either the
AHB bus was not granted in time for further data, or because an AHB not OK response was returned, or
because the used bit was read.

Bit 3 – TXUBR TX Used Bit Read
Set when a transmit buffer descriptor is read with its used bit set.
Cleared on read.

Bit 2 – RXUBR RX Used Bit Read
Set when a receive buffer descriptor is read with its used bit set.
Cleared on read.

Bit 1 – RCOMP Receive Complete
A frame has been stored in memory.
Cleared on read.

Bit 0 – MFS Management Frame Sent
The PHY Maintenance Register has completed its operation.
Cleared on read.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 541
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                GMAC - Ethernet MAC

24.9.11 GMAC Interrupt Enable Register

            Name:           IER
            Offset:         0x028
            Reset:          –
            Property:       Write-only

            This register is write-only and will always return zero.
            The following values are valid for all listed bit names of this register:
            0: No effect.
            1: Enables the corresponding interrupt.

      Bit         31              30          29            28             27            26         25           24
                                           TSUCMP          WOL                           SRI      PDRSFT      PDRQFT
  Access                                      W              W                           W          W            W
   Reset                                       –             –                            –          –           –


      Bit         23              22          21            20             19            18         17           16
               PDRSFR          PDRQFR        SFT          DRQFT           SFR           DRQFR
  Access          W               W           W              W             W             W
   Reset          –               –            –             –             –              –


      Bit         15              14          13            12             11            10          9           8
                EXINT           PFTR         PTZ           PFNZ         HRESP           ROVR
  Access          W               W           W              W             W             W
   Reset          –               –            –             –             –              –


      Bit         7               6            5             4             3              2          1           0
               TCOMP             TFC         RLEX          TUR          TXUBR           RXUBR      RCOMP        MFS
  Access          W               W           W              W             W             W          W            W
   Reset          –               –            –             –             –              –          –           –


            Bit 29 – TSUCMP TSU Timer Comparison

            Bit 28 – WOL Wake On LAN

            Bit 26 – SRI TSU Seconds Register Increment

            Bit 25 – PDRSFT PDelay Response Frame Transmitted

            Bit 24 – PDRQFT PDelay Request Frame Transmitted

            Bit 23 – PDRSFR PDelay Response Frame Received

            Bit 22 – PDRQFR PDelay Request Frame Received

            Bit 21 – SFT PTP Sync Frame Transmitted

            Bit 20 – DRQFT PTP Delay Request Frame Transmitted




        © 2019 Microchip Technology Inc.                           Datasheet                         DS60001507E-page 542
                                               SAM D5x/E5x Family Data Sheet
                                                                 GMAC - Ethernet MAC

Bit 19 – SFR PTP Sync Frame Received

Bit 18 – DRQFR PTP Delay Request Frame Received

Bit 15 – EXINT External Interrupt

Bit 14 – PFTR Pause Frame Transmitted

Bit 13 – PTZ Pause Time Zero

Bit 12 – PFNZ Pause Frame with Non-zero Pause Quantum Received

Bit 11 – HRESP HRESP Not OK

Bit 10 – ROVR Receive Overrun

Bit 7 – TCOMP Transmit Complete

Bit 6 – TFC Transmit Frame Corruption Due to AHB Error

Bit 5 – RLEX Retry Limit Exceeded or Late Collision

Bit 4 – TUR Transmit Underrun

Bit 3 – TXUBR TX Used Bit Read

Bit 2 – RXUBR RX Used Bit Read

Bit 1 – RCOMP Receive Complete

Bit 0 – MFS Management Frame Sent
.
Cleared on read.




© 2019 Microchip Technology Inc.                 Datasheet            DS60001507E-page 543
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                GMAC - Ethernet MAC

24.9.12 GMAC Interrupt Disable Register

            Name:           IDR
            Offset:         0x02C
            Reset:          –
            Property:       Write-only

            This register is write-only and will always return zero.
            The following values are valid for all listed bit names of this register:
            0: No effect.
            1: Disables the corresponding interrupt.

      Bit         31              30          29            28             27            26         25           24
                                           TSUCMP          WOL         RXLPISBC          SRI      PDRSFT      PDRQFT
  Access                                      W              W             R             W          W            W
   Reset                                       –             –             –              –          –           –


      Bit         23              22          21            20             19            18         17           16
               PDRSFR          PDRQFR        SFT          DRQFT           SFR           DRQFR
  Access          W               W           W              W             W             W
   Reset          –               –            –             –             –              –


      Bit         15              14          13            12             11            10          9           8
                EXINT           PFTR         PTZ           PFNZ         HRESP           ROVR
  Access          W               W           W              W             W             W
   Reset          –               –            –             –             –              –


      Bit         7               6            5             4             3              2          1           0
               TCOMP             TFC         RLEX          TUR          TXUBR           RXUBR      RCOMP        MFS
  Access          W               W           W              W             W             W          W            W
   Reset          –               –            –             –             –              –          –           –


            Bit 29 – TSUCMP TSU Timer Comparison

            Bit 28 – WOL Wake On LAN

            Bit 27 – RXLPISBC Receive LPI indication Status Bit Change
            Receive LPI indication status bit change.
            Cleared on read.

            Bit 26 – SRI TSU Seconds Register Increment

            Bit 25 – PDRSFT PDelay Response Frame Transmitted

            Bit 24 – PDRQFT PDelay Request Frame Transmitted

            Bit 23 – PDRSFR PDelay Response Frame Received

            Bit 22 – PDRQFR PDelay Request Frame Received




        © 2019 Microchip Technology Inc.                           Datasheet                         DS60001507E-page 544
                                               SAM D5x/E5x Family Data Sheet
                                                                 GMAC - Ethernet MAC

Bit 21 – SFT PTP Sync Frame Transmitted

Bit 20 – DRQFT PTP Delay Request Frame Transmitted

Bit 19 – SFR PTP Sync Frame Received

Bit 18 – DRQFR PTP Delay Request Frame Received

Bit 15 – EXINT External Interrupt

Bit 14 – PFTR Pause Frame Transmitted

Bit 13 – PTZ Pause Time Zero

Bit 12 – PFNZ Pause Frame with Non-zero Pause Quantum Received

Bit 11 – HRESP HRESP Not OK

Bit 10 – ROVR Receive Overrun

Bit 7 – TCOMP Transmit Complete

Bit 6 – TFC Transmit Frame Corruption Due to AHB Error

Bit 5 – RLEX Retry Limit Exceeded or Late Collision

Bit 4 – TUR Transmit Underrun

Bit 3 – TXUBR TX Used Bit Read

Bit 2 – RXUBR RX Used Bit Read

Bit 1 – RCOMP Receive Complete

Bit 0 – MFS Management Frame Sent




© 2019 Microchip Technology Inc.                 Datasheet            DS60001507E-page 545
                                                                SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

24.9.13 GMAC Interrupt Mask Register

           Name:        IMR
           Offset:      0x030
           Reset:       0x07FFFFFF
           Property:    -

           This register is a read-only register indicating which interrupts are masked. All bits are set at Reset and
           can be reset individually by writing to the Interrupt Enable Register (IER), or set individually by writing to
           the Interrupt Disable Register (IDR).
           For test purposes there is a write-only function to this register that allows the bits in the Interrupt Status
           Register to be set or cleared, regardless of the state of the mask register. A write to this register directly
           affects the state of the corresponding bit in the Interrupt Status Register, causing an interrupt to be
           generated if a 1 is written.
           The following values are valid for all listed bit names of this register when read:
           0: The corresponding interrupt is enabled.
           1: The corresponding interrupt is not enabled.

     Bit        31             30            29            28            27            26            25            24
                                          TSUCMP          WOL                         SRI         PDRSFT        PDRQFT
  Access                                     W             R                           R             R             R
   Reset                                     0              0                          1              1             1


     Bit        23             22            21            20            19            18            17            16
              PDRSFR        PDRQFR          SFT         DRQFT           SFR          DRQFR
  Access         R             R             R             R             R             R
   Reset         1             1             1              1            1             1


     Bit        15             14            13            12            11            10             9             8
               EXINT         PFTR           PTZ          PFNZ          HRESP         ROVR
  Access         R             R             R             R             R             R
   Reset         1             1             1              1            1             1


     Bit         7             6             5              4            3             2              1             0
              TCOMP           TFC          RLEX           TUR          TXUBR         RXUBR        RCOMP           MFS
  Access         R             R             R             R             R             R             R             R
   Reset         1             1             1              1            1             1              1             1


           Bit 29 – TSUCMP TSU Timer Comparison
           Indicates TSU times count and comparison value are equal.

           Bit 28 – WOL Wake On LAN
           WOL interrupt. Indicates a WOL message has been received.

           Bit 26 – SRI TSU Seconds Register Increment
           Indicates the register has incremented.
           Cleared on read.




       © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 546
                                             SAM D5x/E5x Family Data Sheet
                                                                 GMAC - Ethernet MAC

Bit 25 – PDRSFT PDelay Response Frame Transmitted

Bit 24 – PDRQFT PDelay Request Frame Transmitted

Bit 23 – PDRSFR PDelay Response Frame Received

Bit 22 – PDRQFR PDelay Request Frame Received

Bit 21 – SFT PTP Sync Frame Transmitted

Bit 20 – DRQFT PTP Delay Request Frame Transmitted

Bit 19 – SFR PTP Sync Frame Received

Bit 18 – DRQFR PTP Delay Request Frame Received

Bit 15 – EXINT External Interrupt

Bit 14 – PFTR Pause Frame Transmitted

Bit 13 – PTZ Pause Time Zero

Bit 12 – PFNZ Pause Frame with Non-zero Pause Quantum Received

Bit 11 – HRESP HRESP Not OK

Bit 10 – ROVR Receive Overrun

Bit 7 – TCOMP Transmit Complete

Bit 6 – TFC Transmit Frame Corruption Due to AHB Error

Bit 5 – RLEX Retry Limit Exceeded

Bit 4 – TUR Transmit Underrun

Bit 3 – TXUBR TX Used Bit Read

Bit 2 – RXUBR RX Used Bit Read

Bit 1 – RCOMP Receive Complete

Bit 0 – MFS Management Frame Sent




© 2019 Microchip Technology Inc.               Datasheet              DS60001507E-page 547
                                                           SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.14 GMAC PHY Maintenance Register

       Name:          MAN
       Offset:        0x034
       Reset:         0x00000000
       Property:      Read/Write

       This register is a shift register. Writing to it starts a shift operation which is signaled completed when bit 2
       is set in the Network Status Register (NSR). It takes about 2000 MCK cycles to complete, when MDC is
       set for MCK divide by 32 in the Network Configuration Register. An interrupt is generated upon
       completion.
       During this time, the MSB of the register is output on the MDIO pin and the LSB updated from the MDIO
       pin with each MDC cycle. This causes transmission of a PHY management frame on MDIO. Refer also to
       section 22.2.4.5 of the IEEE 802.3 standard.
       Reading during the shift operation returns the current contents of the shift register. At the end of
       management operation, the bits will have shifted back to their original locations. For a read operation, the
       data bits are updated with data read from the PHY. It is important to write the correct values to the register
       to ensure a valid PHY management frame is produced.
       The MDIO interface can read IEEE 802.3 clause 45 PHYs, as well as clause 22 PHYs. To read clause 45
       PHYs, bit 30 should be written with a '0' rather than a '1'. To write clause 45 PHYs, bits 31:28 should be
       written as 0x1:

        PHY                     Access                         Bit Value
                                                               WZO          CLTTO           OP[1]         OP[0]
        Clause 22               Read                           0            1               1             0
                                Write                          0            1               0             1
        Clause 45               Read                           0            0               1             1
                                Write                          0            0               0             1
                                Read + Address                 0            0               1             0

       For a description of MDC generation, see also the 'GMAC Network Configuration Register' (NCR)
       description.




       © 2019 Microchip Technology Inc.                      Datasheet                            DS60001507E-page 548
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

   Bit        31            30           29             28                 27    26                25               24
             WZO          CLTTO               OP[1:0]                                  PHYA[4:1]
Access       R/W           R/W          R/W             R/W                R/W   R/W               R/W              R/W
 Reset         0            0             0              0                  0     0                 0                0


   Bit        23            22           21             20                 19    18                17               16
           PHYA[0:0]                                REGA[4:0]                                            WTN[1:0]
Access       R/W           R/W          R/W             R/W                R/W   R/W               R/W              R/W
 Reset         0            0             0              0                  0     0                 0                0


   Bit        15            14           13             12                 11    10                 9                8
                                                              DATA[15:8]
Access       R/W           R/W          R/W             R/W                R/W   R/W               R/W              R/W
 Reset         0            0             0              0                  0     0                 0                0


   Bit         7            6             5              4                  3     2                 1                0
                                                              DATA[7:0]
Access       R/W           R/W          R/W             R/W                R/W   R/W               R/W              R/W
 Reset         0            0             0              0                  0     0                 0                0


         Bit 31 – WZO Write ZERO
         Must be written to '0'.
         Value       Description
         0           Mandatory
         1           Reserved

         Bit 30 – CLTTO Clause 22 Operation
         Value      Description
         0          Clause 45 operation
         1          Clause 22 operation

         Bits 29:28 – OP[1:0] Operation
         Value       Description
         01          Write
         10          Read
         Other       Reseved

         Bits 27:23 – PHYA[4:0] PHY Address

         Bits 22:18 – REGA[4:0] Register Address
         Specifies the register in the PHY to access.

         Bits 17:16 – WTN[1:0] Write Ten
         Must be written to '10'.
         Value       Description
         10          Mandatory
         Other       Reserved




     © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 549
                                                     SAM D5x/E5x Family Data Sheet
                                                                                   GMAC - Ethernet MAC

Bits 15:0 – DATA[15:0] PHY Data
For a write operation, this field is written with the data to be written to the PHY.
After a read operation, this field contains the data read from the PHY.




© 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 550
                                                           SAM D5x/E5x Family Data Sheet
                                                                                     GMAC - Ethernet MAC

24.9.15 GMAC Receive Pause Quantum Register

           Name:       RPQ
           Offset:     0x038
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29          28               27      26           25           24


  Access
   Reset


     Bit        23           22           21          20               19      18           17           16


  Access
   Reset


     Bit        15           14           13          12               11      10           9            8
                                                           RPQ[15:8]
  Access        R             R           R           R                R        R           R            R
   Reset        0             0           0           0                0        0           0            0


     Bit        7             6           5           4                3        2           1            0
                                                           RPQ[7:0]
  Access        R             R           R           R                R        R           R            R
   Reset        0             0           0           0                0        0           0            0


           Bits 15:0 – RPQ[15:0] Received Pause Quantum
           Stores the current value of the Receive Pause Quantum Register which is decremented every 512 bit
           times.




       © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 551
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.16 GMAC Transmit Pause Quantum Register

           Name:       TPQ
           Offset:     0x03C
           Reset:      0x0000FFFF
           Property:   -


     Bit        31           30           29          28                27      26        25           24


  Access
   Reset


     Bit        23           22           21          20                19      18        17           16


  Access
   Reset


     Bit        15           14           13          12                11      10         9           8
                                                            TPQ[15:8]
  Access       R/W          R/W           R/W         R/W               R/W     R/W       R/W         R/W
   Reset        1             1            1           1                 1       1         1           1


     Bit        7             6            5           4                 3       2         1           0
                                                            TPQ[7:0]
  Access       R/W          R/W           R/W         R/W               R/W     R/W       R/W         R/W
   Reset        1             1            1           1                 1       1         1           1


           Bits 15:0 – TPQ[15:0] Transmit Pause Quantum
           Written with the pause quantum value for pause frame transmission.




       © 2019 Microchip Technology Inc.                       Datasheet                    DS60001507E-page 552
                                                            SAM D5x/E5x Family Data Sheet
                                                                                   GMAC - Ethernet MAC

24.9.17 GMAC TX Partial Store and Forward Register

            Name:       TPSF
            Offset:     0x040
            Reset:      0x00000FFF
            Property:   -


      Bit        31           30           29        28              27       26           25              24
               ENTXP
  Access        R/W
   Reset         0


      Bit        23           22           21        20              19       18           17              16


  Access
   Reset


      Bit        15           14           13        12              11       10           9               8
                                                                               TPB1ADR[11:8]
  Access                                                            R/W      R/W          R/W             R/W
   Reset                                                                 1    1            1               1


      Bit        7             6            5         4                  3    2            1               0
                                                          TPB1ADR[7:0]
  Access        R/W          R/W           R/W       R/W            R/W      R/W          R/W             R/W
   Reset         1             1            1         1                  1    1            1               1


            Bit 31 – ENTXP Enable TX Partial Store and Forward Operation

            Bits 11:0 – TPB1ADR[11:0] Transmit Partial Store and Forward Address
            Watermark value.




        © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 553
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  GMAC - Ethernet MAC

24.9.18 GMAC RX Partial Store and Forward Register

            Name:       RPSF
            Offset:     0x044
            Reset:      0x00000FFF
            Property:   -


      Bit        31           30           29        28             27       26           25              24
               ENRXP
  Access         R
   Reset         0


      Bit        23           22           21        20             19       18           17              16


  Access
   Reset


      Bit        15           14           13        12             11       10           9               8
                                                                              RPB1ADR[11:8]
  Access                                                           R/W      R/W          R/W             R/W
   Reset                                                                1    1            1               1


      Bit        7             6            5        4                  3    2            1               0
                                                         RPB1ADR[7:0]
  Access        R/W          R/W           R/W      R/W            R/W      R/W          R/W             R/W
   Reset         1             1            1        1                  1    1            1               1


            Bit 31 – ENRXP Enable RX Partial Store and Forward Operation

            Bits 11:0 – RPB1ADR[11:0] Receive Partial Store and Forward Address
            Watermark value. Reset = 1.




        © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 554
                                                          SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

24.9.19 GMAC RX Jumbo Frame Max Length Register

           Name:       RJFML
           Offset:     0x048
           Reset:      0x00003FFF
           Property:   -


     Bit        31           30           29        28               27                26        25           24


  Access
   Reset


     Bit        23           22           21        20               19                18        17           16


  Access
   Reset


     Bit        15           14           13        12               11                10         9           8
                                                                           FML[13:8]
  Access                                  R/W       R/W              R/W               R/W       R/W         R/W
   Reset                                   1         1                1                 1         1           1


     Bit        7             6            5         4                3                 2         1           0
                                                          FML[7:0]
  Access       R/W          R/W           R/W       R/W              R/W               R/W       R/W         R/W
   Reset        1             1            1         1                1                 1         1           1


           Bits 13:0 – FML[13:0] Frame Max Length
           Rx jumbo frame maximum length.




       © 2019 Microchip Technology Inc.                    Datasheet                              DS60001507E-page 555
                                                               SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.20 GMAC Hash Register Bottom

           Name:       HRB
           Offset:     0x080
           Reset:      0x00000000
           Property:   Read/Write

           The unicast hash enable (UNIHEN) and the multicast hash enable (MITIHEN) bits in the Network
           Configuration Register (NCFGR) enable the reception of hash matched frames.

     Bit        31            30           29            28                 27   26        25             24
                                                              ADDR[31:24]
  Access       R/W           R/W          R/W           R/W                R/W   R/W       R/W            R/W
   Reset         0            0             0            0                  0     0         0              0


     Bit        23            22           21            20                 19   18        17             16
                                                              ADDR[23:16]
  Access       R/W           R/W          R/W           R/W                R/W   R/W       R/W            R/W
   Reset         0            0             0            0                  0     0         0              0


     Bit        15            14           13            12                 11   10         9              8
                                                              ADDR[15:8]
  Access       R/W           R/W          R/W           R/W                R/W   R/W       R/W            R/W
   Reset         0            0             0            0                  0     0         0              0


     Bit         7            6             5            4                  3     2         1              0
                                                               ADDR[7:0]
  Access       R/W           R/W          R/W           R/W                R/W   R/W       R/W            R/W
   Reset         0            0             0            0                  0     0         0              0


           Bits 31:0 – ADDR[31:0] Hash Address
           The first 32 bits of the Hash Address Register.




       © 2019 Microchip Technology Inc.                          Datasheet                  DS60001507E-page 556
                                                                SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.21 GMAC Hash Register Top

           Name:       HRT
           Offset:     0x084
           Reset:      0x00000000
           Property:   Read/Write

           The Unicast Hash Enable (UNIHEN) and the Multicast Hash Enable (MITIHEN) bits in the Network
           Configuration Register (NCFGR) enable the reception of hash matched frames.

     Bit        31           30           29             28                 27    26        25           24
                                                              ADDR[31:24]
  Access       R/W          R/W           R/W            R/W                R/W   R/W       R/W         R/W
   Reset         0            0            0              0                  0     0         0            0


     Bit        23           22           21             20                 19    18        17           16
                                                              ADDR[23:16]
  Access       R/W          R/W           R/W            R/W                R/W   R/W       R/W         R/W
   Reset         0            0            0              0                  0     0         0            0


     Bit        15           14           13             12                 11    10         9            8
                                                               ADDR[15:8]
  Access       R/W          R/W           R/W            R/W                R/W   R/W       R/W         R/W
   Reset         0            0            0              0                  0     0         0            0


     Bit         7            6            5              4                  3     2         1            0
                                                               ADDR[7:0]
  Access       R/W          R/W           R/W            R/W                R/W   R/W       R/W         R/W
   Reset         0            0            0              0                  0     0         0            0


           Bits 31:0 – ADDR[31:0] Hash Address
           Bits 63 to 32 of the Hash Address Register.




       © 2019 Microchip Technology Inc.                           Datasheet                  DS60001507E-page 557
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

24.9.22 GMAC Specific Address n Bottom Register

           Name:        SAB
           Offset:      0x88 + n*0x08 [n=0..3]
           Reset:       0x00000000
           Property:    -

           The addresses stored in the Specific Address Registers are deactivated at reset or when their
           corresponding Specific Address Register Bottom is written. They are activated when Specific Address
           Register Top is written.

     Bit        31            30            29            28                 27       26            25            24
                                                               ADDR[31:24]
  Access        R/W           R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0             0             0                  0        0             0                0


     Bit        23            22            21            20                 19       18            17            16
                                                               ADDR[23:16]
  Access        R/W           R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0             0             0                  0        0             0                0


     Bit        15            14            13            12                 11       10             9                8
                                                                ADDR[15:8]
  Access        R/W           R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0             0             0                  0        0             0                0


     Bit         7             6             5             4                  3        2             1                0
                                                                ADDR[7:0]
  Access        R/W           R/W           R/W           R/W                R/W     R/W           R/W           R/W
   Reset         0             0             0             0                  0        0             0                0


           Bits 31:0 – ADDR[31:0] Specific Address n
           Least significant 32 bits of the destination address, that is, bits 31:0. Bit zero indicates whether the
           address is multicast or unicast and corresponds to the least significant bit of the first byte received.




       © 2019 Microchip Technology Inc.                            Datasheet                         DS60001507E-page 558
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                              GMAC - Ethernet MAC

24.9.23 GMAC Specific Address n Top Register

           Name:        SAT
           Offset:      0x8C + n*0x08 [n=0..3]
           Reset:       0x00000000
           Property:    -

           The addresses stored in the Specific Address Registers are deactivated at reset or when their
           corresponding Specific Address Register Bottom is written. They are activated when Specific Address
           Register Top is written.

     Bit        31            30            29            28                 27         26        25           24


  Access
   Reset


     Bit        23            22            21            20                 19         18        17           16


  Access
   Reset


     Bit        15            14            13            12                 11         10         9           8
                                                                ADDR[15:8]
  Access        R/W           R/W           R/W           R/W                R/W        R/W       R/W         R/W
   Reset         0             0             0             0                  0          0         0           0


     Bit         7             6             5             4                  3          2         1           0
                                                                ADDR[7:0]
  Access        R/W           R/W           R/W           R/W                R/W        R/W       R/W         R/W
   Reset         0             0             0             0                  0          0         0           0


           Bits 15:0 – ADDR[15:0] Specific Address n
           The most significant bits of the destination address, that is, bits 47:32.




       © 2019 Microchip Technology Inc.                            Datasheet                       DS60001507E-page 559
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.24 GMAC Type ID Match n Register

           Name:       TIDM
           Offset:     0xA8 + n*0x04 [n=0..3]
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29           28               27      26        25           24
              ENIDn
  Access       R/W
   Reset        0


     Bit        23           22           21           20               19      18        17           16


  Access
   Reset


     Bit        15           14           13           12               11      10         9           8
                                                            TID[15:8]
  Access       R/W          R/W           R/W         R/W               R/W     R/W       R/W         R/W
   Reset        0             0            0           0                 0       0         0           0


     Bit        7             6            5           4                 3       2         1           0
                                                            TID[7:0]
  Access       R/W          R/W           R/W         R/W               R/W     R/W       R/W         R/W
   Reset        0             0            0           0                 0       0         0           0


           Bit 31 – ENIDn Enable Copying of TID Matched Frames
           Value      Description
           0          TID n is not part of the comparison match.
           1          TID n is processed for the comparison match.

           Bits 15:0 – TID[15:0] Type ID Match n
           For use in comparisons with received frames type ID/length frames.




       © 2019 Microchip Technology Inc.                       Datasheet                    DS60001507E-page 560
                                                          SAM D5x/E5x Family Data Sheet
                                                                                 GMAC - Ethernet MAC

24.9.25 GMAC Wake on LAN Register

           Name:       WOL
           Offset:     0x0B8
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29         28              27    26        25           24


  Access
   Reset


     Bit        23           22           21         20              19    18        17           16
                                                                     MTI   SA1       ARP         MAG
  Access                                                             R/W   R/W       R/W         R/W
   Reset                                                              0     0         0           0


     Bit        15           14           13         12              11    10         9           8
                                                          IP[15:8]
  Access       R/W          R/W           R/W       R/W              R/W   R/W       R/W         R/W
   Reset        0             0            0          0               0     0         0           0


     Bit        7             6            5          4               3     2         1           0
                                                          IP[7:0]
  Access       R/W          R/W           R/W       R/W              R/W   R/W       R/W         R/W
   Reset        0             0            0          0               0     0         0           0


           Bit 19 – MTI Multicast Hash Event Enable
           Value      Description
           0          Wake on LAN multicast hash Event disabled
           1          Wake on LAN multicast hash Event enabled

           Bit 18 – SA1 Specific Address Register 1 Event Enable
           Value      Description
           0          Wake on Specific Address Register 1 Event disabled
           1          Wake on Specific Address Register 1 Event enabled

           Bit 17 – ARP ARP Request Event Enable
           Value      Description
           0          Wake on LAN ARP request Event disabled
           1          Wake on LAN ARP request Event enabled

           Bit 16 – MAG Magic Packet Event Enable
           Value      Description
           0          Wake on LAN magic packet Event disabled
           1          Wake on LAN magic packet Event enabled




       © 2019 Microchip Technology Inc.                    Datasheet                  DS60001507E-page 561
                                                 SAM D5x/E5x Family Data Sheet
                                                                              GMAC - Ethernet MAC

Bits 15:0 – IP[15:0] ARP Request IP Address
Wake on LAN ARP request IP address. Written to define the 16 least significant bits of the target IP
address that is matched to generate a Wake on LAN event.
 Value      Description
 0x0000 No Event generated, even if matched by the received frame.
 0x0001- Wake on LAN Event generated for matching LSB of the target IP address.
 0xFFFF




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 562
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.26 GMAC IPG Stretch Register

           Name:       IPGS
           Offset:     0x0BC
           Reset:      0x00000000
           Property:   -


     Bit        31           30            29           28              27         26           25            24


  Access
   Reset


     Bit        23           22            21           20              19         18           17            16


  Access
   Reset


     Bit        15           14            13           12              11         10            9            8
                                                             FL[15:8]
  Access       R/W           R/W          R/W          R/W              R/W       R/W          R/W           R/W
   Reset         0            0            0             0               0         0             0            0


     Bit         7            6            5             4               3         2             1            0
                                                             FL[7:0]
  Access       R/W           R/W          R/W          R/W              R/W       R/W          R/W           R/W
   Reset         0            0            0             0               0         0             0            0


           Bits 15:0 – FL[15:0] Frame Length
           Bits FL[7:0] are multiplied with the previously transmitted frame length (including preamble), and divided
                                                                                FL[7:0]
           by FL[15:8]+1 (adding 1 to prevent division by zero). RESULT =
                                                                              F[15+8]+1
           If RESULT > 96 and the IP Stretch Enable bit in the Network Configuration Register (NCFGR.IPGSEN) is
           written to '1', RESULT is used for the transmit inter-packet-gap.




       © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 563
                                                          SAM D5x/E5x Family Data Sheet
                                                                                   GMAC - Ethernet MAC

24.9.27 GMAC Stacked VLAN Register

           Name:       SVLAN
           Offset:     0x0C0
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29         28           27         26           25          24
             ESVLAN
  Access
   Reset        0


     Bit        23           22           21         20           19         18           17          16


  Access
   Reset


     Bit        15           14           13         12           11         10           9           8
                                                     VLAN_TYPE[15:8]
  Access       R/W          R/W           R/W       R/W          R/W         R/W         R/W         R/W
   Reset        0             0            0         0            0           0           0           0


     Bit        7             6            5         4            3           2           1           0
                                                     VLAN_TYPE[7:0]
  Access       R/W          R/W           R/W       R/W          R/W         R/W         R/W         R/W
   Reset        0             0            0         0            0           0           0           0


           Bit 31 – ESVLAN Enable Stacked VLAN Processing Mode
           0: Disable the stacked VLAN processing mode
           1: Enable the stacked VLAN processing mode
            Value       Description
            0           Stacked VLAN Processing disabled
            1           Stacked VLAN Processing enabled

           Bits 15:0 – VLAN_TYPE[15:0] User Defined VLAN_TYPE Field
           When Stacked VLAN is enabled (ESVLAN=1), the first VLAN tag in a received frame will only be
           accepted if the VLAN type field is equal to this user defined VLAN_TYPE, OR equal to the standard
           VLAN type (0x8100).
           Note: The second VLAN tag of a Stacked VLAN packet will only be matched correctly if its VLAN_TYPE
           field equals 0x8100.




       © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 564
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.28 GMAC Specific Address 1 Mask Bottom

           Name:       SAMB1
           Offset:     0x0C8
           Reset:      0x00000000
           Property:   -


     Bit        31            30           29            28                 27      26           25             24
                                                              ADDR[31:24]
  Access       R/W           R/W          R/W           R/W                R/W     R/W          R/W             R/W
   Reset         0            0             0            0                  0       0             0              0


     Bit        23            22           21            20                 19      18           17             16
                                                              ADDR[23:16]
  Access       R/W           R/W          R/W           R/W                R/W     R/W          R/W             R/W
   Reset         0            0             0            0                  0       0             0              0


     Bit        15            14           13            12                 11      10            9              8
                                                              ADDR[15:8]
  Access       R/W           R/W          R/W           R/W                R/W     R/W          R/W             R/W
   Reset         0            0             0            0                  0       0             0              0


     Bit         7            6             5            4                  3       2             1              0
                                                               ADDR[7:0]
  Access       R/W           R/W          R/W           R/W                R/W     R/W          R/W             R/W
   Reset         0            0             0            0                  0       0             0              0


           Bits 31:0 – ADDR[31:0] Specific Address 1 Mask
           Setting a bit to '1' masks the corresponding bit in the Specific Address 1 Bottom register (SAB1).




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 565
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.29 GMAC Specific Address Mask 1 Top

           Name:        SAMT1
           Offset:      0x0CC
           Reset:       0x00000000
           Property:    -


     Bit        31            30           29            28                27       26            25           24


  Access
   Reset


     Bit        23            22           21            20                19       18            17           16


  Access
   Reset


     Bit        15            14           13            12                11       10            9            8
                                                              ADDR[15:8]
  Access       R/W           R/W           R/W          R/W                R/W     R/W           R/W          R/W
   Reset         0            0             0             0                 0        0            0            0


     Bit         7            6             5             4                 3        2            1            0
                                                              ADDR[7:0]
  Access       R/W           R/W           R/W          R/W                R/W     R/W           R/W          R/W
   Reset         0            0             0             0                 0        0            0            0


           Bits 15:0 – ADDR[15:0] Specific Address 1 Mask
           Setting a bit to '1' masks the corresponding bit in the Specific Address 1 register SAT1.




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 566
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.30 GMAC 1588 Timer Nanosecond Comparison Register

           Name:       NSC
           Offset:     0x0DC
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29            28           27           26           25           24


  Access
   Reset


     Bit        23           22           21            20           19           18           17           16
                                                                            NANOSEC[20:16]
  Access                                               R/W          R/W          R/W          R/W           R/W
   Reset                                                0            0             0            0            0


     Bit        15           14           13            12           11           10            9            8
                                                         NANOSEC[15:8]
  Access       R/W           R/W          R/W          R/W          R/W          R/W          R/W           R/W
   Reset         0            0            0            0            0             0            0            0


     Bit         7            6            5            4            3             2            1            0
                                                         NANOSEC[7:0]
  Access       R/W           R/W          R/W          R/W          R/W          R/W          R/W           R/W
   Reset         0            0            0            0            0             0            0            0


           Bits 20:0 – NANOSEC[20:0] 1588 Timer Nanosecond Comparison Value
           Value is compared to the bits [45:24] of the TSU timer count value (upper 21 bits of nanosecond value).




       © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 567
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.31 GMAC 1588 Timer Second Comparison Low Register

           Name:       SCL
           Offset:     0x0E0
           Reset:      0x00000000
           Property:   -


     Bit        31           30           29           28                 27      26          25           24
                                                             SEC[31:24]
  Access       R/W          R/W           R/W          R/W                R/W    R/W          R/W         R/W
   Reset         0            0            0            0                  0      0            0           0


     Bit        23           22           21           20                 19      18          17           16
                                                             SEC[23:16]
  Access       R/W          R/W           R/W          R/W                R/W    R/W          R/W         R/W
   Reset         0            0            0            0                  0      0            0           0


     Bit        15           14           13           12                 11      10           9           8
                                                             SEC[15:8]
  Access       R/W          R/W           R/W          R/W                R/W    R/W          R/W         R/W
   Reset         0            0            0            0                  0      0            0           0


     Bit         7            6            5            4                  3      2            1           0
                                                              SEC[7:0]
  Access       R/W          R/W           R/W          R/W                R/W    R/W          R/W         R/W
   Reset         0            0            0            0                  0      0            0           0


           Bits 31:0 – SEC[31:0] 1588 Timer Second Comparison Value
           Value is compared to seconds value bits [31:0] of the TSU timer count value.




       © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 568
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.32 GMAC 1588 Timer Second Comparison High Register

           Name:       SCH
           Offset:     0x0E4
           Reset:      0x00000000
           Property:   -


     Bit        31            30           29            28               27       26            25           24


  Access
   Reset


     Bit        23            22           21            20               19       18            17           16


  Access
   Reset


     Bit        15            14           13            12               11       10            9             8
                                                              SEC[15:8]
  Access       R/W           R/W          R/W           R/W               R/W      R/W          R/W           R/W
   Reset         0            0             0            0                 0        0            0             0


     Bit         7            6             5            4                 3        2            1             0
                                                              SEC[7:0]
  Access       R/W           R/W          R/W           R/W               R/W      R/W          R/W           R/W
   Reset         0            0             0            0                 0        0            0             0


           Bits 15:0 – SEC[15:0] 1588 Timer Second Comparison Value
           Value is compared to the top 16 bits (most significant 16 bits [47:32] of seconds value) of the TSU timer
           count value.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 569
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.33 GMAC PTP Event Frame Transmitted Seconds High Register

           Name:       EFTSH
           Offset:     0x0E8
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29           28               27        26           25            24


  Access
   Reset


     Bit        23            22           21           20               19        18           17            16


  Access
   Reset


     Bit        15            14           13           12               11        10            9            8
                                                             RUD[15:8]
  Access         R            R            R             R               R         R             R            R
   Reset         0            0            0             0               0          0            0            0


     Bit         7            6            5             4               3          2            1            0
                                                             RUD[7:0]
  Access         R            R            R             R               R         R             R            R
   Reset         0            0            0             0               0          0            0            0


           Bits 15:0 – RUD[15:0] Register Update
           The register is updated with the value that the IEEE 1588 timer seconds register held when the SFD of a
           PTP transmit primary event crosses the MII interface. An interrupt is issued when the register is updated.




       © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 570
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.34 GMAC PTP Event Frame Received Seconds High Register

           Name:       EFRSH
           Offset:     0x0EC
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29           28               27        26           25            24


  Access
   Reset


     Bit        23            22           21           20               19        18           17            16


  Access
   Reset


     Bit        15            14           13           12               11        10            9            8
                                                             RUD[15:8]
  Access         R            R            R             R               R         R             R            R
   Reset         0            0            0             0               0          0            0            0


     Bit         7            6            5             4               3          2            1            0
                                                             RUD[7:0]
  Access         R            R            R             R               R         R             R            R
   Reset         0            0            0             0               0          0            0            0


           Bits 15:0 – RUD[15:0] Register Update
           The register is updated with the value that the IEEE 1588 timer seconds register held when the SFD of a
           PTP transmit primary event crosses the MII interface. An interrupt is issued when the register is updated.




       © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 571
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.35 GMAC PTP Peer Event Frame Transmitted Seconds High Register

           Name:       PEFTSH
           Offset:     0x0F0
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28               27       26           25           24


  Access
   Reset


     Bit        23           22           21           20               19       18           17           16


  Access
   Reset


     Bit        15           14           13           12               11       10            9            8
                                                            RUD[15:8]
  Access        R             R           R             R               R         R            R            R
   Reset         0            0            0            0               0         0            0            0


     Bit         7            6            5            4               3         2            1            0
                                                            RUD[7:0]
  Access        R             R           R             R               R         R            R            R
   Reset         0            0            0            0               0         0            0            0


           Bits 15:0 – RUD[15:0] Register Update
           The register is updated with the value that the IEEE 1588 timer seconds register held when the SFD of a
           PTP transmit peer event crosses the MII interface. An interrupt is issued when the register is updated.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 572
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.36 GMAC PTP Peer Event Frame Received Seconds High Register

           Name:       PEFRSH
           Offset:     0x0F4
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28               27       26           25           24


  Access
   Reset


     Bit        23           22           21           20               19       18           17           16


  Access
   Reset


     Bit        15           14           13           12               11       10            9            8
                                                            RUD[15:8]
  Access        R             R           R            R                R        R            R            R
   Reset         0            0            0            0               0         0            0            0


     Bit         7            6            5            4               3         2            1            0
                                                            RUD[7:0]
  Access        R             R           R            R                R        R            R            R
   Reset         0            0            0            0               0         0            0            0


           Bits 15:0 – RUD[15:0] Register Update
           The register is updated with the value that the 1588 timer seconds register held when the SFD of a PTP
           transmit peer event crosses the MII interface. An interrupt is issued when the register is updated.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 573
                                                                SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

24.9.37 GMAC Octets Transmitted Low Register

           Name:        OTLO
           Offset:      0x100
           Reset:       0x00000000
           Property:    Read-Only

           When reading the Octets Transmitted and Octets Received Registers, bits [31:0] should be read prior to
           bits [47:32] to ensure reliable operation.

     Bit        31            30            29            28                27        26            25            24
                                                               TXO[31:24]
  Access         R             R             R             R                R         R             R             R
   Reset         0             0             0             0                0          0             0            0


     Bit        23            22            21            20                19        18            17            16
                                                               TXO[23:16]
  Access         R             R             R             R                R         R             R             R
   Reset         0             0             0             0                0          0             0            0


     Bit        15            14            13            12                11        10             9            8
                                                               TXO[15:8]
  Access         R             R             R             R                R         R             R             R
   Reset         0             0             0             0                0          0             0            0


     Bit         7             6             5             4                3          2             1            0
                                                                TXO[7:0]
  Access         R             R             R             R                R         R             R             R
   Reset         0             0             0             0                0          0             0            0


           Bits 31:0 – TXO[31:0] Transmitted Octets
           Transmitted octets in valid frames of any type without errors, bits [31:0]. This counter is 48-bits, and is
           read through two registers. This count does not include octets from automatically generated pause
           frames.




       © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 574
                                                               SAM D5x/E5x Family Data Sheet
                                                                                            GMAC - Ethernet MAC

24.9.38 GMAC Octets Transmitted High Register

           Name:        OTHI
           Offset:      0x104
           Reset:       0x00000000
           Property:    Read-Only

           When reading the Octets Transmitted and Octets Received Registers, bits [31:0] should be read prior to
           bits [47:32] to ensure reliable operation.

     Bit        31            30            29            28               27         26            25            24


  Access
   Reset


     Bit        23            22            21            20               19         18            17            16


  Access
   Reset


     Bit        15            14            13            12               11         10            9             8
                                                               TXO[15:8]
  Access         R             R             R            R                R          R             R             R
   Reset         0             0             0             0               0          0             0             0


     Bit         7             6             5             4               3          2             1             0
                                                               TXO[7:0]
  Access         R             R             R            R                R          R             R             R
   Reset         0             0             0             0               0          0             0             0


           Bits 15:0 – TXO[15:0] Transmitted Octets
           Transmitted octets in valid frames of any type without errors, bits [47:32]. This counter is 48-bits, and is
           read through two registers. This count does not include octets from automatically generated pause
           frames.




       © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 575
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.39 GMAC Frames Transmitted

           Name:       FT
           Offset:     0x108
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29            28                27      26            25           24
                                                              FTX[31:24]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


     Bit        23            22           21            20                19      18            17           16
                                                              FTX[23:16]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


     Bit        15            14           13            12                11      10            9             8
                                                              FTX[15:8]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


     Bit         7            6             5            4                 3        2            1             0
                                                               FTX[7:0]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


           Bits 31:0 – FTX[31:0] Frames Transmitted without Error
           Frames transmitted without error. This register counts the number of frames successfully transmitted, i.e.,
           no underrun and not too many retries. Excludes pause frames.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 576
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.40 GMAC Broadcast Frames Transmitted Register

           Name:       BCFT
           Offset:     0x10C
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29            28                 27      26           25           24
                                                              BFTX[31:24]
  Access         R            R            R             R                  R       R            R                R
   Reset         0            0             0            0                  0       0            0                0


     Bit        23            22           21            20                 19      18           17           16
                                                              BFTX[23:16]
  Access         R            R            R             R                  R       R            R                R
   Reset         0            0             0            0                  0       0            0                0


     Bit        15            14           13            12                 11      10           9                8
                                                              BFTX[15:8]
  Access         R            R            R             R                  R       R            R                R
   Reset         0            0             0            0                  0       0            0                0


     Bit         7            6             5            4                  3       2            1                0
                                                               BFTX[7:0]
  Access         R            R            R             R                  R       R            R                R
   Reset         0            0             0            0                  0       0            0                0


           Bits 31:0 – BFTX[31:0] Broadcast Frames Transmitted without Error
           This register counts the number of broadcast frames successfully transmitted without error, i.e., no
           underrun and not too many retries. Excludes pause frames.




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 577
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

24.9.41 GMAC Multicast Frames Transmitted Register

           Name:        MFT
           Offset:      0x110
           Reset:       0x00000000
           Property:    Read-Only


     Bit        31            30           29            28                 27      26            25              24
                                                              MFTX[31:24]
  Access         R            R             R            R                  R        R            R               R
   Reset         0            0             0             0                 0        0            0               0


     Bit        23            22           21            20                 19      18            17              16
                                                              MFTX[23:16]
  Access         R            R             R            R                  R        R            R               R
   Reset         0            0             0             0                 0        0            0               0


     Bit        15            14           13            12                 11      10            9               8
                                                              MFTX[15:8]
  Access         R            R             R            R                  R        R            R               R
   Reset         0            0             0             0                 0        0            0               0


     Bit         7            6             5             4                 3        2            1               0
                                                               MFTX[7:0]
  Access         R            R             R            R                  R        R            R               R
   Reset         0            0             0             0                 0        0            0               0


           Bits 31:0 – MFTX[31:0] Multicast Frames Transmitted without Error
           This register counts the number of multicast frames successfully transmitted without error, i.e., no
           underrun and not too many retries. Excludes pause frames.




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 578
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.42 GMAC Pause Frames Transmitted Register

           Name:       PFT
           Offset:     0x114
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28                27      26           25           24


  Access
   Reset


     Bit        23           22           21           20                19      18           17           16


  Access
   Reset


     Bit        15           14           13           12                11      10            9            8
                                                            PFTX[15:8]
  Access        R             R            R            R                R        R            R            R
   Reset         0            0            0            0                0        0            0            0


     Bit         7            6            5            4                3        2            1            0
                                                            PFTX[7:0]
  Access        R             R            R            R                R        R            R            R
   Reset         0            0            0            0                0        0            0            0


           Bits 15:0 – PFTX[15:0] Pause Frames Transmitted Register
           This register counts the number of pause frames transmitted. Only pause frames triggered by the register
           interface or through the external pause pins are counted as pause frames. Pause frames received
           through the FIFO interface are counted in the frames transmitted counter.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 579
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.43 GMAC 64 Byte Frames Transmitted Register

           Name:       BFT64
           Offset:     0x118
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29           28                 27      26            25           24
                                                             NFTX[31:24]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


     Bit        23            22           21           20                 19      18            17           16
                                                             NFTX[23:16]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


     Bit        15            14           13           12                 11      10            9             8
                                                             NFTX[15:8]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


     Bit         7            6             5            4                 3        2            1             0
                                                              NFTX[7:0]
  Access         R            R            R             R                 R        R            R             R
   Reset         0            0             0            0                 0        0            0             0


           Bits 31:0 – NFTX[31:0] 64 Byte Frames Transmitted without Error
           This register counts the number of 64 byte frames successfully transmitted without error, i.e., no underrun
           and not too many retries. Excludes pause frames.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 580
                                                                SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

24.9.44 GMAC 65 to 127 Byte Frames Transmitted Register

            Name:       TBFT127
            Offset:     0x11C
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31            30           29            28                 27      26           25            24
                                                               NFTX[31:24]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


      Bit        23            22           21            20                 19      18           17            16
                                                               NFTX[23:16]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


      Bit        15            14           13            12                 11      10            9            8
                                                               NFTX[15:8]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


      Bit         7            6             5            4                  3       2             1            0
                                                                NFTX[7:0]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


            Bits 31:0 – NFTX[31:0] 65 to 127 Byte Frames Transmitted without Error
            This register counts the number of 65 to 127 byte frames successfully transmitted without error, i.e., no
            underrun and not too many retries. Excludes pause frames.




        © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 581
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.45 GMAC 128 to 255 Byte Frames Transmitted Register

           Name:       TBFT255
           Offset:     0x120
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31            30           29            28                 27      26           25            24
                                                              NFTX[31:24]
  Access         R            R             R            R                  R       R             R            R
   Reset         0            0             0            0                  0       0             0            0


     Bit        23            22           21            20                 19      18           17            16
                                                              NFTX[23:16]
  Access         R            R             R            R                  R       R             R            R
   Reset         0            0             0            0                  0       0             0            0


     Bit        15            14           13            12                 11      10            9            8
                                                              NFTX[15:8]
  Access         R            R             R            R                  R       R             R            R
   Reset         0            0             0            0                  0       0             0            0


     Bit         7            6             5            4                  3       2             1            0
                                                               NFTX[7:0]
  Access         R            R             R            R                  R       R             R            R
   Reset         0            0             0            0                  0       0             0            0


           Bits 31:0 – NFTX[31:0] 128 to 255 Byte Frames Transmitted without Error
           This register counts the number of 128 to 255 byte frames successfully transmitted without error, i.e., no
           underrun and not too many retries.




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 582
                                                                SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

24.9.46 GMAC 256 to 511 Byte Frames Transmitted Register

            Name:       TBFT511
            Offset:     0x124
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31            30           29            28                 27      26           25            24
                                                               NFTX[31:24]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


      Bit        23            22           21            20                 19      18           17            16
                                                               NFTX[23:16]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


      Bit        15            14           13            12                 11      10            9            8
                                                               NFTX[15:8]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


      Bit         7            6             5            4                  3       2             1            0
                                                                NFTX[7:0]
  Access          R            R             R            R                  R       R             R            R
   Reset          0            0             0            0                  0       0             0            0


            Bits 31:0 – NFTX[31:0] 256 to 511 Byte Frames Transmitted without Error
            This register counts the number of 256 to 511 byte frames successfully transmitted without error, i.e., no
            underrun and not too many retries.




        © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 583
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.47 GMAC 512 to 1023 Byte Frames Transmitted Register

           Name:       TBFT1023
           Offset:     0x128
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31            30           29            28                 27     26            25           24
                                                              NFTX[31:24]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


     Bit        23            22           21            20                 19     18            17           16
                                                              NFTX[23:16]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


     Bit        15            14           13            12                 11     10            9             8
                                                              NFTX[15:8]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


     Bit         7            6             5            4                  3       2            1             0
                                                               NFTX[7:0]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


           Bits 31:0 – NFTX[31:0] 512 to 1023 Byte Frames Transmitted without Error
           This register counts the number of 512 to 1023 byte frames successfully transmitted without error, i.e., no
           underrun and not too many retries.




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 584
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.48 GMAC 1024 to 1518 Byte Frames Transmitted Register

           Name:       TBFT1518
           Offset:     0x12C
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31            30           29            28                 27     26            25           24
                                                              NFTX[31:24]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


     Bit        23            22           21            20                 19     18            17           16
                                                              NFTX[23:16]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


     Bit        15            14           13            12                 11     10            9             8
                                                              NFTX[15:8]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


     Bit         7            6             5            4                  3       2            1             0
                                                               NFTX[7:0]
  Access         R            R            R             R                  R       R            R             R
   Reset         0            0             0            0                  0       0            0             0


           Bits 31:0 – NFTX[31:0] 1024 to 1518 Byte Frames Transmitted without Error
           This register counts the number of 1024 to 1518 byte frames successfully transmitted without error, i.e.,
           no underrun and not too many retries.




       © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 585
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.49 GMAC Greater Than 1518 Byte Frames Transmitted Register

           Name:       GTBFT1518
           Offset:     0x130
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29           28                 27      26           25            24
                                                             NFTX[31:24]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


     Bit        23            22           21           20                 19      18           17            16
                                                             NFTX[23:16]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


     Bit        15            14           13           12                 11      10            9            8
                                                             NFTX[15:8]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


     Bit         7            6            5             4                 3       2             1            0
                                                              NFTX[7:0]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


           Bits 31:0 – NFTX[31:0] Greater than 1518 Byte Frames Transmitted without Error
           This register counts the number of 1518 or above byte frames successfully transmitted without error i.e.,
           no underrun and not too many retries.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 586
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           GMAC - Ethernet MAC

24.9.50 GMAC Transmit Underruns Register

           Name:        TUR
           Offset:      0x134
           Reset:       0x00000000
           Property:    Read-Only


     Bit        31            30            29           28                27        26           25                24


  Access
   Reset


     Bit        23            22            21           20                19        18           17                16


  Access
   Reset


     Bit        15            14            13           12                11        10            9                8
                                                                                                       TXUNR[9:8]
  Access                                                                                           R                R
   Reset                                                                                           0                0


     Bit         7            6             5             4                3         2             1                0
                                                              TXUNR[7:0]
  Access         R            R             R             R                R         R             R                R
   Reset         0            0             0             0                0         0             0                0


           Bits 9:0 – TXUNR[9:0] Transmit Underruns
           This register counts the number of frames not transmitted due to a transmit underrun. If this register is
           incremented then no other statistics register is incremented.




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 587
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.51 GMAC Single Collision Frames Register

            Name:       SCF
            Offset:     0x138
            Reset:      0x00000000
            Property:   -


      Bit        31           30            29           28                27       26           25                 24


  Access
   Reset


      Bit        23           22            21           20                19       18           17                 16
                                                                                                      SCOL[17:16]
  Access                                                                                         R                  R
   Reset                                                                                         0                  0


      Bit        15           14            13           12                11       10           9                  8
                                                              SCOL[15:8]
  Access         R             R            R            R                 R        R            R                  R
   Reset          0            0            0             0                0        0            0                  0


      Bit         7            6            5             4                3        2            1                  0
                                                              SCOL[7:0]
  Access         R             R            R            R                 R        R            R                  R
   Reset          0            0            0             0                0        0            0                  0


            Bits 17:0 – SCOL[17:0] Single Collision
            This register counts the number of frames experiencing a single collision before being successfully
            transmitted i.e., no underrun.




        © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 588
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.52 GMAC Multiple Collision Frames Register

            Name:       MCF
            Offset:     0x13C
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31           30            29           28                27       26           25                 24


  Access
   Reset


      Bit        23           22            21           20                19       18           17                 16
                                                                                                      MCOL[17:16]
  Access                                                                                         R                  R
   Reset                                                                                         0                  0


      Bit        15           14            13           12                11       10           9                  8
                                                              MCOL[15:8]
  Access         R             R            R            R                 R        R            R                  R
   Reset          0            0            0            0                 0        0            0                  0


      Bit         7            6            5            4                 3        2            1                  0
                                                              MCOL[7:0]
  Access         R             R            R            R                 R        R            R                  R
   Reset          0            0            0            0                 0        0            0                  0


            Bits 17:0 – MCOL[17:0] Multiple Collision
            This register counts the number of frames experiencing between two and fifteen collisions prior to being
            successfully transmitted, i.e., no underrun and not too many retries.




        © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 589
                                                            SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.53 GMAC Excessive Collisions Register

           Name:       EC
           Offset:     0x140
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29           28               27        26           25               24


  Access
   Reset


     Bit        23           22           21           20               19        18           17               16


  Access
   Reset


     Bit        15           14           13           12               11        10           9                8
                                                                                                    XCOL[9:8]
  Access                                                                                       R                R
   Reset                                                                                       0                0


     Bit         7            6            5            4               3         2            1                0
                                                            XCOL[7:0]
  Access        R             R            R            R               R         R            R                R
   Reset         0            0            0            0               0         0            0                0


           Bits 9:0 – XCOL[9:0] Excessive Collisions
           This register counts the number of frames that failed to be transmitted because they experienced 16
           collisions.




       © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 590
                                                                SAM D5x/E5x Family Data Sheet
                                                                                             GMAC - Ethernet MAC

24.9.54 GMAC Late Collisions Register

            Name:        LC
            Offset:      0x144
            Reset:       0x00000000
            Property:    Read-Only


      Bit        31            30            29            28               27         26            25               24


  Access
   Reset


      Bit        23            22            21            20               19         18            17               16


  Access
   Reset


      Bit        15            14            13            12               11         10            9                8
                                                                                                          LCOL[9:8]
  Access                                                                                             R                R
   Reset                                                                                             0                0


      Bit         7             6             5             4               3          2             1                0
                                                                LCOL[7:0]
  Access          R             R             R            R                R          R             R                R
   Reset          0             0             0             0               0          0             0                0


            Bits 9:0 – LCOL[9:0] Late Collisions
            This register counts the number of late collisions occurring after the slot time (512 bits) has expired. In
            10/100 mode, late collisions are counted twice i.e., both as a collision and a late collision.




        © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 591
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.55 GMAC Deferred Transmission Frames Register

           Name:       DTF
           Offset:     0x148
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30            29           28                27       26           25                 24


  Access
   Reset


     Bit        23           22            21           20                19       18           17                 16
                                                                                                     DEFT[17:16]
  Access                                                                                        R                  R
   Reset                                                                                         0                 0


     Bit        15           14            13           12                11       10            9                 8
                                                             DEFT[15:8]
  Access         R            R            R            R                 R        R            R                  R
   Reset         0            0            0             0                0        0             0                 0


     Bit         7            6            5             4                3        2             1                 0
                                                             DEFT[7:0]
  Access         R            R            R            R                 R        R            R                  R
   Reset         0            0            0             0                0        0             0                 0


           Bits 17:0 – DEFT[17:0] Deferred Transmission
           This register counts the number of frames experiencing deferral due to carrier sense being active on their
           first attempt at transmission. Frames involved in any collision are not counted nor are frames that
           experienced a transmit underrun.




       © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 592
                                                                SAM D5x/E5x Family Data Sheet
                                                                                              GMAC - Ethernet MAC

24.9.56 GMAC Carrier Sense Errors Register

            Name:        CSE
            Offset:      0x14C
            Reset:       0x00000000
            Property:    Read-only


      Bit        31            30            29            28              27          26            25              24


  Access
   Reset


      Bit        23            22            21            20              19          18            17              16


  Access
   Reset


      Bit        15            14            13            12              11          10             9              8
                                                                                                          CSR[9:8]
  Access                                                                                              R              R
   Reset                                                                                              0              0


      Bit         7             6             5             4              3            2             1              0
                                                                CSR[7:0]
  Access          R             R             R             R              R            R             R              R
   Reset          0             0             0             0              0            0             0              0


            Bits 9:0 – CSR[9:0] Carrier Sense Error
            This register counts the number of frames transmitted with carrier sense was not seen during
            transmission or where carrier sense was de-asserted after being asserted in a transmit frame without
            collision (no underrun). Only incremented in half duplex mode. The only effect of a carrier sense error is
            to increment this register. The behavior of the other statistics registers is unaffected by the detection of a
            carrier sense error.




        © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 593
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.57 GMAC Octets Received Low Register

           Name:       ORLO
           Offset:     0x150
           Reset:      0x00000000
           Property:   Read-Only

           When reading the Octets Transmitted and Octets Received Registers, bits [31:0] should be read prior to
           bits [47:32] to ensure reliable operation.

     Bit        31            30           29           28                27       26           25            24
                                                             RXO[31:24]
  Access         R            R            R             R                R        R             R            R
   Reset         0            0            0             0                0        0             0            0


     Bit        23            22           21           20                19       18           17            16
                                                             RXO[23:16]
  Access         R            R            R             R                R        R             R            R
   Reset         0            0            0             0                0        0             0            0


     Bit        15            14           13           12                11       10            9            8
                                                             RXO[15:8]
  Access         R            R            R             R                R        R             R            R
   Reset         0            0            0             0                0        0             0            0


     Bit         7            6            5             4                3        2             1            0
                                                              RXO[7:0]
  Access         R            R            R             R                R        R             R            R
   Reset         0            0            0             0                0        0             0            0


           Bits 31:0 – RXO[31:0] Received Octets
           Received octets in frame without errors [31:0]. The number of octets received in valid frames of any type.
           This counter is 48-bits and is read through two registers. This count does not include octets from pause
           frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 594
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.58 GMAC Octets Received High Register

           Name:       ORHI
           Offset:     0x154
           Reset:      0x00000000
           Property:   Read-only

           When reading the Octets Transmitted and Octets Received Registers, bits 31:0 should be read prior to
           bits 47:32 to ensure reliable operation.

     Bit        31            30           29            28               27        26           25            24


  Access
   Reset


     Bit        23            22           21            20               19        18           17            16


  Access
   Reset


     Bit        15            14           13            12               11        10            9            8
                                                              RXO[15:8]
  Access         R            R             R            R                R         R             R            R
   Reset         0            0             0            0                0         0             0            0


     Bit         7            6             5            4                3         2             1            0
                                                              RXO[7:0]
  Access         R            R             R            R                R         R             R            R
   Reset         0            0             0            0                0         0             0            0


           Bits 15:0 – RXO[15:0] Received Octets
           Received octets in frame without errors [47:32]. The number of octets received in valid frames of any
           type. This counter is 48-bits and is read through two registers. This count does not include octets from
           pause frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 595
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.59 GMAC Frames Received Register

           Name:       FR
           Offset:     0x158
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29            28                27       26           25           24
                                                              FRX[31:24]
  Access         R            R            R             R                 R        R            R                R
   Reset         0            0             0            0                 0        0            0                0


     Bit        23            22           21            20                19       18           17           16
                                                              FRX[23:16]
  Access         R            R            R             R                 R        R            R                R
   Reset         0            0             0            0                 0        0            0                0


     Bit        15            14           13            12                11       10           9                8
                                                              FRX[15:8]
  Access         R            R            R             R                 R        R            R                R
   Reset         0            0             0            0                 0        0            0                0


     Bit         7            6             5            4                 3        2            1                0
                                                               FRX[7:0]
  Access         R            R            R             R                 R        R            R                R
   Reset         0            0             0            0                 0        0            0                0


           Bits 31:0 – FRX[31:0] Frames Received without Error
           This bit field counts the number of frames successfully received, excluding pause frames. It is only
           incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 596
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.60 GMAC Broadcast Frames Received Register

           Name:       BCFR
           Offset:     0x15C
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30            29           28                 27     26           25            24
                                                             BFRX[31:24]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit        23           22            21           20                 19     18           17            16
                                                             BFRX[23:16]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit        15           14            13           12                 11     10            9            8
                                                             BFRX[15:8]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit         7            6            5            4                  3       2            1            0
                                                              BFRX[7:0]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


           Bits 31:0 – BFRX[31:0] Broadcast Frames Received without Error
           Broadcast frames received without error. This bit field counts the number of broadcast frames
           successfully received. This excludes pause frames, and is only incremented if the frame is successfully
           filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 597
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.61 GMAC Multicast Frames Received Register

           Name:       MFR
           Offset:     0x160
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30            29           28                 27     26           25            24
                                                             MFRX[31:24]
  Access        R             R            R            R                  R      R             R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit        23           22            21           20                 19     18           17            16
                                                             MFRX[23:16]
  Access        R             R            R            R                  R      R             R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit        15           14            13           12                 11     10            9            8
                                                             MFRX[15:8]
  Access        R             R            R            R                  R      R             R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit         7            6            5            4                  3       2            1            0
                                                              MFRX[7:0]
  Access        R             R            R            R                  R      R             R            R
   Reset         0            0            0            0                  0       0            0            0


           Bits 31:0 – MFRX[31:0] Multicast Frames Received without Error
           This register counts the number of multicast frames successfully received without error, excluding pause
           frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 598
                                                             SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.62 GMAC Pause Frames Received Register

           Name:       PFR
           Offset:     0x164
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28                27          26       25           24


  Access
   Reset


     Bit        23           22           21           20                19          18       17           16


  Access
   Reset


     Bit        15           14           13           12                11          10        9           8
                                                            PFRX[15:8]
  Access        R             R            R            R                R           R        R            R
   Reset         0            0            0            0                0           0         0           0


     Bit         7            6            5            4                3           2         1           0
                                                            PFRX[7:0]
  Access        R             R            R            R                R           R        R            R
   Reset         0            0            0            0                0           0         0           0


           Bits 15:0 – PFRX[15:0] Pause Frames Received Register
           This register counts the number of pause frames received without error.




       © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 599
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.63 GMAC 64 Byte Frames Received Register

           Name:       BFR64
           Offset:     0x168
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30            29           28                 27     26            25           24
                                                             NFRX[31:24]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit        23           22            21           20                 19     18            17           16
                                                             NFRX[23:16]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit        15           14            13           12                 11     10            9            8
                                                             NFRX[15:8]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


     Bit         7            6            5            4                  3       2            1            0
                                                              NFRX[7:0]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0            0


           Bits 31:0 – NFRX[31:0] 64 Byte Frames Received without Error
           This bit field counts the number of 64 byte frames successfully received without error. Excludes pause
           frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 600
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.64 GMAC 65 to 127 Byte Frames Received Register

           Name:       TBFR127
           Offset:     0x16C
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31            30           29           28                 27      26           25            24
                                                             NFRX[31:24]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


     Bit        23            22           21           20                 19      18           17            16
                                                             NFRX[23:16]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


     Bit        15            14           13           12                 11      10            9            8
                                                             NFRX[15:8]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


     Bit         7            6            5             4                 3       2             1            0
                                                              NFRX[7:0]
  Access         R            R            R             R                 R       R             R            R
   Reset         0            0            0             0                 0       0             0            0


           Bits 31:0 – NFRX[31:0] 65 to 127 Byte Frames Received without Error
           This bit field counts the number of 65 to 127 byte frames successfully received without error. Excludes
           pause frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 601
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.65 GMAC 128 to 255 Byte Frames Received Register

           Name:       TBFR255
           Offset:     0x170
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30            29           28                 27      26           25           24
                                                             NFRX[31:24]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


     Bit        23           22            21           20                 19      18           17           16
                                                             NFRX[23:16]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


     Bit        15           14            13           12                 11      10            9            8
                                                             NFRX[15:8]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


     Bit         7            6            5             4                 3       2             1            0
                                                              NFRX[7:0]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


           Bits 31:0 – NFRX[31:0] 128 to 255 Byte Frames Received without Error
           This bit field counts the number of 128 to 255 byte frames successfully received without error. Excludes
           pause frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 602
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.66 GMAC 256 to 511 Byte Frames Received Register

           Name:       TBFR511
           Offset:     0x174
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30            29           28                 27      26           25           24
                                                             NFRX[31:24]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


     Bit        23           22            21           20                 19      18           17           16
                                                             NFRX[23:16]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


     Bit        15           14            13           12                 11      10            9            8
                                                             NFRX[15:8]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


     Bit         7            6            5             4                 3       2             1            0
                                                              NFRX[7:0]
  Access         R            R            R            R                  R       R            R             R
   Reset         0            0            0             0                 0       0             0            0


           Bits 31:0 – NFRX[31:0] 256 to 511 Byte Frames Received without Error
           This bit fields counts the number of 256 to 511 byte frames successfully received without error. Excludes
           pause frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 603
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.67 GMAC 512 to 1023 Byte Frames Received Register

           Name:       TBFR1023
           Offset:     0x178
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30            29           28                 27      26           25           24
                                                             NFRX[31:24]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


     Bit        23           22            21           20                 19      18           17           16
                                                             NFRX[23:16]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


     Bit        15           14            13           12                 11      10           9             8
                                                             NFRX[15:8]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


     Bit         7            6            5            4                  3       2            1             0
                                                              NFRX[7:0]
  Access        R             R            R            R                  R       R            R            R
   Reset         0            0            0            0                  0       0            0             0


           Bits 31:0 – NFRX[31:0] 512 to 1023 Byte Frames Received without Error
           This bit field counts the number of 512 to 1023 byte frames successfully received without error. Excludes
           pause frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 604
                                                               SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.68 GMAC 1024 to 1518 Byte Frames Received Register

           Name:        TBFR1518
           Offset:      0x17C
           Reset:       0x00000000
           Property:    Read-Only


     Bit        31            30           29            28                 27      26            25           24
                                                              NFRX[31:24]
  Access         R            R             R            R                  R       R             R            R
   Reset         0            0             0            0                  0        0            0             0


     Bit        23            22           21            20                 19      18            17           16
                                                              NFRX[23:16]
  Access         R            R             R            R                  R       R             R             R
   Reset         0            0             0            0                  0        0            0             0


     Bit        15            14           13            12                 11      10            9             8
                                                              NFRX[15:8]
  Access         R            R             R            R                  R       R             R             R
   Reset         0            0             0            0                  0        0            0             0


     Bit         7            6             5            4                  3        2            1             0
                                                               NFRX[7:0]
  Access         R            R             R            R                  R       R             R             R
   Reset         0            0             0            0                  0        0            0             0


           Bits 31:0 – NFRX[31:0] 1024 to 1518 Byte Frames Received without Error
           This bit field counts the number of 1024 to 1518 byte frames successfully received without error, i.e., no
           underrun and not too many retries.




       © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 605
                                                           SAM D5x/E5x Family Data Sheet
                                                                                   GMAC - Ethernet MAC

24.9.69 GMAC 1519 to Maximum Byte Frames Received Register

           Name:       TMXBFR
           Offset:     0x180
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29         28                 27   26           25          24
                                                          NFRX[31:24]
  Access        R             R           R          R                  R     R           R           R
   Reset        0             0           0          0                  0     0           0           0


     Bit        23           22           21         20                 19   18           17          16
                                                          NFRX[23:16]
  Access        R             R           R          R                  R     R           R           R
   Reset        0             0           0          0                  0     0           0           0


     Bit        15           14           13         12                 11   10           9           8
                                                          NFRX[15:8]
  Access        R             R           R          R                  R     R           R           R
   Reset        0             0           0          0                  0     0           0           0


     Bit        7             6           5          4                  3     2           1           0
                                                           NFRX[7:0]
  Access        R             R           R          R                  R     R           R           R
   Reset        0             0           0          0                  0     0           0           0


           Bits 31:0 – NFRX[31:0] 1519 to Maximum Byte Frames Received without Error
           This bit field counts the number of 1519 Byte or above frames successfully received without error.
           Maximum frame size is determined by the Maximum Frame Size bit (MAXFS, 1536 Bytes) or Jumbo
           Frame Size bit (JFRAME, 10240 Bytes) in the Network Configuration Register (NCFGR). Excludes pause
           frames, and is only incremented if the frame is successfully filtered and copied to memory.




       © 2019 Microchip Technology Inc.                      Datasheet                    DS60001507E-page 606
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.70 GMAC Undersized Frames Received Register

           Name:       UFR
           Offset:     0x184
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31            30           29           28               27        26            25               24


  Access
   Reset


     Bit        23            22           21           20               19        18            17               16


  Access
   Reset


     Bit        15            14           13           12               11        10            9                8
                                                                                                      UFRX[9:8]
  Access                                                                                         R                R
   Reset                                                                                         0                0


     Bit         7            6             5            4               3          2            1                0
                                                             UFRX[7:0]
  Access         R            R            R             R               R          R            R                R
   Reset         0            0             0            0               0          0            0                0


           Bits 9:0 – UFRX[9:0] Undersize Frames Received
           This bit field counts the number of frames received less than 64 bytes in length (10/100 mode, full duplex)
           that do not have either a CRC error or an alignment error.




       © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 607
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.71 GMAC Oversized Frames Received Register

           Name:       OFR
           Offset:     0x188
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28               27       26            25               24


  Access
   Reset


     Bit        23           22           21           20               19       18            17               16


  Access
   Reset


     Bit        15           14           13           12               11       10            9                8
                                                                                                    OFRX[9:8]
  Access                                                                                       R                R
   Reset                                                                                       0                0


     Bit         7            6            5            4               3         2            1                0
                                                            OFRX[7:0]
  Access        R             R            R            R               R         R            R                R
   Reset         0            0            0            0               0         0            0                0


           Bits 9:0 – OFRX[9:0] Oversized Frames Received
           This pit field counts the number of frames received exceeding 1518 Bytes in length (1536 Bytes if
           NCFGR.MAXFS is written to '1') but do not have either a CRC error, an alignment error, nor a receive
           symbol error.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 608
                                                           SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.72 GMAC Jabbers Received Register

           Name:       JR
           Offset:     0x18C
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29          28              27        26           25              24


  Access
   Reset


     Bit        23           22           21          20              19        18           17              16


  Access
   Reset


     Bit        15           14           13          12              11        10            9              8
                                                                                                  JRX[9:8]
  Access                                                                                     R               R
   Reset                                                                                      0              0


     Bit        7             6           5            4              3          2            1              0
                                                           JRX[7:0]
  Access        R             R           R            R              R          R           R               R
   Reset        0             0           0            0              0          0            0              0


           Bits 9:0 – JRX[9:0] Jabbers Received
           This bit field counts the number of frames received exceeding 1518 Bytes in length (1536 Bytes if
           NCFGR.MAXFS is written to '1') and have either a CRC error, an alignment error or a receive symbol
           error.




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 609
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.73 GMAC Frame Check Sequence Errors Register

           Name:       FCSE
           Offset:     0x190
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29           28               27        26           25               24


  Access
   Reset


     Bit        23            22           21           20               19        18           17               16


  Access
   Reset


     Bit        15            14           13           12               11        10            9               8
                                                                                                     FCKR[9:8]
  Access                                                                                         R               R
   Reset                                                                                         0               0


     Bit         7            6            5             4               3         2             1               0
                                                             FCKR[7:0]
  Access         R            R            R             R               R         R             R               R
   Reset         0            0            0             0               0         0             0               0


           Bits 9:0 – FCKR[9:0] Frame Check Sequence Errors
           The register counts frames that are an integral number of bytes, have bad CRC and are between 64 and
           1518 bytes in length (1536 Bytes if NCFGR.MAXFS is written to '1'). This register is also incremented if a
           symbol error is detected and the frame is of valid length and has an integral number of bytes.
           This register is incremented for a frame with bad FCS, regardless of whether it is copied to memory due
           to ignore FCS mode (enabled by writing NCFGR.IRXFCS=1).




       © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 610
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          GMAC - Ethernet MAC

24.9.74 GMAC Length Field Frame Errors Register

           Name:       LFFE
           Offset:     0x194
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31            30           29            28               27        26           25               24


  Access
   Reset


     Bit        23            22           21            20               19        18           17               16


  Access
   Reset


     Bit        15            14           13            12               11        10            9               8
                                                                                                      LFER[9:8]
  Access                                                                                          R               R
   Reset                                                                                          0               0


     Bit         7            6             5            4                3         2             1               0
                                                              LFER[7:0]
  Access         R            R             R            R                R         R             R               R
   Reset         0            0             0            0                0         0             0               0


           Bits 9:0 – LFER[9:0] Length Field Frame Errors
           This bit field counts the number of frames received that have a measured length shorter than that
           extracted from the length field (Bytes 13 and 14). This condition is only counted if the value of the length
           field is less than 0x0600, the frame is not of excessive length and checking is enabled by writing a '1' to
           the Length Field Error Frame Discard bit in the Network Configuration Register (GMAC_NCFGR.LFERD).




       © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 611
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.75 GMAC Receive Symbol Errors Register

           Name:       RSE
           Offset:     0x198
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29           28               27       26           25               24


  Access
   Reset


     Bit        23           22           21           20               19       18           17               16


  Access
   Reset


     Bit        15           14           13           12               11       10           9                8
                                                                                                   RXSE[9:8]
  Access                                                                                      R                R
   Reset                                                                                      0                0


     Bit        7             6           5            4                3        2            1                0
                                                            RXSE[7:0]
  Access        R             R           R            R                R        R            R                R
   Reset        0             0           0            0                0        0            0                0


           Bits 9:0 – RXSE[9:0] Receive Symbol Errors
           This bit field counts the number of frames that had GRXER asserted during reception. For 10/100 mode
           symbol errors are counted regardless of frame length checks. Receive symbol errors will also be counted
           as an FCS or alignment error if the frame is between 64 and 1518 Bytes (1536 Bytes if
           NCFGR.MAXFS=1). If the frame is larger it will be recorded as a jabber error.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 612
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.76 GMAC Alignment Errors Register

           Name:       AE
           Offset:     0x19C
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29           28              27       26           25              24


  Access
   Reset


     Bit        23           22           21           20              19       18           17              16


  Access
   Reset


     Bit        15           14           13           12              11       10            9              8
                                                                                                  AER[9:8]
  Access                                                                                     R               R
   Reset                                                                                      0              0


     Bit        7             6           5            4               3         2            1              0
                                                            AER[7:0]
  Access        R             R           R            R               R         R           R               R
   Reset        0             0           0            0               0         0            0              0


           Bits 9:0 – AER[9:0] Alignment Errors
           This bit field counts the frames that are not an integral number of bytes long and have bad CRC when
           their length is truncated to an integral number of Bytes and are between 64 and 1518 Bytes in length
           (1536 if NCFGR.MAXFS=1). This register is also incremented if a symbol error is detected and the frame
           is of valid length and does not have an integral number of bytes.




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 613
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.77 GMAC Receive Resource Errors Register

           Name:       RRE
           Offset:     0x1A0
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28                 27      26           25             24


  Access
   Reset


     Bit        23           22           21           20                 19      18           17             16
                                                                                                   RXRER[17:16]
  Access                                                                                       R                  R
   Reset                                                                                       0                  0


     Bit        15           14           13           12                 11      10           9                  8
                                                            RXRER[15:8]
  Access        R             R            R            R                 R       R            R                  R
   Reset         0            0            0            0                 0       0            0                  0


     Bit         7            6            5            4                 3       2            1                  0
                                                            RXRER[7:0]
  Access        R             R            R            R                 R       R            R                  R
   Reset         0            0            0            0                 0       0            0                  0


           Bits 17:0 – RXRER[17:0] Receive Resource Errors
           This bit field counts frames that are not an integral number of bytes long and have bad CRC when their
           length is truncated to an integral number of Bytes and are between 64 and 1518 Bytes in length (1536 if
           NCFGR.MAXFS=1). This bit field is also incremented if a symbol error is detected and the frame is of
           valid length and does not have an integral number of Bytes.




       © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 614
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.78 GMAC Receive Overruns Register

           Name:       ROE
           Offset:     0x1A4
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28                27      26           25                24


  Access
   Reset


     Bit        23           22           21           20                19      18           17                16


  Access
   Reset


     Bit        15           14           13           12                11      10           9                 8
                                                                                                   RXOVR[9:8]
  Access                                                                                      R                 R
   Reset                                                                                      0                 0


     Bit        7             6           5            4                 3       2            1                 0
                                                            RXOVR[7:0]
  Access        R             R           R            R                 R       R            R                 R
   Reset        0             0           0            0                 0       0            0                 0


           Bits 9:0 – RXOVR[9:0] Receive Overruns
           This bit field counts the number of frames that are address recognized but were not copied to memory
           due to a receive overrun.




       © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 615
                                                           SAM D5x/E5x Family Data Sheet
                                                                                    GMAC - Ethernet MAC

24.9.79 GMAC IP Header Checksum Errors Register

           Name:       IHCE
           Offset:     0x1A8
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29         28                27      26          25           24


  Access
   Reset


     Bit        23           22           21         20                19      18          17           16


  Access
   Reset


     Bit        15           14           13         12                11      10           9           8


  Access
   Reset


     Bit        7             6           5           4                3       2            1           0
                                                          HCKER[7:0]
  Access        R             R           R           R                R       R           R            R
   Reset        0             0           0           0                0       0            0           0


           Bits 7:0 – HCKER[7:0] IP Header Checksum Errors
           This register counts the number of frames discarded due to an incorrect IP header checksum, but are
           between 64 and 1518 Bytes (1536 Bytes if GMAC_NCFGR.MAXFS=1) and do not have a CRC error, an
           alignment error, nor a symbol error.




       © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 616
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     GMAC - Ethernet MAC

24.9.80 GMAC TCP Checksum Errors Register

           Name:       TCE
           Offset:     0x1AC
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29          28                27     26           25           24


  Access
   Reset


     Bit        23           22           21          20                19     18           17           16


  Access
   Reset


     Bit        15           14           13          12                11     10            9           8


  Access
   Reset


     Bit        7             6           5           4                 3       2            1           0
                                                           TCKER[7:0]
  Access        R             R           R           R                 R       R           R            R
   Reset        0             0           0           0                 0       0            0           0


           Bits 7:0 – TCKER[7:0] TCP Checksum Errors
           This register counts the number of frames discarded due to an incorrect TCP checksum, but are between
           64 and 1518 Bytes (1536 Bytes if NCFGR.MAXFS=1) and do not have a CRC error, an alignment error,
           nor a symbol error.




       © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 617
                                                            SAM D5x/E5x Family Data Sheet
                                                                                     GMAC - Ethernet MAC

24.9.81 GMAC UDP Checksum Errors Register

           Name:       UCE
           Offset:     0x1B0
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29          28                27     26           25           24


  Access
   Reset


     Bit        23           22           21          20                19     18           17           16


  Access
   Reset


     Bit        15           14           13          12                11     10           9            8


  Access
   Reset


     Bit        7             6           5           4                 3       2           1            0
                                                           UCKER[7:0]
  Access        R             R           R           R                 R       R           R            R
   Reset        0             0           0           0                 0       0           0            0


           Bits 7:0 – UCKER[7:0] UDP Checksum Errors
           This register counts the number of frames discarded due to an incorrect UDP checksum, but are between
           64 and 1518 Bytes (1536 Bytes if NCFGR.MAXFS=1) and do not have a CRC error, an alignment error,
           nor a symbol error.




       © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 618
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.82 GMAC 1588 Timer Increment Sub-nanoseconds Register

           Name:       TISUBN
           Offset:     0x1BC
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31            30           29           28                  27     26            25           24


  Access
   Reset


     Bit        23            22           21           20                  19     18            17           16


  Access
   Reset


     Bit        15            14           13           12                  11     10            9            8
                                                             LSBTIR[15:8]
  Access       R/W           R/W          R/W           R/W             R/W       R/W           R/W          R/W
   Reset         0            0            0             0                  0       0            0            0


     Bit         7            6            5             4                  3       2            1            0
                                                             LSBTIR[7:0]
  Access       R/W           R/W          R/W           R/W             R/W       R/W           R/W          R/W
   Reset         0            0            0             0                  0       0            0            0


           Bits 15:0 – LSBTIR[15:0] Lower Significant Bits of Timer Increment Register
           Lower significant bits of Timer Increment Register [15:0], giving a 24-bit timer_increment counter. These
           bits are the sub-ns value which the 1588 timer will be incremented each clock cycle. Bit n = 2(n-16) ns
           giving a resolution of approximately 15.2E-15 sec.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 619
                                                            SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.83 GMAC 1588 Timer Seconds High Register

           Name:       TSH
           Offset:     0x1C0
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31           30           29           28               27       26           25           24


  Access
   Reset


     Bit        23           22           21           20               19       18           17           16


  Access
   Reset


     Bit        15           14           13           12               11       10           9            8
                                                            TCS[15:8]
  Access       R/W          R/W           R/W         R/W               R/W     R/W          R/W          R/W
   Reset        0             0            0           0                 0       0            0            0


     Bit        7             6            5           4                 3       2            1            0
                                                            TCS[7:0]
  Access       R/W          R/W           R/W         R/W               R/W     R/W          R/W          R/W
   Reset        0             0            0           0                 0       0            0            0


           Bits 15:0 – TCS[15:0] Timer Count in Seconds
           This register is writable. It increments by 1 when the IEEE 1588 nanoseconds counter counts to one
           second. It may also be incremented when the Timer Adjust Register is written.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 620
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.84 GMAC 1588 Timer Seconds Low Register

           Name:       TSL
           Offset:     0x1D0
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31           30           29           28                27      26           25           24
                                                            TCS[31:24]
  Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset        0             0            0           0                  0      0            0            0


     Bit        23           22           21           20                19      18           17           16
                                                            TCS[23:16]
  Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset        0             0            0           0                  0      0            0            0


     Bit        15           14           13           12                11      10           9            8
                                                            TCS[15:8]
  Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset        0             0            0           0                  0      0            0            0


     Bit        7             6            5           4                  3      2            1            0
                                                             TCS[7:0]
  Access       R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset        0             0            0           0                  0      0            0            0


           Bits 31:0 – TCS[31:0] Timer Count in Seconds
           This register is writable. It increments by 1 when the IEEE 1588 nanoseconds counter counts to one
           second. It may also be incremented when the Timer Adjust Register is written.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 621
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.85 1588 Timer Sync Strobe Seconds [31:0] Register

            Name:       TSSSL
            Offset:     0x1C8
            Reset:      0x00000000
            Property:   Read/Write


      Bit        31           30           29           28                27      26           25           24
                                                             VTS[31:24]
  Access        R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset         0             0            0           0                  0      0            0            0


      Bit        23           22           21           20                19      18           17           16
                                                             VTS[23:16]
  Access        R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset         0             0            0           0                  0      0            0            0


      Bit        15           14           13           12                11      10           9            8
                                                             VTS[15:8]
  Access        R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset         0             0            0           0                  0      0            0            0


      Bit        7             6            5           4                  3      2            1            0
                                                              VTS[7:0]
  Access        R/W          R/W           R/W         R/W                R/W    R/W          R/W          R/W
   Reset         0             0            0           0                  0      0            0            0


            Bits 31:0 – VTS[31:0] Value of Timer Seconds Register Capture
            This register is writable. It increments by 1 when the IEEE 1588 nanoseconds counter counts to one
            second. It may also be incremented when the Timer Adjust Register is written.




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 622
                                                             SAM D5x/E5x Family Data Sheet
                                                                                                  GMAC - Ethernet MAC

24.9.86 GMAC 1588 Timer Sync Strobe Nanoseconds Register

           Name:       TSSN
           Offset:     0x1CC
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31           30           29           28                27                 26        25           24
                                                                               VTN[29:24]
  Access                                  R/W         R/W                R/W                R/W       R/W         R/W
   Reset                                   0           0                  0                  0         0           0


     Bit        23           22           21           20                19                 18        17           16
                                                            VTN[23:16]
  Access       R/W          R/W           R/W         R/W                R/W                R/W       R/W         R/W
   Reset        0             0            0           0                  0                  0         0           0


     Bit        15           14           13           12                11                 10         9           8
                                                            VTN[15:8]
  Access       R/W          R/W           R/W         R/W                R/W                R/W       R/W         R/W
   Reset        0             0            0           0                  0                  0         0           0


     Bit        7             6            5           4                  3                  2         1           0
                                                             VTN[7:0]
  Access       R/W          R/W           R/W         R/W                R/W                R/W       R/W         R/W
   Reset        0             0            0           0                  0                  0         0           0


           Bits 29:0 – VTN[29:0] Value Timer Nanoseconds Register Capture
           This register is writable. It increments by 1 when the IEEE 1588 nanoseconds counter counts to one
           second. It may also be incremented when the Timer Adjust Register is written.




       © 2019 Microchip Technology Inc.                       Datasheet                                DS60001507E-page 623
                                                                SAM D5x/E5x Family Data Sheet
                                                                                                     GMAC - Ethernet MAC

24.9.87 GMAC 1588 Timer Nanoseconds Register

           Name:        TN
           Offset:      0x1D4
           Reset:       0x00000000
           Property:    Read/Write


     Bit        31            30            29            28                27                 26        25           24
                                                                                  TNS[29:24]
  Access                                   R/W           R/W                R/W                R/W       R/W         R/W
   Reset                                    0             0                  0                  0         0           0


     Bit        23            22            21            20                19                 18        17           16
                                                               TNS[23:16]
  Access        R/W          R/W           R/W           R/W                R/W                R/W       R/W         R/W
   Reset         0             0            0             0                  0                  0         0           0


     Bit        15            14            13            12                11                 10         9           8
                                                               TNS[15:8]
  Access        R/W          R/W           R/W           R/W                R/W                R/W       R/W         R/W
   Reset         0             0            0             0                  0                  0         0           0


     Bit         7             6            5             4                  3                  2         1           0
                                                                TNS[7:0]
  Access        R/W          R/W           R/W           R/W                R/W                R/W       R/W         R/W
   Reset         0             0            0             0                  0                  0         0           0


           Bits 29:0 – TNS[29:0] Timer Count in Nanoseconds
           This register is writable. It can also be adjusted by writes to the IEEE 1588 Timer Adjust Register. It
           increments by the value of the IEEE 1588 Timer Increment Register each clock cycle.




       © 2019 Microchip Technology Inc.                          Datasheet                                DS60001507E-page 624
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                       GMAC - Ethernet MAC

24.9.88 GMAC 1588 Timer Adjust Register

           Name:        TA
           Offset:      0x1D8
           Reset:       0x00000000
           Property:    Write-Only


     Bit         31            30            29             28                 27                 26       25           24
                ADJ                                                                 ITDT[29:24]
  Access         W                           W              W                  W                  W        W            W
   Reset         0                            0             0                  0                  0         0           0


     Bit         23            22            21             20                 19                 18       17           16
                                                                 ITDT[23:16]
  Access         W             W             W              W                  W                  W        W            W
   Reset         0             0              0             0                  0                  0         0           0


     Bit         15            14            13             12                 11                 10        9           8
                                                                 ITDT[15:8]
  Access         W             W             W              W                  W                  W        W            W
   Reset         0             0              0             0                  0                  0         0           0


     Bit         7             6              5             4                  3                  2         1           0
                                                                  ITDT[7:0]
  Access         W             W             W              W                  W                  W        W            W
   Reset         0             0              0             0                  0                  0         0           0


           Bit 31 – ADJ Adjust 1588 Timer
           Write as '1' to subtract from the 1588 timer. Write as '0' to add to it.

           Bits 29:0 – ITDT[29:0] Increment/Decrement
           The number of nanoseconds to increment or decrement the IEEE 1588 Timer Nanoseconds Register. If
           necessary, the IEEE 1588 Seconds Register will be incremented or decremented.




       © 2019 Microchip Technology Inc.                             Datasheet                               DS60001507E-page 625
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         GMAC - Ethernet MAC

24.9.89 GMAC IEEE 1588 Timer Increment Register

           Name:       TI
           Offset:     0x1DC
           Reset:      0x00000000
           Property:   Read/Write


     Bit        31           30           29           28                27      26          25           24


  Access
   Reset


     Bit        23           22           21           20                19      18          17           16
                                                              NIT[7:0]
  Access       R/W          R/W           R/W          R/W               R/W     R/W         R/W         R/W
   Reset         0            0            0            0                 0          0        0           0


     Bit        15           14           13           12                11      10           9           8
                                                             ACNS[7:0]
  Access       R/W          R/W           R/W          R/W               R/W     R/W         R/W         R/W
   Reset         0            0            0            0                 0          0        0           0


     Bit         7            6            5            4                 3          2        1           0
                                                             CNS[7:0]
  Access       R/W          R/W           R/W          R/W               R/W     R/W         R/W         R/W
   Reset         0            0            0            0                 0          0        0           0


           Bits 23:16 – NIT[7:0] Number of Increments
           The number of increments after which the alternative increment is used.

           Bits 15:8 – ACNS[7:0] Alternative Count Nanoseconds
           Alternative count of nanoseconds by which the 1588 Timer Nanoseconds Register will be incremented
           each clock cycle.

           Bits 7:0 – CNS[7:0] Count Nanoseconds
           A count of nanoseconds by which the IEEE 1588 Timer Nanoseconds Register will be incremented each
           clock cycle.




       © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 626
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.90 GMAC PTP Event Frame Transmitted Seconds Low Register

           Name:       EFTSL
           Offset:     0x1E0
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29          28                27      26           25           24
                                                           RUD[31:24]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        23           22           21          20                19      18           17           16
                                                           RUD[23:16]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        15           14           13          12                11      10           9            8
                                                           RUD[15:8]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        7             6           5            4                3       2            1            0
                                                            RUD[7:0]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


           Bits 31:0 – RUD[31:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Seconds Register holds when the SFD of
           a PTP transmit primary event crosses the MII interface. An interrupt is issued when the register is
           updated.




       © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 627
                                                               SAM D5x/E5x Family Data Sheet
                                                                                                  GMAC - Ethernet MAC

24.9.91 GMAC PTP Event Frame Transmitted Nanoseconds Register

           Name:       EFTN
           Offset:     0x1E4
           Reset:      0x00000000
           Property:   Read-only


     Bit        31            30           29            28                27                26       25           24
                                                                                RUD[29:24]
  Access                                    R            R                 R                 R        R            R
   Reset                                    0            0                 0                 0         0           0


     Bit        23            22           21            20                19                18       17           16
                                                              RUD[23:16]
  Access         R            R             R            R                 R                 R        R            R
   Reset         0            0             0            0                 0                 0         0           0


     Bit        15            14           13            12                11                10        9           8
                                                              RUD[15:8]
  Access         R            R             R            R                 R                 R        R            R
   Reset         0            0             0            0                 0                 0         0           0


     Bit         7            6             5            4                 3                 2         1           0
                                                               RUD[7:0]
  Access         R            R             R            R                 R                 R        R            R
   Reset         0            0             0            0                 0                 0         0           0


           Bits 29:0 – RUD[29:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Nanoseconds Register holds when the
           SFD of a PTP transmit primary event crosses the MII interface. An interrupt is issued when the bit field is
           updated.




       © 2019 Microchip Technology Inc.                          Datasheet                             DS60001507E-page 628
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.92 GMAC PTP Event Frame Received Seconds Low Register

           Name:       EFRSL
           Offset:     0x1E8
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30           29          28                27      26           25           24
                                                           RUD[31:24]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        23           22           21          20                19      18           17           16
                                                           RUD[23:16]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        15           14           13          12                11      10           9            8
                                                           RUD[15:8]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        7             6           5            4                3       2            1            0
                                                            RUD[7:0]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


           Bits 31:0 – RUD[31:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Seconds Register holds when the SFD of
           a PTP receive primary event crosses the MII interface. An interrupt is issued when the register is
           updated.




       © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 629
                                                              SAM D5x/E5x Family Data Sheet
                                                                                                 GMAC - Ethernet MAC

24.9.93 GMAC PTP Event Frame Received Nanoseconds Register

           Name:       EFRN
           Offset:     0x1EC
           Reset:      0x00000000
           Property:   Read-only


     Bit        31           30            29           28                27                26       25           24
                                                                               RUD[29:24]
  Access                                   R             R                R                 R        R            R
   Reset                                   0             0                0                 0         0           0


     Bit        23           22            21           20                19                18       17           16
                                                             RUD[23:16]
  Access         R            R            R             R                R                 R        R            R
   Reset         0            0            0             0                0                 0         0           0


     Bit        15           14            13           12                11                10        9           8
                                                             RUD[15:8]
  Access         R            R            R             R                R                 R        R            R
   Reset         0            0            0             0                0                 0         0           0


     Bit         7            6            5             4                3                 2         1           0
                                                              RUD[7:0]
  Access         R            R            R             R                R                 R        R            R
   Reset         0            0            0             0                0                 0         0           0


           Bits 29:0 – RUD[29:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Nanoseconds Register holds when the
           SFD of a PTP receive primary event crosses the MII interface. An interrupt is issued when the register is
           updated.




       © 2019 Microchip Technology Inc.                         Datasheet                             DS60001507E-page 630
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.94 GMAC PTP Peer Event Frame Transmitted Seconds Low Register

           Name:       PEFTSL
           Offset:     0x1F0
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29            28                27      26           25           24
                                                             RUD[31:24]
  Access        R             R            R            R                 R       R            R            R
   Reset         0            0            0            0                 0       0            0             0


     Bit        23           22           21            20                19      18           17           16
                                                             RUD[23:16]
  Access        R             R            R            R                 R       R            R            R
   Reset         0            0            0            0                 0       0            0             0


     Bit        15           14           13            12                11      10           9             8
                                                             RUD[15:8]
  Access        R             R            R            R                 R       R            R            R
   Reset         0            0            0            0                 0       0            0             0


     Bit         7            6            5            4                 3       2            1             0
                                                              RUD[7:0]
  Access        R             R            R            R                 R       R            R            R
   Reset         0            0            0            0                 0       0            0             0


           Bits 31:0 – RUD[31:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Seconds Register holds when the SFD of
           a PTP transmit peer event crosses the MII interface. An interrupt is issued when the register is updated.




       © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 631
                                                              SAM D5x/E5x Family Data Sheet
                                                                                                 GMAC - Ethernet MAC

24.9.95 GMAC PTP Peer Event Frame Transmitted Nanoseconds Register

           Name:       PEFTN
           Offset:     0x1F4
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30            29           28                27                26       25           24
                                                                               RUD[29:24]
  Access                                   R            R                 R                 R        R            R
   Reset                                   0            0                 0                 0         0           0


     Bit        23           22            21           20                19                18       17           16
                                                             RUD[23:16]
  Access        R             R            R            R                 R                 R        R            R
   Reset         0            0            0            0                 0                 0         0           0


     Bit        15           14            13           12                11                10        9           8
                                                             RUD[15:8]
  Access        R             R            R            R                 R                 R        R            R
   Reset         0            0            0            0                 0                 0         0           0


     Bit         7            6            5            4                 3                 2         1           0
                                                              RUD[7:0]
  Access        R             R            R            R                 R                 R        R            R
   Reset         0            0            0            0                 0                 0         0           0


           Bits 29:0 – RUD[29:0] Register Update
           The register is updated with the value that the 1588 Timer Nanoseconds Register holds when the SFD of
           a PTP transmit peer event crosses the MII interface. An interrupt is issued when the register is updated.




       © 2019 Microchip Technology Inc.                         Datasheet                             DS60001507E-page 632
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      GMAC - Ethernet MAC

24.9.96 GMAC PTP Peer Event Frame Received Seconds Low Register

           Name:       PEFRSL
           Offset:     0x1F8
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29          28                27      26           25           24
                                                           RUD[31:24]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        23           22           21          20                19      18           17           16
                                                           RUD[23:16]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        15           14           13          12                11      10           9            8
                                                           RUD[15:8]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


     Bit        7             6           5            4                3       2            1            0
                                                            RUD[7:0]
  Access        R             R           R            R                R       R            R            R
   Reset        0             0           0            0                0       0            0            0


           Bits 31:0 – RUD[31:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Seconds Register holds when the SFD of
           a PTP receive primary event crosses the MII interface. An interrupt is issued when the register is
           updated.




       © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 633
                                                              SAM D5x/E5x Family Data Sheet
                                                                                                 GMAC - Ethernet MAC

24.9.97 GMAC PTP Peer Event Frame Received Nanoseconds Register

           Name:       PEFRN
           Offset:     0x1FC
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30            29           28                27                26       25           24
                                                                               RUD[29:24]
  Access                                   R             R                R                 R        R            R
   Reset                                   0             0                0                 0         0           0


     Bit        23           22            21           20                19                18       17           16
                                                             RUD[23:16]
  Access         R            R            R             R                R                 R        R            R
   Reset         0            0            0             0                0                 0         0           0


     Bit        15           14            13           12                11                10        9           8
                                                             RUD[15:8]
  Access         R            R            R             R                R                 R        R            R
   Reset         0            0            0             0                0                 0         0           0


     Bit         7            6            5             4                3                 2         1           0
                                                              RUD[7:0]
  Access         R            R            R             R                R                 R        R            R
   Reset         0            0            0             0                0                 0         0           0


           Bits 29:0 – RUD[29:0] Register Update
           The register is updated with the value that the IEEE 1588 Timer Nanoseconds Register holds when the
           SFD of a PTP receive primary event crosses the MII interface. An interrupt is issued when the register is
           updated.




       © 2019 Microchip Technology Inc.                         Datasheet                             DS60001507E-page 634
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                              GMAC - Ethernet MAC

24.9.98 Received LPI Transitions

            Name:        RLPITR
            Offset:      0x270
            Reset:       0x00000000
            Property:    Read-Only


      Bit        31            30             29            28                  27      26            25            24


  Access
   Reset


      Bit        23            22             21            20                  19      18            17            16


  Access
   Reset


      Bit        15            14             13            12                  11      10            9             8
                                                                 RLPITR[15:8]
  Access          R             R             R             R                   R       R             R             R
   Reset          0             0             0             0                   0       0             0             0


      Bit         7             6             5             4                   3       2             1             0
                                                                 RLPITR[7:0]
  Access          R             R             R             R                   R       R             R             R
   Reset          0             0             0             0                   0       0             0             0


            Bits 15:0 – RLPITR[15:0] Received LPI Transitions
            The value of this bit field is a counter of transitions from receiving normal idle to receiving low power idle.
            Cleared on read.




        © 2019 Microchip Technology Inc.                            Datasheet                          DS60001507E-page 635
                                                              SAM D5x/E5x Family Data Sheet
                                                                                       GMAC - Ethernet MAC

24.9.99 Received LPI Time

           Name:       RLPITI
           Offset:     0x274
           Reset:      0x00000000
           Property:   Read-Only


     Bit        31           30           29           28                   27   26           25           24


  Access
   Reset


     Bit        23           22           21           20                   19   18           17           16
                                                            RLPITI[23:16]
  Access        R             R           R            R                    R     R            R            R
   Reset         0            0            0            0                   0     0            0            0


     Bit        15           14           13           12                   11   10            9            8
                                                            RLPITI[15:8]
  Access        R             R           R            R                    R     R            R            R
   Reset         0            0            0            0                   0     0            0            0


     Bit         7            6            5            4                   3     2            1            0
                                                             RLPITI[7:0]
  Access        R             R           R            R                    R     R            R            R
   Reset         0            0            0            0                   0     0            0            0


           Bits 23:0 – RLPITI[23:0] Received LPI Time
           The value of this bit field increments once every 16 AHB clock cycles when the Low Power Idle Enable bit
           in the Network Configuration Register (NCR.LPI) is written to '1'.
           Cleared on read.




       © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 636
                                                               SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.100 Transmit LPI Transitions

            Name:       TLPITR
            Offset:     0x278
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31           30           29           28                  27    26           25           24


   Access
    Reset


      Bit        23           22           21           20                  19    18           17           16


   Access
    Reset


      Bit        15           14           13           12                  11    10            9            8
                                                             TLPITR[15:8]
   Access        R             R           R            R                   R     R            R            R
    Reset         0            0            0            0                  0      0            0            0


      Bit         7            6            5            4                  3      2            1            0
                                                             TLPITR[7:0]
   Access        R             R           R            R                   R     R            R            R
    Reset         0            0            0            0                  0      0            0            0


            Bits 15:0 – TLPITR[15:0] Transmit LPI Transitions
            A count of the number of times the Low Power Idle Enable bit in the Network Configuration Register
            (NCR.LPI) goes from '0' to '1'.




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 637
                                                               SAM D5x/E5x Family Data Sheet
                                                                                        GMAC - Ethernet MAC

24.9.101 Transmit LPI Time

            Name:       TLPITI
            Offset:     0x27C
            Reset:      0x00000000
            Property:   Read-Only


      Bit        31           30           29           28                   27   26           25           24


  Access
   Reset


      Bit        23           22           21           20                   19   18           17           16
                                                             RLPITI[23:16]
  Access         R             R           R            R                    R     R            R            R
   Reset          0            0            0            0                   0     0            0            0


      Bit        15           14           13           12                   11   10            9            8
                                                             RLPITI[15:8]
  Access         R             R           R            R                    R     R            R            R
   Reset          0            0            0            0                   0     0            0            0


      Bit         7            6            5            4                   3     2            1            0
                                                              RLPITI[7:0]
  Access         R             R           R            R                    R     R            R            R
   Reset          0            0            0            0                   0     0            0            0


            Bits 23:0 – RLPITI[23:0] Transmit LPI Time
            The value of this bit field increments once every 16 AHB clock cycles when the Low Power Idle Enable bit
            in the Network Configuration Register (NCR.LPI) is written to '1'.
            Cleared on read.




        © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 638
