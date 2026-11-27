# Configuration Requirements

<!-- Requirements are added here during Phase 2 of the RBD workflow. -->
<!-- Format: req(ID): title -->

### CONF-POWER-THRESH-001

**Title:** Battery thresholds are configuration values

**Status:** validated

**Dependencies:** none

**Description:** The battery thresholds are configuration constants defined in one place, with these defaults: level bounds L1 / L2 / L3 = 3.90 / 3.70 / 3.50 V, cut-off 3.30 V, no-battery limit 2.50 V, averaging window 60 s, charge full = a peak ≥ 4.10 V then a drop of 20 mV below the peak, empty-lockout release voltage 3.50 V, lockout re-check interval 10 min. Why each default: [design_notes.md](../hardware/design_notes.md) (*Battery thresholds*). The values measured on the bench must be settable without touching the logic.

### CONF-POWER-ADCCAL-001

**Title:** Battery-measurement calibration is configurable

**Status:** draft

**Dependencies:** none

**Description:** The battery divider ratio (default 2.000) and an offset (default 0 mV) are configuration values, set once after the bench calibration.
