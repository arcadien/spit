# Performance Requirements

<!-- Requirements are added here during Phase 2 of the RBD workflow. -->
<!-- Format: req(ID): title -->

### PERF-POWER-REG-001

**Title:** 3.3 V rail static regulation

**Status:** validated

**Dependencies:** [TECH-POWER-REG-001](technical.md#tech-power-reg-001)

**Description:** The 3.3 V rail stays at 3.30 V ± 3 % (3.20–3.40 V) for loads from 0 to 500 mA and system-rail inputs from 3.0 V to 5.0 V.

### PERF-POWER-REG-002

**Title:** 3.3 V rail under load transients

**Status:** validated

**Dependencies:** [PERF-POWER-REG-001](performance.md#perf-power-reg-001), [TECH-POWER-DIST-001](technical.md#tech-power-dist-001)

**Description:** At the controller's 3.3 V pin, the rail stays ≥ 3.10 V during Wi-Fi transmit bursts and during full-volume audio playback, with the battery at 3.4 V. The controller does not reset, with Wi-Fi transmit and full-volume audio running together for 60 s.

### PERF-POWER-PATH-001

**Title:** Power-path voltage drop

**Status:** validated

**Dependencies:** [FUNC-POWER-PATH-001](functional.md#func-power-path-001)

**Description:** At a 110 mA system load, the system rail is within 0.10 V of the battery voltage on battery, and within 0.50 V of the external-supply voltage on the external supply. On the external supply with the switch on, the cell charge current is the one set by R_PROG ([PLAT-POWER-CHARGE-002](platform.md#plat-power-charge-002)) within ± 10 %: the cells are charged only through the charger.

### PERF-POWER-CHARGE-001

**Title:** Full charge time

**Status:** validated

**Dependencies:** [FUNC-POWER-CHARGE-001](functional.md#func-power-charge-001), [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001)

**Description:** A full charge of the pack, from the cut-off of [CONF-POWER-THRESH-001](configuration.md#conf-power-thresh-001) to the end of charge, with the robot switched off, takes ≤ 8 h at the 1 A charge current (R_PROG 1.2 kΩ).

### PERF-POWER-THERMAL-001

**Title:** Leg wall temperature while charging

**Status:** validated

**Dependencies:** [FUNC-POWER-CHARGE-001](functional.md#func-power-charge-001), [FUNC-POWER-PATH-001](functional.md#func-power-path-001)

**Description:** While charging at the maximum charge current, the outer wall of the PLA leg next to the charger stays ≤ 45 °C (PLA softens at ~55–60 °C). Lids are closed and the ambient is 20–25 °C. Two cases: robot off, and robot running at a 1 A load on the external supply. The limit holds over 30 min of charge.

### PERF-POWER-MAINS-001

**Title:** External supply voltage under the maximum combined load

**Status:** validated

**Dependencies:** [FUNC-POWER-PATH-001](functional.md#func-power-path-001)

**Description:** With a 5 V ≥ 2 A supply, the battery charging at maximum current and a 1 A system load, the voltage at the charger input stays ≥ 4.60 V for 30 min.

### PERF-POWER-MONITOR-001

**Title:** Battery voltage measurement accuracy

**Status:** draft

**Dependencies:** [FUNC-POWER-MONITOR-001](functional.md#func-power-monitor-001), [CONF-POWER-ADCCAL-001](configuration.md#conf-power-adccal-001)

**Description:** After calibration ([CONF-POWER-ADCCAL-001](configuration.md#conf-power-adccal-001)), the battery voltage reported by the firmware is within ±3 % of a multimeter reading at B+ over 3.0–4.2 V.

### PERF-POWER-SLEEP-001

**Title:** Deep-sleep current from the battery

**Status:** draft

**Dependencies:** [TECH-POWER-SLEEP-001](technical.md#tech-power-sleep-001), [FUNC-POWER-GATE-001](functional.md#func-power-gate-001)

**Description:** In deep sleep, with every wake source armed and the storage card supply cut, the robot draws ≤ 0.65 mA from the battery (breakdown per module: [power_budget.md](../hardware/power_budget.md)). With ~5–10 % of capacity left after the cut-off, this keeps the pack above the protection's 2.4 V threshold for weeks.

### PERF-POWER-OFF-001

**Title:** Battery drain with the switch off

**Status:** draft

**Dependencies:** [FUNC-POWER-SWITCH-001](functional.md#func-power-switch-001)

**Description:** With the power switch off and no external supply, the battery drain is ≤ 60 µA: charger and protection quiescent current, the battery divider and power-path diode leakage (breakdown: [power_budget.md](../hardware/power_budget.md)). The limit holds at room temperature and at 35 °C (a hot room).

### PERF-POWER-RUNTIME-001

**Title:** Runtime on a full charge

**Status:** draft

**Dependencies:** [PERF-POWER-CHARGE-001](performance.md#perf-power-charge-001)

**Description:** From a full charge to the low-battery shutdown, on two cells of ≥ 2500 mAh rated capacity each, the robot runs ≥ 20 h under the reference profile: Wi-Fi connected and idle, both screens at full backlight, no audio. The expected average current per module is in [power_budget.md](../hardware/power_budget.md).
