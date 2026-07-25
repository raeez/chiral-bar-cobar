"""Regression guards for the ordered chiral bar sign/completion surface."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BAR_CONSTRUCTION = ROOT / "chapters/theory/bar_construction.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _bar_text() -> str:
    return BAR_CONSTRUCTION.read_text()


def test_ordered_bar_definition_uses_precise_desuspension_signs():
    text = _bar_text()

    required_fragments = [
        r"the signs are not independent notation",
        r"(-1)^{\sum_{q<i}(|a_q|-1)}",
        r"(-1)^{\sum_i |a_i|}",
        r"(-1)^{\sum_{q<i}(|a_q|-1)+|a_i|}",
        r"Proposition~\ref{prop:ordered-bar-local-differential-identities}",
        r"Theorem~\ref{thm:ordered-bar-complete-conilpotent-functor}",
    ]

    for fragment in required_fragments:
        assert fragment in text


def test_ordered_bar_keeps_full_fm_separate_from_chirass_quotient():
    text = _bar_text()

    required_fragments = [
        r"For a non-adjacent full-FM face",
        r"The consecutive-block",
        r"\(\chirAss\) quotient has only adjacent word-contractions",
        r"full pairwise FM screen",
    ]

    for fragment in required_fragments:
        assert fragment in text


def test_ordered_bar_completion_gate_is_explicit():
    text = _bar_text()

    required_fragments = [
        "finite output in every",
        "fixed word-length window",
        "finite-output and product-completion hypotheses",
        "every finite word-length quotient is conilpotent",
        "product completion is",
        "complete pro-conilpotence",
    ]

    for fragment in required_fragments:
        assert fragment in text


def test_placeholder_sign_language_does_not_return_to_definition():
    text = _bar_text()

    forbidden_fragments = [
        r"\epsilon_i = \sum_{j=0}^{i-1} |\phi_j| + \sum_{j=0}^{i-1} 1",
        r"\sigma_{ij} is a sign determined by",
        r"Sign: $(-1)^{\epsilon_i}$",
    ]

    for fragment in forbidden_fragments:
        assert fragment not in text


def test_harvest_matrix_marks_ordered_bar_row_applied_after_pass():
    text = MATRIX.read_text()

    assert "C Ordered chiral bar construction" in text
    assert "Pass 506" in text
    assert "applied for local harvest" in text
