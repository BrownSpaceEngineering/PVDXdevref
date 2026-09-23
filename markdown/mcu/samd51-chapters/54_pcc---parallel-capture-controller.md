# 52. PCC - Parallel Capture Controller

*Source: `Atmel-SAMD51.pdf`, pages 1925-1945 — SAMD51 family datasheet*

                                                                       SAM D5x/E5x Family Data Sheet
                                                                                      PCC - Parallel Capture Controller


52.    PCC - Parallel Capture Controller

52.1   Overview
       The Parallel Capture Controller can be used to interface an external system, such as a CMOS digital
       image sensor, ADC, or DSP, and capture its parallel data.



52.2   Features
         •   One clock, up to 14-bit parallel data and two Data Enable on I/O lines
         •   Data can be sampled every other time (e.g. for chrominance sampling)
         •   Supports connection of the DMAC which offers buffer reception without processor intervention
         •   Auto-scale feature available when 10, 12 or 14 bits data size is selected.
         •   Can be used to interface a CMOS Digital Image Sensor, an ADC, etc.



52.3   Block Diagram
       Figure 52-1. Block Diagram


                                                         Data
                                     DMAC
                                                         Status
                                                                                                       CLK

                                                                                                       DATA[n:0]
                                                                       Parallel Capture
                                                       PCC Interrupt
                              Interrupt Controller                        Controller                   DEN1

                                                                                                       DEN2



                                                     CLK_APB_PCC
                                     MCLK




                                                                               APB




52.4   Signal Description
        Signal                                  Description                               Type
        CLK                                     Digital input                             PCC Clock
        DATA[n:0]                               Digital input                             Data [n:0]
        DEN1                                    Digital input                             Data Enable 1
        DEN2                                    Digital input                             Data Enable 2




       © 2019 Microchip Technology Inc.                                  Datasheet                                 DS60001507E-page 1925
                                                           SAM D5x/E5x Family Data Sheet
                                                                         PCC - Parallel Capture Controller


52.5     Product Dependencies
         For the Parallel Capture Controller to function as intended, other interconnected modules of the system
         must be configured accordingly.

52.5.1   I/O Lines
         The PCC pins may be multiplexed with the I/O lines Controller. The user must first configure the I/O
         Controller to assign the PCC pins to their peripheral functions.

52.5.2   Power Management
         The PCC will continue to operate in any Sleep mode where the selected source clock is running. Events
         connected to the event system can trigger other operations in the system without exiting Sleep modes.

52.5.3   Clocks
         The PCC bus clock (CLK_APB_PCC) is provided by the Main Clock Controller (MCLK) through the AHB-
         APB D bridge. The clock is enabled and disabled by writing the PCC bit the in the APB D Mask register
         (MCLK.APBDMASK.PCC). See the register description for the default state of the PCC bus clock.
         For capturing operation, the external device has to provide a PCC clock signal (PCC_CLK) synchronous
         to the data received ("pixel clock") through a pin. See the PORT section and the Multiplexing table for
         details.
         Writing any of the registers does not require the PCC_CLK to be enabled.


                        Important: The CLK_APB_PCC clock frequency must be at least twice the PCC_CLK
                        frequency.


         Related Links
         15.7 Register Summary
         6. I/O Multiplexing and Considerations
         32. PORT - I/O Pin Controller

52.5.4   DMA
         The DMAC can be configured to use the RX channel of the PCC as trigger source.
         If configured, a trigger signal is send to the DMAC when data is received by the PCC, such that the
         DMAC will automatically read the received data buffer. The buffer ready signal will be automatically clear
         upon the read done by the DMAC.
         Related Links
         52.6.3 Programming Sequence
         52.6.3.1 Without DMAC
         52.6.3.2 With DMAC

52.5.5   Interrupts
         The PCC has these interrupts:
          • OVRE - Overrun Error interrupt
          • DRDY - Data Ready interrupt




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1926
                                                            SAM D5x/E5x Family Data Sheet
                                                                             PCC - Parallel Capture Controller

         The interrupt request line is connected to the interrupt controller. Using the interrupts requires the
         interrupt controller to be configured first. Refer to NVIC - Nested Interrupt Nested Vector Interrupt
         Controller for details.

