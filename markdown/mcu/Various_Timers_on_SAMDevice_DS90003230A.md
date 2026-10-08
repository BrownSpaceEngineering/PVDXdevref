# Various_Timers_on_SAMDevice_DS90003230A

*Source: `original/mcu/Various_Timers_on_SAMDevice_DS90003230A.pdf` (10 pages)*

<!-- page 1 -->



# **TB3230** 

## **Various Timers on SAM Devices** 

### **Introduction** 

Timers are fundamental modules used in microcontroller-based embedded applications. It is hard to imagine designing an embedded application without using timers. Timers are peripherals that generate periodic events used to measure time intervals, generate delays, and time outs. Timers are also used in other application scenarios, such as generating PWM outputs, capturing inputs, and so on. 

In any embedded application, CPU and resource utilization plays a crucial role in the performance of the application function. For example, if there are no timers, to blink an LED every 2 seconds, the application needs to continuously check whether the time has elapsed. While the application regularly checks the elapsed time, the CPU has nothing meaningful to do, in the process valuable CPU bandwidth gets wasted. Timers can be used in such scenarios to generate an interrupt at specified time, meanwhile the CPU can perform other meaningful tasks, or can sleep for that duration to save power. 

Microchip’s Smart ARM (SAM) series of microcontrollers (MCUs) come with a variety of timers, which provide flexibility in developing the real-time embedded applications. 

This document discusses the possible application scenarios under which the timers in the SAM series of MCUs can be used. 

DS90003230A-page 1 

© 2019 Microchip Technology Inc. 



<!-- page 2 -->

**TB3230** 

### **Table of Contents** 

|Introduction.....................................................................................................................................................1|
|---|
|1.<br>Description.............................................................................................................................................. 3|
|2.<br>Implementation........................................................................................................................................6|
|3.<br>Resources...............................................................................................................................................7|
|The Microchip Website...................................................................................................................................8|
|Product Change Notification Service..............................................................................................................8|
|Customer Support.......................................................................................................................................... 8|
|Microchip Devices Code Protection Feature..................................................................................................8|
|Legal Notice................................................................................................................................................... 8|
|Trademarks.................................................................................................................................................... 9|
|Quality Management System......................................................................................................................... 9|
|Worldwide Sales and Service.......................................................................................................................10|



DS90003230A-page 2 

© 2019 Microchip Technology Inc. 



<!-- page 3 -->

**TB3230 Description** 

### **1.** 

### **Description** 

The SAM series of MCUs supports the following timers: 

- Watchdog Timer (WDT) 

- Real-Time Timer (RTT) 

- Real-Time Clock (RTC) 

- System Timer (SysTick) 

- Timer/Counter (TC) 

- Timer/Counter for Control Applications (TCC) 

#### **Watchdog Timer (WDT)** 

An embedded system must be designed in such a way that it is more independent. In case of a system hang, it must be able to recover from the situation without any user intervention. System hanging can be dangerous in real-time applications, for example, a car moving at high speed, goes out of control and crashes. The air bags do not kick in at right time due to a software hang. This is a dangerous and a life-threatening situation. It is imperative for the application to be designed for such scenarios to be real time responsive and self-reliant. This is an example of a situation where WDT can be used. 

The WDT can be used to monitor software hangs and deadlock situations. The WDT makes it possible to recover from such error conditions by resetting the processor. This timer is configured to a predefined time-out period and is constantly running when enabled. It does not reset until the predefined timeout period elapses or an application clears it. 

The WDT peripheral is available in all the SAM family of devices. 

#### **Real-Time Timer (RTT)** 

Performance and low-power consumption are two important requirements of modern embedded devices. For example, an IoT-based health monitoring wearable device monitors the heartbeat, step count, distance covered, and so on. Because the device needs to continuously monitor the health parameters, it needs to have a high-resolution timer. The device needs to consume less power as it operates on a battery power source. The RTT module in SAM devices is a good choice to address the needs of these real-time low-power applications. 

The RTT is built around a 32-bit counter sourced from the 32 kHz internal or external oscillator, which can generate periodic interrupts or triggers an alarm on a programmed value. The RTT can be used for applications which need attention at regular intervals. It can generate the required time interval with low-power capability, as it uses a slow 32 kHz clock. 

The RTT runs continuously till it reaches the maximum counter value and rolls out to zero once it overflows. If the RTT is programmed to generate an alarm in between, the user must be aware of clearing it after the alarm as it continuously runs. 

