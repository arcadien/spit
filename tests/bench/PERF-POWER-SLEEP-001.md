<!-- @req PERF-POWER-SLEEP-001 -->
# Bench test PERF-POWER-SLEEP-001 — deep-sleep current from the battery

Requirement: [PERF-POWER-SLEEP-001](../../requirements/performance.md#perf-power-sleep-001). Manual test, run at bring-up step **3.9** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- A multimeter with a µA range.
- The firmware with its deep-sleep entry (every wake source armed, card supply cut).

## Setup
1. Whole robot, cells in, SW1 on, no external supply.
2. Meter in series with B+, on the mA range while awake (the wake-up current through a µA shunt can reset the controller).

## Steps
1. Let the firmware go to deep sleep; switch the meter to the µA range.
2. Read the current 60 s after the controller has gone to sleep.

## Pass criteria
- The current is ≤ 0.65 mA.

## Results
| Date | Commit / build | Sleep current | Pass | By | Notes |
|---|---|---|---|---|---|
