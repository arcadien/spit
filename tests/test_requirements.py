"""Requirement coverage: every validated requirement is checked somewhere, or justified in audits/exclusions.yml
(a coverage exclusion, `id: COVERAGE-…`).

Covered = a pytest test tagged @pytest.mark.req('<ID>'), a bench sheet under tests/bench/ (the RBD bench sheet path)
carrying a `<!-- @req <ID> -->` line, or a firmware Unity test tagged `// req: <ID>` under software/. A requirement
waiting for its firmware test is covered by a coverage exclusion until that test exists. A bench sheet that was never
run (no result line) is reported.
"""
import glob
import os
import re
import warnings

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID = r'[A-Z]+-[A-Z0-9]+-[A-Z0-9]+-\d{3}'
SECTIONS = ('## Equipment', '## Setup', '## Steps', '## Pass criteria', '## Results')


def read(path):
    return open(path, encoding='utf-8').read()


def requirements():
    """{id: status}"""
    reqs = {}
    for f in glob.glob(os.path.join(ROOT, 'requirements', '*.md')):
        for m in re.finditer(rf'^### ({ID})\n(?:(?:\*\*.*)?\n)*?\*\*Status:\*\* (\S+)\n(?:.*\n)*?\*\*Description:\*\* (.*)',
                             read(f), re.M):
            reqs[m.group(1)] = m.group(2)
    return reqs


def sheets():
    return glob.glob(os.path.join(ROOT, 'tests', 'bench', '*-*-*-*.md'))


def unity_tagged():
    files = [f for ext in ('c', 'cpp', 'h') for f in glob.glob(os.path.join(ROOT, 'software', '**', f'*.{ext}'),
                                                                 recursive=True)]
    return {i for f in files for i in re.findall(rf'// req: ({ID})', read(f))}


def test_every_validated_requirement_is_tested_or_excluded():
    # Given the validated requirements, the tests, the test sheets and the exclusions
    reqs = {i for i, st in requirements().items() if st == 'validated'}
    tagged = {i for f in glob.glob(os.path.join(ROOT, 'tests', '*.py'))
              for i in re.findall(rf"@pytest\.mark\.req\('({ID})'\)", read(f))}
    covered = tagged | {i for f in sheets() for i in re.findall(rf'^<!-- @req ({ID}) -->$', read(f), re.M)} | unity_tagged()
    # only a coverage exclusion (id: COVERAGE-…) stands for a test; other exclusions only name the requirements they waive
    entries = read(os.path.join(ROOT, 'audits', 'exclusions.yml')).split('  - id: ')[1:]
    excluded = {i for e in entries if e.startswith('COVERAGE-') for i in re.findall(ID, e.split('\n', 1)[1])}
    # Then every validated requirement is covered or excluded
    assert sorted(reqs - covered - excluded) == []


def test_every_test_sheet_is_complete_and_names_a_requirement():
    reqs = requirements()
    never_run = []
    for f in sheets():
        rid, text = os.path.basename(f)[:-3], read(f)
        # Given a manual test sheet: it is named after an existing requirement and links to it
        assert rid in reqs, f'{f}: no requirement {rid}'
        assert f'[{rid}](../../requirements/' in text, f'{f}: no link to its requirement'
        # And it carries the RBD tag of its requirement on its first line
        assert text.startswith(f'<!-- @req {rid} -->\n'), f'{f}: first line is not <!-- @req {rid} -->'
        # Then it has every section, in order
        pos = [text.find(s) for s in SECTIONS]
        assert -1 not in pos and pos == sorted(pos), f'{f}: sections missing or out of order'
        # And its result table has a header; a sheet without any result line was never run
        rows = [ln for ln in text[pos[-1]:].splitlines() if ln.startswith('|')]
        assert len(rows) >= 2 and rows[0].startswith('| Date |'), f'{f}: no result table'
        if len(rows) == 2:
            never_run.append(rid)
    if never_run:
        warnings.warn(f'{len(never_run)} manual test sheet(s) never run: {", ".join(sorted(never_run))}')
