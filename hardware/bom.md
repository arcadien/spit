# SPIT — bill of materials

Everything the robot is built from, with its reference in the schematic ([kicad/spit_schematic.pdf](kicad/spit_schematic.pdf)).
Why each part is there and where it sits: [design_notes.md](design_notes.md). What is still to buy: [shopping_list.md](shopping_list.md).

## Electronics

| Item | Qty | Notes |
|---|---|---|
| U2 **LOLIN S3 Mini** (wemos.cc original, ESP32-S3FH4R2) | 1 | 34.3 × 25.4, USB-C; male headers soldered pins to the back, plugged into its carrier |
| U3, U4 1.3" IPS 240×240 ST7789 SPI module **with CS** (8 pins), board 27 × 42 | 2 | `lcd130cs` |
| BT1, BT2 18650 Li-ion cell | 2 | one per leg; 18500 also fits (`bat = [18.5, 50]`) |
| Battery contact plates 13 × 18 × 1.2: spring (Ø5, 10.7 high) + button (+, 1.8 overall) | 2 pairs | one pair per leg, wires soldered on the tabs |
| U1 TP4056 charger breakout, **protected (DW01)**, 28.7 × 17.15 × 0.9 (26.3 once its micro-USB is desoldered and the nubs filed) | 1 | left leg, flat above the TPS63020; fed by J1 on its IN pads; **R_PROG swapped for 2.4 k** (0.5 A) |
| J1 micro-USB breakout | 1 | charge port in the left foot, plug from behind at the heel |
| SW1 mini slide switch, 3 pins (1P2T), body 12.95 × 6.9, lever 5.15 | 1 | left leg floor; **check its current rating** (≥ 1 A) |
| U9 **TPS63020** buck-boost module, 3.3 V, EN + PS/SYNC, 26.7 × 17.7 (measured) | 1 | left leg, flat above the microSD; EN to VIN, PS/SYNC to GND |
| U7 DS3231 RTC board (ZS-042) + CR2032 | 1 | right leg, I2C; SQW not wired |
| U8 ADXL345 accelerometer board (GY-291) | 1 | left middle, I2C |
| U6 INMP441 I2S microphone board, 10 × 10 | 1 | left middle, Ø1 hole in the decor groove |
| U11 **BME280** board, purple GY-BME280, 3.3 V | 1 | right leg (z ≈ 190), Ø1.5 vent; no LED on this board |
| U10 **AM312** mini PIR motion sensor | 1 | top of the right middle column, z ≈ 233, 1.25 mm right of the axis |
| J2 microSD breakout, 3.3 V, **no regulator**, 18.2 × 18.2 × 1.5 (21 with the socket) | 1 | left leg |
| U5 MAX98357A I2S amplifier breakout | 1 | right middle; VIN / GND on their own twisted pair from the power board |
| LS1 speaker 39 × 22 × 10 mm, 8 Ω | 1 | behind the lower black panel of the right middle column |
| Q1 P-MOSFET **AO3401A** (or DMG2305UX / SI2301), SOT-23 | 1 | power path, battery side; glued upside down on the perfboard |
| Q5 P-MOSFET **AO3401A** + R22 **100 kΩ** | 1 + 1 | switch the microSD's 3V3 (SD_EN, GPIO36), on the power-path board |
| D1 Schottky **1N5822** (through-hole, 3 A) | 1 | power path, USB side, band towards VPATH (before the switch; 1N5818 also does) |
| D3 **TVS SMAJ5.0A / SMBJ5.0A** (unidirectional) | 1 | on the TP4056's IN+ / IN− pads, cathode to IN+ |
| F1, F2 **polyfuse** (radial PPTC), ≥ 16 V (XF160: 30 V), hold **1.6 A** | 2 | one in each cell's + wire, standing on the inner front wall in front of the cell (XF160 15 × 16 × 2.5) |
| R1 **4.7 kΩ** | 1 | power path, MOSFET gate pull-down |
| R2, R3 **1 MΩ** | 2 | B+ divider (battery monitor): R2 in line in the harness at the TP4056 B+ pad (heat-shrink), R3 on the power-path perfboard |
| Q4 NPN **BC547B** + R23 **1 MΩ**, R24 **330 kΩ** 1/4 W | 1 + 2 | VSYS sense into GPIO37: Q4 and R24 standing on the carrier, R23 in line in the harness at the power-path board (heat-shrink) |
| R15 **68 kΩ**, R16 **100 kΩ** | 1 + 1 | VUSB → USB_DET divider, on the power-path perfboard |
| **2.4 kΩ** (through-hole 1/4 W, or SMD 0805 / 1206) | 1 | replaces the TP4056's R_PROG (1.2 k, removed). A through-hole one can hang on two short wires (≤ 2 cm) on the R_PROG pads, heat-shrink over each joint and the body, glued flat within 5.5 mm above the board (`charger_h`). **The PROG node must never touch GND** (charge current unlimited); a broken wire only stops the charge |
| R4, R18 **10 kΩ** (+ R5–R9 10 kΩ) | 2 (+ 5) | R4 BL_EN → GND (P1), R18 amp SD → GND (P2); R5–R9 microSD pull-ups, only if the reader has none |
| R10, R17 **1 kΩ** | 2 | in series GPIO4 → amp SD, AM312 OUT → GPIO3, on P2 |
| R11, R13, R14, R20 **33 Ω** | 4 | microSD CLK, amp BCLK, amp LRC, MOSI, at the S3 pins |
| R12, R19 **47 Ω** (+ 68 / 100 Ω to try) | 2 | SCK split on the S3's carrier |
| R21 **100 Ω** + C12 **10 µF tantalum 16 V** (+ to PIR_VDD, F6), or a 47 µF electrolytic Ø5 × 7 at most | 1 + 1 | RC filter on the AM312's supply, on P2 (parts ≤ 9 mm in front of it) |
| C1 **220 µF SMD 7343** (7.3 × 4.3), Panasonic POSCAP 10TPE220ML, polymer tantalum 10 V, ESR 25 mΩ (in stock) | 1 | **required**, 3V3–GND at the S3, lying flat on the carrier under the S3 (C2 + / E2 −, a lead offcut soldered on each end); **SMD tantalum band = +** |
| C2, C4, C10 **10 µF tantalum 16 V** (+ to 3V3; in stock) or ceramic X5R/X7R ≥ 6.3 V ("106"), 2.54 pitch, h ≤ 9 | 3 | P1 (G9 + / G10), microSD reader (C4 **lying flat** on its pins: only ~6.6 mm to the TPS63020), P2 (F9 + / F10) |
| C3, C5, C6, C8, C11 **100 nF ceramic**, through-hole, 2.54 pitch, small body (≤ ~4 mm wide, h ≤ 9 on P1 / P2, ≤ 10 under the S3) | 5 | P1 (H9–H10), microSD reader (on its pins), GPIO1 and GPIO21 at the S3 (under it between the headers, ~0.1 mm to their plastic), P2 (G9–G10); **C6 never a tantalum** (leakage on VBAT/2); a 7.15 × 2.4 film fits only C3 (H9–H11) and C5 |
| C7 electrolytic **470 µF**, 10 V, low ESR, Panasonic **EEUFC1A471** (Ø8 × 11.5) | 1 | on the amp's VIN / GND pins, lying across behind the board |
| C9 electrolytic **22 µF** (10–47 µF), 16 V, **Ø ≤ 5.15** lying (`charger_h` 6) | 1 | on the TP4056's IN pads next to D3 |
| Q2 AO3401A + Q3 AO3400A / 2N7002 + 10 kΩ | (1 + 1 + 1) | only if the screens' BLK draws the LED current (see *Signals*) |
| Stripboard 2.54 mm (single-sided), cut to **24 × 32** (9 × 12 holes) | 2 | P1, P2: `../renders/spit_board_p1.svg`, `_p2.svg` |
| **Single-sided** perfboard (FR4) with separate pads, cut to **26.6 × 20** (10 × 8 holes) | 1 | power path (Q1, D1, R1, R3, R15 / R16, Q5 / R22, star ground), `../renders/spit_board_power.svg` |
| **Single-sided** perfboard (FR4) with separate pads, cut to **25.6 × 34.4** (10 × 13 holes) | 1 | the S3's carrier, `../renders/spit_board_s3.svg` |
| Female headers **2 × 8**, 2.54, 8.5 mm high | 2 | the S3's socket (`s3_sock_h` MEASURE) |
| **Right-angle** male header 1 × 8 | 2 | X1 / X4, on the screens' backs, pins down |
| Male header 1 × 2 | 1 | X6, in place of the amp's screw terminal |
| **Dupont 2.54 crimp kit**: housings 1 × 2 … 1 × 8, female contacts (**~100**, ~55 used), male contacts (~20) | 1 kit | X1–X9, X15; ratchet crimper SN-28B / PA-09; spare male pins to plug the keyed cavities |
| **JST-XH** (2.50 pitch) inline pairs to crimp: housings 2- and 4-pin, male + female, with their contacts | 2 + 3 | X12, X16; X10, X13, X14 (SN-28B crimper; 30 AWG folded like in the Dupont contacts) |
| Silicone wire **30 AWG**, tinned copper (not CCA), **10-colour kit** (needs purple and blue) | ~20.3 m | cut lengths from the 3D model in `hardware/spit_harness.pdf` (estimate + 3 cm each, service loops and pigtails included); ≤ 3.6 m per colour (yellow); 9 colours used (grey for the analog sense wires), no black |
| Silicone wire **26 AWG** | ~7.7 m: red 3.3, black 2.5, blue 0.8, white 0.8, grey 0.3 | power pairs: B+/B− of each cell, VSYS / VUSB / VPATH and their GND (red / black), 3V3 / logic GND to P1 (white / blue), amp pair, speaker (grey) (cut lengths in `hardware/spit_harness.pdf`) |
| **Wire-wrap wire 30 AWG** (Kynar insulated), 1 small spool | 1 | Q1 / Q5 leads on the power-path board (a few mm each), signal jumpers (power jumpers in 26 AWG) |
| **Tinned copper wire** 0.5–0.6 mm (or cut resistor leads) | ~0.5 m | bare GND buses (carrier column E, power-board row 1) |
| Cyanoacrylate or 5-minute epoxy | — | the S3's female headers on the single-sided carrier |
| USB charger **5 V ≥ 2 A** + micro-USB cable | 1 | mains operation while charging |
| Heat-shrink 1.5–3 mm, **coloured assortment** (black, white, yellow, orange, purple at least) | ~1 m | twisted pair ends, solder joints, Dupont insulation wings, tube exits; black signal-bus rings; coloured power-rail bands (white OUT+, yellow VPATH, orange VSYS, purple VUSB, ~40 × 10 mm) |

## Hardware

| Item | Qty | Notes |
|---|---|---|
| Brass tube 8 / 7 mm, cut to ~20 mm | 3 | one per joint |
| M2.5 × 6 (or × 8) screws, **thin / ultra-low head, black** (head Ø~5, height ≤ 2) | 32 | lids: 7 per middle column, 9 per leg. Threaded **straight into the printed bosses** (Ø2.1 pilot, 9 deep) through the lid (Ø2.9 hole): × 6 engages 4.4 mm, × 8 6.4 mm. Good for ~10–20 openings: turn backwards until the thread clicks, then tighten, snug only. Upgrade: drill the pilots to 3.5 for M2.5 heat-set inserts |
| M2 × 5 self-tapping screws | (8) | only if the measured screen has usable mounting holes |
| Rubber feet, stick-on Ø8 (e.g. 3M Bumpon) | 16 | 4 per column |
| Epoxy (splints, tubes, collars), CA (plugs) | | |

## Filament

| Material | Parts | Approx. |
|---|---|---|
| Matte grey PLA | 8 column halves, 8 lid halves, 4 splints | ~350 g |
| Matte black PLA | panel plugs | < 10 g |
| PETG (any colour) | 3 tube collars | < 5 g |
