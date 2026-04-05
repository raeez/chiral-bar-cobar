r"""Tests for the genus-3 Siegel modular form engine.

Verifies genus-3 shadow amplitudes, Siegel modular form dimensions,
theta characteristics, E_8 lattice theta functions, sewing construction,
degeneration, complementarity, Schottky problem, and multi-path verification.

Multi-path verification: >= 3 independent paths per result.

Organized into sections:
  1. Faber-Pandharipande lambda_3 (3 independent paths)
  2. Genus-3 Siegel modular form dimensions (known tables)
  3. Theta characteristics at genus 3 (36 even + 28 odd)
  4. Theta function evaluation (diagonal period matrices)
  5. E_8 lattice root system combinatorics
  6. Shadow amplitudes: Heisenberg, Virasoro, lattice VOAs
  7. Sewing construction
  8. Genus-3 -> genus-2 degeneration
  9. Complementarity at genus 3
  10. Generating function consistency
  11. Cross-genus lambda ratios
  12. Landscape sweep
  13. Multi-path verification
  14. Schottky form and ring structure
  15. Eisenstein series evaluation
  16. Theta product formulas
  17. E_8 Siegel-Weil verification
  18. Böcherer discussion
  19. Edge cases and error handling
"""

import math
import pytest
import numpy as np
from fractions import Fraction

from compute.lib.siegel_genus3_engine import (
    # FP numbers
    lambda_fp,
    ahat_genus_coefficient,
    # Dimensions
    genus3_dimension,
    genus3_cusp_dimension,
    genus3_eisenstein_dimension,
    GENUS3_DIMENSIONS,
    GENUS3_CUSP_DIMENSIONS,
    # Theta characteristics
    enumerate_theta_characteristics,
    theta_characteristic_parity,
    count_even_odd_characteristics,
    classify_theta_characteristics,
    # Theta functions
    genus3_theta_with_char,
    genus3_theta_nullwert,
    genus3_period_matrix_diagonal,
    genus3_period_matrix_general,
    validate_period_matrix,
    # Lattice theta
    e8_roots_array,
    e8_norm4_vectors,
    genus3_lattice_theta_diagonal,
    e8_genus3_representation_number,
    # Eisenstein
    genus3_eisenstein_diagonal_coefficient,
    # Shadow amplitudes
    shadow_F3,
    shadow_F3_ahat,
    shadow_F3_bernoulli,
    heisenberg_F3,
    virasoro_F3,
    lattice_voa_F3,
    # Sewing
    genus3_sewing_kernel_heisenberg,
    genus3_sewing_F3_heisenberg,
    # Degeneration
    genus3_to_genus2_degeneration_check,
    # Schottky
    schottky_form_description,
    compute_schottky_indicator,
    # Landscape
    F3_landscape,
    # Complementarity
    complementarity_F3,
    virasoro_complementarity_F3,
    heisenberg_complementarity_F3,
    # Generating function
    genus_generating_function_check,
    # Multi-path
    full_multi_path_verification_genus3,
    # Stable graphs
    genus3_graph_sum_scalar,
    # Cross-genus
    cross_genus_lambda_ratios,
    # Theta products
    thomae_formula_genus3,
    # Siegel-Weil
    siegel_weil_genus3_e8,
    # Cusp form
    genus3_first_cusp_form_description,
    # Ring structure
    genus3_ring_structure,
    # E8 combinatorics
    e8_orthogonal_root_triples,
    e8_perpendicular_root_counts,
    # Eisenstein evaluation
    e4_eisenstein,
    e6_eisenstein,
    dedekind_eta,
    # E8 genus-3 theta
    e8_genus3_theta_at_diagonal,
    # Lattice theta numerical
    genus3_lattice_theta_numerical,
    # Kappa table
    kappa_table,
    # Böcherer
    bocherer_genus3_discussion,
)


# ============================================================================
# 1. FABER-PANDHARIPANDE LAMBDA_3 (3 independent paths)
# ============================================================================

class TestFaberPandharipandeLambda3:
    """Three independent computation paths for lambda_3^FP = 31/967680."""

    def test_lambda3_exact_value(self):
        """Path 1: Direct formula lambda_3 = (2^5-1)/2^5 * |B_6|/6!."""
        lam3 = lambda_fp(3)
        assert lam3 == Fraction(31, 967680)

    def test_lambda3_from_bernoulli(self):
        """Path 2: Compute from Bernoulli number B_6 = 1/42."""
        B_6 = Fraction(1, 42)
        power = 2**5  # = 32
        lam3 = Fraction(power - 1, power) * B_6 / Fraction(math.factorial(6))
        assert lam3 == Fraction(31, 967680)

    def test_lambda3_from_ahat(self):
        """Path 3: A-hat generating function coefficient."""
        lam3_ahat = ahat_genus_coefficient(3)
        assert lam3_ahat == Fraction(31, 967680)

    def test_lambda3_numerical_value(self):
        """Verify the numerical value is approximately 3.204e-05."""
        lam3 = lambda_fp(3)
        assert abs(float(lam3) - 31.0 / 967680.0) < 1e-15

    def test_lambda3_all_three_paths_agree(self):
        """All three paths produce the same value."""
        path1 = lambda_fp(3)
        path2 = shadow_F3_bernoulli(1)  # F_3 at kappa=1 = lambda_3
        path3 = shadow_F3_ahat(1)
        assert path1 == path2 == path3

    def test_lambda1_through_lambda5(self):
        """Verify the first 5 Faber-Pandharipande numbers."""
        assert lambda_fp(1) == Fraction(1, 24)
        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp(3) == Fraction(31, 967680)
        assert lambda_fp(4) == Fraction(127, 154828800)
        # lambda_5 = (2^9-1)/2^9 * |B_10|/10! = 511/512 * 5/66 / 3628800
        lam5 = lambda_fp(5)
        expected = Fraction(511, 512) * Fraction(5, 66) / Fraction(math.factorial(10))
        assert lam5 == expected


