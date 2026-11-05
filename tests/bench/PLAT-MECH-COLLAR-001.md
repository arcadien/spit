# Bench test PLAT-MECH-COLLAR-001 — printed collar: on by hand up to the boss, glued joint holds axially

Requirement: [PLAT-MECH-COLLAR-001](../../requirements/platform.md#plat-mech-collar-001). The model part (the collar
bore is a parameter of its own, no WARNING) is checked by `tests/test_mechanical.py`; this sheet is the print part.
Manual test, run with the first joint (bring-up step **4**, [bring-up.md](bring-up.md)); add a line to *Results*
every time it is run. The bore calibrated for the printer / filament used is in
[measurements.md](../../hardware/measurements.md) (*Brass tube*, collar row).

## Equipment
- The collars printed flat with the calibrated bore, on the printer and filament the calibration was made on.
- The first joint: two neighbouring columns, the brass tube glued in the fixed column (PLAT-MECH-PIVOT-001).
- Slow epoxy, a toothpick.

## Setup
1. Clean the collar bore of any stringing. Columns side by side, the bearing ring against the dimpled face.

## Steps
1. Push the collar along the tube by hand up to the turning column's boss. Note the force (slides / tight / forced).
2. With the collar against the boss, try to tilt it on the tube.
3. Columns pressed together, epoxy between collar and tube, then a bead behind the collar; none on the boss. Cure.
4. Swing the turning column ten times through its travel, then pull it sideways away from the fixed column.

## Pass criteria
- The collar reaches the boss by hand, without a tool, and does not tilt on the tube.
- After gluing: the joint turns, and the turning column does not move along the tube when pulled.

## Results
| Date | Commit / build | Printer / filament / bore | Fit by hand | Holds axially, turns | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
