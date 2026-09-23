# 32. PORT - I/O Pin Controller

*Source: `Atmel-SAMD51.pdf`, pages 883-912 — SAMD51 family datasheet*

                                                         SAM D5x/E5x Family Data Sheet
                                                                                  PORT - I/O Pin Controller


32.    PORT - I/O Pin Controller

32.1   Overview
       The I/O Pin Controller (PORT) controls the I/O pins of the device. The I/O pins are organized in a series
       of groups, collectively referred to as a PORT group. Each PORT group can have up to 32 pins that can
       be configured and controlled individually or as a group. The number of PORT groups on a device may
       depend on the package or number of pins. Each pin may either be used for general purpose I/O under
       direct application control or be assigned to an embedded device peripheral. When used for general
       purpose I/O, each pin can be configured as input or output, with a highly configurable driver and pull
       settings.
       All I/O pins have true read-modify-write functionality when used for general purpose I/O. The direction or
       the output value of one or more pins may be changed (set, Reset or toggled) explicitly without
       unintentionally changing the state of any other pins in the same port group by a single, atomic 8-, 16- or
       32-bit write.
       The PORT is connected to the high-speed bus matrix through an AHB/APB bridge.



32.2   Features
         • Selectable Input and Output Configuration for Each Individual Pin
         • Software-controlled Multiplexing of Peripheral Functions on I/O Pins
         • Flexible Pin Configuration Through a Dedicated Pin Configuration Register
         • Configurable Output Driver and Pull Settings:
             – Totem-pole (push-pull)
             – Pull configuration
             – Driver strength
         • Configurable Input Buffer and Pull Settings:
             – Internal pull-up or pull-down
             – Input sampling criteria
             – Input buffer can be disabled if not needed for lower power consumption
             – Read-Modify-Write support for output value (OUTCLR/OUTSET/OUTGL) and pin direction
               (DIRCLR/DIRSET/DIRTGL)
         • Input Event:
             – Up to four input event pins for each PORT group
             – SET/CLEAR/TOGGLE event actions for each event input on output value of a pin
             – Can be output to pin




       © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 883
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                        PORT - I/O Pin Controller


32.3     Block Diagram
         Figure 32-1. PORT Block Diagram
                                                     PORT

                                                                        Peripheral Mux Select

                                                        Control
                                                          and          Port Line
                                                                       Bundles
                                                        Status
                                                                                             Pad Line
                                                                                             Bundles




                                                                                   PORTMUX
                                                        IP Line Bundles                                     I/O
                                                                                                           PADS


                         PERIPHERALS                                                                           Analog Pad
                                                                                                               Connections

                                                       Digital Controls of Analog Blocks
                                                                                                         ANALOG
                                                                                                         BLOCKS




32.4     Signal Description
         Table 32-1. Signal Description for PORT

          Signal name                  Type                 Description
          Pxy                          Digital I/O          General purpose I/O pin y in group x

         Refer to the I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One
         signal can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



32.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly as follows.

32.5.1   I/O Lines
         The I/O lines of the PORT are mapped to pins of the physical device. The following naming scheme is
         used:
         Each line bundle with up to 32 lines is assigned an identifier 'xy', with letter x=A, B, C… and two-digit
         number y=00, 01, …31. Examples: A24, C03.
         PORT pins are labeled 'Pxy' accordingly, for example PA24, PC03. This identifies each pin in the device
         uniquely.
         Each pin may be controlled by one or more peripheral multiplexer settings, which allows the pad to be
         routed internally to a dedicated peripheral function. When the setting is enabled, the selected peripheral




         © 2019 Microchip Technology Inc.                            Datasheet                                    DS60001507E-page 884
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      PORT - I/O Pin Controller

         has control over the Output state of the pad, as well as the ability to read the current Physical Pad state.
         Refer to I/O Multiplexing and Considerations for details.
         Device-specific configurations may cause some lines (and the corresponding Pxy pin) not to be
         implemented.
         Related Links
         6. I/O Multiplexing and Considerations

32.5.2   Power Management
         During Reset, all PORT lines are configured as inputs with input buffers, output buffers and pull disabled.
         When the device is set to the BACKUP sleep mode, even if the PORT configuration registers and input
         synchronizers will lose their contents (these will not be restored when PORT is powered up again), the
         latches in the pads will keep their current configuration, such as the output value and pull settings. Refer
         to the Power Manager documentation for more features related to the I/O lines configuration in and out of
         BACKUP mode.
         The PORT peripheral will continue operating in any Sleep mode where its source clock is running.
         Related Links
         18.6.3.4 I/O Lines Retention in HIBERNATE or BACKUP Mode

32.5.3   Clocks
         The PORT bus clock (CLK_PORT_APB) can be enabled and disabled in the Main Clock module, and the
         default state of CLK_PORT_APB can be found in the Peripheral Clock Masking section in MCLK – Main
         Clock.
         The PORT requires an APB clock, which may be divided from the CPU main clock and allows the CPU to
         access the registers of PORT through the high-speed matrix and the AHB/APB bridge.
         One clock cycle latency can be observed on the APB access in case of concurrent PORT accesses.
         Related Links
         15. MCLK – Main Clock

32.5.4   DMA
         Not applicable.

32.5.5   Interrupts
         Not applicable.

32.5.6   Events
         The events of this peripheral are connected to the Event System.
         The output of an event to a pin through PORT is always asynchronous. This must be configured in the
         Event System by writing ASYNCHRONOUS to the Path Selection bits in the respective Channel n Control
         register of the Event System (EVSYS.CHANNELn.PATH).
         Related Links
         31. EVSYS – Event System

32.5.7   Debug Operation
         When the CPU is halted in Debug mode, this peripheral will continue normal operation.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 885
                                                                             SAM D5x/E5x Family Data Sheet
                                                                                                         PORT - I/O Pin Controller

32.5.8   Register Access Protection
         All registers with write access can be optionally write-protected by the Peripheral Access Controller
         (PAC).
         Note: Optional write protection is indicated by the "PAC Write Protection" property in the register
         description.
         Write protection does not apply for accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller

32.5.9   Analog Connections
         Analog functions are connected directly between the analog blocks and the I/O pads using analog buses.
         However, selecting an analog peripheral function for a given pin will disable the corresponding digital
         features of the pad.



32.6     Functional Description
         Figure 32-2. Overview of the PORT

                                                                      PORT                                        PAD

                                                                              PULLEN
                                                    PULLENx

                                                                              DRIVE
                                                    DRIVEx
                                                                                                               Pull
                                                                                                               Resistor
                                                                              OUT                PG
                                                        OUTx                                                     PAD
                                                                                          VDD
                          APB Bus




                                                                              OE                 NG
                                                        DIRx

                                                                              INEN
                                                        INENx

                                    INx                                       IN
                                            Q       D     Q       D



                                                R             R


                                                Synchronizer


                                                          Input to Other Modules   Analog Input/Output