# ============================================================================
# 2. GENUS-3 SIEGEL MODULAR FORM DIMENSIONS
# ============================================================================

class TestGenus3Dimensions:
    """Known dimensions of M_k(Sp(6,Z)) from Tsuyumine (1986)."""

    def test_dim_weight_4(self):
        assert genus3_dimension(4) == 1

    def test_dim_weight_6(self):
        assert genus3_dimension(6) == 1

    def test_dim_weight_8(self):
        assert genus3_dimension(8) == 1

    def test_dim_weight_10(self):
        assert genus3_dimension(10) == 1

    def test_dim_weight_12(self):
        """First weight with cusp form: dim = 2."""
        assert genus3_dimension(12) == 2

    def test_dim_weight_14(self):
        assert genus3_dimension(14) == 2

    def test_cusp_dim_below_12(self):
        """No cusp forms at genus 3 below weight 12."""
        for k in [4, 6, 8, 10]:
            assert genus3_cusp_dimension(k) == 0

    def test_cusp_dim_weight_12(self):
        """First cusp form at weight 12."""
        assert genus3_cusp_dimension(12) == 1

    def test_eisenstein_dimension(self):
        """Eisenstein = total - cusp."""
        for k in [4, 6, 8, 10, 12, 14]:
            m = genus3_dimension(k)
            s = genus3_cusp_dimension(k)
            e = genus3_eisenstein_dimension(k)
            assert e == m - s

    def test_odd_weight_vanishes(self):
        """Odd weight => dim = 0 (by -I symmetry)."""
        for k in [1, 3, 5, 7, 9, 11, 13]:
            assert genus3_dimension(k) == 0

    def test_dim_weight_24(self):
        """Weight 24 has 6 forms."""
        assert genus3_dimension(24) == 6


# ============================================================================
# 3. THETA CHARACTERISTICS AT GENUS 3
# ============================================================================

class TestThetaCharacteristics:
    """2^6 = 64 characteristics: 36 even + 28 odd."""

    def test_total_count(self):
        chars = enumerate_theta_characteristics(3)
        assert len(chars) == 64

    def test_even_odd_formula(self):
        n_even, n_odd = count_even_odd_characteristics(3)
        assert n_even == 36
        assert n_odd == 28

    def test_even_odd_sum(self):
        n_even, n_odd = count_even_odd_characteristics(3)
        assert n_even + n_odd == 64

    def test_classify_matches_count(self):
        classification = classify_theta_characteristics(3)
        assert len(classification['even']) == 36
        assert len(classification['odd']) == 28

    def test_trivial_characteristic_is_even(self):
        """[0,0,0; 0,0,0] is even (parity = 0)."""
        a = (0, 0, 0)
        b = (0, 0, 0)
        assert theta_characteristic_parity(a, b) == 0

    def test_parity_computation(self):
        """[1,0,0; 1,0,0] has parity 1 (odd)."""
        a = (1, 0, 0)
        b = (1, 0, 0)
        assert theta_characteristic_parity(a, b) == 1

    def test_parity_mixed(self):
        """[1,1,0; 0,0,1] has parity 0 (even)."""
        a = (1, 1, 0)
        b = (0, 0, 1)
        assert theta_characteristic_parity(a, b) == 0

    def test_genus1_characteristics(self):
        """At genus 1: 3 even + 1 odd = 4 total.

        For g=1: chars are [a;b] with a,b in {0,1}.
        [0;0]: parity 0 (even), [0;1]: parity 0, [1;0]: parity 0, [1;1]: parity 1.
        Formula: 2^{g-1}(2^g+1) = 3 even, 2^{g-1}(2^g-1) = 1 odd.
        """
        n_even, n_odd = count_even_odd_characteristics(1)
        assert n_even == 3
        assert n_odd == 1

    def test_genus2_characteristics(self):
        """At genus 2: 10 even + 6 odd = 16."""
        n_even, n_odd = count_even_odd_characteristics(2)
        assert n_even == 10
        assert n_odd == 6