52.5.6   Events
         Not applicable.

52.5.7   Debug Operation
         When the CPU is halted in debug mode, the PCC will not halt normal operation.
         Note: A buffer overflow condition will occur if the received data buffer is not read by CPU or CPU
         DMAC.

52.5.8   Register Access Protection
         To prevent any single software error from corrupting PCC behavior, certain registers in the address space
         can be write-protected by setting the WPEN bit in the Write Protection Mode Register (WPMR).
         If a write access to a write-protected register is detected, the WPVS flag in the Write Protection Status
         Register (WPSR) is set and WPSR.WPVSRC indicates the register in which the write access has been
         attempted.
         The WPVS bit is automatically cleared after reading WPSR.
         The following registers can be write-protected:
           • PCC Mode Register

52.5.9   Analog Connections
         Not applicable.


52.6     Functional Description
52.6.1   Principle of Operation
         For better understanding and to ease reading, the following description uses an example with a CMOS
         digital image sensor.
         The CMOS digital image sensor provides a sensor clock, an 10-bit data synchronous with the sensor
         clock and two data enables which are also synchronous with the sensor clock.
         Figure 52-2. Parallel Capture Controller Connection with CMOS Digital Image Sensor

                                                   Parallel Capture
                                                      Controller
                                                                                                       CMOS Digital
                                                                       CLK                 PCLK        Image Sensor

                                    Data                         DATA[9:0]                 DATA[9:0]
                DMAC
                                                                      DEN1                 VSYNC

                                                                      DEN2                 HSYNC




         The PCC must be configured first, and is enabled by writing a '1' to the Parallel Capture Enable bit in the
         Mode Register (MR.PCEN).




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 1927
                                                   SAM D5x/E5x Family Data Sheet
                                                                  PCC - Parallel Capture Controller

Once enabled, the PCC samples the data at rising edge of the sensor clock, and resynchronizes it with
the PCC clock domain.
The input data bus size can be programmed using the Input Data Size bit field (MR.ISIZE).
A re-initialization of the internal mechanism of the PCC can be automatically done by setting the CID
register when a falling edge of the DEN1 or DEN2 is detected. This feature allows glitch filtering and
prevents image de-synchronization.
The number of the data which can be read in the Reception Holding Register (RHR) can be programmed
by writing the Data Size bit field (MR.DSIZE). The PCC samples one or several sensor data, according to
the DSIZE value.
If the MR.SCALE bit is written to '1' and MR.ISIZE ≠ 0, the sampled data is automatically up-scaled to 16
bits. When the right number of data has be sampled, data are stored in the RHR, and the Data Ready
flag in the Interrupt Status Register (ISR.DRDY) is set to '1'.
The PCC can be associated with a reception channel of the DMA Controller (DMAC). This performs
reception transfer from the PCC to a memory buffer without any intervention from the CPU. Transfer
status signals from the DMAC are available in the Interrupt Status Register through the flags ISR.ENDRX
and ISR.RXBUFF.
The PCC can be configured to either comply with the sensor data enable signals, or not. If the Always
Sampling bit in the Mode Register (MR.ALWYS) is written to '0', the PCC samples the sensor data at the
rising edge of the sensor clock only if both data enable signals are active (at '1'). If ALWYS is written to
'1', the PCC samples the sensor data at the rising edge of the sensor clock, independent of the data
enable signals.
The PCC can be configured to sample the sensor data only every other time. This is particularly useful
when only the luminance Y from a YUV422 data stream of a CMOS digital image sensor is to be
sampled. If the Half Sampling bit in the Mode Register (MR.HALFS) is written to '0', the PCC samples the
sensor data as configured above. If MR.HALFS=1, the PCC samples the sensor data as configured
above (i.e. respecting the MR.ALWYS setting), but only one time out of two.
The PCC can either sample the even or odd sensor data, depending on the First Sample bit
(MR.FRSTS). If sensor data are numbered with an index from zero to n in the order they are received and
FRSTS=0, only data with an even index are sampled. For FRSTS=1, only data with an odd index are
sampled.
If data are ready in the Reception Holding Register (RHR) but it is not read before new data is stored in
RHR, an overrun error occurs: The previous data is lost and the Overrun Error flag in the Interrupt Status
Register (ISR.OVRE) is set. This flag is automatically cleared when ISR is read (reset after read).
The flags ENDRX, RXBUFF, DRDY and OVRE can be a source of the PCC interrupt.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1928
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   PCC - Parallel Capture Controller