32.6.1   Principle of Operation
         Each PORT group of up to 32 pins is controlled by the registers in PORT, as described in the figure.
         These registers in PORT are duplicated for each PORT group, with increasing base addresses. The
         number of PORT groups may depend on the package/number of pins.




         © 2019 Microchip Technology Inc.                                    Datasheet                             DS60001507E-page 886
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                           PORT - I/O Pin Controller

          Figure 32-3. Overview of the peripheral functions multiplexing
                                         PORT bit y                             PORTMUX

                                 Port y PINCFG         Port y Peripheral
                                   PMUXEN              Mux Enable
                                                       Port y Line Bundle
                                     Port y                                        0
                                  Data+Config
                                     Port y            Port y PMUX Select
                                   PMUX[3:0]
                                                                                                         PAD y
                                                                                           Pad y

                                                                                           Line Bundle
                                Periph Signal 0                             0

                                Periph Signal 1                             1
                                                                                   1
                               Peripheral Signals to
                               be muxed to Pad y


                               Periph Signal 15                             15

          The I/O pins of the device are controlled by PORT peripheral registers. Each port pin has a corresponding
          bit in the Data Direction (DIR) and Data Output Value (OUT) registers to enable that pin as an output and
          to define the Output state.
          The direction of each pin in a PORT group is configured by the DIR register. If a bit in DIR is set to '1', the
          corresponding pin is configured as an output pin. If a bit in DIR is set to '0', the corresponding pin is
          configured as an input pin.
          When the direction is set as output, the corresponding bit in the OUT register will set the level of the pin.
          If bit y in OUT is written to '1', pin y is driven HIGH. If bit y in OUT is written to '0', pin y is driven LOW. Pin
          configuration can be set by Pin Configuration (PINCFGy) registers, with y=00, 01, ..31 representing the
          bit position.
          The Data Input Value (IN) is set as the input value of a port pin with resynchronization to the PORT clock.
          To reduce power consumption, these input synchronizers can be clocked only when system requires
          reading the input value, as specified in the SAMPLING field of the Control register (CTRL). The value of
          the pin can always be read, whether the pin is configured as input or output. If the Input Enable bit in the
          Pin Configuration registers (PINCFGy.INEN) is '0', the input value will not be sampled.
          In PORT, the Peripheral Multiplexer Enable bit in the PINCFGy register (PINCFGy.PMUXEN) can be
          written to '1' to enable the connection between peripheral functions and individual I/O pins. The
          Peripheral Multiplexing n (PMUXn) registers select the peripheral function for the corresponding pin. This
          will override the connection between the PORT and that I/O pin, and connect the selected peripheral
          signal to the particular I/O pin instead of the PORT line bundle.

32.6.2    Basic Operation

32.6.2.1 Initialization
          After reset, all standard function device I/O pads are connected to the PORT with outputs tri-stated and
          input buffers disabled, even if there is no clock running.
          However, specific pins, such as those used for connection to a debugger, may be configured differently,
          as required by their special function.




         © 2019 Microchip Technology Inc.                             Datasheet                           DS60001507E-page 887
                                                             SAM D5x/E5x Family Data Sheet
                                                                                        PORT - I/O Pin Controller

32.6.2.2 Operation
         Each I/O pin Pxy can be controlled by the registers in PORT. Each PORT group x has its own set of
         PORT registers, with a base address at byte address (PORT + 0x80 * group index) (A corresponds to
         group index 0, B to 1, etc...). Within that set of registers, the pin index is y, from 0 to 31.
         Refer to I/O Multiplexing and Considerations for details on available pin configuration and PORT groups.

         Configuring Pins as Output
         To use pin Pxy as an output, write bit y of the DIR register to '1'. This can also be done by writing bit y in
         the DIRSET register to '1' - this will avoid disturbing the configuration of other pins in that group. The y bit
         in the OUT register must be written to the desired output value.
         Similarly, writing an OUTSET bit to '1' will set the corresponding bit in the OUT register to '1'. Writing a bit
         in OUTCLR to '1' will set that bit in OUT to zero. Writing a bit in OUTTGL to '1' will toggle that bit in OUT.

         Configuring Pins as Input
         To use pin Pxy as an input, bit y in the DIR register must be written to '0'. This can also be done by writing
         bit y in the DIRCLR register to '1' - this will avoid disturbing the configuration of other pins in that group.
         The input value can be read from bit y in register IN as soon as the INEN bit in the Pin Configuration
         register (PINCFGy.INEN) is written to '1'.
         By default, the input synchronizer is clocked only when an input read is requested. This will delay the
         read operation by two cycles of the PORT clock. To remove the delay, the input synchronizers for each
         PORT group of eight pins can be configured to be always active, but this will increase power
         consumption. This is enabled by writing '1' to the corresponding SAMPLINGn bit field of the CTRL
         register, see CTRL.SAMPLING for details.

         Using Alternative Peripheral Functions
         To use pin Pxy as one of the available peripheral functions, the corresponding PMUXEN bit of the
         PINCFGy register must be '1'. The PINCFGy register for pin Pxy is at byte offset (PINCFG0 + y).
         The peripheral function can be selected by setting the PMUXO or PMUXE in the PMUXn register. The
         PMUXO/PMUXE is at byte offset PMUX0 + (y/2). The chosen peripheral must also be configured and
         enabled.
         Related Links
         6. I/O Multiplexing and Considerations

32.6.3   I/O Pin Configuration
         The Pin Configuration register (PINCFGy) is used for additional I/O pin configuration. A pin can be set in
         a totem-pole or pull configuration.
         As pull configuration is done through the Pin Configuration register, all intermediate PORT states during
         switching of pin direction and pin values are avoided.
         The I/O pin configurations are described further in this chapter, and summarized in Table 32-2.
32.6.3.1 Pin Configurations Summary
         Table 32-2. Pin Configurations Summary

          DIR       INEN        PULLEN        OUT        Configuration
          0         0           0             X          Reset or analog I/O: all digital disabled




         © 2019 Microchip Technology Inc.                      Datasheet                             DS60001507E-page 888
                                                             SAM D5x/E5x Family Data Sheet
                                                                                          PORT - I/O Pin Controller

         ...........continued
         DIR       INEN         PULLEN             OUT   Configuration
         0         0            1                  0     Pull-down; input disabled
         0         0            1                  1     Pull-up; input disabled
         0         1            0                  X     Input
         0         1            1                  0     Input with pull-down
         0         1            1                  1     Input with pull-up
         1         0            X                  X     Output; input disabled
         1         1            X                  X     Output; input enabled

