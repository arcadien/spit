<!-- @req PLAT-MECH-LIDSTOP-001 -->
# Bench test PLAT-MECH-LIDSTOP-001 — lids stiff between their supports

Requirement: [PLAT-MECH-LIDSTOP-001](../../requirements/platform.md#plat-mech-lidstop-001), parent
[TECH-MECH-LID-001](../../requirements/technical.md#tech-mech-lid-001). The model part (stop asserts, lid span) is
checked by `tests/test_mechanical.py`; this sheet is the print part. Manual test, run on each newly printed column and its
lid; add a line to *Results* every time it is run.

## Equipment
- A printed column and its lid, lid screws, its boards in place (controller, distribution board, screen, flat boards).
- For comparison, if still at hand: the left leg printed on 2026-11-21 (no stops).

## Setup
1. Screw the lid on (all screws).

## Steps
1. Press firmly with a thumb on the lid at every stop (pairs of side stops, see `lid_stops` in the model).
2. Press halfway between each pair of neighbouring supports (screw rows, stops, boards under the lid).

## Pass criteria
- No visible flex of the lid at any spot.
- The lid sits flat on both stops (no rocking when pressed on one edge).

## Results
| Date | Commit / build | Column | At the stops | Between supports | Pass | By | Notes |
|---|---|---|---|---|---|---|---|
