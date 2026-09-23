# MP2672AGD

*Source: `MP2672AGD.pdf` (43 pages) — converted from PDF*


<!-- page 1 -->

MP2672A
                                                                     Boost Charger with Cell Balance for
                                                                    2-Cell Lithium-Ion Batteries in Series
DESCRIPTION                                                            FEATURES
The MP2672A is a highly integrated, flexible                               4.0V to 5.75V Operating Input Voltage
switch-mode battery charger IC for Lithium-ion                             Up to 14V Sustainable Voltage
batteries with two cells in series. This makes it                          Up to 2A Configurable Charge Current for
applicable for a wide range of portable                                     Battery with 2 Cells in Series
applications.                                                              Compatible with Host-Control or Standalone
When an input power supply is present, the                                  Mode
MP2672A operates in boost mode to charge the                               NVDC Power Path Management
battery with two cells in series. When charging is                         Configurable Input Voltage Limit
enabled, the MP2672A automatically detects the                             Configurable Charge Voltage with 0.5%
battery voltage and charges the battery in three                            Accuracy
phases: pre-charge, constant current charge,                               No External Sense Resistor Required
and constant voltage charge. Other features                                Integrated Cell-Balancing Circuit for
include charge termination and auto-recharge.                               Mismatched Cells
The device also has a narrow voltage DC (NVDC)                             Preconditioning for Fully Depleted Battery
power structure. With a deeply discharged                                  Flexible New Charging Cycle Initiation
battery, the MP2672A regulates the system                                  Charging Operation Indicator in Standalone
output to a minimum voltage level. This powers                              Mode
the system instantly while simultaneously                                  Missing Battery Detection in Host-Control
charging the battery via the battery FET.                                   Mode
                                                                           I2C Port for Flexible System Parameter
The MP2672A provides a cell balance function.                               Setting and Status Reporting in Host-
It can monitor the voltage across each cell, then                           Control Mode
equalize the cell’s voltages if the difference
                                                                           Negative Temperature Coefficient (NTC)
between the two cells exceeds the mismatch
                                                                            Pin for Temperature Monitoring Compliant
threshold.
                                                                            with JEITA Standards
The device has two configuration modes:                                    Built-In Charging Protection and
standalone mode and host-control mode. In                                   Configurable Safety Timer
standalone mode, the charging parameters can                               MOSFET Cycle-by-Cycle Over-Current
be configured by hardware pins. In host-control                             Protection (OCP)
mode, the charging parameters can be                                       Thermal Regulation and Thermal Shutdown
configured by the I2C registers.                                           Available in a QFN-18 (2mmx3mm)
Diverse and robust protections include a thermal                            Package
regulation loop to decrease the charge current in
                                                                       APPLICATIONS
case the junction temperature exceeds the
thermal loop threshold, and battery temperature                            Portable Handheld Solutions
protection that is compliant with JEITA standards.                         Point-of-Sale (POS) Machines
Other safety features include input over-voltage                           Bluetooth Speakers
protection (OVP), battery OVP, thermal                                     E-Cigarettes
shutdown, battery temperature monitoring, a                                General 2-Cell Applications
watchdog timer, and a configurable backup timer
                                                                       All MPS parts are lead-free, halogen-free, and adhere to the RoHS directive.
to prevent prolonged charging of a dead battery.                       For MPS green status, please visit the MPS website under Quality
                                                                       Assurance. “MPS”, the MPS logo, and “Simple, Easy Solutions” are
The MP2672A is available in a QFN-18                                   trademarks of Monolithic Power Systems, Inc. or its subsidiaries.
(2mmx3mm) package.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                                     1
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 2 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL APPLICATIONS
Standalone Mode
Use a resistor to connect the CV pin to AGND. Set the battery-full voltage according to Table 1.
                                               Table 1: Battery Voltage Settings
                                               RVBATT Range                VBATT_REG
                                               30kΩ to 35kΩ                  8.4V
                                               70kΩ to 75kΩ                  8.6V
                                            100kΩ to 105kΩ                   8.7V
                                            130kΩ to 135kΩ                   8.8V




                                                                                SYS
                                                  BST
                                                                     Q2                Q3
                                L1                                                          BATT
             VIN                                  SW
                                                              Q1
                                                  IN                                                         CBATT
                 CIN
                        RH

                                                  VLIM
                                                                                            MID
                        RL                                    MP2672A
                                                  ACOK
                                                                                            VCC
                                                  STAT
                       VCC
                                                                                        AGND                   RT1
                                                  CV

                                                                                            NTC
                                                   ISET
                                                                                                               RT2
                   RVBATT              RISET                         PGND
                                                                                                                RNTC


                                   Figure 1: Typical Application in Standalone Mode




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                           2
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| R Range VBATT | V BATT_REG |
| --- | --- |
| 30kΩ to 35kΩ | 8.4V |
| 70kΩ to 75kΩ | 8.6V |
| 100kΩ to 105kΩ | 8.7V |
| 130kΩ to 135kΩ | 8.8V |


<!-- page 3 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL APPLICATIONS (continued)
Host-Control Mode
Connect the CV pin to VCC. Set the battery-full voltage according to the I2C register (see Figure 2).




                                                                                SYS
                                                  BST
                                                                    Q2                Q3
                                L1                                                         BATT
             VIN                                  SW
                                                             Q1
                                                  IN                                                         CBATT
                CIN
                        RH

                                                  VLIM
                                                                                           MID
                        RL                                    MP2672A
                                                  ACOK
                                                                                           VCC
                                                  STAT
                      VCC
                                                                                        AGND                   RT1
                                                  CV
                                                  SDA
                      MCU                                                                  NTC
                                                  SCL
                                                  ISET                                                         RT2

                                                                     PGND
                                      RISET                                                                    RNTC



                                  Figure 2: Typical Application in Host Control Mode




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                          3
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 4 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

                                           ORDERING INFORMATION
                     Part Number*                     Package                  Top Marking          MSL Rating
                 MP2672AGD-xxxx**              QFN-18 (2mmx3mm)                 See Below                 1
                  EVKT-MP2672A                   Evaluation kit                    N/A                   N/A
                             *For Tape & Reel, add suffix –Z (e.g. MP2672AGD–xxxx–Z).
    **“-xxxx” is the register setting option. The factory default is “-0000”. This content can be viewed in the I2C
  Register Map section starting on page 28. For custom options, contact an MPS FAE to obtain an “-xxxx” value.

                                                      TOP MARKING




                     BNJ: Product code
                     Y: Year code
                     WW: Week code
                     LLLL: Lot number


                                    EVALUATION KIT EVKT-MP2672A
    EVKT-MP2672A kit contents (items below can be ordered separately):
        #       Part Number                    Item                                                                  Quantity
        1       EV2672A-D-00A                  MP2672A evaluation board                                                 1
                                               Includes one USB to I2C communication interface, one
        2       EVKT-USBI2C-02 bag                                                                                      1
                                               USB cable, and one ribbon cable
        3       Online resources               Include datasheet, user guide, product brief, and GUI                    1

                        Order directly from MonolithicPower.com or our distributors.

                                                                                            Input Power
                                                                                               Supply


                                                                          Ribbon
                                                             2
             GUI              USB Cable           USB to I C               Cable
                                                Communication                             EV2672A-D-00A                 Battery
                                                   Interface




                                                                                                Load


                                     Figure 3: EVKT-MP2672A Evaluation Kit Set-Up




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                      4
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Part Number* | Package | Top Marking | MSL Rating |
| --- | --- | --- | --- |
| MP2672AGD-xxxx** | QFN-18 (2mmx3mm) | See Below | 1 |
| EVKT-MP2672A | Evaluation kit | N/A | N/A |

| # | Part Number | Item | Quantity |
| --- | --- | --- | --- |
| 1 | EV2672A-D-00A | MP2672A evaluation board | 1 |
| 2 | EVKT-USBI2C-02 bag | Includes one USB to I2C communication interface, one USB cable, and one ribbon cable | 1 |
| 3 | Online resources | Include datasheet, user guide, product brief, and GUI | 1 |


<!-- page 5 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

                                             PACKAGE REFERENCE




                                                   ACOK




                                                                   STAT

                                                                          SDA

                                                                                SCL
                                                            CV
                                                   18      17      16     15    14



                                        IN     1                                    13     PGND

                                       SW      2                                    12     SW

                                      BST      3                                    11     SYS

                                     VCC       4                                      10   BATT



                                                   5        6       7      8    9
                                                   ISET


                                                            AGND

                                                                   VLIM

                                                                          NTC

                                                                                MID
                                                          QFN-18 (2mmx3mm)




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                         5
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 6 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

PIN FUNCTIONS
     Pin #     Name               Type (1)   Description
      1             IN               P       Input power pin.
                                             Switching node. The SW pin is the middle point between the MP2672A’s high-side
     2, 12        SW                 P
                                             and low-side MOSFETs.
                                             Bootstrap. Connect a bootstrap capacitor between the BST and SW pins to provide
      3          BST                 P
                                             a floating supply for the high-side FET driver.
                                             Internal LDO output pin. Bypass a 1µF ceramic capacitor from this pin to AGND.
      4          VCC                 P
                                             It is not recommended to pull more than 20mA from this pin.
                                             Charge current setting. Connect an external resistor from this pin to AGND to
      5         ISET                AI       configure the charge current. This also limits the maximum charge current in host-
                                             control mode.
      6        AGND                  P       Analog ground.
                                             Input voltage limit feedback pin. Connect a resistor divider from IN to AGND to
      7         VLIM                AI
                                             configure the minimum input voltage limit threshold.
                                             Battery temperature-sense input. Connect NTC to a negative temperature
                                             coefficient thermistor. Configure the temperature window with a voltage divider
      8          NTC                AI       connected from VRNTC to NTC to AGND. Configurable JEITA thresholds are
                                             supported. See the Negative Temperature Coefficient (NTC) Thermistor section on
                                             page 23 for more details.
                                             Middle point of the high-side and low-side cells. The MID pin measures the
      9          MID                 P       voltage of each cell and provides a balance path for each cell. Connect MID to
                                             AGND to disable the cell balance function.
                                             Battery positive terminal. Connect a capacitor from BATT to PGND, and place it
      10        BATT                 P
                                             as close as possible to the IC.
                                             System output. Connect a capacitor from SYS to PGND, and place it as close as
      11         SYS                 P
                                             possible to the IC.
      13       PGND                 P        Power ground.
      14        SCL                 DI       I2C interface clock pin. This pin is only valid if the CV pin is connected to VCC.
      15        SDA                DIO       I2C interface data pin. This pin is only valid if the CV pin is connected to VCC.
                --------------
      16        STAT                DO       Charging operation indicator. This pin is an open-drain output.
                                             Operation mode and battery voltage control pin. Pull CV to VCC to configure
                                             the IC to host-control mode. Connect an external resistor to AGND to configure IC
      17           CV               AI
                                             to standalone mode. In standalone mode, configure the battery-full voltage via the
                                             CV pin’s resistor.
               ----------------
                                             Valid input supply indicator. This pin is an open-drain output. It is pulled low when
      18       ACOK                 DO       the input voltage exceeds the under-voltage lockout threshold (VIN_UVLO) and is
                                             below the over-voltage lockout threshold (VIN_OVLO).
Note:
1)     AI = analog input, DI = digital input, DO = digital output, DIO = digital input and output, P = power.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                     6
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Pin # | Name | Type (1) | Description |
| --- | --- | --- | --- |
| 1 | IN | P | Input power pin. |
| 2, 12 | SW | P | Switching node. The SW pin is the middle point between the MP2672A’s high-side and low-side MOSFETs. |
| 3 | BST | P | Bootstrap. Connect a bootstrap capacitor between the BST and SW pins to provide a floating supply for the high-side FET driver. |
| 4 | VCC | P | Internal LDO output pin. Bypass a 1µF ceramic capacitor from this pin to AGND. It is not recommended to pull more than 20mA from this pin. |
| 5 | ISET | AI | Charge current setting. Connect an external resistor from this pin to AGND to configure the charge current. This also limits the maximum charge current in host- control mode. |
| 6 | AGND | P | Analog ground. |
| 7 | VLIM | AI | Input voltage limit feedback pin. Connect a resistor divider from IN to AGND to configure the minimum input voltage limit threshold. |
| 8 | NTC | AI | Battery temperature-sense input. Connect NTC to a negative temperature coefficient thermistor. Configure the temperature window with a voltage divider connected from VRNTC to NTC to AGND. Configurable JEITA thresholds are supported. See the Negative Temperature Coefficient (NTC) Thermistor section on page 23 for more details. |
| 9 | MID | P | Middle point of the high-side and low-side cells. The MID pin measures the voltage of each cell and provides a balance path for each cell. Connect MID to AGND to disable the cell balance function. |
| 10 | BATT | P | Battery positive terminal. Connect a capacitor from BATT to PGND, and place it as close as possible to the IC. |
| 11 | SYS | P | System output. Connect a capacitor from SYS to PGND, and place it as close as possible to the IC. |
| 13 | PGND | P | Power ground. |
| 14 | SCL | DI | I2C interface clock pin. This pin is only valid if the CV pin is connected to VCC. |
| 15 | SDA | DIO | I2C interface data pin. This pin is only valid if the CV pin is connected to VCC. |
| 16 | -------------- STAT | DO | Charging operation indicator. This pin is an open-drain output. |
| 17 | CV | AI | Operation mode and battery voltage control pin. Pull CV to VCC to configure the IC to host-control mode. Connect an external resistor to AGND to configure IC to standalone mode. In standalone mode, configure the battery-full voltage via the CV pin’s resistor. |
| 18 | ---------------- ACOK | DO | Valid input supply indicator. This pin is an open-drain output. It is pulled low when the input voltage exceeds the under-voltage lockout threshold (V ) and is IN_UVLO below the over-voltage lockout threshold (V ). IN_OVLO |


