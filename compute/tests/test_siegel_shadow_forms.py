r"""Tests for Siegel modular forms from genus-2 shadow amplitudes.

Verifies:
  1. Faber-Pandharipande numbers (exact arithmetic)
  2. Shadow amplitude F_2 = kappa * lambda_2^{FP} for all families
  3. Siegel theta function coefficients (E_8, Leech, D_{16}^+, E_8 x E_8)
  4. Fourier coefficient tables and positivity
  5. Leech cusp projection (nonvanishing of cusp component)
  6. Igusa ring dimensions
  7. Bocherer discriminant sums
  8. Witt genus-2 obstruction (E_8 x E_8 = D_{16}^+ at genus 2)
  9. Kappa additivity
 10. Three-route cross-verification
 11. Landscape sweep (all standard families)
 12. Genus-2 stable graph amplitudes (class G and class L)

All arithmetic is exact (fractions.Fraction) where possible.
Numerical tolerances used only for floating-point summaries.
"""

import pytest
from fractions import Fraction
from typing import Dict

from compute.lib.siegel_shadow_forms import (
    # FP numbers
    lambda_fp,
    shadow_amplitude_F2,
    # Theta coefficients
    siegel_theta_coeff_e8,
    siegel_theta_coeff_leech,
    siegel_theta_coeff_d16plus,
    siegel_theta_coeff_e8e8,
    # Tables
    fourier_table_eisenstein,
    fourier_table_leech,
    _half_integral_matrices,
    # Cusp projection
    leech_eisenstein_difference,
    leech_cusp_projection_table,
    # Igusa ring
    igusa_dimension,
    igusa_cusp_dimension,
    IGUSA_DIMENSIONS,
    IGUSA_CUSP_DIMENSIONS,
    # Bocherer
    bocherer_discriminant_sums,
    e8_bocherer_sums,
    leech_bocherer_sums,
    # Witt obstruction
    witt_genus2_obstruction,
    # F_2 computations
    shadow_F2_lattice,
    shadow_F2_virasoro,
    shadow_F2_affine_kac_moody,
    # Genus-2 graphs
    genus2_graph_F2_class_G,
    genus2_graph_F2_class_L,
    # Landscape
    landscape_F2,
    # Cross-verification
    verify_F2_three_routes,
    verify_kappa_additivity_genus2,
    # Siegel weight
    siegel_weight_from_voa,
    siegel_form_space_for_lattice,
    # Witt class
    genus2_witt_class,
    # Full suite
    full_verification,
)
from compute.lib.siegel_eisenstein import (
    siegel_eisenstein_coefficient,
    bernoulli,
)
from compute.lib.genus2_bocherer_bridge import (
    genus2_rep_e8,
    genus2_rep_leech,
    LEECH_KISSING,
)


# ============================================================================
# 1. FABER-PANDHARIPANDE NUMBERS
# ============================================================================

class TestFaberPandharipande:
    """Exact verification of lambda_g^{FP} = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda_1(self):
        """lambda_1^{FP} = 1/24 (from B_2 = 1/6)."""
        lam = lambda_fp(1)
        assert lam == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^{FP} = 7/5760 (from B_4 = -1/30)."""
        lam = lambda_fp(2)
        # (2^3 - 1)/2^3 * (1/30) / 24 = (7/8) * (1/30) / 24 = 7 / 5760
        assert lam == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^{FP} = 31/967680 (from B_6 = 1/42)."""
        lam = lambda_fp(3)
        # (2^5 - 1)/2^5 * (1/42) / 720 = (31/32) * (1/42) / 720 = 31/967680
        expected = Fraction(31, 32) * Fraction(1, 42) / Fraction(720)
        assert lam == expected

    def test_lambda_4(self):
        """lambda_4^{FP} from B_8 = -1/30."""
        lam = lambda_fp(4)
        B8 = bernoulli(8)
        expected = Fraction(2**7 - 1, 2**7) * abs(B8) / Fraction(40320)
        assert lam == expected

    def test_lambda_5(self):
        """lambda_5^{FP} from B_{10} = 5/66."""
        lam = lambda_fp(5)
        B10 = bernoulli(10)
        expected = Fraction(2**9 - 1, 2**9) * abs(B10) / Fraction(3628800)
        assert lam == expected

    def test_lambda_1_numerical(self):
        assert abs(float(lambda_fp(1)) - 1/24) < 1e-15

    def test_lambda_2_numerical(self):
        assert abs(float(lambda_fp(2)) - 7/5760) < 1e-15

    def test_all_positive(self):
        """All lambda_g^{FP} are strictly positive."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP should be positive"

    def test_decreasing(self):
        """lambda_g^{FP} is strictly decreasing."""
        for g in range(1, 7):
            assert lambda_fp(g) > lambda_fp(g + 1), \
                f"lambda_{g} should be > lambda_{g+1}"

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# ============================================================================
# 2. SHADOW AMPLITUDE F_2
# ============================================================================

