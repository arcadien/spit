# Branch `audit-2026-11-24`

**Goal:** resolve the 20 findings of the full RBD audit `audits/2026-11-24-audit.md` (fix or exclude each).

**State:** fixed: 1 (PLAT-POWER-CHARGE-001 points to PLAT-MECH-CHARGEPORT-001 for the port position), 3 (manual
sheets moved to tests/bench/), 4 (every bench sheet tagged, tag asserted by the sheet test), 9 (`accepted_prefixes` for
requirements/*.md); excluded: 5
(AUDIT-META-TESTS-001, meta tests of the RBD process kept), 6 (AUDIT-PRE-RBD-IMPL-001, design of the initial
snapshot), 7 (AUDIT-NO-TEST-COMMIT-001, tests inside req commits), 10 (AUDIT-REQ-FILE-COMMITS-001, published
format / path commits), 11 (AUDIT-NO-ARCHITECTURE-001, no firmware on main yet:
temporary); open: 2, 8, 12–20.

**Findings:** pushes are refused by the RBD plugin hook while the latest audit has open findings.

**Open questions:** none.

**Next step:** decide fix or exclude for 12.
