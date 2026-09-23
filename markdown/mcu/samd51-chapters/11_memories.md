# 9. Memories

*Source: `Atmel-SAMD51.pdf`, pages 54-60 — SAMD51 family datasheet*

                                                           SAM D5x/E5x Family Data Sheet
                                                                                                       Memories


9.      Memories

9.1     Embedded Memories
          • Internal high-speed Flash with Read-While-Write (RWW) capability on a section of the array
          • Internal high-speed RAM, single-cycle access at full speed
          • Internal backup RAM, single-cycle access at full speed



9.2     Physical Memory Map
        The high-speed bus is implemented as a bus matrix. All high-speed bus addresses are fixed, and they
        are never remapped in any way, even during boot. The 32-bit physical address space is mapped as
        follows:
        Table 9-1. Physical Memory Map

                                                                 Size in KB (unless otherwise stated)
                                                           SAMD51x20        SAMD51x19
                   Memory                  Start Address                                          SAMD51x18
                                                           SAME51x20        SAME51x19
                                                                                                  SAME51x18
                                                           SAME53x20        SAME53x19
                                                                                                  SAME53x18
                                                           SAME54x20        SAME54x19
               Embedded Flash               0x00000000       1024                512                   256
              Embedded SRAM                 0x20000000        256                192                   128
             Peripheral Bridge A            0x40000000
             Peripheral Bridge B            0x41000000
                                                                              16384 Bytes
             Peripheral Bridge C            0x42000000
             Peripheral Bridge D            0x43000000
                Backup SRAM                 0x47000000                              8
               NVM User Page                0x00804000                          512 Bytes

        Note:
         1. X = G, J, N or P. Refer to Ordering Information for available device part numbers.

9.2.1   Flash Memory Parameters
        A single page contains 512 Bytes, which is applicable to all the device part numbers listed in the
        Configuration Summary.
        Number of pages available in a device part number will vary depending on available maximum Flash
        memory size.
        Equation 9-1. Calculating Flash Memory
                          ����ℎ���� �����
        ������������� =
                          �������� �����




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 54
                                                       SAM D5x/E5x Family Data Sheet
                                                                                                   Memories


9.3   SRAM Memory Configuration

      Retention
      Depending on the application and power budget needs, part of the system memory can be retained in
      Standby or Hibernate sleep modes. The amount of the SRAM retained in this mode is software
      selectable, by writing the RAMCFG bits in the Power Manager Standby Configuration register and
      Hibernate Configuration register respectively (STDBYCFG.RAMCFG and HIBCFG.RAMCFG).
      By default, the entire system memory section is retained, but no retention or bottom 32KB memory
      retention options are also available.
      Figure 9-1. Retention Options
                                                                                           Full SRAM Size




                               Full Memory                             No Memory
                                Retention                               Retention




                                                                                           32 KB
                                                   32 KB
                                                  Retention
           0x20000000                                                                      0 KB

      RAM Error Correction
      For safety applications, the SAM D5x/E5x family embeds error correction codes (ECC) to detect and
      correct single bit errors, or to enable dual error detection for the system memory. The ECC is software
      selectable through the RAM ECCDIS bit in the NVM User Row. For additional information, refer to Table
      9-2.
      When enabled, the top half system memory will be reserved to store the ECC, and will not be available
      for the application.




      © 2019 Microchip Technology Inc.                  Datasheet                           DS60001507E-page 55
                                                             SAM D5x/E5x Family Data Sheet
                                                                                                  Memories

Figure 9-2. Memory with RAM Error Correction
                                          SAME54x20             SAME54x19
                                                                                    256KB



                                                                                    192KB



                                          Error Correction



                                                                 Error Correction



                                                                                    128KB



                                                                                    96KB




                                                                                    32KB



                             0x20000000                                             0KB



Note: If the ECC is used, full SRAM retention must be enabled.