32.6.3.2 Input Configuration
         Figure 32-4. I/O configuration - Standard Input
                                           PULLEN                       PULLEN     INEN   DIR
                                                                              0     1      0


                                            DIR

                                            OUT


                                             IN

                                            INEN

         Figure 32-5. I/O Configuration - Input with Pull
                                           PULLEN                       PULLEN     INEN   DIR
                                                                              1     1      0


                                            DIR

                                            OUT


                                             IN

                                            INEN

         Note: When pull is enabled, the pull value is defined by the OUT value.
32.6.3.3 Totem-Pole Output
         When configured for totem-pole (push-pull) output, the pin is driven low or high according to the
         corresponding bit setting in the OUT register. In this configuration there is no current limitation for sink or
         source other than what the pin is capable of. If the pin is configured for input, the pin will float if no
         external pull is connected.
         Note: Enabling the output driver will automatically disable pull.




        © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 889
                                                           SAM D5x/E5x Family Data Sheet
                                                                                      PORT - I/O Pin Controller

         Figure 32-6. I/O Configuration - Totem-Pole Output with Disabled Input
                                            PULLEN                   PULLEN    INEN   DIR
                                                                           0    0      1


                                             DIR

                                             OUT


                                              IN

                                             INEN

         Figure 32-7. I/O Configuration - Totem-Pole Output with Enabled Input
                                            PULLEN                   PULLEN    INEN   DIR
                                                                           0    1      1


                                             DIR

                                             OUT


                                              IN

                                             INEN

         Figure 32-8. I/O Configuration - Output with Pull
                                            PULLEN                   PULLEN    INEN   DIR
                                                                           1    0      0


                                             DIR

                                             OUT


                                              IN

                                             INEN


32.6.3.4 Digital Functionality Disabled
         Neither Input nor Output functionality are enabled.
         Figure 32-9. I/O Configuration - Reset or Analog I/O: Digital Output, Input and Pull Disabled
                                            PULLEN                   PULLEN    INEN   DIR
                                                                           0    0      0


                                             DIR

                                             OUT


                                              IN

                                             INEN


32.6.4   Events
         The PORT allows input events to control individual I/O pins. These input events are generated by the
         EVSYS module and can originate from a different clock domain than the PORT module.
         The PORT can perform the following actions:




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 890
                                                            SAM D5x/E5x Family Data Sheet
                                                                                      PORT - I/O Pin Controller

           • Output (OUT): I/O pin will be set when the incoming event has a high level ('1') and cleared when the
             incoming event has a low-level ('0').
           • Set (SET): I/O pin will be set when an incoming event is detected.
           • Clear (CLR): I/O pin will be cleared when an incoming event is detected.
           • Toggle (TGL): I/O pin will toggle when an incoming event is detected.
         The event is output to pin without any internal latency. For SET, CLEAR and TOGGLE event actions, the
         action will be executed up to three clock cycles after a rising edge.
         The event actions can be configured with the Event Action m bit group in the Event Input Control
         register( EVCTRL.EVACTm). Writing a '1' to a PORT Event Enable Input m of the Event Control register
         (EVCTRL.PORTEIm) enables the corresponding action on input event. Writing '0' to this bit disables the
         corresponding action on input event. Note that several actions can be enabled for incoming events. If
         several events are connected to the peripheral, any enabled action will be taken for any of the incoming
         events. Refer to EVSYS – Event System. for details on configuring the Event System.
         Each event input can address one and only one I/O pin at a time. The selection of the pin is indicated by
         the PORT Event Pin Identifier of the Event Input Control register (EVCTR.PIDn). On the other hand, one
         I/O pin can be addressed by up to four different input events. To avoid action conflict on the output value
         of the register (OUT) of this particular I/O pin, only one action is performed according to the table below.
         Note that this truth table can be applied to any SET/CLR/TGL configuration from two to four active input
         events.
         Table 32-3. Priority on Simultaneous SET/CLR/TGL Event Actions

          EVACT0             EVACT1           EVACT2        EVACT3          Executed Event Action
          SET                SET              SET           SET             SET
          CLR                CLR              CLR           CLR             CLR
          All Other Combinations                                            TGL

         Be careful when the event is output to pin. Due to the fact the events are received asynchronously, the
         I/O pin may have unpredictable levels, depending on the timing of when the events are received. When
         several events are output to the same pin, the lowest event line will get the access. All other events will
         be ignored.
         Related Links
         31. EVSYS – Event System

32.6.5   PORT Access Priority
         The PORT is accessed by different systems:
           • The ARM® CPU through the high-speed matrix and the AHB/APB bridge (APB)
           • EVSYS through four asynchronous input events
         The following priority is adopted:
           1.   APB
           2.   EVSYS input events, except for events with EVCTRL.EVACTn=OUT, where the output pin directly
                follows the event input signal, independently of the OUT register value.
         For input events that require different actions on the same I/O pin, refer to 32.6.4 Events.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 891
                                                           SAM D5x/E5x Family Data Sheet
                                                                                    PORT - I/O Pin Controller


32.7      Register Summary
          The I/O pins are assembled in pin groups with up to 32 pins. Group 0 consists of the PA pins, and group 1
          is for the PB pins, etc. Each pin group has its own PORT registers, with a 0x80 address spacing. For
          example, the register address offset for the Data Direction (DIR) register for group 0 (PA00 to PA31) is
          0x00, and the register address offset for the DIR register for group 1 (PB00 to PB31) is 0x80.

 Offset        Name        Bit Pos.

                              7:0                                     DIR[7:0]
                             15:8                                     DIR[15:8]
 0x00           DIR
                             23:16                                   DIR[23:16]
                             31:24                                   DIR[31:24]
                              7:0                                    DIRCLR[7:0]
                             15:8                                   DIRCLR[15:8]
 0x04         DIRCLR
                             23:16                                  DIRCLR[23:16]
                             31:24                                  DIRCLR[31:24]
                              7:0                                    DIRSET[7:0]
                             15:8                                   DIRSET[15:8]
 0x08         DIRSET
                             23:16                                  DIRSET[23:16]
                             31:24                                  DIRSET[31:24]
                              7:0                                    DIRTGL[7:0]
                             15:8                                   DIRTGL[15:8]
 0x0C         DIRTGL
                             23:16                                  DIRTGL[23:16]
                             31:24                                  DIRTGL[31:24]
                              7:0                                     OUT[7:0]
                             15:8                                     OUT[15:8]
 0x10          OUT
                             23:16                                   OUT[23:16]
                             31:24                                   OUT[31:24]
                              7:0                                   OUTCLR[7:0]
                             15:8                                   OUTCLR[15:8]
 0x14         OUTCLR
                             23:16                                 OUTCLR[23:16]
                             31:24                                 OUTCLR[31:24]
                              7:0                                   OUTSET[7:0]
                             15:8                                   OUTSET[15:8]
 0x18         OUTSET
                             23:16                                 OUTSET[23:16]
                             31:24                                 OUTSET[31:24]
                              7:0                                   OUTTGL[7:0]
                             15:8                                   OUTTGL[15:8]
 0x1C         OUTTGL
                             23:16                                 OUTTGL[23:16]
                             31:24                                 OUTTGL[31:24]
                              7:0                                      IN[7:0]
                             15:8                                      IN[15:8]
 0x20           IN
                             23:16                                    IN[23:16]
                             31:24                                    IN[31:24]




          © 2019 Microchip Technology Inc.                  Datasheet                          DS60001507E-page 892
                                                                       SAM D5x/E5x Family Data Sheet
                                                                                              PORT - I/O Pin Controller

