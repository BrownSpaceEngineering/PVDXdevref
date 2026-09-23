# 45. ADC – Analog-to-Digital Converter

*Source: `Atmel-SAMD51.pdf`, pages 1585-1639 — SAMD51 family datasheet*

                                                           SAM D5x/E5x Family Data Sheet
                                                                        ADC – Analog-to-Digital Converter


45.    ADC – Analog-to-Digital Converter

45.1   Overview
       The Analog-to-Digital Converter (ADC) converts analog signals to digital values. The ADC has up to 12-
       bit resolution, and is capable of a sampling rate of up to 1MSPS. The input selection is flexible, and both
       differential and single-ended measurements can be performed. In addition, several internal signal inputs
       are available. The ADC can provide both signed and unsigned results.
       ADC measurements can be started by either application software or an incoming event from another
       peripheral in the device. ADC measurements can be started with predictable timing, and without software
       intervention.
       Both internal and external reference voltages can be used.
       An integrated temperature sensor is available for use with the ADC. The bandgap voltage, as well as the
       scaled I/O and core voltages, can also be measured by the ADC.
       The ADC has a compare function for accurate monitoring of user-defined thresholds, with minimum
       software intervention required.
       The ADC can be configured for 8-, 10- or 12-bit results. ADC conversion results are provided left- or right-
       adjusted, which eases calculation when the result is represented as a signed value. It is possible to use
       DMA to move ADC results directly to memory or peripherals when conversions are done.
       The SAM D5x/E5x has two ADC instances, ADC0 and ADC1. The two inputs can be sampled
       simultaneously, as each ADC includes sample and hold circuits.
       Note: When the Peripheral Touch Controller (PTC) is enabled, ADC0 is serving the PTC exclusively. In
       this case, ADC0 cannot be used by the user application.



45.2   Features
         •   Two Analog to Digital Converters (ADC) ADC0 and ADC1
         •   8-, 10- or 12-bit resolution
         •   Up to 1,000,000 samples per second (1MSPS)
         •   Differential and single-ended inputs
               – Up to 32 analog inputs per ADC (20 unique channels total)
                  32 positive and 10 negative, including internal and external
         •   Internal inputs:
               – Internal temperature sensor
               – Bandgap voltage
               – Scaled core supply
               – Scaled I/O supply
               – Scaled VBAT supply
               – DAC
         •   Single, continuous and sequencing options
         •   Windowing monitor with selectable channel
         •   Conversion range: Vref = [1.0V to VDDANA ]




       © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1585
                                                              SAM D5x/E5x Family Data Sheet
                                                                             ADC – Analog-to-Digital Converter

         •   Built-in internal reference and external reference options
         •   Event-triggered conversion for accurate timing (one event input)
         •   Optional DMA transfer of conversion settings or result
         •   Hardware gain and offset compensation
         •   Averaging and oversampling with decimation to support up to 16-bit result
         •   Selectable sampling time
         •   Flexible Power / Throughput rate management
       ADC0 can be configured to serve the Peripheral Touch Controller (PTC). Refer to the PTC chapter for
       details.



45.3   Block Diagram
       Figure 45-1. ADC Block Diagram
                                                           CTRLB                       DSEQCTRL


                                                          AVGCTRL                       WINLT


                                                          SAMPCTRL                      WINUT
                   INPUTCTRL
                                                           EVCTRL                    OFFSETCORR


                                                           SWTRIG                     GAINCORR


         ADC0
          ...
         ADCn
       INT.SIG

                                                          ADC                          POST
                                                                                     PROCESSING
                                                                                                            RESULT

         ADC0
          ...
         ADCn


                             INT1V
                           INTVCC0                                   CTRLA            DSEQSTAT
                           INTVCC1
                            VREFA
                             ...
                            VREFn
                                                                PRESCALER


                                          REFCTRL




45.4   Signal Description
        Signal                             Description                Type
        VREF[A, B, C]                      Analog input               External reference voltage
        AIN[31..0]                         Analog input               Analog input channels




       © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1586
                                                            SAM D5x/E5x Family Data Sheet
                                                                          ADC – Analog-to-Digital Converter

         Note: One signal can be mapped on several pins.
         Related Links
         6. I/O Multiplexing and Considerations



45.5     Product Dependencies
         In order to use this peripheral, other parts of the system must be configured correctly, as described below.

45.5.1   I/O Lines
         Using the ADC's I/O lines requires the I/O pins to be configured using the port configuration (PORT).

         Related Links
         32. PORT - I/O Pin Controller

45.5.2   Power Management
         The ADC will continue to operate in any Sleep mode where the selected source clock is running. The
         ADC’s interrupts, except the OVERRUN interrupt, can be used to wake up the device from Sleep modes,
         except the OVERRUN interrupt. Events connected to the event system can trigger other operations in the
         system without exiting Sleep modes.
         Related Links
         18. PM – Power Manager

45.5.3   Clocks
         The ADC bus clocks (CLK_APB_ADCx) can be enabled in the Main Clock, which also defines the default
         state.
         Each ADC requires a generic clock (GCLK_ADCx). This clock must be configured and enabled in the
         Generic Clock Controller (GCLK) before using the ADC.
         A generic clock is asynchronous to the bus clock. Due to this asynchronicity, writes to certain registers will
         require synchronization between the clock domains. Refer to Synchronization for further details.
         Related Links
         15.6.2.6 Peripheral Clock Masking
         14. GCLK - Generic Clock Controller

45.5.4   DMA
         The DMA request line is connected to the DMA Controller (DMAC). Using the ADC DMA requests
         requires the DMA Controller to be configured first.
         Related Links
         22. DMAC – Direct Memory Access Controller

45.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the ADC interrupt requires the
         interrupt controller to be configured first.
         Related Links
         10.2 Nested Vector Interrupt Controller




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1587
                                                             SAM D5x/E5x Family Data Sheet
                                                                           ADC – Analog-to-Digital Converter

45.5.6    Events
          The events are connected to the Event System.
          Related Links
          31. EVSYS – Event System

45.5.7    Debug Operation
          When the CPU is halted in debug mode the ADC will halt normal operation. The ADC can be forced to
          continue operation during debugging. Refer to DBGCTRL register for details.
          Related Links
          45.8.3 DBGCTRL

45.5.8    Register Access Protection
          All registers with write-access are optionally write-protected by the Peripheral Access Controller (PAC),
          except the following register:
           • Interrupt Flag Status and Clear (INTFLAG) register
          Optional write protection by the Peripheral Access Controller (PAC) is denoted by the "PAC Write
          Protection" property in each individual register description.
          PAC write protection does not apply to accesses through an external debugger.
          Related Links
          27. PAC - Peripheral Access Controller

45.5.9    Analog Connections
          I/O-pins (AINx), as well as the VREFA/VREFB/VREFC reference voltage pins are analog inputs to the
          ADC. Any internal reference source, such as a bandgap voltage reference, or DAC must be configured
          and enabled prior to its use with the ADC.


45.5.10 Calibration
        The BIASREFBUF, BIASR2R and BIASCOMP calibration values from the production test must be loaded
        from the NVM Software Calibration Area into the ADC Calibration register (CALIB) by software to achieve
        specified accuracy.



45.6      Functional Description

45.6.1    Principle of Operation
          By default, the ADC provides results with 12-bit resolution. 8-bit or 10-bit results can be selected in order
          to reduce the conversion time, see 45.6.2.8 Conversion Timing and Sampling Rate.
          The ADC has an oversampling with decimation option that can extend the resolution to 16 bits. The input
          values can be either internal (e.g., an internal temperature sensor) or external (connected I/O pins). The
          user can also configure whether the conversion should be single-ended or differential.

45.6.2    Basic Operation

45.6.2.1 Initialization
          The following registers are enable-protected, meaning that they can only be written when the ADC is
          disabled (CTRLA.ENABLE=0):




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1588
                                                           SAM D5x/E5x Family Data Sheet
                                                                         ADC – Analog-to-Digital Converter

          • Control A (CTRLA), except ENABLE and SWRST bits
          • Event Control register (EVCTRL)
          • Calibration register (CALIB)
         Enable-protection is denoted by the "Enable-Protected" property in the register description.
45.6.2.2 Enabling, Disabling, and Resetting
         The ADC is enabled by writing a '1' to the Enable bit in the Control A register (CTRLA.ENABLE). The
         ADC is disabled by writing CTRLA.ENABLE=0.
         The ADC is reset by writing a '1' to the Software Reset bit in the Control A register (CTRLA.SWRST). All
         registers in the ADC, except DBGCTRL, will be reset to their initial state, and the ADC will be disabled.
         Refer to 45.8.1 CTRLA for details.
45.6.2.3 Operation
         In the most basic configuration, the ADC samples values from the configured internal or external sources
         (INPUTCTRL register). The rate of the conversion depends on the combination of the GCLK_ADCx
         frequency and the clock prescaler.
         To convert analog values to digital values, the ADC needs to be initialized first, as described in the
         Initialization section. Data conversion can be started either manually by setting the Start bit in the
         Software Trigger register (SWTRIG.START=1), or automatically by configuring an automatic trigger to
         initiate the conversions. The ADC starts sampling the input only after the start of conversion is triggered.
         This means that even after the MUX selection is made, sample and hold (S&H) operation starts only on
         the conversion trigger. A free-running mode can be used to continuously convert an input channel. When
         using free-running mode the first conversion must be started, while subsequent conversions will start
         automatically at the end of previous conversions.
         The ADC starts sampling the input only after the start of a conversion is triggered. This means that even
         after the MUX selection is made, sample and hold operation starts only on the conversion trigger.
         The result of the conversion is stored in the Result register (RESULT) overwriting the result from the
         previous conversion.
         To avoid data loss, if more than one channel is enabled, the conversion result must be read as soon as it
         is available (INTFLAG.RESRDY). Failing to do so will result in an overrun error condition, indicated by the
         OVERRUN bit in the Interrupt Flag Status and Clear register (INTFLAG.OVERRUN).
         To enable one of the available interrupts sources, the corresponding bit in the Interrupt Enable Set
         register (INTENSET) must be written to '1'.
         Related Links
         45.6.2.1 Initialization

45.6.2.4 Prescaler Selection
         The ADC is clocked by GCLK_ADCx. There is also a prescaler in the ADC to enable conversion at lower
         clock rates. Refer to CTRLA for details on prescaler settings. Refer to 45.6.2.8 Conversion Timing and
         Sampling Rate for details on timing and sampling rate.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1589
                                                            SAM D5x/E5x Family Data Sheet
                                                                                  ADC – Analog-to-Digital Converter

         Figure 45-2. ADC Prescaler


                                           GCLK_ADCx                         9-BIT PRESCALER




                                                                                                           DIV128

                                                                                                                    DIV256
                                                                                   DIV16

                                                                                           DIV32

                                                                                                   DIV64
                                                           DIV2

                                                                    DIV4

                                                                           DIV8
                          CTRLA.PRESCALER[2:0]




                                                                                    CLK_ADCx
         Note: The minimum prescaling factor is DIV2.

45.6.2.5 Reference Configuration
         The ADC has various sources for its reference voltage VREF. The Reference Voltage Selection bit field in
         the Reference Control register (REFCTRL.REFSEL) determines which reference is selected. By default,
         the internal voltage reference VREF is selected. Based on customer application requirements, the
         external or internal reference can be selected. Refer to REFCTRL.REFSEL for further details on available
         selections.
         Related Links
         45.8.6 REFCTRL

45.6.2.6 ADC Resolution
         The ADC supports 8-bit, 10-bit or 12-bit resolution. Resolution can be changed by writing the Resolution
         bit group in the Control B register (CTRLB.RESSEL). By default, the ADC resolution is set to 12 bits. The
         resolution affects the propagation delay, see also 45.6.2.8 Conversion Timing and Sampling Rate.

45.6.2.7 Differential and Single-Ended Conversions
         The ADC has two conversion options: differential and single-ended.
         If the positive input is always positive, the single-ended conversion should be used in order to have full
         12-bit resolution in the conversion.
         If the positive input level may go below the negative input, the differential mode should be used in order to
         get correct results.
         The differential mode is enabled by writing a '1' to the DIFFMODE bit in the input control register
         (INPUTCTRL.DIFFMODE). Both conversion types could be run in single mode or in free-running mode.
         When the free-running mode is selected, an ADC input will continuously sample the input and performs a
         new conversion. The INTFLAG.RESRDY bit will be set at the end of each conversion.

