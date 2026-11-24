# Hardware documentation checklist

Applied by the `hardware-doc-reviewer` agent on every review. Grow it after each review (see `SKILL.md`, step 4).
Each check: what to compare, and where the truth lives.

## Sources of truth

- Wires, ends, lengths, build steps: `tools/boards.py` (board wires, nets, connectors) and `tools/harness.py`
  (`EXTRA` wires, `STEPS`, `PIGTAIL`, `TOL`).
- Nets: `tools/kicad_sch_gen.py` → `hardware/kicad/spit.kicad_sch`.
- Conventions: `CLAUDE.md` (*Hardware Conventions*, *Colour code*) and `hardware/design_notes.md` (*Colour code*).
- Values and limits: `requirements/*.md`; measured values: `hardware/measurements.md`.
- Parts in stock: `hardware/shopping_list.md`, *already in stock*.

## Documents in scope

`hardware/spit_harness.html` + `.pdf`, `hardware/spit_wiring.html` (+ its SVG), `hardware/kicad/spit_schematic.pdf`,
`hardware/design_notes.md` (*Wiring*, *Placement*, *Colour code*, boards, connectors), `hardware/bom.md`,
`hardware/shopping_list.md`, `hardware/power_budget.md`, `tests/bench/bring-up.md`, `tests/bench/*.md`,
README parts table.

## Checks

### Agreement with the sources
- Every wire of boards.py / harness.py appears in the guide with the same number, colour, rings, both ends and length.
- Every net named in a doc exists in the schematic with the same name; no doc names a net the schematic lacks.
- Module, board and connector names are the same in the guide, the diagram, the design notes and the BOM.
- A value quoted in a doc (voltage, resistor, current, length) matches its requirement or measurement, or the doc
  links to it instead of copying it (TECH-BUILD-DOCS-001: each fact written once).

### Wiring conventions
- Each wire end is typed soldered / Dupont / JST-XH (with F / M for connectors) and each wire has a length.
- Power pairs: red / black for battery and 5 V rails, white / blue for 3V3; blue never on a signal; no yellow 3V3.
- Red / black rails carry the band colour of their rail (none B±, white TP4056 OUT±, yellow VPATH, orange VSYS,
  purple VUSB) on both wires and both ends.
- 30 AWG signals use the role colour of the table and the ring count of their bus (none SPI/local, 1 I2S/PIR,
  2 I2C, 3 microSD).
- Resistors sit on the board or harness side, never at the LED or module.
- Charging goes through J1 in the left foot; the TP4056's own micro-USB is shown desoldered.

### Builder usability (a beginner follows it)
- Each build step states its first action, the tools and parts it needs, and ends with its bench test.
- Steps follow the bring-up order of `tests/bench/bring-up.md`; no step uses a wire or board not built yet.
- Every abbreviation and part code (P1, J1, W12…) is defined at first use or in a legend.
- Every link and cross-reference resolves (file exists, anchor exists).
- Safety notes (polarity, cell handling, fuse, hot plug) stand before the step that needs them.

### Diagrams and print output
- PDFs: no blank page, A4, text extractable (`pdftotext -layout`).
- Rendered pages (`pdftoppm -r 100`): labels readable at print size, no overlap, every symbol in the legend, wire
  colours tell apart in print.
- The HTML and its PDF tell the same thing (same step count, same wire count).
- Images carry no EXIF/GPS: `python3 ~/.claude/skills/hardware-change/scripts/strip_exif.py --check <paths>`.

### Language
- English everywhere in the docs; units with a space (`3.3 V`, `26 AWG`).

## Accepted exceptions

None yet. Format: `- <file / item>: <deviation> — <why it is intended> (<date>)`.