<!-- page 7 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

ABSOLUTE MAXIMUM RATINGS (2)                                              Thermal Resistance (7)                   θJA        θJC
BATT .............................................-0.3V to +14V           QFN-18 (2mmx3mm) .............. 70 ...... 15... °C/W
SW .........................-0.3V (-2V for 50ns) to +14V
SYS ...............................................-0.3V to +14V          Notes:
                                                                          2) Exceeding these ratings may damage the device.
MID, IN ..........................................-0.3V to +12V           3) The maximum allowable power dissipation is a function of the
BST to SW………….. ......................-0.3V to +5V                           maximum junction temperature, TJ (MAX), the junction-to-
All other pins to AGND ....................-0.3V to +5V                      ambient thermal resistance, θJA, and the ambient temperature,
                                                                             TA. The maximum allowable continuous power dissipation at
Continuous power dissipation .......(TA = 25°C) (3)                          any ambient temperature is calculated by PD (MAX) = (TJ
................................................................. 1.78W      (MAX) - TA) / θJA. Exceeding the maximum allowable power
Junction temperature ................................150°C                   dissipation can cause excessive die temperature, and the
                                                                             regulator may go into thermal shutdown. Internal thermal
Lead temperature (solder) ........................260°C                      shutdown circuitry protects the device from permanent
Storage temperature…………...-65°C to +150°C                                    damage.
                                                                          4) The device is not guaranteed to function outside of its operating
ESD Ratings                                                                  conditions.
                                                                          5) Per ANSI/ESDA/JEDEC JS-001.
Human body model (HBM) (5) .................. 2000V                       6) Per JESD22-C101.
Charged device model (CDM) (6) ............... 250V                       7) Measured on JESD51-7, 4-layer PCB.

Recommended Operating Conditions (4)
IN to PGND………………………….. 4V to 5.75V
BATT to PGND ..................................... Up to 9V
ICC.......................................................... Up to 2A
IDSCHG..................................................... Up to 3A
ISYS ........................................................ Up to 2A
Operating junction temp (TJ) .... -40°C to +125°C




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                                7
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 8 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

ELECTRICAL CHARACTERISTICS
VIN = 5V, TA = 25°C, unless otherwise noted.
Parameter                              Symbol Condition                                          Min       Typ       Max    Units
Input Power Characteristics
Input over-voltage lockout
                                       VIN_OVLO    VIN rising                                    5.75       6.0      6.25    V
(OVLO) threshold
Input OVLO threshold
                                                                                                           150              mV
hysteresis
Input under-voltage lockout
                                       VIN_UVLO    VIN falling                                   3.25      3.45      3.65    V
(UVLO) threshold
Input UVLO threshold
                                                                                                           150              mV
hysteresis
Boost Converter
VCC LDO output                           VVCC      VIN = 5V, IVCC = 20mA                         3.5        3.6      3.7     V
Low-side N-channel MOSFET
                                        RON_Q1                                                              54        70    mΩ
on resistance
High-side N-channel MOSFET
                                        RON_Q2                                                              28        40    mΩ
on resistance
Peak current limit for low-side
                                         ILS_PK    VIN=5V                                         6          7               A
N-channel MOSFET
Valley current limit for high-
                                         IHS_VL    VIN=5V                                         5          6               A
side N-channel MOSFET
Operating frequency                       fSW      REG07H, bit[7] = 1                           1100       1270      1440   kHz
System regulation minimum                          REG00H, bits[3:1] = 100,
                                                                                                 6.55       6.7      6.85    V
voltage (VBATT_PRE + VTRACK)                       VBATT = 5V
Battery track regulation
                                        VTRACK                                                             300              mV
voltage
Battery Charger
                                                   REG00H, bits[3:1] = 000                       5.9       6.05      6.2
Pre-charge threshold                  VBATT_PRE    REG00H, bits[3:1] = 100                      6.25       6.4       6.55    V
                                                   REG00H, bits[3:1] = 111                      6.6        6.75      6.9
Pre-charge threshold
                                                   VBATT falling                                           250              mV
hysteresis
Pre-charge current                        IPRE     VBATT = 5.9V                                  230       320       410    mA




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                      8
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 9 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

ELECTRICAL CHARACTERISTICS (continued)
VIN = 5V, TA = 25°C, unless otherwise noted.
Parameter                                 Symbol       Condition                              Min        Typ         Max     Units
                                                       REG01H, bits[3:0] = 0101,
                                                                                               0.9        1           1.1     A
                                                       RISET = 6kΩ
Fast charge current                          ICC
                                                       REG01H, bits[3:0] = 1111,
                                                                                               1.8        2           2.2     A
                                                       RISET = 6kΩ
                                                       If ICC > 1.5A,
                                                                                                8         11          14      %
Termination charge current                  ITERM      as a percentage of ICC
                                                       If ICC ≤ 1.5A (setting)                130        160         190      mA
Input minimum voltage
                                         VIN_MIN_REF                                          1.18       1.2         1.22     V
regulation reference
                                                      VBATT_REG = 8.3V, host-control
                                                      mode, REG00H, bits[7:5] = 000
                                                      VBATT_REG = 8.4V,
                                                      host-control mode: REG00H,
                                                      bits[7:5] = 001,
                                                      standalone mode:
Battery charge voltage                                RVBATT = 30kΩ
                                        VBATT_REG_ACC                                        -0.50                   +0.50    %
regulation                                            VBATT_REG = 8.8V,
                                                      host-control mode: REG00H,
                                                      bits[7:5] = 101,
                                                      standalone mode:
                                                      RVBATT = 135kΩ
                                                      VBATT_REG = 8.2V, host-control
                                                      mode, REG00H, bits[7:5] = 111
Recharge threshold below
                                           VRECH                                                         450                  mV
VBATT_REG
Battery pack over-voltage
                                         VBATT_OVP     As a percentage of VBATT_REG           102        104         105      %
protection (OVP) threshold
Battery pack OVP
                                                       REG00H, bit[0] = 0                                150                  mV
hysteresis
SYS-to-BATT N-channel
                                           RON_Q3                                              22         31          40     mΩ
MOSFET on resistance
                                                       VIN < VIN_UVLO, VBATT = 8.4V,
Battery quiescent current                  IBATT_Q                                             19         31          42      μA
                                                       system no load
----------------   --------------
ACOK, STAT, pin output                                 Sinking 1.5mA                                                 400      mV
low voltage
----------------   ---------------
ACOK, STAT, pin leakage                                Connected to 5V                                                1       μA
current




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                         9
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 10 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

ELECTRICAL CHARACTERISTICS (continued)
VIN = 5V, TA = 25°C, unless otherwise noted.
Parameter                                 Symbol        Condition                             Min        Typ         Max    Units
Termination deglitch time                 tTERM_DGL                                                      180                 ms
Recharge deglitch time                    tRECH_DGL                                                      180                 ms
Battery Temperature Monitoring (JEITA)
NTC low temp rising threshold    VCOLD                  As a percentage of VCC                 70        71          72      %
NTC low temp rising threshold
                                                        As a percentage of VCC                           2.4                 %
hysteresis
NTC cool temp rising threshold   VCOOL                  As a percentage of VCC                 62        63          64      %
NTC cool temp rising threshold
                                                        As a percentage of VCC                           2.2                 %
hysteresis
NTC warm temp falling
                                VWARM                   As a percentage of VCC                39.4      40.4         41.4    %
threshold
NTC warm temp falling
                                                        As a percentage of VCC                           2.5                 %
threshold hysteresis
NTC hot temp falling threshold   VHOT                   As a percentage of VCC                33.5      34.5         35.5    %
NTC hot temp falling threshold
                                                        As a percentage of VCC                           2.5                 %
hysteresis
Thermal Regulation and Protection
Thermal shutdown
                                TJ_SHDN                 Rising threshold                                 150                 °C
temperature
Thermal shutdown hysteresis                             Temperature falling                              20                  °C
Cell Balance Function
Internal balance FET on                   RON_BHS                                                        2.1                 Ω
resistance                                RON_BLS                                                        1.3                 Ω
                                                         2
Cell balance starting voltage                           I C-configurable,
                                         VCELL_BAL                                            3.35       3.5         3.65    V
threshold                                               REG01H, bit[6] = 0
Cell voltage high-to-low cell
                                       VCELL_DIFF_HTL REG01H, bit[5] = 0                                 50          70     mV
mismatch threshold
Cell voltage high-to-low cell
                                                                                                         52                 mV
mismatch threshold hysteresis
Cell voltage low-to-high cell
                                       VCELL_DIFF_LTH REG01H, bit[4] = 0                                 50          70     mV
mismatch threshold
Cell voltage low-to-high cell
                                                                                                         58                 mV
mismatch threshold hysteresis
                                                        As a percentage of the
High-side cell OVP threshold             VHCELL_OVP                                           101       102.5        104     %
                                                        battery-full voltage
                                                        As a percentage of the
Low-side OVP threshold                   VLCELL_OVP                                           101       102.5        104     %
                                                        battery-full voltage




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                      10
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 11 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

ELECTRICAL CHARACTERISTICS (continued)
VIN = 5V, TA = 25°C, unless otherwise noted.
Parameter                              Symbol Condition                                     Min         Typ          Max   Units
 2
I C Communication Interface
Input high threshold level                VIH      VPULL UP = 1.8V                          1.3                             V
Input low threshold level                  VIL     VPULL_UP = 1.8V                                                   0.4    V
Output low threshold level                VOL      ISINK = 5mA                                                       0.4    V
I2C clock frequency                       fSCL                                                                       400   kHz
Timing Characteristics
Clock frequency                           fCLK                                                          131                kHz
Watchdog timer(8)                         tWTD     REG02H, bits[5:4] = 01                                40                sec
                                                   I2C-configurable,
Safety charge timer                       tTMR                                               16          20                hours
                                                   REG02H, bits[2:1] = 11
Pre-charge timer                                                                                          1                hours
Note:
8) Guaranteed by design




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                    11
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 12 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL CHARACTERISTICS
                       IPRE vs. Junction Temperature
                       VBATT = 5V
                                                                                                  ICC vs. Junction Temperature
                600                                                                     2.50



                450                                                                     2.00
IPRE (mA)




                                                                        ICC (A)
                300                                                                     1.50                                   ICC=1A
                                                                                                                               ICC=2A

                150                                                                     1.00



                  0                                                                     0.50
                      -50           0       50      100           150                            -50   -25   0   25 50 75 100 125 150
                                     TEMPERATURE (°C)                                                         TEMPERATURE (°C)

                                                                                                  VBATT_REG vs. Junction Temperature
                       ITERM vs. Junction Temperature                                             VBATT_REG = 8.4V
                250                                                                        8.5


                200
                                                                                           8.4
                                                                        VBATT_REG (V)
  ITERM (mA)




                150
                                                                                           8.3
                100

                                                                                           8.2
                 50                                      ICC=1A
                                                         ICC=2A
                  0                                                                        8.1
                      -50           0       50      100           150                            -50         0       50      100        150
                                     TEMPERATURE (°C)                                                         TEMPERATURE (°C)

                                                                                                  Battery Cell OVP vs. Junction
                       VBATT_PRE vs. Junction Temperature                                         Temperature
                6.5                                                                     105


                                                                                        104
                                                                        BATTERY CELL OVP
                                                                          THRESHOLD (%)




                6.4