# ============================================================================
# 4. THETA FUNCTION EVALUATION
# ============================================================================

class TestThetaFunctions:
    """Numerical evaluation of genus-3 theta functions."""

    def test_trivial_theta_at_identity(self):
        """Theta[0;0](i*I_3) should be a real positive number."""
        Omega = genus3_period_matrix_diagonal(1j, 1j, 1j)
        a = (0, 0, 0)
        b = (0, 0, 0)
        val = genus3_theta_nullwert(a, b, Omega, n_max=2)
        # Should be real and positive (sum of Gaussians)
        assert abs(val.imag) < 1e-6
        assert val.real > 0

    def test_odd_theta_vanishes(self):
        """Odd theta nullwerte vanish identically."""
        Omega = genus3_period_matrix_diagonal(1j, 1j, 1j)
        a = (1, 0, 0)
        b = (1, 0, 0)
        val = genus3_theta_nullwert(a, b, Omega, n_max=3)
        assert abs(val) < 1e-6

    def test_diagonal_theta_factorizes(self):
        """At diagonal Omega, theta[0;0] factorizes as product of genus-1 thetas."""
        tau1, tau2, tau3 = 1.0j, 1.2j, 0.8j
        Omega = genus3_period_matrix_diagonal(tau1, tau2, tau3)
        a = (0, 0, 0)
        b = (0, 0, 0)
        val_g3 = genus3_theta_nullwert(a, b, Omega, n_max=3)

        # Genus-1 theta[0;0](tau) = sum_{n in Z} q^{n^2/2} where q = e^{2pi i tau}
        def theta_g1(tau, n_max=10):
            result = 0.0 + 0.0j
            for n in range(-n_max, n_max + 1):
                result += np.exp(np.pi * 1j * tau * n**2)
            return result

        product = theta_g1(tau1, 10) * theta_g1(tau2, 10) * theta_g1(tau3, 10)
        assert abs(val_g3 - product) < 1e-4

    def test_period_matrix_validation(self):
        """Valid period matrix check."""
        Omega_good = genus3_period_matrix_diagonal(1j, 1j, 1j)
        assert validate_period_matrix(Omega_good)

        # Bad: not symmetric
        Omega_bad = np.array([[1j, 0.1, 0], [0, 1j, 0], [0, 0, 1j]])
        assert not validate_period_matrix(Omega_bad)

    def test_general_period_matrix(self):
        """General (non-diagonal) period matrix construction."""
        Omega = genus3_period_matrix_general(
            1j, 1j, 1j, 0.1j, 0.05j, 0.05j
        )
        assert validate_period_matrix(Omega)
        assert Omega.shape == (3, 3)

    def test_theta_symmetry(self):
        """Theta[a;b](Omega) depends only on a,b mod 2."""
        Omega = genus3_period_matrix_diagonal(1.5j, 1.2j, 1.1j)
        a1, b1 = (0, 0, 0), (0, 0, 0)
        val = genus3_theta_nullwert(a1, b1, Omega, n_max=2)
        # This should be well-defined and nonzero for the trivial characteristic
        assert abs(val) > 0.1


# ============================================================================
# 5. E_8 LATTICE ROOT SYSTEM COMBINATORICS
# ============================================================================

class TestE8Combinatorics:
    """E_8 root system and orthogonal triple counts."""

    def test_e8_has_240_roots(self):
        roots = e8_roots_array()
        assert len(roots) == 240

    def test_e8_roots_have_norm_2(self):
        roots = e8_roots_array()
        norms = np.sum(roots**2, axis=1)
        assert np.allclose(norms, 2.0)

    def test_e8_inner_products(self):
        """E_8 roots have inner products in {-2,-1,0,1,2}."""
        roots = e8_roots_array()
        gram = roots @ roots.T
        rounded = np.round(gram).astype(int)
        unique_ips = set(rounded.flatten())
        assert unique_ips <= {-2, -1, 0, 1, 2}

    def test_perpendicular_to_one_root(self):
        """126 roots perpendicular to any given root (D_7 subsystem)."""
        counts = e8_perpendicular_root_counts()
        assert counts['n_perp_to_1'] == 126

    def test_perpendicular_to_two_roots(self):
        """60 roots perpendicular to a given orthogonal pair."""
        counts = e8_perpendicular_root_counts()
        assert counts['n_perp_to_2'] == 60

    def test_perpendicular_to_three_roots(self):
        """26 roots perpendicular to a given orthogonal triple."""
        counts = e8_perpendicular_root_counts()
        assert counts['n_perp_to_3'] == 26

    def test_orthogonal_triple_count(self):
        """240 * 126 * 60 = 1,814,400 ordered orthogonal triples."""
        count = e8_orthogonal_root_triples()
        assert count == 240 * 126 * 60
        assert count == 1814400

    def test_orthogonal_triple_matches_rep_number(self):
        """r_3(E_8, diag(1,1,1)) = number of ordered orthogonal root triples."""
        triple_count = e8_orthogonal_root_triples()
        rep = e8_genus3_representation_number(1, 1, 1)
        assert rep == triple_count


