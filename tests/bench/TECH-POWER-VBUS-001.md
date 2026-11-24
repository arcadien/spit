<!-- @req TECH-POWER-VBUS-001 -->
# Bench test TECH-POWER-VBUS-001 — a USB host powers only the controller

Requirement: [TECH-POWER-VBUS-001](../../requirements/technical.md#tech-power-vbus-001). Manual test, run at bring-up step **3.7** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- A PC with a USB-C cable to the S3 Mini.
- A multimeter (V range, and µA / mA ranges for currents).

## Setup
1. Whole power block and S3 Mini wired (step 3.7).

## Steps
1. Cells out, no external supply, SW1 on, PC on and plugged into the S3: read VSYS.
2. Cells in, SW1 on, PC off with the cable still plugged in: meter on mA in series with B+, read the current with the cable in, then with it out; the difference is the current into the host's VBUS.
3. PC on: flash the firmware with SW1 on, then with SW1 off.

## Pass criteria
- Step 1: VSYS < 0.1 V.
- Step 2: current into the host's VBUS ≤ 1 mA.
- Step 3: flashing succeeds in both switch positions.

## Results
| Date | Commit / build | VSYS (host only) | Back-leak | Flashing on / off | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
