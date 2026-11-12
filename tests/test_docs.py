"""Documentation layout: each fact written once, in the document that owns it."""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
README = (ROOT / 'README.md').read_text(encoding='utf-8')
# a heading line or table header that marks each kind of content, and the document that owns it
OWNED = {
    'bill of materials': ('## Electronics', 'hardware/bom.md'),
    'GPIO table': ('| Function | Signals | Notes |', 'hardware/design_notes.md'),
    'colour code': ('### Colour code', 'hardware/design_notes.md'),
    'connector table': ('| Ref | Module ↔ harness |', 'hardware/design_notes.md'),
}


@pytest.mark.req('TECH-BUILD-DOCS-001')
def test_every_relative_link_of_the_readme_resolves():
    # Given the README's markdown links
    links = re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', README)
    # When the web links are left out
    local = [l for l in links if not l.startswith(('http://', 'https://'))]
    # Then each one names a file or folder of the repository
    assert [l for l in local if not (ROOT / l).exists()] == []


@pytest.mark.req('TECH-BUILD-DOCS-001')
@pytest.mark.parametrize('kind', OWNED)
def test_owned_content_lives_in_its_document_not_in_the_readme(kind):
    # Given the marker of a kind of content and the document that owns it
    marker, owner = OWNED[kind]
    # When the README and the owner are read
    text = (ROOT / owner).read_text(encoding='utf-8')
    # Then only the owner holds it
    assert marker not in README
    assert marker in text
