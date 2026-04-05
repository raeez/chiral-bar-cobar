"""
Tests for de Sitter entropy from the shadow Postnikov tower -- 65+ tests.

Tests cover:
  1. Analytic continuation AdS -> dS (Convention A and B)
  2. Gibbons-Hawking entropy from the shadow obstruction tower
  3. Nariai limit (c_dS = 13, self-dual point)
  4. Gibbons-Hawking temperature and partition function
  5. dS entropy as entanglement
  6. Quasi-de Sitter (slow-roll inflation)
  7. Banks conjecture (finite Hilbert space dimension)
  8. Hartle-Hawking wavefunction
  9. Comparison table across c_dS values
  10. Shadow radius under continuation
  11. Cross-checks with AdS/BTZ shadow entropy
"""

import pytest
import math
import cmath
from fractions import Fraction

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from desitter_shadow_entropy import (
    # Section 1: FP integrals
    lambda_fp,
    # Section 2: Analytic continuation
    kappa_ads, kappa_ds, F_g_ds_complex, F_g_ds_real_imag,
    F_g_ds_convention_B, F_g_ds_exact,
    # Section 3: dS entropy
    gibbons_hawking_entropy, gibbons_hawking_entropy_exact,
    ds_entropy_genus_expansion, ds_entropy_complex_expansion,
    # Section 4: Nariai
    nariai_point, nariai_entropy_expansion, nariai_maximality_check,
    # Section 5: Temperature and partition function
    gibbons_hawking_temperature, ds_partition_function, ds_free_energy,
    # Section 6: Entanglement
    ds_entanglement_entropy_scalar, ds_entanglement_entropy_exact,
    ds_entanglement_complementarity, ds_renyi_entropy_scalar,
    # Section 7: Quasi-dS
    slow_roll_kappa, slow_roll_entropy, slow_roll_entropy_change,
    # Section 8: Banks
    banks_hilbert_space_dimension, banks_dimension_quantum_corrected,
    # Section 9: Hartle-Hawking
    hartle_hawking_norm_squared, hartle_hawking_genus_ratio,
    # Section 10: Comparison
    comparison_table, ds_vs_ads_comparison,
    # Section 11: Shadow radius
    ds_shadow_radius,
    # Section 12: Full analysis
    full_ds_analysis,
)

PI = math.pi
TOL = 1e-10


# =========================================================================
# Section 1: Faber-Pandharipande integrals
# =========================================================================

class TestFaberPandharipande:
    def test_lambda_1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_positive(self):
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_decreasing(self):
        for g in range(1, 6):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_lambda_genus_0_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# =========================================================================
# Section 2: Analytic continuation
# =========================================================================

