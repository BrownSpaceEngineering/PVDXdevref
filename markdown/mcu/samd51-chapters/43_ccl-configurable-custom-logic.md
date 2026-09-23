# 41. CCL – Configurable Custom Logic

*Source: `Atmel-SAMD51.pdf`, pages 1393-1411 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                       CCL – Configurable Custom Logic


41.    CCL – Configurable Custom Logic

41.1   Overview
       The Configurable Custom Logic (CCL) is a programmable logic peripheral which can be connected to the
       device pins, to events, or to other internal peripherals. This allows the user to eliminate logic gates for
       simple glue logic functions on the PCB.
       Each LookUp Table (LUT) consists of three inputs, a truth table, an optional synchronizer/filter, and an
       optional edge detector. Each LUT can generate an output as a user programmable logic expression with
       three inputs. Inputs can be individually masked.
       The output can be combinatorially generated from the inputs, and can be filtered to remove spikes.
       Optional sequential logic can be used. The inputs of the sequential module are individually controlled by
       two independent, adjacent LUT (LUT0/LUT1, LUT2/LUT3 etc.) outputs, enabling complex waveform
       generation.



41.2   Features
         • Glue logic for general purpose PCB design
         • Up to 4 programmable LookUp Tables (LUTs)
         • Combinatorial logic functions:
           AND, NAND, OR, NOR, XOR, XNOR, NOT
         • Sequential logic functions:
           Gated D Flip-Flop, JK Flip-Flop, gated D Latch, RS Latch
         • Flexible LUT inputs selection:
            – I/Os
            – Events
            – Internal peripherals
            – Subsequent LUT output
         • Output can be connected to the I/O pins or the Event System
         • Optional synchronizer, filter, or edge detector available on each LUT output




       © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1393
                                                                                            SAM D5x/E5x Family Data Sheet
                                                                                                                         CCL – Configurable Custom Logic


41.3     Block Diagram
         Figure 41-1. Configurable Custom Logic

                                      LUTCTRL0                                                                           LUT0
                                       (INSEL)


                           Internal
                                                                                     LUTCTRL0                LUTCTRL0
                            Events                                                   (FILTSEL)               (EDGESEL)                        SEQCTRL      CTRL
                                                                                                                                             (SEQSEL0)   (ENABLE)
                                                                                                                                                                                  Event System
                                I/O
                                                 Truth Table   8                                                                                                           OUT0
                                                                    Filter / Synch               Edge Detector
                                                                         CLR                          CLR                       Sequential                                        I/O
                        Peripherals                                                                                                CLR



                                            LUTCTRL0
                                            (ENABLE)
                                                         D Q
                     CLK_CCL_APB
                        GCLK_CCL

                                      LUTCTRL1                                                                           LUT1
                                       (INSEL)


                           Internal
                                                                                     LUTCTRL1                LUTCTRL1
                            Events                                                   (FILTSEL)               (EDGESEL)                                     CTRL
                                                                                                                                                         (ENABLE)
                                                                                                                                                                                  Event System
                                I/O
                                                 Truth Table   8                                                                                                           OUT1
                                                                    Filter / Synch               Edge Detector
                                                                         CLR                          CLR                                                                         I/O
                        Peripherals


                                            LUTCTRL1
                                            (ENABLE)
                                                         D Q
                     CLK_CCL_APB
                        GCLK_CCL
                                                                                                                                                                  UNIT 0

                                                                                                                                                                                  Event System
                                                                               .




                                                                                                                                                                     OUT2x-1
                                                                              .
                                                                           ...




                                                                                                                                                         UNIT x                   I/O




41.4     Signal Description
          Pin Name                                 Type                                                Description
          OUT[n:0]                                 Digital output                                      Output from lookup table
          IN[3n+2:0]                               Digital input                                       Input to lookup table

           1.   n is the number of CCL groups.
         Refer to I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One signal
         can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



41.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