CoreSight ETB Connection
When enabled, the bottom 32 KB system memory space is reserved for CoreSight ETB debug usage.
The figure below shows an example where both ECC and CoreSight ETB are enabled.




© 2019 Microchip Technology Inc.                             Datasheet                      DS60001507E-page 56
                                                                   SAM D5x/E5x Family Data Sheet
                                                                                                                Memories

      Figure 9-3. Memory with ECC and CoreSight ETB
                                                SAME54x20             SAME54x19
                                                                                           256KB



                                                                                           192KB



                                                Error Correction



                                                                       Error Correction



                                                                                           128KB



                                                                                           96KB




                                                                                           32KB

                                                 CoreSight ETB         CoreSight ETB
                                   0x20000000                                              0KB




9.4   NVM User Page Mapping
      The NVM User Page can be read at address 0x00804000. The size of the NVM User Page is 512 Bytes.
      The first eight 32-bit words (32 Bytes) of the Non Volatile Memory (NVM) User Page contain calibration
      data that are automatically read at device power on. The remaining 480 Bytes can be used for storing
      custom parameters.
      To write the NVM User Page, refer to the NVMCTRL (Non-Volatile Memory Controller) documentation.
      When writing to the user pages, the new values do not get loaded by the other peripheral on the device
      until a device reset occurs.
      Note: Before erasing the NVM User Page, ensure that the first 32 Bytes are read to a buffer and later
      written back to the same area unless a configuration change is intended.
      Table 9-2. NVM User Page Mapping - Dedicated Entries

       Bit Pos. Name                       Usage                                     Related Peripheral      Default
                                                                                     Register                Values
       0           BOD33 Disable           BOD33 Disable at power-on.                SUPC.BOD33              0x1
       8:1         BOD33 Level             BOD33 threshold level at power- SUPC.BOD33                        0x1C
                                           on.
       10:9        BOD33 Action            BOD33 Action at power-on.                 SUPC.BOD33              0x1
       14:11       BOD33 Hysteresis BOD33 Hysteresis configuration                   SUPC.BOD33              0x2
                                    at power-on.




      © 2019 Microchip Technology Inc.                             Datasheet                              DS60001507E-page 57
                                                     SAM D5x/E5x Family Data Sheet
                                                                                                   Memories

...........continued
 Bit Pos. Name                     Usage                               Related Peripheral      Default
                                                                       Register                Values
 25:15       BOD12 Calibration Factory settings - do not change.(1)                            -
             Parameters
 29:26       NVM BOOT              NVM Bootloader Size                 NVMCTRL                 0xF
 31:30       Reserved              Factory settings - do not change.                           -
 35:32       SEESBLK               Number of NVM Blocks                NVMCTRL                 0x0
                                   composing a SmartEEPROM
                                   sector
 38:36       SEEPSZ                SmartEEPROM Page Size               NVMCTRL                 0x0
 39          RAM ECCDIS            RAM ECC Disable                     RAMECC                  0x1
 47:40       Reserved              Factory settings - do not change.                           -
 48          WDT Enable            WDT Enable at power-on.             WDT.CTRLA               0x0
 49          WDT Always-On         WDT Always-On at power-on.          WDT.CTRLA               0x0
 53:50       WDT Period            WDT Period at power-on.             WDT.CONFIG              0xB
 57:54       WDT Window            WDT Window mode time-out at         WDT.CONFIG              0xB
                                   power-on.
 61:58       WDT EWOFFSET          WDT Early Warning Interrupt         WDT.EWCTRL              0xB
                                   Time Offset at power-on.
 62          WDT WEN               WDT Timer Window Mode               WDT.CTRLA               0x0
                                   Enable at power-on.
 63          Reserved              Factory settings - do not change.
 95:64       NVM LOCKS             NVM Region Lock Bits.               NVMCTRL                 0xFFFF FFFF
 127:96      (fourth word)         User page
 159:128 Reserved                  Factory settings - do not change.
 Other       -                     User pages


      CAUTION
                 1.    BOD12 is calibrated in production, and the calibration parameters must not be changed to
                       ensure the correct device behavior.


