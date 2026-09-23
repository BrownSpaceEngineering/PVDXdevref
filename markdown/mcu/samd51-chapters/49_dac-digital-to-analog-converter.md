# 47. DAC – Digital-to-Analog Converter

*Source: `Atmel-SAMD51.pdf`, pages 1671-1709 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                        DAC – Digital-to-Analog Converter


47.    DAC – Digital-to-Analog Converter

47.1   Overview
       The Digital-to-Analog Converter (DAC) converts a digital value to a voltage. The DAC Controller controls
       two DACs, which can operate either as two independent DACs or as a single DAC in differential mode.
       Each DAC is 12-bit resolution and is capable of converting up to 1,000,000 samples per second (MSPS).



47.2   Features
         •   Two independent DACs or single DAC in differential mode
         •   DAC with 12-bit resolution
         •   Integrated or Standalone filters with 2x, 4x, 8x, 16x, or 32x oversampling rate (OSR)
         •   Up to 1MSPS conversion rate
         •   Hardware support for 16-bit using dithering
         •   Multiple trigger sources
         •   High-drive capabilities
         •   DAC0 used as internal input
         •   DMA support



47.3   Block Diagram
       Figure 47-1. DAC Controller Block Diagram


                        DATABUF0                                                                Internal input
                                          DITH0          SINC0
                           DATA0                                           DAC0                        VOUT0


                                                                                                       VREFA
                                     DAC Controller
                                                                                            VDDANA
                        DATABUF1                                                            Ref.voltage (VREF)
                                          DITH1          SINC1
                           DATA1                                           DAC1                        VOUT1




47.4   Signal Description
        Signal                   Description                                   Type
        VOUT0                    DAC0 output                                   Analog output
        VOUT1                    DAC1 output                                   Analog output




       © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1671
                                                             SAM D5x/E5x Family Data Sheet
                                                                           DAC – Digital-to-Analog Converter

         ...........continued
          Signal                   Description                                    Type
          VREFA                    External reference                             Analog input

         One signal can be mapped on several pins.


                        Important:
                        When an analog peripheral is enabled, the analog output of the peripheral will interfere with the
                        alternative functions of the output pads. This is also true even when the peripheral is used for
                        internal purposes.
                        Analog inputs do not interfere with alternative pad functions.


         Related Links
         6. I/O Multiplexing and Considerations



47.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

47.5.1   I/O Lines
         Using the DAC Controller’s I/O lines requires the I/O pins to be configured in the PORT - I/O Pin
         Controller.
         Table 47-1. I/O Lines

          Instance                          Signal            Peripheral Function
          DAC                               VOUT0             A
          DAC                               VOUT1             A
          DAC                               VREFA             A

47.5.2   Power Management
         The DAC Controller will continue to operate in any sleep mode where the selected source clock is
         running.
         The DAC Controller interrupts can be used to wake up the device from sleep modes.
         Events connected to the event system can trigger other operations in the system without exiting sleep
         modes.

         Related Links
         18. PM – Power Manager

47.5.3   Clocks
         The DAC bus clock (CLK_DAC_APB) can be enabled and disabled in the Main Clock module, and the
         default state of CLK_DAC_APB can be found in Peripheral Clock Masking.
         A generic clock (GCLK_DAC) is required to clock the DAC Controller. This clock must be configured and
         enabled in the generic clock controller before using the DAC Controller.




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1672
                                                            SAM D5x/E5x Family Data Sheet
                                                                         DAC – Digital-to-Analog Converter

         This generic clock is asynchronous to the bus clock (CLK_DAC_APB). Due to this asynchronicity, writes
         to certain registers will require synchronization between the clock domains. Refer to 47.6.8
         Synchronization for further details.
         Related Links
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller

47.5.4   DMA
         The DMA request line is connected to the DMA Controller (DMAC). Using the DAC Controller DMA
         requests requires to configure the DMAC first.
         Related Links
         22. DMAC – Direct Memory Access Controller

47.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the DAC Controller interrupts
         requires the interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller
         10.2 Nested Vector Interrupt Controller

47.5.6   Events
         The events are connected to the Event System.
         Related Links
         31. EVSYS – Event System

47.5.7   Debug Operation
         When the CPU is halted in debug mode the DAC will halt normal operation. Any on-going conversions will
         be completed. The DAC can be forced to continue normal operation during debugging. If the DAC is
         configured in a way that requires it to be periodically serviced by the CPU through interrupts or similar,
         improper operation or data loss may result during debugging.
         Related Links
         47.8.15 DBGCTRL

47.5.8   Register Access Protection
         All registers with write access can be write-protected optionally by the Peripheral Access Controller
         (PAC), except for the following registers:
           • Interrupt Flag Status and Clear (INTFLAG) register
           • Data Buffer (DATABUFx) registers
         Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
         Protection" property in each individual register description.
         PAC write protection does not apply to accesses through an external debugger.
         Related Links
         27. PAC - Peripheral Access Controller




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1673
                                                             SAM D5x/E5x Family Data Sheet
                                                                           DAC – Digital-to-Analog Converter

47.5.9    Analog Connections
          The DAC has up to two analog output pins (VOUT0, VOUT1) and one analog input pin (VREFA) that
          must be configured first.
          When an internal input is used, it must be enabled before DAC Controller is enabled.
          The analog signals of AC, ADC, DAC and OPAMP can be interconnected.
          See Analog Connections of Peripherals for details.


47.6      Functional Description

47.6.1    Principle of Operation
          Each DAC converts the digital value located in the Data register (DATA0 or DATA1) into an analog
          voltage on the DAC output (VOUT0 or VOUT1, respectively).
          A conversion is started when new data is loaded to the Data register. The resulting voltage is available on
          the DAC output after the conversion time. A conversion can also be started by input events from Event
          System.

47.6.2    Basic Operation
47.6.2.1 Initialization
          The following registers are enable-protected, meaning they can only be written when the DAC Controller
          is disabled (CTRLA.ENABLE=0):
           •   Control B register (CTRLB)
           •   Event Control register (EVCTRL)
           •   DAC0 Control (DACCTRL0)
           •   DAC1 Control (DACCTRL1)
          Enable-protection is denoted by the Enable-Protected property in the register description.
47.6.2.2 Enabling, Disabling and Resetting
          The DAC Controller is enabled by writing a '1' to the Enable bit in the Control A register
          (CTRLA.ENABLE). The DAC Controller is disabled by writing a '0' to CTRLA.ENABLE.
          The DAC Controller is reset by writing '1' to the Software Reset bit in the Control A register
          (CTRLA.SWRST). All registers in the DAC will be reset to their initial state, and the DAC Controller will be
          disabled. Refer to 47.8.1 CTRLA for details.
47.6.2.3 DAC Configuration
          Each individual DAC is configured by its respective DAC Control register (DACCTRLx)). These settings
          are applied when DAC Controller is enabled and can be changed only when DAC Controller is disabled.
           • Enable the selected DAC by writing a '1' to DACCTRLx.ENABLE.
           • Select the data alignment with DACCCTRLx.LEFTADJ. Writing a '1' will left-align the data
             (DATABUFx/DATAx[31:20]). Writing a '0' to LEFTADJ will right-align the data (DATABUFx/
             DATAx[11:0]).
           • If operation in standby mode is desired for DACx, write a '1' to the Run in Standby bit in the DAC
             Control register (DACCCTRLx.RUNSTDBY). If RUNSTDBY=1, DACx continues normal operation
             when system is in standby mode. If RUNSTDBY=0, DACx is halted in standby mode.
           • Select dithering mode with DACCCTRLx.DITHER. Writing '1' to DITHER will enable dithering mode,
             writing a '0' will disable it. Refer to 47.6.9.5 Dithering Mode for details.




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1674
                                                               SAM D5x/E5x Family Data Sheet
                                                                           DAC – Digital-to-Analog Converter

          • Select the refresh period with the Refresh Period bit field in DACCCTRLx.REFRESH[3:0]. Writing
            any value greater than '1' to the REFRESH bit field will enable and select the refresh mode. Refer to
            47.6.9.3 Conversion Refresh for details.
          • Select the output buffer current according to data rate (for low power application) with the Current
            Control bit field DACCTRLx.CCTRL[1:0]. Refer to 47.6.9.2 Output Buffer Current Control for details.
          • Select standalone filter usage by writing to DACCTRLx.FEXT. Writing FEXT=1 selects a standalone
            filter, FEXT=0 selects the filter integrated to the DAC. See also 47.6.9.6 Interpolation Mode for
            details.
          • Select the filter oversampling ratio by writing to DACCTRLx.OSR[2:0]. writing OSR=0 selects no
            oversampling; writing any other value will enable interpolation of input data. See also 47.6.9.6
            Interpolation Mode for details.
         Once the DAC Controller is enabled, DACx requires a startup time before the first conversion can start.
         The DACx Startup Ready bit in the Status register (STATUS.READYx) indicates that DACx is ready to
         convert a data when STATUS.READYx=1.
         Conversions started while STATUS.READYx=0 shall be discarded.
         VOUTx is at tri-state level if DACx is not enabled.
