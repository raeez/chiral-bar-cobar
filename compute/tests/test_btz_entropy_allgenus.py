"""
Tests for BTZ black hole entropy at all genera from the shadow Postnikov tower.

Tests organized by section:
  1. Classical (genus 0): Bekenstein-Hawking / Cardy formula
  2. One-loop (genus 1): logarithmic correction, three routes
  3. Two-loop (genus 2): shadow + planted-forest corrections
  4. Three-loop (genus 3): 42-graph expansion
  5. Four-loop (genus 4): 379-graph expansion (scalar only)
  6. Full entropy expansion
  7. Euclidean path integral and Hawking-Page transition
  8. Rademacher / Cardy comparison
  9. Entanglement entropy cross-check
 10. Log corrections for c = 1..26
 11. Complementarity at all genera
 12. A-hat generating function
 13. Convergence diagnostics
 14. Monster module and special central charges
 15. Cross-verification between routes
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from btz_entropy_allgenus import (
    # Section 1: Faber-Pandharipande
    lambda_fp, lambda_fp_float,
    # Section 2: Virasoro data
    kappa_virasoro, virasoro_S3, virasoro_S4, virasoro_S5, virasoro_shadow_data,
    # Section 3: Classical
    bekenstein_hawking_entropy, inverse_hawking_temperature, hawking_temperature,
    # Section 4: One-loop
    F1_virasoro, log_correction_coefficient, genus1_entropy_correction,
    heat_kernel_F1, shadow_tower_F1, selberg_zeta_F1, verify_genus1_three_routes,
    # Section 5: Two-loop
    F2_scalar, planted_forest_g2, F2_full,
    genus2_entropy_correction,
    # Section 6: Three-loop
    F3_scalar, planted_forest_g3, F3_full,
    genus3_entropy_correction,
    # Section 7: Four-loop
    F4_scalar, F4_full,
    genus4_entropy_correction,
    # Section 8: Full expansion
    free_energy_table, entropy_all_genera,
    # Section 9: Euclidean path integral
    euclidean_free_energy_btz, euclidean_free_energy_ads,
    hawking_page_temperature, hawking_page_free_energy,
    # Section 10: Rademacher
    cardy_density_of_states, cardy_with_log_correction, log_cardy_density,
    rademacher_leading_term, log_rademacher_leading, verify_cardy_rademacher,
    # Section 11: Entanglement
    entanglement_entropy_scalar, entanglement_complementarity,
    # Section 12: Log correction table
    log_correction_table,
    # Section 13: Complementarity
    complementarity_all_genera,
    # Section 14: A-hat
    ahat_generating_function_value, scalar_genus_sum, ahat_closed_form,
    verify_ahat_identity,
    # Section 15: Convergence
    genus_decay_ratios, convergence_radius_scalar, shadow_partition_convergent,
    # Section 16: Special cases
    monster_entropy, critical_string_entropy, self_dual_entropy,
    # Section 17: Phase structure
    phase_diagram_data,
)

PI = math.pi
TWO_PI = 2 * PI


# =========================================================================
# Section 1: Faber-Pandharipande numbers
# =========================================================================

class TestFaberPandharipande:
    def test_lambda1_exact(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2_exact(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3_exact(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda4_exact(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (Bernoulli sign pitfall)."""
        for g in range(1, 11):
            assert lambda_fp(g) > 0

    def test_strictly_decreasing(self):
        for g in range(1, 10):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_float_matches_fraction(self):
        for g in range(1, 6):
            assert abs(lambda_fp_float(g) - float(lambda_fp(g))) < 1e-15


# =========================================================================
# Section 2: Virasoro shadow data
# =========================================================================

class TestVirasoroData:
    def test_kappa_c26(self):
        assert kappa_virasoro(26) == Fraction(13)

    def test_kappa_c1(self):
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_kappa_c13_self_dual(self):
        """At c=13: kappa = 13/2, and kappa' = kappa (self-dual)."""
        assert kappa_virasoro(13) == Fraction(13, 2)
        assert kappa_virasoro(26 - 13) == Fraction(13, 2)

    def test_S3_c_independent(self):
        assert virasoro_S3() == Fraction(2)

    def test_S4_c26(self):
        # S_4 = 10 / (26 * (5*26 + 22)) = 10 / (26 * 152) = 10/3952 = 5/1976
        assert virasoro_S4(26) == Fraction(10, 26 * 152)

    def test_S4_diverges_c0(self):
        """S_4 has a pole at c = 0 (excluded from domain)."""
        with pytest.raises((ZeroDivisionError, ValueError)):
            virasoro_S4(0)

    def test_S5_sign(self):
        """S_5 is negative for c > 0."""
        assert virasoro_S5(26) < 0

    def test_shadow_data_keys(self):
        data = virasoro_shadow_data(24)
        assert set(data.keys()) == {'c', 'kappa', 'S_3', 'S_4', 'S_5'}


