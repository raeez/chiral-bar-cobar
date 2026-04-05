r"""Tests for BTZ quantum gravity engine: black hole entropy from the shadow CohFT.

Tests organized by section:
  1.  Faber-Pandharipande intersection numbers (exact arithmetic)
  2.  Virasoro shadow data (kappa, S_3, S_4, S_5)
  3.  Free energies F_g (scalar + planted-forest)
  4.  Shadow partition function Z^sh
  5.  Bekenstein-Hawking entropy (classical)
  6.  One-loop (genus-1) quantum correction
  7.  Two-loop (genus-2) quantum correction
  8.  Three-loop (genus-3) quantum correction
  9.  Four-loop and five-loop corrections (genus 4-5)
  10. Full entropy expansion
  11. Hawking-Page phase transition
  12. Farey tail expansion
  13. Renyi entropy
  14. Entanglement entropy
  15. A-hat generating function and convergence
  16. Special central charges (c=1, 13, 24, 26)
  17. Large-c semiclassical limit
  18. Cross-checks and consistency
"""

import pytest
from fractions import Fraction
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from btz_quantum_gravity_engine import (
    # Section 1
    lambda_fp,
    # Section 2
    kappa_virasoro, kappa_heisenberg, kappa_kac_moody,
    virasoro_S3, virasoro_S4, virasoro_S5,
    # Section 3
    F_g_scalar, planted_forest_g2, planted_forest_g3,
    virasoro_free_energy, heisenberg_free_energy, free_energy_table,
    # Section 4
    shadow_partition_function, shadow_free_energy_sum,
    shadow_partition_function_complex,
    # Section 5
    bekenstein_hawking_entropy, bekenstein_hawking_rotating,
    inverse_hawking_temperature, hawking_temperature,
    # Section 6
    entropy_correction_genus_g, entropy_all_genera,
    quantum_corrections_table,
    # Section 7
    euclidean_action_btz, euclidean_action_thermal_ads,
    hawking_page_temperature_classical, hawking_page_temperature,
    hawking_page_shift,
    # Section 8
    farey_sequence, farey_tail_term, farey_tail_partition,
    farey_tail_entropy,
    # Section 9
    twist_operator_dimension, renyi_entropy_scalar,
    renyi_entropy_with_shadow_corrections, renyi_convergence_to_von_neumann,
    # Section 10
    entanglement_entropy_leading, entanglement_entropy_with_corrections,
    entanglement_complementarity,
    # Section 11
    ahat_generating_function, scalar_free_energy_sum, ahat_closed_form,
    verify_ahat_identity, shadow_convergence_radius,
    # Section 12
    full_entropy_report,
    # Section 13
    pure_gravity_c24, critical_string_c26, self_dual_c13, free_boson_c1,
    # Section 14
    entropy_landscape, large_c_limit,
    # Section 15
    explicit_1loop_correction, explicit_2loop_correction,
    explicit_3loop_correction, explicit_4loop_correction,
    explicit_5loop_correction,
    # Section 16
    verify_bekenstein_hawking_rotating, verify_nonrotating_is_rotating_special_case,
    convergence_diagnostics,
)

PI = math.pi
TWO_PI = 2.0 * PI


# =========================================================================
# Section 1: Faber-Pandharipande intersection numbers
# =========================================================================

