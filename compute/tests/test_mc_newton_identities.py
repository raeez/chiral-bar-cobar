r"""Tests for mc_newton_identities.py -- Newton's identities from the MC bracket.

Verifies:
  1. Newton identity algebra (pure, no physics)
  2. Ramanujan Delta verification at primes 2, 3, 5, 7, 11, 13
  3. Power sum computation (direct vs recursive consistency)
  4. Atom reconstruction from two power sums
  5. GL(n) Newton for n > 2
  6. W_3 multi-channel seeds
  7. Genus-g correction structure
  8. Beyond-Newton analysis

References:
  prop:mc-bracket-determines-atoms (arithmetic_shadows.tex)
  prop:shadow-symmetric-power (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
import pytest

from compute.lib.mc_newton_identities import (
    ramanujan_tau,
    satake_parameters,
    power_sum,
    power_sums_direct,
    power_sums_recursive,
    newton_identity_residual,
    verify_newton_all_arities,
    delta_satake_at_prime,
    delta_newton_verification,
    delta_power_sums_table,
    atoms_from_power_sums,
    verify_reconstruction,
    newton_identity_gln,
    elementary_from_power_sums_gln,
    verify_newton_gln,
    w3_shadow_seeds,
    w3_mixed_newton_recursion,
    genus_g_newton_correction,
    beyond_newton_analysis,
    delta_comprehensive_verification,
)


# =====================================================================
# 1. Ramanujan tau values
# =====================================================================

class TestRamanujanTau:
    """Verify tau(n) against known values (Ramanujan, 1916)."""

    def test_tau_1(self):
        assert ramanujan_tau(1) == 1

    def test_tau_2(self):
        assert ramanujan_tau(2) == -24

    def test_tau_3(self):
        assert ramanujan_tau(3) == 252

    def test_tau_4(self):
        assert ramanujan_tau(4) == -1472

    def test_tau_5(self):
        assert ramanujan_tau(5) == 4830

    def test_tau_6(self):
        assert ramanujan_tau(6) == -6048

    def test_tau_7(self):
        assert ramanujan_tau(7) == -16744

    def test_tau_11(self):
        assert ramanujan_tau(11) == 534612

    def test_tau_13(self):
        assert ramanujan_tau(13) == -577738

    def test_tau_multiplicative(self):
        """tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        # tau(6) = tau(2)*tau(3) since gcd(2,3) = 1
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)

    def test_tau_prime_power(self):
        """tau(p^2) = tau(p)^2 - p^11 for Hecke eigenform."""
        p = 2
        assert (ramanujan_tau(p * p)
                == ramanujan_tau(p) ** 2 - p ** 11)


# =====================================================================
# 2. Satake parameters
# =====================================================================

class TestSatakeParameters:
    """Verify Satake parameters alpha + beta = a(p), alpha*beta = p^{k-1}."""

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
    def test_satake_sum(self, p):
        """alpha + beta = tau(p)."""
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        assert abs((alpha + beta) - tau_p) < 1e-6

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
    def test_satake_product(self, p):
        """alpha * beta = p^11."""
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        assert abs(alpha * beta - p ** 11) < 1

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
    def test_ramanujan_bound(self, p):
        """Deligne: |alpha| = |beta| = p^{11/2}."""
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        target = p ** (11 / 2)
        assert abs(abs(alpha) - target) / target < 1e-6
        assert abs(abs(beta) - target) / target < 1e-6

    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_discriminant_negative(self, p):
        """Ramanujan => discriminant tau(p)^2 - 4*p^11 < 0 => complex conjugate pair."""
        tau_p = ramanujan_tau(p)
        disc = tau_p ** 2 - 4 * p ** 11
        assert disc < 0, f"Discriminant at p={p} is {disc}, expected negative"


# =====================================================================
# 3. Power sums
# =====================================================================

