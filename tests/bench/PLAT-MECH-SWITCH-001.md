# Bench test PLAT-MECH-SWITCH-001 — power switch on its floor pad in the printed left leg

Requirement: [PLAT-MECH-SWITCH-001](../../requirements/platform.md#plat-mech-switch-001). The model part (measured
parameters, pins, offset, clearance asserts) is checked by `tests/test_mechanical.py`; this sheet is the print part.
Manual test, run at bring-up step **4** ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run.

## Equipment
- The printed left leg (bottom half).
- SW1 (TC-R13-603C-05), wires soldered.
- A ballpoint pen; glue (cyanoacrylate or hot glue).

## Setup
1. Dry fit: lay SW1 lever down on the floor pad, its two ear holes over the two pins, the lever in the floor slot.

## Steps
1. With the switch dry fitted, push the lever from under the leg with the pen tip to both ends of its travel.
2. Lift the switch, put a little glue on the pad around the slot (not in it), put it back on the pins and press it
   down until the glue holds.
3. Once the glue is set, flip the lever again with the pen tip, 5 times each way; wiggle the switch body.

## Pass criteria
- The pins go through both ear holes and the plate lies flat on the pad.
- The lever slides freely over its whole travel; on and off are both reached with the pen tip from under the leg.
- Nothing sticks out under the leg.
- Once glued, the body has no play and no glue has reached the lever.

## Results
| Date | Commit / build | Pins fit | Lever on / off with the pen | Body play | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
