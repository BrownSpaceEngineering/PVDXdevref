# PVDX board designs

KiCad projects for the PVDX boards, copied from their BrownSpaceEngineering repos (not submodules).
The upstream repos are the source of truth for ongoing design work; re-copy to update.

KiCad lock files, `-backups/`, autosaves, `fp-info-cache`, `.kicad_prl`, and `.bak` files were left out.

| Folder | Upstream repo | Commit | Contents |
| --- | --- | --- | --- |
| `battery-board/` | [PVDX-Battery-Board](https://github.com/BrownSpaceEngineering/PVDX-Battery-Board) | `92fe52d` (2026-10-13) | Battery stack, heaters, thermistors; gerbers in `manufacturing/` |
| `compute-board/` | [PVDX-Compute-Board](https://github.com/BrownSpaceEngineering/PVDX-Compute-Board) | `c12a1c8` (2026-10-01) | SAMD51 compute board (2-layer `Compute Board/`, 4-layer `compute4layer/`), dev board, shared `Components/` |
| `solar-boards/` | [SolarBoards](https://github.com/BrownSpaceEngineering/SolarBoards) | `316883e` (2026-09-24) | Solar PCBs: `SolarPCB_Arm`, `SolarPCB_Long`, `SolarPCB_Short` with gerbers |
| `uhf-balun-board/` | [uhf-balun-board](https://github.com/BrownSpaceEngineering/uhf-balun-board) | `b9d6cff` (2026-09-22) | UHF balun board (newer revision, adds plated through-holes); gerbers in `gerbers/` |
| `balun-board/` | [balun-board](https://github.com/BrownSpaceEngineering/balun-board) | `164e4f9` (2026-09-16) | Earlier revision of the UHF balun board |
| `adcs-pmb/` | [PVDX-ADCS-PMB](https://github.com/BrownSpaceEngineering/PVDX-ADCS-PMB) | `089a12e` (2026-09-29) | ADCS + perovskite measurement board: photodiode amplifiers, magnetorquer drivers, perovskite pixel switching (`schematics/`); gerbers and plots in `manufacturing/` |
| `magnetorquer-board/` | [magnetorquer-board](https://github.com/BrownSpaceEngineering/magnetorquer-board) | `9018ce9` (2025-10-23) | Magnetorquer board |

Schematics are in `*.kicad_sch` files. These are plain-text S-expressions, so you can grep them for
symbol references, net labels, and part values.
