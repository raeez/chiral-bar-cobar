"""
Guardrails for Theorem B scope separation and the curved genus >= 1
homotopy surface.

The live theorem surface separates four claims:

1. thm:chiral-positselski-at-each-weight is conditional on the
   finite-window de Rham chiral model. Its finite object is F^{<=w}C,
   not a quotient using the low-weight piece in the denominator.
2. thm:chiral-positselski-weight-completed is conditional on CP1--CP3
   for strict Mittag-Leffler completed chiral coalgebra towers.
3. prop:chiral-positselski-raw-direct-sum-class-M-false is the linear
   separation between finite-support direct sums and completed
   inverse-limit mode families; it carries no co/contra conclusion.
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
ALGEBRAIC_FOUNDATIONS_TEX = (
    ROOT / "chapters/theory/algebraic_foundations.tex"
)
CONCORDANCE_TEX = ROOT / "chapters/connections/concordance.tex"
EDITORIAL_CONSTITUTION_TEX = (
    ROOT / "chapters/connections/editorial_constitution.tex"
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
    assert "F^{\\leq w}C" in window
    assert "finite-window de Rham chiral" in window
    assert "finite-stage chiral Positselski datum" in window
    assert "\\mathsf{Pos}^{\\mathrm{ch}}_{\\mathrm{co\\text{-}ctr}}" in window
    assert "Transition compatibility" in window
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
    assert "Continuous fixed-coalgebra co--contra comparison" in window
    assert "\\ClaimStatusConditional" in window
    for token in ("(CP1)", "(CP2)", "(CP3)"):
        assert token in window
    assert "strict Mittag" in window
    assert "retains the transition maps and topology" in tex


def test_off_koszul_ran_uses_fixed_coalgebra_and_typed_twisting_packages():
    tex = CODERIVED_TEX.read_text()
    theorem = _env_block(tex, "\\label{thm:chiral-bar-cobar-positselski-7-2}")
    assert "\\ClaimStatusConditional" in theorem
    assert "\\mathsf{Pos}^{\\mathrm{ch}}_{\\mathrm{co\\text{-}ctr}}" in theorem
    assert "de Rham realization" in theorem
    assert "second-kind acyclic" in theorem
    assert "generators" in theorem
    assert "D^{\\mathrm{co}}" in theorem
    assert "D^{\\mathrm{ctr}}" in theorem
    assert "\\Omega^{\\mathrm{ch}}(C_S)" not in theorem

    off_koszul_window = _forward_window_from(
        tex, "\\label{thm:off-koszul-ran-inversion}", 5000
    )
    assert "D^{\\mathrm{co}}(C\\text{-}\\mathrm{CoFact})" in off_koszul_window
    assert "D^{\\mathrm{ctr}}(C\\text{-}\\mathrm{ContraFact})" in off_koszul_window
    assert "def:acyclic-chiral-twisting-comparison" in tex
    assert "\\mathsf{Tw}^{\\mathrm{ch}}_{\\mathrm{acyc}}" in off_koszul_window
    assert "Theorem~6.5" in off_koszul_window
    assert "is an isomorphism in\n$D^{\\mathrm{co}}" not in off_koszul_window


def test_foundational_koszul_recognition_uses_the_quadratic_coalgebra():
    tex = ALGEBRAIC_FOUNDATIONS_TEX.read_text()

    construction = _forward_window_from(
        tex, "\\label{const:quadratic-dual}", 3000
    )
    assert "A^i:=C(s^{-1}V,s^{-2}R)" in construction
    assert "T^c(s^{-1}V)" in construction
    assert "A(V^*,R^\\perp)" in construction
    assert "T^c(sV^*)" not in tex

    pair = _forward_window_from(
        tex, "\\label{def:koszul-pair-classical}", 3200
    )
    assert "A_j^i\\longrightarrow B(A_j)" in pair
    assert "\\Omega(A_j^i)\\longrightarrow A_j" in pair
    assert "B(A_j)\\longrightarrow A_j^i" not in pair
    for reference in (
        "Theorem~2.3.2",
        "Theorem~3.4.6",
        "Corollary~2.3.4",
    ):
        assert reference in pair

    chiral_definition = _forward_window_from(
        tex, "\\label{def:koszul-chiral-algebra}", 2200
    )
    chiral_definition_flat = " ".join(chiral_definition.split())
    assert "Type signature: Open quadrant" in chiral_definition_flat
    assert "(\\cA,\\cA^i,\\kappa_\\cA,F_\\bullet)" in chiral_definition_flat
    assert "chiral Koszul morphism" in chiral_definition_flat

    recognition = _window_around(
        tex, "\\label{rem:equivalent-formulations-koszul}", 5000
    )
    recognition_flat = " ".join(recognition.split())
    assert "\\ClaimStatusConditional" in recognition_flat
    assert "H_{\\mathrm{CL}}(\\cA,\\cA^i,\\kappa_\\cA)" in recognition_flat
    assert "\\cA^i\\longrightarrow\\barB_X(\\cA)" in recognition_flat
    assert "\\Omega_X(\\cA^i)\\longrightarrow\\cA" in recognition_flat
    assert (
        "universal quasi-free resolution for every augmented dg algebra"
        in recognition_flat
    )


def test_theorem_b_is_typed_quadratic_koszul_recognition():
    tex = BAR_COBAR_INVERSION_TEX.read_text()
    theorem = _env_block(tex, "\\label{thm:bar-cobar-inversion-qi}")
    theorem_flat = " ".join(theorem.split())
    assert "Quadratic Koszul recognition" in theorem_flat
    assert "\\ClaimStatusConditional" in theorem_flat
    assert "Type signature: Open quadrant" in theorem_flat
    assert "H_{\\mathrm{CL}}(A,A^{\\mathrm i},\\tau_{\\mathrm i})" in theorem_flat
    assert (
        "A^{\\mathrm i}=C(s^{-1}V,s^{-2}R)\\subset T^c(s^{-1}V)"
        in theorem_flat
    )
    assert "q_A\\colon A^{\\mathrm i}\\longrightarrow B_X(A)" in theorem_flat
    assert "the following conditions are equivalent" in theorem_flat
    for token in (
        "q_A",
        "\\Omega_X(A^{\\mathrm i})\\longrightarrow A",
        "K^L_{\\tau_{\\mathrm i}}",
        "K^R_{\\tau_{\\mathrm i}}",
        "quadratic Koszul diagonal",
    ):
        assert token in theorem_flat
    assert "D^{\\mathrm{co}}" not in theorem_flat
    assert "C_{\\mathcal A}:=" not in theorem_flat


def test_scope_chapter_uses_q_a_and_keeps_neighboring_lanes_typed():
    tex = THEOREM_B_TEX.read_text()
    opening = tex[:9000]
    assert "Theorem~B: quadratic Koszul recognition" in tex
    assert "q_A\\colon A^{\\mathrm i}\\longrightarrow B_X(A)" in opening
    assert "\\varepsilon_A\\colon\\Omega_XB_X(A)\\longrightarrow A" in opening
    assert "belongs to Theorem~A" in opening
    assert "Theorem~5.2" in opening
    assert "Theorem~6.5" in opening

    theorem = _env_block(
        tex, "\\label{thm:theorem-B-scope-quadratic-recognition}"
    )
    theorem_flat = " ".join(theorem.split())
    for token in (
        "Type signature: Open quadrant",
        "H_{\\mathrm{CL}}(A,A^{\\mathrm i},\\tau_{\\mathrm i})",
        "q_A\\colon A^{\\mathrm i}\\to B_X(A)",
        "\\Omega_X(A^{\\mathrm i})\\to A",
        "K^L_{\\tau_{\\mathrm i}}",
        "K^R_{\\tau_{\\mathrm i}}",
        "quadratic Koszul diagonal",
    ):
        assert token in theorem_flat

    retired = (
        "Theorem~B (chiral Positselski)",
        "two distinct ``Theorem~B'' statements",
        "Theorem B as $\\eta_C",
        "chiral Positselski (Theorem~B)",
        "Module-level Theorem B",
    )
    for phrase in retired:
        assert phrase not in tex


def test_concordance_separates_fixed_coalgebra_and_algebra_lanes():
    concordance = CONCORDANCE_TEX.read_text()
    start = concordance.index(r"\emph{Fixed-coalgebra second-kind scope.}")
    end = concordance.index(
        r"\subsection{The Lagrangian form of complementarity}", start
    )
    window = concordance[start:end]
    assert "D^{\\mathrm{co}}(C\\text{-}\\mathrm{CoFact})" in window
    assert "D^{\\mathrm{ctr}}(C\\text{-}\\mathrm{ContraFact})" in window
    assert "Theorem~5.2" in window
    assert "Theorem~6.5" in window
    assert "\\mathsf{Tw}^{\\mathrm{ch}}_{\\mathrm{acyc}}" in window
    assert "\\Omega_X \\barB_X(\\cA)" not in window

    editorial = EDITORIAL_CONSTITUTION_TEX.read_text()
    h1_start = editorial.index(
        r"\textbf{H1\,: fixed-coalgebra coderived formalism"
    )
    h1_end = editorial.index(r"\textbf{H2\,", h1_start)
    h1 = editorial[h1_start:h1_end]
    assert "fixed chiral CDG-coalgebra" in h1
    assert "\\ClaimStatusOpen" in h1
    assert "\\mathsf{Tw}^{\\mathrm{ch}}_{\\mathrm{acyc}}" in h1


@independent_verification(
    claim="prop:chiral-positselski-raw-direct-sum-class-M-false",
    derived_from=[
        "finite-support direct sum inside the product completion",
        "compatible partial sums define the all-one inverse-limit "
        "point",
    ],
    verified_against=[
        "direct finite-support calculation for the all-one sequence",
        "Virasoro mode-pair specialization",
    ],
    disjoint_rationale=(
        "The first path is pure linear algebra; the second identifies "
        "the abstract basis with explicit Virasoro mode pairs."
    ),
)
def test_mode_family_separates_direct_sum_from_product_completion():
    tex = THEOREM_B_TEX.read_text()
    window = _forward_window_from(
        tex, "\\label{prop:chiral-positselski-raw-direct-sum-class-M-false}", 3600
    )
    assert "v_k=L_{-k}\\mathbf1" in window
    assert "\\mathbf e_k=s^{-1}v_k\\otimes s^{-1}v_k" in window
    assert "V_\\oplus=\\bigoplus" in window
    assert "V_\\Pi=\\prod" in window
    assert "infinite weight support" in window


def test_feigin_frenkel_center_topology_leaves_cp2_cp3_separate():
    tex = THEOREM_B_TEX.read_text()
    definition = _forward_window_from(
        tex, "\\label{def:ff-center-weight-completion-theorem-b}", 2200
    )
    assert "\\widehat{\\mathfrak z}_{\\mathrm{wt}}" in definition
    assert "\\prod_{w\\geq0}\\mathfrak z" in definition
    assert "supplies the\ntopological part of \\textup{(CP1)}" in definition
    assert "(CP2)" in definition and "(CP3)" in definition

    lemma = _window_around(
        tex, "\\label{lem:ff-center-finite-weight-windows}", 2600
    )
    assert "\\ClaimStatusProvedHere" in lemma
    assert "finite-dimensional" in lemma
    assert "strict surjections" in lemma
    assert "additional assertions" in lemma

    family_window = _forward_window_from(
        tex, "\\label{cor:positselski-applicable-families}", 3600
    )
    assert "applicability criteria" in family_window
    assert "def:ff-center-weight-completion-theorem-b" in family_window
    assert "lem:ff-center-finite-weight-windows" in family_window
    assert "applies once this" in family_window


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


def test_theorem_b_setup_separates_raw_curvature_from_scalar_projection():
    tex = THEOREM_B_TEX.read_text()
    setup = _forward_window_from(
        tex, "\\label{sec:weight-filtration-chiral-bar}", 2600
    )
    assert "d^{(g)\\,2}=h^{(g)}\\ast(-)" in setup
    assert "m_1^{(g)\\,2}(a)" in setup
    assert (
        "m_2(m_0^{(g)},a)-m_2(a,m_0^{(g)})"
        in setup
    )
    assert "\\operatorname{tr}_{\\mathrm{diag}}" in setup
    assert "\\kappa(\\cA)\\,\\omega_g" in setup
    assert "scalar display is its Hodge projection" in setup
    assert "h^{(g)} = \\kappa \\cdot \\omega_g" not in tex
