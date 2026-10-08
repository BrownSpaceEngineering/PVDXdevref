# Atmel-42415-WIRELESS-AT86RF215_Datasheet

*Source: `Atmel-42415-WIRELESS-AT86RF215_Datasheet.pdf` (235 pages) — converted from PDF*


<!-- page 1 -->

                        Atmel AT86RF215 Device Family

                      Sub-1GHz/2.4GHz Transceiver and I/Q Radio for
                                          IEEE Std 802.15.4TM-2015
                                         IEEE Std 802.15.4gTM-2012
                                                 ETSI TS 102 887-1

                         AT86RF215 / AT86RF215IQ / AT86RF215M

                                                                             DATASHEET

Features AT86RF215

 Fully integrated radio transceiver covering 389.5-510MHz / 779-1020MHz / 2400-
   2483.5MHz including:
        European band:             863-870MHz / 870-876MHz / 915-921MHz
        Chinese band:              470-510MHz / 779-787MHz
        North American band:       902-928MHz
        Korean band:               917-923.5MHz
        Japanese band:             920-928MHz
        World-wide ISM band:       2400-2483.5MHz
 I/Q data interface:
      One TX and two RX serial low voltage differential signal (LVDS) interfaces
      13-bit I/Q data interface with a sampling frequency of up to 4MHz
 Transceiver Control interface: SPI (serial peripheral interface)
 Supported PHYs (*proprietary)
      MR-FSK
          Symbol rates: 50, 100, 150, 200, 300*, 400ksymbol/s
          Rate 1/2-FEC: RSC and NRNSC, with and without interleaving
          Order: 2-level, 4-level
      MR-OFDM
          Option 1: 100, 200, 400, 800, 1200*, 1600*, 2400*kb/s
          Option 2: 50, 100, 200, 400, 600, 800, 1200*kb/s
          Option 3: 50, 100, 200, 300, 400, 600kb/s
          Option 4: 50, 100, 150, 200, 300kb/s
      MR-O-QPSK
          100kchip/s with 6.25, 12.5, 25, 50kb/s data rate
          200kchip/s with 12.5, 25*, 50*, 100*kb/s data rate
          1000kchip/s with 31.25, 125, 250, 500kb/s data rate
          2000kchip/s with 31.25, 125, 250, 500, 1000*kb/s data rate
      O-QPSK
          1000kchip/s with 250kb/s and 500*kb/s data rate
          2000kchip/s with 250kb/s and 1000*kb/s data rate
 Bi-directional differential RF signal ports for:
      Band I: 433/470/780/863/868/915/917/920MHz
      Band II: 2450MHz



                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 2 -->

 Simultaneous operation of sub-1GHz and 2.4GHz transceiver
 Separate 2kbytes RX and TX frame buffer
 IEEE MAC support
        Frame filter (IEEE Std 802.15.4-2006)
        FCS handling
        Automatic acknowledgement (IEEE Std 802.15.4-2006)
        CCA with automatic transmit
 Industry leading link budget
      Programmable TX output power up to +14.5dBm@900MHz band
      Noise figure below 5dB for sub-1GHz and 2.4GHz transceiver
      Receiver sensitivity down to -123dBm at 6.25kb/s MR-O-QPSK
 Radio transceiver features
      Integrated TX/RX switch, LNA, PLL loop filter and RF frontend control
      Fast settling PLL supporting frequency hopping
      Automatic filter calibration
 Received signal strength indicator / energy detection
 True random number generator
 Optimized for low BOM cost and ease of production
 Low power supply voltage from 1.8V to 3.6V
 Internal voltage regulators and battery monitor
 Reduced power consumption (RPC) modes for MR-FSK and MR-OQPSK
 Low current consumption (incl. baseband processing / without I/Q interface)
        Deep sleep      30nA
        RX listen       6..28mA (RPC mode dependent)
        RX active       28mA
        TX              62mA @14dBm output power
 Industrial temperature range from –40°C to +85°C
 48-pin low-profile lead-free plastic QFN package




                                         Atmel AT86RF215 - DATASHEET                      2
                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 3 -->

1.      Description
        The AT86RF215 is a multi-band radio transceiver for various sub-1GHz bands and the 2.4GHz band specially designed
        for smart metering and applications implementing IEEE Std 802.15.4g™-2012 [3], ETSI TS 102 887-1 [5], IEEE Std
        802.15.4TM-2015 [7].
        The device is comprised of two independent transceivers, each with its own baseband and I/Q data interface. The
        AT86RF215 incorporates two transceivers and two baseband cores forming two independent radio systems. The
        transceivers are highly integrated minimizing the number of external components required on the printed circuit board
        (PCB). The supply voltage ranges from 1.8V to 3.6V. A 26MHz temperature controlled oscillator (TCXO) or a crystal
        oscillator (XTAL) is used as a reference clock.
        The AT86RF215 allows simultaneous independent reception in the sub-1GHz and 2.4GHz bands. Each radio frequency
        (RF) port is accessed with balanced differential signal pairs. Optimal sensitivity and output power are achieved with 50Ω
        differential load. The device offers a high link budget with maximum TX output power of 14.5dBm@900MHz and
        sensitivity down to -123dBm@MR-OQPSK-6.25kb/s.
        The device is controlled via a fast serial peripheral interface (SPI). Dedicated MAC hardware, random number generator
        and on-board battery monitoring improve overall system efficiency and timing.
        The AT86RF215 can be operated with an external microcontroller (e.g. Atmel SAM4 Family) and/or an external
        baseband processor.


1.1     Device Family

1.1.1   Overview

        Table 1-1.   Device Family Overview

        Device                  Description
        AT86RF215                Dual band transceiver and I/Q radio
                                 Embedded baseband supporting MR-FSK, MR-OFDM, MR-O-QPSK, and O-QPSK
                                 Compliant to IEEE Std 802.15.4g™-2012 [3]; IEEE Std 802.15.4™-2011 [2]; ETSI TS 102 887-1
                                  [5], IEEE Std 802.15.4TM-2015 [7]
        AT86RF215IQ              I/Q radio (13-bit I/Q low voltage differential signal (LVDS) interface)
        AT86RF215M               Sub-1GHz Transceiver and I/Q radio
                                 Embedded baseband supporting MR-FSK, MR-OFDM, MR-O-QPSK, and O-QPSK
                                 Compliant to IEEE Std 802.15.4g™-2012 [3]; ETSI TS 102 887-1 [5]
        Note:    For operation of the AT86RF215M see "Basic Operation of AT86RF215M" on page 42.

1.1.2   Device Identification
        The device identifier can be read from the register RF_PN. The version number of the device can be read from the
        register RF_VN.

1.1.3   Register Description
1.1.3.1 RF_PN – Device Part Number
        The register contains the part number of the device.




                                                                                         Atmel AT86RF215 - DATASHEET                      3
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 4 -->

       Bit                 7           6          5          4         3       2            1             0
       (0x000D)                                                  PN                                                       RF_PN
       Read/Write          R           R          R          R         R       R            R            R

        Bit 7:0 – RF_PN.PN: Device Part Number
       The register contains the part number of the device.

       Table 1-2.     PN

       Sub-register            Value       Description
       PN                      0x34        AT86RF215
                               0x35        AT86RF215IQ
                               0x36        AT86RF215M

1.1.3.2 RF_VN – Device Version Number
       The register contains the version number of the device.
       Bit                     7            6            5       4         3         2             1             0
       (0x000E)                                                       VN                                                      RF_VN
       Read/Write              R            R            R       R         R        R              R             R
       Initial Value v.1       0            0            0       0         0         0             0             1
       Initial Value v.3       0            0            0       0         0         0             1             1


1.2    Block Diagram
       The device features two independent radio systems. It contains one sub-1GHz transceiver and one 2.4GHz transceiver.
       Each transceiver is paired with a baseband core optimized to demodulate signals commonly used in the associated
       band, thus providing complete RF-to-Baseband operation. The internal baseband cores support MR-FSK, O-QPSK/MR-
       O-QPSK and MR-OFDM modulation schemes. Alternatively users can route the I/Q data stream directly to an external
       processor for advanced signal processing using the 13-bit LVDS interface.
       The AT86RF215 block diagram is shown in Figure 1-1.




                                                                                   Atmel AT86RF215 - DATASHEET                        4
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 5 -->

Figure 1-1. AT86RF215 Block Diagram


                AT86RF215

                 2.4GHz Radio (RF24)                                                  Random Number Generator
                                                                                                                       Battery Monitor              DVDD (1.8V)
                                                                                                                        (BATMON)              Digital Voltage Regulator
                                      Automatic Gain Control (AGC)


                 Receiver Analog Frontend                                                       Receiver Digital                         Baseband Core1
                                                                                                Frontend                                 (BBC1)

                                                                            Sigma-Delta                                                                            RX
                      Low                                  Band                                        Filter,     I_DATA[13:0]
                                                                               Analog                                                                             Frame
                      Noise                                 Pass                                       Down-       Q_DATA[13:0]
                                            Mixer                              Digital                                                                            Buffer
                      Amplifier                             Filter                                    Sampling
                                                                             Converter
                      (LNA)                                (BPF)                                     (RX_DFE)
                                                                             (SDADC)

                                                                                                                                             MR-FSK



                                                                          AVDD1 (1.8V)
    RFN/RFP                            2.4GHz Frequency                                              Analog
                                                                     Analog Voltage Regulator
    2.4GHz                             Synthesizer (PLL)                                            Calibration
                                                                      (2.4GHz Transceiver)                                                   MR-OFDM




                 Transmitter Analog Frontend                                                    Transmitter
                                                                                                                                            MR-O-QPSK/
                                                                                                Digital Frontend                             O-QPSK
                                                                                                                                                                    TX
                                                            Low               Digital                 Filter,      I_DATA[13:0]                                   Frame
                           Power
                                                           Pass               Analog                   Up-         Q_DATA[13:0]                                   Buffer
                          Amplifier         Mixer
                                                           Filter            Converter               Sampling
                             (PA)
                                                           (LPF)              (DAC)                 (TX_DFE)

                                                                                                                                                                           RXD24
                                                                                                                                                   Serial                  RXCLK
                                                                                                                                                 I/Q Data                  RXD09
                                                                                                                                                 Interface                 TXD
                                                                                                                                                  (LVDS)                   TXCLK


                                                                                                                                                                           RSTN
                 Sub-1GHz Radio (RF09)                                                Random Number Generator                                                              IRQ

                                      Automatic Gain Control (AGC)                                                                                 Serial                  MISO
                                                                                                                                                Peripheral                 MOSI
                                                                                                                                                 Interface                 SELN
                 Receiver Analog Frontend                                                       Receiver Digital                                   (SPI)                   SCLK

                                                                                                Frontend
                                                                                                                                         Baseband Core0
                                                                            Sigma-Delta
                      Low                                  Band                                       Filter,      I_DATA[13:0]          (BBC0)
                                                                               Analog                                                                              RX
                      Noise                                 Pass                                      Down-        Q_DATA[13:0]
                                            Mixer                              Digital                                                                            Frame
                      Amplifier                             Filter                                   Sampling
                                                                             Converter                                                                            Buffer
                      (LNA)                                (BPF)                                    (RX_DFE)
                                                                             (SDADC)

                                                                                                                                             MR-FSK


                                                                          AVDD0 (1.8V)
   RFN/RFP                            Sub-1GHz Frequency
                                                                     Analog Voltage Regulator
                                                                                                     Analog
                                       Synthesizer (PLL)                                            Calibration
   Sub-1GHz                                                          (Sub-1GHz Transceiver)
                                                                                                                                             MR-OFDM




                 Transmitter Analog Frontend                                                    Transmitter
                                                                                                Digital Frontend                            MR-O-QPSK/
                                                                                                                                             O-QPSK

                                                            Low               Digital                 Filter,      I_DATA[13:0]
                           Power                                                                                                                                    TX
                                                           Pass               Analog                   Up-         Q_DATA[13:0]
                          Amplifier         Mixer                                                                                                                 Frame
                                                           Filter            Converter               Sampling
                             (PA)                                                                                                                                 Buffer
                                                           (LPF)              (DAC)                 (TX_DFE)




                                                                                                                   XOSC / Clock PLL


                                                                                                                      XTAL/TCXO




       Notes:    1.     Baseband Core0/1 are not available at AT86RF215IQ
                 2.     2.4GHz Radio (RF24) and Baseband Core1 (BBC1) are not available at AT86RF215M




                                                                                                                            Atmel AT86RF215 - DATASHEET                            5
                                                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 6 -->

1.3   Control Logic and Naming Conventions
      Both radio and baseband cores have separate register blocks. The sub-1GHz radio register names are prefixed by
      “RF09_”. The 2.4GHz radio transceiver register names are prefixed by “RF24_”. The register descriptions, including
      sub-register descriptions, for both radios and their respective basebands are identical. In rare cases where a register is
      only valid for one specific radio (or baseband), the register for the other radio (or baseband) is ignored.
      The baseband processor Core0 is connected to the sub-1GHz radio and Core1 is connected to the 2.4GHz radio.
      The baseband registers of Core0 are prefixed by “BBC0_”. The baseband register of Core1 are prefixed by “BBC1_”.
      The general reference for both core registers is prefixed by “BBCn_”. Both cores are identical and have separate
      register spaces.
      Common registers of the AT86RF215 which are not specific for the radio or baseband are prefixed by “RF_”.
      Note, the datasheet refers to the naming convention of IEEE Std 802.15.4g™-2012 [3] in regards to multi rate and multi
      regional frequency (MR) PHYs. The IEEE Std 802.15.4TM-2015 [7] names the PHYs SUN, i.e. smart metering utility
      network.




                                                                                   Atmel AT86RF215 - DATASHEET                      6
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 7 -->

2.    Pin-out Diagram and Description

2.1   Pin-out Diagram
      The pin-out of the AT86RF215 is shown in Figure 2-1.

      Figure 2-1. Pin-out




                             AVSS   AVDD1   EVDD   AVSS   MISO   MOSI    SELN   SCLK           DEVDD   DVSS   DVDD
                                                                                                                              PADDLE
                                                                                       IRQ                                    (AVSS)

                             48 47 46 45 44 43 42 41 40 39 38 37


      FEA24        1                                                                                                      36 RXDP24
      FEB24        2                                                                                                      35 RXDN24
       AVSS        3                                                                                                      34 RXCLKP
      RFP24        4                                                                                                      33 RXCLKN
      RFN24        5                                                                                                      32 DVSS
       AVSS        6
                                              AT86RF215                                                                   31 RXDP09
       AVSS        7                                                                                                      30 RXDN09
                                    48Pin (7x7)mm2, Pitch=0.5mm
      RFP09        8                                                                                                      29 DEVDD
      RFN09        9                                                                                                      28 TXDP
       AVSS 10                                                                                                            27 TXDN
      FEA09 11                                                                                                            26 TXCLKP
      FEB09 12                                                                                                            25 TXCLKN


                             13 14 15 16 17 18 19 20 21 22 23 24


                             RSTN   AVDD0   EVDD   AVSS   TCXO   XTAL2   AVSS   DVSS
                                                                                       DEVDD
                                                                                               CLKO    DVSS   DVSS




                                                                                                Atmel AT86RF215 - DATASHEET                      7
                                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 8 -->

Table 2-1.    Pin Description

# Pin        Name        Type     Description
1            FEA24       Output   RF frontend control; digital output for the 2.4GHz transceiver
2            FEB24       Output   RF frontend control; digital output for the 2.4GHz transceiver
3            AVSS        In/Out   Analog ground (RF)
4            RFP24       In/Out   Differential RF input/output 2.4GHz (positive)
5            RFN24       In/Out   Differential RF input/output 2.4GHz (negative)
6            AVSS        In/Out   Analog ground (RF)
7            AVSS        In/Out   Analog ground (RF)
8            RFP09       In/Out   Differential RF input/output for sub-1GHz transceiver (positive)
9            RFN09       In/Out   Differential RF input/output for sub-1GHz transceiver (negative)
10           AVSS        In/Out   Analog ground (RF)
11           FEA09       Output   RF frontend control; digital output for the sub-1GHz transceiver
12           FEB09       Output   RF frontend control; digital output for the sub-1GHz transceiver
13           RSTN        Input    Reset input (active low)
14           AVDD0       In/Out   Internal regulated analog 1.8V supply output voltage (internally generated) for
                                  analog circuitry of the sub-1GHz transceiver
15           EVDD        Input    External analog supply voltage (VDD); 3.0V typical
16           AVSS        In/out   Analog ground
17           TCXO        Input    TCXO or crystal oscillator (26MHz) input
18           XTAL2       Output   Crystal oscillator
19           AVSS        In/Out   Analog ground
20           DVSS        In/Out   Digital ground
21           DEVDD       Input    External digital supply voltage (VDD); 3.0V typical
22           CLKO        Output   Clock output
23           DVSS        In/Out   Digital ground
24           DVSS        In/Out   Digital ground
25           TXCLKN      Input    Differential TX I/Q clock interface input (negative)
26           TXCLKP      Input    Differential TX I/Q clock interface input (positive)
27           TXDN        Input    Differential TX I/Q data interface input (negative)
28           TXDP        Input    Differential TX I/Q data interface input (positive)
29           DEVDD       Input    External digital supply voltage (VDD); 3.0V typical
30           RXDN09      Output   Differential RX I/Q data interface output sub-1GHz transceiver (negative)
31           RXDP09      Output   Differential RX I/Q data interface output sub-1GHz transceiver (positive)
32           DVSS        In/Out   Digital ground
33           RXCLKN      Output   Differential RX I/Q clock interface output (negative)
34           RXCLKP      Output   Differential RX I/Q clock interface output (positive)
35           RXDN24      Output   Differential RX I/Q data interface output 2.4GHz transceiver (negative)
36           RXDP24      Output   Differential RX I/Q data interface output 2.4GHz transceiver (positive)
37           DVDD        In/Out   Internal regulated supply output voltage (internally generated) for digital circuitry
38           DVSS        In/Out   Digital ground



                                                                           Atmel AT86RF215 - DATASHEET                      8
                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 9 -->

        # Pin     Name          Type          Description
        39        DEVDD         Output        External digital supply voltage (VDD); 3.0V typical
        40        IRQ           Output        Interrupt output
        41        SCLK          Input         SPI interface clock input
        42        SELN          Input         SPI select input (active low)
        43        MOSI          Input         SPI data input
        44        MISO          Output        SPI data output
        45        AVSS          In/Out        Analog ground
        46        EVDD          Input         External analog supply voltage (VDD); 3.0V typical
        47        AVDD1         In/Out        Internal regulated analog 1.8V supply output voltage (internally generated) for
                                              analog circuitry for the 2.4GHz transceiver
        48        AVSS          In/Out        Analog ground




2.2     Pin Description

2.2.1   RFP09/RFN09, RFP24/RFN24
        The differential RF pins (RFP09/RFN09; RFP24/RFN24) provide common-mode rejection to suppress the switching
        noise of the internal and external digital signal processing blocks.
        A 50Ω differential load at the RF ports ensures high sensitivity and output power. A DC path between the RF pins is
        supported; a DC path to ground or supply voltage is not supported. When connecting an RF load providing a DC path to
        the power supply or ground, AC coupling is required.
        The pins RFP24/RFN24 of AT86RF215M are shortened to AVSS internally and may not be connected.

2.2.2   EVDD, DEVDD (VDD)
        EVDD is the external analog supply voltage. DEVDD is the external digital supply voltage. External decoupling
        capacitors must be placed close to these device pins. EVDD and DEVDD must be shorted at board level and should
        always have the same potential.

2.2.3   AVDD0, AVDD1
        AVDD0 and AVDD1 are internally generated/regulated analog supply voltages. External compensation capacitors must
        be placed close to these device pins. These supplies are activated, and de-activated, by the sleep-mode logic. Do not
        use these signals as references or power supplies. AVDD0 and AVDD1 must not be shorted. For further information
        about the analog supply voltages are described in section "Voltage Regulator" on page 75.
        An external compensation capacitor at the pin AVDD1 is not required for AT86RF215M, the pin can have no
        connections.

2.2.4   DVDD
        DVDD is an internally generated/regulated digital supply voltage. An external compensation capacitor must be placed
        close to this device pin. For further information about the digital supply voltage are described in section "Voltage
        Regulator" on page 75.

2.2.5   AVSS, DVSS
        AVSS is the analog ground; DVSS is the digital ground voltage. The analog and the digital grounds should be separated
        on the PCB and only connected at a single point on the PCB.


                                                                                      Atmel AT86RF215 - DATASHEET                     9
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 10 -->

2.2.6   MISO, MOSI, SCLK, SELN
        Pins MISO, MOSI, SCLK and SELN are SPI specific pins which provide register read/write access for device operation.
        For further information about the control interface see section "SPI Transceiver Control Interface" on page 16.

2.2.7   RXDN09/RXDP09, RXDN24/RXDP24, RXCLKP/RXCLKN, TXDP/TXDN, TXCLKP/TXCLKN
        Pins RXDN09/RXDP09, RXDN24/RXDP24, RXCLKP/RXCLKN, TXDP/TXDN and TXCLKP/TXCLKN are low voltage
        differential signal (LVDS) I/Q data interface pins. For further information see section "Serial I/Q Data Interface" on page
        22.
        The pins RXDN24/RXDP24 are not supported for AT86RF215M, the pins shall have no connections.

2.2.8   IRQ
        Pin IRQ is the interrupt pin from the transceiver to the microcontroller and is controlled by both radios and basebands.
        The interrupt source can be detected by reading the interrupt status registers using the device control interface (SPI).
        For further information about IRQ configuration see section "Interrupt Signalling" on page 19.

2.2.9   RSTN
        Pin RSTN is the active low reset pin. For further information see section "Reset Modes " on page 13.

2.2.10 FEA09/FEB09, FEA24/FEB24
        The digital output pins FEAnn and FEBnn can control an external RF analog frontend device, in general external LNA,
        PA. For each transceiver band two frontend control pins are specified. The pins are not differential. For further
        information see section "External Frontend Control" on page 70.
        The pins FEA24/FEB24 are not supported for AT86RF215M, the pins shall have no connections.

2.2.11 TCXO/XTAL2
        Pin TCXO (Temperature Controlled Crystal Oscillator) is the input pin of a 26MHz clock from a TCXO device. Pin
        XTAL2 must be grounded if operating the device with a TCXO.
        Alternatively, the device can be operated with a 26MHz Crystal (XTAL) which must be connected between pin TCXO
        and pin XTAL2. For further information see section "Crystal Oscillator and TCXO" on page 67.

2.2.12 CLKO
        Pin CLKO provides a clock output signal. An external microcontroller can use this clock signal as an input clock source.
        For further information about the clock output configuration see "Clock Output" on page 20.




                                                                                      Atmel AT86RF215 - DATASHEET                     10
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 11 -->

3.   Application Schematic
     A basic application schematic of the AT86RF215 is shown in Figure 3-1. The RF ports require a 50Ω differential load for
     best RF performance. The transceiver is operated with a 26MHz TCXO.

     Figure 3-1. Basic Application Schematic




                                                                                                                                                                                       SPI




                                                                                                                                                                                      Digital
                                                                                                                                           Cdec
                                                   C  dec
                                                                             Cdec                                                                                                     Control
                                         (not required for
                                          AT86RF215M)                                                                                          VDD
                                                                                VDD                                                                     Cdec    PADDLE
                                                                                                                                                                (AVSS)


                                                       48 47 46 45 44 43 42 41 40 39 38 37


          n.c. for AT86RF215M                          AVSS   AVDD1      EVDD     AVSS   MISO     MOSI        SELN   SCLK   IRQ        DEVDD   DVSS   DVDD
                                     1 FEA24                                                                                                             RXDP24 36
                                     2 FEB24                                                                                                             RXDN24 35
                                     3    AVSS                                                                                                           RXCLKP 34
                   2.4 GHz           4 RFP24                                                                                                             RXCLKN 33




                                                                                                                                                                                       I/Q Data Interface
                    Front-
                     end             5 RFN24                                                                                                             DVSS    32
                                     6    AVSS
                                                                             AT86RF215                                                                   RXDP09 31
                                     7    AVSS                                                            2                                              RXDN09 30
                                                              48Pin (7x7)mm , Pitch=0.5mm                                                                                     Cdec
                   Sub-
                  1GHz               8 RFP09                                                                                                             DEVDD 29
                  Front-
                   end
                                     9 RFN09                                                                                                             TXDP    28      VDD

                                    10    AVSS                                                                                                           TXDN    27
                                    11 FEA09                                                                                                             TXCLKP 26
                                    12 FEB09                                                                                                             TXCLKN 25

                                                       RSTN   AVDD0      EVDD     AVSS   TCXO     XTAL2       AVSS   DVSS
                                                                                                                            DEVDD
                                                                                                                                       CLKO    DVSS   DVSS

                                                       13 14 15 16 17 18 19 20 21 22 23 24

                                                                      Cdec
                                                                                VDD             VDDTCXO
                                                                                                                                    VDD                         RF

                                                                                Cdec     TCXO                                       Cdec                                              Digital
                                                                                                                                                                         CF
                                                                                                                                                                                      Control




     The external analog power supply EVDD, the external digital power supply DEVDD and the integrated voltage
     regulators outputs AVDD0, DVDD and AVDD1 must be decoupled by a capacitor (Cdec). All decoupling capacitors
     should be placed as close as possible to the pins and should have low-resistance and low-inductance connection to
     ground. EVDD and DEVDD must be shorted at PCB level and should always have the same potential (V DD).




                                                                                                                                               Atmel AT86RF215 - DATASHEET                                  11
                                                                                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 12 -->

A low-pass filter (CF, RF) should be placed close to pin CLKO to reduce the emission of CLKO signal harmonics.
This is not needed if pin CLKO is not used as a microcontroller clock source. In this case, clock output signal
should be disabled during device initialization, see register RF_CLKO.
The pins RFP24/RFN24 of the AT86RF215M are connected to AVSS and must not be connected. The pins
RXDP24/RXDN24 are not supported for the AT86RF215M and can be left opened.




                                                                       Atmel AT86RF215 - DATASHEET                     12
                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 13 -->

4.      Control and Data Interfaces

4.1     Reset Modes

4.1.1   Summary Reset Modes
         The AT86RF215 can be reset by the following conditions:
             Power-on reset or voltage drop, see section "Power-on Reset" below
             Chip Reset command, see section "Chip Reset" on page 14
             Chip Reset via pulse at pin RSTN, see section "Chip Reset" on page 14
             Transceiver Reset, see section "Transceiver Reset" on page 14
             State SLEEP, see section "State SLEEP" on page 34
             State DEEP_SLEEP, see section "State DEEP_SLEEP and Wake-up Procedure" on page 34
        The AT86RF215 registers can be classified into register groups for common chip functionality, for the I/Q data interface,
        for the sub-1GHz transceiver and for the 2.4GHz transceiver. Table 4-1 shows which register groups are reset by which
        reset source.

        Table 4-1.   AT86RF215 Reset Modes

        Reset Source                      Common Chip           I/Q Data Interface    Sub-1GHz                   2.4GHz
                                          Register              Register              Transceiver                Transceiver
                                                                                      Register                   Register
                                          RF_CFG,               RF_IQIFC0 and         RF09_* and                 RF24_* and
                                          RF_XOC,               RF_IQIFC1             BBC0_*                     BBC1_*
                                          RF_CLKO and
                                          RF_BMDVC
        Power-On Reset                    reset                 reset                 reset                      reset
        Chip Reset                        reset                 reset                 reset                      reset
        Sub-1GHz Transceiver Reset                                                    reset
        2.4GHz Transceiver Reset                                                                                 reset
        Sub-1GHz Transceiver SLEEP                                                    reset
        2.4GHz Transceiver SLEEP                                                                                 reset
        DEEP_SLEEP                                              reset                 reset                      reset



4.1.2   Power-on Reset
        A power-on reset is initiated if the supply voltage drops below the operating range of the voltage regulator (see section
        "Voltage Regulator" on page 75) and returns back to the supported range again. For further information about the
        operation range see section "Operating Range" on page 187.
        The power-on procedure is shown in Figure 4-1.




                                                                                     Atmel AT86RF215 - DATASHEET                     13
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 14 -->

        Figure 4-1. Power-on Procedure


        Event     VDD on



        State         Power-on                                   TRXOFF




        Block         XOSC, DVREG                                CLKO active



        IRQ                                                       WAKEUP


        Time
                                    tPOWERON



        When the external supply voltage (VDD) is initially supplied to the AT86RF215, the device enables the crystal oscillator
        (XOSC) and the internal 1.8V voltage regulator for the digital domain (DVREG). After tPOWERON the output clock signal is
        available at pin CLKO at default clock rate of 26MHz. During the power-on procedure, all registers are set to their
        default values. As soon as the state TRXOFF is reached, the SPI is enabled and it can be used to control the device. At
        the same time, the interrupt IRQS.WAKEUP at both transceivers is set to 1 and the pin IRQ is asserted high.

4.1.3   Chip Reset
        The Chip Reset procedure resets the entire device (i.e. both radios, sub-1GHz and 2.4GHz and both baseband cores),
        all registers are set to their default values.
        The Chip Reset is triggered by the pin RSTN or by writing the Chip Reset command. The Chip Reset is triggered by
        pulling the pin RSTN to low, keeping it low for tRST and to release it to high again; for further timing information see
        section "Power-on Reset Characteristics" on page 188. To trigger the Chip Reset via the Chip Reset command, the
        value 0x07 needs to be written to the sub-register RF_RST.CMD.
        After initiating the Chip Reset procedure, the device enters the internal state RESET. After the reset procedure is
        completed, the state RESET is left and the state TRXOFF is reached. The completion of the reset procedure is
        indicated by the interrupt IRQS.WAKEUP for both transceivers.
        For further information about state changes see section "State Machine" on page 33.

4.1.4   Transceiver Reset
        While the Chip Reset procedure resets the entire device (sub-1GHz/BBC0 and 2.4GHz/BBC1), the Transceiver Reset is
        used to reset only a single transceiver (RF09/BBC0 or RF24/BBC1). The Transceiver Reset is initiated by writing the
        command RESET to the register RFn_CMD of the corresponding transceiver. During the reset procedure the
        corresponding transceiver state machine is reset and the corresponding transceiver (RFn_*) and baseband registers
        (BBCn_*) are set to their default values. The common device registers (RF_*) are not reset.
        Once the reset procedure is completed, the state TRXOFF is reached and the interrupt IRQS.WAKEUP is issued for the
        corresponding transceiver.

4.1.5   Register Description
4.1.5.1 RF_RST – Chip Reset
        The register RF_RST allows resetting the entire device via an SPI command.




                                                                                      Atmel AT86RF215 - DATASHEET                     14
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 15 -->

Bit                   7      6          5            4        3          2            1             0
(0x0005)              –      –          –            –        –                     CMD                            RF_RST
Read/Write            R      R          R            R        R         RW          RW            RW
Initial Value         0      0          0            0        0          0            0             0

 Bit 2:0 – RF_RST.CMD: Chip Reset Command
Writing the value 0x7 to the sub-register CMD triggers the reset procedure of the entire device; the values 0x0 to 0x6
have no effect.

Table 4-2.      CMD

Sub-register          Name                    Value      Description
CMD                   RF_RESET                 0x7       CHIP RESET




                                                                             Atmel AT86RF215 - DATASHEET                     15
                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| CMD | RF_RESET | 0x7 | CHIP RESET |


<!-- page 16 -->

4.2     SPI Transceiver Control Interface

4.2.1   Introduction
        The control interface comprises an SPI slave and provides access to registers and frame buffers of the AT86RF215.
        Table 4-3 shows the SPI signals.

        Table 4-3.   SPI Signals

        SPI Signal           Direction      Description
        SCLK                 Input          SPI clock signal
        SELN                 Input          SPI select signal, active low
        MOSI                 Input          SPI data master output, slave input signal
        MISO                 Output         SPI data master input, slave output signal


        The SPI is byte-oriented with bi-directional communication between master and slave. Each byte is transferred with the
        MSB first. The SPI select signal SELN is active low. The number of clocks at SCLK must be a multiple of eight. The
        AT86RF215 SPI provides register and frame buffer access in a linear address space. The access mode is configured
        by the address in the COMMAND bytes.

4.2.2   SPI Protocol
        Each SPI sequence starts by setting SELN to low and finishes by releasing SELN to high. After setting SELN to low, the
        two COMMAND bytes are transferred from the SPI master via pin MOSI followed by SPI clock signals to read or to write
        data. The two COMMAND bytes define the SPI access mode (read or write access) and the 14-bit address (see Table
        4-4).

        Table 4-4.   SPI COMMAND Definition

         Bit[15]         Bit[14]         Bit[13:8]                          Bit[7:0]                              SPI Access Mode
         MODE[1]         MODE[0]         ADDRESS[13:8]                      ADDRESS[7:0]
         COMMAND[15:8]                                                      COMMAND[7:0]
         0               0               ADDRESS[13:8]                      ADDRESS[7:0]                          Read
         1               0               ADDRESS[13:8]                      ADDRESS[7:0]                          Write
         0               1               ADDRESS[13:8]                      ADDRESS[7:0]                          Reserved
         1               1               ADDRESS[13:8]                      ADDRESS[7:0]                          Reserved


        The SPI can be operated in single or block access mode. The single access mode (see section 4.2.4) is used to read or
        to write a single register value. The block access mode (see section 4.2.4) is used to read or to write a block of data
        with a variable number of data bytes.

4.2.3   Single Access Mode
        The single access mode is a three byte operation. First the two COMMAND bytes are transferred on MOSI. If MODE
        indicates a write access, then the third byte contains the value that is written to the selected address (see Figure 4-2). If
        MODE indicates a read access, then the content of the selected address is returned with the third byte on pin MISO
        (see Figure 4-3).




                                                                                         Atmel AT86RF215 - DATASHEET                     16
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 17 -->

        Figure 4-2. SPI Single Write Access


        SELN


        SCLK


        MOSI      MODE[1:0], ADDRESS[13:8]       ADDRESS[7:0]            VALUEADDRESS



        MISO




        Figure 4-3. SPI Single Read Access


        SELN


        SCLK


        MOSI      MODE[1:0], ADDRESS[13:8]       ADDRESS[7:0]



        MISO                                                             VALUEADDRESS




4.2.4   Block Access Mode
        The block access mode is entered when SELN remains low after the third byte of the single access mode. During block
        write access the fourth byte on MOSI is written to the next address (ADDRESS+1) and so on. The same procedure
        applies to the block read access, where the content of the next address (ADDRESS+1) is returned with the fourth byte
        on pin MISO. The block mode can access the whole address space (see Figure 4-4 and Figure 4-5).

Figure 4-4. SPI Block Write Access


SELN


SCLK

                                                                                                                  ...
MOSI     MODE[1:0], ADDRESS[13:8]       ADDRESS[7:0]            VALUEADDRESS             VALUEADDRESS+1             ALUEADDRESS+n



MISO




                                                                                        Atmel AT86RF215 - DATASHEET                     17
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 18 -->

Figure 4-5. SPI Block Read Access


SELN


SCLK

                                                                                                                                                      ...
MOSI     MODE[1:0], ADDRESS[13:8]                     ADDRESS[7:0]



MISO                                                                                  VALUEADDRESS                    VALUEADDRESS+1                    ALUEADDRESS+n




4.2.5   SPI Timing
        Figure 4-6 and Figure 4-7 illustrate the SPI timing and its parameters. The corresponding timing parameter values tSPI_0
        - tSPI_9 are defined in section "SPI Timing Characteristics" on page 204.

        Figure 4-6. SPI Timing, Definition of Timing Parameters tSPI_0, tSPI_5, tSPI_6, tSPI_8, tSPI_9.

                tSPI_0                                                                                                              tSPI_9       tSPI_8

        SELN
                                                                        tSPI_5
        SCLK


        MOSI             7        6   5   4       3       2   1   0               7      6    5    4     3     2     1      0
                                                                                                                                             tSPI_6

        MISO        Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0              Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0




        Figure 4-7. SPI Timing, Definition of Timing Parameters tSPI_1 to tSPI_4.

        SELN


        SCLK
                                      tSPI_3 tSPI_4

        MOSI                              Bit 7                                  Bit 6                                   Bit 5
                         tSPI_1                                       tSPI_2
        MISO                                      Bit 7                               Bit 6                                 Bit 5




        SELN low enables the MISO output driver of the AT86RF215. The MSB of values transferred via MISO is valid after tSPI_
        1 and is updated at each falling edge of SCLK. If the MISO driver is disabled (during inactive SPI periods), no internal

        pull-up circuitry is connected to it. Driving the appropriate signal level must be ensured by the master device or an
        external pull-up resistor.
        Referring to Figure 4-6 and Figure 4-7, the AT86RF215 MOSI is sampled at the rising edge of the SCLK signal. The
        signal MOSI must be stable before and after the rising edge of SCLK as specified by tSPI_3 and tSPI_4. The output (MISO)
        is initiated at the falling edge of SCLK.
        The SPI command is processed at the last rising clock edge of SCLK.




                                                                                                                   Atmel AT86RF215 - DATASHEET                          18
                                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 19 -->

4.3     Interrupt Signalling
        The radios and the basebands of the AT86RF215 generate interrupt events. All enabled interrupt events are logically
        OR’d to form the single external interrupt signal at pin IRQ.
        The IRQ behavior and the pad driver strength can be configured by the register RF_CFG. The register RF_CFG content
        is maintained during state DEEP_SLEEP and is cleared during RESET.
        The active polarity of pin IRQ can be configured by sub-register RF_CFG.IRQP. After a reset procedure the polarity is
        set to active high.
        For further information see section "Interrupts" on page 38.

4.3.1   Register Description
4.3.1.1 RF_CFG – IRQ Configuration
        The register RF_CFG contains bits to configure the IRQ behavior.
        Bit                    7           6           5            4         3        2              1             0
        (0x0006)               –           –            –           –      IRQMM      IRQP                 DRV                     RF_CFG
        Read/Write            R            R           R            R         RW      RW            RW            RW
        Initial Value          0           0           0            0         1        0              0             1

         Bit 3 – RF_CFG.IRQMM: IRQ Mask Mode
        The bit IRQMM configures the IRQ mask mode.

        Table 4-5.      IRQMM

        Sub-register               Value       Description
        IRQMM                      0x0         Masked IRQ reasons do not appear in IRQS register
                                   0x1         Masked IRQ reasons do appear in IRQS register

         Bit 2 – RF_CFG.IRQP: IRQ Polarity
        The bit IRQP configures the IRQ pin polarity.

        Table 4-6.      IRQP

        Sub-register               Value       Description
        IRQP                       0x0         Active high
                                   0x1         Active low

         Bit 1:0 – RF_CFG.DRV: Output Driver Strength of Pads
        The bits DRV configure the pads driver strength of the pins IRQ, MISO, and the frontend control (i.e. FEA09, FEB09,
        FEA24, FEB24) pins.

        Table 4-7.      DRV

        Sub-register           Name                          Value      Description
        DRV                    RF_DRV2                        0x0       2mA
                               RF_DRV4                        0x1       4mA
                               RF_DRV6                        0x2       6mA
                               RF_DRV8                        0x3       8mA




                                                                                             Atmel AT86RF215 - DATASHEET                     19
                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| IRQMM | 0x0 | Masked IRQ reasons do not appear in IRQS register |
|  | 0x1 | Masked IRQ reasons do appear in IRQS register |

| Sub-register | Value | Description |
| --- | --- | --- |
| IRQP | 0x0 | Active high |
|  | 0x1 | Active low |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| DRV | RF_DRV2 | 0x0 | 2mA |
|  | RF_DRV4 | 0x1 | 4mA |
|  | RF_DRV6 | 0x2 | 6mA |
|  | RF_DRV8 | 0x3 | 8mA |


<!-- page 20 -->

4.4     Clock Output
        The AT86RF215 provides a clock output signal at pin CLKO.
        The clock output signal is generated by the oscillator module using the external crystal or TCXO; see section "Crystal
        Oscillator and TCXO" on page 67 for further information about the oscillator configuration.
        After reset or power-on the clock output signal is enabled and set to the default clock rate value of 26MHz. The signal’s
        driver strength and the clock frequency can be configured by register RF_CLKO.
        Resetting AT86RF215 via Chip Reset causes the register RF_CLKO to be reset to its default value.
        In state DEEP_SLEEP the clock output signal is paused. If the device is woken up by writing command TRXOFF to one
        of the transceiver command registers, the clock output signal continues after tDEEP_SLEEP_TRXOFF with the configuration that
        has been set before entering state DEEP_SLEEP.
        If the clock output signal is not used, it is recommended to switch it off. The output signal can be switched off by the
        sub-register RF_CLKO.OS.
        For electrical parameter of the clock output signal see section "Clock Output – pin CLKO" on page 189 and "General
        Transceiver Specifications" on page 188.

4.4.1   Register Description
4.4.1.1 RF_CLKO – Clock Output
        The register RF_CLKO contains configuration bits for the clock output signal. The register setting is maintained during
        state DEEP_SLEEP.
        Bit                   7       6          5            4         3          2            1             0
        (0x0007)              –       –          –                DRV                          OS                           RF_CLKO
        Read/Write            R       R          R         RW           RW        RW          RW            RW
        Initial Value         0       0          0            0         1          0            0             1

         Bit 4:3 – RF_CLKO.DRV: Output Driver Strength CLKO
        The bit DRV configures the CLKO pad driver strength.

        Table 4-8.      DRV

        Sub-register          Name                     Value      Description
        DRV                   RF_DRVCLKO2               0x0       2mA
                              RF_DRVCLKO4               0x1       4mA
                              RF_DRVCLKO6               0x2       6mA
                              RF_DRVCLKO8               0x3       8mA

         Bit 2:0 – RF_CLKO.OS: Clock Output Selection
        The bit OS configures the clock output frequency of the CLKO output signal. The change of the clock output frequency
        occurs immediately and spike free.




                                                                                       Atmel AT86RF215 - DATASHEET                     20
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| DRV | RF_DRVCLKO2 | 0x0 | 2mA |
|  | RF_DRVCLKO4 | 0x1 | 4mA |
|  | RF_DRVCLKO6 | 0x2 | 6mA |
|  | RF_DRVCLKO8 | 0x3 | 8mA |


<!-- page 21 -->

Table 4-9.   OS

Sub-register      Value   Description
OS                0x0     OFF
                  0x1     26MHz
                  0x2     32MHz
                  0x3     16MHz
                  0x4     8MHz
                  0x5     4MHz
                  0x6     2MHz
                  0x7     1MHz




                                        Atmel AT86RF215 - DATASHEET                     21
                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| OS | 0x0 | OFF |
|  | 0x1 | 26MHz |
|  | 0x2 | 32MHz |
|  | 0x3 | 16MHz |
|  | 0x4 | 8MHz |
|  | 0x5 | 4MHz |
|  | 0x6 | 2MHz |
|  | 0x7 | 1MHz |


<!-- page 22 -->

4.5     Serial I/Q Data Interface

4.5.1    Introduction
        A point-to-point, low voltage differential signalling (LVDS) interface is used for the data transfer between the
        AT86RF215 and an external baseband processor. The implemented interface is based on the IEEE standard 1596.3-
        1996 (see [4]). The specific interface of the AT86RF215 has a data rate of 128Mb/s composed of 16 data bits at 4MHz
        for each of the I and Q data streams from the device. The LVDS clock frequency is 64MHz. The interface uses double
        data rate (DDR). A new data bit is received and transmitted at both the falling and rising edge of the LVDS clock.
        In order to decrease current consumption, a proprietary scalable LVDS (SLVDS) interface is implemented in addition to
        the IEEE standard functionality.
        The AT86RF215 data interface consists of two receive and one transmit signal paths. The interface signals are all
        implemented as differential pairs. Two receive pairs and one clock pair form the LVDS driver. One transmit pair and one
        clock pair form the LVDS receiver. Within this document the terminologies of I/Q data driver and receiver are used with
        reference to the external baseband processor, see Figure 4-8.

        Figure 4-8. I/Q Data Interface


         AT86RF215                                                        External Baseband

                        RX        I/Q Data    2       RXDP24/             I/Q Data
                                  Driver              RXDN24              Receiver
             2.4GHz                           2
              Radio                                   RXDP09/
                                                      RXDN09
                                              2       RXCLKP/
                                                      RXCLKN


                                                                2
                        RX    TX I/Q Data              TXDP/              I/Q Data
            Sub-1GHz             Receiver              TXDN               Driver
              Radio
                             TX                       TXCLKP/ 2
                                                      TXCLKN




        The TXCLK must have the same frequency as the RXCLK signal. There is no requirement on the phase alignment. The
        RXCLK driver is also enabled while transmitting data, so that the external baseband can derive the TXCLK from the
        RXCLK, see Table 10-34 on page 206 and Table 10-35 on page 207 for the required phase relation between clock and
        data.
        The driver and receiver should be on the same printed circuit board (PCB) and have a small ground potential Vgdb (see
        Figure 4-9 on page 23) difference. The length of the PCB wires between the devices is expected to be short and their
        differential impedance should be 100Ω.




                                                                                     Atmel AT86RF215 - DATASHEET                     22
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 23 -->

        Figure 4-9. I/Q Data Interface Structure (Refer to [4])


                                      driver             interface                receiver


                                          Voa     A                    A’   Via

                                                        B                             100Ω
                                                  B                    B’
                                          Vob                               Vib


                                                             Vgdp




4.5.2    Configuration
        The proprietary SLVDS link has a low voltage swing of 200mV with a common mode offset voltage of 200mV. The
        differential lines must be terminated with a 100Ω differential impedance. This termination is included in the I/Q data
        receiver of the AT86RF215. Voltage swing and offset can be adjusted with sub-registers IQIFC0.DRV and IQIFC0.CMV.
        Note that a higher voltage swing also increases the current consumption.
        The I/Q data interface can also be operated with a common mode voltage of 1.2V. In this way the AT86RF215 can
        communicate with common LVDS interfaces compliant to the IEEE standard 1596.3-1996 [4]. The higher common
        mode voltage is selected if bit IQIFC0.CMV1V2 is set to 1. If it is set to 1, the sub-register IQIFC0.CMV has no function.
        The I/Q data interface receivers operate over a wide input common mode range. They have a differential input
        hysteresis and a fail safe circuit. The hysteresis avoids amplifying small signal noise at zero input voltages. Input
        voltages can be zero when receiver inputs are open or the connected drivers are powered down. The hysteresis means
        that an input signal must change by more than Vhyst (see Table 10-32 on page 206) to toggle the receiver output. If no
        driver circuit is connected to the inputs, the fail safe circuit sets the sub-register IQIFC1.FAILSF to 1 and the internal
        pull-ups force the open inputs to DEVDD.
        Refer to chapter "Electrical Characteristics" on page 187 for a complete list of all DC and AC characteristics of the
        LVDS interface.

4.5.3    Characteristics and Timing
        Double data rate is implemented to clock the data using both negative and positive clock edges. The data sent by the
        AT86RF215 (transceiver state RX) is center aligned. The data received from an external baseband processor
        (transceiver TX) must be edge aligned. Uneven data bits are related to the rising clock edge. Even data bits are related
        to the falling clock edge (see Figure 4-10 on page 24).
        The skew between RX clock and data can be adjusted to match the timing requirement of the LVDS input of an external
        baseband processor. The skew alignment parameter is set by the sub-register IQIFC1.SKEWDRV. Figure 4-10 shows
        the functionality of the skew alignment. The skew settings must only be altered when the LVDS interface is off (for
        example in state TRXOFF).




                                                                                     Atmel AT86RF215 - DATASHEET                      23
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 24 -->

        Figure 4-10. Clock to Data Timing Alignment

        RX Link - I/Q Driver (AT86RF215 OUTPUT)
                                  -1ns   0ns   +1ns   +2ns                       -1ns   0ns   +1ns   +2ns

        RXCLK
                  IQIFC1.SKEWDRV: 3      2     1      0

                                             tD CLK-DATA_RX(1)

        RXD09                    RXD09[31]                                  RXD09[30]                                    RXD09[29]              RXD09
                                                                    tSkewD2(2)

        RXD24                    RXD24[31]                                  RXD24[30]                                    RXD24[29]               RXD24


        TX Link – I/Q Receiver (AT86RF215 INPUT)

        TXCLK
                                                                 tSkewR1(3) (-1ns)                                       tSkewR1 (2ns)

        TXD                    Valid Data[31]                             Valid Data[30]                                 Valid Data[29]       Valid Data



        Notes:   1.   Programmable clock to data delay at the I/Q data interface driver (for details refer to register
                      IQIFC1.SKEWDRV on page 28 and section "I/Q Data Interface Driver AC Specification" on page 206)
                 2.   LVDS data channel to LVDS data channel skew (see section "I/Q Data Interface Driver AC Specification"
                       on page 206)
                 3.   Skew tolerable at receiver input to meet setup and hold time requirements (see section "I/Q Data Interface
                      Receiver AC Specification" on page 207)


        The data sampling rate fs ranges from 400ksample/s to 4Msample/s and is defined by the registers RFn_TXDFE and
        RFn_RXDFE. The interface transfers the I/Q data in 32-bit data words with a fixed rate of 4Mword/s. This results in a
        fixed rate of 128Mb/s with a double data rate clock frequency of 64MHz at the interface.
        An IDLE period must be inserted between each 32-bit data word if a lower sampling rate fs is used. During the IDLE
        period zero words are transmitted. A zero word consists of 32 zero bits.
        The interface must be DC coupled, because the bit stream is not DC balanced.

4.5.4    Word Format
        The I/Q data interface is based on serializing/de-serializing a 32-bit word. The 32-bit word is composed of a two bit I
        synchronization pattern followed by a 14-bit I data word and a two bit Q synchronization pattern followed by a 14-bit Q
        data word (see Table 4-10 below).

        Table 4-10. I/Q Data Interface Word Frame Format

        Bit[31:30]            Bit[29:16]                                                                    Bit[15:14]              Bit[13:0]
        I_SYNC = 0b10         I_DATA[13:0]                                                                  Q_SYNC = 0b01           Q_DATA[13:0]


        The actual baseband signal data is contained in sub-fields I_DATA[13:1] and Q_DATA[13:1], each interpreted as 13-bit
        2’s complement signed values with {I,Q}_DATA[13] being the sign bit and {I,Q}_DATA[1] being the least significant bit.




                                                                                                                             Atmel AT86RF215 - DATASHEET                      24
                                                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 25 -->

              For the transmit I/Q data (pin TXD) TX control information can be embedded in the bit I_DATA[0]. In this case,
              embedded TX control must be enabled in the register IQIFC0.EEC and the bit Q_DATA[0] must be zero. If embedded
              TX control is not enabled, the bits {I,Q}_DATA[0] are not interpreted.
              For the receive I/Q data (pin RXD09/24) the bits {I,Q}_DATA[0] are not used and always equal to 0.
              For details on the I/Q data processing refer to section "Transmitter Digital Frontend" on page 43 and "Receiver Digital
              Frontend" on page 53. Embedded TX control is described in section "Transmit Control" on page 46.

 4.5.5         Sample Rate
              The sample rate (SR) of the I/Q data stream at TXD must be the same as the transmit sample rate configured in
              register TXDFE.SR. A number of m = TXDFE.SR-1 zero words must be inserted between the data carrying 32-bit
              words (refer to Figure 4-11 below).
              The sample rate of the I/Q data stream at RXD09 and RXD24 is the same as the receive sample rate configured in
              register RXDFE.SR. Zero words are inserted in the same format as for the TXD stream.

Figure 4-11. I/Q Data at Different Sample Rates

Sample Rate

                32Bit   32Bit   32Bit   32Bit     32Bit   32Bit   32Bit    32Bit     32Bit   32Bit   32Bit   32Bit     32Bit   32Bit   32Bit   32Bit     32Bit   32Bit   32Bit   32Bit   32Bit
4Msample/s
                Data    Data    Data    Data      Data    Data    Data     Data      Data    Data    Data    Data      Data    Data    Data    Data      Data    Data    Data    Data    Data

                32Bit   Zero    32Bit   Zero      32Bit   Zero    32Bit    Zero      32Bit   Zero    32Bit   Zero      32Bit   Zero    32Bit   Zero      32Bit   Zero    32Bit   Zero    32Bit
2Msample/s                                                                                                                                               Data    Word    Data    Word    Data
                Data    Word    Data    Word      Data    Word    Data     Word      Data    Word    Data    Word      Data    Word    Data    Word

                32Bit   Zero    Zero    32Bit     Zero    Zero    32Bit    Zero      Zero    32Bit   Zero    Zero      32Bit   Zero    Zero    32Bit     Zero    Zero    32Bit   Zero    Zero
4/3Msample/s    Data    Word    Word    Data      Word    Word    Data     Word      Word    Data    Word    Word      Data    Word    Word    Data      Word    Word    Data    Word    Word

                32Bit   Zero    Zero    Zero      32Bit   Zero    Zero     Zero      32Bit   Zero    Zero    Zero      32Bit   Zero    Zero    Zero      32Bit   Zero    Zero    Zero    32Bit
1Msample/s
                Data    Word    Word    Word      Data    Word    Word     Word      Data    Word    Word    Word      Data    Word    Word    Word      Data    Word    Word    Word    Data

                32Bit   Zero    Zero    Zero      Zero    32Bit   Zero     Zero      Zero    Zero    32Bit   Zero      Zero    Zero    Zero    32Bit     Zero    Zero    Zero    Zero    32Bit
800ksample/s
                Data    Word    Word    Word      Word    Data    Word     Word      Word    Word    Data    Word      Word    Word    Word    Data      Word    Word    Word    Word    Data

                32Bit   Zero    Zero    Zero      Zero    Zero    32Bit    Zero      Zero    Zero    Zero    Zero      32Bit   Zero    Zero    Zero      Zero    Zero    32Bit   Zero    Zero
2/3Msample/s
                Data    Word    Word    Word      Word    Word    Data     Word      Word    Word    Word    Word      Data    Word    Word    Word      Word    Word    Data    Word    Word

                32Bit   Zero    Zero    Zero      Zero    Zero    Zero     Zero      32Bit   Zero    Zero    Zero      Zero    Zero    Zero    Zero      32Bit   Zero    Zero    Zero    Zero
500ksample/s
                Data    Word    Word    Word      Word    Word    Word     Word      Data    Word    Word    Word      Word    Word    Word    Word      Data    Word    Word    Word    Word

                32Bit   Zero    Zero    Zero      Zero    Zero    Zero     Zero      Zero    Zero    32Bit   Zero      Zero    Zero    Zero    Zero      Zero    Zero    Zero    Zero    32Bit
400ksample/s
                Data    Word    Word    Word      Word    Word    Word     Word      Word    Word    Data    Word      Word    Word    Word    Word      Word    Word    Word    Word    Data
                                                 (SR-1) 32bit Zero Words


              0µs                               1µs                                2µs                               3µs                               4µs                           5µs




 4.5.6         Operation and Synchronization
              If the AT86RF215 operates in I/Q radio mode, it automatically enables the required I/Q data interface driver and
              receiver. The TX link (TXD and TXCLK receiver) is enabled in the states TXPREP and TX. In addition, the RXCLK
              driver is activated because the AT86RF215 operates as I/Q data interface clock master. The RX link is enabled in state
              RX and incorporates the RXCLK and RXD09 or RXD24 driver for the sub-1GHz or 2.4GHz transceiver, respectively.
              For details about the transceiver operating modes and states refer to chapter "Basic Operation " on page 30
              After enabling the TX link, the TXD and TXCLK driver require a start-up time (see section "I/Q Data Interface Driver DC
              and Startup Specification" on page 205). The start-up phase is followed by the initial synchronization. If the I_SYNC
              pattern is detected after 32 or more zero bits, the de-serialization of the I/Q data is started. The synchronization of the
              TX link is validated at each expected I_SYNC and Q_SYNC pattern. An I_SYNC pattern is expected either 16 bits after
              a Q_SYNC pattern or 32 or more zero bits after a 32-bit data word. A Q_SYNC pattern is expected 16 bits after an
              I_SYNC pattern. Figure 4-12 on page 26 shows the start-up phase and initial synchronization of the TX link.
              The successful reception of a I/Q data word is indicated by the synchronization status bit IQIFC2.SYNC. The bit is
              cleared at each read access and set again at the reception of the next I/Q data word.



                                                                                                                                   Atmel AT86RF215 - DATASHEET                                   25
                                                                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 26 -->

        If the validation of the synchronization fails, the received data word is ignored, the synchronization status bit
        IQIFC2.SYNC is cleared and an error status is indicated together with an interrupt (see bit IQIFC0.SF and
        IRQS.IQIFSF). A synchronization failure is also indicated if a bit pattern other than I_SYNC is detected during the IDLE
        condition. The error status is cleared after a new successful initial word synchronization. Figure 4-13 below shows an
        example of a synchronization failure caused by a wrong I_SYNC pattern followed by a new synchronization.
        Disabling the I/Q data driver (transceiver is set to state TRXOFF) resets the bits IQIFC2.SYNC and IQIFC0.SF to zero.
        Between the last 32-bit word of a TX baseband frame and the first 32-bit word of the following TX baseband frame, zero
        bits must be inserted for a minimum of 2.5µs (400ksample/s period) to ensure a correct resynchronization of the I/Q
        data interface.

        Figure 4-12. I/Q Data Interface Initial Synchronization



        STATE           TRANSITION                                              TXPREP
                                         tstartupR(1)

        TXD,TXCLK                                                              I_SYNC        I_DATA        Q_SYNC       Q_DATA       I_SYNC

                                                         ≥32 zero bits
                                                                                   initial synchronization
        IQIFC1.FAILSF


        IQIFC2.SYNC



        Note:   I/Q data interface receiver start-up time (see section "I/Q Data Interface Driver DC and Startup Specification"
                     on page 205)

        Figure 4-13. I/Q Data Interface Synchronization Failure


                               I_SYNC
        TXD           Q_DATA
                                ≠ 0b10
                                                                                        I_SYNC         I_DATA       Q_SYNC       Q_DATA        I_SYNC

                                                               ≥32 zero bits
                               synchronization failure                                           new synchronization
        IQIFC0.SF


        IQIFC2.SYNC


        IRQ
                                     IQIFSF


4.5.7    Loop-back Test
        An external loop-back feature is available to test the I/Q data interface by sending the data from the receiver TXD
        directly to the driver RXD09 and RXD24. Like in normal operation mode, the TXCLK is expected to be a looped back
        version of RXCLK with no guaranteed phase alignment. Due to the synchronization of the loop-back data to the driver
        clock RXCLK, the delay from TXD to RXD09/24 is up to 18-bit periods.
        The loop-back mode is enabled setting bit IQIFC0.EXTLB to 1. Note, the loop-back mode must not be enabled in
        normal transmit operation mode, the loop-back mode shall be used for interface test and setup.




                                                                                                   Atmel AT86RF215 - DATASHEET                          26
                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 27 -->

4.5.8    Register Description
4.5.8.1 RF_IQIFC0 – Transceiver I/Q Data Interface Configuration Register 0
        The register configures the I/Q data interface.
        Bit                7           6             5          4        3          2             1             0
                        EXTLB          SF                 DRV                 CMV             CMV1V2          EEC             RF_IQIFC0
        Read/Write        RW           R            RW          RW       RW         RW          RW            RW
        Initial Value      0           0             0          1        0          1             0             0

         Bit 7 – IQIFC0.EXTLB: I/Q IF External Loopback
        The bit enables the external loopback functionality. If the bit is set to 1, the received data of the I/Q IF pin TXDn/p is fed
        back via the pins RXDxxn/p.

        Table 4-11. EXTLB

        Sub-register           Value        Description
        EXTLB                   0x0         External loopback disabled
                                0x1         External loopback enabled

         Bit 6 – IQIFC0.SF: I/Q IF Synchronization Failure
        The bit indicates whether the data stream of the I/Q data interface is synchronized correctly.

        Table 4-12. SF

        Sub-register           Value        Description
        SF                      0x0         No synchronization failure
                                0x1         Synchronization failure

         Bit 5:4 – IQIFC0.DRV: I/Q IF Driver Output Current
        The sub-register configures the I/Q data interface driver output current.

        Table 4-13. DRV

        Sub-register           Value        Description
        DRV                     0x0         1mA
                                0x1         2mA
                                0x2         3mA
                                0x3         4mA

         Bit 3:2 – IQIFC0.CMV: I/Q IF common mode voltage
        The sub-register configures the common mode voltage of the I/Q data interface signals.

        Table 4-14. CMV

        Sub-register           Value        Description
        CMV                     0x0         150mV
                                0x1         200mV
                                0x2         250mV
                                0x3         300mV

         Bit 1 – IQIFC0.CMV1V2: I/Q IF Common Mode Voltage Compliant to IEEE Std 1596
        The common mode voltage of 1.2V compliant to the IEEE Std 1596 is set. Sub-register CMV has no effect.



                                                                                         Atmel AT86RF215 - DATASHEET                      27
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| EXTLB | 0x0 | External loopback disabled |
|  | 0x1 | External loopback enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| SF | 0x0 | No synchronization failure |
|  | 0x1 | Synchronization failure |

| Sub-register | Value | Description |
| --- | --- | --- |
| DRV | 0x0 | 1mA |
|  | 0x1 | 2mA |
|  | 0x2 | 3mA |
|  | 0x3 | 4mA |

| Sub-register | Value | Description |
| --- | --- | --- |
| CMV | 0x0 | 150mV |
|  | 0x1 | 200mV |
|  | 0x2 | 250mV |
|  | 0x3 | 300mV |


<!-- page 28 -->

       Table 4-15. CMV1V2

        Sub-register          Value         Description
        CMV1V2                   0x0        CMV sub-register value is valid
                                 0x1        Common mode of 1.2V is set

        Bit 0 – IQIFC0.EEC: I/Q IF Enable Embedded TX Start Control
       The bit enables the ability to start and finish transmitting by a control bit within the I/Q data stream (I_DATA[0]). If this bit
       is set to 1, the transmit start and finish cannot be controlled by SPI commands.

       Table 4-16. EEC

        Sub-register          Value         Description
        EEC                      0x0        Embedded control is not enabled.
                                 0x1        Embedded control is enabled.

4.5.8.2 RF_IQIFC1 – Transceiver I/Q Data Interface Configuration Register 1
       The register configures the skew behavior, the chip mode of the I/Q data interface and contains the status of the I/Q
       data interface receiver.
        Bit               7            6            5             4           3       2            1             0
                        FAILSF                    CHPM                        –       –                SKEWDRV                 RF_IQIFC1
        Read/Write        R            RW          RW          RW          RW        RW          RW            RW
        Initial Value     0            0            0             0           0       0            1             0

        Bit 7 – IQIFC1.FAILSF: I/Q IF Receiver Failsafe Status
       This bit indicates that the LVDS receiver is in failsafe mode. The failsafe mode is entered if the LVDS receiver is not
       driven by an LVDS driver.

        Bit 6:4 – IQIFC1.CHPM: Chip Mode
       This sub-register configures the working mode of the chip and define which parts (RF, baseband, I/Q IF) are in
       operation. Note, the AT86RF215IQ supports chip mode one (CHPM=1) only. Also note, the AT86RF215M generally
       does not support operation of BBC1 and RF24.

       Table 4-17. CHPM

        Sub-register       Name                            Value      Description
        CHPM               RF_MODE_BBRF                     0x0       RF enabled, baseband (BBC0, BBC1) enabled, I/Q IF disabled
                           RF_MODE_RF                       0x1       RF enabled, baseband (BBC0, BBC1) disabled, I/Q IF enabled
                           RF_MODE_BBRF09                   0x4       RF enabled, baseband (BBC0) disabled and (BBC1) enabled, I/Q
                                                                      IF for sub-GHz Transceiver enabled
                           RF_MODE_BBRF24                   0x5       RF enabled, baseband (BBC1) disabled and (BBC0) enabled, I/Q
                                                                      IF for 2.4GHz Transceiver enabled

        Bit 1:0 – IQIFC1.SKEWDRV: Skew alignment I/Q IF driver
       This sub-register configures the alignment of the I/Q data interface RXDxxn/p signal edges relative to the RXCLKn/p
       clock edges. The register values define the time from the RXCLKn/p clock edge to the next RXDxxn/p signal edge. The
       reset value of 2 (3.906ns) corresponds to a half bit period with the data center aligned in reference to the clock.




                                                                                          Atmel AT86RF215 - DATASHEET                      28
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CMV1V2 | 0x0 | CMV sub-register value is valid |
|  | 0x1 | Common mode of 1.2V is set |

| Sub-register | Value | Description |
| --- | --- | --- |
| EEC | 0x0 | Embedded control is not enabled. |
|  | 0x1 | Embedded control is enabled. |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| CHPM | RF_MODE_BBRF | 0x0 | RF enabled, baseband (BBC0, BBC1) enabled, I/Q IF disabled |
|  | RF_MODE_RF | 0x1 | RF enabled, baseband (BBC0, BBC1) disabled, I/Q IF enabled |
|  | RF_MODE_BBRF09 | 0x4 | RF enabled, baseband (BBC0) disabled and (BBC1) enabled, I/Q |
|  |  |  | IF for sub-GHz Transceiver enabled |
|  | RF_MODE_BBRF24 | 0x5 | RF enabled, baseband (BBC1) disabled and (BBC0) enabled, I/Q |
|  |  |  | IF for 2.4GHz Transceiver enabled |


<!-- page 29 -->

       Table 4-18. SKEWDRV

        Sub-register           Value        Description
        SKEWDRV                0x0          1.906ns
                               0x1          2.906ns
                               0x2          3.906ns
                               0x3          4.906ns

4.5.8.3 RF_IQIFC2 – Transceiver I/Q Data Interface Configuration Register 2
       The register contains the status of the I/Q data interface deserializer.
        Bit               7            6              5     4          3          2             1             0
                        SYNC           –              –     –          –          –             –             –             RF_IQIFC2
        Read/Write       R             RW             R     R         RW          RW          RW            RW
        Initial Value     0            0              0     0          1          0             1             1

        Bit 7 – IQIFC2.SYNC: I/Q IF Deserializer Synchronization Status
       This bit indicates that the I/Q IF has synchronized to the incoming I/Q data stream.




                                                                                       Atmel AT86RF215 - DATASHEET                      29
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SKEWDRV | 0x0 | 1.906ns |
|  | 0x1 | 2.906ns |
|  | 0x2 | 3.906ns |
|  | 0x3 | 4.906ns |


<!-- page 30 -->

5.      Basic Operation

5.1     Operating Modes

5.1.1   Operating Modes Description
        The AT86RF215 contains two transceivers. Each transceiver comprises a radio and a baseband module. Each
        transceiver can be operated in two different modes:
               Baseband mode
               I/Q radio mode.
        The AT86RF215IQ only provides the I/Q radio mode for both transceivers. For device differentiation see section "Device
        Family" on page 3.
        In the baseband mode, the internal baseband controls the radio and processes the data encoding/decoding for transmit
        and receive from the internal frame buffer. Figure 5-1 shows a sample system setup if both transceivers are operated in
        this mode.
        In the I/Q radio mode, the radio is controlled from an external microcontroller via SPI and the data are exchanged via
        the I/Q data interface which is described in section "Serial I/Q Data Interface" on page 22. This allows the usage of an
        external baseband. In the I/Q radio mode any access to BBCn_* registers of the respective baseband has no effect.
        This implies that no baseband interrupts are issued and the registers BBCn_IRQS are not changed. An example setup
        for both transceivers operated in I/Q radio mode is shown in Figure 5-2.
        If one transceiver is operated in I/Q radio mode and the other transceiver is operated in baseband controlled mode, a
        mixed setup applies (see Figure 5-3 and Figure 5-4).
        After reset or wakeup from state DEEP_SLEEP, the baseband mode is set for both transceivers as default. The mode
        can be configured by the sub-register IQIFC1.CHPM; see Table 5-1 below.

        Table 5-1.    Chip mode Configurations

                                                 TRX09                               TRX24
        Operating Mode                                                                                                              TXD
                                                 RF09       BBC0         RXD09       RF24           BBC1           RXD24
                                                 on         on           off         on             on             off
        IQIFC1.CHPM = RF_MODE_BBRF                                                                                                  off
                                                 Baseband mode                       Baseband mode
                                                 on         off          on          on             off            on
        IQIFC1.CHPM = RF_MODE_RF                                                                                                    on
                                                 I/Q radio mode                      I/Q radio mode
                                                 on         off          on          on             on             off
        IQIFC1.CHPM = RF_MODE_BBRF09                                                                                                on
                                                 I/Q radio mode                      Baseband mode
                                                 on         on           on          on             off            on
        IQIFC1.CHPM = RF_MODE_BBRF24                                                                                                on
                                                 Baseband mode                       I/Q radio mode
        Note:     See sub-register IQIFC1.CHPM for chip mode enumerations




                                                                                    Atmel AT86RF215 - DATASHEET                           30
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 31 -->

Figure 5-1. System Setup Using Baseband Mode for both Transceivers


 AT86RF215                                     IRQ              External
                                               SPI              Microcontroller
                                              Reset

      RF09              BBC0
      Radio            Basband



      RF24              BBC1
      Radio           Baseband




Figure 5-2. System Setup Using I/Q Radio Mode for both Radios


 AT86RF215                                     IRQ              External
                                               SPI              Microcontroller /
                                              Reset             Baseband
      RF09                                    RXD09
      Radio

                                               TXD                    Baseband

      RF24
      Radio                                   RXD24




Figure 5-3. System Setup for mixed Setup (TRX09 in I/Q Radio Mode, TRX24 in Baseband Mode)


 AT86RF215                                     IRQ              External
                                               SPI              Microcontroller /
                                              Reset             Baseband
      RF09                                    RXD09
                                                                      Baseband
      Radio                                    TXD


      RF24              BBC1
      Radio           Baseband




Figure 5-4. System Setup for mixed Setup (TRX24 in I/Q Radio Mode, TRX09 in Baseband Mode)


 AT86RF215                                     IRQ              External
                                               SPI              Microcontroller /
                                              Reset             Baseband
      RF09              BBC0
      Radio           Baseband



      RF24                                     TXD
                                                                      Baseband
      Radio                                   RXD24




                                                                         Atmel AT86RF215 - DATASHEET                     31
                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 32 -->

5.1.2   Register Description
5.1.2.1 RF_IQIFC1 – Transceiver I/Q Data Interface Configuration Register 1
        The register configures the skew behavior, the chip mode of the I/Q data interface and contains the status of the I/Q
        data interface receiver.
        Bit                7         6          5            4        3          2            1             0
                         FAILSF               CHPM                     –         –                SKEWDRV                 RF_IQIFC1
        Read/Write         R        RW         RW         RW         RW         RW          RW            RW
        Initial Value      0         0          0            0        0          0            1             0

         Bit 6:4 – IQIFC1.CHPM: Chip Mode
        This sub-register configures the working mode of the chip and define which parts (RF, baseband, I/Q IF) are in
        operation. Note, the AT86RF215IQ supports chip mode one (CHPM=1) only. Also note, the AT86RF215M generally
        does not support operation of BBC1 and RF24.

        Table 5-2.      CHPM

        Sub-register        Name                      Value      Description
        CHPM                RF_MODE_BBRF               0x0       RF enabled, baseband (BBC0, BBC1) enabled, I/Q IF disabled
                            RF_MODE_RF                 0x1       RF enabled, baseband (BBC0, BBC1) disabled, I/Q IF enabled
                            RF_MODE_BBRF09             0x4       RF enabled, baseband (BBC0) disabled and (BBC1) enabled, I/Q
                                                                 IF for sub-GHz Transceiver enabled
                            RF_MODE_BBRF24             0x5       RF enabled, baseband (BBC1) disabled and (BBC0) enabled, I/Q
                                                                 IF for 2.4GHz Transceiver enabled




                                                                                     Atmel AT86RF215 - DATASHEET                      32
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| CHPM | RF_MODE_BBRF | 0x0 | RF enabled, baseband (BBC0, BBC1) enabled, I/Q IF disabled |
|  | RF_MODE_RF | 0x1 | RF enabled, baseband (BBC0, BBC1) disabled, I/Q IF enabled |
|  | RF_MODE_BBRF09 | 0x4 | RF enabled, baseband (BBC0) disabled and (BBC1) enabled, I/Q |
|  |  |  | IF for sub-GHz Transceiver enabled |
|  | RF_MODE_BBRF24 | 0x5 | RF enabled, baseband (BBC1) disabled and (BBC0) enabled, I/Q |
|  |  |  | IF for 2.4GHz Transceiver enabled |


<!-- page 33 -->

5.2   State Machine
      The AT86RF215 state machine forms the basis for both operating modes. Figure 5-5 shows the state machine of one of
      the transceiver. This section describes the different states and how to initiate state transitions.

      Figure 5-5. State Machine

                                                                      CMD=SLEEP
           POWER                                                          to the        DEEP_
                                                       SLEEP
            OFF*                                                          other         SLEEP*
                                                                       transceiver

                                                       CMD=TRXOFF
                                                        IRQ: WAKEUP
                            Power On
                            IRQ: WAKEUP      CMD=SLEEP                CMD=TRXOFF
                                                                       IRQ: WAKEUP

                          RSTN = 0,
                                                                                         TX, RX,
            any state
                        RF_RST = 7 or              TRXOFF             CMD=TRXOFF        TXPREP or
                        CMD=RESET                                                      TRANSITION
                            IRQ: WAKEUP




                                                CMD=TXPREP                CMD=RX




                                                TRANSITION                            TRANSITION




                                                  IRQ: TRXRDY




                                CMD=TX                                 CMD=RX

                TX          CMD=TXPREP             TXPREP             CMD=TXPREP           RX
                                                                                                                 TX, RX or
                              IRQ: TRXRDY                               IRQ: TRXRDY                               TXPREP
                                frame end                              frame end
                                 IRQ: TXFE                              IRQ: RXFE

                                                                                                                PLL unlock
                              CMD=TXPREP or PLL lock after channel update                                       IRQ: TRXERR
                                                  IRQ: TRXRDY



      Legend:
           CMD=TRXOFF               transition by value written to register
                RSTN = 0            transition by pin RSTN value
                frame end           transition by event end of transmission or reception
             IRQ: WAKEUP            interrupt status
       * Internal state, cannot be read from register RFn_STATE


      The current transceiver state is determined by reading the register RFn_STATE. A state change is initiated by writing a
      command to the register RFn_CMD. The provided command is appended to the command queue. The command
      queue has a depth of one element. As soon as the previous command has been executed, the next command is
      fetched and handled. For example, if in the state TRXOFF the commands TXPREP and TX are written consecutively to
      the register RFn_CMD, the transition from state TRXOFF to TXPREP is executed before the transition to state TX is
      started.



                                                                                                    Atmel AT86RF215 - DATASHEET                     33
                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

|  | CMD=T IRQ: W |  | RXOF AKEUP |  |
| --- | --- | --- | --- | --- |
| CMD= | SLEEP |  |  | CMD=TRXOFF IRQ: WAKEUP |


<!-- page 34 -->

        An interrupt indication may be associated with some state changes. In this case the corresponding interrupt can be read
        from the registers RFn_IRQS or BBCn_IRQS, for further information see sections "Interrupt Signalling" on page 19 and
        "Interrupts" on page 38.
        The following paragraphs describe the different states and the state transitions.

5.2.2   Power-on Procedure
        For further information see section "Power-on Reset" on page 13.

5.2.3   General State Transitions
        From each state a Chip Reset or Transceiver Reset can be initiated that forces the entire device or a certain transceiver
        to be reset and afterwards to enter state TRXOFF. For further information see section "Reset Modes " on page 13.

5.2.4   State TRXOFF
        In state TRXOFF all registers can be accessed via SPI.
        By default the 1.8V analog voltage regulator (AVDD) is off. The analog voltage regulator is turned on during the
        transition to the states TXPREP or RX and turned off when returning to the state TRXOFF. To shorten the transition
        time, the analog voltage regulator (AVDD) can be configured by the sub-register AUXS.AVEN to remain on in state
        TRXOFF.
        After the transceiver has completed the power-on procedure, it automatically reaches the state TRXOFF and the
        interrupt IRQS.WAKEUP is issued. The state TRXOFF can be reached from all states by writing the command TRXOFF
        to the register RFn_CMD.

5.2.5   State SLEEP
        While the one of the transceiver is in state SLEEP, all registers of the transceiver are reset. In contrast to the state
        DEEP_SLEEP, the digital voltage regulator (DVREG) stays on.
        From state TRXOFF the transceiver is set to state SLEEP by writing the command SLEEP to the register RFn_CMD.
        The state SLEEP can be left again by writing command TRXOFF to the register RFn_CMD. If the transceiver reaches
        the state TRXOFF, the interrupt IRQS.WAKEUP is issued.

5.2.6   State DEEP_SLEEP and Wake-up Procedure
        During state DEEP_SLEEP the DVREG is turned off and the clock output signal (CLKO) is paused; see section "Clock
        Output" on page 20 for further information about CLKO. In state DEEP_SLEEP the lowest current consumption value
        IDEEP_SLEEP is reached.
        If one of the transceivers (sub1-GHz or 2.4GHz) has been set to state SLEEP and the other transceiver (2.4GHz or
        sub1-GHz) is set to the state SLEEP as well, the state DEEP_SLEEP is entered automatically (i.e. both transceivers
        need to be set to SLEEP to enter state DEEP_SLEEP). Figure 5-6 shows the procedure to enter state DEEP_SLEEP.

        Figure 5-6. Procedure entering state DEEP_SLEEP

                                              Command SLEEP to
                                                 RF09_CMD



        CLKO                    CLKO active            CLKO paused



        State RF09               TRXOFF                DEEP_SLEEP




        State RF24                SLEEP                DEEP_SLEEP




                                                                                       Atmel AT86RF215 - DATASHEET                     34
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 35 -->

        Writing command TRXOFF, via SPI, while in state DEEP_SLEEP causes the transition from state DEEP_SLEEP to
        TRXOFF. Writing the command TRXOFF to one of the registers RFn_CMD wakes-up both transceivers. Figure 5-7
        shows the procedure to leave state DEEP_SLEEP and to wake-up.

        Figure 5-7. Wake-up from DEEP_SLEEP Procedure

                                           Command TRXOFF to
                                           RF09_CMD or RF24_CMD



        CLKO                CLKO paused                             CLKO active



        State RF09       DEEP_SLEEP                                 TRXOFF




        State RF24       DEEP_SLEEP                                 TRXOFF



        IRQ                                                         WAKEUP


        Time                                          tDEEP_SLEEP
                                                        _TRXOFF




        Once the command TRXOFF is written to one of the radio register RFn_CMD, the XOSC and DVREG are started. After
        tDEEP_SLEEP_TRXOFF both transceivers enter the state TRXOFF and both interrupts IRQS.WAKEUP are issued. The clock
        output signal is available and provided to pin CLKO if enabled before the state DEEP_SLEEP has been entered. This
        procedure is similar to the power-on procedure. All registers are set to their reset values. However the registers
        RF_CFG, RF_CLKO, RF_XOC and RF_BMDVC are not reset. These registers keep their values during state
        DEEP_SLEEP, see section "AT86RF215 Reset Modes" on page 13.

5.2.7   State TXPREP
        The state TXPREP is used to prepare the transceiver for transmission or reception. In the state TXPREP, the analog
        voltage regulator is powered up, the PLL is locked to the configured frequency and analog calibrations are initiated (see
        section "Analog Calibrations" on page 80). To achieve maximum performance, the TX output power (register
        PAC.TXPWR) and the center frequency (see section "Frequency Synthesizer (PLL)" on page 62) must be configured in
        state TRXOFF. The analog transmitter and receiver are still disabled.
        In the I/Q radio mode the I/Q data interface (pins RXCLKP/N, TXCLKP/N and TXDP/N) is enabled.
        The state TXPREP can be reached from any state, except from the sleep states (i.e. SLEEP and DEEP_SLEEP), by
        writing the command TXPREP to the register RFn_CMD. Depending on the state in which the command TXPREP is
        written different transition durations are required to reach the state TXPREP. For example, from state TRXOFF the
        duration tTRXOFF_TXPREP is required to reach TXPREP.
        In the baseband mode, the baseband switches automatically from the state TX to the state TXPREP once frame
        transmission is completed. It switches automatically from state RX to state TXPREP, once a frame reception is
        completed.
        Entering the state TXPREP by writing the command TXPREP causes the device to issue the interrupt IRQS.TRXRDY
        once the state TXPREP is reached.

5.2.8   State TX
        The state TX is used to transmit data. The PLL is locked to the transmit frequency. The analog voltage regulator, the
        transmitter analog frontend and transmitter digital frontend are all enabled.




                                                                                    Atmel AT86RF215 - DATASHEET                     35
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 36 -->

        In the baseband mode, the baseband enables the transmitter and provides I/Q data to the radio. The samples are
        handled by the radio and transmitted over-the-air. If all samples are sent, the baseband (operated in basic mode)
        disables the transmitter and sets the state TXPREP automatically. For further information see sections "Example
        Transmit Procedure Using Basic Mode" on page 172 and "Example Transmit Procedure Using Auto Mode" on page
        174.
        In the I/Q radio mode, the external microcontroller controls the transmitter via SPI and the I/Q data is provided by the
        I/Q interface. The transmitter control is described in section "Transmit Control" on page 46. In the I/Q radio mode, the
        I/Q data interface (pins RXCLKP/N, TXCLKP/N and TXDP/N) is enabled. For further information see section
        "Transmitter Usage in I/Q Radio Mode " on page 178.
        The state TX is reached from the state TXPREP by writing the command TX to the register RFn_CMD. If the command
        TXPREP or TRXOFF is written to the transceiver while being in state TX, an ongoing transmission is aborted.

5.2.9   State RX
        The state RX is used to receive data. The PLL is locked to the receive frequency. The analog voltage regulator, the
        receiver analog frontend and the receiver digital frontend are all enabled.
        In the baseband mode, the baseband decodes received data. If the baseband has received a complete frame and the
        interrupt IRQS.RXFE occurs, it stops the reception and the transceiver is switched to the state TXPREP automatically.
        For further information about the receive procedure see sections "Example Receive Procedure Using Basic Mode" on
        page 173 and "Example Receive Procedure Using Auto Mode" on page 176.
        In the I/Q radio mode, the I/Q data interface (pins RXCLKP/N, RXDP/N09 (sub1-GHz) or RXDP/N24 (2.4GHz)) is
        enabled.
        The state RX is reached from the state TXPREP or from the state TRXOFF by writing the command RX to the register
        RFn_CMD. If the command TXPREP or TRXOFF is written to the transceiver while being in state RX, an ongoing
        reception is aborted.

5.2.10 Register Description
5.2.10.1 RFn_STATE – Transceiver State
        The register contains the current transceiver state.
        Bit               7          6           5             4       3          2            1             0
                          –           –          –             –       –                   STATE                          RFn_STATE
        Read/Write        R          R           R             R       R          R            R            R
        Initial Value     0          0           0             0       0          1            1             1

         Bit 2:0 – STATE.STATE: Transceiver State
        The current transceiver state can be determined by reading the sub-register STATE. A state transition is triggered by
        writing a new command to the sub-register CMD.




                                                                                      Atmel AT86RF215 - DATASHEET                     36
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 37 -->

      Table 5-3.       STATE

       Sub-register          Name                        Value     Description
       STATE                 RF_TRXOFF                   0x2       TRXOFF (Transceiver off, SPI active)
                             RF_TXPREP                   0x3       TXPREP (Transmit preparation)
                             RF_TX                       0x4       TX (Transmit)
                             RF_RX                       0x5       RX (Receive)
                             RF_TRANSITION               0x6       TRANSITION (State transition in progress)
                             RF_RESET                    0x7       RESET (Transceiver is in state RESET or SLEEP)

5.2.10.2 RFn_CMD – Transceiver Command
      This register allows control of the transceiver.
       Bit                   7        6         5              4         3           2            1             0
                             –        –         –              –         –                      CMD                           RFn_CMD
       Read/Write            R        R         R              R         R          RW          RW            RW
       Initial Value         0        0         0              0         0           0            0             0

       Bit 2:0 – CMD.CMD: Transceiver Command
      The sub-register controls the transceiver states. Writing a new command to the sub-register triggers a state transition.
      The current state can be read from sub-register STATE.

      Table 5-4.       CMD

       Sub-register          Name                        Value     Description
       CMD                   RF_NOP                      0x0       NO OPERATION
                             RF_SLEEP                    0x1       SLEEP
                             RF_TRXOFF                   0x2       TRXOFF (Transceiver off, SPI active)
                             RF_TXPREP                   0x3       TXPREP (Transmit preparation)
                             RF_TX                       0x4       TX (Transmit)
                             RF_RX                       0x5       RX (Receive)
                             RF_RESET                    0x7       RESET (transceiver reset, the transceiver state will automatically
                                                                   end up in state TRXOFF)




                                                                                         Atmel AT86RF215 - DATASHEET                     37
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| STATE | RF_TRXOFF | 0x2 | TRXOFF (Transceiver off, SPI active) |
|  | RF_TXPREP | 0x3 | TXPREP (Transmit preparation) |
|  | RF_TX | 0x4 | TX (Transmit) |
|  | RF_RX | 0x5 | RX (Receive) |
|  | RF_TRANSITION | 0x6 | TRANSITION (State transition in progress) |
|  | RF_RESET | 0x7 | RESET (Transceiver is in state RESET or SLEEP) |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| CMD | RF_NOP | 0x0 | NO OPERATION |
|  | RF_SLEEP | 0x1 | SLEEP |
|  | RF_TRXOFF | 0x2 | TRXOFF (Transceiver off, SPI active) |
|  | RF_TXPREP | 0x3 | TXPREP (Transmit preparation) |
|  | RF_TX | 0x4 | TX (Transmit) |
|  | RF_RX | 0x5 | RX (Receive) |
|  | RF_RESET | 0x7 | RESET (transceiver reset, the transceiver state will automatically |
|  |  |  | end up in state TRXOFF) |


<!-- page 38 -->

5.3     Interrupts

5.3.1   Description
        The AT86RF215 generates in certain scenarios interrupt events (IRQ). Depending on the interrupt configuration, all
        interrupt events (from the sub-1GHz radio, 2.4GHz radio, baseband core 0 and baseband core 1) are combined to a
        single interrupt signal.
        Interrupts can be enabled / disabled for each radio and baseband core separately by the registers RFn_IRQM and
        BBCn_IRQM. After a reset procedure and a wake-up from DEEP_SLEEP procedure, all interrupt sources are disabled
        except the interrupt WAKEUP.
        The pending interrupt event(s) or source(s) can be determined by reading the radio and baseband IRQ status registers
        RFn_IRQS and BBCn_IRQS. Each radio and baseband block provides its own interrupt status register. Altogether there
        are four interrupt status registers.
        The radio interrupt status registers RFn_IRQS indicate interrupt events that are related to radio functionality, such as
        IRQS.TRXERR, IRQS.EDC or IRQS.TRXRDY, or general transceiver functionality, such as IRQS.IQIFSF,
        IRQS.BATLOW, IRQS.WAKEUP. Table 5-5 summarizes the radio interrupts status and refers to sections that provide
        further information about the corresponding interrupt.

        Table 5-5.   Radio Interrupt Status

        Interrupt               Section for further information                  Comment

        IRQS.WAKEUP             "State DEEP_SLEEP and Wake-up                    Returning from the state DEEP_SLEEP, the
                                Procedure" on page 34                            interrupt IRQS.WAKEUP is always set for
                                                                                 both radios together. On the other hand, the
                                                                                 interrupt IRQS.WAKEUP is set only for the
                                                                                 corresponding radio that returns from the
                                                                                 State SLEEP.
                                "Reset Modes " on page 13                        Once a Chip Reset procedure is completed,
                                                                                 the interrupt IRQS.WAKEUP is issued for
                                                                                 both transceivers. A Transceiver Reset
                                                                                 completion is indicated by the interrupt
                                                                                 IRQS.WAKEUP for the corresponding
                                                                                 transceiver only.

        IRQS.TRXRDY             "Frequency Synthesizer (PLL)" on page 62
                                and "State TXPREP" on page 35

        IRQS.EDC                "Energy Measurement" on page 56

        IRQS.BATLOW             "Battery Monitor (BATMON) " on page 78           The IRQ IRQS.BATLOW is issued pair wise,
                                                                                 i.e. this IRQ is always set for both radios
                                                                                 (sub1-GHz and 2.4GHz) at the same time.

        IRQS.TRXERR             "Frequency Synthesizer (PLL)" on page 62

        IRQS.IQIFSF             "Serial I/Q Data Interface" on page 22           Applicable in I/Q radio mode only.




                                                                                     Atmel AT86RF215 - DATASHEET                     38
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 39 -->

        The baseband interrupt status registers BBCn_IRQS indicate interrupt events that are related to frame processing
        functionality. The baseband interrupt status registers BBCn_IRQS do not change if the device is operated in the I/Q
        radio mode. For further information about baseband interrupts see section "Baseband Core" on page 81.
        The IRQ status registers are cleared automatically by reading the corresponding register via SPI. The interrupt status
        registers can be read separately or all IRQ status registers can be read at once using the SPI block mode; see section
        "SPI Transceiver Control Interface" on page 16 for further information about SPI access.
        There can be more than one interrupt event pending at a time. As long as there is any unmasked/enabled interrupt
        reason pending, the pin IRQ is kept active. If the sub-register RF_CFG.IRQMM is set to 1, the interrupt status can be
        read from the interrupt status registers (IRQS), even if the corresponding IRQ is not enabled.

5.3.2   Register Description
5.3.2.1 BBCn_IRQM – Baseband IRQ Mask
        The register BBCn_IRQM contains the baseband IRQ mask. A bit set to 1 enables the corresponding IRQ to cause an
        IRQ pin event. A bit set to 0 disables the corresponding IRQ to cause an IRQ pin event.
        Bit                 7           6           5             4     3       2            1             0
                          FBLI        AGCR        AGCH        TXFE     RXEM   RXAM        RXFE          RXFS            BBCn_IRQM
        Read/Write         RW          RW          RW             RW   RW      RW          RW            RW
        Initial Value       0           0           0             0     0       0            0             0

         Bit 7 – IRQM.FBLI: Frame Buffer Level Indication Interrupt Mask
        If this bit is set to 1, the interrupt FBLI is enabled.

         Bit 6 – IRQM.AGCR: AGC Release Interrupt Mask
        If this bit is set to 1, the interrupt AGCR is enabled.

         Bit 5 – IRQM.AGCH: AGC Hold Interrupt Mask
        If this bit is set to 1, the interrupt AGCH is enabled.

         Bit 4 – IRQM.TXFE: Transmitter Frame End Interrupt Mask
        If this bit is set to 1 the interrupt TXFE is enabled.

         Bit 3 – IRQM.RXEM: Receiver Extended Match Interrupt Mask
        If this bit is set to 1, the interrupt RXEM is enabled.

         Bit 2 – IRQM.RXAM: Receiver Address Match Interrupt Mask
        If this bit is set to 1, the interrupt RXAM is enabled.

         Bit 1 – IRQM.RXFE: Receiver Frame End Interrupt Mask
        If this bit is set to 1, the interrupt RXFE is enabled.

         Bit 0 – IRQM.RXFS: Receiver Frame Start Interrupt Mask
        If this bit is set to 1, the interrut RXFS is enabled.

5.3.2.2 RFn_IRQM – Radio IRQ Mask
        The register RFn_IRQM contains the radio IRQ mask. A bit set to 1 enables the corresponding IRQ to cause an IRQ pin
        event. A bit set to 0 disables the corresponding IRQ to cause an IRQ pin event.




                                                                                    Atmel AT86RF215 - DATASHEET                     39
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 40 -->

        Bit                7           6           5            4         3           2            1             0
                           –           –        IQIFSF     TRXERR     BATLOW        EDC         TRXRDY      WAKEUP             RFn_IRQM
        Read/Write        R           R          RW             RW       RW          RW          RW            RW
        Initial Value      0           0           0            0         0           0            0             1

        Bit 5 – IRQM.IQIFSF: I/Q IF Synchronization Failure Interrupt Mask
       If this bit is set to 1, the interrupt IQIFSF is enabled.

        Bit 4 – IRQM.TRXERR: Transceiver Error Interrupt Mask
       If this bit is set to 1, the interrupt TRXERR is enabled.

        Bit 3 – IRQM.BATLOW: Battery Low Interrupt Mask
       If this bit is set to 1, the interrupt BATLOW is enabled.

        Bit 2 – IRQM.EDC: Energy Detection Completion Interrupt Mask
       If this bit is set to 1, the interrupt EDC is enabled.

        Bit 1 – IRQM.TRXRDY: Transceiver Ready Interrupt Mask
       If this bit is set to 1, the interrupt TRXRDY is enabled.

        Bit 0 – IRQM.WAKEUP: Wake-up / Reset Interrupt Mask
       If this bit is set to 1, the interrupt WAKEUP is enabled. This bit is automatically set to 1 in the states POWER_ON,
       DEEP_SLEEP, SLEEP and RESET.

5.3.2.3 RFn_IRQS – Radio IRQ Status
       The register RFn_IRQS contains the radio IRQ status. A bit set to 1 indicates that the corresponding IRQ has occurred.
       The register is cleared by a read access.
        Bit                7           6           5            4         3           2            1             0
                           –           –        IQIFSF     TRXERR     BATLOW        EDC         TRXRDY      WAKEUP             RFn_IRQS
        Read/Write        R           R           R             R         R           R            R            R
        Initial Value      0           0           0            0         0           0            0             0

        Bit 5 – IRQS.IQIFSF: I/Q IF Synchronization Failure Interrupt
       This bit is set to 1 if the I/Q data interface synchronization fails.

        Bit 4 – IRQS.TRXERR: Transceiver Error Interrupt
       This bit is set to 1 if a transceiver error is detected, i.e. a PLL lock error occurs.

        Bit 3 – IRQS.BATLOW: Battery Low Interrupt
       This bit is set to 1 if the battery monitor detects a voltage at EVDD that is below the threshold voltage.

        Bit 2 – IRQS.EDC: Energy Detection Completion Interrupt
       This bit is set to 1 if a single or continuous energy measurement is completed. It is not set if the automatic energy
       measurement mode is used.




                                                                                          Atmel AT86RF215 - DATASHEET                     40
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 41 -->

        Bit 1 – IRQS.TRXRDY: Transceiver Ready Interrupt
       This bit is set to 1 if the command TXPREP is written to the register RFn_CMD and transceiver reaches the state
       TXPREP. While being in the state TXPREP and changing the RF frequency, the IRQ TRXRDY is issued once the
       frequency settling is completed. Note: It is not set if the baseband switches automatically to the state TXPREP due to
       an IRQ TXFE or RXFE.

        Bit 0 – IRQS.WAKEUP: Wake-up / Reset Interrupt
       This bit is set to 1 if the wake-up procedure from state SLEEP/DEEP_SLEEP or power-up procedure is completed. It
       also indicates the completion of the RESET procedure.

5.3.2.4 BBCn_IRQS – Baseband IRQ Status
       The register BBCn_IRQS contains the baseband IRQ status. A bit set to 1 indicates that the corresponding IRQ has
       occurred. The register is cleared by a read access.
        Bit               7           6           5           4          3             2             1             0
                        FBLI        AGCR       AGCH         TXFE        RXEM          RXAM        RXFE          RXFS            BBCn_IRQS
        Read/Write        R           R           R           R          R             R             R            R
        Initial Value     0           0           0           0          0             0             0             0

        Bit 7 – IRQS.FBLI: Frame Buffer Level Indication Interrupt
       During frame recieve this bit is set to 1 if the number of received bytes is greater than the frame buffer level indication
       (see registers BBCn_FBLIL and BBCn_FBLIH).

        Bit 6 – IRQS.AGCR: AGC Release Interrupt
       This bit is set to 1 if the baseband releases the AGC. The interrupts AGCH and AGCR are exclusive; i.e. only the last
       occurrence of both status bits is indicated. The interrupt AGCR is cleared automatically by the interrupt AGCH.

        Bit 5 – IRQS.AGCH: AGC Hold Interrupt
       This bit is set to 1 if the baseband holds the AGC. The interrupts AGCH and AGCR are exclusive; i.e. only the last
       occurrence of both status bits is indicated. The interrupt AGCH is cleared automatically by the interrupt AGCR.

        Bit 4 – IRQS.TXFE: Transmitter Frame End Interrupt
       This bit is set to 1 if the frame transmission is completed. The state is automatically changed from TX to TXPREP. This
       automatic state change does not cause an IRQ TRXRDY.

        Bit 3 – IRQS.RXEM: Receiver Extended Match Interrupt
       This bit is set to 1 if a received frame matches the extended frame filter rules.

        Bit 2 – IRQS.RXAM: Receiver Address Match Interrupt
       This bit is set to 1 if a received frame matches the 3rd level filter rules.

        Bit 1 – IRQS.RXFE: Receiver Frame End Interrupt
       This bit is set to 1 if frame end is detected. The state is automatically changed from RX to TXPREP. This automatic
       state change does not cause an IRQ TRXRDY.

        Bit 0 – IRQS.RXFS: Receiver Frame Start Interrupt
       This bit is set to 1 if a valid frame start (PHR) is detected.

5.3.2.5 RF_CFG – IRQ Configuration
       The register RF_CFG contains bits to configure the IRQ behavior.




                                                                                           Atmel AT86RF215 - DATASHEET                      41
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 42 -->

      Bit                7            6           5          4         3          2             1             0
      (0x0006)           –            –           –          –       IRQMM      IRQP                 DRV                     RF_CFG
      Read/Write         R            R           R         R         RW         RW           RW            RW
      Initial Value      0            0           0          0         1          0             0             1

       Bit 3 – RF_CFG.IRQMM: IRQ Mask Mode
      The bit IRQMM configures the IRQ mask mode.

      Table 5-6.      IRQMM

      Sub-register            Value       Description
      IRQMM                   0x0         Masked IRQ reasons do not appear in IRQS register
                              0x1         Masked IRQ reasons do appear in IRQS register



5.4   Basic Operation of AT86RF215M
      The AT86RF215M includes the sub-1GHz transceiver only. Generally the registers of the 2.4GHz radio and the
      baseband core 1 must not be accessed. For operation of the AT86RF215M the following aspects must be considered:
            The TRX24 (i.e. RF24, BBC1, RXD24) is not available for chip mode operation (see Table 5-1 on page 30)
            After reset and wakeup from DEEP_SLEEP the interrupt IRQS.WAKEUP is set in the registers RF09_IRQS
             and RF24_IRQS. The IRQ is cleared by reading both registers RFn_IRQS.
            The state DEEP_SLEEP is entered by writing the command SLEEP to the registers RF09_CMD and
             RF24_CMD.
      The pins RFN24/RFP24; RXDN24/RXDP24; FEA24/FEB24 and AVDD1 are not supported (see section "Pin-out
      Diagram and Description" on page 7).




                                                                                       Atmel AT86RF215 - DATASHEET                     42
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| IRQMM | 0x0 | Masked IRQ reasons do not appear in IRQS register |
|  | 0x1 | Masked IRQ reasons do appear in IRQS register |


<!-- page 43 -->

6.      Module Description

6.1     Transmitter Frontend
        For configuration of the transmitter frontend the transceiver must be in the State TRXOFF.

6.1.1   Transmitter Digital Frontend
        The Transmitter Digital Frontend (TX_DFE) performs discrete time sampling rate conversion of the complex baseband
        signal. For this conversion, a zero-intermediate frequency (zero-IF) architecture is applied.
        The TX I/Q input signals are the data words I_DATA[13:0] and Q_DATA[13:0]. The baseband signal data is contained in
        sub-fields I_DATA[13:1] and Q_DATA[13:1] for the in-phase and quadrature signal, respectively. Each sub-field is
        interpreted as a 13-bit two’s complement signed value with {I,Q}_DATA[13] being the sign bit and {I,Q}_DATA[1] being
        the least significant bit. If embedded TX start is used, the control field entry I_DATA[0] can be utilized for a convenient
        PA ramp up control, see section "Transmit Control" on page 46. The control signal embedded in I_DATA[0] is
        automatically delayed according to the processing delay caused by the TX_DFE filter stages, see Figure 6-1. The field
        entry Q_DATA[0] is be set to 0.
        The I/Q data sampling frequency fs is to be configured according to

                                                                             4
                                                                     fs       MHz
                                                                            SR
        where SR is defined by the register TXDFE.SR. The signal processing flow is depicted in Figure 6-1.
        The baseband signal at sampling frequency fs can be pre-filtered at block PRE_FLT. A selection of suitable normalized
        cut-off frequencies fcut (TXDFE.RCUT) is configurable. This filter stage can be utilized to relax interpolation complexity of
        the baseband processor (suppression of unwanted images). For fcut = 1, the block is bypassed, reducing group delay.
        Up-sampling from fs to 4MHz is accomplished by UP_SRC(1:SR), employing a linear phase FIR interpolation filter, with
        normalized cut-off frequency 1/SR.
        Finally, up-sampling to the DAC sampling frequency of 32MHz is accomplished by UP_SRC(1:8), employing three
        stages of linear phase FIR filters with normalized cut-off frequency ½.

        Figure 6-1. TX Up-Sampling and Filtering



                                                  TX_EN                                                                               I_DATA[0]
                              PA_CTRL                                                  Delay



                                                                                                                                      I_DATA[13:1]
                                  DAC                      UP_SRC                  UP_SRC (1:SR)
              LPF                                 @32MHz                                                      PRE_FLT          @fs
         (low pass filter)
                             (digital-to-analog             (1:8)          @4MHz     (up-sampling)             (pre- filter)
                                 converter)                (up-sampling)
                                                                                                                                      Q_DATA[13:1]


                                                            TX_DFE




                                                                                               Atmel AT86RF215 - DATASHEET                        43
                                                                                                 Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 44 -->

        The overall signal processing delay depends on the register settings TXDFE.RCUT and TXDFE.SR as summarized in
        Table 6-1.



        Table 6-1.   Transmit Processing Delay

        TXDFE.RCUT            TXDFE.SR           ttx_proc_delay [µs]
        0,1,2,3                     1                   4.0
                                    2                   8.5
                                    3                  11.0
                                    4                  15.0
                                    5                  18.5
                                    6                  20.5
                                    8                  28.5
                                   10                  34.0
        4                           1                   2.0
                                    2                   4.0
                                    3                  5.25
                                    4                  6.25
                                    5                   8.3
                                    6                   8.5
                                    8                  10.25
                                   10                  13.75


        The low-pass filter (LPF) following the DAC can be configured such that DAC images are sufficiently attenuated, see
        section "Transmitter Analog Frontend" below.

6.1.2   Transmitter Analog Frontend
        The transmitter is based on a direct up-conversion architecture as shown in Figure 1-1 on page 5. After the digital to
        analog converter (DAC) the I-signals and Q-signals are passed through analog 2nd order low-pass filters (LPF). The low-
        pass cut-off frequency can be set by register TXCUTC.LPFCUT. A cut-off frequency range from 80kHz to 1000kHz is
        covered with uniform logarithmic stepping see Figure 6-2. The cut-off frequency setting should be aligned with the
        bandwidth of the transmit signal depending on the data rate and modulation scheme selected, see section "Transceiver
        Usage in Baseband Mode" on page 169.




                                                                                  Atmel AT86RF215 - DATASHEET                      44
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 45 -->

        Figure 6-2. Transmitter Anti-Aliasing Low-Pass Filter Frequency Response

                        0


                        -2

                                                                                                                        BW=0
                        -4
                                                                                                                        BW=1
                                                                                                                        BW=2
                        -6
                                                                                                                        BW=3

                        -8                                                                                              BW=4
                                                                                                                        BW=5

           Gain [dB]
                       -10                                                                                              BW=6
                                                                                                                        BW=7
                       -12                                                                                              BW=8
                                                                                                                        BW=9
                       -14                                                                                              BW=10
                                                                                                                        BW=11
                       -16


                       -18


                       -20
                             10               100                           1000                               10000
                                                         Frequency [kHz]




6.1.3   Power Amplifier
        At transmit start and transmit end, the transmit power is ramped up and down within a specific time period to mitigate
        spurious signal emission in adjacent frequency bands. The power ramp time is adjustable to meet different applications
        and regulatory requirements. Spurious emissions are especially critical at band edges where the adjacent band is a
        restricted band with more stringent requirements. The power amplifier ramp time is adjustable by the sub-register
        TXCUTC.PARAMP. The ramp curve of the power amplifier output magnitude resembles a non-linear curve (half sine
        shaped). The ramp time is independent on the TX power setting.
        The TX power is adjustable with the sub-register PAC.TXPWR in about 1dB steps. The maximum TX power depends
        on the modulation scheme and the crest factor of the transmit signal. The nominal maximum TX power PTX relates to a
        constant envelope modulation scheme like MR-FSK (see "Transmitter Characteristics " on page 190 and "Output Power
        at Several Modulations " on page 208). The maximum (average) transmit power of OFDM signals is about 5.5dB lower
        compared to a constant envelope signal since the OFDM peak power is mapped to the maximum output power that the
        PA can deliver to the load. The average OFDM transmit power is lower due to the signal’s crest factor.
        The bias current of the PA can be adjusted with the sub-register PAC.PACUR to reduce the transmitter supply current if
        lower transmit power settings are used. This feature is useful if the transmitter supply current will be minimized, see "TX
        Current Consumption and Output Power at PAC.PACUR settings" on page 211 for detailed information. The bias
        current stepping includes a transmitter small signal gain step of 1dB. The maximum transmit power is delivered with
        sub-register PAC.PACUR = 3.
        A dedicated voltage regulator provides the power amplifier supply voltage. This supply voltage can be adjusted with the
        sub-register AUXS.PAVC. It is recommended to set the supply voltage to 2.4V (AUXS.PAVC = 2, default) where the
        power amplifier delivers the maximum TX power.




                                                                                     Atmel AT86RF215 - DATASHEET                      45
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 46 -->

6.1.4   Transmit Control
        There are three different methods to control the transmitter:
              Baseband mode
              I/Q radio mode with SPI control
              I/Q radio mode using embedded control


        Baseband Mode
        In the baseband mode (see "Operating Modes" on page 30), the alignment between transmitter signal ramp up/down
        and baseband data is automatically done by the baseband core.
        Figure 6-3 shows the transmit timing diagram. From the state TXPREP, the transmission is started by writing the
        command TX to the register RFn_CMD. The state machine immediately changes to state TX.

        Figure 6-3. Transmitter Control Timing Diagram for Baseband Mode
                      TX Power                                                   PA                                            PA
                      [dBm]                                                     Ramp                                          Ramp

                                 ttx_bb_delay ttx_proc_delay ttx_start_delay   tpa_ramp                                       tpa_ramp

                                                                                                                                            Time

                                                                                                                    ...
              State TX_PREP                                                                TX                                            TX_PREP


        Instruction       CMD=TX

         TX frame                                                                               I/Q Data Samples              Padding



        The actual frame start is delayed by internal processing delays:
              Transmit baseband processing delay ttx_bb_delay, which is PHY mode dependent
              Transmit processing delay ttx_proc_delay, which is dependent of the Transmitter Digital Frontend
              Transmitter start up delay ttx_start_delay .


        The start of the power amplifier ramp is automatically aligned to these delays. Table 6-2 shows the ttx_bb_delay for different
        PHY mode settings.

        Table 6-2.     Transmit Baseband Processing Delay

        PC.PT                       Condition                          ttx_bb_delay [µs]
                                       FSKC1.SRATE = 0                              42
                                       FSKC1.SRATE = 1                              21
                                       FSKC1.SRATE = 2                              19
               1 MR-FSK
                                       FSKC1.SRATE = 3                              11
                                       FSKC1.SRATE = 4                              9.5
                                       FSKC1.SRATE = 5                              5.5
              2 MR-OFDM                                                            <3.5
              3 MR-OQPSK                                                           <3.0




                                                                                                           Atmel AT86RF215 - DATASHEET                     46
                                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 47 -->

I/Q Radio Mode
In the I/Q radio mode, the alignment between the PA ramp and baseband data has to be controlled by the external
microcontroller see "Word Format" on page 24.
Figure 6-4 shows the timing of control signals to start and end the transmit process including the data samples applied
to the serial I/Q data interface. The transceiver must be in state TXPREP before transmission can be started.



Figure 6-4. Transmitter Control Timing Diagram for I/Q Radio Mode

                TX Power                                       PA                                            PA
                [dBm]                                         Ramp                                          Ramp

                           ttx_proc_delay ttx_start_delay tpa_ramp                            ttx_proc_delay tpa_ramp

                                                                                                                             Time


State                TX_PREP                                             TX                                             TX_PREP


Instruction                       CMD=TX                                                          CMD=TX_PREP                     EEC=0

I_DATA[0]                                                                                                                         EEC=1

                 Internal Delay
                                                       TX Start (delayed)

I/Q-Interface          Zero Samples                          I/Q Data Samples                 Padding

    Processing Delay                   Zero Samples              I/Q Data Samples (delayed)                Padding


                                             ttx_start_delay - ttx_proc_delay
              Legend:
                    External Signals
                    Internal Signals



In order to start transmitting, either the SPI command RFn_CMD=TX (while RF_IQIFC0.EEC=0) or the embedded
control (i.e. RF_IQIFC0.EEC=1) in the I/Q data stream I_DATA[0]=1 can be used. When transmitting is started, zero
samples are sent at the serial I/Q data interface. The I/Q data samples of the I/Q data interface are subject to
processing delay ttx_proc_delay (see Table 6-1 on page 44). In order to make the timing between TX start signal and I/Q
data samples independent from this processing delay, the embedded TX start signal is internally delayed by the same
time as the processing delay. The begin of the PA ramp-up is delayed by ttx_start_delay (see Table 10-7 on page 189).
Consequently, the TX start signal has to appear ttx_start_delay earlier than the I/Q data samples if it is desired that the PA
ramp fades the TX signal magnitude.
Note, that the TX start signal is not delayed by ttx_proc_delay if the SPI command is used. Consequently, the time between
the SPI command and the begin of the data samples is ttx_start_delay - ttx_proc_delay which may be positive or negative
depending on the processing delay of the TX digital frontend.
The transmit process can be finished by the SPI command CMD.CMD=TXPREP if embedded control is not enabled
(RF_IQIFC0.EEC=0). Alternatively, if embedded control is enabled (RF_IQIFC0.EEC=1), the transmit process is
stopped if the embedded control bit in the I/Q data stream is zero (I_DATA[0]=0).
The beginning of the PA ramp-down is delayed by ttx_proc_delay to align it with the I/Q data samples. It is advisable to add
padding samples in the I/Q data stream to provide a non-zero signal amplitude during PA ramp down.
The usage of the transmitter control in I/Q radio mode is also described in the section "Transmitter Usage in I/Q Radio
Mode " on page 178.



                                                                                                     Atmel AT86RF215 - DATASHEET                       47
                                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 48 -->

6.1.5   Register Description
6.1.5.1 RFn_TXCUTC – Transmitter Filter Cutoff Control and PA Ramp Time
        The register configures the transmitter filter and PA ramp time.
        Bit                7            6        5             4           3           2             1             0
                               PARAMP             –            –                            LPFCUT                             RFn_TXCUTC
        Read/Write        RW         RW          R             R         RW            RW            RW          RW
        Initial Value      0            0        0             0           1           0             0             0

         Bit 7:6 – TXCUTC.PARAMP: Power Amplifier Ramp Time
        The sub-register configures the ramp up/down time of the power amplifier.

        Table 6-3.      PARAMP

        Sub-register        Name                        Value       Description
        PARAMP              RF_PARAMP4U                  0x0        tpa_ramp = 4μs
                            RF_PARAMP8U                  0x1        tpa_ramp = 8μs
                            RF_PARAMP16U                 0x2        tpa_ramp = 16μs
                            RF_PARAMP32U                 0x3        tpa_ramp = 32μs

         Bit 3:0 – TXCUTC.LPFCUT: Transmitter cut-off frequency
        The sub-register configures the transmitter low pass filter cut-off frequency.

        Table 6-4.      LPFCUT

        Sub-register        Name                        Value       Description
        LPFCUT              RF_FLC80KHZ                  0x0        fLPFCUT = 80kHz
                            RF_FLC100KHZ                 0x1        fLPFCUT = 100kHz
                            RF_FLC125KHZ                 0x2        fLPFCUT = 125kHz
                            RF_FLC160KHZ                 0x3        fLPFCUT = 160kHz
                            RF_FLC200KHZ                 0x4        fLPFCUT = 200kHz
                            RF_FLC250KHZ                 0x5        fLPFCUT = 250kHz
                            RF_FLC315KHZ                 0x6        fLPFCUT = 315kHz
                            RF_FLC400KHZ                 0x7        fLPFCUT = 400kHz
                            RF_FLC500KHZ                 0x8        fLPFCUT = 500kHz
                            RF_FLC625KHZ                 0x9        fLPFCUT = 625kHz
                            RF_FLC800KHZ                 0xA        fLPFCUT = 800kHz
                            RF_FLC1000KHZ                0xB        fLPFCUT = 1000kHz

6.1.5.2 RFn_TXDFE – Transmitter TX Digital Frontend
        The register configures the transmitter digital frontend.
        Bit                7            6        5             4           3           2             1             0
                                    RCUT                    DM                               SR                                 RFn_TXDFE
        Read/Write        RW         RW         RW          RW           RW            RW            RW          RW
        Initial Value      0            0        0             0           0           0             0             1

         Bit 7:5 – TXDFE.RCUT: TX filter relative to the cut-off frequency
        The sub-register configures where the relative cut-off frequency fCUT is set; where 1.0 refers to half the TXDFE sample
        frequency fS.




                                                                                            Atmel AT86RF215 - DATASHEET                     48
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| PARAMP | RF_PARAMP4U | 0x0 | tpa_ramp = 4μs |
|  | RF_PARAMP8U | 0x1 | tpa_ramp = 8μs |
|  | RF_PARAMP16U | 0x2 | tpa_ramp = 16μs |
|  | RF_PARAMP32U | 0x3 | tpa_ramp = 32μs |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| LPFCUT | RF_FLC80KHZ | 0x0 | fLPFCUT = 80kHz |
|  | RF_FLC100KHZ | 0x1 | fLPFCUT = 100kHz |
|  | RF_FLC125KHZ | 0x2 | fLPFCUT = 125kHz |
|  | RF_FLC160KHZ | 0x3 | fLPFCUT = 160kHz |
|  | RF_FLC200KHZ | 0x4 | fLPFCUT = 200kHz |
|  | RF_FLC250KHZ | 0x5 | fLPFCUT = 250kHz |
|  | RF_FLC315KHZ | 0x6 | fLPFCUT = 315kHz |
|  | RF_FLC400KHZ | 0x7 | fLPFCUT = 400kHz |
|  | RF_FLC500KHZ | 0x8 | fLPFCUT = 500kHz |
|  | RF_FLC625KHZ | 0x9 | fLPFCUT = 625kHz |
|  | RF_FLC800KHZ | 0xA | fLPFCUT = 800kHz |
|  | RF_FLC1000KHZ | 0xB | fLPFCUT = 1000kHz |


<!-- page 49 -->

       Table 6-5.       RCUT

        Sub-register             Value        Description
        RCUT                     0x0          fCUT=0.25 *fS/2
                                 0x1          fCUT=0.375*fS/2
                                 0x2          fCUT=0.5 *fS/2
                                 0x3          fCUT=0.75 *fS/2
                                 0x4          fCUT=1.00 *fS/2

        Bit 4 – TXDFE.DM: Direct Modulation
       If this sub-register is set to 1 the transmitter direct modulation is enabled. Direct modulation is available for FSK and
       OQPSK (OQPSKC0.FCHIP=0;1). Direct modulation must also be enabled at the BBCx registers (FSKDM.EN and
       OQPSKC0.DM).

        Bit 3:0 – TXDFE.SR: TX Sample Rate
       The sub-register configures the sampling frequency of the incoming transmit signal. Undefined values are mapped to
       the default setting of fS=4000kHz.

       Table 6-6.       SR

        Sub-register             Value        Description
        SR                       0x1          fS=4000kHz
                                 0x2          fS=2000kHz
                                 0x3          fS=(4000/3)kHz
                                 0x4          fS=1000kHz
                                 0x5          fS=800kHz
                                 0x6          fS=(2000/3)kHz
                                 0x8          fS=500kHz
                                 0xA          fS=400kHz

6.1.5.3 RFn_PAC – Transmitter Power Amplifier Control
       The register sets the transmitter output power and controls the power amplifier bias current.
        Bit                  7           6             5        4      3          2            1             0
                             –                PACUR                            TXPWR                                       RFn_PAC
        Read/Write           R           RW           RW        RW    RW         RW          RW            RW
        Initial Value        0           1             1        1      1          1            1             1

        Bit 6:5 – PAC.PACUR: Power Amplifier Current Control
       PACUR configures the power amplifier DC current (useful for low power settings).




                                                                                      Atmel AT86RF215 - DATASHEET                     49
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| RCUT | 0x0 | fCUT=0.25 *fS/2 |
|  | 0x1 | fCUT=0.375*fS/2 |
|  | 0x2 | fCUT=0.5 *fS/2 |
|  | 0x3 | fCUT=0.75 *fS/2 |
|  | 0x4 | fCUT=1.00 *fS/2 |

| Sub-register | Value | Description |
| --- | --- | --- |
| SR | 0x1 | fS=4000kHz |
|  | 0x2 | fS=2000kHz |
|  | 0x3 | fS=(4000/3)kHz |
|  | 0x4 | fS=1000kHz |
|  | 0x5 | fS=800kHz |
|  | 0x6 | fS=(2000/3)kHz |
|  | 0x8 | fS=500kHz |
|  | 0xA | fS=400kHz |


<!-- page 50 -->

       Table 6-7.       PACUR

        Sub-register            Value        Description
        PACUR                    0x0         Power amplifier current reduction by about 22mA (3dB reduction of max. small signal gain)
                                 0x1         Power amplifier current reduction by about 18mA (2dB reduction of max. small signal gain)
                                 0x2         Power amplifier current reduction by about 11mA (1dB reduction of max. small signal gain)
                                 0x3         No power amplifier current reduction (max. transmit small signal gain)

        Bit 4:0 – PAC.TXPWR: Transmitter Output Power
       TXPWR controls the transmit output power setting. Maximum output power is TXPWR=31, minimum output power is
       TXPWR=0. The output power can be set by about 1dB step resolution. Refer to section "Output Power" in section
       "Typical Characteristics" for detailed output power information and charts.

       Table 6-8.       TXPWR

        Sub-register            Value        Description
        TXPWR                    0x00        minimum output power
                                  ...        about 1dB steps
                                 0x1F        maximum output power

6.1.5.4 RFn_AUXS – Transceiver Auxiliary Settings
       The register controls transceiver auxiliary settings.
        Bit                7            6             5            4         3          2             1             0
                        EXTLNAB
                                            AGCMAP               AVEXT    AVEN         AVS                PAVC                   RFn_AUXS
                           YP
        Read/Write        RW            RW          RW            RW        RW          R           RW            RW
        Initial Value      0            0             0            0         0          0             1             0

        Bit 1:0 – AUXS.PAVC: Power Amplifier Voltage Control
       The sub-register controls the supply voltage of the internal power amplifier.

       Table 6-9.       PAVC

        Sub-register            Value        Description
        PAVC                     0x0         2.0V
                                 0x1         2.2V
                                 0x2         2.4V

6.1.5.5 RF_IQIFC0 – Transceiver I/Q Data Interface Configuration Register 0
       The register configures the I/Q data interface.
        Bit                7            6             5            4         3          2             1             0
        (0x000A)         EXTLB          SF                 DRV                   CMV              CMV1V2          EEC             RF_IQIFC0
        Read/Write        RW            R           RW            RW        RW         RW           RW            RW
        Initial Value      0            0             0            1         0          1             0             0

        Bit 0 – RF_IQIFC0.EEC: I/Q IF Enable Embedded TX Start Control
       The bit enables the ability to start and finish transmitting by a control bit within the I/Q data stream (I_DATA[0]). If this bit
       is set to 1, the transmit start and finish cannot be controlled by SPI commands.




                                                                                             Atmel AT86RF215 - DATASHEET                      50
                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| PACUR | 0x0 | Power amplifier current reduction by about 22mA (3dB reduction of max. small signal gain) |
|  | 0x1 | Power amplifier current reduction by about 18mA (2dB reduction of max. small signal gain) |
|  | 0x2 | Power amplifier current reduction by about 11mA (1dB reduction of max. small signal gain) |
|  | 0x3 | No power amplifier current reduction (max. transmit small signal gain) |

| Sub-register | Value | Description |
| --- | --- | --- |
| TXPWR | 0x00 | minimum output power |
|  | ... | about 1dB steps |
|  | 0x1F | maximum output power |

| Sub-register | Value | Description |
| --- | --- | --- |
| PAVC | 0x0 | 2.0V |
|  | 0x1 | 2.2V |
|  | 0x2 | 2.4V |


<!-- page 51 -->

Table 6-10. EEC

Sub-register      Value   Description
EEC               0x0     Embedded control is not enabled.
                  0x1     Embedded control is enabled.




                                                             Atmel AT86RF215 - DATASHEET                     51
                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| EEC | 0x0 | Embedded control is not enabled. |
|  | 0x1 | Embedded control is enabled. |


<!-- page 52 -->

6.2     Receiver Frontend
        For configuration of the receiver frontend the transceiver must be in the State TRXOFF.

6.2.1   Receiver Analog Frontend
        After passing a low-noise amplifier (LNA) the received signal is down-converted to a low intermediate frequency (IF). A
        variable IF in combination with variable band-pass filtering provides flexibility with respect to channel selection at
        different channel spacing. In addition to the analog channel filter, there is an digital channel filter after the ADC which is
        described in section "Receiver Digital Frontend".
        The band-pass filter frequency response follows a 2nd order Butterworth characteristic (see Figure 6-5) and provides
        adjacent channel signal attenuation prior to the analog to digital conversion. The band-pass filter 3dB cut-off frequency
        can be set by sub-register RXBWC.BW which also sets the used IF. Three different bandwidth settings are possible for
        each IF. The range from 160kHz to 2000kHz is covered with uniform logarithmic stepping.

        Figure 6-5. Receiver Analog Band-Pass Filter Frequency Response


                        0


                        -2


                        -4

                                                                                                                             BW=0
                        -6                                                                                                   BW=1
                                                                                                                             BW=2
                        -8
                                                                                                                             BW=3


           Gain [dB]
                                                                                                                             BW=4
                       -10
                                                                                                                             BW=5
                                                                                                                             BW=6
                       -12
                                                                                                                             BW=7
                                                                                                                             BW=8
                       -14
                                                                                                                             BW=9

                       -16                                                                                                   BW=10
                                                                                                                             BW=11

                       -18


                       -20
                             0   500   1000       1500        2000         2500    3000        3500         4000
                                                         Frequency [kHz]



        Independent of the bandwidth setting of the band-pass filter, the IF can be increased by a factor of 1.25 by setting sub-
        register RXBWC.IFS to 1. This leads to a set of IF values of 320, 640, 1250 and 2500kHz. The increased IF allows the
        receiver to adapt to different channel schemes.



                                                                                       Atmel AT86RF215 - DATASHEET                       52
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 53 -->

        Both, the bandwidth and the IF shift setting, do not only determine the IF of the band-pass filter, but also switches the
        PLL to the frequency needed to run the receiver on the selected IF frequency. No extra PLL settings are necessary in
        regards to the IF.

6.2.2   Receiver Digital Frontend
        The purpose of the Receiver Digital Frontend (RX_DFE) is discrete time sampling rate conversion of the complex
        baseband signal at the I/Q ADC interface. In addition, Automatic Gain Control (AGC) and estimation of the Received
        Signal Strength Indicator (RSSI) are provided by the RX_DFE. The signal processing flow is depicted in Figure 6-6.
        The analog to digital converter (ADC) provides the raw data of the complex low-IF baseband signal at a sampling
        frequency of 32MHz. At a first stage, the raw data is down-sampled to the sampling frequency of 4MHz (block
        DOWN_SRC(1:8)) and converted to zero-IF (DOWN_MIX). Depending on the configuration register RXDFE.SR, the
        signal is further down-sampled to the target receive sampling frequency:

                                                                                    4
                                                                            fs       MHz
                                                                                   SR
        This is accomplished by block DOWN_SRC(1:SR), employing a linear phase FIR decimation filter with normalized cut-
        off frequency 1/SR.
        The discrete time baseband signal can be further filtered by block POST_FLT. A selection of suitable normalized cut-off
        frequencies fcut (RXDFE.RCUT) is available. This filter can be used for attenuation of out-of-band signals (such as
        adjacent channels).
        The AGC can be configured such that either the baseband signal prior to POST_FLT (signal x1) or the output signal of
        POST_FLT (signal x0) is used for power estimation, see Figure 6-6. This is described in more detail in the section
        "Automatic Gain Control (AGC)" below.
        The RX I/Q output interface consists of data words I_DATA[13:0] and Q_DATA[13:0]. The actual baseband signal data
        of the in-phase and quadrature signals is contained in sub-fields I_DATA[13:1] and Q_DATA[13:1], respectively. Each
        sub-field is interpreted as a 13-bit two’s complement signed value with {I,Q}_DATA[13] being the sign bit and
        {I,Q}_DATA[1] being the least significant bit. The field entries {I,Q}_DATA[0] are reserved bits and set to 0.

        Figure 6-6. RX Down-Sampling and Filtering




                                                                                                                                            (I_DATA[13:1],0)
                      BPF          ADC                  DOWN_SRC (1:8)
                      (band      (analog-to-              (down-sampling)             DOWN_SRC (1:SR)                 POST_FLT
        LNA                                    @32MHz                         @4MHz                             @fs
                       pass         digital-              DOWN_MIX                      (down-sampling)                (post filter)
                       filter)    converter)               (down mixer)
                                                                                                                                           (Q_DATA[13:1],0)




                                                                          RSSI                                 x1
                                                                                             AGC

                                                                          GCW
                                                                                                               x0
                                                 RX_DFE




6.2.3   Automatic Gain Control (AGC)
        The Automatic Gain Control (AGC) of the AT86RF215 is a discrete time regulation loop.




                                                                                                     Atmel AT86RF215 - DATASHEET                               53
                                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 54 -->

As shown in Figure 6-6, either the variance of the signal x1 (AGCC.AGCI set to 1) or the variance of the signal x0
(AGCC.AGCI set to 0) is measured and compared with a target variance. If the control loop is enabled (sub-register
AGCC.EN is set to 1), the gain of the LNA is set to aim for a vanishing control deviation. Figure 6-7 illustrates the
update process of the AGC.

Figure 6-7. AGC Update Process

                           Tu
                  Tw                    Ta


                  WAIT               AVERAGE                WAIT               AVERAGE




                                               GCW[4:0]
                                               RSSI[7:0]


Initially, the AGC performs a wait period for the duration Tw. This wait period is required to assure sufficient settling time
of the LNA gain changes through the whole receive path. In addition, the variance of the reference signal is estimated
by averaging complex magnitude values over time Ta. The averaging duration can be configured by the sub-register
AGCC.AVGS which depends on the sampling frequency specified by the sub-register RXDFE.SR. At the end of each
update period, a new gain control word GCW is stored in the register AGCS.GCW. The gain control word GCW can
take discrete values from {0,1,…,gmax}, where each step corresponds to 3dB receiver gain change. As shown in Table
6-11, the maximum value gmax depends on the sub-register setting RXBWC.BW, see section "Receiver Analog
Frontend" on page 52.

Table 6-11. AGC Maximum Gain Control Value

RXBWC.BW                                                         gmax
0x0, 0x1, 0x2                                                    21
0x3, 0x4, 0x5                                                    21
0x6, 0x7, 0x8                                                    22
0x9, 0xA, 0xB                                                    23


It is recommended using the reference signal x0 after filtering (AGCC.AGCI set to 0), since POST_FLT reduces signal
parts of possibly adjacent channels. However, the disadvantage compared to the usage of reference signal x1 is, that
time Tw is larger (due to the group-delay of POST_FLT) and as a consequence, the overall AGC update period takes
longer. For details, refer to Table 6-12.
The update of the gain control word GCW and, consequently, feedback to the LNA can be suspended by freezing the
AGC (sub-register AGCC.FRZC set to 1). This is usually desirable if a preamble has been detected and the data path
should not be further impacted by LNA gain changes. If the baseband core is enabled, the AT86RF215 automatically
takes care of AGC freeze and its release, see section "Baseband Core" on page 81. In this case, information on AGC
freeze and AGC release can be observed by the sub-register AGCC.FRZS and the interrupt signals AGCH and AGCR,
respectively, see section "Interrupts" on page 38.
The AGC target value can be configured by the sub-register AGCS.TGT. A low AGC target value is usually
recommended, since it improves robustness against adjacent channel interferers. However, a low target value
decreases the signal to noise ratio (SNR) of the data path and the residual dynamic range with respect to deep fades.




                                                                               Atmel AT86RF215 - DATASHEET                     54
                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 55 -->

If the AGC is not enabled (AGCC.EN=0), the receiver gain can be directly controlled by writing to the sub-register
AGCS.GCW.
Since the dynamic range of the receiver is limited to the number of gain steps, the AGC target level cannot be reached
for all receive input power levels. Therefore, an external baseband processor should be capable of utilizing the entire
dynamic range of the ADC. Note, that the sub-cores of the baseband (see section "Baseband Core" on page 81)
contain a specific normalization unit to achieve that.
Table 6-12 summarizes the update time Tu as a function of the sub-register settings AGCC.AGCI, RXDFE.SR and
AGCC.AVGS.

Table 6-12. AGC Update Time Tu in µs for AGCC.AGCI={1}/{0}

AGCC.AVGS        RXDFE.SR
                 10            8            6              5               4             3                 2               1
0                45/65         42/48        31.5/43.5      26.25/36.25     21/29         15.75/21.75       10.5/14.5       6.75/8.75
1                65/85         58/74        43.5/55.5      36.25/46.25     29/37         21.75/27.75       14.5/18.5       8.75/10.75
2                105/125       90/106       67.5/79.5      56.25/66.25     45/53         33.75/39.75       22.5/26.5       12.75/14.75
3                185/205       154/170      115.5/127.5    96.25/106.25    77/85         57.75/63.75       38.5/42.5       20.75/22.75


The AT86RF215 supports operation with an external LNA. In this case, the behavior of the AGC depends on the ability
to bypass the external LNA. If the external LNA can be bypassed (AUXS.EXTLNABYP is set to 1), the gain of the
internal LNA is reduced by the amount of the external LNA gain (9dB if AUXS.AGCMAP is set to 1, 12dB if
AUXS.AGCMAP is set to 2) in case GCW > 17. For GCW ≤ 17, the external LNA is bypassed and the internal LNA
operates as usual. If the external LNA cannot be bypassed (AUXS.EXTLNABYP is set to 0), the AGC accommodates
the gain of the external LNA if applicable. Note, that in this case, the tolerance with regard to the receiver maximum
input level is reduced by the amount of gain of the external LNA, see "External Frontend Control" on page 70.
Radio Signal Strength Indicator (RSSI)
Irrespective of the AGC freeze, the update process (Figure 6-7) is continued in order to update the RSSI value which is
an estimate of the current receive power in dBm with values from {-127,-126,…,3,4}. This value is stored to the sub-
register RFn_RSSI. A value of 127 indicates an invalid RSSI value.
After reaching state RX, a time tRX_RSSI has to elapse until the first valid RSSI value is available. The time tRX_RSSI is listed
in Table 6-13 and can be calculated by:
                                                tRX_RSSI = 8.0µs · RXDFE.SR + Tu.

Table 6-13. Time tRX_RSSI in µs until valid RSSI values available after reaching state RX (for AGCC.AGCI={1}/{0})

AGCC.AVGS        RXDFE.SR
                 10           8            6              5                4             3                 2               1
0                125/145      106/112      79.5/91.5      66.25/76.25      53/61         39.75/45.75       26.5/30.5       14.75/16.75
1                145/165      122/138      91.5/103.5     76.25/86.25      61/69         45.75/51.75       30.5/34.5       16.75/18.75
2                185/205      154/170      115.5/127.5    96.25/106.25     77/85         57.75/63.75       38.5/42.5       20.75/22.75
3                265/285      218/234      163.5/175.5    136.25/146.25    109/117       81.75/87.75       54.5/58.5       28.75/30.75




                                                                                 Atmel AT86RF215 - DATASHEET                       55
                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 56 -->

6.2.4   Energy Measurement
        The energy measurement module can be used as part of a channel selection algorithm, such as energy detection (ED)
        scan procedure, or as part of a clear channel assessment procedure (CCA). The AT86RF215 energy detection module
        is characterized by:
             Wide measurement range
             1dB resolution
             Three different energy measurement modes
             Configurable energy detection averaging duration
             Current Received Signal Strength Indicator (RSSI) value
        The AGC module forms the basis for the energy measurement module. For further information see section "Automatic
        Gain Control (AGC)" on page 53. If the receiver is enabled (State RX), the AGC measures the energy on the configured
        channel and the result is stored to the register RFn_RSSI.
        The provided RSSI values are used by the energy measurement module to generate an average value.
        The energy measurement module supports three different modes
             Automatic measurement (default mode)
             Single measurement
             Continuous measurement.
        The desired measurement mode is configured in register RFn_EDC. For all measurement modes, the measurement
        averaging duration is set by register RFn_EDD. The averaging duration should be greater than the minimum AGC
        update time, see Table 6-12 on page 55 for further information. Measurements are only executed if the transceiver is in
        the State RX.


        Automatic Measurement Mode
        Using the baseband mode in the automatic measurement mode, an energy measurement is triggered automatically by
        the baseband for an incoming frame. Once the baseband holds the AGC, the measurement period is started. In case
        the ongoing frame reception is cancelled by the internal baseband or by leaving the state RX, the energy measurement
        is cancelled as well. The internal baseband cancels the measurement if it detects that the received frame is invalid or if
        the frame end is detected. If the measurement is completed, the averaging result can be read from the register
        RFn_EDV and is valid until the next interrupt IRQS.RXFS. For a cancelled measurement the register RFn_EDV
        contains either an incorrect value or an invalid value, i.e. 127. Following this approach, for each completely received
        frame an energy value is available, the end of the automatically triggered measurement is not signaled by the interrupt
        IRQS.EDC.
        The automatic measurement mode can also be used in the I/Q radio mode. The energy measurement is triggered by
        setting the bit AGCC.FRZC to 1. After the completion of the measurement period (RFn_EDD), the result can be read
        from the register RFn_EDV. If the bit AGCC.FRZC is set to 0 while the measurement duration is not completed, the
        measurement is stopped and the result is invalid.


        Single and Continuous Measurement Mode
        If energy measurement shall be started independent from frame reception in the baseband mode or I/Q radio mode, the
        single or continuous measurement mode can be used. For example, the single measurement mode can be used for a
        single measurement period as required during the CCA procedure. The continuous measurement mode can be used for
        a series of measurement cycles as required for an ED scan.




                                                                                     Atmel AT86RF215 - DATASHEET                     56
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 57 -->

        If the single or continuous measurement mode is used in the baseband mode, it is recommended to disable the
        baseband before entering the State RX to avoid any frame detection/decoding by the baseband during the
        measurement period. The baseband is disabled by setting bit PC.BBEN to 0.
        Before the energy measurement can be started, the radio needs to be in the State RX. The measurement is triggered
        by writing the value 1 (for single mode) or 2 (for continuous mode) to the sub-register EDC.EDM.
        Once the measurement averaging period is completed in the single or continuous mode, the interrupt IRQS.EDC is
        issued and the measurement result can be read from the register RFn_EDV. The result is valid until a next
        measurement is started.
        The single measurement mode ends with issuing the interrupt IRQS.EDC and the energy detection mode is reset
        automatically to its default value (automatic mode). If the baseband is enabled, an incoming signal may trigger an
        automatic ED measurement and the previous measured ED value stored in the register RFn_EDV is updated.
        In the continuous measurement mode, the measurement is not stopped with the completion of the first measurement
        period. It continues with measuring periods until the energy detection mode value (RFn_EDC) is set to 0 or the state RX
        is left. Every time the measurement averaging period is completed, the result is stored to the register RFn_EDV and the
        interrupt IRQS.EDC is issued. If a previous result is not read before the next measurement period provides the next
        result, the previous register value is overwritten. The default measurement mode (i.e. automatic mode) is set
        automatically if the continuous mode is stopped by leaving the State RX.

6.2.5   Register Description
6.2.5.1 RFn_RXBWC – Receiver Filter Bandwidth Control
        The register configures the receiver filter settings.
        Bit                7           6          5             4       3          2            1             0
                           –           –          IFI           IFS                     BW                                RFn_RXBWC
        Read/Write         R          R          RW             RW     RW         RW          RW            RW
        Initial Value      0           0          0             0       1          0            1             1

         Bit 5 – RXBWC.IFI: IF Inversion
        A value of one configures the receiver to implement the inverted-sign IF frequency. Use default setting for normal
        operation.

         Bit 4 – RXBWC.IFS: IF Shift
        A value of one configures the receiver to shift the IF frequency by factor of 1.25. This is useful to place the image
        frequency according to channel scheme.

         Bit 3:0 – RXBWC.BW: Receiver Bandwidth
        The sub-register controls the receiver filter bandwidth settings.




                                                                                       Atmel AT86RF215 - DATASHEET                     57
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 58 -->

       Table 6-14. BW

        Sub-register      Name                              Value     Description
        BW                RF_BW160KHZ_                      0x0       fBW=160kHz; fIF=250kHz
                          IF250KHZ
                          RF_BW200KHZ_                      0x1       fBW=200kHz; fIF=250kHz
                          IF250KHZ
                          RF_BW250KHZ_                      0x2       fBW=250kHz; fIF=250kHz
                          IF250KHZ
                          RF_BW320KHZ_                      0x3       fBW=320kHz; fIF=500kHz
                          IF500KHZ
                          RF_BW400KHZ_                      0x4       fBW=400kHz; fIF=500kHz
                          IF500KHZ
                          RF_BW500KHZ_                      0x5       fBW=500kHz; fIF=500kHz
                          IF500KHZ
                          RF_BW630KHZ_                      0x6       fBW=630kHz; fIF=1000kHz
                          IF1000KHZ
                          RF_BW800KHZ_                      0x7       fBW=800kHz; fIF=1000kHz
                          IF1000KHZ
                          RF_BW1000KHZ_                     0x8       fBW=1000kHz; fIF=1000kHz
                          IF1000KHZ
                          RF_BW1250KHZ_                     0x9       fBW=1250kHz; fIF=2000kHz
                          IF2000KHZ
                          RF_BW1600KHZ_                     0xA       fBW=1600kHz; fIF=2000kHz
                          IF2000KHZ
                          RF_BW2000KHZ_                     0xB       fBW=2000kHz; fIF=2000kHz
                          IF2000KHZ

6.2.5.2 RFn_RXDFE – Receiver Digital Frontend
       The register configures the receiver digital frontend.
        Bit              7           6             5              4        3          2            1             0
                                    RCUT                          –                        SR                                 RFn_RXDFE
        Read/Write      RW           RW           RW              R       RW         RW          RW            RW
        Initial Value    0           0             0              0        0          0            0             1

        Bit 7:5 – RXDFE.RCUT: RX filter relative cut-off frequency
       The sub-register configures the relative cut-off frequency fCUT; where 1.0 refers to half the sample frequency fS.

       Table 6-15. RCUT

        Sub-register         Value        Description
        RCUT                  0x0         fCUT=0.25 *fS/2
                              0x1         fCUT=0.375*fS/2
                              0x2         fCUT=0.5 *fS/2
                              0x3         fCUT=0.75 *fS/2
                              0x4         fCUT=1.00 *fS/2

        Bit 3:0 – RXDFE.SR: RX Sample Rate
       The sub-register configures the sampling frequency of the received signal. Undefined values are mapped to default
       setting fS=4000kHz.




                                                                                          Atmel AT86RF215 - DATASHEET                     58
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| BW | RF_BW160KHZ_ | 0x0 | fBW=160kHz; fIF=250kHz |
|  | IF250KHZ |  |  |
|  | RF_BW200KHZ_ | 0x1 | fBW=200kHz; fIF=250kHz |
|  | IF250KHZ |  |  |
|  | RF_BW250KHZ_ | 0x2 | fBW=250kHz; fIF=250kHz |
|  | IF250KHZ |  |  |
|  | RF_BW320KHZ_ | 0x3 | fBW=320kHz; fIF=500kHz |
|  | IF500KHZ |  |  |
|  | RF_BW400KHZ_ | 0x4 | fBW=400kHz; fIF=500kHz |
|  | IF500KHZ |  |  |
|  | RF_BW500KHZ_ | 0x5 | fBW=500kHz; fIF=500kHz |
|  | IF500KHZ |  |  |
|  | RF_BW630KHZ_ | 0x6 | fBW=630kHz; fIF=1000kHz |
|  | IF1000KHZ |  |  |
|  | RF_BW800KHZ_ | 0x7 | fBW=800kHz; fIF=1000kHz |
|  | IF1000KHZ |  |  |
|  | RF_BW1000KHZ_ | 0x8 | fBW=1000kHz; fIF=1000kHz |
|  | IF1000KHZ |  |  |
|  | RF_BW1250KHZ_ | 0x9 | fBW=1250kHz; fIF=2000kHz |
|  | IF2000KHZ |  |  |
|  | RF_BW1600KHZ_ | 0xA | fBW=1600kHz; fIF=2000kHz |
|  | IF2000KHZ |  |  |
|  | RF_BW2000KHZ_ | 0xB | fBW=2000kHz; fIF=2000kHz |
|  | IF2000KHZ |  |  |

| Sub-register | Value | Description |
| --- | --- | --- |
| RCUT | 0x0 | fCUT=0.25 *fS/2 |
|  | 0x1 | fCUT=0.375*fS/2 |
|  | 0x2 | fCUT=0.5 *fS/2 |
|  | 0x3 | fCUT=0.75 *fS/2 |
|  | 0x4 | fCUT=1.00 *fS/2 |


<!-- page 59 -->

       Table 6-16. SR

       Sub-register            Value        Description
       SR                       0x1         fS=4000kHz
                                0x2         fS=2000kHz
                                0x3         fS=(4000/3)kHz
                                0x4         fS=1000kHz
                                0x5         fS=800kHz
                                0x6         fS=(2000/3)kHz
                                0x8         fS=500kHz
                               0xA          fS=400kHz

6.2.5.3 RFn_AGCC – Receiver AGC Control 0
       The register controls the transceiver automatic gain control (AGC).
       Bit                7            6            5           4         3           2            1             0
                           –          AGCI               AVGS            RST        FRZS        FRZC            EN            RFn_AGCC
       Read/Write        RW            RW          RW           RW       RW           R          RW            RW
       Initial Value      1            0            0           0         0           0            0             1

        Bit 6 – AGCC.AGCI: AGC Input
       This bit controls the input signal of the AGC. If this bit is zero, the filtered (after channel filter) front end signal is used.
       Otherwise the unfiltered signal is used which enables the AGC to settle faster.

        Bit 5:4 – AGCC.AVGS: AGC Average Time in Number of Samples
       The time of averaging RX data samples for the AGC values is defined by number of samples.

       Table 6-17. AVGS

       Sub-register            Value        Description
       AVGS                     0x0         8 samples
                                0x1         16 samples
                                0x2         32 samples
                                0x3         64 samples

        Bit 3 – AGCC.RST: AGC Reset
       A value of one resets the AGC and sets the maximum receiver gain. After command execution, the bit is reset
       automatically.

        Bit 2 – AGCC.FRZS: AGC Freeze Status
       A value of one indicates that the AGC is on hold. The AGC can be put on hold either automatically by the baseband
       core or by writing a value of one to the AGC freeze control bit FRZC. The AGC is released by the baseband or if the
       FRZC bit is set to 0.

        Bit 1 – AGCC.FRZC: AGC Freeze Control
       A value of one forces the AGC to freeze to its current value. A value of zero releases the AGC.

        Bit 0 – AGCC.EN: AGC Enable
       A value of one enables the automatic gain control; a value of zero allows a manual setting of the RX gain control by
       sub-register AGCS.GCW.




                                                                                          Atmel AT86RF215 - DATASHEET                      59
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SR | 0x1 | fS=4000kHz |
|  | 0x2 | fS=2000kHz |
|  | 0x3 | fS=(4000/3)kHz |
|  | 0x4 | fS=1000kHz |
|  | 0x5 | fS=800kHz |
|  | 0x6 | fS=(2000/3)kHz |
|  | 0x8 | fS=500kHz |
|  | 0xA | fS=400kHz |

| Sub-register | Value | Description |
| --- | --- | --- |
| AVGS | 0x0 | 8 samples |
|  | 0x1 | 16 samples |
|  | 0x2 | 32 samples |
|  | 0x3 | 64 samples |


<!-- page 60 -->

6.2.5.4 RFn_AGCS – Receiver AGCG
       The register controls the AGC and the receiver gain.
        Bit              7            6          5         4          3           2             1             0
                                     TGT                                         GCW                                       RFn_AGCS
        Read/Write      RW           RW         RW        RW          RW         RW           RW            RW
        Initial Value    0            1          1         1          0           1             1             1

        Bit 7:5 – AGCS.TGT: AGC Target Level
       This sub-register sets the AGC target level relative to ADC full scale.

       Table 6-18. TGT

        Sub-register         Value        Description
        TGT                   0x0         Target=-21dB
                              0x1         Target=-24dB
                              0x2         Target=-27dB
                              0x3         Target=-30dB
                              0x4         Target=-33dB
                              0x5         Target=-36dB
                              0x6         Target=-39dB
                              0x7         Target=-42dB

        Bit 4:0 – AGCS.GCW: RX Gain Control Word
       If AGCC_EN is set to 1, a read of bit AGCS.GCW indicates the current receiver gain setting. If AGCC_EN is set to 0, a
       write access to GCW manually sets the receiver gain. An integer value of 23 indicates the maximum receiver gain; each
       integer step changes the gain by 3dB.

6.2.5.5 RFn_RSSI – Received Signal Strength Indicator
       This register contains the Received Signal Strength Indicator value.
        Bit              7            6          5         4          3           2             1             0
                                                               RSSI                                                         RFn_RSSI
        Read/Write       R           R           R         R          R           R             R            R
        Initial Value    0            1          1         1          1           1             1             1

        Bit 7:0 – RSSI.RSSI: Received Signal Strength Indicator
       This register contains the RSSI value of the selected radio channel and bandwidth. The value reflects the received
       signal power in dBm. A value of 127 indicates that the RSSI value is invalid. The register value presents a signed
       integer value (value range -127...+4) using twos complement representation.

6.2.5.6 RFn_EDC – Energy Detection Configuration
       The register configures the energy detection measurement mode.




                                                                                       Atmel AT86RF215 - DATASHEET                     60
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| TGT | 0x0 | Target=-21dB |
|  | 0x1 | Target=-24dB |
|  | 0x2 | Target=-27dB |
|  | 0x3 | Target=-30dB |
|  | 0x4 | Target=-33dB |
|  | 0x5 | Target=-36dB |
|  | 0x6 | Target=-39dB |
|  | 0x7 | Target=-42dB |


<!-- page 61 -->

        Bit              7           6            5            4         3           2            1             0
                         –           –            –            –         –           –                 EDM                    RFn_EDC
        Read/Write       R           R            R            R         R           R          RW            RW
        Initial Value    0           0            0            0         0           0            0             0

        Bit 1:0 – EDC.EDM: Energy Detection Mode
       Table 6-19. EDM

        Sub-register      Name                          Value      Description
        EDM               RF_EDAUTO                      0x0       EDAUTO: Energy detection measurement is automatically
                                                                   triggered if the AGC is held by the internal baseband or by setting
                                                                   bit FRZC.
                          RF_EDSINGLE                    0x1       EDSINGLE: A single energy detection measurement is started.
                          RF_EDCONT                      0x2       EDCONT: A continuous energy detection measurements of
                                                                   configured interval defined in register EDD is started.
                          RF_EDOFF                       0x3       EDOFF: Energy detection measurement is disabled.

6.2.5.7 RFn_EDD – Receiver Energy Detection Averaging Duration
       The register contains the averaging duration of RSSI values for energy detection calculation.
        Bit              7           6            5            4         3           2            1             0
                                                        DF                                             DTB                    RFn_EDD
        Read/Write      RW           RW           RW         RW          RW         RW          RW            RW
        Initial Value    0           1            0            0         0           0            0             1

        Bit 7:2 – EDD.DF: Receiver energy detection duration factor
       The factor of the averaging time is defined. The averaging time is calculated by T[μs]=DF*DTB.

        Bit 1:0 – EDD.DTB: Receiver energy detection average duration time basis
       The time basis of averaging RSSI values is defined.

       Table 6-20. DTB

        Sub-register         Value        Description
        DTB                  0x0          2μs
                             0x1          8μs
                             0x2          32μs
                             0x3          128μs

6.2.5.8 RFn_EDV – Receiver Energy Detection Value
       The register contains the averaged energy detection value.
        Bit              7           6            5            4         3           2            1             0
                                                                   EDV                                                        RFn_EDV
        Read/Write       R           R            R            R         R           R            R            R
        Initial Value    0           1            1            1         1           1            1             1

        Bit 7:0 – EDV.EDV: Receiver energy detection value
       The register contains the averaged energy detection value. The register value presents a signed integer value (value
       range -127...+4).




                                                                                         Atmel AT86RF215 - DATASHEET                     61
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| EDM | RF_EDAUTO | 0x0 | EDAUTO: Energy detection measurement is automatically |
|  |  |  | triggered if the AGC is held by the internal baseband or by setting |
|  |  |  | bit FRZC. |
|  | RF_EDSINGLE | 0x1 | EDSINGLE: A single energy detection measurement is started. |
|  | RF_EDCONT | 0x2 | EDCONT: A continuous energy detection measurements of |
|  |  |  | configured interval defined in register EDD is started. |
|  | RF_EDOFF | 0x3 | EDOFF: Energy detection measurement is disabled. |

| Sub-register | Value | Description |
| --- | --- | --- |
| DTB | 0x0 | 2μs |
|  | 0x1 | 8μs |
|  | 0x2 | 32μs |
|  | 0x3 | 128μs |


<!-- page 62 -->

6.3     Frequency Synthesizer (PLL)

6.3.1   Overview
        The frequency synthesizer generates the RF frequency which is used during the transmit process to convert the
        baseband signal to an RF signal. During the receive process, the generated RF frequency is used to mix down the
        received RF signal to a low IF signal.
        Two separate frequency synthesizers are implemented in the AT86RF215, one for the sub-1GHz transceiver and one
        for the 2.4GHz transceiver. The reference clocks for both fractional-N based synthesizers are derived from the 26MHz
        clock at pin TCXO. The PLLs and their filters are fully integrated; no external components are required for frequency
        synthesis.

        Table 6-21. Frequency Ranges and Resolutions

        Frequency range                     Frequency resolution             Comment

        389.5MHz … 510MHz                   ≈100Hz (6.5MHz/216)              Sub-1GHz transceiver,
                                                                             valid for CNM.CM equal to 0 or 1

        779MHz…1020MHz                      ≈200Hz (13.0MHz/216)             Sub-1GHz transceiver,
                                                                             valid for CNM.CM equal to 0 or 2

        2400MHz…2483.5MHz                   ≈400Hz (26.0MHz/216)             2.4GHz transceiver,
                                                                             valid for CNM.CM equal to 0 or 3

        Notes:     In the range from 409.5 to 416MHz and from 819 to 832MHz the performance in regards to receiver sensitivity
                   and transmitter quality is decreased due to the increased phase noise.
        The PLLs operate at State TXPREP, State TX and State RX, refer to Figure 5-5 on page 33.
        When reaching State TXPREP from State TRXOFF, interrupt IRQS.TRXRDY is generated. It indicates that the PLL is
        locked, the analog modules are settled and the transceiver is ready to transmit.
        The PLL is automatically frequency tuned:
                During the transition from State TRXOFF to State TXPREP (after the general calibrations described in section
                 "Analog Calibrations" on page 80 .), refer to transition time tTRXOFF_TXPREP in section "Electrical Characteristics"
                 on page 187.
                If the channel frequency registers are written in State TXPREP and the PLL locks, the interrupt IRQS.TRXRDY
                 is generated. The tuning time depends on the channel step size, refer to tPLL_CH_SW .
                Switching the transceiver from State TRXOFF to State TXPREP or State RX.
        If the PLL unlocks, the interrupt IRQS.TRXERR is generated. Interrupt IRQS.TRXERR does not cause any state
        change. The PLL locks autonomously again which is indicated by interrupt IRQS.TRXRDY. A new PLL settling process
        can be triggered by switching the transceiver to State TRXOFF and then back to State TXPREP or State RX. The PLL
        lock status is indicated by the sub-register PLL.LS.

6.3.2   Channel Configuration
        The channel frequency must be configured in State TRXOFF using registers RFn_CS, RFn_CCF0H, RFn_CCF0L,
        RFn_CNL, RFn_CNM. Within in the same frequency range (see Table 6-21 above) the channel frequency can also be
        changed in State TXPREP. A write access to the register RFn_CNM applies the current channel register values and
        makes the frequency changes effective. If register RFn_CNM is not written the channel frequency is not changed. The
        register RFn_CNM must always be written last.


                                                                                        Atmel AT86RF215 - DATASHEET                     62
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 63 -->

The channel can be configured by two different schemes:
         IEEE-compliant scheme defined in [3](clause 8.1.2 “Channel assignments”)
         Fine resolution scheme


IEEE-compliant Scheme (CNM.CM=0)
The IEEE-compliant channel scheme refers to Table 68d and Table 68e of [3]. It is enabled if sub-register CNM.CM is
set to 0 (default). The channel frequency is calculated as follows:

f channel  (CCF0  CN  CS)  25kHz  f offset
The channel center frequency base value CCF0 is a 16-bit value. The register RFn_CCF0H contains the high byte and
the register RFn_CCF0L the low byte value. The frequency resolution is 25kHz.
The channel number CN is a 9-bit value. The register RFn_CNL contains the low byte value and bit 9 is the value of
sub-register CNM.CNH.
The channel spacing CS is an 8-bit value. The value has a resolution of 25kHz. The register RFn_CS has to be set
accordingly.
The frequency foffset is 0Hz for the sub-1GHz transceiver frequency channels (RF09). For the 2.4GHz transceiver
(RF24) the frequency foffset is 1.5GHz.
Example: OFDM (option 1), channel 2 in the 863MHz band is configured as follows:
           The base frequency is 863.625MHz.
            CCF0H.CCF0H,CCF0L.CCF0L = 863.625MHz / 25kHz = 34,545 (0x86F1)
           Channel spacing is 1.2MHz
            CS.CS = 1.2MHz / 25kHz = 48 (0x30)
           Channel value is 2
            RFn_CNL = 2, CNM.CNH = 0 and CNM.CM = 0
           The programming sequence is started at register RF09_CS with the following values: 0x30, 0xF1, 0x86, 0x02,
            0x00 (register order: RF09_CS, RF09_CCF0L, RF09_CCF0H, RF09_CNL, RF09_CNH)
The frequencies must be within the supported range, otherwise the behavior is undefined. The device is not protected
against incorrect frequency settings.


Fine Resolution Channel Scheme CNM.CM=1
The fine resolution channel scheme mode 1 is enabled if sub-register CNM.CM is set to 1.

                          6.5MHz  N channel
f channel  377MHz 
                               216
N channel   CCF0H,CCF0L, CNL126030
                                        1340967



The channel number Nchannel is a 24-bit value and consists of high byte RFn_CCF0H, middle byte RFn_CCF0L and low
byte RFn_CNL. The channel number Nchannel ranges from 126.030 (389.5MHz) to 1340.967 (510MHz); other values are
not supported and proper PLL behavior is not guaranteed. The setting is valid for the sub-1GHz transceiver (RF09); the
setting has no effect for the 2.4GHz transceiver (RF24).


Fine Resolution Channel Scheme CNM.CM=2




                                                                            Atmel AT86RF215 - DATASHEET                     63
                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 64 -->

        The fine resolution channel scheme mode 2 is enabled if sub-register CNM.CM is set to 2.

                               13MHz  N channel
        f channel  754MHz 
                                   216
        N channel   CCF0H,CCF0L, CNL126030
                                              1340967



        The channel number Nchannel is a 24-bit value and consists of high byte RFn_CCF0H, middle byte RFn_CCF0L, and low
        byte RFn_CNL. The channel number Nchannel ranges from 126.030 (779MHz) to 1340.967 (1020MHz); other values are
        not supported and proper PLL behavior is not guaranteed. The setting is valid for the sub-1GHz transceiver (RF09); the
        setting has no effect for the 2.4GHz transceiver (RF24).


        Fine Resolution Channel Scheme CNM.CM=3
        The fine resolution channel scheme mode 3 is enabled if sub-register CNM.CM is set to 3.

                                26MHz  N channel
        f channel  2366MHz 
                                    216
        N channel   CCF0H,CCF0L, CNL85700
                                              296172



        The channel number Nchannel is a 24-bit value and consists of high byte RFn_CCF0H, middle byte RFn_CCF0L, and low
        byte RFn_CNL. The channel number Nchannel ranges from 85.700 (2400MHz) to 296.172 (2483.5MHz); other values are
        not supported and proper PLL behavior is not guaranteed. The setting is valid for the 2.4GHz transceiver (RF24); the
        setting has no effect for the sub-1GHz transceiver (RF09).

6.3.3   Register Description
6.3.3.1 RFn_CS – Channel Spacing
        The register configures the channel spacing with a resolution of 25kHz. The register CNM must be written to take over
        the CS value. The CNM register must always be written last.
        Bit               7         6          5          4           3         2            1             0
                                                               CS                                                         RFn_CS
        Read/Write       RW        RW         RW         RW           RW       RW          RW            RW
        Initial Value     0         0          0          0           1         0            0             0

         Bit 7:0 – CS.CS: Channel Spacing with 25kHz Resolution
        Example: A value of 0x08 needs to be set (8x25kHz) for a channel spacing of 200kHz.

6.3.3.2 RFn_CCF0L – Channel Center Frequency F0 Low Byte
        The register configures the base value of the channel center frequency F0 (low byte) with a resolution of 25kHz. The
        register CNM must be written to latch the CCFOL value. The CNM register must always be written last.
        Bit               7         6          5          4           3         2            1             0
                                                              CCF0L                                                     RFn_CCF0L
        Read/Write       RW        RW         RW         RW           RW       RW          RW            RW
        Initial Value     1         1          1          1           1         0            0             0

         Bit 7:0 – CCF0L.CCF0L: Channel Center Frequency with 25kHz Channel Spacing
        The reset value (0xf8) of the channel register results in 902.2MHz for the sub-1GHz transceiver (RF09) and 2402.2MHz
        for the 2.4GHz transceiver (RF24): CCF0=0x8cf8=36088; CS=200KHz, CN=0.




                                                                                    Atmel AT86RF215 - DATASHEET                     64
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 65 -->

6.3.3.3 RFn_CCF0H – Channel Center Frequency F0 High Byte
       The register configures the base value of the channel center frequency F0 (high byte) with a resolution of 25kHz. The
       register CNM must be written to latch the CCFOH value. The CNM register must always be written last.
        Bit              7           6            5          4           3         2            1             0
                                                                 CCF0H                                                     RFn_CCF0H
        Read/Write      RW           RW          RW         RW           RW       RW          RW            RW
        Initial Value    1           0            0          0           1         1            0             0

        Bit 7:0 – CCF0H.CCF0H: Channel Center Frequency with 25kHz Channel Spacing
       The reset value (0x8c) of the channel register results in 902.2MHz for the sub-1GHz transceiver (RF09) and 2402.2MHz
       for the 2.4GHz module (RF24): CCF0=0x8cf8=36088; CS=200KHz, CN=0.

6.3.3.4 RFn_CNL – Channel Number Low Byte
       The register contains the transceiver channel number low byte CN[7:0]. The register CNM must be written to latch the
       CNL value. The CNM register must always be written last.
        Bit              7           6            5          4           3         2            1             0
                                                                 CNL                                                        RFn_CNL
        Read/Write      RW           RW          RW         RW           RW       RW          RW            RW
        Initial Value    0           0            0          0           0         0            0             0

6.3.3.5 RFn_CNM – Channel Mode and Channel Number High Bit
       The register configures the channel mode and channel number bit 9 CN[8]. A write operation to this register applies the
       channel register CS, CCFOL, CCFOH and CNL values.
        Bit              7           6            5          4           3         2            1             0
                              CM                  –          –           –         –            –           CNH             RFn_CNM
        Read/Write      RW           RW           R          R           R         R            R           RW
        Initial Value    0           0            0          0           0         0            0             0

        Bit 7:6 – CNM.CM: Channel Setting Mode
       Table 6-22. CM

        Sub-register         Value        Description
        CM                    0x0         IEEE compliant channel scheme; f=(CCF0+CN*CS)*25kHz+foffset; (foffset = 0Hz for sub-1GHz
                                          transceiver; foffset = 1.5GHz for 2.4GHz transceiver)
                              0x1         Fine resolution (389.5-510.0)MHz with 99.182Hz channel stepping
                              0x2         Fine resolution (779-1020)MHz with 198.364Hz channel stepping
                              0x3         Fine resolution (2400-2483.5)MHz with 396.728Hz channel stepping

        Bit 0 – CNM.CNH: Channel Number CN[8]
       The bit sets bit 9 (CN[8]) of the channel number CN[8:0]. Bit 9 is only needed for frequency range (2400-2483.5)MHz,
       MR-OFDM Option 4 and MR-FSK mode #1 for: TotalNumChan=416

6.3.3.6 RFn_PLL – Transceiver PLL
       This register provides status of the PLL operation.




                                                                                       Atmel AT86RF215 - DATASHEET                     65
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CM | 0x0 | IEEE compliant channel scheme; f=(CCF0+CN*CS)*25kHz+foffset; (foffset = 0Hz for sub-1GHz |
|  |  | transceiver; foffset = 1.5GHz for 2.4GHz transceiver) |
|  | 0x1 | Fine resolution (389.5-510.0)MHz with 99.182Hz channel stepping |
|  | 0x2 | Fine resolution (779-1020)MHz with 198.364Hz channel stepping |
|  | 0x3 | Fine resolution (2400-2483.5)MHz with 396.728Hz channel stepping |


<!-- page 66 -->

        Bit              7           6             5          4         3         2             1             0
                         –           –                  LBW             –         –            LS             –              RFn_PLL
        Read/Write       R           R             RW         RW        RW        RW            R           RW
        Initial Value    0           0             0          0         1         0             0             0

        Bit 5:4 – PLL.LBW: Loop Bandwidth
       This sub-register controls the PLL loop bandwidth.The sub-register is applicable for the sub-1GHz transceiver only
       (RF09). The TX modulation quality (i.e. FSK eye diagram) can be adjusted when direct modulation is used.

       Table 6-23. LBW

        Sub-register         Value       Description
        LBW                  0x0         default
                             0x1         15% smaller PLL loopbandwidth
                             0x2         15% larger PLL loopbandwidth

        Bit 1 – PLL.LS: PLL Lock Status
       Table 6-24. LS

        Sub-register         Value       Description
        LS                   0x0         PLL is not locked.
                             0x1         PLL is locked.

6.3.3.7 RFn_PLLCF – PLL center frequency value
       Center frequency calibration is performed from state TRXOFF to state TXPREP and at channel change. The register
       displays the center frequency value of the current channel.
        Bit              7           6             5          4         3         2             1             0
                         –           –                                       CF                                            RFn_PLLCF
        Read/Write       R           R             RW         RW        RW        RW          RW            RW
        Initial Value    0           0             0          0         0         0             0             0

        Bit 5:0 – PLLCF.CF: PLL center frequency value




                                                                                       Atmel AT86RF215 - DATASHEET                     66
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| LBW | 0x0 | default |
|  | 0x1 | 15% smaller PLL loopbandwidth |
|  | 0x2 | 15% larger PLL loopbandwidth |

| Sub-register | Value | Description |
| --- | --- | --- |
| LS | 0x0 | PLL is not locked. |
|  | 0x1 | PLL is locked. |


<!-- page 67 -->

6.4     Crystal Oscillator and TCXO
        The main features of the crystal oscillator are:
                Operation with external crystal or TCXO
                Amplitude controlled low phase noise 26MHz clock generation using external crystal
                Fast crystal oscillation settling time after enable (tXOSC_SETTL , see Table 10-7 on page 189)
                Configurable crystal frequency trimming with a capacitance load array RF_XOC.TRIM

6.4.1   Overview
        The oscillator generates the reference frequency for both radios, the sub-1GHz radio and the 2.4GHz radio. All internal
        generated frequencies of the transceivers are derived from this unique frequency. The overall system performance is
        therefore determined by the accuracy of the reference frequency.
        Two operating modes are supported:
                Crystal oscillator mode
                TCXO mode.

6.4.2   Crystal Oscillator mode
        Advantages using the integrated oscillator with an external crystal are low cost, no extra current consumption and fast
        start up of oscillation, typically tXOSC_SETTL =150μs, see Table 10-7 on page 189. Crystals suffer in contrast to TCXOs
        from higher frequency offset and frequency temperature drift which is especially critical in narrow band applications.
        The output frequency of the internal oscillator depends on the load capacitance between crystal pins TCXO and XTAL2.
        The total load capacitance CL must be equal to the vendor specified load capacitance of the crystal itself. It consists of
        the external capacitors CX and parasitic capacitances of PCB traces and IC pins. Parasitic capacitance of IC pin TCXO
        and pin XTAL2 is about CLEAD_DEVICE = 5
        CLEAD_         Lead capacitance of the AT86RF215                                                       5                        pF
        DEVICE

        each, see Table 10-5 on page 188.
        The external components of the crystal oscillator should be selected carefully and the related board layout should avoid
        parasitic capacitances. Crystal lines must be routed as short as possible and not in proximity to digital I/O signals. The
        register RF_XOC provides access to the control signals of the oscillator.
        Figure 6-8 shows all parasitic capacitances, such as PCB stray capacitances and the pin input capacitance summarized
        as CPAR.




                                                                                       Atmel AT86RF215 - DATASHEET                           67
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 68 -->

        Figure 6-8. Simplified Crystal Oscillator Schematic with External Components


                    CPAR   CX              CX         CPAR



                                26MHz
                    TCXO                   XTAL2        PCB
                                                   IC internal



            CTRIM                                  CTRIM

         TRIM[3:0]                          TRIM[3:0]




                                EVDD


        Additional internal trimming capacitors CTRIM are available. Any value in the range from 0pF to 4.5pF with a 0.3pF
        resolution is selectable using sub-register RF_XOC.TRIM. To calculate the total load capacitance, the following formula
        can be used:
        CLOAD_CRYSTAL=CL = 0.5 • (CX + CTRIM + CPAR).
        The trimming capacitors provide the possibility to reduce frequency deviations caused by variations of the production
        process or by tolerances of external components. Note, that the oscillation frequency can only be reduced by increasing
        the trimming capacitance. The frequency deviation caused by one step of RF_XOC.TRIM depends on Q-factor and CL
        of crystal and is about 2ppm in typical configurations.
        An amplitude control circuit is included to ensure stable operation under different operating conditions and for different
        crystal types. Enabling the crystal oscillator after leaving state DEEP_SLEEP, RESET or at power-on procedure a
        higher startup current during the amplitude build-up phase is drawn to guarantee a short start-up time. The current is
        reduced to the amount necessary for a robust oscillation during stable operation. This also keeps the drive level of the
        crystal low. To reduce oscillator startup current by 0.8mA, set bit RF_XOC.FS to 0. Start-up time is increased.
        Crystals with a higher load capacitance are generally less sensitive to parasitic pulling effects caused by variations of
        external components or board and circuit parasitics. On the other hand, a larger crystal load capacitance results in a
        longer start-up time, higher steady state current consumption and higher drive level.
        Refer to Table 10-5 on page 188 for crystal parameter specification.

6.4.3   External Reference Frequency with TCXO Setup
        The downsides of TCXOs are higher current consumption, extended start-up time in the range of milliseconds, and
        higher costs. The benefits are lower frequency offset and temperature compensated frequency drift.
        When using an external reference frequency, the TCXO output signal must be connected to pin TCXO. The oscillation
        peak-to-peak amplitude should be between 600mV and 1600mV. The TCXO input of the AT86RF215 is designed for
        clipped sin wave signals which shall be DC-coupled and ground referred. The parasitic ground capacity of pin TCXO is
        about CLEAD_DEVICE=5
        CLEAD_         Lead capacitance of the AT86RF215                                                     5                        pF
        DEVICE

        see Table 10-5 on page 188. Pin XTAL2 must be connected to ground if operating the device with a TCXO.




                                                                                      Atmel AT86RF215 - DATASHEET                          68
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 69 -->

        Figure 6-9. Block Diagram External Reference Frequency Setup with TCXO




                               TCXO
                                    26 MHz,
                                    clipped sine
                                    wave

                TCXO                                            XTAL2            PCB
                                                                            IC internal
                R=100kOhm
                        CPAR
                                                               Internal clock




6.4.4   Register Description
6.4.4.1 RF_XOC – Crystal Oscillator Control
        The register controls the operation of the crystal oscillator.
        Bit                     7           6             5          4           3        2             1             0
        (0x0009)                –            –            –         FS                         TRIM                                  RF_XOC
        Read/Write             RW           R             R         RW          RW        RW          RW            RW
        Initial Value           0           0             0          1           0        0             0             0

         Bit 4 – RF_XOC.FS: Crystal Oscillator fast start-up enable
        The sub-register enables the fast start-up option of the crystal oscillator. If the sub-register is set to 1, the fast start-up
        option is enabled.

         Bit 3:0 – RF_XOC.TRIM: Crystal Oscillator Trim
        The sub-register controls two internal capacitance arrays connected to the crystal oscillator pins TCXO and XTAL2.

        Table 6-25. TRIM

        Sub-register                Value        Description
        TRIM                          0x0        +0.0pF
                                      0x1        +0.3pF
                                      0x2        +0.6pF
                                      0x3        +0.9pF
                                      0x4        +1.2pF
                                      0x5        +1.5pF
                                      0x6        +1.8pF
                                      0x7        +2.1pF
                                      0x8        +2.4pF
                                      0x9        +2.7pF
                                      0xa        +3.0pF
                                      0xb        +3.3pF
                                      0xc        +3.6pF
                                      0xd        +3.9pF
                                      0xe        +4.2pF
                                      0xf        +4.5pF



                                                                                               Atmel AT86RF215 - DATASHEET                     69
                                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| TRIM | 0x0 | +0.0pF |
|  | 0x1 | +0.3pF |
|  | 0x2 | +0.6pF |
|  | 0x3 | +0.9pF |
|  | 0x4 | +1.2pF |
|  | 0x5 | +1.5pF |
|  | 0x6 | +1.8pF |
|  | 0x7 | +2.1pF |
|  | 0x8 | +2.4pF |
|  | 0x9 | +2.7pF |
|  | 0xa | +3.0pF |
|  | 0xb | +3.3pF |
|  | 0xc | +3.6pF |
|  | 0xd | +3.9pF |
|  | 0xe | +4.2pF |
|  | 0xf | +4.5pF |


<!-- page 70 -->

6.5     External Frontend Control
        The AT86RF215 device provides four output pins for external frontend control (external LNA, PA), two pins for each
        transceiver. The control pins are assigned as follows:
               Pins FEA24 and FEB24 for the 2.4GHz band
               Pins FEA09 and FEB09 for the sub-1GHz band

6.5.1   Frontend Configurations
        The AT86RF215 device provides three configurations to control an external frontend. The pins of the transceiver are
        controlled by the state machine and switch automatically according to the state, refer to "State Machine" on page 33.
        The configuration must be selected depending on the external frontend implementation and can be configured by
        register RFn_PADFE.
        Note, the pins do not act differential.


        Frontend Pin Configuration 1
        Configuration 1 supports the automatic gain control of the external LNA (see section "Automatic Gain Control (AGC)" on
        page 53 ). The LNA of the frontend module must have the ability to be bypassed. A frontend module control with the
        following truth table (Table 6-26) is supported.

        Table 6-26. Frontend Control Pins Configuration I

        Mode      Frontend mode description               FEA pin      FEB pin       State of the radio
        0         All off (sleep mode)                    0            0             TRXOFF/ SLEEP/ RESET/ TXPREP
        1         RX LNA mode                             0            1             RX
        2         TX mode                                 1            0             TX
        3         RX bypass mode                          1            1             RX


        Frontend Pin Configuration 2
        Configuration 2 supports a frontend module control with the following truth table (Table 6-27).

        Table 6-27. Frontend Control Pins Configuration 2

        Mode          Frontend mode description           FEA pin      FEB pin       State of the radio
        0             All off (sleep mode)                0            0             TRXOFF/ SLEEP/ RESET/ TXPREP
        1             RX mode                             0            1             RX
        2             TX mode                             1            1             TX


        Frontend Pin Configuration 3
        Configuration 3 supports an automatic gain control of the external LNA. The frontend module cannot be switched off by
        the pin configuration. The on/off state must be controlled by a microcontroller. Configuration 3 supports a frontend
        module control with the following truth table (Table 6-28).




                                                                                     Atmel AT86RF215 - DATASHEET                     70
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 71 -->

        Table 6-28. Frontend Control Pins Configuration 3

        Mode          Frontend mode description                   FEA pin   FEB pin        State of the radio
        0             RX bypass mode                              0         0              RX
        1             RX LNA mode                                 0         1              RX
        2             TX mode                                     1         1              TX


        External Frontend Configuration Example

        Figure 6-10. Frontend Example Schematic 1: Configuration 1 and Configuration 2

                    Configuration 2

                    Frontend 2.4GHz
                     Control logic      S1        S2                                       S1
                         All off        0         0                                        S2
                                                                                                                           AT86RF215
                         RX Mode        0         1
                         TX Mode        1         1
                                                                                                                           FEA24
                                                                                  Balun
        Antenna
        2.4GHz                                              LNA
                                                                                                                           FEB24

                                                                                                                           RFP24
                                                                      PA
                                                                                                                           RFN24

                    Configuration 1
                    Frontend 900MHz or 470MHz                                                                              RFP09
                    Control logic            S1        S2
                                                                                                                           RFN09
                              All off        0         0
                              RX Mode        0         1
                              TX Mode        1         0
                                                                                                                           FEA09
                      RX bypass Mode         1         1
                                                                                                                           FEB09
         Antenna
        470MHz or                                           LNA                   Balun
         900MHz


                                                                                          S1
                                                                      PA                  S2




6.5.2   Frontend Pin – Timing Diagram
        Figure 6-11 shows the transmit timing diagram of the external pin behavior and the TX transmission.




                                                                                           Atmel AT86RF215 - DATASHEET                        71
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 72 -->

        Figure 6-11. Transmitter Frontend Pin Timing Diagram

                         TX Power                                                   PA                                          PA
                         [dBm]                                                     Ramp                                        Ramp

                                    ttx_bb_delay ttx_proc_delay ttx_start_delay   tpa_ramp                                    tpa_ramp

                                                                                                                                             Time

                                                                                                                     ...
                State TX_PREP                                                                TX                                          TX_PREP


           Instruction      CMD=TX
        TX mode
        FEA/B pins



6.5.3   External Low Noise Amplifier (LNA) and Internal Automatic Gain Control (AGC)
        If an external frontend with an LNA is deployed, the AT86RF215 needs to be configured accordingly to make the higher
        sensitivity effective and to meet the adjacent channel specification of the system.
        The AT86RF215 supports an external LNA with either 9dB or 12dB gain, refer to AUXS.AGCMAP. The internal AGC
        scheme accommodates this external behavior and the RFn_RSSI and RFn_EDV values are mapped automatically.
        Refer to section "Automatic Gain Control (AGC)" on page 53 for further information.
        In case the external LNA has a gain that differs from the supported values as defined by sub-register AUXS.AGCMAP,
        the value with the closest corresponding setting should be used and the RFn_RSSI and RFn_EDV values needs to be
        re-evaluated according to the application. If the gain of the external LNA is higher than supported the adjacent channel
        robustness might suffer.
        It is recommended to use a frontend with the ability to bypass the LNA. If the external frontend has the ability to bypass
        the LNA, the sub-register AUXS.EXTLNABYP can be set and the external LNA is accommodated in the AGC scheme of
        the AT86RF215 for optimized performance. The configuration 1 or 3 should be applied (PADFE.PADFE). Depending on
        the receiver input level, the external frontend mode “RX LNA mode” (for low signal input strength; register value
        AGCS.GCW>17) or the “RX bypass mode” (for strong signal input strength, register value AGCS.GCW≤17) is switched
        automatically, see Table 6-26 and Table 6-28. Note, the register value AGCS.GCW is only reset at state change to
        state RX. At “RX bypass mode” an external gain of 0dB is assumed for the RFn_RSSI and RFn_EDV automatic
        calculation.

6.5.4   Register Description
6.5.4.1 RFn_AUXS – Transceiver Auxiliary Settings
        The register controls transceiver auxiliary settings.
        Bit                 7              6              5              4              3          2             1             0
                         EXTLNAB
                                               AGCMAP                 AVEXT          AVEN         AVS                PAVC                   RFn_AUXS
                            YP
        Read/Write         RW             RW             RW             RW            RW          R            RW            RW
        Initial Value       0              0              0              0              0          0             1             0

         Bit 7 – AUXS.EXTLNABYP: External LNA Bypass Availability
        The bit activates an AGC scheme where the external LNA can be bypassed using pins FEAnn/FEBnn.




                                                                                                        Atmel AT86RF215 - DATASHEET                     72
                                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 73 -->

       Table 6-29. EXTLNABYP

        Sub-register         Value     Description
        EXTLNABYP             0x0      Bypass of external LNA not available
                              0x1      Bypass of external LNA available

        Bit 6:5 – AUXS.AGCMAP: AGC Map
       Depending on the external frontend setup (external LNA), a specific AGC gain mapping is applied considering the gain
       of the external LNA (about 9dB or 12dB external LNA gain). If EXTLNABYP is set to 1 and AGCMAP is set to 0, the
       pins FEAnn/FEBnn are set such that the external LNA is bypassed, see also register PADFE for further explanation.

       Table 6-30. AGCMAP

        Sub-register         Value     Description
        AGCMAP                0x0      Internal AGC, no external LNA used
                              0x1      AGC back-off for external LNA of about 9dB gain
                              0x2      AGC back-off for external LNA of about 12dB gain

        Bit 4 – AUXS.AVEXT: Analog Voltage External Driven
       The bit disables the internal analog supply voltage. If this bit is set to 1, an external supply must be connected to the
       corresponding AVDD (AVDD0: sub-1GHz radio; AVDD1 2.4GHz radio).

        Bit 3 – AUXS.AVEN: Analog Voltage Enable
       If this bit is set to 1, the analog voltage regulator turns on in state TRXOFF. This setting enables faster transition from
       state TRXOFF to TXPREP or RX, but comes with a higher current consumption in state TRXOFF. The analog voltage
       regulator is always turned off in state SLEEP.

       Table 6-31. AVEN

        Sub-register         Value     Description
        AVEN                  0x0      Disabled
                              0x1      Enabled

        Bit 2 – AUXS.AVS: Analog Voltage Status
       The bit indicates that the analog voltage has settled.

        Bit 1:0 – AUXS.PAVC: Power Amplifier Voltage Control
       The sub-register controls the supply voltage of the internal power amplifier.

       Table 6-32. PAVC

        Sub-register         Value     Description
        PAVC                  0x0      2.0V
                              0x1      2.2V
                              0x2      2.4V

6.5.4.2 RFn_PADFE – External Frontend Control Pad Configuration
       This register sets the configurations for the external frontend control pins FEAnn and FEBnn. The external frontend
       setup of the board is configured by sub-registers AUXS.EXTLNABYP and AUXS.AGCMAP.




                                                                                       Atmel AT86RF215 - DATASHEET                     73
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| EXTLNABYP | 0x0 | Bypass of external LNA not available |
|  | 0x1 | Bypass of external LNA available |

| Sub-register | Value | Description |
| --- | --- | --- |
| AGCMAP | 0x0 | Internal AGC, no external LNA used |
|  | 0x1 | AGC back-off for external LNA of about 9dB gain |
|  | 0x2 | AGC back-off for external LNA of about 12dB gain |

| Sub-register | Value | Description |
| --- | --- | --- |
| AVEN | 0x0 | Disabled |
|  | 0x1 | Enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| PAVC | 0x0 | 2.0V |
|  | 0x1 | 2.2V |
|  | 0x2 | 2.4V |


<!-- page 74 -->

Bit               7           6          5             4         3           2            1             0
                      PADFE               –            –         –           –            –             –            RFn_PADFE
Read/Write       RW           RW         R             R         R           R            R            R
Initial Value     0           0          0             0         0           0            0             0

 Bit 7:6 – PADFE.PADFE: Frontend Pins Configuration
The sub-register sets the configurations for the frontend control pins. The pins FEAnn and FEBnn are switched based
on the radio state.
Configuration 0: no Frontend control; FEAnn and FEBnn output is always 0
Configuration 1: (1 pin is TX switch; 1 pin is RX switch; LNA can be bypassed)
FEA|FEB: L|L: TXPREP (Frontend off); H|L: TX (Transmit); L|H: RX (Receive); H|H: RX with LNA Bypass
Configuration 2: (1 pin is enable, 1 pin is TXRX switch; 1 | 0 additional option)
FEA|FEB: L|L: TXPREP (Frontend off); H|H: TX (Transmit); L|H: RX (Receive); H|L: RX with LNA Bypass
Configuration 3: (1 pin is TXRX switch, 1 pin is LNA Bypass, 1 pin (MCU) is enable)
FEA|FEB|MCUPin: L|L|L: TXPREP (Frontend off); H|H|H: TX (Transmit); L|H|H: RX (Receive); L|L|H: RX with LNA
Bypass

Table 6-33. PADFE

Sub-register       Name                        Value       Description
PADFE              RF_FEMODE0                    0x0       Configuration 0
                   RF_FEMODE1                    0x1       Configuration 1
                   RF_FEMODE2                    0x2       Configuration 2
                   RF_FEMODE3                    0x3       Configuration 3




                                                                                 Atmel AT86RF215 - DATASHEET                     74
                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| PADFE | RF_FEMODE0 | 0x0 | Configuration 0 |
|  | RF_FEMODE1 | 0x1 | Configuration 1 |
|  | RF_FEMODE2 | 0x2 | Configuration 2 |
|  | RF_FEMODE3 | 0x3 | Configuration 3 |


<!-- page 75 -->

6.6     Voltage Regulator

6.6.1   Main Power Supplies
        The AT86RF215 has three independent bandgap stabilized internal voltage regulators:
              DVREG:           Digital 1.8V domain, pin DVDD
              AVREG0: Analog/RF 1.8V sub-1GHz transceiver domain. pin AVDD0
              AVREG1: Analog/RF 1.8V 2.4GHz transceiver domain, pin AVDD1
        A simplified schematic of the internal voltage regulators is shown in Figure 6-12.

        Figure 6-12. Simplified Schematic of Voltage Regulator

                                    AVREG1 (RF24)

                                 AVREG0 (RF09)
                               DVREG
                                         (D)EVDD        PCB
                                                                                 AVDD1
          Bandgap                                                        AVDD0
           Voltage    1.225V
          Reference                                 DVDD
            (BG)




                                                                 C dec




        The voltage regulators require decouple capacitors for stable operation. The values of the decouple capacitors
        determine the settling time. A recommended value is Cdec= 100nF (see Table 10-4 on page 188). The decouple
        capacitors should be placed as close as possible to the pins and should be connected to ground with the shortest
        possible traces. The pins DVDD, AVDD0 and AVDD1 must not be shorted.
        The DVREG is enabled during start-up and is switched off in state DEEP_SLEEP. The AVREG is enabled only on
        request by the radio. Table 6-34 reflects the status of the voltage regulators in various transceiver states.

        Table 6-34. Voltage Regulator Status

        Sub-1GHz                    2.4GHz                 DVREG          AVREG0         AVREG1           Comments
        transceiver state           transceiver state
        TRXOFF                      TRXOFF                 ON             OFF            OFF
        SLEEP                       TRXOFF                 ON             OFF            OFF
        TRXOFF                      SLEEP                  ON             OFF            OFF
        SLEEP                       SLEEP                  OFF            OFF            OFF              DEEP_SLEEP
        TRXOFF, SLEEP               TXPREP, TX, RX         ON             OFF            ON1              See Note 1
        TXPREP, TX, RX              TRXOFF, SLEEP          ON             ON1            OFF              See Note 1
        TXPREP, TX, RX              TXPREP, TX, RX         ON             ON1            ON1              See Note 1




                                                                                           Atmel AT86RF215 - DATASHEET                        75
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 76 -->

        Note:     1.    If sub-register AUXS.AVEN is set to 1, the analog voltage regulator is on in all states except state SLEEP.
                        The current consumption in state TRXOFF is increased by the individual current consumption of the
                        voltage regulator of 80μA.
        The status of the analog voltage regulators are indicated by sub-register AUXS.AVS.
        It is recommended using the internal voltage regulators but it is also possible to supply the voltage domains by an
        external voltage supply. The analog voltages can be supplied at pin AVDD0 and pin AVDD1. In order to supply external
        voltages, the internal analog voltage regulators must be switched off by sub-register AUXS.AVEXT. Note, that the
        voltages must not exceed the maximum voltage on analog pins (see section "Absolute Maximum Ratings*" on page
        187). The internal digital voltage regulator cannot be switched off. An external voltage has to overdrive the internal
        voltage.
        Each voltage regulator features a current limitation which is active during voltage regulator start-up. The start-up current
        is limited to IVREG_LIMIT =60
        IVREG_          Current limitation of internal voltage                                          43        60          78           mA
        LIMIT           regulator at start-up
         (see Table 10-4 on page 188). After start-up, the current limitation is released, the voltage regulator load current is no
        longer limited.

6.6.2   Register Description
6.6.2.1 RFn_AUXS – Transceiver Auxiliary Settings
        The register controls transceiver auxiliary settings.
        Bit                  7           6            5            4         3        2             1             0
                         EXTLNAB
                                             AGCMAP              AVEXT    AVEN       AVS                 PAVC                  RFn_AUXS
                            YP
        Read/Write          RW           RW          RW           RW        RW       R            RW            RW
        Initial Value        0           0            0            0         0        0             1             0

         Bit 7 – AUXS.EXTLNABYP: External LNA Bypass Availability
        The bit activates an AGC scheme where the external LNA can be bypassed using pins FEAnn/FEBnn.

        Table 6-35. EXTLNABYP

        Sub-register             Value        Description
        EXTLNABYP                 0x0         Bypass of external LNA not available
                                  0x1         Bypass of external LNA available

         Bit 6:5 – AUXS.AGCMAP: AGC Map
        Depending on the external frontend setup (external LNA), a specific AGC gain mapping is applied considering the gain
        of the external LNA (about 9dB or 12dB external LNA gain). If EXTLNABYP is set to 1 and AGCMAP is set to 0, the
        pins FEAnn/FEBnn are set such that the external LNA is bypassed, see also register PADFE for further explanation.




                                                                                           Atmel AT86RF215 - DATASHEET                          76
                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| IVREG_ LIMIT | Current limitation of internal voltage |  | 43 | 60 | 78 | mA |
| --- | --- | --- | --- | --- | --- | --- |
|  | regulator at start-up |  |  |  |  |  |

| Sub-register | Value | Description |
| --- | --- | --- |
| EXTLNABYP | 0x0 | Bypass of external LNA not available |
|  | 0x1 | Bypass of external LNA available |


<!-- page 77 -->

Table 6-36. AGCMAP

Sub-register          Value     Description
AGCMAP                 0x0      Internal AGC, no external LNA used
                       0x1      AGC back-off for external LNA of about 9dB gain
                       0x2      AGC back-off for external LNA of about 12dB gain

 Bit 4 – AUXS.AVEXT: Analog Voltage External Driven
The bit disables the internal analog supply voltage. If this bit is set to 1, an external supply must be connected to the
corresponding AVDD (AVDD0: sub-1GHz radio; AVDD1 2.4GHz radio).

 Bit 3 – AUXS.AVEN: Analog Voltage Enable
If this bit is set to 1, the analog voltage regulator turns on in state TRXOFF. This setting enables faster transition from
state TRXOFF to TXPREP or RX, but comes with a higher current consumption in state TRXOFF. The analog voltage
regulator is always turned off in state SLEEP.

Table 6-37. AVEN

Sub-register          Value     Description
AVEN                   0x0      Disabled
                       0x1      Enabled

 Bit 2 – AUXS.AVS: Analog Voltage Status
The bit indicates that the analog voltage has settled.

 Bit 1:0 – AUXS.PAVC: Power Amplifier Voltage Control
The sub-register controls the supply voltage of the internal power amplifier.

Table 6-38. PAVC

Sub-register          Value     Description
PAVC                   0x0      2.0V
                       0x1      2.2V
                       0x2      2.4V




                                                                                Atmel AT86RF215 - DATASHEET                     77
                                                                                 Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| AGCMAP | 0x0 | Internal AGC, no external LNA used |
|  | 0x1 | AGC back-off for external LNA of about 9dB gain |
|  | 0x2 | AGC back-off for external LNA of about 12dB gain |

| Sub-register | Value | Description |
| --- | --- | --- |
| AVEN | 0x0 | Disabled |
|  | 0x1 | Enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| PAVC | 0x0 | 2.0V |
|  | 0x1 | 2.2V |
|  | 0x2 | 2.4V |


<!-- page 78 -->

6.7     Battery Monitor (BATMON)

6.7.1   Battery Monitor Description
        The battery monitor (BATMON) detects and indicates a low supply voltage at pin EVDD. The main features of the
        battery monitor are:
              Configurable voltage thresholds ranging from 1.70V to 3.675V
              Generation of an interrupt if supply voltage (EVDD) drops below the configured threshold level
        A simplified schematic of the BATMON module with its input and output signals is shown in Figure 6-13.

        Figure 6-13. Simplified Battery Monitor Schematic


                                    EVDD
          BATMON_HR                               +         BATMON_OK

           4              DAC                     -
                                   Threshold
                                    Voltage
                                                          „1“
                                                                clear
                    For input-to-output mapping
                                                                D
                      see BATMON register
                                                                    Q
                                                                        BATMON_IRQ



        The battery monitor can be configured using the register RF_BMDVC. The sub-register RF_BMDVC.BMVTH defines
        the threshold voltage for battery level indication. The threshold voltage is configurable with a resolution of 75mV in the
        upper voltage range (RF_BMDVC.BMHR=1) and with a resolution of 50mV in the lower voltage range
        (RF_BMDVC.BMHR=0).
        The sub-register RF_BMDVC.BMS indicates the status of the battery voltage:
              RF_BMDVC.BMS=0: The battery voltage is lower than the threshold voltage.
              RF_BMDVC.BMS=1: The battery voltage is higher than the threshold voltage.
        The battery monitor is inactive during state DEEP_SLEEP.
        A supply voltage drop below the configured threshold value is indicated by interrupt IRQS.BATLOW. The interrupt
        IRQS.BATLOW is issued by both transceivers if not in state SLEEP.
        No interrupt is generated if:
              The EVDD voltage is below the default 1.8V threshold at power on, i.e. RF_BMDVC.BMS has never been 1.
              A new threshold is set which is still below the supply voltage, i.e. RF_BMDVC.BMS remains 0.
        Noise or temporary voltage drops may generate unwanted interrupts if the EVDD voltage is close to the programmed
        threshold voltage. To avoid this, the interrupt IRQM.BATLOW could be disabled or a lower threshold value could be set.
        The default threshold level is 1.8V. Operating the AT86RF215 at a supply voltage of 1.8V generates the interrupt
        IRQS.BATLOW during power-on.

6.7.2   Register Description
6.7.2.1 RF_BMDVC – Transceiver Battery Monitor Control and Digital Voltage Regulator Control
        The register configures the battery monitor. The status of the EVDD supply voltage is accessible by reading bit BMS
        with respect to the current BMVTH and BMHR threshold settings.




                                                                                      Atmel AT86RF215 - DATASHEET                     78
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 79 -->

Bit               7            6          5          4            3       2            1             0
(0x0008)           –           –         BMS       BMHR                       BMVTH                               RF_BMDVC
Read/Write        R            R          R         RW        RW         RW           RW           RW
Initial Value     0            0          0          0            0       0            1             0

 Bit 5 – RF_BMDVC.BMS: Battery Monitor Status
The bit indicates the level of the external supply voltage with respect to the configured battery monitor threshold. A
value of one indicates that the voltage at pin EVDD is above the configured threshold, zero otherwise.

 Bit 4 – RF_BMDVC.BMHR: Battery Monitor High Range
The bit configures the threshold range for the battery monitor.

Table 6-39. BMHR

Sub-register           Value       Description
BMHR                   0x0         Low range enabled, see BMVTH.
                       0x1         High range enabled, see BMVTH.

 Bit 3:0 – RF_BMDVC.BMVTH: Battery Monitor Voltage Threshold
The sub-register configures the threshold voltage for the battery monitor.

Table 6-40. BMVTH

Sub-register           Value       Description
BMVTH                  0x0         BMHR=1: 2.550V | BMHR=0: 1.70V
                       0x1         BMHR=1: 2.625V | BMHR=0: 1.75V
                       0x2         BMHR=1: 2.700V | BMHR=0: 1.80V
                       0x3         BMHR=1: 2.775V | BMHR=0: 1.85V
                       0x4         BMHR=1: 2.850V | BMHR=0: 1.90V
                       0x5         BMHR=1: 2.925V | BMHR=0: 1.95V
                       0x6         BMHR=1: 3.000V | BMHR=0: 2.00V
                       0x7         BMHR=1: 3.075V | BMHR=0: 2.05V
                       0x8         BMHR=1: 3.150V | BMHR=0: 2.10V
                       0x9         BMHR=1: 3.225V | BMHR=0: 2.15V
                       0xA         BMHR=1: 3.300V | BMHR=0: 2.20V
                       0xB         BMHR=1: 3.375V | BMHR=0: 2.25V
                       0xC         BMHR=1: 3.450V | BMHR=0: 2.30V
                       0xD         BMHR=1: 3.525V | BMHR=0: 2.35V
                       0xE         BMHR=1: 3.600V | BMHR=0: 2.40V
                       0xF         BMHR=1: 3.675V | BMHR=0: 2.45V




                                                                              Atmel AT86RF215 - DATASHEET                     79
                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| BMHR | 0x0 | Low range enabled, see BMVTH. |
|  | 0x1 | High range enabled, see BMVTH. |

| Sub-register | Value | Description |
| --- | --- | --- |
| BMVTH | 0x0 | BMHR=1: 2.550V \| BMHR=0: 1.70V |
|  | 0x1 | BMHR=1: 2.625V \| BMHR=0: 1.75V |
|  | 0x2 | BMHR=1: 2.700V \| BMHR=0: 1.80V |
|  | 0x3 | BMHR=1: 2.775V \| BMHR=0: 1.85V |
|  | 0x4 | BMHR=1: 2.850V \| BMHR=0: 1.90V |
|  | 0x5 | BMHR=1: 2.925V \| BMHR=0: 1.95V |
|  | 0x6 | BMHR=1: 3.000V \| BMHR=0: 2.00V |
|  | 0x7 | BMHR=1: 3.075V \| BMHR=0: 2.05V |
|  | 0x8 | BMHR=1: 3.150V \| BMHR=0: 2.10V |
|  | 0x9 | BMHR=1: 3.225V \| BMHR=0: 2.15V |
|  | 0xA | BMHR=1: 3.300V \| BMHR=0: 2.20V |
|  | 0xB | BMHR=1: 3.375V \| BMHR=0: 2.25V |
|  | 0xC | BMHR=1: 3.450V \| BMHR=0: 2.30V |
|  | 0xD | BMHR=1: 3.525V \| BMHR=0: 2.35V |
|  | 0xE | BMHR=1: 3.600V \| BMHR=0: 2.40V |
|  | 0xF | BMHR=1: 3.675V \| BMHR=0: 2.45V |


<!-- page 80 -->

6.8   Analog Calibrations
      Several analog radio blocks include calibration loops to minimize performance degradation due to process and
      temperature variation. All calibrations are initiated during the state transition from state TRXOFF to state TXPREP or to
      state RX (see "State Machine" on page 33). To achieve best calibration values and maximum RF performance, TX
      output power (register PAC.TXPWR) and the center frequency (see section "Frequency Synthesizer (PLL)" on page 62)
      must be configured in state TRXOFF.
      Following calibrations are performed:
           RX band-pass and TX low-pass filter cut-off frequency
           RX band-pass and TX low-pass filter DC offset
           Transmitter LO leakage
           PLL center frequency.
      At default register settings, the analog supply voltage is disabled in state TRXOFF to minimize supply current. Since all
      calibrations are based on the analog supply voltage AVDD0/AVDD1, the analog voltage regulator is turned on as a first
      step in the calibration sequence. The time to set up the analog supply voltage depends on the decouple capacitance
      (Cdec) at the pins AVDD0/AVDD1 and may be significant with respect to the duration of the calibrations. To minimize the
      state transition time, it is possible to enable the analog supply voltage at the state TRXOFF by setting sub-register
      AUXS.AVEN to 1.
      Refer to Table 10-7 on page 189 for typical transition time from state TRXOFF to state TXPREP. The interrupt
      IRQS.TRXRDY indicates that all calibrations are completed successfully.




                                                                                  Atmel AT86RF215 - DATASHEET                      80
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 81 -->

6.9     Baseband Core

6.9.1   Overview
        The AT86RF215 features dedicated baseband core functionality of:
               An MR-FSK PHY in support of [3] and [5]
               An MR-OFDM PHY in support of [3] and [5]
               An O-QPSK PHY in support of [3], [2] and [5]

        Figure 6-14. Simplified Block Diagram of the Baseband Cores


                   2.4GHz                             CORE1 (BBC1)
                   (RF24)
                              TX_{I,Q}_DATA[13:0]          MR-FSK
                    TX_FE                                                     TX FRAME BUFFER

                                                          MR-OFDM
                              RX_{I,Q}_DATA[13:0]
                    RX_FE                                                    RX FRAME BUFFER
                                  AGCR/H                   O-QPSK




                 Sub-1GHz                             CORE0 (BBC0)
                  (RF09)
                              TX_{I,Q}_DATA[13:0]          MR-FSK
                     TX_FE                                                    TX FRAME BUFFER

                                                          MR-OFDM
                              RX_{I,Q}_DATA[13:0]
                    RX_FE                                                    RX FRAME BUFFER
                                  AGCR/H                   O-QPSK




        As shown in Figure 6-14, the AT86RF215 includes baseband core CORE0 connected with the sub-1GHz radio and
        baseband core CORE1 connected with the 2.4GHz radio. CORE0 and CORE1 are identical and can be independently
        used.
        Each baseband core contains PHY implementations for MR-FSK, MR-OFDM and O-QPSK, according to section "MR-
        FSK PHY" on page 86, section "MR-OFDM PHY" on page 112 and section "O-QPSK PHY" on page 120, respectively.
        For each core, only one of the PHYs can be selected at a time. The PHY of the baseband core is selected by sub-
        register PC.PT. With sub-register PC.BBEN the baseband core is enabled separately. The baseband core can be
        disabled in two ways: set PC.BBEN or PC.PT to 0. For configuration of the PHYs the transceiver must be in the State
        TRXOFF.
        The selected PHY accesses the transmit frame buffer and receive frame buffer containing the PHY payload for transmit
        and receive, respectively. Details of the frame buffer are described in section "Frame Buffer" on page 132.




                                                                                  Atmel AT86RF215 - DATASHEET                     81
                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 82 -->

        The selected PHY accesses the radio using the TX and RX I/Q data interface, see section "Transmitter Digital
        Frontend" on page 43 and section "Receiver Digital Frontend" on page 53, respectively.

6.9.2   Baseband Interrupts
        If the baseband core is used (i.e. transceiver is operated in baseband mode, see section "Operating Modes" on page
        30), baseband-specific interrupts are issued. These interrupts indicate receive and transmit status and frame processing
        information of the baseband core. The corresponding interrupts can be enabled or disabled by the register
        BBCn_IRQM. The baseband interrupt reasons can be read from the register BBCn_IRQS. Each baseband core (BBC0
        and BBC1) uses its own interrupt status and mask registers.
        In Table 6-41 an overview of all baseband interrupts is shown with references to more detailed descriptions. For further
        information about radio interrupts see section "Interrupts" on page 38.

Table 6-41. Baseband Interrupts

 Interrupt       Section for Further          Comment
                 Information
 IRQS.RXFS       "MR-FSK PHY" on page         This interrupt is issued if a valid PHY header is detected during frame receive. With
                 86, "MR-OFDM PHY" on         the occurrence of IRQ RXFS, the valid PHR information is updated in PHY registers
                 page 112 and "O-QPSK         (i.e. BBCn_RXFLH, BBCn_RXFLL).
                 PHY" on page 120
 IRQS.RXFE       "Frame Filter" on page       The IRQ RXFE is issued at the end of a successful frame reception. The complete
                 141                          frame payload is stored in the receive frame buffer. With this interrupt, the transceiver
                                              changes automatically from state RX to state TXPREP.
                                              Additionally, the First Level of Filtering must pass. If the Address Filter is enabled, a
                                              matching frame must be recognized.
                                              The IRQ RXFE is issued tRXFE after frame end (see "Transition Timing" on page
                                              189).
 IRQS.RXEM       "Frame Filter" on page       This interrupt occurs during frame receive if the Address Filter is enabled and if the
                 141                          received frame is recognized as extended. The exact IRQ timing depends on the MAC
                                              header. The IRQ occurs if the MAC header parsing is completed.
 IRQS.RXAM       "Frame Filter" on page       This interrupt occurs during frame receive if the Address Filter is enabled and if the
                 141                          received frame is recognized as matching. The exact IRQ timing depends on the MAC
                                              header. The IRQ occurs if the MAC header parsing is completed.
 IRQS.TXFE                                    The IRQ_TXFE is issued when a frame is completely transmitted.
 IRQS.AGCH       "Automatic Gain Control      The interrupt AGCH is issued during frame receive if a preamble of the selected PHY
                 (AGC)" on page 53            is detected. With this IRQ the AGC is notified from the baseband core to hold its
                                              current amplification settings.
                                              IRQs AGCH and AGCR are exclusive. With the occurrence of AGCH a pending IRQ
                                              AGCR is cleared. The register BBCn_IRQS only indicates the last occurred of both
                                              IRQs.
                                              This interrupt is for information purposes only.
 IRQS.AGCR       "Automatic Gain Control      The interrupt AGCR is issued during frame receive if a receive process is finished.
                 (AGC)" on page 53            With this IRQ the AGC is notified from the baseband core to release its amplification
                                              settings and adapt its amplification to the receive signal strength automatically. IRQ
                                              AGCR also indicates a finished or canceled receive process. If IRQ AGCR occurs
                                              during the receive process, the reception is canceled and restarted.
                                              IRQs AGCH and AGCR are exclusive. With the occurrence of AGCR a pending IRQ
                                              AGCH is cleared. The register BBCn_IRQS only indicates the last occurred of both
                                              IRQs.
                                              This interrupt is for information purposes only.




                                                                                       Atmel AT86RF215 - DATASHEET                     82
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 83 -->

Interrupt         Section for Further             Comment
                  Information
IRQS.FBLI         "Frame Buffer Level             The interrupt FBLI can be used to monitor the receive frame buffer level. If the pre-
                  Interrupt" on page 134          programmed number of octets have been received (i.e. stored to the frame buffer), the
                                                  IRQ FBLI is issued. The number of received octets can be configured by the registers
                                                  BBCn_FBLIL and BBCn_FBLIH.


       Transmit
       In Figure 6-15 a typical IRQ behavior during frame transmit is shown.

       Figure 6-15. Baseband Interrupts during Frame Transmit


        RF Signal                    SHR          PHR                    PSDU


        STATE         TXPREP                                    TX                                     TXPREP


        IRQ
                                                                                              TXFE


       Receive
       Figure 6-16 shows the interrupt behavior during a receive process (all possible baseband receive IRQs are shown).

       Figure 6-16. Baseband Interrupts during Frame Receive

                                                                                 tRXFE


        RF Signal        SHR       PHR                       PSDU


        STATE                                     RX                                      TXPREP


        IRQ
                       AGCH                RXFS    RXEM                               RXFE,AGCR
                                                      RXAM


       In Figure 6-17 a receive procedure is shown that is canceled after the occurrence of the IRQ RXEM. Subsequent
       interrupts are suppressed afterwards. The receive process is restarted after IRQ AGCR. A frame reception is canceled
       if the received signal shows a discontinuity or if no valid PHR is found.

       Figure 6-17. Baseband Interrupts during Canceled Frame Reception

                                                                  corrupted frame
                                                             (i.e. incomplete PSDU)

        RF Signal         SHR       PHR       PSDU


        STATE                                            RX


        IRQ
                        AGCH               RXFS    RXEM
                                                     AGCR




                                                                                                  Atmel AT86RF215 - DATASHEET                     83
                                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 84 -->

6.9.3   Register Description
6.9.3.1 BBCn_PC – PHY Control
        This register configures the baseband PHY.
        Bit               7            6             5            4       3        2            1             0
                         CTX         FCSFE        FCSOK      TXAFCS     FCST     BBEN                 PT                    BBCn_PC
        Read/Write       RW            RW            R            RW      RW      RW          RW            RW
        Initial Value     0            1             0            1       0        1            0             0

         Bit 7 – PC.CTX: Continuous Transmit
        This sub-register enables the continuous transmit mode.

        Table 6-42. CTX

        Sub-register           Value        Description
        CTX                    0x0          Continuous transmission disabled
                               0x1          Continuous transmission enabled

         Bit 6 – PC.FCSFE: Frame Check Sequence Filter Enable
        This sub-register configures the filter function of the FCS check. If this sub-register is set to 1, an IRQ RXFE occurs only
        if the frame has a valid FCS. If this sub-register is set to 0, an IRQ RXFE occurs regardless of the FCS validity.

        Table 6-43. FCSFE

        Sub-register           Value        Description
        FCSFE                  0x0          FCS filter disabled
                               0x1          FCS filter enabled

         Bit 5 – PC.FCSOK: Frame Check Sequence OK
        This sub-register indicates whether the FCS of a detected frame is valid or not. This sub-register is automatically set to
        0 if a frame start is detected. FCSOK is updated once the frame is received completely.

        Table 6-44. FCSOK

        Sub-register           Value        Description
        FCSOK                  0x0          FCS not valid
                               0x1          FCS valid

         Bit 4 – PC.TXAFCS: Transmitter Auto Frame Check Sequence
        If the sub-register TXAFCS is set to 1 during transmission, the internal calculated FCS (type dependent of FCST) is
        inserted into the last 2 or 4 PSDU octets, respectively. Note, this sub-register should be set to 1 only if the TX frame
        length is greater than the length of the selected FCS type, otherwise sub-register TXAFCS should be set to 0.

        Table 6-45. TXAFCS

        Sub-register           Value        Description
        TXAFCS                 0x0          FCS not calculated
                               0x1          FCS autonomously calculated

         Bit 3 – PC.FCST: Frame Check Sequence Type
        The sub-register FCST configures the used Frame Check Sequence Type.




                                                                                       Atmel AT86RF215 - DATASHEET                     84
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CTX | 0x0 | Continuous transmission disabled |
|  | 0x1 | Continuous transmission enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| FCSFE | 0x0 | FCS filter disabled |
|  | 0x1 | FCS filter enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| FCSOK | 0x0 | FCS not valid |
|  | 0x1 | FCS valid |

| Sub-register | Value | Description |
| --- | --- | --- |
| TXAFCS | 0x0 | FCS not calculated |
|  | 0x1 | FCS autonomously calculated |


<!-- page 85 -->

Table 6-46. FCST

Sub-register         Value     Description
FCST                  0x0      FCS type 32-bit
                      0x1      FCS type 16-bit

 Bit 2 – PC.BBEN: Baseband Enable
This sub-register enables the baseband.

Table 6-47. BBEN

Sub-register         Value     Description
BBEN                  0x0      Baseband is not enabled (switched off)
                      0x1      Baseband is enabled (switched on)

 Bit 1:0 – PC.PT: PHY Type
This sub-register sets the PHY type.

Table 6-48. PT

Sub-register       Name                      Value     Description
PT                 BB_PHYOFF                     0x0   OFF
                   BB_MRFSK                      0x1   MR-FSK
                   BB_MROFDM                     0x2   MR-OFDM
                   BB_MROQPSK                    0x3   MR-O-QPSK or legacy O-QPSK




                                                                        Atmel AT86RF215 - DATASHEET                     85
                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| FCST | 0x0 | FCS type 32-bit |
|  | 0x1 | FCS type 16-bit |

| Sub-register | Value | Description |
| --- | --- | --- |
| BBEN | 0x0 | Baseband is not enabled (switched off) |
|  | 0x1 | Baseband is enabled (switched on) |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| PT | BB_PHYOFF | 0x0 | OFF |
|  | BB_MRFSK | 0x1 | MR-FSK |
|  | BB_MROFDM | 0x2 | MR-OFDM |
|  | BB_MROQPSK | 0x3 | MR-O-QPSK or legacy O-QPSK |


<!-- page 86 -->

6.10   MR-FSK PHY

6.10.1 Overview
       The baseband sub-core MR-FSK of the AT86RF215 implements the MR-FSK mode specified in IEEE Std 802.15.4g™-
       2012 [3] and the GFSK PHY specified in ETSI TS 102 887-1, see [5]. Additional RAW mode extensions support a more
       flexible usage beyond the standard application.
       Key features are:
               Dual sense of synchronization word detection
               Forward Error Correction
               RAW mode

6.10.2 Coding and Modulation
6.10.2.1 Overview Coding and Modulation

       Figure 6-18. Simplified Signal Flow


                                                                               PA_CTRL           I_DATA[0]




                                                                                                 I_DATA[13:1]
          PACKET
                            FEC          ILV        DW           B2S          GFSK_MOD
          ENGINE                                                                                 Q_DATA[13:1]
                                      optional



       The basic signal flow is illustrated in Figure 6-18. The information bits of a packet can be optionally processed by
       Forward Error Correction (FEC), interleaving (ILV), and data whitening (DW). Bit-To-Symbol-Mapping (B2S) produces
       the discrete-time frequency symbol sequence. The corresponding I/Q baseband GFSK signal is passed to the I/Q data
       interface including the control signal of the power amplifier. For details, refer to section "Transmitter Digital Frontend" on
       page 43 and section "Modulation Index and Bandwidth Time Product" on page 88.

6.10.2.2 Forward Error Correction (FEC) and Interleaving (ILV)
       The sub-core MR-FSK supports both of the FEC schemes of IEEE Std 802.15.4g™-2012, applying terminated rate ½
       convolutional codes with constraint length K = 4, using a
               non-recursive and non-systematic code (NRNSC) encoder (phyFSKFECScheme = 0) or
               recursive and systematic code (RSC) encoder (phyFSKFECScheme = 1).
       The FEC scheme can be configured with sub-register FSKC2.FECS.
       Regardless of the FEC scheme, code-symbol interleaving specified in IEEE Std 802.15.4g™-2012 can be enabled by
       setting sub-register FSKC2.FECIE to 1. Interleaving is automatically bypassed if FEC is not enabled.
       With regard to the default register settings, FEC can be enabled with FSKPHRTX.SFD = 1. However, enabling of FEC
       may depend on several other register settings, as shown in Table 6-55 and Table 6-56. The motivation of this concept is
       described in section "PPDU Configuration" on page 90.




                                                                                      Atmel AT86RF215 - DATASHEET                     86
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 87 -->

6.10.2.3 Data Whitening (DW)
       The AT86RF215 supports data whitening as specified in IEEE Std 802.15.4g™-2012 [3]. Data whitening is enabled with
       sub-register FSKPHRTX.DW = 1. At receive, evaluation of the DW bit of the PHR field is automatically performed for
       de-whitening the PSDU. Note, that data whitening is performed at the code-bit level only for cases where FEC is
       enabled, see Figure 6-18 and IEEE Std 802.15.4g™-2012 [3]. Data whitening is not enabled in RAW mode, see section
       "RAW Mode" on page 92.

6.10.2.4 Bit-To-Symbol Mapping (B2S)
       Bit-To-Symbol Mapping depends on the modulation order (2-level or 4-level FSK), configured with sub-register
       FSKC0.MORD.

       The mapping of a (code)-bit c(k ) to a frequency symbol xS (k ) for 2-level FSK is shown in Table 6-49.


       Table 6-49. Bit-To-Symbol Mapping for 2-level FSK

       c(k)                                       Frequency Symbol xS(k)                   Frequency Deviation
       0                                          -1                                       -fdev
       1                                          +1                                       +fdev



       The mapping of the (code)-bit tuple (c(2k ), c(2k  1)) to the frequency symbol xS (k ) for 4-level FSK is shown in

       Table 6-50. For each tuple (c(2k ), c(2k  1)) , the entry c(2k ) is the predecessor with regard to the bit entry
       c(2k  1) .

       Table 6-50. Bit-To-Symbol Mapping for 4-level FSK

       (c(2k),c(2k+1))                            Frequency Symbol xS(k)                   Frequency Deviation
       (0,1)                                      -1                                       -fdev
       (0,0)                                      -1/3                                     -fdev/3
       (1,0)                                      +1/3                                     +fdev/3
       (1,1)                                      +1                                       +fdev


       4-level FSK is only active at the PHR or PSDU, see section "PPDU Types" on page 89.
       The AT86RF215 supports further modifications:

              If FSKC2.PRI is set to 1, frequency symbols xS (k ) of the preamble part of the PPDU are replaced with

                 xS (k ) at transmit. This setting is not evaluated at receive.

              If FSKC1.FI is set to 1, frequency symbols xS (k ) of the whole PPDU are replaced with  xS (k ) at transmit.
               At receive, the demodulator applies the corresponding inversion.




                                                                                   Atmel AT86RF215 - DATASHEET                      87
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 88 -->

6.10.2.5 Symbol Rate
       The AT86RF215 supports a selection of symbol rates targeting PHY modes according to IEEE Std 802.15.4g™-2012
       [3] and ETSI TS 102 887-1 [5], as shown in Table 6-51. The symbol rate 1/T, is configured with sub-register
       FSKC1.SRATE. Since the sub-core MR-FSK accesses the I/Q data interface with a fixed sampling rate converter, the
       digital front end (DFE) must be configured with specific settings as a function of the symbol rate, as shown in Table 6-
       51. For details of the DFE, refer to sections "Transmitter Digital Frontend" on page 43 and "Receiver Digital Frontend"
       on page 53.

       Table 6-51. Symbol Rate Settings

                                                                        Symbol Rate 1/T [kHz]
                                  50              100             150              200                  300                 400
        AT86RF215 Version         v.1     v.3     v.1     v.3     v.1       v.3    v.1        v.3       v.1       v.3       v.1        v.3
        FSKC1.SRATE               0       0       1       1       2         2      3          3         4         4         5          5
        TX Interface Rate [kHz]   400     500     800     1000    2000      2000   2000       2000      4000      4000      4000       4000
        TXDFE.SR                  10      8       5       4       2         2      2          2         1         1         1          1
        RX Interface Rate [kHz]   400     400     800     800     1000      1000   1000       1000      2000      2000      2000       2000
        RXDFE.SR                  10      10      5       5       4         4      4          4         2         2         2          2



6.10.2.6 Modulation Index and Bandwidth Time Product
       The complex continuous-phase baseband signal using GFSK depends on the parameters:
                modulation index h
                time bandwidth product BT
       For details on GFSK, refer to section "Gaussian Frequency Shift Keying" on page 100.
       The modulation index h can be configured with sub-register FSKC0.MIDX which is evaluated for both transmit and
       receive. The sub-register FSKC0.MIDXS allows further scaling of the target modulation index. This sub-register is
       applied at transmit only.
       The bandwidth time product BT can be configured with sub-register FSKC0.BT. When using 4-level FSK, the following
       restrictions apply:
                 h≥1
                 BT = 2
       With regard to the definition of the modulation index h in conjunction with 4-level FSK, please refer to section "Gaussian
       Frequency Shift Keying" on page 100.

6.10.2.7 PHR-PSDU Data Rate
       The actual PHR-PSDU data rate fD depends on the symbol rate 1/T, the modulation order and whether FEC is enabled,
       see Table 6-52.

       Table 6-52. Data Rate at PHR-PSDU

        Modulation Order                         FEC enabled                                  PHR-PSDU Data Rate fD
        2-level                                  no                                           1/T
        4-level                                  no                                           2/T




                                                                                       Atmel AT86RF215 - DATASHEET                           88
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 89 -->

       Modulation Order                          FEC enabled                                 PHR-PSDU Data Rate fD
       2-level                                   yes                                         1/(2T)
       4-level                                   yes                                         1/T

6.10.3 PPDU Types
       The structure of the Physical Protocol Data Unit (PPDU) is based on the specification of IEEE Std 802.15.4g™-2012.
       The standard introduces concurrent sensing (dual sense) of “uncoded” versus “coded” packets, applying predefined
       pairs of synchronization words (SFD0, SFD1). The term “coded” means that FEC is enabled, whereas “uncoded” means
       that FEC is disabled.
       The AT86RF215 provides extended usage of the dual sense mechanism in order to support simultaneous sensing of
       proprietary PPDUs and/or IEEE PPDUs. The PPDU types are described below.

6.10.3.1 SFD-16 (SFD0/1 PPDU)

                          2-level                                2-level or 4-level




         Preamble (phyFSKPreambleLength x 8)   SFD-16     PHR              PSDU




                                           SFD0 or SFD1         uncoded or coded


       This PPDU is suitable for operation according to IEEE Std 802.15.4g™-2012 [3], containing Preamble, SFD (either
       SFD0 or SFD1), PHR and PSDU.
       The Preamble consists of phyFSKPreambleLength multiples of the sequence 01010101, configurable with sub-registers
       FSKC1.FSKPLH and FSKPLL.FSKPLL.
       The sequence of the SFD consists of 16bits (SFD-16). At transmit, selection of the SFD (either SFD0 or SFD1) is
       configured with sub-register FSKPHRTX.SFD.
       The actual bit sequence of SFD0 and SFD1 can be configured with registers BBCn_FSKSFD0H, BBCn_FSKSFD0L
       and BBCn_FSKSFD1H, BBCn_FSKSFD1L, respectively.

6.10.3.2 RAW-SFD-16 (RAW-SFD0/1-PPDU)

                          2-level                                2-level or 4-level




         Preamble (phyFSKPreambleLength x 8)   SFD-16               PSDU




                                           SFD0 or SFD1         uncoded or coded


       This proprietary PPDU is similar to the SFD0/1-PPDU with the exception that the PHY header field (PHR) is omitted.




                                                                                      Atmel AT86RF215 - DATASHEET                     89
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 90 -->

6.10.3.3 SFD-32 (SFD0-SFD1-PPDU)
                                   2-level                                   2-level or 4-level




         Preamble (phyFSKPreambleLength x 8)            SFD-32         PHR             PSDU



                                                     SFD0    SFD1         uncoded or coded

       This proprietary PPDU is similar to the SFD0/1-PPDU, except that the SFD part is the concatenation of the
       synchronization words SFD0 and SFD1 (SFD-32). Dual sense is not supported.

6.10.3.4 RAW-SFD-32 (RAW-SFD0-SFD1-PPDU)
                                   2-level                                   2-level or 4-level




         Preamble (phyFSKPreambleLength x 8)            SFD-32                  PSDU



                                                     SFD0    SFD1            uncoded or coded

       This proprietary PPDU is similar to the SFD0-SFD1-PPDU, except that the PHY header field (PHR) is omitted.

6.10.3.5 PPDU Configuration
       Instead of assuming a fixed assignment of SFD0 and SFD1 in the context of IEEE Std 802.15.4g™-2012 [3], (“uncoded”
       vs. “coded”), the AT86RF215 employs extended interpretation of the SFD.
       The interpretation of SFD0 and SFD1 can be configured using sub-registers FSKC4.CSFD0 and FSKC4.CSFD1,
       respectively. The configuration is evaluated at both, transmit and receive. This supports dual sense or single sense of
       various PPDU types. At transmit, the actual selection of the SFD (either SFD0 or SFD1) is configured with sub-register
       FSKPHRTX.SFD. In case FSKC4.SFD32 is set to 1 (single sense), the configuration of FSKC4.CSFD1 is irrelevant.

6.10.4 Transmit Operation and Configuration
6.10.4.1 General Transmit Configuration
       The basic settings of modulation and coding can be configured according to "Coding and Modulation" on page 86.
       During this configuration, the AT86RF215 shall be in state TRXOFF.
       As shown in Table 6-51, the value TXDFE.SR must be set according to the symbol rate. The other settings of the
       transmitter frontend are more flexible depending on the spectral requirements. Recommended values for modulation
       index ½ and 1 are shown in Table 6-53 and Table 6-54, respectively.

       Table 6-53. Recommended Configuration of the Transmitter Frontend (modulation index 0.5) )

        Register                                                       Symbol Rate [kHz]
                              50               100               150             200                  300                   400
        TXCUTC.PARAMP         3                2                 2               2                    1                     1
        TXCUTC.LPFCUT         0                1                 3               4                    6                     7
        TXDFE.RCUT            0                0                 0               0                    0                     0




                                                                                       Atmel AT86RF215 - DATASHEET                     90
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 91 -->

       Table 6-54. Recommended Configuration of the Transmitter Frontend (modulation index 1)

        Register                                                       Symbol Rate [kHz]
                             50               100                150           200                     300                   400
        TXCUTC.PARAMP        3                2                  2             2                       1                     1
        TXCUTC.LPFCUT        0                3                  5             6                       8                     9
        TXDFE.RCUT           4                4                  4             4                       4                     4


       Table 6-55 and Table 6-56 provide the complete list of possible register settings in order to enable FEC. The notation
       “[1]”, refers to the MSB of the corresponding register.

       Table 6-55. Enabling FEC (FSKC4.SFD32 = 0)

        Register                                                                Value

        FSKPHRTX.SFD                                     0                                                        1

        FSKC4.CSFD0[1]              0                        1                       -                                -

        FSKC4.CSFD1[1]              -                        -                       0                                1

        FEC enabled                 no                       yes                     no                               yes



       Table 6-56. Enabling FEC (FSKC4.SFD32 = 1)

        Register                                                                     Value

        FSKC4.CSFD0[1]                        0                                             1

        FEC enabled                           no                                            yes


       Prior to transmission, the AT86RF215 must be in state TXPREP, see section "State Machine" on page 33. A
       transmission is initiated with register CMD.CMD set to TX, see "State Machine" on page 33. Assembly of a complete
       PPDU is performed autonomously, including all signal processing steps, such as FEC, interleaving, and modulation.

6.10.4.2 Direct Modulation RF215 v.3 (RF_VN = 0x03)
       AT86RF215 v.3 provides the additional feature to set the transmitter to direct modulation. The direct modulation shall be
       used for all FSK modes. It improves the modulation quality especially at high output power (>8dBm).
       The direct modulation is enabled by:
            Sub-register TXDFE.DM = 1
            Sub-register FSKDM.EN = 1
       The FSK modulation quality can be optimized by setting pre-emphasis filter. The pre-emphasis filter settings depend on
       the symbol rate and have the same settings for 2-FSK and 4-FSK. It is recommended to enable the pre-emphasis
       filtering by sub-register FSKDM.PE=1 and choose following pre-emphasis filter setting:




                                                                                     Atmel AT86RF215 - DATASHEET                        91
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 92 -->

      Table 6-57. Pre-emphasis setting for FSK direct modulation

       Symbol Rate          Sub-register FSKPE0                   Sub-register FSKPE1                     Sub-register FSKPE2
       50kHz                            0x02                             0x03                                           0xFC
       100kHz                           0x0E                             0x0F                                           0xF0
       150kHz                           0x3C                             0x3F                                           0xC0
       200kHz                           0x74                             0x7F                                           0x80
       300kHz                           0x05                             0x3C                                           0xC3
       400kHz                           0x13                             0x29                                           0xC7


      When the direct modulation (TXDFE.DM = 1, FSKDM.EN = 1) is enabled together with pre-emphasis (FSKDM.PE=1),
      adjusting the bandwidth time product BT by register FSKC0.BT is without effect.
      It is therefore recommended to apply pre-emphasis only for symbol rates above 100kHz.


6.10.4.3 IEEE Mode
      For a PPDU without mode switch (see, [3] sub-clause 18.1.1), the PHR sub-fields shall be configured as indicated in
      Figure 6-19.

      Figure 6-19. MR-FSK TX-PHR

      MS   R1                  R0                 FCS             DW                   L10-L0
      0    FSKPHRTX.RB1        FSKPHRTX.RB2       PC.FCST         FSKPHRTX.DW          BBCn_TXFLH,BBCn_TXFLL


      In order to configure and transmit a PPDU with mode switch (see, [3] sub-clause 18.1.1), the RAW mode shall be
      applied, see section "RAW Mode" below. In this case, the 16 PHR bits shall be considered as a 2 octet PSDU to be
      stored in the TX frame buffer. Since the RAW mode can be combined with FEC, the AT86RF215 supports transmit of a
      coded mode switch PPDU.

6.10.4.4 RAW Mode
      The RAW mode can be enabled, according to the settings shown in Table 6-58 and Table 6-59. The notation “[0]”,
      refers to the LSB of the corresponding register.



      Table 6-58. Enabling RAW Mode (FSKC4.SFD32 = 0)

       Register                                                                 Value

       FSKPHRTX.SFD                                     0                                                       1

       FSKC4.CSFD0[0]               0                       1                      -                                -

       FSKC4.CSFD1[0]               -                       -                      0                                1

       RAW mode enabled             no                      yes                    no                               yes




                                                                                   Atmel AT86RF215 - DATASHEET                        92
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| MS | R 1 | R 0 | FCS | DW | L -L 10 0 |
| --- | --- | --- | --- | --- | --- |
| 0 | FSKPHRTX.RB1 | FSKPHRTX.RB2 | PC.FCST | F SKPHRTX.DW | BBCn_TXFLH,BBCn_TXFLL |


<!-- page 93 -->

       Table 6-59. Enabling RAW Mode (FSKC4.SFD32 = 1)

        Register                                                                     Value

        FSKC4.CSFD0[0]                      0                                            1

        RAW mode enabled                    no                                           yes


       In RAW mode, assembly of the PHR is bypassed. Information of the TX frame buffer is passed to the baseband
       processor octet by octet. In contrast to the IEEE mode, the bit order of each octet can be configured with sub-register
       FSKC4.RAWRBIT. The PSDU length can be configured with registers BBCn_TXFLH and BBCn_TXFLL.
       In RAW mode, the following baseband functionality is always disabled:
              Whitening,
              Automatic FCS computation.

6.10.5 Receive Operation and Configuration
6.10.5.1 General Receive Configuration
       The settings for coding and modulation can be configured according to "Coding and Modulation" on page 86. During
       this configuration, the AT86RF215 shall be in state TRXOFF.
       As shown in Table 6-51, the value RXDFE.SR must be set according to the symbol rate. The other settings of the
       receiver frontend are more flexible. Due to higher allowed radio frequency tolerance according to [3], clause 18.1.5.3.,
       and the requirements for receiver interference rejection, clause 18.1.5.8, it is advantageous to separate the receiver
       frontend configurations into a sub-1GHz and a 2.4 GHz section.
       Recommended values for modulation index ½ and 1 in sub-1GHz band are shown in Table 6-60 and Table 6-62,
       respectively. Recommended values for modulation index ½ and 1 in 2.4GHz band are shown in Table 6-61 and Table
       6-63, respectively.

       Table 6-60. Recommended Configuration values of the sub-1GHz Receiver Frontend (modulation index 1/2)

        Register                                                     Symbol Rate [kHz]
                            50              100              150               200                  300                   400
        RXBWC.BW            0               1                3                 3                    5                     6
        RXBWC.IFS           0               0                0                 0                    1                     0
        RXDFE.RCUT          0               0                0                 1                    0                     0
        AGCC.AVGS           0               0                0                 0                    0                     0
        AGCS.TGT            1               1                1                 1                    1                     1




                                                                                     Atmel AT86RF215 - DATASHEET                     93
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 94 -->

       Table 6-61. Recommended Configuration values of the 2.4GHz Receiver Frontend (modulation index 1/2)

        Register                                                  Symbol Rate [kHz]
                           50             100              150              200                  300                   400
        RXBWC.BW           0              1                3                4                    6                     7
        RXBWC.IFS          0              0                0                0                    0                     0
        RXDFE.RCUT         0              0                0                1                    0                     1
        AGCC.AVGS          0              0                0                0                    0                     0
        AGCS.TGT           1              1                1                1                    1                     1



       Table 6-62. Recommended Configuration values of the sub-1GHz Receiver Frontend (modulation index 1)

        Register                                                  Symbol Rate [kHz]
                           50             100              150              200                  300                   400
        RXBWC.BW           0              3                4                5                    6                     8
        RXBWC.IFS          0              0                0                1                    0                     1
        RXDFE.RCUT         1              1                1                2                    1                     1
        AGCC.AVGS          0              0                0                0                    0                     0
        AGCS.TGT           1              1                1                1                    1                     1



       Table 6-63. Recommended Configuration values of the 2.4 GHz Receiver Frontend (modulation index 1)

        Register                                                  Symbol Rate [kHz]
                           50             100              150              200                  300                   400
        RXBWC.BW           1              4                6                6                    7                     8
        RXBWC.IFS          0              0                0                0                    0                     1
        RXDFE.RCUT         1              1                2                3                    1                     2
        AGCC.AVGS          0              0                0                0                    0                     0
        AGCS.TGT           1              1                1                1                    1                     1



6.10.5.2 Preamble Detection
       During preamble search, the sub-core is in state LISTEN. This state can be observed with AGCC.FRZS = 0.
       The receiver scans for a preamble pattern by doing advanced signal processing on the correlator output (value C) and
       comparing the result to a threshold TPREAMBLE.




                                                                                  Atmel AT86RF215 - DATASHEET                     94
                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 95 -->

       Figure 6-20. Simplified State Diagram of Preamble Detector




                                                                          LISTEN
                                                                       (AGCC.FRZS = 0)




                                 C ≤ TPREAMBLE && FSKC2.RXPTO = 0                        C > TPREAMBLE
                                 Timeout
                                 Override
                                 PPDU received



                                                                   PREAMBLE_LOCK
                                                                       (AGCC.FRZS = 1)




       The threshold can be adjusted by sub-register FSKC3.PDT. If the value is above the threshold, the sub-core goes to
       state PREAMBLE_LOCK. This state can be observed with AGCC.FRZS = 1.
       If sub-register FSKC2.RXPTO is set to 1, the state PREAMBLE_LOCK is left if no synchronization word has been
       detected within the time of the configured preamble length (timeout). In this configuration, the settings of the preamble
       length (FSKC1.FSKPLH and FSKPLL.FSKPLL) shall be equivalent for both, transmit and receive.
       If sub-register FSKC2.RXPTO is set to 0, the state PREAMBLE_LOCK is left if the correlation C value is no longer
       above the threshold. In this configuration, the settings of the preamble length can be different for transmit and receive.
       Assuming default settings for FSKC3.PDT and FSKC2.PDTM set to 1, the minimum preamble length for robust
       performance is shown in Table 6-64.

       Table 6-64.   Minimum Preamble Length

        Symbol Rate [kHz]                                         Minimum Preamble Length [octets]
        50                                                        2
        100                                                       3
        150                                                       8
        200                                                       8
        300                                                       8
        400                                                       10



6.10.5.3 Synchronization Word Detection
       Prior to synchronization word detection, the sub-core must be in state PREAMBLE_LOCK, see section "Preamble
       Detection" on page 94.
       Synchronization word detection is based on correlation of the expected synchronization words w0 (SFD0, configured
       with BBCn_FSKSFD0H, BBCn_FSKSFD0L) and w1 (SFD1, configured with BBCn_FSKSFD1H, BBCn_FSKSFD1L)
       with the sequence of binary frequency estimates obtained from the demodulator.




                                                                                         Atmel AT86RF215 - DATASHEET                     95
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 96 -->

For dual sense (FSKC4.SFD32 = 0), the receiver simultaneously checks for hypothesis H0 and H1. The hypothesis H0 is
considered true (H0 = 1) if the corresponding correlation with w0 is above a threshold. Similar, the hypothesis H1 is
considered true (H1 = 1) if the corresponding correlation with w1 is above a threshold. For further details on the SFD
correlation, please refer to section "SFD-Correlation" on page 100.
Based on H0 and H1, the receiver proceeds as shown in Table 6-65. The decision is indicated with FSKPHRRX.SFD.
Note that the receiver prefers configuration FSKC4.CSFD0, in case both hypothesis are true.

Table 6-65. Decision at Dual Sense Mode

H0               H1              Decision
0                0               None
1                0               Receiver applies configuration FSKC4.CSFD0 and indicates FSKPHRRX.SFD = 0.
0                1               Receiver applies configuration FSKC4.CSFD1 and indicates FSKPHRRX.SFD = 1.
1                1               Receiver applies configuration FSKC4.CSFD0 and indicates FSKPHRRX.SFD = 0.


For single sense (FSKC4.SFD32 = 1), the receiver checks for a single hypothesis H only. The hypothesis is considered
true (H = 1) if two consecutive correlations with w0 and w1 are above a threshold. For further details on the SFD
correlation refer to section "SFD-Correlation" on page 100.
Based on H, the receiver proceeds as shown in Table 6-66.

Table 6-66. Decision at Single Sense Mode

H                     Decision
0                     None
1                     Receiver applies configuration FSKC4.CSFD0 and always indicates FSKPHRRX.SFD = 0.


The synchronization word detector makes two independent decisions according to the “winning” configuration of
FSKC4.CSFD0 and FSKC4.CSFD1, respectively:
     1.   RAW mode is enabled or disabled
     2.   FEC is enabled or disabled.
The decisions affect consecutive decoding steps.
The threshold configuration FSKC3.SFDT influences the tolerance with regard to correlation errors. A large threshold
reduces the probability of false synchronization events. However, if FEC is to be supported, it is recommended setting
FSKC3.SFDT = 8 in order to benefit from the coding plus processing gain (approx. 5-6dB) introduced by rate ½
convolutional coding.
The synchronization quality (probability of false synchronization, receiver sensitivity) is also influenced by the distance
properties of the synchronization words, especially for dual sense. The standard provides suitable pairs, see IEEE Std
802.15.4g™-2012 [3] sub-clause 18.1.1.2.
If pre-defined synchronization words with sub-optimal distance properties have to be used, it is recommended applying
a larger threshold at the expense of decreased sensitivity. In particular, it is recommended setting
         FSKC3.SFDT = 15
         FSKC4.SFDQ = 1
Based on these settings, the receiver scans for synchronization words matching all bit decisions and discards the PPDU
otherwise.



                                                                              Atmel AT86RF215 - DATASHEET                      96
                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 97 -->

      Dual sense can be disabled with either of the following methods:
                Set FSKC4.SFD32 = 0 and assign equal synchronization word entries to (BBCn_FSKSFD0H,
                 BBCn_FSKSFD0L) and (BBCn_FSKSFD1H, BBCn_FSKSFD1L).
                Set FSKC4.SFD32 = 1 and assign preamble bits to (BBCn_FSKSFD0H, BBCn_FSKSFD0L).

6.10.5.4 IEEE Mode
      If (after synchronization word detection) the receiver proceeds with non-RAW mode, the receiver autonomously
      performs evaluation of the PHR bits. Two cases have to be distinguished:
               PPDU without switch mode and
               PPDU with switch mode.

      PPDU without mode switch
      If the first detected information bit (MS, see Figure 6-19) of the PHR is 0 or mode switch detection is disabled (sub-
      register FSKC2.MSE is set to 0), the receiver autonomously scans for the remaining PHR bits according to IEEE Std
      802.15.4g™-2012 [3] sub-clause 18.1.1.3. and performs:
                Detection of the FCS type,
                De-whitening (if DW = 1),
                PSDU length evaluation.
      Available PPDU based receiver status information are shown in Table 6-67.

      Table 6-67. Receiver Status

       Status                                   Register                                  Description
       Frame length                             BBCn_RXFLL, BBCn_RXFLH                    The detected PSDU length in octets.
       MS                                       FSKPHRRX.MS                               If MS=1, a mode switch PPDU has
                                                                                          been detected.
       Reserved bit R1                          FSKPHRTX.RB1                              The value of the first detected reserved
                                                                                          bit R1.
       Reserved bit R0                          FSKPHRTX.RB2                              The value of the second detected
                                                                                          reserved bit R0.
       FCST                                     FSKPHRRX.FCST                             The value of the detected FCS type.
       DW                                       FSKPHRTX.DW                               The value of the detected DW bit. If
                                                                                          DW=1, de-whitening is automatically
                                                                                          applied at PSDU.
       SFD                                      FSKPHRTX.SFD                              Indicates the decision of the
                                                                                          synchronization word detector, see
                                                                                          section "Synchronization Word
                                                                                          Detection" on page 95.
       Received signal power                    EDV.EDV                                   An estimate of the received signal
                                                                                          power in dBm of the frame.


      Frames with detected PSDU length field entries equal to 0 are automatically discarded (no frame start interrupt RXFS).
      The interrupt behavior is shown in Figure 6-16 on page 83.




                                                                                  Atmel AT86RF215 - DATASHEET                      97
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 98 -->

      PPDU with mode switch
      If the first detected information bit (MS, see Figure 6-19) of the PHR is 1 and mode switch detection is enabled (sub-
      register FSKC2.MSE is set to 1), the 16 PHR bits of a mode switch PPDU are written to the frame buffer without regard
      to their content. In this case, the bit order can be configured with sub-register FSKC4.RAWRBIT. The status information
      of bit MS is stored in sub-register FSKPHRRX.MS indicating that a mode switch packet has been received. Status
      information contained in FSKPHRTX.RB1, FSKPHRTX.RB2, FSKPHRRX.FCST, and FSKPHRRX.DW are invalid and
      shall be ignored. The interrupt behavior is shown in Figure 6-21. Upon detection of a mode switch PPDU, the following
      baseband functionality is automatically disabled:
               FCS evaluation and FCS filtering,
               Address filtering.

      Figure 6-21. Baseband Interrupts during Frame Receive (mode switch PPDU)

                                         tRXFE

      RF Signal        SHR         PHR


      STATE                   RX                  TXPREP


      IRQ
                       AGCH                RXFS
                                           RXFE,AGCR




6.10.5.5 RAW Mode
      If (after synchronization word detection) the receiver proceeds with RAW mode operation, the decoded PSDU bits are
      directly written to the frame buffer octet by octet. In contrast to the IEEE mode, the bit order of each octet can be
      configured with sub-register FSKC4.RAWRBIT. Due to the lack of a pre-defined PHY header (PHR), information about
      the expected PSDU length shall be programmed to registers BBCn_FSKRRXFLH and BBCn_FSKRRXFLL. The
      expected PSDU length must be programmed to the RX frame length fields before the interrupt RXFS occurs. The
      interrupt behavior is shown in Figure 6-22. In RAW mode, the following baseband functionalities are always disabled:
               De-whitening,
               FCS evaluation and FCS filtering,
               Address filtering.

      Figure 6-22. Baseband Interrupts during Frame Receive (RAW mode)

                                                            tRXFE


      RF Signal        SHR                       PSDU


      STATE                                  RX                     TXPREP


      IRQ
                       AGCH   RXFS                            RXFE,AGCR




                                                                                 Atmel AT86RF215 - DATASHEET                     98
                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 99 -->

       In case the synchronization word detector decides for a coded RAW-PPDU, the content written to the frame buffer is
       based on the information bits obtained from de-interleaving and de-coding. In this case, the bits are actually not truly
       “raw”. It should be noted, that FEC applies terminated convolutional codes. Hence, care must be taken with respect to
       the settings of the length information (BBCn_FSKRRXFLH and BBCn_FSKRRXFLL).

6.10.5.6 Receiver Override
       The AT86RF215 supports receiver override (RXO) in order to mitigate the capture effect. The receiver goes back to
       state LISTEN if both applies:
                the preamble detector is in state PREAMBLE_LOCK,
                the receiver strength rapidly increases above a threshold.
       The threshold can be configured with sub-register FSKC2.RXO. If set to 3, RXO is disabled.

6.10.5.7 Reduced Power Consumption (RPC)
       The MR-FSK core supports receive operation with reduced power consumption (RPC) during state LISTEN. RPC is
       enabled with sub-register FSKRPC.EN set to 1.
       The principle applied for power saving is illustrated in Figure 6-23. If RPC is enabled, the baseband core automatically
       toggles between two internal receive modes ON and OFF. During receive mode OFF, the blocks of the receiver front
       end are switched off. The corresponding blocks are enabled, once the baseband is in receive mode ON.
       Apparently, preamble detection is only enabled at receive mode ON. As illustrated in Figure 6-23, the preamble of the
       incoming frame could not be detected at the first time interval t1 during receive mode ON. At the consecutive time
       interval with receive mode ON, the duration tMIN was sufficient for preamble detection leading to state
       PREAMBLE_LOCK. From this time, the transition to OFF is automatically blocked, leading to normal receive operation
       of the remaining PPDU signal. The AT86RF215 indicates state RX during receive regardless of the receive mode
       ON/OFF.

       Figure 6-23. RPC Mode

                                                    t1          tMIN


       RF Signal                                          Preamble          SFD   PHR      PSDU


       STATE                                                     RX                                           TXPREP


       PDT_STATE                             LISTEN                          PREAMBLE_LOCK


       RX_MODE             ON       OFF        ON        OFF                      ON

                                      tOFF      tON


       IRQ
                                                                     AGCH               RXFS              RXFE,AGCR




       The minimal ON time ton equates to the minimal preamble length of the receiver which depends on the FSK symbol rate,
       see Table 6-64. When configuring the RX preamble length to <8 the register FSKC2.PDTM must be set to 1.
       In order to assure reliable preamble detection, the following settings are recommended:

                  tON  t MIN (minimal RX preamble length, Table 6-64)

                  2t ON  t OFF  t TX -Preamble


                                                                                           Atmel AT86RF215 - DATASHEET                        99
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 100 -->

       Consequently, TX and RX device have different settings for the preamble length, and sub-register FSKC2.RXPTO must
       be set to 0. There is one register set for preamble length setting (BBCn_FSKPLL, FSKC1.FSKPLH) for the receive and
       transmit mode, at transmission the preamble length needs to be re-configured this includes the ACK and also the
       automatic ACK (AACK) feature.
       The duration tON can be configured with register BBCn_FSKRPCONT and sub-register FSKRPC.BASET.
       The duration tOFF can be configured with register BBCn_FSKRPCOFFT and sub-register FSKRPC.BASET.
       The RPC mode should not be used during energy measurement, see section "Energy Measurement" on page 56.
       Energy measurements during RPC may lead to incorrect energy detection values EDV.EDV. Also RSSI values may not
       be correct RFn_RSSI.

6.10.6 Appendix
6.10.6.1 Gaussian Frequency Shift Keying
       The phase of the ideal continuous-phase baseband signal using Gaussian Frequency Shift Keying (GFSK) is given as

                                                           h
                                                               t
                                                 (t )         xS (k ) g BT (  kT )d
                                                           T 0 k

       with discrete-time frequency symbol sequence {xS (k )} , symbol rate 1 / T , and modulation index h.

                                                                              h
       The corresponding frequency deviation is defined as         f dev       .
                                                                             2T
       The Gaussian impulse g BT is defined as

                       1  t 1               t 1 
                                                                                                                         t
                                                                                 2                    2
            g BT (t )  erf  (  )   erf  (  ) ,
                       2  T 2               T 2 
                                                                             
                                                                                ln2
                                                                                    BT and erf(t )    
                                                                                                       0
                                                                                                          exp(  2 )d

       depending on the bandwidth time product BT.

       Based on this definition, the modulation index h is independent of the alphabet of the frequency values xS (k ) . In

       particular,   4-level FSK uses inner frequency values xS (k ) { 1              , 1 } in addition to outer frequency values
                                                                                    3       3
       xS (k ) {1,1} , see Table 6-50. This should be taken into consideration when configuring the device with Filtered
       4FSK according to IEEE Std 802.15.4g™-2012 [3], which uses a slightly different definition of the modulation index. The
       modulation index of 0.33 for Filtered 4FSK is obtained with h = 1, which in turn is configured with sub-register
       FSKC0.MIDX = 3.

6.10.6.2 SFD-Correlation
       Synchronization word detection is based on correlation of the expected synchronization words w0 (SFD0, configured
       with BBCn_FSKSFD0H, BBCn_FSKSFD0L) and w1 (SFD1, configured with BBCn_FSKSFD1H, BBCn_FSKSFD1L)
       with the sequence of binary frequency estimates {xˆ S (k )} obtained from the demodulator.

       The synchronization word detector applies soft-decisions in order to support a quality criterion of the correlation. The
       frequency estimates (obtained from the demodulator at the symbol rate) are quantized soft values from the set
       {-7,-6,..,-1,0,+1,..,+7} with
               -7 indicating a very reliable estimate of a negative frequency,
                0 indicating a completely unreliable frequency estimate,



                                                                                             Atmel AT86RF215 - DATASHEET                      100
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 101 -->

                 +7 indicating a very reliable estimate of a positive frequency.
       For dual sense (FSKC4.SFD32 = 0), the receiver simultaneously checks for hypothesis H0 and H1 related to the
       synchronization words w0 and w1, respectively:
                                                            15
                                                  H p :  wp (n) xˆS (k  n)  TSFD with p  0,1
                                                            n 0

       The threshold is given as

                                                                   TSFD  7  FSKC3.SFDT
       For single sense (FSKC4.SFD32 = 1), a synchronization word is considered as detected if


                                            15                                    15
                                     H :  w0 (n) xˆS (k  n)  TSFD and  w1 (n) xˆS (k  n  16)  TSFD
                                         n 0                                  n 0

       Setting FSKC4.SFDQ = 1 forces soft values to hard quantized values (either -7 if negative or +7 if non-negative) prior to
       correlation.

6.10.7 Register Description
6.10.7.1 BBCn_FSKC0 – FSK Configuration Byte 0
       This register configures the FSK PHY.
        Bit                7            6               5            4        3         2              1             0
                                BT                           MIDXS                     MIDX                       MORD           BBCn_FSKC0
        Read/Write        RW           RW           RW               RW      RW        RW            RW            RW
        Initial Value      1            1               0            1        0         1              1             0

        Bit 7:6 – FSKC0.BT: FSK Bandwidth Time Product
       These bits configure the shaping for filtered FSK modulation, where B is the 3 dB bandwidth of the shaping filter and T
       is the FSK symbol period.

       Table 6-68. BT

        Sub-register           Value         Description
        BT                      0x0          BT = 0.5
                                0x1          BT = 1.0
                                0x2          BT = 1.5
                                0x3          BT = 2.0

        Bit 5:4 – FSKC0.MIDXS: Modulation Index Scale
       These bits configure the scaling factor s with regard to MIDX. The effectively applied modulation index results in the
       modulation index configured with MIDX times s.




                                                                                              Atmel AT86RF215 - DATASHEET                     101
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| BT | 0x0 | BT = 0.5 |
|  | 0x1 | BT = 1.0 |
|  | 0x2 | BT = 1.5 |
|  | 0x3 | BT = 2.0 |


<!-- page 102 -->

       Table 6-69. MIDXS

       Sub-register            Value        Description
       MIDXS                   0x0          s = 1.0 - 1/8
                               0x1          s = 1.0
                               0x2          s = 1.0 + 1/8
                               0x3          s = 1.0 + 1/4

        Bit 3:1 – FSKC0.MIDX: Modulation Index
       These bits configure the modulation index.

       Table 6-70. MIDX

       Sub-register            Value        Description
       MIDX                    0x0          Modulation index = 0.375
                               0x1          Modulation index = 0.5
                               0x2          Modulation index = 0.75
                               0x3          Modulation index = 1.0
                               0x4          Modulation index = 1.25
                               0x5          Modulation index = 1.5
                               0x6          Modulation index = 1.75
                               0x7          Modulation index = 2.0

        Bit 0 – FSKC0.MORD: FSK Modulation Order
       This bit configures the modulation order.

       Table 6-71. MORD

       Sub-register            Value        Description
       MORD                    0x0          2-FSK
                               0x1          4-FSK

6.10.7.2 BBCn_FSKC1 – FSK Configuration Byte 1
       This register configures the FSK PHY.
       Bit                7            6              5        4         3             2             1             0
                              FSKPLH                  FI        –                           SRATE                              BBCn_FSKC1
       Read/Write        RW            RW             RW      RW        RW             RW           RW           RW
       Initial Value      0            0              0        0         0             0             0             0

        Bit 7:6 – FSKC1.FSKPLH: FSK Preamble Length High Byte
       The FSK preamble length in octets is configured by the 10-bit setting {FSKPLH,FSKPLL}.

        Bit 5 – FSKC1.FI: Frequency Inversion
       If this bit is set to 1, the sign of the FSK deviation frequency is inverted.




                                                                                            Atmel AT86RF215 - DATASHEET                     102
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| MIDXS | 0x0 | s = 1.0 - 1/8 |
|  | 0x1 | s = 1.0 |
|  | 0x2 | s = 1.0 + 1/8 |
|  | 0x3 | s = 1.0 + 1/4 |

| Sub-register | Value | Description |
| --- | --- | --- |
| MIDX | 0x0 | Modulation index = 0.375 |
|  | 0x1 | Modulation index = 0.5 |
|  | 0x2 | Modulation index = 0.75 |
|  | 0x3 | Modulation index = 1.0 |
|  | 0x4 | Modulation index = 1.25 |
|  | 0x5 | Modulation index = 1.5 |
|  | 0x6 | Modulation index = 1.75 |
|  | 0x7 | Modulation index = 2.0 |

| Sub-register | Value | Description |
| --- | --- | --- |
| MORD | 0x0 | 2-FSK |
|  | 0x1 | 4-FSK |


<!-- page 103 -->

        Bit 3:0 – FSKC1.SRATE: MR-FSK Symbol Rate
       Table 6-72. SRATE

       Sub-register           Value        Description
       SRATE                  0x0          50kHz
                              0x1          100kHz
                              0x2          150kHz
                              0x3          200kHz
                              0x4          300kHz
                              0x5          400kHz

6.10.7.3 BBCn_FSKC2 – FSK Configuration Byte 2
       This register configures the FSK PHY.
       Bit               7            6             5         4          3          2             1             0
                       PDTM                 RXO             RXPTO       MSE        PRI          FECS         FECIE          BBCn_FSKC2
       Read/Write       RW            RW            RW       RW         RW         RW           RW            RW
       Initial Value     0            1             0         0          0          0             0             1

        Bit 7 – FSKC2.PDTM: Preamble Detection Mode
       This sub-field configures the preamble detection mode for the MR-FSK-PHY. It is recommended to enable this sub-
       register only if the preamble length is less than 8 octets.

       Table 6-73. PDTM

       Sub-register           Value        Description
       PDTM                   0x0          Preamble detection does not take RSSI values into account
                              0x1          Preamble detection takes RSSI values into account.

        Bit 6:5 – FSKC2.RXO: Receiver Override
       If Receiver Override is enabled during frame reception, the FSK receiver restarts synchronization after a rapid input
       signal increase. The minimum input signal level is -110dBm.

       Table 6-74. RXO

       Sub-register           Value        Description
       RXO                    0x0          Receiver restarted by > 6dB stronger frame
                              0x1          Receiver restarted by >12dB stronger frame
                              0x2          Receiver restarted by >18dB stronger frame
                              0x3          Receiver override disabled

        Bit 4 – FSKC2.RXPTO: Receiver Preamble Time Out
       If this bit is set to 1, the FSK receiver restarts synchronization if no valid SFD field was found within a complete FSK
       preamble length period {FSKPLH,FSKPLL}. If this bit is set to 0, the FSK receiver restarts synchronization upon lost
       preamble autocorrelation if no valid SFD field was found.




                                                                                         Atmel AT86RF215 - DATASHEET                     103
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SRATE | 0x0 | 50kHz |
|  | 0x1 | 100kHz |
|  | 0x2 | 150kHz |
|  | 0x3 | 200kHz |
|  | 0x4 | 300kHz |
|  | 0x5 | 400kHz |

| Sub-register | Value | Description |
| --- | --- | --- |
| PDTM | 0x0 | Preamble detection does not take RSSI values into account |
|  | 0x1 | Preamble detection takes RSSI values into account. |

| Sub-register | Value | Description |
| --- | --- | --- |
| RXO | 0x0 | Receiver restarted by > 6dB stronger frame |
|  | 0x1 | Receiver restarted by >12dB stronger frame |
|  | 0x2 | Receiver restarted by >18dB stronger frame |
|  | 0x3 | Receiver override disabled |


<!-- page 104 -->

       Table 6-75. RXPTO

       Sub-register           Value        Description
       RXPTO                   0x0         Receiver preamble timeout disabled
                               0x1         Receiver preamble timeout enabled

        Bit 3 – FSKC2.MSE: Mode Switch Enable
       If this bit is set to 1, the mode switch PHR bit of an incoming frame is evaluated.

       Table 6-76. MSE

       Sub-register           Value        Description
       MSE                     0x0         Mode Switch disabled
                               0x1         Mode Switch enabled

        Bit 2 – FSKC2.PRI: Preamble Inversion
       If this bit is set to 1, the sign of the FSK deviation frequency belonging to the preamble part is inverted.

        Bit 1 – FSKC2.FECS: FEC Scheme
       If this bit is set to 0, a non-recursive and non-systematic convolutional code (NRNSC) is employed. Otherwise, a
       recursive and systematic convolutional code (RSC) is employed.

       Table 6-77. FECS

       Sub-register           Value        Description
       FECS                    0x0         NRNSC
                               0x1         RSC

        Bit 0 – FSKC2.FECIE: FEC Interleaving Enable
       If MR-FSK forward error correction is enabled, this bit allows to enable or disable code-symbol interleaving.

       Table 6-78. FECIE

       Sub-register           Value        Description
       FECIE                   0x0         Interleaving disabled
                               0x1         Interleaving enabled

6.10.7.4 BBCn_FSKC3 – FSK Configuration Byte 3
       This register configures the FSK PHY.
       Bit                7           6             5             4      3         2            1             0
                                            SFDT                                       PDT                                BBCn_FSKC3
       Read/Write        RW           RW           RW         RW        RW        RW          RW            RW
       Initial Value      1           0             0             0      0         1            0             1

        Bit 7:4 – FSKC3.SFDT: SFD Detection Threshold
       Lower values increase the SFD detector sensitivity. Higher values increase the SFD selectivity. The default value 8 is
       recommended for simultaneous sensing of the SFD pairs according to IEEE 802.15.4g. It is recommended to set
       SFDT=15 and SFDQ=1 for SFD patterns with weak or unknown cross-correlation properties.

        Bit 3:0 – FSKC3.PDT: Preamble Detection Threshold
       Lower values increase the preamble detector sensitivity.




                                                                                       Atmel AT86RF215 - DATASHEET                     104
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| RXPTO | 0x0 | Receiver preamble timeout disabled |
|  | 0x1 | Receiver preamble timeout enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| MSE | 0x0 | Mode Switch disabled |
|  | 0x1 | Mode Switch enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| FECS | 0x0 | NRNSC |
|  | 0x1 | RSC |

| Sub-register | Value | Description |
| --- | --- | --- |
| FECIE | 0x0 | Interleaving disabled |
|  | 0x1 | Interleaving enabled |


<!-- page 105 -->

6.10.7.5 BBCn_FSKC4 – FSK Configuration Byte 4
       This register configures the FSK PHY.
       Bit                7           6            5           4            3            2             1             0
                          –          SFDQ        SFD32     RAWRBIT               CSFD1                     CSFD0                 BBCn_FSKC4
       Read/Write         R           RW          RW          RW            RW           RW          RW            RW
       Initial Value      0           0            0           1            1            0             0             0

        Bit 6 – FSKC4.SFDQ: SFD Quantization
       If this bit is set to 1, the FSK receiver applies a hard decisions rather than a soft decisions at the bit positions with
       regard to SFD search.

        Bit 5 – FSKC4.SFD32: SFD 32Bit
       If this bit is zero, the FSK receiver simultaneously searches for two 16-bit SFD fields configured with
       {FSKSFD0H;FSKSFD0L} and {FSKSFD1H;FSKSFD1L}, respectively. If this bit is set to 1, the FSK receiver searches
       for a single 32-bit SFD {FSKSFD1H;FSKSFD1L;FSKSFD0H;FSKSFD0L}. (LSB 1st)

       Table 6-79. SFD32

       Sub-register           Value        Description
       SFD32                   0x0         Search for two 16-bit SFD
                               0x1         Search for a single 32-bit SFD

        Bit 4 – FSKC4.RAWRBIT: RAW mode Reversal Bit
       This bit configures the bit order of the payload octets in RAW mode. If set to 1, the order is MSB first.

        Bit 3:2 – FSKC4.CSFD1: Configuration of PPDU with SFD1
       This register configures the PPDU with SFD1.

       Table 6-80. CSFD1

       Sub-register           Value        Description
       CSFD1                   0x0         Uncoded IEEE mode
                               0x1         Uncoded RAW mode
                               0x2         Coded IEEE mode
                               0x3         Coded RAW mode

        Bit 1:0 – FSKC4.CSFD0: Configuration of PPDU with SFD0
       This register configures the PPDU with SFD0.

       Table 6-81. CSFD0

       Sub-register           Value        Description
       CSFD0                   0x0         Uncoded IEEE mode
                               0x1         Uncoded RAW mode
                               0x2         Coded IEEE mode
                               0x3         Coded RAW mode

6.10.7.6 BBCn_FSKPLL – FSK Preamble Length Low Byte
       This register configures the FSK Preamble Length.




                                                                                              Atmel AT86RF215 - DATASHEET                     105
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SFD32 | 0x0 | Search for two 16-bit SFD |
|  | 0x1 | Search for a single 32-bit SFD |

| Sub-register | Value | Description |
| --- | --- | --- |
| CSFD1 | 0x0 | Uncoded IEEE mode |
|  | 0x1 | Uncoded RAW mode |
|  | 0x2 | Coded IEEE mode |
|  | 0x3 | Coded RAW mode |

| Sub-register | Value | Description |
| --- | --- | --- |
| CSFD0 | 0x0 | Uncoded IEEE mode |
|  | 0x1 | Uncoded RAW mode |
|  | 0x2 | Coded IEEE mode |
|  | 0x3 | Coded RAW mode |


<!-- page 106 -->

       Bit              7          6          5          4            3        2              1             0
                                                             FSKPLL                                                    BBCn_FSKPLL
       Read/Write      RW         RW         RW         RW            RW      RW            RW            RW
       Initial Value    0          0          0          0            1        0              0             0

       Bit 7:0 – FSKPLL.FSKPLL: FSK Preamble Length Low Byte
      This setting controls the FSK preamble length transmitted. The preamble length in octets is configured with the 10 bit
      setting {FSKPLH,FSKPLL}.

6.10.7.7 BBCn_FSKSFD0L – FSK SFD0 Low Byte
       Bit              7          6          5          4            3        2              1             0
                                                          FSKSFD0L                                                    BBCn_FSKSFD0L
       Read/Write      RW         RW         RW         RW            RW      RW            RW            RW
       Initial Value    0          0          0          0            1        0              0             1

       Bit 7:0 – FSKSFD0L.FSKSFD0L: FSK SFD0 Low Byte
      The register is the low byte of FSK start-of-frame delimiter SFD0. (LSB 1st)

6.10.7.8 BBCn_FSKSFD0H – FSK SFD0 High Byte
       Bit              7          6          5          4            3        2              1             0
                                                          FSKSFD0H                                                   BBCn_FSKSFD0H
       Read/Write      RW         RW         RW         RW            RW      RW            RW            RW
       Initial Value    0          1          1          1            0        0              1             0

       Bit 7:0 – FSKSFD0H.FSKSFD0H: FSK SFD0 High Byte
      The register is the high byte of FSK start-of-frame delimiter SFD0. (LSB 1st)

6.10.7.9 BBCn_FSKSFD1L – FSK SFD1 Low Byte
       Bit              7          6          5          4            3        2              1             0
                                                          FSKSFD1L                                                    BBCn_FSKSFD1L
       Read/Write      RW         RW         RW         RW            RW      RW            RW            RW
       Initial Value    1          1          1          1            0        1              1             0

       Bit 7:0 – FSKSFD1L.FSKSFD1L: FSK SFD1 Low Byte
      The register is the low byte of FSK start-of-frame delimiter SFD1. (LSB 1st)

6.10.7.10 BBCn_FSKSFD1H – FSK SFD1 High Byte
       Bit              7          6          5          4            3        2              1             0
                                                          FSKSFD1H                                                   BBCn_FSKSFD1H
       Read/Write      RW         RW         RW         RW            RW      RW            RW            RW
       Initial Value    0          1          1          1            0        0              1             0

       Bit 7:0 – FSKSFD1H.FSKSFD1H: FSK SFD1 High Byte
      The register is the high byte of FSK start-of-frame delimiter SFD1. (LSB 1st)

6.10.7.11 BBCn_FSKPHRTX – FSK PHR TX Information
      This register controls the FSK PHR and SHR for the next transmit frame.




                                                                                     Atmel AT86RF215 - DATASHEET                     106
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 107 -->

       Bit              7             6            5         4            3    2             1             0
                        –             –            –          –          SFD   DW          RB2           RB1        BBCn_FSKPHRTX
       Read/Write       R             R            R         R            RW   RW          RW            RW
       Initial Value    0             0            0         0            0    1             0             0

       Bit 3 – FSKPHRTX.SFD: SFD type
      This bit configures the SFD type of the next transmitted MR-FSK frame.

      Table 6-82. SFD

       Sub-register           Value        Description
       SFD                    0x0          SFD0 is used
                              0x1          SFD1 is used

       Bit 2 – FSKPHRTX.DW: Data Whitening
      This bit corresponds to the IEEE Std 802.15.4g-2012 PIB attribute phyFSKScramblePSDU. If this bit is set to 1, the data
      whitening of the PSDU is enabled, otherwise data whitening of the PSDU is disabled.

      Table 6-83. DW

       Sub-register           Value        Description
       DW                     0x0          PSDU data whitening disabled
                              0x1          PSDU data whitening enabled

       Bit 1 – FSKPHRTX.RB2: Reserved PHR Bit 2
      This bit configures the content of the reserved FSK PHR bit 2 for transmit.

       Bit 0 – FSKPHRTX.RB1: Reserved PHR Bit 1
      This bit configures the content of the reserved FSK PHR bit 1 for transmit.

6.10.7.12 BBCn_FSKPHRRX – FSK PHR RX Information
      This register contains information of the PHR and SHR field of the last received FSK frame. This register is updated
      with IRQ RXFS.
       Bit              7             6            5         4            3    2             1             0
                       FCST           MS           –          –          SFD   DW          RB2           RB1        BBCn_FSKPHRRX
       Read/Write       R             R            R         R            R    R             R            R
       Initial Value    0             0            0         0            0    0             0             0

       Bit 7 – FSKPHRRX.FCST: Frame Check Sequence Type
      This sub-register reflects the content of the PHR FCS bit of the last received FSK frame.

      Table 6-84. FCST

       Sub-register           Value        Description
       FCST                   0x0          FCS type 32-bit
                              0x1          FCS type 16-bit

       Bit 6 – FSKPHRRX.MS: Mode Switch
      This bit reflects the content of the Mode Switch PHR bit of the last received FSK frame.




                                                                                    Atmel AT86RF215 - DATASHEET                     107
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SFD | 0x0 | SFD0 is used |
|  | 0x1 | SFD1 is used |

| Sub-register | Value | Description |
| --- | --- | --- |
| DW | 0x0 | PSDU data whitening disabled |
|  | 0x1 | PSDU data whitening enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| FCST | 0x0 | FCS type 32-bit |
|  | 0x1 | FCS type 16-bit |


<!-- page 108 -->

       Bit 3 – FSKPHRRX.SFD: SFD type
      This bit reflects the detected SFD type of the last received MR-FSK frame.

      Table 6-85. SFD

       Sub-register         Value        Description
       SFD                   0x0         SFD0 detected
                             0x1         SFD1 detected

       Bit 2 – FSKPHRRX.DW: Data Whitening
      This bit corresponds to the IEEE Std 802.15.4g-2012 PIB attribute phyFSKScramblePSDU. If this bit is set to 1, the data
      whitening of the PSDU is enabled, otherwise data whitening of the PSDU is disabled. This bit reflects the content of the
      PHR DW bit of the last received FSK frame. It is not valid in RAW mode operation.

      Table 6-86. DW

       Sub-register         Value        Description
       DW                    0x0         PSDU data whitening disabled
                             0x1         PSDU data whitening enabled

       Bit 1 – FSKPHRRX.RB2: Reserved PHR Bit 2
      This bit reflects the content of the reserved PHR bit 2 of the last received FSK frame.

       Bit 0 – FSKPHRRX.RB1: Reserved PHR Bit 1
      This bit reflects the content of the reserved PHR bit 1 of the last received FSK frame.

6.10.7.13 BBCn_FSKRRXFLL – FSK Raw Mode RX Frame Length Low Byte
       Bit              7           6            5         4            3       2            1             0
                                                            FSKRRXFLL                                               BBCn_FSKRRXFLL
       Read/Write      RW           RW          RW        RW            RW     RW          RW            RW
       Initial Value    1           1            1         1            1       1            1             1

       Bit 7:0 – FSKRRXFLL.FSKRRXFLL: FSK Raw Mode RX Frame Length Low Byte
      This register configures the low byte for the receive frame length of the FSK RAW mode.

6.10.7.14 BBCn_FSKRRXFLH – FSK Raw Mode RX Frame Length High Byte
       Bit              7           6            5         4            3       2            1             0
                        –           –            –          –           –             FSKRRXFLH                    BBCn_FSKRRXFLH
       Read/Write       R           R            R         R            R      RW          RW            RW
       Initial Value    0           0            0         0            0       1            1             1

       Bit 2:0 – FSKRRXFLH.FSKRRXFLH: FSK Raw Mode RX Frame Length High Byte
      This register configures the three MSBs for the receive frame length of the FSK RAW mode.




                                                                                    Atmel AT86RF215 - DATASHEET                     108
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SFD | 0x0 | SFD0 detected |
|  | 0x1 | SFD1 detected |

| Sub-register | Value | Description |
| --- | --- | --- |
| DW | 0x0 | PSDU data whitening disabled |
|  | 0x1 | PSDU data whitening enabled |


<!-- page 109 -->

6.10.7.15 BBCn_FSKDM – FSK Direct Modulation
        Bit               7          6          5           4            3        2            1             0
                          –          –           –          –            –        –           PE            EN           BBCn_FSKDM
        Read/Write       R           R          R           R            R       R           RW            RW
        Initial Value     0          0          0           0            0        0            0             0

        Bit 1 – FSKDM.PE: FSK Preemphasis
       If this sub-register is set to 1, the FSK direct modulation preemphasized. This sub-register is ignored if subregister
       FSKDM.EN is 0.

        Bit 0 – FSKDM.EN: FSK Direct Modulation Enable
       If this sub-register and sub-register RFxx_TXDFE.DM are set to 1, the FSK direct modulation is enabled.

6.10.7.16 BBCn_FSKPE0 – FSK Preemphasis 0
        Bit               7          6          5           4            3        2            1             0
                                                                FSKPE0                                                  BBCn_FSKPE0
        Read/Write      RW          RW         RW          RW            RW      RW          RW            RW
        Initial Value     0          0          0           0            0        0            0             0

        Bit 7:0 – FSKPE0.FSKPE0: FSK Preemphasis 0
       This register contains configuration information for the FSK direct modulation preemphasis.

6.10.7.17 BBCn_FSKPE1 – FSK Preemphasis 1
        Bit               7          6          5           4            3        2            1             0
                                                                FSKPE1                                                  BBCn_FSKPE1
        Read/Write      RW          RW         RW          RW            RW      RW          RW            RW
        Initial Value     0          0          0           0            0        0            0             0

        Bit 7:0 – FSKPE1.FSKPE1: FSK Preemphasis 1
       This register contains configuration information for the FSK direct modulation preemphasis.

6.10.7.18 BBCn_FSKPE2 – FSK Preemphasis 2
        Bit               7          6          5           4            3        2            1             0
                                                                FSKPE2                                                  BBCn_FSKPE2
        Read/Write      RW          RW         RW          RW            RW      RW          RW            RW
        Initial Value     0          0          0           0            0        0            0             0

        Bit 7:0 – FSKPE2.FSKPE2: FSK Preemphasis 2
       This register contains configuration information for the FSK direct modulation preemphasis.


6.10.7.19 RFn_TXDFE – Transmitter TX Digital Frontend
       The register configures the transmitter digital frontend.




                                                                                      Atmel AT86RF215 - DATASHEET                     109
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 110 -->

       Bit              7            6              5      4          3          2            1             0
                                   RCUT                   DM                          SR                                 RFn_TXDFE
       Read/Write      RW            RW             RW    RW         RW         RW          RW            RW
       Initial Value    0            0              0      0          0          0            0             1

       Bit 4 – TXDFE.DM: Direct Modulation
      If this sub-register is set to 1 the transmitter direct modulation is enabled. Direct modulation is available for FSK and
      OQPSK (OQPSKC0.FCHIP=0;1). Direct modulation must also be enabled at the BBCx registers (FSKDM.EN and
      OQPSKC0.DM).

6.10.7.20 BBCn_FSKRPC – FSK Reduced Power Consumption
      This register contains configurations to control the reduced power consumption for the MR-FSK PHY.
       Bit              7            6              5      4          3          2            1             0
                         –           –              –      –         EN                    BASET                       BBCn_FSKRPC
       Read/Write       R            R              R      R         RW         RW          RW            RW
       Initial Value    0            0              0      0          0          0            1             1

       Bit 3 – FSKRPC.EN: Enable
      This bit enables reduced power consumption during the listen phase of the MR-FSK PHY.

       Bit 2:0 – FSKRPC.BASET: Base Time
      This subfield configures the base time for reduced power consumption configuration during the listen phase of the MR-
      FSK PHY (see register FSKRPCONT and FSKRPCOFFT).

      Table 6-87. BASET

       Sub-register          Value        Description
       BASET                 0x0          0.5 us
                             0x1          1.0 us
                             0x2          2.0 us
                             0x3          4.0 us
                             0x4          8.0 us
                             0x5          16.0 us
                             0x6          32.0 us
                             0x7          64.0 us

6.10.7.21 BBCn_FSKRPCONT – FSK Reduced Power Consumption On Time
      This register configures the on time to control the reduced power consumption for the MR-FSK PHY.
       Bit              7            6              5      4          3          2            1             0
                                                           FSKRPCONT                                                BBCn_FSKRPCONT
       Read/Write      RW            RW             RW    RW         RW         RW          RW            RW
       Initial Value    1            0              1      0          0          0            0             0

       Bit 7:0 – FSKRPCONT.FSKRPCONT: FSK Reduced Power Consumption On Time
      This register configures the active period in multiples of the base time (see register FSKRPC).

6.10.7.22 BBCn_FSKRPCOFFT – FSK Reduced Power Consumption Off Time
      This register configures the off time to control the reduced power consumption for the MR-FSK PHY.




                                                                                     Atmel AT86RF215 - DATASHEET                     110
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| BASET | 0x0 | 0.5 us |
|  | 0x1 | 1.0 us |
|  | 0x2 | 2.0 us |
|  | 0x3 | 4.0 us |
|  | 0x4 | 8.0 us |
|  | 0x5 | 16.0 us |
|  | 0x6 | 32.0 us |
|  | 0x7 | 64.0 us |


<!-- page 111 -->

Bit               7         6          5          4          3          2            1             0
                                                                                                                  BBCn_
                                                  FSKRPCOFFT
                                                                                                               FSKRPCOFFT
Read/Write      RW         RW         RW         RW         RW         RW          RW            RW
Initial Value     1         0          1          0          0          0            0             0

 Bit 7:0 – FSKRPCOFFT.FSKRPCOFFT: FSK Reduced Power Consumption Off Time
This register configures the power save period in multiples of the base time (see register FSKRPC).




                                                                            Atmel AT86RF215 - DATASHEET                     111
                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 112 -->

6.11   MR-OFDM PHY

6.11.1 Overview
       The multi-rate and multi-regional orthogonal frequency division multiplexing (MR-OFDM) PHY specified in IEEE Std
       802.15.4g™-2012 [3] and ETSI TS 102 887-1 [5] is RF band agnostic and supports data rates ranging from 50kb/s to
       800kb/s and extended data rates (*) from 1200kb/s to 2400kb/s as listed in Table 6-88.

       Table 6-88. MR-OFDM PHY Options and Modulation Schemes

                               MCS            Option 1         Option 2          Option 3              Option 4
       OFDMC.OPT                              0                1                 2                     3
       Nominal bandwidth                      1094             552               281                   156
       [kHz]
       DFT size                               128              64                32                    16
       Active tones                           104              52                26                    14
       Pilot tones                            8                4                 4                     2
       Data tones                             96               48                24                    12
                                                                     PSDU data rates [kb/s]
       BPSK, rate ½, 4 x       0              100              50                -                     -
       frequency repetition
       BPSK, rate ½, 2 x       1              200              100               50                    -
       frequency repetition
       QPSK, rate ½, 2 x       2              400              200               100                   50
       frequency repetition
       QPSK, rate ½            3              800              400               200                   100
       QPSK, rate ¾            4              1200(*)          600               300                   150
       16-QAM, rate ½          5              1600(*)          800               400                   200
       16-QAM, rate ¾          6              2400(*)          1200(*)           600                   300


       The subcarrier spacing is constant and equal to 10416-2/3 Hz (or 31250/3 Hz). The symbol rate is 8-1/3 ksymbol/s
       which corresponds to 120μs per symbol. This symbol includes a quarter-duration cyclic prefix (CP; 24μs) and a base
       symbol (96μs).
       This PHY includes four options, each one characterized by the number of active tones during the PHR or PSDU. The
       modulation and coding scheme (MCS) allows selecting different PSDU data rates per option. The MCS of the PHY
       header is defined as the lowest available MCS per option accordingly which is zero for Option 1 and 2, one for Option 3
       and two for Option 4, respectively.
       While the MR-OFDM bandwidth option (OFDMC.OPT) is a common prerequisite for transmitter and receiver, the
       transmitter sends the MCS of the PSDU per frame as part of the PHY header (OFDMPHRTX.MCS) which is evaluated
       by the receiver accordingly (OFDMPHRRX.MCS).
       The extended data rates of 1200kb/s, 1600kb/s and 2400kb/s for Option 1 and 1200kb/s for Option 2 use the same
       modulation and coding schemes as the appropriate modes for Option 3 and Option 4. Interleaving for these modes is
       defined in accordance to section 18.2.3.5 of [3].




                                                                                     Atmel AT86RF215 - DATASHEET                     112
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 113 -->

       The frame transmission and reception follows the procedures as described in section "Transceiver Usage in Baseband
       Mode" on page 169 with an basic example provided by section "Example: Transceiver Usage in Baseband Mode" on
       page 170.
       The MR-OFDM PHY is part of each Baseband Core and utilizes the RF frontends as shown in Figure 6-14 via the I/Q
       data interface. The PHY is connected to the appropriate Transmitter Digital Frontend and Receiver Digital Frontend,
       respectively.

6.11.2 Transmitter Configuration
       While MR-OFDM frame transmission generally follows the procedures described in section "Transceiver Usage in
       Baseband Mode" on page 169 , specific configurations as listed in Table 6-89 must be set to prepare the MR-OFDM
       PHY and the associated Digital- and RF-Frontend. A specific order of the shown configuration steps is not required. The
       corresponding register values should only be changed in state TRXOFF.

       Table 6-89. Transmitter Configuration Steps

       No           Action                                                                                                 Register
       0            Activate the MR-OFDM Physical Layer                                                                    PC.PT
       1            Configure MR-OFDM bandwidth option                                                                     OFDMC.OPT
       2            Configure modulation and coding scheme                                                                 OFDMPHRTX.MCS
       3            Select scrambler seed                                                                                  OFDMC.SSTX
       4            Configure PIB attribute phyOFDMInterleaving                                                            OFDMC.POI
       5            Specify I/Q data interface rate of the Transmitter Digital Frontend                                    TXDFE.SR
                    (dependent on OFDMC.OPT)
       6            Specify cut-off frequency of the Transmitter Digital Frontend filter                                   TXDFE.RCUT
                    (dependent on OFDMC.OPT)
       7            Specify cut-off frequency of the Transmitter Analog Frontend filter                                    TXCUTC.LPFCUT
                    (dependent on OFDMC.OPT)
       8            Configure transmit power                                                                               PAC.TXPWR


       The MR-OFDM bandwidth option is the central parameter that determines the sampling rate of the I/Q data interface
       and particular transmit filter settings. Recommended settings are listed in Table 6-90.

       Table 6-90. Recommended Transmitter Frontend Configuration

       Register                   Option 1                  Option 2                   Option 3                        Option 4
       TXDFE.SR                   3                         3                          6                               6
       TXDFE.RCUT                 4                         3                          3                               2
       TXCUTC.LPFCUT              10                        8                          5                               3


       The modulation (OFDMC.OPT), coding scheme (OFDMPHRTX.MCS) and the scrambler seed (OFDMC.SSTX) are
       direct entries to the MR-OFDM PHY header fields, as well as the PSDU length (configured by BBCn_TXFLL and
       BBCn_TXFLH). Additionally, the reserved PHR bits can be configured by OFDMPHRTX.RB5, OFDMPHRTX.RB17,
       OFDMPHRTX.RB18 and OFDMPHRTX.RB21. According to [5] these bits are not evaluated by the receiver.
       The PIB attribute phyOFDMInterleaving as defined in section 9.3. of [3] is configured by OFDMC.POI. It has no
       influence if the MCS has no frequency spreading defined (OFDMPHRTX.MCS = [3,4,5,6]).



                                                                                           Atmel AT86RF215 - DATASHEET                     113
                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 114 -->

       Especially for higher order (16-QAM) modulation with OFDMPHRTX.MCS=[5,6], it is recommended limiting the transmit
       power setting to comply to EVM requirements according to [3] and optimize receiver performance. Recommended
       settings are listed in Table 6-91.

       Table 6-91. Recommended maximum Transmit Power setting and EVM

                                            MCS0          MCS1           MCS2           MCS3            MCS4            MCS5            MCS6
        EVM requirements [3]                -10           -10            -10            -10             -13             -16             -19
        PAC.TXPWR, recommended              31            31             31             31              29              27              25
        PAC.TXPWR, maximum                  31            31             31             31              31              30              28



6.11.3 Receiver Configuration
6.11.3.1 Receiver Configuration Steps
       While MR-OFDM frame reception generally follows the procedures described in section "Example Receive Procedure
       Using Basic Mode" on page 173, specific configurations as listed in Table 6-92 must be set in order to prepare the MR-
       OFDM PHY and the associated Digital- and RF-Frontend. A specific order of the shown configuration steps is not
       required. The corresponding register values should only be changed in state TRXOFF.

       Table 6-92. Receiver Configuration Steps

        No          Action                                                                                               Register
        0           Activate the MR-OFDM Physical Layer                                                                  PC.PT
        1           Configure MR-OFDM bandwidth option                                                                   OFDMC.OPT
        2           Configure PIB attribute phyOFDMInterleaving                                                          OFDMC.POI
        3           Select ‘low frequency offset’ option if applicable                                                   OFDMC.LFO
        4           Specify I/Q data interface rate of the Receiver Digital Frontend                                     RXDFE.SR
                    (dependent on OFDMC.OPT)
        5           Specify cut-off frequency of the Receiver Digital Frontend filter                                    RXDFE.RCUT
                    (dependent on OFDMC.OPT and OFDMC.LFO)
        6           Specify bandwidth and IF frequency of the Receiver Analog Frontend filter                            RXBWC.BW and
                    (dependent on OFDMC.OPT and OFDMC.LFO)                                                               RXBWC.IFS
        7           Specify AGC measurement period                                                                       AGCC.AVGS
                    (dependent on OFDMC.OPT)
        8           Specify AGC speed                                                                                    AGCC.AGCI
                    (dependent on OFDMC.OPT)
        9           Set AGC target level to 3 (default)                                                                  AGCS.TGT
        10          Adjust preamble detector threshold                                                                   OFDMSW.PDT


       The MR-OFDM bandwidth option is the central parameter that determines the sampling rate of the I/Q data interface
       and particular receive filter and AGC settings. Recommended settings are listed in Table 6-93.
       The 2.4GHz configuration has slightly opened frontend filters adapted to the higher expected absolute frequency offset.
       In case that a TCXO or similar clock source is used, the expected frequency offset reduces. This allows narrowing the
       filter settings equivalent to the sub-1GHz configuration for better ACI suppression. An exception is recommended for
       option 1 where the higher phase noise of the 2.4GHz radio requires the SSBF bandwidth not to be reduced.



                                                                                             Atmel AT86RF215 - DATASHEET                      114
                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 115 -->

       Note, that a TXCO based system with expected low frequency offset should be indicated to the 2.4 GHz PHY MR-
       OFDM receiver by setting OFDMC.LFO to 1. Then the MR-OFDM preamble detector searches for the STF (short
       training field) pattern in a reduced frequency span which makes it more robust against misdetection.

       Table 6-93. Recommended PHY Receiver and Digital Frontend Configuration

        Register               Option 1                Option 2                Option 3                        Option 4
        TXDFE.SR               3                       3                       6                               6
                                                sub-core 0 + sub-1GHz Radio Frontend
        RXDFE.RCUT             4                       2                       2                               1
        RXBWC.BW               9                       7                       4                               2
        RXBWC.IFS              1                       1                       0                               1
                                          sub-core 1 + 2.4GHz Radio Frontend, OFDMC.LFO=0
        RXDFE.RCUT             4                       2                       3                               1
        RXBWC.BW               10                      7                       5                               3
        RXBWC.IFS              1                       1                       1                               0
                                          sub-core 1 +2.4GHz Radio Frontend, OFDMC.LFO=1
        RXDFE.RCUT             4                       2                       2                               1
        RXBWC.BW               9                       7                       4                               2
        RXBWC.IFS              1                       1                       0                               1


        AGCC.AVGS              0                       0                       0                               0
        AGCC.AGCI              0                       0                       0                               0
        OFDMSW.PDT             5                       5                       4                               3


       To achieve good results for receiver energy detection, the averaging duration composed of sub-registers EDD.DTBand
       EDD.DF should be configured according to the MR-OFDM PHY symbol time.
       IEEE Std 802.15.4™-2006 [1] defines 8 symbols periods averaging time for ED. For MR-OFDM this translates to
       8*120us = 960us, configured by EDD.DTB=2 and EDD.DF=30.

6.11.3.2 Receiver Operation
       When the MR-OFDM receiver is activated, it searches for STF preamble patterns. If a preamble is found the IRQ
       IRQM.AGCH is issued and the AGC is put on hold (AGCC.FRZS = 1). Synchronization and channel acquisition are
       executed. The PHY header is demodulated and decoded using the MCS as defined in [3] for the PHR field.
       If the CRC-8 check indicates a valid PHY header and the frame length field is greater than zero, the frame start IRQ
       IRQM.RXFS is issued. At this event the MR-OFDM PHR status registers OFDMPHRRX.MCS, OFDMC.SSRX including
       the reserved bits OFDMPHRRX.RB5, OFDMPHRRX.RB17, OFDMPHRRX.RB18, and OFDMPHRRX.RB21 are
       updated. The PHR frame length field is mapped to the registers BBCn_RXFLH and BBCn_RXFLL, respectively. Further
       information on the receive procedure can be found in section "Example Receive Procedure Using Basic Mode" on page
       173.
       On frame start (IRQ IRQM.RXFS), the measured average signal power of the currently received frame is available in
       sub-register EDV.EDV, see section 6.2.4 on page 56 for details.


       Spurious Compensation


                                                                                   Atmel AT86RF215 - DATASHEET                     115
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 116 -->

       In case of performance degradation due to clock harmonics on receive channels with center frequency being multiple of
       26MHz or 32MHz, the MR-OFDM Spurious Compensation feature can be enabled by sub-register OFDMPHRRX.SPC.
       In that case the AGC target level (AGCS.TGT) should be set to 0.
       It is not recommended activating Spurious Compensation for MR-OFDM Option 4 because of its small bandwidth,
       especially if the MCS is expected to be greater three.


       Receiver Override
       The Receiver Override feature, activated by sub-register OFDMSW.RXO set to 1, enables the MR-OFDM PHY to
       restart a preamble detection at any time during reception if the received signal power has increased significantly. This
       reduces the influence of frame misdetections and hidden node effects.

6.11.4 Register Description
6.11.4.1 BBCn_OFDMPHRTX – MR-OFDM Transmitter PHY Header Configuration
       The register is used to compose the MR-OFDM PHY header (PHR) for transmission.
        Bit              7             6            5           4          3           2              1             0
                        RB21         RB18          RB17        RB5          –                       MCS                     BBCn_OFDMPHRTX
        Read/Write      RW             RW          RW          RW          R          RW            RW            RW
        Initial Value    0             0            0           0          0           0              0             0

        Bit 7 – OFDMPHRTX.RB21: Reserved PHR Bit 21
       The sub-register defines the PHR bit. The content is transmitted but serves no function.

        Bit 6 – OFDMPHRTX.RB18: Reserved PHR Bit 18
       The sub-register defines the PHR bit. The content is transmitted but serves no function.

        Bit 5 – OFDMPHRTX.RB17: Reserved PHR Bit 17
       The sub-register defines the PHR bit. The content is transmitted but serves no function.

        Bit 4 – OFDMPHRTX.RB5: Reserved PHR Bit 5
       The sub-register defines the PHR bit. The content is transmitted, but serves no function.

        Bit 2:0 – OFDMPHRTX.MCS: Modulation and Coding Scheme
       The sub-register sets the PSDU modulation and coding scheme, and fills the lower 3 bits of the PHR Rate field. The
       upper bits are filled with zero respectively.

       Table 6-94. MCS

        Sub-register           Value        Description
        MCS                    0x0          BPSK, coding rate 1/2, 4 x frequency repetition
                               0x1          BPSK, coding rate 1/2, 2 x frequency repetition
                               0x2          QPSK, coding rate 1/2, 2 x frequency repetition
                               0x3          QPSK, coding rate 1/2
                               0x4          QPSK, coding rate 3/4
                               0x5          16-QAM, coding rate 1/2
                               0x6          16-QAM, coding rate 3/4

6.11.4.2 BBCn_OFDMPHRRX – MR-OFDM Receiver PHY Header Status
       PHY header (PHR) status information is updated at interrupt Receiver Frame Start (RXFS).



                                                                                           Atmel AT86RF215 - DATASHEET                       116
                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| MCS | 0x0 | BPSK, coding rate 1/2, 4 x frequency repetition |
|  | 0x1 | BPSK, coding rate 1/2, 2 x frequency repetition |
|  | 0x2 | QPSK, coding rate 1/2, 2 x frequency repetition |
|  | 0x3 | QPSK, coding rate 1/2 |
|  | 0x4 | QPSK, coding rate 3/4 |
|  | 0x5 | 16-QAM, coding rate 1/2 |
|  | 0x6 | 16-QAM, coding rate 3/4 |


<!-- page 117 -->

       Bit              7             6          5              4     3         2            1             0
                                                                                                                         BBCn_
                       RB21          RB18       RB17           RB5   SPC                   MCS
                                                                                                                       OFDMPHRRX
       Read/Write       R             R          R             R     RW        R             R            R
       Initial Value    0             0          0              0     0         0            0             0

       Bit 7 – OFDMPHRRX.RB21: Reserved PHR Bit 21
      This sub-register reflects the content of the reserved PHR bit 21 of the last received MR-OFDM frame.

       Bit 6 – OFDMPHRRX.RB18: Reserved PHR Bit 18
      This sub-register reflects the content of the reserved PHR bit 18 of the last received MR-OFDM frame.

       Bit 5 – OFDMPHRRX.RB17: Reserved PHR Bit 17
      This sub-register reflects the content of the reserved PHR bit 17 of the last received MR-OFDM frame.

       Bit 4 – OFDMPHRRX.RB5: Reserved PHR Bit 5
      This sub-register reflects the content of the reserved PHR bit 5 of the last received MR-OFDM frame.

       Bit 3 – OFDMPHRRX.SPC: RX Spurious Compensation
      If this sub-register is set to 1, the spurious compensation (SPC) is activated. This is recommended if the receive
      channel is a multiple of 26MHz or 32MHz. Otherwise, it is recommended to set this sub-register to 0.

       Bit 2:0 – OFDMPHRRX.MCS: Modulation and Coding Scheme
      The sub-register reflects the lower 3 bits of the PHR rate field and indicates the PSDU modulation and coding scheme
      of the last received MR-OFDM frame. See OFDMPHRTX.MCS for value-to-coding mapping.

6.11.4.3 BBCn_OFDMC – MR-OFDM PHY Configuration
       Bit              7             6          5              4     3         2            1             0
                              SSRX                      SSTX         LFO      POI                 OPT                 BBCn_OFDMC
       Read/Write       R             R         RW             RW    RW       RW           RW            RW
       Initial Value    0             0          0              0     0         0            0             0

       Bit 7:6 – OFDMC.SSRX: Receiver Scrambler Seed Status
      SSRX reflects the PHR scrambler field and sets the initial seed of the de-scrambler PN9 sequence. PHY header (PHR)
      status information is updated at interrupt Receiver Frame Start (RXFS).

      Table 6-95. SSRX

       Sub-register           Value       Description
       SSRX                   0x0         0b000010111
                              0x1         0b101110111
                              0x2         0b000011100
                              0x3         0b101111100

       Bit 5:4 – OFDMC.SSTX: Transmitter Scrambler Seed Configuration
      SSTX sets the initial seed of the scrambler PN9 sequence and fills the PHR scrambler field (sec. 18.2.3.11, IEEE Std.
      802.15.4g-2012).




                                                                                    Atmel AT86RF215 - DATASHEET                     117
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SSRX | 0x0 | 0b000010111 |
|  | 0x1 | 0b101110111 |
|  | 0x2 | 0b000011100 |
|  | 0x3 | 0b101111100 |


<!-- page 118 -->

      Table 6-96. SSTX

       Sub-register         Value        Description
       SSTX                  0x0         0b000010111
                             0x1         0b101110111
                             0x2         0b000011100
                             0x3         0b101111100

       Bit 3 – OFDMC.LFO: Reception with Low Frequency Offset
      The sub-register is configured depending on the absolute frequency offset of the received OFDM signal.

      Table 6-97. LFO

       Sub-register         Value        Description
       LFO                   0x0         If the frequency offset has higher deviation than 57.3kHz, this sub-register should be set to
                                         0.
                             0x1         If it is guaranteed that the absolute frequency offset of the received OFDM signal is less than
                                         57.3kHz (i.e. usage of a TCXO), this sub-register should be set to 1. In conjunction with an
                                         adapted RF frontend configuration, the MR-OFDM receiver benefits from an improved ACI
                                         suppression.

       Bit 2 – OFDMC.POI: PIB Attribute phyOFDMInterleaving
      If this sub-register is 0, the MR-OFDM interleaver has a depth of one symbol. Otherwise, if this sub-register is 1, the
      MR-OFDM interleaver has a depth equal to the frequency domain spreading factor symbols. This sub-register reflects
      the PIB attribute phyOFDMInterleaving (see IEEE Std 802.15.4g-2012).

       Bit 1:0 – OFDMC.OPT: MR-OFDM Bandwidth Option
      MR-OFDM options 1 to 4 are configured by values 0 to 3 respectively.

      Table 6-98. OPT

       Sub-register         Value        Description
       OPT                   0x0         Option 1
                             0x1         Option 2
                             0x2         Option 3
                             0x3         Option 4

6.11.4.4 BBCn_OFDMSW – OFDM Switches
      This register controls test functionality of the MR-OFDM PHY.
       Bit              7            6              5         4          3           2            1             0
                                    PDT                     RXO           –          –            –             –         BBCn_OFDMSW
       Read/Write      RW           RW           RW         RW          RW          RW          RW            RW
       Initial Value    0            1              1         1          0           0            0             0

       Bit 7:5 – OFDMSW.PDT: Preamble Detection Threshold
      Lower values increase the preamble detector sensitivity.

       Bit 4 – OFDMSW.RXO: Receiver Override
      If Receiver Override is enabled during frame reception, the MR-OFDM receiver restarts synchronization after a rapidly
      increased signal power per OFDM symbol of more than 12dB.




                                                                                         Atmel AT86RF215 - DATASHEET                     118
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SSTX | 0x0 | 0b000010111 |
|  | 0x1 | 0b101110111 |
|  | 0x2 | 0b000011100 |
|  | 0x3 | 0b101111100 |

| Sub-register | Value | Description |
| --- | --- | --- |
| LFO | 0x0 | If the frequency offset has higher deviation than 57.3kHz, this sub-register should be set to |
|  |  | 0. |
|  | 0x1 | If it is guaranteed that the absolute frequency offset of the received OFDM signal is less than |
|  |  | 57.3kHz (i.e. usage of a TCXO), this sub-register should be set to 1. In conjunction with an |
|  |  | adapted RF frontend configuration, the MR-OFDM receiver benefits from an improved ACI |
|  |  | suppression. |

| Sub-register | Value | Description |
| --- | --- | --- |
| OPT | 0x0 | Option 1 |
|  | 0x1 | Option 2 |
|  | 0x2 | Option 3 |
|  | 0x3 | Option 4 |


<!-- page 119 -->

Table 6-99. RXO

Sub-register      Value   Description
RXO               0x0     Receiver override disabled
                  0x1     Receiver override enabled




                                                       Atmel AT86RF215 - DATASHEET                     119
                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| RXO | 0x0 | Receiver override disabled |
|  | 0x1 | Receiver override enabled |


<!-- page 120 -->

6.12   O-QPSK PHY

6.12.1 Overview
       The baseband sub-core O-QPSK of the AT86RF215 provides functionality with regard to the MR-O-QPSK PHY
       according to IEEE Std 802.15.4g™-2012 [3] and the O-QPSK PHY of ETSI TS 102 887-1, see [5]. In this document,
       both PHY types are generalized to MR-O-QPSK, due to their similarity and relation.
       The supported modes for MR-O-QPSK are shown in Table 6-100. Additional proprietary modes neither specified in [3]
       nor in [5] are available, see Table 6-100.

       Table 6-100. MR-O-QPSK Modes

       Chip Rate      Rate Mode      PSDU Data Rate       Description
       [kchip/s]                     [kb/s]
       100            0              6.25                 O-QPSK-A-PHY-ID-0 [3],
                                                          O-QPSK-PHY-OPTION-1 [5]
                      1              12.5                 O-QPSK-A-PHY-ID-1 [3]
                      2              25                   O-QPSK-A-PHY-ID-2 [3]
                      3              50                   O-QPSK-A-PHY-ID-3 [3]
       200            0              12.5                 O-QPSK-PHY-OPTION-2 [5]
                      1              25                   Proprietary (as O-QPSK-A-PHY-ID-1; chip rate is 200kchip/s)
                      2              50                   Proprietary (as O-QPSK-A-PHY-ID-2; chip rate is 200kchip/s)
                      3              100                  Proprietary (as O-QPSK-A-PHY-ID-3; chip rate is 200kchip/s)
       1000           0              31.25                O-QPSK-B-PHY-ID-0 [3]
                      1              125                  O-QPSK-B-PHY-ID-1 [3]
                      2              250                  O-QPSK-B-PHY-ID-2 [3]
                      3              500                  O-QPSK-B-PHY-ID-3 [3]
       2000           0              31.25                O-QPSK-C-PHY-ID-0 [3]
                      1              125                  O-QPSK-C-PHY-ID-1 [3]
                      2              250                  O-QPSK-C-PHY-ID-2 [3]
                      3              500                  O-QPSK-C-PHY-ID-3 [3]
                      4              1000                 Proprietary (as O-QPSK-C-PHY-ID-3; spreading bypassed)


       In addition, support for the O-QPSK PHY of the 780MHz, 915MHz, and 2450MHz frequency band with regard to clause
       10 of IEEE Std 802.15.4™-2011 [2] is provided, referred to as legacy O-QPSK. Some legacy O-QPSK high data rate
       modes based on this PHY are supported as well, see Table 6-101.


       With respect to the O-QPSK PHY specification of ETSI TS 102 887-1 [5], the AT86RF215 supports PPDU Type 2 (see
       Figure 6-25) in addition to PPDU Type 1 (see Figure 6-24). PPDU Type 2 can be applied regardless of the chip rate.




                                                                                Atmel AT86RF215 - DATASHEET                      120
                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 121 -->

       Figure 6-24. MR-O-QPSK PPDU Type 1
                                                                               Octets
                                                                   3                                     Variable
        Preamble               SFD-1                               As defined in in [3] 8.3.1.3          PSDU
                               As defined in [3] clause 18.3.1.2
                SHR                                                PHR                                   PHY payload



       Figure 6-25. MR-O-QPSK PPDU Type 2
                                                                                                  Octets
                                                                   7
        Preamble               SFD-2                               PSDU
                               As defined in [5] clause 6.1.2
               SHR                                                 PHY payload


                                                                                                  Octets
                                                                   18
        Preamble               SFD-3                               PSDU
                               As defined in [5] clause 6.1.2
               SHR                                                 PHY payload


       For PPDU Type 2, rate modes other than 0 are not supported since there is no PHR contained signaling the rate mode.
       Table 6-101 summarizes the supported modes for legacy O-QPSK according to [2]. There is additional support of some
       of the legacy proprietary high data rate modes compatible with the AT86RF212B and the AT86RF23X family.

       Table 6-101. Legacy O-QPSK Modes

        Chip Rate       PSDU Data Rate         Description
        [kchip/s]       [kb/s]
        1000            250                    O-QPSK PHY of the 780MHz and 915MHz frequency band [2]
        1000            500                    Proprietary high data rate mode compatible with AT86RF212B
        2000            250                    O-QPSK PHY of the 2450MHz frequency band [2]
        2000            1000                   Proprietary high data rate mode compatible with AT86RF23X


       The AT86RF215 supports simultaneous operation of MR-O-QPSK and legacy O-QPSK according to sub-clause 18.3.3
       of [3]. This is described in more detail in section "Receive Operation and Configuration" on page 123.
       In order to configure the baseband sub-core of the AT86RF215 with O-QPSK operation mode (MR-O-QPSK or legacy
       O-QPSK), sub-register PC.PT must be set to 3, see "Baseband Core" on page 81.

6.12.2 Transmit Operation and Configuration
6.12.2.1 General Transmit Configuration
       The desired chip rate can be selected with sub-register OQPSKC0.FCHIP. The desired impulse response of the pulse
       shaping filter can be selected with sub-register OQPSKC0.MOD.
       For MR-O-QPSK, the parameters for spreading and coding are implicitly defined by the chip frequency
       (OQPSKC0.FCHIP), see Table 164 and Table 165 of [3] and Table 9 of [5].


                                                                                        Atmel AT86RF215 - DATASHEET                     121
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

|  |  | Octets |  |
| --- | --- | --- | --- |
|  |  | 3 | Variable |
| Preamble | SFD-1 As defined in [3] clause 18.3.1.2 | As defined in in [3] 8.3.1.3 | PSDU |
| SHR |  | PHR | PHY payload |

|  |  | Octets |
| --- | --- | --- |
|  |  | 7 |
| Preamble | SFD-2 As defined in [5] clause 6.1.2 | PSDU |
| SHR |  | PHY payload |

|  |  | Octets |
| --- | --- | --- |
|  |  | 18 |
| Preamble | SFD-3 As defined in [5] clause 6.1.2 | PSDU |
| SHR |  | PHY payload |


<!-- page 122 -->

Prior to transmission of an MR-O-QPSK PPDU (regardless of the PPDU Type), sub-register OQPSKPHRTX.LEG must
be set to 0.
Only partial user access to PHR sub-field entries exists, as indicated in Figure 6-26.

Figure 6-26. MR-O-QPSK TX-PHR
SM        RM1       RM0   R1   R0                     L10-L0                              H7-H0
0         OQPSKPHRTX.MOD       OQPSKPHRTX.RB0         BBCn_TXFLH,BBCn_TXFLL               HCS, automatically computed



The reserved bit R1 is used in order to signal proprietary rate modes, see [3]. Table 6-102 provides details of the
mapping to the sub-field (RM1, RM0, R1) as a function of the sub-register entries OQPSKC0.FCHIP and
OQPSKPHRTX.MOD. Undefined rate modes are set to rate mode 0, assuring that the AT86RF215 does not assemble
a void PPDU.

Table 6-102. MR-O-QPSK Rate Mode Mapping

    OQPSKC0.FCHIP                         OQPSKPHRTX.MOD                             (RM1,RM0,R1)
    0x0, 0x1, 0x2                         0x0                                        (0,0,0)
                                          0x1                                        (0,1,0)
                                          0x2                                        (1,0,0)
                                          0x3                                        (1,1,0)
                                          Otherwise                                  (0,0,0)
    0x3                                   0x0                                        (0,0,0)
                                          0x1                                        (0,1,0)
                                          0x2                                        (1,0,0)
                                          0x3                                        (1,1,0)
                                          0x4                                        (0,1,1)
                                          Otherwise                                  (0,0,0)


Configuration of the PPDU Type is obtained by sub-register OQPSKPHRTX.PPDUT. If set to 1 (PPDU Type 2), the
frame length entry (obtained by registers BBCn_TXFLL and BBCn_TXFLH must be either 7 or 18) selects the
corresponding SFD and PSDU interleaver, see [5]. For frame lengths other than 7 or 18, the transceiver assembles
PPDU Type 1, even if OQPSKPHRTX.PPDUT is set to 1.
For legacy O-QPSK, the parameters for spreading are implicitly defined by the chip frequency (OQPSKC0.FCHIP), see
Table 73 and Table 74 of [2]. In contrast to the multi-rate MR-O-QPSK PHY, high data rate modes must be pre-
configured with sub-register OQPSKC3.HRLEG for both transmit and receive.
Prior to transmission of a legacy PPDU, sub-register OQPSKPHRTX.LEG must be set to 1. The configuration of the
PHR is shown in Figure 6-27.

Figure 6-27. Legacy O-QPSK TX-PHR

L0-L7                     R
BBCn_TXFLL[6:0]           OQPSKPHRTX.RB0




                                                                             Atmel AT86RF215 - DATASHEET                      122
                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| SM | RM1 | RM0 | R1 | R0 | L10-L0 | H7-H0 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | OQPSKPHRTX.MOD |  |  | OQPSKPHRTX.RB0 | BBCn_TXFLH,BBCn_TXFLL | HCS, automatically computed |

| L -L 0 7 | R |
| --- | --- |
| BBCn_TXFLL[6:0] | OQPSKPHRTX.RB0 |


<!-- page 123 -->

       Since the AT86RF215 O-QPSK baseband sub-core accesses the TX I/Q data interface, the transmitter frontend (see
       section "Transmitter Frontend" on page 43) should be configured with specific settings as a function of the chip rate.
       This is shown in Table 6-103.

       Table 6-103. O-QPSK Transmitter Frontend Configuration

                                                                     Chip Rate [kchip/s]
              Register
                                100                      200                     1000                           2000

        TXCUTC.PARAMP           0x3                      0x2                     0x0                            0x0
        TXCUTC.LPFCUT           0x7                      0x7                     0xB                            0xB
        TXDFE.SR                0xA                      0x5                     0x1                            0x1
        TXDFE.RCUT              0x3                      0x3                     0x3                            0x4


       A transmission is initiated with register CMD.CMD set to TX, see "State Machine" on page 33. Assembly of a complete
       PPDU is performed autonomously, including all signal processing steps, such as FEC, interleaving, spreading and
       modulation according to [3], [5] and [2], respectively.
       It is possible to initiate a transmission before any of the PHY payload data (PSDU) is loaded to the transmit frame buffer
       since the baseband sub-core autonomously starts with transmission of the SHR, see for instance Figure 6-24. However,
       the first payload octet is requested from the baseband sub-core just after the duration of the SHR relative to the transmit
       request. The PSDU belonging to the next PPDU must be available by that time. The SHR time depending on the chip
       rate is defined in [2] , [3] and [5]. For further information about frame buffer see section "Transmit Frame Buffer Under-
       run Detection" on page 132.

6.12.2.2 Direct Modulation RF215 v.3 (RF_VN = 0x03)
       AT86RF215 v.3 provides the additional feature to set the transmitter to direct modulation. The direct modulation shall be
       used for MR-O-QPSK chip rate 100kchip/s and 200kchip/s (OQPSKC0.FCHIP=0;1), it is not applicable for higher data
       rates. It improves the modulation quality especially at high output power (>8dBm).
       The direct modulation is enabled by:
            Sub-register TXDFE.DM = 1
            Sub-register OQPSKC0.DM = 1

6.12.3 Receive Operation and Configuration
       For receive, the AT86RF215 must be in state RX, see section "State Machine" on page 33.
       As shown in Figure 6-28, the O-QPSK baseband sub-core of the AT86RF215 contains two specific receiver units, RX_0
       for the receiving of MR-O-QPSK frames and RX_1 for the receiving of legacy O-QPSK frames. Both units share the
       same I/Q data interface and, consequently, the same receiver frontend. The transceiver can simultaneously listen for
       both PHY types at the same channel. This feature is restricted to chip rates of 1000kchip/s and 2000kchip/s
       (OQPSKC0.FCHIP = 2 or OQPSKC0.FCHIP = 3), respectively. If one receiver unit detects a frame start, the
       complementary receiver unit is disabled. Single or dual receive is selected with sub-register OQPSKC2.RXM.




                                                                                    Atmel AT86RF215 - DATASHEET                       123
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 124 -->

Figure 6-28. RX for O-QPSK


                                                                          en_0
                                                                   status_0
                                                     RX_0          oct_0
                                                  (MR-O-QPSK)      rxfs_0                          status
                                                                   agc_0{h,r}                      oct
                                                                                                   rxfs
                                                                                    RX_CTRL
                                                                           en_1                    agc{h,r}
                  I_DATA[13:0]                                      status_1                       fcs_type
                                                     RX_1          oct_1
                                      @fs
                                                 (legacy O-QPSK)   rxfs_1
                  Q_DATA[13:0]                                     agc_1{h,r}


                                                  O-QPSK Receiver



During frame reception, each receiver performs preamble detection, SFD search and PHR evaluation. The sensitivity
level for preamble detection can be configured with sub-registers OQPSKC1.PDT0 and OQPSKC1.PDT1, respectively.
Lower values increase the receiver sensitivity for rate mode 0, whereas larger values improve robustness with regard to
the capture effect.
For MR-O-QPSK, the search space of SFD words can be configured with sub-register OQPSKC3.NSFD. If PPDU Type
2 is not used, it is recommended to set OQPSKC3.NSFD to 0, improving robustness of SHR detection.
For MR-O-QPSK, the HCS of the detected PHR information bits is automatically evaluated. Frames with invalid HCS as
well as frames with a detected length field entry equal to 0 are automatically discarded (no frame start event). For
legacy O-QPSK, frames with a detected length field entry equal to 0 are automatically discarded. In case of a valid
frame start event, the AT86RF215 captures several pieces of status information, as shown in Table 6-104. This
information remains unchanged until the next frame start event occurs.

Table 6-104. Receiver Status

Status                         Register                  Description
Frame length                   BBCn_RXFLL,               The detected PSDU length in octets.
                               BBCn_RXFLH
PHY type                       OQPSKPHRRX.LEG            Indicates, whether a legacy O-QPSK or MR-O-QPSK frame has
                                                         been received.
Rate mode                      OQPSKPHRRX.MOD            Indicates the detected rate mode (valid for MR-O-QPSK only).
Reserved bit                   OQPSKPHRTX.RB0            The value of the detected reserved bit R0 (MR-O-QPSK) or R
                                                         (legacy O-QPSK)
Received signal power          EDV.EDV                   An estimate of the received signal power in dBm of the frame
PPDU type                      OQPSKPHRRX.PPDUT          Indicates the PPDU type of the received frame (valid for MR-O-
                                                         QPSK only).




                                                                             Atmel AT86RF215 - DATASHEET                         124
                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 125 -->

Regardless of the PHY type (MR-O-QPSK or legacy O-QPSK), the detected PSDU content is passed to the receive
frame buffer octet by octet. The procedure of frame buffer handling and FCS evaluation is unified for all baseband sub-
cores, see section "Frame Buffer" on page 132. However, with regard to FCS evaluation and dual receive mode
(OQPSKC2.RXM = 2), the FCS type must be a-priori known, indicated by the signal fcs_type, see Figure 6-28. In case
a legacy frame has been received, the FCS type is set to the content of register OQPSKC2.FCSTLEG. If an MR-O-
QPSK frame has been received, the FCS type is obtained from register PC.FCST.
If using proprietary rate modes (OQPSKPHRTX.MOD > 3), conflicts may occur with respect to interoperation since the
reserved bit R1 must not be interpreted while evaluating the rate mode. (The standard text according to [3] is not specific
about the content of the reserved bits). Those issues can be avoided if sub-register OQPSKC2.ENPROP is set to 0. In
this case, reception of proprietary modes (OQPSKPHRTX.MOD > 3) is not supported. Note, that this restriction is not
required if an MR-O-QPSK compliant device other than the AT86RF215 is only supporting the mandatory rate mode 0.
Since the AT86RF215 O-QPSK baseband sub-core accesses the RX I/Q data interface, the receiver frontend (see
section "Receiver Frontend" on page 52) must be configured with specific register settings, as a function of the chip
rate. This is shown in Table 6-105. Recommended settings of the AGC are shown in Table 6-106.

Table 6-105. O-QPSK Receiver Frontend Configuration (Filter Settings)

                                                              Chip Rate [kchip/s]
        Register
                         100                      200                     1000                           2000
RXBWC.BW                 0x0                      0x2                     0x8                            0xB
RXBWC.IFS                0x0                      0x0                     0x0                            0x0
RXDFE.SR                 0xA                      0x5                     0x1                            0x1
RXDFE.RCUT               0x1                      0x1                     0x0                            0x2
EDD.DTB                  0x3                      0x3                     0x3                            0x3
EDD.DF                   0xA                      0x5                     0x4                            0x4

Table 6-106. O-QPSK Receiver Frontend Configuration (AGC Settings)

                                                              Chip Rate [kchip/s]
        Register
                         100                      200                     1000                           2000
AGCC.AGCI                0x0                      0x0                     0x0                            0x0
AGCC.AVGS                0x2                      0x2                     0x0                            0x0
AGCC.EN                  0x1                      0x1                     0x1                            0x1
AGCS.TGT                 0x3                      0x3                     0x3                            0x3


The AT86RF215 supports receiver override (RXO) in order to mitigate the capture effect. The receiver goes back to
preamble detection if both applies:
        a preamble has been detected and
        the receiver strength rapidly increases above 12dB (RX_0: MR-O-QPSK) or 9dB (RX_1: legacy O-QPSK).
RXO for MR-O-QPSK is enabled with sub-register OQPSK.RXO set to 1.
RXO for legacy O-QPSK is enabled with sub-register OQPSK.RXOLEG set to 1.
Typical values of the AWGN receiver sensitivity are shown in Table 10-19 on page 196.




                                                                             Atmel AT86RF215 - DATASHEET                       125
                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 126 -->

       In principle, it is possible to combine any of the O-QPSK modes with any of the center frequencies supported by the
       AT86RF215. This is relevant if the O-QPSK PHY is intended to be used with frequency bands other than the bands
       specified in Table 66 of [3]. However, some constraints must be taken into consideration with respect to the maximum
       crystal tolerance. In particular, let fc be the carrier frequency of the desired channel. The value

                                                                          f0
                                                              pmax         p0
                                                                          fc
       defines the value of the maximum crystal tolerance in ppm, where fc and p0 are given in Table 6-107.

       Table 6-107. Parameter for Maximum Crystal Tolerance

        PHY Type        Chip Rate   f0       p0
                        [kchip/s]   [GHz]    [ppm]
        MR-O-QPSK       100         1.0      20
                        200         1.0      20
                        1000        1.0      20
                        2000        2.5      20
        Legacy          1000        1.0      50
        O-Q-PSK         2000        2.5      50


       At center frequencies of multiples of 26MHz or 32MHz, the receive band might be subject to spurious emission. In case
       of a noticeable degradation due to spurious emission, it is recommended enabling spurious compensation by setting
       sub-register OQPSKC2.SPC to 1.
       For MR-O-QPSK, the AT86RF215 supports receive operation with reduced power consumption (RPC) during RX listen.
       This can be configured with sub-register OQPSKC2.RPC set to 1.
       The principle of power saving is similar to the one of MR-FSK (see "Reduced Power Consumption (RPC)" on page 99),
       with the exception that the OFF and ON time cannot be configured.
       RPC is not supported for legacy O-QPSK.
       The RPC mode should not be used during energy measurement, see section "Energy Measurement" on page 56.
       Energy measurements during RPC may lead to incorrect energy detection values EDV.EDV.

6.12.4 Register Description
6.12.4.1 BBCn_OQPSKC0 – O-QPSK Configuration Byte 0
       This register configures the O-QPSK PHY.
        Bit              7          6             5       4           3           2            1             0
                          –         –             –      DM         MOD           –                FCHIP               BBCn_OQPSKC0
        Read/Write       R          R             R      RW          RW           R          RW            RW
        Initial Value    0          0             0       0           0           0            0             0

        Bit 4 – OQPSKC0.DM: Direct Modulation
       If this sub-register and sub-register RFxx_TXDFE.DM are set to 1, the direct modulation for OQPSK is enabled. This
       sub-register is applicable if OQPSKC0.FCHIP is 0 or 1 and ignored otherwise.

        Bit 3 – OQPSKC0.MOD: Modulation
       This sub-register configures the impulse response of the shaping filter.




                                                                                      Atmel AT86RF215 - DATASHEET                     126
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 127 -->

      Table 6-108. MOD

       Sub-register      Name                            Value        Description
       MOD               BB_RC08                          0x0         RC-0.8 shaping (raised cosine, roll-off = 0.8)
                         BB_RRC08                         0x1         RRC-0.8 shaping (root raised cosine, roll-off = 0.8)

       Bit 1:0 – OQPSKC0.FCHIP: Chip Frequency
      This sub-register configures the O-QPSK chip frequency.

      Table 6-109. FCHIP

       Sub-register      Name                            Value        Description
       FCHIP             BB_FCHIP100                      0x0         100kchip/s
                         BB_FCHIP200                      0x1         200kchip/s
                         BB_FCHIP1000                     0x2         1000kchip/s
                         BB_FCHIP2000                     0x3         2000kchip/s

6.12.4.2 BBCn_OQPSKC1 – O-QPSK Configuration Byte 1
      This register configures the O-QPSK PHY.
       Bit               7           6             5            4           3           2            1             0
                       RXO      RXOLEG                      PDT1                                  PDT0                       BBCn_OQPSKC1
       Read/Write      RW            RW          RW          RW            RW          RW          RW            RW
       Initial Value     1           1             0            1           1           0            1             1

       Bit 7 – OQPSKC1.RXO: Receiver Override for MR-O-QPSK PHY
      This bit configures the receiver override mode for MR-O-QPSK. If this bit is set to 1, the receiver override function is
      enabled.

      Table 6-110. RXO

       Sub-register          Value        Description
       RXO                   0x0          Receiver override disabled
                             0x1          Receiver override enabled

       Bit 6 – OQPSKC1.RXOLEG: Receiver Override for legacy O-QPSK PHY
      This sub-register configures the receiver override mode for legacy O-QPSK. If this bit is set to 1, the receiver override
      function is enabled.

      Table 6-111. RXOLEG

       Sub-register          Value        Description
       RXOLEG                0x0          receiver override disabled
                             0x1          receiver override enabled

       Bit 5:3 – OQPSKC1.PDT1: Preamble Detection Threshold 1
      Lower values increase the preamble detector sensitivity for legacy O-QPSK.

       Bit 2:0 – OQPSKC1.PDT0: Preamble Detection Threshold 0
      Lower values increase the preamble detector sensitivity for MR-O-QPSK.

6.12.4.3 BBCn_OQPSKC2 – OQPSK Configuration Byte 2
      This register configures the O-QPSK PHY.



                                                                                            Atmel AT86RF215 - DATASHEET                     127
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| MOD | BB_RC08 | 0x0 | RC-0.8 shaping (raised cosine, roll-off = 0.8) |
|  | BB_RRC08 | 0x1 | RRC-0.8 shaping (root raised cosine, roll-off = 0.8) |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| FCHIP | BB_FCHIP100 | 0x0 | 100kchip/s |
|  | BB_FCHIP200 | 0x1 | 200kchip/s |
|  | BB_FCHIP1000 | 0x2 | 1000kchip/s |
|  | BB_FCHIP2000 | 0x3 | 2000kchip/s |

| Sub-register | Value | Description |
| --- | --- | --- |
| RXO | 0x0 | Receiver override disabled |
|  | 0x1 | Receiver override enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| RXOLEG | 0x0 | receiver override disabled |
|  | 0x1 | receiver override enabled |


<!-- page 128 -->

Bit                7           6            5          4           3          2            1             0
                   –           –          SPC        RPC       ENPROP     FCSTLEG               RXM                BBCn_OQPSKC2
Read/Write         R           R          RW          RW         RW          RW           RW           RW
Initial Value      0           0            0          0           1          1            0             0

 Bit 5 – OQPSKC2.SPC: RX Spurious Compensation
This bit should be set to 1 for receive channels being multiple of 26MHz or 32MHz. A Spurious compensation is
activated to improve O-QPSK sensitivity in this environment.

Table 6-112. SPC

Sub-register           Value       Description
SPC                     0x0        RX Spurious Compensation disabled
                        0x1        RX Spurious Compensation enabled

 Bit 4 – OQPSKC2.RPC: Reduce Power Consumption
If this sub-register is set to 1, the receiver operates in a reduced power consumption mode (RPC), provided the receiver
is listening for frames of the MR-O-QPSK PHY only (RXM is 0).

Table 6-113. RPC

Sub-register           Value       Description
RPC                     0x0        power saving is disabled
                        0x1        power saving is enabled

 Bit 3 – OQPSKC2.ENPROP: Enable Proprietary Modes
If this sub-register is set to 1, reception of proprietary rate modes > 3 is supported.

Table 6-114. ENPROP

Sub-register           Value       Description
ENPROP                  0x0        Reception of proprietary rate modes is not supported
                        0x1        Reception of proprietary rate modes is supported

 Bit 2 – OQPSKC2.FCSTLEG: FCS type for Legacy O-QPSK PHY
This sub-register configures the FCS type for legacy O-QPSK PHY reception.

Table 6-115. FCSTLEG

Sub-register           Value       Description
FCSTLEG                 0x0        FCS type for legacy O-QPSK is 32-bit (this mode is a proprietary setting)
                        0x1        FCS type legacy O-QPSK is 16-bit

 Bit 1:0 – OQPSKC2.RXM: Receive Mode
This sub-register configures the receive mode.




                                                                                  Atmel AT86RF215 - DATASHEET                     128
                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| SPC | 0x0 | RX Spurious Compensation disabled |
|  | 0x1 | RX Spurious Compensation enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| RPC | 0x0 | power saving is disabled |
|  | 0x1 | power saving is enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| ENPROP | 0x0 | Reception of proprietary rate modes is not supported |
|  | 0x1 | Reception of proprietary rate modes is supported |

| Sub-register | Value | Description |
| --- | --- | --- |
| FCSTLEG | 0x0 | FCS type for legacy O-QPSK is 32-bit (this mode is a proprietary setting) |
|  | 0x1 | FCS type legacy O-QPSK is 16-bit |


<!-- page 129 -->

      Table 6-116. RXM

       Sub-register          Value       Description
       RXM                   0x0         Listen for frames of MR-O-QPSK PHY only
                             0x1         Listen for frames of legacy O-QPSK PHY only (if applicable)
                             0x2         Listen for both, frames of MR-O-QPSK and legacy O-QPSK PHY (if applicable)
                             0x3         Disable detection for both PHYs

6.12.4.4 BBCn_OQPSKC3 – O-QPSK Configuration Byte 3
      This register configures the O-QPSK PHY.
       Bit               7           6           5           4          3           2             1             0
                         –           –        HRLEG          –              NSFD                  –             –         BBCn_OQPSKC3
       Read/Write        R           R          RW          R          RW          RW             R            R
       Initial Value     0           0           0           0          0           0             0             0

       Bit 5 – OQPSKC3.HRLEG: High Rate Legacy OQPSK
      If this bit is set to 1, the TRX enables a proprietary high data rate mode for legacy O-QPSK. This applies for both,
      transmit and receive.

      Table 6-117. HRLEG

       Sub-register          Value       Description
       HRLEG                 0x0         Legacy O-QPSK according to IEEE Std 802.15.4-2006
                             0x1         Proprietary legacy O-QPSK high data rate mode

       Bit 3:2 – OQPSKC3.NSFD: SFD Search Space for MR-O-QPSK
      This sub-register configures the search space of SFD words for MR-O-QPSK.

      Table 6-118. NSFD

       Sub-register          Value       Description
       NSFD                  0x0         Search for SFD_1 only
                             0x1         Search for SFD_1 and SFD_2
                             0x2         Search for SFD_1 and SFD_3
                             0x3         Search for SFD_1 and SFD_2 and SFD_3

6.12.4.5 BBCn_OQPSKPHRTX – O-QPSK PHR TX
      This register configures the O-QPSK PHR field for the next transmit frame.
       Bit               7           6           5           4          3           2             1             0
                                                                                                                             BBCn_
                         –           –         PPDUT       RB0                     MOD                        LEG
                                                                                                                           OQPSKPHRTX
       Read/Write        R           R          RW          RW         RW          RW           RW            RW
       Initial Value     0           0           0           0          0           0             0             0

       Bit 5 – OQPSKPHRTX.PPDUT: PPDU Type Selection for MR-O-QPSK
      PPDUT configures the PPDU Type for MR-O-QPSK.




                                                                                         Atmel AT86RF215 - DATASHEET                     129
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| RXM | 0x0 | Listen for frames of MR-O-QPSK PHY only |
|  | 0x1 | Listen for frames of legacy O-QPSK PHY only (if applicable) |
|  | 0x2 | Listen for both, frames of MR-O-QPSK and legacy O-QPSK PHY (if applicable) |
|  | 0x3 | Disable detection for both PHYs |

| Sub-register | Value | Description |
| --- | --- | --- |
| HRLEG | 0x0 | Legacy O-QPSK according to IEEE Std 802.15.4-2006 |
|  | 0x1 | Proprietary legacy O-QPSK high data rate mode |

| Sub-register | Value | Description |
| --- | --- | --- |
| NSFD | 0x0 | Search for SFD_1 only |
|  | 0x1 | Search for SFD_1 and SFD_2 |
|  | 0x2 | Search for SFD_1 and SFD_3 |
|  | 0x3 | Search for SFD_1 and SFD_2 and SFD_3 |


<!-- page 130 -->

      Table 6-119. PPDUT

      Sub-register           Value       Description
      PPDUT                  0x0         PPDU Type 1 - PPDU with SFD_1, PHR and PSDU of variable length.
                             0x1         PPDU Type 2 - PPDU with SFD_2 or SFD_3 and PSDU of fixed length. (SFD_2: PSDU
                                         length is 7 octets) (SFD_3: PSDU length is 18 octets)

       Bit 4 – OQPSKPHRTX.RB0: Reserved Bit 0
      This bit configures the content of the reserved bit RB0 of MR-O-QPSK or reserved bit for legacy O-QPSK.

       Bit 3:1 – OQPSKPHRTX.MOD: Rate Mode
      This sub-register configures the rate mode for MR-O-QPSK.

      Table 6-120. MOD

      Sub-register           Value       Description
      MOD                    0x0         Rate mode 0 (IEEE Std 802.15.4g-2012)
                             0x1         Rate mode 1 (IEEE Std 802.15.4g-2012)
                             0x2         Rate mode 2 (IEEE Std 802.15.4g-2012)
                             0x3         Rate mode 3 (IEEE Std 802.15.4g-2012)
                             0x4         Rate mode 4 (proprietary, setting reserved bit RB1 to 1), only supported for 2000kchip/s

       Bit 0 – OQPSKPHRTX.LEG: PHY Type
      This bit configures the PHY type.

      Table 6-121. LEG

      Sub-register           Value       Description
      LEG                    0x0         MR-O-QPSK
                             0x1         Legacy O-QPSK

6.12.4.6 BBCn_OQPSKPHRRX – O-QPSK PHR RX
      This register contains information of the PHR field of the last received O-QPSK frame.
      Bit                7           6            5          4           3          2            1             0
                                                                                                                            BBCn_
                         –           –         PPDUT        RB0                   MOD                        LEG
                                                                                                                          OQPSKPHRRX
      Read/Write         R           R           R           R          R           R            R            R
      Initial Value      0           0            0          0           0          0            0             0

       Bit 5 – OQPSKPHRRX.PPDUT: PPDU Type Indication for MR-O-QPSK
      This bit reflects the PPDU type for the last received MR-O-QPSK frame.

      Table 6-122. PPDUT

      Sub-register           Value       Description
      PPDUT                  0x0         Frame with PPDU type 1 received
                             0x1         Frame with PPDU type 2 received

       Bit 4 – OQPSKPHRRX.RB0: Reserved Bit 0
      This bit reflects the content of the reserved PHR bit RB0 of the last received MR-O-QPSK frame or reserved bit of the
      last received legacy O-QPSK frame.




                                                                                        Atmel AT86RF215 - DATASHEET                     130
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| PPDUT | 0x0 | PPDU Type 1 - PPDU with SFD_1, PHR and PSDU of variable length. |
|  | 0x1 | PPDU Type 2 - PPDU with SFD_2 or SFD_3 and PSDU of fixed length. (SFD_2: PSDU |
|  |  | length is 7 octets) (SFD_3: PSDU length is 18 octets) |

| Sub-register | Value | Description |
| --- | --- | --- |
| MOD | 0x0 | Rate mode 0 (IEEE Std 802.15.4g-2012) |
|  | 0x1 | Rate mode 1 (IEEE Std 802.15.4g-2012) |
|  | 0x2 | Rate mode 2 (IEEE Std 802.15.4g-2012) |
|  | 0x3 | Rate mode 3 (IEEE Std 802.15.4g-2012) |
|  | 0x4 | Rate mode 4 (proprietary, setting reserved bit RB1 to 1), only supported for 2000kchip/s |

| Sub-register | Value | Description |
| --- | --- | --- |
| LEG | 0x0 | MR-O-QPSK |
|  | 0x1 | Legacy O-QPSK |

| Sub-register | Value | Description |
| --- | --- | --- |
| PPDUT | 0x0 | Frame with PPDU type 1 received |
|  | 0x1 | Frame with PPDU type 2 received |


<!-- page 131 -->

        Bit 3:1 – OQPSKPHRRX.MOD: Rate Mode
       This sub-register reflects the rate mode of the last received MR-O-QPSK frame.

       Table 6-123. MOD

        Sub-register          Value        Description
        MOD                   0x0          Rate mode 0 (IEEE Std 802.15.4g-2012)
                              0x1          Rate mode 1 (IEEE Std 802.15.4g-2012)
                              0x2          Rate mode 2 (IEEE Std 802.15.4g-2012)
                              0x3          Rate mode 3 (IEEE Std 802.15.4g-2012)
                              0x4          Rate mode 4 (proprietary, reserved bit RB1 = 1), only supported for 2000kchip/s

        Bit 0 – OQPSKPHRRX.LEG: PHY Type
       This bit reflects the PHY type of the last received O-QPSK frame.

       Table 6-124. LEG

        Sub-register          Value        Description
        LEG                   0x0          MR-O-QPSK frame received
                              0x1          Legacy O-QPSK frame received



6.12.4.7 RFn_TXDFE – Transmitter TX Digital Frontend
       The register configures the transmitter digital frontend.
        Bit               7           6            5           4          3          2            1             0
                                    RCUT                      DM                          SR                                 RFn_TXDFE
        Read/Write      RW            RW          RW          RW         RW         RW          RW            RW
        Initial Value     0           0            0           0          0          0            0             1

        Bit 4 – TXDFE.DM: Direct Modulation
       If this sub-register is set to 1 the transmitter direct modulation is enabled. Direct modulation is available for FSK and
       OQPSK (OQPSKC0.FCHIP=0;1). Direct modulation must also be enabled at the BBCx registers (FSKDM.EN and
       OQPSKC0.DM).




                                                                                         Atmel AT86RF215 - DATASHEET                     131
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| MOD | 0x0 | Rate mode 0 (IEEE Std 802.15.4g-2012) |
|  | 0x1 | Rate mode 1 (IEEE Std 802.15.4g-2012) |
|  | 0x2 | Rate mode 2 (IEEE Std 802.15.4g-2012) |
|  | 0x3 | Rate mode 3 (IEEE Std 802.15.4g-2012) |
|  | 0x4 | Rate mode 4 (proprietary, reserved bit RB1 = 1), only supported for 2000kchip/s |

| Sub-register | Value | Description |
| --- | --- | --- |
| LEG | 0x0 | MR-O-QPSK frame received |
|  | 0x1 | Legacy O-QPSK frame received |


<!-- page 132 -->

6.13   Frame Buffer

6.13.1 Overview
       Each baseband core has access to two frame buffers: one buffer for TX and one for RX. Both frame buffers are
       accessible by SPI (see section "SPI Transceiver Control Interface") for read and write. The buffers are shared between
       the different baseband cores.
       During TX the baseband core reads payload data (PSDU) for transmission from the transmit frame buffer. The transmit
       frame buffer holds up to 2047 PSDU octets. The register BBCn_FBTXS addresses the first octet, while the register
       BBCn_FBTXE addresses the last octet of the transmit frame buffer. The content of the lowest frame buffer address (i.e.
       BBCn_FBTXS) is transmitted first.
       On receive, the baseband core stores up to 2047 PSDU octets in the receive frame buffer. Register BBCn_FBRXS
       addresses the first octet, while register BBCn_FBRXE addresses the last octet of the receive frame buffer. The first
       received PSDU octet is stored to the lowest frame buffer address (i.e. BBCn_FBRXS).

6.13.2 Receive
       During receive, the baseband core stores the received PSDU octets to the receive frame buffer. The first PSDU octet is
       stored after IRQ RXFS (receiver frame start) is issued. The number of received octets is updated with IRQ RXFS and
       can be read from the registers BBCn_RXFLH and BBCn_RXFLL. If IRQ RXFE (receiver frame end) occurs, the
       complete PSDU (incl. FCS) has been stored to the receive frame buffer.

6.13.3 Transmit
       Since the PHYs automatically generate the SHR and PHR from predefined settings, the frame buffer holds PHY
       payload (PSDU) only. The baseband cores start with the transmission of the PPDU after the frame preamble has been
       transmitted. During transmit, the first frame buffer read access occurs after the end of the preamble (part of the SHR)
       transmission. The length of the preamble depends of the selected PHY. Further frame buffer accesses, for consecutive
       PSDU octets, have an arbitrary timing. Once the IRQ TXFE is issued, all PSDU octets are completely read and
       transmitted. The PSDU data must be provided to the frame buffer latest right before it is required otherwise a TX under-
       run occurs (see "Transmit Frame Buffer Under-run Detection" below).
       The PSDU length of the transmitted frame is configured by the concatenation of the registers BBCn_TXFLL and
       BBCn_TXFLH. The length includes the FCS field.
       The AT86RF215 implements an automatic frame check sequence (FCS) generation (see "Frame Check Sequence" on
       page 138). It is enabled by the sub-register PC.TXAFCS and the sub-register PC.FCST configures the length of the
       FCS (16-bit / 32-bit). If the automatic FCS generation is enabled, the PSDU octets containing the FCS are generated by
       the AT86RF215 and it is not required to provide the FCS to the transmit frame buffer.

6.13.4 Transmit Frame Buffer Under-run Detection
       It is not required to provide the complete PSDU before transmit frame start. The baseband core reads the PHY payload,
       after the preamble transmission from the transmit frame buffer. Thus, the transmit frame buffer can be written after the
       transmit frame start while the preamble is transmitted.
       If the external MCU fails to provide the PSDU before it is required by the baseband core, a transmit frame buffer under-
       run event occurs. The AT86RF215 transmits (unwanted) previous octets. The sub-register PS.TXUR indicates missing
       TX data in the frame buffer. It is set and reset respectively to the equation:




                                                                                   Atmel AT86RF215 - DATASHEET                     132
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 133 -->

                                1                         if ADDRSPI  ADDRCORE
                               
                    PS .TXUR   0                         if SPI write access to BBCn _ TXFLL
                               PS .TXUR
                                                           else
                                                                                                            ,
where ADDRSPI is the last frame buffer write address (via SPI) and ADDRCORE is the last frame buffer read access
address (from baseband core).
Note, the PSDU, written to the transmit frame buffer, must contain the FCS field regardless of the sub-register
PC.TXAFCS. If the sub-register PC.TXAFCS is set to 1, the FCS data in the transmit frame buffer can have any value.
Once the sub-register PS.TXUR is set to 1, it remains 1. With an SPI write access to the register BBCn_TXFLL, the
sub-register PS.TXUR is reset to 0 and the value of ADDRSPI is set to “-1”.
If the sub-register PC.TXAFCS is set to 1 and a buffer under-run event has occurred, the FCS is calculated based on
the data currently stored in the frame buffer (corrupted PSDU). That means, that the frame is coherent, but the
containing data are wrong.
Figure 6-29 shows the flow chart of a frame transmit with transmit frame buffer under-run detection. This scenario is
applicable if the transmit frame start is not be delayed by the writing of the PSDU data. This comes with the risk of
transmit frame buffer under-run event.

Figure 6-29. Frame Transmit Flow using Transmit Under-run Indication

              write
    BBCn_TXFLH and BBCn_TXFLL



               initiation
          transmit frame start



                 write
   PSDU data to transmit frame buffer




              IRQ TXFE
              occurred?




                TXUR?




                                   transmit frame buffer
         transmit successfully
                                        under-run



Figure 6-30 shows a reliable frame transmit flow with no frame buffer under-run event since the frame payload is stored
to the transmit frame buffer before the transmit start is triggered.




                                                                            Atmel AT86RF215 - DATASHEET                      133
                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 134 -->

       Figure 6-30. Safe Frame Transmit Flow

                     write
           BBCn_TXFLH and BBCn_TXFLL



                        write
          PSDU data to transmit frame buffer



                      initiation
                 transmit frame start




                      IRQ TXFE          N
                      occurred?

                            Y



                 transmit successfully



       If the frame needs to be re-transmitted without any change of the payload data, neither the transmit frame buffer nor the
       transmit frame length (BBCn_TXFLH, BBCn_TXFLL) needs to be updated. In this scenario, the sub-register PS.TXUR
       remains unchanged.

6.13.5 Frame Buffer Level Monitor
       The frame buffer level (FBL) monitor is a level gauge that provides the actual number of octets read/stored from/to the
       frame buffer by the baseband core. The processing of the payload octets can be monitored with the FBL. It is used in
       transmit and receive procedures differently.
       During frame receive the FBL indicates the number of bytes stored from the baseband core to the receive frame buffer.
       The FBL value is reset with the starting the receive procedure (i.e. by writing the command RX to the register
       RFn_CMD).
       During frame transmit the FBL indicates the number of octets already read by the baseband core from the transmit
       frame buffer. The FBL is reset while the preamble transmit is in progress.
       The value of the frame buffer level is stored to the registers BBCn_FBLL and BBCn_FBLH. Both registers are
       concatenated to the 11-bit frame buffer level (FBL) value.

6.13.6 Frame Buffer Level Interrupt
       The frame buffer level interrupt (FBLI) is a baseband interrupt. For further information about baseband interrupts see
       section "Baseband Interrupts" on page 82.
       The IRQ FBLI is issued if the current number of received bytes is greater than the number stored to the FBLI value
       while writing to the register BBCn_FBLIH.
       During frame reception the interrupt FBLI is issued if a certain number of octets have been actually received (i.e. stored
       to the frame buffer). The number of received octets can be configured by the FBLI value. The registers BBCn_FBLIL
       and BBCn_FBLIH are concatenated to the 11-bit FBLI value.




                                                                                    Atmel AT86RF215 - DATASHEET                     134
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 135 -->

6.13.7 Register Description
6.13.7.1 BBCn_PS – PHY Status and Settings
       This register contains PHY status information.
        Bit               7          6           5          4            3         2             1             0
                          –          –           –           –           –         –             –          TXUR             BBCn_PS
        Read/Write       RW          R           R          R            R         R             R            R
        Initial Value     0          0           0          0            0         0             0             0

        Bit 0 – PS.TXUR: TX Underrun
       Bit TXUR indicates a TX frame buffer underrun. If the last frame buffer write address is lower than the current internal
       frame buffer read address during frame transmit, the sub-regitser is set to 1. It is reset with CMD=TX (Transmit Start).

6.13.7.2 BBCn_FBLL – Frame Buffer Level Low Byte
       This register contains the eight least significant bits of the frame buffer level (FBL) value. To get a consistent value, the
       register values FBLL and FBLH must read by a SPI block access.
        Bit               7          6           5          4            3         2             1             0
                                                                 FBLL                                                       BBCn_FBLL
        Read/Write        R          R           R          R            R         R             R            R
        Initial Value     0          0           0          0            0         0             0             0

6.13.7.3 BBCn_FBLH – Frame Buffer Level High Byte
       This register contains the three most significant bits of the frame buffer level (FBL).
        Bit               7          6           5          4            3         2             1             0
                          –          –           –           –           –                    FBLH                          BBCn_FBLH
        Read/Write        R          R           R          R            R         R             R            R
        Initial Value     0          0           0          0            0         0             0             0

6.13.7.4 BBCn_RXFLH – RX Frame Length High Byte
       This register contains the three most significant bits of the RX frame length. It is updated if a valid PHR is detected.
       Note, that an RX frame length of 0 prevents IRQ RXFS.
        Bit               7          6           5          4            3         2             1             0
                          –          –           –           –           –                   RXFLH                         BBCn_RXFLH
        Read/Write        R          R           R          R            R         R             R            R
        Initial Value     0          0           0          0            0         0             0             0

6.13.7.5 BBCn_RXFLL – RX Frame Length Low Byte
       This register contains the eight least significant bits of the RX frame length. It is updated if a valid PHR is detected.
       Note, that an RX frame length of 0 prevents IRQ RXFS.
        Bit               7          6           5          4            3         2             1             0
                                                                 RXFLL                                                     BBCn_RXFLL
        Read/Write        R          R           R          R            R         R             R            R
        Initial Value     0          0           0          0            0         0             0             0

6.13.7.6 BBCn_TXFLH – TX Frame Length High Byte
       This register contains the three most significant bits of the TX frame length.




                                                                                        Atmel AT86RF215 - DATASHEET                     135
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 136 -->

        Bit               7           6          5           4           3         2              1             0
                          –           –           –          –           –                    TXFLH                         BBCn_TXFLH
        Read/Write        R          R           R           R           R        RW            RW            RW
        Initial Value     0           0          0           0           0         0              0             0

6.13.7.7 BBCn_TXFLL – TX Frame Length Low Byte
       This register contains the eight least significant bits of the TX frame length.
        Bit               7           6          5           4           3         2              1             0
                                                                 TXFLL                                                      BBCn_TXFLL
        Read/Write       RW         RW          RW          RW           RW       RW            RW            RW
        Initial Value     0           0          0           0           0         0              0             0

6.13.7.8 BBCn_FBRXS – Frame Buffer RX Start
       This register contains the first octet of the receive frame buffer.
        Bit               7           6          5           4           3         2              1             0
                                                                 FBRXS                                                      BBCn_FBRXS
        Read/Write       RW         RW          RW          RW           RW       RW            RW            RW
        Initial Value     0           0          0           0           0         0              0             0

6.13.7.9 BBCn_FBRXE – Frame Buffer RX End
       This register contains the last octet of the receive frame buffer.
        Bit               7           6          5           4           3         2              1             0
                                                                 FBRXE                                                      BBCn_FBRXE
        Read/Write       RW         RW          RW          RW           RW       RW            RW            RW
        Initial Value     0           0          0           0           0         0              0             0

6.13.7.10 BBCn_FBTXS – Frame Buffer TX Start
       This register contains the first octet of the transmit frame buffer.
        Bit               7           6          5           4           3         2              1             0
                                                                 FBTXS                                                      BBCn_FBTXS
        Read/Write       RW         RW          RW          RW           RW       RW            RW            RW
        Initial Value     0           0          0           0           0         0              0             0

6.13.7.11 BBCn_FBTXE – Frame Buffer TX End
       This register contains the last octet of the transmit frame buffer.
        Bit               7           6          5           4           3         2              1             0
                                                                 FBTXE                                                      BBCn_FBTXE
        Read/Write       RW         RW          RW          RW           RW       RW            RW            RW
        Initial Value     0           0          0           0           0         0              0             0

6.13.7.12 BBCn_FBLIL – Frame Buffer Level Interrupt Value Low Byte
       This register contains the eight least significant bits of the frame buffer level interrupt (FBLI) value. A new FBLI value is
       valid if the register FBLIH is written.




                                                                                         Atmel AT86RF215 - DATASHEET                     136
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 137 -->

        Bit               7           6          5           4           3           2            1             0
                                                                 FBLIL                                                      BBCn_FBLIL
        Read/Write       RW          RW         RW          RW           RW        RW           RW            RW
        Initial Value     1           1          1           1           1           1            1             1

6.13.7.13 BBCn_FBLIH – Frame Buffer Level Interrupt Value High Byte
       This register contains the three most significant bits of the frame buffer level interrupt value. If this sub-register is
       written, the value in register FBLIL will be valid.
        Bit               7           6          5           4           3           2            1             0
                          –           –           –          –           –                     FBLIH                        BBCn_FBLIH
        Read/Write        R           R          R           R           R         RW           RW            RW
        Initial Value     0           0          0           0           0           1            1             1




                                                                                         Atmel AT86RF215 - DATASHEET                     137
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 138 -->

6.14   Frame Check Sequence

6.14.1 Overview
       The AT86RF215 supports an automatic handling of the frame check sequence (FCS) for TX and RX. Two different FCS
       types are defined in [3]: a 16-bit CRC and a 32-bit CRC. The FCS type used, is selected by sub-register PC.FCST.
       The embedded frame check sequence unit (FCS) is characterized by:
               Indication of bit errors, based on a cyclic redundancy check (CRC) of length 16 bit or 32 bit
               Use of International Telecommunication Union (ITU) CRC polynomial
               Automatic evaluation during reception
               Automatic generation during transmission.

6.14.2 Transmit
       If the AT86RF215 operates in state TX, the FCS can be automatically calculated and appended to the PHY payload
       (PSDU). If the sub-register PC.TXAFCS is set to 1, the last two octets (16-bit FCS) or four octets (32-bit FCS) of the
       transmitted PSDU are replaced by the internally calculated FCS. The Table 6-125 below shows the supported PSDU
       size depending on the different FCS length settings. If a PSDU length is shorter or equal than the FCS length
       transmitted, the automatic FCS generation is not supported.

       Table 6-125. Supported Transmit PSDU Length depending on FCS Type

       TX FCS Type                Automatic FCS insertion    Supported PSDU length
       32-bit; PC.FCST = 0        PC.TXAFCS = 1              5..2047
       16-bit; PC.FCST = 1        PC.TXAFCS = 1              3..2047
       32-bit or 16-bit           PC.TXAFCS = 0              1..2047


       If the sub-register PC.TXAFCS is set to 0, the FCS is read/transmitted from the transmit frame buffer (see section
       "Frame Buffer" on page 132).

6.14.3 Receive
       If the device operates in state RX, the FCS is automatically checked. The sub-register PC.FCSOK provides the result of
       this check. It is updated with IRQ RXFE. Table 6-126 below shows the FCS handling for specific PSDU length.

       Table 6-126. Supported Receive PSDU Length depending on FCS Type

       RX FCS Type         Receive PSDU length       Receiver FCS check
       32-bit              0                         Frame not handled (no IRQ RXFE)
                           1..3                      FCS not valid
                           4..2047                   FCS checked
       16-bit              0                         Frame not handled (no IRQ RXFE)
                           1                         FCS not valid
                           2..2047                   FCS checked


       Note:      If the baseband core receives a legacy O-QPSK (see section "O-QPSK PHY" on page 120) frame, the sub-
                  register PC.FCST is not used and the value set in the sub-register OQPSKC2.FCSTLEG is applied instead.



                                                                                     Atmel AT86RF215 - DATASHEET                      138
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 139 -->

6.14.4 Interrupt Receiver Frame End
       The interrupt receiver frame end (RXFE) occurs at frame end to indicate that the controller can further process the
       received frame.
       The FCS is intended for use at the MAC layer to detect corrupted frames at the first level of filtering (see section "First
       Level of Filtering" on page 141). The first level of filtering discards all received frames that do not have a valid FCS field.
       If the sub-register PC.FCSFE is set to 0, a frame passes the first level of filtering regardless of the validity of the FCS
       field.
       If a frame passes this filtering, an IRQ RXFE is issued otherwise an IRQ RXFE is omitted.
       Note:      This rule is only sufficient if the address filter is not enabled (see section "Frame Filter" on page 141). Table 6-
                  136 shows the dependencies if the address filter is enabled.

6.14.5 Register Description
6.14.5.1 BBCn_PC – PHY Control
       This register configures the baseband PHY.
        Bit                 7           6             5            4       3         2            1             0
                          CTX         FCSFE        FCSOK      TXAFCS     FCST      BBEN                 PT                    BBCn_PC
        Read/Write        RW            RW            R            RW     RW        RW          RW            RW
        Initial Value       0           1             0            1       0         1            0             0

        Bit 7 – PC.CTX: Continuous Transmit
       This sub-register enables the continuous transmit mode.

       Table 6-127. CTX

        Sub-register            Value        Description
        CTX                     0x0          Continuous transmission disabled
                                0x1          Continuous transmission enabled

        Bit 6 – PC.FCSFE: Frame Check Sequence Filter Enable
       This sub-register configures the filter function of the FCS check. If this sub-register is set to 1, an IRQ RXFE occurs only
       if the frame has a valid FCS. If this sub-register is set to 0, an IRQ RXFE occurs regardless of the FCS validity.

       Table 6-128. FCSFE

        Sub-register            Value        Description
        FCSFE                   0x0          FCS filter disabled
                                0x1          FCS filter enabled

        Bit 5 – PC.FCSOK: Frame Check Sequence OK
       This sub-register indicates whether the FCS of a detected frame is valid or not. This sub-register is automatically set to
       0 if a frame start is detected. FCSOK is updated once the frame is received completely.




                                                                                         Atmel AT86RF215 - DATASHEET                     139
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CTX | 0x0 | Continuous transmission disabled |
|  | 0x1 | Continuous transmission enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| FCSFE | 0x0 | FCS filter disabled |
|  | 0x1 | FCS filter enabled |


<!-- page 140 -->

Table 6-129. FCSOK

Sub-register          Value     Description
FCSOK                  0x0      FCS not valid
                       0x1      FCS valid

 Bit 4 – PC.TXAFCS: Transmitter Auto Frame Check Sequence
If the sub-register TXAFCS is set to 1 during transmission, the internal calculated FCS (type dependent of FCST) is
inserted into the last 2 or 4 PSDU octets, respectively. Note, this sub-register should be set to 1 only if the TX frame
length is greater than the length of the selected FCS type, otherwise sub-register TXAFCS should be set to 0.

Table 6-130. TXAFCS

Sub-register          Value     Description
TXAFCS                 0x0      FCS not calculated
                       0x1      FCS autonomously calculated

 Bit 3 – PC.FCST: Frame Check Sequence Type
The sub-register FCST configures the used Frame Check Sequence Type.

Table 6-131. FCST

Sub-register          Value     Description
FCST                   0x0      FCS type 32-bit
                       0x1      FCS type 16-bit

 Bit 2 – PC.BBEN: Baseband Enable
This sub-register enables the baseband.

Table 6-132. BBEN

Sub-register          Value     Description
BBEN                   0x0      Baseband is not enabled (switched off)
                       0x1      Baseband is enabled (switched on)

 Bit 1:0 – PC.PT: PHY Type
This sub-register sets the PHY type.

Table 6-133. PT

Sub-register        Name                        Value    Description
PT                  BB_PHYOFF                     0x0    OFF
                    BB_MRFSK                      0x1    MR-FSK
                    BB_MROFDM                     0x2    MR-OFDM
                    BB_MROQPSK                    0x3    MR-O-QPSK or legacy O-QPSK




                                                                              Atmel AT86RF215 - DATASHEET                     140
                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| FCSOK | 0x0 | FCS not valid |
|  | 0x1 | FCS valid |

| Sub-register | Value | Description |
| --- | --- | --- |
| TXAFCS | 0x0 | FCS not calculated |
|  | 0x1 | FCS autonomously calculated |

| Sub-register | Value | Description |
| --- | --- | --- |
| FCST | 0x0 | FCS type 32-bit |
|  | 0x1 | FCS type 16-bit |

| Sub-register | Value | Description |
| --- | --- | --- |
| BBEN | 0x0 | Baseband is not enabled (switched off) |
|  | 0x1 | Baseband is enabled (switched on) |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| PT | BB_PHYOFF | 0x0 | OFF |
|  | BB_MRFSK | 0x1 | MR-FSK |
|  | BB_MROFDM | 0x2 | MR-OFDM |
|  | BB_MROQPSK | 0x3 | MR-O-QPSK or legacy O-QPSK |


<!-- page 141 -->

6.15    IEEE MAC Support

6.15.1 Overview
        The AT86RF215 provides embedded IEEE MAC support reducing the MCU to transceiver interaction. The functionality
        is dedicated to support IEEE Std 802.15.4TM-2006 [1].
        The most common feature is the frame filter (see section "Frame Filter" below) which discards frames that are not
        directed to the device and thus prevents the controller to analyze the complete over-the-air traffic.
        With the described procedure "Clear Channel Assessment with Automatic Transmit (CCATX)" on page 148 a CCA
        measurement is performed and a frame is automatically transmitted if the CCA result is appropriate. The procedure
        "Transmit and Switch to Receive (TX2RX)" on page 148 switches to state RX once the frame transmission is completed
        automatically. The section "Automatic Acknowledgement (AACK)" on page 146 describes a procedure to automatically
        transmit an acknowledgement frame in response to a received frame.


        It is not allowed to modify the registers mentioned in Table 6-134 below while an IEEE MAC Support procedure is
        active.

        Table 6-134. Registers, modified by IEEE MAC Support procedures

         Register                 Used by MAC procedure
         BBCn_OQPSKPHRTX          AACK
         BBCn_OFDMPHRTX           AACK
         BBCn_FSKPHRTX            AACK
         RFn_CMD                  AACK, CCATX, TX2RX
         RFn_EDC                  CCATX
         RFn_AGCC                 CCATX
         BBCn_PC                  CCATX



6.15.2 Frame Filter
6.15.2.1 Overview
        Frame filtering is a procedure that evaluates whether or not a received frame matches predefined criteria, like address
        information or frame types. The filtering procedure as described in [1] clause 7.5.6.2. (“Reception and rejection”) is
        applied to the frame. If a frame passes all selected filter criteria, the interrupt receiver frame end (IRQS.RXFE) is
        generated. If the IRQ RXFE is not issued, the received frame did not pass at least one of the enabled filters.

6.15.2.2 First Level of Filtering
        The first level of filtering rejects all received frames that do not have a valid FCS field (see sub-register PC.FCSFE). In
        case PC.FCSFE is set to 0, a frame passes the first level of filtering regardless of the validity of the FCS field.

6.15.2.3 Second Level of Filtering
        If the AT86RF215 operates in promiscuous mode, each received frame passes this filter stage. The promiscuous mode
        is enabled by sub-register AFC0.PM. If the device does not operate in promiscuous mode, the address filtering is
        applied (if enabled).




                                                                                      Atmel AT86RF215 - DATASHEET                      141
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 142 -->

6.15.2.4 Address Filter
       The address filter consists of three filter blocks: global filter, 3rd level filter and extended filter. The 3rd level filter consists
       of four equal filter units to support multiple address filtering (see section "Multi Address Filtering (MAF)" on page 144). If
       at least one unit is enabled by AFC0.AFEN0, AFC0.AFEN1, AFC0.AFEN2 or AFC0.AFEN3, the address filter is
       enabled. The address filter rules are derived from the mentioned filter procedure (see section "Overview" on page 141)
       and extended to support two additional rules.
       Global Filter Rules
             Frame type matches settings in sub-register BBCn_AFFTM
              (register BBCn_AFFTM operates as a global frame type filter)
             Frame version matches settings in sub-register BBCn_AFFVM
              (register BBCn_AFFVM operates as a global frame version filter)
       Third Level Filter Rules
             If a destination PAN identifier is included in the frame, it should match macPANId [1] or shall be the broadcast
              PAN identifier.
             If a short destination address is included in the frame, it should match either macShortAddress [1] or the
              broadcast address. Otherwise, if an extended destination address is included in the frame, it shall match
              macExtendedAddress [1].
             If the frame type indicates that the frame is a beacon frame, the source PAN identifier shall match macPanId
              unless macPANId is equal to the broadcast PAN identifier in which case the beacon frame shall be accepted
              regardless of the source PAN identifier.
             If only source addressing fields are included in a data or MAC command frame, the frame shall be accepted
              only if the device is the PAN coordinator (MACPANC set) and the source PAN identifier matches MACPID.
             1st additional filter rule:
              The frame type does not indicate an ACK frame.
              2nd additional filter rule
              The frame contains any address.
       If an incoming frame passes all global rules and all third level filter rules, an address match interrupt (IRQS.RXAM)
       occurs.
       A frame which passes the global rules and one of the following extended rules, is considered as an extended frame and
       the extended match interrupt (IRQS.RXEM) is issued:
       Extended Filter Rules
             The frame type has a value of 4 to 7
             The frame version indicates a value of 2 or 3
             The source address type is set to 1
             The frame type is not 0 and the destination address type is set to 1.


       The different filter stages and its dependencies during frame parsing are shown in the flow chart in Figure 6-31.




                                                                                           Atmel AT86RF215 - DATASHEET                      142
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 143 -->

Figure 6-31. Flow Chart of Different Frame Filter Stages




                                                                          start frame parsing


                                                                              valid PHR         N
                                                                              detected ?

                                                                                  Y
                                                                      generation IRQ RXFS



                                                                                                N
                                                                            AFEN0..3=1 ?

                                                                                        Y
                                                                          check global rules


                                                                      N
                                                                            rules passed ?



       address filter
                                                                               Y

                                       check 3rd level filter rules                                 check extended filter rules


                                       N                                                                                   N
                                            rules passed ?                                               rules passed ?

                                                      Y                                                           Y

                                        generation IRQ RXAM                                          generation IRQ RXEM




                                                                             IRQ RXAM
2nd level of
                                                               N
                                                                              or RXEM
                                              N                               occurred?
  filtering
                                PM=1?
                                                                                    Y
                                   Y




                                                                      N
                                                                              FCSFE=1




       1st level of filtering
                                                                                    Y
                                                                             check FCS



                                                                                                N
                                                                            FCS correct ?

                                                                                    Y


                                                                      generation IRQ RXFE


                                                                      frame parsing finished




                                                                                                                      Atmel AT86RF215 - DATASHEET                      143
                                                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 144 -->

6.15.2.5 Multi Address Filtering (MAF)
       A device may be connected to different networks and may need to handle different addresses and network IDs. To
       support such scenarios, the address filter consists of four equal 3rd level filter units which work independently from each
       other. Each unit can be enabled and configured separately. If one unit detects an address match, the address match
       interrupt (IRQS.RXAM) is issued. The register BBCn_AFS indicates which unit has actually an address match detected.

       Figure 6-32. Address Filter with Multi Address Filtering (MAF)


                                                                MAF
                        Address Filter                                           BBCn_AFS.AM0..3

                                                        3rd Level Filter         IRQ RXAM


         frame data
                              Global Filter


                                                                                 IRQ RXEM
                                                        Extended Filter




       The 3rd level filter units are separately configurable by the following parameters (see Table 6-135 below):
             Enable bit
             macShortAddress
             macPanId
             PAN coordinator enable
             Map reserved frame types.
       The same macExtendedAddress is valid for all 3rd level filter units.

6.15.2.6 Configuration and Status
       The address filter rules require MAC relevant information. These MAC information are configured by several registers
       as shown in Table 6-135.

       Table 6-135. Address Filter Registers

        Sub-register       IEEE 802.15.4-2006      Size          Reset     Comment
        Name               Attribute or Name       [bits]        Value
        AFEN*                                      1             0         If this sub-register is set to 1, the corresponding address
                                                                           filter unit is enabled.
        MACEA0..7          macExtendedAddress      64            0         These registers define the macExtendedAddress.
        MACSHA0F*,         macShortAddress         16            0xFFFF    These registers define the macSortAddress.
        MACSHA1F*
        MACPID0F*,         macPANId                16            0xFFFF    These registers define the macPANId.
        MACPID1F*
        PM                 macPromiscuousMode      1             0         If this sub-register is set to 1, the frame filter operates in
                                                                           promiscuous mode.
        PANC*              PANCoordinator          1             0         If this sub-register is set to 1, the frame filter operates as a
                                                                           PAN coordinator.




                                                                                       Atmel AT86RF215 - DATASHEET                      144
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 145 -->

        Sub-register        IEEE 802.15.4-2006             Size         Reset    Comment
        Name                Attribute or Name              [bits]       Value
        AFFTM               frame type bitmask             8            0x0B     Address filter frame type bitmask.
        MRFT*               map reserved frame             1            0        If this sub-register is set to 1, incoming frames with
                            types                                                reserved frame types [4..7] are filtered like data frames. If
                                                                                 the frame header matches the address filter, RXAM IRQ
                                                                                 occurs. A RXEM IRQ is issued anyway.
        AFFVM               frame version bitmask          4            3        Address filter frame version mask
        AM*                 address filter status          1            0        If this bit is set to 1, the address filter has detected an
                                                                                 address match. This bit is updated once the MAC header
                                                                                 of an incoming frame is completely parsed.
        EM                  extended match status          1            0        If this bit is set to 1, the frame filter has detected an
                                                                                 extended match. The bit is updated once the MAC header
                                                                                 of an incoming frame is completely parsed.
       Note:      Register names marked with a star “*” are indexed with the last digit to be valid for each of the four 3 rd level
                  filter units (i.e. AFEN* is implemented as AFEN0, AFEN1, AFEN2, AFEN3).
6.15.2.7 Interrupts
       Four baseband IRQs are related to frame reception, see section "Baseband Interrupts" on page 82 for further
       information about the other baseband interrupts. The interrupt receiver frame start (IRQS.RXFS) indicates a valid frame
       header detection. The interrupt receiver address match (IRQS.RXAM) occurs if the address filter is enabled and the
       frame matches the address filter rules. The interrupt receiver extended match (IRQS.RXEM) occurs if the address filter
       is enabled and the frame matches the extended rules, see above. The interrupt receiver frame end (IRQS.RXFE)
       occurs at frame end to indicate that the entire frame has been stored to the RX frame buffer and is available for further
       processing by an external microcontroller. IRQS.RXFE is only issued if all filters are passed. The dependencies of the
       four RX IRQs are shown in Table 6-136.

       Table 6-136. Receiver IRQ Occurrences during Frame Receive Processing

        Address filter settings and scan results                                           IRQ occurrence
        AFEN         AM             EM              PM              First Level of              IRQ             IRQ             IRQ             IRQ
                                                                    Filtering passed           RXFS            RXAM            RXEM            RXFE
        address      address        extended        receiver
        filter       filter         match           promiscuous
        enabled      match          detected        mode
                     detected
        0            n.a.           n.a.            n.a.            0                      1               0               0               0
        0            n.a.           n.a.            n.a.            1                      1               0               0               1
        1            0              0               0               0                      1               0               0               0
        1            1              0               0               0                      1               1               0               0
        1            0              1               0               0                      1               0               1               0
        1            1              1               0               0                      1               1               1               0
        1            0              0               0               1                      1               0               0               0
        1            0              0               1               1                      1               0               0               1
        1            0              1               0               1                      1               0               1               1
        1            0              1               1               1                      1               0               1               1
        1            1              0               0               1                      1               1               0               1



                                                                                               Atmel AT86RF215 - DATASHEET                       145
                                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 146 -->

        Address filter settings and scan results                                    IRQ occurrence
        AFEN          AM           EM          PM             First Level of             IRQ             IRQ             IRQ             IRQ
                                                              Filtering passed          RXFS            RXAM            RXEM            RXFE
        address       address      extended    receiver
        filter        filter       match       promiscuous
        enabled       match        detected    mode
                      detected
        1             1            0           1              1                     1               1               0               1
        1             1            1           0              1                     1               1               1               1
        1             1            1           1              1                     1               1               1               1
       Note:      If an ACK frame is received, an IRQ RXFE occurs without the interrups RXAM and RXEM.

6.15.3 Automatic Acknowledgement (AACK)
6.15.3.1 Overview
       Automatic Acknowledgement is a procedure that transmits automatically an acknowledgement (ACK) frame if the
       following conditions of an incoming frame are met:
               Frame passes all third level filtering rules (see section "Address Filter" on page 142)
               The frame type is one (i.e. data frame) or three (i.e. MAC command frame)
               The ACK request bit of the frame control field is set to 1.


       AACK Features:
               Automatic sequence number handling
               Automatic FCS generation
               Configurable timing between RX frame end and ACK frame start
               Data rate of ACK frame can be determined by incoming frame or by predefined TX settings
               Configuration of the ACK frame content source: Either the ACK frame content is generated internally or the
                ACK frame is sent from the TX frame buffer (requires controller interaction).
               FCS type of the ACK can be derived from incoming frame or from predefined settings


       The embedded AACK procedure supports IEEE Std 802.15.4TM-2006 [1]. Do not use AACK in conjunction with
       procedure "Transmit and Switch to Receive (TX2RX)".

6.15.3.2 Configuration
       The AACK procedure is enabled if sub-register AMCS.AACK is set to 1. Additionally, the frame filter (see section
       "Frame Filter" on page 141) has to be enabled (and configured).
       The ACK time tack between IRQ RXFE and ACK transmit start is configured by registers BBCn_AMAACKTL and
       BBCn_AMAACKTH (see section "Timing" on page 148).
       The ACK frame data rate is selected by sub-register AMCS.AACKDR. This setting enables the feature ACK data rate
       adaptation. If sub-register AMCS.AACKDR is set to 1, some configured PHY settings are overwritten during the
       transmission of the ACK frame (see Table 6-137) and restored once the ACK frame transmit is completed. The re-
       programmed settings are PHY dependent as described in Table 6-137.




                                                                                        Atmel AT86RF215 - DATASHEET                       146
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 147 -->

Table 6-137. Reprogrammed Data Rate Settings during AACK if sub-register AMCS.AACKDR is set to 1

PHY type               Reprogrammed data rate settings with            Comment
                       feature ACK data rate adaptation

MR-OFDM                OFDMPHRTX.MCS = OFDMPHRRX.MCS                   MCS level of the ACK frame is adapted to the MCS level
                                                                       of the received frame.

MR-FSK                 FSKPHRTX.SFD = FSKPHRRX.SFD                     SFD selection is adapted to the recognized SFD of the
                                                                       received frame.

MR-OQPSK / OQPSK       OQPSKPHRTX.LEG = OQPSKPHRRX.LEG                 Transmission of legacy OQPSK upon receive of legacy
                                                                       OQPSK. Adaption of rate mode and PPDU type setting
                       OQPSKPHRTX.MOD = OQPSKPHRRX.MOD
                                                                       of the ACK frame to the received frame.
                       OQPSKPHRTX.PPDUT = OQPSKPHRRX.PPDUT



The ACK FCS type is selected by the sub-register AMCS.AACKFA. If this sub-register is set to 1, the automatic FCS
adaptation of the ACK frame is enabled. This feature applies to MR-FSK and legacy O-QPSK PHY only. For MR-OFDM
and MR-OQPSK this feature has no effect since the FCS type of the received frame must match the setting in PC.FCST
anyway.
The source of the ACK frame content is set by the sub-register AMCS.AACKS. If this sub-register is set to 0, the ACK
frame content is generated autonomously by the AT86RF215. The sequence number of the received frame is copied to
the ACK frame. Depending on the selected FCS type, the ACK frame has a length of 5 octets (16-bit FCS) or a length of
7 octets (32-bit FCS). The FCS is appended (as specified in [1] and [3]). The transmit frame buffer is not used.
If the sub-register AMCS.AACKS is set to 1, the ACK frame content is transmitted using the TX frame buffer content.
The ACK frame length must be configured by registers BBCn_TXFLL and BBCn_TXFLH. The MCU must provide the
frame content to the transmit frame buffer and FCS settings before the time tack expires.
During ACK transmit, the frame pending field of the ACK’s frame control field (see [1]) is derived from register
BBCn_AMAACKPD. Depending on the address filter unit that has detected an address filter match (see section "Multi
Address Filtering (MAF)" on page 144), the content of sub-register AMAACKPD.PD0, AMAACKPD.PD1,
AMAACKPD.PD2 or AMAACKPD.PD3 is copied to the frame pending field.
If the ACK frame transmission is sent completely, the IRQ TXFE occurs to indicate that the procedure is completed.
Figure 6-33 shows the AT86RF215 state, interrupts and RF-signals for the AACK procedure. If the received frame does
not require an acknowledgement (e.g. for a beacon frame), the AACK procedure finishes with the interrupt RXFE in
state TXPREP.

Figure 6-33. AACK Procedure

                                                  trxfe
                                                            tack

 RF Signal               Receive frame                                      ACK frame


 STATE                         RX                         TXPREP                 TX                             TXPREP


 IRQ
                        RXFS   RXAM/                RXFE                                             TXFE
                               RXEM




                                                                          Atmel AT86RF215 - DATASHEET                      147
                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 148 -->

6.15.3.3 Timing
       While the AT86RF215 is in the state RX, enabled receiver interrupts occur as described in section "Baseband
       Interrupts" on page 82. The interrupt RXFE has a delay of trxfe relative to the last bit at the antenna signal. The time trxfe
       depends on PHY settings.
       The ACK frame is transmitted tack after the interrupt RXFE. The time tack is configurable by registers BBCn_AMAACKTL
       and BBCn_AMAACKTH.

6.15.4 Transmit and Switch to Receive (TX2RX)
       Transmit and switch to receive is a procedure that switches to the state RX automatically if the frame transmission is
       completed. The procedure is useful if an ACK reception is expected after a transmission.
       The TX2RX feature can be combined with certain frame filter settings (i.e. blocking all frames except ACK frames)
       getting only the interrupt RXFE if an ACK frame is expected. Timeouts must be supervised by an external controller.
       The procedure TX2RX is enabled by sub-register AMCS.TX2RX. Figure 6-34 shows a TX2RX scenario.

       Figure 6-34. Behaviour of procedure TX2RX

        RF Signal                       Transmit Frame


        STATE       TXPREP                    TX                      RX


        IRQ
                                                               TXFE


       Do not use procedure TX2RX together with procedure "Automatic Acknowledgement (AACK)" and not together with
       procedure "Clear Channel Assessment with Automatic Transmit (CCATX)".



6.15.5 Clear Channel Assessment with Automatic Transmit (CCATX)
       The procedure CCATX provides a clear channel assessment (CCA) meachnism with an automatic frame transmission if
       the channel is assessed as idle. The CCA measurement based on the energy detection mode (CCA-ED) is supported
       only [1].
       The procedure CCATX is enabled if the sub-register AMCS.CCATX is set to 1. It is started with a single energy
       detection (ED) measurement (by writing the value 0x1 to sub-register EDC.EDM; see section "Energy Measurement" on
       page 56). The ED measurement time tED is configured by the register RFn_EDD and the AT86RF215 must be in state
       RX to start the procedure. The interrupt EDC is issued if the ED measurement is finished. The ED result is compared to
       the threshold value set by register BBCn_AMEDT.
       If the measured ED value is above the value in register BBCn_AMEDT, the channel is assessed as busy and the
       interrupt TXFE is issued. The sub-register AMCS.CCAED is set with the occurrence of the interrupt EDC containing the
       result of the comparison.
       If the ED value is equal or below the value in register BBCn_AMEDT, the channel is assessed as clear. The sub-
       register AMCS.CCAED is set to 0 with the occurrence of the interrupt EDC. The AT86RF215 switches to state TXPREP
       and state TX automatically afterwards and transmits the frame from the TX frame buffer. Once the state TXPREP is
       reached the interrupt TRXRDY is issued. Once the frame transmission is completed, the interrupt TXFE is issued.




                                                                                       Atmel AT86RF215 - DATASHEET                      148
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 149 -->

       It is recommended disabling the baseband (set PC.BBEN to 0) to avoid that the baseband decodes/receives any frame
       during the ED measurement. The baseband is enabled automatically again (and the sub-register PC.BBEN is
       automatically set to 1) if the procedure CCATX detects a clear channel since the baseband must be enabled for
       transmit. If the baseband has been disabled for the measurement period and the channel has assessed as busy, the
       baseband needs to be enabled again by setting PC.BBEN to 1. Do not use procedure CCATX together with procedure
       "Transmit and Switch to Receive (TX2RX)".
       The following Figure 6-35 and Figure 6-36 show the respective behaviour.

       Figure 6-35. Behaviour of procedure CCATX detecting a busy channel

       RF Signal                   Signal on Desired Channel


       STATE                                              RX

       Energy
       Detection        off                      active                    off


       IRQ
                                                                   TXFE,
                                                   ted             EDC




       Note:       The procedure CCATX is started by a single ED measurement only (EDC.EDM = 0x1).




       Figure 6-36. Behaviour of procedure CCATX detecting a clear channel


        RF Signal                                                                        Transmit Frame


        STATE                                RX                        TXPREP                 TX                 TXPREP

        Energy
        Detection        off                      active                                      off


        IRQ
                                                                    EDC,                                     TXFE
                                                                    TRXRDY
                                                    ted




6.15.6 Register Description
6.15.6.1 BBCn_AFC0 – Address Filter Configuration 0
       This register configures the address filter.
        Bit                    7            6                  5   4               3           2             1             0
                               –             –                 –   PM            AFEN3      AFEN2         AFEN1        AFEN0            BBCn_AFC0
        Read/Write             R            R                  R   RW             RW          RW           RW            RW
        Initial Value          0            0                  0   0               0           0             0             0

        Bit 4 – AFC0.PM: Promiscuous Mode
       This sub-register controls the promiscuous mode.


                                                                                                    Atmel AT86RF215 - DATASHEET                     149
                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 150 -->

       Table 6-138. PM

        Sub-register           Value        Description
        PM                      0x0         Promiscuous mode is disabled
                                0x1         Promiscuous mode is enabled

        Bit 3 – AFC0.AFEN3: Address Filter Enable 3
       If this sub-register is set to 1, the global filter, the extended filter and the 3rd level filter unit #3 are enabled.

        Bit 2 – AFC0.AFEN2: Address Filter Enable 2
       If this sub-register is set to 1, the global filter, the extended filter and the 3rd level filter unit #2 are enabled.

        Bit 1 – AFC0.AFEN1: Address Filter Enable 1
       If this sub-register is set to 1, the global filter, the extended filter and the 3rd level filter unit #1 are enabled.

        Bit 0 – AFC0.AFEN0: Address Filter Enable 0
       If this sub-register is set to 1, the global filter, the extended filter and the 3rd level filter unit #0 are enabled.


6.15.6.2 BBCn_AFC1 – Address Filter Configuration 1
       This register configures the address filter.
        Bit                7            6           5          4           3           2            1             0
                        MRFT3         MRFT2      MRFT1      MRFT0       PANC3       PANC2       PANC1         PANC0            BBCn_AFC1
        Read/Write       RW            RW          RW         RW           RW         RW          RW            RW
        Initial Value      0            0           0          0           0           0            0             0

        Bit 7 – AFC1.MRFT3: Map Reserved Frame Types 3
       This sub-register controls the 3rd level filter unit 3. If this sub-register is set to 1, frames with reserved frame types (4, 5,
       6 or 7) are handeled like data frames. Otherwise, reserved frame types are discarded.

        Bit 6 – AFC1.MRFT2: Map Reserved Frame Types 2
       This sub-register controls the 3rd level filter unit 2. If this sub-register is set to 1, frames with reserved frame types (4, 5,
       6 or 7) are handeled like data frames. Otherwise, reserved frame types are discarded

        Bit 5 – AFC1.MRFT1: Map Reserved Frame Types 1
       This sub-register controls the 3rd level filter unit 1. If this sub-register is set to 1, frames with reserved frame types (4, 5,
       6 or 7) are handeled like data frames. Otherwise, reserved frame types are discarded.

        Bit 4 – AFC1.MRFT0: Map Reserved Frame Types 0
       This sub-register controls the 3rd level filter unit 0. If this sub-register is set to 1, frames with reserved frame types (4, 5,
       6 or 7) are handeled like data frames. Otherwise, reserved frame types are discarded.

        Bit 3 – AFC1.PANC3: PAN Coordinator 3
       If this sub-register is set to 1, the 3rd level filter unit 3 is configured as a PAN coordinator.

        Bit 2 – AFC1.PANC2: PAN Coordinator 2
       If this sub-register is set to 1, the 3rd level filter unit 2 is configured as a PAN coordinator.

        Bit 1 – AFC1.PANC1: PAN Coordinator 1
       If this sub-register is set to 1, the 3rd level filter unit 1 is configured as a PAN coordinator.



                                                                                           Atmel AT86RF215 - DATASHEET                     150
                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| PM | 0x0 | Promiscuous mode is disabled |
|  | 0x1 | Promiscuous mode is enabled |


<!-- page 151 -->

        Bit 0 – AFC1.PANC0: PAN Coordinator 0
       If this sub-register is set to 1, the 3rd level filter unit 0 is configured as a PAN coordinator.

6.15.6.3 BBCn_AFFTM – Address Filter Frame Type Mask
       This register controls the global frame type filter. A bit which is 0 in AFFTM refuses frames with respective frame types
       (i.e. if bit 2 is clear, all frames with frame type 2 are refused). Otherwise a bit is set, frames with respective frame types
       are processed by further filter stages. The reset value is set to 0x0B. Thus, the address filter does not refuse frames
       with frame types 0, 1 and 3 (beacon, data, command frames) by default.
        Bit               7           6           5           4            3         2             1             0
                                                                  AFFTM                                                      BBCn_AFFTM
        Read/Write       RW          RW          RW          RW           RW        RW            RW           RW
        Initial Value     0           0           0           0            1         0             1             1

        Bit 7:0 – AFFTM.AFFTM: Address Filter Frame Type Mask
6.15.6.4 BBCn_AFFVM – Address Filter Frame Version Mask
        Bit               7           6           5           4            3         2             1             0
                           –          –           –           –                           AFFVM                              BBCn_AFFVM
        Read/Write        R           R           R           R           RW        RW            RW           RW
        Initial Value     0           0           0           0            0         0             1             1

        Bit 3:0 – AFFVM.AFFVM: Address Filter Frame Version Mask
       This register controls the global frame version filter. A bit which is 0 in AFFVM refuses frames with respective frame
       versions (i.e. if bit 1 is 0, all frames with frame version 1 are refused). Otherwise a bit is set to 1, frames with respective
       frame versions are processed by further filter stages. The reset value 3 does not refuse frames with frame version 0 and
       1.

6.15.6.5 BBCn_AFS – Address Filter Status
       This register provides the status of the address filter.
        Bit               7           6           5           4            3         2             1             0
                           –          –           –          EM           AM3       AM2           AM1          AM0            BBCn_AFS
        Read/Write        R           R           R           R            R         R             R            R
        Initial Value     0           0           0           0            0         0             0             0

        Bit 4 – AFS.EM: Extended Match
       This sub-register is set to 1 if the extended filter detects an extended match. This bit is automatically cleared with a
       frame start event (IRQ RXFS).

        Bit 3 – AFS.AM3: Address Match Filter 3
       This sub-register is set to 1 if the 3rd level filter unit #3 detects an address match. This bit is automatically cleared with a
       frame start event (IRQ RXFS).

        Bit 2 – AFS.AM2: Address Match Filter 2
       This sub-register is set to 1 if the 3rd level filter unit #2 detects an address match. This bit is automatically cleared with a
       frame start event (IRQ RXFS).

        Bit 1 – AFS.AM1: Address Match Filter 1
       This sub-regsiter is set to 1 if the 3rd level filter unit #1 detects an address match. This bit is automatically cleared with a
       frame start event (IRQ RXFS).



                                                                                          Atmel AT86RF215 - DATASHEET                     151
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 152 -->

       Bit 0 – AFS.AM0: Address Match Filter 0
      This sub-register is set to 1 if the 3rd level filter unit #0 detects an address match. This bit is automatically cleared with a
      frame start event (IRQ RXFS).

6.15.6.6 BBCn_MACEA0 – MAC Extended Address Byte 0
      This register contains the MAC extended address bits 7 to 0.
       Bit               7          6           5           4            3         2            1             0
                                                                MACEA0                                                   BBCn_MACEA0
       Read/Write       RW         RW          RW          RW         RW          RW          RW            RW
       Initial Value     0          0           0           0            0         0            0             0

       Bit 7:0 – MACEA0.MACEA0: MAC Extended Address Byte 0
6.15.6.7 BBCn_MACEA1 – MAC Extended Address Byte 1
      This register contains the MAC extended address bits 15 to 8.
       Bit               7          6           5           4            3         2            1             0
                                                                MACEA1                                                   BBCn_MACEA1
       Read/Write       RW         RW          RW          RW         RW          RW          RW            RW
       Initial Value     0          0           0           0            0         0            0             0

       Bit 7:0 – MACEA1.MACEA1: MAC Extended Address Byte 1
6.15.6.8 BBCn_MACEA2 – MAC Extended Address Byte 2
      This register contains the MAC extended address bits 23 to 16.
       Bit               7          6           5           4            3         2            1             0
                                                                MACEA2                                                   BBCn_MACEA2
       Read/Write       RW         RW          RW          RW         RW          RW          RW            RW
       Initial Value     0          0           0           0            0         0            0             0

       Bit 7:0 – MACEA2.MACEA2: MAC Extended Address Byte 2
6.15.6.9 BBCn_MACEA3 – MAC Extended Address Byte 3
      This register contains the MAC extended address bits 31 to 17.
       Bit               7          6           5           4            3         2            1             0
                                                                MACEA3                                                   BBCn_MACEA3
       Read/Write       RW         RW          RW          RW         RW          RW          RW            RW
       Initial Value     0          0           0           0            0         0            0             0

       Bit 7:0 – MACEA3.MACEA3: MAC Extended Address Byte 3
6.15.6.10 BBCn_MACEA4 – MAC Extended Address Byte 4
      This register contains the MAC extended address bits 39 to 32.




                                                                                       Atmel AT86RF215 - DATASHEET                     152
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 153 -->

        Bit               7          6           5           4            3         2             1             0
                                                                 MACEA4                                                    BBCn_MACEA4
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     0          0           0           0            0         0             0             0

        Bit 7:0 – MACEA4.MACEA4: MAC Extended Address Byte 4
6.15.6.11 BBCn_MACEA5 – MAC Extended Address Byte 5
       This register contains the MAC extended address bits 47 to 40.
        Bit               7          6           5           4            3         2             1             0
                                                                 MACEA5                                                    BBCn_MACEA5
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     0          0           0           0            0         0             0             0

        Bit 7:0 – MACEA5.MACEA5: MAC Extended Address Byte 5
6.15.6.12 BBCn_MACEA6 – MAC Extended Address Byte 6
       This register contains the MAC extended address bits 55 to 48.
        Bit               7          6           5           4            3         2             1             0
                                                                 MACEA6                                                    BBCn_MACEA6
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     0          0           0           0            0         0             0             0

        Bit 7:0 – MACEA6.MACEA6: MAC Extended Address Byte 6
6.15.6.13 BBCn_MACEA7 – MAC Extended Address Byte 7
       This register contains the MAC extended address bits 63 to 56.
        Bit               7          6           5           4            3         2             1             0
                                                                 MACEA7                                                    BBCn_MACEA7
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     0          0           0           0            0         0             0             0

        Bit 7:0 – MACEA7.MACEA7: MAC Extended Address Byte 7
6.15.6.14 BBCn_MACPID0F0 – MAC Pan ID Byte 0 Filter 0
       This register contains the MAC Pan ID bits 7 to 0 for 3rd level filter unit 0.
        Bit               7          6           5           4            3         2             1             0
                                                             MACPID0F0                                                   BBCn_MACPID0F0
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1            1         1             1             1

        Bit 7:0 – MACPID0F0.MACPID0F0: MAC Pan ID Byte 0 Filter 0
6.15.6.15 BBCn_MACPID1F0 – MAC Pan ID Byte 1 Filter 0
       This register contains the MAC Pan ID bits 15 to 8 for 3rd level filter unit 0.




                                                                                         Atmel AT86RF215 - DATASHEET                     153
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 154 -->

        Bit               7          6           5           4          3           2             1             0
                                                             MACPID1F0                                                   BBCn_MACPID1F0
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID1F0.MACPID1F0: MAC Pan ID Byte 1 Filter 0
6.15.6.16 BBCn_MACSHA0F0 – MAC Short Address Byte 0 Filter 0
       This register contains the MAC short address bits 7 to 0 for 3rd level filter unit 0.
        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA0F0                                                  BBCn_MACSHA0F0
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA0F0.MACSHA0F0: MAC Short Address Byte 0 Filter 0
6.15.6.17 BBCn_MACSHA1F0 – MAC Short Address Byte 1 Filter 0
       This register contains the MAC short address bits 15 to 8 for 3rd level filter unit 0.
        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA1F0                                                  BBCn_MACSHA1F0
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA1F0.MACSHA1F0: MAC Short Address Byte 1 Filter 0
6.15.6.18 BBCn_MACPID0F1 – MAC Pan ID Byte 0 Filter 1
       This register contains the MAC Pan ID bits 7 to 0 for 3rd level filter unit 1.
        Bit               7          6           5           4          3           2             1             0
                                                             MACPID0F1                                                   BBCn_MACPID0F1
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID0F1.MACPID0F1: MAC Pan ID Byte 0 Filter 1
6.15.6.19 BBCn_MACPID1F1 – MAC Pan ID Byte 1 Filter 1
       This register contains the MAC Pan ID bits 15 to 8 for 3rd level filter unit 1.
        Bit               7          6           5           4          3           2             1             0
                                                             MACPID1F1                                                   BBCn_MACPID1F1
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID1F1.MACPID1F1: MAC Pan ID Byte 1 Filter 1
6.15.6.20 BBCn_MACSHA0F1 – MAC Short Address Byte 0 Filter 1
       This register contains the MAC short address bits 7 to 0 for 3rd level filter unit 1.




                                                                                         Atmel AT86RF215 - DATASHEET                     154
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 155 -->

        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA0F1                                                  BBCn_MACSHA0F1
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA0F1.MACSHA0F1: MAC Short Address Byte 0 Filter 1
6.15.6.21 BBCn_MACSHA1F1 – MAC Short Address Byte 1 Filter 1
       This register contains the MAC short address bits 15 to 8 for 3rd level filter unit 1.
        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA1F1                                                  BBCn_MACSHA1F1
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA1F1.MACSHA1F1: MAC Short Address Byte 1 Filter 1
6.15.6.22 BBCn_MACPID0F2 – MAC Pan ID Byte 0 Filter 2
       This register contains the MAC Pan ID bits 7 to 0 for 3rd level filter unit 2.
        Bit               7          6           5           4          3           2             1             0
                                                             MACPID0F2                                                   BBCn_MACPID0F2
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID0F2.MACPID0F2: MAC Pan ID Byte 0 Filter 2
6.15.6.23 BBCn_MACPID1F2 – MAC Pan ID Byte 1 Filter 2
       This register contains the MAC Pan ID bits 15 to 8 for 3rd level filter unit 2.
        Bit               7          6           5           4          3           2             1             0
                                                             MACPID1F2                                                   BBCn_MACPID1F2
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID1F2.MACPID1F2: MAC Pan ID Byte 1 Filter 2
6.15.6.24 BBCn_MACSHA0F2 – MAC Short Address byte 0 Filter 2
       This register contains the MAC short address bits 7 to 0 for 3rd level filter unit 2.
        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA0F2                                                  BBCn_MACSHA0F2
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA0F2.MACSHA0F2: MAC Short Address byte 0 Filter 2
6.15.6.25 BBCn_MACSHA1F2 – MAC Short Address byte 1 Filter 2
       This register contains the MAC short address bits 15 to 8 for 3rd level filter unit 2.




                                                                                         Atmel AT86RF215 - DATASHEET                     155
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 156 -->

        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA1F2                                                  BBCn_MACSHA1F2
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA1F2.MACSHA1F2: MAC Short Address byte 1 Filter 2
6.15.6.26 BBCn_MACPID0F3 – MAC Pan ID Byte 0 Filter 3
       This register contains the MAC Pan ID bits 7 to 0 for 3rd level filter unit 3.
        Bit               7          6           5           4          3           2             1             0
                                                             MACPID0F3                                                   BBCn_MACPID0F3
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID0F3.MACPID0F3: MAC Pan ID Byte 0 Filter 3
6.15.6.27 BBCn_MACPID1F3 – MAC Pan ID Byte 1 Filter 3
       This register contains the MAC Pan ID bits 15 to 8 for 3rd level filter unit 3.
        Bit               7          6           5           4          3           2             1             0
                                                             MACPID1F3                                                   BBCn_MACPID1F3
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACPID1F3.MACPID1F3: MAC Pan ID Byte 1 Filter 3
6.15.6.28 BBCn_MACSHA0F3 – MAC Short Address byte 0 Filter 3
       This register contains the MAC short address bits 7 to 0 for 3rd level filter unit 3.
        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA0F3                                                  BBCn_MACSHA0F3
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA0F3.MACSHA0F3: MAC Short Address byte 0 Filter 3
6.15.6.29 BBCn_MACSHA1F3 – MAC Short Address byte 1 Filter 3
       This register contains the MAC short address bits 15 to 8 for 3rd level filter unit 3.
        Bit               7          6           5           4          3           2             1             0
                                                             MACSHA1F3                                                  BBCn_MACSHA1F3
        Read/Write       RW         RW          RW          RW         RW          RW           RW            RW
        Initial Value     1          1           1           1          1           1             1             1

        Bit 7:0 – MACSHA1F3.MACSHA1F3: MAC Short Address byte 1 Filter 3
6.15.6.30 BBCn_AMCS – Auto Mode Configuration and Status
       This register contains configuration and status information for the auto modes.




                                                                                         Atmel AT86RF215 - DATASHEET                     156
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 157 -->

Bit                7           6            5          4          3          2              1             0
                AACKFT     AACKFA        AACKDR     AACKS       AACK       CCAED        CCATX         TX2RX           BBCn_AMCS
Read/Write         R           RW          RW         RW         RW          R            RW            RW
Initial Value      0           0            0          0          0          0              0             0

 Bit 7 – AMCS.AACKFT: Auto Acknowledgement Frame Transmit
If this bit has been set to 1, the AACK procedure has automatically transmitted an ACK frame. Otherwise no automatic
ACK frame has been transmitted. This bit is updated with the IRQ RXFE if the AACK procedure is active.

Table 6-139. AACKFT

Sub-register           Value        Description
AACKFT                   0x0        No ACK frame has been automatically transmitted,
                         0x1        An ACK frame has been automatically transmitted.

 Bit 6 – AMCS.AACKFA: Auto Acknowledgement FCS Adaption
If this sub-register is set to 1, the FCS type of the automatically generated ACK frame is derived from the FCS type of
the received frame. Otherwise, if this sub-register is 0, the FCS type of the ACK frame is derived from the setting in sub-
register PC.FCST.

Table 6-140. AACKFA

Sub-register           Value        Description
AACKFA                   0x0        FCS type of AACK derived from setting FCST
                         0x1        FCS type of AACK derived from previous received frame

 Bit 5 – AMCS.AACKDR: Auto Acknowledgement Data Rate
If this bit is set to 1, the automatic acknowledgement is sent using the modulation settings of the received frame. If this
bit is set to 0, the automatic acknowledgement is transmitted using the current PHY settings.

Table 6-141. AACKDR

Sub-register           Value        Description
AACKDR                   0x0        Automatic ACK data rate derived from current PHY settings
                         0x1        Automatic ACK data rate equals received frame

 Bit 4 – AMCS.AACKS: Auto Acknowledgement Source
If this bit is set to 0, the automatic acknowledgement is sent by the transceiver respective to IEEE Std 802.15.4-2006.
The transmit frame buffer is not changed. If this bit is set to 1, the automatic acknowledgement is transmitted from the
transmit frame buffer.

Table 6-142. AACKS

Sub-register           Value        Description
AACKS                    0x0        Automatic ACK generated by transceiver
                         0x1        Automatic ACK transmit from transmit frame buffer

 Bit 3 – AMCS.AACK: Auto Acknowledgement
If this bit is set to 1, the automatic acknowledgement feature is enabled. This bit is only applicable if the address filter is
enabled.




                                                                                 Atmel AT86RF215 - DATASHEET                       157
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| AACKFT | 0x0 | No ACK frame has been automatically transmitted, |
|  | 0x1 | An ACK frame has been automatically transmitted. |

| Sub-register | Value | Description |
| --- | --- | --- |
| AACKFA | 0x0 | FCS type of AACK derived from setting FCST |
|  | 0x1 | FCS type of AACK derived from previous received frame |

| Sub-register | Value | Description |
| --- | --- | --- |
| AACKDR | 0x0 | Automatic ACK data rate derived from current PHY settings |
|  | 0x1 | Automatic ACK data rate equals received frame |

| Sub-register | Value | Description |
| --- | --- | --- |
| AACKS | 0x0 | Automatic ACK generated by transceiver |
|  | 0x1 | Automatic ACK transmit from transmit frame buffer |


<!-- page 158 -->

       Table 6-143. AACK

       Sub-register           Value        Description
       AACK                    0x0         Automatic Acknowledge disabled
                               0x1         Automatic Acknowledge enabled

        Bit 2 – AMCS.CCAED: CCA Energy Detection Result
       This bit indicates the status of the result of the last CCA measurement. It is updated with the finished ED measurement,
       while the procedure CCATX is active.

       Table 6-144. CCAED

       Sub-register        Name                          Value      Description
       CCAED               BB_CH_CLEAR                   0x0        Channel is clear
                           BB_CH_BUSY                    0x1        Channel is busy

        Bit 1 – AMCS.CCATX: CCA Measurement and automatic Transmit
       If this bit is set to 1, the auto mode feature CCA with automatic transmit is enabled.

       Table 6-145. CCATX

       Sub-register           Value        Description
       CCATX                   0x0         CCATX procedure is disabled
                               0x1         CCATX procedure is enabled

        Bit 0 – AMCS.TX2RX: Transmit and Switch to Receive
       If this bit is set to 1, the transceiver switches automatically to state RX if a transmit is completed.

       Table 6-146. TX2RX

       Sub-register           Value        Description
       TX2RX                   0x0         TX2RX procedure disabled
                               0x1         TX2RX procedure enabled

6.15.6.31 BBCn_AMEDT – Auto Mode Energy Detection Threshold
       This register contains the energy detection threshold for a CCA measurement. It is stored as a signed number in a
       range of [-127..128]. An ED value above the threshold indicates a busy channel, otherwise the channel is assessed as
       clear.
       Bit                7           6            5           4           3           2             1             0
                                                                   AMEDT                                                       BBCn_AMEDT
       Read/Write        RW           RW          RW        RW             RW          RW          RW            RW
       Initial Value      1           0            1           1           0           1             0             1

        Bit 7:0 – AMEDT.AMEDT: Auto Mode Energy Detection Threshold
6.15.6.32 BBCn_AMAACKPD – Auto Mode Automatic ACK Pending Data
       This register configures the behaviour of the pending data bit of an automatic acknowledgement frame.




                                                                                            Atmel AT86RF215 - DATASHEET                     158
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| AACK | 0x0 | Automatic Acknowledge disabled |
|  | 0x1 | Automatic Acknowledge enabled |

| Sub-register | Name | Value | Description |
| --- | --- | --- | --- |
| CCAED | BB_CH_CLEAR | 0x0 | Channel is clear |
|  | BB_CH_BUSY | 0x1 | Channel is busy |

| Sub-register | Value | Description |
| --- | --- | --- |
| CCATX | 0x0 | CCATX procedure is disabled |
|  | 0x1 | CCATX procedure is enabled |

| Sub-register | Value | Description |
| --- | --- | --- |
| TX2RX | 0x0 | TX2RX procedure disabled |
|  | 0x1 | TX2RX procedure enabled |


<!-- page 159 -->

       Bit               7        6          5          4          3         2             1             0
                         –         –         –          –        PD3        PD2          PD1           PD0        BBCn_AMAACKPD
       Read/Write       R         R          R          R        RW         RW           RW            RW
       Initial Value     0        0          0          0          0         0             0             0

       Bit 3 – AMAACKPD.PD3: Pending Data 3
      An automatic acknowledgement frame (transmitted by hardware) contains a set pending data subfield if the following
      conditions are met:
      - Bit PD3 is set to 1 and
      - The 3rd level filter unit #3 has detected a MAC command data request frame prior.

       Bit 2 – AMAACKPD.PD2: Pending Data 2
      An automatic acknowledgement frame (transmitted by hardware) contains a set pending data subfield if the following
      conditions are met:
      - Bit PD2 is set to 1 and
      - The 3rd level filter unit #2 has detected a MAC command data request frame prior.

       Bit 1 – AMAACKPD.PD1: Pending Data 1
      An automatic acknowledgement frame (transmitted by hardware) contains a set pending data subfield if the following
      conditions are met:
      - Bit PD1 is set to 1 and
      - The 3rd level filter unit #1 has detected a MAC command data request frame prior.

       Bit 0 – AMAACKPD.PD0: Pending Data 0
      An automatic acknowledgement frame (transmitted by hardware) contains a set of pending data subfield if the following
      conditions are met:
      - Bit PD0 is set to 1 and
      - The 3rd level filter unit #0 has detected a MAC command data request frame prior.

6.15.6.33 BBCn_AMAACKTL – Auto Mode Automatic ACK Time
      This register configures the time between IRQ RXFE and an automatic acknowledgement frame start in us. It contains
      the low byte.
       Bit               7        6          5          4          3         2             1             0
                                                        AMAACKTL                                                  BBCn_AMAACKTL
       Read/Write      RW         RW        RW         RW        RW         RW           RW            RW
       Initial Value     1        1          0          0          0         0             0             0

       Bit 7:0 – AMAACKTL.AMAACKTL: Auto Mode Automatic ACK Time
6.15.6.34 BBCn_AMAACKTH – Auto Mode Automatic ACK Time
      This register configures the time between IRQ RXFE and an automatic acknowledgement frame start in us. It contains
      the three most significant bits.




                                                                                  Atmel AT86RF215 - DATASHEET                     159
                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 160 -->

Bit             7     6        5       4        3       2             1             0
                –     –        –       –        –              AMAACKTH                      BBCn_AMAACKTH
Read/Write      R     R        R       R       R       RW           RW            RW
Initial Value   0     0        0       0        0       0             0             0

 Bit 2:0 – AMAACKTH.AMAACKTH: Auto Mode Automatic ACK Time




                                                            Atmel AT86RF215 - DATASHEET                      160
                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 161 -->

6.16   Random Number Generator
       The AT86RF215 has a true random number generator implemented. The unit generates random values by observation
       of noise. A random value contains eight bits and is available in register RFn_RNDV. It is updated with a period of tRND.
       The random values in RFn_RNDV are valid only if the following conditions are met:
              The AT86RF215 operates in state RX and the PLL has locked.
              The analog frontend (see "Receiver Analog Frontend" on page 52) of the radio must be configured to the
               widest filter bandwidth (RXBWC.BW = 0x0B).
              The bit RXBWC.IFS must be set to 1
              After entering state RX, the first two random values are invalid and are read from register RFn_RNDV.
       To prevent the baseband core from unwanted synchronization and frame reception during random number value
       reading, it is recommended switching off the baseband core by bit PC.BBEN.

6.16.1 Register Description
6.16.1.1 RFn_RNDV – Random Value
       The register contains an eight bit random value.
        Bit               7         6          5          4          3          2            1             0
                                                              RNDV                                                      RFn_RNDV
        Read/Write        R         R          R          R          R          R            R            R
        Initial Value     0         0          0          0          0          0            0             0




                                                                                    Atmel AT86RF215 - DATASHEET                     161
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 162 -->

6.17   Phase Measurement Unit

6.17.1 Description
       The Phase Measurement Unit (PMU) allows register based monitoring of the phase and several other signal
       parameters of the output of the Receiver Digital Frontend (RX_DFE) with a constant PMU period of 8 us.
       Given the complex RX_DFE output signal with components I_DATA and Q_DATA (see Figure 6-6 on page 53) ,
       denoted as x = xi + i*xq, Table 6-147 describes the PMU result options. Column BBCn_PMUC reflects the required bit-
       combination for control register BBCn_PMUC (MSB left; ‘x’ mark don’t care bits). A single configuration provides
       synchronous result values in all output registers BBCn_PMUVAL, BBCn_PMUQF, BBCn_PMUI and BBCn_PMUQ.

       Table 6-147. PMU Signal Monitoring Options

       Description                            Expression                                     Output Register             BBCn_PMUC
       Sampled Phase                          round( arg(x) / pi * 128 )                     BBCn_PMUVAL                 8’b0xxxxx01
       Average Phase                          round( arg(mean(x)) / pi * 128 )               BBCn_PMUVAL                 8’b0xxxxx11
       Sampled Real Part                      Re{x}, rounded to 8 bit                        BBCn_PMUI                   8’b01xxxx01
       Sampled Imaginary Part                 Im{x}, rounded to 8 bit                        BBCn_PMUQ                   8’b01xxxx01
       Average Real Part                      mean( Re{x} ), rounded to 8 bit                BBCn_PMUI                   8’b01xxxx11
       Average Imaginary Part                 mean( Im{x} ), rounded to 8 bit                BBCn_PMUQ                   8’b01xxxx11
       Sampled Normalized Real Part           round( Re{ exp(i*arg(x)) } * 63 )              BBCn_PMUI                   8’b00xxxx01
       Sampled Normalized Imaginary           round( Re{ exp(i*arg(x)) } * 63 )              BBCn_PMUQ                   8’b00xxxx01
       Part
       Average Normalized Real Part           round( Re{ exp(i*arg(mean(x))) } * 63 )        BBCn_PMUI                   8’b00xxxx11
       Average Normalized Imaginary Part      round( Re{ exp(i*arg(mean(x))) } * 63 )        BBCn_PMUQ                   8’b00xxxx11
       Phase Stability (Quality Factor)       inverse mean deviation of arg(x) over          BBCn_PMUQF                  8’b0x0xxxx1
                                              PMU period
       Frequency Offset (Phase Drift)         FO[Hz] = 500 kHz * BBCn_PMUQF / 256            BBCn_PMUQF                  8’b0x1xxxx1,
                                                                                                                         fs = 1MHz


       While ‘Sampled’ parameters are single captures of x at the end of the PMU period, averaging combines all samples
       within.
       Note that for frequency offset measurement the RX_DFE sample rate shall be configured to 1 MHz.
       Depending on the application it might be necessary to evaluate these signal parameters strictly synchronous to the
       PMU period. Sub register PMUC.SYNC helps to verify this synchronization. It reflects a 1MHz counter running from 0 to
       7 during the 8 us PMU period. All output registers are updated at the transition from 7 to 0.

6.17.2 Register
6.17.2.1 BBCn_PMUC – PMU Control
       This is the main control register for PMU functionality.




                                                                                        Atmel AT86RF215 - DATASHEET                     162
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 163 -->

Bit                7            6           5           4          3           2            1             0
                CCFTS         IQSEL        FED                   SYNC                     AVG            EN           BBCn_PMUC
Read/Write       RW            RW          RW           R          R          R           RW            RW
Initial Value      0            0           0           1          1           1            1             0

 Bit 7 – PMUC.CCFTS: Channel Center Frequency Time Synchronization
Channel Center Frequency Time Synchronization allows to restrict channel center frequency changes to a raster equal
to the PMU period.

Table 6-148. CCFTS

Sub-register           Value        Description
CCFTS                   0x0         Changes on the channel center frequency are directly applied according to register CNM.
                        0x1         Changes on the channel center frequency, initiated by register CNM, are time-aligned to the
                                    PMU period of 8 us.

 Bit 6 – PMUC.IQSEL: IQ Output Selector
IQSEL selects, if (PMUI+i*PMUQ) returns the normalized or not normalized I/Q representation corresponding to
PMUVAL.

Table 6-149. IQSEL

Sub-register           Value        Description
IQSEL                   0x0         Normalized I/Q: (PMUI + i*PMUQ) ~= 63 * exp( i * pi * PMUVAL / 128 )
                        0x1         I/Q without normalization: arg(PMUI + i*PMUQ) = pi * PMUVAL / 128.

 Bit 5 – PMUC.FED: Frequency Error Detection
If enabled, the PMUQF returns a frequency error estimate instead of the PMU quality factor.

Table 6-150. FED

Sub-register           Value        Description
FED                     0x0         Frequency error detection is disabled. PMUQF acts as an unsigned quality factor value
                                    [0..255].
                        0x1         Frequency error detection is enabled. For a sample rate of 1 MHz (RXDFE_SR==4) the
                                    measured frequency offset calculates to FO[Hz] = 1MHz/2 * PMUQF/256, where PMUQF is
                                    interpreted as a signed 2th-complement value [-128..127].

 Bit 4:2 – PMUC.SYNC: PMU Synchronisation
This subfield reflects a 1MHz counter running from 0 to 7 during the 8us PMU period and is dedicated for software
synchronisation.

 Bit 1 – PMUC.AVG: I/Q Averaging Enable
If averaging is enabled, the PMU computes a phase value, from the averaged receiver digital frontend I/Q output. The
averaging period is equal to the PMU period (8us). If averaging is disabled, the SNR of a PMU phase value depends on
the frontend filter configuration.




                                                                                   Atmel AT86RF215 - DATASHEET                     163
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CCFTS | 0x0 | Changes on the channel center frequency are directly applied according to register CNM. |
|  | 0x1 | Changes on the channel center frequency, initiated by register CNM, are time-aligned to the |
|  |  | PMU period of 8 us. |

| Sub-register | Value | Description |
| --- | --- | --- |
| IQSEL | 0x0 | Normalized I/Q: (PMUI + i*PMUQ) ~= 63 * exp( i * pi * PMUVAL / 128 ) |
|  | 0x1 | I/Q without normalization: arg(PMUI + i*PMUQ) = pi * PMUVAL / 128. |

| Sub-register | Value | Description |
| --- | --- | --- |
| FED | 0x0 | Frequency error detection is disabled. PMUQF acts as an unsigned quality factor value |
|  |  | [0..255]. |
|  | 0x1 | Frequency error detection is enabled. For a sample rate of 1 MHz (RXDFE_SR==4) the |
|  |  | measured frequency offset calculates to FO[Hz] = 1MHz/2 * PMUQF/256, where PMUQF is |
|  |  | interpreted as a signed 2th-complement value [-128..127]. |


<!-- page 164 -->

       Table 6-151. AVG

        Sub-register          Value       Description
        AVG                   0x0         I/Q sampling at end of PMU period
                              0x1         I/Q averaging over PMU period

        Bit 0 – PMUC.EN: PMU Enable
       If enabled, the phase measurement unit (PMU) periodically measures phase and other signal parameters based on the
       receiver digital frontend I/Q output.

       Table 6-152. EN

        Sub-register          Value       Description
        EN                    0x0         PMU disabled
                              0x1         PMU enabled

6.17.2.2 BBCn_PMUVAL – PMU Phase Value
       The PMU phase value is an 8-bit value, covering angles 0 to 2*pi, in 256 steps. A value of zero equals 0 degrees, a
       value of 255 equals 360/256*255 degrees.
        Bit               7           6           5          4            3    2            1             0
                                                                 PMUVAL                                              BBCn_PMUVAL
        Read/Write        R           R           R          R            R    R            R            R
        Initial Value     0           0           0          0            0    0            0             0

        Bit 7:0 – PMUVAL.PMUVAL: PMU Phase Value
6.17.2.3 BBCn_PMUQF – PMU Quality Factor
       If PMUC_FED=0, PMUQF represents the PMU quality factor as an 8-bit value related to the average change of phase
       drift during the PMU measurement interval. A value of 255 indicates best quality. If PMUC_FED=1, PMUQF represents
       a 2th-complement frequency offset measure.
        Bit               7           6           5          4            3    2            1             0
                                                                 PMUQF                                               BBCn_PMUQF
        Read/Write        R           R           R          R            R    R            R            R
        Initial Value     0           0           0          0            0    0            0             0

        Bit 7:0 – PMUQF.PMUQF: PMU Quality Factor
6.17.2.4 BBCn_PMUI – PMU I/Q value, real part.
       Real part of the PMU measurement value, 2th-complement (signed)
        Bit               7           6           5          4            3    2            1             0
                                                                  PMUI                                                 BBCn_PMUI
        Read/Write        R           R           R          R            R    R            R            R
        Initial Value     0           0           0          0            0    0            0             0

        Bit 7:0 – PMUI.PMUI: PMU I/Q value, real part, 2th-complement (signed)
6.17.2.5 BBCn_PMUQ – PMU I/Q value, imaginary part
       Imaginary part of the PMU measurement value, 2th-complement (signed)




                                                                                   Atmel AT86RF215 - DATASHEET                     164
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| AVG | 0x0 | I/Q sampling at end of PMU period |
|  | 0x1 | I/Q averaging over PMU period |

| Sub-register | Value | Description |
| --- | --- | --- |
| EN | 0x0 | PMU disabled |
|  | 0x1 | PMU enabled |


<!-- page 165 -->

Bit             7        6        5         4          3       2            1             0
                                                PMUQ                                                  BBCn_PMUQ
Read/Write      R        R        R         R          R       R            R            R
Initial Value   0        0        0         0          0       0            0             0

 Bit 7:0 – PMUQ.PMUQ: PMU I/Q value, imaginary part, 2th-complement (signed)




                                                                   Atmel AT86RF215 - DATASHEET                     165
                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 166 -->

6.18   Timestamp Counter

6.18.1 Overview
       Each baseband core contains a Timestamp Counter module with a 32-bit counter. The module can capture different
       timestamp information of received or transmitted frames or it operates as a free running counter.
       The registers BBCn_CNT0, BBCn_CNT1, BBCn_CNT2, BBCn_CNT3 are concatenated to the 32-bit counter word
       CNT. The register BBCn_CNT0 contains the least significant bits; BBCn_CNT3 contains the most significant bits. To
       retrieve a consistent 32-bit CNT value, all four registers must be read by a SPI block read access (see section "Block
       Access Mode" on page 17) starting with the register BBCn_CNT0. Otherwise, it leads to an inconsistent value.
       The counter offers several modes, see Table 6-153. The counter is enabled by setting the sub-register CNTC.EN to 1. If
       the sub-register is set to 0, the counter is stopped and reset to zero. The counter is reset to 0 automatically if either sub-
       register CNTC.RSTRXS or CNTC.RSTTXS is set to 1 and the respective event occurs.
       If enabled, the counter is running in all transceiver states, except states RESET, SLEEP and DEEP_SLEEP. It is
       clocked with a clock rate of 32MHz. If the counter reaches its maximum value of 0xFFFFFFFF, the counter overflows to
       zero with the next clock cycle.

       Table 6-153. Counter Modes

       Counter Mode               Configuration                                   Comment
       Off                        CNTC.EN = 0                                     The counter is reset to zero.
       Free running               CNTC.CAPRXS = 0 and                             The timestamp counter module operates in free
                                  CNTC.CAPTXS = 0                                 running counter mode. The CNT value reflects the
                                                                                  current counter value.
       Capture                    CNTC.CAPRXS = 1 or                              The timestamp counter module operates in
                                  CNTC.CAPTXS = 1                                 capture mode. The CNT value reflects the last
                                                                                  captured value.


       A typical application for the timestamp counter is visualized in Figure 6-37. It shows the reset of the counter value CNT
       with a TX start event and capture of the counter value with an RX frame start event.
       Note, the TX start event occurs ttx_bb_delay after the command TX is written to the register RFn_CMD (see 6.1.4).

       Figure 6-37. Application Example Timestamp Counter

       CNT                                                 y        z



       counter    x-1 x   0   1   2   3   4   5   6   7   z-1 z z+1 z+2 z+3



       TX start


       RX start
       Note:
       BBCn_CNTC.RSTTXS = 1
       BBCn_CNTC.CAPRXS = 1




                                                                                      Atmel AT86RF215 - DATASHEET                     166
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 167 -->

6.18.2 Register Description
6.18.2.1 BBCn_CNTC – Counter Configuration
       This register configures the timestamp counter.
        Bit                7           6            5           4           3           2             1             0
                           –           –            –       CAPTXS        CAPRXS    RSTTXS        RSTRXS           EN           BBCn_CNTC
        Read/Write         R           R            R         RW           RW           RW          RW            RW
        Initial Value      0           0            0           0           0           0             0             0

        Bit 4 – CNTC.CAPTXS: Capture of Counter Values at TX Start Event
       If this bit is set to 1, the counter value is captured to the registers BBCn_CNTn triggered by a TX start event. The TX
       start event complies to the rising edge of the enable of the power amplifier. If neither sub-register CAPRXS nor
       CAPTXS is set to 1, the registers BBCn_CNTn contain the current counter value.

       Table 6-154. CAPTXS

        Sub-register           Value       Description
        CAPTXS                  0x0        The counter value is not captured to registers BBCn_CNTn at TX start event.
                                0x1        The counter value is captured to registers BBCn_CNTn at TX start event.

        Bit 3 – CNTC.CAPRXS: Capture of Counter Values at RX Start Event
       If this bit is set to 1, the counter value is captured to the registers BBCn_CNTn triggered by an RX frame start event.
       The RX frame start event complies to the interrupt RXFS. If neither sub-register CAPRXS nor CAPTXS is set to 1, the
       registers BBCn_CNTn contain the current counter value.

       Table 6-155. CAPRXS

        Sub-register           Value       Description
        CAPRXS                  0x0        The counter value is not captured to registers BBCn_CNTn at RX frame start event.
                                0x1        The counter value is captured to registers BBCn_CNTn at RX frame start event.

        Bit 2 – CNTC.RSTTXS: Reset at TX Start Event
       If this bit is set to 1, the counter is reset at TX start event.

       Table 6-156. RSTTXS

        Sub-register           Value       Description
        RSTTXS                  0x0        The counter is not reset at TX start event
                                0x1        The counter is reset at TX start event

        Bit 1 – CNTC.RSTRXS: Reset at RX Start Event
       If this bit is set to 1, the counter is reset at RX frame start event. The RX frame start event complies to the interrupt
       RXFS.

       Table 6-157. RSTRXS

        Sub-register           Value       Description
        RSTRXS                  0x0        The counter is not reset at RX frame start event.
                                0x1        The counter is reset at RX frame start event.

        Bit 0 – CNTC.EN: Enable
       If this bit is set to 1, the counter is enabled.



                                                                                             Atmel AT86RF215 - DATASHEET                     167
                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CAPTXS | 0x0 | The counter value is not captured to registers BBCn_CNTn at TX start event. |
|  | 0x1 | The counter value is captured to registers BBCn_CNTn at TX start event. |

| Sub-register | Value | Description |
| --- | --- | --- |
| CAPRXS | 0x0 | The counter value is not captured to registers BBCn_CNTn at RX frame start event. |
|  | 0x1 | The counter value is captured to registers BBCn_CNTn at RX frame start event. |

| Sub-register | Value | Description |
| --- | --- | --- |
| RSTTXS | 0x0 | The counter is not reset at TX start event |
|  | 0x1 | The counter is reset at TX start event |

| Sub-register | Value | Description |
| --- | --- | --- |
| RSTRXS | 0x0 | The counter is not reset at RX frame start event. |
|  | 0x1 | The counter is reset at RX frame start event. |


<!-- page 168 -->

       Table 6-158. EN

       Sub-register          Value       Description
       EN                     0x0        The counter is disabled and reset to zero.
                              0x1        The counter is enabled and running.

6.18.2.2 BBCn_CNT0 – Counter Byte 0
       This register contains bits 7 to 0 of the 32-bit timestamp counter. The counter has a resolution of 1/32MHz. For a
       consistent counter value the registers BBCn_CNT0...3 have to be read by a SPI block access.
       Bit               7           6            5          4           3            2            1             0
                                                                 CNT0                                                         BBCn_CNT0
       Read/Write        R           R           R           R           R            R            R            R
       Initial Value     0           0            0          0           0            0            0             0

        Bit 7:0 – CNT0.CNT0: Counter Byte 0
6.18.2.3 BBCn_CNT1 – Counter Byte 1
       This register contains bits 15 to 8 of the 32-bit timestamp counter. The counter has a resolution of 1/32MHz. For a
       consistent counter value the registers BBCn_CNT0...3 have to be read by a SPI block access.
       Bit               7           6            5          4           3            2            1             0
                                                                 CNT1                                                         BBCn_CNT1
       Read/Write        R           R           R           R           R            R            R            R
       Initial Value     0           0            0          0           0            0            0             0

        Bit 7:0 – CNT1.CNT1: Counter Byte 1
6.18.2.4 BBCn_CNT2 – Counter Byte 2
       This register contains bits 23 to 16 of the 32-bit timestamp counter. The counter has a resolution of 1/32MHz. For a
       consistent counter value the registers BBCn_CNT0...3 have to be read by a SPI block access.
       Bit               7           6            5          4           3            2            1             0
                                                                 CNT2                                                         BBCn_CNT2
       Read/Write        R           R           R           R           R            R            R            R
       Initial Value     0           0            0          0           0            0            0             0

        Bit 7:0 – CNT2.CNT2: Counter Byte 2
6.18.2.5 BBCn_CNT3 – Counter Byte 3
       This register contains bits 31 to 24 of the 32-bit timestamp counter. The counter has a resolution of 1/32MHz. For a
       consistent counter value the registers BBCn_CNT0...3 have to be read by a SPI block access.
       Bit               7           6            5          4           3            2            1             0
                                                                 CNT3                                                         BBCn_CNT3
       Read/Write        R           R           R           R           R            R            R            R
       Initial Value     0           0            0          0           0            0            0             0

        Bit 7:0 – CNT3.CNT3: Counter Byte 3




                                                                                          Atmel AT86RF215 - DATASHEET                     168
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| EN | 0x0 | The counter is disabled and reset to zero. |
|  | 0x1 | The counter is enabled and running. |


<!-- page 169 -->

7.    Transceiver Usage
      The following sections provide a reference about how to configure and control the AT86RF215 for transmit and receive
      procedures.


7.1   Transceiver Usage in Baseband Mode
      In order to transmit or receive a frame using the AT86RF215 in baseband mode (see section "Operating Modes" on
      page 30), the radio and the baseband needs to be configured according to the following items:
           Channel configuration
            PLL and channel configuration are described in section "Frequency Synthesizer (PLL)" on page 62.
           Frontend configuration
            The transmitter frontend is described in section "Transmitter Frontend" on page 43 and the receiver frontend is
            described in section "Receiver Frontend" on page 52.
           Energy measurement and AGC configuration
            The energy measurement and AGC configuration are described in section "Energy Measurement" on page 56
            and "Automatic Gain Control (AGC)" on page 53 respectively.
           Baseband configuration
            The general baseband configuration is described in section "Baseband Core" on page 81.
           State control
            The state machine and the state control are described in section "State Machine" on page 33.
           Interrupt handling
            The interrupt handling is described in section "Interrupts" on page 38.
           MAC support (only required if auto mode is used)
            Automatic procedures support IEEE MAC-based operations and can reduced the MCU load. The embedded
            functionality of the MAC support is described in section "IEEE MAC Support" on page 141.




                                                                                Atmel AT86RF215 - DATASHEET                      169
                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 170 -->

7.2     Example: Transceiver Usage in Baseband Mode
        This section describes the required steps for transmit and receive in the baseband mode exemplarily.
        The transceiver can be operated with or without the support of the embedded MAC functionality. The operation without
        the embedded MAC functionality is called basic mode and using the support of the embedded MAC functionality is
        called auto mode.
        The basic mode allows and requires controlling of every operation step of the transceiver and its timing.
        The auto mode aims at MAC protocol operations with respect to [1]. It uses certain MAC protocol functionality from the
        baseband modules. By doing so, it can reduce time-critical frame handling such as acknowledgement transmission from
        the MCU. The features of the auto mode and their control are described in section "IEEE MAC Support" on page 141.
        In section 7.2.1 the common configuration required for transmit and receive is described. Using the basic mode, the
        section "Example Transmit Procedure Using Basic Mode" on page 172 focuses on the transmit procedure while section
        "Example Receive Procedure Using Basic Mode" on page 173 focuses on the receive procedure. In a similar manner
        the transmit and receive procedures with the support of the auto mode are described in section "Example Transmit
        Procedure Using Auto Mode" on page 174 and respectively in section "Example Receive Procedure Using Auto Mode"
        on page 176.
        The sub-1GHz transceiver is used in the following description. Therefore the generic prefixes have to be replaced by
        the actual ones. That means, ”RFn” needs to replaced by “RF09” and “BBCn” needs to be replaced by “BBC0”.
        The example configuration uses the 915MHz band (channel 3) and MR-OFDM Option 1 with MCS level 3 at 800kb/s.
        For further information see section "MR-OFDM PHY" on page 112. If a different modulation scheme such as O-QPSK is
        desired, the section "O-QPSK PHY" on page 120 provides corresponding information.
        For the following steps it is assumed that the entire device has gone through a reset procedure, such as Power-on
        Reset or Chip Reset, and has entered in the State TRXOFF. During the power-on or reset procedure all registers are
        set to their default values.
        In this walkthrough, the 2.4GHz transceiver is not used and therefore stays in state TRXOFF.

7.2.1   Common Configuration
        Control and Data Interfaces
        In this configuration walkthrough, the control and data interfaces ("Control and Data Interfaces" on page 13) are used
        with their default values.
        Interrupt Configuration
        For the example configuration the used interrupts (for baseband mode) are enabled by writing the value 0x1F to the
        registers RFn_IRQM and BBCn_IRQM. For more information about interrupt configuration and handling see sections
        "Interrupt Signalling" on page 19 and "Interrupts" on page 38.
        Channel Configuration
        The channel center frequency f0 for OFDM Option 1 operated in the 915MHz frequency band is 903.2MHz, see [3]
        Table 68d. The channel center frequency f0 needs to be set in the registers RFn_CCF0L and RFn_CCF0H. Due to the
        resolution (i.e. 25kHz) of both registers, the register setting CCF0 is calculated as following:
        CCF0 = f0 / 25kHz; here: CCF0 = 903.2MHz / 25kHz = 0x8D20.
        The low byte of CCF0 needs to be written to RFn_CCF0L while the high byte is written to RFn_CCF0H.
        The channel spacing for OFDM Option 1 operated in the 915MHz frequency band is 1.2MHz, see [3] Table 68d. The
        value 1.2MHz is encoded for the register RFn_CS to the value 0x30.




                                                                                    Atmel AT86RF215 - DATASHEET                      170
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 171 -->

The presented procedure uses channel 3 in the IEEE-compliant channel scheme. Therefore the value 0x03 is written
first to register RFn_CNL and then the value 0x00 is written to register RFn_CNM to trigger the channel setting update.
The described configuration leads to the channel frequency of 906.8MHz.
Frontend Configuration
The transmitter and receiver frontends need to be configured to support OFDM Option 1. According to table
"Recommended Transmitter Frontend Configuration" on page 113 and table "Recommended PHY Receiver and Digital
Frontend Configuration" on page 115 , the following sub-registers are set as follows:
     TXDFE.SR and RXDFE.SR are set to 3,
     TXDFE.RCUT and RXDFE.RCUT are set to 4,
     TXCUTC.LPFCUT is set to 0xB and
     RXBWC.BW is set to 9.
The sub-registers TXCUTC.PARAMP and RXBWC.IFS are kept to their default values of 0.
The maximum transmit power is limited for OFDM due to its signal characteristics, see section "MR-OFDM PHY" on
page 112 and sub-register PAC.TXPWR. The sub-register PAC.TXPWR is set to 0x1C.
Energy Measurement and AGC Configuration
The reset values for the AGC configuration are already suitable for ODFM Option 1; the sub-register AGCC.AVGS and
AGCC.AGCI are kept to 0 and the sub-register AGCS.TGT is kept to 3.
For CCA measurement the energy detection average duration is set to 960µs. This is equal to 8 symbols with a symbol
duration of 120µs, see [3] Table 70 and section 18.2. This measurement duration is set by writing the value 0x7A to the
register RFn_EDD.
Modulation Configuration
To make use of the MR-OFDM modulation, the PHY type needs to be configured; set the sub-register PC.PT to 2 (MR-
OFDM). For this example all other sub-registers of register BBCn_PC are not changed. The OFDM modulation is
configured to use option 1 and the data rate of 800kb/s. After reset, the OFDM option 1 is set as the default value in the
sub-register OFDMC.OPT. The data rate is configured by the sub-register OFDMPHRRX.MCS. The desired data rate is
achieved by setting sub-register OFDMPHRTX.MCS to 3.
Configuration Summary
The Table 7-1 shows all registers and their values that are changed (in comparison to their reset value) for this example
configuration:

Table 7-1.   Example Register Configuration

Register                           Value             Register                             Value

RF09_IRQM, 0x100                   0x1F              BBC0_IRQM, 0x300                     0x1F

RF09_CS, 0x104                     0x30              BBC0_PC, 0x301                       0x56

RF09_CCF0L, 0x105                  0x20              BBC0_OFDMPHRTX, 0x30C                0x03

RF09_CCF0H, 0x106                  0x8D

RF09_CNL, 0x107, Note 1            0x03

RF09_RXBWC, 0x109                  0x09

RF09_RXDFE, 0x10A                  0x83




                                                                            Atmel AT86RF215 - DATASHEET                      171
                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 172 -->

        Register                                 Value            Register                                 Value

        RF09_EDD, 0x10F                          0x7A

        RF09_RNDV, 0x111                         Note 2

        RF09_TXCUTC, 0x112                       0x0B

        RF09_TXDFE, 0x113                        0x83

        RF09_PAC, 0x114                          0x7C

        Note:     1.   To trigger the channel setting update, the value 0x00 is written to register RFn_CNM even if this value is
                       not changed.
                  2.   This register content varies. For further information see section "Random Number Generator" on page 161.

7.2.2   Example Transmit Procedure Using Basic Mode
        Before a frame is transmitted, the channel is usually checked for any other ongoing transmission. This is done in the
        context of a CSMA procedure. This section omits the CSMA backoff procedure and directly measures the channel’s
        energy to determine if the channel is idle or not. If a frame should be transmitted without any CSMA procedure, the
        following step can be skipped.
        Clear Channel Assessment (CCA)
        The CCA sequence uses the energy measurement feature, see section "Energy Measurement" on page 56. Figure 7-1
        shows the procedure of the CCA sequence. Note, the figure does not represent the absolute time scale.

        Figure 7-1. CCA Sequence



        State              TRXOFF   TRANSITION    TXPREP                 RX                     TXPREP     TRXOFF



        Instruction          CMD=TXPREP          BBEN=0 CMD=RX   EDM=1                  CMD=TXPREP CMD=TRXOFF       Read EDV
                                                                                          BBEN=1


        IRQ
                                            TRXRDY                                    EDC   TRXRDY

        Time
                                                                              960µs




        To avoid any frame decoding or detection during the energy measurement, the baseband is disabled by setting
        PC.BBEN to 0. From state TRXOFF that is reached after completion of the reset or power-on procedure, the command
        TXPREP is written to the register RFn_CMD. The command TXPREP causes the radio to set the desired frequency and
        to power-on AVDD. Once this is completed, the state TXPREP is reached and the interrupt IRQS.TRXRDY is issued.
        From the state TXPREP the command RX is written to the register RFn_CMD to reach state RX. The energy
        measurement is triggered by setting EDC.EDM to 1.
        The measurement completion is indicated by interrupt IRQS.EDC. To reduce the power consumption and to prepare the
        next steps, the transceiver is set to the state TXPREP by writing the command TXPREP to the register RFn_CMD. The
        baseband is enabled again by setting PC.BBEN to 1. Once the transceiver reaches the state TXPREP, the interrupt
        IRQS.TRXRDY is issued. To reach state TRXOFF, the command TRXOFF is written to the register RFn_CMD.
        The result of the energy measurement is read from the register RFn_EDV.




                                                                                              Atmel AT86RF215 - DATASHEET                     172
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 173 -->

        Frame Transmission
        Before the frame can be transmitted, the frame length needs to be written to the registers BBCn_TXFLL and
        BBCn_TXFLH. The length value includes the FCS octets that are automatically appended to the frame contents as part
        of the PSDU. In this example the FCS type is kept to its default value, see PC.FCST.
        There are two options to handle the frame download and transmit start sequence. Either the transmission is triggered
        first and afterwards the frame content is provided to the TX frame buffer or the frame content is provided first and frame
        transmission is triggered afterwards. The first approach leads to an earlier transmission over-the-air, but may cause a
        buffer under-run issue. For further information see section "Frame Buffer" on page 132. In Figure 7-2 the frame
        transmission sequence using the second approach is shown.

        Figure 7-2. Frame Transmit Sequence



        RF signal


        State             TRXOFF                               TRANSITION   TXPREP       TX                      TXPREP


                       Set TX   Frame download via SPI,
        Instruction    length   begin writing at          CMD=TXPREP            CMD=TX
                                BBC0_FBTXS


        IRQ
                                                                       TRXRDY                                  TXFE




        After the frame length has been set, the frame content is written to the TX frame buffer. It is not required to write the
        FCS octets to the frame buffer. The FCS octets are appended during transmission automatically if enabled by the sub-
        register PC.TXAFCS.
        Frame transmission can only be triggered from the state TXPREP. The state TXPREP is reached from the state
        TRXOFF by writing the command TXPREP to the register RFn_CMD. Once the state TXPREP is reached, the interrupt
        TRXRDY is issued. From state TXPREP the transmission is triggered by writing the command TX to the register
        RFn_CMD.
        The baseband starts the transmission with PA up-ramping, sending the corresponding frame preamble and PHY
        header. After the transmission of the preamble and the PHY header, the TX frame buffer content is transmitted.
        If the transmission of the frame content including FCS and PA down-ramping is completed, the interrupt IRQS.TXFE is
        issued and the state is automatically changed to TXPREP.

7.2.3   Example Receive Procedure Using Basic Mode
        After the example configuration (see section 7.2 on page 170) is completed, the transceiver is switched to state RX by
        writing the command RX to the register RFn_CMD. Now the receiver is able to receive a frame. The frame reception
        sequence is shown by Figure 7-3.




                                                                                              Atmel AT86RF215 - DATASHEET                     173
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 174 -->

        Figure 7-3. Frame Receive Sequence



        RF signal


        State            TRXOFF   TRANSITION                        RX                      TXPREP

                                                                                                                Read frame length
                                                                                                                Upload frame content
        Instruction          CMD=RX                                                                             Read EDV



        IRQ
                                               AGCH   RXFS   RXAM                         RXFE,
                                                                                          AGCR




        If the baseband core detects a preamble, it holds the AGC automatically. If a valid frame header is decoded by the
        OFDM unit, the interrupt IRQS.RXFS is issued.
        (The interrupt IRQS.RXAM is triggered, if the frame filter is configured and enabled and the received frame matches the
        corresponding settings. For further information see section "Frame Filter" on page 141. The presented example
        configuration does not use the frame filter.)
        The end of the frame reception is indicated by the interrupt IRQS.RXFE. It is issued, if the FCS validation is correct.
        With the interrupt IRQS.RXFE, the state is automatically changed from RX to TXPREP. If the frame is not received
        completely or the FCS validation is not correct, the transceiver stays in state RX to receive the next frame and the AGC
        is released.
        The length of the received frame can be read from the registers BBCn_RXFLL and BBCn_RXFLH. With the length
        information the frame can be read from the frame buffer starting at register BBCn_FBRXS. If the energy of the received
        frame is of interest, it can be read from the register RFn_EDV. The energy measurement has been automatically
        triggered by the baseband core with the interrupt IRQS.RXFS.

7.2.4   Example Transmit Procedure Using Auto Mode
        The following paragraphs explain how to use the auto mode for implementing the transmit procedure described in
        section 7.2.2 on page 172. Using the automatic CCATX feature combines CCA and frame transmission, thus reducing
        microcontroller to transceiver interaction. The CCATX feature performs the energy measurement for the CCA procedure
        automatically, compares the measured value to the configured threshold and triggers transmission if the channel is idle.
        The details of the CCATX procedure are available in section "Clear Channel Assessment with Automatic Transmit
        (CCATX)" on page 148.
        Figure 7-4 shows the CCA sequence followed by the frame transmission. Note, the figure does not represent the
        absolute time scale.




                                                                                    Atmel AT86RF215 - DATASHEET                        174
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

|  |  |
| --- | --- |
| R A | XFE, GCR |


<!-- page 175 -->

Figure 7-4. CCA and Frame Transmit Sequence using Auto Mode

RF signal


State           TRXOFF       TRANSITION    TXPREP                RX                TXPREP         TX            TXPREP


                                                                Set TX length,
Instruction   AMEDT=0xAC   CMD=TXPREP            CMD=RX   EDM=1 download                                       Read
              CCATX=1                                           frame via SPI,                                 CCAED
              BBEN=0                                            begin writing at
                                                                BBC0_FBTXS
IRQ
                                        TRXRDY                                     EDC,                       TXFE
                                                                                   TRXRDY
Time
                                                                      960µs




In state TRXOFF that is reached after completion of the reset or power-on procedure, the transceiver gets configured as
described in section "Common Configuration" on page 170. The power-on procedure and the common configuration is
not shown in Figure 7-4.
In the same way as in the basic mode, the CCA duration and measurement mode are configured as described in
section "Energy Measurement" on page 56. Besides that, the CCATX procedure requires to setup the energy threshold
determining which energy level is assessed as idle or busy. The energy threshold value for the example (OFDM option
1, MCS 3) is -84dBm (see [1]). This value is configured by writing the value 0xAC to register BBCn_AMEDT.
The automatic CCATX procedure is enabled by setting the bit AMCS.CCATX to 1. To avoid unwanted conflicts with
other automatic procedures, it is recommend disabling procedures such as automatic acknowledgment transmission
and transmit and switch to receive by setting AMCS.AACK to 0 and AMCS.TX2RX to 0, respectively while CCATX is in
use. To avoid any frame decoding or detection during the energy measurement, the baseband cores are disabled by
setting PC.BBEN to 0.
From state TRXOFF the command TXPREP is written to the register RFn_CMD. The command TXPREP causes the
radio to set the desired frequency and to power-on AVDD. Once this is completed, the state TXPREP is reached and
the interrupt IRQS.TRXRDY is issued.
From the state TXPREP the command RX is written to the register RFn_CMD to reach state RX. The energy
measurement is triggered by setting EDC.EDM to 1.
Before the frame can be transmitted, the frame length needs to be written to the registers BBCn_TXFLL and
BBCn_TXFLH. The length value includes the FCS octets that are appended to the frame contents automatically as part
of the PSDU. In this example the FCS type is kept to its default value, see PC.FCST.
There are several options when to download the frame to the frame buffer. It can be downloaded either before the entire
CCATX procedure, during the CCA measurement period or during the preamble transmission. It needs be ensured that
the frame content is available to the baseband for actual transmission to avoid a buffer under-run issue. For further
information about the buffer under-run issue see section "Frame Buffer" on page 132. In this example, the frame
content is downloaded to the frame buffer during the energy measurement period.
The energy measurement completion is indicated by the interrupt IRQS.EDC. If the measured energy value is below the
threshold value set in the register BBCn_AMEDT, the CCATX procedure continues and switches to the state TX. Since
switching from state RX to state TX transits the state TXPREP, the interrupt TRXRDY is issued. With the interrupt
IRQS.EDC the status bit AMCS.CCAED is updated. It provides the status of the comparison between measured and
configured energy threshold. The value of the energy measurement can be read from register RFn_EDV.
If the measured energy is above the configured threshold, the state is not switched automatically to TX. It stays in state
RX instead. Figure 6-35 on page 149 shows a busy channel scenario. If further frame reception is requested, the
baseband needs to be enabled again by setting PC.BBEN to 1.



                                                                                            Atmel AT86RF215 - DATASHEET                     175
                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 176 -->

        In state TX the frame is transmitted from the frame buffer. For the frame transmission the baseband is enabled again
        automatically. The baseband starts the transmission with PA up-ramping, sending the corresponding frame preamble
        and PHY header. After the transmission of the preamble and the PHY header, the TX frame buffer content is
        transmitted.
        If the transmission of the frame content including FCS and PA down-ramping is completed, the interrupt IRQS.TXFE is
        issued and the state is changed to TXPREP automatically. Since the interrupt TXFE is always issued at the end of the
        CCATX procedure, the status bit AMCS.CCAED provides information about the actual transmission. If the bit indicates
        that the channel has been assessed as idle, the frame transmission has been executed automatically during the
        CCATX procedure. If the bit indicates a busy channel, the CCATX procedure has not started the frame transmission
        after the energy measurement period. Further steps of the CSMA algorithm such as backoff and CCA retry need to be
        controlled by the MCU.

7.2.5   Example Receive Procedure Using Auto Mode
        The following section describes the receive procedure including acknowledgment frame transmission with the support of
        the auto mode. The automatic acknowledgement transmission features (AACK) uses the frame filter module to
        determine if an acknowledgement frame needs to be transmitted. The duration between the end of the frame reception
        and the ACK frame transmission is configured by registers BBCn_AMAACKTL and BBCn_AMAACKTH. The frame filter
        configuration is described in section "Frame Filter" on page 141. The details of the AACK procedure are available in
        section "Automatic Acknowledgement (AACK)" on page 146 .
        After the example configuration (see section 7.2 on page 170), the above mentioned configuration for the AACK feature
        and the frame filter setup are completed, the transceiver is switched to state RX by writing the command RX to the
        register RFn_CMD. Now the receiver is able to receive a frame. The frame reception sequence including ACK
        transmission is shown in Figure 7-5. Note, the figure does not represent the absolute time scale.

        Figure 7-5. Frame Receive Sequence with Automatic Acknowledgment Transmission



        RF signal                                                              RX                          TX



        State                      TRXOFF    TRANSITION                             RX       TXPREP        TX      TXPREP



        Instruction   AMAACKTL/H=1080µs     CMD=RX                                                                          Read frame length
                      AACK=1                                                                                                Upload frame content
                      Frame filter config                                                                                   Read EDV

        IRQ
                                                          AGCH   RXFS   RXAM              RXFE,                 TXFE
                                                                                          AGCR
        Time
                                                                                              1080µs




        If the baseband core detects a preamble, it holds the AGC automatically. If a valid frame header is decoded by the
        OFDM module, the interrupt IRQS.RXFS is issued. The interrupt IRQS.RXAM is triggered if the frame filter detects a
        matching address in the received frame.
        The end of the frame reception is indicated by the interrupt IRQS.RXFE. It is issued if the FCS validation is correct. With
        the interrupt IRQS.RXFE, the state changes from RX to TXPREP automatically. If the frame is not received completely
        or the FCS validation is not correct, the transceiver stays in state RX to receive the next frame and the AGC is released.




                                                                                         Atmel AT86RF215 - DATASHEET                          176
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

|  |  |
| --- | --- |
| A | GCH |


<!-- page 177 -->

The frame filter and the AACK module determine that an ACK transmission is required and start a timer to trigger the
ACK transmission. The timer duration between the end of frame reception and the start of ACK transmission is read
from the registers BBCn_AMAACKTL and BBCn_AMAACKTH. The AACK module creates the ACK frame automatically
and transmits it at the configured time after the interrupt RXFE. At the end of the ACK transmission the interrupt TXFE
is issued and the state TXPREP is entered.
After the interrupt RXFE the length of the received frame can be read from the registers BBCn_RXFLL and
BBCn_RXFLH. With the length information the frame can be read from the frame buffer starting at register
BBCn_FBRXS. If the energy of the received frame is of interest, it can be read from the register RFn_EDV. The energy
measurement has been triggered automatically by the baseband core by the interrupt IRQS.RXFS.




                                                                           Atmel AT86RF215 - DATASHEET                     177
                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 178 -->

7.3   Transmitter Usage in I/Q Radio Mode
      This section explains how to configure the AT86RF215 for transmission in I/Q radio mode. It is assumed, that the radio
      has been reset before and is in State TRXOFF. All interrupts in register RFn_IRQS should be enabled. Following steps
      shall be performed:
           Enable I/Q radio mode by setting sub-register IQIFC1.CHPM=1 at AT86RF215. For further description of chip
            modes, see section "Operating Modes" on page 30. The I/Q radio mode is set by default at AT86RF215IQ.
           Configure the Transmitter Frontend:
                 Set the transmitter analog frontend sub-registers TXCUTC.LPFCUT and TXCUTC.PARAMP, see section
                  "Transmitter Analog Frontend" on page 44.
                 Set the transmitter digital frontend sub-registers TXDFE.SR and TXDFE.RCUT, see section "Transmitter
                  Digital Frontend" on page 43
           Configure the channel parameters, see section "Channel Configuration" on page 62 and transmit power, see
            section "Power Amplifier" on page 45.
           Optional: Perform ED measurement, see section "Energy Measurement" on page 56. The following steps are
            recommended:
                 Configure the measurement period, see register RFn_EDD.
                 Switch to State RX.
                 Start and finish a measurement:
                     For single and continuous ED modes a measurement starts if the mode is written to sub-register
                         EDC.EDM. The completion of the measurement is indicated by the interrupt IRQS.EDC. The
                         resulting ED value can be read from register RFn_EDV.
                     For the automatic mode, a measurement starts by setting bit AGCC.FRZC=1. After the completion of
                         the measurement period, the ED value can be read from register RFn_EDV.
           Switch to State TXPREP; interrupt IRQS.TRXRDY is issued.
           To start the actual transmission, there are two possibilities, depending on the setting of sub-register
            IQIFC0.EEC:
                 IQIFC0.EEC=0: Provide I/Q samples on the "Serial I/Q Data Interface". Enable the radio transmitter by
                  writing command TX to the register RFn_CMD via SPI. Be aware of the critical time alignment between
                  providing I/Q samples and enabling the radio transmitter, see section "Transmit Control" on page 46.
                  Make sure to pre-pend zero samples to the I/Q samples for proper PA ramp-up.
                 IQIFC0.EEC=1: Provide I/Q samples on the "Serial I/Q Data Interface". The transmitter is activated
                  automatically with the TX start signal embedded in I_DATA[0], see Figure 6-4 on page 47. Provided SPI
                  commands such as TX and TXPREP are ignored.
           To finish a transmission depends on the setting of bit IQIFC0.EEC:
                 IQIFC0.EEC=0: To leave the State TX, write command TXPREP to the register RFn_CMD. Reaching
                  State TXPREP is indicated by the interrupt IRQS.TRXRDY. Make sure to append enough padding
                  samples to the I/Q samples to provide data until the PA is ramped-down, see section "Transmit Control"
                  on page 46.
                 IQIFC0.EEC=1: If the bit I_DATA[0] is set to 0 (see Figure 6-4 on page 47) the ramp down process of
                  the PA is started automatically. After ramp down the transmitter switches back to State TXPREP.
                  Padding samples are required to avoid spurious emission during PA ramp-down.
      An example transmission for IQIFC0.EEC=1 is shown in Figure 7-6. As shown, no external SPI command is needed to
      control the transmission; provided SPI commands such as TXPREP are ignored if IQIFC0.EEC=1. The zero samples
      have to be pre-pended at least ttx_start_delay before the actual I/Q samples start. The duration of the padding shall
      correspond to the PA down-ramp time.




                                                                                 Atmel AT86RF215 - DATASHEET                      178
                                                                                   Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 179 -->

Figure 7-6. Transmit sequence in I/Q Radio Mode for IQIFC0.EEC=1



                         ttx_proc_delay      ttx_start_delay   tpa_ramp           ttx_proc_delay   tpa_ramp


RF signal


I_DATA[0]
                           ttx_start_delay                                                 tpa_ramp

I/Q Interface            Zero Samples                               I/Q Samples             Padding



State           TXPREP                                                      TX                                TXPREP




                                                                                      Atmel AT86RF215 - DATASHEET                       179
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 180 -->

7.4   Receiver Usage in I/Q Radio Mode
      This section explains how to configure the AT86RF215 for reception of data in I/Q radio mode. It is assumed, that the
      radio has been reset before and is in State TRXOFF. All interrupts in register RFn_IRQS should be enabled
      (RFn_IRQM=0x3f). In order to use the receiver in I/Q radio mode the following steps shall be performed:
             Enable I/Q radio mode by setting sub-register IQIFC1.CHPM=1. For further description of chip modes, see
              section "Operating Modes" on page 30. For AT86RF215IQ the I/Q radio mode is set by default.
             Configure the Receiver Frontend:
                     Set the receiver analog frontend sub-registers RXBWC.BW and RXBWC.IFS, see section "Receiver
                      Analog Frontend" on page 52.
                     Set the receiver digital frontend sub-registers RXDFE.SR and RXDFE.RCUT, see section "Receiver
                      Digital Frontend" on page 53.
                     Set the AGC registers RFn_AGCC and RFn_AGCS, see section "Automatic Gain Control (AGC)" on
                      page 53.
             Configure the channel, see section "Channel Configuration" on page 62.
             Switch to State TXPREP; interrupt IRQS.TRXRDY is issued. TXD and TXCLK are activated as shown in
              Figure 4-12 on page 26.
             Prepare the external baseband for reception of I/Q samples, see section "Serial I/Q Data Interface" on page 22
              then enable the radio receiver by writing command RX to the register RFn_CMD. To prevent the AGC from
              switching its gain during reception, it is recommended to set AGCC.FRZC=1 after reception of the preamble,
              see section 0 on page 54. Accordingly, the AGC has to be released after finishing reception by setting
              AGCC.FRZC=0.
      Now, continuous I/Q samples are provided at the I/Q data interface.
      The receive state can be stopped at any time by writing command TXPREP to the register RFn_CMD. A successful
      state transition to TXPREP is indicated by the interrupt IRQS.TRXRDY.
      The receive procedure is exemplary shown in Figure 7-7.

      Figure 7-7. Receive Sequence in I/Q Radio Mode


      RF signal


      I/Q Interface                                       I/Q Samples




      State           TRXOFF   TRANSITION                 RX                            TXPREP




      Instruction        CMD=RX             AGCC.FRZC=1                         CMD=TXPREP    AGCC.FRZC=0



      IRQ
                                                                                     TRXRDY




                                                                                 Atmel AT86RF215 - DATASHEET                     180
                                                                                  Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 181 -->

8.       Register Summary
         All registers not mentioned within the following table are reserved for internal use and must not be overwritten. When
         writing to a register, any reserved bits shall be overwritten only with their reset value.
Addr        Name          Bit 7             Bit 6            Bit 5            Bit 4            Bit 3             Bit 2             Bit 1             Bit 0    Page
0x0000    RF09_IRQS         –                 –              IQIFSF          TRXERR           BATLOW             EDC             TRXRDY            WAKEUP       40
0x0001    RF24_IRQS         –                 –              IQIFSF          TRXERR           BATLOW             EDC             TRXRDY            WAKEUP       40
0x0002    BBC0_IRQS        FBLI             AGCR             AGCH             TXFE             RXEM             RXAM              RXFE               RXFS       41
0x0003    BBC1_IRQS        FBLI             AGCR             AGCH             TXFE             RXEM             RXAM              RXFE               RXFS       41
0x0005     RF_RST           –                 –                –                –                –                                 CMD                          14
0x0006     RF_CFG           –                 –                –                –             IRQMM              IRQP                        DRV              19, 41
0x0007    RF_CLKO           –                 –                –                      DRV                                          OS                           20
0x0008    RF_BMDVC          –                 –              BMS             BMHR                                        BMVTH                                  78
0x0009     RF_XOC           –                 –                –               FS                                         TRIM                                  69
0x000A    RF_IQIFC0       EXTLB              SF                       DRV                               CMV                       CMV1V2             EEC      27, 50
0x000B    RF_IQIFC1       FAILSF                             CHPM                                –                 –                       SKEWDRV            28, 32
0x000C    RF_IQIFC2       SYNC                –                –                –                –                 –                 –                 –        29
0x000D     RF_PN                                                                       PN

0x000E     RF_VN                                                                       VN
0x0100    RF09_IRQM         –                 –              IQIFSF          TRXERR           BATLOW             EDC             TRXRDY            WAKEUP       39
0x0101    RF09_AUXS     EXTLNABYP                   AGCMAP                   AVEXT             AVEN              AVS                        PAVC             50, 72, 76
0x0102   RF09_STATE         –                 –                –                –                –                                STATE                         36
0x0103    RF09_CMD          –                 –                –                –                –                                 CMD                          37
0x0104     RF09_CS                                                                     CS                                                                       64
0x0105   RF09_CCF0L                                                                   CCF0L                                                                     64
0x0106   RF09_CCF0H                                                                   CCF0H                                                                     65
0x0107    RF09_CNL                                                                    CNL                                                                       65
0x0108    RF09_CNM                  CM                         –                –                –                 –                 –               CNH        65
0x0109   RF09_RXBWC         –                 –               IFI             IFS                                         BW                                    57
0x010A   RF09_RXDFE                         RCUT                                –                                         SR                                    58
0x010B   RF09_AGCC          –               AGCI                      AVGS                     RST               FRZS             FRZC                EN        59
0x010C    RF09_AGCS                         TGT                                                                  GCW                                            60
0x010D    RF09_RSSI                                                                   RSSI                                                                      60
0x010E    RF09_EDC          –                 –                –                –                –                 –                        EDM                 60
0x010F    RF09_EDD                                                     DF                                                                    DTB                61
0x0110    RF09_EDV                                                                    EDV                                                                       61
0x0111    RF09_RNDV                                                                   RNDV                                                                      161
0x0112   RF09_TXCUTC               PARAMP                      –                –                                        LPFCUT                                 48
                                                                                                                                                             48, 109,
0x0113   RF09_TXDFE                         RCUT                              DM                                          SR
                                                                                                                                                               131
0x0114    RF09_PAC          –                       PACUR                                                       TXPWR                                           49
0x0116   RF09_PADFE                PADFE                       –                –                –                 –                 –                 –        73
0x0121    RF09_PLL          –                 –                       LBW                        –                 –                LS                 –        65
0x0122   RF09_PLLCF         –                 –                                                          CF                                                     66
0x0125    RF09_TXCI         –                 –                                                         DCOI                                                    225
0x0126    RF09_TXCQ         –                 –                                                         DCOQ                                                    226
0x0127   RF09_TXDACI    ENTXDACID                                                             TXDACID                                                           223
0x0128   RF09_TXDACQ   ENTXDACQD                                                             TXDACQD                                                            223
0x0200    RF24_IRQM         –                 –              IQIFSF          TRXERR           BATLOW             EDC             TRXRDY            WAKEUP       39
0x0201    RF24_AUXS     EXTLNABYP                   AGCMAP                   AVEXT             AVEN              AVS                        PAVC             50, 72, 76
0x0202   RF24_STATE         –                 –                –                –                –                                STATE                         36
0x0203    RF24_CMD          –                 –                –                –                –                                 CMD                          37
0x0204     RF24_CS                                                                     CS                                                                       64
0x0205   RF24_CCF0L                                                                   CCF0L                                                                     64




                                                                                                          Atmel AT86RF215 - DATASHEET                             181
                                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Addr | Name | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Page |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x0000 | RF09_IRQS | – | – | IQIFSF | TRXERR | BATLOW | EDC | TRXRDY | WAKEUP | 40 |
| 0x0001 | RF24_IRQS | – | – | IQIFSF | TRXERR | BATLOW | EDC | TRXRDY | WAKEUP | 40 |
| 0x0002 | BBC0_IRQS | FBLI | AGCR | AGCH | TXFE | RXEM | RXAM | RXFE | RXFS | 41 |
| 0x0003 | BBC1_IRQS | FBLI | AGCR | AGCH | TXFE | RXEM | RXAM | RXFE | RXFS | 41 |
| 0x0005 | RF_RST | – | – | – | – | – | CMD |  |  | 14 |
| 0x0006 | RF_CFG | – | – | – | – | IRQMM | IRQP | DRV |  | 19, 41 |
| 0x0007 | RF_CLKO | – | – | – | DRV |  | OS |  |  | 20 |
| 0x0008 | RF_BMDVC | – | – | BMS | BMHR | BMVTH |  |  |  | 78 |
| 0x0009 | RF_XOC | – | – | – | FS | TRIM |  |  |  | 69 |
| 0x000A | RF_IQIFC0 | EXTLB | SF | DRV |  | CMV |  | CMV1V2 | EEC | 27, 50 |
| 0x000B | RF_IQIFC1 | FAILSF | CHPM |  |  | – | – | SKEWDRV |  | 28, 32 |
| 0x000C | RF_IQIFC2 | SYNC | – | – | – | – | – | – | – | 29 |
| 0x000D | RF_PN | PN |  |  |  |  |  |  |  |  |
| 0x000E | RF_VN | VN |  |  |  |  |  |  |  |  |
| 0x0100 | RF09_IRQM | – | – | IQIFSF | TRXERR | BATLOW | EDC | TRXRDY | WAKEUP | 39 |
| 0x0101 | RF09_AUXS | EXTLNABYP | AGCMAP |  | AVEXT | AVEN | AVS | PAVC |  | 50, 72, 76 |
| 0x0102 | RF09_STATE | – | – | – | – | – | STATE |  |  | 36 |
| 0x0103 | RF09_CMD | – | – | – | – | – | CMD |  |  | 37 |
| 0x0104 | RF09_CS | CS |  |  |  |  |  |  |  | 64 |
| 0x0105 | RF09_CCF0L | CCF0L |  |  |  |  |  |  |  | 64 |
| 0x0106 | RF09_CCF0H | CCF0H |  |  |  |  |  |  |  | 65 |
| 0x0107 | RF09_CNL | CNL |  |  |  |  |  |  |  | 65 |
| 0x0108 | RF09_CNM | CM |  | – | – | – | – | – | CNH | 65 |
| 0x0109 | RF09_RXBWC | – | – | IFI | IFS | BW |  |  |  | 57 |
| 0x010A | RF09_RXDFE | RCUT |  |  | – | SR |  |  |  | 58 |
| 0x010B | RF09_AGCC | – | AGCI | AVGS |  | RST | FRZS | FRZC | EN | 59 |
| 0x010C | RF09_AGCS | TGT |  |  | GCW |  |  |  |  | 60 |
| 0x010D | RF09_RSSI | RSSI |  |  |  |  |  |  |  | 60 |
| 0x010E | RF09_EDC | – | – | – | – | – | – | EDM |  | 60 |
| 0x010F | RF09_EDD | DF |  |  |  |  |  | DTB |  | 61 |
| 0x0110 | RF09_EDV | EDV |  |  |  |  |  |  |  | 61 |
| 0x0111 | RF09_RNDV | RNDV |  |  |  |  |  |  |  | 161 |
| 0x0112 | RF09_TXCUTC | PARAMP |  | – | – | LPFCUT |  |  |  | 48 |
|  |  |  |  |  |  |  |  |  |  | 48, 109, |
| 0x0113 | RF09_TXDFE | RCUT |  |  | DM | SR |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 131 |
|  |  |  |  |  |  |  |  |  |  |  |
| 0x0114 | RF09_PAC | – | PACUR |  | TXPWR |  |  |  |  | 49 |
| 0x0116 | RF09_PADFE | PADFE |  | – | – | – | – | – | – | 73 |
| 0x0121 | RF09_PLL | – | – | LBW |  | – | – | LS | – | 65 |
| 0x0122 | RF09_PLLCF | – | – | CF |  |  |  |  |  | 66 |
| 0x0125 | RF09_TXCI | – | – | DCOI |  |  |  |  |  | 225 |
| 0x0126 | RF09_TXCQ | – | – | DCOQ |  |  |  |  |  | 226 |
| 0x0127 | RF09_TXDACI | ENTXDACID | TXDACID |  |  |  |  |  |  | 223 |
| 0x0128 | RF09_TXDACQ | ENTXDACQD | TXDACQD |  |  |  |  |  |  | 223 |
| 0x0200 | RF24_IRQM | – | – | IQIFSF | TRXERR | BATLOW | EDC | TRXRDY | WAKEUP | 39 |
| 0x0201 | RF24_AUXS | EXTLNABYP | AGCMAP |  | AVEXT | AVEN | AVS | PAVC |  | 50, 72, 76 |
| 0x0202 | RF24_STATE | – | – | – | – | – | STATE |  |  | 36 |
| 0x0203 | RF24_CMD | – | – | – | – | – | CMD |  |  | 37 |
| 0x0204 | RF24_CS | CS |  |  |  |  |  |  |  | 64 |
| 0x0205 | RF24_CCF0L | CCF0L |  |  |  |  |  |  |  | 64 |


<!-- page 182 -->

Addr         Name          Bit 7            Bit 6           Bit 5           Bit 4             Bit 3             Bit 2            Bit 1           Bit 0      Page
0x0206    RF24_CCF0H                                                                CCF0H                                                                     65
0x0207     RF24_CNL                                                                  CNL                                                                      65
0x0208     RF24_CNM                  CM                       –               –                 –                 –                –             CNH          65
0x0209   RF24_RXBWC          –                –              IFI            IFS                                          BW                                   57
0x020A    RF24_RXDFE                        RCUT                              –                                          SR                                   58
0x020B    RF24_AGCC          –              AGCI                    AVGS                       RST              FRZS             FRZC             EN          59
0x020C    RF24_AGCS                         TGT                                                                 GCW                                           60
0x020D     RF24_RSSI                                                                 RSSI                                                                     60
0x020E     RF24_EDC          –                –               –               –                 –                 –                      EDM                  60
0x020F     RF24_EDD                                                  DF                                                                  DTB                  61
0x0210     RF24_EDV                                                                  EDV                                                                      61
0x0211    RF24_RNDV                                                                 RNDV                                                                      161
0x0212   RF24_TXCUTC               PARAMP                     –               –                                         LPFCUT                                48
                                                                                                                                                            48, 109,
0x0213    RF24_TXDFE                        RCUT                            DM                                           SR
                                                                                                                                                              131
0x0214     RF24_PAC          –                      PACUR                                                      TXPWR                                          49
0x0216    RF24_PADFE               PADFE                      –               –                 –                 –                –               –          73
0x0221     RF24_PLL          –                –                     LBW                         –                 –               LS               –          65
0x0222    RF24_PLLCF         –                –                                                         CF                                                    66
0x0225     RF24_TXCI         –                –                                                        DCOI                                                   225
0x0226    RF24_TXCQ          –                –                                                        DCOQ                                                   226
0x0227    RF24_TXDACI    ENTXDACID                                                           TXDACID                                                          223
0x0228   RF24_TXDACQ     ENTXDACQD                                                           TXDACQD                                                          223
0x0300    BBC0_IRQM        FBLI             AGCR            AGCH            TXFE              RXEM             RXAM              RXFE            RXFS         39
                                                                                                                                                            84, 139,
0x0301     BBC0_PC          CTX             FCSFE           FCSOK          TXAFCS             FCST              BBEN                      PT
                                                                                                                                                              222
0x0302     BBC0_PS           –                –               –               –                 –                 –                –             TXUR         135
0x0304    BBC0_RXFLL                                                                RXFLL                                                                     135
0x0305    BBC0_RXFLH         –                –               –               –                 –                                RXFLH                        135
0x0306    BBC0_TXFLL                                                                TXFLL                                                                     136
0x0307    BBC0_TXFLH         –                –               –               –                 –                                TXFLH                        135
0x0308    BBC0_FBLL                                                                  FBLL                                                                     135
0x0309    BBC0_FBLH          –                –               –               –                 –                                FBLH                         135
0x030A    BBC0_FBLIL                                                                 FBLIL                                                                    136
0x030B    BBC0_FBLIH         –                –               –               –                 –                                FBLIH                        137
0x030C BBC0_OFDMPHRTX      RB21             RB18            RB17            RB5                 –                                MCS                          116
0x030D BBC0_OFDMPHRRX      RB21             RB18            RB17            RB5                SPC                               MCS                          116
0x030E   BBC0_OFDMC                 SSRX                            SSTX                       LFO               POI                     OPT                  117
0x030F   BBC0_OFDMSW                        PDT                             RXO                 –                 –                –               –          118
0x0310   BBC0_OQPSKC0        –                –               –             DM                MOD                 –                      FCHIP                126
0x0311   BBC0_OQPSKC1      RXO             RXOLEG                           PDT1                                                 PDT0                         127
0x0312   BBC0_OQPSKC2        –                –             SPC             RPC              ENPROP           FCSTLEG                    RXM                  127
0x0313   BBC0_OQPSKC3        –                –             HRLEG             –                        NSFD                        –               –          129
0x0314 BBC0_OQPSKPHRTX       –                –             PPDUT           RB0                                 MOD                              LEG          129
0x0315 BBC0_OQPSKPHRRX       –                –             PPDUT           RB0                                 MOD                              LEG          130
0x0320    BBC0_AFC0          –                –               –             PM                AFEN3            AFEN2             AFEN1           AFEN0        149
0x0321    BBC0_AFC1        MRFT3            MRFT2           MRFT1          MRFT0              PANC3            PANC2             PANC1           PANC0        150
0x0322    BBC0_AFFTM                                                                AFFTM                                                                     151
0x0323    BBC0_AFFVM         –                –               –               –                                         AFFVM                                 151
0x0324     BBC0_AFS          –                –               –             EM                 AM3              AM2              AM1             AM0          151
0x0325   BBC0_MACEA0                                                                MACEA0                                                                    152
0x0326   BBC0_MACEA1                                                                MACEA1                                                                    152
0x0327   BBC0_MACEA2                                                                MACEA2                                                                    152
0x0328   BBC0_MACEA3                                                                MACEA3                                                                    152
0x0329   BBC0_MACEA4                                                                MACEA4                                                                    152
0x032A   BBC0_MACEA5                                                                MACEA5                                                                    153
0x032B   BBC0_MACEA6                                                                MACEA6                                                                    153




                                                                                                         Atmel AT86RF215 - DATASHEET                            182
                                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Addr | Name | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Page |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x0206 | RF24_CCF0H | CCF0H |  |  |  |  |  |  |  | 65 |
| 0x0207 | RF24_CNL | CNL |  |  |  |  |  |  |  | 65 |
| 0x0208 | RF24_CNM | CM |  | – | – | – | – | – | CNH | 65 |
| 0x0209 | RF24_RXBWC | – | – | IFI | IFS | BW |  |  |  | 57 |
| 0x020A | RF24_RXDFE | RCUT |  |  | – | SR |  |  |  | 58 |
| 0x020B | RF24_AGCC | – | AGCI | AVGS |  | RST | FRZS | FRZC | EN | 59 |
| 0x020C | RF24_AGCS | TGT |  |  | GCW |  |  |  |  | 60 |
| 0x020D | RF24_RSSI | RSSI |  |  |  |  |  |  |  | 60 |
| 0x020E | RF24_EDC | – | – | – | – | – | – | EDM |  | 60 |
| 0x020F | RF24_EDD | DF |  |  |  |  |  | DTB |  | 61 |
| 0x0210 | RF24_EDV | EDV |  |  |  |  |  |  |  | 61 |
| 0x0211 | RF24_RNDV | RNDV |  |  |  |  |  |  |  | 161 |
| 0x0212 | RF24_TXCUTC | PARAMP |  | – | – | LPFCUT |  |  |  | 48 |
|  |  |  |  |  |  |  |  |  |  | 48, 109, |
| 0x0213 | RF24_TXDFE | RCUT |  |  | DM | SR |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 131 |
|  |  |  |  |  |  |  |  |  |  |  |
| 0x0214 | RF24_PAC | – | PACUR |  | TXPWR |  |  |  |  | 49 |
| 0x0216 | RF24_PADFE | PADFE |  | – | – | – | – | – | – | 73 |
| 0x0221 | RF24_PLL | – | – | LBW |  | – | – | LS | – | 65 |
| 0x0222 | RF24_PLLCF | – | – | CF |  |  |  |  |  | 66 |
| 0x0225 | RF24_TXCI | – | – | DCOI |  |  |  |  |  | 225 |
| 0x0226 | RF24_TXCQ | – | – | DCOQ |  |  |  |  |  | 226 |
| 0x0227 | RF24_TXDACI | ENTXDACID | TXDACID |  |  |  |  |  |  | 223 |
| 0x0228 | RF24_TXDACQ | ENTXDACQD | TXDACQD |  |  |  |  |  |  | 223 |
| 0x0300 | BBC0_IRQM | FBLI | AGCR | AGCH | TXFE | RXEM | RXAM | RXFE | RXFS | 39 |
|  |  |  |  |  |  |  |  |  |  | 84, 139, |
| 0x0301 | BBC0_PC | CTX | FCSFE | FCSOK | TXAFCS | FCST | BBEN | PT |  |  |
|  |  |  |  |  |  |  |  |  |  | 222 |
|  |  |  |  |  |  |  |  |  |  |  |
| 0x0302 | BBC0_PS | – | – | – | – | – | – | – | TXUR | 135 |
| 0x0304 | BBC0_RXFLL | RXFLL |  |  |  |  |  |  |  | 135 |
| 0x0305 | BBC0_RXFLH | – | – | – | – | – | RXFLH |  |  | 135 |
| 0x0306 | BBC0_TXFLL | TXFLL |  |  |  |  |  |  |  | 136 |
| 0x0307 | BBC0_TXFLH | – | – | – | – | – | TXFLH |  |  | 135 |
| 0x0308 | BBC0_FBLL | FBLL |  |  |  |  |  |  |  | 135 |
| 0x0309 | BBC0_FBLH | – | – | – | – | – | FBLH |  |  | 135 |
| 0x030A | BBC0_FBLIL | FBLIL |  |  |  |  |  |  |  | 136 |
| 0x030B | BBC0_FBLIH | – | – | – | – | – | FBLIH |  |  | 137 |
| 0x030C | BBC0_OFDMPHRTX | RB21 | RB18 | RB17 | RB5 | – | MCS |  |  | 116 |
| 0x030D | BBC0_OFDMPHRRX | RB21 | RB18 | RB17 | RB5 | SPC | MCS |  |  | 116 |
| 0x030E | BBC0_OFDMC | SSRX |  | SSTX |  | LFO | POI | OPT |  | 117 |
| 0x030F | BBC0_OFDMSW | PDT |  |  | RXO | – | – | – | – | 118 |
| 0x0310 | BBC0_OQPSKC0 | – | – | – | DM | MOD | – | FCHIP |  | 126 |
| 0x0311 | BBC0_OQPSKC1 | RXO | RXOLEG | PDT1 |  |  | PDT0 |  |  | 127 |
| 0x0312 | BBC0_OQPSKC2 | – | – | SPC | RPC | ENPROP | FCSTLEG | RXM |  | 127 |
| 0x0313 | BBC0_OQPSKC3 | – | – | HRLEG | – | NSFD |  | – | – | 129 |
| 0x0314 | BBC0_OQPSKPHRTX | – | – | PPDUT | RB0 | MOD |  |  | LEG | 129 |
| 0x0315 | BBC0_OQPSKPHRRX | – | – | PPDUT | RB0 | MOD |  |  | LEG | 130 |
| 0x0320 | BBC0_AFC0 | – | – | – | PM | AFEN3 | AFEN2 | AFEN1 | AFEN0 | 149 |
| 0x0321 | BBC0_AFC1 | MRFT3 | MRFT2 | MRFT1 | MRFT0 | PANC3 | PANC2 | PANC1 | PANC0 | 150 |
| 0x0322 | BBC0_AFFTM | AFFTM |  |  |  |  |  |  |  | 151 |
| 0x0323 | BBC0_AFFVM | – | – | – | – | AFFVM |  |  |  | 151 |
| 0x0324 | BBC0_AFS | – | – | – | EM | AM3 | AM2 | AM1 | AM0 | 151 |
| 0x0325 | BBC0_MACEA0 | MACEA0 |  |  |  |  |  |  |  | 152 |
| 0x0326 | BBC0_MACEA1 | MACEA1 |  |  |  |  |  |  |  | 152 |
| 0x0327 | BBC0_MACEA2 | MACEA2 |  |  |  |  |  |  |  | 152 |
| 0x0328 | BBC0_MACEA3 | MACEA3 |  |  |  |  |  |  |  | 152 |
| 0x0329 | BBC0_MACEA4 | MACEA4 |  |  |  |  |  |  |  | 152 |
| 0x032A | BBC0_MACEA5 | MACEA5 |  |  |  |  |  |  |  | 153 |
| 0x032B | BBC0_MACEA6 | MACEA6 |  |  |  |  |  |  |  | 153 |


<!-- page 183 -->

Addr         Name          Bit 7             Bit 6           Bit 5            Bit 4               Bit 3            Bit 2            Bit 1           Bit 0    Page
0x032C    BBC0_MACEA7                                                                  MACEA7                                                                  153
0x032D   BBC0_MACPID0F0                                                               MACPID0F0                                                                153
0x032E   BBC0_MACPID1F0                                                               MACPID1F0                                                                153
0x032F BBC0_MACSHA0F0                                                               MACSHA0F0                                                                  154
0x0330 BBC0_MACSHA1F0                                                               MACSHA1F0                                                                  154
0x0331   BBC0_MACPID0F1                                                               MACPID0F1                                                                154
0x0332   BBC0_MACPID1F1                                                               MACPID1F1                                                                154
0x0333 BBC0_MACSHA0F1                                                               MACSHA0F1                                                                  154
0x0334 BBC0_MACSHA1F1                                                               MACSHA1F1                                                                  155
0x0335   BBC0_MACPID0F2                                                               MACPID0F2                                                                155
0x0336   BBC0_MACPID1F2                                                               MACPID1F2                                                                155
0x0337 BBC0_MACSHA0F2                                                               MACSHA0F2                                                                  155
0x0338 BBC0_MACSHA1F2                                                               MACSHA1F2                                                                  155
0x0339   BBC0_MACPID0F3                                                               MACPID0F3                                                                156
0x033A   BBC0_MACPID1F3                                                               MACPID1F3                                                                156
0x033B BBC0_MACSHA0F3                                                               MACSHA0F3                                                                  156
0x033C BBC0_MACSHA1F3                                                               MACSHA1F3                                                                  156
0x0340     BBC0_AMCS      AACKFT            AACKFA          AACKDR           AACKS               AACK             CCAED            CCATX            TX2RX      156
0x0341    BBC0_AMEDT                                                                   AMEDT                                                                   158
0x0342   BBC0_AMAACKPD       –                 –               –                –                 PD3              PD2              PD1             PD0        158
0x0343   BBC0_AMAACKTL                                                                AMAACKTL                                                                 159
0x0344   BBC0_AMAACKTH       –                 –               –                –                   –                            AMAACKTH                      159
0x0360    BBC0_FSKC0                BT                               MIDXS                                         MIDX                             MORD       101
0x0361    BBC0_FSKC1               FSKPLH                     FI                –                                          SRATE                               102
0x0362    BBC0_FSKC2      PDTM                       RXO                     RXPTO                MSE              PRI              FECS            FECIE      103
0x0363    BBC0_FSKC3                                 SFDT                                                                  PDT                                 104
0x0364    BBC0_FSKC4         –              SFDQ            SFD32            RAWRBIT                      CSFD1                             CSFD0              105
0x0365    BBC0_FSKPLL                                                                  FSKPLL                                                                  105
0x0366   BBC0_FSKSFD0L                                                                FSKSFD0L                                                                 106
0x0367   BBC0_FSKSFD0H                                                                FSKSFD0H                                                                 106
0x0368   BBC0_FSKSFD1L                                                                FSKSFD1L                                                                 106
0x0369   BBC0_FSKSFD1H                                                                FSKSFD1H                                                                 106
0x036A   BBC0_FSKPHRTX       –                 –               –                –                 SFD              DW               RB2             RB1        106
0x036B   BBC0_FSKPHRRX     FCST              MS                –                –                 SFD              DW               RB2             RB1        107
0x036C    BBC0_FSKRPC        –                 –               –                –                  EN                              BASET                       110
0x036D BBC0_FSKRPCONT                                                               FSKRPCONT                                                                  110
0x036E BBC0_FSKRPCOFFT                                                              FSKRPCOFFT                                                                 110
0x0370   BBC0_FSKRRXFLL                                                               FSKRRXFLL                                                                108
0x0371 BBC0_FSKRRXFLH        –                 –               –                –                   –                            FSKRRXFLH                     108
0x0372    BBC0_FSKDM         –                 –               –                –                   –                –               PE              EN        109
0x0373    BBC0_FSKPE0                                                                  FSKPE0                                                                  109
0x0374    BBC0_FSKPE1                                                                  FSKPE1                                                                  109
0x0375    BBC0_FSKPE2                                                                  FSKPE2                                                                  109
0x0380     BBC0_PMUC      CCFTS             IQSEL            FED                                 SYNC                               AVG              EN        162
0x0381    BBC0_PMUVAL                                                                  PMUVAL                                                                  164
0x0382    BBC0_PMUQF                                                                   PMUQF                                                                   164
0x0383     BBC0_PMUI                                                                    PMUI                                                                   164
0x0384     BBC0_PMUQ                                                                    PMUQ                                                                   164
0x0390     BBC0_CNTC         –                 –               –             CAPTXS             CAPRXS            RSTTXS           RSTRXS            EN        167
0x0391     BBC0_CNT0                                                                    CNT0                                                                   168
0x0392     BBC0_CNT1                                                                    CNT1                                                                   168
0x0393     BBC0_CNT2                                                                    CNT2                                                                   168
0x0394     BBC0_CNT3                                                                    CNT3                                                                   168
0x0400     BBC1_IRQM       FBLI             AGCR            AGCH              TXFE               RXEM             RXAM              RXFE            RXFS       39
                                                                                                                                                             84, 139,
0x0401      BBC1_PC        CTX              FCSFE           FCSOK            TXAFCS              FCST             BBEN                       PT
                                                                                                                                                               222




                                                                                                            Atmel AT86RF215 - DATASHEET                          183
                                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Addr | Name | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Page |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x032C | BBC0_MACEA7 | MACEA7 |  |  |  |  |  |  |  | 153 |
| 0x032D | BBC0_MACPID0F0 | MACPID0F0 |  |  |  |  |  |  |  | 153 |
| 0x032E | BBC0_MACPID1F0 | MACPID1F0 |  |  |  |  |  |  |  | 153 |
| 0x032F | BBC0_MACSHA0F0 | MACSHA0F0 |  |  |  |  |  |  |  | 154 |
| 0x0330 | BBC0_MACSHA1F0 | MACSHA1F0 |  |  |  |  |  |  |  | 154 |
| 0x0331 | BBC0_MACPID0F1 | MACPID0F1 |  |  |  |  |  |  |  | 154 |
| 0x0332 | BBC0_MACPID1F1 | MACPID1F1 |  |  |  |  |  |  |  | 154 |
| 0x0333 | BBC0_MACSHA0F1 | MACSHA0F1 |  |  |  |  |  |  |  | 154 |
| 0x0334 | BBC0_MACSHA1F1 | MACSHA1F1 |  |  |  |  |  |  |  | 155 |
| 0x0335 | BBC0_MACPID0F2 | MACPID0F2 |  |  |  |  |  |  |  | 155 |
| 0x0336 | BBC0_MACPID1F2 | MACPID1F2 |  |  |  |  |  |  |  | 155 |
| 0x0337 | BBC0_MACSHA0F2 | MACSHA0F2 |  |  |  |  |  |  |  | 155 |
| 0x0338 | BBC0_MACSHA1F2 | MACSHA1F2 |  |  |  |  |  |  |  | 155 |
| 0x0339 | BBC0_MACPID0F3 | MACPID0F3 |  |  |  |  |  |  |  | 156 |
| 0x033A | BBC0_MACPID1F3 | MACPID1F3 |  |  |  |  |  |  |  | 156 |
| 0x033B | BBC0_MACSHA0F3 | MACSHA0F3 |  |  |  |  |  |  |  | 156 |
| 0x033C | BBC0_MACSHA1F3 | MACSHA1F3 |  |  |  |  |  |  |  | 156 |
| 0x0340 | BBC0_AMCS | AACKFT | AACKFA | AACKDR | AACKS | AACK | CCAED | CCATX | TX2RX | 156 |
| 0x0341 | BBC0_AMEDT | AMEDT |  |  |  |  |  |  |  | 158 |
| 0x0342 | BBC0_AMAACKPD | – | – | – | – | PD3 | PD2 | PD1 | PD0 | 158 |
| 0x0343 | BBC0_AMAACKTL | AMAACKTL |  |  |  |  |  |  |  | 159 |
| 0x0344 | BBC0_AMAACKTH | – | – | – | – | – | AMAACKTH |  |  | 159 |
| 0x0360 | BBC0_FSKC0 | BT |  | MIDXS |  | MIDX |  |  | MORD | 101 |
| 0x0361 | BBC0_FSKC1 | FSKPLH |  | FI | – | SRATE |  |  |  | 102 |
| 0x0362 | BBC0_FSKC2 | PDTM | RXO |  | RXPTO | MSE | PRI | FECS | FECIE | 103 |
| 0x0363 | BBC0_FSKC3 | SFDT |  |  |  | PDT |  |  |  | 104 |
| 0x0364 | BBC0_FSKC4 | – | SFDQ | SFD32 | RAWRBIT | CSFD1 |  | CSFD0 |  | 105 |
| 0x0365 | BBC0_FSKPLL | FSKPLL |  |  |  |  |  |  |  | 105 |
| 0x0366 | BBC0_FSKSFD0L | FSKSFD0L |  |  |  |  |  |  |  | 106 |
| 0x0367 | BBC0_FSKSFD0H | FSKSFD0H |  |  |  |  |  |  |  | 106 |
| 0x0368 | BBC0_FSKSFD1L | FSKSFD1L |  |  |  |  |  |  |  | 106 |
| 0x0369 | BBC0_FSKSFD1H | FSKSFD1H |  |  |  |  |  |  |  | 106 |
| 0x036A | BBC0_FSKPHRTX | – | – | – | – | SFD | DW | RB2 | RB1 | 106 |
| 0x036B | BBC0_FSKPHRRX | FCST | MS | – | – | SFD | DW | RB2 | RB1 | 107 |
| 0x036C | BBC0_FSKRPC | – | – | – | – | EN | BASET |  |  | 110 |
| 0x036D | BBC0_FSKRPCONT | FSKRPCONT |  |  |  |  |  |  |  | 110 |
| 0x036E | BBC0_FSKRPCOFFT | FSKRPCOFFT |  |  |  |  |  |  |  | 110 |
| 0x0370 | BBC0_FSKRRXFLL | FSKRRXFLL |  |  |  |  |  |  |  | 108 |
| 0x0371 | BBC0_FSKRRXFLH | – | – | – | – | – | FSKRRXFLH |  |  | 108 |
| 0x0372 | BBC0_FSKDM | – | – | – | – | – | – | PE | EN | 109 |
| 0x0373 | BBC0_FSKPE0 | FSKPE0 |  |  |  |  |  |  |  | 109 |
| 0x0374 | BBC0_FSKPE1 | FSKPE1 |  |  |  |  |  |  |  | 109 |
| 0x0375 | BBC0_FSKPE2 | FSKPE2 |  |  |  |  |  |  |  | 109 |
| 0x0380 | BBC0_PMUC | CCFTS | IQSEL | FED | SYNC |  |  | AVG | EN | 162 |
| 0x0381 | BBC0_PMUVAL | PMUVAL |  |  |  |  |  |  |  | 164 |
| 0x0382 | BBC0_PMUQF | PMUQF |  |  |  |  |  |  |  | 164 |
| 0x0383 | BBC0_PMUI | PMUI |  |  |  |  |  |  |  | 164 |
| 0x0384 | BBC0_PMUQ | PMUQ |  |  |  |  |  |  |  | 164 |
| 0x0390 | BBC0_CNTC | – | – | – | CAPTXS | CAPRXS | RSTTXS | RSTRXS | EN | 167 |
| 0x0391 | BBC0_CNT0 | CNT0 |  |  |  |  |  |  |  | 168 |
| 0x0392 | BBC0_CNT1 | CNT1 |  |  |  |  |  |  |  | 168 |
| 0x0393 | BBC0_CNT2 | CNT2 |  |  |  |  |  |  |  | 168 |
| 0x0394 | BBC0_CNT3 | CNT3 |  |  |  |  |  |  |  | 168 |
| 0x0400 | BBC1_IRQM | FBLI | AGCR | AGCH | TXFE | RXEM | RXAM | RXFE | RXFS | 39 |
|  |  |  |  |  |  |  |  |  |  | 84, 139, |
| 0x0401 | BBC1_PC | CTX | FCSFE | FCSOK | TXAFCS | FCST | BBEN | PT |  |  |
|  |  |  |  |  |  |  |  |  |  | 222 |
|  |  |  |  |  |  |  |  |  |  |  |


<!-- page 184 -->

Addr         Name          Bit 7             Bit 6          Bit 5           Bit 4               Bit 3           Bit 2            Bit 1           Bit 0    Page
0x0402      BBC1_PS          –                 –              –               –                   –               –                –             TXUR     135
0x0404     BBC1_RXFLL                                                                RXFLL                                                                135
0x0405    BBC1_RXFLH         –                 –              –               –                   –                              RXFLH                    135
0x0406     BBC1_TXFLL                                                                 TXFLL                                                               136
0x0407    BBC1_TXFLH         –                 –              –               –                   –                              TXFLH                    135
0x0408     BBC1_FBLL                                                                  FBLL                                                                135
0x0409     BBC1_FBLH         –                 –              –               –                   –                              FBLH                     135
0x040A     BBC1_FBLIL                                                                 FBLIL                                                               136
0x040B     BBC1_FBLIH        –                 –              –               –                   –                              FBLIH                    137
0x040C BBC1_OFDMPHRTX      RB21              RB18           RB17             RB5                  –                              MCS                      116
0x040D BBC1_OFDMPHRRX      RB21              RB18           RB17             RB5                SPC                              MCS                      116
0x040E    BBC1_OFDMC               SSRX                             SSTX                        LFO              POI                     OPT              117
0x040F   BBC1_OFDMSW                         PDT                            RXO                   –               –                –               –      118
0x0410   BBC1_OQPSKC0        –                 –              –              DM                 MOD               –                      FCHIP            126
0x0411   BBC1_OQPSKC1      RXO            RXOLEG                            PDT1                                                 PDT0                     127
0x0412   BBC1_OQPSKC2        –                 –            SPC             RPC               ENPROP           FCSTLEG                   RXM              127
0x0413   BBC1_OQPSKC3        –                 –           HRLEG              –                         NSFD                       –               –      129
0x0414 BBC1_OQPSKPHRTX       –                 –           PPDUT             RB0                                MOD                              LEG      129
0x0415 BBC1_OQPSKPHRRX       –                 –           PPDUT             RB0                                MOD                              LEG      130
0x0420     BBC1_AFC0         –                 –              –              PM               AFEN3             AFEN2            AFEN1           AFEN0    149
0x0421     BBC1_AFC1      MRFT3             MRFT2          MRFT1            MRFT0             PANC3            PANC2             PANC1           PANC0    150
0x0422    BBC1_AFFTM                                                                 AFFTM                                                                151
0x0423    BBC1_AFFVM         –                 –              –               –                                         AFFVM                             151
0x0424     BBC1_AFS          –                 –              –              EM                 AM3             AM2              AM1             AM0      151
0x0425    BBC1_MACEA0                                                                MACEA0                                                               152
0x0426    BBC1_MACEA1                                                                MACEA1                                                               152
0x0427    BBC1_MACEA2                                                                MACEA2                                                               152
0x0428    BBC1_MACEA3                                                                MACEA3                                                               152
0x0429    BBC1_MACEA4                                                                MACEA4                                                               152
0x042A    BBC1_MACEA5                                                                MACEA5                                                               153
0x042B    BBC1_MACEA6                                                                MACEA6                                                               153
0x042C    BBC1_MACEA7                                                                MACEA7                                                               153
0x042D   BBC1_MACPID0F0                                                             MACPID0F0                                                             153
0x042E   BBC1_MACPID1F0                                                             MACPID1F0                                                             153
0x042F BBC1_MACSHA0F0                                                              MACSHA0F0                                                              154
0x0430 BBC1_MACSHA1F0                                                              MACSHA1F0                                                              154
0x0431   BBC1_MACPID0F1                                                             MACPID0F1                                                             154
0x0432   BBC1_MACPID1F1                                                             MACPID1F1                                                             154
0x0433 BBC1_MACSHA0F1                                                              MACSHA0F1                                                              154
0x0434 BBC1_MACSHA1F1                                                              MACSHA1F1                                                              155
0x0435   BBC1_MACPID0F2                                                             MACPID0F2                                                             155
0x0436   BBC1_MACPID1F2                                                             MACPID1F2                                                             155
0x0437 BBC1_MACSHA0F2                                                              MACSHA0F2                                                              155
0x0438 BBC1_MACSHA1F2                                                              MACSHA1F2                                                              155
0x0439   BBC1_MACPID0F3                                                             MACPID0F3                                                             156
0x043A   BBC1_MACPID1F3                                                             MACPID1F3                                                             156
0x043B BBC1_MACSHA0F3                                                              MACSHA0F3                                                              156
0x043C BBC1_MACSHA1F3                                                              MACSHA1F3                                                              156
0x0440     BBC1_AMCS      AACKFT            AACKFA         AACKDR           AACKS              AACK            CCAED             CCATX           TX2RX    156
0x0441    BBC1_AMEDT                                                                 AMEDT                                                                158
0x0442   BBC1_AMAACKPD       –                 –              –               –                 PD3              PD2              PD1             PD0     158
0x0443   BBC1_AMAACKTL                                                              AMAACKTL                                                              159
0x0444   BBC1_AMAACKTH       –                 –              –               –                   –                          AMAACKTH                     159
0x0460    BBC1_FSKC0                BT                              MIDXS                                       MIDX                             MORD     101
0x0461    BBC1_FSKC1               FSKPLH                    FI               –                                          SRATE                            102
0x0462    BBC1_FSKC2      PDTM                       RXO                    RXPTO               MSE              PRI             FECS            FECIE    103




                                                                                                          Atmel AT86RF215 - DATASHEET                       184
                                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Addr | Name | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Page |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x0402 | BBC1_PS | – | – | – | – | – | – | – | TXUR | 135 |
| 0x0404 | BBC1_RXFLL | RXFLL |  |  |  |  |  |  |  | 135 |
| 0x0405 | BBC1_RXFLH | – | – | – | – | – | RXFLH |  |  | 135 |
| 0x0406 | BBC1_TXFLL | TXFLL |  |  |  |  |  |  |  | 136 |
| 0x0407 | BBC1_TXFLH | – | – | – | – | – | TXFLH |  |  | 135 |
| 0x0408 | BBC1_FBLL | FBLL |  |  |  |  |  |  |  | 135 |
| 0x0409 | BBC1_FBLH | – | – | – | – | – | FBLH |  |  | 135 |
| 0x040A | BBC1_FBLIL | FBLIL |  |  |  |  |  |  |  | 136 |
| 0x040B | BBC1_FBLIH | – | – | – | – | – | FBLIH |  |  | 137 |
| 0x040C | BBC1_OFDMPHRTX | RB21 | RB18 | RB17 | RB5 | – | MCS |  |  | 116 |
| 0x040D | BBC1_OFDMPHRRX | RB21 | RB18 | RB17 | RB5 | SPC | MCS |  |  | 116 |
| 0x040E | BBC1_OFDMC | SSRX |  | SSTX |  | LFO | POI | OPT |  | 117 |
| 0x040F | BBC1_OFDMSW | PDT |  |  | RXO | – | – | – | – | 118 |
| 0x0410 | BBC1_OQPSKC0 | – | – | – | DM | MOD | – | FCHIP |  | 126 |
| 0x0411 | BBC1_OQPSKC1 | RXO | RXOLEG | PDT1 |  |  | PDT0 |  |  | 127 |
| 0x0412 | BBC1_OQPSKC2 | – | – | SPC | RPC | ENPROP | FCSTLEG | RXM |  | 127 |
| 0x0413 | BBC1_OQPSKC3 | – | – | HRLEG | – | NSFD |  | – | – | 129 |
| 0x0414 | BBC1_OQPSKPHRTX | – | – | PPDUT | RB0 | MOD |  |  | LEG | 129 |
| 0x0415 | BBC1_OQPSKPHRRX | – | – | PPDUT | RB0 | MOD |  |  | LEG | 130 |
| 0x0420 | BBC1_AFC0 | – | – | – | PM | AFEN3 | AFEN2 | AFEN1 | AFEN0 | 149 |
| 0x0421 | BBC1_AFC1 | MRFT3 | MRFT2 | MRFT1 | MRFT0 | PANC3 | PANC2 | PANC1 | PANC0 | 150 |
| 0x0422 | BBC1_AFFTM | AFFTM |  |  |  |  |  |  |  | 151 |
| 0x0423 | BBC1_AFFVM | – | – | – | – | AFFVM |  |  |  | 151 |
| 0x0424 | BBC1_AFS | – | – | – | EM | AM3 | AM2 | AM1 | AM0 | 151 |
| 0x0425 | BBC1_MACEA0 | MACEA0 |  |  |  |  |  |  |  | 152 |
| 0x0426 | BBC1_MACEA1 | MACEA1 |  |  |  |  |  |  |  | 152 |
| 0x0427 | BBC1_MACEA2 | MACEA2 |  |  |  |  |  |  |  | 152 |
| 0x0428 | BBC1_MACEA3 | MACEA3 |  |  |  |  |  |  |  | 152 |
| 0x0429 | BBC1_MACEA4 | MACEA4 |  |  |  |  |  |  |  | 152 |
| 0x042A | BBC1_MACEA5 | MACEA5 |  |  |  |  |  |  |  | 153 |
| 0x042B | BBC1_MACEA6 | MACEA6 |  |  |  |  |  |  |  | 153 |
| 0x042C | BBC1_MACEA7 | MACEA7 |  |  |  |  |  |  |  | 153 |
| 0x042D | BBC1_MACPID0F0 | MACPID0F0 |  |  |  |  |  |  |  | 153 |
| 0x042E | BBC1_MACPID1F0 | MACPID1F0 |  |  |  |  |  |  |  | 153 |
| 0x042F | BBC1_MACSHA0F0 | MACSHA0F0 |  |  |  |  |  |  |  | 154 |
| 0x0430 | BBC1_MACSHA1F0 | MACSHA1F0 |  |  |  |  |  |  |  | 154 |
| 0x0431 | BBC1_MACPID0F1 | MACPID0F1 |  |  |  |  |  |  |  | 154 |
| 0x0432 | BBC1_MACPID1F1 | MACPID1F1 |  |  |  |  |  |  |  | 154 |
| 0x0433 | BBC1_MACSHA0F1 | MACSHA0F1 |  |  |  |  |  |  |  | 154 |
| 0x0434 | BBC1_MACSHA1F1 | MACSHA1F1 |  |  |  |  |  |  |  | 155 |
| 0x0435 | BBC1_MACPID0F2 | MACPID0F2 |  |  |  |  |  |  |  | 155 |
| 0x0436 | BBC1_MACPID1F2 | MACPID1F2 |  |  |  |  |  |  |  | 155 |
| 0x0437 | BBC1_MACSHA0F2 | MACSHA0F2 |  |  |  |  |  |  |  | 155 |
| 0x0438 | BBC1_MACSHA1F2 | MACSHA1F2 |  |  |  |  |  |  |  | 155 |
| 0x0439 | BBC1_MACPID0F3 | MACPID0F3 |  |  |  |  |  |  |  | 156 |
| 0x043A | BBC1_MACPID1F3 | MACPID1F3 |  |  |  |  |  |  |  | 156 |
| 0x043B | BBC1_MACSHA0F3 | MACSHA0F3 |  |  |  |  |  |  |  | 156 |
| 0x043C | BBC1_MACSHA1F3 | MACSHA1F3 |  |  |  |  |  |  |  | 156 |
| 0x0440 | BBC1_AMCS | AACKFT | AACKFA | AACKDR | AACKS | AACK | CCAED | CCATX | TX2RX | 156 |
| 0x0441 | BBC1_AMEDT | AMEDT |  |  |  |  |  |  |  | 158 |
| 0x0442 | BBC1_AMAACKPD | – | – | – | – | PD3 | PD2 | PD1 | PD0 | 158 |
| 0x0443 | BBC1_AMAACKTL | AMAACKTL |  |  |  |  |  |  |  | 159 |
| 0x0444 | BBC1_AMAACKTH | – | – | – | – | – | AMAACKTH |  |  | 159 |
| 0x0460 | BBC1_FSKC0 | BT |  | MIDXS |  | MIDX |  |  | MORD | 101 |
| 0x0461 | BBC1_FSKC1 | FSKPLH |  | FI | – | SRATE |  |  |  | 102 |
| 0x0462 | BBC1_FSKC2 | PDTM | RXO |  | RXPTO | MSE | PRI | FECS | FECIE | 103 |


<!-- page 185 -->

Addr         Name         Bit 7   Bit 6          Bit 5    Bit 4              Bit 3            Bit 2           Bit 1           Bit 0     Page
0x0463    BBC1_FSKC3                      SFDT                                                        PDT                               104
0x0464    BBC1_FSKC4        –     SFDQ           SFD32   RAWRBIT                     CSFD1                            CSFD0             105
0x0465    BBC1_FSKPLL                                              FSKPLL                                                               105
0x0466   BBC1_FSKSFD0L                                            FSKSFD0L                                                              106
0x0467   BBC1_FSKSFD0H                                            FSKSFD0H                                                              106
0x0468   BBC1_FSKSFD1L                                            FSKSFD1L                                                              106
0x0469   BBC1_FSKSFD1H                                            FSKSFD1H                                                              106
0x046A   BBC1_FSKPHRTX      –       –              –        –                 SFD             DW               RB2            RB1       106
0x046B   BBC1_FSKPHRRX    FCST     MS              –        –                 SFD             DW               RB2            RB1       107
0x046C    BBC1_FSKRPC       –       –              –        –                 EN                              BASET                     110
0x046D BBC1_FSKRPCONT                                           FSKRPCONT                                                               110
0x046E BBC1_FSKRPCOFFT                                          FSKRPCOFFT                                                              110
0x0470   BBC1_FSKRRXFLL                                           FSKRRXFLL                                                             108
0x0471 BBC1_FSKRRXFLH       –       –              –        –                  –                            FSKRRXFLH                   108
0x0472    BBC1_FSKDM        –       –              –        –                  –                –              PE              EN       109
0x0473    BBC1_FSKPE0                                              FSKPE0                                                               109
0x0474    BBC1_FSKPE1                                              FSKPE1                                                               109
0x0475    BBC1_FSKPE2                                              FSKPE2                                                               109
0x0480     BBC1_PMUC      CCFTS   IQSEL          FED                         SYNC                             AVG              EN       162
0x0481    BBC1_PMUVAL                                              PMUVAL                                                               164
0x0482    BBC1_PMUQF                                               PMUQF                                                                164
0x0483     BBC1_PMUI                                                PMUI                                                                164
0x0484     BBC1_PMUQ                                                PMUQ                                                                164
0x0490     BBC1_CNTC        –       –              –     CAPTXS             CAPRXS           RSTTXS          RSTRXS            EN       167
0x0491     BBC1_CNT0                                                CNT0                                                                168
0x0492     BBC1_CNT1                                                CNT1                                                                168
0x0493     BBC1_CNT2                                                CNT2                                                                168
0x0494     BBC1_CNT3                                                CNT3                                                                168
0x2000    BBC0_FBRXS                                               FBRXS                                                                136
0x27FE    BBC0_FBRXE                                               FBRXE                                                                136
0x2800    BBC0_FBTXS                                               FBTXS                                                                136
0x2FFE    BBC0_FBTXE                                               FBTXE                                                                136
0x3000    BBC1_FBRXS                                               FBRXS                                                                136
0x37FE    BBC1_FBRXE                                               FBRXE                                                                136
0x3800    BBC1_FBTXS                                               FBTXS                                                                136
0x3FFE    BBC1_FBTXE                                               FBTXE                                                                136




                                                                                       Atmel AT86RF215 - DATASHEET                        185
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Addr | Name | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Page |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x0463 | BBC1_FSKC3 | SFDT |  |  |  | PDT |  |  |  | 104 |
| 0x0464 | BBC1_FSKC4 | – | SFDQ | SFD32 | RAWRBIT | CSFD1 |  | CSFD0 |  | 105 |
| 0x0465 | BBC1_FSKPLL | FSKPLL |  |  |  |  |  |  |  | 105 |
| 0x0466 | BBC1_FSKSFD0L | FSKSFD0L |  |  |  |  |  |  |  | 106 |
| 0x0467 | BBC1_FSKSFD0H | FSKSFD0H |  |  |  |  |  |  |  | 106 |
| 0x0468 | BBC1_FSKSFD1L | FSKSFD1L |  |  |  |  |  |  |  | 106 |
| 0x0469 | BBC1_FSKSFD1H | FSKSFD1H |  |  |  |  |  |  |  | 106 |
| 0x046A | BBC1_FSKPHRTX | – | – | – | – | SFD | DW | RB2 | RB1 | 106 |
| 0x046B | BBC1_FSKPHRRX | FCST | MS | – | – | SFD | DW | RB2 | RB1 | 107 |
| 0x046C | BBC1_FSKRPC | – | – | – | – | EN | BASET |  |  | 110 |
| 0x046D | BBC1_FSKRPCONT | FSKRPCONT |  |  |  |  |  |  |  | 110 |
| 0x046E | BBC1_FSKRPCOFFT | FSKRPCOFFT |  |  |  |  |  |  |  | 110 |
| 0x0470 | BBC1_FSKRRXFLL | FSKRRXFLL |  |  |  |  |  |  |  | 108 |
| 0x0471 | BBC1_FSKRRXFLH | – | – | – | – | – | FSKRRXFLH |  |  | 108 |
| 0x0472 | BBC1_FSKDM | – | – | – | – | – | – | PE | EN | 109 |
| 0x0473 | BBC1_FSKPE0 | FSKPE0 |  |  |  |  |  |  |  | 109 |
| 0x0474 | BBC1_FSKPE1 | FSKPE1 |  |  |  |  |  |  |  | 109 |
| 0x0475 | BBC1_FSKPE2 | FSKPE2 |  |  |  |  |  |  |  | 109 |
| 0x0480 | BBC1_PMUC | CCFTS | IQSEL | FED | SYNC |  |  | AVG | EN | 162 |
| 0x0481 | BBC1_PMUVAL | PMUVAL |  |  |  |  |  |  |  | 164 |
| 0x0482 | BBC1_PMUQF | PMUQF |  |  |  |  |  |  |  | 164 |
| 0x0483 | BBC1_PMUI | PMUI |  |  |  |  |  |  |  | 164 |
| 0x0484 | BBC1_PMUQ | PMUQ |  |  |  |  |  |  |  | 164 |
| 0x0490 | BBC1_CNTC | – | – | – | CAPTXS | CAPRXS | RSTTXS | RSTRXS | EN | 167 |
| 0x0491 | BBC1_CNT0 | CNT0 |  |  |  |  |  |  |  | 168 |
| 0x0492 | BBC1_CNT1 | CNT1 |  |  |  |  |  |  |  | 168 |
| 0x0493 | BBC1_CNT2 | CNT2 |  |  |  |  |  |  |  | 168 |
| 0x0494 | BBC1_CNT3 | CNT3 |  |  |  |  |  |  |  | 168 |
| 0x2000 | BBC0_FBRXS | FBRXS |  |  |  |  |  |  |  | 136 |
| 0x27FE | BBC0_FBRXE | FBRXE |  |  |  |  |  |  |  | 136 |
| 0x2800 | BBC0_FBTXS | FBTXS |  |  |  |  |  |  |  | 136 |
| 0x2FFE | BBC0_FBTXE | FBTXE |  |  |  |  |  |  |  | 136 |
| 0x3000 | BBC1_FBRXS | FBRXS |  |  |  |  |  |  |  | 136 |
| 0x37FE | BBC1_FBRXE | FBRXE |  |  |  |  |  |  |  | 136 |
| 0x3800 | BBC1_FBTXS | FBTXS |  |  |  |  |  |  |  | 136 |
| 0x3FFE | BBC1_FBTXE | FBTXE |  |  |  |  |  |  |  | 136 |


<!-- page 186 -->

9.   Package Drawing
     Figure 9-1 shows the package drawing of the AT86RF215.

     Figure 9-1. Package Drawing QFN48




                                                              Atmel AT86RF215 - DATASHEET                     186
                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 187 -->

10.    Electrical Characteristics

10.1   Absolute Maximum Ratings*

                                                                                     *Notice:   Stresses beyond those listed under “Absolute
       Storage temperature ............................ -50 to 150°C
                                                                                                Maximum Ratings” may cause permanent
       Lead temperature .......................................... 260°C                        damage to the device. This is a stress rating only
                                                                                                and functional operation of the device at these or
       ESD voltage (Human Body Model) .................... 4kV
                                                                                                any other conditions beyond those indicated in
       Input RF level .............................................. 10dBm                      the operational sections of this specification are
                                                                                                not implied. Exposure to absolute maximum
       Voltage on all digital pins ...................... -0.3 to 4.0V
                                                                                                rating conditions for extended periods may affect
       Voltage on all analog pins..................... -0.3 to 2.0V                             device reliability.



10.2   Operating Range

       Table 10-1. Operating Range

       Symbol          Parameter                                         Condition                           Min.        Typ.         Max.          Unit
       TOP             Operating temperature range                                                            -40                      85           °C
       VDD             DEVDD/EVDD digital and analog                                                          1.8         3.0          3.6           V
                       external supply voltage




10.3   Digital Pin Specifications
       Test Condition: TOP = 25°C

       Table 10-2. Digital pin specifications

       Symbol          Parameter                                         Condition                           Min.        Typ.         Max.          Unit
       VIH             High level input voltage                                                            VDD–0.4                                   V
       VIL             Low level input voltage                                                                                         0.4           V
       VOH             High level output voltage                                                           VDD–0.4                                   V
       VOL             Low level output voltage                                                                                        0.4           V




                                                                                                   Atmel AT86RF215 - DATASHEET                           187
                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Storage temperature ............................ -50 to 150°C |  |
| --- | --- |
| Lead temperature .......................................... 260°C |  |
| ESD voltage (Human Body Model) .................... 4kV |  |
| Input RF level .............................................. 10dBm |  |
| Voltage on all digital pins ...................... -0.3 to 4.0V |  |
| Voltage on all analog pins ..................... -0.3 to 2.0V |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| TOP | Operating temperature range |  | -40 |  | 85 | °C |
| VDD | DEVDD/EVDD digital and analog |  | 1.8 | 3.0 | 3.6 | V |
|  | external supply voltage |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| VIH | High level input voltage |  | VDD–0.4 |  |  | V |
| VIL | Low level input voltage |  |  |  | 0.4 | V |
| VOH | High level output voltage |  | VDD–0.4 |  |  | V |
| VOL | Low level output voltage |  |  |  | 0.4 | V |


<!-- page 188 -->

10.4   Power-on Reset Characteristics

       Table 10-3. Power-on Reset Voltage Characteristics

       Symbol        Parameter                                Condition                             Min.        Typ.         Max.          Unit
       tRST          Pulse width at pin RSTN                                                         625                                    ns
       VPOT          Power-on Reset threshold voltage         rising slope (power supply            1.55         1.6         1.65           V
                                                              priviously discharged)(1)
                                                              falling slope(2)                      1.45         1.5         1.55           V
       tPOT          Power-on Reset recovery time             Time of EVDD/DEVDD (VDD) <              1                                    ms
                                                              VPOT
       VPSR          Power-on slope                                                                 0.01                     3300          V/ms
       Notes: 1.     Threshold when device is released from reset when voltage is rising.
              2.     The Power-on Reset will not work unless the supply voltage has been dropped below V POT.




10.5   General Transceiver Specifications

       Table 10-4. General Transceiver Specifications

       Symbol        Parameter                                Condition                             Min.        Typ.         Max.          Unit
       f0            Reference clock frequency                TCXO or XTAL                                        26                       MHz
       Cdec          Decoupling capacitor at pins                                                    100         100        10000          nF
                     AVDD0, DVDD and AVDD1
       IVREG_LIMIT   Current limitation of internal voltage                                          43           60          78           mA
                     regulator at start-up




10.6   Crystal Oscillator Specification

       Table 10-5. XOSC Specification

       Symbol        Parameter                                Condition                             Min.        Typ.         Max.          Unit
       fCRYSTAL      Crystal frequency requirement                                                                26                       MHz
       CLOAD_        Load capacitances of the crystal                                                             8                        pF
       CRYSTAL

       ESR           Maximum ESR of crystal                                                                                   70            Ω
                     specification
       CLEAD_        Lead capacitance of the AT86RF215                                                            5                        pF
       DEVICE




                                                                                           Atmel AT86RF215 - DATASHEET                          188
                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| tRST | Pulse width at pin RSTN |  | 625 |  |  | ns |
| VPOT | Power-on Reset threshold voltage | rising slope (power supply | 1.55 | 1.6 | 1.65 | V |
|  |  | priviously discharged)(1) |  |  |  |  |
|  |  | falling slope(2) | 1.45 | 1.5 | 1.55 | V |
| tPOT | Power-on Reset recovery time | Time of EVDD/DEVDD (VDD) < | 1 |  |  | ms |
|  |  | VPOT |  |  |  |  |
| VPSR | Power-on slope |  | 0.01 |  | 3300 | V/ms |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| f0 | Reference clock frequency | TCXO or XTAL |  | 26 |  | MHz |
| Cdec | Decoupling capacitor at pins AVDD0, DVDD and AVDD1 |  | 100 | 100 | 10000 | nF |
|  |  |  |  |  |  |  |
| IVREG_LIMIT | Current limitation of internal voltage regulator at start-up |  | 43 | 60 | 78 | mA |
|  |  |  |  |  |  |  |


<!-- page 189 -->

10.7   Clock Output – pin CLKO

       Table 10-6. Clock Output Specification

       Symbol            Parameter                           Condition                            Min.        Typ.         Max.          Unit
       fCLKO             Clock output (pin CLKO) frequency   RF_CLKO.OS=1                                       26                       MHz
                                                             RF_CLKO.OS=2                                       32
                                                             RF_CLKO.OS=3                                       16
                                                             RF_CLKO.OS=4                                       8
                                                             RF_CLKO.OS=5                                       4
                                                             RF_CLKO.OS=6                                       2
                                                             RF_CLKO.OS=7                                       1
       DCLKO             Duty cycle                                                                42                       58            %




10.8   Transition Time
       The time reference of an SPI command is the last rising clock of SCLK of the SPI VALUE.

       Table 10-7. Transition Timing

       Symbol            Parameter                           Condition                            Min.        Typ.         Max.          Unit
       tPOWERON          Transition time from power-on       XTAL supplier: ACT BN serie                                   500           μs
                         (VDD>1.6V) until interrupt WAKEUP   (Cload=8pF); Cdec_DVDD=100nF
                         (state TRXOFF)
       tSLEEP_           Transition time from state SLEEP                                                       1                        μs
       TRXOFF            (SPI command CMD=TRXOFF) until
                         interrupt WAKEUP (state TRXOFF)
       tDEEP_SLEEP_ Transition time from state               XTAL supplier: ACT BN serie                                   500           μs
       TRXOFF       DEEP_SLEEP (SPI command                  (Cload=8pF); Cdec_DVDD=100nF
                    CMD=TRXOFF) until interrupt
                    WAKEUP (state TRXOFF) and
                    stable clock output at pin CLKO
       tRESET_           Transition time from release                                                           1                        μs
       TRXOFF            RESETN until state TRXOFF
       tTRXOFF_          Transition time from state TRXOFF Cdec_AVDD=100nF                                      90         200           μs
       TXPREP            (SPI command CMD=TXPREP) until
                         interrupt TRXRDY (state TXPREP)
       tTRXOFF_RX        Transition time from TRXOFF (SPI    Cdec_AVDD=100nF                                    90         200           μs
                         command CMD=RX) to state RX
       tTXPREP_TX        Transition time from TXPREP (SPI    state machine reaction time; for                              200           ns
                         command CMD=TX) to state TX         more details about the TX
                                                             procedure see chapter
                                                             "Transmitter Frontend"
       ttx_start_delay   Delay from state TX until the PA                                                       4                        μs
                         ramp start
       tTXPREP_RX        Transition time from TXPREP (SPI                                                                  200           ns
                         command CMD=RX) to state RX
       tTXPREP_          Transition time from TXPREP (SPI                                                                  200           ns
       TRXOFF            command CMD=TRXOFF) to state
                         TRXOFF
       tRX_TRXOFF        Transition time from RX (SPI                                                                      200           ns
                         command CMD=TRXOFF) to state
                         TRXOFF



                                                                                        Atmel AT86RF215 - DATASHEET                        189
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 190 -->

        Symbol        Parameter                                 Condition                              Min.        Typ.         Max.          Unit
        tRX_TXPREP    Transition time from RX (IRQ RXFE                                                                         200           ns
                      or SPI command CMD=TXPREP) to
                      state TXPREP
        tTX_TXPREP_   Transition time from TX (IRQ TXFE)                                                                        200           ns
        TXFE          to state TXPREP
        tTX_TXPREP_   Transition time from TX (SPI              PA ramp time                                                     33           μs
        CMD           command CMD=TXPREP) to state              RFn_TXCUTC_PARAMP = 3
                      TXPREP
        tTX_TRXOFF    Transition time from TX (SPI                                                                              200           ns
                      command CMD=TRXOFF) to state
                      TRXOFF
        tVREG_SETTL   Settling time of AVDD or DVDD             Cdec=100nF                                           35                       μs
                      voltage regulator
        tXOSC_SETTL   Settling time of the crystal oscillator    XTAL supplier: ACT BN serie                        150                       μs
                                                                (Cload=8pF) / fast start up option
        tPLL_CH_SW    Frequency channel switch time             ∆fchannel<20MHz                         10                      100           μs
                      (PLL) in state TXPREP
        tRXFE         IRQ RXFE processing delay relative        Transceiver received a valid                                    100           μs
                      to frame end; typical time depends        frame.
                      on specific PHY mode




10.9   Transmitter Characteristics

10.9.1 General Transmitter Characteristics
       Refer to section "Output Power at Several Modulations " on page 208 for detailed output power information and charts.
       Test Conditions: TOP= 25°C, VDD= 3.0V, fchannel (500MHz band)=490MHz

       Table 10-8. Transmitter Characteristics for the 500MHz Band

        Symbol        Parameter                                 Condition                              Min.        Typ.         Max.          Unit
        PTX_05        TX output power                           Maximum output power for               12.0         16.0        16.5          dBm
                                                                continous wave at device pin
        PRANGE_05     Output power range                                                                            27.0                      dB
                        nd                           (1)
        PHARM2_05_S 2        harmonic single ended              w/o filtering; continuous wave at                  -14.0                      dBm
                                                                maximal output power
        PHARM3_05_S 3rd harmonic single ended(1)                w/o filtering; continuous wave at                   0.0                       dBm
                                                                maximal output power
        PHARM4_05_S 4th harmonic single ended(1)                w/o filtering; continuous wave at                  -23.0                      dBm
                                                                maximal output power
        PHARM5_05_S 5th harmonic single ended(1)                w/o filtering; continuous wave at                  -12.0                      dBm
                                                                maximal output power
        Note:    1.   Requires external filtering to comply with regulatory rules.




                                                                                             Atmel AT86RF215 - DATASHEET                        190
                                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 191 -->

       Test Conditions: TOP= 25°C, VDD= 3.0V, fchannel (900MHz band)=870MHz

       Table 10-9. Transmitter Characteristics for the 900MHz Band

        Symbol        Parameter                               Condition                            Min.        Typ.         Max.          Unit
        PTX_09        TX output power                         Maximum output power for             11.0         14.5        16.0          dBm
                                                              continous wave
        PRANGE_09     Output power range                                                                        27.0                      dB
        PHARM2_09_S 2nd harmonic single ended(1)              w/o filtering; continuous wave                   -17.0                      dBm
                                                              modulation at maximal output
                                                              power
        PHARM3_09_S 3rd harmonic single ended(1)              w/o filtering; continuous wave at                 -8.0                      dBm
                                                              maximal output power
        PHARM4_09_S 4th harmonic single ended(1)              w/o filtering; continuous wave at                -27.0                      dBm
                                                              maximal output power
        PHARM5_09_S 5th harmonic single ended(1)              w/o filtering; continuous wave at                -25.0                      dBm
                                                              maximal output power
        Note:    1.   Requires external filtering to comply with regulatory rules.


       Test Conditions: TOP= 25°C, VDD= 3.0V, fchannel (2.4GHzHz band)=2440MHz

       Table 10-10. Transmitter Characteristics for the 2.4GHz Band

        Symbol        Parameter                               Condition                            Min.        Typ.         Max.          Unit
        PTX_24        TX output power                         Maximum output power for             11.0         14.0        15.5          dBm
                                                              continous wave
        PRANGE_24     Output power range                                                                        28.0                      dB
        PHARM2_24_S   2nd harmonic single ended(1)            w/o filtering; continuous wave at                -28.0                      dBm
                                                              maximal output power
        PHARM3_24_S 3rd harmonic single ended(1)              w/o filtering; continuous wave at                 -7.0                      dBm
                                                              maximal output power
        PHARM4_24_S 4th harmonic single ended(1)              w/o filtering; continuous wave at                -38.0                      dBm
                                                              maximal output power
        PHARM5_24_S 5th harmonic single ended(1)              w/o filtering; continuous wave at                -27.0                      dBm
                                                              maximal output power
        Note:    1.   Requires external filtering to comply with regulatory rules.

10.9.2 Transmitter Signal Quality
       Table 10-11 shows the typical FSK modulation quality value (frequency deviation and zero crossing) according to [3].




                                                                                          Atmel AT86RF215 - DATASHEET                       191
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| PTX_24 | TX output power | Maximum output power for | 11.0 | 14.0 | 15.5 | dBm |
|  |  | continous wave |  |  |  |  |
| PRANGE_24 | Output power range |  |  | 28.0 |  | dB |
| PHARM2_24_S | 2nd harmonic single ended(1) | w/o filtering; continuous wave at |  | -28.0 |  | dBm |
|  |  | maximal output power |  |  |  |  |
| PHARM3_24_S | 3rd harmonic single ended(1) | w/o filtering; continuous wave at |  | -7.0 |  | dBm |
|  |  | maximal output power |  |  |  |  |
| PHARM4_24_S | 4th harmonic single ended(1) | w/o filtering; continuous wave at |  | -38.0 |  | dBm |
|  |  | maximal output power |  |  |  |  |
| PHARM5_24_S | 5th harmonic single ended(1) | w/o filtering; continuous wave at |  | -27.0 |  | dBm |
|  |  | maximal output power |  |  |  |  |


<!-- page 192 -->

Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, fchannel (500MHz band)=490MHz / fchannel (900MHz
band)=902MHz / fchannel (2.4GHz band)=2445MHz, maximum output power (PAC.TXPWR=31)

Table 10-11. FSK Modulation quality (frequency deviation, zero crossing)

  Symbol       Modulation   Modulation         500MHz Band                 900MHz Band                         2.4GHz Band
   Rate                       Index
                                          Freq. dev.   Zero cros.   Freq. dev.          Zero cros.       Freq. dev.      Zero cros.
[ksymbol/s]                                [% RMS]      [% peak]     [% RMS]             [% peak]         [% RMS]         [% peak]
     50           2FSK           1             4           1               3                  1               4                1
    100           2FSK          0.5            7           1               5                  2               7                2
    100           2FSK           1            11           1               7                  1               7                1
    150           2FSK          0.5           12           2               8                  2               6                3
    200           2FSK          0.5            9           3               6                  3               5                4
    300           2FSK          0.5           13           5               10                 5              10                5


Table 10-12 shows the typical OFDM error vector magnitude (EVM) values. The column P_RF max (maximum output
power at device pin) is the maximal (RMS) transmit power of OFDM signals measured at the device and the
PAC.TXPWR reflects the according register setting. Note, the maximum (RMS) transmit power of OFDM signals is
about 5.5dB lower compared to a constant envelope (CW signals). Refer to OFDM power charts in chapter "Output
Power at Several Modulations " on page 208.
Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, fchannel(500MHz band)=490MHz / fchannel (900MHz
band)=902MHz / fchannel (2.4GHz band)=2445MHz




                                                                            Atmel AT86RF215 - DATASHEET                            192
                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 193 -->

Table 10-12. EVM of MR-OFDM PHY mode

Option        MCS         IEEE EVM              500MHz band                      900MHz band                            2.4GHz band
                          spec [dB]      EVM     P_RFmax [dBm] /         EVM        P_RFmax [dBm] /           EVM         P_RFmax [dBm] /
                          [3]            [dB]    PAC.TXPWR               [dB]       PAC.TXPWR                 [dB]        PAC.TXPWR
1             0,1,2,3     -10             -18           12.0 / 31          -17            11.5 / 31               -15           10.5 / 31
1             4(1)        -13             -20          10.5 / 29(2)        -19           10.0 / 29(2)             -17          9.5 / 29(2)
1             5(1)        -16             -22          9.0 / 27(2)         -21            9.0 / 27(2)             -19          8.0 / 27(2)
1             6(1)        -19             -23          7.0 / 25(2)         -22            7.0 / 25(2)             -20          6.5 / 25(2)
2             0,1,2,3     -10             -18           12.0 / 31          -17            11.5 / 31               -15           10.5 / 31
2             4           -13             -20          10.5 / 29(2)        -19           10.0 / 29(2)             -17          9.5 / 29(2)
2             5           -16             -22          9.0 / 27(2)         -21            9.0 / 27(2)             -19          8.0 / 27(2)
2             6(1)        -19             -23          7.0 / 25(2)         -22            7.0 / 25(2)             -20          6.5 / 25(2)
3             1,2,3       -10             -18           12.0 / 31          -17            11.5 / 31               -15           10.5 / 31
3             4           -13             -20          10.5 / 29(2)        -19           10.0 / 29(2)             -17          9.5 / 29(2)
3             5           -16             -22          9.0 / 27(2)         -21            9.0 / 27(2)             -19          8.0 / 27(2)
3             6           -19             -23          7.0 / 25(2)         -22            7.0 / 25(2)             -20          6.5 / 25(2)
4             2,3         -10             -18           12.0 / 31          -17            11.5 / 31               -15           10.5 / 31
4             4           -13             -20          10.5 / 29(2)        -19           10.0 / 29(2)             -17          9.5 / 29(2)
4             5           -16             -22          9.0 / 27(2)         -21            9.0 / 27(2)             -19          8.0 / 27(2)
4             6           -19             -23          7.0 / 25(2)         -22            7.0 / 25(2)             -20          6.5 / 25(2)
Note:    1.             extended modes (proprietary)
         2.             See Table 6-91


Table 10-13 shows the typical OQPSK offset error vector magnitude (EVM) values according to [3].
Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, fchannel (500MHz band)=490MHz / fchannel (900MHz
band)=902MHz / fchannel (2.4GHz band)=2445MHz

Table 10-13. EVM of MR-OQPSK, legacy OQPSK

Chip                          500MHz band                             900MHz band                                 2.4GHz band
Rate
                  IQ Offset EVM       IQ Offset EVM      IQ Offset EVM       IQ Offset EVM            IQ Offset EVM         IQ Offset EVM
[kchip/s]              [%]                 [%]                [%]                  [%]                     [%]                    [%]
                      P_RF=             P_RFmax=             P_RF=             P_RFmax=                   P_RF=               P_RFmax=
                      0dBm               16dBm               0dBm               14.5dBm                   0dBm                 14.0dBm
100                       2                 1                    2                   1                       2                      1
200                       4                 2                    4                   2                       3                      2
1000                      6                 2                    5                   2                       10                     2
2000                      8                 3                    8                   3                       11                     3




                                                                                         Atmel AT86RF215 - DATASHEET                         193
                                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 194 -->

10.10 Receiver Characteristics

10.10.1 General Receiver Characteristics
       Test Conditions: TOP= 25°C, VDD= 3.0V

       Table 10-14. Receiver Characteristics for the 500MHz Band

        Symbol      Parameter                         Condition                             Min.        Typ.         Max.          Unit
        PRXmax_05   Maximum RX input level            fulfills PER limit                                 -5.0                      dBm
        NF05        Noise figure                                                                         4.3                       dB
        PSPUR_RX_05 Spurious emissions for 500MHz     30 ... ≤ 1000MHz                                               -57.0         dBm
                    band at maximum RX gain           >1 ... 12.75GHz                                                -47.0         dBm
        IIP305      3rd – order intercept point       At maximum gain                                   -13.0                      dBm
                                                      Offset freq. interf. 1 = 5MHz
                                                      Offset freq. interf. 2 = 10MHz
        RSSITOL_05 RSSI tolerance                     Tolerance within gain steps           -5.0                     +5.0          dB
        RSSIRANGE   RSSI dynamic range                                                                  117.0                      dB
        _05

        RSSIRES_05 RSSI resolution                                                                        1                        dB
        RSSISENS_   RSSI sensitivity                  100kHz signal bandwidth                          -117.0                      dBm
        05



       Table 10-15. Receiver Characteristics for the 900MHz Band

        Symbol      Parameter                         Condition                             Min.        Typ.         Max.          Unit
        PRXmax_09   Maximum RX input level            fulfills PER limit                                 -5.0                      dBm
        NF09        Noise figure                                                                         4.5                       dB
        PSPUR_RX_09 Spurious emissions for 900MHz     30 ... ≤ 1000MHz                                               -57.0         dBm
                    band at maximum RX gain           >1 ... 12.75GHz                                                -47.0         dBm
        IIP309      3rd – order intercept point       At maximum gain                                   -11.0                      dBm
                                                      Offset freq. interf. 1 = 5MHz
                                                      Offset freq. interf. 2 = 10MHz
        RSSITOL_09 RSSI tolerance                     Tolerance within gain step            -5.0                     +5.0          dB
        RSSIRANGE   RSSI dynamic range                                                                  117.0                      dB
        _09

        RSSIRES_09 RSSI resolution                                                                        1                        dB
        RSSISENS_   RSSI sensitivity                  100kHz signal bandwidth                          -117.0                      dBm
        09




       Table 10-16. Receiver Characteristics for the 2.4GHz Band

        Symbol      Parameter                         Condition                             Min.        Typ.         Max.          Unit
        PRXmax_24   Maximum RX input level            fulfills PER limits                                -5.0                      dBm
        NF24        Noise figure                                                                         4.3                       dB
        PSPUR_RX_24 Spurious emissions at maximum RX 30 ... ≤ 1000MHz                                                -57.0         dBm
                    gain                             >1 ... 12.75GHz                                                 -47.0         dBm
        IIP324      3rd – order intercept point       At maximum gain                                   -15.0                      dBm
                                                      Offset freq. interf. 1 = 5MHz
                                                      Offset freq. interf. 2 = 10MHz
        RSSITOL_24 RSSI tolerance                     Tolerance within gain step            -5.0                     +5.0          dB




                                                                                   Atmel AT86RF215 - DATASHEET                       194
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| PRXmax_05 | Maximum RX input level | fulfills PER limit |  | -5.0 |  | dBm |
| NF05 | Noise figure |  |  | 4.3 |  | dB |
| PSPUR_RX_05 | Spurious emissions for 500MHz band at maximum RX gain | 30 ... ≤ 1000MHz |  |  | -57.0 | dBm |
|  |  | >1 ... 12.75GHz |  |  | -47.0 | dBm |
| IIP305 | 3rd – order intercept point | At maximum gain |  | -13.0 |  | dBm |
|  |  | Offset freq. interf. 1 = 5MHz |  |  |  |  |
|  |  | Offset freq. interf. 2 = 10MHz |  |  |  |  |
| RSSITOL_05 | RSSI tolerance | Tolerance within gain steps | -5.0 |  | +5.0 | dB |
| RSSIRANGE | RSSI dynamic range |  |  | 117.0 |  | dB |
| _05 |  |  |  |  |  |  |
| RSSIRES_05 | RSSI resolution |  |  | 1 |  | dB |
| RSSISENS_ | RSSI sensitivity | 100kHz signal bandwidth |  | -117.0 |  | dBm |
| 05 |  |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| PRXmax_09 | Maximum RX input level | fulfills PER limit |  | -5.0 |  | dBm |
| NF09 | Noise figure |  |  | 4.5 |  | dB |
| PSPUR_RX_09 | Spurious emissions for 900MHz band at maximum RX gain | 30 ... ≤ 1000MHz |  |  | -57.0 | dBm |
|  |  | >1 ... 12.75GHz |  |  | -47.0 | dBm |
| IIP309 | 3rd – order intercept point | At maximum gain |  | -11.0 |  | dBm |
|  |  | Offset freq. interf. 1 = 5MHz |  |  |  |  |
|  |  | Offset freq. interf. 2 = 10MHz |  |  |  |  |
| RSSITOL_09 | RSSI tolerance | Tolerance within gain step | -5.0 |  | +5.0 | dB |
| RSSIRANGE | RSSI dynamic range |  |  | 117.0 |  | dB |
| _09 |  |  |  |  |  |  |
| RSSIRES_09 | RSSI resolution |  |  | 1 |  | dB |
| RSSISENS_ | RSSI sensitivity | 100kHz signal bandwidth |  | -117.0 |  | dBm |
| 09 |  |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| PRXmax_24 | Maximum RX input level | fulfills PER limits |  | -5.0 |  | dBm |
| NF24 | Noise figure |  |  | 4.3 |  | dB |
| PSPUR_RX_24 | Spurious emissions at maximum RX gain | 30 ... ≤ 1000MHz |  |  | -57.0 | dBm |
|  |  | >1 ... 12.75GHz |  |  | -47.0 | dBm |
| IIP324 | 3rd – order intercept point | At maximum gain |  | -15.0 |  | dBm |
|  |  | Offset freq. interf. 1 = 5MHz |  |  |  |  |
|  |  | Offset freq. interf. 2 = 10MHz |  |  |  |  |
| RSSITOL_24 | RSSI tolerance | Tolerance within gain step | -5.0 |  | +5.0 | dB |


<!-- page 195 -->

        Symbol        Parameter                          Condition                            Min.        Typ.         Max.          Unit
        RSSIRANGE     RSSI dynamic range                                                                  117.0                      dB
        _24

        RSSIRES_24 RSSI resolution                                                                          1                        dB
        RSSISENS_     RSSI sensitivity                   100kHz signal bandwidth                         -117.0                      dBm
        24




10.10.2 Receiver Sensitivity
       Table 10-17 shows the typical receiver sensitivity for MR-FSK PHY modes.
       Test Conditions: TOP= 25°C, VDD= 3.0V, fchannel (sub-1GHz)=868MHz/ fchannel (2.4GHz)=2440MHz, ideal receiver input,
       clock source=TCXO, BT=2.0.

       Table 10-17. Receiver Sensitivity for MR-FSK

          Symbol         Modulation      Modulation     FEC        Receiver         Receiver       Condition/Note
           Rate                            Index      (NRNSC)     Sensitivity      Sensitivity
        [ksymbol/s]                                    and ILV    sub-1GHz           2.4GHz
                                                                    [dBm]            [dBm]
              50            2FSK             1          yes          -114             -115         Preamble length 8 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              50            2FSK             1          no           -109             -110
              100           2FSK            0.5         yes          -109             -110         Preamble length 8 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              100           2FSK            0.5         no           -103             -104
              100           2FSK             1          yes          -111             -112         Preamble length 8 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              100           2FSK             1          no           -106             -107
              150           2FSK            0.5         yes          -108             -109         Preamble length 12 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              150           2FSK            0.5         no           -102             -103
              200           2FSK            0.5         yes          -107             -107         Preamble length 16 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              200           2FSK            0.5         no           -102             -102
              300           2FSK            0.5         yes          -106             -106         Preamble length 24 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              300           2FSK            0.5         no           -100             -101
              100           4FSK            1.0         yes          -107             -107         Preamble length16 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              100           4FSK            1.0         no            -99             -99
              200           4FSK            1.0         yes          -104             -104         Preamble length 32 octets; PSDU
                                                                                                   length 250 octets; PER < 10%
              200           4FSK            1.0         no            -96             -95


       Table 10-18 shows the typical receiver sensitivity for MR-OFDM PHY modes.
       Test Conditions: TOP= 25°C, VDD= 3.0V, fchannel (sub-1GHz)=868MHz / fchannel (2.4GHz)=2440MHz , ideal receiver input
       signal, clock source=TCXO.




                                                                                     Atmel AT86RF215 - DATASHEET                       195
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 196 -->

Table 10-18. Receiver Sensitivity for MR-OFDM

Option    MCS               PSDU Data Rate        Receiver              Receiver              Condition/Note
                            [kb/s]                Sensitivity           Sensitivity
                                                  sub-1GHz [dBm]        2.4GHz [dBm]
   1            0                  100                    -109                -112            PSDU length 250 octets; PER < 10%
   1            1                  200                    -109                -110
   1            2                  400                    -107                -107
   1            3                  800                    -104                -105
   1           4(1)                1200                   -101                -102
   1           5(1)                1600                   -97                 -98
                   (1)
   1           6                   2400                   -92                 -93
   2            0                   50                    -111                -113
   2            1                  100                    -111                -112
   2            2                  200                    -108                -109
   2            3                  400                    -106                -107
   2            4                  600                    -104                -104
   2            5                  800                    -101                -102
   2           6(1)                1200                   -96                 -96
   3            1                   50                    -113                -113
   3            2                  100                    -109                -110
   3            3                  200                    -107                -108
   3            4                  300                    -106                -107
   3            5                  400                    -102                -103
   3            6                  600                    -97                 -98
   4            2                   50                    -111                -112
   4            3                  100                    -109                -110
   4            4                  150                    -108                -109
   4            5                  200                    -105                -106
   4            6                  300                    -101                -102
 Notes:   1.             extended mode (proprietary)
Table 10-19 shows the typical receiver sensitivity for MR-O-QPSK and legacy O-QPSK PHY modes.
Test Conditions: TOP= 25°C, VDD= 3.0V, fchannel (sub-1GHz)=868MHz / fchannel (2.4GHz)=2440MHz , ideal receiver input
signal, clock source=TCXO

Table 10-19. Receiver Sensitivity for MR-O-QPSK

 Chip Rate               Rate       PSDU Data             Receiver            Receiver          Condition/Note
 [kchip/s]               Mode       Rate [kb/s]          Sensitivity         Sensitivity
                                                       sub-1GHz [dBm]      2.4GHz [dBm]
    100                    0              6.25              -123               -123
    100                    1              12.5              -121               -121             PSDU length 20 octets; PER < 10%
    100                    2              25                -119               -119
    100                    3              50                -117               -117             PSDU length 250 octets; PER < 10%



                                                                                       Atmel AT86RF215 - DATASHEET                     196
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 197 -->

Chip Rate   Rate   PSDU Data        Receiver         Receiver         Condition/Note
[kchip/s]   Mode   Rate [kb/s]     Sensitivity      Sensitivity
                                 sub-1GHz [dBm]   2.4GHz [dBm]
  200        0        12.5            -121            -121
                                                                      PSDU length 20 octets; PER < 10%
  200        1         25             -119            -119
  200        2         50             -116            -116
                                                                      PSDU length 250 octets; PER < 10%
  200        3        100             -115            -115
  1000       0       31.25            -117            -117            PSDU length 20 octets; PER < 10%
  1000       1        125             -112            -112
  1000       2        250             -110            -110            PSDU length 250 octets; PER < 10%
  1000       3        500             -108            -108
  1000      Leg       250             -103            -103            PSDU length 20 octets; PER < 1%,
  1000      Leg       500             -101            -102            PSDU length 20 octets; PER < 1%;
                                                                      Proprietary
  2000       0       31.25            -116            -116            PSDU length 20 octets; PER < 10%
  2000       1        125             -110            -110
  2000       2        250             -108            -109            PSDU length 250 octets; PER < 10%
  2000       3        500             -107            -107
  2000       4        1000            -106            -105            PSDU length 250 octets; PER < 10%;
                                                                      Proprietary
  2000      Leg       250             -103            -104            PSDU length 20 octets; PER < 1%
  2000      Leg       1000            -96              -96            PSDU length 20 octets; PER < 1%;
                                                                      Proprietary




                                                             Atmel AT86RF215 - DATASHEET                     197
                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 198 -->

10.10.3 Adjacent Channel Rejection
       Table 10-20 through Table 10-22 show the typical (alternate) adjacent channel rejection values for MR-FSK PHY
       modes.
       Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity
       [3], desired input signal is a transmitted signal from AT86RF215, interferer is an un-modulated carrier, fchannel =868MHz,
       measurements according to [3].

       Table 10-20. Adjacent Channel Rejection Values for MR-FSK at sub-1GHz according to [3]

        Symbol Rate       Modulation    Modulation     ACI/AACI             Condition/Note
        [ksymbol/s]                     Index          Rejection [dB]
              50             2FSK            1               45/52          Channel spacing 200kHz; PER < 10%
             100             2FSK           0.5              41/48
             100             2FSK            1               43/51          Channel spacing 400kHz; PER < 10%
             150             2FSK           0.5              42/49
             200             2FSK           0.5              42/ 47
             200             2FSK           1.0              44/ 50         Channel spacing 600kHz; PER < 10%
             300             2FSK           0.5              42/49
             100             4FSK            1               41/50          Channel spacing 400kHz; PER < 10%


       Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity
       [3], desired input signal is a transmitted signal from AT86RF215, interferer is an un-modulated carrier, fchannel
       =2440MHz, measurements according to [3].

       Table 10-21. Adjacent Channel Rejection Values for MR-FSK at 2.4GHz according to [3]

        Symbol Rate       Modulation    Modulation     ACI/AACI             Condition/Note
        [ksymbol/s]                     Index          Rejection [dB]
              50             2FSK            1               38/44          Channel spacing 200kHz; PER < 10%
             100             2FSK            1               40/45          Channel spacing 400kHz; PER < 10%
             150             2FSK           0.5              38/42
             200             2FSK           0.5              35/42
             300             2FSK           0.5              31/41          Channel spacing 600kHz; PER < 10%




                                                                                    Atmel AT86RF215 - DATASHEET                     198
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 199 -->

Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity
[3], desired input signal is a transmitted signal from AT86RF215, interferer is an un-modulated carrier, fchannel =868MHz,
FEC disabled, measurements according to [5].

Table 10-22. Adjacent Channel Rejection Values for MR-FSK at sub-1GHz according to [5]

Symbol Rate        Modulation    Modulation     Interference          Condition/Note
[ksymbol/s]                      Index          rejection [dB]
                                                df=200/400/600kHz
       50             2FSK            1              45/52/57         PER < 10%
       100            2FSK           0.5             42/48/52
       150            2FSK           0.5             26/41/46
       100            4FSK           1.0             19/42/47


Table 10-23 shows the typical adjacent channel rejection values for MR-OFDM.
Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity
[3], desired input signal is a transmitted signal from AT86RF215, interferer is a modulated signal, fchannel (sub-
1GHz)=868MHz, fchannel (2.4GHz)=2440MHz, measurements according to [3].

Table 10-23. Adjacent Channel Rejection Values for MR-OFDM according to [3]

Option       MCS   PSDU         ACI / AACI         ACI / AACI       Condition/Note
                   Data Rate    Rejection          Rejection
                   [kb/s]       sub-1GHz [dB]      2.4GHz [dB]
   1          0       100            24/58             23/51
   1          1       200            24/55             23/49
                                                                    Channel spacing 1.2MHz; PER < 10%
   1          2       400            24/52             22/45
   1          3       800            21/48             20/44
   1          4      1200            12/45             12/41
   1          5      1600            13/43             13/41        Channel spacing 1.2MHz; PER < 10%; Proprietary
   1          6      2400             5/42              3/38
   2          0       50             51/62             47/57
   2          1       100            50/60             46/55
   2          2       200            47/57             43/52
                                                                    Channel spacing 800kHz; PER < 10%
   2          3       400            44/54             40/49
   2          4       600            40/51             37/46
   2          5       800            37/48             39/45
   2          6      1200            33/45             32/40        Channel spacing 800kHz; PER < 10%; Proprietary
   3          1       50             46/61             29/53
   3          2       100            46/58             29/50
   3          3       200            44/56             29/48
                                                                    Channel spacing 400kHz; PER < 10%
   3          4       300            38/53             29/46
   3          5       400            38/50             28/43
   3          6       600            32/46             25/39




                                                                             Atmel AT86RF215 - DATASHEET                     199
                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 200 -->

Option    MCS       PSDU            ACI / AACI      ACI / AACI       Condition/Note
                    Data Rate       Rejection       Rejection
                    [kb/s]          sub-1GHz [dB]   2.4GHz [dB]
   4        2          50               19/52            18/47
   4        3          100              19/53            18/45
   4        4          150              18/51            16/41       Channel spacing 200kHz; PER < 10%
   4        5          200              18/48            18/40
   4        6          300              14/43            9/35


The following table shows the typical adjacent channel rejection values for MR-O-QPSK.
Test Conditions: AT86RF215 v.3, TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity
[3], interferer is a modulated signal, fchannel (sub-1GHz)=868MHz, fchannel (2.4GHz)=2440MHz, measurements according
to [3].

Table 10-24. Adjacent Channel Rejection Values for MR-O-QPSK

Chip Rate       Rate        PSDU Data Rate      ACI / AACI        ACI / AACI          Condition/Note
[kchip/s]       Mode        [kb/s]              Rejection         Rejection
                                                sub-1GHz [dB]     2.4GHz [dB]
100             0           6.25                59/60             52/55               Channel spacing 200kHz; PER < 10%
100             1           12.5                57/59             50/54
100             2           25                  53/57             47/51
100             3           50                  49/55             43/49
200             0           12.5                60/68             52/60               Channel spacing 400kHz; PER < 10%
200             1           25                  56/65             51/59
200             2           50                  51/60             45/53
200             3           100                 48/55             47/49
1000            0           31.25               61/>70            52/63               Channel spacing 2MHz; PER < 10%
1000            1           125                 60/63             51/58
1000            2           250                 56/64             50/57
1000            3           500                 52/61             43/55
2000            0           31.25               67/>70            60/>70              Channel spacing 5MHz; PER < 10%
2000            1                               61/68             54/63
2000            2                               58/67             55/61
2000            3           500                 56/64             53/59
2000            4           1000                58/62             49/58               Channel spacing 5MHz; PER < 10%;
                                                                                      Proprietary
1000            Leg         250                 46/53             40/46               Channel spacing 2MHz; PER < 1%
2000            Leg         250                 53/60             47/52               Channel spacing 5MHz; PER < 1%




                                                                            Atmel AT86RF215 - DATASHEET                        200
                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 201 -->

10.10.4 Blocking
       Table 10-25 shows the blocking parameter for MR-FSK PHY modes.
       Test Conditions: TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity [3], desired input
       signal is a transmitted signal from AT86RF215, interferer is generated by a signal generator, fchannel (sub-
       1GHz)=868MHz, measurements according to [6].

       Table 10-25. Blocking parameter for MR-FSK according to [6]

        Symbol Rate           Modulation   Modulation   Blocking at        Condition/Note
        [ksymbol/s]                        Index        ±2MHz/±10MHz
                                                        [dB]
              50                2FSK              1          61/69         RX bandwidth 160kHz
              100               2FSK              0.5        57/65         RX bandwidth 200kHz
              100               2FSK              1          58/66         RX bandwidth 320kHz
              150               2FSK              0.5        55/63         RX bandwidth 320kHz
              200               2FSK              0.5        54/61         RX bandwidth 320kHz
              200               2FSK              1.0        56/63         RX bandwidth 500kHz
              300               2FSK              0.5        52/59         RX bandwidth 500kHz
              100               4FSK              1          48/55         RX bandwidth 320kHz


       Table 10-26 shows the blocking parameter for MR-OFDM.
       Test Conditions: TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity [3], desired input
       signal is a transmitted signal from AT86RF215, interferer is generated by a signal generator, fchannel (sub-
       1GHz)=868MHz, measurements according to [6].

       Table 10-26. Blocking parameter for MR-OFDM according to [6]

        Option      MCS            PSDU Data Rate       Blocking at       Condition/Note
                                   [kb/s]               ±2MHz/±10MHz
                                                        [dB]
          1               0                100              47/65         RX bandwidth 1250kHz
          1               1                200              47/65
          1               2                400              47/64
          1               3                800              45/63
          1               4                1200             43/60
          1               5                1600             43/57
          1               6                2400             43/51
          2               0                 50              54/70         RX bandwidth 800kHz
          2               1                100              54/70
          2               2                200              54/68
          2               3                400              54/66
          2               4                600              53/63
          2               5                800              52/60
          2               6                1200             47/54
          3               1                 50              65/72         RX bandwidth 400kHz



                                                                                  Atmel AT86RF215 - DATASHEET                      201
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 202 -->

Option    MCS            PSDU Data Rate        Blocking at         Condition/Note
                         [kb/s]                ±2MHz/±10MHz
                                               [dB]
   3            2               100                    62/69
   3            3               200                    60/67
   3            4               300                    58/65
   3            5               400                    55/62
   3            6               600                    50/57
   4            2                50                    64/71       RX bandwidth 250kHz
   4            3               100                    62/69
   4            4               150                    61/68
   4            5               200                    57/64
   4            6               300                    53/60


Table 10-27 shows the blocking parameter for MR-O-QPSK.
Test Conditions: TOP= 25°C, VDD= 3.0V, desired signal power 3dB above specified receiver sensitivity [3], desired input
signal is a transmitted signal from AT86RF215, interferer is generated by a signal generator, fchannel (sub-
1GHz)=868MHz, measurements according to [6].

Table 10-27. Blocking parameter for MR-O-QPSK according to [6]

Chip Rate     Rate      PSDU Data Rate         Blocking at         Condition/Note
[kchip/s]     Mode      [kb/s]                 ±2MHz/±10MHz
                                               [dB]
100           0         6.25                   73/80               RX bandwidth 160kHz
100           3         50                     70/76
200           0         12.5                   70/77               RX bandwidth 250kHz
200           3         100                    67/73
1000          0         31.25                  53/72               RX bandwidth 1000kHz
1000          3         500                    49/66
2000          0         31.25                  37/71               RX bandwidth 2000kHz
2000          3         500                    37/64
2000          4         1000                   37/63
1000          Leg       250                    46/63               RX bandwidth 1000kHz
2000          Leg       250                    34/63               RX bandwidth 2000kHz




                                                                           Atmel AT86RF215 - DATASHEET                      202
                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 203 -->

10.11 Current Consumption Specifications
     Test Conditions: TOP = 25°C, VDD = 3.0V, CLKO = OFF

     Table 10-28. Current Consumption Specifications

      Symbol        Parameter                            Condition                           Min.        Typ.         Max.          Unit
      IDEEP_SLEEP   Supply current in DEEP_SLEEP                                                           30                       nA
                    state
      ITRXOFF       Supply current TRXOFF state                                                            3                        mA
      IRX09         Supply current RX state for Sub-     Sub-1GHz transceiver @ RX                         28                       mA
                    1GHz transceiver                     state and 2.4GHz transceiver @
                                                         sleep state
                                                         MR-2FSK-50ksymbols/s
      IRX09_FSK_    Supply current RX state for Sub-     Sub-1GHz transceiver @ RX                         15                       mA
      RPC1:1        1GHz transceiver using MR-FSK        state and 2.4GHz transceiver @
                    reduced power consumption mode       sleep state
                    (RPC) with on:off time = 1:1         MR-2FSK 50ksymbols/s
                                                         MR-FSK RPC with on:off time
                                                         1:1 may cause a sensitivity loss
                                                         of up to 0.5dB
      IRX09_FSK_    Supply current RX state for Sub-     Sub-1GHz transceiver @ RX                         5                        mA
      RPC1:16       1GHz transceiver using MR-FSK        state and 2.4GHz transceiver @
                    reduced power consumption mode       sleep state
                    (RPC) with on:off time = 1:16        MR-2FSK 50ksymbols/s
                                                         MR-FSK RPC with on:off time
                                                         1:16 may cause a sensitivity
                                                         loss of up to 1.0dB
      IRX09_        Supply current RX state for Sub-     Sub-1GHz transceiver @ RX                         17                       mA
      OQPSK_RPC     1GHz transceiver using MR-OQPSK      state and 2.4GHz transceiver @
                    reduced power consumption mode       sleep state
                    (RPC)                                MR-OQPSK: Chiprate
                                                         100kbit/s, Rate mode 0
                                                         MR-OQPSK RPC may cause a
                                                         sensitivity loss of up to 0.5dB
      IRX24         Supply current RX state for 2.4GHz   2.4GHz transceiver @ RX state                     33                       mA
                    transceiver                          and Sub-1GHz transceiver @
                                                         sleep state
                                                         MR-2FSK-50ksymbols/s
      IRX24_FSK_    Supply current RX state for 2.4GHz   2.4GHz transceiver @ RX state                     16                       mA
      RPC1:1        transceiver using MR-FSK reduced     Sub-1GHz transceiver @ sleep
                    power consumption mode (RPC)         state
                    with on:off time = 1:1               MR-2FSK 50ksymbols/s
                                                         MR-FSK RPC with on:off time
                                                         1:16 may cause a sensitivity
                                                         loss of up to 0.5dB
      IRX24_FSK_    Supply current RX state for 2.4GHz   2.4GHz transceiver @ RX state                     5                        mA
      RPC1:16       transceiver using MR-FSK reduced     Sub-1GHz transceiver @ sleep
                    power consumption mode (RPC)         state
                    with on:off time = 1:16              MR-2FSK 50ksymbols/s
                                                         MR-FSK RPC with on:off time
                                                         1:16 may cause a sensitivity
                                                         loss of up to 1.0dB




                                                                                    Atmel AT86RF215 - DATASHEET                       203
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 204 -->

      Symbol       Parameter                            Condition                            Min.        Typ.         Max.          Unit
      IRX24_       Supply current RX state for 2.4GHz   2.4GHz transceiver @ RX state                      18                       mA
      OQPSK_RPC    transceiver using MR-OQPSK           and Sub-1GHz transceiver @
                   reduced power consumption mode       sleep state
                   (RPC)
      ITX09        Supply current TX state for Sub-     Sub-1GHz transceiver @ TX                          64                       mA
                   1GHz transceiver                     state and 2.4GHz transceiver @
                   see Figure 11-9                      sleep state
                                                        MR-2FSK 50ksymbols/s
                                                        fchannel=900MHz
                                                        PAC.TXPWR= 31
                                                        PAC.PACUR=2
      ITX24        Supply current TX state for 2.4GHz   2.4GHz transceiver @ TX state                      62                       mA
                   transceiver                          and Sub-1GHz transceiver @
                   see Figure 11-11                     sleep state
                                                        MR-2FSK 50ksymbols/s
                                                        fchannel=2445MHz
                                                        PAC.TXPWR= 31
                                                        PAC.PACUR=2;
      IIQIF_RX1    Supply current for RX I/Q interface  One differential RX data stream                    6                        mA
                   driver: The current must be added to RXD and one differential clock
                   the RX state current in case one I/Q RXCLK is running
                   driver interface is used.
      IIQIF_RX2    Supply current for 2 RX I/Q interface Two differential RX data stream                   9                        mA
                   drivers: The current must be added RXD and one differential clock
                   to the RX state current in case both RXCLK is running
                   I/Q driver interfaces are used.
      IIQIF_TX     Supply current for TX I/Q interface One differential TX data stream                     3                        mA
                   receiver: The current must be added TXD and one differential clock
                   to the TX state current in case the TXCLK is running
                   I/Q receive interface is used.
      IVREG        Current consumption of AVDD or                                             60           80         120           μA
                   DVDD voltage regulator




10.12 SPI Timing Characteristics
      Test Conditions: TOP= 85°C, VDD= 1.8V, CLOAD=35pF, pad driver strength set to default (unless otherwise stated).

      Table 10-29. SPI Timing Characteristics

      Symbol       Parameter                            Condition                            Min.        Typ.         Max.          Unit
      fSCLK        SCLK frequency                                                                          25                       MHz
      tSPI_0       SELN falling edge to SCLK rising                                           50                                    ns
                   edge
      tSPI_1       SELN falling edge to MISO active                                                                    25           ns
      tSPI_2       SCLK falling edge to MISO out        data delay time                        5                       19           ns
                                                        C_LOAD=35pF and default pad
                                                        driver strength
      tSPI_3       MOSI setup time                                                             5                                    ns
      tSPI_4       MOSI hold time                                                              5                                    ns
      tSPI_5       LSB last byte to MSB next byte       SPI read/write                        125                                   ns
      tSPI_6       SELN rising edge to MISO tri state                                                                  10           ns



                                                                                   Atmel AT86RF215 - DATASHEET                        204
                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| fSCLK | SCLK frequency |  |  | 25 |  | MHz |
| tSPI_0 | SELN falling edge to SCLK rising edge |  | 50 |  |  | ns |
|  |  |  |  |  |  |  |
| tSPI_1 | SELN falling edge to MISO active |  |  |  | 25 | ns |
| tSPI_2 | SCLK falling edge to MISO out | data delay time | 5 |  | 19 | ns |
|  |  | C_LOAD=35pF and default pad |  |  |  |  |
|  |  | driver strength |  |  |  |  |
| tSPI_3 | MOSI setup time |  | 5 |  |  | ns |
| tSPI_4 | MOSI hold time |  | 5 |  |  | ns |
| tSPI_5 | LSB last byte to MSB next byte | SPI read/write | 125 |  |  | ns |
| tSPI_6 | SELN rising edge to MISO tri state |  |  |  | 10 | ns |


<!-- page 205 -->

      Symbol       Parameter                              Condition                            Min.        Typ.         Max.          Unit
      tSPI_8       SPI idle time SELN rising to falling   SPI read/write, idle time             50                                    ns
                   edge                                   between consecutive SPI
                                                          access
      tSPI_9       Last SCLK rising edge to SELN                                                45                                    ns
                   rising edge




10.13 I/Q Data Interface Driver DC and Startup Specification
      The DC specification for the LVDS driver of the I/Q data interface is given in the following tables. The general
      measurement conditions are described in [4] on page 231. However, some adaptations are required due to the specific
      signal levels of the proprietary interface. The parameters are valid for an output current of 2mA (see register RF_IQIFC0
      on page 27).

      Table 10-30. I/Q Data Interface Driver DC and Startup Specification (proprietary mode)

      Symbol       Parameter                              Condition                            Min.        Typ.         Max.          Unit
      Voh          Output voltage, Voa or Vob             Rload = 100Ω, +/-1%                                           385           mV
      Vol          Output voltage, Voa or Vob             Rload = 100Ω, +/-1%                    0                                    mV
      |Vod|        Output differential voltage            Rload = 100Ω, +/-1%                   100         200         270           mV
      Vos          Output common mode voltage             Rload = 100Ω, +/-1%                   80          200         270           mV
      RO           Output impedance single ended          Vcm = 300mV, 100mV                    40           50          63            Ω
      ∆RO          RO mismatch between A and B            Rload = 100Ω, +/-1%                                            10            %
      |∆Vod|       Change of |Vod| between “0” and “1”    Rload = 100Ω, +/-1%                                            35           mV
      ∆Vos         Change in Vos between “0” and “1”      Rload = 100Ω, +/-1%                                            35           mV
      Isa          Output current                         Driver shorted to ground                                       10           mA
      Isb          Output current                         Driver shorted to ground                                       10           mA
      Isab         Output current                         Driver outputs shorted together.                                3           mA
      tstartupD    Startup time from enable until LVDS                                                                   10           μs
                   is ready to drive

      Table 10-31. I/Q Data Interface Driver DC and Startup Specification (IEEE mode, reduced range link)

      Symbol       Parameter                              Condition                            Min.        Typ.         Max.          Unit
      Voh          Output voltage, Voa or Vob             Rload = 100Ω, +/-1%                                           1375          mV
      Vol          Output voltage, Voa or Vob             Rload = 100Ω, +/-1%                  1025                                   mV
      |Vod|        Output differential voltage            Rload = 100Ω, +/-1%                               200                       mV
      Vos          Output common mode voltage             Rload = 100Ω, +/-1%                              1200                       mV
      RO           Output impedance single ended          Vcm = 300mV, 100mV                    40                      140            Ω
      ∆RO          RO mismatch between A and B            Rload = 100Ω, +/-1%                                            10            %
      |∆Vod|       Change of |Vod| between “0” and “1”    Rload = 100Ω, +/-1%                                            35           mV
      ∆Vos         Change in Vos between “0” and “1”      Rload = 100Ω, +/-1%                                            35           mV
      Isa          Output current                         Driver shorted to ground                                       10           mA
      Isb          Output current                         Driver shorted to ground                                       10           mA
      Isab         Output current                         Driver outputs shorted together.                                3           mA
      tstartupD    Startup time from enable until LVDS                                                                   10           μs
                   is ready to drive




                                                                                      Atmel AT86RF215 - DATASHEET                          205
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Voh | Output voltage, Voa or Vob | Rload = 100Ω, +/-1% |  |  | 385 | mV |
| Vol | Output voltage, Voa or Vob | Rload = 100Ω, +/-1% | 0 |  |  | mV |
| \|Vod\| | Output differential voltage | Rload = 100Ω, +/-1% | 100 | 200 | 270 | mV |
| Vos | Output common mode voltage | Rload = 100Ω, +/-1% | 80 | 200 | 270 | mV |
| RO | Output impedance single ended | Vcm = 300mV, 100mV | 40 | 50 | 63 | Ω |
| ∆RO | RO mismatch between A and B | Rload = 100Ω, +/-1% |  |  | 10 | % |
| \|∆Vod\| | Change of \|Vod\| between “0” and “1” | Rload = 100Ω, +/-1% |  |  | 35 | mV |
| ∆Vos | Change in Vos between “0” and “1” | Rload = 100Ω, +/-1% |  |  | 35 | mV |
| Isa | Output current | Driver shorted to ground |  |  | 10 | mA |
| Isb | Output current | Driver shorted to ground |  |  | 10 | mA |
| Isab | Output current | Driver outputs shorted together. |  |  | 3 | mA |
| tstartupD | Startup time from enable until LVDS |  |  |  | 10 | μs |
|  | is ready to drive |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Voh | Output voltage, Voa or Vob | Rload = 100Ω, +/-1% |  |  | 1375 | mV |
| Vol | Output voltage, Voa or Vob | Rload = 100Ω, +/-1% | 1025 |  |  | mV |
| \|Vod\| | Output differential voltage | Rload = 100Ω, +/-1% |  | 200 |  | mV |
| Vos | Output common mode voltage | Rload = 100Ω, +/-1% |  | 1200 |  | mV |
| RO | Output impedance single ended | Vcm = 300mV, 100mV | 40 |  | 140 | Ω |
| ∆RO | RO mismatch between A and B | Rload = 100Ω, +/-1% |  |  | 10 | % |
| \|∆Vod\| | Change of \|Vod\| between “0” and “1” | Rload = 100Ω, +/-1% |  |  | 35 | mV |
| ∆Vos | Change in Vos between “0” and “1” | Rload = 100Ω, +/-1% |  |  | 35 | mV |
| Isa | Output current | Driver shorted to ground |  |  | 10 | mA |
| Isb | Output current | Driver shorted to ground |  |  | 10 | mA |
| Isab | Output current | Driver outputs shorted together. |  |  | 3 | mA |
| tstartupD | Startup time from enable until LVDS |  |  |  | 10 | μs |
|  | is ready to drive |  |  |  |  |  |


<!-- page 206 -->

10.14 I/Q Data Interface Receiver DC and Startup Specification
      The DC specification for the LVDS receiver of the I/Q data interface is given in the following tables. The general
      measurement conditions are described in [4] on page 231. However, some adaptations are required due to the specific
      signal levels of the proprietary interface. See Figure 4-9 on page 23 for the definition of Vgdp (voltage difference of
      ground potentials).

      Table 10-32. I/Q Data Interface Receiver DC and Startup Specification (proprietary mode)

       Symbol         Parameter                             Condition                            Min.        Typ.         Max.          Unit
       Vi             Input voltage, Via or Vib             |Vgdp| < 50mV (driver receiver         0                      435           mV
                                                            ground potential difference)
       Vidth          Input differential threshold          |Vgdp| < 50mV                         -70                      70           mV
       Vhyst          Input differential voltage                                                  25                                    mV
       Rin            Receiver differential input                                                 80          100         125            Ω
                      impedance
       tstartupR      Startup time from enable until LVDS                                                                   1           μs
                      is ready to receive

      Table 10-33. I/Q Data Interface Receiver DC and Startup Specification (IEEE mode, reduced range link)

       Symbol         Parameter                             Condition                            Min.        Typ.         Max.          Unit
       Vi             Input voltage, Via or Vib             |Vgdp| < 50mV (driver receiver        825                     1575          mV
                                                            ground potential difference)
       Vidth          Input differential threshold          |Vgdp| < 50mV                        -100                     100           mV
       Vhyst          Input differential voltage                                                  25                                    mV
       Rin            Receiver differential input                                                 80          100         125            Ω
                      impedance
       tstartupR      Startup time from enable until LVDS                                                                   1           μs
                      is ready to receive




10.15 I/Q Data Interface Driver AC Specification
      The following tables summarize the dynamic parameters of the LVDS driver of the I/Q data interface. The reference of
      skew value is the RXCLK channel (see also section "Characteristics and Timing" on page 23). AC parameter for
      proprietary and IEEE mode are identical.

      Table 10-34. I/Q Data Interface Driver AC Specification

       Symbol         Parameter                             Condition                            Min.        Typ.         Max.          Unit
       Clock          RXCLK duty cycle                      f = 64MHz                             45           50          55            %
       tfall          Vod fall time 20..80%                 Zload = 100Ω, +/-1 %                                           2.3          ns
       trise          Vod rise time 20..80%                 Zload = 100Ω, +/-1 %                                           2.3          ns
       tskewD1        Differential skew                     any differential pair                                         200           ps
       tskewD2        LVDS data channel to LVDS data        Data to data                                                  500           ps
                      channel skew
       tD CLK-DATA_   Delay clock to data for               SKEWDRV=0x0, 1.906ns                  0.5         1.9          3.1          ns
       RX             RXD09/RXD24 outputs                   SKEWDRV=0x1, 2.906ns                  1.9         2.9          3.9          ns
                                                            SKEWDRV=0x2, 3.906ns                  2.9         3.9          4.9          ns
                                                            (default)
                                                            SKEWDRV=0x3, 4.906ns                  3.9         4.9          5.9          ns




                                                                                       Atmel AT86RF215 - DATASHEET                           206
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Vi | Input voltage, Via or Vib | \|Vgdp\| < 50mV (driver receiver | 0 |  | 435 | mV |
|  |  | ground potential difference) |  |  |  |  |
| Vidth | Input differential threshold | \|Vgdp\| < 50mV | -70 |  | 70 | mV |
| Vhyst | Input differential voltage |  | 25 |  |  | mV |
| Rin | Receiver differential input impedance |  | 80 | 100 | 125 | Ω |
|  |  |  |  |  |  |  |
| tstartupR | Startup time from enable until LVDS is ready to receive |  |  |  | 1 | μs |
|  |  |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Vi | Input voltage, Via or Vib | \|Vgdp\| < 50mV (driver receiver | 825 |  | 1575 | mV |
|  |  | ground potential difference) |  |  |  |  |
| Vidth | Input differential threshold | \|Vgdp\| < 50mV | -100 |  | 100 | mV |
| Vhyst | Input differential voltage |  | 25 |  |  | mV |
| Rin | Receiver differential input impedance |  | 80 | 100 | 125 | Ω |
|  |  |  |  |  |  |  |
| tstartupR | Startup time from enable until LVDS is ready to receive |  |  |  | 1 | μs |
|  |  |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Clock | RXCLK duty cycle | f = 64MHz | 45 | 50 | 55 | % |
| tfall | Vod fall time 20..80% | Zload = 100Ω, +/-1 % |  |  | 2.3 | ns |
| trise | Vod rise time 20..80% | Zload = 100Ω, +/-1 % |  |  | 2.3 | ns |
| tskewD1 | Differential skew | any differential pair |  |  | 200 | ps |
| tskewD2 | LVDS data channel to LVDS data channel skew | Data to data |  |  | 500 | ps |
|  |  |  |  |  |  |  |
| tD CLK-DATA_ RX | Delay clock to data for RXD09/RXD24 outputs | SKEWDRV=0x0, 1.906ns | 0.5 | 1.9 | 3.1 | ns |
|  |  | SKEWDRV=0x1, 2.906ns | 1.9 | 2.9 | 3.9 | ns |
|  |  | SKEWDRV=0x2, 3.906ns | 2.9 | 3.9 | 4.9 | ns |
|  |  | (default) |  |  |  |  |
|  |  | SKEWDRV=0x3, 4.906ns | 3.9 | 4.9 | 5.9 | ns |


<!-- page 207 -->

      Symbol       Parameter                              Condition                             Min.        Typ.         Max.          Unit
      tjitter      RXCLK jitter                                                                                          100           ps

      Figure 10-1. Definition of tskewD1



                        Differential Signal   VOS

                                                                      tskewD1




10.16 I/Q Data Interface Receiver AC Specification
      The following table shows the AC parameter of the LVDS receiver of the I/Q data interface.

      Table 10-35. I/Q Data Interface Receiver AC Specification

      Symbol       Parameter                              Condition                             Min.        Typ.         Max.          Unit
      tskewR1      Skew tolerable at receiver input to    Data channel to clock channel           -1                       2           ns
                   meet setup and hold time
                   requirements




10.17 Digital Block Timing Specification
      The following table shows the timing of digital units.

      Table 10-36. Digital Blocks Timing

      Symbol       Parameter                              Condition                             Min.        Typ.         Max.          Unit
      tRND         Update time of random number           Transceiver must operate in                                      1           μs
                   value                                  state RX.




                                                                                    Atmel AT86RF215 - DATASHEET                          207
                                                                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| tjitter | RXCLK jitter |  |  |  | 100 | ps |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| tskewR1 | Skew tolerable at receiver input to | Data channel to clock channel | -1 |  | 2 | ns |
|  | meet setup and hold time |  |  |  |  |  |
|  | requirements |  |  |  |  |  |

| Symbol | Parameter | Condition | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| tRND | Update time of random number | Transceiver must operate in state RX. |  |  | 1 | μs |
|  | value |  |  |  |  |  |


<!-- page 208 -->

11.    Typical Characteristics

11.1   Output Power at Several Modulations
       RMS output power is measured at device pins. Measurements are performed under typical conditions
       (DEVDD/EVDD=3.0V, Temp=25degC), RFn_PAC.PACUR=0x3.

       Figure 11-1. Output power vs. RF09_PAX.TXPWR register for several modulations at f channel=500MHz


                                                                  Output power vs. RF09_PAC.TXPWR register value at 500MHz
                                        20

                                        15

                                        10




            Output Power P_RFr [dBm]
                                         5                                                                                                                  CW
                                                                                                                                                            FSK
                                         0
                                                                                                                                                            OQPSK
                                        -5                                                                                                                  OFDM O1

                                       -10                                                                                                                  OFDM O2
                                                                                                                                                            OFDM O3
                                       -15
                                                                                                                                                            OFDM O4
                                       -20

                                       -25
                                                 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                                          RF09_PAC.TXPWR register value




       Figure 11-2. Output power vs. RF09_PAX.TXPWR register for several modulations at f channel=900MHz

                                                                          Output power vs. RF09_PAC.TXPWR register value at 900MHz
                                       20

                                       15

                                       10




         Output Power P_RF [dBm]
                                        5                                                                                                                    CW
                                                                                                                                                             FSK
                                        0
                                                                                                                                                             OQPSK
                                        -5                                                                                                                   OFDM O1

                                       -10                                                                                                                   OFDM O2
                                                                                                                                                             OFDM O3
                                       -15
                                                                                                                                                             OFDM O4
                                       -20

                                       -25
                                             0    1   2   3   4   5   6    7   8   9   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                                            RF09_PAC.TXPWR register value




                                                                                                                                                Atmel AT86RF215 - DATASHEET                     208
                                                                                                                                                 Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 209 -->

       Figure 11-3. Output power vs. RF24_PAX.TXPWR register for several modulations at f channel=2445MHz


                                                         Output power vs. RF24_PAC.TXPWR register value at 2445MHz
                                      20

                                      15

                                      10




            Output Power P_RF [dBm]
                                                                                                                                         CW
                                       5
                                                                                                                                         OQPSK
                                       0                                                                                                 FSK
                                                                                                                                         OFDM O1
                                       -5
                                                                                                                                         OFDM O2

                                      -10                                                                                                OFDM O3
                                                                                                                                         OFDM O4
                                      -15

                                      -20
                                             0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                           RF24_PAC.TXPWR register value




11.2   Output Power versus Supply Voltage

       Figure 11-4. Maximum output power vs. supply voltage at fchannel=500MHz for 2FSK-50ksymbols/s

                                                          Output power (2FSK-50ksymbols/s) vs. supply voltage EVDD
                                                                        (fChannel=500MHz, TXPWR=31)
                                      20.0




                                      15.0




         Output power P_RF [dBm]
                                      10.0                                                                                               PAVC=0


                                                                                                                                         PAVC=1


                                       5.0                                                                                               PAVC=2




                                       0.0
                                             1.8            2            2.2              2.4              2.6     2.8               3
                                                                                       EVDD [V]




                                                                                                                            Atmel AT86RF215 - DATASHEET                      209
                                                                                                                              Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 210 -->

Figure 11-5. Maximum output power vs. supply voltage at fchannel=900MHz for 2FSK-50ksymbols/s

                                          Output power (2FSK-50ksymbols/s) vs. supply voltage
                                                    (fChannel=900MHz, TXPWR=31)
                            20.0




                            15.0




  Output Power P_RF [dBm]
                            10.0                                                                             PAVC=0


                                                                                                             PAVC=1


                             5.0                                                                             PAVC=2




                             0.0
                                   1.8   2.0        2.2         2.4         2.6         2.8         3.0
                                                              EVDD [V]



Figure 11-6. Maximum output power vs. supply voltage at fchannel=2445MHz for 2FSK-50ksymbols/s

                                          Output power (2FSK-50ksymbols/s) vs. supply voltage
                                                    (fChannel=900MHz, TXPWR=31)
                            20.0




                            15.0




  Output Power_RF [dBm]
                            10.0                                                                             PAVC=0


                                                                                                             PAVC=1


                             5.0                                                                             PAVC=2




                             0.0
                                   1.8   2.0        2.2         2.4         2.6         2.8         3.0
                                                              EVDD [V]




                                                                                                Atmel AT86RF215 - DATASHEET                     210
                                                                                                 Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 211 -->

11.3   TX Current Consumption and Output Power at PAC.PACUR settings

       Figure 11-7. Current consumption vs. PAC.TXPWR at PA current settings (PAC.PACUR) for 2FSK-50ksymbols/s at
                    500MHz band


                                                           TX Supply Current (2FSK-50ksymbols/s) at PAC.PACUR Setting
                                                                                (fChannel=500MHz)
                                 90


                                 80


                                 70


                                 60




          Supply Current [mA]
                                                                                                                                                  PAC.PACUR:

                                 50                                                                                                                      0
                                                                                                                                                         1
                                 40                                                                                                                      2
                                                                                                                                                         3
                                 30


                                 20


                                 10


                                  0
                                       0   1   2   3   4    5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                                      RF09_PAC.TXPWR register value



       Figure 11-8. Output power vs. PAC.TXPWR at PA current settings (PAC.PACUR) for 2FSK-50ksymbols/s at 500MHz
                    band


                                                           TX Output Power (2FSK-50ksymbols/s) at PAC.PACUR Setting
                                                                               (fChannel=500MHz)
                                 20



                                 15



                                 10




       Output Power P_RF [dBm]
                                                                                                                                                  PAC.PACUR:
                                  5
                                                                                                                                                         0
                                                                                                                                                         1
                                                                                                                                                         2
                                  0
                                                                                                                                                         3


                                  -5



                                 -10



                                 -15
                                       0   1   2   3   4    5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                                 RF09_PAC.TXPWR register value




                                                                                                                                   Atmel AT86RF215 - DATASHEET                      211
                                                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 212 -->

Figure 11-9. Current consumption vs. PAC.TXPWR at PA current settings (PAC.PACUR) for 2FSK-50ksymbols/s at
             900MHz band


                                                       TX Supply Current (2FSK-50ksymbols/s) at PAC.PACUR Setting
                                                                            (fChannel=900MHz)
                              80


                              70


                              60




   Supply Current P_RF [mA]
                              50                                                                                                              PAC.PACUR:

                                                                                                                                                     0
                              40                                                                                                                     1
                                                                                                                                                     2
                                                                                                                                                     3
                              30


                              20


                              10


                               0
                                   0   1   2   3   4    5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                             RF09_PAC.TXPWR register value


Figure 11-10. Output power vs. PAC.TXPWR at PA current settings (PAC.PACUR) for 2FSK-50ksymbols/s at 900MHz
              band

                                                       TX Output Power (2FSK-50ksymbols/s) at PAC.PACUR Setting
                                                                           (fChannel=900MHz)
                              20



                              15



                              10




Output Power P_RF [dBm]
                                                                                                                                              PAC.PACUR:
                               5
                                                                                                                                                     0
                                                                                                                                                     1
                                                                                                                                                     2
                               0
                                                                                                                                                     3


                              -5



                          -10



                          -15
                                   0   1   2   3   4    5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                             RF09_PAC.TXPWR register value




                                                                                                                               Atmel AT86RF215 - DATASHEET                      212
                                                                                                                                 Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 213 -->

Figure 11-11. Current consumption vs. PAC.TXPWR at PA current settings (PAC.PACUR) for 2FSK-50ksymbols/s at
              2.4GHz band


                                                    TX Supply Current (2FSK-50ksymbols/s) at PAC.PACUR Setting
                                                                         (fChannel=2445MHz)
                          80


                          70


                          60




   Supply Current [mA]
                          50
                                                                                                                                      PAC.PACUR:
                                                                                                                                             0
                          40
                                                                                                                                             1
                                                                                                                                             2

                          30                                                                                                                 3



                          20


                          10


                           0
                                0   1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                         RF24_PAC.TXPWR register value


Figure 11-12. Output power vs. PAC.TXPWR at PA current settings (PAC.PACUR) for 2FSK-50ksymbols/s at 2.4GHz
              band

                                                    TX Output Power (2FSK-50ksymbols/s) at PAC.PACUR Setting
                                                                       (fChannel=2445MHz)
                          20



                          15



                          10




Output Power P_RF [dBm]
                           5                                                                                                          PAC.PACUR:
                                                                                                                                             0
                                                                                                                                             1
                           0                                                                                                                 2
                                                                                                                                             3


                           -5



                          -10



                          -15
                                0   1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
                                                                         RF24_PAC.TXPWR register value




                                                                                                                          Atmel AT86RF215 - DATASHEET                      213
                                                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 214 -->

11.4   TX Output Power at Temperature Sweep

       Figure 11-13. Maximum TX output power vs. temperature for 2FSK-50ksymbols/s


                                                       Maximum TX Output Power (2FSK-50ksymbols/s) vs. Temperature
                                                                            (PAC.PACUR=3)
                                    18


                                    16


                                    14




         Output Power P_RF [dBm]
                                    12

                                                                                                                                490000000
                                                                                                                                 500MHz
                                    10
                                                                                                                                902000000
                                                                                                                                 900MHz
                                     8
                                                                                                                                 2445MHz
                                                                                                                                244500000
                                     6                                                                                          0


                                     4


                                     2


                                     0
                                         -40                          0                          25                      85
                                                                            Temperature [degC]



11.5   TX Output Power at Frequency Sweep

       Figure 11-14. Maximum TX output power vs. frequency for 2FSK-50ksymbols/s at 500MHz band


                                               Maximum TX Output Power (2FSK-50ksymbols/s) vs Frequency at PAC.PACUR
                                                              Setting 500MHz Band (PAC.TXPWR=31)
                                    18


                                    16


                                    14




          Output Power P_RF [dBm]
                                    12
                                                                                                                                PAC.PACUR:
                                    10                                                                                               0
                                                                                                                                     1
                                     8
                                                                                                                                     2
                                     6                                                                                               3

                                     4


                                     2


                                     0
                                         390     400      410   420   430    440    450    460   470   480   490   500    510
                                                                              Frequency [MHz]




                                                                                                                   Atmel AT86RF215 - DATASHEET                      214
                                                                                                                     Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 215 -->

Figure 11-15. Maximum TX output power vs. frequency for 2FSK-50ksymbols/s at 900MHz band


                                             Maximum TX Output Power (2FSK-50ksymbols/s) vs Frequency at PAC.PACUR
                                                            Setting 900MHz Band (PAC.TXPWR=31)
                            18


                            16


                            14




         Output Power P_RF [dBm]
                            12
                                                                                                                                                 PAC.PACUR:
                            10                                                                                                                          0
                                                                                                                                                        1
                                   8
                                                                                                                                                        2
                                   6                                                                                                                    3

                                   4


                                   2


                                   0
                                       790    800     810   820      830   840     850   860    870     880   890      900   910     920   930
                                                                                   Frequency [MHz]




Figure 11-16. Maximum TX output power vs. frequency for 2FSK-50ksymbols/s at 2400MHz band


                                             Maximum TX Output Power (2FSK-50ksymbols/s) vs Frequency at PAC.PACUR
                                                            Setting 2400MHz Band, (PAC.TXPWR=31)
                            16


                            14


                            12




  Output Power P_RF [dBm]
                            10                                                                                                                   PAC.PACUR:
                                                                                                                                                        0
                                   8
                                                                                                                                                        1
                                                                                                                                                        2
                                   6
                                                                                                                                                        3

                                   4


                                   2


                                   0
                                    2400            2410      2420          2430         2440         2450      2460          2470         2480
                                                                                   Frequency [MHz]




                                                                                                                                     Atmel AT86RF215 - DATASHEET                     215
                                                                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 216 -->

11.6   Receiver Sensitivity

       Figure 11-17. Receiver sensitivity vs. frequency for selected modulations (900MHz band)


                                          Receiver Sensitivity vs Frequency 900MHz Band for selected modulations
                              -90


                              -95


                             -100


                             -105




         Sensitivity [dBm]
                                                                                                                 2FSK-
                                                                                                                2FSK50MI10
                                                                                                                 50ksymbols/s
                             -110

                                                                                                                 OFDM
                             -115
                                                                                                                OFDMO2M4
                                                                                                                 Opt.2, MCS4:
                                                                                                                 600kb/s

                             -120                                                                                OQPSK
                                                                                                                OQPSKFC0RM0
                                                                                                                 Chip Rate
                                                                                                                 100kchip/s,
                             -125
                                                                                                                 Rate Mode 0
                                                                                                                 6.25kb/s
                             -130
                                    795        815       835      855        875     895       915       935
                                                                  Frequency [MHz]



       Figure 11-18. Receiver sensitivity vs. frequency for selected modulations (2400MHz band)


                                          Receiver Sensitivity vs Frequency 2400MHz Band for selected modulations
                              -90


                              -95


                             -100


                             -105




         Sensitivity [dBm]
                                                                                                                 2FSK-
                                                                                                                2FSK50MI10
                                                                                                                 50ksymbols/s
                             -110

                                                                                                                 OFDM
                             -115
                                                                                                                OFDMO2M4
                                                                                                                 Opt.2, MCS4:
                                                                                                                 600kb/s

                             -120                                                                                OQPSK
                                                                                                                OQPSKFC0RM0
                                                                                                                 Chip Rate
                                                                                                                 100kchip/s,
                             -125
                                                                                                                 Rate Mode 0
                                                                                                                 6.25kb/s
                             -130
                                 2405         2415      2425      2435      2445     2455     2465      2475
                                                                 Frequency [MHz]




                                                                                                          Atmel AT86RF215 - DATASHEET                     216
                                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 217 -->

11.7   Frequency Synthesizer (PLL)

       Figure 11-19. PLL phase noise


                                                                   Phase Noise
                                  0


                                 -20


                                 -40




         Phase noise [dBc/Hz]
                                 -60


                                 -80                                                                             Channel=490MHz
                                                                                                                 Channel=902MHz
                                -100                                                                             Channel=2445MHz


                                -120


                                -140


                                -160
                                  1.00E+03   1.00E+04       1.00E+05            1.00E+06         1.00E+07
                                                        Offset Frequency [Hz]




                                                                                           Atmel AT86RF215 - DATASHEET                     217
                                                                                            Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 218 -->

12.   Acronyms and Abbreviations
      Table 12-1 contains acronyms and abbreviations used in this document.

      Table 12-1. Acronyms and Abbreviations

      Abbreviations    Description
      AACI             Alternate Adjacent Channel Interference Tolerance
      ACI              Adjacent Channel Interference Tolerance
      ACK              Acknowledgement
      ADC              Analog-to-Digital Converter
      AGC              Automatic Gain Control
      AVREG            Analog Voltage Regulator
      AWGN             Additive White Gaussian Noise
      BATMON           Battery Monitor
      BPF              Band-Pass Filter
      BPSK             Binary Phase Shift Keying
      CCA              Clear Channel Assessment
      CRC              Cyclic Redundancy Check
      CW               Continuous Wave
      DAC              Digital-to-Analog Converter
      DDR              Double Data Rate
      DVREG            Digital Voltage Regulator
      ED               Energy Detect
      ESD              Electrostatic Discharge
      EVM              Error Vector Magnitude
      FCF              Frame Control Field
      FCS              Frame Check Sequence
      FEC              Forward Error Correction
      FSK              Frequency Shift Keying
      FTN              Filter Tuning Network
      HCS              Header Check Sequence
      I/O              Input/Output
      I/Q              In/Quadrature-Phase
      I/Q IF           I/Q Interface
      IC               Integrated Circuit
      IEEE             Institute of Electrical and Electronic Engineers
      IF               Intermediate Frequency
      IRQ              Interrupt Request
      ISM              Industrial Scientific Medical
      LNA              Low-Noise Amplifier




                                                                              Atmel AT86RF215 - DATASHEET                     218
                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 219 -->

Abbreviations   Description
LPF             Low-Pass Filter
LSB             Least Significant Bit
LVDS            Low-Voltage Differential-Signalling
MAC             Medium Access Control
MFR             MAC Footer
MHR             MAC Header
MISO            Master Input, Slave Output
MOSI            Master Output, Slave Input
MR-OFDM         Multi-Rate and multi-regional Orthogonal Frequency Division Multiplexing
MR-O-QPSK       Multi-Rate and multi-regional Offset Quadrature Phase-Shift Keying
MSB             Most Significant Bit
MSDU            MAC Service Data Unit
O-QPSK          Offset Quadrature Phase Shift Keying
PA              Power Amplifier
PAN             Personal Area Network
PCB             Printed Circuit Board
PER             Packet Error Rate
PHR             PHY Header
PHY             Physical Layer
PLL             Phase-Looked Loop
PPDU            PHY Protocol Data Unit
PRBS            Pseudo Random Binary Sequence
PSD             Power Spectrum Density
PSDU            PHY Service Data Unit
QAM             Quadrature Amplitude Modulation
QFN             Quad Flat No-Lead Package
RBW             Resolution Bandwidth
RC              Raised Cosine
RF              Radio Frequency
RPC             Reduced Power Consumption
RSSI            Received Signal Strength Indicator
RX              Receiver
RXFE            Receiver Front End
SFD             Start-Of-Frame Delimiter
SHR             Synchronization Header
SLVDS           Scaleable LVDS
SPI             Serial Peripheral Interface
SUN             Smart metering utility network
TRX             Transceiver
TX              Transmitter



                                                                           Atmel AT86RF215 - DATASHEET                      219
                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 220 -->

Abbreviations   Description
TXFE            Transmitter Frontend
XOSC            Crystal Oscillator




                                       Atmel AT86RF215 - DATASHEET                     220
                                        Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 221 -->

13.    Appendix

13.1   Continuous Transmission

13.1.1 Frame Based Continuous Transmission
       The AT86RF215 comprises a frame based continuous transmit mode. This is useful for application / production tests as
       well as certification tests. Using this mode, the transceiver acts as a continuous transmitter.
       The continuous transmission is enabled if the sub-register PC.CTX is set to 1. Prior to transmission, the AT86RF215
       must be in state TXPREP, see section "State Machine" on page 33. A frame transmission, started by CMD.CMD=TX
       with enabled continuous transmit mode (PC.CTX), transmits synchronization header (SHR), PHY header (PHR) and
       repeatedly PHY payload (PSDU). The current PHY settings are used; the length of the PHY payload is configured by
       the concatenation of the registers BBCn_TXFLH and BBCn_TXFLL. If the sub-register PC.TXAFCS is set to 1, the last
       PHY payload octets are replaced by the calculated FCS (see "Frame Check Sequence" on page 138).
       The transmission proceeds as long as the sub-register PC.CTX remains 1. If the sub-register PC.CTX is set to 0, the
       transmission stops once the current PSDU transmission is completed (Figure 13-1). The AT86RF215 enters state
       TXPREP afterwards (see "State TXPREP" on page 35).

       Figure 13-1. Continuous Transmission Sequence


       RF Signal              SHR   PHR          PSDU                  PSDU                          PSDU


       STATE         TXPREP                             TX                                           TX                 TXPREP


       Instruction       CMD=TX

       PC.CTX



       While in continuous TX mode, the transmit frame buffer is read out cyclically by the baseband core. Pad bits (as
       described in [3] for MR-OFDM and MR-O-QPSK) are only inserted in the last PSDU transmit cycle.
       Alternatively, this transmit mode can be stopped immediately if the command TRXOFF is written to the sub-register
       CMD.CMD=TRXOFF.
       Table 13-2 shows the required register modifications for continuous transmit.

13.1.2 DAC Value Overwrite
       The AT86RF215 comprises a DAC (digital to analog converter) value overwrite functionality. Each transceiver contains
       two transmitter DACs (for the in-phase and quadrature-phase signal) in order to transmit IQ signals. Both DAC values
       can be overwritten separately by register settings. This feature is useful to transmit an LO carrier which is necessary for
       certain certifications.
       If the sub-register TXDACI.ENTXDACID is set to 1, the digital input value of the in-phase signal DAC is overwritten with
       the value of the sub-register TXDACI.TXDACID. Respective, if the sub-register TXDACQ.ENTXDACQD is set to 1, the
       digital input value of the quadrature-phase signal DAC is overwritten with the value of the sub-register
       TXDACQ.TXDACQD.




                                                                                    Atmel AT86RF215 - DATASHEET                       221
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 222 -->

       Both sub-registers TXDACI.TXDACID and TXDACQ.TXDACQD contain seven bit binary values in the range from 0x00
       to 0x7E. A value of 0x3F results in a zero signal output magnitude of the respective DAC. A value of 0x00 results in the
       minimum signal output of the respective DAC, a value of 0x7E results in the maximum output signal of the respective
       DAC.
       If the transceiver is in state TX and both DAC values are overwritten, the transceiver transmits an LO carrier of the
       frequency selected by the "Frequency Synthesizer (PLL)" on page 62.
       To start a continuous transmission of a LO carrier, the transmitter is started as described in Frame Based Continuous
       Transmission. Alternatively, the transmitter can be started using chip mode 1 if sub-register IQIFC1.CHPM is set to
       0x01. In this case the transmitter is started by command TX.
       Table 13-1 describes the recommended scenario for DAC value overwrite, Table 13-2 shows the required register
       modifications for continuous transmit for RF215 and RF215IQ.

       Table 13-1. Recommended DAC Value Overwrite Scenario

        TXDACI.TXDACID                  TXDACQ.TXDACQD                    Comment

        0x7E                            0x3F                              The in-phase DAC has the maximum signal
                                                                          magnitude, the quadrature-phase DAC has the
                                                                          minimum signal magnitude. During transmit a carrier
                                                                          with output power, respective to sub-register
                                                                          PAC.TXPWR is transmitted.

       Table 13-2. Required Register Settings for Continuous Transmit

        RF215 (frame based)                        RF215 (DAC overwrite)                            RF215IQ (DAC overwrite)
        IQIFC1.CHPM = 0                            IQIFC1.CHPM = 0                                  IQIFC1.CHPM = 1
        PC.CTX = 1                                 PC.CTX = 1
        Configure PHY mode                         Configure PHY mode
        {BBCn_TXFLH,BBCn_TXFLL} = 1..2047          {BBCn_TXFLH,BBCn_TXFLL} = 1..2047
                                                   TXDACI.TXDACID = 0x7E                            TXDACI.TXDACID = 0x7E
                                                   TXDACQ.TXDACQD = 0x3F                            TXDACQ.TXDACQD = 0x3F
                                                   TXDACI.ENTXDACID = 1                             TXDACI.ENTXDACID = 1
                                                   TXDACQ.ENTXDACQD = 1                             TXDACQ.ENTXDACQD = 1
        CMD.CMD = TX                               CMD.CMD = TX                                     CMD.CMD = TX

13.1.3 Register Description
13.1.3.1 BBCn_PC – PHY Control
       This register configures the baseband PHY.
        Bit              7          6          5           4          3           2            1             0
                        CTX       FCSFE      FCSOK     TXAFCS       FCST        BBEN                 PT                    BBCn_PC
        Read/Write      RW         RW          R          RW         RW          RW          RW            RW
        Initial Value    0          1          0           1          0           1            0             0

        Bit 7 – PC.CTX: Continuous Transmit
       This sub-register enables the continuous transmit mode.




                                                                                      Atmel AT86RF215 - DATASHEET                     222
                                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 223 -->

       Table 13-3. CTX

        Sub-register           Value        Description
        CTX                    0x0          Continuous transmission disabled
                               0x1          Continuous transmission enabled



13.1.3.2 RFn_TXDACI – In-phase input value for TXDAC
       Input I value can be applied at TXDAC (DC measurement)
        Bit                7           6            5          4          3     2             1             0
                        ENTXDAC
                                                                      TXDACID                                           RFn_TXDACI
                           ID
        Read/Write        RW           RW          RW         RW         RW     RW          RW            RW
        Initial Value      0           0            0          0          0     0             0             0

        Bit 7 – TXDACI.ENTXDACID: Enable input to TXDAC
        Bit 6:0 – TXDACI.TXDACID: Input to TXDAC data


13.1.3.3 RFn_TXDACQ – Quadrature-phase input value for TXDAC
       Input Q value can be applied at TXDAC (DC measurement)
        Bit                7           6            5          4          3     2             1             0
                        ENTXDAC
                                                                      TXDACQD                                           RFn_TXDACQ
                          QD
        Read/Write        RW           RW          RW         RW         RW     RW          RW            RW
        Initial Value      0           0            0          0          0     0             0             0

        Bit 7 – TXDACQ.ENTXDACQD: Enable input to TXDAC
        Bit 6:0 – TXDACQ.TXDACQD: Input to TXDAC data




                                                                                     Atmel AT86RF215 - DATASHEET                     223
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

**Extracted table(s) on this page:**

| Sub-register | Value | Description |
| --- | --- | --- |
| CTX | 0x0 | Continuous transmission disabled |
|  | 0x1 | Continuous transmission enabled |


<!-- page 224 -->

14.   Ordering Information

      Ordering Code           Carrier Type    Package                       Voltage              Temperature Range
                                                                            Range
      AT86RF215-ZU            Tray            PQ                            (1.8 - 3.6)V         Industrial (-40C to +85C)
                                              (Lead-free/Halogen-free)
      AT86RF215-ZUR           Tape & Reel     PQ                            (1.8 - 3.6)V         Industrial (-40C to +85C)
                                              (Lead-free/Halogen-free)
      AT86RF215IQ-ZU          Tray            PQ                            (1.8 - 3.6)V         Industrial (-40C to +85C)
                                              (Lead-free/Halogen-free)
      AT86RF215IQ-ZUR         Tape & Reel     PQ                            (1.8 - 3.6)V         Industrial (-40C to +85C)
                                              (Lead-free/Halogen-free)
      AT86RF215M-ZU           Tray            PQ                            (1.8 - 3.6)V         Industrial (-40C to +85C)
                                              (Lead-free/Halogen-free)
      AT86RF215M-ZUR          Tape & Reel     PQ                            (1.8 - 3.6)V         Industrial (-40C to +85C)
                                              (Lead-free/Halogen-free)
      Note:   Pb-free packaging, complies to European Directive for Restriction of Hazardous Substances (RoHS directive).
              Also Halide free and fully Green
      Note:   Minimum Tape&Reel quantity: 4000




                                                                               Atmel AT86RF215 - DATASHEET                     224
                                                                                Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 225 -->

15.    Errata

15.1   Errata Overview

       Table 15-1. Errata Overview

        Device                Version        Applicable Errata Numbers
        AT86RF215             v.1            1, 2, 3, 4, 5, 6, 7, 8, 10
                              v.3            no known errata
        AT86RF215M            v.1            1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                              v.3            9
        AT86RF215IQ           v.1            1, 2, 6, 8
                              v.3            no known errata




15.2   Errata AT86RF215 Description

15.2.1 Errata #1: Low transmitter LO leakage calibration
       Description: During state transition from TRXOFF to TXPREP the LO leakage calibration is automatically executed
       and the derived calibration values are stored to the corresponding registers; i.e. TXCI.DCOI and TXCQ.DCOQ. The
       automatic LO leakage calibration loop has a failure rate of about 3%.
       Software workaround:
       Step 1: Generate/Calculate correct calibration values
       During device initialization or significant environment changes, identify the correct calibration values for each used
       frequency band. Generate calibration values:
            Initiate automatic calibration loop from state TRXOFF by writing command TXPREP to register RFn_CMD.
            Wait until state TRXRDY is reached
            Read the calibration values from registers RFn_TXCI_DCOI and RFn_TXCQ_DCOQ
       Repeat above procedure five times and calculate the median value for TXCI and TXCQ
       Step 2: Apply correct calibration values
       After a state transition from TRXOFF to TXPREP write the derived median calibration values from step 1 to the
       corresponding sub-registers TXCI.DCOI and TXCQ.DCOQ.
       Note that a state transition from the state TRXOFF to RX passed internally the state TXPREP. Therefore after the state
       transition (from the state TRXOFF to RX) step 2 is applicable after reaching state RX as well.

15.2.1.1 RFn_TXCI – Transmit calibration I path
       The register contains information about the TX LO leakage calibration value of the transmit I path. At the transition
       process from state TRXOFF to TX the calibration is started automatically.




                                                                                     Atmel AT86RF215 - DATASHEET                     225
                                                                                      Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 226 -->

        Bit                   7          6          5          4          3          2             1             0
                              –          –                                    DCOI                                             RFn_TXCI
        Read/Write           RW          R         RW         RW         RW          RW          RW            RW
        Initial Value         0          0          0          1          1          1             1             1

        Bit 5:0 – TXCI.DCOI: DC offset calibration value I path
       The value of the LO leakage calibration of the transmit I path is captured.

15.2.1.2 RFn_TXCQ – Transmit calibration Q path
       The register contains information about the TX LO leakage calibration value of the transmit Q path. At the transition
       process from state TRXOFF to TX the calibration is started automatically.
        Bit                   7          6          5          4          3          2             1             0
                              –          –                                    DCOQ                                            RFn_TXCQ
        Read/Write            R          R         RW         RW         RW          RW          RW            RW
        Initial Value         0          0          0          1          1          1             1             1

        Bit 5:0 – TXCQ.DCOQ: DC offset calibration value Q path
       The value of the LO leakage calibration of the transmit Q path is captured.


                                                                                                                     [Errata reference 4807]

15.2.2 Errata #2: State transition not successful
       Description:
       Scenario 1 – State transition is triggered by writing a command to the register RFn_CMD
       The following state transitions may not be completed:
              State TRXOFF to state TXPREP
              State TRXOFF to state RX
       After transitioning to the above mentioned states, the target state is provided by the register RFn_STATE and in case of
       transition to state TXPREP the interrupt TRXRDY is issued if interrupt is enabled,. If state transition is not completed,
       the state register RFn_STATE provides the state TRANSITION and in case of transition to state TXPREP no interrupt is
       issued. When the transition period exceeds tTRXOFF_TXPREP(max)=200µs and the target state is not reached, the following
       workaround is required.
       Scenario 2 – State transition is triggered by changing the channel frequency
       Changing the channel frequency (see section "Frequency Synthesizer (PLL)" on page 62) in the state TXPREP, an
       internal state transition may not be completed. If the internal state transition is completed, the interrupt TRXRDY is
       issued, if interrupt is enabled, and the sub-register PLL.LS is set to 1. When no interrupt is issued or the value of the
       sub-register PLL.LS is not 1 within a period of tTRXOFF_TXPREP(max)=200µs, the following workaround is required.
       Software workaround for scenario 1 and 2:
         Step 1:        Write to the register RFn_PLL the value 9
         Step 2:        Wait for 20us
         Step 3:        Write to the register RFn_PLL the value 8
         Step 4:        Scenario 1: Wait until the target state is reached or in case of transition to state TXPREP the interrupt
                        TRXRDY is issued as well if interrupt is enabled.
                        Scenario 2: Wait until the interrupt TRXRDY is issued or the sub-register PLL.LS is set to 1.




                                                                                          Atmel AT86RF215 - DATASHEET                     226
                                                                                           Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 227 -->

         Step 5: If the target state is not reached or the interrupt TRXRDY is not issued within 20μs, repeat the procedure
                 starting with step 1.


                                                                                                             [Errata reference 4810]

15.2.3 Errata #3: TX Signal Quality for FSK
       Description:
       One modulation quality parameter of FSK is the zero crossing tolerance. The excursions for the zero crossings for all
       trajectories of the eye diagram shall be within 12.5% of Ts (see IEEE Std 802.15.4g™-2012). The spectrum analyzer
       receiver bandwidth is 4x(Symbol rate) regardless of the modulation index of the FSK mode and no receiver input
       measurement filter is applied. Due to transmitter limitations the FSK modes require power backoff to fullfil the zero
       crossing requirements in the 900MHz and 2.4GHz band, the 500MHz band is not affected, see Table 15-2.

       Table 15-2. MR-FSK power backoff

        Modulation     Frequency      Mod.        Symbol rate   Max(P_R      Register          Comments
                       band           index       [ksymbol/s]   F) [dBm]     PAC.TXPWR
               2-FSK       900MHz             1            50        13.0    28                Operation RF215 to RF215 at
                                                                                               maximum output power possible
               2-FSK       900MHz             1          100         11.0    24
               2-FSK       900MHz             1          200         11.0    24
               2-FSK       900MHz          0.5           100         10.0    22                Operation RF215 to RF215 at
                                                                                               11.0dBm output power possible
               2-FSK       900MHz          0.5           150         10.0    22
               2-FSK       900MHz          0.5           200         10.0    22
               2-FSK       900MHz          0.5           300         10.0    22


               2-FSK      2400MHz             1            50         8.0    19                Operation RF215 to RF215 at
                                                                                               12.0dBm output power possible
               2-FSK      2400MHz             1          100          6.0    16
               2-FSK      2400MHz          0.5           150     exceeds     -                 Operation RF215 to RF215 at
                                                                    limits                     9.0dBm output power possible
               2-FSK      2400MHz          0.5           200     exceeds     -
                                                                    limits
       Note:   Refer to MR-FSK power charts in section "Output Power at Several Modulations " on page 208 for correct
               register PAC.TXPWR setting.
                                                                                                             [Errata reference 4820]

15.2.4 Errata #4: TX Signal Quality for MR-OFDM
       Description:
       The RMS error [dB] of the error vector magnitude determines the signal quality of MR-OFDM. The limits are specified in
       IEEE Std 802.15.4g™-2012, Table 161; depending on MCS level. The Max(P_RF) is the maximum RMS output power
       of the MR-OFDM signals which fulfills the standards, see Table 15-3. MR-OFDM modes that are not mentioned
       (MCS=0,1,2,3) in Table 15-3 on page 228 are not affected.




                                                                                  Atmel AT86RF215 - DATASHEET                      227
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 228 -->

      Table 15-3. MR-OFDM power backoff

       Modulation    Frequency    Option   MCS        Max(P_RF)   Register        Comments
                     band                             [dBm]       PAC.TXPWR
                     [MHz]
       MR-OFDM       500MHz       4        6          10.0        29              Operation RF215 to RF215 at full output
                                                                                  power possible


       MR-OFDM       900MHz       2        4          9.0         28              Operation RF215 to RF215 at full output
                                                                                  power possible
       MR-OFDM       900MHz       2        5          5.0         23
       MR-OFDM       900MHz       3        5          7.0         26
       MR-OFDM       900MHz       3        6          5.0         23              Operation RF215 to RF215 at 5.0dBm
                                                                                  output power possible
       MR-OFDM       900MHz       4        5          8.0         26              Operation RF215 to RF215 at full output
                                                                                  power possible
       MR-OFDM       900MHz       4        6          6.0         23              Operation RF215 to RF215 at 8.0dBm
                                                                                  output power possible


       MR-OFDM       2400MHz      2        4          7.0         26              Operation RF215 to RF215 at full output
                                                                                  power possible
       MR-OFDM       2400MHz      2        5          6.0         25              Operation RF215 to RF215 at 8.0dBm
                                                                                  output power possible
       MR-OFDM       2400MHz      3        4          7.0         26              Operation RF215 to RF215 at full output
                                                                                  power possible
       MR-OFDM       2400MHz      3        5          6.0         25              Operation RF215 to RF215 at 8.0dBm
                                                                                  output power possible
       MR-OFDM       2400MHz      3        6          5.0         24              Operation RF215 to RF215 at 5.0dBm
                                                                                  output power possible
       MR-OFDM       2400MHz      4        4          8.0         26              Operation RF215 to RF215 at full output
                                                                                  power possible
       MR-OFDM       2400MHz      4        5          7.0         25
       MR-OFDM       2400MHz      4        6          5.0         23              Operation RF215 to RF215 at 5.0dBm
                                                                                  output power possible
      Note:    Refer to MR-OFDM power charts in section "Output Power at Several Modulations " on page 208 for correct
               register PAC.TXPWR setting.
                                                                                                        [Errata reference 4664]

15.2.5 Errata #5: Reduced power consumption mode (RPC) causes higher PER
      Description:
      The usage of reduced power consumption mode (RPC) for MR-FSK and MR-OQPSK may cause a higher packet error
      rate.
      Software workaround:
      The RPC is configured with sub-register OQPSKC2.RPC set to 1 for MR-OQPSK modulation and sub-register
      FSKRPC.EN set to 1 for MR-FSK modulation. In addition, the following settings must be made:
          Write to the register RFn_PLL the value 9 if the AT86RF215 is in state RX and the desired channel frequency
              has been reached.




                                                                              Atmel AT86RF215 - DATASHEET                     228
                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 229 -->

           Write to the register RFn_PLL the value 8 prior to a change of the channel frequency or if the state RX has
             been left (including automatic state change from RX to TXPREP).
                                                                                                            [Errata reference 4841]

15.2.6 Errata #6: State Machine Command RFn_CMD=TRXOFF may not be succeeded
       Description:
       If the current state is different from SLEEP, the execution of the command TRXOFF may fail.
       Software workaround:
            Check state by reading register RFn_STATE
            Repeat the command RFn_CMD=TRXOFF if the target state was not reached.
                                                                                                            [Errata reference 4840]

15.2.7 Errata #7: Acknowledgement Frame is transmitted without ACK request
       Description:
       The Automatic Acknowledgement unit transmits an acknowledgement frame without an ACK request under the
       following condition:
           A frame is received that does not match the 3rd level filter rules but its ACK request bit is set and the next
             incoming frame matches all 3rd level filter rules but the ACK request bit is zero (this second frame is
             acknowledged).
       Software workaround:
            If the interrupt RXFE is issued and the AR bit in the header of the incoming frame is set to 0, then apply the
             following sequence before the ACK frame is automatically transmitted:
              Set sub-register AMCS.AACK to 0
              Set sub-register AMCS.AACK back to 1
                                                                                                            [Errata reference 4830]

15.2.8 Errata #8: Scalable LVDS I/Q data interface link does not support fail safe mode
       Description:
       The pins RXCLKP/RXCLKN, RXDN09/RXDP09 and RXDN24/RXDP24 must not be pulled high in SLVDS mode when
       the I/Q interface is disabled (powered-down). Thus the SLVDS interface link does not support the fail safe feature. In
       modes compliant to the IEEE standard 1596.1-1996 fail-safe detection with pull-up resistors is supported.
       Solution:
            Do not pull high pins RXCLK and RXDx using the SLVDS link option (common mode voltage of 200mV with a
             voltage swing of 200mV).
            Do not use a fail safe circuit with pull-up resistor when using the SLVDS link option.
            Use 100kΩ pull-down resistors if the I/Q interface is disabled (power-down) and the pins RXCLK and RXDxxx
             would be floating when using the SLVDS link option.
                                                                                                     [Errata reference 4860]

15.2.9 Errata #9: RF215M device has a wrong part number
       Description:
       The RF215M device part number is 0x34 instead of 0x36 (register RF_PN.PN).

15.2.10 Errata #10: Missing AGC release upon receive of an invalid legacy O-QPSK frame
       Description:


                                                                                  Atmel AT86RF215 - DATASHEET                      229
                                                                                    Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 230 -->

Upon receive of a legacy O-QPSK frame with an invalid PHR field, the receiver may not correctly release the AGC and
may not listen the next incoming O-QPSK frames. The errata is only relevant if receive of legacy O-QPSK is enabled
(BBCn_PC.PT = 3, BBCn_OQPSKC0.FCHIP > 1 and receive mode BBCn_OQPSKC2.RXM = 1 or
BBCn_OQPSKC2.RXM = 2).
Software workaround:
     Start a timer with the interrupt AGCH.
     Stop the timer if one of the interrupts AGCR or RXFS occurs within the expected period T.
     At timer trigger set BBEN=0 and back to BBEN=1 again.
The expected timer period T depends on the O-QPSK receive mode (OQPSKC2.RXM).
     BBCn_OQPSKC2.RXM = 1 : T = 200 us
     BBCn_QQPSKC2.RXM = 2 : T = 6000 us
                                                                                                   [Errata reference 4908]




                                                                         Atmel AT86RF215 - DATASHEET                     230
                                                                          Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 231 -->

16.     References

[1] IEEE Std 802.15.4™-2006: IEEE Standard for Information technology-- Local and metropolitan area networks--
    Specific requirements-- Part 15.4: Wireless Medium Access Control (MAC) and Physical Layer (PHY) Specifications
    for Low Rate Wireless Personal Area Networks (WPANs)

[2] IEEE Std 802.15.4™-2011: IEEE Standard for Local and metropolitan area networks--Part 15.4: Low-Rate Wireless
    Personal Area Networks (LR-WPANs)

[3] IEEE Std 802.15.4g™-2012: IEEE Standard for Local and metropolitan area networks--Part 15.4: Low-Rate Wireless
    Personal Area Networks (LR-WPANs) Amendment 3: Physical Layer (PHY) Specifications for Low-Data-Rate,
    Wireless, Smart Metering Utility Networks

[4] IEEE Standard for Low-Voltage Differential Signals (LVDS) for Scalable Coherent Interface (SCI) 1596.3-1996.

[5] ETSI TS 102 887-1 V<1.1.1> (2013-07): Electromagnetic compatibility and radio spectrum Matters (ERM); Short
    Range Devices; Smart Metering Wireless Access Protocol (SMEP). Part 1; PHY Layer.

[6] ETSI EN 300 220-1 V2.4.1 (2012-05) Electromagnetic compatibility and Radio spectrum Matters (ERM); Short Range
    Device (SRD)

[7]   IEEE Std 802.15.4™-2015: IEEE Standard for Low-Rate Wireless Personal Area Networks (WPANs)




                                                                             Atmel AT86RF215 - DATASHEET                      231
                                                                               Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 232 -->

17.   Table of Contents
                          1. Description ......................................................................................... 3
                               1.1     Device Family.................................................................................................... 3
                               1.2     Block Diagram ................................................................................................... 4
                               1.3     Control Logic and Naming Conventions ............................................................ 6

                          2. Pin-out Diagram and Description........................................................ 7
                               2.1     Pin-out Diagram ................................................................................................ 7
                               2.2     Pin Description .................................................................................................. 9

                          3. Application Schematic ...................................................................... 11
                          4. Control and Data Interfaces ............................................................. 13
                               4.1     Reset Modes ................................................................................................... 13
                               4.2     SPI Transceiver Control Interface ................................................................... 16
                               4.3     Interrupt Signalling .......................................................................................... 19
                               4.4     Clock Output ................................................................................................... 20
                               4.5     Serial I/Q Data Interface.................................................................................. 22

                          5. Basic Operation ............................................................................... 30
                               5.1     Operating Modes............................................................................................. 30
                               5.2     State Machine ................................................................................................. 33
                               5.3     Interrupts ......................................................................................................... 38
                               5.4     Basic Operation of AT86RF215M ................................................................... 42

                          6. Module Description .......................................................................... 43
                               6.1     Transmitter Frontend .................................................................................... 43
                               6.2     Receiver Frontend ......................................................................................... 52
                               6.3     Frequency Synthesizer (PLL) .......................................................................... 62
                               6.4     Crystal Oscillator and TCXO ........................................................................... 67
                               6.5     External Frontend Control ............................................................................... 70
                               6.6     Voltage Regulator ........................................................................................... 75
                               6.7     Battery Monitor (BATMON) ............................................................................. 78
                               6.8     Analog Calibrations ......................................................................................... 80
                               6.9     Baseband Core ............................................................................................... 81
                               6.10    MR-FSK PHY .................................................................................................. 86
                               6.11    MR-OFDM PHY ............................................................................................ 112
                               6.12    O-QPSK PHY ................................................................................................ 120
                               6.13    Frame Buffer ................................................................................................. 132
                               6.14    Frame Check Sequence ............................................................................... 138
                               6.15    IEEE MAC Support ....................................................................................... 141
                               6.16    Random Number Generator .......................................................................... 161
                               6.17    Phase Measurement Unit .............................................................................. 162
                               6.18    Timestamp Counter....................................................................................... 166

                          7. Transceiver Usage ......................................................................... 169
                               7.1     Transceiver Usage in Baseband Mode ......................................................... 169
                               7.2     Example: Transceiver Usage in Baseband Mode ......................................... 170
                               7.3     Transmitter Usage in I/Q Radio Mode ........................................................... 178
                               7.4     Receiver Usage in I/Q Radio Mode ............................................................... 180

                          8. Register Summary ......................................................................... 181



                                                                                       Atmel AT86RF215 - DATASHEET                                     232
                                                                                         Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 233 -->

9. Package Drawing ........................................................................... 186
10. Electrical Characteristics ................................................................ 187
     10.1 Absolute Maximum Ratings* ......................................................................... 187
     10.2 Operating Range ........................................................................................... 187
     10.3 Digital Pin Specifications ............................................................................... 187
     10.4 Power-on Reset Characteristics .................................................................... 188
     10.5 General Transceiver Specifications............................................................... 188
     10.6 Crystal Oscillator Specification ...................................................................... 188
     10.7 Clock Output – pin CLKO .............................................................................. 189
     10.8 Transition Time ............................................................................................. 189
     10.9 Transmitter Characteristics ........................................................................... 190
     10.10 Receiver Characteristics ............................................................................... 194
     10.11 Current Consumption Specifications ............................................................. 203
     10.12 SPI Timing Characteristics ............................................................................ 204
     10.13 I/Q Data Interface Driver DC and Startup Specification ................................ 205
     10.14 I/Q Data Interface Receiver DC and Startup Specification ............................ 206
     10.15 I/Q Data Interface Driver AC Specification .................................................... 206
     10.16 I/Q Data Interface Receiver AC Specification ............................................... 207
     10.17 Digital Block Timing Specification ................................................................. 207

11. Typical Characteristics .................................................................. 208
     11.1     Output Power at Several Modulations ........................................................... 208
     11.2     Output Power versus Supply Voltage ............................................................ 209
     11.3     TX Current Consumption and Output Power at PAC.PACUR settings .......... 211
     11.4     TX Output Power at Temperature Sweep ..................................................... 214
     11.5     TX Output Power at Frequency Sweep ......................................................... 214
     11.6     Receiver Sensitivity ....................................................................................... 216
     11.7     Frequency Synthesizer (PLL) ........................................................................ 217

12. Acronyms and Abbreviations .......................................................... 218
13. Appendix ........................................................................................ 221
     13.1     Continuous Transmission .............................................................................. 221

14. Ordering Information ...................................................................... 224
15. Errata                                              ........................................................ 225
     15.1     Errata Overview ............................................................................................ 225
     15.2     Errata AT86RF215 Description ..................................................................... 225

16. References .................................................................................... 231
17. Table of Contents ........................................................................... 232
18. Revision History ............................................................................. 234




                                                           Atmel AT86RF215 - DATASHEET                                  233
                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 234 -->

18.   Revision History
      Doc Rev.   Date      Comments
      42415E     05/2016   Section "MR-FSK PHY":
                                - Information in section "Direct Modulation RF215 v.3 (RF_VN = 0x03)" added
                                     (Pre-emphasis setting for FSK direct modulation)
                           Section "SPI Transceiver Control Interface":
                                - Correction of tSPI_5 in "SPI Timing"
                           Reference to IEEE Std 802.15.4TM-2015 [7]
                           Information of "Frequency Synthesizer (PLL)" in section "Typical Characteristics"
                           added
      42415D     11/2015   Section Errata:
                                - RF215M information added "Errata Overview"
                                - Errata 7: improved SW workaround "Errata AT86RF215 Description"
                           Section MR-FSK PHY "MR-FSK PHY"
                                - Default AGC receiver setting added (Table 6-60/Table 6-62/Table 6-61/Table
                                     6-63)
                           Section Frequency Synthesizer (PLL) "Frequency Synthesizer (PLL)"
                                - Description for sub-register PLL.LBW improved (PLL.LBW)
                           Section IEEE MAC Support ("IEEE MAC Support")
                                - Description of section "Clear Channel Assessment with Automatic Transmit
                                     (CCATX)" and "Transmit and Switch to Receive (TX2RX)" extended
      42415C     07/2015   RF215-v.3 information:
                                - FSK sample rate TXDFE.SR ( Table 6-51)
                                - FSK direct modulation ("Direct Modulation RF215 v.3 (RF_VN = 0x03)")
                                - QPSK direct modulation ("Direct Modulation RF215 v.3 (RF_VN = 0x03)")
                                - Additional information in section "Typical Characteristics"
                           Additional information in section
                           Update and additional information in section "Electrical Characteristics"
                           Editorial updates
      42415B     04/2015   Added Ordering Information
      42415A     03/2015   Initial document release




                                                                     Atmel AT86RF215 - DATASHEET                      234
                                                                       Atmel-42415E-WIRELESS-RF215_Datasheet_052016

<!-- page 235 -->

Atmel Corporation                              Atmel Asia Limited                             Atmel Munich GmbH                              Atmel Japan G.K.
1600 Technology Drive                          Unit 01-5 & 16, 19F                            Business Campus                                16F Shin-Osaki Kangyo Bldg.
San Jose, CA 95110                             BEA Tower, Millennium City 5                   Parkring 4                                     1-6-4 Osaki, Shinagawa-ku
USA                                            418 Kwun Tong Road                             D-85748 Garching b. Munich                     Tokyo 141-0032
Tel: (+1)(408) 441-0311                        Kwun Tong, Kowloon                             GERMANY                                        JAPAN
Fax: (+1)(408) 487-2600                        HONG KONG                                      Tel: (+49) 89-31970-0                          Tel: (+81)(3) 6417-0300
www.atmel.com                                  Tel: (+852) 2245-6100                          Fax: (+49) 89-3194621                          Fax: (+81)(3) 6417-0370
                                               Fax: (+852) 2722-1369



© 2016 Atmel Corporation. All rights reserved. / Rev.: Atmel-42415E-WIRELESS-RF215_Datasheet_052016

Atmel®, Atmel logo and combinations thereof, Enabling Unlimited Possibilities®, and others are registered trademarks or trademarks of Atmel
Corporation or its subsidiaries. Other terms and product names may be trademarks of others.

Disclaimer: The information in this document is provided in connection with Atmel products. No license, express or implied, by estoppel or otherwise, to any intellectual property right
is granted by this document or in connection with the sale of Atmel products. EXCEPT AS SET FORTH IN THE ATMEL TERMS AND CONDITIONS OF SALES LOCATED ON THE
ATMEL WEBSITE, ATMEL ASSUMES NO LIABILITY WHATSOEVER AND DISCLAIMS ANY EXPRESS, IMPLIED OR STATUTORY WARRANTY RELATING TO ITS PRODUCTS
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. IN NO EVENT
SHALL ATMEL BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE, SPECIAL OR INCIDENTAL DAMAGES (INCLUDING, WITHOUT LIMITATION,
DAMAGES FOR LOSS AND PROFITS, BUSINESS INTERRUPTION, OR LOSS OF INFORMATION) ARISING OUT OF THE USE OR INABILITY TO USE THIS DOCUMENT,
EVEN IF ATMEL HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. Atmel makes no representations or warranties with respect to the accuracy or completeness of
the contents of this document and reserves the right to make changes to specifications and products descriptions at any time without notice. Atmel does not make any commitment to
update the information contained herein. Unless specifically provided otherwise, Atmel products are not suitable for, and shall not be used in, automotive applications. Atmel products
are not intended, authorized, or warranted for use as components in applications intended to support or sustain life.




                                                                                                           Atmel AT86RF215 - DATASHEET                                                     235
                                                                                                             Atmel-42415E-WIRELESS-RF215_Datasheet_052016
