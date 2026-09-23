# 38. USB – Universal Serial Bus

*Source: `Atmel-SAMD51.pdf`, pages 1109-1203 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                                 USB – Universal Serial Bus


38.    USB – Universal Serial Bus

38.1   Overview
       The Universal Serial Bus interface (USB) module complies with the Universal Serial Bus (USB) 2.1
       specification supporting both device and embedded host modes.
       The USB device mode supports 8 endpoint addresses. All endpoint addresses have one input and one
       output endpoint, for a total of 16 endpoints. Each endpoint is fully configurable in any of the four transfer
       types: control, interrupt, bulk or isochronous. The USB host mode supports up to 8 pipes. The maximum
       data payload size is selectable up to 1023 bytes.
       Internal SRAM is used to keep the configuration and data buffer for each endpoint. The memory locations
       used for the endpoint configurations and data buffers is fully configurable. The amount of memory
       allocated is dynamic according to the number of endpoints in use, and the configuration of these. The
       USB module has a built-in Direct Memory Access (DMA) and will read/write data from/to the system RAM
       when a USB transaction takes place. No CPU or DMA Controller resources are required.
       To maximize throughput, an endpoint can be configured for ping-pong operation. When this is done the
       input and output endpoint with the same address are used in the same direction. The CPU or DMA
       Controller can then read/write one data buffer while the USB module writes/reads from the other buffer.
       This gives double buffered communication.
       Multi-packet transfer enables a data payload exceeding the maximum packet size of an endpoint to be
       transferred as multiple packets without any software intervention. This reduces the number of interrupts
       and software intervention needed for USB transfers.
       For low power operation the USB module can put the microcontroller in any sleep mode when the USB
       bus is idle and a suspend condition is given. Upon bus resume, the USB module can wake the
       microcontroller from any sleep mode.



38.2   Features
         • Compatible with the USB 2.1 specification
         • USB Embedded Host and Device mode
         • Supports full (12Mbit/s) and low (1.5Mbit/s) speed communication
         • Supports Link Power Management (LPM-L1) protocol
         • On-chip transceivers with built-in pull-ups and pull-downs
         • On-Chip USB serial resistors
         • 1kHz SOF clock available on external pin
         • Device mode
            – Supports 8 IN endpoints and 8 OUT endpoints
            – No endpoint size limitations
            – Built-in DMA with multi-packet and dual bank for all endpoints
            – Supports feedback endpoint
            – Supports crystal less clock
         • Host mode
            – Supports 8 physical pipes




       © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1109
                                                              SAM D5x/E5x Family Data Sheet
                                                                                        USB – Universal Serial Bus

              –   No pipe size limitations
              –   Supports multiplexed virtual pipe on one physical pipe to allow an unlimited USB tree
              –   Built-in DMA with multi-packet support and dual bank for all pipes
              –   Supports feedback endpoint
              –   Supports the USB 2.0 Phase-locked SOFs feature



38.3   USB Block Diagram
       Figure 38-1. LS/FS Implementation: USB Block Diagram

                                 USB

        SRAM Controller


             AHB Slave             dedicated bus      AHB Master



                                                        User
               APB               device-wide bus
                                                      Interface               USB 2.0                   DM
                                                                               Core                     DP
                                                             USB interrupts                             SOF 1kHz
                   NVIC



                                                             GCLK_USB
                   GCLK



                                                            System clock domain    USB clock domain




38.4   Signal Description
        Pin Name                Pin Description                                                  Type
        DM                      Data -: Differential Data Line - Port                            Input/Output
        DP                      Data +: Differential Data Line + Port                            Input/Output
        SOF 1kHZ                SOF Output                                                       Output

       Refer to I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One signal
       can be mapped on several pins.
       Related Links
       6. I/O Multiplexing and Considerations



38.5   Product Dependencies
       In order to use this peripheral module, other parts of the system must be configured correctly, as
       described below.




       © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 1110
                                                             SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.5.1   I/O Lines
         The USB pins may be multiplexed with the I/O lines Controller. The user must first configure the I/O
         Controller to assign the USB pins to their peripheral functions.
         A 1kHz SOF clock is available on an external pin. The user must first configure the I/O Controller to
         assign the 1kHz SOF clock to the peripheral function. The SOF clock is available for device and host
         mode.

38.5.2   Power Management
         This peripheral can continue to operate in any Sleep mode where its source clock is running. The
         interrupts can wake up the device from Sleep modes. Events connected to the event system can trigger
         other operations in the system without exiting Sleep modes.
         Related Links
         18. PM – Power Manager

38.5.3   Clocks
         The USB bus clock (CLK_USB_AHB) can be enabled and disabled in the Main Clock module, MCLK,
         and the default state of CLK_USB_AHB can be found in the Peripheral Clock Masking.
         A generic clock (GCLK_USB) is required to clock the USB. This clock must be configured and enabled in
         the Generic Clock Controller before using the USB.
         This generic clock is asynchronous to the bus clock (CLK_USB_AHB). Due to this asynchronicity, writes
         to certain registers will require synchronization between the clock domains.
         The USB module requires a GCLK_USB of 48 MHz ± 0.25% clock for low speed and full speed operation.
         To follow the USB data rate at 12 Mbit/s in full-speed mode, the CLK_USB_AHB clock should be at
         minimum 8 MHz.
         Clock recovery is achieved by a digital phase-locked loop in the USB module, which complies with the
         USB jitter specifications. If crystal-less operation is used in USB device mode, refer to USB Clock
         Recovery Module.
         Related Links
         14. GCLK - Generic Clock Controller
         14.6.6 Synchronization
         15.8.7 AHBMASK
         28.6.4.2 Additional Features

38.5.4   DMA
         The USB has a built-in Direct Memory Access (DMA) and will read/write data to/from the system RAM
         when a USB transaction takes place. No CPU or DMA Controller resources are required.

38.5.5   Interrupts
         The interrupt request line is connected to the Interrupt Controller. In order to use interrupt requests of this
         peripheral, the Interrupt Controller (NVIC) must be configured first. Refer to Nested Vector Interrupt
         Controller for details.
         Related Links
         10.2 Nested Vector Interrupt Controller




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1111
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.5.6    Events
          Not applicable.

38.5.7    Debug Operation
          When the CPU is halted in debug mode the USB peripheral continues normal operation. If the USB
          peripheral is configured in a way that requires it to be periodically serviced by the CPU through interrupts
          or similar, improper operation or data loss may result during debugging.

38.5.8    Register Access Protection
          Registers with write access can be optionally write-protected by the Peripheral Access Controller (PAC),
          except for the following:
           •   Device Interrupt Flag (INTFLAG) register
           •   Endpoint Interrupt Flag (EPINTFLAG) register
           •   Host Interrupt Flag (INTFLAG) register
           •   Pipe Interrupt Flag (PINTFLAG) register
          Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
          description.
          Write protection does not apply for accesses through an external debugger.

38.5.9    Analog Connections
          Not applicable.

38.5.10 Calibration
        The output drivers for the DP/DM USB line interface can be fine tuned with calibration values from
        production tests. The calibration values must be loaded from the NVM Software Calibration Area into the
        USB Pad Calibration register (PADCAL) by software, before enabling the USB, to achieve the specified
        accuracy. Refer to NVM Software Calibration Area Mapping for further details.
          For details on Pad Calibration, refer to Pad Calibration (38.8.1.6 PADCAL) register.



38.6      Functional Description

38.6.1    USB General Operation

38.6.1.1 Initialization
          After a hardware reset, the USB is disabled. The user should first enable the USB (CTRLA.ENABLE) in
          either device mode or host mode (CTRLA.MODE).




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1112
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                                     USB – Universal Serial Bus

Figure 38-2. General States




                                                                    HW RESET | CTRLA.SWRST
                                                                                              Any state




                                                             Idle




                              CTRLA.ENABLE = 1
                              CTRLA.MODE   =0



                                          CTRLA.ENABLE = 0    CTRLA.ENABLE = 1       CTRLA.ENABLE = 0
                                                              CTRLA.MODE   =1




                             Device                                                           Host




After a hardware reset, the USB is in the idle state. In this state:
  •   The module is disabled. The USB Enable bit in the Control A register (CTRLA.ENABLE) is reset.
  •   The module clock is stopped in order to minimize power consumption.
  •   The USB pad is in suspend mode.
  •   The internal states and registers of the device and host are reset.
Before using the USB, the Pad Calibration register (PADCAL) must be loaded with production calibration
values from the NVM Software Calibration Area.
The USB is enabled by writing a '1' to CTRLA.ENABLE. The USB is disabled by writing a '0' to
CTRLA.ENABLE.
The USB is reset by writing a '1' to the Software Reset bit in CTRLA (CTRLA.SWRST). All registers in the
USB will be reset to their initial state, and the USB will be disabled. Refer to the CTRLA register for
details.
The user can configure pads and speed before enabling the USB by writing to the Operating Mode bit in
the Control A register (CTRLA.MODE) and the Speed Configuration field in the Control B register
(CTRLB.SPDCONF). These values are taken into account once the USB has been enabled by writing a
'1' to CTRLA.ENABLE.
After writing a '1' to CTRLA.ENABLE, the USB enters device mode or host mode (according to
CTRLA.MODE).
The USB can be disabled at any time by writing a '0' to CTRLA.ENABLE.




© 2019 Microchip Technology Inc.                                      Datasheet                                DS60001507E-page 1113
                                                            SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

          Refer to 38.6.2 USB Device Operations for the basic operation of the device mode.
          Refer to 38.6.3 Host Operations for the basic operation of the host mode.

38.6.2    USB Device Operations
          This section gives an overview of the USB module device operation during normal transactions. For more
          details on general USB and USB protocol, refer to the Universal Serial Bus specification revision 2.1.

38.6.2.1 Initialization
          To attach the USB device to start the USB communications from the USB host, a zero should be written
          to the Detach bit in the Device Control B register (CTRLB.DETACH). To detach the device from the USB
          host, a one must be written to the CTRLB.DETACH.
          After the device is attached, the host will request the USB device descriptor using the default device
          address zero. On successful transmission, it will send a USB reset. After that, it sends an address to be
          configured for the device. All further transactions will be directed to this device address. This address
          should be configured in the Device Address field in the Device Address register (DADD.DADD) and the
          Address Enable bit in DADD (DADD.ADDEN) should be written to one to accept communications directed
          to this address. DADD.ADDEN is automatically cleared on receiving a USB reset.

38.6.2.2 Endpoint Configuration
          Endpoint data can be placed anywhere in the device RAM. The USB controller accesses these endpoints
          directly through the AHB master (built-in DMA) with the help of the endpoint descriptors. The base
          address of the endpoint descriptors needs to be written in the Descriptor Address register (DESCADD) by
          the user. Refer also to the Endpoint Descriptor structure in 38.8.4.1 Endpoint Descriptor Structure.
          Before using an endpoint, the user should configure the direction and type of the endpoint in Type of
          Endpoint field in the Device Endpoint Configuration register (EPCFG.EPTYPE0/1). The endpoint
          descriptor registers should be initialized to known values before using the endpoint, so that the USB
          controller does not read random values from the RAM.
          The Endpoint Size field in the Packet Size register (PCKSIZE.SIZE) should be configured as per the size
          reported to the host for that endpoint. The Address of Data Buffer register (ADDR) should be set to the
          data buffer used for endpoint transfers.
          The RAM Access Interrupt bit in Device Interrupt Flag register (INTFLAG.RAMACER) is set when a RAM
          access underflow error occurs during IN data stage.
          When an endpoint is disabled, the following registers are cleared for that endpoint:
           •   Device Endpoint Interrupt Enable Clear/Set (EPINTENCLR/SET) register
           •   Device Endpoint Interrupt Flag (EPINTFLAG) register
           •   Transmit Stall 0 bit in the Endpoint Status register (EPSTATUS.STALLRQ0)
           •   Transmit Stall 1 bit in the Endpoint Status register (EPSTATUS.STALLRQ1)

38.6.2.3 Multi-Packet Transfers
          Multi-packet transfer enables a data payload exceeding the endpoint maximum transfer size to be
          transferred as multiple packets without software intervention. This reduces the number of interrupts and
          software intervention required to manage higher level USB transfers. Multi-packet transfer is identical to
          the IN and OUT transactions described below unless otherwise noted in this section.
          The application software provides the size and address of the RAM buffer to be proceeded by the USB
          module for a specific endpoint, and the USB module will split the buffer in the required USB data transfers
          without any software intervention.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1114
                                                             SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

         Figure 38-3. Multi-Packet Feature - Reduction of CPU Overhead




                 Data Payload
                                                       Without Multi-packet support
                                                                                                       Transfer Complete Interrupt
                                                                                                                   &
                                                                                                            Data Processing
                      Maximum Endpoint size


                                                       With Multi-packet support



38.6.2.4 USB Reset
         The USB bus reset is initiated by a connected host and managed by hardware.
         During USB reset the following registers are cleared:
          • Device Endpoint Configuration (EPCFG) register - except for Endpoint 0
          • Device Frame Number (FNUM) register
          •   Device Address (DADD) register
          •   Device Endpoint Interrupt Enable Clear/Set (EPINTENCLR/SET) register
          •   Device Endpoint Interrupt Flag (EPINTFLAG) register
          •   Transmit Stall 0 bit in the Endpoint Status register (EPSTATUS.STALLRQ0)
          •   Transmit Stall 1 bit in the Endpoint Status register (EPSTATUS.STALLRQ1)
          •   Endpoint Interrupt Summary (EPINTSMRY) register
          •   Upstream resume bit in the Control B register (CTRLB.UPRSM)
         At the end of the reset process, the End of Reset bit is set in the Interrupt Flag register
         (INTFLAG.EORST).
38.6.2.5 Start-of-Frame
         When a Start-of-Frame (SOF) token is detected, the frame number from the token is stored in the Frame
         Number field in the Device Frame Number register (FNUM.FNUM), and the Start-of-Frame interrupt bit in
         the Device Interrupt Flag register (INTFLAG.SOF) is set. If there is a CRC or bit-stuff error, the Frame
         Number Error status flag (FNUM.FNCERR) in the FNUM register is set.
38.6.2.6 Management of SETUP Transactions
         When a SETUP token is detected and the device address of the token packet does not match
         DADD.DADD, the packet is discarded and the USB module returns to idle and waits for the next token
         packet.
         When the address matches, the USB module checks if the endpoint is enabled in EPCFG. If the
         addressed endpoint is disabled, the packet is discarded and the USB module returns to idle and waits for
         the next token packet.
         When the endpoint is enabled, the USB module then checks on the EPCFG of the addressed endpoint. If
         the EPCFG.EPTYPE0 is not set to control, the USB module returns to idle and waits for the next token
         packet.
         When the EPCFG.EPTYPE0 matches, the USB module then fetches the Data Buffer Address (ADDR)
         from the addressed endpoint's descriptor and waits for a DATA0 packet. If a PID error or any other PID
         than DATA0 is detected, the USB module returns to idle and waits for the next token packet.




        © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1115
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            USB – Universal Serial Bus

        When the data PID matches and if the Received Setup Complete interrupt bit in the Device Endpoint
        Interrupt Flag register (EPINTFLAG.RXSTP) is equal to zero, ignoring the Bank 0 Ready bit in the Device
        Endpoint Status register (EPSTATUS.BK0RDY), the incoming data is written to the data buffer pointed to
        by the Data Buffer Address (ADDR). If the number of received data bytes exceeds the endpoint's
        maximum data payload size as specified by the PCKSIZE.SIZE, the remainders of the received data
        bytes are discarded. The packet will still be checked for bit-stuff and CRC errors. Software must never
        report a endpoint size to the host that is greater than the value configured in PCKSIZE.SIZE. If a bit-stuff
        or CRC error is detected in the packet, the USB module returns to idle and waits for the next token
        packet.
        If data is successfully received, an ACK handshake is returned to the host, and the number of received
        data bytes, excluding the CRC, is written to the Byte Count (PCKSIZE.BYTE_COUNT). If the number of
        received data bytes is the maximum data payload specified by PCKSIZE.SIZE, no CRC data is written to
        the data buffer. If the number of received data bytes is the maximum data payload specified by
        PCKSIZE.SIZE minus one, only the first CRC data is written to the data buffer. If the number of received
        data is equal or less than the data payload specified by PCKSIZE.SIZE minus two, both CRC data bytes
        are written to the data buffer.
        Finally the EPSTATUS is updated. Data Toggle OUT bit (EPSTATUS.DTGLOUT), the Data Toggle IN bit
        (EPSTATUS.DTGLIN), the current bank bit (EPSTATUS.CURRBK) and the Bank Ready 0 bit
        (EPSTATUS.BK0RDY) are set. Bank Ready 1 bit (EPSTATUS.BK1RDY) and the Stall Bank 0/1 bit
        (EPSTATUS.STALLQR0/1) are cleared on receiving the SETUP request. The RXSTP bit is set and
        triggers an interrupt if the Received Setup Interrupt Enable bit is set in Endpoint Interrupt Enable Set/
        Clear register (EPINTENSET/CLR.RXSTP).
38.6.2.7 Management of OUT Transactions
        Figure 38-4. OUT Transfer: Data Packet Host to USB Device
                                                                                                    Memory Map
         HOST
                                                                                                     I/O Register

                                                                                                  USB I/O Registers




                     BULK OUT             BULK OUT        BULK OUT                                  Internal RAM
                       EPT 2                EPT 3           EPT 1             USB Module
                                                                                                                      DESCADD
                                                                                                  USB Endpoints
                                                                                                  Descriptor Table
                      D   D   D      D    D   D   D   D   D   D   D
                      A   A   A      A    A   A   A   A   A   A   A
                      T   T   T      T    T   T   T   T   T   T   T
                      A   A   A      A    A   A   A   A   A   A   A                              ENDPOINT 1 DATA
                      0   1   0      0    1   0   1   0   0   1   0
                                                                                                 ENDPOINT 3 DATA
            DP                                                                USB Buffers
            DM

                                                                      time                       ENDPOINT 2 DATA




        When an OUT token is detected, and the device address of the token packet does not match
        DADD.DADD, the packet is discarded and the USB module returns to idle and waits for the next token
        packet.




       © 2019 Microchip Technology Inc.                               Datasheet                         DS60001507E-page 1116
                                                           SAM D5x/E5x Family Data Sheet
                                                                                 USB – Universal Serial Bus

         If the address matches, the USB module checks if the endpoint number received is enabled in the
         EPCFG of the addressed endpoint. If the addressed endpoint is disabled, the packet is discarded and the
         USB module returns to idle and waits for the next token packet.
         When the endpoint is enabled, the USB module then checks the Endpoint Configuration register
         (EPCFG) of the addressed output endpoint. If the type of the endpoint (EPCFG.EPTYPE0) is not set to
         OUT, the USB module returns to idle and waits for the next token packet.
         The USB module then fetches the Data Buffer Address (ADDR) from the addressed endpoint's descriptor,
         and waits for a DATA0 or DATA1 packet. If a PID error or any other PID than DATA0 or DATA1 is
         detected, the USB module returns to idle and waits for the next token packet.
         If EPSTATUS.STALLRQ0 in EPSTATUS is set, the incoming data is discarded. If the endpoint is not
         isochronous, a STALL handshake is returned to the host and the Transmit Stall Bank 0 interrupt bit in
         EPINTFLAG (EPINTFLAG.STALL0) is set.
         For isochronous endpoints, data from both a DATA0 and DATA1 packet will be accepted. For other
         endpoint types the PID is checked against EPSTATUS.DTGLOUT. If a PID mismatch occurs, the
         incoming data is discarded, and an ACK handshake is returned to the host.
         If EPSTATUS.BK0RDY is set, the incoming data is discarded, the bit Transmit Fail 0 interrupt bit in
         EPINTFLAG (EPINTFLAG.TRFAIL0) and the status bit STATUS_BK.ERRORFLOW are set. If the
         endpoint is not isochronous, a NAK handshake is returned to the host.
         The incoming data is written to the data buffer pointed to by the Data Buffer Address (ADDR). If the
         number of received data bytes exceeds the maximum data payload specified as PCKSIZE.SIZE, the
         remainders of the received data bytes are discarded. The packet will still be checked for bit-stuff and CRC
         errors. If a bit-stuff or CRC error is detected in the packet, the USB module returns to idle and waits for
         the next token packet.
         If the endpoint is isochronous and a bit-stuff or CRC error in the incoming data, the number of received
         data bytes, excluding CRC, is written to PCKSIZE.BYTE_COUNT. Finally the EPINTFLAG.TRFAIL0 and
         CRC Error bit in the Device Bank Status register (STATUS_BK.CRCERR) is set for the addressed
         endpoint.
         If data was successfully received, an ACK handshake is returned to the host if the endpoint is not
         isochronous, and the number of received data bytes, excluding CRC, is written to
         PCKSIZE.BYTE_COUNT. If the number of received data bytes is the maximum data payload specified by
         PCKSIZE.SIZE no CRC data bytes are written to the data buffer. If the number of received data bytes is
         the maximum data payload specified by PCKSIZE.SIZE minus one, only the first CRC data byte is written
         to the data buffer If the number of received data is equal or less than the data payload specified by
         PCKSIZE.SIZE minus two, both CRC data bytes are written to the data buffer.
         Finally in EPSTATUS for the addressed output endpoint, EPSTATUS.BK0RDY is set and
         EPSTATUS.DTGLOUT is toggled if the endpoint is not isochronous. The flag Transmit Complete 0
         interrupt bit in EPINTFLAG (EPINTFLAG.TRCPT0) is set for the addressed endpoint.
