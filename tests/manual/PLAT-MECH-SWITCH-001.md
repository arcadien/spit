# Manual test PLAT-MECH-SWITCH-001 — SW1 screwed under the left-leg floor

Requirement: [PLAT-MECH-SWITCH-001](../../requirements/platform.md#plat-mech-switch-001). The slot size and the lever
recess are checked by `tests/test_mechanical.py` once the model carries the switch; this sheet is the print check.
Run it on the first print of the left leg's floor, then after any change to the switch housing; add a line to
*Results* every time it is run.

## Equipment
- The printed left-leg bottom half, the TC-R13-603C-05 switch, its two screws, a small screwdriver.
- A ruler or calliper.

## Setup
1. Clean the slot and the two screw holes (no stringing, no elephant foot on the slot edges).

## Steps
1. Put the switch in its housing from inside the leg, flange against the floor, and screw it.
2. From below, slide the lever end to end 10 times with a fingertip (or a pen tip).
3. Lay the leg on a flat table, floor down: check the lever does not touch the table.

## Pass criteria
- Step 1: the switch seats flat, both screws bite, no crack around the holes.
- Step 2: the lever reaches both positions (continuity meter: 1–2 then 2–3) without binding on the slot ends.
- Step 3: the lever stays recessed above the table in both positions.

## Results
| Date | Commit / build | Seats / screws | Full travel | Recessed | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