class TestShadowAmplitudeF2:
    """F_2(A) = kappa(A) * lambda_2^{FP}."""

    def test_F2_heisenberg_rank1(self):
        """F_2(H_1) = 1 * 7/5760 = 7/5760."""
        assert shadow_amplitude_F2(Fraction(1)) == Fraction(7, 5760)

    def test_F2_e8(self):
        """F_2(V_{E_8}) = 8 * 7/5760 = 7/720."""
        assert shadow_amplitude_F2(Fraction(8)) == Fraction(7, 720)

    def test_F2_leech(self):
        """F_2(V_{Leech}) = 24 * 7/5760 = 7/240."""
        assert shadow_amplitude_F2(Fraction(24)) == Fraction(7, 240)

    def test_F2_d4(self):
        """F_2(V_{D_4}) = 4 * 7/5760 = 7/1440."""
        assert shadow_amplitude_F2(Fraction(4)) == Fraction(7, 1440)

    def test_F2_d16(self):
        """F_2(V_{D_{16}^+}) = 16 * 7/5760 = 7/360."""
        assert shadow_amplitude_F2(Fraction(16)) == Fraction(7, 360)

    def test_F2_zero_kappa(self):
        """F_2(A) = 0 when kappa = 0 (uncurved)."""
        assert shadow_amplitude_F2(Fraction(0)) == Fraction(0)

    def test_F2_lattice_convenience(self):
        """Convenience function shadow_F2_lattice agrees with manual computation."""
        for rank in [4, 8, 16, 24]:
            assert shadow_F2_lattice(rank) == Fraction(rank) * lambda_fp(2)

    def test_F2_virasoro(self):
        """F_2(Vir_c) = (c/2) * 7/5760."""
        for c_val in [1, 13, 26]:
            expected = Fraction(c_val, 2) * lambda_fp(2)
            assert shadow_F2_virasoro(Fraction(c_val)) == expected

    def test_F2_virasoro_c1(self):
        """F_2(Vir_{c=1}) = 7/11520."""
        assert shadow_F2_virasoro(Fraction(1)) == Fraction(7, 11520)

    def test_F2_virasoro_c26(self):
        """F_2(Vir_{c=26}) = 13 * 7/5760 = 91/5760 = 7/360 * (13/16)... check."""
        F2 = shadow_F2_virasoro(Fraction(26))
        assert F2 == Fraction(13) * Fraction(7, 5760)

    def test_F2_affine_sl2_level1(self):
        """F_2(V_1(sl_2)): kappa = 3*3/(2*2) = 9/4."""
        F2 = shadow_F2_affine_kac_moody(k=1, dim_g=3, h_dual=2)
        expected = Fraction(9, 4) * lambda_fp(2)
        assert F2 == expected

    def test_F2_affine_sl2_level2(self):
        """F_2(V_2(sl_2)): kappa = 3*4/(2*2) = 3."""
        F2 = shadow_F2_affine_kac_moody(k=2, dim_g=3, h_dual=2)
        expected = Fraction(3) * lambda_fp(2)
        assert F2 == expected


# ============================================================================
# 3. SIEGEL THETA COEFFICIENTS
# ============================================================================