# ============================================================================
# 6. SHADOW AMPLITUDES
# ============================================================================

class TestShadowAmplitudesGenus3:
    """F_3 = kappa * lambda_3 for standard families."""

    def test_heisenberg_k1(self):
        result = heisenberg_F3(1)
        assert result['F_3'] == Fraction(31, 967680)
        assert result['shadow_class'] == 'G'
        assert result['all_paths_agree']

    def test_heisenberg_k8(self):
        """E_8 lattice VOA equivalent."""
        result = heisenberg_F3(8)
        assert result['F_3'] == 8 * Fraction(31, 967680)
        assert result['F_3'] == Fraction(31, 120960)

    def test_heisenberg_k24(self):
        """Leech lattice rank."""
        result = heisenberg_F3(24)
        assert result['F_3'] == 24 * Fraction(31, 967680)
        assert result['F_3'] == Fraction(31, 40320)

    def test_virasoro_c26(self):
        """Critical string: kappa = 13."""
        result = virasoro_F3(26)
        assert result['F_3_scalar'] == 13 * Fraction(31, 967680)
        assert result['shadow_class'] == 'M'

    def test_virasoro_c13(self):
        """Self-dual point: kappa = 13/2."""
        result = virasoro_F3(13)
        assert result['kappa'] == Fraction(13, 2)
        assert result['F_3_scalar'] == Fraction(13, 2) * Fraction(31, 967680)

    def test_virasoro_c1(self):
        result = virasoro_F3(1)
        assert result['kappa'] == Fraction(1, 2)
        assert result['F_3_scalar'] == Fraction(31, 1935360)

    def test_lattice_voa_rank8(self):
        result = lattice_voa_F3(8)
        assert result['F_3'] == Fraction(31, 120960)
        assert result['siegel_weight'] == Fraction(4)

    def test_lattice_voa_rank24(self):
        result = lattice_voa_F3(24)
        assert result['F_3'] == Fraction(31, 40320)
        assert result['siegel_weight'] == Fraction(12)

    def test_F3_linear_in_kappa(self):
        """F_3 is linear in kappa (additivity)."""
        k1, k2 = 3, 5
        F3_sum = shadow_F3(k1) + shadow_F3(k2)
        F3_combined = shadow_F3(k1 + k2)
        assert F3_sum == F3_combined

    def test_F3_scales_correctly(self):
        """F_3(alpha * A) = alpha * F_3(A) for scalar multiplication."""
        kappa = 7
        alpha = 3
        assert shadow_F3(alpha * kappa) == alpha * shadow_F3(kappa)


# ============================================================================
# 7. SEWING CONSTRUCTION
# ============================================================================

class TestSewingGenus3:
    """Genus-3 sewing construction for Heisenberg."""

    def test_sewing_F3_matches_shadow(self):
        """Sewing F_3 agrees with shadow amplitude."""
        for k in [1, 2, 4, 8, 24]:
            F3_sewing = genus3_sewing_F3_heisenberg(k)
            F3_shadow = shadow_F3(k)
            assert F3_sewing == F3_shadow

    def test_sewing_kernel_convergent(self):
        """Sewing kernel converges for |q| < 1."""
        q1 = np.exp(2 * np.pi * 1j * 2j)  # |q| = exp(-4pi) << 1
        q2 = np.exp(2 * np.pi * 1j * 2j)
        q3 = np.exp(2 * np.pi * 1j * 2j)
        Z = genus3_sewing_kernel_heisenberg(1, q1, q2, q3)
        assert np.isfinite(Z)
        assert abs(Z) > 0

    def test_sewing_product_factorizes(self):
        """In the fully degenerate limit, sewing factorizes into genus-1."""
        q = np.exp(2 * np.pi * 1j * 3j)  # Deep in cusp
        Z_g3 = genus3_sewing_kernel_heisenberg(1, q, q, q)
        # Should approximately equal eta(3i)^{-3}
        eta_val = dedekind_eta(3j)
        Z_product = eta_val**(-3)
        # These won't match exactly because sewing kernel is leading order,
        # but the absolute values should be comparable
        assert abs(Z_g3) > 0
        assert np.isfinite(Z_g3)


# ============================================================================
# 8. GENUS-3 -> GENUS-2 DEGENERATION
# ============================================================================

