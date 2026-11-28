# Hardware documentation review — 2026-11-28

First run of `/hardware-doc-review` (scope: all), on `doc-review-skill` merged with main (#26). Re-checked against
`audit-2026-11-24` (#28): every finding still holds there (finding 8's "R_PROG 2.4 k" example aside).
27 findings: 2 errors, 19 warnings, 6 nits. Decision: **fix** all but 12 (**accepted**, see the checklist).

| # | Sev. | Finding | Fix at | Decision |
|---|---|---|---|---|
| 1 | error | No polarity check of C1 before the step 3 power-up (nor C2 step 4, C10 / C12 step 6) | `tools/harness.py` STEPS | fix |
| 2 | error | First cell plugged (step 2) without "SW1 off, charger out" and without a cell polarity check | `tools/harness.py` STEPS[1], `page()` | fix |
| 3 | warning | Harness step order and tests differ from bring-up (3V3 before the TPS63020, FUSE / PATH / SWITCH sheets missing, no cross-links) | `tools/harness.py` STEPS end with links to bring-up steps and sheets (bring-up owns the test order); `bring-up.md` links the harness steps | fix |
| 4 | warning | bring-up 3.1 "its own micro-USB" (desoldered); design notes "stays unused" | `tests/bench/bring-up.md`, `hardware/design_notes.md` | fix |
| 5 | warning | Step 1 "slide them into X10, X12, X13 and X14": X16 missing | `tools/harness.py` STEPS[0] | fix |
| 6 | warning | Part codes undefined in the guide (F1 / F2 polyfuses and their place, D1, D3, C9, Q1, Q5, R_PROG, R5–R9, C4, C5, C7, DW01) | `tools/harness.py` parts legend | fix |
| 7 | warning | SD_CLK (W66) / SD GND (W69) twist not stated | `tools/harness.py` or `tools/boards.py` note | fix |
| 8 | warning | No tools / parts list per step | `tools/harness.py` STEPS field | fix |
| 9 | warning | Overlapping labels in the harness diagrams (p4, p8, p11, p29) | `tools/harness.py` diagram() | fix |
| 10 | warning | "fi" ligature lost in the PDF text | `tools/harness.py` CSS | fix |
| 11 | warning | Doc net names differ from the schematic (OUT+/OUTP, B+/BAT+, B−, VBAT/2, 3V3, SPK−), reconciled only by `boards.py` ALIAS | `tools/kicad_sch_gen.py` names, drop ALIAS | fix |
| 12 | warning | Schematic PDF one A2 page, unreadable on A4 | — | accepted |
| 13 | warning | Prose wire lengths about half the generated ones (C9 ~16 cm vs 33, C1 ~35 vs 72, microSD ~30 vs 55–58) | `design_notes.md`, `spit_wiring.html`, HOTPLUG sheet; TECH-POWER-HOTPLUG-001 (req) | fix (link the harness table) |
| 14 | warning | Wire totals copied and stale (30 AWG 20.3 vs 20.98 m, red 2.0 vs 1.83 m) | `bom.md`, `shopping_list.md`, `design_notes.md` | fix (link the totals) |
| 15 | warning | F1 / F2 drawn flat on the top shelf | `hardware/spit_wiring.html` | fix |
| 16 | warning | Left tube "12" wires in the drawing (14) | `hardware/spit_wiring.html` | fix |
| 17 | warning | Wiring sketch: no end types or lengths, no link to the harness guide | `hardware/spit_wiring.html` | fix (link; sketch is an overview) |
| 18 | warning | Dead link `renders/spit_column_sections.svg` | `hardware/spit_wiring.html` | fix |
| 19 | warning | USB_DET described as the S3's PC USB | `hardware/spit_wiring.html` | fix |
| 20 | warning | power_budget plain-text references (checklist 3.1, E-M2, E-M3/5/7) and a README citation that no longer exists | `hardware/power_budget.md` | fix |
| 21 | warning | French column titles in the wiring drawing | `hardware/spit_wiring.html` | fix |
| 22 | nit | Decimal commas and French words ("3,3 V", "R_PROG 1,2k", "inter.", "case") | `spit_wiring.html`, `kicad_sch_gen.py`, `harness.py` | fix |
| 23 | nit | AM312 Ø10 (11.5), "X10–X14", tube fill 37 % (38) | `hardware/spit_wiring.html` | fix |
| 24 | nit | Legend XHF entry misses X16 | `tools/harness.py` | fix |
| 25 | nit | Near-empty page 2, orphan heading page 5 | `tools/harness.py` print CSS | fix |
| 26 | nit | Diagram split threshold "7 pt" (6.5) | `hardware/design_notes.md` | fix |
| 27 | nit | Test load 3.9 Ω "5 W" in PLAT-POWER-SWITCH-001, "≥ 10 W" in the sheets | `requirements/platform.md` (req) | fix (≥ 10 W) |

Fixes go on a branch from main once #28 is merged (it touches the same files).

## Tooling to add (so the next review does not find these again)

Automated checks in `tests/` (pytest), each under a requirement:
- net names cited in the docs exist in the schematic (11);
- wire lengths and totals quoted in prose match `harness.py` (13, 14), or the prose links instead;
- every relative link and cited path resolves; E-Mx / bring-up references are links (18, 20);
- label overlap in the harness diagrams (9);
- no French words or decimal commas in the doc sources and generated drawings (21, 22);
- each harness step links to existing bring-up steps and bench sheets (3).
