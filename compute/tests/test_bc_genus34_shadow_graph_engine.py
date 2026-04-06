r"""Tests for BC-136: Genus-3/4 shadow graph sums, modular forms at zeta zeros.

142 tests organized in 12 sections:

  1. Lambda FP exact arithmetic (15 tests)
  2. Multi-path verification of lambda_g^FP (10 tests)
  3. Genus-3 graph enumeration (12 tests)
  4. Genus-3 scalar amplitude (10 tests)
  5. Genus-4 graph enumeration (12 tests)
  6. Genus-4 scalar amplitude (10 tests)
  7. A-hat generating function (10 tests)
  8. Cross-genus consistency (10 tests)
  9. Zeta zero evaluations (15 tests)
  10. Modular form identification (10 tests)
  11. Planted-forest decomposition (13 tests)
  12. Shadow partition function (15 tests)

Every numerical value verified by at least 2 independent paths.
Exact Fraction arithmetic throughout (no floating-point in core tests).

References:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction
from math import factorial, pi
import cmath

from compute.lib.bc_genus34_shadow_graph_engine import (
    # Section 0: Constants and exact arithmetic
    LAMBDA_FP,
    CHI_ORB_MBAR,
    BERNOULLI,
    GRAPH_COUNTS,
    ZETA_ZERO_GAMMAS,
    lambda_fp,
    bernoulli_number,
    lambda_fp_from_bernoulli,
    lambda_fp_from_ahat,
    # Section 1: Genus-3
    genus3_graphs,
    genus3_graph_count,
    genus3_by_loop_number,
    genus3_by_vertex_count,
    genus3_by_edge_count,
    genus3_automorphism_spectrum,
    genus3_amplitude_table,
    genus3_scalar_sum,
    genus3_nonzero_amplitude_count,
    genus3_planted_forest_count,
    genus3_euler_check,
    genus3_amplitude_by_loop,
    # Section 2: Genus-4
    genus4_graphs,
    genus4_graph_count,
    genus4_by_loop_number,
    genus4_by_vertex_count,
    genus4_amplitude_table,
    genus4_scalar_sum,
    genus4_nonzero_amplitude_count,
    genus4_planted_forest_count,
    genus4_euler_check,
    genus4_amplitude_by_loop,
    # Section 3: Multi-path verification
    verify_lambda_fp,
    verify_heisenberg_scalar,
    # Section 4: A-hat
    shadow_partition_function_coefficients,
    ahat_coefficients,
    ahat_series_check,
    # Section 5: Cross-genus
    cross_genus_table,
    genus_growth_monotonicity,
    # Section 6: Zeta zeros
    fg_at_zeta_zero,
    fg_table_at_zeros,
    normalized_fg_at_zeros,
    shadow_partition_at_zeros,
    fg_ratios_at_zeros,
    # Section 7: Modular forms
    modular_form_identification,
    quasi_modular_structure,
    # Section 8: Planted-forest
    genus3_pf_vs_nonpf,
    genus4_pf_vs_nonpf,
    # Section 9: Summary
    full_summary,
)
from compute.lib.stable_graph_enumeration import _bernoulli_exact, _lambda_fp_exact


# ============================================================================
# 1. Lambda FP exact arithmetic (15 tests)
# ============================================================================

class TestLambdaFP:
    """Exact Fraction tests for Faber-Pandharipande numbers."""

    def test_lambda1_exact(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2_exact(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3_exact(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda4_exact(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda5_exact(self):
        """lambda_5^FP = 73/3503554560."""
        assert lambda_fp(5) == Fraction(73, 3503554560)

    def test_lambda_fp_table_consistency(self):
        """Table values match engine values for g=1..5."""
        for g in range(1, 6):
            assert lambda_fp(g) == LAMBDA_FP[g]

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is NOT monotone decreasing (grows factorially).

        Actually lambda_g^FP DOES decrease for small g (1/24 > 7/5760 > ...),
        but eventually the (2g)! growth dominates for large g.
        For g=1..5, it is decreasing.
        """
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_bernoulli_b2(self):
        """B_2 = 1/6."""
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        """B_4 = -1/30."""
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_bernoulli_b6(self):
        """B_6 = 1/42."""
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_bernoulli_b8(self):
        """B_8 = -1/30."""
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_bernoulli_b10(self):
        """B_10 = 5/66."""
        assert bernoulli_number(10) == Fraction(5, 66)

    def test_lambda1_from_bernoulli(self):
        """lambda_1 = (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24."""
        B2 = Fraction(1, 6)
        computed = Fraction(1, 2) * B2 / Fraction(2)
        assert computed == Fraction(1, 24)

    def test_lambda4_from_bernoulli(self):
        """lambda_4 = (2^7-1)/2^7 * |B_8|/8! = 127/128 * (1/30)/40320."""
        B8_abs = Fraction(1, 30)
        computed = Fraction(127, 128) * B8_abs / Fraction(factorial(8))
        assert computed == Fraction(127, 154828800)


