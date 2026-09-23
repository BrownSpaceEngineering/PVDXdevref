# 59. Schematic Checklist

*Source: `Atmel-SAMD51.pdf`, pages 2096-2111 — SAMD51 family datasheet*

                                                            SAM D5x/E5x Family Data Sheet
                                                                                           Schematic Checklist


59.      Schematic Checklist

59.1     Introduction
         This chapter describes a common checklist which should be used when starting and reviewing the
         schematics for a SAM D5x/E5x design. This chapter illustrates recommended power supply connections,
         how to connect external analog references, programmer, debugger, oscillator and crystal.

59.1.1   Operation in Noisy Environment
         If the device is operating in an environment with much electromagnetic noise, it must be protected from
         this noise to ensure reliable operation. In addition to following best practice EMC design guidelines, the
         recommendations listed in the schematic checklist sections must be followed. In particular, placing
         decoupling capacitors very close to the power pins, an RC-filter on the RESET pin, and a pull-up resistor
         on the SWCLK pin is critical for reliable operations. It is also relevant to eliminate or attenuate noise in
         order to avoid that it reaches supply pins, I/O pins and crystals.



59.2     Power Supply
         The SAM D5x/E5x supports a single or dual power supply from 1.71V to 3.63V. The same voltage must
         be applied to both VDDIO and VDDANA. VDDIOB level must be lower or equal to VDDIO / VDDANA.
         When I/O pads in the VDDIOB cluster are multiplexed as analog pads, VDDANA is used to power the I/O.
         Using this configuration may result in an electrical conflict if the VDDIOB voltage is different from that of
         VDDIO / VDDANA. If the application has such requirements, it is required to power VDDIOB, VDDIO, and
         VDDANA from the same supply source to ensure that they are always at the same voltage.
         The internal voltage regulator has four different modes:
           • Linear mode: This mode does not require any external inductor. This is the default mode when CPU
             and peripherals are running
           • Switching mode (Buck): The most efficient mode when the CPU and peripherals are running.
           • Low Power (LP) mode: This is the default mode used when the device is in Standby mode
           • Shutdown mode: When the device is in Backup mode, the internal regulator is turned off
         Selecting between switching mode and linear mode can be done by software on the fly, but the power
         supply must be designed according to which mode is to be used.

59.2.1   Power Supply Connections
         The following figures shows the recommended power supply connections for switched/linear mode, linear
         mode only and with battery backup.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 2096
                                                        SAM D5x/E5x Family Data Sheet
                                                                                        Schematic Checklist

Figure 59-1. Power Supply Connection for Switching/Linear Mode

   IO Supply                              Close to device                          SAM Device
(1.71V — 3.63V)                           (for every pin)
                                                                     VDDIOB                          VBAT (PB03)
                Main Supply
            (1.71V — 3.63V)
                                                                  VDDANA


                                                                      VDDIO


                                                100nF             10µH
                                                        100nF
                                                                         VSW
          1µF         10µF         10µF
                                                                VDDCORE

                                                                           100nF
                                                             4.7µF

                                                                         GND


                                                                  GNDANA



Figure 59-2. Power Supply Connection for Linear Mode Only

   IO Supply                              Close to device                          SAM Device
(1.71V — 3.63V)                           (for every pin)
                                                                     VDDIOB                          VBAT (PB03)
                Main Supply
            (1.71V — 3.63V)
                                                                  VDDANA


                                                                      VDDIO


                                                100nF
                                                                         VSW

          1µF         10µF         10µF                   100nF

                                                                VDDCORE

                                                             4.7µF       100nF

                                                                         GND


                                                                  GNDANA




© 2019 Microchip Technology Inc.                            Datasheet                       DS60001507E-page 2097
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                                 Schematic Checklist

       Figure 59-3. Power Supply Connection for Battery Backup

          IO Supply                              Close to device                           SAM E54
       (1.71V — 3.63V)                           (for every pin)
                                                                               VDDIOB                       VBAT (PB03)
                       Main Supply
                   (1.71V — 3.63V)
                                                                            VDDANA


                                                                                VDDIO


                                                   100nF   100nF            10µH
                                                                   100nF
                                                                                   VSW
                 1µF         10µF         10µF
                                                                           VDDCORE

                                                                       4.7µF       100nF

                                                                                   GND


                                                                           GNDANA


       Note:
        1. The passive component value shown in figures 58-1, 58-2 & 58-3 is a typical example. Refer to
             54.10.1 Voltage Regulator Characteristics for details on specification.
        2. Decoupling capacitors should be placed close to the device for each supply pin pair in the signal
             group, low ESR capacitors should be used for better decoupling.
        3. An inductor should be added between the external power and the VDD for power filtering.
        4. A ferrite bead has better filtering performance compared to standard inductor at high frequencies. A
             ferrite bead can be added between the main power supply (VDD) and VDDANA to prevent digital
             noise from entering the analog power domain. The bead should provide enough impedance (i.e.,
             50Ω at 20 MHz and 220Ω at 100 MHz) to separate the digital and analog power domains. Make
             sure to select a ferrite bead designed for filtering applications with a low DC resistance to avoid a
             large voltage drop across the ferrite bead.



