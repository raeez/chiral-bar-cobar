"""
Guardrails for Theorem B scope separation and the curved genus >= 1
homotopy surface.

The live theorem surface separates four claims:

1. thm:chiral-positselski-at-each-weight is conditional on the
   finite-window de Rham chiral model. Its finite object is F^{<=w}C,
   not a quotient using the low-weight piece in the denominator.
2. thm:chiral-positselski-weight-completed is conditional on CP1--CP3
   for strict Mittag-Leffler completed chiral coalgebra towers.
3. prop:chiral-positselski-raw-direct-sum-class-M-false is a raw
   direct-sum obstruction: S4 is only the first nonzero term; the
   obstruction is the nonterminating harmonic family.
4. thm:curved-chain-homotopy-trichotomy uses a strict
   complete-filtered mapping complex Rlim Hom for the fixed tower, not
   the unrestricted mapping object of pro-Ch.
"""

from __future__ import annotations

from pathlib import Path

from compute.lib.independent_verification import independent_verification


ROOT = Path(__file__).resolve().parents[2]
THEOREM_B_TEX = ROOT / "chapters/theory/theorem_B_scope_platonic.tex"
CODERIVED_TEX = ROOT / "chapters/theory/coderived_models.tex"
BAR_COBAR_INVERSION_TEX = (
    ROOT / "chapters/theory/bar_cobar_adjunction_inversion.tex"
)


def _window_around(text: str, label: str, radius: int = 700) -> str:
    idx = text.index(label)
    return text[max(0, idx - radius) : idx + radius]


def _forward_window_from(text: str, label: str, radius: int = 2200) -> str:
    idx = text.index(label)
    return text[idx : idx + radius]


def _env_block(text: str, label: str) -> str:
    idx = text.index(label)
    begin_candidates = [
        text.rfind("\\begin{theorem}", 0, idx),
        text.rfind("\\begin{proposition}", 0, idx),
        text.rfind("\\begin{corollary}", 0, idx),
    ]
    begin = max(begin_candidates)
    end_candidates = [
        text.find("\\end{theorem}", idx),
        text.find("\\end{proposition}", idx),
        text.find("\\end{corollary}", idx),
    ]
    end = min(candidate for candidate in end_candidates if candidate != -1)
    return text[begin:end]


@independent_verification(
    claim="thm:curved-chain-homotopy-trichotomy",
    derived_from=[
        "raw direct sum is finite-support data while strict completion "
        "is finite-window tower data",
        "finite windows stabilize in the standard weight-truncation "
        "tower",
        "strict continuous mapping complexes are Rlim of finite-stage "
        "Hom complexes with Milnor lim^1 control",
    ],
    verified_against=[
        "lem:complete-filtered-comparison for square-zero total "
        "complexes",
        "prop:standard-strong-filtration eventual constancy on each "
        "finite total-weight window",
        "CP1--CP3 proved on the strict Mittag-Leffler completed "
        "chiral coalgebra surface",
    ],
    disjoint_rationale=(
        "Finite support versus completion is linear algebra; "
        "finite-window stabilization is conformal-weight bookkeeping; "
        "Milnor control is homological algebra. They test different "
        "failure modes."
    ),
)
def test_curved_chain_homotopy_trichotomy_surface_is_strict_complete_filtered():
    tex = CODERIVED_TEX.read_text()
    window = _window_around(tex, "\\label{def:three-curved-chain-surfaces}", 2400)
    assert "strict weight-completed chain surface" in window
    assert "not asserted to be the unrestricted derived" in window
    assert "high-weight tail need not be a subcomplex" in window

    theorem = _window_around(tex, "\\label{thm:curved-chain-homotopy-trichotomy}", 2600)
    assert "square-zero total differential" in theorem
    assert "co/contra theorem" in theorem
    assert "not a formal\nconsequence of the finite-stage theorem" in tex


@independent_verification(
    claim="thm:chiral-positselski-at-each-weight",
    derived_from=[
        "finite low-weight chiral coalgebra F^{<=w}C",
        "bar-degree-plus-weight conilpotency on the finite window",
        "finite-dimensional graded pieces in the finite window",
    ],
    verified_against=[
        "Positselski 2011 classical co/contra correspondence",
        "chiral product/sum exactness hypothesis stated in "
        "thm:chiral-co-contra-correspondence",
    ],
    disjoint_rationale=(
        "The finite-dimensional/conilpotent calculation is internal; "
        "the product/sum exactness is a separate chiral D-module "
        "second-kind condition."
    ),
)
def test_finite_weight_surface_uses_low_weight_subcoalgebra_and_is_conditional():
    tex = THEOREM_B_TEX.read_text()
    window = _env_block(tex, "\\label{thm:chiral-positselski-at-each-weight}")
    assert "\\ClaimStatusConditional" in window
    assert "finite low-weight subobject" in window
    assert "F^{\\leq w}C" in window
    assert "finite-window de Rham chiral model" in window
    assert "product/sum exactness" in window
    assert ("C/F^" + "{<=w}") not in tex
    assert ("C/F^" + "{>w}") not in tex