Related Links
25. NVMCTRL – Nonvolatile Memory Controller
19. SUPC – Supply Controller
19.8.5 BOD33
20. WDT – Watchdog Timer
20.8.1 CTRLA




© 2019 Microchip Technology Inc.                      Datasheet                             DS60001507E-page 58
                                                         SAM D5x/E5x Family Data Sheet
                                                                                                            Memories

      20.8.2 CONFIG
      20.8.3 EWCTRL
      45.6.3.1 Device Temperature Measurement



9.5   NVM Software Calibration Area Mapping
      The NVM Software Calibration Area contains calibration data that are determined and written during
      production test. These calibration values should be read by the application software and written back to
      the corresponding register.
      The NVM Software Calibration Area can be read at address 0x00800080.
      The NVM Software Calibration Area can not be written.
      Table 9-3. NVM Software Calibration Area Mapping

       Bit Position Name                    Description                                                 Default
                                                                                                        Value
       1:0              AC BIAS             AC Comparator 0/1 Bias Scaling. To be written to            0x1
                                            the AC CALIB register.
       4:2              ADC0 BIASCOMP       Bias comparator scaling. To be written to the ADC0          0x7
                                            CALIB register.
       7:5              ADC0 BIASREFBUF Bias reference buffer scaling. To be written to the             0x7
                                        ADC0 CALIB register.
       10:8             ADC0 BIASR2R        Bias rail-to-rail amplifier scaling. To be written to the   0x7
                                            ADC0 CALIB register.
       15:11            Reserved            -                                                           -
       18:16            ADC1 BIASCOMP       Bias comparator scaling. To be written to the ADC1          0x7
                                            CALIB register.
       21:19            ADC1 BIASREFBUF Bias reference buffer scaling. To be written to the             0x7
                                        ADC1 CALIB register.
       24:22            ADC1 BIASR2R        Bias rail-to-rail amplifier scaling. To be written to the   0x7
                                            ADC1 CALIB register.
       35:25            Reserved            -                                                           -
       36:32            USB TRANSN          USB TRANSN calibration value. To be written to the 0x09
                                            USB PADCAL register.
       41:37            USB TRANSP          USB TRANSP calibration value. To be written to the          0x19
                                            USB PADCAL register.
       44:42            USB TRIM            USB TRIM calibration value. To be written to the            0x6
                                            USB PADCAL register.

      The NVM Software Calibration Area for temperature calibration parameters can not be written.
      The NVM Software Calibration Area for temperature calibration parameters can be read at address
      0x00800100.




      © 2019 Microchip Technology Inc.                     Datasheet                              DS60001507E-page 59
                                                         SAM D5x/E5x Family Data Sheet
                                                                                                  Memories

      Table 9-4. NVM Software Calibration Area Mapping - Temperature Calibration Parameters

       Bit Position Name                 Description
       7:0              TLI              Integer part of calibration temperature TL
       11:8             TLD              Decimal part of calibration temperature TL
       19:12            THI              Integer part of calibration temperature TH
       23:20            THD              Decimal part of calibration temperature TH
       39:24            Reserved         Reserved for future use.
       51:40            VPL              Temperature calibration parameters.
       63:52            VPH
       75:63            VCL
       87:76            VCH
       127:88           Reserved         Reserved for future use.

      Note: Engineering Sample devices have no valid temperature calibration parameters.



9.6   Serial Number
      Each device has a unique 128-bit serial number which is a concatenation of four 32-bit words contained
      at the following addresses:
      Word 0: 0x008061FC
      Word 1: 0x00806010
      Word 2: 0x00806014
      Word 3: 0x00806018
      The uniqueness of the serial number is guaranteed only when using all 128 bits.




      © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 60
