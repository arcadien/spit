# mech-collar-bore — collar bore on its own clearance (PLAT-MECH-COLLAR-001), stacked on audit-lotD

## Goal
The tube collar bore stops sharing the glued pivot clearance (8.00): printed flat, it is a vertical hole that prints
much smaller. Requirement = the principle (collar glued on each tube, bore sized for the print process); the values
live in `hardware/measurements.md`.

## State
- `test:` bench sheet `tests/bench/PLAT-MECH-COLLAR-001.md`; `req:` validated (2026-11-05); `feat:` `collar_clr` 0.32
  (Ø8.25, Ender 3 PETG, collars_petg 2026-11-05), `tube_collar()` uses it, model test in `tests/test_mechanical.py`,
  measurements row, README. `make check` clean.
- Stacked on audit-lotD because the parent FUNC-MECH-JOINT-001 is only there (audit D3).

- Requirements slimmed (2026-11-05, user: principle in requirements, values in a log): CONF-POWER-THRESH-001
  (defaults → design_notes.md *Battery thresholds*), FUNC-POWER-MONITOR-002 and FUNC-POWER-CUTOFF-002 (bounds from
  CONF, no duplicated values), PLAT-POWER-CHARGE-002 (R_PROG value and fallback → measurements.md / open_questions.md).
  Done here, not on a new branch: this branch had rewritten three of them (no clash; mech-collar-bore merges it).

## Open questions
| # | Question | Answer |
|---|---|---|
| MC-1 | Values in the requirement? | No: principle only, values and their justification in measurements.md (user, 2026-11-05) |
| MC-2 | PLAT-MECH-PIVOT-001 still carries its values (8.00 / 8.05, tube_test3): slim it the same way? | Yes, on this branch (user, 2026-11-05): principle only, test checks structure, values in measurements.md |

## Next
Bench sheet at bring-up step 4 (6 PETG collars Ø8.25 printed). Merge after audit-lotD.
