# 50. PTC - Peripheral Touch Controller

*Source: `Atmel-SAMD51.pdf`, pages 1884-1887 — SAMD51 family datasheet*

                                                        SAM D5x/E5x Family Data Sheet
                                                                      PTC - Peripheral Touch Controller


50.    PTC - Peripheral Touch Controller

50.1   Overview
       The Peripheral Touch Controller (PTC) acquires signals in order to detect a touch on the capacitive
       sensors. The external capacitive touch sensor is typically formed on a PCB, and the sensor electrodes
       are connected to the analog front end of the PTC through the I/O pins in the device. The PTC supports
       both self and mutual capacitance sensors.
       In the Mutual Capacitance mode, sensing is done using capacitive touch matrices in various X-Y
       configurations, including indium tin oxide (ITO) sensor grids. The PTC requires one pin per X-line and one
       pin per Y-line.
       In the Self Capacitance mode, the PTC requires only one pin (Y-line) for each touch sensor.
       The number of available pins and the assignment of X- and Y-lines is depending on both package type
       and device configuration. Refer to the Configuration Summary and I/O Multiplexing table for details.
       Related Links
       6. I/O Multiplexing and Considerations



50.2   Features
         • Low-Power, High-Sensitivity, Environmentally Robust Capacitive Touch Buttons, Sliders, and Wheels
         • Supports Wake-up on Touch from sleep mode Sleep mode
         • Supports Mutual Capacitance and Self Capacitance Sensing
            – Mix-and-Match Mutual and Self Capacitance Sensors
         • One Pin per Electrode – No External Components
         • Load Compensating Charge Sensing
            – Parasitic capacitance compensation and adjustable gain for superior sensitivity
         • Zero Drift Over the Temperature and VDD Range
            – Auto calibration and recalibration of sensors
         • Single-shot and free-running Charge Measurement
         • Hardware Noise Filtering and Noise Signal Desynchronization for High Conducted Immunity
         • Selectable channel change delay allows choosing the settling time on a new channel, as required
         • Acquisition-start triggered by command or through auto-triggering feature
         • Low CPU utilization through interrupt on acquisition-complete
         • Using ADC peripheral for signal conversion and acquisition
       Related Links
       6. I/O Multiplexing and Considerations




       © 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1884
                                                               SAM D5x/E5x Family Data Sheet
                                                                              PTC - Peripheral Touch Controller


50.3   Block Diagram
       Figure 50-1. PTC Block Diagram Mutual Capacitance


                                                 Input              Compensation
                                                Control                Circuit


                                               Y0
                                               Y1              RS
                                                                                      Charge         ADC          IRQ
                                                                                     Integrator     System
                                               Ym                                                                 Result
                                                                                                             10

        CX0Y0
                                               X0


       C XnYm                                  X1                    X Line Driver
                                               Xn



       Figure 50-2. PTC Block Diagram Self Capacitance


                                             Input             Compensation
                                            Control               Circuit


                                          Y0
                                          Y1              RS
                                                                                 Charge             ADC           IRQ
       CY0                                                                      Integrator         System
                                          Ym                                                                      Result
                                                                                                             10


                 CYm


                                                                X Line Driver




50.4   Signal Description
       Table 50-1. Signal Description for PTC

        Name                      Type                     Description
        Y[m:0]                    Analog                   Y-line (Input/Output)
        X[n:0]                    Digital                  X-line (Output)

       Note: The number of X- and Y-lines are device dependent. Refer to Configuration Summary for details.




       © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1885
                                                           SAM D5x/E5x Family Data Sheet
                                                                         PTC - Peripheral Touch Controller

         Refer to I/O Multiplexing and Considerations for details on the pin mapping for this peripheral. One signal
         can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



50.5     System Dependencies
         In order to use this peripheral, configure the other components of the system as described in the following
         sections.

50.5.1   I/O Lines
         The I/O lines used for analog X- and Y-lines must be connected to external capacitive touch sensor
         electrodes. External components are not required for normal operation. However, to improve the EMC
         performance, a series resistor of 1 kΩ or more can be used on X- and Y-lines.
50.5.1.1 Mutual Capacitance Sensor Arrangement
         A mutual capacitance sensor is formed between two I/O lines - an X electrode for transmitting and Y
         electrode for sensing. The mutual capacitance between the X and Y electrode is measured by the
         peripheral touch controller.
         Figure 50-3. Mutual Capacitance Sensor Arrangement
                                                                               Sensor Capacitance Cx,y
                  MCU
                                                                             Cx0,y0   Cx0,y1   Cx0,ym
                                            X0

                                                                             Cx1,y0   Cx1,y1   Cx1,ym
                                            X1
                                                                             Cxn,y0   Cxn,y1   Cxn,ym
                                            Xn
                                       PTC
                                       PTC
                                      Module
                                      Module
                                            Y0

                                            Y1

                                            Ym



50.5.1.2 Self Capacitance Sensor Arrangement
         A self capacitance sensor is connected to a single pin on the peripheral touch controller through the Y
         electrode for sensing the signal. The sense electrode capacitance is measured by the peripheral touch
         controller.




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 1886
                                                            SAM D5x/E5x Family Data Sheet
                                                                        PTC - Peripheral Touch Controller

         Figure 50-4. Self-Capacitance Sensor Arrangement

                                  MCU
                                                                   Sensor Capacitance Cy

                                                       Y0
                                                                                  Cy0

                                                       Y1
                                                                                  Cy1
                                                   PTC
                                                  Module

                                                       Ym                         Cym




         For more information about designing the touch sensor, refer to Buttons, Sliders and Wheels Touch
         Sensor Design Guide.

50.5.2   Analog-Digital Converter (ADC)
         The PTC is using the ADC for signal conversion and acquisition. The ADC must be enabled and
         configured appropriately to allow correct behavior of the PTC.
         Related Links
         45. ADC – Analog-to-Digital Converter



50.6     Functional Description
         In order to access the PTC, the user must use the Atmel|START QTouch® Configurator to configure and
         link the QTouch Library firmware with the application software. QTouch Library can be used to implement
         buttons, sliders, and wheels in a variety of combinations on a single interface.
         Figure 50-5. QTouch Library Usage

             Custom Code                    Compiler


                                                                           Link                    Application


                                            QTouch
                                            Library

         For more information about QTouch Library, refer to the QTouch Library Peripheral Touch Controller User
         Guide.




         © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 1887
