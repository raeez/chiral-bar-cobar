"""Surface checks for the strict Koszul boundary wording."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTLOOK = ROOT / "chapters" / "connections" / "outlook.tex"
CONCORDANCE = ROOT / "chapters" / "connections" / "concordance.tex"
CACHE = ROOT / "notes" / "first_principles_cache_comprehensive.md"


def test_strict_koszul_boundary_is_not_swampland_branding():
    active = OUTLOOK.read_text(encoding="utf-8") + "\n" + CONCORDANCE.read_text(
        encoding="utf-8"
    )

    assert r"\begin{conjecture}[Strict Koszul boundary]" in active
    assert "algebraic swampland" not in active
    assert "swampland boundary" not in active
    assert "distance function" not in active
    assert "distance on the landscape" not in active
    assert "quantum-gravity distance criterion" in active


def test_cache_row_173_records_closure_without_renaming_label():
    cache = CACHE.read_text(encoding="utf-8")

    assert "| 173 | Outlook \"Koszul swampland\" (conj:koszul-swampland)" in cache
    assert "Closed 2026-06-09" in cache
    assert "old label is retained only as a cross-reference mnemonic" in cache