...........continued

  Offset               Name     Bit Pos.

                                  7:0                                        SAMPLING[7:0]
                                 15:8                                       SAMPLING[15:8]
   0x24                 CTRL
                                 23:16                                      SAMPLING[23:16]
                                 31:24                                      SAMPLING[31:24]
                                  7:0                                        PINMASK[7:0]
                                 15:8                                        PINMASK[15:8]
   0x28           WRCONFIG
                                 23:16               DRVSTR                                    PULLEN        INEN     PMUXEN
                                 31:24     HWSEL     WRPINCFG             WRPMUX                     PMUX[3:0]
                                  7:0      PORTEIx       EVACTx[1:0]                           PIDx[4:0]
                                 15:8      PORTEIx       EVACTx[1:0]                           PIDx[4:0]
   0x2C                EVCTRL
                                 23:16     PORTEIx       EVACTx[1:0]                           PIDx[4:0]
                                 31:24     PORTEIx       EVACTx[1:0]                           PIDx[4:0]
   0x30                PMUX0      7:0                    PMUXO[3:0]                                 PMUXE[3:0]
     ...
   0x3F                PMUX15     7:0                    PMUXO[3:0]                                 PMUXE[3:0]
   0x40            PINCFG0        7:0                DRVSTR                                    PULLEN        INEN     PMUXEN
     ...
   0x5F            PINCFG31       7:0                DRVSTR                                    PULLEN        INEN     PMUXEN




32.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to 32.5.8 Register Access Protection.




              © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 893
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                             PORT - I/O Pin Controller

32.8.1         Data Direction

               Name:        DIR
               Offset:      0x00
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to configure one or more I/O pins as an input or output. This register can be
               manipulated without doing a read-modify-write operation by using the Data Direction Toggle (DIRTGL),
               Data Direction Clear (DIRCLR) and Data Direction Set (DIRSET) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31            30           29            28                27       26            25           24
                                                                  DIR[31:24]
   Access           RW           RW            RW           RW                 RW       RW           RW            RW
    Reset            0            0             0            0                 0         0            0             0


         Bit        23            22           21            20                19       18            17           16
                                                                  DIR[23:16]
   Access           RW           RW            RW           RW                 RW       RW           RW            RW
    Reset            0            0             0            0                 0         0            0             0


         Bit        15            14           13            12                11       10            9             8
                                                                  DIR[15:8]
   Access           RW           RW            RW           RW                 RW       RW           RW            RW
    Reset            0            0             0            0                 0         0            0             0


         Bit         7            6             5            4                 3         2            1             0
                                                                   DIR[7:0]
   Access           RW           RW            RW           RW                 RW       RW           RW            RW
    Reset            0            0             0            0                 0         0            0             0


               Bits 31:0 – DIR[31:0] Port Data Direction
               These bits set the data direction for the individual I/O pins in the PORT group.
                Value      Description
                0          The corresponding I/O pin in the PORT group is configured as an input.
                1          The corresponding I/O pin in the PORT group is configured as an output.




           © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 894
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                PORT - I/O Pin Controller

32.8.2         Data Direction Clear

               Name:        DIRCLR
               Offset:      0x04
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to set one or more I/O pins as an input, without doing a read-modify-write
               operation. Changes in this register will also be reflected in the Data Direction (DIR), Data Direction Toggle
               (DIRTGL) and Data Direction Set (DIRSET) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31             30            29            28                 27       26            25            24
                                                                DIRCLR[31:24]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


         Bit        23             22            21            20                 19       18            17            16
                                                                DIRCLR[23:16]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


         Bit        15             14            13            12                 11       10             9             8
                                                                   DIRCLR[15:8]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


         Bit         7             6             5             4                  3        2              1             0
                                                                    DIRCLR[7:0]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


               Bits 31:0 – DIRCLR[31:0] Port Data Direction Clear
               Writing a '0' to a bit has no effect.
               Writing a '1' to a bit will clear the corresponding bit in the DIR register, which configures the I/O pin as an
               input.
                Value        Description
                0            The corresponding I/O pin in the PORT group will keep its configuration.
                1            The corresponding I/O pin in the PORT group is configured as input.




           © 2019 Microchip Technology Inc.                            Datasheet                          DS60001507E-page 895
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                PORT - I/O Pin Controller

32.8.3         Data Direction Set

               Name:        DIRSET
               Offset:      0x08
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to set one or more I/O pins as an output, without doing a read-modify-write
               operation. Changes in this register will also be reflected in the Data Direction (DIR), Data Direction Toggle
               (DIRTGL) and Data Direction Clear (DIRCLR) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31             30            29            28                  27      26            25            24
                                                                   DIRSET[31:24]
   Access           RW            RW            RW            RW                  RW      RW            RW             RW
    Reset            0             0             0             0                   0       0              0             0


         Bit        23             22            21            20                  19      18            17            16
                                                                   DIRSET[23:16]
   Access           RW            RW            RW            RW                  RW      RW            RW             RW
    Reset            0             0             0             0                   0       0              0             0


         Bit        15             14            13            12                  11      10             9             8
                                                                    DIRSET[15:8]
   Access           RW            RW            RW            RW                  RW      RW            RW             RW
    Reset            0             0             0             0                   0       0              0             0


         Bit         7             6             5             4                   3       2              1             0
                                                                    DIRSET[7:0]
   Access           RW            RW            RW            RW                  RW      RW            RW             RW
    Reset            0             0             0             0                   0       0              0             0


               Bits 31:0 – DIRSET[31:0] Port Data Direction Set
               Writing '0' to a bit has no effect.
               Writing '1' to a bit will set the corresponding bit in the DIR register, which configures the I/O pin as an
               output.
                Value        Description
                0            The corresponding I/O pin in the PORT group will keep its configuration.
                1            The corresponding I/O pin in the PORT group is configured as an output.




           © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 896
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                                PORT - I/O Pin Controller