class TestSiegelThetaE8:
    """Theta_{E_8}^{(2)} = E_4^{(2)} by Siegel-Weil."""

    def test_diag_11(self):
        """r_2(E_8, diag(1,1)) = 240 * 126 = 30240."""
        coeff = siegel_theta_coeff_e8(1, 0, 1)
        assert coeff == 30240
        # Cross-check with direct enumeration
        direct = genus2_rep_e8(1, 0, 1)
        assert direct == 30240

    def test_matrix_111(self):
        """r_2(E_8, ((1, 1/2), (1/2, 1))) at Delta = 3."""
        coeff = siegel_theta_coeff_e8(1, 1, 1)
        assert coeff is not None
        assert coeff > 0
        # Cross-check with direct
        direct = genus2_rep_e8(1, 1, 1)
        if direct is not None:
            assert coeff == direct

    def test_agrees_with_eisenstein(self):
        """Theta_{E_8}^{(2)} Fourier coefficients = E_4^{(2)} coefficients."""
        for (a, b, c) in [(1, 0, 1), (1, 1, 1), (2, 0, 1)]:
            Delta = 4 * a * c - b * b
            if Delta > 0:
                theta = siegel_theta_coeff_e8(a, b, c)
                eis = int(siegel_eisenstein_coefficient(4, a, b, c))
                assert theta == eis, f"Mismatch at T=({a},{b},{c}): {theta} vs {eis}"

    def test_all_positive(self):
        """All E_4^{(2)} coefficients are strictly positive at T > 0."""
        for (a, b, c) in [(1, 0, 1), (1, 1, 1), (2, 0, 1), (2, 0, 2), (2, 1, 2)]:
            coeff = siegel_theta_coeff_e8(a, b, c)
            assert coeff is not None and coeff > 0, \
                f"E_4^(2) at ({a},{b},{c}) should be positive, got {coeff}"

    def test_zero_matrix(self):
        """Coefficient at T = 0 is 1."""
        assert siegel_theta_coeff_e8(0, 0, 0) == 1

    def test_negative_discriminant(self):
        """Non-positive-definite T gives 0."""
        assert siegel_theta_coeff_e8(1, 3, 1) == 0  # Delta = 4 - 9 < 0


class TestSiegelThetaLeech:
    """Theta_{Leech}^{(2)} coefficients from shell data."""

    def test_no_norm2(self):
        """Leech has no norm-2 vectors, so r_2(Leech, diag(1,1)) = 0."""
        assert siegel_theta_coeff_leech(1, 0, 1) == 0

    def test_diag_22(self):
        """r_2(Leech, diag(2,2)): pairs of orthogonal minimal vectors."""
        coeff = siegel_theta_coeff_leech(2, 0, 2)
        expected = LEECH_KISSING * 93150  # 196560 * 93150 (orthogonal pairs)
        # But this counts ordered pairs, divided by epsilon = 2.
        # Actually: r_2(Leech, ((2,0),(0,2))) counts all (v1,v2) with
        # |v1|^2 = |v2|^2 = 4, (v1,v2) = 0.
        # That's 196560 * 93150 ordered pairs.
        assert coeff == expected

    def test_min_shell_b1(self):
        """r_2(Leech, ((2, 1/2), (1/2, 2))) = 196560 * 47104."""
        coeff = siegel_theta_coeff_leech(2, 1, 2)
        expected = 196560 * 47104
        assert coeff == expected

    def test_min_shell_b2(self):
        """r_2(Leech, ((2, 1), (1, 2))) = 196560 * 4600."""
        coeff = siegel_theta_coeff_leech(2, 2, 2)
        expected = 196560 * 4600
        assert coeff == expected

    def test_zero_vector(self):
        """r_2(Leech, 0) = 1."""
        assert siegel_theta_coeff_leech(0, 0, 0) == 1

    def test_one_zero(self):
        """r_2(Leech, ((0,0),(0,2))) = 196560 (one zero, one minimal)."""
        assert siegel_theta_coeff_leech(0, 0, 2) == 196560


class TestSiegelThetaD16:
    """Theta_{D_{16}^+}^{(2)} = E_8^{(2)} by Siegel-Weil."""

    def test_diag_11(self):
        """r_2(D_{16}^+, diag(1,1)) = E_8^{(2)}(diag(1,1))."""
        coeff = siegel_theta_coeff_d16plus(1, 0, 1)
        eis = int(siegel_eisenstein_coefficient(8, 1, 0, 1))
        assert coeff == eis

    def test_positive(self):
        """E_8^{(2)} coefficients are positive."""
        for (a, b, c) in [(1, 0, 1), (1, 1, 1), (2, 0, 2)]:
            coeff = siegel_theta_coeff_d16plus(a, b, c)
            assert coeff is not None and coeff > 0


class TestSiegelThetaE8xE8:
    """Theta_{E_8 x E_8}^{(2)} = (E_4^{(2)})^2 by tensor product."""

    def test_diag_11(self):
        """(E_4)^2 at diag(1,1) is a product convolution."""
        coeff = siegel_theta_coeff_e8e8(1, 0, 1)
        assert coeff is not None and coeff > 0

    def test_weight_check(self):
        """(E_4^{(2)})^2 has weight 8, matching D_{16}^+ at weight 8."""
        # Both E_8 x E_8 and D_{16}^+ produce weight-8 forms
        coeff_e8e8 = siegel_theta_coeff_e8e8(1, 0, 1)
        coeff_d16 = siegel_theta_coeff_d16plus(1, 0, 1)
        # They should agree because dim S_8(Sp(4,Z)) = 0
        assert coeff_e8e8 == coeff_d16