Figure 52-3. PCC Waveforms (DSIZE=4_DATA, ALWYS = 0, HALFS = 0)
                  MCLK


                   CLK


               DATA[7:0]      0x01    0x12    0x23    0x34     0x45        0x56      0x67        0x78     0x89


                   DEN1


                   DEN2


               ISR.DRDY

          Read of ISR.DRDY


             RHR.RDATA                                                                      0x5645_3423


Figure 52-4. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 0, HALFS = 0, SCALE = 0)
                    MCLK


                      CLK


                DATA[9:0]     0x101   0x112   0x123   0x134    0x145       0x156     0x167       0x178    0x189


                     DEN1


                     DEN2


                 ISR.DRDY

          Read of ISR.DRDY


               RHR.RDATA                                              0x0134_0123           0x0156_0145


Figure 52-5. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 0, HALFS = 0, SCALE = 1)
                    MCLK


                      CLK


                DATA[9:0]     0x101   0x112   0x123   0x134    0x145       0x156     0x167       0x178    0x189


                   DEN1


                    DEN2


               ISR.DRDY

          Read of ISR.DRDY


              RHR.RDATA                                               0x4D00_48C0           0x5580_5140




© 2019 Microchip Technology Inc.                              Datasheet                                           DS60001507E-page 1929
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                         PCC - Parallel Capture Controller

Figure 52-6. PCC Waveforms (DSIZE=4_DATA, ALWYS = 1, HALFS = 0)
                   MCLK


                    CLK


                DATA[7:0]     0x01    0x12    0x23        0x34      0x45        0x56       0x67        0x78      0x89


                   DEN1


                   DEN2


               ISR.DRDY

          Read of ISR.DRDY


             RHR.RDATA                                                     0x3423_1201                                  0x7867_5645


Figure 52-7. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 1, HALFS = 0, SCALE = 0)
                  MCLK


                    CLK


              DATA[9:0]       0x101   0x112   0x123       0x134     0x145       0x156      0x167       0x178     0x189


                   DEN1


                   DEN2


               ISR.DRDY

          Read of ISR.DRDY


             RHR.RDATA                               0x0112_0101           0x0134_0123             0x0156_0145           0x0178_0167


Figure 52-8. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 1, HALFS = 0, SCALE = 1)
                  MCLK


                    CLK


              DATA[9:0]       0x101   0x112   0x123       0x134     0x145       0x156      0x167       0x178     0x189


                  DEN1


                   DEN2


               ISR.DRDY

          Read of ISR.DRDY


              RHR.RDATA                              0x4480_4040           0x4D00_48C0             0x5580_5140           0x5E00_59C0




© 2019 Microchip Technology Inc.                                   Datasheet                                             DS60001507E-page 1930
                                                             SAM D5x/E5x Family Data Sheet
                                                                                   PCC - Parallel Capture Controller

Figure 52-9. PCC Waveforms (DSIZE=4_DATA, ALWYS = 0, HALFS = 1, FRSTS = 0)
                    MCLK


                      CLK


                 DATA[7:0]    0x01    0x12    0x23    0x34        0x45     0x56      0x67    0x78         0x89


                    DEN1


                    DEN2


                 ISR.DRDY

          Read of ISR.DRDY


               RHR.RDATA                                                                             0x6745_2301


Figure 52-10. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 0, HALFS = 1, FRSTS =
0, SCALE = 0)
                    MCLK


                      CLK


                DATA[9:0]     0x101   0x112   0x123   0x134      0x145     0x156     0x167   0x178        0x189


                    DEN1


                    DEN2


                ISR.DRDY

          Read of ISR.DRDY


              RHR.RDATA                                      0x0123_0101                             0x0167_0145


Figure 52-11. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 0, HALFS = 1, FRSTS =
0, SCALE = 1)
                     MCLK


                      CLK


                DATA[9:0]     0x101   0x112   0x123   0x134      0x145     0x156     0x167   0x178        0x189


                    DEN1


                    DEN2


                ISR.DRDY

          Read of ISR.DRDY


              RHR.RDATA                                      0x48C0_4040                             0x5140_0145