38.6.2.8 Multi-Packet Transfers for OUT Endpoint
         The number of data bytes received is stored in endpoint PCKSIZE.BYTE_COUNT as for normal
         operation. Since PCKSIZE.BYTE_COUNT is updated after each transaction, it must be set to zero when
         setting up a new transfer. The total number of bytes to be received must be written to
         PCKSIZE.MULTI_PACKET_SIZE. This value must be a multiple of PCKSIZE.SIZE, otherwise excess
         data may be written to SRAM locations used by other parts of the application.




        © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1117
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                USB – Universal Serial Bus

        EPSTATUS.DTGLOUT management for non-isochronous packets and EPINTFLAG.BK1RDY/BK0RDY
        management are as for normal operation.
        If a maximum payload size packet is received, PCKSIZE.BYTE_COUNT will be incremented by
        PCKSIZE.SIZE after the transaction has completed, and EPSTATUS.DTGLOUT will be toggled if the
        endpoint is not isochronous. If the updated PCKSIZE.BYTE_COUNT is equal to
        PCKSIZE.MULTI_PACKET_SIZE (i.e. the last transaction), EPSTATUS.BK1RDY/BK0RDY, and
        EPINTFLAG.TRCPT0/TRCPT1 will be set.
38.6.2.9 Management of IN Transactions
        Figure 38-5. IN Transfer: Data Packet USB Device to Host After Request from Host




                                                                                                       Memory Map

          HOST                                                                                          I/O Register

                                                                                    CPU              USB I/O Registers




                                                                                                       Internal RAM
                                                                                                    ENDPOINT 2 DATA
                                                                                  USB Module
                              EPT 2                 EPT 3             EPT 1                                              DESCADD
                                                                                                     USB Endpoints
                              D   D   D     D   D   D   D   D     D    D      D                      Descriptor Table
                              A   A   A     A   A   A   A   A     A    A      A
                              T   T   T     T   T   T   T   T     T    T      T
                              A   A   A     A   A   A   A   A     A    A      A
                              0   1   0     0   1   0   1   0     0    1      0                     ENDPOINT 3 DATA


            DP                                                                    USB Buffers
            DM
                          I             I                     I
                          N             N                     N
                  EPT 2   T       EPT 3 T               EPT 1 T
                          O             O                     O                                     ENDPOINT 1 DATA
                          K             K                     K
                          E             E                     E
                          N             N                     N

                                                                      time


        When an IN token is detected, and if the device address of the token packet does not match
        DADD.DADD, the packet is discarded and the USB module returns to idle and waits for the next token
        packet.
        When the address matches, the USB module checks if the endpoint received is enabled in the EPCFG of
        the addressed endpoint and if not, the packet is discarded and the USB module returns to idle and waits
        for the next token packet.
        When the endpoint is enabled, the USB module then checks on the EPCFG of the addressed input
        endpoint. If the EPCFG.EPTYPE1 is not set to IN, the USB module returns to idle and waits for the next
        token packet.
        If EPSTATUS.STALLRQ1 in EPSTATUS is set, and the endpoint is not isochronous, a STALL handshake
        is returned to the host and EPINTFLAG.STALL1 is set.




        © 2019 Microchip Technology Inc.                                Datasheet                            DS60001507E-page 1118
                                                            SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

         If EPSTATUS.BK1RDY is cleared, the flag EPINTFLAG.TRFAIL1 is set. If the endpoint is not
         isochronous, a NAK handshake is returned to the host.
         The USB module then fetches the Data Buffer Address (ADDR) from the addressed endpoint's descriptor.
         The data pointed to by the Data Buffer Address (ADDR) is sent to the host in a DATA0 packet if the
         endpoint is isochronous. For non-isochronous endpoints a DATA0 or DATA1 packet is sent depending on
         the state of EPSTATUS.DTGLIN. When the number of data bytes specified in endpoint
         PCKSIZE.BYTE_COUNT is sent, the CRC is appended and sent to the host.
         For isochronous endpoints, EPSTATUS.BK1RDY is cleared and EPINTFLAG.TRCPT1 is set.
         For all non-isochronous endpoints the USB module waits for an ACK handshake from the host. If an ACK
         handshake is not received within 16 bit times, the USB module returns to idle and waits for the next token
         packet. If an ACK handshake is successfully received EPSTATUS.BK1RDY is cleared,
         EPINTFLAG.TRCPT1 is set and EPSTATUS.DTGLIN is toggled.
38.6.2.10 Multi-Packet Transfers for IN Endpoint
         The total number of data bytes to be sent is written to PCKSIZE.BYTE_COUNT as for normal operation.
         The Multi-packet size register (PCKSIZE.MULTI_PACKET_SIZE) is used to store the number of bytes
         that are sent, and must be written to zero when setting up a new transfer.
         When an IN token is received, PCKSIZE.BYTE_COUNT and PCKSIZE.MULTI_PACKET_SIZE are
         fetched. If PCKSIZE.BYTE_COUNT minus PCKSIZE.MULTI_PACKET_SIZE is less than the endpoint
         PCKSIZE.SIZE, endpoint BYTE_COUNT minus endpoint PCKSIZE.MULTI_PACKET_SIZE bytes are
         transmitted, otherwise PCKSIZE.SIZE number of bytes are transmitted. If endpoint
         PCKSIZE.BYTE_COUNT is a multiple of PCKSIZE.SIZE, the last packet sent will be zero-length if the
         AUTOZLP bit is set.
         If a maximum payload size packet was sent (i.e. not the last transaction), MULTI_PACKET_SIZE will be
         incremented by the PCKSIZE.SIZE. If the endpoint is not isochronous the EPSTATUS.DTLGIN bit will be
         toggled when the transaction has completed. If a short packet was sent (i.e. the last transaction),
         MULTI_PACKET_SIZE is incremented by the data payload. EPSTATUS.BK0/1RDY will be cleared and
         EPINTFLAG.TRCPT0/1 will be set.
38.6.2.11 Ping-Pong Operation
         When an endpoint is configured for ping-pong operation, it uses both the input and output data buffers
         (banks) for a given endpoint in a single direction. The direction is selected by enabling one of the IN or
         OUT direction in EPCFG.EPTYPE0/1 and configuring the opposite direction in EPCFG.EPTYPE1/0 as
         Dual Bank.
         When ping-pong operation is enabled for an endpoint, the endpoint in the opposite direction must be
         configured as dual bank. The data buffer, data address pointer and byte counter from the enabled
         endpoint are used as Bank 0, while the matching registers from the disabled endpoint are used as Bank
         1.




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1119
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

        Figure 38-6. Ping-Pong Overview


                                                                                               Endpoint
                                                                                              single bank
                  Without Ping Pong
                                                                                       t


                                                                                              Endpoint
                                                                                              dual bank
                                                                                                Bank0

                     With Ping Pong                                                             Bank1
                                                                                       t




                                USB data packet

                                Available time for data processing by CPU
                                to avoid NACK

        The Bank Select flag in EPSTATUS.CURBK indicates which bank data will be used in the next
        transaction, and is updated after each transaction. According to EPSTATUS.CURBK,
        EPINTFLAG.TRCPT0 or EPINTFLAG.TRFAIL0 or EPINTFLAG.TRCPT1 or EPINTFLAG.TRFAIL1 in
        EPINTFLAG and Data Buffer 0/1 ready (EPSTATUS.BK0RDY and EPSTATUS.BK1RDY) are set. The
        EPSTATUS.DTGLOUT and EPSTATUS.DTGLIN are updated for the enabled endpoint direction only.
38.6.2.12 Feedback Operation
        Feedback endpoints are endpoints with same the address but in different directions. This is usually used
        in explicit feedback mechanism in USB Audio, where a feedback endpoint is associated to one or more
        isochronous data endpoints to which it provides feedback service. The feedback endpoint always has the
        opposite direction from the data endpoint.
        The feedback endpoint always has the opposite direction from the data endpoint(s). The feedback
        endpoint has the same endpoint number as the first (lower) data endpoint. A feedback endpoint can be
        created by configuring an endpoint with different endpoint size (PCKSIZE.SIZE) and different endpoint
        type (EPCFG.EPTYPE0/1) for the IN and OUT direction.
        Example Configuration for Feedback Operation:
         • Endpoint n / IN: EPCFG.EPTYPE1 = Interrupt IN, PCKSIZE.SIZE = 64.
         • Endpoint n / OUT: EPCFG.EPTYPE0= Isochronous OUT, PCKSIZE.SIZE = 512.
38.6.2.13 Suspend State and Pad Behavior
        The following figure, Pad Behavior, illustrates the behavior of the USB pad in Device mode.




        © 2019 Microchip Technology Inc.                              Datasheet             DS60001507E-page 1120
                                                 SAM D5x/E5x Family Data Sheet
                                                                       USB – Universal Serial Bus

Figure 38-7. Pad Behavior




                                                    CTRLA.ENABLE = 1
                                   Idle         |   CTRLB.DETACH = 0
                                               | INTFLAG.SUSPEND = 0




                        CTRLA.ENABLE = 0
                   |    CTRLB.DETACH = 1
                   | INTFLAG.SUSPEND = 1
                                                          Active




In Idle state, the pad is in Low Power Consumption mode.
In Active state, the pad is active.
The following figure, Pad Events, illustrates the pad events leading to a PAD state change.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1121
                                                          SAM D5x/E5x Family Data Sheet
                                                                                     USB – Universal Serial Bus

        Figure 38-8. Pad Events




                                   Suspend detected              Cleared on Wakeup




                                                        Wakeup detected      Cleared by software to acknowledge the interrupt




                                          Active          Idle                          Active




        The Suspend Interrupt bit in the Device Interrupt Flag register (INTFLAG.SUSPEND) is set when a USB
        Suspend state has been detected on the USB bus. The USB pad is then automatically put in the Idle
        state. The detection of a non-idle state sets the Wake Up Interrupt bit (INTFLAG.WAKEUP) and wakes
        the USB pad.
        The pad goes to the Idle state if the USB module is disabled or if CTRLB.DETACH is written to one. It
        returns to the Active state when CTRLA.ENABLE is written to one and CTRLB.DETACH is written to zero.
38.6.2.14 Remote Wakeup
        The remote wakeup request (also known as upstream resume) is the only request the device may send
        on its own initiative. This should be preceded by a DEVICE_REMOTE_WAKEUP request from the host.
        First, the USB must have detected a “Suspend” state on the bus, i.e. the remote wakeup request can only
        be sent after INTFLAG.SUSPEND has been set.
        The user may then write a one to the Remote Wakeup bit (CTRLB.UPRSM) to send an Upstream
        Resume to the host initiating the wakeup. This will automatically be done by the controller after 5 ms of
        inactivity on the USB bus.
        When the controller sends the Upstream Resume INTFLAG.WAKEUP is set and INTFLAG.SUSPEND is
        cleared.
        The CTRLB.UPRSM is cleared at the end of the transmitting Upstream Resume.
        In case of a rebroadcast resume initiated by the host, the End of Resume bit (INTFLAG.EORSM) flag is
        set when the rebroadcast resume is completed.




       © 2019 Microchip Technology Inc.                     Datasheet                                DS60001507E-page 1122
                                                          SAM D5x/E5x Family Data Sheet
                                                                                USB – Universal Serial Bus

        In the case where the CTRLB.UPRSM bit is set while a host initiated downstream resume is already
        started, the CTRLB.UPRSM is cleared and the upstream resume request is ignored.
38.6.2.15 Link Power Management L1 (LPM-L1) Suspend State Entry and Exit as Device
        The LPM Handshake bit in CTRLB.LPMHDSK should be configured to accept the LPM transaction.
        When a LPM transaction is received on any enabled endpoint n and a handshake has been sent in
        response by the controller according to CTRLB.LPMHDSK, the Device Link Power Manager (EXTREG)
        register is updated in the bank 0 of the addressed endpoint's descriptor. It contains information such as
        the Best Effort Service Latency (BESL), the Remote Wake bit (bRemoteWake), and the Link State
        parameter (bLinkState). Usually, the LPM transaction uses only the endpoint number 0.
        If the LPM transaction was positively acknowledged (ACK handshake), USB sets the Link Power
        Management Interrupt bit (INTFLAG.LPMSUSP) bit which indicates that the USB transceiver is
        suspended, reducing power consumption. This suspend occurs 9 microseconds after the LPM transaction
        according to the specification.
        To further reduce consumption, it is recommended to stop the USB clock while the device is suspended.
        The MCU can also enter in one of the available sleep modes if the wakeup time latency of the selected
        sleep mode complies with the host latency constraint (see the BESL parameter in 38.8.4.4 EXTREG
        register).
        Recovering from this LPM-L1 suspend state is exactly the same as the Suspend state (see Section
        38.6.2.13 Suspend State and Pad Behavior) except that the remote wakeup duration initiated by USB is
        shorter to comply with the Link Power Management specification.
        If the LPM transaction is responded with a NYET, the Link Power Management Not Yet Interrupt Flag
        (INTFLAG.LPMNYET) is set. This generates an interrupt if the Link Power Management Not Yet Interrupt
        Enable bit (INTENCLR/SET.LPMNYET) is set.
        If the LPM transaction is responded with a STALL or no handshake, no flag is set, and the transaction is
        ignored.




        © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1123
                                                                              SAM D5x/E5x Family Data Sheet
                                                                                                          USB – Universal Serial Bus

38.6.2.16 USB Device Interrupt
         Figure 38-9. Device Interrupt
                           EPINTFLAG7.STALL

                                                  EPINTENSET7.STALL0/STALL1
                           EPINTFLAG7.TRFAIL1

                                                  EPINTENSET7.TRFAIL1
                           EPINTFLAG7.TRFAIL0

                                                                                          EPINTSMRY
                                                  EPINTENSET7.TRFAIL0

             ENDPOINT7    EPINTFLAG7.RXSTP                                                EPINT7

                                                  EPINTENSET7.RXSTP                       EPINT6
                          EPINTFLAG7.TRCPT1

                                                   EPINTENSET7.TRCPT1

                           EPINTFLAG7.TRCPT0

                                                   EPINTENSET7.TRCPT0

                                                                                                                          USB EndPoint
                                                                                                                            Interrupt



                            EPINTFLAG0.STALL

                                                EPINTENSET0.STALL0/STALL1
                           EPINTFLAG0.TRFAIL1

                                                EPINTENSET0.TRFAIL1
                           EPINTFLAG0.TRFAIL0

                                                EPINTENSET0.TRFAIL0                       EPINT1

                           EPINTFLAG0.RXSTP                                               EPINT0

              ENDPOINT0                         EPINTENSET0.RXSTP

                           EPINTFLAG0.TRCPT1

                                                EPINTENSET0.TRCPT1

                           EPINTFLAG0.TRCPT0
                                                                                                                                             USB
                                                EPINTENSET0.TRCPT0                                                                         Interrupt




                          INTFLAG.LPMSUSP

                                                  INTENSET.LPMSUSP

                          INTFLAG.LPMNYET

                                                  INTENSET.DDISC

                          INTFLAG.RAMACER

                                                  INTENSET.RAMACER

                          INTFLAG.UPRSM

                INTFLAG                           INTENSET.UPRSM

                          INTFLAG.EORSM
                                                                                                   USB Device Interrupt
                                                  INTENSET.EORSM

                          INTFLAG.WAKEUP   *
                                                  INTENSET.WAKEUP

                          INTFLAG.EORST

                                                  INTENSET.EORST

                          INTFLAG.SOF

                                                  INTENSET.SOF

                         INTFLAGA.MSOF

                                                  INTENSET.MSOF

                          INTFLAG.SUSPEND

                                                  INTENSET.SUSPEND



                  * Asynchronous interrupt
         The WAKEUP is an asynchronous interrupt and can be used to wake-up the device from any sleep mode.




        © 2019 Microchip Technology Inc.                                      Datasheet                                        DS60001507E-page 1124
                                                           SAM D5x/E5x Family Data Sheet
                                                                                 USB – Universal Serial Bus

38.6.3   Host Operations
         This section gives an overview of the USB module Host operation during normal transactions. For more
         details on general USB and USB protocol, refer to Universal Serial Bus Specification revision 2.1.
38.6.3.1 Device Detection and Disconnection
         Prior to device detection the software must set the VBUS is OK bit (CTRLB.VBUSOK) register when the
         VBUS is available. This notifies the USB host that USB operations can be started. When the bit
         CTRLB.VBUSOK is zero and even if the USB HOST is configured and enabled, host operation is halted.
         Setting the bit CTRLB.VBUSOK will allow host operation when the USB is configured.
         The Device detection is managed by the software using the Line State field in the Host Status
         (STATUS.LINESTATE) register. The device connection is detected by the host controller when DP or DM
         is pulled high, depending of the speed of the device.
         The device disconnection is detected by the host controller when both DP and DM are pulled down using
         the STATUS.LINESTATE registers.
         The Device Connection Interrupt bit (INTFLAG.DCONN) is set if a device connection is detected.
         The Device Disconnection Interrupt bit (INTFLAG.DDISC) is set if a device disconnection is detected.
38.6.3.2 Host Terminology
         In host mode, the term pipe is used instead of endpoint. A host pipe corresponds to a device endpoint,
         refer to "Universal Serial Bus Specification revision 2.1." for more information.
38.6.3.3 USB Reset
         The USB sends a USB reset signal when the user writes a one to the USB Reset bit
         (CTRLB.BUSRESET). When the USB reset has been sent, the USB Reset Sent Interrupt bit in the
         INTFLAG (INTFLAG.RST) is set and all pipes will be disabled.
         If the bus was previously in a suspended state (i.e., the Start of Frame Generation Enable bit
         (CTRLB.SOFE) is zero), the USB will switch it to the Resume state, causing the bus to asynchronously
         set the Host Wakeup Interrupt flag (INTFLAG.WAKEUP). The CTRLB.SOFE bit will be set in order to
         generate SOFs immediately after the USB reset.
         During USB reset the following registers are cleared:
           •   All Host Pipe Configuration register (PCFG)
           •   Host Frame Number register (FNUM)
           •   Interval for the Bulk-Out/Ping transaction register (BINTERVAL)
           •   Host Start-of-Frame Control register (HSOFC)
           •   Pipe Interrupt Enable Clear/Set register (PINTENCLR/SET)
           •   Pipe Interrupt Flag register (PINTFLAG)
           •   Pipe Freeze bit in Pipe Status register (PSTATUS.FREEZE)
         After the reset the user should check the Speed Status field in the Status register (STATUS.SPEED) to
         find out the current speed according to the capability of the peripheral.
