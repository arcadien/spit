<!-- @req PERF-POWER-MONITOR-001 -->
# Bench test PERF-POWER-MONITOR-001 — calibrated battery voltage reading

Requirement: [PERF-POWER-MONITOR-001](../../requirements/performance.md#perf-power-monitor-001). Manual test, run at bring-up step **3.7 and 5** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- An adjustable bench supply in place of the cells.
- A multimeter (V range).
- The firmware reporting the battery voltage (serial log), calibrated as in [CONF-POWER-ADCCAL-001](../../requirements/configuration.md#conf-power-adccal-001).

## Setup
1. Bench supply on B+ / B− in place of the cells, SW1 on, firmware running.

## Steps
1. Set the supply to 3.0 V. Read B+ with the multimeter, and the reported value as the mean of 16 samples.
2. Repeat at 3.3, 3.7 and 4.2 V.

## Pass criteria
- At every voltage, the reported value is within ±3 % of the multimeter reading.

## Results
| Date | Commit / build | 3.0 V | 3.3 V | 3.7 V | 4.2 V | Pass | By | Notes |
|---|---|---|---|---|---|---|---|---|