47.6.2.4 Digital to Analog Conversion
         Each DAC converts a digital value (stored in DATAx register) into an analog voltage. The conversion
         range is between GND and the selected DAC voltage reference VREF. The default source for VREF is
         the internal reference voltage VREF. Other voltage reference options are the analog supply voltage
         (VDDANA) and the external voltage reference (VREFA). The voltage reference is selected by writing to
         the Reference Selection bits in the Control B register (CTRLB.REFSEL).
         The output voltage from the DAC can be calculated using the following formula:
                   DATAx
         �OUTx =         × VREF
                    4095
         A new conversion starts as soon as a new value is loaded into DATAx. DATAx can either be loaded via
         the APB bus during a CPU write operation, using DMA, or from the DATABUFx register when a STARTx
         event occurs.
         Refer to 47.5.6 Events for details. Even if both DAC use the same GCLK, each data conversion can be
         started independently.
         The conversion time is given by the period TGCLK of the generic clock GCLK_DAC and the number of bits:
         �CONV = 12 × 2 × �GCLK

         The End Of Conversion bit in the Status register indicates that a conversion is completed
         (STATUS.EOCx=1). This means that VOUTx is stable.




        © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1675
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                             DAC – Digital-to-Analog Converter

         Figure 47-2. Single DAC Conversion
                                          t0                                     t12                                t24
               GCLK_DAC



                   DATAx          0x3FF          0xFFF


                   Start of
                Conversion


            STATUS.EOCx


                   0xFFF      VREF


                   0x7FF      VREF/2
                                               VOUTx

                   0x000      0

                                                                       T CONV

         Since the DAC conversion is implemented as pipelined procedure, a new conversion can be started after
         only 12 GCLK_DAC periods. Therefore if DATAx is written while a conversion is ongoing, start of
         conversion is postponed until DACx is ready to start next conversion.
         The maximum conversion rate (samples per second) is therefore:
                      2
         CRmax =
                    �conv

         Figure 47-3. Multiple DAC Conversions
                                          t0                     t12             t24               t36               t48
               GCLK_DAC                          ...                     ...           ...                 ...             ...


                   DATAx          0x000        0x3FF                   0x7FF                             0xFFF


                   Start of
               Conversion


            STATUS.EOCx


                   0xFFF      VREF


                   0x7FF      VREF/2


                   0x000      0                VOUTx


                                                       T CONV0                                            T CONV2

                                                                       T CONV1

         Related Links
         19. SUPC – Supply Controller

47.6.3   Operating Conditions
           • The DAC voltage reference must be below VDDANA.
           • The maximum conversion rate of 1MSPS can be achieved only if VDDANA is above 2.4V.




         © 2019 Microchip Technology Inc.                                 Datasheet                                 DS60001507E-page 1676
                                                            SAM D5x/E5x Family Data Sheet
                                                                          DAC – Digital-to-Analog Converter

           • The frequency of GCLK_DAC must be equal or lower than 12MHz (corresponding to 1MSPS).

47.6.4   DMA Operation
         In single mode (CTRLB.DIFF=0), DAC Controller generates the following DMA requests:
           • Data Buffer 0 Empty (EMPTY0): The request is set when data is transferred from DATABUF0 or
             DATA0 to the internal data buffer of DAC0. The request is cleared when either DATA0 register or
             DATABUF0 register is written, or by writing a '1' to the EMPTY0 bit in the Interrupt Flag register
             (INTFLAG.EMPTY0).
           • Data Buffer 1 Empty (EMPTY1): The request is set when data is transferred from DATABUF1 or
             DATA1 to the internal data buffer of DAC1. The request is cleared when either DATA0 register or
             DATABUF1 register is written, or by writing a one to the EMPTY1 bit in the Interrupt Flag register
             (INTFLAG.EMPTY1).
           • Filter 0 Result Ready (RESRDY0): The request is set when the filter is used as standalone, and filter
             output is ready. The request is cleared by writing a '1' to the RESRDY0 bit in the Interrupt Flag
             register (INTFLAG.RESRDY0).
           • Filter 1 Result Ready (RESRDY1): The request is set when the filter is used as standalone, and filter
             output is ready. The request is cleared by writing a '1' to the RESRDY1 bit in the Interrupt Flag
             register (INTFLAG.RESRDY1).
         In differential mode (CTRLB.DIFF=1), DAC Controller generates the following DMA request:
           • Data Buffer 0 Empty (EMPTY0): The request is set when data is transferred from DATABUF0 or
             DATA0 to the internal data buffer of DAC1. The request is cleared when either DATA0 register or
             DATABUF0 register is written, or by writing a one to the EMPTY0 bit in the Interrupt Flag register
             (INTFLAG.EMPTY0).
         If the CPU accesses the registers which are source of DMA request set/clear condition, the DMA request
         can be lost or the DMA transfer can be corrupted, if enabled.

47.6.5   Interrupts
         The DAC Controller has the following interrupt sources:
           • DAC0 Data Buffer Empty (EMPTY0): Indicates that the internal data buffer of DAC0 is empty.
           • DAC1 Data Buffer Empty (EMPTY1): Indicates that the internal data buffer of DAC1 is empty.
           • DAC0 Underrun (UNDERRUN0): Indicates that the internal data buffer of DAC0 is empty and a
             DAC0 start of conversion event occurred. Refer to 47.5.6 Events for details.
           • DAC1 Underrun (UNDERRUN1): Indicates that the internal data buffer of DAC1 is empty and a
             DAC1 start of conversion event occurred. Refer to 47.5.6 Events for details.
           • Filter 0 Result Ready (RESRDY0): Indicates that Filter 0 result is ready if set as standalone filter.
           • Filter 1 Result Ready (RESRDY1): Indicates that Filter 1 result is ready if set as standalone filter.
           • Filter 0 Overrun (OVERRUN0): Indicates that the DMA request has not been cleared while the
             RESULT0 register gets new data.
           • Filter 1 Overrun (OVERRUN1): Indicates that the DMA request has not been cleared while the
             RESULT1 register gets new data.
         These interrupts are asynchronous wake-up sources.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a '1' to the corresponding bit in the Interrupt Enable Set (INTENSET)




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1677
                                                            SAM D5x/E5x Family Data Sheet
                                                                          DAC – Digital-to-Analog Converter

         register, and disabled by writing a '1' to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
         register.
         An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is enabled.
         The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or the DAC
         Controller is reset. See 47.8.6 INTFLAG for details on how to clear interrupt flags.
         All interrupt requests from the peripheral are ORed together on system level to generate one combined
         interrupt request to the NVIC. The user must read the INTFLAG register to determine which interrupt
         condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated.