38.6.3.4 Pipe Configuration
         Pipe data can be placed anywhere in the RAM. The USB controller accesses these pipes directly through
         the AHB master (built-in DMA) with the help of the pipe descriptors. The base address of the pipe
         descriptors needs to be written in the Descriptor Address register (DESCADD) by the user. Refer also to
         38.8.7.1 Pipe Descriptor Structure.
         Before using a pipe, the user should configure the direction and type of the pipe in Type of Pipe field in
         the Host Pipe Configuration register (PCFG.PTYPE). The pipe descriptor registers should be initialized to




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1125
                                                             SAM D5x/E5x Family Data Sheet
                                                                                     USB – Universal Serial Bus

         known values before using the pipe, so that the USB controller does not read the random values from the
         RAM.
         The Pipe Size field in the Packet Size register (PCKSIZE.SIZE) should be configured as per the size
         reported by the device for the endpoint associated with this pipe. The Address of Data Buffer register
         (ADDR) should be set to the data buffer used for pipe transfers.
         The Pipe Bank bit (PCFG.BK) should be set to one if dual banking is desired. Dual bank is not supported
         for Control pipes.
         The Ram Access Interrupt bit in Host Interrupt Flag register (INTFLAG.RAMACER) is set when a RAM
         access underflow error occurs during an OUT stage.
         When a pipe is disabled, the following registers are cleared for that pipe:
          •   Interval for the Bulk-Out/Ping transaction register (BINTERVAL)
          •   Pipe Interrupt Enable Clear/Set register (PINTENCLR/SET)
          •   Pipe Interrupt Flag register (PINTFLAG)
          •   Pipe Freeze bit in Pipe Status register (PSTATUS.FREEZE)

38.6.3.5 Pipe Activation
         A disabled pipe is inactive, and will be reset along with its context registers (pipe registers for the pipe n).
         Pipes are enabled by writing the Type of the Pipe bit (PCFG.PTYPE) to a value different than 0x0
         (disabled).
         When a pipe is enabled, the Pipe Freeze bit in the Pipe Status register (PSTATUS.FREEZE) is set. This
         allows the user to complete the configuration of the pipe, without starting a USB transfer.
         When starting an enumeration, the user retrieves the device descriptor by sending a GET_DESCRIPTOR
         USB request. This descriptor contains the maximal packet size of the device default control endpoint
         (bMaxPacketSize0), which the user should use to reconfigure the size of the default control pipe.

38.6.3.6 Pipe Address Setup
         Once the device has answered the first host requests with the default device address 0, the host assigns
         a new address to the device. The host controller has to send a USB reset to the device and a
         SET_ADDRESS(addr) SETUP request with the new address to be used by the device. Once this SETUP
         transaction is complete, the user writes the new address to the Pipe Device Address field in the Host
         Control Pipe register (CTRL_PIPE.PDADDR) in Pipe descriptor. All following requests by this pipe will be
         performed using this new address.

38.6.3.7 Suspend and Wakeup
         Setting CTRLB.SOFE to zero when in host mode will cause the USB to cease sending Start-of-Frames
         on the USB bus and enter the Suspend state. The USB device will enter the Suspend state 3ms later.
         Before entering suspend by writing CTRLB.SOFE to zero, the user must freeze the active pipes by
         setting their PSTATUS.FREEZE bit. Any current on-going pipe will complete its transaction, and then all
         pipes will be inactive. The user should wait at least 1 complete frame before entering the suspend mode
         to avoid any data loss.
         The device can awaken the host by sending an Upstream Resume (Remote Wakeup feature). When the
         host detects a non-idle state on the USB bus, it sets the INTFLAG.WAKEUP. If the non-idle bus state
         corresponds to an Upstream Resume (K state), the Upstream Resume Received Interrupt bit in INTFLAG
         (INTFLAG.UPRSM) is set and the user must generate a Downstream Resume within 1 ms and for at
         least 20 ms. It is required to first write a one to the Send USB Resume bit in CTRLB (CTRLB.RESUME)
         to respond to the upstream resume with a downstream resume. Alternatively, the host can resume from a




        © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 1126
                                                           SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

        suspend state by sending a Downstream Resume on the USB bus (CTRLB.RESUME set to 1). In both
        cases, when the downstream resume is completed, the CTRLB.SOFE bit is automatically set and the
        host enters again the active state.

38.6.3.8 Phase-locked SOFs
        To support the Synchronous Endpoints capability, the period of the emitted Start-of-Frame is maintained
        while the USB connection is not in the active state. This does not apply for the disconnected/connected/
        reset states. It applies for active/idle/suspend/resume states. The period of Start-of-Frame will be 1ms
        when the USB connection is in active state and an integer number of milli-seconds across idle/suspend/
        resume states.
        To ensure the Synchronous Endpoints capability, the GCLK_USB clock must be kept running. If the
        GCLK_USB is interrupted, the period of the emitted Start-of-Frame will be erratic.

38.6.3.9 Management of Control Pipes
        A control transaction is composed of three stages:
          • SETUP
          • Data (IN or OUT)
          • Status (IN or OUT)
        The user has to change the pipe token according to each stage using the Pipe Token field in PCFG
        (PCFG.PTOKEN).
        For control pipes only, the token is assigned a specific initial data toggle sequence:
          • SETUP: Data0
          • IN: Data1
          • OUT: Data1

38.6.3.10 Management of IN Pipes
        IN packets are sent by the USB device controller upon IN request reception from the host. All the
        received data from the device to the host will be stored in the bank provided the bank is empty. The pipe
        and its descriptor in RAM must be configured.
        The host indicates it is able to receive data from the device by clearing the Bank 0/1 Ready bit in
        PSTATUS (PSTATUS.BK0/1RDY), which means that the memory for the bank is available for new USB
        transfer.
        The USB will perform IN requests as long as the pipe is not frozen by the user.
        The generation of IN requests starts when the pipe is unfrozen (PSTATUS.PFREEZE is set to zero).
        When the current bank is full, the Transmit Complete 0/1 bit in PINTFLAG (PINTFLAG.TRCPT0/1) will be
        set and trigger an interrupt if enabled and the PSTATUS.BK0/1RDY bit will be set.
        PINTFLAG.TRCPT0/1 must be cleared by software to acknowledge the interrupt. This is done by writing
        a one to the PINTFLAG.TRCPT0/1 of the addressed pipe.
        The user reads the PCKSIZE.BYTE_COUNT to know how many bytes should be read.
        To free the bank the user must read the IN data from the address ADDR in the pipe descriptor and clear
        the PKSTATUS.BK0/1RDY bit. When the IN pipe is composed of multiple banks, a successful IN
        transaction will switch to the next bank. Another IN request will be performed by the host as long as the
        PSTATUS.BK0/1RDY bit for that bank is set. The PINTFLAG.TRCPT0/1 and PSTATUS.BK0/1RDY will be
        updated accordingly.




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1127
                                                            SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

         The user can follow the current bank looking at Current Bank bit in PSTATUS (PSTATUS.CURBK) and by
         looking at Data Toggle for IN pipe bit in PSTATUS (PSTATUS.DTGLIN).
         When the pipe is configured as single bank (Pipe Bank bit in PCFG (PCFG.BK) is 0), only
         PINTFLAG.TRCPT0 and PSTATUS.BK0 are used. When the pipe is configured as dual bank (PCFG.BK
         is 1), both PINTFLAG.TRCPT0/1 and PSTATUS.BK0/1 are used.

38.6.3.11 Management of OUT Pipes
         OUT packets are sent by the host. All the data stored in the bank will be sent to the device provided the
         bank is filled. The pipe and its descriptor in RAM must be configured.
         The host can send data to the device by writing to the data bank 0 in single bank or the data bank 0/1 in
         dual bank.
         The generation of OUT packet starts when the pipe is unfrozen (PSTATUS.PFREEZE is zero).
         The user writes the OUT data to the data buffer pointer by ADDR in the pipe descriptor and allows the
         USB to send the data by writing a one to the PSTATUS.BK0/1RDY. This will also cause a switch to the
         next bank if the OUT pipe is part of a dual bank configuration.
         PINTFLAGn.TRCPT0/1 must be cleared before setting PSTATUS.BK0/1RDY to avoid missing an
         PINTFLAGn.TRCPT0/1 event.

38.6.3.12 Alternate Pipe
         The user has the possibility to run sequentially several logical pipes on the same physical pipe. It allows
         addressing of any device endpoint of any attached device on the bus.
         Before switching pipe, the user should save the pipe context (Pipe registers and descriptor for pipe n).
         After switching pipe, the user should restore the pipe context (Pipe registers and descriptor for pipe n)
         and in particular PCFG, and PSTATUS.

38.6.3.13 Data Flow Error
         This error exists only for isochronous and interrupt pipes for both IN and OUT directions. It sets the
         Transmit Fail bit in PINTFLAG (PINTFLAG.TRFAIL), which triggers an interrupt if the Transmit Fail bit in
         PINTENCLR/SET(PINTENCLR/SET.TRFAIL) is set. The user must check the Pipe Interrupt Summary
         register (PINTSMRY) to find out the pipe which triggered the interrupt. Then the user must check the
         origin of the interrupt’s bank by looking at the Pipe Bank Status register (STATUS_BK) for each bank. If
         the Error Flow bit in the STATUS_BK (STATUS_BK.ERRORFLOW) is set then the user is able to
         determine the origin of the data flow error. As the user knows that the endpoint is an IN or OUT the error
         flow can be deduced as OUT underflow or as an IN overflow.
         An underflow can occur during an OUT stage if the host attempts to send data from an empty bank. If a
         new transaction is successful, the relevant bank descriptor STATUS_BK.ERRORFLOW will be cleared.
         An overflow can occur during an IN stage if the device tries to send a packet while the bank is full.
         Typically this occurs when a CPU is not fast enough. The packet data is not written to the bank and is
         lost. If a new transaction is successful, the relevant bank descriptor STATUS_BK.ERRORFLOW will be
         cleared.

38.6.3.14 CRC Error
         This error exists only for isochronous IN pipes. It sets the PINTFLAG.TRFAIL, which triggers an interrupt
         if PINTENCLR/SET.TRFAIL is set. The user must check the PINTSMRY to find out the pipe which
         triggered the interrupt. Then the user must check the origin of the interrupt’s bank by looking at the bank
         descriptor STATUS_BK for each bank and if the CRC Error bit in STATUS_BK (STATUS_BK.CRCERR) is
         set then the user is able to determine the origin of the CRC error. A CRC error can occur during the IN




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1128
                                                          SAM D5x/E5x Family Data Sheet
                                                                                USB – Universal Serial Bus

        stage if the USB detects a corrupted packet. The IN packet will remain stored in the bank and
        PINTFLAG.TRCPT0/1 will be set.

38.6.3.15 PERR Error
        This error exists for all pipes. It sets the PINTFLAG.PERR Interrupt, which triggers an interrupt if
        PINTFLAG.PERR is set. The user must check the PINTSMRY register to find out the pipe which can
        cause an interrupt.
        A PERR error occurs if one of the error field in the STATUS_PIPE register in the Host pipe descriptor is
        set and the Error Count field in STATUS_PIPE (STATUS_PIPE.ERCNT) exceeds the maximum allowed
        number of Pipe error(s) as defined in Pipe Error Max Number field in CTRL_PIPE
        (CTRL_PIPE.PERMAX). Refer to section 38.8.7.7 STATUS_PIPE register.
        If one of the error field in the STATUS_PIPE register from the Host Pipe Descriptor is set and the
        STATUS_PIPE.ERCNT is less than the CTRL_PIPE.PERMAX, the STATUS_PIPE.ERCNT is
        incremented.

38.6.3.16 Link Power Management L1 (LPM-L1) Suspend State Entry and Exit as Host.
        An EXTENDED LPM transaction can be transmitted by any enabled pipe. The PCFGn.PTYPE should be
        set to EXTENDED. Other fields as PCFG.PTOKEN, PCFG.BK and PCKSIZE.SIZE are irrelevant in this
        configuration. The user should also set the EXTREG.VARIABLE in the descriptor as described in
        38.8.7.4 EXTREG register.
        When the pipe is configured and enabled, an EXTENDED TOKEN followed by a LPM TOKEN are
        transmitted. The device responds with a valid HANDSHAKE, corrupted HANDSHAKE or no
        HANDSHAKE (TIME-OUT).
        If the valid HANDSHAKE is an ACK, the host will immediately proceed to L1 SLEEP and the
        PINTFLAG.TRCT0 is set. The minimum duration of the L1 SLEEP state will be the
        TL1RetryAndResidency as defined in the reference document "ENGINEERING CHANGE NOTICE, USB
        2.0 Link Power Management Addendum". When entering the L1 SLEEP state, the CTRLB.SOFE is
        cleared, avoiding Start-of-Frame generation.
        If the valid HANDSHAKE is a NYET PINTFLAG.TRFAIL is set.
        If the valid HANDSHAKE is a STALL the PINTFLAG.STALL is set.
        If there is no HANDSHAKE or corrupted HANDSHAKE, the EXTENDED/LPM pair of TOKENS will be
        transmitted again until reaching the maximum number of retries as defined by the CTRL_PIPE.PERMAX
        in the pipe descriptor.
        If the last retry returns no valid HANDSHAKE, the PINTFLAGn.PERR is set, and the STATUS_BK is
        updated in the pipe descriptor.
        All LPM transactions, should they end up with a ACK, a NYET, a STALL or a PERR, will set the
        PSTATUS.PFREEZE bit, freezing the pipe before a succeeding operation. The user should unfreeze the
        pipe to start a new LPM transaction.
        To exit the L1 STATE, the user initiate a DOWNSTREAM RESUME by setting the bit CTRLB.RESUME or
        a L1 RESUME by setting the Send L1 Resume bit in CTRLB (CTRLB.L1RESUME). In the case of a L1
        RESUME, the K STATE duration is given by the BESL bit field in the EXTREG.VARIABLE field. See
        38.8.7.4 EXTREG.
        When the host is in the L1 SLEEP state after a successful LPM transmitted, the device can initiate an
        UPSTREAM RESUME. This will set the Upstream Resume Interrupt bit in INTFLAG (INTFLAG.UPRSM).
        The host should proceed then to a L1 RESUME as described above.




        © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1129
                                               SAM D5x/E5x Family Data Sheet
                                                                     USB – Universal Serial Bus

After resuming from the L1 SLEEP state, the bit CTRLB.SOFE is set, allowing Start-of-Frame generation.




© 2019 Microchip Technology Inc.                 Datasheet                        DS60001507E-page 1130
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                              USB – Universal Serial Bus

38.6.3.17 Host Interrupt
         Figure 38-10. Host Interrupt
                    PINTFLAG7.STALL

                                                 PINTENSET.STALL
                   PINTFLAG7.PERR

                                                PINTENSET.PERR

                    PINTFLAG7.TRFAIL

                                                                          PINTSMRY
                                                 PINTENSET.TRFAIL

          PIPE7    PINTFLAG7.TXSTP                                         PINT7

                                                PINTENSET.TXSTP            PINT6
                   PINTFLAG7.TRCPT1

                                                 PINTENSET.TRCPT1

                    PINTFLAG7.TRCPT0

                                                 PINTENSET.TRCPT0

                                                                                                        USB PIPE
                                                                                                         Interrupt


                    PINTFLAG0.STALL

                                                 PINTENSET.STALL
                   PINTFLAG0.PERR

                                                PINTENSET.PERR

                    PINTFLAG0.TRFAIL

                                               PINTENSET.TRFAIL            PINT1

                   PINTFLAG0.TXSTP                                         PINT0

           PIPE0                               PINTENSET.TXSTP

                   PINTFLAG0.TRCPT1

                                               PINTENSET.TRCPT1

                   PINTFLAG0.TRCPT0
                                                                                                                             USB
                                               PINTENSET.TRCPT0                                                            Interrupt




                     INTFLAG.DDISC *

                                                 INTENSET.DDISC

                     INTFLAG.DCONN *

                                                 INTENSET.DCONN

                     INTFLAG.RAMACER

         INTFLAGA                                INTENSET.RAMACER

                     INTFLAG.UPRSM
                                                                                   USB Host Interrupt
                                                 INTENSET.UPRSM

                     INTFLAG.DNRSM

                                                 INTENSET.DNRSM

                     INTFLAG.WAKEUP *

                                                 INTENSET.WAKEUP

                     INTFLAG.RST

                                                 INTENSET.RST

                     INTFLAG.HSOF

                                                 INTENSET.HSOF



                    * Asynchronous interrupt

         The WAKEUP is an asynchronous interrupt and can be used to wake-up the device from any sleep mode.




         © 2019 Microchip Technology Inc.                           Datasheet                                    DS60001507E-page 1131
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                             USB – Universal Serial Bus


38.7      Register Summary
          The register mapping depends on the Operating Mode field in the Control A register (CTRLA.MODE).
          The register summary is detailed below.

38.7.1    Common Device Summary

 Offset        Name        Bit Pos.

  0x00        CTRLA           7:0      MODE                                                        RUNSTBY       ENABLE       SWRST
  0x01       Reserved
  0x02      SYNCBUSY          7:0                                                                                ENABLE       SWRST
  0x03       QOSCTRL          7:0                                                           DQOS[1:0]                  CQOS[1:0]
  0x0D      FSMSTATUS         7:0                                                 FSMSTATE[6:0]
  0x24                        7:0                                           DESCADD[7:0]
  0x25                       15:8                                          DESCADD[15:8]
             DESCADD
  0x26                       23:16                                         DESCADD[23:16]
  0x27                       31:24                                         DESCADD[31:24]
  0x28                        7:0            TRANSN[1:0]                                          TRANSP[4:0]
              PADCAL
  0x29                       15:8                            TRIM[2:0]                                          TRANSN[4:2]


38.7.2    Device Summary

Table 38-1. General Device Registers
 Offset        Name        Bit Pos.

  0x04       Reserved
  0x05       Reserved
  0x06       Reserved
  0x07       Reserved
  0x08                        7:0                                        NREPLY         SPDCONF[1:0]              UPRSM       DETACH
              CTRLB
  0x09                       15:8                                                       LPMHDSK[1:0]              GNAK
  0x0A         DADD                    ADDEN                                        DADD[6:0]
  0x0B       Reserved
  0x0C        STATUS          7:0        LINESTATE[1:0]                                    SPEED[1:0]
  0x0E       Reserved
  0x0F       Reserved
  0x10                        7:0                            FNUM[4:0]
               FNUM
  0x11                       15:8     FNCERR                                               FNUM[10:5]
  0x12       Reserved
  0x14                        7:0     RAMACER        UPRSM    EORSM      WAKEUP      EORST           SOF                      SUSPEND
             INTENCLR
  0x15                       15:8                                                                                LPMSUSP      LPMNYET
  0x16       Reserved
  0x17       Reserved
  0x18                        7:0     RAMACER        UPRSM    EORSM      WAKEUP      EORST           SOF                      SUSPEND
             INTENSET
  0x19                       15:8                                                                                LPMSUSP      LPMNYET
  0x1A       Reserved
  0x1B       Reserved




          © 2019 Microchip Technology Inc.                            Datasheet                                 DS60001507E-page 1132
                                                                            SAM D5x/E5x Family Data Sheet
                                                                                                        USB – Universal Serial Bus

...........continued

  Offset                Name    Bit Pos.

   0x1C                           7:0      RAMACER      UPRSM         EORSM         WAKEUP       EORST          SOF                     SUSPEND
                   INTFLAG
   0x1D                          15:8                                                                                     LPMSUSP       LPMNYET
   0x1E            Reserved
   0x1F            Reserved
   0x20                           7:0                                                    EPINT[7:0]
                 EPINTSMRY
   0x21                          15:8                                                    EPINT[15:8]
   0x22            Reserved
   0x23            Reserved