41.5.1   I/O Lines
         The CCL can take inputs and generate output through I/O pins. For this to function properly, the I/O pins
         must be configured to be used by a Look Up Table (LUT).
         Related Links
         32. PORT - I/O Pin Controller




         © 2019 Microchip Technology Inc.                                                        Datasheet                                                  DS60001507E-page 1394
                                                           SAM D5x/E5x Family Data Sheet
                                                                         CCL – Configurable Custom Logic

41.5.2   Power Management
         This peripheral can continue to operate in any Sleep mode where its source clock is running. Events
         connected to the event system can trigger other operations in the system without exiting Sleep modes.
         Related Links
         18. PM – Power Manager

41.5.3   Clocks
         The CCL bus clock (CLK_CCL_APB) can be enabled and disabled in the Main Clock module, MCLK (see
         MCLK - Main Clock), and the default state of CLK_CCL_APB can be found in Peripheral Clock Masking.
         A generic clock (GCLK_CCL) is optionally required to clock the CCL. This clock must be configured and
         enabled in the Generic Clock Controller (GCLK) before using input events, filter, edge detection or
         sequential logic. GCLK_CCL is required when input events, a filter, an edge detector, or a sequential sub-
         module is enabled. Refer to GCLK - Generic Clock Controller for details.
         This generic clock is asynchronous to the user interface clock (CLK_CCL_APB).
         Related Links
         15. MCLK – Main Clock
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller

41.5.4   DMA
         Not applicable.

41.5.5   Interrupts
         Not applicable.

41.5.6   Events
         The CCL can use events from other peripherals and generate events that can be used by other
         peripherals. For this feature to function, the events have to be configured properly. Refer to the Related
         Links below for more information about the event users and event generators.
         Related Links
         31. EVSYS – Event System

41.5.7   Debug Operation
         When the CPU is halted in Debug mode the CCL continues normal operation. However, the CCL cannot
         be halted when the CPU is halted in Debug mode. If the CCL is configured in a way that requires it to be
         periodically serviced by the CPU, improper operation or data loss may result during debugging.

41.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC). Refer to PAC - Peripheral Access Controller for details.
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1395
                                                             SAM D5x/E5x Family Data Sheet
                                                                           CCL – Configurable Custom Logic

41.5.9    Analog Connections
          Not applicable.



41.6      Functional Description

41.6.1    Principle of Operation
          Configurable Custom Logic (CCL) is a programmable logic block that can use the device port pins,
          internal peripherals, and the internal Event System as both input and output channels. The CCL can
          serve as glue logic between the device and external devices. The CCL can eliminate the need for
          external logic component and can also help the designer overcome challenging real-time constrains by
          combining core independent peripherals in clever ways to handle the most time critical parts of the
          application independent of the CPU.

41.6.2    Operation

41.6.2.1 Initialization
          The following bits are enable-protected, meaning that they can only be written when the corresponding
          even LUT is disabled (LUTCTRLx.ENABLE=0):
           • Sequential Selection bits in the Sequential Control x (SEQCTRLx.SEQSEL) register
          The following registers are enable-protected, meaning that they can only be written when the
          corresponding LUT is disabled (LUTCTRLx.ENABLE=0):
           • LUT Control x (LUTCTRLx) register, except the ENABLE bit
          Enable-protected bits in the LUTCTRLx registers can be written at the same time as LUTCTRLx.ENABLE
          is written to '1', but not at the same time as LUTCTRLx.ENABLE is written to '0'.
          Enable-protection is denoted by the Enable-Protected property in the register description.
41.6.2.2 Enabling, Disabling, and Resetting
          The CCL is enabled by writing a '1' to the Enable bit in the Control register (CTRL.ENABLE). The CCL is
          disabled by writing a '0' to CTRL.ENABLE.
          Each LUT is enabled by writing a '1' to the Enable bit in the LUT Control x register (LUTCTRLx.ENABLE).
          Each LUT is disabled by writing a '0' to LUTCTRLx.ENABLE.
          The CCL is reset by writing a '1' to the Software Reset bit in the Control register (CTRL.SWRST). All
          registers in the CCL will be reset to their initial state, and the CCL will be disabled. Refer to 41.8.1 CTRL
          for details.
