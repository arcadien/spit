"""PLAT-MECH acceptance criteria checked on the model (requirements/platform.md): mechanical/scad/spit.scad is
evaluated once by OpenSCAD without any export (part="none"), its echoed values and WARNINGs are read back."""
import os
import re
import shutil
import subprocess

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAD = os.path.join(ROOT, 'mechanical', 'scad', 'spit.scad')
VALUES = ('tube_od', 'tube_glue_clr', 'tube_run_clr')


@pytest.fixture(scope='session')
def model(tmp_path_factory):
    d = tmp_path_factory.mktemp('model')
    probe = d / 'probe.scad'
    probe.write_text(f'include <{SCAD.replace(os.sep, "/")}>\necho({", ".join(f"{v}={v}" for v in VALUES)});\n',
                     encoding='utf-8')
    run = subprocess.run([shutil.which('openscad') or 'openscad', '-D', 'part="none"', '-o', str(d / 'm.echo'),
                          str(probe)], capture_output=True, text=True, timeout=300)
    echo = (d / 'm.echo').read_text(encoding='utf-8') + run.stdout + run.stderr
    line = next(ln for ln in echo.splitlines() if ln.startswith(f'ECHO: {VALUES[0]} ='))
    values = {k: float(v) for k, v in re.findall(r'(\w+) = ([-\d.]+)', line)}
    return values, [ln for ln in echo.splitlines() if 'WARNING' in ln or 'ERROR' in ln]


def source():
    return open(SCAD, encoding='utf-8').read()


@pytest.mark.req('PLAT-MECH-CHARGEPORT-001')
def test_plat_mech_chargeport_001_charge_port_geometry_asserts_hold(model):
    # Given the model and its charge-port geometry asserts (axis, mouth depth, height, clearances)
    asserts = re.findall(r'echo\("WARNING: charge port', source())
    assert len(asserts) >= 6, 'charge port asserts removed from spit.scad'
    # When it is evaluated
    _, warnings = model
    # Then it prints no WARNING / ERROR at all (make check clean)
    assert warnings == []


@pytest.mark.req('PLAT-MECH-PIVOT-001')
def test_plat_mech_pivot_001_teardrop_bores_sized_from_tube_test3(model):
    # Given the evaluated model
    values, warnings = model
    # Then the tube and its two clearances are the measured ones
    assert values == {'tube_od': 7.93, 'tube_glue_clr': 0.07, 'tube_run_clr': 0.12}
    # And every pivot bore is a teardrop (pivot_cut cuts with xtear only)
    body = re.search(r'module pivot_cut\(i\) \{(.*?)\n\}', source(), re.S).group(1)
    assert 'xtear(' in body and 'cylinder(' not in body
    # And the model is clean
    assert warnings == []


@pytest.mark.req('PLAT-MECH-SWITCH-001')
def test_plat_mech_switch_001_switch_glued_on_pad_located_by_pins(model):
    # Given the model
    src = source()
    # Then the switch is the measured 3 A one: body, lever, travel, mounting plate and its holes
    for line in (r'sw_body = \[9\.75, 8\.17\];', r'sw_lever = \[4, 3\.9\];', r'sw_travel = 2\.2;',
                 r'sw_recess = 0\.5;', r'sw_plate = \[19\.5, 8, 0\.42\];', r'sw_pitch = 14\.45;',
                 r'sw_hole = 2\.45;', r'sw_x = col_w / 2 \+ 2;'):
        assert re.search('^' + line, src, re.M), line
    # And it is located by pins through its holes, no screws
    assert 'sw_pin' in src and 'pilot' not in re.search(r'module switch_pad\(\) \{(.*?)\n\}', src, re.S).group(1)
    # And the model is clean (charge port, lid and shelf asserts included)
    _, warnings = model
    assert warnings == []


@pytest.mark.xfail(strict=True, reason='PLAT-MECH-CONTACT-001 not implemented yet')
@pytest.mark.req('PLAT-MECH-CONTACT-001')
def test_plat_mech_contact_001_plates_located_by_guides_without_glue(model):
    # Given the model
    src = source()
    # Then the plates are the measured ones (flat part + centred tab)
    assert re.search(r'^contact = \[13, 11, 1\.2\];', src, re.M)
    assert re.search(r'^contact_tab = \[3, 7\.5\];', src, re.M)
    # And both shelves get their guides, below the plate face, clear of the tab
    assert src.count('contact_guides(') >= 3
    assert 'WARNING: contact guides higher than the plate' in src
    assert 'WARNING: contact stops run into the tab' in src
    # And the model is clean
    _, warnings = model
    assert warnings == []