59.3   External Analog Reference Connections
       The following schematic checklist is only necessary if the application is using one or more of the external
       analog references. If the internal references are used instead, the following circuits are not necessary.




       © 2019 Microchip Technology Inc.                                Datasheet                     DS60001507E-page 2098
                                            SAM D5x/E5x Family Data Sheet
                                                                         Schematic Checklist

Figure 59-4. External Analog Reference Schematic With Three References
                                              Close to device
                                              (for every pin)

                                                  VREFA


                   EXTERNAL
                                    4.7μF        100nF
                  REFERENCE 1                        GND



                                                  VREFB


                   EXTERNAL
                                    4.7μF        100nF
                  REFERENCE 2                        GND



                                                  VREFC


                   EXTERNAL
                                    4.7μF        100nF
                  REFERENCE 3                        GND




© 2019 Microchip Technology Inc.            Datasheet                       DS60001507E-page 2099
                                           SAM D5x/E5x Family Data Sheet
                                                                       Schematic Checklist

Figure 59-5. External Analog Reference Schematic With Two References
                                              Close to device
                                              (for every pin )

                                                  VREFA


                EXTERNAL
                                   4.7μF         100 nF
               REFERENCE 1                           GND



                                                  VREFB


                EXTERNAL
                                   4.7μF         100 nF
               REFERENCE 2                           GND




                                                  VREFC



                                                     GND




© 2019 Microchip Technology Inc.            Datasheet                     DS60001507E-page 2100
                                                             SAM D5x/E5x Family Data Sheet
                                                                                         Schematic Checklist

       Figure 59-6. External Analog Reference Schematic With One Reference
                                                              Close to device
                                                              (for every pin )

                                                                  VREFA


                        EXTERNAL
                                             4.7μF               100 nF
                       REFERENCE                                     GND



                                                                  VREFB



                                                                     GND




                                                                  VREFC



                                                                     GND




       Table 59-1. External Analog Reference Connections

        Signal Name        Recommended Pin Connection            Description
        VREFx              1.0V to (VDDANA - 0.6V) for ADC       External reference VREFx for the analog port
                           1.0V to (VDDANA - 0.6V) for DAC
                           Decoupling/filtering capacitors
                           100nF(1)(2) and 4.7µF(1)
        GND                                                      Ground

       1. These values are only given as a typical example.
       2. Decoupling capacitor should be placed close to the device for each supply pin pair in the signal group.



59.4   External Reset Circuit
       When the external Reset function is used, connect the external Reset circuit to the RESET pin as shown
       below. If the external Reset function is not required, the circuit is not necessary: the RESET pin can either
       remain unconnected, or be driven LOW externally by the application circuitry.
       The Reset switch can also be removed if a manual Reset is not necessary. The RESET pin itself has an
       internal pull-up resistor, hence it is optional to add any external pull-up resistor.




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 2101
                                                               SAM D5x/E5x Family Data Sheet
                                                                                         Schematic Checklist

       Figure 59-7. External Reset Circuit Schematic

                                            VDD

                                           10kΩ

                                           330Ω           RESET


                                              100nF
                                                               GND




       A pull-up resistor makes sure that the Reset does not go low and unintentionally causing a device Reset.
       An additional resistor has been added in series with the switch to safely discharge the filtering capacitor,
       i.e. preventing a current surge when shorting the filtering capacitor which again can cause a noise spike
       that can have a negative effect on the system.
       Table 59-2. Reset Circuit Connections

        Signal Name               Recommended Pin Connection                                   Description
        RESET                     Reset low level threshold voltage                            Reset pin
                                  VDDIO = 1.71V - 2.0V: Below 0.33 * VDDIO
                                  VDDIO = 2.7V - 3.6V: Below 0.36 * VDDIO
                                  Decoupling/filter capacitor 100nF(1)
                                  Pull-up resistor 10kΩ(1,2)
                                  Resistor in series with the switch 330Ω(1)

       1. These values are only given as a typical example.
       2. The SAM D5x/E5x features an internal pull-up resistor on the RESET pin, hence an external pull-up is
       optional.