47.6.6   Events
         The DAC Controller can generate the following output events:
           • Data Buffer 0 Empty (EMPTY0): Generated when the internal data buffer of DAC0 is empty. Refer to
             47.6.4 DMA Operation for details.
           • Data Buffer 1 Empty (EMPTY1): Generated when the internal data buffer of DAC1 is empty. Refer to
             47.6.4 DMA Operation for details.
           • Filter 0 Result Ready (RESRDY0): Generated when standalone filter 0 result is ready.
           • Filter 1 Result Ready (RESRDY1): Generated when standalone filter 1 result is ready.
         Writing a '1' to an Event Output bit in the Event Control Register (EVCTRL.EMPTYEOx) enables the
         corresponding output event. Writing a '0' to this bit disables the corresponding output event. Refer to the
         Event System chapter for details on configuring the event system.
         The DAC Controller can take the following actions on an input event:
           • DAC0 Start Conversion (START0): DATABUF0 value is transferred into DATA0 as soon as DAC0 is
             ready for the next conversion, and then conversion is started. START0 is considered as
             asynchronous to GCLK_DAC, thus it is resynchronized in the DAC Controller. Refer to 47.6.2.4
             Digital to Analog Conversion for details.
           • DAC1 Start Conversion (START1): DATABUF1 value is transferred into DATA1 as soon as DAC1 is
             ready for the next conversion, and then conversion is started. START1 is considered as
             asynchronous to GCLK_DAC, thus it is resynchronized in the DAC Controller. Refer to 47.6.2.4
             Digital to Analog Conversion for details.
         Writing a '1' to an Event Input bit in the Event Control register (EVCTRL.STARTEIx) enables the
         corresponding action on input event. Writing a '0' to this bit will disable the corresponding action on input
         event.
         Note: When several events are connected to the DAC Controller, the enabled action will be taken on
         any of the incoming events.
         By default, DAC Controller detects rising edge events. Falling edge detection can be enabled by writing
         '1' to EVCTRL.INVEIx.
         Note that if an event occurs before startup time is completed, DATAx is loaded but start of conversion is
         ignored.

47.6.7   Sleep Mode Operation
         If the Run In Standby bit in the DAC Control x register DACCCTRLx.RUNSTDBY=1, the DACx will
         continue the conversions in standby sleep mode.
         If DACCCTRLx.RUNSTDBY=0, the DACx will stop conversions in standby sleep mode.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1678
                                                             SAM D5x/E5x Family Data Sheet
                                                                         DAC – Digital-to-Analog Converter

         If DACx conversion is stopped in standby sleep mode, DACx is also disabled to reduce power
         consumption. When exiting standby sleep mode, DACx is enabled again, therefore a certain startup time
         is required before starting a new conversion.
         DAC Controller is compatible with SleepWalking: if RUNSTDBY=1, when an input event (STARTx) is
         detected in sleep mode, the DAC Controller will request GCLK_DAC in order to complete the conversion.

47.6.8   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         An exception is the Channel Enable bit in the Peripheral Channel Control registers (PCHCTRLm.CHEN).
         When changing this bit, the bit value must be read-back to ensure the synchronization is complete and to
         assert glitch free internal operation. Note that changing the bit value under ongoing synchronization will
         not generate an error.
         The following bits are synchronized when written:
           • Software Reset bit in control register (CTRLA.SWRST)
           • Enable bit in control register (CTRLA.ENABLE)
         The following registers are synchronized when written:
           •   DAC0 data register (DATA0)
           •   DAC1 data register (DATA1)
           •   DAC0 data buffer register (DATABUF0)
           •   DAC1 data buffer register (DATABUF1)
         Required write synchronization is denoted by the "Write-Synchronized" property in the register
         description.
         Related Links
         13.3 Register Synchronization

47.6.9   Additional Features

47.6.9.1 DAC0 as Internal Input
         The analog output of DAC0, VOUT0, is internally available as input signal for other peripherals (AC, ADC,
         and OPAMP) when DAC0 is enabled.
         Note: The pin VOUT0 will be dedicated as internal input and cannot be configured as alternate function.

47.6.9.2 Output Buffer Current Control
         Power consumption can be reduced by controlling the output buffer current, according to conversion rate.
         Writing to the Current Control bits in DAC Control x register (DACCTRLx.[1:0]) will select an output buffer
         current.
         Related Links
         47.8.9 DACCTRL0
         47.8.10 DACCTRL1

47.6.9.3 Conversion Refresh
         Conversion Refresh only works when the input data is not interpolated, i.e. the Oversampling Rate in the
         DAC Control register is zero (DACCTRLx.OSR=0x0).




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1679
                                                              SAM D5x/E5x Family Data Sheet
                                                                            DAC – Digital-to-Analog Converter

         The DAC can only maintain its output within one LSB of the desired value for approximately 100µs. When
         a DAC is used to generate a static voltage or at a rate less than 20kSPS, the conversion must be
         refreshed periodically. The OSCULP32K clock can start new conversions automatically after a specified
         period. Write a value to the Refresh bit field in the DAC Control x register (DACCTRLx.REFRESH[3:0]) to
         select the refresh period according to the formula:
         �REFRESH = REFRESH × �OSCULP32K

         The actual period will depend on the tolerance of the OSCULP32K (see Electrical Characteristics).
         If DACCTRLx.REFRESH=0, there is no conversion refresh. DACCTRLx.REFRESH=1 is Reserved.
         If no new conversion is started before the refresh period is completed, DACx will convert the DATAx value
         again.
         In standby sleep mode, the refresh mode remains enabled if DACCTRLx.RUNSTDBY=1.
         If DATAx is written while a refresh conversion is ongoing, the conversion of the new content of DATAx is
         postponed until DACx is ready to start the next conversion.
47.6.9.4 Differential Mode
         DAC0 and DAC1 can be configured to operate in differential mode, i.e. the combined output is a voltage
         balanced around VREF/2, see also the figure below.
         In differential mode, DAC0 and DAC1 are converting synchronously the DATA0 value. DATA0 must
         therefore be a signed value, represented in two’s complement format with DATA0[11] as the signed bit.
         DATA0 has therefore the range [-2047:2047].
         VOUT0 is the positive output and VOUT1 the negative output. The differential output voltage is therefore:
                  DATA0
         �OUT =         × VREF = �OUT0 − �OUT1
                   2047
         DACCTRL0 serves as the configuration register for both DAC0 and DAC1. Therefore DACCTRL1 does
         not need to be written.
         The differential mode is enabled by writing a '1' to the Differential bit in the Control B register
         (CTRLB.DIFF).
         Figure 47-4. DAC Conversions in Differential Mode
                                DATA0
                          2047 (0xFFF)     VREF


                                                        VOUT0

                              0 (0x800)    VREF/2

                                                        VOUT1



                          -2047 (0x000)    0




        © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 1680
                                                                                        SAM D5x/E5x Family Data Sheet
                                                                                                                  DAC – Digital-to-Analog Converter

47.6.9.5 Dithering Mode
         Dithering is enabled by setting DACCTRLx.DITHER to 1. In dithering mode, DATAx is a 16-bit unsigned
         value where DATAx[15:4] is the 12-bit data converted by DAC and DATAx[3:0] represent the dither bits,
         used to minimize the quantization error.
         The principle is to make 16 sub-conversions of the DATAx[15:4] value or the (DATAx[15:4] + 1) value, so
         that by averaging those two values, the conversion result of the 16-bit value (DATAx[15:0]) is accurate.
         To operate, the STARTx event must be configured to generate 16 events for each DATAx[15:0]
         conversion, and DATABUFx must be loaded every 16 DAC conversions. EMPTYx event and DMA
         request are therefore generated every 16 DATABUFx to DATAx transfer. STATUS.EOCx still reports end
         of each sub-conversions.
         Following timing diagram shows examples with DATA0[15:0] = 0x1204 followed by DATA0[15:0] =
         0x1238.
         Figure 47-5. DAC Conversions in Dithering Mode
                          DATA0[15:0]


                                0x1240
                                                                                                                                                               0x1238
                                0x1230

                                                                                     VOUT0
                                0x1210
                                0x1200                                                              0x1204

                              sub-conversion   1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16 1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16



47.6.9.6 Interpolation Mode
         The DAC provides interpolation that allows for oversampling ratios (OSR) of 2x, 4x, 8x, 16x or 32x.
         Interpolation mode is selected by writing a non-zero value to the Oversampling Ratio bits in the DACx
         Control register (DACCTRLx.OSR).
         The data is sampled once over OSR trigger events and then recomputed at the trigger sample rate using
         a third-order SINC filter.
         The figures below show the spectral mask of the SINC filter depending on the selected OSR. �� is the
         sampling frequency of the input signal which corresponds to the trigger frequency divided by OSR.
         The Filter usage bit DACCTRLx.FEXT determines whether the filter is integrated to the corresponding
         DAC or used as a standalone filter driven by DMA. If DACCTRLx.FEXT=0, the DAC takes the filter output
         while the value of RESULTx is reading zero. Conversely, If DACCTRLx.FEXT=1, the DAC value remains
         zero, and the value of RESULTx register reflects the filter output.




        © 2019 Microchip Technology Inc.                                                   Datasheet                                                            DS60001507E-page 1681
                                                                                                                             SAM D5x/E5x Family Data Sheet
                                                                                                                                                                     DAC – Digital-to-Analog Converter