41.6.2.3 Lookup Table Logic
          The lookup table in each LUT unit can generate any logic expression OUT as a function of three inputs
          (IN[2:0]), as shown in Figure 41-2. One or more inputs can be masked. The truth table for the expression
          is defined by TRUTH bits in LUT Control x register (LUTCTRLx.TRUTH).




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1396
                                                            SAM D5x/E5x Family Data Sheet
                                                                           CCL – Configurable Custom Logic

         Figure 41-2. Truth Table Output Value Selection
                                                                                 LUT
                                                 TRUTH[0]
                                                 TRUTH[1]
                                                 TRUTH[2]
                                                 TRUTH[3]
                                                 TRUTH[4]                               OUT
                                                 TRUTH[5]
                                                 TRUTH[6]            LUTCTRL
                                                                     (ENABLE)
                                                 TRUTH[7]

                                       IN[2:0]

         Table 41-1. Truth Table of LUT

          IN[2]                    IN[1]               IN[0]                    OUT
          0                        0                   0                        TRUTH[0]
          0                        0                   1                        TRUTH[1]
          0                        1                   0                        TRUTH[2]
          0                        1                   1                        TRUTH[3]
          1                        0                   0                        TRUTH[4]
          1                        0                   1                        TRUTH[5]
          1                        1                   0                        TRUTH[6]
          1                        1                   1                        TRUTH[7]

41.6.2.4 Truth Table Inputs Selection

         Input Overview
         The inputs can be individually:
          • Masked
          • Driven by peripherals:
             – Analog comparator output (AC)
             – Timer/Counters waveform outputs (TC)
             – Serial Communication output transmit interface (SERCOM)
          • Driven by internal events from Event System
          • Driven by other CCL sub-modules
         The Input Selection for each input y of LUT x is configured by writing the Input y Source Selection bit in
         the LUT x Control register (LUTCTRLx.INSELy).

         Masked Inputs (MASK)
         When a LUT input is masked (LUTCTRLx.INSELy=MASK), the corresponding TRUTH input (IN) is
         internally tied to zero, as shown in this figure:




        © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1397
                                                   SAM D5x/E5x Family Data Sheet
                                                               CCL – Configurable Custom Logic

Figure 41-3. Masked Input Selection




Internal Feedback Inputs (FEEDBACK)
When selected (LUTCTRLx.INSELy=FEEDBACK), the Sequential (SEQ) output is used as input for the
corresponding LUT.
The output from an internal sequential sub-module can be used as input source for the LUT, see figure
below for an example for LUT0 and LUT1. The sequential selection for each LUT follows the formula:
IN 2N � = SEQ �
IN 2N+1 � = SEQ �
With N representing the sequencer number and i=0,1,2 representing the LUT input index.
For details, refer to 41.6.2.7 Sequential Logic.
Figure 41-4. Feedback Input Selection




Linked LUT (LINK)
When selected (LUTCTRLx.INSELy=LINK), the subsequent LUT output is used as the LUT input (e.g.,
LUT2 is the input for LUT1), as shown in this figure:




© 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 1398
                                                       SAM D5x/E5x Family Data Sheet
                                                                   CCL – Configurable Custom Logic

Figure 41-5. Linked LUT Input Selection




                                            LUT0        SEQ 0


                                                         CTRL
                                                       (ENABLE)


                                            LUT1




                                            LUT2        SEQ 1


                                                         CTRL
                                                       (ENABLE)


                                            LUT3




                                         LUT(2n – 2)    SEQ n


                                                         CTRL
                                                       (ENABLE)


                                          LUT(2n-1)