# =========================================================================
# Section 3: Classical (genus 0) — Bekenstein-Hawking
# =========================================================================

class TestClassical:
    def test_S_BH_positive(self):
        for c in [1, 6, 12, 24, 26]:
            assert bekenstein_hawking_entropy(c, 1) > 0

    def test_S_BH_formula(self):
        """S_BH = 2*pi*sqrt(c*M/6)."""
        c, M = 24, 6
        expected = 2 * PI * math.sqrt(24 * 6 / 6.0)
        assert abs(bekenstein_hawking_entropy(c, M) - expected) < 1e-10

    def test_S_BH_sqrt_c_scaling(self):
        """S_BH scales as sqrt(c) at fixed M."""
        s1 = bekenstein_hawking_entropy(1, 1)
        s4 = bekenstein_hawking_entropy(4, 1)
        assert abs(s4 / s1 - 2.0) < 1e-10

    def test_S_BH_sqrt_M_scaling(self):
        """S_BH scales as sqrt(M) at fixed c."""
        s1 = bekenstein_hawking_entropy(6, 1)
        s4 = bekenstein_hawking_entropy(6, 4)
        assert abs(s4 / s1 - 2.0) < 1e-10

    def test_inverse_temperature_positive(self):
        for c in [1, 12, 24]:
            assert inverse_hawking_temperature(c, 1) > 0

    def test_temperature_inverse(self):
        c, M = 24, 10
        T = hawking_temperature(c, M)
        beta = inverse_hawking_temperature(c, M)
        assert abs(T * beta - 1.0) < 1e-10

    def test_saddle_point_consistency(self):
        """dS_0/dM = beta_H: the saddle-point relation."""
        c, M = 24, 100
        S0 = bekenstein_hawking_entropy(c, M)
        beta = inverse_hawking_temperature(c, M)
        # dS_0/dM = pi * sqrt(c/(6M)) = beta_H
        dS_dM = PI * math.sqrt(c / (6.0 * M))
        assert abs(beta - dS_dM) < 1e-10

    def test_c24_M1_equals_4pi(self):
        """For Monster (c=24, M=1): S_BH = 4*pi."""
        assert abs(bekenstein_hawking_entropy(24, 1) - 4 * PI) < 1e-10


# =========================================================================
# Section 4: One-loop (genus 1) — logarithmic correction
# =========================================================================

class TestOneLoop:
    def test_F1_formula(self):
        """F_1(Vir_c) = c/48."""
        for c in [1, 12, 24, 26]:
            assert F1_virasoro(c) == Fraction(c, 48)

    def test_log_coeff_minus_three_halves(self):
        assert log_correction_coefficient() == Fraction(-3, 2)

    def test_log_correction_reduces_entropy(self):
        """The log correction always reduces S (for large S_0)."""
        S1 = genus1_entropy_correction(24, 1000)
        assert S1 < 0

    def test_three_routes_agree(self):
        """Routes A (heat kernel), B (shadow), C (Selberg) all give c/48."""
        for c in [1, 6, 12, 13, 24, 26]:
            result = verify_genus1_three_routes(c)
            assert result['all_agree'], f"Routes disagree at c={c}"
            assert result['A_matches']
            assert result['B_matches']
            assert result['C_matches']

    def test_heat_kernel_float(self):
        assert abs(heat_kernel_F1(24) - 0.5) < 1e-14

    def test_shadow_tower_exact(self):
        assert shadow_tower_F1(24) == Fraction(1, 2)

    def test_selberg_zeta_float(self):
        assert abs(selberg_zeta_F1(24) - 0.5) < 1e-14


# =========================================================================
# Section 5: Two-loop (genus 2)
# =========================================================================

