# Contributing

How to change SPIT by hand, without network access and without an AI assistant. Every step below runs offline once
the tools are installed.

## Tools

| Tool | Used for | Notes |
|---|---|---|
| OpenSCAD **2026.11-RC0** release candidate (`openscad`), pinned: [Linux AppImage](https://files.openscad.org/rc/OpenSCAD-2026.11-RC0-x86_64.AppImage), [Windows installer](https://files.openscad.org/rc/OpenSCAD-2026.11-RC0-x86-64-Installer.exe) | the model, STL export, renders | GUI for previewing, CLI for the scripts; the same version as CI (`.github/workflows/check.yml`): another version may export different geometry; on Windows `make check` finds it in `C:\Program Files\OpenSCAD (Nightly)` (or `OpenSCAD`) without any PATH change, and runs `openscad.com`, the console binary |
| Python 3 | `tools/*.py`, `scripts/*.py` | standard library only, except the two `uv` scripts below |
| `uv` | `scripts/check_renders.py` (Pillow), `scripts/overhang.py` (trimesh), the requirement tests `tests/` (`uvx pytest`, in the ERC stage) | downloads packages on the first run: run `make check` once **while online** to fill the cache, then work offline with `UV_OFFLINE=1` |
| Node.js (`node`) | `tools/wiring_svg.js` | static SVG of the wiring sketch |
| Firefox + Ghostscript (`gs`, or `gswin64c` on Windows) | printable wiring guide `hardware/spit_harness.pdf` | without Firefox the HTML guide is still written, not the PDF |
| KiCad 10: AppImage in `~/bin`, or `kicad-cli` on the PATH | schematic generation, ERC and the requirement tests (`erc` stage, every commit) | needed for every commit (pre-commit runs the `erc` stage); `KICAD=/path/to/kicad.AppImage` overrides; on Windows found in `C:\Program Files\KiCad\*in` |
| OrcaSlicer | slicing `mechanical/3mf/spit.3mf` | by hand, at the end |

## Workflow (RBD)

Every change starts from a requirement in `requirements/` (see the README, *Requirements*):

1. **Requirement**: write it (or find it), status `draft`; once agreed, set `**Status:** validated` and commit it alone
   as `req(<ID>): <title>`. References to other requirements are markdown links.
2. **Tests** where they apply (firmware: Unity, tag `// req: <ID>`; tools: pytest, `@pytest.mark.req('<ID>')`), commit
   `test(<ID>): …`.
3. **Change**, commit `<feat|tech|perf|ui|conf|fix>(<ID>): …`. Run `make hook` once: the `commit-msg` hook refuses a
   commit that touches `mechanical/` or `hardware/` without a validated requirement ID, the `pre-commit` hook runs
   the fast checks (model, ERC, docs: seconds), the `pre-push` hook the slow ones (STL export, renders, Orca project meshes). The CI job
   `check` (model, STL, ERC, docs) must pass before a pull request is merged into main.

Work on a branch; its state (goal, findings, its still-open questions, next step) lives in `status.md` at the repo root, read first
when the branch is picked up again and removed before the merge (main has none). A branch whose change still waits for a measurement (`MEASURE` value, bench check) is not merged
until the measurement is done and folded into the model or the requirement: the risk is still there.

A change in `mechanical/` or `hardware/` brings extra checks and updates in the same commit; the lists are in
`CLAUDE.md`, *Change workflow*. In short: `make check` clean, renders and
harness guide regenerated, schematic + ERC + board plans + wiring pages for electrical changes, and the README, `hardware/design_notes.md`, `hardware/bom.md`,
`hardware/power_budget.md`, `hardware/shopping_list.md`, `hardware/measurements.md`, `open_questions.md` kept in step.

## Validation stages

**Validation** (`make check`: every stage but meshes, overhang and orca). The git hooks, installed by `make hook`,
split it: **pre-commit** runs the fast stages (model, erc, docs), **pre-push** the slow ones (stl, renders, meshes); CI
(`check` job: model, stl, erc, docs, then a diff of the regenerated SVG / HTML) gates merges to main. **Incremental**:
each stage runs only when its input files changed since its last pass (a geometry change: ~9 min; a wire colour change:
the docs stage only, ~40 s; nothing changed: instant). `make check-all` forces every stage, `make check-<stage>` one
stage. Logs in `build/check/`.

| Stage | Runs when | What fails it |
|---|---|---|
| model | the `.scad` files change | `spit.scad` evaluated without export (seconds): any OpenSCAD `WARNING` / `ERROR`, the model's own geometry checks included |
| stl | the `.scad` files, `build4.sh`, `stl2_3mf.py` change, or the STLs on disk are not the last ones it exported (they are not in git) | any print part (Ender 3 halves, CR-10 one-piece, the `tube_test3` trial print) with an OpenSCAD `WARNING` / `ERROR`; a raw plate (written to `build/plates/`) off its bed (Ender 3 220 × 220, CR-10 300 × 300) |
| meshes | **pre-push** (`make check-meshes`, not part of `make check`), when the STLs or the Orca projects change | `tools/update_orca_project.py` on `mechanical/3mf/spit.3mf` and `spit_cr10.3mf`: meshes swapped for the current STLs, layout kept, backup in `backups/`; an up-to-date project is not rewritten; an object without its STL fails. The pre-push hook then refuses the push until the rewritten projects are committed |
| overhang | **only on request** (`make check-overhang`, not part of `make check`: overhangs are checked in Orca) | `scripts/overhang.py` (uv + trimesh): a region over 2 cm² facing down more than 50° from vertical, unless it is a ceiling narrower than 3 mm (bridge) or listed with its reason in `scripts/overhang_allow.json` (`--limit 45` for a stricter pass) |
| orca | **only on request** (`make check-orca`, not part of `make check`: needs the OrcaSlicer AppImage, Linux only) | `scripts/orca_check.py` refreshes the meshes of `mechanical/3mf/spit.3mf` (Ender 3) and `mechanical/3mf/spit_cr10.3mf` (CR-10) in place (layout kept, backup in `backups/`; same as `update_orca_project.py`), then the OrcaSlicer CLI (AppImage, no GUI) slices every plate: a part that grew off its plate or into its neighbour fails |
| erc | the KiCad files, `kicad_sch_gen.py`, the requirements, tests, test sheets or firmware sources change | `tools/kicad_sch_gen.py` regenerates the schematic and its PDF (fails when its netlist differs from the generator's nets); KiCad ERC through `kicad-cli`: any error (warnings are listed); the requirement acceptance tests (`uvx pytest tests`) |
| renders | `mechanical/scad/spit.scad`, `build4.sh`, the libraries change | `tools/build4.sh renders`: a PNG missing, not rewritten or blank |
| docs | `boards.py`, `harness.py`, `hardware/spit_wiring.html`, `wiring_svg.js` or `mechanical/scad/spit.scad` (wire lengths) change | `boards.py` (net checks), `wiring_svg.js`, `harness.py`: an output missing or not rewritten, a blank page in `hardware/spit_harness.pdf` |

The hooks also refuse a commit / push when the check rewrote tracked files (schematic, 3MF meshes, renders, guides):
add them and commit again (`git commit --no-verify` skips it).

## Mechanical

Everything that gets printed lives in `mechanical/`:

| Path | What | Who writes it |
|---|---|---|
| `mechanical/scad/spit.scad` | the model: every dimension is a named parameter at the top of the file | **you** |
| `mechanical/stl/` | one STL per part, in print orientation; **not in git**: `make check-stl` before a print | `tools/build4.sh stl` |
| `mechanical/3mf/spit.3mf` | **the Orca project** (plates arranged by hand, Ender 3) | Orca, then `tools/update_orca_project.py` |
| `mechanical/3mf/spit_cr10.3mf` | the CR-10 Orca project (one-piece parts) | Orca, then `tools/update_orca_project.py` |
| `mechanical/3mf/spit_plate*.3mf` | raw plates, starting point of a new Orca layout; **not in git** | `tools/build4.sh 3mf` |

### 1. Change the model

1. Open `mechanical/scad/spit.scad` in OpenSCAD. Change values in the parameter block at the top of the file, never
   numbers buried in a module. Values still marked `MEASURE` wait for a measurement (`hardware/measurements.md`).
2. Preview: set `part` (top of the file) to the part you are working on (`"col1"`, `"lid_mid"`, `"open"`…), F5. Set it
   back to its default before committing.
3. Render (F6) the parts you touched: an OpenSCAD `WARNING` (for instance `WARNING: connector …`) is a failed check,
   not a cosmetic message. The scripts below stop on any WARNING.

### 2. Regenerate what depends on it

The shortest path is the incremental check, which redoes only what changed:

```sh
cd spit                        # your clone of the repository
UV_OFFLINE=1 make check        # model → stl → erc → renders → docs (each only when its inputs changed)
```

It takes 5–10 min after a model change (STL export ~5 min, renders ~4 min). Logs: `build/check/<stage>.log`. To run
one step by hand instead:

| Command | Writes |
|---|---|
| `tools/build4.sh stl` | `mechanical/stl/spit_*.stl` (Ender 3 halves) |
| `tools/build4.sh cr10stl` | `mechanical/stl/spit_cr10_*.stl` (one-piece parts) |
| `tools/build4.sh tests` | trial print `tube_test3` (finished trials `pir_test`, `tube_test`, `tube_test2` stay in the model, export them one-off) |
| `openscad -D 'part="print_<part>"' -o <part>.stl mechanical/scad/spit.scad` | any other part, one-off (e.g. `test_level`, `test_screen`: kept in the model, no longer exported) |
| `tools/build4.sh renders` | `renders/*.png` (README pictures, connector details) |
| `python3 -I tools/harness.py` | `hardware/spit_harness.html` + `.pdf` (wire lengths are read from the model) |
| `tools/build4.sh 3mf` | raw plates in `mechanical/3mf/spit_plate*.3mf` (**not** the Orca projects) |

### 3. Update the Orca projects

The plates in `mechanical/3mf/spit.3mf` were arranged by hand: **never regenerate that file**, only swap its meshes.

1. Close the project in OrcaSlicer (if it stays open, saving from Orca later puts the old meshes back).
2. `python3 -I tools/update_orca_project.py mechanical/3mf/spit.3mf` — each object gets the STL of the same name,
   positions, rotations, plates and settings are kept; a copy of the old file goes to `backups/`. Add `--check` to
   only list what would change.
3. Same for the CR-10: `python3 -I tools/update_orca_project.py mechanical/3mf/spit_cr10.3mf`.
4. Reopen the project in Orca, check the plates (a part that grew may now overlap or leave the bed), slice.

The `pre-push` hook does steps 2 and 3 itself when the STLs changed (`meshes` stage) and refuses the push until the
rewritten projects are committed: close them in Orca first.

A **new** part has no object in the Orca project yet: import its STL in Orca by hand, place it, save.

### 4. Commit

```sh
git add -A
git commit -m "feat(MECH-…-001): …"   # validated requirement ID (commit-msg hook); pre-commit runs model, erc, docs
```

- The hook refuses the commit if the check fails, or if it rewrote tracked files (schematic, guide, board drawings; renders and Orca meshes at pre-push): `git add`
  them and commit again.
- STL files are not in git: `make check-stl` exports them before a print.
- Allowed commit prefixes (checked when pushing): `req`, `test`, `feat`, `tech`, `perf`, `ui`, `conf`, `arch`, `plan`,
  `chore`, `fix`, `docs`, `style`, `refactor`; `feat(ID):`-style prefixes need an existing requirement ID in
  `requirements/`.
- Offline, commits stay local: `git push` once the network is back.

### Pitfalls

- OpenSCAD 2021 writes one object per STL; the multi-object 3MF files come from `tools/stl2_3mf.py`.
- Tangent faces (two solids just touching) make non-manifold STLs: overlap them by 0.01 mm.
- `make check` never runs the Orca slicing or overhang checks: check overhangs in Orca's preview before printing.
