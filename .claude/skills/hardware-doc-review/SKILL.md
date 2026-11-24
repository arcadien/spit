---
name: hardware-doc-review
description: Review the builder-facing hardware documentation of SPIT (wiring guide, harness PDF, wiring diagram, design notes wiring chapters, BOM, shopping list, bring-up and bench sheets) against its generators and the repo conventions. Read-only; dispatches the hardware-doc-reviewer agent and walks the findings with the user. Use for /hardware-doc-review, "review the wiring doc", "check the harness guide", "review the hardware docs".
argument-hint: "[all | <doc path> … ]  (default: all)"
---

# Hardware documentation review

Scope: **$ARGUMENTS** (empty means `all`).

This skill is **read-only**: it never edits docs, generators or requirements. Fixes go through the normal RBD
workflow afterwards, with the user.

## 1. Dispatch

Launch the `hardware-doc-reviewer` agent (`.claude/agents/hardware-doc-reviewer.md`) with:
- the scope above;
- the path of `checklist.md` next to this file (the agent applies every check in it and every accepted exception);
- a scratch directory for page renders (the session scratchpad).

Only one agent: a review needs the whole picture (one wire is in boards.py, the guide, the diagram and the BOM).

## 2. Report

Show the agent's table as is, then a two-line summary in French: number of findings per severity, and the
generator most findings point to. The fix location is the **source** (`tools/harness.py`, `tools/boards.py`,
`tools/wiring_svg.js`, `tools/kicad_sch_gen.py`, a markdown doc), never a generated file.

## 3. Process findings with the user

For each finding, in order: explain it in one or two sentences, then let the user choose:
- **Fix**: done later, through RBD (`docs:` for a markdown-only fix, a requirement-tagged commit for anything in
  `hardware/` or a generator). Do not start it without the user's go.
- **Accepted**: the deviation is intentional. Add it to *Accepted exceptions* in `checklist.md` (what, where, why),
  so the next review does not report it again.
- **False positive**: the check is wrong or too broad. Sharpen the check in `checklist.md`.

## 4. Grow the checklist

The checklist is the memory of this skill. After a review, add to `checklist.md`:
- a check for any defect the user found that the agent missed;
- the sharpened wording of a check that gave a false positive;
- the exceptions accepted in step 3.

Keep one line per check, grouped by concern; a check names what to compare and where the truth lives. Committing it
is a `chore:` change (outside `mechanical/` and `hardware/`).
