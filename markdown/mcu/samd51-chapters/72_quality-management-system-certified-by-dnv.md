# Quality Management System Certified by DNV

*Source: `Atmel-SAMD51.pdf`, pages 2127-2128 — SAMD51 family datasheet*

                                                   SAM D5x/E5x Family Data Sheet

application meets with your specifications. MICROCHIP MAKES NO REPRESENTATIONS OR
WARRANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED, WRITTEN OR ORAL, STATUTORY
OR OTHERWISE, RELATED TO THE INFORMATION, INCLUDING BUT NOT LIMITED TO ITS
CONDITION, QUALITY, PERFORMANCE, MERCHANTABILITY OR FITNESS FOR PURPOSE.
Microchip disclaims all liability arising from this information and its use. Use of Microchip devices in life
support and/or safety applications is entirely at the buyer’s risk, and the buyer agrees to defend,
indemnify and hold harmless Microchip from any and all damages, claims, suits, or expenses resulting
from such use. No licenses are conveyed, implicitly or otherwise, under any Microchip intellectual
property rights unless otherwise stated.


Trademarks
The Microchip name and logo, the Microchip logo, AnyRate, AVR, AVR logo, AVR Freaks, BitCloud,
chipKIT, chipKIT logo, CryptoMemory, CryptoRF, dsPIC, FlashFlex, flexPWR, Heldo, JukeBlox, KeeLoq,
Kleer, LANCheck, LINK MD, maXStylus, maXTouch, MediaLB, megaAVR, MOST, MOST logo, MPLAB,
OptoLyzer, PIC, picoPower, PICSTART, PIC32 logo, Prochip Designer, QTouch, SAM-BA, SpyNIC, SST,
SST Logo, SuperFlash, tinyAVR, UNI/O, and XMEGA are registered trademarks of Microchip Technology
Incorporated in the U.S.A. and other countries.
ClockWorks, The Embedded Control Solutions Company, EtherSynch, Hyper Speed Control, HyperLight
Load, IntelliMOS, mTouch, Precision Edge, and Quiet-Wire are registered trademarks of Microchip
Technology Incorporated in the U.S.A.
Adjacent Key Suppression, AKS, Analog-for-the-Digital Age, Any Capacitor, AnyIn, AnyOut, BodyCom,
CodeGuard, CryptoAuthentication, CryptoAutomotive, CryptoCompanion, CryptoController, dsPICDEM,
dsPICDEM.net, Dynamic Average Matching, DAM, ECAN, EtherGREEN, In-Circuit Serial Programming,
ICSP, INICnet, Inter-Chip Connectivity, JitterBlocker, KleerNet, KleerNet logo, memBrain, Mindi, MiWi,
motorBench, MPASM, MPF, MPLAB Certified logo, MPLIB, MPLINK, MultiTRAK, NetDetach, Omniscient
Code Generation, PICDEM, PICDEM.net, PICkit, PICtail, PowerSmart, PureSilicon, QMatrix, REAL ICE,
Ripple Blocker, SAM-ICE, Serial Quad I/O, SMART-I.S., SQI, SuperSwitcher, SuperSwitcher II, Total
Endurance, TSHARC, USBCheck, VariSense, ViewSpan, WiperLock, Wireless DNA, and ZENA are
trademarks of Microchip Technology Incorporated in the U.S.A. and other countries.
SQTP is a service mark of Microchip Technology Incorporated in the U.S.A.
Silicon Storage Technology is a registered trademark of Microchip Technology Inc. in other countries.
GestIC is a registered trademark of Microchip Technology Germany II GmbH & Co. KG, a subsidiary of
Microchip Technology Inc., in other countries.
All other trademarks mentioned herein are property of their respective companies.
© 2018, Microchip Technology Incorporated, Printed in the U.S.A., All Rights Reserved.

ISBN: 978-1-5224-4642-2


Quality Management System Certified by DNV

ISO/TS 16949
Microchip received ISO/TS-16949:2009 certification for its worldwide headquarters, design and wafer
fabrication facilities in Chandler and Tempe, Arizona; Gresham, Oregon and design centers in California
and India. The Company’s quality system processes and procedures are for its PIC® MCUs and dsPIC®
DSCs, KEELOQ® code hopping devices, Serial EEPROMs, microperipherals, nonvolatile memory and




© 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 2127
                                                SAM D5x/E5x Family Data Sheet

analog products. In addition, Microchip’s quality system for the design and manufacture of development
systems is ISO 9001:2000 certified.




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 2128