VBATT_PRE (V)




                                                                                        103


                                                                                        102
                6.3
                                                                                                                        LS_Cell_OVP
                                                                                        101
                                                                                                                        HS_Cell_OVP

                6.2                                                                     100
                      -50           0          50      100        150                            -50         0       50      100        150
                                        TEMPERATURE (°C)                                                      TEMPERATURE (°C)



MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                              12
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 13 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL PERFORMANCE CHARACTERISTICS
VIN = 5V, TA = 25°C, unless otherwise noted.

                      Constant Current Mode Charge                                            Constant Voltage Mode Charge
                      Efficiency                                                              Efficiency
                      VIN = 5V, fSW = 1200kHz , L = 1.5μH,                                    VIN = 5V, fSW = 1200kHz, L = 1.5μH,
                      (DCR = 10mΩ), ISYS = 0A                                                 (DCR = 10mΩ), VBATT = 8.4V, ISYS = 0A
                1                                                                    1


              0.95                                                                 0.95




                                                                      EFFICIENCY
 EFFICIENCY




               0.9                                                                  0.9


              0.85                                                                 0.85
                                                       ICC=2A
                                                       ICC=1A
               0.8                                                                  0.8
                     6.4        6.9        7.4        7.9       8.4                       0           0.5         1         1.5       2
                                        VBATT (V)                                                             IBATT (A)

                      Configurable Charge Current
                      Standalone mode
               2.5

                2

               1.5
  ICC (A)




                1

               0.5

                0
                     5          10         15         20        25
                                      RISET (kΩ)




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                              13
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 14 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL PERFORMANCE CHARACTERISTICS (continued)
VIN = 5V, VBATT_PRE = 6.5V, ICC = 2A, ISYS = 0A, VBATT = 0V to 8.4V, CIN = 10μF, CSYS = 44μF,
CBATT = 22μF, L = 1.5μH, fSW = 1200kHz, TA = 25°C, unless otherwise noted.

                           Battery Charge Curve                                                Auto-Recharge
                           VBATT_REG = 8.4V                                                    VBATT_REG = 8.4V




   CH2: VSYS                                                           CH2: VSYS
     2V/div.                                                             2V/div.
  CH1: VBATT                                                          CH1: VBATT
     2V/div.                                                             2V/div.
  CH4: IBATT                                                           CH4: IBATT
 500mA/div.                                                           500mA/div.
      ------------------                                                  ------------------
 CH3: STAT                                                           CH3: STAT
     2V/div.                                                             2V/div.
                                               4s/div.                                                               2s/div.


                                                                                               Constant Current Charge Steady
                           Pre-Charge Steady State                                             State
                           VBATT = 5V                                                          VBATT = 7.4V




  CH1: VBATT
     2V/div.                                                          CH1: VBATT
  CH3: IBATT                                                             2V/div.
 500mA/div.                                                            CH3: IBATT
                                                                      500mA/div.
     CH4: IL
                                                                        CH4: IL
     1A/div.
                                                                        1A/div.
   CH2: VSW                                                            CH2: VSW
     5V/div.                                                             5V/div.
                                               1μs/div.                                                              1μs/div.



                           Constant Voltage Charge Steady                                      Constant Voltage Charge Steady
                           State                                                               State
                           VBATT = 8.4V (1A)                                                   VBATT = 8.4V (0.5A)




                                                                      CH1: VBATT
  CH1: VBATT
                                                                         2V/div.
     2V/div.
                                                                       CH3: IBATT
  CH3: IBATT
                                                                      500mA/div.
 500mA/div.
                                                                        CH4: IL
    CH4: IL
                                                                        1A/div.
    1A/div.
                                                                       CH2: VSW
   CH2: VSW
                                                                         5V/div.
     5V/div.
                                               1μs/div.                                                              1μs/div.



MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                    14
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 15 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL PERFORMANCE CHARACTERISTICS (continued)
VIN = 5V, VBATT_PRE = 6.5V, ICC = 2A, ISYS = 0A, VBATT = 0V to 8.4V, CIN = 10μF, CSYS = 44μF,
CBATT = 22μF, L = 1.5μH, fSW = 1200kHz, TA = 25°C, unless otherwise noted.

                 Start-Up through VIN                                              Shutdown through VIN
                 VBATT = 7.4V                                                      VBATT = 7.4V




     CH1: VIN                                                          CH1: VIN
      2V/div.                                                           2V/div.

   CH2: VBATT                                                        CH2: VBATT
      2V/div.                                                           2V/div.
    CH4: IBATT                                                        CH4: IBATT
      1A/div.                                                           1A/div.
    CH3: VSW                                                          CH3: VSW
      5V/div.                                                           5V/div.
                                    40ms/div.                                                         40ms/div.


                 Boost Enabled                                                     Boost Disabled
                 VBATT = 7.4V                                                      VBATT = 7.4V


     CH1: VIN                                                          CH1: VIN
      2V/div.                                                           2V/div.




   CH2: VBATT                                                        CH2: VBATT
      2V/div.                                                           2V/div.
    CH4: IBATT                                                        CH4: IBATT
      1A/div.                                                           1A/div.
    CH3: VSW                                                          CH3: VSW
      5V/div.                                                           5V/div.
                                    40ms/div.                                                         40ms/div.



                 Constant Current Charge Enabled                                   Constant Current Charge Disabled
                 VBATT = 7.4V, MP2672A-0000                                        VBATT = 7.4V, MP2672A-0000


   CH1: VBATT                                                        CH1: VBATT
      2V/div.                                                           2V/div.




    CH2: VSYS                                                         CH2: VSYS
      2V/div.                                                           2V/div.
    CH4: IBATT                                                        CH4: IBATT
      1A/div.                                                           1A/div.
    CH3: VSW                                                          CH3: VSW
      5V/div.                                                           5V/div.
                                    20ms/div.                                                         20ms/div.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                          15
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 16 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL PERFORMANCE CHARACTERISTICS (continued)
VIN = 5V, VBATT = 0V to 8.4V, CIN = 10μF, CSYS = 44μF, CBATT = 22μF, L = 1.5μH, fSW = 1200kHz,
TA = 25°C, unless otherwise noted.

                            Constant Current Charge Enabled                                             Constant Current Charge Disabled
                            VBATT = 7.4V, MP2672A-000E                                                  VBATT = 7.4V, MP2672A-000E




   CH1: VBATT                                                                  CH1: VBATT
      2V/div.                                                                     2V/div.
    CH2: VSYS                                                                   CH2: VSYS
      2V/div.                                                                     2V/div.
    CH4: IBATT                                                                  CH4: IBATT
      1A/div.                                                                     1A/div.
    CH3: VSW                                                                    CH3: VSW
      5V/div.                                                                     5V/div.
                                               400μs/div.                                                                   20μs/div.


                            Standard NTC Protection                                                     JEITA NTC Protection
                            VBATT = 7.4V, standard NTC, ICC = 2A,                                       VBATT = 8.15V, JEITA NTC, ICC = 2A,
                            vary V_NTC                                                                  vary V_NTC




                                                                               CH2: VBATT
   CH2: VBATT                                                                     2V/div.
      2V/div.                                                                   CH1: VNTC
    CH1: VNTC                                                                     1V/div.
      1V/div.                                                                         CH3:
       ------------------
                                                                                   ------------------
  CH3: STAT                                                                         STAT
      2V/div.                                                                      2V/div.
    CH4: IBATT                                                                  CH4: IBATT
      1A/div.                                                                     1A/div.
                                                 4s/div.                                                                     4s/div.


                            LS Cell Balance                                                             HS Cell Balance
                            ICC = 1A, ISYS = 0A, HS cell is 3.6V and LS cell                            ICC = 1A, ISYS = 0A, HS cell is 3.8V and LS cell
                            is 3.8V, balance enabled, balance resistor is                               is 3.6V, balance enabled, balance resistor is
                            17mΩ                                                                        17mΩ




    CH1: VMID
      2V/div.

                                                                                CH1: VMID
  CH3: IBATTH                                                                     2V/div.
  500mA/div.
                                                                               CH3: IBATTH
                                                                               500mA/div.
  CH4: IBATTL                                                                  CH4: IBATTL
  500mA/div.                                                                   500mA/div.

                                               200ms/div.                                                                  200ms/div.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                                               16
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 17 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

FUNCTIONAL BLOCK DIAGRAM

                                                                                                                  CSYS

                                                                                                       SYS


                       SW                                                                                                 Q3                   BATT
                                                                        Q2


 CIN                                         Q1
                                                                                            A1
                       BST                                                                                       Charge
                                                                                                 iHS
                                                                                                                 Pump            Balance       MID
                                                                                                                                   and
                       VIN                                                                                        Pre-          Protection
                                                             A2                                                  Charge
                                                                                                                  Loop
                                                                  ILS
                                                                                                                    IBATT_FB


                                                    TJ_FB
                                                                    EA1
                                                                                                                         VIN             VCC
                                              TJ_REF         Junction Temp Loop
                VLIM                                                                                                           LDO
                                                    VBATT_FB        EA2
                                              VBATT_REG                             VCOMP
                                                                                             PWM Controller
                                                             Battery Voltage Loop
                                  Charge          IBATT_FB
                       CV        Parameter                          EA3
                                  Setting
                                              ICC_REF    Charge Current Loop
                       ISET                       VSYS_FB                                                                    NTC
                                                                                                                          Protection
                                                                    EA4                                                                        NTC
                                              VSYS_REF System Voltage Loop
                                                  VIN_FB
                                                                    EA5
                                                         1.2V
                                                               Input Voltage Loop                                                      AGND


                                   DAC                                                                                                 STAT
                                                              Thermal
                                                             Shutdown                            Control Logic
                                                                                                                                       ACOK


                 SCL
                              I2C Block and
                                                                   Timer
                                 Register
                 SDA



                                    CV


                                                                                     PGND


                                             Figure 4: Functional Block Diagram




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                                          17
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 18 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

OPERATION
The MP2672A is a highly integrated switch-                             The boost converter turns off again if VSYS is still
mode battery charger IC that charges lithium-ion                       below 110% of VIN after a 1ms soft-start time.
batteries with two cells in series from a 5V input                     It is recommended to choose VBATT_PRE and VTRACK
power supply. This means it can be used with an                        to ensure that the minimum output voltage of the
adapter or USB input.                                                  boost converter exceeds 110% of the maximum
Host-Control Mode and Standalone Mode                                  DC input voltage.
The MP2672A can operate in either host-control                         Input Power Start-Up
mode or standalone mode. After the input starts                        When the input voltage is below the under-
up, the MP2672A checks the CV pin’s status.                            voltage lockout threshold (VIN_UVLO), SYS is
If CV is pulled up to logic high, the MP2672A                          powered by the battery via Q3, which is fully
works in host-control mode. If CV is connected                         turned on at this time. When input power is
to ground through a resistor, the MP2672A                              connected and VIN exceeds VIN_UVLO, Q3 stops
works in standalone mode.                                              being fully on and enters virtual diode mode. At
                                                                       the same time, the boost converter starts up with
In host-control mode, the charging parameters                          a soft start of the system voltage loop. When the
(VBATT_REG and ICC) can be configured by the I2C                       system voltage rises to about 20mV above the
registers. In standalone mode, they can be set                         battery voltage, Q3 turns off. It turns on again
by hardware pins.                                                      with a soft-start charging current after the
Table 2: Host-Control Mode vs. Standalone Mode                         system’s voltage soft start completes.
       CV Pin           Mode         VBATT_REG          ICC            Narrow Voltage DC (NVDC) Power Structure
     Connected                          Set by        Set by           The MP2672A features a narrow voltage DC
      to AGND       Standalone           CV           ISET             (NVDC) power structure that is comprised of a
     via resistor                      resistor      resistor          frond-end boost converter and a rear-end battery
                                                                       FET between the SYS and BATT pins. This
                                        Set by        Set by
     Pulled up          Host-                                          allows for separate control between the system
                                         I2C           I2C
      to VCC           control                                         and the battery. The system is given the priority
                                       register     register (9)
                                                                       to start up, even with a deeply discharged or
Note:                                                                  missing battery. When input power is available
9)     The maximum charge current is limited by the ISET pin, even     and a depleted battery is connected, the system
       in host-control mode.
                                                                       voltage is regulated to the minimum system