The RTT peripheral module is available in the SAM E70/S70/V7x/G55 family of devices. 

#### **Real Time Clock (RTC)** 

The RTC is used to provide a precise time and date. It plays a very important role in the embedded systems applications, such as the digital clock, data logging system, and so on. The RTC is a good option for applications which need time stamps. 

Consider the example of a greenhouse farming embedded application. The embedded device monitors the environment of the greenhouse. The system is designed in such a way that the device monitors the temperature and humidity every hour and logs the data to the sever. The RTC is a good timer choice to implement the periodic data logging, particularly in terms of resource and power utilization. The system can be designed in such a way that the RTC can monitor time in Sleep mode, wake up the CPU every hour, log data, and go back to sleep. 

The RTC typically runs continuously to keep track of time. The RTC enables periodic events, as well as interrupts at a specified time. It operates in low power with a 32 kHz external or internal crystal, and the RTC can run when the main system is powered down. This enables it to maintain current time against an absolute time reference. 

DS90003230A-page 3 

© 2019 Microchip Technology Inc. 



<!-- page 4 -->

**TB3230 Description** 

Additionally, the RTC provides an alarm option. An alarm time can be set in the device and moved to low power. Since the RTC continuously keeps track of time, whenever the current time matches with the alarm time it triggers an interrupt and can wake up the device. 

Most of the SAM devices support 12-hour or 24-hour time formats, and time is represented as seconds, minutes, and hours. The date is represented as day, month, and year. The SAM devices support the leap year correction feature. 

The RTC peripheral is available in all the SAM family of devices. 

## **System Timer (SysTick)** 

As part of the Cortex-M core, ARM provides a basic timer called as System Timer (SysTick). The Cortex-M CPU architecture is used in various computing devices such as, MCUs, ASICs, and so on. ARM provides SysTick as part of the Cortex-M core, hence applications that require basic timing functionality does not need to depend on a dedicated timer. 

On Cortex-M based SAM devices, in RTOS-based applications, the Systick could be the timer choice to implement the RTOS’s periodic tick time functionality as it is closely tied to the CPU and easy to port across another platform. In Non-RTOS based applications, the SysTick could be used for any general timer periodic functions. 

The SysTick as a timer choice is useful in applications where the CPU goes into Low-Power mode (Idle sleep) while the peripherals are running, and timing functionality is not required in Sleep mode. Because the SysTick is tightly tied to the CPU core, when the SAM device goes into Idle Sleep mode, the SysTick also goes to sleep along with it, therefore helping to reduce the power consumed. After the device wakes up, with the occurrence of an event or interrupt, the SysTick timer comes back and continues ticking once the CPU is active. 

The SysTick is designed as 24-bit countdown timer with an automatic reload option, once the timer is started it counts down till it reaches zero. Then it raises an interrupt and loads the new count value to reload the register. The SysTick can be clocked from the processor clock. 

The SysTick peripheral is available in all the SAM family of devices. 

## **Timer/Counter (TC)** 

Embedded applications need the generation of precision time delays, such as the counting of events, generating a specific time to switch on lights, traffic signals, and so on. Most of the embedded products need the time component to operate. The Timer/Counter (TC) in a microcontroller plays a crucial role in performing these tasks. 

The TC module of the SAM devices helps in generating delays to synchronize events, or can provide timeouts in a protocol data exchange. For example, the system (master) is running at a high frequency, but the slave interacting with the master is running at much lower frequency. This leads to synchronization issues. A small amount of delay may be needed in order to synchronize both master and slave. Similarly, while communicating with devices through protocol, sometimes a timeout is needed and needs to be retried if the slave does not respond. The TC is useful in such scenarios. 

The TC consists of counter with an 8-bit, 16-bit, or 32-bit selectable configuration, an internal prescaler, and compare/ capture channels. The TC is clocked from the Generic Clock and Advanced Peripheral Bus (APB). 

The TC can also perform waveform generation, such as frequency generation and single slope pulse-width modulation (PWM) generation. It can be used in a smart home example to control appliances, such as the dimming of light, or regulating a fan. The appliances cannot be directly fed an analog, digital zero, or high-voltage level to control them, this action will either switch them off or on. The wave generation ability Capture mode is useful in calculating the duty cycle, frequency, and pulse width of the TC module, and will be helpful in controlling appliances. 

The TC peripheral is available in all the SAM family of devices. 

## **Timer/Counter for Control Applications (TCC)** 

