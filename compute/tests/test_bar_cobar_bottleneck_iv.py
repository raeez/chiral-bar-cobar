"""Independent verification for Theorem A / bar-cobar bottlenecks."""

from __future__ import annotations

from sympy import Rational

from compute.lib.bar_cobar_bottleneck_invariants import (
    degree_cutoff_profile,
    divisor_core_summary,
    weight_slices_stabilize,
    t,
)
from compute.lib.independent_verification import independent_verification
from compute.lib.theorem_thm_a_bl_rectification_engine import (
    STANDARD_FAMILIES,
    heisenberg,
    verify_theorem_a_vs_bl,
    verify_theorem_b_vs_bl,
)


@independent_verification(
    claim="lem:degree-cutoff",
    derived_from=[
        "Strong filtration axiom in bar_cobar_adjunction_curved.tex: "
        "mu_r(F^{i_1},...,F^{i_r}) subset F^{i_1+...+i_r}",
        "Manuscript proof of lem:degree-cutoff using the abstract "
        "filtration inclusion",
    ],
    verified_against=[
        "Finite quotient algebra Q[epsilon]/(epsilon^{N+1}) with "
        "epsilon in F^1",
        "Direct monomial survival test epsilon^r = 0 iff r >= N+1",
    ],
    disjoint_rationale=(
        "The proof is an abstract filtered-operation argument. The test "
        "uses the concrete quotient algebra Q[epsilon]/epsilon^{N+1} and "
        "computes survival of monomials directly in the quotient."
    ),
)
def test_degree_cutoff_finite_quotient_model():
    """Only arities r <= N survive in Q[epsilon]/epsilon^{N+1}."""
    for stage in range(1, 8):
        profile = degree_cutoff_profile(stage, max_arity=stage + 3)
        assert all(profile[arity] for arity in range(1, stage + 1))
        assert all(
            not profile[arity]
            for arity in range(stage + 1, stage + 4)
        )


@independent_verification(
    claim="prop:mc4-weight-cutoff",
    derived_from=[
        "MC4 weight-cutoff proof in bar_cobar_adjunction_curved.tex using "
        "filtered-subcomplex isomorphisms F_{<=w}C_{N+1}->F_{<=w}C_N",
        "Corollary cor:mc4-surjective-criterion",
    ],
    verified_against=[
        "Finite two-term rational chain complexes Q^2 -> Q by weight",
        "Exact rank computation of H^0 and H^1 on every weight slice",
        "Identity transition on slices w <= N in the explicit toy tower",
    ],
    disjoint_rationale=(
        "The manuscript proof is categorical and uses the Milnor/"
        "Mittag-Leffler criterion. The test builds explicit rational "
        "matrices by weight and computes cohomology ranks directly."
    ),
)
def test_mc4_weight_slices_stabilize_in_explicit_tower():
    """Weight slices stabilize stagewise in an exact finite matrix tower."""
    assert weight_slices_stabilize(max_stage=9)


@independent_verification(
    claim="thm:divisor-core-calculus-inv",
    derived_from=[
        "PID ideal proof of divisor cores in bar_cobar_adjunction_inversion.tex",
        "Chinese remainder theorem criterion stated in "
        "thm:divisor-core-calculus-inv",
    ],
    verified_against=[
        "Linear algebra inside Q[t]/((t-1)^2(t+2)) using coefficient vectors",
        "Rank formula dim(U cap V)=dim U + dim V - dim(U+V)",
        "Direct gcd/lcm computation over Q[t] by sympy Poly",
    ],
    disjoint_rationale=(
        "The theorem proof argues with ideals in a PID. The test embeds "
        "the cores as concrete subspaces of a three-dimensional quotient "
        "module and verifies exactness, lattice identities, and splitting "
        "by matrix ranks."
    ),
)
def test_divisor_core_calculus_by_linear_algebra():
    """Divisor-core ranks, lattice operations, and CRT splitting agree."""
    p = (t - 1) ** 2 * (t + 2)
    g1 = t - 1
    g2 = t + 2
    data = divisor_core_summary(p, g1, g2)

    assert data["degree_p"] == 3
    assert data["rank_g1"] == 1
    assert data["rank_g2"] == 1
    assert data["quotient_dim_g1"] == data["quotient_degree_g1"] == 2
    assert data["quotient_dim_g2"] == data["quotient_degree_g2"] == 2

    assert data["rank_gcd"] == 0
    assert data["intersection_rank"] == data["rank_gcd"]
    assert data["rank_lcm"] == 2
    assert data["sum_rank"] == data["rank_lcm"]

    assert data["g1_splits"] is False
    assert data["g2_splits"] is True


@independent_verification(
    claim="thm:bar-cobar-platonic",
    derived_from=[
        "Theorem A Platonic statement in bar_cobar_adjunction_inversion.tex",
        "Vallette/Beilinson-Drinfeld proof lane cited by the manuscript",
    ],
    verified_against=[
        "Booth-Lazarev Global Koszul duality scope engine",
        "Cross-family standard landscape check in "
        "theorem_thm_a_bl_rectification_engine.py",
        "Heisenberg finite Koszul witness",
    ],
    disjoint_rationale=(
        "The manuscript derives the Platonic theorem through the chiral "
        "bar-cobar and Verdier lane. The test asks an independently "
        "encoded model-structure scope engine whether the algebraic "
        "bar-cobar counit is confirmed, not contradicted, and not confused "
        "with the geometric Verdier claim."
    ),
)
def test_bar_cobar_platonic_algebraic_scope_cross_family():
    """BL-compatible algebraic content agrees across all standard families."""
    for family in STANDARD_FAMILIES:
        result = verify_theorem_a_vs_bl(family)
        assert result["part_1_bar_cobar_inversion"]["bl_assessment"] == (
            "CONFIRMED"
        )
        assert result["overall"]["bl_confirms"] is True
        assert result["overall"]["bl_contradicts"] is False
        assert result["overall"]["bl_supersedes"] is False
        assert "NOT ADDRESSED" in result[
            "part_2_verdier_intertwining"
        ]["bl_assessment"]


@independent_verification(
    claim="thm:koszul-reflection",
    derived_from=[
        "Unified Theorem A proof in theorem_A_infinity_2.tex",
        "Spectral-sequence collapse cited for the Koszul-locus counit",
    ],
    verified_against=[
        "Booth-Lazarev derived unit/counit comparison encoded in "
        "verify_theorem_b_vs_bl",
        "Heisenberg genus-zero Koszul witness with kappa=1",
    ],
    disjoint_rationale=(
        "The manuscript proof uses the chiral spectral-sequence and "
        "Positselski collapse lane. The test verifies the same restricted "
        "counit clause through the model-categorical BL comparison on the "
        "finite Heisenberg witness."
    ),
)
def test_koszul_reflection_counit_clause_on_finite_witness():
    """The Koszul-locus counit clause is confirmed on the Heisenberg witness."""
    result = verify_theorem_b_vs_bl(heisenberg())
    assert result["on_koszul_locus"] is True
    assert result["theorem_b_applies"] is True
    assert result["bl_assessment"] == "CONFIRMED"
    assert result["proof_comparison"]["independent"] is True
    assert heisenberg().kappa == Rational(1)
