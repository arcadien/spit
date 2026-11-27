<!-- @req PLAT-POWER-CHARGE-002 -->
# Bench test PLAT-POWER-CHARGE-002 — charge current set by R_PROG

Requirement: [PLAT-POWER-CHARGE-002](../../requirements/platform.md#plat-power-charge-002). Manual test, run at bring-up step **2 and 3.1** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- The TP4056 module, unpowered.
- A multimeter (V, Ω, and mA / 10 A ranges).
- One cell, rested at **3.5–3.7 V** (discharge it first if it is fuller: see [PERF-POWER-CHARGE-001](PERF-POWER-CHARGE-001.md), *Setup*). From there it stays in constant current (1 A) for more than 30 min, so the whole 15 min reading is at full current.
- A 5 V ≥ 2 A USB charger and a micro-USB cable.
- A thermometer: IR, thermocouple, or a 100 kΩ NTC thermistor (the 3D printer kind) read on the multimeter's Ω range (table in [PERF-POWER-THERMAL-001](PERF-POWER-THERMAL-001.md)).

## Setup
1. Module unpowered: measure R_PROG in place. The fitted value is in [measurements.md](../../hardware/measurements.md) (1.2 kΩ "122", factory).
2. Note the rested cell voltage (start voltage).
3. Cell on B+ / B−, the meter on its **10 A socket** (the mA socket fuse blows at 0.5 A) in series in B+: A socket on the module's B+, COM on the cell +.
4. NTC: pressed on the TP4056 chip with a strip of Kapton tape.

## Steps
1. Note R_PROG and the chip temperature before plugging (room temperature).
2. USB into the module; after 1 min, read the charge current.
3. Module in open air: read the chip temperature every 5 min up to **15 min**. Unplug at once if it reaches 80 °C (NTC ≤ 12.5 kΩ).

## Pass criteria
- R_PROG within ± 5 % of the recorded value (1.2 kΩ: 1.14–1.26 kΩ).
- Charge current 1200 / R_PROG ± 10 % (1.2 kΩ: 0.90–1.10 A).
- Chip < 60 °C at 15 min (NTC > 24.9 kΩ).

## Results
| Date | Commit / build | R_PROG | Start V | Current | Chip °C 5 / 10 / 15 min | Pass | By | Notes |
|---|---|---|---|---|---|---|---|---|
