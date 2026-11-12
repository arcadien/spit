"""Project name: SPIT (SPit Is not TARS)."""
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ARCHIVES = ('references/', 'reviews/', 'audits/')   # TARS stays there: the film robot and the archived wording
BRAILLE = {'S': [2, 3, 4], 'P': [1, 2, 3, 4], 'I': [2, 4], 'T': [2, 3, 4, 5]}


@pytest.mark.req('TECH-BUILD-NAME-001')
@pytest.mark.xfail(strict=True, reason='rename not done yet')
def test_no_versioned_path_is_named_after_tars():
    # Given the versioned files
    paths = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    # When the archives are left out
    named = [p for p in paths if 'tars' in p.lower() and not p.startswith(ARCHIVES)]
    # Then none is named after TARS
    assert named == []


@pytest.mark.req('TECH-BUILD-NAME-001')
@pytest.mark.xfail(strict=True, reason='rename not done yet')
def test_model_engraves_spit_in_letters_and_braille():
    # Given the model
    scad = (ROOT / 'mechanical/scad/spit.scad').read_text()
    # When its engraving is read
    cells = re.search(r'braille_spit = (\[.*?\]);', scad).group(1)
    # Then it spells SPIT in letters and in braille
    assert 'text("SPIT"' in scad
    assert eval(cells) == [BRAILLE[c] for c in 'SPIT']
