r"""Tests for dressed_propagator_engine: edge integral coefficients and Hodge-lambda bridge.

Section 1: Hodge R-matrix properties
Section 2: Dressed propagator coefficients P^R(D+, D-)
Section 3: ALGEBRAIC PROOF of symmetry from symplectic condition
Section 4: Faber-Pandharipande numbers (the correct free energy formula)
Section 5: Shadow tower free energy F_g = kappa * lambda_g^FP (Theorem D)
Section 6: Virasoro F_2 and complementarity
Section 7: Structural gap between CohFT graph sum and shadow tower
Section 8: All-genera A-hat generating function

HONEST FRAMING:
    F_g(A) = kappa(A) * lambda_g^FP is proved by Theorem D (MC equation),
    not by the CohFT graph sum.  The CohFT graph sum at (g,0) computes a
    DIFFERENT quantity (psi-class integrals without Hodge class).
    The dressed propagator coefficient is an algebraic object of independent
    interest (symmetry from symplectic condition), not a "gap resolution."

Ground truth:
    Theorem D / thm:genus-universality (higher_genus_foundations.tex)
    Faber-Pandharipande formula: lambda_g^FP = int_{M-bar_{g,1}} lambda_g psi^{2g-2}
"""

import pytest
from fractions import Fraction

from compute.lib.dressed_propagator_engine import (
    dressed_propagator_coefficient,
    dressed_propagator_table,
    symmetry_proof_step,
    symmetry_proof_all,
    verify_symplectic_condition,
    faber_pandharipande_number,
    shadow_tower_free_energy,
    virasoro_free_energy,
    virasoro_complementarity,
    cohft_vs_shadow_comparison_g2,
    virasoro_cohft_vs_shadow_g2,
    fp_table,
    ahat_generating_function_coefficients,
)
from compute.lib.cohft_vertex_engine import r_matrix_coefficients


# ============================================================
# Section 1: Hodge R-matrix
# ============================================================

class TestHodgeRMatrix:

    def test_r0_is_1(self):
        assert r_matrix_coefficients(4)[0] == Fraction(1)

    def test_r1_from_bernoulli(self):
        """R_1 = B_2/(2*1) = (1/6)/2 = 1/12."""
        assert r_matrix_coefficients(4)[1] == Fraction(1, 12)

    def test_r2(self):
        assert r_matrix_coefficients(4)[2] == Fraction(1, 288)

    def test_r3_negative(self):
        assert r_matrix_coefficients(4)[3] == Fraction(-139, 51840)

    def test_symplectic_all(self):
        """R(-z)R(z) = 1 through degree 10."""
        result = verify_symplectic_condition(10)
        assert result['all_pass']


# ============================================================
# Section 2: Dressed propagator coefficients
# ============================================================

class TestDressedPropagatorCoefficients:

    def test_P_00(self):
        """P^R(0,0) = R_1 = 1/12."""
        assert dressed_propagator_coefficient(0, 0) == Fraction(1, 12)

    def test_P_10(self):
        """P^R(1,0) = R_2 = 1/288."""
        assert dressed_propagator_coefficient(1, 0) == Fraction(1, 288)

    def test_P_01_expanded(self):
        """P^R(0,1) = R_1^2 - R_2 = 1/144 - 1/288 = 1/288."""
        R = r_matrix_coefficients(4)
        assert dressed_propagator_coefficient(0, 1) == R[1] ** 2 - R[2]
        assert dressed_propagator_coefficient(0, 1) == Fraction(1, 288)

    def test_P_11(self):
        R = r_matrix_coefficients(4)
        assert dressed_propagator_coefficient(1, 1) == R[2] * R[1] - R[3]

    def test_P_02_telescopes(self):
        """P^R(0,2) = R_1*R_2 - R_2*R_1 + R_3 = R_3."""
        R = r_matrix_coefficients(4)
        assert dressed_propagator_coefficient(0, 2) == R[3]

    def test_P_20(self):
        """P^R(2,0) = R_3 (single term)."""
        R = r_matrix_coefficients(4)
        assert dressed_propagator_coefficient(2, 0) == R[3]

    def test_eta_scaling(self):
        p1 = dressed_propagator_coefficient(1, 1, eta_inv=Fraction(1))
        p7 = dressed_propagator_coefficient(1, 1, eta_inv=Fraction(7))
        assert p7 == 7 * p1

    def test_table_consistency(self):
        table = dressed_propagator_table(4)
        for dp in range(5):
            for dm in range(5):
                assert table[(dp, dm)] == dressed_propagator_coefficient(dp, dm)


# ============================================================
# Section 3: ALGEBRAIC PROOF of symmetry
# ============================================================

class TestSymmetryProof:
    """P^R(D+,D-) = P^R(D-,D+) proved from R(-z)R(z) = 1."""

    def test_proof_0_0(self):
        assert symmetry_proof_step(0, 0)['proof_chain_valid']

    def test_proof_1_0(self):
        assert symmetry_proof_step(1, 0)['proof_chain_valid']

    def test_proof_0_1(self):
        assert symmetry_proof_step(0, 1)['proof_chain_valid']

    def test_proof_2_1(self):
        assert symmetry_proof_step(2, 1)['proof_chain_valid']

    def test_proof_3_2(self):
        assert symmetry_proof_step(3, 2)['proof_chain_valid']

    def test_proof_all_degree_5(self):
        """Full proof chain for all 36 pairs with D+, D- <= 5."""
        result = symmetry_proof_all(5)
        assert result['all_valid']
        assert result['n_pairs'] == 36

    def test_symplectic_load_bearing(self):
        """Symplectic condition vanishes at each N used in the proof."""
        R = r_matrix_coefficients(12)
        for N in range(1, 10):
            s = sum((-1) ** m * R[m] * R[N - m] for m in range(N + 1))
            assert s == Fraction(0), f"N={N}"


