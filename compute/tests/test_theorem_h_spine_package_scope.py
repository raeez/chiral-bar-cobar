"""Guards for Theorem H theorem-spine hypothesis discipline."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CLAUDE = ROOT / "CLAUDE.md"
FIVE_THEOREMS = ROOT / "standalone/five_theorems_modular_koszul.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_claude_theorem_h_row_names_full_hh_package():
    text = _text(CLAUDE)
    required = [
        r"**H**",
        r"Theorem H remains conditional on its \(H_H\) package",
        r"for each family datum $H_H(A_b;S)$",
        r"$C^\bullet_{\mathrm{ch}}(A_b,A_b)=R\!\operatorname{Hom}_{A_b^e}(A_b,A_b)$",
        "strong deformation retract",
        r"$\operatorname{Supp}\mathrm{ChirHoch}^\bullet(A_b)\subseteq S$",
        r"$\operatorname{Conv}(B_X(A_b),A_b)\xrightarrow{\sim}C^\bullet_{\mathrm{ch}}(A_b,A_b)$",
        "bounded-to-chart quasi-isomorphism",
    ]
    for fragment in required:
        assert fragment in text

    assert "Theorem H remains conditional on its $H_3$ package" not in text
    assert r"$\mathrm{ChirHoch}^\bullet \subset \{0,1,2\}$" not in text


def test_five_theorems_uses_family_retract_and_derived_bimodule_center():
    text = _text(FIVE_THEOREMS)
    required = [
        r"$H_H(\cA;S)$ consists of a complete filtered cochain model $Q_\cA$",
        r"R\!\operatorname{Hom}_{A_b\otimes A_b^{\mathrm{op}}}(A_b,A_b)",
        r"\operatorname{Conv}(B_X(\cA),\cA)",
        r"p_\cA\iota_\cA=\id_{K_{\cA,S}}",
        r"\operatorname{Supp}\ChirHoch^\bullet(\cA)\subseteq S",
        "bounded-to-chart quasi-isomorphism",
    ]
    for fragment in required:
        assert fragment in text

    assert r"\ChirHoch^*(\cA) = H^*(\mathrm{CoDer}(\barB(\cA)))" not in text


def test_theorem_h_support_is_family_indexed():
    text = _text(FIVE_THEOREMS)
    required = [
        r"Fix a finite set $S\subset\mathbb Z$",
        r"\ChirHoch^n(\cA)\cong H^n(K_{\cA,S})",
        r"P_\cA(t) =\sum_{n\in S}\dim H^n(K_{\cA,S})t^n",
        r"$H_H(\cA;S_\cA)$",
    ]
    for fragment in required:
        assert fragment in text

    assert r"\operatorname{Supp}\ChirHoch^\bullet(\cA)\subseteq\{0,1,2\}" not in text


def test_harvest_matrix_records_hh_spine_pass():
    text = _text(MATRIX)
    assert "E Theorem H / Hochschild" in text
    assert "Pass 511" in text
