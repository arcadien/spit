# Branch `audit-2026-11-24`

**Goal:** resolve the 20 findings of the full RBD audit `audits/2026-11-24-audit.md` (fix or exclude each).

**State:** fixed: 8 (Given / When / Then markers), 20 (board score ceilings stated, commit 757b539), 19 (joints ±45°, ≤ 5 N at the foot, minimal side play with the collar glued against the boss, ≤ 2 mm provisional until E-M11 tightens it; AN1 answered), 18 (VSENSE falling edge timed from the rail crossing 2.3 V), 17 (factory R_PROG 1.2 kΩ, 1 A, kept until the wall test of E-M8; charge ≤ 8 h), 15, 16 (threshold defaults in CONF-POWER-THRESH-001, referred to by name), 14 (SWITCH-002 refers to PATH-001 for the running robot), 13 (pending notes moved to open_questions.md), 12 (Acceptance sentences out of the requirements, their limits kept, procedures in
bench sheets and tests), 1 (PLAT-POWER-CHARGE-001 points to PLAT-MECH-CHARGEPORT-001 for the port position), 3 (manual
sheets moved to tests/bench/), 4 (every bench sheet tagged, tag asserted by the sheet test), 9 (`accepted_prefixes` for
requirements/*.md); excluded: 5
(AUDIT-META-TESTS-001, meta tests of the RBD process kept), 6 (AUDIT-PRE-RBD-IMPL-001, design of the initial
snapshot), 7 (AUDIT-NO-TEST-COMMIT-001, tests inside req commits), 10 (AUDIT-REQ-FILE-COMMITS-001, published
format / path commits), 11 (AUDIT-NO-ARCHITECTURE-001, no firmware on main yet:
temporary), 2 (COVERAGE-FIRMWARE-001, the firmware requirements: warned until the first Unity
test, due after); open: none.

**Findings:** pushes are refused by the RBD plugin hook while the latest audit has open findings.

**Open questions:** none of its own. Blocked before merge by E-M11 (side play measured on the current leg).

**Next step:** push `audit-2026-11-24` and `doc-review-skill`; measure E-M11 with the `pivot_test<i>` trial piece and the printed leg; merge only after E-M11.