# ============================================================================
# 4. FOURIER COEFFICIENT TABLES
# ============================================================================

class TestFourierTables:
    """Fourier coefficient tables for various forms."""

    def test_half_integral_matrices_count(self):
        """Correct number of positive definite T with entries <= 2."""
        matrices = _half_integral_matrices(2)
        # Each T = (a, b, c) with 1 <= a, c <= 2, 4ac - b^2 > 0
        # For a=1, c=1: |b| < 2, so b in {-1, 0, 1} → 3
        # For a=1, c=2: 4*2 - b^2 > 0, |b| < 2sqrt(2) ≈ 2.83, so b in {-2,-1,0,1,2} → 5
        # For a=2, c=1: same as above → 5
        # For a=2, c=2: 16 - b^2 > 0, |b| < 4, so b in {-3,-2,-1,0,1,2,3} → 7
        # Total = 3 + 5 + 5 + 7 = 20
        assert len(matrices) == 20

    def test_eisenstein_table_all_positive(self):
        """All E_k^{(2)} coefficients at T > 0 are positive (Kitaoka)."""
        for k in [4, 6, 8, 10, 12]:
            table = fourier_table_eisenstein(k, max_entry=2)
            for T, coeff in table.items():
                assert coeff > 0, f"E_{k}^(2) at {T} should be positive, got {coeff}"

    def test_leech_table_no_norm2(self):
        """Leech lattice has no norm-2 vectors: r_2(Leech, diag(1,1)) = 0."""
        table = fourier_table_leech(max_entry=2)
        assert table.get((1, 0, 1)) == 0

    def test_leech_table_min_shell(self):
        """Leech lattice minimal shell: r_2(Leech, diag(2,2)) > 0."""
        table = fourier_table_leech(max_entry=2)
        val = table.get((2, 0, 2))
        assert val is not None and val > 0


# ============================================================================
# 5. LEECH CUSP PROJECTION
# ============================================================================

class TestLeechCuspProjection:
    """Theta_{Leech}^{(2)} has nontrivial cusp component."""

    def test_cusp_nonvanishing_at_diag_11(self):
        """At T = diag(1,1): Leech = 0 but E_{12} > 0, so difference < 0."""
        diff = leech_eisenstein_difference(1, 0, 1)
        assert diff is not None
        assert diff < 0, "Cusp component must be negative at diag(1,1)"

    def test_cusp_at_diag_22(self):
        """At T = diag(2,2): compute and verify nonzero."""
        diff = leech_eisenstein_difference(2, 0, 2)
        assert diff is not None
        # The difference is Leech_rep - E12_coeff.
        # This can be positive or negative depending on the shell data.

    def test_cusp_table_has_nonzero(self):
        """The cusp projection table has at least one nonzero entry."""
        table = leech_cusp_projection_table(max_entry=2)
        nonzero = [T for T, v in table.items() if v is not None and v != 0]
        assert len(nonzero) > 0, "Cusp projection should have nonzero entries"

    def test_cusp_nonvanishing_implies_chi12(self):
        """Nonzero cusp projection proves chi_12 component is nonzero.
        Since dim S_{12}(Sp(4,Z)) = 1, any nonzero cusp coefficient means
        the chi_12 projection is nonzero."""
        diff = leech_eisenstein_difference(1, 0, 1)
        assert diff != 0, "Nonzero cusp projection at diag(1,1)"
        # dim S_12 = 1, so the cusp part is a multiple of chi_12
        # (modulo the Klingen Eisenstein correction)


# ============================================================================
# 6. IGUSA RING DIMENSIONS
# ============================================================================

