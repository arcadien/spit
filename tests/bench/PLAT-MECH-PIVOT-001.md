# Bench test PLAT-MECH-PIVOT-001 — first printed pivot joint: glued side holds, turning side turns

Requirement: [PLAT-MECH-PIVOT-001](../../requirements/platform.md#plat-mech-pivot-001). The model part (bore sizes,
teardrop bores, no WARNING) is checked by `tests/test_mechanical.py`; this sheet is the print part. Manual test, run at
bring-up step **4** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- Two printed neighbouring columns (first joint), the brass tube cut to length (its measured Ø and the calibrated clearances: [measurements.md](../../hardware/measurements.md), *Brass tube*).
- Epoxy or cyanoacrylate glue; an 8 mm drill bit to ream a bore that binds.

## Setup
1. Clean the bores of any stringing. Dry-fit the tube in both bores without glue.

## Steps
1. Glued side (teardrop, `tube_od + tube_glue_clr`): push the tube in. It must hold without play; glue it and let it cure.
2. Turning side (teardrop, `tube_od + tube_run_clr`): slide the neighbouring column on and swing it through its full travel ten times.
3. Hold the glued column and try to wobble the turning one sideways.

## Pass criteria
- Glued side: the tube holds before glue and does not turn once glued.
- Turning side: turns freely over the whole travel, without wobble (micro play only).

## Results
| Date | Commit / build | Glued side | Turning side | Pass | By | Notes |
|---|---|---|---|---|---|---|
