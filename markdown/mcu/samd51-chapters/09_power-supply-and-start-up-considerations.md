# 7. Power Supply and Start-Up Considerations

*Source: `Atmel-SAMD51.pdf`, pages 47-51 — SAMD51 family datasheet*

                                                                                                  SAM D5x/E5x Family Data Sheet
                                                                                                                                                            Power Supply and Start-Up ...


7.      Power Supply and Start-Up Considerations

7.1     Power Domain Overview
        Figure 7-1. Power Domain Block Diagram




                                                                                                                                                                       BAT (PB[3])
                                             VDDCORE




                                                                                                                                         PD[21:20]
                                                                                                                             PC[31:10]
                                                                                                                 PB[31:10]
                                                                              PA[31:30]

                                                                                          PA[27:12]




                                                                                                                                                              VDDANA
                                    GNDANA
                          VDDANA




                                                                                                      PD[12:8]




                                                                                                                                                                                                      VDDIOB
                                                                      VDDIO
                                                                VSW
                                                       GND
                                                                                                                                                                             VBAT                               PA[11:8]

                                                                              VDDIO                                                                                                             POR             PB[11:10]
                       VDDANA
                                                          VOLTAGE                          XOSCs                                                                                                                PC[7:4]
         PA[7:2]               DAC                       REGULATOR                                                                                           VSWOUT                           POR              PC[1:0]
                                                                      BOD12                                                                             OSCULP32K
         PB[9:4]                   AC                                                                                                                                                        BOD33
                                                                                                                                                                                                               PB[2:0]
                                                                                                                                                         VOLTAGE
         PC[3:2]             ADC0/1                                                                                                                     REGULATOR                           XOSC32K
                                                                                                                                                                                                                PA[1:0]
                                                                      VDDCORE
         PD[1:0]
                                   PTC

                                                             VSW
                                   POR
                                                              Digital Logic                               RTC, PM,
                                                             CPU, Peripherals                           SUPC, RSTC                                   128KB
                                                                                                                                                             32KB                4KB     4KB
                                                                                                                                                     96KB
                                                                DFLL48M                                      VDDBU
                                                                                                                                                       SYSTEM                        BACKUP
                                                                                                                                                        RAM                           RAM
                                                               FDPLL200M



        The SAM D5x/E5x power domains are not independent of each other:
          • VDDCORE, VDDIO and VDDIOB share GND, whereas VDDANA refers to GNDANA.
          • VDDANA and VDDIO must share the main supply, VDD.
          • VDDCORE pin is just an output for monitoring the internal voltage regulator. This is not an input for
            an external supply.
          • VSWOUT, VSW and VDDBU are internal power domains.
          • The VSW pin is for inductor connection to run the Main Voltage Regulator in switching mode.



7.2     Power Supply Considerations

7.2.1   Power Supplies
        The SAM D5x/E5x has the following power supply pins:
          • VDDIO – Powers I/O lines, XOSCn and the internal regulator for VDDCORE. Voltage is 1.71V to
            3.63V.
          • VDDIOB – Powers I/O B lines. Voltage is 1.71V to 3.63V.
          • VDDANA – Powers I/O lines, the Automatic Power Switch, ADC0/1, AC, DAC and PTC. Voltage is
            1.71V to 3.63V.
          • VBAT – Powers the Automatic Power Switch. Voltage is 1.71V to 3.63V




        © 2019 Microchip Technology Inc.                                                              Datasheet                                                                                      DS60001507E-page 47
                                                         SAM D5x/E5x Family Data Sheet
                                                                              Power Supply and Start-Up ...

          • VDDCORE – Serves as the internal voltage regulator output in linear mode, depending on the
            powering configuration. It powers the VSW core power domain and the VDDBU backup domain,
            memories, peripherals, DFLL48M, FDPLL200M, and RAMs. Voltage is 1.2V typical.
          • The Automatic Power Switch is a configurable switch that selects between VDD and VBAT as supply
            for the internal output VSWOUT, see the figure in 7.1 Power Domain Overview.
        The same voltage must be applied to both VDDIO and VDDANA. This common voltage is referred to as
        VDD in the data sheet.
        VDDIOB voltage level must be equal or lower than VDDIO.
        The ground pins, GND, are common to VDDCORE, and VDDIO. The ground pin for VDDANA is
        GNDANA.
        For decoupling recommendations for the different power supplies, refer to the schematic checklist.
        Related Links
        59. Schematic Checklist
        6.2.9 GPIO Clusters
        7.2.3 Typical Powering Schematic

7.2.2   Voltage Regulator
        The SAM D5x/E5x internal Main Voltage Regulator has three different modes:
          • Linear mode: This is the default mode when CPU and peripherals are running. It does not require an
            external inductor.
          • Switching mode. This is the most power efficient mode when the CPU and peripherals are running.
            This mode can be selected by software on the fly.
          • Shutdown mode. When the chip is in backup mode, the internal regulator is off, the VSW core power
            domain is OFF. The VDDBU backup domain is powered by the backup regulator (LPVREG).
        Note that the Voltage Regulator modes are controlled by the Power Manager.