# ============================================================
# Section 4: Faber-Pandharipande numbers
# ============================================================

class TestFaberPandharipande:
    """lambda_g^FP = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1}(2g)!)."""

    def test_genus_1(self):
        assert faber_pandharipande_number(1) == Fraction(1, 24)

    def test_genus_2(self):
        assert faber_pandharipande_number(2) == Fraction(7, 5760)

    def test_genus_3(self):
        assert faber_pandharipande_number(3) == Fraction(31, 967680)

    def test_genus_4(self):
        assert faber_pandharipande_number(4) == Fraction(127, 154828800)

    def test_all_positive(self):
        for g in range(1, 8):
            assert faber_pandharipande_number(g) > 0

    def test_strictly_decreasing(self):
        for g in range(1, 7):
            assert faber_pandharipande_number(g) > faber_pandharipande_number(g + 1)

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            faber_pandharipande_number(0)

    def test_fp_table(self):
        table = fp_table(5)
        assert table[1] == Fraction(1, 24)
        assert table[2] == Fraction(7, 5760)
        assert len(table) == 5


# ============================================================
# Section 5: Shadow tower free energy (Theorem D)
# ============================================================

class TestShadowTowerFreeEnergy:
    """F_g(A) = kappa(A) * lambda_g^FP."""

    def test_heisenberg_g1(self):
        assert shadow_tower_free_energy(1, Fraction(1)) == Fraction(1, 24)

    def test_heisenberg_g2(self):
        assert shadow_tower_free_energy(2, Fraction(1)) == Fraction(7, 5760)

    def test_kappa_scaling(self):
        for k in [Fraction(1), Fraction(3), Fraction(1, 2)]:
            F2 = shadow_tower_free_energy(2, k)
            assert F2 == k * Fraction(7, 5760)

    def test_virasoro_g2_c1(self):
        assert virasoro_free_energy(2, Fraction(1)) == Fraction(7, 11520)

    def test_virasoro_g2_c13(self):
        assert virasoro_free_energy(2, Fraction(13)) == Fraction(13, 2) * Fraction(7, 5760)


# ============================================================
# Section 6: Complementarity
# ============================================================

class TestComplementarity:
    """F_g(c) + F_g(26-c) = 13 * lambda_g^FP."""

    def test_g2_c1(self):
        assert virasoro_complementarity(2, Fraction(1))['holds']

    def test_g2_c13_selfdual(self):
        r = virasoro_complementarity(2, Fraction(13))
        assert r['holds']
        assert r['F_c'] == r['F_dual']

    def test_g2_generic(self):
        assert virasoro_complementarity(2, Fraction(7, 3))['holds']

    def test_g1(self):
        assert virasoro_complementarity(1, Fraction(5))['holds']

    def test_g3(self):
        assert virasoro_complementarity(3, Fraction(4))['holds']

    def test_all_genera(self):
        for g in range(1, 5):
            assert virasoro_complementarity(g, Fraction(7))['holds'], f"g={g}"


# ============================================================
# Section 7: Structural gap documentation
# ============================================================

class TestStructuralGap:
    """The CohFT graph sum at (g,0) != shadow tower free energy."""

    def test_heisenberg_gap_nonzero(self):
        """CohFT psi-sum != kappa * lambda_2^FP (structural, not convention)."""
        r = cohft_vs_shadow_comparison_g2(Fraction(1))
        assert r['gap_is_nonzero']

    def test_heisenberg_gap_positive(self):
        """CohFT psi-sum > shadow Hodge-lambda (psi sums overcount)."""
        r = cohft_vs_shadow_comparison_g2(Fraction(1))
        assert r['structural_gap'] > 0

    def test_gap_exists_all_kappa(self):
        for k in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            r = cohft_vs_shadow_comparison_g2(k)
            assert r['gap_is_nonzero'], f"kappa={k}"

    def test_virasoro_gap_nonzero(self):
        r = virasoro_cohft_vs_shadow_g2(Fraction(2))
        assert r['structural_gap'] != Fraction(0)

    def test_virasoro_shadow_value(self):
        """Shadow tower gives F_2 = (c/2) * 7/5760 regardless of C, Q."""
        for c in [Fraction(1), Fraction(2), Fraction(13)]:
            r = virasoro_cohft_vs_shadow_g2(c)
            assert r['shadow_total'] == (c / 2) * Fraction(7, 5760)


# ============================================================
# Section 8: A-hat generating function
# ============================================================

class TestAhatGeneratingFunction:
    r"""Verify SUM F_g x^{2g} = kappa * (x/2 / sin(x/2) - 1)."""

    def test_coefficients_match_fp(self):
        """A-hat coefficients equal FP numbers."""
        result = ahat_generating_function_coefficients(5)
        for g in range(1, 6):
            assert result['coefficients'][g] == faber_pandharipande_number(g)

    def test_is_ahat(self):
        result = ahat_generating_function_coefficients(3)
        assert result['is_ahat']
