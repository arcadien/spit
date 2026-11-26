# Bench test PLAT-MECH-CONTACT-001 — cell contact plates held without glue

Requirement: [PLAT-MECH-CONTACT-001](../../requirements/platform.md#plat-mech-contact-001). The model part (measured
plate, guide height, tab clearance) is checked by `tests/test_mechanical.py`; this sheet is the print part. Manual
test, run at bring-up step **4** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- A printed leg (bottom half) with both contact shelves.
- Its − (spring) and + (button) plates, wires soldered on the tabs.
- A charged 18650 cell; the leg's lid and screws.

## Setup
1. Lay the leg on its front face, lid off.

## Steps
1. Slide each plate in from the back, tab first, between its side rails, wire fed through the slot; let go.
2. Insert the cell − end first, pushing the spring down, then tilt it in.
3. Screw the lid on, stand the leg upright, shake it gently; take the lid off and look at the plates.

## Pass criteria
- Each plate slides in without forcing and drops against its two front stops by itself; its tab passes between them.
- With the cell in, both plates lie flat on their shelves, centred on the cell, nothing glued.
- After shaking, the plates have not moved and the cell voltage reads at the wires.

## Results
| Date | Commit / build | Leg | Plates drop in | Plates in place after shaking | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