Internal Power Supply                                                  voltage (VSYS_MIN) which is set via REG00H,
The VCC LDO is powered by the input power                              bits[3:1].
supply, and it powers the internal circuit and                         Figure 5 shows the system voltage control,
MOSFET driver. When the input is absent, the                           described in detail below:
VCC LDO is off. An external capacitor must be
connected from the VCC pin to AGND. The VCC                                 When the battery voltage (VBATT) is below
output is regulated to about 3.6V when VIN is 5V.                            VBATT_PRE, the system voltage is regulated to
If VIN is below 3.6V, the LDO enters low-dropout                             VSYS_REG_MIN = VBATT_PRE + VTRACK. The
mode, and the LDO FET fully turns on. The VCC                                battery FET works linearly to charge the
output cannot handle current loads exceeding                                 battery with the pre-charge current.
20mA.                                                                       When VBATT is above VBATT_PRE, the battery
Input Voltage vs. System Voltage Limitation                                  FET is fully turned on, and the system
To prevent the MP2672A from entering open-loop                               voltage always exceeds VBATT by the value
operation due to the low-side MOSFET’s minimum                               calculated with IBATT x RON_Q3. Once battery
on time, the boost converter turns off if VSYS drops                         charging completes, the system output
below 110% of VIN. The converter restarts, then                              (VSYS) is regulated to VBATT + VTRACK.
checks the input voltage and system voltage again.



MP2672A Rev. 1.0                                     www.MonolithicPower.com                                            18
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| CV Pin | Mode | V BATT_REG | I CC |
| --- | --- | --- | --- |
| Connected to AGND via resistor | Standalone | Set by CV resistor | Set by ISET resistor |
| Pulled up to VCC | Host- control | Set by I2C register | Set by I2C register (9) |


<!-- page 19 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

    When charging is disabled and REG00H,
     bit[4] = 0, VSYS is also regulated to VTRACK,
     which is greater than the real battery voltage.


                                                           vSYS

                                                 VTRACK


                                     VBATT_PRE
                                                       vBATT




                                                 Figure 5: VSYS Variation with VBATT
Battery Charge Profile                                                 VBATT_PRE. If VBATT_PRE is not reached before the
The MP2672A provides three main charging                               pre-charge timer (60min) expires, the charge
phases: constant current pre-charge, constant                          cycle ceases, and a corresponding timeout fault
current fast charge, and constant voltage charge                       signal is asserted.
(see Figure 6).                                                        Phase 2 (Constant Current Fast Charge): When
Phase 1 (Constant Current Pre-Charge): When                            VBATT exceeds VBATT_PRE, the MP2672A stops the
VBATT is below the pre-charge to fast charge                           pre-charge phase and enters the fast charge
threshold (VBATT_PRE), the MP2672A regulates                           phase. The fast charge current can be
the system voltage to VSYS_REG_MIN. The part                           configured via the ISET pin in standalone mode
applies a safe pre-charge current (IPRE) to charge                     or via the I2C register in host-control mode.
the deeply depleted battery until VBATT reaches

                                                               System Voltage                        VTRACK
        VBATT_REG
                              VTRACK                                      Battery Voltage
      VSYS_REG_MIN


                                                                                                                 ICC
                                                                                  Charge
                                                                                  Current


                                                                                                                 IPRE
                                                                                                                 ITERM

                                  Pre-Charge               Fast         Constant Voltage            Charge
                                                          Charge            Charge                Termination
                                                  Figure 6: Battery Charge Profile




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                             19
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 20 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

Phase 3 (Constant Voltage Charge): When VBATT                          Auto-Recharge
reaches the battery regulation voltage                                 When the battery is fully charged and charging is
(VBATT_REG), the charge current begins to                              terminated, the battery may be discharged by
decrease (see Figure 7). The charge cycle is                           system consumption or self-discharge (see
complete once the constant voltage loop is                             Figure 8). The MP2672A automatically starts a
dominant, and the charge current drops below                           new charging cycle (without requiring a manual
the charge termination current threshold for a                         charging cycle restart) when the battery voltage
200ms deglitch time. This 200ms deglitch time is                       drops below the recharge threshold for 200ms.
designed to start each charge cycle; after 200ms
expires, the charge-full signal asserts whether                                                   VBATT
the termination conditions have been met.                                  VRECH
                  VSYS
                                                                             Charge
      VBATT_REG                                                              Current
                                                                                                   200ms
                                   VBATT                                                                             Charging
                                                                            Charging         Recharge Deglitch
                                                                                                                      Starts
          ITERM                                                              Done                 Time

    Charge Current
                                                                                    Figure 8: Recharging Profile

                                      200ms                            Charging Enabled (Default Setting)
                Soft Start      Forced Charging Time                   If the battery is not expected to be charged
                   a) Forced Charge Time                               frequently during high state of charge (SOC)
                         VSYS                                          conditions, the MP2672A has an one-time
                                                                       programmable (OTP) option (REG05H, bit[7]) to
    VBATT_REG
                                                                       disable charging when the input power is on, and
                     Charge Current      VBATT                         the battery voltage exceeds the recharge voltage
                                                                       threshold. Charging is enabled until the battery
      ITERM
                                                                       voltage falls below the recharge threshold.
                                                                       Battery-Full Voltage Setting
                                    200ms              Charging        The MP2672A has a CV pin that can configure
        Constant Voltage Termination Deglitch Time      Done
                                                                       the battery regulation voltage.
          b) Termination Deglitch Time
 Figure 7: Forced Charge Time and Termination                          When CV is pulled up to VCC, the MP2672A
                 Deglitch Time                                         operates in host-control mode. The battery
                                                                       regulation voltage is configured through the I2C.
If ITERM is not reached before the safety charge
timer expires (see the Safety Timer section on                         When CV is connected to AGND via a resistor,
page 22), the charging cycle stops and the                             the MP2672A operates in standalone mode. The
corresponding timeout fault signal is asserted.                        battery regulation voltage is set according to
                                                                       Table 3.
Charging termination can be manually disabled
by pulling the NTC pin up to VCC. A new                                        Table 3: VBATT_REG vs. RVBATT Resistor
charging cycle starts when the following                                        Resistor Range           VBATT_REG
conditions are valid:                                                            30kΩ to 35kΩ               8.4V
      The input power is re-plugged in                                          70kΩ to 75kΩ               8.6V
                                                                                100kΩ to 105kΩ              8.7V
      Auto-recharge is enabled
                                                                                130kΩ to 135kΩ              8.8V
      The charging enable bit is toggled (only for
       host-control mode)                                              Figure 9 shows the simplified diagram.
      There is no thermistor fault on the NTC pin
      There is no safety timer fault
      There is no battery over-voltage condition
      Thermal shutdown is not occurring

MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                    20
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Resistor Range | V BATT_REG |
| --- | --- |
| 30kΩ to 35kΩ | 8.4V |
| 70kΩ to 75kΩ | 8.6V |
| 100kΩ to 105kΩ | 8.7V |
| 130kΩ to 135kΩ | 8.8V |


<!-- page 21 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

                                                                       The internal reference of the input voltage loop
                                                                       is 1.2V, and VIN_MIN can be estimated with
                                                                       Equation (2):
  CV

            VTH1                                                                                            RH +RL
                                                                                           VIN_MIN =1.2              (2)
                                                                                                             RL
                                                  Battery Voltage
            VTH2                                    Reference          Battery Supplement Mode and Virtual Diode
                              Decoding      DAC
                                                                       Mode
            VTH3                                                       When VIN_MIN is reached, the charge current is
                                                                       reduced to keep VIN from dropping further.
            VTH4
                                                                       However, if the charge current drops to 0A and
                                                                       the input source is still overloaded due to a
   Figure 9: Simplified Diagram of the VBATT_REG                       heavy system load, the system voltage (VSYS)
           Setting in Standalone Mode                                  continues dropping. If VSYS falls below VBATT, the
                                                                       MP2672A enters battery supplement mode. The
Charge Current Setting                                                 battery starts to supplement the system load
In standalone mode, the charge current (ICC) is                        along with the boost converter. In supplement
set by a resistor connected to the ISET pin                            mode, the battery FET operates as a virtual
(RISET). Calculate ICC with Equation (1):                              diode.
                             12kΩ                                      When VSYS falls 30mV below VBATT, the battery
                     ICC =         (A)                         (1)
                                                                       FET turns on, and its source-to-drain voltage is
                             RISET
                                                                       regulated at 24mV. As the battery discharge
In host-control mode, the charge current can be                        current rises, the virtual diode loop is saturated
configured via RISET and REG01H, bits[3:0]. RISET                      and the battery FET fully turns on. The source-
determines the full-scale value of the register.                       to-drain voltage is the discharge current times
For example, if RISET is 6kΩ, the I2C-configurable                     the on resistance of the battery FET.
range is between 500mA and 2000mA, with
                                                                       Missing Battery Detection
100mA per step. If RISET is 24kΩ, the I2C-
configurable range is between 125mA and                                The MP2672A is capable of detecting whether a
500mA, with 25mA per step. RISET is                                    battery is connected. The device detects a
recommended to be between 6kΩ and 24kΩ.                                missing battery under the following conditions:

Minimum Input Voltage Limit                                                Charging is enabled
                                                                           Auto-recharge is triggered
To avoid overloading the adapter, the MP2672A
implements input voltage based power                                       Recovery from any fault
management by continuously monitoring the                              If a battery cannot be found, a 1Hz blinking on
                                                                            --------------
input voltage (VIN). When the minimum input                            the STAT pin indicates the missing battery
voltage limit (VIN_MIN) is reached, the charge                         condition, or the BATTFLOAT_STAT bit is set 1
current is reduced to prevent VIN from dropping                        in host-control mode. Figure 10 shows the
further. VIN_MIN can be configured by a voltage                        battery missing detection flowchart.
divider on the VLIM pin.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                          21
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 22 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER


                               Enable Charge




                                Counter A = 0


                                Start charging
                                  Timer initiates               Has the timer expired?

                                                          No                                        Yes
                                                                             No

                              Charging terminated?
                                                                   If A < 2, A = A+1
                                                                                                    A=0
                                                                   If A = 2, A = A+0
                                       Yes



                 Yes

                                                                                       A = 2?
                             Battery FET turns off
                                                                                                                 No
                                                                                         Yes
                                                     No


                                 VBATT < VRECH?                                   Battery missing         Battery is present




                                       Figure 10: Missing Battery Detection Flowchart
Battery Over-Voltage Protection                                          writing 0 and 1 sequentially to the REG00H,
The MP2672A is designed with a built-in battery                          bit[4]. The following actions restart the safety
over-voltage protection (OVP) threshold, which                           timer:
is 104% of VBATT_REG. If a battery OV event                                      Beginning a new charge cycle
occurs, the MP2672A turns off the battery FET
(Q3) and stops charging. At this time, the boost                                 Writing REG00H, bit[4] from 0 to 1 (charge
converter continues operating, and the system                                     enabled)
voltage tracks the battery voltage with additional                               Writing REG02H, bits[2:1] from 00 to
VTRACK.                                                                           01/10/11 (safety timer enabled)
When the balance function is enabled (the MID                                    Writing REG02H bit[3] from 0 to 1 (software
pin is not pulled down to AGND), the MP2672A                                      reset)
uses the MID pin to monitor each cell’s voltage.                         In the event of an NTC hot or cold fault, the
Generally, if any one of the cell’s voltages                             charging timer is suspended. Once the NTC fault
exceeds 102.5% of VBATT_REG / 2, the MP2672A                             is removed, the timer continues to count from the
stops charging the battery.                                              value it was at before the NTC fault.
Safety Timer                                                             Watchdog Timer
The MP2672A provides both a pre-charge and                               When the MP2672A operates in host-control
fast charge cycle safety timer to avoid an                               mode, a watchdog timer is provided to reset all
extended charging cycle due to abnormal battery                          the registers to their default values if the
conditions. When the battery is below VBATT_PRE,                         watchdog timer is not reset periodically. By doing
the safety timer for pre-charge is 60 minutes.                           this, the MP2672A’s register values return to
The fast charge cycle safety timer starts when                           their default settings when no action occurs on
the battery enters fast charge mode. The fast                            the I2C bus for a certain time. The watchdog
charge safety timer can be configured or                                 timer duration can be configured and disabled
disabled via the I2C.                                                    via the I2C.
The safety timer is reset at the beginning of a
new charging cycle. It can also be reset by

MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                   22
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 23 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

Negative Temperature Coefficient (NTC)                                 different temperature window, described in detail
Thermistor                                                             below:
The term thermistor refers to any thermally                            1. When VNTC < VHOT or VNTC > VCOLD, charging
sensitive resistor, and a negative temperature                            is suspended, and all timers are suspended.
coefficient (NTC) thermistor is generally called a
thermistor. Thermistors can be used for multiple                       2. When VHOT < VNTC < VWARM, the battery
purposes, as their characteristics are different                          regulation voltage (VBATT_REG) is reduced by
based on their manufacturing method, structure,                           120mV/cell from the configurable threshold.
and shape. Unless otherwise noted, the                                 3. When VCOOL < VNTC < VCOLD, the charging
thermistor resistance values are classified at a                          current is reduced to half of the configurable
standard temperature of 25°C. The resistance of                           charge current.
a thermistor is solely a function of its absolute
                                                                                                            ICC