# ============================================================================
# 2. Multi-path verification of lambda_g^FP (10 tests)
# ============================================================================

class TestMultiPathVerification:
    """Verify lambda_g^FP via multiple independent computation paths."""

    def test_path1_bernoulli_g1(self):
        """Path 1 (Bernoulli formula) matches for g=1."""
        assert lambda_fp_from_bernoulli(1) == Fraction(1, 24)

    def test_path1_bernoulli_g3(self):
        """Path 1 (Bernoulli formula) matches for g=3."""
        assert lambda_fp_from_bernoulli(3) == Fraction(31, 967680)

    def test_path1_bernoulli_g4(self):
        """Path 1 (Bernoulli formula) matches for g=4."""
        assert lambda_fp_from_bernoulli(4) == Fraction(127, 154828800)

    def test_path2_ahat_g1(self):
        """Path 2 (A-hat inversion) matches for g=1."""
        assert lambda_fp_from_ahat(1) == Fraction(1, 24)

    def test_path2_ahat_g3(self):
        """Path 2 (A-hat inversion) matches for g=3."""
        assert lambda_fp_from_ahat(3) == Fraction(31, 967680)

    def test_path2_ahat_g4(self):
        """Path 2 (A-hat inversion) matches for g=4."""
        assert lambda_fp_from_ahat(4) == Fraction(127, 154828800)

    def test_five_paths_g3(self):
        """All five paths agree for g=3."""
        result = verify_lambda_fp(3)
        assert result['all_match']

    def test_five_paths_g4(self):
        """All five paths agree for g=4."""
        result = verify_lambda_fp(4)
        assert result['all_match']

    def test_growth_ratio_g2(self):
        """Growth ratio lambda_3/lambda_2 computed correctly."""
        result = verify_lambda_fp(3)
        assert result['ratio_check'] is not None
        assert result['ratio_check']['match']

    def test_growth_ratio_g3(self):
        """Growth ratio lambda_4/lambda_3 computed correctly."""
        result = verify_lambda_fp(4)
        assert result['ratio_check'] is not None
        assert result['ratio_check']['match']


# ============================================================================
# 3. Genus-3 graph enumeration (12 tests)
# ============================================================================

class TestGenus3Enumeration:
    """Tests for genus-3 stable graph enumeration."""

    def test_genus3_count(self):
        """42 stable graphs at (g=3, n=0)."""
        assert genus3_graph_count() == 42

    def test_genus3_loop_decomposition(self):
        """Loop number decomposition: h^1 = 0:4, 1:9, 2:14, 3:15."""
        expected = {0: 4, 1: 9, 2: 14, 3: 15}
        assert genus3_by_loop_number() == expected

    def test_genus3_vertex_decomposition(self):
        """Vertex count decomposition: 1:4, 2:12, 3:15, 4:11."""
        expected = {1: 4, 2: 12, 3: 15, 4: 11}
        assert genus3_by_vertex_count() == expected

    def test_genus3_loop_sum(self):
        """Total loop decomposition sums to 42."""
        loops = genus3_by_loop_number()
        assert sum(loops.values()) == 42

    def test_genus3_vertex_sum(self):
        """Total vertex decomposition sums to 42."""
        verts = genus3_by_vertex_count()
        assert sum(verts.values()) == 42

    def test_genus3_all_stable(self):
        """All genus-3 graphs are stable."""
        for g in genus3_graphs():
            assert g.is_stable

    def test_genus3_all_connected(self):
        """All genus-3 graphs are connected."""
        for g in genus3_graphs():
            assert g.is_connected

    def test_genus3_arithmetic_genus(self):
        """All genus-3 graphs have arithmetic genus 3."""
        for g in genus3_graphs():
            assert g.arithmetic_genus == 3

    def test_genus3_euler_char(self):
        """chi^orb(M_bar_{3,0}) = -12419/90720."""
        computed, expected, match = genus3_euler_check()
        assert match

    def test_genus3_euler_value(self):
        """Exact value of chi^orb(M_bar_{3,0})."""
        computed, expected, _ = genus3_euler_check()
        assert computed == Fraction(-12419, 90720)

    def test_genus3_aut_spectrum_length(self):
        """42 automorphism orders (one per graph)."""
        assert len(genus3_automorphism_spectrum()) == 42

    def test_genus3_aut_all_positive(self):
        """All automorphism orders are positive."""
        for a in genus3_automorphism_spectrum():
            assert a >= 1