45.6.2.8 Conversion Timing and Sampling Rate
         The following figure shows the ADC timing for one single conversion. A conversion starts after the
         software or event start are synchronized with the GCLK_ADCx clock. The input channel is sampled in the
         first half CLK_ADCx period.




        © 2019 Microchip Technology Inc.                          Datasheet                                          DS60001507E-page 1590
                                                                                              SAM D5x/E5x Family Data Sheet
                                                                                                              ADC – Analog-to-Digital Converter

Figure 45-3. ADC Timing for One Conversion in 12-bit Resolution
CLK_ADC



START


STATE             SAMPLING    MSB       10             9        8       7        6       5    4      3   2     1   LSB




INT




The sampling time can be increased by using the Sampling Time Length bit group in the Sampling Time
Control register (SAMPCTRL.SAMPLEN). As example, the next figure is showing the timing conversion
with sampling time increased to six CLK_ADC cycles.
Figure 45-4. ADC Timing for One Conversion with Increased Sampling Time, 12-bit
CLK_ADC



START


STATE                                       SAMPLING                            MSB      10   9      8   7     6    5       4        3     2      1   LSB




INT




The ADC provides also offset compensation, see the following figure. The offset compensation is enabled
by the Offset Compensation bit in the Sampling Control register (SAMPCTRL.OFFCOMP).
Note: If offset compensation is used, the sampling time must be set to one cycle of CLK_ADCx.
In free running mode, the sampling rate RS is calculated by
RS = fCLK_ADC / ( nSAMPLING + nOFFCOMP + nDATA)
Here, nSAMPLING is the sampling duration in CLK_ADC cycles, nOFFCOMP is the offset compensation
duration in clock cycles, and nDATA is the bit resolution. fCLK_ADC is the ADC clock frequency from the
internal prescaler: fCLK_ADC = fGCLK_ADC / 2^(1 + CTRLA.PRESCALER)
Figure 45-5. ADC Timing for One Conversion with Offset Compensation, 12-bit
CLK_ADC



START


STATE                 Offset Compensation        SAMPLING      MSB      10       9       8    7      6   5     4    3       2        1    LSB




INT




The impact of resolution on the sampling rate is seen in the next two figures, where free-running sampling
in 12-bit and 8-bit resolution are compared.
Figure 45-6. ADC Timing for Free Running in 12-bit Resolution

  CLK_ADC



  CONVERT


  STATE     LSB    SAMPLING    MSB          10             9        8       7        6    5   4      3   2     1   LSB   SAMPLING   MSB   10      9   8     7   6




  INT




© 2019 Microchip Technology Inc.                                                                  Datasheet                                     DS60001507E-page 1591
                                                                        SAM D5x/E5x Family Data Sheet
                                                                                               ADC – Analog-to-Digital Converter

        Figure 45-7. ADC Timing for Free Running in 8-bit Resolution

         CLK_ADC



         CONVERT


         STATE      LSB   SAMPLING   MSB      6    5   4    3   2   1   LSB   SAMPLING   MSB    6      5      4   3   2    1        LSB   SAMPLING   MSB




         INT




        The propagation delay of an ADC measurement is given by:
                                           1 + Resolution
        PropagationDelay =
                                                �ADC

                   Example. In order to obtain 1MSPS in 12-bit resolution with a sampling time length of
                   four CLK_ADC cycles, fCLK_ADC must be 1MSPS * (4 + 12) = 16MHz. As the minimal
                   division factor of the prescaler is 2, GCLK_ADC must be 32MHz.

45.6.2.9 Accumulation
        The results of multiple, consecutive conversions can be accumulated. The number of samples to be
        accumulated is specified by the Sample Number field in the Average Control register
        (AVGCTRL.SAMPLENUM). When accumulating more than 16 samples, the result will be too large to fit
        the 16-bit RESULT register size. To avoid overflow, the result is right shifted automatically to fit within the
        available register size. The number of automatic right shifts is specified in the table below.
        Note: To perform the accumulation of two or more samples, the Conversion Result Resolution field in
        the Control B register (CTRLB.RESSEL) must be set.
        Table 45-1. Accumulation

         Number of                           AVGCTRL.               Number of       Final Result                               Automatic
         Accumulated                         SAMPLENUM              Automatic Right Precision                                  Division Factor
         Samples                                                    Shifts
         1                                   0x0                    0                               12 bits                    0
         2                                   0x1                    0                               13 bits                    0
         4                                   0x2                    0                               14 bits                    0
         8                                   0x3                    0                               15 bits                    0
         16                                  0x4                    0                               16 bits                    0
         32                                  0x5                    1                               16 bits                    2
         64                                  0x6                    2                               16 bits                    4
         128                                 0x7                    3                               16 bits                    8
         256                                 0x8                    4                               16 bits                    16
         512                                 0x9                    5                               16 bits                    32
         1024                                0xA                    6                               16 bits                    64
         Reserved                            0xB –0xF                                               12 bits                    0




       © 2019 Microchip Technology Inc.                                  Datasheet                                        DS60001507E-page 1592
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                    ADC – Analog-to-Digital Converter

         Table 45-2. Accumulation

         Number of             AVGCTRL.               Intermediate     Number of                Final Result     Automatic
         Accumulated           SAMPLENUM              Result Precision Automatic                Precision        Division
         Samples                                                       Right Shifts                              Factor
         1                     0x0                    12 bits                0                  12 bits          0
         2                     0x1                    13 bits                0                  13 bits          0
         4                     0x2                    14 bits                0                  14 bits          0
         8                     0x3                    15 bits                0                  15 bits          0
         16                    0x4                    16 bits                0                  16 bits          0
         32                    0x5                    17 bits                1                  16 bits          2
         64                    0x6                    18 bits                2                  16 bits          4
         128                   0x7                    19 bits                3                  16 bits          8
         256                   0x8                    20 bits                4                  16 bits          16
         512                   0x9                    21 bits                5                  16 bits          32
         1024                  0xA                    22 bits                6                  16 bits          64
         Reserved              0xB –0xF               12 bits                                   12 bits          0

45.6.2.10 Averaging
         Averaging is a feature that increases the sample accuracy, at the cost of a reduced sampling rate. This
         feature is suitable when operating in noisy conditions.
         Averaging is done by accumulating m samples, as described in 45.6.2.9 Accumulation, and dividing the
         result by m. The averaged result is available in the RESULT register. The number of samples to be
         accumulated is specified by writing to AVGCTRL.SAMPLENUM as shown in Table 45-3.
         The division is obtained by a combination of the automatic right shift described above, and an additional
         right shift that must be specified by writing to the Adjusting Result/Division Coefficient field in AVGCTRL
         (AVGCTRL.ADJRES), as described in Table 45-3.
         Note: To perform the averaging of two or more samples, the Conversion Result Resolution field in the
         Control B register (CTRLB.RESSEL) must be set.
         Averaging AVGCTRL.SAMPLENUM samples will reduce the un-averaged sampling rate by a factor
                   1
                            .
         AVGCTRL.SAMPLENUM
         When the averaged result is available, the INTFLAG.RESRDY bit will be set.
         Table 45-3. Averaging
         Number of   AVGCTRL.              Intermediate   Number of      Division    AVGCTRL.    Total Number Final Result   Automatic
         Accumulated SAMPLENUM             Result         Automatic      Factor      ADJRES      of Right     Precision      Division
         Samples                           Precision      Right Shifts                           Shifts                      Factor

         1              0x0                12 bits        0              1           0x0                       12 bits       0

         2              0x1                13             0              2           0x1         1             12 bits       0

         4              0x2                14             0              4           0x2         2             12 bits       0




        © 2019 Microchip Technology Inc.                             Datasheet                            DS60001507E-page 1593
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                    ADC – Analog-to-Digital Converter

        ...........continued
         Number of   AVGCTRL.              Intermediate   Number of      Division       AVGCTRL.   Total Number Final Result   Automatic
         Accumulated SAMPLENUM             Result         Automatic      Factor         ADJRES     of Right     Precision      Division
         Samples                           Precision      Right Shifts                             Shifts                      Factor

         8                 0x3             15             0              8              0x3        3             12 bits       0

         16                0x4             16             0              16             0x4        4             12 bits       0

         32                0x5             17             1              16             0x4        5             12 bits       2

         64                0x6             18             2              16             0x4        6             12 bits       4

         128               0x7             19             3              16             0x4        7             12 bits       8

         256               0x8             20             4              16             0x4        8             12 bits       16

         512               0x9             21             5              16             0x4        9             12 bits       32

         1024              0xA             22             6              16             0x4        10            12 bits       64

         Reserved          0xB –0xF                                                     0x0                      12 bits       0


45.6.2.11 Oversampling and Decimation
        By using oversampling and decimation, the ADC resolution can be increased from 12 bits up to 16 bits,
        for the cost of reduced effective sampling rate.
        To increase the resolution by n bits, 4n samples must be accumulated. The result must then be right
        shifted by n bits. This right shift is a combination of the automatic right shift and the value written to
        AVGCTRL.ADJRES. To obtain the correct resolution, the ADJRES must be configured as described in the
        table below. This method will result in n bit extra LSB resolution.
        Table 45-4. Configuration Required for Oversampling and Decimation

         Result     Number of              AVGCTRL.SAMPLENUM[3:0]                   Number of           AVGCTRL.ADJRES[2:0]
         Resolution Samples to                                                      Automatic
                    Average                                                         Right Shifts
         13 bits               41 = 4      0x2                                      0                   0x1
         14 bits               42 = 16     0x4                                      0                   0x2
         15 bits               43 = 64     0x6                                      2                   0x1
         16 bits               44 = 256    0x8                                      4                   0x0

45.6.2.12 Window Monitor
        The window monitor feature allows comparing the conversion result in the RESULT register to predefined
        threshold values.
        The window mode is selected by writing the Window Monitor Mode bits in the Control B register
        (CTRLB.WINMODE). Threshold values must be written in the Window Monitor Lower Threshold register
        (WINLT) and Window Monitor Upper Threshold register (WINUT).
        When the Window Single Sample (CTRLB.WINSS) bit is written to '1', the window comparator is working
        on each sample instead of the accumulated value. The number of samples matching with window
        comparator is available on Window Comparator Counter bits (STATUS.WCC).
        In differential mode, WINLT and WINUT are evaluated as signed values. Otherwise they are evaluated as
        unsigned values. The significant WINLT and WINUT bits are given by the precision selected in the
        Conversion Result Resolution bit group in the Control B register (CTRLB.RESSEL). This means that for




        © 2019 Microchip Technology Inc.                             Datasheet                                DS60001507E-page 1594
                                                            SAM D5x/E5x Family Data Sheet
                                                                          ADC – Analog-to-Digital Converter

         example in 8-bit mode, only the eight lower bits will be considered. In addition, in differential mode, the
         eighth bit will be considered as the sign bit, even if the ninth bit is zero.
         The INTFLAG.WINMON interrupt flag is set when either the conversion result matches the window
         monitor condition, when the Window Comparator Counter is not zero in case of accumulation with
         CTRLB.WINSS=1.

45.6.2.13 Offset and Gain Correction
         Inherent gain and offset errors affect the absolute accuracy of the ADC.
         The offset error is defined as the deviation of the actual ADC transfer function from an ideal straight line
         at zero input voltage. The offset error cancellation is handled by the Offset Correction register
         (OFFSETCORR). The offset correction value is subtracted from the converted data before writing the
         Result register (RESULT).
         The gain error is defined as the deviation of the last output step’s midpoint from the ideal straight line,
         after compensating for offset error. The gain error cancellation is handled by the Gain Correction register
         (GAINCORR).
         To correct these two errors, the Digital Correction Logic Enabled bit in the Control B register
         (CTRLB.CORREN) must be set.
         Offset and gain error compensation results are both calculated according to:
         Result = Conversion value+ − OFFSETCORR ⋅ GAINCORR
         The correction will introduce a latency of 13 CLK_ADC clock cycles. In free running mode this latency is
         introduced on the first conversion only, since its duration is always less than the propagation delay. In
         single conversion mode this latency is introduced for each conversion.
         Figure 45-8. ADC Timing Correction Enabled
                          START




                                    CONV0        CONV1           CONV2           CONV3




                                             CORR0           CORR1           CORR2           CORR3




