# PVDX Datasheet Index

Converted from the original PDFs in `PVDXdocs/` into Markdown for fast,
greppable access. All files preserve page markers (`<!-- page N -->`) so you
can trace any claim back to a page in the source PDF. Clean tables detected
in the source are rendered as Markdown tables inline; everything else is
`pdftotext -layout` output, which keeps columns and register-bit tables
reasonably aligned even without table detection.

Start here, then open only the specific file(s) relevant to the peripheral
you're working on — most of these docs are long, and loading one is much
cheaper than loading the whole corpus.

## Battery Charger

| Part | File | Notes |
|---|---|---|
| MP2672A (2-cell Li-Ion/Li-Poly boost switching charger) | `battery-charger/MP2672AGD.md` | I2C host-control mode registers + standalone resistor-config mode |

## Magnetometer

| Part | File | Notes |
|---|---|---|
| RM3100 breakout board | `magnetometer/RM3100-Breakout-Board-User-Manual.md` | Board-level: pinout, connections, usage |
| RM3100/RM2100 sensor IC | `magnetometer/RM3100-RM2100-Magnetometer-User-Manual.md` | Full sensor reference: registers, cycle count, sample rate config |

*Note: `.docx` versions of both existed alongside the PDFs in the source; skipped as duplicates of the PDF content.*

## Display

| Part | File | Notes |
|---|---|---|
| Midas MDOB256064D1Y (OLED module) | `display/Midas-MDOB256064D1Y.md` | Module-level datasheet, pinout, mechanical |
| SSD1362 (OLED driver IC) | `display/SSD1362-controller.md` | Full command set / register reference for the driver chip on the module |

## 9-Axis IMU

| Part | File | Notes |
|---|---|---|
| ICM-20948 (9-axis IMU) | `9-axis/ICM-20948-datasheet.md` | Full register map across all 4 user banks (search `REG_BANK_SEL`, `WHO_AM_I`, etc.) |
| ICM-20948 eval board | `9-axis/ICM-20948-EVB-appnote.md` | Application note for the eval board variant |

## MRAM

| Part | File | Notes |
|---|---|---|
| EMxxLX MRAM | `mram/EMxxLX-MRAM-datasheet.md` | Non-volatile memory datasheet |

*Note: a `.docx` duplicate existed alongside the PDF; skipped.*

## Camera

| Part | File | Notes |
|---|---|---|
| ArduCAM Mini 2MP shield | `camera/ArduCAM-Mini-2MP-datasheet.md` | Shield-level datasheet |
| ArduCAM Mini 2MP shield | `camera/ArduCAM-Mini-2MP-appnote.md` | Hardware application note (wiring, setup) |
| OV2640 (image sensor IC on the ArduCAM shield) | `camera/OV2640-datasheet.md` | Sensor register reference |
| SCCB bus spec (OmniVision's I2C-like control bus) | `camera/OmniVision-SCCB-spec.md` | Protocol spec — needed to talk to the OV2640 registers |

## Gyroscope

| Part | File | Notes |
|---|---|---|
| SCH16T (6-axis inertial sensor) | `gyroscope/SCH16T-K01-datasheet-full.md` | Full datasheet, SPI register interface |
| SCH16T chip-carrier PCB | `gyroscope/SCH16T-PCB-specification.md` | Breakout board BOM/pinout for prototyping |
| SCH1000 series | `gyroscope/SCH1000-assembly-instructions.md` | Assembly instructions |
| SCH16T C code example | `gyroscope/sch16t-c-code-example/` | **Working STM32 (HAL) example project** — `code/main.c`, `hw.c`, register-level driver. Extracted as-is (not converted), since it's already source code. Start with `code/main.c` and `code/hw.c`. |

## UHF Radio

| Part | File | Notes |
|---|---|---|
| AT86RF215 (sub-GHz + 2.4 GHz IEEE 802.15.4 transceiver, 235 pages) | `uhf/AT86RF215-datasheet.md` | Full register map (search `RF09_`, `RF24_`, `BBC0_`, `RF_PN`), SPI protocol, state machine. The register summary is in chapter 8, page 181. |
| ATREB215-XPRO / XPRO-A extension board | `uhf/ATREB215-XPRO-user-guide.md` | Board level: Xplained Pro header pinout and SMA antenna connectors |

## MCU (SAMD51 / Cortex-M4)

| Doc | File | Notes |
|---|---|---|
| **SAMD51 family datasheet (2,130 pages)** | `mcu/samd51-chapters/` | **Split into 73 per-chapter files** — see `mcu/samd51-chapters/_INDEX.md` for the full chapter list with page ranges. Go straight to the peripheral you need (e.g. chapter 37 = SERCOM SPI, 38 = SERCOM I2C, 47 = ADC, 24 = DMAC). Do not load the whole thing. |
| ASF API Reference Manual (497 pages) | `mcu/ASF-API-Reference-Manual.md` | Atmel Software Framework driver API reference — function signatures/usage for the peripherals above |
| Cortex-M4 Generic User Guide (ARM DUI0553, 277 pages) | `mcu/Cortex-M4-Generic-User-Guide-DUI0553.md` | Core architecture reference: NVIC, SysTick, exceptions, instruction set |
| Arm Cortex-M4 Processor Datasheet | `mcu/Arm-Cortex-M4-Processor-Datasheet.md` | Shorter processor-level overview |
| Adafruit Grand Central M4 Express guide | `mcu/Adafruit-Grand-Central-M4-guide.md` | Board-level guide (pinouts, bootloader, board-specific notes) — likely the actual dev board in use |
| SAM D-series timer app note | `mcu/SAM-Various-Timers-appnote.md` | Focused app note on TC/TCC timer usage patterns |

## Suggested lookup order for a typical task

1. **"How do I drive peripheral X on the SAMD51?"** → `mcu/samd51-chapters/_INDEX.md` to find the chapter → read that chapter → cross-reference `mcu/ASF-API-Reference-Manual.md` for the driver function calls.
2. **"How do I talk to sensor Y over SPI/I2C?"** → the sensor's own datasheet (register map) + the relevant SAMD51 SERCOM chapter (37 for SPI, 38 for I2C) for the MCU side.
3. **Board-specific pin/bootloader questions** → `mcu/Adafruit-Grand-Central-M4-guide.md`.

## Conversion notes

- Source: `pdftotext -layout` (preserves column/table alignment as plain text) + `pdfplumber` table detection for clean cell-based tables (skipped on the 3 largest docs — SAMD51, ASF Reference, DUI0553 — where layout text alone is sufficient and full table detection would be slow for little gain).
- Every page break is marked `<!-- page N -->` referencing the *original* PDF's page number, so you can go back to the source PDF for figures/diagrams that don't survive text extraction (pinout diagrams, block diagrams, PCB layouts).
- Figures, schematics, and diagrams are **not** captured — text extraction is blind to them. If you need a diagram, open the source PDF page directly (page number is in the nearest `<!-- page N -->` marker).