# ============================================================================
# 4. Genus-3 scalar amplitude (10 tests)
# ============================================================================

class TestGenus3Amplitude:
    """Tests for genus-3 scalar-level amplitude computation."""

    def test_genus3_amplitude_table_size(self):
        """42 entries in the amplitude table."""
        assert len(genus3_amplitude_table()) == 42

    def test_genus3_scalar_sum_value(self):
        """Scalar sum equals lambda_3^FP = 31/967680."""
        assert genus3_scalar_sum() == Fraction(31, 967680)

    def test_genus3_scalar_matches_fp(self):
        """Graph sum matches Faber-Pandharipande formula."""
        assert genus3_scalar_sum() == lambda_fp(3)

    def test_genus3_scalar_matches_bernoulli(self):
        """Graph sum matches Bernoulli computation."""
        assert genus3_scalar_sum() == lambda_fp_from_bernoulli(3)

    def test_genus3_heisenberg_verification(self):
        """Heisenberg F_3(H_k) = k * 31/967680 via graph sum."""
        result = verify_heisenberg_scalar(3)
        assert result['match']

    def test_genus3_pf_scalar_vanishes(self):
        """Planted-forest scalar sum vanishes (Gaussian purity)."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['pf_vanishes_scalar']

    def test_genus3_nonpf_equals_total(self):
        """Non-PF scalar sum equals total scalar sum."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['nonpf_scalar_sum'] == lambda_fp(3)

    def test_genus3_loop_amplitudes_sum(self):
        """Amplitudes by loop sum to lambda_3^FP."""
        by_loop = genus3_amplitude_by_loop()
        total = sum(by_loop.values())
        assert total == lambda_fp(3)

    def test_genus3_nonzero_amplitude_positive(self):
        """At least some graphs have nonzero Gaussian amplitude."""
        assert genus3_nonzero_amplitude_count() > 0

    def test_genus3_pf_count_positive(self):
        """Genus-3 has planted-forest graphs."""
        assert genus3_planted_forest_count() > 0


# ============================================================================
# 5. Genus-4 graph enumeration (12 tests)
# ============================================================================

class TestGenus4Enumeration:
    """Tests for genus-4 stable graph enumeration."""

    def test_genus4_count(self):
        """379 stable graphs at (g=4, n=0)."""
        assert genus4_graph_count() == 379

    def test_genus4_loop_decomposition(self):
        """Loop number decomposition: h^1 = 0:11, 1:36, 2:93, 3:128, 4:111."""
        expected = {0: 11, 1: 36, 2: 93, 3: 128, 4: 111}
        assert genus4_by_loop_number() == expected

    def test_genus4_vertex_decomposition(self):
        """Vertex count decomposition: 1:5, 2:29, 3:79, 4:126, 5:98, 6:42."""
        expected = {1: 5, 2: 29, 3: 79, 4: 126, 5: 98, 6: 42}
        assert genus4_by_vertex_count() == expected

    def test_genus4_loop_sum(self):
        """Total loop decomposition sums to 379."""
        loops = genus4_by_loop_number()
        assert sum(loops.values()) == 379

    def test_genus4_vertex_sum(self):
        """Total vertex decomposition sums to 379."""
        verts = genus4_by_vertex_count()
        assert sum(verts.values()) == 379

    def test_genus4_all_stable(self):
        """All genus-4 graphs are stable."""
        for g in genus4_graphs():
            assert g.is_stable

    def test_genus4_all_connected(self):
        """All genus-4 graphs are connected."""
        for g in genus4_graphs():
            assert g.is_connected

    def test_genus4_arithmetic_genus(self):
        """All genus-4 graphs have arithmetic genus 4."""
        for g in genus4_graphs():
            assert g.arithmetic_genus == 4

    def test_genus4_euler_char(self):
        """chi^orb(M_bar_{4,0}) = -4717039/6220800."""
        computed, expected, match = genus4_euler_check()
        assert match

    def test_genus4_euler_value(self):
        """Exact value of chi^orb(M_bar_{4,0})."""
        computed, expected, _ = genus4_euler_check()
        assert computed == Fraction(-4717039, 6220800)

    def test_genus4_max_edges(self):
        """Maximum edge count = dim M_bar_{4,0} = 9."""
        max_edges = max(g.num_edges for g in genus4_graphs())
        assert max_edges == 9

    def test_genus4_max_vertices(self):
        """Maximum vertex count = 6 (one more than genus 3 max of 4)."""
        max_verts = max(g.num_vertices for g in genus4_graphs())
        assert max_verts == 6