32.8.4         Data Direction Toggle

               Name:        DIRTGL
               Offset:      0x0C
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to toggle the direction of one or more I/O pins, without doing a read-modify-
               write operation. Changes in this register will also be reflected in the Data Direction (DIR), Data Direction
               Set (DIRSET) and Data Direction Clear (DIRCLR) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31             30            29            28                  27      26            25            24
                                                                   DIRTGL[31:24]
   Access           RW            RW            RW            RW                  RW       RW            RW            RW
    Reset            0             0             0             0                   0        0             0             0


         Bit        23             22            21            20                  19      18            17            16
                                                                   DIRTGL[23:16]
   Access           RW            RW            RW            RW                  RW       RW            RW            RW
    Reset            0             0             0             0                   0        0             0             0


         Bit        15             14            13            12                  11      10             9             8
                                                                    DIRTGL[15:8]
   Access           RW            RW            RW            RW                  RW       RW            RW            RW
    Reset            0             0             0             0                   0        0             0             0


         Bit         7             6             5             4                   3        2             1             0
                                                                    DIRTGL[7:0]
   Access           RW            RW            RW            RW                  RW       RW            RW            RW
    Reset            0             0             0             0                   0        0             0             0


               Bits 31:0 – DIRTGL[31:0] Port Data Direction Toggle
               Writing '0' to a bit has no effect.
               Writing '1' to a bit will toggle the corresponding bit in the DIR register, which reverses the direction of the
               I/O pin.
                Value        Description
                0            The corresponding I/O pin in the PORT group will keep its configuration.
                1            The direction of the corresponding I/O pin is toggled.




           © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 897
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                              PORT - I/O Pin Controller

32.8.5         Data Output Value

               Name:        OUT
               Offset:      0x10
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register sets the data output drive value for the individual I/O pins in the PORT.
               This register can be manipulated without doing a read-modify-write operation by using the Data Output
               Value Clear (OUTCLR), Data Output Value Set (OUTSET), and Data Output Value Toggle (OUTTGL)
               registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31            30            29            28                27       26              25          24
                                                                   OUT[31:24]
   Access           RW            RW           RW            RW                 RW       RW              RW         RW
    Reset            0             0            0             0                 0         0              0           0


         Bit        23            22            21            20                19       18              17          16
                                                                   OUT[23:16]
   Access           RW            RW           RW            RW                 RW       RW              RW         RW
    Reset            0             0            0             0                 0         0              0           0


         Bit        15            14            13            12                11       10              9           8
                                                                   OUT[15:8]
   Access           RW            RW           RW            RW                 RW       RW              RW         RW
    Reset            0             0            0             0                 0         0              0           0


         Bit         7             6            5             4                 3         2              1           0
                                                                    OUT[7:0]
   Access           RW            RW           RW            RW                 RW       RW              RW         RW
    Reset            0             0            0             0                 0         0              0           0


               Bits 31:0 – OUT[31:0] PORT Data Output Value
               For pins configured as outputs via the Data Direction register (DIR), these bits set the logical output drive
               level.
               For pins configured as inputs via the Data Direction register (DIR) and with pull enabled via the Pull
               Enable bit in the Pin Configuration register (PINCFG.PULLEN), these bits will set the input pull direction.
                Value       Description
                0           The I/O pin output is driven low, or the input is connected to an internal pull-down.
                1           The I/O pin output is driven high, or the input is connected to an internal pull-up.




           © 2019 Microchip Technology Inc.                           Datasheet                          DS60001507E-page 898
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                               PORT - I/O Pin Controller

32.8.6         Data Output Value Clear

               Name:        OUTCLR
               Offset:      0x14
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to set one or more output I/O pin drive levels low, without doing a read-
               modify-write operation. Changes in this register will also be reflected in the Data Output Value (OUT),
               Data Output Value Toggle (OUTTGL) and Data Output Value Set (OUTSET) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31            30            29            28                 27       26            25            24
                                                                OUTCLR[31:24]
   Access           RW            RW            RW            RW              RW          RW            RW            RW
    Reset            0             0             0             0                  0        0             0             0


         Bit        23            22            21            20                 19       18            17            16
                                                                OUTCLR[23:16]
   Access           RW            RW            RW            RW              RW          RW            RW            RW
    Reset            0             0             0             0                  0        0             0             0


         Bit        15            14            13            12                 11       10             9             8
                                                                   OUTCLR[15:8]
   Access           RW            RW            RW            RW              RW          RW            RW            RW
    Reset            0             0             0             0                  0        0             0             0


         Bit         7             6             5             4                  3        2             1             0
                                                                   OUTCLR[7:0]
   Access           RW            RW            RW            RW              RW          RW            RW            RW
    Reset            0             0             0             0                  0        0             0             0


               Bits 31:0 – OUTCLR[31:0] PORT Data Output Value Clear
               Writing '0' to a bit has no effect.
               Writing '1' to a bit will clear the corresponding bit in the OUT register. Pins configured as outputs via the
               Data Direction register (DIR) will be set to low output drive level. Pins configured as inputs via DIR and
               with pull enabled via the Pull Enable bit in the Pin Configuration register (PINCFG.PULLEN) will set the
               input pull direction to an internal pull-down.
                Value        Description
                0            The corresponding I/O pin in the PORT group will keep its configuration.
                1            The corresponding I/O pin output is driven low, or the input is connected to an internal pull-
                             down.




           © 2019 Microchip Technology Inc.                            Datasheet                         DS60001507E-page 899
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                PORT - I/O Pin Controller

32.8.7         Data Output Value Set

               Name:        OUTSET
               Offset:      0x18
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to set one or more output I/O pin drive levels high, without doing a read-
               modify-write operation. Changes in this register will also be reflected in the Data Output Value (OUT),
               Data Output Value Toggle (OUTTGL) and Data Output Value Clear (OUTCLR) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31             30            29            28                 27       26            25            24
                                                                OUTSET[31:24]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


         Bit        23             22            21            20                 19       18            17            16
                                                                OUTSET[23:16]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


         Bit        15             14            13            12                 11       10             9             8
                                                                   OUTSET[15:8]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


         Bit         7             6             5             4                  3        2              1             0
                                                                    OUTSET[7:0]
   Access           RW            RW            RW            RW              RW          RW            RW             RW
    Reset            0             0             0             0                  0        0              0             0


               Bits 31:0 – OUTSET[31:0] PORT Data Output Value Set
               Writing '0' to a bit has no effect.
               Writing '1' to a bit will set the corresponding bit in the OUT register, which sets the output drive level high
               for I/O pins configured as outputs via the Data Direction register (DIR). For pins configured as inputs via
               Data Direction register (DIR) with pull enabled via the Pull Enable register (PULLEN), these bits will set
               the input pull direction to an internal pull-up.
                Value        Description
                0            The corresponding I/O pin in the group will keep its configuration.
                1            The corresponding I/O pin output is driven high, or the input is connected to an internal pull-
                             up.




           © 2019 Microchip Technology Inc.                            Datasheet                          DS60001507E-page 900
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                PORT - I/O Pin Controller