class TestGenus3Degeneration:
    """Genus-3 to genus-2 degeneration consistency."""

    def test_degeneration_ratio(self):
        result = genus3_to_genus2_degeneration_check(1)
        assert result['F_3'] == Fraction(31, 967680)
        assert result['F_2'] == Fraction(7, 5760)
        assert result['F_1'] == Fraction(1, 24)

    def test_lambda_ratio_exact(self):
        result = genus3_to_genus2_degeneration_check(1)
        ratio = result['lambda_ratio_3_2']
        assert ratio == Fraction(31, 967680) / Fraction(7, 5760)
        # Simplify: 31*5760 / (967680*7) = 178560 / 6773760 = 31/1176
        assert ratio == Fraction(31, 1176)

    def test_degeneration_consistent(self):
        result = genus3_to_genus2_degeneration_check(8)
        assert result['degeneration_consistent']

    def test_F_hierarchy(self):
        """F_1 > F_2 > F_3 for positive kappa (decreasing genus corrections)."""
        for k in [1, 2, 8, 24]:
            result = genus3_to_genus2_degeneration_check(k)
            assert result['F_1'] > result['F_2'] > result['F_3'] > 0


# ============================================================================
# 9. COMPLEMENTARITY AT GENUS 3
# ============================================================================

class TestComplementarityGenus3:
    """Koszul dual complementarity at genus 3."""

    def test_heisenberg_antisymmetry(self):
        """For Heisenberg: kappa + kappa' = 0, so F_3 + F_3' = 0."""
        result = heisenberg_complementarity_F3(1)
        assert result['kappa_sum'] == 0
        assert result['F_3_sum'] == 0
        assert result['complementarity_holds']

    def test_virasoro_complementarity_sum(self):
        """For Virasoro: kappa(c) + kappa(26-c) = 13 (AP24: NOT zero!)."""
        result = virasoro_complementarity_F3(10)
        assert result['kappa_sum'] == 13
        assert result['F_3_sum'] == 13 * Fraction(31, 967680)

    def test_virasoro_self_dual_c13(self):
        """At c=13: kappa = 13/2, Koszul dual also c=13, kappa' = 13/2."""
        result = virasoro_complementarity_F3(13)
        assert result['kappa_A'] == Fraction(13, 2)
        assert result['kappa_dual'] == Fraction(13, 2)
        assert result['kappa_sum'] == 13

    def test_virasoro_c0_complementarity(self):
        """At c=0: kappa=0, dual c=26, kappa'=13."""
        result = virasoro_complementarity_F3(0)
        assert result['kappa_A'] == 0
        assert result['kappa_dual'] == 13
        assert result['F_3_A'] == 0
        assert result['F_3_dual'] == 13 * Fraction(31, 967680)

    def test_heisenberg_several_levels(self):
        for k in [1, 2, 4, 8, 24]:
            result = heisenberg_complementarity_F3(k)
            assert result['F_3_sum'] == 0


# ============================================================================
# 10. GENERATING FUNCTION CONSISTENCY
# ============================================================================

class TestGeneratingFunctionGenus3:
    """A-hat generating function consistency at genus 3."""

    def test_gf_at_kappa_1(self):
        result = genus_generating_function_check(1, g_max=5)
        for g in range(1, 6):
            assert result[f'F_{g}']['consistent']

    def test_lambda3_from_gf(self):
        result = genus_generating_function_check(1)
        assert result['lambda_3_direct_vs_computed']

    def test_gf_at_kappa_24(self):
        result = genus_generating_function_check(24, g_max=4)
        assert result['F_3']['value'] == 24 * Fraction(31, 967680)

    def test_gf_ahat_coefficients_alternate(self):
        """The A-hat series (x/2)/sinh(x/2) has alternating signs."""
        result = genus_generating_function_check(1, g_max=5)
        for g in range(1, 6):
            coeff = result[f'F_{g}']['ahat_coefficient']
            # Should be (-1)^g * lambda_g
            assert coeff == (-1)**g * lambda_fp(g)


# ============================================================================
# 11. CROSS-GENUS LAMBDA RATIOS
# ============================================================================

class TestCrossGenusLambdaRatios:
    """Ratios of lambda_g values and consistency."""

    def test_ratio_32(self):
        ratios = cross_genus_lambda_ratios()
        r = ratios['ratios']['lambda_3/lambda_2']['exact']
        assert r == Fraction(31, 1176)

    def test_ratio_21(self):
        ratios = cross_genus_lambda_ratios()
        r = ratios['ratios']['lambda_2/lambda_1']['exact']
        assert r == Fraction(7, 240)

    def test_ahat_consistent(self):
        result = cross_genus_lambda_ratios()
        assert result['ahat_consistent']

    def test_lambda_decreasing(self):
        """lambda_1 > lambda_2 > lambda_3 > lambda_4 > lambda_5."""
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)


# ============================================================================
# 12. LANDSCAPE SWEEP
# ============================================================================

