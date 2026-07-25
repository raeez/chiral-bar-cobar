"""Guards for Theorem A/B master-row ambient discipline."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CLAUDE = ROOT / "CLAUDE.md"
MAIN = ROOT / "main.tex"
PREFACE = ROOT / "chapters/frame/preface.tex"
GUIDE = ROOT / "chapters/frame/guide_to_main_results.tex"
TOWER = ROOT / "chapters/frame/open_beilinson_tower_platonic.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_claude_theorem_a_row_records_universal_ran_reconstruction():
    text = _text(CLAUDE)
    required = [
        r"**A**",
        "enhanced associative bar--cobar equivalence in the pro-nilpotent Francis--Gaitsgory Ran ambient",
        r"universal reconstruction $\Omega_XB_X(A_b)\xrightarrow{\sim}A_b$",
        r"$K_X(A_b)=\mathbb D_{\operatorname{Ran}}B_X(A_b)$",
        r"$H_{\mathrm{fact}}$ for factorization closure",
        r"$H_{\mathrm{conv}}$ for completed chain realization",
        r"$H_{\mathrm{VD}}$ for Verdier transport and biduality",
    ]
    for fragment in required:
        assert fragment in text

    assert "universal reconstruction" in text


def test_claude_theorem_b_row_is_quadratic_recognition():
    text = _text(CLAUDE)
    required = [
        r"**B**",
        "quadratic Koszul recognition for a chosen presentation",
        r"$q_{A_b}\colon A_b^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)\to B_X(A_b)$",
        r"$\Omega_X(A_b^{\mathrm i})\to A_b$",
        "connected positive-weight quadratic presentation",
        "finite-window comparison",
        "exhaustive complete filtrations",
        r"$H_{\mathrm{PBW}}^{\mathrm{det}}$",
        r"$H_{\mathrm{CL}}(A_b,A_b^{\mathrm i},\tau_{\mathrm i})$",
    ]
    for fragment in required:
        assert fragment in text

    assert "The comparison $q_{A_b}" in text


def test_frontmatter_propagates_the_a_b_map_distinction():
    guide = _text(GUIDE)
    tower = _text(TOWER)
    for text in (guide, tower):
        assert "universal reconstruction" in text
        assert r"q_\cA\colon\cA^{\mathrm i}" in text
        assert r"B_X(\cA)" in text
        assert "Quadratic Koszul recognition" in text
        assert "fixed curved coalgebra" in text or "fixed-coalgebra" in text


def test_abstract_and_preface_begin_from_the_two_distinct_maps():
    main = _text(MAIN)
    preface = _text(PREFACE)

    abstract_start = main.index(r"\begin{abstract}")
    abstract_end = main.index(r"\end{abstract}", abstract_start)
    abstract = main[abstract_start:abstract_end]
    assert "Francis and Gaitsgory's pro-nilpotence theorem" in abstract
    assert r"\Omega_XB_X(\cA)\xrightarrow{\sim}\cA" in abstract
    assert r"q_\cA\colon \cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)" in abstract
    assert r"\longrightarrow B_X(\cA)" in abstract

    assert r"\label{thm:preface-point-bar-cobar}" in preface
    assert r"\label{thm:preface-enhanced-ran-reconstruction}" in preface
    assert "Proposition~4.1.2" in preface
    assert r"proof of \cite[Theorem~5.1.1]{Francis2012}" in preface
    assert r"\label{thm:preface-quadratic-recognition}" in preface
    assert r"q_A\colon A^{\mathrm i}\longrightarrow B(A)" in preface
    assert r"\Omega(A^{\mathrm i})\longrightarrow A" in preface
    assert "asks whether the smaller presentation-dependent coalgebra" in preface


def test_frontmatter_types_the_bp_central_identity_and_open_kappa_lane():
    guide = _text(GUIDE)
    tower = _text(TOWER)
    for text in (guide, tower):
        assert "25/3" in text
        assert (
            "c(k)+c(-k-6)=50" in text
            or r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50" in text
        )
        assert "ClaimStatusOpen" in text
        assert "genus-one" in text
        assert "conditional" in text
        assert r"\{0,13,250/3\}" in text or "$(0,13,250/3)$" in text

    def c_bp(k: int) -> Fraction:
        k = Fraction(k)
        return -((2 * k + 3) * (3 * k + 1)) / (k + 3)

    for k in (0, 1, -1, -4):
        assert c_bp(k) + c_bp(-k - 6) == Fraction(50)
    conditional_value = Fraction(1, 6) * Fraction(50)
    assert conditional_value == Fraction(25, 3)


def test_frontmatter_types_the_mukai_eight_as_a_candidate():
    guide = _text(GUIDE)
    tower = _text(TOWER)
    for text in (guide, tower):
        assert r"2c_+(\widetilde H(K3,\mathbb Z))=8" in text
        assert r"H_{\mathrm{chart}}" in text
        assert r"H_{\mathrm{KD}}" in text
        assert r"H_{\mathrm{scalar}}" in text
        assert r"H_{\mathrm{mod}}" in text
        assert r"H_{\mathrm{quant}}" in text
        assert "ClaimStatusConjectured" in text

    assert "Bruinier's \\cite[Lemma~5.1]{Bruinier2002}" in guide
    assert r"N'=\operatorname{lcm}(N,8)" in guide
    assert "Lusztig's root-of-unity construction takes the root order as input" in guide
    assert r"Mukai witness at $K^\kappa=8$" not in guide


def test_main_part_openings_propagate_the_typed_spine():
    main = _text(MAIN)
    assert "Theorem~A: enhanced Ran reconstruction" in main
    assert "Theorem~B: quadratic recognition" in main
    assert r"q_{A_b}\colon A_b^{\mathrm i}\to B_X(A_b)" in main
    assert "Theorem~H is a family-indexed support theorem" in main
    assert r"A row in the proposed $5{\times}5$ matrix is determined by five constructions" in main
    assert r"A modular package $H_{\mathrm{mod}}(A_b)$ consists" in main

    final_start = main.index(r"\label{thm:final-surviving-invariants-diagram}")
    final_end = main.index(r"\end{theorem}", final_start)
    final = main[final_start:final_end]
    assert r"\phi_j^{\mathrm{ord}}:=\phi_j\circ\operatorname{Av}" in final
    assert "complete list of invariants" not in final


def test_harvest_matrix_records_ab_spine_pass():
    text = _text(MATRIX)
    assert "A2 / review Theorem A ambient" in text
    assert "D2 typed Theorem A skeleton" in text
    assert "Pass 513" in text


def test_harvest_matrix_no_longer_lists_theorem_spine_as_residual():
    text = _text(MATRIX)
    assert "The compact A/B/C/D/H theorem spine is synchronized through passes 510--513" in text
    assert "theorem-spine consolidation remains" not in text
    assert "Global theorem-spine integration remains" not in text
    assert "global theorem-spine rewrite remains" not in text