© 2019 Microchip Technology Inc.                               Datasheet                                           DS60001507E-page 1931
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                            PCC - Parallel Capture Controller

         Figure 52-12. PCC Waveforms (DSIZE=4_DATA, ALWYS = 0, HALFS = 1, FRSTS = 1)
                             MCLK


                               CLK


                          DATA[7:0]    0x01    0x12    0x23    0x34     0x45        0x56      0x67    0x78    0x89


                             DEN1


                             DEN2


                          ISR.DRDY

                   Read of ISR.DRDY


                        RHR.RDATA                                                                                    0x7856_3412


         Figure 52-13. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 0, HALFS = 1, FRSTS =
         1, SCALE = 0)
                            MCLK


                             CLK


                       DATA[9:0]       0x101   0x112   0x123   0x134    0x145       0x156     0x167   0x178   0x189


                            DEN1


                            DEN2


                        ISR.DRDY

                   Read of ISR.DRDY


                       RHR.RDATA                                               0x0134_0112                           0x0178_0156


         Figure 52-14. PCC Waveforms (ISIZE=10_BITS, DSIZE=2_DATA, ALWYS = 0, HALFS = 1, FRSTS =
         1, SCALE = 1)
                            MCLK


                              CLK


                        DATA[9:0]      0x101   0x112   0x123   0x134    0x145       0x156     0x167   0x178   0x189


                            DEN1


                            DEN2


                        ISR.DRDY

                   Read of ISR.DRDY


                      RHR.RDATA                                                0x4D00_4880                           0x5E00_5580




52.6.2   Register Access Protection
         The configuration bit fields ISIZE, SCALE, DSIZE, ALWYS, HALFS and FRSTS in the Mode Register
         (MR) can be changed ONLY if the PCC is disabled at this time (MR.PCEN=0).




         © 2019 Microchip Technology Inc.                              Datasheet                                      DS60001507E-page 1932
                                                          SAM D5x/E5x Family Data Sheet
                                                                        PCC - Parallel Capture Controller

52.6.3   Programming Sequence

52.6.3.1 Without DMAC
           1.   Write the Interrupt Enable and Interrupt Disable Registers (IER and IDR) in order to configure the
                PCC interrupt mask.
           2.   Write the Mode Register (MR) fields ISIZE, SCALE, DSIZE, ALWYS, HALFS and FRSTS in order to
                configure the PCC. Do not enable the PCC in this write access.
           3.   Write the PCC Enable bit in the Mode Register (MR.PCEN) to '1' in order to enable the PCC. Do
                not change the configuration from the previous step.
           4.   Wait for a Data Ready, either by polling the Data Ready flag in the Interrupt Status Register
                (ISR.DRDY) or by waiting for the corresponding interrupt.
           5.   Check the Overrun Error flag (ISR.OVRE).
           6.   Read the data in the Reception Holding Register (RHR).
           7.   If new data are expected, go to step 4.
           8.   Disable the PCC by writing MR.PCEN to '0' without changing the configuration.
52.6.3.2 With DMAC
           1.   Write the Interrupt Enable and Interrupt Disable Registers (IER and IDR) in order to configure the
                PCC interrupt mask.
           2.   Configure DMAC transfer in the DMAC registers.
           3.   Write the Mode Register (MR) fields ISIZE, SCALE, DSIZE, ALWYS, HALFS and FRSTS in order to
                configure the PCC. Do not enable the PCC in this write access.
           4.   Write the PCC Enable bit in the Mode Register (MR.PCEN) to '1' in order to enable the PCC. Do
                not change the configuration from the previous step.
           5.   Wait for end of transfer, indicated by the interrupt corresponding the End Receive flag in the
                Interrupt Status Register (ISR.ENDRX).
           6.   Check the Overrun Error flag (ISR.OVRE).
           7.   If a new buffer transfer is expected, go to step 5.
           8.   Disable the PCC by writing MR.PCEN to '0' without changing the configuration.




         © 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1933
                                                            SAM D5x/E5x Family Data Sheet
                                                                               PCC - Parallel Capture Controller