Figure 47-6. Interpolator Spectral Mask for 2x OSR
                                                        3rd order SINC filter overall mask for OSR = 2                                                                        3rd order SINC filter 0–fs/2 mask for OSR = 2
                                    0                                                                                                                       0




                                   -24                                                                                                                    -2.4
        gain (dB), overall mask




                                                                                                                                 gain (dB), 0–fs/2 mask
                                   -48                                                                                                                    -4.8




                                   -72                                                                                                                    -7.2




                                   -96                                                                                                                    -9.6




                                  -120                                                                                                                    -12
                                         0   0.125*fs   0.25*fs   0.375*fs   0.5*fs   0.625*fs   0.75*fs   0.875*fs   1*fs                                       0    fs/16   fs/8     3*fs/16    fs/4     5*fs/16    3*fs/8   7*fs/16   fs/2
                                                                  frequency (Hz), overall mask                                                                                        frequency (Hz), 0–fs/2 mask


Figure 47-7. Interpolator Spectral Mask for 4x OSR
                                                        3rd order SINC filter overall mask for OSR = 4                                                                        3rd order SINC filter 0–fs/2 mask for OSR = 4
                                    0                                                                                                                       0




                                   -24                                                                                                                    -2.4
        gain (dB), overall mask




                                                                                                                                 gain (dB), 0–fs/2 mask

                                   -48                                                                                                                    -4.8




                                   -72                                                                                                                    -7.2




                                   -96                                                                                                                    -9.6




                                  -120                                                                                                                    -12
                                         0   0.25*fs    0.5*fs     0.75*fs    1*fs    1.25*fs    1.5*fs    1.75*fs    2*fs                                       0    fs/16   fs/8     3*fs/16    fs/4     5*fs/16    3*fs/8   7*fs/16   fs/2
                                                                  frequency (Hz), overall mask                                                                                        frequency (Hz), 0–fs/2 mask


Figure 47-8. Interpolator Spectral Mask for 8x OSR
                                                        3rd order SINC filter overall mask for OSR = 8                                                                        3rd order SINC filter 0–fs/2 mask for OSR = 8
                                    0                                                                                                                       0




                                   -24                                                                                                                    -2.4
        gain (dB), overall mask




                                                                                                                                 gain (dB), 0–fs/2 mask




                                   -48                                                                                                                    -4.8




                                   -72                                                                                                                    -7.2




                                   -96                                                                                                                    -9.6




                                  -120                                                                                                                    -12
                                         0    0.5*fs     1*fs       1.5*fs    2*fs     2.5*fs     3*fs      3.5*fs    4*fs                                       0    fs/16   fs/8     3*fs/16    fs/4     5*fs/16    3*fs/8   7*fs/16   fs/2
                                                                  frequency (Hz), overall mask                                                                                        frequency (Hz), 0–fs/2 mask




© 2019 Microchip Technology Inc.                                                                                             Datasheet                                                                         DS60001507E-page 1682
                                                                                                                              SAM D5x/E5x Family Data Sheet
                                                                                                                                                                          DAC – Digital-to-Analog Converter

         Figure 47-9. Interpolator Spectral Mask for 16x OSR
                                                            3rd order SINC filter overall mask for OSR = 16                                                                        3rd order SINC filter 0–fs/2 mask for OSR = 16
                                            0                                                                                                                    0




                                           -24                                                                                                                 -2.4
                gain (dB), overall mask




                                                                                                                                      gain (dB), 0–fs/2 mask
                                           -48                                                                                                                 -4.8




                                           -72                                                                                                                 -7.2




                                           -96                                                                                                                 -9.6




                                          -120                                                                                                                 -12
                                                 0   1*fs    2*fs       3*fs     4*fs       5*fs     6*fs     7*fs     8*fs                                           0    fs/16    fs/8     3*fs/16    fs/4     5*fs/16   3*fs/8   7*fs/16   fs/2
                                                                     frequency (Hz), overall mask                                                                                           frequency (Hz), 0–fs/2 mask


         Figure 47-10. Interpolator Spectral Mask for 32x OSR
                                                            3rd order SINC filter overall mask for OSR = 32                                                                        3rd order SINC filter 0–fs/2 mask for OSR = 32
                                            0                                                                                                                    0




                                           -24                                                                                                                 -2.4
                gain (dB), overall mask




                                                                                                                                      gain (dB), 0–fs/2 mask

                                           -48                                                                                                                 -4.8




                                           -72                                                                                                                 -7.2




                                           -96                                                                                                                 -9.6




                                          -120                                                                                                                 -12
                                                 0   2*fs    4*fs       6*fs     8*fs      10*fs     12*fs    14*fs   16*fs                                           0    fs/16    fs/8     3*fs/16    fs/4     5*fs/16   3*fs/8   7*fs/16   fs/2
                                                                     frequency (Hz), overall mask                                                                                           frequency (Hz), 0–fs/2 mask



47.6.9.7 Dithering-Interpolation Mode
         It is possible to enable both Dithering and Interpolation at the same time by setting DACCTRLx.DITHER
         and DACCTRLx.OSR prior to enabling the DAC. In Dithering-Interpolation mode, the output of dithering is
         sampled at a number of events corresponding to the OSR value. The valid OSR value is 2, 4, 8, or 16.

         Figure 47-11. Dithering-Interpolation Data Path


                                                                                                                                                                                            DACCTRL.FEXT
                                             DAC Controller

                                                                                                                                                                                                                     1                        APB
           16bit                                     DATABUF                16bit                    DITHER                   16bit                                        SINC              12bit
                                                                                                                                                                                                                     0                        DAC
                                                                     data/16-events                                   data/N-events                                                        data/event




        © 2019 Microchip Technology Inc.                                                                                       Datasheet                                                                             DS60001507E-page 1683
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    DAC – Digital-to-Analog Converter


47.7      Register Summary

 Offset        Name        Bit Pos.

 0x00         CTRLA           7:0                                                                                 ENABLE    SWRST
 0x01         CTRLB           7:0                                                                         REFSEL[1:0]         DIFF
 0x02         EVCTRL          7:0     RESRDYEO1 RESRDYEO0     INVEI1       INVEI0    EMPTYEO1      EMPTYEO0      STARTEI1   STARTEI0
 0x03        Reserved
 0x04        INTENCLR         7:0     OVERRUN1   OVERRUN0    RESRDY1      RESRDY0      EMPTY1       EMPTY0      UNDERRUN1 UNDERRUN0
 0x05        INTENSET         7:0     OVERRUN1   OVERRUN0    RESRDY1      RESRDY0      EMPTY1       EMPTY0      UNDERRUN1 UNDERRUN0
 0x06        INTFLAG          7:0     OVERRUN1   OVERRUN0    RESRDY1      RESRDY0      EMPTY1       EMPTY0      UNDERRUN1 UNDERRUN0
 0x07         STATUS          7:0                                                       EOC1         EOC0         READY1    READY0
                              7:0                            DATABUF1    DATABUF0       DATA1        DATA0        ENABLE    SWRST
                             15:8
 0x08       SYNCBUSY
                             23:16
                             31:24
                              7:0      DITHER    RUNSTDBY     FEXT                           CCTRL[1:0]           ENABLE    LEFTADJ
 0x0C        DACCTRL0
                             15:8                 OSR[2:0]                                                REFRESH[3:0]
                              7:0      DITHER    RUNSTDBY     FEXT                           CCTRL[1:0]           ENABLE    LEFTADJ
 0x0E        DACCTRL1
                             15:8                 OSR[2:0]                                                REFRESH[3:0]
                              7:0                                               DATA[7:0]
 0x10          DATA0
                             15:8                                              DATA[15:8]
                              7:0                                               DATA[7:0]
 0x12          DATA1
                             15:8                                              DATA[15:8]
                              7:0                                             DATABUF[7:0]
 0x14        DATABUF0
                             15:8                                            DATABUF[15:8]
                              7:0                                             DATABUF[7:0]
 0x16        DATABUF1
                             15:8                                            DATABUF[15:8]
 0x18        DBGCTRL          7:0                                                                                           DBGRUN
 0x19
   ...       Reserved
 0x1B
                              7:0                                             RESULT[7:0]
 0x1C        RESULT0
                             15:8                                             RESULT[15:8]
                              7:0                                             RESULT[7:0]
 0x1E        RESULT1
                             15:8                                             RESULT[15:8]