59.5   Unused or Unconnected Pins
       For unused pins the default state of the pins will give the lowest current leakage. Thus there is no need to
       do any configuration of the unused pins in order to lower the power consumption.



59.6   Clocks and Crystal Oscillators
       The SAM D5x/E5x can be run from internal or external clock sources, or a mix of internal and external
       sources. An example of usage can be to use the internal 48MHz DFLL as source for the system clock
       and an external 32.768kHz watch crystal as clock source for the Real-Time counter (RTC).




       © 2019 Microchip Technology Inc.                         Datasheet                     DS60001507E-page 2102
                                                              SAM D5x/E5x Family Data Sheet
                                                                                            Schematic Checklist

59.6.1   External Clock Source
         Figure 59-8. External Clock Source Schematic

                                               External
                                                Clock
                                                                XIN


                                                       XOUT/GPIO
                                                      NC/GPIO



         Table 59-3. External Clock Source Connections

          Signal Name        Recommended Pin Connection                            Description
          XIN                XIN is used as input for an external clock signal     Input for inverting oscillator pin
          XOUT/GPIO          Can be left unconnected or used as normal GPIO        NC/GPIO

59.6.2   Crystal Oscillator
         Figure 59-9. Crystal Oscillator Schematic

                                                                  XIN

                                                  26pF
                                                               XOUT

                                                  26pF



         The crystal should be located as close to the device as possible. Long signal lines may cause too high
         load to operate the crystal, and cause crosstalk to other parts of the system.
         Table 59-4. Crystal Oscillator Checklist

          Signal Name          Recommended Pin Connection                Description
          XIN                  Load capacitor 26pF(1)(2)                 External crystal between 8 to 48MHz
          XOUT                 Load capacitor 26pF(1)(2)

         1. These values are only given as a typical example.
         2. The capacitors should be placed close to the device for each supply pin pair in the signal group.

59.6.3   External Real Time Oscillator
         The low frequency crystal oscillator is optimized for use with a 32.768kHz watch crystal. When selecting
         crystals, load capacitance and the crystal’s Equivalent Series Resistance (ESR) must be taken into
         consideration. Both values are specified by the crystal vendor.
         SAM D5x/E5x oscillator is optimized for very low power consumption, hence close attention should be
         made when selecting crystals.




         © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 2103
                                                              SAM D5x/E5x Family Data Sheet
                                                                                            Schematic Checklist

         The typical parasitic load capacitance values are available in the Electrical Characteristics section. This
         capacitance and PCB capacitance can allow using a crystal inferior to 12.5pF load capacitance without
         external capacitors as shown in the next figure.
         Figure 59-10. External Real Time Oscillator without Load Capacitor


                                                               XIN32


                                              32.768kHz       XOUT32




         To improve accuracy and Safety Factor, the crystal datasheet can recommend adding external capacitors
         as shown the figure below.
         To find suitable load capacitance for a 32.768kHz crystal, consult the crystal datasheet.
         Figure 59-11. External Real Time Oscillator with Load Capacitor

                                                   18pF         XIN32


                                               32.768kHz      XOUT32

                                                   18pF



         Table 59-5. External Real Time Oscillator Checklist

          Signal Name             Recommended Pin Connection                    Description
          XIN32                   Load capacitor 18pF(1)(2)                     Timer oscillator input
          XOUT32                  Load capacitor 18pF(1)(2)                     Timer oscillator output

         1. These values are only given as typical examples.
         2. The capacitors should be placed close to the device for each supply pin pair in the signal group.
         Note: In order to minimize the cycle-to-cycle jitter of the external oscillator, keep the neighboring pins as
         steady as possible. For neighboring pin details, refer to the Oscillator Pinout section.