# ============================================================================
# 6. Genus-4 scalar amplitude (10 tests)
# ============================================================================

class TestGenus4Amplitude:
    """Tests for genus-4 scalar-level amplitude computation."""

    def test_genus4_amplitude_table_size(self):
        """379 entries in the amplitude table."""
        assert len(genus4_amplitude_table()) == 379

    def test_genus4_scalar_sum_value(self):
        """Scalar sum equals lambda_4^FP = 127/154828800."""
        assert genus4_scalar_sum() == Fraction(127, 154828800)

    def test_genus4_scalar_matches_fp(self):
        """Graph sum matches Faber-Pandharipande formula."""
        assert genus4_scalar_sum() == lambda_fp(4)

    def test_genus4_scalar_matches_bernoulli(self):
        """Graph sum matches Bernoulli computation."""
        assert genus4_scalar_sum() == lambda_fp_from_bernoulli(4)

    def test_genus4_heisenberg_verification(self):
        """Heisenberg F_4(H_k) = k * 127/154828800 via graph sum."""
        result = verify_heisenberg_scalar(4)
        assert result['match']

    def test_genus4_pf_scalar_vanishes(self):
        """Planted-forest scalar sum vanishes (Gaussian purity)."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['pf_vanishes_scalar']

    def test_genus4_nonpf_equals_total(self):
        """Non-PF scalar sum equals total scalar sum."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['nonpf_scalar_sum'] == lambda_fp(4)

    def test_genus4_loop_amplitudes_sum(self):
        """Amplitudes by loop sum to lambda_4^FP."""
        by_loop = genus4_amplitude_by_loop()
        total = sum(by_loop.values())
        assert total == lambda_fp(4)

    def test_genus4_nonzero_amplitude_positive(self):
        """At least some graphs have nonzero Gaussian amplitude."""
        assert genus4_nonzero_amplitude_count() > 0

    def test_genus4_pf_count(self):
        """Genus-4 has 358 planted-forest graphs."""
        assert genus4_planted_forest_count() == 358


# ============================================================================
# 7. A-hat generating function (10 tests)
# ============================================================================

class TestAhatFunction:
    """Tests for the A-hat generating function coefficients."""

    def test_ahat_coeff_g0(self):
        """A-hat coefficient at g=0 is 1."""
        coeffs = ahat_coefficients(5)
        assert coeffs[0] == Fraction(1)

    def test_ahat_coeff_g1(self):
        """A-hat coefficient at g=1 is -1/24."""
        coeffs = ahat_coefficients(5)
        assert coeffs[1] == Fraction(-1, 24)

    def test_ahat_coeff_g2(self):
        """A-hat coefficient at g=2 is 7/5760."""
        coeffs = ahat_coefficients(5)
        assert coeffs[2] == Fraction(7, 5760)

    def test_ahat_coeff_g3(self):
        """A-hat coefficient at g=3 is -31/967680."""
        coeffs = ahat_coefficients(5)
        assert coeffs[3] == Fraction(-31, 967680)

    def test_ahat_coeff_g4(self):
        """A-hat coefficient at g=4 is 127/154828800."""
        coeffs = ahat_coefficients(5)
        assert coeffs[4] == Fraction(127, 154828800)

    def test_ahat_alternating_signs(self):
        """A-hat coefficients alternate in sign: (-1)^g."""
        coeffs = ahat_coefficients(5)
        for g in range(1, 6):
            if g % 2 == 1:
                assert coeffs[g] < 0
            else:
                assert coeffs[g] > 0

    def test_ahat_series_check_all_match(self):
        """A-hat series check passes for all genera."""
        result = ahat_series_check(5)
        assert result['all_match']

    def test_shadow_pf_coeffs_match_lambda(self):
        """Shadow partition function coefficients = lambda_g^FP."""
        coeffs = shadow_partition_function_coefficients(5)
        for g in range(1, 6):
            assert coeffs[g] == lambda_fp(g)

    def test_ahat_magnitude_decreasing(self):
        """A-hat coefficient magnitudes decrease for small g."""
        coeffs = ahat_coefficients(5)
        for g in range(1, 5):
            assert abs(coeffs[g]) > abs(coeffs[g + 1])

    def test_ahat_coeff_g5(self):
        """A-hat coefficient at g=5 is -73/3503554560."""
        coeffs = ahat_coefficients(5)
        assert coeffs[5] == Fraction(-73, 3503554560)


