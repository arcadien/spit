# Branch mech-lid-stop

## Goal
Print feedback on the left leg (CR-10, 2026-11-21): the lid flexes over the battery bay; the microSD breakout floats
sideways in its grooves; the charge port breakout stops ~1 mm short of the lid.

## State
- TECH-MECH-LID-001 / PLAT-MECH-LIDSTOP-001 validated and done: 13 lid stops on the column side walls (all four
  columns, around the splint zones); no lid span over 30 mm (longest 29.7, between existing screw rows).
- TECH-MECH-MOUNT-001 / PLAT-MECH-SDSLOT-001 validated and done: microSD grooves 0.5 mm per side (`sd_side_clr`).
- PLAT-MECH-CHARGEPORT-001 fix: breakout length re-measured 14.85 (was 16), PCB back against the lid again.
- Renders added: `renders/spit_lids_inside.png` (4 lids, inner faces), `renders/spit_sd_grooves.png`.

## Open questions
- None.

## Next step
Push (pre-push: STL, renders, Orca meshes), print a leg and its lid, run the bench sheets PLAT-MECH-LIDSTOP-001 and
PLAT-MECH-SDSLOT-001, then merge.