47.8      Register Description
          Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
          8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
          accessed directly.
          Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
          write protection is denoted by the "PAC Write-Protection" property in each individual register description.
          For details, refer to 47.5.8 Register Access Protection.




          © 2019 Microchip Technology Inc.                             Datasheet                                DS60001507E-page 1684
                                                 SAM D5x/E5x Family Data Sheet
                                                               DAC – Digital-to-Analog Converter

Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
refer to 47.6.8 Synchronization.
Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1685
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                  DAC – Digital-to-Analog Converter

47.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x00
               Property:    PAC Write-Protection, Write-Synchronized


         Bit         7             6             5              4             3             2             1             0
                                                                                                       ENABLE        SWRST
   Access                                                                                                R/W           R/W
    Reset                                                                                                 0             0


               Bit 1 – ENABLE Enable DAC Controller
               Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
               disabled. The value written to CTRLA.ENABLE will read back immediately and the corresponding bit in
               the Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be
               cleared when the operation is complete.
                Value      Description
                0          The peripheral is disabled.
                1          The peripheral is enabled.

               Bit 0 – SWRST Software Reset
               Writing '0' to this bit has no effect.
               Writing '1' to this bit resets all registers in the DAC to their initial state, and the DAC will be disabled.
               Writing a '1' to CTRLA.SWRST will always take precedence, meaning that all other writes in the same
               write-operation will be discarded.
               Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
               CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
               Value         Description
               0             There is no reset operation ongoing.
               1             The reset operation is ongoing.




           © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 1686
                                                               SAM D5x/E5x Family Data Sheet
                                                                            DAC – Digital-to-Analog Converter

47.8.2         Control B

               Name:       CTRLB
               Offset:     0x01
               Reset:      0x02
               Property:   PAC Write-Protection


         Bit        7             6           5            4            3            2                 1            0
                                                                                         REFSEL[1:0]               DIFF
   Access                                                                           R/W            R/W             R/W
    Reset                                                                            0                 1            0


               Bits 2:1 – REFSEL[1:0] Reference Selection
               This bit field selects the Reference Voltage for both DACs.
                Value        Name        Description
                0x0          VREFAU Unbuffered external voltage reference (not buffered in DAC, direct connection)
                0x1          VDDANA Voltage supply
                0x2          VREFAB Buffered external voltage reference (buffered in DAC)
                0x3          INTREF Internal bandgap reference

               Bit 0 – DIFF Differential Mode Enable
               This bit defines the conversion mode for both DACs.
                Value       Description
                0           Single mode
                1           Differential mode




           © 2019 Microchip Technology Inc.                     Datasheet                              DS60001507E-page 1687
                                                                   SAM D5x/E5x Family Data Sheet
                                                                               DAC – Digital-to-Analog Converter

47.8.3         Event Control

               Name:        EVCTRL
               Offset:      0x02
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7            6             5            4            3            2          1             0
                RESRDYEO1    RESRDYEO0        INVEI1      INVEI0      EMPTYEO1     EMPTYEO0    STARTEI1      STARTEI0
   Access          R/W           R/W           R/W         R/W           R/W          R/W        R/W           R/W
    Reset            0            0             0            0            0            0          0             0


               Bit 7 – RESRDYEO1 Enable Result Ready of Filter 1 output event
               This bit controls whether the RESRDY1 Event is enabled when the interpolated data is ready.
                Value       Description
                0           Interpolated Data Ready Event is disabled
                1           Interpolated Data Ready Event is enabled

               Bit 6 – RESRDYEO0 Enable Result Ready of Filter 0 output event
               This bit controls whether the RESRDY0 Event is enabled when the interpolated data is ready.
                Value       Description
                0           Interpolated Data Ready Event is disabled
                1           Interpolated Data Ready Event is enabled

               Bit 5 – INVEI1 Enable Inversion of DAC1 Start Conversion Input Event
               This bit defines the detection of the input event for DAC1 START.
                Value       Description
                0           Input event source is not inverted.
                1           Input event source is inverted.

               Bit 4 – INVEI0 Enable Inversion of DAC0 Start Conversion Input Event
               This bit defines the detection of the input event for DAC0 START.
                Value       Description
                0           Input event source is not inverted.
                1           Input event source is inverted.

               Bit 3 – EMPTYEO1 Data Buffer Empty Event Output DAC1
               This bit indicates if the Data Buffer Empty Event output for DAC1 is enabled.
                Value       Description
                0            Data Buffer Empty event is disabled.
                1            Data Buffer Empty event is enabled.

               Bit 2 – EMPTYEO0 Data Buffer Empty Event Output DAC0
               This bit indicates if the Data Buffer Empty Event output for DAC0 is enabled.
                Value       Description
                0            Data Buffer Empty event is disabled.
                1            Data Buffer Empty event is enabled.




           © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1688
                                                  SAM D5x/E5x Family Data Sheet
                                                               DAC – Digital-to-Analog Converter

Bit 1 – STARTEI1 Start Conversion Event Input DAC1
This bit indicates if the Start input event for DAC1 is enabled.
 Value       Description
 0            A new conversion will not be triggered on any incoming event.
 1            A new conversion will be triggered on any incoming event.

Bit 0 – STARTEI0 Start Conversion Event Input DAC0
This bit indicates if the Start input event for DAC0 is enabled.
 Value       Description
 0            A new conversion will not be triggered on any incoming event.
 1            A new conversion will be triggered on any incoming event.




© 2019 Microchip Technology Inc.                   Datasheet                   DS60001507E-page 1689
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                  DAC – Digital-to-Analog Converter

47.8.4         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x04
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set register (INTENSET).

         Bit         7             6             5              4             3             2             1             0
                OVERRUN1      OVERRUN0        RESRDY1       RESRDY0       EMPTY1         EMPTY0      UNDERRUN1     UNDERRUN0
   Access           R/W           R/W           R/W           R/W           R/W            R/W           R/W           R/W
    Reset            0             0             0              0             0             0             0             0


               Bit 7 – OVERRUN1 Overrun Interrupt Enable for Filter Channel 1
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Overrun Interrupt Enable for Filter Channel 1 bit, which disables the
               Filter 1 Overrun interrupt.
                Value        Description
                0            Filter 1 Result Ready interrupt is disabled.
                1            Filter 1 Result Ready interrupt is enabled.

               Bit 6 – OVERRUN0 Overrun Interrupt Enable for Filter Channel 0
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Overrun Interrupt Enable for Filter Channel 0 bit, which disables the
               Filter 0 Overrun interrupt.
                Value        Description
                0            Filter 0 Result Ready interrupt is disabled.
                1            Filter 0 Result Ready interrupt is enabled.

               Bit 5 – RESRDY1 Filter Channel 1 Result Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Filter Channel 1 Result Ready Interrupt Enable bit, which disables the
               Filter Channel 1 Result Ready interrupt.
                Value        Description
                0            Filter 1 Result Ready interrupt is disabled.
                1            Filter 1 Result Ready interrupt is enabled.

               Bit 4 – RESRDY0 Filter Channel 0 Result Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Filter Channel 0 Result Ready Interrupt Enable bit, which disables the
               Filter Channel 0 Result Ready interrupt.
                Value        Description
                0            Filter 0 Result Ready interrupt is disabled.
                1            Filter 0 Result Ready interrupt is enabled.

               Bit 3 – EMPTY1 Data Buffer 1 Empty Interrupt Enable
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 1690
                                                    SAM D5x/E5x Family Data Sheet
                                                                 DAC – Digital-to-Analog Converter

Writing a '1' to this bit will clear the Data Buffer 1 Empty Interrupt Enable bit, which disables the Data
Buffer 1 Empty interrupt.
Value         Description
0             The Data Buffer 1 Empty interrupt is disabled.
1             The Data Buffer 1 Empty interrupt is enabled.