45.6.3   Additional Features

45.6.3.1 Device Temperature Measurement
         The device provides two temperature sensors (TSENSP and TSENSC, respectively) at different locations
         in the die, controlled by the SUPC - Supply Controller. The output voltages from the sensors, VTP and
         VTC, can be sampled by the ADC.
         The respective temperature sensor selection is dependent on the configuration of SUPC:
          • If the SUPC is not in on-demand mode (SUPC.VREF.ONDEMAND=0), and if SUPC.VREF.TSEN=1
             and SUPC.VREF.VREFOE=0, the temperature sensor is selected by writing to the Temperature




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1595
                                                            SAM D5x/E5x Family Data Sheet
                                                                          ADC – Analog-to-Digital Converter

              Sensor Channel Selection bit in the Voltage Reference System Control register
              (SUPC.VREF.TSSEL).

               SUPC                                  ADC

                                                           TSENSP
                   TSENSP
                                                           TSENSC
                                                                               ADC        RESULT
                                                               ...                            TP, TC
                   TSENSC



               VREF.OE, VREF.TSEN,                       INPUTCTRL.MUXPOS
                  VREF.TSSEL
            The state of the MUX input selection bit fields in the ADC Input Control register
            (ADC.INPUTCTRL.MUXPOS and MUXNEG) does not affect the sensor selection.
          • If the SUPC is in on-demand mode in (SUPC.VREF.ONDEMAND=1) and SUPC.VREF.TSEN=1, the
            output will be automatically set to the sensor requested by the ADC, independent of
            SUPC.VREF.TSSEL. SUPC.VREF.VREFOE can also be set to '1'.
              Which temperature sensor is requested by the ADC is selected by writing to the Positive MUX Input
              Selection bits in the Input Control register (ADC.INPUTCTRL.MUXPOS).
        Using the two conversion results, TP and TC, and the temperature calibration parameters found in the
        NVM Software Calibration Area, the die temperature T can be calculated:
              TL ⋅ VPH ⋅ TC − VPL ⋅ TH ⋅ TC − TL ⋅ VCH ⋅ TP + TH ⋅ VCL ⋅ TP
        �=
                       VCL ⋅ TP − VCH ⋅ TP − VPL ⋅ TC + VPH ⋅ TC
        Here, TL and TH are decimal numbers composed of their respective integer part (TLI, THI) and decimal
        parts (TLD and THD) from the NVM Software Calibration Area.
        Note: The accuracy is dependent on the current temperature, and degrades towards extreme
        conditions.
        Related Links
        19. SUPC – Supply Controller

45.6.3.2 Double Buffering
        The following registers are double buffered:
          • Input Control (INPUTCTRL)
          •   Control B (CTRLB)
          •   Reference Control (REFCTRL)
          •   Average Control (AVGCTRL)
          •   Sampling Time Control (SAMPCTRL)
          •   Window Monitor Lower Threshold (WINLT)
          •   Window Monitor Upper Threshold (WINUT)
          •   Gain Correction (GAINCORR)
          •   Offset Correction (OFFSETCORR)




        © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 1596
                                                            SAM D5x/E5x Family Data Sheet
                                                                             ADC – Analog-to-Digital Converter

        When one of these registers is written, the data is stored in the corresponding buffer as long as the
        current conversion is not impacted, and the corresponding busy status will be set in the Synchronization
        Busy register (SYNCBUSY). When a new RESULT is available, data stored in the buffer registers will be
        transfered to the ADC and a new conversion can start.
45.6.3.3 DMA Sequencing
        The ADC can sequence a series of conversion. When DMA sequencing is enabled, a set of ADC
        configuration registers can be automatically refreshed using the DMA controller.


                                                            Reload Request                                 ADC

                                                      DSEQCTRL                 DSEQSTAT



                                                                                               INPUTCTRL


                                                                                                 CTRLB


                                                                                                REFCTRL


                                                                                               AVGCTRL


                                                                                               SAMPCTRL

          DMA
                                     Peripheral Bus




                                                                                                 WINLT
        Controller                                        DSEQDATA

                                                                                                 WINUT


                                                                                               GAINCORR


                                                                                              OFFSETCORR




        Enabling DMA Sequencing
        DMA Sequencing is enabled when at least one bit in the DMA Sequence Control register (DSEQCTRL) is
        '1'.
        When this is the case, the BUSY status bit in the DMA Sequential Status register (DSEQSTAT.BUSY) is
        set to '1'.
        Disabling DMA Sequencing
        DMA Sequencing is disabled when at least one of the following conditions is valid:
         • The ADC is disabled (CTRLA.ENABLE = 0).
         • The ADC is reset (CTRLA.SWRST = 1).
         • The DMA Sequence Control register (DSEQCTRL) is written '0' and the ongoing DMA sequence is
           completed.




       © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1597
                                                SAM D5x/E5x Family Data Sheet
                                                              ADC – Analog-to-Digital Converter

  • The DMA Sequencing Stop bit in Input Control register is '1' (INPUTCTRL.DSEQSTOP = 1) and the
    ongoing DMA sequence is complete. One additional measurement will be done before the ADC is
    disabled.
When the DMA sequencing is disable, the BUSY status bit in the DMA Sequential Status register
(DSEQSTAT.BUSY) is cleared and the DMA trigger generation is disabled.
Note that if the DSEQCTRL register is written to a non-zero value, the DSEQSTOP bit in the INPUTCTRL
register will be cleared and the sequencing operation will not be stopped.
Restarting DMA Sequencing
When the DSEQSTOP bit is set (INPUTCTRL.DSEQSTOP = 1) and the sequence is disabled
(DSEQSTAT.BUSY=0), it is possible to restart the sequencing by enabling one of the following conditions:
  • Write the DSEQSTOP bit in Input Control register to zero (INPUTCTRL.DSEQSTOP = 0)
  • Apply a FLUSH software command (SWTRIG.FLUSH = 1)
  • Enable the flush event (EVCTRL.FLUSHEI). The sequence will restart when the flush event is
    received
DMA Sequencing Operation
Each ADC register that is part of the DMA sequencing has a separate enable bit in the DSEQCTRL
register to indicate that this field should be part of the DMA sequencing. When an enable bit in
DSEQCTRL is '1', the respective register will be updated when an access to DSEQDATA is decoded.
The DMA Sequencing (DSEQ) trigger request is generated when BUSY status bit is one
(DSEQSTAT.BUSY=1), the ADC is idle or a new conversion starts, and one of the following condition is
true:
  • Input Control or Control B bits in DMA Sequential Control register is '1' (DSEQCTRL.INPUTCTRL=1
     or DSEQCTRL.CTRLB=1)
  • Reference Control, Sampling Time Control or Average Control bits in DMA Sequential Control
     register is set (DSEQCTRL.REFCTRL=1, DSEQCTRL.AVGCTRL=1 or DSEQCTRL.SAMPCTRL=1)
  • Window Monitor Upper Threshold or Window Monitor Lower Threshold bits in DMA Sequential
     Control register is set (DSEQCTRL.WINUT=1 or DSEQCTRL.WINLT=1)
  • Offset Correction or Gain Correction bits in DMA Sequential Control register is set
     (DSEQCTRL.GAINCORR=1 or DSEQCTRL.OFFSETCORR=1)
Note: When received, the DMA data must be written to DSEQDATA register only, and only 32-bit DMA
access is supported.
If a field is not enabled for DMA update, the corresponding register update will be ignored when
DSEQDATA register is written. The table below shows the DSEQ trigger generation condition and internal
ADC registers refresh when the DSEQDATA register is written by the DMA.




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1598
                                               SAM D5x/E5x Family Data Sheet
                                                            ADC – Analog-to-Digital Converter

Table 45-5. DSEQ Trigger Generation and Internal ADC Register updates

 Condition                    Value      Action when DMA writes to DSEQDATA
 DSEQSTAT.INPUTCT             0           • No DMA trigger is generated
 RL or                                    • No data in the memory must be reserved
 DSEQSTAT.CTRLB
                              1           • A DMA trigger is generated
                                          • One word (32-bit) must be reserved in the memory
                                          • INPUTCTRL ← DSEQDATA[15:0] if
                                            DSEQSTAT.INPUTCTRL = 1
                                          • CTRLB ← DSEQDATA[31:16] if DSEQSTAT.CTRLB = 1

 DSEQSTAT.REFCTRL 0                       • No DMA trigger is generated
 or                                       • No data in the memory must be reserved
 DSEQSTAT.AVGCTRL
 or               1                       • A DMA trigger is generated
 DSEQSTAT.SAMPCT                          • One word (32-bit) must be reserved in the memory
 RL                                       • REFCTRL ← DSEQDATA[7:0] if DSEQSTAT.REFCTRL
                                            =1
                                          • AVGCTRL ← DSEQDATA[23:16] if
                                            DSEQSTAT.AVGCTRL = 1
                                          • SAMPCTRL ← DSEQDATA[31:24] if
                                            DSEQSTAT.SAMPCTRL = 1

 DSEQSTAT.WINLT or            0           • No DMA trigger is generated
 DSEQSTAT.WINUT                           • No data in the memory must be reserved

                              1           •   A DMA trigger is generated
                                          •   One word (32-bit) must be reserved in the memory
                                          •   WINLT ← DSEQDATA[15:0] if DSEQSTAT.WINLT = 1
                                          •   WINUT ← DSEQDATA[31:16] if DSEQSTAT.WINUT = 1

 DSEQSTAT.GAINCOR 0                       • No DMA trigger is generated
 R or                                     • No data in the memory must be reserved
 DSEQSTAT.OFFSETC
 ORR              1                       • A DMA trigger is generated
                                          • One word (32-bit) must be reserved in the memory
                                          • GAINCORR ← DSEQDATA[15:0] if
                                            DSEQSTAT.GAINCORR = 1
                                          • OFFSETCORR ← DSEQDATA[31:16] if
                                            DSEQSTAT.OFFSETCORR = 1

The DMA Sequential Status register (DSEQSTAT) stores the remaining registers to be updated by the
DMA. During a sequence and when a write access to the DSEQDATA register is detected, the
DSEQSTAT bits which were source of the corresponding DSEQ trigger will be cleared. When all
DSEQSTAT bits are zero (except BUSY bit), the DSEQCTRL register bits (except AUTOSTART) are
copied into the DSEQSTAT register and a new DMA sequence is started when a new ADC conversion
starts.




© 2019 Microchip Technology Inc.                Datasheet                       DS60001507E-page 1599
                                                      SAM D5x/E5x Family Data Sheet
                                                                  ADC – Analog-to-Digital Converter

DMA Descriptor Setup and Data Memory Organization
When DMA sequencing is enabled, the DMA Controller (DMAC) must be configured in the following way:
 • Select 32-bit beat size transfer (DMAC.BTCTRL.BEATSIZE=WORD).
 • Enable the source address increment options (DMAC.BTCTRL.SRCINC = 1,
   DMAC.BTCTRL.STEPSEL = SRC, DMAC.BTCTRL.STEPSIZE = X1).
 • Disable the destination address increment (DMAC.BTCTRL.DSTINC=0).
 • Set the block transfer count value (DMAC.BTCNT).
 • Set the block transfer source address (DMAC.SRCADDR), as described in the DMAC Addressing
   section. The address corresponds to the memory section from where the DMA reads the data.
 • Select the ADC.DSEQDATA address as value for the block transfer destination address
   (DMAC.DSTADDR = ADC.DSEQDATA address).
 • Select the channel single transfer type (DMAC.CHCTRLA.BURSTLEN=SINGLE)
 • Select the channel burst trigger action (DMAC.CHCTRLA.TRIGACT=BURST)
 • Select the ADC DMA Sequencing trigger as channel trigger source
   (DMAC.CHCTRLA.TRIGSRC=DSEQ)
 • Enable optional channel interrupts (DMAC.CHINTENSET)
 • Enable the corresponding DMA channel (DMAC.CHCTRLA.ENABLE)