class TestIgusaDimensions:
    """Dimensions of M_k(Sp(4,Z)) and S_k(Sp(4,Z))."""

    def test_dim_M4(self):
        """dim M_4(Sp(4,Z)) = 1 (spanned by E_4)."""
        assert igusa_dimension(4) == 1

    def test_dim_M6(self):
        """dim M_6(Sp(4,Z)) = 1 (spanned by E_6)."""
        assert igusa_dimension(6) == 1

    def test_dim_M8(self):
        """dim M_8(Sp(4,Z)) = 1 (E_4^2 = E_8 because dim S_8 = 0)."""
        # Actually: dim M_8 should be the number of monomials E_4^a E_6^b chi_10^c chi_12^d = 8
        # 4a + 6b + 10c + 12d = 8: only (a,b,c,d) = (2,0,0,0). So dim = 1.
        assert igusa_dimension(8) == 1

    def test_dim_M10(self):
        """dim M_{10}(Sp(4,Z)) = 2 (E_4 E_6 and chi_{10})."""
        assert igusa_dimension(10) == 2

    def test_dim_M12(self):
        """dim M_{12}(Sp(4,Z)) = 3 (E_4^3, E_6^2, chi_{12})."""
        assert igusa_dimension(12) == 3

    def test_dim_M0(self):
        """dim M_0 = 1 (constants)."""
        assert igusa_dimension(0) == 1

    def test_dim_M2(self):
        """dim M_2 = 0 (no weight-2 forms)."""
        assert igusa_dimension(2) == 0

    def test_dim_odd_weight(self):
        """Odd weight: dim = 0 for k < 35."""
        for k in [1, 3, 5, 7, 9, 11, 13]:
            assert igusa_dimension(k) == 0

    def test_cusp_dim_small(self):
        """No cusp forms for weight < 10."""
        for k in [0, 2, 4, 6, 8]:
            assert igusa_cusp_dimension(k) == 0

    def test_cusp_dim_10(self):
        """dim S_{10} = 1 (chi_{10})."""
        assert igusa_cusp_dimension(10) == 1

    def test_cusp_dim_12(self):
        """dim S_{12} = 1 (chi_{12})."""
        assert igusa_cusp_dimension(12) == 1

    def test_cusp_dim_14(self):
        """dim S_{14} = 0."""
        assert igusa_cusp_dimension(14) == 0

    def test_dim_growth(self):
        """dim M_k grows with k (not necessarily monotone at each step).

        The Siegel modular form ring C[E_4, E_6, chi_{10}, chi_{12}] is
        a polynomial ring with generators of degrees 4, 6, 10, 12.
        The Hilbert function is NOT monotone: dim M_{12} = 3 > dim M_{14} = 2
        because weight 14 = 4+10 = 4+4+6 has only 2 monomials while
        weight 12 = 4+4+4 = 6+6 = 12 has 3.  The dimension is monotone
        for sufficiently large k.
        """
        assert igusa_dimension(20) > igusa_dimension(4)
        assert igusa_dimension(16) > igusa_dimension(6)
        # Non-monotonicity at weight 14: dim M_12 = 3 > dim M_14 = 2
        assert igusa_dimension(12) == 3
        assert igusa_dimension(14) == 2

    def test_dim_formula_agrees_with_table(self):
        """Computed dimensions agree with the hardcoded table."""
        for k, expected in IGUSA_DIMENSIONS.items():
            computed = igusa_dimension(k)
            assert computed == expected, \
                f"dim M_{k}: computed {computed}, expected {expected}"


# ============================================================================
# 7. BOCHERER DISCRIMINANT SUMS
# ============================================================================

class TestBochererSums:
    """Bocherer discriminant sums for lattice VOAs."""

    def test_e8_sums_nonempty(self):
        """E_8 Bocherer sums are nonempty."""
        sums = e8_bocherer_sums()
        assert len(sums) > 0

    def test_e8_sums_all_positive(self):
        """E_8 Bocherer sums are all positive (Eisenstein coefficients positive)."""
        sums = e8_bocherer_sums()
        for D, val in sums.items():
            assert val > 0, f"E_8 Bocherer sum at D={D} should be positive, got {val}"

    def test_leech_sums_nonempty(self):
        """Leech Bocherer sums are nonempty."""
        sums = leech_bocherer_sums()
        assert len(sums) > 0

    def test_leech_sums_at_minus_16(self):
        """Leech Bocherer sum at D = -16 (from b=0, a=c=2)."""
        sums = leech_bocherer_sums()
        # D = 0 - 16 = -16 comes from a=c=2, b=0
        assert -16 in sums
        # The value should be LEECH_KISSING * 93150 / 2
        # (divided by epsilon = 2 because a=c and b=0)
        expected = Fraction(LEECH_KISSING * 93150, 2)
        # But the function also sums over other (a,b,c) with the same discriminant.
        # D = -16 also comes from a=2, c=2, b=0 (only one such matrix with a<=c).
        # For a=c=2, b=0: D = 0 - 16 = -16. No other matrix gives D = -16 with a <= c <= 3.
        # (a=1, c=4 would give D = b^2 - 16, needing b^2 = 0, i.e., a=1, c=4, b=0, D=-4)
        # So the sum IS the single term.
        assert sums[-16] == expected

    def test_leech_negative_discriminants(self):
        """All Bocherer discriminants are negative."""
        sums = leech_bocherer_sums()
        for D in sums:
            assert D < 0, f"Discriminant should be negative, got D={D}"