7.2.3   Typical Powering Schematic
        The SAM D5x/E5x uses a single supply from 1.71V to 3.63V.
        The following figure shows the recommended power supply connection.
        Figure 7-2. Power Supply Connection for Linear Mode Only
                                                                     DEVICE
                                                                                    VBAT (PB03)
                                                     VDDANA
                                Main Supply
                                (1.71V — 3.63V)

                                                      VDDIO



                                                       VSW

                                                   VDDCORE


                                                        GND


                                                    GNDANA




        © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 48
                                                            SAM D5x/E5x Family Data Sheet
                                                                                Power Supply and Start-Up ...

          Figure 7-3. Power Supply Connection for Switching/Linear Mode
                                                                       DEVICE
                                                                                      VBAT (PB03)

                                 Main Supply          VDDANA
                                 (1.71V — 3.63V)

                                                        VDDIO




                                                         VSW

                                                     VDDCORE


                                                          GND


                                                      GNDANA




          Figure 7-4. Power Supply Connection for Battery Backup
                                                                       DEVICE
                                                                                      VBAT (PB03)

                                 Main Supply          VDDANA
                                 (1.71V — 3.63V)

                                                        VDDIO




                                                         VSW

                                                     VDDCORE


                                                          GND


                                                      GNDANA




7.2.4     Power-Up Sequence

7.2.4.1   Supply Order
          VDDIO and VDDANA must have the same supply sequence, and must be connected together.
          Note that VDDIO supplies the XOSCn, so VDDIO must be present before the applicaion uses the XOSC
          feature. This is also applicable to all digital features present on pins supplied by VDDIO. VDDIOB must
          be present before the application uses features present on pins supplied by VDDIOB.
7.2.4.2   Minimum Rise Rate
          One integrated power-on reset (POR) circuits monitoring VDDANA requires a minimum rise rate.
7.2.4.3   Maximum Rise Rate
          The rise rate of the power supplies must not exceed the values described in Electrical Characteristics.



7.3       Power-Up
          This section summarizes the power-up sequence of the SAM D5x/E5x. The behavior after power-up is
          controlled by the Power Manager.
          Related Links




          © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 49
                                                            SAM D5x/E5x Family Data Sheet
                                                                                Power Supply and Start-Up ...

        18. PM – Power Manager

7.3.1   Starting of Internal Regulator
        After power-up, the device is set to its initial state and kept in Reset, until the power has stabilized
        throughout the device.
        The internal regulator provides VDDCORE. Once the external voltage VDDIO/VDDANA and VDDCORE
        reach a stable value, the internal Reset is released.
        Related Links
        18. PM – Power Manager

7.3.2   Starting of Clocks
        Once the power has stabilized and the internal Reset is released, the device will use a 48MHz clock by
        default. The clock source for this clock signal is DFLL48M, which is enabled after a reset by default. This
        is also the default time base for Generic Clock Generator 0. In turn, Generator 0 provides the main clock
        GCLK_MAIN which is used by the Main Clock module (MCLK).
        Some synchronous system clocks are active after Start-Up, allowing software execution. Refer to the
        “Clock Mask Registers” section in the MCLK-Main Clock documentation for the list of clocks that are
        running by default. Synchronous system clocks that are running receive the 48MHz clock from Generic
        Clock Generator 0. Other generic clocks are disabled.
        Related Links
        18. PM – Power Manager

7.3.3   I/O Pins
        After power-up, the I/O pins are tri-stated except PA30, which is pull-up enabled and configured as input
        in order to serve as part of the debug interface.

7.3.4   Fetching of Initial Instructions
        After Reset has been released, the CPU starts fetching PC and SP values from the Reset address,
        0x00000000. This points to the first executable address in the internal Flash memory. The code read from
        the internal Flash can be used to configure the clock system and clock sources. See the related
        peripheral documentation for details. Refer to the ARM Architecture Reference Manual for more
        information on CPU startup (http://www.arm.com).



7.4     Power-On Reset and Brown-Out Detector
        The SAM D5x/E5x embeds three features to monitor, warn and/or reset the device:
         • POR: Power-on Reset on the main supply VDD (VDDANA/VSWOUT).
         • BOD33: Brown-out detector on VSWOUT/VBAT
         • Brown-out detector internal to the voltage regulator for VDDCORE. BOD12 is calibrated in production
            and its calibration parameters are stored in the NVM User Row. This data should not be changed if
            the User Row is written to in order to assure correct behavior.

7.4.1   Power-On Reset on VSWOUT
        VSWOUT is monitored by POR. Monitoring is always activated, including startup and all sleep modes. If
        VSWOUT goes below the threshold voltage, the entire chip is reset.




        © 2019 Microchip Technology Inc.                      Datasheet                             DS60001507E-page 50
                                                       SAM D5x/E5x Family Data Sheet
                                                                         Power Supply and Start-Up ...

7.4.2   Power-On Reset on the main supply VDD (VDDANA/VDDIO)
        The Main supply VDD (VDDANA/VDDIO) is monitored by POR. Monitoring is always activated, including
        startup and all sleep modes. If VDD goes below the threshold voltage, all I/Os supplied by VDDIO are
        reset.

7.4.3   Brown-Out Detector on VSWOUT/VBAT
        BOD33 monitors VSWOUT or VBAT depending on configuration.
        Related Links
        19. SUPC – Supply Controller

7.4.4   Brown-Out Detector on VDDCORE
        Once the device has started up, BOD12 monitors the internal VDDCORE.
        Related Links
        19. SUPC – Supply Controller




        © 2019 Microchip Technology Inc.                Datasheet                          DS60001507E-page 51