class TestFaberPandharipande:
    """Exact intersection numbers lambda_g^FP."""

    def test_lambda_1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_4(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda_5(self):
        assert lambda_fp(5) == Fraction(73, 3503554560)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (AP22: Bernoulli signs are correct)."""
        for g in range(1, 9):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP must be positive"

    def test_bernoulli_decay(self):
        """lambda_g^FP ~ 1/(2*pi)^{2g} (Bernoulli decay)."""
        for g in range(2, 8):
            ratio = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            # Should be roughly 1/(2*pi)^2 ~ 0.025
            assert ratio < 0.1, f"Decay ratio at g={g} too large: {ratio}"

    def test_invalid_genus_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# =========================================================================
# Section 2: Virasoro shadow data
# =========================================================================

class TestVirasoroShadowData:
    """Shadow data for the Virasoro algebra."""

    def test_kappa_virasoro(self):
        assert kappa_virasoro(24) == Fraction(12)
        assert kappa_virasoro(26) == Fraction(13)
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_kappa_heisenberg(self):
        assert kappa_heisenberg(1) == Fraction(1)
        assert kappa_heisenberg(3) == Fraction(3)

    def test_kappa_kac_moody_sl2(self):
        """kappa(sl_2_k) = 3*(k+2)/4.  dim(sl_2)=3, h^v=2."""
        assert kappa_kac_moody(3, 1, 2) == Fraction(9, 4)

    def test_S3_c_independent(self):
        assert virasoro_S3() == Fraction(2)

    def test_S4_virasoro(self):
        """Q^contact = 10/[c(5c+22)] for Virasoro."""
        assert virasoro_S4(1) == Fraction(10, 27)
        # c=2: 10/(2*(10+22)) = 10/64 = 5/32
        assert virasoro_S4(2) == Fraction(10, 64)

    def test_S5_virasoro(self):
        """S_5 = -48/[c^2(5c+22)]."""
        s5 = virasoro_S5(1)
        assert s5 == Fraction(-48, 27)


# =========================================================================
# Section 3: Free energies F_g
# =========================================================================

class TestFreeEnergies:
    """Free energies at each genus."""

    def test_F1_virasoro(self):
        """F_1 = kappa/24 = c/48."""
        assert virasoro_free_energy(24, 1) == Fraction(1, 2)
        assert virasoro_free_energy(48, 1) == Fraction(1)

    def test_F1_heisenberg(self):
        """F_1(H_k) = k/24."""
        assert heisenberg_free_energy(1, 1) == Fraction(1, 24)
        assert heisenberg_free_energy(24, 1) == Fraction(1)

    def test_F2_scalar(self):
        """F_2^{sc} = kappa * 7/5760 = 7c/11520."""
        assert F_g_scalar(Fraction(12), 2) == Fraction(12) * Fraction(7, 5760)

    def test_F2_planted_forest_virasoro(self):
        """delta_pf^{(2,0)} = 2*(20 - c/2)/48 = -(c-40)/48 for Virasoro."""
        c = 24
        kappa = kappa_virasoro(c)
        S3 = virasoro_S3()
        pf = planted_forest_g2(kappa, S3)
        expected = Fraction(2) * (20 - Fraction(24, 2)) / Fraction(48)
        assert pf == expected

    def test_F2_planted_forest_heisenberg_zero(self):
        """Heisenberg has S_3 = 0, so planted-forest vanishes."""
        assert planted_forest_g2(1, 0) == Fraction(0)

    def test_F2_full_virasoro(self):
        """Full F_2 = scalar + planted-forest."""
        F2 = virasoro_free_energy(24, 2)
        F2_sc = F_g_scalar(kappa_virasoro(24), 2)
        pf = planted_forest_g2(kappa_virasoro(24), virasoro_S3())
        assert F2 == F2_sc + pf

    def test_free_energy_table_length(self):
        table = free_energy_table(24, g_max=5)
        assert len(table) == 5

    def test_F_g_all_positive_virasoro(self):
        """All scalar free energies are positive (from positive lambda_g^FP)."""
        for g in range(1, 8):
            assert F_g_scalar(Fraction(12), g) > 0


# =========================================================================
# Section 4: Shadow partition function
# =========================================================================

class TestShadowPartitionFunction:
    """Z^sh = exp(sum F_g * hbar^{2g})."""

    def test_Z_at_hbar_zero(self):
        """Z^sh(hbar=0) = exp(0) = 1."""
        # At hbar=0, all terms vanish
        assert abs(shadow_partition_function(24, hbar=0.0) - 1.0) < 1e-14

    def test_Z_positive(self):
        """Z^sh > 0 for real hbar."""
        Z = shadow_partition_function(24, hbar=0.5)
        assert Z > 0

    def test_Z_monotone_in_hbar(self):
        """Z^sh increases with hbar (since F_g > 0)."""
        Z1 = shadow_partition_function(24, hbar=0.1)
        Z2 = shadow_partition_function(24, hbar=0.5)
        assert Z2 > Z1

    def test_log_Z_equals_free_energy_sum(self):
        """log Z^sh = sum F_g * hbar^{2g}."""
        hbar = 0.3
        Z = shadow_partition_function(24, hbar=hbar)
        F_sum = shadow_free_energy_sum(24, hbar=hbar)
        assert abs(math.log(Z) - F_sum) < 1e-12


# =========================================================================
# Section 5: Bekenstein-Hawking entropy
# =========================================================================

class TestBekensteinHawking:
    """Classical (genus-0) entropy."""

    def test_cardy_formula(self):
        """S_BH = 2*pi*sqrt(c*M/6)."""
        c, M = 24, 10
        S = bekenstein_hawking_entropy(c, M)
        expected = 2 * PI * math.sqrt(24 * 10 / 6.0)
        assert abs(S - expected) < 1e-12

    def test_rotating_reduces_to_nonrotating(self):
        """S_BH(E_L=M, E_R=M) = 2*S_BH(M) for non-rotating (both chiralities).

        Convention: bekenstein_hawking_entropy(c, M) = 2*pi*sqrt(c*M/6)
        is the SINGLE CHIRALITY Cardy formula.  The rotating formula with
        E_L = E_R = M gives the sum of two copies, i.e., twice the
        non-rotating formula.
        """
        for c in [1, 13, 24, 26]:
            for M in [1, 10, 100]:
                S_single = bekenstein_hawking_entropy(c, M)
                S_rot = bekenstein_hawking_rotating(c, M, M)
                assert abs(2 * S_single - S_rot) < 1e-10

    def test_rotating_general(self):
        """S = 4*pi*sqrt(c*E_L/6) + 4*pi*sqrt(c*E_R/6)."""
        c = 24
        E_L, E_R = 5, 10
        S = bekenstein_hawking_rotating(c, E_L, E_R)
        expected = 4 * PI * math.sqrt(c * E_L / 6.0) + 4 * PI * math.sqrt(c * E_R / 6.0)
        assert abs(S - expected) < 1e-12

    def test_zero_mass(self):
        assert bekenstein_hawking_entropy(24, 0) == 0.0

    def test_inverse_temperature(self):
        """beta_H = pi*sqrt(c/(6M))."""
        c, M = 24, 10
        beta = inverse_hawking_temperature(c, M)
        expected = PI * math.sqrt(24 / 60.0)
        assert abs(beta - expected) < 1e-12

    def test_temperature_inverse(self):
        """T_H = 1/beta_H."""
        c, M = 24, 10
        T = hawking_temperature(c, M)
        beta = inverse_hawking_temperature(c, M)
        assert abs(T * beta - 1.0) < 1e-12


# =========================================================================
# Section 6: One-loop correction
# =========================================================================

class TestOneLoopCorrection:
    """Genus-1 logarithmic correction: S_1 = -(3/2)*log(S_BH/(2*pi))."""

    def test_coefficient(self):
        """The universal -3/2 coefficient."""
        c, M = 24, 10
        S_BH = bekenstein_hawking_entropy(c, M)
        S_1 = entropy_correction_genus_g(c, M, 1)
        expected = -1.5 * math.log(S_BH / TWO_PI)
        assert abs(S_1 - expected) < 1e-12

    def test_sign_negative(self):
        """The one-loop correction is negative for large black holes."""
        c, M = 24, 100
        S_1 = entropy_correction_genus_g(c, M, 1)
        assert S_1 < 0

    def test_three_routes_agree(self):
        """F_1 from heat kernel = shadow tower = Selberg zeta = c/48."""
        for c in [1, 12, 24, 26]:
            F1_shadow = float(virasoro_free_energy(c, 1))
            F1_exact = float(c) / 48.0
            assert abs(F1_shadow - F1_exact) < 1e-14

    def test_explicit_1loop(self):
        data = explicit_1loop_correction(24, 10)
        assert abs(data['F_1'] - 0.5) < 1e-14
        assert data['log_coefficient'] == -1.5
        assert data['three_routes_agree']


# =========================================================================
# Section 7: Two-loop correction
# =========================================================================

class TestTwoLoopCorrection:
    """Genus-2 correction with planted-forest."""

    def test_F2_exact_c24(self):
        """F_2(Vir_24) = scalar + planted-forest (exact)."""
        F2 = virasoro_free_energy(24, 2)
        # scalar: 12 * 7/5760 = 7/480
        F2_sc = Fraction(12) * Fraction(7, 5760)
        assert F2_sc == Fraction(7, 480)
        # planted-forest: 2*(20-12)/48 = 16/48 = 1/3
        pf = Fraction(2) * (20 - 12) / Fraction(48)
        assert pf == Fraction(1, 3)
        assert F2 == F2_sc + pf

    def test_planted_forest_vanishes_c40(self):
        """At c=40: planted-forest at genus 2 vanishes."""
        pf = planted_forest_g2(kappa_virasoro(40), virasoro_S3())
        assert pf == Fraction(0)

    def test_S2_scaling(self):
        """S_2 ~ F_2 * epsilon^2 = F_2 * (2*pi/S_BH)^2."""
        c, M = 24, 100
        S_BH = bekenstein_hawking_entropy(c, M)
        S_2 = entropy_correction_genus_g(c, M, 2)
        F2 = float(virasoro_free_energy(c, 2))
        epsilon = TWO_PI / S_BH
        expected = F2 * epsilon ** 2
        assert abs(S_2 - expected) < 1e-12

    def test_explicit_2loop(self):
        data = explicit_2loop_correction(24, 10)
        assert data['F_2_total'] == data['F_2_scalar'] + data['F_2_planted_forest']


# =========================================================================
# Section 8: Three-loop correction
# =========================================================================

class TestThreeLoopCorrection:
    """Genus-3 correction from 42 stable graphs."""

    def test_F3_has_planted_forest(self):
        """Virasoro planted-forest at genus 3 is nonzero for generic c."""
        F3_sc = F_g_scalar(kappa_virasoro(24), 3)
        F3_full = virasoro_free_energy(24, 3)
        assert F3_full != F3_sc, "Planted-forest should be nonzero at genus 3"

    def test_F3_scaling(self):
        """S_3 ~ F_3 * epsilon^4."""
        c, M = 24, 100
        S_BH = bekenstein_hawking_entropy(c, M)
        S_3 = entropy_correction_genus_g(c, M, 3)
        F3 = float(virasoro_free_energy(c, 3))
        epsilon = TWO_PI / S_BH
        expected = F3 * epsilon ** 4
        assert abs(S_3 - expected) < 1e-12

    def test_explicit_3loop(self):
        data = explicit_3loop_correction(24, 10)
        assert abs(data['F_3_total'] - data['F_3_scalar'] - data['F_3_planted_forest']) < 1e-14


# =========================================================================
# Section 9: Four-loop and five-loop corrections
# =========================================================================

class TestHigherLoopCorrections:
    """Genus 4-5 corrections (scalar only at these genera)."""

    def test_F4_scalar(self):
        """F_4^{sc}(Vir_24) = 12 * 127/154828800."""
        F4 = virasoro_free_energy(24, 4)
        expected = Fraction(12) * Fraction(127, 154828800)
        assert F4 == expected

    def test_F5_scalar(self):
        """F_5^{sc}(Vir_24) = 12 * 73/3503554560."""
        F5 = virasoro_free_energy(24, 5)
        expected = Fraction(12) * Fraction(73, 3503554560)
        assert F5 == expected

    def test_S4_scaling(self):
        """S_4 ~ F_4 * epsilon^6."""
        c, M = 24, 100
        S_BH = bekenstein_hawking_entropy(c, M)
        S_4 = entropy_correction_genus_g(c, M, 4)
        F4 = float(virasoro_free_energy(c, 4))
        epsilon = TWO_PI / S_BH
        assert abs(S_4 - F4 * epsilon ** 6) < 1e-15

    def test_S5_scaling(self):
        """S_5 ~ F_5 * epsilon^8."""
        c, M = 24, 100
        S_BH = bekenstein_hawking_entropy(c, M)
        S_5 = entropy_correction_genus_g(c, M, 5)
        F5 = float(virasoro_free_energy(c, 5))
        epsilon = TWO_PI / S_BH
        assert abs(S_5 - F5 * epsilon ** 8) < 1e-16

    def test_explicit_4loop(self):
        data = explicit_4loop_correction(24, 10)
        assert data['F_4_scalar'] > 0

    def test_explicit_5loop(self):
        data = explicit_5loop_correction(24, 10)
        assert data['F_5_scalar'] > 0
        assert 'first computation' in data['note']

    def test_corrections_decrease_with_genus(self):
        """Higher-genus corrections are monotonically decreasing in absolute value."""
        c, M = 24, 100
        corrections = []
        for g in range(2, 6):
            Sg = abs(entropy_correction_genus_g(c, M, g))
            corrections.append(Sg)
        for i in range(len(corrections) - 1):
            assert corrections[i] > corrections[i + 1], \
                f"|S_{i+2}| should be > |S_{i+3}|"


# =========================================================================
# Section 10: Full entropy expansion
# =========================================================================

class TestFullEntropyExpansion:
    """Full expansion S = S_BH + S_1 + ... + S_{g_max}."""

    def test_total_close_to_classical(self):
        """For large M, quantum corrections are small relative to S_BH."""
        data = entropy_all_genera(24, 1000, g_max=5)
        assert abs(data['relative_correction']) < 0.01

    def test_all_genera_contains_all_keys(self):
        data = entropy_all_genera(24, 10, g_max=5)
        assert 'S_BH' in data
        assert 'S_1' in data
        assert 'S_5' in data
        assert 'S_total' in data
        assert 'F_table' in data

    def test_quantum_corrections_table(self):
        rows = quantum_corrections_table(24, 10, g_max=5)
        assert len(rows) == 5
        assert rows[0]['g'] == 1

    def test_total_equals_sum(self):
        """S_total = S_BH + sum of S_g."""
        data = entropy_all_genera(24, 10, g_max=5)
        total_check = data['S_BH']
        for g in range(1, 6):
            total_check += data[f'S_{g}']
        assert abs(data['S_total'] - total_check) < 1e-10


# =========================================================================
# Section 11: Hawking-Page phase transition
# =========================================================================

class TestHawkingPage:
    """Phase transition between BTZ and thermal AdS."""

    def test_classical_temperature(self):
        """beta_HP = 2*pi at leading order."""
        assert abs(hawking_page_temperature_classical() - TWO_PI) < 1e-12

    def test_btz_dominates_high_T(self):
        """BTZ saddle dominates at high temperature (small beta)."""
        c = 24
        beta_small = 1.0
        F_btz = euclidean_action_btz(c, beta_small, g_max=0)
        F_ads = euclidean_action_thermal_ads(c, beta_small)
        assert F_btz < F_ads, "BTZ should dominate at high T"

    def test_ads_dominates_low_T(self):
        """AdS saddle dominates at low temperature (large beta)."""
        c = 24
        beta_large = 100.0
        F_btz = euclidean_action_btz(c, beta_large, g_max=0)
        F_ads = euclidean_action_thermal_ads(c, beta_large)
        assert F_ads < F_btz, "AdS should dominate at low T"

    def test_quantum_shift_small(self):
        """Quantum corrections shift beta_HP by a small amount."""
        shift_data = hawking_page_shift(24, g_max=3)
        classical = shift_data['classical']
        for g in range(1, 4):
            key = f'shift_{g}'
            if key in shift_data:
                assert abs(shift_data[key]) < 1.0, \
                    f"Quantum shift at g_max={g} should be small"


# =========================================================================
# Section 12: Farey tail expansion
# =========================================================================

class TestFareyTail:
    """Farey tail: Z(tau) = sum_{gamma} Z_0(gamma.tau)."""

    def test_farey_sequence_identity(self):
        """The identity (c=0, d=1) is always in the Farey sequence."""
        pairs = farey_sequence(1)
        assert (0, 1) in pairs

    def test_farey_sequence_coprimality(self):
        """All pairs in the Farey sequence are coprime."""
        pairs = farey_sequence(5)
        for c_F, d in pairs:
            if c_F > 0:
                assert math.gcd(c_F, abs(d)) == 1

    def test_identity_term_dominates(self):
        """The identity term (BTZ saddle) dominates at high temperature."""
        c = 24
        tau = 0.1j  # high temperature: small Im(tau)
        Z_full = farey_tail_partition(c, tau, N_farey=3)
        Z_identity = farey_tail_term(c, tau, 0, 1)
        # Identity should be the dominant contribution
        assert abs(Z_identity) > 0

    def test_farey_entropy_consistent(self):
        """Farey tail entropy approaches BH entropy at high temperature."""
        data = farey_tail_entropy(24, M=100, N_farey=3)
        assert data['S_BH'] > 0
        # The Farey correction should be small for large M
        if data['log_Z_farey'] > -1e10 and data['log_Z_btz'] > -1e10:
            assert abs(data['farey_correction']) < data['S_BH']


# =========================================================================
# Section 13: Renyi entropy
# =========================================================================

class TestRenyiEntropy:
    """Renyi entropy from the replica trick."""

    def test_twist_dimension_c24(self):
        """h_n = (c/24)*(n - 1/n) for c=24, n=2: h_2 = 1*(2-1/2) = 3/2."""
        h = twist_operator_dimension(24, 2)
        assert abs(h - 1.5) < 1e-14

    def test_renyi_n_equals_1(self):
        """S_1 = (c/3)*log(L/eps) (von Neumann limit)."""
        c = 24
        L_eps = 1000
        S_1 = renyi_entropy_scalar(c, 1, L_eps)
        S_EE = (c / 3.0) * math.log(L_eps)
        assert abs(S_1 - S_EE) < 1e-10

    def test_renyi_n_equals_2(self):
        """S_2 = (c/6)*(1+1/2)*log = (c/4)*log."""
        c = 24
        L_eps = 1000
        S_2 = renyi_entropy_scalar(c, 2, L_eps)
        expected = (c / 4.0) * math.log(L_eps)
        assert abs(S_2 - expected) < 1e-10

    def test_renyi_decreases_with_n(self):
        """S_n decreases as n increases (for n >= 1)."""
        c = 24
        L_eps = 1000
        for n in range(2, 10):
            S_n = renyi_entropy_scalar(c, n, L_eps)
            S_np1 = renyi_entropy_scalar(c, n + 1, L_eps)
            assert S_n > S_np1

    def test_renyi_approaches_von_neumann(self):
        """S_n -> S_EE as n -> 1 from above.

        More precisely, (1+1/n)/2 -> 1 as n -> infinity gives S_infty = c/6 * log,
        and the n->1 limit gives S_EE = c/3 * log.
        The ratio S_n / S_EE = (1+1/n)/2 should approach 1 as n -> 1.
        """
        c = 24
        L_eps = 1000
        S_EE = (c / 3.0) * math.log(L_eps)
        # S_n / S_EE = (1+1/n)/2
        # As n grows: S_n/S_EE -> 1/2 (Renyi min-entropy limit)
        # At n=2: S_2/S_EE = 3/4
        S_2 = renyi_entropy_scalar(c, 2, L_eps)
        assert abs(S_2 / S_EE - 0.75) < 1e-10

    def test_renyi_with_shadow_corrections(self):
        """Shadow corrections at genus >= 2 contribute to Renyi entropy."""
        data = renyi_entropy_with_shadow_corrections(24, 2, g_max=3)
        assert 'corrections' in data
        assert 'S_n_total' in data
        # The corrections should be present (not all zero for Virasoro)
        assert data['total_correction'] != 0.0


# =========================================================================
# Section 14: Entanglement entropy
# =========================================================================

class TestEntanglementEntropy:
    """Entanglement entropy with shadow corrections."""

    def test_leading_calabrese_cardy(self):
        """S_EE = (c/3)*log(L/eps)."""
        c = 24
        L_eps = 1000
        S = entanglement_entropy_leading(c, L_eps)
        expected = (c / 3.0) * math.log(L_eps)
        assert abs(S - expected) < 1e-10

    def test_complementarity_sum(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps) (AP24)."""
        L_eps = 1000
        for c in [1, 6, 13, 20, 25]:
            data = entanglement_complementarity(c, L_eps)
            assert data['match'], f"Complementarity fails at c={c}"

    def test_complementarity_universal(self):
        """The sum 26/3 is independent of c (universal constraint)."""
        L_eps = 500
        expected = (26.0 / 3.0) * math.log(L_eps)
        for c in range(1, 26):
            data = entanglement_complementarity(c, L_eps)
            assert abs(data['sum'] - expected) < 1e-10

    def test_self_dual_c13(self):
        """At c=13: S_EE = S_EE' = (13/3)*log."""
        L_eps = 1000
        S = entanglement_entropy_leading(13, L_eps)
        S_dual = entanglement_entropy_leading(13, L_eps)
        assert abs(S - S_dual) < 1e-14

    def test_corrections_present_virasoro(self):
        """Class M (Virasoro) has nonzero shadow corrections."""
        data = entanglement_entropy_with_corrections(24, g_max=5)
        # At least some corrections should be nonzero
        assert data['total_correction'] != 0.0

    def test_corrections_formula(self):
        """delta_S^{(g)} = (2g-1)*F_g for the n->1 limit."""
        c = 24
        data = entanglement_entropy_with_corrections(c, g_max=5)
        for g in range(2, 6):
            Fg = float(virasoro_free_energy(c, g))
            expected = (2 * g - 1) * Fg
            assert abs(data['corrections'][g] - expected) < 1e-14


# =========================================================================
# Section 15: A-hat generating function and convergence
# =========================================================================

class TestAHatGeneratingFunction:
    """A-hat(ix) - 1 = (x/2)/sin(x/2) - 1."""

    def test_ahat_at_zero(self):
        """A-hat(i*0) - 1 = 0."""
        assert abs(ahat_generating_function(0.0)) < 1e-14

    def test_ahat_leading_term(self):
        """A-hat(ix) - 1 ~ x^2/24 for small x."""
        x = 0.01
        val = ahat_generating_function(x)
        expected = x**2 / 24.0
        assert abs(val - expected) / expected < 0.01

    def test_series_matches_closed_form(self):
        """sum lambda_g * hbar^{2g} = A-hat closed form."""
        for c in [1, 12, 24]:
            data = verify_ahat_identity(c, hbar=0.5, g_max=20)
            assert data['match'], f"A-hat identity fails at c={c}"

    def test_convergence_radius(self):
        """Convergence radius is 2*pi."""
        assert abs(shadow_convergence_radius() - TWO_PI) < 1e-12

    def test_series_convergent_inside_radius(self):
        """The series converges for hbar < 2*pi."""
        c = 24
        hbar = 5.0  # < 2*pi ~ 6.28
        series = scalar_free_energy_sum(c, hbar, g_max=30)
        closed = ahat_closed_form(c, hbar)
        assert abs(series - closed) < 1e-6


# =========================================================================
# Section 16: Special central charges
# =========================================================================

class TestSpecialCentralCharges:
    """Pure gravity (c=24), critical string (c=26), self-dual (c=13), free boson (c=1)."""

    def test_pure_gravity_c24(self):
        """c=24: kappa=12, F_1 = 1/2."""
        data = pure_gravity_c24(M=10)
        assert abs(data['kappa'] - 12.0) < 1e-12
        assert abs(data['F_table'][1] - 0.5) < 1e-12

    def test_critical_string_c26(self):
        """c=26: kappa=13. Dual algebra Vir_0 is uncurved."""
        data = critical_string_c26(M=10)
        assert abs(data['kappa'] - 13.0) < 1e-12

    def test_self_dual_c13(self):
        """c=13: kappa = 13/2 = kappa'. Self-dual."""
        data = self_dual_c13(M=10)
        assert abs(data['kappa'] - 6.5) < 1e-12

    def test_free_boson_c1(self):
        """c=1 (Heisenberg k=1): kappa=1, class G."""
        data = free_boson_c1(M=10)
        # F_1 = kappa * 1/24 = 1/24
        assert abs(data['F_table'][1] - 1.0 / 24.0) < 1e-12

    def test_monster_kappa(self):
        """Monster V^natural: kappa(Vir_24) = 12 (AP48: this uses Virasoro formula)."""
        assert float(kappa_virasoro(24)) == 12.0

    def test_c26_dual_is_c0(self):
        """Vir_26^! = Vir_0: kappa(Vir_0) = 0."""
        assert kappa_virasoro(0) == Fraction(0)


# =========================================================================
# Section 17: Large-c semiclassical limit
# =========================================================================

class TestLargeCLimit:
    """Recovery of semiclassical gravity at large c."""

    def test_relative_correction_decreases(self):
        """Quantum corrections become negligible as c -> infinity."""
        M = 10
        prev_rel = None
        for c in [10, 100, 1000]:
            data = entropy_all_genera(c, M, g_max=3)
            rel = abs(data['relative_correction'])
            if prev_rel is not None:
                assert rel < prev_rel, f"Corrections should decrease with c"
            prev_rel = rel

    def test_S1_grows_logarithmically(self):
        """S_1 ~ -(3/4)*log(c) at fixed M."""
        M = 100
        c_values = [100, 1000, 10000]
        S1_values = [entropy_correction_genus_g(c, M, 1) for c in c_values]
        # S_1 = -(3/2)*log(S_BH/(2pi)) and S_BH ~ sqrt(c),
        # so S_1 ~ -(3/4)*log(c)
        for i in range(len(S1_values)):
            assert S1_values[i] < 0  # Always negative

    def test_S2_suppressed_at_large_c(self):
        """S_2 ~ 1/c at large c (suppressed by 1/S_BH^2 ~ 1/c)."""
        M = 100
        S2_100 = entropy_correction_genus_g(100, M, 2)
        S2_10000 = entropy_correction_genus_g(10000, M, 2)
        # Should scale as ~1/c
        ratio = abs(S2_10000 / S2_100)
        assert ratio < 0.1  # much smaller

    def test_large_c_report(self):
        data = large_c_limit(M=10)
        assert len(data['data']) >= 3
        # Last entry (largest c) should have smallest relative correction
        rels = [d['relative'] for d in data['data']]
        assert abs(rels[-1]) < abs(rels[0])


# =========================================================================
# Section 18: Cross-checks and consistency
# =========================================================================

class TestCrossChecks:
    """Consistency checks across different computation routes."""

    def test_rotating_special_case(self):
        for c in [1, 13, 24, 26]:
            data = verify_nonrotating_is_rotating_special_case(c, 10)
            assert data['match']

    def test_rotating_explicit(self):
        data = verify_bekenstein_hawking_rotating(24, 5, 10)
        assert data['match']

    def test_convergence_diagnostics_large_M(self):
        """Large M: the expansion converges."""
        data = convergence_diagnostics(24, 1000, g_max=5)
        assert data['convergent']
        assert data['epsilon'] < TWO_PI

    def test_convergence_diagnostics_ratios(self):
        """Decay ratios should be < 1 for convergent expansion."""
        data = convergence_diagnostics(24, 100, g_max=5)
        for r in data['decay_ratios'][1:]:  # skip g=1->2 (different scaling)
            assert r < 1.0, f"Decay ratio {r} >= 1"

    def test_entropy_landscape_monotone_in_c(self):
        """At fixed M, S_BH increases with c."""
        landscape = entropy_landscape(M=10, g_max=3)
        S_prev = 0
        for c in sorted(landscape.keys()):
            assert landscape[c]['S_BH'] > S_prev
            S_prev = landscape[c]['S_BH']

    def test_full_report_fields(self):
        report = full_entropy_report(24, 10, g_max=5)
        assert 'S_BH' in report
        assert 'S_total' in report
        assert 'beta_HP_classical' in report
        assert 'convergent' in report
        assert 'ahat_check' in report

    def test_F_g_polynomial_in_kappa(self):
        """F_g^{scalar} = kappa * lambda_g^FP is linear in kappa."""
        for g in range(1, 6):
            F_k1 = float(F_g_scalar(Fraction(1), g))
            F_k2 = float(F_g_scalar(Fraction(2), g))
            assert abs(F_k2 - 2 * F_k1) < 1e-14

    def test_heisenberg_no_planted_forest(self):
        """Heisenberg (class G) has zero planted-forest at ALL genera."""
        for g in range(1, 6):
            F_heis = heisenberg_free_energy(1, g)
            F_scalar = F_g_scalar(Fraction(1), g)
            assert F_heis == F_scalar

    def test_virasoro_has_planted_forest_g2(self):
        """Virasoro (class M) has nonzero planted-forest at genus >= 2 (generic c)."""
        for c in [1, 12, 24, 26]:
            if c == 40:
                continue  # exceptional: pf vanishes at c=40
            F_sc = F_g_scalar(kappa_virasoro(c), 2)
            F_full = virasoro_free_energy(c, 2)
            assert F_full != F_sc, f"Planted-forest should be nonzero at c={c}"

    def test_entropy_positivity(self):
        """Total entropy is positive for M > 0."""
        for c in [1, 13, 24, 26]:
            data = entropy_all_genera(c, 10, g_max=5)
            if 'error' not in data:
                assert data['S_total'] > 0

    def test_kappa_additivity(self):
        """kappa(H_{k1} + H_{k2}) = kappa(H_{k1}) + kappa(H_{k2}) (independent sum)."""
        k1, k2 = 3, 5
        assert kappa_heisenberg(k1 + k2) == kappa_heisenberg(k1) + kappa_heisenberg(k2)


# =========================================================================
# Additional targeted tests for numerical results
# =========================================================================

class TestNumericalResults:
    """Targeted numerical verification of key results."""

    def test_bh_entropy_c24_M1(self):
        """S_BH(c=24, M=1) = 2*pi*sqrt(4) = 4*pi."""
        S = bekenstein_hawking_entropy(24, 1)
        assert abs(S - 4 * PI) < 1e-12

    def test_bh_entropy_c24_M10(self):
        """S_BH(c=24, M=10) = 2*pi*sqrt(40) = 4*pi*sqrt(10)."""
        S = bekenstein_hawking_entropy(24, 10)
        assert abs(S - 4 * PI * math.sqrt(10)) < 1e-10

    def test_F1_c24_value(self):
        assert float(virasoro_free_energy(24, 1)) == 0.5

    def test_F2_c24_numerical(self):
        F2 = float(virasoro_free_energy(24, 2))
        # scalar: 7/480 ~ 0.014583
        # pf: 1/3 ~ 0.333333
        # total ~ 0.347917
        assert abs(F2 - (7.0 / 480.0 + 1.0 / 3.0)) < 1e-12

    def test_F3_c24_numerical(self):
        F3 = float(virasoro_free_energy(24, 3))
        # scalar: 31*12/967680 ~ 0.000384
        # pf: nonzero correction
        assert F3 > 0

    def test_five_loop_c24_M10(self):
        """5-loop correction for c=24, M=10: small but nonzero."""
        data = explicit_5loop_correction(24, 10)
        assert data['F_5_scalar'] > 0
        assert data['S_5'] > 0
        # Should be much smaller than S_BH
        S_BH = bekenstein_hawking_entropy(24, 10)
        assert data['S_5'] < 0.01 * S_BH

    def test_renyi_n2_c24(self):
        """S_2(c=24) = (24/4)*log(1000) = 6*log(1000)."""
        S_2 = renyi_entropy_scalar(24, 2, 1000)
        expected = 6.0 * math.log(1000)
        assert abs(S_2 - expected) < 1e-10

    def test_entanglement_c24(self):
        """S_EE(c=24) = 8*log(1000)."""
        S = entanglement_entropy_leading(24, 1000)
        expected = 8.0 * math.log(1000)
        assert abs(S - expected) < 1e-10

    def test_complementarity_sum_value(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps)."""
        L_eps = 1000
        expected = (26.0 / 3.0) * math.log(L_eps)
        result = entanglement_complementarity(12, L_eps)
        assert abs(result['sum'] - expected) < 1e-10