When an ADC condition is enabled to trigger a DMA transfer, one word (32-bit) will be read by the DMA
from the memory source location. Since the source address is incrementing by 0x1, the data memory
must be organized in a contiguous memory area. As consequence, if an ADC group of registers does not
generate any DMA trigger, no data must be reserved in the memory area for this register group. The next
figure shows an example of memory organization when all ADC registers are part of the sequence, and a
second example where WINLT and WINUT registers are not part of the sequence.

  Memory                                                    Memory
                                    +0x00                                                        +0x00
         INPUTCTRL                                                 INPUTCTRL

            CTRLB                                                     CTRLB
                                    +0x04                                                        +0x04
         REFCTRL                                                    REFCTRL
        DON'T CARE                                                 DON'T CARE
         AVGCTRL                                                    AVGCTRL
        SAMPCTRL                    +0x08                          SAMPCTRL                      +0x08
            WINLT                                                  GAINCORR

            WINUT                                                 OFFSETCORR
                                    +0x0C                                                        +0x0C = SRCADDR
         GAINCORR

       OFFSETCORR
                                    +0x10 = SRCADDR




All registers are in the sequence                          WINLT / WINUT registers are not in the sequence
Automatic Start Conversion




© 2019 Microchip Technology Inc.                      Datasheet                             DS60001507E-page 1600
                                                           SAM D5x/E5x Family Data Sheet
                                                                         ADC – Analog-to-Digital Converter

         By default, a new conversion starts when a new start software or event trigger is received. It is also
         possible to automatically enable an ADC conversion by writing '1' to the AUTOSTART bit in DSEQCTRL
         register (DSEQCTRL.AUTOSTART). When set, the ADC automatically starts a new conversion when a
         DMA sequence is complete.
         Note: If averaging or oversampling is enabled, the new conversion automatically starts only when the
         previous RESULT is available (averaging or oversampling operation is complete).
         Note: If the free-run mode is enabled (CTRLB.FREERUN=1), the new conversion automatically starts
         when the previous RESULT is available and the DMA sequence is complete. As consequence, the
         AUTOSTART bit has no effect in free-run operating mode.
         Note: If the conversion is triggered by event (EVCTRL.STARTEI=1), the automatic start conversion is
         disabled and the AUTOSTART settings are ignored.
         Related Links
         22.6.2.7 Addressing

45.6.3.4 Master - Slave Operation
         ADC1 will serve as a slave of ADC0 by writing a '1' to the Slave Enable bit in the Control A register of the
         ADC1 instance (ADC1.CTRLA.SLAVEEN). When enabled, GCLK_ADC0 clock and ADC0 controls are
         internally routed to the ADC1 instance.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1601
                                                      SAM D5x/E5x Family Data Sheet
                                                                    ADC – Analog-to-Digital Converter

                                                                      ADC0.DSEQCTRL

                                             ADC0.AVGCTRL              ADC0.WINLT

                                             ADC0.SAMPCTRL             ADC0.WINUT

                                              ADC0.EVCTRL            ADC0.OFFSETCORR

                                              ADC0.SWTRIG             ADC0.GAINCORR
   ADC0
    ...
   ADCn
 INT.SIG
                                                                                        ADC0.RESULT
            ADC0.INPUTCTRL                   ADC 0                       POST
                                                                       PROCESSING
                                                                                       ADC0.DSEQSTAT
   ADC0
    ...
   ADCn
                     INT1V                           ADC0.CTRLA
                    INTVCC0
                    INTVCC1
                      VREFA
                        ...
                      VREFn                         PRESCALER


                              ADC0.REFCTRL

  ADC0
   ...
  ADCn
INT.SIG
                                                                                        ADC1.RESULT

                                              ADC 1
                                                                         POST
           ADC1.INPUTCTRL
                                                                       PROCESSING
                                                                                       ADC1.DSEQSTAT
  ADC0
   ...
  ADCn
                     INT1V                         ADC1.CTRLA         ADC1.GAINCORR
                                                    SLAVEEN
                    INTVCC0
                    INTVCC1
                                                  ADC1.AVGCTRL       ADC1.OFFSETCORR
                      VREFA
                        ...
                      VREFn                      ADC1.SAMPCTRL          ADC1.WINUT

                                                  ADC1.SWTRIG           ADC1.WINLT
                              ADC1.REFCTRL
                                                  ADC1.SWTRIG         ADC1.DSEQCTRL

In this mode of operation, the slave ADC1 is enabled by accessing the CTRLA register of the master
ADC0. In the same way, the master ADC event inputs will be automatically routed to the slave ADC,
meaning that the input events configuration must be done in the master ADC (ADC0.EVCTRL).
ADC measurements can either start simultaneously on both ADCs, or be interleaved. The trigger mode
selection is available in the master ADC Control A register (ADC0.CTRLA.DUALSEL).
Note: The interleaved sampling is only usable in single conversion mode (ADC.CTRLB.FREERUN=0).
To restart an interleaved sequence, the user can apply different options:
 • Flush the master ADC (ADC0.SWTRIG.FLUSH = 1)
 • Disable/re-enable the master ADC (ADC0.CTRLA.ENABLE)




© 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1602
                                                                           SAM D5x/E5x Family Data Sheet
                                                                                               ADC – Analog-to-Digital Converter

           • Reset and reconfigure master ADC (ADC0.CTRLA.SWRST = 1)
           • Enable the flush event (EVCTRL.FLUSHEI = 1)

            Start Trigger
         (Software or Event)



                       ADC0 Start Conversion   ADC1 Start Conversion   ADC0 Start Conversion     ADC1 Start Conversion   ADC0 Start Conversion



45.6.4   DMA Operation
         The ADC generates the following DMA request:
           • Result Conversion Ready (RESRDY): the request is set when a conversion result is available and
             cleared when the RESULT register is read. When the averaging operation is enabled, the DMA
             request is set when the averaging is completed and result is available.
           • DMA Sequencing (DSEQ): for details refer to "add link to DMA sequencing"

45.6.5   Interrupts
         The ADC has the following interrupt sources:
           • Result Conversion Ready: RESRDY
           • Window Monitor: WINMON
           • Overrun: OVERRUN
         These interrupts, except the OVERRUN interrupt, are asynchronous wake-up sources. See Sleep Mode
         Controller for details.
         Each interrupt source has an interrupt flag associated with it. The interrupt flag in the Interrupt Flag Status
         and Clear (INTFLAG) register is set when the interrupt condition occurs. Each interrupt can be
         individually enabled by writing a one to the corresponding bit in the Interrupt Enable Set (INTENSET)
         register, and disabled by writing a one to the corresponding bit in the Interrupt Enable Clear (INTENCLR)
         register. An interrupt request is generated when the interrupt flag is set and the corresponding interrupt is
         enabled. The interrupt request remains active until the interrupt flag is cleared, the interrupt is disabled, or
         the ADC is reset. See INTFLAG register for details on how to clear interrupt flags. All interrupt requests
         from the peripheral are ORed together on system level to generate one combined interrupt request to the
         NVIC. Refer to Nested Vector Interrupt Controller for details. The user must read the INTFLAG register to
         determine which interrupt condition is present.
         Note that interrupts must be globally enabled for interrupt requests to be generated. Refer to Nested
         Vector Interrupt Controller for details.
         Related Links
         45.8.16 INTFLAG

45.6.6   Events
         The ADC can generate the following output events:
           • Result Ready (RESRDY): Generated when the conversion is complete and the result is available.
             Refer to EVCTRL register for details.
           • Window Monitor (WINMON): Generated when the window monitor condition match. Refer to CTRLB
             register for details.
         Setting an Event Output bit in the Event Control Register (EVCTRL.xxEO=1) enables the corresponding
         output event. Clearing this bit disables the corresponding output event. Refer to the Event System
         chapter for details on configuring the event system.




         © 2019 Microchip Technology Inc.                                     Datasheet                                  DS60001507E-page 1603
                                                             SAM D5x/E5x Family Data Sheet
                                                                         ADC – Analog-to-Digital Converter

         The ADC can take the following actions on an input event:
           • Start conversion (START): Start a conversion. Refer to SWTRIG register for details.
           • Conversion flush (FLUSH): Flush the conversion. Refer to SWTRIG register for details.
         Setting an Event Input bit in the Event Control register (EVCTRL.xxEI=1) enables the corresponding
         action on input event. Clearing this bit disables the corresponding action on input event.
         The ADC uses only asynchronous events, so the asynchronous Event System channel path must be
         configured. By default, the ADC will detect a rising edge on the incoming event. If the ADC action must be
         performed on the falling edge of the incoming event, the event line must be inverted first. This is done by
         setting the corresponding Event Invert Enable bit in Event Control register (EVCTRL.xINV=1).
         Note: If several events are connected to the ADC, the enabled action will be taken on any of the
         incoming events. If FLUSH and START events are available at the same time, the FLUSH event has
         priority.
         Related Links
         45.8.2 EVCTRL
         45.8.5 CTRLB
         45.8.13 SWTRIG
         31. EVSYS – Event System

45.6.7   Sleep Mode Operation
         The ONDEMAND and RUNSTDBY bits in the Control A register (CTRLA) control the behavior of the ADC
         during standby sleep mode, in cases where the ADC is enabled (CTRLA.ENABLE = 1). For further details
         on available options, refer to Table 45-6.
         Note: When CTRLA.ONDEMAND=1, the analog block is powered-off when the conversion is complete.
         When a start request is detected, the system returns from sleep and starts a new conversion after the
         start-up time delay.
         Table 45-6. ADC Sleep Behavior

          CTRLA.RUNSTDBY CTRLA.ONDEMAND CTRLA.ENABLE Description
          x                         x                  0                   Disabled
          0                         0                  1                   Run in all sleep modes except
                                                                           STANDBY.
          0                         1                  1                   Run in all sleep modes on request,
                                                                           except STANDBY.
          1                         0                  1                   Run in all sleep modes.
          1                         1                  1                   Run in all sleep modes on request.

45.6.8   Synchronization
         Due to asynchronicity between the main clock domain and the peripheral clock domains, some registers
         need to be synchronized when written or read.
         The following bits are synchronized when written:
           • Software Reset bit in Control A register (CTRLA.SWRST)
           • Enable bit in Control A register (CTRLA.ENABLE)




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1604
                                                 SAM D5x/E5x Family Data Sheet
                                                               ADC – Analog-to-Digital Converter

The following registers are synchronized when written:
  •   Input Control register (INPUTCTRL)
  •   Control B register (CTRLB)
  •   Reference Control (REFCTRL)
  •   Average control register (AVGCTRL)
  •   Sampling time control register (SAMPCTRL)
  •   Window Monitor Lower Threshold register (WINLT)
  •   Window Monitor Upper Threshold register (WINUT)
  •   Gain correction register (GAINCORR)
  •   Offset Correction register (OFFSETCORR)
  •   Software Trigger register (SWTRIG)
Required write synchronization is denoted by the "Write-Synchronized" property in the register
description.




© 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1605
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                    ADC – Analog-to-Digital Converter