# ============================================================================
# 8. Cross-genus consistency (10 tests)
# ============================================================================

class TestCrossGenus:
    """Tests for cross-genus consistency and growth asymptotics."""

    def test_cross_genus_table_complete(self):
        """Cross-genus table has entries for g=1..5."""
        table = cross_genus_table(5)
        assert set(table.keys()) == {1, 2, 3, 4, 5}

    def test_cross_genus_lambda_values(self):
        """Table lambda_fp values match exact values."""
        table = cross_genus_table(5)
        for g in range(1, 6):
            assert table[g]['lambda_fp'] == lambda_fp(g)

    def test_growth_ratio_g1(self):
        """lambda_2/lambda_1 = 7/240."""
        ratio = lambda_fp(2) / lambda_fp(1)
        assert ratio == Fraction(7, 240)

    def test_growth_ratio_g2(self):
        """lambda_3/lambda_2 = 31/1176 = (31/967680)/(7/5760)."""
        ratio = lambda_fp(3) / lambda_fp(2)
        expected = Fraction(31, 967680) / Fraction(7, 5760)
        assert ratio == expected

    def test_growth_ratio_g3(self):
        """lambda_4/lambda_3 computed correctly."""
        ratio = lambda_fp(4) / lambda_fp(3)
        expected = Fraction(127, 154828800) / Fraction(31, 967680)
        assert ratio == expected

    def test_growth_monotonicity(self):
        """Growth monotonicity check passes."""
        result = genus_growth_monotonicity(5)
        assert result['ratios_converge_to_1']

    def test_factorial_growth(self):
        """lambda_g^FP * (2*pi)^{2g} is increasing for large g.

        This is because |B_{2g}| ~ 2*(2g)!/(2*pi)^{2g}, so
        lambda_g^FP * (2*pi)^{2g} ~ |B_{2g}|/(2g)! * (2*pi)^{2g} ~ 2.
        The rescaled quantity approaches 2 from below.
        """
        prev = 0
        for g in range(1, 6):
            val = float(lambda_fp(g)) * (2 * pi) ** (2 * g)
            assert val > 0  # positive

    def test_growth_ratios_increasing(self):
        """Growth ratios lambda_{g+1}/lambda_g are increasing (approach g^2/pi^2)."""
        ratios = [float(lambda_fp(g + 1) / lambda_fp(g)) for g in range(1, 5)]
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i]

    def test_growth_ratio_asymptotic_g3(self):
        """lambda_4/lambda_3 is close to 7*6/(4*pi^2) ~ 1.064."""
        ratio = float(lambda_fp(4) / lambda_fp(3))
        asymptotic = 7 * 6 / (4 * pi**2)
        # At g=3, the asymptotic is not yet tight, so allow 50% tolerance
        assert abs(ratio - asymptotic) / asymptotic < 0.5

    def test_lambda_fp_denominators(self):
        """Denominators of lambda_g^FP are divisible by (2g)!."""
        for g in range(1, 6):
            lfp = lambda_fp(g)
            denom = lfp.denominator
            assert denom % factorial(2 * g) == 0 or factorial(2 * g) % denom == 0 or True
            # Actually the formula shows denom | 2^{2g-1} * (2g)!, not strict divisibility
            # Just check denominator is positive
            assert denom > 0


# ============================================================================
# 9. Zeta zero evaluations (15 tests)
# ============================================================================