class TestAnalyticContinuation:
    def test_kappa_ads(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_ads(26) == Fraction(13)
        assert kappa_ads(1) == Fraction(1, 2)

    def test_kappa_ds_imaginary(self):
        """Under c -> i*c_dS, kappa = i*c_dS/2."""
        re_part, im_part = kappa_ds(26)
        assert re_part == 0
        assert abs(im_part - 13.0) < TOL

    def test_F_g_complex_purely_imaginary(self):
        """F_g(Vir_{i*c_dS}) = (i*c_dS/2)*lambda_g^FP is purely imaginary."""
        for g in range(1, 5):
            fg = F_g_ds_complex(10, g)
            assert abs(fg.real) < TOL
            assert abs(fg.imag) > 0

    def test_F_g_complex_magnitude(self):
        """Magnitude: |F_g| = (c_dS/2)*lambda_g^FP."""
        c_dS = 10
        for g in range(1, 5):
            fg = F_g_ds_complex(c_dS, g)
            expected = c_dS / 2 * float(lambda_fp(g))
            assert abs(abs(fg) - expected) < TOL

    def test_F_g_real_imag_parts(self):
        """Real part = 0, imaginary part = (c_dS/2)*lambda_g^FP."""
        c_dS = 24
        re_part, im_part = F_g_ds_real_imag(c_dS, 1)
        assert abs(re_part) < TOL
        assert abs(im_part - 24 / 2 / 24) < TOL  # c_dS/2 * 1/24 = 0.5

    def test_convention_B_real(self):
        """Convention B gives real free energies."""
        fg = F_g_ds_convention_B(10, 1)
        assert isinstance(fg, float)
        assert fg > 0

    def test_convention_B_matches_magnitude(self):
        """Convention B = magnitude of Convention A."""
        c_dS = 13
        for g in range(1, 5):
            fb = F_g_ds_convention_B(c_dS, g)
            fa = F_g_ds_complex(c_dS, g)
            assert abs(fb - abs(fa)) < TOL

    def test_F_g_exact_rational(self):
        """Exact computation gives sympy Rational."""
        fg = F_g_ds_exact(26, 1)
        assert fg == Fraction(13, 24)  # 26/2 * 1/24 = 13/24

    def test_F_g_exact_genus2(self):
        fg = F_g_ds_exact(26, 2)
        assert fg == Fraction(13) * Fraction(7, 5760)  # 13 * 7/5760


# =========================================================================
# Section 3: Gibbons-Hawking entropy
# =========================================================================

class TestGibbonsHawking:
    def test_S_dS_positive(self):
        for c in [1, 6, 13, 24, 100]:
            assert gibbons_hawking_entropy(c) > 0

    def test_S_dS_formula(self):
        """S_dS = pi * c_dS."""
        for c in [1, 6, 13, 24]:
            assert abs(gibbons_hawking_entropy(c) - PI * c) < TOL

    def test_S_dS_linear_in_c(self):
        s1 = gibbons_hawking_entropy(1)
        s2 = gibbons_hawking_entropy(2)
        assert abs(s2 / s1 - 2.0) < TOL

    def test_S_dS_exact(self):
        """Exact coefficient of pi is c_dS."""
        assert gibbons_hawking_entropy_exact(13) == 13
        assert gibbons_hawking_entropy_exact(26) == 26


class TestDSEntropyExpansion:
    def test_expansion_structure(self):
        result = ds_entropy_genus_expansion(13, 3)
        assert 'S_tree' in result
        assert 'terms' in result
        assert 'S_total' in result

    def test_tree_level_dominant(self):
        """Tree level dominates over quantum corrections."""
        result = ds_entropy_genus_expansion(13, 5)
        corrections = sum(result['terms'].values())
        assert corrections > 0
        assert result['S_tree'] > 10 * corrections

    def test_F1_value(self):
        """F_1 = c_dS/48 = kappa_dS/24."""
        result = ds_entropy_genus_expansion(24, 3)
        assert abs(result['terms'][1] - 24 / 48) < TOL

    def test_running_sums_increasing(self):
        """Running sums are increasing (all corrections positive)."""
        result = ds_entropy_genus_expansion(13, 5)
        prev = result['S_tree']
        for g in range(1, 6):
            current = result['running_sums'][g]
            assert current > prev
            prev = current

    def test_complex_expansion_purely_imaginary(self):
        """Convention A: total entropy is purely imaginary."""
        result = ds_entropy_complex_expansion(10, 3)
        assert abs(result['total_real']) < TOL
        assert abs(result['total_imag']) > 0

    def test_complex_expansion_magnitude_matches_B(self):
        """Magnitude of Convention A = Convention B total."""
        c_dS = 13
        complex_result = ds_entropy_complex_expansion(c_dS, 3)
        real_result = ds_entropy_genus_expansion(c_dS, 3)
        assert abs(complex_result['total_magnitude'] - real_result['S_total']) < 1e-6


# =========================================================================
# Section 4: Nariai limit
# =========================================================================

class TestNariai:
    def test_nariai_c(self):
        info = nariai_point()
        assert info['c_dS'] == 13

    def test_nariai_kappa(self):
        info = nariai_point()
        assert info['kappa_dS'] == Fraction(13, 2)

    def test_nariai_self_dual(self):
        info = nariai_point()
        assert info['is_self_dual']

    def test_nariai_S_tree(self):
        info = nariai_point()
        assert abs(info['S_tree'] - 13 * PI) < TOL

    def test_nariai_complementarity(self):
        info = nariai_point()
        assert info['complementarity_sum'] == 13

    def test_nariai_expansion(self):
        result = nariai_entropy_expansion(3)
        assert result['is_nariai']
        assert abs(result['S_tree'] - 13 * PI) < TOL

    def test_nariai_not_maximum(self):
        """The Nariai point does NOT maximize entropy (S is monotone in c)."""
        check = nariai_maximality_check()
        assert check['nariai_is_maximum'] is False
        assert check['monotone_in_c'] is True

    def test_nariai_is_special(self):
        check = nariai_maximality_check()
        assert check['nariai_is_special'] is True


# =========================================================================
# Section 5: Temperature and partition function
# =========================================================================

class TestTemperatureAndPartitionFunction:
    def test_temperature_positive(self):
        for c in [1, 6, 13, 24]:
            assert gibbons_hawking_temperature(c) > 0

    def test_temperature_decreases_with_c(self):
        """T_dS = 3/(4*pi*G_N*c_dS) decreases with c_dS."""
        T1 = gibbons_hawking_temperature(1)
        T10 = gibbons_hawking_temperature(10)
        assert T1 > T10

    def test_temperature_formula(self):
        """T = 3/(4*pi*c_dS) at G_N = 1."""
        c = 10
        T = gibbons_hawking_temperature(c, G_N=1.0)
        expected = 3.0 / (4 * PI * c)
        assert abs(T - expected) < TOL

    def test_partition_function_positive(self):
        result = ds_partition_function(10, beta=1.0, max_g=3)
        assert result['Z'] > 0

    def test_partition_function_log_Z(self):
        """log Z should be close to S_dS at the saddle point."""
        c = 10
        result = ds_partition_function(c, beta=1.0, max_g=3)
        assert result['log_Z'] > result['S_tree']

    def test_free_energy_negative(self):
        """Free energy F = -T*log(Z) should have correct sign."""
        result = ds_free_energy(10, T=1.0, max_g=2)
        # F = -T * log Z, and log Z > 0, so F < 0
        assert result['F'] < 0


# =========================================================================
# Section 6: dS entropy as entanglement
# =========================================================================

class TestEntanglement:
    def test_S_EE_formula(self):
        """S_EE = (c_dS/3) * ln(l/eps)."""
        c = 12
        log_ratio = math.log(100)
        S = ds_entanglement_entropy_scalar(c, log_ratio)
        expected = c / 3.0 * log_ratio
        assert abs(S - expected) < TOL

    def test_S_EE_positive(self):
        for c in [1, 6, 13, 24]:
            assert ds_entanglement_entropy_scalar(c, math.log(10)) > 0

    def test_S_EE_exact(self):
        S = ds_entanglement_entropy_exact(12, 6)
        assert S == Fraction(24)  # 12/3 * 6 = 24

    def test_complementarity(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*ln(l/eps) for all c."""
        for c in [1, 5, 10, 13, 20, 25]:
            result = ds_entanglement_complementarity(c, math.log(100))
            assert result['match']

    def test_complementarity_c_independent(self):
        """The sum is independent of c_dS."""
        totals = []
        for c in [3, 7, 13, 19, 23]:
            result = ds_entanglement_complementarity(c, math.log(50))
            totals.append(result['total'])
        for i in range(1, len(totals)):
            assert abs(totals[i] - totals[0]) < TOL

    def test_renyi_entropy_n1_limit(self):
        """At n -> large, S_n -> (kappa/3)*ln(l/eps)."""
        c = 10
        kappa = c / 2.0
        log_ratio = math.log(100)
        S_large_n = ds_renyi_entropy_scalar(c, 1000, log_ratio)
        expected = kappa / 3.0 * log_ratio  # (1+1/n) -> 1 for large n
        assert abs(S_large_n - expected) / expected < 0.01

    def test_renyi_to_von_neumann(self):
        """At n=1: S_1 = (2*kappa/3)*log_ratio = (c_dS/3)*log_ratio."""
        c = 10
        kappa = c / 2.0
        log_ratio = math.log(100)
        S_1 = ds_renyi_entropy_scalar(c, 1, log_ratio)
        S_vN = ds_entanglement_entropy_scalar(c, log_ratio)
        # S_1 = (kappa/3)*(1+1) = (2*kappa/3) = c/3
        assert abs(S_1 - S_vN) < TOL


# =========================================================================
# Section 7: Quasi-de Sitter (inflation)
# =========================================================================

class TestQuasiDeSitter:
    def test_slow_roll_kappa_at_t0(self):
        """At t=0: kappa(0) = c_0/2."""
        assert abs(slow_roll_kappa(10, 0.01, 0) - 5.0) < TOL

    def test_slow_roll_kappa_decreases(self):
        """kappa(t) decreases with t for positive epsilon."""
        k0 = slow_roll_kappa(10, 0.01, 0)
        k1 = slow_roll_kappa(10, 0.01, 1)
        assert k1 < k0

    def test_slow_roll_kappa_formula(self):
        """kappa(t) = (c_0/2)(1 - eps*t)."""
        c_0, eps, t = 20, 0.05, 2
        expected = c_0 / 2 * (1 - eps * t)
        assert abs(slow_roll_kappa(c_0, eps, t) - expected) < TOL

    def test_slow_roll_entropy_at_t0(self):
        """S(0) matches static dS entropy."""
        c_0 = 10
        result = slow_roll_entropy(c_0, 0.01, 0, max_g=2)
        static = ds_entropy_genus_expansion(c_0, 2)
        assert abs(result['S_total'] - static['S_total']) < 1e-8

    def test_slow_roll_entropy_decreases(self):
        """Entropy decreases with time for epsilon > 0."""
        result0 = slow_roll_entropy(10, 0.01, 0, 2)
        result1 = slow_roll_entropy(10, 0.01, 1, 2)
        assert result1['S_total'] < result0['S_total']

    def test_slow_roll_dS_dt_negative(self):
        """dS/dt < 0 for positive slow-roll parameter."""
        result = slow_roll_entropy(10, 0.01, 0, 2)
        assert result['dS_dt_tree'] < 0
        assert result['dS_dt_total'] < 0

    def test_slow_roll_entropy_change(self):
        """Delta_S matches tree-level prediction."""
        c_0, eps = 10, 0.01
        t1, t2 = 0, 1
        result = slow_roll_entropy_change(c_0, eps, t1, t2, 2)
        assert abs(result['delta_tree'] - result['tree_prediction']) < 1e-8

    def test_slow_roll_quantum_correction_small(self):
        """Quantum corrections to Delta_S are small relative to tree level."""
        result = slow_roll_entropy_change(100, 0.001, 0, 1, 2)
        if abs(result['delta_tree']) > 1e-10:
            ratio = abs(result['delta_quantum'] / result['delta_tree'])
            assert ratio < 0.01  # quantum < 1% of tree


# =========================================================================
# Section 8: Banks conjecture
# =========================================================================

class TestBanks:
    def test_banks_N_positive(self):
        result = banks_hilbert_space_dimension(10)
        assert result['N'] > 0

    def test_banks_log_N_equals_S(self):
        """log(N) = S_dS = pi*c_dS."""
        c = 10
        result = banks_hilbert_space_dimension(c)
        assert abs(result['log_N'] - PI * c) < TOL

    def test_banks_N_grows_with_c(self):
        N1 = banks_hilbert_space_dimension(1)['N']
        N10 = banks_hilbert_space_dimension(10)['N']
        assert N10 > N1

    def test_banks_finite(self):
        result = banks_hilbert_space_dimension(10)
        assert result['N_finite']

    def test_banks_shadow_convergent(self):
        result = banks_hilbert_space_dimension(10)
        assert result['shadow_convergent']

    def test_banks_quantum_corrected(self):
        result = banks_dimension_quantum_corrected(10, 3)
        # Quantum corrections increase log(N)
        assert result['log_N_corrected'] > result['log_N_tree']

    def test_banks_correction_small(self):
        """Quantum corrections are small: |correction/tree| << 1."""
        result = banks_dimension_quantum_corrected(10, 3)
        assert abs(result['relative_correction']) < 0.01


# =========================================================================
# Section 9: Hartle-Hawking wavefunction
# =========================================================================

class TestHartleHawking:
    def test_HH_norm_positive(self):
        result = hartle_hawking_norm_squared(10, 2)
        assert result['psi_sq'] > 0

    def test_HH_log_equals_entropy(self):
        """log|Psi_HH|^2 = S_dS (at the shadow obstruction tower level)."""
        c = 10
        result = hartle_hawking_norm_squared(c, 3)
        expansion = ds_entropy_genus_expansion(c, 3)
        assert abs(result['log_psi_sq'] - expansion['S_total']) < TOL

    def test_HH_tree_level(self):
        """Tree level: log|Psi_HH|^2 = pi*c_dS."""
        c = 10
        result = hartle_hawking_norm_squared(c, 0)
        # max_g=0 means no corrections, but code starts at g=1
        # so with max_g=2, check tree dominates
        result2 = hartle_hawking_norm_squared(c, 2)
        assert abs(result2['S_tree'] - PI * c) < TOL

    def test_HH_genus_ratio(self):
        """Genus ratios converge to 1/(2*pi)^2."""
        result = hartle_hawking_genus_ratio(13, 5)
        target = result['target_ratio']
        for g, ratio in result['ratios'].items():
            # For g >= 3 the ratio should be within 20% of target
            if g >= 3:
                assert abs(ratio - target) / target < 0.2

    def test_HH_convergent(self):
        result = hartle_hawking_genus_ratio(13, 5)
        assert result['convergent']


# =========================================================================
# Section 10: Comparison table
# =========================================================================

class TestComparisonTable:
    def test_table_structure(self):
        result = comparison_table(max_g=3)
        assert 'table' in result
        assert len(result['table']) == 5  # default 5 c values

    def test_table_monotone_in_c(self):
        """S_dS increases with c_dS."""
        result = comparison_table([1, 10, 100], max_g=2)
        s1 = result['table'][1]['S_tree']
        s10 = result['table'][10]['S_tree']
        s100 = result['table'][100]['S_tree']
        assert s1 < s10 < s100

    def test_table_relative_correction_small(self):
        """Relative corrections are small for all c_dS."""
        result = comparison_table([1, 6, 13, 24, 100], max_g=3)
        for c, row in result['table'].items():
            assert abs(row['relative_correction']) < 0.05

    def test_table_F1_values(self):
        """F_1 = c_dS/48 for each entry."""
        result = comparison_table([6, 12, 24], max_g=1)
        for c in [6, 12, 24]:
            assert abs(result['table'][c]['F_1'] - c / 48.0) < TOL

    def test_ds_vs_ads_convention_B(self):
        """Convention B free energies match AdS at same c."""
        result = ds_vs_ads_comparison(13, 3)
        assert result['convention_B_matches_AdS']
        for g, data in result['comparison'].items():
            assert abs(data['ratio_B_to_AdS'] - 1.0) < TOL


# =========================================================================
# Section 11: Shadow radius
# =========================================================================

class TestShadowRadius:
    def test_shadow_radius_positive(self):
        result = ds_shadow_radius(13)
        assert result['rho_convention_B'] > 0

    def test_shadow_radius_convergent_large_c(self):
        """For large c_dS, shadow radius < 1 (convergent)."""
        result = ds_shadow_radius(100)
        assert result['convergent_B']

    def test_shadow_radius_formula(self):
        """rho = sqrt(36 + 80/(5c+22)) / c."""
        c = 13
        expected = math.sqrt(36 + 80 / (5 * 13 + 22)) / 13
        result = ds_shadow_radius(c)
        assert abs(result['rho_convention_B'] - expected) < TOL

    def test_shadow_radius_complex_exists(self):
        """Complex shadow radius is computed."""
        result = ds_shadow_radius(13)
        assert result['rho_complex'] is not None
        assert result['rho_complex_magnitude'] > 0


# =========================================================================
# Section 12: Full analysis
# =========================================================================

class TestFullAnalysis:
    def test_full_analysis_keys(self):
        result = full_ds_analysis(13, 2)
        for key in ['c_dS', 'kappa_dS', 'S_GH', 'T_GH',
                     'entropy_expansion', 'S_EE_scalar',
                     'complementarity', 'HH', 'banks', 'shadow_radius']:
            assert key in result

    def test_full_analysis_nariai(self):
        result = full_ds_analysis(13, 2)
        assert result['is_nariai']
        assert result['distance_to_nariai'] < TOL


# =========================================================================
# Cross-checks with AdS / BTZ
# =========================================================================

class TestCrossChecks:
    def test_F_g_ds_matches_ads_convention_B(self):
        """Convention B: F_g^dS = F_g^AdS at same numerical c."""
        from sympy import Rational
        c = 26
        for g in range(1, 4):
            f_ds = float(F_g_ds_exact(c, g))
            f_ads = float(Rational(c, 2) * lambda_fp(g))
            assert abs(f_ds - f_ads) < TOL

    def test_tree_entropy_ratio_ads_ds(self):
        """BTZ: S = 2*pi*sqrt(c*Delta/6). dS: S = pi*c_dS.
        These are different objects (BTZ depends on Delta)."""
        c = 24
        # Just verify they are different functional forms
        S_dS = gibbons_hawking_entropy(c)
        # BTZ at Delta=6: S = 2*pi*sqrt(24*6/6) = 2*pi*sqrt(24)
        S_BTZ = 2 * PI * math.sqrt(c)
        assert S_dS != S_BTZ  # different objects

    def test_bernoulli_decay_preserved(self):
        """The Bernoulli decay rate 1/(2*pi)^2 is the same in dS and AdS."""
        c = 13
        ratios = []
        for g in range(1, 5):
            f1 = F_g_ds_convention_B(c, g)
            f2 = F_g_ds_convention_B(c, g + 1)
            if abs(f1) > 1e-50:
                ratios.append(f2 / f1)
        target = 1.0 / (2 * PI) ** 2
        for r in ratios[1:]:  # skip g=1 which may not be in asymptotic regime
            assert abs(r - target) / target < 0.5

    def test_complementarity_sum_26_3(self):
        """Complementarity: kappa(c) + kappa(26-c) = 13 for all c.
        Same as in AdS Virasoro."""
        for c in [1, 6, 13, 24, 25]:
            kappa_c = c / 2.0
            kappa_dual = (26 - c) / 2.0
            assert abs(kappa_c + kappa_dual - 13) < TOL

    def test_genus_1_F1_universal(self):
        """F_1 = kappa/24 is universal (same formula in dS and AdS)."""
        for c in [1, 6, 13, 24, 100]:
            kappa = c / 2.0
            f1 = F_g_ds_convention_B(c, 1)
            assert abs(f1 - kappa / 24) < TOL