32.8.8         Data Output Value Toggle

               Name:        OUTTGL
               Offset:      0x1C
               Reset:       0x00000000
               Property:    PAC Write-Protection

               This register allows the user to toggle the drive level of one or more output I/O pins, without doing a read-
               modify-write operation. Changes in this register will also be reflected in the Data Output Value (OUT),
               Data Output Value Set (OUTSET) and Data Output Value Clear (OUTCLR) registers.


                            Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                            consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                            registers, with a 0x80 address spacing. For example, the register address offset for the Data
                            Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                            the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31             30            29            28                 27       26            25            24
                                                                OUTTGL[31:24]
   Access           RW            RW            RW            RW              RW           RW            RW            RW
    Reset            0             0             0             0                  0         0             0             0


         Bit        23             22            21            20                 19       18            17            16
                                                                OUTTGL[23:16]
   Access           RW            RW            RW            RW              RW           RW            RW            RW
    Reset            0             0             0             0                  0         0             0             0


         Bit        15             14            13            12                 11       10             9             8
                                                                   OUTTGL[15:8]
   Access           RW            RW            RW            RW              RW           RW            RW            RW
    Reset            0             0             0             0                  0         0             0             0


         Bit         7             6             5             4                  3         2             1             0
                                                                    OUTTGL[7:0]
   Access           RW            RW            RW            RW              RW           RW            RW            RW
    Reset            0             0             0             0                  0         0             0             0


               Bits 31:0 – OUTTGL[31:0] PORT Data Output Value Toggle
               Writing '0' to a bit has no effect.
               Writing '1' to a bit will toggle the corresponding bit in the OUT register, which inverts the output drive level
               for I/O pins configured as outputs via the Data Direction register (DIR). For pins configured as inputs via
               Data Direction register (DIR) with pull enabled via the Pull Enable register (PULLEN), these bits will
               toggle the input pull direction.
                Value        Description
                0            The corresponding I/O pin in the PORT group will keep its configuration.
                1            The corresponding OUT bit value is toggled.




           © 2019 Microchip Technology Inc.                            Datasheet                          DS60001507E-page 901
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                            PORT - I/O Pin Controller

32.8.9         Data Input Value

               Name:       IN
               Offset:     0x20
               Reset:      0x00000000
               Property:   -



                           Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                           consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                           registers, with a 0x80 address spacing. For example, the register address offset for the Data
                           Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                           the DIR register for group 1 (PB00 to PB31) is 0x80.



         Bit        31            30           29           28               27        26           25            24
                                                                 IN[31:24]
   Access            R            R            R             R               R         R             R            R
    Reset            0            0            0             0               0          0            0             0


         Bit        23            22           21           20               19        18           17            16
                                                                 IN[23:16]
   Access            R            R            R             R               R         R             R            R
    Reset            0            0            0             0               0          0            0             0


         Bit        15            14           13           12               11        10            9             8
                                                                 IN[15:8]
   Access            R            R            R             R               R         R             R            R
    Reset            0            0            0             0               0          0            0             0


         Bit         7            6            5             4               3          2            1             0
                                                                  IN[7:0]
   Access            R            R            R             R               R         R             R            R
    Reset            0            0            0             0               0          0            0             0


               Bits 31:0 – IN[31:0] PORT Data Input Value
               These bits are cleared when the corresponding I/O pin input sampler detects a logical low level on the
               input pin.
               These bits are set when the corresponding I/O pin input sampler detects a logical high level on the input
               pin.




           © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 902
                                                              SAM D5x/E5x Family Data Sheet
                                                                                          PORT - I/O Pin Controller

32.8.10 Control

           Name:        CTRL
           Offset:      0x24
           Reset:       0x00000000
           Property:    PAC Write-Protection



                        Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                        consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                        registers, with a 0x80 address spacing. For example, the register address offset for the Data
                        Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                        the DIR register for group 1 (PB00 to PB31) is 0x80.



     Bit        31            30            29           28            27            26           25            24
                                                         SAMPLING[31:24]
  Access        RW           RW            RW            RW           RW            RW            RW           RW
   Reset         0            0             0             0            0             0             0            0


     Bit        23            22            21           20            19            18           17            16
                                                         SAMPLING[23:16]
  Access        RW           RW            RW            RW           RW            RW            RW           RW
   Reset         0            0             0             0            0             0             0            0


     Bit        15            14            13           12            11            10            9            8
                                                          SAMPLING[15:8]
  Access        RW           RW            RW            RW           RW            RW            RW           RW
   Reset         0            0             0             0            0             0             0            0


     Bit         7            6             5             4            3             2             1            0
                                                          SAMPLING[7:0]
  Access        RW           RW            RW            RW           RW            RW            RW           RW
   Reset         0            0             0             0            0             0             0            0


           Bits 31:0 – SAMPLING[31:0] Input Sampling Mode
           Configures the input sampling functionality of the I/O pin input samplers, for pins configured as inputs via
           the Data Direction register (DIR).
           The input samplers are enabled and disabled in sub-groups of eight. Thus if any pins within a byte
           request continuous sampling, all pins in that eight pin sub-group will be continuously sampled.
            Value      Description
            0          On demand sampling of I/O pin is enabled.
            1          Continuous sampling of I/O pin is enabled.




       © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 903
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                             PORT - I/O Pin Controller

32.8.11 Write Configuration

            Name:        WRCONFIG
            Offset:      0x28
            Reset:       0x00000000
            Property:    PAC Write-Protection, Write-Only



                         Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                         consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                         registers, with a 0x80 address spacing. For example, the register address offset for the Data
                         Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                         the DIR register for group 1 (PB00 to PB31) is 0x80.


            This Write-only register is used to configure several pins simultaneously with the same configuration
            and/or peripheral multiplexing.
            In order to avoid side effect of non-atomic access, 8-bit or 16-bit writes to this register will have no effect.
            Reading this register always returns zero.

      Bit         31            30            29            28              27          26                25          24
               HWSEL       WRPINCFG                      WRPMUX                              PMUX[3:0]
  Access          W             W                           W               W            W                W           W
   Reset          0             0                            0                  0        0                0           0


      Bit         23            22            21            20              19          18                17          16
                             DRVSTR                                                   PULLEN             INEN      PMUXEN
  Access                        W                                                        W                W           W
   Reset                        0                                                        0                0           0


      Bit         15            14            13            12              11          10                9           8
                                                             PINMASK[15:8]
  Access          W             W             W             W               W            W                W           W
   Reset          0             0             0              0                  0        0                0           0


      Bit         7             6             5              4                  3        2                1           0
                                                                 PINMASK[7:0]
  Access          W             W             W             W               W            W                W           W
   Reset          0             0             0              0                  0        0                0           0


            Bit 31 – HWSEL Half-Word Select
            This bit selects the half-word field of a 32-PORT group to be reconfigured in the atomic write operation.
            This bit will always read as zero.
             Value        Description
             0            The lower 16 pins of the PORT group will be configured.
             1            The upper 16 pins of the PORT group will be configured.




        © 2019 Microchip Technology Inc.                             Datasheet                            DS60001507E-page 904
                                                  SAM D5x/E5x Family Data Sheet
                                                                           PORT - I/O Pin Controller