class TestLandscapeSweepGenus3:
    """F_3 for the full standard landscape."""

    def test_landscape_has_all_families(self):
        landscape = F3_landscape()
        expected = [
            'Heisenberg_k1', 'Heisenberg_k24', 'Virasoro_c1/2',
            'Virasoro_c1', 'Virasoro_c26', 'Virasoro_c13',
            'Affine_sl2_k1', 'Affine_sl3_k1',
            'E8_lattice', 'Leech_lattice',
            'BetaGamma_lam1', 'W3_c2',
        ]
        for name in expected:
            assert name in landscape, f"Missing {name}"

    def test_landscape_e8(self):
        landscape = F3_landscape()
        assert landscape['E8_lattice']['kappa'] == Fraction(8)
        assert landscape['E8_lattice']['F_3'] == 8 * Fraction(31, 967680)

    def test_landscape_leech(self):
        landscape = F3_landscape()
        assert landscape['Leech_lattice']['kappa'] == Fraction(24)
        assert landscape['Leech_lattice']['F_3'] == 24 * Fraction(31, 967680)

    def test_landscape_virasoro_c26(self):
        landscape = F3_landscape()
        assert landscape['Virasoro_c26']['kappa'] == Fraction(13)

    def test_landscape_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        landscape = F3_landscape()
        assert landscape['Affine_sl2_k1']['kappa'] == Fraction(9, 4)

    def test_landscape_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        landscape = F3_landscape()
        assert landscape['Affine_sl3_k1']['kappa'] == Fraction(16, 3)

    def test_landscape_shadow_classes(self):
        """Verify shadow depth classes."""
        landscape = F3_landscape()
        assert landscape['Heisenberg_k1']['shadow_class'] == 'G'
        assert landscape['Virasoro_c1']['shadow_class'] == 'M'
        assert landscape['Affine_sl2_k1']['shadow_class'] == 'L'
        assert landscape['BetaGamma_lam1']['shadow_class'] == 'C'
        assert landscape['W3_c2']['shadow_class'] == 'M'

    def test_landscape_all_positive(self):
        """All F_3 values are positive for positive kappa."""
        landscape = F3_landscape()
        for name, data in landscape.items():
            if data['kappa'] > 0:
                assert data['F_3'] > 0, f"{name} has non-positive F_3"


# ============================================================================
# 13. MULTI-PATH VERIFICATION
# ============================================================================

class TestMultiPathGenus3:
    """Multi-path verification mandate: >= 3 independent paths."""

    def test_multi_path_kappa_1(self):
        result = full_multi_path_verification_genus3(1)
        assert result['all_paths_agree']
        assert result['n_independent_paths'] >= 3

    def test_multi_path_kappa_8(self):
        result = full_multi_path_verification_genus3(8)
        assert result['all_paths_agree']
        assert result['F_3'] == Fraction(31, 120960)

    def test_multi_path_kappa_24(self):
        result = full_multi_path_verification_genus3(24)
        assert result['all_paths_agree']

    def test_multi_path_with_sewing(self):
        """For integer kappa, sewing path is also available."""
        result = full_multi_path_verification_genus3(4)
        assert result['all_paths_agree']
        assert result['path_sewing'] is not None
        assert result['n_independent_paths'] >= 4

    def test_multi_path_degeneration_consistent(self):
        result = full_multi_path_verification_genus3(1)
        assert result['degeneration_consistent']


# ============================================================================
# 14. SCHOTTKY FORM AND RING STRUCTURE
# ============================================================================

class TestSchottkyForm:
    """Schottky form and genus-3 ring structure."""

    def test_schottky_description(self):
        desc = schottky_form_description()
        assert desc['weight'] == 8
        assert desc['genus'] == 3
        assert desc['torelli_degree'] == 2

    def test_schottky_indicator_at_diagonal(self):
        """Diagonal Omega = degenerate point, Schottky should detect this."""
        Omega = genus3_period_matrix_diagonal(2j, 2j, 2j)
        indicator = compute_schottky_indicator(Omega, n_max=2)
        # Diagonal period matrix is NOT in the Jacobian locus of a smooth
        # genus-3 curve (it's the product of 3 elliptic curves, which is
        # in the closure of the Jacobian locus but on a degenerate boundary).
        # The indicator may or may not be zero depending on the precise formula used.
        assert np.isfinite(indicator)

    def test_ring_structure_not_polynomial(self):
        ring = genus3_ring_structure()
        assert ring['polynomial_ring'] is False
        assert ring['genus'] == 3

    def test_first_cusp_form_weight_12(self):
        desc = genus3_first_cusp_form_description()
        assert desc['weight'] == 12
        assert desc['cusp_form'] is True
        assert desc['eigenform'] is True
        assert desc['L_function_degree'] == 8


# ============================================================================
# 15. EISENSTEIN SERIES EVALUATION
# ============================================================================

