# Branch mech-audio — speaker and amplifier housing

Branch state file (CLAUDE.md, *Branches*): read it first when the branch is picked up again, keep it
current, answer the questions here.

## Goal
Fit the speaker and the I2S amplifier actually bought into the right middle column (column 2), and write the AUDIO /
MECH requirements for them before any model change.

## State (2026-11-12)
- Main merged again (audit lots 2, C, D, E, OpenSCAD RC, charge-port front post): grey sense wires, XF160 in the
  shopping list, FUNC-MECH-JOINT-001 next to the audio requirements. Answered questions removed:
  their answers are in the requirements, the model, `measurements.md` and the shopping list.
- AUDIO domain written: FUNC-AUDIO-SPEAK-001, TECH-AUDIO-SHUTDOWN-001, PLAT-MECH-SPEAKER-001 validated;
  PERF-AUDIO-PEAK-001 (volume cap) and PLAT-AUDIO-AMP-001 (clone board size) draft until measured.
- Model: 4 Ω 2 W speaker 25.27 × 13.80 × 7.15 just under the splint (z 30–55), on pads under its short-end tabs,
  side rails + stop notched for its lower nub, glued; lid speaker tabs removed; grille widened. `make check` and
  `make check-overhang` clean, renders and harness lengths regenerated, README / measurements / open questions (AU1).
- Main merged (requirements reformatted, power safety, charge-port post).
- Clone amplifier received, 17.7 along the header × 18.8 across, E-M1 passed: `amp` folded in, PLAT-AUDIO-AMP-001 validated.
- Review finding 1 (audit A3) done: 4 Ω 2 W speaker in the schematic, BOM, wiring page, budget, bring-up.
- 2026-10-31 (session Tars): pytest for TECH-AUDIO-SHUTDOWN-001; X6 removed, speaker pair soldered on OUT+ / OUT−
  (model, boards, harness, wiring page, README, renders, `make check` clean); 2.2 kΩ dropped from the shopping list.
  Validated and committed: PLAT-POWER-SWITCH-001 ≥ 2 A (stays draft until E-M6, SW1's marking),
  PERF-AUDIO-PEAK-001 cap also ≤ 2 W at VSYS 4.7 V, TECH-AUDIO-SHUTDOWN-001 ≤ 10 µA with the pull-up (audit D4),
  PLAT-MECH-SPEAKER-001 1.5 mm pads (audit D7); power budget amplifier sleep ~4 µA; SW1 at 2 A in the bring-up / BOM.
  Audit 2026-10-29 has nothing left on this branch. Merge blocked by E-M6 and AU1 (see *Open questions*).

## Findings
- **Speaker**: the first one (66 × 30 × 17 box, bare driver 28.6 wide) does not fit the 27.2 interior; replaced by
  the 4 Ω 2 W speaker from stock.
- **Amplifier**: the generic "I2S DAC AMP" module has no shutdown pin; replaced by the purple MAX98357A clone (3 in
  stock), SD on GPIO4 as designed.
- Requirements touched later: [PLAT-POWER-DIST-001](requirements/platform.md#plat-power-dist-001) (MAX98357A on its own
  VSYS pair, C7), [TECH-POWER-BACKFEED-001](requirements/technical.md#tech-power-backfeed-001) (amplifier enable low at start-up),
  `hardware/power_budget.md` amplifier row.

## Open questions
None on this branch. Blocking the merge: [E-M6](open_questions.md) (SW1 rating, PLAT-POWER-SWITCH-001) and
[AU1](open_questions.md) (volume cap, PERF-AUDIO-PEAK-001).

## Next
- Bench: volume cap (PERF-AUDIO-PEAK-001), FUNC-AUDIO-SPEAK-001 SPL check, sound step of PLAT-AUDIO-AMP-001.
- Cleanup (own change): `lid_mid_left` is now identical to `lid_mid` (remove the part: build4.sh, Orca mapping,
  CONTRIBUTING.md).
- Remove status.md before merging.