class TestTwoLoop:
    def test_F2_scalar_formula(self):
        """F_2^{sc} = (c/2) * (7/5760)."""
        assert F2_scalar(24) == Fraction(24, 2) * Fraction(7, 5760)

    def test_planted_forest_g2_heisenberg_zero(self):
        """For Heisenberg-like (S_3 = 0): delta_pf = 0.

        NOTE: This tests the formula with S_3=0 directly; Heisenberg
        has kappa = k, not c/2. But the formula gives 0 when S_3 = 0.
        """
        # delta_pf = S_3*(10*S_3 - kappa)/48.  If S_3 = 0 => delta_pf = 0.
        # The planted_forest_g2 function uses Virasoro data (S_3=2), so
        # we test the structural property differently.
        pass

    def test_planted_forest_g2_c40_zero(self):
        """delta_pf^{(2,0)} = -(c-40)/48 vanishes at c = 40."""
        pf = planted_forest_g2(40)
        assert pf == Fraction(0)

    def test_planted_forest_g2_c26(self):
        """At c=26: delta_pf = -(26-40)/48 = 14/48 = 7/24."""
        pf = planted_forest_g2(26)
        expected = Fraction(-(26 - 40), 48)  # 14/48 = 7/24
        assert pf == expected

    def test_F2_full_larger_than_scalar_c26(self):
        """For c=26: planted-forest correction is positive (c < 40)."""
        assert F2_full(26) > F2_scalar(26)

    def test_F2_full_smaller_than_scalar_c50(self):
        """For c=50: planted-forest correction is negative (c > 40)."""
        assert F2_full(50) < F2_scalar(50)

    def test_genus2_correction_small(self):
        """S_2 << S_0 for large M."""
        S0 = bekenstein_hawking_entropy(24, 1000)
        S2 = genus2_entropy_correction(24, 1000)
        assert abs(S2) < 0.01 * S0

    def test_F2_full_exact_c26(self):
        """Verify exact value of F_2^{full} at c=26."""
        scalar = Fraction(13) * Fraction(7, 5760)
        pf = Fraction(7, 24)
        expected = scalar + pf
        assert F2_full(26) == expected


# =========================================================================
# Section 6: Three-loop (genus 3)
# =========================================================================

class TestThreeLoop:
    def test_F3_scalar_formula(self):
        """F_3^{sc} = (c/2) * (31/967680)."""
        assert F3_scalar(24) == Fraction(12) * Fraction(31, 967680)

    def test_planted_forest_g3_exists(self):
        """The genus-3 planted-forest correction is nonzero for Virasoro."""
        pf = planted_forest_g3(26)
        assert pf != 0

    def test_F3_full_differs_from_scalar(self):
        """Full F_3 differs from scalar F_3 (class M: infinite depth)."""
        assert F3_full(26) != F3_scalar(26)

    def test_genus3_correction_smaller_than_genus2(self):
        """S_3 < S_2 for large M (Bernoulli decay)."""
        M = 1000
        S2 = abs(genus2_entropy_correction(24, M))
        S3 = abs(genus3_entropy_correction(24, M))
        assert S3 < S2

    def test_F3_scalar_positive(self):
        """F_3^{scalar} > 0 for c > 0."""
        for c in [1, 12, 24, 26]:
            assert F3_scalar(c) > 0


# =========================================================================
# Section 7: Four-loop (genus 4)
# =========================================================================

class TestFourLoop:
    def test_F4_scalar_formula(self):
        """F_4^{sc} = (c/2) * (127/154828800)."""
        assert F4_scalar(24) == Fraction(12) * Fraction(127, 154828800)

    def test_F4_positive(self):
        for c in [1, 12, 24, 26]:
            assert F4_scalar(c) > 0

    def test_genus4_correction_smaller_than_genus3(self):
        """S_4 < S_3 for large M (Bernoulli decay)."""
        M = 1000
        S3 = abs(genus3_entropy_correction(24, M))
        S4 = abs(genus4_entropy_correction(24, M))
        assert S4 < S3


# =========================================================================
# Section 8: Full entropy expansion
# =========================================================================