52.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0                           DSIZE[1:0]                                          PCEN
                             15:8                                                 FRSTS   HALFS     ALWYS       SCALE
 0x00           MR
                             23:16                                                                 ISIZE[2:0]
                             31:24           CID[1:0]
                              7:0                                                 RXBUF   ENDRX     OVRE        DRDY
                             15:8
 0x04           IER
                             23:16
                             31:24
                              7:0                                                RXBUFF   ENDRX     OVRE        DRDY
                             15:8
 0x08           IDR
                             23:16
                             31:24
                              7:0                                                RXBUFF   ENDRX     OVRE        DRDY
                             15:8
 0x0C           IMR
                             23:16
                             31:24
                              7:0                                                RXBUFF   ENDRX     OVRE        DRDY
                             15:8
 0x10           ISR
                             23:16
                             31:24
                              7:0                                         RDATA[7:0]
                             15:8                                        RDATA[15:8]
 0x14          RHR
                             23:16                                       RDATA[23:16]
                             31:24                                       RDATA[31:24]
 0x18
   ...       Reserved
 0xDF
                              7:0                                                                               WPEN
                             15:8                                         WPKEY[7:0]
 0xE0         WPMR
                             23:16                                       WPKEY[15:8]
                             31:24                                       WPKEY[23:16]
                              7:0                                                                               WPVS
                             15:8                                        WPVSRC[7:0]
 0xE4          WPSR
                             23:16                                       WPVSRC[15:8]
                             31:24




52.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.




          © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1934
                                                  SAM D5x/E5x Family Data Sheet
                                                                 PCC - Parallel Capture Controller

Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
write protection is denoted by the "PAC Write-Protection" property in each individual register description.
For details, refer to 52.6.2 Register Access Protection.
Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1935
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                    PCC - Parallel Capture Controller

52.8.1         PCC Mode Register

               Name:         MR
               Offset:       0x00
               Reset:        0x00000000
               Property:     -

               This register can only be written if the WPEN bit is cleared in the Write Protection Mode Register.

         Bit        31               30         29                28          27          26            25            24
                          CID[1:0]
   Access           R/W              R/W
    Reset            0                0


         Bit        23               22         21                20          19          18            17            16
                                                                                                     ISIZE[2:0]
   Access                                                                                R/W           R/W           R/W
    Reset                                                                                  0             0            0


         Bit        15               14         13                12          11          10             9            8
                                                                            FRSTS       HALFS         ALWYS         SCALE
   Access                                                                    R/W         R/W           R/W           R/W
    Reset                                                                     0            0             0            0


         Bit         7                6          5                 4          3            2             1            0
                                                     DSIZE[1:0]                                                     PCEN
   Access                                      R/W                R/W                                                R/W
    Reset                                        0                 0                                                  0


               Bits 31:30 – CID[1:0] Clear If Disabled
               Clears status flags if disabled. These bits are useful to re-initialize the internal mechanism of the PCC to
               avoid corrupted data due to glitches. Each time a falling edge of the selected DEN1 or DEN2 signal is
               detected, the internal mechanism of the PCC is re-initialized to avoid alignment issues.
                Value      Description
                0x0        Clear not enabled
                0x1        Clear on falling edge on DEN1 enabled
                0x2        Clear on falling edge on DEN2 enabled
                0x3        Clear on falling edge on either DEN1 or DEN2 enabled

               Bits 18:16 – ISIZE[2:0] Input Data Size
               Value       Name                   Description
               0x0         8_BITS                 Input data bus size is 8 bits
               0x1         10_BITS                Input data bus size is 10 bits
               0x2         12_BITS                Input data bus size is 12 bits
               0x3         14_BITS                Input data bus size is 14 bits

               Bit 11 – FRSTS First Sample
               This bit is useful only if the HALFS bit is set to 1. If data are numbered in the order that they are received
               with an index from 0 to n.




           © 2019 Microchip Technology Inc.                             Datasheet                       DS60001507E-page 1936
                                                 SAM D5x/E5x Family Data Sheet
                                                                PCC - Parallel Capture Controller

 Value        Description
 0            Only data with an even index are sampled.
 1            Only data with an odd index are sampled.

