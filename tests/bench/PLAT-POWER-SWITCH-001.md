<!-- @req PLAT-POWER-SWITCH-001 -->
# Bench test PLAT-POWER-SWITCH-001 — SW1 rating and heating at 1 A

Requirement: [PLAT-POWER-SWITCH-001](../../requirements/platform.md#plat-power-switch-001). Manual test, run at bring-up step **1 and 3.2** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- A bench supply, 3.7 V, current limit raised to 1.5 A.
- A 3.9 Ω ≥ 10 W load resistor (≈ 1 A at 3.7 V).
- A thermocouple or an IR thermometer.
- A multimeter (V range, and 10 A range).

## Setup
1. Before assembly: read the rating of SW1 on its datasheet or its marking.
2. Power path wired (step 3.2), bench supply in place of the cells, the 3.9 Ω load on VSYS / GND, SW1 on.

## Steps
1. Read the SW1 body temperature, switch the supply on.
2. After 10 min at ≈ 1 A, read the SW1 body temperature again.

## Pass criteria
- Setup 1: contacts rated ≥ 1 A.
- Step 2: the temperature rise of SW1 is ≤ 10 °C.

## Results
| Date | Commit / build | Rating | Rise after 10 min | Pass | By | Notes |
|---|---|---|---|---|---|---|
