<!-- @req PLAT-MECH-PIVOT-001 -->
# Bench test PLAT-MECH-PIVOT-001 — first printed pivot joint: glued side holds, turning side turns

Requirement: [PLAT-MECH-PIVOT-001](../../requirements/platform.md#plat-mech-pivot-001). The model part (bore sizes,
teardrop bores, no WARNING) is checked by `tests/test_mechanical.py`; this sheet is the print part. Manual test, run at
bring-up step **4** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- Two printed neighbouring columns (first joint), the brass tube (7.93 measured) cut to length.
- Epoxy or cyanoacrylate glue; an 8 mm drill bit to ream a bore that binds.
- A protractor, a ruler, a kitchen scale or a luggage scale (5 N ≈ 510 g).

## Setup
1. Clean the bores of any stringing. Dry-fit the tube in both bores without glue.

## Steps
1. Glued side (8.00 teardrop): push the tube in. It must hold without play; glue it and let it cure.
2. Turning side (8.05 teardrop): slide the neighbouring column on and swing it ±45° ten times.
3. Hold the glued column flat: push the turning one at its foot with the scale over ±45°, note the highest reading;
   push its foot sideways (along the tube) one way then the other, note the side play on the ruler.

## Pass criteria
- Glued side: the tube holds before glue and does not turn once glued.
- Turning side: turns over ±45° under ≤ 5 N at the foot, side play ≤ 2 mm at the foot ([FUNC-MECH-JOINT-001](../../requirements/functional.md#func-mech-joint-001)). Over 5 N: ream; over 2 mm: the bore is too loose, reprint the turning side tighter (8.02–8.03).

## Results
| Date | Commit / build | Glued side | Turning side N / mm | Pass | By | Notes |
|---|---|---|---|---|---|---|