Bit 10 – HALFS Half Sampling
This function is independent from the ALWYS bit.
 Value      Description
 0          The Parallel Capture Controller samples all the data.
 1          The Parallel Capture Controller samples the data only every other time.

Bit 9 – ALWYS Always Sampling
Value      Description
0          The parallel capture Controller samples the data when both data enables are active.
1          The parallel capture controller always samples the data, regardless of the state of data
           enable.

Bit 8 – SCALE Scale Data
Value      Description
0          No effect.
1          When input data size is not equal to 8 bits (ISIZE ≠ 0), the data stored in the PCC_RHR is
           automatically up-scaled to 16 bits.

Bits 5:4 – DSIZE[1:0] Data Size
Value       Name      Description
0x0         1_DATA 1 data is read in the PCC_RHR
0x1         2_DATA 2 data are read in the PCC_RHR
0x2         4_DATA 4 data are read in the PCC_RHR (only for 8 bits data size, ISIZE = 0)
0x3                   Reserved

Bit 0 – PCEN Parallel Capture Enable
Value      Description
0          The Parallel Capture Controller is disabled.
1          The Parallel Capture Controller is enabled.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1937
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                     PCC - Parallel Capture Controller

52.8.2         Interrupt Enable Register

               Name:        IER
               Offset:      0x04
               Reset:       0x00000000
               Property:    -


         Bit        31             30            29            28            27              26      25           24


   Access
    Reset


         Bit        23             22            21            20            19              18      17           16


   Access
    Reset


         Bit        15             14            13            12            11              10      9            8


   Access
    Reset


         Bit         7             6             5             4              3              2       1            0
                                                                           RXBUF         ENDRX      OVRE        DRDY
   Access                                                                    W               W       W            W
    Reset                                                                     0              0       0            0


               Bit 3 – RXBUF Reception Buffer Full Interrupt Enable.
               Writing a '1' to this register enables the Reception Buffer Full interrupt.
               Writing a '0' has no effect.

               Bit 2 – ENDRX End of Reception Transfer Interrupt Enable
               Writing a '1' to this register enables the End of Reception Transfer interrupt.
               Writing a '0' has no effect.

               Bit 1 – OVRE Overrun Error Interrupt Enable
               Writing a '1' to this register enables the Overrun Error interrupt.
               Writing a '0' has no effect.

               Bit 0 – DRDY Data Ready Interrupt Enable
               Writing a '1' to this register enables the Data Ready Interrupt interrupt.
               Writing a '0' has no effect.




           © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1938
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                      PCC - Parallel Capture Controller

52.8.3         Interrupt Disable Register

               Name:        IDR
               Offset:      0x08
               Reset:       0x00000000
               Property:    -


         Bit         31            30            29            28             27              26      25           24


   Access
    Reset


         Bit         23            22            21            20             19              18      17           16


   Access
    Reset


         Bit         15            14            13            12             11              10      9            8


   Access
    Reset


         Bit         7             6              5             4             3               2       1            0
                                                                           RXBUFF         ENDRX      OVRE        DRDY
   Access                                                                     W               W       W            W
    Reset                                                                     0               0       0            0


               Bit 3 – RXBUFF Reception Buffer Full Interrupt Disable
               Writing a '1' to this register disables the Reception Buffer Full interrupt.
               Writing a '0' has no effect.

               Bit 2 – ENDRX End of Reception Transfer Interrupt Disable
               Writing a '1' to this register disables the End of Reception Transfer interrupt.
               Writing a '0' has no effect.

               Bit 1 – OVRE Overrun Error Interrupt Disable
               Writing a '1' to this register disables the Overrun Error interrupt.
               Writing a '0' has no effect.

               Bit 0 – DRDY Data Ready Interrupt Disable
               Writing a '1' to this register disables the Data Ready interrupt.
               Writing a '0' has no effect.




           © 2019 Microchip Technology Inc.                           Datasheet                       DS60001507E-page 1939
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                 PCC - Parallel Capture Controller