@independent_verification(
    claim="thm:chiral-positselski-weight-completed",
    derived_from=[
        "CP1 continuous completed curved chiral coalgebra",
        "CP2 coderived category recovered by derived inverse limit",
        "CP3 contraderived category recovered by derived inverse "
        "limit plus product/sum exactness",
    ],
    verified_against=[
        "Keller 2009 complete augmented algebra bar-cobar comparison",
        "thm:completed-bar-cobar-strong square-zero total-complex "
        "Milnor comparison",
    ],
    disjoint_rationale=(
        "Keller works over complete augmented algebras over a field; "
        "the MC4 comparison is a chain-level Milnor argument. Neither "
        "proves the chiral completed co/contra Rlim theorem."
    ),
)
def test_weight_completed_positselski_is_conditional_on_strict_ml_surface():
    tex = THEOREM_B_TEX.read_text()
    window = _env_block(tex, "\\label{thm:chiral-positselski-weight-completed}")
    assert "Continuous chiral Positselski comparison" in window
    assert "\\ClaimStatusConditional" in window
    for token in ("(CP1)", "(CP2)", "(CP3)"):
        assert token in window
    assert "strict Mittag" in window
    assert "not a consequence of quotienting the raw" in tex


def test_off_koszul_ran_uses_named_chiral_positselski_72_package():
    tex = CODERIVED_TEX.read_text()
    theorem = _env_block(tex, "\\label{thm:chiral-bar-cobar-positselski-7-2}")
    assert "\\ClaimStatusConditional" in theorem
    assert "\\mathsf{Pos}^{\\mathrm{ch}}_{7.2}" in theorem
    assert "de Rham realization" in theorem
    assert "second-kind acyclic generators" in theorem
    assert "\\tau_{\\geq 0}C_S" in theorem

    off_koszul_window = _forward_window_from(
        tex, "\\label{thm:off-koszul-ran-inversion}", 5000
    )
    assert "thm:chiral-bar-cobar-positselski-7-2" in off_koszul_window
    assert "chiral adaptation of" not in off_koszul_window
    assert "via the chiral adaptation" not in tex


def test_theorem_b_genus_zero_clause_is_ftm_equivalence_not_definition():
    tex = BAR_COBAR_INVERSION_TEX.read_text()
    theorem = _env_block(tex, "\\label{thm:bar-cobar-inversion-qi}")
    assert "Strict genus-\\(0\\) FTM surface" in theorem
    assert "the following four conditions are equivalent" in theorem
    for token in (
        "chiral Koszul morphism",
        "\\psi_0",
        "\\eta_0",
        "twisted tensor products",
    ):
        assert token in theorem
    assert "non-tautological FTM package" in theorem

    proof_window = _forward_window_from(
        tex, "\\begin{proof}[Dependency-closed proof]", 2200
    )
    assert "not proved by reusing" in proof_window
    assert "FTM equivalence package" in proof_window


@independent_verification(
    claim="prop:chiral-positselski-raw-direct-sum-class-M-false",
    derived_from=[
        "finite-type/completion failure for compatible Virasoro "
        "finite-window families",
        "nonterminating harmonic family {delta_r}_{r>=4}; S4 is only "
        "the first detected nonzero term",
    ],
    verified_against=[
        "direct numerical evaluation of S4(Vir_c) at c=100",
        "representation-theoretic completion obstruction for Virasoro "
        "mode families",
    ],
    disjoint_rationale=(
        "The S4 check is a shadow-tower computation; the mode-family "
        "completion obstruction is a representation-theoretic finite "
        "support failure."
    ),
)
def test_raw_direct_sum_class_m_failure_uses_infinite_family_not_s4_alone():
    c = 100
    s4 = 10.0 / (c * (5 * c + 22))
    expected_s4 = 1.9157e-4
    assert abs(s4 - expected_s4) / expected_s4 < 5e-4

    tex = THEOREM_B_TEX.read_text()
    window = _forward_window_from(
        tex, "\\label{prop:chiral-positselski-raw-direct-sum-class-M-false}", 3600
    )
    assert "first detected term" in window
    assert "nonterminating" in window
    assert "not an element of the raw" in window


def test_no_stale_quotient_truncation_notation_in_guarded_surfaces():
    theorem_b = THEOREM_B_TEX.read_text()
    tests = Path(__file__).read_text()
    stale_tokens = (
        "C/F^" + "{<=w}",
        "hatC = lim_w C" + "/F",
        "{C/F^" + "{<=w}}",
    )
    for stale in stale_tokens:
        assert stale not in theorem_b
        assert stale not in tests
