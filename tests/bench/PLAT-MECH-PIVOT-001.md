<!-- @req PLAT-MECH-PIVOT-001 -->
# Bench test PLAT-MECH-PIVOT-001 — first printed pivot joint: glued side holds, turning side turns

Requirement: [PLAT-MECH-PIVOT-001](../../requirements/platform.md#plat-mech-pivot-001). The model part (bore sizes,
teardrop bores, no WARNING) is checked by `tests/test_mechanical.py`; this sheet is the print part. Manual test, run at
bring-up step **4** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- Two printed neighbouring columns (first joint), the brass tube (7.93 measured) cut to length. With only one leg
  printed, its neighbour can be the trial piece `pivot_test<i>` (the top ~25 mm of the middle column, same bores and
  bearing ring, `tools/build4.sh tests`): `pivot_test1` next to the left leg (tube glued in the leg, turning in the
  piece), `pivot_test2` next to the right leg (tube glued in the piece, the leg turns). Hold the piece in the hand and
  take the force and the side play at the leg's foot.
- Epoxy or cyanoacrylate glue; an 8 mm drill bit to ream a bore that binds.
- The printed collar (`print_collar`), a strip of 80 g printer paper (~0.1 mm) as a shim.
- A protractor, a ruler, a kitchen scale or a luggage scale (5 N ≈ 510 g).

## Setup
1. Clean the bores of any stringing. Dry-fit the tube in both bores without glue.

## Steps
1. Glued side (8.00 teardrop): push the tube in. It must hold without play; glue it and let it cure.
2. Turning side (8.05 teardrop): slide the neighbouring column on and swing it ±45° ten times.
3. Collar: push the turning column against the glued one (bearing ring in contact), lay the paper strip against the
   inner face of the turning boss, slide the collar on the tube against the paper and glue it to the tube only (no
   glue on the paper or the boss). Once cured, tear the paper out.
4. Hold the glued column flat: push the turning one at its foot with the scale over ±45°, note the highest reading;
   push its foot sideways (along the tube) one way then the other, note the side play on the ruler (E-M11).

## Pass criteria
- Glued side: the tube holds before glue and does not turn once glued.
- Turning side: turns over ±45° under ≤ 5 N at the foot ([FUNC-MECH-JOINT-001](../../requirements/functional.md#func-mech-joint-001)). Over 5 N: ream the bore, or check that no glue reached the boss.
- Collar: the paper strip no longer slides between collar and boss (axial play ≤ 0.1 mm).
- Side play at the foot ≤ 2 mm (provisional), recorded: this first measurement tightens the bound (E-M11 in [open_questions.md](../../open_questions.md)).

## Results
| Date | Commit / build | Glued side | Turning side N / mm | Pass | By | Notes |
|---|---|---|---|---|---|---|
