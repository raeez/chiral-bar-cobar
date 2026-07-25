"""Semantic guards for the residual presentation/bar/Verdier surfaces."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

SURFACES = (
    "appendices/combinatorial_frontier.tex",
    "appendices/nonlinear_modular_shadows.tex",
    "appendices/notation_index.tex",
    "chapters/connections/editorial_constitution.tex",
    "chapters/connections/feynman_connection.tex",
    "chapters/connections/thqg_introduction_supplement.tex",
    "chapters/connections/thqg_introduction_supplement_body.tex",
    "chapters/connections/thqg_open_closed_realization.tex",
    "chapters/examples/bar_complex_tables.tex",
    "chapters/examples/beta_gamma.tex",
    "chapters/examples/heisenberg_eisenstein.tex",
    "chapters/examples/lattice_foundations.tex",
    "chapters/examples/w3_holographic_datum.tex",
    "chapters/theory/algebraic_foundations.tex",
    "chapters/theory/bar_cobar_adjunction_curved.tex",
    "chapters/theory/compact_completed_mc3_comparison_platonic.tex",
    "chapters/theory/en_koszul_duality.tex",
    "chapters/theory/existence_criteria.tex",
    "chapters/theory/higher_genus_foundations.tex",
    "chapters/theory/poincare_duality_quantum.tex",
    "standalone/introduction_full_survey.tex",
    "standalone/N4_mc4_completion.tex",
    "standalone/programme_summary_sections9_14.tex",
    "standalone/survey_modular_koszul_duality_v2.tex",
)

AI = (
    r"(?:\\cA|\\mathcal\{A\}|(?<![A-Za-z\\])A)"
    r"(?:_\{[^}]+\}|_[A-Za-z\\]+)?"
    r"(?:\^\{\\mathrm\{?\s*i\}?\}|\^\{i\}|\^i)"
)

DIRECT_AI_FROM_BAR_COHOMOLOGY = re.compile(
    AI
    + r"\s*(?::=|=|\\coloneqq)\s*"
    + r"H\^(?:\\bullet|\*|\{\\bullet\})\s*"
    + r"(?:\\!\s*)?(?:\\bigl)?\s*\(?(?:\\barB|\\bar\{B\}|B)",
    re.DOTALL,
)
BAR_COHOMOLOGY_AS_AI = re.compile(
    r"(?:bar cohomology|cohomology coalgebra)\s+"
    r"(?:is|gives|defines|equals)\s+(?:the\s+)?(?:intrinsic\s+)?"
    r"(?:Koszul[- ]dual\s+|bar[- ]dual\s+)?(?:coalgebra\s+)?" + AI,
    re.DOTALL | re.IGNORECASE,
)
SECOND_COBAR_TO_PARTNER = re.compile(
    r"(?:after|followed by) (?:a )?(?:completed )?cobar"
    r".{0,120}(?:\\cA|\\mathcal\{A\}|A)\^!",
    re.DOTALL | re.IGNORECASE,
)


def source(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def local_windows(text: str, radius: int = 2) -> list[str]:
    lines = text.splitlines()
    return ["\n".join(lines[index : index + radius + 1]) for index in range(len(lines))]


def test_residual_surfaces_keep_presentation_and_bar_cohomology_typed_apart():
    offenders: list[str] = []
    for relative in SURFACES:
        text = source(relative)
        for block in local_windows(text):
            if DIRECT_AI_FROM_BAR_COHOMOLOGY.search(block):
                offenders.append(f"direct:{relative}")
                break
            if BAR_COHOMOLOGY_AS_AI.search(block):
                offenders.append(f"prose:{relative}")
                break
            if SECOND_COBAR_TO_PARTNER.search(block):
                offenders.append(f"cobar:{relative}")
                break
    assert offenders == []


def test_priority_surfaces_display_the_canonical_comparison_chain():
    required = {
        "appendices/notation_index.tex": (
            r"\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)",
            r"q_\cA\colon\cA^{\mathrm i}\to B_X(\cA)",
            r"K_X(\cA)",
            r"\VD(q_\cA)",
            r"\nu_\cA\colon K_X(\cA)\to\cA^!",
        ),
        "chapters/connections/thqg_open_closed_realization.tex": (
            r"\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)",
            r"q_\cA\colon\cA^{\mathrm i}\to B^{\mathrm{ch}}(\cA)",
            r"K_X(\cA)=\mathbb D_{\Ran}B^{\mathrm{ch}}(\cA)",
            r"\mathbb D(q_\cA)",
            r"\nu_\cA\colon K_X(\cA)\to\cA^!",
        ),
        "chapters/theory/compact_completed_mc3_comparison_platonic.tex": (
            r"A^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)",
            r"q_A\colon A^{\mathrm i}\longrightarrow\bar B_X(A)",
            r"K_X(A):=\mathbb D_{\Ran}\bar B_X(A)",
            r"\mathbb D(q_A)",
            r"\nu_A\colon K_X(A)\to A^!",
        ),
        "chapters/theory/higher_genus_foundations.tex": (
            r"\mathcal A_i^{\mathrm i}=C_X(s^{-1}V_i,s^{-2}R_i)",
            r"q_i\colon\mathcal A_i^{\mathrm i}\longrightarrow",
            r"\mathbb D(q_i)\colon K_X(\mathcal A_i)",
        ),
    }
    for relative, fragments in required.items():
        text = source(relative)
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {relative}"


def test_cohomological_suspension_is_uniform_in_foundational_definitions():
    for relative in (
        "chapters/theory/algebraic_foundations.tex",
        "chapters/theory/existence_criteria.tex",
    ):
        text = source(relative)
        assert re.search(r"C(?:_\{\\mathcal D\}|_X)?\(s\^{-1\}V,s\^{-2\}R\)", text)
        forbidden = (
            r"C_{\mathcal D}(sV,s^2R)",
            r"T^c_{\mathcal D}(sV)",
            r"\Lambda^c(sV)",
            r"(sV)^{\otimes",
        )
        for fragment in forbidden:
            assert fragment not in text, f"{fragment!r} remains in {relative}"


def test_n4_summary_separates_presentation_coalgebra_and_finite_dual_algebra():
    text = source("standalone/N4_mc4_completion.tex")
    for fragment in (
        r"A^{\mathrm i}=C(s^{-1}V,s^{-2}R)",
        r"q_A\colon A^{\mathrm i}\to B(A)",
        r"\Omega(A^{\mathrm i})\to A",
        r"quadratic dual algebra on",
        r"$sV^*$ with relations generated by~$s^2R^\perp$",
    ):
        assert fragment in text