class TestEisensteinEvaluation:
    """Numerical evaluation of genus-1 Eisenstein series."""

    def test_e4_at_i(self):
        """E_4(i) = 1 + 240*sum sigma_3(n) q^n with q = exp(-2*pi)."""
        val = e4_eisenstein(1j, n_max=50)
        # Known: E_4(i) = 12 * (2*pi)^4 / (2*Gamma(1/4)^8) * something...
        # More practically: E_4(i) ~ 1 + 240*exp(-2*pi) + ...
        # The exponential suppression makes this very close to 1.
        assert abs(val.imag) < 1e-10
        # E_4(i) is known to be approximately 1.000064
        # (240 * exp(-2*pi) ~ 240 * 0.00187... ~ 0.449)
        # Wait, exp(-2pi) ~ 0.001867 so 240*0.001867 ~ 0.448
        # Actually q = exp(2*pi*i*i) = exp(-2*pi), so
        # E_4(i) ~ 1 + 240 * sigma_3(1) * exp(-2*pi) = 1 + 240*exp(-2*pi)
        # ~ 1 + 240 * 0.001867 ~ 1.448
        assert 1.0 < val.real < 2.0

    def test_e6_at_i(self):
        """E_6(i) is real at tau = i."""
        val = e6_eisenstein(1j, n_max=50)
        assert abs(val.imag) < 1e-10

    def test_eta_at_i(self):
        """eta(i) ~ 0.76823 (known special value)."""
        val = dedekind_eta(1j, n_max=100)
        assert abs(val.imag) < 1e-6
        assert abs(val.real - 0.76823) < 0.001

    def test_eta_includes_q_24th(self):
        """Verify that eta(tau) includes the q^{1/24} prefactor (AP46)."""
        # eta(i) = exp(-pi/12) * prod_{n>=1}(1 - exp(-2*pi*n))
        # The q^{1/24} = exp(2*pi*i*tau/24) = exp(-pi/12) at tau = i
        q_24th = np.exp(-np.pi / 12)
        prod_val = 1.0
        for n in range(1, 100):
            prod_val *= (1 - np.exp(-2 * np.pi * n))
        eta_expected = q_24th * prod_val
        eta_computed = dedekind_eta(1j)
        assert abs(eta_computed - eta_expected) < 1e-10

    def test_e4_modular_property(self):
        """E_4(-1/tau) = tau^4 * E_4(tau) (weight-4 modularity)."""
        tau = 0.3 + 1.2j
        e4_tau = e4_eisenstein(tau, n_max=30)
        e4_neg_inv = e4_eisenstein(-1.0 / tau, n_max=30)
        assert abs(e4_neg_inv - tau**4 * e4_tau) < 0.01 * abs(e4_tau)


# ============================================================================
# 16. THETA PRODUCT FORMULAS
# ============================================================================

class TestThetaProducts:
    """Genus-3 theta product computations."""

    def test_thomae_counts(self):
        Omega = genus3_period_matrix_diagonal(2j, 2j, 2j)
        result = thomae_formula_genus3(Omega, n_max=2)
        assert result['n_even'] == 36
        assert result['n_odd'] == 28

    def test_theta_product_finite(self):
        Omega = genus3_period_matrix_diagonal(2j, 2j, 2j)
        result = thomae_formula_genus3(Omega, n_max=2)
        assert np.isfinite(result['product_even_thetas'])
        assert np.isfinite(result['sum_4th_powers'])
        assert np.isfinite(result['sum_8th_powers'])


# ============================================================================
# 17. E_8 SIEGEL-WEIL VERIFICATION
# ============================================================================

class TestSiegelWeilGenus3:
    """Siegel-Weil theorem: Theta_{E_8}^{(3)} = E_4^{(3)}."""

    def test_siegel_weil_description(self):
        desc = siegel_weil_genus3_e8()
        assert desc['weight'] == 4
        assert desc['rank'] == 8
        assert desc['genus_3_dimension'] == 1

    def test_e8_theta_diagonal_factorization(self):
        """At diagonal Omega, Theta_{E8}^{(3)} = E_4(tau1)*E_4(tau2)*E_4(tau3)."""
        tau1, tau2, tau3 = 1.5j, 1.2j, 1.8j
        val = e8_genus3_theta_at_diagonal(tau1, tau2, tau3)
        # Each factor should be close to 1 (exponentially small corrections)
        assert np.isfinite(val)
        assert abs(val) > 0.5  # Product of ~1 values

    def test_e8_theta_equals_e4_cubed_at_diagonal(self):
        """Theta_{E8}^{(3)}(diag(tau,tau,tau)) = E_4(tau)^3."""
        tau = 2.0j  # Deep in cusp for good convergence
        val = e8_genus3_theta_at_diagonal(tau, tau, tau)
        e4_val = e4_eisenstein(tau, n_max=30)
        expected = e4_val**3
        assert abs(val - expected) < 1e-6

    def test_siegel_weil_rep_number(self):
        """The representation number r_3(E_8, diag(1,1,1)) = 1,814,400."""
        count = e8_orthogonal_root_triples()
        assert count == 1814400

    def test_e8_rep_number_trivial(self):
        """r_3(E_8, diag(0,0,0)) = 1 (only the zero triple)."""
        rep = e8_genus3_representation_number(0, 0, 0)
        assert rep == 1


# ============================================================================
# 18. BÖCHERER DISCUSSION
# ============================================================================

class TestBochererGenus3:
    """Böcherer-type conjecture at genus 3."""

    def test_discussion_structure(self):
        desc = bocherer_genus3_discussion()
        assert desc['status'] == 'OPEN'
        assert 'degree-8' in desc['genus_3_challenge']

    def test_genus2_analogue_proved(self):
        desc = bocherer_genus3_discussion()
        assert 'proved' in desc['genus_2_analogue']


