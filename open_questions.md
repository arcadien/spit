# TARS4 — open questions

Only what is still open. A question leaves this file once answered: its answer goes into the document it changes
(`hardware/measurements.md`, a requirement, the model, the README…); history stays in git and `reviews/`.
A branch's own questions live in its `status.md`; a branch blocked by an item here names its ID.

## Questions

| # | Question | What the answer changes | Blocks |
|---|---|---|---|
| E-M8 | **TP4056 temperature** (PLA legs): leg wall after 15 and 30 min of charge | > 45 °C → R_PROG 3.6 kΩ (330 mA) or the lower left leg in PETG; still too hot: a switching charger (TP5100 1 A + separate DW01; IP2312 does not fit flat, 34.4 × 15). Copper RPi heatsink ≤ ~3 mm + 0.5–1 mm thermal pad between chip and heatsink, never between board and PLA. R_PROG row of `hardware/measurements.md` | PLAT-POWER-CHARGE-002 |
| RF1 | **Rename `usbb` → `usb_charging_socket`** in `mechanical/scad/tars4.scad` (J1 in the schematic) | separate `refactor` commit: the `usbb*` parameters, the `usbb_z0` / `usbb_y0` geometry keys of `tools/harness.py`, `hardware/measurements.md` | — |
| D-M9 | Actual position of the S3's first pin row (8.8 mm from the USB edge per the LOLIN drawing) | carrier cut margins (`my0` in `tools/boards.py`) | — |
| AN1 | Wanted swing angle for the legs | free wire length at the twist | — |

## Measurements

Dimensions go into `hardware/measurements.md`, bench results into the bench sheet named by the requirement (bring-up
order in `tests/bench/bring-up.md`, currents in `hardware/power_budget.md`).

| # | Measurement | Blocks |
|---|---|---|
| `bk_h` | TPS63020 inductor height | — |
| `pir_pcb_dn` | AM312 board mid-plane offset from the detector axis | — |
| SC1 | Screen active area checked lit (`active_dz`, `active_dx`) | — |
| ST1 | Solder tails on the wall side (ADXL345, MAX98357A, micro-USB), ≤ 1 mm | — |
| E-M1 | SD pull-up of the amplifier (R18) | measured on branch `mech-audio` (36 mV, pass): closes with it |
| E-M2 | Screens' BLK current and pull-up | — |
| E-M3 | D1 leakage when warm | — |
| E-M4 | AM312 high level | — |
| E-M5 | DW01 wake-up | — |
| E-M6 | SW1 rating (marking, ≥ 2 A) | PLAT-POWER-SWITCH-001, branch `mech-audio` |
| E-M7 | Sleep current with and without the microSD card | — |
| AU1 | Firmware volume cap: VSYS ≥ 3.0 V at the amplifier with the pack at 3.30 V | PERF-AUDIO-PEAK-001, branch `mech-audio` |