temperature.
Refer to the thermistor’s datasheet for the                             Charge 0.5 x ICC
mathematic equation that calculates the                                 Current
relationship between resistance and the
absolute temperature of the thermistor. It can
also be calculated with Equation (3):                                                           VBATT_REG            VBATT_REG –
                                                                                                                    120mV/cell x 2
                                                                        Charge
                                     1 1 
                                  β -                                Voltage
                   R1=R2  e         T1 T2 
                                                          (3)

Where R1 is the resistance at the absolute
temperature T1, R2 is the resistance at the
absolute temperature T2, and β is a constant that                              Cold      Cool                     Warm               Hot
depends on the thermistor’s material.                                       Figure 11: JEITA Compatible NTC Window
The MP2672A continuously monitors the                                  For a given thermistor, two of four temperature
battery’s temperature by measuring the voltage                         thresholds can be configured by changing the
on the NTC pins. This voltage is determined by                         values of RT1 and RT2. See the Selecting an NTC
the voltage divider. The voltage divider ratio is                      Sensor Resistor section on page 34 for more
determined by the NTC thermistor’s resistance                          details.
values under different ambient battery
temperatures.                                                          Thermal Regulation and Thermal Shutdown
                                                                       To guarantee safe operation, the MP2672A
The MP2672A internally sets a predetermined                            limits the die temperature. If the internal junction
upper and lower bounds of the temperature                              temperature reaches the preset threshold, the
range. If the voltage at the NTC pin goes out of                       MP2672A starts to reduce the charge current to
the hot or cold threshold, the temperature is                          prevent greater power dissipation.
outside its safe operating limit. At this time,
charging ceases until the operating temperature                        When VBATT > VBATT_PRE, the die temperature limit
returns to within its safe range.                                      is always set to 120°C. When VBATT < VBATT_PRE,
                                                                       the die temperature limit can be configured to
To satisfy JEITA requirements, the MP2672A                             multiple values (60°C, 80°C, 100°C, or 120°C),
monitors four temperature thresholds: the cold                         which can be configured by the one-time
battery threshold (TNTC < 0°C), the cool battery                       programmable (OTP) register (REG05H,
threshold (0°C < TNTC < 10°C), the warm battery                        bits[4:3]).
threshold (45°C < TNTC < 60°C), and the hot
battery threshold (TNTC > 60°C).                                       If the junction temperature reaches 150°C, the
                                                                       boost converter enters shutdown mode.
For a given NTC thermistor, these temperatures
correspond to the VCOLD, VCOOL, VWARM, and VHOT
values. Figure 11 shows the typical JEITA
operation when the battery temperature is in a

MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                               23
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 24 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

Indications                                                                        Balancing Algorithm
                                                                 ---------------
The MP2672A has two open-drain pins (ACOK                                          The balance block only operates in charge mode.
      --------------                                                               Balancing starts when any cell voltage exceeds
and STAT ) to indicate the input power and                                         the balance start point (VCELL_BAL).
charging status. Table 4 shows the behavior for
each of these indications.                                                         The voltage difference between cells should
                                                                                   exceed VCELL_DIFF. The MP2672A detects the cell
   Table 4: Input Power and Charging Statuses                                      voltages in the pack, then checks the voltage
                                 -----------------     ----------------
  Charging State                 ACOK                  STAT                        difference between two cells. If the differential
  Charging                        Low                   Low                        voltage exceeds VCELL_DIFF, the corresponding
  Charging complete,                                                               balance MOSFET turns on.
                                    Low              Open drain
  charging disabled
                                                                                   To measure the open-circuit voltage of the cell,
  Charging suspended
                                                                                   balancing is frequently suspended for a short
  due to one of the
  following:                                                                       duration.    Charging      always      operates
                                                                                   independently of the balance algorithm if no
   Battery OVP                     Low
                                                        1Hz
   Timer fault                                       blinking                     other charging fault occurs. The cell voltage is
   NTC hot fault                                                                  measured for 200µs when cell balancing is
   NTC cold fault                                                                 suspended. Then cell balancing operates for
   Battery floating                                                               249.8ms each 250ms cycle (see Figure 13).
  Thermal shutdown                  Low              Open drain
                                                                                                         On               On            On
Battery Cell Balance and Protection                                                        Balance
The MP2672A provides battery cell balance and                                             MOSFET

protection for dual-cell applications (see Figure                                                                 Off             Off

12). The part can sense the voltage across each
                                                                                                                  On              On          On
cell. Generally, if these two cells have voltages
                                                                                        Cell Voltage
that are mismatched by more than 50mV, the                                             Measurement
internal discharge path turns on to discharge the                                                        Off              Off           Off
cell with the higher voltage until the two cell                                                           200µs         249.8ms
voltages have a difference that is below 30mV.
                                                                                             Figure 13: Battery Balance Clock
If battery over-voltage protection (OVP) occurs
                                                                                   Figure 14 shows the battery balance flowchart.
before the two cells are equalized, charging is
suspended.
                                                                                                                  POR
The MP2672A integrates the balance path and
control circuit. An external power dissipation
resistor is also required to limit the balance                                                         Turn off balancing path
current. If the cell balance function is not used,                                                      and measure the cell
                                                                                                               voltage
connect MID directly to AGND.

                       BATT
                                                                                                         Any cell > VCELL_BAL?          No



                                                                                                                  Yes
                        MID                  Balance
                                               and
                                            Protection                                                    VCELL > VCELL_DIFF?           No


                       PGND
                                                                                                                  Yes


                                                                                                       Turn on the balancing
                                                                                                                path
    Figure 12: Battery Balance Block Diagram
                                                                                         Figure 14: Battery Balance Flowchart


MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                                       24
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Charging State | ----------------- ACOK | ---------------- STAT |
| --- | --- | --- |
| Charging | Low | Low |
| Charging complete, charging disabled | Low | Open drain |
| Charging suspended due to one of the following:  Battery OVP  Timer fault  NTC hot fault  NTC cold fault  Battery floating | Low | 1Hz blinking |
| Thermal shutdown | Low | Open drain |


<!-- page 25 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

For extremely unbalanced dual-cell batteries,                          Boost Converter Suspend Mode
the charger takes a few cycles to balance the                          The MP2672A offers suspend mode to turn off
battery voltages. For some applications, such as                       the boost converter even when the input is
removable dual-cell batteries, a charger is                            present. In this mode, the SYS pin is powered by
required to balance two cells in one charge cycle.                     the battery through the internal battery FET, and
In this case, an external cell-balance circuit is                      the input quiescent current is optimized.
recommended (see Figure 15).
                                                                       The MP2672A enters this mode by setting
The MP2672A also has an option to                                      REG02H, bit[0] to 0. The MP2672A-000E is
automatically disable termination if cell                              preset to this mode. The boost is suspended if
balancing is active. By doing this, the two cells                      any of the following conditions occur:
are better matched once charging is terminated.
                                                                           Charging terminated
The cell voltage measured within the 200µs time                            Charging disabled
is also delivered to the battery cell OVP block. If                        An NTC fault has occurred
OVP occurs, charging is suspended (the battery
                                                                           A timer fault has occurred
FET turns off) until the measured cell voltage
                                                                           Battery over-voltage protection (OVP) has
drops below the recovery threshold, which is set
                                                                            occurred
by REG00H, bit[0].


                                                          BATT




                         Balance                            MID
                         Control



                                                         PGND




                                        Figure 15: External Cell-Balancing Circuit
Series Interface                                                       SDA and SCL are connected to the positive
The IC uses two wires: a serial data (SDA) wire                        supply voltage via a current source or pull-up
and serial clock (SCL) wire. All I2C master and                        resistor. When the bus is free, both lines are
slave devices are connected with these two                             pulled high.
wires. The master (e.g. a microcontroller or                           The MP2672A’s SDA is a bidirectional line, and
digital signal processor) generates the bus clock                      SCL is a unidirectional line.
and initiates communication on the bus. The
slave devices receive and respond to the bus                           The data on the SDA line must be stable during
commands from the master device. To                                    the high period of the clock (see Figure 16). The
communicate with a specific device, each slave                         high or low state of the data line can only change
device must have a unique bus address.                                 when the clock signal on the SCL line is low. One
                                                                       clock pulse is generated for each data bit
The I2C interface supports both standard mode                          transferred.
(up to 100kbits), and fast mode (up to 400kbits).
The SDA and SCL pins are open drains. Both the


MP2672A Rev. 1.0                                     www.MonolithicPower.com                                          25
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 26 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER




        SDA




                                                                      Change of
        SCL                          Data line stable;                data allowed
                                     data valid

                                                  Figure 16: Bit Transfer on the I2C Bus
All transactions begin with a start (S) command                                      transition on the SDA line when the SCL is high
and can be terminated by a stop (P) command.                                         (see Figure 17). Start and stop conditions are
A start condition is defined as a high-to-low                                        always generated by the master. The bus is
transition on the SDA line while SCL is high. A                                      considered busy after a start condition, and free
stop condition is defined as a low-to-high                                           after a stop condition.


       SDA




       SCL
                   Start (S)                                                                                           Stop (P)

                                                   Figure 17: Start and Stop Conditions
Data on the I2C bus is transferred in 8-bit                                          An acknowledgement occurs after every byte.
packets (bytes) (see Figure 18). Each byte must                                      The acknowledge bit allows the receiver to signal
be followed by an acknowledge bit (ACK). Data                                        to the transmitter that the byte was successfully
is transferred with the most significant bit (MSB)                                   received and another byte may be sent. All clock
first.                                                                               pulses, including the 9th acknowledge clock
                                                                                     pulse, are generated by the master.
                                                                                                              Acknowledgement
                                                                 Acknowledgement
                                                                                                              Signal from Receiver
                                                                 Signal from Slave
 SDA
                               MSB
SCL

        Start or               1        2                7   8          9                1     2              8         9            Stop or
        Repeated                                                                                                                     Repeated
                                                                       ACK                                            ACK
        Start                                                                                                                        Start

                                                 Figure 18: Data Transfer on the I2C Bus




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                               26
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 27 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

The transmitter releases the SDA line during the                                       indicates a transmission (write) and a 1 indicates
acknowledge clock pulse so the receiver can pull                                       a request for data (read). Figure 19 shows the
the SDA line low. If it remains high during the 9th                                    complete data transfer.
clock pulse, this is called a not acknowledge
                                                                                       If the register address is not defined, the charger
(NACK) signal. The master can then generate
                                                                                       IC sends back a NACK signal and returns to the
either a stop condition to abort the transfer, or a
                                                                                       idle state.
repeated start (S) to start a new transfer.
                                                                                       The MP2672A operates as a slave device with
After the start condition is received, a slave
                                                                                       the address 4BH. The MP2672A supports
address is sent. This address is 7 bits long
                                                                                       single-byte R/W (see Figure 20 and Figure 21).
followed by an 8th data direction bit (R/W). A 0
 SDA


 SCL
         Start               1–7              8           9               1–7           8              9         1–7             8          9
                                                                                                                                                 Stop
                          Address             R/W       ACK                    Data                 ACK                Data               ACK

                                                        Figure 19: Complete Data Transfer


                     1 bit           7 bits             1 bit 1 bit           8 bits           1 bit        8 bits            1 bit 1 bit

                      S         Slave Address            0        A    Register Address         A           Data               A      P


                             From Master to Slave             From Slave to Master     A = Acknowledge (SDA Low)       S = Start     P = Stop

                                                                               2
                                                              Figure 20: I C Single Write


 1 bit           7 bits            1 bit 1 bit           8 bits          1 bit 1 bit           7 bits          1 bit 1 bit            8 bits    1 bit 1 bit

   S       Slave Address            0     A         Register Address      A        S        Slave Address       1      A              Data       /A     P


         From Master to Slave            A = Acknowledge (SDA Low)                     S = Start

         From Slave to Master            /A = not Acknowledge (SDA High)               P = Stop
                                                                               2
                                                              Figure 21: I C Single Read




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                                                27
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 28 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

I2C REGISTER MAP
IC Address 4BH
  Register Name          Address         R/W      Description                                                         Default
                                                  Battery regulation voltage, charge configuration,
       REG00H               0x00         R/W                                                                         0011 1000
                                                  and SYS voltage setting register.
                                                  Cell balance setting and charge current setting
       REG01H               0x01         R/W                                                                         1000 1111
                                                  register.
       REG02H               0x02         R/W      Timer setting register.                                            1001 0101
       REG03H               0x03          R       Status register.                                                   0000 0000
       REG04H               0x04          R       Fault register.                                                    0000 0000