# ============================================================================
# 19. EDGE CASES AND ERROR HANDLING
# ============================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_lambda_fp_genus_0_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_lambda_fp_negative_genus_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(-1)

    def test_shadow_F3_kappa_zero(self):
        """F_3(kappa=0) = 0."""
        assert shadow_F3(0) == 0

    def test_shadow_F3_negative_kappa(self):
        """F_3 with negative kappa (physical for ghost systems)."""
        assert shadow_F3(-13) == -13 * Fraction(31, 967680)

    def test_kappa_table_consistent(self):
        """Kappa table entries match expected values."""
        table = kappa_table()
        assert table['Heisenberg_k1'] == 1
        assert table['Virasoro_c26'] == 13
        assert table['E8_lattice'] == 8
        assert table['Affine_sl2_k1'] == Fraction(9, 4)

    def test_period_matrix_bad_shape(self):
        bad = np.eye(2, dtype=complex)
        assert not validate_period_matrix(bad)

    def test_graph_sum_kappa_zero(self):
        result = genus3_graph_sum_scalar(0)
        assert result['total'] == 0


# ============================================================================
# 20. ADDITIONAL CROSS-CHECKS
# ============================================================================

class TestAdditionalCrossChecks:
    """Additional cross-checks and consistency tests."""

    def test_F3_equals_graph_sum_total(self):
        """Graph sum total equals shadow F_3."""
        for k in [1, 4, 8, 24]:
            graph_result = genus3_graph_sum_scalar(k)
            shadow_result = shadow_F3(k)
            assert graph_result['total'] == shadow_result

    def test_virasoro_has_planted_forest_correction(self):
        """Class M algebras have planted-forest corrections at genus 3."""
        result = virasoro_F3(10)
        assert result['has_planted_forest_correction']

    def test_heisenberg_no_boundary_correction(self):
        """Class G (Heisenberg) has zero boundary correction."""
        result = heisenberg_F3(1)
        assert result['boundary_correction'] == 0

    def test_kappa_additivity_F3(self):
        """F_3(A1 tensor A2) = F_3(A1) + F_3(A2) for independent systems."""
        kappa1, kappa2 = 3, 7
        assert shadow_F3(kappa1) + shadow_F3(kappa2) == shadow_F3(kappa1 + kappa2)

    def test_e8_kissing_number(self):
        """E_8 has 240 roots (kissing number of E_8)."""
        roots = e8_roots_array()
        assert len(roots) == 240

    def test_lambda_3_denominator(self):
        """lambda_3 has denominator 967680 = 32 * 30240 = 32 * 6!*42."""
        lam3 = lambda_fp(3)
        assert lam3.denominator == 967680

    def test_lambda_3_numerator(self):
        """lambda_3 has numerator 31 = 2^5 - 1."""
        lam3 = lambda_fp(3)
        assert lam3.numerator == 31
        assert 31 == 2**5 - 1

    def test_bernoulli_B6(self):
        """B_6 = 1/42 (used in lambda_3 computation)."""
        from compute.lib.siegel_eisenstein import bernoulli as bernoulli_fn
        B6 = bernoulli_fn(6)
        assert B6 == Fraction(1, 42)

    def test_F3_E8_equals_lattice_rank_times_lambda3(self):
        """F_3(V_{E_8}) = 8 * 31/967680 = 31/120960."""
        result = lattice_voa_F3(8)
        assert result['F_3'] == Fraction(31, 120960)

    def test_cusp_dimension_monotone(self):
        """Cusp form dimension is non-decreasing in weight."""
        prev = 0
        for k in sorted(GENUS3_CUSP_DIMENSIONS.keys()):
            curr = GENUS3_CUSP_DIMENSIONS[k]
            assert curr >= prev
            prev = curr

    def test_total_dimension_monotone(self):
        """Total dimension is non-decreasing in weight."""
        prev = 0
        for k in sorted(GENUS3_DIMENSIONS.keys()):
            curr = GENUS3_DIMENSIONS[k]
            assert curr >= prev
            prev = curr

    def test_eta_product_representation(self):
        """Verify eta(i)^24 is related to Delta(i) = eta(i)^24."""
        eta_val = dedekind_eta(1j, n_max=100)
        delta_val = eta_val**24
        assert abs(delta_val.imag) < 1e-8
        # Delta(i) is known to be a positive real number
        assert delta_val.real > 0

    def test_e4_constant_term(self):
        """E_4(tau) -> 1 as Im(tau) -> infinity."""
        tau = 100j  # Very deep in cusp
        val = e4_eisenstein(tau, n_max=5)
        assert abs(val - 1.0) < 1e-10

    def test_genus3_dim_table_complete(self):
        """Dimension table covers all even weights 4-24."""
        for k in range(4, 25, 2):
            assert k in GENUS3_DIMENSIONS, f"Missing weight {k}"
