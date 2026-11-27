<!-- @req PLAT-MECH-SDSLOT-001 -->
# Bench test PLAT-MECH-SDSLOT-001 — microSD breakout located by its grooves

Requirement: [PLAT-MECH-SDSLOT-001](../../requirements/platform.md#plat-mech-sdslot-001), parent
[TECH-MECH-MOUNT-001](../../requirements/technical.md#tech-mech-mount-001). The model part (side play asserts) is checked
by `tests/test_mechanical.py`; this sheet is the print part. Manual test, run on each newly printed left leg; add a line
to *Results* every time it is run.

## Equipment
- The printed left leg (or its top half), lid off.
- The microSD breakout (header removed, wires soldered or not).
- A caliper.

## Setup
1. Lay the leg front face down, open side up.

## Steps
1. Slide the breakout into its grooves from the lid side, socket towards the lid, until its front edge meets the stop.
2. Push it fully to the left, then fully to the right; measure the travel with the caliper.
3. Slide it out again.

## Pass criteria
- The board slides in and out without forcing.
- Total side travel ≤ 1 mm.
- The front edge rests against the stop.

## Results
| Date | Commit / build | Side travel (mm) | Slides freely | Pass | By | Notes |
|---|---|---|---|---|---|---|