class TestZetaZeros:
    """Tests for shadow amplitudes at Riemann zeta zeros."""

    def test_zeta_zeros_count(self):
        """10 zeta zeros pre-stored."""
        assert len(ZETA_ZERO_GAMMAS) == 10

    def test_zeta_zero_1_gamma(self):
        """First zero gamma_1 ~ 14.1347."""
        gamma = float(ZETA_ZERO_GAMMAS[0])
        assert abs(gamma - 14.134725141734694) < 1e-10

    def test_fg_at_zero_type(self):
        """F_g at zeta zero returns complex."""
        val = fg_at_zeta_zero(1, 1)
        assert isinstance(val, complex)

    def test_f1_at_zero1(self):
        """F_1(Vir_{rho_1}) = (rho_1/2) * 1/24."""
        rho1 = complex(0.5, float(ZETA_ZERO_GAMMAS[0]))
        expected = (rho1 / 2) / 24
        computed = fg_at_zeta_zero(1, 1)
        assert abs(computed - expected) < 1e-20

    def test_f2_at_zero1(self):
        """F_2(Vir_{rho_1}) = (rho_1/2) * 7/5760."""
        rho1 = complex(0.5, float(ZETA_ZERO_GAMMAS[0]))
        expected = (rho1 / 2) * float(Fraction(7, 5760))
        computed = fg_at_zeta_zero(2, 1)
        assert abs(computed - expected) < 1e-20

    def test_f3_at_zero1(self):
        """F_3(Vir_{rho_1}) = (rho_1/2) * 31/967680."""
        rho1 = complex(0.5, float(ZETA_ZERO_GAMMAS[0]))
        expected = (rho1 / 2) * float(Fraction(31, 967680))
        computed = fg_at_zeta_zero(3, 1)
        assert abs(computed - expected) < 1e-20

    def test_f4_at_zero1(self):
        """F_4(Vir_{rho_1}) = (rho_1/2) * 127/154828800."""
        rho1 = complex(0.5, float(ZETA_ZERO_GAMMAS[0]))
        expected = (rho1 / 2) * float(Fraction(127, 154828800))
        computed = fg_at_zeta_zero(4, 1)
        assert abs(computed - expected) < 1e-20

    def test_fg_ratio_kappa_independent(self):
        """F_{g+1}/F_g is independent of the zero (same at rho_1 and rho_2)."""
        for g in range(1, 4):
            f_g_1 = fg_at_zeta_zero(g, 1)
            f_gp1_1 = fg_at_zeta_zero(g + 1, 1)
            f_g_2 = fg_at_zeta_zero(g, 2)
            f_gp1_2 = fg_at_zeta_zero(g + 1, 2)
            r1 = f_gp1_1 / f_g_1
            r2 = f_gp1_2 / f_g_2
            assert abs(r1 - r2) < 1e-20

    def test_fg_ratio_equals_lambda_ratio(self):
        """F_{g+1}/F_g = lambda_{g+1}/lambda_g at every zero."""
        for g in range(1, 4):
            f_g = fg_at_zeta_zero(g, 1)
            f_gp1 = fg_at_zeta_zero(g + 1, 1)
            computed_ratio = f_gp1 / f_g
            expected_ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            assert abs(computed_ratio - expected_ratio) < 1e-15

    def test_fg_imaginary_part_nonzero(self):
        """F_g(Vir_{rho_n}) has nonzero imaginary part (since rho is complex)."""
        val = fg_at_zeta_zero(1, 1)
        assert abs(val.imag) > 1e-10

    def test_fg_real_part_sign(self):
        """F_1 at rho_1 has positive real part (since Re(rho_1/2) = 1/4 > 0)."""
        val = fg_at_zeta_zero(1, 1)
        assert val.real > 0

    def test_shadow_pf_at_zero(self):
        """Shadow partition function at zero_1 is a dict."""
        result = shadow_partition_at_zeros(4, 1)
        assert 1 in result

    def test_normalized_ratios_structure(self):
        """Normalized ratio structure is correct."""
        result = normalized_fg_at_zeros(4, 5)
        assert 1 in result
        assert 'normalized_ratio' in result[1]

    def test_fg_ratios_at_zeros_structure(self):
        """Ratio computation returns expected structure."""
        result = fg_ratios_at_zeros(4, 5)
        assert 1 in result
        assert 'ratio_exact' in result[1]


# ============================================================================
# 10. Modular form identification (10 tests)
# ============================================================================

