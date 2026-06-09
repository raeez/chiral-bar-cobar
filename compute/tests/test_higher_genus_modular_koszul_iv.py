"""Independent verification for higher-genus modular Koszul bottlenecks.

The tests in this file are deliberately small finite witnesses.  They do not
reprove the manuscript.  They verify exact consequences of the proof surfaces
from sources disjoint from the local TeX derivations: oriented boundary-chain
signs, finite PBW weight blocks, low-arity shadow recursion, and explicit
W3 graph constants.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

from sympy import Rational, Symbol, cancel, factor, numer, simplify, symbols

from compute.lib.independent_verification import independent_verification


def _boundary_square_coefficients(edge_count: int) -> dict[tuple[int, ...], int]:
    """Compute the signed cellular boundary square on an ordered edge cube.

    For an ordered list of contractible boundary edges, use the standard
    cellular sign convention

        d(e_0, ..., e_{n-1}) = sum_i (-1)^i (e_0, ..., hat e_i, ..., e_{n-1}).

    The terminal key records the remaining ordered edge tuple after two
    contractions.  Every coefficient must vanish.
    """
    edges = tuple(range(edge_count))
    first_boundary: dict[tuple[int, ...], int] = defaultdict(int)
    for i in range(edge_count):
        face = edges[:i] + edges[i + 1 :]
        first_boundary[face] += (-1) ** i

    second_boundary: dict[tuple[int, ...], int] = defaultdict(int)
    for face, coeff in first_boundary.items():
        for j in range(len(face)):
            terminal = face[:j] + face[j + 1 :]
            second_boundary[terminal] += coeff * ((-1) ** j)
    return dict(second_boundary)


@independent_verification(
    claim="comp:heisenberg-g2-fp-grr-check",
    derived_from=[
        "Faber-Pandharipande closed lambda_2 formula with explicit Bernoulli B4",
        "Rank-one Heisenberg scalar characteristic kappa(H_1)=1",
    ],
    verified_against=[
        "GRR A-hat x^4 coefficient extraction from (x/2)/sin(x/2)-1",
        "Exact finite-window scalar free-energy witness in faber_pandharipande_cross_verification",
    ],
    disjoint_rationale=(
        "The manuscript computation derives F_2(H_1) from the explicit "
        "Faber-Pandharipande/Mumford genus-2 coefficient.  The verification "
        "extracts the same coefficient from the GRR/A-hat series and checks "
        "the rank-one scalar free energy directly, while separately recording "
        "that the genus-2 Hodge socle integral 1/5760 is not this coefficient."
    ),
)
def test_heisenberg_g2_fp_grr_disjoint_scalar_window():
    """Rank-one Heisenberg has F_2=7/5760 by both FP and GRR routes."""
    from compute.lib.faber_pandharipande_cross_verification import (
        genus2_heisenberg_fp_grr_disjoint_check,
    )

    witness = genus2_heisenberg_fp_grr_disjoint_check()

    assert witness["claim"] == "comp:heisenberg-g2-fp-grr-check"
    assert witness["heisenberg_kappa"] == Rational(1)
    assert witness["fp_lambda2"] == Rational(7, 5760)
    assert witness["grr_lambda2"] == Rational(7, 5760)
    assert witness["F2_from_fp"] == Rational(7, 5760)
    assert witness["F2_from_grr"] == Rational(7, 5760)
    assert witness["socle_integral_lambda2_lambda1"] == Rational(1, 5760)
    assert witness["socle_integral_is_free_energy"] is False
    assert witness["all_match"] is True


@independent_verification(
    claim="thm:differential-square-zero",
    derived_from=[
        "higher_genus_modular_koszul ambient D_A proof via relative log Fulton--MacPherson compactification",
        "Mok25 normal-crossings degeneration package for the ambient complementarity algebra",
    ],
    verified_against=[
        "Oriented cellular chain identity d^2=0 on an ordered codimension-two boundary cube",
        "Pure edge-contraction sign computation with no moduli-space or TeX dependency",
    ],
    disjoint_rationale=(
        "The manuscript derives ambient square-zero from relative log-FM "
        "geometry and degeneration strata.  This test checks the independent "
        "oriented-chain sign mechanism: every pair of edge contractions occurs "
        "in the two possible orders with opposite signs."
    ),
)
def test_ambient_square_zero_codimension_two_signs():
    """Every two-edge contraction appears twice with opposite signs."""
    for edge_count in range(2, 6):
        coefficients = _boundary_square_coefficients(edge_count)
        assert coefficients
        assert all(value == 0 for value in coefficients.values())

    # Exact pair constants: for i < j, the two signs are
    # (-1)^i(-1)^(j-1) and (-1)^j(-1)^i.
    for i, j in ((0, 1), (0, 2), (1, 3), (2, 4)):
        assert (-1) ** (i + j - 1) + (-1) ** (i + j) == 0


@independent_verification(
    claim="thm:pbw-allgenera-km",
    derived_from=[
        "higher_genus_modular_koszul Kac-Moody PBW proof using Whitehead acyclicity and Killing-form contraction",
        "genus-g PBW enrichment argument in the affine KM theorem body",
    ],
    verified_against=[
        "Finite affine sl2 PBW block computation in pbw_propagation_engine",
        "Szego regular-part residue check and colored-partition enrichment dimensions for genera 1, 2, 3",
    ],
    disjoint_rationale=(
        "The theorem proof is written at the abstract semisimple-g and all-genus "
        "level.  The test verifies a finite affine sl2 model: the regular "
        "propagator has zero residue, enrichment dimensions scale as g times "
        "colored partitions, and d2 has trivial kernel at each positive weight."
    ),
)
def test_km_pbw_allgenera_sl2_enrichment_blocks():
    """Affine sl2 enrichment blocks are killed at E3 for genera 1, 2, 3."""
    from compute.lib.pbw_propagation_engine import (
        AffineSl2GenusgVerification,
        verify_collision_differential_independence,
    )

    assert all(verify_collision_differential_independence(max_genus=3).values())

    for genus in (1, 2, 3):
        verifier = AffineSl2GenusgVerification(genus)
        # Exact first constants for 3-coloured partitions:
        # p_3(1)=3 and p_3(2)=9.
        ok_1, actual_1, expected_1 = verifier.verify_enrichment_dimension(1)
        ok_2, actual_2, expected_2 = verifier.verify_enrichment_dimension(2)
        assert ok_1 and actual_1 == expected_1 == 3 * genus
        assert ok_2 and actual_2 == expected_2 == 9 * genus

        for weight in range(1, 7):
            assert verifier.verify_d2_kills_enrichment(weight)


@independent_verification(
    claim="thm:pbw-allgenera-principal-w",
    derived_from=[
        "higher_genus_modular_koszul principal W PBW proof using stress-tensor diagonal block triangularity",
        "principal finite-type W-algebra theorem body and its all-genera enrichment elimination",
    ],
    verified_against=[
        "Cartan exponent tables in compute.lib.lie_algebra via w_algebra_pbw_genus1",
        "Explicit W3 vacuum-module L0 and W_(1) computations through conformal weight 8",
    ],
    disjoint_rationale=(
        "The manuscript proof argues abstractly from principal exponents and "
        "the L0 diagonal block.  This test checks finite root-system tables "
        "and an explicit W3 vacuum-module calculation: the unique weight-2 "
        "generator preserves weight, while every higher-spin generator raises it."
    ),
)
def test_principal_w_pbw_triangular_weight_blocks():
    """Principal finite-type W generators force an upper triangular d2 block."""
    from compute.lib.w_algebra_pbw_genus1 import (
        d2_target_weight,
        has_unique_stress_tensor,
        higher_spin_generators,
        principal_generator_weights,
        verify_w3_d2_weight_pattern,
        verify_w3_l0_scalar,
    )

    expected_weights = {
        ("A", 1): [2],
        ("A", 2): [2, 3],
        ("A", 3): [2, 3, 4],
        ("B", 2): [2, 4],
        ("C", 2): [2, 4],
        ("G", 2): [2, 6],
        ("F", 4): [2, 6, 8, 12],
    }

    for family, weights in expected_weights.items():
        assert principal_generator_weights(*family) == weights
        assert has_unique_stress_tensor(*family)
        assert all(weight > 2 for weight in higher_spin_generators(*family))
        for source_weight in range(2, 9):
            assert d2_target_weight(source_weight, 2) == source_weight
            for spin in higher_spin_generators(*family):
                assert d2_target_weight(source_weight, spin) > source_weight

    assert all(verify_w3_l0_scalar(max_weight=8).values())
    assert all(verify_w3_d2_weight_pattern(max_weight=8).values())


@independent_verification(
    claim="prop:shadow-formality-low-degree",
    derived_from=[
        "higher_genus_modular_koszul low-degree shadow-formality proposition",
        "tree-sum proof using Mbar_0,4 and Mbar_0,5 in the proposition body",
    ],
    verified_against=[
        "linf_bracket_engine low-arity shadow recursion for Heisenberg affine sl2 and Virasoro",
        "independent Virasoro OPE shadow constants S2=c/2 S3=2 S4=10/(c(5c+22))",
    ],
    disjoint_rationale=(
        "The proof identifies low-degree tree sums with formality obstructions. "
        "The test computes the first three shadow coefficients in a separate "
        "finite recursion engine for three archetypes and checks the expected "
        "vanishing and nonvanishing pattern."
    ),
)
def test_shadow_formality_low_degree_archetype_witnesses():
    """Low-degree formality shadows match curvature/cubic/quartic data."""
    from compute.lib.linf_bracket_engine import (
        LInfBracketComputer,
        ell3_affine_sl2,
        ell3_heisenberg,
        ell3_virasoro_explicit,
    )

    heis = LInfBracketComputer.heisenberg_shadows(Fraction(3), max_r=4)
    affine = LInfBracketComputer.affine_sl2_shadows(Fraction(2), max_r=4)
    vir = LInfBracketComputer.virasoro_shadows(Fraction(26), max_r=4)

    assert heis[2] == Fraction(3)
    assert heis[3] == heis[4] == 0
    assert ell3_heisenberg(Fraction(3)) == 0

    assert affine[2] == Fraction(3)
    assert affine[3] == ell3_affine_sl2(Fraction(2)) == Fraction(1)
    assert affine[4] == 0

    assert vir[2] == Fraction(13)
    assert vir[3] == ell3_virasoro_explicit(Fraction(26)) == Fraction(2)
    assert vir[4] == Fraction(10, 26 * 152) == Fraction(5, 1976)


@independent_verification(
    claim="prop:propagator-variance",
    derived_from=[
        "higher_genus_modular_koszul propagator variance proposition",
        "H-Poisson bracket comparison in equation eq:propagator-variance",
    ],
    verified_against=[
        "weighted Cauchy-Schwarz algebra identity for two channels",
        "W3 exact OPE data factorization 1280*(25c^2+100c-428)^2/(c^3*(5c+22)^6)",
    ],
    disjoint_rationale=(
        "The proof computes the variance as the difference between two "
        "H-Poisson brackets.  The test verifies the independent weighted "
        "Cauchy-Schwarz square identity and then checks the exact W3 "
        "factorization from finite OPE gradient data."
    ),
)
def test_propagator_variance_weighted_square_and_w3_factorization():
    """The variance is a weighted square; for W3 the exact square factor is P(c)^2."""
    from compute.lib.propagator_variance import (
        c,
        propagator_variance,
        w3_kappas,
        w3_mixing_polynomial,
        w3_quartic_gradients,
    )

    k1, k2, f1, f2 = symbols("k1 k2 f1 f2", nonzero=True)
    delta_two_channel = cancel(
        f1**2 / k1 + f2**2 / k2 - (f1 + f2) ** 2 / (k1 + k2)
    )
    expected_square = cancel((k2 * f1 - k1 * f2) ** 2 / (k1 * k2 * (k1 + k2)))
    assert simplify(delta_two_channel - expected_square) == 0

    delta_w3 = cancel(propagator_variance(w3_kappas(), w3_quartic_gradients()))
    P = w3_mixing_polynomial()
    assert factor(delta_w3) == 1280 * P**2 / (c**3 * (5 * c + 22) ** 6)
    assert simplify(numer(delta_w3) / P**2 - 1280) == 0


@independent_verification(
    claim="thm:multi-weight-genus-expansion",
    derived_from=[
        "higher_genus_modular_koszul multi-weight genus expansion theorem",
        "stable-graph decomposition proof of delta F_g cross in the theorem body",
    ],
    verified_against=[
        "multichannel_genus2 W3 finite Feynman-rule engine",
        "closed arithmetic identity 3/c + 9/(2c) + 1/16 + 21/(4c) = (c+204)/(16c)",
    ],
    disjoint_rationale=(
        "The theorem states the all-genus decomposition.  This test checks the "
        "first nontrivial multi-weight witness using a separate W3 genus-2 "
        "Feynman-rule engine and exact rational arithmetic for the four "
        "contributing boundary graphs."
    ),
)
def test_multi_weight_w3_genus2_cross_channel_constants():
    """W3 genus 2 has four exact mixed graph constants summing to (c+204)/(16c)."""
    from compute.lib.multichannel_genus2 import genus2_cross_channel_corrections

    for c_value in (Fraction(1), Fraction(2), Fraction(26), Fraction(50)):
        result = genus2_cross_channel_corrections(c_value)
        assert result["delta_Gamma2_banana"] == Fraction(3, c_value)
        assert result["delta_Gamma4_theta"] == Fraction(9, 2 * c_value)
        assert result["delta_Gamma5_mixed"] == Fraction(1, 16)
        assert result["delta_Gamma7_barbell"] == Fraction(21, 4 * c_value)
        assert result["delta_total"] == Fraction(c_value + 204, 16 * c_value)

    c_symbol = Symbol("c", nonzero=True)
    total = (
        3 / c_symbol
        + Rational(9, 2) / c_symbol
        + Rational(1, 16)
        + Rational(21, 4) / c_symbol
    )
    assert simplify(total - (c_symbol + 204) / (16 * c_symbol)) == 0