Bit 2 – EMPTY0 Data Buffer 0 Empty Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Data Buffer 0 Empty Interrupt Enable bit, which disables the Data
Buffer 0 Empty interrupt.
Value         Description
0             The Data Buffer 0 Empty interrupt is disabled.
1             The Data Buffer 0 Empty interrupt is enabled.

Bit 1 – UNDERRUN1 Underrun Interrupt Enable for DAC1
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Data Buffer 1 Underrun Interrupt Enable bit, which disables the Data
Buffer 1 Underrun interrupt.
Value         Description
0             The Data Buffer 1 Underrun interrupt is disabled.
1             The Data Buffer 1 Underrun interrupt is enabled.

Bit 0 – UNDERRUN0 Underrun Interrupt Enable for DAC0
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the Data Buffer 0 Underrun Interrupt Enable bit, which disables the Data
Buffer 0 Underrun interrupt.
Value         Description
0             The Data Buffer 0 Underrun interrupt is disabled.
1             The Data Buffer 0 Underrun interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1691
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                  DAC – Digital-to-Analog Converter

47.8.5         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x05
               Reset:       0x00
               Property:    PAC Write-Protection

               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear register (INTENCLR).

         Bit         7             6             5             4             3              2             1             0
                OVERRUN1      OVERRUN0        RESRDY1      RESRDY0        EMPTY1        EMPTY0      UNDERRUN1     UNDERRUN0
   Access           R/W           R/W           R/W           R/W           R/W           R/W           R/W           R/W
    Reset            0             0             0             0             0              0             0             0


               Bit 7 – OVERRUN1 Overrun Interrupt Enable for Filter Channel 1
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Overrun Interrupt Enable for Filter Channel 1 bit, which enables the
               Filter 1 Overrun interrupt.
                Value        Description
                0            Filter 1 Result Ready interrupt is disabled.
                1            Filter 1 Result Ready interrupt is enabled.

               Bit 6 – OVERRUN0 Overrun Interrupt Enable for Filter Channel 0
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Overrun Interrupt Enable for Filter Channel 0 bit, which enables the
               Filter 0 Overrun interrupt.
                Value        Description
                0            Filter 0 Result Ready interrupt is disabled.
                1            Filter 0 Result Ready interrupt is enabled.

               Bit 5 – RESRDY1 Filter Channel 1 Result Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Filter Channel 1 Result Ready Interrupt Enable bit, which enables the
               Filter Channel 1 Result Ready interrupt.
                Value        Description
                0            Filter 1 Result Ready interrupt is disabled.
                1            Filter 1 Result Ready interrupt is enabled.

               Bit 4 – RESRDY0 Filter Channel 0 Result Ready Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will set the Filter Channel 0 Result Ready Interrupt Enable bit, which enables the
               Filter Channel 0 Result Ready interrupt.
                Value        Description
                0            Filter 0 Result Ready interrupt is disabled.
                1            Filter 0 Result Ready interrupt is enabled.

               Bit 3 – EMPTY1 Data Buffer 1 Empty Interrupt Enable
               Writing a '0' to this bit has no effect.




           © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 1692
                                                   SAM D5x/E5x Family Data Sheet
                                                                 DAC – Digital-to-Analog Converter

Writing a '1' to this bit will set the Data Buffer 1 Empty Interrupt Enable bit, which enables the Data Buffer
1 Empty interrupt.
 Value        Description
 0            The Data Buffer 1 Empty interrupt is disabled.
 1            The Data Buffer 1 Empty interrupt is enabled.

Bit 2 – EMPTY0 Data Buffer 0 Empty Interrupt Enable
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Data Buffer 0 Empty Interrupt Enable bit, which enables the Data Buffer
0 Empty interrupt.
 Value        Description
 0            The Data Buffer 0 Empty interrupt is disabled.
 1            The Data Buffer 0 Empty interrupt is enabled.

Bit 1 – UNDERRUN1 Underrun Interrupt Enable for DAC1
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Data Buffer 1 Underrun Interrupt Enable bit, which enables the Data
Buffer 1 Underrun interrupt.
Value         Description
0             The Data Buffer 1 Underrun interrupt is disabled.
1             The Data Buffer 1 Underrun interrupt is enabled.

Bit 0 – UNDERRUN0 Underrun Interrupt Enable for DAC0
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will set the Data Buffer 0 Underrun Interrupt Enable bit, which enables the Data
Buffer 0 Underrun interrupt.
Value         Description
0             The Data Buffer 0 Underrun interrupt is disabled.
1             The Data Buffer 0 Underrun interrupt is enabled.




© 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1693
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                DAC – Digital-to-Analog Converter

47.8.6         Interrupt Flag Status and Clear

               Name:        INTFLAG
               Offset:      0x06
               Reset:       0x00
               Property:    -


         Bit         7            6              5            4            3             2            1             0
                OVERRUN1      OVERRUN0        RESRDY1     RESRDY0       EMPTY1       EMPTY0      UNDERRUN1     UNDERRUN0
   Access          R/W           R/W            R/W         R/W           R/W          R/W           R/W           R/W
    Reset            0            0              0            0            0             0            0             0


               Bit 7 – OVERRUN1 Overrun for Filter Channel 1
               This flag is set when the DMA is not cleared while the RESULT1 register gets new data.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Overrun for Filter Channel 0 flag.
                Value        Description
                0            Filter 1 Result Ready interrupt is disabled.
                1            Filter 1 Result Ready interrupt is enabled.

               Bit 6 – OVERRUN0 Overrun for Filter Channel 0
               This flag is set when the DMA is not cleared while the RESULT0 register gets new data.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Overrun for Filter Channel 0 flag.

               Bit 5 – RESRDY1 Filter Channel 1 Result Ready
               This flag is set when the filter is used as standalone (DACCTRL1.FEXT=1) and the filter output is ready.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Filter Channel 1 Result Ready flag.

               Bit 4 – RESRDY0 Filter Channel 0 Result Ready
               This flag is set when the filter is used as standalone (DACCTRL0.FEXT=1) and the filter output is ready.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Filter Channel 0 Result Ready flag.

               Bit 3 – EMPTY1 Data Buffer 1 Empty
               This flag is cleared by writing a '1' to it or by writing new data to DATA1 or DATABUF1.
               This flag is set when the data buffer for DAC1 is empty and will generate an interrupt request if
               INTENCLR/INTENSET.EMPTY1=1.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Data Buffer 1 Empty interrupt flag.

               Bit 2 – EMPTY0 Data Buffer 0 Empty
               This flag is cleared by writing a '1' to it or by writing new data to DATA0 or DATABUF0.
               This flag is set when the data buffer for DAC0 is empty and will generate an interrupt request if
               INTENCLR/INTENSET.EMPTY0=1.
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Data Buffer 0 Empty interrupt flag.




           © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1694
                                                 SAM D5x/E5x Family Data Sheet
                                                              DAC – Digital-to-Analog Converter

Bit 1 – UNDERRUN1 DAC1 Underrun
This flag is cleared by writing a '1' to it.
This flag is set when a start conversion event (START1) occurred before new data is copied/written to the
DAC1 data buffer and will generate an interrupt request if INTENCLR/INTENSET.UNDERRUN1=1.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the DAC1 Underrun interrupt flag.

Bit 0 – UNDERRUN0 DAC0 Underrun
This flag is cleared by writing a '1' to it.
This flag is set when a start conversion event (START0) occurred before new data is copied/written to the
DAC) data buffer and will generate an interrupt request if INTENCLR/INTENSET.UNDERRUN0=1.
Writing a '0' to this bit has no effect.
Writing a '1' to this bit will clear the DAC0 Underrun interrupt flag.




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1695
                                                                SAM D5x/E5x Family Data Sheet
                                                                              DAC – Digital-to-Analog Converter