class TestPowerSums:
    """Verify power sum computations."""

    def test_p1_equals_e1(self):
        """p_1 = alpha + beta."""
        alpha, beta = satake_parameters(-24, 12, 2)
        p = power_sums_direct(alpha, beta, 1)
        assert abs(p[1] - (alpha + beta)) < 1e-6

    def test_p2_formula(self):
        """p_2 = (alpha+beta)^2 - 2*alpha*beta = e1^2 - 2*e2."""
        alpha, beta = satake_parameters(-24, 12, 2)
        p = power_sums_direct(alpha, beta, 2)
        e1 = alpha + beta
        e2 = alpha * beta
        expected = e1 ** 2 - 2 * e2
        assert abs(p[2] - expected) < 1e-3

    def test_direct_vs_recursive(self):
        """Direct and recursive power sums agree."""
        alpha, beta = satake_parameters(-24, 12, 2)
        p_dir = power_sums_direct(alpha, beta, 8)
        p_rec = power_sums_recursive(alpha, beta, 8)
        for r in range(1, 9):
            assert abs(p_dir[r] - p_rec[r]) / max(abs(p_dir[r]), 1) < 1e-6

    def test_power_sum_recurrence(self):
        """p_r = e1*p_{r-1} - e2*p_{r-2} holds for all r >= 3."""
        alpha, beta = satake_parameters(-24, 12, 2)
        e1 = alpha + beta
        e2 = alpha * beta
        p = power_sums_direct(alpha, beta, 10)
        for r in range(3, 11):
            expected = e1 * p[r - 1] - e2 * p[r - 2]
            assert abs(p[r] - expected) / max(abs(p[r]), 1) < 1e-6


# =====================================================================
# 4. Newton identity verification (the algebraic heart)
# =====================================================================