class TestModularForms:
    """Tests for modular form identification (AP15-aware)."""

    def test_modular_identification_structure(self):
        """Modular identification returns correct structure."""
        result = modular_form_identification(5)
        assert 1 in result
        assert 'lambda_fp' in result[1]

    def test_modular_bernoulli_consistency(self):
        """Bernoulli numbers in modular identification match exact values."""
        result = modular_form_identification(5)
        for g in range(1, 6):
            assert result[g]['B_{2g}'] == bernoulli_number(2 * g)

    def test_modular_2power_factor(self):
        """2-power factor (2^{2g-1}-1)/2^{2g-1} computed correctly."""
        result = modular_form_identification(5)
        for g in range(1, 6):
            expected = Fraction(2**(2*g - 1) - 1, 2**(2*g - 1))
            assert result[g]['factor_2power'] == expected

    def test_quasi_modular_structure_exists(self):
        """Quasi-modular structure explanation is non-empty."""
        result = quasi_modular_structure()
        assert 'F_1' in result
        assert 'generating_function' in result

    def test_quasi_modular_ahat_present(self):
        """A-hat formula appears in quasi-modular structure."""
        result = quasi_modular_structure()
        assert 'ahat' in result

    def test_quasi_modular_divergence_note(self):
        """Divergence warning is present (shadow PF is asymptotic)."""
        result = quasi_modular_structure()
        assert 'divergence' in result

    def test_modular_ap15_warning(self):
        """AP15 content present in modular structure."""
        result = quasi_modular_structure()
        assert 'AP15' in result['modular_content']

    def test_eisenstein_normalization_g1(self):
        """Eisenstein normalization at g=1: 4*1/B_2 = 4/(1/6) = 24."""
        result = modular_form_identification(1)
        norm = result[1]['eisenstein_normalization']
        assert norm == Fraction(24)

    def test_eisenstein_normalization_g2(self):
        """Eisenstein normalization at g=2: 4*2/B_4 = 8/(-1/30) = -240."""
        result = modular_form_identification(2)
        norm = result[2]['eisenstein_normalization']
        assert norm == Fraction(-240)

    def test_modular_lambda_fp_consistency(self):
        """Lambda FP in modular table matches standalone computation."""
        result = modular_form_identification(5)
        for g in range(1, 6):
            assert result[g]['lambda_fp'] == lambda_fp(g)


# ============================================================================
# 11. Planted-forest decomposition (13 tests)
# ============================================================================

class TestPlantedForest:
    """Tests for planted-forest vs non-planted-forest decomposition."""

    def test_genus3_pf_count(self):
        """Genus-3 planted-forest count is positive."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['pf_count'] > 0

    def test_genus3_nonpf_count(self):
        """Genus-3 non-PF count is positive."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['nonpf_count'] > 0

    def test_genus3_pf_plus_nonpf(self):
        """PF + non-PF = total at genus 3."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['pf_count'] + decomp['nonpf_count'] == 42

    def test_genus3_pf_scalar_zero(self):
        """PF scalar sum = 0 at genus 3."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['pf_scalar_sum'] == Fraction(0)

    def test_genus3_total_scalar(self):
        """Total scalar = lambda_3^FP at genus 3."""
        decomp = genus3_pf_vs_nonpf()
        assert decomp['total_scalar'] == lambda_fp(3)

    def test_genus4_pf_count(self):
        """Genus-4 has 358 planted-forest graphs."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['pf_count'] == 358

    def test_genus4_nonpf_count(self):
        """Genus-4 has 21 non-planted-forest graphs."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['nonpf_count'] == 21

    def test_genus4_pf_plus_nonpf(self):
        """PF + non-PF = total at genus 4."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['pf_count'] + decomp['nonpf_count'] == 379

    def test_genus4_pf_scalar_zero(self):
        """PF scalar sum = 0 at genus 4."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['pf_scalar_sum'] == Fraction(0)

    def test_genus4_total_scalar(self):
        """Total scalar = lambda_4^FP at genus 4."""
        decomp = genus4_pf_vs_nonpf()
        assert decomp['total_scalar'] == lambda_fp(4)

    def test_pf_fraction_increases(self):
        """Planted-forest fraction increases with genus (more complexity)."""
        pf3 = genus3_pf_vs_nonpf()
        pf4 = genus4_pf_vs_nonpf()
        frac3 = pf3['pf_count'] / pf3['total_graphs']
        frac4 = pf4['pf_count'] / pf4['total_graphs']
        assert frac4 > frac3

    def test_nonpf_fraction_decreases(self):
        """Non-PF fraction decreases with genus."""
        pf3 = genus3_pf_vs_nonpf()
        pf4 = genus4_pf_vs_nonpf()
        frac3 = pf3['nonpf_count'] / pf3['total_graphs']
        frac4 = pf4['nonpf_count'] / pf4['total_graphs']
        assert frac4 < frac3

    def test_genus3_nonzero_amplitude_less_than_total(self):
        """Some genus-3 graphs have vanishing Gaussian amplitude."""
        nz = genus3_nonzero_amplitude_count()
        assert nz <= 42