Bit 30 – WRPINCFG Write PINCFG
This bit determines whether the atomic write operation will update the Pin Configuration register
(PINCFGy) or not for all pins selected by the WRCONFIG.PINMASK and WRCONFIG.HWSEL bits.
Writing '0' to this bit has no effect.
Writing '1' to this bit updates the configuration of the selected pins with the written WRCONFIG.DRVSTR,
WRCONFIG.PULLEN, WRCONFIG.INEN, WRCONFIG.PMUXEN, and WRCONFIG.PINMASK values.
This bit will always read as zero.
 Value        Description
 0            The PINCFGy registers of the selected pins will not be updated.
 1            The PINCFGy registers of the selected pins will be updated.

Bit 28 – WRPMUX Write PMUX
This bit determines whether the atomic write operation will update the Peripheral Multiplexing register
(PMUXn) or not for all pins selected by the WRCONFIG.PINMASK and WRCONFIG.HWSEL bits.
Writing '0' to this bit has no effect.
Writing '1' to this bit updates the pin multiplexer configuration of the selected pins with the written
WRCONFIG. PMUX value.
This bit will always read as zero.
 Value        Description
 0            The PMUXn registers of the selected pins will not be updated.
 1            The PMUXn registers of the selected pins will be updated.

Bits 27:24 – PMUX[3:0] Peripheral Multiplexing
These bits determine the new value written to the Peripheral Multiplexing register (PMUXn) for all pins
selected by the WRCONFIG.PINMASK and WRCONFIG.HWSEL bits, when the WRCONFIG.WRPMUX
bit is set.
These bits will always read as zero.

Bit 22 – DRVSTR Output Driver Strength Selection
This bit determines the new value written to PINCFGy.DRVSTR for all pins selected by the
WRCONFIG.PINMASK and WRCONFIG.HWSEL bits, when the WRCONFIG.WRPINCFG bit is set.
This bit will always read as zero.

Bit 18 – PULLEN Pull Enable
This bit determines the new value written to PINCFGy.PULLEN for all pins selected by the
WRCONFIG.PINMASK and WRCONFIG.HWSEL bits, when the WRCONFIG.WRPINCFG bit is set.
This bit will always read as zero.

Bit 17 – INEN Input Enable
This bit determines the new value written to PINCFGy.INEN for all pins selected by the
WRCONFIG.PINMASK and WRCONFIG.HWSEL bits, when the WRCONFIG.WRPINCFG bit is set.
This bit will always read as zero.

Bit 16 – PMUXEN Peripheral Multiplexer Enable
This bit determines the new value written to PINCFGy.PMUXEN for all pins selected by the
WRCONFIG.PINMASK and WRCONFIG.HWSEL bits, when the WRCONFIG.WRPINCFG bit is set.
This bit will always read as zero.




© 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 905
                                                 SAM D5x/E5x Family Data Sheet
                                                                           PORT - I/O Pin Controller

Bits 15:0 – PINMASK[15:0] Pin Mask for Multiple Pin Configuration
These bits select the pins to be configured within the half-word group selected by the
WRCONFIG.HWSEL bit.
These bits will always read as zero.
 Value      Description
 0          The configuration of the corresponding I/O pin in the half-word group will be left unchanged.
 1          The configuration of the corresponding I/O pin in the half-word PORT group will be updated.




© 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 906
                                                              SAM D5x/E5x Family Data Sheet
                                                                                         PORT - I/O Pin Controller

32.8.12 Event Input Control

            Name:       EVCTRL
            Offset:     0x2C
            Reset:      0x00000000
            Property:   PAC Write-Protection



                        Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                        consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                        registers, with a 0x80 address spacing. For example, the register address offset for the Data
                        Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                        the DIR register for group 1 (PB00 to PB31) is 0x80.


            There are up to four input event pins for each PORT group. Each byte of this register addresses one
            Event input pin.

      Bit        31            30                 29     28            27           26            25              24
              PORTEIx               EVACTx[1:0]                                  PIDx[4:0]
  Access         RW           RW              RW         RW           RW            RW           RW            RW
   Reset          0            0                  0       0            0             0             0              0


      Bit        23            22                 21     20            19           18            17              16
              PORTEIx               EVACTx[1:0]                                  PIDx[4:0]
  Access         RW           RW              RW         RW           RW            RW           RW            RW
   Reset          0            0                  0       0            0             0             0              0


      Bit        15            14                 13     12            11           10             9              8
              PORTEIx               EVACTx[1:0]                                  PIDx[4:0]
  Access         RW           RW              RW         RW           RW            RW           RW            RW
   Reset          0            0                  0       0            0             0             0              0


      Bit         7            6                  5       4            3             2             1              0
              PORTEIx               EVACTx[1:0]                                  PIDx[4:0]
  Access         RW           RW              RW         RW           RW            RW           RW            RW
   Reset          0            0                  0       0            0             0             0              0


            Bits 31,23,15,7 – PORTEIx PORT Event Input Enable x [x = 3..0]
            Value       Description
            0           The event action x (EVACTx) will not be triggered on any incoming event.
            1           The event action x (EVACTx) will be triggered on any incoming event.

            Bits 30:29, 22:21,14:13,6:5 – EVACTx PORT Event Action x [x = 3..0]
            These bits define the event action the PORT will perform on event input x. See also Table 32-4.

            Bits 28:24,20:16,12:8,4:0 – PIDx PORT Event Pin Identifier x [x = 3..0]
            These bits define the I/O pin on which the event action will be performed, according to Table 32-5.




        © 2019 Microchip Technology Inc.                       Datasheet                           DS60001507E-page 907
                                                 SAM D5x/E5x Family Data Sheet
                                                                    PORT - I/O Pin Controller

Table 32-4. PORT Event x Action ( x = [3..0] )

 Value                             Name                       Description
 0x0                               OUT                        Output register of pin will be set
                                                              to level of event.
 0x1                               SET                        Set output register of pin on
                                                              event.
 0x2                               CLR                        Clear output register of pin on
                                                              event.
 0x3                               TGL                        Toggle output register of pin on
                                                              event.