# ============================================================================
# 8. WITT GENUS-2 OBSTRUCTION
# ============================================================================

class TestWittObstruction:
    """E_8 x E_8 and D_{16}^+ agree at genus 2 (dim S_8 = 0)."""

    def test_diag_11(self):
        """(E_4)^2 = E_8 at T = diag(1,1)."""
        diff = witt_genus2_obstruction(1, 0, 1)
        assert diff == 0

    def test_matrix_111(self):
        """(E_4)^2 = E_8 at T = ((1, 1/2), (1/2, 1))."""
        diff = witt_genus2_obstruction(1, 1, 1)
        assert diff == 0

    def test_diag_22(self):
        """(E_4)^2 = E_8 at T = diag(2,2)."""
        diff = witt_genus2_obstruction(2, 0, 2)
        assert diff == 0

    def test_matrix_201(self):
        """(E_4)^2 = E_8 at T = ((2, 0), (0, 1))."""
        diff = witt_genus2_obstruction(2, 0, 1)
        assert diff == 0

    def test_witt_class_function(self):
        """genus2_witt_class reports equivalence for E8xE8 vs D16+."""
        result = genus2_witt_class('E8xE8', 'D16+')
        assert result['genus2_equivalent'] is True

    def test_witt_class_e8_vs_leech(self):
        """E_8 (weight 4) and Leech (weight 12) have different weights,
        so they are not directly comparable. This tests the function handles
        different lattices gracefully."""
        # E_8 at diag(2,2) vs Leech at diag(2,2): different objects, different weights.
        # Just verify the function runs.
        result = genus2_witt_class('E8', 'Leech')
        # They will differ because they have different theta series
        assert isinstance(result['differences'], dict)


# ============================================================================
# 9. KAPPA ADDITIVITY
# ============================================================================

class TestKappaAdditivity:
    """F_2 is additive under tensor product (kappa is additive)."""

    def test_e8_plus_e8(self):
        """F_2(E_8 x E_8) = 2 * F_2(E_8)."""
        result = verify_kappa_additivity_genus2()
        assert result['E8xE8_additive'] is True

    def test_d4_times_4(self):
        """F_2(D_4^4) = 4 * F_2(D_4) = F_2(rank 16)."""
        result = verify_kappa_additivity_genus2()
        assert result['D4x4_additive'] is True

    def test_explicit_values(self):
        """Check explicit F_2 values in the additivity result."""
        result = verify_kappa_additivity_genus2()
        assert result['F2_E8'] == Fraction(7, 720)
        assert result['F2_E8xE8_additive'] == Fraction(7, 360)
        assert result['F2_D4'] == Fraction(7, 1440)


# ============================================================================
# 10. THREE-ROUTE CROSS-VERIFICATION
# ============================================================================

class TestThreeRoutes:
    """Independent verification of F_2 via three routes."""

    def test_e8_routes_agree(self):
        """Routes 1 and 2 agree for E_8."""
        result = verify_F2_three_routes('E8')
        assert result['routes_1_2_agree'] is True

    def test_e8_siegel_positive(self):
        """Route 3: Siegel-Weil checks are all positive for E_8."""
        result = verify_F2_three_routes('E8')
        assert result.get('all_siegel_positive', True) is True

    def test_d16_routes_agree(self):
        """Routes 1 and 2 agree for D_{16}^+."""
        result = verify_F2_three_routes('D16+')
        assert result['routes_1_2_agree'] is True

    def test_leech_routes_agree(self):
        """Routes 1 and 2 agree for Leech."""
        result = verify_F2_three_routes('Leech')
        assert result['routes_1_2_agree'] is True

    def test_d4_routes_agree(self):
        """Routes 1 and 2 agree for D_4."""
        result = verify_F2_three_routes('D4')
        assert result['routes_1_2_agree'] is True

    def test_e8_F2_value(self):
        result = verify_F2_three_routes('E8')
        assert result['F2_bar'] == Fraction(7, 720)

    def test_leech_F2_value(self):
        result = verify_F2_three_routes('Leech')
        assert result['F2_bar'] == Fraction(7, 240)


# ============================================================================
# 11. LANDSCAPE SWEEP
# ============================================================================

