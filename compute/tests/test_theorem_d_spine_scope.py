"""Guards for Theorem D theorem-spine scoping."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CLAUDE = ROOT / "CLAUDE.md"
INTRODUCTION = ROOT / "chapters/theory/introduction.tex"
CONCORDANCE = ROOT / "chapters/connections/concordance.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_claude_theorem_d_row_has_curved_scalar_multichannel_split():
    text = _text(CLAUDE)
    required = [
        r"**D**",
        r"$\operatorname{Obs}^{\mathrm{def}}_g\in H^2(\operatorname{Def}_g)$",
        r"$\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1}=+\kappa\lambda_1$",
        r"$\mathfrak O_g^K=\kappa\lambda_{-1}(\mathbb E_g)$",
        r"$\operatorname{ch}_g(\mathfrak O_g^K)=(-1)^g\kappa\lambda_g$",
        r"$F_g=\kappa\lambda_g^{\mathrm{FP}}+\delta F_g^{\mathrm{cross}}$",
        r"$H_D^{\mathrm{tr}}$ for deformation-to-$K$ comparison",
    ]
    for fragment in required:
        assert fragment in text


def test_main_introduction_part_map_scopes_theorem_d():
    text = _text(INTRODUCTION)
    required = [
        "Theorem D: genus-one deformation class, higher-genus K-theory class, and their conditional comparison",
        r"curved fiber identity $m_1^2=[m_0,-]$",
        r"scalar diagonal $\operatorname{tr}_{\mathrm{diag}}(m_0)=\kappa\omega_g$",
    ]
    for fragment in required:
        assert fragment in text

    assert r"Theorem D $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$" not in text


def test_concordance_integrability_paragraph_does_not_call_ahat_c1():
    text = _text(CONCORDANCE)
    required = [
        r"Theorem~D is a four-stage integrability comparison",
        r"$H_D^1$ gives $\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1} =\kappa\lambda_1$",
        r"$H_D^K$ gives $\mathfrak O_g^K=\kappa\lambda_{-1}(\mathbb E_g)$",
        r"$H_D^{\mathrm{graph}}$ gives $F_g=\kappa\lambda_g^{\mathrm{FP}} +\delta F_g^{\mathrm{cross}}$",
        r"The $\hat{A}$-genus expression is the scalar characteristic-class trace",
        "The bundle and its first Chern class remain distinct preceding objects",
    ]
    for fragment in required:
        assert fragment in text

    forbidden = [
        r"Theorem~D is the \emph{integrability condition}: $\mathrm{obs}_g = \kappa \cdot \lambda_g$",
        r"The $\hat{A}$-genus is the \emph{first Chern class}",
    ]
    for fragment in forbidden:
        assert fragment not in text


def test_harvest_matrix_records_spine_pass():
    text = _text(MATRIX)
    assert "G Theorem D / modular tower" in text
    assert "Pass 510" in text