45.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0     ONDEMAND RUNSTDBY       SLAVEEN           DUALSEL[1:0]                          ENABLE       SWRST
 0x00         CTRLA
                             15:8       R2R                                                                       PRESCALER[2:0]
 0x02         EVCTRL          7:0                            WINMONEO RESRDYEO          STARTINV      FLUSHINV       STARTEI       FLUSHEI
 0x03        DBGCTRL          7:0                                                                                                  DBGRUN
                              7:0     DIFFMODE                                                       MUXPOS[4:0]
 0x04       INPUTCTRL
                             15:8     DSEQSTOP                                                       MUXNEG[4:0]
                              7:0                                                RESSEL[1:0]           CORREN        FREERUN       LEFTADJ
 0x06         CTRLB
                             15:8                                                         WINSS                    WINMODE[2:0]
 0x08        REFCTRL          7:0     REFCOMP                                                                 REFSEL[3:0]
 0x09        Reserved
 0x0A        AVGCTRL          7:0                            ADJRES[2:0]                                 SAMPLENUM[3:0]
 0x0B       SAMPCTRL          7:0     OFFCOMP                                                  SAMPLEN[5:0]
                              7:0                                                 WINLT[7:0]
 0x0C          WINLT
                             15:8                                                WINLT[15:8]
                              7:0                                                 WINUT[7:0]
 0x0E         WINUT
                             15:8                                                WINUT[15:8]
                              7:0                                               GAINCORR[7:0]
 0x10       GAINCORR
                             15:8                                                                        GAINCORR[11:8]
                              7:0                                              OFFSETCORR[7:0]
 0x12      OFFSETCORR
                             15:8                                                                       OFFSETCORR[11:8]
 0x14         SWTRIG          7:0                                                                                     START         FLUSH
 0x15
   ...       Reserved
 0x2B
 0x2C        INTENCLR         7:0                                                                      WINMON        OVERRUN       RESRDY
 0x2D        INTENSET         7:0                                                                      WINMON        OVERRUN       RESRDY
 0x2E        INTFLAG          7:0                                                                      WINMON        OVERRUN       RESRDY
 0x2F         STATUS          7:0                                   WCC[5:0]                                                       ADCBUSY
                              7:0       WINLT     SAMPCTRL    AVGCTRL      REFCTRL        CTRLB      INPUTCTRL        ENABLE       SWRST
                                                                                                     OFFSETCOR
                             15:8                                                        SWTRIG                     GAINCORR        WINUT
 0x30       SYNCBUSY                                                                                      R
                             23:16
                             31:24     RBSSW
                              7:0                                                 DATA[7:0]
                             15:8                                                 DATA[15:8]
 0x34       DSEQDATA
                             23:16                                               DATA[23:16]
                             31:24                                               DATA[31:24]
                              7:0     GAINCORR     WINUT       WINLT       SAMPCTRL     AVGCTRL       REFCTRL         CTRLB       INPUTCTRL
                                                                                                                                  OFFSETCOR
                             15:8
 0x38       DSEQCTRL                                                                                                                 R
                             23:16
                             31:24    AUTOSTART




          © 2019 Microchip Technology Inc.                             Datasheet                                   DS60001507E-page 1606
                                                                     SAM D5x/E5x Family Data Sheet
                                                                                     ADC – Analog-to-Digital Converter

...........continued

  Offset               Name     Bit Pos.

                                  7:0      GAINCORR   WINUT      WINLT       SAMPCTRL   AVGCTRL   REFCTRL       CTRLB       INPUTCTRL
                                                                                                                         OFFSETCOR
                                 15:8
   0x3C           DSEQSTAT                                                                                                     R
                                 23:16
                                 31:24      BUSY
                                  7:0                                            RESULT[7:0]
   0x40                RESULT
                                 15:8                                            RESULT[15:8]
   0x42
     ...           Reserved
   0x43
                                  7:0                                             RESS[7:0]
   0x44                RESS
                                 15:8                                             RESS[15:8]
   0x46
     ...           Reserved
   0x47
                                  7:0                         BIASR2R[2:0]                                  BIASCOMP[2:0]
   0x48                CALIB
                                 15:8                                                                       BIASREFBUF[2:0]




45.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to the section on Synchronization.
               Some registers are synchronized when read and/or written. Synchronization is denoted by the "Write-
               Synchronized" or the "Read-Synchronized" property in each individual register description. For details,
               refer to Synchronization section.
               Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
               Enable-protection is denoted by the "Enable-Protected" property in each individual register description.
               Related Links
               45.6.8 Synchronization




              © 2019 Microchip Technology Inc.                           Datasheet                           DS60001507E-page 1607
                                                                    SAM D5x/E5x Family Data Sheet
                                                                                     ADC – Analog-to-Digital Converter

45.8.1         Control A

               Name:        CTRLA
               Offset:      0x00
               Reset:       0x0000
               Property:    Enable-Protected, PAC Write-Protection, Write-Synchronized


         Bit        15            14            13            12             11             10         9              8
                   R2R                                                                           PRESCALER[2:0]
   Access           R/W                                                                    R/W        R/W            R/W
    Reset            0                                                                      0          0              0


         Bit         7             6             5            4                  3          2          1              0
                ONDEMAND      RUNSTDBY        SLAVEEN             DUALSEL[1:0]                      ENABLE        SWRST
   Access           R/W          R/W            R/W          R/W            R/W                       R/W            R/W
    Reset            0             0             0            0                  0                     0              0


               Bit 15 – R2R Rail to Rail Operation Enable
               Value      Description
               0          Rail-to-Rail operation disable
               1          Rail-to-Rail operation enable. The R2R bit must be set to ‘1’ only in differential mode.

               Bits 10:8 – PRESCALER[2:0] Prescaler Configuration
               This field defines the ADC clock relative to the peripheral clock according Table below. This field is not
               synchronized. For the slave ADC, these bits have no effect when the SLAVEEN bit is set
               (CTRLA.SLAVEEN= 1).
                Value       Name                Description
                0x0         DIV2                Peripheral clock divided by 2
                0x1         DIV4                Peripheral clock divided by 4
                0x2         DIV8                Peripheral clock divided by 8
                0x3         DIV16               Peripheral clock divided by 16
                0x4         DIV32               Peripheral clock divided by 32
                0x5         DIV64               Peripheral clock divided by 64
                0x6         DIV128              Peripheral clock divided by 128
                0x7         DIV256              Peripheral clock divided by 256

               Bit 7 – ONDEMAND On Demand Control
               The On Demand operation mode allows the ADC to be enabled or disabled, depending on other
               peripheral requests.
               In On Demand operation mode, i.e., if the ONDEMAND bit has been previously set, the ADC will only be
               running when requested by a peripheral. If there is no peripheral requesting the ADC will be in a disable
               state.
               If On Demand is disabled the ADC will always be running when enabled.
               In standby sleep mode, the On Demand operation is still active if the CTRLA.RUNSTDBY bit is '1'. If
               CTRLA.RUNSTDBY is '0', the ADC is disabled.
               This bit is not synchronized.
               Note: For the slave ADC, this bit has no effect when the SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
               ONDEMAND bit from master ADC instance will control the On Demand operation mode.




           © 2019 Microchip Technology Inc.                           Datasheet                        DS60001507E-page 1608
                                                 SAM D5x/E5x Family Data Sheet
                                                               ADC – Analog-to-Digital Converter

 Value        Description
 0            The ADC is always on , if enabled.
 1            The ADC is enabled, when a peripheral is requesting the ADC conversion. The ADC is
              disabled if no peripheral is requesting it.

Bit 6 – RUNSTDBY Run in Standby
This bit controls how the ADC behaves during standby sleep mode.
This bit is not synchronized.
Note: For the slave ADC, this bit has no effect when the SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
RUNSTDBY bit from master ADC instance will control the slave ADC operation in standby sleep mode.
 Value        Description
 0            The ADC is halted during standby sleep mode.
 1            The ADC is not stopped in standby sleep mode. If CTRLA.ONDEMAND=1, the ADC will be
              running when a peripheral is requesting it. If CTRLA.ONDEMAND=0, the ADC will always be
              running in standby sleep mode.

Bit 5 – SLAVEEN Slave Enable
This bit enables the master/slave operation and it is available only in the slave ADC instance.
This bit is not synchronized and can be set only for the slave ADC. For the master ADC, this bit is always
read zero.
 Value       Description
 0           The master/slave operation is disabled
 1           The ADC1 is enabled as a slave of ADC0

Bits 4:3 – DUALSEL[1:0] Dual Mode Trigger Selection
These bits define the trigger mode, as shown in Table below. These bits are available in the master ADC
and have no effect if the master/slave operation is disabled (ADC1.CTRLA.SLAVEEN=0).
 Value      Name            Description
 0x0        BOTH            Start event or software trigger will start a conversion on both ADCs
 0x1        INTERLEAVE START event or software trigger will alternatingly start a conversion on ADC0
                            and ADC1.
                            Note: The interleaved sampling is only usable in single conversion mode
                            (ADC.CTRLB.FREERUN=0).
 0x2 -                      Reserved
 0x3

Bit 1 – ENABLE Enable
Due to synchronization there is delay from writing CTRLA.ENABLE until the peripheral is enabled/
disabled. The value written to CTRL.ENABLE will read back immediately and the ENABLE bit in the
Synchronization Busy register (SYNCBUSY.ENABLE) will be set. SYNCBUSY.ENABLE will be cleared
when the operation is complete.
For the slave ADC, this bit has no effect when the SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
 Value      Description
 0          The ADC is disabled.
 1          The ADC is enabled.

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.




© 2019 Microchip Technology Inc.                   Datasheet                         DS60001507E-page 1609
                                                   SAM D5x/E5x Family Data Sheet
                                                                 ADC – Analog-to-Digital Converter

Writing a '1' to this bit resets all registers in the ADC, except DBGCTRL, to their initial state, and the ADC
will be disabled.
Writing a '1' to CTRL.SWRST will always take precedence, meaning that all other writes in the same
write-operation will be discarded.
Due to synchronization there is a delay from writing CTRLA.SWRST until the reset is complete.
CTRLA.SWRST and SYNCBUSY.SWRST will both be cleared when the reset is complete.
Value         Description
0             There is no reset operation ongoing.
1             The reset operation is ongoing.




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1610
                                                                 SAM D5x/E5x Family Data Sheet
                                                                               ADC – Analog-to-Digital Converter

45.8.2         Event Control

               Name:       EVCTRL
               Offset:     0x02
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6              5          4             3            2            1             0
                                              WINMONEO   RESRDYEO     STARTINV     FLUSHINV      STARTEI      FLUSHEI
   Access                                       R/W        R/W           R/W          R/W          R/W          R/W
    Reset                                        0          0             0            0            0             0


               Bit 5 – WINMONEO Window Monitor Event Out
               This bit indicates whether the Window Monitor event output is enabled or not and an output event will be
               generated when the window monitor detects something.
                Value       Description
                0            Window Monitor event output is disabled and an event will not be generated.
                1            Window Monitor event output is enabled and an event will be generated.

               Bit 4 – RESRDYEO Result Ready Event Out
               This bit indicates whether the Result Ready event output is enabled or not and an output event will be
               generated when the conversion result is available.
                Value       Description
                0            Result Ready event output is disabled and an event will not be generated.
                1            Result Ready event output is enabled and an event will be generated.

               Bit 3 – STARTINV Start Conversion Event Invert Enable
               For the slave ADC, this bit has no effect when the SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
                Value      Description
                0          Start event input source is not inverted.
                1          Start event input source is inverted.

               Bit 2 – FLUSHINV Flush Event Invert Enable
               For the slave ADC, this bit has no effect when the SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
                Value      Description
                0          Flush event input source is not inverted.
                1          Flush event input source is inverted.

               Bit 1 – STARTEI Start Conversion Event Input Enable
               For the slave ADC, this bit has no effect when the SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
                Value      Description
                0          A new conversion will not be triggered on any incoming event.
                1          A new conversion will be triggered on any incoming event.

               Bit 0 – FLUSHEI Flush Event Input Enable
               For a slave ADC, this bit has no effect when the respective SLAVEEN bit is set (CTRLA.SLAVEEN= 1).
                Value      Description
                0          A flush and new conversion will not be triggered on any incoming event.




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1611
                                                  SAM D5x/E5x Family Data Sheet
                                                                ADC – Analog-to-Digital Converter

 Value        Description
 1            A flush and new conversion will be triggered on any incoming event.




© 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 1612
                                                             SAM D5x/E5x Family Data Sheet
                                                                          ADC – Analog-to-Digital Converter

45.8.3         Debug Control

               Name:       DBGCTRL
               Offset:     0x03
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit        7             6           5          4            3           2            1           0
                                                                                                        DBGRUN
   Access                                                                                                 R/W
    Reset                                                                                                  0


               Bit 0 – DBGRUN Debug Run
               This bit is not reset by a software reset.
               This bit controls the functionality when the CPU is halted by an external debugger.
               This bit should be written only while a conversion is not ongoing.
               When slave operation is enabled, master and slave ADC instances must have the same DBGRUN bit
               value tu ensure proper operation.
                Value       Description
                0           The ADC is halted when the CPU is halted by an external debugger.
                1           The ADC continues normal operation when the CPU is halted by an external debugger.




           © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 1613
                                                                 SAM D5x/E5x Family Data Sheet
                                                                              ADC – Analog-to-Digital Converter

