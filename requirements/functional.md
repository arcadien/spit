# Functional Requirements

<!-- Requirements are added here during Phase 2 of the RBD workflow. -->
<!-- Format: req(ID): title -->

### FUNC-POWER-CHARGE-001

**Title:** Battery charges from an external 5 V USB supply

**Status:** validated

**Dependencies:** [TECH-POWER-CHARGE-001](technical.md#tech-power-charge-001)

**Description:** When a 5 V USB supply is connected to the robot's charge port, the battery charges and the charge stops by itself when the battery is full ([TECH-POWER-CHARGE-001](technical.md#tech-power-charge-001)). The charge port is on the heel (back face) of the left leg and can be reached while the robot stands upright on its feet, without opening any lid, lifting or tilting the robot. A standard micro-USB cable plugged in horizontally from behind rests on the table and leaves the robot standing; with the robot lying face down, the port stays reachable too.

### FUNC-POWER-PATH-001

**Title:** On an external supply, the system load does not draw from the battery

**Status:** validated

**Dependencies:** [FUNC-POWER-CHARGE-001](functional.md#func-power-charge-001), [TECH-POWER-CHARGE-001](technical.md#tech-power-charge-001)

**Description:** While an external supply is connected, the system rail is fed from that supply, not from the battery, so the charger only sees battery current and ends the charge normally while the robot runs. With a full battery (charge ended) and the supply connected, the battery current stays ≥ −0.1 mA whether the system load is on or off: no load current comes from the battery.

### FUNC-POWER-PATH-002

**Title:** Connecting or disconnecting the external supply does not reset the robot

**Status:** validated

**Dependencies:** [FUNC-POWER-PATH-001](functional.md#func-power-path-001)

**Description:** Plugging in or unplugging the external supply while the robot runs on a charged battery must not reset the controller. Across 20 plug / unplug cycles at a 110 mA system load and 20 at a 1 A load, the system rail never drops below 3.0 V and the controller never resets (no brown-out or power-on reset).

### FUNC-POWER-SWITCH-001

**Title:** The power switch turns the robot off

**Status:** validated

**Dependencies:** none

**Description:** A user-operated switch disconnects the system rail from both the battery and the external supply. With the switch off, the system rail is < 0.1 V both on battery alone and with the external supply connected. Exception: a host plugged into the programming port powers the controller only ([TECH-POWER-VBUS-001](technical.md#tech-power-vbus-001)).

### FUNC-POWER-SWITCH-002

**Title:** Charging works with the power switch off

**Status:** validated

**Dependencies:** [FUNC-POWER-CHARGE-001](functional.md#func-power-charge-001), [FUNC-POWER-SWITCH-001](functional.md#func-power-switch-001)

**Description:** The robot recharges when plugged in, whether it is switched on or off: switching it off neither stops nor slows the charge: on the same battery, the charge current with the robot switched off and with it switched on and idle differ by no more than 10 %. Where its consumption comes from while it is on is [FUNC-POWER-PATH-001](functional.md#func-power-path-001)'s.

### FUNC-POWER-MONITOR-001

**Title:** Firmware measures the battery voltage

**Status:** validated

**Dependencies:** none

**Description:** The firmware measures the voltage at the battery terminals (not the system rail), both on battery and with the external supply connected. The reported value is the B+ voltage within ±5 % before calibration (the calibrated accuracy is [PERF-POWER-MONITOR-001](performance.md#perf-power-monitor-001)'s); on the external supply it does not follow the system rail (~4.7 V).

### FUNC-POWER-MONITOR-002

**Title:** Battery level classification ("hunger")

**Status:** validated

**Dependencies:** [FUNC-POWER-MONITOR-001](functional.md#func-power-monitor-001), [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)

**Description:** On battery, the firmware averages the battery voltage over the averaging window of [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001) and classifies it into five levels: fed (v ≥ L1), peckish (L2 ≤ v < L1), hungry (L3 ≤ v < L2), starving (cut-off < v < L3), empty (v ≤ cut-off), where L1 > L2 > L3 are the level bounds and the cut-off is that of [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001): each boundary belongs to exactly one band. The window average is the only hysteresis: there is no extra band, so one sample (a Wi-Fi or amplifier peak) cannot change the level. For example, a 2 s dip of 0.3 V inside a stable window leaves the level unchanged.

### FUNC-POWER-MONITOR-003

**Title:** Charging and full states replace the level on an external supply

**Status:** validated

**Dependencies:** [FUNC-POWER-DETECT-001](functional.md#func-power-detect-001), [FUNC-POWER-MONITOR-001](functional.md#func-power-monitor-001), [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)

**Description:** While the external supply is present, the firmware reports the battery state as "charging" instead of a level, then "full" once the charge has ended. The end of charge is inferred from the battery voltage alone; the charger's status output is not wired. "Full" is reported once the averaged voltage, having reached the charge-full peak level, has fallen by the charge-full drop below its highest value ([CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)): relative to the peak, so a charger ending anywhere in 4.158–4.242 V is seen. When the supply is removed, the [FUNC-POWER-MONITOR-002](functional.md#func-power-monitor-002) level is reported again.

### FUNC-POWER-DETECT-001

**Title:** Firmware detects the external supply

**Status:** validated

**Dependencies:** none

**Description:** The firmware knows whether an external supply is connected to the charge port, whatever the battery state. The detection follows a plug-in or an unplug within 1 s.

### FUNC-POWER-DETECT-002

**Title:** Connecting the external supply wakes the robot

**Status:** validated

**Dependencies:** [FUNC-POWER-DETECT-001](functional.md#func-power-detect-001), [FUNC-POWER-SWITCH-001](functional.md#func-power-switch-001)

**Description:** With the power switch on, connecting the external supply wakes the controller from deep sleep, including after a low-battery shutdown ([FUNC-POWER-CUTOFF-002](functional.md#func-power-cutoff-002)). With the switch off, plugging in only charges the battery ([FUNC-POWER-SWITCH-002](functional.md#func-power-switch-002)): the robot stays off. The wake-up comes within 1 s of plugging in, and the reported wake cause is the supply detection; with the switch off, the system rail stays < 0.1 V.

### FUNC-POWER-VSENSE-001

**Title:** Firmware detects that the system rail is powered

**Status:** validated

**Dependencies:** none

**Description:** The firmware knows whether the system rail (after the power switch) is powered, independently of the battery voltage and of the external supply. This covers the case "switch off, controller powered from the programming port". The rail is reported present for 3.0–5.0 V and absent below 2.3 V (the amplifier needs ≥ 2.5 V); on battery, the report follows a switch toggle within 100 ms. With the controller powered from the programming port and the switch turned off, the rail capacitors drain only through the regulator's quiescent current and the rail takes tens of seconds to fall; the report then turns absent within 100 ms of the rail falling below 2.3 V.

### FUNC-POWER-CUTOFF-001

**Title:** Low-battery shutdown

**Status:** validated

**Dependencies:** [FUNC-POWER-MONITOR-002](functional.md#func-power-monitor-002), [FUNC-POWER-DETECT-001](functional.md#func-power-detect-001), [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)

**Description:** When the averaged battery voltage reaches the empty level (≤ the cut-off of [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)) and no external supply is present, the firmware puts the robot into deep sleep. No shutdown happens while the external supply is present, nor when the battery reading is below the no-battery limit of [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001) (no cells: controller powered from the programming port).

### FUNC-POWER-CUTOFF-002

**Title:** An empty battery stays asleep until it is charging and above the lockout release voltage

**Status:** validated

**Dependencies:** [FUNC-POWER-CUTOFF-001](functional.md#func-power-cutoff-001), [FUNC-POWER-DETECT-002](functional.md#func-power-detect-002)

**Description:** After a low-battery shutdown, the firmware records an "empty" state that survives deep sleep. While it is set, every wake returns to deep sleep without turning on the screens, the amplifier or the radio. It is cleared only when the external supply is present and the battery is above the empty-lockout release voltage ([CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)). While the supply is present, the controller wakes on a timer every re-check interval ([CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)) to test this; on battery alone no timer wake is armed, so an empty battery is not drained further. While the state is set, a wake returns to deep sleep within 200 ms with the screen, amplifier and card enables low, and the timer wakes come at the re-check interval ± 10 %.

### FUNC-POWER-GATE-001

**Title:** Firmware can cut the supply of the removable storage card

**Status:** validated

**Dependencies:** none

**Description:** The removable storage card's supply is switched by the firmware and is off while the controller is in reset or has not yet driven the switch. Before cutting it, the firmware stops driving the card's signal lines. Off means < 0.1 V at the card, and the card's signal pins are inputs whenever its supply is off.

### FUNC-MECH-JOINT-001

**Title:** The columns turn on their joints

**Status:** draft

**Dependencies:** none

**Description:** The four columns are joined on one horizontal axis by three joints; each column turns by hand ±45° from the aligned position relative to its neighbours, and the wires running from column to column cross each joint inside its tube, so turning a column twists them over their free length instead of pulling on them. Over the whole ±45°, the column turns under a push ≤ 5 N at its foot, with the smallest side play at the foot that this force allows; its bound is set from the side play measured on the first assembled joint (pending: E-M11, [open_questions.md](../open_questions.md)). Twenty turns back and forth over ±45° leave every wire crossing a joint intact.
