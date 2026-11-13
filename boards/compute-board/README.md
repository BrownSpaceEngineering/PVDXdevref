# PVDX Compute Board

This repo contains kicad files for the PVDX Compute board, the main command/control interface for PVDX. The board contains: the SAMD51 microcontroller, 3 MRAM chips, an accelerometer, a 3-axis magnetometer, and headers for interfacing with the EPS, the battery board, the burn wire, the photodiodes, the ADCS/perovskite boards, the S-Band, the UHF, the display, and the ArduCam. 

The repo is organized into four main folders: 
1. Components (kicad symbols, footprints, and step files for each component not already built into the kicad libraries; shared between the other three folders)
2. SAMD51 Devboard (a simplified version for testing; it is run off USB-C, and houses only buck converters (not present on the final boards) and the SAMD51. All other components are exposed as headers. Every pin on the SAMD51 is also exposed)
3. Compute Board (the two layer implementation of the unified board containing all the final flight components with headers only for peripherals)
4. compute4layer (a copy of the Compute Board project with only the layout changed to a 4-layer (signal, GND, power, signal) stackup)

## Schematics 

Presented here are images of the schematics shared by the Compute Board and compute4layer: 
<img width="1571" height="1089" alt="image" src="https://github.com/user-attachments/assets/00618cd4-b301-4f3a-91be-1605d36d1eb8" />
<img width="1554" height="1076" alt="image" src="https://github.com/user-attachments/assets/566f2a2b-d947-4330-9a75-8fb0b2f780f4" />
<img width="1567" height="1081" alt="image" src="https://github.com/user-attachments/assets/c0bb2190-1a8c-4a0a-bd27-0210650a50a2" />

## Datasheets

For ease of access, here is a table of datasheets for the onboard components: 

| Component   | Part number |
| ----------- | ----------- | 
| SAMD51 | [Microchip ATSAMD51N19A](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-D5x-E5x-Family-Data-Sheet-DS60001507.pdf) |
| MRAM        | [Everspin EM008LX](https://datasheet.lcsc.com/datasheet/pdf/902c3bb2baf214246dee551af985b64a.pdf?productCode=C17289052) |
| Accelerometer   | [Murata SCH16T-K01](https://sensorsandpower.angst-pfister.com/fileadmin/images/news/Datasheet-SCH16T-K01_JAN2024.pdf) |
| Magnetometer | [PNI RM3100](https://www.tri-m.com/products/pni/RM3100-User-Manual.pdf) |
| Buck converter | [Microchip MCP-1604-180I](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/22042B.pdf) |
| I2C Multiplexer | [TI TCA9546A](https://www.ti.com/lit/ds/symlink/tca9546a.pdf?ts=1790848067365&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FTCA9546A%253Futm_source%253Dgoogle%2526utm_medium%253Dcpc%2526utm_campaign%253Dasc-tech-inno-dynpf_interface-cpc-pf-google-eu_en_int%2526utm_content%253Dprodfolddynamic%2526gclsrc%253Daw.ds%2526gad_source%253D1%2526gad_campaignid%253D23906084824%2526gbraid%253D0AAAAAC068F1EFfNekYsYivcdyWkmR2bSt%2526gclid%253DCjwKCAjwifjVBhBKEiwAYx4K9HgTKyl_4xHH1cxt9nXmtXohIvQla9mqUfnjyi_wMP_Zy_10j3Y5wxoCV-IQAvD_BwE) | 