Internal Events Inputs Selection (EVENT)
Asynchronous events from the Event System can be used as input selection, as shown in the below
image. For each LUT, one event input line is available and can be selected on each LUT input. Before
enabling the event selection by writing LUTCTRLx.INSELy=EVENT, the Event System must be
configured first.
By default CCL includes an edge detector. When the event is received, an internal strobe is generated
when a rising edge is detected. The pulse duration is one GCLK_CCL clock cycle. The following steps
ensure proper operation:
  1.   Enable the GCLK_CCL clock.
  2.   Configure the Event System to route the event asynchronously.
  3.   Select the event input type (LUTCTRLx.INSEL).
  4.   If a strobe must be generated on the event input falling edge, write a '1' to the Inverted Event Input
       Enable bit in LUT Control register (LUTCTRLx.INVEI) .
  5.   Enable the event input by writing the Event Input Enable bit in LUT Control register
       (LUTCTRLx.LUTEI) to '1'.




© 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1399
                                                 SAM D5x/E5x Family Data Sheet
                                                               CCL – Configurable Custom Logic

Figure 41-6. Event Input Selection




I/O Pin Inputs (IO)
When the IO pin is selected as LUT input (LUTCTRLx.INSELy=IO), the corresponding LUT input will be
connected to the pin, as shown in the figure below.
Figure 41-7. I/O Pin Input Selection




Analog Comparator Inputs (AC)
The AC outputs can be used as input source for the LUT (LUTCTRLx.INSELy=AC).
The analog comparator outputs are distributed following the formula:
IN[N][i]=AC[N % ComparatorOutput_Number]
With N representing the LUT number and i=[0,1,2] representing the LUT input index.
Before selecting the comparator output, the AC must be configured first.
The output of comparator 0 is available on even LUTs ("LUT(2x)": LUT0, LUT2) and the comparator 1
output is available on odd LUTs ("LUT(2x+1)": LUT1, LUT3), as shown in the figure below.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1400
                                                          SAM D5x/E5x Family Data Sheet
                                                                      CCL – Configurable Custom Logic

Figure 41-8. AC Input Selection




Timer/Counter Inputs (TC)
The TC waveform output WO[0] can be used as input source for the LUT (LUTCTRLx.INSELy=TC). Only
consecutive instances of the TC, i.e. TCx and the subsequent TC(x+1), are available as default and
alternative TC selections (e.g., TC0 and TC1 are sources for LUT0, TC1 and TC2 are sources for LUT1,
etc). See the figure below for an example for LUT0. More general, the Timer/Counter selection for each
LUT follows the formula:
IN � � = ��������� � % TC_Instance_Number
IN � � = ������������� � + 1 % TC_Instance_Number
Where N represents the LUT number and i represents the LUT input index (i=0,1,2).
For devices with more than four TC instances, it is also possible to enable a second alternative option
(LUTCTRLx.INSEL=ALT2TC). This option is intended to relax the alternative pin function or PCB design
constraints when the default or the alternative TC instances are used for other purposes. When enabled,
the Timer/Counter selection for each LUT follows the formula:
IN � � = ������������������� � + 4 % TC_Instance_Number
Note that for not implemented TC_Instance_Number, the corresponding input is tied to ground.
Before selecting the waveform outputs, the TC must be configured first.
Figure 41-9. TC Input Selection




                                         TC0
                                         (default)         WO[0]



                                         TC1
                                       (alternative)       WO[0]



                                         TC4
                                                           WO[0]
                                   (second alternative)




© 2019 Microchip Technology Inc.                          Datasheet                  DS60001507E-page 1401
                                                SAM D5x/E5x Family Data Sheet
                                                               CCL – Configurable Custom Logic

Timer/Counter for Control Application Inputs (TCC)
The TCC waveform outputs can be used as input source for the LUT. Only WO[2:0] outputs can be
selected and routed to the respective LUT input (i.e., IN0 is connected to WO0, IN1 to WO1, and IN2 to
WO2), as shown in the figure below.
Note:
The TCC selection for each LUT follows the formula:
IN � � = ��� � % ��C_Instance_Number
Where N represents the LUT number.
Before selecting the waveform outputs, the TCC must be configured first.
Figure 41-10. TCC Input Selection




