# Branch mech-switch-3a

**Goal:** fit the new 3 A slide switch SW1 (TRU Components TC-R13-603C-05, received 2026-11-26) in the left leg floor
([PLAT-MECH-SWITCH-001](requirements/platform.md#plat-mech-switch-001)). The old mini switch body (12.95 × 6.9) is
replaced; the new one has a 19.5 mm mounting plate with two ears, which ran into the charge port when centred.

**State:** model done: plate glued flat on a pad, located by two Ø2.2 pins through the ear holes (no screws: a
screwdriver cannot reach them under the bottom contact shelf), switch 2 mm off-centre towards the right wall (plate to
charge port 0.68 mm, to the wall 1.85 mm), lever 0.5 mm recessed in a 6.8 × 4.5 floor slot. Rating 3 A 125 V recorded
(E-M6 closed).

**Open on this branch:** PLAT-POWER-SWITCH-001 (draft, on `mech-audio`) still says "Pending: E-M6"; only its 1 A
temperature-rise bench check remains.

**Next step:** push (renders, meshes), print the left leg bottom, run
[tests/bench/PLAT-MECH-SWITCH-001.md](tests/bench/PLAT-MECH-SWITCH-001.md), merge. Remove this file before the merge.
