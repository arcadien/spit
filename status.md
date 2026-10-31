# audit-lot3 — build pipeline (audit 2026-10-29, lot C)

## Goal
Fix the build-pipeline findings C1–C10 of `audits/2026-10-29-audit-full.md`, one commit each.

## State
- Done: C1 (stl digest includes its STLs), C3 (CI diffs the SVG / HTML outputs), C5 (meshes fails on an object
  without STL), C9 (erc inputs: firmware sources, .gitignore), C7 (harness PDF through Ghostscript only, deterministic,
  3 portrait pages on Windows too), C2 (erc regenerates the schematic; generator fails on mismatch / no KiCad, exports
  the PDF).
- Not pushed: GitHub SSH unreachable on 2026-10-31 (also `mech-chargeport-front`, `audit-lot2` PR not opened).

## Open questions
| # | Question | Answer |
|---|---|---|
| L3-1 | C6: tube_section.py hard-codes stale wire lists. Derive them from harness.py (tube routes), or drop the tube / column section SVGs? | |

## Next
C4 (hooks: content hashes, dirty-input guard), C8 (commit-prefix check on push), C10 (labels, shared part ↔ STL
mapping, overhang_allow.json), C6 once L3-1 is answered.