Table 38-2. Device Endpoint Register n
  Offset                Name    Bit Pos.

  0x1m0                EPCFGn     7:0                               EPTYPE1[1:0]                                         EPTYPE0[1:0]
  0x1m1            Reserved
  0x1m2            Reserved
  0x1m3            Reserved
  0x1m4        EPSTATUSCLRn       7:0       BK1RDY      BK0RDY       STALLRQ1      STALLRQ0                    CURBK       DTGLIN       DTGLOUT
  0x1m5        EPSTATUSSETn       7:0       BK1RDY      BK0RDY       STALLRQ1      STALLRQ0                    CURBK       DTGLIN       DTGLOUT
  0x1m6           EPSTATUSn       7:0       BK1RDY      BK0RDY       STALLRQ1      STALLRQ0                    CURBK       DTGLIN       DTGLOUT
  0x1m7          EPINTFLAGn       7:0                   STALL1        STALL0        RXSTP        TRFAIL1       TRFAIL0     TRCPT1       TRCPT0
  0x1m8         EPINTENCLRn       7:0                   STALL1        STALL0        RXSTP        TRFAIL1       TRFAIL0     TRCPT1       TRCPT0
  0x1m9         EPINTENSETn       7:0                   STALL1        STALL0        RXSTP        TRFAIL1       TRFAIL0     TRCPT1       TRCPT0
  0x1mA            Reserved
  0x1mB            Reserved


Table 38-3. Device Endpoint n Descriptor Bank 0
 Offset 0x              Name    Bit Pos.
    n0 +
   index

   0x00                           7:0                                                     ADD[7:0]
   0x01                          15:8                                                    ADD[15:8]
                       ADDR
   0x02                          23:16                                                   ADD[23:16]
   0x03                          31:24                                                   ADD[31:24]
   0x04                           7:0                                                 BYTE_COUNT[7:0]
   0x05                          15:8      MULTI_PACKET_SIZE[1:0]                                 BYTE_COUNT[13:8]
                   PCKSIZE
   0x06                          23:16                                             MULTI_PACKET_SIZE[9:2]
   0x07                          31:24     AUTO_ZLP                   SIZE[2:0]                             MULTI_PACKET_SIZE[13:10]
   0x08                           7:0                      VARIABLE[3:0]                                           SUBPID[3:0]
                       EXTREG
   0x09                          15:8                                                         VARIABLE[10:4]
   0x0A           STATUS_BK       7:0                                                                                    ERRORFLOW      CRCERR
   0x0B            Reserved       7:0
   0x0C            Reserved       7:0
   0x0D            Reserved       7:0
   0x0E            Reserved       7:0
   0x0F            Reserved       7:0




              © 2019 Microchip Technology Inc.                                 Datasheet                                 DS60001507E-page 1133
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                     USB – Universal Serial Bus

Table 38-4. Device Endpoint n Descriptor Bank 1
Offset 0x        Name        Bit Pos.
   n0
 + 0x10 +
  index

  0x00                          7:0                                                 ADD[7:0]
  0x01                         15:8                                                ADD[15:8]
                 ADDR
  0x02                         23:16                                               ADD[23:16]
  0x03                         31:24                                               ADD[31:24]
  0x04                          7:0                                             BYTE_COUNT[7:0]
  0x05                         15:8     MULTI_PACKET_SIZE[1:0]                             BYTE_COUNT[13:8]
               PCKSIZE
  0x06                         23:16                                         MULTI_PACKET_SIZE[9:2]
  0x07                         31:24    AUTO_ZLP                 SIZE[2:0]                             MULTI_PACKET_SIZE[13:10]
  0x08         Reserved         7:0
  0x09         Reserved        15:8
  0x0A        STATUS_BK         7:0                                                                                 ERRORFLOW     CRCERR
  0x0B         Reserved         7:0
  0x0C         Reserved         7:0
  0x0D         Reserved         7:0
  0x0E         Reserved         7:0
  0x0F         Reserved         7:0


38.7.3      Host Summary

Table 38-5. General Host Registers
  Offset         Name        Bit Pos.

  0x04         Reserved
  0x05         Reserved
  0x06         Reserved
  0x07         Reserved
  0x08                          7:0                   TSTK         TSTJ                         SPDCONF[1:0]          RESUME
                CTRLB
  0x09                         15:8                                                      L1RESUME        VBUSOK      BUSRESET      SOFE
  0x0A          HSOFC           7:0      FLENCE                                                                FLENC[3:0]
  0x0B         Reserved
  0x0C          STATUS          7:0         LINESTATE[1:0]                                       SPEED[1:0]
  0x0E         Reserved
  0x0F         Reserved
  0x10                          7:0                              FNUM[4:0]
                 FNUM
  0x11                         15:8                                                              FNUM[10:5]
  0x12         FLENHIGH         7:0                                              FLENHIGH[7:0]
  0x14                          7:0     RAMACER      UPRSM        DNRSM       WAKEUP           RST        HSOF
               INTENCLR
  0x15                         15:8                                                                                    DDISC      DCONN
  0x16         Reserved
  0x17         Reserved
  0x18                          7:0     RAMACER      UPRSM        DNRSM       WAKEUP           RST        HSOF
               INTENSET
  0x19                         15:8                                                                                    DDISC      DCONN




            © 2019 Microchip Technology Inc.                              Datasheet                                 DS60001507E-page 1134
                                                                           SAM D5x/E5x Family Data Sheet
                                                                                                         USB – Universal Serial Bus

...........continued

  Offset                Name    Bit Pos.

   0x1A            Reserved
   0x1B            Reserved
   0x1C                           7:0      RAMACER      UPRSM       DNRSM        WAKEUP            RST         HSOF
                   INTFLAG
   0x1D                          15:8                                                                                      DDISC        DCONN
   0x1E            Reserved
   0x1F            Reserved
   0x20                           7:0                                                  PINT[7:0]
                  PINTSMRY
   0x21                          15:8                                                 PINT[15:8]
   0x22            Reserved
   0x23


Table 38-6. Host Pipe Register n
  Offset                Name    Bit Pos.

  0x1m0                PCFGn      7:0                                           PTYPE[2:0]                      BK              PTOKEN[1:0]
  0x1m1            Reserved
  0x1m2            Reserved
  0x1m3           BINTERVAL       7:0                                               BINTERVAL[7:0]
  0x1m4         PSTATUSCLRn       7:0       BK1RDY      BK0RDY                  PFREEZE                       CURBK                      DTGL
  0x1m5          PSTATUSETn       7:0       BK1RDY      BK0RDY                  PFREEZE                       CURBK                      DTGL
  0x1m6           PSTATUSn        7:0       BK1RDY      BK0RDY                  PFREEZE                       CURBK                      DTGL
  0x1m7           PINTFLAGn       7:0                                STALL        TXSTP          PERR         TRFAIL      TRCPT1       TRCPT0
  0x1m8          PINTENCLRn       7:0                                STALL        TXSTP          PERR         TRFAIL      TRCPT1       TRCPT0
  0x1m9          PINTENSETn       7:0                                STALL        TXSTP          PERR         TRFAIL      TRCPT1       TRCPT0
  0x1mA            Reserved
  0x1mB            Reserved


Table 38-7. Host Pipe n Descriptor Bank 0
 Offset 0x              Name    Bit Pos.
    n0 +
   index

   0x00                           7:0                                                  ADD[7:0]
   0x01                          15:8                                                 ADD[15:8]
                       ADDR
   0x02                          23:16                                                ADD[23:16]
   0x03                          31:24                                                ADD[31:24]
   0x04                           7:0                                              BYTE_COUNT[7:0]
   0x05                          15:8      MULTI_PACKET_SIZE[1:0]                                BYTE_COUNT[13:8]
                   PCKSIZE
   0x06                          23:16                                          MULTI_PACKET_SIZE[9:2]
   0x07                          31:24     AUTO_ZLP                 SIZE[2:0]                               MULTI_PACKET_SIZE[13:10]
   0x08                           7:0                      VARIABLE[3:0]                                          SUBPID[3:0]
                       EXTREG
   0x09                          15:8                                                        VARIABLE[10:4]
   0x0A           STATUS_BK       7:0                                                                                   ERRORFLOW      CRCERR
   0x0B                          15:8
   0x0C                           7:0                                                         PDADDR[6:0]
                  CTRL_PIPE
   0x0D                          15:8                       PEPMAX[3:0]                                           PEPNUM[3:0]




              © 2019 Microchip Technology Inc.                               Datasheet                                  DS60001507E-page 1135
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                                   USB – Universal Serial Bus

...........continued

 Offset 0x             Name    Bit Pos.
    n0 +
   index

   0x0E                           7:0                ERCNT[2:0]               CRC16ER      TOUTER         PIDER     DAPIDER       DTGLER
                STATUS_PIPE
   0x0F                          15:8