45.8.4         Input Control

               Name:       INPUTCTRL
               Offset:     0x04
               Reset:      0x0000
               Property:   PAC Write-Protection, Write-Synchronized


         Bit        15           14            13           12           11           10            9            8
                DSEQSTOP                                                          MUXNEG[4:0]
   Access          R/W                                     R/W          R/W           R/W          R/W          R/W
    Reset            0                                      0             0            0            0            0


         Bit         7            6            5            4             3            2            1            0
                DIFFMODE                                                          MUXPOS[4:0]
   Access          R/W                                     R/W          R/W           R/W          R/W          R/W
    Reset            0                                      0             0            0            0            0


               Bit 15 – DSEQSTOP Stop DMA Sequencing
               When the bit is set, the DMA sequencing automatically stops when the last sequence configuration is
               complete.
               Note: one more conversion will be done after the last sequence is complete.

               Bits 12:8 – MUXNEG[4:0] Negative MUX Input Selection
               These bits define the MUX selection for the negative ADC input.
                Value      Name                         Description
                0x00       AIN0                          ADC AIN0 pin
                0x01       AIN1                          ADC AIN1 pin
                0x02       AIN2                          ADC AIN2 pin
                0x03       AIN3                          ADC AIN3 pin
                0x04       AIN4                          ADC AIN4 pin
                0x05       AIN5                          ADC AIN5 pin
                0x06       AIN6                          ADC AIN6 pin
                0x07       AIN7                          ADC AIN7 pin
                0x08 -                                   Reserved
                0x17
                0x18       GND                           Internal ground
                0x19 -                                   Reserved
                0x1F

               Bit 7 – DIFFMODE Differential Mode
               Value       Description
               0x0         The ADC is running in singled-ended mode.
               0x1         The ADC is running in differential mode. In this mode, the voltage difference between the
                           MUXPOS and MUXNEG inputs will be converted by the ADC.

               Bits 4:0 – MUXPOS[4:0] Positive MUX Input Selection
               These bits define the MUX selection for the positive ADC input. If the internal bandgap voltage or
               temperature sensor input channel is selected, then the Sampling Time Length bit group in the Sampling




           © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1614
                                                 SAM D5x/E5x Family Data Sheet
                                                              ADC – Analog-to-Digital Converter

Control register must be written with a corresponding value, as shown in “Table 54-24. Operating
Conditions”.
Value       Name                                       Description
0x00        AIN0                                       ADC AIN0 pin
0x01        AIN1                                       ADC AIN1 pin
0x02        AIN2                                       ADC AIN2 pin
0x03        AIN3                                       ADC AIN3 pin
0x04        AIN4                                       ADC AIN4 pin
0x05        AIN5                                       ADC AIN5 pin
0x06        AIN6                                       ADC AIN6 pin
0x07        AIN7                                       ADC AIN7 pin
0x08        AIN8                                       ADC AIN8 pin
0x09        AIN9                                       ADC AIN9 pin
0x0A        AIN10                                      ADC AIN10 pin
0x0B        AIN11                                      ADC AIN11 pin
0x0C        AIN12                                      ADC AIN12 pin
0x0D        AIN13                                      ADC AIN13 pin
0x0E        AIN14                                      ADC AIN14 pin
0x0F        AIN15                                      ADC AIN15 pin
0x10        AIN16                                      ADC AIN16 pin
0x11        AIN17                                      ADC AIN17 pin
0x12        AIN18                                      ADC AIN18 pin
0x13        AIN19                                      ADC AIN19 pin
0x14        AIN20                                      ADC AIN20 pin
0x15        AIN21                                      ADC AIN21 pin
0x16        AIN22                                      ADC AIN22 pin
0x17        AIN23                                      ADC AIN23 pin
0x18        SCALEDCOREVCC                              1/4 Scaled Core Supply
0x19        SCALEDVBAT                                 1/4 Scaled VBAT Supply
0x1A        SCALEDIOVCC                                1/4 Scaled I/O Supply
0x1B        BANDGAP                                    Bandgap Voltage
0x1C        PTAT                                       Temperature Sensor
0x1D        CTAT                                       Temperature Sensor
0x1E        DAC                                        DAC Output




© 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1615
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                    ADC – Analog-to-Digital Converter

45.8.5         Control B

               Name:       CTRLB
               Offset:     0x06
               Reset:      0x0000
               Property:   PAC Write-Protection, Write-Synchronized


         Bit        15           14            13           12                 11          10         9             8
                                                                          WINSS                  WINMODE[2:0]
   Access                                                                  R/W            R/W        R/W          R/W
    Reset                                                                      0           0          0             0


         Bit         7            6            5            4                  3           2          1             0
                                                                 RESSEL[1:0]            CORREN    FREERUN        LEFTADJ
   Access                                                  R/W             R/W            R/W        R/W          R/W
    Reset                                                   0                  0           0          0             0


               Bit 11 – WINSS Window Single Sample
               When this bit is written the window functionality is working on each conversions and not on the
               accumulated value. The number of convesions matching with the window comparator is available on
               STATUS register (STATUS.WCC). The last sample result is available on RESS register.

               Bits 10:8 – WINMODE[2:0] Window Monitor Mode
               These bits enable and define the window monitor mode.
                Value      Name                    Description
                0x0        DISABLE                 No window mode (default)
                0x1        MODE1                   RESULT > WINLT
                0x2        MODE2                   RESULT < WINUT
                0x3        MODE3                   WINLT < RESULT < WINUT
                0x4        MODE4                   !(WINLT < RESULT < WINUT)
                0x5 -                              Reserved
                0x7

               Bits 4:3 – RESSEL[1:0] Conversion Result Resolution
               These bits define whether the ADC completes the conversion 12-, 10- or 8-bit result resolution.
                Value      Name               Description
                0x0        12BIT              12-bit result
                0x1        16BIT              For averaging mode output
                0x2        10BIT              10-bit result
                0x3        8BIT               8-bit result

               Bit 2 – CORREN Digital Correction Logic Enable
               The ADC conversion result in the RESULT register is then corrected for gain and offset based on the
               values in the GAINCORR and OFFSETCORR registers. Conversion time will be increased by 13 cycles
               according to the value in the Offset Correction Value bit group in the Offset Correction register.
                Value      Description
                0          Disable the digital result correction
                1          Enable the digital result correction




           © 2019 Microchip Technology Inc.                         Datasheet                        DS60001507E-page 1616
                                                     SAM D5x/E5x Family Data Sheet
                                                                   ADC – Analog-to-Digital Converter

Bit 1 – FREERUN Free Running Mode
Value      Description
0          The ADC run in single conversion mode
1          The ADC is in free running mode and a new conversion will be initiated when a previous
           conversion completes

Bit 0 – LEFTADJ Left-Adjusted Result
The high byte of the 12-bit result will be present in the upper part of the result register. Writing this bit to
zero (default) will right-adjust the value in the RESULT register.
 Value      Description
 0          The ADC conversion result is right-adjusted in the RESULT register
 1          The ADC conversion result is left-adjusted in the RESULT register




© 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1617
                                                                SAM D5x/E5x Family Data Sheet
                                                                              ADC – Analog-to-Digital Converter

45.8.6         Reference Control

               Name:       REFCTRL
               Offset:     0x08
               Reset:      0x00
               Property:   PAC Write-Protection, Write-Synchronized


         Bit         7            6            5            4            3             2                 1            0
                 REFCOMP                                                                   REFSEL[3:0]
   Access          R/W                                                  R/W          R/W             R/W             R/W
    Reset            0                                                   0             0                 0            0


               Bit 7 – REFCOMP Reference Buffer Offset Compensation Enable
               The gain error can be reduced by enabling the reference buffer offset compensation. This will increase
               the start-up time of the reference.
                Value       Description
                0           Reference buffer offset compensation is disabled.
                1           Reference buffer offset compensation is enabled.

               Bits 3:0 – REFSEL[3:0] Reference Selection
               These bits select the reference for the ADC.
                Value      Name        Description
                0x0        INTREF internal bandgap reference, refer to the SUPC.VREF.SEL register for more
                                       details
                x01                    Reserved
                0x2        INTVCC0 1/2 VDDANA (only for VDDANA > 2.0v)
                0x3        INTVCC1 VDDANA
                0x4        AREFA       External reference
                0x5        AREFB       External reference
                0x6        AREFC       External reference (ADC1 only)
                other      -           Reserved




           © 2019 Microchip Technology Inc.                      Datasheet                               DS60001507E-page 1618
                                                                  SAM D5x/E5x Family Data Sheet
                                                                              ADC – Analog-to-Digital Converter

45.8.7         Average Control

               Name:       AVGCTRL
               Offset:     0x0A
               Reset:      0x00
               Property:   PAC Write-Protection, Write-Synchronized


         Bit         7            6               5          4           3            2            1               0
                                              ADJRES[2:0]                             SAMPLENUM[3:0]
   Access                        R/W             R/W        R/W         R/W          R/W          R/W          R/W
    Reset                         0               0          0           0            0            0               0


               Bits 6:4 – ADJRES[2:0] Adjusting Result / Division Coefficient
               These bits define the division coefficient in 2^n steps.

               Bits 3:0 – SAMPLENUM[3:0] Number of Samples to be Collected
               These bits define how many samples are added together. The result will be available in the Result
               register (RESULT). Note: if the result width increases, CTRLB.RESSEL must be changed.
                Value      Description
                0x0        1 sample
                0x1        2 samples
                0x2        4 samples
                0x3        8 samples
                0x4        16 samples
                0x5        32 samples
                0x6        64 samples
                0x7        128 samples
                0x8        256 samples
                0x9        512 samples
                0xA        1024 samples
                0xB -      Reserved
                0xF




           © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1619
                                                                 SAM D5x/E5x Family Data Sheet
                                                                               ADC – Analog-to-Digital Converter

45.8.8         Sampling Time Control

               Name:       SAMPCTRL
               Offset:     0x0B
               Reset:      0x00
               Property:   PAC Write-Protection, Write-Synchronized


         Bit         7            6            5            4            3                  2      1            0
                 OFFCOMP                                                     SAMPLEN[5:0]
   Access          R/W                        R/W          R/W          R/W            R/W        R/W          R/W
    Reset            0                         0            0            0                  0      0            0


               Bit 7 – OFFCOMP Comparator Offset Compensation Enable
               Setting this bit enables the offset compensation for each sampling period to ensure low offset and
               immunity to temperature or voltage drift. This compensation increases the sampling time by three clock
               cycles that results in a fixed sampling duration of 4 CLK_ADC cycles.
               This bit must be set to zero to validate the SAMPLEN value. It’s not possible to use OFFCOMP=1 and
               SAMPLEN>0.

               Bits 5:0 – SAMPLEN[5:0] Sampling Time Length
               These bits control the ADC sampling time in number of CLK_ADC cycles, depending of the prescaler
               value, thus controlling the ADC input impedance. Sampling time is set according to the equation:
               Sampling time = SAMPLEN+1 ⋅ CLKADC




           © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1620
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                     ADC – Analog-to-Digital Converter

45.8.9         Window Monitor Lower Threshold

               Name:       WINLT
               Offset:     0x0C
               Reset:      0x0000
               Property:   PAC Write-Protection, Write-Synchronized


         Bit        15            14           13            12                 11          10        9           8
                                                                  WINLT[15:8]
   Access          R/W           R/W          R/W           R/W                R/W         R/W       R/W         R/W
    Reset            0            0             0            0                  0           0         0           0


         Bit         7            6             5            4                  3           2         1           0
                                                                  WINLT[7:0]
   Access          R/W           R/W          R/W           R/W                R/W         R/W       R/W         R/W
    Reset            0            0             0            0                  0           0         0           0


               Bits 15:0 – WINLT[15:0] Window Lower Threshold
               If the window monitor is enabled, these bits define the lower threshold value.




           © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1621
                                                               SAM D5x/E5x Family Data Sheet
                                                                                 ADC – Analog-to-Digital Converter

