<!-- @req PERF-POWER-RUNTIME-001 -->
# Bench test PERF-POWER-RUNTIME-001 — runtime on a full charge

Requirement: [PERF-POWER-RUNTIME-001](../../requirements/performance.md#perf-power-runtime-001). Manual test, run at bring-up step **3.9 and 5** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- Two cells of ≥ 2500 mAh rated capacity each.
- The firmware with the reference profile (Wi-Fi connected and idle, both screens at full backlight, no audio) and a log of its start and shutdown times.

## Setup
1. Cells charged until the charger ends the charge, external supply then unplugged.

## Steps
1. Start the robot with the reference profile; note the start time.
2. Let it run until the low-battery shutdown; read the shutdown time from the firmware log.

## Pass criteria
- Shutdown − start ≥ 20 h.

## Results
| Date | Commit / build | Start | Shutdown | Runtime | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