Serial Communication Output Transmit Inputs (SERCOM)
The serial engine transmitter output from Serial Communication Interface (SERCOM TX, TXd for USART,
MOSI for SPI) can be used as input source for the LUT. The figure below shows an example for LUT0
and LUT1. The SERCOM selection for each LUT follows the formula:
IN � � = ������[� % SERCOM_Instance_Number
With N representing the LUT number and i=0,1,2 representing the LUT input index.
Before selecting the SERCOM as input source, the SERCOM must be configured first: the SERCOM TX
signal must be output on SERCOMn/pad[0], which serves as input pad to the CCL.
Figure 41-11. SERCOM Input Selection




Related Links
6. I/O Multiplexing and Considerations
32. PORT - I/O Pin Controller
14. GCLK - Generic Clock Controller
46. AC – Analog Comparators
48. TC – Timer/Counter
49. TCC – Timer/Counter for Control Applications
33. SERCOM – Serial Communication Interface




© 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 1402
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                  CCL – Configurable Custom Logic

41.6.2.5 Filter
         By default, the LUT output is a combinatorial function of the LUT inputs. This may cause some short
         glitches when the inputs change value. These glitches can be removed by clocking through filters, if
         demanded by application needs.
         The Filter Selection bits in LUT Control register (LUTCTRLx.FILTSEL) define the synchronizer or digital
         filter options. When a filter is enabled, the OUT output will be delayed by two to five GCLK cycles. One
         APB clock after the corresponding LUT is disabled, all internal filter logic is cleared.
         Note: Events used as LUT input will also be filtered, if the filter is enabled.
         Figure 41-12. Filter

                                                                                            FILTSEL

                                      Input


                                                                                                      OUT

                                                                                        G
                                              D       Q   D       Q   D       Q     D       Q


                                                  R           R           R             R

                               GCLK_CCL
                                     CLR


41.6.2.6 Edge Detector
         The edge detector can be used to generate a pulse when detecting a rising edge on its input. To detect a
         falling edge, the TRUTH table should be inverted.
         The edge detector is enabled by writing '1' to the Edge Selection bit in LUT Control register
         (LUTCTRLx.EDGESEL). In order to avoid unpredictable behavior, either the filter or synchronizer must be
         enabled.
         Edge detection is disabled by writing a '0' to LUTCTRLx.EDGESEL. After disabling a LUT, the
         corresponding internal Edge Detector logic is cleared one APB clock cycle later.
         Figure 41-13. Edge Detector




41.6.2.7 Sequential Logic
         Each LUT pair can be connected to the internal sequential logic which can be configured to work as D flip
         flop, JK flip flop, gated D-latch or RS-latch by writing the Sequential Selection bits on the corresponding
         Sequential Control x register (SEQCTRLx.SEQSEL). Before using sequential logic, the GCLK_CCL clock
         and optionally each LUT filter or edge detector must be enabled.
         Note: While configuring the sequential logic, the even LUT must be disabled. When configured the even
         LUT must be enabled.




         © 2019 Microchip Technology Inc.                             Datasheet                             DS60001507E-page 1403
                                                     SAM D5x/E5x Family Data Sheet
                                                                   CCL – Configurable Custom Logic

Gated D Flip-Flop (DFF)
When the DFF is selected, the D-input is driven by the even LUT output (LUT0 and LUT2), and the G-
input is driven by the odd LUT output (LUT1 and LUT3), as shown in Figure 41-14.
Figure 41-14. D Flip Flop




When the even LUT is disabled (LUTCTRL0.ENABLE=0 / LUTCTRL2.ENABLE=0), the flip-flop is
asynchronously cleared. The reset command (R) is kept enabled for one APB clock cycle. In all other
cases, the flip-flop output (OUT) is refreshed on rising edge of the GCLK_CCL, as shown in Table 41-2.
Table 41-2. DFF Characteristics

 R          G           D          OUT
 1          X           X          Clear
 0          1           1          Set
                        0          Clear
            0           X          Hold state (no change)


JK Flip-Flop (JK)
When this configuration is selected, the J-input is driven by the even LUT output (LUT0 and LUT2), and
the K-input is driven by the odd LUT output (LUT1 and LUT3), as shown in Figure 41-15.
Figure 41-15. JK Flip Flop




When the even LUT is disabled (LUTCTRL0.ENABLE=0 / LUTCTRL2.ENABLE=0), the flip-flop is
asynchronously cleared. The reset command (R) is kept enabled for one APB clock cycle. In all other
cases, the flip-flop output (OUT) is refreshed on rising edge of the GCLK_CCL, as shown in Table 41-3.
Table 41-3. JK Characteristics

 R           J          K          OUT
 1           X          X          Clear
 0           0          0          Hold state (no change)
 0           0          1          Clear
 0           1          0          Set
 0           1          1          Toggle




© 2019 Microchip Technology Inc.                       Datasheet                   DS60001507E-page 1404
                                                               SAM D5x/E5x Family Data Sheet
                                                                           CCL – Configurable Custom Logic

         Gated D-Latch (DLATCH)
         When the DLATCH is selected, the D-input is driven by the even LUT output (LUT0 and LUT2), and the
         G-input is driven by the odd LUT output (LUT1 and LUT3), as shown in Figure 41-14.
         Figure 41-16. D-Latch

          even LUT             D      Q     OUT


              odd LUT          G
                                               When the even LUT is disabled (LUTCTRL0.ENABLE=0 /
         LUTCTRL2.ENABLE=0), the latch output will be cleared. The G-input is forced enabled for one more APB
         clock cycle, and the D-input to zero. In all other cases, the latch output (OUT) is refreshed as shown in
         Table 41-4.
         Table 41-4. D-Latch Characteristics

          G            D            OUT
          0            X            Hold state (no change)
          1            0            Clear
          1            1            Set


         RS Latch (RS)
         When this configuration is selected, the S-input is driven by the even LUT output (LUT0 and LUT2), and
         the R-input is driven by the odd LUT output (LUT1 and LUT3), as shown in Figure 41-17.
         Figure 41-17. RS-Latch

                                                  even LUT      S    Q       OUT

                                                     odd LUT    R

         When the even LUT is disabled LUTCTRL0.ENABLE=0 / LUTCTRL2.ENABLE=0), the latch output will be
         cleared. The R-input is forced enabled for one more APB clock cycle and S-input to zero. In all other
         cases, the latch output (OUT) is refreshed as shown in Table 41-5.
         Table 41-5. RS-Latch Characteristics

          S           R            OUT
          0           0            Hold state (no change)
          0           1            Clear
          1           0            Set
          1           1            Forbidden state