47.8.7         Status

               Name:       STATUS
               Offset:     0x07
               Reset:      0x00
               Property:   -


         Bit         7            6            5            4            3           2         1            0
                                                                       EOC1         EOC0     READY1      READY0
   Access                                                                R           R         R            R
    Reset                                                                0           0         0            0


               Bit 3 – EOC1 DAC1 End of Conversion
               This bit is cleared when DATA1 register is written.
                Value        Description
                0            No conversion completed since last load of DATA1.
                1            DAC1 conversion is complete, VOUT1 is stable.

               Bit 2 – EOC0 DAC0 End of Conversion
               This bit is cleared when DATA0 register is written.
                Value        Description
                0            No conversion completed since last load of DATA0.
                1            DAC0 conversion is complete, VOUT0 is stable.

               Bit 1 – READY1 DAC1 Startup Ready
               Value      Description
               0          DAC1 is not ready for conversion.
               1          Startup time has elapsed, DAC1 is ready for conversion.

               Bit 0 – READY0 DAC0 Startup Ready
               Value      Description
               0          DAC0 is not ready for conversion.
               1          Startup time has elapsed, DAC0 is ready for conversion.




           © 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1696
                                                                 SAM D5x/E5x Family Data Sheet
                                                                                DAC – Digital-to-Analog Converter

47.8.8         Synchronization Busy

               Name:       SYNCBUSY
               Offset:     0x08
               Reset:      0x00000000
               Property:   -


         Bit        31           30              29         28            27           26        25           24


   Access
    Reset


         Bit        23           22              21         20            19           18        17           16


   Access
    Reset


         Bit        15           14              13         12            11           10        9            8


   Access
    Reset


         Bit        7             6              5          4             3            2         1            0
                                              DATABUF1   DATABUF0       DATA1        DATA0     ENABLE       SWRST
   Access                                        R          R             R            R         R            R
    Reset                                        0          0             0            0         0            0


               Bit 5 – DATABUF1 Data Buffer DAC1
               This bit is set when DATABUF1 register is written.
               This bit is cleared when DATABUF1 synchronization is completed.
                Value        Description
                0            No ongoing synchronized access.
                1            Synchronized access is ongoing.

               Bit 4 – DATABUF0 Data Buffer DAC0
               This bit is set when DATABUF0 register is written.
               This bit is cleared when DATABUF0 synchronization is completed.
                Value        Description
                0            No ongoing synchronized access.
                1            Synchronized access is ongoing.

               Bit 3 – DATA1 Data DAC1
               This bit is set when DATA1 register is written.
               This bit is cleared when DATA1 synchronization is completed.
                Value        Description
                0            No ongoing synchronized access.
                1            Synchronized access is ongoing.




           © 2019 Microchip Technology Inc.                         Datasheet                    DS60001507E-page 1697
                                                SAM D5x/E5x Family Data Sheet
                                                               DAC – Digital-to-Analog Converter

Bit 2 – DATA0 Data DAC0
This bit is set when DATA0 register is written.
This bit is cleared when DATA0 synchronization is completed.
 Value        Description
 0            No ongoing synchronized access.
 1            Synchronized access is ongoing.

Bit 1 – ENABLE DAC Enable Status
This bit is set when CTRLA.ENABLE bit is written.
This bit is cleared when CTRLA.ENABLE synchronization is completed.
 Value        Description
 0            No ongoing synchronization.
 1            Synchronization is ongoing.

Bit 0 – SWRST Software Reset
This bit is set when CTRLA.SWRST bit is written.
This bit is cleared when CTRLA.SWRST synchronization is completed.
 Value        Description
 0            No ongoing synchronization.
 1            Synchronization is ongoing.




© 2019 Microchip Technology Inc.                 Datasheet                     DS60001507E-page 1698
                                                                      SAM D5x/E5x Family Data Sheet
                                                                                  DAC – Digital-to-Analog Converter

47.8.9         DAC0 Control

               Name:        DACCTRL0
               Offset:      0x0C
               Reset:       0x0000
               Property:    PAC Write-Protection, Enabled-Protected


         Bit        15            14            13            12            11                10                  9        8
                               OSR[2:0]                                                            REFRESH[3:0]
   Access           R/W           R/W           R/W                        R/W                R/W            R/W          R/W
    Reset            0             0             0                          0                  0                  0        0


         Bit         7             6             5                4         3                  2                  1        0
                  DITHER      RUNSTDBY         FEXT                              CCTRL[1:0]                ENABLE       LEFTADJ
   Access           R/W           R/W           R/W                        R/W                R/W            R/W          R/W
    Reset            0             0             0                          0                  0                  0        0


               Bits 15:13 – OSR[2:0] Oversampling Ratio
               This field defines the oversampling ratio/interpolation depth.
                Value       Name                      Description
                0x0         OSR_1                     1x OSR (no interpolation)
                0x1         OSR_2                     2x OSR
                0x2         OSR_4                     4x OSR
                0x3         OSR_8                     8x OSR
                0x4         OSR_16                    16x OSR
                0x5         OSR_32                    32x OSR
                other       -                         Reserved

               Bits 11:8 – REFRESH[3:0] Refresh period
               This field defines the refresh period. If REFRESH=0x0, the refresh mode is disabled. If REFRESH>0x1,
               else the refresh period is:
               �REFRESH = REFRESH × 30μs

               Bit 7 – DITHER Dithering Mode
               Value       Description
               0           Dithering mode is disabled.
               1           Dithering mode is enabled.

               Bit 6 – RUNSTDBY Run in Standby
               This bit controls the behavior of DAC0 during standby sleep mode.
                Value       Description
                0           DAC0 is disabled during standby sleep mode.
                1           DAC0 continues to operate during standby sleep mode.

               Bit 5 – FEXT External Filter Enable
               This bit controls the usage of the filter.
                Value       Description
                0           The filter is integrated to the DAC




           © 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 1699
                                                   SAM D5x/E5x Family Data Sheet
                                                                 DAC – Digital-to-Analog Converter

 Value        Description
 1            The filter is used as standalone

Bits 3:2 – CCTRL[1:0] Current Control
This field defines the current in output buffer according to conversion rate.
Current Control
 Value       Name                Description
 0x0         CC100K              GCLK_DAC ≤ 1.2MHz (100kSPS)
 0x1         CC1M                1.2MHz < GCLK_DAC ≤ 6MHz (500kSPS)
 0x2         CC12M               6MHz < GCLK_DAC ≤ 12MHz (1MSPS)
 0x3         Reserved

Bit 1 – ENABLE Enable DAC0
This bit enables DAC0 when DAC Controller is enabled (CTRLA.ENABLE).
 Value      Description
 0          DAC0 is disabled.
 1          DAC0 is enabled.

Bit 0 – LEFTADJ Left Adjusted Data
This bit controls how the 12-bit conversion data is adjusted in the Data and Data Buffer registers.
 Value       Description
 0           DATA0 and DATABUF0 registers are right-adjusted.
 1           DATA0 and DATABUF0 registers are left-adjusted.




© 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1700
                                                                  SAM D5x/E5x Family Data Sheet
                                                                              DAC – Digital-to-Analog Converter

47.8.10 DAC1 Control

           Name:        DACCTRL1
           Offset:      0x0E
           Reset:       0x0000
           Property:    PAC Write-Protection, Enabled-Protected


     Bit        15            14            13            12            11                10                  9        8
                           OSR[2:0]                                                            REFRESH[3:0]
  Access        R/W           R/W           R/W                        R/W                R/W            R/W          R/W
   Reset         0             0             0                          0                  0                  0        0


     Bit         7             6             5                4         3                  2                  1        0
              DITHER      RUNSTDBY         FEXT                              CCTRL[1:0]                ENABLE       LEFTADJ
  Access        R/W           R/W           R/W                        R/W                R/W            R/W          R/W
   Reset         0             0             0                          0                  0                  0        0


           Bits 15:13 – OSR[2:0] Oversampling Ratio
           This field defines the oversampling ratio/interpolation depth.
            Value       Name                      Description
            0x0         OSR_1                     1x OSR (no interpolation)
            0x1         OSR_2                     2x OSR
            0x2         OSR_4                     4x OSR
            0x3         OSR_8                     8x OSR
            0x4         OSR_16                    16x OSR
            0x5         OSR_32                    32x OSR
            other       -                         Reserved

           Bits 11:8 – REFRESH[3:0] Refresh period
           This field defines the refresh period. If REFRESH=0x0, the refresh mode is disabled. If REFRESH>0x1,
           else the refresh period is:
           �REFRESH = REFRESH × 30μs

           Bit 7 – DITHER Dithering Mode
           Value       Description
           0           Dithering mode is disabled.
           1           Dithering mode is enabled.

           Bit 6 – RUNSTDBY Run in Standby
           This bit controls the behavior of DAC1 during standby sleep mode.
            Value       Description
            0           DAC1 is disabled during standby sleep mode.
            1           DAC1 continues to operate during standby sleep mode.

           Bit 5 – FEXT External Filter Enable
           This bit controls the usage of the filter.
            Value       Description
            0           The filter is integrated to the DAC




       © 2019 Microchip Technology Inc.                           Datasheet                               DS60001507E-page 1701
                                                  SAM D5x/E5x Family Data Sheet
                                                                DAC – Digital-to-Analog Converter

 Value        Description
 1            The filter is used as standalone