Table 32-5. PORT Event x Pin Identifier ( x = [3..0] )

 Value                             Name                       Description
 0x0                               PIN0                       Event action to be executed on
                                                              PIN 0.
 0x1                               PIN1                       Event action to be executed on
                                                              PIN 1.
 ...                               ...                        ...
 0x31                              PIN31                      Event action to be executed on
                                                              PIN 31.




© 2019 Microchip Technology Inc.                  Datasheet                  DS60001507E-page 908
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           PORT - I/O Pin Controller

32.8.13 Peripheral Multiplexing n

            Name:        PMUX
            Offset:      0x30 + n*0x01 [n=0..15]
            Reset:       0x00
            Property:    PAC Write-Protection



                         Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                         consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                         registers, with a 0x80 address spacing. For example, the register address offset for the Data
                         Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                         the DIR register for group 1 (PB00 to PB31) is 0x80.


            There are up to 16 Peripheral Multiplexing registers in each group, one for every set of two subsequent
            I/O lines. The n denotes the number of the set of I/O lines.

      Bit         7             6                5         4             3             2                1           0
                                    PMUXO[3:0]                                             PMUXE[3:0]
  Access         RW            RW                RW       RW            RW            RW                RW         RW
   Reset          0             0                0         0             0             0                0           0


            Bits 7:4 – PMUXO[3:0] Peripheral Multiplexing for Odd-Numbered Pin
            These bits select the peripheral function for odd-numbered pins (2*n + 1) of a PORT group, if the
            corresponding PINCFGy.PMUXEN bit is '1'.
            Not all possible values for this selection may be valid. For more details, refer to the I/O Multiplexing and
            Considerations.

                      PMUXO[3:0]                 Name     Description
                         0x0                          A   Peripheral function A selected
                         0x1                          B   Peripheral function B selected
                         0x2                          C   Peripheral function C selected
                         0x3                          D   Peripheral function D selected
                         0x4                          E   Peripheral function E selected
                         0x5                          F   Peripheral function F selected
                         0x6                          G   Peripheral function G selected
                         0x7                          H   Peripheral function H selected
                         0x8                          I   Peripheral function I selected
                         0x9                          J   Peripheral function J selected
                         0xA                          K   Peripheral function K selected
                         0xB                          L   Peripheral function L selected
                         0xC                          M   Peripheral function M selected




        © 2019 Microchip Technology Inc.                         Datasheet                              DS60001507E-page 909
                                                   SAM D5x/E5x Family Data Sheet
                                                                              PORT - I/O Pin Controller

...........continued
         PMUXO[3:0]                Name       Description
               0xD                  N         Peripheral function N selected
            0xE-0xF                  -        Reserved

Bits 3:0 – PMUXE[3:0] Peripheral Multiplexing for Even-Numbered Pin
These bits select the peripheral function for even-numbered pins (2*n) of a PORT group, if the
corresponding PINCFGy.PMUXEN bit is '1'.
Not all possible values for this selection may be valid. For more details, refer to the I/O Multiplexing and
Considerations.

         PMUXE[3:0]                Name      Description
               0x0                  A        Peripheral function A selected
               0x1                  B        Peripheral function B selected
               0x2                  C        Peripheral function C selected
               0x3                  D        Peripheral function D selected
               0x4                  E        Peripheral function E selected
               0x5                  F        Peripheral function F selected
               0x6                  G        Peripheral function G selected
               0x7                  H        Peripheral function H selected
               0x8                  I        Peripheral function I selected
               0x9                  J        Peripheral function J selected
              0xA                   K        Peripheral function K selected
              0xB                   L        Peripheral function L selected
              0xC                   M        Peripheral function M selected
              0xD                   N        Peripheral function N selected
            0xE-0xF                 -        Reserved

Related Links
6. I/O Multiplexing and Considerations




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 910
                                                                SAM D5x/E5x Family Data Sheet
                                                                                            PORT - I/O Pin Controller

32.8.14 Pin Configuration

            Name:        PINCFG
            Offset:      0x40 + n*0x01 [n=0..31]
            Reset:       0x00
            Property:    PAC Write-Protection



                         Tip: The I/O pins are assembled in pin groups (”PORT groups”) with up to 32 pins. Group 0
                         consists of the PA pins, group 1 is for the PB pins, etc. Each pin group has its own PORT
                         registers, with a 0x80 address spacing. For example, the register address offset for the Data
                         Direction (DIR) register for group 0 (PA00 to PA31) is 0x00, and the register address offset for
                         the DIR register for group 1 (PB00 to PB31) is 0x80.


            There are up to 32 Pin Configuration registers in each PORT group, one for each I/O line.

      Bit         7             6             5             4             3             2            1             0
                            DRVSTR                                                  PULLEN          INEN        PMUXEN
  Access                       RW                                                     RW            RW            RW
   Reset                        0                                                       0            0             0


            Bit 6 – DRVSTR Output Driver Strength Selection
            This bit controls the output driver strength of an I/O pin configured as an output.
             Value       Description
             0           Pin drive strength is set to normal drive strength.
             1           Pin drive strength is set to stronger drive strength.

            Bit 2 – PULLEN Pull Enable
            This bit enables the internal pull-up or pull-down resistor of an I/O pin configured as an input.
             Value      Description
             0          Internal pull resistor is disabled, and the input is in a high-impedance configuration.
             1          Internal pull resistor is enabled, and the input is driven to a defined logic level in the absence
                        of external input.

            Bit 1 – INEN Input Enable
            This bit controls the input buffer of an I/O pin configured as either an input or output.
            Writing a zero to this bit disables the input buffer completely, preventing read-back of the Physical Pin
            state when the pin is configured as either an input or output.
             Value       Description
             0           Input buffer for the I/O pin is disabled, and the input value will not be sampled.
             1           Input buffer for the I/O pin is enabled, and the input value will be sampled when required.

            Bit 0 – PMUXEN Peripheral Multiplexer Enable
            This bit enables or disables the peripheral multiplexer selection set in the Peripheral Multiplexing register
            (PMUXn) to enable or disable alternative peripheral control over an I/O pin direction and output drive
            value.
            Writing a zero to this bit allows the PORT to control the pad direction via the Data Direction register (DIR)
            and output drive value via the Data Output Value register (OUT). The peripheral multiplexer value in




        © 2019 Microchip Technology Inc.                         Datasheet                            DS60001507E-page 911
                                                  SAM D5x/E5x Family Data Sheet
                                                                            PORT - I/O Pin Controller

PMUXn is ignored. Writing '1' to this bit enables the peripheral selection in PMUXn to control the pad. In
this configuration, the Physical Pin state may still be read from the Data Input Value register (IN) if
PINCFGn.INEN is set.
 Value       Description
 0           The peripheral multiplexer selection is disabled, and the PORT registers control the direction
             and output drive value.
 1           The peripheral multiplexer selection is enabled, and the selected peripheral function controls
             the direction and output drive value.




© 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 912