41.6.3   Events
         The CCL can generate the following output events:
           • OUTx: Lookup Table Output Value
         Writing a '1' to the LUT Control Event Output Enable bit (LUTCTRL.LUTEO) enables the corresponding
         output event. Writing a '0' to this bit disables the corresponding output event.




         © 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1405
                                                          SAM D5x/E5x Family Data Sheet
                                                                        CCL – Configurable Custom Logic

         The CCL can take the following actions on an input event:
           • INSELx: The event is used as input for the TRUTH table. For further details refer to 41.5.6 Events.
         Writing a '1' to the LUT Control Event Input Enable bit (LUTCTRL.LUTEI) enables the corresponding
         action on input event. Writing a '0' to this bit disables the corresponding action on input event.
         Related Links
         31. EVSYS – Event System

41.6.4   Sleep Mode Operation
         When using the GCLK_CCL internal clocking, writing the Run In Standby bit in the Control register
         (CTRL.RUNSTDBY) to '1' will allow GCLK_CCL to be enabled in Standby Sleep mode.
         If CTRL.RUNSTDBY=0, the GCLK_CCL will be disabled in Standby Sleep mode. If the Filter, Edge
         Detector or Sequential logic are enabled, the LUT output will be forced to zero in STANDBY mode. In all
         other cases, the TRUTH table decoder will continue operation and the LUT output will be refreshed
         accordingly.
         Related Links
         18. PM – Power Manager




         © 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1406
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    CCL – Configurable Custom Logic