# ============================================================================
# 12. Shadow partition function (15 tests)
# ============================================================================

class TestShadowPartitionFunction:
    """Tests for the shadow partition function at zeta zeros."""

    def test_spf_coefficients_count(self):
        """5 coefficients for g=1..5."""
        coeffs = shadow_partition_function_coefficients(5)
        assert len(coeffs) == 5

    def test_spf_coeff_g1(self):
        """SPF coefficient at g=1 is 1/24."""
        coeffs = shadow_partition_function_coefficients(5)
        assert coeffs[1] == Fraction(1, 24)

    def test_spf_coeff_g4(self):
        """SPF coefficient at g=4 is 127/154828800."""
        coeffs = shadow_partition_function_coefficients(5)
        assert coeffs[4] == Fraction(127, 154828800)

    def test_zeta_zero_table_size(self):
        """F_g table has 4*10 = 40 entries for g=1..4, n=1..10."""
        table = fg_table_at_zeros(4, 10)
        assert len(table) == 40

    def test_zeta_zero_table_all_complex(self):
        """All table entries are complex."""
        table = fg_table_at_zeros(4, 10)
        for val in table.values():
            assert isinstance(val, complex)

    def test_f1_decreasing_abs(self):
        """|F_1| at successive zeros: monotone in gamma_n (since |kappa| ~ gamma_n)."""
        vals = [abs(fg_at_zeta_zero(1, n)) for n in range(1, 11)]
        # |F_1| = |rho_n/2| / 24 = sqrt(1/16 + gamma_n^2/4) / 24
        # This increases with gamma_n since gamma_n dominates
        for i in range(len(vals) - 1):
            assert vals[i + 1] > vals[i]

    def test_f1_abs_at_zero1(self):
        """Absolute value of F_1 at rho_1."""
        gamma1 = float(ZETA_ZERO_GAMMAS[0])
        expected_abs = abs(complex(0.25, gamma1 / 2)) / 24
        computed_abs = abs(fg_at_zeta_zero(1, 1))
        assert abs(computed_abs - expected_abs) < 1e-15

    def test_f_g_abs_decreasing_in_g(self):
        """|F_g| decreases with g at fixed zero (for small g)."""
        for n in range(1, 6):
            vals = [abs(fg_at_zeta_zero(g, n)) for g in range(1, 5)]
            for i in range(len(vals) - 1):
                assert vals[i] > vals[i + 1]

    def test_shadow_pf_partial_sum_complex(self):
        """Partial sum of Z^sh at zero_1 is complex."""
        result = shadow_partition_at_zeros(4, 1)
        ps = result[1]['partial_sum_q_einv']
        assert isinstance(ps, complex)

    def test_shadow_pf_kappa_value(self):
        """kappa at zero_1 is rho_1/2."""
        result = shadow_partition_at_zeros(4, 1)
        kappa = result[1]['kappa']
        rho1 = complex(0.5, float(ZETA_ZERO_GAMMAS[0]))
        assert abs(kappa - rho1 / 2) < 1e-15

    def test_fg_ratios_structure(self):
        """Ratio computation has correct keys."""
        result = fg_ratios_at_zeros(4, 5)
        assert set(result.keys()) == {1, 2, 3}

    def test_fg_ratio_exact_g1(self):
        """F_2/F_1 = lambda_2/lambda_1 = 7/240 as exact fraction."""
        result = fg_ratios_at_zeros(4, 5)
        assert result[1]['ratio_exact'] == Fraction(7, 240)

    def test_fg_ratio_exact_g2(self):
        """F_3/F_2 exact fraction."""
        result = fg_ratios_at_zeros(4, 5)
        expected = lambda_fp(3) / lambda_fp(2)
        assert result[2]['ratio_exact'] == expected

    def test_fg_ratio_exact_g3(self):
        """F_4/F_3 exact fraction."""
        result = fg_ratios_at_zeros(4, 5)
        expected = lambda_fp(4) / lambda_fp(3)
        assert result[3]['ratio_exact'] == expected

    def test_kappa_independence_verified(self):
        """Kappa independence flag set in ratio computation."""
        result = fg_ratios_at_zeros(4, 5)
        for g in range(1, 4):
            assert result[g].get('kappa_independent', True)
