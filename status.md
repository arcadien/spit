# docs-tube-fitting — tube fitting in the wiring guide

## Goal
Add how the three pivot tubes are fitted (which column is fixed, which turns, glue, collar) to
`hardware/tars4_harness.html`, and fix the contradiction between the README assembly order (tubes glued first, harness
threaded bare) and the guide (tubes threaded on the bench, harness finished before fitting).

## State
- `tools/harness.py`: new *Joints* section (values from the model: tube cut 16.5, bores 8.00 / 8.05, collar 13 × 2,
  15° clicks), steps 2, 5, 6, 7 say which ends stay loose until their tube is fitted.
- Loose side per tube (from the harness wire ends): left tube = left leg (X13–X16 contacts out of their housings),
  middle tube = right middle (P2 solders, X4 / X5), right tube = right leg (X9, right cell pair).
- README: tube cut 16.5 mm (was ~20, the model gives 2 × 6.6 + 0.8 + 2 + 0.5), assembly order step 3 rewritten.

## Open questions
| # | Question | Answer |
|---|---|---|
| TF-1 | Tube order: README (tubes first) or guide (bench first)? | Guide: tube threaded bare on the bench, one side finished, bench test, then glue + collar, the other side finished in TARS (2026-11-03) |

## Next
First joint dry-fitted: check the detent clicks with the collar glued tight (walls flex ~0.5 mm), and that a few
contacts at a time pass the Ø8 bore. Then PR.