Motors are one of the important components used in appliances and products. Motors are found in Electric fans, washing machines, refrigerators, water pumps, and so on. 

When an appliance has a motor as a component, such as in a washing machine application, the motor rotates in either forward or reverse direction for specific time interval to complete the desired task. To develop such motorcontrolled products, a control application is necessary to perform the tasks. To enable such application development, the SAM MCUs have a module called the Timer/Counter for Control Applications (TCC) which helps in providing necessary counts, clock pulses, events, and wave generation for controlling the motors. 

DS90003230A-page 4 

© 2019 Microchip Technology Inc. 



<!-- page 5 -->

**TB3230 Description** 

The TCC consists of a counter, a prescaler, compare/capture channels, and control logic. The counter feature with the compare/capture channel can be used for capturing the frequency and pulse width of the input. The TCC can generate a waveform, such as frequency generation and pulse-width modulation, which can be used in controlling motor applications. Generated waveforms can also be used for ballast in LED, H-bridge, power converters, and other types of power control applications. They allow for low-side and high-side output with optional dead-time insertion. 

The TCC peripheral is available in all the SAM C2x/D1x/D21/DA1/L2x/D5x/E5x family of devices. 

The following table provides the possible application usage scenarios of the various timers available in the SAM family of devices. 

|**Possible Usage**<br>**Scenario**|**WDT**|**RTT**|**RTC**|**SysTick**|**TC**|**TCC**|
|---|---|---|---|---|---|---|
|**Software Reset/**<br>**System Hang**|✔|✖|✖|✖|✖|✖|
|**Periodic Functions**|✖|✔|✖|✔|✔|✔|
|**Periodic Events with**<br>**Low Power**|✖|✔|✔|✖|✖|✖|
|**Clock/Calendar**|✖|✖|✔|✖|✖|✖|
|**Frequency**<br>**Generation**|✖|✖|✖|✖|✔|✔|
|**Motor Control**|✖|✖|✖|✖|✖|✔|
|**Input capture**|✖|✖|✖|✖|✔|✔|
|**Single-slope PWM**<br>**generation**|✖|✖|✖|✖|✔|✔|
|**Dual-slope PWM**|✖|✖|✖|✖|✖|✔|
|**RTOS**|✖|✖|✖|✔|✖|✖|



**Note:** The items displaying “✖” do not necessarily mean that the usage cannot be done. This table only shows a small number of suggestions for the scenarios where timers can be used in the SAM family of devices. 

DS90003230A-page 5 

© 2019 Microchip Technology Inc. 



<!-- page 6 -->

**TB3230 Implementation** 

# **2. Implementation** 

MPLAB<sup>®</sup> Harmony v3 is a fully integrated embedded software development framework. It provides interoperable firmware libraries for application development on 32-bit microcontrollers and microprocessors. It includes an easy to use Graphical User Interface (MPLAB Harmony Configurator) for selecting, configuring, and generating starter codes, peripheral libraries and middlewares (USB, TCP/IP, graphics, and so on). 

The following are the basic repositories necessary to build applications using MPLAB Harmony v3 framework. These repositories are available on GitHub. 

- CSP (Chip Support Package) 

- DEV_PACKS (Harmony 3 Product Database) 

- MHC (Harmony 3 Configurator) 

Use the MPLAB Harmony 3 Framework Downloader to download the repositories. 

MPLAB Harmony v3 provides examples for every peripheral module available. The example references for the Timer Modules discussed in this document are as follows: 

- Watchdog Timer 

- Real-time Timer 

- Real Time clock 

- System Timer 

- Timer/Counter 

- Timer/Counter for control applications 

DS90003230A-page 6 

© 2019 Microchip Technology Inc. 



<!-- page 7 -->

**TB3230 Resources** 

# **3. Resources** 

For additional information on timers, refer to the following documents: 

- SAM D21 Timer/Counter (TC) Overview: https://microchipdeveloper.com/32arm:samd21-tc-overview 

- Guide for Timer-based Driven Shield on SAM Devices: 

   - https://microchipdeveloper.com/touch:guide-for-timer-based-driven-shield-on-sam-devices 

- Using the Timer Counter for Control Applications in SAM D11: 

   - http://ww1.microchip.com/downloads/en/AppNotes/Atmel-42357-Using-the-Timer-Counter-for-ControlApplications_ApplicationNote_AT07690.pdf 

- SAM D21 System Timer (SysTick): 

   - https://microchipdeveloper.com/32arm:samd21-systick 

DS90003230A-page 7 

© 2019 Microchip Technology Inc. 



<!-- page 8 -->

**TB3230** 

# **The Microchip Website** 

Microchip provides online support via our website at http://www.microchip.com/. This website is used to make files and information easily available to customers. Some of the content available includes: 

- **Product Support** – Data sheets and errata, application notes and sample programs, design resources, user’s guides and hardware support documents, latest software releases and archived software 

- **General Technical Support** – Frequently Asked Questions (FAQs), technical support requests, online discussion groups, Microchip design partner program member listing 

- **Business of Microchip** – Product selector and ordering guides, latest Microchip press releases, listing of seminars and events, listings of Microchip sales offices, distributors and factory representatives 

# **Product Change Notification Service** 

Microchip’s product change notification service helps keep customers current on Microchip products. Subscribers will receive email notification whenever there are changes, updates, revisions or errata related to a specified product family or development tool of interest. 

To register, go to http://www.microchip.com/pcn and follow the registration instructions. 

# **Customer Support** 

Users of Microchip products can receive assistance through several channels: 

- Distributor or Representative 

- Local Sales Office 

- Embedded Solutions Engineer (ESE) 

- Technical Support 

Customers should contact their distributor, representative or ESE for support. Local sales offices are also available to help customers. A listing of sales offices and locations is included in this document. 

Technical support is available through the website at: http://www.microchip.com/support 

# **Microchip Devices Code Protection Feature** 

Note the following details of the code protection feature on Microchip devices: 

- Microchip products meet the specification contained in their particular Microchip Data Sheet. 

- Microchip believes that its family of products is one of the most secure families of its kind on the market today, when used in the intended manner and under normal conditions. 

- There are dishonest and possibly illegal methods used to breach the code protection feature. All of these methods, to our knowledge, require using the Microchip products in a manner outside the operating specifications contained in Microchip’s Data Sheets. Most likely, the person doing so is engaged in theft of intellectual property. 

- Microchip is willing to work with the customer who is concerned about the integrity of their code. 

- Neither Microchip nor any other semiconductor manufacturer can guarantee the security of their code. Code protection does not mean that we are guaranteeing the product as “unbreakable.” 

Code protection is constantly evolving. We at Microchip are committed to continuously improving the code protection features of our products. Attempts to break Microchip’s code protection feature may be a violation of the Digital Millennium Copyright Act. If such acts allow unauthorized access to your software or other copyrighted work, you may have a right to sue for relief under that Act. 

# **Legal Notice** 

Information contained in this publication regarding device applications and the like is provided only for your convenience and may be superseded by updates. It is your responsibility to ensure that your application meets with 

DS90003230A-page 8 

© 2019 Microchip Technology Inc. 



<!-- page 9 -->

**TB3230** 

your specifications. MICROCHIP MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED, WRITTEN OR ORAL, STATUTORY OR OTHERWISE, RELATED TO THE INFORMATION, INCLUDING BUT NOT LIMITED TO ITS CONDITION, QUALITY, PERFORMANCE, MERCHANTABILITY OR FITNESS FOR PURPOSE. Microchip disclaims all liability arising from this information and its use. Use of Microchip devices in life support and/or safety applications is entirely at the buyer’s risk, and the buyer agrees to defend, indemnify and hold harmless Microchip from any and all damages, claims, suits, or expenses resulting from such use. No licenses are conveyed, implicitly or otherwise, under any Microchip intellectual property rights unless otherwise stated. 

# **Trademarks** 

The Microchip name and logo, the Microchip logo, Adaptec, AnyRate, AVR, AVR logo, AVR Freaks, BesTime, BitCloud, chipKIT, chipKIT logo, CryptoMemory, CryptoRF, dsPIC, FlashFlex, flexPWR, HELDO, IGLOO, JukeBlox, KeeLoq, Kleer, LANCheck, LinkMD, maXStylus, maXTouch, MediaLB, megaAVR, Microsemi, Microsemi logo, MOST, MOST logo, MPLAB, OptoLyzer, PackeTime, PIC, picoPower, PICSTART, PIC32 logo, PolarFire, Prochip Designer, QTouch, SAM-BA, SenGenuity, SpyNIC, SST, SST Logo, SuperFlash, Symmetricom, SyncServer, Tachyon, TempTrackr, TimeSource, tinyAVR, UNI/O, Vectron, and XMEGA are registered trademarks of Microchip Technology Incorporated in the U.S.A. and other countries. 

APT, ClockWorks, The Embedded Control Solutions Company, EtherSynch, FlashTec, Hyper Speed Control, HyperLight Load, IntelliMOS, Libero, motorBench, mTouch, Powermite 3, Precision Edge, ProASIC, ProASIC Plus, ProASIC Plus logo, Quiet-Wire, SmartFusion, SyncWorld, Temux, TimeCesium, TimeHub, TimePictra, TimeProvider, Vite, WinPath, and ZL are registered trademarks of Microchip Technology Incorporated in the U.S.A. 

Adjacent Key Suppression, AKS, Analog-for-the-Digital Age, Any Capacitor, AnyIn, AnyOut, BlueSky, BodyCom, CodeGuard, CryptoAuthentication, CryptoAutomotive, CryptoCompanion, CryptoController, dsPICDEM, dsPICDEM.net, Dynamic Average Matching, DAM, ECAN, EtherGREEN, In-Circuit Serial Programming, ICSP, INICnet, Inter-Chip Connectivity, JitterBlocker, KleerNet, KleerNet logo, memBrain, Mindi, MiWi, MPASM, MPF, MPLAB Certified logo, MPLIB, MPLINK, MultiTRAK, NetDetach, Omniscient Code Generation, PICDEM, PICDEM.net, PICkit, PICtail, PowerSmart, PureSilicon, QMatrix, REAL ICE, Ripple Blocker, SAM-ICE, Serial Quad I/O, SMART-I.S., SQI, SuperSwitcher, SuperSwitcher II, Total Endurance, TSHARC, USBCheck, VariSense, ViewSpan, WiperLock, Wireless DNA, and ZENA are trademarks of Microchip Technology Incorporated in the U.S.A. and other countries. 

SQTP is a service mark of Microchip Technology Incorporated in the U.S.A. 

The Adaptec logo, Frequency on Demand, Silicon Storage Technology, and Symmcom are registered trademarks of Microchip Technology Inc. in other countries. 

GestIC is a registered trademark of Microchip Technology Germany II GmbH & Co. KG, a subsidiary of Microchip Technology Inc., in other countries. 

All other trademarks mentioned herein are property of their respective companies. 

© 2019, Microchip Technology Incorporated, Printed in the U.S.A., All Rights Reserved. 

ISBN: 978-1-5224-5259-1 

# **Quality Management System** 

For information regarding Microchip’s Quality Management Systems, please visit http://www.microchip.com/quality. 

DS90003230A-page 9 

© 2019 Microchip Technology Inc. 



<!-- page 10 -->



# **Worldwide Sales and Service** 

|**AMERICAS**|**ASIA/PACIFIC**|**ASIA/PACIFIC**|**EUROPE**|
|---|---|---|---|
|**Corporate Office**<br>2355 West Chandler Blvd.<br>Chandler, AZ 85224-6199<br>Tel: 480-792-7200<br>Fax: 480-792-7277<br>Technical Support:<br>http://www.microchip.com/support<br>Web Address:<br>http://www.microchip.com<br>**Atlanta**<br>Duluth, GA<br>Tel: 678-957-9614<br>Fax: 678-957-1455<br>**Austin, TX**|**Australia - Sydney**<br>Tel: 61-2-9868-6733<br>**China - Beijing**<br>Tel: 86-10-8569-7000<br>**China - Chengdu**<br>Tel: 86-28-8665-5511<br>**China - Chongqing**<br>Tel: 86-23-8980-9588<br>**China - Dongguan**<br>Tel: 86-769-8702-9880<br>**China - Guangzhou**<br>Tel: 86-20-8755-8029<br>**China - Hangzhou**<br>Tel: 86-571-8792-8115|**India - Bangalore**<br>Tel: 91-80-3090-4444<br>**India - New Delhi**<br>Tel: 91-11-4160-8631<br>**India - Pune**<br>Tel: 91-20-4121-0141<br>**Japan - Osaka**<br>Tel: 81-6-6152-7160<br>**Japan - Tokyo**<br>Tel: 81-3-6880- 3770<br>**Korea - Daegu**<br>Tel: 82-53-744-4301<br>**Korea - Seoul**<br>Tel: 82-2-554-7200|**Austria - Wels**<br>Tel: 43-7242-2244-39<br>Fax: 43-7242-2244-393<br>**Denmark - Copenhagen**<br>Tel: 45-4450-2828<br>Fax: 45-4485-2829<br>**Finland - Espoo**<br>Tel: 358-9-4520-820<br>**France - Paris**<br>Tel: 33-1-69-53-63-20<br>Fax: 33-1-69-30-90-79<br>**Germany - Garching**<br>Tel: 49-8931-9700<br>**Germany - Haan**|
|Tel: 512-257-3370<br>**Boston**<br>Westborough, MA<br>Tel: 774-760-0087<br>Fax: 774-760-0088<br>**Chicago**<br>Itasca, IL<br>Tel: 630-285-0071<br>Fax: 630-285-0075<br>**Dallas**<br>Addison, TX<br>Tel: 972-818-7423<br>Fax: 972-818-2924<br>**Detroit**<br>Novi, MI<br>Tel: 248-848-4000<br>**Houston, TX**<br>Tel: 281-894-5983<br>**Indianapolis**<br>Noblesville, IN<br>Tel: 317-773-8323<br>Fax: 317-773-5453<br>Tel: 317-536-2380<br>**Los Angeles**<br>Mission Viejo, CA<br>Tel: 949-462-9523<br>Fax: 949-462-9608<br>Tel: 951-273-7800<br>**Raleigh, NC**<br>Tel: 919-844-7510<br>**New York, NY**<br>Tel: 631-435-6000<br>**San Jose, CA**<br>Tel: 408-735-9110|**China - Hong Kong SAR**<br>Tel: 852-2943-5100<br>**China - Nanjing**<br>Tel: 86-25-8473-2460<br>**China - Qingdao**<br>Tel: 86-532-8502-7355<br>**China - Shanghai**<br>Tel: 86-21-3326-8000<br>**China - Shenyang**<br>Tel: 86-24-2334-2829<br>**China - Shenzhen**<br>Tel: 86-755-8864-2200<br>**China - Suzhou**<br>Tel: 86-186-6233-1526<br>**China - Wuhan**<br>Tel: 86-27-5980-5300<br>**China - Xian**<br>Tel: 86-29-8833-7252<br>**China - Xiamen**<br>Tel: 86-592-2388138<br>**China - Zhuhai**<br>Tel: 86-756-3210040|**Malaysia - Kuala Lumpur**<br>Tel: 60-3-7651-7906<br>**Malaysia - Penang**<br>Tel: 60-4-227-8870<br>**Philippines - Manila**<br>Tel: 63-2-634-9065<br>**Singapore**<br>Tel: 65-6334-8870<br>**Taiwan - Hsin Chu**<br>Tel: 886-3-577-8366<br>**Taiwan - Kaohsiung**<br>Tel: 886-7-213-7830<br>**Taiwan - Taipei**<br>Tel: 886-2-2508-8600<br>**Thailand - Bangkok**<br>Tel: 66-2-694-1351<br>**Vietnam - Ho Chi Minh**<br>Tel: 84-28-5448-2100|Tel: 49-2129-3766400<br>**Germany - Heilbronn**<br>Tel: 49-7131-72400<br>**Germany - Karlsruhe**<br>Tel: 49-721-625370<br>**Germany - Munich**<br>Tel: 49-89-627-144-0<br>Fax: 49-89-627-144-44<br>**Germany - Rosenheim**<br>Tel: 49-8031-354-560<br>**Israel - Ra’anana**<br>Tel: 972-9-744-7705<br>**Italy - Milan**<br>Tel: 39-0331-742611<br>Fax: 39-0331-466781<br>**Italy - Padova**<br>Tel: 39-049-7625286<br>**Netherlands - Drunen**<br>Tel: 31-416-690399<br>Fax: 31-416-690340<br>**Norway - Trondheim**<br>Tel: 47-72884388<br>**Poland - Warsaw**<br>Tel: 48-22-3325737<br>**Romania - Bucharest**<br>Tel: 40-21-407-87-50<br>**Spain - Madrid**<br>Tel: 34-91-708-08-90<br>Fax: 34-91-708-08-91<br>**Sweden - Gothenberg**<br>Tel: 46-31-704-60-40<br>**Sweden - Stockholm**<br>Tel: 46-8-5090-4654<br>**UK - Wokingham**|
|Tel: 408-436-4270<br>**Canada - Toronto**|||Tel: 44-118-921-5800<br>Fax: 44-118-921-5820|
|Tel: 905-695-1980<br>Fax: 905-695-2078||||



DS90003230A-page 10 

© 2019 Microchip Technology Inc. 

