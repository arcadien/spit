<!-- @req PERF-POWER-OFF-001 -->
# Bench test PERF-POWER-OFF-001 — battery drain with the switch off

Requirement: [PERF-POWER-OFF-001](../../requirements/performance.md#perf-power-off-001). Manual test, run at bring-up step **3.9** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- A multimeter with a µA range.
- A warm room or an enclosure at 35 °C, a thermometer.

## Setup
1. Whole robot, cells in, SW1 off, no external supply.
2. Meter in series with B+, on the µA range.

## Steps
1. At room temperature: read the current.
2. At 35 °C (D1 only blocks on battery, when the charger is off and does not heat the leg): read the current after 30 min at that temperature.

## Pass criteria
- The current is ≤ 60 µA at both temperatures.

## Results
| Date | Commit / build | Room temperature | 35 °C | Pass | By | Notes |
|---|---|---|---|---|---|---|