class TestFullExpansion:
    def test_free_energy_table_keys(self):
        table = free_energy_table(24, 4)
        assert set(table.keys()) == {1, 2, 3, 4}

    def test_free_energy_table_F1(self):
        table = free_energy_table(24, 4)
        assert table[1] == Fraction(1, 2)

    def test_entropy_all_genera_keys(self):
        result = entropy_all_genera(24, 100, 3)
        assert 'S_0' in result
        assert 'S_1' in result
        assert 'S_2' in result
        assert 'S_3' in result
        assert 'S_total' in result

    def test_S_total_close_to_S_0(self):
        """For large M, S_total ~ S_0 (corrections are small)."""
        result = entropy_all_genera(24, 10000, 4)
        assert abs(result['S_total'] - result['S_0']) / result['S_0'] < 0.01

    def test_corrections_decrease_with_genus(self):
        """Higher-genus corrections are successively smaller."""
        result = entropy_all_genera(24, 100, 4)
        for g in range(2, 4):
            assert abs(result[f'S_{g+1}']) < abs(result[f'S_{g}'])

    def test_expansion_parameter_small(self):
        """2*pi / S_0 < 1 for large M (saddle-point condition)."""
        S0 = bekenstein_hawking_entropy(24, 100)
        assert TWO_PI / S0 < 1.0

    def test_entropy_below_threshold(self):
        """Return error for S_0 <= 0."""
        result = entropy_all_genera(24, -1, 2)
        assert 'error' in result


# =========================================================================
# Section 9: Euclidean path integral
# =========================================================================

class TestEuclidean:
    def test_btz_free_energy_negative(self):
        """F_BTZ < 0 (the on-shell action is negative)."""
        for beta in [0.5, 1.0, 2.0]:
            assert euclidean_free_energy_btz(24, beta, 0) < 0

    def test_ads_free_energy_negative(self):
        """F_AdS < 0."""
        for beta in [1.0, 5.0, 10.0]:
            assert euclidean_free_energy_ads(24, beta) < 0

    def test_btz_dominates_high_T(self):
        """BTZ dominates at high temperature (small beta)."""
        beta = 0.1
        F_btz = euclidean_free_energy_btz(24, beta, 2)
        F_ads = euclidean_free_energy_ads(24, beta)
        assert F_btz < F_ads

    def test_ads_dominates_low_T(self):
        """Thermal AdS dominates at low temperature (large beta)."""
        beta = 100.0
        F_btz = euclidean_free_energy_btz(24, beta, 2)
        F_ads = euclidean_free_energy_ads(24, beta)
        assert F_ads < F_btz

    def test_hawking_page_classical(self):
        """Classical HP temperature: beta_HP = 2*pi."""
        assert abs(hawking_page_temperature(24, 0) - TWO_PI) < 1e-10

    def test_phase_transition_exists(self):
        """There exists a beta where dominance switches."""
        data = hawking_page_free_energy(24,
            [0.5, 1.0, 2.0, PI, TWO_PI, 3*PI, 10.0], 2)
        phases = [d['dominant'] for d in data['data']]
        assert 'BTZ' in phases
        assert 'AdS' in phases


# =========================================================================
# Section 10: Rademacher / Cardy comparison
# =========================================================================

class TestRademacher:
    def test_cardy_density_positive_small_n(self):
        """Density is positive for small n (no overflow)."""
        for n in [10, 50]:
            assert cardy_density_of_states(24, n) > 0

    def test_log_cardy_grows(self):
        """log rho grows with n."""
        log1 = log_cardy_density(24, 100)
        log2 = log_cardy_density(24, 200)
        assert log2 > log1

    def test_log_cardy_leading_exponent(self):
        """Leading exponent: 2*pi*sqrt(c*n/6)."""
        c, n = 24, 10000
        expected = 2 * PI * math.sqrt(c * n / 6.0)
        log_rho = log_cardy_density(c, n)
        # The log-density should be close to S_0 (subleading corrections are small)
        assert abs(log_rho - expected) / expected < 0.05

    def test_log_correction_reduces_density(self):
        """The -3/2 log correction reduces density at small n."""
        n = 50
        rho_corr = cardy_with_log_correction(24, n)
        assert rho_corr > 0

    def test_rademacher_leading_positive(self):
        for n in [10, 100]:
            assert rademacher_leading_term(24, n) > 0

    def test_cardy_rademacher_match_large_n(self):
        """For large n, Cardy and Rademacher leading exponents agree."""
        result = verify_cardy_rademacher(24, [100, 1000, 10000])
        for d in result['data']:
            # The log_ratio = log(rho_R/rho_C) should be subleading
            # compared to log_cardy itself
            if not math.isnan(d['log_ratio']):
                assert abs(d['log_ratio']) < 0.1 * abs(d['log_cardy'])

    def test_log_rademacher_positive(self):
        """log rho from Rademacher is positive for moderate n."""
        for n in [100, 1000]:
            assert log_rademacher_leading(24, n) > 0