59.6.4   Calculating the Correct Crystal Decoupling Capacitor
         The model shown in Figure 59-12 can be used to calculate correct load capacitor for a given crystal. This
         model includes internal capacitors CLn, external parasitic capacitance CELn and external load capacitance
         CPn.




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 2104
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                                     Schematic Checklist

       Figure 59-12. Crystal Circuit With Internal, External and Parasitic Capacitance




                                                           CL1          CL2




                                                                                 External Internal
                                             XIN                    XOUT




                                              CEL1   CP1          CP2     CEL2




       Using this model the total capacitive load for the crystal can be calculated as shown in the equation
       below:
                   ��1 + ��1 + �EL1 ��2 + ��2 + �EL2
          �tot =
                   ��1 + ��1 + �EL1 + ��2 + ��2 + �EL2

       where Ctot is the total load capacitance seen by the crystal. This value should be equal to the load
       capacitance value found in the crystal manufacturer datasheet.
       The parasitic capacitance CELn can in most applications be disregarded as these are usually very small. If
       accounted for, these values are dependent on the PCB material and PCB layout.
       For some crystal the internal capacitive load provided by the device itself can be enough. To calculate the
       total load capacitance in this case. CELn and CPn are both zero, CL1 = CL2 = CL, and the equation reduces
       to the following:
                   ��
          �tot =
                   2
       See the related links for equivalent internal pin capacitance values.



59.7   Programming and Debug Ports
       For programming and/or debugging the SAM D5x/E5x, the device should be connected using the Serial
       Wire Debug, SWD, interface. Currently the SWD interface is supported by several Microchip and third
       party programmers and debuggers, like the Atmel-ICE, SAM-ICE or SAM D5x/E5x Xplained Pro (SAM
       D5x/E5x evaluation kit) Embedded Debugger.
       Refer to the Atmel-ICE, SAM-ICE or SAM D5x/E5x Xplained Pro user guides for details on debugging
       and programming connections and options. For connecting to any other programming or debugging tool,
       refer to that specific programmer or debugger’s user guide.
       The SAM D5x/E5x Xplained Pro evaluation board supports programming and debugging through the
       onboard embedded debugger so no external programmer or debugger is needed.




       © 2019 Microchip Technology Inc.                          Datasheet                              DS60001507E-page 2105
                                                            SAM D5x/E5x Family Data Sheet
                                                                                           Schematic Checklist

         Note: A pull-up resistor on the SWCLK pin is critical for reliable operation. Refer to related link for more
         information.
         Figure 59-13. SWCLK Circuit Connections
                             VDD



                             1kΩ
                                            SWCLK




         Table 59-6. SWCLK Circuit Connections

          Pin Name                            Description                         Recommended Pin Connection
          SWCLK                               Serial wire clock pin               Pull-up resistor 1kΩ

         Related Links
         59.1.1 Operation in Noisy Environment

59.7.1   Cortex Debug Connector (10-pin)
         For debuggers and/or programmers that support the Cortex Debug Connector (10-pin) interface the
         signals should be connected as shown in Figure 59-14 with details described in Table 59-7.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 2106
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                            Schematic Checklist

         Figure 59-14. Cortex Debug Connector (10-pin)

          VDD
                  Cortex Debug Connector
                          (10-pin)
                   VTref           SWDIO
                          1
                   GND             SWDCLK                 RESET
                   GND
                                   NC
                                                        SWCLK
                    NC             NC
                                   RESET
                    NC
                                                         SWDIO


                                                           GND




         Table 59-7. Cortex Debug Connector (10-pin)

          Header Signal Name                Description
          SWDCLK                            Serial wire clock pin
          SWDIO                             Serial wire bidirectional data pin
          RESET                             Target device reset pin, active low
          VTref                             Target voltage sense, should be connected to the device VDD
          GND                               Ground

59.7.2   20-pin IDC JTAG Connector
         For debuggers and/or programmers that support the 20-pin IDC JTAG Connector, e.g. the SAM-ICE, the
         signals should be connected as shown in Figure 59-15 with details described in Table 59-8.




         © 2019 Microchip Technology Inc.                           Datasheet                    DS60001507E-page 2107
                                                               SAM D5x/E5x Family Data Sheet
                                                                                           Schematic Checklist

         Figure 59-15. 20-pin IDC JTAG Connector

          VDD
                     20-pin IDC JTAG Connector

                      VCC             NC
                             1
                                     GND                  RESET
                        NC
                                      GND
                     NC
                   SWDIO              GND                SWCLK
                 SWDCLK               GND

                        NC            GND                 SWDIO
                        NC            GND*
                   RESET              GND*                   GND

                       NC             GND*

                        NC            GND*




         Table 59-8. 20-pin IDC JTAG Connector

          Header Signal Name Description
          SWDCLK                     Serial wire clock pin
          SWDIO                      Serial wire bidirectional data pin
          RESET                      Target device reset pin, active low
          VCC                        Target voltage sense, should be connected to the device VDD
          GND                        Ground
          GND*                       These pins are reserved for firmware extension purposes. They can be left
                                     unconnected or connected to GND in normal debug environment. They are not
                                     essential for SWD in general.