52.8.4         Interrupt Mask Register

               Name:       IMR
               Offset:     0x0C
               Reset:      0x00000000
               Property:   -


         Bit        31           30            29           28            27           26        25           24


   Access
    Reset


         Bit        23           22            21           20            19           18        17           16


   Access
    Reset


         Bit        15           14            13           12            11           10        9            8


   Access
    Reset


         Bit         7            6            5            4             3            2         1            0
                                                                        RXBUFF       ENDRX      OVRE        DRDY
   Access                                                                 R            R         R            R
    Reset                                                                 0            0         0            0


               Bit 3 – RXBUFF Reception Buffer Full Interrupt Mask
               Value      Description
               1          The Reception Buffer Full interrupt is enabled.
               0          The Reception Buffer Full interrupt is not enabled.

               Bit 2 – ENDRX End of Reception Transfer Interrupt Mask
               Value      Description
               1          The End of Reception Transfer interrupt is enabled.
               0          The End of Reception Transfer interrupt is not enabled.

               Bit 1 – OVRE Overrun Error Interrupt Mask
               Value      Description
               1          The Overrun Error interrupt is enabled.
               0          The Overrun Error interrupt is not enabled.

               Bit 0 – DRDY Data Ready Interrupt Mask
               Value      Description
               1          The Data Ready interrupt is enabled.
               0          The Data Ready interrupt is not enabled.




           © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1940
                                                                 SAM D5x/E5x Family Data Sheet
                                                                               PCC - Parallel Capture Controller

52.8.5         Interrupt Status Register

               Name:       ISR
               Offset:     0x10
               Reset:      0x00000000
               Property:   -


         Bit        31           30           29            28           27           26            25           24


   Access
    Reset


         Bit        23           22           21            20           19           18            17           16


   Access
    Reset


         Bit        15           14           13            12           11           10            9            8


   Access
    Reset


         Bit         7            6            5            4            3            2             1            0
                                                                      RXBUFF        ENDRX          OVRE        DRDY
   Access                                                                R            R             R            R
    Reset                                                                0            0             0            0


               Bit 3 – RXBUFF Reception Buffer Full
               Value      Description
               0          The signal Buffer Full from the reception PDC channel is inactive.
               1          The signal Buffer Full from the reception PDC channel is active.

               Bit 2 – ENDRX End of Reception Transfer
               Value      Description
               0          The End of Transfer signal from the reception PDC channel is inactive.
               1          The End of Transfer signal from the reception PDC channel is active.

               Bit 1 – OVRE Overrun Error Interrupt Status
               The OVRE flag is automatically reset when this register is read or when the PCC is disabled.
                Value     Description
                0         No overrun error occurred since the last read of this register.
                1         At least one overrun error occurred since the last read of this register.

               Bit 0 – DRDY Data Ready Interrupt Status
               The DRDY flag is automatically reset when RHR is read or when the PCC is disabled.
                Value     Description
                0         No new data is ready to be read since the last read of RHR.
                1         New data is ready to be read since the last read of RHR.




           © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1941
                                                              SAM D5x/E5x Family Data Sheet
                                                                                PCC - Parallel Capture Controller

52.8.6         Reception Holding Register

               Name:       RHR
               Offset:     0x14
               Reset:      0x00000000
               Property:   -


         Bit        31           30               29    28                 27         26        25           24
                                                            RDATA[31:24]
   Access           R             R               R     R                  R          R          R           R
    Reset           0             0               0     0                  0          0          0           0


         Bit        23           22               21    20                 19         18        17           16
                                                            RDATA[23:16]
   Access           R             R               R     R                  R          R          R           R
    Reset           0             0               0     0                  0          0          0           0


         Bit        15           14               13    12                 11         10         9           8
                                                             RDATA[15:8]
   Access           R             R               R     R                  R          R          R           R
    Reset           0             0               0     0                  0          0          0           0


         Bit        7             6               5     4                  3          2          1           0
                                                             RDATA[7:0]
   Access           R             R               R     R                  R          R          R           R
    Reset           0             0               0     0                  0          0          0           0


               Bits 31:0 – RDATA[31:0] Reception Data

               ISIZE                          SCALE                DSIZE                    Description
               8_BITS                         -                    1_DATA                   RDATA[7:0] is useful
                                                                   2_DATA                   RDATA[15:0] is useful
                                                                   4_DATA                   RDATA[31:0] is useful
               10_BITS                        0 (OFF)              1_DATA                   RDATA[9:0] is useful
                                                                   2_DATA                   RDATA[9:0] and
                                                                                            RDATA[25:16] are useful
                                              1 (ON)               1_DATA                   RDATA[15:0] is useful
                                                                   2_DATA                   RDATA[31:0] is useful
               12_BITS                        0 (OFF)              1_DATA                   RDATA[11:0] is useful
                                                                   2_DATA                   RDATA[11:0] and
                                                                                            RDATA[27:16] are useful
                                              1 (ON)               1_DATA                   RDATA[15:0] is useful
                                                                   2_DATA                   RDATA[31:0] is useful




           © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 1942
                                             SAM D5x/E5x Family Data Sheet
                                                         PCC - Parallel Capture Controller