Table 38-8. Host Pipe n Descriptor Bank 1
 Offset 0x             Name    Bit Pos.
 n0 +0x10
  +index

   0x00                           7:0                                                ADD[7:0]
   0x01                          15:8                                               ADD[15:8]
                       ADDR
   0x02                          23:16                                              ADD[23:16]
   0x03                          31:24                                              ADD[31:24]
   0x04                           7:0                                            BYTE_COUNT[7:0]
   0x05                          15:8     MULTI_PACKET_SIZE[1:0                             BYTE_COUNT[13:8]
                   PCKSIZE
   0x06                          23:16                                        MULTI_PACKET_SIZE[9:2]
   0x07                          31:24    AUTO_ZLP                SIZE[2:0]                            MULTI_PACKET_SIZE[13:10]
   0x08                           7:0
   0x09                          15:8
   0x0A           STATUS_BK       7:0                                                                              ERRORFLOW      CRCERR
   0x0B                          15:8
   0x0C                           7:0
   0x0D                          15:8
   0x0E                           7:0                ERCNT[2:0]               CRC16ER      TOUTER         PIDER     DAPIDER       DTGLER
                STATUS_PIPE
   0x0F                          15:8




38.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16-, and 32-bit accesses are supported. In addition,
               the 8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers require synchronization when read and/or written. Synchronization is denoted by the
               "Read-Synchronized" and/or "Write-Synchronized" property in each individual register description.
               Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
               Protection" property in each individual register description.
               Some registers are enable-protected, meaning they can only be written when the module is disabled.
               Enable protection is denoted by the "Enable-Protected" property in each individual register description.
               Refer to the 38.5.8 Register Access Protection, PAC - Peripheral Access Controller and GCLK
               Synchronization for details.
               Related Links
               27. PAC - Peripheral Access Controller

38.8.1         Communication Device Host Registers




              © 2019 Microchip Technology Inc.                            Datasheet                                DS60001507E-page 1136
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                          USB – Universal Serial Bus

38.8.1.1 Control A

            Name:        CTRLA
            Offset:      0x00
            Reset:       0x00
            Property:    PAC Write-Protection, Write-Synchronised


      Bit         7              6             5              4             3              2             1              0
                MODE                                                                  RUNSTDBY        ENABLE         SWRST
   Access        R/W                                                                     R/W            R/W            R/W
    Reset         0                                                                        0             0              0


            Bit 7 – MODE Operating Mode
            This bit defines the operating mode of the USB.
             Value       Description
             0           USB Device mode
             1           USB Host mode

            Bit 2 – RUNSTDBY Run in Standby Mode
            This bit is Enable-Protected.
             Value       Description
             0           USB clock is stopped in standby mode.
             1           USB clock is running in standby mode

            Bit 1 – ENABLE Enable
            Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
            disabled. The value written to CTRLA.ENABLE will read back immediately and the Synchronization status
            enable bit in the Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE
            will be cleared when the operation is complete.
            This bit is Write-Synchronized.
             Value       Description
             0           The peripheral is disabled or being disabled.
             1           The peripheral is enabled or being enabled.

            Bit 0 – SWRST Software Reset
            Writing a zero to this bit has no effect.
            Writing a '1' to this bit resets all registers in the USB, to their initial state, and the USB will be disabled.
            Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
            write-operation will be discarded.
            Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
            CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
            This bit is Write-Synchronized.
             Value        Description
             0            There is no reset operation ongoing.
             1            The reset operation is ongoing.




        © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1137
                                                            SAM D5x/E5x Family Data Sheet
                                                                                 USB – Universal Serial Bus

38.8.1.2 Synchronization Busy

            Name:       SYNCBUSY
            Offset:     0x02
            Reset:      0x00
            Property:   -


      Bit        7             6           5            4            3            2            1            0
                                                                                            ENABLE       SWRST
  Access                                                                                       R            R
   Reset                                                                                       0            0


            Bit 1 – ENABLE Synchronization Enable status bit
            This bit is cleared when the synchronization of ENABLE register between the clock domains is complete.
            This bit is set when the synchronization of ENABLE register between clock domains is started.

            Bit 0 – SWRST Synchronization Software Reset status bit
            This bit is cleared when the synchronization of SWRST register between the clock domains is complete.
            This bit is set when the synchronization of SWRST register between clock domains is started.




        © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1138
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       USB – Universal Serial Bus

38.8.1.3 QOS Control

            Name:       QOSCTRL
            Offset:     0x03
            Reset:      0x0F
            Property:   PAC Write-Protection


      Bit         7            6            5            4             3                2        1                 0
                                                                           DQOS[1:0]                  CQOS[1:0]
  Access                                                             R/W               R/W      R/W               R/W
   Reset                                                               1                1        1                 1


            Bits 3:2 – DQOS[1:0] Data Quality of Service
            These bits define the memory priority access during the endpoint or pipe read/write data operation. Refer
            to SRAM Quality of Service.

            Bits 1:0 – CQOS[1:0] Configuration Quality of Service
            These bits define the memory priority access during the endpoint or pipe read/write configuration
            operation. Refer to SRAM Quality of Service.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1139
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.1.4 Finite State Machine Status

            Name:       FSMSTATUS
            Offset:     0x0D
            Reset:      0xXXXX
            Property:   Read only


      Bit         7            6            5            4            3            2            1               0
                                                                FSMSTATE[6:0]
   Access                      R            R            R            R            R            R               R
    Reset                      0            0            0            0            0            0               1


            Bits 6:0 – FSMSTATE[6:0] Fine State Machine Status
            These bits indicate the state of the finite state machine of the USB controller.
             Value      Name                Description
             0x01       OFF (L3)            Corresponds to the powered-off, disconnected, and disabled state.
             0x02       ON (L0)             Corresponds to the Idle and Active states.
             0x04       SUSPEND (L2)
             0x08       SLEEP (L1)
             0x10       DNRESUME            Down Stream Resume.
             0x20       UPRESUME            Up Stream Resume.
             0x40       RESET               USB lines Reset.
             Others                         Reserved




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1140
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.1.5 Descriptor Address

            Name:       DESCADD
            Offset:     0x24
            Reset:      0x00000000
            Property:   PAC Write-Protection


      Bit        31           30           29            28           27           26           25           24
                                                         DESCADD[31:24]
  Access        R/W          R/W           R/W          R/W          R/W          R/W          R/W          R/W
    Reset         0            0            0            0            0            0             0            0


      Bit        23           22           21            20           19           18           17           16
                                                         DESCADD[23:16]
  Access        R/W          R/W           R/W          R/W          R/W          R/W          R/W          R/W
    Reset         0            0            0            0            0            0             0            0


      Bit        15           14           13            12           11           10            9            8
                                                         DESCADD[15:8]
  Access        R/W          R/W           R/W          R/W          R/W          R/W          R/W          R/W
    Reset         0            0            0            0            0            0             0            0


      Bit         7            6            5            4            3            2             1            0
                                                          DESCADD[7:0]
  Access        R/W          R/W           R/W          R/W          R/W          R/W          R/W          R/W
    Reset         0            0            0            0            0            0             0            0


            Bits 31:0 – DESCADD[31:0] Descriptor Address Value
            These bits define the base address of the main USB descriptor in RAM. The two least significant bits
            must be written to zero.




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1141
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.1.6 Pad Calibration

               Name:          PADCAL
               Offset:        0x28
               Reset:         0x0000
               Property:      PAC Write-Protection

               The Pad Calibration values must be loaded from the NVM Software Calibration Area into the USB Pad
               Calibration register by software, before enabling the USB, to achieve the specified accuracy.
               Refer to NVM Software Calibration Area Mapping for further details.
               Refer to for further details.

         Bit         15                 14        13         12           11        10            9            8
                                               TRIM[2:0]                                      TRANSN[4:2]
   Access                           R/W          R/W        R/W                    R/W           R/W          R/W
    Reset                               0         0          0                      0             0            0


         Bit         7                  6         5          4             3        2             1            0
                          TRANSN[1:0]                                           TRANSP[4:0]
   Access           R/W             R/W                     R/W           R/W      R/W           R/W          R/W
    Reset            0                  0                    0             0        0             0            0


               Bits 14:12 – TRIM[2:0] Trim bits for DP/DM
               These bits calibrate the matching of rise/fall of DP/DM.

               Bits 10:6 – TRANSN[4:0] Trimmable Output Driver Impedance N
               These bits calibrate the NMOS output impedance of DP/DM drivers.

               Bits 4:0 – TRANSP[4:0] Trimmable Output Driver Impedance P
               These bits calibrate the PMOS output impedance of DP/DM drivers.

38.8.2         Device Registers - Common




           © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1142
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.2.1 Control B

            Name:       CTRLB
            Offset:     0x08
            Reset:      0x0000
            Property:   PAC Write-Protection


      Bit        15           14           13            12           11           10            9            8
                                                                       LPMHDSK[1:0]            GNAK
   Access                                                            R/W          R/W           R/W
    Reset                                                             0             0            0


      Bit         7            6            5            4            3             2            1            0
                                                      NREPLY           SPDCONF[1:0]           UPRSM        DETACH
   Access                                                R           R/W          R/W           R/W          R/W
    Reset                                                0            0             0            0            0


            Bits 11:10 – LPMHDSK[1:0] Link Power Management Handshake
            These bits select the Link Power Management Handshake configuration.
             Value      Description
             0x0        No handshake. LPM is not supported.
             0x1        ACK
             0x2        NYET
             0x3        Reserved

            Bit 9 – GNAK Global NAK
            This bit configures the operating mode of the NAK.
            This bit is not synchronized.
             Value       Description
             0           The handshake packet reports the status of the USB transaction
             1           A NAK handshake is answered for each USB transaction regardless of the current endpoint
                         memory bank status

            Bit 4 – NREPLY No reply excepted SETUP Token
            This bit is cleared by hardware when receiving a SETUP packet.
            This bit has no effect for any other endpoint but endpoint 0.
             Value        Description
             0            Disable the “NO_REPLY” feature: Any transaction to endpoint 0 will be handled according to
                          the USB2.0 standard.
             1            Enable the “NO_REPLY” feature: Any transaction to endpoint 0 will be ignored except
                          SETUP.

            Bits 3:2 – SPDCONF[1:0] Speed Configuration
            These bits select the speed configuration.
             Value      Description
             0x0        FS: Full-speed
             0x1        LS: Low-speed
             0x2        Reserved




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1143
                                                  SAM D5x/E5x Family Data Sheet
                                                                         USB – Universal Serial Bus

 Value        Description
 0x3          Reserved

Bit 1 – UPRSM Upstream Resume
This bit is cleared when the USB receives a USB reset or once the upstream resume has been sent.
 Value        Description
 0            Writing a zero to this bit has no effect.
 1            Writing a one to this bit will generate an upstream resume to the host for a remote wakeup.

Bit 0 – DETACH Detach
Value      Description
0          The device is attached to the USB bus so that communications may occur.
1          It is the default value at reset. The internal device pull-ups are disabled, removing the device
           from the USB bus.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1144
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.2.2 Device Address

            Name:       DADD
            Offset:     0x0A
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6             5            4            3             2            1             0
               ADDEN                                                DADD[6:0]
  Access        R/W           R/W          R/W           R/W          R/W           R/W          R/W          R/W
   Reset          0            0             0            0            0             0            0             0


            Bit 7 – ADDEN Device Address Enable
            This bit is cleared when a USB reset is received.
             Value        Description
             0            Writing a zero will deactivate the DADD field (USB device address) and return the device to
                          default address 0.
             1            Writing a one will activate the DADD field (USB device address).

            Bits 6:0 – DADD[6:0] Device Address
            These bits define the device address. The DADD register is reset when a USB reset is received.




        © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1145
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        USB – Universal Serial Bus

38.8.2.3 Status

            Name:       STATUS
            Offset:     0x0C
            Reset:      0x40
            Property:   -


      Bit         7            6            5            4            3                  2        1            0
                  LINESTATE[1:0]                                           SPEED[1:0]
   Access         R            R                                     R/W                R/W
    Reset         0            1                                      0                  1


            Bits 7:6 – LINESTATE[1:0] USB Line State Status
            These bits define the current line state DP/DM.

            LINESTATE[1:0]                                    USB Line Status
            0x0                                               SE0/RESET
            0x1                                               FS-J or LS-K State
            0x2                                               FS-K or LS-J State

            Bits 3:2 – SPEED[1:0] Speed Status
            These bits define the current speed used of the device
            .

            SPEED[1:0]                                   SPEED STATUS
            0x0                                          Low-speed mode
            0x1                                          Full-speed mode
            0x2                                          Reserved
            0x3                                          Reserved




        © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1146
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       USB – Universal Serial Bus

38.8.2.4 Device Frame Number

            Name:       FNUM
            Offset:     0x10
            Reset:      0x0000
            Property:   Read only


      Bit        15           14              13        12           11                10         9           8
              FNCERR                                                      FNUM[10:5]
  Access        R/W                          R/W       R/W          R/W            R/W           R/W         R/W
   Reset          0                           0          0            0                0          0           0


      Bit         7            6              5          4            3                2          1           0
                                           FNUM[4:0]                                         MFNUM[2:0]
  Access        R/W          R/W             R/W       R/W          R/W            R/W           R/W         R/W
   Reset          0            0              0          0            0                0          0           0


            Bit 15 – FNCERR Frame Number CRC Error
            This bit is cleared upon receiving a USB reset.
            This bit is set when a corrupted frame number (or micro-frame number) is received.
            This bit and the SOF (or MSOF) interrupt bit are updated at the same time.

            Bits 13:3 – FNUM[10:0] Frame Number
            These bits are cleared upon receiving a USB reset.
            These bits are updated with the frame number information as provided from the last SOF packet even if a
            corrupted SOF is received.

            Bits 2:0 – MFNUM[2:0] Micro Frame Number
            These bits are cleared upon receiving a USB reset or at the beginning of each Start-of-Frame (SOF
            interrupt).
            These bits are updated with the micro-frame number information as provided from the last MSOF packet
            even if a corrupted MSOF is received.




        © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1147
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.2.5 Device Interrupt Enable Clear

            Name:       INTENCLR
            Offset:     0x14
            Reset:      0x0000
            Property:   PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

      Bit        15            14           13            12           11           10            9             8
                                                                                              LPMSUSP       LPMNYET
   Access                                                                                        R/W           R/W
    Reset                                                                                         0             0


      Bit         7            6             5            4            3             2            1             0
              RAMACER       UPRSM          EORSM       WAKEUP        EORST          SOF                     SUSPEND
   Access       R/W           R/W           R/W          R/W          R/W           R/W                        R/W
    Reset         0            0             0            0            0             0                          0


            Bit 9 – LPMSUSP Link Power Management Suspend Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Link Power Management Suspend Interrupt Enable bit and disable
            the corresponding interrupt request.
             Value      Description
             0          The Link Power Management Suspend interrupt is disabled.
             1          The Link Power Management Suspend interrupt is enabled and an interrupt request will be
                        generated when the Link Power Management Suspend interrupt Flag is set.

            Bit 8 – LPMNYET Link Power Management Not Yet Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Link Power Management Not Yet interrupt Enable bit and disable the
            corresponding interrupt request.
             Value      Description
             0          The Link Power Management Not Yet interrupt is disabled.
             1          The Link Power Management Not Yet interrupt is enabled and an interrupt request will be
                        generated when the Link Power Management Not Yet interrupt Flag is set.

            Bit 7 – RAMACER RAM Access Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the RAM Access interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The RAM Access interrupt is disabled.
             1           The RAM Access interrupt is enabled and an interrupt request will be generated when the
                         RAM Access interrupt Flag is set.

            Bit 6 – UPRSM Upstream Resume Interrupt Enable
            Writing a zero to this bit has no effect.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1148
                                                   SAM D5x/E5x Family Data Sheet
                                                                          USB – Universal Serial Bus

Writing a one to this bit will clear the Upstream Resume interrupt Enable bit and disable the
corresponding interrupt request.
 Value      Description
 0          The Upstream Resume interrupt is disabled.
 1          The Upstream Resume interrupt is enabled and an interrupt request will be generated when
            the Upstream Resume interrupt Flag is set.

Bit 5 – EORSM End Of Resume Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the End Of Resume interrupt Enable bit and disable the corresponding
interrupt request.
 Value       Description
 0           The End Of Resume interrupt is disabled.
 1           The End Of Resume interrupt is enabled and an interrupt request will be generated when the
             End Of Resume interrupt Flag is set.

Bit 4 – WAKEUP Wake-Up Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Wake Up interrupt Enable bit and disable the corresponding interrupt
request.
 Value      Description
 0          The Wake Up interrupt is disabled.
 1          The Wake Up interrupt is enabled and an interrupt request will be generated when the Wake
            Up interrupt Flag is set.

Bit 3 – EORST End of Reset Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the End of Reset interrupt Enable bit and disable the corresponding
interrupt request.
 Value       Description
 0           The End of Reset interrupt is disabled.
 1           The End of Reset interrupt is enabled and an interrupt request will be generated when the
             End of Reset interrupt Flag is set.

Bit 2 – SOF Start-of-Frame Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Start-of-Frame interrupt Enable bit and disable the corresponding
interrupt request.
 Value       Description
 0           The Start-of-Frame interrupt is disabled.
 1           The Start-of-Frame interrupt is enabled and an interrupt request will be generated when the
             Start-of-Frame interrupt Flag is set.

Bit 0 – SUSPEND Suspend Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Suspend Interrupt Enable bit and disable the corresponding interrupt
request.
 Value      Description
 0          The Suspend interrupt is disabled.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1149
                                                  SAM D5x/E5x Family Data Sheet
                                                                        USB – Universal Serial Bus

 Value        Description
 1            The Suspend interrupt is enabled and an interrupt request will be generated when the
              Suspend interrupt Flag is set.




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1150
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.2.6 Device Interrupt Enable Set

            Name:       INTENSET
            Offset:     0x18
            Reset:      0x0000
            Property:   PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

      Bit        15            14           13            12           11           10            9               8
                                                                                               LPMSUSP      LPMNYET
   Access                                                                                        R/W            R/W
    Reset                                                                                         0               0


      Bit         7            6             5            4             3            2            1               0
              RAMACER       UPRSM          EORSM       WAKEUP        EORST          SOF                     SUSPEND
   Access       R/W           R/W           R/W          R/W          R/W           R/W                         R/W
    Reset         0            0             0            0             0            0                            0


            Bit 9 – LPMSUSP Link Power Management Suspend Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the Link Power Management Suspend Enable bit and enable the
            corresponding interrupt request.
             Value      Description
             0          The Link Power Management Suspend interrupt is disabled.
             1          The Link Power Management Suspend interrupt is enabled.

            Bit 8 – LPMNYET Link Power Management Not Yet Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the Link Power Management Not Yet interrupt bit and enable the
            corresponding interrupt request.
             Value      Description
             0          The Link Power Management Not Yet interrupt is disabled.
             1          The Link Power Management Not Yet interrupt is enabled.

            Bit 7 – RAMACER RAM Access Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the RAM Access Enable bit and enable the corresponding interrupt
            request.
             Value      Description
             0          The RAM Access interrupt is disabled.
             1          The RAM Access interrupt is enabled.

            Bit 6 – UPRSM Upstream Resume Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the Upstream Resume Enable bit and enable the corresponding interrupt
            request.
             Value      Description
             0          The Upstream Resume interrupt is disabled.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1151
                                                   SAM D5x/E5x Family Data Sheet
                                                                         USB – Universal Serial Bus

 Value        Description
 1            The Upstream Resume interrupt is enabled.

Bit 5 – EORSM End Of Resume Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the End Of Resume interrupt Enable bit and enable the corresponding
interrupt request.
 Value       Description
 0           The End Of Resume interrupt is disabled.
 1           The End Of Resume interrupt is enabled.

Bit 4 – WAKEUP Wake-Up Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Wake Up interrupt Enable bit and enable the corresponding interrupt
request.
 Value      Description
 0          The Wake Up interrupt is disabled.
 1          The Wake Up interrupt is enabled.

Bit 3 – EORST End of Reset Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the End of Reset interrupt Enable bit and enable the corresponding
interrupt request.
 Value       Description
 0           The End of Reset interrupt is disabled.
 1           The End of Reset interrupt is enabled.

Bit 2 – SOF Start-of-Frame Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Start-of-Frame interrupt Enable bit and enable the corresponding
interrupt request.
 Value       Description
 0           The Start-of-Frame interrupt is disabled.
 1           The Start-of-Frame interrupt is enabled.

Bit 0 – SUSPEND Suspend Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Suspend interrupt Enable bit and enable the corresponding interrupt
request.
 Value      Description
 0          The Suspend interrupt is disabled.
 1          The Suspend interrupt is enabled.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1152
                                                               SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.2.7 Device Interrupt Flag Status and Clear

            Name:       INTFLAG
            Offset:     0x01C
            Reset:      0x0000
            Property:   -


      Bit        15            14           13            12           11            10            9               8
                                                                                               LPMSUSP      LPMNYET
   Access                                                                                        R/W              R/W
    Reset                                                                                          0               0


      Bit         7            6             5            4             3            2             1               0
              RAMACER       UPRSM          EORSM       WAKEUP        EORST          SOF                     SUSPEND
   Access       R/W           R/W           R/W          R/W          R/W           R/W                           R/W
    Reset         0            0             0            0             0            0                             0


            Bit 9 – LPMSUSP Link Power Management Suspend Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the USB module acknowledge a Link Power Management Transaction (ACK
            handshake) and has entered the Suspended state and will generate an interrupt if INTENCLR/
            SET.LPMSUSP is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the LPMSUSP Interrupt Flag.

            Bit 8 – LPMNYET Link Power Management Not Yet Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the USB module acknowledges a Link Power Management Transaction (handshake
            is NYET) and will generate an interrupt if INTENCLR/SET.LPMNYET is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the LPMNYET Interrupt Flag.

            Bit 7 – RAMACER RAM Access Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a RAM access underflow error occurs during IN data stage. This bit will generate an
            interrupt if INTENCLR/SET.RAMACER is one.
            Writing a zero to this bit has no effect.

            Bit 6 – UPRSM Upstream Resume Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the USB sends a resume signal called “Upstream Resume” and will generate an
            interrupt if INTENCLR/SET.UPRSM is one.
            Writing a zero to this bit has no effect.

            Bit 5 – EORSM End Of Resume Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the USB detects a valid “End of Resume” signal initiated by the host and will
            generate an interrupt if INTENCLR/SET.EORSM is one.
            Writing a zero to this bit has no effect.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1153
                                                   SAM D5x/E5x Family Data Sheet
                                                                          USB – Universal Serial Bus

Bit 4 – WAKEUP Wake Up Interrupt Flag
This flag is cleared by writing a one to the flag.
This flag is set when the USB is reactivated by a filtered non-idle signal from the lines and will generate
an interrupt if INTENCLR/SET.WAKEUP is one.
Writing a zero to this bit has no effect.

Bit 3 – EORST End of Reset Interrupt Flag
This flag is cleared by writing a one to the flag.
This flag is set when a USB “End of Reset” has been detected and will generate an interrupt if
INTENCLR/SET.EORST is one.
Writing a zero to this bit has no effect.

Bit 2 – SOF Start-of-Frame Interrupt Flag
This flag is cleared by writing a one to the flag.
This flag is set when a USB “Start-of-Frame” has been detected (every 1 ms) and will generate an
interrupt if INTENCLR/SET.SOF is one.
The FNUM is updated. In High Speed mode, the MFNUM register is cleared.
Writing a zero to this bit has no effect.

Bit 0 – SUSPEND Suspend Interrupt Flag
This flag is cleared by writing a one to the flag.
This flag is set when a USB “Suspend” idle state has been detected for 3 frame periods (J state for 3 ms)
and will generate an interrupt if INTENCLR/SET.SUSPEND is one.
Writing a zero to this bit has no effect.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1154
                                                                SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.2.8 Endpoint Interrupt Summary

               Name:       EPINTSMRY
               Offset:     0x20
               Reset:      0x0000
               Property:   -


         Bit        15           14           13          12                 11     10           9            8
                                                               EPINT[15:8]
   Access           R             R           R            R                 R      R            R            R
    Reset           0             0           0            0                 0      0            0            0


         Bit        7             6           5            4                 3      2            1            0
                                                               EPINT[7:0]
   Access           R             R           R            R                 R      R            R            R
    Reset           0             0           0            0                 0      0            0            0


               Bits 15:0 – EPINT[15:0] EndPoint Interrupt
               The flag EPINT[n] is set when an interrupt is triggered by the EndPoint n. See 38.8.3.5 EPINTFLAGn
               register in the device EndPoint section.
               This bit will be cleared when no interrupts are pending for EndPoint n.

38.8.3         Device Registers - Endpoint




           © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1155
                                                                SAM D5x/E5x Family Data Sheet
                                                                              USB – Universal Serial Bus

38.8.3.1 Device Endpoint Configuration register n

            Name:       EPCFGn
            Offset:     0x100 + (n x 0x20)
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit        7             6                5          4          3         2          1            0
                                           EPTYPE1[2:0]                               EPTYPE0[2:0]
   Access                    R/W               R/W        R/W                R/W          R/W          R/W
    Reset                      0                0          0                    0          0            0


            Bits 6:4 – EPTYPE1[2:0] Endpoint Type for IN direction
            These bits contains the endpoint type for IN direction.
            Upon receiving a USB reset EPCFGn.EPTYPE1 is cleared except for endpoint 0 which is unchanged.
             Value      Description
             0x0        Bank1 is disabled.
             0x1        Bank1 is enabled and configured as Control IN.
             0x2        Bank1 is enabled and configured as Isochronous IN.
             0x3        Bank1 is enabled and configured as Bulk IN.
             0x4        Bank1 is enabled and configured as Interrupt IN.
             0x5        Bank1 is enabled and configured as Dual-Bank OUT
                    (Endpoint type is the same as the one defined in EPTYPE0)
            0x6-0x7 Reserved

            Bits 2:0 – EPTYPE0[2:0] Endpoint Type for OUT direction
            These bits contains the endpoint type for OUT direction.
            Upon receiving a USB reset EPCFGn.EPTYPE0 is cleared except for endpoint 0 which is unchanged.
             Value      Description
             0x0        Bank0 is disabled.
             0x1        Bank0 is enabled and configured as Control SETUP / Control OUT.
             0x2        Bank0 is enabled and configured as Isochronous OUT.
             0x3        Bank0 is enabled and configured as Bulk OUT.
             0x4        Bank0 is enabled and configured as Interrupt OUT.
             0x5        Bank0 is enabled and configured as Dual Bank IN
                    (Endpoint type is the same as the one defined in EPTYPE1)
            0x6-0x7 Reserved




        © 2019 Microchip Technology Inc.                        Datasheet                  DS60001507E-page 1156
                                                             SAM D5x/E5x Family Data Sheet
                                                                              USB – Universal Serial Bus

38.8.3.2 EndPoint Status Clear n

            Name:       EPSTATUSCLRn
            Offset:     0x104 + (n * 0x20)
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6              5          4              3      2        1            0
              BK1RDY        BK0RDY         STALLRQ1   STALLRQ0               CURBK    DTGLIN     DTGLOUT
   Access        W            W               W          W                    W         W            W
    Reset         0            0              0          0                     0        0            0


            Bit 7 – BK1RDY Bank 1 Ready Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear EPSTATUS.BK1RDY bit.

            Bit 6 – BK0RDY Bank 0 Ready Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear EPSTATUS.BK0RDY bit.

            Bit 5 – STALLRQ1 STALL bank 1 Request Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear EPSTATUS.STALLRQ1 bit.

            Bit 4 – STALLRQ0 STALL bank 0 Request Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear EPSTATUS.STALLRQ0 bit.

            Bit 2 – CURBK Current Bank Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear EPSTATUS.CURBK bit.

            Bit 1 – DTGLIN Data Toggle IN Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear EPSTATUS.DTGLIN bit.

            Bit 0 – DTGLOUT Data Toggle OUT Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the EPSTATUS.DTGLOUT bit.




        © 2019 Microchip Technology Inc.                         Datasheet              DS60001507E-page 1157
                                                             SAM D5x/E5x Family Data Sheet
                                                                              USB – Universal Serial Bus

38.8.3.3 EndPoint Status Set n

            Name:       EPSTATUSSETn
            Offset:     0x105 + (n x 0x20)
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6              5          4              3      2        1            0
              BK1RDY        BK0RDY         STALLRQ1   STALLRQ0               CURBK    DTGLIN     DTGLOUT
   Access        W            W               W          W                    W         W            W
    Reset         0            0              0          0                     0        0            0


            Bit 7 – BK1RDY Bank 1 Ready Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set EPSTATUS.BK1RDY bit.

            Bit 6 – BK0RDY Bank 0 Ready Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set EPSTATUS.BK0RDY bit.

            Bit 5 – STALLRQ1 STALL Request bank 1 Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set EPSTATUS.STALLRQ1 bit.

            Bit 4 – STALLRQ0 STALL Request bank 0 Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set EPSTATUS.STALLRQ0 bit.

            Bit 2 – CURBK Current Bank Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set EPSTATUS.CURBK bit.

            Bit 1 – DTGLIN Data Toggle IN Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set EPSTATUS.DTGLIN bit.

            Bit 0 – DTGLOUT Data Toggle OUT Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the EPSTATUS.DTGLOUT bit.




        © 2019 Microchip Technology Inc.                         Datasheet              DS60001507E-page 1158
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     USB – Universal Serial Bus

38.8.3.4 EndPoint Status n

            Name:        EPSTATUSn
            Offset:      0x106 + (n x 0x20)
            Reset:       0x00
            Property:    PAC Write-Protection


      Bit         7            6             5             4            3             2             1            0
               BK1RDY       BK0RDY                     STALLRQ                     CURBK         DTGLIN      DTGLOUT
   Access         R            R                           R                          R            R             R
    Reset         0            0                           2                          0             0            0


            Bit 7 – BK1RDY Bank 1 is ready
            For Control/OUT direction Endpoints, the bank is empty.
            Writing a one to the bit EPSTATUSCLR.BK1RDY will clear this bit.
            Writing a one to the bit EPSTATUSSET.BK1RDY will set this bit.
             Value      Description
             0          The bank number 1 is not ready : For IN direction Endpoints, the bank is not yet filled in.
             1          The bank number 1 is ready: For IN direction Endpoints, the bank is filled in. For
                        Control/OUT direction Endpoints, the bank is full.

            Bit 6 – BK0RDY Bank 0 is ready
            Writing a one to the bit EPSTATUSCLR.BK0RDY will clear this bit.
            Writing a one to the bit EPSTATUSSET.BK0RDY will set this bit.
            Value       Description
            0           The bank number 0 is not ready : For IN direction Endpoints, the bank is not yet filled in. For
                        Control/OUT direction Endpoints, the bank is empty.
            1           The bank number 0 is ready: For IN direction Endpoints, the bank is filled in. For
                        Control/OUT direction Endpoints, the bank is full.

            Bit 4 – STALLRQ STALL bank x request
            Writing a zero to the bit EPSTATUSCLR.STALLRQ will clear this bit.
            Writing a one to the bit EPSTATUSSET.STALLRQ will set this bit.
            This bit is cleared by hardware when receiving a SETUP packet.
             Value        Description
             0            Disable STALLRQx feature.
             1            Enable STALLRQx feature: a STALL handshake will be sent to the host in regards to bank x.

            Bit 2 – CURBK Current Bank
            Writing a zero to the bit EPSTATUSCLR.CURBK will clear this bit.
            Writing a one to the bit EPSTATUSSET.CURBK will set this bit.
            Value       Description
            0           The bank0 is the bank that will be used in the next single/multi USB packet.
            1           The bank1 is the bank that will be used in the next single/multi USB packet.

            Bit 1 – DTGLIN Data Toggle IN Sequence
            Writing a zero to the bit EPSTATUSCLR.DTGLINCLR will clear this bit.
            Writing a one to the bit EPSTATUSSET.DTGLINSET will set this bit.




        © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1159
                                                   SAM D5x/E5x Family Data Sheet
                                                                          USB – Universal Serial Bus

 Value        Description
 0            The PID of the next expected IN transaction will be zero: data 0.
 1            The PID of the next expected IN transaction will be one: data 1.

Bit 0 – DTGLOUT Data Toggle OUT Sequence
Writing a zero to the bit EPSTATUSCLR.DTGLOUTCLR will clear this bit.
Writing a one to the bit EPSTATUSSET.DTGLOUTSET will set this bit.
Value       Description
0           The PID of the next expected OUT transaction will be zero: data 0.
1           The PID of the next expected OUR transaction will be one: data 1.




© 2019 Microchip Technology Inc.                     Datasheet                      DS60001507E-page 1160
                                                              SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

38.8.3.5 Device EndPoint Interrupt Flag n

            Name:       EPINTFLAGn
            Offset:     0x107 + (n x 0x20)
            Reset:      0x00
            Property:   -


      Bit        7             6             5          4            3            2            1            0
                                           STALL      RXSTP                     TRFAIL                    TRCPT
   Access                                  R/W         R/W                       R/W                       R/W
    Reset                                    0          0                         0                         0


            Bit 5 – STALL Transmit Stall x Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a Transmit Stall occurs and will generate an interrupt if EPINTENCLR/SET.STALL is
            one.
            EPINTFLAG.STALL is set for a single bank OUT endpoint or double bank IN/OUT endpoint when current
            bank is "0".
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the STALL Interrupt Flag.

            Bit 4 – RXSTP Received Setup Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a Received Setup occurs and will generate an interrupt if EPINTENCLR/SET.RXSTP
            is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the RXSTP Interrupt Flag.

            Bit 2 – TRFAIL Transfer Fail x Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a transfer fail occurs and will generate an interrupt if EPINTENCLR/SET.TRFAIL is
            one.
            EPINTFLAG.TRFAIL is set for a single bank OUT endpoint or double bank IN/OUT endpoint when current
            bank is "0".
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the TRFAIL Interrupt Flag.

            Bit 0 – TRCPT Transfer Complete x interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a Transfer complete occurs and will generate an interrupt if EPINTENCLR/
            SET.TRCPT is one. EPINTFLAG.TRCPT is set for a single bank OUT endpoint or double bank IN/OUT
            endpoint when current bank is "0".
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the TRCPT0 Interrupt Flag.




        © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1161
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

38.8.3.6 Device EndPoint Interrupt Enable n

            Name:        EPINTENCLRn
            Offset:      0x108 + (n x 0x20)
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Endpoint Interrupt Enable Set (EPINTENSET) register.

      Bit         7             6             5            4             3             2             1            0
                                           STALL         RXSTP                      TRFAIL                      TRCPT
   Access                                   R/W           R/W                         R/W                        R/W
    Reset                                     0            0                           0                          0


            Bit 5 – STALL Transmit STALL x Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Transmit Stall x Interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The Transmit Stall x interrupt is disabled.
             1           The Transmit Stall x interrupt is enabled and an interrupt request will be generated when the
                         Transmit Stall x Interrupt Flag is set.

            Bit 4 – RXSTP Received Setup Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Received Setup Interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The Received Setup interrupt is disabled.
             1           The Received Setup interrupt is enabled and an interrupt request will be generated when the
                         Received Setup Interrupt Flag is set.

            Bit 2 – TRFAIL Transfer Fail x Interrupt Enable
            The user should look into the descriptor table status located in ram to be informed about the error
            condition : ERRORFLOW, CRC.
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Transfer Fail x Interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The Transfer Fail bank x interrupt is disabled.
             1           The Transfer Fail bank x interrupt is enabled and an interrupt request will be generated when
                         the Transfer Fail x Interrupt Flag is set.

            Bit 0 – TRCPT Transfer Complete x interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Transfer Complete x interrupt Enable bit and disable the
            corresponding interrupt request.
             Value      Description
             0          The Transfer Complete bank x interrupt is disabled.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1162
                                                   SAM D5x/E5x Family Data Sheet
                                                                        USB – Universal Serial Bus

 Value        Description
 1            The Transfer Complete bank x interrupt is enabled and an interrupt request will be generated
              when the Transfer Complete x Interrupt Flag is set.




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1163
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                          USB – Universal Serial Bus

38.8.3.7 Device Interrupt EndPoint Set n

            Name:        EPINTENSETn
            Offset:      0x109 + (n x 0x20)
            Reset:       0x0000
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Endpoint Interrupt Enable Set (EPINTENCLR) register. This
            register is cleared by USB reset or when EPEN[n] is zero.

      Bit         7              6             5             4              3              2        1            0
                                            STALL          RXSTP                         TRFAIL                TRCPT
   Access                                     R/W           R/W                           R/W                   R/W
    Reset                                      0             0                             0                     0


            Bit 5 – STALL Transmit Stall x Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Transmit bank x Stall interrupt.
            Value       Description
            0           The Transmit Stall x interrupt is disabled.
            1           The Transmit Stall x interrupt is enabled.

            Bit 4 – RXSTP Received Setup Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Received Setup interrupt.
            Value       Description
            0           The Received Setup interrupt is disabled.
            1           The Received Setup interrupt is enabled.

            Bit 2 – TRFAIL Transfer Fail bank x Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Transfer Fail interrupt.
            Value       Description
            0           The Transfer Fail interrupt is disabled.
            1           The Transfer Fail interrupt is enabled.

            Bit 0 – TRCPT Transfer Complete bank x interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Transfer Complete x interrupt.
            0.2.4 Device Registers - Endpoint RAM
             Value      Description
             0          The Transfer Complete bank x interrupt is disabled.
             1          The Transfer Complete bank x interrupt is enabled.




        © 2019 Microchip Technology Inc.                           Datasheet                        DS60001507E-page 1164
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                                              USB – Universal Serial Bus

38.8.4   Device Registers - Endpoint RAM

38.8.4.1 Endpoint Descriptor Structure

                                              Data Buffers


                                                 EPn BK1




                                                 EPn BK0




                                               Endpoint
                                              descriptors



                                                 Reserved
                                                STATUS_BK

                                      Bank1      Reserved
                      Descriptor En




                                                 PCKSIZE
                                                  ADDR
                                                            (2 x 0xn0) + 0x10
                                                 Reserved
                                                STATUS_BK

                                      Bank0      EXTREG
                                                 PCKSIZE
                                                                                   Growing Memory Addresses




                                                  ADDR      2 x 0xn0




                                                 Reserved   +0x01B
                                                STATUS_BK   +0x01A
                                      Bank1      Reserved   +0x018
                      Descriptor E0




                                                 PCKSIZE    +0x014
                                                  ADDR      +0x010
                                                 Reserved   +0x00B
                                      Bank0
                                                STATUS_BK   +0x00A
                                                 EXTREG     +0x008
                                                 PCKSIZE    +0x004
                                                  ADDR      +0x000          DESCADD




         © 2019 Microchip Technology Inc.                              Datasheet                                        DS60001507E-page 1165
                                                              SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

38.8.4.2 Address of Data Buffer

            Name:       ADDR
            Offset:     0x00 & 0x10
            Reset:      0xxxxxxxx
            Property:   NA


      Bit        31           30           29           28                 27     26           25            24
                                                             ADDR[31:24]
   Access       R/W          R/W           R/W         R/W                R/W     R/W          R/W          R/W
    Reset         x            x            x            x                 x       x            x            x


      Bit        23           22           21           20                 19     18           17            16
                                                             ADDR[23:16]
   Access       R/W          R/W           R/W         R/W                R/W     R/W          R/W          R/W
    Reset         x            x            x            x                 x       x            x            x


      Bit        15           14           13           12                 11     10            9            8
                                                             ADDR[15:8]
   Access       R/W          R/W           R/W         R/W                R/W     R/W          R/W          R/W
    Reset         x            x            x            x                 x       x            x            x


      Bit         7            6            5            4                 3       2            1            0
                                                              ADDR[7:0]
   Access       R/W          R/W           R/W         R/W                R/W     R/W          R/W          R/W
    Reset         x            x            x            x                 x       x            x            x


            Bits 31:0 – ADDR[31:0] Data Pointer Address Value
            These bits define the data pointer address as an absolute word address in RAM. The two least significant
            bits must be zero to ensure the start address is 32-bit aligned.




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1166
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                         USB – Universal Serial Bus

38.8.4.3 Packet Size

            Name:       PCKSIZE
            Offset:     0x04 & 0x14
            Reset:      0xxxxxxxxx
            Property:   NA


      Bit         31          30              29                 28         27           26           25           24
             AUTO_ZLP                      SIZE[2:0]                                 MULTI_PACKET_SIZE[13:10]
   Access         R/W        R/W             R/W                R/W         R/W         R/W          R/W          R/W
    Reset          x           0              0                  x           0           0             0           0


      Bit         23          22              21                 20         19           18           17           16
                                                           MULTI_PACKET_SIZE[9:2]
   Access         R/W        R/W             R/W                R/W         R/W         R/W          R/W          R/W
    Reset          0           0              0                  0           0           0             0           0


      Bit         15          14              13                 12         11           10            9           8
              MULTI_PACKET_SIZE[1:0]                                        BYTE_COUNT[13:8]
   Access         R/W        R/W             R/W                R/W         R/W         R/W          R/W          R/W
    Reset          0           x              0                  0           0           0             0           0


      Bit          7           6              5                  4           3           2             1           0
                                                                BYTE_COUNT[7:0]
   Access         R/W        R/W             R/W                R/W         R/W         R/W          R/W          R/W
    Reset          0           0              0                  0           0           0             0           x


            Bit 31 – AUTO_ZLP Automatic Zero Length Packet
            This bit defines the automatic Zero Length Packet mode of the endpoint.
            When enabled, the USB module will manage the ZLP handshake by hardware. This bit is for IN endpoints
            only. When disabled the handshake should be managed by firmware.
             Value       Description
             0           Automatic Zero Length Packet is disabled.
             1           Automatic Zero Length Packet is enabled.

            Bits 30:28 – SIZE[2:0] Endpoint size
            These bits contains the maximum packet size of the endpoint.

            Value                                      Description
            0x0                                        8 Byte
            0x1                                        16 Byte
            0x2                                        32 Byte
            0x3                                        64 Byte
            0x4                                        128 Byte(1)
            0x5                                        256 Byte(1)




        © 2019 Microchip Technology Inc.                              Datasheet                       DS60001507E-page 1167
                                                     SAM D5x/E5x Family Data Sheet
                                                                    USB – Universal Serial Bus

...........continued
 Value                                 Description
 0x6                                   512 Byte(1)
 0x7                                   1023 Byte(1)

 (1) for Isochronous endpoints only.

Bits 27:14 – MULTI_PACKET_SIZE[13:0] Multiple Packet Size
These bits define the 14-bit value that is used for multi-packet transfers.
For IN endpoints, MULTI_PACKET_SIZE holds the total number of bytes sent. MULTI_PACKET_SIZE
should be written to zero when setting up a new transfer.
For OUT endpoints, MULTI_PACKET_SIZE holds the total data size for the complete transfer. This value
must be a multiple of the maximum packet size.

Bits 13:0 – BYTE_COUNT[13:0] Byte Count
These bits define the 14-bit value that is used for the byte count.
For IN endpoints, BYTE_COUNT holds the number of bytes to be sent in the next IN transaction.
For OUT endpoint or SETUP endpoints, BYTE_COUNT holds the number of bytes received upon the last
OUT or SETUP transaction.




© 2019 Microchip Technology Inc.                      Datasheet                  DS60001507E-page 1168
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.4.4 Extended Register

            Name:        EXTREG
            Offset:      0x08
            Reset:       0xxxxxxxx
            Property:    NA


      Bit         15          14               13           12           11         10                 9            8
                                                                   VARIABLE[10:4]
  Access                      R/W             R/W           R/W         R/W         R/W            R/W             R/W
    Reset                      0               0             0           0           0                 0            0


      Bit          7           6               5             4           3           2                 1            0
                                VARIABLE[3:0]                                            SUBPID[3:0]
  Access          R/W         R/W             R/W           R/W         R/W         R/W            R/W             R/W
    Reset          0           0               0             x           0           0                 0            x


            Bits 14:4 – VARIABLE[10:0] Variable field send with extended token
            These bits define the VARIABLE field of a received extended token. These bits are updated when the
            USB has answered by an handshake token ACK to a LPM transaction. See Section 2.1.1 Protocol
            Extension Token in the reference document “ENGINEERING CHANGE NOTICE, USB 2.0 Link Power
            Management Addendum”.
            To support the USB2.0 Link Power Management addition the VARIABLE field should be read as
            described below.

            VARIABLES                      Description
            VARIABLE[3:0]                  bLinkState (1)
            VARIABLE[7:4]                  BESL (2)
            VARIABLE[8]                    bRemoteWake (1)
            VARIABLE[10:9]                 Reserved

             1.    For a definition of LPM Token bRemoteWake and bLinkState fields, refer to "Table 2-3 in the
                   reference document ENGINEERING CHANGE NOTICE, USB 2.0 Link Power Management
                   Addendum".
             2.    For a definition of LPM Token BESL field, refer to "Table 2-3 in the reference document
                   ENGINEERING CHANGE NOTICE, USB 2.0 Link Power Management Addendum" and "Table X-
                   X1 in Errata for ECN USB 2.0 Link Power Management.

            Bits 3:0 – SUBPID[3:0] SUBPID field send with extended token
            These bits define the SUBPID field of a received extended token. These bits are updated when the USB
            has answered by an handshake token ACK to a LPM transaction. See Section 2.1.1 Protocol Extension
            Token in the reference document “ENGINEERING CHANGE NOTICE, USB 2.0 Link Power Management
            Addendum”.




        © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 1169
                                                               SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.4.5 Device Status Bank

               Name:       STATUS_BK
               Offset:     0x0A & 0x1A
               Reset:      0xxxxxxxx
               Property:   NA


         Bit        7             6           5            4           3            2            1            0
                                                                                            ERRORFLOW      CRCERR
   Access                                                                                       R/W          R/W
    Reset                                                                                        x            x


               Bit 1 – ERRORFLOW Error Flow Status
               This bit defines the Error Flow Status.
               This bit is set when a Error Flow has been detected during transfer from/towards this bank.
               For OUT transfer, a NAK handshake has been sent.
               For Isochronous OUT transfer, an overrun condition has occurred.
               For IN transfer, this bit is not valid. EPSTATUS.TRFAIL0 and EPSTATUS.TRFAIL1 should reflect the flow
               errors.
                Value        Description
                0            No Error Flow detected.
                1            A Error Flow has been detected.

               Bit 0 – CRCERR CRC Error
               This bit defines the CRC Error Status.
               This bit is set when a CRC error has been detected in an isochronous OUT endpoint bank.
               0.2.5 Host Registers - Common
                Value        Description
                0            No CRC Error.
                1            CRC Error detected.

38.8.5         Host Registers - Common




           © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1170
                                                             SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

38.8.5.1 Control B

            Name:       CTRLB
            Offset:     0x08
            Reset:      0x0000
            Property:   PAC Write-Protection


      Bit        15           14           13           12            11           10           9            8
                                                                  L1RESUME      VBUSOK      BUSRESET       SOFE
   Access                                                            R/W          R/W          R/W          R/W
    Reset                                                             0            0            0            0


      Bit         7            6            5            4            3            2            1            0
                                                                       SPDCONF[1:0]          RESUME
   Access                                                            R/W          R/W          R/W
    Reset                                                             0            0            0


            Bit 11 – L1RESUME Send USB L1 Resume
            Writing 0 to this bit has no effect.
            1: Generates a USB L1 Resume on the USB bus. This bit should only be set when the Start-of-Frame
            generation is enabled (SOFE bit set). The duration of the USB L1 Resume is defined by the
            EXTREG.VARIABLE[7:4] bits field also known as BESL (See LPM ECN).See also 38.8.7.4 EXTREG
            Register.
            This bit is cleared when the USB L1 Resume has been sent or when a USB reset is requested.

            Bit 10 – VBUSOK VBUS is OK
            This notifies the USB HOST that USB operations can be started. When this bit is zero and even if the
            USB HOST is configured and enabled, HOST operation is halted. Setting this bit will allow HOST
            operation when the USB is configured and enabled.
             Value       Description
             0           The USB module is notified that the VBUS on the USB line is not powered.
             1           The USB module is notified that the VBUS on the USB line is powered.

            Bit 9 – BUSRESET Send USB Reset
            Value      Description
            0          Reset generation is disabled. It is written to zero when the USB reset is completed or when a
                       device disconnection is detected. Writing zero has no effect.
            1          Generates a USB Reset on the USB bus.

            Bit 8 – SOFE Start-of-Frame Generation Enable
            Value      Description
            0          The SOF generation is disabled and the USB bus is in suspend state.
            1          Generates SOF on the USB bus in full speed and keep it alive in low speed mode. This bit is
                       automatically set at the end of a USB reset (INTFLAG.RST) or at the end of a downstream
                       resume (INTFLAG.DNRSM) or at the end of L1 resume.

            Bits 3:2 – SPDCONF[1:0] Speed Configuration for Host
            These bits select the host speed configuration as shown below




        © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1171
                                              SAM D5x/E5x Family Data Sheet
                                                                   USB – Universal Serial Bus

 Value        Description
 0x0          Low and Full Speed capable
 0x1          Reserved
 0x2          Reserved
 0x3          Reserved

Bit 1 – RESUME Send USB Resume
Writing 0 to this bit has no effect.
1: Generates a USB Resume on the USB bus.
This bit is cleared when the USB Resume has been sent or when a USB reset is requested.




© 2019 Microchip Technology Inc.                Datasheet                       DS60001507E-page 1172
                                                               SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

38.8.5.2 Host Start-of-Frame Control

            Name:        HSOFC
            Offset:      0x0A
            Reset:       0x00
            Property:    PAC Write-Protection

            During a very short period just before transmitting a Start-of-Frame, this register is locked. Thus, after
            writing, it is recommended to check the register value, and write this register again if necessary. This
            register is cleared upon a USB reset.

      Bit         7             6             5            4             3             2                  1           0
               FLENCE                                                                       FLENC[3:0]
   Access        R/W                                                    R/W           R/W                R/W         R/W
    Reset         0                                                      0             0                  0           0


            Bit 7 – FLENCE Frame Length Control Enable
            When this bit is '1', the time between Start-of-Frames can be tuned by up to +/-0.06% using FLENC[3:0].
            Note: In Low Speed mode, FLENCE must be '0'.
            Value       Description
            0           Start-of-Frame is generated every 1ms.
            1           Start-of-Frame generation depends on the signed value of FLENC[3:0].
                        USB Start-of-Frame period equals 1ms + (FLENC[3:0]/12000)ms

            Bits 3:0 – FLENC[3:0] Frame Length Control
            These bits define the signed value of the 4-bit FLENC that is added to the Internal Frame Length when
            FLENCE is '1'. The internal Frame length is the top value of the frame counter when FLENCE is zero.




        © 2019 Microchip Technology Inc.                         Datasheet                               DS60001507E-page 1173
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       USB – Universal Serial Bus

38.8.5.3 Status

            Name:       STATUS
            Offset:     0x0C
            Reset:      0x00
            Property:   Read only


      Bit         7            6            5            4           3                  2        1            0
                  LINESTATE[1:0]                                          SPEED[1:0]
   Access         R            R                                    R/W                R/W
    Reset         0            0                                     0                  0


            Bits 7:6 – LINESTATE[1:0] USB Line State Status
            These bits define the current line state DP/DM.

            LINESTATE[1:0]                                    USB Line Status
            0x0                                               SE0/RESET
            0x1                                               FS-J or LS-K State
            0x2                                               FS-K or LS-J State

            Bits 3:2 – SPEED[1:0] Speed Status
            These bits define the current speed used by the host.

            SPEED[1:0]                                   Speed Status
            0x0                                          Full-speed mode
            0x1                                          Low-speed mode
            0x2                                          Reserved
            0x3                                          Reserved




        © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1174
                                                             SAM D5x/E5x Family Data Sheet
                                                                                       USB – Universal Serial Bus

38.8.5.4 Host Frame Number

            Name:       FNUM
            Offset:     0x10
            Reset:      0x0000
            Property:   PAC Write-Protection


      Bit        15           14              13        12           11                10        9            8
                                                                          FNUM[10:5]
  Access                                     R/W       R/W          R/W            R/W          R/W          R/W
   Reset                                      0         0            0                 0         0            0


      Bit        7             6              5         4            3                 2         1            0
                                           FNUM[4:0]
  Access        R/W          R/W             R/W       R/W          R/W
   Reset         0             0              0         0            0


            Bits 13:3 – FNUM[10:0] Frame Number
            These bits contains the current SOF number.
            These bits can be written by software to initialize a new frame number value. In this case, at the next
            SOF, the FNUM field takes its new value.
            As the FNUM register lies across two consecutive byte addresses, writing byte-wise (8-bits) to the FNUM
            register may produce incorrect frame number generation. It is recommended to write FNUM register
            word-wise (32-bits) or half-word-wise (16-bits).




        © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1175
                                                               SAM D5x/E5x Family Data Sheet
                                                                                       USB – Universal Serial Bus

38.8.5.5 Host Frame Length

            Name:        FLENHIGH
            Offset:      0x12
            Reset:       0x00
            Property:    Read-Only


      Bit         7            6             5             4            3              2         1            0
                                                            FLENHIGH[7:0]
  Access          R            R             R             R            R              R         R            R
   Reset          0            0             0             0            0              0         0            0


            Bits 7:0 – FLENHIGH[7:0] Frame Length
            These bits contains the 8 high-order bits of the internal frame counter.
            Table 38-9. Counter Description vs. Speed

            Host Register Description
            STATUS.SPEED
            Full Speed         With a USB clock running at 12MHz, counter length is 12000 to ensure a SOF
                               generation every 1 ms.




        © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1176
                                                              SAM D5x/E5x Family Data Sheet
                                                                                    USB – Universal Serial Bus

38.8.5.6 Host Interrupt Enable Register Clear

            Name:       INTENCLR
            Offset:     0x14
            Reset:      0x0000
            Property:   PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

      Bit        15            14           13           12            11           10            9            8
                                                                                                DDISC       DCONN
   Access                                                                                        R/W          R/W
    Reset                                                                                         0            0


      Bit         7            6             5            4            3            2             1            0
              RAMACER       UPRSM          DNRSM      WAKEUP          RST         HSOF
   Access       R/W           R/W           R/W         R/W           R/W          R/W
    Reset         0            0             0            0            0            0


            Bit 9 – DDISC Device Disconnection Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Device Disconnection interrupt Enable bit and disable the
            corresponding interrupt request.
             Value      Description
             0          The Device Disconnection interrupt is disabled.
             1          The Device Disconnection interrupt is enabled and an interrupt request will be generated
                        when the Device Disconnection interrupt Flag is set.

            Bit 8 – DCONN Device Connection Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Device Connection interrupt Enable bit and disable the
            corresponding interrupt request.
             Value      Description
             0          The Device Connection interrupt is disabled.
             1          The Device Connection interrupt is enabled and an interrupt request will be generated when
                        the Device Connection interrupt Flag is set.

            Bit 7 – RAMACER RAM Access Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the RAM Access interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The RAM Access interrupt is disabled.
             1           The RAM Access interrupt is enabled and an interrupt request will be generated when the
                         RAM Access interrupt Flag is set.

            Bit 6 – UPRSM Upstream Resume from Device Interrupt Disable
            Writing a zero to this bit has no effect.




        © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1177
                                                   SAM D5x/E5x Family Data Sheet
                                                                         USB – Universal Serial Bus

Writing a one to this bit will clear the Upstream Resume interrupt Enable bit and disable the
corresponding interrupt request.
 Value      Description
 0          The Upstream Resume interrupt is disabled.
 1          The Upstream Resume interrupt is enabled and an interrupt request will be generated when
            the Upstream Resume interrupt Flag is set.

Bit 5 – DNRSM Down Resume Interrupt Disable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Down Resume interrupt Enable bit and disable the corresponding
interrupt request.
 Value       Description
 0           The Down Resume interrupt is disabled.
 1           The Down Resume interrupt is enabled and an interrupt request will be generated when the
             Down Resume interrupt Flag is set.

Bit 4 – WAKEUP Wake Up Interrupt Disable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Wake Up interrupt Enable bit and disable the corresponding interrupt
request.
 Value      Description
 0          The Wake Up interrupt is disabled.
 1          The Wake Up interrupt is enabled and an interrupt request will be generated when the Wake
            Up interrupt Flag is set.

Bit 3 – RST BUS Reset Interrupt Disable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Bus Reset interrupt Enable bit and disable the corresponding
interrupt request.
 Value       Description
 0           The Bus Reset interrupt is disabled.
 1           The Bus Reset interrupt is enabled and an interrupt request will be generated when the Bus
             Reset interrupt Flag is set.

Bit 2 – HSOF Host Start-of-Frame Interrupt Disable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Host Start-of-Frame interrupt Enable bit and disable the
corresponding interrupt request.
 Value      Description
 0          The Host Start-of-Frame interrupt is disabled.
 1          The Host Start-of-Frame interrupt is enabled and an interrupt request will be generated when
            the Host Start-of-Frame interrupt Flag is set.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1178
                                                                SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

38.8.5.7 Host Interrupt Enable Register Set

            Name:        INTENSET
            Offset:      0x18
            Reset:       0x0000
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

      Bit        15            14            13           12            11            10            9             8
                                                                                                  DDISC        DCONN
   Access                                                                                          R/W          R/W
    Reset                                                                                           0             0


      Bit         7             6            5             4             3            2             1             0
              RAMACER        UPRSM         DNRSM       WAKEUP          RST          HSOF
   Access        R/W          R/W           R/W           R/W          R/W           R/W
    Reset         0             0            0             0             0            0


            Bit 9 – DDISC Device Disconnection Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the Device Disconnection interrupt bit and enable the DDSIC interrupt.
            Value       Description
            0           The Device Disconnection interrupt is disabled.
            1           The Device Disconnection interrupt is enabled.

            Bit 8 – DCONN Device Connection Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the Device Connection interrupt bit and enable the DCONN interrupt.
            Value       Description
            0           The Device Connection interrupt is disabled.
            1           The Device Connection interrupt is enabled.

            Bit 7 – RAMACER RAM Access Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the RAM Access interrupt bit and enable the RAMACER interrupt.
            Value       Description
            0           The RAM Access interrupt is disabled.
            1           The RAM Access interrupt is enabled.

            Bit 6 – UPRSM Upstream Resume from the device Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the Upstream Resume interrupt bit and enable the UPRSM interrupt.
            Value       Description
            0           The Upstream Resume interrupt is disabled.
            1           The Upstream Resume interrupt is enabled.

            Bit 5 – DNRSM Down Resume Interrupt Enable
            Writing a zero to this bit has no effect.




        © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 1179
                                                   SAM D5x/E5x Family Data Sheet
                                                                         USB – Universal Serial Bus

Writing a one to this bit will set the Down Resume interrupt Enable bit and enable the DNRSM interrupt.
Value       Description
0           The Down Resume interrupt is disabled.
1           The Down Resume interrupt is enabled.

Bit 4 – WAKEUP Wake Up Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Wake Up interrupt Enable bit and enable the WAKEUP interrupt
request.
 Value      Description
 0          The WakeUp interrupt is disabled.
 1          The WakeUp interrupt is enabled.

Bit 3 – RST Bus Reset Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Bus Reset interrupt Enable bit and enable the Bus RST interrupt.
Value       Description
0           The Bus Reset interrupt is disabled.
1           The Bus Reset interrupt is enabled.

Bit 2 – HSOF Host Start-of-Frame Interrupt Enable
Writing a zero to this bit has no effect.
Writing a one to this bit will set the Host Start-of-Frame interrupt Enable bit and enable the HSOF
interrupt.
 Value      Description
 0          The Host Start-of-Frame interrupt is disabled.
 1          The Host Start-of-Frame interrupt is enabled.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1180
                                                              SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.5.8 Host Interrupt Flag Status and Clear

            Name:       INTFLAG
            Offset:     0x1C
            Reset:      0x0000
            Property:   -


      Bit        15           14            13          12            11           10           9             8
                                                                                              DDISC        DCONN
   Access                                                                                      R/W          R/W
    Reset                                                                                       0             0


      Bit         7            6             5           4            3            2            1             0
              RAMACER       UPRSM          DNRSM      WAKEUP         RST         HSOF
   Access       R/W          R/W            R/W         R/W          R/W          R/W
    Reset         0            0             0           0            0            0


            Bit 9 – DDISC Device Disconnection Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the device has been removed from the USB Bus and will generate an interrupt if
            INTENCLR/SET.DDISC is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the DDISC Interrupt Flag.

            Bit 8 – DCONN Device Connection Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a new device has been connected to the USB BUS and will generate an interrupt if
            INTENCLR/SET.DCONN is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the DCONN Interrupt Flag.

            Bit 7 – RAMACER RAM Access Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a RAM access error occurs during an OUT stage and will generate an interrupt if
            INTENCLR/SET.RAMACER is one.
            Writing a zero to this bit has no effect.

            Bit 6 – UPRSM Upstream Resume from the Device Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the USB has received an Upstream Resume signal from the Device and will
            generate an interrupt if INTENCLR/SET.UPRSM is one.
            Writing a zero to this bit has no effect.

            Bit 5 – DNRSM Down Resume Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when the USB has sent a Down Resume and will generate an interrupt if INTENCLR/
            SET.DRSM is one.
            Writing a zero to this bit has no effect.




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1181
                                                  SAM D5x/E5x Family Data Sheet
                                                                        USB – Universal Serial Bus

Bit 4 – WAKEUP Wake Up Interrupt Flag
This flag is cleared by writing a one.
This flag is set when:
l The host controller is in suspend mode (SOFE is zero) and an upstream resume from the device is
detected.
l The host controller is in suspend mode (SOFE is zero) and an device disconnection is detected.
l The host controller is in operational state (VBUSOK is one) and an device connection is detected.
In all cases it will generate an interrupt if INTENCLR/SET.WAKEUP is one.
Writing a zero to this bit has no effect.

Bit 3 – RST Bus Reset Interrupt Flag
This flag is cleared by writing a one to the flag.
This flag is set when a Bus “Reset” has been sent to the Device and will generate an interrupt if
INTENCLR/SET.RST is one.
Writing a zero to this bit has no effect.

Bit 2 – HSOF Host Start-of-Frame Interrupt Flag
This flag is cleared by writing a one to the flag.
This flag is set when a USB “Host Start-of-Frame” in Full Speed/High Speed or a keep-alive in Low
Speed has been sent (every 1 ms) and will generate an interrupt if INTENCLR/SET.HSOF is one.
The value of the FNUM register is updated.
Writing a zero to this bit has no effect.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1182
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

38.8.5.9 Pipe Interrupt Summary

               Name:       PINTSMRY
               Offset:     0x20
               Reset:      0x0000
               Property:   Read-only


         Bit        15           14            13           12                11      10            9            8
                                                                 PINT[15:8]
   Access           R             R            R            R                 R        R            R            R
    Reset            0            0            0            0                 0        0            0            0


         Bit         7            6            5            4                 3        2            1            0
                                                                 PINT[7:0]
   Access           R             R            R            R                 R        R            R            R
    Reset            0            0            0            0                 0        0            0            0


               Bits 15:0 – PINT[15:0]
               The flag PINT[n] is set when an interrupt is triggered by the pipe n. See 38.8.6.6 PINTFLAG register in
               the Host Pipe Register section.
               This bit will be cleared when there are no interrupts pending for Pipe n.
               Writing to this bit has no effect.

38.8.6         Host Registers - Pipe




           © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1183
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

38.8.6.1 Host Pipe n Configuration

            Name:        PCFGn
            Offset:      0x100 + (n x 0x20)
            Reset:       0x00
            Property:    PAC Write-Protection


      Bit         7             6               5            4              3         2             1                 0
                                                         PTYPE[2:0]                   BK                PTOKEN[1:0]
   Access                                      R/W          R/W            R/W       R/W           R/W            R/W
    Reset                                       0            0              0         0             0                 0


            Bits 5:3 – PTYPE[2:0] Type of the Pipe
            These bits contains the pipe type.

            PTYPE[2:0]              Description
            0x0                     Pipe is disabled
            0x1                     Pipe is enabled and configured as CONTROL
            0x2                     Pipe is enabled and configured as ISO
            0x3                     Pipe is enabled and configured as BULK
            0x4                     Pipe is enabled and configured as INTERRUPT
            0x5                     Pipe is enabled and configured as EXTENDED
            0x06-0x7                Reserved

            These bits are cleared upon sending a USB reset.

            Bit 2 – BK Pipe Bank
            This bit selects the number of banks for the pipe.
            For control endpoints writing a zero to this bit is required as only Bank0 is used for Setup/In/Out
            transactions.
            This bit is cleared when a USB reset is sent.

            BK(1)                          Description
            0x0                            Single-bank endpoint
            0x1                            Dual-bank endpoint

             1.   Bank field is ignored when PTYPE is configured as EXTENDED.
            Value       Description
            0           A single bank is used for the pipe.
            1           A dual bank is used for the pipe.

            Bits 1:0 – PTOKEN[1:0] Pipe Token
            These bits contains the pipe token.




        © 2019 Microchip Technology Inc.                              Datasheet                     DS60001507E-page 1184
                                               SAM D5x/E5x Family Data Sheet
                                                                   USB – Universal Serial Bus

 PTOKEN[1:0](1)                                         Description
 0x0                                                    SETUP(2)
 0x1                                                    IN
 0x2                                                    OUT
 0x3                                                    Reserved

  1.   PTOKEN field is ignored when PTYPE is configured as EXTENDED.
  2.   Available only when PTYPE is configured as CONTROL
Theses bits are cleared upon sending a USB reset.




© 2019 Microchip Technology Inc.                Datasheet                    DS60001507E-page 1185
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.6.2 Interval for the Bulk-Out/Ping Transaction

            Name:       BINTERVAL
            Offset:     0x103 + (n x 0x20)
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6             5              4            3         2             1             0
                                                            BINTERVAL[7:0]
   Access        R/W          R/W           R/W            R/W          R/W       R/W           R/W           R/W
    Reset         0            0             0              0            0         0             0             0


            Bits 7:0 – BINTERVAL[7:0] BINTERVAL
            These bits contains the Ping/Bulk-out period.
            These bits are cleared when a USB reset is sent or when PEN[n] is zero.

            BINTERVAL Description
            =0            Multiple consecutive OUT token is sent in the same frame until it is acked by the
                          peripheral
            >0            One OUT token is sent every BINTERVAL frame until it is acked by the peripheral

            Depending from the type of pipe the desired period is defined as:

            PTYPE                   Description
            Interrupt               1 ms to 255 ms
            Isochronous             2^(Binterval) * 1 ms
            Bulk or control         1 ms to 255 ms
            EXT LPM                 bInterval ignored. Always 1 ms when a NYET is received.




        © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1186
                                                              SAM D5x/E5x Family Data Sheet
                                                                             USB – Universal Serial Bus

38.8.6.3 Pipe Status Clear n

            Name:       PSTATUSCLR
            Offset:     0x104 + (n x 0x20)
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6            5             4             3     2        1            0
               BK1RDY       BK0RDY                    PFREEZE               CURBK                 DTGL
   Access        W             W                          W                  W                      W
    Reset         0            0                          0                   0                     0


            Bit 7 – BK1RDY Bank 1 Ready Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear PSTATUS.BK1RDY bit.

            Bit 6 – BK0RDY Bank 0 Ready Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear PSTATUS.BK0RDY bit.

            Bit 4 – PFREEZE Pipe Freeze Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear PSTATUS.PFREEZE bit.

            Bit 2 – CURBK Current Bank Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear PSTATUS.CURBK bit.

            Bit 0 – DTGL Data Toggle Clear
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear PSTATUS.DTGL bit.




        © 2019 Microchip Technology Inc.                        Datasheet              DS60001507E-page 1187
                                                              SAM D5x/E5x Family Data Sheet
                                                                              USB – Universal Serial Bus

38.8.6.4 Pipe Status Set Register n

            Name:       PSTATUSSET
            Offset:     0x105 + (n x 0x20)
            Reset:      0x00
            Property:   PAC Write-Protection


      Bit         7            6            5             4              3     2        1            0
               BK1RDY       BK0RDY                    PFREEZE                CURBK                 DTGL
   Access        W             W                         W                    W                      W
    Reset         0            0                          0                    0                     0


            Bit 7 – BK1RDY Bank 1 Ready Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the bit PSTATUS.BK1RDY.

            Bit 6 – BK0RDY Bank 0 Ready Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set the bit PSTATUS.BK0RDY.

            Bit 4 – PFREEZE Pipe Freeze Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set PSTATUS.PFREEZE bit.

            Bit 2 – CURBK Current Bank Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set PSTATUS.CURBK bit.

            Bit 0 – DTGL Data Toggle Set
            Writing a zero to this bit has no effect.
            Writing a one to this bit will set PSTATUS.DTGL bit.




        © 2019 Microchip Technology Inc.                        Datasheet               DS60001507E-page 1188
                                                               SAM D5x/E5x Family Data Sheet
                                                                                     USB – Universal Serial Bus

38.8.6.5 Pipe Status Register n

            Name:        PSTATUS
            Offset:      0x106 + (n x 0x20)
            Reset:       0x00
            Property:    PAC Write-Protection


      Bit         7            6             5             4            3             2            1             0
               BK1RDY       BK0RDY                     PFREEZE                     CURBK                       DTGL
   Access         R            R                          R                           R                          R
    Reset         0            0                           0                          0                          0


            Bit 7 – BK1RDY Bank 1 is ready
            Writing a one to the bit EPSTATUSCLR.BK1RDY will clear this bit.
            Writing a one to the bit EPSTATUSSET.BK1RDY will set this bit.
            This bank is not used for Control pipe.
             Value      Description
             0          The bank number 1 is not ready: For IN the bank is empty. For Control/OUT the bank is not
                        yet fill in.
             1          The bank number 1 is ready: For IN the bank is filled full. For Control/OUT the bank is filled
                        in.

            Bit 6 – BK0RDY Bank 0 is ready
            Writing a one to the bit EPSTATUSCLR.BK0RDY will clear this bit.
            Writing a one to the bit EPSTATUSSET.BK0RDY will set this bit.
            This bank is the only one used for Control pipe.
             Value      Description
             0          The bank number 0 is not ready: For IN the bank is not empty. For Control/OUT the bank is
                        not yet fill in.
             1          The bank number 0 is ready: For IN the bank is filled full. For Control/OUT the bank is filled
                        in.

            Bit 4 – PFREEZE Pipe Freeze
            Writing a one to the bit EPSTATUSCLR.PFREEZE will clear this bit.
            Writing a one to the bit EPSTATUSSET.PFREEZE will set this bit.
            This bit is also set by the hardware:
             • When a STALL handshake has been received.
             • After a PIPE has been enabled (rising of bit PEN.N).
             • When an LPM transaction has completed whatever handshake is returned or the transaction was
                 timed-out.
             • When a pipe transfer was completed with a pipe error. See 38.8.6.6 PINTFLAG register.
            When PFREEZE bit is set while a transaction is in progress on the USB bus, this transaction will be
            properly completed. PFREEZE bit will be read as “1” only when the ongoing transaction will have been
            completed.
             Value     Description
             0         The Pipe operates in normal operation.
             1         The Pipe is frozen and no additional requests will be sent to the device on this pipe address.




        © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1189
                                                  SAM D5x/E5x Family Data Sheet
                                                                         USB – Universal Serial Bus

Bit 2 – CURBK Current Bank
Value      Description
0          The bank0 is the bank that will be used in the next single/multi USB packet.
1          The bank1 is the bank that will be used in the next single/multi USB packet.

Bit 0 – DTGL Data Toggle Sequence
Writing a one to the bit EPSTATUSCLR.DTGL will clear this bit.
Writing a one to the bit EPSTATUSSET.DTGL will set this bit.
This bit is toggled automatically by hardware after a data transaction.
This bit will reflect the data toggle in regards of the token type (IN/OUT/SETUP).
 Value        Description
 0            The PID of the next expected transaction will be zero: data 0.
 1            The PID of the next expected transaction will be one: data 1.




© 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1190
                                                               SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

38.8.6.6 Host Pipe Interrupt Flag Register

            Name:       PINTFLAG
            Offset:     0x107 + (n x 0x20)
            Reset:      0x00
            Property:   -


      Bit         7            6             5           4            3            2            1             0
                                           STALL       TXSTP        PERR         TRFAIL                     TRCPT
   Access                                  R/W          R/W          R/W          R/W                        R/W
    Reset                                    0           0            0            0                          2


            Bit 5 – STALL STALL Received Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a stall occurs and will generate an interrupt if PINTENCLR/SET.STALL is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the STALL Interrupt Flag.

            Bit 4 – TXSTP Transmitted Setup Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a Transfer Complete occurs and will generate an interrupt if PINTENCLR/
            SET.TXSTP is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the TXSTP Interrupt Flag.

            Bit 3 – PERR Pipe Error Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a pipe error occurs and will generate an interrupt if PINTENCLR/SET.PERR is one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the PERR Interrupt Flag.

            Bit 2 – TRFAIL Transfer Fail Interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a Transfer Fail occurs and will generate an interrupt if PINTENCLR/SET.TRFAIL is
            one.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the TRFAIL Interrupt Flag.

            Bit 0 – TRCPT Transfer Complete x interrupt Flag
            This flag is cleared by writing a one to the flag.
            This flag is set when a Transfer complete occurs and will generate an interrupt if PINTENCLR/
            SET.TRCPT is one. PINTFLAG.TRCPT is set for a single bank IN/OUT pipe or a double bank IN/OUT
            pipe when current bank is 0.
            Writing a zero to this bit has no effect.
            Writing a one to this bit clears the TRCPT Interrupt Flag.




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1191
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                       USB – Universal Serial Bus

38.8.6.7 Host Pipe Interrupt Clear Register

            Name:        PINTENCLR
            Offset:      0x108 + (n x 0x20)
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Pipe Interrupt Enable Set (PINTENSET) register.
            This register is cleared by USB reset or when PEN[n] is zero.

      Bit         7             6             5             4             3            2             1             0
                                           STALL         TXSTP         PERR          TRFAIL                      TRCPT
   Access                                   R/W           R/W           R/W           R/W                         R/W
    Reset                                     0             0             0            0                           2


            Bit 5 – STALL Received Stall Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Received Stall interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The received Stall interrupt is disabled.
             1           The received Stall interrupt is enabled and an interrupt request will be generated when the
                         received Stall interrupt Flag is set.

            Bit 4 – TXSTP Transmitted Setup Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Transmitted Setup interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The Transmitted Setup interrupt is disabled.
             1           The Transmitted Setup interrupt is enabled and an interrupt request will be generated when
                         the Transmitted Setup interrupt Flag is set.

            Bit 3 – PERR Pipe Error Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Pipe Error interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The Pipe Error interrupt is disabled.
             1           The Pipe Error interrupt is enabled and an interrupt request will be generated when the Pipe
                         Error interrupt Flag is set.

            Bit 2 – TRFAIL Transfer Fail Interrupt Disable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will clear the Transfer Fail interrupt Enable bit and disable the corresponding
            interrupt request.
             Value       Description
             0           The Transfer Fail interrupt is disabled.




        © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1192
                                                   SAM D5x/E5x Family Data Sheet
                                                                         USB – Universal Serial Bus

 Value        Description
 1            The Transfer Fail interrupt is enabled and an interrupt request will be generated when the
              Transfer Fail interrupt Flag is set.

Bit 0 – TRCPT Transfer Complete Bank x interrupt Disable
Writing a zero to this bit has no effect.
Writing a one to this bit will clear the Transfer Complete interrupt Enable bit x and disable the
corresponding interrupt request.
 Value      Description
 0          The Transfer Complete Bank x interrupt is disabled.
 1          The Transfer Complete Bank x interrupt is enabled and an interrupt request will be
            generated when the Transfer Complete interrupt x Flag is set.




© 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1193
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                      USB – Universal Serial Bus

38.8.6.8 Host Interrupt Pipe Set Register

            Name:         PINTENSET
            Offset:       0x109 + (n x 0x20)
            Reset:        0x00
            Property:     PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Pipe Interrupt Enable Set (PINTENCLR) register.
            This register is cleared by USB reset or when PEN[n] is zero.

      Bit         7              6             5              4               3        2          1            0
                                             STALL         TXSTP         PERR        TRFAIL                  TRCPT
   Access                                     R/W            R/W          R/W         R/W                     R/W
    Reset                                      0              0               0        0                       2


            Bit 5 – STALL Stall Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Stall interrupt.
            Value       Description
            0           The Stall interrupt is disabled.
            1           The Stall interrupt is enabled.

            Bit 4 – TXSTP Transmitted Setup Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Transmitted Setup interrupt.
            Value       Description
            0           The Transmitted Setup interrupt is disabled.
            1           The Transmitted Setup interrupt is enabled.

            Bit 3 – PERR Pipe Error Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Pipe Error interrupt.
            Value       Description
            0           The Pipe Error interrupt is disabled.
            1           The Pipe Error interrupt is enabled.

            Bit 2 – TRFAIL Transfer Fail Interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Transfer Fail interrupt.
            Value       Description
            0           The Transfer Fail interrupt is disabled.
            1           The Transfer Fail interrupt is enabled.

            Bit 0 – TRCPT Transfer Complete x interrupt Enable
            Writing a zero to this bit has no effect.
            Writing a one to this bit will enable the Transfer Complete interrupt Enable bit x.
            0.2.7 Host Registers - Pipe RAM




        © 2019 Microchip Technology Inc.                            Datasheet                     DS60001507E-page 1194
                                                                         SAM D5x/E5x Family Data Sheet
                                                                                                                USB – Universal Serial Bus

          Value               Description
          0                   The Transfer Complete x interrupt is disabled.
          1                   The Transfer Complete x interrupt is enabled.

38.8.7   Host Registers - Pipe RAM

38.8.7.1 Pipe Descriptor Structure


                                             Data Buffers


                                                 Pn BK1




                                                 Pn BK0




                                         Pipe descriptors

                                                 Reserved
                                               STATUS _PIPE
                                                 CTRL_BK
                                     Bank1
                                                 Reserved
                                                 Reserved
                     Descriptor Pn




                                                 PCKSIZE
                                                  ADDR        (2 x 0xn0) + 0x10
                                                 Reserved
                                               STATUS _PIPE
                                                CTRL_PIPE
                                     Bank0
                                                STATUS_BK
                                                 EXTREG
                                                 PCKSIZE
                                                  ADDR        2 x 0xn0



                                                 Reserved     +0x01F
                                                                                     Growing Memory Addresses




                                               STATUS _PIPE   +0x01E
                                                 CTRL_BK      +0x01C
                                     Bank1
                                                 Reserved     +0x01A
                                                 Reserved     +0x018
                     Descriptor P0




                                                 PCKSIZE      +0x014
                                                  ADDR        +0x010
                                                 Reserved     +0x00F
                                               STATUS _PIPE   +0x00E
                                                CTRL_PIPE     +0x00C
                                     Bank0
                                                STATUS_BK     +0x00A
                                                 EXTREG       +0x008
                                                 PCKSIZE      +0x004
                                                  ADDR        +0x000          DESCADD




         © 2019 Microchip Technology Inc.                                Datasheet                                        DS60001507E-page 1195
                                                              SAM D5x/E5x Family Data Sheet
                                                                                 USB – Universal Serial Bus

38.8.7.2 Address of the Data Buffer

            Name:       ADDR
            Offset:     0x00 & 0x10
            Reset:      0xxxxxxxx
            Property:   NA


      Bit        31           30           29          28                 27     26           25           24
                                                            ADDR[31:24]
   Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W          R/W
    Reset        0             0            0           0                  0      0           0            0


      Bit        23           22           21          20                 19     18           17           16
                                                            ADDR[23:16]
   Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W          R/W
    Reset        0             0            0           0                  0      0           0            0


      Bit        15           14           13          12                 11     10           9            8
                                                             ADDR[15:8]
   Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W          R/W
    Reset        0             0            0           0                  0      0           0            0


      Bit        7             6            5           4                  3      2           1            0
                                                             ADDR[7:0]
   Access       R/W          R/W           R/W         R/W                R/W   R/W          R/W          R/W
    Reset        0             0            0           0                  0      0           0            x


            Bits 31:0 – ADDR[31:0] Data Pointer Address Value
            These bits define the data pointer address as an absolute double word address in RAM. The two least
            significant bits must be zero to ensure the descriptor is 32-bit aligned.




        © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1196
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                     USB – Universal Serial Bus

38.8.7.3 Packet Size

            Name:       PCKSIZE
            Offset:     0x04 & 0x14
            Reset:      0xxxxxxxx
            Property:   NA


      Bit         31          30              29            28          27           26           25           24
             AUTO_ZLP                      SIZE[2:0]                             MULTI_PACKET_SIZE[13:10]
   Access         R/W        R/W             R/W            R/W        R/W          R/W          R/W          R/W
    Reset          x           0              0              x           0           0             0           0


      Bit         23          22              21            20          19           18           17           16
                                                        MULTI_PACKET_SIZE[9:2]
   Access         R/W        R/W             R/W            R/W        R/W          R/W          R/W          R/W
    Reset          0           0              0              0           0           0             0           0


      Bit         15          14              13            12          11           10            9           8
              MULTI_PACKET_SIZE[1:0]                                    BYTE_COUNT[5:0]
   Access         R/W        R/W             R/W            R/W        R/W          R/W          R/W          R/W
    Reset          0           x              0              0           0           0             0           x


      Bit          7           6              5              4           3           2             1           0


   Access
    Reset


            Bit 31 – AUTO_ZLP Automatic Zero Length Packet
            This bit defines the automatic Zero Length Packet mode of the pipe.
            When enabled, the USB module will manage the ZLP handshake by hardware. This bit is for OUT pipes
            only. When disabled the handshake should be managed by firmware.
             Value       Description
             0           Automatic Zero Length Packet is disabled.
             1           Automatic Zero Length Packet is enabled.

            Bits 30:28 – SIZE[2:0] Pipe size
            These bits contains the size of the pipe.
            Theses bits are cleared upon sending a USB reset.

            SIZE[2:0]                         Description
            0x0                               8 Byte
            0x1                               16 Byte
            0x2                               32 Byte
            0x3                               64 Byte
            0x4                               128 Byte(1)
            0x5                               256 Byte(1)




        © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1197
                                                  SAM D5x/E5x Family Data Sheet
                                                                        USB – Universal Serial Bus

...........continued
 SIZE[2:0]                         Description
 0x6                               512 Byte(1)
 0x7                               1024 Byte in HS mode(1)
                                   1023 Byte in FS mode(1)

1. For Isochronous pipe only.

Bits 27:14 – MULTI_PACKET_SIZE[13:0] Multi Packet IN or OUT size
These bits define the 14-bit value that is used for multi-packet transfers.
For IN pipes, MULTI_PACKET_SIZE holds the total number of bytes sent. MULTI_PACKET_SIZE should
be written to zero when setting up a new transfer.
For OUT pipes, MULTI_PACKET_SIZE holds the total data size for the complete transfer. This value must
be a multiple of the maximum packet size.

Bits 13:8 – BYTE_COUNT[5:0] Byte Count
These bits define the 14-bit value that contains number of bytes sent in the last OUT or SETUP
transaction for an OUT pipe, or of the number of bytes to be received in the next IN transaction for an
input pipe.




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1198
                                                            SAM D5x/E5x Family Data Sheet
                                                                                USB – Universal Serial Bus

38.8.7.4 Extended Register

            Name:       EXTREG
            Offset:     0x08
            Reset:      0xxxxxxxx
            Property:   NA


      Bit        15           14            13         12            11         10                 9            8
                                                              VARIABLE[10:4]
  Access                     R/W           R/W        R/W            R/W       R/W             R/W             R/W
    Reset                      0            0          0              0          0                 0            0


      Bit        7             6            5          4              3          2                 1            0
                                VARIABLE[3:0]                                        SUBPID[3:0]
  Access        R/W          R/W           R/W        R/W            R/W       R/W             R/W             R/W
    Reset        0             0            0          x              0          0                 0            x


            Bits 14:4 – VARIABLE[10:0] Variable field send with extended token
            These bits define the VARIABLE field sent with extended token. See “Section 2.1.1 Protocol Extension
            Token in the reference document ENGINEERING CHANGE NOTICE, USB 2.0 Link Power Management
            Addendum.”
            To support the USB2.0 Link Power Management addition the VARIABLE field should be set as described
            below.

            VARIABLE                                 Description
            VARIABLE[3:0]                            bLinkState(1)
            VARIABLE[7:4]                            BESL (See LPM ECN)(2)
            VARIABLE[8]                              bRemoteWake(1)
            VARIABLE[10:9]                           Reserved

            (1) for a definition of LPM Token bRemoteWake and bLinkState fields, refer to "Table 2-3 in the reference
            document ENGINEERING CHANGE NOTICE, USB 2.0 Link Power Management Addendum"
            (2) for a definition of LPM Token BESL field, refer to "Table 2-3 in the reference document ENGINEERING
            CHANGE NOTICE, USB 2.0 Link Power Management Addendum" and "Table X-X1 in Errata for ECN USB 2.0
            Link Power Management.


            Bits 3:0 – SUBPID[3:0] SUBPID field send with extended token
            These bits define the SUBPID field sent with extended token. See “Section 2.1.1 Protocol Extension
            Token in the reference document ENGINEERING CHANGE NOTICE, USB 2.0 Link Power Management
            Addendum”.
            To support the USB2.0 Link Power Management addition the SUBPID field should be set as described in
            “Table 2.2 SubPID Types in the reference document ENGINEERING CHANGE NOTICE, USB 2.0 Link
            Power Management Addendum”.




        © 2019 Microchip Technology Inc.                    Datasheet                              DS60001507E-page 1199
                                                             SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

38.8.7.5 Host Status Bank

            Name:       STATUS_BK
            Offset:     0x0A & 0x1A
            Reset:      0xxxxxxxx
            Property:   NA


      Bit         7            6            5            4            3            2            1            0
                                                                                          ERRORFLOW      CRCERR
  Access                                                                                      R/W          R/W
    Reset                                                                                       x            x


            Bit 1 – ERRORFLOW Error Flow Status
            This bit defines the Error Flow Status.
            This bit is set when a Error Flow has been detected during transfer from/towards this bank.
            For IN transfer, a NAK handshake has been received. For OUT transfer, a NAK handshake has been
            received. For Isochronous IN transfer, an overrun condition has occurred. For Isochronous OUT transfer,
            an underflow condition has occurred.
             Value        Description
             0            No Error Flow detected.
             1            A Error Flow has been detected.

            Bit 0 – CRCERR CRC Error
            This bit defines the CRC Error Status.
            This bit is set when a CRC error has been detected in an isochronous IN endpoint bank.
             Value        Description
             0            No CRC Error.
             1            CRC Error detected.




        © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1200
                                                               SAM D5x/E5x Family Data Sheet
                                                                                   USB – Universal Serial Bus

38.8.7.6 Host Control Pipe

            Name:       CTRL_PIPE
            Offset:     0x0C
            Reset:      0xXXXX
            Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized


      Bit        15            14                 13     12             11         10                 9        8
                                    PERMAX[3:0]                                         PEPNUM[3:0]
   Access       R/W           R/W             R/W        R/W           R/W         R/W            R/W         R/W
    Reset         0            0                  0       x              0          0                 0        x


      Bit         7            6                  5       4              3          2                 1        0
                                                                    PDADDR[6:0]
   Access                     R/W             R/W        R/W           R/W         R/W            R/W         R/W
    Reset                      0                  0       0              0          0                 0        x


            Bits 15:12 – PERMAX[3:0] Pipe Error Max Number
            These bits define the maximum number of error for this Pipe before freezing the pipe automatically.

            Bits 11:8 – PEPNUM[3:0] Pipe EndPoint Number
            These bits define the number of endpoint for this Pipe.

            Bits 6:0 – PDADDR[6:0] Pipe Device Address
            These bits define the Device Address for this pipe.




        © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1201
                                                              SAM D5x/E5x Family Data Sheet
                                                                                  USB – Universal Serial Bus

38.8.7.7 Host Status Pipe

            Name:       STATUS_PIPE
            Offset:     0x0E & 0x1E
            Reset:      0xxxxxxxx
            Property:   PAC Write-Protection, Write-Synchronized, Read-Synchronized


      Bit        15           14           13            12           11           10            9           8


   Access
    Reset


      Bit         7            6            5            4            3            2             1           0
                          ERCNT[2:0]                 CRC16ER       TOUTER        PIDER        DAPIDER     DTGLER
   Access       R/W           R/W          R/W          R/W          R/W          R/W           R/W         R/W
    Reset         0            0            x            x            x            x             x           x


            Bits 7:5 – ERCNT[2:0] Pipe Error Counter
            These bits define the number of errors detected on the pipe.

            Bit 4 – CRC16ER CRC16 ERROR
            This bit defines the CRC16 Error Status.
            This bit is set when a CRC 16 error has been detected during a IN transactions.
             Value        Description
             0            No CRC 16 Error detected.
             1            A CRC 16 error has been detected.

            Bit 3 – TOUTER TIME OUT ERROR
            This bit defines the Time Out Error Status.
            This bit is set when a Time Out error has been detected during a USB transaction.
             Value        Description
             0            No Time Out Error detected.
             1            A Time Out error has been detected.

            Bit 2 – PIDER PID ERROR
            This bit defines the PID Error Status.
            This bit is set when a PID error has been detected during a USB transaction.
             Value        Description
             0            No PID Error detected.
             1            A PID error has been detected.

            Bit 1 – DAPIDER Data PID ERROR
            This bit defines the PID Error Status.
            This bit is set when a Data PID error has been detected during a USB transaction.
             Value        Description
             0            No Data PID Error detected.
             1            A Data PID error has been detected.




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1202
                                                 SAM D5x/E5x Family Data Sheet
                                                              USB – Universal Serial Bus

Bit 0 – DTGLER Data Toggle Error
This bit defines the Data Toggle Error Status.
This bit is set when a Data Toggle Error has been detected.
 Value        Description
 0            No Data Toggle Error.
 1            Data Toggle Error detected.




© 2019 Microchip Technology Inc.                  Datasheet            DS60001507E-page 1203
