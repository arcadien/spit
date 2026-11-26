<!-- @req FUNC-MECH-JOINT-001 -->
# Manual test FUNC-MECH-JOINT-001 — the columns turn on their joints

Requirement: [FUNC-MECH-JOINT-001](../../requirements/functional.md#func-mech-joint-001). Manual test on the first
assembled robot (harness fitted, lids on), then after any change to the joints or the tube routes; add a line to
*Results* every time it is run.

## Equipment
- The assembled robot, switched off, cells out.
- A multimeter (continuity), the wiring guide (`hardware/spit_harness.html`, housing pin-outs).
- A protractor (or a phone inclinometer app), a ruler, a kitchen scale or a luggage scale (5 N ≈ 510 g).
- A pencil: on the cloth, mark the aligned position and ±45° around the joint axis (foot ~230 mm below the pivot: ±45° ≈ 160 mm of arc each way).

## Setup
1. Robot lying on its back on a soft cloth, columns aligned.
2. Continuity check P1 / P2 → every housing (as in the harness guide's last step): note any open wire.

## Steps
1. For each of the three joints in turn, hold one column and:
   - push its neighbour at the foot with the scale pad, perpendicular to the column, from the aligned position to +45°
     and back to −45°; note the highest reading;
   - at 0° and at ±45°, push the foot sideways (along the pivot axis) one way then the other; the ruler at the foot
     gives the side play.
2. Turn each joint back and forth 20 times over ±45°.
3. Redo the continuity check of the setup.

## Pass criteria
- Step 1: every joint turns over ±45° under ≤ 5 N (≤ 510 g on the scale) at the foot, with ≤ 2 mm side play at the foot.
- Step 3: the same continuity as in the setup (no wire opened by the turns), no wire visibly pulled at a tube end.

## Results
| Date | Commit / build | Left joint N / mm | Middle joint N / mm | Right joint N / mm | Continuity after 20 turns | Pass | By | Notes |
|---|---|---|---|---|---|---|---|---|