REG 00H (Default: 0011 1000)
                                    Reset by          Reset
 Bit        Name          POR                                     R/W     Description                          Comment
                                    REG_RST          by WTD

  7      VBATT_REG[2]        0            Y              Y        R/W     000: 8.3V
                                                                          001: 8.4V
                                                                                                     These bits set the battery
                                                                          010: 8.5V
                                                                                                     regulation voltage. They
                                                                          011: 8.6V
  6      VBATT_REG[1]        0            Y              Y        R/W                                are set to 001 by default.
                                                                          100: 8.7V
                                                                                                     They       are      OTP-
                                                                          101: 8.8V
                                                                                                     configurable.
                                                                          110: 8.9V
  5      VBATT_REG[0]        1            Y              Y        R/W     111: 8.2V

         CHG_CON                                                          0: Charging disabled       This bit is set to 1 by
  4                          1            Y              Y        R/W
           FIG                                                            1: Charging enabled        default.

                                                                                                     These bits set the system
  3      VBATT_PRE[2]        1            Y             N         R/W     0.4V                       minimum voltage offset. It
                                                                                                     has a 6.0V offset, ranges
                                                                                                     between 6.0V and 6.7V,
                                                                                                     and is set to 6.4V by
  2      VBATT_PRE[1]        0            Y             N         R/W     0.2V                       default.
                                                                                                     This threshold is also
                                                                                                     used as the pre-charge
                                                                                                     battery voltage threshold.
  1      VBATT_PRE[0]        0            Y             N         R/W     0.1V
                                                                                                     It is OTP-configurable.

         CELL_OVP                                                                                    The bit sets the cell over-
                                                                          0: 80mV
  0          _               0            Y             N         R/W                                voltage protection (OVP)
                                                                          1: 0mV
           HYS                                                                                       hysteresis.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                     28
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Register Name | Address | R/W | Description | Default |
| --- | --- | --- | --- | --- |
| REG00H | 0x00 | R/W | Battery regulation voltage, charge configuration, and SYS voltage setting register. | 0011 1000 |
| REG01H | 0x01 | R/W | Cell balance setting and charge current setting register. | 1000 1111 |
| REG02H | 0x02 | R/W | Timer setting register. | 1001 0101 |
| REG03H | 0x03 | R | Status register. | 0000 0000 |
| REG04H | 0x04 | R | Fault register. | 0000 0000 |

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | V [2] BATT_REG | 0 | Y | Y | R/W | 000: 8.3V 001: 8.4V 010: 8.5V 011: 8.6V 100: 8.7V 101: 8.8V 110: 8.9V 111: 8.2V | These bits set the battery regulation voltage. They are set to 001 by default. They are OTP- configurable. |
| 6 | V [1] BATT_REG | 0 | Y | Y | R/W |  |  |
| 5 | V [0] BATT_REG | 1 | Y | Y | R/W |  |  |
| 4 | CHG_CON FIG | 1 | Y | Y | R/W | 0: Charging disabled 1: Charging enabled | This bit is set to 1 by default. |
| 3 | V [2] BATT_PRE | 1 | Y | N | R/W | 0.4V | These bits set the system minimum voltage offset. It has a 6.0V offset, ranges between 6.0V and 6.7V, and is set to 6.4V by default. This threshold is also used as the pre-charge battery voltage threshold. It is OTP-configurable. |
| 2 | V [1] BATT_PRE | 0 | Y | N | R/W | 0.2V |  |
| 1 | V [0] BATT_PRE | 0 | Y | N | R/W | 0.1V |  |
| 0 | CELL_OVP _ HYS | 0 | Y | N | R/W | 0: 80mV 1: 0mV | The bit sets the cell over- voltage protection (OVP) hysteresis. |


<!-- page 29 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

REG 01H (Default: 1000 1111)
                                       Reset by         Reset
 Bit          Name            POR                                   R/W      Description             Comment
                                       REG_RST         by WTD
                                                                                                     This bit is set to 0 by
                                                                             0: Standard
  7       NTC_TYPE              1           Y              Y        R/W                              default.   It  is  OTP-
                                                                             1: JEITA
                                                                                                     configurable.
                                                                                                     This bit sets the cell-
                                                                             0: 3.5V                 balance start point. It is set
  6         VCELL_BAL           0           Y              Y        R/W
                                                                             1: 3.7V                 to 0 by default, and is OTP-
                                                                                                     configurable.
                                                                                                     This bit sets the cell-
         BALANCE_
                                                                             0: 50mV                 balance threshold. It is set
  5     THRESHOLD_              0           Y              Y        R/W
                                                                             1: 70mV                 to 0 by default, and is OTP-
            H2L
                                                                                                     configurable.
                                                                                                     This bit sets the cell-
         BALANCE_
                                                                             0: 50mV                 balance threshold. It is set
  4     THRESHOLD_              0           Y              Y        R/W
                                                                             1: 70mV                 to 0 by default, and is OTP-
            L2H
                                                                                                     configurable.

                                                                                                     These bits set the fast
  3           ICC[2]            1           Y              Y        R/W      800mA                   charge current setting.
                                                                                                     If RISET is 6kΩ:
                                                                                                     These bits have a 500mA
                                                                                                     offset, a 500mA to
  2           ICC[2]            1           Y              Y        R/W      400mA                   2000mA range, and are
                                                                                                     set to 1111 by default.
                                                                                                     If RISET is 24kΩ:
  1           ICC[1]            1           Y              Y        R/W      200mA                   These bits have a 125mA
                                                                                                     offset, a 125mA to 500mA
                                                                                                     range, are set to 1111 by
                                                                                                     default, and are OTP-
  0           ICC[0]            1           Y              Y        R/W      100mA                   configurable.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                     29
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | NTC_TYPE | 1 | Y | Y | R/W | 0: Standard 1: JEITA | This bit is set to 0 by default. It is OTP- configurable. |
| 6 | V CELL_BAL | 0 | Y | Y | R/W | 0: 3.5V 1: 3.7V | This bit sets the cell- balance start point. It is set to 0 by default, and is OTP- configurable. |
| 5 | BALANCE_ THRESHOLD_ H2L | 0 | Y | Y | R/W | 0: 50mV 1: 70mV | This bit sets the cell- balance threshold. It is set to 0 by default, and is OTP- configurable. |
| 4 | BALANCE_ THRESHOLD_ L2H | 0 | Y | Y | R/W | 0: 50mV 1: 70mV | This bit sets the cell- balance threshold. It is set to 0 by default, and is OTP- configurable. |
| 3 | I [2] CC | 1 | Y | Y | R/W | 800mA | These bits set the fast charge current setting. If R is 6kΩ: ISET These bits have a 500mA offset, a 500mA to 2000mA range, and are set to 1111 by default. If R is 24kΩ: ISET These bits have a 125mA offset, a 125mA to 500mA range, are set to 1111 by default, and are OTP- configurable. |
| 2 | I [2] CC | 1 | Y | Y | R/W | 400mA |  |
| 1 | I [1] CC | 1 | Y | Y | R/W | 200mA |  |
| 0 | I [0] CC | 1 | Y | Y | R/W | 100mA |  |


<!-- page 30 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

REG 02H (Default: 1001 0101)
                                    Reset by         Reset
 Bit        Name           POR                                   R/W     Description                          Comment
                                    REG_RST         by WTD
                                                                                                     This bit is set to 1 by
                                                                         0: 600kHz
  7           fSW            1            Y             Y        R/W                                 default.   It  is  OTP-
                                                                         1: 1200kHz
                                                                                                     configurable.
          I2C_WD_
           TIMER_                                                        0: Normal                   This bit is set to 0 by
  6                          0            Y             N        R/W
                                                                         1: Reset                    default.
           RESET
         WD_TIMER                                                        00: Disable timer           These bits set the I2C
  5                          0            Y             N        R/W
            [1]                                                          01: 40s                     watchdog timer limit. They
         WD_TIMER                                                        10: 80s                     are set to 01 by default,
  4                          1            Y             N        R/W     11: 160s                    and are OTP-configurable.
            [0]
                                                                                                     This bit is set to 0 by
                                                                         0: Keep current
        REGISTER_                                                                                    default. After a reset, this
  3                          0            Y             N        R/W     setting
          RESET                                                                                      bit    returns     to      0
                                                                         1: Reset
                                                                                                     automatically.
                                                                         00: Disable charge
  2     CHG_TMR[1]           1            Y             Y        R/W     timer
                                                                                                     These bits are set to 10 by
                                                                         01: 8 hours
                                                                                                     default.
                                                                         10: 20 hours
  1     CHG_TMR[0]           0            Y             Y        R/W
                                                                         11: 12 hours
                                                                         0: Enable
                                                                         suspended mode
                                                                         (disable the boost)         This bit is set to 1 by
  0       EN_SUSP            1            Y             Y        R/W
                                                                         1: Disable                  default.
                                                                         suspended mode
                                                                         (enable the boost)




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                   30
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | f SW | 1 | Y | Y | R/W | 0: 600kHz 1: 1200kHz | This bit is set to 1 by default. It is OTP- configurable. |
| 6 | I2C_WD_ TIMER_ RESET | 0 | Y | N | R/W | 0: Normal 1: Reset | This bit is set to 0 by default. |
| 5 | WD_TIMER [1] | 0 | Y | N | R/W | 00: Disable timer 01: 40s 10: 80s 11: 160s | These bits set the I2C watchdog timer limit. They are set to 01 by default, and are OTP-configurable. |
| 4 | WD_TIMER [0] | 1 | Y | N | R/W |  |  |
| 3 | REGISTER_ RESET | 0 | Y | N | R/W | 0: Keep current setting 1: Reset | This bit is set to 0 by default. After a reset, this bit returns to 0 automatically. |
| 2 | CHG_TMR[1] | 1 | Y | Y | R/W | 00: Disable charge timer 01: 8 hours 10: 20 hours 11: 12 hours | These bits are set to 10 by default. |
| 1 | CHG_TMR[0] | 0 | Y | Y | R/W |  |  |
| 0 | EN_SUSP | 1 | Y | Y | R/W | 0: Enable suspended mode (disable the boost) 1: Disable suspended mode (enable the boost) | This bit is set to 1 by default. |


<!-- page 31 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

REG 03H (Default: 0000 0000)
                                        Reset by         Reset
 Bit         Name            POR                                     R/W      Description                Comment
                                        REG_RST         by WTD
  7      RESERVED             N/A           N/A            N/A         R      Reserved.                  Reserved.
  6      RESERVED             N/A           N/A            N/A         R      Reserved.                  Reserved.
                                                                              00: Not charging
  5     CHG_STAT[1]            0            N/A            N/A         R      01: Pre-charge
                                                                              10: Constant current
                                                                                                         These bits are set to 00
                                                                              or constant voltage
                                                                                                         by default.
                                                                              charge
  4     CHG_STAT[0]            0            N/A            N/A         R      11: Charging
                                                                              complete
                                                                              0: Not in PPM              This bit is set to 0 by
  3       PPM_STAT             0            N/A            N/A         R
                                                                              1: in VIN PPM              default.
        BATTFLOAT_                                                            0: Battery present         This bit is set to 0 by
  2                            0            N/A            N/A         R
           STAT                                                               1: Battery missing         default.
                                                                              0: Normal
           THERM_                                                                                        This bit is set to 0 by
  1                            0            N/A            N/A         R      1: Thermal
            STAT                                                                                         default.
                                                                              regulation
                                                                              0: Not in VSYSMIN
                                                                              regulation                 This bit is set to 0 by
  0      VSYS_STAT             0            N/A            N/A         R
                                                                              1: In VSYSMIN              default.
                                                                              regulation




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                   31
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | RESERVED | N/A | N/A | N/A | R | Reserved. | Reserved. |
| 6 | RESERVED | N/A | N/A | N/A | R | Reserved. | Reserved. |
| 5 | CHG_STAT[1] | 0 | N/A | N/A | R | 00: Not charging 01: Pre-charge 10: Constant current or constant voltage charge 11: Charging complete | These bits are set to 00 by default. |
| 4 | CHG_STAT[0] | 0 | N/A | N/A | R |  |  |
| 3 | PPM_STAT | 0 | N/A | N/A | R | 0: Not in PPM 1: in VIN PPM | This bit is set to 0 by default. |
| 2 | BATTFLOAT_ STAT | 0 | N/A | N/A | R | 0: Battery present 1: Battery missing | This bit is set to 0 by default. |
| 1 | THERM_ STAT | 0 | N/A | N/A | R | 0: Normal 1: Thermal regulation | This bit is set to 0 by default. |
| 0 | VSYS_STAT | 0 | N/A | N/A | R | 0: Not in V SYSMIN regulation 1: In V SYSMIN regulation | This bit is set to 0 by default. |