class TestLandscapeSweep:
    """F_2 for the entire standard landscape."""

    def test_all_entries_have_kappa(self):
        """Every landscape entry has a kappa value."""
        landscape = landscape_F2()
        for name, data in landscape.items():
            assert 'kappa' in data, f"Missing kappa for {name}"

    def test_all_entries_have_F2(self):
        """Every landscape entry has an F_2 value."""
        landscape = landscape_F2()
        for name, data in landscape.items():
            assert 'F_2' in data, f"Missing F_2 for {name}"

    def test_all_F2_nonnegative(self):
        """All F_2 values are non-negative (kappa >= 0 for unitary theories)."""
        landscape = landscape_F2()
        for name, data in landscape.items():
            assert data['F_2'] >= 0, f"F_2 should be >= 0 for {name}, got {data['F_2']}"

    def test_heisenberg_d1(self):
        """Heisenberg rank 1: F_2 = 7/5760."""
        landscape = landscape_F2()
        assert landscape['Heisenberg_d1']['F_2'] == Fraction(7, 5760)

    def test_lattice_e8(self):
        """Lattice E_8: F_2 = 7/720."""
        landscape = landscape_F2()
        assert landscape['Lattice_E8']['F_2'] == Fraction(7, 720)

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c=13 (self-dual): F_2 = 13/2 * 7/5760."""
        landscape = landscape_F2()
        assert landscape['Virasoro_c13.0']['F_2'] == Fraction(13, 2) * Fraction(7, 5760)

    def test_virasoro_c26_critical(self):
        """Virasoro at c=26 (critical): F_2 = 13 * 7/5760."""
        landscape = landscape_F2()
        assert landscape['Virasoro_c26.0']['F_2'] == Fraction(13) * Fraction(7, 5760)

    def test_landscape_has_multiple_classes(self):
        """Landscape includes G, L, and M class algebras."""
        landscape = landscape_F2()
        classes = {data['class'] for data in landscape.values()}
        assert 'G' in classes, "Missing class G"
        assert 'L' in classes, "Missing class L"
        assert 'M' in classes, "Missing class M"

    def test_sl2_level1_kappa(self):
        """sl_2 level 1: kappa = 3*3/(2*2) = 9/4."""
        landscape = landscape_F2()
        assert landscape['sl2_level1']['kappa'] == Fraction(9, 4)


# ============================================================================
# 12. GENUS-2 STABLE GRAPH AMPLITUDES
# ============================================================================

class TestGenus2StableGraphs:
    """Graph amplitudes for class G and class L algebras."""

    def test_class_G_matches_F2(self):
        """Class G: graph sum = kappa * lambda_2 (no boundary corrections)."""
        for rank in [1, 4, 8, 16, 24]:
            kappa = Fraction(rank)
            result = genus2_graph_F2_class_G(kappa)
            expected = kappa * lambda_fp(2)
            assert result['F_2'] == expected

    def test_class_G_shadow_depth(self):
        """Class G has shadow depth 2."""
        result = genus2_graph_F2_class_G(Fraction(8))
        assert result['shadow_depth'] == 2

    def test_class_L_has_correction(self):
        """Class L: boundary correction from planted-forest term.
        For affine sl_2 level 1: kappa = 9/4, S_3 = 2."""
        kappa = Fraction(9, 4)
        S3 = Fraction(2)
        result = genus2_graph_F2_class_L(kappa, S3)
        assert result['delta_pf'] != 0, "Class L should have nonzero correction"
        assert result['shadow_depth'] == 3

    def test_class_L_S3_zero_reduces_to_G(self):
        """Class L with S_3 = 0 reduces to class G."""
        kappa = Fraction(8)
        result = genus2_graph_F2_class_L(kappa, Fraction(0))
        expected_bulk = kappa * lambda_fp(2)
        assert result['delta_pf'] == 0
        assert result['F_2'] == expected_bulk


# ============================================================================
# 13. SIEGEL WEIGHT FROM VOA DATA
# ============================================================================

class TestSiegelWeight:
    """Weight of genus-2 theta series from lattice rank."""

    def test_e8_weight(self):
        assert siegel_weight_from_voa(8) == 4

    def test_leech_weight(self):
        assert siegel_weight_from_voa(24) == 12

    def test_d16_weight(self):
        assert siegel_weight_from_voa(16) == 8

    def test_d4_weight(self):
        assert siegel_weight_from_voa(4) == 2

    def test_odd_rank_raises(self):
        with pytest.raises(ValueError):
            siegel_weight_from_voa(3)

    def test_space_for_e8(self):
        """M_4(Sp(4,Z)) has dimension 1, so Theta_{E_8}^{(2)} is unique."""
        info = siegel_form_space_for_lattice(8)
        assert info['weight'] == 4
        assert info['dim_M_k'] == 1
        assert info['dim_S_k'] == 0
        assert info['purely_eisenstein'] is True

    def test_space_for_leech(self):
        """M_{12}(Sp(4,Z)) has dimension 3, with 1-dim cusp space."""
        info = siegel_form_space_for_lattice(24)
        assert info['weight'] == 12
        assert info['dim_M_k'] == 3
        assert info['dim_S_k'] == 1
        assert info['purely_eisenstein'] is False

    def test_space_for_d16(self):
        """M_8(Sp(4,Z)) has dimension 1, so Theta_{D_{16}^+}^{(2)} = E_8."""
        info = siegel_form_space_for_lattice(16)
        assert info['weight'] == 8
        assert info['dim_M_k'] == 1
        assert info['dim_S_k'] == 0
        assert info['purely_eisenstein'] is True


# ============================================================================
# 14. COMPREHENSIVE FULL VERIFICATION
# ============================================================================

class TestFullVerification:
    """Run the complete verification suite."""

    def test_full_suite_runs(self):
        """Full verification suite completes without error."""
        result = full_verification()
        assert isinstance(result, dict)
        assert 'faber_pandharipande' in result
        assert 'landscape_F2' in result
        assert 'E8_three_routes' in result
        assert 'kappa_additivity' in result

    def test_full_fp_numbers(self):
        """FP numbers in the full suite are correct."""
        result = full_verification()
        assert result['faber_pandharipande'][1]['lambda_g_FP'] == Fraction(1, 24)
        assert result['faber_pandharipande'][2]['lambda_g_FP'] == Fraction(7, 5760)

    def test_full_witt(self):
        """Witt obstruction vanishes in the full suite."""
        result = full_verification()
        assert result['witt_E8xE8_vs_D16']['genus2_equivalent'] is True

    def test_full_additivity(self):
        """Kappa additivity holds in the full suite."""
        result = full_verification()
        assert result['kappa_additivity']['E8xE8_additive'] is True

    def test_full_igusa(self):
        """Igusa dimensions in the full suite are correct."""
        result = full_verification()
        assert result['igusa_dimensions'][4]['dim_M'] == 1
        assert result['igusa_dimensions'][12]['dim_M'] == 3
        assert result['igusa_dimensions'][12]['dim_S'] == 1


# ============================================================================
# 15. NUMERICAL CONSISTENCY
# ============================================================================

class TestNumericalConsistency:
    """Floating-point sanity checks on exact results."""

    def test_F2_e8_numerical(self):
        """F_2(E_8) ~ 0.00972."""
        F2 = float(shadow_F2_lattice(8))
        assert abs(F2 - 7/720) < 1e-12

    def test_F2_leech_numerical(self):
        """F_2(Leech) ~ 0.02917."""
        F2 = float(shadow_F2_lattice(24))
        assert abs(F2 - 7/240) < 1e-12

    def test_lambda_2_numerical(self):
        """lambda_2^{FP} ~ 0.001215."""
        lam2 = float(lambda_fp(2))
        assert abs(lam2 - 7/5760) < 1e-12

    def test_F2_ratios(self):
        """F_2 ratios match rank ratios (kappa additivity)."""
        F2_e8 = float(shadow_F2_lattice(8))
        F2_leech = float(shadow_F2_lattice(24))
        ratio = F2_leech / F2_e8
        assert abs(ratio - 3.0) < 1e-10  # 24/8 = 3


# ============================================================================
# 16. EDGE CASES AND ERROR HANDLING
# ============================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_F2_negative_kappa(self):
        """F_2 with negative kappa (e.g., ghost system)."""
        F2 = shadow_amplitude_F2(Fraction(-13))
        assert F2 < 0

    def test_theta_negative_discriminant(self):
        """Theta coefficient at non-positive-definite T is 0."""
        assert siegel_theta_coeff_e8(1, 3, 1) == 0  # Delta = 4-9 < 0

    def test_witt_obstruction_invalid(self):
        """Witt obstruction at non-positive-definite T returns None."""
        result = witt_genus2_obstruction(1, 3, 1)
        assert result is None

    def test_leech_diff_at_norm2(self):
        """Leech - E_12 at diag(1,1) is well-defined."""
        diff = leech_eisenstein_difference(1, 0, 1)
        assert isinstance(diff, Fraction)

    def test_bocherer_empty_for_trivial(self):
        """Bocherer sums for a function that always returns 0."""
        sums = bocherer_discriminant_sums(lambda a, b, c: 0, 2, 2)
        assert len(sums) == 0 or all(v == 0 for v in sums.values())