...........continued
 ISIZE                             SCALE       DSIZE                 Description
 14_BITS                           0 (OFF)     1_DATA                RDATA[13:0] is useful
                                               2_DATA                RDATA[13:0] and
                                                                     RDATA[29:16] are useful
                                   1 (ON)      1_DATA                RDATA[15:0] is useful
                                               2_DATA                RDATA[31:0] is useful




© 2019 Microchip Technology Inc.             Datasheet                   DS60001507E-page 1943
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                  PCC - Parallel Capture Controller

52.8.7         Write Protection Mode Register

               Name:       WPMR
               Offset:     0xE0
               Reset:      0x00000000
               Property:   -


         Bit        31           30           29          28                 27         26        25           24
                                                              WPKEY[23:16]
   Access          R/W          R/W           R/W        R/W             R/W           R/W       R/W          R/W
    Reset           0             0            0          0                  0          0         0            0


         Bit        23           22           21          20                 19         18        17           16
                                                               WPKEY[15:8]
   Access          R/W          R/W           R/W        R/W             R/W           R/W       R/W          R/W
    Reset           0             0            0          0                  0          0         0            0


         Bit        15           14           13          12                 11         10        9            8
                                                               WPKEY[7:0]
   Access          R/W          R/W           R/W        R/W             R/W           R/W       R/W          R/W
    Reset           0             0            0          0                  0          0         0            0


         Bit        7             6            5          4                  3          2         1            0
                                                                                                             WPEN
   Access                                                                                                     R/W
    Reset                                                                                                      0


               Bits 31:8 – WPKEY[23:0] Write Protection Key
               Value       Name    Description
               0x50434 PASSWD Writing any other value in this field aborts the write operation of the WPEN bit.
               3                   Always reads as 0.

               Bit 0 – WPEN Write Protection Enable
               Value      Description
               0          Disables the write protection if WPKEY corresponds to 0x504343 (“PCC” in ASCII).
               1          Enables the write protection if WPKEY corresponds to 0x504343 (“PCC” in ASCII).




           © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1944
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                   PCC - Parallel Capture Controller

52.8.8         Write Protection Status Register

               Name:       WPSR
               Offset:     0xE4
               Reset:      0x00000000
               Property:   -


         Bit        31            30           29            28            27            26          25            24


   Access
    Reset


         Bit        23            22           21            20            19            18          17            16
                                                              WPVSRC[15:8]
   Access            R            R             R            R                 R         R            R            R
    Reset            0            0             0            0                 0         0            0            0


         Bit        15            14           13            12            11            10           9            8
                                                                 WPVSRC[7:0]
   Access            R            R             R            R                 R         R            R            R
    Reset            0            0             0            0                 0         0            0            0


         Bit         7            6             5            4                 3         2            1            0
                                                                                                                 WPVS
   Access                                                                                                          R
    Reset                                                                                                          0


               Bits 23:8 – WPVSRC[15:0] Write Protection Violation Source
               When WPVS = 1, WPVSRC indicates the register address offset at which a write access has been
               attempted.

               Bit 0 – WPVS Write Protection Violation Status
               Value      Description
               0          No write protection violation has occurred since the last read of the WPSR.
               1          A write protection violation has occurred since the last read of the WPSR. If this violation is
                          an unauthorized attempt to write a protected register, the associated violation is reported into
                          field WPVSRC.




           © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 1945