45.8.10 Window Monitor Upper Threshold

           Name:       WINUT
           Offset:     0x0E
           Reset:      0x0000
           Property:   PAC Write-Protection, Write-Synchronized


     Bit        15            14           13           12                 11           10        9           8
                                                             WINUT[15:8]
  Access       R/W           R/W          R/W           R/W                R/W         R/W       R/W         R/W
   Reset         0            0             0            0                  0           0         0           0


     Bit         7            6             5            4                  3           2         1           0
                                                              WINUT[7:0]
  Access       R/W           R/W          R/W           R/W                R/W         R/W       R/W         R/W
   Reset         0            0             0            0                  0           0         0           0


           Bits 15:0 – WINUT[15:0] Window Upper Threshold
           If the window monitor is enabled, these bits define the upper threshold value.




       © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1622
                                                                 SAM D5x/E5x Family Data Sheet
                                                                               ADC – Analog-to-Digital Converter

45.8.11 Gain Correction

            Name:        GAINCORR
            Offset:      0x10
            Reset:       0x0000
            Property:    PAC Write-Protection, Write-Synchronized


      Bit        15             14            13            12            11            10             9             8
                                                                                         GAINCORR[11:8]
  Access                                                                 R/W           R/W           R/W           R/W
   Reset                                                                  0              0             0             0


      Bit         7             6             5             4             3              2             1             0
                                                             GAINCORR[7:0]
  Access         R/W           R/W           R/W           R/W           R/W           R/W           R/W           R/W
   Reset          0             0             0             0             0              0             0             0


            Bits 11:0 – GAINCORR[11:0] Gain Correction Value
            If CTRLB.CORREN=1, these bits define how the ADC conversion result is compensated for gain error
            before being written to the result register. The gain correction is a fractional value, a 1-bit integer plus an
            11-bit fraction, and therefore ½ <= GAINCORR < 2. GAINCORR values range from 0.10000000000 to
            1.11111111111.




        © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 1623
                                                            SAM D5x/E5x Family Data Sheet
                                                                         ADC – Analog-to-Digital Converter

45.8.12 Offset Correction

            Name:       OFFSETCORR
            Offset:     0x12
            Reset:      0x0000
            Property:   PAC Write-Protection, Write-Synchronized


      Bit        15           14           13          12          11           10           9           8
                                                                               OFFSETCORR[11:8]
  Access                                                           R/W         R/W          R/W         R/W
   Reset                                                            0           0            0           0


      Bit        7             6            5          4            3           2            1           0
                                                      OFFSETCORR[7:0]
  Access        R/W          R/W           R/W        R/W          R/W         R/W          R/W         R/W
   Reset         0             0            0          0            0           0            0           0


            Bits 11:0 – OFFSETCORR[11:0] Offset Correction Value
            If CTRLB.CORREN=1, these bits define how the ADC conversion result is compensated for offset error
            before being written to the Result register. This OFFSETCORR value is in two’s complement format.




        © 2019 Microchip Technology Inc.                    Datasheet                       DS60001507E-page 1624
                                                                SAM D5x/E5x Family Data Sheet
                                                                              ADC – Analog-to-Digital Converter

45.8.13 Software Trigger

            Name:        SWTRIG
            Offset:      0x14
            Reset:       0x00
            Property:    PAC Write-Protection, Write-Synchronized


      Bit         7             6             5             4             3              2             1             0
                                                                                                    START         FLUSH
  Access                                                                                              W             RW
   Reset                                                                                               0             0


            Bit 1 – START Start ADC Conversion
            Writing a '1' to this bit will start a conversion or sequence. The bit is cleared by hardware when the
            conversion has started. Writing a '1' to this bit when it is already set has no effect.
            Writing a '0' to this bit has no effect.

            Bit 0 – FLUSH ADC Conversion Flush
            Writing a '1' to this bit will flush the ADC pipeline. A flush will restart the ADC clock on the next peripheral
            clock edge, and all conversions in progress will be aborted and lost. This bit will be cleared after the ADC
            has been flushed.
            After the flush, the ADC will resume where it left off; i.e., if a conversion was pending, the ADC will start a
            new conversion.
            Writing a '0' to this bit has no effect.




        © 2019 Microchip Technology Inc.                          Datasheet                           DS60001507E-page 1625
                                                                SAM D5x/E5x Family Data Sheet
                                                                              ADC – Analog-to-Digital Converter

45.8.14 Interrupt Enable Clear

            Name:        INTENCLR
            Offset:      0x2C
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.

      Bit         7             6             5             4             3             2             1               0
                                                                                    WINMON       OVERRUN        RESRDY
  Access                                                                              R/W           R/W           R/W
   Reset                                                                                0             0               0


            Bit 2 – WINMON Window Monitor Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Window Monitor Interrupt Enable bit, which disables the corresponding
            interrupt request.
             Value        Description
             0            The window monitor interrupt is disabled.
             1            The window monitor interrupt is enabled, and an interrupt request will be generated when the
                          Window Monitor interrupt flag is set.

            Bit 1 – OVERRUN Overrun Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Overrun Interrupt Enable bit, which disables the corresponding
            interrupt request.
             Value        Description
             0            The Overrun interrupt is disabled.
             1            The Overrun interrupt is enabled, and an interrupt request will be generated when the
                          Overrun interrupt flag is set.

            Bit 0 – RESRDY Result Ready Interrupt Disable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will clear the Result Ready Interrupt Enable bit, which disables the corresponding
            interrupt request.
             Value        Description
             0            The Result Ready interrupt is disabled.
             1            The Result Ready interrupt is enabled, and an interrupt request will be generated when the
                          Result Ready interrupt flag is set.




        © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1626
                                                                 SAM D5x/E5x Family Data Sheet
                                                                               ADC – Analog-to-Digital Converter

45.8.15 Interrupt Enable Set

            Name:        INTENSET
            Offset:      0x2D
            Reset:       0x00
            Property:    PAC Write-Protection

            This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
            in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.

      Bit         7             6              5             4             3             2             1            0
                                                                                      WINMON       OVERRUN       RESRDY
  Access                                                                                R/W           R/W          R/W
   Reset                                                                                 0             0            0


            Bit 2 – WINMON Window Monitor Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Window Monitor Interrupt bit, which enables the Window Monitor
            interrupt.
             Value        Description
             0            The Window Monitor interrupt is disabled.
             1            The Window Monitor interrupt is enabled.

            Bit 1 – OVERRUN Overrun Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Overrun Interrupt bit, which enables the Overrun interrupt.
            Value         Description
            0             The Overrun interrupt is disabled.
            1             The Overrun interrupt is enabled.

            Bit 0 – RESRDY Result Ready Interrupt Enable
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit will set the Result Ready Interrupt bit, which enables the Result Ready interrupt.
            Value         Description
            0             The Result Ready interrupt is disabled.
            1             The Result Ready interrupt is enabled.




        © 2019 Microchip Technology Inc.                          Datasheet                            DS60001507E-page 1627
                                                              SAM D5x/E5x Family Data Sheet
                                                                            ADC – Analog-to-Digital Converter

45.8.16 Interrupt Flag Status and Clear

            Name:       INTFLAG
            Offset:     0x2E
            Reset:      0x00
            Property:   –


      Bit         7            6             5            4             3            2             1            0
                                                                                  WINMON      OVERRUN        RESRDY
  Access                                                                            R/W          R/W           R/W
    Reset                                                                            0             0            0


            Bit 2 – WINMON Window Monitor Interrupt Flag
            This flag is cleared by writing a '1' to the flag or by reading the RESULT register.
            This flag is set on the next GCLK_ADC cycle after a match with the window monitor condition, and an
            interrupt request will be generated if INTENCLR/SET.WINMON is '1'.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Window Monitor interrupt flag.

            Bit 1 – OVERRUN Overrun Interrupt Flag
            This flag is cleared by writing a '1' to the flag.
            This flag is set if RESULT is written before the previous value has been read by CPU, and an interrupt
            request will be generated if INTENCLR/SET.OVERRUN=1.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Overrun interrupt flag.

            Bit 0 – RESRDY Result Ready Interrupt Flag
            This flag is cleared by writing a '1' to the flag or by reading the RESULT register.
            This flag is set when the conversion result is available, and an interrupt will be generated if INTENCLR/
            SET.RESRDY=1.
            Writing a '0' to this bit has no effect.
            Writing a '1' to this bit clears the Result Ready interrupt flag.




        © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1628
                                                               SAM D5x/E5x Family Data Sheet
                                                                             ADC – Analog-to-Digital Converter

45.8.17 STATUS

           Name:       STATUS
           Offset:     0x2F
           Reset:      0x00
           Property:   -


     Bit         7            6             5              4             3          2         1           0
                                                WCC[5:0]                                              ADCBUSY
  Access         R            R             R              R             R          R                     R
   Reset         0            0             0              0             0          0                     0


           Bits 7:2 – WCC[5:0] Window Comparator Counter
           These bits indicates the number of sample matching with the window comparator.
           Writing a zero to this bit will have no effect.
           Writing a one to this bit will have no effect.

           Bit 0 – ADCBUSY ADC Busy Status
           This bit is read one when the data acquisition in on going.
           Writing a zero to this bit will have no effect.
           Writing a one to this bit will have no effect.




       © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1629
                                                            SAM D5x/E5x Family Data Sheet
                                                                          ADC – Analog-to-Digital Converter

45.8.18 Synchronization Busy

           Name:       SYNCBUSY
           Offset:     0x30
           Reset:      0x00000000
           Property:   -


     Bit        31           30             29         28           27           26           25             24
              RBSSW
  Access        R
   Reset        0


     Bit        23           22             21         20           19           18           17             16


  Access
   Reset


     Bit        15           14             13         12           11           10           9              8
                                                                  SWTRIG     OFFSETCORR   GAINCORR       WINUT
  Access                                                            R            R            R              R
   Reset                                                            0             0           0              0


     Bit        7             6              5         4            3             2           1              0
              WINLT      SAMPCTRL         AVGCTRL   REFCTRL       CTRLB       INPUTCTRL    ENABLE        SWRST
  Access        R             R             R          R            R            R            R              R
   Reset        0             0              0         0            0             0           0              0


           Bit 31 – RBSSW Reset BootStrap Switch Synchronization Busy

           Bit 11 – SWTRIG Software Trigger Synchronization Busy
           This bit is cleared when the synchronization of SWTRIG register between the clock domains is complete.
           This bit is set when the synchronization of SWTRIG register between clock domains is started.
           Note: For the slave ADC, this bit is always read zero when the SLAVEEN bit is set (CTRLA.SLAVEEN=
           1).

           Bit 10 – OFFSETCORR Offset Correction Synchronization Busy
           This bit is cleared when the synchronization of OFFSETCORR register between the clock domains is
           complete.
           This bit is set when the synchronization of OFFSETCORR register between clock domains is started.

           Bit 9 – GAINCORR Gain Correction Synchronization Busy
           This bit is cleared when the synchronization of GAINCORR register between the clock domains is
           complete.
           This bit is set when the synchronization of GAINCORR register between clock domains is started.

           Bit 8 – WINUT Window Monitor Upper Threshold Synchronization Busy
           This bit is cleared when the synchronization of WINUT register between the clock domains is complete.
           This bit is set when the synchronization of WINUT register between clock domains is started.




       © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1630
                                                SAM D5x/E5x Family Data Sheet
                                                              ADC – Analog-to-Digital Converter

Bit 7 – WINLT Window Monitor Lower Threshold Synchronization Busy
This bit is cleared when the synchronization of WINLT register between the clock domains is complete.
This bit is set when the synchronization of WINLT register between clock domains is started.

Bit 6 – SAMPCTRL Sampling Time Control Synchronization Busy
This bit is cleared when the synchronization of SAMPCTRL register between the clock domains is
complete.
This bit is set when the synchronization of SAMPCTRL register between clock domains is started.

Bit 5 – AVGCTRL Average Control Synchronization Busy
This bit is cleared when the synchronization of AVGCTRL register between the clock domains is
complete.
This bit is set when the synchronization of AVGCTRL register between clock domains is started.

Bit 4 – REFCTRL Reference Control Synchronization Busy
This bit is cleared when the synchronization of REFCTRL register between the clock domains is
complete.
This bit is set when the synchronization of REFCTRL register between clock domains is started.

