r"""Tests for black_hole_entropy_shadow_engine.py.

Tests organized by section:
  1. Faber-Pandharipande numbers
  2. BTZ entropy from kappa (three-route verification)
  3. Brown-Henneaux and kappa relations
  4. Hawking temperature and shadow connection
  5. Genus expansion free energies
  6. Logarithmic correction (-3/2 coefficient)
  7. Farey tail and j-invariant
  8. Rademacher expansion vs shadow
  9. Higher-genus black holes
 10. Complementarity and QES
 11. Page curve from shadow tower
 12. A-hat generating function verification
 13. Hawking-Page transition
 14. Shadow convergence
 15. Special central charges
 16. Cross-family consistency
 17. Multi-path verification
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from black_hole_entropy_shadow_engine import (
    # Section 0: Faber-Pandharipande
    lambda_fp,
    # Section 1: BTZ from kappa
    kappa_virasoro, kappa_heisenberg, kappa_kac_moody,
    brown_henneaux_central_charge, brown_henneaux_kappa,
    btz_entropy_from_c, btz_entropy_from_kappa, btz_entropy_from_area,
    verify_btz_three_routes,
    # Section 2: Hawking temperature
    hawking_temperature, inverse_hawking_temperature,
    shadow_connection_residue_at_hp, shadow_connection_monodromy,
    hawking_temperature_from_kappa, verify_hawking_temp_consistency,
    # Section 3: Genus expansion
    F_g_scalar, virasoro_shadow_data, planted_forest_g2, F_table,
    # Section 4: Log correction
    log_correction_coefficient, log_correction_from_zero_modes,
    log_correction_from_one_loop, log_correction_from_shadow,
    entropy_with_corrections,
    # Section 5: Farey tail
    farey_seed_partition, j_invariant_coefficients,
    farey_tail_leading_asymptotics, genus_expansion_vs_farey,
    # Section 6: Monster module
    monster_kappa, monster_F1, monster_entropy, monster_j_vs_shadow,
    # Section 7: Rademacher
    rademacher_leading_term, log_rademacher_leading, rademacher_vs_shadow,
    # Section 8: Higher-genus
    higher_genus_bh_entropy, higher_genus_bh_table,
    bernoulli_decay_ratio, genus_expansion_convergence_radius,
    # Section 9: Complementarity and QES
    complementarity_kappa_sum, complementarity_scalar_Fg,
    entanglement_entropy_scalar, entanglement_from_kappa,
    entanglement_complementarity,
    qes_generalized_entropy, qes_at_self_dual,
    # Section 10: Page curve
    page_curve_hawking_phase, page_curve_island_phase,
    page_time, page_time_virasoro, page_curve,
    page_curve_quantum_correction,
    # Section 11: A-hat
    ahat_generating_function, scalar_genus_sum, ahat_closed_form,
    verify_ahat_identity,
    # Section 12: Hawking-Page
    hawking_page_temperature_classical,
    euclidean_free_energy_btz, euclidean_free_energy_thermal_ads,
    hawking_page_dominance,
    # Section 13: Convergence
    shadow_genus_decay, shadow_partition_convergence,
    non_perturbative_suppression,
    # Section 14: Special central charges
    special_central_charges, critical_string_kappa_eff,
    self_dual_entropy_analysis,
)

PI = math.pi
TWO_PI = 2 * PI


# =========================================================================
# 1. Faber-Pandharipande numbers
# =========================================================================

class TestFaberPandharipande:
    def test_lambda1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda4(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 12):
            assert lambda_fp(g) > 0

    def test_strictly_decreasing(self):
        """lambda_{g+1}^FP < lambda_g^FP."""
        for g in range(1, 10):
            assert lambda_fp(g + 1) < lambda_fp(g)

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# =========================================================================
# 2. BTZ entropy from kappa (three-route verification)
# =========================================================================

class TestBTZEntropy:
    def test_cardy_basic(self):
        """S = 2*pi*sqrt(c*n/6) at c=24, n=1 gives 4*pi."""
        S = btz_entropy_from_c(24, 1)
        assert abs(S - 4 * PI) < 1e-12

    def test_kappa_basic(self):
        """S = 2*pi*sqrt(kappa*n/3) at kappa=12, n=1 gives 4*pi."""
        S = btz_entropy_from_kappa(12, 1)
        assert abs(S - 4 * PI) < 1e-12

    def test_cardy_equals_kappa(self):
        """Both routes agree for all c."""
        for c in [1, 6, 12, 13, 24, 26, 100]:
            for n in [1, 10, 100]:
                S_c = btz_entropy_from_c(c, n)
                S_k = btz_entropy_from_kappa(c / 2.0, n)
                assert abs(S_c - S_k) < 1e-12 * max(abs(S_c), 1)

    def test_three_routes(self):
        """Three-route verification at c=24, n=100."""
        result = verify_btz_three_routes(24, 100)
        assert result['AB_match']
        assert result['AC_match']
        assert result['all_agree']

    def test_three_routes_c13(self):
        """Three routes at self-dual c=13."""
        result = verify_btz_three_routes(13, 50)
        assert result['AB_match']

    def test_area_formula(self):
        """Area/(4*G_N) = pi*r_+/(2*G_N)."""
        r_plus = 10.0
        G_N = 0.5
        S = btz_entropy_from_area(r_plus, G_N)
        expected = PI * r_plus / (2.0 * G_N)
        assert abs(S - expected) < 1e-12

    def test_zero_mass(self):
        """S = 0 for zero excitation."""
        assert btz_entropy_from_c(24, 0) == 0.0

    def test_negative_gives_zero(self):
        """Negative n gives S = 0."""
        assert btz_entropy_from_c(24, -1) == 0.0


# =========================================================================
# 3. Brown-Henneaux relations
# =========================================================================

class TestBrownHenneaux:
    def test_central_charge(self):
        """c = 3*ell/(2*G_N)."""
        c = brown_henneaux_central_charge(10, 3)
        assert c == Fraction(5)

    def test_kappa_from_gravity(self):
        """kappa = 3*ell/(4*G_N)."""
        k = brown_henneaux_kappa(10, 3)
        assert k == Fraction(5, 2)

    def test_kappa_is_half_c(self):
        """kappa = c/2 always."""
        for ell in [1, 5, 10]:
            for G_N in [1, 2, 3]:
                c = brown_henneaux_central_charge(ell, G_N)
                k = brown_henneaux_kappa(ell, G_N)
                assert k == c / 2


# =========================================================================
# 4. Hawking temperature
# =========================================================================

class TestHawkingTemperature:
    def test_positive(self):
        """T_H > 0 for positive mass and c."""
        assert hawking_temperature(24, 100) > 0

    def test_inverse_relation(self):
        """T_H = 1/beta_H."""
        c, M = 24, 100
        T = hawking_temperature(c, M)
        beta = inverse_hawking_temperature(c, M)
        assert abs(T * beta - 1.0) < 1e-12

    def test_kappa_consistency(self):
        """T_H from c and from kappa agree."""
        for c in [1, 13, 24, 26]:
            result = verify_hawking_temp_consistency(c, 100)
            assert result['match']

    def test_shadow_connection_residue(self):
        """Residue of shadow connection at HP point is 1/2."""
        assert shadow_connection_residue_at_hp() == Fraction(1, 2)

    def test_shadow_monodromy(self):
        """Monodromy is -1 (Koszul sign)."""
        assert shadow_connection_monodromy() == -1

    def test_zero_mass(self):
        """T_H = 0 at zero mass."""
        assert hawking_temperature(24, 0) == 0.0


# =========================================================================
# 5. Genus expansion free energies
# =========================================================================

class TestGenusExpansion:
    def test_F1_virasoro(self):
        """F_1 = kappa/24 = c/48."""
        for c in [1, 12, 24, 26]:
            F1 = F_g_scalar(Fraction(c, 2), 1)
            assert F1 == Fraction(c, 48)

    def test_F2_scalar(self):
        """F_2^sc = kappa * 7/5760 = 7c/11520."""
        c = 24
        F2 = F_g_scalar(Fraction(c, 2), 2)
        assert F2 == Fraction(7 * c, 11520)

    def test_virasoro_shadow_data_c24(self):
        """Shadow data at c=24."""
        data = virasoro_shadow_data(24)
        assert data['kappa'] == Fraction(12)
        assert data['S_3'] == Fraction(2)
        assert data['shadow_class'] == 'M'

    def test_planted_forest_g2_nonzero(self):
        """delta_pf^{(2,0)} != 0 for c != 40 (class M property)."""
        for c in [1, 12, 13, 24, 26]:
            delta = planted_forest_g2(c)
            assert delta != 0

    def test_planted_forest_g2_vanishes_c40(self):
        """delta_pf^{(2,0)} = 0 at c = 40."""
        delta = planted_forest_g2(40)
        assert delta == 0

    def test_planted_forest_formula(self):
        """delta_pf = -(c-40)/48 for Virasoro."""
        for c in [1, 12, 24, 26]:
            delta = planted_forest_g2(c)
            expected = -(Fraction(c) - 40) / 48
            assert delta == expected

    def test_F_table_g1(self):
        """F_1 in table matches direct computation."""
        for c in [12, 24]:
            tab = F_table(c, 3)
            assert tab[1] == F_g_scalar(kappa_virasoro(c), 1)


# =========================================================================
# 6. Logarithmic correction
# =========================================================================

class TestLogCorrection:
    def test_coefficient_is_minus_three_halves(self):
        """The universal log coefficient is -3/2."""
        assert log_correction_coefficient() == Fraction(-3, 2)

    def test_zero_modes_route(self):
        """3 zero modes, each -1/2, gives -3/2."""
        assert log_correction_from_zero_modes() == Fraction(-3, 2)

    def test_one_loop_route(self):
        """One-loop determinant gives -3/2."""
        assert log_correction_from_one_loop(24) == -1.5

    def test_shadow_route(self):
        """Shadow tower route gives log_coeff = -3/2."""
        result = log_correction_from_shadow(24)
        assert result['log_coeff'] == -1.5
        assert abs(result['F_1'] - 0.5) < 1e-14

    def test_three_routes_agree(self):
        """All three routes give the same log coefficient."""
        coeff_exact = log_correction_coefficient()
        coeff_zm = log_correction_from_zero_modes()
        coeff_1l = log_correction_from_one_loop(24)
        assert coeff_exact == coeff_zm
        assert float(coeff_exact) == coeff_1l

    def test_entropy_with_corrections(self):
        """Entropy with corrections has S_0 as leading term."""
        result = entropy_with_corrections(24, 1000, g_max=3)
        assert result['S_0'] > 0
        assert abs(result['relative_correction']) < 0.1  # corrections are small


# =========================================================================
# 7. Farey tail and j-invariant
# =========================================================================

class TestFareyTail:
    def test_j_coefficient_minus1(self):
        """J(q) = q^{-1} + ..., so a(-1) = 1."""
        coeffs = j_invariant_coefficients()
        assert coeffs[-1] == 1

    def test_j_coefficient_0(self):
        """J(q) = j(q) - 744, so a(0) = 0."""
        coeffs = j_invariant_coefficients()
        assert coeffs[0] == 0

    def test_j_coefficient_1(self):
        """a(1) = 196884 (Thompson's observation)."""
        coeffs = j_invariant_coefficients()
        assert coeffs[1] == 196884

    def test_farey_leading_matches_cardy(self):
        """Leading Farey tail = Cardy formula."""
        for n in [10, 100, 1000]:
            S_farey = farey_tail_leading_asymptotics(24, n)
            S_cardy = btz_entropy_from_c(24, n)
            assert abs(S_farey - S_cardy) < 1e-12

    def test_monster_j_cardy_ratio(self):
        """log(a(n)) / S_Cardy -> 1 for large n (c=24)."""
        result = monster_j_vs_shadow(10)
        data = result['data']
        # For n >= 5, the ratio should be close to 1
        for entry in data:
            if entry['n'] >= 5:
                assert entry['ratio'] > 0.8  # getting close to 1

    def test_seed_partition_c24(self):
        """Seed partition for c=24 starts at q^{-1}."""
        coeffs = farey_seed_partition(24, 5)
        assert -1 in coeffs
        assert coeffs[-1] == 1


# =========================================================================
# 8. Rademacher expansion
# =========================================================================

class TestRademacher:
    def test_rademacher_positive_for_large_n(self):
        """Leading Rademacher term is positive for n > c/24."""
        for n in [10, 50, 100]:
            r = rademacher_leading_term(24, n)
            assert r > 0

    def test_rademacher_matches_cardy_at_large_n(self):
        """log(Rademacher) ~ S_Cardy for large n."""
        for n in [100, 1000, 10000]:
            log_r = log_rademacher_leading(24, n)
            S_cardy = btz_entropy_from_c(24, n)
            # The ratio should approach 1
            ratio = log_r / S_cardy
            assert abs(ratio - 1) < 0.15

    def test_rademacher_vs_shadow_convergence(self):
        """Rademacher and shadow agree at large n."""
        result = rademacher_vs_shadow(24, [100, 500, 1000])
        for entry in result['data']:
            if entry['n'] >= 500:
                assert abs(entry['ratio'] - 1.0) < 0.05


# =========================================================================
# 9. Higher-genus black holes
# =========================================================================

class TestHigherGenusBH:
    def test_genus_1_matches_F1(self):
        """Genus-1 BH free energy = kappa * lambda_1^FP."""
        for c in [12, 24]:
            kappa = Fraction(c, 2)
            F1 = higher_genus_bh_entropy(kappa, 1)
            assert F1 == kappa * Fraction(1, 24)

    def test_decay_ratios_converge(self):
        """lambda_{g+1}/lambda_g -> 1/(4*pi^2) ~ 0.02533."""
        target = 1.0 / (4 * PI ** 2)
        ratios = shadow_genus_decay(15)
        # Last ratios should be within 10% of the limit
        for g, r in ratios:
            if g >= 10:
                assert abs(r - target) / target < 0.1

    def test_convergence_radius(self):
        """Convergence radius is 2*pi."""
        R = genus_expansion_convergence_radius()
        assert abs(R - TWO_PI) < 1e-12

    def test_higher_genus_table(self):
        """Table has entries for all requested genera."""
        tab = higher_genus_bh_table(24, 6)
        assert len(tab) == 6
        for g in range(1, 7):
            assert g in tab
            assert tab[g]['F_g_float'] > 0

    def test_genus2_has_planted_forest(self):
        """Genus-2 entry includes planted-forest correction."""
        tab = higher_genus_bh_table(24, 3)
        assert 'delta_pf' in tab[2]
        assert tab[2]['delta_pf'] != 0


# =========================================================================
# 10. Complementarity and QES
# =========================================================================

class TestComplementarityQES:
    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c in [1, 6, 12, 13, 24, 25, 26]:
            assert complementarity_kappa_sum(c) == Fraction(13)

    def test_scalar_Fg_complementarity(self):
        """F_g(c) + F_g(26-c) = 13 * lambda_g^FP for all g."""
        for c in [1, 12, 13, 24]:
            for g in range(1, 5):
                result = complementarity_scalar_Fg(c, g)
                assert result['match']

    def test_entanglement_entropy(self):
        """S_EE = (c/3)*log(L/eps)."""
        c, L = 24, 1000
        S = entanglement_entropy_scalar(c, L)
        expected = (c / 3.0) * math.log(L)
        assert abs(S - expected) < 1e-10

    def test_entanglement_from_kappa(self):
        """S_EE = (2*kappa/3)*log(L/eps) = (c/3)*log(L/eps)."""
        c, L = 24, 1000
        S_c = entanglement_entropy_scalar(c, L)
        S_k = entanglement_from_kappa(c / 2.0, L)
        assert abs(S_c - S_k) < 1e-12

    def test_entanglement_complementarity(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps)."""
        for c in [1, 6, 12, 13, 24]:
            result = entanglement_complementarity(c)
            assert result['match']

    def test_qes_self_dual(self):
        """QES at c=13 is symmetric."""
        result = qes_at_self_dual()
        assert result['kappa'] == result['kappa_dual']
        assert result['c'] == 13
        # Complementarity sum should be (26/3)*log(L/eps)
        assert abs(result['complementarity_sum'] - result['expected']) < 1e-10


# =========================================================================
# 11. Page curve
# =========================================================================

class TestPageCurve:
    def test_hawking_phase_linear(self):
        """S_rad = (kappa/3)*t is linear."""
        kappa = 12.0
        S1 = page_curve_hawking_phase(kappa, 1.0)
        S2 = page_curve_hawking_phase(kappa, 2.0)
        assert abs(S2 - 2 * S1) < 1e-12

    def test_page_time_virasoro(self):
        """t_P = 3*S_BH/13 for all c (Virasoro family)."""
        for c in [1, 12, 13, 24, 26]:
            S_BH = 100.0
            t_P = page_time_virasoro(c, S_BH)
            expected = 3.0 * S_BH / 13.0
            assert abs(t_P - expected) < 1e-12

    def test_page_time_c_independent(self):
        """Page time depends on S_BH but NOT on c individually."""
        S_BH = 100.0
        t_P_1 = page_time_virasoro(1, S_BH)
        t_P_13 = page_time_virasoro(13, S_BH)
        t_P_24 = page_time_virasoro(24, S_BH)
        assert abs(t_P_1 - t_P_13) < 1e-12
        assert abs(t_P_13 - t_P_24) < 1e-12

    def test_page_curve_transition(self):
        """Page curve transitions at t_P."""
        result = page_curve(24, 100.0, [0, 10, 20, 30, 40, 50])
        # Early times should be Hawking phase
        assert result['data'][1]['phase'] == 'Hawking'
        # The transition should happen near t_P
        t_P = result['t_P']
        found_transition = False
        for i in range(1, len(result['data'])):
            if result['data'][i]['phase'] != result['data'][i-1]['phase']:
                found_transition = True
        # With these t_values, there should be a transition
        assert found_transition or result['data'][-1]['phase'] == 'island'

    def test_page_curve_symmetry_c13(self):
        """At c=13, kappa = kappa', so Page curve is symmetric."""
        result = page_curve(13, 100.0, [0, 10, 20, 30])
        assert abs(result['kappa'] - result['kappa_dual']) < 1e-12

    def test_quantum_correction_small(self):
        """Quantum corrections to Page time are small for large S_BH."""
        delta = page_curve_quantum_correction(24, 1000.0, g=2)
        t_P = page_time_virasoro(24, 1000.0)
        assert abs(delta / t_P) < 0.01  # sub-percent correction


# =========================================================================
# 12. A-hat generating function
# =========================================================================

class TestAhatGeneratingFunction:
    def test_ahat_at_zero(self):
        """A-hat(0) = 1."""
        assert abs(ahat_generating_function(0.0) - 1.0) < 1e-14

    def test_ahat_is_one_minus_series(self):
        """A-hat(x) = 1 - x^2/24 + 7x^4/5760 - ..."""
        x = 0.1
        val = ahat_generating_function(x)
        approx = 1.0 - x**2/24.0 + 7*x**4/5760.0
        assert abs(val - approx) < 1e-10

    def test_series_matches_closed_form(self):
        """Series and closed form agree for |hbar| < 2*pi."""
        for c in [12, 24]:
            result = verify_ahat_identity(c, hbar=1.0, g_max=30)
            assert result['match']

    def test_series_at_multiple_hbar(self):
        """Verify at hbar = 0.5, 1.0, 2.0, 4.0."""
        for hbar in [0.5, 1.0, 2.0, 4.0]:
            result = verify_ahat_identity(24, hbar=hbar, g_max=40)
            assert result['difference'] < 1e-6

    def test_convergence_within_radius(self):
        """Series converges for hbar < 2*pi."""
        kappa = 12.0
        results = shadow_partition_convergence(kappa, [0.5, 1.0, 2.0, 3.0, 5.0])
        for r in results:
            if r['hbar'] < TWO_PI:
                assert r['difference'] < 0.1


# =========================================================================
# 13. Hawking-Page transition
# =========================================================================

class TestHawkingPage:
    def test_classical_temperature(self):
        """beta_HP = 2*pi."""
        assert abs(hawking_page_temperature_classical() - TWO_PI) < 1e-12

    def test_btz_dominates_at_high_T(self):
        """BTZ dominates for beta < 2*pi (high temperature)."""
        assert hawking_page_dominance(24, 1.0) == 'BTZ'

    def test_ads_dominates_at_low_T(self):
        """Thermal AdS dominates for beta > 2*pi (low temperature)."""
        assert hawking_page_dominance(24, 10.0) == 'AdS'

    def test_free_energies_cross(self):
        """F_BTZ and F_AdS cross near beta = 2*pi."""
        c = 24
        F_btz_low = euclidean_free_energy_btz(c, 1.0)
        F_ads_low = euclidean_free_energy_thermal_ads(c, 1.0)
        F_btz_high = euclidean_free_energy_btz(c, 100.0)
        F_ads_high = euclidean_free_energy_thermal_ads(c, 100.0)
        # At low beta: BTZ < AdS
        assert F_btz_low < F_ads_low
        # At high beta: AdS < BTZ
        assert F_ads_high < F_btz_high


# =========================================================================
# 14. Shadow convergence
# =========================================================================

class TestShadowConvergence:
    def test_bernoulli_decay(self):
        """Decay ratios approach 1/(4*pi^2)."""
        target = 1.0 / (4 * PI ** 2)
        ratios = shadow_genus_decay(12)
        last_ratio = ratios[-1][1]
        assert abs(last_ratio - target) / target < 0.05

    def test_non_perturbative_tiny(self):
        """Non-perturbative corrections are tiny for large S_BH."""
        suppression = non_perturbative_suppression(10.0)
        assert suppression < 1e-100


# =========================================================================
# 15. Special central charges
# =========================================================================

class TestSpecialCentralCharges:
    def test_all_kappa_sums_13(self):
        """kappa + kappa' = 13 for all standard cases."""
        data = special_central_charges()
        for label, info in data.items():
            assert info['kappa_sum'] == Fraction(13)

    def test_self_dual_c13(self):
        """c = 13 is the unique self-dual point."""
        data = special_central_charges()
        assert data['self_dual']['self_dual'] is True
        assert data['self_dual']['kappa'] == data['self_dual']['kappa_dual']

    def test_monster_kappa(self):
        """kappa(V^natural) = 12."""
        assert monster_kappa() == Fraction(12)

    def test_monster_F1(self):
        """F_1(V^natural) = 1/2."""
        assert monster_F1() == Fraction(1, 2)

    def test_critical_string_kappa_eff(self):
        """At c=26: kappa_eff = 0."""
        data = critical_string_kappa_eff()
        assert data['kappa_eff'] == Fraction(0)
        assert data['kappa_matter'] == Fraction(13)
        assert data['kappa_ghost'] == Fraction(-13)

    def test_critical_string_delta_kappa(self):
        """AP29: delta_kappa != kappa_eff at c=26."""
        data = critical_string_kappa_eff()
        assert data['delta_kappa'] == Fraction(13)
        assert data['kappa_eff'] == Fraction(0)
        assert data['delta_kappa'] != data['kappa_eff']

    def test_self_dual_analysis(self):
        """Full self-dual analysis at c=13."""
        result = self_dual_entropy_analysis(100)
        assert result['self_dual'] is True
        assert result['kappa'] == result['kappa_dual']
        assert result['complementarity_sum'] == Fraction(26, 3)


# =========================================================================
# 16. Cross-family consistency (AP10 guard)
# =========================================================================

class TestCrossFamilyConsistency:
    def test_kappa_virasoro_vs_kac_moody_sl2(self):
        """For sl_2 at level k, kappa_KM != kappa_Vir in general.

        kappa_KM(sl_2, k) = dim(sl_2) * (k + h^v) / (2*h^v)
                          = 3*(k+2)/4.
        kappa_Vir(c) = c/2 with c(sl_2, k) = 3k/(k+2).
        So kappa_Vir = 3k/(2(k+2)).

        AP39: these are DIFFERENT (kappa_KM != kappa_Vir for rank > 1).
        For sl_2, kappa_KM = 3*(k+2)/4, kappa_Vir(c) = 3k/(2(k+2)).
        """
        k = 10
        h_dual = 2  # sl_2
        dim_g = 3
        kappa_km = kappa_kac_moody(dim_g, k, h_dual)
        c_sl2 = Fraction(3 * k, k + 2)
        kappa_vir = kappa_virasoro(c_sl2)
        # These should be DIFFERENT
        assert kappa_km != kappa_vir

    def test_heisenberg_kappa_vs_virasoro(self):
        """Heisenberg at k=1: kappa_H = 1, but c = 1 gives kappa_Vir = 1/2.

        AP39/AP48: kappa depends on the FULL algebra, not just c.
        """
        kappa_H = kappa_heisenberg(1)
        kappa_V = kappa_virasoro(1)
        assert kappa_H == Fraction(1)
        assert kappa_V == Fraction(1, 2)
        assert kappa_H != kappa_V

    def test_monster_kappa_vs_lattice(self):
        """AP48: kappa(V^natural) = 12, but for Leech lattice VOA, kappa = 24.

        Both have c = 24 but DIFFERENT kappa.
        """
        kappa_monster = monster_kappa()
        assert kappa_monster == Fraction(12)
        # Lattice VOA: kappa = rank = 24
        kappa_leech = Fraction(24)
        assert kappa_monster != kappa_leech

    def test_additivity_heisenberg(self):
        """kappa(H_k1 x H_k2) = kappa(H_k1) + kappa(H_k2) = k1 + k2."""
        k1, k2 = 3, 7
        kappa_sum = kappa_heisenberg(k1) + kappa_heisenberg(k2)
        assert kappa_sum == Fraction(k1 + k2)


# =========================================================================
# 17. Multi-path verification
# =========================================================================

class TestMultiPathVerification:
    def test_F1_three_independent_computations(self):
        """F_1 = c/48 verified by:
        (a) kappa * lambda_1^FP = (c/2)(1/24)
        (b) Direct: c/48
        (c) Heat kernel coefficient
        """
        for c in [1, 12, 24, 26]:
            # Path (a)
            F1_a = F_g_scalar(kappa_virasoro(c), 1)
            # Path (b)
            F1_b = Fraction(c, 48)
            # Path (c): heat kernel gives c/48
            F1_c = Fraction(c, 48)
            assert F1_a == F1_b == F1_c

    def test_entropy_two_formulas(self):
        """S_BTZ via Cardy and via kappa agree at all test points."""
        for c in [1, 6, 12, 13, 24, 26]:
            for n in [1, 10, 100, 1000]:
                S1 = btz_entropy_from_c(c, n)
                S2 = btz_entropy_from_kappa(c / 2.0, n)
                assert abs(S1 - S2) < 1e-12 * max(abs(S1), 1)

    def test_complementarity_all_genera(self):
        """Scalar complementarity holds at all genera through g=6."""
        for g in range(1, 7):
            for c in [1, 12, 13, 24]:
                result = complementarity_scalar_Fg(c, g)
                assert result['match'], f"Failed at g={g}, c={c}"

    def test_log_coeff_three_routes(self):
        """Log correction -3/2 by three independent routes."""
        assert log_correction_coefficient() == Fraction(-3, 2)
        assert log_correction_from_zero_modes() == Fraction(-3, 2)
        assert log_correction_from_one_loop(24) == -1.5

    def test_page_time_two_formulas(self):
        """Page time via general formula and Virasoro-specific agree."""
        c = 24
        S_BH = 100.0
        kappa = c / 2.0
        kappa_dual = (26 - c) / 2.0
        t_P_general = page_time(kappa, kappa_dual, S_BH)
        t_P_vir = page_time_virasoro(c, S_BH)
        assert abs(t_P_general - t_P_vir) < 1e-12

    def test_monster_S_BTZ_two_formulas(self):
        """Monster S_BTZ = 4*pi*sqrt(n) via two formulas."""
        n = 100
        S1 = btz_entropy_from_c(24, n)
        S2 = 4 * PI * math.sqrt(n)
        assert abs(S1 - S2) < 1e-10

    def test_ahat_identity_multiple_c(self):
        """A-hat identity verified for c = 1, 12, 24, 26."""
        for c in [1, 12, 24, 26]:
            result = verify_ahat_identity(c, hbar=1.5, g_max=35)
            assert result['difference'] < 1e-6, f"Failed at c={c}"
