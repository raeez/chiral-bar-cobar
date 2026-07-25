"""
Guardrails for the ordered E1 all-genus theorem surface.

The ordered E1 modular chapter states its all-genus surfaces on the
strict ordered Mittag--Leffler modular tower, whose convergence and
descent data form the explicit hypothesis package.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
E1_TEX = ROOT / "chapters/theory/e1_modular_koszul.tex"


def _window_around(text: str, label: str, radius: int = 1300) -> str:
    idx = text.index(label)
    return text[max(0, idx - radius) : idx + radius]


def test_e1_all_genus_surfaces_carry_the_strict_tower_package():
    tex = E1_TEX.read_text()
    labels = (
        "thm:e1-theorem-A-modular",
        "thm:e1-theorem-B-modular",
        "thm:e1-theorem-C-modular",
        "thm:e1-theorem-D-modular",
        "thm:e1-theorem-H-modular",
    )
    for label in labels:
        window = _window_around(tex, "\\label{" + label + "}")
        assert "\\ClaimStatusConditional" in window


def test_e1_section_names_strict_ordered_tower_hypotheses():
    tex = E1_TEX.read_text()
    section = _window_around(tex, "\\label{sec:e1-five-theorems}", 1900)
    assert "strict ordered Mittag" in section
    assert "square-zero" in section
    assert "filtration-continuous" in section
    assert "degree-$2$ component of the\nordered Maurer--Cartan element" in section