Bit 3 – CTRLB Control B Synchronization Busy
This bit is cleared when the synchronization of CTRLB register between the clock domains is complete.
This bit is set when the synchronization of CTRLB register between clock domains is started.

Bit 2 – INPUTCTRL Input Control Synchronization Busy
This bit is cleared when the synchronization of INPUTCTRL register between the clock domains is
complete.
This bit is set when the synchronization of INPUTCTRL register between clock domains is started.

Bit 1 – ENABLE ENABLE Synchronization Busy
This bit is cleared when the synchronization of ENABLE register between the clock domains is complete.
This bit is set when the synchronization of ENABLE register between clock domains is started.
Note: For the slave ADC, this bit is always read zero when the SLAVEEN bit is set (CTRLA.SLAVEEN=
1).

Bit 0 – SWRST SWRST Synchronization Busy
This bit is cleared when the synchronization of SWRST register between the clock domains is complete.
This bit is set when the synchronization of SWRST register between clock domains is started




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1631
                                                               SAM D5x/E5x Family Data Sheet
                                                                                 ADC – Analog-to-Digital Converter

45.8.19 DSEQDATA

           Name:       DSEQDATA
           Offset:     0x34
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31            30           29            28                 27          26       25            24
                                                              DATA[31:24]
  Access        W             W            W             W                  W           W         W            W
   Reset         0            0             0            0                  0           0         0            0


     Bit        23            22           21            20                 19          18       17            16
                                                              DATA[23:16]
  Access        W             W            W             W                  W           W         W            W
   Reset         0            0             0            0                  0           0         0            0


     Bit        15            14           13            12                 11          10        9            8
                                                              DATA[15:8]
  Access        W             W            W             W                  W           W         W            W
   Reset         0            0             0            0                  0           0         0            0


     Bit         7            6             5            4                  3           2         1            0
                                                               DATA[7:0]
  Access        W             W            W             W                  W           W         W            W
   Reset         0            0             0            0                  0           0         0            0


           Bits 31:0 – DATA[31:0] DMA Sequential Data
           This register stores data written by the DMA and re-directed to the first enabled ADC registers in the
           DSEQSTAT register.




       © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1632
                                                             SAM D5x/E5x Family Data Sheet
                                                                          ADC – Analog-to-Digital Converter

45.8.20 DSEQCTRL

           Name:        DSEQCTRL
           Offset:      0x38
           Reset:       0x00000000
           Property:    PAC Write-Protection


     Bit        31           30            29          28           27            26       25           24
            AUTOSTART
  Access       R/W
   Reset         0


     Bit        23           22            21          20           19            18       17           16


  Access
   Reset


     Bit        15           14            13          12           11            10           9        8
                                                                                                   OFFSETCORR
  Access                                                                                               R/W
   Reset                                                                                                0


     Bit         7            6             5           4            3             2           1        0
            GAINCORR       WINUT          WINLT    SAMPCTRL      AVGCTRL        REFCTRL   CTRLB     INPUTCTRL
  Access       R/W           R/W          R/W          R/W          R/W           R/W      R/W         R/W
   Reset         0            0             0           0            0             0           0        0


           Bit 31 – AUTOSTART ADC Auto-Start Conversion
           Value      Description
           0          ADC conversion starts when a DMA sequence is complete and a start software or event
                      trigger is received.
           1          ADC conversion automatically starts when a DMA sequence is complete. This setting is
                      ignored if the convertion start by event is enabled (EVCTRL.STARTEI=1).

           Bit 8 – OFFSETCORR Offset Correction
           Value      Description
           0          DMA update of the Offset Correction register is disabled.
           1          DMA update of the Offset Correction register is enabled.

           Bit 7 – GAINCORR Gain Correction
           Value      Description
           0          DMA update of the Gain Correction register is disabled.
           1          DMA update of the Gain Correction register is enabled.

           Bit 6 – WINUT Window Monitor Upper Threshold
           Value      Description
           0          DMA update of the Window Monitor Upper Threshold register is disabled.
           1          DMA update of the Window Monitor Upper Threshold register is enabled.




       © 2019 Microchip Technology Inc.                      Datasheet                     DS60001507E-page 1633
                                                 SAM D5x/E5x Family Data Sheet
                                                               ADC – Analog-to-Digital Converter

Bit 5 – WINLT Window Monitor Lower Threshold
Value      Description
0          DMA update of the Window Monitor Lower Threshold register is disabled.
1          DMA update of the Window Monitor Lower Threshold register is enabled.

Bit 4 – SAMPCTRL Sampling Time Control
Value      Description
0          DMA update of the Sampling Time Control register is disabled.
1          DMA update of the Sampling Time Control register is enabled.

Bit 3 – AVGCTRL Average Control
Value      Description
0          DMA update of the Average Control register is disabled.
1          DMA update of the Average Control register is enabled.

Bit 2 – REFCTRL Reference Control
Value      Description
0          DMA update of the Reference Control register is disabled.
1          DMA update of the Reference Control register is enabled.

Bit 1 – CTRLB Control B
Value      Description
0          DMA update of the Control B register is disabled.
1          DMA update of the Control B register is enabled.

Bit 0 – INPUTCTRL Input Control
Value      Description
0           DMA update of the Input Control register is disabled.
1           DMA update of the Input Control register is enabled.




© 2019 Microchip Technology Inc.                   Datasheet                    DS60001507E-page 1634
                                                            SAM D5x/E5x Family Data Sheet
                                                                         ADC – Analog-to-Digital Converter

45.8.21 DSEQSTAT

           Name:       DSEQSTAT
           Offset:     0x3C
           Reset:      0x00000000
           Property:   -


     Bit        31           30            29          28           27           26            25           24
               BUSY
  Access        R
   Reset         0


     Bit        23           22            21          20           19           18            17           16


  Access
   Reset


     Bit        15           14            13          12           11           10             9           8
                                                                                                       OFFSETCORR
  Access                                                                                                    R
   Reset                                                                                                    0


     Bit         7            6             5           4            3            2             1           0
            GAINCORR       WINUT          WINLT    SAMPCTRL      AVGCTRL      REFCTRL         CTRLB     INPUTCTRL
  Access        R             R            R           R            R             R            R            R
   Reset         0            0             0           0            0            0             0           0


           Bit 31 – BUSY DMA Sequencing Busy
           The bit is set when the DMA sequencing is enabled or restarted.
           The bit is cleared when the DMA sequencing is disabled.

           Bit 8 – OFFSETCORR Offset Correction
           Value      Description
           0          DMA update of the Offset Correction register is complete or disabled.
           1          DMA update of the Offset Correction register is enabled.

           Bit 7 – GAINCORR Gain Correction
           Value      Description
           0          DMA update of the Gain Correction register is complete or disabled.
           1          DMA update of the Gain Correction register is enabled.

           Bit 6 – WINUT Window Monitor Upper Threshold
           Value      Description
           0          DMA update of the Window Monitor Upper Threshold register is complete or disabled.
           1          DMA update of the Window Monitor Upper Threshold register is enabled.

           Bit 5 – WINLT Window Monitor Lower Threshold
           Value      Description
           0          DMA update of the Window Monitor Lower Threshold register is complete or disabled.




       © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1635
                                                 SAM D5x/E5x Family Data Sheet
                                                              ADC – Analog-to-Digital Converter

 Value        Description
 1            DMA update of the Window Monitor Lower Threshold register is enabled.

Bit 4 – SAMPCTRL Sampling Time Control
Value      Description
0          DMA update of the Sampling Time Control register is complete or disabled.
1          DMA update of the Sampling Time Control register is enabled.

Bit 3 – AVGCTRL Average Control
Value      Description
0          DMA update of the Average Control register is complete or disabled.
1          DMA update of the Average Control register is enabled.

Bit 2 – REFCTRL Reference Control
Value      Description
0          DMA update of the Reference Control register is complete or disabled.
1          DMA update of the Reference Control register is enabled.

Bit 1 – CTRLB Control B
Value      Description
0          DMA update of the Control B register is complete or disabled.
1          DMA update of the Control B register is enabled.

Bit 0 – INPUTCTRL Input Control
Value      Description
0           DMA update of the Input Control register is complete or disabled.
1           DMA update of the Input Control register is enabled.




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1636
                                                                  SAM D5x/E5x Family Data Sheet
                                                                                   ADC – Analog-to-Digital Converter

45.8.22 Result

           Name:        RESULT
           Offset:      0x40
           Reset:       0x0000
           Property:    -


     Bit         15            14            13            12                 11          10          9             8
                                                                RESULT[15:8]
  Access         R             R             R             R                   R          R           R             R
   Reset         0             0             0              0                  0          0           0             0


     Bit         7             6             5              4                  3          2           1             0
                                                                RESULT[7:0]
  Access         R             R             R             R                   R          R           R             R
   Reset         0             0             0              0                  0          0           0             0


           Bits 15:0 – RESULT[15:0] Result Conversion Value
           These bits will hold up to a 16-bit ADC conversion result, depending on the configuration.
           In single conversion mode without averaging, the ADC conversion will produce a 12-bit result, which can
           be left- or right-shifted, depending on the setting of CTRLB.LEFTADJ.
           If the result is left-adjusted (CTRLB.LEFTADJ), the high byte of the result will be in bit position [15:8],
           while the remaining 4 bits of the result will be placed in bit locations [7:4]. This can be used only if an 8-bit
           result is needed; i.e., one can read only the high byte of the entire 16-bit register.
           If the result is not left-adjusted (CTRLB.LEFTADJ) and no oversampling is used, the result will be
           available in bit locations [11:0], and the result is then 12 bits long. If oversampling is used, the result will
           be located in bit locations [15:0], depending on the settings of the Average Control register.




       © 2019 Microchip Technology Inc.                             Datasheet                         DS60001507E-page 1637
                                                               SAM D5x/E5x Family Data Sheet
                                                                                ADC – Analog-to-Digital Converter

45.8.23 RESS

           Name:       RESS
           Offset:     0x44
           Reset:      0x0000
           Property:   -


     Bit        15            14           13            12                11          10        9           8
                                                              RESS[15:8]
  Access         R            R            R             R                 R           R         R           R
   Reset         0            0             0            0                 0           0         0           0


     Bit         7            6             5            4                 3           2         1           0
                                                              RESS[7:0]
  Access         R            R            R             R                 R           R         R           R
   Reset         0            0             0            0                 0           0         0           0


           Bits 15:0 – RESS[15:0] Last ADC Conversion Result
           These bits will hold up the last ADC conversion result.




       © 2019 Microchip Technology Inc.                          Datasheet                      DS60001507E-page 1638
                                                                SAM D5x/E5x Family Data Sheet
                                                                            ADC – Analog-to-Digital Converter

45.8.24 Calibration

            Name:       CALIB
            Offset:     0x48
            Reset:      0x0000
            Property:   PAC Write-Protection, Enable-Protected


      Bit        15           14               13         12          11           10          9            8
                                                                                        BIASREFBUF[2:0]
  Access                                                                          R/W         R/W          R/W
   Reset                                                                           0           0            0


      Bit        7             6                5          4          3            2           1            0
                                           BIASR2R[2:0]                                  BIASCOMP[2:0]
  Access                     R/W               R/W        R/W                     R/W         R/W          R/W
   Reset                       0                0          0                       0           0            0


            Bits 10:8 – BIASREFBUF[2:0] Bias Reference Buffer Scaling
            This value from production test must be loaded from the NVM software calibration row into the CALIB
            register by software to achieve the specified accuracy. Refer to NVM Software Calibration Area Mapping
            for further details.
            The value must be copied only, and must not be changed.

            Bits 6:4 – BIASR2R[2:0] Bias R2R ampli Scaling
            This value from production test must be loaded from the NVM software calibration row into the CALIB
            register by software to achieve the specified accuracy. Refer to NVM Software Calibration Area Mapping
            for further details.
            The value must be copied only, and must not be changed

            Bits 2:0 – BIASCOMP[2:0] Bias Comparator Scaling
            This value from production test must be loaded from the NVM software calibration row into the CALIB
            register by software to achieve the specified accuracy. Refer to NVM Software Calibration Area Mapping
            for further details.
            The value must be copied only, and must not be changed




        © 2019 Microchip Technology Inc.                        Datasheet                      DS60001507E-page 1639