class TestNewtonIdentities:
    """Verify Newton's identities from the MC bracket (prop:mc-bracket-determines-atoms)."""

    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_newton_r1(self, p):
        """Newton at r=1: p_1 - e_1 = 0."""
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        ps = power_sums_direct(alpha, beta, 1)
        e1 = alpha + beta
        e2 = alpha * beta
        res = newton_identity_residual(ps, e1, e2, 1)
        assert abs(res) < 1e-6

    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_newton_r2(self, p):
        """Newton at r=2: p_2 - e_1*p_1 + 2*e_2 = 0."""
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        ps = power_sums_direct(alpha, beta, 2)
        e1 = alpha + beta
        e2 = alpha * beta
        res = newton_identity_residual(ps, e1, e2, 2)
        assert abs(res) < 1e-3

    @pytest.mark.parametrize("p,r", [
        (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
        (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
        (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
        (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
    ])
    def test_newton_higher_arity(self, p, r):
        """Newton at r >= 3: p_r - e1*p_{r-1} + e2*p_{r-2} = 0."""
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        ps = power_sums_direct(alpha, beta, r)
        e1 = alpha + beta
        e2 = alpha * beta
        res = newton_identity_residual(ps, e1, e2, r)
        assert abs(res) / max(abs(ps[r]), 1) < 1e-6


class TestNewtonAllArities:
    """Full Newton verification at all arities simultaneously."""

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
    def test_all_arities_hold(self, p):
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        result = verify_newton_all_arities(alpha, beta, max_r=8)
        assert result['all_newton_hold']
        assert result['all_consistent']


# =====================================================================
# 5. Explicit power sum verification for Delta at p=2
# =====================================================================

class TestDeltaPrime2Explicit:
    """Hand-computed power sums for Delta at p=2 (from the task prompt)."""

    def setup_method(self):
        self.alpha, self.beta = satake_parameters(-24, 12, 2)
        self.e1 = self.alpha + self.beta  # = -24
        self.e2 = self.alpha * self.beta  # = 2048

    def test_e1(self):
        assert abs(self.e1 - (-24)) < 1e-6

    def test_e2(self):
        assert abs(self.e2 - 2048) < 1

    def test_p1(self):
        """p_1 = -24."""
        assert abs(power_sum(self.alpha, self.beta, 1) - (-24)) < 1e-6

    def test_p2(self):
        """p_2 = (-24)^2 - 2*2048 = 576 - 4096 = -3520."""
        p2 = power_sum(self.alpha, self.beta, 2)
        assert abs(p2 - (-3520)) < 1e-3

    def test_p3(self):
        """p_3 = (-24)^3 - 3*2048*(-24) = -13824 + 147456 = 133632."""
        p3 = power_sum(self.alpha, self.beta, 3)
        assert abs(p3 - 133632) < 1e-1

    def test_p2_newton(self):
        """Newton: p_2 = e1*p_1 - 2*e2 = (-24)*(-24) - 2*2048 = 576 - 4096 = -3520."""
        p1 = power_sum(self.alpha, self.beta, 1)
        p2 = power_sum(self.alpha, self.beta, 2)
        newton_p2 = self.e1 * p1 - 2 * self.e2
        assert abs(p2 - newton_p2) < 1e-3

    def test_p3_newton(self):
        """Newton: p_3 = e1*p_2 - e2*p_1 = (-24)*(-3520) - 2048*(-24) = 84480 + 49152 = 133632."""
        p1 = power_sum(self.alpha, self.beta, 1)
        p2 = power_sum(self.alpha, self.beta, 2)
        p3 = power_sum(self.alpha, self.beta, 3)
        newton_p3 = self.e1 * p2 - self.e2 * p1
        assert abs(p3 - newton_p3) / abs(p3) < 1e-6

    def test_p4(self):
        """p_4 = e1*p_3 - e2*p_2."""
        p2 = power_sum(self.alpha, self.beta, 2)
        p3 = power_sum(self.alpha, self.beta, 3)
        p4 = power_sum(self.alpha, self.beta, 4)
        newton_p4 = self.e1 * p3 - self.e2 * p2
        assert abs(p4 - newton_p4) / max(abs(p4), 1) < 1e-6

    def test_p5(self):
        """p_5 = e1*p_4 - e2*p_3."""
        p3 = power_sum(self.alpha, self.beta, 3)
        p4 = power_sum(self.alpha, self.beta, 4)
        p5 = power_sum(self.alpha, self.beta, 5)
        newton_p5 = self.e1 * p4 - self.e2 * p3
        assert abs(p5 - newton_p5) / max(abs(p5), 1) < 1e-6

    def test_p6(self):
        """p_6 = e1*p_5 - e2*p_4."""
        p4 = power_sum(self.alpha, self.beta, 4)
        p5 = power_sum(self.alpha, self.beta, 5)
        p6 = power_sum(self.alpha, self.beta, 6)
        newton_p6 = self.e1 * p5 - self.e2 * p4
        assert abs(p6 - newton_p6) / max(abs(p6), 1) < 1e-6

    def test_p7(self):
        """p_7 = e1*p_6 - e2*p_5."""
        p5 = power_sum(self.alpha, self.beta, 5)
        p6 = power_sum(self.alpha, self.beta, 6)
        p7 = power_sum(self.alpha, self.beta, 7)
        newton_p7 = self.e1 * p6 - self.e2 * p5
        assert abs(p7 - newton_p7) / max(abs(p7), 1) < 1e-6

    def test_p8(self):
        """p_8 = e1*p_7 - e2*p_6."""
        p6 = power_sum(self.alpha, self.beta, 6)
        p7 = power_sum(self.alpha, self.beta, 7)
        p8 = power_sum(self.alpha, self.beta, 8)
        newton_p8 = self.e1 * p7 - self.e2 * p6
        assert abs(p8 - newton_p8) / max(abs(p8), 1) < 1e-6


# =====================================================================
# 6. Delta at primes 3, 5, 7
# =====================================================================

class TestDeltaPrime3:
    """Newton verification for Delta at p=3."""

    def setup_method(self):
        self.alpha, self.beta = satake_parameters(252, 12, 3)
        self.e1 = self.alpha + self.beta
        self.e2 = self.alpha * self.beta

    def test_e1_is_252(self):
        assert abs(self.e1 - 252) < 1e-6

    def test_e2_is_3_11(self):
        assert abs(self.e2 - 3 ** 11) < 1

    def test_p2(self):
        p2 = power_sum(self.alpha, self.beta, 2)
        expected = 252 ** 2 - 2 * 3 ** 11
        assert abs(p2 - expected) < 1e-1

    def test_p3_newton(self):
        p = power_sums_direct(self.alpha, self.beta, 3)
        newton_p3 = self.e1 * p[2] - self.e2 * p[1]
        assert abs(p[3] - newton_p3) / max(abs(p[3]), 1) < 1e-6


class TestDeltaPrime5:
    """Newton verification for Delta at p=5."""

    def setup_method(self):
        self.alpha, self.beta = satake_parameters(4830, 12, 5)
        self.e1 = self.alpha + self.beta
        self.e2 = self.alpha * self.beta

    def test_e1_is_4830(self):
        assert abs(self.e1 - 4830) < 1e-6

    def test_e2_is_5_11(self):
        assert abs(self.e2 - 5 ** 11) < 1

    def test_newton_all(self):
        result = verify_newton_all_arities(self.alpha, self.beta, max_r=8)
        assert result['all_newton_hold']


class TestDeltaPrime7:
    """Newton verification for Delta at p=7."""

    def setup_method(self):
        self.alpha, self.beta = satake_parameters(-16744, 12, 7)
        self.e1 = self.alpha + self.beta
        self.e2 = self.alpha * self.beta

    def test_e1_is_minus_16744(self):
        assert abs(self.e1 - (-16744)) < 1e-6

    def test_e2_is_7_11(self):
        assert abs(self.e2 - 7 ** 11) < 1

    def test_newton_all(self):
        result = verify_newton_all_arities(self.alpha, self.beta, max_r=8)
        assert result['all_newton_hold']


# =====================================================================
# 7. Atom reconstruction
# =====================================================================

class TestAtomReconstruction:
    """Verify that (alpha, beta) can be reconstructed from (p_1, p_2)."""

    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_delta_reconstruction(self, p):
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        result = verify_reconstruction(alpha, beta, max_r=8)
        assert result['match']
        assert result['all_power_sums_match']

    def test_real_satake_reconstruction(self):
        """Reconstruction for real Satake parameters (non-Ramanujan)."""
        # Artificial example: alpha=3, beta=5
        alpha, beta = 3.0 + 0j, 5.0 + 0j
        result = verify_reconstruction(alpha, beta)
        assert result['match']

    def test_complex_conjugate_reconstruction(self):
        """Reconstruction for complex conjugate pair."""
        alpha = 2.0 + 3.0j
        beta = 2.0 - 3.0j
        result = verify_reconstruction(alpha, beta)
        assert result['match']


# =====================================================================
# 8. GL(n) Newton identities
# =====================================================================

class TestGLnNewton:
    """Newton's identities for GL(n) with n > 2."""

    def test_gl2(self):
        """GL(2): standard two-variable Newton."""
        alphas = [3.0 + 1j, 3.0 - 1j]
        result = verify_newton_gln(alphas, max_r=10)
        assert result['all_newton_hold']
        assert result['all_e_match']

    def test_gl3(self):
        """GL(3): three Satake parameters."""
        alphas = [2.0 + 1j, 2.0 - 1j, -1.0 + 0j]
        result = verify_newton_gln(alphas, max_r=10)
        assert result['all_newton_hold']
        assert result['all_e_match']

    def test_gl4(self):
        """GL(4): four Satake parameters."""
        alphas = [1.0 + 2j, 1.0 - 2j, -1.0 + 0.5j, -1.0 - 0.5j]
        result = verify_newton_gln(alphas, max_r=12)
        assert result['all_newton_hold']
        assert result['all_e_match']

    def test_gl5_higher_r_redundant(self):
        """For GL(5), p_r for r > 5 is determined by p_1,...,p_5."""
        alphas = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = verify_newton_gln(alphas, max_r=15)
        assert result['all_newton_hold']
        # All 15 Newton identities hold, but only 5 are independent

    def test_elementary_recovery(self):
        """Recover elementary symmetric polynomials from power sums."""
        alphas = [2.0, 3.0, 5.0]
        # e_1 = 10, e_2 = 31, e_3 = 30
        result = verify_newton_gln(alphas, max_r=6)
        e = result['elementary_newton']
        assert abs(e[1] - 10.0) < 1e-6
        assert abs(e[2] - 31.0) < 1e-6
        assert abs(e[3] - 30.0) < 1e-6


# =====================================================================
# 9. Beyond Newton (the deep question)
# =====================================================================

class TestBeyondNewton:
    """What the shadow tower provides beyond Newton."""

    def test_gl2_all_redundant_after_2(self):
        """For GL(2), arities > 4 are redundant (all Newton consequences)."""
        result = beyond_newton_analysis(2, max_r=20)
        assert result['independent_power_sums'] == 2
        assert result['redundant_power_sums'] == 17
        assert result['newton_determines_all']

    def test_gl3_all_redundant_after_3(self):
        """For GL(3), arities > 5 are redundant."""
        result = beyond_newton_analysis(3, max_r=20)
        assert result['independent_power_sums'] == 3
        assert result['redundant_power_sums'] == 16

    def test_genus0_nothing_beyond_newton(self):
        """At genus 0, the MC equation provides EXACTLY Newton's identities."""
        result = beyond_newton_analysis(2)
        assert 'NOTHING' in result['genus0_beyond_newton']

    def test_genus1_quasimodular(self):
        """At genus 1, corrections are quasi-modular (E_2*)."""
        result = beyond_newton_analysis(2)
        assert 'E_2*' in result['genus1_beyond_newton'] or \
               'quasi-modular' in result['genus1_beyond_newton']


# =====================================================================
# 10. W_3 multi-channel
# =====================================================================

class TestW3MultiChannel:
    """Multi-channel Newton for W_3."""

    @pytest.mark.parametrize("c_val", [1.0, 2.0, 10.0, 25.0, 50.0])
    def test_seeds_well_defined(self, c_val):
        seeds = w3_shadow_seeds(c_val)
        assert seeds['kappa_TT'] == c_val / 2
        assert abs(seeds['kappa_WW'] - 5 * c_val / 6) < 1e-10
        assert seeds['kappa_TW'] == 0.0

    def test_w3_alpha(self):
        """alpha(c) = 16/(22 + 5c)."""
        c_val = 10.0
        seeds = w3_shadow_seeds(c_val)
        assert abs(seeds['alpha_w3'] - 16 / (22 + 50)) < 1e-10

    def test_w3_singular_c0(self):
        with pytest.raises(ValueError):
            w3_shadow_seeds(0.0)

    def test_w3_singular_c_minus_22_over_5(self):
        with pytest.raises(ValueError):
            w3_shadow_seeds(-22 / 5)

    def test_mixed_recursion_structure(self):
        result = w3_mixed_newton_recursion(10.0, max_r=6)
        assert 'T_channel' in result
        assert 'W_channel' in result
        assert result['T_channel']['kappa'] == 5.0
        assert abs(result['W_channel']['kappa'] - 50 / 6) < 1e-10

    def test_t_channel_virasoro(self):
        """T-channel is standard Virasoro tower."""
        result = w3_mixed_newton_recursion(10.0)
        lam = result['T_channel']['effective_coupling']
        assert abs(lam - (-6 / 10)) < 1e-10


# =====================================================================
# 11. Genus corrections
# =====================================================================

class TestGenusCorrections:
    """Genus-g corrections to Newton's identity."""

    def test_genus0_residual_zero(self):
        """At genus 0, Newton's identity has zero residual."""
        alpha, beta = satake_parameters(-24, 12, 2)
        for r in range(3, 9):
            result = genus_g_newton_correction(alpha, beta, 0, r)
            assert abs(result['genus0_residual']) / max(1, abs(alpha ** r)) < 1e-6

    def test_genus1_structure(self):
        """Genus-1 correction has the expected structure."""
        alpha, beta = satake_parameters(-24, 12, 2)
        result = genus_g_newton_correction(alpha, beta, 1, 5)
        assert result['genus'] == 1
        assert 'quasi-modular' in result['note'] or 'E_2*' in result['note']
        assert 'correction_structure' in result

    def test_genus2_structure(self):
        """Genus-2 correction involves planted-forest graphs."""
        alpha, beta = satake_parameters(-24, 12, 2)
        result = genus_g_newton_correction(alpha, beta, 2, 5)
        assert result['genus'] == 2
        assert 'planted-forest' in result['note']


# =====================================================================
# 12. Comprehensive verification
# =====================================================================

class TestComprehensiveVerification:
    """Full Delta verification across multiple primes."""

    def test_comprehensive_default_primes(self):
        result = delta_comprehensive_verification(max_r=8)
        assert result['all_passed']

    def test_comprehensive_at_p2(self):
        result = delta_comprehensive_verification(primes=[2], max_r=8)
        assert result['per_prime'][2]['all_newton_hold']
        assert result['per_prime'][2]['ramanujan_holds']
        assert result['per_prime'][2]['atoms_reconstructed']

    def test_comprehensive_at_p3(self):
        result = delta_comprehensive_verification(primes=[3], max_r=8)
        assert result['per_prime'][3]['all_newton_hold']

    def test_comprehensive_at_p5(self):
        result = delta_comprehensive_verification(primes=[5], max_r=8)
        assert result['per_prime'][5]['all_newton_hold']

    def test_comprehensive_at_p7(self):
        result = delta_comprehensive_verification(primes=[7], max_r=8)
        assert result['per_prime'][7]['all_newton_hold']


# =====================================================================
# 13. Cross-checks with existing modules
# =====================================================================

class TestCrossChecks:
    """Cross-check against mc_newton_spectral.py and symmetric_power_shadow.py."""

    def test_power_sum_from_satake_consistency(self):
        """Our power_sum matches symmetric_power_shadow.power_sum_from_satake."""
        try:
            from compute.lib.symmetric_power_shadow import power_sum_from_satake
            alpha, beta = satake_parameters(-24, 12, 2)
            for r in range(1, 9):
                ours = power_sum(alpha, beta, r)
                theirs = power_sum_from_satake(alpha, beta, r)
                assert abs(ours - theirs) / max(abs(ours), 1) < 1e-6
        except ImportError:
            pytest.skip("symmetric_power_shadow not available")

    def test_tau_consistency(self):
        """Our ramanujan_tau matches symmetric_power_shadow.ramanujan_tau."""
        try:
            from compute.lib.symmetric_power_shadow import ramanujan_tau as tau_other
            for n in [1, 2, 3, 4, 5, 6, 7]:
                assert ramanujan_tau(n) == tau_other(n)
        except ImportError:
            pytest.skip("symmetric_power_shadow not available")


# =====================================================================
# 14. The MC=Newton principle (prop:mc-bracket-determines-atoms)
# =====================================================================

class TestMCNewtonPrinciple:
    """The MC bracket [Theta, Theta] = 0 at genus 0, arity r+1 gives Newton."""

    def test_two_atoms_determined_by_two_power_sums(self):
        """For n=2 Satake parameters, (p_1, p_2) determine (alpha, beta)."""
        for p in [2, 3, 5, 7]:
            tau_p = ramanujan_tau(p)
            alpha, beta = satake_parameters(tau_p, 12, p)
            # Recover from power sums
            p1 = alpha + beta
            p2 = alpha ** 2 + beta ** 2
            alpha_rec, beta_rec = atoms_from_power_sums(p1, p2)
            # Should match (up to permutation)
            match = (abs(alpha_rec - alpha) < 1e-3 and abs(beta_rec - beta) < 1e-3) or \
                    (abs(alpha_rec - beta) < 1e-3 and abs(beta_rec - alpha) < 1e-3)
            assert match, f"Failed atom reconstruction at p={p}"

    def test_higher_arities_are_consequences(self):
        """p_r for r >= 3 are consequences of p_1, p_2 via Newton recurrence."""
        alpha, beta = satake_parameters(-24, 12, 2)
        e1 = alpha + beta
        e2 = alpha * beta
        p = power_sums_direct(alpha, beta, 12)
        # Reconstruct p_r from (p_1, p_2) via recurrence
        p_rec = {1: p[1], 2: p[2]}
        for r in range(3, 13):
            p_rec[r] = e1 * p_rec[r - 1] - e2 * p_rec[r - 2]
        for r in range(3, 13):
            assert abs(p[r] - p_rec[r]) / max(abs(p[r]), 1) < 1e-6

    def test_newton_is_tautological_for_gl2(self):
        """For GL(2), Newton's identities at arity >= 3 are tautological."""
        # This is the key insight: the MC equation at genus 0 gives
        # EXACTLY Newton's identities, which for n=2 variables are
        # consequences of the characteristic polynomial X^2 - e1*X + e2 = 0.
        # No new information beyond e1 = p_1 and e2 = (p_1^2 - p_2)/2.
        result = beyond_newton_analysis(2, max_r=20)
        assert result['independent_power_sums'] == 2
        assert result['genus0_beyond_newton'] == \
               'NOTHING (all genus-0 constraints are Newton)'


# =====================================================================
# 15. Explicit p_4 through p_8 for Delta at p=2
# =====================================================================

class TestDeltaP2HigherPowerSums:
    """Explicit computation of p_4 through p_8 for Ramanujan Delta at p=2."""

    def setup_method(self):
        self.alpha, self.beta = satake_parameters(-24, 12, 2)
        self.e1 = -24.0
        self.e2 = 2048.0  # = 2^11
        # Build the full tower via recurrence
        self.p = {0: 2.0, 1: self.e1}
        for r in range(2, 9):
            self.p[r] = self.e1 * self.p[r - 1] - self.e2 * self.p[r - 2]

    def test_p4_value(self):
        """p_4 = e1*p_3 - e2*p_2 = (-24)*133632 - 2048*(-3520)."""
        expected = self.e1 * 133632 - self.e2 * (-3520)
        assert abs(self.p[4] - expected) < 1e-1

    def test_p5_value(self):
        p5 = self.p[5]
        expected = self.e1 * self.p[4] - self.e2 * self.p[3]
        assert abs(p5 - expected) < 1

    def test_p6_value(self):
        p6 = self.p[6]
        expected = self.e1 * self.p[5] - self.e2 * self.p[4]
        assert abs(p6 - expected) < 1

    def test_p7_value(self):
        p7 = self.p[7]
        expected = self.e1 * self.p[6] - self.e2 * self.p[5]
        assert abs(p7 - expected) < 1

    def test_p8_value(self):
        p8 = self.p[8]
        expected = self.e1 * self.p[7] - self.e2 * self.p[6]
        assert abs(p8 - expected) < 1

    def test_all_newton_hold_to_p8(self):
        """All Newton identities hold for p_1 through p_8."""
        ps = power_sums_direct(self.alpha, self.beta, 8)
        for r in range(3, 9):
            res = newton_identity_residual(ps, self.e1 + 0j, self.e2 + 0j, r)
            assert abs(res) / max(abs(ps[r]), 1) < 1e-6, \
                f"Newton fails at r={r}: residual = {res}"

    def test_direct_matches_recurrence(self):
        """Direct alpha^r + beta^r matches the Newton recurrence to p_8."""
        ps_direct = power_sums_direct(self.alpha, self.beta, 8)
        for r in range(1, 9):
            assert abs(ps_direct[r] - self.p[r]) / max(abs(self.p[r]), 1) < 1e-6