<!-- page 32 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

REG 04H (Default: 0000 0000)
                                        Reset by         Reset
 Bit          Name            POR                                    R/W      Description                Comment
                                        REG_RST         by WTD
                                                                              0: Normal operation
                                                                                                         This bit is set to 0 by
  7       WD_FAULT              0           N/A            N/A         R      1: The watchdog
                                                                                                         default.
                                                                              timer has expired
                                                                              0: Normal operation
                                                                                                         This bit is set to 0 by
  6     INPUT_FAULT             0           N/A            N/A         R      1: Input OVP has
                                                                                                         default.
                                                                              occurred
                                                                              0: Normal operation
          THERMSD_                                                                                       This bit is set to 0 by
  5                             0           N/A            N/A         R      1: Thermal
            FAULT                                                                                        default.
                                                                              shutdown
                                                                              0: Normal operation
                                                                                                         This bit is set to 0 by
  4     TIMER_FAULT             0           N/A            N/A         R      1: The safety timer
                                                                                                         default.
                                                                              has expired
                                                                              0: Normal operation
                                                                                                         This bit is set to 0 by
  3       BAT_FAULT             0           N/A            N/A         R      1: Battery OVP has
                                                                                                         default.
                                                                              occurred
                                                                              000: Normal
  2     NTC_FAULT[2]            0           N/A            N/A         R      operation
                                                                              001: An NTC cold
                                                                              fault has occurred
                                                                              010: An NTC cool           These bits are set to
  1     NTC_FAULT[1]            0           N/A            N/A         R      fault has occurred         000 by default.
                                                                              011: An NTC warm
                                                                              fault has occurred
  0     NTC_FAULT[0]            0           N/A            N/A         R      100: An NTC hot
                                                                              fault has occurred




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                  32
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | WD_FAULT | 0 | N/A | N/A | R | 0: Normal operation 1: The watchdog timer has expired | This bit is set to 0 by default. |
| 6 | INPUT_FAULT | 0 | N/A | N/A | R | 0: Normal operation 1: Input OVP has occurred | This bit is set to 0 by default. |
| 5 | THERMSD_ FAULT | 0 | N/A | N/A | R | 0: Normal operation 1: Thermal shutdown | This bit is set to 0 by default. |
| 4 | TIMER_FAULT | 0 | N/A | N/A | R | 0: Normal operation 1: The safety timer has expired | This bit is set to 0 by default. |
| 3 | BAT_FAULT | 0 | N/A | N/A | R | 0: Normal operation 1: Battery OVP has occurred | This bit is set to 0 by default. |
| 2 | NTC_FAULT[2] | 0 | N/A | N/A | R | 000: Normal operation 001: An NTC cold fault has occurred 010: An NTC cool fault has occurred 011: An NTC warm fault has occurred 100: An NTC hot fault has occurred | These bits are set to 000 by default. |
| 1 | NTC_FAULT[1] | 0 | N/A | N/A | R |  |  |
| 0 | NTC_FAULT[0] | 0 | N/A | N/A | R |  |  |


<!-- page 33 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

REG 05H (Default: 1110 0000) (10)
                                     Reset by        Reset
 Bit        Name           POR                                   R/W      Description                Comment
                                     REG_RST        by WTD
                                                                          0: No charging after
                                                                          input start-up when
                                                                          VBATT > VRECH
                                                                                                     This bit is set to 1 by
  7        RCHG              1           N/A           N/A        N/A     1: Automatic
                                                                                                     default.
                                                                          charging after input
                                                                          start-up when VBATT
                                                                          > VRECH
  6     RESERVED             1           N/A           N/A        N/A     Reserved.                  Reserved.
                                                                          0: Do not suspend
                                                                          termination when
                                                                          cell balancing is
        BALANCE_                                                          active                     This bit is set to 1 by
  5                          1           N/A           N/A        N/A
         EOC_EN                                                           1: Suspend                 default.
                                                                          termination when
                                                                          cell balancing is
                                                                          active
                                                                          00: 120°C
  4       TJ_REG[1]          0           N/A           N/A        N/A
                                                                          01: 100°C                  This bit is set to 00 by
                                                                          10: 80°C                   default.
  3       TJ_REG[0]          0           N/A           N/A        N/A     11: 60°C
  2     RESERVED           N/A           N/A           N/A        N/A     Reserved.                  Reserved.
  1     RESERVED           N/A           N/A           N/A        N/A     Reserved.                  Reserved.
  0     RESERVED           N/A           N/A           N/A        N/A     Reserved.                  Reserved.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                               33
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | RCHG | 1 | N/A | N/A | N/A | 0: No charging after input start-up when V > V BATT RECH 1: Automatic charging after input start-up when V BATT > V RECH | This bit is set to 1 by default. |
| 6 | RESERVED | 1 | N/A | N/A | N/A | Reserved. | Reserved. |
| 5 | BALANCE_ EOC_EN | 1 | N/A | N/A | N/A | 0: Do not suspend termination when cell balancing is active 1: Suspend termination when cell balancing is active | This bit is set to 1 by default. |
| 4 | T [1] J_REG | 0 | N/A | N/A | N/A | 00: 120°C 01: 100°C 10: 80°C 11: 60°C | This bit is set to 00 by default. |
| 3 | T [0] J_REG | 0 | N/A | N/A | N/A |  |  |
| 2 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 1 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 0 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |


<!-- page 34 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

REG 06H (Default: 0000 0011) (10)
                                             Reset by       Reset
 Bit            Name              POR                                R/W      Description                Comment
                                             REG_RST       by WTD
  7        RESERVED                N/A            N/A       N/A       N/A     Reserved.                  Reserved.
  6        RESERVED                N/A            N/A       N/A       N/A     Reserved.                  Reserved.
  5        RESERVED                N/A            N/A       N/A       N/A     Reserved.                  Reserved.
  4        RESERVED                N/A            N/A       N/A       N/A     Reserved.                  Reserved.
  3        RESERVED                N/A            N/A       N/A       N/A     Reserved.                  Reserved.
  2        RESERVED                N/A            N/A       N/A       N/A     Reserved.                  Reserved.
  1        RESERVED                  1            N/A       N/A       N/A     Reserved.                  Reserved.
                                                                              When charging is
                                                                              suspended:
         NVDC_MODE_                                                           0: Disable DC/DC           This bit is set to 1 by
  0                                  1            N/A       N/A       N/A
             EN                                                               switching                  default.
                                                                              1: Enable DC/DC
                                                                              switching
Note:
10) This register is for OTP only. It is not accessible.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                  34
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Bit | Name | POR | Reset by REG_RST | Reset by WTD | R/W | Description | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 6 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 5 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 4 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 3 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 2 | RESERVED | N/A | N/A | N/A | N/A | Reserved. | Reserved. |
| 1 | RESERVED | 1 | N/A | N/A | N/A | Reserved. | Reserved. |
| 0 | NVDC_MODE_ EN | 1 | N/A | N/A | N/A | When charging is suspended: 0: Disable DC/DC switching 1: Enable DC/DC switching | This bit is set to 1 by default. |


<!-- page 35 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

OTP MAP
        #          Bit[7]           Bit[6]            Bit[5]           Bit[4]         Bit[3]        Bit[2]        Bit[1]    Bit[0]

    00H                     VBATT_REG: 8.2V-8.9V                        N/A                  VBATT_PRE: 6.0V to 6.7V         N/A

    01H         NTC Type          VCELL_BAL       VCELL_DIFF_HL     VCELL_DIFF_LH     ICC: 500mA to 2000mA/100mA step (RISET = 6kΩ)

    02H            FSW               N/A                   WATCHDOG                    N/A           N/A           N/A       N/A

                                                   BALANCE_           TJ_REG: 60°C, 80°C,
  05H (10)        RCHG               N/A                                                             N/A           N/A       N/A
                                                    EOC_EN             100°C , or 120°C
                                                                                                                            NVDC
  06H (10)          N/A              N/A               N/A                      N/A                  N/A           N/A
                                                                                                                           Mode_EN

Note:
10) This register is for OTP only. It is not accessible.

OTP DEFAULT
                       OTP Items                                                        Default
                        VBATT_REG                                                         8.4V
                        VBATT_PRE                                                         6.4V
                        NTC Type                                                         JEITA
                         VCELL_BAL                                                        3.5V
                  Balance Threshold H2L                                                  50mV
                  Balance Threshold L2H                                                  50mV
                           ICC                                                          2000mA
                        SW FREQ                                                        1200kHz
                      WATCHDOG                                                            40s
                          RCHG                                 New charge cycle starts after start-up when VBATT > VRECH
                                                                Enabled (if the two cells are not balanced, EOC is not
                    BALANCE_EOC_EN
                                                                       asserted, even all conditions are met)
              Thermal Regulation Threshold                                               120°C
                   NVDC Mode_EN                                 Enable DC/DC switching when charging is suspended




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                         35
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| # | Bit[7] | Bit[6] | Bit[5] | Bit[4] | Bit[3] | Bit[2] | Bit[1] | Bit[0] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00H | VBATT_REG: 8.2V-8.9V |  |  | N/A | VBATT_PRE: 6.0V to 6.7V |  |  | N/A |
| 01H | NTC Type | VCELL_BAL | VCELL_DIFF_HL | VCELL_DIFF_LH | ICC: 500mA to 2000mA/100mA step (RISET = 6kΩ) |  |  |  |
| 02H | FSW | N/A | WATCHDOG |  | N/A | N/A | N/A | N/A |
| 05H (10) | RCHG | N/A | BALANCE_ EOC_EN | TJ_REG: 60°C, 80°C, 100°C , or 120°C |  | N/A | N/A | N/A |
| 06H (10) | N/A | N/A | N/A | N/A |  | N/A | N/A | NVDC Mode_EN |

| OTP Items | Default |
| --- | --- |
| V BATT_REG | 8.4V |
| V BATT_PRE | 6.4V |
| NTC Type | JEITA |
| V CELL_BAL | 3.5V |
| Balance Threshold H2L | 50mV |
| Balance Threshold L2H | 50mV |
| I CC | 2000mA |
| SW FREQ | 1200kHz |
| WATCHDOG | 40s |
| RCHG | New charge cycle starts after start-up when V > V BATT RECH |
| BALANCE_EOC_EN | Enabled (if the two cells are not balanced, EOC is not asserted, even all conditions are met) |
| Thermal Regulation Threshold | 120°C |
| NVDC Mode_EN | Enable DC/DC switching when charging is suspended |


<!-- page 36 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

APPLICATION INFORMATION                                                                        VCOLD  RT1
                                                                                       RT2 =                RL                     (8)
Setting the Charge Current in Standalone                                                        1-VCOLD
Mode
                                                                       Where VHOT is the high temperature threshold,
In standalone mode, the MP2672A’s charge                               VCOLD is the low temperature threshold, RH is the
current (ICC) can be set by an external resistor                       value of the NTC resistor at high temperatures
(RISET). Estimate ICC with Equation (4):                               within the required temperature operation range,
                              12kΩ                                     and RL is the value of the NTC resistor at low
                      ICC =         (A)                   (4)          temperatures.
                              RISET
The charge current can be configured up to 2.0A.                                                               VCC
Table 5 shows the expected RISET value for
typical charge currents.
       Table 5: Charge Current Setting Table
                                                                                                                             RT1
               RISET (kΩ)            ICC (A)                                                     VCOLD

                   24                   0.5
                                                                                                 VCOOL            NTC
                   12                   1.0                                     NTC
                                                                             Protection
                   6                    2.0
                                                                                                                            RT2
Setting the Minimum Input Voltage Limit                                                          VWARM
In charge mode, connect a voltage divider from
IN to AGND, then tap it to VLIM to configure the                                                                             RNTC
                                                                                                 VHOT
minimum input voltage. Calculate the minimum
input voltage with Equation (5):                                                                              AGND


                                   RH +RL
               VIN_MIN =1.2V                             (5)
                                    RL                                            Figure 22: NTC Protection Block
Where 1.2V is the reference of the minimum                             RT1 and RT2 allow the high temperature limit and
input voltage loop. With a given RL, RH can be                         low temperature limit to be configured
estimated with Equation (6):                                           independently. With this feature, the MP2672A
                                                                       can use most types of NTC resistors with
                            VIN_MIN -1.2V                              different   temperature      operation    range
               RH =RL                                    (6)
                                 1.2V                                  requirements.
For example, if a 4.675V minimum input voltage                         The RT1 and RT2 values depend on the type of
limit is expected, RL = 10kΩ and RH = 28.7kΩ.                          the NTC resistor. For example, the 103AT
                                                                       thermistor    has  the  following electrical