41.7      Register Summary

 Offset        Name        Bit Pos.

 0x00          CTRL           7:0               RUNSTDBY                                                ENABLE   SWRST
 0x01
   ...       Reserved
 0x03
 0x04        SEQCTRL0         7:0                                                               SEQSEL[3:0]
 0x05        SEQCTRL1         7:0                                                               SEQSEL[3:0]
 0x06
   ...       Reserved
 0x07
                              7:0     EDGESEL                     FILTSEL[1:0]                          ENABLE
                             15:8                   INSELx[3:0]                                 INSELx[3:0]
 0x08        LUTCTRL0
                             23:16               LUTEO       LUTEI          INVEI               INSELx[3:0]
                             31:24                                               TRUTH[7:0]
                              7:0     EDGESEL                     FILTSEL[1:0]                          ENABLE
                             15:8                   INSELx[3:0]                                 INSELx[3:0]
 0x0C        LUTCTRL1
                             23:16               LUTEO       LUTEI          INVEI               INSELx[3:0]
                             31:24                                               TRUTH[7:0]
                              7:0     EDGESEL                     FILTSEL[1:0]                          ENABLE
                             15:8                   INSELx[3:0]                                 INSELx[3:0]
 0x10        LUTCTRL2
                             23:16               LUTEO       LUTEI          INVEI               INSELx[3:0]
                             31:24                                               TRUTH[7:0]
                              7:0     EDGESEL                     FILTSEL[1:0]                          ENABLE
                             15:8                   INSELx[3:0]                                 INSELx[3:0]
 0x14        LUTCTRL3
                             23:16               LUTEO       LUTEI          INVEI               INSELx[3:0]
                             31:24                                               TRUTH[7:0]




41.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 41.5.8 Register Access Protection.
          Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
          Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




          © 2019 Microchip Technology Inc.                           Datasheet                       DS60001507E-page 1407
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                      CCL – Configurable Custom Logic

41.8.1         Control

               Name:         CTRL
               Offset:       0x00
               Reset:        0x00
               Property:     PAC Write-Protection


         Bit         7               6              5              4              3                2     1            0
                               RUNSTDBY                                                                ENABLE       SWRST
   Access                          R/W                                                                  R/W           W
    Reset                            0                                                                   0            0


               Bit 6 – RUNSTDBY Run in Standby
               This bit indicates if the GCLK_CCL clock must be kept running in standby mode. The setting is ignored
               for configurations where the generic clock is not required. For details refer to 41.6.4 Sleep Mode
               Operation.


                             Important: This bit must be written before enabling the CCL.




               Value        Description
               0            Generic clock is not required in standby sleep mode.
               1            Generic clock is required in standby sleep mode.

               Bit 1 – ENABLE Enable
               Value      Description
               0          The peripheral is disabled.
               1          The peripheral is enabled.

               Bit 0 – SWRST Software Reset
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit resets all registers in the CCL to their initial state.
               Value         Description
               0             There is no reset operation ongoing.
               1             The reset operation is ongoing.




           © 2019 Microchip Technology Inc.                              Datasheet                       DS60001507E-page 1408
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                CCL – Configurable Custom Logic

