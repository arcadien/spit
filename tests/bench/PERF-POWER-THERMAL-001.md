<!-- @req PERF-POWER-THERMAL-001 -->
# Bench test PERF-POWER-THERMAL-001 — leg wall temperature while charging (E-M8)

Requirement: [PERF-POWER-THERMAL-001](../../requirements/performance.md#perf-power-thermal-001). Manual test, run at bring-up step **3.9** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- The assembled leg (or robot), lids closed, both cells in.
- A multimeter (V and Ω ranges).
- A thermometer: thermocouple, IR, or a **100 kΩ NTC thermistor** (the 3D printer kind, B ≈ 3950) read on the Ω range. Check it first: ~100 kΩ at 25 °C.

  | °C | 25 | 30 | 35 | 40 | **45** | 50 | **55** | 60 |
  |---|---|---|---|---|---|---|---|---|
  | NTC kΩ | 100 | 80.4 | 65.1 | 53.0 | **43.5** | 35.9 | **29.8** | 24.9 |

- A 5 V ≥ 2 A USB charger and a micro-USB cable.
- A 4.7 Ω ≥ 10 W resistor (≈ 1 A on VSYS on mains, ~4.6 V) with crocodile leads, for case B.
- A room at 20–25 °C.

## Setup
1. Find the spot on the outer wall of the left leg right next to the TP4056; mark it with a pencil. NTC: taped flat on the mark with Kapton tape, a square of folded paper over it so the room air does not cool it.
2. **Start voltage**: discharge the pack to 3.30 V under load (see [PERF-POWER-CHARGE-001](PERF-POWER-CHARGE-001.md), *Setup*), then let it rest 30 min: B+ rested **3.4–3.6 V**, noted in *Results*. From there a 2 × 2500 mAh pack stays in constant current (full charge current, the hottest phase) for over 3 h at 1 A, so the whole test runs at full current. A fuller pack (> 3.8 V rested) gives too low a reading.
3. The leg at room temperature (wall = room ± 1 °C) before each case.

## Steps
1. Case A, robot off: plug the charger; read the wall temperature every 5 min for **30 min** (0, 5 … 30). Keep reading every 10 min up to 60 min if it still rises by more than 1 °C per 10 min at 30 min (plateau, noted only).
2. **Stop at once** and unplug if the wall reaches **55 °C** (NTC ≤ 29.8 kΩ): PLA softens above it.
3. Let it cool to room temperature, discharge again to the start voltage.
4. Case B, robot on with the 4.7 Ω load on VSYS (≈ 1 A on the external supply): same readings and stop rule.

## Pass criteria
- Every reading over the 30 min ≤ 45 °C (NTC ≥ 43.5 kΩ). Above: E-M8 ([open_questions.md](../../open_questions.md)) gives the next R_PROG, then run again.

## Results
| Date | Commit / build | R_PROG | Start V | A 15 / 30 min | B 15 / 30 min | Room | Pass | By | Notes |
|---|---|---|---|---|---|---|---|---|---|