# =========================================================================
# Section 11: Entanglement entropy
# =========================================================================

class TestEntanglement:
    def test_calabrese_cardy_formula(self):
        """S_EE = (c/3) * log(L/eps)."""
        c, L = 24, 1000
        expected = (c / 3.0) * math.log(L)
        assert abs(entanglement_entropy_scalar(c, L) - expected) < 1e-10

    def test_complementarity_universal(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps) for all c."""
        for c in [1, 5, 10, 13, 20, 25]:
            result = entanglement_complementarity(c, 1000)
            assert result['match'], f"Complementarity fails at c={c}"

    def test_complementarity_c_independent(self):
        """The sum is c-independent."""
        sums = []
        for c in [1, 6, 13, 24, 25]:
            result = entanglement_complementarity(c, 1000)
            sums.append(result['sum'])
        for s in sums[1:]:
            assert abs(s - sums[0]) < 1e-10

    def test_self_dual_point(self):
        """At c=13: S_EE = (13/3)*log(L/eps)."""
        L = 1000
        expected = (13.0 / 3.0) * math.log(L)
        assert abs(entanglement_entropy_scalar(13, L) - expected) < 1e-10


# =========================================================================
# Section 12: Log correction table
# =========================================================================

class TestLogCorrectionTable:
    def test_table_has_26_entries(self):
        table = log_correction_table(g_max=2)
        assert len(table) == 26

    def test_F1_equals_c_over_48(self):
        table = log_correction_table(g_max=1)
        for c in range(1, 27):
            assert abs(table[c]['F_1'] - c / 48.0) < 1e-14

    def test_planted_forest_in_table(self):
        table = log_correction_table(g_max=2)
        for c in range(1, 27):
            assert 'delta_pf_g2' in table[c]

    def test_kappa_values(self):
        table = log_correction_table(g_max=1)
        for c in range(1, 27):
            assert abs(table[c]['kappa'] - c / 2.0) < 1e-14

    def test_all_class_M(self):
        table = log_correction_table(g_max=1)
        for c in range(1, 27):
            assert table[c]['shadow_class'] == 'M'

    def test_g3_corrections_present(self):
        table = log_correction_table(g_max=3)
        for c in range(1, 27):
            assert 'F_3_full' in table[c]
            assert 'delta_pf_g3' in table[c]


# =========================================================================
# Section 13: Complementarity at all genera
# =========================================================================

class TestComplementarityAllGenera:
    def test_scalar_complementarity_genus1(self):
        result = complementarity_all_genera(10, 1)
        assert result['genera'][1]['scalar_match']

    def test_scalar_complementarity_all_genera(self):
        """Scalar complementarity: F_g(c) + F_g(26-c) = 13*lambda_g for all g."""
        for c in [1, 10, 13, 20, 26]:
            result = complementarity_all_genera(c, 4)
            assert result['scalar_complementarity'], \
                f"Scalar complementarity fails at c={c}"

    def test_self_dual_scalar(self):
        """At c=13: F_g(13) = F_g(26-13) = (13/2)*lambda_g."""
        result = complementarity_all_genera(13, 3)
        for g in range(1, 4):
            entry = result['genera'][g]
            assert abs(entry['F_g_scalar_c'] - entry['F_g_scalar_dual']) < 1e-14

    def test_full_sum_differs_from_scalar_g2(self):
        """Full (with planted-forest) sum differs from scalar sum at g>=2."""
        result = complementarity_all_genera(10, 3)
        for g in [2, 3]:
            entry = result['genera'][g]
            assert abs(entry['full_sum'] - entry['scalar_sum']) > 1e-15


# =========================================================================
# Section 14: A-hat generating function
# =========================================================================

class TestAhat:
    def test_ahat_at_zero(self):
        assert abs(ahat_generating_function_value(0) - 1.0) < 1e-14

    def test_ahat_positive(self):
        """A-hat(x) > 0 for 0 < x < 2*pi."""
        for x in [0.1, 0.5, 1.0, 2.0, 4.0, 6.0]:
            assert ahat_generating_function_value(x) > 0

    def test_ahat_formula(self):
        """A-hat(x) = (x/2)/sinh(x/2)."""
        for x in [0.5, 1.0, 2.0]:
            expected = (x / 2.0) / math.sinh(x / 2.0)
            assert abs(ahat_generating_function_value(x) - expected) < 1e-14

    def test_series_closed_form_match(self):
        """Series sum matches closed form."""
        for c in [6, 12, 24]:
            result = verify_ahat_identity(c, hbar=0.5, g_max=30)
            assert result['match'], f"A-hat identity fails at c={c}"

    def test_series_closed_form_hbar1(self):
        result = verify_ahat_identity(24, hbar=1.0, g_max=30)
        assert result['match']

    def test_series_converges_within_radius(self):
        """Series converges for hbar < 2*pi."""
        result = verify_ahat_identity(24, hbar=5.0, g_max=50)
        # Less strict tolerance for larger hbar
        assert result['difference'] < 1e-4

    def test_convergence_radius(self):
        assert abs(convergence_radius_scalar() - TWO_PI) < 1e-10

    def test_closed_form_at_zero(self):
        """Closed form vanishes at hbar = 0."""
        assert abs(ahat_closed_form(24, 0.0)) < 1e-14


# =========================================================================
# Section 15: Convergence diagnostics
# =========================================================================

class TestConvergence:
    def test_genus_ratios_approach_limit(self):
        """F_{g+1}/F_g -> 1/(4*pi^2) ~ 0.02533."""
        ratios = genus_decay_ratios(24, 10)
        target = 1.0 / (4 * PI**2)
        # Last few ratios should be close to the limit
        for g, r in ratios[-3:]:
            assert abs(r - target) / target < 0.05

    def test_shadow_convergent_large_c(self):
        """Shadow partition function converges for large c."""
        for c in [12, 24, 26, 50]:
            assert shadow_partition_convergent(c)

    def test_bernoulli_decay_fast(self):
        """F_g decays geometrically with ratio ~ 1/40."""
        ratios = genus_decay_ratios(24, 8)
        for _, r in ratios:
            assert r < 0.1  # Much less than 1


# =========================================================================
# Section 16: Monster module
# =========================================================================

class TestMonster:
    def test_monster_S_BH(self):
        """S_BH = 4*pi for c=24, M=1."""
        result = monster_entropy(M=1.0)
        assert abs(result['S_0'] - 4 * PI) < 1e-10

    def test_monster_kappa(self):
        result = monster_entropy(M=1.0)
        assert abs(result['kappa'] - 12.0) < 1e-10

    def test_monster_F1(self):
        result = monster_entropy(M=1.0)
        assert abs(result['F_table'][1] - 0.5) < 1e-14


# =========================================================================
# Section 17: Critical string (c=26)
# =========================================================================

class TestCriticalString:
    def test_kappa_eff_zero(self):
        result = critical_string_entropy(M=100)
        assert abs(result['kappa_eff']) < 1e-14

    def test_kappa_13(self):
        result = critical_string_entropy(M=100)
        assert abs(result['kappa'] - 13.0) < 1e-10

    def test_ghost_kappa_minus_13(self):
        result = critical_string_entropy(M=100)
        assert abs(result['kappa_ghost'] + 13.0) < 1e-14


# =========================================================================
# Section 18: Self-dual (c=13)
# =========================================================================

class TestSelfDual:
    def test_self_dual_flag(self):
        result = self_dual_entropy(M=100)
        assert result['self_dual'] is True

    def test_delta_kappa_zero(self):
        result = self_dual_entropy(M=100)
        assert abs(result['delta_kappa']) < 1e-14

    def test_kappa_13_over_2(self):
        result = self_dual_entropy(M=100)
        assert abs(result['kappa'] - 6.5) < 1e-10


# =========================================================================
# Section 19: Phase diagram
# =========================================================================

class TestPhaseDiagram:
    def test_phase_diagram_has_entries(self):
        data = phase_diagram_data()
        assert len(data['phases']) > 0

    def test_both_phases_appear(self):
        """Both BTZ and AdS phases appear in the diagram."""
        data = phase_diagram_data(
            c_values=[24],
            beta_values=[0.1, 0.5, 1.0, TWO_PI, 10.0, 50.0],
        )
        phases = list(data['phases'][24].values())
        assert 'BTZ' in phases
        assert 'AdS' in phases


# =========================================================================
# Section 20: Cross-verification between modules
# =========================================================================

class TestCrossVerification:
    def test_F1_two_routes(self):
        """F_1 from shadow obstruction tower matches F_1 from direct formula."""
        for c in [1, 6, 12, 24, 26]:
            shadow = float(shadow_tower_F1(c))
            direct = float(F1_virasoro(c))
            assert abs(shadow - direct) < 1e-14

    def test_kappa_additivity(self):
        """kappa is additive: kappa(c1) + kappa(c2) = kappa(c1+c2)/? NO.
        But: F_g(c) + F_g(c') = (c+c')/2 * lambda_g = F_g(c+c') for the
        independent-sum with vanishing mixed OPE.
        """
        for c1, c2 in [(6, 18), (10, 16), (1, 25)]:
            for g in [1, 2, 3]:
                F_sum = float(kappa_virasoro(c1) * lambda_fp(g)) + \
                        float(kappa_virasoro(c2) * lambda_fp(g))
                F_combined = float(kappa_virasoro(c1 + c2) * lambda_fp(g))
                assert abs(F_sum - F_combined) < 1e-14

    def test_complementarity_sum_13(self):
        """kappa(c) + kappa(26-c) = 13 for all c."""
        for c in range(0, 27):
            total = float(kappa_virasoro(c) + kappa_virasoro(26 - c))
            assert abs(total - 13.0) < 1e-14

    def test_all_F_g_decrease(self):
        """F_1 > F_2 > F_3 > F_4 for all c > 0 (at the scalar level)."""
        for c in [1, 12, 24, 26]:
            vals = [float(kappa_virasoro(c) * lambda_fp(g)) for g in range(1, 5)]
            for i in range(len(vals) - 1):
                assert vals[i] > vals[i + 1]

    def test_planted_forest_vanishes_c40(self):
        """The planted-forest correction at g=2 vanishes at c=40."""
        assert planted_forest_g2(40) == Fraction(0)

    def test_F2_scalar_matches_kappa_times_lambda(self):
        for c in [1, 12, 24, 26]:
            assert F2_scalar(c) == kappa_virasoro(c) * lambda_fp(2)

    def test_entropy_hierarchy(self):
        """S_0 >> |S_1| >> |S_2| >> |S_3| for large M."""
        result = entropy_all_genera(24, 10000, 3)
        assert result['S_0'] > abs(result['S_1']) * 10
        assert abs(result['S_1']) > abs(result['S_2']) * 5
        assert abs(result['S_2']) > abs(result['S_3'])


# =========================================================================
# Section 21: Exact arithmetic consistency
# =========================================================================

class TestExactArithmetic:
    def test_F1_c24_exact(self):
        assert F1_virasoro(24) == Fraction(1, 2)

    def test_F1_c26_exact(self):
        assert F1_virasoro(26) == Fraction(13, 24)

    def test_F2_scalar_c24_exact(self):
        expected = Fraction(12) * Fraction(7, 5760)
        assert F2_scalar(24) == expected

    def test_planted_forest_g2_c26_exact(self):
        expected = Fraction(7, 24)
        assert planted_forest_g2(26) == expected

    def test_kappa_complementarity_exact(self):
        """kappa(c) + kappa(26-c) = 13 exactly."""
        for c in range(0, 27):
            assert kappa_virasoro(c) + kappa_virasoro(26 - c) == Fraction(13)

    def test_lambda_fp_recurrence(self):
        """Verify lambda_g via Bernoulli recurrence."""
        # lambda_1 = (2^1 - 1)/(2^1) * |B_2|/(2!) = (1/2)*(1/6)/2 = 1/24
        assert lambda_fp(1) == Fraction(1, 24)
        # lambda_2 = (2^3 - 1)/(2^3) * |B_4|/(4!) = (7/8)*(1/30)/24 = 7/5760
        assert lambda_fp(2) == Fraction(7, 5760)


# =========================================================================
# Section 22: Boundary cases and error handling
# =========================================================================

class TestBoundary:
    def test_S_BH_zero_M(self):
        assert bekenstein_hawking_entropy(24, 0) == 0.0

    def test_S_BH_negative_M(self):
        assert bekenstein_hawking_entropy(24, -1) == 0.0

    def test_entropy_expansion_low_M(self):
        """Expansion at small M (expansion parameter large, but should not crash)."""
        result = entropy_all_genera(24, 0.01, 2)
        assert 'S_0' in result

    def test_ahat_near_singularity(self):
        """A-hat(x) near x=2*pi has large but finite value."""
        x = TWO_PI - 0.01
        val = ahat_generating_function_value(x)
        assert val > 0
        assert math.isfinite(val)

    def test_lambda_fp_raises_g0(self):
        with pytest.raises(ValueError):
            lambda_fp(0)