59.7.3   Trace (CoreSight 20) Connector
         The Trace Port Interface Unit (TPIU) takes data from the Embedded Trace Module (ETM) and allows
         debugger communication to ETM. The following figure shows the connection diagram.




         © 2019 Microchip Technology Inc.                          Datasheet                   DS60001507E-page 2108
                                                              SAM D5x/E5x Family Data Sheet
                                                                                               Schematic Checklist

       Figure 59-16. Trace (CoreSight 20) Connector Diagram




59.8   QSPI Interface
       Table 59-9. QSPI Interface Pins and Connections

        Pin Name                           Recommended Pin Connection Description
        PA08 - PA11                        Application dependent                       QSPI I/O lines
        PB10                               Application dependent                       QSPI Clock
        PB11                               Application dependent                       QSPI Chip Select

                                                                          VDDIO

         QSPI
         PA08                                     SI / SIO0    VDD
         PA09                                     SO / SIO1
         PA10                                     SIO2                          C
         PA11                                     SIO3                          100n
         PB10                                     SCK           VSS
         PB11                                     CS            PAD
                               R605
                    VDDIO       100k
                                                                          GND

       Note: Signal integrity can be improved by adding series resistors on each QSPI line. The resistor value
       should be based on the corresponding I/O pin drive strength (decided by PINCFGn.DRVSTR) and PCB
       trace impedance. It is recommended to do simulation using the device IBIS files to choose the correct
       termination and PCB trace impedance combination.



59.9   USB Interface
       The USB interface consists of a differential data pair (D+/D-) and a power supply (VBUS, GND).
       Refer to the Electrical Characteristics section for operating voltages which will allow USB operation.




       © 2019 Microchip Technology Inc.                       Datasheet                             DS60001507E-page 2109
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                                 Schematic Checklist

Table 59-10. USB Interface Checklist

   Signal     Recommended Pin Connection                                                                           Description
   Name
     D+         • The impedance of the pair should be matched on the PCB to                                        USB full speed / low
                  minimize reflections.                                                                            speed positive data
                • USB differential tracks should be routed with the same                                           upstream pin
     D-           characteristics (length, width, number of vias, etc.)                                            USB full speed / low
                • For a tightly coupled differential pair,the signal routing should be                             speed negative data
                  as parallel as possible, with a minimum number of angles and                                     upstream pin
                  vias.

Figure 59-17. Low Cost USB Interface Example Schematic
                                                 USB        VBUS
                                               Connector                USB
                                                                    Differential
                                                                   Data Line Pair              USB_D+
                                                   VBUS
                                                     D+
                                                      D-
                                                    GND
                                                                                               USB_D-
                                                Shield


                                                                   GND (Board)


It is recommended to increase ESD protection on the USB D+, D-, and VBUS lines using dedicated
transient suppressors. These protections should be located as close as possible to the USB connector to
reduce the potential discharge path and reduce discharge propagation within the entire system.
The USB FS cable includes a dedicated shield wire that should be connected to the board with caution.
Special attention should be paid to the connection between the board ground plane and the shield from
the USB connector and the cable.
Tying the shield directly to ground would create a direct path from the ground plane to the shield, turning
the USB cable into an antenna. To limit the USB cable antenna effect, it is recommended to connect the
shield and ground through an RC filter.
Figure 59-18. Protected USB Interface Example Schematic

                                                              USB Transient
                                                VBUS
                                                              protection

                                     USB
                                   Connector                                       USB
                                                                               Differential
                                                                              Data Line Pair            USB_D+
                                       VBUS
                                         D+
                                          D-
                                        GND
                                                                                                        USB_D-
                                                   4.5nF




                                    Shield
                                                   1MΩ




                                       RC Filter
                                     (GND/Shield
                                     Connection)           GND (Board)




© 2019 Microchip Technology Inc.                                     Datasheet                                      DS60001507E-page 2110
                                                       SAM D5x/E5x Family Data Sheet
                                                                                    Schematic Checklist


59.10   SDHC Interface
        The SD/MMC Host Controller (SDHC) is compliant with the SD Host Controller Standard specifications.
        There are two instances of SDHC available on this device: SDHC0 and SDHC1. The typical connection
        diagram is shown in the following figure.




        © 2019 Microchip Technology Inc.                Datasheet                        DS60001507E-page 2111