41.8.2         Sequential Control x

               Name:       SEQCTRL
               Offset:     0x04 + n*0x01 [n=0..1]
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6             5            4             3           2                 1            0
                                                                                           SEQSEL[3:0]
   Access                                                                 R/W         R/W            R/W             R/W
    Reset                                                                  0           0                 0            0


               Bits 3:0 – SEQSEL[3:0] Sequential Selection
               These bits select the sequential configuration:
               Sequential Selection
                Value      Name                       Description
                0x0        DISABLE                    Sequential logic is disabled
                0x1        DFF                        D flip flop
                0x2        JK                         JK flip flop
                0x3        LATCH                      D latch
                0x4        RS                         RS latch
                0x5 -                                 Reserved
                0xF




           © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 1409
                                                                                SAM D5x/E5x Family Data Sheet
                                                                                                  CCL – Configurable Custom Logic

41.8.3         LUT Control x

               Name:        LUTCTRL
               Offset:      0x08 + n*0x04 [n=0..3]
               Reset:       0x00000000
               Property:    PAC Write-Protection, Enable-protected


         Bit        31             30                 29                  28                27          26                  25           24
                                                                               TRUTH[7:0]
   Access           R/W           R/W                 R/W             R/W                   R/W         R/W                 R/W         R/W
    Reset            0             0                   0                  0                  0           0                   0           0


         Bit        23             22                 21                  20                19          18                  17           16
                                LUTEO             LUTEI              INVEI                                    INSELx[3:0]
   Access                         R/W                 R/W             R/W                   R/W         R/W                 R/W         R/W
    Reset                          0                   0                  0                  0           0                   0           0


         Bit        15             14                 13                  12                11          10                   9           8
                                        INSELx[3:0]                                                           INSELx[3:0]
   Access           R/W           R/W                 R/W             R/W                   R/W         R/W                 R/W         R/W
    Reset            0             0                   0                  0                  0           0                   0           0


         Bit         7             6                   5                  4                  3           2                   1           0
                 EDGESEL                                   FILTSEL[1:0]                                               ENABLE
   Access           R/W                               R/W             R/W                                                   R/W
    Reset            0                                 0                  0                                                  0


               Bits 31:24 – TRUTH[7:0] Truth Table
               These bits define the value of truth logic as a function of inputs IN[2:0].

               Bit 22 – LUTEO LUT Event Output Enable
               Value      Description
               0          LUT event output is disabled.
               1          LUT event output is enabled.

               Bit 21 – LUTEI LUT Event Input Enable
               Value      Description
               0          LUT incoming event is disabled.
               1          LUT incoming event is enabled.

               Bit 20 – INVEI Inverted Event Input Enable
               Value       Description
               0           Incoming event is not inverted.
               1           Incoming event is inverted.

               Bit 7 – EDGESEL Edge Selection
               Value      Description
               0          Edge detector is disabled.
               1          Edge detector is enabled.




           © 2019 Microchip Technology Inc.                                       Datasheet                                 DS60001507E-page 1410
                                                 SAM D5x/E5x Family Data Sheet
                                                              CCL – Configurable Custom Logic

Bits 5:4 – FILTSEL[1:0] Filter Selection
These bits select the LUT output filter options:
Filter Selection
 Value       Name                           Description
 0x0         DISABLE                        Filter disabled
 0x1         SYNCH                          Synchronizer enabled
 0x2         FILTER                         Filter enabled
 0x3         -                              Reserved

Bit 1 – ENABLE LUT Enable
Value      Description
0          The LUT is disabled.
1          The LUT is enabled.

Bits 19:16,15:12,11:8 – INSELx LUT Input x Source Selection
These bits select the LUT input x source:
 Value      Name                          Description
 0x0        MASK                          Masked input
 0x1        FEEDBACK                      Feedback input source
 0x2        LINK                          Linked LUT input source
 0x3        EVENT                         Event input source
 0x4        IO                            I/O pin input source
 0x5        AC                            AC input source
 0x6        TC                            TC input source
 0x7        ALTTC                         Alternative TC input source
 0x8        TCC                           TCC input source
 0x9        SERCOM                        SERCOM input source




© 2019 Microchip Technology Inc.                  Datasheet                  DS60001507E-page 1411
