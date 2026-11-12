# Bench test PERF-AUDIO-PEAK-001 — firmware volume cap (AU1)

Requirement: [PERF-AUDIO-PEAK-001](../../requirements/performance.md#perf-audio-peak-001). Manual test, run at bring-up
after the MAX98357A step ([bring-up.md](bring-up.md)); add a line to *Results* every time it is run. It sets the cap
value (MEASURE): write it in [measurements.md](../../hardware/measurements.md) and in the firmware configuration.

## Equipment
- The assembled robot, cells fitted, speaker soldered on the amplifier OUT+ / OUT−.
- Bench firmware with: full-scale 400 Hz and 1 kHz sine tones and the loudest voice file, digital volume in 1 dB steps
  (−12 dB to 0 dB), screens on and Wi-Fi connected while it plays, a boot counter printed on the serial port.
  The `bench-tests` S3 firmware has the amplifier, an MP3 and 3 coarse volumes only: add the tones, the 1 dB steps and
  the boot counter first.
- A scope, or a multimeter with min-hold, on the amplifier VIN (X13 VSYS / GND amp contacts).
- A true-RMS multimeter for case B (class D output: read across the speaker terminals, speaker connected).
- The 6.8 Ω 10 W resistor with crocodile leads; a 5 V ≥ 2 A USB charger and a micro-USB cable.

## Setup
1. Case A (battery): discharge the pack through the 6.8 Ω on VSYS (SW1 on), as in
   [PERF-POWER-CHARGE-001](PERF-POWER-CHARGE-001.md), until B+ reads 3.30 V under load; remove the resistor. Use the
   real cells, not the bench supply: its stiffer output would give a too optimistic cap.
2. Case B (external supply): charger plugged, SW1 on.

## Steps
1. Case A, volume −12 dB: play the 400 Hz tone, the 1 kHz tone, then the voice file, 5 s each. Read the minimum VIN
   and the boot counter.
2. Raise the volume by 1 dB and repeat step 1, until VIN < 3.0 V, a reset, or 0 dB. Cap A = the last step that passed.
3. Case B, volume at cap A: play the 1 kHz tone, read the RMS voltage across the speaker. If > 2.83 V, lower by 1 dB
   until ≤ 2.83 V. Cap B = that step.
4. Cap = the lower of cap A and cap B. Recheck B+ is still ≥ 3.25 V at the end of case A (else recharge to 3.30 V and
   redo the last steps).

## Pass criteria
- At the cap, case A: VIN ≥ 3.0 V on all three sounds, boot counter unchanged.
- At the cap, case B: ≤ 2.83 V RMS across the speaker (2 W on 4 Ω).

## Results
| Date | Commit / build | B+ at start | Cap A | Min VIN at cap | Cap B | V RMS at cap | Cap | Pass | By | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
