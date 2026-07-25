"""Guards for MC5 closure scope in editorial_constitution.tex."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/connections/editorial_constitution.tex"


def visible_text() -> str:
    return "\n".join(
        line
        for line in SOURCE.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def window_after_label(text: str, label: str, lines: int) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    return "\n".join(text.split(anchor, 1)[1].splitlines()[:lines])


def environment_window(text: str, label: str, lines: int) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    prefix, suffix = text.split(anchor, 1)
    begin = prefix.rfind(r"\begin{")
    assert begin != -1, label
    return "\n".join((prefix[begin:] + anchor + suffix).splitlines()[:lines])


class TestEditorialConstitutionMC5Scope:
    def test_standard_tower_mc5_closure_is_explicitly_conditional(self):
        text = visible_text()
        window = normalized(environment_window(text, "cor:standard-tower-mc5-closure", 95))

        required = (
            "Conditional standard-tower MC5 closure under DK/KL and",
            "\\ClaimStatusConditional",
            "conditional on these four packages",
            "no further infinite-tower algebraic obstruction",
            "not an unconditional closure theorem",
            "Conjecture~\\ref{conj:master-dk-kl}",
            "Conjecture~\\ref{conj:standard-tower-mc5-reduction}",
            "BV/BRST/bar comparison package",
            "under the full stated package",
        )
        for fragment in required:
            assert fragment in window

        forbidden = (
            "Standard-tower MC5 closure on the canonical Yangian locus",
            "Then the standard-tower MC5 packet closes.",
            "Hence the standard-tower MC5 packet closes.",
        )
        for fragment in forbidden:
            assert fragment not in window

    def test_standard_tower_reduction_remains_conjectural(self):
        text = visible_text()
        window = normalized(environment_window(text, "conj:standard-tower-mc5-reduction", 95))

        required = (
            "\\ClaimStatusConjectured",
            "conditional implication, not a closure theorem",
            "Conjecture~\\ref{conj:master-dk-kl}",
            "conditional on the stated hypotheses",
        )
        for fragment in required:
            assert fragment in window