Selecting an NTC Sensor Resistor                                       characteristics:
Figure 22 shows an internal voltage divider
reference circuit that limits the high and low                             At 0°C, RNTC_COLD = 27.28kΩ
temperature thresholds for VHOT and VCOLD,                                 At 60°C, RNTC_HOT = 3.02kΩ
respectively.                                                          Based on Equations (7) and Equation (8), as well
For a given NTC thermistor, select the                                 as the VHOT and VCOLD values from the electrical
appropriate RT1 and RT2 values to set the NTC                          characteristics mentioned above, RT1 = 12.62kΩ,
window. Calculate RT1 and RT2 using Equation (7)                       and RT2 = 3.63kΩ.
and Equation (8), respectively:                                        Apply the spreadsheet                for      RT1   and      RT2
              (1-VCOLD )(1-VHOT )(RL -RH )                             calculation if required.
    RT1=                                                  (7)
           (1-VHOT )  VCOLD -(1-VCOLD )  VHOT


MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                        36
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| R (kΩ) ISET | I (A) CC |
| --- | --- |
| 24 | 0.5 |
| 12 | 1.0 |
| 6 | 2.0 |


<!-- page 37 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

Selecting the Inductor                                                 With an 8.4V battery voltage, 2A maximum
Inductor selection is a tradeoff between cost,                         charge current, 8.7V system voltage, typical
size, and efficiency. A lower-value inductor                           input voltage (VIN = 5V), 1.2MHz switching
results in lower DCR for components of a similar                       frequency, 90% efficiency, and expected 4.5A
size, but results in higher current ripple,                            inductor peak current, the inductance is
magnetic hysteretic losses, and output                                 calculated to be about 1.5μH.
capacitances. The inductor ripple current should                       A 1.5µH inductor with >5A saturation current is
not exceed 30% of the maximum input current                            recommended for applications with a 1.2MHz
under the worst-case conditions.                                       switching frequency. A 2.5µH inductor with >5A
Choose an inductor that does not saturate under                        saturation current is recommended for
the worst-case load conditions. The inductor’s                         applications with a 600kHz switching frequency.
saturation current should be greater than the                          Selecting the Input Capacitor
peak current limit of the low-side MOSFET.
                                                                       CIN is the boost converter’s input capacitor in
When the MP2672A works in charge mode,                                 charge mode. Calculate CIN with Equation (12):
estimate the required inductance with Equation
                                                                                                 1-VIN / VSYS
(9):                                                                               CIN                                (12)
                                                                                           8  fSW 2  L  ΔVIN /VIN
                      VIN  (VSYS -VIN )
               L=                                         (9)          Where ∆VIN / VIN can be estimated with Equation
                    VSYS  fSW  ΔIL_MAX                               (13):
Where VSYS is the system’s minimum regulation                                         ΔVIN      1-VIN / VSYS
voltage, fSW is the switching frequency, and                                                                          (13)
∆IL_MAX is the peak-to-peak inductor ripple                                           VIN    8  CIN  fSW 2  L
current, calculated with Equation (10):                                Assume the maximum input voltage ripple is 1%.
             ΔIL_MAX =2  IL_PK -IIN(MAX)             (10)
                                                                       When VSYS is 9.2V, VIN is 5V, L is 1µH, and fSW is
                                                                       1200kHz, then CIN is calculated to be 4.7µF.
Where IL_PK is the expected inductor peak                              Place one >4.7µF ceramic capacitor with X5R or
current, and IIN(MAX) is maximum input current,                        X7R dielectrics at the IN terminal.
estimated with Equation (11):
                                                                       Selecting the System Capacitor
                            VSYS  ISYS(MAX)                           In charge mode, CSYS is the output capacitor of
               IIN(MAX) =                               (11)
                                VIN                                  the boost converter. CSYS keeps the VSYS ripple
                                                                       small (<0.5%) and ensures feedback loop
Where ISYS(MAX) is the maximum boost output                            stability. Select the system capacitor based on
current, and Ƞ is the boost efficiency.                                the ripple current. For the best results, X5R or
                                                                       X7R dielectric ceramic capacitors are
                                                                       recommended for their low ESR and small
                                                                       temperature coefficients. For most applications,
                                                                       two 22µF capacitors and one 1µF capacitor are
                                                                       sufficient. Place these capacitors as close as
                                                                       possible to the IC.




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                            37
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 38 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

PCB Layout Guidelines
Efficient PCB layout is critical for meeting
specified noise, efficiency, and stability
requirements. For the best results, refer to
Figure 23 and follow the guidelines below:
1. Place the output capacitor as close to SYS
   and PGND as possible.
2. Place the local power input capacitors as
   close as possible to the IN and PGND pins.
3. Minimize the length of the high-side
   switching node (SW, inductor) trace that                                                     Top Layer
   carries the high current.
4. Keep the switching node short, and route it
   away from all control signals, especially the
   feedback network.
5. Route the power stages adjacent to their
   grounds.




                                                                                          Bottom Layer
                                                                              Figure 23: Recommended PCB Layout




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                         38
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 39 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL APPLICATION CIRCUITS
                                                                                                    DC/DC               MCU
                                                                CVCC      CSYS
                                                                1μF       2 x 22μF


                                                                                                 Other Rails
                                    100nF        BST VCC               SYS
                        Optional                                Q2       Q3 BATT
                                    L1                                               22μF
                                                 SW                                                                   Amplifier
                                   1.5μH                                               CBATT
     CIN
     10μF                                                  Q1

                                                                                                          Motor
                                                 ACOK                       MID
                                                                                                          Driver
                                                 VIN      MP2672A
                                                 VLIM

                                                 SDA                      STAT
                                                                                                 VCC
                                                 SCL                                     RT1
                                                                        NTC
                                                CV ISET         PGND AGND
                                                                                         RT2

                                                        RISET
                                                                                         RNTC


                 Figure 24: MP2672A-0000 Application Reference Circuit for NVDC Applications

                                               Table 6: Key BOM from Figure 24
  Qty         Ref           Value          Description                                           Package           Manufacturer
   1          CIN           10µF           Ceramic capacitor, 16V, X5R or X7R                     0805                Any
   2         CSYS           22µF           Ceramic capacitor, 16V, X5R or X7R                     0805                Any
   1         CBATT          22µF           Ceramic capacitor, 16V, X5R or X7R                     1206                Any
   1         CVCC            1µF           Ceramic capacitor, 10V, X5R or X7R                     0603                Any
   1         CBST           100nF          Ceramic capacitor, 25V, X5R or X7R                     0603                Any
                                           Inductor, 1.5µH, saturation current >8A, low
    1         L1            1.5µH                                                                  SMD                 Any
                                           DCR




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                      39
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Qty | Ref | Value | Description | Package | Manufacturer |
| --- | --- | --- | --- | --- | --- |
| 1 | C IN | 10µF | Ceramic capacitor, 16V, X5R or X7R | 0805 | Any |
| 2 | C SYS | 22µF | Ceramic capacitor, 16V, X5R or X7R | 0805 | Any |
| 1 | C BATT | 22µF | Ceramic capacitor, 16V, X5R or X7R | 1206 | Any |
| 1 | C VCC | 1µF | Ceramic capacitor, 10V, X5R or X7R | 0603 | Any |
| 1 | C BST | 100nF | Ceramic capacitor, 25V, X5R or X7R | 0603 | Any |
| 1 | L1 | 1.5µH | Inductor, 1.5µH, saturation current >8A, low DCR | SMD | Any |


<!-- page 40 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

TYPICAL APPLICATION CIRCUITS (continued)

                                                                              CVCC          CSYS
                                                                              1μF           4.7μF



                                                     100nF     BST     VCC           SYS
                                                      CBST
                                      Optional                            Q2           Q3
                                                    L1                                      BATT     22μF
                                                               SW
                                                   1.5μH
                      CIN                                                                              CBATT
                     10μF                                                Q1


                                                               ACOK                         MID
                                                               VIN      MP2672A
                                                               VLIM

                                                               SDA                          STAT
                                                                                                               VCC
                                                               SCL                                       RT1
                                                                                       NTC
                                                               CV ISET        PGND AGND
                                                                                                        RT2

                                                                      RISET
                                                                                                        NTC


             Figure 25: MP2672A-000E Application Reference Circuit for Charge Only Applications

                                                 Table 7: Key BOM from Figure 25
  Qty         Ref           Value        Description                                                Package      Manufacturer
   1          CIN           10µF         Ceramic capacitor, 16V, X5R or X7R                          0805           Any
   1         CSYS           4.7µF        Ceramic capacitor, 16V, X5R or X7R                          0805           Any
   1         CBATT          22µF         Ceramic capacitor, 16V, X5R or X7R                          1206           Any
   1         CVCC            1µF         Ceramic capacitor, 10V, X5R or X7R                          0603           Any
   1         CBST           100nF        Ceramic capacitor, 25V, X5R or X7R                          0603           Any
                                         Inductor; 1.5µH, saturation current >8A, low
    1         L1            1.5µH                                                                    SMD             Any
                                         DCR




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                    40
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Qty | Ref | Value | Description | Package | Manufacturer |
| --- | --- | --- | --- | --- | --- |
| 1 | C IN | 10µF | Ceramic capacitor, 16V, X5R or X7R | 0805 | Any |
| 1 | C SYS | 4.7µF | Ceramic capacitor, 16V, X5R or X7R | 0805 | Any |
| 1 | C BATT | 22µF | Ceramic capacitor, 16V, X5R or X7R | 1206 | Any |
| 1 | C VCC | 1µF | Ceramic capacitor, 10V, X5R or X7R | 0603 | Any |
| 1 | C BST | 100nF | Ceramic capacitor, 25V, X5R or X7R | 0603 | Any |
| 1 | L1 | 1.5µH | Inductor; 1.5µH, saturation current >8A, low DCR | SMD | Any |


<!-- page 41 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

PACKAGE INFORMATION
                                                    QFN-18 (2mmx3mm)



          PIN 1 ID
          MARKING                                                                                              PIN 1 ID
                                                                                                               0.15X0.10 TYP


    PIN 1 ID
    INDEX AREA




                               TOP VIEW                                              BOTTOM VIEW




                              SIDE VIEW




                                                                          NOTE:
        0.15X0.10
                                                                          1) ALL DIMENSIONS ARE IN
                                                                          MILLIMETERS.
                                                                          2) EXPOSED PADDLE SIZE DOES NOT
                                                                          INCLUDE MOLD FLASH.
                                                                          3) LEAD COPLANARITY SHALL BE 0.10
                                                                          MILLIMETERS MAX.
                                                                          4) JEDEC REFERENCE IS MO-220.
                                                                          5) DRAWING IS NOT TO SCALE.


               RECOMMENDED LAND PATTERN




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                   41
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

<!-- page 42 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

CARRIER INFORMATION



                                            Pin1              1                 1               1                 1
                                                                     ABCD            ABCD                ABCD         ABCD




                                                                                        Feed Direction



                                                                                                            Carrier     Carrier
                           Package           Quantity/     Quantity/        Quantity/      Reel
    Part Number                                                                                              Tape        Tape
                          Description          Reel         Tube              Tray       Diameter
                                                                                                            Width        Pitch
    MP2672AGD-              QFN-18
                                               5000            N/A            N/A           13in            12mm         8mm
      xxxx–Z              (2mmx3mm)




MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                      42
12/1/2020        MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Part Number | Package Description | Quantity/ Reel | Quantity/ Tube | Quantity/ Tray | Reel Diameter | Carrier Tape Width | Carrier Tape Pitch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP2672AGD- xxxx–Z | QFN-18 (2mmx3mm) | 5000 | N/A | N/A | 13in | 12mm | 8mm |


<!-- page 43 -->

MP2672A – 2-CELL LI-ION OR LI-POLYMER BOOST SWITCHING CHARGER

Revision History
                      Revision                                                                                        Pages
  Revision #                            Description
                        Date                                                                                         Updated
        1.0          11/10/2020         Initial Release                                                                 -




Notice: The information in this document is subject to change without notice. Users should warrant and guarantee that third-
party Intellectual Property rights are not infringed upon when integrating MPS products into any application. MPS will not assume
any legal responsibility for any said applications.

MP2672A Rev. 1.0                                     www.MonolithicPower.com                                                   43
11/10/2020       MPS Proprietary Information. Patent Protected. Unauthorized Photocopy and Duplication Prohibited.
                                                © 2020 MPS. All Rights Reserved.

**Extracted table(s) on this page:**

| Revision # | Revision Date | Description | Pages Updated |
| --- | --- | --- | --- |
| 1.0 | 11/10/2020 | Initial Release | - |