Bits 3:2 – CCTRL[1:0] Current Control
This field defines the current in output buffer.
Current Control
 Value       Name              Description
 0x0         CC100K            GCLK_DAC <= 1.2MHz (100kSPS)
 0x1         CC1M              1.2MHz < GCLK_DAC <= 6MHz (500kSPS)
 0x2         CC12M             6MHz < GCLK_DAC <= 12MHz (1MSPS)
 0x3                           Reserved

Bit 1 – ENABLE Enable DAC1
This bit enables DAC1 when DAC Controller is enabled (CTRLA.ENABLE).
 Value      Description
 0          DAC1 is disabled.
 1          DAC1 is enabled.

Bit 0 – LEFTADJ Left Adjusted Data
This bit controls how the 12-bit conversion data is adjusted in the Data and Data Buffer registers.
 Value       Description
 0           DATA1 and DATABUF1 registers are right-adjusted.
 1           DATA1 and DATABUF1 registers are left-adjusted.




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1702
                                                             SAM D5x/E5x Family Data Sheet
                                                                              DAC – Digital-to-Analog Converter

47.8.11 Data DAC0

           Name:       DATA0
           Offset:     0x10
           Reset:      0x0000
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        15           14           13           12                11          10        9             8
                                                            DATA[15:8]
  Access        W            W            W             W                W           W         W            W
   Reset         0            0            0            0                0           0         0             0


     Bit         7            6            5            4                3           2         1             0
                                                            DATA[7:0]
  Access        W            W            W             W                W           W         W            W
   Reset         0            0            0            0                0           0         0             0


           Bits 15:0 – DATA[15:0] DAC0 Data
           DATA0 register contains the 12-bit value that is converted to a voltage by the DAC0. The adjustment of
           these 12 bits within the 16-bit register is controlled by DACCTRL0.LEFTADJ:
           - DATA[11:0] when DACCTRL0.LEFTADJ=0.
           - DATA[15:4] when DACCTRL0.LEFTADJ=1.
           In dithering mode (whatever DACCTRL0.LEFTADJ value):
           - DATA[15:4] are the 12-bit converted by DAC0.
           - DATA[3:0] are the dither bits.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1703
                                                             SAM D5x/E5x Family Data Sheet
                                                                              DAC – Digital-to-Analog Converter

47.8.12 Data DAC1

           Name:       DATA1
           Offset:     0x12
           Reset:      0x0000
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        15           14           13           12                11          10        9             8
                                                            DATA[15:8]
  Access        W            W            W             W                W           W         W            W
   Reset         0            0            0            0                0           0         0             0


     Bit         7            6            5            4                3           2         1             0
                                                            DATA[7:0]
  Access        W            W            W             W                W           W         W            W
   Reset         0            0            0            0                0           0         0             0


           Bits 15:0 – DATA[15:0] DAC1 Data
           DATA1 register contains the 12-bit value that is converted to a voltage by the DAC1. The adjustment of
           these 12 bits within the 16-bit register is controlled by DACCTRL1.LEFTADJ:
           - DATA[11:0] when DACCTRL1.LEFTADJ=0.
           - DATA[15:4] when DACCTRL1.LEFTADJ=1.
           In dithering mode (whatever DACCTRL1.LEFTADJ value):
           - DATA[15:4] are the 12-bit converted by DAC1.
           - DATA[3:0] are the dither bits.




       © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1704
                                                           SAM D5x/E5x Family Data Sheet
                                                                            DAC – Digital-to-Analog Converter

47.8.13 Data Buffer DAC0

           Name:       DATABUF0
           Offset:     0x14
           Reset:      0x0000
           Property:   Write-Synchronized


     Bit        15           14           13        12              11             10        9           8
                                                      DATABUF[15:8]
  Access        W            W            W          W              W              W         W           W
   Reset        0             0             0        0                  0          0         0           0


     Bit        7             6             5        4                  3          2         1           0
                                                         DATABUF[7:0]
  Access        W            W            W          W              W              W         W           W
   Reset        0             0             0        0                  0          0         0           0


           Bits 15:0 – DATABUF[15:0] DAC0 Data Buffer
           DATABUF0 contains the value to be transferred into DATA0 when a START0 event occurs.




       © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1705
                                                           SAM D5x/E5x Family Data Sheet
                                                                            DAC – Digital-to-Analog Converter

47.8.14 Data Buffer DAC1

           Name:       DATABUF1
           Offset:     0x16
           Reset:      0x0000
           Property:   Write-Synchronized


     Bit        15           14           13        12              11             10        9           8
                                                      DATABUF[15:8]
  Access        W            W            W          W              W              W         W           W
   Reset        0             0             0        0                  0          0         0           0


     Bit        7             6             5        4                  3          2         1           0
                                                         DATABUF[7:0]
  Access        W            W            W          W              W              W         W           W
   Reset        0             0             0        0                  0          0         0           0


           Bits 15:0 – DATABUF[15:0] DAC1 Data Buffer
           DATABUF1 contains the value to be transferred into DATA1 when a START1 event occurs.




       © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1706
                                                           SAM D5x/E5x Family Data Sheet
                                                                        DAC – Digital-to-Analog Converter

47.8.15 Debug Control

           Name:       DBGCTRL
           Offset:     0x18
           Reset:      0x00
           Property:   PAC Write-Protection


     Bit        7             6           5            4           3            2            1           0
                                                                                                      DBGRUN
  Access
   Reset                                                                                                 0


           Bit 0 – DBGRUN Debug Run
           This bit is not reset by a software reset.
           This bits controls the functionality when the CPU is halted by an external debugger.
            Value       Description
            0           The DAC is halted when the CPU is halted by an external debugger. Any ongoing conversion
                        will complete.
            1           The DAC continues normal operation when the CPU is halted by an external debugger.




       © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 1707
                                                             SAM D5x/E5x Family Data Sheet
                                                                               DAC – Digital-to-Analog Converter

47.8.16 Result 0

            Name:       RESULT0
            Offset:     0x1C
            Reset:      0x0000
            Property:   Read-Synchronized


      Bit        15           14           13          12                 11          10        9           8
                                                           RESULT[15:8]
  Access         R             R           R           R                  R           R         R           R
   Reset         0             0           0           0                  0           0         0           0


      Bit        7             6           5           4                  3           2         1           0
                                                            RESULT[7:0]
  Access         R             R           R           R                  R           R         R           R
   Reset         0             0           0           0                  0           0         0           0


            Bits 15:0 – RESULT[15:0] Channel 0 Filter Output
            RESULT[15:0] contains the value of the interpolated data written to DATA0 or DATABUF0 in standalone
            mode (DACCTRL0.FEXT=1).




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1708
                                                             SAM D5x/E5x Family Data Sheet
                                                                               DAC – Digital-to-Analog Converter

47.8.17 Result 1

            Name:       RESULT1
            Offset:     0x1E
            Reset:      0x0000
            Property:   Read-Synchronized


      Bit        15           14           13          12                 11          10        9           8
                                                           RESULT[15:8]
  Access         R             R           R           R                  R           R         R           R
   Reset         0             0           0           0                  0           0         0           0


      Bit        7             6           5           4                  3           2         1           0
                                                            RESULT[7:0]
  Access         R             R           R           R                  R           R         R           R
   Reset         0             0           0           0                  0           0         0           0


            Bits 15:0 – RESULT[15:0] Channel 0 Filter Output
            RESULT[15:0] contains the value of the interpolated data written to DATA1 or DATABUF1 in standalone
            mode (DACCTRL1.FEXT=1).




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1709
